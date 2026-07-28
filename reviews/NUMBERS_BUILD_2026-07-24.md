# Numbers Build — ops / journey after Leviticus apps

**Date:** 2026-07-24  
**Kind:** build approach (Pre-Code) — **not** binding law  
**Status:** **full draft + tree_derived_v1 complete** — 47 units · 1289 STEPs; reprocess `NUMBERS_TREE_DERIVE_2026-07-24.md` · `artifacts/reprocess_book_from_trees.py --book num`

**Related:**  
- Continuity prompt: `PROMPT_continue_numbers_2026-07-24.md`  
- Leviticus full draft: `LEVITICUS_BUILD_2026-07-21.md` · units `logic/units/lev_*.yaml`  
- Exodus full draft: `EXODUS_BUILD_2026-07-21.md` · units `logic/units/exo_*.yaml`  
- Architecture stack: `ARCHITECTURE_genesis_stack_2026-07-21.md`  
- Oral policy: `RESEARCH_valid_oral_torah_2026-07-19.md` (**Sifrei Bamidbar** for Num law densification)  
- Units: `logic/units/num_*.yaml`  
- Generator: `artifacts/generate_numbers_units.py`  
- Data: `Data/Num.xml` · `Data/sifrei_bamidbar_he.json`

On substantive update: rename to today’s date and fix links.

---

## 1. Purpose

Wire **Numbers** so the system run continues after Leviticus sanctuary apps:

```text
Genesis → Exodus (install) → Leviticus (apps) → Numbers (ops / census / journey / tests) → Deuteronomy (recompile)
```

Numbers is mostly **operations**: census and camp layout, logistics of march, purity of the camp, case-law islands (sotah, nazir, red heifer, vows, cities of refuge), crisis narratives (spies, Korach, Meribah, Peor), and land-prep (second census, inheritance, borders).

It does **not** re-boot the mishkan or re-author Lev purity/korban type systems. Free names resolve to:

| Class | Examples |
|-------|----------|
| **EXOD_IMPORT** | ohel mo'ed, altar system, priest office, cloud/glory, trumpets seed |
| **LEV_IMPORT** | purity grades, korban types, YK/blood center as background |
| **GEN_AMBIENT** | people graph, land promise memory |
| **NUM_LOCAL** | census rules, camp order, nazir/sotah procedure, journey tests, inheritance cases |

**Mode (locked):** one **manageable thorough block** at a time (**47** total). Same spirit as Exodus/Lev — not one giant dump, not one unit per verse.

**Target size:** ~10–30 verses/block; census lists and dedication lists may run longer; dense case law stays shorter.

---

## 2. Thorough-pass checklist (every block)

1. **Written Hebrew** — derive from `Data/Num.xml`; English only as gloss `[EN-AID]`.  
2. **Trees** — `taamim_tree_parse.py` v1 for **every verse** → `binary_trees` + `tree_ascii`.  
3. **Logic shape** — `boot_steps` / `decision_table` / narrative **FSM** as genre fits; always he+translit+en on atoms.  
4. **Imports** — Gen/Exod/Lev free names in `depends_on` / notes; do not re-spec Tent.  
5. **Oral dual-track** — **Sifrei Bamidbar** when law densifies (`Data/sifrei_bamidbar_he.json`); MH possible; never silent-merge.  
6. **Coverage** — `tree_coverage` provisional roles.  
7. **Scenarios** — small expect-after-step checks.  
8. **Confidence** — hypothesis / tested — **not binding religious law**.

---

## 3. Oral open order (Numbers)

| Block type | Prefer first Oral (among possibles) |
|------------|-------------------------------------|
| Census / camp / march narrative | Written first; midrash/Bavli dual-track when thickening |
| Case law (sotah, nazir, parah, vows, refuge, inheritance) | **Sifrei Bamidbar** → MH + Bavli → optional Mishnah |
| Crisis narrative (spies, Korach, Meribah, Peor) | Written first; midrash dual-track named |
| Festival calendar restatement (28–29) | Written; Sifrei/Mishnah dual-track when densifying |

MH endpoints remain **possible Oral** (standing §5).  
Do **not** invent Sifrei text for empty shelves; sample only what is in the local dump.

---

## 4. Verse numbering note

Block refs follow **local `Data/Num.xml` / OSIS** (Hebrew MT chapter lengths). Trust XML `osisID` (`Num.C.V`). English Bible chapter splits occasionally differ (e.g. end of Korach / staff narrative) — use OSIS.

**Book size:** 36 chapters · **1289** verses (OSIS; note Num 25 has **19** vv in `Data/Num.xml`).

---

## 5. Locked block map (47)

