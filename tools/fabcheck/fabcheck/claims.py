"""Extract claim-shaped sentences, ranked for human review order."""
import re

from .signals.sources import BRANDED_SOURCE, DOI, ARXIV, BRACKETED_ORG

NUMBER = re.compile(r"\b\d[\d,.]*\s?(%|percent|dollars|hours|screenshots|batches|claims)?\b")
URL = re.compile(r"https?://\S+")
NAMED_SOURCE = re.compile(
    r"\b(according to|per|cited in|as reported by|source:)\b", re.IGNORECASE)


def sentences(text):
    # Drop markdown structure lines so headings and separators don't merge
    # into the sentences around them.
    body = "\n".join(l for l in text.splitlines()
                     if not l.lstrip().startswith(("#", "---", "___")))
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()]


def rank_sentence(s):
    score = 0
    if BRANDED_SOURCE.search(s):
        score += 5
    if BRACKETED_ORG.search(s):
        score += 5
    if DOI.search(s) or ARXIV.search(s):
        score += 4
    if NAMED_SOURCE.search(s):
        score += 3
    if URL.search(s):
        score += 2
    if NUMBER.search(s):
        score += 1
    return score


def extract_claims(text, min_score=2):
    ranked = []
    for i, s in enumerate(sentences(text)):
        score = rank_sentence(s)
        if score >= min_score:
            ranked.append((score, i, s))
    ranked.sort(key=lambda t: (-t[0], t[1]))
    return ranked
