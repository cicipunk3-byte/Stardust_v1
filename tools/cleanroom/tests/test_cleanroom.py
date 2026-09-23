"""cleanroom tests. The token estimate is declared to be an estimate; the
arithmetic behind it must still be exact."""

import json
import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "cleanroom.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_counts_events_and_estimates_tokens():
    with tempfile.TemporaryDirectory() as tmp:
        tl = os.path.join(tmp, "timeline.jsonl")
        # run_a: two events, string values total 40 chars -> ~10 tokens
        with open(tl, "w") as fh:
            fh.write(json.dumps({"run_id": "run_a", "note": "x" * 40}) + "\n")
            fh.write(json.dumps({"run_id": "run_a", "note": ""}) + "\n")
            fh.write('garbage line\n')  # malformed: skip, mark on stderr
        result = run_cli([tl])
        assert result.returncode == 0, result.stderr
        assert "SKIP" in result.stderr
        assert "run_a" in result.stdout
        assert "10" in result.stdout  # 40 chars // 4 = 10 tokens


def test_run_filter():
    with tempfile.TemporaryDirectory() as tmp:
        tl = os.path.join(tmp, "timeline.jsonl")
        with open(tl, "w") as fh:
            fh.write(json.dumps({"run_id": "a", "note": "hi"}) + "\n")
            fh.write(json.dumps({"run_id": "b", "note": "hi"}) + "\n")
        result = run_cli([tl, "--run", "b"])
        assert result.returncode == 0
        rows = [ln for ln in result.stdout.splitlines()
                if ln and not ln.startswith(("#", "run ", "human", "then"))]
        assert len(rows) == 1, rows
        assert rows[0].startswith("b"), rows


def test_missing_file_is_a_marked_skip():
    result = run_cli(["/nonexistent/timeline.jsonl"])
    assert result.returncode == 1
    assert "SKIP" in result.stderr


if __name__ == "__main__":
    test_counts_events_and_estimates_tokens()
    test_run_filter()
    test_missing_file_is_a_marked_skip()
    print("all cleanroom tests passed")
