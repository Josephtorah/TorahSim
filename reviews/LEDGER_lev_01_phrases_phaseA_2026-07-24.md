# Phase A — Leviticus 1 phrase ledger (verse + tree only)

> **SUPERSEDED (2026-07-24):** Leaf-level redo is in  
> **`LEDGER_lev_01_phaseA_LEAF_2026-07-24.md`** (+ `.json`).  
> This file kept only the **top-split** grain; do not use it for variable derivation.

**Date:** 2026-07-24  
**Kind:** finite free-phrase inventory — **Written only**  
**Status:** **superseded** by leaf-level Phase A  
**Not:** Oral, dry-runner, or “validated cross-book PASS” yet  

**Related:**  
- Step 1 storyboard: `REGISTRY_sanctuary_v0_2026-07-24.md`  
- Pointer styles: `architecture/ARCHITECTURE_pass2_pointers_2026-07-19.md`  
- Hebrew: `Data/Lev.xml` · trees: `taamim_tree_parse.py` v1  
- Units: `logic/units/lev_01_*.yaml`

**Rule for this phase:** every row is a **Hebrew surface** that actually appears in Lev 1, placed on the **LEFT or RIGHT** of that verse’s top ta'amim split. English is gloss only. No Exodus write-sites yet (that is Phase B). No Oral.

On substantive update: rename to today’s date and fix links.

---

## 0. How to read this (non-programmer)

For each verse we ask three simple questions:

1. **What does the verse say in Hebrew?** (word line)  
2. **How does the cantillation tree split it?** (LEFT half / RIGHT half — like a natural pause in the middle)  
3. **Which important phrases sit on which half?**  

Those phrases are our candidate **variable names** — because they are **words the text uses**, not labels we invented first.

```text
Verse words  →  tree top split  →  phrase on LEFT or RIGHT  →  (later Phase B: where was this written earlier?)
```

**Confidence for Phase A:** structure placement = **tested** (parser + Hebrew).  
“This is a cross-book variable” = **not claimed yet** (needs Phase B).

---

## 1. Method (short)

| Step | What we did |
|------|-------------|
| 1 | Load each Lev 1:1–17 from `Data/Lev.xml` |
| 2 | Parse ta'amim tree v1 (`taamim_tree_parse.py`) |
| 3 | Take the **top binary split** (first big LEFT / RIGHT) |
| 4 | Mark fixed Hebrew phrases (install names, offering types, acts) if present |
| 5 | Record **surface form** + **arm** + plain English |

**Not done yet:** linking to Exodus/Genesis; Oral; PASS/FAIL validation.

**Parser status:** all 17 verses `unique` (one clear tree each).

---

## 2. Inventory — unique phrases in Lev 1

Grouped for discussion. Counts = how many verses use the phrase (surface variants collapsed to dictionary form).

### 2.1 Install / environment candidates (expect Exodus write later)

| Hebrew | How to say | English | Verses in Lev 1 | Typical tree arm |
|--------|------------|---------|-----------------|------------------|
| מֵאֹהֶל מוֹעֵד | *me-ohel mo’ed* | **from** the Tent of Meeting | 1 | RIGHT |
| פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of the Tent of Meeting | 3, 5 | RIGHT |
| בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron | 5, 7, 8, 11 | both (see verses) |
| הַכֹּהֲנִים | *ha-kohanim* | the priests | 5, 8, 11 | with sons of Aaron |
| הַכֹּהֵן | *ha-kohen* | the priest | 7, 9, 12, 13, 15, 17 | both |
| הַמִּזְבֵּחַ | *ha-mizbeach* | the altar | 5, 7, 8, 11, 12, 15, 16 | both |
| הַמִּזְבֵּחָה | *ha-mizbechah* | onto the altar | 9, 13, 15, 17 | both |
| יֶרֶךְ הַמִּזְבֵּחַ | *yerech ha-mizbeach* | side of the altar | 11 | LEFT |
| קִיר הַמִּזְבֵּחַ | *kir ha-mizbeach* | wall of the altar | 15 | RIGHT |

