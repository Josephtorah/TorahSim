# Sanctuary spine V1 — Hub (Step 6 of 6)

**Date:** 2026-07-25  
**Kind:** demo package hub — experimental model, **not** binding religious law  
**Status:** **V1 COMPLETE**  
**Folder:** `reviews/sanctuary_spine_v1/`

### Package index

| Step | File | Role |
|------|------|------|
| 1 | [CHARTER](DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md) | Frozen verses, names, success criteria |
| 2 | [WRITES](DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md) | Exodus install symbol table |
| 3 | [USES](DEMO_sanctuary_spine_v1_USES_2026-07-25.md) | Lev / Num / Deut resolve matrix |
| 4 | [OLAH_CATTLE](DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md) | Lev 1:1–9 cattle procedure |
| 5 | [CLOUD_FSM](DEMO_sanctuary_spine_v1_CLOUD_FSM_2026-07-25.md) | Num 9–10 stay/go machine |
| 6 | **This hub** | Diagram, full table, takeaways, dry-run checklist |

**Tutorials (this folder):**  
- Beginners: [TUTORIAL_BEGINNERS_sanctuary_spine_v1_2026-07-25.md](TUTORIAL_BEGINNERS_sanctuary_spine_v1_2026-07-25.md)  
- Full-stack: [TUTORIAL_FULLSTACK_sanctuary_spine_v1_2026-07-25.md](TUTORIAL_FULLSTACK_sanctuary_spine_v1_2026-07-25.md)  

**Method tutorials (`logic/`):**  
`../../logic/TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md` ·  
`../../logic/TUTORIAL_FIVE_BOOKS_INTERLOCK_FULLSTACK_2026-07-25.md`

On substantive update: rename to today’s date and fix links.

---

## 1. One-sentence result

Later Torah **resolves sanctuary free names** installed in Exodus: Leviticus **operates** rites at the Tent, Numbers **moves** under the cloud, Deuteronomy **recompiles** place language for land life — without rebuilding the machine each time.

---

## 2. System diagram

```text
┌──────────────────────────────────────────────────────────────────────────┐
│ EXODUS — INSTALL                                                         │
│  25:8–9  mikdash + tavnit                                                │
│  27:1    mizbeach design                                                 │
│  27:21   ohel mo'ed named                                                │
│  28:1    benei Aharon → kohen                                            │
│  29:4/42 petach ohel mo'ed + meet/speak                                  │
│  40:6    place altar before entrance                                     │
│  40:34–35 anan covers Tent; kavod fills mishkan  →  ONLINE               │
└─────────────────────────────┬────────────────────────────────────────────┘
                              │ free names exported
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────────┐
│ LEV 1:1–9       │ │ NUM 9:15–23     │ │ DEUT 12:5–14        │
│ OPERATE         │ │ + 10:11–13 OPS  │ │ RECOMPILE           │
│                 │ │                 │ │                     │
│ speech FROM     │ │ cloud on        │ │ "place YHWH will    │
│   ohel mo'ed    │ │   mishkan       │ │  choose"            │
│ bring TO petach │ │ lift → march    │ │ (role continuity;   │
│ priests + dam   │ │ dwell → camp    │ │  NOT same string    │
│ on mizbeach     │ │                 │ │  as ohel mo'ed)     │
│ cattle olah FSM │ │ travel FSM      │ │                     │
└─────────────────┘ └─────────────────┘ └─────────────────────┘
```

### Job of each stage

| Stage | Software metaphor | What it does with the machine |
|-------|-------------------|-------------------------------|
| **Exod** | `terraform apply` / service install | Creates symbols + go-live |
| **Lev 1** | Request handler using injected deps | Runs cattle olah against Tent/altar/priests |
| **Num 9–10** | Orchestrator / autoscaler signal | Cloud = stay/go input |
| **Deut 12** | Config migration for new environment | Land-era place key |

---

## 3. Full free-name resolve table

