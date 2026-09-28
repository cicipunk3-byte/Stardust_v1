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

## License clearance (RESOLVED Sep 28, receipts)

The handoff README's caution ("do not make the ThinkPink desktop build
public while its Hindsight license question is open") is RETIRED. The
upstream is public and permissive:

- Hindsight: github.com/vectorize-io/hindsight (Vectorize AI, Inc.),
  public repo, LICENSE = MIT (Copyright (c) 2025 Vectorize AI, Inc.).
  Confirmed against the repo LICENSE file AND the pinned wheel
  (hindsight-embed==0.10.1, License-Expression: MIT).
- MIT permits redistribution and sale by anyone. No restriction flows
  upstream into ThinkPink.

Layered licensing for the release (PI ruling, Sep 28, /cat):

- ThinkPink packaging layer: CC BY-NC-SA 4.0. Free for all to use,
  share, and rebuild; commercial use excluded; downstream adaptations
  carry the same terms. Plain-language line for the page: "Free for
  everyone. Nobody sells this packaging."
- Hindsight underneath: remains MIT, credited, untouched.
- Owed before release: a third-party notices file (Hindsight's own
  transitive dependencies each carry their own licenses).

Distribution shape (PI ruling, Sep 28, /cat): the public git suggests
the tool and carries the source; the lab's packaged zips stay PRIVATE
in the handoff repo as disaster backups in case public downloads
disappear.

## Upload sequence (REVISED for the fresh-public-git shape; the PI's browser step)

Ruling (/cat, Sep 28): "archive and fresh. separate paths. archive
only on git." The private thinkpink repo is the archive path and stays
private. A FRESH public repo carries the release. The lab hosts no
packaged zips publicly; the site card suggests the tool and links the
fresh repo + upstream Hindsight.

1. PI nod on the fresh-repo name and creation.
2. Fresh public repo created; LICENSE + NOTICE land first (staged at
   releases/thinkpink-public/ in this lab repo).
3. README + packaging source land from Cecil/Cat's hands (kernel
   content is theirs, verbatim or not at all).
4. Site card goes live per
   `scratch/la-thinkpink-public-git-prompt-2026-09-28.md` (replaces
   the archived download prompt).
5. Verify: live fetch of the card, links resolve, no names, no
   em-dashes, claims match lab/pinkpromise.md.
