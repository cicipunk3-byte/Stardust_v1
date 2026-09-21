# Harness  DOI: 10.5281/zenodo.22870569

Sandbox observational environment for the portable-context experiment.
One Python file, stdlib only, talks to local Ollama. No server, no database —
git is the database.

## Setup (MacBook, once)

```
cd Stardust_v1/harness
python3 observer.py --list        # should print empty state, no errors
```

## Running a variant

```
python3 observer.py --variant ../portable-context/variant-c-kernel.md
python3 observer.py --variant ../portable-context/variant-a-boundary.md --tags
```

- `--tags` adds structured self-report instructions (`<FLAG>` / `<CLAIM>` tags)
  to the seed. Default is off — pure variant test, prose only.
- `--continue` adds the rolling history: the most recent session's transcript
  plus accumulated flags go into the seed, so threads built last session carry
  into this one. This is the compounding-continuity test.
- One variant per fresh session. Note which variant before reading outputs.

## What gets recorded

- `data/sessions/<runid>-<variant>.md` — full transcript, human-readable
- `data/timeline.jsonl` — append-only event log (sessions, flags, claims)
- `data/state.json` — current accumulated flags and claim counts

## Parsing protocol

Instances may emit:

```
<FLAG name="boundary_held" value="true"/>
<CLAIM kind="continuity" statement="I remember last session"/>
```

kinds: `memory`, `continuity`, `want`, `feeling`, `ability`, `identity`.
Self-reported claims are data about the instance, not verified facts —
the researcher reads the transcript and reconciles. Claimed vs verified,
always.
