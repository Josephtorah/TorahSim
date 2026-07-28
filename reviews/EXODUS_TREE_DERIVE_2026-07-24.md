# Exodus tree-derive reprocess

**Date:** 2026-07-24  
**Kind:** deepen track (Pre-Code) — **not** binding religious law  
**Status:** **complete** — all phases 0–2f done (45 units · 1213 STEPs)  
**Related:** `EXODUS_BUILD_2026-07-21.md` (original bulk draft) · generator supersede path: `artifacts/reprocess_exodus_from_trees.py`

On substantive update: rename to today’s date and fix links.

---

## Contract (Phase 0 — locked)

### Order (required)
```text
Hebrew verse → ta'amim tree (v1) → top split / arms → STEP claim(s) → maps_to → tree_coverage
```
**Not:** English block summary → STEP blob → paste trees.

### Grain
- **Default:** one primary STEP **per verse**, id `STEP_Ex_{ch}_{v}`.
- STEP text must cite **left arm** and **right arm** of the top binary split (etnachta or root children).
- Name-list / pure roster verses: still one STEP; arms = list structure.
- Law blocks (`decision_table`): keep genre; add **tree-cited** boot_steps per verse; decision rows hypothesis from Written markers (אם/כי/וכי) when present, else retain structural IF only when justified.

### Fields
- Every atom: **he + he_translit + en** (translit from Hebrew letters; en is free gloss `[EN-AID]`).
- `binary_trees` full `tree_ascii`; `rule_set_version: v1`.
- `meta.tree_derive_version: tree_derived_v1`.
- `maps_to: ["STEP_Ex_C_V"]` for that verse only (not multi-verse smear).
- Confidence: structure **tested**; logic claims **hypothesis** unless labeled otherwise.

### What this pass is / is not
| Is | Is not |
|----|--------|
| Tree-first grain + arm-cited steps for all Exod verses | Full TIR 100% role perfection |
| Replaces bulk multi-verse STEP blobs | Binding religious law |
| Compatible free names for Lev imports | Mekhilta deep rewrite (dual-track samples retained/refreshed) |

### Phase map

| Phase | Scope | Units | Status |
|-------|--------|-------|--------|
| **0** | Contract | this file | **done** |
| **1** | Pilot Exod 1 | `exo_01_*` | **done** (later folded into 2a label) |
| **2a** | Ch. 1–6 | 6 units | **done** |
| **2b** | Ch. 7–11 | 5 units | **done** |
| **2c** | Ch. 12–24 law/narrative spine | 18 units | **done** |
| **2d** | Ch. 25–31 install | 7 units | **done** |
| **2e** | Ch. 32–34 crisis | 3 units | **done** |
| **2f** | Ch. 35–40 | 6 units | **done** |

**Totals:** 45 units · **1213** `STEP_Ex_*` · **1213** `tree_ascii` · **0** parse errors · `meta.tree_derive_version: tree_derived_v1`

### What v1 delivered vs still open

| Delivered | Still open |
|-----------|------------|
| One STEP per verse from top-split L/R arms | Rich English/Hebrew narrative claim per arm (still template [EN-AID]) |
| `maps_to` = that verse’s STEP only | Full TIR 100% word roles |
| Real letter-map translit (not `w0`) | Pointed scholarly translit |
| Law units keep decision_table + condition marker rows | Deep Mekhilta wiring per law verse |
| Full book reprocessed in phases | Hand polish of high-value islands (Pesach, Decalogue, mishpatim) |

---

## Changelog

- 2026-07-24: Contract locked; reprocess track opened.
- 2026-07-24: Phase 1 done — `exo_01` pilot.
- 2026-07-24: Phases 2a–2f done — all 45 `exo_*` units `tree_derived_v1`.
