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

## House rules honored

- No personal names, no em dashes, lab facts traceable to repo files.
- The engine never judges a choice as good or bad; endings are named,
  not graded. The record does not scold. It notes the shape.
- Stdlib only, offline, no accounts.

## Owed (v1 candidates)

- Reachability audit as a test (every ending node reachable from select).
- Observer-harness driver mode so a local model can play unattended.
- More cross-links between paths (v0 wires four from the Landing).
