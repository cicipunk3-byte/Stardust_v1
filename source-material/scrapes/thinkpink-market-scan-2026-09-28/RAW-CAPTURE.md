# RAW CAPTURE — ThinkPink market scan (run 2026-09-28, Ziggy, directed by Cecil /c)

Scope (Cecil's words, restated as questions): (1) what the market currently has like ThinkPink, (2) what gap ThinkPink fills for free, (3) product feature list. Delivered inline in thread per his request.

## Sources fetched

1. **localaimaster.com/blog/msty-vs-ollama-vs-lm-studio** — "Msty vs Ollama vs LM Studio (2026): Best No-Terminal AI App" — fetched 2026-09-28 ~15:25 ET, HTTP 200, 23,037 chars extracted (full page read; captured below in excerpt). Comparison of Msty / Ollama / LM Studio / Jan on install, model library, RAG, offline/privacy, OS support, pricing.
2. **vellum.ai/blog/best-private-personal-ai-assistants** — "10 Best Private Personal AI Assistants in 2026" (Nicolas Zeeb, Sep 7 2026) — fetched 2026-09-28 ~15:25 ET, HTTP 200, 35,995 chars (read chars 0-20000). Ranked list w/ scoring rubric (privacy architecture 30%, security model 20%, open source 15%, assistant depth 20%, setup 15%).
3. **Brave search result sets** (captured as returned):
   - "local AI assistant desktop app 2026 LM Studio AnythingLLM Msty Jan comparison privacy local LLM" — 10 results
   - "'AI companion' OR 'personal AI' desktop app local-first memory governance ethics 2026" — 10 results
   - "auditable AI assistant governance app users can inspect AI decisions log transparency 2026 product" — 8 results
   - "Jan AI pricing LM Studio free vs paid Msty subscription local AI app business model 2026" — 8 results

## Key excerpts (verbatim, for fabcheck)

### From localaimaster.com (Msty vs Ollama vs LM Studio)

> "Msty advertises zero telemetry, no forced sign-in and local-first storage. Strong privacy posture, but the app is closed source, so you trust the vendor's claims rather than the code."

> "The catch is the business model. Msty (now branded Msty Studio) has a genuinely usable free tier (split chats, knowledge stacks, web search), but advanced features sit behind Aurum, priced at $149 per user / year or a $349 per-user one-time lifetime license. It is also the only tool here that is not open source."

> "Ollama's official desktop app first shipped in v0.10 (mid-2025)... On Linux, the GUI hasn't landed yet, so Linux users still run Ollama from the terminal."

> "LM Studio is free but not open source."

> "Jan is the choice for people who insist on real open source. It's an Apache 2.0-licensed desktop app (built by Menlo Research)... It supports chatting over your own files, custom assistants with system prompts, MCP for agentic use, and connecting multiple model providers (local plus optional cloud bridges to OpenAI, Anthropic and others)."

> "Mixing in a cloud provider (which Msty makes easy) sends that traffic out — keep your sensitive chats on local models."

### From vellum.ai (10 Best Private Personal AI Assistants)

> "[Jan.ai] is primarily a chat interface with no persistent memory, no identity layer, and no proactive reach-outs."

> "[LM Studio's] a model runner and inference server, not a personal assistant — there's no persistent memory, no identity, no proactivity, no action-taking outside the chat window."

> "[AnythingLLM is] positioned more as a document intelligence tool than a personal assistant — it doesn't have persistent memory about you as a person, just the documents you feed it... Cloud hosting starts at $50/month; the free version requires self-hosting via Docker."

> "Open source is auditable, closed source is not. Claiming 'we don't store your data' is easy. Shipping code you can inspect is a different commitment entirely."

> "The 2026 Stanford HAI AI Index identified a widening gap between AI capability growth and governance readiness."

> Scoring rubric weights: privacy architecture 30%, security model 20%, open source 15%, assistant capability depth 20%, setup & accessibility 15%.

> "Vellum [the ranked product] ... Credentials live in a completely separate process and never reach the AI model... Every sensitive action shows an Allow/Deny prompt with a risk badge... Pricing: Free Base plan. Pro from $50/mo."

### From search result snippets (marked single-source, not page-verified)

- Companion-app market: Character.AI/Google settled lawsuits alleging the chatbot contributed to mental health crises among young users (digitalhumancorp.com research page, May 2026). SINGLE SOURCE, not page-verified.
- Companion platforms "optimized to keep users inside the app... business models of Replika, Character.AI, and Nomi depend on users spending more time inside the platform" (digitalhumancorp.com). SINGLE SOURCE, not page-verified.
- Jan: "over 5.5 million downloads" (vellum.ai blog + seodatapulse + premai — two-plus sources, consistent).
- AI governance tooling (Credo AI, Monitaur, Arthur AI, OneTrust): enterprise, "pricing is custom"/contract-based, serves the company's compliance need, not the individual user (cloudeagle.ai, peoplemanagingpeople.com, reco.ai roundups). SINGLE-SOURCE-EACH, directionally consistent.
- Reddit r/LocalLLaMA post (Jan 2026): individual builder hand-rolling "identity kernel — a handful of small files compiled directly into the system prompt on every turn. Persona, continuity model... memory governance policy" plus personal "ethics framework... consent requirements." DEMAND SIGNAL, hobbyist, not a product.

## Fabcheck notes

- **Vellum name collision FLAG:** the market article ranks a product called "Vellum" (vellum.ai, open-source personal AI assistant, credential isolation). Our lab's shell is also called vellum-assistant. I could NOT confirm from these pages whether they are the same project. Do not cite this article as covering our stack until checked. Flagged, not resolved.
- Pricing figures ($149 Aurum, $50/mo AnythingLLM cloud, Jan free) each trace to a single fetched page or two consistent snippets; treat as June-Sep 2026 snapshots.
- Market-size projections ($49B→$552B companions, $16.29B→$73.8B assistants) NOT carried into findings — vendor-blog projections, low value for our purpose.

## Base-verification close-out (standing directive line)

Base verification: no outreach candidates proposed or contacted in this scrape; no individuals or organizations contacted; base checks N/A for this run.
