# Ta'amim parse notes (living doc)

**Purpose:** Working notes on **how we parse verse trees from ta'amim**.  
Update this file whenever we learn a correction, edge case, or policy change.

**Related (do not duplicate long specs here):**

| Doc / path | Role |
|------------|------|
| `logic/TAAMIM_TREE_PARSER.md` | Method: versioned rules, golden tests, error workflow |
| `logic/taamim_rules/CURRENT` | Active rule version id |
| `logic/taamim_rules/vN/` | Frozen ranks + algorithm for that version |
| `taamim_tree_parse.py` | Interpreter of the active version |
| `logic/TREE_INTERPRETATION_RULES.md` | Tree → **logic** (IF/THEN); different layer |

**Owner language:** English-fluent only. When citing Hebrew: `עברית / translit / "English gloss"`.

---

## Current understanding (update when wrong)

### Two layers (classical continuous dichotomy)

1. **Glue layer (conjunctives + zero marks)**  
   - A conjunctive means: this word is chanted/read **with** what follows (no structural break).  
   - Zero / unmarked (e.g. some OSHB splits) also **bind** to the next marked word.  
   - Glue until a **disjunctive**.  
   - Result = **terminal unit** (leaf of the dichotomy):  
     - one word that already has a disjunctive, **or**  
     - **several words** ending in a disjunctive (word combo leaf).

2. **Nest layer (disjunctives)**  
   - Disjunctive ranks (etnachta, zaqef, tifcha, silluq, …) **split** the verse.  
   - **Binary continuous dichotomy (Wickes-style):** keep dividing a span into **two** sides by accent strength, then divide each side again, until you reach those **terminal units**.  
   - The tree **nests units**, not “every raw word always as its own leaf.”

**One line:** Conjunctives build multi-word bricks; disjunctives build the tree out of those bricks.

### What “binary continuous dichotomy” means (plain)

| Term | Meaning |
|------|---------|
| **Binary** | Each structural split has two children (left / right). |
| **Continuous** | The same divide-again rule applies inside each half, repeatedly. |
| **Dichotomy** | Division into parts by ranked disjunctives. |
| **Wickes-style** | Classical accent-rank dichotomy tradition (not our invention). |

### What we are **not** doing at this layer

- Not IF/THEN legal logic (that is Pre-Code Logic + TIR).  
- Not English-driven splits.  
- Not silent per-verse hacks in code — change **rules** + **version** + note here.

---

## Implementation status

| Item | Status | Notes |
|------|--------|--------|
| Rule versioning (`taamim_rules/vN`) | **yes** | `CURRENT` → active version |
| Golden regression tests | **yes** | `v1/tests/golden.json` |
| Glue → multi-word terminal units | **yes (v2, mandatory)** | Conjunctives/zero glue until disjunctive; dichotomy on bricks only |
| Dichotomy on units (not raw words only) | **yes (v2)** | Pure binary nest of glue bricks; no flat n-ary word lists |
| Poetry system (Psalms, Proverbs, Job) | **checkpoint CLOSED (v3)** | Prov 915 + Ps 2527 + Job 1070 all ok; 23 goldens; `DONE_poetry_checkpoint_2026-07-27.md` |
| Multi-parse report (Wu/Lowery-style) | **not yet** | v1 always unique or fail |
| OSHB `n=` as authority | **no** | Optional comparison only; our trees come from marks + our rules |

**Active implementation:** see `logic/taamim_rules/CURRENT` and that version’s `ALGORITHM.md`.

---

## Open questions

- Exact policy when **two disjunctives** share the same rank in one span (leftmost vs rightmost continuous dichotomy detail).  
- How to treat **double marks** on one word beyond “strongest disjunctive wins.”  
- Poetry ranks table (separate from prose).  
- Whether maqqef-joined forms in the scroll vs OSHB `<w>` splits should always match terminal units.  
- How closely to mirror Wu & Lowery CFG vs Wickes binary-only.

Log resolutions below under **Changelog**, then encode in a new `taamim_rules/vN`.

---

## How to update this doc

When you find an adjustment:

1. **Write it here first** (Changelog + change “Current understanding” if needed).  
2. If it changes behavior: copy `taamim_rules/vN` → `vN+1`, edit ranks/algorithm, point `CURRENT`, add golden test.  
3. Run `python3 taamim_tree_parse.py --test`.  
4. Note the new version in the Changelog row.

