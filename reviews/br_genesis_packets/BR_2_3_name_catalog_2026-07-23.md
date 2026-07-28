# Catalog: BR 2:3 people-map and “this is…” references across Bereshit Rabbah

**Date:** 2026-07-23  
**Related packet:** `BR_2_3_generations.md`  
**Hub:** `../BR_Genesis_Interface_2026-07-23.md`  
**Source scan:** `Data/bereshit_rabbah_he.json`  
**Kind:** research catalog · dual-track · not binding law  

**Language:** Hebrew terms with how-to-say-it + plain English.

---

## 0. What this file is

BR 2:3 maps Genesis 1:2–5 phrases onto **people and generations** with **זה** / *zeh* / “**this is** …”.

This catalog answers:

1. What is that local map?  
2. Does each name get **multiple** “this is…” links later in BR?  
3. Is the 2:3 table used later as a permanent keyring?

---

## 1. Method

- Scan whole Bereshit Rabbah for **זה** + name (or “this is the generation of…”).  
- Counts = section hits in our dump (approximate; regex-based).  
- “Multiple references” means **many independent verse-hooks**, not one key reused by citation.

---

## 2. The BR 2:3 bindings (local map)

| Written phrase (English) | Hebrew hook (approx.) | Link | Points to |
|--------------------------|----------------------|------|-----------|
| Earth was formless waste | *tohu* / TOH-hoo | this is… | **Adam** the first human |
| And void | *vohu* / VOH-hoo | this is… | **Cain** |
| Darkness | *choshekh* / KHO-shekh | this is… | **Generation of Enosh** |
| On the face of the deep | *tehom* / te-HOM | this is… | **Generation of the Flood** |
| Spirit of God on the waters | *ruach Elohim…* | linked to Gen 8:1 | Wind/spirit after the Flood |
| “Let there be light” | *yehi or* / ye-HEE or | this is… | **Abraham** |
| Light called Day | — | this is… | **Jacob** |
| Darkness called Night | — | this is… | **Esau** |
| Evening / morning | — | this is… | Esau / Jacob again |
| “One day” | — | optional | Lord’s day / **Yom Kippur** (Day of Atonement) |

This is **one teaching session**, not the only BR read of Genesis 1:2 (see 2:1 phrase-echo, 2:2 upper/lower complaint).

---

## 3. Summary: multiple references?

| Name | ~“This is…” hits in BR | Multiple? | Notes |
|------|------------------------:|-----------|--------|
| **Abraham** | ~35 | **Yes, many** | Most common person-ID |
| **Jacob** | ~22–23 | **Yes, many** | Often vs Esau / righteous lines |
| **Esau** | ~20–22 | **Yes, many** | Often wicked / enemy / chiefs |
| **Adam** | ~6 | **Yes, few** | Different hooks each time |
| **Cain** | ~3 | **Barely** | 2:3 + ~two others |
| **Enosh’s generation** | ~1–2 as full “this is…” | **Almost only 2:3** | Generation named elsewhere without that formula |
| **Flood generation** | “Flood generation” very common; hard “this is…” rarer | **Theme reused a lot** | Narrative, not a hard keyring |

---

## 4. Catalog by name

### 4.1 Abraham / *Avraham* / Abraham

**In 2:3:** “Let there be light” → Abraham (Isaiah 41:2 “from the east,” read as he **lit** / *he’ir*).

**Multiple later “this is Abraham” hooks (examples):**

| Approx. BR locus | Other verse/theme bound to Abraham |
|------------------|-------------------------------------|
| Many sections (~35 total) | Fear of God / fearers of the Lord |
| | Friend / pure heart / lover of God |
| | “One was Abraham” (Ezekiel) |
| | Binding of Isaac contexts |
| | Kindness of Abraham (Micah) |
| | Song of Songs “my dove” readings |
| | Great among the Anakim (Joshua midrash) |

**Design:** multi-verse **sink** — many keys → same person.  
**Not:** later BR saying “lookup Gen 1 light key.”

---

### 4.2 Jacob / *Yaakov* / Jacob

**In 2:3:** light called Day → Jacob; morning → Jacob.

**Multiple later hooks (examples):**

