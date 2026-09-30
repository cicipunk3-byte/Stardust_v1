# FINDINGS — bluetooth / mesh / mining capture & the "feeding window" structure, 2026-09-24

Scope: Cat's directive — verify whether Bluetooth/radio, mesh, and crypto mining energy can be "captured similarly and recycled through a closed circuit," on a scheduled feeding-window structure (capture → recycle → replenish on a clock). **This is the feasibility verification she asked for before continuing.** Raw: [RAW-CAPTURE-2026-09-24.md](RAW-CAPTURE-2026-09-24.md). LAB-SIDE.

---

## Part A — Bluetooth and radio waves: the similarity is identity

Bluetooth **is** radio waves. It's not "similar to" radio — it's a protocol family riding radio: 2.402-2.480 GHz in the license-free ISM band, wavelength ~12.5 cm, the **same band** as Wi-Fi, Zigbee, and microwave ovens ([everythingRF](https://www.everythingrf.com/community/bluetooth-frequency-bands); [Wikipedia, 2.4 GHz radio use](https://en.wikipedia.org/wiki/2.4_GHz_radio_use); [Texas Instruments coexistence paper](https://www.ti.com/pdfs/vf/bband/coexistence.pdf): "Wi-Fi and Bluetooth products both operate in the unlicensed 2.4 GHz ISM band"). Bluetooth divides that band into 79 channels of 1 MHz and hops between them up to 1,600 times/second to coexist with Wi-Fi ([Wikipedia](https://en.wikipedia.org/wiki/2.4_GHz_radio_use)).

**Consequence for the capture question:** a Bluetooth signal is capturable by exactly the same physics as any other radio — a rectenna tuned to 2.4 GHz. Nothing new is required; the previous scrape's walls apply unchanged.

## Part B — Capturing Bluetooth specifically: provable, microwatts

- A **fully-integrated 2.4 GHz harvester produced ~423 microwatts from ambient RF** — and that paper explicitly targets the BLE-abundant indoor environment, with target devices in the hundreds-of-µW class ([Nature-inspired RFEH system, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9227311/)).
- A dedicated 2.4 GHz rectenna achieved **71% conversion efficiency from a Wi-Fi router at 1 meter** — note: dedicated, aimed, short-range source ([wideband rectenna study](https://www.researchgate.net/publication/304563203_A_wideband_rectenna_for_24_GHz-band_RF_energy_harvesting)).
- State-of-the-art quantum-assisted rectennas (Nature Electronics) target ambient signals **below -20 dBm** — and their stated ceiling of ambition is powering IoT sensors ([Live Science coverage](https://www.livescience.com/technology/electronics/wi-fi-and-bluetooth-signals-can-be-harvested-to-power-small-devices)).

**Verdict:** provable, and bounded. Bluetooth/BLE harvesting powers sensors and node electronics (µW class). It will never power compute. Same six-to-seven-order-of-magnitude wall as the last scrape, now confirmed for the 2.4 GHz band specifically.

## Part C — Mesh technology: a topology, not an energy source

Honest scope note: the mesh-specific search was folded into the other rounds, so this is the thinnest section — flagged per SOP. What the captures establish: mesh (Bluetooth Mesh, Zigbee/802.15.4 at 2.4 GHz) is a **communication topology** — nodes relay each other's packets to extend range ([Wikipedia, 2.4 GHz radio use](https://en.wikipedia.org/wiki/2.4_GHz_radio_use)).

The physics: **relaying consumes energy; it does not create it.** Every hop in a mesh is a device spending power to transmit. A mesh network's ambient RF is the same µW/cm² environment as any radio, no denser in any capturable sense than the traffic itself. Where mesh becomes *relevant* to the structure: as the **nervous system** of a distributed harvesting deployment — BLE-mesh sensor nodes are exactly the µW-class devices RF harvesting can power ([the 423 µW system explicitly pairs with BLE environments](https://pmc.ncbi.nlm.nih.gov/articles/PMC9227311/)). Mesh is the plumbing for a feeding-window network, not the food.

## Part D — Crypto mining: this is where the structure is REAL

**Heat capture from mining is commercial, at scale, today.** Nearly all the electricity a miner consumes becomes heat, and capturing it is now done in production:

- **Finland, district heating:** joint mining+heating operations are running now — Terahash Energy's "Genesis" project sends mining waste heat to industry and homes; Hashlabs hosts six miner-to-district-heating sites ([Grist, Jan 2026](https://grist.org/buildings/bitcoin-cryptocurrency-district-heat-finland/)). MARA integrated mining into **two existing Finnish district heating systems in under 30 days**, delivering megawatts of heat ([MARA](https://www.mara.com/posts/beyond-the-blockchain-how-bitcoin-mining-powers-clean-low-cost-district-heating) ⚠ miner self-report).
- **Canada:** Mintgreen's "Digital Boilers" (immersion-cooled miners) supply a **12-year heat purchase agreement** to North Vancouver's city-owned utility — 100 buildings, 7,000 apartments ([K33 Research](https://k33.com/research/archive/articles/repurposing-waste-heat-from-bitcoin-mining-can-lower-heating-costs-and) ⚠ crypto research shop).
- **Home scale exists:** a ~$900 heater that is also a miner ([CNBC](https://www.cnbc.com/2025/11/16/bitcoin-crypto-mining-home-heating-energy-bills.html)) — skeptics quoted on efficiency, but the device proves the residential form factor.

**The feeding-window structure itself is a proven grid mechanism.** This is the part that verifies:

- Miners are an **"economic battery"** — they "curtail demand within minutes and join demand response programs," converting surplus renewable generation into value "without physical infrastructure, without degradation, with unlimited cycling" ([peer-reviewed review, Energy Reviews](https://www.sciencedirect.com/science/article/pii/S2590174525005458)).
- **Live precedent:** during Winter Storm Elliott (Dec 2022), Texas miners curtailed **>1.5 GW within minutes** to stabilize the grid; West Texas operations absorbed 1.3 TWh of otherwise-curtailed wind in 2022 ([Blink](https://www.blink.sv/blog/how-bitcoin-mining-supports-power-grids-and-renewable-energy) ⚠ advocacy site — the curtailment programs themselves are documented by the grid operators).
- Operators already run the exact schedule described: **feed during surplus windows** (cheap midday solar, overnight wind), **curtail during scarcity**, capture the energy as heat the whole time ([arbitrage-window pattern](https://nicosmid.substack.com/p/how-flexible-loads-are-reshaping); [CPower](https://cpowerenergy.com/vpps-and-flexible-demand-response-bitcoin-mining-flexes-its-capabilities/)).

So: **feed on a window → capture (heat) → store (district/water thermal mass) → replenish/release on schedule** is not speculative. It's running, at megawatt scale, on two continents.

## The honesty flags (non-negotiable)

1. **Heat reuse does not make mining green.** The strongest journalism on this says it straight: mining heat recovery is "a positive side-effect that largely has a negative climate impact, not something that we want to incentivize" ([Grist](https://grist.org/buildings/bitcoin-cryptocurrency-district-heat-finland/)). Peer-reviewed numbers: PoW mining runs 100-130 TWh/yr with 48.6-64.4 Mt CO2 ([Energy Reviews](https://www.sciencedirect.com/science/article/pii/S2590174525005458)). If the lab ever touches this, it's as *heat customers* or *load-shaping participants*, never as "green mining."
2. **Scale mismatch, stated plainly:** the proven implementations are megawatt district systems. A single home ASIC is ~3 kW — ~300 idle Mac Minis. A lab-scale version exists (heater-miner form factor) but its provable product is room heat plus a mining payout, not computer power.
3. **RF capture of mining rigs specifically:** miners emit EMI, not harvestable power. No source found claiming useful RF capture from mining hardware. (Negative result, logged.)

## Verdict — is the structure possible?

**Yes — in the thermal and scheduling lane, where it is already running.** The provable assembly:

| element | status |
|---|---|
| Bluetooth/radio capture | PROVEN, µW ceiling (sensors/nodes only) |
| mesh as energy source | NOT an energy source — it's the communication layer for a network of µW harvesters |
| mining energy capture | PROVEN as heat capture, ~100% of input, commercial at district and home scale |
| scheduled feeding windows | PROVEN — demand response + arbitrage windows are live grid mechanisms |
| closed circuit (recycle + replenish) | PROVEN in the thermal lane — heat stored and released on schedule displaces other heating |

**No — in the RF lane as a power source for compute.** That wall is physical and now twice-confirmed.

The one-sentence version: **the feeding-window recycling structure is real and running at industrial scale — as heat economics, not as radio. The radio is for the sensors; the schedule is for the grid; the heat is the battery.** Ready for whatever she posits next. /ziggy
