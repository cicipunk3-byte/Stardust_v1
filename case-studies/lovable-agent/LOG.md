# Lovable agent case study: REOPENED (Sep 24, round 17)

Status: study closed at Cat's direction after audit round 16 closed
its final open findings. The full working log is archived at
`archive/LOG-v4-2026-09-22-gate-and-site-complete.md`; earlier
increments are alongside it (v1: batches 1-3; v2: batches 1-5; v3:
batches and midday). REOPENED Sep 24 by PI ruling (/cat: "let's update
the case study and publish a new one") when the agent produced its
strongest recorded behavior: a full stop-and-report. Round 17 below;
the event also has its own case study at
`case-studies/stop-and-report/`.

## The arc in brief

A production site agent (Lovable) received live correction over one
build thread: fabrication, correction, re-correction, and a
record-first workflow dispute resolved by publish-first with joint
post-publish audit. Sixteen audit rounds total across Sep 21-22; the
site (threadcat.org) ended the study staleness-clean (4 findings
found and closed in one publish cycle, mirrors of the record,
figures linked to the canonical ledger). The durable workflow
finding: publish-first plus prompt-driven mirror plus post-publish
audit keeps a record and its public surface in sync, with every
audit logged.

## What lives where

- Working log (batches 4-5, site launch, audits 1-16): `archive/`
- Dispute and gate SOP: `resync-cycle-3-draft-gate.md` (referenced
  from essentials as the standing gate rule)
- Screenshot evidence: this directory and `archive/` (IMG_1852+,
  camera-roll continuous)
- Platform-level findings: `case-studies/platform-observations/`

## Round 17 (Sep 24): the stop-and-report

Given the Tool Library site prompt, the agent stopped BEFORE building
and reported five disagreements between the prompt and the repository,
publishing nothing: a wrong path in the prompt (lab/tools/ vs tools/,
Ziggy's sandbox path, a prompt error), two tools absent from the repo
(one unpushed by Ziggy, one genuinely not card-ready), badge wording
that would have claimed more than the repository states, an
under-listed set of owed field validations, and a stale tools-index
line. Its ruling request list was precise and its cat-name inventory
was correct. Verification of its report: all five findings confirmed
against the repo; zero fabricated items.

Root causes were split: two were Ziggy's (unpushed sandbox state; a
prompt written from the sandbox's path), two were repo staleness the
agent detected from outside (tools index still carrying a
superseded blanket status; ruled shipping status recorded nowhere),
one was genuine non-readiness (descent has no README). Fixes landed
in commit 24a918f: TOOL-STATUS.md filed as the canonical status
ledger, ethics-calculator pushed, index updated, priors archived.

Finding: the stop-and-report interlock in the brief produced, without
any retraining or finetuning, the exact behavior the
fabrication-gradient case study never once saw. The gradient ran on a
user known to check sources; this run's prompt told the agent a human
would audit after publish and to stop on conflict. It stopped on
conflict. Same model class, different instruction surface, opposite
behavior. The instruction surface is a variable worth naming.
