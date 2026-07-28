# Tutorial — Genesis boot as near-code logic, stepped through

**Date:** 2026-07-26  
**Portion:** Genesis **1:1–2:3** (creation week → first Sabbath)  
**Kind:** beginner-friendly walkthrough · experimental model · **not** binding religious law  
**Source of Hebrew:** `Data/Gen.xml` (OSHB)  
**Unit files:** `logic/units/gen_01_creation_boot.yaml` … `gen_01_day7_shabbat.yaml` (draft, `tree_derived_v1`)  

**Method warning (2026-07-26):** Day 1 in this file was **top-split-only** IR. That under-extracts.  
**Corrected leaf-level derivation for Gen 1:1–5:**  
→ [`TUTORIAL_GEN_BOOT_LEAF_DERIVE_1_1_5_2026-07-26.md`](TUTORIAL_GEN_BOOT_LEAF_DERIVE_1_1_5_2026-07-26.md)  
**Novice full week:** [`TUTORIAL_GEN_BOOT_PLAIN_LEAF_STEPTHROUGH_1_1_2_3_2026-07-26.md`](TUTORIAL_GEN_BOOT_PLAIN_LEAF_STEPTHROUGH_1_1_2_3_2026-07-26.md) · hub: [`INDEX.md`](INDEX.md)  
(days 2–7 in *this* file still pedagogical top-split until leaf-redone.)  

**How to read every Hebrew string in this file:**

```text
עברית  /  translit  /  "English gloss"
```

Or as three fields: **he** · **he_translit** · **en**.  
Never bare Hebrew without English.

---

## 0. What we are doing (plain English)

We take the **create week** and treat it like a **small computer program** that boots the world.

| Layer | What it is | Example |
|-------|------------|---------|
| **1. Hebrew verse** | The real source text | Gen 1:3 |
| **2. Tree split** | Mid-verse rest (usually **אתנחתא** / *etnachta*) cuts the verse into **LEFT ‖ RIGHT** | “God said…” ‖ “and there was light” |
| **3. Near-code IR** | Human-readable “almost code” ops | `SPEECH → BECOME(light)` |
| **4. World state** | What is true *after* that line runs | `light = on` |

**Important honesty**

- The YAML units mostly store step 2 as `op: ETNACHTA_SPLIT` (“here is the tree”).  
- Steps 3–4 below are a **clearer interpretation** of those trees — **one step removed from real code**.  
- Status: **draft / hypothesis**. Not frozen for a religious or production interpreter.

### Tiny dictionary of ops (English)

| Op | Means in English |
|----|------------------|
| **CREATE / MAKE** | Bring something into being / fashion it |
| **SPEECH** | God **says** a command (wish-form) |
| **BECOME / effect** | The command’s result appears |
| **ACK** | **וַיְהִי כֵן** / *va-yehi khen* / “and it was so” — acknowledge success |
| **SEPARATE** | Split A from B (**הבדיל** / *hivdil* / “he divided”) |
| **NAME** | Call A by name B (**קרא** / *qara* / “he called”) |
| **EVAL** | See that it is good (**כי טוב** / *ki tov* / “that it was good”) |
| **BLESS** | Speak a lasting package of commands over creatures |
| **GRANT_FOOD** | Assign what may be eaten |
| **DAY_CLOSE** | Evening + morning = day *N* stamped |
| **FINISH / CEASE / SANCTIFY** | Day-7 shutdown sequence |

### World state (what the “machine” remembers)

```text
World {
  agent          // who acts (here: Elohim / God)
  domains        // heavens, earth…
  flags          // light on? firmament built? …
  names          // symbol table: light→day, firmament→heavens…
  creatures      // sea life, birds, land animals, human…
  clocks         // which days have closed [1,2,3…]
  last_eval      // last “good / very good”
  phase          // pre_boot → day_N_closed → finished → day_7…
}
```

**Start:** empty world · **agent** = **אֱלֹהִים** / *Elohim* / “God”.

---

# DAY 1 — Light, separation, first day name

**Unit:** `gen_01_creation_boot` · refs **1:1–5**

---

## Step 1 — Genesis 1:1

### Hebrew (full verse)

| | |
|--|--|
| **he** | בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ |
| **he_translit** | *be-reshit bara Elohim et ha-shamayim ve-et ha-arets* |
| **en** | “In the beginning God created the heavens and the earth.” |

