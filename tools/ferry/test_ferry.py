#!/usr/bin/env python3
"""ferry tests. House method: real-failure positive controls + clean negative
controls, run from this directory via `python3 -m unittest test_ferry -v`.

Positive controls are neutralized versions of the two REAL failures from the
Sep 25 maintenance sweep that motivated this tool:
  - attribution drift (a gate/account attributed to the wrong pilot), and
  - a brief-number collision across collections (two briefs took 044).
All pilot names are scrubbed from fixtures; the structure of each failure
is what the controls preserve.
"""

import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).parent
FERRY = HERE / "ferry.py"
sys.path.insert(0, str(HERE))
import ferry  # noqa: E402


def make_tree():
    """A minimal workspace skeleton with the zones ferry knows about."""
    root = Path(tempfile.mkdtemp(prefix="ferry-test-"))
    for d in ("memory/concepts", "memory/archive", "lab/briefs",
              "lab/source-material", "private-briefings", "scratch/thread-export"):
        (root / d).mkdir(parents=True, exist_ok=True)
    return root


def write(root, rel, text):
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


CLAIMS_ATTRIBUTION = json.dumps({
    "claims": [{"id": "gate-owner",
                "forbidden": ["blue's gate"],
                "note": "gate belongs to RED"}]
})


def run(argv):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = ferry.main(argv)
    return code, buf.getvalue()


class TestSweep(unittest.TestCase):
    def setUp(self):
        self.root = make_tree()
        self.claims = write(self.root, "claims.json", CLAIMS_ATTRIBUTION)

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_sweep_flags_active_zone_as_fix_in_place(self):
        """P1 (real failure, neutralized): stale gate attribution on an ACTIVE
        surface must be flagged FIX IN PLACE and exit 1."""
        write(self.root, "memory/concepts/note.md",
              "the proposal sits at blue's gate for review.")
        code, out = run(["sweep", "--claims", str(self.claims), "--root", str(self.root)])
        self.assertEqual(code, 1)
        self.assertIn("FIX IN PLACE", out)
        self.assertIn("note.md", out)

    def test_sweep_flags_append_only_as_correction_only(self):
        """P2 (house discipline): the same pattern in an APPEND-ONLY zone must
        be flagged 'append correction only' and must NOT fail the build --
        the record is never rewritten."""
        write(self.root, "memory/archive/2026-09-25.md",
              "earlier note mentioned blue's gate.")
        code, out = run(["sweep", "--claims", str(self.claims), "--root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertIn("APPEND CORRECTION ONLY", out)

    def test_sweep_clean_tree_exits_zero(self):
        """N1: clean surfaces, zero findings, exit 0."""
        write(self.root, "memory/concepts/note.md", "nothing to see here.")
        code, out = run(["sweep", "--claims", str(self.claims), "--root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertIn("CLEAN", out)

    def test_sweep_bad_claims_file_is_a_clean_error(self):
        """N2: malformed claims file exits with a message, not a traceback."""
        bad = write(self.root, "bad.json", "{not json")
        with self.assertRaises(SystemExit):
            run(["sweep", "--claims", str(bad), "--root", str(self.root)])


class TestCollisions(unittest.TestCase):
    def setUp(self):
        self.root = make_tree()

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_cross_collection_collision_is_caught(self):
        """P3 (real failure, neutralized): the same brief number filed in both
        collections must be reported and exit 1."""
        write(self.root, "lab/briefs/044-first.md", "# Brief 044")
        write(self.root, "private-briefings/brief-044-second.md", "# Brief 044")
        code, out = run(["collisions", "--root", str(self.root)])
        self.assertEqual(code, 1)
        self.assertIn("CROSS-COLLISION", out)
        self.assertIn("044", out)

    def test_within_collection_duplicate_is_caught(self):
        """P4: two files claiming the same number in ONE collection."""
        write(self.root, "lab/briefs/044-first.md", "# Brief 044")
        write(self.root, "lab/briefs/044-second.md", "# Brief 044 again")
        code, out = run(["collisions", "--root", str(self.root)])
        self.assertEqual(code, 1)
        self.assertIn("DUPLICATE", out)

    def test_clean_collections_exit_zero(self):
        """N3: unique numbers across both collections."""
        write(self.root, "lab/briefs/044-first.md", "# Brief 044")
        write(self.root, "private-briefings/brief-045-second.md", "# Brief 045")
        code, out = run(["collisions", "--root", str(self.root)])
        self.assertEqual(code, 0)
        self.assertIn("CLEAN", out)

    def test_archive_copies_do_not_count(self):
        """Archived priors keep their old numbers by design; they must not
        trip the collision check."""
        write(self.root, "lab/briefs/044-first.md", "# Brief 044")
        write(self.root, "lab/briefs/archive/044-first-v1.md", "# Brief 044 prior")
        code, out = run(["collisions", "--root", str(self.root)])
        self.assertEqual(code, 0)


class TestCarry(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="ferry-carry-"))

    def tearDown(self):
        shutil.rmtree(self.root)

    def test_carry_manifest_hashes_match_shasum(self):
        """P5: the emitted manifest's hashes must match an independent sha256
        computation -- the manifest is the arbiter, so it gets verified
        against ground truth, not against itself."""
        payload = write(self.root, "doc.md", "carry me whole, no pretty versions\n")
        spec = write(self.root, "carry.json", json.dumps({
            "package": "test package",
            "destination": "test folder",
            "files": ["doc.md"],
        }))
        code, out = run(["carry", "--manifest", str(spec)])
        self.assertEqual(code, 0)
        manifest = json.loads((self.root / "MANIFEST-CARRY.json").read_text())
        self.assertEqual(manifest["files"][0]["sha256"],
                         subprocess.run(["shasum", "-a", "256", str(payload)],
                                        capture_output=True, text=True).stdout.split()[0])
        sheet = (self.root / "carry-sheet.md").read_text()
        self.assertIn("doc.md", sheet)
        self.assertIn(manifest["files"][0]["sha256"], sheet)

    def test_carry_missing_file_writes_nothing(self):
        """N4: a missing file means NO partial manifest -- the chain never
        ships an unverified package."""
        spec = write(self.root, "carry.json", json.dumps({
            "package": "test", "files": ["gone.md"],
        }))
        code, out = run(["carry", "--manifest", str(spec)])
        self.assertEqual(code, 2)
        self.assertFalse((self.root / "MANIFEST-CARRY.json").exists())
        self.assertFalse((self.root / "carry-sheet.md").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
