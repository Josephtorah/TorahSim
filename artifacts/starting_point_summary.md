# Starting Point — Torah as computational information architecture

## Web recovery short form

> Focus on Lev 12 as test case.  
> Methodology: Parse ta'amim trees → extract rules → link to Oral sources.  
> Representation only — traceable at every step.

---

## Hypothesis (testable claims)

1. The Masoretic Text + cantillation encodes hierarchical, recursive syntactic structure (binary/CFG-like) usable as a parse layer.
2. Oral layers enable generative, rule-bounded processing: **Mishnah** as boot/declarative procedures; **Talmud** as derivation/inference.
3. Multi-scale patterns (parallelism, chiasmus, self-similarity) organize the corpus beyond single verses.
4. Modern tools can **represent and run aspects** of this structure for study—without claiming autonomous law generation.

## Immediate starting text

**Leviticus 12:1–8** (Parashat Tazria) — short legal unit on postpartum impurity/purification.

Why:

- Only 8 verses; self-contained procedure  
- Clear Written conditions and durations  
- Rich Oral expansion (Mishnah Niddah, Talmud Niddah 31a, midrashim)  
- Ideal for testing **Written = data**, **Oral = runtime**

### Written content (summary)

| Birth | Impurity | Purification |
|-------|----------|--------------|
| Male | 7 days (like niddah) | 33 days blood purification |
| Female | 14 days | 66 days |

During impurity: no holy things / sanctuary. Day 8: male circumcision. End: offerings (lamb + bird, or two birds if poor); priest atones → pure.

### Syntactic layer

Ta'amim create recursive trees: header → condition (birth + gender) → timed consequences → restrictions/reference → ritual → pure status.

Existing LREC treebank methodology proves full-Bible modelability.

### Oral examples

- **Talmud Niddah 31a** — doubled periods for girls (oath/remorse in labor explanation, R. Shimon b. Yochai).  
- **Mishnah Niddah** — counting, stains, miscarriage timing (e.g. 3:7), caesarean cases; often without citing Lev 12.

## Methodology

1. Acquire structured text (`Data/`, Sefaria, treebanks).  
2. Parse syntactic trees (ta'amim).  
3. Extract rules only from delimited phrases + explicit verse wording.  
4. Link named Oral sources.  
5. Build JSON / Python **only** when justified.  
6. Document every mapping.

## Current artifacts (this folder)

- `lev12_2_model.json` — first justified verse model  
- `leviticus_12_full_model.json` — full chapter  
- `leviticus_12_analysis_process.md` — process log  
- `leviticus_12_2_word_by_word.md` — phrase accounting  
- `lev12_torah_model.py` — layered demo  
- `torah_test_scenarios.json` — input scenarios  
- Mishnah Niddah ch. 1–3 extracts from `Data/`

## Expand only when previous layer is solid

Order preferred by the thread:

1. Data structures (trees / JSON)  
2. Explicit Oral links  
3. Small executable representation  
4. Scenario harness  
5. Broader chapters (e.g. Berakhot)
