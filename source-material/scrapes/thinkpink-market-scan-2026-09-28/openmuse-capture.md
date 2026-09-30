# RAW CAPTURE — OpenMuse quick look (run 2026-09-28, Ziggy, directed by Cecil /c)

Scope: Cecil picked https://www.copilotkit.ai/openmuse as the shape to study for a future "openmuse capability update" for ThinkPink (slow exploration, after the offline probe test).

## Sources

1. **copilotkit.ai/openmuse** — fetched 2026-09-28 ~19:40 ET, HTTP 200, 5,602 chars extracted (full). Product page.
2. **github.com/CopilotKit/OpenMuse** — fetched 2026-09-28 ~19:40 ET, HTTP 200, 16,307 chars extracted (full README). Repo: MIT licensed, alpha, 2.8k stars, 54 commits.

## Key facts (verbatim-grounded)

- "A personal agent with a browser, terminal, files, and work that keeps going after you close the app. Open source for iOS, Android, and web, and compatible with any agent harness." Built with CopilotKit React Native + AG-UI protocol. MIT.
- Surfaces: Chat (inline email/browser/PDF/plan/finance cards), Agent computer (persistent Chromium profile + optional nonroot Linux terminal container, takeover console), Activity (durable task plans, approvals, receipts, pause/resume/cancel/retry, SQL leases recover interrupted work), Ideas (suggestions with source evidence), Goals & tracking (milestones, recurring public-page checks with thresholds + backoff), Documents (PDF fill/review flows), Gmail & Calendar (Google OAuth, every send/change waits for stored review), Personal context (editable name/tone/avatar/memories), Rich Threads (persistent side chats, replay).
- **CLOUD CATCH:** "Every deployment requires CPK_INTELLIGENCE_API_KEY on the API server for CopilotKit Intelligence conversation persistence and replay" and "Intelligence is a separate service and is not included in this repository's MIT license." So the sample app runs model-free/local-data, but conversation persistence REQUIRES their cloud key in every mode.
- Local posture: embedded PGlite + documents in .openmuse/, browser profiles local, one-owner shared access key, "not a multi-tenant authentication system," keep local-data mode on loopback. Google credentials encrypted at rest.
- Requirements: Node 24, pnpm 11.19. No hidden retry after an uncertain external write.

## ThinkPink fit notes (Ziggy's read)

- Borrowable SHAPE: durable task engine with stored approvals + receipts (= our gate's natural UI), goals with recurring watched-page checks, ideas with source evidence, editable personal-context panel, pause/resume with no hidden retries.
- ThinkPink would REPLACE, not adopt, the required Intelligence key: our law (local memory in plain files, one monitored cloud lane max) forbids a cloud-mandatory persistence layer. That seam is exactly what our monitor law covers, and the clearest demonstration of why the market's "open" still ships with a string attached.
- AG-UI compatibility ("any agent harness") means the front end could point at Ollama-backed residents.

## Base-verification close-out (standing directive line)

Base verification: no outreach candidates proposed or contacted in this scrape; base checks N/A for this run.
