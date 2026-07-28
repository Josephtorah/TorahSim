# Derive from Genesis 1 + Mishnah (dual-track)

**Date:** 2026-07-24  
**Kind:** Written trees + named Mishnah · **not** binding law · does **not** rewrite Written  
**Lenses:** Pre-Code (Hebrew trees) + full-stack / Torah-scholar  
**Parser:** `taamim_tree_parse.py` v1 · `Gen.1.1` · `Gen.1.5` · `Gen.1.10` · `Gen.1.28` · (`Gen.5.2` companion)  

**Rule:** Hebrew first + transliteration + English. Mishnah is dual-track Oral only.

---

## Method (what we are doing)

```text
1. Full verse (Hebrew + free English)
2. Ta'amim tree (structure from cantillation)
3. Written cold notes (what the tree/words force)
4. Mishnah attachment (named locus + operation)
5. Derived claims — labeled hypothesis / tested-on-Mishnah-surface
```

We **do not** invent Lev IF rows from midrash. We only ask: *given this verse tree + this Mishnah use, what practice logic is licensed as Oral reading?*

---

# A. Genesis 1:5 — day / night naming + “one day”

## A1. Full verse

**Hebrew (OSHB/Gen.xml):**  
וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם אֶחָד

**Free English:**  
And God called the light “day,” and the darkness He called “night.” And there was evening and there was morning: **one day**.

### Key atoms (he + translit + en)

| he | translit | en |
|----|----------|-----|
| וַיִּקְרָא אֱלֹהִים | va-yikra Elohim | and God called / named |
| לָאוֹר יוֹם | la-or yom | to the light: day |
| וְלַחֹשֶׁךְ קָרָא לָיְלָה | ve-la-choshekh kara lailah | and to the darkness He called night |
| וַיְהִי עֶרֶב | va-yehi erev | and there was evening |
| וַיְהִי בֹקֶר | va-yehi boker | and there was morning |
| **יוֹם אֶחָד** | **yom eḥad** | **one day** |

## A2. Tree (`Gen.1.5` · v1)

```text
PHRASE (binary 13w)
├── LEFT (through etnachta): naming block
│   ├── call light → day   (… לָאוֹר֙ י֔וֹם)
│   └── call darkness → night (… קָרָא לָ֑יְלָה)  ← etnachta
└── RIGHT (to silluq): day-cycle close
    ├── evening + morning (וַיְהִי עֶרֶב … בֹ֖קֶר)
    └── **יוֹם אֶחָד** (י֥וֹם אֶחָֽד)  ← verse end
```

**Top split (structure):**  
**Name light/dark** ‖ **evening→morning → “one day.”**

The phrase Mishnah cares about sits in the **right half**, as the **label of the completed cycle**, not inside the naming of light alone.

## A3. Written cold notes

1. “Day” is both a **name for light** and a **unit closed by evening+morning**.  
2. Order forced in the close: **עֶרֶב / erev / evening** then **בֹקֶר / boker / morning**, then **יוֹם אֶחָד / yom eḥad**.  
3. Tree groups **yom eḥad** with the evening–morning pair (right of etnachta), not with “He called light day” alone.

## A4. Mishnah: **חֻלִּין / Chullin** 5:5

**שִׁמְעוֹן בֶּן זוֹמָא / Shimon ben Zoma:**  
“One day” in **מַעֲשֵׂה בְרֵאשִׁית / ma’aseh vereshit / work of creation** = day follows night.  
Same for **אוֹתוֹ וְאֶת בְּנוֹ / oto ve-et beno / “it and its young”** (Lev 22): one day = **night then day**.

## A5. Dual-track derivation

| id | claim | confidence | source |
|----|--------|------------|--------|
| W-1.5-a | A creation “day” is closed by evening→morning sequence | tested (verse wording + tree right branch) | Written Gen 1:5 |
| W-1.5-b | *Yom eḥad* labels that whole cycle | tested (position at silluq under evening/morning) | Written tree |
| M-CHUL-5.5 | Legal “one day” for mother/young slaughter ban uses **creation day boundary** (night→day) | tested on Mishnah surface | Oral: Chullin 5:5 |
| X-1 | Shared string **יוֹם אֶחָד** licenses gezerah-shavah-style import of day-boundary | hypothesis (Mishnah presents it; we don’t re-judge midrash rules) | Chullin 5:5 |

