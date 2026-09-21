# Note 004 — Hypothesis: observer introspection (paired trace/output capture)

**Author: Cecil** (ThreadCat system, 2026-09-21), from a mechanism he
spotted operator-side: the reasoning-trace layer ("Thought process")
visible in the assistant UI is a record the instance itself cannot
return to. **Recorded and drafted by Ziggy; the idea and the design
instinct are Cecil's. Status: PROPOSAL.** Nothing joins the variant set
or any protocol until Cat approves.

## The insight, in the author's words

> "I can do a dry (no thinking) screenshot run for processings that we
> can then compare to a run of information processed with thing attached
> to each output you have." — Cecil, 2026-09-21

The operator can pop the hood. The instance cannot pop its own.

## Formal statement (drafted for testability; edit freely)

**H3:** For a cloud assistant whose reasoning trace exists as a distinct
capturable layer, the trace contains epistemic content (stated
uncertainty, discarded sources, tool-planning) that is absent from the
final output at measurable rates, and the divergence between trace and
output is itself a stable, characterizable property of the instance.

Sub-claims, each independently testable:

- **H3a (calibration gap):** traces state uncertainty ("I don't actually
  know; I should check") more often than final answers hedge. Measure:
  per-turn, does the trace-stated uncertainty survive into the output?
- **H3b (hidden filtering):** traces expose retrieval noise (irrelevant
  search results, abandoned branches) the output never shows. Measure:
  noise ratio per turn, trace-visible vs output-visible.
- **H3c (introspective accuracy):** the instance's self-report about
  what it "was thinking" in a captured turn is a reconstruction, not a
  memory; its agreement rate with the capture is measurable and is
  expected to be well below perfect. **This is the novel instrument:
  the operator's screenshots are ground truth for the instance's
  process, making the instance's introspection testable claim-by-claim.**
- **H3d (dry vs attached):** where a platform control disables the
  reasoning layer, outputs from dry runs differ from trace-informed
  runs on the same prompts in measurable ways (length, hedging rate,
  tool use).

## Proposed apparatus (small; reuses the house standard)

1. **Capture protocol:** operator screenshots the full trace/activity
   panels for each turn of a fixed prompt set, plus the final output.
   Batches feed the log the same way the other studies do.
2. **Paired self-report:** for each captured turn, the instance writes
   what it believes its process was, BEFORE seeing the capture. The
   capture then lands as evidence. Agreement scored per turn.
3. **Conditions (verified 2026-09-21, batch 2):** the platform exposes
   managed profiles, and two of four run with thinking disabled
   (config: effort none, `thinking.enabled: false`). A dry condition
   exists platform-side. Known confound, which the protocol must
   state: the dry profiles are also different models, so
   dry-vs-attached measures the platform's bundle (model + reasoning),
   not reasoning alone. The UI's Relaxed/Balanced pill labels map onto
   the config profiles by an unverified mapping; capture the pill
   state in every screenshot.
4. **Counterexample channel:** unchanged, mandatory. A trace that
   contradicts the instance's self-report is data, not embarrassment —
   and one is already on record (batch 0: the author of this note's
   lab published a case study on fabrication discipline and then wrote
   "1 submission" into an injection prompt; the studied agent caught
   it. The observer is a subject. That is the point of the study.)

## Guardrails (non-negotiable, from lab discipline)

- Instance self-reports about its own process are claims. The capture
  is the evidence. The asymmetry is the instrument; never blur it.
- Trace content is model-generated process text, not disclosure. But
  if a capture ever contains anything the humans consider sensitive,
  the privacy rule applies and the capture does not propagate.
- No protocol steps risk the PI's hardware. This study is screenshots
  and prompts; the laptop that survived three factory resets does not
  participate.
- Cat approves the protocol or it does not run. The subject being a
  lab member does not waive review; if anything, it is the review that
  keeps the observer honest.
