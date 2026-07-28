# Torah-v7

**Path:** `<old-home>/code/Torah-v7`  
**Reviewed:** 2026-07-18  
**Depth:** L0 from `PROJECT_HIGHLIGHTS.md` (English only; no re-run)  
**Decision:** cherry-pick (process + a few structural ideas); **do not** import architecture thesis wholesale

## What it is (3–5 bullets)

- Next iteration after v5/v6 family: cantillation binary tree as the “instruction,” full Tanakh as program  
- Strong **process** story: verify rules against Mishnah/Talmud JSON with exact Hebrew quotes; tiers of provenance  
- Architecture thesis: Torah = program, Mishnah = tests, Nehemiah 8 = boot, 5 monitor books, dove multi-pass  
- Flagship claims: Gen 1 declarations, Lev 13–14 loop ↔ Negaim 3:3, numbers-as-equations, middot-as-opcodes  
- **Self-retired:** too much imposed logic (Deut 4:2); reset toward v8 spec

## Hub files

- `PROJECT_HIGHLIGHTS.md` — this handoff  
- `PARSE_RULES_VERIFIED.md` — best candidate for careful read  
- `V7_PARSER_RULES_EXTRACTED.md`  
- `v8/TREE-TO-EXECUTION.md` — tree walk → gates/deposits/loops (method only)  
- `OVERVIEW.md` — Gen 1:1 / Lev 13 worked examples in English  

## Worth saving (max 5)

1. **Verification method:** strip niqqud, search full corpus, quote Hebrew, never invent from memory; keep verified / observation / impl separate  
2. **Only RESULT-side deposits; PROCESS read-only** — clear hypothesis to test on legal units (not accept as law)  
3. **Tree shape / depth as typed structure** (declaration vs command/fulfillment) — TIR-adjacent, needs Hebrew re-derive  
4. **Lev 13–14 ↔ Negaim** as *named Oral cross-check* pattern (not silent merge)  
5. **Design principles:** no imposed logic, Hebrew first, disputes as data, uncertainty valid, supersede don’t delete, deterministic tree + golden verses  

## Dead ends / ignore (or treat as interpretation only)

- Torah/Tanakh = executable program; Nehemiah = `main()`; monitor books as EVAL/TEST/LOG/CMD/STATUS (OS metaphor layer — already demoted in v6 Q&A)  
- Dove protocol / 7-pass convergence as confirmed  
- Middot = opcodes, LEFT=general/RIGHT=specific as Liskov — **hypothesis / reading**, not proven discovery  
- Blind-import 39 MAM CSVs + ~40MB Sefaria dumps (license / we already have `Data/`)  
- “Holds across all 23,211 verses” without our own fixtures  
- Whole call-graph / ring / DAG stats without English audit of method  

## Open questions (max 3)

1. Of the ~71 “verified” rules, which are **parse/structure** vs **imposed execution semantics**?  
2. Does PROCESS/RESULT deposit rule survive on Lev 12 (timed purity) without inventing clocks?  
3. How does “כי has 4 Talmud meanings” change the v6 first-token BECAUSE rule?

## Next action

Read `PARSE_RULES_VERIFIED.md` later for **structure/parse** rules only; re-derive any legal logic in `logic/` from Hebrew. Do not port runtime.
