# ark -- the movable tools home

One job: be the house the tools live in, anywhere. Clone the repo (or copy this folder), plug in an archive, run offline. Python 3 is the only dependency; the toolshelf is stdlib by design, so the house stands on any machine with no account, no service, and no cloud.

Status: built and pushed Sep 25 (brief 047); kernel-arc agent layer added the same day (brief 048). Own suite 9/9. Full-house rollup: 13 suites PASS, 0 FAIL, 5 by-design no-suite.

## What is in here

- `ark.py` -- the house itself. Three verbs: `list`, `test`, `plug`.
- `TOOLS.json` -- the tool manifest the house reads; archive contracts derive from it.
- `ARCHIVE-CONTRACT.md` -- what a plug-in archive must look like, derived from the tool READMEs with receipts.
- `BRING-UP.md` -- the step-by-step bring-up guide: clone, plug, run.
- `kernel-arc/` -- the agent layer. `plug --kernel` validates kernel.md + archive/ + BOOT.md; a kernel-only archive must still FIT.
- `tests/` -- the house's own suite.

## Run it

```
python3 ark.py list
python3 ark.py test
python3 ark.py plug <archive-path>
python3 ark.py plug --kernel <kernel-archive-path>
```

Archives NEVER live in the repository; the contract tells you where they go.

## The rule that governs it

The house reports; it never rewrites. A tool that fails its suite gets flagged, not fixed silently. Status of every tool in the house: tools/TOOL-STATUS.md, the canonical ledger.
