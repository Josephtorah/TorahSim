# Beginner’s tutorial: How we derive logic from the Torah  
### (You do **not** need to speak Hebrew)

This guide is for people starting from zero: no Hebrew, no programming, no prior Torah study required.

You will learn:

1. What we mean by **“logic”** here  
2. Why we start from **Hebrew**, not English  
3. How to **read** Hebrew on the page (with training wheels)  
4. What each **step** does, and how it builds toward a finished logic document  
5. A full walkthrough of **Leviticus 12** (childbirth purity rules) as an example  

**Worked example file:** `logic/units/lev_12_childbirth.yaml`  
**Long tutorial (pipeline + show all work + Gen day 4):** `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md`  
**Genesis boot tutorials (day 1 / create week):** `logic/gen_boot/INDEX.md` (start with plain leaf step-through) · unit `logic/units/gen_01_creation_boot.yaml`  
**Full technical method:** `logic/SYSTEM.md`  
**Blank form to copy:** `logic/templates/unit_template.yaml`

---

## Big picture (one minute)

Imagine a cookbook written in a language you don’t speak.

- You should **not** invent recipes from a rough English paraphrase someone made later.  
- You **should** look at the original words, get a careful gloss of each phrase, and then write down:  
  **when** this applies, **what** happens, and **for how long**.

That write-up is our **logic document**.  
It is **not** computer code. Code (if any) comes *later*, and only to follow what the document already says.

```
Hebrew text  →  tree (how the sentence is split)  →  clear WHEN / THEN rules
                                                      (and timed “states”)
```

---

## Part 1 — Words you’ll see a lot

| Word | Plain meaning |
|------|----------------|
| **Torah** | Here: the Five Books of Moses (Genesis–Deuteronomy). We work verse by verse. |
| **Hebrew** | The original language of the Torah text we treat as the source. |
| **Transliteration** | Hebrew written with English letters so you can *sound* it. Example: זָכָר → `zakhar`. |
| **Gloss / free translation** | Everyday English for a phrase. Helpful for *you*; **not** the legal source. |
| **Logic** | Precise “when / then / for how long / what status” rules, not poetry. |
| **Derivation** | Tracing a rule back to exact Hebrew words (and structure). |
| **Unit** | One self-contained block we study (e.g. Leviticus 12:1–8). |
| **Binary / ta'amim tree** | How the verse is *split into nested phrases* (like a family tree of clauses). |
| **Decision table** | Rows of cases: “IF this… THEN that…” |
| **State machine** | A map of statuses over time: impure → sitting period → pure after ritual. |
| **Scenario** | A test story: “If a boy is born, how many days?” checked against the rules. |
| **Confidence** | How sure we are: hypothesis / tested / established / failed / dead end. |

### The golden display rule (always)

Whenever you see Hebrew, you should also see:

```text
Hebrew   /   transliteration   /   "English meaning"
```

Example:

```text
זָכָר  /  zakhar  /  "male"
```

**Never** leave bare Hebrew without those two helpers.

---

## Part 2 — Two rules that never change

### Rule 1: Hebrew is the source of truth

We derive numbers, genders, and outcomes from the **Hebrew** text in this project’s `Data/` folder (for Leviticus: `Data/Lev.xml`).

English Bibles are useful **reading aids**.  
They are **not** allowed to invent a rule by themselves.

If English and Hebrew seem to disagree → **Hebrew wins**, and we note the conflict.

### Rule 2: English is for *you*, not for the rulebook

You are allowed—and expected—to understand everything in English.  
But every claim must still point at a Hebrew phrase (plus transliteration).

---

## Part 3 — How to “read” Hebrew without speaking it

You will not “learn Hebrew” in this tutorial. You will learn a **reading habit**:

1. Look at the **Hebrew letters** (so you know which exact words were used).  
2. Read the **transliteration** out loud if you want (optional).  
3. Read the **English gloss**.  
4. Ask: *What job does this phrase do?*  
   - setup / header  
   - **when** (condition)  
   - **then** (result)  
   - how long (number words)  
   - comparison / reference  
   - final status  

### Number words you’ll meet in Lev 12

| Hebrew | Translit | English | Number we use |
|--------|----------|---------|----------------|
| שִׁבְעַת יָמִים | shiv'at yamim | seven days | **7** |
| שְׁבֻעַיִם | shevu'ayim | two weeks | **14** |
| שְׁלֹשִׁים + שְׁלֹשֶׁת | shloshim + shloshet | thirty + three | **33** |
| שִׁשִּׁים + שֵׁשֶׁת | shishim + sheshet | sixty + six | **66** |
| שְׁמִינִי | shemini | eighth | **day 8** |

