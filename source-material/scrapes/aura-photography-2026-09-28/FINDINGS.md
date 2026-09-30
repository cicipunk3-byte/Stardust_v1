# FINDINGS — Aura photography: the actual science
Scrape: 2026-09-28, requested by Cecil (/c). RAW-CAPTURE.md carries hits + verification log. Headline first, then the mechanism, then what's real underneath.

## Headline finding

**There are two different "aura photo" technologies, and neither photographs an aura.** The classic Kirlian photograph records a real but mundane electrical event (corona discharge, dominated by moisture and pressure). The modern "aura camera" doesn't detect any field around your body at all: your hands on the plates act as electrodes in a standard biometric circuit, the machine reads your skin's electrical conductance and temperature, and software looks those numbers up in a color table and paints the result around your portrait. The colors are a programmed lookup, not a detection.

## Mechanism 1: Kirlian photography (the classic, 1939)

An object or fingertip sits on photographic film atop a charged metal plate. High voltage ionizes the air at the contact, and the discharge glows. Real physics, verified: the discharge pattern is "stochastic electric ionization" governed by voltage, frequency, contact pressure, humidity, and grounding ([Wikipedia summary of the primary literature](https://en.wikipedia.org/wiki/Kirlian_photography)). The decisive experiments: most variation in streamer length, density, curvature, AND COLOR of a living fingertip's corona is accounted for by skin moisture ([Science 1976, DOI 10.1126/science.968480](https://www.science.org/doi/10.1126/science.968480); foundational physics in [Boyers & Tiller 1973, J. Appl. Phys., DOI 10.1063/1.1662715](https://doi.org/10.1063/1.1662715)). The famous "phantom leaf" demo (a cut-off piece still shows in the glow) disappears when the plate is cleaned of residual moisture between shots. Colors specifically: color film's dye layers interact with discharge intensity, so the hues are artifacts of film chemistry meeting electric current, not information about the subject. Ironically, the one honest use case the 1976 paper supports: quantifying moisture.

## Mechanism 2: the modern aura camera (Coggins lineage, 1970s-present)

Three parts ([teardown of the AuraCamera 6000 by someone who did R&D for its inventor](https://www.jentechyoga.com/2019/06/the-auracamera-6000-system.html), corroborated by [multiple](https://euromedfoundation.com/aura-photography-equipment-explained-science-costs-and-wellness-context/) [explainers](https://www.theaurajourney.com/aura-blog/posts/behind-the-lens-the-technology-that-captures-your-aura)):

1. **Hand plates = biometric electrodes.** They measure galvanic skin response (GSR, formally electrodermal activity, EDA) and skin temperature; some systems add heart rate variability. Sitting with palms on metal plates is a standard psychophysiology setup.
2. **Color assignment = software lookup.** Readings are mapped to colors through "programmed associations" / "algorithms based on color theory." In the original Polaroid systems this was literal: the bio-readings lit colored bulbs inside the camera box, and a double exposure put those colors around your portrait. Vendors' own materials concede the mapping is interpretive; one vendor's claim of an "electoral dermal layer" (no such anatomy) shows the marketing layer's rigor.
3. **Portrait overlay.** A normal photo of you, with the machine-colored field composited around it.

## What's real underneath (this matters for whatever /c brings next)

The measurement is legitimate psychophysiology; only the interpretation layer is pseudoscience. EDA is one of the most-studied human physiological signals there is ([Wikipedia: EDA](https://en.wikipedia.org/wiki/Electrodermal_activity)), driven by the sympathetic nervous system, not consciously controlled, and it does track something: **arousal intensity**. But two hard limits, verified:

- **Intensity, not valence:** joy and fear produce the same conductivity increase ([EDA review](https://www.innsightful.com/electrodermal-activity-eda-the-science-of-skin-conductance-and-emotional-arousal/)). Any aura color chart that claims to distinguish calm-love from anxiety from excitement is claiming a discrimination the sensor physically cannot make.
- **It's a proxy for arousal, with confounds:** hydration, temperature, electrode pressure, and handling all shift readings ([Kirlian-side artifacts](https://en.wikipedia.org/wiki/Kirlian_photography); EDA is used seriously in [biofeedback and seizure-prodrome research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8927283/), where those confounds are controlled).

So the honest one-sentence summary: **an aura photo is a polygraph-adjacent arousal gauge wearing a color wheel, originally double-exposed onto a Polaroid.** What the colors track, to the extent they track anything stable, is sympathetic arousal in the moment, interpreted through a chart with no empirical basis.

## Open items / flags

- GDV (Korotkov's digital successor) has a small, contested literature; not scraped in depth this round, flag for a follow-up pass if it becomes load-bearing.
- No peer-reviewed study validating aura-color charts was found; their absence IS the finding, stated as found-absent.
- Boyers & Tiller: Tiller later drifted toward fringe interpretations of his own co-authored physics; the 1973 paper itself is uncontested measurement work.
- Standing-directive close-out: no outreach candidates proposed (N/A).
- Ready for /c's reveal whenever he is.
