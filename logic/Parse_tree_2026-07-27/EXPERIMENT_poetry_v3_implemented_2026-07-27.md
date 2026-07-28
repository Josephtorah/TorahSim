# Poetry parse experiment — v3 implemented

**Date:** 2026-07-27  
**CURRENT:** `v3`  
**Status:** **checkpoint CLOSED** — see `DONE_poetry_checkpoint_2026-07-27.md`  
(goldens 23/23; Prov 915 + Ps 2527 + Job 1070 all ok_all)  

---

## What shipped

| Piece | Path / behavior |
|-------|-----------------|
| Poetry ranks | `logic/taamim_rules/v3/ranks_poetry.yaml` |
| Prose ranks | `logic/taamim_rules/v3/ranks_prose.yaml` (v2 glue rules) |
| Algorithm | `logic/taamim_rules/v3/ALGORITHM.md` |
| System select | Ps, Prov → poetry; Job 1–2, 42 → prose; Job 3–41 → poetry |
| CLI | default auto; `--force-prose` / `--force-poetry` |
| Goldens | **23/23** pass (`python3 taamim_tree_parse.py --test`) |
| Prov smoke | **915/915** unique · leaf · pure · poetry — `SMOKE_prov_v3_2026-07-27.md` |

### Critical poetry rank differences (vs prose)

| Mark | Prose v2 | Poetry v3 seed |
|------|----------|----------------|
| **dehi** | conjunctive | **disjunctive rank 2** |
| **ole** | conjunctive | **disjunctive rank 1** |
| **zinor** | disjunctive 3 | disjunctive **2** |

That lets dual proverbs split **trust in YHWH** as its own brick before etnachta — better logic track.

---

## Goldens (logic-friendly seed)

### Batch 0 (initial seed)

| Verse | System | Logic track | bricks |
|-------|--------|-------------|--------|
| Gen 1:3 | prose | create light control | 3 |
| Job 1:1 | **prose** | frame control | 7 |
| Prov 3:5 | poetry | trust ‖ do not lean | 4 |
| Prov 14:12 | poetry | seems right → death | 4 |
| Prov 6:23 | poetry | lamp/light equations | 4 |
| Prov 1:7 | poetry | fear/knowledge ‖ fools | 4 |
| Ps 1:6 | poetry | two ways | 4 |
| Job 3:3 | poetry | body control | 4 |

### Batch 1 (next — hard marks + duals)

All **unique · poetry · pure_binary · leaf_complete**.

| Verse | bricks | Logic track / hard marks |
|-------|--------|--------------------------|
| **Ps 1:1** | 7 | ole + zinor; 3× NOT ladder (walk / stand / sit) |
| **Ps 1:2** | 4 | torah delight ‖ meditate day/night |
| **Prov 10:1** | 6 | title (ole) ‖ wise son ‖ foolish son |
| **Prov 3:6** | 3 | know in ways → he straightens (follow 3:5) |
| **Prov 4:18** | 4 | path of righteous ‖ light going to day |
| **Prov 11:1** | 4 | false scales abom ‖ just weight delight |
| **Prov 15:1** | 4 | soft answer ‖ harsh word |
| **Prov 16:25** | 4 | // 14:12 IF→THEN (same bracket shape) |
| **Prov 22:6** | 4 | train child ‖ when old will not turn |
| **Job 3.4** | 5 | day be darkness (ole; continue 3:3) |
| **Prov 8:1** | 3 | does not wisdom call ‖ understanding raise voice |

**Bracket locks (plain he, no niqqud/taamim):**

| Verse | `expect_bracket_plain` |
|-------|------------------------|
| Ps.1.1 | `[[[אשרי ה/איש אשר לא הלך] ב/עצת רשעים] [[ו/ב/דרך חטאים לא עמד] [ו/ב/מושב לצים לא ישב]]]` |
| Ps.1.2 | `[[כי אם ב/תורת יהוה חפצ/ו] [ו/ב/תורת/ו יהגה יומם ו/לילה]]` |
| Prov.10.1 | `[[משלי שלמה] [[בן חכם ישמח אב] [ו/בן כסיל תוגת אמ/ו]]]` |
| Prov.3.6 | `[ב/כל דרכי/ך דע/הו [ו/הוא יישר ארחתי/ך]]` |
| Prov.4.18 | `[[ו/ארח צדיקים כ/אור נגה] [הולך ו/אור עד נכון ה/יום]]` |
| Prov.11.1 | `[[מאזני מרמה תועבת יהוה] [ו/אבן שלמה רצונ/ו]]` |
| Prov.15.1 | `[[מענה רך ישיב חמה] [ו/דבר עצב יעלה אף]]` |
| Prov.16.25 | `[[יש דרך ישר ל/פני איש] [ו/אחרית/ה דרכי מות]]` |
| Prov.22.6 | `[[חנך ל/נער על פי דרכ/ו] [גם כי יזקין לא יסור ממ/נה]]` |
| Job.3.4 | `[[ה/יום ה/הוא יהי] [חשך אל ידרש/הו אלוה מ/מעל [ו/אל תופע עלי/ו נהרה]]]` |
| Prov.8.1 | `[ה/לא חכמה תקרא [ו/תבונה תתן קול/ה]]` |

### Batch 2 (smoke structural outliers)

| Verse | bricks | Role |
|-------|--------|------|
| Prov.2.4 | 2 | Minimal dual |
| Prov.1.22 | 7 | zinor+ole nest |
| Prov.24.12 | 9 | Max bricks in Prov |
| Prov.30.4 | 7 | Long pazer ladder |

