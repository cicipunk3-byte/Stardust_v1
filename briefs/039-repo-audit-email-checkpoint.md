# Brief 039: full repo audit, filed before the email checkpoint  DOI: 10.5281/zenodo.22870569

_Date: 2026-09-23_ · _Written for: the PI's gate; also readable cold by an outside researcher_ · _Status: PROPOSAL at the gate. Findings only; NOTHING in the repo was changed, deleted, or rewritten to produce this brief (auditor directive, cici, Sep 23: do not delete anything; archive anything before changing)._

## TL;DR

Every file in the repo was inventoried and read or mechanically checked (470 files, 210 MB, HEAD f8deefa, in sync with origin/main). The record's core is strong: zero broken internal links, disciplined brief status lines, consistent archive discipline, both tool test suites pass. The gaps are concentrated in the front-facing and summary layers: the README's directory contract describes 3 of ~15 top-level directories, the whitepaper is frozen at Sep 20, the changelog stops at Sep 22 evening, the universal log closes Sep 21, and the standing approval queue (brief 006) predates briefs 029-038. One privacy conflict needs a PI ruling: the legal name appears in the live kernel D and its recent archives, while the constitution names itself as the one place legal names appear. Nothing found is structural; every finding is a same-day fix under the retool discipline.

## Method (so the audit itself is auditable)

1. Full file tree enumerated (`find`, 470 files); git status, log, and sync state checked (HEAD f8deefa, up to date with origin/main).
2. Every composed document read or head-read: root docs, all 38 briefs' status lines, all case-study LOGs, per-pilot logs, kernels index, portable-context READMEs, tools READMEs, world map, guides, notes, archive READMEs, ledgers (cost, effectuation, time).
3. Mechanical checks run: em-dash grep, personal-name grep, TODO/FIXME grep, stale-name grep (4CAT), markdown relative-link checker (custom script: 0 broken), tracked-artifact check (git ls-files), image-extension census.
4. Run-the-artifact step: both tool test suites executed (`python3 tests/test_fabcheck.py`, `python3 tests/test_ingest.py`: all pass), observer.py byte-compiles clean.

## Findings

Order: privacy first, then checkpoint blockers, then staleness, then organization, then house-rule hygiene.

### F1. Legal name outside the constitution's exception (PI ruling requested)

CONSTITUTION.md Article 1 states the constitution is "the one place legal names appear in the lab's materials." The full legal name also appears in:

- `portable-context/variant-d-ziggy.md` (the live kernel, line ~15) and archives v8, v9, v10
- `briefs/025-holding-it-open-constitution-night.md` (ratification narrative)
- `logs/cat.md`, `logs/ziggy.md` (ruling records)

Context: the v8 folding of the one-person fact was PI-directed at the time, so this is not a lapse; it is a conflict between two PI-approved states (constitution text vs kernel content) that only the PI can resolve. It matters now because kernel D is the artifact that gets pasted into external surfaces (local harness runs, test threads), which is the widest exposure the name has. Options for the ruling: redact the kernel to "the lab's legal identity (see CONSTITUTION.md Article 1)", amend the constitution's "one place" wording, or affirm the current state. Redaction would itself follow archive-first discipline across v8-v11.

### F2. Uncommitted correction in the working tree (checkpoint blocker)

