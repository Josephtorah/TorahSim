# Parse tree — ta’amim verification (2026-07-27)

**Folder:** `logic/Parse_tree_2026-07-27/`  
**Kind:** parser re-research + verification · **not** binding law  
**Rule set:** **`v3`** (`logic/taamim_rules/CURRENT`) — glue + **poetry seed**  
**Interpreter:** `taamim_tree_parse.py` (repo root)

---

## Start here

| Doc | Role |
|------|------|
| **[../TREE_DISPLAY.md](../TREE_DISPLAY.md)** | **PERMANENT** top-down B# GLUE\|ATOM English |
| **[../TREE_DISPLAY_LEAF_EN_HE_MORPH.md](../TREE_DISPLAY_LEAF_EN_HE_MORPH.md)** | **ACTIVE chat tree format:** `(en · he)` + morph tables · Lev 1:2 |
| **[REPORT_simple_leaf_en_he_oshb_morph_2026-07-27.md](REPORT_simple_leaf_en_he_oshb_morph_2026-07-27.md)** | Experiment report (same format; demos Gen + Lev) |
| **[DISPLAY_FORMAT.md](DISPLAY_FORMAT.md)** | Dated pointer → `TREE_DISPLAY.md` |
| **[../pre_logic_methods_2026-07-28/](../pre_logic_methods_2026-07-28/INDEX.md)** | **MOVED 2026-07-28:** FLAT/LEDGER/MORPH mockups, Gen 1:1–20 HTML run, generator script, pre-code logic experiment + tutorials now live in `logic/pre_logic_methods_2026-07-28/` |
| **[AUDIT_tree_parse_vs_scholarship_2026-07-27.md](AUDIT_tree_parse_vs_scholarship_2026-07-27.md)** | **Web/scholarship audit:** Wickes-aligned; gaps documented; no code change |
| **[RESEARCH_how_to_parse_poetry_teamin_2026-07-27.md](RESEARCH_how_to_parse_poetry_teamin_2026-07-27.md)** | **Poetry design:** separate ranks for the Three; Job frame exception; not Lowth |
| **[EXPERIMENT_poetry_logic_seed_2026-07-27.md](EXPERIMENT_poetry_logic_seed_2026-07-27.md)** | **Experiment:** Prov/Ps dual-logic seed |
| **[EXPERIMENT_poetry_v3_implemented_2026-07-27.md](EXPERIMENT_poetry_v3_implemented_2026-07-27.md)** | **v3 live:** ranks_poetry + goldens + samples |
| **[SMOKE_prov_v3_2026-07-27.md](SMOKE_prov_v3_2026-07-27.md)** | **Prov full-book smoke:** **915/915** unique · leaf · pure · poetry |
| **[DONE_poetry_checkpoint_2026-07-27.md](DONE_poetry_checkpoint_2026-07-27.md)** | **CLOSED:** display contract + Ps/Job/Prov smokes + units + TIR status |
| **Logic** `../units/prov_03_trust_know.yaml` | Poetry unit 1: Prov 3:5–6 (TIR-023/024) |
| **Logic** `../units/prov_14_way_death.yaml` | Poetry unit 2: 14:12 // 16:25 (**TIR-025 tested**) |
| **Logic** `../units/prov_15_soft_harsh.yaml` | Poetry unit 3: 15:1 soft‖harsh (**TIR-023 tested**) |
| **[GLUE_BRICKS_v2_MANDATORY_2026-07-27.md](GLUE_BRICKS_v2_MANDATORY_2026-07-27.md)** | **Glue required**; OSHB `n=` note; no flat trees |
| **[VERIFY_taamim_parse_to_leaves_2026-07-27.md](VERIFY_taamim_parse_to_leaves_2026-07-27.md)** | Earlier v1 full-Torah leaf audit (pre-glue) |
| `_torah_audit_summary.json` | v1 machine summary (5853 verses) |

## Canonical method (stable paths)

| Path | Role |
|------|------|
| `logic/TAAMIM_TREE_PARSER.md` | Method + versioning workflow |
| `logic/TAAMIM_PARSE_NOTES.md` | Living notes + changelog |
| `logic/taamim_rules/v1/ALGORITHM.md` | Exact split algorithm |
| `logic/taamim_rules/v1/ranks_prose.yaml` | Mark → rank |
| `logic/taamim_rules/v1/tests/golden.json` | Regression cases |
| `taamim_tree_parse.py` | Code (interprets rules only) |

## Commands

```bash
# golden tests
python3 taamim_tree_parse.py --test

# full tree (root → leaves)
python3 taamim_tree_parse.py Gen.1.3 --tree

# every leaf listed
python3 taamim_tree_parse.py Gen.1.3 --leaves

# both + JSON
python3 taamim_tree_parse.py Gen.1.3 --tree --leaves --json
```

## Result

- **v1:** full Torah leaf-complete (every word under the tree).  
- **v2:** same + **mandatory glue bricks** + **pure binary** nest (no flat n-ary word lists).  
- **v3 (CURRENT):** poetry ranks + system selector; goldens **23/23**.  
- **Smokes:** Prov **915/915**, Ps **2527/2527**, Job **1070/1070** (frame prose / body poetry).  
- Display: **permanent** top-down **B# GLUE\|ATOM** English → **`logic/TREE_DISPLAY.md`**.  
- **Checkpoint CLOSED:** `DONE_poetry_checkpoint_2026-07-27.md`.  
- **Full Tanakh parse deferred**.

**Last updated:** 2026-07-27 (poetry checkpoint **CLOSED**)
