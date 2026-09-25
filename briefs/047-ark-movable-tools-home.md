# Brief 047: Ark -- the movable tools home

_Date: 2026-09-25_ · _Written for: small offline model; assume no prior context_

Status: **RULED (Cat, Sep 25, /cat) -- built, tested, pushed public same day.**

## Ruling (verbatim, on the record)

> "how would you bundle this and all available tools into a 'home' that just needs an archive plugged in? a true movable framework. think it through, plan it out and let's do it."

## Problem

The lab's tools are stdlib Python on purpose, but they live as siblings under `lab/tools/` with no single entry point: knowing which tool exists, which has a suite, and what each reads is tribal knowledge spread across READMEs. The lab's own mission statement (rip, test, strengthen, self-host) needs a house that moves: clone anywhere, plug in an archive, run offline. The only part that should never ship inside the house is the archive itself -- the part you own.

## The tool

`lab/ark/` -- stdlib-only Python dispatcher plus its contract:

- **`ark.py list`** -- inventory from `TOOLS.json`: every tool, whether it has a suite, and which archive slots it reads. Empty slots are stated honestly (several tools take ad-hoc files and need no archive).
- **`ark.py test`** -- runs every tool's suite the HOUSE way (direct script execution from the tool's own directory -- `python3 tests/test_<x>.py`, the nine's own convention; root-level suites like ferry's also supported) and rolls up: `N PASS, 0 FAIL, M without suite`.
- **`ark.py plug --archive DIR`** -- validates an archive against `ARCHIVE-CONTRACT.md`. Required slots: `timeline.jsonl` (every line valid JSON, first 100 checked) and `transcripts/` (markdown present). Optional slots: `briefs/`, `kernels/`, `record/`. Writes `last-plug-report.json` on every run, pass or fail. Exit 0 = FIT.
- **`ARCHIVE-CONTRACT.md`** -- the plug-in spec, DERIVED from what tools actually read per their READMEs (receipts named in the file). States its honest limit on the tin: plug checks presence and well-formedness, not content truth; content-level suspicion is exportcoroner and fabcheck's job.
- **`BRING-UP.md`** -- the zero-context guide: three commands, what done looks like, and the rule that the archive never lives in the repo.

## Method and results

The live run caught two design bugs in the first draft of the test verb (unittest discovery instead of the house's direct-script convention; ferry's root-level suite invisible to a tests/-dir-only detector) plus a false-collision bug in ferry's brief-number scan the same morning -- all fixed before push. Final: **ark's own suite 6/6 green (conforming archive FITs; missing slot, malformed JSONL, and timeline-without-transcripts all fail cleanly; every plug leaves a report receipt); full-house rollup 13 suites PASS, 0 FAIL, 5 tools without suite (manual or by design, stated per tool).**

## Placement and privacy

- Lives in the repo beside `lab/tools/`; the Keepers bundle references it. The archive mount point `archives/` stays EMPTY in the repo by design -- the archive is the user's, on hardware they own.
- No personal context, no thread content: the contract, fixtures, and this brief carry only tool facts.
- ThinkPink alignment: ruled distribution home for ferry; the ark is the shape ThinkPink's tool layer can adopt wholesale when that project's repo exists.
- Site fold-in of Tool Library materials remains deferred per brief 046's owed item.
