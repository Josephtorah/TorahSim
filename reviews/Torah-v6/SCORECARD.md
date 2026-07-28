# Torah-v6

**Path:** `<old-home>/code/Torah-v6`  
**Reviewed:** 2026-07-18  
**Depth:** L0 from **their** English Q&A (`v8/QA-TORAH-GROK.md`) — no local re-run  
**Decision:** cherry-pick (methods + lessons only)

## What it is (3–5 bullets)

- Tanakh-wide cantillation → binary tree → “gates” (IF verses) + root co-occurrence runtime over 39 books  
- Headline story: 23,211 verse ops, 488 gates, 0 dead *gates*, 16 math formulas, ~149 authored pattern rules  
- `v8/SPEC.md` is a rewrite blueprint; **v6** is what actually produced the numbers  
- Mishnah “oracle” (686 pairs) is **parsed only** — never executed as tests  
- Stronger honesty layer in the Q&A than earlier family marketing (Liskov order, dove post-hoc, metric corrections)

## Hub files (paths worth opening later)

- `v8/QA-TORAH-GROK.md` — grounded answers (prefer this over SPEC marketing)  
- `v8/SPEC.md` — blueprint only  
- `v6/docs/MASTER-PATTERN.md` — authored rules (Hebrew signal + proof verse)  
- `v6/docs/ASSUMPTIONS.md` — A-001…A-035 ledger  
- `v6/src/pipeline/parse.py` + `accents.py` — tree algorithm  
- `v8/TALMUD-INSTRUCTIONS-CLEAN.md` — 28 literal-only Talmud process rules  
- `v8/output/mishnah_oracle.json` — aspirational oracle (no validator)

## Worth saving (max 5)

1. **כי rule (as shipped):** verse-initial bare כי → BECAUSE (not IF gate); אם/ואם/וכי → IF — simple first-token rule  
2. **Leftmost continuous dichotomy** + prose/poetic te'amim fork (and Job prose gap as known bug)  
3. **Reject catalog:** temple-as-software, grammar-as-opcodes, imposed runtime state, OS book roles  
4. **“Suspect our reading when gates die”** + ASSUMPTIONS-style ledger pattern  
5. **Math fixtures for Lev 12:4 / 12:5** (30+3=33, 60+6=66) as tree-arithmetic *checks*, not purity FSM

## Dead ends / ignore

- Importing `lev.json` / fired-gate / dead-gate / interface dashboards (corpus-global; silent wrong numbers if partial)  
- Blind-copy `v8/data/` (no LICENSE; Sefaria `license: null`; re-source texts)  
- “0 dead code,” “143 rules,” “Liskov discovered before Mishnah,” dove-as-confirmed protocol (corrected in Q&A)  
- 686 oracle as a working test suite (write-only; no Torah op IDs)  
- Timed purity states (7+33 / 14+66) — **not implemented** in v6; structural numbers only

## Open questions (max 3)

1. Would a null-corpus header-type test still look “97% special”? (they never ran it)  
2. Root table accuracy vs OSHB sample? (never measured; generator lost)  
3. First-token כי vs PROCESS/RESULT-side כי — which matches legal reading better for Torah_Grok?

## Next action

Keep **method + kill-list + כי lesson**; do not port runtime. Optionally read MASTER-PATTERN / ASSUMPTIONS for TIR-adjacent ideas only after Hebrew re-derive in `logic/`.
