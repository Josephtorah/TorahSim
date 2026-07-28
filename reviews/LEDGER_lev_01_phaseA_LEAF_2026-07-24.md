# Phase A (redo) — Leviticus 1 leaf-level phrase ledger

**Date:** 2026-07-24  
**Kind:** finite free-phrase inventory — **Written only** · **leaf-level**  
**Status:** Phase A **redone** — supersedes top-split-only `LEDGER_lev_01_phrases_phaseA_2026-07-24.md`  
**Not yet:** Phase B write-sites · Oral · dry-runner  

**Related:** `REGISTRY_sanctuary_v0_2026-07-24.md` · `logic/TAAMIM_TREE_PARSER.md` · `taamim_tree_parse.py` v1 · `Data/Lev.xml`

On substantive update: rename to today’s date and fix links.

---

## 0. What changed (why redo)

| Old Phase A | This redo |
|-------------|-----------|
| Only **top** LEFT/RIGHT of the verse | **Every leaf** + full path in the tree |
| Marks used to build tree, then ignored in the table | **Every leaf keeps its cantillation mark + rank** |
| Variables ≈ “phrase somewhere on half-verse” | Variables = **Hebrew on specific leaves / multi-leaf paths** |

**Rule:** Variable names come from **Hebrew surfaces on leaves** (and multi-leaf spans the tree groups). English is gloss only. No Oral in this phase.

---

## 1. Method (leaf-level)

```text
For each Lev 1:1–17:
  1. Read all words + all cantillation marks from Data/Lev.xml
  2. Parse full ta'amim tree (rule_set_version v1) — every mark participates
  3. Walk every LEAF: index, he, mark_id, rank, path from root
  4. Record flat constituents (parent whose children are all leaves)
  5. Derive VAR_* only from Hebrew on those leaves/spans
```

### Path notation (how to read the tree address)

From the **root** of the verse tree:

| Symbol | Meaning |
|--------|---------|
| `L` | go to left child of a binary split |
| `R` | go to right child of a binary split |
| `C0`, `C1`, … | child index when the node is a **flat chain** (3+ leaves, no interior disjunctive) |

Example (Lev 1:5): `RLLRC2` = root→Right→Left→Left→Right→child2 → leaf **הכהנים** / *ha-kohanim* / “the priests” (pashta).

### Rank scale (v1 prose)

| Rank | Role | Examples |
|-----:|------|----------|
| 1 | Emperors (strongest breaks) | etnachta, silluq |
| 2 | Kings | zaqef qatan, tifcha, … |
| 3 | Dukes | pashta, tevir, revia, … |
| 4 | Officers | telisha gedola, geresh, … |
| 9 | Conjunctive / glue | munach, mercha, qadma, zero (no mark) |

**Parser status:** all 17 verses `unique` under v1.

**Scale:** 252 leaves across 17 verses; 98 variable occurrences; 44 unique variable ids.

---

## 2. Variable catalog (derived from leaves)

Each `VAR_*` id is a handle. The real name is the **Hebrew** column.

| var_id | Hebrew form(s) | Translit (letter-map) | English gloss | Kind | Lev 1 verses | Sample path(s) |
|--------|----------------|----------------------|---------------|------|--------------|----------------|
| `VAR_benei_aharon` | בני אהרן | bny 'hrn | sons of Aaron | install | 5, 7, 8, 11 | `LLLRC`, `LLRL`, `RLLRC` |
| `VAR_ha_kohanim` | הכהנים | hkhnym | the priests | install | 5, 8, 11 | `LLRR`, `RLLRC2` |
| `VAR_ha_kohen` | הכהן | hkhn | the priest | install | 7, 9, 12, 13, 15, 17 | `LLLR`, `LLLRC2`, `LRLLC2`, `RLLC1`, … |
| `VAR_ha_mizbeach` | המזבח | hmzbch | the altar | install | 5, 7, 8, 11, 12, 15, 16 | `LLRR`, `LRR`, `RLLRR`, `RLRR`, … |
| `VAR_ha_mizbechah` | המזבחה | hmzbchh | onto the altar | install | 9, 13, 15, 17 | `LRLR`, `LRRR`, `RLR`, `RLRR` |
| `VAR_kir_ha_mizbeach` | קיר המזבח | qyr hmzbch | wall of the altar | install | 15 | `RRR` |
| `VAR_me_ohel_moed` | מאהל מועד | m'hl mv'd | from the Tent of Meeting | install | 1 | `RRL` |
| `VAR_petach_ohel_moed` | פתח אהל מועד | ptch 'hl mv'd | entrance of the Tent of Meeting | install | 3, 5 | `RLL`, `RRR` |
| `VAR_yerech_ha_mizbeach` | ירך המזבח | yrk hmzbch | side of the altar | install | 11 | `LLLRC` |
| `VAR_lifnei_YHWH` | לפני יהוה | lpny yhvh | before YHWH | presence | 3, 5, 11 | `LR`, `RRR` |
| `VAR_YHWH` | יהוה | yhvh | YHWH | divine | 1 | `RLLR` |
| `VAR_la_YHWH` | ליהוה | lyhvh | to/for YHWH | divine | 2, 9, 13, 14, 17 | `LR`, `LRR`, `RR`, `RRR` |
| `VAR_adam` | אדם | 'dm | person | agent | 2 | `LRLL` |
| `VAR_mosheh` | משה | mshh | Moses | agent | 1 | `LRR` |
| `VAR_benei_yisrael` | בני ישראל | bny yshr'l | children of Israel | people | 2 | `LLLRC` |
| `VAR_ben_ha_bakar` | בן הבקר | bn hbqr | cattle young | type | 5 | `LLRC` |
| `VAR_benei_ha_yonah` | בני היונה | bny hyvnh | young pigeons | type | 14 | `RLRRC` |
| `VAR_ha_bakar` | הבקר | hbqr | cattle | type | 2, 3 | `LLRR`, `RLRLR` |
| `VAR_ha_behemah` | הבהמה | hbhmh | domestic animal class | type | 2 | `RLLR` |
| `VAR_ha_of` | העוף | h'vp | bird | type | 14 | `LLLC2` |
| `VAR_ha_olah` | העלה | h'lh | the burnt offering | type | 4, 6 | `LRR`, `LRRR` |
| `VAR_ha_torim` | התרים | htrym | turtledoves | type | 14 | `RLLC2` |
| `VAR_ha_tzon` | הצאן | htz'n | flock | type | 2, 10 | `LLLC2`, `RLRRR` |
| `VAR_isheh` | אשה | 'shh | fire-offering | type | 9, 13, 17 | `RLRL`, `RRLRC0`, `RRLRL` |
| `VAR_korban` | קרבן | qrbn | offering | type | 2 | `LRLRR` |
| `VAR_korbankhem` | קרבנכם | qrbnkm | your offering | type | 2 | `RRRR` |
| `VAR_korbano` | קרבנו | qrbnv | his offering | type | 3, 10, 14 | `LLLC2`, `LLLC3`, `LLRR`, `RRR` |
| `VAR_le_olah` | לעלה | l'lh | as burnt offering | type | 10 | `LR` |
| `VAR_olah` | עלה | 'lh | burnt offering | type | 3, 9, 13, 14, 17 | `LLLC1`, `LLRL`, `RLLL`, `RRLL`, … |
| `VAR_damo` | דמו | dmv | its blood | substance | 11, 15 | `RLLRC4`, `RLR` |
| `VAR_esh` | אש | 'sh | fire | substance | 7 | `LLR` |
| `VAR_etzim` | עצים | 'tzym | wood | substance | 7 | `RLR` |
| `VAR_ha_dam` | הדם | hdm | the blood | substance | 5 | `RLRR`, `RRLLC2` |
| `VAR_ha_esh` | האש | h'sh | the fire | substance | 7, 8, 12, 17 | `LRRRC2`, `RLRC2`, `RRLRC2`, `RRR` |
| `VAR_ha_etzim` | העצים | h'tzym | the wood | substance | 8, 12, 17 | `LRRLR`, `RLLR`, `RRLLR` |
| `VAR_hiktir` | והקטיר | vhqtyr | turn to smoke | act | 9, 13, 15, 17 | `LRLLC0`, `LRRL`, `RLLC0`, `RLRL` |
| `VAR_samakh` | וסמך | vsmk | lean hand | act | 4 | `LLL` |
| `VAR_shachat` | ושחט | vshcht | slaughter | act | 5, 11 | `LLL`, `LLLLL` |
| `VAR_zarak` | וזרקו | vzrqv | dash blood | act | 5, 11 | `RLLL`, `RRLLC0` |
| `VAR_tamim` | תמים | tmym | unblemished | guard | 3, 10 | `LRLR`, `RLR` |
| `VAR_zakhar` | זכר | zkr | male | guard | 3, 10 | `LRLL`, `RLL` |
| `VAR_reach_nichoach` | ריח ניחוח · ריח ניחח | rych nychvch · rych nychch | pleasing aroma | formula | 9, 13, 17 | `RLRR`, `RRLRC`, `RRLRR` |
| `VAR_mekom_ha_deshen` | מקום הדשן | mqvm hdshn | place of the ashes | place | 16 | `RR` |
| `VAR_tzafonah` | צפנה | tzpnh | northward | place | 11 | `LLR` |

### Kind counts

| Kind | # unique vars |
|------|--------------:|
| install | 9 |
| presence | 1 |
| divine | 2 |
| agent | 2 |
| people | 1 |
| type | 14 |
| substance | 6 |
| act | 4 |
| guard | 2 |
| formula | 1 |
| place | 2 |

---

## 3. How a variable is “born” from leaves (worked Lev 1:5)

Full leaf walk for the densest sanctuary verse:

