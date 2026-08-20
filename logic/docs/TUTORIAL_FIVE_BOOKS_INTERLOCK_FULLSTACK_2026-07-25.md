# Tutorial: Five books of Torah as one system — how they interlock

### For full-stack developers · You do **not** need to speak Hebrew

**Date:** 2026-07-25  
**Kind:** architecture tutorial — experimental model, **not** binding religious law  
**Status:** living  
**Lens:** sequential run + internal data + content pointers (declare / use)  

**Related:**  
- Declare/use method: `TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md`  
- Pass 1 roles: `reviews/architecture/ARCHITECTURE_pass1_five_books_2026-07-19.md`  
- Pointers: `reviews/architecture/ARCHITECTURE_pass2_pointers_2026-07-19.md`  
- Registries: `reviews/architecture/ARCHITECTURE_pass3_registries_2026-07-19.md`  
- Lev 1 resolve: `reviews/PHASE_B_lev_01_write_sites_2026-07-24.md`  
- Genesis stack: `reviews/architecture/ARCHITECTURE_genesis_stack_2026-07-21.md`  

On substantive update: rename to today’s date and fix links.

---

## Table of contents

1. [What you will learn](#1-what-you-will-learn)  
2. [One-system picture](#2-one-system-picture)  
3. [Book roles at a glance](#3-book-roles-at-a-glance)  
4. [Genesis — bootstrap & seed data](#4-genesis--bootstrap--seed-data)  
5. [Exodus — install the machine](#5-exodus--install-the-machine)  
6. [Leviticus — run the apps](#6-leviticus--run-the-apps)  
7. [Numbers — ops & stress tests](#7-numbers--ops--stress-tests)  
8. [Deuteronomy — recompile for the land](#8-deuteronomy--recompile-for-the-land)  
9. [Interlock map — concrete chains](#9-interlock-map--concrete-chains)  
10. [Dependency graph (dev view)](#10-dependency-graph-dev-view)  
11. [What each book exports and imports](#11-what-each-book-exports-and-imports)  
12. [How to read sequentially vs resolve backward](#12-how-to-read-sequentially-vs-resolve-backward)  
13. [Practice exercises](#13-practice-exercises)  
14. [Repo artifacts](#14-repo-artifacts)  
15. [Limits of this model](#15-limits-of-this-model)

---

## 1. What you will learn

By the end you should be able to:

1. State each of the **five books’ architectural role** (hypothesis model).  
2. Name **specific Hebrew free names** each book **writes** and later books **read**.  
3. Trace **at least three multi-book chains** (e.g. Tent, people graph, covenant land).  
4. Explain interlock in **normal software terms** (boot → install → app → ops → recompile).  
5. Know when something is a **seed** vs an **install** vs a **local declare**.

**Hebrew always appears as:**  
`עברית` / *transliteration* / “English gloss”

---

## 2. One-system picture

Treat the Written Torah as **one long run**, not five unrelated apps:

```text
┌─────────────────────────────────────────────────────────────────┐
│ GENESIS                                                         │
│ Boot world · seed people · covenant patterns · Egypt handoff    │
└────────────────────────────┬────────────────────────────────────┘
                             │ people-in-Egypt, land promise, kinds…
┌────────────────────────────▼────────────────────────────────────┐
│ EXODUS                                                          │
│ Exit · Sinai · covenant · INSTALL sanctuary machine             │
└────────────────────────────┬────────────────────────────────────┘
                             │ Tent, priests, altar, “as commanded”
┌────────────────────────────▼────────────────────────────────────┐
│ LEVITICUS                                                       │
│ OPERATE machine: offerings, purity, holiness, calendar          │
└────────────────────────────┬────────────────────────────────────┘
                             │ types, purity grades, festival skeleton
┌────────────────────────────▼────────────────────────────────────┐
│ NUMBERS                                                         │
│ OPS: census, camp, march, crisis, war, land edge                │
└────────────────────────────┬────────────────────────────────────┘
                             │ journey memory, east tribes, refuge seed
┌────────────────────────────▼────────────────────────────────────┐
│ DEUTERONOMY                                                     │
│ RECOMPILE: remember · restate law · land constitution · handoff │
└─────────────────────────────────────────────────────────────────┘
```

**Interdependence rule:** later books usually **do not reinstall** the world or the Tent. They **resolve names and state** written earlier (content pointers), and sometimes **declare local** types or patches.

---

## 3. Book roles at a glance

| Book | Dev metaphor | Writes (exports) | Reads (imports) |
|------|--------------|------------------|-----------------|
| **Genesis** | BIOS / seed DB / identity graph | World, day cycle, kinds, people, land promise, Egypt end-state, cult *seeds* | Almost nothing prior |
| **Exodus** | Installer + first OS services | Tent, priests, altar, covenant, Decalogue, “as YHWH commanded” | People-in-Egypt, land promise, God of fathers |
| **Leviticus** | Business apps on that install | Offering types, purity tables, holiness code, festival calendar | Tent, priests, altar, presence |
| **Numbers** | Ops / staging / load tests | Census, camp layout, travel log, some statutes, land prep | Tent still center, purity/priests background, people graph |
| **Deuteronomy** | Recompile / migration guide | Restated law, land focus, Moses succession | Journey memory, Sinai memory, law families from Exod–Num |

**Confidence:** traditional block outlines = well known; “boot/install/app/ops/recompile” = **project hypothesis**, useful for engineering, not claimed as dogma.

---

## 4. Genesis — bootstrap & seed data

### 4.1 Role

**Cold-start the universe and the people story** before any national sanctuary system exists.

### 4.2 Structure (packages)

| Package | Rough span | Metaphor |
|---------|------------|----------|
| Creation week | 1:1–2:3 | Kernel boot |
| Garden | 2:4–3:24 | First runtime + breach |
| Early humanity | 4–5 | Multiplayer + lineage table |
| Flood / Noah | 6–9 | Disaster recovery + policy API |
| Nations / Babel | 10–11 | Multi-tenant + language split |
| Patriarchs | 12–36 | Covenant services |
| Joseph → Egypt | 37–50 | Export people to foreign host |

### 4.3 Concrete exports (examples)

| Export | Hebrew | Translit | English | Later consumers |
|--------|--------|----------|---------|-----------------|
| Day cycle | וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר | *va-yehi-erev va-yehi-boker* | evening then morning = day | Law assumes “days”; calendar ambient |
| Kinds | לְמִינֵהוּ | *le-minehu* | according to its kind | Animal vocabulary for offerings/food |
| People graph | twelve sons → tribes | — | tribal raw material | Exod rosters; Num census/camp |
| Land promise | לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ | *le-zar‘akha etten et-ha-arets* | to your seed I give the land | Exod/Num/Deut “land YHWH swore” |
| Egypt handoff | end of Gen 50 | — | Israel **in Egypt** | Exod 1 continues without reboot |
| Altar seed | Gen 8:20 מזבח / *mizbeach* | altar | Noah builds altar, offers עֹלֹת / *olot* | Word seed; **not** Tent altar install |
| Aroma seed | Gen 8:21 רֵיחַ הַנִּיחֹחַ | *re’ach ha-nichoach* | soothing aroma | Exod 29 / Lev 1 formula family |
| Covenant mark | Gen 17 circumcision | — | brit sign | National identity later |

### 4.4 What Genesis does *not* install

- Tabernacle / Tent of Meeting system  
- Aaronic priesthood office for the nation  
- Levitical purity grades as a full app suite  

Those wait for Exodus (+ Lev densification).

---

## 5. Exodus — install the machine

### 5.1 Role

**Deliver the people, cut covenant, and install the sanctuary + priest system** that later books operate.

### 5.2 Structure (major blocks)

| Block | Rough ch. | Metaphor |
|-------|-----------|----------|
| Bondage → exit | 1–15 | Migration out of host |
| Wilderness tests | 15–18 | Early ops |
| Sinai / Decalogue / mishpatim | 19–24 | Core law + covenant |
| **Tabernacle command** | 25–31 | Design docs |
| Crisis (calf) | 32–34 | Failed input / recovery |
| **Build + fill** | 35–40 | Compile + deploy + go-live |

### 5.3 Concrete installs (writes)

| Symbol | Hebrew | Translit | English | Primary write | Later use |
|--------|--------|----------|---------|---------------|-----------|
| Sanctuary goal | מִקְדָּשׁ | *mikdash* | sanctuary | **Exod 25:8** | Whole cult |
| Pattern | תַּבְנִית | *tavnit* | blueprint | **Exod 25:9** | Build must match |
| Tent of Meeting | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting | **Exod 27:21** (first name) | Lev/Num speech & rites |
| Entrance | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of Tent | **Exod 29:4, 29:42** | Lev 1:3, 1:5 bring/blood site |
| Altar (install) | מִזְבֵּחַ | *mizbeach* | altar | **Exod 27:1** design; **40:6** place | Lev blood/fire |
| Priests | בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron | **Exod 28:1** | Lev operators |
| Presence online | כָּבוֹד מָלֵא | *kavod male* | glory filled | **Exod 40:34–35** | Lev 1:1 from-Tent; Num cloud |
| Command pointer | כַּאֲשֶׁר צִוָּה | *ka’asher tzivvah* | as He commanded | dense in Exod build | Lev/Num execution |

### 5.4 Concrete imports from Genesis

| Import | How Exodus uses it |
|--------|-------------------|
| Israel in Egypt | Exod 1 opens with growth/oppression — no reboot of Joseph story |
| God of Abraham/Isaac/Jacob | Bush call, covenant language |
| Land promise | “bring you to the land…” |
| Twelve tribes material | Genealogy / camp later |

### 5.5 Interlock sample (Exod → Lev)

```text
WRITE Exod 29:4   petach ohel mo'ed  (priest wash location)
WRITE Exod 29:42  meet/speak at entrance
WRITE Exod 40:34  Tent covered / glory filled
USE   Lev 1:1     speech FROM ohel mo'ed
USE   Lev 1:3     bring TO petach ohel mo'ed
USE   Lev 1:5     blood on altar AT that entrance
```

Full method: `TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md` · Phase B: `PHASE_B_lev_01_write_sites_2026-07-24.md`.

---

## 6. Leviticus — run the apps

### 6.1 Role

**Operate the sanctuary machine**: what may be offered, how purity works, holy life, calendar around that Tent.

### 6.2 Structure (major blocks)

| Block | Rough ch. | Metaphor |
|-------|-----------|----------|
| Offerings | 1–7 | Input types + procedures |
| Investiture / crisis | 8–10 | Deploy priests; invalid fire |
| Purity | 11–15 | State machines (food, birth, skin, fluids) |
| Yom Kippur / blood center | 16–17 | Core transaction / blood rules |
| Holiness code | 18–20 | Ethics + land |
| Priests / sancta | 21–22 | Operator constraints |
| Festivals | 23–24 | Calendar app |
| Land / vows | 25–27 | Economics + seals |

### 6.3 Concrete imports (from Exodus)

| Free name | USE example | WRITE (Exod) |
|-----------|-------------|--------------|
| אֹהֶל מוֹעֵד / *ohel mo’ed* | Lev 1:1 from Tent | 27:21 · live 40:34 |
| פֶּתַח … / *petach…* | Lev 1:3 bring there | 29:4, 29:42 |
| בְּנֵי אַהֲרֹן / *benei Aharon* | Lev 1:5 blood handlers | 28:1 |
| מִזְבֵּחַ / *mizbeach* | Lev 1:5+ blood/fire | 27:1 · 40:6 |

### 6.4 Concrete local declares (Lev-born)

| Symbol | Hebrew | Where | Notes |
|--------|--------|-------|-------|
| Offering noun | קָרְבָּן / *korban* | **Lev 1:2** first Torah hit | App-local type word |
| North of altar | צָפֹנָה / *tzafonah* | Lev 1:11 | Local geometry |
| Place of ashes | מְקוֹם הַדֶּשֶׁן / *mekom ha-deshen* | Lev 1:16 | Local detail |
| Purity grades | טָמֵא / טָהוֹר / *tame* / *tahor* | Lev 11–15 dense | Registry home ≈ Lev |
| “This is the torah of…” | זֹאת תּוֹרַת / *zot torat* | Lev hubs | Procedure indexes |

### 6.5 Exports to later books

| Export | Later use |
|--------|-----------|
| Offering type system | Num festival schedules; purity background |
| Festival skeleton (Lev 23) | Num 28–29 quantities; Deut festival restatements |
| Holiness / land ethics | Deut social law echoes |
| YK / blood center | Background for sanctuary seriousness |

### 6.6 Interlock sample (Exod install + Gen seed + Lev local)

```text
Gen 8:20     SEED   mizbeach + olot
Exod 27/40   INSTALL sanctuary altar
Exod 29      INSTALL lean / slaughter / smoke patterns
Lev 1:2      LOCAL  declare korban menu
Lev 1:3–9    USE    petach + kohanim + mizbeach + olah path
```

---

## 7. Numbers — ops & stress tests

### 7.1 Role

**Run the system under motion and stress**: count people, arrange camp, march with the Tent, handle revolt, war, and land-edge logistics.

### 7.2 Structure (sketch)

| Block | Rough ch. | Metaphor |
|-------|-----------|----------|
| Census / camp | 1–4 | Inventory + topology |
| Camp purity / dedication | 5–7 | Health checks + load |
| Levites / Pesach II / depart | 8–10 | Roles + cloud travel control |
| Crises | 11–14, 16–17, 20–21, 25 | Failure modes |
| Law islands | 15, 18–19, 27–30, 35–36 | Patches + inheritance |
| Bilʿam | 22–24 | External oracle stress |
| Land prep | 26, 32–36 | Second census, east tribes, borders, refuge |

### 7.3 Concrete imports

| From | What Numbers still needs |
|------|---------------------------|
| **Exodus** | Tent still speech center (Num 1:1 בְּאֹהֶל מוֹעֵד / *be-ohel mo’ed*); cloud over mishkan; priests/Levites |
| **Leviticus** | Purity grades, offering types as background |
| **Genesis** | Tribal graph for census and camp standards |

### 7.4 Concrete writes (Numbers-local + handoffs)

| Export | Hebrew / idea | Later / parallel use |
|--------|---------------|----------------------|
| Census data | counts by tribe | War capacity; inheritance base |
| Camp layout | דֶּגֶל / *degel* / standard | March order |
| Cloud journey | when cloud lifts, move | Travel FSM (install presence → ops control) |
| Cities of refuge seed | Num 35 | **Deut 4 / 19** restate |
| East tribes deal | Num 32 | Land division conditions |
| Journeys log | Num 33 | Memory of path (Deut historical prologue uses journey memory) |

### 7.5 Interlock sample (presence → travel)

```text
WRITE Exod 40:34–35   cloud/glory on mishkan  (presence online)
USE   Num 9:15–23     cloud on mishkan governs stay/go
USE   Num 10:11+      lift cloud → march
```

**Same object, new job:** sanctuary presence becomes **ops traffic light**.

### 7.6 Interlock sample (people graph)

```text
WRITE Gen 29–35 / 46   sons → tribes
USE   Num 1–2          census + camp by tribe
USE   Num 26           second census after death of generation
USE   Num 34–36        land / heiresses depend on tribal structure
```

---

## 8. Deuteronomy — recompile for the land

### 8.1 Role

**Moses’ farewell recompile:** remember the journey, restate law for life **in the land**, renew covenant, hand off to Joshua, close the Torah run.

### 8.2 Structure (10-phase map used in this repo)

| Phase | Ch. | Content |
|-------|-----|---------|
| A | 1–3 | Historical prologue (reads Numbers/Exodus memory) |
| B | 4–6 | Law frame, Decalogue restatement, Shema |
| C | 7–11 | Loyalty / land / not-for-your-righteousness |
| D–G | 12–26 | Legal core (central place, king, war, social…) |
| H | 27–28 | Ceremony + blessings/curses |
| I | 29–30 | Moab covenant |
| J | 31–34 | Torah written, song, blessing, Moses’ death |

See `reviews/DEUTERONOMY_BUILD_2026-07-24.md`.

### 8.3 Concrete imports (heavy pointer book)

| Import | Example |
|--------|---------|
| Horeb / Sinai memory | Deut 5 Decalogue restatement |
| Journey failures | Spies refusal (cf. Num 13–14) in Deut 1 |
| East conquest | Sihon/Og (cf. Num 21) in Deut 2–3 |
| Levitical / social law families | Refuge, festivals, slaves, etc. restated |
| Exodus centralization trajectory | “the place YHWH will choose” develops sanctuary centralization for land |

### 8.4 Concrete Deuteronomy-local emphasis

| Theme | Hebrew | Translit | English | Role |
|-------|--------|----------|---------|------|
| Shema | שְׁמַע יִשְׂרָאֵל | *shema Yisrael* | Hear O Israel | Loyalty kernel (Deut 6) |
| Chosen place | הַמָּקוֹם אֲשֶׁר־יִבְחַר | *ha-makom asher-yivchar* | the place He will choose | Land-era sanctuary key (Deut 12) |
| King law | שׂוֹם תָּשִׂים עָלֶיךָ מֶלֶךְ | *som tasim… melech* | set a king | Constitutional patch (Deut 17) |
| Return / choose life | Deut 30 | — | teshuvah + life/death | Covenant close |

### 8.5 Interlock sample (refuge cities)

```text
WRITE Num 35     cities of refuge (detailed statute)
USE   Deut 4:41–43  Moses sets three east cities
USE   Deut 19       west-bank rules restated / extended
```

### 8.6 Interlock sample (historical prologue = log replay)

```text
WRITE Num 13–14   spies + rejection
USE   Deut 1:19–46  Moses retells; draws legal-moral conclusion
WRITE Num 21      Sihon/Og
USE   Deut 2–3    retell + allotment memory
```

Deuteronomy often **replays the ops log** then **re-emits policy**.

---

## 9. Interlock map — concrete chains

### Chain 1 — Sanctuary spine (clearest)

```text
Gen (optional seeds: altar, olah, aroma)
    ↓
Exod 25–40  INSTALL  mikdash, ohel mo'ed, petach, mizbeach, kohanim, kavod
    ↓
Lev 1–16    OPERATE  offerings, purity, YK at that machine
    ↓
Num 1–10    OPS      speech at Tent; cloud governs march
    ↓
Deut 12+    RECOMPILE  "place YHWH will choose" for land life
```

**Interdependence:** Lev/Num break if Tent/priests never installed. Deut centralization assumes a sanctuary *idea* already real in the story.

### Chain 2 — People / census / land

```text
Gen 29–50   WRITE  sons → tribal identities; Egypt population
Exod 1      USE    people multiply in Egypt
Exod 6      USE    tribal roster fragments
Num 1–2     USE    full census + camp topology
Num 26      USE    second census (new generation)
Num 32–36   USE    land east/west, inheritance, heiresses
Deut 1–3    USE    people/land memory for conquest framing
```

### Chain 3 — Covenant / Decalogue / loyalty

```text
Gen 15–17   SEED    land/seed covenant; circumcision
Exod 19–24  INSTALL Sinai covenant; Decalogue; blood covenant
Exod 32–34  CRISIS  calf; second tablets
Deut 5      RESTATE Decalogue
Deut 6–11   APP     Shema, love, teach, loyalty
Deut 27–30  CLOSE   curses/blessings; Moab covenant; choose life
```

### Chain 4 — Calendar / offerings

```text
Exod 12, 23     SEED/INSTALL  Pesach, festival outlines
Lev 23          REGISTRY      full festival calendar
Num 28–29       SCHEDULE      daily/festival offering quantities
Deut 16         RECOMPILE     festivals for land / central place
```

### Chain 5 — Failure modes (why Numbers depends on both install and people)

```text
Exod install   gives sacred center + rules
Lev purity     defines clean/unclean camp expectations
Num 5          camp purity enforcement
Num 11–14, 16  complaint, spies, Korach = stress tests of authority/trust
Deut 1         reads those failures as teaching data
```

---

## 10. Dependency graph (dev view)

```text
                    ┌──────────────┐
                    │   Genesis    │
                    │ boot + seed  │
                    └──────┬───────┘
           people, land, Egypt, kinds, cult seeds
                           │
                    ┌──────▼───────┐
                    │   Exodus     │
                    │   INSTALL    │
                    └──────┬───────┘
           Tent, priests, altar, covenant, law tables
                    ┌──────┴───────┐
                    │              │
             ┌──────▼──────┐ ┌─────▼──────┐
             │  Leviticus  │ │  (also Num │
             │  APPS       │ │   uses     │
             └──────┬──────┘ │   install) │
           types, purity,    └─────┬──────┘
           calendar                │
                    ┌──────────────┘
                    │
             ┌──────▼──────┐
             │  Numbers    │
             │  OPS        │
             └──────┬──────┘
           census, camp, crises, land edge
                    │
             ┌──────▼──────┐
             │ Deuteronomy │
             │ RECOMPILE   │
             └─────────────┘
           memory + restated constitution
```

**Not a strict DAG for every verse** — Deuteronomy also reaches back to Genesis promises and Exodus Horeb. Think **primary edges** plus long-range memory pointers.

---

## 11. What each book exports and imports

### Quick reference table

| Book | Top exports | Top imports |
|------|-------------|-------------|
| **Gen** | World state, people graph, land promise, Egypt end, cult seeds | — |
| **Exod** | Sanctuary machine, priests, Decalogue, covenant, command-compliance culture | Gen people/Egypt/land/God-of-fathers |
| **Lev** | Offering/purity/holiness/calendar registries | Exod sanctuary environment |
| **Num** | Census/camp/travel data, refuge/inheritance patches, crisis log | Exod Tent/cloud; Lev purity/types; Gen tribes |
| **Deut** | Land-facing restate, Shema/loyalty core, succession | Journey log (Num), Sinai (Exod), law families (Exod–Num), promises (Gen) |

### Layer cheat-sheet (for variable work)

| Layer | Mostly lives in | Example free names |
|-------|-----------------|-------------------|
| L0 Ambient | Genesis | day, kinds, people, land promise |
| L1 Install | Exodus | ohel mo’ed, petach, kohen, mizbeach, kavod |
| L2 App registries | Leviticus | korban types, tame/tahor, zot torat X |
| L3 Ops data | Numbers | census, degel, journeys, miklat |
| L4 Recompile | Deuteronomy | place-He-chooses, shema, king law |

---

## 12. How to read sequentially vs resolve backward

| Mode | What you see | What you prove |
|------|--------------|----------------|
| **Forward** | Install-shaped text (“make…”, “bring Aaron…”) | Candidate exports |
| **Backward from use** | Free names in Lev/Num/Deut | Which earlier write they resolve to |
| **Together** | Full interlock map | PASS / LOCAL / layered |

Trees (cantillation) help **group tokens inside a verse**.  
They do **not** alone prove cross-book variables — **reuse does**.

See also: declare/use tutorial § on sequential vs use-first.

---

## 13. Practice exercises

### Exercise 1 — One chain, three books

Trace **cloud / presence**:

1. Exod 40:34–35 — write  
2. Num 9:15–23 — use as travel control  
3. Optional: Deut memory of journey  

Write three rows: USE / WRITE / pointer type.

### Exercise 2 — Seed vs install

Compare:

- Gen 8:20 altar  
- Exod 27:1 + 40:6 altar  
- Lev 1:5 altar  

Label each seed / install / use.

### Exercise 3 — Local declare

Confirm `קרבן` / *korban* first major legal surface at Lev 1:2 and list what Lev 1 still **imports** from Exodus in the same chapter.

### Exercise 4 — Deut replay

Open Deut 1:19–46 and map which Numbers episode it replays (spies). Note one legal-moral “export” of the retelling.

---

## 14. Repo artifacts

| Artifact | Role |
|----------|------|
| `logic/units/gen_*.yaml` | Genesis units (tree_derived_v1) |
| `logic/units/exo_*.yaml` | Exodus units |
| `logic/units/lev_*.yaml` | Leviticus units |
| `logic/units/num_*.yaml` | Numbers units |
| `logic/units/deu_*.yaml` | Deuteronomy units |
| `reviews/*_BUILD_*.md` | Per-book build docs |
| `reviews/PHASE_B_lev_01_write_sites_2026-07-24.md` | Gold example resolve matrix |
| `logic/TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md` | How to extract variables |

Parse any verse:

```bash
python3 taamim_tree_parse.py Exod.40.34 --tree
python3 taamim_tree_parse.py Lev.1.5 --tree
python3 taamim_tree_parse.py Num.9.17 --tree
python3 taamim_tree_parse.py Deut.6.4 --tree
```

---

## 15. Limits of this model

| Claim | Status |
|-------|--------|
| Five-phase architecture helps navigation | **Useful hypothesis** |
| Content pointers exist (names, places, state) | **Tested** on sanctuary spine / Lev 1 |
| Full automatic symbol resolver for all free names | **Not built** |
| Every verse is “code” | **No** — genre mix (narrative, law, song, list) |
| Binding religious law | **Not claimed** here |
| English summaries as source | **Forbidden** for derivation |

---

## Appendix — One-page cheat sheet

```text
GENESIS     boot + seed DB + Egypt handoff
EXODUS      install sanctuary + covenant OS
LEVITICUS   apps: korban, purity, holiness, mo'adim
NUMBERS     ops: count, camp, march, fail, prepare land
DEUTERONOMY recompile for land + handoff Moses→Joshua

Interlock = later free names resolve earlier writes
            (+ some LOCAL declares in each book)

Best demo chain: Exod Tent install → Lev 1 operate → Num cloud march → Deut central place
```

---

## Changelog

- 2026-07-25: Initial five-book interlock tutorial for full-stack developers with concrete multi-book chains.
