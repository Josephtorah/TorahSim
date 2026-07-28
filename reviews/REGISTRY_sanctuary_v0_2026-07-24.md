# Sanctuary symbol table v0 — Exodus writes, Leviticus 1 reads

**Date:** 2026-07-24  
**Kind:** cross-book variable lab (hypothesis / working model — **not** binding religious law)  
**Status:** **Step 1 of sequence** — discuss before Step 2 (ambient Gen) or Step 3 (dry-runner)  
**Related:**  
- Pointer theory: `ARCHITECTURE_pass2_pointers_2026-07-19.md`  
- Registries: `ARCHITECTURE_pass3_registries_2026-07-19.md`  
- Units: `logic/units/exo_25_*` … `exo_40_*`, `logic/units/lev_01_*`  
- Hebrew source: `Data/Exod.xml`, `Data/Lev.xml`

On substantive update: rename to today’s date and fix links.

---

## 0. What this step is / is not

| This is | This is not |
|---------|-------------|
| A **declare / use** map for sanctuary free names | A running interpreter |
| **Written→Written** only (Exod install → Lev 1 operate) | Oral merge |
| Small enough to discuss in one sitting | Full Exodus or full Leviticus inventory |
| Layer **L1 install** (Tent/priests/altar/presence) | Layer L0 Genesis ambient (next step) |

**One-sentence claim (hypothesis):**  
Leviticus 1 **does not reinstall** the sanctuary; it **resolves names** that Exodus already wrote into a symbol table, then runs offering procedures against that environment.

---

## 1. Mental model (program-shaped)

```text
EXODUS 25–40          LEVITICUS 1
─────────────────     ─────────────────────────────
WRITE symbols    →    READ free names (no rebuild)
  mikdash goal          speech FROM ohel_moed (1:1)
  pattern (tavnit)      bring TO petach_ohel (1:3)
  altar design          blood ON mizbeach (1:5+)
  priest office         operators = benei_aharon (1:5+)
  presence online       assumes machine is live (P-STATE)
                      + LOCAL app vars (olah, bakar, dam…)
```

**Kinds of “variables” in this lab**

| Kind | Role | Example |
|------|------|---------|
| **Install symbol** | Written once in Exod; reused by name | `ohel_moed` |
| **Runtime flag** | State after install | `kavod_online` (glory filled) |
| **App-local** | Declared/used inside Lev 1 procedure | `olah`, `bakar`, blood rites |
| **Ambient** | World already true (mostly Gen) | day, kinds, people — **not this file** |

---

## 2. DECLARE table — Exodus writers (sanctuary install)

Primary write loci use **install-sense** Exodus (tabernacle block), not earlier narrative reuses (e.g. early “altar” of war, Midian “kohen”).

| Symbol id | Hebrew | Translit | English | Primary write (Written) | Unit export (if any) | Notes |
|-----------|--------|----------|---------|-------------------------|----------------------|-------|
| `SYM_mikdash_dwell` | מִקְדָּשׁ … וְשָׁכַנְתִּי | *mikdash … ve-shakhanti* | Sanctuary so I dwell among them | **Exod 25:8** | `EXPORT_mikdash_dwell` (`exo_25_…`) | Goal of whole install |
| `SYM_tavnit` | תַּבְנִית הַמִּשְׁכָּן | *tavnit ha-mishkan* | Pattern of the mishkan | **Exod 25:9** | `EXPORT_pattern_mountain` | Blueprint / data, not yet built object |
| `SYM_mishkan` | מִשְׁכָּן | *mishkan* | Dwelling structure | **Exod 25:9** onward; erect **40** | (spread) | Built object family |
| `SYM_ohel_moed` | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting | Named in install block (e.g. **27:21**; erect **40**) | (spread) | Speech / meeting center |
| `SYM_petach_ohel` | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | Entrance of the Tent of Meeting | **Exod 29:4** (wash/bring); function **29:42** | via investiture | **Place key** for later rites |
| `SYM_speech_meet` | אִוָּעֵד … לְדַבֵּר | *ivva’ed … ledabber* | I will meet / speak there | **Exod 29:42** | (with tamid) | Explains **why** Lev 1:1 speech-from-Tent works |
| `SYM_mizbeach_olah` | מִזְבַּח (הָעֹלָה) | *mizbeach (ha-olah)* | (Burnt-offering) altar | Design **Exod 27:1+**; placed **40:6** at entrance | `EXPORT_mizbeach_nechoshet` | Lev 1 blood/fire target |
| `SYM_benei_aharon` | בְּנֵי אַהֲרֹן | *benei Aharon* | Sons of Aaron | Appoint **Exod 28:1**; clothed/invested **28–29** | priest garment units | Operators of blood/fire |
| `SYM_kohen_office` | לְכַהֲנוֹ לִי | *le-khahano li* | To priest for Me | **Exod 28:1, 28:3–4** | garments / investiture | Office, not one garment only |
| `SYM_olat_tamid` | עֹלַת תָּמִיד | *olat tamid* | Continual burnt offering | **Exod 29:38–42** | `EXPORT_olat_tamid` | Same *olah* family as Lev 1; different schedule |
| `SYM_kavod_online` | כְּבוֹד יְהוָה מָלֵא | *kevod YHWH male* | Glory filled the mishkan | **Exod 40:34–35** | `EXPORT_mishkan_filled` | **Runtime: machine live** |
| `SYM_anan_cover` | הֶעָנָן | *he-anan* | Cloud covering Tent | **Exod 40:34–35** | `EXPORT_cloud_journey` | Presence signal (later travel too) |
| `SYM_lev_handoff` | — | — | Install complete → Lev free names resolve | **Exod 40** end-state | `EXPORT_lev_handoff` | Project-level handoff label |

