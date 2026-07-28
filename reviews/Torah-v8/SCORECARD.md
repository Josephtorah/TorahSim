# Torah-v8

**Path:** `<old-home>/code/Torah-v8`  
**Reviewed:** 2026-07-18  
**Depth:** L0 English summary only  
**Decision:** cherry-pick a few methods; **do not** adopt “Torah Engine” runtime

## What it is (3–5 bullets)

- Thesis: Tanakh structured like source code; te'amim = deterministic binary parse trees  
- Pipeline story: Nedarim 37b-style layers (read → roots → verse structure → accents)  
- Large architecture writeup (many markdown files, 7-layer stack) + partial working interpreter  
- Claimed interpreter quality vs ground truth: **~73% precision / 42% recall** (their number; not re-run here)  
- Flagship targets: Lev 13–14 ↔ Negaim; Mishnah “3×5 grid = tree at chapter scale”; morphological form signal  

## Hub files

- `PARSE_RULES.md` / `REJECTED_RULES.md` — rule discipline + over-fire fixes  
- `THE_CANTILLATION_PARADOX.txt` — “grammar ≠ tree splits” writeup  
- `HOW_TO_PARSE_A_VERSE.md`, `SLIDING_WINDOW.md` — interpreter method  
- `SCHEMA.md`, `BUILD_ORDER.md` — DB/stack design (reference only)  

## Worth saving (max 5)

1. **Deterministic tree: same input → same tree** (we already enforce via versioned rules + goldens)  
2. **Morphology/form is signal** (verb/noun/particle roles) — hypothesis with Lev 13 anecdote; don’t throw form away  
3. **Rules must not over-fire** — start source-verse-local; widen only with evidence (sliding window / tiered cost)  
4. **REJECTED_RULES catalog habit** — same as v5/v6 kill lists  
5. **Lev 13–14 ↔ Negaim as stress test** — after Lev 12; named Oral only  

## Dead ends / ignore

- Nehemiah **is** the compiler / boot machine as fact  
- Mishnah 3×5 grid = proven binary tree at chapter scale (April V100–V103) without our re-derive  
- Etnachta-as-equals-sign / whole-system equations as general law  
- Full 7-layer “Torah Engine” stack merge  
- Talmud as free root resolver without quote-level verification here  
- Their precision/recall as our success metric  

## Open questions (agent-owned)

None blocking. If we later steal a rule idea, read `PARSE_RULES.md` + `REJECTED_RULES.md` only.

## Next action

Leave code/DB here. Continue Torah_Grok: Lev 12 → goldens → Lev 13–14. Optionally skim `REJECTED_RULES.md` when writing TIR rules.
