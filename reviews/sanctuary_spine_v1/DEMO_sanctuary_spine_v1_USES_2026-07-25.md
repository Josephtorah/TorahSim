# Sanctuary spine V1 — Step 3: Symbol table USES (Lev · Num · Deut)

**Date:** 2026-07-25  
**Kind:** demo free-name USE matrix — experimental, **not** binding religious law  
**Status:** **Step 3 done**  
**Folder:** `reviews/sanctuary_spine_v1/`  
**Charter:** `DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md`  
**Writes:** `DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md`  
**Next:** Step 4 — cattle olah procedure (Lev 1:1–9)

**Source:** Hebrew via `taamim_tree_parse.py` v1 · English `[EN-AID]` only.

On substantive update: rename to today’s date and fix links.

---

## 0. What this step is

For each charter free name, list **USE** sites in the V1 verse slice:

| Stage | Verses |
|-------|--------|
| Operate | Lev 1:1–9 |
| Ops | Num 9:15–23 · 10:11–13 |
| Recompile | Deut 12:5–14 |

| Field | Meaning |
|-------|---------|
| **USE** | Verse + Hebrew surface + tree path (prefix of multi-leaf) |
| **WRITE** | From Step 2 (primary) |
| **Pointer** | How use hooks write |
| **Result** | PASS · PASS_alias · PASS_recompile · INSTALL_ONLY · OPEN |

**Path notation:** `L`/`R` binary walk; `C0`… flat child index (same as leaf ledger).

---

## 1. Master USE matrix

| Handle | WRITE (Step 2) | USE summary (V1 slice) | Pointer | Result |
|--------|----------------|------------------------|---------|--------|
| `SYM_mikdash` | Exod 25:8 | **No surface** in Lev 1:1–9 / Num 9–10 / Deut 12:5–14 | — | **INSTALL_ONLY** (goal; later books use other keys) |
| `SYM_tavnit` | Exod 25:9 | **No surface** in V1 use range | — | **INSTALL_ONLY** (design-time) |
| `SYM_mishkan` | Exod 25:9 · 40:34–35 | **Num 9:15–22**, **10:11** — הַמִּשְׁכָּן / *ha-mishkan* / the dwelling; משכן העדת | P-NAME / P-STATE | **PASS** |
| `SYM_ohel_moed` | Exod 27:21 · 40:34 | **Lev 1:1** מֵאֹהֶל מוֹעֵד / *me-ohel mo’ed* / from the Tent of Meeting | P-NAME + P-STATE | **PASS** |
| | | **Num 9:17** הָאֹהֶל / *ha-ohel* / the tent (same object family; not full phrase) | P-NAME (short form) | **PASS_alias** |
| `SYM_petach_ohel` | Exod 29:4 · 29:42 · 40:6 | **Lev 1:3, 1:5** פֶּתַח אֹהֶל מוֹעֵד | P-PLACE | **PASS** |
| `SYM_mizbeach` | Exod 27:1 · 40:6 | **Lev 1:5, 1:7–9** הַמִּזְבֵּחַ / הַמִּזְבֵּחָה | P-NAME | **PASS** |
| `SYM_benei_aharon` | Exod 28:1 | **Lev 1:5, 1:7–8** בְּנֵי אַהֲרֹן (+ הַכֹּהֲנִים) | P-NAME | **PASS** |
| `SYM_kohen` | Exod 28:1 | **Lev 1:5, 1:7–9** הַכֹּהֵן / הַכֹּהֲנִים | P-NAME | **PASS** |
| `SYM_anan` | Exod 40:34–35 | **Num 9:15–22 · 10:11–12** הֶעָנָן / *he-anan* / the cloud | P-STATE | **PASS** (ops job: travel control) |
| `SYM_kavod` | Exod 40:34–35 | **No surface** in V1 Num cloud block (cloud carries ops; glory was go-live) | P-STATE install | **INSTALL_ONLY** in V1 use slice* |
| `SYM_makom_yivchar` | *(not Exod)* | **Deut 12:5, 11, 14** הַמָּקוֹם אֲשֶׁר־יִבְחַר / *ha-makom asher-yivchar* | P-STATE recompile | **PASS_recompile** |

\*Num cloud block stresses **ענן** / *anan* more than **כבוד** / *kavod*; glory remains the Exod 40 go-live write. Optional later: hunt *kavod* outside V1 slice.

### Procedure locals (Lev 1:1–9 only — for Step 4)

