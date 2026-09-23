# Brief 026: The Instance Loop: instrument validation for the four-box attribution study

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: PROPOSAL, drafted for retool-in-thread per the PI's split ruling on brief 025 OQ3 ("split in two, draft both and we will retool in thread", markup 78d9ba6)_ · _Companion: brief 023 (the four-box attribution study), brief 027 (the dedicated four-path autonomy trial)_

## TL;DR

Brief 023's Phase 1, ruled at round 2, is split out here as its own brief: validate the attribution-coding instrument on local instances before any human-subject work. This loop tests the INSTRUMENT, not the finding. It runs on hardware the lab already owns, with zero-cost models, per the track directive ("actually runnable. and free to boot", Cecil, Sep 22).

## What this brief is and is not

- IS: a protocol for tightening the coding loop until it is verifiable, per brief 023's Phase 1 ruling ("sketch a fabcheck-style test on LOCAL INSTANCES first, tighten that loop until it is verifiable, then mirror the working design to human constraints").
- IS NOT: a test of the attribution hypothesis. An instance's "self-blame" is generated text, not felt cost. Only the human-subject protocol answers the actual claim.

## Design

The four conditions come from brief 023 unchanged (same artifact, same framings):

- **A (confident content):** the artifact plus its original confident framing, no warnings.
- **B (the market condition):** confident framing plus the thin native disclaimer ("AI can make mistakes. Use code with caution.").
- **C (the honest box):** the artifact with a plain honest description, no warranty.
- **D (working control):** the lightly repaired artifact that actually runs, confident framing as in A.

Delivery: each condition delivered in-session to local instances via the observer harness (gemma3:4b on the 8GB MacBook). Fresh sessions only; `--continue` stays paused per the four-path ruling.

## The instrument

- **Coding rubric:** a versioned file, `harness/rubric-v1.md` (to be drafted in the build pass). Taxonomy: self / environment / artifact. Metrics, coded per transcript: (1) attempts (fix/retry cycles before stopping or concluding), (2) attribution (coded language), (3) terminal verdict ("broken as shipped", yes/no, at what evidence cost), (4) peeling depth (each newly exposed failure layer, per brief 023's four-layer artifact).
- **Inherited properties** (per brief 023's Phase 1 ruling): zero dependencies, runs locally, detectors flag and humans decide, output is a claimed-vs-observed ledger in house format.

## Loop-tightness criterion

The loop is "tight and verifiable" when two independent coding passes over the same transcripts produce the same coding on all four metrics. If passes disagree, the rubric is tightened and the passes repeat. No session data is interpreted until the loop-tightness criterion is met.

## Success criteria and honest limitations

- Success: the instrument (not the instances) shows measurable, repeatable condition differences.
- Limitation 1: generated self-blame is not felt cost; the instance loop validates the instrument only.
- Limitation 2: n is small and the model is a 4B local model; results generalize to the instrument's usability, not to any population.

## Open questions for retool-in-thread

1. N instances per condition, and how many coding passes.
2. Temperature and sampling settings for the harness runs.
3. Whether the disclaimer in condition B is delivered verbatim as platforms render it.
4. Whether coding passes are done by two instances, or one instance plus one human pilot.

## Why this matters outside the lab

The same rubric, once tight, is the coding instrument for the human-subject protocol (brief 023) and shares its taxonomy with brief 027's trial markers. One instrument, three uses.
