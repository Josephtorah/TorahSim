# Gold example: Lev 1:5 — 100% word (+ morph letter) coverage

**Date:** 2026-07-25  
**Kind:** precision template — every word has a role; morph pieces named where they matter  
**Status:** gold reference for “nothing out of place” accounting  
**Not:** binding religious law  

**Verse:** Leviticus 1:5  
**OSIS:** `Lev.1.5`  
**Parser:** `taamim_tree_parse.py` v1 · `status: unique` · 22 words  

**Related:**  
- Procedure use: `DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md` STEP_5  
- Pattern scan: `SCAN_glue_morph_patterns_2026-07-25.md`  
- Method: “account for every word; some morph letters; glue is still in place”

---

## 1. Plain line (all words, in order)

**Hebrew (unpointed plains):**  
ושחט את בן הבקר לפני יהוה והקריבו בני אהרן הכהנים את הדם וזרקו את הדם על המזבח סביב אשר פתח אהל מועד

**Translit (letter-map):**  
*ve-shahat et ben ha-bakar lifnei YHWH ve-hiqrivu benei Aharon ha-kohanim et ha-dam ve-zarku et ha-dam al ha-mizbeach saviv asher petach ohel mo'ed*

**EN-AID:**  
He shall slaughter the cattle-young before YHWH; the sons of Aaron the priests shall present the blood and dash the blood on the altar around, which is [at] the entrance of the Tent of Meeting.

---

## 2. Top tree (why the verse is “two programs”)

```text
TOP LEFT  — bringer side
  slaughter  +  cattle-young  +  before YHWH

TOP RIGHT — priest / sanctuary side
  present blood  +  dash blood on altar around  +  at entrance of Tent
```

**Code-like shape (pedagogy only):**

```text
// LEFT
bringer.slaughter(cattle_young, relation=before_YHWH)

// RIGHT
priests.present(blood)
priests.dash(blood, on=altar, around=true, at=petach_ohel_moed)
```

---

## 3. Full coverage table — every word

**Coverage: 22/22 words.**  
Roles: `act` · `glue_*` · `morph_*` · `content_*` · `free_name` · `relator` · `formula_adj`

| # | Path | Mark | Hebrew plain | Translit | Morph (OSHB) | Parts (slash) | Role | What it does | Feeds |
|--:|------|------|--------------|----------|--------------|---------------|------|--------------|-------|
| 0 | `LLL` | tevir | ושחט | *ve-shahat* | HC/Vqq3ms · lemma c/7819 | **ו** + שחט | **act** + **morph_vav** | And-he-shall-slaughter; vav links sequence | STEP slaughter |
| 1 | `LLRC0` | zero | את | *et* | HTo · 853 | את | **glue_object_marker** | Marks definite object of slaughter | → points to #2–3 |
| 2 | `LLRC1` | mercha | בן | *ben* | HNcmsc · 1121 | בן | **content_construct** | “son/young of …” | with #3 = animal |
| 3 | `LLRC2` | tifcha | הבקר | *ha-bakar* | HTd/Ncbsa · d/1241 | **ה** + בקר | **content_type** + **morph_ha** | The cattle (definite) | patient of slaughter |
| 4 | `LRL` | munach | לפני | *lifnei* | HR/Ncbpc · l/6440 | **ל** + פני | **relator_complex** | “before” (to-face of) | with #5 |
| 5 | `LRR` | etnachta | יהוה | *YHWH* | HNp · 3068 | יהוה | **divine_name** | YHWH; ends LEFT half | before_YHWH |
| 6 | `RLLL` | telisha_gedola | והקריבו | *ve-hiqrivu* | HC/Vhq3cp · c/7126 | **ו** + הקריבו | **act** + **morph_vav** | And-they-shall-bring-near (present) | priest present blood |
| 7 | `RLLRC0` | qadma | בני | *benei* | HNcmpc · 1121 | בני | **content_construct** | “sons of …” | office phrase start |
| 8 | `RLLRC1` | mahpach | אהרן | *Aharon* | HNp · 175 | אהרן | **content_person** | Aaron | with #7–9 |
| 9 | `RLLRC2` | pashta | הכהנים | *ha-kohanim* | HTd/Ncmpa · d/3548 | **ה** + כהנים | **free_name** + **morph_ha** | The priests; closes office phrase | `SYM_kohen` / with #7–8 `SYM_benei_aharon` |
| 10 | `RLRL` | zero | את | *et* | HTo · 853 | את | **glue_object_marker** | Marks blood as object of present | → #11 |
| 11 | `RLRR` | zaqef_qatan | הדם | *ha-dam* | HTd/Ncmsa · d/1818 | **ה** + דם | **content_substance** + **morph_ha** | The blood | patient of present |
| 12 | `RRLLC0` | qadma | וזרקו | *ve-zarku* | HC/Vqq3cp · c/2236 | **ו** + זרקו | **act** + **morph_vav** | And-they-shall-dash | dash blood |
| 13 | `RRLLC1` | zero | את | *et* | HTo · 853 | את | **glue_object_marker** | Marks blood again as object of dash | → #14 |
| 14 | `RRLLC2` | mahpach | הדם | *ha-dam* | HTd/Ncmsa · d/1818 | **ה** + דם | **content_substance** + **morph_ha** | The blood (same substance, new verb) | patient of dash |
| 15 | `RRLLC3` | zero | על | *al* | HR · 5921 | על | **glue_spatial** | “on” | → #16 |
| 16 | `RRLLC4` | pashta | המזבח | *ha-mizbeach* | HTd/Ncmsa · d/4196 | **ה** + מזבח | **free_name** + **morph_ha** | The altar | `SYM_mizbeach` |
| 17 | `RRLR` | zaqef_qatan | סביב | *saviv* | HNcbsa · 5439 | סביב | **adverb_spatial** | Around (how blood is applied) | dash manner |
| 18 | `RRRLL` | zero | אשר | *asher* | HTr · 834 | אשר | **glue_relative** | “which/that” opens locator clause | → #19–21 |
| 19 | `RRRLR` | tifcha | פתח | *petach* | HNcmsc · 6607 | פתח | **content_construct** | “entrance of …” | free-name phrase |
| 20 | `RRRRL` | mercha | אהל | *ohel* | HNcmsc · 168 | אהל | **content_construct** | “tent of …” | free-name phrase |
| 21 | `RRRRR` | silluq | מועד | *mo'ed* | HNcmsa · 4150 | מועד | **free_name_close** | “meeting” closes phrase; verse end | `SYM_petach_ohel` |

