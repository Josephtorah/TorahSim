# Research — How to parse poetry ta’amim (design; not implemented)

**Date:** 2026-07-27  
**Status:** **Partial** design from web/scholarship + repo policy  
**Kind:** research · **not** binding law · **code not changed**  
**Current code:** prose **v2** only; Ps / Prov / Job → `fail` unless `--force-prose` (debug only)

---

## 1. One-line answer

**Parse poetry with the same *kind* of engine (glue + ranked disjunctives + dichotomy), but a separate poetry accent system for the “Three” books — not Lowth parallelism and not forced prose ranks.**

---

## 2. What not to use as the main driver

| Approach | Why weak as sole parser |
|----------|-------------------------|
| Metre | Biblical verse is free rhythm, not fixed metre |
| Lowth parallel types (synonymous / antithetical / synthetic) | Useful labels; not constitutive of all verse; non-deterministic lineation |
| English “this feels poetic” | Violates Hebrew-first policy |

Parallelism / cola can be **secondary** notes later; they are not the ta’amim tree backbone.

---

## 3. The real formal signal: two Tiberian systems

| System | Books | Top-level idea |
|--------|-------|----------------|
| **Twenty-One (prose)** | Torah, Prophets, most Writings | Almost always **silluq** + interior **etnachta**; 4-tier hierarchy |
| **Three / *sifrei emet* (poetry)** | **Psalms, Proverbs, Job** (body) | **Sof pasuq** sole emperor; 1–3 stichs; top dividers **oleh ve-yored** and/or **atnach** (sometimes revia as major divider) |

**Critical:** same or similar *glyphs* can have **different names / roles** in the two systems (e.g. prose *tifcha* vs poetic *tarcha*; *mercha* vs part of *oleh ve-yored*).  
→ **Never silently reuse `ranks_prose.yaml` as poetry.**

**Authorities:** Wickes (poetical 1881 + prose 1887); Breuer *Taʿamei ha-Miqra*; Yeivin; Gesenius §15; Richter/Breuer syntax charts; OSHB accents notes (Wickes-based).

---

## 4. How a poetry verse typically splits (top level)

Unlike prose’s near-universal “one etnachta under silluq”:

```text
Poetry verse (sof pasuq / silluq end)
  may be:
    · one stich
    · two stichs   (oleh ve-yored and/or atnach as major cuts)
    · three stichs
```

**Within a stich**, major disjunctives include (names vary by table):

- *revia* (qaton / gadol)  
- *tzinnor*  
- *dechi* / *deḥi*  
- *revia mugrash*  

Placement is **more flexible** than prose’s “tipcha must sit immediately before the emperor” pattern.

**Job exception:** Job **1–2** and **42** (frame narrative) use the **prose** system; the dialogues use **poetry**.  
Book-id-only `if book in {Ps,Prov,Job}` is **wrong** without this frame exception.

---

## 5. What Torah_Grok should implement (design)

### 5.1 System switch (already sketched)

```text
system = prose | poetry
```

Selected by **verse**, not only book:

| Input | System |
|-------|--------|
| Gen…Deut, Prophets, most Writings | prose (v2) |
| Ps.*, Prov.* | poetry |
| Job.1.*, Job.2.*, Job.42.* | **prose** (frame) |
| Job.3–41 | poetry |

Encode the Job ranges in **rule data**, not ad-hoc Python forever.

### 5.2 New package pieces (next code version, e.g. v3)

| File | Role |
|------|------|
| `ranks_poetry.yaml` | Mark → kind + rank for the Three (parallel to prose) |
| `ALGORITHM.md` (poetry section or dual) | Glue + dichotomy **using poetry ranks**; document top-level 1–3 stich patterns |
| `tests/golden_poetry.json` | Seed: Ps.1.1, Ps.23.1, Prov.1.1, Job.3.3; plus Job.1.1 **prose** |
| Loader | Load prose vs poetry ranks by `system` |

### 5.3 Reuse from prose v2

| Keep | Change |
|------|--------|
| Glue-then-dichotomy idea | New mark table |
| Pure binary preferred | May need explicit multi-stich top shape (2- or 3-way **documented**) if classical poetry allows three primary stichs — decide before freeze |
| No silent winner | `unique` / `multi` / `fail` |
| Top-down **DISPLAY_FORMAT** | Same display contract |
| OSHB `n=` optional check only | Same |

**Open design fork (must decide before coding):**  
A) Force pure binary always (split three stichs as nested binary), **or**  
B) Allow top-level **ternary** only when three major poetic emperors/kings mark three stichs.

Recommend: start with **A** (binary nest) + golden tests; revisit if goldens fight the text.

### 5.4 What not to build first

- Full Lowth labeler  
- Automatic chiasmus detector as tree core  
- ETCBC dependency trees as ta’amim substitute  

Those can be dual-track later.

---

## 6. Implementation sketch (when you say go)

```text
1. Draft ranks_poetry.yaml from Wickes/Breuer/Richter secondary tables
2. System selector: book + Job chapter ranges
3. parse_verse: if poetry → load poetry ranks; else prose v2
4. Same glue_bricks + binary nest (v2 algorithm) on poetry ranks
5. Goldens: 5–10 verses; refuse wrong-system
6. Bump CURRENT only when goldens pass (v3 recommended if ALGORITHM text grows)
7. Never treat --force-prose on Psalms as “done”
```

---

## 7. Confidence

| Claim | Label |
|-------|--------|
| Poetry needs separate accent system from prose | **tested** (standard Masorah) |
| Driver = ta’amim ranks, not metre/Lowth alone | **strong** |
| Job 1–2, 42 are prose frame | **tested** (standard) |
| Exact officer-level ranks identical across Wickes/Price/Breuer | **open** (edge cases) |
| Whether top-level 3-stich must be ternary node | **open** (design choice) |
| Implemented in CURRENT | **no** — design only |

---

## 8. Bottom line

**How to parse poetry:** use the **poetic ta’amim system** of the Three books (ranks + glue + dichotomy), with **Job’s narrative frame as prose**, and keep literary parallelism as a secondary comment—not the tree engine.

**Next when you want code:** seed `ranks_poetry.yaml` + Job frame map + a handful of goldens under a new rule version.
