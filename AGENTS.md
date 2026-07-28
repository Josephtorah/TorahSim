# Torah_Grok

This repo contains Torah and Jewish text data (JSON files under `Data/`) and experimental analysis of structure, systems, and models.

## Rules
- **Research placement:** **Never store research in the repo top folder.** Create or use a **topic subfolder** (usually `reviews/<topic>/` with `INDEX.md`). Examples: `reviews/br_link_studies/`, `reviews/sanctuary_spine_v1/`. Pre-Code units stay under `logic/units/`. See `reviews/STANDING_DECISIONS.md` §0a.
- **Dated filenames (from 2026-07-19):** research reports, notes, discoveries, and built indexes we own use a `_YYYY-MM-DD` suffix (e.g. `REPORT_<topic>_YYYY-MM-DD.md`, `DISCOVERIES_2026-07-19.md`, `cite_index_2026-07-18.json`). **On substantive update, rename the file so the date becomes today’s date**, and fix links. Hub exceptions with stable names only: `README.md`, `Agents.md`/`AGENTS.md`, `reviews/STANDING_DECISIONS.md` (still set **Last updated** in body). Not for `Data/` source. See `reviews/STANDING_DECISIONS.md` §0.
- **Possible Oral (Mesorat haShas):** Do **not** rule out any MH reference. Every MH endpoint is **possible Oral**; job preference only chooses what to open first. Research: `reviews/RESEARCH_valid_oral_torah_2026-07-19.md` (§6). `STANDING_DECISIONS` §5.
- Treat `Data/` as source data — do not modify JSON files unless explicitly asked.
- Prefer Python scripts in the repo root for processing/analysis (or under `artifacts/` for recovered models). **Exception:** for **deriving logic from Torah**, do **not** use Python (or other code) as the place rules are invented—use the Pre-Code Logic System under `logic/` (see below). Code may only **interpret** frozen logic documents later.
- Ask before large refactors or bulk file changes.
- Hebrew text files use `_he` suffix; English use `_en`.
- **Always derive logic from Hebrew.** Never use English as the source text for models, parsers, rules, or logic. English (`_en` files, translations, glosses) may be used only as secondary aids (labels, debugging, comparison, accessibility)—never as the canonical input for derivation.
- **Owner language:** the project owner is **fluent in English only, not Hebrew**. All logic documents must include Hebrew **and** English (glosses, free translations, and comments) so every step is readable in English, while Hebrew remains the sole derivation source.
- **Never bare Hebrew.** Every Hebrew string in logic work must appear with **transliteration + English** in the same place:
  - Structured fields: `he` + `he_translit` + `en` (required, not optional).
  - Comments / prose: inline form `עברית / translit / "English gloss"`.
  - Applies to binary trees, phrase maps, decision tables, FSMs, rules, Oral notes, scenarios, and chat explanations.
