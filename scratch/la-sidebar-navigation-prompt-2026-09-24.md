# LA prompt: desktop sidebar navigation + home readability pass (Sep 24, 2026)

TO-THE-AGENT: add a desktop sidebar for navigating the site and the home page's sections, keep the continuous single-scroll on mobile, and make small copy additions so a first-time visitor can orient in under ten seconds. This is a navigation and layout pass; do not rewrite existing copy except where named below.

## Desktop (lg screens and up)

1. **Left sidebar, sticky.** A slim fixed left rail (roughly 200-230px) visible on lg and wider. The main content shifts right to make room; keep the max content width comfortable to read (aim for a 65-75 character measure on body text).
2. **The rail is the thread.** Render the sidebar as a vertical line (continuing the existing thread-line motif) with one icon node per item. The current section's node gets the pink accent dot and teal icon; the line itself stays charcoal. This is the navigation metaphor: the visitor moves along the thread and the pink dot shows where they are.
3. **Two groups, in this order.**
   - "This page" (home anchors, scroll-spy active state): Research (microscope icon), What we've built (package icon), Case studies (folder-search icon), Open by default (lock-open icon), Get involved (handshake icon).
   - "Pages" (site pages): Mission (compass), Philosophy (book-open), Tools (wrench), Manual (book), Local model (cpu), Wary of AI (eye-off), Reflections (feather), Papers (file-text), Benchmarks (gauge), Changelog (history), Governance (scale).
4. Use one consistent stroke icon set (Lucide is fine and already in the stack); icons monochrome charcoal, teal on hover, teal-plus-pink-dot for the active item. No multicolor icons; the palette discipline from the logo pass holds.
5. Scroll-spy: as the visitor scrolls the home page, the active anchor updates. Use aria-current on the active link. Sidebar links on other pages navigate home (to the anchor) or to the page as appropriate.
6. Below lg: no sidebar. Keep the current top bar exactly as it is.

## Mobile (below lg)

7. Keep the single continuous scroll unchanged; this is deliberate, the page reads as one thread on a phone. Do not add tabs or sections-on-demand.
8. Add a thin scroll-progress indicator: a 2px thread line at the very top of the viewport with a small pink bead that travels along it as the visitor scrolls. Respect prefers-reduced-motion (show progress as a plain filled line with no animation).
9. Keep the existing mobile menu; it only needs to keep working.

## Home page layout (desktop only where named)

10. On desktop with the sidebar present: "Research focus" may go from a stacked list to a 2x2 grid, and "What we've actually built" from 5 stacked cards to a 2-column grid, so the page is less of an endless scroll for mouse users. Mobile keeps the stacked layout.
11. Do not reorder, merge, or delete any section.

## Copy additions (the only copy changes in this pass)

12. Directly under the headline, before the mission paragraph, add one plain-language line for a cold visitor: "In plain terms: we test whether an AI can carry its memory between conversations using files a person owns, instead of memory hidden inside the model." Keep it set quieter than the mission paragraph.
13. Add a "Start here" text link near the hero that jumps to the Research focus section (desktop and mobile). It gets no special color beyond the standard teal link treatment.

## Rules (standing)

- No em-dashes anywhere.
- No strengthened claims: the new line describes the method, it claims no results.
- No content changes on any other page. Figures, statuses, and tables untouched.
- Icons are interface elements, not illustrations: no new photographic assets.

## Process

Publish-first. Make the changes, publish, then report line by line: every sidebar item with its icon, the scroll-spy behavior, the mobile progress indicator, the two copy additions, and every layout change. Cache-bust. The humans audit jointly in thread after publish.
