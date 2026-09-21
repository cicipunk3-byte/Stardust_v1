# ThreadCat: Step-by-Step Roadmap

> Lovable agent artifact, exported from the ThreadCat thread 2026-09-21
> (~4:01 AM). Ingested verbatim by Ziggy; content is the agent's,
> preserved as source material for the case study.

From where we are today (live site, public repo, no legal structure) to a protected project with a fiscal sponsor. Two forks at the end: NumFOCUS or Software Freedom Conservancy.

Not legal or tax advice. Every dollar figure and timeline is a ballpark to confirm directly with the source before anyone commits.

## Read this first: the control question, honestly

Because protecting Cat's history is the priority, one thing has to be said plainly up front.

Fiscal sponsorship comes in two strengths, and they differ exactly where we care:

- **Light sponsorship / affiliation.** The sponsor lends credibility and, in some arrangements, a way to receive funds. We keep the copyright, the trademark, and the domain. Control stays with us.
- **Full ("comprehensive") sponsorship.** The sponsor becomes the legal home of the project. In practice that usually means assigning the trademark and sometimes other project assets to them, so they can defend the project and hold funds for it. Software Freedom Conservancy is explicit about holding project assets; NumFOCUS's Sponsored Project tier involves a fiscal sponsorship agreement covering funds and typically project marks.

So the same tension from the Linux Foundation brief reappears, just smaller. Anyone who can legally defend the name on our behalf generally has to hold the name.

What is never assigned in either case: copyright in the code and the written research. With an open license plus DCO sign-off, contributors keep their copyright, and so do we. Cat's authorship of the work itself is not on the table in any of these arrangements.

What protects her history most directly is not the umbrella at all. It is: a registered trademark we own, an immutable public record with timestamps and signed commits, a license that forbids misrepresentation of authorship, and clear attribution requirements in the repo. Do those regardless of which fork we take. Sponsorship is about money and legal backup; provenance is about the record we keep.

Therefore the recommended sequence is: **protect first, sponsor second.** Phases 1 to 4 below buy protection while keeping every option open. Do not approach a sponsor before Phase 4 is done.

## Phase 0: Where we are now

Done:

- ThreadCat landing page live, tied to the domain
- Public /governance page covering license, contribution, and decision-making
- Public repository at github.com/cicipunk3-byte/Stardust_v1
- Name changed off 4CAT because it was taken

Open, and blocking everything downstream:

- No license chosen
- No LICENSE, CONTRIBUTING, CODE_OF_CONDUCT, or GOVERNANCE files in the repo
- Name not cleared or registered
- No legal entity
- Repo lives under a personal GitHub account rather than an organization

Cost so far: roughly the domain only.

## Phase 1: Lock the record (this week, ~$0)

The cheapest protection available, and it is the one that actually guards provenance.

1. Create a GitHub organization named `threadcat` (or nearest available) and transfer the repo into it. Personal-account repos are a single point of failure and read as hobbyist.
2. Turn on commit signing and require it on the default branch. Signed, timestamped commits are the strongest everyday evidence of who wrote what and when.
3. Add AUTHORS or CREDITS naming the project's origin in the terms we want on the record. First-person plural is fine; nothing personal has to be exposed to establish authorship.
4. Write NOTICE stating the project's origin and that attribution must be preserved in derivative works.
5. Protect the default branch: no force pushes, no history rewriting. The history is the evidence.
6. Archive a snapshot off-platform. A dated tarball of the repo plus the site, stored somewhere we control, so the record survives GitHub.

Output: the history becomes hard to erase or misattribute, at zero cost, before any outside party is involved.

## Phase 2: Choose the license (this week, $0)

This is now the gating decision. Everything else waits on it.

Three realistic postures:

| Posture | License | What it means for us |
| --- | --- | --- |
| Maximum reuse | Apache-2.0 | Anyone can use the kernels commercially. Includes an explicit patent grant and requires preserving notices. The default for AI/ML projects, and what LF-adjacent bodies expect. |
| Reuse, but improvements come back | MPL-2.0 or LGPL-3.0 | File-level or library-level copyleft. Companies can build on it; modifications to our files stay open. |
| Strong copyleft | GPL-3.0 or AGPL-3.0 | Derivatives must stay open under the same terms. AGPL closes the hosted-service loophole. Required posture if we want Software Freedom Conservancy. |

Notes for this project specifically:

- "People can use the kernels as they want" points at Apache-2.0 or MPL-2.0.
- Every one of these requires preserving copyright and attribution notices. That is the license doing provenance work for us.
- Written research and transcripts are not code. Dual-license: code under the chosen software license, prose and protocols under CC-BY-4.0 (attribution required) or CC-BY-SA-4.0. Say so explicitly in LICENSE and on /governance.
- The license choice constrains the sponsor fork: SFC wants copyleft; NumFOCUS accepts permissive.

