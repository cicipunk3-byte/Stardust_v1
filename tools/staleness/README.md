# staleness; number-consistency checker (Red Cat)

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: PENDING PI ADOPTION; fixture tests pass

Fixture tests pass (3/3) including a synthetic error-11 reproduction. A run against the live kernel archive pair is still owed.

Built for the error-11 class (a stale credit figure written from memory
into a kernel, Sep 23). Extracts money, percent, and multi-digit figures
with context from a document, compares against a canonical reference file,
and lists figures present in one and not the other. A candidate is a
question, not a conviction: units, dates, and semantics are human calls.
The smoke test on the error-11 pair (kernel v9 vs the cost ledger) is owed.