### 2.2 Presence / address

| Hebrew | How to say | English | Verses | Typical arm |
|--------|------------|---------|--------|-------------|
| לִפְנֵי יְהוָה | *lifnei YHWH* | before YHWH | 3, 5, 11 | both |
| לַיהוָה | *la-YHWH* | to/for YHWH | 2, 9, 13, 14, 17 | both |
| יְהוָה | *YHWH* | YHWH | 1 (bare) | RIGHT |

### 2.3 App / procedure (local to offering — may join type tables later)

| Hebrew | How to say | English | Verses |
|--------|------------|---------|--------|
| אָדָם | *adam* | a person (who brings) | 2 |
| קָרְבָּן / קָרְבָּנוֹ / קָרְבַּנְכֶם | *korban / korbano / korbankhem* | offering / his / your | 2, 3, 10, 14 |
| הַבְּהֵמָה | *ha-behemah* | domestic animal class | 2 |
| הַבָּקָר / בֶּן־הַבָּקָר | *ha-bakar / ben ha-bakar* | cattle / cattle young | 2, 3, 5 |
| הַצֹּאן | *ha-tzon* | flock | 2, 10 |
| הָעוֹף | *ha-of* | bird | 14 |
| הַתֹּרִים | *ha-torim* | turtledoves | 14 |
| בְּנֵי הַיּוֹנָה | *benei ha-yonah* | young pigeons | 14 |
| עֹלָה / הָעֹלָה / לְעֹלָה | *olah / ha-olah / le-olah* | burnt offering | 3–4, 6, 9–10, 13–14, 17 |
| אִשֶּׁה | *isheh* | fire-offering | 9, 13, 17 |
| רֵיחַ נִיחֹחַ | *re’ach nichoach* | pleasing aroma | 9, 13, 17 |
| דָּם / הַדָּם / דָּמוֹ | *dam / ha-dam / damo* | blood / its blood | 5, 11, 15 |
| זָכָר | *zakhar* | male | 3, 10 |
| תָּמִים | *tamim* | unblemished | 3, 10 |

### 2.4 Acts (verbs that look like “operations”)

| Hebrew | How to say | English | Verses | Arm pattern (interesting) |
|--------|------------|---------|--------|---------------------------|
| וְסָמַךְ | *ve-samakh* | lean (hand) | 4 | LEFT with the olah |
| וְשָׁחַט | *ve-shachat* | slaughter | 5, 11 | **LEFT** |
| וְזָרְקוּ | *ve-zarku* | dash/throw blood | 5, 11 | **RIGHT** (with priests) |
| וְהִקְטִיר | *ve-hiktir* | turn to smoke | 9, 13, 15, 17 | with priest + altar |

### 2.5 Place details (may need write-site or local definition)

| Hebrew | How to say | English | Verse | Arm |
|--------|------------|---------|-------|-----|
| צָפֹנָה | *tzafonah* | northward | 11 | LEFT (with slaughter side) |
| מְקוֹם הַדֶּשֶׁן | *mekom ha-deshen* | place of the ashes | 16 | RIGHT |

### 2.6 People / agents

| Hebrew | How to say | English | Verse | Arm |
|--------|------------|---------|-------|-----|
| מֹשֶׁה | *Mosheh* | Moses | 1 | LEFT |
| בְּנֵי יִשְׂרָאֵל | *benei Yisrael* | children of Israel | 2 | LEFT |

---

## 3. Verse-by-verse ledger

For each verse: **linear Hebrew (unpointed plain)** → top split → phrases on each arm.

### Lev 1:1

| | |
|--|--|
| **Plain line** | ויקרא אל משה וידבר יהוה אליו מאהל מועד לאמר |
| **LEFT** | ויקרא אל משה — *call to Moses* |
| **RIGHT** | וידבר יהוה אליו מאהל מועד לאמר — *YHWH speaks from Tent* |

