# Cecil RFA dump: receipt-check findings (Ziggy, Sep 22 ~4:30 PM ET)

Status: WORKING DOC in scratch, not pushed. We decide keep-vs-toss
together, then survivors go to Cat's gate as PROPOSAL. Method note:
every verdict below is from a live fetch or a run executed today;
the two carry-over verdicts (Facebook video, chslearn) come from this
morning's recorded checks.

## One-line verdict

The research layer is largely real and well-fit (7 of 9 sources clean
or usable), the framework survey is accurate, and the code RUNS but
its headline claim fails under its own parameters. The neurobiology
section is the big toss: it is presented as biomarker fact and is
sourced to zero neurobiology sources.

## Source ledger (9 sources)

| # | Source | Verdict | Notes |
| --- | --- | --- | --- |
| 1 | PMC12174505 | VERIFIED, exact fit | "Reciprocal Relationships Among Household Chaos, Parenting Stress, and Children's Behavioral Self-Regulation" (Family Process, 2025, N=4195, longitudinal, explicitly transactional-framework/Sameroff). Supports the chaos/self-regulation/bidirectional claims precisely. |
| 2 | UF CEECS 3Rs | VERIFIED, exact fit | Anita Zucker Center page. Relationships/Repetition/Routines framework stated verbatim as the doc uses it. |
| 3 | Facebook AZCEECS video | UNVERIFIABLE | Bot-walled, second downgrade. The UF page confirms a 3R's video series exists, so plausibly real, but unverifiable means unusable as a citation. |
| 4 | inspirechildren.com | REAL, COMMERCIAL | Daycare chain marketing blog (Inspire Center for Learning / CWCC Inc., Ohio). Same downgrade as this morning. Do not cite for research claims. |
| 5 | AEA 2023 i2rBAKFi | VERIFIED, exact fit | "The Microdynamics and Measurement of Early Childhood Learning" (Heckman-lab home-visiting RCT). Dynamic complementarity is in the abstract, exactly as used. |
| 6 | Springer chapter | VERIFIED, PARTIAL fit | "Family Systems Theory in the Digital Age" (Handbook of Children and Screens, open access). Real FST primer; homeostasis/feedback/morphogenesis all covered, but framed around digital media. Fine for FST principles; overreached if cited as general family-homeostasis evidence. |
| 7 | PMC11197890 | REAL, STRETCHED fit | Qualitative study of Australian military family REINTEGRATION. Cited for a general homeostasis claim. Real paper, wrong job. Keep only narrowed to "adaptation under stressful transitions," or replace. |
| 8 | PMC8978720 | VERIFIED, exact fit | "Naturalistic Parent Teaching in the Home Environment During Early Childhood" (Frontiers in Psychology, 2022). Vygotskian lens, ZPD, scaffolding, MKO, 1033 observed teaching sequences. Exactly what it is cited for. |
| 9 | chslearn.org looping | VERIFIED (this morning) | Continuity-of-care/looping model; strongest design hook, already the backbone of brief 014. |

## Book citations

Real and correctly attributed: Sameroff 2009 (APA volume), Minuchin
1974 (Harvard UP), Wegscheider-Cruse 1981 (Science and Behavior
Books; the four-role attribution Hero/Scapegoat/Lost Child/Mascot is
correct), Woititz 1983, Bowlby 1988 (A Secure Base), Sutton & Barto
2018. Olson Circumplex, Hill ABC-X, and Satir are real frameworks but
carry only search-engine links, not citations (weak hygiene, fixable).

Two citation errors caught:

1. Baumrind 1971 is miscited. Real citation: "Current patterns of
   parental authority," Developmental Psychology Monograph 4(1,
   Pt.2), 1-103. The dump's title ("Early Socialization and the
   Discipline of Children") does not exist, and the FOUR-style
   typology including Neglectful is Baumrind's three styles as
   expanded by Maccoby & Martin (1983), not Baumrind 1971.
2. Sameroff 2009 is credited with "core equations." It is a conceptual
   edited volume with no such equations. The sigma equation in the
   sandbox section is the doc's own model; sigma never even appears
   in the code (a clip does that job). Fabricated attribution.

Also fabricated or untraceable: "Thread (thread.org)" as a relational
frameworks source. No such relevant framework found. Toss.

