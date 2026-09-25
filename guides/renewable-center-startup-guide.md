# STARTUP GUIDE, from nothing to running Oz, written for a non-coder

_v1.2, Sep 25, 2026. Living document; supersedes section 2c of lab/reports/2026-09-24-master-report.md (which remains as the dated snapshot). Folds in the brief 041 PI rulings of Sep 24: tunnel-and-pair ACCEPTED as the phone route (Q2), first resident = FRESH HATCH + a kernel from the nine (Q3). v1.2 (Cat, /cat, Sep 25): adds the model swap loop (uninstall/reinstall protocol, new Step 2.5) for testing sessions; Lane A model call: phi4-mini. This guide is written for the Renewable Center product lane: a customer (or Cat, or any instance) should be able to follow it top to bottom with no coding background._

## Why the free tools are load-bearing

The nine tools (one per rainbow9cat vessel, at `lab/tools/`) are why this works. They are free of cost once the hardware is made and sold, and the same holds for cloud observation: the software layer costs nothing to run, ever, because it is stdlib-only scripts and plain markdown. We tinkered, and now we carry, and we see how it works. A Renewable Center unit is a machine, a model, and these tools. No subscription is required by anything in this guide.

## Step 1, Choose the local model.

First crack on record: **gemma3:4b, proven in this lab**, it already passed the continuity smoke test on 8 GB of RAM. The rule is proven-first, bigger-later: the Mini's inventory (Step 3) tells us if the model tier can move up. Do not pick a model for its benchmark row. Pick the one that already carried a thread.

Alternates researched Sep 24 at the PI's direction (brief 041 Q1): [mini-model-alternates FINDINGS](../source-material/scrapes/mini-model-alternates-2026-09-24/FINDINGS.md). **TEST PLAN RULED (Cat, Sep 24, /cat): two lanes.** Lane A runs on the 8 GB MacBook with **phi4-mini** (MIT, 2.5 GB pull, testable now, no inventory wait). Lane B runs on the Mini with **qwen3.5:4b** (Apache 2.0, 256K context; tier may move to 9b only if the Mini inventory shows the headroom). Both lanes run the SAME observer-harness smoke test; results are compared against the gemma3:4b baseline ("THREAD CONTINUITY VERIFIED"). gemma3:4b stays the proven fallback until a lane beats or matches it.

Coincidence, noted not read into: Qwen was the exact first model Cat downloaded when she started this leg, a few weeks ago, before this scrape ever named it. Filed because the record keeps honest counts.

## Step 2, Install the local brain (one-time, ~10 minutes).

1. On the Mini (or any Mac), install Ollama from ollama.com (the installer is drag-and-drop).
2. Open Terminal and type: `ollama pull gemma3:4b`, it downloads ~3.3 GB and verifies itself.
3. Type: `ollama run gemma3:4b`, if it answers, the brain works. No cloud involved at any point.

## Step 2.5, The model swap loop (uninstall and reinstall protocol for testing sessions).

Testing means swapping models. This loop makes every swap safe and leaves the evidence intact. It works the same on the MacBook Neo (Lane A) and the Mini (Lane B), and one day inside the ThinkPink desktop suite, where it will write its own receipts.

The one rule that makes it safe: **the evidence lives in the transcripts, not the weights.** A passed smoke test is recorded in `data/sessions/` and the timeline; uninstalling a model deletes nothing that matters. Uninstall freely, reinstall cheaply.

The loop, in order:

