# Exodus Build — thin install after Genesis handoff

**Date:** 2026-07-21  
**Kind:** build approach (Pre-Code) — **not** binding law  
**Status:** **full draft complete** — all 40 thorough blocks (Exod 1–40 / 1213 verses)

**Related:**  
- Genesis complete draft: `GENESIS_BUILD_2026-07-20.md` · `ARCHITECTURE_genesis_stack_2026-07-21.md`  
- Observations: `NOTES_progress_observations_2026-07-20.md`  
- Oral policy: `RESEARCH_valid_oral_torah_2026-07-19.md` (Mekhilta for Exod law decode)  
- Lev needs Exod stage: `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md`  
- Units: `logic/units/exo_*.yaml` (45 files)  
- Generator (re-run / extend): `artifacts/generate_exodus_units.py`

On substantive update: rename to today’s date and fix links.

---

## 1. Purpose

Wire **Exodus** so a full system run can continue after Genesis:

```text
Genesis boot/sagas → Exodus (nation pressure + law + sanctuary install) → Lev apps
```

**Mode used:** one **manageable block** at a time, each with trees + logic + Oral policy; owner authorized autonomous “next” through the whole schedule.

---

## 2. Thorough-pass checklist (every block)

| Step | What | Status |
|------|------|--------|
| 1. Written Hebrew | `Data/Exod.xml` derivation | done (all blocks) |
| 2. Trees | `taamim_tree_parse.py` v1 every verse → `binary_trees` + `tree_ascii` | **1213/1213** |
| 3. Logic shape | `boot_steps` + `state_machine`; law blocks also `decision_table` | done draft |
| 4. he+translit+en | Structured fields | done (verse linear en = free gloss [EN-AID]) |
| 5. Oral dual-track | Named; never silent-merge | done |
| 6. Mekhilta | Extensive samples on primary/strong law strips from `Data/mekhilta_*` | done where corpus non-empty |
| 7. Coverage | `tree_coverage` provisional roles | done heuristic |
| 8. Confidence | hypothesis / tested — not binding law | labeled |

---

## 3. Oral open order (Exodus)

| Block type | Prefer first Oral (among possibles) |
|------------|-------------------------------------|
| Narrative | Written first; midrash/Bavli dual-track when thickening |
| Law / covenant case | **Mekhilta** → MH + cite_index Bavli → optional Mishnah |
| Sanctuary build | Written blueprint first; Mekhilta/Bavli dual-track on disputes (esp. Shabbat vs work) |

MH endpoints remain **possible Oral** (standing §5).

**Mekhilta local density:** Sefaria-index chapters **12–23, 31, 35** have text; empty indexes do not invent midrash. Units on empty shelves keep dual-track policy + midrash/Bavli possible Oral.

---

## 4. Block map (complete draft)

