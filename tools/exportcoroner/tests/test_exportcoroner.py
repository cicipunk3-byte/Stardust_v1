"""exportcoroner tests. Positive controls are the REAL quarantined fabrications
from the CCS doc (Gemini deep-research scrape, Sep 2026). Negative controls:
a verified-real citation and the hand-cleaned CCS field manual, which must
come back with zero signals (house regression)."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LAB = os.path.abspath(os.path.join(TOOL_DIR, "..", ".."))
CCS_MANUAL = os.path.join(LAB, "tools", "rainbow9cat", "ccs-field-manual.md")

FABRICATED = """According to The Tao of Agency (2027), all vessels align.
Published by [Open Secure AI Alliance] in the great compendium.
"""

REAL = """Sycophancy can be reduced via synthetic data filtration
(Wei et al., ArXiv 2308.03958). The intervention used a 5:1 mix.
"""


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "exportcoroner.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_real_fabrications_flag():
    with tempfile.TemporaryDirectory() as tmp:
        f = os.path.join(tmp, "fab.md"); open(f, "w").write(FABRICATED)
        result = run_cli([f])
        assert result.returncode == 0, result.stderr
        assert "branded-source-future-year" in result.stdout
        assert "bracket-placeholder-source" in result.stdout


def test_real_citation_does_not_flag():
    with tempfile.TemporaryDirectory() as tmp:
        f = os.path.join(tmp, "real.md"); open(f, "w").write(REAL)
        result = run_cli([f])
        assert "no quarantine-class signals" in result.stdout


def test_hand_cleaned_manual_regression_zero():
    """If this fails, the detector got broader than the human cleanup."""
    assert os.path.exists(CCS_MANUAL), f"missing {CCS_MANUAL}"
    result = run_cli([CCS_MANUAL])
    assert "no quarantine-class signals" in result.stdout, result.stdout


def test_directory_scan():
    with tempfile.TemporaryDirectory() as tmp:
        open(os.path.join(tmp, "a.md"), "w").write(FABRICATED)
        open(os.path.join(tmp, "b.md"), "w").write(REAL)
        result = run_cli([tmp])
        assert "2 files" in result.stdout
        assert "branded-source-future-year" in result.stdout


if __name__ == "__main__":
    test_real_fabrications_flag()
    test_real_citation_does_not_flag()
    test_hand_cleaned_manual_regression_zero()
    test_directory_scan()
    print("all exportcoroner tests passed")
