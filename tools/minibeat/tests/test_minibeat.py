"""minibeat tests. Run against a throwaway git repo. The tool reports and
stamps; it never sends anything, and the test pins that."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def git(repo, *args):
    return subprocess.run(["git", *args], cwd=repo,
                          capture_output=True, text=True,
                          env={**os.environ,
                               "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
                               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})


def make_repo(tmp):
    repo = os.path.join(tmp, "repo")
    os.makedirs(repo)
    git(repo, "init", "-q")
    open(os.path.join(repo, "HEARTBEAT.md"), "w").write("# heartbeats\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-qm", "init")
    return repo


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "minibeat.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_pulse_reports_head_and_dirty_count():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        open(os.path.join(repo, "uncommitted.md"), "w").write("dirty\n")
        result = run_cli([repo])
        assert result.returncode == 0, result.stderr
        assert "in sync: None" in result.stdout  # no upstream configured
        assert "uncommitted: 1" in result.stdout


def test_stamp_appends_to_heartbeat():
    with tempfile.TemporaryDirectory() as tmp:
        repo = make_repo(tmp)
        result = run_cli([repo, "--stamp"])
        assert result.returncode == 0, result.stderr
        content = open(os.path.join(repo, "HEARTBEAT.md")).read()
        assert "minibeat: HEAD" in content


def test_non_repo_is_a_marked_skip():
    with tempfile.TemporaryDirectory() as tmp:
        result = run_cli([tmp])
        assert result.returncode == 1
        assert "SKIP" in result.stderr


if __name__ == "__main__":
    test_pulse_reports_head_and_dirty_count()
    test_stamp_appends_to_heartbeat()
    test_non_repo_is_a_marked_skip()
    print("all minibeat tests passed")
