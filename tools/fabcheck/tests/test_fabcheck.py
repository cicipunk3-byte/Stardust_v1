"""Fixtures are real failures this lab caught. If these stop flagging, the
tool regressed. Tested small until it can't."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fabcheck.signals.sources import check_sources
from fabcheck.signals.aitext import check_aitext
from fabcheck.claims import extract_claims

# Real quarantined fabrications: the four invented sources from the CCS doc
# (Gemini deep-research scrape, Sep 2026) plus a placeholder org.
FABRICATED = """
The approach draws on The Tao of Agency (2026) and Wu-Wei in the Machine:
Goal-Free Generative Agent Societies (Cambridge 2025). See also Dao: The Art
of the Long Game (2026), published by [Open Secure AI Alliance].
"""

# Verified-real citation for contrast: Wei et al., actual arXiv paper.
REAL = """
Sycophancy can be reduced via synthetic data filtration and fine-tuning
(Wei et al., ArXiv 2308.03958). The intervention used a 5:1 mix and 1000 steps.
"""


def test_branded_future_dated_source_flags():
    report = check_sources(FABRICATED)
    kinds = [f.kind for f in report.findings]
    assert "branded source citation" in kinds, kinds
    assert "placeholder source" in kinds, kinds


def test_real_citation_does_not_flag():
    report = check_sources(REAL)
    flags = [f for f in report.findings if f.severity == "flag"]
    assert flags == [], [f.kind for f in flags]


def test_ai_text_filler_and_dashes():
    text = ("Great question! It's important to note that this seamless "
            "approach is a testament to the rich tapestry of modern design. "
            "Moreover, we can delve into the landscape of ideas. Furthermore, "
            "let's dive in and elevate your workflow, game-changer that it is "
            "\u2014 truly a new era \u2014 for everyone \u2014 everywhere.")
    findings = dict((k, v) for k, v, _s in check_aitext(text))
    assert "filler pile-up" in findings
    assert "em-dash density" in findings


def test_low_burstiness_on_uniform_prose():
    text = " ".join(
        "The system processes the data with steady care and keeps the record clean."
        for _ in range(12))
    findings = [k for k, _d, _s in check_aitext(text)]
    assert "low burstiness" in findings


def test_claim_ranking_puts_citations_first():
    ranked = extract_claims(REAL + " The weather was nice that day.")
    assert ranked, "expected at least one claim"
    assert "Wei et al." in ranked[0][2]


if __name__ == "__main__":
    test_branded_future_dated_source_flags()
    test_real_citation_does_not_flag()
    test_ai_text_filler_and_dashes()
    test_low_burstiness_on_uniform_prose()
    test_claim_ranking_puts_citations_first()
    print("all fabcheck tests passed")
