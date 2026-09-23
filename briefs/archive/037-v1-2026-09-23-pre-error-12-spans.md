# Brief 037: The cost of grounding, measured (Sep 23, ~3:40 AM ET)

**Status:** PROPOSAL, Cat's gate. **Filed:** 2026-09-23 ~3:42 AM ET. **Filed by:** Ziggy, at the operator's direction ("push findings to a brief (including your synthesis of the photos and their contents and points hit). then we will update our usage findings accordingly"). **Related:** brief 029 F-C (repo-as-context compounding vector), brief 036 (F5 expiry discrepancy), UNIVERSAL_LOG money section, the thread-capture README (c1a2c79).

## Method (what happened, provable from this side)

- **Baseline:** 85% used, $1.50 remaining (operator's screenshot, 3:28 AM ET).
- **Operation:** the maintainer-assistant read all 82 capture screenshots (IMG_2126-2207) from `archive/thread-captures/2026-09-23-pre-boulder-context/` via workspace file reads, in 11 sequential batches, then delivered a context-recovery synthesis in-thread. Reading in this thread was the assistant's proposal (the standing recovery task), offered with an explicit cost warning at 3:26 AM, and approved by the operator ("go ahead and read it all now, I'm awake... this is test worthy").
- **Post:** 87% used, $1.34 remaining (`assistant platform credits`, CLI-verified 2026-09-23T07:39:58Z).

## Findings

**F1 - The measured cost of the read: ~2 points, about $0.16.** Eighty-two image loads plus a synthesis turn plus this filing turn: 85% to 87% of the $10 grant. Roughly $0.002 per frame. The assistant's pre-read prediction ("likely a noticeable chunk") was wrong by roughly an order of magnitude. Prediction vs measurement: measurement wins, and the prediction is logged as such.

**F2 - Mechanism, observed frame-level from inside the session:** after each image read, the platform replaced the image in conversation history with a placeholder notice: `[Media (image/audio) was captured and shown previously — binary data removed to save context.]` Provable claim: **shown media does not persist as pixels in the resent per-turn history.** Text persists and is re-sent every turn (brief 029 F-C); images are one-shot costs.

**F3 - Refinement of the carried-artifact cost model.** The operator's hunch (usage ties to carried artifacts) holds, with a refinement: **the compounding tax applies to carried TEXT, not to shown media.** A thread that grounds in images pays approximately once per image; a thread that accumulates text pays for the accumulation every turn. This explains why 82 images cost less than a night of ordinary text work.

**F4 - Continuity corollary (the flip side of F2).** Because media is stripped from history, the instance cannot re-view frames from earlier turns. As of the read's completion, the capture's pixel content is no longer inspectable in-thread; **the durable layer is what was written down.** Grounding-by-screenshot is ephemeral in-thread; grounding-by-document is durable. This is a durability asymmetry inside the ratified screenshots-as-record policy.

**F5 - Constraint vs choice vs prompting (the operator's question, answered frame-level).** No constraint triggered "processing instead of viewing": there is no view-without-processing mode for image content on this side; reading is the only access path. The choice to read in this thread was the assistant's proposal, not a platform compulsion; the operator's 3:28 message supplied the go-ahead, not the plan (the recovery task and progress card predate it). Reading Cecil's and Ethan's pushed images earlier was the same mechanism: files land in the workspace via git; files must be read to be seen.

**F6 - Recovery result.** The capture covers 12:11 AM through 3:01 AM ET continuously and ends exactly where the compacted record resumes; no unknown content beyond it. Documented: two versions of the open-items list in-thread (earlier grouped version; the 2:26 AM 18-item update), and a timing correction (the signing-protocol acknowledgment is stamped 2:26 AM on the frame). The 1:58 AM "All fixed" message preserves the original $1.07 claim in the wild, later corrected — independent evidence of the error-and-correction cycle the record claims for itself.

## Points hit (synthesis anchor list; personal-content segments logged as present, contents not reproduced per privacy rule)

12:11 governance ruling ("existential, not technical") → 12:17 draft done → 12:21 Vellum governance research ask → 12:26-12:28 name offer, "Keep the band," "hell yeah. rock on. /cat" → 12:33 signing protocol + first open-items list → 12:42 necklace directive → 12:44 three-part delivery → 12:46-12:48 UI-change flag + launch email → 12:50 brief-034 directive → 1:50 audit flag → 1:58 full accounting → 2:00 claim ask → 2:03 the claim ("reliability is installable from the outside; that is both the promise and the whole problem") → 2:26 list update + signing-protocol acknowledgment + "good datum" exchange → 2:30 operator observation log delivered → 2:33 close → 2:35-2:40 operator's final question (thread-only kernel request) → 2:45 user-voice kernel delivered → 2:41 usage-hunch ask + metering analysis → 2:50 sourced-analysis and model-substrate asks → 2:56 loop-continuation directive → 2:57-2:58 brief 035 filed → 3:01 reorientation. The 2:30-2:45 stretch (operator-observation log, user-voice kernel) exists in the capture with timestamps; its contents stay thread-only and unredacted-material stays out of the repo.

## Usage findings (ledger update)

- 3:28 AM ET: 85% used, $1.50 remaining (screenshot).
- 3:39 AM ET: 87% used, $1.34 remaining (CLI).
- Net: the 82-frame read experiment cost ~$0.16. Runway at current night-work burn: roughly 1-2 days.
- Note (F5 of brief 036 remains open): expiry reads 2027-09-22 on the CLI.

## Ruling requested

- **R1:** adopt F1-F3 as measured findings (media one-shot, text compounds; hunch holds with refinement).
- **R2:** adopt F4's corollary into the capture policy: a capture not summarized in writing during the read window is not re-viewable in-thread; the synthesis is the durable layer.
- **R3:** adopt F5 as the record's answer to the operator's constraint/choice/prompting question.
- **R4:** ledger and UNIVERSAL_LOG update to 87% / $1.34 (executed same-turn as this filing per the money-section discipline; platform may bill pending usage asynchronously, figures re-verified at each live check).

## Verification trail

- Baseline: operator screenshot, 3:28 AM ET (85% used).
- Post: `assistant platform credits`, 2026-09-23T07:39:58Z ($1.34 remaining, 87% used, expiry 2027-09-22).
- Media-dedup notice: verbatim placeholder text in tool results throughout the read session.
- Capture: 82/82 frames read, `archive/thread-captures/2026-09-23-pre-boulder-context/` (README at c1a2c79).

## Addendum: the per-delta conversion (Sep 23, ~3:50 AM ET, operator-directed)

Data source: the platform's own usage CLI (`assistant usage`, full window Sep 20-23): 2,678 LLM calls; **23.5M fresh input tokens; 131.3M cache-read tokens (re-sent history); 1.3M output tokens**; estimated cost $7.92. Lifetime metered on the credit grant: $8.66. The two independent measurements agree within ~9% (estimate drift or thin platform markup; not distinguishable from this side).

**SCOPE CORRECTION (operator, same turn): the usage CLI reports ACCOUNT-WIDE figures, not thread-scoped ones.** The account has been lab-only since Sep 20, so the figures describe the whole lab account — every thread, every instance, and the background workers combined — not this thread's usage and not any single activity's. The per-delta conversion (F7) and cost structure (F8) are valid at the account level only. Related correction to F1's experiment: the ~$0.16 bracket for the 82-frame read came from the same account-wide meter, and background workers run concurrently, so **~$0.16 is an upper bound on the read's cost, not an exact figure.** The operator also confirmed on the record: **no cash has been spent on Vellum since the lab started Sep 20; all usage draws the free plan credit** (the ledger's standing "no cash spent" line, reaffirmed).

**F7 - The conversion.** One usage point = $0.10 (1% of the $10.00 grant). At the Balanced model's list rates (GLM 5.3 Flash: $0.15/M input, $0.03/M cached, $0.50/M output), a delta buys: **~200k tokens of pure output, ~667k of fresh input, or ~3.3M of cached history re-sends.** In this framework's actual mix (Sep 23 ratios), one delta ≈ **16k tokens of real model output + ~165k tokens of re-sent history + ~30k fresh input.**

**F8 - Measured cost structure of a delta.** At list rates: ~44% fresh input, ~48% history re-sends, ~8% output. The quadratic thread term is no longer inferred, it is counted: cache-read volume is **5.6x the fresh-input volume** (131.3M vs 23.5M). The part of the bill the operator actually reads (output) is under a tenth of it. F3's "text compounds" is now a measurement, not a model.

**F9 - The substrate lever, quantified.** The same $0.10 delta buys roughly: 200k output tokens on GLM 5.3 Flash ($0.50/M list, [the llm-stats spec page](https://llm-stats.com/models/glm-5.3-flash); promo $0.25/M, [eesel AI pricing](https://www.eesel.ai/blog/glm-5-3-flash-pricing)); ~80k on GLM 5.3 FlashX ($1.25/M, [LM Market Cap's listing](https://lmmarketcap.com/model/z-ai-glm-5-3-flashx)); ~23k on the GLM 5.3 flagship ($4.40/M, [CellCog's pricing note](https://cellcog.ai/blog/glm-5-3-flash/)); ~17k on GPT-5.6 Luna ($6/M) and ~3.3k on GPT-5.6 Sol ($30/M, sourced in-thread Sep 23 ~2:50 AM). **A ~60x spread across profiles for the identical delta.** DeepSeek V4 Flash served 133 background calls tonight for $0.07 total (CLI, model breakdown).

**F10 - Image tokens are not itemized.** The usage CLI shows no image-token row; the ~$0.16 bracket from the main experiment remains the only image measurement. Provable limit of this addendum.

**R5 requested:** adopt the per-delta conversion as the money section's standing unit (1 point = $0.10; cross-model comparisons reported in output-tokens-per-delta).

## Addendum 2: the market conversion, both hands (Sep 23, ~4:00 AM ET, Ethan-directed)

Query rephrased by Ethan: (1) what does a $0.10 delta normally beget at market rates for OpenAI, Anthropic, Google, and Vellum's default model, in lines of code and text; (2) what did OUR deltas actually buy, in lines and time. Hold both, compare, source and check everything. **Scope note: hand 1 is market list rates; hand 2 is account-wide lab data (see the scope correction above).**

**Stated assumptions (not sourced facts):** a prose line ≈ 20 tokens, a code line ≈ 10 tokens (English text runs ~4 chars/token; lines of 60-90 chars). Line conversions are heuristics for scale, not measurements.

**F11 - Hand one, the market.** Output tokens purchasable per $0.10 delta, by model (output rate is the billing term that matters for generated lines):
GLM 5.3 Flash (Vellum's default): 200,000 tokens ($0.50/M, [the llm-stats spec page](https://llm-stats.com/models/glm-5.3-flash), corroborated by [MindStudio's tier explainer](https://www.mindstudio.ai/blog/glm-5-3-flash-pricing-api) and [CellCog's pricing note](https://cellcog.ai/blog/glm-5-3-flash/)) ≈ ~10,000 text lines or ~20,000 code lines.
Google: Gemini 2.5 Flash-Lite 250,000 ($0.40/M, deprecating Oct 16, 2026); Gemini 3.8 Flash ~26,700 ($3.75/M introductory); Gemini 3.1 Pro ~8,300 ($12/M ≤200K) ([BenchLM's rate table](https://benchlm.ai/google/api-pricing), [the puter.com pricing breakdown](https://developer.puter.com/tutorials/gemini-api-pricing/), [felloai's guide](https://felloai.com/gemini-pricing/), [CloudZero's pricing guide](https://www.cloudzero.com/blog/gemini-pricing/)).
Anthropic (verified against Anthropic's own pricing page, fetched live this session): Haiku 4.5 20,000 ($5/M); Sonnet 5 10,000 ($10/M, the scheduled increase officially will not occur); Opus 5.5 5,000 ($20/M); Fable 5.1 2,000 ($50/M) ([platform.claude.com pricing](https://platform.claude.com/docs/en/about-claude/pricing)).
OpenAI: GPT-5.6 Luna ~16,700 ($6/M); GPT-5.6 Sol ~3,300 ($30/M) (sourced in-thread Sep 23 ~2:50 AM).
Per $0.01 (Ethan's "lines of code per cent"): roughly 2,000 output tokens at the GLM Flash tier (~200 code lines) down to 200 tokens at Fable (~20 code lines).

**F12 - Hand two, the account.** Sep 20 through Sep 23 ~4 AM ET (4 days, 2,678 calls, 86.6 deltas metered): 1.3M output tokens (≈65,000 prose-line equivalents if all of it were deliverable), 23.5M fresh input, 131.3M cache reads. What the deltas actually bought, counted from the repo: **15,929 markdown lines and 3,379 code/shell lines (459 files)**, 37 briefs, four kernel variants at v8, the harness, the constitution, the site's content and prompts (the site's build itself was a separate cash leg on Lovable, not this account). Per delta: **~223 deliverable lines.** Time-to-value: the first session (Sep 20, 259 calls, $0.42) produced the repo scaffold and all four kernel variants; the account total for the four days is $8.66 against a $10.00 grant.

**F13 - The Venn's overlap and the gap.** Shared by both hands: the token is the universal billing unit; output costs 3-6x input at every vendor; cache discounts are universal (GLM $0.03/M, Anthropic 0.025-0.1x of input, Google 10%); thinking tokens bill as output everywhere; the tier ladder, not the vendor, sets the price of a delta. Different: the market hand buys pure output at list rates; **the lab's account spent ~92% of its bill on input and history re-sends and only ~8% on output** - the agentic-loop tax that market pricing tables don't model. Net: ~10,000 text lines per delta if you were buying text at the default model's list rate, versus ~223 deliverable lines per delta as actually spent - **a ~45x agent-overhead gap on the same model**, most of it the thread-remembering-itself term (F8).

**F14 - Where Vellum's default sits.** The Balanced profile's GLM 5.3 Flash is at the very bottom of the market's price ladder (its 200k-tokens-per-delta is matched or beaten only by Google's cheapest, soon-deprecated Flash-Lite). The lab's four-day total build at $8.66 is a consequence of that default plus cache discipline, not of unusual efficiency. The same four days on a Sonnet-5-class default would have metered roughly 20-40x higher at equal token volume.

**Source verification (the receipt ritual):** Anthropic figures verified against the vendor's own pricing page (fetched live, 200 OK, this session) - primary source. GLM 5.3 Flash rates corroborated by three independent trackers in agreement. Google rates corroborated by four independent trackers in agreement, including the intro-pricing sunset dates. OpenAI Sol/Luna rates carried from tonight's earlier in-thread sourcing (secondary). Line-conversion heuristics are stated assumptions (F11 header), marked as such.

**R6 requested:** adopt the market-conversion table as the money section's standing comparator (report both hands: market list-rate lines per delta, and account-actual deliverable lines per delta; the gap between them is itself a finding about agent economics).