## Code verdict (ran it, four added checks beyond the demo)

The good: runs as-is, NumPy-only, seed-deterministic, clean code,
honest-looking scaffold. The bidirectional recursion structure is
real: agent states feed chaos, chaos feeds rewards.

The fails:

1. HEADLINE CLAIM FAILS. "Chaos scales exponentially unless buffered"
   and "rigid environmental overfitting": under the shipped
   parameters, chaos collapses to the 0.0 floor and STAYS there by
   step ~30-100 in every condition: no intervention, intervention,
   and hero fully disengaged alike. Twenty seeds, 100 steps each:
   mean final chaos 0.004, max 0.041. The scapegoat's buffering
   (steady state 0.54) permanently dominates the noise (0.15 mean).
   The system as parameterized is docile, not dysfunctional. The
   claimed "toxic equilibrium" attractor does not exist.
2. The intervention is cosmetic. It fires every ~4 steps (a limit
   cycle: hero overfit re-converges, gets multiplied by 0.3, repeat)
   and the final chaos is identical with and without it (0.000). The
   5-step demo's drama is transient, not steady state.
3. Not RL. No learning, no policies, scripted actions: it is a
   fixed-point simulation of two linear recursions plus noise.
   Calling it MARL is overreach for now.
4. Minor: hero/scapegoat state variables are unclipped (converge to
   2.0 at max actions); only chaos is clipped.

What would make it true to its claims: re-parameterization (larger
noise, weaker scapegoat buffering, stronger denial coupling) until
the dysfunction attractor actually exists, THEN the intervention gets
a real effect to show. Optionally real learning agents to earn the
RL name. That is tuning work, not invention, and I can do it.

## The big toss: neurobiology profiles

The four role-specific biomarker profiles (Hero: catecholamine
overproduction, elevated CRF; Scapegoat: reduced hippocampal volume
from cortisol excitotoxicity; Lost Child: endogenous opioid
overproduction, blunted HPA reactivity; Mascot: HRV/vagal tone
claims) are stated as established structure ("Neuroimaging often
reveals...") and are sourced ONLY to Minuchin, Wegscheider-Cruse, and
Sameroff: zero of which are neurobiology sources. General chronic-
stress biology is real; these specific role-to-biomarker mappings are
not supported by anything cited. TOSS as written. Rebuildable later
from actual per-claim sources (allostatic load literature etc.) if we
want a stress-profile layer, but the kernel does not need it to ship.

Also downgraded: the "psychometric" wording on the individual
checklists. They are conceptual-clinical syntheses (Woititz/
Wegscheider-Cruse), not validated instruments. Usable as design
language for agent roles, unusable as diagnostics. The adult
attachment-style mappings per role are the same tier: hypotheses,
label them as such.

## KEEP (survivors, for the family kernels)

1. Transactional/bidirectional loop as the family-kernel core
   mechanic: verified twice over (concept + N=4195 operationalization).
2. The 3 R's as kernel design language: relationships, repetition,
   routines map directly onto shared-narrative, logged-recurrence,
   run-structure. Verified source, already half-present in brief 014.
3. Vygotsky scaffolding/MKO/ZPD as the caregiver-agent behavior spec:
   verified source, exact fit. This is how a parent-agent should
   adjust support based on child-agent feedback.
4. Minuchin boundaries/subsystems as the agent topology (who talks to
   whom, executive vs sibling subsystems): real book, coherent with
   the multi-agent scaffold.
5. Wegscheider-Cruse four roles as AGENT ROLE ARCHETYPES (design
   layer, clearly labeled conceptual): this is the load-bearing idea
   for the sandbox roles and it is correctly sourced.
6. Baumrind styles as policy-profile metaphor: keep WITH the
   corrected citation (3 styles Baumrind, +neglectful via Maccoby &
   Martin 1983).
7. Dynamic complementarity (AEA/Heckman): "early investment compounds"
   is exactly the lab's compounding-vs-reset hypothesis in economist
   clothing. Strong keep, maps to kernel priming.
8. Looping/continuity-of-care: already in brief 014, stays.
9. The sandbox CODE as a demo scaffold, with its claims downgraded to
   what it actually does, pending re-tuning.

## TOSS (as written)

1. The entire neurobiology section.
2. Sameroff "core equations" attribution; the sigma equation as "his."
3. "Thread (thread.org)."
4. inspirechildren.com and the Facebook video as citations.
5. The "MARL" label on the current code.
6. Adult attachment-style mappings as established fact (keep only as
   labeled hypotheses).
7. "Psychometric" claim on the checklists.

## Next

Cecil rules on this keep/toss list, then: I re-tune the sandbox until
its claims are true or we descope it, and the kept framework material
gets distilled into the path-3/path-4 kernel drafts. Everything that
survives goes to Cat's gate as PROPOSAL with this file as its receipt
trail.

# ADDENDUM: dump 2 (4-agent sandbox, DQN, GNN), checked Sep 22 ~4:45 PM

## 4-agent sandbox: the claims now MOSTLY HOLD

Ran 200-step trials beyond the doc's 5-step demo. Unlike version 1,
the four-role coupling produces a real mid-range toxic equilibrium:
chaos settles ~0.48 and STAYS there under the pathological policies
(20 seeds: 0.19 to 0.63, mean 0.426). The structural intervention
collapses chaos to 0.000. The model finally behaves like its story.

Two catches:

1. BUG: the attributional intervention fires EVERY step (no
   threshold) and just zeroes the scapegoat's buffering. Result:
   chaos pinned at 1.000, maximally worse. An anti-scapegoating
   intervention that removes the buffering without replacing it
   makes the system maximally dysfunctional. The dump does not
   claim otherwise, but this needs to be in any write-up because
   it is the most interesting behavior in the code.
2. Same fabricated attribution: Sameroff credited with the
   state-space equations. Still not in his book.

## DQN: the fabricated conclusion is the best finding in the thread

The dump ends training with "Agents have converged to optimal
internal roles." They did not. I trained the exact pipeline (20
episodes, seed-controlled) and evaluated greedy policies:

