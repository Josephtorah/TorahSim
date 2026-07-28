# Research: Theory 9 — root/family graph (re-score BR co-cites)

**Date:** 2026-07-26  
**Folder:** `reviews/br_link_studies/`  
**Theory:** T9 — cross-verse fabric is **root/consonant family** (and sound play), not Strong’s ID equality  
**Test:** Re-score all BR multi-cite co-edges by shared **root family** (Strong’s lemma → derivation chain → consonant root key)  
**Data:** `_verify_T9_root_family_2026-07-26.json` · morphhb WLC · Open Scriptures Strong’s Hebrew dict  
**Kind:** research · dual-track · **not** binding law  

---

## 0. Why this test

Earlier Strong’s-ID test (`VERIFY_br_unique_combos_2026-07-26.md`):

- BR co-cite edges almost never shared a **rare identical Strong’s** number  
- Flagship BR 1:1 *amon* lattice looked **unlinked** under Strong’s equality  
- But midrash clearly joins אָמוֹן / *amon* · אֹמֵן / *omen* · אֱמֻנִים / *emunim*  

**Hypothesis:** same **root family א־מ־ן** is the real glue; Strong’s splits the family into different IDs.

---

## 1. Method

1. Load Strong’s Hebrew dictionary (~8674 entries).  
2. Map each `H####` → **root key** = consonants of primitive lemma, following “from H…” derivation when present.  
   - Examples verified: H525, H539, H543, H529, H530, H571 → **אמנ**  
   - H216 → **אור** · H914 → **בדל** · H7225 → **ראש**  
3. For each Tanakh verse: set of content roots (drop roots appearing in >400 verses).  
4. For each BR co-cite edge (same section, two distinct refs):  
   - shared content **Strong’s**?  
   - shared content **roots**?  
   - **root-only** = root share without Strong’s share (Theory 9 “lift”)  
5. Baseline: 5000 random Tanakh verse pairs.

**Limit:** Root keys from Strong’s derivation, not a full morphological analyzer.  
**Limit:** Midrashic **sound play** across *unrelated* Strong’s roots (e.g. No-Amon H528) needs a second layer (see §5).

---

## 2. Results (headline numbers)

| Measure | BR co-cites (~12,891 edges) | Random pairs (5,000) |
|---------|----------------------------:|---------------------:|
| Any shared **content Strong’s** | **18.7%** | 2.4% |
| Any shared **content root** | **16.0%** | 2.2% |
| **Root share but no Strong’s share** (“T9 lift”) | **2.0%** (263 edges) | 0.8% |
| Shared root with corpus freq ≤3 | **0.1%** | — |
| Shared Strong’s n=1 | **0%** | — |

### Read carefully

1. **BR is still ~7–8× more linked than random** on both Strong’s and roots (18.7% / 16% vs ~2%). Something non-random is going on.  
2. **Root family does *not* massively increase overall share** vs Strong’s (16% < 18.7%). Most edges still share **nothing** content-like (~81–84%).  
3. **Theory 9 lift is real but small in bulk:** ~2% of edges are explained *only* when you step up from Strong’s ID to root family.  
4. That 2% includes the **classic petihah lattices** that made Strong’s look broken.

---

## 3. Flagship win: BR 1:1 *amon* lattice

Under Strong’s IDs, Prov 8:30 (H525) and Num 11:12 (H539) **do not share** a content Strong’s number.

Under **root אמנ**:

| Edge | Shared root | Notes |
|------|-------------|--------|
| Prov 8:30 ↔ Num 11:12 | **אמנ** | *amon* ↔ *omen* |
| Prov 8:30 ↔ Lam 4:5 | **אמנ** | *amon* ↔ *emunim* |
| Prov 8:30 ↔ Esth 2:7 | **אמנ** | *amon* ↔ *omen* |
| Num ↔ Lam ↔ Esth (pairs) | **אמנ** | full clique on 3 proofs |

**Theory 9 explains the petihah that Strong’s missed.**  
Corpus freq of root אמנ ≈ 366 verses (not rare globally) — so the link is **family membership**, not “unique password.”

### Nah 3:8 No-Amon — sound play beyond Strong’s root

| Form | Strong’s | Derivation in dict |
|------|----------|--------------------|
| אָמוֹן (Prov 8:30) | H525 | from H539 אמן (train/foster) |
| אָמוֹן in נֹא אָמוֹן | **H528** | **Egyptian** adjunct of No (H4996) — **not** from H539 |

So Nah 3:8 is linked by BR as **homograph / sound play**, not Strong’s-family derivation.  

