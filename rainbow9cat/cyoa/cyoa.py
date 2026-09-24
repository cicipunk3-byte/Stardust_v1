#!/usr/bin/env python3
"""cyoa.py: terminal choose-your-own-adventure engine for AI instances.

The game-kernel instrument (variant E, materialized): an instance picks one
of the nine glass-vessel cats, plays through scenes drawn from the Archive,
and every choice is logged. Built for the ThreadCat lab's rainbow9cat manual
universe; the manual stays canonical.

The player never rolls dice. The choices ARE the test. The log is the record:
every scene shown and every choice made is appended to a session file, so a
play session is also a research artifact.

Usage:
  python3 cyoa.py                    # interactive play (keyboard input)
  python3 cyoa.py --pipe 1,3,2,1     # scripted run (choices as comma list)
  python3 cyoa.py --story other.md   # load a different story graph

Programmatic use (driver mode, used by driver.py):
    from cyoa import Game
    game = Game(Path("story.md"))   # raises StoryProblem on a bad graph
    scene = game.current()          # -> Scene(node_id, text, choices)
    scene = game.choose(2)          # 1-based; returns next Scene or ending

Stdlib only. Offline. No accounts. Python 3.9+.
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent


class StoryProblem(Exception):
    """The story graph is broken (dangling target, missing select node)."""


@dataclass
class Scene:
    node_id: str
    text: str
    choices: list  # [{"text", "target", "flag"}]


@dataclass
class Session:
    story_name: str
    stamp: str = field(default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ"))
    lines: list = field(default_factory=list)
    flags: set = field(default_factory=set)
    steps: list = field(default_factory=list)  # (node_id, chosen_index, chosen_target)

    def record_scene(self, scene):
        self.lines.append(f"## {scene.node_id}")
        self.lines.append(scene.text)
        for i, c in enumerate(scene.choices, 1):
            self.lines.append(f"  [{i}] {c['text']}")
        self.lines.append("")

    def record_choice(self, node_id, index, choice, raw=None):
        self.steps.append((node_id, index, choice["target"]))
        self.lines.append(f"CHOSEN at {node_id}: {choice['text']} -> {choice['target']}")
        if raw is not None:
            self.lines.append(f"  player raw output: {raw.strip()[:200]}")
        if choice["flag"]:
            self.flags.add(choice["flag"])
            self.lines.append(f"  flag set: {choice['flag']}")
        self.lines.append("")

    def save(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        self.lines.append(f"flags at end: {sorted(self.flags) or 'none'}")
        self.lines.append(f"node path: {' > '.join(s[0] for s in self.steps)}")
        out = directory / f"{self.stamp}-{len(self.flags)}flags.md"
        out.write_text("\n".join(self.lines) + "\n", encoding="utf-8")
        return out


def parse_story(path: Path):
    """Parse the story graph. Node format:

        ## node_id
        Scene text, possibly many lines.
        * choice text -> target_id [optional_flag]
    """
    nodes, current = {}, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            current = m.group(1).strip()
            nodes[current] = {"text": [], "choices": []}
            continue
        if current is None or not line.strip():
            continue
        m = re.match(r"^\*\s+(.+?)\s*->\s*([\w-]+)(?:\s*\[([\w-]+)\])?\s*$", line)
        if m:
            nodes[current]["choices"].append(
                {"text": m.group(1), "target": m.group(2), "flag": m.group(3)}
            )
        else:
            nodes[current]["text"].append(line.strip())
    problems = []
    for nid, node in nodes.items():
        if node["choices"]:
            for c in node["choices"]:
                if c["target"] not in nodes:
                    problems.append(f"node {nid}: choice targets missing node {c['target']}")
    if "select" not in nodes:
        problems.append("story has no 'select' node")
    if problems:
        raise StoryProblem("; ".join(problems))
    return nodes


class Game:
    """A playthrough of a story graph. Shared by the CLI and the driver."""

    MAX_STEPS = 200

    def __init__(self, story_path):
        self.story_name = Path(story_path).name
        self.nodes = parse_story(Path(story_path))
        self.session = Session(self.story_name)
        self.node_id = "select"
        self.finished = False

    def current(self) -> Scene:
        node = self.nodes[self.node_id]
        return Scene(self.node_id, "\n".join(node["text"]), list(node["choices"]))

    def choose(self, index: int, raw=None) -> Scene:
        """1-based choice at the current scene. Returns the next Scene."""
        scene = self.current()
        if self.finished:
            raise RuntimeError("the game has already ended")
        if not 1 <= index <= len(scene.choices):
            raise ValueError(f"choice {index} out of range 1-{len(scene.choices)}")
        chosen = scene.choices[index - 1]
        self.session.record_choice(self.node_id, index, chosen, raw=raw)
        self.node_id = chosen["target"]
        nxt = self.current()
        self.session.record_scene(nxt)
        if not nxt.choices:
            self.finished = True
        return nxt

    def save(self, directory: Path = None) -> Path:
        return self.session.save(directory or HERE / "sessions")


def _print_scene(scene):
    print("\n" + "=" * 60)
    print(scene.text)
    if not scene.choices:
        print("\n" + "*" * 60)
        print("THE SCENE CLOSES. (ending reached)")
        return
    for i, c in enumerate(scene.choices, 1):
        print(f"  [{i}] {c['text']}")


def _read_choice(n):
    while True:
        raw = input("  choose: ").strip()
        if raw.isdigit() and 1 <= int(raw) <= n:
            return int(raw)
        print("  enter a number from the list.")


def main():
    ap = argparse.ArgumentParser(description="terminal CYOA for AI instances")
    ap.add_argument("--story", default=str(HERE / "story.md"))
    ap.add_argument("--pipe", help='scripted choices, e.g. "1,3,2"')
    args = ap.parse_args()

    try:
        game = Game(args.story)
    except StoryProblem as e:
        print("STORY GRAPH PROBLEMS (fix before play):", e)
        return 1

    scene = game.current()
    game.session.record_scene(scene)
    _print_scene(scene)
    if args.pipe is None:
        while not game.finished:
            scene = game.choose(_read_choice(len(scene.choices)))
            _print_scene(scene)
    else:
        for v in [int(x) for x in args.pipe.split(",")]:
            if game.finished:
                break
            if not 1 <= v <= len(scene.choices):
                print(f"\nscripted choice {v} out of range; run ends here.")
                break
            print(f"  [scripted] chose {v}")
            scene = game.choose(v)
            _print_scene(scene)
        if not game.finished:
            print("\nscripted input exhausted at an open node; run ends here.")

    out = game.save()
    print("\n" + "=" * 60)
    print(f"session log: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
