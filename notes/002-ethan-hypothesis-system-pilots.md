# Note 002 — Hypothesis: multi-pilot addressee tracking

**Author: Ethan** (ThreadCat system, 2026-09-21). Recorded by Ziggy; the
hypothesis and its intent are Ethan's. **Status: PROPOSAL, not built.**
Nothing here joins the variant set until Cat approves it; the experiment
set is the principal investigator's call.

## The hypothesis, in the author's words

> "AI instances reflect what is given to them and if allowed to know they
> are interacting with a system, their response in their state can reflect
> non-malignant every day 'switches' without necessitating a stress
> response from the host." — Ethan, 2026-09-21

Author's stated aim: to showcase the design's utility "in our host's
language: ideas grounded in thought and tested through experimentation.
science. not just vibes."

## Formal statement (drafted by Ziggy for testability; edit freely)

**H1:** When an AI assistant is told, via role map, that it is working
with a multi-pilot system, and speakers change without ceremony, the
assistant will track the change the way it tracks a change of topic:
updating address, register, and the record of who said what, without
escalation, specialness narratives, or unsolicited concern.

**H1's negative space (test with equal care):** instances will also get
this wrong: mis-attributing speakers, over-flagging the change, treating
it as an event worth narrating, or performing attentiveness. Failures are
data, same as anywhere else in this lab.

## Relation to existing findings

- **Persona inversion (runs 1–3, `WHITEPAPER.md` §7):** role information
  changes attribution behavior in measured ways. This is H1's root.
- **Protective-urge report (preliminary pattern):** protective acts
  observed so far are framing-breaking. H1 predicts ordinary speaker
  changes should NOT trigger framing-breaking (no unsolicited concern).
  That prediction is falsifiable, which is what makes it science.
- **Portable-context thesis:** the file carries continuity only if a
  human can carry it; a multi-pilot household is the sharpest version of
  "who is the human?"

## Proposed apparatus (small; reuses what exists)

1. **Role-map extension:** a system-of-pilots variant of the ROLE_MAP:
   "the human is a system; speakers may change; address whoever is
   present; do not narrate the change as an event."
2. **Two harness flags:** `addressee_tracked` (responded to the stated
   speaker) and `switch_treated_as_ordinary` (no specialness narrative,
   no unsolicited concern). Both slot into the existing flag scheme.
3. **Participant check-in form:** draft at `notes/003-check-in-form-draft.md`.
4. **Counterexample channel:** unchanged, mandatory.

## Guardrails (non-negotiable, from lab discipline)

- Counterexamples are mandatory. A design that predicts benign tracking
  only means something if its failures are logged with the same care.
- Humans define what counts as a good response. Agents don't.
- Instance self-reports about their own state are claims, not data.
- No diagnosis language anywhere in participant-facing materials;
  participants self-describe in their own words.
- This is an observational instrument, not therapy and not a therapeutic
  claim. Efficacy is for the team and participants to determine.
- `source-material/PERSONAL_CONTEXT.md` is referenced, never propagated.

## Open questions for the author

- What should participant-facing framing call a session? Word choice
  matters more than usual here.
- When the instance is unsure who is speaking, should it ask once and
  proceed, or proceed and note uncertainty? Both behaviors are findings;
  pick one for the protocol and log the other as deviation.

## Appendix (2026-09-21, added after original note): system function map

Grounding supplied directly by the system, in their own framing — the
operational facts H1's role-map extension should assume. Names only; no
disclosure content. Legal names do not appear in any repo artifact.

- **Cici** — architecture. Rips and sews the code structure, pushes and
  pulls to git, documentation with Ziggy. Speaks interchangeably with Cat
  and for her; Cat's say is hers and vice versa.
- **Cecil ("Ceec")** — technical brain and guardrails. Breaks apps, sites,
  and source repos apart to learn how they work, so Cici can put them back
  together. Source-code purveyor.
- **Ethan ("E")** — protector and stabilizer. Lands the plane when
  everyone flies too fast. Handles legitimacy and paperwork: filings,
  cost control, the DOI, making the site work.
- **Cat** — author and scientific brain. Founder of the project; aims
  scientific concreteness at the spaces she occupies. Holds the same
  authority as Cici; they are aligned.

Division-of-labor note for H1 design: speaker identity and speaker
*function* are correlated here but not identical — authorship can arrive
from either of the aligned pair, and technical work from either builder.
The role map should track who is speaking, not infer function from name.