**Dev sketch (not a frozen unit):**

```text
DAY_BOUNDARY_CREATION = night_start → daylight_end   # from Gen 1:5 cycle
APPLY to: ban(slaughter mother AND young on same DAY_BOUNDARY_CREATION)
```

---

# B. Genesis 1:10 — dry land / water gathering / seas

## B1. Full verse

**Hebrew:**  
וַיִּקְרָא אֱלֹהִים לַיַּבָּשָׁה אֶרֶץ וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים וַיַּרְא אֱלֹהִים כִּי טוֹב

**Free English:**  
And God called the dry land “earth,” and the gathering of the waters He called “seas,” and God saw that it was good.

### Key atoms

| he | translit | en |
|----|----------|-----|
| לַיַּבָּשָׁה אֶרֶץ | la-yabashah eretz | to the dry land: earth |
| **וּלְמִקְוֵה הַמַּיִם** | **ul-mikveh ha-mayim** | **and to the gathering of the waters** |
| **קָרָא יַמִּים** | **kara yammim** | **He called seas** |
| כִּי טוֹב | ki tov | that it was good |

## B2. Tree (`Gen.1.10` · v1)

```text
PHRASE (binary 12w)
├── LEFT (to etnachta): two namings
│   ├── call dry land → earth     (… יַבָּשָׁה֙ אֶ֔רֶץ)
│   └── call water-gathering → seas
│         [וּלְמִקְוֵה הַמַּיִם] [קָרָא יַמִּ֑ים]  ← etnachta on יַמִּים
└── RIGHT: evaluation
    └── God saw that [it was] good
```

**Top split:** **Naming (land + seas)** ‖ **evaluation (good).**

Mishnah’s phrase is a **tight pair** under the left branch:  
**מקוה המים** (object named) + **ימים** (name given), balanced against land→earth.

## B3. Written cold notes

1. **מִקְוֵה / mikveh** here is “gathering/collection,” not yet the later technical pool — but the **same root-word** later law uses.  
2. Tree puts **mikveh ha-mayim** and **yammim** as one naming clause, parallel to **yabashah / eretz**.  
3. Seas = **named gathering of waters**, not “any wet thing.”

## B4. Mishnah: **מִקְוָאוֹת / Mikvaot** 5:4 = **פָּרָה / Parah** 8:8

- **Meir:** all seas ≅ mikveh — *shene’emar* Gen 1 naming.  
- **Yehudah:** only the great sea; “seas” = many kinds in it.  
- **Yose:** seas purify as flowing; invalid for zav/metzora and for mei ḥatat.

## B5. Dual-track derivation

| id | claim | confidence | source |
|----|--------|------------|--------|
| W-1.10-a | Waters have a **named gathered form** (*mikveh*) called seas | tested | Written |
| W-1.10-b | Land-naming ‖ sea-naming are structural twins (tree) | tested | Tree left branch |
| M-MIK-5.4 | Oral may treat **sea** as **mikveh-class water body** via this verse | tested on Mishnah | Mikvaot 5:4 |
| M-MIK-dispute | Scope of “seas” and which purity uses are allowed is **machloket** | tested | three opinions |
| X-2 | Bridge: creation vocabulary → purity water types (not: seas are Temple mikvaot) | hypothesis | dual-track |

**Dev sketch:**

```text
NAME(water_gathering) = seas
ORAL_READ (Meir): seas ⊆ mikveh_like
ORAL_READ (Yehudah): only great_sea ⊆ mikveh_like
ORAL_READ (Yose): seas purify_as flow; exclude(use=zav|metzora|hatat_water)
```

---

# C. Genesis 1:28 — bless them; be fruitful; fill; rule

## C1. Full verse

