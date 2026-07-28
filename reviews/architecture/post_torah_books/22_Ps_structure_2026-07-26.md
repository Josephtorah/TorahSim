# Psalms (Ps) — deeper structure

**Date:** 2026-07-26  
**Kind:** post-Torah structure report · **hypothesis** · not binding law  
**Layer:** Writings · Liturgical API  
**Metrics source:** `_scan_data.json` (morphhb WLC)  
**Index:** [INDEX.md](INDEX.md)

---

## 1. Scale

| Metric | Value |
|--------|------:|
| Chapters | 150 |
| Verses | 2527 |
| Avg verses/chapter | 16.8 |
| Densest chapters | ch.119(176vv), ch.78(72vv), ch.89(53vv), ch.18(51vv) |

**Open:** `Ps 1:1` — אשרי האיש אשר לא הלך בעצת רשעים ובדרך חטאים לא עמד ובמושב לצים לא ישב  
**Close:** `Ps 150:6` — כל הנשמה תהלל יה הללו יה

**Theme verse-hits (Strong’s presence per verse, top):** YHWH=627, Elohim=322, land_eretz=188, day_yom=107, wicked=80, king_melek=63, righteous=50, spirit_ruah=39

---

## 2. Literary / structural arc

| # | Block |
|---|--------|
| 1 | 1–41 Book I |
| 2 | 42–72 Book II |
| 3 | 73–89 Book III |
| 4 | 90–106 Book IV |
| 5 | 107–150 Book V (incl. 119 mega; Hallel; Songs of Ascents; final hallelujahs) |

**Structure note:** Five-book psalter; genres mixed (lament, praise, royal, wisdom, Zion). Ps 119 longest chapter in Tanakh scan.

**Structural signals:** Five book seams (41,72,89,106,150); acrostic 119.

---

## 3. Computer-model role

Userland syscalls for prayer-state; BR’s densest non-Gen shelf; always-on UI library.

**Candidate ops:** `PRAY_LAMENT`, `PRAISE`, `ROYAL_PSALM`, `TORAH_DELIGHT`, `LIGHT_FACE`, `HALLELUJAH_CLOSE`

---

## 4. Link to Torah main

Torah meditation (1, 19, 119); Exodus memory; kingship under YHWH.

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
