"""kernelpress: transcript-to-kernel distillation scaffold with retention budget.

Orange Cat tool. Splits a transcript into sections, applies a target
retention budget (default 20 percent), and emits a kernel draft skeleton
with per-section word allowances and verbatim anchor candidates. It does
NOT write the kernel prose: distillation is a human (or human-gated)
judgment. Compression without a DC check is just loss with confidence.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="kernelpress", description=__doc__)
    parser.add_argument("transcript", help="markdown transcript")
    parser.add_argument("--budget", type=float, default=0.2,
                        help="target retention as a fraction of source words (default 0.2)")
    args = parser.parse_args(argv)

    text = Path(args.transcript).read_text(encoding="utf-8", errors="replace")
    words = len(text.split())
    budget = max(1, int(words * args.budget))

    # section split on markdown headers, else on blank-line paragraph runs
    if re.search(r"^#{1,3} ", text, re.MULTILINE):
        sections = re.split(r"(?=^#{1,3} )", text, flags=re.MULTILINE)
    else:
        sections = [p for p in text.split("\n\n") if p.strip()]

    per_section = max(1, budget // max(1, len(sections)))

    print("# kernelpress draft skeleton (NOT a kernel; a human writes the prose)")
    print(f"source: {args.transcript}")
    print(f"source words: {words} | retention budget ({args.budget:.0%}): {budget} words")
    print(f"sections: {len(sections)} | allowance each: ~{per_section} words")
    print()
    for i, section in enumerate(sections, 1):
        heading = section.strip().splitlines()[0][:60]
        sw = len(section.split())
        print(f"## section {i}: {heading}")
        print(f"   source words: {sw} | allowance: ~{per_section}")
        # anchor candidates: lines with numbers, quotes, or verdict words
        for line in section.splitlines():
            s = line.strip()
            if re.search(r"(\d{2,}|\"|\b(ruling|finding|adopted|ratified|error)\b)", s, re.IGNORECASE):
                print(f"   ANCHOR-CANDIDATE: {s[:100]}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
