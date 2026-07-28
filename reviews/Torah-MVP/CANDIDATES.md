# Cherry-pick (post–Audit 2)

Authoritative: `AUDIT-2026-07-10.md`.

## Port first (KEEP)

| Path | Note |
|------|------|
| `data/text_MAM_*.csv` | Corpus; compare to Torah_Grok `Data/` |
| `torahc2/` | Self-contained stdlib compiler |
| `tests/test_torahc2.py` | 573 tests on dirty tree |
| `output2/main.py` + `output2/runtime_adapter.py` | Hand-maintained chain; optional |
| `reports/BINARY_STRUCTURE_ANALYSIS.md` | Numbers verified 2026-07-10 |
| FINDINGS.md §7 | Epistemics only |

## Upstream before port

- Commit prophet-test dirty tree (22 files)  
- gitignore tracked `output/__pycache__`  

## Do not port

| Path / claim | Why |
|--------------|-----|
| `output/` | bloat + pyc tracked |
| main `torahc/linker.py` | hash fabrications |
| “1/106” | PROSE_ONLY |
| Lev 11 water/bird as truth | negation bug |
| Lev 12 timers from this repo | **not in code** |

## RE-TEST queue

- אין/לא in `compile_classification`  
- setumah 377 vs 378  
- 2 missed ketiv/qere  
- 2 Lev 13 non-splits  
- re-pin commit after clean commit  
