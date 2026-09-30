# Raw capture log — oz-adjacent-research scrape, 2026-09-24

Operator: Ziggy. Scope confirmed by Cat (/cat, "all look good. happy hunting"), all five RQs. Round 1: five web searches (Brave provider), one per RQ. Round 2: one arXiv fetch + two targeted searches. Captures are search-provider excerpts of the listed sources, saved the same turn per SOP step 1. Timestamps UTC.

## Round 1 (~14:10-14:15 UTC)

| # | query | key sources retrieved |
|---|---|---|
| 1 | RQ1 memory offloading | arxiv.org/html/2603.07670v1 (Memory for Autonomous LLM Agents survey); github.com/Shichun-Liu/Agent-Memory-Paper-List; arxiv.org/html/2604.08224v1 (Externalization in LLM Agents); arxiv.org/html/2606.30306v1 (Always-On Agents survey); mem0.ai/blog/state-of-ai-agent-memory-2026; emergentmind.com persistent-memory topic page; arxiv.org/html/2603.19935 (Memori); arxiv.org/html/2606.24775 (agent-native memory system) |
| 2 | RQ2 governed agent runtimes | github.com/systempromptio/awesome-ai-agent-governance; orca.security runtime tools roundup; openhands.dev blog (self-hosted coding agents); opensource.microsoft.com Agent Governance Toolkit announcement; github.com/siyad01/agentbox; github.com/bureado/awesome-agent-runtime-security; flowtivity.ai AGT writeup |
| 3 | RQ3 oversight labs | kore.ai observability blog (VENDOR); arthur.ai playbook (VENDOR); labs.cloudsecurityalliance.org CAISI research note; deloitte.com observability article (VENDOR); linkedin framework post (VENDOR); arxiv.org/html/2506.04836 (public-sector oversight structures); arxiv.org/html/2508.18765v1 (Governance-as-a-Service); dash.datadoghq.com session page (VENDOR) |
| 4 | RQ4 frugal AI | researchsquare.com energy-efficient RAG survey (RS-10597421); arxiv.org/html/2608.21621 (FrugalSOT); medium SLM piece (LOW-GRADE source); arxiv 2305.05176 (FrugalGPT); pith.science SLM citation page; arxiv.org/html/2609.11940 (battery price of edge AI); nexos.ai FrugalGPT explainer (VENDOR) |
| 5 | RQ5 experience compounding | arxiv.org/abs/2505.16067 + html v2 (experience-following behavior); aclanthology.org/2026.acl-long.27 (same, published); arxiv.org/html/2604.27003v1 (experience reuse / continual learning at memory level); preprints.org 202601.0618 (storage→reflection→experience survey); dl.acm.org ACT-R-inspired memory architecture (10.1145/3765766.3765803) |

## Round 2 (~14:20 UTC)

| # | target | retrieved |
|---|---|---|
| 6 | arxiv.org/abs/2606.30306 full abstract page | authors: Tianyu Ding, Aditya Nannapaneni, Bingfan Liu, Ling Zhang; submitted 29 Jun 2026; cs.MA/cs.AI; affiliations NOT stated on page (base verification PENDING); abstract captured incl. AOEP-v0 protocol and six diagnostic axes |
| 7 | AgentOps authorship search | AgentOps paper (arXiv 2411.05285): Liming Dong (CSIRO's Data61), Qinghua Lu (Data61/UNSW), Liming Zhu (Data61/UNSW), Sydney, Australia; taxonomy of AgentOps observability |
| 8 | longitudinal deployment study search | arxiv.org/abs/2601.17087 (Lost in Simulation, Seshadri et al., multi-country user study); arxiv.org/abs/2501.04227 + agentlaboratory.github.io (Agent Laboratory, Schmidgall et al.); PMC13542291 (persona-prompted agents, Serbia institutes); JAI multi-agent empirical evaluation; Springer agentic AI survey |

## Retrieval notes
- No paywalls hit. No JS-rendered failures. Search-provider snippets are the capture medium for round-1 sources; the arXiv abstract page was fetched in full.
- Fabcheck flags raised during capture are recorded inline in FINDINGS.md, not here.
