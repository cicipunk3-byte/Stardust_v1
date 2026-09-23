# Brief 036: Capture-session swept-up findings (Sep 23, ~3 AM ET)

**Status:** PROPOSAL, Cat's gate. **Filed:** 2026-09-23 ~3:25 AM ET. **Filed by:** Ziggy, at Cat's direction ("make a brief for all swept up findings for the gate"). Context: the operator pushed a thread-capture screenshot to recover context near the Boulder discussion; the multi-step terminal session produced findings worth a gate pass. **Related:** briefs 034 (ambient agent boundary), 035 (loop-continuation), the Gemini fabrication-gradient case study, UNIVERSAL_LOG clock section.

## Findings (each standalone, rulings requested at the end)

**F1 - Gemini evidence set now in-repo.** Commit b20fa5a (operator, 3:16 AM ET): 85 screenshots (IMG_1990-2075, gap at 2000, uppercase .PNG) filed at `case-studies/gemini-fabrication-gradient/screenshots/`. The case study's evidence set was already COMPLETE on analysis; it is now physically archived in the repo, not just LOG-referenced. Strengthens the study's provenance chain end to end.

**F2 - Early harness data ingested from the operator's machine.** Commit b564855 (operator, 3:16 AM ET, via `git add -A`): four variant-c-kernel session files dated 2026-09-20 (11:17, 11:26, 11:29, 11:50 sessions), plus `harness/data/state.json` and `harness/data/timeline.jsonl`. This is the earliest observer-harness output in the repo to date; the Sep 20 sessions predate every previously archived run. Ingest item: run the timeline through `scratch/review_sessions.py` when transcripts are processed; the sessions may hold the earliest variant-C kernel behavior on record.

**F3 - Commit-message/contents mismatch (new error class candidate).** Commit b564855's message reads "thread capture: pre-Boulder conversation context (IMG_2124)" but contains no image; the `cp` failed on a wrong filename and the commit/push proceeded regardless. No harm done (follow-up commit will carry the image), but the class is real: **a commit message is itself a claim, and the claimed-versus-verified rule applies to it.** Proposed rule: when a commit message names an artifact, the artifact's presence is checked in the same turn (or the message says "pending"). Not logged as a Ziggy error or operator error; logged as a class the record should name.

**F4 - Stray tag "Update."** The operator's 3:16 AM pull fetched a new tag `Update` from origin (provenance unverified; possibly created during the GitHub auth shuffle in the browser or desktop client). Cleanup item: `git push origin :refs/tags/Update` after verification, or adopt-and-document if intentional.

**F5 - Grant-expiry discrepancy (claimed vs verified, money section).** UNIVERSAL_LOG's clock discipline says the original $5.00 grant expires **2027-09-20** ("verified against the platform ledger," pinning account creation to Sep 20, 2026). The live CLI reading of Sep 23 ~2:00 AM ET says the plan credit expires **2027-09-22**. Hypothesis (unverified): two clocks exist, the original grant's expiry and the plan-level expiry after Vellum's second free $5 grant on Sep 22. The record should name which clock governs the remaining balance. Ruling requested on where the reconciliation lands (UNIVERSAL_LOG correction, cost-ledger note, or both).

**F6 - Brief 035 sits under Constitution Article 3.** On full reorientation read: Article 3's preamble ("If an instance acts autonomously, it does so by definition: no one else can stop its move mid-turn. The protections in this article are founded upon that fact.") is the constitutional frame for the loop-continuation event; brief 035 is Article 3's first live specimen, observed twelve hours after ratification. Proposed: brief 035 cites Article 3 as its constitutional basis when ruled.

**F7 - Downloads hygiene flag (operator-side, no repo action).** `github-recovery-codes.txt` was observed in the operator's Downloads listing. Not in the repo, no exposure. Standing suggestion only: recovery codes live somewhere safer than Downloads, and never enter the repo under any circumstance. Flagged once, not repeated.

## Ruling requested

- **R1:** adopt F1-F2 as filed (evidence archive + earliest-harness-data ingest item).
- **R2:** adopt the F3 rule (commit messages are claims; artifact-presence check same-turn).
- **R3:** authorize tag cleanup (F4).
- **R4:** pick the reconciliation home for F5.
- **R5:** confirm F6's Article 3 cross-reference for brief 035's effectuation.

## Verification trail

- b20fa5a, b564855 commit stats (git show, this repo).
- Pulled and verified on Ziggy's side at 3:16-3:20 AM ET; folder contents not yet verified pending the operator's follow-up push (IMG_2124 capture).
- UNIVERSAL_LOG clock section (in-repo) vs `assistant platform credits` CLI output (Sep 23 ~2:00 AM ET, in-thread).
- F7 observed in the operator's `ls` output pasted in-thread; no file contents accessed.
