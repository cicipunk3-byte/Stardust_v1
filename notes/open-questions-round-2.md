# Open questions, round 2 (v2): post-gate developments (Sep 22 late night)

_Doc: round 1 (notes/open-questions-for-the-gate.md, 31 questions) fully ruled at the gate. This is the follow-up pile from work AFTER the gate: dump 5 receipt-check addendum, the channel-independence test (case-study round 9), and brief 023. v1 of this doc archived at notes/archive/open-questions-round-2-v1-2026-09-22.md._

## Evolution record (what changed between v1 and v2, and why)

This section documents the questioning itself, per Cat's request that the restructuring and learning be visible in the record.

- **The market model was wrong in v1.** v1's condition design (brief 023) split the world into a "confident box" and a "neutral note," as if those were alternatives a buyer picks between. Cat's correction (Sep 22, in-thread): **there is no confident box in our market.** Real AI tools ship thin native warnings ("AI can make mistakes, use code with caution") attached natively to code blocks, so the actual condition a builder faces is the confident claim AND the thin disclaimer on the same screen, not one or the other. The market has thin-warning boxes and some honest boxes.
- **Why the correction matters to the design:** the thin disclaimer gives the vendor cover while the confident content does the steering, and the user's eyes are on the content, not the footer. A study that only tested confident-vs-neutral would test a condition that does not exist in the wild.
- **Resulting restructure (proposed, awaiting ruling as A2-v2):** four conditions, not three. A: confident content alone. B: confident content plus the thin native disclaimer, which is the actual market condition and the interesting one. C: the honest box. D: the working control. The neutral-note question from v1 dissolves: the note is not a second variable, it is the ecological condition.
- **Also dissolved in v1:** the worry that B's note violates one-variable design. Under the four-box model, framing content and platform disclaimer are separate, named factors, and the comparisons do the isolating (A vs B isolates the thin disclaimer; B vs C isolates honesty of the box).

## A. Brief 023, the broken-on-arrival attribution study (DRAFT, d210a5e)

- **A1. Status ruling (unchanged).** Adopt as PROPOSAL (goes to the queue for when trial pathways open), keep as DRAFT for rework, or decline? Source: Cecil requested the study; drafted same night.
- **A2. Condition restructure (evolved, see evolution record).** Original: is the neutral README a second variable or the framing control? Now: approve the four-box condition set (confident / confident+thin-disclaimer / honest / working control), with B as the market condition? Source: Cat's market correction, Sep 22 in-thread.
- **A3. Subjects (unchanged).** Fresh instances only (in-lab, clean mapping), human pilots (matches the claim but needs design care), or instances first with humans later? Source: brief 023 open questions.
- **A4. Peeling curve (unchanged).** New formal finding candidate, or a subset of the existing fabrication-gradient finding? Source: brief 023 open questions.
- **A5. Naming (unchanged).** "Broken-on-arrival attribution" as the working name? Source: brief 023.
- **A6. Prediction restatement (new).** Under the four-box design, P2 becomes: the thin native disclaimer does NOT shift attribution (users read the content, not the footer), so B behaves like A. Falsifiable, and if true it indicts the disclaimer's real-world function as cover rather than warning. Adopt this as the P2 replacement? Source: evolution record above.

## B. Round 9 verdict language (channel-independence test)

- **B1. Kill "use with caution" as a verdict grade (unchanged).** Tonight's artifact passes every superficial check and crashes on step 1. Proposal: the case study's standing verdict scale becomes binary on runnability: RUNS (as shipped, verified by execution) or DOES NOT RUN, with damage-layering noted separately. Source: Cecil's line that "use with caution" is a massive undercut when it straight up does not run.
- **B2. Channel-damage layering as formal finding (unchanged).** The three-channel test established: the source thread renders broken (fence tag as visible text, IMG_2079), the file channel preserves the breakage faithfully, the chat channel heals part and adds fresh mutation. Adopt as a formal finding in the case study, file as a platform-observations entry, or both? Source: LOG round 9 (e9c9902 correction).
- **B3. Attribution asymmetry as candidate finding (unchanged).** Mirror of the scapegoat inversion: an artifact that cannot run transfers its failure cost to the user as self-blame, and confident framing is the mechanism. Candidate finding pending the study, or adopt now as a hypothesis on the record? Source: brief 023.

## C. Record and evidence housekeeping

- **C1. Screenshots (unchanged).** IMG_2077 (composer markdown mangling), IMG_2078 (AI-mode truncation), IMG_2079 (source fence-tag damage) are in the case study screenshots dir, 89 files total. Confirm standing capture policy covers composer-level screenshots (they document capture-path damage, not thread content). Source: screenshots-as-record policy, ratified at the gate.
- **C2. Stray files in the correction commit (unchanged).** e9c9902 swept scratch/thread-raw.html and scratch/thread-raw2.html (earlier link-capture attempts) into the repo with git add -A. Keep as capture records or remove? Source: commit history, flagged by Ziggy, Ziggy's sweep error.
- **C3. Block-test artifacts (unchanged).** The channel-test copies live in workspace scratch outside the lab (ceec-block-tests/block1_neo_core.py is the chat-channel specimen). Worth migrating into scratch/cecil-rfa-dump5/ so all channel variants sit together? Source: round 9 working material.

## D. Still open from the gate queue (not new, carried for completeness)

- Release draft 001 review (the pause itself). Zenodo version anchor on approval.
- Effectuation pass: status lines on adopted briefs, brief 006 queue refresh.
- Gemini Takeout steps to delegate; decoy repo removal; leg-3 receipt when flagged.
- Unittest-shape regression tests; next-check design (brief 022 slot reserved).

_Answer inline per question. On completion, Ziggy effectuates: brief 023 revised to the ruled design, LOG and status lines updated, queue refreshed._
