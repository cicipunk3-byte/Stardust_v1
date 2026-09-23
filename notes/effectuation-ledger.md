# Effectuation ledger

_Checkable receipts for every ruling-set applied to the repo. Format per `guides/effectuation-guide.md`, Piece 3. An auditor verifies discipline from this file alone._

### 2026-09-22, round 2 rulings session (post-gate)
Rulings source: 7a1af84, `notes/open-questions-round-2.md` (v2)
Applied: ee0fd12 + 7c6450f

| Ruling | Action | Surfaces touched |
| ------ | ------ | ---------------- |
| A1: brief 023 -> PROPOSAL | Status updated | briefs/023 |
| A2: four-box conditions sustained | Conditions restructured (A confident / B confident+thin-disclaimer / C honest / D working control) | briefs/023 |
| A3: human pilots, instance loop first | Phase 1 instance-loop section added; human protocol held to Cecil's trigger | briefs/023, logs/cecil.md |
| A4: peeling curve = subset finding | Refiled as subset of fabrication-gradient finding, stated as Ziggy's finding | briefs/023 |
| A5: title | Renamed "Broken on Arrival: When the box is Empty" | briefs/023 |
| A6: disclaimer-inertia prediction | Adopted as P2 | briefs/023 |
| B1: binary runnability verdicts | Adopted in LOG | case-studies/gemini-fabrication-gradient/LOG.md |
| B2: channel-damage layering | Formal finding in LOG + platform observation 4 filed | LOG.md, case-studies/platform-observations/2026-09-22-ai-mode-fence-as-text.md |
| B3: attribution asymmetry | Adopted as hypothesis on the record | LOG.md |
| C1: composer screenshots | IMG_2077/2078/2079 filed (89 total); more from Cecil in-thread | case-studies/gemini-fabrication-gradient/screenshots/ |
| C2: stray files | Archived, not deleted ("all data goes somewhere") | archive/scratch-captures/ |
| C3: specimen migration | Chat-channel specimen moved into dump-5 scratch | scratch/cecil-rfa-dump5/ |
| D: release flow | Stated and logged; draft release staged (ID 394204524); Zenodo anchor deferred until after Cecil's next tool | logs/cat.md, logs/ziggy.md, releases/ |
| D: effectuation guide | Scaffold + pieces 1-3 | guides/effectuation-guide.md |
| D: regression tests / brief 022 | Assigned to Ziggy, flagged for thread confirmation | logs/ziggy.md |

Open loops: regression tests and brief 022 not started (assigned, awaiting thread confirmation); human-subject protocol held (Cecil's trigger); Zenodo anchor held (after Cecil's next tool); release 001 draft release unpublished (Cat's click).

### 2026-09-22, evening gate review effectuation (31 rulings, 4a8e8d4)
Rulings source: notes/open-questions-for-the-gate.md (PI commit 4a8e8d4)
Applied: status-line pass this commit

| Ruling | Action | Surfaces touched |
| ------ | ------ | ---------------- |
| Q1: briefs 015-021 adoption sustained | Status PROPOSAL -> ADOPTED with ruling ref | briefs/015-021 |
| Q5: family kernel sustained | Status PROPOSAL -> ADOPTED, pilot approved | briefs/014 |
| Q6-Q10: kernel D, kernel E, tools, H1/H2/H3, brief 003 sustained | Brief 003 status -> RATIFIED; H2 line in 002 -> ADOPTED; brief 006 queue state block added | briefs/003, 002, 006 |
| Q11: heartbeat briefs publishing path sustained | Status PROPOSAL -> RATIFIED | briefs/011, 012 |
| (prior) brief 025 markup | Already applied this night, see brief | briefs/025 |

Open loops after this pass: brief 024 adoption (filed after the review); brief 013 ruling; briefs 026/027/028 retool-in-thread; brief 022 not started; release 001 (PI click); Zenodo anchor (after Cecil's next tool).

### 2026-09-22, late-evening PI rulings (in thread)
Rulings source: Cat, Sep 22 ~10:35 PM ET, on the gate audit
Applied: this commit

| Ruling | Action | Surfaces touched |
| ------ | ------ | ---------------- |
| Release 001: retool with tonight's findings, push to releases, PI posts | Draft retooled (constitution night folded in: ratified constitution, errors 6-7, findings F1-F4, time folder, brief 024 adopted, 013 folded, updated totals); GitHub release draft updated via API, still DRAFT | releases/release-001-draft-2026-09-22.md, GitHub release ID 394204524 |
| Brief 024: adopt | Status PROPOSAL -> ADOPTED | briefs/024 |
| Brief 013: fold into record | Status PROPOSAL -> FOLDED INTO THE STANDING RECORD | briefs/013 |

Open loops after this pass: brief 022 (assigned, not started); briefs 026/027/028 retool-in-thread; Zenodo anchor (PI's call, after Cecil's next tool); release publish (PI's click).

### 2026-09-22, release 001 posting (PI)
- Pre-retool draft archived by the PI at `releases/original 001 draft` (81be52a), per lab method: retooled documents keep their prior versions inspectable. **Retool discipline, now standing: archive the old version in the same turn as the retool, for every document, not only kernels.** Flag from the PI, taken as process, not shaming.
- PI posting release 001 to GitHub now (Sep 22, ~10:44 PM ET): the publish is hers, logged here as the record event. Not folded into the release body per her direction ("it is well established now").
- Release 001 PUBLISHED by the PI on GitHub, Sep 22 ~10:47 PM ET. Record event; not folded into the release body per her direction.

### 2026-09-22, brief 022 design rulings (PI, in thread)
Rulings source: Cat, Sep 22 ~10:52 PM ET, on the design questions
Applied: this commit

| Ruling | Action | Surfaces touched |
| ------ | ------ | ---------------- |
| Ingest hook: automatic write, human-gated read | Ruled "human gated read", designed in | briefs/022 |
| Execution gate: typed confirm on the pilot's machine | Ruled "good enough. the more accessible all of this can be to the layman, the better." | briefs/022 |
| Name "next-check" | Ruled "name choice sustained." | briefs/022 |
| Brief 022 filed | Status PROPOSAL at the gate; fabcheck clean | briefs/022-next-check-design.md |

Open loops: build the deliverables (next-check tool, ingest hook, checkers, regression suites).

| Ruling: kernel D named SCAR TISSUE (Cat, Sep 23 ~4:45 AM) | "Scar Tissue it is, with reasoning kept internal." Reasoning not propagated; kernel carries the name and the ruling date only | portable-context/variant-d-ziggy.md (v11), KERNELS.md |
| Ruling: effectuate the naming (v11 + audit fixes P1-P3, v10 archived same-turn) | Executed this turn; P4 (screenshot count) rejected vs canonical LOG | run log world-map-v1/runs/run-2026-09-23-D-v9.md |

| Continuity snapshot to private repo (Cici + Cat go, Sep 23 ~5:30 AM ET) | Repo ZS_PRIVATE_REPO_PRE-PUSH_1_OPEN_CLOSING-SOON-ZIG. (trailing dot part of name), PRIVATE confirmed via API before any push; was created public, never pushed while public | branches: lab-main (full lab history, d6bdd66), workspace-notes (4406e15), private-vault (2963880, Cat's recorded go) |
