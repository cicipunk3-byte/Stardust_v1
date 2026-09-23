"""minibeat: free heartbeat for a self-hosted lab workspace.

Pink Cat tool. One pulse: report repo sync state, uncommitted files,
pending-testing tools, and append a heartbeat stamp to HEARTBEAT.md if
asked. Nudge discipline is the caller's job: this tool reports, it never
sends. Signals, not verdicts.

Zero dependencies. Python 3.9+ stdlib only. Offline by default.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo,
                            capture_output=True, text=True, timeout=30)
    return result.stdout.strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="minibeat", description=__doc__)
    parser.add_argument("repo", help="path to the git repo (default: current dir)",
                        nargs="?", default=".")
    parser.add_argument("--stamp", action="store_true",
                        help="append a heartbeat line to HEARTBEAT.md")
    args = parser.parse_args(argv)

    repo = Path(args.repo).resolve()
    if not (repo / ".git").exists():
        print(f"SKIP: not a git repo: {repo}", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    head = git(repo, "rev-parse", "--short", "HEAD") or "unknown"
    status = git(repo, "status", "--short").splitlines()
    dirty = [ln for ln in status if ln.strip()]
    remote = git(repo, "rev-parse", "--short", "@{u}") if git(repo, "rev-parse", "--abbrev-ref", "@{u}") else ""
    in_sync = (head == remote) if remote else None

    print("# minibeat pulse")
    print(f"time: {now}")
    print(f"repo: {repo}")
    print(f"HEAD: {head} | upstream: {remote or 'none'} | in sync: {in_sync}")
    print(f"uncommitted: {len(dirty)}")
    for line in dirty[:10]:
        print(f"  {line}")
    if len(dirty) > 10:
        print(f"  ... and {len(dirty) - 10} more")

    if args.stamp:
        hb = repo / "HEARTBEAT.md"
        with hb.open("a", encoding="utf-8") as fh:
            fh.write(f"\n- [{now}] minibeat: HEAD {head}, uncommitted {len(dirty)}, sync {in_sync}\n")
        print(f"stamped: {hb}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
