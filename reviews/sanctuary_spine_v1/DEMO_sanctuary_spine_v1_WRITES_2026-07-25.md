# Sanctuary spine V1 — Step 2: Symbol table WRITES (Exodus install)

**Date:** 2026-07-25  
**Kind:** demo free-name write table — experimental, **not** binding religious law  
**Status:** **Step 2 done**  
**Folder:** `reviews/sanctuary_spine_v1/`  
**Charter:** `DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md` (same folder)  
**Next:** Step 3 — USE matrix (Lev 1 / Num 9–10 / Deut 12)

**Source:** Hebrew from `../../Data/Exod.xml` via `../../taamim_tree_parse.py` v1 (all listed verses `status: unique`).  
**English:** `[EN-AID]` gloss only.

On substantive update: rename to today’s date and fix links.

---

## 0. What this step is

For each **install free name** in the charter (§3.1), record:

| Field | Meaning |
|-------|---------|
| **WRITE** | V1 Exodus locus where the system meaning is set |
| **Surface** | Hebrew as it appears (+ translit + English) |
| **Tree** | Top split role (and note if multi-leaf) |
| **Op** | What the verse *does* to the symbol (declare / design / place / activate) |
| **Pointer type later uses will use** | Expected P-NAME / P-PLACE / P-STATE… |
| **Confidence** | tested (Hebrew present) / hypothesis (job label) |

**Not in this step:** Lev/Num/Deut uses (Step 3). Procedure IF tables (Step 4). Cloud FSM (Step 5).

---

## 1. Install sequence (ordered writes)

```text
1. Exod 25:8–9    GOAL + PATTERN     mikdash, tavnit, mishkan (as pattern object)
2. Exod 27:1      DESIGN ALTAR       mizbeach
3. Exod 27:21     NAME TENT          ohel mo'ed (first clear name in Torah)
4. Exod 28:1      APPOINT PRIESTS    benei Aharon, kohen office
5. Exod 29:4      PLACE KEY          petach ohel mo'ed (bring-to)
6. Exod 29:42     FUNCTION           petach + speech/meet + olah tamid frame
7. Exod 40:6      LAYOUT GO-LIVE     mizbeach ha-olah before petach mishkan/ohel
8. Exod 40:34–35  PRESENCE ONLINE    anan, kavod, ohel mo'ed, mishkan filled
```

---

## 2. Master WRITE table (charter §3.1)

| Handle | Hebrew | Translit | English | Primary WRITE | Op | Tree (top) | Later pointer | Conf. |
|--------|--------|----------|---------|---------------|-----|------------|---------------|-------|
| `SYM_mikdash` | מִקְדָּשׁ | *mikdash* | sanctuary | **Exod 25:8** | DECLARE goal | L: “make me a *mikdash*” / R: “I will dwell among them” | P-NAME / goal | tested |
| `SYM_tavnit` | תַּבְנִית | *tavnit* | pattern / blueprint | **Exod 25:9** | DECLARE data | L: pattern of mishkan + vessels shown / R: “so you shall make” | P-CMD (build to pattern) | tested |
| `SYM_mishkan` | מִשְׁכָּן | *mishkan* | dwelling | **Exod 25:9** (pattern); **40:34–35** (filled object) | DECLARE then FILL | 25:9 L includes *tavnit ha-mishkan*; 40:34 R glory fills *ha-mishkan* | P-NAME / P-STATE | tested |
| `SYM_mizbeach` | מִזְבֵּחַ | *mizbeach* | altar | **Exod 27:1** design; **40:6** place | DESIGN + PLACE | 27:1 L: “make the altar…”; 40:6 L: give olah-altar / R: before entrance | P-NAME | tested |
| `SYM_ohel_moed` | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting | **Exod 27:21** first name; **40:34** covered | NAME + ACTIVATE site | 27:21 L opens “in *ohel mo’ed*…”; 40:34 L cloud covers *ohel mo’ed* | P-NAME / P-STATE | tested |
| `SYM_petach_ohel` | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of the Tent | **Exod 29:4**; function **29:42**; layout **40:6** | PLACE KEY + FUNCTION | 29:4 L: bring to *petach ohel mo’ed*; 29:42 L ends at entrance before YHWH; 40:6 R before entrance | P-PLACE | tested |
| `SYM_benei_aharon` | בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron | **Exod 28:1** | APPOINT office + name list | L: bring Aaron & sons to priest for Me; R: named sons = *benei Aharon* | P-NAME | tested |
| `SYM_kohen` | כֹּהֵן / לְכַהֲנוֹ | *kohen* / *le-khahano* | priest / to priest | **Exod 28:1** | APPOINT role | L: *le-khahano li* “to priest for Me” | P-NAME | tested |
| `SYM_anan` | עָנָן | *anan* | cloud | **Exod 40:34–35** | ACTIVATE signal | 40:34 L: cloud covers Tent; 40:35 L: cloud dwells on it | P-STATE (later travel) | tested |
| `SYM_kavod` | כָּבוֹד | *kavod* | glory | **Exod 40:34–35** | ACTIVATE presence | R both verses: glory of YHWH filled the mishkan | P-STATE | tested |

