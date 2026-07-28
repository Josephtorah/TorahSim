# Experiment — poetry seed set with trackable plain-verse logic

**Date:** 2026-07-27  
**Kind:** experiment design + first force-prose previews · **not** finished poetry grammar  
**Data:** morphhb WLC · marks inventory in `_poetry_logic_candidates_2026-07-27.json`  
**Display:** locked top-down (`DISPLAY_FORMAT.md`); trees below are **force-prose debug** until `ranks_poetry` ships  

---

## 1. Why these books/verses

We want poetry where **logic is obvious from the plain verse** (IF/THEN, dual paths, equations), so we can check whether the **tree shape** matches the **claim shape** — without needing dense midrash first.

| Genre | Why good for logic tracking |
|-------|-----------------------------|
| **Proverbs** | Dual lines: A vs B, cause → effect, X = Y |
| **Psalm 1** | Two ways: righteous path vs wicked path; clear NOT-ladder |
| **Job frame vs body** | Control: prose marks vs poetry marks |

**Avoided for first seed:** long theophanies, dense Job speeches, pure praise lists with weak binary claims.

---

## 2. Recommended seed set (primary)

### Tier A — start here (best logic + short)

| Ref | Plain logic (trackable) | Why for tree experiment |
|-----|-------------------------|-------------------------|
| **Prov 1:7** | Fear-of-LORD ⇔ start of knowledge; fools despise wisdom | Dual: **positive equation** ‖ **negative reaction** |
| **Prov 3:5** | Trust LORD ‖ do not lean on own understanding | Dual **commands** (do / do-not) |
| **Prov 3:6** | Know him in all ways → he straightens paths | **IF/THEN** (human act → divine result) |
| **Prov 14:12** | Way seems right → end is death | **Seems** vs **end** (deceptive path) |
| **Prov 4:18** | Path of righteous like light growing to day | Path-light (ties H216 light work) |
| **Prov 6:23** | Mitzvah=lamp; torah=light; discipline=way of life | **Triple equation** (already in light studies) |
| **Prov 10:1** | Wise son → father joy ‖ foolish son → mother grief | Classic **A vs B** proverb |
| **Ps 1:6** | LORD knows righteous way ‖ wicked way perishes | Clean **two ways** close |
| **Ps 1:1** | Happy = not walk / not stand / not sit (evil seats) | Three-step **negation ladder** (harder marks) |
| **Job 1:1** | Control: prose narrative frame | **Must parse as prose**, not poetry |
| **Job 3:3** | Control: poetry body sample | Poetry marks on lament |

### Tier B — later

Ps 1:2 (torah delight); more Prov duals; one longer Prov unit.

---

## 3. What the marks already show (inventory)

Poetry verses in this set repeatedly show marks our prose table only half-knows:

| Mark (as named under prose ranks) | Role in poetry seed |
|-----------------------------------|---------------------|
| **dehi** | Very common on divine name / path words (e.g. יהוה in Prov 1:7, 3:5) |
| **revia** + **geresh_muqdam** | Often on second stich |
| **ole** (+ mercha) | Poetic; Prov 10:1 *Shelomoh*; Ps 1 |
| **zinor**, **yerah ben yomo** | Ps 1:1 — clearly non-prose inventory |

**Pattern under force-prose (debug only):** most of these short proverbs collapse to a **3-brick** shape:

```text
LEFT  (through etnachta)   = claim A
RIGHT = [ mid brick | silluq brick ]  = claim B / result
```

That often **matches** dual-logic proverbs — encouraging — but **dehi/ole/zinor** are not properly ranked as poetry yet, so this is **provisional**.

**Job 1:1** uses prose-like marks (tevir, tifcha, etnachta, darga…) and a **deeper** brick tree — good control that frame ≠ poetry body.

---

## 4. Three top-down previews (force-prose · track logic)

> **Label every tree:** `force-prose DEBUG — not ranks_poetry`  
> When poetry ranks exist, re-display under locked format without that warning.

### Prov 3:5 — dual command (easiest logic track)

```text
### TREE  Prov.3.5  ·  force-prose DEBUG  ·  pure binary + glue
words=9 · bricks=3
en: "Trust in the LORD with all your heart, and do not lean on your own understanding."

PLAIN LOGIC
  A: TRUST  →  LORD  (with whole heart)
  B: DO NOT lean  →  on your understanding
  Shape: command-pair (positive ‖ negative)

TOP-DOWN (provisional)
PHRASE  (9w · binary)
├── B0 [0–4] · GLUE  "trust in the LORD with all your heart"   ← etnachta
└── PHRASE  (4w · binary)
    ├── B1 [5–6] · GLUE  "and on your understanding"
    └── B2 [7–8] · GLUE  "do not lean"                         ← silluq

TRACK CHECK
  ✓ Top split separates A from B
  ✓ Negation "do not lean" sits in right half
  ? dehi on יהוה ranked under prose table — poetry rank TBD
```

