# 1 Samuel (1Sam) — deeper structure

**Date:** 2026-07-26  
**Kind:** post-Torah structure report · **hypothesis** · not binding law  
**Layer:** Former Prophets · History OS  
**Metrics source:** `_scan_data.json` (morphhb WLC)  
**Index:** [INDEX.md](INDEX.md)

---

## 1. Scale

| Metric | Value |
|--------|------:|
| Chapters | 31 |
| Verses | 811 |
| Avg verses/chapter | 26.2 |
| Densest chapters | ch.17(58vv), ch.14(52vv), ch.25(44vv), ch.20(42vv) |

**Open:** `1Sam 1:1` — ויהי איש אחד מן הרמתים צופים מהר אפרים ושמו אלקנה בן ירחם בן אליהוא בן תחו בן צוף אפרתי  
**Close:** `1Sam 31:13` — ויקחו את עצמתיהם ויקברו תחת האשל ביבשה ויצמו שבעת ימים

**Theme verse-hits (Strong’s presence per verse, top):** YHWH=240, day_yom=131, Elohim=90, king_melek=75, land_eretz=45, spirit_ruah=14, exile_galah=13, covenant_berit=7

---

## 2. Literary / structural arc

| # | Block |
|---|--------|
| 1 | 1–7 Samuel birth, Shiloh failure, ark capture/return, Mizpah |
| 2 | 8–12 Request for king; Saul anointed; kingdom “renewed” |
| 3 | 13–15 Saul’s failures (unlawful sacrifice, Amalek) |
| 4 | 16–31 David rise; Saul pursuit; Saul death |

**Structure note:** Transition architecture: priest/judge → prophet → king. Parallel tracks Saul vs David after ch.16.

**Structural signals:** “Give us a king”; spirit leaves Saul; David anointed mid-book.

---

## 3. Computer-model role

Architecture migration PR: add king API; first implementation (Saul) fails acceptance tests; David branch opened.

**Candidate ops:** `MIGRATE_TO_MONARCHY`, `INSTALL_KING_TYPE`, `REJECT_PARTIAL_OBEY`, `ANONY_DAVID_SEED`

---

## 4. Link to Torah main

Kingship debated against Deut king-law background; ark/tabernacle continuity from Torah cult.

**Access pattern (default project model):** Torah remains **main**; this book is typically **history runtime**, **policy handler**, **library/UI**, or **restore/logger** — not a second main. Cosmic/wisdom shelves may **export** symbols Torah **lazy-resolves**.

---

## 5. Confidence & fence

| Claim | Label |
|-------|--------|
| Chapter/verse metrics | **tested** (OSHB/morphhb counts) |
| Arc divisions | **hypothesis** (standard literary map) |
| Computer-model role | **hypothesis** |
| Binding law | **no** |

Not a full tree-derive of every verse. Deeper STEPs only where other tracks already derived (e.g. Prov 8 block, BR pins).
