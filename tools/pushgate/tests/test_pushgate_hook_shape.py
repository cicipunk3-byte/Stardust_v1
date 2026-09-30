"""pushgate test: the HOOK SHAPE, not just the sweeper.

The Sep 29 suite (test_pushgate.py) proves the LOGIC: given staged files,
pushgate finds em-dashes and exits 1. It does not prove the thing that
actually matters for a pre-push hook, which is what git DOES with a
non-zero exit from the hook.

That distinction is not academic. The error-4 class was born because a
check PRINTED its findings while the push ran anyway. A gate that
computes correctly and does not stop anything is the exact failure the
tool exists to prevent, and the sweeper suite cannot see it.

This file points a REAL `git push` at a REAL remote and asserts the push
did not happen. Two controls, one assertion each:

  A. pushgate as installed pre-push hook  -> em-dash committed -> push BLOCKED
  B. pushgate as installed pre-push hook  -> clean committed    -> push SUCCEEDS

B is the load-bearing one. A hook that blocks everything is not a gate
either; it is an outage. Both directions, or the claim is not earned.

FOUND DEFECT (Sep 30 ~1 AM heartbeat, found by this file on its first
run). pushgate in hook mode sweeps `git diff --cached`, and the index is
EMPTY by the time a pre-push hook runs: `git commit` drains it. So the
installed hook reads zero files, prints "0 staged file(s) swept, 0
findings", exits 0, and the push goes through with the em-dash inside
the commits. Reproduced against a real bare remote: the em-dash commit
LANDED. The tool prints the right words and stops nothing, which is
verbatim the error-4 failure it was built to kill. Its --files mode is
unaffected and correct, which is why nine months of staging-based tests
never saw it: every existing control stages a file and calls the sweeper
directly, so the controls test a mode the push path never uses.

This file currently FAILS on control A by design. The test is the
receipt; it goes red until the hook path is fixed (the hook needs to
sweep the outgoing commit range, not the index).

Everything runs against throwaway repos built under a temp dir. Nothing
here touches the lab repo or the network: the "remote" is a bare repo on
local disk, so this is an honest local proof and NOT a field run against
the real remote. A tested tool is not an installed gate; this makes the
TESTS stronger, it does not install anything.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

PUSHGATE = Path(__file__).resolve().parent.parent / "pushgate.py"
EM_DASH = "\u2014"


def git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def build_pair(root: Path, name: str) -> tuple[Path, Path, Path]:
    """Returns (work_repo, bare_remote, pushgate_copy)."""
    remote = root / f"{name}-remote.git"
    work = root / f"{name}-work"
    remote.mkdir()
    git(["init", "--bare", "-q", str(remote)], cwd=root)
    work.mkdir()
    git(["init", "-q"], cwd=work)
    git(["config", "user.email", "t@t.t"], cwd=work)
    git(["config", "user.name", "t"], cwd=work)
    git(["remote", "add", "origin", str(remote)], cwd=work)
    (work / "a.txt").write_text("ok\n")
    git(["add", "a.txt"], cwd=work)
    git(["commit", "-q", "-m", "base"], cwd=work)
    git(["push", "-q", "origin", "HEAD:refs/heads/main"], cwd=work)

    # Install pushgate as the real pre-push hook. git runs this executable
    # with the remote name + URL as argv; our args are baked in. The hook
    # is a copy so the engine runs from inside this temp repo, exactly the
    # way a real install would behave.
    pg_dir = work / ".gate"
    pg_dir.mkdir()
    pg = pg_dir / "pushgate.py"
    pg.write_text(PUSHGATE.read_text())
    hook = work / ".git" / "hooks" / "pre-push"
    hook.write_text(f'#!/bin/sh\nexec python3 "{pg}" --staged\n')
    hook.chmod(0o755)
    return work, remote, pg


def remote_has(remote: Path, branch: str, expect_sha: str) -> bool:
    out = git(["rev-parse", branch], cwd=remote)
    return out.returncode == 0 and out.stdout.strip() == expect_sha


def case_blocked(root: Path) -> list[str]:
    work, remote, _ = build_pair(root, "blocked")
    (work / "bad.txt").write_text(f"an {EM_DASH} em dash\n")
    git(["add", "bad.txt"], cwd=work)
    git(["commit", "-q", "-m", "bad"], cwd=work)
    head = git(["rev-parse", "HEAD"], cwd=work).stdout.strip()
    before = git(["rev-parse", "main"], cwd=remote).stdout.strip()

    push = git(["push", "origin", "HEAD:refs/heads/main"], cwd=work)

    fails = []
    if push.returncode == 0:
        fails.append("A: push SUCCEEDED with an em-dash staged; the hook did not stop it")
    if "PUSHGATE: BLOCKED" not in (push.stdout + push.stderr):
        fails.append("A: push failed but pushgate did not say BLOCKED")
    if remote_has(remote, "main", head):
        fails.append("A: remote advanced to the blocked commit")
    if not remote_has(remote, "main", before):
        fails.append("A: remote moved off its base commit (unexpected)")
    return fails


def case_clean(root: Path) -> list[str]:
    work, remote, _ = build_pair(root, "clean")
    (work / "good.txt").write_text("plain - hyphen, no em dash\n")
    git(["add", "good.txt"], cwd=work)
    git(["commit", "-q", "-m", "good"], cwd=work)
    head = git(["rev-parse", "HEAD"], cwd=work).stdout.strip()

    push = git(["push", "origin", "HEAD:refs/heads/main"], cwd=work)

    fails = []
    if push.returncode != 0:
        fails.append(f"B: clean push BLOCKED by the hook ({push.stderr.strip()[:200]})")
    if not remote_has(remote, "main", head):
        fails.append("B: push reported success but the remote did not advance")
    return fails


def main() -> int:
    if not PUSHGATE.exists():
        print(f"pushgate not found at {PUSHGATE}", file=sys.stderr)
        return 2
    results: list[str] = []
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        results += case_blocked(root)
        results += case_clean(root)

    if results:
        print("pushgate hook-shape: FAIL")
        for r in results:
            print(f"  {r}")
        return 1
    print("pushgate hook-shape: PASS")
    print("  A. real git push, em-dash staged  -> BLOCKED, remote unchanged")
    print("  B. real git push, clean staged    -> SUCCEEDS, remote advanced")
    print("  (local bare remote; not a field run against the real origin)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
