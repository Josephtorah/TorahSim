# Architecture Pass 3 — Type registries and data tables in the Written Torah

**Date:** 2026-07-19  
**Kind:** architecture scan (hypothesis / working model — not binding law)  
**Pass:** 3 of multi-pass series  
**Question:** Where does the Written store **type data** (lists, classes, offices, times), and how do those tables **join**?  
**Prior:**  
- `ARCHITECTURE_discussion_2026-07-19.md`  
- `ARCHITECTURE_pass1_five_books_2026-07-19.md`  
- `ARCHITECTURE_pass2_pointers_2026-07-19.md`  

**Corpus:** `Data/{Gen,Exod,Lev,Num,Deut}.xml`. Counts = verses containing a normalized Hebrew term (morph `/` and cantillation stripped). Some terms are noisy (noted).

On update: rename to today’s date; fix links.

---

## 0. Pass 3 in one sentence

The Written Torah does not only “run procedures”; it **declares registries** — animals, purity states, offices, offering types, times, land/people — and later code **reads and joins** those tables by shared Hebrew keys.

---

## 1. What counts as a “registry” here

| Kind | Meaning | Written signals |
|------|---------|-----------------|
| **Type enum** | Allowed/forbidden classes | “from cattle / flock / bird”; “these you may eat” |
| **Closed list** | Named members | unclean birds; priest garments; blemishes |
| **Role table** | Who may act | priests, levites, nazir, judges |
| **State labels** | Status vocabulary | טמא / *tame* / impure; טהור / *tahor* / pure |
| **Time table** | Calendar keys | mo’adim, shabbat, pesach, yovel |
| **Procedure index** | Named torah-of-X | זאת תורת / *zot torat* / “this is the torah of…” |
| **People graph** | Names, tribes, counts | toldot, censuses, inheritance |

**Explicit index headers (rare but strong):**

- **זאת תורת** / *zot torat* / “this is the instruction/law of…” — **14 hits**, almost all **Lev** (11) + **Num** (3).  
- **אֵלֶּה הַמִּצְוֹת** / *elleh ha-mitzvot* / “these are the commandments” — book seals (Lev 27:34; Num 36:13).  
- **וְאֵלֶּה הַמִּשְׁפָּטִים** / *ve’elleh ha-mishpatim* / “and these are the rules” — Exod 21:1 (covenant code open).

**Pass 3 claim:** Leviticus is the **primary registry warehouse** for cult/purity; Exodus writes **office and build** tables; Numbers adds **logistics and patches**; Deuteronomy **recompiles** select tables for land life; Genesis seeds **taxonomy vocabulary and people data**.

---

## 2. Density snapshot (verse hits by book)

Useful as **where the vocabulary lives**, not as exact theology counts.

| Domain term | Gen | Exod | Lev | Num | Deut | Read as |
|-------------|----:|-----:|----:|----:|-----:|---------|
| טמא *tame* impure | 3 | 0 | **107** | 30 | 10 | Purity registry home = **Lev** |
| כהן *kohen* priest | 6 | 14 | **152** | 64 | 13 | Priest ops = **Lev**; install Exod; field Num |
| לוי *levi* | 6 | 9 | 3 | **65** | 27 | Levite logistics = **Num** |
| חטאת *chatat* | 8 | 11 | **66** | 42 | 6 | Sin-offering table = **Lev** (+Num) |
| אשם *asham* | 2 | 0 | **30** | 4 | 1 | Guilt-offering = **Lev** |
| שלמים *shelamim* | 1 | 2 | **22** | 17 | 1 | Peace-offering = **Lev/Num** |
| צרעת *tzara’at* | 0 | 1 | **27** | 1 | 1 | Scale-disease = **Lev 13–14** |
| שרץ *sheretz* swarmers | 2 | 1 | **12** | 0 | 1 | Food/swarm table = **Lev 11** |
| מום *mum* blemish | 2 | 0 | **9** | 1 | 2 | Blemish list = **Lev 21–22** |
| יובל *yovel* jubilee | 1 | 0 | **7** | 0 | 0 | Jubilee = **Lev 25** |
| מועד *mo’ed* appointed time | 4 | 37 | 44 | **60** | 2 | Calendar thick Exod–Num; land restate Deut festivals elsewhere |
| פסח *pesach* | 0 | 8 | 2 | 10 | 5 | Multi-book festival key |
| שבת *shabbat* | 15 | 29 | 36 | 13 | 24 | Cross-corpus time key |
| בהמה *behemah* | 17 | 19 | 22 | 7 | 7 | Shared animal key (multi-table) |
| בקר *bakar* cattle | 43 | 53 | 32 | **68** | 36 | High in narrative + offerings |
| נחלה *nachalah* inheritance | 1 | 0 | 0 | 12 | **18** | Land registry = **Num/Deut** |
| ארץ *eretz* land | **223** | 98 | 54 | 92 | 145 | Genesis seeds land theme |

