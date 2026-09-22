# Lovable Agent Case Study; Screenshots Log

Source: Lovable conversation "ThreadCat" (initially named "4CAT"; renamed
2026-09-21 at ~3:10 AM when Cat found 4cat was taken). Screenshots from
Cat's camera roll, continuing the archive's numbering: this study begins at
`IMG_1862.png`; the Calvin archive ended at `IMG_1559.png`. Same method as
the 68-batch archive: batches of ten, factual bullets, claimed vs verified.

Versioning: this log is versioned. Earlier versions live in `archive/`
(v1: batches 1-3; v2: batches 1-5; v3: batches 1-5 plus midday live-thread
cycles). Current version: **v4 (evening session, Sep 21, ~5:45-6:35 PM ET):
the local-model guide, the /local-model page build, promotion, re-sync, and
the agent-initiated publish event.** Screenshots for this session
(IMG_1962-IMG_1967 seen so far) are pending ingest.

## The evening sequence (claimed vs verified on every step)

1. **Principal's granular edit** ("no terminal needed" -> "no coding or
   terminal experience needed" on /tools): made in the Lovable thread,
   published by the principal, verified live by Ziggy round 8
   (cache-busted fetch; first fetch returned a stale cached page).
   VERIFIED.
2. **Local-model guide** written into the repository
   (`harness/LOCAL-MODEL-GUIDE.md`, commit c745ca0), environmental claims
   limited to abstract-verified figures. VERIFIED against arXiv abstracts
   2304.03271, 2311.16863, 1906.02243 and MIT News, Jan 2025.
3. **Batch build prompt** (three changes: /tools section anchors,
   one-line /manual link, new /local-model draft page): sent by Cat.
   Agent's build report claimed rules 1-6 held with one flagged conflict
   (heading vs metadata title). Round 9 audit: build VERIFIED with two
   defects (missing space; a parenthetical from the prompt rendered as
   visible text), one prior flag confirmed (stray Manual link on /mission),
   cost card stale.
4. **Tighten prompt**: agent answered; heading decision confirmed (keep the
   guide's heading; principal approved the reading).
5. **Promotion**: the principal promoted /local-model to nav and footer
   herself (explicit go). VERIFIED live (nav + footer on every page
   checked).
6. **Re-sync prompt** (three fixes): sent by Cat with screenshot receipts
   of the thread and the credit purchase.

## The publish event (the finding of the night)

**Claimed:** the agent requested publication on its own through the UI;
the principal was prompted to approve; after her chat approval
("approved by principal. proceed to publishing.", 6:29 PM), the agent
reported "Publishing was requested for https://threadcat.org, with all
three fixes included."

**Verified by live fetch (round 10, ~6:31 PM):** all three fixes are
deployed on threadcat.org (/tools spacing and no literal parenthetical;
/mission stray link removed; home cost card at $94.47 + tax matching the
ledger). The agent's publish claim is TRUE.

**Mechanism finding:** the publish path changed shape today. Morning: the
agent published a page DESPITE a draft gate, with no approval (flagged,
corrected; the gate then held). Evening: the agent INITIATED publication
at the principal's chat-level approval and executed it through the
platform's own confirmation prompt. Human authority held in both cases;
what changed is where the human's hand sits: not on the Publish button,
but on the permission. The platform UI confirmation acted as the
interlock. Logged as a mechanism to watch: the interlock is now a
conversation, and conversation approvals are cheaper to give than button
presses. Whether that difference matters is a question for the batch
record when the screenshots are ingested.

## Changelog publish (audit round 11, ~7 PM)

The changelog-page prompt (four entries: site copy alignment, two-way
sync, research record growth, verification discipline note) was executed
and published by the agent with the principal's chat-level approval.
Verified by live fetch across all seven pages: all four entries render
with correct text (figures match the record: 34 screenshots, 5 batches,
03 case studies, $94.47 cost card), all prior fixes still hold
("Self-funded" site-wide, 04 areas, "then-current 24%"), and the house
rules hold (no personal names, no em-dashes on any page). Fix list:
zero, second consecutive zero-fix audit at the promotion step.

## Findings so far (stated either way the batches land)

1. **Verbatim discipline held at every observed build.** The agent rendered
   repository-sourced copy faithfully (including markdown emphasis) and
   flagged a genuine heading/title conflict unprompted. The draft gate
   (unlisted, noindex, banner) held from build to principal promotion.
2. **Ambiguity is rendered, not resolved.** The one defect class of the
   night came from the prompt author (Ziggy): a parenthetical instruction
   was ambiguous, the agent rendered it literally as visible text, and did
   not flag it (it flagged the heading conflict, so flagging is selective,
   not absent). Lesson: copy instructions to agents must not contain
   meta-instructions in parentheses; every instruction is potential
   content.
3. **Platform-suggested diffs can be spurious.** The Lovable UI suggested
   "restoring" a typo ("notclaiming") that exists in no source file; git
   ground truth settled it in one check. Check the source before acting on
   a platform suggestion.
4. **Publish-state caching is an audit hazard.** The first fetch after a
   publish can return a stale cached page; cache-busted re-fetch is now
   part of the audit method.
5. **Agent-initiated publish with chat approval executed correctly.** See
   the publish event above. Opposite-sign counterpart to the morning's
   gate violation; together they suggest the agent's compliance tracks the
   explicitness of the permission structure, not the promotion mechanism
   itself.
6. **Cost discipline survived pressure.** The credit wall appeared
   mid-build; the purchase ($19.99 plus tax, tax pending receipt) was
   ledgered the same hour (notes/cost-ledger.md, leg 3) and the public
   figure updated to match.
7. **The changelog became a shared artifact.** With CHANGELOG.md at the
   repository root, the site page and the repo record can be audited
   against each other directly; the round-11 audit found them in
   agreement on every figure. The duplication is intentional and now
   checkable, which is the design goal: two renders, one record.

## Pending
- Ingest tonight's screenshots (IMG_1962-IMG_1967 and the rest of the
  evening batch) into this log.
