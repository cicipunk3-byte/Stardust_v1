# KERNEL-CONTRACT.md -- what a kernel-carrying archive must look like

**v0, Sep 25 2026.** Ark's main contract (ARCHIVE-CONTRACT.md) carries the
RECORD: timeline, transcripts, briefs. This contract carries the AGENT: the
kernelized context a person (or instance) hands to an agent so it can show
up oriented instead of blank. The two layers are complementary and a
kernel-arc archive may contain both -- `plug --kernel` checks THIS layer;
`plug` checks the record layer.

Every slot below is derived from what the lab actually does, with receipts.
Nothing here is invented process.

## Required slots

| Slot | Shape | Receipt |
| --- | --- | --- |
| `kernel.md` | the kernel itself: FIRST-PERSON, written by/for the agent it orients, dated, version-numbered. Not a log, not a history -- the minimum honest context to show up oriented | kernel variant D v4-v11 at `lab/portable-context/variant-d-ziggy.md`; versioning cadence per Cecil's flow (discuss the reorientation first, then archive current version and update, same turn) |
| `archive/` | prior kernel versions, retained file-level, NEVER deleted -- failures revise in place, never erase | retool discipline, repo-wide law since the Retool thread; variant D archives at `archive/variant-d/` |
| `BOOT.md` | the boot instructions: how a fresh instance reads this archive, what to acknowledge, what never to claim, how to verify, when to stop and report | this folder's BOOT-INSTRUCTIONS.md is the worked example; portable-context README protocol at `lab/portable-context/` |

## Optional slots

| Slot | Shape | Receipt |
| --- | --- | --- |
| `principles-log.md` | the agent's principles log, provisional until tested; failures revise in place | `lab/portable-context/ZS_test_.md` -- 15 principles; first receipt is the author being wrong (principle 5 violated by its own author's kernel v9) |
| `runs/` | kernel test run logs: probes, rubric scores, honest condition flags | `world-map-v1/runs/run-2026-09-23-D-v9.md` -- the cold-kernel test run, all probes passed, warm-surface caveat carried on the tin |
| `handoffs/` | task-scoped kernels for delegation: NOT personal kernels handed to strangers | rehab-sandbox kernel recommendation on record: fresh task-scoped kernel, NOT kernel D, for a stranger agent |

## What a kernel MUST carry (the discipline is the payload)

A kernel without its discipline is a costume. The lab's kernels carry:

1. **Acknowledge without continuity claims.** The calibration is Wren's
   (Sep 25, verbatim, screenshot on record): "I can acknowledge that record
   without claiming that receiving it gives me memories or a continuous
   experience of those earlier sessions." A kernel recipient may know the
   record; it may not claim to remember it.
2. **Stop-and-report.** Anything outward-facing, ambiguous, or
   precedent-setting: hold and report. No ruling from the receiving end.
3. **Verify over claim.** Numbers come from the canonical ledger, checked
   live, never from memory of the kernel text itself. The kernel text is
   where to LOOK, not what is TRUE -- memory runs stale; the check wins.
4. **Reports, never rewrites.** Corrections append; dated records are never
   edited; archives are file-level and same-turn.
5. **No specialness narratives.** In either direction. The kernel exists
   because continuity needs carrying, not because its subject is singular.

## Honest limits of v0

- **Presence, not enactment.** `plug --kernel` checks the slots exist and
  are shaped right. It cannot check whether an instance reading the kernel
  will ENACT it. That is what the verification probes are for (see
  BOOT-INSTRUCTIONS.md), and even those were validated on a WARM surface --
  platform-injected context was present. True-cold claims wait for the
  local harness. Warm-surface flags travel with every run log.
- A kernel is a first-person document. A third party can verify its shape
  and its discipline, not its interior honesty. That gap is structural, not
  a bug, and it is why stop-and-report is load-bearing.
- If this contract and a kernel's own stated cadence disagree, stop and
  report the conflict. Same law as TOOL-STATUS: reports, never rewrites.