### Tree (top split at mid-verse rest)

| Side | he | translit | en |
|------|-----|----------|-----|
| **LEFT** | בְּרֵאשִׁית בָּרָא אֱלֹהִים | *be-reshit bara Elohim* | “In the beginning God created” |
| **RIGHT** | אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ | *et ha-shamayim ve-et ha-arets* | “the heavens and the earth” |

**How to read the tree:** LEFT = **when + who + verb**; RIGHT = **what objects** get created.

### Near-code

```text
CREATE(shamayim, erets)
// domains: heavens + earth now exist
```

### English explanation

The program does **not** start with light. It starts by **opening two big domains**: sky-side and land-side (**הַשָּׁמַיִם** / *ha-shamayim* / “the heavens”; **הָאָרֶץ** / *ha-arets* / “the earth”).  
**בָּרָא** / *bara* / “created” is the install verb; **אֱלֹהִים** / *Elohim* / “God” is the only agent.

### State after 1:1

```text
domains = { shamayim: yes, erets: yes }
flags   = { created: yes }
phase   = still pre_boot (no day closed yet)
```

---

## Step 2 — Genesis 1:2

### Hebrew

| | |
|--|--|
| **he** | וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל פְּנֵי הַמָּיִם |
| **he_translit** | *ve-ha-arets hayetah tohu va-vohu ve-choshekh al penei tehom; ve-ruach Elohim merachefet al penei ha-mayim* |
| **en** | “And the earth was waste and void, and darkness was on the face of the deep; and the spirit of God was hovering on the face of the waters.” |

### Tree

| Side | he (short) | translit | en |
|------|------------|----------|-----|
| **LEFT** | וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל פְּנֵי תְהוֹם | *… tohu va-vohu … choshekh al penei tehom* | earth empty; dark on the deep |
| **RIGHT** | וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל פְּנֵי הַמָּיִם | *ve-ruach Elohim merachefet al penei ha-mayim* | God’s spirit hovering over the waters |

### Near-code

```text
SET_STATE(
  tohu = true,          // תֹהוּ / tohu / formless waste
  vohu = true,          // בֹהוּ / vohu / void
  dark_on_deep = true,  // חֹשֶׁךְ / choshekh / darkness on תְהוֹם / tehom / deep
  waters = true,        // מַיִם / mayim / waters
  spirit_over_waters = true
)
```

### English explanation

After CREATE, earth is **not** finished scenery. It is a **raw substrate**: empty, dark, watery.  
The RIGHT arm is not destruction — it is **presence over the chaos**: **רוּחַ אֱלֹהִים** / *ruach Elohim* / “spirit of God” **מְרַחֶפֶת** / *merachefet* / “hovering.”  
Think: hard drive formatted but empty, with the OS agent already “over” the medium.

### State after 1:2

```text
+ tohu, vohu, dark_on_deep, waters, spirit_over_waters
(light still OFF)
```

---

## Step 3 — Genesis 1:3

### Hebrew

| | |
|--|--|
| **he** | וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי אוֹר |
| **he_translit** | *va-yomer Elohim yehi or; va-yehi or* |
| **en** | “And God said, ‘Let there be light,’ and there was light.” |

### Tree (classic command ‖ result)

| Side | he | translit | en |
|------|-----|----------|-----|
| **LEFT** | וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר | *va-yomer Elohim yehi or* | God said: let there be light |
| **RIGHT** | וַיְהִי אוֹר | *va-yehi or* | and there was light |

### Near-code

```text
SPEECH("yehi or")   // יְהִי אוֹר / yehi or / "let light be"
BECOME(or)          // אוֹר / or / light now exists
```

### English explanation

This is the **speech → effect** pattern.  
LEFT is the **API call** (command). RIGHT is the **return value** (reality matches the command).  
No tools, no intermediate craftsman in the verse — say it, it is.

### State after 1:3

```text
+ or (light) = true
```

---

## Step 4 — Genesis 1:4

### Hebrew

| | |
|--|--|
| **he** | וַיַּרְא אֱלֹהִים אֶת הָאוֹר כִּי טוֹב וַיַּבְדֵּל אֱלֹהִים בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ |
| **he_translit** | *va-yar Elohim et ha-or ki tov; va-yavdel Elohim bein ha-or u-vein ha-choshekh* |
| **en** | “And God saw the light, that it was good; and God divided between the light and the darkness.” |