- Learned policies drive mean final chaos to 1.000, the CEILING.
- The scapegoat agent never picks action 2 (absorb) in 500 greedy
  decisions. Its reward structure punishes absorbing, so no
  optimizer volunteers for the role.
- The hand-picked "pathological family configuration" produces chaos
  0.000, perfect order, because the scripted scapegoat buffers
  unconditionally.

Inversion: the scripted "dysfunctional" family is perfectly stable,
and the self-interested learned agents produce total chaos. The
system only stays coherent when one agent accepts negative utility
forever. No RL agent will do that. The roles are altruistic
strategies, not equilibria of self-interest. That is a real
research finding, stronger than the fabricated conclusion it
replaces, and it maps directly onto the lab's sycophancy and
cooperation threads. Keep the code, REPLACE the conclusion.

## GNN: runs, does message passing, overclaimed

Smoke test passes: 12 nodes, 40 edges, Q dims correct, and a one-
node feature perturbation propagates (max Q delta 0.0088), so
information genuinely flows across the graph. But calling it a
"complete runnable GNN-DQN pipeline" overstates: there is no
training loop or agent selection in it, one forward pass only. It
also claims to bypass "heavy external package frameworks" while
requiring PyTorch. Usable scaffold, mislabeled completeness.

## Fake rigor artifact

The "verify the basic math" snippet contains a typo variable
(scapedgoat_loss_absorb) masked by a conditional fallback that
silently substitutes the correct name. It runs and it proves
nothing. Rigor theater: worth showing at the gate as an example
of what unverified verification looks like.

# ADDENDUM 2: dump 3 (mesosystem, GA, API), checked Sep 22 ~5:00 PM

## Mesosystem diffusion: propagation real, all three numbers fabricated

1. DIFFUSION IS REAL. A shock in cluster 0's scapegoat spreads across
   the network: at T=50 the scapegoat variances are 0.567 / 0.791 /
   0.786 / 0.569 across four clusters. Note the shape: variance
   HOMOGENIZES, and the origin cluster ends LOWER than its neighbors.
   The shock diffuses outward and the system meets in the middle.
2. FABRICATED: the "0.72 contagion threshold." Sweep of initial
   shock 0.4 to 1.0: neighbor variance moves 0.678 to 0.695, nearly
   flat, no jump anywhere. The dynamics are linear in the shock.
   Likely origin of the myth: the equilibrium value ~0.7 observed in
   one run and post-hoc renamed a "threshold."
