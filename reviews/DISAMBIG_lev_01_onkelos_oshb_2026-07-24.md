# Lev 1 leaf disambiguation — Onkelos + OSHB morph

**Date:** 2026-07-24  
**Kind:** dual-track sense aid for Phase A leaf variables — **not** binding law  
**Status:** **done** for Lev 1 hard leaves (discuss before Phase B write-sites)  
**Decision:** Use **Targum Onkelos** as primary sense-checker; use **OSHB lemma/morph** (already in `Data/Lev.xml`) as form/root family. Not Radak bulk this pass (no local root book). Not Rambam for leaf naming.

**Related:**  
- Leaf ledger: `LEDGER_lev_01_phaseA_LEAF_2026-07-24.md`  
- Sanctuary storyboard: `REGISTRY_sanctuary_v0_2026-07-24.md`  
- Oral policy: named dual-track only; never silent-merge into Written  
- Standing: English not derivation source; Hebrew + tree first  

**Sources (labeled):**  
| Layer | Source | Tag |
|-------|--------|-----|
| Structure / surface | Hebrew + ta'amim tree v1 | `[HE-WRITTEN][HE-STRUCT]` |
| Form / lemma family | OSHB `lemma` + `morph` on `Data/Lev.xml` | `[#IMPOSED:OSHB-morph]` |
| Traditional sense | Targum Onkelos Lev 1 (Sefaria `Onkelos_Leviticus.1`) | `[ORAL/TARGUM-Onkelos]` |
| English of Onkelos | Sefaria English of that Targum | `[EN-AID]` of dual-track only |

On substantive update: rename to today’s date and fix links.

---

## 0. Decision (why Onkelos, not only roots)

| Tool | Best for | Used here? |
|------|----------|------------|
| **Onkelos** | “What does this **verse** mean by this word?” | **Yes — primary for hard leaves** |
| **OSHB morph/lemma** | Prefixes, noun vs verb family, Strong’s-style id | **Yes — on every hard leaf** |
| Radak *Shorashim* | Root dictionary across corpus | Not this pass (no dump in `Data/`) |
| Rambam | Codified procedure later | Not for naming leaves |

Onkelos matches what you remembered: **Aramaic Torah that chooses a reading**.  
OSHB is free in-repo data for “is this the offering-noun family or the go-up verb family?”

---

## 1. Rules of use (so we don’t cheat)

1. **Written leaf + path stay first** — Targum does not move a leaf or invent a tree.  
2. **Dual-track only** — Onkelos is quoted beside the leaf; it does not replace Hebrew.  
3. **OSHB is labeled `#IMPOSED`** — morphology is external scholarly markup, useful and fallible.  
4. **English of Onkelos is for you to read** — not a new source of variables.  
5. Outcome per leaf: `clear` | `cleared_by_onkelos` | `cleared_by_morph` | `still_open`.

---

## 2. Hard-leaf pass (the ones that were unclear)

### 2.1 `עלה` / *olah* — burnt offering vs “went up”

| Field | Value |
|-------|--------|
| **Hebrew surface** | עלה / העלה / לעלה |
| **Ledger VARs** | `VAR_olah`, `VAR_ha_olah`, `VAR_le_olah` |
| **Verses** | 1:3, 1:4, 1:6, 1:9, 1:10, 1:13, 1:14, 1:17 |
| **Risk** | Same letters as verb “go up” |

**OSHB morph `[#IMPOSED]`:** every Lev 1 hit uses **lemma `5930`** (offering-noun family), **not** `5927` (go-up verb). Morph like `HNcfsa` / `HTd/Ncfsa` = noun forms.  

**Onkelos `[ORAL/TARGUM]`:** consistently **עֲלָתָא** / *alata* / “burnt-offering” (e.g. 1:3 “If his offering is a **burnt-offering**…”; 1:4 “head of the **burnt-offering**”).  

| Verdict | **`cleared_by_morph` + `cleared_by_onkelos`** |
|---------|-----------------------------------------------|
| Variable sense | **Burnt-offering type**, not motion verb |
| Keep separate forms? | Yes for now: bare / *ha-* / *le-* are grammar forms of same type family |

---

### 2.2 `אשה` / *isheh* — fire-offering vs “woman”

