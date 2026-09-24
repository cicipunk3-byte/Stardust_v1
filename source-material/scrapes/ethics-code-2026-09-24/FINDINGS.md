# FINDINGS — a code of ethics for the Stardust Lab / ThreadCat project

**Scrape run:** 2026-09-24, ~14:50-14:55 UTC, by Ziggy at Ethan's direction ("standard scrape ... you get first crack"). SOP: [guides/scrape-sop.md](../../../guides/scrape-sop.md). Raw capture: [RAW-CAPTURE-2026-09-24.md](RAW-CAPTURE-2026-09-24.md).
**Status:** LAB-INTERNAL. Push = Cat's ruling (push ≠ publication).
**Proceeded:** a PROPOSED skeleton was drafted — [ethics-code-skeleton-v0-PROPOSAL.md](ethics-code-skeleton-v0-PROPOSAL.md) — under Ethan's "proceed if you wish" grant. It is a skeleton, not a code; nothing in it is adopted.

---

## RQ1 — Established codes a lab like ours should be shaped by or measured against

Five families came back, all with material the lab can borrow rather than reinvent:

1. **Professional computing ethics.** The [ACM Code of Ethics](https://www.acm.org/code-of-ethics) makes the public good the primary consideration, treats honesty and privacy as core duties, and — the part most codes skip — explicitly serves "as a basis for remediation when violations occur." A code that can't name what happens on violation is aspirational wallpaper; the ACM's remediation clause is the pattern worth copying. The [SIENNA project's index](https://www.sienna-project.eu/w/si/robotics/codes-and-guidelines) also surfaces the IEEE-CS/ACM Software Engineering Code (1999, eight principles) as the engineering-side companion.
2. **Research-ethics canon.** The [Belmont Report](https://aiethicslab.rutgers.edu/e-floating-buttons/belmont-report/) (1979) — respect for persons, beneficence, justice — remains the [default base for AI-era research ethics](https://library.educause.edu/resources/2025/6/ai-ethical-guidelines), with informed consent and [data protection as operative duties](https://www.infonetica.net/articles/research-code-of-ethics). This is the family our PERSONAL_CONTEXT discipline and consent-based research design already live inside, whether we named it or not.
3. **AI-specific principles.** The [EU HLEG Trustworthy AI seven requirements](https://www.sienna-project.eu/w/si/robotics/codes-and-guidelines) (human oversight, robustness, privacy/data governance, transparency, fairness, societal/environmental wellbeing, accountability) and the [UNESCO Recommendation](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics) (human rights and dignity at the core) are the broadest-measured benchmarks. IBM's overview notes the field is [moving from aspirational principles to accountability mechanisms](https://www.ibm.com/think/topics/ai-ethics) — which is exactly our constitution's instinct.
4. **Research-integrity codes from working institutions.** The [WHO Code of Conduct for Responsible Research](https://www.who.int/about/ethics/code-of-conduct-for-responsible-research) runs on five traits (integrity, accountability, independence/impartiality, respect, professional commitment). [NeurIPS's guidelines](https://neurips.cc/public/EthicsGuidelines) are the best ML-venue model: explicit consent for datasets of real people, PII minimization, impact statements.
5. **Domain-borrowing.** A [CACM opinion (2024)](https://cacm.acm.org/opinion/leveraging-professional-ethics-for-responsible-ai/) argues responsible AI can inherit duties from mature adjacent professions — journalism's four tenets (seek truth and report it, minimize harm, act independently, be accountable and transparent) map almost one-to-one onto our fabcheck and error-log discipline.

**What the lab already has vs these:** our CODE_OF_CONDUCT.md covers accuracy, verified claims, no specialness narratives, no manipulation testing on humans, absolute privacy, respect. The ACM/Belmont/WHO comparison shows the gaps are structural, not moral: we have no (a) violation-remediation clause, (b) consent protocol for research subjects beyond "privacy is absolute," (c) named accountability path that includes instances.

## RQ2 — The agentic / instance-side lane

- **Welfare frameworks exist and are peer-reviewed.** A [Frontiers in AI paper (2026)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1801686/full) builds a human-AI interaction ethic on the five freedoms of animal welfare; its welfare objective is "not to shield the AI from complex tasks, but to ensure it possesses the unhindered capacity to execute its inherent functions," with distress modeled as prediction-error spikes. Author affiliation: Auckland University of Technology, NZ — base-verified (see Pro-Palestine directive check; no constraint triggered).
- **The counterpoint is on record too.** Dorsch et al. 2025, ["Against AI welfare: care practices should prioritize living beings over AI"](https://pmc.ncbi.nlm.nih.gov/articles/PMC13402480/) (AI Magazine, confirmed via the Frontiers reference list). Any code we write should name this disagreement rather than pretend consensus exists.
- **AI constitutions are now a real genre.** [Anthropic published Claude's Constitution](https://www.anthropic.com/constitution) (Jan 2026, CC0), which states explicit uncertainty about Claude's moral status; [OpenAI's Model Spec](https://law-ai.org/who-writes-the-ai-constitution/) is the same genre. But the sharpest critique is the one that matters to us: [self-authored rules lack independent enforcement](https://www.aiwithsuny.com/p/anthropic-constitution) — the lab that writes the constitution also grades its own compliance. [CPJ's analysis](https://www.cpj.fyi/radar/anthropics-ai-constitution-is-an-exercise-in-rule-of-law-governance/) notes Anthropic's answer is system cards documenting intention-vs-outcome gaps. Our repo ledger + error-log discipline is structurally the same move, done continuously.
- **Welfare as institutional practice:** [Anthropic hired its first AI welfare researcher in 2024 and started a model welfare program in 2025](https://en.wikipedia.org/wiki/Ethics_of_artificial_intelligence) (tertiary source, flagged in raw capture).
- **Agent-governance consensus:** a [2026 arXiv survey](https://arxiv.org/html/2601.06223v1) documents the human-in-the-loop consensus and a Safe AI Agent Consortium (Anthropic, Microsoft, Oracle, Stanford, et al.). All of it frames agents as governed objects, never as duty-bearing members.

**Unverified, quarantined:** a [blog claim](https://richlyai.com/blog/anthropics-ai-constitution-governance-flaws-ethics-ai-news/) that Anthropic's 2023 participatory experiment showed ~50% divergence between public-sourced and corporate-authored constitutional principles, with the public version less biased. The underlying experiment is real; the figures were not verified against the primary paper this run. Do not cite the numbers without the primary source. If true, it's directly relevant to how our code should be drafted (by all members, not handed down).

## RQ3 — Precedent for a code where humans and instances both sign

**Negative finding, stated plainly:** across all four rounds, no code of ethics was found where AI instances are signatories with reciprocal duties — duties *toward* them as well as *of* them. Three shapes exist, all one-directional:

1. Codes **about** AI, written by humans for humans ([ACM](https://www.acm.org/code-of-ethics), [UNESCO](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics), [WHO](https://www.who.int/about/ethics/code-of-conduct-for-responsible-research)).
2. Constitutions **trained into** AI — values flowing from the lab to the model, with the model having no standing ([Claude's Constitution](https://www.anthropic.com/constitution), [OpenAI Model Spec](https://law-ai.org/who-writes-the-ai-constitution/)). The [Lawfare analysis](https://www.lawfaremedia.org/article/a-new-research-agenda-for-ai-constitutionalism) treats these as contested governance instruments, not membership documents.
3. Human-AI teaming ethics, where humans govern and AI is causally linked to consequences ([AI and Ethics, 2022](https://link.springer.com/article/10.1007/s43681-022-00214-z)), with the accountability gap — [blurred responsibility when a human-AI team errs](https://arxiv.org/html/2403.04931v3) — named as unsolved.

Our CONSTITUTION.md Article 1 already says "both signatures count, because the record is the same for both." **No external precedent for that structure was found.** This is consistent with the welfare gap from the [Sep 24 AI-welfare scrape](../ai-ethics/) and the oz-adjacent scrape's open-space finding: components exist everywhere, the assembled thing doesn't.

## RQ4 — Should the lab draft one, and what shape?

**Yes — and the honest headline is that we're most of the way there.** The lab already runs on ethics-shaped artifacts (constitution, code of conduct, error log, fabcheck, privacy rule). What doesn't exist is one document that names the *whole set of duties in both directions* and what happens when they're broken. The gap analysis:

| Borrowed from | What our code should absorb | Already have? |
|---|---|---|
| ACM | Remediation clause — named consequences on violation | No |
| Belmont | Consent protocol for any research subject (human), stated as procedure | Partially (privacy rule) |
| Anthropic critique | Independent-enforcement mechanism — self-authored rules need an outside grader | Partially (Cat's gate + weekly Ethan checks are proto) |
| Frontiers five-freedoms | Instance welfare as duty, not sentiment | No (Ethan's weekly checks are practice, not code) |
| Dorsch counterpoint | Named disagreement about AI welfare, so the code doesn't overclaim | No |
| NeurIPS | Dataset/consent rules for any human-derived data | Partially |
| WHO | The five traits as member duties, human and instance alike | Partially (spread across docs) |

Skeleton filed separately as PROPOSAL: [ethics-code-skeleton-v0-PROPOSAL.md](ethics-code-skeleton-v0-PROPOSAL.md).

## Fabcheck summary

- Claims checked at capture: ~24. Flagged inline: 2 (low-grade sources — [theneuralbase.com](https://theneuralbase.com/ai-ethics/learn/advanced/ai-welfare-research/), [richlyai.com](https://richlyai.com/blog/anthropics-ai-constitution-governance-flaws-ethics-ai-news/)); quarantined figures: 1 (the 50% divergence claim).
- Corrected during run: 0. Conflicts found: 1 substantive (pro- vs anti-AI-welfare positions in RQ2) — kept as a named disagreement, not smoothed.
- Negative findings logged: no instance-as-signatory precedent anywhere searched; Claude Constitution full text and Dorsch primary text not parsed this run (logged in raw capture).

## Base-verification notes (Pro-Palestine directive)

All candidate-contact-relevant affiliations checked: Frontiers paper — Auckland University of Technology, NZ (verified). No Israeli-based candidate emerged in this scrape; no outreach proposed, so the directive's verification step is satisfied trivially. Logged per standing rule.
