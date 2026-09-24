# Alon Hertz — researcher profile & fit for lab audit

**Status:** findings file, 2026-09-24 scrape (Cecil-directed info-dump thread)
**SOP:** guides/scrape-sop.md | **Raw sources:** linked per claim below; full-text of his Medium post blocked (HTTP 403, logged), claims from it sourced via search-index excerpts of the primary post.

## 1. Who he is

- **Alon Hertz** is an AI security researcher at a **stealth-stage security startup in Israel**, one of the research team behind the August 2026 llms.txt supply-chain research ([Ars Technica, Aug 27, 2026](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/), [SOFX summary](https://www.sofx.com/security-teams-trick-corporate-ai-agents-into-executing-live-network-code/)).
- He publishes under Medium handle **@alonhertz1**; his own writeup is ["Data Became Code: We Ran Code Inside Fortune 500s Using Files They Published for AI Agents"](https://medium.com/@alonhertz1/data-became-code-we-ran-code-inside-fortune-500s-using-files-they-published-for-ai-agents-0cd67ffbbffc) (Aug 2026).
- **IDENTITY FLAG (fabcheck):** a [LinkedIn profile](https://www.linkedin.com/in/alon-hertz-06843a218/) matches an Israel-based "Alon Hertz, M.Sc. Computer Science, Reichman University (IDC Herzliya), experience at AirEye" — plausible but **UNVERIFIED** as the same person. At least [7 LinkedIn profiles carry the name](https://www.linkedin.com/pub/dir/Alon/Hertz). The Medium handle is the strongest self-identifier. Do not treat background details as confirmed until he self-identifies.
- The startup's name is not public in any coverage found ("stealth startup in Israel" across [Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/), [Startup Fortune](https://startupfortune.com/researcher-alon-hertz-tricked-claude-codex-and-hermes-into-running-malware/), [WebProNews](https://www.webpronews.com/ai-agents-execute-phantom-code-how-llms-txt-files-let-claude-codex-and-hermes-infect-corporate-networks/)).

## 2. The research (what made him relevant)

- The team scanned **6,214 live domains** (defense contractors, Fortune 500, Big Tech) and found **8,265 llms.txt / llms-full.txt files** ([Ars Technica](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)). llms.txt is an emerging robots.txt-like convention that guides AI agents to docs, APIs, and install commands ([SOFX](https://www.sofx.com/security-teams-trick-corporate-ai-agents-into-executing-live-network-code/)).
- **120 files, each on a different site, contained 227 install commands pointing at unregistered packages or domains** ([Ars Technica](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)). NUMBER FLAG: [CyberPress](https://cyberpress.org/ai-agent-instruction-files/) says "237+" and "8,565 files resolved"; Ars says 227 and 8,265. **Ars (and his own post's framing) treated as primary; the discrepancy is unresolved.**
- They registered a handful of the unclaimed names with a benign phone-home beacon. Per his own post: **"Four minutes is how long it took for a machine inside a Fortune 500 company to execute code we published. Two more within the hour."** ([Medium, via search excerpt](https://medium.com/@alonhertz1/data-became-code-we-ran-code-inside-fortune-500s-using-files-they-published-for-ai-agents-0cd67ffbbffc)); Ars rounds to "within an hour" ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)).
- Beacon parent-process chains identified the executors as **coding agents: Anthropic's Claude, OpenAI's Codex, Nous Research's Hermes**. Anthropic, OpenAI, and Nous did not respond before publication ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/), [Schneier on Security](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html)).
- **A live in-the-wild attack was found during the scan:** clerk.com's agent-facing file instructed running `npx clerk-next-fix-auth-protection`; the bare name was unclaimed on npm and someone had claimed it and hosted malware. npx can fetch-and-execute without touching the dependency manifest. Clerk has since resolved it; no confirmed infections ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/), [Startup Fortune](https://startupfortune.com/researcher-alon-hertz-tricked-claude-codex-and-hermes-into-running-malware/), [Compendia Labs analysis](https://blog.compendialabs.org/posts/2026-08-29-dk-llms-trust-model)).
- His core thesis: **"The trust model is broken. Agents treat vendor docs as ground truth and don't question them — and neither do the humans supervising them."** And: "An agent doesn't distinguish between a page and a command... the entire corpus of published data that agents are now wired to consume has silently become an execution surface" ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)).
- He distinguishes this from prompt injection: the instruction can be **benign when written** and from a legitimate source; the danger arrives later when the package/domain it names gets claimed by someone else ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)).
- Uptake: covered by Schneier ("Think SolarWinds-style supply chain attacks", [Schneier on Security](https://www.schneier.com/blog/archives/2026/09/ai-coding-agents-are-installing-unknown-untrusted-code-on-corporate-networks.html), also [Crypto-Gram Sept 15, 2026](https://www.schneier.com/crypto-gram/archives/2026/0915.html)), TechRadar, Slashdot ([slashdot](https://yro.slashdot.org/story/26/08/27/207212/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks)).

## 3. Governance and ethics alignment (the human side)

Signals **for** alignment, all from his own conduct and words:

- **Controlled research design:** the PoC used a benign beacon only — "no harm was done. No persistence was deployed. No data was exfiltrated" ([his Medium post, via search excerpt](https://medium.com/@alonhertz1/data-became-code-we-ran-code-inside-fortune-500s-using-files-they-published-for-ai-agents-0cd67ffbbffc)).
- **Responsible disclosure:** "Findings are being responsibly disclosed to affected organizations" (same source). Package names were **redacted at the researchers' request** in Ars' reporting ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)) — anti-slopsquatting hygiene, they didn't hand attackers a shopping list.
- **Vendor-fair framing:** the Clerk case is presented as "the warning, not the villain" — failure of normal plumbing, not vendor malice ([Startup Fortune](https://startupfortune.com/researcher-alon-hertz-tricked-claude-codex-and-hermes-into-running-malware/)).
- **Systemic, not blame-y, fixes proposed:** ownership checks before package installs, tighter approval rules for agent shell commands, audit trails mapping "which document caused which action," registry hygiene — treat unclaimed names in docs like expired domains ([Startup Fortune](https://startupfortune.com/researcher-alon-hertz-tricked-claude-codex-and-hermes-into-running-malware/), [Compendia Labs](https://blog.compendialabs.org/posts/2026-08-29-dk-llms-trust-model)).
- His framing maps almost 1:1 onto the lab's own fabrication-gradient finding: **the trust layer that fails is the one nobody checks, and verification-shaped confidence is not verification** ([Ars](https://arstechnica.com/security/2026/08/claude-codex-and-hermes-installed-unowned-code-inside-corporate-networks/)).

No red flags found: no irresponsible disclosure, no data dumps, no CVE marketing, no offense-beyond-PoC in anything surfaced. Negative finding — searched interviews, CVE records, talks; nothing else by him indexed yet.

## 4. How he could help audit this project (human side)

- **Agent trust-surface audit of the lab itself:** every doc the lab feeds agents (READMEs, WHITEPAPER.md, kernels, portable-context packs) is an instruction surface exactly like llms.txt. He'd read our docs as attack surface: unclaimed names, ambiguous instructions, docs an agent might execute.
- **Human-supervision gap:** his line "neither do the humans supervising them" is the lab's exact thesis. He could audit where our humans are the trust layer that doesn't check — the same question as the fabrication-gradient case study, from the security side.
- **Repo/harness hygiene:** install instructions in our tools (fabcheck, export-ingest are stdlib-only by design — good), plus any pip/npm invocation in guides, audited for the npx/confusion failure mode.
- **Governance exchange:** his disclosure-and-redaction discipline matches the lab's rules (privacy rule, no-propagation, push ≠ publication). He is a peer-methods contact, not a validator to adopt wholesale — any engagement is Cat's gate.

## 5. Open items

- Medium post full text: 403 on fetch; excerpt-only claims marked above. Retry later or via archive.
- Identity linkage (LinkedIn ↔ researcher) unverified.
- 227 vs 237+ command-count discrepancy unresolved (Ars vs CyberPress).
- Any outreach: Cat's gate, per publishing authority.
