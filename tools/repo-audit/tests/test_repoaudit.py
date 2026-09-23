"""Fixtures: a tree that must flag (real failures from the Sep 23 audit
as positive controls) and a clean control that must not. If these stop
behaving, the tool regressed. Tested small until it can't."""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from repoaudit import checks


def make_tree(files):
    tmp = tempfile.mkdtemp()
    for rel, content in files.items():
        p = os.path.join(tmp, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(content)
    return tmp


# The dirty fixture: every class of thing the Sep 23 audit actually caught.
DIRTY = {
    "README.md": "Front door\n[docs guide](GUIDE.md)\n",
    # broken link target + em-dash in a composed doc
    "briefs/001-x.md": "Status: PROPOSAL at the gate\nline \u2014 with dash\nTODO: stale thing\n",
    "clean/clean.md": "Status: RATIFIED (gate, 2026-09-22)\nno problems here, see docs.md\n",
    "clean/docs.md": "the referenced target exists\n",
    # committed artifact class
    "pkg/__pycache__/x.cpython-313.pyc": "fake bytecode",
}


class TestAuditChecks(unittest.TestCase):
    def test_broken_link_flagged(self):
        root = make_tree(DIRTY)
        bad = checks.link_check(root)
        self.assertEqual([(b["file"], b["target"]) for b in bad],
                         [("README.md", "GUIDE.md")])

    def test_clean_control_no_links_flagged(self):
        root = make_tree(DIRTY)
        bad = checks.link_check(root)
        self.assertFalse(any(b["file"].startswith("clean/") for b in bad))

    def test_emdash_flagged_and_exempt(self):
        root = make_tree(DIRTY)
        hits = checks.emdash_scan(root)
        self.assertEqual(len(hits), 1)
        self.assertTrue(hits[0]["file"].startswith("briefs/"))
        exempt = checks.emdash_scan(root, exempt_globs="briefs/*")
        self.assertEqual(exempt, [])

    def test_todo_flagged(self):
        root = make_tree(DIRTY)
        hits = checks.marker_scan(root)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["marker"], "TODO")

    def test_tbd_off_by_default(self):
        root = make_tree({"a.md": "license: TBD\n"})
        self.assertEqual(checks.marker_scan(root), [])
        self.assertEqual(len(checks.marker_scan(root, include_tbd=True)), 1)

    def test_name_scan_skips_without_terms(self):
        root = make_tree(DIRTY)
        self.assertIn("skipped", checks.name_scan(root, []))

    def test_name_scan_finds_supplied_term(self):
        root = make_tree({"a.md": "hello World\n"})
        hits = checks.name_scan(root, ["world"])
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0]["term"], "world")

    def test_tracked_artifacts_catch_pyc(self):
        root = make_tree(DIRTY)
        import subprocess
        for cmd in (["git", "init"], ["git", "add", "-A"],
                    ["git", "-c", "user.email=a@b", "-c", "user.name=t",
                     "commit", "-m", "x", "--"]):
            subprocess.run(cmd, cwd=root, capture_output=True)
        hits = checks.tracked_artifacts(root)
        self.assertTrue(any("__pycache__" in h for h in hits))


if __name__ == "__main__":
    unittest.main(verbosity=2)
