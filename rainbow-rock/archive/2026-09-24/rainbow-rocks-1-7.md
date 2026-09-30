# Rainbow Rocks #1–7 — the found structural pieces

*Extracted Sep 24 from the PDF transcript "Rainbow Rock + Offline Oz" (agent side, GPT platform). Provenance: ATC's research notes, Cecil's thread. A "rainbow rock" = a small, holdable coincidence that becomes useful because it subtly strengthens the structure. Note them, test them, never read them as messages.*

**#1 — The Boundary Principle** (from the mCloud/device-farm architecture fossil). "Every capability available to an agent must cross an explicit, inspectable boundary." Nothing exists merely because the AI can discover it; something becomes available because we explicitly put it inside the boundary. The agent is a controlled intermediary between the thing being operated and the system doing the operating. Layer diagram gained: World → Environment/Device Fabric → Ground Control → Human.

**#2 — Capability is granted, not assumed** (from the MCP spec). Tools are model-controlled, but applications keep a human in the loop: deny tool invocations, make exposed tools visible, confirm operations. Don't add "MCP" to the constitution; add the durable principle that survives any protocol.

**#3 — Deny-by-default** (from GitHub's local sandboxing docs). Access is denied unless explicitly granted. Not "the AI can do everything except 17 things" but "the AI can do nothing until we give it something to do." Five-line security philosophy: **Default: deny / Grant: explicit / Scope: minimal / Duration: preferably bounded / Record: logged.**

**#4 — The event isn't the log** (from OpenTelemetry). Events are first-class objects: named occurrences at meaningful points (state changes, checkpoints, lifecycle, exceptions). Think WORLD STATE / EVENTS / DERIVED STATE, not a single world.log. The payoff is **replay** — reconstruct the sequence instead of trusting someone's recollection. Reinforces Article VI: Event → Evidence → Interpretation → Hypothesis.

**#5 — Authorization at the moment of action** (from OWASP agent security). Per-request authorization, not permanent trust established at startup. Log access with identity, query, and result. Trust doesn't become a credential.

**#6 — Keep the audit trail boring** (convergent pattern in local-agent projects). Every tool call recorded: decision, inputs, outputs, timing, session. Plus the honesty rule from a repo that warns its defenses are heuristics: **no security mechanism shall be represented as stronger than the evidence supporting it.** Article I applied to engineering.

**#7 — Separable layers** (from SandBase Harness). Model loop / agent runtime / sandbox / memory / governance / observability are separable layers. Don't make one component responsible for being the entire organism. The world can just be the world; everything else interfaces with it. The triangle that keeps the project honest: **Agreement (constitution) / Permission (security model) / Evidence (what actually happened).** If those three stay separate, the project is hard to accidentally corrupt.

**Bonus rock — the epistemic habit itself.** For exploratory research: "Rainbow rock. Interesting coincidence. Does it contain a useful structural insight?" Then test it. Neither "OMG it means something" nor "meaningless coincidence."