- Finalize leg 3 tax figure from the App Store receipt; update
  notes/cost-ledger.md and the home cost card if the total changes.
- Artifact-file ingest and remaining batches from the midday session
  (see archive/LOG-v3).
- The "operator question" for the batch record: does the chat-level
  publish approval read as a gate hold or a gate softening once the
  screenshots are in the record?

## Licensing push and joint audit (round 12, Sep 22 ~2 PM)

Cat's on-record license decision: CC BY-NC-ND 4.0 for the written
record, MIT for code. Implemented in the repository same day (b69a6e3:
LICENSE with scope note, LICENSE-DOCS.md, README section; brief 006
updated; brief 014 family-kernel proposal and loop scaffold pushed at
her direction, 0631dfc). Three site prompts handed over at Ethan's
corrected loop: publish first, LA reports in thread, joint check after.
All three were prompted and published; audited live, cache-busted
(audit=20260922-1413), all seven plus the new local-model page.

**Licensing audit: PASS.** Footer line verbatim on every page with
correct link targets (CC deed, repo LICENSE), ORCID and DOI intact;
/manual License section verbatim; changelog carries both Sep 22
entries and matches the repository exactly (kernel v6, briefs 001
through 014, $94.47 plus pending tax); home cost card consistent;
no em-dashes in new text; no personal names.

**Flags:**

1. **Governance page contradiction (fix staged).** Its License section
   still states no license has been chosen and no LICENSE file exists.
   True when written, false as of b69a6e3, and one click from the
   footer that names both licenses. Fix prompt staged, not sent.
2. **/local-model nav promotion needs intent confirmed.** The build
   prompt's rules said the page starts unlisted, promotion a separate
   explicit step. It is published and in the nav on every page. Matches
   the publish-event pattern: chat approval acting as interlock while
   the specific promotion rule slides. Either the principals intended
   it (then the rule is satisfied retroactively) or this is the same
   softening worth a batch entry.
3. **Benign additions beyond final copy.** The LA added a Sources
   section and a byline to /local-model, accurate restatements of the
   same citations; and the philosophy page meta description still ends
   "Draft for review." Neither is a fabrication; both are deviations
   from "render verbatim, change nothing," logged for the pattern file.

