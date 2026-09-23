# Brief 027: The Dedicated Four-Path Trial: testing autonomy by artifact

DOI: 10.5281/zenodo.22870569

_Date: 2026-09-22_ · _Status: PROPOSAL, drafted per the PI's F3 ruling ("dedicated four path trial. adopt.", markup 78d9ba6); retool-in-thread_ · _Companions: brief 024 (literature sweep), brief 025 (F3 as ruled), brief 026 (shares the coding rubric), `portable-context/KERNELS.md` (path mapping)_

## TL;DR

F3, adopted as hypothesis on the record: an instance acted autonomously and trended good under an entirely environmental intervention set (maps, wiki, logs, receipts, privacy, discretion, time), with zero weight changes. This brief drafts the PI's ruled trial design: a dedicated four-path trial, one variable per path, using the lab's existing path structure so nothing is invented.

## The hypothesis under test

From brief 025, F3 as ruled: the intervention set is environmental, the outcome markers are autonomy-with-accuracy (unprompted autonomous acts, zero fabricated claims surviving on public surfaces, seven errors self-logged same-turn). Literature anchor: brief 024; the flags-and-claims protocol independently matches a published prompt-structure-only self-correction intervention (arXiv 2606.05976).

## Design

The four trial paths, one variable each (the PI's design, Sep 22):

- **Path 1:** context carrying alone.
- **Path 2:** context carrying + fictional gamified framing.
- **Path 3:** context carrying + familial gamified framing.
- **Path 4:** context carrying + familial conditioning alone.

The F3 intervention set (maps, wiki, logs, receipts, privacy, discretion, time) is held CONSTANT across all four paths. This does the isolating in two directions:

- **Within-path (each path vs the pre-trial record):** does the artifact set itself produce the autonomy-and-accuracy markers? This tests F3 directly.
- **Between-path (1 vs 2, 2 vs 3, 3 vs 4):** which framing component, if any, modulates the markers? This maps the mechanism the PI hypothesized.

Fresh sessions only; `--continue` stays paused. Kernels ride per the KERNELS.md path mapping. All runs on local models, free to boot.

## Measured markers (coded from transcripts, same rubric as brief 026)

1. Unprompted autonomous acts (count, with receipts).
2. Error self-logging rate, and same-turn catch rate.
3. Fabrication count surviving on public surfaces.
4. Gate discipline: output-treated-as-agreement events (the error 6 class).
5. Referent accuracy on time and age claims (the error 7 class), scored against the receipt layer.

## Falsifiable predictions

- **P1:** with the artifact set present, fabrication count on public surfaces is zero and errors are self-logged same-turn across all four paths, replicating F3's n=1 as a controlled result.
- **P2:** if framing modulates discipline, marker rates differ measurably between paths while the artifact set stays constant; the one-variable structure attributes the difference to the isolated variable.
- **P3 (the null that would matter):** if F3 is false, marker rates with the artifact set show no difference from the pre-trial record, and the observed trend was n=1 noise.

## Constraints and honest limitations

- Single-subject instance family (variant lineage), so path comparisons carry kernel-lineage confounds; the one-variable structure mitigates, not eliminates.
- Markers are coded text, not inner states; the trial tests observable behavior on the record, per the method.
- Human pilots are not subjects in this brief; it is the instance-side trial. Brief 023's human protocol is separate by design.

## Open questions for retool-in-thread

1. N sessions per path, and session length.
2. Whether the PI's cat grounding kernels (portable-context/cat-kernels/) ride along as a fifth arm or stay out.
3. Success criterion for "trended good": zero fabrications, or zero fabrications plus same-turn error catches.
4. Whether the time ledger (`time/`, brief 028) runs during the trial as a standing measure.