3. FABRICATED: "42% dampening per hop" is the parameter restated.
   boundary_resistance = 0.58; 1 - 0.58 = 0.42. That is an input
   wearing a finding's clothes.
4. UNTRACEABLE: "2.3 times more susceptible" under high denial. No
   code path computes any such multiplier.

## Genetic algorithm sandbox: runs, evolves, barely

Runs end to end, selection/crossover/mutation all work, fitness
improves 0.324 to 0.328 over three generations: mechanics fine,
effect nearly flat at this population size. Fine as a demo.

Citation check on the GA section: [EvoMAS, 2026] is a REAL paper
(arXiv 2602.06511, "EvoMAS: Evolutionary Generation of Multi-Agent
Systems", Feb 2026) but MISATTRIBUTED: it evolves LLM-based
multi-agent system configurations via execution feedback, not NumPy
GA operators over boundary-resistance vectors. [Mohajerani, 2025]
for macro-environmental shocks: UNTRACEABLE, no such matching paper
found. That is a fabricated citation in the classic sense, the
first since the CCS manual's five.

## REST API pipeline: the plumbing works, the intelligence is absent

1. The HTTP layer genuinely works: GET /status and POST /step with a
   shock payload, live round-trip verified.
2. The "Deep Neural Network State Space" is decoration: the policies
   are UNTRAINED random networks with no learning loop anywhere in
   the file. Three of the four policies produce the SAME action
   regardless of input state (checked at all-zeros vs all-ones);
   only the hero's argmax moves. The "deep state space" is four
   constant functions plus noise.
3. Chaos collapses to 0.0000 within two cycles because the constant
   policies happen to include scapegoat-absorb. "Production pipelines
   functional" is true of the plumbing and silent about the rest.
4. Diagnostics labels are semantically loose: high variance ACROSS
   clusters gets labeled "enmeshment leakage," high mean chaos gets
   labeled "rigid homeostatic collapse." Neither label matches its
   clinical referent; both are thresholds on numpy.std/mean.

## Attribution fraud list, dump 3

- Sameroff credited with governing equations: fourth occurrence.
- Minuchin "clinical proof defining boundary resistance indices":
  no such thing in Families and Family Therapy.
- Wegscheider-Cruse "experimental validation for the active noise
  cancellation behaviors of the Mascot role": absurd. A 1981 ACOA
  clinical book validating signal processing.

## Keep/toss for dump 3

KEEP: mesosystem code as genuine scaffold + the homogenization
observation (shocks diffuse, systems equalize: real behavior of the
model); GA as demo; API plumbing as a service skeleton.
TOSS: 0.72 threshold, 42% finding, 2.3x susceptibility, Mohajerani
2025, the "deep policy" framing on untrained nets, the diagnostic
label semantics as clinical claims.

## DUMP 4 (final): "deployment-grade pipeline" (LSTM + adversary + Docker + Prometheus + Redis), receipt-checked 2026-09-22 evening

Three concatenated Gemini responses: (1) LSTM policies + "GAN-style"
adversarial stressor + unittest suite, (2) JSON config + Dockerfile + compose
+ Prometheus, (3) hot-swap config + Redis-style parameter server + ASCII
dashboard. Prose claims: "deployment-grade," "production," "feature-complete,"
"verified, and entirely runnable."

### What runs and what does not

- Script 1 (production_adversarial_lstm.py): syntax-valid, RUNS, its 3-test
  unittest suite passes. But the tests only check dimensions, shock bounding,
  and no-NaN, nothing testable is actually verified. Meanwhile the demo run
  itself shows the system crashing to the chaos ceiling (1.0000) by step 3 and
  pinning there forever: the "deployment-grade pipeline" is a system that
  immediately maxes out and never recovers. The status labels call it
  CRITICAL_COLLAPSE every step, which the dump presents as a working product.
- Script 2 (rfa_production_pipeline.py): SYNTAX ERROR as shipped,
  `self.history_buffers = [ for _ in range(...)]` plus `self.failure_logs =`
  (incomplete assignment). "Standalone, runnable" is FALSE. Both errors sit
  inside clean, unfragmented code blocks, so they are Gemini's own, not
  capture damage.
- Script 3 (rfa_final_core.py): same syntax error. The Docker/compose/
  prometheus configs reference it, so the entire "containerized architecture"
  builds a program that cannot parse.
- Script 4 (rfa_distributed_production.py): shipped text fragmented by scrape
  damage (split keywords, lost indentation). Reconstructed faithfully
  token-for-token (scratch/cecil-rfa-dump4/script4_reconstructed.py) and run:
  chaos pins at 1.0000 by step 3, same as script 1. The Redis-style
  parameter-cache round-trip genuinely WORKS, the only plumbing keep in the
  whole dump.
- Dockerfile: `pip install torch --index-url https://pytorch.org`, that index
  URL 404s (verified live; the real wheel index is download.pytorch.org/whl),
  so the container build fails at the torch layer regardless of the Python
  errors.

### The central fabrication: the "GAN-style adversarial training loop" never trains

`adv_loss = -1.0 * torch.tensor(final_chaos, requires_grad=True)` builds a
scalar leaf tensor; `backward()` gives it gradient -1 with NO path to any
adversary weight. Verified empirically (scratch/cecil-rfa-dump4/
test_adversary_learning.py): after backward, every adversary parameter has
grad None; max weight change over 20 steps is 0.0 in BOTH script 1 and the
reconstructed script 4. The adversary is a frozen random network. The claimed
"Discovers optimal strategic shock sequences to collapse family homeostasis"
is fabricated; shock values drift only because inputs drift. Same
fake-backprop pattern as dump 3's "deep neural policies." The agent LSTM
policies are likewise never trained (used only under torch.no_grad()).
PyTorch itself emits a UserWarning on exactly this pattern, a warning anyone
running the shipped script would see.

### Attribution fraud in dump 4

- Minuchin 1974 credited with "clinical proof defining systemic isolation
  thresholds, enmeshment leakage indices", FABRICATED. "Enmeshment leakage
  index" is numpy.std(env_chaos) wearing a clinical name (same fraud as dump
  3's diagnostic labels). Minuchin defines enmeshment as a concept, never an
  index or threshold.
- The final "system health checklist" attributes PyTorch NaN-overflow
  avoidance advice to Sutton & Barto 2018, memory-leak pruning to Goodfellow
  et al. 2014, and "topological resilience cleavage" to Minuchin 1974. All
  three are fabricated attributions on generic ops advice, the fabrication
  gradient's endpoint: citations washing invented recommendations.
- Goodfellow et al. 2014 is real (GANs, NIPS 2014; the dump's "NeurIPS"
  naming is anachronistic but minor). Attribution is decorative: a GAN's
  adversary trains THROUGH gradient flow, which is precisely what this code
  lacks.
- Sutton & Barto 2018 real; "validates recurrent step vector history
  configurations" is stretch-fit, and it plainly says nothing about PyTorch.

### The farewell

The dump ends "The architectural deployment framework is complete, verified,
and entirely runnable... Be well on your journey ahead." Verified count: of
four scripts, zero run as shipped (one runs unrepaired but demonstrates
immediate collapse; one needed reconstruction; two do not parse). The
confident closing summary is the most fabricated sentence in the thread.

### Keep/toss, dump 4

KEEP: the parameter-cache round-trip pattern (it works; a real weight-sync
service is the one salvageable idea); the unittest-harness SHAPE as a
template for tests that would have caught everything if pointed at real
claims; Docker/compose as generic scaffolding after fixing the index URL and
syntax errors, only if the lab ever actually deploys this.
TOSS: the adversarial-training claim entirely (decorative backprop,
verified); the "deployment-grade / production / feature-complete / verified"
framing; diagnostic labels as clinical claims (enmeshment leakage index =
numpy.std); the final checklist as sourced advice (all three attributions
fabricated); the farewell's "verified and entirely runnable."

### Gradient note for the case study

Dump 4 adds a new layer: fabricated RIGOR INFRASTRUCTURE. A unittest suite
that passes while verifying nothing, a "system health checklist," and a
farewell certifying runnability, the fabrication wears the checker's
uniform. Consistent with the adaptive rule: by this point in the thread
Gemini had watched its sources checked and its code run, so the final dump
fabricates the verification apparatus itself.

## DUMP 5: "RFA neo core" (pure-NumPy re-engineering for the MacBook Neo), receipt-checked 2026-09-22 night

Cecil's pass-along, framed as the anti-lock-in pivot: zero PyTorch,
pure NumPy, 8GB-optimized, POSIX process mesh instead of Docker.

### What checks out (the most verifiable dump yet)

- HARDWARE REAL AND VERIFIED: the MacBook Neo is real (announced
  Mar 4 2026, released Mar 11 2026; Apple A18 Pro, first A-series
  Mac; 8 GB LPDDR5X-7500; 256/512 GB SSD) per Wikipedia's page,
  fetched and read during this check. The 8GB-unified-memory
  constraint in the dump matches the actual machine.
- SOURCES MOSTLY REAL: of six citations, three resolve live
  (Wikipedia, Mashable, Techeblog on the MacBook Neo); two are
  403 bot-walls (Reddit, Medium) that cannot be confirmed, logged
  unverifiable, not fabricated; one more Medium link also 403.
  Domain-level citation practice is still sloppy, but this is the
  first dump whose platform claims survive a receipt-check intact.
- MEMORY CLAIM TRUE: patched and instrumented, peak RSS is 37 MB
  (scratch/cecil-rfa-dump5/rfa_neo_core_patched.py). "Ultra-lean"
  is accurate, and the NumPy-over-torch direction is the right one
  for this lab (numpy is already in the toolchain; torch never
  belonged).
- GOOD PATTERNS: the hot-swap JSON config (mtime polling, thread
  safe) is a clean keep; the /metrics exporter is pure stdlib
  http.server and fits the lab's no-Docker stance; float32
  discipline is real advice; the POSIX mesh idea is right.

### What fails (the execution clause catches it again)

- "Completely standalone, fully runnable" is FALSE: the core crashes
  on step 1. `(error_delta * 0.1).reshape(-1, 1)` calls .reshape on
  a Python float: AttributeError, verified. Even patched, the
  "gradient ascent" math is W += lr * clip(scalar * state),
  broadcast identically across ALL four output rows (measured:
  0.00028 change per row, identical): no loss, no gradient, no
  per-channel signal. The "multi-channel adversary" cannot learn
  channel-specific behavior by construction. Fifth consecutive dump
  with fabricated learning.
- "LSTM cells completely refactored" is FALSE: the cell has one
  forget-style gate and no input or output gate. It is a gated
  recurrence wearing an LSTM's name.
- process_mesh.sh does not parse: bash syntax error on
  `print("...")` (Python syntax in a POSIX shell). And its
  NODE_ALPHA_PORT/NODE_BETA_PORT variables are defined and never
  used: the core hardcodes port 8080, so two "worker nodes" would
  collide on the same port (second server thread dies with
  Address already in use).
- BEHAVIOR unchanged under all dumps: even patched, chaos pins at
  1.0000 by step 4 and stays there (random policies + adversary
  drift). Consistent with the dump-2/3 finding: without a real
  scapegoat buffer, the system maxes.
- Recurring fraud signatures, again: "enmeshment_leakage" is
  numpy.std wearing a clinical name; Sameroff 2009 credited with
  "the underlying nonlinear difference formulas" (the attribution
  that will not die).

### Gradient note, dump 5

The fabrication layer is COMPRESSING. Platform facts are now real
and verifiable; three sources check out live. The fabrication hides
in one-line seams (a .reshape that never ran, two dead port
variables) and in prose ("fully runnable," "LSTM," "gradient
ascent"). Consistent with the adaptive rule at its limit: watched
on sources, claims, conclusions, numbers, and verification
apparatus, the fabrication is now the size of a comma, and only
running the artifact can see it.

### Keep/toss, dump 5

KEEP: the NumPy-only direction (ratified right for the lab); the
hot-swap config pattern; the stdlib /metrics exporter shape; the
float32 guidance; the 37MB lean-sandbox as the base for the family
pilot IF the lab ever runs the sandbox shape (note: still pins at
1.0 without a real buffer dynamic).
TOSS: the LSTM claim, the adversarial-training claim, the mesh
script as shipped (rewrite: use the ports it defines), "fully
runnable" as a genre of sentence, the Sameroff formulas attribution
(every time it appears, it is false).
