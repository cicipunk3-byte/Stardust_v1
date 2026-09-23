"""throughline tests. Counts must be exact and file order must be
oldest to newest; the trend line is only as honest as its ordering."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "throughline.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_counts_are_exact_and_ordered():
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "01-first.md"), "w").write("continuity continuity nothing else here\n")
        open(os.path.join(tmp, "02-second.md"), "w").write("one mention of continuity only\n")
        result = run_cli([tmp, "continuity"])
        assert result.returncode == 0, result.stderr
        assert "total=3" in result.stdout
        assert "2 1" in result.stdout  # oldest first: 2 mentions, then 1


def test_case_insensitive_by_default():
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "01.md"), "w").write("Continuity CONTINUITY continuity\n")
        result = run_cli([tmp, "continuity"])
        assert "total=3" in result.stdout


def test_case_sensitive_flag():
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "01.md"), "w").write("Continuity CONTINUITY continuity\n")
        result = run_cli([tmp, "continuity", "--case"])
        assert "total=1" in result.stdout


def test_missing_corpus_is_a_marked_skip():
    result = run_cli(["/nonexistent/corpus", "term"])
    assert result.returncode == 1
    assert "SKIP" in result.stderr


if __name__ == "__main__":
    test_counts_are_exact_and_ordered()
    test_case_insensitive_by_default()
    test_case_sensitive_flag()
    test_missing_corpus_is_a_marked_skip()
    print("all throughline tests passed")
