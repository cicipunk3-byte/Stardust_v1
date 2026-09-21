"""Gemini Takeout stub.

Google Takeout exports Gemini history as HTML (MyActivity.html), not JSON,
and the markup changes without notice. Writing a parser against it silently
produces garbage on format drift, which violates the house rule: mark
failures, do not hide them.

So this stub does the useful part (telling you what you have and what to do)
and refuses to fake the rest. To add a real parser: confirm the current
Takeout markup, write a test fixture from a real export, then replace this.
"""

import re
from html import unescape


def parse(conv_or_path):
    path = getattr(conv_or_path, "name", str(conv_or_path))
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            head = fh.read(200000)
    except OSError:
        head = ""

    prompts = re.findall(r'<div class="[^"]*prompt-text[^"]*"[^>]*>(.*?)</div>',
                         head, re.DOTALL)

    return {
        "provider": "gemini",
        "title": "GEMINI TAKEOUT: stub run, prompts extracted raw if any",
        "created": None,
        "updated": None,
        "messages": [
            {"role": "user", "text": unescape(re.sub(r"<[^>]+>", "", p)).strip(),
             "ts": None}
            for p in prompts if p.strip()
        ],
        "stub": True,
        "note": "responses not parsed; markup drift risk. See module docstring.",
    }
