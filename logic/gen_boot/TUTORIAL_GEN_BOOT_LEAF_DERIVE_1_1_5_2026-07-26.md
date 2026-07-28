# Leaf-level derivation — Genesis 1:1–5 (boot day one)

**Date:** 2026-07-26  
**Method:** **every leaf** of the ta’amim tree → role → near-code op  
**Source trees:** `logic/units/gen_01_creation_boot.yaml` → `binary_trees.verse_trees` (`tree_ascii`, rule_set **v1**)  
**Hebrew source:** `Data/Gen.xml`  
**Kind:** tutorial · hypothesis roles · **not** binding law  
**Folder hub:** [`INDEX.md`](INDEX.md)  

**Supersedes (for day one):** top-split-only IR in [`TUTORIAL_GEN_BOOT_IR_STEPTHROUGH_2026-07-26.md`](TUTORIAL_GEN_BOOT_IR_STEPTHROUGH_2026-07-26.md) § Day 1  

**Novice plain English for the full week 1:1–2:3 (tree leaves → logic, step-through):**  
→ [`TUTORIAL_GEN_BOOT_PLAIN_LEAF_STEPTHROUGH_1_1_2_3_2026-07-26.md`](TUTORIAL_GEN_BOOT_PLAIN_LEAF_STEPTHROUGH_1_1_2_3_2026-07-26.md)  

---

## 0. Why top-split alone is not enough

**Wrong method (previous walkthrough):**

```text
verse → LEFT ‖ RIGHT (etnachta only) → one or two English ops
```

That **throws away**:

- nested phrases (who binds to which verb)  
- dual **את … ואת** object inventory (TIR-015)  
- particle jobs (**כי**, **בין … ובין**)  
- repeated verbs vs one verb  
- which leaf is the **etnachta head** (pivot of a half)

**Required method (this file):**

```text
full tree_ascii
  → list every leaf [i] with he + translit + en
  → assign role + TIR (or OPEN) + which STEP it feeds
  → only then write near-code (ops must cite leaf indices)
```

**Rule:** If a detail is not on a leaf (or an explicit tree node grouping leaves), it is **not derived**.

---

## 0.1 Role legend used below

| Role id | English job |
|---------|-------------|
| `time_header` | When/frame of the act (**בראשית**) |
| `verb_create` | Create verb (**ברא**) |
| `agent` | Who acts (**אלהים**) |
| `glue_object_marker` | **את** / **ואת** — binds verb → definite patient (TIR-014) |
| `domain_object` | Patient domain (**השמים**, **הארץ**) |
| `set_include_list` | Parallel *et…ve-et* inventory (TIR-015) |
| `subject_state` | Subject of a state clause (**הארץ**) |
| `verb_be` | **היה** “was” |
| `state_predicate` | Quality of subject (**תהו**, **בהו**) |
| `locative_prep` | **על** “on/over” |
| `face_construct` | **פני** “face of” (construct) |
| `depth_object` | **תהום** deep |
| `agent_spirit` | **רוח** spirit (as actor-side) |
| `verb_hover` | **מרחפת** hovering |
| `medium_object` | **המים** waters |
| `verb_speech` | **אמר** said |
| `jussive_be` | **יהי** let-there-be |
| `result_be` | **ויהי** and-there-was |
| `payload_light` | **אור** light |
| `verb_see` | **ראה** saw |
| `eval_particle` | **כי** that/because (here: content of seeing) |
| `eval_grade` | **טוב** good |
| `verb_separate` | **הבדיל** divided |
| `between_a` / `between_b` | **בין X** / **ובין Y** pair structure |
| `verb_name` | **קרא** called |
| `name_target` | Thing named (**לאור**, **לחשך**) |
| `name_label` | New name (**יום**, **לילה**) |
| `clock_part` | **ערב** / **בקר** evening/morning |
| `day_unit` | **יום** as day-count word |
| `day_ordinal` | **אחד** one |

Every Hebrew leaf is written as: **he** / *translit* / "English".

---

# Genesis 1:1 — leaf derive CREATE with dual domains

