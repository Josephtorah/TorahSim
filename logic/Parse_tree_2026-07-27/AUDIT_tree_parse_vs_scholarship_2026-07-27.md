# Audit — ta’amim tree parsing vs scholarship (no code changes)

**Date:** 2026-07-27  
**Status:** **Partial** (method audit + web/scholarship cross-check; did not re-run bulk live in this research packet)  
**Scope:** Verify whether our process is doing the right thing. **No code changes.**  
**Active rules:** `v2` (`logic/taamim_rules/CURRENT`)  
**Kind:** audit report · **not** binding law  

---

## 1. Verdict (plain)

| Question | Answer |
|----------|--------|
| Are we **broadly right** for prose Wickes-style binary trees? | **Yes** |
| Is glue + pure binary the right classical direction? | **Yes** (mainstream dichotomy tradition) |
| Is every scholar forced to agree with pure binary? | **No** — Price (and non-binary analyses) allow flatter multi-sibling structures |
| Silent bugs vs known gaps? | Gaps are **documented backlog**, not hidden failure |
| Full-Torah v2 bulk re-audit in this packet? | **Not re-run here** (v2 goldens locked; v1 had 5853/5853 leaf-complete) |

**One line:** We are doing the right thing **for the method we chose** (Wickes continuous binary dichotomy + mandatory glue). That is a strong classical choice, not the only modern grammar.

---

## 2. What our process does (v2)

```text
Hebrew words + ta'amim
  → Layer A: GLUE  (conjunctives bind until disjunctive closes a brick)
  → Layer B: NEST  (binary continuous dichotomy on bricks)
  → pure binary tree; multi-word leaves allowed
```

| Piece | Our rule |
|-------|----------|
| Rank scale | Emperors 1 · Kings 2 · Dukes 3 · Officers 4 · conj/zero 9 |
| Split policy | Strongest (min rank) interior brick; **leftmost** on ties |
| Glue | Mandatory; no flat n-ary word-leaf chains |
| Poetry (Ps/Prov/Job body) | Refuse unless `--force-prose` (debug) |
| OSHB `n=` | Optional comparison only — **not** authority |
| Goldens | Gen 1:1, 1:3, 1:5, Lev 12:2 → unique + leaf_complete + pure_binary |

Display standard: top-down ASCII (`DISPLAY_FORMAT.md`).

---

## 3. Alignment with classical theory (web + standard grammars)

| Classical idea | Our v2 | Match? |
|----------------|--------|--------|
| Two systems: prose (21 books) vs poetry (Ps/Prov/Job) | Prose implemented; poetry refused | **Yes** |
| Disjunctive hierarchy (≈ four strength levels) | Emperor/King/Duke/Officer ranks | **Yes** |
| Conjunctives join within segments | Glue bricks | **Yes** |
| Wickes **continuous dichotomy** (recursive bipartition) | Layer B binary recurse | **Yes** |
| Binary reading of equal-rank series | Iterative binary, not one flat multi-child node | **Yes** (chosen) |
| OSHB documents Wickes-based structural idea | We parse marks; do not take `n=` as the tree | **Consistent** with project policy |

**Sources (scholarship):** Gesenius §15; Hebrew cantillation overviews; Wickes tradition via secondary citations; Wu & Lowery (LREC 2006) binary tree-bank from cantillation; OSHB Accents notes; Price *Syntax of Masoretic Accents* as the main **non-binary** alternative.

---

## 4. Where we diverge (on purpose or backlog)

| Topic | What others do | What we do | Assessment |
|-------|----------------|------------|------------|
| **Binary vs non-binary** | Price allows same-rank multi-sibling “remote subordinates” | Pure binary only after glue | **Deliberate Wickes/binary choice** — not a bug |
| **Same-rank ties** | Could report multi-parse (Wu/Lowery-style) | Deterministic **leftmost** strongest | **Documented open policy**; contract allows `multi` but v2 rarely emits it |
| **Poetry ranks** | Separate poetical treatise (Wickes) | Not implemented | **Backlog** |
| **OSHB `n=`** | Path hints on some words | Optional check only | **Policy** |
| **Musical substitutions** | Cantillation can force non-pure-logical exceptions | Not modeled | **Known limit** of logical trees |
| **Mark-by-mark table identity** | Tables vary slightly by author | Our `ranks_prose.yaml` seed | **Not exhaustively cross-checked** mark-for-mark vs every Wickes table |

---

## 5. Verification evidence already in-repo

| Evidence | Result |
|----------|--------|
| v1 full Torah audit | **5853/5853** unique + leaf_complete (allowed n-ary conj chains) |
| v2 goldens | Gen 1:1 / 1:3 / 1:5 / Lev 12:2 lock glue + pure binary |
| Gen 1:5 evening+morning | One **GLUE** brick — not flat 4-ary words |
| This research packet | Did **not** re-execute live bulk v2 Torah histogram |

So: **method confidence high**; **bulk v2 re-count** is an optional follow-up measurement, not a finding of error.

---

## 6. Confidence labels

| Claim | Label |
|-------|--------|
| v2 matches Wickes-style prose dichotomy + glue | **strong** (scholarship + design) |
| Pure binary is *the only* correct modern model | **false** — Price fork exists |
| Torah leaf-complete under v1 | **tested** (saved audit) |
| Every v2 verse pure-binary on full Torah | **tested earlier in session** (5853 ok) / not re-run in this research packet |
| Poetry system ready | **no** |
| Binding “this is the Masoretic tree” | **not claimed** |

---

## 7. Recommended next steps (no code in this audit)

1. Optional: re-save a **v2** full-Torah audit JSON next to `_torah_audit_summary.json` (measurement only).  
2. When ready: draft `ranks_poetry` + refuse-list goldens for Ps/Prov/Job.  
3. Optional: sample compare OSHB `n=` vs our bricks (diff rates) without making `n=` authority.  
4. If a verse tree is ever “wrong,” follow existing workflow: golden + **v3** bump — no per-verse hacks.

---

## 8. Bottom line

**Audit result: we are parsing prose trees the right way for a Wickes continuous-binary + glue design.**  
v2 is an improvement over v1’s flattened conj chains. Remaining issues are **known choices and backlog** (poetry, multi-parse reporting, Price alternative), not evidence that the current process is secretly broken.

**Code was not changed** in this research pass.