| i | path | rank | mark | Hebrew | Translit | English | VAR |
|--:|------|-----:|------|--------|----------|---------|-----|
| 0 | `LLL` | 3 | tevir | ושחט | vshcht | and he shall slaughter | `VAR_shachat` |
| 1 | `LLRC0` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 2 | `LLRC1` | 9 | mercha | בן | bn | son of | `VAR_ben_ha_bakar` |
| 3 | `LLRC2` | 2 | tifcha | הבקר | hbqr | the cattle | `VAR_ben_ha_bakar` |
| 4 | `LRL` | 9 | munach | לפני | lpny | before | `VAR_lifnei_YHWH` |
| 5 | `LRR` | 1 | etnachta | יהוה | yhvh | YHWH | `VAR_lifnei_YHWH` |
| 6 | `RLLL` | 4 | telisha_gedola | והקריבו | vhqrybv | and he shall bring it near | — |
| 7 | `RLLRC0` | 9 | qadma | בני | bny | sons of | `VAR_benei_aharon` |
| 8 | `RLLRC1` | 9 | mahpach | אהרן | 'hrn | Aaron | `VAR_benei_aharon` |
| 9 | `RLLRC2` | 3 | pashta | הכהנים | hkhnym | the priests | `VAR_ha_kohanim` |
| 10 | `RLRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 11 | `RLRR` | 2 | zaqef_qatan | הדם | hdm | the blood | `VAR_ha_dam` |
| 12 | `RRLLC0` | 9 | qadma | וזרקו | vzrqv | and they shall dash | `VAR_zarak` |
| 13 | `RRLLC1` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 14 | `RRLLC2` | 9 | mahpach | הדם | hdm | the blood | `VAR_ha_dam` |
| 15 | `RRLLC3` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 16 | `RRLLC4` | 3 | pashta | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 17 | `RRLR` | 2 | zaqef_qatan | סביב | sbyb | around | — |
| 18 | `RRRLL` | 9 | zero_conjunctive | אשר | 'shr | which/that | — |
| 19 | `RRRLR` | 2 | tifcha | פתח | ptch | entrance of | `VAR_petach_ohel_moed` |
| 20 | `RRRRL` | 9 | mercha | אהל | 'hl | tent of | `VAR_petach_ohel_moed` |
| 21 | `RRRRR` | 1 | silluq | מועד | mv'd | meeting | `VAR_petach_ohel_moed` |

**Flat constituents** (tree groups whose children are all leaves — natural “chunks”):

| path | head mark | Hebrew chunk |
|------|-----------|--------------|
| `LLR` | tifcha | את בן הבקר |
| `LR` | etnachta | לפני יהוה |
| `RLLR` | pashta | בני אהרן הכהנים |
| `RLR` | zaqef_qatan | את הדם |
| `RRLL` | pashta | וזרקו את הדם על המזבח |
| `RRRL` | tifcha | אשר פתח |
| `RRRR` | silluq | אהל מועד |

**Reading (hypothesis, still Written-only):**

- `LLL` **ושחט** / *ve-shachat* / “slaughter” — act leaf (tevir).
- `LLRC*` **בן הבקר** / *ben ha-bakar* / “cattle young” — multi-leaf type under tifcha domain.
- `LR` **לפני יהוה** / *lifnei YHWH* / “before YHWH” — presence pair ending in **etnachta** (top mid-verse).
- `RLLRC*` **בני אהרן הכהנים** / *benei Aharon ha-kohanim* — operator chunk (pashta domain); vars `VAR_benei_aharon` + `VAR_ha_kohanim`.
- `RLR` **את הדם** / *et ha-dam* / blood object (zaqef).
- `RRLL` **וזרקו את הדם על המזבח** — dash blood on altar (pashta domain).
- `RRR*` **פתח אהל מועד** — entrance of Tent (tifcha + mercha + **silluq**).

This is **leaf-level** structure: same verse as before, but variable sites have **addresses** and **marks**, not only “RIGHT half.”

---

## 4. Verse-by-verse: all leaves + variables

### Lev 1:1

- **Words:** 9 · **parser:** unique · **rules:** v1
- **Linear (plain):** ויקרא אל משה וידבר יהוה אליו מאהל מועד לאמר
- **Linear (translit):** vyqr' 'l mshh vydbr yhvh 'lyv m'hl mv'd l'mr

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LL` | 2 | tifcha | ויקרא | vyqr' | and He called | — |
| 1 | `LRL` | 9 | zero_conjunctive | אל | 'l | to/toward | — |
| 2 | `LRR` | 1 | etnachta | משה | mshh | Moses | `VAR_mosheh` |
| 3 | `RLLL` | 9 | mahpach | וידבר | vydbr | and He spoke | — |
| 4 | `RLLR` | 3 | pashta | יהוה | yhvh | YHWH | `VAR_YHWH` |
| 5 | `RLR` | 2 | zaqef_qatan | אליו | 'lyv | to him | — |
| 6 | `RRLL` | 9 | mercha | מאהל | m'hl | from (the) tent of | `VAR_me_ohel_moed` |
| 7 | `RRLR` | 2 | tifcha | מועד | mv'd | meeting | `VAR_me_ohel_moed` |
| 8 | `RRR` | 1 | silluq | לאמר | l'mr | saying | — |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_me_ohel_moed` | מאהל מועד | `RRL` | tifcha | mercha,tifcha |
| `VAR_mosheh` | משה | `LRR` | etnachta | etnachta |
| `VAR_YHWH` | יהוה | `RLLR` | pashta | pashta |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LR` | etnachta | אל משה |
| `RLL` | pashta | וידבר יהוה |
| `RRL` | tifcha | מאהל מועד |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 9w) וַ/יִּקְרָ֖א אֶל מֹשֶׁ֑ה וַ/יְדַבֵּ֤ר יְהוָה֙ א…
├── PHRASE (binary 3w) וַ/יִּקְרָ֖א אֶל מֹשֶׁ֑ה
│   ├── [0] וַ/יִּקְרָ֖א (tifcha, rank=2)
│   └── PHRASE (binary 2w) אֶל מֹשֶׁ֑ה
│       ├── [1] אֶל (no cantillation mark — bind as conjunctive, rank=9)
│       └── [2] מֹשֶׁ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 6w) וַ/יְדַבֵּ֤ר יְהוָה֙ אֵלָ֔י/ו מֵ/אֹ֥הֶל מוֹעֵ֖ד…
    ├── PHRASE (binary 3w) וַ/יְדַבֵּ֤ר יְהוָה֙ אֵלָ֔י/ו
    │   ├── PHRASE (binary 2w) וַ/יְדַבֵּ֤ר יְהוָה֙
    │   │   ├── [3] וַ/יְדַבֵּ֤ר (mahpach (conjunctive), rank=9)
    │   │   └── [4] יְהוָה֙ (pashta, rank=3)
    │   └── [5] אֵלָ֔י/ו (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) מֵ/אֹ֥הֶל מוֹעֵ֖ד לֵ/אמֹֽר
        ├── PHRASE (binary 2w) מֵ/אֹ֥הֶל מוֹעֵ֖ד
        │   ├── [6] מֵ/אֹ֥הֶל (mercha (conjunctive), rank=9)
        │   └── [7] מוֹעֵ֖ד (tifcha, rank=2)
        └── [8] לֵ/אמֹֽר (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:2

- **Words:** 21 · **parser:** unique · **rules:** v1
- **Linear (plain):** דבר אל בני ישראל ואמרת אלהם אדם כי יקריב מכם קרבן ליהוה מן הבהמה מן הבקר ומן הצאן תקריבו את קרבנכם
- **Linear (translit):** dbr 'l bny yshr'l v'mrt 'lhm 'dm ky yqryb mkm qrbn lyhvh mn hbhmh mn hbqr vmn htz'n tqrybv 't qrbnkm

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLL` | 4 | gershayim | דבר | dbr | speak | — |
| 1 | `LLLRC0` | 9 | zero_conjunctive | אל | 'l | to/toward | — |
| 2 | `LLLRC1` | 9 | mahpach | בני | bny | sons of | `VAR_benei_yisrael` |
| 3 | `LLLRC2` | 3 | pashta | ישראל | yshr'l | Israel | `VAR_benei_yisrael` |
| 4 | `LLRL` | 9 | munach | ואמרת | v'mrt | and you shall say | — |
| 5 | `LLRR` | 2 | zaqef_qatan | אלהם | 'lhm | to them | — |
| 6 | `LRLL` | 3 | revia | אדם | 'dm | a person | `VAR_adam` |
| 7 | `LRLRLC0` | 9 | zero_conjunctive | כי | ky | when/if/that | — |
| 8 | `LRLRLC1` | 9 | mercha | יקריב | yqryb | he shall bring near | — |
| 9 | `LRLRLC2` | 3 | tevir | מכם | mkm | from you | — |
| 10 | `LRLRR` | 2 | tifcha | קרבן | qrbn | offering | `VAR_korban` |
| 11 | `LRR` | 1 | etnachta | ליהוה | lyhvh | to YHWH | `VAR_la_YHWH` |
| 12 | `RLLL` | 9 | zero_conjunctive | מן | mn | from | — |
| 13 | `RLLR` | 3 | revia | הבהמה | hbhmh | the animal | `VAR_ha_behemah` |
| 14 | `RLRLL` | 9 | zero_conjunctive | מן | mn | from | — |
| 15 | `RLRLR` | 3 | pashta | הבקר | hbqr | the cattle | `VAR_ha_bakar` |
| 16 | `RLRRL` | 9 | zero_conjunctive | ומן | vmn | and from | — |
| 17 | `RLRRR` | 2 | zaqef_qatan | הצאן | htz'n | the flock | `VAR_ha_tzon` |
| 18 | `RRL` | 2 | tifcha | תקריבו | tqrybv | you shall bring near | — |
| 19 | `RRRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 20 | `RRRR` | 1 | silluq | קרבנכם | qrbnkm | your offering | `VAR_korbankhem` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_benei_yisrael` | בני ישראל | `LLLRC` | pashta | mahpach,pashta |
| `VAR_adam` | אדם | `LRLL` | revia | revia |
| `VAR_korban` | קרבן | `LRLRR` | tifcha | tifcha |
| `VAR_la_YHWH` | ליהוה | `LRR` | etnachta | etnachta |
| `VAR_ha_behemah` | הבהמה | `RLLR` | revia | revia |
| `VAR_ha_bakar` | הבקר | `RLRLR` | pashta | pashta |
| `VAR_ha_tzon` | הצאן | `RLRRR` | zaqef_qatan | zaqef_qatan |
| `VAR_korbankhem` | קרבנכם | `RRRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLLR` | pashta | אל בני ישראל |
| `LLR` | zaqef_qatan | ואמרת אלהם |
| `LRLRL` | tevir | כי יקריב מכם |
| `RLL` | revia | מן הבהמה |
| `RLRL` | pashta | מן הבקר |
| `RLRR` | zaqef_qatan | ומן הצאן |
| `RRR` | silluq | את קרבנכם |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 21w) דַּבֵּ֞ר אֶל בְּנֵ֤י יִשְׂרָאֵל֙ וְ/אָמַרְתָּ֣ …
├── PHRASE (binary 12w) דַּבֵּ֞ר אֶל בְּנֵ֤י יִשְׂרָאֵל֙ וְ/אָמַרְתָּ֣ …
│   ├── PHRASE (binary 6w) דַּבֵּ֞ר אֶל בְּנֵ֤י יִשְׂרָאֵל֙ וְ/אָמַרְתָּ֣ …
│   │   ├── PHRASE (binary 4w) דַּבֵּ֞ר אֶל בְּנֵ֤י יִשְׂרָאֵל֙
│   │   │   ├── [0] דַּבֵּ֞ר (gershayim, rank=4)
│   │   │   └── PHRASE (3-ary 3w) אֶל בְּנֵ֤י יִשְׂרָאֵל֙
│   │   │       ├── [1] אֶל (no cantillation mark — bind as conjunctive, rank=9)
│   │   │       ├── [2] בְּנֵ֤י (mahpach (conjunctive), rank=9)
│   │   │       └── [3] יִשְׂרָאֵל֙ (pashta, rank=3)
│   │   └── PHRASE (binary 2w) וְ/אָמַרְתָּ֣ אֲלֵ/הֶ֔ם
│   │       ├── [4] וְ/אָמַרְתָּ֣ (munach (conjunctive), rank=9)
│   │       └── [5] אֲלֵ/הֶ֔ם (zaqef qatan, rank=2)
│   └── PHRASE (binary 6w) אָדָ֗ם כִּֽי יַקְרִ֥יב מִ/כֶּ֛ם קָרְבָּ֖ן לַֽ/י…
│       ├── PHRASE (binary 5w) אָדָ֗ם כִּֽי יַקְרִ֥יב מִ/כֶּ֛ם קָרְבָּ֖ן
│       │   ├── [6] אָדָ֗ם (revia, rank=3)
│       │   └── PHRASE (binary 4w) כִּֽי יַקְרִ֥יב מִ/כֶּ֛ם קָרְבָּ֖ן
│       │       ├── PHRASE (3-ary 3w) כִּֽי יַקְרִ֥יב מִ/כֶּ֛ם
│       │       │   ├── [7] כִּֽי (no cantillation mark — bind as conjunctive, rank=9)
│       │       │   ├── [8] יַקְרִ֥יב (mercha (conjunctive), rank=9)
│       │       │   └── [9] מִ/כֶּ֛ם (tevir, rank=3)
│       │       └── [10] קָרְבָּ֖ן (tifcha, rank=2)
│       └── [11] לַֽ/יהוָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 9w) מִן הַ/בְּהֵמָ֗ה מִן הַ/בָּקָר֙ וּ/מִן הַ/צֹּ֔א…
    ├── PHRASE (binary 6w) מִן הַ/בְּהֵמָ֗ה מִן הַ/בָּקָר֙ וּ/מִן הַ/צֹּ֔אן
    │   ├── PHRASE (binary 2w) מִן הַ/בְּהֵמָ֗ה
    │   │   ├── [12] מִן (no cantillation mark — bind as conjunctive, rank=9)
    │   │   └── [13] הַ/בְּהֵמָ֗ה (revia, rank=3)
    │   └── PHRASE (binary 4w) מִן הַ/בָּקָר֙ וּ/מִן הַ/צֹּ֔אן
    │       ├── PHRASE (binary 2w) מִן הַ/בָּקָר֙
    │       │   ├── [14] מִן (no cantillation mark — bind as conjunctive, rank=9)
    │       │   └── [15] הַ/בָּקָר֙ (pashta, rank=3)
    │       └── PHRASE (binary 2w) וּ/מִן הַ/צֹּ֔אן
    │           ├── [16] וּ/מִן (no cantillation mark — bind as conjunctive, rank=9)
    │           └── [17] הַ/צֹּ֔אן (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) תַּקְרִ֖יבוּ אֶת קָרְבַּנְ/כֶֽם
        ├── [18] תַּקְרִ֖יבוּ (tifcha, rank=2)
        └── PHRASE (binary 2w) אֶת קָרְבַּנְ/כֶֽם
            ├── [19] אֶת (no cantillation mark — bind as conjunctive, rank=9)
            └── [20] קָרְבַּנְ/כֶֽם (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:3

- **Words:** 17 · **parser:** unique · **rules:** v1
- **Linear (plain):** אם עלה קרבנו מן הבקר זכר תמים יקריבנו אל פתח אהל מועד יקריב אתו לרצנו לפני יהוה
- **Linear (translit):** 'm 'lh qrbnv mn hbqr zkr tmym yqrybnv 'l ptch 'hl mv'd yqryb 'tv lrtznv lpny yhvh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLC0` | 9 | zero_conjunctive | אם | 'm | if | — |
| 1 | `LLLC1` | 9 | mahpach | עלה | 'lh | burnt offering / goes up | `VAR_olah` |
| 2 | `LLLC2` | 3 | pashta | קרבנו | qrbnv | his offering | `VAR_korbano` |
| 3 | `LLRL` | 9 | zero_conjunctive | מן | mn | from | — |
| 4 | `LLRR` | 2 | zaqef_qatan | הבקר | hbqr | the cattle | `VAR_ha_bakar` |
| 5 | `LRLL` | 9 | mercha | זכר | zkr | male | `VAR_zakhar` |
| 6 | `LRLR` | 2 | tifcha | תמים | tmym | unblemished | `VAR_tamim` |
| 7 | `LRR` | 1 | etnachta | יקריבנו | yqrybnv | he shall bring it near | — |
| 8 | `RLLLL` | 9 | zero_conjunctive | אל | 'l | to/toward | — |
| 9 | `RLLLR` | 4 | geresh_muqdam | פתח | ptch | entrance of | `VAR_petach_ohel_moed` |
| 10 | `RLLRL` | 9 | mahpach | אהל | 'hl | tent of | `VAR_petach_ohel_moed` |
| 11 | `RLLRR` | 3 | pashta | מועד | mv'd | meeting | `VAR_petach_ohel_moed` |
| 12 | `RLRL` | 9 | munach | יקריב | yqryb | he shall bring near | — |
| 13 | `RLRR` | 2 | zaqef_qatan | אתו | 'tv | it | — |
| 14 | `RRL` | 2 | tifcha | לרצנו | lrtznv | for its acceptance | — |
| 15 | `RRRL` | 9 | mercha | לפני | lpny | before | `VAR_lifnei_YHWH` |
| 16 | `RRRR` | 1 | silluq | יהוה | yhvh | YHWH | `VAR_lifnei_YHWH` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_petach_ohel_moed` | פתח אהל מועד | `RLL` | pashta | geresh_muqdam,mahpach,pashta |
| `VAR_lifnei_YHWH` | לפני יהוה | `RRR` | silluq | mercha,silluq |
| `VAR_olah` | עלה | `LLLC1` | mahpach | mahpach |
| `VAR_korbano` | קרבנו | `LLLC2` | pashta | pashta |
| `VAR_ha_bakar` | הבקר | `LLRR` | zaqef_qatan | zaqef_qatan |
| `VAR_zakhar` | זכר | `LRLL` | mercha | mercha |
| `VAR_tamim` | תמים | `LRLR` | tifcha | tifcha |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | pashta | אם עלה קרבנו |
| `LLR` | zaqef_qatan | מן הבקר |
| `LRL` | tifcha | זכר תמים |
| `RLLL` | geresh_muqdam | אל פתח |
| `RLLR` | pashta | אהל מועד |
| `RLR` | zaqef_qatan | יקריב אתו |
| `RRR` | silluq | לפני יהוה |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 17w) אִם עֹלָ֤ה קָרְבָּנ/וֹ֙ מִן הַ/בָּקָ֔ר זָכָ֥ר ת…
├── PHRASE (binary 8w) אִם עֹלָ֤ה קָרְבָּנ/וֹ֙ מִן הַ/בָּקָ֔ר זָכָ֥ר ת…
│   ├── PHRASE (binary 5w) אִם עֹלָ֤ה קָרְבָּנ/וֹ֙ מִן הַ/בָּקָ֔ר
│   │   ├── PHRASE (3-ary 3w) אִם עֹלָ֤ה קָרְבָּנ/וֹ֙
│   │   │   ├── [0] אִם (no cantillation mark — bind as conjunctive, rank=9)
│   │   │   ├── [1] עֹלָ֤ה (mahpach (conjunctive), rank=9)
│   │   │   └── [2] קָרְבָּנ/וֹ֙ (pashta, rank=3)
│   │   └── PHRASE (binary 2w) מִן הַ/בָּקָ֔ר
│   │       ├── [3] מִן (no cantillation mark — bind as conjunctive, rank=9)
│   │       └── [4] הַ/בָּקָ֔ר (zaqef qatan, rank=2)
│   └── PHRASE (binary 3w) זָכָ֥ר תָּמִ֖ים יַקְרִיבֶ֑/נּוּ
│       ├── PHRASE (binary 2w) זָכָ֥ר תָּמִ֖ים
│       │   ├── [5] זָכָ֥ר (mercha (conjunctive), rank=9)
│       │   └── [6] תָּמִ֖ים (tifcha, rank=2)
│       └── [7] יַקְרִיבֶ֑/נּוּ (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 9w) אֶל פֶּ֝תַח אֹ֤הֶל מוֹעֵד֙ יַקְרִ֣יב אֹת֔/וֹ לִ…
    ├── PHRASE (binary 6w) אֶל פֶּ֝תַח אֹ֤הֶל מוֹעֵד֙ יַקְרִ֣יב אֹת֔/וֹ
    │   ├── PHRASE (binary 4w) אֶל פֶּ֝תַח אֹ֤הֶל מוֹעֵד֙
    │   │   ├── PHRASE (binary 2w) אֶל פֶּ֝תַח
    │   │   │   ├── [8] אֶל (no cantillation mark — bind as conjunctive, rank=9)
    │   │   │   └── [9] פֶּ֝תַח (geresh muqdam, rank=4)
    │   │   └── PHRASE (binary 2w) אֹ֤הֶל מוֹעֵד֙
    │   │       ├── [10] אֹ֤הֶל (mahpach (conjunctive), rank=9)
    │   │       └── [11] מוֹעֵד֙ (pashta, rank=3)
    │   └── PHRASE (binary 2w) יַקְרִ֣יב אֹת֔/וֹ
    │       ├── [12] יַקְרִ֣יב (munach (conjunctive), rank=9)
    │       └── [13] אֹת֔/וֹ (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) לִ/רְצֹנ֖/וֹ לִ/פְנֵ֥י יְהוָֽה
        ├── [14] לִ/רְצֹנ֖/וֹ (tifcha, rank=2)
        └── PHRASE (binary 2w) לִ/פְנֵ֥י יְהוָֽה
            ├── [15] לִ/פְנֵ֥י (mercha (conjunctive), rank=9)
            └── [16] יְהוָֽה (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:4

- **Words:** 9 · **parser:** unique · **rules:** v1
- **Linear (plain):** וסמך ידו על ראש העלה ונרצה לו לכפר עליו
- **Linear (translit):** vsmk ydv 'l r'sh h'lh vnrtzh lv lkpr 'lyv

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLL` | 9 | munach | וסמך | vsmk | and he shall lean | `VAR_samakh` |
| 1 | `LLR` | 2 | zaqef_qatan | ידו | ydv | his hand | — |
| 2 | `LRL` | 2 | tifcha | על | 'l | on/upon | — |
| 3 | `LRRL` | 9 | munach | ראש | r'sh | head of | — |
| 4 | `LRRR` | 1 | etnachta | העלה | h'lh | the burnt offering | `VAR_ha_olah` |
| 5 | `RLL` | 9 | mercha | ונרצה | vnrtzh | and it shall be accepted | — |
| 6 | `RLR` | 2 | tifcha | לו | lv | for him | — |
| 7 | `RRL` | 9 | mercha | לכפר | lkpr | to atone | — |
| 8 | `RRR` | 1 | silluq | עליו | 'lyv | upon him | — |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_samakh` | וסמך | `LLL` | munach | munach |
| `VAR_ha_olah` | העלה | `LRRR` | etnachta | etnachta |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LL` | zaqef_qatan | וסמך ידו |
| `LRR` | etnachta | ראש העלה |
| `RL` | tifcha | ונרצה לו |
| `RR` | silluq | לכפר עליו |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 9w) וְ/סָמַ֣ךְ יָד֔/וֹ עַ֖ל רֹ֣אשׁ הָ/עֹלָ֑ה וְ/נִר…
├── PHRASE (binary 5w) וְ/סָמַ֣ךְ יָד֔/וֹ עַ֖ל רֹ֣אשׁ הָ/עֹלָ֑ה
│   ├── PHRASE (binary 2w) וְ/סָמַ֣ךְ יָד֔/וֹ
│   │   ├── [0] וְ/סָמַ֣ךְ (munach (conjunctive), rank=9)
│   │   └── [1] יָד֔/וֹ (zaqef qatan, rank=2)
│   └── PHRASE (binary 3w) עַ֖ל רֹ֣אשׁ הָ/עֹלָ֑ה
│       ├── [2] עַ֖ל (tifcha, rank=2)
│       └── PHRASE (binary 2w) רֹ֣אשׁ הָ/עֹלָ֑ה
│           ├── [3] רֹ֣אשׁ (munach (conjunctive), rank=9)
│           └── [4] הָ/עֹלָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 4w) וְ/נִרְצָ֥ה ל֖/וֹ לְ/כַפֵּ֥ר עָלָֽי/ו
    ├── PHRASE (binary 2w) וְ/נִרְצָ֥ה ל֖/וֹ
    │   ├── [5] וְ/נִרְצָ֥ה (mercha (conjunctive), rank=9)
    │   └── [6] ל֖/וֹ (tifcha, rank=2)
    └── PHRASE (binary 2w) לְ/כַפֵּ֥ר עָלָֽי/ו
        ├── [7] לְ/כַפֵּ֥ר (mercha (conjunctive), rank=9)
        └── [8] עָלָֽי/ו (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:5

- **Words:** 22 · **parser:** unique · **rules:** v1
- **Linear (plain):** ושחט את בן הבקר לפני יהוה והקריבו בני אהרן הכהנים את הדם וזרקו את הדם על המזבח סביב אשר פתח אהל מועד
- **Linear (translit):** vshcht 't bn hbqr lpny yhvh vhqrybv bny 'hrn hkhnym 't hdm vzrqv 't hdm 'l hmzbch sbyb 'shr ptch 'hl mv'd

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLL` | 3 | tevir | ושחט | vshcht | and he shall slaughter | `VAR_shachat` |
| 1 | `LLRC0` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 2 | `LLRC1` | 9 | mercha | בן | bn | son of | `VAR_ben_ha_bakar` |
| 3 | `LLRC2` | 2 | tifcha | הבקר | hbqr | the cattle | `VAR_ben_ha_bakar` |
| 4 | `LRL` | 9 | munach | לפני | lpny | before | `VAR_lifnei_YHWH` |
| 5 | `LRR` | 1 | etnachta | יהוה | yhvh | YHWH | `VAR_lifnei_YHWH` |
| 6 | `RLLL` | 4 | telisha_gedola | והקריבו | vhqrybv | and he shall bring it near | — |
| 7 | `RLLRC0` | 9 | qadma | בני | bny | sons of | `VAR_benei_aharon` |
| 8 | `RLLRC1` | 9 | mahpach | אהרן | 'hrn | Aaron | `VAR_benei_aharon` |
| 9 | `RLLRC2` | 3 | pashta | הכהנים | hkhnym | the priests | `VAR_ha_kohanim` |
| 10 | `RLRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 11 | `RLRR` | 2 | zaqef_qatan | הדם | hdm | the blood | `VAR_ha_dam` |
| 12 | `RRLLC0` | 9 | qadma | וזרקו | vzrqv | and they shall dash | `VAR_zarak` |
| 13 | `RRLLC1` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 14 | `RRLLC2` | 9 | mahpach | הדם | hdm | the blood | `VAR_ha_dam` |
| 15 | `RRLLC3` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 16 | `RRLLC4` | 3 | pashta | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 17 | `RRLR` | 2 | zaqef_qatan | סביב | sbyb | around | — |
| 18 | `RRRLL` | 9 | zero_conjunctive | אשר | 'shr | which/that | — |
| 19 | `RRRLR` | 2 | tifcha | פתח | ptch | entrance of | `VAR_petach_ohel_moed` |
| 20 | `RRRRL` | 9 | mercha | אהל | 'hl | tent of | `VAR_petach_ohel_moed` |
| 21 | `RRRRR` | 1 | silluq | מועד | mv'd | meeting | `VAR_petach_ohel_moed` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_petach_ohel_moed` | פתח אהל מועד | `RRR` | silluq | tifcha,mercha,silluq |
| `VAR_benei_aharon` | בני אהרן | `RLLRC` | mahpach | qadma,mahpach |
| `VAR_lifnei_YHWH` | לפני יהוה | `LR` | etnachta | munach,etnachta |
| `VAR_ben_ha_bakar` | בן הבקר | `LLRC` | tifcha | mercha,tifcha |
| `VAR_shachat` | ושחט | `LLL` | tevir | tevir |
| `VAR_ha_kohanim` | הכהנים | `RLLRC2` | pashta | pashta |
| `VAR_ha_dam` | הדם | `RLRR` | zaqef_qatan | zaqef_qatan |
| `VAR_zarak` | וזרקו | `RRLLC0` | qadma | qadma |
| `VAR_ha_dam` | הדם | `RRLLC2` | mahpach | mahpach |
| `VAR_ha_mizbeach` | המזבח | `RRLLC4` | pashta | pashta |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLR` | tifcha | את בן הבקר |
| `LR` | etnachta | לפני יהוה |
| `RLLR` | pashta | בני אהרן הכהנים |
| `RLR` | zaqef_qatan | את הדם |
| `RRLL` | pashta | וזרקו את הדם על המזבח |
| `RRRL` | tifcha | אשר פתח |
| `RRRR` | silluq | אהל מועד |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 22w) וְ/שָׁחַ֛ט אֶת בֶּ֥ן הַ/בָּקָ֖ר לִ/פְנֵ֣י יְהוָ…
├── PHRASE (binary 6w) וְ/שָׁחַ֛ט אֶת בֶּ֥ן הַ/בָּקָ֖ר לִ/פְנֵ֣י יְהוָ…
│   ├── PHRASE (binary 4w) וְ/שָׁחַ֛ט אֶת בֶּ֥ן הַ/בָּקָ֖ר
│   │   ├── [0] וְ/שָׁחַ֛ט (tevir, rank=3)
│   │   └── PHRASE (3-ary 3w) אֶת בֶּ֥ן הַ/בָּקָ֖ר
│   │       ├── [1] אֶת (no cantillation mark — bind as conjunctive, rank=9)
│   │       ├── [2] בֶּ֥ן (mercha (conjunctive), rank=9)
│   │       └── [3] הַ/בָּקָ֖ר (tifcha, rank=2)
│   └── PHRASE (binary 2w) לִ/פְנֵ֣י יְהוָ֑ה
│       ├── [4] לִ/פְנֵ֣י (munach (conjunctive), rank=9)
│       └── [5] יְהוָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 16w) וְ֠/הִקְרִיבוּ בְּנֵ֨י אַהֲרֹ֤ן הַֽ/כֹּֽהֲנִים֙…
    ├── PHRASE (binary 6w) וְ֠/הִקְרִיבוּ בְּנֵ֨י אַהֲרֹ֤ן הַֽ/כֹּֽהֲנִים֙…
    │   ├── PHRASE (binary 4w) וְ֠/הִקְרִיבוּ בְּנֵ֨י אַהֲרֹ֤ן הַֽ/כֹּֽהֲנִים֙
    │   │   ├── [6] וְ֠/הִקְרִיבוּ (telisha gedola, rank=4)
    │   │   └── PHRASE (3-ary 3w) בְּנֵ֨י אַהֲרֹ֤ן הַֽ/כֹּֽהֲנִים֙
    │   │       ├── [7] בְּנֵ֨י (qadma (conjunctive), rank=9)
    │   │       ├── [8] אַהֲרֹ֤ן (mahpach (conjunctive), rank=9)
    │   │       └── [9] הַֽ/כֹּֽהֲנִים֙ (pashta, rank=3)
    │   └── PHRASE (binary 2w) אֶת הַ/דָּ֔ם
    │       ├── [10] אֶת (no cantillation mark — bind as conjunctive, rank=9)
    │       └── [11] הַ/דָּ֔ם (zaqef qatan, rank=2)
    └── PHRASE (binary 10w) וְ/זָרְק֨וּ אֶת הַ/דָּ֤ם עַל הַ/מִּזְבֵּ֨חַ֙ סָ…
        ├── PHRASE (binary 6w) וְ/זָרְק֨וּ אֶת הַ/דָּ֤ם עַל הַ/מִּזְבֵּ֨חַ֙ סָ…
        │   ├── PHRASE (5-ary 5w) וְ/זָרְק֨וּ אֶת הַ/דָּ֤ם עַל הַ/מִּזְבֵּ֨חַ֙
        │   │   ├── [12] וְ/זָרְק֨וּ (qadma (conjunctive), rank=9)
        │   │   ├── [13] אֶת (no cantillation mark — bind as conjunctive, rank=9)
        │   │   ├── [14] הַ/דָּ֤ם (mahpach (conjunctive), rank=9)
        │   │   ├── [15] עַל (no cantillation mark — bind as conjunctive, rank=9)
        │   │   └── [16] הַ/מִּזְבֵּ֨חַ֙ (pashta, rank=3)
        │   └── [17] סָבִ֔יב (zaqef qatan, rank=2)
        └── PHRASE (binary 4w) אֲשֶׁר פֶּ֖תַח אֹ֥הֶל מוֹעֵֽד
            ├── PHRASE (binary 2w) אֲשֶׁר פֶּ֖תַח
            │   ├── [18] אֲשֶׁר (no cantillation mark — bind as conjunctive, rank=9)
            │   └── [19] פֶּ֖תַח (tifcha, rank=2)
            └── PHRASE (binary 2w) אֹ֥הֶל מוֹעֵֽד
                ├── [20] אֹ֥הֶל (mercha (conjunctive), rank=9)
                └── [21] מוֹעֵֽד (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:6

- **Words:** 6 · **parser:** unique · **rules:** v1
- **Linear (plain):** והפשיט את העלה ונתח אתה לנתחיה
- **Linear (translit):** vhpshyt 't h'lh vntch 'th lntchyh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LL` | 2 | tifcha | והפשיט | vhpshyt | and he shall flay | — |
| 1 | `LRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 2 | `LRR` | 1 | etnachta | העלה | h'lh | the burnt offering | `VAR_ha_olah` |
| 3 | `RLL` | 9 | mercha | ונתח | vntch | and he shall cut up | — |
| 4 | `RLR` | 2 | tifcha | אתה | 'th | it (f.) | — |
| 5 | `RR` | 1 | silluq | לנתחיה | lntchyh | into its pieces | — |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_ha_olah` | העלה | `LRR` | etnachta | etnachta |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LR` | etnachta | את העלה |
| `RL` | tifcha | ונתח אתה |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 6w) וְ/הִפְשִׁ֖יט אֶת הָ/עֹלָ֑ה וְ/נִתַּ֥ח אֹתָ֖/הּ…
├── PHRASE (binary 3w) וְ/הִפְשִׁ֖יט אֶת הָ/עֹלָ֑ה
│   ├── [0] וְ/הִפְשִׁ֖יט (tifcha, rank=2)
│   └── PHRASE (binary 2w) אֶת הָ/עֹלָ֑ה
│       ├── [1] אֶת (no cantillation mark — bind as conjunctive, rank=9)
│       └── [2] הָ/עֹלָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 3w) וְ/נִתַּ֥ח אֹתָ֖/הּ לִ/נְתָחֶֽי/הָ
    ├── PHRASE (binary 2w) וְ/נִתַּ֥ח אֹתָ֖/הּ
    │   ├── [3] וְ/נִתַּ֥ח (mercha (conjunctive), rank=9)
    │   └── [4] אֹתָ֖/הּ (tifcha, rank=2)
    └── [5] לִ/נְתָחֶֽי/הָ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:7

- **Words:** 11 · **parser:** unique · **rules:** v1
- **Linear (plain):** ונתנו בני אהרן הכהן אש על המזבח וערכו עצים על האש
- **Linear (translit):** vntnv bny 'hrn hkhn 'sh 'l hmzbch v'rkv 'tzym 'l h'sh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLL` | 4 | telisha_gedola | ונתנו | vntnv | and they shall put | — |
| 1 | `LLLRC0` | 9 | qadma | בני | bny | sons of | `VAR_benei_aharon` |
| 2 | `LLLRC1` | 9 | darga | אהרן | 'hrn | Aaron | `VAR_benei_aharon` |
| 3 | `LLLRC2` | 3 | tevir | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 4 | `LLR` | 2 | tifcha | אש | 'sh | fire | `VAR_esh` |
| 5 | `LRL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 6 | `LRR` | 1 | etnachta | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 7 | `RLL` | 9 | mercha | וערכו | v'rkv | and they shall arrange | — |
| 8 | `RLR` | 2 | tifcha | עצים | 'tzym | woods | `VAR_etzim` |
| 9 | `RRL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 10 | `RRR` | 1 | silluq | האש | h'sh | the fire | `VAR_ha_esh` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_benei_aharon` | בני אהרן | `LLLRC` | darga | qadma,darga |
| `VAR_ha_kohen` | הכהן | `LLLRC2` | tevir | tevir |
| `VAR_esh` | אש | `LLR` | tifcha | tifcha |
| `VAR_ha_mizbeach` | המזבח | `LRR` | etnachta | etnachta |
| `VAR_etzim` | עצים | `RLR` | tifcha | tifcha |
| `VAR_ha_esh` | האש | `RRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLLR` | tevir | בני אהרן הכהן |
| `LR` | etnachta | על המזבח |
| `RL` | tifcha | וערכו עצים |
| `RR` | silluq | על האש |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 11w) וְ֠/נָתְנוּ בְּנֵ֨י אַהֲרֹ֧ן הַ/כֹּהֵ֛ן אֵ֖שׁ ע…
├── PHRASE (binary 7w) וְ֠/נָתְנוּ בְּנֵ֨י אַהֲרֹ֧ן הַ/כֹּהֵ֛ן אֵ֖שׁ ע…
│   ├── PHRASE (binary 5w) וְ֠/נָתְנוּ בְּנֵ֨י אַהֲרֹ֧ן הַ/כֹּהֵ֛ן אֵ֖שׁ
│   │   ├── PHRASE (binary 4w) וְ֠/נָתְנוּ בְּנֵ֨י אַהֲרֹ֧ן הַ/כֹּהֵ֛ן
│   │   │   ├── [0] וְ֠/נָתְנוּ (telisha gedola, rank=4)
│   │   │   └── PHRASE (3-ary 3w) בְּנֵ֨י אַהֲרֹ֧ן הַ/כֹּהֵ֛ן
│   │   │       ├── [1] בְּנֵ֨י (qadma (conjunctive), rank=9)
│   │   │       ├── [2] אַהֲרֹ֧ן (darga (conjunctive), rank=9)
│   │   │       └── [3] הַ/כֹּהֵ֛ן (tevir, rank=3)
│   │   └── [4] אֵ֖שׁ (tifcha, rank=2)
│   └── PHRASE (binary 2w) עַל הַ/מִּזְבֵּ֑חַ
│       ├── [5] עַל (no cantillation mark — bind as conjunctive, rank=9)
│       └── [6] הַ/מִּזְבֵּ֑חַ (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 4w) וְ/עָרְכ֥וּ עֵצִ֖ים עַל הָ/אֵֽשׁ
    ├── PHRASE (binary 2w) וְ/עָרְכ֥וּ עֵצִ֖ים
    │   ├── [7] וְ/עָרְכ֥וּ (mercha (conjunctive), rank=9)
    │   └── [8] עֵצִ֖ים (tifcha, rank=2)
    └── PHRASE (binary 2w) עַל הָ/אֵֽשׁ
        ├── [9] עַל (no cantillation mark — bind as conjunctive, rank=9)
        └── [10] הָ/אֵֽשׁ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:8

