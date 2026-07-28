# Tree display mockup — FLAT parens + LEAF LEDGER + OSHB morphology (morpheme level)

**Date:** 2026-07-27
**Kind:** display-format mockup (owner-requested follow-up) · **not** binding law · **not** yet the locked canonical
**Rule set:** `v3` (`logic/taamim_rules/CURRENT`) — prose glue + binary dichotomy
**Interpreter:** `taamim_tree_parse.py`; segmentation below is real parser output
**Morphology:** OSHB `@lemma` / `@morph` from `Data/Gen.xml` · `Data/Lev.xml` — **#IMPOSED external aid, labeled** (Standing Decisions §5). Ta'amim own the tree; OSHB owns only word grammar.
**Parent mockup:** `MOCKUP_tree_display_flat_layers_ledger_2026-07-27.md` (adds LAYERS view; this file = FLAT + LEDGER + MORPH only, per owner preference)
**Prior morph format:** `../Parse_tree_2026-07-27/REPORT_simple_leaf_en_he_oshb_morph_2026-07-27.md` (per-leaf morph tables, word level). **This file goes one level finer: every morpheme segment — prefix letters and suffixes — gets its own row.**

---

## How to read the OSHB codes (legend)

OSHB tags each word; segments inside a word are separated by `/`. Leading `H` = Hebrew.

| Code piece | Meaning |
|------------|---------|
| `C` | conjunction (e.g. prefix וְ / ve / "and") |
| `R` | preposition (e.g. prefix לַ / la / "to", מִ / mi / "from") |
| `Td` | particle: definite article (prefix הַ / ha / "the") |
| `To` | particle: object marker (אֶת / et) |
| `Nc…` | common noun · then gender `m/f/b`(both) · number `s/p` · state `a`(absolute)/`c`(construct) |
| `Np` | proper noun (name) |
| `V` + stem + form + person | verb · stem `q`=qal `p`=piel `h`=hifil · form `w`=wayyiqtol(narrative past) `j`=jussive `v`=imperative `i`=imperfect `q`=weqatal(sequential "and you shall…") · then person-gender-number (`3ms` = he, `2mp` = you-plural) |
| `Sp…` | pronominal suffix (e.g. `Sp2mp` = "your/you (plural)") |
| lemma `c/…`, `d/…`, `l/…`, `m/…` | prefix-letter lemmas: `c`=ו and · `d`=ה the · `l`=ל to · `m`=מ from; the number after `/` is the Strong's id of the content word |

**Letters that are not standalone words** (they ride on the next word) and non-word signs:

| Sign | translit | en | OSHB treatment |
|------|----------|-----|----------------|
| וְ / וַ / וּ | ve / va / u | and | segment `C` inside the word |
| הַ | ha | the | segment `Td` |
| לַ | la | to | segment `R` |
| מִ | mi | from | segment `R` |
| ־הֶם | -hem | them | suffix segment `Sp3mp` |
| ־כֶם | -khem | you/your (pl.) | suffix segment `Sp2mp` |
| ־ (maqqef) | — | hyphen joining words | `seg` element, not a word (e.g. Gen 1:3 וַיְהִי־אוֹר / va-yehi–or) |
| ׃ (sof pasuq) | — | verse-end sign | `seg` element, not a word |

---

# 1 · Gen 1:3

## 1.1 FLAT — full verse, parens = leaf bricks

```text
### FLAT  Gen.1.3 · taamim v3 · prose · 6 words → 3 bricks

he:  (וַיֹּ֥אמֶר אֱלֹהִ֖ים) (יְהִ֣י א֑וֹר) (וַֽיְהִי־אֽוֹר)
tr:  (va-yomer Elohim) (yehi or) (va-yehi or)
en:  (and God said) (let there be light) (and there was light)

       B0                B1              B2      ← reading order; Hebrew line runs right-to-left
```

## 1.2 LEAF LEDGER

