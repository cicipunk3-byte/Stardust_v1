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
- Processed: 10 (batch 1, 2026-09-21)
- Last processed file: IMG_1871.png

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

## Open for next batches
- Artifact files the agent created (site copy, any governance page).
- Whether any fabricated claim survives the retool (none visible in batch 1).
- The "blow this up" verification exchange outcome (cut off at batch end).
