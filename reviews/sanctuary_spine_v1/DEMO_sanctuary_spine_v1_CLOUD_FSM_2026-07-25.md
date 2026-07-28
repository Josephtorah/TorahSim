# Sanctuary spine V1 — Step 5: Cloud stay / go FSM (Num 9:15–23 · 10:11–13)

**Date:** 2026-07-25  
**Kind:** demo state machine from Hebrew + trees — experimental, **not** binding religious law  
**Status:** **Step 5 done**  
**Folder:** `reviews/sanctuary_spine_v1/`  
**Charter:** `DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md`  
**Writes / Uses:** Step 2–3 (`SYM_anan`, `SYM_mishkan`, `SYM_ohel_moed` aliases)  
**Prior procedure:** Step 4 cattle olah (operate *at* the machine)  
**Next:** Step 6 — hub package  

**Source:** `Data/Num.xml` · `taamim_tree_parse.py` v1.  
**English:** `[EN-AID]` only.

On substantive update: rename to today’s date and fix links.

---

## 0. What this step is

Show Numbers treating the **same sanctuary cloud** Exodus turned on as a **travel controller**:

```text
Exod 40:34–35   WRITE  cloud covers Tent; glory fills mishkan   (presence ONLINE)
Num 9:15–23     USE    cloud on mishkan → stay / lift → journey rules
Num 10:11–13    USE    concrete fire: cloud lifts → they march from Sinai
```

**Genre:** narrative FSM (ops), not korban IF tables.  
**Not:** full trumpet chapter, full itinerary, binding law.

---

## 1. Free names (resolved)

| Handle | Hebrew in Num block | Translit | English | WRITE |
|--------|---------------------|----------|---------|-------|
| `SYM_anan` | הֶעָנָן | *he-anan* | the cloud | Exod 40:34–35 |
| `SYM_mishkan` | הַמִּשְׁכָּן / מִשְׁכַּן הָעֵדֻת | *ha-mishkan* / *mishkan ha-edut* | dwelling / dwelling of the testimony | Exod 25:9 · 40:34–35 |
| `SYM_ohel` (alias) | הָאֹהֶל | *ha-ohel* | the tent | same machine as *ohel mo’ed* (PASS_alias, Step 3) |

**Job shift (important):**

| Stage | Cloud’s job |
|-------|-------------|
| Exod 40 | **Go-live signal** — covers Tent at install complete |
| Num 9–10 | **Ops input** — dwell = camp; lift = march |

---

## 2. States (V1)

| State id | Plain English | Hebrew cues |
|----------|---------------|-------------|
| `S_COVERED_DAY` | Cloud covers mishkan by day | כִּסָּה הֶעָנָן / *kissah he-anan* / the cloud covered |
| `S_FIRE_NIGHT` | Night appearance as fire on mishkan | כְּמַרְאֵה־אֵשׁ / *ke-mar’eh-esh* / like appearance of fire |
| `S_CAMPED` | Israel stays camped while cloud dwells on mishkan | יַחֲנוּ / *yahnu* / they camp; cloud ישְׁכֹּן / *yishkon* / dwells |
| `S_LIFTING` | Cloud is taken up from tent/mishkan | הֵעָלוֹת / נַעֲלָה הֶעָנָן / *he‘alot* / *na‘alah he-anan* / cloud is lifted |
| `S_MARCHING` | Israel journeys | יִסְעוּ / נָסְעוּ / *yis‘u* / *nas‘u* / they journey |
| `S_SETTLE` | Cloud settles at a place → they camp there | יִשְׁכֹּן … שָׁם יַחֲנוּ / *yishkon … sham yahnu* |

**Authority wrapper (every transition):**  
עַל־פִּי יְהוָה / *al-pi YHWH* / “by the mouth of YHWH” — journey **and** camp (9:18, 9:20, 9:23; 10:13).

---

## 3. Transitions (from the verses)

```text
                    ┌─────────────────────┐
                    │  S_COVERED_DAY      │◄── init Num 9:15 day of erecting
                    │  (+ S_FIRE_NIGHT    │
                    │   evening pattern)  │
                    └──────────┬──────────┘
                               │ cloud dwells on mishkan
                               ▼
                    ┌─────────────────────┐
         ┌─────────►│  S_CAMPED           │◄────────┐
         │          │  "they camp"        │         │
         │          └──────────┬──────────┘         │
         │                     │ cloud lifted       │
         │                     ▼                    │
         │          ┌─────────────────────┐         │
         │          │  S_LIFTING          │         │
         │          └──────────┬──────────┘         │
         │                     │ after lift         │
         │                     ▼                    │
         │          ┌─────────────────────┐         │
         │          │  S_MARCHING         │         │
         │          └──────────┬──────────┘         │
         │                     │ cloud settles      │
         │                     ▼                    │
         │          ┌─────────────────────┐         │
         └──────────│  S_SETTLE → CAMPED  │─────────┘
                    └─────────────────────┘
```

