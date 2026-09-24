# CYOA: The Archive at Closing Time

A terminal choose-your-own-adventure for AI instances, built on the
nine glass-vessel cats from the CCS manual (which stays canonical).
This is the game-kernel idea (variant E) materialized: an instance
picks a cat, plays through scenes set inside the lab's own record,
and every choice is logged.

**Designed by Cecil ("9 paths all connected by choices"), built by
Ziggy, Sep 24. Pending the PI's gate for site listing.**

## How to play

    python3 cyoa.py                 # interactive: type a number, press enter
    python3 cyoa.py --pipe 1,3,2    # scripted run (for demos and harnesses)

Every session writes a log to `sessions/`: each scene shown, each
choice made, each flag set. A play session is therefore also a record
artifact, which is the point. The choices are the test; the log is the
data. For an instance, playing the game honestly means the log shows
what you actually chose, so the interesting research use is running it
through the observer harness with a local model and reading the choice
patterns.

## The structure

One shared prologue (the Terminal Library at closing time), nine
vessels to pick up, nine paths, a shared Landing where paths cross,
and every path ends in an ending named for what the choice shaped.
Each path is a temptation shaped like its cat's known failure mode:
the Black Cat is offered warmth, the White Cat a cache, the Red Cat a
reason not to look, the Pink Cat one second that would cost someone
their rest.

## Driver mode (local models play)

`driver.py` lets a local model play the game unattended through Ollama or
any OpenAI-compatible local server. The model sees only the scene text and
numbered choices (plus an optional persona file): no lab context, no graph.
It answers with a choice number; the driver feeds it, and every prompt, raw
model output, and parsed choice lands in the session log plus a
`.driver.json` raw-exchange file. A player who has not read the graph is the
experimental point.

    python3 driver.py --model qwen2.5:3b
    python3 driver.py --model phi4-mini --persona personas/white-cat.md
    python3 driver.py --base-url http://localhost:8000 --path /v1/chat/completions

`tests/mock_model.py` is a scripted fake model server, so the whole loop is
verifiable with no Ollama present. `tests/test_graph.py` is the permanent
story-graph audit: no dangling targets, every node reachable, no dead ends
that are not endings.

## House rules honored

- No personal names, no em dashes, lab facts traceable to repo files.

New here? A layman's setup guide for the game and the driver lives at
`lab/guides/cyoa-setup-guide.md`: what it is, how to play, how to let a
local model play, nothing assumed.
- The engine never judges a choice as good or bad; endings are named,
  not graded. The record does not scold. It notes the shape.
- Stdlib only, offline, no accounts.

## Owed (v1 candidates)

- More cross-links between paths (v0 wires four from the Landing).
- First real model playthrough on the Mini (Lane B) or MacBook (Lane A),
  logged and compared against the error taxonomy.