- **Words:** 18 · **parser:** unique · **rules:** v1
- **Linear (plain):** וערכו בני אהרן הכהנים את הנתחים את הראש ואת הפדר על העצים אשר על האש אשר על המזבח
- **Linear (translit):** v'rkv bny 'hrn hkhnym 't hntchym 't hr'sh v't hpdr 'l h'tzym 'shr 'l h'sh 'shr 'l hmzbch

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLL` | 3 | revia | וערכו | v'rkv | and they shall arrange | — |
| 1 | `LLRLL` | 9 | mahpach | בני | bny | sons of | `VAR_benei_aharon` |
| 2 | `LLRLR` | 3 | pashta | אהרן | 'hrn | Aaron | `VAR_benei_aharon` |
| 3 | `LLRR` | 2 | zaqef_qatan | הכהנים | hkhnym | the priests | `VAR_ha_kohanim` |
| 4 | `LRLL` | 3 | yetiv | את | 't | (object marker) | — |
| 5 | `LRLR` | 2 | zaqef_qatan | הנתחים | hntchym | the pieces | — |
| 6 | `LRRLL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 7 | `LRRLR` | 2 | tifcha | הראש | hr'sh | the head | — |
| 8 | `LRRRL` | 9 | zero_conjunctive | ואת | v't | and | — |
| 9 | `LRRRR` | 1 | etnachta | הפדר | hpdr | the suet | — |
| 10 | `RLLL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 11 | `RLLR` | 3 | pashta | העצים | h'tzym | the woods | `VAR_ha_etzim` |
| 12 | `RLRC0` | 9 | munach | אשר | 'shr | which/that | — |
| 13 | `RLRC1` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 14 | `RLRC2` | 2 | zaqef_qatan | האש | h'sh | the fire | `VAR_ha_esh` |
| 15 | `RRL` | 2 | tifcha | אשר | 'shr | which/that | — |
| 16 | `RRRL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 17 | `RRRR` | 1 | silluq | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_benei_aharon` | בני אהרן | `LLRL` | pashta | mahpach,pashta |
| `VAR_ha_kohanim` | הכהנים | `LLRR` | zaqef_qatan | zaqef_qatan |
| `VAR_ha_etzim` | העצים | `RLLR` | pashta | pashta |
| `VAR_ha_esh` | האש | `RLRC2` | zaqef_qatan | zaqef_qatan |
| `VAR_ha_mizbeach` | המזבח | `RRRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLRL` | pashta | בני אהרן |
| `LRL` | zaqef_qatan | את הנתחים |
| `LRRL` | tifcha | את הראש |
| `LRRR` | etnachta | ואת הפדר |
| `RLL` | pashta | על העצים |
| `RLR` | zaqef_qatan | אשר על האש |
| `RRR` | silluq | על המזבח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 18w) וְ/עָרְכ֗וּ בְּנֵ֤י אַהֲרֹן֙ הַ/כֹּ֣הֲנִ֔ים אֵ֚…
├── PHRASE (binary 10w) וְ/עָרְכ֗וּ בְּנֵ֤י אַהֲרֹן֙ הַ/כֹּ֣הֲנִ֔ים אֵ֚…
│   ├── PHRASE (binary 4w) וְ/עָרְכ֗וּ בְּנֵ֤י אַהֲרֹן֙ הַ/כֹּ֣הֲנִ֔ים
│   │   ├── [0] וְ/עָרְכ֗וּ (revia, rank=3)
│   │   └── PHRASE (binary 3w) בְּנֵ֤י אַהֲרֹן֙ הַ/כֹּ֣הֲנִ֔ים
│   │       ├── PHRASE (binary 2w) בְּנֵ֤י אַהֲרֹן֙
│   │       │   ├── [1] בְּנֵ֤י (mahpach (conjunctive), rank=9)
│   │       │   └── [2] אַהֲרֹן֙ (pashta, rank=3)
│   │       └── [3] הַ/כֹּ֣הֲנִ֔ים (zaqef qatan, rank=2)
│   └── PHRASE (binary 6w) אֵ֚ת הַ/נְּתָחִ֔ים אֶת הָ/רֹ֖אשׁ וְ/אֶת הַ/פָּ֑…
│       ├── PHRASE (binary 2w) אֵ֚ת הַ/נְּתָחִ֔ים
│       │   ├── [4] אֵ֚ת (yetiv, rank=3)
│       │   └── [5] הַ/נְּתָחִ֔ים (zaqef qatan, rank=2)
│       └── PHRASE (binary 4w) אֶת הָ/רֹ֖אשׁ וְ/אֶת הַ/פָּ֑דֶר
│           ├── PHRASE (binary 2w) אֶת הָ/רֹ֖אשׁ
│           │   ├── [6] אֶת (no cantillation mark — bind as conjunctive, rank=9)
│           │   └── [7] הָ/רֹ֖אשׁ (tifcha, rank=2)
│           └── PHRASE (binary 2w) וְ/אֶת הַ/פָּ֑דֶר
│               ├── [8] וְ/אֶת (no cantillation mark — bind as conjunctive, rank=9)
│               └── [9] הַ/פָּ֑דֶר (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 8w) עַל הָ/עֵצִים֙ אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ אֲשֶׁ֖ר עַל…
    ├── PHRASE (binary 5w) עַל הָ/עֵצִים֙ אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ
    │   ├── PHRASE (binary 2w) עַל הָ/עֵצִים֙
    │   │   ├── [10] עַל (no cantillation mark — bind as conjunctive, rank=9)
    │   │   └── [11] הָ/עֵצִים֙ (pashta, rank=3)
    │   └── PHRASE (3-ary 3w) אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ
    │       ├── [12] אֲשֶׁ֣ר (munach (conjunctive), rank=9)
    │       ├── [13] עַל (no cantillation mark — bind as conjunctive, rank=9)
    │       └── [14] הָ/אֵ֔שׁ (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) אֲשֶׁ֖ר עַל הַ/מִּזְבֵּֽחַ
        ├── [15] אֲשֶׁ֖ר (tifcha, rank=2)
        └── PHRASE (binary 2w) עַל הַ/מִּזְבֵּֽחַ
            ├── [16] עַל (no cantillation mark — bind as conjunctive, rank=9)
            └── [17] הַ/מִּזְבֵּֽחַ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:9

- **Words:** 14 · **parser:** unique · **rules:** v1
- **Linear (plain):** וקרבו וכרעיו ירחץ במים והקטיר הכהן את הכל המזבחה עלה אשה ריח ניחוח ליהוה
- **Linear (translit):** vqrbv vkr'yv yrchtz bmym vhqtyr hkhn 't hkl hmzbchh 'lh 'shh rych nychvch lyhvh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLL` | 9 | mercha | וקרבו | vqrbv | and its innards | — |
| 1 | `LLR` | 2 | tifcha | וכרעיו | vkr'yv | and its legs | — |
| 2 | `LRL` | 9 | munach | ירחץ | yrchtz | he shall wash | — |
| 3 | `LRR` | 1 | etnachta | במים | bmym | in water | — |
| 4 | `RLLC0` | 9 | qadma | והקטיר | vhqtyr | and he shall turn to smoke | `VAR_hiktir` |
| 5 | `RLLC1` | 9 | mahpach | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 6 | `RLLC2` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 7 | `RLLC3` | 3 | pashta | הכל | hkl | the all | — |
| 8 | `RLR` | 2 | zaqef_qatan | המזבחה | hmzbchh | onto the altar | `VAR_ha_mizbechah` |
| 9 | `RRLL` | 3 | tevir | עלה | 'lh | burnt offering / goes up | `VAR_olah` |
| 10 | `RRLRC0` | 9 | mercha | אשה | 'shh | fire-offering | `VAR_isheh` |
| 11 | `RRLRC1` | 9 | zero_conjunctive | ריח | rych | aroma of | `VAR_reach_nichoach` |
| 12 | `RRLRC2` | 2 | tifcha | ניחוח | nychvch | soothing | `VAR_reach_nichoach` |
| 13 | `RRR` | 1 | silluq | ליהוה | lyhvh | to YHWH | `VAR_la_YHWH` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_reach_nichoach` | ריח ניחוח | `RRLRC` | tifcha | zero_conjunctive,tifcha |
| `VAR_hiktir` | והקטיר | `RLLC0` | qadma | qadma |
| `VAR_ha_kohen` | הכהן | `RLLC1` | mahpach | mahpach |
| `VAR_ha_mizbechah` | המזבחה | `RLR` | zaqef_qatan | zaqef_qatan |
| `VAR_olah` | עלה | `RRLL` | tevir | tevir |
| `VAR_isheh` | אשה | `RRLRC0` | mercha | mercha |
| `VAR_la_YHWH` | ליהוה | `RRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LL` | tifcha | וקרבו וכרעיו |
| `LR` | etnachta | ירחץ במים |
| `RLL` | pashta | והקטיר הכהן את הכל |
| `RRLR` | tifcha | אשה ריח ניחוח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 14w) וְ/קִרְבּ֥/וֹ וּ/כְרָעָ֖י/ו יִרְחַ֣ץ בַּ/מָּ֑יִ…
├── PHRASE (binary 4w) וְ/קִרְבּ֥/וֹ וּ/כְרָעָ֖י/ו יִרְחַ֣ץ בַּ/מָּ֑יִם
│   ├── PHRASE (binary 2w) וְ/קִרְבּ֥/וֹ וּ/כְרָעָ֖י/ו
│   │   ├── [0] וְ/קִרְבּ֥/וֹ (mercha (conjunctive), rank=9)
│   │   └── [1] וּ/כְרָעָ֖י/ו (tifcha, rank=2)
│   └── PHRASE (binary 2w) יִרְחַ֣ץ בַּ/מָּ֑יִם
│       ├── [2] יִרְחַ֣ץ (munach (conjunctive), rank=9)
│       └── [3] בַּ/מָּ֑יִם (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 10w) וְ/הִקְטִ֨יר הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙ הַ/מִּזְבּ…
    ├── PHRASE (binary 5w) וְ/הִקְטִ֨יר הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙ הַ/מִּזְבּ…
    │   ├── PHRASE (4-ary 4w) וְ/הִקְטִ֨יר הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙
    │   │   ├── [4] וְ/הִקְטִ֨יר (qadma (conjunctive), rank=9)
    │   │   ├── [5] הַ/כֹּהֵ֤ן (mahpach (conjunctive), rank=9)
    │   │   ├── [6] אֶת (no cantillation mark — bind as conjunctive, rank=9)
    │   │   └── [7] הַ/כֹּל֙ (pashta, rank=3)
    │   └── [8] הַ/מִּזְבֵּ֔חָ/ה (zaqef qatan, rank=2)
    └── PHRASE (binary 5w) עֹלָ֛ה אִשֵּׁ֥ה רֵֽיחַ נִיח֖וֹחַ לַֽ/יהוָֽה
        ├── PHRASE (binary 4w) עֹלָ֛ה אִשֵּׁ֥ה רֵֽיחַ נִיח֖וֹחַ
        │   ├── [9] עֹלָ֛ה (tevir, rank=3)
        │   └── PHRASE (3-ary 3w) אִשֵּׁ֥ה רֵֽיחַ נִיח֖וֹחַ
        │       ├── [10] אִשֵּׁ֥ה (mercha (conjunctive), rank=9)
        │       ├── [11] רֵֽיחַ (no cantillation mark — bind as conjunctive, rank=9)
        │       └── [12] נִיח֖וֹחַ (tifcha, rank=2)
        └── [13] לַֽ/יהוָֽה (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:10

- **Words:** 13 · **parser:** unique · **rules:** v1
- **Linear (plain):** ואם מן הצאן קרבנו מן הכשבים או מן העזים לעלה זכר תמים יקריבנו
- **Linear (translit):** v'm mn htz'n qrbnv mn hkshbym 'v mn h'zym l'lh zkr tmym yqrybnv

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLC0` | 9 | zero_conjunctive | ואם | v'm | and if | — |
| 1 | `LLLC1` | 9 | zero_conjunctive | מן | mn | from | — |
| 2 | `LLLC2` | 9 | qadma | הצאן | htz'n | the flock | `VAR_ha_tzon` |
| 3 | `LLLC3` | 9 | darga | קרבנו | qrbnv | his offering | `VAR_korbano` |
| 4 | `LLLC4` | 9 | zero_conjunctive | מן | mn | from | — |
| 5 | `LLLC5` | 3 | tevir | הכשבים | hkshbym | the lambs | — |
| 6 | `LLRC0` | 9 | mercha | או | 'v | or | — |
| 7 | `LLRC1` | 9 | zero_conjunctive | מן | mn | from | — |
| 8 | `LLRC2` | 2 | tifcha | העזים | h'zym | the goats | — |
| 9 | `LR` | 1 | etnachta | לעלה | l'lh | as burnt offering | `VAR_le_olah` |
| 10 | `RLL` | 9 | mercha | זכר | zkr | male | `VAR_zakhar` |
| 11 | `RLR` | 2 | tifcha | תמים | tmym | unblemished | `VAR_tamim` |
| 12 | `RR` | 1 | silluq | יקריבנו | yqrybnv | he shall bring it near | — |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_ha_tzon` | הצאן | `LLLC2` | qadma | qadma |
| `VAR_korbano` | קרבנו | `LLLC3` | darga | darga |
| `VAR_le_olah` | לעלה | `LR` | etnachta | etnachta |
| `VAR_zakhar` | זכר | `RLL` | mercha | mercha |
| `VAR_tamim` | תמים | `RLR` | tifcha | tifcha |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | tevir | ואם מן הצאן קרבנו מן הכשבים |
| `LLR` | tifcha | או מן העזים |
| `RL` | tifcha | זכר תמים |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 13w) וְ/אִם מִן הַ/צֹּ֨אן קָרְבָּנ֧/וֹ מִן הַ/כְּשָׂ…
├── PHRASE (binary 10w) וְ/אִם מִן הַ/צֹּ֨אן קָרְבָּנ֧/וֹ מִן הַ/כְּשָׂ…
│   ├── PHRASE (binary 9w) וְ/אִם מִן הַ/צֹּ֨אן קָרְבָּנ֧/וֹ מִן הַ/כְּשָׂ…
│   │   ├── PHRASE (6-ary 6w) וְ/אִם מִן הַ/צֹּ֨אן קָרְבָּנ֧/וֹ מִן הַ/כְּשָׂ…
│   │   │   ├── [0] וְ/אִם (no cantillation mark — bind as conjunctive, rank=9)
│   │   │   ├── [1] מִן (no cantillation mark — bind as conjunctive, rank=9)
│   │   │   ├── [2] הַ/צֹּ֨אן (qadma (conjunctive), rank=9)
│   │   │   ├── [3] קָרְבָּנ֧/וֹ (darga (conjunctive), rank=9)
│   │   │   ├── [4] מִן (no cantillation mark — bind as conjunctive, rank=9)
│   │   │   └── [5] הַ/כְּשָׂבִ֛ים (tevir, rank=3)
│   │   └── PHRASE (3-ary 3w) א֥וֹ מִן הָ/עִזִּ֖ים
│   │       ├── [6] א֥וֹ (mercha (conjunctive), rank=9)
│   │       ├── [7] מִן (no cantillation mark — bind as conjunctive, rank=9)
│   │       └── [8] הָ/עִזִּ֖ים (tifcha, rank=2)
│   └── [9] לְ/עֹלָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 3w) זָכָ֥ר תָּמִ֖ים יַקְרִיבֶֽ/נּוּ
    ├── PHRASE (binary 2w) זָכָ֥ר תָּמִ֖ים
    │   ├── [10] זָכָ֥ר (mercha (conjunctive), rank=9)
    │   └── [11] תָּמִ֖ים (tifcha, rank=2)
    └── [12] יַקְרִיבֶֽ/נּוּ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:11

- **Words:** 17 · **parser:** unique · **rules:** v1
- **Linear (plain):** ושחט אתו על ירך המזבח צפנה לפני יהוה וזרקו בני אהרן הכהנים את דמו על המזבח סביב
- **Linear (translit):** vshcht 'tv 'l yrk hmzbch tzpnh lpny yhvh vzrqv bny 'hrn hkhnym 't dmv 'l hmzbch sbyb

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLLL` | 9 | qadma | ושחט | vshcht | and he shall slaughter | `VAR_shachat` |
| 1 | `LLLLR` | 4 | geresh | אתו | 'tv | it | — |
| 2 | `LLLRC0` | 9 | munach | על | 'l | on/upon | — |
| 3 | `LLLRC1` | 9 | darga | ירך | yrk | side/thigh of | `VAR_yerech_ha_mizbeach` |
| 4 | `LLLRC2` | 3 | tevir | המזבח | hmzbch | the altar | `VAR_yerech_ha_mizbeach` |
| 5 | `LLR` | 2 | tifcha | צפנה | tzpnh | northward | `VAR_tzafonah` |
| 6 | `LRL` | 9 | munach | לפני | lpny | before | `VAR_lifnei_YHWH` |
| 7 | `LRR` | 1 | etnachta | יהוה | yhvh | YHWH | `VAR_lifnei_YHWH` |
| 8 | `RLLL` | 4 | pazer | וזרקו | vzrqv | and they shall dash | `VAR_zarak` |
| 9 | `RLLRC0` | 9 | telisha_qetana | בני | bny | sons of | `VAR_benei_aharon` |
| 10 | `RLLRC1` | 9 | qadma | אהרן | 'hrn | Aaron | `VAR_benei_aharon` |
| 11 | `RLLRC2` | 9 | darga | הכהנים | hkhnym | the priests | `VAR_ha_kohanim` |
| 12 | `RLLRC3` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 13 | `RLLRC4` | 3 | tevir | דמו | dmv | its blood | `VAR_damo` |
| 14 | `RLRL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 15 | `RLRR` | 2 | tifcha | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 16 | `RR` | 1 | silluq | סביב | sbyb | around | — |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_benei_aharon` | בני אהרן | `RLLRC` | qadma | telisha_qetana,qadma |
| `VAR_lifnei_YHWH` | לפני יהוה | `LR` | etnachta | munach,etnachta |
| `VAR_yerech_ha_mizbeach` | ירך המזבח | `LLLRC` | tevir | darga,tevir |
| `VAR_shachat` | ושחט | `LLLLL` | qadma | qadma |
| `VAR_tzafonah` | צפנה | `LLR` | tifcha | tifcha |
| `VAR_zarak` | וזרקו | `RLLL` | pazer | pazer |
| `VAR_ha_kohanim` | הכהנים | `RLLRC2` | darga | darga |
| `VAR_damo` | דמו | `RLLRC4` | tevir | tevir |
| `VAR_ha_mizbeach` | המזבח | `RLRR` | tifcha | tifcha |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLLL` | geresh | ושחט אתו |
| `LLLR` | tevir | על ירך המזבח |
| `LR` | etnachta | לפני יהוה |
| `RLLR` | tevir | בני אהרן הכהנים את דמו |
| `RLR` | tifcha | על המזבח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 17w) וְ/שָׁחַ֨ט אֹת֜/וֹ עַ֣ל יֶ֧רֶךְ הַ/מִּזְבֵּ֛חַ …
├── PHRASE (binary 8w) וְ/שָׁחַ֨ט אֹת֜/וֹ עַ֣ל יֶ֧רֶךְ הַ/מִּזְבֵּ֛חַ …
│   ├── PHRASE (binary 6w) וְ/שָׁחַ֨ט אֹת֜/וֹ עַ֣ל יֶ֧רֶךְ הַ/מִּזְבֵּ֛חַ …
│   │   ├── PHRASE (binary 5w) וְ/שָׁחַ֨ט אֹת֜/וֹ עַ֣ל יֶ֧רֶךְ הַ/מִּזְבֵּ֛חַ
│   │   │   ├── PHRASE (binary 2w) וְ/שָׁחַ֨ט אֹת֜/וֹ
│   │   │   │   ├── [0] וְ/שָׁחַ֨ט (qadma (conjunctive), rank=9)
│   │   │   │   └── [1] אֹת֜/וֹ (geresh, rank=4)
│   │   │   └── PHRASE (3-ary 3w) עַ֣ל יֶ֧רֶךְ הַ/מִּזְבֵּ֛חַ
│   │   │       ├── [2] עַ֣ל (munach (conjunctive), rank=9)
│   │   │       ├── [3] יֶ֧רֶךְ (darga (conjunctive), rank=9)
│   │   │       └── [4] הַ/מִּזְבֵּ֛חַ (tevir, rank=3)
│   │   └── [5] צָפֹ֖נָ/ה (tifcha, rank=2)
│   └── PHRASE (binary 2w) לִ/פְנֵ֣י יְהוָ֑ה
│       ├── [6] לִ/פְנֵ֣י (munach (conjunctive), rank=9)
│       └── [7] יְהוָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 9w) וְ/זָרְק֡וּ בְּנֵי֩ אַהֲרֹ֨ן הַ/כֹּהֲנִ֧ים אֶת …
    ├── PHRASE (binary 8w) וְ/זָרְק֡וּ בְּנֵי֩ אַהֲרֹ֨ן הַ/כֹּהֲנִ֧ים אֶת …
    │   ├── PHRASE (binary 6w) וְ/זָרְק֡וּ בְּנֵי֩ אַהֲרֹ֨ן הַ/כֹּהֲנִ֧ים אֶת …
    │   │   ├── [8] וְ/זָרְק֡וּ (pazer, rank=4)
    │   │   └── PHRASE (5-ary 5w) בְּנֵי֩ אַהֲרֹ֨ן הַ/כֹּהֲנִ֧ים אֶת דָּמ֛/וֹ
    │   │       ├── [9] בְּנֵי֩ (telisha qetana (conjunctive), rank=9)
    │   │       ├── [10] אַהֲרֹ֨ן (qadma (conjunctive), rank=9)
    │   │       ├── [11] הַ/כֹּהֲנִ֧ים (darga (conjunctive), rank=9)
    │   │       ├── [12] אֶת (no cantillation mark — bind as conjunctive, rank=9)
    │   │       └── [13] דָּמ֛/וֹ (tevir, rank=3)
    │   └── PHRASE (binary 2w) עַל הַ/מִּזְבֵּ֖חַ
    │       ├── [14] עַל (no cantillation mark — bind as conjunctive, rank=9)
    │       └── [15] הַ/מִּזְבֵּ֖חַ (tifcha, rank=2)
    └── [16] סָבִֽיב (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:12

- **Words:** 18 · **parser:** unique · **rules:** v1
- **Linear (plain):** ונתח אתו לנתחיו ואת ראשו ואת פדרו וערך הכהן אתם על העצים אשר על האש אשר על המזבח
- **Linear (translit):** vntch 'tv lntchyv v't r'shv v't pdrv v'rk hkhn 'tm 'l h'tzym 'shr 'l h'sh 'shr 'l hmzbch

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLL` | 9 | mahpach | ונתח | vntch | and he shall cut up | — |
| 1 | `LLLR` | 3 | pashta | אתו | 'tv | it | — |
| 2 | `LLR` | 2 | zaqef_qatan | לנתחיו | lntchyv | into its pieces | — |
| 3 | `LRLL` | 9 | zero_conjunctive | ואת | v't | and | — |
| 4 | `LRLR` | 2 | tifcha | ראשו | r'shv | its head | — |
| 5 | `LRRL` | 9 | zero_conjunctive | ואת | v't | and | — |
| 6 | `LRRR` | 1 | etnachta | פדרו | pdrv | its suet | — |
| 7 | `RLLL` | 9 | mahpach | וערך | v'rk | and he shall arrange | — |
| 8 | `RLLR` | 3 | pashta | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 9 | `RLR` | 2 | zaqef_qatan | אתם | 'tm | them | — |
| 10 | `RRLLL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 11 | `RRLLR` | 3 | pashta | העצים | h'tzym | the woods | `VAR_ha_etzim` |
| 12 | `RRLRC0` | 9 | munach | אשר | 'shr | which/that | — |
| 13 | `RRLRC1` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 14 | `RRLRC2` | 2 | zaqef_qatan | האש | h'sh | the fire | `VAR_ha_esh` |
| 15 | `RRRL` | 2 | tifcha | אשר | 'shr | which/that | — |
| 16 | `RRRRL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 17 | `RRRRR` | 1 | silluq | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_ha_kohen` | הכהן | `RLLR` | pashta | pashta |
| `VAR_ha_etzim` | העצים | `RRLLR` | pashta | pashta |
| `VAR_ha_esh` | האש | `RRLRC2` | zaqef_qatan | zaqef_qatan |
| `VAR_ha_mizbeach` | המזבח | `RRRRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | pashta | ונתח אתו |
| `LRL` | tifcha | ואת ראשו |
| `LRR` | etnachta | ואת פדרו |
| `RLL` | pashta | וערך הכהן |
| `RRLL` | pashta | על העצים |
| `RRLR` | zaqef_qatan | אשר על האש |
| `RRRR` | silluq | על המזבח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 18w) וְ/נִתַּ֤ח אֹת/וֹ֙ לִ/נְתָחָ֔י/ו וְ/אֶת רֹאשׁ֖/…
├── PHRASE (binary 7w) וְ/נִתַּ֤ח אֹת/וֹ֙ לִ/נְתָחָ֔י/ו וְ/אֶת רֹאשׁ֖/…
│   ├── PHRASE (binary 3w) וְ/נִתַּ֤ח אֹת/וֹ֙ לִ/נְתָחָ֔י/ו
│   │   ├── PHRASE (binary 2w) וְ/נִתַּ֤ח אֹת/וֹ֙
│   │   │   ├── [0] וְ/נִתַּ֤ח (mahpach (conjunctive), rank=9)
│   │   │   └── [1] אֹת/וֹ֙ (pashta, rank=3)
│   │   └── [2] לִ/נְתָחָ֔י/ו (zaqef qatan, rank=2)
│   └── PHRASE (binary 4w) וְ/אֶת רֹאשׁ֖/וֹ וְ/אֶת פִּדְר֑/וֹ
│       ├── PHRASE (binary 2w) וְ/אֶת רֹאשׁ֖/וֹ
│       │   ├── [3] וְ/אֶת (no cantillation mark — bind as conjunctive, rank=9)
│       │   └── [4] רֹאשׁ֖/וֹ (tifcha, rank=2)
│       └── PHRASE (binary 2w) וְ/אֶת פִּדְר֑/וֹ
│           ├── [5] וְ/אֶת (no cantillation mark — bind as conjunctive, rank=9)
│           └── [6] פִּדְר֑/וֹ (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 11w) וְ/עָרַ֤ךְ הַ/כֹּהֵן֙ אֹתָ֔/ם עַל הָֽ/עֵצִים֙ א…
    ├── PHRASE (binary 3w) וְ/עָרַ֤ךְ הַ/כֹּהֵן֙ אֹתָ֔/ם
    │   ├── PHRASE (binary 2w) וְ/עָרַ֤ךְ הַ/כֹּהֵן֙
    │   │   ├── [7] וְ/עָרַ֤ךְ (mahpach (conjunctive), rank=9)
    │   │   └── [8] הַ/כֹּהֵן֙ (pashta, rank=3)
    │   └── [9] אֹתָ֔/ם (zaqef qatan, rank=2)
    └── PHRASE (binary 8w) עַל הָֽ/עֵצִים֙ אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ אֲשֶׁ֖ר עַ…
        ├── PHRASE (binary 5w) עַל הָֽ/עֵצִים֙ אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ
        │   ├── PHRASE (binary 2w) עַל הָֽ/עֵצִים֙
        │   │   ├── [10] עַל (no cantillation mark — bind as conjunctive, rank=9)
        │   │   └── [11] הָֽ/עֵצִים֙ (pashta, rank=3)
        │   └── PHRASE (3-ary 3w) אֲשֶׁ֣ר עַל הָ/אֵ֔שׁ
        │       ├── [12] אֲשֶׁ֣ר (munach (conjunctive), rank=9)
        │       ├── [13] עַל (no cantillation mark — bind as conjunctive, rank=9)
        │       └── [14] הָ/אֵ֔שׁ (zaqef qatan, rank=2)
        └── PHRASE (binary 3w) אֲשֶׁ֖ר עַל הַ/מִּזְבֵּֽחַ
            ├── [15] אֲשֶׁ֖ר (tifcha, rank=2)
            └── PHRASE (binary 2w) עַל הַ/מִּזְבֵּֽחַ
                ├── [16] עַל (no cantillation mark — bind as conjunctive, rank=9)
                └── [17] הַ/מִּזְבֵּֽחַ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:13

