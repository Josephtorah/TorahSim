# Beginner tutorial: How we derive logic from Genesis (boot)

### You do **not** need to speak Hebrew

**Date:** 2026-07-19  
**Track:** Genesis Build  
**Worked unit:** `logic/units/gen_01_creation_boot.yaml`  
**Approach note:** `reviews/GENESIS_BUILD_2026-07-20.md`  
**Longer tutorial (full pipeline + day 4 show-all-work):** `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md`  
**General Pre-Code method:** `logic/SYSTEM.md` · `logic/TUTORIAL_BEGINNERS.md` (Lev-style purity example)

On update: rename this file to today’s date and fix links.

---

## What you will learn

1. What “logic from Genesis” means (and how it differs from Leviticus)  
2. **Which verses** we used first and why  
3. The **boot logic** we derived (readable without YAML)  
4. **How** we derived it step by step (trees → steps → state → exports)  
5. Where **Oral Torah** fits (helper only, not the boot source)  
6. How this later becomes **computer code**  

---

## Part 1 — Big picture in plain English

### Think “computer boot,” not “sacrifice rules”

| Leviticus units (e.g. offerings) | Genesis 1:1–5 (this tutorial) |
|----------------------------------|-------------------------------|
| “**When** someone offers, **then** do X” | “**In order**, the world is set up like this” |
| Decision tables, procedures | **Init sequence** + **world state** |
| Needs Tent / priests (often from Exodus) | Almost nothing to import yet — **this is the start** |

If we ever “run the whole Torah system” in software:

```text
1. Run Genesis boot   ← you are here
2. … more Genesis / Exodus install …
3. Run Leviticus apps (offerings, purity, …)
```

Leviticus does **not** re-boot the universe for every offering.  
But a **full** run needs Genesis boot **once**.

### Where does the logic come from?

**Strictly from Written Genesis (Hebrew),** same rule as Lev:

```text
Hebrew verse  →  ta'amim tree (how the verse splits)  →  logic document
```

English is only so you can **read** the work.  
English does **not** invent the steps.

---

## Part 2 — Which verses, and why

### Focus: **Genesis 1:1–5** (one unit)

| Verses | Role in the boot |
|--------|------------------|
| **1:1** | Create heavens and earth |
| **1:2** | Describe earth / dark / deep / spirit on waters |
| **1:3** | Speech → light exists |
| **1:4** | Evaluate light as good; separate light from dark |
| **1:5** | Name day/night; evening + morning = **day one** |

### Why not only 1:1?

1:1 alone does not create light or define a **day**.  
We would have no `day_cycle` export for later books to reuse.

### Why not all of chapter 1 yet?

Days 2–6 (sky waters, land, plants, animals, humans) are **later units** when we need those exports.  
**1:1–5** is the smallest **complete first day**.

---

## Part 3 — The logic we derived (the heart of this thread)

Read this as a tiny program that only **initializes** the world.

### A. Ordered steps (the boot log)

```text
STEP 1  [Gen 1:1]  CREATE
        Agent: Elohim / God
        Objects: heavens, earth

STEP 2  [Gen 1:2]  SET_STATE
        Earth: tohu va-vohu (formless/void — keep Hebrew labels)
        Darkness on the deep
        Spirit of God hovering on the waters

STEP 3  [Gen 1:3]  SPEECH_ACT
        God says: "yehi or" / "let there be light"
        Result: light exists

STEP 4a [Gen 1:4]  EVALUATE
        God sees the light: ki tov / "that [it is] good"
        (Note: ki here means "that", NOT "if someone offers…")

STEP 4b [Gen 1:4]  SEPARATE
        God divides between the light and between the darkness

STEP 5a [Gen 1:5]  NAME
        Light → called "day" (yom)
        Darkness → called "night" (laylah)

STEP 5b [Gen 1:5]  TICK_DAY
        Evening + morning → "day one" (yom echad)
```

### B. World state after 1:1–5 (what is true)

After these steps, the logic says the world includes at least:

| State | Plain English |
|-------|----------------|
| Heavens exist | Created in 1:1 |
| Earth exists | Created in 1:1; described in 1:2 |
| Waters present | Locus of hovering in 1:2 |
| Darkness present | 1:2; later named night |
| Light exists | 1:3 |
| Light separated from dark | 1:4 |
| Day / night names | 1:5 |
| Day one completed | 1:5 |

### C. Exports (what later “code modules” may import)

These are **named outputs** of the boot — like public constants:

