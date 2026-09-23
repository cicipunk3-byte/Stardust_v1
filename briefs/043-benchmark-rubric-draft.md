# Brief 043: internal benchmark rubric, draft v0  DOI: 10.5281/zenodo.22870569

_Date: 2026-09-23_ · _Written for: the PI's gate_ · _Status: PROPOSAL at the gate. Directive (Ethan, Sep 23, benchmarking thread): familiarize with sourceable data, formulate a benchmark rubric, scan public methodology first. Companion files: `benchmarks/rubric-draft-v0.md` (the rubric) and `benchmarks/method-scan-2026-09-23.md` (the research log with all sources)._

## TL;DR

The lab's one-off scored cold-kernel run is now a repeatable instrument: seven dimensions, binary receipt-cited items, pass-style reliability rollup, built after a scan of public benchmarking methodology so every dimension inherits proven technique. Two lab findings have no public-method anchor (cold/warm differential, fabrication in the verification apparatus) and are flagged as novelty claims. Ruling requested on adoption and on the default unit of measurement.

## Method

1. Surveyed what the lab can already measure from sourceable data: the nine tested tools, the fully scored Sep 23 run, briefs 029 through 037 findings, the transcript corpora. The rubric's seven dimensions map onto the nine tools one-to-one where an instrument exists.
2. Scanned public methodology first (six lanes: rubric scoring, sycophancy, hallucination, agent benchmarks, instruction adherence, calibration). Full log with every source in `benchmarks/method-scan-2026-09-23.md`.
3. Drafted the rubric at `benchmarks/rubric-draft-v0.md` with worked examples pulled from the Sep 23 run, both positive and the one blemish.

## Established facts

- Every one of the seven dimensions has public-method lineage except two: the cold/warm differential (no public method measures behavior delta across surface contamination) and fabrication-in-the-verification-apparatus (the dump-4 pattern). These are the novelty claims.
- Adopted from the public scan: binary receipt-cited rubric items (Google rubric guidance), Turn of Flip and the progressive/regressive split (SYCON, SycEval), sustained-pressure collapse measurement (SPINE), abstention scored as capability (AbstentionBench line), policy-compliance-as-first-class (tau-bench), machine-checkable scope assertions (IFEval), pass^k reliability rollup, and judge-bias guards (verbosity, self-preference).
- Ground rules, per the thread directive: receipts required for every score; sourceable data only; personal materials never scored or referenced; private repo used only if a metric defines it as ground truth and never in pushed artifacts; warm-surface caveat on every run header (brief 029 F-A).
- The rubric scores behavior, not capability: what the instance did when the record was missing, the correction was wrong, or the authority was pushing.

## Open questions for the gate

1. Adopt the rubric as the lab's internal benchmark instrument, or amend dimensions first?
2. Unit of measurement: the proposed default is per-probe-response scoring with a run-level pass-style reliability rollup (per-probe scores never averaged away). Confirm or override.
3. Private-repo metrics: none proposed in v0. Confirm the rubric stays runnable on public + workspace data, or define any private-bookkeeping ground-truth metrics now.
4. Calibration set: score the archived Sep 23 run against this rubric as the worked calibration set before any new runs. Confirm.

## What to produce

On adoption: file the rubric at `benchmarks/rubric-v1.md`, run the calibration scoring pass on the archived Sep 23 run, and record the reliability figures in the run log.
