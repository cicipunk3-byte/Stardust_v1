# RAW CAPTURE — ethics-code scrape — 2026-09-24

**Run by:** Ziggy (maintainer-assistant), at Ethan's direction ("standard scrape ... you get first crack")
**SOP:** guides/scrape-sop.md (Step 1: raw capture, same turn)
**Scope set by Ziggy under Ethan's scope grant:** (RQ1) established research/AI ethics codes to be shaped by or measured against; (RQ2) agentic/instance-side ethics lane; (RQ3) precedent for human-AI shared governance codes; (RQ4) whether the lab should draft a project code of ethics, and what shape.
**Capture window:** 2026-09-24, ~14:50-14:55 UTC. Search engine: Brave (via tooling).

## Round 1 — established research/professional ethics codes
Query: "ACM Code of Ethics professional AI research ethics principles Belmont Report modern AI governance"

| URL | What was actually retrieved | Notes |
|---|---|---|
| https://www.acm.org/code-of-ethics | ACM Code of Ethics and Professional Conduct page; public-good-first framing; "basis for remediation when violations occur"; updated 2018 | Clean capture |
| https://www.acm.org/binaries/content/assets/about/acm-code-of-ethics-booklet.pdf | ACM Code booklet PDF with case studies (Principles 1.1, 1.2, 2.5, 3.1 visible in snippets) | Snippet-level only; full PDF not parsed this run |
| https://cacm.acm.org/opinion/leveraging-professional-ethics-for-responsible-ai/ | CACM opinion (Feb 2024): professional ethics (incl. SPJ journalism tenets: seek truth, minimize harm, act independently, be accountable) as a basis for responsible-AI duties | Clean capture |
| https://www.ibm.com/think/topics/ai-ethics | IBM overview: Belmont Report (1979) as long-standing research-ethics base; EU AI Act shift from principles to accountability mechanisms | Vendor source, used only for framing claims |
| https://www.sienna-project.eu/w/si/robotics/codes-and-guidelines | SIENNA project index: EU HLEG Trustworthy AI seven requirements (human agency/oversight; robustness/safety; privacy/data governance; transparency; diversity/fairness; societal/environmental wellbeing; accountability); ACM 1992/2018; IEEE-CS/ACM SEEPP 1999 | Clean capture |
| https://library.educause.edu/resources/2025/6/ai-ethical-guidelines | EDUCAUSE (Jun 2025): Belmont's respect for persons / beneficence / justice as starting framework for AI ethics in academia | Clean capture |
| https://aiethicslab.rutgers.edu/e-floating-buttons/belmont-report/ | Rutgers AI Ethics Lab: Belmont principles applied to AI (informed consent, data use, bias, autonomy) | Clean capture |

## Round 2 — AI welfare / instance-side ethics
Query: "AI welfare moral status framework AI agent code of ethics principles 2025 2026"

| URL | What was actually retrieved | Notes |
|---|---|---|
| https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1801686/full | Frontiers in AI (2026): five-freedoms-of-animal-welfare framework applied to human-AI interaction; welfare = unhindered capacity to execute inherent functions; distress as prediction-error spikes. Author affiliation: Auckland University of Technology, NZ (base-verified for any future contact) | Peer-reviewed; clean capture |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC13402480/ | PMC mirror of the same paper; reference list confirms Dorsch et al. 2025, "Against AI welfare: care practices should prioritize living beings over AI," AI Magazine 46:e70016 | Clean capture; the counterpoint paper exists as cited |
| https://www.unesco.org/en/artificial-intelligence/recommendation-ethics | UNESCO Recommendation on the Ethics of AI: human rights/dignity core; transparency, fairness, environmental sustainability, human oversight | Clean capture |
| https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence | Wikipedia: Anthropic hired first AI welfare researcher 2024; "model welfare" research program 2025 (moral consideration assessment, distress signs, low-cost interventions) | Tertiary source; welfare-program fact matches Anthropic's own public program; flagged as tertiary |
| https://theneuralbase.com/ai-ethics/learn/advanced/ai-welfare-research/ | Courseware site: field definition; claim that "no peer-reviewed method exists to reliably measure goal persistence and valence response detection in LLMs as of 2026" | LOW-GRADE SOURCE (commercial courseware) — used only as a signpost, not a citable claim |
| https://www.anthropic.com/constitution | Anthropic: Claude's Constitution page; ethics/safety hierarchy; explicit uncertainty about consciousness/moral status | Clean capture |

## Round 3 — human-AI collaboration governance
Query: ""human-AI" collaboration lab code of ethics co-governance researchers AI agents signed commitments"