| Arm | Surface Hebrew | Translit | English | Kind |
|-----|----------------|----------|---------|------|
| LEFT | משה | *Mosheh* | Moses | agent |
| RIGHT | יהוה | *YHWH* | YHWH | divine_agent |
| RIGHT | מאהל מועד | *me-ohel mo’ed* | **from** the Tent of Meeting | install_env |

**Tree observation:** Tent is on the **speech half**, not the “call Moses” half.

---

### Lev 1:2

| | |
|--|--|
| **Plain line** | דבר אל בני ישראל … אדם כי יקריב מכם קרבן ליהוה מן הבהמה מן הבקר ומן הצאן … |
| **LEFT** | speech + person brings **קרבן ליהוה** |
| **RIGHT** | type list: **בהמה / בקר / צאן** + your offering |

| Arm | Surface | Translit | English | Kind |
|-----|---------|----------|---------|------|
| LEFT | בני ישראל | *benei Yisrael* | children of Israel | people |
| LEFT | אדם | *adam* | a person | agent |
| LEFT | קרבן | *korban* | offering | app_type |
| LEFT | ליהוה | *la-YHWH* | to/for YHWH | divine_agent |
| RIGHT | הבהמה | *ha-behemah* | domestic animal | app_type |
| RIGHT | הבקר | *ha-bakar* | cattle | app_type |
| RIGHT | הצאן | *ha-tzon* | flock | app_type |
| RIGHT | קרבנכם | *korbankhem* | your offering | app_type |

**Tree observation:** **Who/why** (LEFT) vs **from which animal class** (RIGHT). Clean type-registry shape.

---

### Lev 1:3

| | |
|--|--|
| **LEFT** | אם עלה קרבנו מן הבקר זכר תמים יקריבנו — *IF cattle olah, male, whole* |
| **RIGHT** | אל פתח אהל מועד … לפני יהוה — *to the entrance … before YHWH* |

| Arm | Surface | Translit | English | Kind |
|-----|---------|----------|---------|------|
| LEFT | עלה | *olah* | burnt offering | app_type |
| LEFT | קרבנו | *korbano* | his offering | app_type |
| LEFT | הבקר | *ha-bakar* | cattle | app_type |
| LEFT | זכר | *zakhar* | male | app_guard |
| LEFT | תמים | *tamim* | unblemished | app_guard |
| RIGHT | פתח אהל מועד | *petach ohel mo’ed* | entrance of Tent of Meeting | install_env |
| RIGHT | לפני יהוה | *lifnei YHWH* | before YHWH | presence_place |

**Tree observation:** **Case conditions** LEFT; **where to bring** RIGHT. Classic IF / location split.

---

### Lev 1:4

| | |
|--|--|
| **LEFT** | וסמך ידו על ראש העלה — *lean hand on head of the olah* |
| **RIGHT** | ונרצה לו לכפר עליו — *accepted for him, to atone* |

| Arm | Surface | Translit | English | Kind |
|-----|---------|----------|---------|------|
| LEFT | וסמך | *ve-samakh* | lean | app_act |
| LEFT | העלה | *ha-olah* | the burnt offering | app_type |

**Tree observation:** Act + object LEFT; result formula RIGHT (no new install names).

---

### Lev 1:5 — densest sanctuary verse

| | |
|--|--|
| **LEFT** | ושחט את בן הבקר לפני יהוה — *slaughter cattle young before YHWH* |
| **RIGHT** | והקריבו בני אהרן הכהנים את הדם וזרקו … על המזבח … פתח אהל מועד |