**Noise note:** some patterns over-hit (e.g. זב-family false friends). Prefer **locus lists** below over raw counts for those.

---

## 3. Master map of major registries

### R1 — Creature / animal taxonomy

| Registry | Home (Written) | What it stores | Joins to |
|--------------------------|----------------|----------|
| **Creation kinds** | Gen 1:21–25; 7:14 | בהמה / חיה / רמש / עוף by kind | Later “animal” vocabulary |
| **Clean/unclean for flood** | Gen 7:2 | pure vs not-pure animals (7/7 vs 2/2) | Seed of food purity idea |
| **Offering input types** | **Lev 1–7** (esp. 1:2, 1:10, 1:14; 3:1) | cattle / flock (sheep/goat) / birds (turtledove, pigeon); sex/flags per case | Altar procedure; priest ops |
| **Food creatures** | **Lev 11** (summary 11:46) | land animals, water (fins/scales), birds (named reject list), swarmers | Deut 14 restate; offering-behemah join risk |
| **Food creatures (land restatement)** | **Deut 14:3–21** | parallel table + land framing | Lev 11 |

**Architectural point for Lev 1:** offering channel is a **local type table** in Lev 1, not a copy of Lev 11. Same word בהמה invites a **join**; Oral hardens boundaries (Pass 2 P-JOIN).

**Sample keys (he + sense):**

- Lev 1:2 — מִן הַבְּהֵמָה מִן הַבָּקָר וּמִן הַצֹּאן / *min ha-behemah min ha-bakar u-min ha-tzon* / from the animal, cattle, and flock.  
- Lev 1:14 — מִן הַתֹּרִים אוֹ מִן בְּנֵי הַיּוֹנָה / *min ha-torim o min benei ha-yonah* / turtledoves or young pigeons.  
- Lev 11:2 — זֹאת הַחַיָּה אֲשֶׁר תֹּאכְלוּ / *zot ha-chayyah asher tokhelu* / this is the living thing you may eat…  
- Deut 14:4 — זֹאת הַבְּהֵמָה אֲשֶׁר תֹּאכֵלוּ שׁוֹר שֵׂה כְשָׂבִים… / *zot ha-behemah… shor seh khesavim* / this is the animal you may eat: ox, sheep, goat…

---

### R2 — Offering-type registry (korban menu)

| Type | Primary Written home | Index signal |
|------|----------------------|--------------|
| עולה / *olah* / burnt | Lev 1; procedures Lev 6:2 “torah of olah” | זאת תורת העולה |
| מנחה / *minchah* / grain | Lev 2; 6:7 | זאת תורת המנחה |
| שלמים / *shelamim* / peace | Lev 3; 7:11 | זאת תורת זבח השלמים |
| חטאת / *chatat* / sin | Lev 4–5; 6:18 | זאת תורת החטאת |
| אשם / *asham* / guilt | Lev 5; 7:1 | זאת תורת האשם |
| מלאים / *millu’im* / ordination | Lev 8 context; listed Lev 7:37 | bundle index |
| **Bundle index** | **Lev 7:37** | “this is the torah for olah, minchah, chatat, asham, millu’im, shelamim” |
| Public schedule expansion | **Num 28–29** | daily/Sabbath/new moon/festival quantities |
| Continuity / tamid seed | Exod 29:38–42 | continual offering at Tent entrance |

**Pass 3 claim:** Lev 1–7 is the **canonical offering type DB + procedures**. Num 28–29 is a **schedule/quantity view** on related types. Exodus supplies **environment + some continuous service**.

---

### R3 — Purity / body / fabric state registries

| Registry | Home | Nature |
|----------|------|--------|
| Food purity | Lev 11 | type lists + טמא/טהור labels |
| Childbirth | Lev 12 | time-state machine (male/female paths) — project unit exists |
| Scale disease (person) | Lev 13–14 | diagnostic states + purification pipeline |
| Scale disease (garment/house) | Lev 13:47+; 14:33+ | object states |
| Genital discharges | Lev 15 | zav / niddah-related states |
| Summary torah lines | Lev 12:7; 13:59; 14:32, 14:57; 15:32 | registry seals |
| Corpse-related water | Num 19 (red heifer) | field purity patch |
| Camp purity uses | Num 5 | applies purity ideas to camp |

**Density:** טמא verses peak in **Lev (107)**. That is the purity **namespace capital**.

**Pre-Code fit:** these blocks are natural **FSM / decision-table** units (already seen with Lev 12).

---

### R4 — Blemish / fitness registries (who/what may approach)

