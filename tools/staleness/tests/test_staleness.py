"""staleness tests. The positive control is the real error-11 catch (Sep 23):
kernel v9 shipped "$1.90 of $10.00 used" while the canonical ledger carried
"$1.34 remaining". If this stops flagging, the error-11 class is uncovered."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DOC = """## cost
Platform credit: $1.90 of $10.00 used as of this writing.
Plan total: $10.00.
"""

REF = """## canonical ledger
Platform credit: $1.34 remaining of $10.00 (87% used).
Plan total: $10.00.
"""


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "staleness.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_error11_figure_is_flagged():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        ref = os.path.join(tmp, "ref.md"); open(ref, "w").write(REF)
        result = run_cli([doc, ref])
        assert result.returncode == 0, result.stderr
        assert "$1.9" in result.stdout, "the stale figure must appear as a candidate"
        assert "STALENESS CANDIDATES" in result.stdout


def test_shared_figures_do_not_flag():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        ref = os.path.join(tmp, "ref.md"); open(ref, "w").write(REF)
        result = run_cli([doc, ref])
        out = result.stdout
        # $10.00 appears in both; it must not be listed as a candidate
        cand_section = out.split("figures in reference")[0]
        assert "$10.00" not in cand_section.replace("STALENESS CANDIDATES", "").split(":", 1)[-1] or "$10.00" not in [ln.split()[0] for ln in cand_section.splitlines() if ln.strip().startswith("$")]


def test_matching_docs_produce_zero_candidates():
    with tempfile.TemporaryDirectory() as tmp:
        same = os.path.join(tmp, "same.md"); open(same, "w").write(REF)
        result = run_cli([same, same])
        assert "STALENESS CANDIDATES): 0" in result.stdout


if __name__ == "__main__":
    test_error11_figure_is_flagged()
    test_shared_figures_do_not_flag()
    test_matching_docs_produce_zero_candidates()
    print("all staleness tests passed")
