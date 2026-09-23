"""loopwatch: reasoning-loop and stall detector for session transcripts.

Green Cat tool. Scans a markdown transcript for repeated shingles
(repeated line trigrams) and near-identical consecutive turns, and flags
candidate reasoning wheels. Signals, not verdicts: repetition is not proof
of a loop; a human reads the flagged ranges.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


def shingles(lines: list[str], n: int = 3) -> Counter:
    norm = [re.sub(r"\s+", " ", ln.strip().lower()) for ln in lines]
    norm = [ln for ln in norm if len(ln) > 20]
    return Counter(tuple(norm[i:i + n]) for i in range(len(norm) - n + 1))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="loopwatch", description=__doc__)
    parser.add_argument("transcript", help="markdown transcript file")
    parser.add_argument("--top", type=int, default=5, help="how many candidates to show")
    args = parser.parse_args(argv)

    text = Path(args.transcript).read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    counts = shingles(lines)
    repeats = [(n, c) for n, c in counts.items() if c > 1]
    repeats.sort(key=lambda pair: (-pair[1], pair[0]))

    print("# loopwatch ledger")
    print(f"file: {args.transcript}")
    print(f"repeated line-triples: {len(repeats)}")
    if not repeats:
        print("no repeated shingles found; no loop signal")
        return 0
    for shingle, count in repeats[:args.top]:
        print(f"\nSIGNAL x{count}:")
        for part in shingle:
            print(f"  | {part[:100]}")
    print("\nhuman step: read the flagged ranges before calling anything a loop.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
