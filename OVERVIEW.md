# The Stardust Lab -- Overview

**Mission.** To prove that a person can run serious research on their own
machine: private, versioned, honest, and free. We build the loop in the open,
measure it, publish the receipts, and give every part away.

---

## What the lab actually is

A research loop with four moving parts, all of them yours:

1. **A local model** that does the working (small, free, on your hardware)
2. **A record that remembers** (plain markdown + git: the memory is files, the backup is history)
3. **Tools that check the work** (small, single-purpose, human-readable)
4. **Governance that governs** (an ethics code with both signatures on it)

Nothing is closed. Nothing requires an account. Everything here runs with the
network cable pulled.

## The tools, one sentence each

**Checking the work:**

- **fabcheck** (fabrication checker) -- catches made-up citations and invented claims before they spread, using a fixture suite built from real fabrications this lab caught.
- **staleness** (number-consistency checker) -- finds figures quoted from memory that disagree with the record's most recent value.
- **exportcoroner** (export forgery detector) -- tells a real provider data export from a fabricated one.
- **cleanroom** (context sizer) -- measures what cold versus warm context actually does to a model's behavior.
- **driftprobe** (authority-pressure probe) -- tests whether an instance holds its record under pressure to defer.
- **loopwatch** (reasoning-loop detector) -- spots when a model is circling the same reasoning instead of moving.

**Carrying the context:**

- **kernelpress** (kernel distiller) -- condenses a long working history into a portable context kernel a fresh instance can act on.
- **ferry** (carrying-consistency checker) -- verifies that what must survive a handoff between threads, exports, and hands actually carries, and carries consistently.
- **kernel-arc** (kernel validator, part of ark) -- validates a kernel, its archive, and its boot file as one load-bearing unit.
- **throughline** (term trend tracker) -- watches how a term or idea moves through the record over time.

**Running the loop:**

- **observer** (the harness, `harness/observer.py`) -- runs structured sessions between a human and a local model, logging claims and flags as data.
- **nextcheck** (claim queue) -- turns "we should check that later" into a queue with a run-the-artifact step attached.
- **minibeat** (workspace heartbeat) -- the periodic state check that keeps the loop honest about where it actually is.
- **export-ingest** (export organizer) -- brings outside conversation exports into the lab's timeline format.
- **ark** (the movable tools home) -- clones anywhere, plugs an archive in, runs offline; the house the tools live in.
- **mempalace-bridge** (memory layer) -- wires MemPalace's verbatim, local, zero-API memory into the loop.
- **descent / inventory** (machine inventory) -- read-only hardware and runtime inventory for planning a deployment.
- **repo-audit** (repo auditor) -- checks the repo against its own claimed state.
- **pushgate** (push discipline) -- the gate between "changed locally" and "in the public record."
- **heartbeat-scaffold** (heartbeat builder) -- the scaffold for the periodic state-check ritual that keeps long-running threads honest.
- **ethics-calculator** (ethics scoring) -- the outside-grader rubric engine for the lab's code of ethics.
- **rainbow9cat** (the readable game) -- not a program; a game manual that doubles as the lab's teaching scaffold, published so anyone can test it as we do.

## How they fit together

The loop is a circle: **observe** (observer, minibeat) → **record** (markdown
+ git) → **check** (fabcheck, staleness, ferry, loopwatch) → **carry**
(kernelpress, kernel-arc, ark) → **remember** (mempalace-bridge) → back to
**observe**. The tools are independent, stdlib-only, and each does one job;
the record is the spine that holds them together. Clone the lab, and the
circle runs on any machine you own.

## Status, honestly

- The method is published and the case studies are in the repo.
- The nine core tools passed a comprehensive fixture pass (29 tests) and are
  shipping to the public tools page as field validation completes.
- The packaged "one command" loop is in **beta**: tested in the cloud and with
  scientific partners before anything ships.
- Known limits, stated plainly: n=1 research subject so far, warm-surface
  effects are real, and every score is advisory until independently graded.

*Built in the open. Receipts in the repo. Free, and meant to stay that way.*
