# Expansion without BR: Gen header not mentioned → full Tanakh search

**Date:** 2026-07-26  
**Question:** Can we find an **expansion** for a **Genesis verse BR does not mention**, by searching the **whole Hebrew Bible** (not BR)?  
**Kind:** explore / T-expand probe · **not** binding law  
**Data:** OSHB morphhb WLC (`/tmp/morphhb/wlc`, **23 213** verses) + Strong’s lemmas; BR = `Data/bereshit_rabbah_he.json`  
**Related:** [VERIFY_br_complete_gen_coverage_2026-07-26.md](VERIFY_br_complete_gen_coverage_2026-07-26.md) · T6 light expand · absolute ports  

---

## 1. One-line answer

**Yes.** **Gen 1:22** (fish/bird blessing: *peru u-revu u-mil’u* the **waters/seas**, birds multiply on **earth**) has:

| Gate | Result |
|------|--------|
| BR **tagged** cite | **0** (`<small>(בראשית א, כב)</small>` never) |
| BR **bare** distinctive 1:22 text | **not found** (water-fill / bird-on-earth lines) |
| Full Tanakh **same-opcode expands** | **many** (Gen 1:28, 9:1–7, 17:20, 28:3, 35:11, Exod 1:7, Jer/Ezek re-issues, …) |

So expansion is **discoverable from Written Tanakh alone**. BR is **not** required as the index that opens this header.

---

## 2. Method (how “not mentioned” + “expansion” were defined)

### 2.1 Not mentioned in BR

Two independent filters (both required for a **clean** probe):

1. **Tagged cites:** parse `<small>(בראשית …)</small>` with Hebrew chapter/verse letters (e.g. `א, כח` = 1:28).  
2. **Bare distinctive phrases:** consonantal search of the whole BR blob for verse-specific strings (not stock formulas shared with other verses).

Tagged-only “uncited” is **not** enough: Gen **1:7 / 1:10 / 1:27** are tag-0 but **bare-quoted** in BR (firmament make, name dry land, create adam in image).

### 2.2 Expansion (absolute, no BR)

On full morphhb (all books):

- Build verse → set of **Strong’s numbers** on `<w lemma=…>`.  
- Query **multi-lemma packages** from the header’s content roots.  
- Rank hits by **extra content lemmas** (fields the header lacks).  
- Prefer hits that keep the **same opcode family** and add parameters (who, where, how much, rule, nation, knowledge-fill, …).

This is the same spirit as absolute ports / T6: **thin header → later verse with more fields on the same operator**.

---

## 3. Clean vs contaminated Gen 1 candidates

| Ref | BR tags | Distinctive bare in BR? | Notes |
|-----|--------:|-------------------------|--------|
| 1:7 | 0 | **yes** (e.g. *va-ya‘as … ha-raqia‘*) | Contaminated |
| 1:8 | 0 | **yes** (name raqia shamayim) | Contaminated |
| 1:10 | 0 | **yes** (name dry land / seas) | Contaminated |
| 1:13 | 0 | **yes** (day-three close formula) | Contaminated |
| 1:18 | 0 | **partial** (*u-limshol ba-yom u-va-lailah* yes) | Not clean |
| **1:19** | 0 | **no** (full *yom revi‘i* close) | Clean but **thin day-close** — weak expand class |
| **1:22** | 0 | **no** on 1:22-only lines | **Best clean expand-header** |
| **1:23** | 0 | **no** (*yom chamishi*) | Clean day-close control |
| 1:27 | 0 | **yes** (*va-yivra … be-tsalmo*) | Contaminated |
| **1:29** | 0 | **no** on food-grant markers | Clean; strong expand (→ Gen 9:3) |
| **1:30** | 0 | **no** on animal-food markers | Clean; pairs 1:29 / 9:3 |

**Neighbor note:** BR **does** tag Gen **1:20** (5×), **1:21** (2×), **1:28** (2×). So the **swarm/create/human-rule block** is touched — but the **first blessing of water-creatures and birds (1:22)** is never tagged and never bare-quoted as the water/bird formula. BR can sample a block without indexing every header.

### Bare checks specific to 1:22 (all False in BR)

| Phrase (plain) | Gloss |
|----------------|--------|
| והעוף ירב בארץ / *ve-ha-‘of yirev ba-arets* | “and the bird shall multiply on the earth” |
| ומלאו את המים בימים / *u-mil’u et ha-mayim ba-yamim* | “and fill the waters in the seas” |
| פרו ורבו ומלאו את המים / *peru u-revu u-mil’u et ha-mayim* | full water-domain fruitfulness |

**Contrast (human package — present in BR bare/tags):**  
פרו ורבו ומלאו את הארץ / *peru u-revu u-mil’u et ha-arets* / “be fruitful… fill the **earth**” and ורדו בדגת / *u-redu bi-dgat* / “and rule the fish of…” → **Gen 1:28** territory, not 1:22.

