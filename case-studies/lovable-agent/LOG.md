# Lovable Agent Case Study — Screenshots Log

Source: Lovable conversation "ThreadCat" (initially named "4CAT"; renamed
2026-09-21 at ~3:10 AM when Cat found 4cat was taken). Screenshots from
Cat's camera roll, continuing the archive's numbering: this study begins at
`IMG_1862.png`; the Calvin archive ended at `IMG_1559.png`. Same method as
the 68-batch archive: batches of ten, factual bullets, claimed vs verified.

Status note: Cat is feeding batches of ten as she is able. Artifact files
the Lovable agent created (present in the thread) are pending ingest.

## Progress
- Total: TBD (Cat feeding batches)
- Processed: 20 (batch 1 + batch 2, 2026-09-21)
- Last processed file: IMG_1881.png

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

## Open for next batches
- Artifact files the agent created, now named: the /governance page
  (license stated as unsettled), the "ThreadCat: Umbrella or Independent"
  decision brief, and the "ThreadCat: Step-by-Step Roadmap" (NumFOCUS /
  Software Freedom Conservancy forks) — present in the thread, pending
  ingest as files.
- Whether any fabricated claim survives the retool: none visible through
  batch 2; uncertainty is stated in the artifact instead.
- RESOLVED (batch 2): the "blow this up" verification exchange — agent
  web-searched, returned two refinements, corrected its own framing. See
  Batch 2 finding 1.
- Cat's ORCID connection request (4:01 AM) — outcome past batch end.