| Arm | Surface | Translit | English | Kind |
|-----|---------|----------|---------|------|
| LEFT | ושחט | *ve-shachat* | slaughter | app_act |
| LEFT | בן הבקר | *ben ha-bakar* | cattle young | app_type |
| LEFT | לפני יהוה | *lifnei YHWH* | before YHWH | presence_place |
| RIGHT | בני אהרן | *benei Aharon* | sons of Aaron | install_env |
| RIGHT | הכהנים | *ha-kohanim* | the priests | install_env |
| RIGHT | הדם | *ha-dam* | the blood | app_substance |
| RIGHT | וזרקו | *ve-zarku* | they dash (blood) | app_act |
| RIGHT | המזבח | *ha-mizbeach* | the altar | install_env |
| RIGHT | פתח אהל מועד | *petach ohel mo’ed* | entrance of Tent | install_env |

**Tree observation (important):**  
- **Slaughter** stays LEFT (bringer side / before YHWH).  
- **Priests + blood + altar + entrance** cluster RIGHT.  
That is finite structure, not our summary: the tree separates **kill act** from **priestly blood application at sanctuary furniture**.

---

### Lev 1:6

| LEFT | העלה — flay the olah | RIGHT | cut in pieces |

Only keyed phrase: **העלה** / *ha-olah* on LEFT. No new install names.

---

### Lev 1:7

| LEFT | בני אהרן הכהן … אש על המזבח | RIGHT | arrange wood on the fire |

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | בני אהרן | sons of Aaron |
| LEFT | הכהן | the priest |
| LEFT | המזבח | the altar |

---

### Lev 1:8

| LEFT | בני אהרן הכהנים + pieces | RIGHT | on wood/fire **on the altar** |

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | בני אהרן, הכהנים | priests arrange pieces |
| RIGHT | המזבח | altar as location of fire stack |

---

### Lev 1:9

| LEFT | wash innards/legs | RIGHT | priest turns all to smoke on altar; olah / isheh / aroma / to YHWH |

| Arm | Surface | English |
|-----|---------|---------|
| RIGHT | הכהן, המזבחה, עלה, אשה, ריח ניחוח, ליהוה | close of cattle path formula |

---

### Lev 1:10 — flock branch open

| LEFT | ואם מן הצאן … לעלה | RIGHT | זכר תמים יקריבנו |

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | הצאן, קרבנו, לעלה | flock as olah |
| RIGHT | זכר, תמים | male + unblemished guards |

**Tree observation:** animal/source LEFT; fitness guards RIGHT (compare 1:3 where guards were LEFT with cattle — same ideas, slightly different split shape).

---

### Lev 1:11 — flock slaughter / blood

Same **LEFT slaughter / RIGHT priests+blood+altar** pattern as 1:5, plus:

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | ירך המזבח, צפנה, לפני יהוה | north side of altar, before YHWH |
| RIGHT | בני אהרן, הכהנים, דמו, המזבח | priests dash its blood |

---

### Lev 1:12–13

| 12 LEFT | cut pieces | 12 RIGHT | priest arranges on altar fire |
| 13 LEFT | wash | 13 RIGHT | priest + smoke + olah/isheh/aroma formula (like 1:9) |

---

### Lev 1:14 — bird branch open

| LEFT | ואם מן העוף עלה קרבנו ליהוה | RIGHT | turtledoves **or** young pigeons |

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | העוף, עלה, קרבנו, ליהוה | bird olah to YHWH |
| RIGHT | התרים, בני היונה, קרבנו | allowed bird species |

**Tree observation:** class LEFT; **species choice** RIGHT.

---

### Lev 1:15

| LEFT | priest to altar, nip head, smoke on altar | RIGHT | blood on **wall of altar** |

| Arm | Surface | English |
|-----|---------|---------|
| LEFT | הכהן, המזבח, המזבחה, והקטיר | priest + altar ops |
| RIGHT | דמו, קיר המזבח | blood + altar wall |

---

### Lev 1:16

| LEFT | remove crop/feathers | RIGHT | throw beside altar eastward to **place of ashes** |

| Arm | Surface | English |
|-----|---------|---------|
| RIGHT | המזבח, מקום הדשן | altar + ash place |

