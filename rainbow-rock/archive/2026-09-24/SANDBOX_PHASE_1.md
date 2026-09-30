# Phase 1 — Empty Sandbox

`rainbow_rock_sandbox.py` is the first working Rainbow Rock component. It is
purposefully narrow: it has no network client, no model integration, no shell
execution, no game bridge, no agent identity, and no mutating world action.

## Data boundary

The program writes only below the directory supplied with `--data-dir`. The
default is `.rainbow-rock-sandbox` in the current working directory. Its
records are ordinary JSON/JSONL files and can be inspected without the
program.

## Lifecycle

```sh
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data start
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data status
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data snapshot
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data export-audit
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data stop
```

Reset is deliberately explicit and exports the audit trail first:

```sh
python3 rainbow_rock_sandbox.py --data-dir .rainbow-rock-data reset --confirm-reset
```

## What it proves

The sandbox can start, stop, reset, report state, snapshot state, and create
append-oriented world/audit records. It does **not** yet prove a World Bridge,
permission service, authorized action, agent continuity, or Rock handoff.

## Verification rule

Run the lifecycle commands using an explicit data directory and inspect the
created `world/state.json`, `world/events.jsonl`, `audit/events.jsonl`, and
`world/snapshots/` artifacts. If stop/reset/snapshot behavior is not
explainable from those files, do not advance to Phase 2.
