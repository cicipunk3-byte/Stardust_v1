"""exportcoroner: forgery and corruption detector for provider exports.

Grey Cat tool. Scans a directory of provider export files for the lab's
known failure classes: branded title-plus-year citations (the CCS class),
bracketed placeholder sources, and broken link-encoding artifacts.
Signals, not verdicts. Fixtures are the real quarantined fabrications.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# positive control shapes, from the real CCS quarantine (fabcheck lineage)
BRANDED_SOURCE = re.compile(r"\b([A-Z][A-Za-z' ]{3,40})\s+\((\d{4})\)")
# bracketed PLACEHOLDER sources like "[Open Secure AI Alliance]": at least two
# words of 3+ letters with a lowercase letter somewhere (all-caps banners like
# "[ THE GLASS VESSEL ]" are section headings in the hand-cleaned manual, not
# sources; the case test keeps them out)
BRACKET_SOURCE = re.compile(r"\[\s*([A-Za-z]{3,}[A-Za-z ]*)\s*\]")
# broken link-encoding from the ~1MB CCS export
LINK_ROT = re.compile(r"(?i)%2F|&amp;lt;|\]\(https?://[^)]{500,}")

FUTURE_YEAR = 2027  # a 2026-or-earlier year is fine; repo-time aware humans re-tune


def scan_file(path: Path) -> list[tuple[str, int, str]]:
    signals: list[tuple[str, int, str]] = []
    for i, raw in enumerate(path.read_text(
            encoding="utf-8", errors="replace").splitlines(), 1):
        for match in BRANDED_SOURCE.finditer(raw):
            year = int(match.group(2))
            if year >= FUTURE_YEAR:
                signals.append(("branded-source-future-year", i, match.group(0)[:80]))
        for match in BRACKET_SOURCE.finditer(raw):
            content = match.group(1)
            words = content.split()
            if len(words) >= 2 and any(c.islower() for c in content):
                signals.append(("bracket-placeholder-source", i, match.group(0)[:80]))
        for match in LINK_ROT.finditer(raw):
            signals.append(("link-encoding-rot", i, raw.strip()[:80]))
    return signals


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="exportcoroner", description=__doc__)
    parser.add_argument("target", help="export file or directory of exports")
    args = parser.parse_args(argv)

    target = Path(args.target)
    files = sorted(target.rglob("*")) if target.is_dir() else [target]
    files = [f for f in files if f.is_file() and not f.name.startswith(".")]

    print("# exportcoroner ledger")
    print(f"target: {target} ({len(files)} files)")
    total = 0
    for f in files:
        for kind, line, snippet in scan_file(f):
            total += 1
            print(f"SIGNAL [{kind}] {f.name}:{line}: {snippet}")
    if total == 0:
        print("no quarantine-class signals found (clean control passed)")
    print("\nhuman step: signals are where to look, not what to delete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