- **Words:** 16 · **parser:** unique · **rules:** v1
- **Linear (plain):** והקרב והכרעים ירחץ במים והקריב הכהן את הכל והקטיר המזבחה עלה הוא אשה ריח ניחח ליהוה
- **Linear (translit):** vhqrb vhkr'ym yrchtz bmym vhqryb hkhn 't hkl vhqtyr hmzbchh 'lh hv' 'shh rych nychch lyhvh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLL` | 9 | mercha | והקרב | vhqrb | and the innards | — |
| 1 | `LLR` | 2 | tifcha | והכרעים | vhkr'ym | and the legs | — |
| 2 | `LRL` | 9 | munach | ירחץ | yrchtz | he shall wash | — |
| 3 | `LRR` | 1 | etnachta | במים | bmym | in water | — |
| 4 | `RLLC0` | 9 | qadma | והקריב | vhqryb | and he shall bring near | — |
| 5 | `RLLC1` | 9 | mahpach | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 6 | `RLLC2` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 7 | `RLLC3` | 3 | pashta | הכל | hkl | the all | — |
| 8 | `RLRL` | 9 | munach | והקטיר | vhqtyr | and he shall turn to smoke | `VAR_hiktir` |
| 9 | `RLRR` | 2 | zaqef_qatan | המזבחה | hmzbchh | onto the altar | `VAR_ha_mizbechah` |
| 10 | `RRLLL` | 9 | munach | עלה | 'lh | burnt offering / goes up | `VAR_olah` |
| 11 | `RRLLR` | 3 | revia | הוא | hv' | it is | — |
| 12 | `RRLRL` | 3 | tevir | אשה | 'shh | fire-offering | `VAR_isheh` |
| 13 | `RRLRRL` | 9 | mercha | ריח | rych | aroma of | `VAR_reach_nichoach` |
| 14 | `RRLRRR` | 2 | tifcha | ניחח | nychch | soothing | `VAR_reach_nichoach` |
| 15 | `RRR` | 1 | silluq | ליהוה | lyhvh | to YHWH | `VAR_la_YHWH` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_reach_nichoach` | ריח ניחח | `RRLRR` | tifcha | mercha,tifcha |
| `VAR_ha_kohen` | הכהן | `RLLC1` | mahpach | mahpach |
| `VAR_hiktir` | והקטיר | `RLRL` | munach | munach |
| `VAR_ha_mizbechah` | המזבחה | `RLRR` | zaqef_qatan | zaqef_qatan |
| `VAR_olah` | עלה | `RRLLL` | munach | munach |
| `VAR_isheh` | אשה | `RRLRL` | tevir | tevir |
| `VAR_la_YHWH` | ליהוה | `RRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LL` | tifcha | והקרב והכרעים |
| `LR` | etnachta | ירחץ במים |
| `RLL` | pashta | והקריב הכהן את הכל |
| `RLR` | zaqef_qatan | והקטיר המזבחה |
| `RRLL` | revia | עלה הוא |
| `RRLRR` | tifcha | ריח ניחח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 16w) וְ/הַ/קֶּ֥רֶב וְ/הַ/כְּרָעַ֖יִם יִרְחַ֣ץ בַּ/מּ…
├── PHRASE (binary 4w) וְ/הַ/קֶּ֥רֶב וְ/הַ/כְּרָעַ֖יִם יִרְחַ֣ץ בַּ/מּ…
│   ├── PHRASE (binary 2w) וְ/הַ/קֶּ֥רֶב וְ/הַ/כְּרָעַ֖יִם
│   │   ├── [0] וְ/הַ/קֶּ֥רֶב (mercha (conjunctive), rank=9)
│   │   └── [1] וְ/הַ/כְּרָעַ֖יִם (tifcha, rank=2)
│   └── PHRASE (binary 2w) יִרְחַ֣ץ בַּ/מָּ֑יִם
│       ├── [2] יִרְחַ֣ץ (munach (conjunctive), rank=9)
│       └── [3] בַּ/מָּ֑יִם (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 12w) וְ/הִקְרִ֨יב הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙ וְ/הִקְטִ֣…
    ├── PHRASE (binary 6w) וְ/הִקְרִ֨יב הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙ וְ/הִקְטִ֣…
    │   ├── PHRASE (4-ary 4w) וְ/הִקְרִ֨יב הַ/כֹּהֵ֤ן אֶת הַ/כֹּל֙
    │   │   ├── [4] וְ/הִקְרִ֨יב (qadma (conjunctive), rank=9)
    │   │   ├── [5] הַ/כֹּהֵ֤ן (mahpach (conjunctive), rank=9)
    │   │   ├── [6] אֶת (no cantillation mark — bind as conjunctive, rank=9)
    │   │   └── [7] הַ/כֹּל֙ (pashta, rank=3)
    │   └── PHRASE (binary 2w) וְ/הִקְטִ֣יר הַ/מִּזְבֵּ֔חָ/ה
    │       ├── [8] וְ/הִקְטִ֣יר (munach (conjunctive), rank=9)
    │       └── [9] הַ/מִּזְבֵּ֔חָ/ה (zaqef qatan, rank=2)
    └── PHRASE (binary 6w) עֹלָ֣ה ה֗וּא אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ לַ/יהוָֽה
        ├── PHRASE (binary 5w) עֹלָ֣ה ה֗וּא אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ
        │   ├── PHRASE (binary 2w) עֹלָ֣ה ה֗וּא
        │   │   ├── [10] עֹלָ֣ה (munach (conjunctive), rank=9)
        │   │   └── [11] ה֗וּא (revia, rank=3)
        │   └── PHRASE (binary 3w) אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ
        │       ├── [12] אִשֵּׁ֛ה (tevir, rank=3)
        │       └── PHRASE (binary 2w) רֵ֥יחַ נִיחֹ֖חַ
        │           ├── [13] רֵ֥יחַ (mercha (conjunctive), rank=9)
        │           └── [14] נִיחֹ֖חַ (tifcha, rank=2)
        └── [15] לַ/יהוָֽה (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:14

- **Words:** 15 · **parser:** unique · **rules:** v1
- **Linear (plain):** ואם מן העוף עלה קרבנו ליהוה והקריב מן התרים או מן בני היונה את קרבנו
- **Linear (translit):** v'm mn h'vp 'lh qrbnv lyhvh vhqryb mn htrym 'v mn bny hyvnh 't qrbnv

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLC0` | 9 | darga | ואם | v'm | and if | — |
| 1 | `LLLC1` | 9 | zero_conjunctive | מן | mn | from | — |
| 2 | `LLLC2` | 3 | tevir | העוף | h'vp | the bird | `VAR_ha_of` |
| 3 | `LLRL` | 9 | mercha | עלה | 'lh | burnt offering / goes up | `VAR_olah` |
| 4 | `LLRR` | 2 | tifcha | קרבנו | qrbnv | his offering | `VAR_korbano` |
| 5 | `LR` | 1 | etnachta | ליהוה | lyhvh | to YHWH | `VAR_la_YHWH` |
| 6 | `RLLC0` | 9 | munach | והקריב | vhqryb | and he shall bring near | — |
| 7 | `RLLC1` | 9 | zero_conjunctive | מן | mn | from | — |
| 8 | `RLLC2` | 3 | revia | התרים | htrym | the turtledoves | `VAR_ha_torim` |
| 9 | `RLRL` | 3 | tevir | או | 'v | or | — |
| 10 | `RLRRC0` | 9 | zero_conjunctive | מן | mn | from | — |
| 11 | `RLRRC1` | 9 | mercha | בני | bny | sons of | `VAR_benei_ha_yonah` |
| 12 | `RLRRC2` | 2 | tifcha | היונה | hyvnh | the pigeon | `VAR_benei_ha_yonah` |
| 13 | `RRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 14 | `RRR` | 1 | silluq | קרבנו | qrbnv | his offering | `VAR_korbano` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_benei_ha_yonah` | בני היונה | `RLRRC` | tifcha | mercha,tifcha |
| `VAR_ha_of` | העוף | `LLLC2` | tevir | tevir |
| `VAR_olah` | עלה | `LLRL` | mercha | mercha |
| `VAR_korbano` | קרבנו | `LLRR` | tifcha | tifcha |
| `VAR_la_YHWH` | ליהוה | `LR` | etnachta | etnachta |
| `VAR_ha_torim` | התרים | `RLLC2` | revia | revia |
| `VAR_korbano` | קרבנו | `RRR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | tevir | ואם מן העוף |
| `LLR` | tifcha | עלה קרבנו |
| `RLL` | revia | והקריב מן התרים |
| `RLRR` | tifcha | מן בני היונה |
| `RR` | silluq | את קרבנו |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 15w) וְ/אִ֧ם מִן הָ/ע֛וֹף עֹלָ֥ה קָרְבָּנ֖/וֹ לַֽ/יה…
├── PHRASE (binary 6w) וְ/אִ֧ם מִן הָ/ע֛וֹף עֹלָ֥ה קָרְבָּנ֖/וֹ לַֽ/יה…
│   ├── PHRASE (binary 5w) וְ/אִ֧ם מִן הָ/ע֛וֹף עֹלָ֥ה קָרְבָּנ֖/וֹ
│   │   ├── PHRASE (3-ary 3w) וְ/אִ֧ם מִן הָ/ע֛וֹף
│   │   │   ├── [0] וְ/אִ֧ם (darga (conjunctive), rank=9)
│   │   │   ├── [1] מִן (no cantillation mark — bind as conjunctive, rank=9)
│   │   │   └── [2] הָ/ע֛וֹף (tevir, rank=3)
│   │   └── PHRASE (binary 2w) עֹלָ֥ה קָרְבָּנ֖/וֹ
│   │       ├── [3] עֹלָ֥ה (mercha (conjunctive), rank=9)
│   │       └── [4] קָרְבָּנ֖/וֹ (tifcha, rank=2)
│   └── [5] לַֽ/יהוָ֑ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 9w) וְ/הִקְרִ֣יב מִן הַ/תֹּרִ֗ים א֛וֹ מִן בְּנֵ֥י ה…
    ├── PHRASE (binary 7w) וְ/הִקְרִ֣יב מִן הַ/תֹּרִ֗ים א֛וֹ מִן בְּנֵ֥י ה…
    │   ├── PHRASE (3-ary 3w) וְ/הִקְרִ֣יב מִן הַ/תֹּרִ֗ים
    │   │   ├── [6] וְ/הִקְרִ֣יב (munach (conjunctive), rank=9)
    │   │   ├── [7] מִן (no cantillation mark — bind as conjunctive, rank=9)
    │   │   └── [8] הַ/תֹּרִ֗ים (revia, rank=3)
    │   └── PHRASE (binary 4w) א֛וֹ מִן בְּנֵ֥י הַ/יּוֹנָ֖ה
    │       ├── [9] א֛וֹ (tevir, rank=3)
    │       └── PHRASE (3-ary 3w) מִן בְּנֵ֥י הַ/יּוֹנָ֖ה
    │           ├── [10] מִן (no cantillation mark — bind as conjunctive, rank=9)
    │           ├── [11] בְּנֵ֥י (mercha (conjunctive), rank=9)
    │           └── [12] הַ/יּוֹנָ֖ה (tifcha, rank=2)
    └── PHRASE (binary 2w) אֶת קָרְבָּנֽ/וֹ
        ├── [13] אֶת (no cantillation mark — bind as conjunctive, rank=9)
        └── [14] קָרְבָּנֽ/וֹ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:15

- **Words:** 14 · **parser:** unique · **rules:** v1
- **Linear (plain):** והקריבו הכהן אל המזבח ומלק את ראשו והקטיר המזבחה ונמצה דמו על קיר המזבח
- **Linear (translit):** vhqrybv hkhn 'l hmzbch vmlq 't r'shv vhqtyr hmzbchh vnmtzh dmv 'l qyr hmzbch

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLL` | 9 | mahpach | והקריבו | vhqrybv | and he shall bring it near | — |
| 1 | `LLLR` | 3 | pashta | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 2 | `LLRL` | 9 | zero_conjunctive | אל | 'l | to/toward | — |
| 3 | `LLRR` | 2 | zaqef_qatan | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 4 | `LRLL` | 3 | pashta | ומלק | vmlq | and he shall nip | — |
| 5 | `LRLRL` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 6 | `LRLRR` | 2 | zaqef_qatan | ראשו | r'shv | its head | — |
| 7 | `LRRL` | 2 | tifcha | והקטיר | vhqtyr | and he shall turn to smoke | `VAR_hiktir` |
| 8 | `LRRR` | 1 | etnachta | המזבחה | hmzbchh | onto the altar | `VAR_ha_mizbechah` |
| 9 | `RLL` | 9 | munach | ונמצה | vnmtzh | and it shall be drained | — |
| 10 | `RLR` | 2 | zaqef_qatan | דמו | dmv | its blood | `VAR_damo` |
| 11 | `RRL` | 2 | tifcha | על | 'l | on/upon | — |
| 12 | `RRRL` | 9 | mercha | קיר | qyr | wall of | `VAR_kir_ha_mizbeach` |
| 13 | `RRRR` | 1 | silluq | המזבח | hmzbch | the altar | `VAR_kir_ha_mizbeach` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_kir_ha_mizbeach` | קיר המזבח | `RRR` | silluq | mercha,silluq |
| `VAR_ha_kohen` | הכהן | `LLLR` | pashta | pashta |
| `VAR_ha_mizbeach` | המזבח | `LLRR` | zaqef_qatan | zaqef_qatan |
| `VAR_hiktir` | והקטיר | `LRRL` | tifcha | tifcha |
| `VAR_ha_mizbechah` | המזבחה | `LRRR` | etnachta | etnachta |
| `VAR_damo` | דמו | `RLR` | zaqef_qatan | zaqef_qatan |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | pashta | והקריבו הכהן |
| `LLR` | zaqef_qatan | אל המזבח |
| `LRLR` | zaqef_qatan | את ראשו |
| `LRR` | etnachta | והקטיר המזבחה |
| `RL` | zaqef_qatan | ונמצה דמו |
| `RRR` | silluq | קיר המזבח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 14w) וְ/הִקְרִיב֤/וֹ הַ/כֹּהֵן֙ אֶל הַ/מִּזְבֵּ֔חַ ו…
├── PHRASE (binary 9w) וְ/הִקְרִיב֤/וֹ הַ/כֹּהֵן֙ אֶל הַ/מִּזְבֵּ֔חַ ו…
│   ├── PHRASE (binary 4w) וְ/הִקְרִיב֤/וֹ הַ/כֹּהֵן֙ אֶל הַ/מִּזְבֵּ֔חַ
│   │   ├── PHRASE (binary 2w) וְ/הִקְרִיב֤/וֹ הַ/כֹּהֵן֙
│   │   │   ├── [0] וְ/הִקְרִיב֤/וֹ (mahpach (conjunctive), rank=9)
│   │   │   └── [1] הַ/כֹּהֵן֙ (pashta, rank=3)
│   │   └── PHRASE (binary 2w) אֶל הַ/מִּזְבֵּ֔חַ
│   │       ├── [2] אֶל (no cantillation mark — bind as conjunctive, rank=9)
│   │       └── [3] הַ/מִּזְבֵּ֔חַ (zaqef qatan, rank=2)
│   └── PHRASE (binary 5w) וּ/מָלַק֙ אֶת רֹאשׁ֔/וֹ וְ/הִקְטִ֖יר הַ/מִּזְבּ…
│       ├── PHRASE (binary 3w) וּ/מָלַק֙ אֶת רֹאשׁ֔/וֹ
│       │   ├── [4] וּ/מָלַק֙ (pashta, rank=3)
│       │   └── PHRASE (binary 2w) אֶת רֹאשׁ֔/וֹ
│       │       ├── [5] אֶת (no cantillation mark — bind as conjunctive, rank=9)
│       │       └── [6] רֹאשׁ֔/וֹ (zaqef qatan, rank=2)
│       └── PHRASE (binary 2w) וְ/הִקְטִ֖יר הַ/מִּזְבֵּ֑חָ/ה
│           ├── [7] וְ/הִקְטִ֖יר (tifcha, rank=2)
│           └── [8] הַ/מִּזְבֵּ֑חָ/ה (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 5w) וְ/נִמְצָ֣ה דָמ֔/וֹ עַ֖ל קִ֥יר הַ/מִּזְבֵּֽחַ
    ├── PHRASE (binary 2w) וְ/נִמְצָ֣ה דָמ֔/וֹ
    │   ├── [9] וְ/נִמְצָ֣ה (munach (conjunctive), rank=9)
    │   └── [10] דָמ֔/וֹ (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) עַ֖ל קִ֥יר הַ/מִּזְבֵּֽחַ
        ├── [11] עַ֖ל (tifcha, rank=2)
        └── PHRASE (binary 2w) קִ֥יר הַ/מִּזְבֵּֽחַ
            ├── [12] קִ֥יר (mercha (conjunctive), rank=9)
            └── [13] הַ/מִּזְבֵּֽחַ (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:16

- **Words:** 12 · **parser:** unique · **rules:** v1
- **Linear (plain):** והסיר את מראתו בנצתה והשליך אתה אצל המזבח קדמה אל מקום הדשן
- **Linear (translit):** vhsyr 't mr'tv bntzth vhshlyk 'th 'tzl hmzbch qdmh 'l mqvm hdshn

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLC0` | 9 | mercha | והסיר | vhsyr | and he shall remove | — |
| 1 | `LLC1` | 9 | zero_conjunctive | את | 't | (object marker) | — |
| 2 | `LLC2` | 2 | tifcha | מראתו | mr'tv | its crop | — |
| 3 | `LR` | 1 | etnachta | בנצתה | bntzth | with its feathers | — |
| 4 | `RLLLL` | 9 | qadma | והשליך | vhshlyk | and he shall throw | — |
| 5 | `RLLLR` | 4 | geresh | אתה | 'th | it (f.) | — |
| 6 | `RLLRL` | 9 | mahpach | אצל | 'tzl | beside | — |
| 7 | `RLLRR` | 3 | pashta | המזבח | hmzbch | the altar | `VAR_ha_mizbeach` |
| 8 | `RLR` | 2 | zaqef_qatan | קדמה | qdmh | eastward | — |
| 9 | `RRLL` | 9 | zero_conjunctive | אל | 'l | to/toward | — |
| 10 | `RRLR` | 2 | tifcha | מקום | mqvm | place of | `VAR_mekom_ha_deshen` |
| 11 | `RRR` | 1 | silluq | הדשן | hdshn | the ash | `VAR_mekom_ha_deshen` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_mekom_ha_deshen` | מקום הדשן | `RR` | silluq | tifcha,silluq |
| `VAR_ha_mizbeach` | המזבח | `RLLRR` | pashta | pashta |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LL` | tifcha | והסיר את מראתו |
| `RLLL` | geresh | והשליך אתה |
| `RLLR` | pashta | אצל המזבח |
| `RRL` | tifcha | אל מקום |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 12w) וְ/הֵסִ֥יר אֶת מֻרְאָת֖/וֹ בְּ/נֹצָתָ֑/הּ וְ/הִ…
├── PHRASE (binary 4w) וְ/הֵסִ֥יר אֶת מֻרְאָת֖/וֹ בְּ/נֹצָתָ֑/הּ
│   ├── PHRASE (3-ary 3w) וְ/הֵסִ֥יר אֶת מֻרְאָת֖/וֹ
│   │   ├── [0] וְ/הֵסִ֥יר (mercha (conjunctive), rank=9)
│   │   ├── [1] אֶת (no cantillation mark — bind as conjunctive, rank=9)
│   │   └── [2] מֻרְאָת֖/וֹ (tifcha, rank=2)
│   └── [3] בְּ/נֹצָתָ֑/הּ (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 8w) וְ/הִשְׁלִ֨יךְ אֹתָ֜/הּ אֵ֤צֶל הַ/מִּזְבֵּ֨חַ֙ …
    ├── PHRASE (binary 5w) וְ/הִשְׁלִ֨יךְ אֹתָ֜/הּ אֵ֤צֶל הַ/מִּזְבֵּ֨חַ֙ …
    │   ├── PHRASE (binary 4w) וְ/הִשְׁלִ֨יךְ אֹתָ֜/הּ אֵ֤צֶל הַ/מִּזְבֵּ֨חַ֙
    │   │   ├── PHRASE (binary 2w) וְ/הִשְׁלִ֨יךְ אֹתָ֜/הּ
    │   │   │   ├── [4] וְ/הִשְׁלִ֨יךְ (qadma (conjunctive), rank=9)
    │   │   │   └── [5] אֹתָ֜/הּ (geresh, rank=4)
    │   │   └── PHRASE (binary 2w) אֵ֤צֶל הַ/מִּזְבֵּ֨חַ֙
    │   │       ├── [6] אֵ֤צֶל (mahpach (conjunctive), rank=9)
    │   │       └── [7] הַ/מִּזְבֵּ֨חַ֙ (pashta, rank=3)
    │   └── [8] קֵ֔דְמָ/ה (zaqef qatan, rank=2)
    └── PHRASE (binary 3w) אֶל מְק֖וֹם הַ/דָּֽשֶׁן
        ├── PHRASE (binary 2w) אֶל מְק֖וֹם
        │   ├── [9] אֶל (no cantillation mark — bind as conjunctive, rank=9)
        │   └── [10] מְק֖וֹם (tifcha, rank=2)
        └── [11] הַ/דָּֽשֶׁן (silluq (verse-end emperor), rank=1)
