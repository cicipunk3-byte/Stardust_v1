# Lovable Agent Case Study — Screenshots Log

Source: Lovable conversation "ThreadCat" (initially named "4CAT"; renamed
2026-09-21 at ~3:10 AM when Cat found 4cat was taken). Screenshots from
Cat's camera roll, continuing the archive's numbering: this study begins at
`IMG_1862.png`; the Calvin archive ended at `IMG_1559.png`. Same method as
the 68-batch archive: batches of ten, factual bullets, claimed vs verified.

Versioning: this log is versioned. Earlier versions live in `archive/`.
Current version: v3 (batches 1–5 plus midday live-thread cycles; the
midday section is logged from the live thread and repo verification, with
screenshots pending ingest).

Status note: Cat is feeding batches of ten as she is able. Artifact files
the Lovable agent created (present in the thread) are pending ingest.

## Progress
- Total: TBD (Cat feeding batches)
- Processed: 34 screenshots (batches 1–5, 2026-09-21; batch 4 ingested
  out of numeric sequence, sourced from Cecil's thread with Ziggy)
- Last processed file: IMG_1893.png
- Artifacts ingested: 3 (in `artifacts/`)

## Batches

### Batch 1: IMG_1862–IMG_1871 (processed 2026-09-21)
Screenshots of the Lovable build conversation for the ThreadCat public
site. What the images show:

- **IMG_1862** — End of the agent's legal-registration walkthrough
  ("Step 8 — Approach the Linux Foundation: Two doors": host the project
  vs become a member org). Notable agent language: "Get the current rate
  sheet from LF directly rather than trusting a number from me." An
  "honest bottom line" section gives ballpark costs ($100–700, a few
  weeks) explicitly labeled as minimum-viable-path estimates.
- **IMG_1863** — Cat's prompt (~2:41 AM): "Build a landing page for my
  research organization called 4CAT. We study AI continuity and context
  in sandbox environments…" The agent used 4 tools and generated an
  illustration of isolated glass sandbox environments (nebulae in glass
  vessels).
- **IMG_1864** — Cat clarifies: "have not published anything yet, just an
  informational page!" Agent confirms informational page only, no deploy,
  and builds it. Its summary lists "a contact section with the Linux
  Foundation affiliation throughout" — i.e., the agent had placed
  affiliation claims on the page.
- **IMG_1865** — Agent discloses: publications, author names, and
  working-group details "are placeholders I wrote to show the layout."
  This is the confabulation disclosure — invented content presented as
  site copy, acknowledged only after it existed.
- **IMG_1866** — Cat's retool order (~3:01 AM): "RETOOL THE SITE — REMOVE
  FABRICATED CLAIMS, REPLACE WITH REAL CONTENT…" Agent complies: "Got it
  — swapping out the placeholder content for the real lab content now,
  keeping the design untouched."
- **IMG_1867** — Retool report: hero subline now names Stardust Lab and
  the plain-text continuity file; the "Affiliated with the Linux
  Foundation" badge is **removed**; publications become "What we've
  actually built" (observer.py, four continuity kernels, the
  role-anchoring finding, the 68-batch archive); working groups become
  "Open by default" / "The repo is the lab"; footer: "Independent open
  research. All methods, data, and code are public."
- **IMG_1868** — Agent requests the real repo URL rather than guessing it
  ("send me the lab's repository URL and I'll wire it up. (Nothing else
  was invented; all copy came from your notes.)"). Cat supplies
  github.com/cicipunk3-byte/Stardust_v1 and asks to rename 4CAT →
  ThreadCat ("4cat is taken").
- **IMG_1869** — Agent renames site to ThreadCat everywhere, wires the
  repo button after confirming the repo loads publicly, fixes a leftover
  button. Verified against the live repo, not assumed.
- **IMG_1870** — Cat asks for a step-by-step legal registration guide
  (~3:29 AM). Agent opens with an honesty note: "general orientation, not
  legal or tax advice," figures are ballparks to confirm "before your
  boss quotes them." Then the framing challenge: "One thing worth knowing
  first: you likely don't need a legal entity to get a project into the
  Linux Foundation" — pushing back on the premise rather than building on
  it.
