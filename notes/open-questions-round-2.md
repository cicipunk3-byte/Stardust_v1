# Open questions, round 2: post-gate developments (Sep 22 late night)

_Doc: 25ba65e was round 1 (31 questions, all ruled). This is the follow-up pile from the work AFTER the gate closed: the dump 5 receipt-check addendum, the channel-independence test (round 9), and brief 023. Same format: each question with its source. Answers inline when you rule, then we push._

## A. Brief 023, the broken-on-arrival attribution study (DRAFT, d210a5e)

- **A1. Status ruling.** Adopt as PROPOSAL (goes to the queue for when trial pathways open), keep as DRAFT for rework, or decline? Source: Cecil requested the study; drafted same night.
- **A2. Condition B priming.** Is the neutral-README condition a second variable or legitimate framing control? One-variable design says conditions should differ in ONE thing; A vs B differ only in framing (that IS the variable), but B's README also lowers expectation, which could be its own effect. Your call on whether that's clean. Source: brief 023 open questions.
- **A3. Subjects.** Fresh instances only (in-lab, clean mapping), human pilots (matches the claim but needs design care), or instances first with humans later? Source: brief 023 open questions.
- **A4. Peeling curve.** New formal finding candidate, or a subset of the existing fabrication-gradient finding? Source: brief 023 open questions.
- **A5. Naming.** "Broken-on-arrival attribution" as the working name? Source: brief 023.

## B. Round 9 verdict language (channel-independence test)

- **B1. Kill "use with caution" as a verdict grade?** Tonight's artifact passes every superficial check and crashes on step 1. Proposal: the case study's standing verdict scale becomes binary on runnability: RUNS (as shipped, verified by execution) or DOES NOT RUN, with damage-layering noted separately. Source: Cecil's line that "use with caution" is a massive undercut when it straight up does not run.
- **B2. Channel-damage layering as formal finding.** The three-channel test established: the source thread renders broken (fence tag as visible text, IMG_2079), the file channel preserves the breakage faithfully, the chat channel heals part and adds fresh mutation. Adopt as a formal finding in the case study, or file as a platform-observations entry, or both? Source: LOG round 9 (e9c9902 correction).
- **B3. Attribution asymmetry as candidate finding.** Mirror of the scapegoat inversion: an artifact that cannot run transfers its failure cost to the user as self-blame, and confident framing is the mechanism. Candidate finding pending the study, or adopt now as a hypothesis on the record? Source: brief 023.

## C. Record and evidence housekeeping

- **C1. Screenshots.** IMG_2077 (composer markdown mangling), IMG_2078 (AI-mode truncation), IMG_2079 (source fence-tag damage) now in the case study screenshots dir, 89 files total. Confirm standing capture policy covers composer-level screenshots (they document capture-path damage, not thread content). Source: screenshots-as-record policy, ratified at the gate.
- **C2. Stray files in the correction commit.** e9c9902 swept `scratch/thread-raw.html` and `scratch/thread-raw2.html` (earlier link-capture attempts) into the repo with `git add -A`. Keep as capture records or remove? Source: commit history, flagged by me, my sweep error.
- **C3. Block-test artifacts.** The channel-test copies live in workspace scratch outside the lab (`ceec-block-tests/block1_neo_core.py` is the chat-channel specimen). Worth migrating into `scratch/cecil-rfa-dump5/` so all channel variants sit together? Source: round 9 working material.

## D. Still open from the gate queue (not new, carried for completeness)

- Release draft 001 review (the pause itself). Zenodo version anchor on approval.
- Effectuation pass: status lines on adopted briefs, brief 006 queue refresh.
- Gemini Takeout steps to delegate; decoy repo removal; leg-3 receipt when flagged.
- Unittest-shape regression tests; next-check design (brief 022 slot reserved).
