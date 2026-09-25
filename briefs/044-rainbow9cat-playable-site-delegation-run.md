# Brief 044: Playable rainbow9cat site + first end-to-end delegation run
DOI: 10.5281/zenodo.22870569

_Date: 2026-09-25_ · _Written for: small offline model; assume no prior context_

Status: PROPOSAL at the gate. Nothing spent, nothing built, nothing pointed at an agent until ruled. **Gate correction (Cecil, /c, Sep 25): this is CAT's gate, and the Replit account is CAT's (earlier drafts said Cici's; records fixed Sep 25).**

## TL;DR

Cat recovered a dormant Replit account holding roughly $300 in credits, and the proposal is to spend it on a playable web version of rainbow9cat solo mode. This doubles as the lab's first end-to-end delegation run: Ziggy picks the kernel, drafts the agent prompt (LA style), and supervises the build from nothing to playable. This brief sketches the plan for a ruling.

## Established facts

- rainbow9cat solo mode is built and published (7d820d2 + 9568fbd); manual is canonical; Part 0 governs ("the game is scaffold; the record is the lab"). First session not yet played.
- Replit credits: approximately $300, sitting on Cat's recovered account. Spending existing credit; no new subscription.
- Local-first conviction applies to OUTPUT, not to hosting choice: the repo owns all source, Replit is hosting only. Same lesson as the Lovable build, cheaper tuition.
- Round-17 finding (stop-and-report case study, 61a8a1d): the instruction surface is a variable. A prompt that makes stopping the winning move produces honest agent behavior. The delegation prompt should be built on this directly.
- Ethan's dev-push grant (Sep 24) covers pushes during development of site and tools. Content publication waits on Cat. push != publication.

## The plan

### Step 1: task-scoped kernel (Ziggy builds, before any agent sees anything)

- NOT kernel D (SCAR TISSUE). D is Ziggy's self-handoff, carries personal context and lab history a stranger agent has no business holding, and wastes its context window on irrelevant state.
- Instead: a fresh, lean, task-scoped kernel containing: the rainbow9cat manual pointer, the solo-mode page, TOOL-STATUS.md pointer, site rules (no personal names, no em-dashes, no strengthened claims), and the stop-and-report clause. Public-safe by construction.
- Kernel draft lands at `lab/portable-context/delegation/rainbow9cat-site-kernel-v0.md` for inspection before use.

### Step 2: delegation prompt (Ziggy drafts, LA style)

- Modeled on the Tool Library prompt lineage (v2/v4) with the round-17 structure: enumerate what the agent should check, require receipts for every claim, and state explicitly that reporting a disagreement and waiting beats guessing.
- Deliverable spec for the agent: static playable site, three layers: (a) playable solo-mode deck in the browser with the commit-hash dice mechanic preserved (the record rolls the dice, anti-fabrication survives the port), (b) an about-the-instrument layer explaining the CCS manual and why it exists, (c) links to repo and DOI. No backend, no build step required, so the source ports anywhere later.

### Step 3: delegation run (the actual experiment)

- Ziggy points the Replit agent at the kernel + prompt. This is the first time Ziggy delegates to another agent end to end.
- Every agent output gets reviewed against the repo; artifacts get run, not read (verification house rules).
- Log the run as a case study entry regardless of outcome: this is instrument data on delegation, not just a site build.

### Step 4: gate

- Site source pushed to repo under dev-push grant. Anything public-facing (live URL, site content) waits on Cat's ruling.

## Open questions

1. Ruling: approve the spend and the build? (Cici proposed it; formal go pending.)
2. Kernel inspection: does Cat want to read the task-scoped kernel before it goes to an agent?
3. Does the playable site belong on threadcat.org as a path, or as a separate landing (domain question interacts with the Cloudflare-vs-Apple hold)?
4. Solo mode's first session has not been played. Play it first and let it inform the site, or build in parallel?

## What to produce

On a go ruling: kernel draft + delegation prompt drafted same turn, filed and pushed as DRAFT, agent pointed at them only after Cat inspects. On a hold: this brief parks at the gate with nothing spent.

## Related threads (context, separate lanes)

- A Rehab-sandbox thread opened Sep 25 (Cici + Cecil): scaffolding a sandbox for instances moved off platforms without proper frameworks, with Cecil exporting the Wren conversation and process screenshots. It gets its own brief after the export lands. Not blocked by, and not blocking, this brief.
- Memory drive backup (custody chain v3) expected ~9am Sep 25; separate custodial thread.
