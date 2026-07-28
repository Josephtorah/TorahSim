# Pre-Code Logic (`logic/`)

Canonical place to **derive Torah logic before code**.

| File | Purpose |
|------|---------|
| [TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md](TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md) | **Main tutorial (2026-07-20)** — full derive pipeline, show all work, Day 4 walkthrough |
| [TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md](TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md) | **Full-stack dev tutorial** — declare/use variables across books, leaf trees, Phase A/B (Exod→Lev 1) |
| [TUTORIAL_FIVE_BOOKS_INTERLOCK_FULLSTACK_2026-07-25.md](TUTORIAL_FIVE_BOOKS_INTERLOCK_FULLSTACK_2026-07-25.md) | **Five books as one system** — roles, exports/imports, concrete interlock chains (Gen→Deut) |
| [TUTORIAL_BEGINNERS.md](TUTORIAL_BEGINNERS.md) | Lev-oriented beginner path (Lev 12 purity) |
| [gen_boot/](gen_boot/INDEX.md) | **Genesis boot (1:1–2:3)** — plain leaf step-through + leaf derive + IR notes |
| [TAAMIM_TREE_PARSER.md](TAAMIM_TREE_PARSER.md) | **Our** versioned ta'amim → binary tree parser (rules + how to fix errors) |
| [**TREE_DISPLAY_LEAF_EN_HE_MORPH.md**](TREE_DISPLAY_LEAF_EN_HE_MORPH.md) | **ACTIVE** chat tree: `(en · he)` leaves + OSHB morph — Lev 1:2 |
| [**TREE_DISPLAY.md**](TREE_DISPLAY.md) | Display index (points to active format) |
| [Parse_tree_2026-07-27/](Parse_tree_2026-07-27/INDEX.md) | Taamim parse research + poetry checkpoint (points to TREE_DISPLAY) |
| [SHOW_WORK_TREES_2026-07-20.md](SHOW_WORK_TREES_2026-07-20.md) | **Where to record trees** — unit `binary_trees` + `tree_ascii` (show all work) |
| [TAAMIM_PARSE_NOTES.md](TAAMIM_PARSE_NOTES.md) | **Living notes** — update as we adjust parse understanding (glue vs nest, changelog) |
| [taamim_rules/](taamim_rules/) | Frozen rule versions (`CURRENT`, `v1/ranks_prose.yaml`, golden tests) |
| [lexicon/](lexicon/) | **Versioned gloss table** (EN-AID; hand entries override Strong's auto #IMPOSED) — regenerate via `artifacts/generate_lexicon_v1.py` |
| [role_rules/](role_rules/) | **Versioned leaf→role rules** (auto illustrative labels, not derivation) + goldens: `python3 logic/role_rules/check_golden.py` |
| [pre_logic_methods_2026-07-28/](pre_logic_methods_2026-07-28/INDEX.md) | Pre-code logic track: week experiment, tutorials, architecture plan (SQLite index: `build_db.py`) |
| [TREE_INTERPRETATION_RULES.md](TREE_INTERPRETATION_RULES.md) | Living catalog: consistent tree→logic rules; 100% word-use aspiration |
| [SYSTEM.md](SYSTEM.md) | Full method (formats, steps, comments, language policy) |
| [SCHEMA.yaml](SCHEMA.yaml) | Field definitions |
| [templates/unit_template.yaml](templates/unit_template.yaml) | Start a new unit here |
| [units/](units/) | Logic packages (one YAML per unit) |
| [units/gen_01_day4_lights.yaml](units/gen_01_day4_lights.yaml) | Genesis boot + full tree record (show-work reference) |
| [units/lev_12_childbirth.yaml](units/lev_12_childbirth.yaml) | Worked example (Leviticus 12 legal) |

**Source of truth:** Hebrew.  
**Accessibility (hard rule):** every Hebrew string needs **he + he_translit + en** (or inline `HE / translit / "English"`). Owner is English-fluent only.  
**Structure:** binary/ta'amim trees first (our parser under `taamim_rules/`) — **store under unit `binary_trees`** — then `tree_coverage`, then tables/FSM/boot rules.  
**Not for derivation:** inventing *legal* rules in Python — see root `AGENTS.md`. Structure rules are YAML under `taamim_rules/`; code only interprets them.  
**Worked examples:** `units/gen_01_day4_lights.yaml` (trees + boot) · `units/lev_12_childbirth.yaml` (legal)  
**Parse a verse:** `python3 taamim_tree_parse.py Lev.12.2` · **Tests:** `python3 taamim_tree_parse.py --test`