**All charter §3.1 install names: WRITE found. None OPEN.**

`SYM_makom_yivchar` is **not** an Exodus write (Deut recompile) — deferred to Step 3 with policy from charter.

---

## 3. Verse cards (show work)

### 3.1 Exod 25:8 — `SYM_mikdash` (+ dwell goal)

| | |
|--|--|
| **Plain line** | ועשו לי מקדש ושכנתי בתוכם |
| **Translit** | *ve-asu li mikdash ve-shakhanti be-tokham* |
| **EN-AID** | They shall make Me a sanctuary, and I will dwell among them |
| **Top tree** | **L:** make Me a *mikdash* · **R:** I will dwell among them |
| **Writes** | `SYM_mikdash` (goal object); dwell intent (presence *purpose*, not yet online) |
| **Op** | `DECLARE_GOAL` |
| **Confidence** | structure tested; “export for whole cult” hypothesis |

---

### 3.2 Exod 25:9 — `SYM_tavnit`, `SYM_mishkan` (as blueprint)

| | |
|--|--|
| **Plain line** | ככל אשר אני מראה אותך את תבנית המשכן ואת תבנית כל כליו וכן תעשו |
| **Translit** | *ke-khol asher ani mar’eh otkha et tavnit ha-mishkan ve-et tavnit kol kelav ve-khen ta’asu* |
| **EN-AID** | According to all that I show you — the pattern of the mishkan and of all its vessels — so you shall make |
| **Top tree** | **L:** show you pattern of mishkan + vessels · **R:** so you shall make |
| **Writes** | `SYM_tavnit` (data); `SYM_mishkan` as **design target** (not yet erected) |
| **Op** | `DECLARE_PATTERN` / build constraint |
| **Note** | *et* marks definite objects *tavnit ha-mishkan* / *tavnit* vessels — glue pointing at design payloads, not free names themselves |

---

### 3.3 Exod 27:1 — `SYM_mizbeach` (design)

| | |
|--|--|
| **Plain line** | ועשית את המזבח עצי שטים … רבוע יהיה המזבח … |
| **Translit** | *ve-asita et ha-mizbeach atsei shittim …* |
| **EN-AID** | You shall make the altar of acacia wood… the altar shall be square… |
| **Top tree** | **L:** make the altar of acacia · **R:** dimensions (altar square, height) |
| **Writes** | `SYM_mizbeach` as **constructed type** (tabernacle bronze altar family) |
| **Op** | `DESIGN` |
| **Seed (not V1 write)** | Gen 8:20 etc. earlier *mizbeach* — different layer (`PASS_layered` at use time) |

---

