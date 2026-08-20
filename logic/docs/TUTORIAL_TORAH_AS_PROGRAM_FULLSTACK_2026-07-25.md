# Tutorial: Torah as program — declare / use variables across books

### For full-stack developers · You do **not** need to speak Hebrew

**Date:** 2026-07-25  
**Kind:** engineering tutorial — experimental model, **not** binding religious law  
**Status:** living  
**Worked spine:** Exodus installs sanctuary → Leviticus 1 operates  
**Repo:** (private workshop)  

On substantive update: rename to today’s date and fix in-repo links.

---

## Table of contents

1. [Who this is for](#1-who-this-is-for)  
2. [The engineering mental model](#2-the-engineering-mental-model)  
3. [Hard rules (do not skip)](#3-hard-rules-do-not-skip)  
4. [Glossary (seed, write, pointer, leaf…)](#4-glossary-seed-write-pointer-leaf)  
5. [Repo map](#5-repo-map)  
6. [End-to-end pipeline](#6-end-to-end-pipeline)  
7. [Phase 0 — Pick a use module](#7-phase-0--pick-a-use-module)  
8. [Phase A — Leaf-level variable extraction](#8-phase-a--leaf-level-variable-extraction)  
9. [Phase A+ — Disambiguate hard leaves](#9-phase-a--disambiguate-hard-leaves)  
10. [Phase B — Resolve write-sites](#10-phase-b--resolve-write-sites)  
11. [Worked example A — Entrance of the Tent](#11-worked-example-a--entrance-of-the-tent)  
12. [Worked example B — Sons of Aaron / priests](#12-worked-example-b--sons-of-aaron--priests)  
13. [Worked example C — Local declare (`קרבן`)](#13-worked-example-c--local-declare-קרבן)  
14. [How this compares to normal software](#14-how-this-compares-to-normal-software)  
15. [Other Torah spines that do the same thing](#15-other-torah-spines-that-do-the-same-thing)  
16. [Commands cheat sheet](#16-commands-cheat-sheet)  
17. [Artifact checklist (what to write down)](#17-artifact-checklist-what-to-write-down)  
18. [Common mistakes](#18-common-mistakes)  
19. [What we have *not* built yet](#19-what-we-have-not-built-yet)  
20. [Practice exercise](#20-practice-exercise)  
21. [Further reading in this repo](#21-further-reading-in-this-repo)

---

## 1. Who this is for

You are a **full-stack developer**. You understand:

- declare / initialize vs read / call  
- modules, imports, env vs app config  
- ASTs / parse trees  
- provenance and “don’t invent state”

You may **not** know Hebrew. That is fine. This project always stores:

```text
he  +  he_translit  +  en
```

Example:  
**אֹהֶל מוֹעֵד** / *ohel mo’ed* / “Tent of Meeting”

**Hebrew is the source of truth.** English is for reading and debugging only.

---

## 2. The engineering mental model

### 2.1 One-sentence product

> Treat later Torah as **code that resolves names** written by earlier Torah — using **content pointers** (shared Hebrew names, places, “as commanded,” narrative end-state), not modern verse IDs.

### 2.2 Stack metaphor (hypothesis, useful, not dogma)

```text
Genesis      →  world boot / seed data / people graph
Exodus       →  install nation + sanctuary machine (symbol table write)
Leviticus    →  apps / procedures on that machine (name resolve + local types)
Numbers      →  ops / load tests / journey with machine
Deuteronomy  →  recompile / migration brief for land life
```

### 2.3 The pattern you will implement by hand

```text
WRITE (declare / install)          USE (read / operate)
─────────────────────────          ────────────────────
Exod 29:4  petach ohel mo'ed  →   Lev 1:3  bring to petach ohel mo'ed
Exod 28:1  benei Aharon office →   Lev 1:5  benei Aharon ha-kohanim act
Exod 40:34 ohel mo'ed live     →   Lev 1:1  speech FROM ohel mo'ed
```

**Critical:** Leviticus 1 does **not** rebuild the Tent. It **resolves free names**.

### 2.4 Two scopes of “variable”

| Scope | Like | Example |
|-------|------|---------|
| **Environment / install** | Process env, infra, DI container | Tent, altar, priests, presence online |
| **App / procedure local** | Function locals, request DTO | `קרבן` / *korban* / offering type menu in Lev 1:2 |
| **Seed** | Legacy constant later specialized | Noah’s altar (Gen 8:20) vs Tent altar (Exod 27/40) |

---

## 3. Hard rules (do not skip)

| # | Rule | Why |
|---|------|-----|
| 1 | **Derive from Hebrew**, never from English alone | English is `[EN-AID]` |
| 2 | **Trees first** (ta'amim / cantillation) | Structure before IF/THEN narrative |
| 3 | **Every Hebrew string** has translit + English next to it | Owner is English-fluent only |
| 4 | **No silent Oral merge** | Onkelos/Sifra = dual-track, named locus |
| 5 | **Label confidence** | `tested` / `hypothesis` / `open` / `failed` |
| 6 | **Not binding religious law** unless product owner asks that frame | Experimental models |
| 7 | **No per-verse hacks** in the ta'amim parser | Bump rule version instead |
| 8 | **Do not invent rules in Python** | Code interprets frozen logic docs later; derivation stays in YAML/docs |

Standing defaults: `reviews/STANDING_DECISIONS.md` · method: `logic/SYSTEM.md`.

---

## 4. Glossary (seed, write, pointer, leaf…)

### 4.1 Software-shaped terms we use

| Term | Plain meaning | Dev analogy |
|------|---------------|-------------|
| **Surface** | Exact Hebrew string in the verse | Source token text |
| **Leaf** | One word node in the cantillation tree | AST leaf |
| **Path** | Address from root: `L`, `R`, `C0`… | XPath / AST path |
| **Constituent** | Flat group of leaves under one phrase parent | Multi-token identifier |
| **Variable / free name** | Reused content key (usually multi-leaf) | Exported symbol / env key |
| **Write / declare / install** | Locus that sets up the system meaning | Definition / constructor |
| **Seed** | Earlier similar language, different job/layer | Legacy API / precursor type |
| **Use / read** | Later locus that assumes the name | Import / dereference |
| **Pointer** | *How* use hooks to write | Link kind / edge type |
| **PASS** | Use has a prior write that resolves it | Successful symbol resolve |
| **LOCAL** | First born in this module | Local declaration |
| **PASS_layered** | Seed exists *and* install exists; use needs install | Override / specialized binding |
| **Dual-track Oral** | Named midrash/Targum beside Written | Comment / secondary source, not overwrite |

### 4.2 Pointer types (Written→Written)

From `reviews/architecture/ARCHITECTURE_pass2_pointers_2026-07-19.md`:

| ID | Meaning | Example |
|----|---------|---------|
| **P-NAME** | Same proper/class name | בני אהרן / *benei Aharon* / sons of Aaron |
| **P-PLACE** | Same place key | פתח אהל מועד / entrance of Tent of Meeting |
| **P-STATE** | Narrative continuity / live system | After Exod 40 glory fills → Lev 1 speaks *from* Tent |
| **P-JOIN** | Shared class word across tables | מזבח / altar; עלה / burnt offering family |
| **P-CMD** | “as YHWH commanded” style bind | Later execution tied to prior payload |
| **P-MEM** | Remember / do not forget | Mostly Deuteronomy |
| **P-PARALLEL** | Restated law | Shabbat Exod 20 ↔ Deut 5 |

### 4.3 Cantillation (ta'amim) in one paragraph

Hebrew Bible verses carry **cantillation marks** (musical + hierarchical punctuation).  
Our parser ranks marks (emperors → kings → dukes → conjunctives) and builds a **binary-ish phrase tree** by continuous dichotomy (v1 rules).

- **Stronger disjunctive** → higher split  
- **Conjunctives / no mark** → glue words into a phrase  
- **Etnachta** often ≈ major mid-verse rest (top-ish LEFT/RIGHT)

You do **not** need to memorize every mark name. You need:

1. Full tree exists (all marks participated).  
2. Each leaf has `mark_id`, `rank`, `path`.  
3. Multi-word **names** usually sit as bound leaves under one head.

---

## 5. Repo map

| Path | Role |
|------|------|
| `Data/Gen.xml` … `Deut.xml` | Hebrew source (OSHB-style) |
| `taamim_tree_parse.py` | Interpreter of versioned ta'amim rules |
| `logic/taamim_rules/CURRENT` | Active rule version (`v1`) |
| `logic/units/*.yaml` | Pre-Code logic units (draft tree_derived_v1 bulk exists) |
| `logic/SYSTEM.md` | Pre-Code method |
| `reviews/REGISTRY_sanctuary_v0_2026-07-24.md` | Sanctuary declare/use storyboard |
| `reviews/LEDGER_lev_01_phaseA_LEAF_2026-07-24.md` | Lev 1 leaf ledger |
| `reviews/DISAMBIG_lev_01_onkelos_oshb_2026-07-24.md` | Onkelos + OSHB sense pass |
| `reviews/PHASE_B_lev_01_write_sites_2026-07-24.md` | Write-site matrix |
| `artifacts/reprocess_book_from_trees.py` | Bulk tree→STEP unit writer (not the variable resolver) |

---

## 6. End-to-end pipeline

```text
┌─────────────────────────────────────────────────────────────┐
│ 0. Choose USE module (e.g. Lev 1 offerings)                 │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ A. LEAF LEDGER (Written structure)                          │
│    verse → full ta'amim tree → every leaf path+mark         │
│    → multi-leaf free names from Hebrew surfaces             │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ A+. DISAMBIG (optional dual-track)                          │
│    OSHB lemma/morph [#IMPOSED] + Onkelos [TARGUM]           │
│    → clear homographs (עלה offering vs go-up, etc.)         │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ B. WRITE-SITE RESOLVE                                       │
│    for each free name: search earlier Torah                 │
│    → WRITE_seed / WRITE_install / LOCAL                     │
│    → pointer type + PASS | PASS_layered | LOCAL | OPEN      │
└───────────────────────────┬─────────────────────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│ C. (future) REGISTRY + DRY-RUN                              │
│    load symbols → resolve USE → print hit/miss              │
│    still no full law simulator                              │
└─────────────────────────────────────────────────────────────┘
```

**Order matters:** never start from English theology or from Oral alone.

---

## 7. Phase 0 — Pick a use module

Good first modules:

| Module | Why |
|--------|-----|
| **Lev 1** | Dense free names; clear Exod install behind it |
| Exod 40 end → Lev 1 open | Pure handoff |
| Num 1:1 Tent + date stamp | Same symbols, new ops layer |

Record:

- Book/chapter range  
- Genre (procedure / narrative / registry)  
- Expected imports (sanctuary? people? calendar?)

---

## 8. Phase A — Leaf-level variable extraction

### 8.1 Goal

For every verse in the module:

1. Parse **full** ta'amim tree (all marks).  
2. List **every leaf**: index, Hebrew, mark, rank, path.  
3. Derive **variable candidates** from Hebrew surfaces (prefer multi-leaf).  
4. **Do not** yet attach Exodus write-sites.

### 8.2 Parse a verse

```bash
cd /path/to/TorahSim

# Human-readable tree
python3 taamim_tree_parse.py Lev.1.5 --tree

# Or programmatically
python3 -c "
from taamim_tree_parse import parse_verse, tree_ascii_string
pr = parse_verse('Lev.1.5')
print(pr['status'], pr.get('rule_set_version'))
print(tree_ascii_string(pr['tree']))
for w in pr['words']:
    print(w['index'], w['mark_id'], w['rank'], w['he_plain'])
"
```

OSIS ids: `Gen.1.1`, `Exod.29.4`, `Lev.1.5`, `Num.1.1`, `Deut.6.4`.

### 8.3 Path notation

From the root of the verse tree:

| Token | Meaning |
|-------|---------|
| `L` / `R` | Left / right child of a binary split |
| `C0`, `C1`, … | Index in a flat multi-child (conjunctive chain) |

Example (Lev 1:5): path `RLLRC2` might address  
**הַכֹּהֲנִים** / *ha-kohanim* / “the priests” (pashta leaf).

### 8.4 How a variable is born (algorithm)

```text
for each verse:
  leaves = walk_tree(root)  # path + mark + he per word
  # Prefer longest multi-leaf content spans that match Hebrew keys:
  #   פתח אהל מועד, בני אהרן, לפני יהוה, ...
  # Then single content leaves:
  #   המזבח, הדם, ושחט, ...
  # Skip pure glue as variables: את, על, מן, אשר, ...
  record:
    he, he_translit, en_gloss,
    leaf_indices, paths, head_mark,
    kind: install_env | type | act | substance | ...
```

**Variable id policy:**

- Canonical identity = **Hebrew surface** (or multi-leaf span).  
- Optional handle `VAR_petach_ohel_moed` is a **filename/API convenience**, not the real name.  
- Always display `he + translit + en` with the handle.

### 8.5 What “leaf-level” adds vs top-split-only

| Top-split only | Leaf-level |
|----------------|------------|
| “Priests are on RIGHT half” | Path + mark + exact tokens |
| Easy to over-summarize | Finite address for each free name |
| Marks used then discarded in the table | Marks stored on each leaf |

**You must use leaf-level** if the goal is finite variable derivation.

### 8.6 Deliverable

A ledger document/table, e.g.:

`reviews/LEDGER_<book>_<unit>_phaseA_LEAF_YYYY-MM-DD.md`

Plus optional JSON for tooling.

Reference: `reviews/LEDGER_lev_01_phaseA_LEAF_2026-07-24.md`.

---

## 9. Phase A+ — Disambiguate hard leaves

Hebrew is morphologically dense. Same letters ≠ same job.

### 9.1 Preferred tools (decision already made on Lev 1)

| Tool | Role | Provenance tag |
|------|------|----------------|
| **OSHB lemma/morph** in `Data/*.xml` | Form family (noun 5930 vs verb 5927) | `[#IMPOSED:OSHB-morph]` |
| **Targum Onkelos** | Traditional sense of *this* verse | `[ORAL/TARGUM-Onkelos]` |
| Radak roots | Optional later | named dual-track |
| Rambam | Procedure densification later — **not** leaf naming first | `[ORAL]` |

### 9.2 Classic homographs (Lev 1)

| Surface | Risk | Resolution pattern |
|---------|------|--------------------|
| עלה / *olah* | offering vs “went up” | OSHB lemma `5930` + Onkelos עֲלָתָא |
| אשה / *isheh* | fire-offering vs “woman” | OSHB lemma `801` (not 802) + formula context |
| בני / *benei* | incomplete alone | Always multi-leaf with next name |

### 9.3 Dual-track rule

```text
Written leaf + path     = authority for structure/surface
OSHB                    = labeled form aid
Onkelos                 = labeled sense aid
English of either       = for the human only
```

Never: Onkelos English → invent VAR → force onto tree.

Reference: `reviews/DISAMBIG_lev_01_onkelos_oshb_2026-07-24.md`.

---

## 10. Phase B — Resolve write-sites

### 10.1 Goal

For each free name from Phase A:

```text
USE (module verse + path)
  → WRITE_seed? (earliest similar Hebrew, maybe different job)
  → WRITE_install? (system meaning this module needs)
  → pointer type
  → PASS | PASS_layered | LOCAL | OPEN
```

### 10.2 Search order

1. Same book earlier chapters  
2. Exodus for sanctuary installs  
3. Genesis for seeds / ambient world  
4. Numbers/Deut for later only if your USE is later  

Prefer **install sense** over first string match:

| First string | Often wrong for Lev 1 |
|--------------|------------------------|
| First `מזבח` = Gen 8:20 Noah | Lev 1 needs **Exod 27/40** Tent altar |
| First `כהן` noise | Need **Exod 28:1** Aaronic office |
| First `פתח האהל` Gen 18 | Abraham’s tent door ≠ `פתח אהל מועד` |

### 10.3 Result labels

| Result | Meaning |
|--------|---------|
| **PASS** | Clear prior install; use only resolves |
| **PASS_layered** | Seed + install both exist; use binds install |
| **LOCAL** | First born in this module (e.g. `קרבן` at Lev 1:2) |
| **OPEN** | No honest write yet |

### 10.4 Deliverable

`reviews/PHASE_B_<module>_write_sites_YYYY-MM-DD.md`

Reference: `reviews/PHASE_B_lev_01_write_sites_2026-07-24.md`.

---

## 11. Worked example A — Entrance of the Tent

### 11.1 WRITE — Exod 29:4

**Plain English:** Bring Aaron and his sons to the **entrance of the Tent of Meeting** and wash them.

**Hebrew key:**  
פֶּתַח אֹהֶל מוֹעֵד / *petach ohel mo’ed* / “entrance of the Tent of Meeting”

**Tree (top):**

| Arm | Role |
|-----|------|
| LEFT | Bring Aaron & sons **to petach ohel mo’ed** |
| RIGHT | Wash them with water |

**Related writes:**

| Locus | Role |
|-------|------|
| Exod 29:42 | Continual offering **at** entrance; meet/speak function |
| Exod 40:6 | Place olah altar before entrance |
| Exod 40:34–35 | Presence online |

### 11.2 USE — Lev 1:3

**Plain English:** If cattle burnt offering… bring it to the **entrance of the Tent of Meeting**… before YHWH.

**Tree (top):**

| Arm | Role |
|-----|------|
| LEFT | IF olah from cattle, male, unblemished… |
| RIGHT | Bring to **petach ohel mo’ed** … before YHWH |

**Variable derivation:**

1. Multi-leaf span on RIGHT: פתח + אהל + מועד  
2. Same surface as Exod 29:4  
3. Onkelos: entrance of Tent of Meeting  
4. Phase B: WRITE_install = Exod 29:4 (+ 29:42, 40:6)  
5. Pointer: **P-PLACE** (+ **P-STATE** after Exod 40)

**Program reading:**

```text
// Exodus
install PETACH_OHEL_MOED = "entrance of Tent of Meeting"

// Leviticus 1
if offering.kind == olah && animal == cattle:
    bring(offering, to=PETACH_OHEL_MOED)
```

The “code” is metaphor; the **evidence** is Hebrew identity + tree placement + earlier install.

---

## 12. Worked example B — Sons of Aaron / priests

### 12.1 WRITE — Exod 28:1

**Plain English:** Bring Aaron and his sons to **priest for Me**; names Nadav, Avihu, Eleazar, Itamar — **sons of Aaron**.

**Hebrew:**  
בְּנֵי אַהֲרֹן / *benei Aharon* / “sons of Aaron”  
לְכַהֲנוֹ לִי / *le-khahano li* / “to serve as priest for Me”

**Tree (top):** LEFT = appoint to priest; RIGHT = name list ending **בני אהרן**.

### 12.2 USE — Lev 1:5

**Plain English:** Slaughter… then **sons of Aaron the priests** bring blood and dash it on the altar… at the entrance of the Tent.

**Tree (top + leaf insight):**

| Arm | Content |
|-----|---------|
| LEFT | **Slaughter** animal before YHWH |
| RIGHT | **Priests** + blood + altar + entrance |

Leaf-level: operator chunk **בני אהרן הכהנים** under RIGHT domains (pashta etc.); slaughter leaf separate on LEFT.

**Derivation:**

1. Multi-leaf office phrase at use  
2. WRITE_install = Exod 28:1 (+ Exod 29 investiture)  
3. Pointer: **P-NAME**  
4. Result: **PASS** — no new priest install in Lev 1  

**Program reading:**

```text
// Exodus 28–29
install OPERATORS = SonsOfAaron.asPriests()

// Leviticus 1:5
slaughter(animal)                    // bringer side
OPERATORS.applyBlood(animal, altar)  // priest side
```

---

## 13. Worked example C — Local declare (`קרבן`)

Not everything is an Exodus import.

| Item | Detail |
|------|--------|
| Hebrew | קָרְבָּן / *korban* / “offering / approach-gift” |
| USE | Lev 1:2 type menu open |
| WRITE in Torah | **First hit: Lev 1:2** (not in Gen/Exod as this noun) |
| Result | **LOCAL declare** |

**Program reading:**

```text
// Leviticus module
type Korban = ...
function openOfferingMenu(korban: Korban) { ... }

// Environment still imported:
//   ohel_moed, petach, kohanim, mizbeach from Exodus
```

This is normal software: **libraries imported**, **domain types declared locally**.

---

## 14. How this compares to normal software

### 14.1 Similar

| Software | Torah model |
|----------|-------------|
| Init infrastructure once | Exodus sanctuary install |
| App code uses service names | Lev free names |
| Env vars / DI | Install symbol table |
| Don’t re-bootstrap DB in every handler | Don’t rebuild Tent in every olah |
| Module-local types | `קרבן`, north-side, ash place |
| AST for structure | Ta'amim tree |
| Provenance in PRs | `source` tags + confidence |

### 14.2 Different

| Software | Torah model |
|----------|-------------|
| You invent identifiers | Identifiers are **Hebrew surfaces** |
| `import` is explicit syntax | Pointers are **content** (name/place/state) |
| One definition site enforced by compiler | Human/search resolve; seeds vs installs |
| Types are formal | Types are phrase/lemma families (hypothesis grade early) |
| Runtime executes | We currently **specify**; runtime is future |

### 14.3 What not to cargo-cult

- Do not force every narrative into `if/else`.  
- Do not treat English study Bibles as schema.  
- Do not claim “Torah is Python” as a fact — claim **checkable declare/use maps**.  
- Do not merge Targum into Written rows silently.

---

## 15. Other Torah spines that do the same thing

| WRITE | USE | Notes |
|-------|-----|-------|
| Exod 25–40 sanctuary | Lev 1–16 rites | Cleanest spine |
| Exod 40 presence | Num 9–10 cloud march | P-STATE |
| Exod 12 Pesach | Num 9, Deut 16 | Festival recompile |
| Exod 20 / Deut 5 | Later “keep/remember” | P-PARALLEL / P-MEM |
| Gen 17 brit | Later covenant memory | Seed → national API |
| Num 35 refuge | Deut 4, 19 | Law restatement |
| Lev 23 calendar | Num 28–29 schedules | Registry join |

Start with **sanctuary**; expand once the method is muscle memory.

---

## 16. Commands cheat sheet

```bash
# Tree for any verse
python3 taamim_tree_parse.py Exod.29.4 --tree
python3 taamim_tree_parse.py Lev.1.5 --tree

# Golden parser tests
python3 taamim_tree_parse.py --test

# Bulk unit rebuild (tree_derived STEPs — not variable resolve)
python3 artifacts/reprocess_book_from_trees.py --book lev --phase C

# Optional: Onkelos via Sefaria API (network)
# https://www.sefaria.org/api/texts/Onkelos_Leviticus.1?context=0
```

OSHB morph sample (in XML):

```xml
<w lemma="m/168" morph="HR/Ncmsc">מֵ/אֹ֥הֶל</w>
<w lemma="4150" morph="HNcmsa">מוֹעֵ֖ד</w>
```

= from + tent construct, then *mo’ed*.

---

## 17. Artifact checklist (what to write down)

For each module pass, produce:

### Phase A ledger (required)

- [ ] Every verse: linear Hebrew + translit  
- [ ] Every leaf: `i`, `path`, `rank`, `mark_id`, `he`, `he_translit`, `en`  
- [ ] Variable table: Hebrew span, kind, verse list, sample paths  
- [ ] Full `tree_ascii` available (inline or collapsible)  
- [ ] `rule_set_version: v1` (or current)  
- [ ] Confidence labels  

### Phase A+ disambig (when homographs)

- [ ] OSHB lemma/morph cited with `#IMPOSED`  
- [ ] Onkelos verse quote: Aramaic + translit + English  
- [ ] Verdict: `cleared` / `still_open`  

### Phase B matrix (required for cross-book claim)

- [ ] USE locus + path  
- [ ] WRITE_seed (if any)  
- [ ] WRITE_install (if any)  
- [ ] Pointer type  
- [ ] PASS / PASS_layered / LOCAL / OPEN  

### Always

- [ ] Never bare Hebrew  
- [ ] Not binding law disclaimer  
- [ ] Dated filename per `STANDING_DECISIONS` §0  

---

## 18. Common mistakes

| Mistake | Fix |
|---------|-----|
| Derive variables from English summaries | Start from leaves |
| Use only top LEFT/RIGHT | Record full leaf paths |
| First string match = install | Prefer system install locus; mark seeds |
| Treat Noah’s altar as Tent altar | `PASS_layered` |
| Silent Onkelos merge into Written | Dual-track section |
| Invent STEPs in Python | Docs/YAML first |
| `VAR_*` without Hebrew | Always triple `he/translit/en` |
| Claim runtime exists | We have specs + parsers; not a VM yet |
| Force Gen import into every Lev unit | Ambient world ≠ unit `depends_on` |

---

## 19. What we have *not* built yet

| Exists | Does not exist (yet) |
|--------|----------------------|
| Ta'amim parser | Full law interpreter / VM |
| 209 draft tree_derived units | Live global registry process |
| Lev 1 Phase A leaf ledger | Automatic cross-book linker for all books |
| Lev 1 Phase B write matrix | Scenario executor with world state |
| Onkelos disambig pass (Lev 1) | Offline Onkelos dump in `Data/` (optional) |

Honest status: **specification + structure pipeline**, not production runtime.

---

## 20. Practice exercise

Do this for **one** free name end-to-end (suggested: altar / `מזבח`).

1. Parse `Lev.1.5 --tree`.  
2. Find every leaf path that is altar-related (`המזבח`, etc.).  
3. Record Hebrew + path + mark.  
4. Find WRITE_seed (hint: Gen 8:20) and WRITE_install (hint: Exod 27:1, 40:6).  
5. Assign pointer type + `PASS_layered`.  
6. Write 10 lines: “How a full-stack dev should read this as declare/use.”

Compare your notes to `PHASE_B_lev_01_write_sites_2026-07-24.md` §1.3.

---

## 21. Further reading in this repo

| Doc | When |
|-----|------|
| `logic/SYSTEM.md` | Pre-Code overall |
| `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md` | Tree → boot steps (Gen day 4) |
| `logic/TAAMIM_TREE_PARSER.md` | Parser versioning |
| `reviews/architecture/ARCHITECTURE_pass2_pointers_2026-07-19.md` | Pointer catalog |
| `reviews/architecture/ARCHITECTURE_pass3_registries_2026-07-19.md` | Type registries |
| `reviews/REGISTRY_sanctuary_v0_2026-07-24.md` | Sanctuary storyboard |
| `reviews/LEDGER_lev_01_phaseA_LEAF_2026-07-24.md` | Full leaf ledger |
| `reviews/DISAMBIG_lev_01_onkelos_oshb_2026-07-24.md` | Sense pass |
| `reviews/PHASE_B_lev_01_write_sites_2026-07-24.md` | Write matrix |
| `reviews/STANDING_DECISIONS.md` | Project defaults |

---

## Appendix — One diagram to remember

```text
                    ┌──────────────────────┐
                    │  Hebrew verse        │
                    │  + all ta'amim marks │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │  Full phrase tree    │
                    │  leaves + paths      │
                    └──────────┬───────────┘
                               ▼
              ┌────────────────┴────────────────┐
              ▼                                 ▼
     multi-leaf free names              glue / local acts
     (ohel, petach, kohanim…)           (samakh, shachat…)
              │
              ▼
     optional Onkelos/OSHB sense
              │
              ▼
     search earlier Written
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   INSTALL  SEED    LOCAL
   (Exod)   (Gen)   (first here)
      │       │        │
      └───────┴────┬───┘
                   ▼
            PASS / PASS_layered / LOCAL
                   ▼
         “Torah as program” claim
         (checkable, not mystical)
```

---

## Changelog

- 2026-07-25: Initial full-stack developer tutorial for declare/use variable pipeline (leaf Phase A → disambig → Phase B), with sanctuary worked examples.
