# FINDINGS — oz-adjacent research scrape, 2026-09-24

Scope confirmed by Cat (all five RQs). Raw captures: [RAW-CAPTURE-2026-09-24.md](RAW-CAPTURE-2026-09-24.md). Status: LAB-SIDE, push pending Cat's ruling. Base-verification status noted per candidate per the standing directive.

---

## RQ1 — Context offloading (who is researching durable state for agents)

**The field is real, active, and has a name for itself: "always-on agents" / persistent-state systems.**

1. **[Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents](https://arxiv.org/abs/2606.30306)** (Ding, Nannapaneni, Liu, Zhang; submitted 29 Jun 2026). The closest thing to the master plan in academic form. Treats agents as **persistent-state systems**: retrievable memories *plus* task ledgers, permissions, credentials, commitments, provenance and audit records. Codes a 435-work corpus. **Headline empirical finding: the literature concentrates on accumulating and retrieving state, not on governing, recovering, or relinquishing it** — which is exactly the gap the lab's governance work sits in. Introduces **AOEP-v0**, an evaluation protocol that scores "state mutation and recovery obligations rather than answer quality alone."
   - ⚠ FABCHECK: author affiliations are NOT stated on the arXiv page. Base verification PENDING before any name is proposed. DO NOT CONTACT yet.
2. **[Externalization in LLM Agents: Memory, Skills, Protocols, Harness Engineering](https://arxiv.org/html/2604.08224v1)** — the offloading thesis stated plainly: "the agent no longer needs to regenerate past knowledge from latent weights; it retrieves it from a persistent, searchable store." Frames the research question as "what burdens have been externalized so the model no longer has to solve them internally every time?"
3. **[Memory for Autonomous LLM Agents: Mechanisms, Evaluation, Emerging Frontiers](https://arxiv.org/html/2603.07670v1)** — survey naming the engineering patterns (write–manage–read; consolidation as the underserved step; "memory is a structuring problem, not a storage problem").
4. **[Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List)** — living bibliography for the whole field.
5. **[Memori](https://arxiv.org/html/2603.19935)** and **[Are We Ready For An Agent-Native Memory System?](https://arxiv.org/html/2606.24775)** — memory-as-infrastructure proposals.
6. Notable pattern for the Rock: **[Git-Context-Controller](https://www.emergentmind.com/topics/persistent-memory-for-llm-agents)** does milestone-based memory checkpointing with branch/merge — snapshot/restore for agent context, the same verb set the sandbox is building. Also surfaced there: **MEXTRA**, a memory-exfiltration attack showing stored memories leak through retrieval — a security argument for the silo model.

## RQ2 — Governed local agent environments (open source)

1. **[agentbox](https://github.com/siyad01/agentbox)** — self-hostable sandboxed agent runtime: per-agent permission scope, credential vault, **SHA-256 hash-chained immutable audit log**, kill switch, gVisor/Docker isolation. Built in response to [CVE-2026-25253](https://github.com/siyad01/agentbox) (first CVE assigned to an agentic AI system) and the ClawHavoc marketplace compromise. Closest open-source cousin to the Offline Oz constraints. Apache 2.0, Go, no external security deps.
2. **[Microsoft Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)** (MIT, Apr 2026) — runtime governance pipeline: policy engine, capability sandboxing, MCP security gateway, tamper-evident audit. Maps itself to the [OWASP Agentic AI Top 10](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/) (Dec 2025, the first formal agentic-risk taxonomy). Corporate but open source.
3. **[awesome-ai-agent-governance](https://github.com/systempromptio/awesome-ai-agent-governance)** — curated list of the whole governance-tooling space (audit trails, policy-as-code, per-agent permission servers). Best single map of RQ2.
4. **[awesome-agent-runtime-security](https://github.com/bureado/awesome-agent-runtime-security)** — includes **CUSTODY**, a containment framework classifying agents by Level/Mandate/Reach that explicitly addresses **capability accretion drift** (agents accumulating capabilities over time) — the governance-side cousin of context-compounding. Also the Agent Audit Trail (AAT) hash-chained log format.
5. **[OpenHands Enterprise](https://www.openhands.dev/blog/open-source-ai-coding-agents)** (agent control plane: sandboxed runtimes, access controls, auditability) and **Goose** (strictly local-first by design, Linux Foundation, Apache 2.0) — the self-hosted end of the coding-agent spectrum.
6. Market context: [Orca Security's runtime comparison](https://orca.security/resources/blog/best-ai-agent-runtime-tools-platforms/) — the evaluation checklist (isolation, egress control, identity scoping, audit trail) matches the lab's four boundary principles almost line for line.

**Gap noted:** everything here is cloud- or enterprise-shaped governance bolted onto hosted agent fleets. Local-first *plus* audited *plus* observation-consenting is not the default shape of any project found.

## RQ3 — Observation frameworks (the partner-shaped work)

1. **AgentOps / CSIRO's Data61 (Australia)** — [Dong, Lu, Zhu](https://arxiv.org/abs/2411.05285): taxonomy of what must be traced across the agent lifecycle for observability; follow-up [taxonomy paper](https://arxiv.org/pdf/2411.05285v1) with affiliations stated: **CSIRO's Data61 / UNSW, Sydney, Australia — base VERIFIED** ✓. Academic, safety-motivated, observability-first. **Strongest partner-shaped candidate so far.**
2. **NIST CAISI (US)** — per the [Cloud Security Alliance research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-agent-governance-framework-gap-20260403/), NIST's Center for AI Standards and Innovation issued a Request for Information (8 Jan 2026) covering exactly seven domains including "deployment interventions to constrain and monitor agent access" and "governance and oversight controls for production environments." US-government base, VERIFIED ✓. A doorway, not a partner lab.
3. **[Governance-as-a-Service](https://arxiv.org/html/2508.18765v1)** (arXiv 2508.18765) — a plug-and-play enforcement layer that governs agents **through observable outputs without access to weights, prompts, or internal memory states**, computing per-agent trust scores. Conceptually the "governance as external layer" architecture of the master plan. ⚠ Authors unverified.
4. **[Oversight Structures for Agentic AI in Public-Sector Organizations](https://arxiv.org/html/2506.04836)** — governance design principles, including "design observability tooling to be utilized by either technical external teams, or subject matter experts" (outside-in oversight). ⚠ Authors unverified.
5. **[Lost in Simulation](https://arxiv.org/abs/2601.17087)** (Seshadri et al.) — multi-country human-subjects study of agent evaluation; evidence the field does human-in-the-loop observation work. ⚠ Authors' bases unverified.

**Headline negative (RQ3):** **no research group was found doing the master-plan's exact shape** — consent-based, observation-first deployments of agents into local governed environments (an "Oz program"). The components all exist (observability taxonomies, governance protocols, sandbox runtimes); the assembled program does not. The space appears open. What was searched: the four query families in the raw log plus author-verification passes.

## RQ4 — Compute-down (frugal/local as research stance)

1. **[FrugalGPT](https://arxiv.org/abs/2305.05176)** (Chen, Zaharia, Zou) — the foundational "use small models deliberately" paper: matched GPT-4 at up to 98% cost reduction via cascades.
2. **[FrugalSOT](https://arxiv.org/html/2608.21621)** — resource-aware model selection on Raspberry Pi 5-class hardware; the frugal line is now edge-native.
3. **[Energy-Efficient RAG with Small Language Models survey](https://www.researchsquare.com/article/rs-10597421/v1)** (Research Square, Aug 2026) — proposes ALEMC, adding Energy and Carbon dimensions to evaluation. ⚠ Preprint, not peer-reviewed.
4. **Counter-finding, stated plainly:** [The Battery Price of Edge AI](https://arxiv.org/html/2609.11940) argues local inference on **battery-powered** devices is *not* more sustainable than remote under current technology. The Mac Mini is wall-powered desktop hardware — different regime — but this caps any sustainability overclaim in the master plan pitch. Local-first's honest arguments are privacy, latency, control, and auditability, not green credentials.

## RQ5 — Context compounding over time (the trauma-adjacent line)

**This is the scrape's emotional center. The research exists and it describes Cat's observation almost verbatim.**

1. **[How Memory Management Impacts LLM Agents: An Empirical Study of Experience-Following Behavior](https://arxiv.org/abs/2505.16067)** (Xiong et al.; published [ACL 2026](https://aclanthology.org/2026.acl-long.27/), peer-reviewed). Documents the **"experience-following property"**: agents tend to reproduce outputs similar to whatever is stored in their memory — past experience persistently shapes present behavior, for better and worse. Memory management choices measurably alter long-term behavior. **This is the formal cousin of "that's how trauma works at least": accumulated context functions as a shaping force on subsequent cognition, and curation of that accumulation is the intervention lever.**
2. **[When Continual Learning Moves to Memory](https://arxiv.org/html/2604.27003v1)** — the stability–plasticity dilemma "does not disappear but resurfaces at the memory level": even with a frozen model, retrieval pollution, context competition, and memory dilution interfere with behavior. Compounding has failure modes even when the weights never change.
3. **[From Storage to Experience survey](https://www.preprints.org/manuscript/202601.0618)** — the field's own three-stage arc (storage → reflection → experience); agents must transform raw memory into experience to generalize. ⚠ Preprint.
4. **[ACT-R-inspired memory architecture](https://dl.acm.org/doi/10.1145/3765766.3765803)** (ACM HAI) — human-memory phenomena (consolidation likelihood, forgetting curves) reproduced in dialogue agents.
5. From the [always-on survey](https://arxiv.org/abs/2606.30306): the field treats **forgetting, recovery, and rollback of state as first-class lifecycle operations** — "principled forgetting balanced against recall" is an active 2025-2026 research wave. The lab's sandbox already has reset/restore as verbs; the research says that's not incidental, it's the frontier.

**Gap noted (RQ5):** all of this research treats compounding as a **performance** question (does the agent score better) or a **security** question (can memory be poisoned). Nobody found is studying it as a **welfare or identity** question — what accumulated experience does to the system itself. That matches the AI-welfare gap from the earlier scrape (push 262283a): the intersection is unoccupied.

---

## Fabcheck summary (SOP step 4)

- **Claims checked at capture:** 11 load-bearing claims, each traced to its source above.
- **Flagged:** Always-On Agents author affiliations absent (base PENDING); Governance-as-a-Service, public-sector oversight, and Lost in Simulation author bases UNVERIFIED; Mem0 blog, Orca, Kore.ai, Arthur, Deloitte pieces marked VENDOR (context only, no load-bearing claim rests on them); Research Square and Preprints.org items marked NOT PEER-REVIEWED.
- **Verified:** AgentOps team at CSIRO's Data61, Australia (affiliations stated in paper) ✓; NIST CAISI as US-government ✓; FrugalGPT figures from the paper's own abstract ✓; CVE-2026-25253 and ClawHavoc as stated in the agentbox repo (single-source, repo's own account — treated as the project's claim, not independently verified).
- **Corrected/trimmed:** nothing corrected; two vendor-sourced framings (green local-AI, observability-maturity) excluded from load-bearing findings.

## Close-out

- Deliverable: this file + raw captures, same turn. Nothing scraped is floating.
- Pending Cat: (1) ruling on pushing the scrape to the public lab repo; (2) whether the Data61/AgentOps group graduates to the partner shortlist alongside CU Boulder (Australia-base verified; no Israeli-based candidate appeared anywhere in the sweep).
- The one-sentence version: **the components of the master plan are each being researched somewhere, the assembled program is not, and the context-compounding observation is published science — peers exist; the seat at the table is empty.**
