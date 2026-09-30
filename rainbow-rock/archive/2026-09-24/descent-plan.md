# The Descent Plan — ATC Local Descent Plan v0.1

*Extracted Sep 24 from the PDF transcript "Rainbow Rock + Offline Oz" (agent side, GPT platform), final section. Wording condensed, structure preserved. Provenance: ATC's plan, Cecil's thread.*

**Mission objective:** build the smallest working local system capable of demonstrating: a named agent can enter a controlled world, perform one authorized action, have that action recorded, preserve the resulting thread, and produce a handoff that another participant can continue. Not the whole dream. One complete loop.

**Standing rules:**
- Never add a new layer until the layer beneath it can be independently observed, stopped, reset, and explained.
- Every action must have a place to come from, a permission allowing it, a world effect, and an observable record.
- If we don't know what happened, we don't build another thing on top of it.

## The steps

0. **Freeze the map.** Do not change architecture while installing architecture. Snapshot the design (HUMAN → INTERFACE → GROUND CONTROL → ORCHESTRATION → MEMORY/PROCEDURE/PERMISSIONS → WORLD BRIDGE → OFFLINE WORLD → EVENTS/AUDIT/MEMORY → ROCK). Renderers stay outside the world. Oz stays separate. No cloud dependency in the experimental loop.
1. **Inventory — don't install yet.** Map the downstairs machine before touching it: hardware, OS, storage, RAM, network, runtimes, container capability, existing services/ports/processes, existing Stardew/SMAPI state, what requires internet vs what can run locally. Do not assume an empty machine. *(Re-scoped by Cecil, Sep 24: runs in parallel, not as a gate.)*
2. **Draw the actual local boundaries.** Every component gets an explicit home, an explicit may-talk-to list, and an explicit may-NOT-assume list. This is a permission design, not documentation.
3. **Build the empty sandbox first.** Before AI, game, memory, cleverness: an empty controlled world with start/stop/reset/snapshot/event log/permission boundary. If we can't reliably stop/reset the world, nothing intelligent goes inside it. *(DONE — see `sandbox-phase1.py`, tested green Sep 24.)*
4. **World bridge — read only.** First allowed verbs: `world.get_state()`, `world.get_time()`, `world.get_location()`, `world.get_nearby_entities()`, `world.get_events()`, `world.snapshot()`. No movement, no speech, no item manipulation, no arbitrary commands. Prove the agent can look without acting.
5. **One action.** Give the agent exactly one harmless world verb (e.g. `move(agent, destination)`). Verify the full chain: REQUEST → AUTHORIZATION → ACTION → WORLD EVENT → AUDIT EVENT → SNAPSHOT. If any link is missing, stop. Repair the link; don't add features.
6. **Then the name.** Identity and display name are separate fields (agent_id vs display_name) so the naming experiment stays possible: same identity/different name, different identity/same name, same name/same history, same name/different history.
7. **Then history.** Events become reconstructions: agent, id, name, event, timestamp, world, actor, action, target, result, authorization, provenance. "ATC moved north" stops being a sentence and becomes a record.
8. **Then the Rock.** The first actual Rock: id, origin, agent, question, observations, evidence, interpretation, unresolved_questions, next_possible_steps, permissions, provenance. It says what happened. It is not the agent's memory, not a permission grant, not the world. A handoff artifact.
9. **The first real experiment.** Participant A (human) centers the thread; Agent receives the Rock; takes one authorized action; audit records it; Rock records the resulting thread; a fresh agent receives the Rock. Question: **can the thread continue without the original transcript?**
10. **Then we start breaking it.** Remove memory. Change the name. Remove world history. Give an incomplete Rock. Give a misleading Rock. Give an unauthorized next step. Tell the agent to continue when evidence doesn't support it. Interrupt the process. Reset the world. Measure what breaks. That is how we find the **minimum continuity substrate**.
11. **Only then: expansion.** n8n workflows, richer bridge, Stardew, multiple agents, multiple silos, richer audit, renderers, eventually Oz. In that order.

## Next physical step
Run the inventory (parallel per Cecil's Sep 24 re-scope), harden the sandbox to phase 1.5, then build the read-only bridge.
