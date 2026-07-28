# Torah-MVP

**Path:** `<old-home>/code/Torah-MVP`  
**Reviewed:** 2026-07-10  
**Depth:** L0 + **Audit 2 (16Q, live re-runs on prophet-test)**  
**Decision:** undecided  
**Docs:** `REVIEW-2026-07-10.md` (pre-audit) · `AUDIT-2026-07-10.md` (authoritative)

## What it is (3–5 bullets)

- Compiles MAM Leningrad CSVs → Python via **torahc2** (native פ/ס + cantillation + 4 Unicode layers)
- **Reproduced today:** layer counts, 673 blocks, 573 tests, half-verse trees, ketiv/qere 36/38
- Runtime does **not** read Torah at run time (compile-time strings)
- **Lev 12 not implemented** (7+33/14+66 prose-only); Lev 11 has negation bug; Lev 13 mostly works (57/59 splits)
- Dirty **prophet-test** tree is a keeper to commit upstream

## Hub files

- `torahc2/` (esp. `unicode_layers.py`, `blocks.py`, `cantillation.py`, `compiler.py`)
- `data/text_MAM_*.csv`
- `tests/test_torahc2.py`, `output2/main.py`, `output2/runtime_adapter.py`
- `reports/BINARY_STRUCTURE_ANALYSIS.md`, FINDINGS §7

## Worth saving (max 5)

1. Four-layer census method + verified counts (quote 85-convention carefully)
2. פ/ס → 673 block segmentation (know the 690/669/673 triple)
3. In-repo cantillation trees (`build_verse_tree` / `half_verse_split`)
4. torahc2 package + tests (structure-first compiler)
5. Cautious claim + FINDINGS §7 epistemics

## Dead ends / ignore

- “1/106” (no script)
- main-branch hash linker / pre-fix dumps
- “Lev 13 every verse” (57/59)
- Lev 11 verdicts until negation fixed
- Full OS intent claims; runtime as “reading” the Torah

## Open questions (max 3)

1. Commit dirty prophet-test before any port?
2. Port only `torahc2`+data+tests, or also output2 adapter?
3. Re-run layer/marker census on Torah_Grok `Data/` encodings?

## Next action

User: **archive / cherry-pick KEEP list / later**. Next path → new `reviews/<Name>/`.