## A. Full tree (show work)

```text
PHRASE (binary 7w)
├── PHRASE (binary 3w)                    ← LEFT of etnachta (agent-create frame)
│   ├── [0] בְּרֵאשִׁית  (tifcha, rank=2)
│   └── PHRASE (binary 2w)
│       ├── [1] בָּרָא      (munach, rank=9)   ← conjunct: binds to agent
│       └── [2] אֱלֹהִים    (etnachta, rank=1) ← LEFT pivot / agent
└── PHRASE (binary 4w)                    ← RIGHT of etnachta (object inventory)
    ├── PHRASE (binary 2w)
    │   ├── [3] אֵת         (mercha, rank=9)
    │   └── [4] הַשָּׁמַיִם  (tifcha, rank=2)
    └── PHRASE (binary 2w)
        ├── [5] וְאֵת       (mercha, rank=9)
        └── [6] הָאָרֶץ     (silluq, rank=1)   ← verse end
```

**Tree fact:** The top split is **not** “create ‖ heavens+earth” as two vague blobs.  
LEFT nests **time + (create+agent)**; RIGHT nests **two marked objects** in parallel.

## B. Leaf table (100% of 7 words)

| i | he | translit | en | mark | role | TIR | feeds |
|---|-----|----------|-----|------|------|-----|-------|
| 0 | בְּרֵאשִׁית | *be-reshit* | “in beginning” | tifcha | `time_header` | OPEN (boot frame) | STEP_1a |
| 1 | בָּרָא | *bara* | “created” | munach | `verb_create` | — | STEP_1a |
| 2 | אֱלֹהִים | *Elohim* | “God” | **etnachta** | `agent` | — | STEP_1a |
| 3 | אֵת | *et* | object marker | mercha | `glue_object_marker` | **TIR-014** | STEP_1b |
| 4 | הַשָּׁמַיִם | *ha-shamayim* | “the heavens” | tifcha | `domain_object` | TIR-014 payload | STEP_1b |
| 5 | וְאֵת | *ve-et* | “and *et*” | mercha | `glue_object_marker` + list join | **TIR-015** | STEP_1b |
| 6 | הָאָרֶץ | *ha-arets* | “the earth” | silluq | `domain_object` | TIR-015 | STEP_1b |

**Accounted: 7/7.**

## C. How nesting forces the logic (not English guess)

1. Leaves **[1]–[2]** form a 2-word phrase: munach **ברא** attaches to etnachta **אלהים**  
   → **agent is Elohim; verb is bara** (not “beginning created”).  
2. Leaf **[0]** is sibling of that phrase under the 3w LEFT  
   → **time_header scopes the create event**, not an object.  
3. RIGHT is **two parallel (et + NP)** pairs  
   → **set_include_list** of **two domains**, not one compound object without structure.  
4. Without leaves **[3] and [5]**, you lose TIR-014/015 and might invent a single vague “created everything.”

## D. Near-code derived **from leaves only**

```text
// STEP_1a  feeds: leaves 0,1,2
AT time = leaf[0] be-reshit
AGENT    = leaf[2] Elohim
VERB     = leaf[1] bara

// STEP_1b  feeds: leaves 3–6  (TIR-015 inventory under VERB of 1a)
OBJECTS = set_include_list(
  et(leaf[3]) → domain leaf[4] ha-shamayim,
  ve-et(leaf[5]) → domain leaf[6] ha-arets
)

CREATE(
  agent = Elohim,           // [2]
  verb  = bara,             // [1]
  when  = be-reshit,        // [0]
  objects = {shamayim, erets}  // [4],[6] via [3],[5]
)
```

## E. What top-split alone missed

| Detail | Leaf? | Top-split-only IR? |
|--------|-------|---------------------|
| Dual *et…ve-et* inventory | [3][5] | Often collapsed to “heavens and earth” without marker jobs |
| Agent pivot = etnachta on **אלהים** not on verb | [2] | Hidden |
| **ברא** conjunct under agent | [1] | Hidden |
| Time is own leaf, not part of object list | [0] | Sometimes smeared into “in the beginning create…” |

