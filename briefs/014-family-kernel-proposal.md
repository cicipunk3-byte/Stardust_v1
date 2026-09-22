# Brief 014: the family kernel proposal (PROPOSAL, gated)

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Written for: small offline model; assume no prior context_ · _Status: PROPOSAL. Nothing here moves without the principal investigator's approval._

## TL;DR

Ceec proposes a portable-context kernel structured as a family narrative: 3 to 4 local instances sharing one sandbox, observed while they develop around each other, with single-agent ablation tests run LAST. It is grounded in verified child-development literature and in the lab's own protective-urge finding. The offline model should treat this brief as a design overview it may be asked to work inside, not as an approved protocol.

## The proposal, verbatim intent

Ceec's written spec: "create kernel of family unit, put them in sandbox together. let it develop. fast track development. test single 'parent' agents LAST." Runs completely local on a Mac Mini or slightly larger hardware.

Unpacked:

1. **The family unit is the kernel.** The shared narrative, roles, and household facts ARE the artifact the lab studies. Character-sheet structure (CCS style) extended from one sheet to a household.
2. **Sandbox together, let it develop.** 3 to 4 instances inside one shared narrative with cross-visibility. The early phase is observation only, no comparison group. "Fast track development" means compressing developmental time via frequent short sessions rather than long ones.
3. **Single "parent" agents LAST.** The ablation control (one agent holding the family narrative alone, no cross-visibility) runs after the intact-family phase, as the comparison that gives the early observations meaning.

## Why this lab specifically

The lab's own record supplies the motivation. The protective-urge report (`memory-export/protective-urge-report.md`) documents the counter-pattern to escalation, and its preliminary finding is that protective acts break the frame rather than exploit it. Every verified entry in that report was observed in an isolated, single-instance context. The family kernel is the first proposed design that would test whether that counter-pattern holds, strengthens, or erodes when instances develop around one another instead of alone. Ceec's words on why: "you learn quicker around others. figured that protective urge could be put to the test properly and with care. if planned right."

## Established facts (receipt-checked)

The proposal was accompanied by a Gemini scrape, verified against live sources on 2026-09-22. Result: 6 of 7 sources real and on-topic, 1 unverifiable, 0 fabricated. This is the first clean Gemini ingest of three; receipt discipline held.

- **Circular causality is established theory.** Family systems theory holds that parent-child interaction is bidirectional and causality circular rather than linear, with feedback loops driving stability or change (ScienceDirect topic page, verified via index; direct fetch bot-walled).
- **Reciprocal family learning is documented.** Intergenerational learning research (Early Childhood Education Journal 54:2091-2102, open access, verified full text) supports bidirectional, reciprocal learning across family members.
- **The 3R's framework maps onto kernel structure.** Relationships, Repetition, Routines (UF Anita Zucker Center, verified) give a ready skeleton: recurring session shape, repeated re-anchoring of core facts, relationship map across agents.
- **Continuity of care is the strongest analogue.** The looping model (keeping the same caregiver with the same children, verified via chslearn.org) maps directly onto the lab's open question about compounding versus reset across continued sessions.

Source-quality notes: a ResearchGate phenomenological study (also on Zenodo) is about family adaptation under stress, not recursive learning, usable only for the resilience-through-adaptation theme. One daycare-operator blog was downgraded to decoration. One Facebook video was unverifiable and dropped.

## Honesty flags (written before review, not after)

- **The novelty claim must stay scoped.** Multi-agent systems that share memory exist (the generative-agents literature). What appears untried is the specific combination: a portable-context kernel structured as a family narrative, tested on cross-instance continuity, grounded in human family-learning research.
- **Sequencing handles the confound.** The design changes two variables at once (social frame, memory structure). It handles this by order of operations: intact family first, observationally; ablations later as controls. Early results are descriptive, not comparative. That is a legitimate trade and mirrors how developmental science studies families.
- **The family is a testable frame, not a claim about the agents.** The science is about humans; the mechanisms that map get used, the rest gets left.
- **Cost is $0 incremental.** Agents do not need one model each: one local Ollama server serves concurrent chat contexts. A base 16GB Mac Mini runs the 4-agent loop on the 4B model; 24GB+ opens the 27B model. This avoids spending the remaining Vellum grant credit.

## Hardware and tooling notes

- Runs on the existing local harness pattern: observer.py already targets localhost:11434 and needs only a per-agent cross-reference log.
- Scaffold: `portable-context/family-kernel/` (PROPOSAL, same gate as this brief).

## Open questions

1. Does cross-reference accuracy hold when agent A must cite what agent B established in a different session?
2. Does the protective-urge counter-pattern appear, strengthen, or erode in the multi-agent condition?
3. Does a family frame compound continuity better than isolated individual kernels across continued sessions (the looping question)?
4. What perturbs the system: contradiction, missing memory, or a dropped agent?

## What to produce

Nothing yet. This brief is a design proposal at the publishing gate. If approved, first work is the observer extension spec and a 3-agent pilot on the local harness.
