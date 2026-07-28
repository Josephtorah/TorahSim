# Glue & morph pattern scan — sanctuary spine V1 (+ controls)

**Date:** 2026-07-25  
**Kind:** pattern discovery — experimental, **not** binding law  
**Corpus:** V1 spine verses (~Exod install, Lev 1:1–9, Num 9:15–23, 10:11–13, Deut 12:5–14) + Gen 1:1, 1:3, Exod 20:2  
**Tokens:** ~628 word tokens  
**Gold example:** `GOLD_lev_1_5_full_word_coverage_2026-07-25.md`

**Goal:** Find jobs of glue/morph we under-specified earlier, without treating them as noise.

---

## 0. Policy (precision)

| Principle | Practice |
|-----------|----------|
| Nothing out of place | Every word gets a role; prefixes with jobs are named |
| Glue is real | את / על / אל / מן / אשר / כי / אם … are syntax ops |
| Morph letters can matter | ו- sequence, ה- definite, מ- from, ל- to/for, ב- in |
| Not every letter is an opcode | Content consonants usually **spell** the free name |

---

## 1. Patterns we already knew (confirmed)

| Pattern | Shape | Job |
|---------|-------|-----|
| **A** | `verb + את + definite NP` | Mark definite object |
| **B** | `על + place/fire/head` | Spatial “on” |
| **C** | `אל + place/person` | Goal “to” |
| **D** | `מן + type` | Source “from” (cattle/flock) |
| **E** | Construct chain (no particle) | בן הבקר, פתח אהל מועד |

---

## 2. Patterns sharpened or newly emphasized in this scan

### 2.1 **את** repeatedly on the **same** substance under **new verbs**

Seen in **Lev 1:5**: three **את** — objects `בן`, `הדם`, `הדם`.

| Insight | Precision |
|---------|-----------|
| Second/third **את** are not waste | Each verb frame (**הקריבו**, **זרקו**) re-licenses its object |
| Code analogy | New call site → re-state argument binding |

**Pattern F — re-object marking**

```text
V1 + et + NP
V2 + et + same_NP   // NP still needs et under V2
```

---

### 2.2 **Multiple את** listing **parallel objects** (inventory apply)

**Lev 1:8:** את הנתחים, את הראש, ואת הפדר  
**Exod 25:9:** את תבנית המשכן ואת תבנית כל כליו  
**Exod 28:1 / 29:4:** את אהרן ואת בניו  
**Gen 1:1:** את השמים ואת הארץ  

**Pattern G — parallel object list**

```text
verb + et + NP1 + (ve-)et + NP2 + …
```

Job: **enumerate definite patients** of one action (or one creation act).  
Related dual-track: BR *et* as include/fence on domain heads (Gen 1:1) — Oral, named separately.

---

### 2.3 **על פי** — authority channel (not spatial “on”)

**Num 9:18, 20, 23** etc.: עַל פִּי יְהוָה / *al pi YHWH* / “by the mouth of YHWH”

In the scan, **על** often followed by **פי** (5× in spine slice).

| Spatial על | Authority על |
|------------|----------------|
| על המזבח / על האש / על המשכן | על פי יהוה |

**Pattern H — complex prep *al pi***

```text
al + pi + YHWH  →  authority wrapper for camp/journey
```

Must not merge with “blood on altar.” Same letter sequence **על**, different construction.

---

### 2.4 **לפני** — complex relator (before / in presence of)

Morph often **l/6440** = ל + פנים (“to the face of”).

| Use | Example |
|-----|---------|
| Before YHWH | Lev 1:3, 1:5; Exod 27:21; Deut 12:7 |
| Before entrance | Exod 40:6 לפני פתח … |

**Pattern I — *lifnei* X**

```text
lifnei + YHWH     →  presence relation
lifnei + petach   →  spatial “in front of” entrance
```

Account as **relator_complex**, not free name and not “just ל”.

---

### 2.5 **מעל** — “from upon” (lift-off surface)

**Num 9:17** מעל האהל · **Num 10:11** מעל משכן  

Morph HR/R · lemma m/5921 area.

**Pattern J — *me-al* source surface**

```text
lift(cloud, me-al = tent|mishkan) → journey trigger
```

Different from **מן** “from type” (מן הבקר).  
Critical for cloud FSM precision.

---

### 2.6 **אשר** — relative / scene binder (many jobs)

23× in scan. Follow-ons include: **על**, **יבחר**, **ישכן**, **אועד**, **אני**…