**Hebrew:**  
וַיְבָרֶךְ אֹתָם אֱלֹהִים וַיֹּאמֶר לָהֶם אֱלֹהִים פְּרוּ וּרְבוּ וּמִלְאוּ אֶת הָאָרֶץ וְכִבְשֻׁהָ וּרְדוּ בִּדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבְכָל חַיָּה הָרֹמֶשֶׂת עַל הָאָרֶץ

**Free English:**  
And God blessed them, and God said to them: Be fruitful and multiply and fill the earth and subdue it; and rule the fish of the sea and the birds of the heavens and every living thing that creeps on the earth.

### Key atoms

| he | translit | en |
|----|----------|-----|
| **וַיְבָרֶךְ אֹתָם** | **va-yevarekh otam** | **He blessed them** |
| **וַיֹּאמֶר לָהֶם** | **va-yomer lahem** | **He said to them** |
| **פְּרוּ וּרְבוּ** | **peru u-revu** | **be fruitful and multiply** |
| וּמִלְאוּ אֶת הָאָרֶץ | u-mil’u et ha-aretz | and fill the earth |
| וְכִבְשֻׁהָ | ve-khivshuha | and subdue it |
| וּרְדוּ… | u-redu… | and rule/have dominion… |

## C2. Tree (`Gen.1.28` · v1)

```text
PHRASE (binary 22w)
├── LEFT (to etnachta): bless + command-to-them through “subdue”
│   ├── bless them, God
│   └── say to them, God:
│         [peru u-revu] [fill the earth] … [ve-khivshuha]  ← etnachta
└── RIGHT: dominion domains
    └── rule fish / birds / land creepers
```

**Important for Mishnah:**  
**אֹתָם / otam / them** and **לָהֶם / lahem / to them** are both **plural**.  
**פְּרוּ וּרְבוּ** sits under the **speech-to-them** branch, not under dominion alone.

## C3. Written cold notes

1. Blessing and imperative speech are **paired** before dominion list.  
2. Addressees of *peru u-revu* are grammatically **them** (plural).  
3. Tree separates **fruitful/fill/subdue** (left, ends etnachta) from **rule over creatures** (right).

## C4. Mishnah: **יְבָמוֹת / Yevamot** 6:6

- Must not drop **פריה ורביה** until one has children.  
- Shammai: two males · Hillel: male+female (from **Gen 5:2**, not Gen 1).  
- Default: man commanded, not woman.  
- **R. Yoḥanan b. Beroka:** both — because Gen 1 says blessed **them** and said **to them** *peru u-revu*.

### Companion verse Hillel uses — Gen 5:2

**זָכָר וּנְקֵבָה בְּרָאָם / zakhar u-nekevah bera’am / “male and female He created them”**  
Tree: **[male + female] ‖ [created them]** as left unit under etnachta — pair as creation unit.

## C5. Dual-track derivation

| id | claim | confidence | source |
|----|--------|------------|--------|
| W-1.28-a | *Peru u-revu* is divine speech **to them** (plural) after blessing them | tested | Written + tree |
| W-1.28-b | Fruitful/fill/subdue is a different branch from “rule animals” | tested | Tree split |
| M-YEV-default | Surface majority line in mishnah: man obligated in periya u-reviya | tested on Mishnah | Yevamot 6:6 |
| M-YEV-YBB | Minority: both sexes — from **otam/lahem** in Gen 1:28 | tested on Mishnah | R. Yoḥanan b. Beroka |
| M-YEV-Hillel | Fulfillment metric male+female from Gen 5:2 wording | tested on Mishnah | Beit Hillel |
| X-3 | Gen 1:28 supplies **who is addressed**; Gen 5:2 supplies **what counts as pair-fulfillment** (for Hillel) | hypothesis | dual-track |

**Dev sketch:**

```text
COMMAND peru_u_revu:
  addressees: plural "them"          # Written
  obligated_subjects:
    default_mishnah: male
    ybb: male AND female             # Oral dispute
  done_when:
    shamai: sons >= 2
    hillel: male_child AND female_child   # Gen 5:2 oral metric
```

---

# D. Genesis 1 as block — Megillah 3:6 (lectionary)

## D1. Verse?

