"""nextcheck tests. The queue must never claim verification: every claim is
NEEDS-HUMAN and the run-the-artifact step is never silently absent."""

import json
import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DOC = """# doc
## intro
The weather was pleasant that afternoon.
Ran: the tool executed end to end and exited zero.
The exporter supports both formats per the docs.
"""


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "nextcheck.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_claims_queued_as_needs_human():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        result = run_cli([doc])
        assert result.returncode == 0, result.stderr
        report = json.loads(result.stdout)
        assert all(c["status"] == "NEEDS-HUMAN" for c in report["claims"])
        assert len(report["claims"]) >= 2  # weather line must NOT queue
        assert not any("weather" in c["claim"] for c in report["claims"])


def test_artifact_step_is_mandatory_when_given():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        result = run_cli([doc, "--artifact", "python3 -m fabcheck.cli doc.md"])
        report = json.loads(result.stdout)
        assert report["run_the_artifact"]["status"] == "MANDATORY-STEP-PENDING"


def test_without_artifact_the_queue_admits_it():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        result = run_cli([doc])
        report = json.loads(result.stdout)
        assert "NOT-SPECIFIED" in report["run_the_artifact"]["status"]


def test_out_writes_file():
    with tempfile.TemporaryDirectory() as tmp:
        doc = os.path.join(tmp, "doc.md"); open(doc, "w").write(DOC)
        out = os.path.join(tmp, "queue.json")
        result = run_cli([doc, "--out", out])
        assert result.returncode == 0
        assert os.path.exists(out)


if __name__ == "__main__":
    test_claims_queued_as_needs_human()
    test_artifact_step_is_mandatory_when_given()
    test_without_artifact_the_queue_admits_it()
    test_out_writes_file()
    print("all nextcheck tests passed")
