# Brief 041: self-host run results, the fork audit and the cloud hookup  DOI: 10.5281/zenodo.22870569

_Date: 2026-09-23_ · _Written for: the PI's gate_ · _Status: PROPOSAL at the gate. Build-lane directive (Cecil, Sep 23): audit the fork, run it, report back. Nothing was pushed to the lab repo except this brief set; the test assistant was created in the sandbox only._

## TL;DR

The assistant platform's source was forked to the lab's GitHub, audited, installed, and RUN end to end in the sandbox today: hatch, daemon, credential-executor, and gateway all came up, and the runtime answered authenticated-only over HTTP as documented. The decisive finding is structural: a hatched assistant's on-disk workspace is the same file layout the lab's records already use (IDENTITY.md, SOUL.md, NOW.md, memory/, skills/), so migrating the loop to the Mac Mini is a copy, not a port. No model turn was executed: no provider key was configured, by design, pending brief 040.

## Method

1. Cloned `cicipunk3-byte/vellum-assistant` (14,118 files). Fork divergence checked against `vellum-ai/vellum-assistant` upstream: 0 ahead, 0 behind upstream main at ae47e199. MIT license. Zero lab modifications.
2. Read the architecture index, memory deep dive, and hosting docs from source (docs are React-rendered; text extracted from the content components).
3. Installed: `bun install --frozen-lockfile` (3,410 packages, 84.31s), then `./setup.sh` (linked the `vellum` CLI).
4. Ran: `vellum hatch` created local assistant `vellum-fresh-dove-tz77gt`, started the assistant daemon (http://127.0.0.1:7831), the credential-executor sibling process, and the gateway. `vellum ps` confirmed the assistant alive, `cloud: local`.
5. Verified security behavior: unauthenticated HTTP GET to the daemon returned 401 Unauthorized (JWT route-policy enforcement working as documented).
6. Inspected the hatched assistant's data directory on disk.

## Established facts (run receipts)

- CLI version at first run: `@vellumai/cli v0.12.4`. Runtime requirements met exactly (bun 1.3.11, node 22).
- Hatch warnings were honest: "No LLM provider API key is configured. The assistant will fail when you try to send a message." No key was provided. No model turn was executed.
- The daemon boots a disk-pressure guard, background-work gates, and JWT auth before serving, matching the architecture docs.
- The hatched assistant's workspace layout on disk: IDENTITY.md, SOUL.md, NOW.md, HEARTBEAT.md, BOOTSTRAP.md, config.json, memory/, skills/, pkb/, channels/, conversations/, users/, hooks/, routes/, signals/, logs/, data/. This is a one-to-one match with the lab's platform workspace structure.
- Deployment path for the Mini, from the repo's own docs: `./setup.sh` then `vellum hatch` on the host; `vellum tunnel` plus `vellum pair` to reach it from a phone; tunnels run through nginx (installed separately).

## Findings

- F1. The workspace-format identity is the headline: the lab's records and the runtime's native format are the same shape. Migration is a file copy plus a hatch, and the repo stays the source of truth either way.
- F2. The self-host path needs no Vellum account for the core loop, but a model provider is still required for any model turn (Ollama or BYOK; see brief 040).
- F3. Local mode's availability tradeoff is real and documented by the platform itself: the loop is up when the Mini is up.
- F4. The sandbox test consumed most of the free disk (88% used at test end with the clone and node_modules in place). A Mini deployment should budget for the clone, node_modules, and model weights together.
- F5. The fork is a snapshot of a fast upstream. Staying in sync is a decision the gate should make deliberately, not drift into.

## Open questions

1. Does the full turn loop work against Ollama on the Mini's hardware at usable speed (the model the harness already runs is 4b class)?
2. Is the tunnel-and-pair path acceptable to the PI as the phone-access route, given it serves from the host's own address?
3. Which assistant workspace should become the Mini's first resident: a fresh hatch, or the lab's records as the seed workspace?

## What to produce

PI read on findings F1 through F5, plus rulings on the open questions. The build lane's proposed order remains: Ollama turn first, BYOK lane second, tunnel last.
