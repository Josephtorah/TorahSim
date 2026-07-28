# Deuteronomy tree-derive (first draft + v1)

**Date:** 2026-07-24  
**Kind:** deepen track (Pre-Code) — **not** binding religious law  
**Status:** **complete** — phases A–J done (41 units · 959 STEPs)  
**Tool:** `artifacts/reprocess_book_from_trees.py --book deu`  
**Related:** `DEUTERONOMY_BUILD_2026-07-24.md`

## Contract (same as Gen/Exod/Lev/Num v1)

```text
Hebrew verse → ta'amim tree v1 → top-split arms → one STEP_Dt_C_V per verse → maps_to → coverage
```

- `meta.tree_derive_version: tree_derived_v1`
- English on steps = `[EN-AID]` arm gloss (not full hand narrative yet)
- Oral: Written first; **Sifrei Devarim** dual-track samples on lawish genres; never silent-merge
- **Not** binding religious law; not full TIR

## Phases (10)

| Phase | Chapters | Units | ~vv | Content |
|-------|----------|------:|----:|---------|
| **A** | 1–3 | 6 | 112 | Historical prologue |
| **B** | 4–6 | 4 | 107 | Law frame / Decalogue / Shema |
| **C** | 7–11 | 5 | 129 | Loyalty / land / second tablets |
| **D** | 12–14 | 3 | 79 | Place-name / seducers / food-tithe |
| **E** | 15–18 | 4 | 87 | Release / festivals / king / prophet |
| **F** | 19–22 | 4 | 93 | Refuge / war / family / social |
| **G** | 23–26 | 4 | 86 | Assembly / divorce / courts / firstfruits |
| **H** | 27–28 | 4 | 95 | Ceremony + blessings/curses |
| **I** | 29–30 | 2 | 48 | Moab covenant |
| **J** | 31–34 | 5 | 123 | Joshua / song / blessing / death |

**Book size:** 34 chapters · **959** verses · **41** units

## Phase status

| Phase | Status |
|-------|--------|
| A–J | **done** |

**Totals:** 41 units · **959** `STEP_Dt_*` · **959** trees · **0** parse errors (target)

## Limits (v1)

- Template [EN-AID] step glosses; letter-map translit; heuristic `tree_coverage`
- First draft generated from UNIT_SPECS + tree reprocess (no prior hand narrative)

## Changelog

- 2026-07-24: Track opened; 10-phase map; full book complete.