| Export | Meaning | Why it matters later |
|--------|---------|----------------------|
| `day_cycle` | Evening then morning completes a day | Later law can **join** this pattern of “one day” |
| `light_dark` | Light and dark as a separated pair | Shared symbols |
| `create_by_speech` | Effect by “God said… and it was” | Pattern of speech-creation |
| `agent_elohim` | God as agent in this boot | Continuity of actor |

**Important:** Export ≠ “Gen already contains all later laws.”  
Export = “Gen **defines** this pattern; later text may **reuse** it.”

### D. One-line “program” view

```text
CREATE(heavens, earth)
SET earth = {tohu, vohu, dark, deep, spirit_over_waters}
SPEECH("let there be light") → light
EVALUATE(light, good); SEPARATE(light | dark)
NAME(light→day, dark→night); DAY_1 = evening + morning
```

That is the **logic from this thread**, written so a future interpreter can run it.

---

## Part 4 — How we derived it (method you can repeat)

### Step 1 — Choose a complete narrative packet

Ask: “What is the smallest span that finishes a clear unit of world-setup?”  
Answer here: **through day one (1:5)**.

### Step 2 — Load Hebrew only as source

Source file: `Data/Gen.xml`  
Tool: `python3 taamim_tree_parse.py Gen.1.1 --tree` (and 1.2 … 1.5)

You do not need to read Hebrew alone: every phrase is stored as:

```text
he  +  he_translit  +  en
```

Example:  
**בָּרָא** / *bara* / “created”

### Step 3 — Build the tree first (structure before rules)

Cantillation (ta’amim) splits each verse into a **binary tree**.  
Almost every verse has a strong mid-verse rest (**etnachta**) — think “comma in the middle of the verse.”

**Show all work:** paste each verse’s tree into the unit’s **`binary_trees`** section (including full `tree_ascii` from `--tree`), then fill **`tree_coverage`** for every word. Do not leave trees only in chat.  
Procedure: `logic/SHOW_WORK_TREES_2026-07-20.md`. Day-4 reference: `logic/units/gen_01_day4_lights.yaml`.

| Verse | Left of mid-rest (plain English) | Right of mid-rest |
|-------|----------------------------------|-------------------|
| 1:1 | In the beginning God created | the heavens and the earth |
| 1:2 | Earth was tohu/vohu; dark on the deep | spirit of God hovering on the waters |
| 1:3 | God said “let there be light” | and there was light |
| 1:4 | God saw the light that it was good | God separated light and darkness |
| 1:5 | Called light day, darkness night | evening and morning — day one |

**Rule:**  
Tree halves suggest **chunks of meaning**.  
You still **check the Hebrew** before naming a step.

### Step 4 — Label each chunk with a role (not English theology first)

From the tree, assign roles like:

- `action_create`, `speech_frame`, `result_state`, `action_separate`, `clock_part`, …

Each role **feeds** a step or state id (`STEP_3`, `STATE_light`, …).

This is the same idea as Lev **tree → logic roles**, but roles are **boot-shaped**.

### Step 5 — Write the logic formats

For Genesis boot we fill:

1. **boot_steps** — ordered operations  
2. **state_after** — what is true when the unit finishes  
3. **exports** — what other units may import  
4. **scenarios** — plain-English tests of the document  

We do **not** force a big “IF person offers THEN…” table onto Gen 1:1–5.

### Step 6 — Account for every **word**; optional every **letter** (Oral)

**Word layer (required aspiration):** `tree_coverage` in the unit lists **all 52 leaves** in 1:1–5 — either `logic_bearing` or explicit `glue` (e.g. **אֵת** / *et* object marker).

**Letter layer (optional Oral):** only where classical midrash is explicit.  
Example: letter **ב** / *bet* of **בראשית** (Bereishit Rabbah) → “closed on sides, open forward” = query limit on “before creation.”  
Does **not** change CREATE step.

**Access policy (Oral):** Mishnah Chagigah 2:1 — limits expounding **מעשה בראשית** / *ma’aseh bereshit* / Work of Creation (not the boot step list).

| Source | Role for this unit |
|--------|---------------------|
| **Written Gen** | **Defines** boot steps + every word leaf |
| **Bereishit Rabbah** | Possible Oral — letter-bet, debates; **not** step author |
| **Bavli cites** of Gen 1:x | Possible Oral — inventory, day-template joins |
| **Mishnah Chagigah** | Possible Oral — **who may expound** creation |
| **Mesorat haShas** | Possible Oral peers; **no** MH from Tanakh Gen 1:1 node |

**Never** silent-merge Oral into Written.

### Step 7 — Confidence

Mark each claim:

- **tested** — clear on the Hebrew / tree  
- **hypothesis** — plausible, still open  
- **failed** — tried and rejected  

