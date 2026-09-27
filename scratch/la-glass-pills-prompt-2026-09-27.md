# LA prompt #6 -- hero pill buttons + site-wide glass pill style (2026-09-27)

Paste-ready for LA (Lovable). Runs after prompt 5. Source: Cat, Sep 27
(/cat): update the "Start here", "Build Your Toolbox", and "Bundles" links
into pill buttons matching the PinkPromise button, with a glassy look on all
pill buttons across the site, desktop and mobile. Then a full audit runs.

---

## 1. The three hero links become pill buttons

On the homepage, convert these three links from plain underlined text into
pill buttons (fully rounded ends, like the PinkPromise button):

- **Start here** (anchors to #research)
- **Build Your Toolbox** (links to /tools#get-the-tools, keeps its briefcase
  icon)
- **Bundles** (links to /packages, keeps its bundle icon)

Style:

- Glass pill: frosted glass (backdrop blur), pink-tinged translucent
  background, soft pink border or ring, pink text, existing site pink family
- Icon sits inside the pill at the left, text vertically centered
- Height and padding match the PinkPromise button's scale; hover lift or
  glow consistent with it
- Layout on desktop: the three pills in one row (wrapping is fine), placed
  just below the PinkPromise button where the links are now
- Layout on mobile: stacked full-width, minimum 44x44 px touch targets,
  icons scale

## 2. Hierarchy law (do not break)

PinkPromise stays the LOUDEST element on the page: solid pink, largest. The
three new pills are quieter (glass outline style, not solid). A reader should
see PinkPromise first, the pills second. Never make a nav pill outshine the
flagship.

## 3. Site-wide pill consistency

All pill-shaped buttons across all 16 pages share ONE glass treatment (same
border radius, blur, tint, and hover behavior) via a shared component or CSS
class, not per-page styling. This includes "Get involved", any buttons on
/pinkpromise, /packages, /tools, and the governance page. Solid pink pills
(PinkPromise, primary calls to action) and glass pills (secondary navigation)
are two variants of the same component family.

## 4. Constraints

- Labels and destinations unchanged: same words, same links
- No em-dashes, no names, no new pages, no download or email capture
- Text contrast stays AA on every pill, glass or solid
- Progress bead, sidebar, and top menu are untouched (the phone Menu link
  from prompt 4 stays as built)

## Report back

Screenshots: homepage hero (desktop + mobile) with the three pills, one
interior page showing its pill buttons in the shared glass style, and a
hover/pressed state if capturable. Dev environment only; full audit follows
on the live site.