```text
T9 full form needs TWO layers:
  T9a  morphological root family (Strong’s derivation)  ← this test
  T9b  midrashic sound / spelling play across families   ← Nah 3:8
```

**Label:** T9a **tested** on amon care-senses; T9b **required** for great-name sense.

---

## 4. Other root-only examples (same BR openings)

| BR | Pair | Shared root | Midrash job |
|----|------|-------------|-------------|
| 1:5 | Ps 31:19 ↔ Exod 4:11 | **אלמ** | mute / silence lattice |
| 1:5 | Exod 4:11 ↔ Gen 37:7 | **אלמ** | mute ↔ sheaves (*alumim*) — classic polyroot |
| 1:6 | Dan 2:22 ↔ Isa 4:6 / Ps 31:21 / Isa 29:15 | **סתר** | hide / cover package |
| 1:6 | Prov 9:18 ↔ Isa 30:33 / 29:15 | **עמק** | deep package |
| 1:8 | Ezek 40:3 ↔ Prov 8:22 | **קנה** | reed/measure ↔ acquire (*qanah*) — possible overlink |

These are exactly the **polyroot / package** openings where Strong’s ID equality failed and human readers see one family.

---

## 5. What Theory 9 does *not* claim (after the test)

| Claim | Verdict |
|-------|---------|
| Most BR co-cites share a root family | **Failed** (~84% still share no content root) |
| Root family ≫ Strong’s for bulk edges | **Failed** (bulk root share slightly *lower*) |
| Root family explains **flagship petihah lattices** | **Succeeded** |
| Root family = unique rare password | **Failed** (אמנ appears in hundreds of verses) |
| Strong’s derivation captures all midrash sound play | **Failed** (No-Amon H528) |

So T9 is **not** “the universal edge detector.”  
It is the **right identity layer for multi-sense petihot**.

---

## 6. How this fits the larger model

```text
CROSS-VERSE FABRIC (layered):

1. ROOT / SOUND FAMILY (T9)     — polyroot petihot, sense tables
2. STAGE / OPCODE EXPAND (T6)   — light/reishit thin header → later params
3. DUAL-RAIL PORTS (T4)         — complementary jobs, may share no root
4. BLOCK PIN (L5)               — cite opens contiguous procedure
5. THEME / STORY / METHOD       — residual majority of co-cites
6. ORAL MANUAL (T1)             — which layer BR is teaching this unit
```

**BR trains root-graph reading especially when it multi-reads one rare surface form.**  
It does **not** only walk the root graph for every citation.

---

## 7. Refined Theory 9 statement

**Before test:**  
“Real fabric is root family, not Strong’s; BR trains that graph.”

**After test:**

> **Morphological root family (T9a) is the correct identity for polyroot / multi-sense packages** (amon, ilem, satar…). It recovers BR 1:1-style lattices that Strong’s ID equality erased.  
> **It is not the majority co-cite glue** (~16% of edges; ~2% only recoverable via roots).  
> **Full midrash sound graph (T9b)** still exceeds Strong’s derivation (No-Amon).  
> **Code identity for those packages is family-level, re-entrant across books** — consistent with T6 expand and dual-track manual (T1).

**Label:**  
- T9 as *universal* BR edge law → **failed**  
- T9 as *best layer for polyroot petihot* → **tested / strong**  
- T9b sound-play layer → **hypothesis** (clear example, not full scan)

---

## 8. Confidence

| Claim | Label |
|-------|--------|
| Metrics above | **tested** |
| אמנ unifies Prov 8:30 + Num/Lam/Esth | **tested** |
| אלמ unifies mute/sheaves cluster | **tested** |
| Nah 3:8 needs sound play beyond Strong’s root | **tested** |
| Root family explains most BR links | **failed** |
| BR intentionally trains root-graph literacy | **strong hypothesis** |

---

## 9. Next tests (if continued)

1. **T9b:** homograph / same consonants ignoring Strong’s parent (catch No-Amon).  
2. Weight root share by **rarity × petihah-ness** (openers vs mid-section cites).  
3. Build **root lattice graphs** for top BR polyroots (אמן, אלם, סתר, אור, ראש).  
4. Cross with T6: root family = opcode id; instances expand parameters.

---

## 10. Bottom line

Re-scoring by root family **partially confirms Theory 9**:

- **Wins** where we needed it most (amon / ilem / hide packages).  
- **Does not** turn BR into a pure root co-occurrence graph.  
- Real picture: **root/sound lattice is one structural layer**, especially for multi-sense opens; most co-cites still use other layers (stage expand, dual-rail, story, method).

**Simple:** Strong’s said “different words.” Roots say “same family.” BR often teaches the **family**. That is real — and it is not the whole system.