| Field | Value |
|-------|--------|
| **Hebrew surface** | אשה |
| **Ledger VAR** | `VAR_isheh` |
| **Verses** | 1:9, 1:13, 1:17 (formula end of path) |
| **Risk** | Same spelling as “woman” in other contexts |

**OSHB morph:** lemma **`801`** (fire-offering / *isheh* technical), morph `HNcmsc` — **not** lemma `802` (woman).  

**Onkelos:** does **not** always keep a separate Aramaic word for *isheh*; it often **folds** `אשה ריח ניחח` into a favor-acceptance formula, e.g. 1:9 AR roughly:  
עֲלָתָא קֻרְבַּן דְּמִתְקַבֵּל בְּרַעֲוָא קֳדָם יְיָ  
*alata … qurban de-mitqabbel be-ra‘ava qodam YY*  
EN-AID: “burnt-offering, an offering accepted with favor before Adonoy.”  

| Verdict | **`cleared_by_morph`** for “not woman”; Onkelos **paraphrases the whole aroma formula** |
|---------|----------------------------------------------------------------------------------------|
| Variable sense | **Ritual fire-offering term in closing formula**, not “woman” |
| Note | Do not expect 1:1 leaf-to-leaf Aramaic for *isheh*; Targum rewrites the packet |

---

### 2.3 `בני` / *benei* — “sons of …” needs the next leaf

| Surface chain | Verses | Onkelos (sense) | Verdict |
|---------------|--------|-----------------|---------|
| בני ישראל | 1:2 | בְּנֵי יִשְׂרָאֵל / Bnei Yisrael | **clear** multi-leaf `VAR_benei_yisrael` |
| בני אהרן (+ הכהנים/הכהן) | 1:5,7,8,11 | בְּנֵי אַהֲרֹן כָּהֲנַיָּא / sons of Aharon the kohanim | **cleared_by_onkelos** as **priest operators** |
| בני היונה | 1:14 | בְּנֵי יוֹנָה / young pigeons | **clear** bird type (not people) |

**OSHB:** `בני` is construct “sons of”; following name has its own lemma (Israel / Aaron / yonah).  

| Verdict | Leaf `בני` alone is **not** a variable; **multi-leaf span is the name** |
|---------|----------------------------------------------------------------------|
| Design | Keep `VAR_benei_aharon` + `VAR_ha_kohanim` **or** one compound — Onkelos supports treating “sons of Aharon the kohanim” as **one office phrase** |

---

### 2.4 Tent / entrance — install names

| Hebrew | OSHB | Onkelos Aramaic | EN-AID (Onkelos EN) | Verdict |
|--------|------|-----------------|---------------------|---------|
| מאהל מועד (1:1) | lemma `168` + `4150`; `מ/` = from | מִמַּשְׁכַּן זִמְנָא | from the Tent of Meeting | **cleared_by_onkelos** |
| פתח אהל מועד (1:3, 1:5) | same lemma pair | תְּרַע מַשְׁכַּן זִמְנָא | entrance of the Tent of Meeting | **cleared_by_onkelos** |

Aramaic pair: **מַשְׁכַּן זִמְנָא** / *mashkan zimna* / “dwelling of the appointed time” ≈ Tent of Meeting.  
**תְּרַע** / *tera* / “gate/entrance.”  

| Variable sense | Stable install names: from-Tent, entrance-of-Tent |
|----------------|---------------------------------------------------|

---

### 2.5 Altar / blood / priests

| Hebrew | OSHB lemma | Onkelos | Verdict |
|--------|------------|---------|---------|
| מזבח / המזבח / המזבחה | `4196` | מַדְבְּחָא / *madbecha* / altar | **clear** |
| דם / הדם / דמו | `1818` | דְּמָא / *dema* / blood | **clear** |
| כהן / כהנים | `3548` | כַּהֲנָא / כָּהֲנַיָּא | **clear** |
| בני אהרן | Aaron `175` + sons | בְּנֵי אַהֲרֹן | **clear** |

Directional form **המזבחה** (onto the altar): OSHB morph includes directional `Sd` on 1:9, 1:13, etc. — same altar variable, **goal form**.

---

### 2.6 Acts: lean / slaughter / dash / smoke