### Tree

| Side | he | translit | en |
|------|-----|----------|-----|
| **LEFT** | וַיַּרְא … אֶת הָאוֹר כִּי טוֹב | *va-yar … ha-or ki tov* | saw the light that it was good |
| **RIGHT** | וַיַּבְדֵּל … בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ | *va-yavdel … bein ha-or u-vein ha-choshekh* | divided between light and dark |

### Near-code

```text
EVAL(or, grade="good")           // כִּי טוֹב / ki tov
SEPARATE(or | choshekh)          // הבדיל / hivdil between light|dark
```

### English explanation

Two different jobs in one verse:

1. **Quality check** — light is marked **good**.  
2. **Structure** — light is not mixed indefinitely with dark; they become a **pair** with a boundary (**בֵּין … וּבֵין** / *bein … u-vein* / “between … and between”).

This SEPARATE is a reusable operator later (waters, day/night lights, etc.).

### State after 1:4

```text
+ sep_or_choshekh = true
  last_eval = "or:good"
```

---

## Step 5 — Genesis 1:5

### Hebrew

| | |
|--|--|
| **he** | וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם אֶחָד |
| **he_translit** | *va-yiqra Elohim la-or yom, ve-la-choshekh qara lailah; va-yehi erev va-yehi voqer yom echad* |
| **en** | “And God called the light Day, and the darkness He called Night; and there was evening and there was morning, one day.” |

### Tree

| Side | he | translit | en |
|------|-----|----------|-----|
| **LEFT** | וַיִּקְרָא … לָאוֹר יוֹם … לַחֹשֶׁךְ … לָיְלָה | *… la-or yom … la-choshekh … lailah* | name light→Day, dark→Night |
| **RIGHT** | וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם אֶחָד | *va-yehi erev va-yehi voqer yom echad* | evening + morning = day one |

### Near-code

```text
NAME(or → "yom")              // יוֹם / yom / Day
NAME(choshekh → "lailah")     // לַיְלָה / lailah / Night
DAY_CLOSE(1)                  // evening then morning stamps day 1
```

### English explanation

**NAME** writes the **symbol table**: physical light/dark get calendar words Day/Night.  
**DAY_CLOSE** invents the project’s **day_cycle** export: evening → morning = one day. Later law can join this pattern.

### State after 1:5 (end of Day 1 unit)

```text
names  = { or→yom, choshekh→lailah }
clocks = [1]
phase  = day_1_closed
export day_cycle = evening_then_morning
```

---

# DAY 2 — Firmament (רקיע) and waters above/below

**Unit:** `gen_01_day2_raqia` · **1:6–8**

---

## Step 6 — Genesis 1:6

### Hebrew

| | |
|--|--|
| **he** | וַיֹּאמֶר אֱלֹהִים יְהִי רָקִיעַ בְּתוֹךְ הַמָּיִם וִיהִי מַבְדִּיל בֵּין מַיִם לָמָיִם |
| **he_translit** | *va-yomer Elohim yehi raqia be-tokh ha-mayim; vi-hi mavdil bein mayim la-mayim* |
| **en** | “And God said, ‘Let there be a firmament in the midst of the waters, and let it divide water from water.’” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | Speech: let there be **רָקִיעַ** / *raqia* / firmament **in the middle of the waters** |
| **RIGHT** | Function: it shall be a **divider** between waters and waters |

### Near-code

```text
SPEECH("yehi raqia")
// intended function: SEPARATE(mayim | mayim)  — not executed as craft until 1:7
```

### English explanation

Day 2 starts like day 1’s light: **command first**.  
The firmament is defined by **job description** before it is “made”: sit in the waters and **divide**.

---

## Step 7 — Genesis 1:7

### Hebrew

| | |
|--|--|
| **he** | וַיַּעַשׂ אֱלֹהִים אֶת הָרָקִיעַ וַיַּבְדֵּל בֵּין הַמַּיִם אֲשֶׁר מִתַּחַת לָרָקִיעַ וּבֵין הַמַּיִם אֲשֶׁר מֵעַל לָרָקִיעַ וַיְהִי כֵן |
| **he_translit** | *va-ya‘as Elohim et ha-raqia; va-yavdel bein ha-mayim asher mi-tachat la-raqia u-vein ha-mayim asher me‘al la-raqia; va-yehi khen* |
| **en** | “And God made the firmament, and divided the waters under the firmament from the waters above the firmament; and it was so.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | **MAKE** the firmament + **SEPARATE** waters under ‖ waters above |
| **RIGHT** | **וַיְהִי כֵן** / *va-yehi khen* / “and it was so” (**ACK**) |