## F. State after 1:1

```text
agent = Elohim
when_frame = be-reshit
domains = { shamayim: installed, erets: installed }
// light NOT present — no leaf says light
```

---

# Genesis 1:2 — leaf derive substrate + spirit medium

## A. Full tree (compressed ASCII from unit)

```text
PHRASE (14w)  pure_binary: false  (has 3-ary nodes)
├── LEFT 8w (through etnachta on תהום)
│   ├── 4w: earth + was + tohu + vohu
│   │   ├── [0] וְהָאָרֶץ (revia)
│   │   └── 3w: [1] הָיְתָה — [2] תֹהוּ — [3] וָבֹהוּ
│   └── 4w: dark + on face of deep
│       ├── [4] וְחֹשֶׁךְ (tifcha)
│       └── 3-ary: [5] עַל [6] פְּנֵי [7] תְהוֹם (etnachta)
└── RIGHT 6w
    ├── 2w: [8] וְרוּחַ [9] אֱלֹהִים (zaqef)
    └── 4w: [10] מְרַחֶפֶת + 3-ary [11] עַל [12] פְּנֵי [13] הַמָּיִם (silluq)
```

## B. Leaf table (14/14)

| i | he | translit | en | role | feeds |
|---|-----|----------|-----|------|-------|
| 0 | וְהָאָרֶץ | *ve-ha-arets* | “and the earth” | `subject_state` | STEP_2a |
| 1 | הָיְתָה | *hayetah* | “was” | `verb_be` | STEP_2a |
| 2 | תֹהוּ | *tohu* | “formless waste” | `state_predicate` | STEP_2a |
| 3 | וָבֹהוּ | *va-vohu* | “and void” | `state_predicate` (pair with 2) | STEP_2a |
| 4 | וְחֹשֶׁךְ | *ve-choshekh* | “and darkness” | `state_predicate` / dark layer | STEP_2b |
| 5 | עַל | *al* | “on” | `locative_prep` | STEP_2b |
| 6 | פְּנֵי | *penei* | “face of” | `face_construct` | STEP_2b |
| 7 | תְהוֹם | *tehom* | “deep” | `depth_object` (**etnachta head**) | STEP_2b |
| 8 | וְרוּחַ | *ve-ruach* | “and spirit” | `agent_spirit` | STEP_2c |
| 9 | אֱלֹהִים | *Elohim* | “of God” | `agent` (construct with 8) | STEP_2c |
| 10 | מְרַחֶפֶת | *merachefet* | “hovering” | `verb_hover` | STEP_2c |
| 11 | עַל | *al* | “on” | `locative_prep` | STEP_2c |
| 12 | פְּנֵי | *penei* | “face of” | `face_construct` | STEP_2c |
| 13 | הַמָּיִם | *ha-mayim* | “the waters” | `medium_object` | STEP_2c |

## C. Nested groups → separate STEPs (must not mash)

Tree gives **three logic clusters**, not one “chaos” mush:

```text
STEP_2a  leaves [0–3]   // 4w phrase under revia
  SUBJECT erets [0]
  BE hayetah [1]
  PREDICATES {tohu [2], vohu [3]}   // zaqef closes the pair

STEP_2b  leaves [4–7]   // dark on face of deep; etnachta on tehom
  LAYER choshekh [4]
  LOCATIVE al [5] + penei [6] + tehom [7]

STEP_2c  leaves [8–13]  // RIGHT of etnachta
  SPIRIT_AGENT ruach[8] of Elohim[9]
  HOVER merachefet [10]
  LOCATIVE al [11] + penei [12] + mayim [13]
```

## D. Near-code (leaf-cited)

```text
SET_STATE_EARTH(
  subject = erets,              // [0]
  be = hayetah,                 // [1]
  predicates = {tohu, vohu}     // [2][3]
)
SET_DARK_ON_DEEP(
  dark = choshekh,              // [4]
  on_face_of = tehom            // [5][6][7]
)
SET_SPIRIT_OVER_WATERS(
  spirit = ruach_Elohim,        // [8][9]
  hover = merachefet,           // [10]
  on_face_of = mayim            // [11][12][13]
)
```

