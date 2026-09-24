"""Package entry point: `python3 -m fabcheck` (from tools/fabcheck/).

Closes the brief-039 F9 packaging gap: the tool was only runnable as
`python3 -m fabcheck.cli`; the shorter canonical form now works too.
"""
from fabcheck.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
