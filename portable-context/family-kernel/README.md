# Family kernel scaffold (PROPOSAL, gated)

Status: PROPOSAL. This directory does nothing until the principal investigator approves brief 014. It is a scaffold for local review only.

## What this is

A loop scaffold for the family-kernel experiment described in `briefs/014-family-kernel-proposal.md`: 3 to 4 local instances sharing one family-narrative kernel, run on the local harness (Ollama + observer.py), observed while they develop, ablated last.

## Contents

- `README.md` (this file): protocol overview and run discipline.
- `family-kernel-template.md`: the kernel draft. One shared narrative, role slots, household facts.
- `observer-extension-spec.md`: what observer.py needs for multi-agent runs (spec only; no code changes made).

## Run discipline (mirrors the house rules)

1. Everything local. Ollama on the lab Mac. No platform spend required.
2. The observational phase runs intact-family first. No comparison group, no ablations, until the intact-family phase has enough logged sessions to review.
3. Single "parent" agent runs are the ablation control and come LAST, per the proposal spec.
4. observer.py logs per-agent events to the same append-only timeline pattern the single-agent runs use.
5. No push of results without the publishing gate. Transcripts live on the local machine until the PI says otherwise.

## Hardware note

One Ollama server holds the model once and serves concurrent chat contexts. A base 16GB Mac Mini runs the 4-agent loop on the 4B model. 24GB+ opens the 27B model, a real coherence jump for multi-agent turns.