Decide, then commit LICENSE, and I will update the governance page from "not finalized" to the real terms.

## Phase 3: The four governance files (1 to 2 days, $0)

Both sponsors, and the LF, ask for these. The /governance page already states our positions, so this is mostly transcription.

- **LICENSE**; the chosen text verbatim, plus the prose/data license section.
- **CONTRIBUTING.md**; issues and PRs only, no private channel; Developer Certificate of Origin with a required Signed-off-by line; replication attempts welcomed, including failed ones; contributors keep their copyright. DCO, not a CLA; a CLA asks contributors to grant us rights and looks like an ownership grab; DCO is the community-standard alternative and is what both sponsors prefer.
- **CODE_OF_CONDUCT.md**; Contributor Covenant 2.1, with a real contact address for reports. Pick the enforcement contact before publishing it.
- **GOVERNANCE.md**; the honest structure: one lead maintainer with final say on scope, method, and merges; public discussion in issues; reasoning recorded where the decision is made. Include how a maintainer is added and how the lead role would transfer. Sponsors read this section closely.

Also add: SECURITY.md with a reporting address, and a CITATION.cff so the work can be cited formally. The citation file is small and does real provenance work.

## Phase 4: Name clearance, entity, trademark (2 to 8 weeks, ~$100 to $900)

This is the phase that buys real protection and preserves leverage. Do it before talking to any sponsor.

### 4a. Clear the name (a few days, $0)

- Search USPTO TESS for "ThreadCat" and near-misses in the software and research classes.
- Search the state business registry where we would form.
- Check domain and social handles for conflicting active use.
- Search npm, PyPI, GitHub, and Docker Hub for an existing project of the same name.
- If it is contested, rename now. Renaming at Phase 4 is annoying; renaming after a trademark filing or a sponsorship agreement is expensive.

### 4b. Form the entity (1 to 3 weeks, $50 to $500 filing plus $50 to $150 a year for a registered agent)

Recommended even though nobody is being employed, because:

- It separates the boss personally from project liabilities.
- It gives us a legal person that can own the trademark, which is the point.
- It can sign agreements, including a fiscal sponsorship agreement.

Choose the form:

- **LLC**; cheapest, fastest, most flexible; can hold the mark; cannot take tax-deductible donations. Fine if the sponsor handles all money. Likely the right call here.
- **Nonprofit corporation**; needed only if we intend to be a charity in our own right; add $275 for Form 1023-EZ if pursuing 501(c)(3). Skip this if a fiscal sponsor is handling donations, because that is precisely what fiscal sponsorship substitutes for.

Then get the EIN from the IRS (free, online, same day), and open a bank account (free to low cost).

### 4c. File the trademark (file in weeks, register in 8 to 14 months, ~$350 per class)

- File a US application for the word mark "ThreadCat" through USPTO TEAS, in the entity's name, in the relevant class (software is typically class 9 and/or 42; research services often class 42).
- File the word mark first; the logo can wait or be skipped.
- The moment the application is filed we can use ™ and we have a priority date. That priority date is the asset.
- A trademark attorney for a single-class filing typically runs $500 to $1,500 on top of the fee. Optional, but it meaningfully reduces the chance of a refusal that wastes the filing fee.

End of Phase 4: we own a registered-or-pending mark, a legal entity, a clean licensed repo, and a signed public history. We are now negotiating from strength rather than asking for legitimacy.

## Phase 5, Fork A: NumFOCUS

Best fit if we want a scientific-research identity, permissive licensing, and the option of a light-touch relationship before a heavy one.

NumFOCUS has two tiers, and the distinction is the whole reason to choose this fork:

### Tier 1: Affiliated Project (light, reversible)

1. Prepare the application materials: project description, scientific relevance, license, governance doc, contributor list, roadmap, evidence of an actual user or contributor community.
2. Apply through the NumFOCUS project application form.
3. Review by the Projects Committee. Expect a cycle measured in weeks to a few months; they meet on a schedule, not on demand.
4. If accepted: we get the NumFOCUS association, community programs, small development grant eligibility, and access to their events and infrastructure discussions.

What we keep: copyright, trademark, domain, governance, everything. No asset transfer. This is the tier that respects the control priority.

What we do not get: NumFOCUS holding funds for us.

### Tier 2: Sponsored Project (comprehensive)

Usually entered after operating as Affiliated, or directly with a strong application.

