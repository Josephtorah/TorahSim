# Ta'amim tree parser (rule-based, versioned)

**Goal:** Build **our own** verse trees from Hebrew **ta'amim** (cantillation marks) with **one frozen rule set at a time**, applied the same way to every verse.

**Not the same as:** Pre-Code Logic (`logic/units/`) — that turns trees into IF/THEN.  
**This layer:** marks → binary phrase tree only.

**Living notes (adjustments as we learn):** `logic/TAAMIM_PARSE_NOTES.md` — update that doc first when understanding changes; then bump `taamim_rules/vN` if behavior changes.

**Not the same as:** inventing legal rules in Python. This code only **interprets** the versioned rule files under `logic/taamim_rules/`.

---

## Principles

1. **Hebrew marks are the input** — OSHB `Data/*.xml` word text (consonants + nikkud + ta'amim). English never decides splits.
2. **Rules are data** — ranks + algorithm live under `logic/taamim_rules/vN/`. Parser code loads the active version.
3. **Same rules every verse** — no per-chapter special cases outside the rule file (prose vs poetry is a named system switch).
4. **No guessing** — if a verse cannot be parsed uniquely under the rules, emit `status: multi` or `status: fail` with details. Never invent a silent winner.
5. **Errors fix the rules, not one verse** — when a tree is wrong:
   - add a golden regression case
   - change the rule file
   - **bump version** (`v1` → `v2`)
   - re-run all golden tests + reparse
6. **OSHB `n=` is optional check only** — not the authority for *our* trees. Optional `--compare-oshb` may report diffs.

---

## Layout

| Path | Role |
|------|------|
| `logic/TAAMIM_TREE_PARSER.md` | This method doc |
| `logic/taamim_rules/CURRENT` | Active version id (e.g. `v1`) |
| `logic/taamim_rules/v1/` | Frozen rule package |
| `logic/taamim_rules/v1/ranks_prose.yaml` | Mark → rank (prose books) |
| `logic/taamim_rules/v1/ALGORITHM.md` | Exact split algorithm for v1 |
| `logic/taamim_rules/v1/tests/golden.json` | Regression cases |
| `taamim_tree_parse.py` | Interpreter (repo root) |

---

## Workflow when you find an error

```
1. Capture the verse + wrong tree + expected tree (English comments OK).
2. Add/update golden test under logic/taamim_rules/vN/tests/.
3. Edit ranks or ALGORITHM only inside a NEW version directory (copy vN → vN+1).
4. Point logic/taamim_rules/CURRENT at vN+1.
5. Run: python3 taamim_tree_parse.py --test
6. Reparse any units that depended on the old version; record rule_set_version on trees.
```

Do **not** patch a single verse in code with `if verse == ...`.

---

## Output contract

Every parse returns:

- `rule_set_version` — e.g. `v1`
- `system` — `prose` | `poetry`
- `status` — `unique` | `multi` | `fail`
- `tree` — nested nodes (words + phrases)
- `words` — ordered list with mark name/rank (for 100% accounting later)
- `notes` — empty or error/multi details

Logic units **must** store trees under **`binary_trees`** with at least:

- `rule_set_version` (e.g. `v1`)
- per verse: `parser_status`, `pure_binary`, `linear` (he + he_translit + en), `top_binary_split`, **`tree_ascii`** (output of `--tree`), `maps_to` (logic step/rule ids)
- **Chat display (PERMANENT):** top-down **B# · GLUE|ATOM** English — `logic/TREE_DISPLAY.md` (CLI `--tree` is machine/unit snapshot, not the primary chat view)

**Show all work:** do not leave trees only in chat. Full procedure: `logic/SHOW_WORK_TREES_2026-07-20.md`. Standing: `reviews/STANDING_DECISIONS.md` §6a. Reference unit: `logic/units/gen_01_day4_lights.yaml`.

---

## Relation to Pre-Code Logic

```
Hebrew + ta'amim  →  [this parser]  →  binary tree
                          ↓
              logic/units/*.yaml (phrase_map, decision_table, TIR, …)
```

Tree **interpretation** rules remain in `TREE_INTERPRETATION_RULES.md` (TIR-xxx).