We do **not** start from the English number “thirty-three.”  
We read the Hebrew pieces, then write “33” as a **gloss** of those pieces.

### Gender words

| Hebrew | Translit | English |
|--------|----------|---------|
| זָכָר | zakhar | male |
| נְקֵבָה | nekevah | female |

---

## Part 4 — What a finished “logic unit” looks like

A unit is a YAML file under `logic/units/`. Think of it as a **filled workbook**:

| Section | Job (plain English) |
|---------|---------------------|
| `meta` | Title, which verses, where the Hebrew file is |
| `derivation_log` | Diary of steps A–J (“what we did and why”) |
| `source_verses` | Full Hebrew of each verse + full English gloss |
| `binary_trees` | How each verse splits into nested phrases |
| `phrase_map` | Flat list of important phrases and their roles |
| `decision_table` | Side-by-side cases (male vs female, etc.) |
| `state_machine` | Status over time for the person the law describes |
| `rules` | Extra WHEN/THEN that apply across cases |
| `oral_attachments` | Optional later Jewish texts—**labeled**, not mixed in silently |
| `scenarios` | Practice tests without writing code |
| checklist | Did we leak English-only rules? Did we bare-Hebrew? |

You can open the real filled example:

**`logic/units/lev_12_childbirth.yaml`**

---

## Part 5 — The ten steps (A–J), explained simply

We always work in order. Each step **adds something the next step needs**.

---

### Step A — Choose the unit  
**Question it answers:** *What chunk of text are we studying?*

**Why it helps:** Logic falls apart if you mix unrelated stories. A good unit is a **self-contained procedure**.

**Lev 12 example:**  
We chose **Leviticus 12:1–8**  
- Hebrew book: ויקרא / Vayikra / “Leviticus”  
- Topic in plain English: what happens after a woman gives birth (timed impurity, then offerings, then purity).

**Beginner tip:** Prefer short legal blocks over long narrative for your first units.

---

### Step B — Load the **Hebrew** source  
**Question it answers:** *Where are the exact words?*

**Why it helps:** Prevents “I think the verse said…” mistakes.

**Lev 12 example:**  
Source file: `Data/Lev.xml` (Open Scriptures Hebrew Bible).  
We extract verses labeled `Lev.12.1` … `Lev.12.8`.

You may peek at an English Bible only to get oriented.  
You still **copy rule content from Hebrew phrases**.

**Beginner tip:** If a friend only quotes English, ask: “Which Hebrew words?”

---

### Step C — Build the **structure tree** first  
**Question it answers:** *Where does the sentence split? Where is the “IF”?*

