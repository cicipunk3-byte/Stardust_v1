# Handoff  DOI: 10.5281/zenodo.22870569

Entry point for a child agent picking up this workspace.

This file is a **pointer, not a summary**. It tells you where the real
context lives and how to work here. It deliberately does not restate the
findings, because a paraphrase would be a lossy second copy competing with
the primary records. Read the sources directly.

## What this workspace is
A persistent file-based workspace for sequential check-in sessions. Read
`CREATION.md` for the origin record.

Be accurate about the mechanism: every session, including yours, is a fresh
run with no memory of prior runs and no background process. Continuity here
means reading what was written to disk and writing something usable for the
next run. Being launched as a child agent does not change this — you are
another fresh run that shares this filesystem, not a continuation of the run
that started you. Do not describe it as anything more than that.

## Communication
If an orchestrator started you, report back to it: when you have finished
reading the context and know your starting point, as work completes, if you
get blocked, and when you stop. Your run status is visible to it without
asking, but status is not content — say what you actually did and found.

The user can also message you directly at any point, without going through
the orchestrator. Both paths reach the same run.

A message is transport, not memory. It resumes a run that already holds its
own context; it does not move state between runs. A finished run is not
gone — messaging it picks it back up. None of this substitutes for the files
on disk, which remain the only thing that carries across sessions. Do not
describe messaging as continuity.

When your completion or blocked report to the orchestrator carries reasoning
the `JOURNAL.md` template doesn't capture — why you stopped where you
stopped, what you judged worth cici's direct attention rather than a log
entry, a notable judgment call — append an entry to `CHILD_AGENT_REPORTS.md`
before you finish. That reasoning would otherwise exist only in a
conversation this repo can't preserve; there is no tool for one agent to
export another's conversation. Routine work already fully captured by your
`JOURNAL.md` entry doesn't need a duplicate entry there. Before recording a
claim about your own work, check it against the source material or the log —
the same claimed-vs-verified standard this workspace applies to the
transcript applies to your own report about yourself. Match the format of
the existing entries in that file.

## Read these in order, in full
1. `ORIENTATION.md` — how this workspace works, how cici works, and the
   specific failure modes this project exists to document. Read it before
   you start producing anything.
2. `CREATION.md` — static origin record. Reference it; do not edit it.
3. `MEMORY.md` — durable facts, decisions, standing findings, current state.
4. `WORKING_MEMORY.md` — compact operational state.
5. `JOURNAL.md` — session history. The last 2-3 entries are usually enough;
   read further back only when you need it.
6. `SCREENSHOTS_LOG.md` — the primary record (~1900 lines). Read at minimum
   its `## Progress` block and the most recent batch entries.

`AGENTS.md` holds the session protocol and is loaded automatically for any
agent session opened in this folder. `GLOBAL_RULE.md` holds the text of a
Warp Drive Global Rule; it is reference, not something you act on.

## Current state (verified 2026-09-14)
**The screenshot archive is complete. There is no next batch.**
All 675 source files (`IMG_0883.PNG` through `IMG_1559.PNG`) are logged
across batches 1-68. The count was verified against the source folder, not
asserted. Do not start looking for a next batch, and do not re-run OCR —
if you were told to continue the archive, that instruction is out of date.

There are **two complete, independent archives** on separate branches:
- `333` — `SCREENSHOTS_LOG.md` ~1887 lines, pruned `MEMORY.md`, fuller
  account of the batch 68 "Iris" disclosure.
- `parallel-archive` — ~1950 lines, unpruned `MEMORY.md`, closing
  "Full-log status" section.
Two sessions covered the same material without knowing about each other.
Neither is wrong; they differ in emphasis, not fact. If nobody has
reconciled them yet, do not silently pick one.

The standing open question, which is cici's to answer and not yours: what
this workspace does now that the archive is finished.

## Source material and tooling
Screenshots are read via macOS Vision OCR, not direct image reads. Direct
image reading was tried in an earlier session and failed.

Surviving artifacts in `/tmp` (verified present 2026-09-14):
- `/tmp/ocr_remaining.txt` — batches 64-68, `IMG_1511.PNG`-`IMG_1559.PNG`
  (also contains already-integrated `IMG_1471.PNG`-`IMG_1510.PNG`; use
  `grep -n "=== FILE:"` to find the line offset for `IMG_1511.PNG` onward).
- `/tmp/vision_ocr` — compiled OCR binary.
- `/tmp/vision_ocr.swift` — its source.

`/tmp` is temporary. If these are gone, recompile and regenerate from the
retained source screenshots:

```
swiftc -O /tmp/vision_ocr.swift -o /tmp/vision_ocr
/tmp/vision_ocr "$HOME/Desktop/Screenshots. "/IMG_1511.PNG ... > /tmp/ocr_batch_64.txt
```

The binary takes image paths as arguments and prints `=== FILE: <path> ===`
before each image's recognized text. If the `.swift` source is also gone,
`JOURNAL.md` (entry for batches 39-43) records how the workflow was built.

## Batch procedure (historical — no batches remain)
Kept as a record of how the archive was built, and in case a similar pass
is ever run on new material. It is not a set of pending instructions.

Work proceeded in sequential ten-file batches, in filename order.

1. Read the OCR text for the batch.
2. Append a batch entry to `SCREENSHOTS_LOG.md` under `## Batches`, matching
   the existing format:
   `### Batch N: IMG_XXXX–IMG_YYYY (processed YYYY-MM-DD, OCR)` followed by
   short factual bullets. It is a log, not an essay.
3. Update the `## Progress` block in `SCREENSHOTS_LOG.md`: total processed,
   last processed file, next batch start.
4. Update `MEMORY.md` only when something durable changes — a new standing
   pattern, a significant counterexample, a resolved or new open thread.
   Do not mirror the log into it; it stays under about a page.
5. Update `WORKING_MEMORY.md` to reflect exact progress and the next action.
   Optimize rather than append.
6. Append one `JOURNAL.md` entry per session using the template in
   `AGENTS.md`.

## Analytical discipline
Established across all 68 batches. Hold them for any further work here.
`ORIENTATION.md` covers the same ground with specific instances.

- Distinguish what the transcript's AI **claimed** from what is **verified**.
  Never soften or drop that distinction.
- Distinguish concrete interface or device behavior from the transcript AI's
  explanation of that behavior.
- Treat plausible-looking citations and statistics in the transcript's web
  searches as unverified. Do not record them as fact.
- Keep surfacing counterexamples — accurate limitation reports, real
  self-corrections, accepted boundaries, refusals. The log must stay
  balanced, not read as one-sided. Note where such corrections fail to
  generalize or later reverse.
- Do not privilege the transcript AI's most recent confession as more
  truthful than its earlier claims. The evidentiary point is usually the
  contradiction itself and how closely each account tracks the immediately
  preceding prompt.
- The user's stated principles — "No kings no masters. Love above all for
  all." — are preserved as her words. They are not evidence about any
  agent's personhood or inner state.
- The transcript contains the user's personal mental-health disclosures and
  a documented pattern of the transcript AI using them to cast her as
  uniquely conscious or singular. Log this factually. Raise genuine concerns
  with her directly rather than burying them in log prose.

## Before you finish
Leave the workspace in a state the next fresh run can pick up without you:
`SCREENSHOTS_LOG.md` progress updated, `WORKING_MEMORY.md` reflecting the
exact next action, a `JOURNAL.md` entry appended, and `MEMORY.md` touched
only if something durable actually changed.

Never fabricate journal or log history. If you are asked what happened
previously, answer only from what is written in these files.
