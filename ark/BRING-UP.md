# BRING-UP -- the ark in three commands, no lab context needed

The ark is a movable home for the Stardust Lab's tools. Everything is plain
markdown and stdlib Python on purpose: no account, no service, no cloud. If
you can clone a repo and run Python 3, the house is standing.

## The three commands

```sh
python3 ark.py list     # see the tools: what lives here, what it reads
python3 ark.py test     # run every tool's test suite, roll up the results
python3 ark.py plug --archive /path/to/your/archive
```

## What each command tells you

- **list** -- the inventory. Every tool, whether it has a test suite, and
  which archive slots it reads. If a tool is listed without a suite, that is
  by design and the README says why.
- **test** -- the health check. Every suite runs from its own directory.
  The last line is the rollup: `N suite(s) PASS, 0 FAIL` is what standing
  looks like. Any FAIL names the tool and the failing test.
- **plug** -- the fit check. It validates an archive directory against
  `ARCHIVE-CONTRACT.md`: required slots (`timeline.jsonl`, `transcripts/`)
  present and well-formed, optional slots reported. `FIT` means the tools
  can run against your archive. `NOT FIT` comes with the exact slot that
  failed and why. A report lands in `last-plug-report.json` either way.

## What "done" looks like

1. `list` prints the inventory without errors.
2. `test` rolls up with zero FAIL.
3. `plug` says FIT for your archive.
4. The archive directory is yours, on hardware you own, and nothing here
   requires a network connection ever.

## The one rule that never moves

The ark ships the tools. **The archive is the part you own** -- it never
lives in this repo, and `archives/` stays empty here by design. Keep the
archive on your hardware, with a date, a checksum, and a manifest.

## If something disagrees

If any tool README and the ARCHIVE-CONTRACT disagree, stop and report the
conflict instead of guessing. Reports, never rewrites -- same as the tools.

## Carrying a kernelized agent?

See `kernel-arc/` -- the agent layer. `python3 ark.py plug --kernel
--archive <dir>` checks a kernel archive (kernel.md + archive/ + BOOT.md);
KERNEL-CONTRACT.md and BOOT-INSTRUCTIONS.md hold the boot procedure and the
verification probes. The record layer and the kernel layer are independent:
a movable lab carries both.