| Hebrew | Verses | Onkelos sense (EN-AID) | Verdict |
|--------|--------|------------------------|---------|
| וסמך | 1:4 | lay/lean his hand | **clear** |
| ושחט | 1:5, 1:11 | slaughter (*yikkos*) | **clear** |
| וזרקו | 1:5, 1:11 | sprinkle/dash blood | **clear** |
| והקטיר | 1:9+ | burn / cause to go up in smoke on altar | **clear** (ritual burn, not casual fire) |

---

### 2.7 Type menu: cattle / flock / bird

| Hebrew | Onkelos | Verdict |
|--------|---------|---------|
| בהמה | בְּעִירָא (animals) | **clear** class |
| בקר / בן הבקר | תּוֹרֵי / בַּר תּוֹרֵי (cattle / calf) | **clear** |
| צאן | עָנָא (flock) | **clear** |
| עוף | עוֹפָא (fowl) | **clear** |
| תרים / בני יונה | turtledoves / young pigeons | **clear** |

---

### 2.8 Place details that were “OPEN”

| Hebrew | Verse | Onkelos EN-AID | Verdict |
|--------|-------|----------------|---------|
| צפנה | 1:11 | north side of the altar | **cleared_by_onkelos** (geometry of slaughter) |
| מקום הדשן | 1:16 | place where they throw the ashes | **cleared_by_onkelos** (ash dump locus) |

These are **local rite places**, not necessarily Exodus install symbols — still useful as variables; Phase B will ask if an earlier write exists.

---

### 2.9 Formula `ריח ניחח` / pleasing aroma

| Hebrew | Verses | Onkelos |
|--------|--------|---------|
| ריח ניחח / ניחוח | 1:9, 1:13, 1:17 | Often folded into “accepted with favor before Adonoy” |

| Verdict | **cleared as favor-acceptance formula** (Targum paraphrases more than calques) |
|---------|--------------------------------------------------------------------------------|

---

## 3. Summary table (variable clarity after this pass)

| VAR / Hebrew focus | Before | After Onkelos+OSHB |
|--------------------|--------|---------------------|
| `VAR_olah` family | homograph risk | **cleared** (lemma 5930 + עלתא) |
| `VAR_isheh` | woman vs fire-offering | **cleared** (lemma 801; not woman) |
| `VAR_benei_*` | bare בני unclear | **cleared** only as multi-leaf |
| `VAR_ohel_moed` / petach / me- | install | **cleared** (משכן זימנא / תרע) |
| `VAR_ha_mizbeach` family | clear-ish | **cleared** (מדבחא) |
| `VAR_ha_dam` family | clear | **cleared** |
| `VAR_benei_aharon` / kohen | clear-ish | **cleared** as office phrase |
| `VAR_tzafonah` | open | **cleared** (north side) |
| `VAR_mekom_ha_deshen` | open | **cleared** (ash place) |
| `VAR_reach_nichoach` | formula | **cleared** as favor formula (paraphrase) |

**No Lev 1 ledger VAR left in pure “homograph fog.”**  
Phase B can chase **write-sites** without guessing sense.

---

## 4. Recommended naming policy (updated by this pass)

1. **Canonical key** = Hebrew surface span (multi-leaf when construct).  
2. **Form variants** of same type (המזבח / המזבחה) → one **family**, note form.  
3. **OSHB lemma id** optional field on VAR for cross-book joins later (`4196` altar, `5930` olah…).  
4. **Onkelos gloss** optional dual-track field — never sole authority.  
5. Prefer compound **בני אהרן הכהנים** as one office phrase when tree+Targum group them (still OK to keep sub-ids).

---

## 5. What we did *not* do

- Did not rewrite the leaf ledger paths  
- Did not merge Oral into Written STEPs  
- Did not download permanent Onkelos into `Data/` (fetched via Sefaria API for this report; re-fetch or add dump if you want offline)  
- Did not run Radak or full Strong’s dictionary  

---

## 6. Discussion / next

**Ready for Phase B** when you are: for each **install-family** VAR (`ohel_moed`, `petach`, `mizbeach`, `kohen`/`benei_aharon`, presence formulas), attach **earliest Written write-site** (mostly Exodus), still with tree at the use site.

Optional later: save `Data/targum_onkelos_he.json` for offline dual-track.

---

## Changelog

- 2026-07-24: Decision = Onkelos primary + OSHB morph secondary; Lev 1 hard-leaf disambiguation pass complete.