**Confidence:** locus list = **tested (observable in Hebrew)**; “symbol table” framing = **hypothesis**.

### Install sequence (ordered “writes”)

```text
1. Goal + pattern     Exod 25:8–9     SYM_mikdash_dwell, SYM_tavnit
2. Furniture/altar    25–27           SYM_mizbeach_olah (design)
3. Priests            28–29           SYM_benei_aharon, SYM_kohen_office
4. Place + speech fn  29:4, 29:42     SYM_petach_ohel, SYM_speech_meet
5. Erect + place      40              SYM_mishkan, SYM_ohel_moed, altar at door
6. Presence online    40:34–35        SYM_kavod_online, SYM_anan_cover
7. Handoff            after 40        SYM_lev_handoff → Lev may operate
```

---

## 3. USE table — Leviticus 1 free names (all 17 verses)

Source: normalized Hebrew from `Data/Lev.xml` ch.1.  
Pointer types from Pass 2: **P-NAME**, **P-PLACE**, **P-STATE**, **P-JOIN** (class word).

### 3.1 Resolve matrix (install symbols → Lev 1)

| Lev free name (as used) | Verses in Lev 1 | Resolves to DECLARE | Pointer | Rebuilds install? |
|-------------------------|-----------------|---------------------|---------|-------------------|
| אֹהֶל מוֹעֵד / *ohel mo’ed* / Tent of Meeting | 1:1, 1:3, 1:5 | `SYM_ohel_moed` (+ live after 40) | **P-NAME** + **P-STATE** | **No** |
| מֵאֹהֶל מוֹעֵד / *me-ohel mo’ed* / **from** the Tent | 1:1 | `SYM_speech_meet` + `SYM_kavod_online` | **P-STATE** (speech source) | **No** |
| פֶּתַח אֹהֶל מוֹעֵד / *petach ohel mo’ed* / entrance | 1:3, 1:5 | `SYM_petach_ohel` | **P-PLACE** | **No** |
| בְּנֵי אַהֲרֹן הַכֹּהֲנִים / *benei Aharon ha-kohanim* | 1:5, 1:8, 1:11 | `SYM_benei_aharon` + office | **P-NAME** | **No** |
| בְּנֵי אַהֲרֹן הַכֹּהֵן / *… ha-kohen* (sg) | 1:7 | same office family | **P-NAME** | **No** |
| הַכֹּהֵן / *ha-kohen* / the priest | 1:9, 1:12–13, 1:15, 1:17 | `SYM_kohen_office` | **P-NAME** | **No** |
| הַמִּזְבֵּחַ / *ha-mizbeach* / the altar | 1:5, 1:7–9, 1:11–13, 1:15–17 | `SYM_mizbeach_olah` | **P-NAME** | **No** |
| לִפְנֵי יְהוָה / *lifnei YHWH* / before YHWH | 1:3, 1:5, 1:11 | ambient + sanctuary presence | **P-PLACE**/presence | **No** |

**Hit rate (install symbols):** every sanctuary free name in Lev 1 has a clear Exodus write. **No MISSING** for Tent / entrance / priests / altar.

### 3.2 App-local symbols (declared *inside* Lev 1, not Exod install)

These are **procedure variables**, not sanctuary environment:

| Symbol | Hebrew | Translit | English | Lev 1 role |
|--------|--------|----------|---------|------------|
| `APP_korban` | קָרְבָּן | *korban* | Offering / approach-gift | Opening type (1:2) |
| `APP_behemah` | בְּהֵמָה | *behemah* | Domestic animal class | Parent type before cattle/flock |
| `APP_bakar` | בָּקָר | *bakar* | Cattle | Path A (1:3–9) |
| `APP_tzon` | צֹאן | *tzon* | Flock | Path B (1:10–13) |
| `APP_of` | עוֹף | *of* | Bird | Path C (1:14–17) |
| `APP_olah` | עֹלָה | *olah* | Burnt offering | Procedure family (all paths) |
| `APP_dam` | דָּם | *dam* | Blood | Applied to altar (esp. cattle/flock/bird) |
| `APP_tamim` | תָּמִים | *tamim* | Whole / unblemished | Validity guard on animal |
| `APP_samakh` | סָמַךְ | *samakh* | Hand-lean | Identification act (1:4) |

**Note:** `APP_olah` **joins** Exod’s `SYM_olat_tamid` by **class word** (P-JOIN) but Lev 1 is not “run the daily tamid schedule”; it is case law for when a person brings an olah. Same *type family*, different call site.

### 3.3 Verse-by-verse USE log (Lev 1)

| v | Install symbols used | App-local | Program-shaped reading (hypothesis) |
|---|----------------------|-----------|--------------------------------------|
| 1 | `ohel_moed` (speech **from**) | — | Call entry: YHWH speaks from live Tent |
| 2 | — | korban, behemah, bakar, tzon | Declare offering type registry for this app |
| 3 | `petach_ohel` | olah, bakar, tamim | IF cattle olah → bring to **entrance** |
| 4 | — | olah, samakh | Lean hand on head (identity/accept) |
| 5 | `petach_ohel`, `benei_aharon`, `mizbeach` | dam, bakar | Slaughter; priests throw blood on altar at entrance side |
| 6 | — | olah | Flay / piece |
| 7 | `benei_aharon` / kohen, `mizbeach` | — | Fire + wood on altar |
| 8 | `benei_aharon`, `mizbeach` | — | Arrange pieces on fire |
| 9 | kohen, `mizbeach` | olah | Burn all; food-gift scent formula |
| 10 | — | tzon, olah, tamim | IF flock path |
| 11 | `mizbeach`, `benei_aharon` | dam | North side of altar; blood |
| 12–13 | kohen, `mizbeach` | olah | Arrange + burn |
| 14 | — | of, olah | IF bird path |
| 15–17 | kohen, `mizbeach` | dam, olah | Priest-led bird procedure at altar |

---

## 4. What this teaches about “Torah as program”

### 4.1 Declare / use **works** on this spine

```text
WRITE  SYM_ohel_moed, SYM_petach_ohel, SYM_benei_aharon, SYM_mizbeach_olah, SYM_kavod_online
READ   Lev 1 free names
RESULT all sanctuary names resolve; zero “undefined Tent”
```

That is the cross-book logic we wanted for Step 1.

### 4.2 Two different “variable” scopes

| Scope | Written behavior | Interpreter implication |
|-------|------------------|-------------------------|
| **Environment (Exod)** | Built once; presence on | Load install registry before any Lev app |
| **Procedure (Lev 1)** | IF cattle / flock / bird | Local stack for one offering call |

A future runner should **not** re-run Exod 25–40 inside each olah; it should **lookup** environment, then execute Lev steps.

### 4.3 Gaps (honest)

| Gap | Detail |
|-----|--------|
| Unit `depends_on` | Lev 1 units mostly chain **to each other**, not to `exo_40_*` — docs say free-name import; YAML ids under-wire it |
| Exports incomplete | Not every SYM_* has a clean unit export id yet |
| No runtime | This file is a **map**, not a program counter |
| Genesis | Not in this step (ambient day/kinds/people) |
| Oral | Not used (dual-track later if densifying) |

### 4.4 Status of claim

| Claim | Label |
|-------|--------|
| Lev 1 uses Tent/priests/altar without rebuilding them | **tested** (Hebrew read of ch.1 + Exod install loci) |
| Therefore Torah “has variables” in modern sense | **hypothesis** (our model) |
| Full five-book VM | **not claimed** |

---

## 5. Discussion prompts (stop here)

Before Step 2 (ambient Gen) or Step 3 (dry-runner), decide:

1. **Does this DECLARE/USE split match how you want to think about the system?**  
2. **Should we promote these SYM_* into real unit `exports` / Lev `depends_on`**, or keep a separate `registry/*.yaml` for now?  
3. **Anything missing from the sanctuary table** that Lev 1 clearly needs (e.g. wood, fire source, “place of ashes” 1:16)?  
4. **Ready for Step 2** (10 ambient Gen symbols Lev never redefines)?

---

## Changelog

- 2026-07-24: Step 1 created — sanctuary v0 + full Lev 1 resolve matrix.
