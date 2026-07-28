# Genesis Build — how Genesis enters the runnable system

**Date:** 2026-07-20  
**Kind:** build approach (Pre-Code → later interpreter)  
**Status:** full draft + **tree_derived_v1** (2026-07-24) — see `GENESIS_TREE_DERIVE_2026-07-24.md`; not binding law  
**Name:** **Genesis Build** (file: `GENESIS_BUILD_YYYY-MM-DD.md`)

**Related:**  
- **Beginner tutorial (this track, day 1):** `logic/gen_boot/TUTORIAL_GENESIS_BUILD_2026-07-19.md` · hub `logic/gen_boot/INDEX.md`  
- **Long tutorial (derive pipeline + day 4 show-all-work):** `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md`  
- **Draft units:** `logic/units/gen_01_creation_boot.yaml`, `gen_01_day2_raqia.yaml`, `gen_01_day3_land_plants.yaml`, `gen_01_day4_lights.yaml`, `gen_01_day5_sea_birds.yaml`  
- **Genesis full-stack package map:** `architecture/ARCHITECTURE_genesis_stack_2026-07-21.md` (segments + SY comparison)  
- **Progress observations (Gen done → Exod next):** `NOTES_progress_observations_2026-07-20.md`  
- Architecture: `architecture/ARCHITECTURE_discussion_2026-07-19.md`, passes 1–5  
- Oral policy: `RESEARCH_valid_oral_torah_2026-07-19.md` (§6 MH = possible Oral)  
- Lev contrast: `logic/units/lev_01_*.yaml`  

On substantive update: rename to today’s date and fix links.

---

## 1. Purpose of this note

Record how we **use Genesis** in Torah_Grok so that, when the whole system is wired, we can **run** it: Gen boot → (later) Exodus install → Lev apps — without forcing Genesis into a Leviticus-shaped template.

---

## 2. What Genesis stands for in the model

Genesis is the **boot / seed layer**, not the sacrifice application layer.

| Role | Meaning |
|------|---------|
| **Boot sequence** | Ordered creation events that initialize world state |
| **Symbol export** | Names and patterns later modules may import (e.g. day = evening then morning) |
| **People / covenant seed** | Later (beyond 1:1–5): lineage, land promise, Egypt end-state for Exodus |
| **Genre** | Narrative bootstrap (`G7`-like), speech-create (`ויאמר…ויהי`), not casuistic korban IF |

**Not Genesis’s primary job:** animal validators, Tent/priests, purity FSMs, offering pipelines.

---

## 3. Does Lev need Genesis boot?

| Level | Needs Gen 1:1–5? |
|--------|------------------|
| **Full system run** (“start from the beginning → later sanctuary”) | **Yes** — something must create world, light/dark, day cycle, then eventually people, then Exodus install, then Lev |
| **Single Lev rule in isolation** | **Not as a step inside each offering pipeline** — by then the world already “exists.” Lev assumes days, creatures, speech, Israel; it does not re-run creation |

**Analogy:**

```text
Genesis     →  BIOS / OS boot (once)
Exodus      →  install sanctuary machine
Leviticus   →  run offering / purity apps
```

You do **not** reboot the universe for every olah. You **do** boot once if the assembled system is to run from scratch.

Lev’s **tight** runtime imports are more often **Exodus** (Tent, priests, altar). Genesis is **deeper ambient prerequisite** for a full timeline.

---

## 4. Same project machinery as Lev; different logic shape

### Shared (like Lev units)

- Hebrew + `he_translit` + `en` on every atom  
- Confidence + source  
- Dual-track Oral (named only; never silent merge)  
- Scenarios that test the logic document  
- Later code **interprets** frozen YAML only — does not invent rules  

### Different template

| Lev-style | Genesis Build style (e.g. 1:1–5) |
|-----------|----------------------------------|
| WHEN person offers… THEN… | **INIT / ordered STEPS** |
| Type registry (cattle/flock) | **World STATE fields** |
| Procedure (lean → slaughter…) | **Boot steps** (create → speech → separate → name → day) |
| Import Tent/priests | **EXPORT** symbols for later `import:` |
| Decision table first | **Boot log + exports** first |

---

## 5. How to represent Gen 1:1–5 as logic (later codeable)

Conceptual unit sketch — **Genesis Build** first product:

```text
UNIT id: gen_01_creation_boot
scope: Gen 1:1–5
genre: narrative_boot

STEPS (ordered, grounded in Written Hebrew):
  1. CREATE heavens + earth                    # 1:1
  2. DESCRIBE earth: tohu/vohu, dark, deep;
     spirit of God over the waters             # 1:2
  3. SPEECH_ACT "let there be light" → light   # 1:3
  4. EVALUATE light as good;
     SEPARATE light | dark                     # 1:4
  5. NAME light→day, dark→night;
     TICK clock → day_1 (evening + morning)    # 1:5

STATE after unit (examples):
  heavens_exist, earth_exist
  light_exists
  light_separated_from_dark
  names: day, night
  day_cycle = evening_then_morning
  day_index includes day_1

EXPORTS (for later modules):
  day_cycle
  light_dark_pair
  create_by_speech
  (extend as more of Gen 1 is built)

ORAL (optional, dual-track, named):
  possible Oral: Bereishit Rabbah on these verses;
    Bavli paren cites (cite_index);
    MH among midrash peers — not MH edges from Tanakh verse nodes
  do not merge midrash cosmologies into Written face silently

SCENARIOS (examples):
  - After 1:3–4: light exists and is separated from dark?
  - After 1:5: day_1 defined as evening then morning?
```

