# Round 5 — Pass 09: Anomaly / outlier chapters

**Date:** 2026-07-23  
**Question:** Which chapters are statistical outliers on mass, cite density, formulas, multi-view?  
**Method:** per-chapter z-scores on chars, cites/sec, formula hits/sec, davar aher hits.

---

## Highest text-mass z

| Ch | char_z | cite_z | form_z | da_z | chars | cites |
|---:|-------:|-------:|-------:|-----:|------:|------:|
| 98 | 3.19 | 0.88 | 0.17 | 1.99 | 32438 | 131 |
| 65 | 2.69 | -0.01 | -0.18 | 3.62 | 29472 | 116 |
| 44 | 2.25 | -0.29 | 0.1 | 1.17 | 26880 | 105 |
| 91 | 2.03 | 1.89 | 1.69 | 0.35 | 25529 | 91 |
| 1 | 1.65 | 0.83 | 2.06 | 1.58 | 23300 | 97 |
| 84 | 1.65 | -0.3 | 0.11 | 1.17 | 23269 | 100 |
| 68 | 1.64 | 1.23 | 0.62 | 1.99 | 23245 | 100 |
| 70 | 1.61 | -0.94 | -0.01 | 2.4 | 23033 | 69 |

## Highest citation-density z

| Ch | cite_z | char_z |
|---:|-------:|-------:|
| 99 | 2.81 | 1.31 |
| 62 | 2.02 | -0.93 |
| 91 | 1.89 | 2.03 |
| 95 | 1.88 | -1.09 |
| 42 | 1.8 | 0.97 |
| 25 | 1.73 | -1.16 |
| 75 | 1.73 | 1.01 |
| 92 | 1.73 | -0.17 |

## Highest multi-view (DA) z

- ch65: da_z=3.62, char_z=2.69
- ch99: da_z=2.81, char_z=1.31
- ch70: da_z=2.4, char_z=1.61
- ch87: da_z=2.4, char_z=-0.3
- ch24: da_z=1.99, char_z=-0.86
- ch68: da_z=1.99, char_z=1.64

## Profile types

**Narrative bulk** (high mass z, below-average cite density): chapters 65, 44, 84, 70, 12, 49, 100, 48, 78, 34

**Proof-dense compact** (high cite density, not huge mass): chapters 62, 95, 25, 92, 96, 61, 35, 26, 40, 79

**Boot special:** ch.1 — high mass and high formula z (install kit).

---

## Hypothesis

Chapters are not one type. At least three modes:
1. **Bulk story apps** (mass without max cite density)
2. **Proof compressors** (short/medium, citation-hot)
3. **Install / multi-view hubs** (operator + DA spikes)

Outliers are features of a **multi-mode commentary OS**, not noise.

**Confidence:** exploratory stats; z-scores assume rough normality.
