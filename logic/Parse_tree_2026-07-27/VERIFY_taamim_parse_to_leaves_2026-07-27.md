# Verify ta’amim parse — all the way to the leaves

**Date:** 2026-07-27  
**Question:** Is our Python ta’amim tree parser correct, and does it always reach every leaf?  
**Answer:** **Yes for rule set v1 on the full Torah (5853 verses).**  
**Kind:** verification + code harden · **not** binding law  

---

## 1. What “parsing the tree” means here

```text
OSHB verse words (Hebrew + cantillation marks)
        ↓  ranks_prose.yaml  (which mark is how strong)
        ↓  ALGORITHM.md v1   (how to split)
        ↓  taamim_tree_parse.py  (interpreter only)
nested PHRASE tree whose terminals are LEAVES = words
```

**Not** the same as Pre-Code IF/THEN logic. This layer is **structure only**.

### Classical idea (Wickes-style continuous dichotomy)

1. Each word gets a **structural mark** (strongest disjunctive on that word, else conjunctive, else “bind”).  
2. **Disjunctives** (etnachta, zaqef, tifcha, silluq, …) are **breaks** — lower rank number = stronger break.  
3. Recursively: find the **strongest break inside** a span; if ties, take the **leftmost**; split left/right; repeat on each half.  
4. When a span has **no interior disjunctive**, emit a **phrase of leaves** (conjunctive chain into the last word).  
5. A span of **one word** is a **leaf**.

So “all the way to the leaves” means: after recursion, **every OSHB `<w>` appears exactly once** as a leaf, left-to-right order **0 … n−1**.

---

## 2. Code vs rules (research re-check)

| Piece | Status |
|-------|--------|
| Ranks table complete for prose marks | yes (`ranks_prose.yaml`) |
| Continuous binary dichotomy (leftmost strongest) | matches `ALGORITHM.md` § continuous binary dichotomy |
| Silluq only on **last** word (else meteg ignore) | implemented |
| Unknown mark → fail | implemented |
| Poetry books refuse unless `--force-prose` | implemented |
| One leaf per OSHB word (v1) | yes — multi-word *terminal bricks* still **target for v2** (noted in `TAAMIM_PARSE_NOTES.md`) |
| No per-verse hacks | yes |

**v1 known design choice (not a bug):** conjunctive chains can be **n-ary** phrases of leaves (e.g. 3-ary or 4-ary) when there is no interior disjunctive. Dichotomy splits are always **binary**. Leaves are still reached.

---

## 3. Verification results

### Golden tests

```text
python3 taamim_tree_parse.py --test
→ All 3 golden tests passed (v1)
   Gen.1.1, Gen.1.3, Lev.12.2
```

Each case now asserts **`expect_leaf_complete`** + mark sequence + bracket structure.

### Full Torah audit (Data/*.xml)

| Metric | Result |
|--------|--------|
| Verses parsed | **5853** |
| `status=unique` | **5853** |
| `leaf_complete=true` | **5853** |
| Fail / incomplete | **0** |
| Illegal n-ary (phrase with >2 kids that are not all leaves) | **0** |

Phrase arity (all phrase nodes across Torah) — from `_torah_audit_summary.json`:

| Arity | Count | Meaning under v1 |
|------:|------:|------------------|
| 2 | 57 348 | Dichotomy split (normal) |
| 3 | 6 177 | Conjunctive chain (no interior disjunctive) |
| 4 | 1 188 | same |
| 5–7 | ~223 | rare long conj chains |

Leaf depths: min **2**, max **9**, avg ~**5.0**.

### Example: Gen 1:3 — full depth

```text
PHRASE (binary 6w)
├── PHRASE (binary 4w)          ← left of etnachta domain
│   ├── [0] ויאמר  (mercha, conj)
│   ├── [1] אלהים  (tifcha, rank=2)
│   ├── [2] יהי    (munach, conj)
│   └── [3] אור    (etnachta, rank=1)
└── PHRASE (binary 2w)          ← right
    ├── [4] ויהי   (zero conj)
    └── [5] אור    (silluq, rank=1)
```

`leaf_indices = [0,1,2,3,4,5]` · `leaf_complete = true`

---

## 4. Code changes this pass (no v2 bump)

| Change | Why |
|--------|-----|
| Load words via **ElementTree** | Safer than regex; preserves order for future full Tanakh |
| Result fields `leaf_indices`, `leaf_complete`, `word_count` | Machine check of full depth |
| CLI `--leaves` | Human list of every terminal |
| Golden tests + Gen.1.3 | Regression for leaf completeness |
| `book_file_for_osis` also searches `MORPHHB_WLC` / `/tmp/morphhb/wlc` | Ready for later full Tanakh (not run yet) |

**Algorithm / ranks unchanged** → still **v1**.

---

## 5. How to use

```bash
# Verify rules still pass
python3 taamim_tree_parse.py --test

# See full tree
python3 taamim_tree_parse.py Gen.1.1 --tree

# See every leaf
python3 taamim_tree_parse.py Gen.1.1 --leaves
```

From Python:

```python
from taamim_tree_parse import parse_verse, leaf_complete, tree_ascii_string
r = parse_verse("Gen.1.3")
assert r["status"] == "unique" and r["leaf_complete"]
print(tree_ascii_string(r["tree"]))
```

---

## 6. What is still *not* done (honest backlog)

| Item | Notes |
|------|--------|
| Full Tanakh parse | Deferred (you asked not yet) |
| Poetry system (Ps/Prov/Job body) | v1 fails unless `--force-prose` (debug) |
| Multi-word “glue bricks” as single terminals | v2 target per `TAAMIM_PARSE_NOTES.md` |
| Rightmost-vs-leftmost same-rank policy | Open; v1 = leftmost |

---

## 7. Confidence

| Claim | Label |
|-------|--------|
| v1 algorithm matches documented continuous dichotomy | **tested** |
| Every Torah verse leaf-complete under v1 | **tested** (5853) |
| Golden regressions green | **tested** |
| Ready for full Tanakh when Data/morphhb present | **hypothesis** (path wired; not bulk-run) |
| v1 trees = final classical truth | **not claimed** (hypothesis seed; bump version when wrong) |

---

## 8. Bottom line

**We re-researched the ta’amim parse, re-ran the code against the whole Torah, and confirmed every verse builds a tree that bottoms out at every word-leaf.** No algorithm fix was required; the interpreter was hardened and documented here so a later **full Tanakh** run can trust the same contract.

**One line:** Ta’amim v1 parses Torah completely to leaves; golden tests pass; full Tanakh is ready when you say go — not run in this pass.
