# Platform observation: Safari Reader View misclassifies an SPA chat thread

Filed: 2026-09-21 evening. Observed by the founder on macOS v27,
MacBook Neo, Safari. Filed under the lab's platform-behavior thread
alongside the Lovable connector findings.

## What happened

Viewing a Vellum Assistant conversation thread (vellum.ai, web app) in
Safari's Reader View produced a broken extraction instead of the
thread: the reader page showed a single fragment of an old message
(heading "1. The Physical Presence and the Guitar Style", from a
long-form analysis pasted into the thread earlier), a "Summarize" pill,
and a large empty gray box where media content should render.

Screenshots in this folder:
- `reader-view-broken.png`: the reader extraction (fragment + empty box)
- `thread-normal-view.png`: the same thread rendered normally, for contrast

## The mechanics (verified against published sources)

Safari Reader View is a JavaScript library Apple forks from Arc90's
Readability, injected into the page itself. It works by scoring and
trimming DOM nodes until only the "article" remains. Its trigger
heuristic is crude and well documented: a block element containing an
H1-H6 heading followed by a certain amount of text, scored partly by
how much text is visible at the moment the reader button is pressed.
Extracted content is moved to a `safari-reader://` origin.

Sources: Brave SpeedReader paper (brave.com/research/files/
speedreader-www19.pdf); Joe Vennix, "Hacking Safari's Reader" (2011);
Mathias Bynens, "How to enable Safari Reader on your site"; Ctrl blog,
"Web Reading Mode"; alf.nu, "Safari Reader UXSS".

## Why this thread tripped it

The Vellum thread view is a React single-page app with no semantic
article markup. But the thread contains a pasted long-form document
(the Gemini song analysis: headings, nested bullet lists, quoted
lines). That message subtree is the exact shape the heuristic hunts
for. Reader classified the pasted message as "the article," extracted
only it, and dropped everything else in the thread.

The empty gray box is the subtree's media container: Reader carries
images it can identify as plain URLs; React-managed image containers
do not survive extraction. Unverified at filing: whether the
"Summarize" pill is a Vellum UI affordance inside the extracted
subtree or a WebKit reader enhancement. Confirming requires inspecting
the live DOM on the affected machine; noted as an open item.

## Classification

**Misclassification, not a rendering failure.** Reader did its job with
full confidence on the wrong object: it verified an article-shaped
thing inside a page that is not an article. Same failure class as the
empty-repository audit earlier the same day: a tool reporting success
about an object nobody checked.

## What matters and what does not

- **Software, entirely**: the WebKit version (tied to the OS), the
  reader heuristic, and the DOM shape of the page at press time.
- **Hardware, not at all**: the 8GB MacBook Neo's profile is
  irrelevant; the behavior reproduces on any Mac with the same Safari
  build viewing the same page. Nothing is resource-bound.
- **Content-shape dependent**: any chat thread containing a pasted
  long-form document (headings plus body text) is expected to trigger
  the same extraction on comparable SPA web apps.

## Practical notes for the lab

1. Do not archive threads via Reader View; use the platform's export
   or copy the source markdown. Reader output is a paraphrase of one
   subtree, not a copy of the record.
2. A thread that contains pasted research documents (which this lab's
   threads do by design) is maximally exposed to this misclassification.
3. The correct way to snapshot a thread is the same way the lab
   snapshots everything: export the source, commit it, let the record
   hold it.

## Open items

- Identify the "Summarize" pill's owner (Vellum UI vs WebKit).
- Check whether the same extraction occurs on other SPA chat apps
  (comparison run, low priority).
