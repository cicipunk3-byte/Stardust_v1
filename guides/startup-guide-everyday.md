# The Startup Guide (for everyone)

You do not need to be a programmer to run this lab. If you can install an app
and type one line into a terminal, you can do this. Nothing here costs money,
no account is required, and nothing you write ever has to leave your machine.

---

## What you are building, in one paragraph

A research loop that runs on your own computer: a small local AI model that
reads plain markdown files, plus a set of free tools that check its work. The
files are the memory. The git history is the backup. The model is the worker.
If the platform disappears tomorrow, everything you made is still yours.

## What you need

- A computer (Mac or Linux; 8 GB of memory is enough for the starter model)
- About 30 minutes
- No credit card, no account, no subscription

---

## The five steps

### Step 1. Install Ollama (the model runner)

Ollama is a free app that runs AI models on your own computer. Go to
[ollama.com](https://ollama.com), download it for your system, and install it
like any normal app. Open a terminal (on Mac: the Terminal app) and type:

    ollama --version

If you see a version number, it works.

### Step 2. Download the model (about 3 GB, one command)

    ollama pull gemma3:4b

This is the lab's starter model: small enough for an 8 GB laptop, good enough
for the loop. Go make tea. When it's done, type:

    ollama run gemma3:4b

You can now chat with a model that lives entirely on your machine. Type
`/bye` to leave. That's the whole trick: the "cloud" is now your desk.

### Step 3. Get the lab (one command)

    git clone https://github.com/cicipunk3-byte/Stardust_v1.git
    cd Stardust_v1

(No git? Mac: `git` is offered when you first try it. Linux: `sudo apt install git`.)

Everything in the lab is plain text files. Open them in any editor. They are
meant to be read by humans first.

### Step 4. Run the smoke test (one command)

    cd harness
    python3 observer.py --variant ../portable-context/variant-a.md

This starts a session between you and the local model, using one of the lab's
context kernels. Read `harness/CHEATSHEET.md` when you want more: it has the
four commands you actually need, in plain English, with a glossary.

### Step 5. (Optional, recommended) Give it a memory

The lab's memory layer is [MemPalace](https://github.com/MemPalace/mempalace):
it stores your conversation history word-for-word and finds it again by
meaning. One command installs and wires it, with privacy guards already on:

    ./tools/mempalace-bridge/mempalace-fold-in.sh /path/to/Stardust_v1

Then, whenever you want to check the tools are home:

    python3 ark/ark.py list

---

## What you have at the end

A loop that runs with the network cable pulled: local model, verbatim memory,
markdown record, versioned history. Nobody can take it away and nobody can
read it but you.

## When something breaks

- Read `harness/CHEATSHEET.md` (plain English, short)
- Every tool dir has a README written for humans
- Everything is in git, so mistakes are undoable: `git status` first, panic never

*Status: tested setup, documented honestly. If a step fails, that is a bug in
this guide, not in you. File it.*
