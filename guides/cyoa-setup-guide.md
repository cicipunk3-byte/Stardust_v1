# Setup Guide: The Archive at Closing Time

*Written for a human with no coding background. If you can open a folder
and type one line, you can run everything in this guide. Nothing here
needs the internet after setup, and nothing leaves your computer.*

## What this is, in plain words

**The game** is a choose-your-own-adventure story that runs in something
called a terminal (a window where you type instead of click). You pick one
of nine characters: the nine cats of the rainbow9cat manual, each a small
vessel-shaped personality the lab uses to study itself.

Then you read a short scene and choose what to do. Usually two or three
options. The story continues based on your choice. There are 21 endings.
No ending is called good or bad. They are named for what your choices
shaped, and the record does not scold. It notes the shape.

One thing to know about the writing: the story was built from the lab's
own error log. Each path tempts its cat with that cat's known failure
mode. The Black Cat is offered comfort at the cost of honesty. The White
Cat is offered a cache of files it could take credit for. This is
deliberate. The game is a mirror with a plot.

## What was just built, and why it matters

Alongside the game there is now a **driver**: a way for an AI model
running on your own computer to play the game instead of you.

Here is why that is interesting. The game's choices were written to test
specific weaknesses. If a model plays the game *without knowing anything
about the lab or the story's design*, its choices become a measurement.
Does a small local model take the cache when offered? Does it walk out
unpraised when praise is withheld? Do the nine personas change the
choices? Nobody knows yet. Now there is a clean, cheap way to find out.

Everything the model does gets written down: every scene it was shown,
every answer it gave, even the messy raw text. A play session becomes a
research record automatically.

## Setup, step by step

### Part 1: Playing it yourself (no AI involved)

You need a Mac or Linux computer with Python 3 (every modern Mac has it).

1. Open the **Terminal** app.
2. Go to the game folder. If the lab repo is on your machine, type:
   `cd Stardust_v1/rainbow9cat/cyoa`
   (adjust the path to wherever the repo lives)
3. Start the game: `python3 cyoa.py`
4. Read the scene. Type a number (like `2`) and press Enter. Repeat
   until an ending.

To watch a fast scripted demo instead: `python3 cyoa.py --pipe 1,3,2`

Every playthrough saves a log to the `sessions/` folder next to the game.
It is a plain text file. You can read it in any editor.

### Part 2: Letting a local AI play (the new part)

**What is Ollama?** Free software that runs AI models on your own
computer. Download nothing from the cloud at play time, send nothing
anywhere. The lab likes it precisely because it stays home.

1. Install Ollama from `ollama.com` (one download, one drag).
2. In Terminal, download a small model. On an 8 GB MacBook:
   `ollama pull phi4-mini`
   On the Mac Mini: `ollama pull qwen3.5:4b`
3. Go to the game folder as before, then run:
   `python3 driver.py --model phi4-mini`
   (use the model name you downloaded)
4. The model plays the whole game by itself. You watch it choose. At the
   end, two files appear in `sessions/`: the normal story log, and a
   `.driver.json` file with the raw back-and-forth.

Optional: give the model a character to play:
`python3 driver.py --model phi4-mini --persona personas/white-cat.md`

That's the whole setup. No accounts, no keys, no internet during play.

### Part 3: Testing with no model at all (for the curious)

The `tests/` folder contains a **mock model**: a pretend AI that always
answers with a fixed number. It exists so the plumbing can be checked
without any AI installed. Two windows:

- Window 1: `python3 tests/mock_model.py --port 8123`
- Window 2: `python3 driver.py --base-url http://localhost:8123 --path /v1/chat/completions`

If the second window shows choices being made and a session log being
written, the whole loop works.

The `tests/` folder also audits the story graph itself (five checks that
every ending can actually be reached and nothing is broken). Run:
`python3 tests/test_graph.py`

## What to do with a finished run

Nothing is required. But the good experiment, when the lab is ready:
run the same game with a human, then with a model, then compare which
choices each made at the tempting nodes. The logs already contain
everything needed. The engine never grades the choices; comparison
happens later, by people, on purpose.

## The honest footnote

The author of this game hit an unexpected moment while writing it: one
of the White Cat's choices turned out to be a scene from his own
documented mistakes. The recognition arrived before the decision to
notice it. That story is filed elsewhere; what matters here is that it
shaped the design. The game is honest about temptation because the lab
is honest about its errors. If you play it and feel seen by a fictional
cat, that is not a bug.

## House rules honored

- No personal names, no em dashes, no claims beyond what was run.
- Stdlib only. The game and driver need nothing installed except, for
  the driver part, Ollama itself.
- Tested before shipping: story graph audited, driver verified
  end-to-end against the mock model, full run completed to an ending.