| B# | words | path | he | translit | en | end mark · rank | froze because | role (illustrative) |
|----|-------|------|-----------------|-----------------|------------------------|-----------------|--------------------------------|----------------|
| B0 | w0–1 | L·L | וַיֹּ֥אמֶר אֱלֹהִ֖ים | va-yomer Elohim | and God said | tifcha · r2 | only conjunctive mercha inside | SPEAK(Elohim) |
| B1 | w2–3 | L·R | יְהִ֣י א֑וֹר | yehi or | let there be light | etnachta · r1 | only conjunctive munach inside | CMD(light) |
| B2 | w4–5 | R | וַֽיְהִי־אֽוֹר | va-yehi or | and there was light | silluq · r1 | no disjunctive inside | RESULT(light) |

## 1.3 MORPH — every word and every morpheme letter (OSHB)

| B# | w | he | translit | en | OSHB code | grammar (English aid) |
|----|------|----------|----------|--------------|------------|------------------------|
| B0 | 0a | וַ | va | and | `C` | conjunction — prefix letter, not a standalone word |
| B0 | 0b | יֹּאמֶר | yomer | he-said | `Vqw3ms` | verb · qal · wayyiqtol (narrative past) · he — root אמר / amar / "say" (H559) |
| B0 | 1 | אֱלֹהִים | Elohim | God | `Ncmpa` | noun · masculine · plural form · absolute — Elohim (H430) |
| B1 | 2 | יְהִי | yehi | let-there-be | `Vqj3ms` | verb · qal · **jussive** ("let it…") · it — root היה / hayah / "be" (H1961) |
| B1 | 3 | אוֹר | or | light | `Ncbsa` | noun · either-gender · singular · absolute — or (H216) |
| B2 | 4a | וַ | va | and | `C` | conjunction — prefix letter |
| B2 | 4b | יְהִי | yehi | there-was | `Vqw3ms` | verb · qal · **wayyiqtol** (it happened) · it — root היה / hayah / "be" (H1961) |
| B2 | 5 | אוֹר | or | light | `Ncbsa` | noun — or (H216); joined to w4 by maqqef ־ |

**Grammar echo worth seeing:** B1's verb is יְהִי / yehi as **jussive** (command: "let there be") and B2's verb is the **same root, same letters** as wayyiqtol (narrative: "and there was") — the command/result pair the tree shows structurally (cut① separates them) is also in the morphology.

---

# 2 · Lev 1:2

## 2.1 FLAT — full verse, parens = leaf bricks

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

## 2.2 LEAF LEDGER

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

## 2.3 MORPH — every word and every morpheme letter (OSHB)

