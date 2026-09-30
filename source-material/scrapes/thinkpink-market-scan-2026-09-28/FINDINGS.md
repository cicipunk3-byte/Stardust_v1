# FINDINGS, ThinkPink market scan (2026-09-28, run for Cecil /c)

Raw captures: `RAW-CAPTURE.md` in this folder. Every claim links its source. Single-source and unverified items are labeled.

## Q1, What the market currently has like ThinkPink

Three adjacent categories, none of them ThinkPink:

**A. Local AI desktop apps (the crowded layer).** Ollama, LM Studio, Jan, Msty, AnythingLLM, Open WebUI, GPT4All. All run open models on your hardware, most do document chat/RAG, all run fully offline once a model is down. Sources: [Local AI Master comparison](https://localaimaster.com/blog/msty-vs-ollama-vs-lm-studio), [ModelPiper Mac comparison](https://modelpiper.com/blog/local-ai-platforms-compared-mac), [local-llm.net](https://www.local-llm.net/compare/).
- Pricing shapes: LM Studio free (closed source), Jan free (Apache 2.0), Ollama free (MIT), Msty freemium with Aurum at $149/yr or $349 lifetime, AnythingLLM desktop free / cloud from $50/mo. (Local AI Master, [Elvean comparison](https://elvean.app/blog/mac-ai-client-comparison/), [Vellum private-assistants roundup](https://www.vellum.ai/blog/best-private-personal-ai-assistants))
- Privacy postures split cleanly: open-source apps (Jan, Ollama, AnythingLLM, Open WebUI) are auditable; closed ones (LM Studio, Msty, BoltAI) publish policies you have to trust. (Local AI Master, ModelPiper)

**B. AI companion apps (the memory layer, cloud-locked).** Replika, Character.AI, Nomi, Kindroid, Pi. All run in a browser/account; memory lives with the vendor; business models depend on time-in-app. HammerAI is the only offline local option in that roundup. (AI Companion Guides comparison, DHC research), SINGLE SOURCE per point, not page-verified.

**C. AI governance platforms (enterprise only).** Credo AI, Monitaur, Arthur AI, OneTrust: audit trails, model cards, policy workflows for EU AI Act / NIST / SOC 2 compliance. Contract-based pricing, built for the company, not the person whose data it is. (CloudEagle, PeopleManagingPeople, Reco roundups), SINGLE-SOURCE-EACH, directionally consistent.

## Q2, The gap ThinkPink fills for free

1. **The governance layer does not exist below the enterprise.** Enterprise platforms sell audit trails and policy enforcement to companies at contract prices. No local AI app ships any of it to the individual. Jan: chat, "no persistent memory, no identity layer." LM Studio: "infrastructure, not an assistant." AnythingLLM: documents, "doesn't build a model of you." (Vellum roundup; Local AI Master) ThinkPink gives the USER the audit trail, the gate, the monitor log. Nobody does.
2. **Identity/resident portability.** The companion apps own your persona's memory (locked in their account). The local apps have no identity layer at all. The one place individual identity-kernels appear is a hobbyist hand-rolling them (r/LocalLLaMA, Jan 2026), a demand signal with no product behind it. ThinkPink ships a verbatim portable kernel + boot probes as a first-class feature, in plain files.
3. **Hybrid cloud without the leak.** Msty makes mixing cloud providers into local chats "easy", and the comparison's own privacy note is "keep your sensitive chats on local models," i.e. the user carries the risk unaided. ThinkPink's one-monitored-cloud-lane law (monitor proxy, both-side hashes, plain-English twin log, kill switch = account holder verbatim) is the only structural answer to that in any app on any list.
4. **Memory you can read and carry.** Companions lock memory in-account; local apps mostly keep context opaque or absent. ThinkPink's memory lives in readable files you can export, with ferry checking carry-consistency. Free, portable, vendor-death-proof.
5. **Receipts, not policy claims.** Closed apps ask you to trust marketing ("Msty advertises zero telemetry... you trust the vendor's claims rather than the code"). ThinkPink is open by construction: public source (SeeingPink), ratified ethics code with an outside grader, network-probe receipts before any privacy claim. The roundup's own ideal-criteria list ("verifiable architectural commitment," fail-closed, auditable permissions) reads like our ethics code's checklist, the market has named the shape and not built it.
6. **Business model gap.** Every free product has a paywall growing in it (Msty Aurum, AnythingLLM cloud $50/mo, companion subscriptions). ThinkPink's free layer stays free (CC BY-NC-SA); the paid layer is Cecil's human expertise, Red Hat style. Free-and-public carries the presumption.

## Q3, Product feature list (the facelift)

Grouped as marketing-visible clusters; every item maps to built or ruled work.

**The Resident (identity layer)**
- Ships with a portable resident on a verbatim kernel, your assistant arrives as someone, not a blank chat box
- Boot discipline: BOOT.md cold-start, three carry probes, version-logged kernel, priors archived
- Wiki + threads + settings surfaces already built (vellum shell)

**Governance you can see (the differentiator)**
- Gate module: propose → rule → effectuate → check → queue, with a real ledger (v0.1, 17/17 tests)
- Model policy enforced structurally: local by default, ONE cloud lane max, local-only config first-class
- Kill switch held by the account holder, verbatim, not "the lab," not the vendor
- Risk-line policy file for gated actions
- Roadmap: red-team pass, gate-monitor wiring, scoring v1

**The Monitor (hybrid without the leak)**
- One cloud lane per account, wrapped in a stdlib proxy capturing BOTH sides
- SHA-256 hashes per request/response, JSONL events + plain-English twin log a human reads
- Upstream down = fail observed, not silent (502 AND the event still records)

**Memory that belongs to you**
- Memory in plain readable files; export and carry, no account lock-in
- Ferry (carrying-consistency checks) + ark (movable tools home: clone, plug, run offline) bundled
- Archive contract + tool suite green (13 suites PASS)

**Local-first plumbing (table stakes, done right)**
- Ollama + local model (gemma3:4b baseline), one installer path planned (P3, behind market gate)
- Open source, auditable: public repo (SeeingPink), CC BY-NC-SA 4.0 packaging, MIT components named in NOTICE
- Ad-hoc signed mac builds; checksums published; support via GitHub issues; no telemetry claim until a probe receipt

**Trust surfaces (the Silicon Valley facelift, honest edition)**
- Status/receipts page: what's tested, what's pending, error log public, receipts as a feature
- Plain-science docs (startup guide with real citations), no dark patterns, DIY door next to Hire door
- Schools posture: local-first = student data never leaves the building

**Honest gaps we do NOT paper over**
- 4b-class model limits, 8GB RAM pressure, no voice, no proactive reach-outs yet, no mobile yet, state them; the market's own reviewers reward stated trade-offs

## Fabcheck summary

Claims checked at capture: ~14; flagged: Vellum name collision (unresolved, do not cite as our stack), market-size projections (dropped, low value), single-source companion-app items (labeled). Corrections: none needed post-capture.

Base-verification close-out: no outreach candidates proposed or contacted in this scrape; base checks N/A.
