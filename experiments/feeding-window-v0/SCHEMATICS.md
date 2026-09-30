# FEEDING WINDOW v0 — Schematics for the first live experiment

**Status:** PROPOSAL at Cat's gate. Built from the three Sep 24 scrapes (sources: [oz-adjacent](../../source-material/scrapes/oz-adjacent-research/FINDINGS.md), [energy-recycling/RF](../../source-material/scrapes/energy-recycling-rf/FINDINGS.md), [BT/mesh/mining + hardware verification](../../source-material/scrapes/bluetooth-mesh-mining-capture/FINDINGS.md)).
**What died:** mining as an energy lane (dropped by Cat; also unsupported by the record as a green claim).
**What survived, provably:** scheduled capture → storage → scheduled release ("feeding window"), solar as the surplus source, RF as the sensor-tier power, heat as the accounting lane. The structure is real; this document scales it to lab size.

---

## 1. The honest frame (read first)

This experiment does **not** make the Mac Mini green. That hunch is dead and the numbers held the funeral: ambient RF delivers microwatts; the Mini draws ~10 W idle. What this experiment **does** prove, with meter receipts:

1. A **feeding window** — surplus captured in its window, stored, released on schedule — works at lab scale.
2. The **µW tier** (sensors) can run on harvested radio, demonstrating the RF lane's true ceiling.
3. The Mini's **heat output is measured, not assumed** — quantifying the one "recycling" lane a Mini actually has (room heat).

Three lanes, three honest claims, one structure. That's the experiment.

## 2. System diagram (all low-voltage; no mains work anywhere)

```
                 THE SUN  (the only feeder)
                     │
              ┌──────▼──────┐
              │ Solar panel  │   20 W class, 12 V nominal
              │ (window/balcony/outdoor)
              └──────┬──────┘
                     │ panel leads (barrel or MC4)
              ┌──────▼──────┐
              │ Charge       │   LiFePO4 profile, 10 A class,
              │ controller   │   built-in overcharge/over-temp/
              │ (PWM, USB out)  short-circuit protection
              └──┬───────┬───┘
                 │       │ USB 5V out
        ┌────────▼──┐ ┌──▼─────────────┐
        │ LiFePO4    │ │ USB power meter│  (in-line, \$10 class)
        │ battery    │ └──┬─────────────┘
        │ 12 V, BMS  │    │
        └────────────┘    ▼
                    µW/mW TIER LOADS
                    • sensor node (RF-harvest demo)
                    • indicator LED strip / small display
                    • (optional) trickle charge for accessories
                     │
              ┌──────▼───────┐
              │ Logger        │   the Mini (or any always-on box):
              │               │   reads meter via local network,
              │               │   writes CSV, runs the schedule
              └───────────────┘

  SEPARATE LANES (measured, not powered by the above):
  • RF lane: rectenna/harvester module → capacitor → sensor node
  • Heat lane: temperature sensors on Mini intake/exhaust + room
```

## 3. Physical shopping list (existence verified; check prices at order time)

