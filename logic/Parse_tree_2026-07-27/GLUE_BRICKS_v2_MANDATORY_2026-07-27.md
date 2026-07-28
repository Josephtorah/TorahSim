# Glue bricks are mandatory (v2)

**Date:** 2026-07-27  
**Active rule set:** `v2` (`logic/taamim_rules/CURRENT`)  
**Kind:** design + implementation note · **not** binding law  

---

## Does OSHB show parsed trees?

**Partly, not as a full tree dump.**

| OSHB feature | What it is |
|--------------|------------|
| Word order in `<verse>` | Linear text |
| Ta’amim in word text | Marks we parse |
| **`n=` on some `<w>`** | Optional **path hint** for phrase hierarchy (e.g. `1`, `1.0`, `0.0`) — **not** present on every word; conjunctives often have `n` absent |
| Explicit nested XML tree | **No** standard full tree we rely on |

**Policy (project):** Our trees come from **marks + versioned rules**, not from treating OSHB `n=` as authority. `n=` may be compared later.

---

## Glue is required (not optional)

### Layer A — glue

Words with **conjunctive** (or zero/bind) marks stick to the next word until a **disjunctive** closes the unit.

```text
יְהִי (munach = glue) + אוֹר (etnachta = stop)
→ one terminal brick: «יהי אור»
```

### Layer B — nest

Continuous **binary** dichotomy runs on **bricks**, not on raw single words.

**Forbidden (v1 flattening):**  
a 4-ary phrase of four separate word-leaves for “and evening and morning…”

**Required (v2):**  
one GLUE leaf for that chain, then binary nest of bricks.

---

## Commands (always glue under CURRENT=v2)

```bash
python3 taamim_tree_parse.py --test
python3 taamim_tree_parse.py Gen.1.5 --tree --leaves
```

Tree display marks multi-word terminals as **`GLUE`** and ranges `[7-10]`.

---

## Files touched

| Path | Change |
|------|--------|
| `logic/taamim_rules/CURRENT` | → **v2** |
| `logic/taamim_rules/v2/ALGORITHM.md` | Glue then dichotomy |
| `logic/taamim_rules/v2/tests/golden.json` | Gen 1:1, 1:3, 1:5, Lev 12:2 + pure_binary |
| `taamim_tree_parse.py` | `glue_bricks`, binary-only nest, brick list in result |
| `logic/TAAMIM_PARSE_NOTES.md` | Changelog |

v1 kept for `--version v1` regression only.
