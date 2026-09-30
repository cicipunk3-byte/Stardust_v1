# Entry 7 — Thinking-token transparency: users cannot inspect what they pay for

**Date observed:** 2026-09-24
**Reported by:** ceec (pilot directive); note drafted by Ziggy
**Status:** DRAFT, reported in chat per case-study process; files on Cat's go

## Observation

Reasoning models bill thinking tokens at full output-token rates (2-4x input), and those tokens are frequently the majority of a request's real cost ([Codeant](https://codeant.ai/blogs/input-vs-output-vs-reasoning-tokens-cost), [OpenRouter docs](https://openrouter.ai/docs/guides/best-practices/reasoning-tokens)). Anthropic returns only summarized thinking to users by default; the raw chain of thought is withheld unless a special arrangement exists, while billing continues on the full amount ([AI Outlooks](https://aioutlooks.com/thinking-tokens-explained/)). OpenAI's o-series behaves the same way: reasoning counts surfaced via usage fields, raw content not returned ([LeanLabs](https://leanlm.ai/blog/reasoning-token-costs)).

The platform observation: **the meter itemizes a component the product does not show.** A user on a subscription meter (as this lab is) can watch cost accumulate per turn without ever being able to inspect the reasoning that consumed it. The thinking output available in the interface is a summary produced by the same provider doing the billing, with no user-side verification path.

## Why it matters

- It is a transparency asymmetry with money attached: every other pay commodity with an invisible internal component still offers an itemized receipt. The rental-car comparison holds; a renter without mechanical knowledge can still open the hood.
- It blocks exactly the kind of user-side checking this lab is building toward (log-versus-thinking comparison for early detection): the comparison is forced to run on provider-summaries of the thing being measured, and that limitation propagates into any tool built on top.
- The asymmetry compounds for metered subscription users, who see aggregate credit burn but no per-token receipt at all.

## Recommendation (for Anthropic and peers)

Raw-thinking access, or at minimum an itemized per-request receipt (input, output, thinking, cache) exposed in the consumer interface, not just API usage objects. No technical knowledge should be a precondition for inspecting what one is billed for.

## Related lab material

- source-material/scrapes/cost-maltreatment/FINDINGS.md (cost mechanics, section 1)
- source-material/scrapes/ai-ethics/FINDINGS.md (calculator constraint: summary-drift limitation)