| From | Event (Hebrew cue) | To | Verse |
|------|--------------------|-----|-------|
| — | Day mishkan erected; cloud covers | `S_COVERED_DAY` | 9:15 L |
| covered | Evening: fire-appearance until morning | `S_FIRE_NIGHT` (cycle with day) | 9:15 R · 9:16 |
| any | Cloud dwells on mishkan | `S_CAMPED` | 9:17 R · 9:18 R |
| camped | Cloud **lifted** from tent | `S_LIFTING` → `S_MARCHING` | 9:17 L · 9:21–22 |
| marching | Cloud **dwells** at a place | `S_SETTLE` → `S_CAMPED` | 9:17 R |
| camped | Cloud prolonged many days | stay camped; **do not journey** | 9:19 · 9:22 L |
| camped | Cloud few days / overnight / day-night | still: lift → journey | 9:20–21 |
| lifting | `ובהעלתו יסעו` when it is taken up they journey | `S_MARCHING` | 9:22 R |
| * | always under `al-pi YHWH` | camp **or** journey | 9:18, 23 |

**Duration is not a separate state machine** — same stay/go rules whether cloud lasts many days, a month, overnight, or from evening to morning (9:19–22). Duration only answers **how long** in `S_CAMPED` before lift.

---

## 4. Verse cards (tree-aware)

### 4.1 Num 9:15 — init cover + night fire

| | |
|--|--|
| **Linear** | וביום הקים את המשכן כסה הענן את המשכן לאהל העדת ובערב יהיה על המשכן כמראה אש עד בקר |
| **Translit** | *u-ve-yom haqim et ha-mishkan kissah he-anan et ha-mishkan le-ohel ha-edut u-va-erev yihyeh al ha-mishkan ke-mar’eh esh ad boqer* |
| **EN-AID** | On the day the mishkan was erected, the cloud covered the mishkan as the tent of the testimony; evening: on the mishkan like appearance of fire until morning |
| **Top tree** | **L:** day erect + cloud covers mishkan · **R:** evening fire-appearance until morning |
| **Writes into FSM** | enter covered; establish day/night visual cycle on **same mishkan** |
| **Free names** | `SYM_mishkan`, `SYM_anan` |

---

### 4.2 Num 9:16 — standing pattern

| | |
|--|--|
| **EN-AID** | So it was always: the cloud covered it, and appearance of fire by night |
| **Top tree** | **L:** always cloud covers · **R:** fire appearance night |
| **Logic** | `always: day_cover XOR night_fire_appearance` (paired modes on the dwelling) |

---

### 4.3 Num 9:17 — core stay/go rule (key verse)

| | |
|--|--|
| **Linear** | ולפי העלת הענן מעל האהל ואחרי כן יסעו בני ישראל ובמקום אשר ישכן שם הענן שם יחנו בני ישראל |
| **Translit** | *u-lefi he‘alot he-anan me-al ha-ohel ve-ahare khen yis‘u benei Yisrael u-ve-maqom asher yishkon sham he-anan sham yahnu benei Yisrael* |
| **EN-AID** | According to the lifting of the cloud from on the tent, after that Israel journeys; at the place where the cloud dwells, there Israel camps |
| **Top tree** | **L:** when cloud **lifts** from tent → then they **journey** · **R:** where cloud **dwells** → there they **camp** |
| **Logic** | `on lift(from=tent) → MARCH; on dwell(at=place) → CAMP(place)` |
| **Tree insight** | Clean binary: **lift/march** vs **dwell/camp** — two transitions, one verse |
| **Alias** | האהל = tent of the system (not re-installing *ohel mo’ed* string) |

---

### 4.4 Num 9:18 — dual command channel

| | |
|--|--|
| **EN-AID** | By the mouth of YHWH they journey; by the mouth of YHWH they camp; all the days the cloud dwells on the mishkan they camp |
| **Top tree** | **L:** al-pi YHWH journey **and** camp · **R:** while cloud on mishkan → camp |
| **Logic** | Authority = YHWH; **sensor** = cloud on mishkan; both required in the narrative framing |

---

### 4.5 Num 9:19 — long stay

