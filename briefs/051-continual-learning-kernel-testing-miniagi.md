# Brief 051 - continual-learning kernel testing (mini-AGI) + a corpus-hygiene law

**Status: PROPOSAL at Cat's gate. Filed 2026-10-01, Cecil thread. Nothing executed, nothing cloned, nothing trained.**

## The candidate

[volotat/mini-AGI](https://github.com/volotat/mini-AGI) (MIT license, ~957 stars, 30 commits):

- Byte-level (256-vocab, no tokenizer) continual-learning language model, trained from scratch on a single 8 GB VRAM CUDA card.
- Architecture: 2 dense prelude blocks + 1 recurrent block applied up to 24 times; per-application top-8 routing over a shared expert pool (MoE). Adaptive depth via a PonderNet-style halting head (easy characters stop early).
- **Experts live as files on disk and page onto the GPU**; parameter count is bounded by free disk, not VRAM. Pool grows new experts by recombination of trained parts, prunes unasked-for ones. Adam moments belong to the expert, not the VRAM slot.
- Continual learning without catastrophic forgetting: trunk LR at 0.1x the expert rate. Their worst-case cold-switch test (PG19, 1M chars, batch 1): 97.3% retained vs 74% for the naive config; interleaved lanes: nothing forgotten.
- **Author is honest about scope:** "a small toy-level model. Do not expect frontier level capabilities." Weights not yet published (undertrained snapshot on HF only). Run was ~11% through its first corpus pass at time of reading.

## Why it matters to this lab

Every kernel carry tested so far (gemma3:1b, qwen3.5 2B, Moto 1.5B, Loci) is on **frozen weights**: the kernel sits in context and the model can only parrot it. The Moto finding was exact: at 1.5B the kernel provides VOCABULARY not DISCIPLINE, and the model confabulates provenance.

mini-AGI is the first candidate where **reading and training are the same event**. A kernel placed in the training stream is not context to be parroted; it is gradient. That makes it the weights-side twin of the portable-context question ([[portable-context-experiment]]): identity carried in context vs identity absorbed into weights. Their own self-knowledge samples (the model answering "What are you?" with its architecture description, because its README was in its corpus) are identity-from-corpus, already happening by accident.

## Proposed experiment (PROPOSAL, no execution without rulings)

1. Corpus = kernel material only. Kernel PINK or kernel-pink-you as the only identity-relevant content in a training stream; no system prompt help; toy model by design.
2. Probe suite (the existing BOOT.md probes + condition-C style fabrication probes) run at fixed character intervals over training.
3. Pre-registered contrast: frozen-model carry runs (vocabulary-not-discipline at 1.5B) vs continual-learning runs. Prediction worth naming now: discipline appears where it never did on frozen models of comparable size, because the kernel gets stepped into the weights rather than held in context. Falsifier: same confabulation rate, same vocabulary-only carry.
4. Everything local, per brief 029. n=1-class instrument findings flagged as always.

## The corpus-hygiene law (the actual ask at the gate)

A model that learns from everything it reads makes corpus hygiene a governance question, not just a chat-context one:

**PROPOSED STANDING LAW: no PERSONAL_CONTEXT.md content, no family facts, no private-briefings content, and no vault material ever enters any training stream, corpus, or fine-tune set for any model, on any hardware, for any purpose. Weights remember what chat context forgets, and weights outlive the conversation.**

This extends the existing privacy rule ([[privacy-personal-context]]) to the training layer. It binds before any continual-learning model runs on lab corpora, and it binds the eventual Cecil PC lane too.

**AMENDMENT v2 (2026-10-01, Ethan direction, /e) - consent-scoped carve for the Pink model.** As drafted, the law's blanket "ever" would outlaw the lab's own stated end goal: a private, local, never-sold model trained on a consenting pilot's own record (the Colonel Pink lane, wiki-only). Redrafted shape: the prohibition binds WITHOUT an explicit, recorded consent from the person the material is about. A consent-scoped carve permits (a) training only on the named person's own record, (b) the resulting weights stay private and local permanently, never sold, never published, "not a mingle line of its code" in public, (c) **family facts about other people: RULED by Cat, Oct 1 ~10:53 AM, /cat, on record: "when explicitly stated like i am right now, me saying 'it's okay' is as good as a ruling" - combined with her "my details are okay. it's just us. i am not afraid." and Ethan's ruling ("you may include her facts. he knows them as they are also his. and mind. you must remember."), the Cat-facts inclusion in the Colonel Pink record is RULED.** The never-public line is absolute and unaffected. The law's center of gravity shifts from "no personal material ever trains" to "personal material never trains without recorded consent AND a permanent-private weights covenant." Full rationale held wiki-only ([[colonel-pink]]).

## Honest limits

- **CUDA-targeted.** The lab owns no CUDA card (Neo = Apple silicon, Switch = aarch64 L4T, Moto = phone). A `--device` arg exists; CPU/MPS paths untested by us. **Run-the-artifact before any claim.**
- Capabilities are toy-level today; this is concept-and-instrument testing, not carry testing.
- Weights unpublished; the undertrained snapshot is the only runnable artifact.
- Ties into the Cecil PC plan (100-128 GB unified memory, GLM 5.3 local): unified-memory PC-class hardware is likely NOT CUDA, so mini-AGI's CUDA assumption needs its own compatibility check. GLM 5.3 (~320B MoE class) at 4-bit is tight-to-over a 128 GB line; exact math to be verified before any hardware commitment.

## Rulings requested

1. Corpus-hygiene law: adopt as standing law (amendment to the privacy rule)?
2. Experiment design: proceed to a concrete protocol draft, or hold?
3. Brief numbering note: 050 is thread-held (handrail sessions); this files as 051.