## E. Details lost without leaves

| Lost if only top L‖R | Leaves that carry it |
|----------------------|----------------------|
| *tohu* and *vohu* are a **pair under one be-verb** | [1][2][3] nesting |
| Dark is **on the deep’s face**, not “dark exists abstractly” | [5][6][7] 3-ary |
| Spirit is **of Elohim**, not free-floating “spirit” | [8][9] 2w |
| Hover targets **waters’ face**, parallel structure to deep’s face | [11–13] vs [5–7] |
| 3-ary nodes (not pure binary) | pure_binary: false |

## F. State after 1:2

```text
erets.state = {tohu, vohu}
dark_on = tehom.face
spirit_Elohim.hover_on = mayim.face
// still no light leaf
```

---

# Genesis 1:3 — leaf derive SPEECH → RESULT (same payload twice)

## A. Full tree

```text
PHRASE (6w)
├── LEFT 4w (etnachta on אור)
│   ├── 2w speech frame: [0] וַיֹּאמֶר [1] אֱלֹהִים
│   └── 2w wish:        [2] יְהִי [3] א֑וֹר   ← etnachta on light
└── RIGHT 2w
    ├── [4] וַיְהִי
    └── [5] אֽוֹר   ← silluq on light again
```

## B. Leaf table (6/6)

| i | he | translit | en | role | feeds |
|---|-----|----------|-----|------|-------|
| 0 | וַיֹּאמֶר | *va-yomer* | “and he said” | `verb_speech` | STEP_3a |
| 1 | אֱלֹהִים | *Elohim* | “God” | `agent` | STEP_3a |
| 2 | יְהִי | *yehi* | “let there be” | `jussive_be` | STEP_3b |
| 3 | אוֹר | *or* | “light” | `payload_light` (**etnachta**) | STEP_3b |
| 4 | וַיְהִי | *va-yehi* | “and there was” | `result_be` | STEP_3c |
| 5 | אוֹר | *or* | “light” | `payload_light` (**silluq**) | STEP_3c |

## C. Why leaves force two stages (not one “make light”)

1. **[0][1]** = speech frame (said + agent).  
2. **[2][3]** = **jussive + payload** — command content; etnachta lands on **payload light**, so light is the pivot of the wish.  
3. **[4][5]** = **result-be + same payload** — fulfillment reuses the same noun leaf type.  
4. If you only say `BECOME(light)`, you drop that **speech verb** and **jussive** are distinct leaves from **result-be**.

## D. Near-code

```text
// STEP_3a
SPEECH_FRAME(agent=Elohim[1], verb=amar[0])

// STEP_3b  (content of speech; etnachta head = light)
COMMAND(
  mood = jussive yehi[2],
  payload = or[3]
)

// STEP_3c  (right arm; silluq head = light)
RESULT(
  become = va-yehi[4],
  payload = or[5]   // SAME open class as [3] — fulfillment identity
)

// Combined runtime:
SPEECH(Elohim): yehi(or)  ⇒  BECOME(or)
```

## E. State after 1:3

```text
+ or = exists
last_command = yehi(or)
last_result  = va-yehi(or)
```

---

# Genesis 1:4 — leaf derive EVAL then SEPARATE (two verbs, two agents)

## A. Full tree

```text
PHRASE (12w)
├── LEFT 6w (etnachta on טוב)
│   ├── 4w see-frame: [0] וַיַּרְא [1] אֱלֹהִים [2] אֶת [3] הָאוֹר
│   └── 2w grade:     [4] כִּי [5] ט֑וֹב
└── RIGHT 6w
    ├── 2w sep-frame: [6] וַיַּבְדֵּל [7] אֱלֹהִים
    └── 4w between-pair:
        ├── [8] בֵּין [9] הָאוֹר
        └── [10] וּבֵין [11] הַחֹשֶׁךְ
```

## B. Leaf table (12/12)

