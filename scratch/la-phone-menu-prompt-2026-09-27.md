# LA prompt #4 -- minimal phone menu (2026-09-27)

Paste-ready for LA (Lovable). Runs after prompt 3 (pink gradient) in the dev
lane. Decision source: Ziggy rec, sustained by Cat Sep 27 -- phones get a
MINIMAL menu, not a full navigation feature.

---

## The change

Phones currently have no menu at all: only the pink progress bead at the top
of the viewport, and the PinkPromise page is reachable only through the home
page button. Add the smallest possible menu:

**1. A single "Menu" link in the progress-line bar (phones only).**

- Placement: top of the viewport, opposite end from the progress bead
- Style: small, pink (the primary accent per prompt 3), plain text or a
  hamburger glyph, minimum 44x44 px touch target
- Visibility: ONLY on phone widths (the widths that currently show neither
  sidebar nor top menu). Nothing changes at tablet or desktop widths.

**2. Tap behavior.**

- Tap opens the same nav list the top menu uses (same links, same order,
  same labels) as a lightweight overlay or slide-down, glass-tinted per the
  palette
- PinkPromise appears in that list at the same position as everywhere else
- Tapping a link closes the menu and navigates; tapping outside or the
  "Menu" link again closes it
- No new pages, no footer additions, no settings, no animations longer than
  ~200ms

## Constraints

- No em-dashes, no names, no new surfaces beyond the overlay
- The progress bead and its pink color are untouched
- Keyboard/contrast rules do not apply to touch, but keep AA text contrast in
  the overlay

## Report back

Screenshots: closed state (progress bar with Menu link), open state, and a
navigate-then-close sequence, on a phone-width viewport. Dev environment
only.
