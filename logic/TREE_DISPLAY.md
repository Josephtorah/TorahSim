# Tree display — index (memory)

**Primary chat/report format (owner 2026-07-27):**  
→ **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`**

That format is:

1. **`en+he` one line:** `(english · עברית) (next · עברית) … ‖ …`  
2. **Each leaf Bn** with a table: Word (English) | Role (glue/HEAD) | Morphology (English)  
3. **OSHB morph per word** inside multi-word leaves  
4. English-first; Hebrew paired; not bare Hebrew  

**Canonical worked example:** Leviticus 1:2 (in that file).

| Other | Role |
|-------|------|
| CLI `taamim_tree_parse.py --tree` | Debug / unit `tree_ascii` snapshot only |
| `web/taamim_tree/` | Optional D3 webapp experiment |
| ASCII `├──` pyramid nests | Not preferred for chat; owner rejected cluttered art |

**Do not re-quiz.** Update `TREE_DISPLAY_LEAF_EN_HE_MORPH.md` + Agents + STANDING when the owner changes the format.

**Authority:** `Agents.md` · `reviews/STANDING_DECISIONS.md` §6 · this index · the leaf-en-he-morph spec.