| i | he | translit | en | role | TIR | feeds |
|---|-----|----------|-----|------|-----|-------|
| 0 | וַיַּרְא | *va-yar* | “and he saw” | `verb_see` | — | STEP_4a |
| 1 | אֱלֹהִים | *Elohim* | “God” | `agent` | — | STEP_4a |
| 2 | אֶת | *et* | obj marker | `glue_object_marker` | TIR-014 | STEP_4a |
| 3 | הָאוֹר | *ha-or* | “the light” | `payload_light` (seen) | TIR-014 | STEP_4a |
| 4 | כִּי | *ki* | “that” | `eval_particle` | TIR-008 bound | STEP_4a |
| 5 | טוֹב | *tov* | “good” | `eval_grade` (**etnachta**) | — | STEP_4a |
| 6 | וַיַּבְדֵּל | *va-yavdel* | “and he divided” | `verb_separate` | — | STEP_4b |
| 7 | אֱלֹהִים | *Elohim* | “God” | `agent` (re-stated) | — | STEP_4b |
| 8 | בֵּין | *bein* | “between” | `between_a` marker | — | STEP_4b |
| 9 | הָאוֹר | *ha-or* | “the light” | pole A | — | STEP_4b |
| 10 | וּבֵין | *u-vein* | “and between” | `between_b` marker | — | STEP_4b |
| 11 | הַחֹשֶׁךְ | *ha-choshekh* | “the darkness” | pole B | — | STEP_4b |

## C. Nested derivation

**LEFT** is not “saw good light” as one smear:

```text
SEE(
  agent = Elohim[1],
  verb = ra’ah[0],
  object = et[2] → ha-or[3],     // TIR-014
  content = ki[4] + tov[5]       // grade is etnachta head of whole left
)
⇒ EVAL(target=or, grade=good)
```

**RIGHT** is a **new verb frame** (not a modifier of SEE):

```text
SEPARATE(
  agent = Elohim[7],             // leaf re-states agent under new verb
  verb = hivdil[6],
  poles = between(or[9], choshekh[11]) via [8][10]
)
```

## D. Why agent appears twice ([1] and [7])

Tree puts **אלהים** under **each** verb phrase.  
Leaf-level rule: **new verb ⇒ re-bind agent** (same idea as TIR-021 re-object under new verb).  
Top-split IR that says only `EVAL; SEPARATE` without citing **two agent leaves** under-extracts.

## E. Near-code

```text
EVAL(
  agent = Elohim,           // [1]
  see = va-yar,             // [0]
  patient = ha-or,          // [2][3]
  that = ki,                // [4]
  grade = tov               // [5] etnachta
)
SEPARATE(
  agent = Elohim,           // [7]
  verb = va-yavdel,         // [6]
  a = ha-or,                // [8][9]
  b = ha-choshekh           // [10][11]
)
```

## F. State after 1:4

```text
eval.or = good
sep.or_choshekh = true
// names for day/night still absent — no leaf named them yet
```

---

# Genesis 1:5 — leaf derive dual NAME + day clock

## A. Full tree (note 3-ary and 4-ary)

```text
PHRASE (13w)  pure_binary: false
├── LEFT 7w (etnachta on לילה)
│   ├── 4w first naming:
│   │   ├── 3-ary: [0] וַיִּקְרָא [1] אֱלֹהִים [2] לָאוֹר
│   │   └── [3] יוֹם (zaqef)     ← label for light
│   └── 3w second naming:
│       ├── [4] וְלַחֹשֶׁךְ (tifcha)
│       └── [5] קָרָא [6] לָ֑יְלָה (etnachta on Night)
└── RIGHT 6w day stamp
    ├── 4-ary clock parts: [7] וַיְהִי [8] עֶרֶב [9] וַיְהִי [10] בֹקֶר
    └── [11] יוֹם [12] אֶחָד
```

## B. Leaf table (13/13)

