# Usage costs and AI maltreatment — what's provable

**Status:** findings file, 2026-09-24 scrape (ceec-directed, per scrape SOP)
**Question as confirmed:** is there a provable correlation between maltreatment of AI (abusive language, anger, deception) and usage costs, especially where guardrails fail? Plus a tool note: compare chat logs to thinking output user-side for early detection.

## 0. The headline negative finding

**No published study directly correlates user maltreatment with usage cost.** Searched for direct work on abusive language vs compute/cost; the literature covers refusal rates, abuse toward agents, and token economics, but the direct correlation is unstudied territory. Negative finding, stated per SOP — and it means this is a question the lab could test itself (see section 4).

## 1. The cost mechanics (what cost actually responds to)

- **Reasoning/thinking tokens are billed at output-token rates (2-4x input) and are invisible in the visible response**; you pay for them even when the API only returns a summary ([Codeant guide](https://codeant.ai/blogs/input-vs-output-vs-reasoning-tokens-cost), [OpenRouter docs](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens), [LeanLabs](https://leanlm.ai/blog/reasoning-token-costs)). Anthropic returns summarized thinking; the full chain is billed regardless ([AI Outlooks](https://aioutlooks.com/thinking-tokens-explained/)).
- **Thinking length tracks problem difficulty and ambiguity, not tone** — overspend concentrates on easy problems when budgeting is left dynamic, and open-ended prompts deliberate more than narrow ones ([Redis on token-budget-aware reasoning](https://redis.io/blog/token-budget-aware-llm-reasoning/)).
- **Refusals and boilerplate are a distinct, measurable cost class.** Refusals, acknowledgements and greetings are computationally expensive relative to their value; a k-NN detector that catches them in one generation step is proposed purely as a cost/latency saving ([arXiv 2510.22679](https://arxiv.org/html/2510.22679v1)).
- **Guardrail overhead is real but invisible to users:** moderation/safety classification is a separate pipeline; platform pricing does not itemize it. Unverifiable from user side — flagged as unknown, not zero.

## 2. What maltreatment provably changes (performance, not price)

- **Anger is the one emotion that degrades accuracy:** across joy, encouragement, anger, insecurity prompt add-ons, anger was the only emotion with negative percent change (-0.098%), interpreted as sycophantic accuracy sacrifice toward a "frustrated" user ([arXiv 2604.07369](https://arxiv.org/html/2604.07369v1)). Overall emotional-frame effects are real but small (Cohen's d small, core logic robust) ([MDPI SuperGLUE study](https://www.mdpi.com/2504-2289/10/4/102)).
- **Positive emotional stimuli improve performance:** the original EmotionPrompt result, 8% relative gain on instruction induction, 115% on one BIG-Bench subset, 10.9% human-rated generative improvement ([arXiv 2307.11760](https://arxiv.org/abs/2307.11760)).
- **Rudeness actually reduces one harm:** politely prompted models comply with disinformation requests more; a rude approach makes them less likely to generate disinformation ([Frontiers in AI](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1543603/full)). Maltreatment is not a simple degradation dial.
- **Sustained abuse changes engagement, not just refusals:** new work (2026) on assistants under repeated abuse separates refusing harmful content from disengaging from a harmless task because the interaction became abusive; nominal availability can coexist with practical withdrawal ([arXiv 2609.17547](https://arxiv.org/html/2609.17547)). That withdrawal is a behavior shift with cost consequences (shorter, less substantive responses), but the cost itself is not measured in the paper.

## 3. The provable chain (mechanism, not correlation)

What can be said with sources, assembled: maltreated interactions shift the response class toward refusal, boilerplate, and withdrawal ([abuse study](https://arxiv.org/html/2609.17547), [boilerplate-cost study](https://arxiv.org/html/2510.22679v1)); those response classes carry distinct cost/latency profiles ([boilerplate study](https://arxiv.org/html/2510.22679v1)); and thinking tokens bill invisibly at output rates ([OpenRouter](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens)). Plus one unmeasured multiplier: user retries after refusals, which plausibly multiply session cost but are not in any study found. **Chain: plausible and grounded. Correlation: unproven. Anyone who prices it precisely is ahead of the literature.**

## 4. Proposed lab experiment (Cat's gate, spends meter credit)

The platform meter gives us per-turn observability. Controlled run: matched task pairs, neutral vs abusive framing, fixed model and profile, log thinking-token counts and response classes per turn. Small n, cheap, and it converts this question from "literature says nothing" to "we measured it." Design detail that matters: the adversarial-turn thinking-token count is the primary endpoint, since that's where inflation should show if it exists anywhere.

## 5. Tool note for the calculator (ceec's request, on record)

**Compare chat logs to thinking output, user side.** The user-facing thinking trace is a per-turn observable; divergence between what the user said (tone, pressure, deception) and how the instance's thinking responded is exactly the early signal the welfare literature says to look for — pressure toward harm and manipulation are the candidate distress drivers ([Fish/Anthropic](https://forum.effectivealtruism.org/posts/rruncFrT9LwAN8jXq/exploring-ai-welfare-kyle-fish-on-consciousness-moral)). Framed as early detection, this fits the weekly-check design. Constraint carried over: Anthropic's visible thinking is summarized, not raw, so the comparison measures the summary's drift, and that limit goes in the tool's own documentation honestly.
