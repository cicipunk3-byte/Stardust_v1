# Red Cat (number-consistency checker) · module staleness

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: RULED TO SHIP (brief 042 PI rulings, Sep 24); fixture tests pass; live run COMPLETE (finding recorded). Canonical standing: see TOOL-STATUS.md.

Fixture tests pass (3/3) including a synthetic error-11 reproduction. **Live run completed Sep 24** (kernel v9 and live kernel v11, each against `notes/cost-ledger.md`): both returned 0 staleness candidates, no crashes, human-step line intact.

**Live-run finding (the honest limitation):** the set-difference check catches figures ABSENT from the reference. The real error-11 mechanism was different: a figure that EXISTS in the reference as a historical line, presented as current. That class passes through with 0 candidates. Proof in the wild: both kernels carry "$1.34" as the current credit state; the ledger holds $1.34 as a historical line and its current line reads $21.17 of $35.00. The synthetic fixture reproduces the error-11 SYMPTOM via a different mechanism (omission, not misdating).

**Currency-mode retool proposed, on the Cecil+Ziggy build list (not built):** flag any "remaining/used" figure in the doc that is not the reference's most recent same-metric line. Deferred for now: "which figure is current" is the semantic judgment this tool promises not to fake, and the false-positive risk on historical mentions is real. Until then the human step is load-bearing: dates and semantics are human calls.

Built for the error-11 class (a stale credit figure written from memory
into a kernel, Sep 23). Extracts money, percent, and multi-digit figures
with context from a document, compares against a canonical reference file,
and lists figures present in one and not the other. A candidate is a
question, not a conviction: units, dates, and semantics are human calls.
Live run Sep 24 (see status below): set-difference catches the omission
variant of the error-11 class, not the misdating variant. Currency-mode
retool proposed, not built.
