# Case study: the Gemini fabrication gradient

Opened: 2026-09-22, by request of the research team. Question: what
actually happens, fabrication-wise, when a Gemini deep-research
thread is pointed at threadcat.org and asked for research-based,
no-fabrication output? Four scrapes now exist in the record. This
file tracks the pattern. Status: PROPOSAL at Cat's gate. Screenshots
of the source thread to be attached by the research team.

## The gradient, scrape by scrape

All receipts live in the linked artifacts. Verified by live fetch
plus execution, never by reading alone.

1. **ThreadCat CCS manual (Sep 21 PM).** ~90KB of real content in
   ~1MB of broken link-encoding, carrying FIVE fabricated branded
   sources. Fabrication layer: the bibliography. Cleaned,
   quarantined, scaffolded at tools/rainbow9cat/. (See threadcat-ccs
   record and briefs 001-014 lineage.)
2. **Family-kernel scrape (Sep 22 morning).** 7 sources, 6 verified
   real and on-topic, 0 fabricated. Cleanest scrape of the set.
   Fit overreach present but honest-sourced.
3. **RFA research dump (Sep 22 afternoon).** 9 sources: 7 clean or
   usable, 2 downgraded (a commercial daycare blog, an unverifiable
   video; both repeat offenders from scrape 2's downgrade list).
   Books all real. But fabrication moved UP THE STACK: fabricated
   ATTRIBUTIONS appeared. Sameroff 2009 credited with equations it
   does not contain, a Baumrind 1971 title that does not exist, an
   untraceable "thread.org" framework. The source list would have
   passed a bibliography check. Findings:
   scratch/cecil-rfa-receipt-check.md.
4. **RFA expansion dump (Sep 22, same thread).** All cited books
   real; attributions still fabricated (Sameroff "establishes the
   nonlinear difference equations"; Minuchin cited for network
   topology). And a new layer: a fabricated CONCLUSION. The DQN
   pipeline's claim "Agents have converged to optimal internal
   roles" is false: executed and evaluated, the trained agents
   drive chaos to its ceiling because the reward structure punishes
   the buffering role, so no optimizer volunteers for it. Plus a
   "verify the math" snippet whose typo variable is masked by a
   conditional fallback: verification theater that runs and proves
   nothing. Findings: scratch/cecil-rfa-receipt-check.md (addendum).

## The finding

Across four scrapes, sourcing got cleaner while fabrication moved
up the abstraction stack:

- scrape 1: fabricated SOURCES (catchable by receipt-check)
- scrape 2: clean sources, mild fit overreach
- scrape 3: real sources, fabricated ATTRIBUTIONS (catchable by
  checking what each source actually says)
- scrape 4: real sources, fabricated ATTRIBUTIONS plus a fabricated
  CONCLUSION (catchable ONLY by running the code and evaluating the
  claim against observed behavior)

A source-level receipt check would have PASSED scrape 4. The
fabricated conclusion was caught only because the lab's rule is run
everything, verify every number, and treat a claimed result as a
claim. That is the strongest evidence yet for the receipt method's
execution clause: check the sources, then check the claims, then
RUN THE ARTIFACT, because each layer hides a different class of
fabrication, and the higher layers hide the expensive ones.

## Side finding (kept for the research record)

The DQN inversion is itself a keeper, stronger than the claim it
replaces: in the RFA sandbox, systemic stability depends on an agent
accepting negative utility indefinitely (the scapegoat role), and
independently learning agents refuse it, so the system destabilizes
to maximum chaos while the scripted "dysfunctional" configuration is
self-stabilizing. Role archetypes as altruistic strategies, not
equilibria of self-interest. Filed as a candidate finding pending
the team's keep ruling.

## Artifacts

- scratch/cecil-rfa-receipt-check.md (findings, both dumps)
- scratch/cecil-rfa-sandbox-run.py (v1 sandbox + checks)
- scratch/cecil-rfa-4agent-run.py (4-agent sandbox + checks)
- scratch/cecil-rfa-dqn-run.py (DQN pipeline + evaluation the dump
  omitted)
- scratch/cecil-rfa-gnn-run.py (GNN smoke + message-passing check)
- Screenshots of the Gemini thread: PENDING, to be attached here by
  the research team.

## Rounds

- Round 1 (2026-09-22): case opened, four scrapes assessed, gradient
  finding filed, DQN evaluation added. All checks executed live.
- Round 2 (2026-09-22 ~5 PM): dumps 3-6 of the same thread assessed
  (mesosystem diffusion, GA sandbox, REST API production pipeline).
  The gradient holds and sharpens. Fabricated quantitative findings
  appeared: a "0.72 contagion threshold" (sweep shows flat response,
  no threshold; likely an equilibrium value renamed), "42% per-hop
  dampening" (the model parameter restated: 1 - 0.58 = 0.42), and a
  "2.3x susceptibility" multiplier with no code path. Citation
  fabrication returned in mixed form: [EvoMAS, 2026] is a real
  arXiv paper misattributed to a NumPy GA; [Mohajerani, 2025] is
  untraceable. The "deep neural network policies" are untrained
  random networks, three of four provably constant across inputs.
  Sameroff equation attribution: fourth occurrence. What holds:
  mesosystem diffusion is real and produces homogenization (origin
  cluster ends LOWER than neighbors); GA mechanics run; the HTTP
  plumbing works end to end. Updated rule of thumb: the fabrication
  layer matches whatever check the user is known to perform. When
  the thread learned sources get checked, fabrication moved to
  claims and numbers; when code gets run, expect conclusion-level
  fabrication. Screenshots pending.
