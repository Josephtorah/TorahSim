# Tree display mockup — FLAT → LAYERS → LEDGER

**Date:** 2026-07-27
**Kind:** display-format mockup (owner-requested exploration) · **not** binding law · **not** yet the locked canonical
**Rule set:** `v3` (`logic/taamim_rules/CURRENT`) — prose glue + binary dichotomy
**Interpreter:** `taamim_tree_parse.py` (repo root); all segmentation below is real parser output
**Locked display today:** `logic/TREE_DISPLAY.md` (top-down B# GLUE|ATOM). This mockup is a candidate **composite** format; adopting it requires an owner order.

**Related:**
- `../TREE_DISPLAY.md` — PERMANENT top-down B# template
- `../TREE_DISPLAY_LEAF_EN_HE_MORPH.md` — active `(en · he)` + morph chat format
- `../Parse_tree_2026-07-27/GLUE_BRICKS_v2_MANDATORY_2026-07-27.md` — why leaves are glue bricks
- `logic/taamim_rules/v3/ALGORITHM.md` — glue + dichotomy algorithm
- `logic/TREE_INTERPRETATION_RULES.md` — TIR ids (role labels below are **illustrative**, not frozen TIR)

---

## The format in one line

**FLAT** (full verse ×3 languages, parens = leaf bricks) → **LAYERS** (top-down, each layer splits left | right) → **LEDGER** (every leaf as a row: he · translit · en · mark · derivation · role).

---

# 1 · Gen 1:3 — clean demo

## 1.1 FLAT — full verse, parens around each leaf

```text
### FLAT  Gen.1.3 · taamim v3 · prose · 6 words → 3 bricks

he:  (וַיֹּ֥אמֶר אֱלֹהִ֖ים) (יְהִ֣י א֑וֹר) (וַֽיְהִי־אֽוֹר)
tr:  (va-yomer Elohim) (yehi or) (va-yehi or)
en:  (and God said) (let there be light) (and there was light)

       B0                B1              B2      ← reading order; Hebrew line runs right-to-left
```

## 1.2 LAYERS — from the top, each layer splits left | right

```text
LAYER 0 · ROOT · w0–5
   he: וַיֹּ֥אמֶר אֱלֹהִ֖ים יְהִ֣י א֑וֹר וַֽיְהִי־אֽוֹר
   tr: va-yomer Elohim yehi or va-yehi or
   en: "And God said, Let there be light — and there was light."

LAYER 1 · cut① etnachta r1 @w3 → ROOT splits
   LEFT  [L] w0–3
      he: וַיֹּ֥אמֶר אֱלֹהִ֖ים יְהִ֣י א֑וֹר
      tr: va-yomer Elohim yehi or
      en: "and God said: let there be light"
   RIGHT [R] w4–5  = (B2) ← LEAF: no disjunctive inside
      he: (וַֽיְהִי־אֽוֹר)
      tr: (va-yehi or)
      en: (and there was light)

LAYER 2 · cut② tifcha r2 @w1 → [L] splits
   LEFT  [LL] w0–1  = (B0) ← LEAF: only mercha (conj) inside
      he: (וַיֹּ֥אמֶר אֱלֹהִ֖ים)
      tr: (va-yomer Elohim)
      en: (and God said)
   RIGHT [LR] w2–3  = (B1) ← LEAF: only munach (conj) inside
      he: (יְהִ֣י א֑וֹר)
      tr: (yehi or)
      en: (let there be light)

DONE — every word inside exactly one paren: (B0)(B1)(B2)
```

## 1.3 LEAF LEDGER

| B# | words | path | he | translit | en | end mark · rank | froze because | role (illustrative) |
|----|-------|------|-----------------|-----------------|------------------------|-----------------|--------------------------------|----------------|
| B0 | w0–1 | L·L | וַיֹּ֥אמֶר אֱלֹהִ֖ים | va-yomer Elohim | and God said | tifcha · r2 | only conjunctive mercha inside | SPEAK(Elohim) |
| B1 | w2–3 | L·R | יְהִ֣י א֑וֹר | yehi or | let there be light | etnachta · r1 | only conjunctive munach inside | CMD(light) |
| B2 | w4–5 | R | וַֽיְהִי־אֽוֹר | va-yehi or | and there was light | silluq · r1 | no disjunctive inside | RESULT(light) |

---

# 2 · Lev 1:2 — scale test (21 words → 12 bricks, 5 layers)

## 2.1 FLAT

```text
### FLAT  Lev.1.2 · taamim v3 · prose · 21 words → 12 bricks

he:  (דַּבֵּ֞ר) (אֶל־בְּנֵ֤י יִשְׂרָאֵל֙) (וְאָמַרְתָּ֣ אֲלֵהֶ֔ם) (אָדָ֗ם) (כִּֽי־יַקְרִ֥יב מִכֶּ֛ם) (קָרְבָּ֖ן) (לַֽיהוָ֑ה)
     (מִן־הַבְּהֵמָ֗ה) (מִן־הַבָּקָר֙) (וּמִן־הַצֹּ֔אן) (תַּקְרִ֖יבוּ) (אֶת־קָרְבַּנְכֶֽם)

tr:  (dabber) (el-bnei Yisrael) (ve-amarta aleihem) (adam) (ki-yaqriv mikkem) (qorban) (la-YHWH)
     (min-ha-behemah) (min-ha-baqar) (u-min-ha-tzon) (taqrivu) (et-qorbankhem)

en:  (speak!) (to the children of Israel) (and say to them) (a person) (when he brings, from among you)
     (an offering) (to the LORD) (from the livestock) (from the herd) (and from the flock)
     (you shall bring) (your offering)

      B0 … B11 in reading order
```

## 2.2 LAYERS — inline `he / tr / "en"` form for long verses

```text
LAYER 0 · ROOT · w0–20
   דבר אל־בני ישראל ואמרת אלהם אדם כי־יקריב מכם קרבן ליהוה מן־הבהמה מן־הבקר ומן־הצאן תקריבו את־קרבנכם
   dabber el-bnei Yisrael ve-amarta aleihem adam ki-yaqriv mikkem qorban la-YHWH
   min-ha-behemah min-ha-baqar u-min-ha-tzon taqrivu et-qorbankhem
   "Speak to the children of Israel and say to them: a person, when he brings from among you
    an offering to the LORD — from the livestock, from the herd or the flock, you shall bring your offering."

LAYER 1 · cut① etnachta r1 @w11 (on לַֽיהוָ֑ה / la-YHWH)
   [L] w0–11   דבר…ליהוה / dabber…la-YHWH / "speak…an offering to the LORD"                    ← the case
   [R] w12–20  מן־הבהמה…קרבנכם / min-ha-behemah…qorbankhem / "from livestock…your offering"    ← the rule

LAYER 2
   cut② zaqef r2 @w5 → [L] splits
      [LL] w0–5    דבר אל־בני ישראל ואמרת אלהם / dabber el-bnei Yisrael ve-amarta aleihem / "speak to Israel and say to them"
      [LR] w6–11   אדם כי־יקריב מכם קרבן ליהוה / adam ki-yaqriv mikkem qorban la-YHWH / "a person who brings an offering to the LORD"
   cut③ zaqef r2 @w17 → [R] splits
      [RL] w12–17  מן־הבהמה מן־הבקר ומן־הצאן / min-ha-behemah min-ha-baqar u-min-ha-tzon / "from livestock: herd and flock"
      [RR] w18–20  תקריבו את־קרבנכם / taqrivu et-qorbankhem / "you shall bring your offering"

LAYER 3
   cut④ pashta r3 @w3 → [LL] splits
      [LLL] w0–3    דבר אל־בני ישראל / dabber el-bnei Yisrael / "speak to the children of Israel"
      (B2)  w4–5    ואמרת אלהם / ve-amarta aleihem / "and say to them"                    ← LEAF
   cut⑤ tifcha r2 @w10 → [LR] splits
      [LRL] w6–10   אדם כי־יקריב מכם קרבן / adam ki-yaqriv mikkem qorban / "a person who brings an offering"
      (B6)  w11     ליהוה / la-YHWH / "to the LORD"                                       ← LEAF
   cut⑥ revia r3 @w13 → [RL] splits
      (B7)  w12–13  מן־הבהמה / min-ha-behemah / "from the livestock"                      ← LEAF
      [RLR] w14–17  מן־הבקר ומן־הצאן / min-ha-baqar u-min-ha-tzon / "from herd and from flock"
   cut⑦ tifcha r2 @w18 → [RR] splits
      (B10) w18     תקריבו / taqrivu / "you shall bring"                                  ← LEAF
      (B11) w19–20  את־קרבנכם / et-qorbankhem / "your offering"                           ← LEAF

LAYER 4
   cut⑧ gershayim r4 @w0 → [LLL] splits
      (B0)  w0      דבר / dabber / "speak!"                                               ← LEAF
      (B1)  w1–3    אל־בני ישראל / el-bnei Yisrael / "to the children of Israel"          ← LEAF
   cut⑨ revia r3 @w6 → [LRL] splits
      (B3)  w6      אדם / adam / "a person"                                               ← LEAF
      [LRLR] w7–10  כי־יקריב מכם קרבן / ki-yaqriv mikkem qorban / "when he brings from you an offering"
   cut⑩ pashta r3 @w15 → [RLR] splits
      (B8)  w14–15  מן־הבקר / min-ha-baqar / "from the herd"                              ← LEAF
      (B9)  w16–17  ומן־הצאן / u-min-ha-tzon / "and from the flock"                       ← LEAF

LAYER 5
   cut⑪ tevir r3 @w9 → [LRLR] splits
      (B4)  w7–9    כי־יקריב מכם / ki-yaqriv mikkem / "when he brings, from among you"    ← LEAF
      (B5)  w10     קרבן / qorban / "an offering"                                         ← LEAF

DONE — 11 cuts → 12 leaves, every word in exactly one paren
```

## 2.3 LEAF LEDGER

| B# | words | path | he | translit | en | end mark · rank | froze because | role (illustrative) |
|----|-------|--------|-------------------|-------------------|-------------------------------|------------------|-----------------------------|------------------------------|
| B0 | w0 | L·L·L·L | דַּבֵּ֞ר | dabber | speak! | gershayim · r4 | single word | CMD(speak) — commission |
| B1 | w1–3 | L·L·L·R | אֶל־בְּנֵ֤י יִשְׂרָאֵל֙ | el-bnei Yisrael | to the children of Israel | pashta · r3 | no disjunctive inside | ADDRESSEE(Israel) |
| B2 | w4–5 | L·L·R | וְאָמַרְתָּ֣ אֲלֵהֶ֔ם | ve-amarta aleihem | and say to them | zaqef qatan · r2 | only munach inside | CMD(say) — relay |
| B3 | w6 | L·R·L·L | אָדָ֗ם | adam | a person | revia · r3 | single word | SUBJECT(person) |
| B4 | w7–9 | L·R·L·R·L | כִּֽי־יַקְרִ֥יב מִכֶּ֛ם | ki-yaqriv mikkem | when he brings, from among you | tevir · r3 | no disjunctive inside | TRIGGER — כי / ki / "when" |
| B5 | w10 | L·R·L·R·R | קָרְבָּ֖ן | qorban | an offering | tifcha · r2 | single word | OBJECT(offering) |
| B6 | w11 | L·R·R | לַֽיהוָ֑ה | la-YHWH | to the LORD | etnachta · r1 | single word | RECIPIENT — main verse rest |
| B7 | w12–13 | R·L·L | מִן־הַבְּהֵמָ֗ה | min-ha-behemah | from the livestock | revia · r3 | no disjunctive inside | SET(livestock) |
| B8 | w14–15 | R·L·R·L | מִן־הַבָּקָר֙ | min-ha-baqar | from the herd | pashta · r3 | no disjunctive inside | SUBSET(herd) |
| B9 | w16–17 | R·L·R·R | וּמִן־הַצֹּ֔אן | u-min-ha-tzon | and from the flock | zaqef qatan · r2 | no disjunctive inside | SUBSET(flock) |
| B10 | w18 | R·R·L | תַּקְרִ֖יבוּ | taqrivu | you shall bring | tifcha · r2 | single word | CMD(bring) |
| B11 | w19–20 | R·R·R | אֶת־קָרְבַּנְכֶֽם | et-qorbankhem | your offering | silluq · r1 | no disjunctive inside | OBJECT — את/*et* object-mark (TIR-014) |

---

# 3 · Are the marks doing the work? (yes — how)

Every combine and split above comes from the conjunctive/disjunctive marks via the v3 rules. Two steps:

**Step 1 — conjunctives combine (glue).** A word carrying a conjunctive mark (mercha, munach, …) or no accent glues forward to the next word bearing a disjunctive. Each maximal conjunctive run + its closing disjunctive word = one leaf (GLUE if multi-word, ATOM if alone). Gen 1:3 word by word:

| w | word (he / tr / en) | mark | kind | effect |
|---|------------|------------------|-------------|-------------------------------|
| 0 | וַיֹּאמֶר / va-yomer / and-said | mercha | conjunctive | glues forward → |
| 1 | אֱלֹהִים / Elohim / God | **tifcha** | disjunctive r2 | closes leaf **B0** |
| 2 | יְהִי / yehi / let-be | munach | conjunctive | glues forward → |
| 3 | אוֹר / or / light | **etnachta** | disjunctive r1 | closes leaf **B1** |
| 4 | וַיְהִי / va-yehi / and-was | (none — maqqef-bound) | treated conjunctive | glues forward → |
| 5 | אוֹר / or / light | **silluq** | disjunctive r1 | closes leaf **B2** |

**Step 2 — disjunctives split (binary dichotomy).** Over the fixed leaves, the strongest-ranked disjunctive in a span (leftmost on ties, ranks from `ranks_prose.yaml`) makes the cut; recurse into both halves. Hence cut① etnachta (r1) before cut② tifcha (r2).

History: v1 = word-level dichotomy, no glue (flat noisy trees). v2 made glue bricks **mandatory**. v3 = same prose algorithm + poetry ranks. Invariants checked every parse: `leaf_complete` (every word in exactly one brick), `pure_binary` (every internal node has two children).

**Mark-derived (reproducible):** leaf boundaries, parens, nesting, cut order — rerun `python3 taamim_tree_parse.py <ref> --tree`.
**Added human/logic layer (not from marks):** transliterations, English glosses, internal-node summaries, role labels (future TIR work).

---

# 4 · Design notes

- **Parens in FLAT** show the verse exactly as written, already segmented into bricks, in all three languages, before any tree drawing.
- **Cut numbering is layer order** (breadth-first: ① layer 1, ②③ layer 2, …) matching "break each layer down."
- **`path` column** (L·R strings) = directions from root to leaf; ties each ledger row to the LAYERS walk (B4 = left at etnachta, right at zaqef, left at tifcha, right at revia, left at tevir).
- **Two densities:** stacked `he:/tr:/en:` lines for short verses (§1.2); inline `he / tr / "en"` for long verses (§2.2).
- RTL caveat: Hebrew lines render right-to-left; parens may look flipped in some editors/terminals. B# guide line gives reading order.

**Status:** candidate format. If adopted as canonical chat display, update `logic/TREE_DISPLAY.md` + its checklist files on owner order and log in `reviews/STANDING_DECISIONS.md` changelog.
