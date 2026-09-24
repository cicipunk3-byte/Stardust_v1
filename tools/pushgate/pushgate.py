"""pushgate: pre-push discipline for the lab repo.

The error-4-family killer. Three fails of the same class happened on
Sep 24 alone: an em-dash check that printed findings while the push ran
anyway (twice), and an unscoped `git add` that swept another lane's
working files into a push (error 16). This tool exists so the check
STOPS the push instead of narrating it.

What it does, in order:
  1. lists the STAGED files (git diff --cached --name-only) and nothing else
  2. sweeps exactly those files for em-dashes (the house no-em-dash rule)
  3. prints the staged diff --stat for the review-before-push rule
  4. exits 1 on any finding, so a git pre-push hook blocks the push

Install as a hook (from the repo root):
    echo 'python3 tools/pushgate/pushgate.py --staged' > .git/hooks/pre-push
    chmod +x .git/hooks/pre-push

Bypass it with `git push --no-verify` and file an error-log line, that
is what the bypass is FOR: a recorded exception, not a habit.

Zero dependencies. Python 3.9+ stdlib only. Offline.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

EM_DASH = "\u2014"


def staged_files(repo_root: Path) -> list[str]:
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=repo_root, capture_output=True, text=True, check=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


def check_file(path: Path) -> list[str]:
    """Returns a list of findings (line:col) for one file."""
    findings = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return [f"{path}: file staged but missing on disk (delete staged?)"]
    for i, line in enumerate(text.splitlines(), 1):
        col = line.find(EM_DASH)
        if col != -1:
            findings.append(f"{path}: line {i}, col {col + 1}: em-dash found")
    return findings


def run(repo_root: Path, files: list[str]) -> int:
    findings: list[str] = []
    for rel in files:
        findings.extend(check_file(repo_root / rel))
    if findings:
        print("PUSHGATE: BLOCKED. findings in staged files:")
        for f in findings:
            print(f"  {f}")
        print("fix the files, re-stage, push again. or --no-verify and file the error-log line.")
        return 1
    print(f"PUSHGATE: {len(files)} staged file(s) swept, 0 findings.")
    stat = subprocess.run(
        ["git", "diff", "--cached", "--stat"],
        cwd=repo_root, capture_output=True, text=True, check=True,
    )
    print("review this staged list against the files you intended to push:")
    print(stat.stdout.rstrip() or "  (nothing staged)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pushgate", description=__doc__)
    parser.add_argument("--staged", action="store_true",
                        help="sweep the currently staged files (hook mode)")
    parser.add_argument("--files", nargs="*", help="sweep these paths instead")
    args = parser.parse_args(argv)

    repo_root = Path(subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip())
    if args.files is not None:
        files = args.files
    elif args.staged:
        files = staged_files(repo_root)
    else:
        parser.error("use --staged (hook mode) or --files PATH...")
    return run(repo_root, files)


if __name__ == "__main__":
    sys.exit(main())
