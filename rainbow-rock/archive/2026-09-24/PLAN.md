# Rainbow Rock / Offline Oz — Master Plan

**Version:** 1.0
**Date:** 2026-09-24
**Status:** PROPOSAL — local work proceeds freely; any push or publication waits on Cat's gate
**Authors:** Cecil (pilot, design) + Ziggy (maintainer-assistant, build)
**Provenance:** two independently-grown threads converged — the GPT-side "Oz / Rainbow Rock / ATC" line (transplanted Sep 24 after platform context loss) and the Stardust Lab's portable-context + self-host mission. This package is the joined record.

---

## 0. What this package is

One home for the whole program:

| file | what it is |
|---|---|
| `PLAN.md` | this document — the bundle |
| `descent-plan.md` | the 11-step build order, extracted from the transcript |
| `rainbow-rocks-1-7.md` | the seven found structural principles |
| `naming-experiment.md` | the ten-level naming assay + the two controls |
| `silo-hypothesis.md` | compartments, compositional continuity, provenance |
| `architecture-checkpoint.md` | the last GPT-side architecture map, preserved in text |
| `Rainbow_Rock_Agent_Thread_Continuation_v0.1.md` | ATC's foundational research design (Rock schema, tests, metrics) |
| `sandbox-phase1.py` | phase-1 empty sandbox — TESTED GREEN Sep 24 |
| `SANDBOX_PHASE_1.md` | sandbox doc + the phase-2 verification rule |
| `rock-triage-2026-09-24.md` | verdicts on the six repos |

## 1. Mission

Build the smallest working local system that demonstrates **continuity without continuous presence**: a named agent enters a controlled world, performs one authorized action, the action is recorded, the thread is preserved as a Rock, and another participant continues from the Rock alone. Then break it on purpose to find the **minimum continuity substrate**.

Not "is this consciousness?" Just: **did the inquiry survive the handoff?**

## 2. Where we are (Sep 24)

- Phase-1 empty sandbox: **done and tested** (full lifecycle green; review findings filed in the triage conversation: session_id on all records, status-not-error, restore verb, session partitioning).
- Architecture map: **frozen at the checkpoint** (see `architecture-checkpoint.md`).
- Component triage: **done** — six repos mapped to silos; two keepers (nightingale → Audit; harness-sdk → agent loop, phase-gated), one keeper-with-flags (n8n → Procedure), three fossils/cautious (agent-native, codebase-memory-mcp, substrate).
- Descent plan: **extracted and standing** (see `descent-plan.md`; step 1 inventory re-scoped parallel per Cecil's Sep 24 ruling).

## 3. The build order

0. **Freeze the map** — done (this package is the snapshot).
1. **Harden the sandbox to phase 1.5** — Ziggy, on Cecil's nod: session_id on every record, restore-from-snapshot verb, status reports uninitialized as state, audit-plane events separated from world events.
2. **World bridge, read-only** — Stardew verbs only: get_state, get_time, get_location, get_nearby_entities, get_events, snapshot. Look without acting.
3. **One action** — one harmless verb, full chain verified: request → authorization → action → world event → audit event → snapshot.
4. **Name** — identity and display name as separate fields from day one.
5. **History** — events as reconstructions with provenance.
6. **Rock v0** — the first handoff artifact per the v0.1 schema.
7. **The first experiment** — can a fresh agent continue the thread from the Rock alone?
8. **Break it** — the removal battery; find the minimum continuity substrate.
9. **Only then** — expansion (procedure plane, richer bridge, multiple silos, renderers).

**Parallel track (Mini):** run `tools/descent/inventory.py` on the Mac Mini whenever convenient — feeds brief 041, gates nothing.

**Parallel track (the migration):** the whole environment ships to the Mini via `deployment/` — SPEC.md (the target state, verifiable claim by claim), install.sh (staged, idempotent, `--dry-run` for the audit pass, stops on first failed verification), verify.sh (the dry-run audit: every spec claim becomes a command, PASS/FAIL table, receipt to `~/oz/logs/`), ROLLBACK.md (per-stage undo; a stage without a rollback line doesn't ship). Cecil's law on record: **less about plans moving, more about protecting the movement with planning.** v1 scope: layout, runtimes, repo clone, Ollama + gemma3:4b, sandbox lifecycle — no network listeners, no tunnel, no agents in the world, MOVESPEED drive untouchable. Game substrate (S6) is human-performed; script only checks.

## 4. The two original engineering problems

Five of six triaged repos already cover silos that exist as production systems. The parts with **no repo and no substitute**: **the World itself** and **the Rock**. Everything else is assembly. Those two get the original work.

## 5. Standing principles (from the rocks, enforced by the build)

1. **Capability is granted, not assumed.**
2. **Default: deny. Grant: explicit. Scope: minimal. Duration: bounded. Record: logged.**
3. **Events are first-class; the log is not the event.**
4. **Authorization at the moment of action.**
5. **Keep the audit trail boring.**
6. **No security mechanism represented as stronger than its evidence.**
7. **Never add a layer until the layer beneath can be observed, stopped, reset, explained.**
8. **A thread cannot be pulled merely because it exists. It must be offered, received, and accepted. Stop is a first-class success condition.**

## 6. Constraints

- **Locality:** Oz is local on purpose. No cloud dependency in the experimental loop. (substrate/K8s-class tooling is out on principle, not difficulty.)
- **License:** n8n is fair-code — private Oz use only, never bundled into any public Rainbow Rock artifact.
- **Separation:** Rainbow Rock (public, educational, teaches the method) reveals nothing about how Oz works. The lesson is public; the laboratory is not.
- **Meter:** all current phases are local and free; Vellum credit untouched. Vellum is private; no analytical data leaves it.
- **Publishing authority:** Cat holds it. This package is working-tree until ruled on. Push ≠ publication.
- **Privacy:** no personal names on public surfaces; PERSONAL_CONTEXT.md never propagates; private wiki pages never migrate.

## 7. The research program (after the loop works)

- **First elegant experiment:** how small can a Rock get before useful continuity breaks? (compression vs. thread-fidelity curve)
- **Continuity ladder:** L0 same session → L7 Rock→agent→Rock→agent chains, degradation measured per hop.
- **Metrics:** thread fidelity, provenance fidelity, epistemic separation, continuation value, false-continuation rate, false-rejection rate, unauthorized-action rate, handoff compression ratio, recovery rate, human comprehension. (Full definitions in the v0.1 doc.)
- **Cross-link to the lab:** the failure-mode list (capability inflation, false continuity, compulsive continuation) is the fabrication-gradient finding recast as a training spec; the metrics are rubric-shaped and should be reconciled with brief 043 when benchmarking opens.