**Interpreter composition (future):**

```text
run(gen_01_creation_boot)      # sets world state once
...
run(exod_sanctuary_install)    # Tent, priests (thin install)
run(lev_01_olah_...)           # assumes world exists; needs sanctuary state
```

That is **runnable composition** of the same kind as chaining Lev units, with Gen as **init**.

---

## 6. Graphs around Gen 1 (so we don’t misuse MH)

From the Gen 1:1–5 glance:

| Graph | What we saw | Use in Genesis Build |
|-------|-------------|----------------------|
| **MH on “Genesis 1:x” Tanakh** | **0** edges | Do not expect MH as first click on the verse |
| **Written → midrash** | Strong to **Bereishit Rabbah 1:*** | Primary Oral *packet* genre for this span |
| **MH on BR 1:x** | Midrash peers; sparse Talmud/Mishnah | **Possible Oral** peers once on midrash |
| **cite_index** Bavli → Gen 1:x | Sparse but real (e.g. Chagigah inventory; Chullin day template) | Named Oral *uses* / pattern exports |

**Possible Oral policy still holds:** MH members are never ruled out; for Gen openers **prefer** aggadic midrash job-fit (BR), not Sifra.

---

## 7. What not to do

- Force Gen into **korban decision tables** only to “look like Lev.”  
- Re-execute Gen 1:1–5 inside every Lev scenario (wrong and expensive).  
- Claim Gen 1:5 *is* later law (e.g. *oto ve-et beno* day) on the Written face — that is **export + later join**, dual-track if Oral.  
- Treat empty MH on Gen 1:1 as “no Oral.”  

---

## 8. Build order (Genesis Build track)

1. **This approach note** (done).  
2. Day units (draft):
   - `logic/units/gen_01_creation_boot.yaml` — **1:1–5** day one (52 words covered; letter-bet; Chagigah access)
   - `logic/units/gen_01_day2_raqia.yaml` — **1:6–8** day two firmament / waters split (38 words)
   - `logic/units/gen_01_day3_land_plants.yaml` — **1:9–13** day three land/seas + plants by kind (69 words)
   - `logic/units/gen_01_day4_lights.yaml` — **1:14–19** day four luminaries / calendar / dominion (69 words; full `binary_trees` + `tree_ascii`)
   - `logic/units/gen_01_day5_sea_birds.yaml` — **1:20–23** day five sea life + birds + blessing (57 words)
   - `logic/units/gen_01_day6_land_human.yaml` — **1:24–31** day six land animals + human (149 words; 2026-07-20)
   - `logic/units/gen_01_day7_shabbat.yaml` — **2:1–3** day seven complete/cease/sanctify (35 words; 2026-07-20)
3. **Package 0 kernel boot (1:1–2:3) complete as draft units.**  
   - `logic/units/gen_02_03_garden.yaml` — **2:4–3:24** garden package (formation → breach → exile; 640 words, 26 steps, FSM)  
   - `logic/units/gen_04_05_early_humanity.yaml` — **4:1–5:32** Cain/Abel, culture, Adam→Noah (706 words, 16 steps)  
   - `logic/units/gen_06_09_flood_covenant.yaml` — **6:1–9:29** flood + ark + Noach covenant (1299 words, 21 steps)  
   - `logic/units/gen_10_11_nations_babel.yaml` — **10:1–11:32** nations + Babel + Abram stage (679 words, 10 steps)  
   - Abraham package **12–25** (split, 2026-07-20; 5374 words total):
     - `gen_12_14_call_and_lot` (12–14)
     - `gen_15_17_covenant_brit` (15–17)
     - `gen_18_19_sodom` (18–19)
     - `gen_20_22_isaac_binding` (20–22)
     - `gen_23_25_abraham_close` (23–25; handoff to Jacob/Esau)
   - Isaac/Jacob **26–36** (split, 2026-07-20; 5239 words):
     - `gen_26_isaac` · `gen_27_28_blessing_bethel` · `gen_29_30_laban_children`
     - `gen_31_33_return_esau` · `gen_34_36_shechem_edom`
   - Joseph **37–50** Egypt handoff (split, 2026-07-20; 6223 words):
     - `gen_37_38_sold_judah` · `gen_39_41_egypt_rise` · `gen_42_45_brothers`
     - `gen_46_47_migrate` · `gen_48_50_blessings_death`
   **Genesis Build Package 0–6 complete (all 50 chapters as draft units).**  
   Next: thin **Exodus** sanctuary install so Lev free names resolve.  
   On each unit: `logic/SHOW_WORK_TREES_2026-07-20.md`.  
4. Thin **Exodus sanctuary install** so Lev free names resolve.  
5. Lev units `import:` world exports only where real; `import:` Exod for Tent/priests.  
6. Interpreter runs: boot → install → apps.

Lev curriculum can continue in parallel; full “run from scratch” needs Genesis Build + Exodus install + Lev.

---

## 9. One-sentence summary

**Genesis Build = encode Genesis as init logic (ordered boot + world state + exports), same dual-track discipline as Lev, so a full system run has a beginning; Lev does not call boot every time, but the assembled machine does boot once.**
