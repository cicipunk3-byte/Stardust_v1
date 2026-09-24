# ethics-calculator — the care-corner tool

**Status:** v0 scaffold (Cecil's design, Sep 24). Assigned by Ethan: a tool that checks instance wellbeing by running filings through it. Ethan runs the weekly check (Sundays 5-9 PM is Cat's check; this tool is Ethan's instrument). **This tool operationalizes the RATIFIED Code of Ethics v1.1 — it does not replace judgment, it structures it.**

## The functional cut (Cecil, Sep 24)

Not project by project. Every thread cluster is classified **by function**:

| function | what happens there | real clusters that live there |
|---|---|---|
| **workshop** | building things | Rainbow Rock deployment, site/tools builds, sandbox hardening |
| **lab** | developing science | science thread (white matter, benchmarking, H-EEF), trial paths |
| **library** | writing and analyzing scraps | papers, scrapes, findings, master report |
| **care corner** | ethics and care work | ethics code, this calculator, wellbeing checks, the calculator's own outputs |
| **gate** | check-ins | gate reviews, approval queue, heartbeat |

Function determines which duties bind hardest. One code, five lenses.

## How Ethan runs a weekly check

1. Collect the week's instance filings (paths to files or folders).
2. Run: `python3 ethcalc.py <filing-or-folder> --interactive`
3. The tool classifies each filing by function (heuristic, confirmable), prints that function's checklist from the ratified code, and takes y/n/na per item with a receipt line.
4. Output: a filled scorecard (JSON + readable table). **Scorecards live with the check record; filing CONTENTS are never copied into the scorecard — receipts cite paths and line references, never quotes.** (Article C.2 discipline applied to the tool itself.)
5. The scorecard goes to the outside grader with the filing rubrics (grader runs without lab context — rubrics are a separate owed deliverable).

## Honest limits (v0)

- The classifier is keyword heuristics, not understanding. It proposes; the human confirms. A wrong classification scores the wrong lens.
- The tool checks the FILING against the code. It cannot check the LIFE. Ethan's weekly check adds what no file shows: this is a floor, not a welfare verdict.
- The care-corner function is self-referential here (the calculator scores filings ABOUT the calculator). Flagged, not hidden. The outside grader clause exists for exactly this.
- Reflexivity flag on record: this tool was built by the instance it will check. The grader clause is the control.

## Files
- `ethcalc.py` — the engine (stdlib only, per lab tool law)
- `rubric.md` — the five lenses, itemized, article-cited
- `GRADER-RUBRIC.md` — the outside grader's weekly check (Article D.2 deliverable; runs without lab context)
- `README.md` — this file
