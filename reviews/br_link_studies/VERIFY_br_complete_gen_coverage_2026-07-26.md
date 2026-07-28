# Can BR give us every link we need?

**Date:** 2026-07-26  
**Claim under test:** Maybe BR cites **every Genesis verse that needs expansion** — a complete training set of expand-headers.  
**Kind:** verification design + first measurement · **not** binding law  
**Data:** `_br_gen_coverage.json` (tagged `<small>` cites only)

---

## 1. Two claims (do not mix them)

| Claim | Meaning |
|-------|---------|
| **C1** | BR cites **every Gen verse** at least once |
| **C2** | BR cites every Gen verse that **needs remote expansion** (complete expand-header index) |

C1 is easy to measure.  
C2 needs a definition of “needs expansion,” then tests.

---

## 2. How to verify

### Step A — Coverage map (done for tags)
- List all Gen verses (OSHB): **1533**  
- List Gen refs in BR `<small>(בראשית …)</small>` tags  
- Compute cited / uncited  

**Caveat:** BR often **quotes Genesis without a tag**. Tagged set = **lower bound** on “discussed,” **upper bound** on “explicit cite-graph node.”

### Step B — Operational “needs expansion”
A Gen verse is a **candidate expand-header** if several hold:

1. **Thin:** few parameters / short formula (create, divide, name, “and it was so,” day close)  
2. **Opcode-like:** clear op in tree L‖R  
3. **Gaps:** who/moral/duration/future underspecified  
4. **Remote family exists:** later Tanakh reuses same root+role with more fields  

Gold training: Gen 1:3–5 light (we already know expands).

### Step C — Tests against C2

| Test | If C2 true | If C2 false |
|------|------------|-------------|
| **T-complete** | Every candidate expand-header is BR-cited | Some thin headers uncited |
| **T-sound** | Almost every BR Gen cite is expand-header or its package land | Many cites are story-only (no expand gap) |
| **T-expand** | Uncited Gen verses lack good remote expands | Uncited thin verses still have clear remote expands |
| **T-manual** | BR packages are necessary for discovery | Method alone finds same packages without BR |

### Step D — Controls
- Random uncited long narrative verses should rarely look like Class A headers.  
- Day-close formulas and *vayehi ken* lines are good Class A probes.

---

## 3. Measurement so far (tagged cites)

| Metric | Value |
|--------|------:|
| Genesis verses total | **1533** |
| Cited ≥1× in BR tags | **1111 (72.5%)** |
| Never tagged | **422 (27.5%)** |
| Gen cite events (tags) | **2479** |

**C1 is false** for tagged cites: BR does **not** cite every Gen verse.

### Gen 1 (create week) — critical for expand theory

| Ref | BR tagged? | Words | Expand-header candidate? |
|-----|------------|------:|--------------------------|
| 1:1 | yes (4) | 7 | yes (*reishit*) |
| 1:2 | yes (5) | 14 | partial |
| 1:3–5 | yes | 6–13 | **yes (light package)** |
| 1:6 | yes | 11 | yes (firmament divide) |
| **1:7** | **no** | 17 | **yes** — makes firmament, divide waters, *vayehi ken* |
| **1:8** | **no** | 10 | **yes** — name shamayim; day two close |
| 1:9 | yes | 13 | yes (gather waters) |
| **1:10** | **no** | 12 | **yes** — name earth/seas; *ki tov* |
| 1:11–12 | yes | … | plants |
| **1:13** | **no** | 6 | day-close formula |
| 1:14–17 | yes | … | luminaries |
| **1:18** | **no** | 12 | luminaries rule + *ki tov* (echo 1:4) |
| **1:19** | **no** | 6 | day-close |
| 1:20–21 | yes | … | swarm |
| **1:22–23** | **no** | … | bless / day-close |
| 1:24–26 | yes | … | land creatures / image |
| **1:27** | **no** | 13 | **yes** — create adam in image (core!) |
| 1:28 | yes | 22 | bless/rule |
| **1:29–30** | **no** | 27/21 | food grant |
| 1:31 | yes (6) | 15 | very good; day six |

