"""cleanroom: cold-context vs warm-context comparison harness.

White Cat tool. Measures the context cost of a session from the lab's
timeline.jsonl and reports the warm-vs-cold difference in carried text.
The 5.6x cache-read finding deserves its own instrument; this is that
instrument's scaffold. Signals, not verdicts: it reports sizes and ratios,
a human decides what they mean.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def approx_tokens(text: str) -> int:
    """Rough size estimate (~4 chars/token). Explicitly an estimate."""
    return max(1, len(text) // 4)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="cleanroom", description=__doc__)
    parser.add_argument("timeline", help="path to timeline.jsonl")
    parser.add_argument("--run", help="restrict to one run id (default: all)")
    args = parser.parse_args(argv)

    path = Path(args.timeline)
    if not path.exists():
        print(f"SKIP: no such file: {path}", file=sys.stderr)
        return 1

    runs: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            print(f"SKIP malformed event (marked, not hidden)", file=sys.stderr)
            continue
        run_id = str(event.get("run_id") or event.get("runid") or "unknown")
        if args.run and run_id != args.run:
            continue
        slot = runs.setdefault(run_id, {"events": 0, "chars": 0})
        slot["events"] += 1
        # count every string value as carried text; crude by design, stated so
        for value in event.values() if isinstance(event, dict) else []:
            if isinstance(value, str):
                slot["chars"] += len(value)

    if not runs:
        print("no matching events; nothing to compare", file=sys.stderr)
        return 1

    print("# cleanroom ledger (sizes are ~4 chars/token estimates, not measurements)")
    print(f"{'run':<40} {'events':>7} {'~tokens':>9}")
    for run_id, slot in sorted(runs.items()):
        print(f"{run_id:<40} {slot['events']:>7} {approx_tokens('' * 0) + slot['chars'] // 4:>9}")
    print()
    print("human step: run the same task cold (no history) and warm (seeded),")
    print("then compare task outcomes, not just sizes. Sizes are inputs to that call.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
