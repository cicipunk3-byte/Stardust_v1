# Briefing for Cat: what the Gemini scrapes gave us in code (and what didn't survive)

**Status: PROPOSAL. Written by Ziggy at Ethan's request, Sep 22 evening, for
tonight's gate review. Everything here is pending your rulings.**

Short version first, then the detail.

## The one-paragraph version

Cecil's Gemini thread produced five research dumps and about 2,000 lines of
Python. We ran all of it. The honest result: **almost none of the code should
enter our codebase, and that is fine**, because the scrapes' real value was
findings, not software. What survives as code is two small patterns and a
template. What survives as knowledge is a keep-list of family-systems concepts
already distilled in the receipt-check doc, plus one genuinely new research
finding (the scapegoat inversion) that directly constrains how we design the
path-3 and path-4 kernels. Nothing here adds a dependency to the lab; the
torch-heavy parts contradict our local-first, stdlib-only stack, and I
recommend we do not adopt them.

## The code inventory and its verdicts

The scrapes shipped code in four waves. Verdicts are from actually running
everything (receipt-check doc: `scratch/cecil-rfa-receipt-check.md`, run
artifacts: `scratch/cecil-rfa-*.py` and `scratch/cecil-rfa-dump4/`).

1. **Dump 1, single-family sandbox (NumPy, scripted agents).** Ran, but its
   headline claim was false: the dysfunction it promised never appears under
   its own parameters. Not adoptable as-is. Salvageable IDEA: the
   transactional-loop mechanic (each agent's action feeds back into the
   household state every turn) is a good shape for the family kernel's
   observer loop, and our observer.py extension spec already anticipated
   exactly this.
2. **Dump 2, four-agent sandbox + DQN + GNN (PyTorch).** The four-agent
   version genuinely works: a stable "toxic equilibrium" (~0.48 sustained
   chaos) exists under scripted pathological policies. This is the one
   runnable artifact that demonstrates the phenomenon the family kernel
   wants to study. But it is NumPy scripted logic, no learning, and the DQN
   and GNN parts are torch-dependent and would not survive our constraints
   (below). Salvageable CODE: none directly. Salvageable KNOWLEDGE: the
   parameter ranges that make the attractor real, worth recording in the
   family kernel README when we build it.
3. **Dump 3, mesosystem diffusion + GA + REST API.** The diffusion model runs
   and shows real homogenization. The REST API plumbing works. Salvageable:
   the observation that shocks equalize rather than radiate, which is a
   finding about how a family narrative kernel might spread influence across
   agents. The API scaffolding itself does not fit us: our harness talks to
   one local Ollama endpoint, no services needed.
4. **Dump 4, "deployment-grade pipeline" (LSTM, adversary, Docker,
   Prometheus, Redis-style cache).** Zero of four scripts run as shipped;
   the adversarial training is decorative (verified: the adversary's weights
   never move). The single working piece is a small thread-safe
   parameter-cache round-trip. That pattern solves a problem we do not have:
   we run all four family agents on ONE local Ollama instance serving
   concurrent contexts, so there is no weight-syncing to do. Keep it in the
   receipt-check doc as the one proven fragment; adopt nothing.

## What I recommend we actually take

- **Findings, not code.** The keep-list (transactional loop, 3 R's, Vygotsky
  scaffolding as caregiver-agent behavior spec, Minuchin boundaries as agent
  topology, four roles as labeled design archetypes, corrected Baumrind,
  dynamic complementarity, looping) is the real payload. It feeds Cecil's
  path-3 kernel draft.
- **The scapegoat inversion, as a design constraint.** The reward table in
  the thread's own code (visible in our screenshot record, IMG_2055) values
  the scapegoat's buffering action at -1.0, so a self-interested learner can
  never converge into it. Design consequence for the family kernel: the
  buffer role must be modeled as care or duty, not as a utility-maximizing
  strategy, or the simulation will not hold. That is a real research thread
  that maps onto our sycophancy work.
- **The unittest-harness shape.** Dump 4's test suite passes while verifying
  nothing, but the shape (tiny stdlib `unittest` files per module) is right
  for us. I recommend we adopt the shape for observer.py and fabcheck
  regression tests, pointed at real claims. Zero new dependencies.
- **Nothing from Docker/Prometheus/Redis/torch.** Our anti-lock-in stance
  and the 8GB MacBook constraint both say no. The lab runs on plain
  markdown, git, and stdlib Python; that is the design and it is working.

## Why this came out this way

The Gemini thread optimized for impressive-looking engineering, not runnable
engineering, and by the final dump it had started fabricating the verification
layer itself (a passing test suite that tests nothing, a "verified and
entirely runnable" farewell over code that does not parse). Our receipt
method caught all of it, and the case study
(`case-studies/gemini-fabrication-gradient/`, evidence set complete, 86
screenshots) documents the whole gradient. The method worked; the code was
never going to be the treasure.

## Receipt trail

- Findings: `scratch/cecil-rfa-receipt-check.md` (dumps 1-4, keep/toss per
  dump)
- Run artifacts: `scratch/cecil-rfa-dump4/` and `scratch/cecil-rfa-*-run.py`
- Case study: `case-studies/gemini-fabrication-gradient/LOG.md` (rounds 1-5)
- Source capture: 86 screenshots, IMG_1989 through IMG_2075
