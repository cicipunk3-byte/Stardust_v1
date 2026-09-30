# FINDINGS — energy recycling & RF capture, 2026-09-24

Scope: Cat's directive ("closed electrical circuits; energy captured via radio"), provable material only. Raw captures: [RAW-CAPTURE-2026-09-24.md](RAW-CAPTURE-2026-09-24.md). Status: LAB-SIDE.

---

## RQ1 — Closed circuits and energy recycling

**The provable core first:** energy in a closed circuit is conserved, never created. "Recycling" can only mean recovering energy that would otherwise dissipate as heat — nothing in a closed loop yields surplus. No scraped source claims otherwise; the field exists *because* recovery beats generation.

**And here is the surprise: "energy recycling logic" is a real, named engineering discipline.** It's the literal synonym list for [adiabatic circuits](https://en.wikipedia.org/wiki/Adiabatic_circuit): "charge recovery logic, charge recycling logic, clock-powered logic, energy recovery logic, energy recycling logic." The principle, traceable to Charles Bennett ("this energy could in principle be saved and reused"): instead of dumping the charge stored in a transistor's node capacitance to ground as heat, an AC "power clock" and inductive elements *ramp* it gently and take the charge back for the next computation.

Where the field provably stands:
- **Quasi-adiabatic circuits** "reclaim part of the energy spent in the computation process and recycle the recovered energy for subsequent computations" — [IEEE](https://ieeexplore.ieee.org/abstract/document/5728134). Recovery is partial by design; losses determine the ceiling.
- **~50% average energy recycling** demonstrated on-chip in a commercial foundry process by Vaire Computing's adiabatic/reversible approach — [datadeep writeup](https://datadeep.tech/reversible-computing/). ⚠ vendor-adjacent blog; treat the 50% figure as the company's claim, not independently verified. The underlying approach (adiabatic switching via LC resonant circuits) is standard literature.
- **Superconducting AQFP circuits** (Yokohama National University): energy dissipation 10,000–100,000× below advanced CMOS, per the same source. ⚠ same flag.
- **>90% energy recovery** in adiabatic spiking-neuron circuits (npj Unconventional Computing, 2024, per the same article). ⚠ same flag.
- Theoretical floor is real science: [Landauer's principle was experimentally verified](https://link.springer.com/chapter/10.1007/978-3-642-38986-3_3) (Bérut et al., Nature 2012, cited within) — information erasure has a minimum heat cost, so fully reversible computing is the only path to near-zero-dissipation computation.

**The load-bearing caveat:** all of this happens *inside the silicon*. It requires designing the chip around energy recovery from the transistor up. It cannot be retrofitted, bolted on, or harvested from a commodity computer. **A Mac Mini runs standard CMOS; its computation energy leaves as heat, full stop.** No circuit you attach to a Mini recycles its compute energy back.

At household scale, the only provable "recycling" is accounting, not hardware: waste heat recovery (a Mini's ~10-40 W of heat heats the room it's in — if the room is heated anyway, that heat is recycled work), plus choosing efficient hardware in the first place.

## RQ2 — Capturing energy via radio

**Real, measurable, and hard. The numbers are the story.**

How it works: a **rectenna** (antenna + rectifier) converts ambient RF — TV, cellular, WiFi — to DC. [Component-level overview](https://www.mdpi.com/2673-4001/6/3/45).

The physics that constrains it: received power falls with the **square of distance** from the source. The cleanest documented case: downtown Tokyo, 6.5 km from a **100-kilowatt** TV transmitter — signals harvestable, but the power level had fallen **more than nine orders of magnitude (over 90 dB): from a hundred kilowatts to tens of microwatts** ([Stanford ph240](http://large.stanford.edu/courses/2014/ph240/mcmilin2/), citing the Tokyo measurements; corroborated by [Arrow's engineering writeup](https://www.arrow.com/en/research-and-events/articles/realities-of-rf-power-harvesting), which concludes general-purpose far-field harvesting is "quixotic and ultimately impractical" except for dedicated beams).

Real numbers, by source tier:
- **Ambient indoor RF harvesting: nanowatts to a few microwatts** at typical distances from access points; **dedicated power beacons: tens to hundreds of microwatts** ([meta-analysis ranges](https://www.digitalwindmill.com/ai-technology/energy-harvesting-from-ambient-sources-explainer) ⚠ low-grade aggregator — corroborated by the peer-reviewed reviews below).
- Peer-reviewed rectenna reviews: conversion efficiency **15-42% at ambient densities** (20% at 60 µW/m², 40%+ above 500 µW/m² — [ScienceDirect review](https://www.sciencedirect.com/science/article/pii/S2589234725002209)); up to **97.18% PCE in lab best-cases with dedicated high-power input**, for devices in the **0.5-300 milliwatt class** ([rectenna comparative analysis](https://www.sciencedirect.com/science/article/abs/pii/S2213138826001049)).
- City-scale surveys (Imperial College London, 2013) found DVB-T, GSM, 3G and WiFi bands are the viable ambient sources ([summary](https://www.onio.com/article/how-do-rf-harvesting-work.html)).
- Ambient RF can support **microwatt-scale computing** — "one microwatt is enough to do thousands of bits of computation per second" for ultra-low-power circuits ([Joule/Cell Press](https://www.sciencedirect.com/science/article/pii/S2542435120301896)).

**The arithmetic that decides it:** a Mac Mini idles around **10 watts = ~10,000,000 microwatts**. Ambient RF harvesting delivers single-digit microwatts. The gap is **six to seven orders of magnitude**, through no fault of engineering — it's the inverse-square law plus regulatory transmit-power limits. Directed wireless power (beamed at a receiver) works at short range and powers [commercial platforms](https://www.sciencedirect.com/science/article/pii/S2589234725002209) (Powercaster, Cota), but it powers sensors, not computers.

## Verdict, provable-claims-only

1. **Energy recycling is real at chip scale** (adiabatic logic, up to ~50% demonstrated recovery, unverified vendor figure) — and **unreachable at retrofit scale**. You cannot recycle a Mini's compute energy from outside.
2. **RF capture is real and arduous exactly as you said** — it harvests nanowatts to microwatts from ambient fields, and that is a physical wall, not an engineering one.
3. **Where it *does* work for the lab:** the microwatt tier. RF harvesting can genuinely power the *small* things — sensors, indicators, low-power nodes — which is the IoT band the whole field targets. If the Oz sandbox ever sprouts physical-world sensors, radio-power is a provable option **for those**, never for the compute.
4. **The provable green path for the Mini stays:** efficient silicon (its actual strength), green-source electricity, and waste-heat accounting. The recycling grid idea is not crazy — it is six orders of magnitude away from powering this machine, and that gap is what "we only take what is provable" is for.

## Fabcheck summary
- Flagged: Vaire 50%, AQFP and spiking-neuron figures (single vendor-adjacent source chain); digitalwindmill ranges (aggregator, used only when corroborated).
- Verified via peer-reviewed or institutional sources: Tokyo 90 dB / 9-orders case (Stanford course page citing published measurements), ambient µW ranges (multiple ScienceDirect/MDPI reviews), rectenna PCE ranges (two independent reviews).
- Negative result stated: **no source found claiming RF harvesting can power general-purpose compute** — every review scopes it to low-power devices. Searched: the three query families in the raw log.