| Handle | Hebrew | Translit | English | WRITE (Exod) | USE (V1) | Result |
|--------|--------|----------|---------|--------------|----------|--------|
| `SYM_mikdash` | מִקְדָּשׁ | *mikdash* | sanctuary | 25:8 | — | INSTALL_ONLY |
| `SYM_tavnit` | תַּבְנִית | *tavnit* | pattern | 25:9 | — | INSTALL_ONLY |
| `SYM_mishkan` | מִשְׁכָּן | *mishkan* | dwelling | 25:9 · 40:34–35 | Num 9–10 | **PASS** |
| `SYM_ohel_moed` | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting | 27:21 · 40:34 | Lev 1:1 (+ Num *ha-ohel* alias) | **PASS** |
| `SYM_petach_ohel` | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of Tent | 29:4 · 29:42 · 40:6 | Lev 1:3, 1:5 | **PASS** |
| `SYM_mizbeach` | מִזְבֵּחַ | *mizbeach* | altar | 27:1 · 40:6 | Lev 1:5–9 | **PASS** |
| `SYM_benei_aharon` | בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron | 28:1 | Lev 1:5–8 | **PASS** |
| `SYM_kohen` | כֹּהֵן / כֹּהֲנִים | *kohen(im)* | priest(s) | 28:1 | Lev 1:5–9 | **PASS** |
| `SYM_anan` | עָנָן | *anan* | cloud | 40:34–35 | Num 9–10 | **PASS** (ops job) |
| `SYM_kavod` | כָּבוֹד | *kavod* | glory | 40:34–35 | — in V1 use slice | INSTALL_ONLY* |
| `SYM_makom_yivchar` | הַמָּקוֹם אֲשֶׁר־יִבְחַר | *ha-makom asher-yivchar* | place He will choose | *(not Exod)* | Deut 12:5,11,14 | **PASS_recompile** |

\*Glory is go-live; Num V1 narrates cloud more than glory.

### Pointer types used

| Pointer | Where |
|---------|--------|
| **P-NAME** | ohel, mishkan, mizbeach, benei Aharon, kohen |
| **P-PLACE** | petach ohel mo’ed |
| **P-STATE** | cloud/glory online → Lev speech / Num travel |
| **P-STATE recompile** | Deut place-He-chooses (hypothesis: same *role*, new surface) |

---

## 4. Two runtimes on one install

### 4.1 Operate — cattle olah (Step 4 summary)

```text
SPEECH from ohel_moed
  → menu (korban / bakar)
  → IF olah + male + tamim
  → BRING to petach_ohel
  → lean → slaughter (bringer)
  → blood on mizbeach (priests)
  → flay/cut → fire/wood → arrange → wash → smoke
  → close formula
```

**Tree highlight:** Lev 1:5 LEFT slaughter / RIGHT priests+blood+altar+entrance.

### 4.2 Move — cloud FSM (Step 5 summary)

```text
cloud covers mishkan → CAMP
cloud lifts from tent → MARCH
cloud dwells at place → CAMP(there)
always: al-pi YHWH
instance: 10:11 lift at Sinai → march → 10:12 settle Paran
```

**Tree highlight:** Num 9:17 LEFT lift→journey / RIGHT dwell→camp.

---

## 5. Name-resolve dry-run checklist (manual)

Use this as a **read-only checklist** (no code required). For each row: confirm WRITE verse exists, USE verse exists, result matches.

| # | Check | Pass? |
|---|--------|:-----:|
| 1 | Exod 25:8 contains מִקְדָּשׁ / *mikdash* | ☐ |
| 2 | Exod 27:21 contains אֹהֶל מוֹעֵד / *ohel mo’ed* | ☐ |
| 3 | Exod 28:1 appoints בְּנֵי אַהֲרֹן / *benei Aharon* to priest | ☐ |
| 4 | Exod 29:4 has פֶּתַח אֹהֶל מוֹעֵד / *petach ohel mo’ed* | ☐ |
| 5 | Exod 40:34 cloud covers Tent; glory fills mishkan | ☐ |
| 6 | Lev 1:1 speech **from** Tent (מאהל מועד) | ☐ |
| 7 | Lev 1:3 bring **to** entrance | ☐ |
| 8 | Lev 1:5 priests + blood **on** altar **at** entrance | ☐ |
| 9 | Num 9:17 lift → journey; dwell → camp | ☐ |
| 10 | Num 10:11–12 instance of lift/march/settle | ☐ |
| 11 | Deut 12:5 “place He will choose” present | ☐ |
| 12 | No claim that *makom yivchar* **equals** string *ohel mo’ed* | ☐ |
| 13 | Cattle path does not require flock/bird verses | ☐ |
| 14 | All Hebrew in package has translit + English | ☐ |
| 15 | Package labeled not binding religious law | ☐ |

