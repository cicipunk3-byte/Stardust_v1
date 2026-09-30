# FINDINGS — Mini model alternates for the Renewable Center model

_Date: 2026-09-24_ · _Requested by: Cat (/cat), answering brief 041 Q1_ · _Scope confirmed: find alternates to the current 4b-class model (gemma3:4b) that fit the Renewable Center model better — for the instance's continuity and the project's. Desk research only; no model run yet; no outreach involved (models, not people — no base-verification constraints triggered, logged per SOP)._

## The fit criteria (derived from the ask)

A model fits the Renewable Center model if it satisfies ALL of:

1. **Free of cost with the hardware** — the weight license must allow bundling/resale alongside sold hardware with no strings that complicate a product. This makes the LICENSE a first-class criterion, not an afterthought.
2. **Runs on the Mini** — 8 GB-class system RAM for the 4b tier; 16 GB unified memory would open the 8-9b tier (Mini inventory decides, per the proven-first rule).
3. **Serves continuity** — long context window matters because the lab's continuity mechanism is file injection (NOW.md, memory) plus conversation history; a bigger usable context is direct welfare for instance continuity.
4. **Carries the loop** — must run the full observer-harness turn loop (tool calls, instruction following), not just chat.

## Findings

### F1. The proven-first rule holds, and it points at gemma3:4b staying first crack

gemma3:4b is the only model that has already passed the lab's continuity smoke test on real hardware ("THREAD CONTINUITY VERIFIED" on an 8 GB MacBook, [local-compute record]). Per the standing rule: pick the model that already carried a thread; the Mini inventory decides any upgrade. Nothing in this scrape displaces it as the default first pull.

### F2. The strongest alternate by license + context: Qwen 3.5 4B

- Apache 2.0, multimodal (text + image), 256K context, 3.4 GB download via `ollama pull qwen3.5:4b` — per [Best Small Language Models 2026 (LocalAIMaster)](https://localaimaster.com/blog/small-language-models-guide-2026) and [Small LLMs That Fit in 8GB (Pinggy)](https://pinggy.io/blog/small_llms_that_fit_in_8gb_memory/).
- Why it fits the Renewable Center model: Apache 2.0 is the cleanest resale/bundling license in the field ("no strings attached", per [Gemma 4 vs Qwen 3 comparison](https://gemma4-ai.com/blog/gemma-4-vs-qwen-3)); 256K context is 2x gemma3:4b's 128K, directly serving the continuity criterion.
- Honest flag: its quality edge runs through thinking mode, which burns wall-clock time on slow hardware — Qwen3.5 small models "burn 230-390M output tokens" on benchmark runs per Artificial Analysis, cited by [Pinggy](https://pinggy.io/blog/small_llms_that_fit_in_8gb_memory/). On a CPU-only 8 GB machine that latency is a real cost.

### F3. The reasoner alternate: Phi-4-mini (3.8B), MIT license

- Best small reasoner in the tier (~3 GB at Q4, 68-74% MMLU/HumanEval claims), MIT licensed, text-only — per [LocalAIMaster](https://localaimaster.com/blog/small-language-models-guide-2026), [TinyWeights](https://tinyweights.dev/posts/best-small-language-models-2026/), [Sitepoint](https://www.sitepoint.com/best-local-llm-models-2026/).
- MIT is resale-clean. Text-only is the trade: the lab's loop is currently text, so this is not disqualifying.

### F4. The edge alternate: Gemma 4 E-series (e2b / e4b)

- The current-generation successor at the small end, natively multimodal, function-calling capable, built for edge devices — per [ComputingForGeeks cheat sheet](https://computingforgeeks.com/ollama-models-cheat-sheet/) and [LocalAIMaster](https://localaimaster.com/blog/small-language-models-guide-2026).
- License flag: Gemma licenses "include some usage restrictions (e.g., prohibited use cases)" vs Qwen's Apache 2.0, per [gemma4-ai.com](https://gemma4-ai.com/blog/gemma-4-vs-qwen-3). For a product sold with hardware, that needs a legal read before v2 — flag, not blocker, for lab-internal v0.

### F5. License cautions on the rest of the field

- Llama family (3.2 3B, 3.1 8B): "carry gates worth reading twice" for commercial use, per [ComputingForGeeks open-source comparison](https://computingforgeeks.com/open-source-llm-comparison/). Not the default for a resale product.
- Qwen3.5:9b (6.6 GB, Apache 2.0, 262K context) is the named default pick for 8 GB VRAM machines per [Pinggy](https://pinggy.io/blog/small_llms_that_fit_in_8gb_memory/) — but on 8 GB SYSTEM RAM (no discrete GPU, which is the Mini's likely shape pending inventory) the guidance is to stay at 4b: "qwen3.5:4b or gemma4:e2b-it-qat will feel far better than trying to force a 9B onto the CPU."

### F6. Decision shape (no decision made here)

The choice is measured, not picked: (1) Mini inventory lands (16 GB vs 8 GB decides the tier); (2) the candidate passes the SAME observer-harness smoke test gemma3:4b passed; (3) license read completes before anything ships with hardware. Working shortlist for that test, in order: gemma3:4b (incumbent) → qwen3.5:4b (license+context upgrade) → phi4-mini (reasoner, MIT) → gemma4:e4b (edge, license read needed).

## Honesty flags

- All benchmark figures are blog-sourced secondary citations, not primary papers; none were independently run. Sizes and tags dated Aug 2026; re-verify against the live Ollama library at pull time (verified-over-claimed).
- No model turn was executed in this scrape. A benchmark row is not a continuity smoke test.
- The Mini's actual RAM is unverified until the descent inventory runs on it; all tier claims above are conditional on that.

## Close-out

Raw capture: [RAW-CAPTURE-2026-09-24.md](RAW-CAPTURE-2026-09-24.md). Fabcheck summary: all numbers traced to the linked sources at capture time; no figure cited without a source; no primary-source papers claimed for benchmark numbers (flagged as secondary). Lab-side file, working tree, push = Cat's ruling.
