# Deuteronomy Build — recompile after Numbers ops

**Date:** 2026-07-24  
**Kind:** build approach (Pre-Code) — **not** binding law  
**Status:** **full draft + tree_derived_v1** — 41 units · 959 STEPs; reprocess `DEUTERONOMY_TREE_DERIVE_2026-07-24.md` · `artifacts/reprocess_book_from_trees.py --book deu`  

**Related:**  
- Tree-derive track: `DEUTERONOMY_TREE_DERIVE_2026-07-24.md`  
- Numbers handoff: `NUMBERS_BUILD_2026-07-24.md` · `num_36_heiresses`  
- Oral: **Sifrei Devarim** (`Data/sifrei_devarim_he.json`); MH possible  
- Units: `logic/units/deu_*.yaml`  
- Data: `Data/Deut.xml`  

On substantive update: rename to today’s date and fix links.

---

## 1. Purpose

Wire **Deuteronomy** so the system run continues after Numbers land-prep:

```text
Genesis → Exodus (install) → Leviticus (apps) → Numbers (ops) → Deuteronomy (recompile / handoff)
```

Deuteronomy is mostly **recompile + covenant speech**: historical review, Decalogue/Shema restatement, central-sanctuary law code, ceremony and blessings/curses, Moab covenant, Joshua handoff, song, blessing, Moses’ death.

It does **not** re-boot the mishkan from scratch. Free names resolve to:

| Class | Examples |
|-------|----------|
| **GEN_AMBIENT** | People/land promise memory |
| **EXOD_IMPORT** | Horeb, Decalogue, Tent background, cloud |
| **LEV_IMPORT** | Purity/food types, festival skeletons, blood center |
| **NUM_IMPORT** | Spies/refusal, east kings, refuge cities, Joshua, Amalek seed |
| **DEU_LOCAL** | Place-He-chooses, king law, prophet-like-Moses, Moab covenant, Ha'azinu |

**Mode:** one manageable block at a time (**41** total). Same spirit as Num/Lev.

**Target size:** ~7–40 verses/block; long lists (curses, Ha'azinu) may run longer.

---

## 2. Thorough-pass checklist (every block)

1. **Written Hebrew** — `Data/Deut.xml`; English only `[EN-AID]`.  
2. **Trees** — `taamim_tree_parse.py` v1 every verse → `binary_trees` + `tree_ascii`.  
3. **Logic shape** — `boot_steps` / `decision_table` / narrative FSM; he+translit+en on atoms.  
4. **Imports** — Gen/Exod/Lev/Num free names in `depends_on`.  
5. **Oral dual-track** — **Sifrei Devarim** when law densifies; MH possible; never silent-merge.  
6. **Coverage** — `tree_coverage` provisional roles.  
7. **Scenarios** — small expect-after-step checks.  
8. **Confidence** — hypothesis / tested — **not binding religious law**.

---

## 3. Book size

**34** chapters · **959** verses (OSIS / `Data/Deut.xml`).

---

## 4. Ten phases (locked) · 41 units

| Phase | Chapters | Units | ~vv | Content |
|-------|----------|------:|----:|---------|
| **A** | 1–3 | 6 | 112 | Historical prologue |
| **B** | 4–6 | 4 | 107 | Law frame / Decalogue / Shema |
| **C** | 7–11 | 5 | 129 | Loyalty / land / second tablets |
| **D** | 12–14 | 3 | 79 | Place-name / seducers / food-tithe |
| **E** | 15–18 | 4 | 87 | Release / festivals / king / prophet |
| **F** | 19–22 | 4 | 93 | Refuge / war / family / social |
| **G** | 23–26 | 4 | 86 | Assembly / divorce / courts / firstfruits |
| **H** | 27–28 | 4 | 95 | Ceremony + blessings/curses |
| **I** | 29–30 | 2 | 48 | Moab covenant |
| **J** | 31–34 | 5 | 123 | Joshua / song / blessing / death |

### Unit map

| Phase | Unit id | Refs |
|-------|---------|------|
| A | `deu_01_frame_officers` | 1:1–18 |
| A | `deu_01_spies_refuse` | 1:19–46 |
| A | `deu_02_bypass_nations` | 2:1–25 |
| A | `deu_02_sihon` | 2:26–37 |
| A | `deu_03_og_gilead` | 3:1–22 |
| A | `deu_03_moses_barred` | 3:23–29 |
| B | `deu_04_obey_horeb` | 4:1–40 |
| B | `deu_04_refuge_east` | 4:41–49 |
| B | `deu_05_decalogue` | 5:1–33 |
| B | `deu_06_shema` | 6:1–25 |
| C | `deu_07_nations_cherem` | 7:1–26 |
| C | `deu_08_manna_humility` | 8:1–20 |
| C | `deu_09_not_righteousness` | 9:1–29 |
| C | `deu_10_second_tablets` | 10:1–22 |
| C | `deu_11_bless_curse_set` | 11:1–32 |
| D | `deu_12_place_name` | 12:1–31 |
| D | `deu_13_seducers` | 13:1–19 |
| D | `deu_14_food_tithe` | 14:1–29 |
| E | `deu_15_release_firstborn` | 15:1–23 |
| E | `deu_16_festivals_judges` | 16:1–22 |
| E | `deu_17_courts_king` | 17:1–20 |
| E | `deu_18_levi_prophet` | 18:1–22 |
| F | `deu_19_miklat_witness` | 19:1–21 |
| F | `deu_20_war_rules` | 20:1–20 |
| F | `deu_21_eglah_family` | 21:1–23 |
| F | `deu_22_return_sex_laws` | 22:1–29 |
| G | `deu_23_qahal_purity_vows` | 23:1–26 |
| G | `deu_24_divorce_poor` | 24:1–22 |
| G | `deu_25_courts_yibbum` | 25:1–19 |
| G | `deu_26_bikkurim_close` | 26:1–19 |
| H | `deu_27_ebal_curses` | 27:1–26 |
| H | `deu_28_blessings` | 28:1–14 |
| H | `deu_28_curses_a` | 28:15–44 |
| H | `deu_28_curses_b` | 28:45–69 |
| I | `deu_29_moab_covenant` | 29:1–28 |
| I | `deu_30_teshuvah_choice` | 30:1–20 |
| J | `deu_31_charge_torah` | 31:1–30 |
| J | `deu_32_haazinu` | 32:1–43 |
| J | `deu_32_song_aftermath` | 32:44–52 |
| J | `deu_33_ve_zot` | 33:1–29 |
| J | `deu_34_moses_death` | 34:1–12 |

---

## 5. Tool

```bash
python3 artifacts/reprocess_book_from_trees.py --book deu --phase A   # … through J
python3 artifacts/reprocess_book_from_trees.py --book deu            # all
```

UNIT_SPECS inside `reprocess_book_from_trees.py` supply first-draft meta when no prior YAML exists.

---

## Changelog

- 2026-07-24: Track opened; 10-phase map locked; full book tree_derived_v1 (41 units · 959 STEPs).
