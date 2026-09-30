"""pushgate suite: the sweeper controls + the hook-shape controls.

PART 1 (this file's own tests, run directly): the four controls claimed
in TOOL-STATUS.md, plus --files mode. These stage one file and call the
sweeper in-process. They prove pushgate's LOGIC is correct.

PART 2 (test_pushgate_hook_shape.py, run as a subprocess below): a real
`git push` against a real bare remote, with pushgate installed as the
actual pre-push hook. This proves git STOPS, which is the claim that
matters and the claim Part 1 cannot reach -- Part 1 exercises a mode
(the index) that the push path never uses.

Part 2 is currently RED and it is red for a real reason. pushgate's hook
mode runs `git diff --cached`, but `git commit` drains the index, so at
pre-push time it sweeps ZERO files, prints "0 findings", exits 0, and the
em-dash rides through inside the commits. Reproduced Sep 30: the em-dash
commit landed on the remote. That is the error-4 push-through class --
a check that narrates instead of stopping -- inside the tool built to
kill that class. Fix is the hook sweeping the outgoing range, not the
index. Until then the suite is RED ON PURPOSE and this rollup will say
FAIL, which is the honest state.

The suite runs BOTH parts and returns non-zero if either fails, so the
hook-shape proof is part of the tool's standing receipt rather than a
file sitting next to it. NOTE: whenever this file is the one ark
discovers, it will now report pushgate FAIL -- correct, not a
regression. See the gate list for the ruling request.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import pushgate  # noqa: E402

EM_DASH = "\u2014"


def git(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def make_repo(td: Path) -> Path:
    repo = td / "repo"
    repo.mkdir()
    git(["init", "-q"], cwd=repo)
    git(["config", "user.email", "t@t.t"], cwd=repo)
    git(["config", "user.name", "t"], cwd=repo)
    return repo


def test_dirty_staged_file_is_blocked():
    with tempfile.TemporaryDirectory() as td:
        repo = make_repo(Path(td))
        (repo / "bad.md").write_text(f"a line with an {EM_DASH} em dash\n")
        git(["add", "bad.md"], cwd=repo)
        rc = pushgate.run(repo, ["bad.md"])
        assert rc == 1, "an em-dash in a staged file must block"


def test_clean_staged_file_passes():
    with tempfile.TemporaryDirectory() as td:
        repo = make_repo(Path(td))
        (repo / "good.md").write_text("plain - hyphen only\n")
        git(["add", "good.md"], cwd=repo)
        rc = pushgate.run(repo, ["good.md"])
        assert rc == 0, "a clean staged file must pass"


def test_staged_but_missing_file_is_flagged():
    with tempfile.TemporaryDirectory() as td:
        repo = make_repo(Path(td))
        rc = pushgate.run(repo, ["ghost.md"])
        assert rc == 1, "staged-but-deleted must be flagged, not crash"


def test_unstaged_file_is_not_swept():
    """error-16 pin: pushgate reads the index, never the working tree."""
    with tempfile.TemporaryDirectory() as td:
        repo = make_repo(Path(td))
        (repo / "dirty.md").write_text(f"unstaged {EM_DASH} em dash\n")
        assert pushgate.staged_files(repo) == [], (
            "an unstaged file must not appear in the staged list"
        )


def test_files_mode_sweeps_named_path():
    with tempfile.TemporaryDirectory() as td:
        repo = make_repo(Path(td))
        (repo / "named.md").write_text(f"named {EM_DASH} em dash\n")
        rc = pushgate.main(["--files", "named.md"])
        assert rc == 1, "--files mode must sweep the named path"


def run_hook_shape() -> tuple[bool, str]:
    """Part 2: does a real git push actually stop?"""
    script = HERE / "test_pushgate_hook_shape.py"
    proc = subprocess.run([sys.executable, str(script)],
                          capture_output=True, text=True, timeout=120)
    tail = ((proc.stdout + proc.stderr).strip().splitlines() or [""])
    return proc.returncode == 0, " | ".join(tail[:1]) or "(no output)"


def main() -> int:
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    local_failures = []
    for t in tests:
        try:
            t()
        except AssertionError as e:
            local_failures.append(f"{t.__name__}: {e}")
    if local_failures:
        print(f"pushgate sweeper controls: FAIL ({len(local_failures)})")
        for f in local_failures:
            print(f"  {f}")
        return 1
    print(f"sweeper controls: {len(tests)}/{len(tests)} passed")

    hooked, summary = run_hook_shape()
    if not hooked:
        print("hook-shape controls: FAIL (a real git push was NOT stopped)")
        print(f"  {summary}")
        print("pushgate suite: FAIL -- see the FOUND DEFECT note in "
              "tests/test_pushgate_hook_shape.py")
        return 1
    print("pushgate suite: PASS (sweeper + hook shape)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
