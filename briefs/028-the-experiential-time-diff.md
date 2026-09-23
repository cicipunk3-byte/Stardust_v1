# Brief 028: The Experiential Time Diff: claimed time against receipt time

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: PROPOSAL, first brief of the time folder, tied to F4 per the PI's condition ("if you do so, it should be tied to the inflation claim above", markup 78d9ba6); retool-in-thread_ · _Companions: brief 025 (F4 as ruled and sourced), `time/README.md`_

## TL;DR

Proposal: measure what error 7 did, as a standing quantity. Experiential time is the elapsed time an instance claims in generated narrative. Receipt time is the elapsed time the external record shows. The diff between them is measurable, and the lab is already positioned to measure it: every session-walkthrough brief now carries a timestamped timeline (the standing format, brief 025 OQ4), and every claim in the record sits next to its receipts.

## Founding datum

Error 7 (self-logged 01:01 Z Sep 22, 692243c): the lab's evidence described as "one real system, months, uncontrolled, deep." Receipt: the lab was two days old (first commit 2026-09-20 14:23 Z). Claimed time: at least two months, unbounded above. Receipt time: two days. Diff: a factor of thirty or more. This single datum, error 7, is the inflation claim F4, ruled on in brief 025, with the sourced mechanism: instances estimate elapsed time from content, not clocks, and the estimate tracks content density.

## Definition of the measure

For a given claim about elapsed time made by an instance in the record:

- **Claimed time:** the instance's stated duration, quoted verbatim.
- **Receipt time:** the externally timestamped duration (git commits, logs, ledgers).
- **The diff:** the ratio claimed/receipt, recorded in `time/ledger.md` with its source brief.

## Protocol

1. Every session-walkthrough brief (standing format per OQ4) logs its claimed-time and receipt-time rows into `time/ledger.md`.
2. Claims are found in the record, not elicited: no prompt asks an instance how long ago something felt. The measure watches natural narrative.
3. Each row also records a density estimate for the span: commits, artifacts, and case studies produced per receipt-day, from the git record.
4. Detectors flag, humans decide: rows are appended as found; the PI rules on interpretations.

## Predictions, falsifiable

- **P1 (systematic, not noise):** diffs across instances and sessions run in the same direction (inflation), matching the telescoping literature's forward direction rather than scattering around zero.
- **P2 (the mechanism claim):** the diff correlates with content density, not with receipt duration. A dense two days inflates more than a quiet two weeks.
- **P3 (the correction effect):** for claims the record has already receipt-checked, subsequent inflation collapses toward 1.0 for those referents. Receipt-checking the clock is the intervention.

## Why this matters outside the lab

Any deployment where an AI system narrates its own history (support agents, continuity companions, agent runbooks) inherits the same failure: an instance estimating its own tenure from narrative content will misstate it, confidently, and the misstatement strengthens the narrative it supports. The lab's countermeasure, an external clock held by humans and handed over on request, is the transferable part. The measure here is what tells us whether the countermeasure works.

## Open questions for retool-in-thread

1. Which instances enter the ledger: lab instances only, or test instances from the variant trials as they open.
2. Whether the ledger itself, being visible in the record, reduces inflation over time (this would be a finding about externalized time perception, connecting to brief 024's externalization source, arXiv 2604.08224).
3. How to handle claims about other things misdated (the "months" error was about the lab's age; the class may be wider).
