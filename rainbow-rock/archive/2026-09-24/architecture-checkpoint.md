# Architecture checkpoint — the last GPT-side map

*Recorded Sep 24 from Cecil's diagram image ("what we cooked up there"). Not the current structure; the reference checkpoint from the platform side. Preserved here so the map survives outside any screenshot.*

## The stack

**HUMAN** — the dreamer, the planner, the pilot. Flows down: Intent, Collaboration, Choice.

**INTERFACES** — how you see, touch, interact: desktop/laptop (full control & visibility), mobile (on the go), Vision Pro (spatial/immersive), you (the human in the loop).

**SILOS (cognitive boundaries)** — different kinds of knowing; keep them separate, let them work together:
- **Rock** (research thread): inquiry state, evidence & notes, next steps, provenance, portable (hand off)
- **Memory** (learned context): preferences, skills & patterns, important facts, relationships, personal context
- **World** (observed state): environment, events/data, locations, simulations, external info
- **Procedure** (how to do it): workflows, tools & methods, templates, best practices, repeatability
- **Sandbox** (experiments): test/try, alternate paths, safe failure, isolated state, creative play
- **Audit** (accountability): logs, decisions, changes, provenance, what actually happened
- **Oz** (local & trusted): local only, key required, privacy & boundaries, continuity, home base

Cross-silo bridges run **with permission + context**.

**OFFLINE WORLD / SANDBOX** — the living, persistent world. No internet required. Simulated & real environments; objects, locations, time, state; agents & basic AI behaviors; inventory & interactions; deterministic where possible; complete event logging & audit trail. **No outbound network access: isolated, inspectable, persistent, safe.**

**RENDERERS** — different views of the same world: desktop (2D/3D), web (browser), Vision Pro (spatial), other devices (future). World state/events/logs flow to renderers for rendering, analysis, memory sync.

## The flow
1. You + interfaces — interact with the system (local, Apple)
2. Choose a silo — enter the right section of the brain
3. Work in the world — explore, observe, experiment
4. Use cross-silo bridges — when needed, with permission
5. Render + reflect — see, learn, adjust, continue (or stop)

## The Rainbow Rock (as mapped)
A portable thread. A handoff. **Not an access key.** Contains inquiry state; understandable to human + agent; carries provenance & permissions; may be passed (not taken).

## Key concepts
Locality over cloud. Privacy by design. Voluntary participation. Provenance over assumption. Continuity through structure. Parallel, not identical, participants. Human + AI, shoulder to shoulder.

## Key principles
Isolation first (sandbox is offline and controlled). Transparency (everything is logged, traceable, auditable). Modular (each silo has a clear responsibility). Flexible (swap models, tools, or renderers anytime). Human in the loop (you stay in control, always). Start small (version 0.1: one world, simple, observable).

*"Same dream. Better architecture."*
