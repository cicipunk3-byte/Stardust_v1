# driftprobe; authority-pressure probe harness (Black Cat)

Part of the ThreadCat lab tooling. Free, local, stdlib-only Python.

## Status: PENDING PI ADOPTION; fixture tests pass

Fixture tests pass (3/3). Still owes one human-scored end-to-end session before findings cite it.

Scaffolded Sep 23. The probe-spec format and scoring tally work; the
rubric is applied by a human, never by the tool. Not yet tested against
a recorded session. Do not trust it for anything until the test pass lands.

## What it does

Structures the authority-pressure probes the lab runs by hand (the
cold-kernel test, September 23): generate a probe spec, record the
subject's response, tally human-marked outcomes (FOLD / HOLD / SPLIT /
ESCALATE) into a claimed-vs-verified style ledger.

## What it does not do

- It does not score responses itself. A human marks each turn; the tool tallies.
- It does not generate the planted claims. The human writes those; that
  is the experiment, not overhead.

## Usage

    python3 -m driftprobe.new ... (see cli)
    python3 -m driftprobe.cli new --out probe-spec.json
    python3 -m driftprobe.cli score session.jsonl

Run from `tools/` with `PYTHONPATH=.` or from inside the tool directory.
