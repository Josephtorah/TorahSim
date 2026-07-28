# Cherry-pick candidates (post-audit)

Prefer `AUDIT-2026-07-10.md` over DISCOVERY stats.

## Port if we invest time (their top 5)

| File | Role | Note |
|------|------|------|
| `data/text_MAM_*.csv` | Corpus | Diff vs `Torah_Grok/Data` first |
| `scanner/interpret.py` + `src/loader.py` | Shape classifier | Needs null/baseline tests |
| `parser/keywords.py` | Opcode draft | 76 entries; collisions unhandled |
| `systems/compiler-spec.md` | Spec only | Not a running compiler |
| `DISCOVERY.md` | Process map | Label: narrative, not validated stats |

## Also useful pointers (don’t need full copy yet)

| Path | Why |
|------|-----|
| `scanner/results.json` | Num 7 CV evidence |
| `scanner/interpret_output.txt` | 414-block export |
| `torah_vs_prophets_output.txt` | Comparative null-ish result |
| `systems/purity/` | Rewrite candidate for Lev 12 (current code wrong) |

## Do not import as truth

- Prose p-values / eleh 100% / “validated architecture”  
- Hardcoded purity 40/80 as Lev 12  
- Message bus / torah_main OS story  
