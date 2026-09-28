# LA PROMPT: ThinkPink public git card (replaces the download prompt), 28 September 2026

## Context

This REPLACES `la-thinkpink-download-prompt-2026-09-28.md` (now
archived). The release shape changed by PI ruling (/cat, Sep 28):
"archive and fresh. separate paths. archive only on git." The lab does
NOT host packaged copies. The site card SUGGESTS the tool and points
at the fresh public git and the upstream project. The Hindsight
license question is RESOLVED (upstream is MIT, receipt filed in the
lab repo's releases/ folder), so nothing blocks this card.

## Placement

On /pinkpromise, below the existing beta status block ("Status: beta.
Built in the open. Receipts in the repo.") and above the footer, add a
card:

- Badge: "Beta" - same pill/badge treatment as the PinkPromise beta
  flag. Matching style, matching size, parity.
- Heading: "ThinkPink (beta)"
- One line of copy: "The governed assistant, built in the open. Local
  models by default. Free for everyone; nobody sells this packaging."
- Two links, side by side on desktop, stacked on phone:
  - "Read the source" -> the fresh public ThinkPink repository (URL to
    be supplied by the lab before publish; build the card with a
    placeholder href of `#thinkpink-public-git` and flag it in the
    preview)
  - "Hindsight, the optional memory layer" ->
    https://github.com/vectorize-io/hindsight
- Beneath the links, one small line: "Runs against your local Ollama.
  Unsigned beta build; install steps in the repository."

## Do NOT

- Do not link to or mention any packaged zip download. The lab does
  not host binaries for this release. There is no download button.
- Do not use the words "stable", "v1", "buy", "get access", or any
  market language. No pricing, no email capture, no announcement
  copy. It is a suggested tool, not a product launch.
- No telemetry claims of any kind (nothing verified yet).
- No personal names anywhere on this page (threadcat.org rule).
- No em-dashes.

## Changelog

Append to the current changelog block when this publishes: "The
ThinkPink card went live beneath the PinkPromise beta, pointing at the
public source and its upstream memory layer."

## Standing checks

No personal names outside the papers page, no em-dashes, every claim
traceable to lab/pinkpromise.md or the release files in the repo,
screenshots after pages finish loading, cache-busted fetches for
verification. Report before publishing.