**Sifrei** column: lean strength for dual-track samples.  
**Status:** pending | **draft** | done draft — all 47 currently **draft**.

### Phase A — Census and camp, ch. 1–4

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 01 | `num_01_census_command` | **1:1–19** | 19 | boot / registry | thin | **draft** |
| 02 | `num_01_tribe_counts` | **1:20–46** | 27 | registry | thin | **draft** |
| 03 | `num_01_levites_exempt` | **1:47–54** | 8 | decision | medium | **draft** |
| 04 | `num_02_camp_east_south` | **2:1–16** | 16 | boot / layout | thin | **draft** |
| 05 | `num_02_camp_west_north` | **2:17–34** | 18 | boot / layout | thin | **draft** |
| 06 | `num_03_aaron_levi_replace` | **3:1–13** | 13 | boot | medium | **draft** |
| 07 | `num_03_levite_clans_count` | **3:14–39** | 26 | registry | thin | **draft** |
| 08 | `num_03_firstborn_redeem` | **3:40–51** | 12 | decision | medium | **draft** |
| 09 | `num_04_kehat` | **4:1–20** | 20 | procedure | medium | **draft** |
| 10 | `num_04_gershon_merari` | **4:21–49** | 29 | procedure | medium | **draft** |

### Phase B — Camp purity and dedication, ch. 5–7

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 11 | `num_05_camp_pure_theft` | **5:1–10** | 10 | decision | **primary** | **draft** |
| 12 | `num_05_sotah` | **5:11–31** | 21 | decision / procedure | **primary** | **draft** |
| 13 | `num_06_nazir` | **6:1–21** | 21 | decision / procedure | **primary** | **draft** |
| 14 | `num_06_priest_blessing` | **6:22–27** | 6 | boot | medium | **draft** |
| 15 | `num_07_carts_offerings_a` | **7:1–47** | 47 | registry / narrative | thin | **draft** |
| 16 | `num_07_offerings_b_total` | **7:48–89** | 42 | registry / close | thin | **draft** |

### Phase C — Levites, second Pesach, cloud, depart, ch. 8–10

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 17 | `num_08_menorah_levites` | **8:1–26** | 26 | procedure | medium | **draft** |
| 18 | `num_09_pesach_cloud` | **9:1–23** | 23 | decision + FSM | **primary** | **draft** |
| 19 | `num_10_trumpets_depart` | **10:1–36** | 36 | boot + narrative | medium | **draft** |

### Phase D — Wilderness crises, ch. 11–14

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 20 | `num_11_complaint_quail` | **11:1–35** | 35 | narrative FSM | thin | **draft** |
| 21 | `num_12_miriam` | **12:1–16** | 16 | narrative FSM | thin | **draft** |
| 22 | `num_13_spies_sent` | **13:1–33** | 33 | narrative FSM | thin | **draft** |
| 23 | `num_14_rejection` | **14:1–45** | 45 | narrative FSM | thin | **draft** |

### Phase E — Law island + Korach, ch. 15–17

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 24 | `num_15_offerings_laws` | **15:1–31** | 31 | decision | **primary** | **draft** |
| 25 | `num_15_wood_tzitzit` | **15:32–41** | 10 | narrative + decision | **primary** | **draft** |
| 26 | `num_16_korach` | **16:1–35** | 35 | narrative FSM | medium | **draft** |
| 27 | `num_17_plague_staff` | **17:1–28** | 28 | narrative FSM | medium | **draft** |

### Phase F — Priest dues + red heifer, ch. 18–19

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 28 | `num_18_priest_levite_dues` | **18:1–32** | 32 | decision | **primary** | **draft** |
| 29 | `num_19_parah` | **19:1–22** | 22 | procedure / purity FSM | **primary** | **draft** |

### Phase G — Meribah to east conquest, ch. 20–21

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 30 | `num_20_meribah_edom_aaron` | **20:1–29** | 29 | narrative FSM | thin | **draft** |
| 31 | `num_21_snakes_conquest` | **21:1–35** | 35 | narrative FSM | thin | **draft** |

### Phase H — Bilʿam cycle, ch. 22–24

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 32 | `num_22_balak_bilam_call` | **22:1–41** | 41 | narrative FSM | thin | **draft** |
| 33 | `num_23_oracles_1_2` | **23:1–30** | 30 | narrative | thin | **draft** |
| 34 | `num_24_oracles_3_4` | **24:1–25** | 25 | narrative | thin | **draft** |

### Phase I — Peor, second census, succession, ch. 25–27

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 35 | `num_25_peor_pinchas` | **25:1–19** | 19 | narrative + decision | medium | **draft** |
| 36 | `num_26_second_census` | **26:1–65** | 65 | registry | thin | **draft** |
| 37 | `num_27_zelophehad_joshua` | **27:1–23** | 23 | decision + narrative | **primary** | **draft** |