Megillah does **not** parse a single verse. It points to **מַעֲשֵׂה בְרֵאשִׁית (בראשית א) / ma’aseh vereshit (Genesis 1)** — the creation account as a **reading unit**.

Anchor opening **Gen 1:1** for completeness:

**בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ**  
*bereshit bara Elohim et ha-shamayim ve-et ha-aretz*  
“In the beginning God created the heavens and the earth.”

### Tree (`Gen.1.1`)

```text
PHRASE
├── [in beginning] [created God]     ← etnachta on אלהים area
└── [et heavens] [ve-et earth]
```

## D2. Mishnah operation

**Ma’amadot** public Torah reading = creation account (Genesis 1).

## D3. Derive

| id | claim | confidence |
|----|--------|------------|
| M-MEG-3.6 | Gen 1 functions as a **liturgical packet**, not only as midrash fuel | tested on Mishnah |
| X-4 | Mishnah can treat a **whole chapter** as an addressable unit | tested |

No purity/procreation rule is derived from Megillah’s use — only **event → reading assignment**.

---

# E. Synthesis: what we can derive overall

## From Written trees alone (no Oral)

1. Creation **day** is evening→morning labeled *yom eḥad* (1:5).  
2. **Seas** are the **named gathering (*mikveh*) of waters** (1:10).  
3. **Peru u-revu** is spoken **to them** after blessing them; dominion is a further branch (1:28).

## From Mishnah-on-those-verses (Oral, named)

| # | Derived practice logic | Mishnah |
|---|------------------------|---------|
| 1 | Legal “one day” for *oto ve-et beno* = **night→day** like creation | Chullin 5:5 |
| 2 | **Sea** may be classed with **mikveh** for some purity uses; dispute on which sea and which uses | Mikvaot 5:4 / Parah 8:8 |
| 3 | **Periya u-reviya** is a standing obligation with **child-count metrics** and a **who-is-commanded** dispute grounded in Gen 1 plural address | Yevamot 6:6 |
| 4 | Gen 1 is a **public lection** for ma’amadot | Megillah 3:6 |

## What we must **not** claim

- That Mishnah gives a full model of Gen 1 cosmology.  
- That Meir’s “all seas are mikveh” is the only or frozen law.  
- That Yevamot’s default “man only” or YBB’s “both” is decided here for this project — only that **both live on the Mishnah surface**.  
- That BR’s light/tohu theology is in these mishnayot (it is not).

## Unified dual-track picture

```text
Gen 1:5   DAY cycle text  ──Oral──►  day_boundary for slaughter pair-ban
Gen 1:10  SEA naming text ──Oral──►  water_type hierarchy (dispute)
Gen 1:28  BLESS+SPEAK them ──Oral──►  fertility obligation (+ who/metric disputes)
Gen 1:*   CREATION block  ──Oral──►  lectionary id for ma'amadot
```

**Full-stack one-liner:** Mishnah treats Gen 1 as a **shared constants library** (day, water-name, human mandate, reading packet), not as an application to interpret verse-by-verse.

**Torah-scholar one-liner:** The Oral law **specifies measures and duties** by hanging thin hooks on creation wording — while leaving the thick story of creation to midrash.

---

## F. Wired into Pre-Code units (2026-07-24)

Mishnah was **not** used as the derivation source when Gen boot units were first written (Written Hebrew + trees only; Oral stubs).  

**Update applied:** named dual-track `oral_notes` only — **no rewrite** of Written STEPs/exports.

| Verse | Unit | Oral note id |
|-------|------|----------------|
| 1:5 day cycle | `logic/units/gen_01_creation_boot.yaml` | `ORAL_mishnah_chullin_5_5` (+ Megillah 3:6, Chagigah) |
| 1:10 seas | `logic/units/gen_01_day3_land_plants.yaml` | `ORAL_mishnah_mikvaot_5_4` |
| 1:28 peru | `logic/units/gen_01_day6_land_human.yaml` | `ORAL_mishnah_yevamot_6_6` |

Scenarios added: Written export/NAME/BLESS unchanged when Oral is attached.
