# Sanctuary spine V1 demo — Charter (Step 1 of 6)

**Date:** 2026-07-25  
**Kind:** demo charter — experimental model, **not** binding religious law  
**Status:** **frozen for V1** · **all 6 steps done** (hub complete 2026-07-25)  
**Plan:** 6 steps (charter → symbol writes → use matrix → cattle olah → cloud FSM → interlock package)

**Folder:** `reviews/sanctuary_spine_v1/` (all V1 demo steps live here)

**Related:**  
- Plan context: chat + `../../logic/TUTORIAL_FIVE_BOOKS_INTERLOCK_FULLSTACK_2026-07-25.md`  
- Declare/use method: `../../logic/TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md`  
- Lev 1 prior work: `../LEDGER_lev_01_phaseA_LEAF_2026-07-24.md` · `../PHASE_B_lev_01_write_sites_2026-07-24.md` · `../DISAMBIG_lev_01_onkelos_oshb_2026-07-24.md`  
- Units already present: `../../logic/units/exo_*`, `lev_01_*`, `num_09_*`, `num_10_*`, `deu_12_*`

On substantive update: rename to today’s date and fix links.

---

## 0. One-sentence goal

Prove, with Hebrew + trees + a small free-name table, that Torah can be read as:

```text
Exodus INSTALLS sanctuary  →  Leviticus 1 OPERATES on it
                           →  Numbers MOVES by cloud on it
                           →  Deuteronomy RECOMPILES place for land life
```

without rebuilding the machine in each later book.

---

## 1. Chain (locked)

```text
Exod Tent install  →  Lev 1 operate  →  Num cloud march  →  Deut central place
```

| Stage | Book role | V1 job |
|-------|-----------|--------|
| **Install** | Exodus | Write free names + go-live |
| **Operate** | Leviticus 1 | Speech from Tent + cattle olah path only |
| **Ops** | Numbers | Cloud stay / go / march |
| **Recompile** | Deuteronomy 12 | “Place YHWH will choose” (core only) |

---

## 2. Exact verse list (locked)

### 2.1 Install — Exodus

| Ref | Why in V1 |
|-----|-----------|
| **Exod 25:8–9** | Sanctuary goal + pattern (מִקְדָּשׁ / *mikdash*; תַּבְנִית / *tavnit*) |
| **Exod 27:1** | Altar design start (מִזְבֵּחַ / *mizbeach*) |
| **Exod 27:21** | First clear אֹהֶל מוֹעֵד / *ohel mo’ed* / Tent of Meeting |
| **Exod 28:1** | Sons of Aaron appointed to priest (בְּנֵי אַהֲרֹן / *benei Aharon*) |
| **Exod 29:4** | Entrance of Tent as bring-to place (פֶּתַח אֹהֶל מוֹעֵד / *petach ohel mo’ed*) |
| **Exod 29:42** | Continual olah at entrance; meet/speak function |
| **Exod 40:6** | Place olah altar before entrance (layout go-live) |
| **Exod 40:34–35** | Cloud covers Tent; glory fills mishkan (presence online) |

**Count:** 8 loci (10 verses if counting 25:8, 25:9, 40:34, 40:35 separately → **11 verses**).

### 2.2 Operate — Leviticus

| Ref | Why in V1 |
|-----|-----------|
| **Lev 1:1–9** | Call from Tent + cattle burnt-offering path only |

**Count:** 9 verses.  
**Explicitly deferred:** Lev 1:10–13 (flock), 1:14–17 (bird).

### 2.3 Ops — Numbers

| Ref | Why in V1 |
|-----|-----------|
| **Num 9:15–23** | Cloud on mishkan → stay / journey rules |
| **Num 10:11–13** | Cloud lifts; they march (short trigger) |

**Count:** 9 + 3 = **12 verses**.

### 2.4 Recompile — Deuteronomy

| Ref | Why in V1 |
|-----|-----------|
| **Deut 12:5–14** | Seek the place YHWH chooses; bring offerings there; not every local high place |

**Count:** 10 verses.  
**Explicitly deferred:** rest of Deut 12 (meat, blood detail expansions beyond place key).

### 2.5 Totals

| Stage | Verses (approx.) |
|-------|----------------:|
| Exodus install | 11 |
| Leviticus operate | 9 |
| Numbers ops | 12 |
| Deuteronomy recompile | 10 |
| **V1 total** | **~42 verses** |

---

## 3. Free-name list (locked minimal set)

Every name is stored as **he + he_translit + en**. Optional handle `SYM_*` is for docs only.

### 3.1 Install / environment (must resolve)

| Handle | Hebrew | Translit | English |
|--------|--------|----------|---------|
| `SYM_mikdash` | מִקְדָּשׁ | *mikdash* | sanctuary |
| `SYM_tavnit` | תַּבְנִית | *tavnit* | pattern / blueprint |
| `SYM_ohel_moed` | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting |
| `SYM_petach_ohel` | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of the Tent of Meeting |
| `SYM_mizbeach` | מִזְבֵּחַ | *mizbeach* | altar |
| `SYM_benei_aharon` | בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron |
| `SYM_kohen` | כֹּהֵן / כֹּהֲנִים | *kohen* / *kohanim* | priest(s) |
| `SYM_anan` | עָנָן | *anan* | cloud |
| `SYM_kavod` | כָּבוֹד | *kavod* | glory (of YHWH) |
| `SYM_mishkan` | מִשְׁכָּן | *mishkan* | dwelling / Tabernacle |

### 3.2 Recompile key (Deut)

| Handle | Hebrew | Translit | English |
|--------|--------|----------|---------|
| `SYM_makom_yivchar` | הַמָּקוֹם אֲשֶׁר־יִבְחַר | *ha-makom asher-yivchar* | the place that He will choose |