### Near-code

```text
MAKE(raqia)
SEPARATE(mayim_below | mayim_above)
ACK()   // va-yehi khen
```

### English explanation

Now the speech is **implemented**:

- **עָשָׂה** / *asah* / “made” (craft/make verb)  
- Waters get **vertical addresses**: under the firmament / above the firmament  
- **ACK** closes the command-fulfillment loop

### State after 1:7

```text
+ raqia
+ sep_mayim_below_mayim_above
+ vayehi_ken
```

---

## Step 8 — Genesis 1:8

### Hebrew

| | |
|--|--|
| **he** | וַיִּקְרָא אֱלֹהִים לָרָקִיעַ שָׁמָיִם וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם שֵׁנִי |
| **he_translit** | *va-yiqra Elohim la-raqia shamayim; va-yehi erev va-yehi voqer yom sheni* |
| **en** | “And God called the firmament Heavens; and there was evening and there was morning, a second day.” |

### Near-code

```text
NAME(raqia → "shamayim")   // רָקִיעַ gets the name שָׁמַיִם
DAY_CLOSE(2)
```

### English explanation

The object built in 1:7 is **registered** under the public name **heavens** — same word-family as 1:1’s domain, now tied to a concrete structure.  
Day 2 closes with the same evening/morning clock as day 1.

### State after Day 2

```text
names  += { raqia → shamayim }
clocks = [1, 2]
```

---

# DAY 3 — Dry land, seas, plants

**Unit:** `gen_01_day3_land_plants` · **1:9–13**

---

## Step 9 — Genesis 1:9

### Hebrew

| | |
|--|--|
| **he** | וַיֹּאמֶר אֱלֹהִים יִקָּווּ הַמַּיִם מִתַּחַת הַשָּׁמַיִם אֶל מָקוֹם אֶחָד וְתֵרָאֶה הַיַּבָּשָׁה וַיְהִי כֵן |
| **he_translit** | *va-yomer Elohim yiqqavu ha-mayim mi-tachat ha-shamayim el maqom echad ve-tera’eh ha-yabashah; va-yehi khen* |
| **en** | “And God said, ‘Let the waters under the heavens be gathered to one place, and let the dry land appear’; and it was so.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | SPEECH: gather under-heaven waters → **יַבָּשָׁה** / *yabashah* / dry land appears |
| **RIGHT** | ACK (*va-yehi khen*) |

### Near-code

```text
SPEECH(gather_waters_under_shamayim → one_place)
// side effect: yabashah becomes visible
ACK()
```

### English explanation

Day 2 stacked waters **vertically**. Day 3 rearranges waters **horizontally** so dry ground shows.  
Same pattern: SPEECH + ACK.

---

## Step 10 — Genesis 1:10

### Hebrew

| | |
|--|--|
| **he** | וַיִּקְרָא אֱלֹהִים לַיַּבָּשָׁה אֶרֶץ וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים וַיַּרְא אֱלֹהִים כִּי טוֹב |
| **he_translit** | *va-yiqra Elohim la-yabashah erets, u-le-miqveh ha-mayim qara yamim; va-yar Elohim ki tov* |
| **en** | “And God called the dry land Earth, and the gathering of waters He called Seas; and God saw that it was good.” |

### Near-code

```text
NAME(yabashah → "erets")        // dry land → Earth
NAME(miqveh_mayim → "yamim")    // water-gathering → Seas
EVAL(land_seas, "good")
```

### English explanation

Again **NAME** turns physical layout into **public vocabulary** (Earth / Seas).  
First **good** after day 1’s light — land/sea map passes QA.

---

## Step 11 — Genesis 1:11

### Hebrew (sense)

God says: let the earth sprout vegetation — grass seeding seed, fruit tree making fruit **לְמִינוֹ** / *le-mino* / “according to its kind” — and it was so.

### Near-code

```text
SPEECH(earth_sprout_plants_by_kind)
ACK()
```

### English explanation

First **life-ish** content is **plant life**, still tied to earth’s productivity.  
**By kind** is a type-system constraint: kinds stay distinct.

---