| Handle | USE in Lev 1:1–9 | Notes |
|--------|------------------|-------|
| `SYM_olah` | 1:3, 1:4, 1:6, 1:9 | Cattle path type |
| `SYM_dam` | 1:5 (×2 surfaces) | Blood on altar |
| lean / slaughter / dash / smoke | 1:4–5, 1:9 | Acts — Step 4 detail |

---

## 2. USE cards by symbol

### 2.1 `SYM_ohel_moed` — Tent of Meeting

| USE | Surface | Path | Marks | EN-AID role |
|-----|---------|------|-------|-------------|
| **Lev 1:1** | מאהל מועד / *me-ohel mo’ed* | `RRL` | mercha → tifcha | Speech **from** Tent |
| **Num 9:17** | האהל / *ha-ohel* | (in lift-cloud clause) | — | Cloud lifts **from the tent** → then Israel journeys |

**WRITE:** Exod 27:21 name · 40:34 cloud covers full phrase אהל מועד.  
**Pointer:** P-NAME + P-STATE.  
**Result:** **PASS** (Lev full phrase); **PASS_alias** (Num short “the tent” in same cloud system).

**Tree note (Lev 1:1):** top **R** half = YHWH speaks… **from** Tent — use sits on speech side, not call-to-Moses side.

---

### 2.2 `SYM_petach_ohel` — entrance

| USE | Surface | Path | Marks |
|-----|---------|------|-------|
| **Lev 1:3** | פתח אהל מועד | `RLL` | geresh_muqdam, mahpach, pashta |
| **Lev 1:5** | פתח אהל מועד | `RRR` | tifcha, mercha, silluq |

**WRITE:** Exod 29:4 · 29:42 · 40:6.  
**Pointer:** P-PLACE.  
**Result:** **PASS**.

**Tree note:** both uses on **RIGHT** of etnachta-scale split — place/application half of the verse (with bring / blood), not the IF-cattle half (1:3 L) or slaughter half (1:5 L).

**Not in Num 9–10 / Deut 12:5–14** as this three-word phrase (V1).

---

### 2.3 `SYM_mizbeach` — altar

| USE | Surface | Path | Mark |
|-----|---------|------|------|
| Lev 1:5 | המזבח | `RRLLC4` | pashta |
| Lev 1:7 | המזבח | `LRR` | etnachta |
| Lev 1:8 | המזבח | `RRRR` | silluq |
| Lev 1:9 | המזבחה | `RLR` | zaqef_qatan (directional “onto”) |

**WRITE:** Exod 27:1 · 40:6.  
**Pointer:** P-NAME.  
**Result:** **PASS**.  
**Seed note:** Gen altars exist; V1 binds **install** altar (charter).

---

### 2.4 `SYM_benei_aharon` + `SYM_kohen`

| USE | Surface | Path | Marks |
|-----|---------|------|-------|
| Lev 1:5 | בני אהרן הכהנים | `RLLRC` | qadma, mahpach, pashta |
| Lev 1:7 | בני אהרן … הכהן | `LLLRC` + `LLLRC2` | qadma/darga; tevir on הכהן |
| Lev 1:8 | בני אהרן הכהנים | `LLR` | mahpach, pashta, zaqef |
| Lev 1:9 | הכהן | `RLLC1` | mahpach |

**WRITE:** Exod 28:1.  
**Pointer:** P-NAME.  
**Result:** **PASS**.

**Tree note (Lev 1:5):** operators on **RIGHT** with blood/altar; slaughter **LEFT** — same split as Phase A leaf work.

---

### 2.5 `SYM_mishkan` — dwelling (ops layer)

| USE | Surface | Role in verse (EN-AID) |
|-----|---------|-------------------------|
| Num 9:15 | המשכן (×3 in verse) | Day of erecting mishkan; cloud covers mishkan as tent of testimony |
| Num 9:18–20, 22 | המשכן | Cloud on mishkan ↔ camp stay |
| Num 10:11 | משכן העדת | Cloud lifts from mishkan of the testimony |

**WRITE:** Exod 25:9 pattern · 40:34–35 filled.  
**Pointer:** P-NAME / P-STATE.  
**Result:** **PASS** — Numbers runs **travel control** on the same dwelling Exod activated.

**Alias note:** Num often says **משכן** / *mishkan* or **אהל** / *ohel*, not always full **אהל מועד**. Same machine, surface variants → **PASS** / **PASS_alias**.

---

