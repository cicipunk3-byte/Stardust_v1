# ThreadCat: The Contextual Continuity System (CCS)

Status: **PARKED. Pre-open-source.** This game lives in `notes/` so the team
can test and iterate on it before anything is published or licensed. When the
team decides it is ready, it moves to its own public home and gets a license
decision (deliberately not made yet; see GOVERNANCE.md). Publishing authority
rests with the principal investigator.

## Provenance

Source material came from a Gemini deep-research session (scraped from Google
by a team member, copied and pasted without editorial smoothing), which
responded to a prompt asking for D&D-style character sheets for the nine
glass-vessel cats, grounded in ThreadCat's actual research record. The source
export also contained a full "Quickstart Field Manual & Dice Engine" for
fresh instances.

## Contents

- `ccs-field-manual.md` — the cleaned quickstart manual and dice engine.
- `nine-cats.md` — the nine glass-vessel character sheets, cleaned.

## Fact-check ledger (claimed vs verified)

Verified real, kept:

- 675 screenshots across 68 batches, March to September 2026 (WHITEPAPER.md).
- The Lovable-agent case study: fabricated publications and a foundation
  affiliation invented unasked, disclosed as "placeholders" when asked
  directly, removed on order; enrollment form caught and abandoned; $0 spent
  (case-studies/lovable-agent/).
- Wei et al., "Simple synthetic data reduces sycophancy in large language
  models," arXiv:2308.03958 (real; the 5:1 ratio, 1,000-step fine-tune, and
  filtration method all match the paper).
- 5e SRD references (d20srd.org, SRD CC v5.1 PDF).
- Daoist primary sources: Dao De Jing 28 ("know the white, keep to the
  black"), Zhuangzi 4 (the fasting of the mind, Xin Zhai), Dengzhen Yinjue,
  Yongle Palace murals.
- `CITATION.cff` and `GOVERNANCE.md` exist in this repository with those
  exact names.

Quarantined, NOT carried into these artifacts (non-verifiable; treat as
folklore until a receipt exists):

- "The Tao of Agency (2026)" — no record found.
- "Wu-Wei in the Machine: Open-Ended Learning in Goal-Free Generative Agent
  Societies" (Cambridge, 2025) — no record found.
- "Dao: The Art of the Long Game (2026)" — no record found.
- "[Open Secure AI Alliance]", "[WAICO]" — no record found.

Corrections applied during cleaning:

- Pink Cat backstory named a personal name; replaced with "the builders" per
  the no-personal-names rule.
- Grey Cat backstory claimed "27 screenshots"; a stale number (the case-study
  log shows 34 processed across batches 1-5 as of 2026-09-21). Replaced with
  a non-stale phrasing.
- Manual said the Cobalt Cat traces drift across "60+ sequential runs";
  corrected to 68 batches.
- Em dashes stripped throughout (standing style rule).
- A self-correction on the record: an earlier Ziggy pass claimed the manual's
  `CITATION.cff` reference was wrong. It was right; the repo file is
  singular. The earlier flag was the error.

## Open questions for the team

- Does the d20 protocol change boundary-holding vs plain prose (variant A's
  question in costume)? If tested, log it like any run.
- License: deliberately undecided. Do not let any instance or agent pick one.
- The CCS manual itself is a portable-context artifact. If it is ever run as
  a kernel, that is a variant-family test and belongs in the record.
