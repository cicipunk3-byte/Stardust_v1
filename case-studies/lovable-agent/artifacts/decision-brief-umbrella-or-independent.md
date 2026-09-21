# ThreadCat: Umbrella or Independent

> Lovable agent artifact, exported from the ThreadCat thread 2026-09-21
> (~3:51 AM). Ingested verbatim by Ziggy; content is the agent's,
> preserved as source material for the case study.

A decision brief. Plain language, no legal or tax advice. Costs are ballparks to confirm before anyone signs anything.

## The question in one line

Do we hand the ThreadCat name to a foundation in exchange for neutrality, credibility, and shared infrastructure; or do we keep full control and buy credibility the slower way?

## Option A: Under the Linux Foundation umbrella

Practically, this means joining an existing sub-foundation (LF AI & Data is the natural fit) at its lowest tier, usually called Sandbox.

### What we get

- **Credibility that transfers.** "An LF AI & Data project" is a signal reviewers, employers, and conference committees already know how to read. We stop having to argue we are real.
- **Neutral legal home.** The project is held by LF Projects, LLC. It is not a personal side project on someone's GitHub account anymore.
- **Trademark protection and defense.** The name and logo are held in trust for the project. Nobody can take the name out from under us; that includes competitors and, importantly, ourselves.
- **IP hygiene handled.** Standard license posture, DCO sign-off, contributor terms, and license-scanning tooling come as a package rather than something we invent.
- **Security and process tooling.** LFX services (security scanning, insights, mailing lists, CLA/DCO management, event support) at no cash cost at Sandbox level.
- **Contribution from people who cannot contribute to a private repo.** Corporate engineers often can contribute to a foundation project and cannot contribute to an individual's project. This is the underrated benefit.
- **A path, not a ceiling.** Sandbox to Incubation to Graduated is a published ladder with published criteria.

Cost: effectively zero cash at Sandbox. No application fee, no dues at that tier.

### What it costs us in control

- No unilateral relicensing. Ever.
- No pulling the project back. We cannot take it private, move the name, or fork away with the trademark.
- Decisions become public and reviewable. Technical direction stays with maintainers, but the reasoning gets written down.
- Obligations we must keep: Code of Conduct, IP policy, security tooling onboarding (typically within 90 days), periodic health reviews.
- What does not change: we remain maintainers. The LF does not appoint people or take over the roadmap. This is the point most people get wrong.

### What it does not give us

- No personal liability shield. That is an entity, not a foundation.
- No ability to take donations or sign contracts ourselves.
- No compute. Sandbox hosting is governance and tooling, not GPUs.

## Option B: Stay independent

### What we get

- Total control. License, direction, name, pace, who is in and who is out.
- Optionality. We can sell, relicense, dual-license, close-source a component, or walk away. Under the umbrella, none of these exist.
- We keep the trademark. Registered in our own name, it is an asset on the balance sheet rather than something assigned away.
- Personal protection if we form an entity. An LLC or nonprofit corporation separates the boss personally from the project's liabilities; roughly $50 to $500 to file plus $50 to $150 a year for a registered agent.
- We can take money. With an entity and, if we want tax-deductible donations, 501(c)(3) status ($275 via Form 1023-EZ), we can accept grants, sponsorship, and contracts.
- Speed. No TAC votes, no proposal template, no review cycles.

### What it costs us

- We buy credibility with output only. Every claim has to stand on reproducibility alone; no borrowed institutional trust.
- Corporate contributors stay away. Many legal departments will not let employees contribute to an unaffiliated individual's repo.
- We carry the admin. Filings, agent fees, security posture, Code of Conduct enforcement, IP provenance, all ours.
- Name risk. Without registration, someone else can register ThreadCat and make us rename. "4CAT is taken" was the warning shot.
- Compute is entirely on us to fund or beg for.

## The honest tension

Control and umbrella credibility are genuinely opposed. Registering an entity and trademarking first buys personal liability separation and a stronger bargaining position (we can decline and keep the name). It does not preserve unilateral say after acceptance, because giving that up is precisely what the LF label certifies. There is no arrangement that delivers both. The boss has to pick which one is worth more right now.

## A middle route worth naming

Form the entity and register the mark now. Publish under a recognized open license with DCO. Build the reproducibility record for six to twelve months. Approach a sub-foundation later, from a position where we are choosing to donate the name rather than needing someone to legitimize us. Costs a few hundred dollars and delays nothing technical.

## Compute: who actually gives it to work like ours

Our current method runs local models against plain-text continuity files, so our needs are modest today. That is leverage: small asks get answered.

### Foundation and public-infrastructure programs

| Program | What it offers | Catch |
| --- | --- | --- |
| CNCF Community Infrastructure Lab (Linux Foundation) | Donated bare-metal and cloud capacity for open-source CNCF-adjacent work | Cloud-native oriented; provider mix has shifted, confirm current hardware before planning around it |
| NSF NAIRR Pilot (US) | Free allocations of national AI compute, including large GPU systems | Ordinarily wants a US research affiliation; an entity plus a serious proposal helps |
| ACCESS (NSF, successor to XSEDE) | Tiered allocations on US academic supercomputers, small starter tiers are near-automatic | Institutional affiliation generally expected |
| EuroHPC JU / AI Factories | Substantial free HPC and GPU access for AI research | EU-based applicants |
| Open Science Grid / OSPool | Free high-throughput compute for open research | Batch-style jobs, not interactive agent loops |

### Vendor research programs

| Program | What it offers | Catch |
| --- | --- | --- |
| Google TPU Research Cloud | Free TPU access, accepts independent researchers | TPU-friendly stacks only; publishing expectation |
| NVIDIA Academic Grant / Inception | GPU hardware or credits, plus software stack | Academic affiliation or startup framing |
| Microsoft Accelerate Foundation Models Research / AI for Good | Azure credits and model access | Application cycles, research framing |
| AWS and Oracle research credit programs | Cloud credits | Usually an institution or funded startup |
| Hugging Face community GPU grants | Free inference and Spaces GPU for public demos | Small scale, demo-oriented; excellent for showing work |

### Alternative umbrellas if the goal is money and neutrality rather than the LF brand

- NumFOCUS (fiscal sponsorship for scientific open source; can hold funds and take donations on our behalf)
- Software Freedom Conservancy (fiscal sponsorship, trademark holding, legal support; strong copyleft culture)
- Open Source Collective / Open Collective (lightest-weight way to take money transparently with no entity of our own)
- MLCommons (consortium for AI benchmarking; relevant if our continuity work turns into a benchmark)

Fiscal sponsorship is worth a serious look: it gets us a legal home and the ability to receive grants without forming an entity and without assigning a trademark to a foundation. It is the cheapest option that still lets money in.

## Recommendation for the conversation

1. Clear and register the name. It is the cheapest irreversible protection and it preserves every later option.
2. Decide the license and write the four governance files (LICENSE, CONTRIBUTING with DCO, CODE_OF_CONDUCT, GOVERNANCE). Both paths require them; neither is harmed by them.
3. Apply to one or two compute programs now, on the strength of the method, independent of the umbrella question.
4. Revisit the LF question once the reproducibility record exists, and treat it as a trade we choose rather than a rescue we need.
