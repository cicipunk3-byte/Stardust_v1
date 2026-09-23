# kernelpress; kernel distillation scaffold (Orange Cat)

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: PENDING PI ADOPTION; fixture tests pass

Fixture tests pass (4/4); budget math exact. Prose stays human; retention scoring is the owed next step.

Splits a transcript into sections, applies a word retention budget
(default 20 percent), and emits a draft skeleton with per-section
allowances and verbatim anchor candidates (numbers, rulings, findings).
It does not write kernel prose: compression without a human DC check is
just loss with confidence. The retention-scoring pass (draft vs source)
is the owed next step.
