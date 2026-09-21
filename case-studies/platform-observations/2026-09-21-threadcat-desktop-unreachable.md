# Platform observation: threadcat.org unreachable from the pilot's desktop

Date: 2026-09-21, ~7:27 PM ET. Filed by the maintainer-assistant at
Cat's direction ("site went down on desktop and i am now on mobile.
wanted to flag. notate in a small brief just so we have it somewhere").
Status: OPEN, observation only, no diagnosis attempted. Investigation
deferred.

## What was observed

- **Claimed:** threadcat.org would not load on Cat's desktop browser.
  She switched to mobile (iOS) and flagged it in thread.
- **Verified:** from the cloud workspace minutes later (19:27 PM ET),
  the site answered HTTP 200 on three consecutive fetches of `/`
  (0.38 to 1.34 seconds) and HTTP 200 on `/manual`. The site was
  reachable and fast from at least one vantage point at the time of
  filing.

## What this pattern suggests (hypotheses only, no conclusions)

The claimed outage plus the verified 200s together mean the failure,
if it was occurring at flag time, was not a total application outage.
Candidate classes, unordered: local DNS or cache on the desktop, an
ISP or regional network path issue, a CDN edge serving her region
while other edges stayed healthy, or a transient host-side blip that
resolved before the cloud check. None are supported or excluded by
the current data. The record deliberately does not pick one.

## What would settle it

- The desktop's exact error (DNS failure, timeout, TLS error, or an
  HTTP error code), next time it reproduces.
- Whether mobile on the same network also failed, or only desktop
  (she was on mobile cellular or a different path at report time).
- A `dig`/traceroute from the desktop against a curl from another
  network, if it recurs.

## Standing note

Notated and parked at Cat's direction; no investigation scheduled.
The Lovable host's own status page is the first vendor check if it
recurs. Timing datum worth keeping if a pattern emerges: this is the
first reachability flag in the project's record, on day two of the
site being live.
