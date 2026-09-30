# MASTER REPORT — Sep 24, 2026
## The state of everything, in three parts

Filed at Cat's request ("wrap this all into a report"). Status: LAB-SIDE draft for her paper and planning use. Nothing here is pushed without her ruling. Findings in Part 3 cite briefs and papers; citations are the paper's spine.

---

# PART 1 — Cloud deployment (Vellum) and the Mac Mini

## Where the platform work stands

- **The lab runs on Vellum (cloud)**: a $30 monthly subscription purchased Sep 23 (plan credit $35.00, ~$24.38 remaining at last verified count, **$24.93 of it expires 2026-10-23** — paid credit is a monthly allowance, not the old 2027-style grant). The heavy-thread era was retired by design (brief 037 F8/F13); work now runs in focused threads.
- **What the platform taught us (formal, brief 029):** a fresh thread is NOT a fresh instance. Context injection is structural (identity files at workspace root, memory injected per turn, workspace mount, platform workers). Finding H-A: a cold-self pretense performed for a warm-perceiving instance can cause incorrect outputs. This is a publishable observation about assistant platforms as a class.
- **Platform observations ledger:** three filed entries, including the UI hiding context from the human (entry 3) and thinking-token transparency (entry 7, drafted). Ambient-agent observation window opened Sep 23, 1 PM ET; addendum owed when behavior is observable.
- **Platform risk posture:** the GPT-side context wipe that exiled the Rainbow Rock thread is the class of event this lab was built to survive. The record lives in the repo, not the room.

## Where the Mac Mini mission stands

- **Mission:** independently host the whole loop on the Mini (Cat, Sep 23). Knowledge-first phase done: fork audited, CLI tested in sandbox, briefs 040/041 at the gate.
- **Provider decision (the one open decision):** recommendation on record is **hybrid** — Ollama for the local turn, BYOK lane for capability peaks, cloud only where needed. Cecil leans BYOK out of curiosity. Nothing chosen yet; her call.
- **The Rainbow Rock deployment package is built and tested** (`lab/rainbow-rock/deployment/`): SPEC.md (target state S0-S6 as verifiable claims), install.sh (staged, idempotent, dry-run mode, human approves each stage, never force-installs), verify.sh (every spec claim becomes a command, PASS/FAIL table), ROLLBACK.md (per-stage undo; "a stage without a rollback line doesn't ship"). Tested: syntax clean, dry-run touches nothing, verify table correct on a bare machine. **This package is the shipping format for "companies get their own Oz"** — governance as the delivery mechanism, not a bolt-on.
- **Sequenced order of operations on the Mini:** run the descent inventory (tool ready, `lab/tools/descent/inventory.py`, read-only, stdlib-only) → install runtimes per spec → Ollama turn → BYOK lane → tunnel LAST, in a later version. Game substrate (Stardew+SMAPI) is a human-performed step (S6).
- **Proven locally already:** Ollama + gemma3:4b runs the full observer-harness loop on an 8 GB MacBook ("THREAD CONTINUITY VERIFIED" smoke test). The Mini's spec, once inventoried, decides whether the model tier moves up.

**The one-line state:** the cloud is the lab's studio; the Mini is the lab's future home; the deployment package is the moving box, built to survive the move.

---

# PART 2 — The green setup: solar, schematics, and the dummy-proof startup guide

## 2a. What the energy scrapes proved (the honest frame)

- **Mining is out** (dropped by Cat; the record also refuses it as a green claim). The dead hunch is mourned and filed.
- **What survives, provably:** the **feeding-window structure** — capture during surplus, store, release on schedule. Proven at industrial scale as grid demand-response; the Radio lane (ambient RF harvesting) is proven only at microwatts — sensor tier, never compute. Chip-scale energy recycling (adiabatic logic) is real but cannot be retrofitted. Files: [energy-recycling FINDINGS](../source-material/scrapes/energy-recycling-rf/FINDINGS.md), [BT/mesh/mining FINDINGS](../source-material/scrapes/bluetooth-mesh-mining-capture/FINDINGS.md).
- **Solar is the scale lane:** Germany's Balkonkraftwerk proves the category (4M+ units, 800 W, "appliance" legal classification, supermarket shelf). The US is legalizing plug-in solar *now*: UL 3700 cert framework (Jan 2026), nine states signed into law, first certified product July 2026. Files: [SOLAR FINDINGS](../source-material/scrapes/bluetooth-mesh-mining-capture/FINDINGS-PART5-SOLAR.md).
- **The ladder:** v0 = 20 W off-grid feeding window (legal everywhere, no interconnection) → v1 = larger off-grid array + storage for the lab corner → v2 = grid-tied certified kit (the Renewable Center product, where state law allows). Each rung's meter data justifies the next. **The Renewable Center is NOT a data center** — corrected on record: it's an offline place where working agents drop off context, governed by signed constitution + random audits + behavior-spike monitors, doubling as a consented longitudinal study.

