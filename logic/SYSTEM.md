# Pre-Code Logic System (Torah derivation)

**Status:** Canonical method for deriving logic from Torah in this repo.  
**Role:** The logic layer **before** computer code.  
**Not for this stage:** Inventing rules in Python (or any programming language).

Python (or other code) may later **interpret** finished logic documents. It must **not** be where the rules are first discovered or written.

---

## 0. Reader profile (mandatory awareness)

- The project owner is **fluent in English only**, not Hebrew.
- Every logic unit **must** remain readable in English via comments, glosses, and translations.
- **Never bare Hebrew** anywhere in a unit file, template, or chat walkthrough:
  - Fields: always `he` + `he_translit` + `en` together.
  - Prose/comments: always `עברית / translit / "English"`.
  - Scenarios: `value_he` + `value_he_translit` + `value_en`.
  - Bound tree words: each entry is a full triple, not a bare string list.
- That accessibility layer does **not** change the source of truth:
  - **Canonical source = Hebrew text** (from `Data/*_he*` or other Hebrew primary sources).
  - **English = secondary**: labels, comments, free translations, debugging aids.
  - **Never** derive a condition, state, number, or outcome from English alone.
  - If Hebrew and English disagree, **Hebrew wins**; note the conflict in comments.

---

## 1. What this system is

A **human- and machine-readable specification** of Torah-derived logic:

