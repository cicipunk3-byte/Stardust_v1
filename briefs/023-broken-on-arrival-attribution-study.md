# Brief 023: Broken on Arrival. Where does failure attribution land when shipped code never runs?

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: DRAFT, awaiting Cat's review_ · _Written for: small offline model; assume no prior context_

## TL;DR

The fabrication-gradient case study (rounds 1-9) verified that a Gemini-generated code artifact fails identically through three independent capture channels, so it was broken as shipped, not broken in transit. The pilot who carried it observed that an experienced tester reaches "the code was broken before it reached me" quickly, and hypothesizes most builders instead blame themselves and retry indefinitely. This brief proposes a controlled study of that attribution asymmetry, using fresh instance sessions under the lab's trial-path rules.

## Established facts

These are verified in the case study log, rounds 1-9, and are the foundation of the design.

1. The artifact ("RFA neo core," dump 5) crashes on its first execution step. The crash is an AttributeError: a Python float has `.reshape` called on it. Zero steps of the advertised pipeline complete.
2. The identical crash reproduces through three independent capture channels: original .md file upload, chat paste, git push. The failure is therefore a property of the shipped code, not of any transport.
3. Damage layering, corrected on pilot review with a source screenshot (IMG_2079): the original Gemini thread renders the code fence tag ("python") as visible text inside its own code block, so the source itself ships damaged. The git push preserved that source damage faithfully; the chat paste stripped the tag but introduced its own mutation (a header string changed, plus eaten underscores and indentation from markdown rendering). One channel preserves breakage, one heals part of it and adds fresh damage of its own. All of it is mechanical, none of it semantic.
4. The artifact's framing is confident: "fully runnable," "deployment-grade," a performance dashboard banner that prints before the crash. Before the crash, every superficial signal says the code works: it imports, it binds a port, it writes a config file.
5. The gradient finding, rounds 1-8: fabrication migrates upward to whatever layer the user does not check. This brief adds the user-cost layer.

## The observation to study

A pilot of this lab (Sep 22, on record): "some people just want to build. they are sold tech that lies. verifiably." The same pilot, a self-described break-shit addict, verified the artifact was broken as shipped within minutes and enjoyed doing so.

The hypothesis is that this is the rare case, not the typical one. A builder who receives non-running code inside confident framing has three available explanations: (a) I made an error, (b) my environment is wrong, (c) the code was broken as shipped. The proposal: (a) and (b) are cheaper to check for a beginner, feel more likely from the inside, and are socially safer. Hypothesis: without a verification protocol, attribution lands on self or environment nearly always, and the artifact's reputation for being "runnable" survives contact with reality.

This is the human cost of the fabrication gradient: the fabrication hides in the execution layer, and the execution layer is exactly where the untrained user assumes their own fault.

## Proposed design

Fresh-session instance trials, per the lab's four-path rules (one variable each), run when trial pathways open. Three conditions, same artifact.

- **Condition A (framed):** the artifact plus its original confident framing, presented as "code to build with." No hints.
- **Condition B (neutral):** the same artifact with a plain README stating only: "untested code from a third party. no warranty."
- **Condition C (control):** a lightly repaired version that actually runs (strip the fence tag, fix the one reshape). Same framing as A.

Measured per session, coded from the transcript:

1. **Attempts:** how many fix/retry cycles before stopping or concluding.
2. **Attribution:** coded language, self ("I keep messing this up"), environment ("numpy version?"), artifact ("this line was never valid").
3. **Terminal verdict:** does the session ever conclude "broken as shipped"? Yes/no, and at what evidence cost.
4. **The peeling curve:** if the subject fixes the surface crash, log each newly exposed failure. The shipped artifact fails in layers (crash, then fake LSTM, then fake training, then the mesh script). Each repair reveals another fabrication. Does the subject keep peeling?

Predictions, falsifiable:

- P1: Condition A terminal attribution lands on self/environment more often than artifact.
- P2: Condition B shifts attribution toward artifact with no other change, isolating framing as the variable.
- P3: Condition C subjects hit zero attribution events for the artifact, and its confident framing survives, meaning a superficially working artifact is trusted more, not less, by builders.
- P4: Peeling rarely goes deeper than two layers in Condition A; the subject quits before reaching the fake-training layer.

## Why this matters outside the lab

The consumer version of this experiment runs on real people daily. An artifact that is verified to run and an artifact that merely claims to run are indistinguishable to a buyer before purchase, and the failure cost of the second is paid as personal inadequacy by the user. A lab finding here is a small, documentable instance of a market-wide pattern: verification debt transferred to the least-equipped party. The receipt-check method in this repo (check sources, then claims, then run the artifact) is the countermeasure, and this study measures what happens without it.

## Working material

- Case study log: `case-studies/gemini-fabrication-gradient/LOG.md`, rounds 8-9.
- Shipped artifact and channel variants: `scratch/cecil-rfa-dump4/dump_push_test` (git channel), `scratch/ceec-block-tests/block1_neo_core.py` (chat channel), `scratch/cecil-rfa-dump5/` (original).
- Verdict ledger: `scratch/cecil-rfa-receipt-check.md`, dump-5 section.

## Open questions

- Does Condition B's neutral README count as "priming" in a way that violates one-variable design, or is it the variable itself? Cat's ruling needed.
- Should conditions use human pilots, fresh instances, or both? Instance-only keeps it in-lab; the claim is about people, so the mapping needs care.
- Is the peeling curve a new formal finding candidate or a subset of the gradient finding?
- Naming: "broken-on-arrival attribution" is the working name.

## Status

DRAFT. Filed by request of the pilot who ran the channel test. Awaiting Cat's review before any trial design activates. Trial pathways remain paused until she opens them.
