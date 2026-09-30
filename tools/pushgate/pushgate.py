"""pushgate: pre-push discipline for the lab repo.

The error-4-family killer. Three fails of the same class happened on
Sep 24 alone: an em-dash check that printed findings while the push ran
anyway (twice), and an unscoped `git add` that swept another lane's
working files into a push (error 16). This tool exists so the check
STOPS the push instead of narrating it.

What it does, in order:
  1. reads the outgoing refs git hands a pre-push hook on STDIN
     (each line: <local ref> <local sha> <remote ref> <remote sha>)
  2. sweeps every file CHANGED IN THAT COMMIT RANGE for em-dashes
     (the house no-em-dash rule)
  3. exits 1 on any finding, so git aborts the push

The stdin-range sweep is the fix for the Sep 30 defect. The old hook
mode swept `git diff --cached`, but `git commit` drains the index before
pre-push fires, so the hook read zero files, printed "0 findings", and
exited 0 while the em-dash rode through inside the commits. A gate that
narrates instead of stopping is the error-4 class the tool exists to
kill. The range git gives you on stdin is the set of commits actually
leaving the machine; that is what must be swept.

Install as a hook (from the repo root):
    echo 'python3 tools/pushgate/pushgate.py --hook' > .git/hooks/pre-push
    chmod +x .git/hooks/pre-push

--files mode sweeps an explicit path list and is unchanged.

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


def hook_range_files(repo_root: Path, stdin_text: str) -> tuple[list[str], str]:
    """Files changed across the outgoing commit range.

    git feeds a pre-push hook one line per ref on stdin:
        <local ref> <local sha> <remote ref> <remote sha>
    A zero remote sha means a new branch; a zero local sha means a delete.
    Sweep the commits that are actually leaving: <remote sha>..<local sha>.
    Falls back to HEAD~1..HEAD when git gives us nothing usable (e.g. a
    manual invocation), so the hook still checks something rather than
    silently passing.
    """
    specs: list[str] = []
    for line in stdin_text.splitlines():
        parts = line.split()
        if len(parts) != 4:
            continue
        _local_ref, local_sha, _remote_ref, remote_sha = parts
        if local_sha.strip("0") == "":
            continue  # branch deletion: nothing leaving
        if remote_sha.strip("0") == "":
            # new branch: everything reachable from local that is not on
            # any remote-tracking ref
            specs.append("--not")
            specs.append("--remotes")
            specs.append(local_sha)
            continue
        specs.append(f"{remote_sha}..{local_sha}")
    if not specs:
        specs = ["HEAD~1..HEAD"]
    out = subprocess.run(
        ["git", "diff", "--name-only", *specs],
        cwd=repo_root, capture_output=True, text=True,
    )
    if out.returncode != 0:
        # unmerged/unknown sha: fall back rather than pass silently
        out = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1..HEAD"],
            cwd=repo_root, capture_output=True, text=True,
        )
    files = [line for line in out.stdout.splitlines() if line.strip()]
    label = " ".join(specs)
    return files, label


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


def run(repo_root: Path, files: list[str], range_label: str | None = None) -> int:
    scope = f" in range [{range_label}]" if range_label else ""
    findings: list[str] = []
    for rel in files:
        findings.extend(check_file(repo_root / rel))
    if findings:
        print(f"PUSHGATE: BLOCKED. findings in outgoing files{scope}:")
        for f in findings:
            print(f"  {f}")
        print("fix the files, commit, push again. or --no-verify and file the error-log line.")
        return 1
    print(f"PUSHGATE: {len(files)} outgoing file(s) swept{scope}, 0 findings.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="pushgate", description=__doc__)
    parser.add_argument("--hook", action="store_true",
                        help="pre-push hook mode: sweep the outgoing commit range from stdin")
    parser.add_argument("--staged", action="store_true",
                        help="sweep the currently staged files (legacy/manual mode)")
    parser.add_argument("--files", nargs="*", help="sweep these paths instead")
    args = parser.parse_args(argv)

    repo_root = Path(subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, check=True,
    ).stdout.strip())
    if args.files is not None:
        files = args.files
        return run(repo_root, files)
    if args.hook:
        stdin_text = sys.stdin.read() if not sys.stdin.isatty() else ""
        files, label = hook_range_files(repo_root, stdin_text)
        return run(repo_root, files, range_label=label)
    if args.staged:
        files = staged_files(repo_root)
        return run(repo_root, files)
    parser.error("use --hook (pre-push), --staged, or --files PATH...")


if __name__ == "__main__":
    sys.exit(main())
