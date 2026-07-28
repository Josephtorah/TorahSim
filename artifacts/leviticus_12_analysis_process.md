# Leviticus 12 Full Chapter Analysis Process

> Provenance: local recovery + web Grok recovery paste (2026-07-10).  
> Guiding rule: every logical element traces to ta'amim hierarchy, Written text, or a named Oral source. **Representation only — not autonomous law generation.**

## Overview (web recovery)

This document records the step-by-step refinement of modeling Leviticus 12 as a computational information architecture.

**Hypothesis**: The Written Torah provides base data and syntactic structure (via cantillation/ta'amim as parse trees); Oral Torah provides runtime inference/derivation logic. The system is self-describing and progressively revealable.

**Immediate Starting Text**: Leviticus 12 (full short chapter, 8 verses) — legal unit on postpartum purification, ideal for testing structure + derivation.

**Syntactic Layer (Cantillation)**: Ta'amim create hierarchical recursive trees. Strong disjunctives divide major phrases; conjunctives link subunits. Existing LREC treebank proves this is modelable across the entire Hebrew Bible.

**Written Logic from Lev 12**:
- Birth condition → Gender-specific impurity periods → Purification → Offerings → Atonement/purity.

**Oral Derivations** (examples):
- Talmud Niddah 31a: Explains doubled periods for girls (R. Shimon bar Yochai links to the mother's potential oath during labor pain).
- Midrash: Symbolic meanings (life/death cycles, etc.).

**Methodology**:
1. Acquire structured text (Sefaria API + ta'amim).
2. Parse syntactic trees.
3. Extract rules.
4. Link to named Oral sources.
5. Build traceable models only when justified.

**Current Artifact**: JSON model for Lev 12:2 (syntactic tree + rule + one derivation link) — fully traceable.

This is our rigorous, step-by-step foundation. Expand only with clear justification from text/sources.

---

# Detailed process notes (local expansion)

---

## 1. Why this chapter

Compact legal procedure (8 verses). Gender-differentiated timed states + unified closing ritual. Oral Torah expands extensively without always quoting.

---

## 2. Chapter-level ta'amim-style tree (prose legal pattern)

```
Root (Chapter — divine command framework)
├── Intro (v1): "God spoke to Moses saying" (setup/header)
│
├── Male Child Block (v2–4)
│   ├── Condition: woman conceives and bears male
│   │   └── Impurity: 7 days (like niddah)
│   ├── Consequence: 33 days blood purification
│   │   └── Restrictions: no holy things / sanctuary
│   └── Special: circumcision on day 8
│
├── Female Child Block (v5) — parallel structure
│   ├── Condition: woman bears female
│   │   └── Impurity: 14 days (doubled)
│   └── Consequence: 66 days blood purification (doubled)
│
└── Unified Ritual Block (v6–8)
    ├── Condition: end of purification period (male or female)
    ├── Offerings: burnt + sin (lamb + bird, or two birds if poor)
    └── Outcome: priest atones → pure
```

### Consistency checks (thread findings)

| Question | Answer |
|----------|--------|
| Logic consistent across chapter? | Yes — condition → timed states → restrictions → ritual → pure |
| Verse splits predictable? | Yes — gender contrast, special rule (v3), ritual close |
| Variables self-evident? | Yes — gender, impurity days, purification days, status, offerings |

---

## 3. Verse 2 tree + IF placement

Hebrew (Masoretic form as used in thread):

> דַּבֵּ֨ר אֶל־בְּנֵ֣י יִשְׂרָאֵל֮ לֵאמֹר֒ אִשָּׁה֙ כִּ֣י תַזְרִ֔יעַ וְיָלְדָ֖ה זָכָ֑ר וְטָמְאָ֖ה שִׁבְעַ֣ת יָמִ֑ים כִּימֵ֙י נִדַּ֣ת דְּוֹתָ֔הּ תִּטְמָֽא׃

```
Root (sof pasuq)
├── Header: "Speak to the children of Israel saying"
├── Condition pivot: "A woman who conceives and bears a male"
│   └── strong disjunctive near "zachar" → IF trigger
├── Consequence subtree
│   ├── "She shall be impure seven days"
│   └── "Like the days of her niddah impurity"
└── Implication: "She shall be impure"
```

### Derivation steps

1. Header separated by major division → setup, not IF.  
2. Condition pivot at birth + male → **IF child_gender == male**.  
3. Consequence subtree → **THEN** duration + niddah reference.  
4. Implication → status **impure**.  
5. Variables only from delimited phrases: gender, 7 days, niddah reference, impure.

---

## 4. Variables extracted (full chapter)

| Variable | Source in tree | Values |
|----------|----------------|--------|
| child_gender | Condition pivot | male / female |
| impurity_duration_days | Consequence | 7 / 14 |
| purification_duration_days | Consequence | 33 / 66 |
| status | Implication | impure → pure after ritual |
| restrictions | Impurity block | no holy things / sanctuary |
| offering_type | Ritual block | lamb+bird or two birds if poor |
| outcome | Final implication | pure |

---

## 5. Oral integration

### Mishnah Niddah (boot / operational layer)

- Rarely quotes Lev 12; assumes framework.  
- Ch. 1–2: timing, stains, examinations.  
- Ch. 3 (e.g. 3:7): miscarriage day 40 vs 41 — treat as boy **and** girl + niddah blood in ambiguity.  
- Caesarean and other edge cases adjust application of 7/14 + 33/66.  

See `mishnah_niddah_ch1.md` … `ch3.md` and `lev12_mishnah_mapping.md`.

### Talmud Niddah 31a (inference / “why”)

Question: why 7 days for male, 14 for female?

R. Shimon bar Yochai (as summarized in thread): in labor pain the mother may swear never to have relations again; remorse is quicker after a male birth (7) than female (14). Connected to the sin offering at purification’s end.

---

## 6. Word accounting (every word?)

**No** — not one variable per word. Ta'amim **group** words into phrases; content phrases become logic; connectors are glue. Full phrase accounting for v2: `leviticus_12_2_word_by_word.md`.

---

## 7. Refinement history (thread)

1. High-level if-then  
2. Explicit tree + pivot for IF  
3. Full-chapter consistency  
4. Word-level discipline  
5. Mishnah + Talmud layers  
6. Python representation + scenarios  

---

## 8. What this is not

This process does **not** claim:

- A complete formalization of all midot derabbanan  
- Binding poskim-level output from a script  
- That computation replaces study, tradition, or human judgment  

It **does** claim a transparent, auditable mapping useful for reverse-engineering structure.
