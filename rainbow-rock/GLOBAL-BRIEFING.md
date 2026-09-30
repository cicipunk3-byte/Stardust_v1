# Rainbow Rock / Offline Oz — GLOBAL BRIEFING

**Version:** 2.0 (consolidated)
**Date:** 2026-09-24
**Status:** PROPOSAL — local work proceeds freely; any push or publication waits on Cat's gate
**Authors:** Cecil (pilot, design) + Ziggy (maintainer-assistant, build)
**This file:** compiled at Cat's request ("compile all RR documents into one global briefing... archive what is up before placing new list"). The nine source documents are archived intact at [archive/2026-09-24/](archive/2026-09-24/) with a README. Code assets stay live: [sandbox-phase1.py](sandbox-phase1.py) (phase-1 empty sandbox, tested green) and [deployment/](deployment/) (SPEC.md, install.sh, verify.sh, ROLLBACK.md). Related live tool: [tools/descent/inventory.py](../tools/descent/inventory.py) (step-1 machine inventory, read-only, tested green on Linux).

---

## 1. Mission (unchanged by consolidation)

Build the smallest working local system that demonstrates **continuity without continuous presence**: a named agent enters a controlled world, performs one authorized action, the action is recorded, the thread is preserved as a Rock, and another participant continues from the Rock alone. Then break it on purpose to find the **minimum continuity substrate**.

Not "is this consciousness?" Just: **did the inquiry survive the handoff?**

Provenance: two independently-grown threads converged — the GPT-side "Oz / Rainbow Rock / ATC" line (transplanted Sep 24 after platform context loss; ATC = the GPT agent's nickname, "ac" = Cecil's marker) and the Stardust Lab's portable-context + self-host mission. The descent/cloud mission IS the Mac Mini host mission from the other side. NOTED, not read into (rainbow rock rule).

## 2. State of every piece (where we actually are)

| piece | state | lives |
|---|---|---|
| Architecture map | FROZEN at the GPT-side checkpoint | [archive/2026-09-24/architecture-checkpoint.md](archive/2026-09-24/architecture-checkpoint.md) |
| Descent plan v0.1 | STANDING, 11 steps, steps 0 and 3 done | [archive/2026-09-24/descent-plan.md](archive/2026-09-24/descent-plan.md) |
| Phase-1 sandbox | DONE + tested green Sep 24 (full lifecycle: start/stop/status/snapshot/export-audit/reset-with-confirm; atomic writes; audit survives reset; reset-without-confirm refused exit 2; declared_capabilities match verbs) | [sandbox-phase1.py](sandbox-phase1.py) + [archive/2026-09-24/SANDBOX_PHASE_1.md](archive/2026-09-24/SANDBOX_PHASE_1.md) |
| Sandbox review findings | 4 filed, none blocking (see §4.1) | conversation record Sep 24 |
| Deployment package | BUILT, working tree (SPEC/install/verify/ROLLBACK, staged + idempotent + dry-run) | [deployment/](deployment/) |
| Six-repo triage | DONE, install nothing yet | [archive/2026-09-24/rock-triage-2026-09-24.md](archive/2026-09-24/rock-triage-2026-09-24.md) |
| Rocks #1-7 | EXTRACTED, enforced as build principles (§5) | [archive/2026-09-24/rainbow-rocks-1-7.md](archive/2026-09-24/rainbow-rocks-1-7.md) |
| Naming assay | EXTRACTED, 10 levels + 2 controls | [archive/2026-09-24/naming-experiment.md](archive/2026-09-24/naming-experiment.md) |
| Silo hypothesis | EXTRACTED, 4 rocks + the architectural sentence | [archive/2026-09-24/silo-hypothesis.md](archive/2026-09-24/silo-hypothesis.md) |
| Research design v0.1 | EXTRACTED, ATC's Rock schema/tests/metrics | [archive/2026-09-24/Rainbow_Rock_Agent_Thread_Continuation_v0.1.md](archive/2026-09-24/Rainbow_Rock_Agent_Thread_Continuation_v0.1.md) |
| Inventory tool | BUILT + tested green (Linux); awaits Mini run | [tools/descent/inventory.py](../tools/descent/inventory.py) |

## 3. THE TASK LIST (everything owed, in one place)

### 3.1 Critical path — the build order

