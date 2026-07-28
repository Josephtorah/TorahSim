# Torah-2nd-MVP

**Path:** `/Users/brianleblanc/code/Torah-2nd-MVP`  
**Reviewed:** 2026-07-11  
**Depth:** Insight brief (tests + pipeline re-run + hand recounts)  
**Decision:** undecided  
**Full notes:** `REVIEW-2026-07-11.md`

## What it is (3–5 bullets)

- Cantillation-first compiler (V2 of Torah-MVP): all Masoretic mark layers as encoding
- Universal 3-signal extractor (tree position, vowel morphology, block type) — no block-specific extractors
- Also claims Torah “describes its own architecture” (1+3+1, Gen 1 as pipeline) — mostly interpretation
- **Reproduces** from one command (`python3 -m torahc`); 117 tests; better than `~/code/Torah` on re-runs
- Parser/stats strong; “executable program” weak (DB: 0 rules/counts/constraints)

## Hub files

- `torahc/` (tokenizer, cantillation trees, פ/ס blocks)
- `docs/how-we-found-the-program.md`
- `docs/torah-top-level-architecture.md`
- `docs/rabbinic-compression-theory.md`
- `output/torah.db`, `tests/test_compiler.py`
- Commit `82483aa` (honest revert of recursive decompression)

## Worth saving (insights)

1. **Universal-extractor distributional stats** (particles, entity flow, preposition density, domain nouns) — mechanical route to known BH linguistics
2. **Predicate-shape template sequences** (Gen 5, Gen 11, Num 7, Deut 27…) — called the most novel mechanical result
3. **Dispatch formula 0/11/27/32/0** (Ex–Num speech formula) — hand-verified fact
4. **Best layers/trees/blocks implementation** among the three repos (per this brief)
5. Rabbinic compression as **prior-art framing** (prose); revert discipline as method

## Dead ends / ignore

- V1 keyword extraction (falsified)
- Recursive decompression / 7-day loop (theming)
- LLM verse→CS “findings” factory (~450 unfalsifiable)
- Gen 1 = compiler phases (re-fittable mapping)
- “Executable program” (empty rules in DB)

## New vs Torah + Torah-MVP?

**Yes, some:** template detection; universal-extractor stats; verified formula distribution; rabbinic-compression doc; actually regenerable pipeline.  
**Not new:** layers/trees/blocks themselves (MVP); “Torah is a program” story.

## Open questions

1. Freeze Tipeha KING vs DUKE (uncommitted; shifts all tree stats)
2. Template count vs shuffled control?
3. Particle fingerprints on Prophets (out-of-sample)?

## Next action

Insight bank only unless user cherry-picks. Next folder → new brief.
