# Tree display format: leaf line (English · Hebrew) + OSHB morph

**Status:** **ACTIVE display format** (owner liked 2026-07-27) — use when showing a ta’amim tree in chat/reports  
**Companion permanent notes:** `logic/TREE_DISPLAY.md` (layout history); this file = **preferred readable format**  
**Standing:** `reviews/STANDING_DECISIONS.md` §6 · `Agents.md`  
**Kind:** display contract · not binding religious law  

On substantive change: update this file, Agents, STANDING §6, and the Parse_tree report link.

---

## 1. When to use

| Use this format when… | Prefer something else when… |
|------------------------|-----------------------------|
| Owner wants a **readable tree** in chat/markdown | Debugging raw parser CLI only |
| English-first + Hebrew on every leaf | Machine-only JSON for D3 |
| Showing **OSHB morphology** under leaves | Full canvas pyramid art (optional webapp) |

**Parser still owns structure** (`taamim_tree_parse.py`, CURRENT). This is only **how we print** the tree.

---

## 2. The format (canonical)

### 2.1 Header

```text
### TREE  <Book.Ch.V>  ·  taamim vN  ·  system=prose|poetry
words=N · leaves=M · leaf_complete=yes · pure_binary=yes
```

### 2.2 One-line leaf string (`en+he`)

```text
en+he:
  (english phrase · עברית) (next · עברית) … ‖ (after mid-break · עברית) …
```

| Rule | Detail |
|------|--------|
| One `( … · … )` | = **one leaf/brick** (glue unit from our tree) |
| Left of `·` | **English** free gloss of that leaf [EN-AID] |
| Right of `·` | **Hebrew** plain surface of that leaf (no need for bare Hebrew alone) |
| `‖` | Insert **after the leaf that ends in etnachta** (main mid-verse break), when present |
| Order | Left → right = word order / leaf order in the verse |

**Be consistent on object marker *et*:** if Hebrew has את / ו/את, English should say so, e.g.  
`(et + the heavens · את ה/שמים)` not only `(the heavens · את ה/שמים)` when the marker matters for morph.

### 2.3 Leaves + morphology (required when morph is shown)

For **each** leaf Bn:

```text
Bn  (english · Hebrew)
    end mark: <cantillation id>  ·  word indices [i–j]

    | Word (English) | Role | Morphology (English) |
    |----------------|------|----------------------|
    | …              | glue | …                    |
    | …              | HEAD | …                    |
```

| Column | Meaning |
|--------|---------|
| **Word (English)** | Sense of **that** OSHB word (not the whole leaf only) |
| **Role** | `glue` = non-final in leaf; `HEAD` = carries ending disjunctive |
| **Morphology (English)** | Plain-English reading of OSHB `@morph` (+ lemma when useful) |

**Multi-word leaves:** **one table row per word**. Never one merged morph for the whole leaf.

Optional (advanced / debugging): also show raw `lemma` / `morph` codes in a footnote or second table.

### 2.4 Tiny glossary (print when helpful)

| Term | English |
|------|---------|
| Leaf / brick | Chunk of the verse from the cantillation tree |
| glue | Joined to the HEAD; usually conjunctive / bound |
| HEAD | Word where this leaf’s pause sits |
| Object marker (*et*) | Flags “this is the object,” not usually “with” |
| ‖ | Main mid-verse cut (etnachta) |

---

## 3. Worked example (canonical): Leviticus 1:2

**Verse English (flow):**  
Speak to the children of Israel and say to them: a person, when he brings from among you an offering to the LORD—from the livestock, from the herd and from the flock—you shall bring your offering.

### en+he (one line)

```text
en+he:
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
  (et + your offering · את קרבנ/כם)
```

*(Note: B11 English names **et** so object-marker morphology matches the Hebrew.)*

### Leaves + morphology

**B0** `(speak! · דבר)` · end **gershayim** · [0]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| speak! | HEAD | verb — command “speak” (you, masculine singular) |

**B1** `(to the children of Israel · אל בני ישראל)` · end **pashta** · [1–3]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| to | glue | preposition |
| children of | glue | noun “sons/children,” construct |
| Israel | HEAD | proper name |

**B2** `(and say to them · ו/אמרת אל/הם)` · end **zaqef qatan** · [4–5]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| and you shall say | glue | **and** + verb “say” (you ms) |
| to them | HEAD | preposition + **them** |

**B3** `(a person · אדם)` · end **revia** · [6]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| a person / human | HEAD | noun, masculine singular |

**B4** `(when he brings, from among you · כי יקריב מ/כם)` · end **tevir** · [7–9]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| when / if | glue | conjunction-like particle |
| he brings near | glue | verb “offer/bring near” (he) |
| from among you | HEAD | preposition + **you (plural)** |

**B5** `(an offering · קרבן)` · end **tifcha** · [10]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| offering | HEAD | noun, masculine singular |

**B6** `(to the LORD · ל/יהוה)` · end **etnachta** · [11] · **‖ after this leaf**

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| to the LORD | HEAD | preposition + divine name |

**B7** `(from the livestock · מן ה/בהמה)` · end **revia** · [12–13]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| from | glue | preposition |
| the livestock / animal | HEAD | **the** + feminine noun |

**B8** `(from the herd · מן ה/בקר)` · end **pashta** · [14–15]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| from | glue | preposition |
| the herd / cattle | HEAD | **the** + noun |

**B9** `(and from the flock · ו/מן ה/צאן)` · end **zaqef qatan** · [16–17]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| and from | glue | **and** + preposition |
| the flock | HEAD | **the** + noun |

**B10** `(you shall bring · תקריבו)` · end **tifcha** · [18]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| you (pl.) shall bring near | HEAD | verb “offer,” you plural |

**B11** `(et + your offering · את קרבנ/כם)` · end **silluq** · [19–20]

| Word (English) | Role | Morphology (English) |
|----------------|------|----------------------|
| **et** (object marker) | glue | object marker (marks “offering” as object) |
| your offering | HEAD | noun “offering” + **your (plural)** |

---

## 4. Short second example (Gen 1:1) — *et* consistent both sides

```text
en+he:
  (in the beginning · ב/ראשית)
  (God created · ברא אלהים)
  ‖
  (et + the heavens · את ה/שמים)
  (and et + the earth · ו/את ה/ארץ)
```

**B2** and **B3** both show object-marker morphology (את / ו/את). Do not label only one side with *et*.

---

## 5. Provenance

| Field | Source |
|-------|--------|
| Leaf boundaries | Our ta’amim parser (CURRENT), not OSHB `n=` |
| Hebrew in parens | Same verse words as parser |
| Morphology | OSHB `@lemma` / `@morph` per word |
| English | Free gloss [EN-AID]; owner is English-first |

---

## 6. Related

| Path | Role |
|------|------|
| `logic/Parse_tree_2026-07-27/REPORT_simple_leaf_en_he_oshb_morph_2026-07-27.md` | Longer experiment report |
| `logic/TREE_DISPLAY.md` | Other display history / constraints |
| `web/taamim_tree/` | D3 webapp (optional; not this format) |
| `taamim_tree_parse.py` | Structure only |

---

## 7. Confidence

| Claim | Label |
|-------|--------|
| Owner prefers this format for chat tree display | **established** (2026-07-27) |
| Per-word OSHB under multi-word leaves | **tested** (Lev 1:2, Gen demos) |
| Sole permanent format for every context | **no** — primary for **readable tree display**; CLI `--tree` remains for debug |

**Do not re-quiz the owner on this format** unless they ask to change it.