**Note (locked policy):** Do **not** force string equality `ohel mo’ed` = `makom yivchar`. Link as **recompile / P-STATE hypothesis** (same sanctuary *role* in land life), confidence labeled.

### 3.3 Procedure locals (Lev 1 cattle path only)

Tracked only as needed for Step 4 procedure — not full cross-book matrix unless they already appear:

| Handle | Hebrew | Translit | English |
|--------|--------|----------|---------|
| `SYM_olah` | עֹלָה | *olah* | burnt offering |
| `SYM_dam` | דָּם | *dam* | blood |
| `SYM_samakh` | סָמַךְ | *samakh* | lean (hand) |
| `SYM_shachat` | שָׁחַט | *shachat* | slaughter |
| `SYM_zarak` | זָרַק | *zarak* | dash / throw (blood) |
| `SYM_hiktir` | הִקְטִיר | *hiktir* | turn to smoke |

### 3.4 Out of free-name set for V1

- Full vessel inventory (ark, table, menorah detail)  
- Incense altar as separate resolve target  
- Flock/bird olah types  
- All purity grades  
- Full festival calendar  

---

## 4. Six-step plan (locked)

| Step | Deliverable file (in this folder) | Done when |
|------|-----------------------------------|-----------|
| **1** | This charter | Verses + names + success + out-of-scope frozen |
| **2** | `DEMO_sanctuary_spine_v1_WRITES_YYYY-MM-DD.md` | Each §3.1 name has WRITE locus from V1 Exod list (he+translit+en, pointer type) |
| **3** | `DEMO_sanctuary_spine_v1_USES_YYYY-MM-DD.md` | Each name has USE rows at Lev/Num/Deut with path or verse + PASS/LOCAL/OPEN |
| **4** | `DEMO_sanctuary_spine_v1_OLAH_CATTLE_YYYY-MM-DD.md` | Ordered cattle olah steps Lev 1:1–9 from trees (not EN-AID-only) |
| **5** | `DEMO_sanctuary_spine_v1_CLOUD_FSM_YYYY-MM-DD.md` | Stay/go/march states from Num 9:15–23 + 10:11–13 |
| **6** | `DEMO_sanctuary_spine_v1_HUB_YYYY-MM-DD.md` | One diagram + full resolve table + fullstack takeaways; optional name dry-run checklist |

**Cadence:** one step at a time; review before next.  
**No re-bulk** of whole books; deepen this slice only.

---

## 5. Success criteria (V1 done)

V1 is complete only if **all** of the following hold:

1. **Every §3.1 free name** has a WRITE in the Exod verse list (or explicit OPEN with reason).  
2. **Every §3.1 free name** has at least one USE in Lev 1:1–9, Num 9–10, or is install-only with note (e.g. *tavnit* mainly design-time).  
3. **`SYM_makom_yivchar`** is linked as recompile (hypothesis), not fake identity with *ohel mo’ed*.  
4. **Cattle olah** is an ordered procedure grounded in Hebrew + ta'amim structure for Lev 1:1–9.  
5. **Cloud** is a small FSM (stay / when cloud lifts / march) from Num Hebrew.  
6. **Hub doc** is readable in one sitting by a full-stack developer.  
7. All Hebrew appears with **transliteration + English**; confidence labels present; **not binding law**.

---

## 6. Out of scope (explicit)

| Out | Why |
|-----|-----|
| Full Exod 25–31 furniture prose | Demo needs keys, not every board |
| Lev 1 flock/bird paths | Same pattern; cattle is enough |
| Full Num 9 Pesach II narrative | Only cloud block 9:15–23 |
| Full Deut 12 social/meat cases | Place key 12:5–14 only |
| Full TIR 100% word roles | Aspiration, not V1 gate |
| Binding halakhah product | Project rule |
| Executable VM / interpreter | Optional later after freeze |
| Silent Oral merge | Dual-track only if named |
| Re-running all five-book reprocess | Units already exist |

---

## 7. Method constraints (carry into all steps)

1. **Hebrew first** — English is `[EN-AID]` only.  
2. **Trees** — use `taamim_tree_parse.py` v1; prefer leaf paths for free names where useful.  
3. **Never bare Hebrew** — always he + translit + en.  
4. **Seed vs install** — e.g. Gen altar seed ≠ Exod Tent altar install (label if mentioned).  
5. **Provenance** — Written write/use; Oral only dual-track named.  
6. **Confidence** — tested / hypothesis / open.  

---

## 8. Existing assets to reuse (do not rebuild)

| Asset | Use in V1 |
|-------|-----------|
| `logic/units/exo_25_*` … `exo_40_erect_fill.yaml` | Tree background for install verses |
| `logic/units/lev_01_*.yaml` | Lev 1 trees |
| `logic/units/num_09_pesach_cloud.yaml`, `num_10_trumpets_depart.yaml` | Cloud / depart |
| `logic/units/deu_12_place_name.yaml` | Deut 12 |
| Lev 1 Phase A/B + Onkelos disambig | Jump-start Steps 2–4 |

---

## 9. Step status board

| Step | Status |
|------|--------|
| 1 Charter | **done** (this file) |
| 2 Writes | **done** — `DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md` |
| 3 Uses | **done** — `DEMO_sanctuary_spine_v1_USES_2026-07-25.md` |
| 4 Cattle olah | **done** — `DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md` |
| 5 Cloud FSM | **done** — `DEMO_sanctuary_spine_v1_CLOUD_FSM_2026-07-25.md` |
| 6 Hub | **done** — `DEMO_sanctuary_spine_v1_HUB_2026-07-25.md` · **V1 COMPLETE** |

---

## Changelog

- 2026-07-25: Step 1 charter frozen — verse list, free names, 6-step plan, success criteria, out-of-scope.
