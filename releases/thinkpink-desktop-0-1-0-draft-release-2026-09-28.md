# DRAFT RELEASE: ThinkPink desktop 0.1.0 (mac-arm64)

Status: DRAFT. Staged Sep 28, 2026 for the site thread (work order 4a).
Nothing is published. The GitHub release stays a draft and the site
button points at it only when it goes live. Publish = the PI's nod.

## Release facts

- Asset: `ThinkPink-0.1.0-mac-arm64.zip`
- SHA-256: `62cac5a72683da1b23159a85fea5b5a713ed2b3166450c49a326490479e67359`
- Target platform: Apple Silicon Mac (macOS), runs against local Ollama
- Build: real Node 22 + pnpm, electron-builder --mac zip --arm64, from
  the committed source in the handoff repo, with the quit-crash fix and
  the afterPack ad-hoc codesign hook applied. 28/28 tests green.

## Hash provenance (one filename, three builds - read before verifying)

1. `08fbc754...` - original ThinkPink 0.1.0 built on Replit Linux,
   unsigned. This is the hash in the handoff repo's committed
   CHECKSUMS.txt.
2. `1bb32a9d...` - clean-room rebuild from committed source in the
   sandbox (pre-crash-fix). Matched the CHECKSUMS artifacts-path entry.
3. `62cac5a7...` - FINAL build: quit-crash root-caused and fixed
   (28/28 tests) + afterPack ad-hoc codesign hook wired into both
   products' build configs. THIS is the release hash.

The final Threadcat-Guide-1.0.0-mac-arm64.zip is unchanged by the crash
fix: `611702e6cbe635cedd7ecfce6999a115c2857830cb7f49f008d438cc036e790e`.

Updated hashes land in the handoff repo's CHECKSUMS.txt when the
afterPack hook + crash patch land there (repo owner's nod owed).

## Install steps (unsigned build, Gatekeeper)

The app is ad-hoc signed, not Developer ID signed. First launch:

```
xattr -cr ThinkPink.app
codesign --force --deep -s - ThinkPink.app
open ThinkPink.app
```

Requires Ollama running locally. The app detects the local model and
shows an only-local-Ollama pill when connected.

## Honest limits (carry these into the release body verbatim)

- Unsigned and unnotarized. macOS may warn on first launch; the xattr
  step above clears it. Notarization needs the $99/yr Apple Developer
  account (PI's cost call, not made).
- "ZIP integrity does not prove they launch" - the handoff repo rule.
  This build is launch-verified on the Neo (Sep 28).
- Beta. Private family testing is the current gate; the market gate
  (tested in cloud AND with scientific partners) is untouched.

## Upload sequence (the PI's browser step)

1. PI nods on the publish (and on the Hindsight upstream-license
   question if still open for public distribution).
2. Upload the 62cac5a7 zip to a DRAFT GitHub release on
   cicipunk3-byte/Stardust_v1, tag `thinkpink-desktop-v0.1.0`.
3. Paste the release body (facts + honest limits above).
4. Publish the release.
5. Then (and only then) the site download button goes live - see
   `scratch/la-thinkpink-download-prompt-2026-09-28.md`.
6. Verify: fetch the release asset URL, re-hash the download, confirm
   it matches 62cac5a7.
