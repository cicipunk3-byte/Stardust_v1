"""CLI for repoaudit. Run: python3 -m repoaudit.cli [options]

Output is a claimed-vs-verified audit ledger in the house format:
every section is SIGNAL-class (where to look), the dispositions live
in the human pass and the gate brief that follows.
"""

import argparse
import os
import sys

from . import checks

DEFAULT_SUITES = [
    "tools/fabcheck/tests/test_fabcheck.py",
    "tools/export-ingest/tests/test_ingest.py",
]


def build_parser():
    p = argparse.ArgumentParser(
        prog="repoaudit",
        description="Repo audit ritual, machined. Signals, not verdicts: "
                    "every section flags where to look; a human ledger "
                    "decides dispositions.")
    p.add_argument("--root", default=None,
                   help="repo root (default: the lab repo this tool lives in)")
    p.add_argument("-o", "--out", default=None,
                   help="write the ledger to a file (default: stdout; "
                        "/dev/stdout can fail in sandboxes, prefer a file)")
    p.add_argument("--terms-file", default=None,
                   help="file with one sensitive search term per line; the "
                        "name scan runs ONLY if supplied. Terms are never "
                        "logged into the ledger.")
    p.add_argument("--exempt", action="append", default=[],
                   help="glob of paths exempt from the em-dash scan "
                        "(repeatable)")
    p.add_argument("--include-tbd", action="store_true",
                   help="also flag TBD (archives legitimately carry it)")
    p.add_argument("--skip-tests", action="store_true",
                   help="skip the run-the-artifact test step")
    return p


def load_terms(path):
    if not path:
        return []
    with open(path, encoding="utf-8") as fh:
        return [ln.strip() for ln in fh if ln.strip()]


def main(argv=None):
    args = build_parser().parse_args(argv)
    root = args.root
    if not root:
        # tools/repo-audit/repoaudit/cli.py -> repo root is 3 up
        root = os.path.normpath(
            os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    root = os.path.abspath(root)

    lines = []
    add = lines.append

    add("# Repo audit ledger")
    add("")
    add("Signals, not verdicts. Dispositions: human pass + gate brief.")
    add("")

    add("## Git state")
    gs = checks.git_state(root)
    if "error" in gs:
        add("- SKIPPED: %s" % gs["error"])
    else:
        add("- HEAD: %s; origin/main: %s; in_sync: %s" %
            (gs["head"], gs["origin"], gs["in_sync"]))
        add("- working tree: %s" % ("CLEAN" if gs["clean"] else
                                    "DIRTY (checkpoint blocker; see brief "
                                    "039 F2 for the worked example)"))
        if not gs["clean"]:
            for ln in gs["status_porcelain"].splitlines():
                add("  - %s" % ln)
    add("")

    add("## Inventory")
    inv = checks.inventory(root)
    add("- %d files, %.1f MB" % (inv["file_count"], inv["total_mb"]))
    for d, n in inv["files_by_top_dir"].items():
        label = d + "/" if os.path.isdir(os.path.join(root, d)) else d
        add("  - %s: %d" % (label, n))
    add("")

    add("## Signals")
    em = checks.emdash_scan(root, args.exempt)
    add("- em-dash lines in markdown: %d (composed docs are grep-0; "
        "verbatim quotes and generated files await an exemption ruling, "
        "brief 039 F8)" % len(em))
    for h in em:
        add("  - %s:%d %s" % (h["file"], h["line"], h["text"][:80]))

    mk = checks.marker_scan(root, include_tbd=args.include_tbd)
    add("- TODO/FIXME/XXX markers: %d" % len(mk))
    for h in mk:
        add("  - %s:%d [%s] %s" % (h["file"], h["line"], h["marker"],
                                   h["text"][:70]))

    terms = load_terms(args.terms_file)
    ns = checks.name_scan(root, terms)
    if isinstance(ns, dict) and "skipped" in ns:
        add("- name scan: SKIPPED (%s)" % ns["skipped"])
    else:
        add("- name scan: %d hits for %d supplied terms" %
            (len(ns), len(terms)))
        for h in ns:
            add("  - %s:%d %s" % (h["file"], h["line"], h["text"][:80]))

    bad = checks.link_check(root)
    add("- broken relative markdown links: %d" % len(bad))
    for h in bad:
        add("  - %s -> %s" % (h["file"], h["target"]))

    ta = checks.tracked_artifacts(root)
    if isinstance(ta, dict) and "skipped" in ta:
        add("- tracked artifacts: SKIPPED (%s)" % ta["skipped"])
    else:
        add("- committed artifacts (pyc/DS_Store/tmp): %d" % len(ta))
        for f in ta:
            add("  - %s" % f)
    add("")

    add("## Status sweep (brief status line vs last commit)")
    for row in checks.status_sweep(root):
        add("- %s (last commit %s): %s" % (row["file"], row["last_commit"],
                                           row["status_line"][:120]))
    add("")

    add("## Run-the-artifact")
    if args.skip_tests:
        add("- SKIPPED (--skip-tests)")
    else:
        for r in checks.run_tests(root, DEFAULT_SUITES):
            add("- %s: %s (%s)" % (r["suite"], r["result"], r["detail"]))
    add("")
    add("End of ledger. The human pass and the gate brief carry "
        "dispositions; this file carries none.")

    text = "\n".join(lines)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print("ledger written to %s" % args.out)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
