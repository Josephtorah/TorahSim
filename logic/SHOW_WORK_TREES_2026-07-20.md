# Show all work: where ta'amim trees live

**Date:** 2026-07-20  
**Status:** standing procedure (not binding religious law)  
**Audience:** next thread / any agent deriving a logic unit  

On substantive update: rename to today’s date and fix links.

---

## One-sentence rule

**Every logic unit must record full ta'amim trees under `binary_trees` in that unit’s YAML, plus `tree_coverage` for every leaf — do not leave trees only in chat or only as a re-runnable command.**

**Display when showing a tree (ACTIVE):** chat = **`(en · he)` leaf line + OSHB morph tables** — **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`** (Lev 1:2 example). Unit field `tree_ascii` may still store machine CLI `--tree` for show-work.

---

## Where things go

| What | Where | Required? |
|------|--------|-----------|
| **Ta'amim / phrase trees** (structure) | `logic/units/<id>.yaml` → **`binary_trees`** | **Yes** |
| **Every word’s role** (interpretation) | same unit → **`tree_coverage`** | **Yes** (aspire 100%) |
| Boot steps / decision tables / FSM | same unit | Yes (genre-appropriate) |
| Parser rules (ranks, algorithm) | `logic/taamim_rules/vN/` | When fixing parser |
| Parser learning notes | `logic/TAAMIM_PARSE_NOTES.md` | When understanding changes |
| Cross-unit TIR catalog | `logic/TREE_INTERPRETATION_RULES.md` | When adding reusable roles |
| Agent defaults | `reviews/STANDING_DECISIONS.md` §6 | Keep in sync |

**Not enough alone:**

- Only running `python3 taamim_tree_parse.py Book.Ch.V --tree` in chat  
- Only English paraphrase of structure  
- Only `tree_coverage` without `binary_trees` (day 2–3 gap; day 4 fixed 2026-07-20)

**Regenerate anytime** with the parser; the unit still stores the **snapshot used for derivation** (`rule_set_version` required).

---

## Required shape of `binary_trees`

```yaml
binary_trees:
  rule_set_version: "v1"          # REQUIRED — which taamim_rules version
  parser: "taamim_tree_parse.py"
  data_source: "Data/....xml"
  method_note_en: "..."
  tags: ["[HE-STRUCT]"]
  verse_trees:
    Book_Ch_V:
      verse: "..."
      osis_id: "Book.Ch.V"
      parser_status: unique       # unique | multi | fail
      pure_binary: true|false     # false if any n-ary node n≠2
      word_count: N
      linear:
        he: "..."
        he_translit: "..."
        en: "..."                 # free gloss [EN-AID]
      top_binary_split:
        comment: "English: what left vs right means for logic"
        left_half:
          phrase: { he, he_translit, en }
        right_half:
          phrase: { he, he_translit, en }
      tree_ascii: |               # full ASCII from --tree (show work)
        PHRASE ...
      maps_to: [STEP_or_RULE_ids]
      confidence: tested
      source: "[HE-STRUCT][HE-WRITTEN]"
```

**Language:** never bare Hebrew — every stored Hebrew span has `he` + `he_translit` + `en`.

**Worked examples:**

- Genesis day 4 (full `tree_ascii` + maps): `logic/units/gen_01_day4_lights.yaml`  
- Lev opening (top splits + maps): `logic/units/lev_01_call_and_korban_opening.yaml`  
- Lev 12 (dense nested trees): `logic/units/lev_12_childbirth.yaml`  
- Gen day 1 (summaries + role_map): `logic/units/gen_01_creation_boot.yaml`

---

## Companion: `tree_coverage`

After trees exist, assign **every leaf**:

- `index`, `he`, `he_translit`, `en`, `role`, `kind` (`logic_bearing` | `glue`)  
- optional `feeds: [STEP_…]`  
- optional TIR id when using `TREE_INTERPRETATION_RULES.md`

See `logic/TREE_INTERPRETATION_RULES.md` § per-unit requirement.

---

## Derivation order (do not skip)

```text
1. Hebrew source (Data/* XML / _he)
2. Parse each verse → binary_trees (record in unit)
3. tree_coverage (100% leaves)
4. phrase_map / boot_steps / decision_table / FSM (cite tree nodes)
5. Optional Oral dual-track (named only)
6. Scenarios
```

Parser command:

```bash
python3 taamim_tree_parse.py Gen.1.14 --tree
python3 taamim_tree_parse.py Gen.1.14 --json
python3 taamim_tree_parse.py --test
```

---

## Backlog (known gaps)

| Unit | Trees status (as of 2026-07-20) |
|------|----------------------------------|
| `gen_01_creation_boot` | has `binary_trees` (summary style; may thicken ASCII later) |
| `gen_01_day2_raqia` | **needs** full `binary_trees` + `tree_ascii` backfill |
| `gen_01_day3_land_plants` | **needs** full `binary_trees` + `tree_ascii` backfill |
| `gen_01_day4_lights` | **done** (show-work reference) |
| `gen_01_day5_sea_birds` | **done** (1:20–23) |
| `gen_01_day6_land_human` | **done** (1:24–31; 149 words) |
| `gen_01_day7_shabbat` | **done** (2:1–3; closes week) |
| `lev_01_*`, `lev_12_*` | have `binary_trees` (patterns vary) |

When touching day 2 or day 3, backfill `binary_trees` to match day 4.

---

## Related docs

- `reviews/STANDING_DECISIONS.md` §6 (agent-owned default)  
- `logic/SYSTEM.md` §2.4  
- `logic/TAAMIM_TREE_PARSER.md`  
- `logic/templates/unit_template.yaml`  
- `reviews/GENESIS_BUILD_2026-07-20.md`