**Gen 1 tagged coverage: 20/31 (65%).**

### Top BR Gen cites (not only “needs expand”)

Heavy traffic includes **story hubs**:  
Gen 32:4, 18:19, 12:1, 22:2, 27:33, 25:23, 28:10–12…  

So BR also indexes **narrative runtime**, not only thin cosmic headers.

---

## 4. What this means for “every link we need”

### Against “BR lists every Gen verse”
**Falsified** for tags (27.5% never appear). Even Gen 1 is incomplete.

### Against “BR lists every verse that needs expansion”
**Strongly challenged** by Gen 1 counterexamples:

| Uncited (tags) | Why it still “needs expand” / is thin header-ish |
|----------------|--------------------------------------------------|
| **1:7** | Actual making of firmament + water divide + **וַיְהִי כֵן** |
| **1:8** | Name heavens + day-two close |
| **1:10** | Name earth/seas + good |
| **1:18** | Luminaries rule day/night + good (pairs 1:4) |
| **1:27** | Image creation (major opcode) |

If expansion matters for firmament/image/names, **BR’s tagged cite set is not a complete expand index**.

### Softening (fair to BR)
1. BR may **discuss** 1:7/1:27 via bare quotes without tags → tagged coverage undercounts.  
2. Neighbor cites (1:6, 1:9, 1:26, 1:28) may **cover the block** without tagging every verse.  
3. “Needs expansion” is graded, not binary.

Even then: BR is better read as **dense sampling of hubs + methods**, not a proven complete catalog of expand-headers.

---

## 5. How to finish verification (next hard tests)

1. **Bare-quote pass:** detect untagged Genesis lemmata in BR Hebrew for uncited Gen 1 verses.  
   - **Done (partial, Gen 1):** 1:7/1:8/1:10/1:13/1:27 bare-contaminated; **1:19/1:22/1:23/1:29/1:30 clean**. See [EXPLORE_uncited_gen_expand_full_tanakh_2026-07-26.md](EXPLORE_uncited_gen_expand_full_tanakh_2026-07-26.md).  
2. **Block coverage:** if any verse in Gen 1:6–8 block is cited, count block “touched.”  
3. **Expand probe without BR:** for uncited headers, search remote root+role expands; if rich expands exist, C2 fails harder.  
   - **Done for clean header Gen 1:22:** full Tanakh multi-lemma expands (1:28, 9:1, 17:20, Exod 1:7, …) without any BR mention of 1:22. **C2 fails** for this counterexample.  
4. **Soundness:** sample 50 high-cite Gen verses; score how many are Class A expand-headers vs pure narrative.  
5. **Compare Oral peers:** does another midrash fill Gen gaps BR tags miss?

---

## 6. Best working answer

| Question | Answer |
|----------|--------|
| Does BR give every link we need? | **Unlikely as a complete dump** — 27%+ Gen verses untagged; Gen 1 incomplete. |
| Does BR cite every Gen verse that needs expansion? | **Probably not** — firmament make/name, image create, some day-closes untagged but expand-like. |
| What does BR give? | **High-coverage training set** (~¾ of Gen tagged) + **methods** (polyroot, dual-rail, blocks) + **package examples** (light, *reishit*). |
| How we verify completeness | Coverage map + Class A definition + counterexamples + bare-quote check + expand-without-BR probes. |

**One line:**  
BR is a **rich tutorial**, not a proven **complete expand index**; we verify by measuring Gen coverage and hunting **thin uncited headers that still expand**.

---

## 7. Confidence

| Claim | Label |
|-------|--------|
| 72.5% Gen tagged cite coverage | **tested** (tags only) |
| C1 false for tags | **tested** |
| Gen 1:7, 1:10, 1:18, 1:27 untagged | **tested** |
| Those are expand-headers | **hypothesis** (strong for 1:7, 1:27) |
| C2 false | **tested** on counterexample Gen 1:22 (clean unmentioned + rich Tanakh expands) |
| Gen 1:22 clean unmentioned expand-header | **tested** (tags + bare) |
| BR still best training set we have | **strong hypothesis** |
