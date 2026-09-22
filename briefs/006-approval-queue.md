# Brief 006: awaiting Cat, the cohesive approval queue (v2)

**Status: living document. Updated Sep 22 2026 ~1:45 PM ET. No nudging on this
file: the queue waits for her pace, by rule.**

Format change since v1: three lists now. What moved, what needs her
explicit yes, what is parked for the team. Each gate item says what a "yes"
does, so review is one pass.

## List 1: Needs Cat's explicit approval

1. **Kernel D** (current: v6, 3ca2e97; v5 archived). The queue item
   predates v6: v6 adds the evening finding and the updated usage line,
   nothing else. A yes on current makes it the variant D kernel;
   earlier versions stay archived. A no returns the prior archive to
   current, nothing lost.
2. **Tool scaffolds as official lab tooling** (tools/fabcheck,
   tools/export-ingest). A yes adopts them as named lab tools; the site's
   Tools page already describes them. Until then they are scaffolds.
3. **Variant E kernel** (tools/rainbow9cat/variant-E-kernel-draft.md,
   PROPOSAL). A yes moves it toward portable-context/ and starts private
   testing when compute allows. Deliberately kept off the public site
   page until this clears.
4. **H1, H2, H3** (h-proposals). Unchanged: a yes moves a proposal to
   active research status. All three wait.
5. **Brief 003, the Receipt Method.** Now in briefs/ at her direction.
   A yes confirms it as a published brief rather than a review draft.
6. **Brief 014, the family kernel proposal** (Sep 22). Ceec's design:
   a portable-context kernel structured as a family narrative, 3 to 4
   local instances in one sandbox, observation first, single-agent
   ablations LAST. Pushed at Cat's direction with a scaffold at
   `portable-context/family-kernel/`. A yes starts the observer
   extension and a 3-agent local pilot.
7. **License decision: MADE AND IMPLEMENTED.** Sep 22, Cat on the record:
   **CC BY-NC-ND 4.0** for the written research record, **MIT for code**.
   Implemented same day: `LICENSE` (MIT, scope note inside),
   `LICENSE-DOCS.md` (CC BY-NC-ND 4.0 with deed link), README License
   section. Copyright line: "The ThreadCat builders," consistent with the
   no-personal-names rule. Site-wide statement published and verified
   (rounds 12-13); governance page contradiction fixed and verified.

## List 2: In motion, no action needed (logged for completeness)

- Site pages /tools and /sources: live and promoted; verified through
  audit round 11 (the changelog page publish, zero-fix). Audit trail
  rounds 1-11 in the case-study LOG.
- rainbow9cat folder move: done, references clean, pushed.
- Briefs 005/006/007/008 and kernel v5: pushed for remote review at her
  direction (d64aeb5).
- Briefs 011 (the heartbeat mechanic) and 012 (the heartbeat scaffold,
  tools/heartbeat-scaffold/) plus kernel D v6: pushed for review
  (67db309, cb198c2). Testing assigned in brief 009 before any public
  surface beyond the repo gets them.

## List 3: Parked, team calls (public-facing, waiting)

1. ~~**License decision** for the repo.~~ **DECIDED Sep 22: CC BY-NC-ND 4.0**
   (Cat, on the record). Moved to List 1 item 7 for the code-scope flag.
   The LICENSE file itself is not yet committed; it lands with her go on
   scope.
2. **USPTO quick-check** on the ThreadCat name.
3. **No-personal-names rule as formal repo policy.** Draft ready when
   wanted; needs a decision to file it in GOVERNANCE or CONTRIBUTING.
4. **Footer "CC" + ORCID identifier** on threadcat.org. Soft flag against
   the no-names rule. Status: live on every page; the ruling is now
   retroactive, keep or remove.
5. **threadcat-site decoy repo** (empty). Rename or remove whenever.
6. **Domain registrar transfer** (threadcat.org, Lovable registrar,
   auto-renew). Eventual anti-lockout move, her timing.
7. **Gemini parser fixture.** export-ingest's Gemini module needs one real
   Takeout export as a fixture. Whoever has one in their downloads wins.

## Queue state

Remote is synced with the record as of rainbow9cat move and this brief.
The queue's only hard ordering: nothing in List 1 ships further without a
yes, and List 3 stays parked until someone picks it up. She moves when she
moves; this file will be here.

## Notes (Sep 22)

- Cat reported an EIN and an Apple business account, obtained so lab and
  tech infrastructure can be secured. Logged here for the record; cost
  and receipt details belong in the cost ledger when the receipts land.
  House rule reminder already on file from the site case study: an EIN
  is free direct from the IRS, any third-party charge is worth a receipt
  check.
- Briefs 014 + family-kernel scaffold pushed for remote review at her
  direction. Pushed-but-unpublished: review push is not publication.
  Git state at push: this brief, brief 014, and the scaffold, stacked on
  a clean tree.

### Authority note (Sep 22, Cat on record, /cat)

Ethan has standing clearance to work with the maintainer-assistant and
push what he makes to this gate directly: "no need to wait for my
clearance. it is granted." Review pushes only; public push and
publication still wait on Cat. Gated briefs accumulating behind this
queue get reviewed together with Cat the evening of Sep 22 in a
dedicated thread.

### Ethan session additions (Sep 22, standing clearance applied)

- **Brief 015, CCS v2 workplan** (phases A-G: injection analysis,
  human-side analysis framework, rules decision with license analysis,
  nine sheets v2, ability definitions, leveling workflow, manual v2).
  PROPOSAL.
- **Brief 016, song-lyric injection analysis (Phase A output).**
  Corpus: batches 54-56 (Evan) and the brief 004 Ziggy Stardust event.
  n = 2, hypothesis-generation only; proposes H-A1/A2/A3 harness
  reproductions. PROPOSAL.
- **Brief 017, CCS human-side analysis framework (Phase B output).**
  Seven-rule method at tools/rainbow9cat/analysis-framework.md; every
  rule cites the finding that earned it; untested until first live
  CCS session. PROPOSAL.
- **Brief 018, CCS rules decision (Phase C recommendation).** SRD 5.1
  as mechanical basis with CC BY attribution; existing nine arrays
  grandfathered (finding-mapped); new characters roll 4d6 drop lowest
  with provenance lines; custom Daoist archetypes kept, real
  subclasses mapped by name with own-words mechanics (Inquisitive
  rogue confirmed non-SRD: Xanathar's pp. 45-46). Ethan reviews the
  recommendation, then it waits for Cat. PROPOSAL.