```

</details>

### Lev 1:17

- **Words:** 20 · **parser:** unique · **rules:** v1
- **Linear (plain):** ושסע אתו בכנפיו לא יבדיל והקטיר אתו הכהן המזבחה על העצים אשר על האש עלה הוא אשה ריח ניחח ליהוה
- **Linear (translit):** vshs' 'tv bknpyv l' ybdyl vhqtyr 'tv hkhn hmzbchh 'l h'tzym 'shr 'l h'sh 'lh hv' 'shh rych nychch lyhvh

| i | path | rk | mark | Hebrew | Translit | English | VAR |
|--:|------|---:|------|--------|----------|---------|-----|
| 0 | `LLLC0` | 9 | qadma | ושסע | vshs' | and he shall split | — |
| 1 | `LLLC1` | 9 | munach | אתו | 'tv | it | — |
| 2 | `LLLC2` | 3 | zinor | בכנפיו | bknpyv | by its wings | — |
| 3 | `LLRL` | 9 | munach | לא | l' | not | — |
| 4 | `LLRR` | 2 | segol | יבדיל | ybdyl | he shall divide | — |
| 5 | `LRLLC0` | 9 | qadma | והקטיר | vhqtyr | and he shall turn to smoke | `VAR_hiktir` |
| 6 | `LRLLC1` | 9 | mahpach | אתו | 'tv | it | — |
| 7 | `LRLLC2` | 3 | pashta | הכהן | hkhn | the priest | `VAR_ha_kohen` |
| 8 | `LRLR` | 2 | zaqef_qatan | המזבחה | hmzbchh | onto the altar | `VAR_ha_mizbechah` |
| 9 | `LRRLL` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 10 | `LRRLR` | 2 | tifcha | העצים | h'tzym | the woods | `VAR_ha_etzim` |
| 11 | `LRRRC0` | 9 | munach | אשר | 'shr | which/that | — |
| 12 | `LRRRC1` | 9 | zero_conjunctive | על | 'l | on/upon | — |
| 13 | `LRRRC2` | 1 | etnachta | האש | h'sh | the fire | `VAR_ha_esh` |
| 14 | `RLLL` | 9 | munach | עלה | 'lh | burnt offering / goes up | `VAR_olah` |
| 15 | `RLLR` | 3 | revia | הוא | hv' | it is | — |
| 16 | `RLRL` | 3 | tevir | אשה | 'shh | fire-offering | `VAR_isheh` |
| 17 | `RLRRL` | 9 | mercha | ריח | rych | aroma of | `VAR_reach_nichoach` |
| 18 | `RLRRR` | 2 | tifcha | ניחח | nychch | soothing | `VAR_reach_nichoach` |
| 19 | `RR` | 1 | silluq | ליהוה | lyhvh | to YHWH | `VAR_la_YHWH` |

**Variables in this verse:**

| var_id | Hebrew | path | head mark | ranks/marks on span |
|--------|--------|------|-----------|---------------------|
| `VAR_reach_nichoach` | ריח ניחח | `RLRR` | tifcha | mercha,tifcha |
| `VAR_hiktir` | והקטיר | `LRLLC0` | qadma | qadma |
| `VAR_ha_kohen` | הכהן | `LRLLC2` | pashta | pashta |
| `VAR_ha_mizbechah` | המזבחה | `LRLR` | zaqef_qatan | zaqef_qatan |
| `VAR_ha_etzim` | העצים | `LRRLR` | tifcha | tifcha |
| `VAR_ha_esh` | האש | `LRRRC2` | etnachta | etnachta |
| `VAR_olah` | עלה | `RLLL` | munach | munach |
| `VAR_isheh` | אשה | `RLRL` | tevir | tevir |
| `VAR_la_YHWH` | ליהוה | `RR` | silluq | silluq |

<details><summary>Flat constituents (leaf-chains)</summary>

| path | head | chunk |
|------|------|-------|
| `LLL` | zinor | ושסע אתו בכנפיו |
| `LLR` | segol | לא יבדיל |
| `LRLL` | pashta | והקטיר אתו הכהן |
| `LRRL` | tifcha | על העצים |
| `LRRR` | etnachta | אשר על האש |
| `RLL` | revia | עלה הוא |
| `RLRR` | tifcha | ריח ניחח |

</details>

<details><summary>Full tree ASCII</summary>

```text
PHRASE (binary 20w) וְ/שִׁסַּ֨ע אֹת֣/וֹ בִ/כְנָפָי/ו֮ לֹ֣א יַבְדִּי…
├── PHRASE (binary 14w) וְ/שִׁסַּ֨ע אֹת֣/וֹ בִ/כְנָפָי/ו֮ לֹ֣א יַבְדִּי…
│   ├── PHRASE (binary 5w) וְ/שִׁסַּ֨ע אֹת֣/וֹ בִ/כְנָפָי/ו֮ לֹ֣א יַבְדִּי…
│   │   ├── PHRASE (3-ary 3w) וְ/שִׁסַּ֨ע אֹת֣/וֹ בִ/כְנָפָי/ו֮
│   │   │   ├── [0] וְ/שִׁסַּ֨ע (qadma (conjunctive), rank=9)
│   │   │   ├── [1] אֹת֣/וֹ (munach (conjunctive), rank=9)
│   │   │   └── [2] בִ/כְנָפָי/ו֮ (zinor (poetic cousin; rare in prose), rank=3)
│   │   └── PHRASE (binary 2w) לֹ֣א יַבְדִּיל֒
│   │       ├── [3] לֹ֣א (munach (conjunctive), rank=9)
│   │       └── [4] יַבְדִּיל֒ (segol, rank=2)
│   └── PHRASE (binary 9w) וְ/הִקְטִ֨יר אֹת֤/וֹ הַ/כֹּהֵן֙ הַ/מִּזְבֵּ֔חָ/…
│       ├── PHRASE (binary 4w) וְ/הִקְטִ֨יר אֹת֤/וֹ הַ/כֹּהֵן֙ הַ/מִּזְבֵּ֔חָ/ה
│       │   ├── PHRASE (3-ary 3w) וְ/הִקְטִ֨יר אֹת֤/וֹ הַ/כֹּהֵן֙
│       │   │   ├── [5] וְ/הִקְטִ֨יר (qadma (conjunctive), rank=9)
│       │   │   ├── [6] אֹת֤/וֹ (mahpach (conjunctive), rank=9)
│       │   │   └── [7] הַ/כֹּהֵן֙ (pashta, rank=3)
│       │   └── [8] הַ/מִּזְבֵּ֔חָ/ה (zaqef qatan, rank=2)
│       └── PHRASE (binary 5w) עַל הָ/עֵצִ֖ים אֲשֶׁ֣ר עַל הָ/אֵ֑שׁ
│           ├── PHRASE (binary 2w) עַל הָ/עֵצִ֖ים
│           │   ├── [9] עַל (no cantillation mark — bind as conjunctive, rank=9)
│           │   └── [10] הָ/עֵצִ֖ים (tifcha, rank=2)
│           └── PHRASE (3-ary 3w) אֲשֶׁ֣ר עַל הָ/אֵ֑שׁ
│               ├── [11] אֲשֶׁ֣ר (munach (conjunctive), rank=9)
│               ├── [12] עַל (no cantillation mark — bind as conjunctive, rank=9)
│               └── [13] הָ/אֵ֑שׁ (etnachta (major mid-verse rest), rank=1)
└── PHRASE (binary 6w) עֹלָ֣ה ה֗וּא אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ לַ/יהוָֽה
    ├── PHRASE (binary 5w) עֹלָ֣ה ה֗וּא אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ
    │   ├── PHRASE (binary 2w) עֹלָ֣ה ה֗וּא
    │   │   ├── [14] עֹלָ֣ה (munach (conjunctive), rank=9)
    │   │   └── [15] ה֗וּא (revia, rank=3)
    │   └── PHRASE (binary 3w) אִשֵּׁ֛ה רֵ֥יחַ נִיחֹ֖חַ
    │       ├── [16] אִשֵּׁ֛ה (tevir, rank=3)
    │       └── PHRASE (binary 2w) רֵ֥יחַ נִיחֹ֖חַ
    │           ├── [17] רֵ֥יחַ (mercha (conjunctive), rank=9)
    │           └── [18] נִיחֹ֖חַ (tifcha, rank=2)
    └── [19] לַ/יהוָֽה (silluq (verse-end emperor), rank=1)
