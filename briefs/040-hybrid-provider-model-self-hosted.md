# Brief 040: hybrid provider model for the self-hosted loop  DOI: 10.5281/zenodo.22870569

_Date: 2026-09-23_ · _Written for: the PI's gate_ · _Status: PROPOSAL at the gate. Build-lane directive (Cecil, Sep 23): evaluate BYOK vs local for the Mac Mini self-host, file for ruling before any provider is configured._

## TL;DR

The lab can self-host the full assistant runtime on the Mac Mini using the same codebase it runs on now (fork audited clean, identical to upstream, MIT). The runtime supports both BYOK provider keys and Ollama local models through one provider abstraction, so the real question is routing, not choice. This brief proposes a hybrid: Ollama as the default lane for background work, a BYOK frontier key as an opt-in lane for research-critical turns. Ruling requested on the routing policy and on what data may ever touch a third-party provider endpoint.

## Established facts

All facts below were verified in the fork's source on Sep 23 (local clone of cicipunk3-byte/vellum-assistant at ae47e199, identical to upstream main, 0 ahead / 0 behind, MIT license).

- Ollama is a first-class, keyless provider: `assistant/src/providers/ollama/client.ts` extends the OpenAI-compatible chat-completions provider, default base URL `http://127.0.0.1:11434/v1`; the model catalog entry states "Run local models via Ollama. No API key required."
- The provider directory carries at least: anthropic, openai, gemini, openrouter, fireworks, together, baseten, atlascloud, minimax, vercel-ai-gateway, ollama, vellum, and a platform-proxy lane. Call-site routing (`call-site-routing.ts`) and a weak-model lane (`weak-open-model.ts`) exist in the same directory.
- The local hosting docs state the tradeoff directly: local assistants run only when the host machine is awake; Docker and Apple Container isolation modes are listed as "coming soon"; native mode is available now.
- The paired-device path serves the web app from the host's own tunnel address; the docs state conversations never pass through Vellum's servers on that path.
- Lab cost data (brief 037 and the Sep 2026 usage analysis, account-wide): the main agent lane is the dominant cost; memory-selector and retrospective background lanes are a material minority share. The platform's own code separates call sites the same way.

## Working material

Cost and privacy stakes, from the standing record:

- Pre-first-grant cost discipline is lab law. A BYOK key bills per token with no platform grant above it. Ollama on the Mini is free but bounded by the machine's RAM and model quality (the harness record documents 4b-class confabulation rates).
- The local-first conviction (her files lost in a cloud platform, recovered into a git repo she owns) argues against routing lab record content through third-party endpoints by default.
- The Sep 2026 usage audit already operates on a strong/weak lane model (chat profile vs cost-optimized pin for the memory L2 selector). The hybrid proposal mirrors that shape at the provider layer.

## Proposal (for ruling)

1. Ollama is the DEFAULT provider on the self-hosted Mini. Background lanes (memory consolidation, sweeps, filing work, heartbeat) run local, always, no key involved.
2. A single BYOK key may be configured as an opt-in lane for named research-critical turns. Default remains local. No background lane ever touches the BYOK lane.
3. Data rule: PERSONAL_CONTEXT.md contents and anything under the family-facts protection rule never go to a third-party provider endpoint, in any lane, in any prompt. This restates existing law; the proposal adds that provider routing cannot bypass it.
4. The availability tradeoff is accepted for the Mini (it sleeps, the loop sleeps) until the record says otherwise.

## Open questions

1. Does the self-hosted runtime expose per-call-site provider configuration through config files alone, or does routing require code changes? (Verify before implementation; source reading suggests call-site routing exists but the config surface is unverified.)
2. Does the weak-model lane (`weak-open-model.ts`) do anything in local mode, and is it a natural home for the Ollama default?
3. Which single provider would the BYOK lane use if approved, and who holds that key under the credential rules?

## What to produce

PI ruling on items 1 through 4 of the Proposal. If adopted, the build lane configures Ollama first, verifies a full turn, and only then asks about the BYOK lane.
