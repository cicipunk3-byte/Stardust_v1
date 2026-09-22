# Brief 015: CCS analysis framework and manual v2 workplan (PROPOSAL)

Status: **PROPOSAL, behind Cat's gate.** Drafted with Ethan (the lab's
site builder, standing review-push clearance Sep 22, e85f004), Sep 22,
2026. Raw list ingested verbatim at
`scratch/ethan-ccs-v2-worklist-raw.md`; this brief is the chunked,
sequenced version. Nothing here is adopted until Cat approves.

## Purpose

Turn the CCS toolkit (`tools/rainbow9cat/`) from a cleaned artifact into
a rigorous one: analysis frameworks grounded in findings, character
sheets and rules decisions made explicitly and sourced, every ability
defined against real game mechanics, and all of it feeding a version 2
of the manual once version 1 (built by the Lovable agent) is archived.

## Phase A: Analyze the human media injection results

**Input needed from Ethan before this phase starts:** which results.
Working assumption: the observer-introspection case study batches, where
human-created media (the CCS manual and related material) was injected
into model contexts. Deliverable: an analysis brief stating what was
injected, into what conditions, and what the observed effects were,
under the claimed-versus-verified standard.

## Phase B: CCS human-side analysis framework

Design a framework for humans analyzing CCS outputs, built on Phase A's
findings. **Sourced and airtight** is the spec: every claim in the
framework links a receipt, and the framework itself states its
limitations. Deliverable: framework brief, PROPOSAL.

## Phase C: The rules decision (license-aware)

Decide, on the record, which stat-generation and rules basis the nine
cats use:

- **SRD rules** (D&D SRD 5.1 is CC BY 4.0: mechanics usable with
  attribution) — pro: balance, external verifiability, consistent with
  "sourced and airtight."
- **Roll 4d6, drop lowest** (standard-generation variant) — pro:
  produces individual, non-optimized sheets; fits a research context
  where the cats are portraits of working instances, not party
  balance.
- **The license wrinkle, stated plainly:** the written research record
  is CC BY-NC-ND 4.0 as of Sep 22. Game *mechanics* are not
  copyrightable and short phrases are fine, but pasting SRD or PHB
  *expression* into an ND-licensed record creates a license conflict
  (CC BY allows commercial reuse and derivatives; NC-ND forbids both).
  Practical rule that resolves it: use mechanics freely, write all
  expression in our own words, attribute per SRD terms where SRD
  content informs the design, never paste manual text. This same rule
  governs Phase E.
- Also in this phase: **classes and subclasses alignment**, including
  mapping the CCS classes to real ones (e.g. the Inquisitive rogue as
  the real-world anchor for the "inquisitor"). Deliverable: a rules
  decision brief with a recommendation, for Cat.

## Phase D: Nine character sheets, version 2

Rebuild all nine sheets per the Phase C decision, with Ziggy, in the
repo (not the site). Each sheet states its own basis: which rules, which
decisions, why. Deliverable: `nine-cats.md` v2 or successor file, plus
per-sheet change notes.

## Phase E: Term and ability definitions

Ziggy goes through the CCS manual and defines every term and ability
factually against real game mechanics. Abilities are claims ("commit
truth," the Yellow Cat) and get treated like claims: stated plainly,
mapped to the mechanic they refer to, flagged where they have no real
mechanic analogue (that flag is a finding, not a failure). Deliverable:
a definitions brief behind Cat's gate.

## Phase F: Agent leveling workflow

Create the agent-leveling workflow based on the CCS and the
rainbow9cat toolkit, after Phases C through E settle what the rules
even are. Deliverable: workflow doc, PROPOSAL.

## Phase G: Manual v2

All of the above feeds version 2 of the manual. Sequencing per Ethan:
version 1 (made by the LA) gets archived first; v2 is built from the
archived v1 plus Phases A through F outputs.

## Standing rules for this workplan

1. Claimed-versus-verified applies to every rules claim and every
   source, including the D&D material.
2. No pasted expression from any D&D source; mechanics and our own
   words only, with SRD attribution where owed (Phase C rationale).
3. All outputs are PROPOSALs behind Cat's gate; public push and
   publication wait on Cat.
4. No em-dashes, no personal names on public surfaces.