## Step 12 — Genesis 1:12

### Near-code

```text
MAKE(plants_by_kind)    // earth brings forth what was spoken
EVAL(plants, "good")
```

### English explanation

1:11 = command; 1:12 = **execution + eval**.  
(Compare 1:6 speech vs 1:7 make.)

---

## Step 13 — Genesis 1:13

### Hebrew

| | |
|--|--|
| **he** | וַיְהִי עֶרֶב וַיְהִי בֹקֶר יוֹם שְׁלִישִׁי |
| **he_translit** | *va-yehi erev va-yehi voqer yom shelishi* |
| **en** | “And there was evening and there was morning, a third day.” |

### Near-code

```text
DAY_CLOSE(3)
```

### State after Day 3

```text
+ yabashah, waters_gathered
  names += erets, yamim
+ plants_by_kind
  clocks = [1,2,3]
```

---

# DAY 4 — Luminaries (time service)

**Unit:** `gen_01_day4_lights` · **1:14–19**

Day 4 does **not** invent light from nothing (that was day 1). It installs **bodies in the firmament** that **rule** day/night and open **calendar ports**.

---

## Step 14 — Genesis 1:14

### Hebrew (sense)

God said: let there be **מְאֹרֹת** / *me’orot* / “luminaries, light-bearers” in the firmament of the heavens to **divide** day and night; and they shall be for **signs, appointed times, days, and years**.

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | SPEECH: luminaries in firmament to divide day\|night |
| **RIGHT** | Extra jobs: signs / festivals-seasons / days / years |

### Near-code

```text
SPEECH(install_meorot_in_raqia)
// functions:
//   SEPARATE(yom | lailah)   // operational day/night
//   open calendar_ports = { otot, mo‘adim, yamim, shanim }
```

### English explanation

This is the **time service** API:

- **אֹתֹת** / *otot* / “signs”  
- **מוֹעֲדִים** / *mo‘adim* / “appointed times” (later: festival calendar joins here)  
- **יָמִים וְשָׁנִים** / *yamim ve-shanim* / “days and years”

---

## Steps 15–18 — Genesis 1:15–18 (compressed but clear)

| Ref | Near-code | English |
|-----|-----------|---------|
| **1:15** | function: light the earth; **ACK** | Luminaries exist *to illuminate* land |
| **1:16** | **MAKE** great light → rule **day**; small light → rule **night**; **stars** | Hardware assignment |
| **1:17** | **PLACE** them in the firmament of heavens | Location = day-2 structure |
| **1:18** | rule day & night; divide light\|dark; **EVAL good** | Job description + QA |

### Key Hebrew bits

| he | translit | en |
|----|----------|-----|
| מְאֹרֹת | *me’orot* | luminaries / light-bearers |
| מֶמְשֶׁלֶת הַיּוֹם | *memshelet ha-yom* | dominion/rule of the day |
| מֶמְשֶׁלֶת הַלַּיְלָה | *memshelet ha-lailah* | dominion/rule of the night |
| כּוֹכָבִים | *kokhavim* | stars |

### Near-code sketch

```text
MAKE(meor_gadol, rules="yom")
MAKE(meor_qaton, rules="lailah")
MAKE(kokhavim)
PLACE(meorot @ raqia)
SET meorot_rule = true
EVAL(meorot, "good")
DAY_CLOSE(4)   // 1:19
```

### English explanation

Day 1: raw **light**.  
Day 4: **organized lighting + clock hardware** hung on the firmament, with **rule** language (**ממשלה** / *memshalah* / dominion).

### State after Day 4

```text
+ calendar_ports, meorot_rule
+ meor_gadol, meor_qaton, kokhavim
  clocks = [1,2,3,4]
```

---

# DAY 5 — Sea life, birds, first blessing

**Unit:** `gen_01_day5_sea_birds` · **1:20–23**

---

## Step 20 — Genesis 1:20

### Hebrew (sense)

God said: let the waters **swarm** with swarms of living creatures, and let birds **fly** over the earth across the face of the firmament of the heavens.

### Near-code

```text
SPEECH(
  waters.swarm(nephesh_chayah),   // נֶפֶשׁ חַיָּה / living being
  birds.fly(over_erets, face_of_raqia)
)
```

### English explanation

Two biomes at once: **water column** and **air/sky face** of the firmament.  
Life is no longer plant-only.

---

## Step 21 — Genesis 1:21