```

</details>

---

## 5. Leaf-level patterns (for discussion)

### P1 — Operators are a multi-leaf chunk under pashta (1:5, 1:8, 1:11)

`בני אהרן הכהנים` appears as a **flat / near-flat** group with path under the **RIGHT** of etnachta, head often **pashta** on `הכהנים`.

### P2 — Slaughter is a disjunctive leaf on the LEFT of etnachta

`ושחט` at path `LLL` (1:5) / similar LEFT paths (1:11) with **tevir** — not in the priest chunk.

### P3 — Altar and blood share domains under zaqef/pashta on the RIGHT

Blood (`הדם`/`דמו`) and altar (`המזבח`) sit in RIGHT-side king/duke domains (zaqef, pashta), separate from slaughter.

### P4 — Tent entrance is a multi-leaf span ending at silluq

`פתח אהל מועד` paths under deep RIGHT (`RRR…`), last leaf **silluq** on `מועד`.

### P5 — Type menu (1:2) is RIGHT of etnachta as separate king domains

`הבהמה` / `הבקר` / `הצאן` each take leaf slots on the RIGHT type list — registry-shaped.

---

## 6. Limits (honest)

| Done | Not done |
|------|----------|
| Every leaf has mark + rank + path | Phase B earlier-book write sites |
| VAR ids tied to Hebrew leaves/spans | Full TIR role labels for glue words |
| Full tree ASCII per verse | Oral |
| English glosses for reading | Binding law claims |

**Gloss caveat:** English on leaves is `[EN-AID]` / small gloss table — **not** the derivation source. Hebrew leaf is.

**Matching caveat:** multi-leaf VARs use consecutive Hebrew tokens + tree paths. Compound “בני אהרן הכהנים” is visible as a flat constituent; catalog also lists `VAR_benei_aharon` and `VAR_ha_kohanim` separately so both surfaces stay addressable.

---

## 7. Discussion prompts

1. Does **path + mark + Hebrew leaf** feel like the right grain for variable names?
2. Should compound constituents (e.g. whole `בני אהרן הכהנים`) be **one** VAR or **two** linked VARs?
3. Ready for **Phase B** (write-site for each install VAR from earlier Written)?

---

## Changelog

- 2026-07-24: **Redo** Phase A at leaf level (all marks → full tree → leaf paths → VAR from Hebrew).
- 2026-07-24: Prior top-split-only ledger retained as historical; use this file going forward.
