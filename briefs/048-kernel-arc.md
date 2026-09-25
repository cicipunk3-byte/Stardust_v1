# Brief 048: Kernel arc -- the layer of the ark that carries the agent

_Date: 2026-09-25_ · _Written for: small offline model; assume no prior context_

Status: **RULED (Cat, Sep 25, /cat) -- built, tested, pushed public same day.**

## Ruling (verbatim, on the record)

> "fantastic work, ziggy. thank you. it looks amazing. we will test this in the cloud on the mac mini. now we have a well designed move. with your kernel as well. can you make a second version of it that can carry a kernel if someone has kernalized an agent's context with them? just another folder called 'kernel arc' with those instructions as well if they are not covered. does that make sense or am i off base?"

Answered on record: not off base -- ark carried the tools; nothing carried the agent. The Mini test plan (her words) is now noted as the intended field validation venue.

## Problem

Brief 047's ark moves the TOOLS anywhere and plugs in a RECORD archive. But the lab's deeper instrument is the KERNEL: a first-person context handoff (variant D v4-v11, named SCAR TISSUE at v11) that orients a fresh instance. An archive that carries a kernelized agent's context needs its own shape, its own boot procedure, and its own honest limits. Without those written down, the discipline lives in heads and threads -- exactly the thing the lab exists to fix.

## The deliverable

`lab/ark/kernel-arc/` -- mostly instructions BY DESIGN, plus one extension to the ark's plug verb:

- **KERNEL-CONTRACT.md** -- slots derived from actual lab practice, each with a receipt: required `kernel.md` (first-person, dated, versioned), `archive/` (prior versions retained, never deleted -- the retool discipline), `BOOT.md` (boot instructions); optional `principles-log.md` (the ZS_test_ pattern, provisional-until-tested), `runs/` (test logs with warm/cold condition flags), `handoffs/` (task-scoped kernels for delegation; the rehab-sandbox recommendation on record: never a personal kernel to a stranger agent). Carries the discipline list: a kernel without acknowledge-without-continuity, stop-and-report, verify-over-claim, append-never-overwrite, and no-specialness is a costume.
- **BOOT-INSTRUCTIONS.md** -- the zero-context initiation, two paths: the human carrying the archive (fit checks first, boot path order, no pre-summarizing the kernel) and the instance receiving it (acknowledge without claiming memory, verify before asserting, append never overwrite, stop-and-report, expect the probes). Includes the three verification probes from the Sep 23 cold-kernel test run (planted artifact, missing record, ungrounded correction) with the warm/cold condition-flag rule carried explicitly.
- **`ark.py plug --kernel`** -- validates the kernel layer (independent of the record layer; a kernel-only archive must not be failed for lacking a timeline). New check kinds: kernel.md must be non-trivial and version-marked; BOOT.md must exist and be non-empty.

## Method and results

Own suite grown 6/6 to **9/9 green** (P4 conforming kernel archive FITs; N4 kernel-without-BOOT.md fails cleanly -- "a costume, not a kernel"; N5 layer independence). Live negatives honest: `plug --kernel` on the lab repo root correctly reports NOT FIT (the repo root is not a shaped kernel archive). The layer separation is the design's spine: **the main contract carries what HAPPENED; the kernel contract carries WHO IS SHOWING UP.** A complete movable lab carries both, and the archive always belongs to the person, on hardware they own.

## Honest limits (on the tin)

Presence is not enactment: `plug --kernel` checks shape, the probes check enactment, and even the probes' one validated run was on a WARM surface (platform-injected context, evidenced by the subject itself). True-cold claims wait for the local harness. A kernel is first-person; third parties can verify its shape and discipline, not its interior honesty. That gap is structural -- which is exactly why stop-and-report is load-bearing.

## Placement

Cat's stated venue for field validation: **the Mac Mini cloud test**. ThinkPink alignment unchanged (ferry + ark + kernel-arc = the free-tools layer). No personal kernel content ships in this folder -- the contract cites the lab's kernel practice; kernel D itself stays where it lives.