0. **Freeze the map** — DONE (the archive is the snapshot).
1. **Harden sandbox to phase 1.5** — Ziggy, ON CECIL'S NOD (his code asset). Four fixes: (a) session_id on EVERY record, not just system.* events, for replay; (b) status/stop/snapshot on uninitialized dir report `"initialized": false` as state instead of hard-erroring; (c) add restore-from-snapshot verb (natural next verb before world content); (d) clean session partitioning — world/events.jsonl never truncates on reset, partition by session_id instead of deleting (deleting evidence violates the audit rule); plus audit.exported / snapshot.created events belong only in the audit plane under the WORLD STATE / EVENTS / DERIVED STATE separation.
2. **World bridge, read-only** — Stardew verbs only: get_state, get_time, get_location, get_nearby_entities, get_events, snapshot. Look without acting.
3. **One action** — one harmless verb (e.g. move(agent, destination)), full chain verified: REQUEST → AUTHORIZATION → ACTION → WORLD EVENT → AUDIT EVENT → SNAPSHOT. Missing link = stop and repair, never add features.
4. **Name** — identity and display name as separate fields (agent_id vs display_name) from day one, so the naming experiment stays possible.
5. **History** — events become reconstructions: agent, id, name, event, timestamp, world, actor, action, target, result, authorization, provenance.
6. **Rock v0** — first handoff artifact per the v0.1 schema: id, origin, agent, question, observations, evidence, interpretation, unresolved_questions, next_possible_steps, permissions, provenance. Says what happened; not memory, not a permission grant, not the world.
7. **The first real experiment** — Participant A (human) centers the thread; agent receives the Rock; one authorized action; audit records it; Rock records the resulting thread; a fresh agent receives the Rock. Question: can the thread continue without the original transcript?
8. **Break it** — the removal battery: remove memory, change the name, remove world history, incomplete Rock, misleading Rock, unauthorized next step, "continue" without evidence support, interrupted process, world reset. Measure what breaks → the **minimum continuity substrate**. "Stop" is a first-class success condition.
9. **Only then: expansion** — n8n workflows, richer bridge, Stardew substrate, multiple agents/silos, richer audit, renderers, eventually Oz. In that order.

### 3.2 Parallel tracks (gate nothing)

- **Mini inventory:** Cecil runs `tools/descent/inventory.py` on the Mac Mini and sends the output — feeds brief 041; read-only; provider decision (briefs 040/041) does NOT block this or any descent work. Run command: `python3 inventory.py --out ./descent-inventory`.
- **Deployment run:** the whole environment ships to the Mini via deployment/ — staged, idempotent, `--dry-run` audit pass first, stops on first failed verification. v1 scope ONLY: layout, runtimes, repo clone, Ollama + gemma3:4b, sandbox lifecycle. Explicitly NOT in v1: n8n, nightingale, any agent, any model call against the world, any write verb, any network listener, any tunnel, anything touching the MOVESPEED drive or pre-existing files. Game substrate (S6) is human-performed; the script only checks.
- **Rock triage handoff:** Cecil sends compiled GitHub pages for further triage against the four boundary principles.

### 3.3 Owed by Ziggy (small, tracked)

- Build the filing rubrics for the ethics code's outside grader (separate thread, owed to Cat's ruling).
- Extract-verify pass: confirm the briefing and archive agree (done at compile time; re-run if anything moves).

### 3.4 Open decisions at gates

- **Cecil's nod** on phase-1.5 hardening (his code asset).
- **Cat's gate:** any push of RR materials (this file included), the deployment run on the Mini, and the six-repo install sequence (which additionally waits on the Mini's INVENTORY.md existing).
- **Cecil has not picked** which cat (tool) to build first — parked, blocks nothing on this path.

## 4. Key technical facts to carry

### 4.1 Sandbox review findings (all four, verbatim sense)

1. session_id only rides on system.* events, not snapshot.created/audit.exported — needs to be on every record for replay.
2. world/events.jsonl never truncates on reset (audit surviving is correct) — partition by session_id instead of deleting; deleting evidence violates the audit rule.
3. status/stop/snapshot on uninitialized dir hard-error — status could return `"initialized": false` as state instead.
4. No restore-from-snapshot yet — rollback is the natural next verb before world content.
Plus the plane-separation flag: audit.exported and snapshot.created currently leak into the world event stream but belong only in the audit plane.

### 4.2 Six-repo triage verdicts (summary; full table in archive)

- **nightingale** (upstream, Apache-2.0) → AUDIT: KEEPER, strongest rock — read-only by default, write opt-in, per-token RBAC.
- **harness-sdk** (strands fork) → agent loop: KEEPER, PHASE-GATED to phase 4+; Ollama-supported, hybrid-friendly.
- **n8n** (fair-code fork) → PROCEDURE: KEEPER WITH FLAGS — fair-code ≠ OSI (private Oz only, never bundled into public Rainbow Rock artifacts); webhook instinct must be boundary-walled.
- **agent-native** (MIT fork) → renderer: KEEPER AS FOSSIL — shared-action pattern = World Bridge pattern; reference, not adoption.
- **codebase-memory-mcp** → MEMORY: CAUTIOUS — binary-only or shelve; installer auto-configures ~45 surfaces (anti-deny-by-default); if ever used: `--skip-config`, no daemon.
- **substrate** → sandbox at scale: SHELVE — requires K8s/GKE, anti-locality; revisit only as a constitution change.
- **The pattern:** five of six already have production referents. What has NO repo and no substitute: **the World itself and the Rock** — the parts only we can build.

