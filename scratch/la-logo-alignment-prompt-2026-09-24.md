# LA prompt: logo alignment pass (ThreadCat mark, Sep 24, 2026)

TO-THE-AGENT: the site is adopting a new ThreadCat logo mark. Align the site's visual layer with it. This is a design-alignment pass only; do not change any content, figures, statuses, or copy except where named below.

## The new mark

The human will upload the new logo file to this project (two files may be provided: the site mark, a cat head containing an orange-and-teal yin-yang swirl with a pink accent dot; and the GitHub profile mark, a subtler two-comma swirl version; the GitHub one is NOT used on the site).

- Use the uploaded file exactly as provided; do not redraw, restyle, or reinterpret the mark.
- Sample the exact hex values from the uploaded file and use those sampled values as the site's accent palette. Expected families: charcoal-slate (the cat outline, current text color), warm orange, teal, soft pink, white.

## Changes to make

1. **Nav logo:** replace the current logo asset everywhere it appears (header, footer if present) with the new mark. Keep the wordmark "ThreadCat" beside it, same size and placement as now.
2. **Alt text:** set the logo alt text to: "The ThreadCat mark: a cat head holding an orange and teal swirl, two threads in one orbit." Do not add this line anywhere as visible copy.
3. **Favicon:** generate favicon sizes (16, 32, 180, 512) from the new mark, tight-cropped on the cat head. Update every favicon/apple-touch-icon reference. Confirm the old favicon asset no longer loads.
4. **Social card:** update og:image and twitter:image to a card built from the new mark: white background, mark left or centered, wordmark "ThreadCat" and the existing tagline "Continuity & Context · Sandboxed AI Research" set in charcoal. No new claims on the card.
5. **Accent palette (the alignment core):** define CSS custom properties for the four sampled colors, then apply them as ACCENTS ONLY on the existing design. The site stays white, charcoal-text, and scientific; the logo colors accent it, they do not repaint it.
   - Teal: inline text links, section-number accents (the 01-04 research numbers), the Benchmarks nav item if it needs distinguishing.
   - Orange: primary buttons ("Get involved", "Read the research"), the cost-card figure, hover state of teal links.
   - Pink: the small signature accent. Use it as the hover dot on nav links and as the bullet marker in any list where a marker currently has no meaning. Used sparingly; never for text.
   - Charcoal: unchanged, stays the text and outline color.
6. **Hero image:** leave the existing hero sandbox photo in place. Do not generate new imagery.
7. **Fig. captions:** unchanged in style; if a caption color exists, it moves to the sampled charcoal, not an accent color.

## Rules (standing)

- No em-dashes anywhere.
- No strengthened claims: the palette change adds no claims and removes none.
- Do not touch /papers, /sources, /governance content. This pass is chrome only.
- Every changed asset listed in the report with its old and new filename.

## Process

Publish-first. Make the changes, publish, then report every change line by line: each asset swapped, each CSS variable defined, each page where an accent changed. Cache-bust. The humans audit jointly in thread after publish.