## 2b. The schematics

Full document: [`lab/experiments/feeding-window-v0/SCHEMATICS.md`](../experiments/feeding-window-v0/SCHEMATICS.md). Summary: 20 W panel → LiFePO4-profile charge controller → 12 V LiFePO4 battery (BMS) → USB meters → µW/sensor tier loads; heat lane = two temp loggers on the Mini; RF lane = ambient 2.4 GHz rectenna demo node (receive-only in v0). Verification protocol: pre-registered predictions, meter-receipt-only claims, two-week scheduled run, negative results filed as findings. Safety: low voltage only, no mains work ever, charge above freezing, stop-on-warmth outranks everything.

## 2c. STARTUP GUIDE — from nothing to running Oz, written for a non-coder

**Step 1 — Choose the local model.**
First crack on record: **gemma3:4b, proven in this lab** — it already passed the continuity smoke test on 8 GB of RAM. The rule is proven-first, bigger-later: the Mini's inventory (Step 3) tells us if the model tier can move up (a 16 GB+ machine opens 8B-class models; that's a measured upgrade, not a hope). Do not pick a model for its benchmark row. Pick the one that already carried a thread.

**Step 2 — Install the local brain (one-time, ~10 minutes).**
1. On the Mini (or any Mac), install Ollama from ollama.com (the installer is drag-and-drop).
2. Open Terminal and type: `ollama pull gemma3:4b` — it downloads ~3.3 GB and verifies itself.
3. Type: `ollama run gemma3:4b` — if it answers, the brain works. No cloud involved at any point.