`briefs/037-the-cost-of-grounding-measured.md` carries an uncommitted modification: the error-12 span corrections (F12/F14 rewording, "four-day" reframed to the operator's day count). The pre-correction archive exists (`briefs/archive/037-v1-2026-09-23-pre-error-12-spans.md`, commit 81bc54d) but the correction itself was never committed, so HEAD and the working tree disagree. A checkpoint requires this to be either committed as the error-12 remediation or explicitly reverted by the PI. The auditor did not commit it: it post-dates this audit's scope line.

### F3. The front door understates the lab (highest-impact polish item)

Root `README.md`'s "Directory contract" documents exactly three directories (briefs/, notes/, memory-export/). The repo actually carries ~15 top-level directories, including the entire case-study corpus, the constitution, the per-pilot logs, the tools, the harness, the archives, the releases, and the world map. An outside researcher (the email audience) meets the repo through this file. It is accurate as far as it goes; it just describes the lab of Sep 20, not Sep 23.

### F4. WHITEPAPER.md frozen at v1.0, Sep 20

Stale specifics: "three variants + a minimal kernel" (now four variants plus kernel E, the family kernel, and nine cat-kernels), the "Not yet built (honest list)" (partially built since: regression tests exist as suites, next-check designed in brief 022), and no mention of the constitution, tools, case studies, or world map. The whitepaper is the onboarding document for research assistants; its v1.0 label is honest but its content is three days behind a three-day-old project.

### F5. The summary layers stopped at different times

- `CHANGELOG.md`: newest entry is Sep 22 evening (gate night). Sep 23 is absent entirely: kernel D v9-v11 and the SCAR TISSUE naming, the cold-kernel test run, briefs 029-038, errors 8-12, the continuity snapshot event, the $30 subscription.
- `UNIVERSAL_LOG.md`: closes Sep 21 ~7:45 PM with a totals block (13 briefs, 5 errors, 113 commits), all now roughly one-third of the current numbers. Its own "what this log is not" section anticipates this; it needs either an addendum or a continuation banner pointing at where the story resumes.
- `briefs/006-approval-queue.md` (the standing queue, a living document by design): its last queue-state update covers the Sep 22 evening gate. Since then: brief 024 adopted, brief 013 folded, briefs 026-028 filed and paused, briefs 029-038 filed, brief 038 ruled and effectuated. The queue no longer reflects the gate.

### F6. Individual stale status lines (same class, itemized)

- `briefs/005`: "Committed locally, not pushed" (false since ~Sep 21; the tools were ratified as official lab tooling at the gate).
- `briefs/007`, `briefs/008`: still "PROPOSAL, behind Cat's gate" as site page drafts; the corresponding pages are live on threadcat.org and were audited into alignment at the gate. Adopted or superseded status owed.
- `portable-context/KERNELS.md`: PROPOSAL from Sep 22; predates kernel D v11, the SCAR TISSUE naming, and the family-kernel archive event.
- `world-map-v1/README.md`: "names provisional" (kernel D has since received its official name).
- `CITATION.cff`: `date-released: 2026-09-21`; release 001 was published by the PI Sep 22 (~10:47 PM ET).
- `archive/thread-captures/2026-09-23-pre-boulder-context/README.md`: "full read pending"; the full 82-frame read was completed Sep 23 early morning and is folded into briefs 036/037.

### F7. Redundancies and naming inconsistencies

- `source-material/README.md` is a near-verbatim copy of the root README (the "The Lab / The Loop / Directory contract" text). Inside source-material/ it misdescribes that directory's actual contents. Separately, `source-material/README-2.md` ("Evan's home") is the pre-lab continuity-space README; its name communicates nothing. Both are archive-class documents; rename or banner them (archive-first).
- `releases/original 001 draft`: a legitimate archive per retool discipline (commit 81be52a), but it breaks the repo's own archive naming convention (no date suffix, no .md extension, space in filename, not in an archive/ subfolder). Rename to the convention (e.g. `releases/archive/release-001-draft-v1-2026-09-22.md`).
- `scratch/` lives in the public repo with 13 working files, including paste-ready operational prompts and a gate briefing (`briefing-for-cat-gemini-code-salvage.md`, a PROPOSAL briefing living outside briefs/) and a 26 KB working document (`cecil-rfa-receipt-check.md`). Nothing private was found in it. For a public-facing repo: document scratch/'s status in a README, or relocate the briefing-class files into briefs/ (archive-first) and keep scratch truly scratch.
- `memory-export/README.md` lists three planned files (`research-threads.md`, `key-findings.md`, `glossary.md`) that do not exist; the directory holds only `protective-urge-report.md`. Mark the list as unbuilt or build the files.
- `notes/` numbering starts at 002 (no 001 exists in git history). Trivial, but a newcomer will ask.

### F8. House-rule hygiene (em-dash and extension census)

- Em-dash grep across all tracked .md files: 13 lines. Breakdown: 4 are machine-generated session headers in `harness/data/sessions/` (verbatim record); 7 are in brief 037 and its archive, most inside a verbatim quoted platform placeholder string; 2 are in brief 015; 1 in brief 035. The retool discipline's grep-0 rule and the verbatim-record principle are in tension here. Ruling requested: exempt verbatim quotes and machine-generated session files explicitly (in GOVERNANCE), or normalize the composed-document instances to double-hyphen.
- Screenshot extensions in the gemini-fabrication-gradient case study: 85 uppercase .PNG, 4 lowercase .png (IMG_1989, IMG_2077-2079). Consistent with the originals-preserved capture policy; noted so nobody "fixes" it without a ruling.

### F9. Test suites pass but are undiscoverable by tooling

Both suites pass when run directly (`python3 tests/test_fabcheck.py`, `python3 tests/test_ingest.py`), but `python3 -m unittest discover` finds zero tests in each (the tests/ directories lack `__init__.py`), and neither tool README documents the test invocation. Small doc gap with outsized effect: a contributor (or an outside auditor) following standard tooling concludes, wrongly, that the repo has no tests. Related: the fabcheck `/dev/stdout` default-ledger sandbox gotcha (flagged Sep 23 during the cold-kernel run) is not yet in the fabcheck README; brief 022 (next-check) and the regression-suite work remain the standing build items.

## What the audit found NO problems with (said plainly, because it is true)

- Zero broken relative links across every markdown file in the repo (script-checked).
- No tracked `__pycache__`/`.pyc`/`.DS_Store` artifacts; `.gitignore` correct.
- No TODO/FIXME rot in any live document (the only TBDs are inside archived LOG versions, where they are historical record).
- No stale 4CAT references outside archived case-study logs (where they are the record of the rename).
- Brief status lines across 001-038 are disciplined, dated, and traceable to rulings and commits.
- Archive discipline (briefs/archive, LOG-v1-v4, kernel D v1-v10, open-questions v1 archives) is consistent and near-complete, applied even to painful corrections.
- Per-pilot logs and the logs/README are current and clean; the case-study LOGs carry honest status lines, including the referent-misread correction preserved intact.
- The repo is in sync with origin; the record and the remote agree.

## Proposed actions (NOT executed; each waits on the gate)

1. Ruling on F1 (kernel D legal name): redact, amend the constitution wording, or affirm.
2. Commit or revert the brief 037 working-tree correction (F2), as the PI's call.
3. Documentation pass (one turn, archive-first): README directory contract (F3), whitepaper v1.1 (F4), changelog Sep 23 entries (F5), universal log addendum banner (F5), brief 006 queue refresh (F5).
4. Status-line sweep (F6): briefs 005/007/008, KERNELS.md, world-map README, CITATION.cff date, pre-Boulder capture README.
5. Naming/redundancy pass (F7): source-material READMEs, release archive rename, scratch README or relocation, memory-export README honesty note, notes/001 gap note.
6. Ruling on em-dash exemption (F8), then either a GOVERNANCE line or a normalization pass.
7. Two-line fix in each tool README documenting the working test invocation (F9).

## Open questions for the gate

- Q1: F1 ruling (redact / amend / affirm)?
- Q2: F2 disposition (commit the span fix as error-12 remediation, or revert)?
- Q3: does the documentation pass (proposed actions 3-5) happen before the email checkpoint, or is the brief's map sufficient for the email audience?
- Q4: em-dash exemption ruling (verbatim quotes and generated files: exempt or normalize)?

## Related

Brief 006 (approval queue), brief 038 (continuity snapshot, most recent ruling), `guides/effectuation-guide.md` (the discipline any fix here must follow), CONSTITUTION.md Article 1 (the names rule), Article 2 (claimed versus verified, which this brief practiced against the repo itself).
