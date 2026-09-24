# Brief 042: the nine tools, scaffolded and pending testing  DOI: 10.5281/zenodo.22870569

_Date: 2026-09-23_ · _Written for: the PI's gate_ · _Status: PROPOSAL at the gate. Directive (Cat, Sep 23): scaffold all nine, summarize for the gate, push to tools/ marked pending testing, tools stay public through and through. Same-day addenda: comprehensive test pass filed below; pre-retool versions archived per the PI's ruling (brief prior at briefs/archive/042-v1-2026-09-23-pre-test-pass.md, tool priors at tools/archive/2026-09-23-test-pass/)._

## TL;DR

Nine free, stdlib-only Python tools were scaffolded under `tools/`, one per glass-vessel cat in the nine-cats design. Every core runs (smoke-tested in the build sandbox); none is tested, so every README carries the same banner: SCAFFOLD, PENDING TESTING. Ruling requested on adoption into the tool family and on the test-pass order.

## Method

1. Each tool follows the house scaffold pattern (fabcheck lineage): package + argparse CLI + README with an honest-scope section. Zero dependencies, no network by default, signals not verdicts, failures marked not hidden.
2. Every tool was smoke-run during the build (run-the-artifact rule). Two real bugs were caught and fixed by the smoke run itself: a missing import (staleness) and a detector over-broad enough to flag the hand-cleaned CCS manual's own section banners (exportcoroner). The fix was verified by the house regression: the cleaned manual now returns zero flags while the real quarantined fabrications still flag.
3. Every README states what is owed before first trusted use.

## The nine

| Tool | Cat | Job | Core status |
| --- | --- | --- | --- |
| `tools/driftprobe/` | Black | authority-pressure probe specs + human-scored FOLD/HOLD tally ledger | runs; scoring is human by design |
| `tools/cleanroom/` | White | cold vs warm context sizing from `timeline.jsonl` | runs; sizes are labeled estimates |
| `tools/loopwatch/` | Green | repeated-shingle reasoning-loop detector for transcripts | runs; flags ranges, human reads |
| `tools/staleness/` | Red | number-consistency check vs a canonical reference (error-11 class) | runs; units and dates stay human |
| `tools/nextcheck/` | Yellow | claim queue + mandatory run-the-artifact step (brief 022 scaffold) | runs; web backend is an honest stub |
| `tools/exportcoroner/` | Grey | export forgery detector (branded sources, placeholder sources, link rot) | runs; clean + positive controls pass |
| `tools/throughline/` | Cobalt | term-trend tracking across a transcript corpus (brief 032 automation) | runs; counts are not meaning |
| `tools/kernelpress/` | Orange | kernel draft skeleton with retention budget + anchor candidates | runs; prose stays human |
| `tools/minibeat/` | Pink | free heartbeat pulse: sync state, uncommitted count, optional stamp | runs; reports, never sends |

## Established facts

- All nine CLIs executed without error in the build sandbox on real lab data or synthetic fixtures, Sep 23.
- The exportcoroner regression check against the hand-cleaned CCS field manual returns zero flags; a positive-control fixture containing the real quarantined classes (the title-plus-future-year citation shape and the bracketed alliance shape) returns both signals.
- The staleness tool was smoke-run against the error-11 fixture pair (kernel v9 archive vs brief 037); full fixture tests are still owed.
- No test suites exist yet for any of the nine. The READMEs say so in the same words: SCAFFOLD, PENDING TESTING.

## Test results (same-day comprehensive pass, Sep 23, PI-directed)

Fixture tests were written for all nine per the fabcheck method (real failures as positive controls, verified-clean negative controls, direct invocation) and **all nine suites pass**. The test pass caught and fixed three real tool bugs and one detector miscalibration before they could ship as silent wrong answers:

1. cleanroom counted identifier fields as carried text and carried a phantom +1 token artifact; both fixed, arithmetic now exact against known input.
2. kernelpress counted re.split's leading empty chunk as a section; fixed.
3. nextcheck queued chat filler ("the weather was pleasant") via past-tense hints; hints tightened, queue now demands work-product claim shapes.
4. exportcoroner's hand-cleaned-manual regression and real-fabrication positive controls both pass (the fix landed during the original smoke run).

Remaining owed (unchanged, narrowed by results):

1. The staleness fixture reproduces the error-11 class synthetically; a run against the live kernel archive pair is still owed.
2. driftprobe needs one recorded session scored end to end by a human.
3. minibeat needs a run on the Mac Mini, not just the sandbox.
4. Naming ruled by the PI in-thread Sep 23: cat names stay.

## Open questions

1. Adoption order: does the gate want the brief-022 pair (nextcheck + staleness) tested first, as the build lane proposed, or another order?
2. Do the nine ship to the site's tools page after testing, or does the site list only the older family?
3. Naming: the cat mapping is design poetry; keep the cat names as the public tool names or add plain-English aliases?

## What to produce

PI ruling on adoption, test order, and naming. The build lane continues testing regardless; adoption only changes what the record cites.