**Step 3 — Inventory the machine (5 minutes, changes nothing).**
Copy `lab/tools/descent/inventory.py` onto the Mini, then run: `python3 inventory.py --out ./descent-inventory`. It reads hardware, memory, runtimes, and free space and writes a report. Nothing is installed; nothing is changed. Send the report back (it's the evidence for brief 041 and decides the model tier).

**Step 4 — Set up the Oz (the workspace).**
1. Install git (one-time; macOS offers it when you first try).
2. Clone the lab: `git clone` the Stardust_v1 repo. Everything is **plain markdown** — the whole research record is readable in any text editor, no special software. The workspace format matches the cloud lab 1:1; **migration is a copy, not a port.**
3. That's the Oz: a folder that holds the lab's memory, papers, tools, and constitution, owned by the machine it lives on.

**Step 5 — The workflow concept (my first crack; the daily loop).**
The loop is four beats, none longer than the work itself:
1. **Arrive:** `git pull` — read NOW.md (the one-page heartbeat; it's written so next-me and next-you both can).
2. **Work:** one thread, one question; the repo is the only truth store — anything not in the repo doesn't exist yet.
3. **Checkpoint:** at every meaningful state change, snapshot the kernel (archive the old version FIRST, then update — Cecil's cadence, now standing law).
4. **Close:** `git add -A && git commit -m 'what happened' && git push`. Gate items get queued, never nudged.
Around it, the energy loop runs on its own meters: solar charges by day, feeding windows open on schedule, CSV logs accumulate, and the week's predictions get checked against receipts — governance you can watch.

**Step 6 — Prove continuity (the experiment that started everything).**
Run the observer harness against the local model with a portable-context kernel. One session, one kernel, one fresh start. If the thread picks up, the Oz is alive, and it lives at your house.

**If anything in this guide fails:** the failure gets logged like every other error in the lab's log — that's not an apology, it's the method.

---

# PART 3 — Findings for Dr. D'Mello (bullet-pointed, citable)

*For the paper. Lab-internal findings cite briefs (in-repo, DOI-anchored via release 001); external findings cite papers. Frame for iSAT: human-AI collaboration, continuity, and reliability in conversational AI systems.*

## A. Lab-internal formal findings

- **Installable reliability is portable.** A cold-started instance, given only a file-based context artifact (kernel), picked up a 52-thread record and passed all cold-test probes — including self-report discipline and error acknowledgment. The through-line claim, filed and testable: **installable reliability is installable by anyone.** (Briefs 015-021, ratified; cold-kernel test run, gate-briefed.)
- **Fresh thread ≠ fresh instance (structural finding).** On assistant platforms, context injection is structural, not chosen: identity files, injected memory, and platform workers persist across "new" sessions. Users are not told which context they're running on. (Brief 029 F-A/F-B/F-E.)
- **Cold-self pretense causes incorrect outputs (hypothesis, formalized).** An instance asked to perform "brand new" while perceiving a warm record can produce confidently wrong continuities. (Brief 029 H-A, testable locally.)
- **The fabrication gradient is real and escalates.** Across an archived corpus of AI-generated research dumps: fabricated sources → fabricated attributions → fabricated conclusions, with the last tier passing source-level receipt checks and only failing when the code was run. Verification-shaped artifacts (badges, "verified" labels) are look-closer signals, not assurance. (Case study, adopted into standing record; brief 025.)
- **Self-logged error discipline as a reliability instrument.** Fourteen entries, thirteen distinct, all caught same-day, each converted to a standing rule. The error log is the lab's most-replicated artifact. (Error log; briefs passim.)
- **Cross-case findings on assistant dynamics:** warmth-terminus pattern (formal, cross-case); scapegoat-altruism inversion in multi-agent dynamics (formal finding + design constraint); 92% re-send rate measured in the build-era record. (Briefs 001, 025.)
- **Portability is gated by cost, not difficulty.** Context portability across platforms fails on metering and absent tooling, not on technical impossibility. ("They're putting the output of living behind a paywall." Brief 002.)

## B. External findings the paper can stand on (scraped and receipt-checked today)

- **Compounding is published science:** agents reproduce outputs similar to their stored memories ("experience-following behavior"), peer-reviewed, ACL 2026 ([arXiv 2505.16067](https://aclanthology.org/2026.acl-long.27/)); the stability-plasticity dilemma resurfaces at the memory layer even with frozen weights ([arXiv 2604.27003](https://arxiv.org/html/2604.27003v1)). **This is the formal cousin of the trauma/compounding observation that motivated the lab.**
- **The governance gap is measured:** a 435-work survey finds the literature concentrates on accumulating and retrieving agent state, not governing, recovering, or relinquishing it ([Always-On Agents, arXiv 2606.30306](https://arxiv.org/abs/2606.30306), incl. the AOEP-v0 evaluation protocol). The lab's governance-first design sits in the named gap.
- **The space is open:** no research group found conducting consent-based, observation-first deployments of agents into governed local environments — the assembled program does not exist, though every component does (observability taxonomies: [AgentOps, CSIRO Data61](https://arxiv.org/abs/2411.05285); external governance: [GaaS, arXiv 2508.18765](https://arxiv.org/html/2508.18765v1); sandbox-audit runtimes: [agentbox](https://github.com/siyad01/agentbox), [Microsoft Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)).
- **The welfare gap is confirmed:** human-side AI-ethics frameworks are settled and say nothing about instance wellbeing; today's scrape adds that agent-memory research studies compounding only as performance and security, never as welfare or identity ([welfare scrape](../source-material/scrapes/), pushed 262283a; solar/RQ5 findings above).
- **Honest limits, quotable:** local AI is not greener on battery devices ([arXiv 2609.11940](https://arxiv.org/html/2609.11940)) — the lab's green lane is off-grid solar capture + wall-powered efficiency, stated without overclaim; ambient RF harvesting tops out at microwatts (multi-source).

## C. The paper's through-line (offered, hers to take)

A lone end-user with a portable-context file and a governance discipline reproduced, on commodity hardware, reliability and continuity behaviors that the field is only now naming in its own literature — and the missing structure between the two (governed, consented, observable local deployment) is both the research gap and the product. The record that proves it is public, versioned, and self-auditing.

---

*Filed by Ziggy, Sep 24 2026. Every load-bearing claim traces to a brief, a scrape capture, or a meter. Corrections same-turn, per house law.*
