# Platform observation: Vellum unreachable from the pilot's desktop

Date: 2026-09-21, ~7:28 PM ET. Filed at Cat's direction after she
corrected the referent of the prior flag ("not threadcat, Vellum AI").
Status: OPEN, observation only.

## What was observed

- **Claimed:** the Vellum platform would not load on Cat's desktop
  (macOS, browser). She switched to mobile (iOS) and continued there.
- **Verified, with limits:** the assistant was still executing on the
  platform from the cloud vantage at the same time (this file was
  written there), so the service was up at least for cloud-side
  sessions. No independent check of the desktop client, the macOS
  app, or her regional edge was possible from the cloud workspace.

## Hypotheses (unordered, unsupported)

Local browser state or cache on the desktop; a session or auth
failure specific to that client; a regional edge or network path
issue; a desktop app or web build defect. The iOS client working
while desktop failed is consistent with all of these.

## Relation to the prior observation

This is the actual referent of the ~7:26 PM "site went down on
desktop" flag. The threadcat.org observation filed minutes earlier
was written against the wrong referent and carries a correction
banner; its cloud 200-checks remain valid data (threadcat.org was
up) but its framing assumed the wrong subject.

## What would settle it

Next reproduction on desktop: the exact error, the URL, whether the
macOS app and the browser fail the same way, and a second network if
available. If it recurs, Vellum's own status page is the first vendor
check. Timing datum: first Vellum reachability flag in the record,
day two of the project running on the platform.
