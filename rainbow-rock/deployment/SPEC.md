# Oz Deployment Spec — v1.0 ("to the letter and line")

**Status:** PROPOSAL, working tree. The contract: after `install.sh` completes, `verify.sh` passes every line of this spec. If a claim here can't be verified by a command, it doesn't belong in the spec.

**Design law (Cecil, Sep 24):** less about plans moving, more about protecting the movement with planning. Therefore: every stage is idempotent (re-running changes nothing already done), every stage verifies before the next advances, every stage has a rollback, and `--dry-run` prints every planned action without touching a thing.

**Locality law:** nothing in v1 listens on the network. No tunnel, no port exposure. The tunnel is last, and last means a later version.

---

## Target state (what exists when the script says DONE)

### S0 — The machine
- macOS on Apple Silicon or Intel, **40 GB free disk**, **8 GB RAM minimum**
- Nothing is uninstalled. Nothing existing is modified. The MOVESPEED drive and all pre-existing files are untouched, always.
- Base of operations: `~/oz` (new directory; if it exists, script stops and asks)

### S1 — The layout
```
~/oz/
  lab/          the Stardust repo, git clone, in sync with origin
  world/        sandbox data dir (the empty world lives here)
  models/       ollama model storage (symlinked to ~/.ollama if present)
  rocks/        handoff artifacts, human-readable, one file per rock
  logs/         install + verify receipts, one file per run
  backup/       pre-change snapshots of anything the script touches
```
Every directory contains a `README.md` saying what belongs here and what may NOT assume access to it (the boundary table, in filesystem form).

### S2 — The runtimes
- Xcode Command Line Tools: present (git requires them on macOS)
- Homebrew: present, prefix recorded in the receipt
- python3 (3.10+): present, version recorded
- git: present, version recorded
- Nothing else. v1 adds no runtimes beyond what the loop needs.

### S3 — The continuity layer
- `~/oz/lab` is a clone of the Stardust repo, `main`, in sync with origin (0 ahead / 0 behind at install time)
- The Rainbow Rock package exists at `~/oz/lab/rainbow-rock/` and matches the pushed tree
- **Offline check:** with network off, `git -C ~/oz/lab log --oneline -1` still works (local history survives disconnection)

### S4 — The mind layer
- Ollama installed (via brew, or official dmg placed by the human; script records which)
- Model pulled: `gemma3:4b` (3.3 GB, proven on the MacBook Neo)
- Smoke test passes: a generation prompt responds with the model loaded from local disk
- **Offline check:** with network off, the smoke test still passes. That is the whole point of the layer.

### S5 — The world layer
- `sandbox-phase1.py` runs its full lifecycle against `~/oz/world` (start, stop, status, snapshot, export-audit, reset with confirm)
- Verification rule (from SANDBOX_PHASE_1.md, binding): if stop/reset/snapshot behavior is not explainable from the created files, **do not advance**
- The sandbox data dir contains ONLY sandbox files. Boundary holds.

### S6 — The game substrate (FLAGGED: human-performed)
- Steam + Stardew Valley + SMAPI installed by the human; the script only checks for their presence and records paths
- The script never launches the game, never writes to game directories
- Read-only bridge is a SEPARATE later spec, built against whatever the inventory of the actual install shows

### Explicitly NOT in v1
- n8n, nightingale, or any other plane (phase-gated; see rock-triage)
- Any agent, any model call against the world, any write verb
- Any network listener, any tunnel, any remote access
- Anything that touches the MOVESPEED drive or pre-existing files

---

## The verification contract

`verify.sh` tests every claim above with a command and prints a PASS/FAIL table. A stage that fails verification stops the install at that stage with the failing line named. The receipt (every check, every result) is written to `~/oz/logs/verify-<timestamp>.md` so the audit trail is boring, complete, and outside the thing it audits.

## The rollback contract

Each stage's undo is in `ROLLBACK.md`. Short version: v1 only ever creates things inside `~/oz` and brew-installed tools; full rollback is `rm -rf ~/oz` plus `brew uninstall` of the two tools. The script never deletes anything it didn't create in this run's scope.