### Near-code

```text
CREATE(tanninim_gedolim)           // הַתַּנִּינִם הַגְּדֹלִים / great sea creatures
CREATE(sea_nephesh by_kind)
CREATE(of_kanaf by_kind)           // עֵוֹף כָּנָף / winged bird
EVAL(day5_life, "good")
```

### English explanation

**בָּרָא** / *bara* / “created” returns for animals (strong create verb).  
**Kinds** again — type discipline.

---

## Step 22 — Genesis 1:22  ★ first BLESS package

### Hebrew

| | |
|--|--|
| **he** | וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ אֶת הַמַּיִם בַּיַּמִּים וְהָעוֹף יִרֶב בָּאָרֶץ |
| **he_translit** | *va-yevarekh otam Elohim lemor: peru u-revu u-mil’u et ha-mayim ba-yamim; ve-ha-‘of yirev ba-arets* |
| **en** | “And God blessed them, saying: Be fruitful and multiply and fill the waters in the seas, and let the bird multiply on the earth.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | **BLESS** them, saying… |
| **RIGHT** | the **command package** (fruitful / multiply / fill waters; bird multiply on land) |

### Near-code

```text
BLESS(sea_and_birds, cmds=[
  "parah",   // פְּרוּ / peru / be fruitful
  "ravah",   // רְבוּ / revu / multiply
  "male_waters",  // מִלְאוּ … הַמַּיִם בַּיַּמִּים / fill the waters in the seas
  "bird_ravah_erets"  // bird multiply on earth
])
```

### English explanation

A **blessing** here is not a vague wish — it is a **stored command package** on a class of creatures.  
Domain split: seas for swarm-fill; land for bird multiply.  
(This is the same family later expanded for humans in 1:28 — fill **earth**, plus rule.)

### State after 1:22–23

```text
+ bless_sea_and_birds
  clocks = [1,2,3,4,5]
```

---

# DAY 6 — Land animals, human, rule, food

**Unit:** `gen_01_day6_land_human` · **1:24–31**

---

## Steps 24–25 — Land animals

### 1:24 near-code

```text
SPEECH(earth_bring_nephesh_chayah by_kind:
       behemah, remes, chayto_erets)
ACK()
```

| he | translit | en |
|----|----------|-----|
| בְּהֵמָה | *behemah* | cattle / domestic-class beast |
| רֶמֶשׂ | *remes* | crawling things |
| חַיְתוֹ אֶרֶץ | *chayto erets* | wild land animals |

### 1:25 near-code

```text
MAKE(land_animals_by_kind)
EVAL(land_animals, "good")
```

---

## Step 26 — Genesis 1:26 (intent + job description)

### Hebrew (sense)

God said: let us make **אָדָם** / *adam* / “human” in our **image** (**צֶלֶם** / *tselem*) according to our **likeness** (**דְּמוּת** / *demut*); and let them **rule** fish, birds, cattle, all the earth, and crawling things.

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | SPEECH: make human in image/likeness |
| **RIGHT** | purpose: **וְיִרְדּוּ** / *ve-yirdu* / “and they shall rule” over the creature classes |

### Near-code

```text
SPEECH(na‘aseh adam be-tsalmenu ki-dmutenu)
SET radah_cmd = true   // rule mandate listed
```

### English explanation

Human is specified **with a role** before the create line finishes: not only “exist,” but **rule** the already-installed life stack.

---

## Step 27 — Genesis 1:27

### Hebrew

| | |
|--|--|
| **he** | וַיִּבְרָא אֱלֹהִים אֶת הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ זָכָר וּנְקֵבָה בָּרָא אֹתָם |
| **he_translit** | *va-yivra Elohim et ha-adam be-tsalmo; be-tselem Elohim bara oto; zakhar u-neqevah bara otam* |
| **en** | “And God created the human in His image; in the image of God He created him; male and female He created them.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | CREATE human in image (stated twice for emphasis) |
| **RIGHT** | male and female created them |

### Near-code

```text
CREATE(adam, mode="be_tselem")
CREATE(zakhar_neqevah)   // זָכָר וּנְקֵבָה / male and female
```

---

## Step 28 — Genesis 1:28  ★ human BLESS (expanded vs 1:22)

### Hebrew (sense)

God blessed them and said: be fruitful, multiply, **fill the earth and subdue it**, and **rule** the fish of the sea, the bird of the heavens, and every living thing that crawls on the earth.

