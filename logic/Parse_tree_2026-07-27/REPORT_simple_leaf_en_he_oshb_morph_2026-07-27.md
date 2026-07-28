# Report: Simple leaf line (English · Hebrew) + OSHB morphology

**Date:** 2026-07-27  
**Folder:** `logic/Parse_tree_2026-07-27/` (ta’amim parse track)  
**Status:** experiment report; **format promoted** → **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`** (ACTIVE chat display)  
**Kind:** reading format + morph attach · **not** binding religious law  

---

## 1. Purpose

Find an **easy-to-read** way to show ta’amim **leaves** for an English-first owner:

1. Plain English chunk per leaf  
2. Matching **Hebrew** for that leaf  
3. **OSHB morphology** on **each word** inside multi-word leaves  

This is **not** the D3 pyramid UI. It is a **linear / paren** format that stays readable in markdown and chat.

---

## 2. Display format (working draft)

### 2.1 One-line leaf string

```text
en+he:
  (english phrase · עברית) (next · עברית) …
  ‖   ← optional: main mid-verse break (etnachta)
```

### 2.2 Expanded leaf (morphology)

Under each leaf:

```text
Bn  (english · Hebrew)
    leaf ends with: <cantillation mark>  ·  word indices […]
    · [i] glue | HEAD
         Hebrew: …
         cantillation: …
         OSHB lemma: …  →  English sense of lemma
         OSHB morph:  …  →  English sense of grammar