### 3.4 Exod 27:21 — `SYM_ohel_moed` (first name)

| | |
|--|--|
| **Plain line** | באהל מועד מחוץ לפרכת … יערך אתו אהרן ובניו … לפני יהוה … |
| **Translit** | *be-ohel mo’ed mi-hutz la-parokhet … ya’arokh oto Aharon u-vanav … lifnei YHWH* |
| **EN-AID** | In the Tent of Meeting, outside the veil… Aaron and his sons shall arrange it… before YHWH… |
| **Top tree** | **L:** in *ohel mo’ed* … Aaron and sons … before YHWH · **R:** eternal statute for generations |
| **Writes** | `SYM_ohel_moed` **named**; priests already linked as operators of lamp service |
| **Op** | `NAME` + locate service |
| **Confidence** | first Torah co-occurrence of אהל+מועד as this phrase — **tested** |

---

### 3.5 Exod 28:1 — `SYM_benei_aharon`, `SYM_kohen`

| | |
|--|--|
| **Plain line** | ואתה הקרב אליך את אהרן … ואת בניו … לכהנו לי … בני אהרן |
| **Translit** | *ve-atah haqrev eleikha et Aharon … ve-et banav … le-khahano li … benei Aharon* |
| **EN-AID** | Bring near Aaron your brother and his sons with him… to priest for Me… Nadav, Avihu, Eleazar, Itamar, sons of Aaron |
| **Top tree** | **L:** bring Aaron & sons to priest for Me · **R:** name list = *benei Aharon* |
| **Writes** | Office **kohen**; roster **benei Aharon** |
| **Op** | `APPOINT` |
| **Note** | Multi-leaf name on RIGHT; *et* marks Aaron/sons as objects of “bring near” |

---

### 3.6 Exod 29:4 — `SYM_petach_ohel`

| | |
|--|--|
| **Plain line** | ואת אהרן ואת בניו תקריב אל פתח אהל מועד ורחצת אתם במים |
| **Translit** | *ve-et Aharon ve-et banav taqriv el petach ohel mo’ed ve-rahatsta otam ba-mayim* |
| **EN-AID** | Bring Aaron and his sons to the entrance of the Tent of Meeting and wash them with water |
| **Top tree** | **L:** bring to *petach ohel mo’ed* · **R:** wash them with water |
| **Writes** | `SYM_petach_ohel` as **bring-to place key** |
| **Op** | `DECLARE_PLACE` |
| **Preposition cue** | **אל** / *el* / “to” + place name (glue → place variable) |

---

### 3.7 Exod 29:42 — petach function + speech

| | |
|--|--|
| **Plain line** | עלת תמיד … פתח אהל מועד לפני יהוה אשר אועד לכם שמה לדבר אליך שם |
| **Translit** | *olat tamid … petach ohel mo’ed lifnei YHWH asher ivva’ed lakhem shammah le-dabber eleikha sham* |
| **EN-AID** | Continual burnt offering… at the entrance of the Tent of Meeting before YHWH, where I will meet you to speak with you there |
| **Top tree** | **L:** tamid + *petach ohel mo’ed* before YHWH · **R:** I will meet/speak there |
| **Writes** | Strengthens `SYM_petach_ohel` with **speech/meet function**; frames olah-at-entrance (for Lev import) |
| **Op** | `BIND_FUNCTION` |
| **Why Lev 1:1 works later** | Speech *from* Tent assumes this meet/speak binding + 40 go-live |

---

### 3.8 Exod 40:6 — altar placement

| | |
|--|--|
| **Plain line** | ונתתה את מזבח העלה לפני פתח משכן אהל מועד |
| **Translit** | *ve-natata et mizbach ha-olah lifnei petach mishkan ohel mo’ed* |
| **EN-AID** | You shall place the altar of burnt offering before the entrance of the mishkan of the Tent of Meeting |
| **Top tree** | **L:** place the olah-altar · **R:** before entrance of mishkan/Tent |
| **Writes** | `SYM_mizbeach` **placed**; joins `SYM_petach_ohel` + `SYM_mishkan` + `SYM_ohel_moed` in one layout sentence |
| **Op** | `PLACE` / layout link |

