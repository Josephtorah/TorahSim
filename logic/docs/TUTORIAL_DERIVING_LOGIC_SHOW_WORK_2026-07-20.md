# Tutorial: How we derive logic from the Torah (show all work)

### For beginners and intermediate readers · **You do not need to speak Hebrew**

**Date:** 2026-07-20  
**Status:** living tutorial — experimental models, **not** binding religious law  
**Main worked example:** Genesis day 4 · unit `logic/units/gen_01_day4_lights.yaml`  
**Also useful:** Lev legal path · `logic/TUTORIAL_BEGINNERS.md` · `logic/units/lev_12_childbirth.yaml`

On substantive update: rename this file to today’s date and fix in-repo links.

---

## Table of contents

1. [What this project is doing](#1-what-this-project-is-doing)  
2. [Rules of the road (never skip these)](#2-rules-of-the-road-never-skip-these)  
3. [Two genres of “logic”](#3-two-genres-of-logic)  
4. [The pipeline end-to-end](#4-the-pipeline-end-to-end)  
5. [Vocabulary you’ll need](#5-vocabulary-youll-need)  
6. [Step by step — with all work shown (Day 4)](#6-step-by-step--with-all-work-shown-day-4)  
7. [Deep dive: reading a ta'amim tree](#7-deep-dive-reading-a-taamim-tree)  
8. [From trees to boot steps](#8-from-trees-to-boot-steps)  
9. [100% word coverage (`tree_coverage`)](#9-100-word-coverage-tree_coverage)  
10. [State, exports, scenarios](#10-state-exports-scenarios)  
11. [Where Oral Torah fits (and does not)](#11-where-oral-torah-fits-and-does-not)  
12. [How this differs from Leviticus units](#12-how-this-differs-from-leviticus-units)  
13. [Where every artifact lives in the repo](#13-where-every-artifact-lives-in-the-repo)  
14. [Common mistakes](#14-common-mistakes)  
15. [Practice checklist (do the next unit yourself)](#15-practice-checklist-do-the-next-unit-yourself)  
16. [Further reading](#16-further-reading)

---

## 1. What this project is doing

We are building **precise, checkable logic documents** from the **Hebrew** text of the Torah.

Think of it this way:

```text
Not this:  “I remember the English story, so I’ll invent rules.”
This:      “Here is the Hebrew verse → here is how it splits →
            here is every word’s job → here is an ordered logic log.”
```

The finished product is a **YAML unit** under `logic/units/` — a human-readable logic package.  
**Python does not invent the rules.** Python may later *run* a frozen document. Our parser only turns cantillation marks into trees.

**Analogy:**

| Role | Everyday analogy |
|------|------------------|
| Hebrew Torah | Original recipe language |
| Ta'amim tree | How the recipe’s sentences are punctuated / nested |
| Logic unit | Clear procedure card: do A, then B, state is X |
| Later code | A robot that only follows the procedure card |
| English | Sticky notes so you can *read* the card |

---

## 2. Rules of the road (never skip these)

### 2.1 Hebrew is the source; English is a reading aid

We open `Data/Gen.xml` (or other Hebrew sources).  
English Bibles help *you* understand; they **do not** invent conditions, objects, or steps.

### 2.2 Never bare Hebrew

Every Hebrew string appears with **three** parts:

```text
עברית   /   translit   /   "English gloss"
```

Example:

```text
מְאֹרֹת   /   me'orot   /   "luminaries, light-bearers"
```

In structured fields we use:

```yaml
he: "מְאֹרֹת"
he_translit: "me'orot"
en: "luminaries / light-bearers"
```

### 2.3 Show all work

Structure and roles are **written into the unit file**, not left only in chat history.

| Layer | Unit section | What it proves |
|-------|--------------|----------------|
| How the verse splits | `binary_trees` | We used ta'amim, not English punctuation |
| Every word’s job | `tree_coverage` | No silent leftover words |
| The logic | `boot_steps` or decision tables | Ordered / conditional rules |
| Optional Oral | `oral_notes` | Named sources only |

Full policy: `logic/SHOW_WORK_TREES_2026-07-20.md` · `reviews/STANDING_DECISIONS.md` §6a.

### 2.4 Oral Torah is dual-track

If we use midrash or Talmud, we **name the place** and keep it separate from Written boot/law steps.  
We never silently rewrite Genesis to match a midrash story.

### 2.5 Experimental ≠ binding law

These models help us think carefully about structure and sequence.  
They are **not** presented as binding religious law unless the owner explicitly asks for that framing.

### 2.6 Label confidence

| Label | Meaning |
|-------|---------|
| `hypothesis` | Plausible; not fully checked |
| `tested` | Checked against trees / scenarios |
| `established` | Stable for this project so far |
| `failed` / `dead_end` | Tried; document the failure |

---

## 3. Two genres of “logic”

Not every book of the Torah is the same *shape* of logic.

### 3.1 Genesis Build — **boot / init** (our main example here)

```text
Ordered steps that set up the world
  CREATE → SPEECH → MAKE → PLACE → EVALUATE → TICK_DAY …
World STATE accumulates
EXPORTS = symbols later modules may import
```

Like turning on a computer:

```text
Genesis   →  BIOS / OS boot (once)
Exodus    →  install sanctuary “machine” (later, thin)
Leviticus →  run offering / purity apps
```

You do **not** reboot the universe for every sacrifice.  
You **do** need a boot if you want a full run from scratch.

### 3.2 Leviticus-style — **cases and procedures**

```text
WHEN someone offers / is impure …
THEN do this procedure / wait this many days
```

Decision tables, purity state machines, type registries (cattle vs flock).

**Same machinery** (Hebrew → trees → unit YAML · dual-track Oral).  
**Different template** (boot log vs IF/THEN tables).

---

## 4. The pipeline end-to-end

```text
┌─────────────────────────────────────────────────────────────┐
│  1. Choose a unit (complete packet of verses)               │
│     e.g. Gen 1:14–19 = day four                             │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Load Hebrew source                                      │
│     Data/Gen.xml  (English only as aid)                     │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Parse ta'amim trees (our versioned rules)               │
│     python3 taamim_tree_parse.py Gen.1.14 --tree            │
│     RECORD under binary_trees (tree_ascii, top split, …)    │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  4. tree_coverage — every leaf gets a role                  │
│     (logic_bearing or explicit glue)                        │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Invent logic ONLY in the YAML unit                      │
│     boot_steps  OR  decision_table / FSM / rules            │
│     Cite tree nodes / leaves                                │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  6. state_after · exports · scenarios                       │
│     Optional oral_notes (named, dual-track)                 │
└────────────────────────────┬────────────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  7. status: draft → review → frozen                         │
│     Only then may code interpret the document               │
└─────────────────────────────────────────────────────────────┘
```

**What we refuse to do:** invent rules in Python, invent structure from English, merge midrash into Written without a citation, leave trees only in a chat transcript.

---

## 5. Vocabulary you’ll need

| Term | Plain English |
|------|----------------|
| **Unit** | One YAML file = one logic package (e.g. day four) |
| **Verse** | One numbered line of Torah (e.g. Genesis 1:16) |
| **Ta'amim** | Cantillation marks — traditional punctuation / music marks on Hebrew words that **also** encode phrase structure |
| **Disjunctive** | A mark that **splits** phrases (like a strong comma or semicolon) |
| **Conjunctive** | A mark that **binds** words together |
| **Etnachta** | Very common mid-verse rest — often the main left/right split |
| **Silluq** | End-of-verse mark |
| **Leaf** | One word at the bottom of the tree |
| **Binary tree** | Most phrases split into **two** children (left/right). Sometimes our parser keeps 3- or 4-way nodes when marks don’t force a clean pair |
| **Boot step** | One ordered action in Genesis-style units (`SPEECH_ACT`, `MAKE`, …) |
| **Export** | A named result later units may import |
| **Glue** | A word that holds grammar together (e.g. אֶת / *et* object marker) — still listed, not ignored |
| **Mesorat haShas (MH)** | Traditional parallel index among Oral texts; **every MH endpoint is possible Oral** for this project |

---

## 6. Step by step — with all work shown (Day 4)

### 6.1 Why day four?

By day three we already have:

| Day | What exists (roughly) |
|-----|------------------------|
| 1 | Light / dark; day and night **names**; evening→morning clock |
| 2 | רָקִיעַ / *raqia* / “firmament” named שָׁמַיִם / *shamayim* / “heavens” |
| 3 | Dry land named אֶרֶץ / *erets* / “earth”; plants by kind |

Day four **installs luminaries** into that sky shelf and gives them **time, rule, and lighting** jobs.

**Unit id:** `gen_01_day4_lights`  
**Verses:** Genesis **1:14–19**  
**File:** `logic/units/gen_01_day4_lights.yaml`

### 6.2 Step A — Choose the block

**Question:** What is the smallest complete packet?

**Answer:** One creation **day** — speech through evening/morning “fourth day.”

```text
1:14–15  SPEECH + “and it was so”
1:16     MAKE the lights + stars
1:17–18  PLACE + jobs + “good”
1:19     TICK day four
```

We write this in `derivation_log` step A so a future reader sees **why** these verses belong together.

### 6.3 Step B — Load Hebrew and parse trees

**Source:** `Data/Gen.xml`  
**Command (repeat for 14…19):**

```bash
cd /path/to/TorahSim
python3 taamim_tree_parse.py Gen.1.14 --tree
python3 taamim_tree_parse.py Gen.1.14 --json   # machine form if needed
```

**Rule set:** `logic/taamim_rules/CURRENT` → currently `v1`.

We do **not** stop after looking at the terminal. We **paste** into the unit:

- full `tree_ascii`
- top left/right split with he + translit + en
- `pure_binary: true/false`
- `maps_to: [STEP_…]`

That is “show all work.”

### 6.4 Plain English of the six verses (reading aid)

| Ref | Plain English (aid only) |
|-----|---------------------------|
| 1:14 | God said: let there be luminaries in the firmament of the heavens to separate day from night; and let them be for signs, appointed times, days, and years. |
| 1:15 | And let them be for luminaries… to give light on the earth; **and it was so**. |
| 1:16 | God **made** the two great luminaries: the **great** light for rule of the day, the **small** light for rule of the night, and the stars. |
| 1:17 | God **set them** in the firmament of the heavens to give light on the earth. |
| 1:18 | …and to **rule** in day and night, and to **separate** light from darkness; God saw that it was **good**. |
| 1:19 | Evening and morning: **fourth day**. |

### 6.5 Key Hebrew atoms (with training wheels)

| Hebrew | Transliteration | English | Why it matters |
|--------|-----------------|---------|----------------|
| מְאֹרֹת | *me'orot* | luminaries / light-bearers | Day-4 objects — **not** the same word as day-1 light |
| אוֹר | *or* | light | Day-1 phenomenon (already exists) |
| רָקִיעַ | *raqia* | firmament / expanse | Day-2 place where lights go |
| לְהַבְדִּיל | *le-havdil* | to separate | Job: day\|night and later light\|dark |
| אֹתֹת | *otot* | signs | Calendar / signal function |
| מוֹעֲדִים | *mo'adim* | appointed times | Calendar stack |
| יָמִים | *yamim* | days | Calendar stack |
| שָׁנִים | *shanim* | years | Calendar stack |
| וַיַּעַשׂ | *va-ya'as* | and He made | MAKE op (like day 2) |
| מֶמְשֶׁלֶת | *memshelet* | rule / dominion | Great→day, small→night |
| הַמָּאוֹר הַגָּדֹל | *ha-ma'or ha-gadol* | the great light | Written label — **not** “sun” |
| הַמָּאוֹר הַקָּטֹן | *ha-ma'or ha-qaton* | the small light | Written label — **not** “moon” |
| כּוֹכָבִים | *kokhavim* | stars | Made with the two lights |
| וַיִּתֵּן | *va-yiten* | and He set/gave | PLACE op |
| לִמְשֹׁל | *limshol* | to rule | Function paired with *memshelet* |
| כִּי־טוֹב | *ki-tov* | that [it was] good | EVALUATE |
| יוֹם רְבִיעִי | *yom revi'i* | fourth day | Day clock |

**Critical honesty check:**  
English Bibles say “sun” and “moon.” The **Written Hebrew of 1:16** says great light / small light.  
We keep “sun/moon” as English aid or optional Oral naming — **not** as Written boot labels.

### 6.6 Light vs luminaries (lock this in)

```text
Day 1:  CREATE  אוֹר / or / "light"           ← the phenomenon
Day 4:  MAKE    מְאֹרֹת / me'orot / "luminaries" ← the instruments
```

Day four is **not** “God created light again.”  
It is “God installed light-bearers for time, rule, and lighting the earth.”

---

## 7. Deep dive: reading a ta'amim tree

### 7.1 What the tree is

Each **word** is a **leaf**.  
**Phrases** nest above leaves.  
Strong disjunctive marks decide **where** to split.

You do not need to memorize mark names. Focus on:

1. **Top split** (usually etnachta): left half vs right half  
2. Nested pairs that group meaning  
3. Which leaves are glue vs content  

### 7.2 Full work — Genesis 1:14 (speech + calendar)

**Linear (he + translit + en):**

- **he:** וַיֹּאמֶר אֱלֹהִים יְהִי מְאֹרֹת בִּרְקִיעַ הַשָּׁמַיִם לְהַבְדִּיל בֵּין הַיּוֹם וּבֵין הַלָּיְלָה וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים  
- **he_translit:** *va-yomer Elohim yehi me'orot bi-rqia ha-shamayim le-havdil bein ha-yom u-vein ha-lailah ve-hayu le-otot u-le-mo'adim u-le-yamim ve-shanim*  
- **en:** God said: let there be luminaries in the firmament of the heavens to separate the day from the night; and let them be for signs and for appointed times and for days and years.

**Top split (after etnachta on “night”):**

| Side | Meaning |
|------|---------|
| **LEFT** | Speech: let there be luminaries in the firmament; **to separate day \| night** |
| **RIGHT** | **Calendar stack:** signs · mo'adim · days · years |

**ASCII tree (from our parser — this is the recorded work):**

```text
PHRASE (binary 16w)
├── LEFT (through etnachta on night)
│   ├── God said + let-there-be me'orot in firmament of heavens
│   └── to-separate between day | between night
└── RIGHT
    └── and they shall be for signs · mo'adim · days · years
```

(Exact full ASCII with mark ranks is stored in the unit under `binary_trees.verse_trees.Gen_1_14.tree_ascii`.)

**Logic we take from this tree:**

- One **SPEECH_ACT** creates the *idea* of luminaries.  
- Jobs already include **separate day|night** and **time functions**.  
- Location reuses day-2 **firmament of heavens**.

**Maps to:** `STEP_D4_1`

### 7.3 Genesis 1:15 — fulfillment seal

**Top split:**

| LEFT | RIGHT |
|------|-------|
| Be luminaries in firmament **to light the earth** | **וַיְהִי־כֵן** / *va-yehi ken* / “and it was so” |

Pattern shared with days 2–3: speech purpose, then **fulfillment seal**.

**Maps to:** `STEP_D4_2`

### 7.4 Genesis 1:16 — MAKE (the richest verse)

**Plain English:** God made the two great luminaries — great light for day-rule, small light for night-rule — and the stars.

**Top split:**

| LEFT | RIGHT |
|------|-------|
| God **made** the two great luminaries | Detail: great→day, small→night, **and the stars** |

**Full parser tree (show work):**

```text
PHRASE (binary 18w)
├── LEFT (to etnachta)
│   ├── [0] וַיַּעַשׂ / va-ya'as / "and He made"
│   ├── [1] אֱלֹהִים / Elohim / "God"
│   └── the two great luminaries  (includes 3-ary object phrase)
└── RIGHT
    ├── great light → for rule of the day
    ├── small light → for rule of the night
    └── and the stars
```

**Honest note — not pure binary everywhere:**  
Under rule set **v1**, some object phrases are **3-ary** (three children), e.g. אֶת + שְׁנֵי + הַמְּאֹרֹת.  
We record `pure_binary: false`. We do **not** invent fake left/right splits to look prettier.

**Logic:**

| Op | Op name | Evidence |
|----|---------|----------|
| MAKE | `va-ya'as` | Execution after speech (like day 2 firmament) |
| Dominion | *memshelet* | Great → day; small → night |
| Stars | *kokhavim* | Made; **no** separate dominion clause |

**Maps to:** `STEP_D4_3`

### 7.5 Genesis 1:17 — PLACE

**Top split:**

| LEFT | RIGHT |
|------|-------|
| God **set them** in the firmament of the heavens | to give light upon the earth |

Install hardware into day-2 locus; purpose = illuminate day-3 earth.

**Maps to:** `STEP_D4_4`

### 7.6 Genesis 1:18 — jobs + evaluation

**Top split:**

| LEFT | RIGHT |
|------|-------|
| to **rule** day and night; to **separate** light \| dark | God saw **that it was good** |

Two separation axes in day 4:

| Verse | Axis | Hebrew pair |
|-------|------|-------------|
| 1:14 | day \| night | יוֹם / *yom* · לַיְלָה / *lailah* |
| 1:18 | light \| dark | אוֹר / *or* · חֹשֶׁךְ / *choshekh* |

Both reuse day-1 vocabulary; day 4 **instruments** them via luminaries.

**Maps to:** `STEP_D4_5` (functions) + `STEP_D4_6` (evaluate)

### 7.7 Genesis 1:19 — close the day

**Top split:**

| LEFT | RIGHT |
|------|-------|
| evening + morning | fourth day |

Same day-cycle export as days 1–3: evening then morning completes a day index.

Left block is **4-ary** under v1 (`pure_binary: false` for internals). Still clear logic.

**Maps to:** `STEP_D4_7`

---

## 8. From trees to boot steps

After trees exist, we write an **ordered boot log**.  
Each step quotes Hebrew with translit + English and cites the verse.

### 8.1 The day-4 program (readable form)

```text
STEP 1  [1:14]  SPEECH_ACT
        Let there be me'orot in the firmament
        Jobs: separate day|night; signs, mo'adim, days, years

STEP 2  [1:15]  SPEECH_ACT_CONTINUE
        Be luminaries to light the earth
        Seal: va-yehi ken / "and it was so"

STEP 3  [1:16]  MAKE
        Two great lights + stars
        Great → rule of day; small → rule of night

STEP 4  [1:17]  PLACE
        Set them in firmament of heavens to light earth

STEP 5  [1:18a] ASSIGN_FUNCTIONS
        Rule in day and night; separate light|dark

STEP 6  [1:18b] EVALUATE
        ki-tov / "that it was good"

STEP 7  [1:19]  TICK_DAY
        Evening + morning → day 4
```

### 8.2 How a tree “justifies” a step

Example for STEP 3:

| Tree evidence | Boot field |
|---------------|------------|
| Leaf וַיַּעַשׂ / *va-ya'as* / “made” | `op: MAKE` |
| Great light + *memshelet* + day | dominion binding |
| Stars as sibling object under right arm | stars exist, no dominion clause |
| Top left = make two great lights | one MAKE step, not three random English sentences |

We never invent a step that has **no** Written leaf supporting it.

### 8.3 Ops we reuse across Genesis days

| Op | Rough meaning | Seen on |
|----|---------------|---------|
| `SPEECH_ACT` | God said… | 1, 2, 3, 4 |
| `MAKE` | *va-ya'as* execution | 2, 4 |
| `PLACE` | *va-yiten* install | 4 |
| `NAME` | *va-yikra* call X Y | 1, 2, 3 |
| `EVALUATE` | *va-yar … ki-tov* | 1, 3, 4 (not day 2) |
| `TICK_DAY` | evening + morning + day N | every day |
| `va-yehi ken` | fulfillment seal | 2, 3, 4 |

This reuse is intentional: same “instruction set,” different payloads.

---

## 9. 100% word coverage (`tree_coverage`)

### 9.1 Why

If we only pick “important” words, we can smuggle English assumptions in the gaps.  
Aspiration: **every leaf** is either:

- `logic_bearing` — carries meaning for a step, or  
- `glue` — grammar/structure, **explicitly** marked (not ignored)

### 9.2 Day 4 counts

| Verse | Words |
|-------|------:|
| 1:14 | 16 |
| 1:15 | 9 |
| 1:16 | 18 |
| 1:17 | 8 |
| 1:18 | 12 |
| 1:19 | 6 |
| **Total** | **69** |

### 9.3 Sample rows (Genesis 1:14)

| # | he | translit | en | role | kind | feeds |
|---|----|----------|----|------|------|-------|
| 0 | וַיֹּאמֶר | *va-yomer* | and He said | speech_frame | logic_bearing | STEP_D4_1 |
| 1 | אֱלֹהִים | *Elohim* | God | agent | logic_bearing | STEP_D4_1 |
| 2 | יְהִי | *yehi* | let there be | speech_content_verb | logic_bearing | STEP_D4_1 |
| 3 | מְאֹרֹת | *me'orot* | luminaries | speech_content_object | logic_bearing | STEP_D4_1 |
| 6 | לְהַבְדִּיל | *le-havdil* | to separate | purpose_separate | logic_bearing | STEP_D4_1 |
| 12 | לְאֹתֹת | *le-otot* | for signs | time_function | logic_bearing | STEP_D4_1 |

### 9.4 Sample glue (Genesis 1:16)

| he | translit | en | role | kind |
|----|----------|----|------|------|
| אֶת | *et* | object marker | glue_object_marker | glue |

Glue still **feeds** the MAKE step — it is structure work, not “trash.”

### 9.5 Relationship to TIR catalog

Long-term, roles should cite reusable **TIR-xxx** rules (`logic/TREE_INTERPRETATION_RULES.md`).  
Early units may have roles without a TIR id yet — that is backlog, not silence.

---

## 10. State, exports, scenarios

### 10.1 State after day 4

After the boot log runs, the world includes at least:

- Luminaries exist (spoken, made, placed)  
- Great light with day dominion; small light with night dominion  
- Stars present  
- Lights sit in the firmament and illuminate earth  
- Day index includes day 4  

### 10.2 Exports (public API of the unit)

| Export idea | Why a later module might care |
|-------------|-------------------------------|
| `me'orot` vs day-1 `or` | Don’t confuse instruments with first light |
| Calendar stack otot · mo'adim · yamim · shanim | Festivals / time later |
| *memshelet* dominion | Rule patterns |
| Dual separate axes | day\|night and light\|dark |
| No Written sun/moon names | Honesty about 1:16 labels |
| Day 4 complete | Sequential boot |

### 10.3 Scenarios (tests without running code)

Scenarios are **stories** that should match the document:

1. After 1:15 — speech sealed with *va-yehi ken*?  
2. After 1:16 — two lights + stars; great→day; small→night; no required sun/moon names?  
3. After 1:17–18 — placed, ruling, separating light|dark, *ki-tov*?  
4. After 1:19 — day_index = 4?  
5. Import chain — uses day-1 names, day-2 raqia, day-3 earth?

If a scenario fails, the **document** is wrong or incomplete — fix the YAML, don’t patch Python.

---

## 11. Where Oral Torah fits (and does not)

### 11.1 Dual-track picture

```text
Written face (boot steps)     Oral track (optional notes)
─────────────────────────     ───────────────────────────
Gen 1:14–19 Hebrew only       Bereishit Rabbah on these verses
ta'amim trees                 Bavli quotes (via cite_index path)
                              MH among Oral peers
```

Oral may **annotate**, **compare**, or **thicken** discussion.  
Oral must **not** invent Written boot steps without being labeled.

### 11.2 Mesorat haShas policy (standing decision)

Every MH endpoint is **possible Oral**.  
Nothing on the MH graph is ruled out.  
**Job preference** only chooses what to open first (e.g. Sifra first on Lev; midrash often first on Gen narrative).

Research: `reviews/RESEARCH_valid_oral_torah_2026-07-19.md` §6.

### 11.3 Path for Genesis 1

Tanakh verse nodes often have **0** direct MH edges in our link data.  
Typical path:

```text
verse → midrash (e.g. Bereishit Rabbah) → MH among Oral peers
optional: Bavli paren cites via cite_index
```

### 11.4 Day-4 oral stubs (examples of correct style)

- Possible BR on *me'orot*  
- Possible Bavli cites later  
- Note that *shemesh* / *yareach* (sun / moon) names are common later Hebrew / Oral usage — **not** Written 1:16 labels  

---

## 12. How this differs from Leviticus units

| | Genesis day 4 | Leviticus (e.g. olah / Lev 12) |
|--|---------------|--------------------------------|
| Goal | Initialize world features | Case law / ritual procedure |
| Main logic shape | Ordered `boot_steps` | `decision_table` / FSM / `rules` |
| Typical Oral first open | Midrash (BR) | Sifra (for Lev) then MH / Bavli |
| Needs Tent/priests? | No | Often yes (Exodus install later) |
| Same non-negotiables | Hebrew source, trees, show work, dual-track Oral, he+translit+en | same |

If you want the **legal** walkthrough next, open:

- `logic/TUTORIAL_BEGINNERS.md` (Lev 12, very gentle)  
- `logic/units/lev_01_call_and_korban_opening.yaml`  
- `logic/units/lev_01_olah_cattle_procedure.yaml`

---

## 13. Where every artifact lives in the repo

```text
the-workshop/
├── Data/Gen.xml                    # Hebrew source (do not casually edit)
├── taamim_tree_parse.py            # Interprets ta'amim rules only
├── logic/
│   ├── taamim_rules/v1/            # Frozen ranks + algorithm
│   ├── SHOW_WORK_TREES_*.md        # Where to record trees
│   ├── SYSTEM.md                   # Full Pre-Code method
│   ├── SCHEMA.yaml                 # Field definitions
│   ├── templates/unit_template.yaml
│   ├── TREE_INTERPRETATION_RULES.md
│   ├── TUTORIAL_BEGINNERS.md       # Lev-oriented beginner path
│   ├── TUTORIAL_GENESIS_BUILD_*.md # Day-1 boot short tutorial
│   ├── TUTORIAL_DERIVING_LOGIC_SHOW_WORK_*.md  # THIS file
│   └── units/
│       ├── gen_01_creation_boot.yaml
│       ├── gen_01_day2_raqia.yaml
│       ├── gen_01_day3_land_plants.yaml
│       ├── gen_01_day4_lights.yaml   # Full trees + boot (reference)
│       └── lev_*.yaml
└── reviews/
    ├── STANDING_DECISIONS.md       # Agent defaults (§6a trees)
    └── GENESIS_BUILD_*.md          # Why Gen is boot for full system run
```

---

## 14. Common mistakes

| Mistake | Better |
|---------|--------|
| Invent steps from an English Bible alone | Quote Hebrew leaves; English is aid |
| Leave trees only in chat | Paste `tree_ascii` into `binary_trees` |
| Only list “important” words | Fill `tree_coverage` for **all** leaves |
| Call 1:16 “sun and moon” as Written | Great light / small light; sun/moon as aid or Oral |
| Merge midrash into boot steps silently | Dual-track `oral_notes` with named locus |
| Write `if verse == "Gen.1.16"` in parser | Fix rules in new `taamim_rules/vN` |
| Treat draft YAML as religious law | Label experimental; owner may reframe later |
| Skip day dependencies | Day 4 imports days 1–3 geometry |

---

## 15. Practice checklist (do the next unit yourself)

Use this for **Genesis day 5** (1:20–23) or any new unit.

### A. Setup

- [ ] Create `logic/units/gen_01_day5_….yaml` from `logic/templates/unit_template.yaml`  
- [ ] Fill `meta` (id, refs, depends_on, genre: `narrative_boot`)  
- [ ] Write `derivation_log` step A: why this verse block is one unit  

### B. Trees (show all work)

- [ ] For each verse: `python3 taamim_tree_parse.py Gen.1.N --tree`  
- [ ] Under `binary_trees`: `rule_set_version`, per-verse linear (he+translit+en), top split, **`tree_ascii`**, `pure_binary`, `maps_to`  
- [ ] Never bare Hebrew  

### C. Coverage

- [ ] `tree_coverage` with every leaf: role + kind + feeds  
- [ ] Count words; assert total matches parser  

### D. Logic

- [ ] Ordered `boot_steps` only from Written  
- [ ] Each step: op, ref, he+translit+en, confidence, source `[HE-WRITTEN]`  
- [ ] `state_after` + `exports` + `scenarios`  

### E. Oral (optional)

- [ ] `oral_notes` with work name + status `possible_oral`  
- [ ] No silent merge into steps  

### F. Honest labels

- [ ] `confidence_overall`  
- [ ] Open questions listed  
- [ ] Experimental disclaimer  

---

## 16. Further reading

| Doc | When to open it |
|-----|-----------------|
| `logic/units/gen_01_day4_lights.yaml` | See real trees + steps + 69-word coverage |
| `logic/SHOW_WORK_TREES_2026-07-20.md` | Procedure for storing trees |
| `logic/gen_boot/TUTORIAL_GENESIS_BUILD_2026-07-19.md` | Shorter day-1 boot tutorial (see also `logic/gen_boot/INDEX.md`) |
| `logic/TUTORIAL_BEGINNERS.md` | Lev 12 purity walkthrough |
| `logic/SYSTEM.md` | Full Pre-Code method (A–J) |
| `logic/TAAMIM_TREE_PARSER.md` | How the parser and versions work |
| `reviews/GENESIS_BUILD_2026-07-20.md` | Why Gen is boot for a full system run |
| `reviews/STANDING_DECISIONS.md` | Agent defaults (MH, trees, curriculum) |
| `reviews/RESEARCH_valid_oral_torah_2026-07-19.md` | Oral / MH policy research |

---

## Appendix A — Day-4 boot log one-pager

```text
IMPORTS:  day1 light/dark + day/night names + day_cycle
          day2 raqia/shamayim
          day3 erets (earth) as illuminate target

1:14  SPEAK   me'orot in raqia | separate day|night | otot, mo'adim, yamim, shanim
1:15  SPEAK+  light the earth | va-yehi ken
1:16  MAKE    two great lights + stars | great→day rule | small→night rule
1:17  PLACE   in raqia of heavens | light the earth
1:18  JOBS    rule day&night | separate light|dark | EVALUATE good
1:19  TICK    evening + morning = day 4

EXPORTS:  luminaries, calendar stack, dominion, dual separate axes,
          illuminate_earth, no Written sun/moon names, day_4
```

---

## Appendix B — Minimal mental model

If you remember only five sentences:

1. **Hebrew** is the source; English helps you read.  
2. **Trees first** (ta'amim), stored in the unit — show all work.  
3. **Every word** gets a role (`tree_coverage`).  
4. **Logic** is ordered boot steps (Genesis) or WHEN/THEN tables (Leviticus), written in YAML — not invented in Python.  
5. **Oral** is optional, named, dual-track — never a silent rewrite of Written.

---

*End of tutorial. Next natural practice: Genesis day 5 (1:20–23), using the checklist in §15 and day 4 as the formatting reference.*