**Note for Phase B:** `מקום הדשן` may be **local detail** or point earlier; do not assume Exodus install without checking.

---

### Lev 1:17

| LEFT | split bird, priest smokes on altar wood/fire | RIGHT | עלה הוא אשה ריח ניחח ליהוה formula |

Same closing formula cluster as 1:9 / 1:13 on RIGHT.

---

## 4. Patterns worth discussing (still Phase A only)

### Pattern P1 — Sanctuary furniture lives on the “application” half

In 1:5 and 1:11, **priests + blood + altar (+ entrance)** sit together on **RIGHT**, while **slaughter** sits **LEFT**.

That is the tree telling us a split of roles — not us inventing “variables,” but showing **which phrases travel together**.

### Pattern P2 — IF / place split on cattle open (1:3)

**LEFT:** if olah from cattle, male, whole.  
**RIGHT:** bring to **entrance of Tent**, before YHWH.

### Pattern P3 — Type registry open (1:2)

**LEFT:** person brings offering to YHWH.  
**RIGHT:** animal class menu (behemah → bakar / tzon). Bird added later as separate IF (1:14).

### Pattern P4 — Closing formula packet

`עלה` + `אשה` + `ריח ניחח` + `ליהוה` recur at path ends (1:9, 13, 17), usually **RIGHT**.

### Pattern P5 — Two “priest” surfaces

| Surface | Role feel in Lev 1 |
|---------|-------------------|
| בני אהרן הכהנים | group operators (blood, arrange) |
| הכהן | singular operator (smoke, bird path) |

Phase B should ask whether both resolve to the **same install** (Exod 28–29) or need a finer distinction.

---

## 5. Candidate “variable names” after Phase A

These are the **Hebrew keys** we should carry into Phase B (write-site hunt). English handles are secondary.

### Must-resolve (install-like)

1. אהל מועד / *ohel mo’ed* (incl. מאהל, פתח אהל מועד)  
2. בני אהרן / *benei Aharon*  
3. הכהן / הכהנים / *ha-kohen(im)*  
4. מזבח / *mizbeach* (incl. המזבחה, ירך, קיר)  
5. לפני יהוה / *lifnei YHWH* (presence/place formula)

### Must-classify (app / type / act)

6. קרבן family  
7. בהמה / בקר / צאן / עוף (+ torim, benei yonah)  
8. עלה family  
9. דם family  
10. Acts: סמך, שחט, זרק, הקטיר  
11. Guards: זכר, תמים  
12. Formula: אשה, ריח ניחח  

### Needs care (OPEN until Phase B)

13. מקום הדשן / *mekom ha-deshen* — place of ashes  
14. צפנה / *tzafonah* — northward (geometry of altar use)

---

## 6. Limits of Phase A (honest)

| Done | Not done |
|------|----------|
| Every listed phrase appears in the Hebrew of Lev 1 | Proof it was “declared” earlier |
| Tree arm for each | Full TIR role for every word |
| Readable ledger for discussion | Oral commentary |
| Candidate variable list | PASS/FAIL validation |

We intentionally **did not** attach Exodus verses here so Phase A stays “what Lev 1 actually says and how the tree groups it.”

---

## 7. Discussion prompts (stop here)

1. Do these **Hebrew surfaces** feel like the right grain for “variable names”?  
2. Is the **LEFT slaughter / RIGHT priests+altar** pattern (1:5, 1:11) the kind of finite signal you wanted?  
3. Anything **missing** you care about (e.g. אש / *esh* / fire, עצים / wood, כפר / atone)?  
4. Ready for **Phase B**: for each must-resolve phrase, attach the **earliest clear Written write-site** (mostly Exodus) — still no Oral unless a row stays stuck?

---

## Changelog

- 2026-07-24: Phase A ledger created for Lev 1:1–17 (verse + top tree arm + Hebrew surfaces).
