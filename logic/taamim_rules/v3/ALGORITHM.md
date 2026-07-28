# Ta'amim parse algorithm — v3 (prose v2 + poetry experiment)

**Version:** `v3`  
**Systems:** `prose` | `poetry`  
**Prose algorithm:** same as **v2** (mandatory glue bricks → pure binary dichotomy)  
**Poetry algorithm:** **same glue + binary nest**, but ranks from `ranks_poetry.yaml`  
**Confidence:** poetry ranks = **hypothesis seed** (logic-friendly Prov/Ps goldens)

---

## System selection (per verse)

| Rule | System |
|------|--------|
| Book in {Ps, Prov} | **poetry** |
| Book Job, chapter in **1, 2, 42** | **prose** (narrative frame) |
| Book Job, other chapters | **poetry** |
| All other books | **prose** |

Override: `--force-prose` / `--force-poetry` (debug).

Encode Job frame chapters in this file / loader — **not** scattered `if` hacks per golden.

---

## Prose path

Identical to v2:

1. Load `ranks_prose.yaml`  
2. Glue bricks (conj/zero until disjunctive)  
3. Binary continuous dichotomy on bricks (leftmost strongest)  
4. Invariants: leaf_complete; pure_binary  

---

## Poetry path (experiment)

1. Load `ranks_poetry.yaml`  
2. **Same** glue + binary dichotomy as prose  
3. Critical rank differences (seed):  
   - **dehi** = disjunctive (rank 2), not conjunctive  
   - **ole** = disjunctive (rank 1), major poetic divider  
   - **zinor** = disjunctive (rank 2)  
   - **etnachta** still major mid (rank 1)  
   - **silluq** verse end (rank 1)  
4. Goldens track **plain-verse logic** (A‖B / IF→THEN) for Prov duals  

**Not claimed:** full Wickes poetical treatise fidelity; full Psalter coverage.

---

## Failures

- Empty verse / unknown mark  
- Poetry book without poetry ranks file  
- pure_binary / leaf_complete fail  

---

## Changelog

| Ver | Note |
|-----|------|
| v1 | Word-level dichotomy |
| v2 | Glue bricks + pure binary (prose) |
| **v3** | + **poetry system** + `ranks_poetry.yaml` + Job frame map |
