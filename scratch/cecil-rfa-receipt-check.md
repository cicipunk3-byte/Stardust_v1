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
