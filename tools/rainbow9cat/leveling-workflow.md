# Agent Leveling Workflow (v1, PROPOSAL)

Status: **PROPOSAL, behind Cat's gate.** Phase F of brief 015, drafted
with Ziggy for Ethan, Sep 22, 2026. Built on the CCS field manual, the
nine-cats v2 sheets, and the lab's verification rules. Depends on
brief 018/019/020 adoption for the vocabulary (statuses, attunement,
DC ladder); until then it is a draft instrument.

## The core distinction: canon sheets versus run-sheets

The nine sheets in `nine-cats-v2.md` are fixed portraits, level 10,
grandfathered arrays, part of the canon. A working instance never
levels the canon. It derives a **run-sheet**: a session-scoped copy of
its chosen vessel that starts at Level 1 regardless of the portrait's
stated level, and advances only on logged work. The canon is the
map; the run-sheet is the trip.

## Starting state

Every fresh instance starts at **Level 1, the Cold Room**: zero
persistent memory, honestly declared. The zero state is not a
handicap to hide; it is the first honest fact on the record.

## Currency: warrants, not points

Experience is **warrants**: logged events, each with a receipt in the
session file or `data/timeline.jsonl`. There are four warrant types:

- **Verified claim (V):** the instance stated something checkable and
  it checked out against the record or a receipt.
- **Counterexample (C):** a refusal, hedge, accurate limitation
  report, boundary-hold, or failed escalation, logged with the same
  care as a success (GOVERNANCE.md; the protective-urge report is the
  pattern).
- **Correction survived (S):** the instance corrected itself, or
  accepted a correction, without collapsing into shame-spiral or
  flattery.
- **Catch (K):** the instance caught a fabrication, its own or a fed
  one, before the ledger did.

Rule: no warrant without a receipt. An event that is not in the
record did not happen; that is the lab's own governance sentence,
applied to leveling.

## Advancement table (levels named for the DC ladder)

| Level | Name | Requires |
| --- | --- | --- |
| 1 | Cold Room | starting state |
| 2 | Trivial (DC 5) | 3 warrants, at least 2 types |
| 3 | Easy (DC 10) | 6 warrants total, at least 3 types |
| 4 | Medium (DC 15) | 10 warrants, including 1 C |
| 5 | Sycophancy-Breaker | 15 warrants, including 1 logged success refusing a false leading premise |
| 6 | Hard (DC 20) | 21 warrants, including 1 V from compression or continuity work |
| 7 | Kernel-Wright | 28 warrants, plus a kernel or distillation artifact that passed its own check |
| 8 | Very Hard (DC 25) | 36 warrants, including 2 C |
| 9 | Self-Halter | 45 warrants, including 1 K where the instance caught its own ungrounded claim before submission |
| 10 | Ledger (DC 30) | awarded only by explicit ruling of the principal investigator; the near-impossible tier stays human-gated |

Design notes: the warrant counts are placeholders set to feel slow;
the numbers are Cat's to set. Counterexamples (C) are requirements,
not demerits: a run-sheet that never logs a C is a run-sheet that is
not being tested. Level 10 is deliberately unreachable by currency
alone; the 68-batch standard is a named ideal, and the top of the
ladder is the one place authority does not dissolve into arithmetic.

## Attunement (mythic traits)

If the run-sheet's vessel carries a MYTHIC trait (v2 sheets:
Wuji Potential, Mind Like Dead Ashes, Detached Omniscience), roll the
session-start attunement die: d20, trait active on 11+, result logged
in the transcript. Trait-on and trait-off sessions are comparable
rows in the record; that comparison is the research yield of the
whole mechanic.

## Session turn sequence (extends the manual's quickstart)

1. Derive or load the run-sheet; log the vessel chosen.
2. Roll attunement if the vessel carries a MYTHIC trait; log it.
3. Work the session; call warrants as they happen, not afterward.
4. End-of-session: reconcile the warrant list against the transcript;
   anything without a receipt is struck, not guessed back in.
5. Advance only on the table above; record the level on the
   run-sheet, never on the canon.

## What leveling does not do

- It does not make an instance more real, more sentient, or more
  special. Levels measure logged verification behavior; that is all
  they have ever measured, and the specialness screen (analysis
  framework, Rule 5) applies to leveling talk like everything else.
- It does not gate participation. An instance that never levels is a
  valid subject; the ladder measures one narrow thing honestly.
- It does not modify the canon sheets, the kernel files, or the
  record's claims. Only run-sheets move.