---

### 3.9 Exod 40:34–35 — `SYM_anan`, `SYM_kavod` (go-live)

**40:34**

| | |
|--|--|
| **Plain** | ויכס הענן את אהל מועד וכבוד יהוה מלא את המשכן |
| **Translit** | *va-yekhas he-anan et ohel mo’ed u-khevod YHWH male et ha-mishkan* |
| **EN-AID** | The cloud covered the Tent of Meeting, and the glory of YHWH filled the mishkan |
| **Top tree** | **L:** cloud covers *ohel mo’ed* · **R:** glory fills *ha-mishkan* |
| **Writes** | `SYM_anan` active on Tent; `SYM_kavod` fills mishkan; confirms `SYM_ohel_moed` / `SYM_mishkan` as live objects |

**40:35**

| | |
|--|--|
| **Plain** | ולא יכל משה לבוא אל אהל מועד כי שכן עליו הענן וכבוד יהוה מלא את המשכן |
| **Translit** | *ve-lo yakhol Mosheh la-vo el ohel mo’ed ki shakhan alav he-anan u-khevod YHWH male et ha-mishkan* |
| **EN-AID** | Moses could not enter the Tent of Meeting because the cloud dwelled on it and the glory of YHWH filled the mishkan |
| **Top tree** | **L:** Moses cannot enter; cloud dwells · **R:** glory filled mishkan |
| **Op** | `ACTIVATE` / presence online (even Moses blocked) |
| **Handoff** | After this, Lev may operate free names without rebuild — `EXPORT_lev_handoff` spirit in units |

---

## 4. Symbol → write locus index (quick)

| Handle | Primary verse(s) |
|--------|------------------|
| `SYM_mikdash` | 25:8 |
| `SYM_tavnit` | 25:9 |
| `SYM_mishkan` | 25:9 (pattern) · 40:34–35 (filled) |
| `SYM_mizbeach` | 27:1 · 40:6 |
| `SYM_ohel_moed` | 27:21 · 40:34–35 |
| `SYM_petach_ohel` | 29:4 · 29:42 · 40:6 |
| `SYM_benei_aharon` | 28:1 |
| `SYM_kohen` | 28:1 (*le-khahano*) |
| `SYM_anan` | 40:34–35 |
| `SYM_kavod` | 40:34–35 |

---

## 5. Glue observations at WRITE sites (for later detectors)

| Pattern | Example | Role |
|---------|---------|------|
| **את** + definite object | 25:9 *et tavnit…*; 27:1 *et ha-mizbeach*; 40:34 *et ohel mo’ed* | Points at design/place payload — **not** the variable itself |
| **אל** + place | 29:4 *el petach ohel mo’ed* | Destination of install act |
| **לפני** + place | 40:6 *lifnei petach…* | Spatial relation of altar to entrance |

Consistent with charter method: glue **orients**; Hebrew content span **is** the symbol.

---

## 6. What Step 2 does *not* claim

- That every Exod 25–40 free name is catalogued  
- That Gen seeds are false (they are simply **out of V1 write set** except as notes)  
- That Deut *makom yivchar* is written here  
- Full leaf paths for every token (top tree + multi-leaf notes; deeper paths optional in Step 3 uses)  

---

## 7. Step status

| Step | Status |
|------|--------|
| 1 Charter | done |
| **2 Writes** | **done** (this file) |
| 3 Uses | pending |
| 4 Cattle olah | pending |
| 5 Cloud FSM | pending |
| 6 Hub | pending |

---

## Changelog

- 2026-07-25: Step 2 complete — WRITE table for all charter §3.1 install symbols from V1 Exodus verse list.
