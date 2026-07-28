# Sifra (Leviticus) → Talmud link catalog

**Simple idea:** Every place tradition links a **Sifra** unit to a **Talmud** page.  
Sifra is the midrash that walks **Leviticus**, so this is the practical answer to:

> “Where does this Lev/Sifra material show up in the Talmud?”

---

## Why this file exists (and what we are *not* building)

We started toward a **home-grown parallel index** (Sifra↔Talmud, then maybe more).  
That job is already done by **Mesorat haShas** / *mesorat ha-shas* / מסורת הש״ס — traditional “see also” parallels.

| | |
|--|--|
| **Source of truth** | `Data/links*.csv`, `Conection Type` = `mesorat hashas` (~48k edges, all works) |
| **This folder’s files** | **Filtered extracts only** — convenience for Sifra/Lev work |
| **Decision** | **Do not reinvent** a global Oral↔Oral parallel crawler |
| **Recorded** | `README.md` (standing decision) · `DISCOVERIES_2026-07-19.md` Pass 7 |

**Still ours (not replaced by MH):** cite_index, operator_index, Pre-Code logic units, ta’amim trees.

## Files
| File | Use |
|------|-----|
| `sifra_talmud_links_2026-07-18.tsv` | **Easiest** — open in Excel/Sheets; filter columns |
| `sifra_talmud_links_2026-07-18.json` | Full machine list (`links[]`) |
| `sifra_talmud_links_compact_2026-07-18.json` | Counts + all Talmud loci per Sifra section |
| `LEV1_SIFRA_TALMUD_2026-07-19.md` | Lev 1–area readable subset |

## Totals
- **2141** unique Sifra ↔ Talmud pairs
- Almost all connection type: **mesorat hashas** (traditional parallel)
- Source: `Data/links*.csv` (not a new discovery graph — a **view** of MH)

## By Leviticus area (Sifra section)
| Links | Sifra section | Lev range (approx) |
|------:|---------------|--------------------|
| 386 | Vayikra Dibbura d'Chovah | Lev 4–5 (approx) |
| 275 | Emor | Lev 21–24 (approx) |
| 275 | Tzav | Lev 6–8 (approx) |
| 242 | Vayikra Dibbura d'Nedavah | Lev 1–3 (approx) |
| 212 | Acharei Mot | Lev 16–18 (approx) |
| 164 | Kedoshim | Lev 19–20 (approx) |
| 132 | Shemini | Lev 9–11 (approx) |
| 119 | Bechukotai | Lev 26:3–27 (approx) |
| 97 | Behar | Lev 25–26:2 (approx) |
| 90 | Metzora Parashat Zavim | Lev 15 |
| 67 | Metzora | Lev 14 |
| 32 | Tazria Parashat Yoledet | Lev 12 |
| 28 | Tazria Parashat Nega'im | Lev 13 |
| 22 | Braita d'Rabbi Yishmael | — (13 middot intro) |

## Top Talmud tractates
| Links | Tractate |
|------:|----------|
| 324 | Zevachim |
| 238 | Menachot |
| 145 | Yoma |
| 133 | Shevuot |
| 109 | Chullin |
| 96 | Yevamot |
| 95 | Sanhedrin |
| 90 | Keritot |
| 75 | Niddah |
| 72 | Pesachim |
| 66 | Arakhin |
| 62 | Bekhorot |
| 58 | Kiddushin |
| 54 | Horayot |
| 53 | Temurah |
| 47 | Bava Kamma |
| 43 | Shabbat |
| 41 | Rosh Hashanah |
| 35 | Bava Metzia |
| 32 | Meilah |

## Example rows
```text
Sifra, Acharei Mot, Section 1 13
  → Yoma 53a:18  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 1 5
  → Zevachim 18b:13  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 7
  → Chullin 101a:7-9  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 4
  → Meilah 10a:6  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 4
  → Menachot 12b:2  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 3
  → Menachot 20a:11  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 4
  → Menachot 21b:4  (Lev 16–18 (approx))
Sifra, Acharei Mot, Chapter 10 4
  → Menachot 26b:13  (Lev 16–18 (approx))
```

## How to look up (examples)
**Lev 1–3 area (voluntary offerings):** filter TSV `parasha=Vayikra` and section Nedavah, or:
```bash
rg "Dibbura d'Nedavah" reviews/talmud_structure/sifra_talmud_links_2026-07-18.tsv | head
```
**Everything in Zevachim:**
```bash
rg "\tZevachim\t" reviews/talmud_structure/sifra_talmud_links_2026-07-18.tsv | head
```
**Lev 12 (childbirth / Tazria Yoledet):**
```bash
rg "Yoledet|Tazria Parashat Yoledet" reviews/talmud_structure/sifra_talmud_links_2026-07-18.tsv
```

## Honest limits
1. This is the **link catalog** tradition already marked — not a full word-for-word proof.
2. A Talmud page can still *sound like* Sifra without an edge here.
3. Lev chapter ranges are **by Sifra section**, not exact verse IDs per row.

Built for Torah_Grok Pass 6 follow-up.
