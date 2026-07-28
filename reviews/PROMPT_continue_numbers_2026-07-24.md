# Continuity prompt — Torah_Grok (Numbers next)

**Date:** 2026-07-24  
**Kind:** paste-ready session prompt (remember what we need)  
**Status:** active continuity for Written Pre-Code → Numbers

Paste the block under **PROMPT** into a fresh chat (recommended before deep Numbers work).  
On substantive update: rename this file to today’s date and fix links.

---

## PROMPT

```
You are working in the Torah_Grok repo. Follow Agents.md and reviews/STANDING_DECISIONS.md exactly.

## Project stance (do not re-quiz)
- Active workspace: Torah_Grok only. Data/ is source — do not modify JSON/XML unless asked.
- Derive logic from Hebrew Written only. English is gloss/aid, never derivation source.
- Never bare Hebrew: every Hebrew string needs he + he_translit + en (or inline he / translit / "English").
- Oral (Mishnah, Sifra, Mekhilta, Sifrei, BR, Bavli, MH): dual-track only, named locus; never silent-merge into Written steps.
- Possible Oral: do not rule out any Mesorat haShas endpoint; job order only (e.g. Sifrei Bamidbar first on Num law densification).
- Experimental models ≠ binding religious law unless owner asks that framing.
- Pre-Code Logic for Torah derivation: logic/SYSTEM.md, SCHEMA, units under logic/units/. Code interprets frozen docs; do not invent rules only in Python.
- Ta'amim trees: versioned parser taamim_tree_parse.py + logic/taamim_rules/; store trees in unit binary_trees when show-work applies.
- Dated research filenames: rename on substantive update (hub exceptions: README, Agents.md, STANDING_DECISIONS — update Last updated in body).

## Stack status (Written Pre-Code units)
DONE as full first draft (not all frozen/deep):
- Genesis: 26 gen_* units
- Exodus: 45 exo_* units (~1213 trees; Mekhilta samples on law)
- Leviticus: 50 lev_* units (~859 trees; Sifra samples)

DONE (first draft, same day as this prompt):
- Numbers: 47 num_* units (1289 verse trees); build doc NUMBERS_BUILD_2026-07-24.md

NOT STARTED → NEXT:
- Deuteronomy: Data/Deut.xml exists; zero deu_* units

Conceptual stack:
Genesis (platform/boot + sagas + Egypt handoff)
  → Exodus (nation + Sinai + mishkan install)
    → Leviticus (sanctuary apps: offerings, purity, holiness)
      → Numbers (ops / logistics / journey / census / tests)  ← DRAFT DONE
        → Deuteronomy (recompile / covenant speech / migration brief)  ← NEXT

## Oral / research tracks (parallel — not required to run Numbers)
- BR (Bereshit Rabbah): chapter summaries complete under reviews/br_chapter_summaries/; sequential packets early only. BR is optional dual-track for Genesis midrash — not required to derive five-book Written logic.
- Mishnah: full compact reviews under reviews/mishnah_chapter_summaries/ + MASTER_SUMMARY_MISHNAH_2026-07-24.md. Law-shaped Oral neighbor; not a Written compiler.
- Gen 1 Mishnah joins (dual-track only, do not rewrite Written STEPs):
  - gen_01_creation_boot: ORAL_mishnah_chullin_5_5 (day cycle → oto ve-et beno); Megillah 3:6 lection; Chagigah access
  - gen_01_day3_land_plants: ORAL_mishnah_mikvaot_5_4 (seas ≅ mikveh dispute)
  - gen_01_day6_land_human: ORAL_mishnah_yevamot_6_6 (periya u-reviya duty/metrics)
- Derive notes: reviews/mishnah_chapter_summaries/DERIVE_gen1_mishnah_2026-07-24.md
- Peers: Talmudic Logic (Gabbay et al.) models Oral reasoning; nobody reputable compiles Chumash FROM Mishnah/Talmud.

## What we decided about BR vs five books
- Can derive Written Pre-Code logic from the five books without Bereshit Rabbah.
- BR adds Genesis multi-view midrash; not the law/runtime engine.
- Practice packing often needs legal Oral (Mishnah/Sifra/Mekhilta/Sifrei), still dual-track only.

## How to work Numbers (default)
1. Build approach doc: reviews/NUMBERS_BUILD_YYYY-MM-DD.md (see NUMBERS_BUILD_2026-07-24.md).
2. Same discipline as EXODUS_BUILD / LEVITICUS_BUILD: manageable thorough blocks, not one verse unit and not one giant dump.
3. Units: logic/units/num_*.yaml (naming: num_##_slug matching block map).
4. Every block: Hebrew from Data/Num.xml → taamim trees → logic shape (boot_steps / decision_table / FSM as genre fits) → he+translit+en on atoms → tree_coverage aspiration → small scenarios → confidence labels.
5. Imports: free names that resolve to Gen ambient / Exod install / Lev apps — mark depends_on; do not re-spec Tent/altar system from scratch.
6. Oral open order for Numbers: Written first; when law densifies, dual-track named from Data/sifrei_bamidbar_he.json (Sifrei Bamidbar); never silent merge. MH endpoints remain possible Oral.
7. Genre: much of Numbers is narrative + census + logistics + case-law islands — do not force korban IF tables onto pure story.
8. Ask before bulk Data/ changes or large refactors.
9. Generator (when used): artifacts/generate_numbers_units.py — interpreter of frozen block schedule only.

## Key reference units / docs
- logic/SYSTEM.md, logic/SCHEMA.yaml, logic/SHOW_WORK_TREES_2026-07-20.md
- Show-work reference: logic/units/gen_01_day4_lights.yaml
- Legal reference: logic/units/lev_12_childbirth.yaml
- Build patterns: reviews/EXODUS_BUILD_2026-07-21.md, reviews/LEVITICUS_BUILD_2026-07-21.md
- Architecture stack: reviews/architecture/ARCHITECTURE_genesis_stack_2026-07-21.md, reviews/architecture/ARCHITECTURE_discussion_2026-07-19.md
- Continuity file (this): reviews/PROMPT_continue_numbers_2026-07-24.md

## Immediate task
Default: open Deuteronomy Pre-Code (DEUTERONOMY_BUILD dated doc + first deu_* unit(s)), same discipline as Numbers. Optional: deepen high-value Num law blocks with more Sifrei, or wire free-name imports. Do not re-derive Gen/Exod/Lev/Num unless a free-name import forces a check. Do not require BR. Use dual-track Oral only when named and useful.
```

---

## Quick status checklist (for agents)

| Item | State |
|------|--------|
| Gen/Exod/Lev first draft | done |
| Numbers build doc | `NUMBERS_BUILD_2026-07-24.md` |
| `num_*` units | **47 draft complete** (1289 trees) |
| Deuteronomy | **next** |
| BR required for five-book Written? | **no** |
| Oral on Num law | Sifrei Bamidbar dual-track when densifying |

## Related

- `reviews/STANDING_DECISIONS.md` §4 next track  
- `reviews/NUMBERS_BUILD_2026-07-24.md`  
- `Data/Num.xml` · `Data/sifrei_bamidbar_he.json`
