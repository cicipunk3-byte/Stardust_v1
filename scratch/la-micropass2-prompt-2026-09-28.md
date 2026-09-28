# LA prompt — micro-pass #2 (audit of the live publish, Sep 28)

The audit of the live site passed on: homepage pill, sidebar entry, /thinkpink content and URLs, download facts, papers page H1/intro/title, papers changelog line. Four fixes remain. Report each, re-screenshot only what changed (both widths where the change is visible). The publish already happened, so these go live on the next publish.

1. TOOLS PAGE /tools: the minibeat card's badge still reads "Tested, pending gate". The canonical ledger (tools/TOOL-STATUS.md) places minibeat under BUILT AND PUSHED. Change the badge to "Built and pushed". Keep the "Field validation owed: a run on the Mac Mini" line under the card. (This is the second publish where this specific fix has not landed; please confirm the change by quoting the badge line back in your report.)

2. /thinkpink guide, step 3, last sentence: replace "Unsigned beta build: the first launch needs one Terminal step, spelled out there." with "Ad-hoc signed beta build: if macOS asks on first launch, right-click the app and choose Open." The source of truth (STARTUP-PLAIN.md in the SeeingPink repository, commit 365cc27) was updated to exactly this; the site's guide syncs to it.

3. /thinkpink, Get ThinkPink section: in the sentence "The download lives in the project's public repository, as a release built from that source.", make the word "release" a link to https://github.com/cicipunk3-byte/SeeingPink/releases

4. Changelog, under 28 September 2026, Method and tooling, add this entry (note: it cites the SeeingPink repository rather than the research repository; that is deliberate, the release lives there):
"The ThinkPink page went live: the governed desktop assistant, released as v0.1.0 on the SeeingPink repository, built from that repository's own source; the page carries the download (127 MB, Apple Silicon), the setup guide, and the plain-science sources."

5. Confirm the /thinkpink page is now included in the search-engine listing and the sitemap (the publish condition was "at publish time it gets listed"; the page is live now). Report yes/no with what you find.

Rules unchanged: no em-dashes, no lab-member names, no new claims beyond the verified facts already on the page. If anything conflicts with the page's current state, stop and report instead of improvising.
