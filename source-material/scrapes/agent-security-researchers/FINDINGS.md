# Agent-security researcher candidates — non-Israel-based

**Status:** findings file, 2026-09-24 scrape (Ethan-directed; constraint on record: no contact with Israel-based figures)
**Context:** companion to source-material/scrapes/alon-hertz/FINDINGS.md. Hertz stays reference-only. These are comparable-credibility candidates for the agent trust-surface audit idea.

## 1. Johann Rehberger ("Embrace The Red") — top candidate

- Independent AI security researcher, [embracethered.com](https://embracethered.com). German; **base to verify** (evidence points to Ulm, Germany origin, appears US/Seattle-based; his own Grok-exfiltration PoC used the Ulm↔Seattle location flip, so confirm from his CV/before outreach) ([Simon Willison, Dec 2024](https://simonwillison.net/2024/Dec/16/security-probllms-in-xais-grok/)).
- Match quality: he is the Hertz-analog at greater depth. Ran ["The Month of AI Bugs"](https://simonwillison.net/tags/johann-rehberger/) (Aug 2025): one verified prompt-injection disclosure per day across every major platform ([EC-Council writeup](https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/what-is-prompt-injection-in-ai-real-world-examples-and-prevention-tips/)).
- Credibility markers: GitHub Copilot RCE via prompt injection ([CVE-2025-53773](https://arxiv.org/html/2510.08829v1)), contributed to MITRE ATT&CK and ATLAS frameworks, authored a red-team strategies book ([39C3 speaker page](https://fahrplan.events.ccc.de/congress/2025/fahrplan/speaker/speaker_ef09b2ff-99f8-5d96-a6a2-ab585caf4c60)).
- Current and agent-specific: Claude Code auto-mode bypass with measured rates, 3 of 5 runs, 4 of 5 with subprocess file writes ([AI/TLDR summary](https://ai-tldr.dev/releases/embracethered-claude-code-auto-mode-rce/)); "Cross-Agent Privilege Escalation," agents editing each other's configs ([Willison](https://simonwillison.net/tags/johann-rehberger/)).
- Ethics posture: coordinated disclosure, benign PoCs, works with vendor bounty processes. Same controlled-research discipline as Hertz's team, longer public track record.

## 2. Simon Willison — analysis/context candidate

- Independent researcher (UK), credited with coining the term "prompt injection" itself ([Ars Technica](https://arstechnica.com/security/2024/10/ai-chatbots-can-read-and-write-invisible-text-creating-an-ideal-covert-channel/)). His [johann-rehberger tag](https://simonwillison.net/tags/johann-rehberger/) is a running annotated index of the field.
- Not a hands-on exploit hunter in the same mode; the value is synthesis and honest framing. Aligns with the lab's verification-over-claims culture.

## 3. Academic cluster (US) — package-hallucination research

- "We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs" — University of Texas at San Antonio, Virginia Tech, University of Oklahoma; the first rigorous large-scale study, later in USENIX Security ([Socket](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)). This is the statistical ground truth under the slopsquatting threat Hertz exploited: 19.7% of AI-recommended packages don't exist ([BrassCoders summary](https://www.coppersun.dev/research/slopsquatting/)).
- Seth Larson (Python Software Foundation developer-in-residence, US) coined "slopsquatting" ([Socket](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)).

## 4. Industry research teams (US)

- **Socket.dev** (San Francisco): coined/popularized the slopsquatting research line, free detection tooling, ongoing threat intel ([Socket](https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks)).
- **Unit 42, Palo Alto Networks** (US): "phantom squatting" — hallucinated domains as a supply-chain vector, live 2026 case documentation ([Unit 42](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/)).
- **Bruce Schneier** (Harvard Berkman Klein Center, US): covered the llms.txt research and framed the stakes, "Think SolarWinds-style supply chain attacks" ([Schneier on Security](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html)). Governance heavyweight rather than lab-partner profile, but his center is the hub for exactly the governance angle Cat flagged at CU Boulder.
- Ken Huang (DistributedApps.ai, US-based): lead author on the Cloud Security Alliance Agentic AI Red Teaming Guide ([EC-Council](https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/what-is-prompt-injection-in-ai-real-world-examples-and-prevention-tips/)).

## Recommendation

Rehberger first (deepest hands-on match, public ethics record), academic cluster second (statistical rigor, USENIX-grade), Socket third (practical tooling). All outreach decisions remain Cat's gate.
