# Genesis-Experiment

**Path:** `/Users/brianleblanc/code/Genesis-Experiment`  
**Reviewed:** 2026-07-18  
**Depth:** L0 from transfer summary (English only)  
**Decision:** cherry-pick method lessons; do not import pipeline/DB

## What it is (3–5 bullets)

- Genesis-only experiment: cantillation → binary tree for all 1,533 verses (claim: zero parse errors)  
- Strong OSHB + Strong’s lemma morphology; type **words**, not tree leaves  
- Rewrite `parser2.py` → `genesis.db` after Torah-v8 review fixed 9/10 leaf-typing problems  
- Core program-unit claim: **3-verse window** (A declare / B evaluate / C execute)  
- Open: metaphorical פני, silluq/paseq edges, past Genesis, no git  

## Hub files

- `Export/project-summary-2026-07-18.md` — portable handoff  
- `my-project/code/parser2.py` + `genesis.db` — current design  
- `my-project/code/parser.py` — large commented reference (legacy)  
- `Source/` — MAM Genesis, OSHB Gen.xml, Strong’s, Oral corpora  

## Worth saving (max 5)

1. **Type at word level, bottom-up, per-instance** — leaf = bag of typed words, not a single type  
2. **OSHB morphology + lemma as identity** — labeled external aid (#IMPOSED OK if tagged)  
3. **No registry inheritance for typing** — kills homonym/pronoun leakage  
4. **3-verse window as hypothesis** for narrative flow (test; don’t force on legal units)  
5. **Hebrew pure DB / English downstream only** — one-way data flow  

## Dead ends / ignore

- Single-verse “declaration/evaluation/execution” signatures as the main model  
- Sefer Yetzirah categories as required coverage (they say: group after, don’t require)  
- Importing `genesis.db` / full parser into Torah_Grok  
- “All 1,533 zero errors” as our proof without our goldens  
- Extending their stack to 39 books here  

## Open questions (agent-owned)

- Does 3-verse window help **legal** blocks (Lev 12) or only narrative Genesis? Default: **don’t assume**; try only if trees suggest multi-verse scope.

## Next action

When mapping roles in logic units, prefer **word-level** slots. Keep OSHB as labeled morphology. Do not adopt 3-verse program unit as global law.
