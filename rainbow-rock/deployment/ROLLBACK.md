# Rollback — protecting the movement

Law: the script never deletes anything it didn't create in this run's scope, and rollback is planned before the stage runs, not after something breaks.

## Stage-by-stage undo (v1)

| stage | created | undo |
|---|---|---|
| 1 layout | `~/oz/{lab,world,models,rocks,logs,backup}` | `rm -rf ~/oz` (nukes everything below in one move — see "full rollback") |
| 2 runtimes | brew-installed tools only | `brew uninstall <tool>` — script never force-installs, so undo only what you chose to install |
| 3 continuity | the git clone inside `~/oz/lab` | covered by `rm -rf ~/oz` |
| 4 mind | ollama + the gemma3:4b model (3.3 GB) | `ollama rm gemma3:4b` then `brew uninstall ollama` (or delete the app if dmg-installed) |
| 5 world | sandbox artifacts inside `~/oz/world` | `rm -rf ~/oz/world` and re-run stage 5 for a clean empty world |
| 6 game | human-installed; script wrote nothing | nothing to undo from the script |

## Full rollback (everything to zero)

```sh
rm -rf ~/oz
brew list          # then uninstall only what this project added
ollama list        # then remove models if kept for other work
```

## What can never be rolled back by this script

- Anything on the MOVESPEED drive or any pre-existing file — the script never touches it, so it never needs undoing.
- Git history on the remote — the script never pushes. Push remains a human act behind Cat's gate.

## Before any future stage (S7+, bridges and planes)

A stage that introduces a network listener or a database must add its own rollback section HERE in the same turn it's added to the spec. A stage without a rollback line doesn't ship. That is the "protecting the movement with planning" rule, applied forward.