```

| Term | Meaning |
|------|---------|
| **Leaf / brick** | Ta’amim glue unit (our v3 tree) |
| **glue word** | Non-final word in the leaf (usually conjunctive / bound) |
| **HEAD** | Word that carries the leaf’s ending disjunctive |
| **‖** | Top-level mid-verse cut (typically **etnachta**) |
| **OSHB morph** | Word-level grammar from morphhb/OSHB XML |
| **en** | Free English aid only — not derivation source |

### 2.3 Rules of the format

| Do | Don’t |
|----|--------|
| English first for every leaf | Bare Hebrew with no English |
| Hebrew paired to that leaf | Merge two words’ morph into one fake “leaf morph” |
| Morph **per word** inside the leaf | Treat OSHB as tree authority |
| Mark provenance: structure = ta’amim; morph = OSHB | Silent merge of Oral / English into Written |

**Two layers stay distinct:**

```text
ta’amim  →  which words share a leaf
OSHB     →  lemma + morph of each word in that leaf
```

---

## 3. Data sources

| Layer | Source |
|-------|--------|
| Tree / leaves | `taamim_tree_parse.py` · rule set **v3** · pure binary + glue |
| Hebrew surface | Same OSHB/morphhb verse words as parser |
| Morphology | OSHB `@lemma` + `@morph` on each `<w>` |
| English leaf glosses | Free [EN-AID] for display (owner English-only) |

Alignment check on demo verses: **word count parser == OSHB word count**.

---

## 4. Worked examples

### 4.1 Leviticus 1:2

**Full English (flow):**  
Speak to the children of Israel and say to them: a person, when he brings from among you an offering to the LORD—from the livestock, from the herd and from the flock—you shall bring your offering.

**en+he:**

```text
(speak! · דבר)
(to the children of Israel · אל בני ישראל)
(and say to them · ו/אמרת אל/הם)
(a person · אדם)
(when he brings, from among you · כי יקריב מ/כם)
(an offering · קרבן)
(to the LORD · ל/יהוה)
‖
(from the livestock · מן ה/בהמה)
(from the herd · מן ה/בקר)
(and from the flock · ו/מן ה/צאן)
(you shall bring · תקריבו)
(your offering · את קרבנ/כם)
```

**12 leaves · 21 words**

#### B0 — `(speak! · דבר)`  
Ends: **gershayim** · words [0]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| HEAD | speak! | דבר | verb — command “speak” (you ms) |

#### B1 — `(to the children of Israel · אל בני ישראל)`  
Ends: **pashta** · words [1–3]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | to | אל | preposition |
| glue | children of | בני | noun “sons/children,” construct |
| HEAD | Israel | ישראל | proper name |

#### B2 — `(and say to them · ו/אמרת אל/הם)`  
Ends: **zaqef qatan** · words [4–5]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | and you shall say | ו/אמרת | **and** + verb “say” (you ms) |
| HEAD | to them | אל/הם | preposition + **them** |

#### B3 — `(a person · אדם)`  
Ends: **revia** · words [6]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| HEAD | a person / human | אדם | noun, masculine singular |

#### B4 — `(when he brings, from among you · כי יקריב מ/כם)`  
Ends: **tevir** · words [7–9]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | when / if | כי | conjunction-like particle |
| glue | he brings near | יקריב | verb “offer/bring near” (he) |
| HEAD | from among you | מ/כם | preposition + **you (plural)** |

#### B5 — `(an offering · קרבן)`  
Ends: **tifcha** · words [10]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| HEAD | offering | קרבן | noun, masculine singular |

#### B6 — `(to the LORD · ל/יהוה)`  
Ends: **etnachta** (main mid-verse) · words [11]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| HEAD | to the LORD | ל/יהוה | preposition + divine name |

#### B7 — `(from the livestock · מן ה/בהמה)`  
Ends: **revia** · words [12–13]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | from | מן | preposition |
| HEAD | the livestock / animal | ה/בהמה | **the** + feminine noun |

#### B8 — `(from the herd · מן ה/בקר)`  
Ends: **pashta** · words [14–15]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | from | מן | preposition |
| HEAD | the herd / cattle | ה/בקר | **the** + noun |

#### B9 — `(and from the flock · ו/מן ה/צאן)`  
Ends: **zaqef qatan** · words [16–17]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | and from | ו/מן | **and** + preposition |
| HEAD | the flock | ה/צאן | **the** + noun |

#### B10 — `(you shall bring · תקריבו)`  
Ends: **tifcha** · words [18]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| HEAD | you (pl.) shall bring near | תקריבו | verb “offer,” you plural |

#### B11 — `(your offering · את קרבנ/כם)`  
Ends: **silluq** · words [19–20]

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | **(object marker)** *et* | את | **object marker** (H853 / `HTo`) |
| HEAD | your offering | קרבנ/כם | noun “offering” + **your (plural)** |

**Note on *et*:** OSHB tags **את** as object marker (`HTo`), including when it is the **glue** half of a multi-word leaf (B11). Morphology is **per word**, not one blob for the whole leaf.

---

### 4.2 Genesis 1:3

**en+he:**

```text
(and God said · ו/יאמר אלהים)
(let there be light · יהי אור)
‖
(and there was light · ו/יהי אור)
```

#### B0 — `(and God said · ו/יאמר אלהים)` · end **tifcha**

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | and he said | ו/יאמר | **and** + verb “say” (narrative past) |
| HEAD | God | אלהים | noun (Elohim H430) |

#### B1 — `(let there be light · יהי אור)` · end **etnachta**

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | let there be | יהי | verb “be” |
| HEAD | light | אור | noun **light** (H216) |

#### B2 — `(and there was light · ו/יהי אור)` · end **silluq**

| Role | English | Hebrew | Morph (English aid) |
|------|---------|--------|---------------------|
| glue | and there was | ו/יהי | **and** + verb “be” |
| HEAD | light | אור | noun **light** (H216) |

---

### 4.3 Genesis 1:1

**en+he:**

```text
(in the beginning · ב/ראשית)
(God created · ברא אלהים)
‖
(the heavens · את ה/שמים)
(and the earth · ו/את ה/ארץ)
```

#### B0 — `(in the beginning · ב/ראשית)` · end **tifcha**

| Role | English | Morph (English aid) |
|------|---------|---------------------|
| HEAD | in the beginning | preposition **in** + noun **beginning** |

#### B1 — `(God created · ברא אלהים)` · end **etnachta**

| Role | English | Morph (English aid) |
|------|---------|---------------------|
| glue | created | verb “create” |
| HEAD | God | noun Elohim |

#### B2 — `(the heavens · את ה/שמים)` · end **tifcha**

| Role | English | Morph (English aid) |
|------|---------|---------------------|
| glue | **object marker** *et* | object marker H853 / `HTo` |
| HEAD | the heavens | **the** + heavens |

#### B3 — `(and the earth · ו/את ה/ארץ)` · end **silluq**

| Role | English | Morph (English aid) |
|------|---------|---------------------|
| glue | **and + object marker** | **and** + *et* (`HC/To`) |
| HEAD | the earth | **the** + earth |

---

## 5. Findings (experiment)

| Finding | Result |
|---------|--------|
| Simple `(en · he)` line is readable for English-first owner | **Yes** (owner preference) |
| Multi-word leaves need morph **per word** | **Yes** — do not merge morphs |
| OSHB morphs **את** / **ו/את** | **Yes** — `HTo`, `HC/To` |
| Align parse words ↔ OSHB words on demos | **Matched** (Lev 1:2, Gen 1:1, 1:3) |
| D3 pyramid / CSS art | **Out of scope** for this report; separate track under `web/taamim_tree/` |

---

## 6. Open choices (not locked)

1. Add **transliteration** as third field: `(en · he · translit)`?  
2. Hide raw morph **codes** and keep English morph only?  
3. Promote this format into `logic/TREE_DISPLAY.md` as a **chat default** vs keep experiment-only?  
4. Export this shape to JSON for the future D3 webapp (leaf cards + expand morph)?  

---

## 7. Related paths

| Path | Role |
|------|------|
| `taamim_tree_parse.py` | Versioned ta’amim trees (CURRENT=v3) |
| `logic/TREE_DISPLAY.md` | Display decision notes (chat tree model) |
| `web/taamim_tree/` | D3 webapp seed (separate from this format) |
| morphhb / OSHB Gen·Lev XML | `@lemma` / `@morph` on `<w>` |
| `logic/TREE_INTERPRETATION_RULES.md` | TIR (e.g. object marker as role) |

---

## 8. Reproduce (for agents)

```bash
# structure only
python3 taamim_tree_parse.py Lev.1.2 --tree --leaves

# morph lives on OSHB <w lemma morph> in Data/Lev.xml or MORPHHB_WLC
# join by word index 0..n-1 with parse result words
```

---

## 9. Confidence labels

| Claim | Label |
|-------|--------|
| Format useful for English-first reading of leaves | **hypothesis** (owner liked; iterate) |
| Per-word OSHB attach under glue leaves | **tested** on Lev 1:2, Gen 1:1, 1:3 |
| Ready as sole permanent display for all of Tanakh | **no** — still experiment |

**Last updated:** 2026-07-27  
