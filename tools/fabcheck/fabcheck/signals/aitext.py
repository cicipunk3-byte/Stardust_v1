"""AI-text style signals. Correlational. Never a verdict."""
import re
from statistics import stdev, mean

FILLER = [
    "great question", "i'd be happy to", "happy to help", "as an ai",
    "it's important to note", "it is important to note", "delve into",
    "a testament to", "rich tapestry", "in conclusion", "furthermore",
    "moreover", "landscape of", "navigating the", "unlock the power",
    "let's dive in", "game-changer", "seamless", "elevate your",
]

EM_DASH = re.compile(r"\u2014")


def sentence_lengths(text):
    parts = re.split(r"[.!?]+", text)
    return [len(p.split()) for p in parts if len(p.split()) >= 2]


def check_aitext(text):
    findings = []
    words = text.split()
    if not words:
        return findings

    dashes = len(EM_DASH.findall(text))
    dash_rate = dashes / max(len(words), 1)
    if dash_rate > 0.004:  # roughly 1 per 250 words; human prose is rarer
        findings.append(("em-dash density",
                         f"{dashes} em-dashes in {len(words)} words "
                         f"({dash_rate:.4f}/word)", "warn"))

    low = text.lower()
    hits = [f for f in FILLER if f in low]
    if hits:
        findings.append(("filler lexicon",
                         ", ".join(sorted(set(hits))), "warn"))
    if len(hits) >= 4:
        findings.append(("filler pile-up",
                         f"{len(hits)} distinct filler phrases in one document",
                         "flag"))

    lengths = sentence_lengths(text)
    if len(lengths) >= 8:
        spread = stdev(lengths) / max(mean(lengths), 1)
        if spread < 0.35:
            findings.append(("low burstiness",
                             f"sentence-length variation {spread:.2f} "
                             "(uniform lengths correlate with generated text)",
                             "info"))

    return findings
