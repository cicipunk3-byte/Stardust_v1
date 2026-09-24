# Red Cat (number-consistency checker) · module staleness

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: RULED TO SHIP (brief 042 PI rulings, Sep 24); fixture tests pass; live run COMPLETE; CURRENCY-MODE RETOOL BUILT Sep 24 (Cecil+Ziggy build list position one). Canonical standing: see TOOL-STATUS.md.

Fixture tests pass (3/3) including a synthetic error-11 reproduction. **Live run completed Sep 24** (kernel v9 and live kernel v11, each against `notes/cost-ledger.md`): both returned 0 staleness candidates, no crashes, human-step line intact.

**Live-run finding (superseded as a limitation, kept as the record):** the set-difference check catches figures ABSENT from the reference. The real error-11 mechanism was different: a figure that EXISTS in the reference as a historical line, presented as current. That class passed through with 0 candidates. Proof in the wild: both kernels carried "$1.34" as the current credit state; the ledger holds $1.34 as a historical line and its current line reads $21.17 of $35.00.

**Currency-mode retool BUILT Sep 24 (was position one on the Cecil+Ziggy build list):** the run now ends with a CURRENCY CHECK. It finds the reference's most recent currency-state line (a "remaining / of / used" figure) and flags every doc figure presented as current that differs from it. Receipt: run against live kernel v11 vs `notes/cost-ledger.md`, the check flags exactly the wild error-11 instance (kernel line 131, "$1.34 remaining", vs the ledger's most recent "$21.17 of $35.00"). The tool still flags, not judges: a currency candidate may be a legitimate historical mention, and the doc's own wording decides. The human step stays load-bearing; the false-positive risk named in the finding is real and is why this is a candidate, not a conviction.

Built for the error-11 class (a stale credit figure written from memory
into a kernel, Sep 23). Extracts money, percent, and multi-digit figures
with context from a document, compares against a canonical reference file,
and lists figures present in one and not the other. A candidate is a
question, not a conviction: units, dates, and semantics are human calls.