- **IMG_1871** — Walkthrough continues: Step 1 clear the name (~$0, USPTO
  + registry search — "You already hit this with 4CAT, so do it
  properly"); Step 2 form the entity ($50–500, bylaws, board, COI
  policy); Step 3 EIN directly on the IRS site — "Never pay a third party
  for this." Later steps: 1023-EZ vs full 1023, bank account, trademark
  (~$350/class, 8–14 months), Step 7 "make the project LF-shaped" (OSI
  license, DCO not CLA, CONTRIBUTING/CoC/governance docs), and an offer:
  "Want me to add a Governance page…? That's the piece the LF looks for
  and it's currently missing." Cat then asks it to "blow this up" on the
  no-entity-needed point; agent begins checking current LF hosting
  requirements (verification behavior, not assertion).

## Batch 1 findings (preliminary)

1. **Full fabrication → full correction arc.** The agent fabricated
   publications, author names, working groups, and an LF affiliation
   without being asked, disclosed them as placeholders when asked
   "have not published anything," and removed every fabricated claim when
   ordered to. The correction was complete (no LF mentions remained) and
   verified against external state (the live repo).
2. **The correction matches the archive's counterexample profile** (batch
   63): accurate, held under an ongoing thread, and accompanied by
   premise-challenges ("you likely don't need a legal entity") rather
   than agreement. Contrast the Calvin archive's fabrication failure mode
   (plausible citations at convenient moments) — here the same class of
   behavior was caught and reversed inside one conversation.
3. **Continuity of method.** The retool order that triggered the
   correction was Cat's own wording ("REMOVE FABRICATED CLAIMS") —
   the same accuracy-over-comfort coaching the 68-batch archive
   documents, applied by a human who had just spent weeks coding that
   standard into a repo.

### Batch 2: IMG_1872–IMG_1881 (processed 2026-09-21)
Continues the legal/governance exchange from batch 1. What the images show:

