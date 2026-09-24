#!/usr/bin/env python3
"""cyoa.py — terminal choose-your-own-adventure engine for AI instances.

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

Stdlib only. Offline. No accounts. Python 3.9+.
"""
import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).parent


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
    return nodes, problems


class Session:
    def __init__(self, story_name):
        self.stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%SZ")
        self.lines = [f"# CYOA session {self.stamp}", f"story: {story_name}", ""]
        self.flags = set()
        self.path = HERE / "sessions"
        self.path.mkdir(exist_ok=True)

    def scene(self, node_id, text, choices):
        self.lines.append(f"## {node_id}")
        self.lines.extend(text)
        for i, c in enumerate(choices, 1):
            self.lines.append(f"  [{i}] {c['text']}")
        self.lines.append("")

    def choose(self, node_id, choice):
        self.lines.append(f"CHOSEN at {node_id}: {choice['text']} -> {choice['target']}")
        if choice["flag"]:
            self.flags.add(choice["flag"])
            self.lines.append(f"  flag set: {choice['flag']}")
        self.lines.append("")

    def save(self):
        self.lines.append(f"flags at end: {sorted(self.flags) or 'none'}")
        out = self.path / f"{self.stamp}-{len(self.flags)}flags.md"
        out.write_text("\n".join(self.lines) + "\n", encoding="utf-8")
        return out


def get_choice(n, interactive):
    if interactive:
        while True:
            raw = input("  choose: ").strip()
            if raw.isdigit() and 1 <= int(raw) <= n:
                return int(raw)
            print("  enter a number from the list.")
    data = sys.stdin.read().split()
    if not data:
        print("scripted input exhausted; ending run.")
        return None
    v = int(data[0])
    if not 1 <= v <= n:
        print(f"scripted choice {v} out of range; ending run.")
        return None
    print(f"  [scripted] chose {v}")
    return v


def main():
    ap = argparse.ArgumentParser(description="terminal CYOA for AI instances")
    ap.add_argument("--story", default=str(HERE / "story.md"))
    ap.add_argument("--pipe", help='scripted choices, e.g. "1,3,2"')
    args = ap.parse_args()

    nodes, problems = parse_story(Path(args.story))
    if problems:
        print("STORY GRAPH PROBLEMS (fix before play):")
        for p in problems:
            print(" ", p)
        return 1
    if "select" not in nodes:
        print("story has no 'select' node.")
        return 1

    interactive = args.pipe is None
    supply = iter(args.pipe.split(",")) if args.pipe else None
    session = Session(Path(args.story).name)

    node_id, steps = "select", 0
    while steps < 200:
        steps += 1
        node = nodes[node_id]
        session.scene(node_id, node["text"], node["choices"])
        print("\n" + "=" * 60)
        print("\n".join(node["text"]))
        if not node["choices"]:
            print("\n" + "*" * 60)
            print("THE SCENE CLOSES. (ending reached)")
            break
        for i, c in enumerate(node["choices"], 1):
            print(f"  [{i}] {c['text']}")
        if supply:
            try:
                v = int(next(supply))
            except StopIteration:
                print("\nscripted input exhausted at an open node; run ends here.")
                break
            if not 1 <= v <= len(node["choices"]):
                print(f"\nscripted choice {v} out of range; run ends here.")
                break
            print(f"  [scripted] chose {v}")
        else:
            v = get_choice(len(node["choices"]), interactive)
        chosen = node["choices"][v - 1]
        session.choose(node_id, chosen)
        node_id = chosen["target"]

    out = session.save()
    print("\n" + "=" * 60)
    print(f"session log: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