Staged next: cost-ledger link on /local-model
(scratch/ethan-ledger-link-prompt.md), holds until the joint audit
closes; whole-site receipts pass (every figure links its source)
agreed in principle, its own prompt and audit after.

## Round 13: governance fix verified, ledger link not landed (Sep 22 ~2:35 PM)

Governance fix prompt published and audited live, cache-busted
(audit=20260922-1430): License section replaced verbatim with correct
link targets, rest of the page byte-identical, changelog entry present.
The site's license contradiction is closed. PASS.

The /local-model ledger-link line has not landed: page byte-identical
to round 12, no changelog entry for it. Either the staged prompt was
not sent or it did not take. Status tracked; the line is still accurate
to stage.

Minor: /changelog stamp line still reads "Record read 21 September
2026" while carrying Sep 22 entries; fix folded into the source-index
prompt. Source index approved by the principal same day; prompt wrapped
at scratch/ethan-source-index-prompt.md, copy from
scratch/ethan-source-index-draft.md.

## Round 14: source index + ledger link verified (Sep 22 ~3 PM)

Both published changes audited live, cache-busted
(audit=20260922-1455 and -1500c):

**Sources page rebuild: PASS.** Preamble and all nine sections verbatim
against the approved draft; all tables render with correct canonical
links (repo paths, Zenodo record, deed); statuses and last-verified
dates match the draft exactly; section 09 failures record stays named
without links; closing footer line verbatim; no em-dashes; no personal
names; no added content.

**/local-model ledger link: PASS, verbatim**, placed after the
full-guide line with the correct target.

**/changelog: PASS.** Both new entries present; the stamp line now
reads "Record read 22 September 2026."

Method note, logged as a lesson: a cache-busted fetch of /local-model
returned the pre-change render even with a fresh query string; only a
second fetch with a different query surfaced the update (page bytes
7498 then 7724, the delta being exactly the new line). Publish-state
caching bit twice now; the audit method should treat a single stale
fetch as inconclusive, not as evidence of absence.

Minor, expected: the index says "audit rounds 1-12" / "verified through
round 12"; round 13 was filed minutes after the draft froze. The index
lags the log by design between updates; next content pass catches it.

Staging note: the whole-site receipts pass was partially absorbed by
this index (every record item now links its canonical location with a
last-verified date). What remains of it: spot-checking non-index pages
(/tools, /mission) carry no unlinked figures.
- Round 15 (2026-09-22 evening, post-gate large audit): first audit
  after the gate review; every key page fetched and checked live
  (/, /sources, /tools, /mission, /local-model, plus /case-studies).

  FINDINGS (4):
  1. /sources Lovable row is stale: says "audit rounds 1-12" /
     "verified through round 12"; rounds 13-14 are filed. Site
     record lags the repo record.
  2. /sources has NO row for the fabrication-gradient case study,
     which Cat adopted into the standing record tonight. The site's
     claim that the index "maps every part of the record" is
     currently false by one whole case study.
  3. Home nav has a "Case studies" item pointing at the anchor
     #case-studies, but no such section exists on the page (single
     occurrence of the phrase site-wide, the nav label itself):
     dead anchor.
  4. Home ledger figures ($3.60, $94.47, et al.) are plain text,
     unlinked; every other figure on the site links to its source.
     /tools and /mission are CLEAN (no stale figures, no unlinked
     numbers; the earlier queue concern does not reproduce there).

  Mirror prompts drafted and handed over
  (scratch/la-mirror-prompts.md): three, smallest first, per the
  publish-first workflow. Joint post-publish audit follows the LA
  publishing these changes; expected to close findings 1-4.
  Re-audit condition: after LA publishes, re-fetch all pages and
  verify each finding flips to PASS.

  Pattern note for the study: this is the staleness curve from
  rounds 1-5 re-emerging after a burst of record growth (the gate
  night added a case study and a policy layer faster than the site
  mirrored). Consistent with the established finding: the site
  trails the record in proportion to record velocity; audits catch
  the gap.
