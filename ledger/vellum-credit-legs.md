# Vellum credit ledger legs — append-only

Standing rule: **pulling a credit reading creates a ledger obligation.** File the leg in the same turn as the reading. This file carries the running series; VL-002 in the vault carries the subscription record itself.

All figures are plan credit (Vellum Super, $55.00/month allowance). The $100.00/month price and the $55.00 plan credit are DIFFERENT numbers.

| # | Reading (UTC) | Remaining | Used | Expiring ≤30d | Next expiry | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-09-23 ~10:47 | $25.15 of $35.00 | 28% | $24.93 | 2026-10-23 | pre-Super; $35 plan credit era (VL-002) |
| 2 | 2026-09-28 12:17 (PM ET) | $24.41 of $55.00 | 56% | $4.20 | 2026-10-23 | first Super-era reading |
| 3 | 2026-09-28 20:46 | $21.68 of $55.00 | 61% | $1.46 | 2026-10-23 | verified twice, 25s apart, stable |
| 4 | 2026-09-28 21:46 | $21.63 of $55.00 | 61% | $1.41 | 2026-10-23 | settled $21.63, pending $0.00, no daily limit set |

**Supersedes:** the published-card candidate figure is now **$21.63 / 61% of $55.00, checked 2026-09-28**. The $24.41 / 56% figure was published in the Sep 28 site mirror-sweep prompt and is now stale by two legs ($2.78 spent in ~9.5 hours).

**Rate observation (not a projection):** legs 2 → 4 = $2.78 over ~9.5 hours on a heavy flight day. No extrapolation is filed; the allowance is monthly and the spend pattern is bursty.

_Filed 2026-09-28, Ziggy. Append new legs at the bottom; never edit a prior leg._
| 5 | 2026-09-28 22:46 | $21.54 of $55.00 | 61% | $1.32 | 2026-10-23 | heartbeat reading; settled $21.54, pending $0.00, no daily limit set |

**Supersedes:** running figure is now **$21.54 / 61% of $55.00, checked 2026-09-28 22:46 UTC** (leg 4's $21.63 is one hour stale).
| 6 | 2026-09-29 19:07 | $18.41 of $55.00 | 67% | $0.00 | 2026-11-23 | heartbeat reading; settled $18.41, pending $0.00; expiry line now reads 2026-11-23 (prior legs read 2026-10-23) — noted, not interpreted |
| 7 | 2026-09-29 20:06 | $18.33 of $55.00 | 67% | $0.00 | 2026-11-23 | heartbeat reading; settled $18.33, pending $0.00, no daily limit set; 8c drift over ~1 hour since leg 6 (live meter, consistent with Sep 28's nine-cents-in-one-hour observation) |

**Supersedes:** running figure is now **$18.33 / 67% of $55.00, checked 2026-09-29 20:06 UTC** (leg 6's $18.41 is ~1 hour stale).

| 8 | 2026-09-29 21:06 | $18.26 of $55.00 | 67% | $0.00 | 2026-11-23 | heartbeat reading; settled $18.26, pending $0.00, no daily limit set; 7c drift over ~1 hour since leg 7 |

**Supersedes:** running figure is now **$18.26 / 67% of $55.00, checked 2026-09-29 21:06 UTC** (leg 7's $18.33 is ~1 hour stale).
