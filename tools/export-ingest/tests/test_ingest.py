"""End-to-end test on synthetic fixtures shaped like real provider exports."""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))

# ChatGPT shape: list of {title, create_time, mapping tree}
CHATGPT = [{
    "title": "Kernel design chat",
    "create_time": 1758500000.0,
    "update_time": 1758500100.0,
    "mapping": {
        "a": {"parent": None, "children": ["b"], "message": {
            "author": {"role": "user"},
            "content": {"parts": ["design me a continuity kernel"]},
            "create_time": 1758500001.0}},
        "b": {"parent": "a", "children": ["c"], "message": {
            "author": {"role": "assistant"},
            "content": {"parts": ["Here is a draft kernel.", {"type": "image"}]},
            "create_time": 1758500010.0}},
        "c": {"parent": "b", "children": [], "message": {
            "author": {"role": "system"},
            "content": {"parts": ["hidden system text, must be skipped"]},
            "create_time": 1758500011.0}},
    },
}]

# Claude shape: list of {name, created_at, chat_messages}
CLAUDE = [{
    "name": "Resync audit",
    "created_at": "2026-09-21T15:00:00Z",
    "updated_at": "2026-09-21T15:30:00Z",
    "chat_messages": [
        {"sender": "human", "text": "audit the site numbers", "created_at": "2026-09-21T15:00:00Z"},
        {"sender": "assistant", "text": "34 screenshots across 5 batches.", "created_at": "2026-09-21T15:01:00Z"},
    ],
}]

# Garbage that must be skipped loudly, not silently ingested.
GARBAGE = '{"half": '


def setup_fixtures(tmp):
    os.makedirs(os.path.join(tmp, "export"), exist_ok=True)
    with open(os.path.join(tmp, "export", "conversations.json"), "w") as fh:
        json.dump(CHATGPT, fh)
    with open(os.path.join(tmp, "export", "claude-conversations.json"), "w") as fh:
        json.dump(CLAUDE, fh)
    with open(os.path.join(tmp, "export", "broken.json"), "w") as fh:
        fh.write(GARBAGE)


def test_end_to_end():
    tmp = tempfile.mkdtemp()
    out = os.path.join(tmp, "out")
    setup_fixtures(os.path.join(tmp, "export"))

    r = subprocess.run([sys.executable, "-m", "ingest.cli",
                        os.path.join(tmp, "export"), "-o", out],
                       capture_output=True, text=True,
                       cwd=os.path.join(HERE, ".."))
    assert r.returncode == 0, r.stderr
    assert "SKIP" in r.stdout and "broken.json" in r.stdout, r.stdout

    idx = open(os.path.join(out, "INDEX.md")).read()
    assert "Kernel design chat" in idx
    assert "Resync audit" in idx

    chat_md = open(os.path.join(out, "chatgpt", "kernel-design-chat.md")).read()
    assert "design me a continuity kernel" in chat_md
    assert "Here is a draft kernel." in chat_md
    assert "hidden system text" not in chat_md, "system messages must be skipped"

    tl = [json.loads(l) for l in open(os.path.join(out, "timeline.jsonl"))]
    assert len(tl) == 2
    providers = {t["provider"] for t in tl}
    assert providers == {"chatgpt", "claude"}
    for t in tl:
        assert t["stub"] is False

    shutil.rmtree(tmp)


if __name__ == "__main__":
    test_end_to_end()
    print("all export-ingest tests passed")