### Morph letter summary (only pieces with jobs)

| Piece | Where | Job |
|-------|--------|-----|
| **ו** / *ve-* | #0, #6, #12 | Sequence “and …” on finite verbs |
| **ה** / *ha-* | #3, #9, #11, #14, #16 | Definite article “the” |
| **ל** in לפני | #4 | Built into complex prep “before” (to + face) |
| **את** whole word | #1, #10, #13 | Object marker (three times) — **not** optional noise |
| Single consonants inside בקר/מזבח/… | spelling | Accounted as **spelling the content word**, not separate ops |

**Every consonant is in place** either as (a) spelling of a content word, (b) morph prefix with a named job, or (c) the full particle word **את** / **על** / **אשר**.

---

## 4. Glue / morph pattern cards **in this verse**

### P1 — Object chain: `verb + את + definite NP`

```text
שחט + את + בן הבקר
הקריבו + את + הדם
זרקו + את + הדם
```

**Job of את:** bind verb → definite patient.  
**Not a free name.** Dropping it would break precision of “what is acted on.”

### P2 — Same substance, two verbs, **את** repeated

```text
present  את הדם
dash     את הדם
```

**Pattern:** re-mark object when the **verb changes** (not “redundant waste”).  
Each **את** is required for its own verb frame.

### P3 — Spatial apply: `על + definite place`

```text
על + המזבח
```

**Job of על:** spatial “on.”  
Target is free name altar.

### P4 — Relative locator: `אשר + place phrase`

```text
אשר + פתח אהל מועד
```

**Job of אשר:** “which [is at] …” — attaches altar zone to entrance phrase.  
Without it, entrance could float free of the altar application clause.

### P5 — Complex preposition: `לפני + divine name`

```text
לפני + יהוה   (morph: l/ + panim “face”)
```

**Not** simple one-letter prefix only — OSHB treats as prep built from **ל + פני**.  
Role: relation of slaughter locus, not a free-name install.

### P6 — Construct chains (no glue word between)

```text
בן + הבקר     →  cattle-young
בני + אהרן + הכהנים →  office phrase
פתח + אהל + מועד →  entrance free name
```

**“Glue” here is construct syntax**, not a separate particle leaf.

### P7 — Vav on verbs = sequence / narrative chaining

```text
ושחט … והקריבו … וזרקו
```

Accounts for **ו** as discourse sequence on the procedure timeline.

---

## 5. Role inventory (nothing left over)

| Role class | Count | Indices |
|------------|------:|---------|
| act | 3 | 0, 6, 12 |
| glue_object_marker (את) | 3 | 1, 10, 13 |
| glue_spatial (על) | 1 | 15 |
| glue_relative (אשר) | 1 | 18 |
| relator_complex (לפני) | 1 | 4 |
| content / construct / type / substance | 9 | 2,3,7,8,11,14,19,20, (+ parts) |
| free_name / free_name_close | 3 | 9, 16, 21 |
| divine_name | 1 | 5 |
| adverb_spatial | 1 | 17 |
| **Total words** | **22** | **0 unassigned** |

---

## 6. How this feeds “code” (precise)

```text
// LEFT
slaughter(
  patient = construct(ben, ha_bakar),   // #2-3; object via et #1
  relation = before(YHWH)               // #4-5
)

// RIGHT
agents = phrase(benei, Aharon, ha_kohanim)  // #7-9  → env
present(patient = ha_dam)                   // et #10 + #11
dash(
  patient = ha_dam,                         // et #13 + #14
  on = ha_mizbeach,                         // al #15 + #16
  manner = saviv,                           // #17
  located_at = phrase(petach, ohel, mo'ed)  // asher #18 + #19-21
)
```

**Every word appears once in this accounting.**  
**את / על / אשר / ו- / ה-** are present as syntax/morph, not deleted as “unimportant.”

---

## 7. Template columns (reuse on any verse)

| Column | Meaning |
|--------|---------|
| # | Word index 0…n-1 |
| path | Tree address |
| mark | Cantillation id |
| he / translit / en | Never bare Hebrew |
| morph + parts | OSHB form; prefix letters listed |
| role | Controlled vocabulary |
| does | One-line function |
| feeds | Step id or SYM_* or “syntax only” |
| confidence | tested / hypothesis |

---

## Changelog

- 2026-07-25: Gold Lev 1:5 full 22-word coverage + morph letter jobs + glue pattern cards.
