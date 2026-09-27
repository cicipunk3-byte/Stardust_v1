# LA prompt #2 -- Lab Overview page on threadcat.org (2026-09-27)

Paste-ready for LA (Lovable). Site rules in force: no personal names, no
em-dashes, no strengthened claims, beta framing. Source of truth for content:
`lab/OVERVIEW.md` at commit 513c256. Run in Ethan's dev lane.

---

Add a new top-level page to threadcat.org and surface it in the navigation.

**1. Navigation.** Add a nav link labeled **Overview** (desktop nav + mobile
menu), positioned after the existing top-level links, before any footer links.

**2. New page at /overview.** Structure and copy below; keep claims exactly
this size. Tone: warm, plain, confident. This page reads like a brochure but
every claim is already published in the repo.

---

## One lab, one loop, all yours

**Our mission.** To prove that a person can run serious research on their own
machine: private, versioned, honest, and free. We build the loop in the open,
measure it, publish the receipts, and give every part away.

### The shape of the loop

A circle with four moving parts, all of them yours: a local model does the
working, a markdown-and-git record does the remembering, small single-purpose
tools check the work, and a published ethics code governs the whole thing.
Observe, record, check, carry, remember. Repeat. Clone the lab and the circle
runs on any machine you own, with the network cable pulled.

### What we built

- **A harness** that runs structured human-and-model sessions and logs claims as data
- **A checking shelf** of small tools: fabrication checker, number-consistency checker, export forgery detector, reasoning-loop detector, authority-pressure probe, context sizer
- **A carrying set**: kernel distiller, carrying-consistency checker, kernel validator, and ark, the movable home the tools live in
- **A verbatim memory layer**: word-for-word storage with semantic recall, zero API calls, nothing leaves the machine
- **Governance**: a published code of ethics where the AI instances are signatories with reciprocal duties

One sentence per tool, with status badges, lives in the Tool Library.

### Status, honestly

The method is published and the case studies are in the repo. The core tools
passed a comprehensive fixture pass; field validation is ongoing. The packaged
one-command loop is in beta. Known limits, stated plainly: a single research
subject so far, warm-surface effects are real, and every score is advisory
until independently graded.

*Built in the open. Receipts in the repo. Free, and meant to stay that way.*

---

**3. Cross-links.** From /overview: "Tool Library" links to the tools page,
"published" links to /papers, "code of ethics" links to /governance. From the
homepage hero, no changes needed in this update.

**4. Constraints.** Do not add names, version numbers, download buttons, or
email capture anywhere on the page. No em-dashes. Match existing typography,
palette (teal links, orange buttons, pink markers), and spacing. Mobile: the
loop diagram (if used) stacks vertically.

**Report back:** screenshots of /overview and the new nav item, desktop +
mobile, before any deploy beyond the dev environment.
