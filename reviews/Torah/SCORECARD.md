# Torah

**Path:** `/Users/brianleblanc/code/Torah`  
**Size (ex venv):** ~20–25 MB  
**Reviewed:** 2026-07-10  
**Depth:** L0 + external audit (24Q)  
**Decision:** undecided — prefer audit over DISCOVERY “validated” claims  
**Audit:** `AUDIT-2026-07-10.md`

## What it is (3–5 bullets)

- Discovery lab with strong narrative and self-corrections
- Most headline “stats” are **prose-only**, not reproducible code
- One solid reproducible regularity: **Numbers 7 CV ≈ 0.013**
- Comparative Prophets test ≈ **tie** (markers partly generic); Lev/purity stand out
- Six “OS” demos are **hardcoded metaphors**, not text-reading engines; purity code ≠ Lev 12 two-phase

## Hub files

- `DISCOVERY.md` (process + failures — distrust embedded p-values)
- `AUDIT` source: `my-prompts/audit-response-2026-07-10.md`
- `scanner/` (`interpret.py`, `results.json`, `interpret_output.txt`)
- `torah_vs_prophets.py` + `torah_vs_prophets_output.txt`
- `parser/keywords.py`, `systems/compiler-spec.md`, `systems/purity/`
- `data/text_MAM_*.csv`

## Worth saving (max 5)

1. Audit corrections + cautious central finding  
2. Dead ends (spectral/ELS) + “don’t re-cite prose stats”  
3. Reproducible bits: Num 7 CV, 414-block export, Prophets baseline output  
4. Port candidates: MAM CSV, interpret+loader, keywords.py, compiler-spec, DISCOVERY  
5. Leviticus/purity as **anomaly to re-test** (not whole-Torah OS)

## Dead ends / ignore

- eleh 100% / colophon p-values / Genesis 92.7% as “validated”  
- “Zero contradictions” opcode claim  
- Two-tool agreement as quantified proof  
- torah_main.py mega-wiring  
- Message bus as formal system  

## Open questions (max 3)

1. Run interpret.py on shuffled Torah + Ezek 40–48?  
2. Fix or replace purity FSM for real Lev 12 (7+33 / 14+66)?  
3. Cherry-pick port of five files into Torah_Grok or leave pointers only?

## Next action

User decision: **archive** vs **cherry-pick five files**. Then L0 next `~/code` path only.
