#!/usr/bin/env python3
"""ark tests. Positive controls: a synthetic conforming archive plugs FIT.
Negative controls: missing required slot and malformed JSONL fail cleanly
with no false FIT. Run from this directory: python3 -m unittest test_ark -v
"""

import io
import json
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import ark  # noqa: E402


def run(argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = ark.main(argv)
    return code, buf.getvalue()


def make_archive(root, timeline_lines=None, transcripts=True):
    root.mkdir(parents=True, exist_ok=True)
    lines = timeline_lines if timeline_lines is not None else [
        json.dumps({"type": "session", "id": "run-001"}) + "\n",
        json.dumps({"type": "flag", "name": "boundary_held"}) + "\n",
    ]
    (root / "timeline.jsonl").write_text("".join(lines), encoding="utf-8")
    if transcripts:
        (root / "transcripts").mkdir(exist_ok=True)
        (root / "transcripts" / "session-001.md").write_text("# session\n", encoding="utf-8")
    return root


class TestPlug(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="ark-test-"))

    def tearDown(self):
        shutil.rmtree(self.base)

    def test_conforming_archive_fits(self):
        """P1: a conforming synthetic archive plugs FIT, exit 0."""
        archive = make_archive(self.base / "good-archive")
        code, out = run(["plug", "--archive", str(archive)])
        self.assertEqual(code, 0)
        self.assertIn("FIT", out)
        self.assertIn("optional: briefs", out)  # optionals reported, absence fine

    def test_missing_required_slot_does_not_fit(self):
        """N1: no timeline.jsonl -> NOT FIT, exit 1, clean report."""
        archive = self.base / "bad-archive"
        archive.mkdir()
        (archive / "transcripts").mkdir()
        (archive / "transcripts" / "s.md").write_text("# s\n")
        code, out = run(["plug", "--archive", str(archive)])
        self.assertEqual(code, 1)
        self.assertIn("NOT FIT", out)
        self.assertIn("timeline.jsonl", out)

    def test_malformed_jsonl_does_not_fit(self):
        """N2: a timeline with an invalid JSON line is caught, not trusted."""
        archive = make_archive(
            self.base / "corrupt-archive",
            timeline_lines=[json.dumps({"ok": True}) + "\n", "not json\n"],
        )
        code, out = run(["plug", "--archive", str(archive)])
        self.assertEqual(code, 1)
        self.assertIn("NOT FIT", out)
        self.assertIn("not valid JSON", out)

    def test_missing_transcripts_dir_does_not_fit(self):
        """N3: timeline alone is not an archive; transcripts are required."""
        archive = self.base / "half-archive"
        archive.mkdir()
        (archive / "timeline.jsonl").write_text(json.dumps({"a": 1}) + "\n")
        code, out = run(["plug", "--archive", str(archive)])
        self.assertEqual(code, 1)
        self.assertIn("NOT FIT", out)

    def test_plug_writes_report_file(self):
        """P2: every plug writes last-plug-report.json -- the check itself
        leaves a receipt."""
        archive = make_archive(self.base / "good-archive")
        run(["plug", "--archive", str(archive)])
        report = json.loads((HERE.parent / "last-plug-report.json").read_text())
        self.assertTrue(report["timeline.jsonl"]["ok"])


class TestList(unittest.TestCase):
    def test_list_runs_and_names_the_inventory(self):
        """P3: list runs clean and shows the house's occupants."""
        code, out = run(["list"])
        self.assertEqual(code, 0)
        self.assertIn("ferry", out)
        self.assertIn("staleness", out)
        self.assertIn("no archive slots", out)  # empty-slot tools stated honestly


if __name__ == "__main__":
    unittest.main(verbosity=2)