---

## 4. Header under test: Gen 1:22

**Hebrew:**  
וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ אֶת הַמַּיִם בַּיַּמִּים וְהָעוֹף יִרֶב בָּאָרֶץ  

**Translit:**  
*va-yevarekh otam elohim lemor: peru u-revu u-mil’u et ha-mayim ba-yamim; ve-ha-‘of yirev ba-arets*

**English:**  
“And God blessed them, saying: Be fruitful and multiply and fill the waters in the seas, and let the bird multiply on the earth.”

### Content Strong’s (operator inventory)

| H# | lemma / xlit | role in 1:22 |
|----|----------------|--------------|
| H1288 | ברך / *barakh* | bless |
| H6509 | פרה / *parah* | be fruitful |
| H7235 | רבה / *ravah* | multiply |
| H4390 | מלא / *male* | fill |
| H4325 | מים / *mayim* | waters (fill domain) |
| H3220 | ים / *yam* | seas |
| H5775 | עוף / *‘of* | bird |
| H776 | ארץ / *erets* | earth (bird domain) |
| H430 | אלהים / *elohim* | agent |

**Thin header / gap list (why it “needs expand”):**

1. **Domain split only** — water-fill for swarmers; bird multiply on land — no human, no nation, no land-fill for humans.  
2. **No rule/subdue** — no *radah* / *kavash*.  
3. **No post-flood re-issue** or history fulfillment.  
4. **No numeric / national fields** (princes, goy, kehal amim, kings).  
5. **Fill** stays physical (waters); later corpus also fills earth with **people** or **knowledge**.

---

## 5. Full Tanakh expansion table (no BR used to find these)

Multi-lemma search on **23 213** verses. Packages below are **absolute** (shared Strong’s sets).

### 5.1 Core opcode: bless + fruitful + multiply + fill  
**Required:** H1288 ∩ H6509 ∩ H7235 ∩ H4390  

| Hit | Extra fields vs 1:22 | How it expands |
|-----|----------------------|----------------|
| **Gen 1:28** | subdue *kavash* H3533; rule *radah* H7287; fill **earth**; rule fish/bird/living | **Same blessing opcode → human + dominion stack** |
| **Gen 9:1** | Noah + sons; fill **earth** (not seas) | **Post-flood re-issue** to new human root |

Only **two** Tanakh verses hold the full four-root bless package; both are **expansions of 1:22’s thinner animal form**.

### 5.2 Fruitful + multiply + fill (may drop explicit *barakh* in-verse)  
**Required:** H6509 ∩ H7235 ∩ H4390  

| Hit | Expansion note |
|-----|----------------|
| Gen 1:28, 9:1 | as above |
| **Exod 1:7** | Israel *paru… va-yishretsu… va-yirbu… va-ya‘atsmu*; earth **filled** with them — **historical fulfillment / swarm language** (*sharats*) layered on fruitfulness |

### 5.3 Fruitful + multiply (wider family)  
**Required:** H6509 ∩ H7235 · **14** remote hits (sample of high-value expands)

| Hit | he (short) | en role |
|-----|------------|---------|
| **Gen 8:17** | …וּפָרוּ וְרָבוּ עַל הָאָרֶץ / *u-faru ve-ravu ‘al ha-arets* | Exit ark: living things **fruitful/multiply on earth** (restores land swarm after flood) |
| **Gen 9:7** | פְּרוּ וּרְבוּ שִׁרְצוּ בָאָרֶץ / *peru u-revu shirtsu ba-arets* | Second flood blessing + **swarm** imperative |
| **Gen 17:20** | בֵּרַכְתִּי… הִפְרֵיתִי… הִרְבֵּיתִי… שְׁנֵים עָשָׂר נְשִׂיאִים… גּוֹי גָּדוֹל | Ishmael: bless + fruit + multi + **12 princes + great nation** |
| **Gen 28:3** | יְבָרֵךְ… יַפְרְךָ… יַרְבֶּךָ… לִקְהַל עַמִּים | Jacob: El Shaddai → **assembly of peoples** |
| **Gen 35:11** | פְּרֵה וּרְבֵה גּוֹי וּקְהַל גּוֹיִם… וּמְלָכִים | Jacob: **nation + assembly of nations + kings** from loins |
| **Gen 48:4** | מַפְרְךָ וְהִרְבִּיתִיךָ… לִקְהַל עַמִּים + land grant | Ephraim/Manasseh line: multi + **kehal amim** + eternal holding |
| **Jer 3:16** | תִרְבוּ וּפְרִיתֶם בָּאָרֶץ… | Future multi/fruitful **in land**; ark memory drops |
| **Jer 23:3** | וּפָרוּ וְרָבוּ | Remnant flock restored → multi |
| **Ezek 36:11** | וְהִרְבֵּיתִי… אָדָם וּבְהֵמָה וְרָבוּ וּפָרוּ | Land repopulation: human **and** beast multi/fruitful |