Do **not** fix one verse only in `taamim_tree_parse.py`.

---

## Changelog

| Date | Note | Rules version |
|------|------|----------------|
| 2026-07-27 | **Full Torah re-verify:** 5853/5853 unique + leaf-complete under v1. ElementTree word load; `leaf_complete` / `leaf_indices` on parse result; `--leaves` CLI; golden + Gen.1.3. Report: `logic/Parse_tree_2026-07-27/`. No algorithm change → still **v1**. | v1 |
| 2026-07-27 | **v2 mandatory glue bricks:** CURRENT→v2. Layer A glue → terminal multi-word leaves; Layer B pure binary dichotomy on bricks. No flat n-ary conj chains. Goldens Gen.1.1/1.3/1.5/Lev.12.2. See `Parse_tree_2026-07-27/GLUE_BRICKS_v2_MANDATORY_2026-07-27.md`. | **v2** |
| 2026-07-27 | **Display locked:** top-down ASCII only (`Parse_tree_2026-07-27/DISPLAY_FORMAT.md`) unless owner overrides. | v2 |
| 2026-07-27 | **Display made PERMANENT:** `logic/TREE_DISPLAY.md` = top-down **B# · GLUE\|ATOM** + English brick glosses (not raw CLI as chat primary). Wired into Agents + STANDING + all memory files. | v3 |
| 2026-07-27 | **Chat tree format (owner):** `(en · he)` leaf line + per-word OSHB morph tables. Spec: `logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md` (Lev 1:2 canonical). Agents + STANDING §6 updated. | v3 |
| 2026-07-27 | **v3 poetry seed:** CURRENT→v3. `ranks_poetry.yaml` (dehi/ole/zinor disjunctive); system selector + Job frame; goldens Prov 3:5/14:12/6:23/1:7, Ps 1:6, Job 1:1 prose, Job 3:3 poetry. Hypothesis ranks — expand via goldens. | **v3** |
| 2026-07-27 | **v3 golden batch 1:** Ps 1:1 (ole+zinor, 7 bricks), Ps 1:2, Prov 10:1 (title+dual sons), 3:6, 4:18, 11:1, 15:1, 16:25 (//14:12), 22:6, Job 3:4, Prov 8:1. **19/19** pass. No rank change. Doc: `EXPERIMENT_poetry_v3_implemented_2026-07-27.md`. | **v3** |
| 2026-07-27 | **Prov full-book smoke:** 915/915 unique + leaf_complete + pure_binary + system=poetry. Brick hist modal 4 (600). Outlier goldens Prov 2:4 (2), 1:22 (7), 24:12 (9), 30:4 (7) → **23/23**. Report: `SMOKE_prov_v3_2026-07-27.md`. No rank change. | **v3** |
| 2026-07-27 | **First poetry logic unit:** `logic/units/prov_03_trust_know.yaml` (Prov 3:5–6). Trees v3; dual TIR-023 + command→result TIR-024 seed in `TREE_INTERPRETATION_RULES.md`. No parser change. | **v3** |
| 2026-07-27 | **Second poetry logic unit:** `logic/units/prov_14_way_death.yaml` (14:12 // 16:25, identical brackets). TIR-025 path→end **tested**. // share one rule. No parser change. | **v3** |
| 2026-07-27 | **Closure pack:** Ps **2527/2527**, Job **1070/1070** (frame 52 prose / body 1018 poetry). Unit `prov_15_soft_harsh` → TIR-023 **tested**. DONE note + display contract. | **v3** |
| 2026-07-17 | Doc created. Classical model: conjunctives glue multi-word terminals; disjunctives nest those units (Wickes-style continuous dichotomy). v1 gap: still one leaf per word — plan multi-word terminals in v2. | v1 |

---

## Scratch / examples (append freely)

### Target shape (illustration, not frozen test)

Idea for a verse with munach + etnachta:

```
raw words:   …  X(munach)  Y(etnachta)  …
terminal:    …  [X Y]  …     ← multi-word leaf
tree:        dichotomy over terminals only
```

### v1 actual shape (current code)

```
raw words:   …  X  Y  …
leaves:      …  X, Y  …     ← two leaves
phrase:      [X Y] as parent of two one-word leaves
```

When v2 lands, replace this subsection with a real Lev example from golden tests.