| Layer | Purpose |
|-------|---------|
| **Hebrew source span** | Exact words / phrases the claim rests on |
| **Structure** | How the text is segmented (verse, clause, ta'amim, פ/ס, etc.) |
| **Logic objects** | Conditions, outcomes, states, transitions, decision rows |
| **Comments** | English explanations + Hebrew reminders + confidence + provenance |
| **Tests (scenarios)** | Cases stated against the logic doc—not against ad-hoc code |

```
Hebrew (_he)  →  structure notes  →  LOGIC DOCUMENT (this system)
                                         ↓
                              optional later: interpreter code
```

---

## 2. Common formats we use (pre-code)

Use one or more of these **inside** a logic document. Prefer the smallest set that fits the unit.

### 2.1 Decision table (casuistic / if–then cases)

Best for: parallel cases (male/female, clean/unclean, etc.).

| Row | WHEN (conditions from Hebrew) | THEN (outcomes from Hebrew) |
|-----|-------------------------------|-----------------------------|
| R1  | …                             | …                           |

### 2.2 Finite-state machine (status over events / time)

Best for: impurity periods, counting days, eligibility that changes.

- **States** — named statuses (Hebrew term + English gloss)
- **Events** — what can happen (birth, day-count complete, offering, …)
- **Transitions** — `from + event [+ guard] → to` with Hebrew provenance

### 2.3 Production rules (IF–THEN clauses)

Best for: sparse conditions, composed checks, optional Oral attachments.

```
RULE id:
  IF   <predicates grounded in Hebrew>
  THEN <effects grounded in Hebrew>
```

### 2.4 Binary / ta'amim parse trees (**required structure layer**)

Best for: answering *where does the IF sit?* and *which words form one phrase?*

Cantillation (ta'amim) builds a **hierarchical, often binary parse tree** per verse (disjunctives divide; conjunctives link). In this repo’s OSHB `Data/*.xml`, many words carry `n="a.b.c"` path addresses:

- Shorter `n` ≈ higher in the tree  
- Typical top split: `n="1"` (often etnachta / first-half head) vs `n="0"` (second-half / sof-pasuq side)  
- Words with **no** `n` are bound into a neighboring phrase  

**Primary trees:** build with **our** versioned parser (`taamim_tree_parse.py` + `logic/taamim_rules/`). OSHB `n=` is optional cross-check only.

**Rule:** Decision-table rows, boot steps, and FSM fields must **cite tree nodes** (or phrase leaves under those nodes). Do not invent IF/THEN from a flat English reading alone.

**Show all work (required):** store trees **inside the unit** under `binary_trees` — including `rule_set_version`, top split (he+translit+en), full `tree_ascii` from `--tree`, and `maps_to` logic ids. Do not leave structure only in chat or only as a re-runnable command.  
**Chat tree display (PERMANENT):** top-down **B# · GLUE|ATOM** with English brick glosses — **`logic/TREE_DISPLAY.md`** (not raw Hebrew-only CLI as primary).  
Procedure: `logic/SHOW_WORK_TREES_2026-07-20.md` · Standing default: `reviews/STANDING_DECISIONS.md` §6a.  
Reference: `logic/units/gen_01_day4_lights.yaml`. Also: `lev_12_childbirth.yaml`, `lev_01_call_and_korban_opening.yaml`.

**Long-term goal — consistent interpretation + 100% word use:**  
See `logic/TREE_INTERPRETATION_RULES.md`. We are building reusable **TIR-xxx** rules for how tree patterns map to logic roles. Aspiration: every word in every verse tree is **accounted for** (and increasingly logic-bearing) under an explicit rule. Early units will have gaps; record them and improve the catalog rather than inventing one-off mappings. Companion section: **`tree_coverage`** (leaf roles) — required alongside `binary_trees`, not instead of it.

### 2.5 Phrase map (flat leaves of the trees)

Best for: a searchable index of phrase roles  
(header / condition / consequence / reference / close).

Phrases should be **leaves or subtrees** of §2.4, not a replacement for the binary tree.

### 2.6 What we do *not* use as the derivation format

- Free Python / pseudocode as the **source of truth**
- English paraphrase as the **only** evidence for a rule
- Undocumented “the model implies…” without a Hebrew span

---

## 3. File layout

```
logic/
  SYSTEM.md                 ← this document (method)
  SCHEMA.yaml               ← field definitions
  units/                    ← one unit per derivation
    <book>_<ref>_<slug>.yaml
  templates/
    unit_template.yaml      ← copy to start a new unit
```

**Naming:** `lev_12_childbirth.yaml`, `num_27_daughters.yaml`, etc.

Each unit file is a complete **logic package** for one legal/narrative-procedure block.

---

## 4. Mandatory comment policy

Comments are **part of the method**, not optional polish.

### 4.1 Every logic atom must have

1. **`he`** — Hebrew text as it appears in the source span (or exact lemma if justified).
2. **`he_translit`** — **required** simple English-letter transliteration (owner is not fluent in Hebrew).
3. **`en`** — **required** plain English gloss / free translation of that span.
4. **`comment`** — why this atom exists, how it was read, what was *not* inferred (in English).
5. **`confidence`** — one of: `hypothesis` | `tested` | `failed` | `dead_end` | `established`.
6. **`source`** — citation: book, chapter:verse, and path under `Data/` when known.

**Never leave bare Hebrew.** In trees, tables, comments, and indexes, any Hebrew word or phrase must appear with transliteration and English in the same place (fields or inline `HE / translit / "English"`).

### 4.2 Comment language

- Write **`comment` fields in English** (primary language of the project owner).
- Embed Hebrew words in comments when useful, always with a gloss:
  - Example: `זָכָר (zakhar, “male”) triggers the shorter count.`
- When a translation is approximate, say so: `en_note: free translation; not a legal English ruling.`

### 4.3 “Do not invent” rule

If a field cannot point to a Hebrew span (or a **named** Oral source with location), leave it out or mark:

```yaml
status: not_in_written
confidence: hypothesis
comment: "Not stated in the Written span; held only as a question."
```

---

## 5. Derivation process (step by step)

Work these steps **in order**. Record each step in the unit file under `derivation_log`.

### Step A — Choose the unit

- Pick a self-contained block (e.g. Lev 12:1–8).
- Record: why this unit; Hebrew book name + English book name.

### Step B — Load Hebrew source only for derivation

- Open the **`_he`** text (or Hebrew XML / primary Hebrew).
- Optionally open `_en` **only** as a reading aid; do not copy English structure into rules.
- Comment any place the English translation might mislead.

### Step C — Segment structure (**binary tree first**)

1. Build **verse-level binary / ta'amim trees** (from OSHB `n=` paths and/or accent ranks).  
2. Optionally build a **chapter outline tree** of legal blocks.  
3. Then list a **phrase map** (flat leaves) with HE + EN.  
4. Only after that, extract WHEN/THEN.  

Comment: which boundaries are Masoretic (tree) vs analyst role-labels.  
**Do not skip the binary tree** for legal units — see Lev 12 unit.

### Step D — Extract candidate predicates & outcomes

From Hebrew phrases only:

- Conditions (WHEN)
- Outcomes (THEN)
- Durations / numbers (copy Hebrew number words; give English numeric gloss in comments)
- References (“as in …”) — keep as links, do not silently expand

### Step E — Choose logic format(s)

- Decision table and/or FSM and/or rules.
- Comment **why** that format fits this unit.

### Step F — Fill logic objects with bilingual fields

- Every row/transition/rule: HE source + EN gloss + comment + confidence + citation.

### Step G — Attach Oral material only with names (optional)

- Mishnah / Talmud / midrash only with **tractate + location**.
- Separate section: `oral_attachments` — never merge into Written rules without a flag.

### Step H — Scenarios (tests without code)

- List cases: inputs → expected outcomes, each justified by a rule id / transition id.
- English descriptions OK; the **expected values** must still match Hebrew-derived fields.

### Step I — Review for English leakage

Checklist (must pass):

- [ ] No condition exists only in English.
- [ ] All numbers/durations cite Hebrew.
- [ ] Comments explain Hebrew for an English-only reader.
- [ ] Confidence labels present.
- [ ] Conflicts HE vs EN noted if any.

### Step J — Freeze the logic document

- Mark `status: draft | review | frozen`.
- Only after **frozen** may optional interpreter code be written—and that code must **load** this document, not re-derive.

---

## 6. Provenance tags

Tag every claim:

| Tag | Meaning |
|-----|---------|
| `[HE-WRITTEN]` | From Written Torah Hebrew span |
| `[HE-STRUCT]` | From structure (ta'amim, פ/ס, verse break) |
| `[EN-AID]` | English used only as aid—not a source |
| `[ORAL:Name Loc]` | Named Oral source |
| `[INFER]` | Explicit inference; needs stronger justification |
| `[OPEN]` | Unresolved question |

---

## 7. Relationship to older tracks

| Artifact | Role now |
|----------|----------|
| `logic/SYSTEM.md` | **Global** method for Torah logic derivation |
| `artifacts/DERIVATION_METHOD.md` | **Historical/reference** Lev 12 experiment (Python-era) |
| `artifacts/lev12_*.py` / JSON | Recovered experiments—not the template for new derivation |

New work: prefer `logic/units/*.yaml` over new Python models.

---

## 8. Confidence & religious framing

- Prefer honest labels over false certainty.
- These documents are **experimental models**, not binding halakhic rulings, unless the user explicitly asks for that framing.

---

## 9. Quick start

1. Copy `logic/templates/unit_template.yaml` → `logic/units/<name>.yaml`.
2. Fill `meta`, then `derivation_log` steps A–I.
3. Fill `phrase_map`, then `decision_table` and/or `state_machine` and/or `rules`.
4. Add `scenarios` and run the English-leakage checklist.
5. Set `status: frozen` when stable.

For field definitions, see `logic/SCHEMA.yaml`.
