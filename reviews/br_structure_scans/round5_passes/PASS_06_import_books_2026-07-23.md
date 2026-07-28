# Round 5 — Pass 06: Import-book mix by band

**Date:** 2026-07-23  
**Question:** Which biblical books feed BR, and does the mix change early to late?

---

## Observed — top source books (marked cites)

| Book | Cites |
|------|------:|
| Gen | 2417 |
| Ps | 525 |
| Isa | 317 |
| Job | 214 |
| Prov | 199 |
| Deut | 172 |
| Exod | 159 |
| Num | 110 |
| Jer | 105 |
| Sam | 100 |
| Ezek | 88 |
| Chr | 67 |
| Kgs | 64 |
| Dan | 60 |
| Eccl | 59 |
| Judg | 56 |
| Lev | 54 |
| Josh | 47 |

### Genesis fraction of all marked cites

| Band | Gen cites | All cites | Gen fraction |
|------|----------:|----------:|-------------:|
| early | 207 | 725 | 0.286 |
| mid | 935 | 1952 | 0.479 |
| late | 1275 | 2456 | 0.519 |

**Surprise:** Early band is **least** Genesis-heavy by fraction (~29%)—more **Psalms / Isaiah / Job / Prov** petihah imports. Mid/late climb to ~48–52% Genesis as the spine commentary cites its own book harder.

### Early vs late top imports

**Early top:** Gen(207), Ps(120), Isa(83), Job(63), Prov(34), Deut(32), Exod(29), Jer(20)

**Late top:** Gen(1275), Ps(220), Isa(105), Prov(94), Deut(81), Job(67), Exod(67), Jer(58)

---

## Hypothesis

Front of BR behaves like a **library bootloader** (wide Nakh/Torah imports into Genesis). Later BR is a **Genesis-native app** that still keeps Psalms/Isaiah/etc. as shared packages. Same monorepo, different import graph over time.

**Confidence:** tested on classified marked citations; Other bucket absorbs odd labels.