| # | Unit id | Refs | ~vv | Genre | Mekh | Status |
|---|---------|------|-----|-------|------|--------|
| 01 | `exo_01_israel_egypt_oppression` | 1:1–22 | 22 | narrative | thin | **draft** |
| 02 | `exo_02_moses_midian` | 2:1–25 | 25 | narrative | thin | **draft** |
| 03 | `exo_03_bush_call` | 3:1–22 | 22 | narrative | thin | **draft** |
| 04 | `exo_04_signs_return` | 4:1–31 | 31 | narrative | thin | **draft** |
| 05 | `exo_05_bricks_worse` | 5:1–23 | 23 | narrative | thin | **draft** |
| 06 | `exo_06_name_roster` | 6:1–30 | 30 | narrative | thin | **draft** |
| 07 | `exo_07_staff_blood` | 7:1–29 | 29 | narrative | thin | **draft** |
| 08 | `exo_08_frogs_to_swarm` | 8:1–28 | 28 | narrative | thin | **draft** |
| 09 | `exo_09_livestock_hail` | 9:1–35 | 35 | narrative | thin | **draft** |
| 10 | `exo_10_locust_dark` | 10:1–29 | 29 | narrative | thin | **draft** |
| 11 | `exo_11_last_warning` | 11:1–10 | 10 | narrative | thin | **draft** |
| 12a | `exo_12_pesach_command` | 12:1–28 | 28 | decision | **primary** | **draft** + Mekh samples |
| 12b | `exo_12_midnight_leave` | 12:29–51 | 23 | narrative | **primary** | **draft** + Mekh samples |
| 13a | `exo_13_firstborn_matzot` | 13:1–16 | 16 | decision | **primary** | **draft** + Mekh samples |
| 13b | `exo_13_route_pillar` | 13:17–22 | 6 | narrative | medium | **draft** |
| 14 | `exo_14_sea` | 14:1–31 | 31 | narrative | **strong** | **draft** + Mekh samples |
| 15a | `exo_15_song` | 15:1–21 | 21 | narrative | **strong** | **draft** + Mekh samples |
| 15b | `exo_15_marah` | 15:22–27 | 6 | narrative | **strong** | **draft** + Mekh samples |
| 16 | `exo_16_manna_shabbat` | 16:1–36 | 36 | decision | **primary** | **draft** + Mekh samples |
| 17 | `exo_17_water_amalek` | 17:1–16 | 16 | narrative | **strong** | **draft** + Mekh samples |
| 18 | `exo_18_yitro` | 18:1–27 | 27 | narrative | **strong** | **draft** + Mekh samples |
| 19 | `exo_19_sinai_prep` | 19:1–25 | 25 | narrative | **primary** | **draft** + Mekh samples |
| 20 | `exo_20_decalogue_altar` | 20:1–26 | 26 | decision | **primary** | **draft** + Mekh samples |
| 21a | `exo_21_slave_person` | 21:1–27 | 27 | decision | **primary** | **draft** + Mekh samples |
| 21b | `exo_21_ox_pit` | 21:28–37 | 10 | decision | **primary** | **draft** + Mekh samples |
| 22 | `exo_22_property_social` | 22:1–30 | 30 | decision | **primary** | **draft** + Mekh samples |
| 23a | `exo_23_justice_calendar` | 23:1–19 | 19 | decision | **primary** | **draft** + Mekh samples |
| 23b | `exo_23_escort_land` | 23:20–33 | 14 | narrative | **strong** | **draft** + Mekh samples |
| 24 | `exo_24_covenant_ascent` | 24:1–18 | 18 | narrative | medium | **draft** (Mekh index empty) |
| 25 | `exo_25_ark_table_menorah` | 25:1–40 | 40 | boot | thin | **draft** |
| 26 | `exo_26_curtains_boards` | 26:1–37 | 37 | boot | thin | **draft** |
| 27 | `exo_27_altar_court` | 27:1–21 | 21 | boot | thin | **draft** |
| 28 | `exo_28_priest_garments` | 28:1–43 | 43 | boot | thin | **draft** |
| 29 | `exo_29_investiture` | 29:1–46 | 46 | boot | thin | **draft** |
| 30 | `exo_30_incense_shekel` | 30:1–38 | 38 | decision | medium | **draft** + some Mekh |
| 31 | `exo_31_craftsmen_shabbat` | 31:1–18 | 18 | decision | **primary** | **draft** + Mekh samples |
| 32 | `exo_32_golden_calf` | 32:1–35 | 35 | narrative | medium | **draft** |
| 33 | `exo_33_presence` | 33:1–23 | 23 | narrative | medium | **draft** |
| 34 | `exo_34_second_tablets` | 34:1–35 | 35 | narrative | medium | **draft** |
| 35a | `exo_35_shabbat_donate` | 35:1–29 | 29 | decision | **primary** | **draft** + Mekh samples |
| 35b | `exo_35_36_work_start` | 35:30–36:38 | 44 | boot | thin | **draft** |
| 37 | `exo_37_furniture_made` | 37:1–29 | 29 | boot | thin | **draft** |
| 38 | `exo_38_court_inventory` | 38:1–31 | 31 | boot | thin | **draft** |
| 39 | `exo_39_garments_done` | 39:1–43 | 43 | boot | thin | **draft** |
| 40 | `exo_40_erect_fill` | 40:1–38 | 38 | boot | thin | **draft** — Lev handoff |

**Totals:** 45 unit files · **1213** verse trees · all chapters 1–40.

---

## 5. Phase summary

| Phase | Blocks | Content | Oral emphasis |
|-------|--------|---------|----------------|
| **A** Egypt narrative | 01–11 | Oppression → plagues → last warning | Written + midrash dual-track |
| **B** Mekhilta spine | 12a–24 | Pesach → sea → Sinai → mishpatim → covenant | **Mekhilta extensive** (where corpus has text) |
| **C** Sanctuary specs | 25–31 | Blueprints, garments, shekel, Shabbat seal | Written install; Mekhilta on shekel/Shabbat |
| **D** Breach & renew | 32–34 | Calf, presence, second tablets | Dual-track midrash/Bavli |
| **E** Build & fill | 35a–40 | Execute + cloud → **Lev free names** | Written; Shabbat dual-track |

---

## 6. Known draft limits (honest)

1. **Verse English linear glosses** are short free [EN-AID] stubs; boot_steps carry the real English narrative of each strip.  
2. **tree_coverage roles** are heuristic (glue / person / leaf) — not full TIR-xxx yet.  
3. **Mekhilta samples** are first paragraphs per strip, dual-track only — not a complete case commentary on every mishpat.  
4. **Decision tables** are hypothesis IF/THEN sketches for law blocks — deepen with Mekhilta + MH next pass if desired.  
5. **Not frozen** — no interpreter load claim; not binding religious law.

---

## 7. Suggested next (after full Exodus draft)

1. Thin **Lev free-name resolve** using `exo_40` / mishkan exports (altar, ohel, kohen, tamid, …).  
2. Deeper **Mekhilta + decision_table** pass on highest-value law units (12, 20–23, 31, 35).  
3. Optional denser verse English from a labeled EN aid (still never derivation source).  
4. Resume Sifra/Lev curriculum when ready (`STANDING_DECISIONS` §4).

---

## 8. One-sentence summary

**Exodus Build = 45 Pre-Code draft units covering all 1213 verses of Exodus with ta'amim trees, sequential/install logic, and Mekhilta dual-track samples on the law spine — sanctuary filled and ready for Leviticus free names.**