### Phase J — Calendar restatement + vows, ch. 28–30

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 38 | `num_28_daily_shabbat_rosh` | **28:1–15** | 15 | decision / calendar | **primary** | **draft** |
| 39 | `num_28_pesach_shavuot` | **28:16–31** | 16 | decision / calendar | **primary** | **draft** |
| 40 | `num_29_fall_festivals` | **29:1–39** | 39 | decision / calendar | **primary** | **draft** |
| 41 | `num_30_vows` | **30:1–17** | 17 | decision | **primary** | **draft** |

### Phase K — Midian, Transjordan, journeys, ch. 31–33

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 42 | `num_31_midian` | **31:1–54** | 54 | narrative + decision | medium | **draft** |
| 43 | `num_32_gad_reuben` | **32:1–42** | 42 | narrative + decision | medium | **draft** |
| 44 | `num_33_journeys` | **33:1–56** | 56 | registry + command | thin | **draft** |

### Phase L — Borders, refuge, heiresses close, ch. 34–36

| # | Unit id | Refs | ~vv | Genre | Sifrei | Status |
|---|---------|------|-----|-------|--------|--------|
| 45 | `num_34_borders` | **34:1–29** | 29 | registry | thin | **draft** |
| 46 | `num_35_refuge_cities` | **35:1–34** | 34 | decision | **primary** | **draft** |
| 47 | `num_36_heiresses` | **36:1–13** | 13 | decision | **primary** | **draft** |

**Locked total: 47 blocks.**  
**Verse sum:** 1289 (full book; ch.25 = 19 vv in local OSIS).

---

## 6. Phase summary

| Phase | Blocks | Content | Code flavor | Oral emphasis |
|-------|--------|---------|-------------|---------------|
| **A** | 01–10 | Census + camp + Levite service | registries, layout boot, duty procedure | Written; Sifrei medium on firstborn/Levi |
| **B** | 11–16 | Camp pure, sotah, nazir, blessing, dedication | decision / procedure | **Sifrei primary** on 5–6 |
| **C** | 17–19 | Menorah, Levite install, Pesach II, cloud, trumpets | procedure + march FSM | Sifrei on Pesach II |
| **D** | 20–23 | Complaints, Miriam, spies, rejection | narrative FSM | Written + midrash dual-track |
| **E** | 24–27 | Land-entry offerings, wood/tzitzit, Korach, staff | decision + crisis FSM | **Sifrei** on 15; midrash on 16–17 |
| **F** | 28–29 | Priest/Levite dues; red heifer | decision + purity FSM | **Sifrei primary** |
| **G** | 30–31 | Meribah, Edom, Aaron death, snakes, Sihon/Og | narrative FSM | Written first |
| **H** | 32–34 | Bilʿam | narrative / oracles | Written + midrash dual-track |
| **I** | 35–37 | Peor, Pinchas, census II, Zelophehad, Joshua | narrative + inheritance law | Sifrei on inheritance |
| **J** | 38–41 | Tamid/moʿadim restatement; vows | calendar decision | **Sifrei primary** |
| **K** | 42–44 | Midian war, Gad/Reuben, journey list | narrative + logistics | medium |
| **L** | 45–47 | Borders, refuge cities, heiresses | registry + decision | **Sifrei primary** on 35–36 |

---

## 7. Import habit (every Num unit)

Record resolve class when free names appear:

- **EXOD_IMPORT** — Tent, priests, cloud, altar, trumpets seed.  
- **LEV_IMPORT** — purity/korban types, blood/fat rules as background.  
- **GEN_AMBIENT** — land promise, people memory.  
- **NUM_LOCAL** — census, camp order, nazir/sotah/parah/refuge, journey tests.

---

## 8. Generator and autonomy

- Generator: `artifacts/generate_numbers_units.py` (same role as Exod/Lev generators: emit draft units with full trees).  
- Owner style from Exod/Lev: autonomous “next” through schedule after approach is locked.  
- After full draft: deepen Sifrei on primary law blocks; optional IF/THEN runner later.

---

## 9. Done definition (book draft)

- [x] All 47 `num_*.yaml` present under `logic/units/`  
- [x] 1289 verse trees parsed into units  
- [x] Status column all **draft**  
- [x] This file status → **full draft complete**  
- [ ] Standing decisions §4 next → Deuteronomy (after owner go-ahead / deepen pass)

---

## Changelog

- 2026-07-24: Track opened; 47-block map locked; continuity prompt; generator; **full first draft** emitted (47 units / 1289 trees).
