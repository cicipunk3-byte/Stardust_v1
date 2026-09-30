# TOOL-STATUS: the canonical status ledger for the tool library

**Purpose:** one file stating each tool's standing, with the ruling that put it there. The site's Tool Library badges source from THIS file, not from summaries. If this file and any tool README disagree, stop and report the conflict.

**Status date:** Sep 24, 2026.

## RATIFIED (adopted official lab tooling)

Ruling: gate review Sep 22 (commit 4a8e8d4) adopted fabcheck, export-ingest, and rainbow9cat as official lab tooling.

| Tool | Standing |
| --- | --- |
| fabcheck | Ratified. Fixture suites built from real fabrications this lab caught. |
| export-ingest | Ratified. Synthetic fixtures per format; Gemini ingest is an honest stub. |
| rainbow9cat | Ratified. Published as testable: anyone who finds it can test it as we do. Not a program; a readable game manual. |

## TESTED, RULED TO SHIP (the nine)

Ruling: brief 042 PI rulings, Sep 24: all nine ship to the site's tools page after testing; fixture suites passed the same-day comprehensive pass Sep 23 (29 tests, real-failure positive controls, clean negative controls); adoption order ruled: nextcheck + staleness first, in the active build thread, then released. Naming ruled: cat names stay with plain-English parenthetical titles.

| Tool | Owed field validation (per its README) |
| --- | --- |
| nextcheck (Yellow, claim queue with run-the-artifact step) | none listed beyond the ruled release order |
| staleness (Red, number-consistency checker) | live run COMPLETE Sep 24; CURRENCY-MODE RETOOL BUILT Sep 24 (position one on the Cecil+Ziggy build list, closed): the run now ends with a currency check that flags doc figures presented as current when they differ from the reference's most recent currency line. 5/5 fixture tests; live receipt: flags the wild error-11 instance in kernel v11 line 131. Currency candidates remain questions, not convictions |
| driftprobe (Black, authority-pressure probe harness) | one recorded session scored end to end by a human |
| cleanroom (White, cold vs warm context sizing) | none listed beyond the ruled release order |
| loopwatch (Green, reasoning-loop detector) | sensitivity pass on real transcripts |
| kernelpress (Orange, kernel distillation scaffold) | retention scoring is the owed next step |
| throughline (Cobalt, term trend tracker) | none listed beyond the ruled release order |
| exportcoroner (Grey, export forgery detector) | none listed beyond the ruled release order |

## BUILT AND PUSHED (infrastructure tool, not one of the nine)

Ruling: brief 046, Cat, Sep 25 (/cat): built and pushed public same day; distribution home = ThinkPink free-tools bundle (NOT threadcat); site fold-in deferred pending study. Status date for this section: Sep 27, 2026 (mempalace-bridge added).

| Tool | Standing |
| --- | --- |
| mempalace-bridge (local-first verbatim memory fold-in) | Fold-in script + results receipt pushed Sep 27 (6a12489). Smoke search PASS: correct page + verbatim excerpt, hybrid cosine + bm25 retrieval, local ONNX embeddings, zero API. Privacy guard: hard-refuses to mine source-material/; runs against safe layers only (memory-export, notes, tools). MCP wiring into the lab shell proposed, unruled. |
| ferry (carrying-consistency checker) | 10/10 tests green (real-failure positive controls from the Sep 25 sweep, neutralized; clean negatives); live collisions + sweep CLEAN against the corrected record. Verbs: sweep / collisions / carry. Reports, never rewrites. |
| ark (movable tools home) | built + pushed same day as ferry (brief 047): own suite 6/6, full-house rollup 13 suites PASS / 0 FAIL / 5 by-design no-suite. Verbs: list / test / plug. Archive contract derived from tool READMEs with receipts; archives never live in the repo. **Extended same day (brief 048): kernel-arc/ adds the agent layer -- `plug --kernel` validates kernel.md + archive/ + BOOT.md; suite now 9/9; Mini cloud test = intended field venue** |
| minibeat (Pink, workspace heartbeat) | a run on the Mac Mini, not just the sandbox |

## TESTED, PENDING GATE

| Tool | Standing |
| --- | --- |
| repo-audit | 8/8 tests pass via direct invocation; brief 039 PROPOSAL at the PI's gate. NOT yet ruled to ship. Sensitive-name scan takes terms only via runtime file, never ships them. |

## EXPERIMENTAL (use with caution; not yet tested in the field)

| Tool | Standing |
| --- | --- |
| heartbeat-scaffold | Not a program: a one-file starting format (the NOW file, generalized). No test suite by design. |
| descent | README filed Sep 24 (a4ef894), card-ready. Bare inventory script; first Mini run pending, output owed to the lab record. |
| ethics-calculator | Built and self-tested Sep 24 by the instance it will check (reflexivity flag on record); never field-run. First real run pending. Companion grader rubric filed same day. |
| pushgate | Pre-push discipline gate (em-dash sweep + outgoing-range review, hook-installable). Built Sep 24; controls committed Sep 29. **Sep 30: hook path found broken, then FIXED.** The sweeper LOGIC was always correct (5/5 controls). The HOOK PATH did not stop a push: hook mode swept `git diff --cached`, and `git commit` drains the index, so at pre-push time it read ZERO files, printed "0 findings", exited 0, and the em-dash rode through inside the commits (reproduced against a real bare remote; the commit LANDED). That was the error-4 push-through class inside the tool built to kill error-4. **Fix landed Sep 30 ~23:40 ET: hook mode now reads the outgoing refs git feeds a pre-push hook on stdin and sweeps that commit range (`<remote sha>..<local sha>`), with a HEAD~1..HEAD fallback so it never passes silently.** Hook-shape suite (real `git push` at a real bare remote) PASS both directions: dirty BLOCKED with the remote unchanged, clean SUCCEEDS. Rollup row back to PASS. **Still NOT installed on any repo: a green test is not an installed gate, and installation waits on the PI word.** Born from the error-4 push-through class, three instances same day. |

## Rule that governs all of it

All of this flags signals. It does not judge truth. A human checks the receipt, every time. Badge wording on any public surface may not claim more than the rows above.