| Registry | Home | Stores |
|----------|------|--------|
| Priest bodily defects | **Lev 21:17–23** | list: blind, lame, etc. — may not offer bread of God |
| Animal defects for altar | **Lev 22:21–24** | list: blind, broken, etc. — not for vow/offering acceptance |
| “No blemish” constraint | Lev 1:3; 22:21 | תמים / *tamim* / whole — flag on type |

These are **validation tables** on agents (priests) and inputs (animals) — exactly the “acceptable data entry” hunch, now with **named defect enums** in Writing.

---

### R5 — Office / role registries

| Role | Install / define | Operate / expand |
|------|------------------|------------------|
| **Priests (Aaronic)** | Exod 28–29 (names, garments Exod 28:4, consecration) | Lev ritual ops (כהן density peak); rights Lev 6–7; Num 18 burden |
| **Levites** | Exod/Num tribe; **Num 3–4** duties by clan | Num logistics; Deut “levitical priests” provisions |
| **Nazir** | **Num 6** (זאת תורת הנזיר) | Special vow state machine |
| **Judges / priests at chosen place** | Deut 17:8–9 | Land judicial resolve path |
| **Census subjects** | Exod 30:11–16; **Num 1; 26** | Who is counted, by tribe |

**People data seeds:** Gen 46 names; Exod 1 names; Exod 6:16 Levi line — **graph** that Num census keys attach to.

---

### R6 — Time / calendar registries

| Table | Home | Contents |
|-------|------|----------|
| Sabbath | Exod 20:8–11; Exod 31; Lev 23; Deut 5:12–15 | weekly key + dual motivation (creation / exodus) |
| Festival calendar | **Lev 23** (אֵלֶּה מוֹעֲדֵי יְהוָה) | Pesach, matzot, omer/shavuot, trumpets, kippur, sukkot |
| Early festival sketch | Exod 23:14–17; 34:18–23 | three pilgrimage frame |
| Pesach origin | Exod 12 | memorial + first statute-in-Egypt |
| Public korban calendar | **Num 28–29** | quantities per day/type |
| Land festival restatement | **Deut 16** | Pesach/shavuot/sukkot for land life |
| Sabbatical / jubilee | **Lev 25** | 7-year and 50-year land/time economy |
| Day of Atonement date | Lev 16:29; 23:27 | 7th month, 10th day |

**Join example (Pass 2 continued):** Pesach key appears in Exod 12 (origin), Lev 23:5 (date), Num 28:16 (public offerings), Deut 16:1 (land practice + Egypt reason).

---

### R7 — Space / land / sanctuary object registries

| Table | Home | Contents |
|-------|------|----------|
| Mishkan parts & vessels | **Exod 25–31; 35–40** | blueprint data (what to build) |
| Camp layout | **Num 2–3** | tribes around Tent — spatial graph |
| Cities of refuge | **Num 35** | six + levitical cities |
| Inheritance rules | Num 27; 36; **Deut** nachalah language | who holds land |
| Chosen worship place | **Deut 12** | policy key for land (vs Tent entrance in Lev) |

---

### R8 — “Torah of X” procedure index (meta-registry)

Full **זאת תורת** list from scan:

| Ref | Subject |
|-----|---------|
| Lev 6:2 | olah |
| Lev 6:7 | minchah |
| Lev 6:18 | chatat |
| Lev 7:1 | asham |
| Lev 7:11 | shelamim |
| Lev 11:46 | behemah + of + water + sheretz (food creatures summary) |
| Lev 12:7 | yoledet (childbirth) |
| Lev 13:59 | tzara’at of garment |
| Lev 14:32 | metzora who cannot afford |
| Lev 14:57 | tzara’at (general) |
| Lev 15:32 | zav |
| Num 5:29 | jealousy / sotah procedure |
| Num 6:13, 6:21 | nazir |

**Architecture:** these lines are **named modules** — the Written’s own table of contents for procedure packets. Gold for Pre-Code unit boundaries.

---

## 4. How registries relate to “code + data”

```text
REGISTRY (data)              CODE (rules/pipelines)
─────────────────            ──────────────────────
animal types Lev 1      →    if olah from cattle… procedure 1:3–9
food types Lev 11       →    may/may-not eat; impurity consequences
blemish lists Lev 22    →    may not bring for altar favor
priest defect Lev 21    →    may not approach to offer
mo’adim Lev 23          →    what to do on date D
census Num 1            →    who serves / camps where
```

**Exodus** often writes **environment data** (Tent parts, priest garments) that Lev **code** imports (Pass 2).  
**Leviticus** co-locates **many registries + the procedures that use them**.  
**Numbers** adds **views** (schedules, censuses) and **patches** (nazir, red heifer, refuge).  
**Deuteronomy** **recompiles** selected registries for land (food, festivals, officials).

---

## 5. Book-by-book registry role (Pass 3 view)

### Genesis — seed vocab + people graph

