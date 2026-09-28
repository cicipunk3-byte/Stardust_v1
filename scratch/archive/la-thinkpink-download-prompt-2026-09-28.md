# LA PROMPT: ThinkPink desktop download (beta), 28 September 2026

## Context

Site thread work order 4a: the ThinkPink mac download goes beneath the
PinkPromise beta on the site, with a matching beta flag, once the
GitHub release exists. The draft release is staged in the repo at
`releases/thinkpink-desktop-0-1-0-draft-release-2026-09-28.md`.

## Placement

On /pinkpromise, below the existing beta status block ("Status: beta.
Built in the open. Receipts in the repo.") and above the footer, add a
download card:

- Badge: "Beta" - same pill/badge treatment as the PinkPromise beta
  flag. Matching style, matching size, no special treatment beyond
  parity.
- Heading: "ThinkPink desktop (beta)"
- One line of copy: "The governed assistant, packaged for Apple
  Silicon Macs. Runs against your local Ollama. Free, inspectable, and
  governed by design."
- Download button label: "Download for Mac (Apple Silicon)"
- Button href: the GitHub release URL for tag `thinkpink-desktop-v0.1.0`
  on cicipunk3-byte/Stardust_v1. NOTE: the release is a draft until the
  PI publishes it. Build the button now with that href; it 404s until
  publish, which is correct and expected - do not publish the page
  until the release is live. Alternative if the platform needs a live
  href to render: point the button at the repository's releases page
  and switch it to the direct asset URL at publish time.
- Beneath the button, one small line: "SHA-256 and install steps in the
  release notes. Unsigned build; first launch needs one Terminal step."

## Do NOT

- Do not add a homepage banner or hero for this. The PinkPromise page
  owns the download; if a homepage touch is wanted later it is a
  separate ruling.
- Do not use the word "stable", "v1", or any market language. It is
  beta, tested in private family testing only; the market gate (tested
  in cloud AND with scientific partners) stands.
- No em-dashes, no personal names on this page.

## Changelog

Append to the current changelog block as its own bullet when this
publishes: "The ThinkPink desktop (beta) download went live beneath the
PinkPromise beta."

## Standing checks

No personal names outside the papers page, no em-dashes, screenshots
after pages finish loading. Report before publishing.
