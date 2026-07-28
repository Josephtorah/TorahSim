# Leviticus Build — sanctuary apps after Exodus install

**Date:** 2026-07-21  
**Kind:** build approach (Pre-Code) — **not** binding law  
**Status:** **full draft + tree_derived_v1** (2026-07-24) — 50 units; see `LEVITICUS_TREE_DERIVE_2026-07-24.md` · `artifacts/reprocess_book_from_trees.py --book lev`. Original generator: `artifacts/generate_leviticus_units.py`

**Related:**  
- Exodus full draft: `EXODUS_BUILD_2026-07-21.md` · units `logic/units/exo_*.yaml` (stage install)  
- Sanctuary free-name resolve: `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md`  
- Architecture stack: `ARCHITECTURE_discussion_2026-07-19.md` · narrative book `BOOK_torah_grok_journey_so_far_2026-07-21.md`  
- Oral policy: `RESEARCH_valid_oral_torah_2026-07-19.md` (**Sifra** for Lev law decode)  
- Units: `logic/units/lev_*.yaml` (50 schedule files + hand 01–02)
- Generator: `artifacts/generate_leviticus_units.py`  
- Data: `Data/Lev.xml` · `Data/sifra_he.json` (and any `_en` sibling if present)

On substantive update: rename to today’s date and fix links.

---

## 1. Purpose

Wire **Leviticus** so the system run continues after Exodus sanctuary install:

```text
Genesis boot/sagas → Exodus (nation + law + mishkan install) → Leviticus (apps + local registries)
```

Leviticus is mostly **application code** and **local type/procedure registries** on a stage Exodus already built (Tent, priests, altar, vessels, cloud/glory). It does **not** re-boot the mishkan from zero. Free names should resolve **tight to Exodus** where Pass 4 says so; offering types, purity grades, and rite sequences are often **Lev-local**.

**Mode (locked):** one **manageable thorough block** at a time (~50 total). Same spirit as Exodus thorough schedule — not one giant book dump, not one unit per verse.

**Owner lock (2026-07-21):** **50 blocks** for all of Leviticus (27 chapters / **859** verses). Average ≈ **17 verses/block**. Prefer **~10–20** verses on dense case law; allow slightly larger only on ritual narrative or long covenant speech.

---

## 2. Thorough-pass checklist (every block)

Do **all** of these before marking a block draft-complete:

1. **Written Hebrew** — derive from `Data/Lev.xml`; English only as gloss `[EN-AID]`.  
2. **Trees** — `taamim_tree_parse.py` v1 for **every verse** in the block → `binary_trees` + `tree_ascii`.  
3. **Logic shape** — `decision_table` and/or procedure `boot_steps` / purity **state machine** as genre fits; always he+translit+en on atoms.  
4. **Exodus imports** — name free names that resolve to Exod install (ohel mo'ed, mizbeach system, Aharon/sons office, etc.) in `depends_on` / `imports` / derivation_log; do not re-specify the Tent.  
5. **Oral dual-track** — **Sifra first** on law (when corpus has material); then MH + Bavli / Mishnah as possible Oral; never silent-merge.  
6. **Coverage** — `tree_coverage` for all leaves (roles may start heuristic; TIR when deepening).  
7. **Scenarios** — small expect-after-step checks.  
8. **Confidence** — hypothesis / tested — **not binding religious law**.

---

## 3. Oral open order (Leviticus)

| Block type | Prefer first Oral (among possibles) |
|------------|-------------------------------------|
| Offering procedure / case law | **Sifra** → MH + cite_index Bavli → optional Mishnah/Tosefta |
| Purity catalogs / state | **Sifra** first; **Negaim** / related Oral named on 13–14 when thickening |
| Ritual narrative (8–10, 24:10–23) | Written first; midrash/Bavli dual-track when named |
| Holiness / calendar / land | Sifra where sequential; Bavli/midrash dual-track as needed |

MH endpoints remain **possible Oral** (standing §5).  
Local primary dump: `Data/sifra_he.json`. Do **not** invent Sifra text for empty shelves.

---

## 4. Verse numbering note

Block refs follow **local `Data/Lev.xml` / OSIS** (Hebrew-style Lev 6 begins with *tzav* / torat ha-olah material; chapter 6 has **23** verses; chapter 5 ends at **5:26**). When comparing English Bibles, chapter 5–6 boundaries may differ — **trust the XML osisID**.

---

## 5. Locked block map (50)

**Sifra** column: how hard to lean on Sifra for that block.  
**Status:** pending | draft | v0 | done draft.

### Phase A — Offerings (korbanot), ch. 1–7 (~16 blocks)

Local type registries + procedure pipelines. Highest “visible code” density (IF/THEN + pipelines).

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 01 | `lev_01_call_and_korban_opening` | **1:1–3** | 3 | decision / open | primary | **draft done** |
| 02 | `lev_01_olah_cattle_procedure` | **1:4–9** | 6 | procedure | primary | **draft done** |
| 03 | `lev_01_olah_flock` | **1:10–13** | 4 | procedure | primary | **draft** |
| 04 | `lev_01_olah_bird` | **1:14–17** | 4 | procedure | primary | **draft** |
| 05 | `lev_02_minchah` | **2:1–16** | 16 | decision / types | primary | **draft** |
| 06 | `lev_03_shelamim` | **3:1–17** | 17 | decision / fat-blood | primary | **draft** |
| 07 | `lev_04_chatat_priest` | **4:1–12** | 12 | decision | primary | **draft** |
| 08 | `lev_04_chatat_congregation` | **4:13–21** | 9 | decision | primary | **draft** |
| 09 | `lev_04_chatat_leader` | **4:22–26** | 5 | decision | primary | **draft** |
| 10 | `lev_04_chatat_common` | **4:27–35** | 9 | decision | primary | **draft** |
| 11 | `lev_05_asham_graded` | **5:1–13** | 13 | decision | primary | **draft** |
| 12 | `lev_05_asham_sancta` | **5:14–26** | 13 | decision | primary | **draft** |
| 13 | `lev_06_olah_minchah_torah` | **6:1–23** | 23 | procedure / priest torot | primary | **draft** — *split 6:1–11 / 6:12–23 if pass thin* |
| 14 | `lev_07_asham_procedure` | **7:1–10** | 10 | procedure | primary | **draft** |
| 15 | `lev_07_shelamim_types` | **7:11–21** | 11 | decision | primary | **draft** |
| 16 | `lev_07_fat_blood_dues` | **7:22–38** | 17 | decision / summary | primary | **draft** |

### Phase B — Priest inauguration and crisis, ch. 8–10 (~3 blocks)

Ritual FSM; **tight Exodus imports** (millu’im, garments, altar, Tent).

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 17 | `lev_08_milluim` | **8:1–36** | 36 | ritual FSM | medium | **draft** — *split 8:1–17 / 8:18–36 if heavy* |
| 18 | `lev_09_eighth_day` | **9:1–24** | 24 | ritual FSM | medium | **draft** |
| 19 | `lev_10_nadav_avihu` | **10:1–20** | 20 | narrative + rules | medium | **draft** |

### Phase C — Purity spine, ch. 11–15 (~11 blocks)

Type catalogs + pure/impure state machines. Standing curriculum priority. **Lev 12 = rewrite v1** (v0 file remains reference until replaced).

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 20 | `lev_11_animals_water_birds` | **11:1–23** | 23 | type catalog | primary | **draft** |
| 21 | `lev_11_carcass_swarm_close` | **11:24–47** | 24 | types + holiness | primary | **draft** |
| 22 | `lev_12_childbirth` | **12:1–8** | 8 | decision / state | primary | **draft (v1 rewrite)** |
| 23 | `lev_13_skin_initial` | **13:1–17** | 17 | decision / diagnostic | primary | **draft** |
| 24 | `lev_13_boil_burn` | **13:18–28** | 11 | decision | primary | **draft** |
| 25 | `lev_13_head_isolation` | **13:29–46** | 18 | decision | primary | **draft** |
| 26 | `lev_13_garment` | **13:47–59** | 13 | decision | primary | **draft** |
| 27 | `lev_14_metzora_cleanse` | **14:1–32** | 32 | procedure + poverty branch | primary | **draft** — *split 14:1–20 / 14:21–32 if heavy* |
| 28 | `lev_14_house_nega` | **14:33–57** | 25 | decision | primary | **draft** |
| 29 | `lev_15_male_discharge` | **15:1–18** | 18 | state / purity | primary | **draft** |
| 30 | `lev_15_female_discharge` | **15:19–33** | 15 | state / purity | primary | **draft** |

### Phase D — Day of Atonement and blood center, ch. 16–17 (~3 blocks)

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 31 | `lev_16_yk_entry_blood` | **16:1–19** | 19 | ritual procedure | primary | **draft** |
| 32 | `lev_16_yk_goat_statute` | **16:20–34** | 15 | ritual + statute | primary | **draft** |
| 33 | `lev_17_blood_center` | **17:1–16** | 16 | decision / blood | primary | **draft** |

### Phase E — Holiness code core, ch. 18–20 (~4 blocks)

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 34 | `lev_18_sexual_land` | **18:1–30** | 30 | decision / ban list | primary | **draft** |
| 35 | `lev_19_holiness_neighbor` | **19:1–18** | 18 | decision / ethics | primary | **draft** |
| 36 | `lev_19_mixtures_weights` | **19:19–37** | 19 | decision | primary | **draft** |
| 37 | `lev_20_sanctions` | **20:1–27** | 27 | decision / penalties | primary | **draft** |

### Phase F — Priestly holiness and sancta, ch. 21–22 (~4 blocks)

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 38 | `lev_21_priest_family` | **21:1–15** | 15 | decision | primary | **draft** |
| 39 | `lev_21_priest_blemish` | **21:16–24** | 9 | decision | primary | **draft** |
| 40 | `lev_22_holy_food` | **22:1–16** | 16 | decision | primary | **draft** |
| 41 | `lev_22_acceptable_offerings` | **22:17–33** | 17 | decision | primary | **draft** |

### Phase G — Calendar, lamp, bread, blasphemer, ch. 23–24 (~4 blocks)

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 42 | `lev_23_spring_festivals` | **23:1–22** | 22 | calendar registry | primary | **draft** |
| 43 | `lev_23_fall_festivals` | **23:23–44** | 22 | calendar registry | primary | **draft** |
| 44 | `lev_24_lamp_bread` | **24:1–9** | 9 | procedure (Exod import) | medium | **draft** |
| 45 | `lev_24_blasphemer_talion` | **24:10–23** | 14 | narrative + law | medium | **draft** |

### Phase H — Land, covenant, vows, ch. 25–27 (~5 blocks)

| # | Unit id (planned) | Refs | ~vv | Genre | Sifra | Status |
|---|-------------------|------|-----|-------|-------|--------|
| 46 | `lev_25_shemittah` | **25:1–22** | 22 | land / calendar | primary | **draft** |
| 47 | `lev_25_redeem_poor` | **25:23–38** | 16 | decision | primary | **draft** |
| 48 | `lev_25_slave_jubilee` | **25:39–55** | 17 | decision | primary | **draft** |
| 49 | `lev_26_bless_curse` | **26:1–46** | 46 | covenant FSM | medium | **draft** — *longest block; split 26:1–13 / 26:14–46 if needed (still counts as deepening same #)* |
| 50 | `lev_27_vows_valuations` | **27:1–34** | 34 | decision / registry | primary | **draft** |

**Locked total: 50 blocks.**  
**Prior units that count:** #01, #02 draft; #22 has v0 file to upgrade.  
**First-pass draft:** complete (48 generated + 2 hand-kept 01–02; Lev 12 rewritten v1-style).

---

## 6. Phase summary

| Phase | Blocks | Content | Code flavor | Oral emphasis |
|-------|--------|---------|-------------|---------------|
| **A** | 01–16 | Korbanot 1–7 | Procedure + decision tables; type enums | **Sifra** |
| **B** | 17–19 | Inauguration 8–10 | Ritual FSM; Exod free names | Sifra medium + midrash |
| **C** | 20–30 | Purity 11–15 | Catalogs + purity state machines | **Sifra**; Negaim on 13–14 |
| **D** | 31–33 | YK + blood 16–17 | High ritual procedure | **Sifra** |
| **E** | 34–37 | Holiness 18–20 | Ban lists + sanctions | **Sifra** |
| **F** | 38–41 | Priest/sancta 21–22 | Eligibility + blemish rules | **Sifra** |
| **G** | 42–45 | Calendar + lamp/bread 23–24 | Mo’adim registry; Exod imports | Sifra + midrash |
| **H** | 46–50 | Land + covenant + vows 25–27 | Jubilee economics; bless/curse FSM | Sifra / midrash |

---

## 7. Exodus free-name habit (every Lev unit)

When a block uses sanctuary stage terms, record resolve class in the unit (comment or `imports:`):

- **EXOD_IMPORT** — system installed in Exodus (e.g. ohel mo'ed, priest office, Tabernacle altar system, ner tamid seed, incense system). Prefer pointing at relevant `exo_*` unit ids.  
- **LEV_LOCAL** — type, purity grade, or rite mechanic authored primarily in Leviticus.  
- **GEN_AMBIENT** — rare; people graph / world fabric only.  
- **MULTI** — common noun; do not force a single book.

Do not treat “first string hit in Genesis” as Tabernacle install (Pass 4 lesson).

---

## 8. How to run a session

1. Default: **“next Leviticus block”** → only the next pending row in §5.  
2. **Next after full draft:** deepen high-value Sifra blocks (olah/chatat/nega/YK) or wire Lev `import:` free names from `exo_*`; optional tiny IF/THEN runner demo.  
3. Optional: owner names a ref → that block only (still full checklist).  
4. Prefer book order so learning compounds before purity spine; owner may override (e.g. jump to Lev 12 v1).  
5. On law blocks: budget time for **Sifra open + dual-track notes** before calling the pass thorough.  
6. After each block: update Status in this table + `STANDING_DECISIONS` next pointer.  
7. Field splits: if a locked block is too heavy, split mid-range **without changing the locked total philosophy** — add sub-ids (e.g. `lev_14_metzora_cleanse_a/b`) and note here; do not silently drop verses.

---

## 9. On disk after autonomous pass (2026-07-21)

All 50 schedule unit ids present under `logic/units/lev_*.yaml`.
Hand-kept: blocks 01–02. Regenerated/rewritten: 03–50 including Lev 12 v1-style draft.

---

## 10. Honest draft limits (when the pass runs)

Same class as Genesis/Exodus whole-book drafts unless a block is hand-deepened:

- Trees complete per block; TIR roles may stay heuristic at first.  
- Decision tables are hypothesis IF/THEN until Sifra/MH stress-tested.  
- Sifra samples dual-track, not full commentary.  
- Not frozen; not binding religious law.

---

## 11. One-sentence summary

**Leviticus Build = 50 Pre-Code draft units covering all 859 verses as sanctuary apps and local registries on the Exodus stage, with Sifra dual-track samples on law, Written Hebrew first — full first-pass draft complete.**
