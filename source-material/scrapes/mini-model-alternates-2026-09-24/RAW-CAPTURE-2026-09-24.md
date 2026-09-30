# RAW CAPTURE — 2026-09-24 — Mini model alternates scrape

Scope confirmed: alternates to gemma3:4b fitting the Renewable Center model (license-clean for hardware resale, Mini-sized, continuity-serving, loop-capable). Two web search rounds, same turn as findings. No outreach; no base-verification constraints triggered (no people contacted or proposed).

| Round | Query | Sources captured |
|---|---|---|
| 1 | best small LLM 2026 8GB RAM Ollama 4B class agent function calling Qwen3 Phi-4-mini Gemma 3 comparison | localaimaster.com/blog/small-language-models-guide-2026 (Aug 3, 2026); promptquorum.com/local-llms/best-beginner-local-llm-models (Aug 28, 2026); computingforgeeks.com/ollama-models-cheat-sheet/ (Aug 4, 2026); pinggy.io/blog/small_llms_that_fit_in_8gb_memory/ (~1 wk old); morphllm.com/best-ollama-models (Aug 21, 2026); sitepoint.com/best-local-llm-models-2026/ (Mar 13, 2026); tinyweights.dev/posts/best-small-language-models-2026/ (Jul 19, 2026) |
| 2 | Qwen3 4B Apache 2.0 license context window 32k Ollama vs Gemma 3 4B license context | gemma4-ai.com/blog/gemma-4-vs-qwen-3 (Apr 7, 2026); computingforgeeks.com (cheat sheet + open-source-llm-comparison, Mar 2026 test table); huggingface.co/blog/daya-shankar/open-source-llms (May 14, 2026); codersera.com/blog/gemma-3-vs-qwen-3... (Aug 18, 2026); baeseokjae.github.io (May 8, 2026); morphllm.com (again) |

Key captured claims (verbatim or near-verbatim, source-attributed in FINDINGS.md):

- "For 8GB hardware, Phi-4-mini (3.8B) is the best small reasoner (~3GB VRAM at Q4), and Gemma 3 4B is the best pick if you need multimodal/vision or 140+ languages. All three run free in Ollama." — LocalAIMaster
- "qwen3.5:4b (3.4GB), gemma4:e2b-it-qat (4.3GB), nemotron-3-nano:4b (2.8GB), or phi4-mini:3.8b (2.5GB)" for 8GB system RAM — Pinggy
- "Qwen3.5-9B at Q4_K_M (ollama pull qwen3.5:9b, 6.6GB) - the default pick. Apache 2.0, 262K context, native vision" — Pinggy
- "If your 8GB is total system RAM (no discrete GPU) ... will feel far better than trying to force a 9B onto the CPU." — Pinggy
- "Qwen 3's Apache 2.0 license (for models up to 32B) is one of the most permissive in open source — no strings attached. Gemma 4's license is similar but includes some usage restrictions (e.g., prohibited use cases)." — gemma4-ai.com
- "Gemma 3 ... Context was 32K on the 1B and 128K on the 4B/12B/27B" — codersera
- "phi4-mini ... MIT licensed" (listed beside gemma3:4b "multimodal, best coding at this tier") — TinyWeights
- "Kimi K3 and the Llama family carry gates worth reading twice." — ComputingForGeeks open-source comparison
- "the Qwen3.5 small models burn 230-390M output tokens to complete the index ... Thinking mode is where the quality comes from, and it costs you wall-clock time on slow hardware." — Artificial Analysis via Pinggy
- "3B to 4B land in the 180 to 290 [tok/s] band" (recent desktop hardware, Ollama 0.30.x+) — ComputingForGeeks cheat sheet

Retrieval notes: all results are blogs/aggregators, none primary (no model cards pulled); benchmark figures treated as secondary claims and flagged as such in FINDINGS. Model landscape moves monthly — re-verify tags/sizes against ollama.com/library at pull time. Capture command: web_search ×2 (Brave provider), no page fetches needed; quotes taken from search-result extracts.