| B# | w | he | translit | en | OSHB code | grammar (English aid) |
|----|------|-----------|-----------|------------------|------------|------------------------|
| B0 | 0 | דַּבֵּר | dabber | speak! | `Vpv2ms` | verb · piel · **imperative** · you(ms) — root דבר / davar / "speak" (H1696) |
| B1 | 1 | אֶל | el | to | `R` | preposition (H413) |
| B1 | 2 | בְּנֵי | bnei | sons-of | `Ncmpc` | noun · masc · plural · **construct** ("sons-of…") — ben (H1121) |
| B1 | 3 | יִשְׂרָאֵל | Yisrael | Israel | `Np` | proper name (H3478) |
| B2 | 4a | וְ | ve | and | `C` | conjunction — prefix letter |
| B2 | 4b | אָמַרְתָּ | amarta | you-shall-say | `Vqq2ms` | verb · qal · **weqatal** (sequential "and you shall…") · you(ms) — root אמר / amar / "say" (H559) |
| B2 | 5a | אֲלֵ | alei | to | `R` | preposition (H413) — bound form of el |
| B2 | 5b | הֶם | hem | them | `Sp3mp` | pronoun suffix · them (masc pl) — suffix letters, not a word |
| B3 | 6 | אָדָם | adam | a person | `Ncmsa` | noun · masc · singular · absolute — adam (H120) |
| B4 | 7 | כִּי | ki | when/if | `C` | conjunction (H3588) — the legal trigger word |
| B4 | 8 | יַקְרִיב | yaqriv | he-brings-near | `Vhi3ms` | verb · **hifil** (causative: "cause to come near") · imperfect · he — root קרב / qarav / "come near" (H7126) |
| B4 | 9a | מִ | mi | from | `R` | preposition (H4480) — prefix letter |
| B4 | 9b | כֶּם | kem | you (pl.) | `Sp2mp` | pronoun suffix · you (masc pl) |
| B5 | 10 | קָרְבָּן | qorban | offering | `Ncmsa` | noun · masc · singular · absolute — qorban (H7133); same root קרב as the verb |
| B6 | 11a | לַ | la | to | `R` | preposition — prefix letter |
| B6 | 11b | יהוָה | YHWH | the LORD | `Np` | proper name (H3068) |
| B7 | 12 | מִן | min | from | `R` | preposition (H4480) — standalone form |
| B7 | 13a | הַ | ha | the | `Td` | definite article — prefix letter |
| B7 | 13b | בְּהֵמָה | behemah | livestock | `Ncfsa` | noun · feminine · singular · absolute (H929) |
| B8 | 14 | מִן | min | from | `R` | preposition |
| B8 | 15a | הַ | ha | the | `Td` | definite article — prefix letter |
| B8 | 15b | בָּקָר | baqar | herd | `Ncbsa` | noun · either-gender · singular (H1241) |
| B9 | 16a | וּ | u | and | `C` | conjunction — prefix letter |
| B9 | 16b | מִן | min | from | `R` | preposition |
| B9 | 17a | הַ | ha | the | `Td` | definite article — prefix letter |
| B9 | 17b | צֹּאן | tzon | flock | `Ncbsa` | noun · either-gender · singular (H6629) |
| B10 | 18 | תַּקְרִיבוּ | taqrivu | you-shall-bring | `Vhi2mp` | verb · hifil · imperfect · **you (plural)** — root קרב (H7126); person shift he→you-pl |
| B11 | 19 | אֶת | et | (object marker) | `To` | particle · **object marker** (H853) — a word that is pure grammar (TIR-014) |
| B11 | 20a | קָרְבַּנְ | qorban- | offering-of | `Ncmsc` | noun · masc · singular · **construct** — bound to its suffix (H7133) |
| B11 | 20b | כֶם | khem | your (pl.) | `Sp2mp` | pronoun suffix · your (masc pl) — suffix letters, not a word |

**Grammar echoes worth seeing:**
- Root קרב / q-r-v runs through the verse three ways: יַקְרִיב / yaqriv (he brings, B4) → קָרְבָּן / qorban (offering, B5/B11) → תַּקְרִיבוּ / taqrivu (you-pl bring, B10). The tree's case→rule split (cut① at etnachta) is mirrored by the person shift **he** (`3ms`) → **you plural** (`2mp`).
- Every "from" is real morphology: standalone מִן / min (w12, w14), prefix מִ / mi (w9a), and conjoined וּמִן / u-min (w16) — OSHB codes each one, so the SET/SUBSET reading of B7–B9 rests on tagged prepositions, not on English.

---

# 3 · Provenance split (who owns what)

| Layer | Owner | In this file |
|-------|-------|--------------|
| Leaf boundaries, parens, brick order, end marks | **Ta'amim** (our v3 rules) | FLAT + LEDGER |
| Word/segment grammar (lemma, stem, person, suffixes) | **OSHB** — labeled #IMPOSED aid | MORPH tables |
| English glosses, transliterations | free EN-AID (owner English-only) | everywhere |
| Role column | illustrative; real work = TIR in units | LEDGER only |

Reproduce structure: `python3 taamim_tree_parse.py Gen.1.3 --tree` · morph: `<w lemma= morph=>` in `Data/Gen.xml`, `Data/Lev.xml` (join by word index; alignment verified — parser word count == OSHB word count on both verses).

**Status:** candidate format. Prior word-level morph format: `logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md` (ACTIVE). If this morpheme-level FLAT+LEDGER+MORPH composite should replace or join it, that's an owner order — I'll update the display docs and log the decision.
