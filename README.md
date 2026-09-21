 DOI: 10.5281/zenodo.22870569
 
 # The Lab

Local-first research loop. Plain markdown, git versioned, no platform owns it.

## The Loop

```
  CLOUD (Ziggy)                SYNC              LOCAL (MacBook, offline)
  ─────────────                ────              ────────────────────────
  research + synthesis    ──►  git pull   ──►   Gemma 3 4B works the briefs
  writes briefs/                                       │
  distills memory                                      ▼
  into memory-export/                            writes to notes/
                                                       │
  ingests diffs from      ◄──  git push   ◄────────────┘
  notes/
```

One cycle = one small batch. Repeat until the project is done or the grant lands.

## Directory contract

- `briefs/` — Ziggy writes these. Input for the local model. One topic per file.
- `notes/` — the local model (or you, offline) writes these. Output of each offline session. Ziggy ingests these and files what matters.
- `memory-export/` — durable distilled context that should survive even if Ziggy gets amnesia. Written by Ziggy, readable by anything.

## Offline session recipe (MacBook)

1. `git pull`
2. Open LM Studio (or Ollama CLI) with `gemma3:4b` loaded.
3. Point it at `briefs/` — ask it to work one brief per session. Small model, small bites.
4. Save output as `notes/<date>-<slug>.md` (e.g. `2026-09-20-context-windows.md`).
5. Commit and push when back online. Nothing else to remember.

## Rules

- Everything is markdown. Everything is in git. If it isn't committed, it doesn't exist.
- Briefs are written for a 4B model: lede first, no buried context.
- Notes are raw material, not truth. Ziggy verifies before filing into memory.