- Keep an **open mind**: multiple methods are welcome (ta'amim trees, shape/zero-knowledge scans, keyword maps, FSMs, comparative corpora, historical discovery notes, etc.). Do not treat one derivation style as the only valid approach for the whole project—except that **Torah rule derivation** uses the Pre-Code Logic System rather than inventing rules in code.
- Prefer labeling confidence (hypothesis / tested / failed / dead end) over silencing exploration.
- Do not present experimental models as binding religious law unless the user explicitly asks for that framing.

## Pre-Code Logic System (canonical for Torah derivation)

**Use this instead of Python for deriving logic out of the Torah.**

| Path | Role |
|------|------|
| `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md` | **Long tutorial** — full derive pipeline, show all work, Gen day 4 walkthrough |
| `logic/TUTORIAL_BEGINNERS.md` | Lev-oriented plain tutorial (Lev 12) |
| `logic/SYSTEM.md` | Full method: formats, steps A–J, comments, provenance tags |
| `logic/SCHEMA.yaml` | Field definitions for unit documents |
| `logic/templates/unit_template.yaml` | Copy to start a new unit |
| `logic/units/` | Finished / in-progress logic packages |
| `logic/units/lev_12_childbirth.yaml` | Worked Lev 12 example |

### Ta'amim tree parser (structure layer — our own trees)

**We parse phrase trees ourselves from ta'amim**, with a **versioned rule-based** system (not silent guessing; not per-verse hacks).

| Path | Role |
|------|------|
| `logic/TAAMIM_TREE_PARSER.md` | Method: versioned rules, error → bump version, golden tests |
| `logic/TAAMIM_PARSE_NOTES.md` | **Living notes** — update when parse understanding changes (changelog, open questions) |
| `logic/taamim_rules/CURRENT` | Active rule version id |
| `logic/taamim_rules/vN/` | Frozen ranks + algorithm for that version |
| `taamim_tree_parse.py` | Interpreter only — loads active rules, parses any verse the same way |

**When a tree is wrong:** note it in `TAAMIM_PARSE_NOTES.md` → add golden test → fix rules in a **new** version → update `CURRENT` → re-run tests. Never `if verse == …` in code.  
**OSHB `n=`** may be used as an optional comparison, not as the authority for *our* trees.  
**Pre-Code Logic** still owns IF/THEN derivation in YAML units after trees exist.

**Show all work (trees):** record full ta'amim trees **inside each unit** under `binary_trees` (`rule_set_version`, top split, **`tree_ascii`**, `maps_to`) plus **`tree_coverage`** for every leaf. Do not leave trees only in chat. Procedure: `logic/SHOW_WORK_TREES_2026-07-20.md` · standing: `reviews/STANDING_DECISIONS.md` §6a · reference: `logic/units/gen_01_day4_lights.yaml`.

**Tree display (ACTIVE — do not re-quiz):** When showing a ta’amim tree in chat or reports, use **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`**:
1. **en+he line:** `(english · Hebrew) (next · Hebrew) …` with `‖` after etnachta leaf when present;
2. **Each leaf Bn** + table **Word (English) | Role (glue/HEAD) | Morphology (English)**;
3. **OSHB morph per word** inside multi-word leaves (never one merged morph for the whole leaf);
4. English-first; name *et* consistently when Hebrew has את / ו/את.
Canonical example: **Lev 1:2** in that file. CLI `--tree` = debug/unit `tree_ascii` only. Index: `logic/TREE_DISPLAY.md`. Standing: `reviews/STANDING_DECISIONS.md` §6.

**Summary:**
1. Source of truth = Hebrew (`Data/*_he*` / OSHB XML etc.).
2. **Binary / ta'amim trees first** — prefer **our versioned ta'amim parser** (`taamim_tree_parse.py` + `logic/taamim_rules/`); OSHB `n=` optional cross-check. **Store trees in unit `binary_trees`.** Then phrase map / boot steps / decision table / FSM / rules.
3. Express **legal/logic** rules in YAML unit files under `logic/units/` — not as ad-hoc Python. Ta'amim **structure** rules live under `logic/taamim_rules/` and are only *interpreted* by code.
4. Every atom: **`he` + `he_translit` + `en`** (all required) + English `comment` + `confidence` + `source`. Never bare Hebrew.
5. Fill `derivation_log` steps A–J with English comments as you work.
6. Optional Oral only with named location; never silent merge into Written.
7. Scenarios test the logic doc without requiring an interpreter; scenario `value_he` also needs `value_he_translit`.
8. `status: frozen` before any optional code loads the document.

**Reference units:** Lev legal — `logic/units/lev_12_childbirth.yaml`; Genesis boot + full tree record — `logic/units/gen_01_day4_lights.yaml`.

### Tree → logic consistency (long-term goal)
- Maintain a **reusable rule set** for interpreting verse binary trees into logic: `logic/TREE_INTERPRETATION_RULES.md` (TIR-xxx).
- **Aspiration: 100% word use** — every word in a verse tree is assigned a role (including header/glue as explicit roles). Early work may fall short; treat gaps as backlog, not silence.
- Prefer **consistent** cross-verse mappings over one-off interpretations; when stuck, log `[OPEN]` and propose a new TIR rule.
- Units should grow a **`tree_coverage`** table (every word → role + TIR id + feeds).

## Leviticus 12 track (historical / reference)

When working **specifically** on the older Lev 12 legal-derivation artifacts (phrase trees → rules → Oral links), see:
- `artifacts/DERIVATION_METHOD.md` — procedure used for that track
- `artifacts/lev12_torah_model.py` and related JSON under `artifacts/`

That track used a stricter provenance style (ta'amim / Written / named Oral) and Python-era models. It remains a **reference experiment**. **New** Torah logic derivation should use `logic/` (Pre-Code Logic System).

## Reviewing other code folders
- Fast reviews live under `reviews/<ProjectName>/` (see `reviews/README.md`).
- Default depth is **L0 + English docs only**; no re-running foreign code unless asked.
- One folder per source project so we can reference them later without re-scanning.
- **Agent-owned defaults** (active project, כי policy, next unit, what to import): `reviews/STANDING_DECISIONS.md`. Do not re-quiz the owner on those; update that file when evidence changes.