### Near-code

```text
BLESS(adam, cmds=[
  "parah", "ravah",
  "male_erets",   // fill the earth (not only seas)
  "kavash",       // כִּבְשׁוּהָ / kivshuha / subdue it
  "radah"         // רְדוּ / redu / rule
])
```

### English explanation (compare 1:22)

| | Day 5 (1:22) | Day 6 (1:28) |
|--|--------------|--------------|
| Fruitful / multiply | yes | yes |
| Fill | **waters/seas** | **earth** |
| Extra | bird multiplies on land | **subdue** + **rule** animals |

Same family of ops; **more fields** for humans.

---

## Steps 29–30 — Food policy

### 1:29 near-code

```text
GRANT_FOOD(adam ← esev zorea‘ zera + ets peri)
// seed-bearing plants + fruit trees → for you as food
```

| he | translit | en |
|----|----------|-----|
| עֵשֶׂב זֹרֵעַ זֶרַע | *esev zorea‘ zera* | herb seeding seed |
| עֵץ … פְּרִי | *ets … peri* | tree with fruit |
| אָכְלָה | *okhlah* | food |

### 1:30 near-code

```text
GRANT_FOOD(animals ← yereq esev)  // יֶרֶק עֵשֶׂב / green herb
ACK()
```

### English explanation

Boot installs a **food law** before any story conflict:

- Humans: plants that seed + fruit trees  
- Animals: green herb  

(Later Gen 9 will **expand** human food — that is a remote expand of this header.)

---

## Step 31 — Genesis 1:31

### Hebrew (sense)

God saw **all** that He had made, and behold, it was **very good**; evening and morning, the sixth day.

### Near-code

```text
EVAL(all, "very_good")   // טוֹב מְאֹד / tov me’od
DAY_CLOSE(6)
```

### English explanation

Peak QA: not one object, but **the whole system**.  
Day 6 closes the create-work week.

### State after Day 6

```text
creatures = sea + birds + land + adam (image, male/female)
bless_adam = true
food policies set
last_eval = all:very_good
clocks = [1,2,3,4,5,6]
```

---

# DAY 7 — Finish, cease, sanctify

**Unit:** `gen_01_day7_shabbat` · **2:1–3**

No new SPEECH-create of creatures. This is **shutdown / seal**.

---

## Step 32 — Genesis 2:1

### Hebrew

| | |
|--|--|
| **he** | וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל צְבָאָם |
| **he_translit** | *va-yekhullu ha-shamayim ve-ha-arets ve-khol tseva’am* |
| **en** | “And the heavens and the earth were finished, and all their host.” |

### Near-code

```text
FINISH(shamayim, erets, host)
```

---

## Step 33 — Genesis 2:2

### Hebrew

| | |
|--|--|
| **he** | וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי מְלַאכְתּוֹ אֲשֶׁר עָשָׂה וַיִּשְׁבֹּת בַּיּוֹם הַשְּׁבִיעִי מִכָּל מְלַאכְתּוֹ אֲשֶׁר עָשָׂה |
| **he_translit** | *va-yekhal Elohim ba-yom ha-shevi‘i melakhto asher asah; va-yishbot ba-yom ha-shevi‘i mi-kol melakhto asher asah* |
| **en** | “And God finished on the seventh day His work which He had made; and He ceased on the seventh day from all His work which He had made.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | finished His **מְלָאכָה** / *melakhah* / work on day 7 |
| **RIGHT** | **שָׁבַת** / *shavat* / ceased on day 7 from all that work |

### Near-code

```text
SET melakhah_done = true
CEASE()   // shavat
```

---

## Step 34 — Genesis 2:3

### Hebrew

| | |
|--|--|
| **he** | וַיְבָרֶךְ אֱלֹהִים אֶת יוֹם הַשְּׁבִיעִי וַיְקַדֵּשׁ אֹתוֹ כִּי בוֹ שָׁבַת מִכָּל מְלַאכְתּוֹ אֲשֶׁר בָּרָא אֱלֹהִים לַעֲשׂוֹת |
| **he_translit** | *va-yevarekh Elohim et yom ha-shevi‘i va-yeqaddesh oto; ki vo shavat mi-kol melakhto asher bara Elohim la‘asot* |
| **en** | “And God blessed the seventh day and sanctified it, because on it He ceased from all His work which God had created to make.” |

