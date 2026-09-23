"""kernelpress tests. The budget arithmetic and anchor candidates must be
exact; the tool must never emit kernel prose (it scaffolds, a human writes)."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

TR = """# ruling section
The gate ruling adopted the trial design with one variable per path.

## numbers section
Error 11 was logged after the kernel shipped a stale figure.

a plain paragraph of ordinary words without anchors or verdicts.
"""


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "kernelpress.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_budget_math():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md"); open(tr, "w").write(TR)
        result = run_cli([tr])
        words = len(TR.split())
        assert f"source words: {words}" in result.stdout
        assert f"retention budget (20%): {int(words * 0.2)} words" in result.stdout


def test_sections_and_allowance():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md"); open(tr, "w").write(TR)
        result = run_cli([tr])
        assert "sections: 2" in result.stdout  # split on the two headers


def test_anchor_candidates_carry_numbers_and_verdicts():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md"); open(tr, "w").write(TR)
        result = run_cli([tr])
        assert "ANCHOR-CANDIDATE: Error 11" in result.stdout
        assert "ANCHOR-CANDIDATE: The gate ruling" in result.stdout
        assert not any("ordinary words" in ln for ln in result.stdout.splitlines()
                       if "ANCHOR" in ln)


def test_budget_flag_changes_math():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md"); open(tr, "w").write(TR)
        result = run_cli([tr, "--budget", "0.5"])
        words = len(TR.split())
        assert f"retention budget (50%): {int(words * 0.5)} words" in result.stdout


if __name__ == "__main__":
    test_budget_math()
    test_sections_and_allowance()
    test_anchor_candidates_carry_numbers_and_verdicts()
    test_budget_flag_changes_math()
    print("all kernelpress tests passed")