**Why it helps:** Ancient Hebrew Bibles mark **cantillation** (ta'amim)—chanting marks that also act like **punctuation and nesting**.  
In our data file, many words carry a path like `n="1"` or `n="0.1.0"`. Those paths let us draw a **tree**:

- One side of a major split often holds the **condition**  
- The other side often holds the **result**

**Plain analogy:**  
A period and a semicolon tell you where English sentences break.  
Ta'amim / `n=` paths do a similar job in Hebrew—often in a **binary** (two-branch) way.

#### Mini example — Leviticus 12:2 (the teaching verse)

**Full verse (training-wheels form):**

| | |
|--|--|
| **Hebrew** | דַּבֵּר אֶל בְּנֵי יִשְׂרָאֵל לֵאמֹר אִשָּׁה כִּי תַזְרִיעַ וְיָלְדָה זָכָר וְטָמְאָה שִׁבְעַת יָמִים … תִּטְמָא |
| **Translit** | Daber el benei Yisrael lemor: ishah ki tazria veyaledah zakhar, vetam'ah shiv'at yamim … titma |
| **English** | Speak to the children of Israel, saying: A woman when she conceives and bears a **male**—she shall be impure **seven days** … she shall be impure. |

**Top split (simple picture):**

```text
                    [ whole verse ]
                    /              \
         CONDITION half              RESULT half
    head: זָכָר / zakhar / "male"    head: תִּטְמָא / titma / "she shall be impure"
         (n = "1")                        (n = "0")
```

Under the **male** side you also find:

- אִשָּׁה / ishah / “a woman”  
- תַזְרִיעַ / tazria / “she conceives”  
- וְיָלְדָה / veyaledah / “and she bears”  

Under the **impure** side you find:

- שִׁבְעַת יָמִים / shiv'at yamim / “seven days”  
- comparison to נִדָּה / niddah / “menstrual impurity period”  

**How this derives logic:**  
Without the tree, you might guess the IF.  
With the tree, the **IF sits at the pivot** (male birth completed on one side), and the **THEN sits on the other side** (impure seven days).

**Beginner tip:** If you only remember one thing from Step C:  
**Find the pivot word that finishes the “when,” then read the “then” on the other half.**

---

### Step D — Extract WHEN and THEN phrases  
**Question it answers:** *What are the raw ingredients of the rule?*

**Why it helps:** You list only phrases the tree (and Hebrew) actually contain—no inventing.

| Role | Lev 12 male example | Gloss |
|------|---------------------|--------|
| WHEN | וְיָלְדָה זָכָר / veyaledah zakhar | and she bears a male |
| THEN (time) | שִׁבְעַת יָמִים / shiv'at yamim | seven days |
| THEN (status) | וְטָמְאָה / vetam'ah | and she shall be impure |
| Reference | כִּימֵי נִדַּת… / kimei niddat… | as the days of her niddah… |

Female path (v5) parallels this with נְקֵבָה / nekevah / “female” and longer times.

**How this derives logic:**  
You now have **named Lego bricks**. Later tables only snap these bricks together.

---

### Step E — Choose how to **package** the logic  
**Question it answers:** *What shape fits this unit?*

**Why it helps:** Different laws need different containers:

| Shape | Use when… | Lev 12 use |
|-------|-----------|------------|
| **Decision table** | Clear parallel cases | Male row vs female row |
| **State machine** | Status changes over days/events | impure → sit period → pure |
| **Rules** | Extra constraints that span cases | “No sanctuary until days complete” |

**How this derives logic:**  
You stop stuffing everything into one vague paragraph. Each format answers a different question cleanly.

---

### Step F — Fill the tables (always HE + translit + EN)  
**Question it answers:** *What is the actual rulebook?*

#### Decision table (idea)

| Row | WHEN | THEN |
|-----|------|------|
| Male | bears **זָכָר / zakhar / “male”** | impure **7** days, then sit **33** days; circumcision day **8** for the boy |
| Female | bears **נְקֵבָה / nekevah / “female”** | impure **14** days, then sit **66** days |

#### State machine (idea)

Statuses for the mother:

```text
[before birth]
      |
      |  birth (male or female)
      v
[impure]  ----(end of 7 or 14 days)---->  [sit in "bloods of purity"]
      |                                              |
      |                         days complete        |
      v                                              v
                                 [ready for offering]
                                              |
                         bring offerings + priest atones
                                              v
                                           [pure]
```

Hebrew anchors for statuses include:

- טָמְאָה / tam'ah / “impure”  
- תֵּשֵׁב בִּדְמֵי טָהֳרָה / teshev bedemei tahorah / “she shall sit in bloods of purity”  
- וְטָהֲרָה / vetaharah / “and she shall be pure”  

**How this derives logic:**  
Numbers and statuses are no longer “vibes.” They are **fields** tied to Hebrew, ready to test.

---

### Step G — Optional Oral notes (later texts), always named  
**Question it answers:** *Do later teachers explain something—and did we keep that separate?*

**Why it helps:** The Written Torah may state **what**; the Talmud may discuss **why**.  
We never silently rewrite Written numbers using a later explanation.

**Lev 12 example:**  
Talmud **Niddah 31a** asks why the Torah gives seven for a male and fourteen for a female.  
That is an **explanation layer**.  
The **14** already exists in Written Hebrew: שְׁבֻעַיִם / shevu'ayim / “two weeks.”

**Beginner tip:** If it’s not in Leviticus itself, label it Oral and cite tractate + location.

---

### Step H — Write **scenarios** (tests without coding)  
**Question it answers:** *If I apply the rulebook to a story, do I get the right answers?*

**Example scenario (male path):**

| Check | Expected | Hebrew anchor |
|-------|----------|----------------|
| Impure days | 7 | שִׁבְעַת יָמִים / shiv'at yamim / “seven days” |
| Sit days | 33 | שְׁלֹשִׁים + שְׁלֹשֶׁת / thirty + three |
| Circumcision | day 8 | בַּיּוֹם הַשְּׁמִינִי / bayom hashemini / “on the eighth day” |
| After offerings | pure | וְטָהֲרָה / vetaharah / “and she shall be pure” |

**How this derives logic:**  
Scenarios force honesty. If a scenario needs a fact you can’t point to in Hebrew, the rule isn’t ready.

---

### Step I — Leakage checklist  
**Question it answers:** *Did English sneak in as a fake source? Did we leave bare Hebrew?*

Checklist (plain):

- [ ] No condition exists **only** in English  
- [ ] Every number cites Hebrew number-words  
- [ ] Every Hebrew bit has translit + English  
- [ ] Confidence labels are filled  
- [ ] Hebrew vs English conflicts noted (if any)  

**How this derives logic:**  
This is quality control so the workbook stays trustworthy for English-only readers **and** text-faithful.

---

### Step J — Freeze (optional later code)  
**Question it answers:** *Is the rulebook stable enough that software may only **read** it, not reinvent it?*

Until `status: frozen`, treat the unit as editable study notes.  
After freeze, any program must **load** the YAML—not invent new day counts.

---

## Part 6 — Full Lev 12 story in plain English  
*(still anchored in Hebrew)*

1. **Header** (v1–2a): God tells Moses to speak to Israel—setup, not a purity timer.  
2. **Male birth** (v2–4):  
   - IF she bears **זָכָר / zakhar / “male”**  
   - THEN mother is impure **7** days (like niddah)  
   - On day **8**, the boy is circumcised  
   - Mother sits **33** more days in “bloods of purity,” with limits on holy things / sanctuary  
3. **Female birth** (v5):  
   - IF **נְקֵבָה / nekevah / “female”**  
   - THEN impure **14** days, sit **66** days (same pattern, longer Hebrew numbers)  
4. **Shared ending** (v6–8):  
   - When purity days are full—for a son **or** a daughter—she brings offerings  
   - Default: lamb + bird; if she can’t afford a sheep: two birds  
   - Priest atones → she is **pure**

That whole path is what the YAML encodes **without** jumping to Python.

---

## Part 7 — How each layer depends on the one before

```text
A  Pick unit
B  Open Hebrew
C  Tree shows WHERE the IF/THEN sit
D  List the phrases (ingredients)
E  Pick containers (table / states / rules)
F  Fill containers with HE + translit + EN
G  Optional Oral explanation (labeled)
H  Test with scenarios
I  Checklist
J  Freeze when stable
```

If you skip **C (tree)**, your IF is a guess.  
If you skip **F (triples)**, an English-only reader gets lost.  
If you skip **H (scenarios)**, mistakes hide until later.

---

## Part 8 — Mini exercise (try it yourself)

Open `logic/units/lev_12_childbirth.yaml` and find **`binary_trees` → `Lev_12_2`**.

1. Find the head of the left half: **זָכָר / zakhar / “male”**.  
2. Find the duration on the right: **שִׁבְעַת יָמִים / shiv'at yamim / “seven days”**.  
3. Jump to **`decision_table` → `R_male`**. Confirm the same WHEN/THEN.  
4. Jump to **`scenarios` → `SC_male_full_path`**. Confirm expected 7 and 33.

If those three places agree, you have seen the whole derivation chain.

---

## Part 9 — What this is *not*

- Not a claim that “the Torah is a computer program.”  
- Not binding religious legal advice (unless a qualified teacher frames it that way).  
- Not a reason to ignore Jewish tradition—Oral attachments are welcome **with names**.  
- Not a substitute for learning Hebrew if you want fluency; it is a **safe bridge** so English-only readers can still follow rigorous derivation.

---

## Part 10 — Where to go next

| Goal | Open this |
|------|-----------|
| Do your first unit | Copy `logic/templates/unit_template.yaml` → `logic/units/your_name.yaml` |
| See a complete filled unit | `logic/units/lev_12_childbirth.yaml` |
| Full technical rules | `logic/SYSTEM.md` |
| Field list | `logic/SCHEMA.yaml` |
| Project-wide rules | `AGENTS.md` at the repo root |

### One-sentence summary

**We read the Hebrew with English training wheels, use the verse’s tree to find the real IF/THEN, write those rules in a clear workbook, and only then—maybe—let code follow the workbook.**

Welcome. Start with Leviticus 12, go slowly, and keep every Hebrew word paired with a transliteration and an English gloss.