### 5.4 Metaphorical “fill” (same *male* + water/sea image, new object)

| Hit | Package | Expansion type |
|-----|---------|----------------|
| **Isa 11:9** | earth **full** of knowledge of YHWH **as waters cover sea** | *male* retargeted: knowledge, not fish |
| **Hab 2:14** | earth **full** of knowledge of glory… waters cover sea | same knowledge-fill port |

These are **not** biological fruitfulness, but they **reuse fill + water/sea** imagery — a second expansion rail off the “fill waters” half of 1:22.

### 5.5 Side clean headers (same probe, shorter)

**Gen 1:29** (food grant: seed-bearing plant + tree fruit → *okhlah*) — tag 0, bare clean.  
**Strong expand:** **Gen 9:3** — *kol remes… le-okhlah; ke-yereq ‘esev natati…* / all living crawlies for food; green herb baseline still given. **Diet law expands** from plant-only grant to meat + plant analogy.

**Gen 1:30** (green herb for animals) — pairs with 9:3 (*yereq ‘esev*).  

**Gen 1:19** (day-four close) — clean but H7243 “fourth” elsewhere is **calendar/history**, not opcode expand of create-week. Control: **not every clean uncited verse is Class A expand-header**.

---

## 6. What “expansion” looks like on 1:22 (operator view)

```
Gen 1:22  BLESS( animals_water_bird )
          PERU + RAVU
          MALE( domain=waters/seas )
          RAVAH( bird, domain=earth )
                │
                ├─► Gen 1:28  same stack + MALE(earth) + KAVASH + RADAH(fish,bird,living)
                ├─► Gen 8:17 / 9:1 / 9:7  re-issue after flood (+ sharats, human sons)
                ├─► Gen 17 / 28 / 35 / 48  national fields (goy, kehal, princes, kings, land)
                ├─► Exod 1:7  runtime fulfillment in Israel
                ├─► Jer / Ezek  remnant / land multi re-application
                └─► Isa 11:9 / Hab 2:14  MALE retarget (knowledge ~ waters covering sea)
```

**Discovery path without BR:**  
(1) Parse 1:22 content roots → (2) intersect full Tanakh on {parah, ravah} then tighten with male/barakh → (3) read extra fields → (4) rank as expand.  
No Oral index required for the first pass.

---

## 7. Implications for “does BR give every expand we need?”

| Claim | Status after this probe |
|-------|-------------------------|
| C1: BR cites every Gen verse | already **false** (tags ~72.5%) |
| C2: BR cites every Gen expand-header | **further falsified** for tags+bare: **1:22** is expand-header, unmentioned, **rich remote expands exist** |
| BR useless | **false** — still dense training set; tags **1:20–21, 1:28** near this package |
| Expansions only exist when BR lists them | **false** — Written graph alone opens 1:22 |

**Fair softening:** BR may teach the **fruitfulness family** via **1:28** (tagged) and bare “fill the earth,” so a human reader of BR can learn the **opcode** without ever seeing 1:22 cited. That is **block sampling**, not **complete header index**. The question was whether we can find expansion for a verse **not mentioned** — answer remains **yes**.

---

## 8. Confidence

| Item | Label |
|------|--------|
| 1:22 tag count 0 | **tested** |
| 1:22 distinctive bare absent | **tested** (listed phrases) |
| Full Tanakh multi-lemma expands for parah∩ravah(+male/barakh) | **tested** |
| Gen 1:28 / 9:1 are same-opcode expansions of 1:22 | **strong hypothesis** (clear field add) |
| Isa/Hab are secondary fill-rail expands | **hypothesis** (image reuse, not biology) |
| Same method works for 1:29 → 9:3 | **tested** package hit |
| C2 (complete expand-header index) | **false** for this counterexample |

---

## 9. Artifacts / how to re-run

Re-run sketch (repo root; needs `/tmp/morphhb/wlc` + BR JSON):

1. Load all `*.xml` under morphhb WLC → verse → Strong’s sets.  
2. Load BR blob; confirm tag 0 for `א, כב`; bare-search 1:22-only strings.  
3. `find verses where {6509,7235,4390,1288} ⊆ strongs` (and relax sets as in §5).  

Machine notes from this pass live conceptually with coverage cache `_br_gen_coverage.json` (tagged map); this report is the human-readable T-expand result.

---

## 10. Bottom line

We searched **all of the cantillated Hebrew Bible** for expansions of a Genesis verse **BR does not mention**.

**Gen 1:22** is that verse: **no tag, no distinctive bare quote**, yet the Tanakh repeatedly **re-opens** its fruitfulness/fill blessing with **more parameters** (dominion, flood reset, nations, history, knowledge-fill).

**BR is a rich manual, not the only door** — and not a complete list of expand-headers.
