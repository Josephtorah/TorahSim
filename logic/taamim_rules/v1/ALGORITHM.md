# Ta'amim parse algorithm — v1 (prose)

**Version:** `v1`  
**System:** prose (Torah + Prophets + most Writings; not Psalms/Proverbs/Job poetry system)  
**Confidence:** hypothesis — seed; fix via version bump when golden tests fail  

Based on classical **continuous binary dichotomy** (Wickes-style ranks), not OSHB `n=` paths.

---

## Input

- Ordered list of **words** from one verse (OSHB `<w>` text, maqqef-segments as separate words if OSHB splits them).
- From each word string, extract **all** Unicode ta'amim in that word.
- Classify each mark as **disjunctive** or **conjunctive** per `ranks_prose.yaml`.
- **Word's structural mark:** if any disjunctive is present, use the **strongest** disjunctive (lowest rank number). Else if any conjunctive, use conjunctive. Else **zero_conjunctive** (binds like a conjunctive).

**Silluq:** U+05BD (meteg/silluq) on the **last word** of the verse is treated as **silluq** (rank 1). The same codepoint earlier in the verse is **meteg** (ignored for tree structure in v1).

**Sof pasuq** (U+05C3 `׃`) is verse end punctuation, not a word mark.

---

## Rank scale (prose)

Lower number = **stronger** break.

| Rank | Role (English) | Examples |
|------|----------------|----------|
| 1 | Emperors | silluq, etnachta |
| 2 | Kings | segol, shalshelet, zaqef_qatan, zaqef_gadol, tifcha |
| 3 | Dukes | revia, zarqa, pashta, yetiv, tevir |
| 4 | Officers | pazer, geresh, gershayim, telisha_gedola, qarney_para |
| 9 | Conjunctive / zero | munach, mercha, …, zero_conjunctive |

Full table: `ranks_prose.yaml`.

---

## Continuous binary dichotomy (deterministic)

For a non-empty span of words `W[0..n-1]`:

1. If `n == 1`: return a **leaf** node for that word.
2. Collect **interior split candidates**: indices `i` in `0 .. n-2` where `W[i]` has a **disjunctive** mark.
3. If **no** interior disjunctive:
   - Return a **phrase** node whose children are all leaves in order (conjunctive chain into the final word). Final word may still carry the domain-ending disjunctive.
4. Let `R` = minimum (strongest) rank among interior disjunctives.
5. Let `k` = **leftmost** index in `0 .. n-2` with disjunctive rank `R`.  
   (**v1 policy:** leftmost strongest interior break. If wrong on real verses, fix in v2 — do not special-case one verse.)
6. Split after word `k`:
   - `left = W[0..k]` (inclusive)
   - `right = W[k+1..n-1]`
7. Return binary **phrase** node: `children = [parse(left), parse(right)]`.

This is **fully deterministic**: same words + marks → same tree.

---

## Multi-mark / ambiguity

- **Per word:** multiple marks → strongest disjunctive wins (deterministic, not multi).
- **v1 does not** emit `status: multi` for grammar ambiguity (CFG multi-parse).  
  If later we need CYK multi-parse like Wu & Lowery, that is a **new version** with explicit multi output.

---

## Poetry

v1 **refuses** poetry system books unless `--system prose` is forced:

- Psalms, Proverbs, Job (poetic body) → `status: fail` with note to implement `ranks_poetry` in a later version.

---

## Failures

- Empty verse → `fail`
- Unknown Unicode mark in ta'amim block → `fail` listing codepoint (forces rule update)
- Poetry book without prose override → `fail`

---

## Changelog seed

| Ver | Note |
|-----|------|
| v1 | Initial prose continuous dichotomy; leftmost strongest interior split |
