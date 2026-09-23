"""throughline: term and register trend tracking across a transcript corpus.

Cobalt Cat tool. Walks a directory of transcripts, counts occurrences of
query terms per file over time (files sorted by name/date), and prints a
per-term trend line. Whole-timeline perception is MYTHIC on purpose: this
tool reads what it is fed, no more. Signals, not verdicts.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="throughline", description=__doc__)
    parser.add_argument("corpus", help="directory of transcript files")
    parser.add_argument("terms", help="comma-separated terms to track")
    parser.add_argument("--case", action="store_true", help="case-sensitive matching")
    args = parser.parse_args(argv)

    corpus = Path(args.corpus)
    if not corpus.is_dir():
        print(f"SKIP: not a directory: {corpus}", file=sys.stderr)
        return 1
    terms = [t.strip() for t in args.terms.split(",") if t.strip()]
    flags = 0 if args.case else re.IGNORECASE

    files = sorted(p for p in corpus.rglob("*") if p.is_file())
    series: dict[str, list[int]] = {t: [] for t in terms}
    for f in files:
        try:
            text = f.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            print(f"SKIP unreadable {f.name}: {exc}", file=sys.stderr)
            continue
        for t in terms:
            series[t].append(len(re.findall(re.escape(t), text, flags)))

    print("# throughline ledger")
    print(f"corpus: {corpus} ({len(files)} files, oldest to newest, left to right)")
    for t in terms:
        counts = series[t]
        total = sum(counts)
        spark = " ".join(str(c) for c in counts)
        print(f"\n{t}: total={total}")
        print(f"  {spark}")
    print("\nhuman step: counts are not meaning. read the peaks in context.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