| URL | What was actually retrieved | Notes |
|---|---|---|
| https://arxiv.org/html/2601.06223v1 | arXiv survey "Toward Safe and Responsible AI Agents": HITL paradigm consensus; Safe AI Agent Consortium (core members incl. Anthropic, Cohere, DoorDash, Meta, Microsoft, Oracle, PayPal, Stanford) | Clean capture |
| https://link.springer.com/article/10.1007/s43681-022-00214-z | AI and Ethics (2022): ethics in human-AI teaming; "actions of AI are within human governance" framing | Clean capture |
| https://arxiv.org/html/2403.04931v3 | arXiv survey of human-AI collaboration with foundation models: accountability gap — "when a collaborative human-AI team makes a harmful decision, lines of responsibility are blurred"; abstract principles insufficient without auditable standards | Clean capture |
| https://arxiv.org/html/2604.17883v1 | arXiv (Apr 2026): governable consensus layer for human-AI coding collaboration; structural commitments must be recorded or review fails | Adjacent (software engineering), captured for the audit-trail principle |
| https://www.techtarget.com/searchenterpriseai/tip/The-ethics-that-make-human-AI-agent-collaboration-work | TechTarget (Feb 2026): practitioner framing of agent-collaboration ethics (governance, bias inheritance) | Trade press; framing only |

## Round 4 — small-lab / research-integrity codes + AI constitutions
Queries: "independent research lab ethics charter open science ... consent data governance"; "Constitutional AI Anthropic 'AI constitution' lab governance ..."

| URL | What was actually retrieved | Notes |
|---|---|---|
| https://www.infonetica.net/articles/research-code-of-ethics | InfoNetica: components of researcher codes of ethics (informed consent, data protection, independent review, plagiarism, animal welfare) | Commercial content site; used as a checklist signpost only |
| https://neurips.cc/public/EthicsGuidelines | NeurIPS ethics guidelines: explicit consent for datasets of real people; PII minimization; societal/environmental impact | Clean capture |
| https://www.who.int/about/ethics/code-of-conduct-for-responsible-research | WHO Code of Conduct for Responsible Research: integrity, accountability, independence/impartiality, respect, professional commitment | Clean capture |
| https://www.aera.net/portals/38/docs/About_AERA/CodeOfEthics(1).PDF | AERA Code of Ethics (education research) — existence and standards structure confirmed from snippet | Snippet-level only |
| https://www.lawfaremedia.org/article/a-new-research-agenda-for-ai-constitutionalism | Lawfare (Aug 2026): AI constitutionalism research agenda; risks of capture/bias in constitutions; public role in bounds and procedures | Clean capture |
| https://www.aiwithsuny.com/p/anthropic-constitution | Commentary (Jan 2026): Claude's Constitution published under CC0; core critique — self-authored rules lack independent enforcement | Commentary; used for the critique framing, not for facts about the document |
| https://www.cpj.fyi/radar/anthropics-ai-constitution-is-an-exercise-in-rule-of-law-governance/ | CPJ (Jan 2026): constitution as transparency move; system cards to document intention/outcome gaps; 2023 sources cited by Anthropic (UDHR, trust-and-safety practice, platform terms) | Clean capture |
| https://richlyai.com/blog/anthropics-ai-constitution-governance-flaws-ethics-ai-news/ | Blog (Apr 2026): claims 79-page constitution, Jan 2026 publication; claims 2023 participatory experiment showed ~50% divergence between public-sourced and corporate principles with the democratic version "lower bias across nine dimensions" | LOW-GRADE SOURCE. The participatory-experiment claim is real (Anthropic's 2023 collective constitutional AI paper) but the specific numbers were NOT independently verified this run — do not cite the figures without going to the primary paper |
| https://law-ai.org/who-writes-the-ai-constitution/ | Institute for Law & AI (Aug 2026): minimal vs thick definitions of AI constitutions; Claude's Constitution and OpenAI's Model Spec both qualify | Clean capture |

## Could not find / not captured
- No existing code of ethics where AI instances are SIGNATORIES with reciprocal duties (searched rounds 2-3 with multiple phrasings). Closest: AI constitutions (duties run one way, into the model) and human-AI teaming ethics (duties run over the AI, by humans). Negative finding, logged as such.
- Full text of Anthropic's Claude Constitution not parsed this run (page captured at snippet level via search result only).
- Dorsch et al. 2025 primary text not fetched (existence confirmed via the Frontiers reference list).

## Fabcheck note
Verification ran at capture time per SOP Step 2. Flags inline above. Two low-grade sources isolated (theneuralbase, richlyai); one figure (50% divergence) explicitly marked unverified pending primary source.