### 2.6 `SYM_anan` — cloud (ops)

| USE | Surface | Sample path | EN-AID job |
|-----|---------|-------------|------------|
| Num 9:15–16 | הענן | e.g. `LRLLR` | covers mishkan; appearance of fire at night |
| Num 9:17 | הענן (×2) | lift / settle | **when cloud lifts** → journey; where it settles → camp |
| Num 9:18–22 | הענן | various | long stay / few days / overnight rules |
| Num 10:11–12 | הענן | `RLR` | lifts; they journey from Sinai |

**WRITE:** Exod 40:34–35 (cloud on Tent at go-live).  
**Pointer:** P-STATE.  
**Result:** **PASS** with **job shift**: install signal → **march FSM input** (Step 5).

---

### 2.7 `SYM_makom_yivchar` — place He will choose (recompile)

| USE | Surface (span) | Path prefix | EN-AID |
|-----|----------------|-------------|--------|
| Deut 12:5 | המקום אשר יבחר יהוה אלהיכם… | `LL` | seek the place YHWH chooses among tribes to put His name |
| Deut 12:11 | המקום אשר יבחר יהוה אלהיכם בו | `LL` | there bring offerings |
| Deut 12:14 | במקום אשר יבחר יהוה… | `LL` | only in the place He chooses in one of your tribes |

**WRITE:** *Not* Exodus string. Charter policy: **recompile**, not string-equal to *ohel mo’ed*.  
**Pointer:** P-STATE / land-era centralization (hypothesis).  
**Result:** **PASS_recompile**.

**Interlock claim (hypothesis, labeled):**

```text
Exod: fixed ohel mo'ed + petach (portable sanctuary)
Deut: "place YHWH will choose" (land life, central key)
Role continuity: one authorized cult place / presence name
Surface continuity: NOT the same Hebrew phrase
```

---

### 2.8 Install-only in this USE slice

| Handle | Why no USE in V1 range |
|--------|------------------------|
| `SYM_mikdash` | Goal word at 25:8; Lev 1 uses Tent/altar language instead |
| `SYM_tavnit` | Blueprint for builders; not cited in Lev 1 / Num cloud / Deut 12:5–14 |
| `SYM_kavod` | Go-live at 40:34–35; Num V1 block narrates **cloud** more than glory |

These still **count as successful Step 2 writes**; Step 3 marks them **INSTALL_ONLY** honestly.

---

## 3. Stage-level picture

```text
LEV 1:1–9  USES
  me-ohel mo'ed, petach ohel mo'ed, mizbeach,
  benei Aharon / kohen, olah, dam, lifnei YHWH
        ↑ resolve
EXOD INSTALL (Step 2)

NUM 9–10  USES
  mishkan, ohel (alias), anan  →  travel control
        ↑ same machine, new job

DEUT 12:5–14  USES
  makom asher-yivchar  →  recompile place key for land
        ↑ role-level link (hypothesis), not string match
```

---

## 4. Coverage checklist (charter success item 2)

| §3.1 name | USE in V1? | Status |
|-----------|------------|--------|
| mikdash | no | INSTALL_ONLY |
| tavnit | no | INSTALL_ONLY |
| ohel mo’ed | Lev 1:1 (+ Num alias) | PASS |
| petach ohel | Lev 1:3, 1:5 | PASS |
| mizbeach | Lev 1:5–9 | PASS |
| benei Aharon | Lev 1:5–8 | PASS |
| kohen | Lev 1:5–9 | PASS |
| anan | Num 9–10 | PASS |
| kavod | no in use slice | INSTALL_ONLY* |
| mishkan | Num 9–10 | PASS |
| makom yivchar | Deut 12 | PASS_recompile |

Charter §5.2 satisfied: every name has USE **or** install-only note.

---

## 5. What Step 3 does *not* do

- Full leaf dump for all 42 verses (only free-name hits + paths)  
- Cattle olah ordered procedure (Step 4)  
- Cloud FSM states (Step 5)  
- Force *makom* = *ohel mo’ed* string identity  

---

## 6. Step status

| Step | Status |
|------|--------|
| 1 Charter | done |
| 2 Writes | done |
| **3 Uses** | **done** (this file) |
| 4 Cattle olah | pending |
| 5 Cloud FSM | pending |
| 6 Hub | pending |

---

## Changelog

- 2026-07-25: Step 3 USE matrix for V1 Lev/Num/Deut slice; all charter install names PASS or INSTALL_ONLY/recompile.