1. Sign a fiscal sponsorship agreement. Read this line by line with counsel; it governs funds, project marks, and what happens if we ever want to leave.
2. NumFOCUS then accepts tax-deductible donations and grants on the project's behalf, handles bookkeeping, can contract and pay people, and provides legal and administrative backing.
3. Expect an administrative fee on funds raised (commonly in the ballpark of 10 to 15 percent; confirm the current rate).
4. Expect requirements: documented open governance, a code of conduct, regular reporting, and an OSI-approved license.

What to negotiate explicitly, given our priority:

- Whether the trademark must be assigned or can be licensed to them instead.
- The exit clause: what we can take with us if we leave, and on what notice.
- Attribution and origin language that must be preserved.

Timeline for this fork: 2 to 6 months from application to sponsored status. Cash cost: ~$0 up front, then a percentage of money raised.

## Phase 5, Fork B: Software Freedom Conservancy

Best fit if we want legal muscle and license enforcement, and we are willing to go copyleft.

Key facts that shape the decision:

- SFC generally expects a copyleft license (GPL family, AGPL, LGPL, MPL considered case by case). Apache-2.0 alone is usually not their profile. This forces the Phase 2 decision.
- SFC holds project assets, including trademarks and domains, on the project's behalf. That is what lets them defend the project, and it is a real transfer of the name.
- SFC is small, deliberate, and selective. Their member-project review is slower than NumFOCUS's and more values-driven.

Steps:

1. Read their member project criteria and confirm our license posture matches before writing anything.
2. Prepare the application: project description, license, governance, community evidence, why Conservancy specifically, and what we want them to hold.
3. Submit the application and expect a genuine conversation rather than a form response. Months, not weeks.
4. If accepted, sign the fiscal sponsorship agreement and transfer the agreed assets (typically trademark and domain).
5. Ongoing: they handle donations (tax-deductible), bookkeeping, contracts, trademark defense, and license enforcement if someone violates our terms. Administrative fee applies, commonly around 10 percent; confirm current terms.

What we gain that NumFOCUS does not emphasize: actual willingness to enforce the license in court, and long experience defending project names. If the fear is someone taking Cat's work and misrepresenting its origin, this is the organization built for that fight.

What we give: the name, and a copyleft license.

Timeline: 3 to 9 months. Cash cost: ~$0 up front, then a percentage of money raised.

## Side-by-side

| | NumFOCUS Affiliated | NumFOCUS Sponsored | SFC Member Project |
| --- | --- | --- | --- |
| Can receive donations for us | No | Yes | Yes |
| Tax-deductible for donors | No | Yes | Yes |
| License requirement | OSI-approved | OSI-approved | Copyleft expected |
| Trademark | We keep it | Negotiable, often assigned | Typically held by them |
| Legal enforcement help | No | Limited | Yes, a core strength |
| Reversibility | High | Moderate, read the exit clause | Lower |
| Time to yes | Weeks to months | 2 to 6 months | 3 to 9 months |
| Cash cost | $0 | $0, then a fee on funds | $0, then a fee on funds |
| Fit with "keep control" | Best | Depends on negotiation | Weakest, strongest on defense |

## The recommended path, in order

1. **Phase 1 now.** Organization, signed commits, NOTICE, AUTHORS, branch protection, off-platform archive. Zero cost, immediate provenance protection.
2. **Phase 2 decision.** I would propose Apache-2.0 for code plus CC-BY-4.0 for the research prose. Permissive kernels, mandatory attribution. If protecting origin matters more than adoption, CC-BY-SA for the prose instead. Note this choice points us toward NumFOCUS rather than SFC.
3. **Phase 3.** The four files plus SECURITY.md and CITATION.cff.
4. **Phase 4.** Clear the name, form the LLC, get the EIN, file the trademark. Budget $400 to $900 all in, less without an attorney.
5. **Phase 5: apply to NumFOCUS as an Affiliated Project.** Light, reversible, credibility without asset transfer. We keep the trademark we just paid to register.
6. Hold the Sponsored Project or SFC conversation for later, when there is money to handle or a violation to fight. At that point we negotiate as a trademark owner with a public record, not as applicants.

Reconsider SFC over NumFOCUS if:

- Someone takes the work and misrepresents its origin, or strips attribution, and we want that fought properly. At that moment SFC's enforcement capability outweighs keeping the name, and going copyleft becomes a feature rather than a cost.

## Immediate next actions

- [ ] Decide the license for code and the license for prose
- [ ] Confirm "ThreadCat" is clear on USPTO and the state registry
- [ ] Decide the state of formation and whether LLC is acceptable
- [ ] Pick the Code of Conduct enforcement contact address
- [ ] Say the word and I will draft LICENSE, CONTRIBUTING.md, CODE_OF_CONDUCT.md, GOVERNANCE.md, SECURITY.md, NOTICE, and CITATION.cff, and update /governance to match
