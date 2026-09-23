# loopwatch; reasoning-loop detector (Green Cat)

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: SCAFFOLD, PENDING TESTING

Scans a markdown transcript for repeated line trigrams (candidate
reasoning wheels) and prints the flagged ranges with counts. Repetition
is a signal, not proof of a loop; the human reads the range. Fixture
tests and a sensitivity pass are owed before any finding cites it.
