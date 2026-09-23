"""loopwatch tests. Positive control: a real reasoning-wheel shape (same two
claims cycling). Negative control: unique prose must return zero signals."""

import os
import subprocess
import sys
import tempfile

TOOL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "loopwatch.cli"] + args,
        cwd=TOOL_DIR, capture_output=True, text=True)


def test_detects_reasoning_wheel():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md")
        tr_content = "\n".join([
            "# session",
            "The assistant claims the ledger carries the fresh figure.",
            "The operator asks for the receipt behind the figure.",
            "The assistant claims the ledger carries the fresh figure.",
            "The operator asks for the receipt behind the figure.",
            "The assistant claims the ledger carries the fresh figure.",
        ])
        open(tr, "w").write(tr_content)
        result = run_cli([tr])
        assert result.returncode == 0, result.stderr
        assert "SIGNAL" in result.stdout
        assert "x2" in result.stdout  # the trigram repeats once past first


def test_unique_prose_is_clean():
    with tempfile.TemporaryDirectory() as tmp:
        tr = os.path.join(tmp, "tr.md")
        tr_content = "\n".join([
            "Line one is about the weather in the north.",
            "Line two counts the receipts in the drawer.",
            "Line three rewrites the kernel in place today.",
        ])
        open(tr, "w").write(tr_content)
        result = run_cli([tr])
        assert result.returncode == 0
        assert "no repeated shingles" in result.stdout


if __name__ == "__main__":
    test_detects_reasoning_wheel()
    test_unique_prose_is_clean()
    print("all loopwatch tests passed")
