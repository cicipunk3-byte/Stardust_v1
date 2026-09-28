# Staging notes - fresh public ThinkPink repo

Status: STAGING. These files prepare the fresh public repository ruled
Sep 28, 2026 (/cat): "archive and fresh. separate paths. archive only
on git."

## The ruling, applied

- The existing PRIVATE repo cicipunk3-byte/thinkpink becomes the
  archive path. It stays private, on git, untouched. Nothing is made
  public there.
- The fresh public repo is a SEPARATE path: clean history, only what
  the release needs. Built from this staging directory.
- The lab's packaged zips stay private in the handoff repo as disaster
  backups.

## What ships in the fresh repo

- LICENSE (CC BY-NC-SA 4.0 for the packaging layer, spirit clause
  included)
- NOTICE-THIRDPARTY.md (Hindsight MIT credit + dep licenses)
- README - OWED, authored by Cecil/Cat: founder voice is theirs, and
  kernel PINK content must come from Cecil/Cat verbatim (never
  regenerated; the provenance rule)
- Source of the packaging layer - staged from the private archive
  repo at release time, swept for private kernel content before any
  push

## Gate order to flight

1. PI nod on the fresh-repo name and creation.
2. Repo created, LICENSE + NOTICE land first.
3. README + source land from Cecil/Cat's hands.
4. Release/tag per the draft release file.
5. Site card (suggest-the-tool shape) goes live, pointing at the
   fresh repo + upstream Hindsight. Packaged zip is NOT hosted.