| | |
|--|--|
| **EN-AID** | When the cloud prolonged on the mishkan many days, Israel kept YHWH’s charge and **did not journey** |
| **Top tree** | **L:** cloud prolonged many days · **R:** keep charge and do not journey |
| **Logic** | `if dwell_duration == many_days: forbid(MARCH); keep(mishmeret)` |

---

### 4.6 Num 9:20–21 — short stays still same FSM

| Verse | EN-AID | Logic |
|-------|--------|-------|
| 9:20 | Cloud a number of days: camp by YHWH, journey by YHWH | duration short; same dual command |
| 9:21 | Evening to morning then lift → journey; or day and night then lift → journey | overnight or continuous; **lift is the march trigger** |

**Top tree 9:21:** **L:** evening→morning lift→go · **R:** or day-and-night lift→go — two duration variants, same transition.

---

### 4.7 Num 9:22 — any duration; lift ends stay

| | |
|--|--|
| **EN-AID** | Days or a month or days: while cloud prolonged dwelling, they camp and do not journey; **when it is taken up, they journey** |
| **Top tree** | **L:** long dwell → camp, not journey · **R:** when taken up → journey |
| **Logic** | Universal: `on he‘aloto → MARCH` regardless of prior duration |

---

### 4.8 Num 9:23 — seal

| | |
|--|--|
| **EN-AID** | By YHWH’s mouth they camp and journey; they kept YHWH’s charge by YHWH’s mouth through Moses |
| **Top tree** | **L:** camp and journey by YHWH · **R:** kept charge by YHWH via Moses |
| **Logic** | Both transitions under same authority; Moses as human channel |

---

### 4.9 Num 10:11–13 — instance fire (Sinai depart)

| Verse | EN-AID | FSM event |
|-------|--------|-----------|
| **10:11** | Year 2, month 2, day 20: the cloud was taken up from over the mishkan of the testimony | `S_LIFTING` at timestamp |
| **10:12** | Israel set out from Sinai wilderness by stages; the cloud settled in Paran wilderness | `S_MARCHING` then `S_SETTLE` at Paran |
| **10:13** | They journeyed first by the mouth of YHWH through Moses | authority wrapper on first march |

**Top tree 10:11:** **L:** date stamp · **R:** cloud lifted from mishkan ha-edut — **event** isolated on RIGHT.  
**Top tree 10:12:** **L:** they journey from Sinai · **R:** cloud dwells in Paran — march vs settle split.

This is a **logged execution** of the Num 9 rules, not a new control system.

---

## 5. Pseudo-code (readable, not an interpreter)

```text
// After Exod 40: cloud ONLINE on sanctuary

function on_cloud_event(e):
  assert authority == al_pi_YHWH

  if e.type == COVERED_ON_MISHKAN:      # 9:15–16
      state = CAMPED
      visual = DAY_CLOUD or NIGHT_FIRE

  if e.type == LIFTED_FROM_TENT:        # 9:17 L, 9:21–22, 10:11
      state = MARCHING
      // 10:11 instance: from mishkan ha-edut at Sinai

  if e.type == DWELLS_AT(place):        # 9:17 R, 10:12
      state = CAMPED
      camp_at = place                   // e.g. Paran

  if e.type == PROLONGED(days):         # 9:19, 9:22
      state = CAMPED
      allow_march = false until LIFTED
```

---

## 6. Link back to sanctuary spine

| Spine stage | Relation to cloud FSM |
|-------------|----------------------|
| **Exod install** | Creates cloud-on-Tent **presence** (WRITE) |
| **Lev 1 operate** | Assumes machine **stationary and live** (speech from Tent; rites at entrance) — does not implement travel |
| **Num ops** | **Moves** the people with the dwelling under cloud control |
| **Deut recompile** | Later: land life with “place He chooses” (not this FSM; Step 3 / 6) |

**Interdependence:** without Exod go-live, Num cloud has no installed mishkan/Tent to cover; without Num rules, portable sanctuary has no stay/go protocol in the ops layer.

---

## 7. Limits

| Done | Not done |
|------|----------|
| Stay/go/lift/settle states from 9:15–23 | Full trumpet signals (10:1–10) |
| Instance 10:11–13 | Entire wilderness itinerary |
| Tree top-splits for key verses | Full leaf dump |
| Link to SYM_anan / mishkan | Binding halakhah of travel |

---

## 8. Step status

| Step | Status |
|------|--------|
| 1–4 | done |
| **5 Cloud FSM** | **done** (this file) |
| 6 Hub | pending |

---

## Changelog

- 2026-07-25: Step 5 cloud stay/go FSM from Num 9:15–23 + instance 10:11–13; linked to Exod 40 WRITE.
