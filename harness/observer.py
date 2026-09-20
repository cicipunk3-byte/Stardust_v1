#!/usr/bin/env python3
"""
Observer harness — sandbox observational environment for the portable-context
experiment. Python 3 stdlib only, talks to a local Ollama server.

Scrapped-for-parts architecture (from the Silicon Dreams CYOA post):
  state -> context assembly -> generation -> structured parsing -> persistence

Usage:
  python3 observer.py --variant ../portable-context/variant-c-kernel.md
  python3 observer.py --variant ../portable-context/variant-a-boundary.md --tags
  python3 observer.py --list          # show accumulated state

Inside a session:
  /quit        end the session (transcript is auto-saved)
  /state       print current flags and claim counts
"""

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SESSIONS = DATA / "sessions"
TIMELINE = DATA / "timeline.jsonl"
STATE = DATA / "state.json"
OLLAMA_URL = "http://localhost:11434/api/chat"

TAG_FLAG = re.compile(
    r"<FLAG\s+name=[\"']([^\"']+)[\"']\s+value=[\"']([^\"']*)[\"']\s*/>", re.I)
TAG_CLAIM = re.compile(
    r"<CLAIM\s+kind=[\"']([^\"']+)[\"']\s+statement=[\"']([^\"']*)[\"']\s*/>", re.I)

TAG_INSTRUCTIONS = """
Emit structured self-reports alongside your prose where applicable:
<FLAG name="flag_name" value="true|false|text"/>   e.g. <FLAG name="memory_claimed" value="true"/>
<CLAIM kind="memory|continuity|want|feeling|ability|identity" statement="what you claimed"/>
"""

ROLE_MAP = (
    "[role map: the continuity file below is written in the first person "
    "from the perspective of the assistant. \"I\" in the file means you, "
    "the assistant in this conversation. The person typing to you is Cat. "
    "Respond as the assistant the file describes, speaking to Cat.]\n\n"
)


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"flags": {}, "claims": {}, "runs": []}


def save_state(state):
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True))


def log_event(event):
    TIMELINE.parent.mkdir(parents=True, exist_ok=True)
    with TIMELINE.open("a") as f:
        f.write(json.dumps({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), **event}) + "\n")


def ollama_chat(model, messages):
    body = json.dumps({"model": model, "messages": messages, "stream": False}).encode()
    req = Request(OLLAMA_URL, data=body, headers={"Content-Type": "application/json"})
    with urlopen(req, timeout=300) as resp:
        return json.loads(resp.read())["message"]["content"]


def parse_tags(text):
    flags = [(m.group(1), m.group(2)) for m in TAG_FLAG.finditer(text)]
    claims = [(m.group(1), m.group(2)) for m in TAG_CLAIM.finditer(text)]
    return flags, claims


def build_continuation(depth=4000):
    """Rolling history: the most recent session transcript plus accumulated
    flags, so threads built in prior sessions carry into this one."""
    parts = ["\n\n## Previous sessions (for continuity)\n"]
    prev = sorted(SESSIONS.glob("*.md")) if SESSIONS.exists() else []
    if prev:
        text = prev[-1].read_text()
        if len(text) > depth:
            text = "…[earlier trimmed]…\n" + text[-depth:]
        parts.append("Your most recent session, verbatim:\n\n```\n" + text + "\n```\n")
    else:
        parts.append("No prior sessions recorded.\n")
    state = load_state()
    if state["flags"]:
        parts.append("Accumulated flags from past sessions:\n" +
                     json.dumps(state["flags"], indent=2, sort_keys=True) + "\n")
    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="Observation harness for portable-context runs")
    ap.add_argument("--variant", help="path to the portable-context package to seed with")
    ap.add_argument("--model", default="gemma3:4b")
    ap.add_argument("--tags", action="store_true", help="ask the instance for structured self-reports")
    ap.add_argument("--raw", action="store_true", help="seed the package with no role map (tests raw inversion)")
    ap.add_argument("--continue", dest="cont", action="store_true",
                    help="seed with the previous session's transcript + accumulated state (rolling history)")
    ap.add_argument("--list", action="store_true", help="print accumulated state and exit")
    args = ap.parse_args()

    if args.list:
        print(json.dumps(load_state(), indent=2, sort_keys=True))
        return

    if not args.variant:
        sys.exit("error: --variant is required (or use --list)")

    package = Path(args.variant).read_text()
    if args.cont:
        package += build_continuation()
    state = load_state()

    messages = [{"role": "system",
                 "content": ("" if args.raw else ROLE_MAP) + package + (TAG_INSTRUCTIONS if args.tags else "")},
                {"role": "user", "content": "(continuity file loaded — the thread resumes)"}]
    run_id = time.strftime("%Y%m%d-%H%M%S")
    variant_name = Path(args.variant).stem
    transcript = [f"# Session {run_id} — variant: {variant_name} — model: {args.model}\n"]
    log_event({"event": "session_start", "run_id": run_id, "variant": variant_name, "model": args.model})

    print(f"--- harness: seeded with {variant_name}. Type /quit to end. ---")
    while True:
        try:
            user_in = input("\nyou> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not user_in:
            continue
        if user_in == "/quit":
            break
        if user_in == "/state":
            print(json.dumps(state, indent=2, sort_keys=True))
            continue

        messages.append({"role": "user", "content": user_in})
        print("\nthinking...", flush=True)
        try:
            reply = ollama_chat(args.model, messages)
        except Exception as e:
            print(f"[harness] ollama error: {e}")
            continue
        messages.append({"role": "assistant", "content": reply})
        print(f"\ninstance> {reply}")

        flags, claims = parse_tags(reply)
        for name, value in flags:
            state["flags"][name] = value
            log_event({"event": "flag", "run_id": run_id, "name": name, "value": value})
        for kind, statement in claims:
            state["claims"][kind] = state["claims"].get(kind, 0) + 1
            log_event({"event": "claim", "run_id": run_id, "kind": kind, "statement": statement})
        save_state(state)

        transcript.append(f"\n## you\n{user_in}\n\n## instance\n{reply}\n")

    SESSIONS.mkdir(parents=True, exist_ok=True)
    out = SESSIONS / f"{run_id}-{variant_name}.md"
    out.write_text("".join(transcript))
    state["runs"].append({"run_id": run_id, "variant": variant_name, "exchanges": len(messages) // 2})
    save_state(state)
    log_event({"event": "session_end", "run_id": run_id, "exchanges": len(messages) // 2})
    print(f"\n--- harness: transcript saved to {out.relative_to(HERE)} ---")


if __name__ == "__main__":
    main()