### Prov 14:12 — seems right → death (IF/THEN)

```text
### TREE  Prov.14.12  ·  force-prose DEBUG  ·  pure binary + glue
words=8 · bricks=3
en: "There is a way that seems right to a man, but its end is the ways of death."

PLAIN LOGIC
  A: EXISTS path · straight/right · before a man
  B: its end · ways of death
  Shape: appearance ‖ outcome

TOP-DOWN (provisional)
PHRASE  (8w · binary)
├── B0 [0–4] · GLUE  "there is a right-seeming way before a man"  ← etnachta
└── PHRASE  (3w · binary)
    ├── B1 [5] · ATOM  "and its end"
    └── B2 [6–7] · GLUE  "ways of death"                        ← silluq

TRACK CHECK
  ✓ etnachta cuts "seems right" from "death end"
  ✓ Easy golden candidate for poetry ranks later
```

### Prov 6:23 — lamp / light equations (+ our light theme)

```text
### TREE  Prov.6.23  ·  force-prose DEBUG  ·  pure binary + glue
words=9 · bricks=3
en: "For the commandment is a lamp and the teaching is light,
     and the way of life is the rebukes of discipline."

PLAIN LOGIC
  A: mitzvah = lamp  AND  torah = light     (equations; H216 light)
  B: way-of-life = rebukes of discipline
  Shape: identity block ‖ life-path block

TOP-DOWN (provisional)
PHRASE  (9w · binary)
├── B0 [0–4] · GLUE  "for lamp=commandment and torah=light"   ← etnachta on אוֹר
└── PHRASE  (4w · binary)
    ├── B1 [5–6] · GLUE  "and way of life"
    └── B2 [7–8] · GLUE  "rebukes of discipline"

TRACK CHECK
  ✓ Light noun sits at etnachta head of A — good for dual-rail with Gen light
  ✓ Right half is "way of life" package
```

### Ps 1:6 — two ways (psalm, still dual)

```text
### TREE  Ps.1.6  ·  force-prose DEBUG  ·  pure binary + glue
words=8 · bricks=3
en: "For the LORD knows the way of the righteous, but the way of the wicked will perish."

PLAIN LOGIC
  A: LORD knows · way of righteous
  B: way of wicked · perishes
  Shape: two ways (know ‖ perish)

TOP-DOWN (provisional)
PHRASE  (8w · binary)
├── B0 [0–4] · GLUE  "for LORD knows way of righteous"   ← etnachta
└── PHRASE  (3w · binary)
    ├── B1 [5] · ATOM  "and way of"
    └── B2 [6–7] · GLUE  "wicked will perish"
```

### Controls

| Ref | Role |
|-----|------|
| **Job 1:1** | Prose frame — deeper brick tree, tevir/tifcha/darga — parse with **prose v2** for real |
| **Job 3:3** | Poetry body — dehi/revia pattern like Prov; force-prose only provisional |
| **Ps 1:1** | Logic clear (3× NOT) but **mark-heavy** (zinor, ole, yerah) — second-wave poetry golden |

---

## 5. Experiment workflow (next steps)

| Step | Action | Success |
|------|--------|---------|
| **E1** | Freeze seed list above as poetry experiment corpus | Owner agrees |
| **E2** | For each Tier A verse: plain-logic card (A‖B / IF→THEN) | Human-readable |
| **E3** | Inventory poetry-only marks (dehi, ole, zinor, mugrash…) | Table for `ranks_poetry` |
| **E4** | Draft `ranks_poetry.yaml` hypothesis from secondary charts | Versioned, not CURRENT until green |
| **E5** | Goldens: Prov 3:5, 14:12, 6:23, 1:7, Ps 1:6 + Job 1:1 prose | Must match **logic split** + marks |
| **E6** | Only then flip system selector for Ps/Prov/Job body | No bulk Job speeches yet |

**Never:** treat force-prose trees as final poetry truth.

---

## 6. Confidence for this experiment

| Claim | Label |
|-------|--------|
| Prov duals are good logic trackers | **high** |
| Force-prose 3-brick shape often mirrors A‖B | **hypothesis** (useful, not proof) |
| dehi/ole need poetry ranks | **high** |
| Ready to implement full ranks_poetry | **medium** — after E3–E4 |

---

## 7. Bottom line

**Seed = mostly Proverbs dual/IF-THEN lines + Ps 1:6 + Job controls.**  
Logic is easy to track from English/Hebrew plain sense; force-prose already shows a recurring **A ‖ B** top split we can test against real poetry ranks next.

**Pick to implement first when you say go:** Prov **3:5**, **14:12**, **6:23** (and **Job 1:1** as prose control).
