# Genesis scan: את / *et* · גם / *gam* · אך / *akh* · רק / *raq* (include vs limit)

**Date:** 2026-07-25  
**Kind:** Written corpus scan + dual-track link to BR particle school — **not** binding law  
**Corpus:** `Data/Gen.xml` — **1533** verses · **~20,629** word tokens  
**Method:** Normalize OSHB words (strip ta'amim/points); count standalone surfaces את/ואת/גם/וגם/אך/רק + contexts  

**Related:**  
- BR school: `RESEARCH_BR_particles_2026-07-21.md` · `br_genesis_packets/BR_1_14_et.md`  
- Glue scan (spine): `sanctuary_spine_v1/SCAN_glue_morph_patterns_2026-07-25.md`  
- Gold את×3: `sanctuary_spine_v1/GOLD_lev_1_5_full_word_coverage_2026-07-25.md`

On substantive update: rename to today’s date and fix links.

---

## 0. School card vs Genesis counts

Bereshit Rabbah (Nahum → Akiva) names **two pairs**:

| Particle | Translit | School role | Plain English |
|----------|----------|-------------|---------------|
| **את** | *et* | **רבוי** / *ribui* | **Includer** — expand / fence object domain |
| **גם** | *gam* | **רבוי** / *ribui* | **Includer** — “also / even” expands set |
| **אך** | *akh* | **מיעוט** / *mi’ut* | **Limiter** — “but / only” narrows |
| **רק** | *raq* | **מיעוט** / *mi’ut* | **Limiter** — “only / except” narrows |

### Genesis surface counts (this scan)

| Surface | Translit | Count | Density |
|---------|----------|------:|---------|
| **את** | *et* | **668** | ~32 per 1000 words |
| **ואת** | *ve-et* | **210** | parallel “and-et” |
| **את + ואת total** | | **878** | object-marking system |
| **גם** | *gam* | **67** | |
| **וגם** | *ve-gam* | **25** | |
| **גם + וגם total** | | **92** | “also” system |
| **אך** | *akh* | **13** | sparse limiter |
| **רק** | *raq* | **11** | sparse limiter |

**Headline:** Genesis is **את-heavy** and **גם-medium**. **אך/רק** are **rare** but high-signal when they appear.

**Written grammar baseline:** את is primarily the **definite direct-object marker**. BR’s *ribui* is **dual-track Oral** on top of that — not a silent rewrite of grammar.

---

## 1. את / *et* — patterns in Genesis

### 1.1 Core Written job (dominant)

```text
VERB  +  את  +  DEFINITE_PATIENT
```

**Previous word** often a verb or name-as-subject:  
הוליד / *holid* / “begot”, ויקח / *va-yiqqah* / “he took”, ויקרא / *va-yiqra* / “he called”, אלהים / *Elohim*, אברהם / *Avraham*, יוסף / *Yosef*, …

**Next word** often:

| Next surface | Count | Role sketch |
|--------------|------:|-------------|
| כל / *kol* / “all” | 80 | **maximal object** (et + all X) |
| הארץ / *ha-arets* | 16 | land/earth patient |
| שמו / *shemo* / “his name” | 13 | naming formula |
| person names (יוסף, יצחק, יעקב…) | many | people as objects |
| בריתי / *beriti* / “my covenant” | 9 | covenant patient |
| האדם / *ha-adam* | 8 | the human |
| אלהים / יהוה | few | special cases (see BR demos) |

### 1.2 Pattern A — Domain pair (creation / dual objects)

**את X ואת Y** / *et X ve-et Y* / “et A and-et B”

Scan: **~57** tight *et … ve-et …* sequences; **189** verses with 2+ את/ואת; **85** with 3+.

**Flagship:** Gen 1:1  
את השמים ואת הארץ / *et ha-shamayim ve-et ha-arets* / “et the heavens and et the earth”

| Written job | Dual-track BR 1:14 |
|-------------|-------------------|
| Two definite creation domains as objects | *et* includes members under each domain (sun/moon…; plants/Eden…) |

Other clear pairs: father+mother (2:24), cherubim+sword (3:24), Shem+Ham+Yaphet (5:32, 6:10), city+tower (11:5), Sodom+Amora (13:10), etc.

**Code-like:**

```text
create(obj=[heavens, earth])     // dual et marks both domains
take(obj=[wife, Lot, property, souls])  // multi-et inventory
```

### 1.3 Pattern B — Inventory / roster *et* chains

Extreme multi-*et* verses (genealogy, plunder, family staging):

| Ref | *et* count | EN-AID sketch |
|-----|----------:|---------------|
| **Gen 36:6** | **7** | Esau took wives, sons, daughters, household souls, cattle, beasts, property… |
| **Gen 25:2** | **6** | Birth list: Zimran, Yoqshan, Medan… |
| **Gen 34:28** | **5** | Took flock, cattle, donkeys, city-goods, field-goods |
| **Gen 49:31** | **5** | Buried Abraham & Sarah, Isaac & Rebecca, Leah |
| **Gen 1:16** | **4** | Two great lights + stars |

**Pattern:** *et* enumerates **definite members of a take/beget/bury/create set**.  
This is Written **include-by-listing**. Closest natural cousin to BR *ribui* without requiring midrash.

### 1.4 Pattern C — *et kol* “et all …”

**כל** / *kol* / “all” is the **#1** next-word after את (80×).

```text
et + kol + NP  →  patient = entire class / total
```

Examples: wipe out **all** existence (flood), take **all** property, strike **all** field of Amalek, etc.

**Code-like:** `obj = entire(set)` — maximizer under the object marker.

### 1.5 Pattern D — Naming formula

```text
va-yiqra / va-tiqra  +  et  +  shemo  +  NAME
```

High **שמו** after *et*.  

**Job:** mark **the name** as definite object of “call.”  
Not expansion midrash by default — **label binding**.

### 1.6 Pattern E — *et* + divine name (high-signal, sparse)

Examples include:

| Ref | Surface sketch | BR dual-track relevance |
|-----|----------------|-------------------------|
| **Gen 4:1** | קניתי איש **את** יהוה | **BR 22:2 school demo** — without *et*, hard reading “man = YHWH”; with *et*, partnership / Shekhinah graph |
| Gen 5:22, 5:24, 6:9 | walk **את** האלהים | “with God” relational *et* (accompaniment sense in many readings) |
| Gen 24:48 | bless **את** יהוה | patient = YHWH of blessing |

**Written:** special object / accompaniment constructions.  
**Oral:** BR flags Gen 4:1 as **include/fence** particle school (not every *et*+YHWH gets a BR paragraph).

### 1.7 Pattern F — Genealogy engine

Huge share of *et* sits in **X begot *et* Y** chains (chs. 5, 10, 11, 25, 36…).

| Density | Chapters (high *et* rate) |
|---------|---------------------------|
| Highest | **10** (nations list), **22**, **11**, **34**, **14**, **5** |
| Lower | 18, 7, 38, 16… |

**Job:** each birth edge marks **child as definite object** of begetting — builds the **people graph** Genesis exports to later books.

### 1.8 What *et* is *not* (in Written scan)

| Not observed as primary job |
|-------------------------------|
| Free-standing “variable declaration” keyword |
| Automatic “expand to day-3 plants” on every *et* (BR 1:14 is **local** dual-track) |
| Same as **גם** (also) or **רק** (only) |

---

## 2. גם / *gam* · וגם / *ve-gam* — include / “also”

**Count:** 92 (67 גם + 25 וגם)

### 2.1 Dominant Written job: **add another participant or item to the set**

```text
BASE_ACT already in play
  + gam + ANOTHER_AGENT / ANOTHER_OBJECT / ANOTHER_TIME
```

**Recurring shapes:**

| Shape | Example (EN-AID) | Ref |
|-------|------------------|-----|
| **גם הוא** “he also” | Hevel also brought; Shet also fathered | 4:4, 4:26, 10:21… |
| **גם אני** “me too” | Esau: bless me also | 27:34, 27:38 |
| **וגם את X** “and also et X” | also Lot; also the nation; also the maid’s son | 14:16, 15:14, 21:13 |
| **גם … גם …** stacking | straw **also** fodder **also** place | 24:25 (triple) |
| **גם גמליך** | water camels **also** | 24:14, 19, 44, 46 |
| Family expansion | Leah also approached; Rachel also loved | 33:7, 29:30 |

### 2.2 Pattern G — *gam* as **set expansion operator** (Written-clear)

Closest Written match to BR **ribui**:

```text
action covers SET
gam adds member to SET (agent, patient, time, goods)
```

**Flagship multi-expand:** Gen 14:16  
returned **et** all goods, **ve-gam et** Lot, **ve-gam et** women **ve-et** people  

**Flagship agent stack:** Gen 43:8  
we die — **gam** we, **gam** you, **gam** our little ones  

### 2.3 Pattern H — *gam* + *et* cooperation

**25 verses** contain both גם/וגם and את/ואת.

Typical: **וגם את** = “and also [object-mark] X” — **include another definite patient**.

| Dual-track | Written |
|------------|---------|
| BR: *gam* is named *ribui* with *et* | Genesis shows *gam* expanding participants/objects in narrative |

### 2.4 What *gam* is *not*

| Not primary |
|-------------|
| Object marker (that’s *et*) |
| “Only / except” (that’s *akh*/*raq*) |
| Install free-name for sanctuary (wrong book layer) |

---

## 3. אך / *akh* — limit / “but only / just”

**Count:** 13 — each worth a card.

| Ref | Sketch (EN-AID) | Limit reading |
|-----|-----------------|---------------|
| **7:23** | remained **akh** Noah and those with him | survivor set **narrowed** to Noah’s group |
| **9:4** | **akh** flesh with its life-blood you shall not eat | **restrict** food: blood ban |
| **18:32** | speak **akh** this time | **limit** speech attempt to one more |
| **20:12** | she is my sister **akh** not daughter of my mother | **narrow** kinship claim |
| **23:13** | **akh** if you — listen to me | **restrict** negotiation condition |
| **26:9** | **akh** look, she is your wife | **contrastive** correction |
| **27:13** | **akh** listen to my voice | **focus** command |
| **27:30** | **akh** as Jacob left, Esau came | **narrow** timing “just as” |
| **29:14** | **akh** you are my bone and flesh | **affirmative limit** (“surely/only”) |
| **34:15, 34:22** | **akh** in this we agree: if you circumcise | **sole condition** for treaty |
| **34:23** | **akh** let us agree | **restrict** to this deal |
| **44:28** | I said **akh** torn he is torn | **limit** interpretation of fate |

### Pattern I — *akh* as **mi’ut / focus limiter**

```text
wide situation → akh → narrowed claim / condition / survivor / prohibition
```

Aligns with BR **מיעוט** label; Genesis uses it in **narrative and legal-ethical** micro-rules (blood; circumcision treaty).

---

## 4. רק / *raq* — limit / “only / nothing but”

**Count:** 11

| Ref | Sketch (EN-AID) | Limit reading |
|-----|-----------------|---------------|
| **6:5** | inclination of heart **raq** evil all day | moral state **only** evil |
| **14:24** | **raq** what the lads ate… | **except** / only that share |
| **19:8** | do as you wish to daughters; **raq** don’t harm the men | **except** the guests |
| **20:11** | I said **raq** there is no fear of God here | **only** (assessment) |
| **24:8** | **raq et** my son you shall not return there | **only** son must not go back — **BR 59:10** dual-track *raq* as mi’ut (son ≠ grandson) |
| **26:29** | we did **raq** good with you | **only** good (their claim) |
| **37:24** | pit was **raq** empty — no water | **only** empty (no water) |
| **41:40** | **raq** the throne I am greater | **except** throne rank |
| **47:22, 47:26** | **raq** priests’ land not bought | **except** priest land |
| **50:8** | **raq** little ones and flocks stayed in Goshen | **only** those left behind |

### Pattern J — *raq* as **exception / exclusive remainder**

```text
general rule or total scene
  raq → exception set OR exclusive property
```

Often near **לא** / *lo* / “not” (24:8, 47:22).

**Strongest dual-track hook:** Gen **24:8** *raq et beni* — named in BR particle research as **mi’ut** demo (limiter on *son*).

---

## 5. Include vs limit — Written map

```text
                    INCLUDE (ribui-like)              LIMIT (mi'ut-like)
                    ─────────────────                ─────────────────
Object / domain     את  (mark + list patients)       —
Also-expand set     גם / וגם                         —
Maximal patient     את כל …                          —
Exception/only      —                                אך · רק
Sole condition      —                                אך בזאת (34:15)
```

### Cooperation patterns

| Combo | Effect | Example |
|-------|--------|---------|
| **את + ואת** | include multiple objects | 1:1 heavens & earth |
| **וגם את** | include *another* marked object | 14:16 Lot; 21:13 maid’s son |
| **גם + את** same verse | expand agents and objects | 29:30, 30:15 |
| **רק את** | limit *which* object | 24:8 only my son |
| **אך** after wide destruction | survivor limit | 7:23 only Noah… |

---

## 6. Dual-track BR alignment (do not merge)

| BR locus | Genesis verse | Particle | School job |
|----------|---------------|----------|------------|
| BR **1:14** | Gen **1:1** | *et* ×2 | include under heavens/earth + anti-idol fence |
| BR **22:2** | Gen **4:1** | *et* YHWH | fence bad parse + relationship expand |
| BR **53:15** | Gen **21:20** | *et* the lad | fence + household expand |
| Applied *raq* | Gen **24:8** | *raq* | mi’ut generation scope (BR 59:10 family) |
| Applied *gam* | various | *gam* | ribui of patients/agents (BR toolkit) |

**Rule:** Written scan stands alone; BR is **named dual-track** when we deepen a row.

---

## 7. Implications for free names & “code”

| Particle | When generating precise logic |
|----------|-------------------------------|
| **את** | Always account as **object_marker**; following NP may be free name, person, domain, or *kol*-total |
| **ואת** | Parallel object include |
| **גם** | **set_add** member (agent/object/time) |
| **אך / רק** | **restrict** / **except** / **only** on claim or object |
| Multi-*et* lists | **inventory** under one verb |

**None of these particles is itself a sanctuary free name.**  
They are **operators on sets of names and patients** — first-class for precision, second-class for SYM_* install tables.

---

## 8. Stats appendix

| Metric | Value |
|--------|------:|
| Verses in Gen | 1533 |
| את | 668 |
| ואת | 210 |
| Verses with ≥2 את/ואת | 189 |
| Verses with ≥3 | 85 |
| Max את/ואת in one verse | 7 (36:6) |
| גם + וגם | 92 |
| אך | 13 |
| רק | 11 |
| Verses with גם and את | 25 |
| et+kol next | 80 |

---

## 9. Open questions / next scans

1. Tag every *et* as `object` vs `with/accompaniment` (walk with God) — needs sense pass.  
2. Full **et X ve-et Y** pair lexicon (creation, kinship, war booty).  
3. Same four-particle scan on **Exod–Deut** for density shift (law vs narrative).  
4. Gold coverage verse for **גם** stack (e.g. 24:25 or 43:8) and **רק את בני** (24:8).

---

## Changelog

- 2026-07-25: Full Genesis scan of et/gam/akh/raq; Written patterns A–J; counts; BR dual-track alignment.