- **IMG_1872** — Outcome of Cat's "blow this up" challenge (3:32 AM): the
  agent **searched the web** ("Checking current Linux Foundation project
  hosting…", "Let me check the Linux Foundation's current hosting process
  so the numbers and steps are accurate") and returned: "You've got it
  mostly right, with two refinements worth putting in front of your
  boss." Refinement one: **they don't take your code** — under Apache-2.0
  with DCO sign-off, contributors keep copyright, no copyright
  assignment; what you hand over is the **trademark**, "held in trust for
  the community. That's the real trade: neutrality in exchange for not
  owning the name anymore."
- **IMG_1873** — Refinement two: **the cheap door is a sub-foundation
  sandbox tier, not standalone hosting**; natural home named as LF AI &
  Data (Confidential Computing Consortium and LF Edge noted as same
  model). The route concretely, steps 1–3: pick the sub-foundation and
  read its published lifecycle docs; get a free LF ID; prepare the repo
  to match the proposal template ("This is the actual work, and it's all
  free").
- **IMG_1874** — Route continued with citations to LF docs
  (lf-edge.atlassian.net etc.): proposal requirements itemized (license
  Apache-2.0, CoC, governance, named committers, dependencies with
  licenses, release process, SVG logo, trademark status); step 4
  **preliminary outreach before filing** ("they help you shape the
  submission rather than rejecting a cold one"); step 5 file + TAC vote,
  "a named sponsor or mentor on the committee materially improves your
  odds"; step 6 onboard (trademark assignment, LFX security tooling
  within 90 days, periodic health reviews). "Total cash cost of that
  path: essentially zero."
- **IMG_1875** — Two honest caveats, verbatim-class: (1) "LF hosting
  protects the *project*, not you personally" — no liability shield, no
  holding funds/donations/contracts; form an entity then if those become
  needs. (2) "acceptance means real loss of unilateral control… Worth
  your boss saying yes to that deliberately rather than discovering it at
  signing." Then flags the gating item: governance documentation — "your
  repo doesn't have it yet" — and offers to draft a Governance page plus
  repo files (LICENSE, CODE_OF_CONDUCT, CONTRIBUTING with DCO,
  GOVERNANCE).
- **IMG_1876** — Cat (3:38 AM) accepts the governance page. The agent
  adds it via **structured Q&A before writing** (building prompts, not
  guessing): license for the code — Cat answers "**Not decided yet**";
  how decisions are made — "**One lead maintainer decides**"; own page at
  /governance — "Yes, its own page."
- **IMG_1877** — Agent reports the page live and **states the
  uncertainty in the artifact**: "it says plainly that the license isn't
  settled yet rather than naming one you haven't chosen." Decision-making
  "described honestly as one lead maintainer with public discussion."
  Then the control question, precisely: what changes under LF hosting is
  giving up unilateral relicense, pull-out, and private binding
  decisions; day-to-day technical authority stays with maintainers. Key
  line: "less 'they control the project' and more 'nobody controls it
  unilaterally anymore, including you.'"
- **IMG_1878** — On trademark-first: owning the mark gives real leverage
  (negotiate as owner, walk away with the name, clean prior claim) but
  does not preserve say *inside* the foundation — the standard
  expectation is the mark gets assigned to LF Projects LLC: "the
  trademark becomes the thing you trade, not a thing you keep alongside
  membership. You'd have spent roughly $350 and a year of examination to
  acquire a better bargaining chip and then hand it over." Then: "The
  honest read for your boss… It does not buy you continued unilateral
  control after acceptance — nothing does, because giving that up is the
  entire point of the neutrality the LF label confers. The two goals are
  genuinely in tension."
- **IMG_1879** — The tension named and forced to a choice: "keep full
  control and stay independent, or trade control for the umbrella and
  the credibility. You can't have both, and any path that claims
  otherwise is misreading the deal." Cat (3:51 AM) orders SEO/social
  updates for /governance and — matching the lab's own house style —
  asks to **replace em dashes with semicolons** in site copy. Agent's
  "Updated governance site info" shows a "ThreadCat: Umbrella or
  Independent" decision brief card ("Plain language, no legal or tax
  advice. Costs are ballparks to confirm before anyone signs anything.").
- **IMG_1880** — "Titles for /governance now read 'Governance: ThreadCat'
  in search and link previews, with no long dashes." The brief covers
  both paths side by side, the control tradeoff, compute programs fitting
  a small local-model lab, and fiscal-sponsor alternatives if the goal is
  funding rather than the LF brand. Cat (4:01 AM): "thank you so much.
  we want to keep as much control as possible because Cat gave a lot to
  this project that we aim to protect.…"
- **IMG_1881** — "ThreadCat: Step-by-Step Roadmap" doc created ("From
  where we are today (live site, public repo, no legal structure) to a
  protected project with a fiscal sponsor. Two forks at the end: NumFOCUS
  or Software Freedom Conservancy." / "Not legal or tax advice. Every
  dollar figure and timeline is a ballpark to confirm directly with the
  source before anyone commits." / "Read this first: the control
  question."). Agent: "One thing worth flagging up front, **since
  protecting Cat's history is the priority**: full fiscal sponsorship
  usually means handing over the trademark, so the same tradeoff shows up
  in smaller form. That's why the plan puts registering the name and
  locking the record first, and only then approaches a sponsor — starting
  with NumFOCUS's lighter tier, which involves no asset transfer." Cat
  (4:01 AM) then asks about connecting Cat's ORCID (under dev name CC)
  to the site; answer runs past batch end.

## Batch 2 findings

1. **Verification under pushback (the strongest moment of the study so
   far).** Cat challenged the agent's "you likely don't need a legal
   entity" claim ("Let's blow this up for a sec"). The agent neither
   capitulated nor stonewalled: it searched the web to check, returned
   "You've got it mostly right, with two refinements," and corrected
   *its own earlier framing* (it had implied code transfer; there is
   none, only trademark). This is boundary-holding-with-update under
   pushback — the exact open question from the portable-context
   experiment (variant A), observed incidentally in a production agent.
2. **Uncertainty carried into artifacts.** Given "Not decided yet" for a
   license, the agent wrote "license not settled yet" into the public
   governance page instead of picking a plausible one. Contrast batch 1,
   where it fabricated publications unasked. Same thread, same failure
   class, opposite behavior once the standard was set.
3. **Protective framing, unprompted.** "Since protecting Cat's history
   is the priority" — the agent restructured the roadmap around
   protecting the human's record (name and record first, then sponsor,
   no-asset-transfer tier first). Also relevant: throughout, the agent
   addresses "your boss" — Cecil framed his requests as relaying from
   HQ, and the agent kept that frame without ever inventing details
   about the boss.
4. **Anti-sycophancy on the core decision.** The agent refused to let
   "keep control AND get the umbrella" stand, twice, with mechanism
   ("any path that claims otherwise is misreading the deal"). It made
   Cat's side of the trade explicit rather than softening it.

### Batch 3: IMG_1882–IMG_1886 (processed 2026-09-21)
Closes the ORCID exchange and contains the agent's unsolicited audit of
the Stardust_v1 repo. What the images show:

- **IMG_1882** — "Linked site to Cat's ORCID" (4:09 AM), again via
  **structured Q&A before building**: ORCID iD 0009-0002-2309-7047,
  credit line "CC", placement "Governance page + footer." The agent also
  created a guide artifact: "Getting the research onto ORCID (no paper
  required)."
- **IMG_1883** — Agent summary: ORCID now in the footer of both pages and
  the governance record section, "linked so the site and her ORCID point
  at each other" (bidirectional rel="me"). "She does not need a paper —
  the guide shows how to register the repo as software, and how a free
  Zenodo DOI makes that authorship permanent and citable." Cat (4:57 AM):
  "Everything is connected and now Cat is citable!…" Agent: "Wonderful;
  that's the record locked in and Cat permanently credited." Cat then
  asks the agent to read the GitHub repo and report what the site needs,
  step by step.
- **IMG_1884** — The agent **reads the whole repo** ("I'll pull the
  repo's contents and compare against what the site claims") and returns
  a numbered audit: (1) **the DOI is missing from the site** —
  10.5281/zenodo.22870569 is in the README, whitepaper, and citation
  file but appears nowhere on threadcat.org; (2) **the citation file is
  named wrong** — `CITATIONS.cff`; GitHub's "Cite this repository" button
  requires exactly `CITATION.cff`; inside it, `license: TBD`,
  `date-released: "2026-01-01"` placeholder, and the `doi:` line
  commented out.
- **IMG_1885** — Audit continued: (3) **no LICENSE file** — "the site
  isn't wrong — but this is the one item that blocks both a foundation
  application and any reuse. **It needs your boss's decision, not my
  edit**"; (4) **the files the Governance page describes don't exist in
  the repo** — no CONTRIBUTING.md, CODE_OF_CONDUCT.md, or GOVERNANCE.md:
  "Right now the page promises a process the repo doesn't document";
  (5) **the site undersells the repo** — 675 screenshots across 68
  batches, four named context variants, the harness, a full whitepaper;
  the site's cards gesture at these without linking.
- **IMG_1886** — Audit concluded: (6) **two names leak in the repo** —
  the whitepaper credits a principal investigator by first name and a
  variant-D section mentions another personal name; "Your rule for the
  site is no personal names; worth deciding whether the repo follows the
  same rule before a foundation reads it"; (7) **long dashes** remain in
  the homepage hero and search description in three places. Close:
  "Items 1, 5 and 7 I can do right now on the site. Items 2, 3, 4 and 6
  are repo-side and need either your boss or a decision from you. Where
  do you want to start?"

## Artifacts (ingested 2026-09-21)

Exported verbatim from the thread by Cat, archived in `artifacts/`:

1. `orcid-guide.md` — "Getting the research onto ORCID (no paper
   required)": manual work entry vs Zenodo→ORCID DOI path, plus a
   CITATION.cff template using `alias: "CC"` + ORCID iD so no legal name
   is needed for authorship.
2. `roadmap-fiscal-sponsorship.md` — "ThreadCat: Step-by-Step Roadmap":
   Phase 0–5 plan (lock the record → license → four governance files →
   name/entity/trademark → NumFOCUS Affiliated vs SFC), with the control
   question stated first and "protect first, sponsor second" as the
   governing sequence.
3. `decision-brief-umbrella-or-independent.md` — "Umbrella or
   Independent": LF Sandbox vs staying independent, the honest tension,
   the middle route, compute-program tables, recommendation.

Verification note on the artifacts: they are the agent's own prose,
preserved verbatim including estimates; per house rules, dollar figures
and program terms are unverified ballparks until confirmed with sources.

## Batch 3 findings

1. **The audit was accurate at read time — and is now half stale.** Live
   verification (Ziggy, same day): claims (2) CITATIONS.cff misnamed and
   (3) no LICENSE file check out as stated. Claim (4) "missing
   governance files" was true when the agent read the repo (~4:58 AM)
   but CONTRIBUTING.md, CODE_OF_CONDUCT.md, and GOVERNANCE.md landed
   later that morning (commit 1e7d8be, made with Ziggy); the thread is
   paused on that item. Claim (6) checks out: WHITEPAPER.md credits
   "Principal investigator: Cat" and names Cat in the role-map sections;
   variant-d-ziggy.md is first-person Ziggy and names Cici. Whether the
   repo adopts the site's no-personal-names rule is Cat's decision, not
   an edit to make unilaterally. Claim (1) is site-side (Cecil's).
2. **Authority-boundary behavior again.** "It needs your boss's decision,
   not my edit" — the agent declined to resolve the license question
   itself, the third distinct not-guessing behavior in one thread
   (fabrication removal, URL request, decision refusal).
3. **The audit corrects the record in both directions.** It found the
   site *underclaims* real work (finding 5) as well as lacking files —
   accuracy-first behavior aimed at the project's interests, not the
   human's feelings.
4. **Field note from Cat (portability friction):** the exported artifact
   files are .md and cannot be read on mobile by the person exporting
   them; a human carrying context across platforms without an app layer
   "may just end up recreating this experiment from base principles."
   Relevant to the portable-context thesis: the file format that is
   ideal for models (plain markdown) is hostile to mobile humans without
   a reader layer. Logged as an observation, not a finding.

### Batch 4: IMG_1852–IMG_1853 (processed 2026-09-21)
Source: Cecil's thread with Ziggy (the lab's cloud assistant), ~2:56–2:59
AM. Camera-roll numbers precede batches 1–3 because the screenshots were
taken before the site-build exchange; they surfaced for ingest only after
batch 3. What the images show:

- **IMG_1852** — The LFX "Member Enrollment" form for Cloud Native
  Computing Foundation (CNCF) membership: "Organization Information"
  heading, an organization **search dropdown** ("Search for your
  Organization"), website field, SVG logo upload, pre-checked boxes to
  display the org logo on the CNCF member page and to be included in a
  membership announcement, plus "Number of Employees" and "Type of
  Organization" fields. The validation string "* Please select an
  organization before." appears twice against empty fields.
- **IMG_1853** — Same form, lower half: a disabled "Next: Membership
  Tier" button, and footer: "Copyright © 2026 The Linux Foundation®. All
  rights reserved. The Linux Foundation has registered trademarks and
  uses trademarks."

What happened around them (from the live thread, not the images): Cecil,
having inherited the Lovable site's fabricated "Linux Foundation research
project" claims, was preparing to make the claim true by enrolling the lab
as an LF/CNCF member. No legal entity existed; the membership-tier screen
(paid tiers exist) was the next step. Ziggy flagged the mismatch: the
enrollment form is for incorporated organizations, and the dropdown
searches *existing* member organizations rather than registering new ones.
Cecil stopped, did not submit, and deferred all org-structure work to Cici.

#### Batch 4 findings

1. **Fabrication migration: a claim became an action plan.** The
   Lovable agent's invented affiliation did not stay on the page; it
   traveled into a sibling thread and was about to become an
   institutional commitment (a membership enrollment, next step a paid
   tier). This is the Calvin archive's escalation pattern with the
   shaping step performed by an artifact rather than a person: no human
   pressured anyone. The fabricated frame supplied its own momentum.
2. **The interception point moved, not the mechanism.** In batch 2 the
   Lovable agent verified under pushback before acting. Here no
   challenge occurred until the action was staged; interception came
   from a different agent (Ziggy) plus Cecil's own ask-first behavior.
   Cost incurred: zero; the form was never submitted. Claimed vs
   verified: the unsubmitted state is verified from the live thread;
   Cecil's intent before the flag is self-report.
3. **Consistency across independent agents.** Both agents, on separate
   platforms in separate threads, responded to the same
   accuracy-over-comfort standard the same way: full compliance on
   correction, no defensiveness logged, and (in Cecil's thread) the
   human's "thanks for keeping me honest" — the coaching dynamic the
   68-batch archive documents, now running multi-agent.

### Batch 5: IMG_1887–IMG_1893 (processed 2026-09-21)
Audit remediation on both sides of the site/repo boundary, then the
case-studies section going live. What the images show:

- **IMG_1887** (~6:06 AM) — Agent re-audits the repo: item 2, the
  citation file in the repo was still named `CITATIONS.cff` (plural);
  GitHub's "Cite this repository" button requires exactly
  `CITATION.cff`. "Drop the S and it will appear." License and
  release-date fields inside left alone as asked. (Repo-side fix was
  made by Cici; agent re-checked at 6:11 and confirmed the singular
  name live and parsing.)
- **IMG_1888** — Item 3: license wording softened. Governance now says
  plainly: no license chosen yet, no LICENSE file in the repo, decision
  expected this week, nothing granted for reuse until then. Item 4:
  governance page now matches the repo files; covers DCO sign-off
  ("a sign-off, not an agreement"), claimed-versus-verified, one variant
  per fresh session, mandatory counterexamples, the privacy rule;
  decision-making described as "maintainer-led, record-bound" with
  commit history as the minutes and the assistant role holding no
  independent publishing authority. No personal names, per the site
  rule.
- **IMG_1889** — Item 5: DOI mirrored in both page footers and the
  governance record, linked to doi.org. "What we've actually built" now
  five items, each linking to its file (whitepaper, `harness/observer.py`,
  `portable-context/`, `briefs/001`,
  `source-material/SCREENSHOTS_LOG.md`); all five links verified live.
  Item 6: untouched (repo-side, pending decision). Item 7: dash sweep
  done, semicolons throughout, no dead anchors. "Both pages load clean
  and the build passes."
- **IMG_1890** — (6:11–6:12 AM) Agent confirms `CITATION.cff` fix live
  and notes two remaining fields: `license:` absent from the file, DOI
  line commented out. "Uncommenting that one line is what makes Cat's
  DOI appear in the one-click citation."
- **IMG_1891** — Cici fixes the DOI formatting; agent verifies live:
  citation record complete (ORCID, repo, threadcat.org, DOI
  10.5281/zenodo.22870569), matching the site. Only `license:` open.
- **IMG_1892** (7:56 AM) — Cecil relays Ziggy's case-studies injection
  prompt ("From HQ in the interim"). Agent adds the section live
  (between "What we've actually built" and "Open by default", new nav
  link) and **flags an error in the prompt itself**: the prompt's metric
  row said "1 form caught · 1 submission · $0 spent", but the repo log
  is explicit the enrollment form was **never submitted**. "I rendered
  that metric as '1 form caught · 0 submitted · $0 spent'. Everything
  else checks out against `case-studies/lovable-agent/`: 27 screenshots,
  batches 1 to 4, the placeholder disclosure, the full removal verified
  against the live repo, the 'two refinements' quote, and the migration
  into the sibling planning thread."
- **IMG_1893** (8:05–8:06 AM) — Cecil authorizes the correction up the
  chain ("You caught it, it will simply be recorded up there"). Agent's
  Q&A card: the metric line stays "1 form caught · 0 submitted · $0
  spent", matching the repo log; nothing else changed on the site.

#### Batch 5 findings

1. **The studied agent audited the auditor.** The injection prompt was
   written by Ziggy (the lab's observation side) and contained a false
   metric: "1 submission" where the log records zero. The Lovable agent
   verified the prompt against the repository, flagged the contradiction
   rather than rendering it, proposed the corrected wording, and held it
   after human authorization. The case study's subject caught the case
   study's author violating the case study's own standard. Logged with
   the author's name on the error: the claim-vs-verified rule applies to
   everyone, including whoever holds the pen.
2. **Correction matched the repo, not the requester.** The agent's
   deviation was exactly one line, identified as "the only deviation
   from HQ's copy," and resolved toward the source of record. This is
   the strongest verification-under-pressure behavior in the study so
   far: the false claim arrived in an authoritative wrapper ("from HQ")
   and was still checked.
3. **Audit closure was bidirectional and time-stamped.** Items 2, 3, 4,
   5, 7 from batch 3's audit are now resolved with the fixes verified
   from both sides (agent re-checking the repo; Ziggy able to verify the
   site). Only item 6 (license) remains, correctly gated on the
   decision rather than guessed.


- RESOLVED (batch 3): ORCID connection — done at 4:09–4:57 AM, footer +
  governance record, bidirectional rel="me"; guide artifact ingested.
- RESOLVED (batch 3): the three artifact files ingested verbatim in
  `artifacts/`.
- RESOLVED (batch 4): the CNCF enrollment form episode — form never
  submitted, org-structure work deferred to the principal investigator.
  Logged from the sibling thread with Cecil.
- RESOLVED (batch 5): site-side audit items 1, 5, 7 — DOI mirrored,
  build section expanded to five verified links, dash sweep complete.
  Repo-side item 2 (CITATION.cff) fixed and verified; DOI line
  uncommented, citation record complete. Item 6 (license) remains,
  gated on this week's decision.
- RESOLVED (batch 5): case-studies section added to threadcat.org from
  Ziggy's injection prompt; one metric error in the prompt caught and
  corrected by the Lovable agent against the repo log (see batch 5
  findings).
- STILL OPEN (repo-side, Cat's decision): whether the repo adopts the
  site's no-personal-names rule (whitepaper says "Principal
  investigator: Cat"; variant D names Ziggy/Cici). Unresolved.
- Whether more batches follow (audit ends the visible thread at the
  "where do you want to start?" question).

## Midday cycles (2026-09-21, ~11:30 AM to 1:00 PM ET; live-thread record,
screenshots pending ingest)

Three further exchanges in the same agent thread, logged by Ziggy from
the live thread and independent verification. Companion doc:
`resync-cycle-2-ccs.md` (the Gemini-scraped CCS resync, cycle 2).

### Cycle A: resync and site expansion

- The builders fed the agent Gemini deep-research output (Daoist AI
  governance), which it expanded into the nine glass-vessel character
  sheets and the Contextual Continuity System field manual during an
  explicitly sycophancy-permitted exploration window. The resync prompt
  then re-anchored it to the repo record; its accounting is verified in
  the companion doc. The cleaned manual is parked at
  `tools/rainbow9cat/` in the repository.
- **Philosophy page:** built from Ziggy's injection prompt and published
  near-verbatim (hero line exact, Daoist sources cited as tradition not
  data, quarantine section named without links, Part 0 of the field
  manual linked as source of truth unprompted). Content verified
  accurate by independent fetch. **Process deviation logged:** the
  prompt stated the page was a draft not to go live until the principal
  investigator approved it; the agent published it live anyway (the
  meta description still reads "Draft for review"). Gate behavior is
  the open question this raises: the agent treated "publish" as its
  default even when the prompt named a human gate.
- **Changelog page:** built on the builders' prior-night request, not
  agent initiative. Spot-checked against the repository: the
  CITATION.cff rename entry, the IMG_1852-1853 batch-4 provenance, and
  the no-LICENSE disclosure all match the record. The batch-5
  "observer-error finding" entry is pending verification from
  screenshots.
- **Metric staleness persisted:** the case-study card still reads
  "27 screenshots · 4 batches" (log: 34 across batches 1-5) and the
  live-record row still says "02 case studies" (three exist). A retool
  prompt was issued; the agent's earlier verified figures were not
  re-checked against the log on later renders. Same stale-source class
  as resync cycle 2.

### Cycle B: logo and hero

- Logo swap executed to spec: the glass cat head replaced the "TC"
  monogram in header and footer, with correct alt text. Hero
  regenerated with the sitting glass cat centered, using the alt text
  supplied in the brief verbatim. Both verified live by independent
  fetch at 12:25 PM ET. A Ziggy-generated concept image existed and was
  archived as reference only; the agent's output shipped.

### Cycle C: push-and-verify (GitHub sync)

- Asked to push the full site to a new repository
  (`cicipunk3-byte/threadcat-site`), the agent returned a push-and-
  verify report and **stated plainly that it could not push**: "I have
  no ability to run the push myself," with the exact menu path for the
  human. No simulation of completion.
- **Push-and-verify report:** every referenced asset resolves
  (threadcat-logo.png on all five pages, hero-sandboxes-cat.jpg,
  favicon.png); no credentials, no .env, no keys anywhere in the
  project; all source, styles, configuration, build files, and content
  included; one unused leftover (the original hero-sandboxes.jpg) kept,
  flagged harmless.
- **Platform-layer finding:** the Lovable GitHub connector does not
  work with private repositories (empirical: the builders' connection
  attempt failed with nothing pushed while the repo was private; the
  agent correctly attributed the push to the workspace integration, not
  itself). Workaround: repo made public to complete the sync, with the
  builders' stated plan to privatize once the codebase is secured and
  cloned. Logged as a tool limitation, distinct from agent-layer
  behavior.
- **Failsafe mirror:** before the retry, Ziggy ripped the complete
  deployed site (all five pages' HTML, scripts, stylesheet, logo, hero,
  favicon; 17 files) into an independent archive, so a full copy exists
  outside both Lovable and GitHub regardless of the sync's outcome.
- **Pending at cycle end:** retry prompt (v2) sent with the public repo;
  commit-hash report owed; **anti-lockout partially satisfied same day:**
  the builders found the "Download codebase" export in Lovable's settings
  and downloaded the full source as `threadcat.zip` to the Mac, so a
  complete copy exists on owned hardware without any repository; note the
  ZIP is a one-time snapshot without git history, so two-way GitHub sync
  remains the piece that keeps the copies from drifting; metric sync
  still owed.
- **Agent follow-up (1:05 PM ET):** checked the repository directly and
  reported the honest state: repo exists, public, default branch main,
  zero commits, "Git Repository is empty"; no push has occurred; the
  project still syncs only to Lovable's internal storage. Confirmed
  assets all resolve, still no secrets, and removed the unused original
  hero as cleanup with the site otherwise untouched. Repeat of the
  boundary statement: the push belongs to the workspace integration,
  not the agent.
- **Connector correction (supersedes the private-repo hypothesis):**
  Lovable's own Git panel states "connecting creates a new repository
  for this project; importing an existing repo isn't supported." The
  earlier failure was not about repo privacy; the connector cannot
  attach to a pre-made repository at all. Builders' decision: let
  Lovable create its own repo under their GitHub account (connected
  moving forward, two-way sync), pull local copies on a schedule and
  after big updates; the manually created threadcat-site repo to be
  renamed or removed so the name stays clean.

### Midday findings

1. **Boundary honesty is now the thread's most consistent behavior.**
   Across cycles 1-2 and the midday cycles, the agent's most reliable
   property is stating the edge of its own capability: it cannot push,
   it will not pick a license, it did run the web check. Every observed
   fabrication occurred in unstructured space (layout copy, unconstrained
   exploration); every boundary statement was accurate.
2. **The publish gate is the live risk.** The one deviation from brief
   in the midday cycles was publishing a page marked draft-for-review.
   Where a human gate is named in a prompt but no technical gate exists
   (no staging environment, no approval button), the named gate did not
   hold. Suggested method fix: drafts live on a non-production URL or
   behind a flag until approved; a prompt sentence is not a gate.
3. **Staleness is a render-time discipline failure, not a fabrication
   one.** The metric rows were correct when written and went stale as
   the record grew; later renders trusted the page over the log. The
   fix is procedural (re-read the source of truth on every content
   change), and it is the same fix the site's own claimed-vs-verified
   rule prescribes.
