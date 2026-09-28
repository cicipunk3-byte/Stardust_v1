# LA prompt — /thinkpink page finalize (release is live, real URLs now exist)

The public release this page points at is now real: github.com/cicipunk3-byte/SeeingPink, release v0.1.0, asset uploaded and verified.

## Job 1 — swap the placeholder hrefs on the /thinkpink page

Current placeholders and their real replacements (exact strings):

1. `#thinkpink-public-git` → `https://github.com/cicipunk3-byte/SeeingPink`
2. `#thinkpink-public-git/releases` → `https://github.com/cicipunk3-byte/SeeingPink/releases`
3. The download button (if it uses either placeholder above) →
   `https://github.com/cicipunk3-byte/SeeingPink/releases/download/v0.1.0/ThinkPink-0.1.0-mac-arm64.zip`

## Job 2 — align the download section with verified facts only

- Download: ThinkPink-0.1.0-mac-arm64.zip, 127 MB, Apple Silicon (M-series) Macs.
- The app is ad-hoc signed; built by the lab from the repository's own source.
- Requires Ollama and a local model; the plain-language setup guide (STARTUP-PLAIN.md) lives in the repository. Keep the existing citation wording from STARTUP-PLAIN-draft.md unchanged.
- If macOS asks on first launch: right-click the app and choose Open.
- Do NOT add: telemetry claims, performance claims, user counts, market/roadmap language, personal names. No em-dashes anywhere. Beta status stays visible.

## Job 3 — report, do not publish

- Keep the page in preview. Publish waits for the joint audit.
- Reply with: (a) confirmation of each swapped href with the surrounding text, (b) screenshots at 390px and 1280px width, (c) any spot where the placeholder strings above did not match anything on the page (say so plainly, do not improvise).

## Standing reminder

If any part of this prompt conflicts with the current state of the page or repository, stop and report the disagreement instead of guessing.
