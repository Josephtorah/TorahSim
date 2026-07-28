# Round 5 — Pass 03: Formula / operator stack density

**Date:** 2026-07-23  
**Question:** Which midrash operators dominate, and which chapters are operator-hot?

---

## Observed — corpus formula hit totals

| Operator | Approx. hits |
|----------|-------------:|
| zeh | 1070 |
| ela | 1035 |
| sheneemar | 799 |
| beshem | 631 |
| mashal | 482 |
| hada_hu | 431 |
| lama | 293 |
| davar_acher | 214 |
| patah | 205 |
| minayin | 174 |
| keneged | 113 |
| lefikakh | 111 |

**Identity/restrictive glue** (zeh / ela) and **proof** (sheneemar, hada hu) outrun list/parable openers. Beshem (in the name of…) is a major **attribution bus**.

### Top chapters by composite (formula hits + marked cites)

| Ch | Composite | Per-sec | Formula hits | Cites |
|---:|----------:|--------:|-------------:|------:|
| 98 | 247 | 12.35 | 116 | 131 |
| 99 | 247 | 20.58 | 129 | 118 |
| 1 | 237 | 15.8 | 140 | 97 |
| 44 | 235 | 10.22 | 130 | 105 |
| 65 | 234 | 10.17 | 118 | 116 |
| 84 | 225 | 10.23 | 125 | 100 |
| 75 | 210 | 16.15 | 106 | 104 |
| 63 | 201 | 14.36 | 106 | 95 |
| 68 | 193 | 13.79 | 93 | 100 |
| 12 | 189 | 11.81 | 117 | 72 |
| 48 | 188 | 9.4 | 100 | 88 |
| 91 | 186 | 16.91 | 95 | 91 |

Ch **99** and **1** score very high **per section** (dense install / dense close). Ch **98, 44, 65, 84** are bulk composite hubs.

### Band formula presence (hit counts)

- **early:** {'patah': 44, 'davar_acher': 19, 'mashal': 107, 'ela': 210, 'hada_hu': 83, 'beshem': 168, 'sheneemar': 206, 'minayin': 57, 'zeh': 181, 'lama': 59, 'lefikakh': 21, 'keneged': 28}
- **mid:** {'sheneemar': 304, 'hada_hu': 174, 'ela': 396, 'beshem': 244, 'zeh': 395, 'mashal': 158, 'minayin': 53, 'patah': 79, 'lefikakh': 36, 'davar_acher': 78, 'lama': 101, 'keneged': 34}
- **late:** {'sheneemar': 289, 'hada_hu': 174, 'ela': 429, 'zeh': 494, 'beshem': 219, 'mashal': 217, 'lama': 133, 'lefikakh': 54, 'minayin': 64, 'davar_acher': 117, 'patah': 82, 'keneged': 51}

---

## Hypothesis

There is a **shared middleware stack** used book-wide; hot chapters combine **narrative mass + operator + proof**. Front (ch.1) and end (ch.99) are operator-dense relative to length—boot and export configs.

**Confidence:** tested (regex hits; some operators noisy).
