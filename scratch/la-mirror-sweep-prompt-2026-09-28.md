# LA PROMPT: mirror sweep, 28 September 2026

## Context

Final audit and sweep pass for the site/git mirror (site thread work
order 3). The goal: the site and the repository tell one story, no
redundant sections, flow as clear as the ThinkPink repo's shape
(map first, how to run it second, design depth last).

## 1. STALE FIGURE - fix now

The homepage cloud-software card reads "Vellum Super; 44% of the
monthly plan credit used, checked 27 September 2026." A fresh reading
was pulled 28 September:

- Replace with: "Vellum Super; 56% of the monthly plan credit used"
- "checked 28 September 2026"
- The remaining-credit figure is $24.41 of $55.00; use the percent
  form on the card, matching the current card style.

## 2. Mirror audit - page by page, report findings before fixing

For each of the 14 canonical pages, check that every figure and status
line matches its repository source. Known source-of-truth pairs:

- Tool library cards <-> tools/TOOL-STATUS.md (names, status badges,
  "field validation owed" lines)
- Papers page <-> papers/ in the repo
- Benchmarks page <-> lab/benchmarks/
- Cost figures <-> notes/cost-ledger.md
- Changelog <-> actual publication events

Report any figure or status line on the site that the repo does not
back, and any repo status that the site has not caught up to. Do not
fix anything in this step until the findings are reported.

## 3. Redundancy candidates - evaluate and report

Three places where the site currently says the same thing twice. For
each, recommend keep/condense/cut, with reasoning:

a. The homepage carries the full 17-tool library. The /tools page
   exists for exactly this. Proposal: homepage keeps a condensed
   highlight (three ratified tools plus a link to the full library),
   the full library lives only on /tools.

b. "What we've built" on the homepage vs the /packages page. Check
   whether the item lists overlap; the homepage section should tease,
   the packages page should be the complete list.

c. Any section that repeats the PinkPromise description across the
   homepage hero, the /pinkpromise page, and any banner. One canonical
   description (the /pinkpromise page owns it); everywhere else links
   or shortens.

Do not cut anything without reporting first. The homepage sections
(Research, What we've built, Case studies, Open by default, Get
involved) are ruled anchors - they stay; the question is only how much
duplicated detail lives inside them.

## Standing checks

No personal names outside the papers page, no em-dashes, every figure
matches its canonical source, screenshots after pages finish loading,
cache-busted fetches for verification. Report before publishing.