| i | he | translit | en | role | feeds |
|---|-----|----------|-----|------|-------|
| 0 | וַיִּקְרָא | *va-yiqra* | “and he called” | `verb_name` | STEP_5a |
| 1 | אֱלֹהִים | *Elohim* | “God” | `agent` | STEP_5a |
| 2 | לָאוֹר | *la-or* | “to the light” | `name_target` | STEP_5a |
| 3 | יוֹם | *yom* | “Day” | `name_label` | STEP_5a |
| 4 | וְלַחֹשֶׁךְ | *ve-la-choshekh* | “and to the dark” | `name_target` | STEP_5b |
| 5 | קָרָא | *qara* | “he called” | `verb_name` (**second**) | STEP_5b |
| 6 | לָיְלָה | *lailah* | “Night” | `name_label` (**etnachta**) | STEP_5b |
| 7 | וַיְהִי | *va-yehi* | “and there was” | `result_be` | STEP_5c |
| 8 | עֶרֶב | *erev* | “evening” | `clock_part` | STEP_5c |
| 9 | וַיְהִי | *va-yehi* | “and there was” | `result_be` | STEP_5c |
| 10 | בֹקֶר | *voqer* | “morning” | `clock_part` | STEP_5c |
| 11 | יוֹם | *yom* | “day” | `day_unit` | STEP_5c |
| 12 | אֶחָד | *echad* | “one” | `day_ordinal` | STEP_5c |

## C. Critical leaf details top-split misses

### 1. Two naming verbs, not one

- First call: **[0] ויקרא** with agent **[1]** and target **[2] לאור** → label **[3] יום**  
- Second call: **[5] קרא** again (not reused leaf [0]) with target **[4] ולחשך** → label **[6] לילה**

```text
NAME_1(agent=Elohim[1], verb=va-yiqra[0], target=la-or[2], label=yom[3])
NAME_2(verb=qara[5], target=ve-la-choshekh[4], label=lailah[6])
// agent not repeated as a leaf under second call — second verb phrase attaches under LEFT
```

If IR writes only `NAME(light→day, dark→night)`, it **hides the second קרא leaf**.

### 2. Day stamp is not “the word day from naming”

- **[3] יום** = **label for light**  
- **[11] יום** = **day-unit of the clock**  
- **[12] אחד** = ordinal/count **one**

Same string **יום** / *yom* / “day” — **two different leaves, two roles**.  
Collapsing them loses the clock vs name distinction.

### 3. 4-ary evening/morning group

Leaves **[7][8][9][10]** are a **4-ary** phrase: *va-yehi erev va-yehi voqer*  
→ clock is **ordered pair of become-events**, not a single idiom leaf.

```text
DAY_CLOSE(
  sequence = [ become(erev[8] via[7]), become(voqer[10] via[9]) ],
  stamp = yom[11] + echad[12]
)
```

## D. Near-code (full leaf citation)

```text
NAME(
  agent = Elohim,              // [1]
  verb1 = va-yiqra,            // [0]
  map1  = (la-or → yom),       // [2]→[3]
  verb2 = qara,                // [5]
  map2  = (la-choshekh → lailah) // [4]→[6]
)
DAY_CLOSE(
  evening = erev,              // [8] after va-yehi[7]
  morning = voqer,             // [10] after va-yehi[9]
  day_index = 1                // yom[11] + echad[12]
)
```

## E. State after 1:5 (end day one)

```text
names.or = yom                 // from leaves [2][3]
names.choshekh = lailah        // from leaves [4][6]
day_cycle = evening_then_morning  // [7–10]
clocks = [1]                   // [11][12]
eval.or = good                 // still from 1:4
sep.or_choshekh = true
```

---

# Whole-day program (only leaf-justified ops)

