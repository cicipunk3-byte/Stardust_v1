"""nextcheck: claim extraction and verification queue (brief 022 scaffold).

Yellow Cat tool. Reads a document, extracts claim-shaped sentences, and
emits the house claimed-vs-verified queue with a mandatory run-the-artifact
line item. Web verification is an honest stub: resolution needs a paid
search API, so the tool marks the claim NEEDS-HUMAN instead of pretending.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

CLAIM_HINTS = re.compile(
    r"\b(is|are|was|were|has|have|costs?|ran?|works?|supports?|requires?|"
    r"verified|proven|measured|exactly|confirmed)\b", re.IGNORECASE)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="nextcheck", description=__doc__)
    parser.add_argument("document", help="doc whose claims should be queued")
    parser.add_argument("--artifact", help="command that runs the artifact (run-the-artifact step)")
    parser.add_argument("--out", help="write queue as JSON here instead of stdout")
    args = parser.parse_args(argv)

    queue = []
    for i, raw in enumerate(Path(args.document).read_text(
            encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if CLAIM_HINTS.search(line) and len(line) > 30:
            queue.append({
                "line": i,
                "claim": line[:200],
                "status": "NEEDS-HUMAN",
                "backend": "offline-stub (web verification costs money; stub on purpose)",
            })

    report = {
        "document": args.document,
        "generated": datetime.now(timezone.utc).isoformat(),
        "claims": queue,
        "run_the_artifact": {
            "command": args.artifact,
            "status": "MANDATORY-STEP-PENDING" if args.artifact else "NOT-SPECIFIED (a claim queue alone is not verification)",
        },
        "note": "queue only; nothing here is verified. human ledger decides.",
    }
    text = json.dumps(report, indent=2)
    if args.out:
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"wrote claim queue: {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