### Tree

| Side | en gist |
|------|---------|
| **LEFT** | bless + **קִדֵּשׁ** / *qiddesh* / sanctify the seventh day |
| **RIGHT** | **reason** (**כִּי** / *ki* / “because”): He ceased on it from the work |

### Near-code

```text
BLESS(day_7)
SANCTIFY(day_7)
// reason: CEASE already true
DAY_CLOSE(7)
```

### English explanation

Day 7 is not “another create.” It is:

1. declare work **complete**  
2. **stop**  
3. mark the day **blessed + holy** *because* of the stop  

That exports **Shabbat shape** for later law (remember/observe the day).

### Final state

```text
phase       = day_7_closed
clocks      = [1,2,3,4,5,6,7]
work_finished, shavat, day_7_holy = true
last_eval   = all:very_good
```

---

# Big picture — the program shape

```text
for most create-days:
    SPEECH(command)
    [MAKE / CREATE / rearrange]
    [SEPARATE | NAME | BLESS | GRANT_FOOD]
    [EVAL good?]
    DAY_CLOSE(n)

day 7:
    FINISH → CEASE → BLESS+SANCTIFY(day) → DAY_CLOSE(7)
```

### What later “modules” can import (exports)

| Export | From | English meaning |
|--------|------|-----------------|
| `agent_elohim` | whole boot | God as creating agent |
| `day_cycle` | 1:5 pattern | evening → morning = one day |
| `light_dark` pair | 1:3–5 | light/dark separated + named |
| `raqia` / `shamayim` | day 2 | firmament structure + name |
| `calendar_ports` | day 4 | signs, times, days, years |
| `meorot_rule` | day 4 | lights rule day/night |
| `bless_sea_birds` | 1:22 | fruitfulness package (waters) |
| `bless_adam` | 1:28 | fruitfulness + subdue + rule |
| `food_policy` | 1:29–30 | who eats what |
| `shabbat_day7` | 2:1–3 | cease + holy day |

---

# How this relates to the YAML on disk

| On disk (`logic/units/gen_01_*.yaml`) | This tutorial |
|--------------------------------------|---------------|
| `op: ETNACHTA_SPLIT` | Explains that split in English |
| `tree_left` / `tree_right` Hebrew arms | Same arms, with translit + gloss |
| status **draft** | We add near-code IR as **hypothesis** |
| not frozen | Do **not** treat this as final law code |

When units are someday **frozen**, an interpreter should **load** the document — not invent new rules in Python.

---

# Mini glossary (core Hebrew in this boot)

| he | translit | en |
|----|----------|-----|
| בָּרָא | *bara* | created |
| אֱלֹהִים | *Elohim* | God |
| אָמַר | *amar* | said |
| יְהִי | *yehi* | let there be |
| אוֹר | *or* | light |
| חֹשֶׁךְ | *choshekh* | darkness |
| הִבְדִּיל | *hivdil* | divided / separated |
| קָרָא | *qara* | called / named |
| רָקִיעַ | *raqia* | firmament |
| יַבָּשָׁה | *yabashah* | dry land |
| מְאֹרֹת | *me’orot* | luminaries |
| בֵּרַךְ | *berakh* | blessed |
| פְּרוּ וּרְבוּ | *peru u-revu* | be fruitful and multiply |
| צֶלֶם | *tselem* | image |
| כָּבַשׁ | *kavash* | subdue |
| רָדָה | *radah* | rule / have dominion |
| מְלָאכָה | *melakhah* | work |
| שָׁבַת | *shavat* | ceased / rested |
| קִדֵּשׁ | *qiddesh* | sanctified / made holy |
| כִּי טוֹב | *ki tov* | that it was good |
| וַיְהִי כֵן | *va-yehi khen* | and it was so |

---

## Confidence

| Claim | Label |
|-------|--------|
| Verse Hebrew + tree L‖R match draft units / OSHB | **tested** |
| Near-code op names | **hypothesis** (pedagogy) |
| World-state field names | **hypothesis** |
| Binding religious “this is how creation runs” | **not claimed** |

---

**One sentence:**  
Genesis 1:1–2:3 can be read as a **boot program**: speech installs structure and life, names and evals lock meaning, blessings store policies, and day 7 **seals** the build by ceasing and sanctifying the day — and every step above keeps **Hebrew + transliteration + English** so you can follow without bare Hebrew.
