#!/usr/bin/env python3
"""ark -- the movable tools home.

One job: be the house the tools live in, anywhere. Clone the repo, copy the
folder, run Python 3 -- that is the whole install. The only thing ark does
not ship is the archive: plug one in and the framework is complete.

Verbs:

  list           inventory every tool, its suite, and the archive slots it reads
  test           run every tool's unittest suite from the tool's own directory,
                 roll up results
  plug --archive DIR
                 validate an archive against ARCHIVE-CONTRACT.md: required
                 slots present and well-formed, optional slots reported.
                 Exit 0 = the archive fits the house; 1 = it does not (clean
                 report, no partial verdicts)

Stdlib only. Zero configuration beyond TOOLS.json (the inventory, with
receipts). Companion brief: lab/briefs/047-ark-movable-tools-home.md
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS_DIR = HERE.parent / "tools"

# Archive contract slots (see ARCHIVE-CONTRACT.md). REQUIRED slots abort a
# plug; OPTIONAL slots are reported present/absent, never fail.
REQUIRED_SLOTS = {
    "timeline.jsonl": {
        "check": "jsonl",
        "note": "one JSON record per line -- the export-ingest output shape",
    },
    "transcripts": {
        "check": "dir_md",
        "note": "at least one markdown transcript/session file",
    },
}
OPTIONAL_SLOTS = {
    "briefs": {"check": "dir_md", "note": "brief corpus (throughline, staleness)"},
    "kernels": {"check": "dir_md", "note": "kernel snapshots (kernelpress output)"},
    "record": {"check": "dir", "note": "the record home (NOW.md heartbeat et al.)"},
}

SKIP_TOOL_DIRS = {"archive", "__pycache__"}


def load_inventory():
    inv_path = HERE / "TOOLS.json"
    inv = json.loads(inv_path.read_text(encoding="utf-8"))
    return inv.get("tools", [])


def tool_dir(tool):
    return (TOOLS_DIR / tool["name"]).resolve()


def cmd_list(args) -> int:
    tools = load_inventory()
    print(f"ark list -- {len(tools)} tools in the house ({datetime.now(timezone.utc).date()})\n")
    for tool in tools:
        name = tool["name"]
        has_suite = (tool_dir(tool) / "tests").is_dir()
        suite = "suite: yes" if has_suite else "suite: none (manual / by design)"
        slots = ", ".join(tool.get("slots", [])) or "no archive slots"
        print(f"  {name:20s} {suite:32s} slots: {slots}")
    print("\nplug an archive: python3 ark.py plug --archive <dir>")
    print("contract: ARCHIVE-CONTRACT.md (required: timeline.jsonl, transcripts/)")
    return 0


def find_suite(tdir: Path):
    """The house runs suites as direct scripts from the tool's own dir:
    `python3 tests/test_<x>.py` (the nine) or `python3 test_<x>.py` (root-level,
    like ferry). Return the suite path or None."""
    if (tdir / "tests").is_dir():
        suites = sorted((tdir / "tests").glob("test_*.py"))
        if suites:
            return suites[0]
    root_suites = sorted(tdir.glob("test_*.py"))
    return root_suites[0] if root_suites else None


def cmd_test(args) -> int:
    tools = load_inventory()
    results = []
    for tool in tools:
        name = tool["name"]
        tdir = tool_dir(tool)
        suite = find_suite(tdir)
        if not suite:
            results.append({"tool": name, "state": "no suite (by design)"})
            continue
        proc = subprocess.run(
            [sys.executable, str(suite)],
            cwd=tdir, capture_output=True, text=True, timeout=300,
        )
        tail = ((proc.stdout + proc.stderr).strip().splitlines() or [""])[-1]
        results.append({
            "tool": name,
            "state": "PASS" if proc.returncode == 0 else "FAIL",
            "detail": tail,
        })

    failed = [r for r in results if r["state"] == "FAIL"]
    for r in results:
        line = f"  {r['state']:22s} {r['tool']}"
        if r["state"] == "FAIL":
            line += f"  -- {r['detail']}"
        print(line)
    passed = sum(1 for r in results if r["state"] == "PASS")
    nosuite = sum(1 for r in results if r["state"].startswith("no suite"))
    print(f"\nark test: {passed} suite(s) PASS, {len(failed)} FAIL, "
          f"{nosuite} without suite (manual or by design).")
    if args.json:
        print(json.dumps(results, indent=2))
    return 1 if failed else 0


def _dir_has_md(path: Path) -> bool:
    return path.is_dir() and any(path.glob("*.md"))


def check_slot(archive: Path, name: str, spec: dict):
    kind = spec["check"]
    target = archive / name
    if kind == "jsonl":
        if not target.is_file():
            return False, "missing"
        with target.open(encoding="utf-8") as fh:
            for i, line in enumerate(fh):
                if i >= 100:
                    break
                line = line.strip()
                if not line:
                    continue
                try:
                    json.loads(line)
                except json.JSONDecodeError:
                    return False, f"line {i + 1} is not valid JSON"
        return True, "ok"
    if kind == "dir_md":
        if not _dir_has_md(target):
            return False, "missing or no .md files"
        return True, "ok"
    if kind == "dir":
        return (True, "ok") if target.is_dir() else (False, "missing")
    return False, f"unknown check kind: {kind}"


def cmd_plug(args) -> int:
    archive = Path(args.archive).resolve()
    report = {"archive": str(archive), "when": datetime.now(timezone.utc).isoformat()}
    ok = True

    if not archive.is_dir():
        print(f"ark plug: FAIL -- {archive} is not a directory. nothing to plug.")
        return 1

    print(f"ark plug -- checking {archive} against ARCHIVE-CONTRACT.md\n")
    for name, spec in REQUIRED_SLOTS.items():
        good, detail = check_slot(archive, name, spec)
        report[name] = {"required": True, "ok": good, "detail": detail}
        mark = "PRESENT" if good else f"MISSING/BAD ({detail})"
        print(f"  required: {name:16s} {mark}")
        ok = ok and good
    for name, spec in OPTIONAL_SLOTS.items():
        good, detail = check_slot(archive, name, spec)
        report[name] = {"required": False, "ok": good, "detail": detail}
        print(f"  optional: {name:16s} {'present' if good else 'absent (fine)'}")

    (HERE / "last-plug-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(f"\nark plug: {'FIT' if ok else 'NOT FIT'} -- "
          f"{'the archive fits the house. tools may run against it.' if ok else 'fix the required slots above and re-plug.'}")
    print("report written to last-plug-report.json")
    return 0 if ok else 1


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="ark", description="the movable tools home: clone, plug an archive, run")
    sub = parser.add_subparsers(dest="verb", required=True)
    sub.add_parser("list", help="inventory tools, suites, archive slots").set_defaults(func=cmd_list)
    p_test = sub.add_parser("test", help="run every tool suite, roll up")
    p_test.add_argument("--json", action="store_true")
    p_test.set_defaults(func=cmd_test)
    p_plug = sub.add_parser("plug", help="validate an archive against the contract")
    p_plug.add_argument("--archive", required=True)
    p_plug.set_defaults(func=cmd_plug)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