**Optional CLI spot-checks:**

```bash
cd /path/to/Torah_Grok
python3 taamim_tree_parse.py Exod.40.34 --tree
python3 taamim_tree_parse.py Lev.1.5 --tree
python3 taamim_tree_parse.py Num.9.17 --tree
python3 taamim_tree_parse.py Deut.12.5 --tree
```

---

## 6. Charter success criteria — audit

| # | Criterion | Met? |
|---|-----------|------|
| 1 | Every §3.1 install name has WRITE | **Yes** (Step 2) |
| 2 | Every name has USE or install-only note | **Yes** (Step 3) |
| 3 | *makom yivchar* linked as recompile, not string-eq | **Yes** |
| 4 | Cattle olah ordered from Hebrew + trees | **Yes** (Step 4) |
| 5 | Cloud small FSM from Num Hebrew | **Yes** (Step 5) |
| 6 | Hub readable in one sitting | **This file** |
| 7 | he+translit+en · confidence · not binding law | **Yes** throughout |

**V1 demo: complete.**

---

## 7. Takeaways for a full-stack developer

1. **Declare once, use many times** is visible in Written Torah as **content free names**, not `import` syntax.  
2. **Environment vs app:** Exodus installs; Lev 1 runs a procedure; some words (e.g. קָרְבָּן / *korban*) are **local declares**.  
3. **Same symbol, new job:** cloud is go-live in Exod, travel controller in Num.  
4. **Trees give structure inside a verse** (agent splits, IF vs place); **reuse across books** makes a free name a “variable.”  
5. **Recompile ≠ rename equality:** Deut’s chosen place continues sanctuary *role* without repeating *ohel mo’ed*.  
6. **Glue** (את / *et*, אל / *el*, על / *al*) points at payloads; it is not the variable.  
7. **Honest layers:** seed (Gen altar) ≠ install (Exod altar) ≠ use (Lev altar).  
8. **Bulk tree_derived units** gave coverage; this demo **deepened a thin vertical slice** into checkable logic.

---

## 8. What V1 deliberately left out

| Out of scope | Possible later |
|--------------|----------------|
| Full Exod furniture | Expand write set |
| Lev 1 flock/bird | Same procedure pattern |
| Full Num trumpets / itinerary | Ops densification |
| Full Deut 12 cases | Legal densification |
| Sifra / Sifrei deep dual-track | Named Oral packets |
| Executable interpreter | Dry-run only as checklist for now |

---

## 9. Suggested next demos (after V1)

| Idea | Why |
|------|-----|
| V1.1 flock/bird on same install | Prove type branches |
| Refuge Num 35 → Deut 19 | Clean law recompile spine |
| Decalogue Exod 20 → Deut 5 | Parallel restatement |
| Tiny `registry_dry_run.py` | Load Steps 2–3 tables, print PASS |

---

## 10. File map

```text
reviews/sanctuary_spine_v1/
  README.md
  DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md
  DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md
  DEMO_sanctuary_spine_v1_USES_2026-07-25.md
  DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md
  DEMO_sanctuary_spine_v1_CLOUD_FSM_2026-07-25.md
  DEMO_sanctuary_spine_v1_HUB_2026-07-25.md    ← you are here
```

---

## Changelog

- 2026-07-25: Step 6 hub complete — V1 sanctuary spine demo closed; success criteria audited.