| Sub-pattern | Example | Job |
|-------------|---------|-----|
| **J1** locator | אשר פתח אהל מועד (Lev 1:5) | Attach clause to place of altar |
| **J2** stack “which is on” | אשר על האש אשר על המזבח (Lev 1:8) | Nested location stack wood←fire←altar |
| **J3** choice clause | אשר יבחר יהוה (Deut 12) | Build *makom yivchar* free-name span |
| **J4** dwell clause | אשר ישכן שם הענן (Num 9:17) | Define camp place by cloud |
| **J5** function clause | אשר אועד … לדבר (Exod 29:42) | Bind meet/speak function to entrance |
| **J6** shown pattern | אשר אני מראה (Exod 25:9) | Relative “that I show you” |

**Pattern K — *asher* as clause glue** (not one job only — **disambiguate by following verb/prep**).

---

### 2.7 **כי / אם** — logic openers

| Form | Example | Job |
|------|---------|-----|
| **אם** | Lev 1:3 אם עלה | Case IF (olah path) |
| **כי** | Lev 1:2 כי יקריב | When/if person brings |
| **כי אם** | Deut 12:5, 12:14 | “But rather / only” redirect to chosen place |
| **כי** | Exod 40:35 כי שכן | Because (reason cloud blocks entry) |

**Pattern L — casuistic / causal particles**  
These are **control-flow glue**, first-class for code-like IF/WHEN/BECAUSE.

---

### 2.8 **Definite ה-** (morph *ha-* / Td / d/)

~68 tokens with definite marking in the slice.

**Pattern M — *ha-* marks resolve-able definite object**  
Free names at use often appear as **המזבח**, **הדם**, **הכהנים** — the article is part of precise surface, not junk.

---

### 2.9 **Vav on verbs** (ו- + verb)

Very common (slash part **ו** ~95× as first segment in multi-part tokens).

**Pattern N — narrative/procedure sequence**  
ושחט … והקריבו … וזרקו = ordered pipeline steps.

---

### 2.10 **מתוך** — “from among”

**Exod 28:1** מתוך בני ישראל / *mi-tokh benei Yisrael* / from among the children of Israel.

**Pattern O — source set for appointment**  
Priests taken **from among** Israel — morph/source glue, not the free name itself.

---

## 3. Frequency snapshot (spine-ish slice)

| Standalone glue | Approx count | Typical next |
|-----------------|-------------:|--------------|
| אשר | 23 | על / יבחר / ישכן … |
| את | 23 | mishkan, blood, persons, patterns… |
| על | 18 | המשכן / פי / המזבח / האש |
| ואת | 8 | parallel objects |
| אל | 7 | פתח / person / המקום |
| כי | 6 | אם / verbs |
| מן | 3+ | הבקר / הבהמה |

| Prefix-ish slash heads | Count (approx) |
|------------------------|---------------:|
| ו | 95 |
| ה | 67 |
| ל | 34 |
| ב | 23 |
| מ | 15 |

---

## 4. Catalog of glue/morph roles (working vocabulary)

Use these role ids in gold tables:

| Role id | Hebrew examples | Code-like meaning |
|---------|-----------------|-------------------|
| `glue_object_marker` | את | definite object of verb |
| `glue_spatial_on` | על | on/upon (check *al pi* first!) |
| `glue_spatial_to` | אל | to/toward |
| `glue_source_from` | מן | from (type/set) |
| `glue_relative` | אשר | relative/scene binder |
| `glue_logic_if` | אם | IF case |
| `glue_logic_when` | כי | when/that/because (sense by context) |
| `glue_logic_but_only` | כי אם | redirect / exclusive |
| `relator_before` | לפני | before / in presence of |
| `relator_from_upon` | מעל | from upon (lift surface) |
| `relator_from_among` | מתוך | from among |
| `morph_vav_seq` | ו- on verbs | sequence and- |
| `morph_ha_def` | ה- | definite “the” |
| `morph_prep_prefix` | ב-/ל-/מ-/כ- fused | in/to/from/as |
| `auth_al_pi` | על פי | by command of |
| `adverb_around` | סביב | manner around |
| `content_*` | nouns/verbs | free names, acts, types… |

---

## 5. What this changes for “generating code”

| Before (rough) | After (precise) |
|----------------|-----------------|
| Skip “small words” | Emit syntax nodes for את/על/אשר/אם… |
| Treat all על as spatial | Branch: spatial vs **על פי** authority |
| One את per verse | Allow **re-mark** and **parallel lists** |
| Only multi-leaf free names | Also morph: מאהל = from + tent |
| Cloud “from tent” vague | **מעל** = from-upon surface |

---

## 6. Suggested next precision work

1. Apply gold template to **Num 9:17** (lift/camp + מעל + אשר).  
2. Apply to **Deut 12:5** (כי אם + אשר יבחר).  
3. Optional: role tagger that only labels glue/morph (not full free-name AI).  

---

## Changelog

- 2026-07-25: Glue/morph scan on sanctuary spine; patterns F–O; role vocabulary; pairs with Lev 1:5 gold.