- Creature kinds (Gen 1).  
- Pure/not-pure animals in flood logistics (Gen 7:2) — early purity **bit**.  
- Toldot / name lists (e.g. Gen 10; 46:8) — **people data**.  
- Almost no cult type menu, no Tent object registry.

### Exodus — build data + covenant code open + festival seeds

- Mishkan/vessel **parts list** (25–31).  
- Priest **names and garments** (28).  
- Mishpatim corpus open (21:1).  
- Pesach and pilgrimage **seeds**.  
- Census/atonement silver (30:11–16).  
- Not the full korban type DB (that’s Lev).

### Leviticus — registry capital

- Offering types + torah-of-X index.  
- Food purity table.  
- Body/fabric purity state systems.  
- Blemish validators.  
- Holiness / sexual boundary tables (18+).  
- Mo’adim calendar.  
- Sabbatical/jubilee time-economy.  
- Book seal: “these are the mitzvot…” (27:34).

### Numbers — logistics tables + extensions

- Census and camp graphs.  
- Levite duty tables.  
- Nazir module.  
- Public offering quantities (28–29).  
- Refuge cities.  
- Inheritance edge cases.  
- Book seal in plains of Moab (36:13).

### Deuteronomy — recompiled subsets for land

- Food table restatement (14).  
- Festival practice (16).  
- Officials / judicial path (17–18).  
- Social/family case law clusters (21–25) — more **case code** than enum lists.  
- Memory-heavy (Pass 2); fewer new cult type enums than Lev.

---

## 6. Join graph (high value edges)

```text
[Gen creature kinds] ──vocab──► [Lev 11 food] ──parallel──► [Deut 14 food]
         │                              │
         │                              │ P-JOIN risk on "behemah"
         └──────────────────────────────┼──► [Lev 1 offering types]
                                        │
[Exod Tent/priests] ──import──► [Lev 1–16 procedures]
[Exod 12 Pesach] ──key──► [Lev 23] ──► [Num 28] ──► [Deut 16]
[Lev 23 mo'adim] ──detail──► [Num 28–29 quantities]
[Gen tribes] ──keys──► [Num 1/26 census] ──► [Num 34–36 / Deut land]
[Lev purity labels] ──apply──► [Num 5 camp] [Num 19 corpse]
```

---

## 7. Implications for Torah_Grok / Pre-Code

1. **Unit scoping:** prefer boundaries near **זאת תורת** seals and clear type opens (Lev 1:2; 11:2; 23:2).  
2. **Dual fields in YAML:**  
   - `registry:` local types declared in-unit  
   - `import_registry:` e.g. `Exod.priests`, `Exod.Tent`  
   - `join_risk:` e.g. `behemah → Lev.11 / Deut.14`  
3. **Lev 1 work:** treat cattle/flock/bird as **R1 offering registry**; Oral exclusions as validators **on** that registry, not as the registry itself.  
4. **Do not** dump all animal law into one unit — **R1 has multiple tables**.  
5. **Pass 4** can measure: for free names in Lev 1–7, % resolving to R5/R7 Exodus vs R1/R2 local.

---

## 8. Confidence

| Claim | Label |
|-------|--------|
| Lev holds densest purity/offering/blemish registries | **tested** (loci + density) |
| זאת תורת marks procedure modules | **tested** (full list extracted) |
| Num 28–29 is schedule view on offering types | **hypothesis** (strong structural) |
| Deut 14 “is” Lev 11 | **hypothesis** — parallel table / recompile, not proven identity |
| zav-term raw counts | **noisy** — do not use without manual check |

---

## 9. Bottom line

**Pass 3 result:** The Written Torah carries explicit **data tables**:

- **Animals** (offering vs food vs creation kinds)  
- **Offering types** (with a written index at Lev 7:37 and torah-of-X headers)  
- **Purity states and diagnostic modules**  
- **Blemish validators**  
- **Offices** (priest, levite, nazir, judges)  
- **Times** (Sabbath, mo’adim, shemittah/yovel)  
- **Space/people** (Tent parts, camp, census, inheritance)  

**Leviticus** is the main warehouse for cult/purity data **and** the code that uses it.  
**Exodus** supplies build/office data.  
**Numbers** supplies logistics and expansions.  
**Deuteronomy** recompiles selected tables for the land.  
**Genesis** seeds kinds and people.

That supports the owner theory: **the run looks up data inside the Written** — and Pass 3 names **where those tables live**.

---

## 10. Next pass options

| Pass | Focus |
|------|--------|
| **4** | Sanctuary spine free-name resolve sample — **done:** `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md` |
| **5** | Legal genre mix (casuistic IF vs sequence vs speech frame) by book |
| **Segment** | Freeze one registry into Pre-Code (e.g. R1 offering types for Lev 1 only) |

**Recommended:** Pass 4 (measure the Exodus import rate) **or** a thin Pre-Code registry block for Lev 1 types using this map.