```text
// Gen 1:1  leaves 0–6
CREATE(
  when=be-reshit[0], agent=Elohim[2], verb=bara[1],
  objects=set_include_list( et shamayim[3-4], ve-et erets[5-6] )
)

// Gen 1:2  leaves 0–13
SET_STATE_EARTH(erets[0], hayetah[1], {tohu[2], vohu[3]})
SET_DARK_ON_DEEP(choshekh[4], al-penei-tehom[5-7])
SET_SPIRIT_OVER_WATERS(ruach-Elohim[8-9], merachefet[10], al-penei-mayim[11-13])

// Gen 1:3  leaves 0–5
SPEECH(agent=Elohim[1], amar[0]): yehi[2](or[3])
RESULT: va-yehi[4](or[5])

// Gen 1:4  leaves 0–11
EVAL(see Elohim[0-1] et-or[2-3] ki-tov[4-5])
SEPARATE(hivdil Elohim[6-7] bein or[8-9] u-vein choshekh[10-11])

// Gen 1:5  leaves 0–12
NAME(va-yiqra Elohim[0-1] la-or→yom[2-3]; qara[5] la-choshekh→lailah[4,6])
DAY_CLOSE(va-yehi erev[7-8], va-yehi voqer[9-10], yom echad[11-12])
```

---

# Step-through with state (leaf-aware)

| After | New facts (must map to leaves) |
|-------|--------------------------------|
| 1:1 | agent Elohim; domains shamayim+erets via dual *et* |
| 1:2 | earth tohu/vohu; dark on tehom face; spirit hovers on mayim face |
| 1:3 | command yehi(or) + result va-yehi(or) — light exists |
| 1:4 | light evaluated good; light\|dark separated under second agent-verb |
| 1:5 | or named yom; choshekh named lailah; clock evening→morning day **one** |

---

# Coverage metrics (this pass)

| Verse | Leaves | Accounted | Distinct roles (approx) | Multi-op from nesting? |
|-------|-------:|----------:|-------------------------|------------------------|
| 1:1 | 7 | 7 | time, verb, agent, et×2, domain×2 | CREATE + inventory |
| 1:2 | 14 | 14 | state / locative / spirit | 3 STEPs |
| 1:3 | 6 | 6 | speech / jussive / result / light×2 | 3 STEPs |
| 1:4 | 12 | 12 | see / ki / tov / separate / bein | 2 STEPs |
| 1:5 | 13 | 13 | name×2 / clock 4-ary / day+one | 3 STEPs |
| **Total** | **52** | **52** | — | — |

**OPEN TIR needs (not invented away):** boot `time_header` for **בראשית**; narrative `jussive_be` / `result_be` pair; dual `verb_name` pattern; 4-ary day-clock — promote to TIR-xxx when reused.

---

# Contrast: top-split IR vs leaf IR (same verses)

| Verse | Top-split only (old) | Leaf-derived (this file) |
|-------|----------------------|---------------------------|
| 1:1 | `CREATE(heavens, earth)` | CREATE + **when** + **agent** + **bara** + **TIR-015 dual et** |
| 1:2 | `SET chaos + spirit` | **3 clusters**: earth predicates / dark-on-deep / spirit-on-waters |
| 1:3 | `SPEECH → BECOME light` | amar+agent / **yehi+or** / **va-yehi+or** (six leaves) |
| 1:4 | `EVAL; SEPARATE` | see+et+or+**ki+tov**; **second** agent+hivdil+**bein pair** |
| 1:5 | `NAME; DAY_CLOSE(1)` | **two qara**; **two yom roles**; **4-ary** erev/boqer |

---

## Confidence

| Item | Label |
|------|--------|
| tree_ascii from unit / parser v1 | **tested** |
| 100% leaf listing 1:1–5 | **tested** |
| Role tags | **hypothesis** (richer than unit’s provisional `logic_bearing_leaf`) |
| Near-code ops | **hypothesis** — each cites leaf indices |
| Binding religious readout | **not claimed** |

---

## Next (if continued)

1. Promote stable roles to new **TIR-xxx** (boot speech/result, dual naming, day clock).  
2. Patch `gen_01_creation_boot.yaml` `tree_coverage` + `boot_steps` to match this leaf feed graph (not only `ETNACHTA_SPLIT`).  
3. Only then extend leaf method to days 2–7.

**One line:**  
Logic for Gen 1:1–5 is derived **leaf by leaf** from the stored ta’amim trees: every word has a role; every op names the leaves that justify it; top-split alone is **not** a complete derivation.
