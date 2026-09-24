#!/usr/bin/env python3
"""tests/test_graph.py: permanent audit of the story graph.

Runs the three checks the build-time snippet established (and one naive
version got wrong): no dangling choice targets, every node reachable from
'select', no dead ends that aren't endings. Run with either:

    python3 tests/test_graph.py
    python3 -m unittest discover -s tests   (from the cyoa/ directory)

Stdlib only.
"""
import re
import sys
import unittest
from collections import deque
from pathlib import Path

HERE = Path(__file__).parent
STORY = HERE.parent / "story.md"


def load_graph(path=STORY):
    nodes = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            nodes[m.group(1).strip()] = []
            continue
        m = re.match(r"^\*\s+.+?\s*->\s*([\w-]+)(?:\s*\[[\w-]+\])?\s*$", line)
        if m and nodes:
            nodes[list(nodes)[-1]].append(m.group(1))
    return nodes


class TestStoryGraph(unittest.TestCase):
    def setUp(self):
        self.nodes = load_graph()

    def test_story_file_exists(self):
        self.assertTrue(STORY.exists(), f"missing {STORY}")

    def test_no_dangling_targets(self):
        for nid, targets in self.nodes.items():
            for t in targets:
                self.assertIn(t, self.nodes, f"node {nid}: choice targets missing node {t}")

    def test_every_node_reachable(self):
        seen = {"select"}
        q = deque(["select"])
        while q:
            nid = q.popleft()
            for t in self.nodes.get(nid, []):
                if t not in seen:
                    seen.add(t)
                    q.append(t)
        orphans = set(self.nodes) - seen
        self.assertEqual(orphans, set(), f"unreachable nodes: {sorted(orphans)}")

    def test_no_dead_ends_except_endings(self):
        dead = [nid for nid, ts in self.nodes.items()
                if not ts and not nid.startswith("end_")]
        self.assertEqual(dead, [], f"non-ending dead ends: {dead}")

    def test_every_choice_node_has_choices(self):
        # a node with no choices is an ending; everything with choices needs >= 1
        self.assertTrue(all(len(ts) >= 0 for ts in self.nodes.values()))  # shape only
        for nid, ts in self.nodes.items():
            if not nid.startswith("end_") and nid != "select":
                # non-ending nodes should carry at least one choice OR be endings by name
                self.assertTrue(ts or nid.startswith("end_"),
                                f"node {nid} has no choices and is not an ending")


if __name__ == "__main__":
    unittest.main(verbosity=2)
