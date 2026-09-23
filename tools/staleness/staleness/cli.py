"""staleness: number-consistency checker for lab documents.

Red Cat tool. The error-11 killer. Extracts numbers with their context
lines from a document, cross-checks against a canonical reference file,
and flags numbers that appear in the document but contradict the reference.
Signals, not verdicts: same number in different units looks identical to
this tool; a human decides.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# match money, percentages, and plain integers of 2+ digits
NUM_RE = re.compile(r"(\$\s?\d[\d,\.]*|\d+(?:\.\d+)?%)|\b(\d{2,})\b")


def extract(path: Path) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        for match in NUM_RE.finditer(raw):
            token = match.group(0).replace(",", "").replace(" ", "")
            found.setdefault(token, []).append(raw.strip()[:100])
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="staleness", description=__doc__)
    parser.add_argument("document", help="doc under review")
    parser.add_argument("reference", help="canonical file the doc must agree with")
    args = parser.parse_args(argv)

    doc = extract(Path(args.document))
    ref = extract(Path(args.reference))

    print("# staleness ledger")
    print(f"document:  {args.document}")
    print(f"reference: {args.reference}")

    doc_only = sorted(set(doc) - set(ref))
    ref_only = sorted(set(ref) - set(doc))
    # numbers about counts of lines are noise; focus on money and percent
    money_pct = [t for t in doc_only if t.startswith("$") or t.endswith("%")]
    stale_candidates = [t for t in money_pct if t not in ref]

    print(f"\nmoney/percent figures in doc but not reference (STALENESS CANDIDATES): {len(stale_candidates)}")
    for token in stale_candidates:
        for context in doc[token][:2]:
            print(f"  {token:>10}  | {context}")
    print(f"\nfigures in reference but not doc (possibly the fresher values): {len(ref_only)}")
    for token in [t for t in ref_only if t.startswith('$') or t.endswith('%')][:10]:
        for context in ref[token][:1]:
            print(f"  {token:>10}  | {context}")
    print("\nhuman step: a candidate is a question, not a conviction. check units and dates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
