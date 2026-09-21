"""Optional local-model opinion via ollama. Never counts as verification."""
import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:4b"

PROMPT = """You are a claim auditor. For the sentence below, answer in exactly this form:
VERDICT: checkable|opinion|unfalsifiable
WHY: one sentence
WHAT WOULD VERIFY IT: the specific receipt a human should look for
Sentence: {sentence}"""


def judge_claim(sentence, model=MODEL, timeout=60):
    """Returns the model's raw response text, or raises. Local only, no cost."""
    payload = json.dumps({
        "model": model,
        "prompt": PROMPT.format(sentence=sentence),
        "stream": False,
    }).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())["response"]
