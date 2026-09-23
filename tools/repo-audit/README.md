# repoaudit; the repo audit ritual, machined  DOI: 10.5281/zenodo.22870569

Free, local, stdlib-only Python. Part of the ThreadCat lab tooling.
Status: PROPOSAL at the PI's gate (filed with brief 039, Sep 23).

## What it is

The full-repo audit we ran by hand on Sep 23 (brief 039), turned into a
tool. It inventories the repo, checks git cleanliness and sync, and runs
the mechanical signal scans: em-dashes, TODO markers, broken relative
links, committed artifacts, caller-supplied sensitive-name terms, a
brief status-line sweep, and the run-the-artifact step (it executes the
other tools' test suites).

## Honest scope (read this first)

- **Signals, not verdicts.** A flagged line is where to look, not a
  finding. Staleness, redundancy, and rule violations are human
  dispositions; the ledger feeds the gate brief, it does not replace it.
- **The audit is not done when the tool runs.** The Sep 23 audit's most
  important findings (a legal name outside its approved location, a
  stale whitepaper, an uncommitted remediation) came from the human
  read, not from any scanner. The tool mechanizes roughly one third of
  the ritual; the README section below is the other two thirds.
- **The name scan ships without its terms.** Sensitive search terms are
  supplied at run time via `--terms-file` (one term per line) and are
  never written into the repo or the ledger. This is deliberate: the
  capability is public, the term list is not.
- No network, no dependencies, Python 3.9+.

## Run it

From `tools/repo-audit/`:

```
python3 -m repoaudit.cli                      # ledger to stdout
python3 -m repoaudit.cli -o /tmp/audit.md     # ledger to a file
python3 -m repoaudit.cli --terms-file TERMS   # + name scan
python3 -m repoaudit.cli --include-tbd        # flag TBD too
python3 -m repoaudit.cli --exempt 'harness/data/*'   # exempt a path
```

Run the tests (the direct invocation is the documented one; unittest
discover finds 0 because tests/ is not a package, same as the other
tools here):

```
python3 tests/test_repoaudit.py
```

## The full ritual, as run Sep 23 (the log you asked for)

Worked example: brief 039, the audit of this repo at HEAD f8deefa
(470 files, 210 MB). Order matters: state first, then reads, then
mechanics, then the artifact.

1. **State check.** `git status` / `log` / sync. First catch of the day
   lived here: a remediation edit (brief 037 span fix) sitting
   uncommitted in the working tree. A checkpoint requires a clean or
   explicitly-adjudicated tree.
2. **Full enumeration.** Every file listed (`find`, no .git), counted,
   sized. 210 MB of mostly screenshots is normal here; what matters is
   per-directory shape and anything unexpected (a no-extension file, a
   directory the docs never mention).
3. **Read the front door and the governance layer in full:** README,
   WHITEPAPER, CONSTITUTION, GOVERNANCE, CONTRIBUTING, CODE_OF_CONDUCT,
   CHANGELOG, UNIVERSAL_LOG, CITATION.cff, the ledgers. Front-facing
   documents rot fastest; the audit's biggest cluster (brief 039 F3-F5)
   was here, not in the deep record.
4. **Read every brief's status line** and cross-check against the
   rulings on record. Status lines are the record's own health readout;
   one stale "not pushed" line is a small lie with a big audience.
5. **Read the case-study LOGs, per-pilot logs, kernels, tool READMEs,
   archive READMEs, scratch.** Archives get read too; archived does not
   mean exempt (the naming-convention catch lived in releases/).
6. **Mechanical scans** (now this tool): em-dash grep, name scan with
   runtime terms, TODO sweep, broken relative links (script-checked:
   zero), tracked-artifact check, image-extension census.
7. **Run the artifact.** Execute both tools' test suites directly and
   byte-compile the harness. An audit that only reads commits the exact
   sin this lab studies: verification-shaped activity with no execution
   behind it.
8. **The human pass.** Everything flagged gets a disposition: real
   finding / exempt by ruling / fine-as-is. Dispositions land in a gate
   brief (PROPOSAL), never as silent fixes. Do not delete anything;
   archive anything before changing (retool discipline).

## When to run it

Before any checkpoint that faces an outside reader: email to a
researcher, a release, a publication, an anchor. After any heavy night:
the Sep 23 audit found its staleness cluster exactly where three days
of fast record-keeping had outrun the front-facing docs. Cadence rule
of thumb: if the changelog doesn't cover the last working day, the
audit is due.