| # | item | class | notes |
|---|---|---|---|
| 1 | Solar panel, 20 W, 12 V monocrystalline | the feeder | kits with bracket + cables are common ([example class](https://www.topbullshop.com/products/12v-20w-solar-panel-kit-monocrystalline-with-10a-solar-charge-controller-extension-cable-with-battery-clips-o-ring-terminal-for-rv-marine-boat-off-grid-system)) |
| 2 | Charge controller, 10 A PWM with USB output, **LiFePO4 profile** | the regulator | protection circuitry is the spec that matters: overcharge, over-temp, load short-circuit ([verified class](https://www.litime.com/products/20a-pwm-solar-charge-controller)) |
| 3 | LiFePO4 battery, 12 V 12-20 Ah, **with integrated BMS** | the store | LiFePO4 = the safest lithium chemistry for indoors ([kit example](https://www.expertpower.us/products/200w-20a)) |
| 4 | USB power meter (in-line, display) + smart plug with energy monitoring, **local-control** (e.g., a plug with a local API) | the meters | every claim needs a meter; local API keeps the data private |
| 5 | RF harvesting demo, ambient tier: 2.4 GHz rectenna module or RF-DC converter eval board | the µW demo | receives from your own router; **receive-only** |
| 6 | (optional, later) [Powercast Lifetime Power dev kit](https://www.powercastco.com/products/development-kits) | dedicated-beacon tier | 915 MHz, FCC Part 15 approved transmitter + Powerharvester receivers, [orderable at Mouser](https://www.mouser.com/en/new/powercast/powercastlifetimepower/) — this one *transmits*, so it runs only under its own manual's rules; defer to a later phase |
| 7 | Two USB temperature data-loggers (or 1-wire/thermal sensors) | heat lane | intake vs exhaust on the Mini |
| 8 | Cables/adapters: USB-A/C, barrel connectors, small fuse holder | glue | nothing exotic |

Budget shape: lanes 1-4 + 7-8 land in the low hundreds of dollars; the RF demo module is cheap; the Powercast kit is the luxury item (price at order time). **Nothing here requires mains wiring. If any step ever does, the step is wrong.**

## 4. The feeding-window schedule (the structure, verbatim)

- **Window opens** (default: local solar noon ±3 h, adjustable): controller charges the battery from the panel; loads designated "window loads" (the sensor tier, an indicator) draw from the battery, never the wall.
- **Window closes:** loads drop to the battery-only baseline; logger records the day's captured watt-hours.
- **Replenish event:** once battery stays above its floor and the week's budget is met, a scheduled "replenish" run powers a chosen accessory (e.g., topping a power bank) — the release side of the cycle.
- **Everything logs to CSV on the Mini**, local only, cron-driven. I write the logger and schedule; the skill needed to *run* it is near zero.

## 5. Measurement & verification protocol (the lab's own rules, applied)

1. **Pre-registered predictions.** Before each week, we write down expected numbers (panel Wh/day, sensor uptime %, Mini ΔT). Handwritten or committed to the repo first.
2. **Meter receipts only.** A claim without a logged meter reading is an anecdote. The CSV ledger is canonical — same rule as the repo ledger.
3. **Run the artifact.** The schedule runs for real for at least two weeks before any claim is written.
4. **Negative results are results.** If the RF demo harvests too little to run its sensor in your RF environment, that's a filed finding, not a failure.
5. **Fabcheck on ourselves.** Anything I write about the system gets traced to a CSV row.

## 6. Safety rules (non-negotiable)

1. **Low voltage only.** 12 V DC and USB. No mains wiring, ever, by anyone. If a step needs an electrician, it's outside this experiment.
2. **LiFePO4 with BMS only.** No bare cells, no series-stacking packs, no punctured/swollen battery ever recharged. Indoors, on a hard surface, away from bedding.
3. **Charge above freezing.** Lithium charging below 0 °C damages cells — panel lives outside, battery lives inside.
4. **Fusing on the battery lead** (the controller's protection plus an inline fuse is the belt-and-suspenders).
5. **Receive-only RF in v0.** Harvesting antennas only. The one transmitter in scope (Powercast's FCC-approved Powercaster) is deferred, and if it's ever used it runs in its own phase, per its manual, in a room we choose deliberately.
6. **Panel power hygiene:** panel connectors kept dry; controller sized above panel max current (20 W ÷ 12 V ≈ 1.7 A — a 10 A controller has enormous headroom).

## 7. What you need to know (the honest literacy list)

Nothing on this list needs a course; each is an afternoon:

1. **Volts, amps, watts, watt-hours** — and the one equation that governs everything: energy = power × time. A 20 W panel under real sun for 4 effective hours ≈ 60-80 Wh/day (derated for clouds, angle, glass if indoors). That number is the whole budget.
2. **Why the loads must be small:** 80 Wh/day runs the sensor tier *forever* and a router-class device (5 W × 24 h = 120 Wh) *not quite*. Sizing is the skill; the arithmetic is middle-school.
3. **LiFePO4 basics:** what a BMS does, why the chemistry is the safe one, what 20 Ah means (12 V × 20 Ah = 240 Wh stored).
4. **Reading one datasheet:** the charge controller's — battery type setting, max PV input, load output rating.
5. **Cron + CSV:** the schedule and the log. I build both; you need to read them, not write them.
6. **What a rectenna does** (the two-findings papers cover it — µW from ambient RF, physics ceiling, already understood).
7. **When to stop.** Any warmth, smell, or swelling from the battery: disconnect, outside, done for the day. This rule outranks all others.

Cecil's descent rule applies verbatim: **never add a layer until the one beneath it can be independently observed, stopped, and explained.**

## 8. Build order

1. Order lanes 1-4 + 7 (the solar core and meters). RF demo module rides along.
2. Bench test indoors: battery → controller → meter → dummy load. Verify the controller charges with the panel on a windowsill before final placement.
3. Mount panel (window, balcony, or south-facing outdoor spot — placement decides everything; measure before committing).
4. Deploy logger + schedule on the Mini. Week 1 = observation only, no feeding windows.
5. Open the first feeding window. Two weeks of scheduled runs.
6. Add the RF demo node as the second phase, once the solar lane's ledger is boring.
7. File the numbers. Publish nothing without Cat's gate, per standing law.

## 9. What this experiment can and cannot claim

- **CAN claim (if meters agree):** a working lab-scale feeding-window structure; the µW tier powered by the sun and (phase 2) by ambient radio; the Mini's thermal output quantified; a documented template others could replicate — which is the ThreadCat-shaped contribution.
- **CANNOT claim:** green compute. The Mini runs on wall power; this experiment *measures* the lab's energy truth instead of guessing it. The greening of the Mini, if it ever happens, comes from the utility-side lane (green electricity supply), not from anything bolted to a desk.