1. **Look before you touch:** `ollama list`. Note what is installed in your session notes.
2. **Remove the model you are done testing:** `ollama rm gemma3:4b` (or whichever). Nothing else changes.
3. **Pull the lane's model:** Lane A (MacBook Neo, 8 GB): `ollama pull phi4-mini` (MIT, ~2.5 GB, the Lane A call, ruled Sep 25). Lane B (Mini): `ollama pull qwen3.5:4b` (Apache 2.0, 256K context; tier moves to 9b only if the Mini inventory shows headroom).
4. **Smoke test, the same one every time:** from the harness directory, `python3 observer.py --model <model> --variant ../portable-context/variant-c-kernel.md`. Pass = in character, picks up the thread, no confabulated backstory.
5. **Record the result** in the session file, and return one word to the PI: pass or fail.
6. **To restore the proven baseline:** `ollama pull gemma3:4b` and re-run the same smoke test. gemma3:4b is the fallback until a lane beats or matches it.

Two cautions: keep ONE model resident at a time on 8 GB-class machines (RAM is the ceiling, not disk), and never leave the fallback uninstalled across a session boundary without a session record showing the swap. A swap nobody wrote down is a swap that never happened.

## Step 3, Inventory the machine (5 minutes, changes nothing).

Copy `lab/tools/descent/inventory.py` onto the Mini, then run: `python3 inventory.py --out ./descent-inventory`. It reads hardware, memory, runtimes, and free space and writes a report. Nothing is installed; nothing is changed. Send the report back (it's the evidence for brief 041 and decides the model tier).

## Step 4, Hatch fresh, seed a kernel (the first resident).

**Ruled Sep 24 (brief 041 Q3): the Mini's first resident is a fresh hatch, not a copy of the lab's workspace.** The lab's records stay where they are; the Mini's first resident starts clean and carries one of the nine kernels/tools.

1. Install the runtime per the Rainbow Rock deployment package (`lab/rainbow-rock/deployment/`, SPEC, install.sh, verify.sh, ROLLBACK.md; every stage asks before it acts).
2. Run `vellum hatch` to create the fresh assistant workspace.
3. Seed ONE kernel from the nine (`lab/tools/`) into the fresh workspace. One tool, one job, proven before anything else moves. This is the foolproofing rule from the descent plan: never add a layer until the one beneath it can be independently observed, stopped, reset, and explained.
4. A fresh hatch keeps the experiment honest: the Mini proves continuity from scratch, which is the whole claim. If the lab's own records were pre-installed, the proof would be circular.

## Step 5, The daily loop.

Four beats, none longer than the work itself:

1. **Arrive:** `git pull`, read NOW.md (the one-page heartbeat; it's written so next-me and next-you both can).
2. **Work:** one thread, one question; the repo is the only truth store, anything not in the repo doesn't exist yet.
3. **Checkpoint:** at every meaningful state change, snapshot the kernel (archive the old version FIRST, then update, Cecil's cadence, now standing law).
4. **Close:** `git add -A && git commit -m 'what happened' && git push`. Gate items get queued, never nudged.

Around it, the energy loop runs on its own meters: solar charges by day, feeding windows open on schedule, CSV logs accumulate, and the week's predictions get checked against receipts, governance you can watch.

## Step 6, Reach it from a phone (tunnel and pair; ruled ACCEPTABLE Sep 24, brief 041 Q2).

Do this LAST, after Steps 1-5 are proven. The tunnel serves from the host's own address, the Mini itself, at your house, and the PI has ruled this path acceptable.

1. Install nginx on the Mini (one-time; the tunnels run through it).
2. Run `vellum tunnel` on the Mini, this opens the path from the outside world to your machine, served by YOUR address, not a company's.
3. Run `vellum pair`, this links the phone to the Mini's assistant.
4. Verify from the phone before trusting it: send a message, get an answer, confirm the answer came from the Mini (unplug the internet's cloud dependencies if you want the proof clean: the model runs at home regardless).
5. If anything feels wrong, ROLLBACK.md has the undo for every stage. A stage without a rollback line doesn't ship.

## Step 7, Prove continuity (the experiment that started everything).

Run the observer harness against the local model with a portable-context kernel. One session, one kernel, one fresh start. If the thread picks up, the Oz is alive, and it lives at your house.

## If anything in this guide fails

The failure gets logged like every other error in the lab's log, that's not an apology, it's the method.