See **`SMOKE_prov_v3_2026-07-27.md`** for full-book metrics (brick hist: 4-brick modal ~66%).

---

## Top-down samples (standard display)

### Prov.3.5

```text
### TREE  Prov.3.5  ·  taamim v3 poetry  ·  pure binary + glue
words=9 · bricks=4 · leaf_complete=yes · pure_binary=yes
en: "Trust in the LORD with all your heart, and do not lean on your own understanding."

PHRASE  (9w · binary)
├── PHRASE  (5w · binary)
│   ├── B0 [0–2] · GLUE  "trust to the LORD"
│   └── B1 [3–4] · GLUE  "with all your heart"
└── PHRASE  (4w · binary)
    ├── B2 [5–6] · GLUE  "and on your understanding"
    └── B3 [7–8] · GLUE  "do not lean"
```

### Prov.14.12

```text
### TREE  Prov.14.12  ·  taamim v3 poetry  ·  pure binary + glue
words=8 · bricks=4
en: "There is a way that seems right to a man, but its end is the ways of death."

PHRASE  (8w · binary)
├── PHRASE  (5w · binary)
│   ├── B0 [0–2] · GLUE  "there is a right way"
│   └── B1 [3–4] · GLUE  "before a man"
└── PHRASE  (3w · binary)
    ├── B2 [5] · ATOM  "and its end"
    └── B3 [6–7] · GLUE  "ways of death"
```

### Ps.1.1 (batch 1 hard marks)

```text
### TREE  Ps.1.1  ·  taamim v3 poetry  ·  pure binary + glue
words=15 · bricks=7
en: "Happy is the man who has not walked… stood… sat…"

PHRASE  (15w · binary)
├── PHRASE  (7w · binary)
│   ├── PHRASE  (5w · binary)
│   │   ├── B0  "happy the man"
│   │   └── B1  "who has not walked"   ← zinor
│   └── B2  "in counsel of wicked"     ← ole
└── PHRASE  (8w · binary)
    ├── PHRASE  (4w · binary)
    │   ├── B3  "and in way of sinners"
    │   └── B4  "has not stood"        ← etnachta
    └── PHRASE  (4w · binary)
        ├── B5  "and in seat of scorners"
        └── B6  "has not sat"          ← silluq
```

### Prov.10.1 (title + dual sons)

```text
### TREE  Prov.10.1  ·  taamim v3 poetry
words=10 · bricks=6

PHRASE  (10w · binary)
├── PHRASE  (2w · binary)  title
│   ├── B0  "proverbs of"
│   └── B1  "Solomon"                  ← ole
└── PHRASE  (8w · binary)
    ├── PHRASE  (4w · binary)
    │   ├── B2  "wise son"
    │   └── B3  "gladdens a father"    ← etnachta
    └── PHRASE  (4w · binary)
        ├── B4  "and foolish son"
        └── B5  "grief of his mother"  ← silluq
```

### Prov.16.25 (// 14:12)

```text
### TREE  Prov.16.25  ·  same dual shape as Prov.14.12
words=8 · bricks=4
bracket: [[יש דרך ישר ל/פני איש] [ו/אחרית/ה דרכי מות]]
```

### Job.3.4 (body + ole)

```text
### TREE  Job.3.4  ·  poetry body
words=12 · bricks=5

PHRASE  (12w · binary)
├── PHRASE  (3w · binary)
│   ├── B0  "that day"
│   └── B1  "let it be"                ← ole
└── PHRASE  (9w · binary)
    ├── B2  "darkness… God from above" ← etnachta brick
    └── PHRASE  (4w · binary)
        ├── B3  "and let not shine"
        └── B4  "upon it light"
```

---

## Commands

```bash
python3 taamim_tree_parse.py --test
python3 taamim_tree_parse.py Prov.3.5 --tree --leaves
python3 taamim_tree_parse.py Ps.1.1 --tree
python3 taamim_tree_parse.py Prov.10.1 --tree
python3 taamim_tree_parse.py Job.1.1 --tree   # prose frame
python3 taamim_tree_parse.py Job.3.3 --tree   # poetry body
```

---

## Confidence

| Claim | Label |
|-------|--------|
| Seed duals parse unique + pure binary | **tested** (23 goldens) |
| **All of Proverbs** unique + leaf + pure + poetry | **tested** (915/915) |
| dehi-as-disjunctive improves A‖B split | **strong hypothesis** (mass-stable) |
| ole / zinor as poetry disjunctives | **tested** goldens + Prov mass no blow-ups |
| Prov 16:25 tree matches 14:12 shape | **tested** (same bracket plain) |
| Full Wickes poetry fidelity | **not claimed** |
| Ready for all Psalms / all Job speeches | **structure likely**; smoke not yet run |

---

## Logic units (poetry seed)

| Unit | Path | Scope | TIR |
|------|------|--------|-----|
| **prov_03_trust_know** | `logic/units/prov_03_trust_know.yaml` | Prov 3:5–6 dual + know→straighten | 023 tested; 024 hypothesis |
| **prov_14_way_death** | `logic/units/prov_14_way_death.yaml` | Prov 14:12 // 16:25 path→end death | **025 tested** |
| **prov_15_soft_harsh** | `logic/units/prov_15_soft_harsh.yaml` | Prov 15:1 soft ‖ harsh | **023 tested** |

## Smokes (closure)

| Book | ok_all |
|------|--------|
| Prov | 915/915 |
| Ps | 2527/2527 |
| Job | 1070/1070 (frame 52 prose; body 1018 poetry) |

## Next

- **None required for this checkpoint** (CLOSED).  
- Future: promote TIR-024; freeze units; full Tanakh only if owner asks.  
