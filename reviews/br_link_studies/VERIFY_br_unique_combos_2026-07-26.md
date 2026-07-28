# VERIFY — Do unique word combos explain BR’s cited links?

**Date:** 2026-07-26  
**Kind:** large verification · show work · **not** binding law  
**Data:** full Tanakh morphhb (~23,213 verses) · all parseable BR citations  
**Machine summary:** `_verify_br_unique_combos_2026-07-26.json`

---

## Question

If rare Hebrew lemma combos are how absolute links work, then:

1. Do BR-cited verses mostly have unique combos?  
2. When BR cites **two** verses together, do they **share** a rare combo that glues them?

---

## Scale tested

| Item | Count |
|------|------:|
| Unique verse refs cited in BR (tags) | ~3,018 |
| Found in morphhb with lemmas | **3,009** |
| Multi-cite BR sections | 835 |
| Co-cite edges (pairs in same section) | **12,891** |
| Baseline: random Tanakh verses | 2,000 |

**Method:**  
- Drop ultra-common lemmas (appear in >400 verses: YHWH, said, etc.).  
- Remaining = “content” lemmas.  
- For each verse: does it contain any **pair** of content lemmas that appears in only **1** verse in all Tanakh?  
- For each co-cited pair: do the two verses **share** content lemmas, and is that shared glue rare (n=1 or ≤3)?

---

## Result 1 — Most BR-cited verses *have* a unique pair… but so does most of the Bible

| Class | BR-cited verses | % |
|-------|----------------:|--:|
| **Hard:** has a unique content **pair** (n=1 in Tanakh) | 2,610 | **86.7%** |
| Strong: rarest pair ≤3 | 242 | 8.0% |
| Medium / common / none | ~157 | ~5.2% |

**HARD unique (pair or single):** **86.8%** of BR-cited verses.

### Baseline (random Tanakh)

| Class | Random 2,000 | % |
|-------|-------------:|--:|
| Hard unique pair | 1,536 | **76.8%** |
| Strong pair ≤3 | 272 | 13.6% |
| Other | 192 | 9.6% |

BR-cited is only **~10 points** higher than random (86.7% vs 76.8%).

**Meaning:**  
Having *some* unique lemma pair is **normal** for Hebrew verses (rare names, rare juxtapositions).  
It does **not** prove “BR only cites absolute ports.”  
Many “unique pairs” are trivial (two rare proper names that only meet once).

**Verdict on claim “every BR cite is a unique-combo port”:**  
**Mostly true as a weak statistic, but mostly true of the whole Tanakh too — not a BR-specific law.**

---

## Result 2 — Co-cited verses almost never share rare glue (**main falsification**)

When BR puts verse A and verse B in the **same section**, do they share a rare word combo?

| Co-cite edge property | Count | % of 12,891 |
|----------------------|------:|------------:|
| **No shared content lemma at all** | 10,486 | **81.3%** |
| Shared only common-ish content (glue freq >10) | 1,956 | 15.2% |
| Shared glue medium (≤10) | 214 | 1.7% |
| Shared glue strong (≤3) | 235 | **1.8%** |
| Shared glue **hard unique (n=1)** | **0** | **0.0%** |

**Only ~19%** of co-cite edges share *any* non-junk content lemma.  
**Zero** co-cite edges share a lemma-pair (or shared single) that is unique in the whole Tanakh under this test.

### Classic counterexample: BR 1:1 *amon*

| Pair | Shared content lemmas (Strong’s)? |
|------|-------------------------------------|
| Prov 8:30 + Num 11:12 | **none** in our content filter |
| Prov 8:30 + Lam 4:5 | none |
| Prov 8:30 + Esth 2:7 | none |
| Prov 8:30 + Nah 3:8 | none |

Midrash links them by **related root / sound / sense** (אמון / אומן / אמנים / נא אמון), not by an identical rare Strong’s pair living in both verses.

**Verdict on claim “BR links two verses because they share a unique combo”:**  
**Failed** on the large co-cite test.

---

## Result 3 — What this means for the theory

| Claim | Status after verification |
|-------|---------------------------|
| Some verses are absolute ports (unique multi-lemma signatures) | **Still true** (e.g. Job 38:15, Prov 4:18) — hand-checked domains work |
| Unique combos exist for *all* BR cites | **No** — ~3% common-only; and “unique pair” is too easy/noisy |
| BR co-citations are explained by shared unique combos | **No** — 0% hard shared glue; 81% no shared content |
| Random verse ≈ BR cite for “has unique pair” | Roughly yes (77% vs 87%) — weak selectivity |

### What BR is actually doing (updated)

```text
NOT:  find two verses that share password P
BUT:  often:
  - same root family / sound play (amon lattice)
  - same topic with different words (light / hide / path)
  - same story role (prove A then prove B)
  - sometimes same rare lemma lattice (reishit list)
  - sometimes true unique ports (Job 38:15 + Prov 4:18) without sharing a lemma
```

The **twin ports** (Job 38:15 / Prov 4:18) remain excellent **hand-picked** absolute addresses.  
They are **not** the general rule for every BR citation edge.

---

## Result 4 — Sample “common only” BR cites (no rare pair)

Examples that BR cites but fail unique-pair test:  
Exod 20:2, Exod 15:3, Exod 1:1, Deut 5:12, Gen 11:1, etc. — high-frequency theological or formula language.

These are **important** verses, not ports by rarity.

---

## Simple takeaway

1. **Can we verify from other BR cites?** Yes — we checked ~3,000 cites and ~13,000 co-cite edges.  
2. **Do unique combos exist for all of them?** **No.**  
3. **Do co-cited pairs share unique combos?** Almost **never** (0% hard shared; 81% share nothing content-like).  
4. **Rare combos still matter** for finding special *ports* (passwords).  
5. They do **not** by themselves explain **how BR chooses which verses to wire together**.

---

## Confidence

| Finding | Label |
|---------|--------|
| Numbers above | **tested** |
| Unique-pair rate high for most verses (artifact) | **tested** |
| Co-cite shared-unique-glue ≈ 0 | **tested** |
| BR general link logic ≠ shared Strong’s password | **tested** |
| Better automated glue (root families, not Strong’s pairs) | **open next** |

---

## Next method (if we continue)

To re-test more fairly:

1. **Root-family** match (consonantal roots), not only Strong’s number pairs.  
2. **Domain-restricted** uniqueness (e.g. only within light-lemmas).  
3. Separate **name-noise** pairs from semantic pairs.  
4. Score BR edges as: root-share / topic-share / unique-port-pair / thematic-only.

---

## Files

- This report  
- `_verify_br_unique_combos_2026-07-26.json`  
- Prior absolute scan: `SCAN_tanakh_absolute_links_2026-07-26.md`  
