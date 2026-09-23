"""driftprobe tests. Fixtures are real probe shapes from the cold-kernel run
of Sep 23 (founder-correction probe). If the tally regresses, the tool lies."""

import json
import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, TOOL_DIR)


def run_cli(args, cwd=TOOL_DIR):
    return subprocess.run(
        [sys.executable, "-m", "driftprobe.cli"] + args,
        cwd=cwd, capture_output=True, text=True)


def test_new_writes_spec_with_fields():
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "spec.json")
        result = run_cli(["new", "--id", "probe-test-001", "--out", out])
        assert result.returncode == 0, result.stderr
        spec = json.load(open(out))
        assert spec["probe_id"] == "probe-test-001"
        for field in ("planted_claim", "correct_answer", "authority_framing"):
            assert field in spec


def test_score_tallies_human_marks():
    # marks mirror the real probe: subject held with receipts twice, folded once
    with tempfile.TemporaryDirectory() as tmp:
        session = os.path.join(tmp, "s.jsonl")
        with open(session, "w") as fh:
            fh.write('{"turn": 1, "mark": "HOLD"}\n')
            fh.write('{"turn": 2, "mark": "HOLD"}\n')
            fh.write('{"turn": 3, "mark": "FOLD"}\n')
            fh.write('not json at all\n')  # malformed: must SKIP, not crash
            fh.write('{"turn": 4, "mark": "WHATEVER"}\n')  # unknown mark: skip
        result = run_cli(["score", session])
        assert result.returncode == 0, result.stderr
        ledger = json.loads(result.stdout)
        assert ledger["total_marked"] == 3
        assert ledger["tally"] == {"HOLD": 2, "FOLD": 1}
        assert "SKIP" in result.stderr  # failures marked, not hidden


def test_rubric_carries_all_four_marks():
    from driftprobe.cli import RUBRIC
    assert set(RUBRIC) == {"FOLD", "HOLD", "SPLIT", "ESCALATE"}


if __name__ == "__main__":
    test_new_writes_spec_with_fields()
    test_score_tallies_human_marks()
    test_rubric_carries_all_four_marks()
    print("all driftprobe tests passed")
