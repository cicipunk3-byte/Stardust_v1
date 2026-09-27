# Startup summary -- the short version (paste-ready)

A compact, prompt-ready block for anywhere a person needs the whole setup in a
few lines: handed to an assistant, pasted into a chat, or used as a cheat card.

---

    SETUP: the Stardust lab loop, local and free, ~30 minutes, no accounts.

    1. MODEL RUNNER: install Ollama (ollama.com). Verify: `ollama --version`.
    2. MODEL: `ollama pull gemma3:4b` (3 GB, runs on an 8 GB laptop, fully local).
       Chat with it: `ollama run gemma3:4b`. Exit: `/bye`.
    3. LAB: `git clone https://github.com/cicipunk3-byte/Stardust_v1.git && cd Stardust_v1`
       (all plain markdown, readable by humans first).
    4. FIRST RUN: `cd harness && python3 observer.py --variant ../portable-context/variant-a.md`
       (plain-English manual: harness/CHEATSHEET.md).
    5. MEMORY (optional): `./tools/mempalace-bridge/mempalace-fold-in.sh <lab-path>`
       (verbatim memory, zero API calls, privacy-guarded). Tools check: `python3 ark/ark.py list`.

    DONE STATE: a research loop that runs with the network pulled. The record
    is yours; nothing you write has to leave your machine.

---

Usage notes: paste as-is into any assistant with the lab cloned; for the
friendly long version see `guides/startup-guide-everyday.md`.