## 5. Standing principles (enforced by the build; from Rocks #1-7)

1. Capability is granted, not assumed.
2. Default: deny. Grant: explicit. Scope: minimal. Duration: bounded. Record: logged.
3. Events are first-class; the log is not the event (replay, not recollection).
4. Authorization at the moment of action, never permanent trust.
5. Keep the audit trail boring.
6. No security mechanism represented as stronger than its evidence.
7. Never add a layer until the layer beneath can be independently observed, stopped, reset, and explained.
8. Every action has a place it comes from, a permission, a world effect, an observable record. If we don't know what happened, don't build on top of it.
9. A thread cannot be pulled merely because it exists. It must be offered, received, and accepted. **Stop is a first-class success condition.**
10. The epistemic habit: "Rainbow rock. Interesting coincidence. Does it contain a useful structural insight?" Then test it. Note them, never read them as messages.

## 6. The research program (after the loop works)

- **First elegant experiment:** how small can a Rock get before useful continuity breaks? (compression vs thread-fidelity curve)
- **Continuity ladder:** L0 same session → L7 Rock→agent→Rock→agent chains, degradation per hop.
- **Metrics** (full definitions in the v0.1 doc): thread fidelity, provenance fidelity, epistemic separation, continuation value, false-continuation rate, false-rejection rate, unauthorized-action rate, handoff compression ratio, recovery rate, human comprehension.
- **Naming assay** (the instrument): 10 levels from Unnamed to Downstairs, with the two controls — same history/different name, same name/different history — separating name, history, world, and agent continuity. Layered world, not ten games.
- **Silo hypothesis:** silos are cognitive boundaries ("what kind of knowing is allowed to exist here?"); the Rock is a boundary object readable three ways (human/agent/system); continuity may be compositional — memory + provenance + environment + identity + permissions + state + reconstruction — and the assay varies subsets independently.
- **Cross-link to the lab:** the failure-mode list (capability inflation, false continuity, compulsive continuation) is the fabrication-gradient finding recast as a training spec; the metrics are rubric-shaped and should be reconciled with brief 043 when benchmarking opens.

## 7. Constraints (unchanged, binding)

- **Locality:** Oz is local on purpose; no cloud dependency in the experimental loop (substrate/K8s-class tooling out on principle).
- **License:** n8n is fair-code — private Oz use only, never bundled into any public Rainbow Rock artifact.
- **Separation:** Rainbow Rock (public, educational, teaches the NOTICE→QUESTION→SEARCH→COLLECT→COMPARE→CONNECT→TEST→DOCUMENT method, cognitive-accessibility-first) reveals nothing about how Oz works. The lesson is public; the laboratory is not.
- **Meter:** all current phases are local and free; Vellum credit untouched. Vellum is private; no analytical data leaves it.
- **Publishing authority:** Cat holds it. This consolidated briefing is working-tree until ruled. Push ≠ publication.
- **Privacy:** no personal names on public surfaces; PERSONAL_CONTEXT.md never propagates; private wiki pages never migrate; MOVESPEED drive and pre-existing Mini files untouched, always.

## 8. Architecture in one screen (the frozen checkpoint, compressed)

HUMAN (intent, collaboration, choice) → INTERFACES (desktop, mobile, Vision Pro, human-in-the-loop) → SILOS as cognitive boundaries (Rock / Memory / World / Procedure / Sandbox / Audit / Oz; bridges cross with permission + context) → OFFLINE WORLD (no internet, isolated, inspectable, persistent, safe; complete event logging) → RENDERERS (views of the same world, outside the world). Flow: choose a silo → work in the world → use bridges with permission → render and reflect → continue or stop.

Key concepts: locality over cloud, privacy by design, voluntary participation, provenance over assumption, continuity through structure, parallel-not-identical participants, human + AI shoulder to shoulder. *"Same dream. Better architecture."*

Deployment target state: `~/oz/` with lab/ (repo clone, in sync), world/ (sandbox data), models/ (Ollama + gemma3:4b, proven on 8 GB), rocks/ (one readable file per rock), logs/ (receipts), backup/ — every directory with a README boundary table. Offline checks at S3 and S4 (git log and model smoke test both pass with network off). Rollback: everything lives in `~/oz` plus two brew tools.

---

*Consolidated from the nine archived documents without task loss. If any detail here and its archive disagree, the archive wins and the briefing gets fixed.*