| Theme bound to Jacob |
|----------------------|
| Listens to parents’ counsel |
| Righteous goes out from trouble (leaves Beersheba) |
| Walks securely / sleeps without fear (vs Esau, Laban) |
| Chosen of the Lord |
| “Truth to Jacob” (Micah) |
| Wise heart to the right (vs Esau left) |
| Blessings on the head of the righteous |

---

### 4.3 Esau / *Esav* / Esau

**In 2:3:** darkness = Night → Esau; evening → Esau.

**Multiple later hooks (examples):**

| Theme bound to Esau |
|---------------------|
| Wicked / boundary of wickedness |
| Enemy; “Esau and his chiefs” |
| Fool’s heart to the left (wives before sons) |
| Mouth of the wicked covers violence |
| Troubles of the righteous = Esau’s line |

---

### 4.4 Adam / *Adam ha-rishon* / Adam the first human

**In 2:3:** *tohu* → Adam (“for what / as nothing”).

**Other “this is Adam” loci (~6 sections), examples:**

| BR (approx.) | Hook |
|--------------|------|
| 2:3 | *tohu* / formless waste |
| 9:12 | “very good” (Gen 1:31) → Adam |
| 14:1 | Dough-offering / world’s “dough” |
| 21:1–2 | Half among angels; lazy field (Proverbs) → Adam (Eve as vineyard) |

---

### 4.5 Cain / *Kayin* / Cain

**In 2:3:** *vohu* → Cain (tried to return the world to chaos).

**Other hits (~3 total):**

| BR (approx.) | Hook |
|--------------|------|
| 2:3 | *vohu* / void |
| 22:9 | Psalm: wicked draw sword → Cain (Abel as victim) |
| 32:5 | Cain still “hanging loosely,” Flood washes him away |

**Sparse multi-key person.**

---

### 4.6 Generation of Enosh / *dor Enosh*

**In 2:3:** darkness → Enosh’s generation (deeds in the dark; Isaiah 29:15).

**“This is the generation of Enosh”:** essentially the **2:3** teaching.  
The generation is **mentioned** elsewhere with Flood / Tower rebels, usually **without** reusing the Gen 1 darkness key.

---

### 4.7 Generation of the Flood / *dor ha-mabul*

**In 2:3:** face of the deep → Flood generation (deeps burst, Gen 7:11).

**Later:** dozens of sections discuss the Flood generation (judgment, water, moral failure, contrast with Noah). That is **theme reuse**, not a permanent “deep → Flood” API.

Hard “this is the Flood generation” appears in a few midrash lists (e.g. with Enosh / Tower generations as types of wicked ages).

---

## 5. How links are used (scan conclusion)

### Operator (reused constantly)

```text
verse_phrase + "this is" (zeh) + person + optional proof verse
```

~170 “this is” + major person hits corpus-wide (Abraham highest).

### Specific 2:3 table (not a global registry)

```text
// One session
resolve(Gen_1_2_to_5, mode="generations") -> {
  tohu: Adam, vohu: Cain, darkness: Enosh-gen,
  deep: Flood-gen, light: Abraham,
  day: Jacob, night: Esau, ...
}

// Later sessions
resolve(otherVerse, mode="identify") -> { person: Abraham | Jacob | ... }
// same function, NEW verse keys — not lookup of Gen1 table
```

### What travels later

| Travels | Does not travel as hard key |
|---------|-----------------------------|
| Method: “this = person” | “Light always means Abraham via Gen 1:3” |
| Character types (Abraham~light/righteous; Esau~dark/wicked) | Formal back-ref “as we said in BR 2:3” |

---

## 6. Relation to other BR 2 readings of the same verse

| Packet | Link style |
|--------|------------|
| `BR_2_1_tohu_early` | Same **phrase** early + late (Jeremiah) |
| `BR_2_2_earth_complaint` | Earth as **tier** (upper/lower lots) |
| `BR_2_3_generations` | Phrase → **person/generation** (this catalog) |

---

## 7. Fence

- Catalog is a **scan aid**, not complete every paraphrase of every name.  
- Counts are regex-approximate on the local Hebrew dump.  
- Dual-track only; not binding law.  
- Does not claim BR implements a software registry—only describes midrash linking habits.

---

## 8. Links

- Packet: `BR_2_3_generations.md`  
- Hub: `../BR_Genesis_Interface_2026-07-23.md`  
- Source: `../../Data/bereshit_rabbah_he.json`  
