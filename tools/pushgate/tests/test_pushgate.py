"""pushgate tests. The four controls claimed in TOOL-STATUS.md, committed.

Each test builds a throwaway git repo, stages one file, and runs pushgate
against the real index. Nothing here touches the lab repo.

The rule the tests pin: pushgate sweeps the STAGED index and nothing
else (other lanes' uncommitted work stays invisible), it blocks on
findings, and its exit code is the gate (a hook reads it as stop/pass).
"""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUSHGATE = os.path.join(TOOL_DIR, "pushgate.py")

EM_DASH = "\u2014"


def git(repo, *args):
    return subprocess.run(
        ["git", *args], cwd=repo, capture_output=True, text=True,
        env={**os.environ,
             "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
             "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def make_repo(tmp):
    repo = os.path.join(tmp, "repo")
    os.makedirs(repo)
    git(repo, "init", "-q")
    return repo


def write(repo, name, text):
    path = os.path.join(repo, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def run_gate(repo):
    return subprocess.run(
        [sys.executable, PUSHGATE, "--staged"],
        cwd=repo, capture_output=True, text=True)


# --- control 1: a dirty staged file is blocked -------------------------

def test_dirty_staged_file_is_blocked():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        write(repo, "notes.md", f"clean line\nfound this {EM_DASH} oh no\n")
        git(repo, "add", "notes.md")
        result = run_gate(repo)
        assert result.returncode == 1, result.stdout
        assert "BLOCKED" in result.stdout
        assert "em-dash found" in result.stdout
        assert "notes.md" in result.stdout


# --- control 2: a clean staged file passes -----------------------------

def test_clean_staged_file_passes():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        write(repo, "notes.md", "a clean line\nand a normal dash - like that\n")
        git(repo, "add", "notes.md")
        result = run_gate(repo)
        assert result.returncode == 0, result.stdout
        assert "0 findings" in result.stdout


# --- control 3: staged-but-missing is flagged without crashing ---------

def test_staged_but_missing_file_is_flagged():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        path = write(repo, "gone.md", "clean\n")
        git(repo, "add", "gone.md")
        os.remove(path)  # staged deletion
        result = run_gate(repo)
        assert result.returncode == 1, result.stdout
        assert "missing on disk" in result.stdout


# --- control 4: unstaged files stay invisible --------------------------

def test_unstaged_file_is_not_swept():
    """The scoped-add rule. Another lane's dirty file must not be read."""
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        write(repo, "staged.md", "clean\n")
        write(repo, "other-lane.md", f"dirty {EM_DASH} not mine to push\n")
        git(repo, "add", "staged.md")
        result = run_gate(repo)
        assert result.returncode == 0, result.stdout
        assert "other-lane.md" not in result.stdout


# --- control 5: --files mode sweeps named paths ------------------------

def test_files_mode_sweeps_named_path():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        write(repo, "named.md", f"has one {EM_DASH} here\n")
        result = subprocess.run(
            [sys.executable, PUSHGATE, "--files", "named.md"],
            cwd=repo, capture_output=True, text=True)
        assert result.returncode == 1, result.stdout
        assert "named.md" in result.stdout


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    for t in tests:
        t()
    print(f"all pushgate tests passed ({len(tests)}/{len(tests)})")