Example hypothesis: exact English of *tohu/vohu* — keep Hebrew labels + rough gloss.

### Step 8 — Freeze only when ready

`status: draft` now.  
`status: frozen` only when you would trust later code to follow the document without inventing new rules.

---

## Part 5 — Worked mini-example: verse 1:3 only

**Hebrew idea:** God said “let there be light,” and there was light.

**Tree:**

```text
[ God said | let-there-be light ]   ← mid-verse rest on "light" in the command
[ and there was light ]             ← second half: result
```

**Logic:**

```text
SPEECH_ACT(
  agent = Elohim,
  content = "yehi or" / "let there be light"
)
→ RESULT: light exists
```

**Export:** `create_by_speech` (said → was).

**Not logic from English alone:** we did not invent “God thought about light.” The verbs are **said** and **was**.

---

## Part 6 — How this becomes computer code later

```text
TODAY (Pre-Code):
  gen_01_creation_boot.yaml   ← human + machine readable logic

LATER (optional interpreter):
  world = {}
  run_unit("gen_01_creation_boot")  # executes STEP_1 … STEP_5b
  # world["light_exists"] == True
  # world["exports"]["day_cycle"] == "evening_then_morning"

  run_unit("exod_sanctuary_install")  # future
  run_unit("lev_01_olah_...")         # assumes world already booted
```

**Code may only interpret frozen logic.**  
Code must **not** invent new boot steps.

---

## Part 7 — Compare to Leviticus (so you don’t get lost)

| Question | Genesis 1:1–5 | Leviticus 1 (offerings) |
|----------|---------------|-------------------------|
| Main question | What gets **initialized**? | What is **allowed / how is it done**? |
| Typical op | CREATE, SPEECH, SEPARATE, NAME | WHEN, INCLUDE, EXCLUDE, PROCEDURE |
| Tree mid-split | Often **action \| result** or **condition \| next action** | Often **case setup \| place/outcome** |
| Preferred Oral | Bereishit Rabbah / Bavli cites (optional) | Sifra first, then Bavli (possible Oral) |
| Full system | **Boot once** | **App** after boot + Exodus install |

Same **project rules**. Different **shapes**.

---

## Part 8 — Checklist: derive logic from any Genesis narrative span

1. [ ] Pick a **complete** narrative packet (not a half-day if you need day_cycle).  
2. [ ] Load **Hebrew** (`Data/Gen.xml`).  
3. [ ] Parse **trees** (`taamim_tree_parse.py Gen.x.y --tree`).  
4. [ ] For each verse, write **left \| right** of etnachta in English *after* seeing Hebrew+translit.  
5. [ ] Name **ops** (CREATE, SET_STATE, SPEECH_ACT, …) only if the Hebrew verbs support them.  
6. [ ] List **state** true after the span.  
7. [ ] List **exports** later modules might import.  
8. [ ] Add **scenarios** that a human can check without code.  
9. [ ] Optional **Oral** notes — named, dual-track, never invent Written steps.  
10. [ ] Mark **confidence** on every claim.  

---

## Part 9 — Files to open

| File | What it is |
|------|------------|
| `logic/units/gen_01_creation_boot.yaml` | Full formal logic (steps, trees, exports, scenarios) |
| `reviews/GENESIS_BUILD_2026-07-20.md` | Why Gen is boot for the whole system |
| `logic/TUTORIAL_BEGINNERS.md` | General Pre-Code (Lev 12 example) |
| `logic/SYSTEM.md` | Full method A–J |
| Command | `python3 taamim_tree_parse.py Gen.1.3 --tree` |

---

## Part 10 — Bottom line (memorize this)

**We derive Genesis boot logic the same way we derive Leviticus logic: from Hebrew + ta’amim trees into a Pre-Code document.**  

**The content of that logic is different: ordered world initialization and exports, not offering decision tables.**  

**Oral Torah may annotate and join; it does not write the boot steps.**  

**Later computer code only runs what this document already says.**

---

## Appendix — Logic at a glance (copy/paste)

```text
# Gen 1:1–5 boot (Written face)

CREATE(heavens, earth)                    # 1:1
SET earth = tohu/vohu; dark on deep;
    spirit of God over waters             # 1:2
SPEECH("let there be light") → light      # 1:3
EVALUATE(light, good)                     # 1:4a
SEPARATE(light | dark)                    # 1:4b
NAME(light→day, dark→night)               # 1:5a
DAY_1 = evening + morning                 # 1:5b

EXPORT day_cycle = evening_then_morning
EXPORT light_dark pair
EXPORT create_by_speech
```

That is the logic from this work, for beginners and for future code.
