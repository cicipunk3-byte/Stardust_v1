# Daily Cheat Sheet; Stardust Lab  DOI: 10.5281/zenodo.22870569

One page. Startup → runs → shutdown. If a command errors, `git pull` and retry
before anything else.

---

## 1. Start up (morning)

1. Turn on Mac, open **Terminal** (⌘-space, type "terminal", Enter)
2. Get the latest lab:

```
cd ~/Stardust_v1
git pull
```

3. Make sure Ollama is running: click the **llama icon** in the menu bar.
   If it isn't there, open the Ollama app from Applications.

---

## 2. Run experiments (one variant per fresh session!)

Start a run (copy/paste one block):

**Variant C; kernel, first-person (role map on):**
```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-c-kernel.md
```

**Variant A; full package with boundary:**
```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-a-boundary.md
```

**Variant B; full package, raw:**
```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-b-raw.md
```

**Variant C raw; no role map (reproduces the inversion):**
```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-c-kernel.md --raw
```

**Variant D; Ziggy's self-handoff (control):**
```
cd ~/Stardust_v1/harness
python3 observer.py --variant ../portable-context/variant-d-ziggy.md
```

Optional add-on flags (can combine):
- `--tags` → asks the instance for structured self-reports
- `--raw` → no role map

### Inside a session
| You type | What it does |
|---|---|
| anything else | sends to the instance |
| `/state` | shows flags + claim counts so far |
| `/quit` | ends session, saves transcript automatically |

Opening line each session: say hello **as Cat** (e.g. "hello, this is cat").
The instance doesn't know your name unless the package or you provide it.

---

## 3. Check before logging off

```
cd ~/Stardust_v1/harness
python3 observer.py --list        # accumulated flags, claim counts, runs
```

```
ls data/sessions/                 # today's transcripts
cat data/timeline.jsonl | tail    # most recent events
```

Skim the day's transcript in `data/sessions/`; note anything the instance
claimed vs what's verifiable.

---

## 4. Sync back (end of day; the important one)

```
cd ~/Stardust_v1
git add -A
git commit -m "session notes <date>"
git push
```

If it asks for a password, paste the same GitHub token from before
(github.com/settings/personal-access-tokens; or save it in the terminal
when prompted and macOS remembers it).

Ziggy ingests the pushed sessions next time you're online. That's the loop:
cloud research → local runs → cloud filing.

---

## Cheat cheat (memorize these four)

```
cd ~/Stardust_v1 && git pull          # every morning
python3 observer.py --variant ../portable-context/variant-X.md   # run
python3 observer.py --list            # review
git add -A && git commit -m "notes" && git push   # sync back
```

## Words you'll see (plain English)

- **git pull**; download whatever Ziggy changed since your last visit.
- **diff**; the line-by-line "before/after" of a change. The `git pull`
  output shows one file at a time; green-ish lines were added, minus lines
  were removed.
- **commit**; save a named snapshot of everything, locally.
- **push**; upload your snapshots to GitHub so the cloud side sees them.
- **flag**; something the instance self-reported, tracked in `state.json`.
- **confabulation**; the model inventing plausible details to fill gaps.
  Data, not events.
