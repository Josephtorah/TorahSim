# Architecture discussion — Written Torah as sequential run + internal data + pointers

**Date:** 2026-07-19  
**Kind:** architecture discussion (hypothesis / working model — not binding law)  
**Status:** recorded from owner–agent conversation; open to revision  

**Related:**  
- **Pass 1 five-book scan:** `ARCHITECTURE_pass1_five_books_2026-07-19.md`  
- **Pass 2 pointers:** `ARCHITECTURE_pass2_pointers_2026-07-19.md`  
- **Pass 3 registries:** `ARCHITECTURE_pass3_registries_2026-07-19.md`  
- **Pass 4 sanctuary resolve:** `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md`  
- **Pass 5 genres:** `ARCHITECTURE_pass5_genres_2026-07-19.md`  
- **Genesis Build:** `GENESIS_BUILD_2026-07-20.md` — Gen as boot/init for runnable system  
- **Genesis full-stack packages:** `ARCHITECTURE_genesis_stack_2026-07-21.md` — segment map + Sefer Yetzirah comparative note  
- Pre-Code method: `logic/SYSTEM.md`  
- Oral coding method: `reviews/talmud_structure/ORAL_CODES_WRITTEN_2026-07-19.md`  
- Lev 1:2 research: `reviews/talmud_structure/LEV_1_2_RESEARCH_2026-07-19.md`  
- Narrative report: `reviews/talmud_structure/REPORT_lev_1_2_oral_coding_2026-07-19.md`  
- Standing decisions: `reviews/STANDING_DECISIONS.md`  
- Older, separate artifact (not this discussion): `artifacts/hebrew_bible_architecture_summary.md`

---

## Naming note

There was **no** project-level “architecture discussion” file for this model yet.  

This file is named:

```text
ARCHITECTURE_discussion_YYYY-MM-DD.md
```

per dated-filename policy (`STANDING_DECISIONS` §0). On substantive update, **rename** to the new day’s date and fix links.

Hub exceptions stay stable (`README.md`, `Agents.md`, `STANDING_DECISIONS.md`).

---

## 1. The hunch (owner)

The Written Torah may run in some **sequential order**. As it runs, it **looks for data inside the Written Torah**. Somehow the text “knows where to look” — perhaps **pointers**. Example: **Leviticus may read data from Exodus**.

Related earlier hunch (same session arc):

- Lev 1 animal classes (cattle, flock, birds, etc.) look like a **protocol for acceptable input** (what may be offered / what is out of scope).  
- Theory: Written holds the **bulk of the code**.  
- Question: does it also hold the **data** the code runs on?  
- Maybe Written is **both code and data**.

---

## 2. Working model (hypothesis)

Treat the Written Torah as:

### 2.1 Sequential program counter

Books and units unfold in order. Story and law **assume prior state**. A later passage often does not reinstall the world; it **operates on** what earlier passages already set up.

Rough book roles (architectural sketch, not theology):

| Stretch | Role in the model |
|---------|-------------------|
| Genesis | People, land, covenant patterns, early offering motifs |
| Exodus | **Install / build**: Sinai law block, **Tent of Meeting**, priesthood, altar, vessels, “as YHWH commanded” |
| Leviticus | **Run / regulate**: offerings, purity, life around that sanctuary |
| Numbers | Camp movement; stress-test the system |
| Deuteronomy | Restate / re-aim for life in the land |

So: **run forward; resolve names and prior commands by looking back (and sometimes sideways) inside the same corpus.**

### 2.2 Data inside the Written

Not only “instructions.” The corpus also carries:

- **Type / class names** (e.g. בהמה / *behemah* / animal, בקר / *bakar* / cattle, צאן / *tzon* / flock, עוף / *of* / bird)  
- **Named kinds** (e.g. turtledoves, young pigeons in Lev 1:14)  
- **Flags / constraints** (זכר / *zakhar* / male, תמים / *tamim* / unblemished)  
- **Institutions and places** (אהל מועד / *ohel mo’ed* / Tent of Meeting, altar, priests)  
- **Longer catalogs** elsewhere (e.g. Lev 11 / Deut 14 food species lists)  
- **Prior-command payloads** (“which I commanded…”)  

**Instance** data (this animal, this owner, today) is lived situation — not a ledger row inside Genesis–Deuteronomy. The Torah stores **schema, lists, and world-setup**, not the temple’s live queue.

### 2.3 Code-like material in the Written

- Casuistic cases (if olah from cattle…)  
- Sequences / pipelines (lean → slaughter → blood → flay → arrange → burn)  
- Agents and places in the rite  
- Outcomes (favor, pleasing aroma, etc.)

### 2.4 Pointers (content pointers, not modern verse IDs)

The raw Hebrew rarely uses a formal “see Exodus 25:8” citation syntax. Resolution styles that **do** exist:

1. **Shared names (namespace keys)** — later “Tent of Meeting” expects earlier Exodus definition/install.  
2. **“As commanded” formulas** — bind current act to a prior instruction.  
3. **Repeated class words** — join across passages (same Hebrew type name, multiple “tables”).  
4. **Narrative prerequisites** — you cannot fully run “bring to the Tent entrance” if the Tent was never built.  
5. **Sequence itself** — order of books and of cases (cattle → flock → bird) is part of control flow.

So: **pointers in spirit = content resolution**, not primarily chapter:verse addresses (those are later apparatus).

### 2.5 Where Oral fits

Oral (Sifra, Bavli, etc.) is **not** the first store for “what is the Tent?”  

Oral often acts as:

- **extra validators** on Written hooks (surplus מן / *min* / “from…”, מכם / *mikem* / “from you”, edge animal bans, convert vs apostate, etc.)  
- **resolution rules** when a Written key is underspecified  
- **parallel map** across Oral works (Mesorat haShas) — separate from Written→Written pointers  

Project rule unchanged: **named Oral only; never silent merge into Written.** Dual-track.

---

## 3. Lev 1 as a worked sketch of the model

### Input protocol / type channel (mostly Written local data + cases)

- **Lev 1:2** — who offers; offering as action; animal classes (behemah → bakar + tzon).  
- **Lev 1:3+** — case dispatch: if olah from cattle → male, whole, Tent door…  
- Later — flock channel; bird channel with named bird kinds.

Reading: **acceptable input types + constraints**, then channel-specific rules.

### Pipeline after accept (Written process code)

- **Lev 1:4–9** — lean, slaughter, blood, flay, arrange, burn (cattle path).  
  Less “type registry,” more **procedure on a valid instance**.

### Execution environment (often Exodus-installed state)

When Lev says priests, Tent entrance, before YHWH at the sanctuary:

- **Look back to Exodus** for install/definition of Tent, priesthood, altar world.  
- Lev **consumes** that state; it does not rebuild it from zero.

### Edge validators (often Oral on Written hooks)

Violated / worshipped / terefah / set-aside / goring animals; apostate filters; etc. — largely Oral expansions. Hooks remain Written words.

### Cross-book join example

If “animal” alone matched every use of behemah in the food lists, wild game might enter. Local Lev wording (cattle + flock) is read as locking the offering set (Sifra and Bavli pressure this). That is a **join conflict** across Written tables — resolved by local list + midrash, not by inventing types outside Hebrew.

---

## 4. Layered answer: code and data?

| Layer | Computational reading | Mostly from |
|-------|----------------------|-------------|
| Offer type (olah, …) | opcode / message type | Written case headers |
| Animal class (cattle / flock / bird) | input type / enum | Written Lev 1 |
| Male, unblemished | field constraints | Written |
| From you / Israel address | auth / membership | Written + Oral edges |
| Min-exclusions (violated, …) | validators | Oral on Written hooks |
| Lean–slaughter–blood–… | pipeline | Written procedure |
| Tent, priests, altar | environment / imported state | Often Exodus (Written) |
| Food-animal catalogs | other tables to join | Written elsewhere (Lev 11, Deut 14, …) |

**Bulk of code for this track:** Written Hebrew (project policy).  
**Bulk of type data for Lev 1 channels:** also Written in Lev.  
**Sanctuary world-state:** largely earlier Written (Exodus).  
**Hard edge lists:** often Oral.  

So: **Written can be modeled as both code and data in one corpus**, with **internal resolution**. Oral is a second resolution layer, not the primary database for Tent/cattle/flock names.

---

## 5. Exodus → Leviticus pointer default (testable)

Default architectural claim for sanctuary/offerings:

```text
Exodus  →  builds / installs  (Tent, priests, altar, commanded baseline)
Leviticus → runs / regulates (what you may bring, how, purity around that space)
```

**Test procedure (for later work):**

For each Lev unit, for every free name (Tent, priests, altar, olah, bakar, …):

1. Mark the symbol.  
2. Ask: is **definition/install** earlier in Written (often Exodus)?  
3. Log: `resolves_to: Written/Exodus…` | `local to this unit` | `Oral only` | `open`.  
4. Check whether “Lev sanctuary nouns resolve to Exodus” holds at high rate.

This produces a **Written→Written pointer map**, distinct from Mesorat haShas (Oral↔Oral) and from `cite_index` (Bavli quoting Tanakh).

---

## 6. Pre-Code modeling suggestion

When writing Lev units, consider explicit lanes:

1. **Type registry (Written-first)** — behemah / bakar / tzon / of + named birds  
2. **Constraints (Written)** — zakhar, tamim, place  
3. **Imported state (Written, often Exodus)** — Tent, priests, altar  
4. **Validators (Oral, named)** — mumar, rovea, terefah, …  
5. **Pipeline (Written)** — 1:4–9 style steps  

Keeps dual-track clean and makes the architecture falsifiable per unit.

---

## 7. Confidence labels

| Claim | Label |
|-------|--------|
| Sequential order + later use of earlier sanctuary is a useful architecture | **hypothesis / strong working model** |
| Lev 1 type names are largely Written local data | **tested** (on face of Lev 1) |
| Many edge bans are Oral on Written hooks | **tested** (Sifra §2 + Bavli cites on Lev 1:2) |
| “Pointers” = content resolution, not modern verse syntax | **tested** (observation of corpus habits) |
| Every Lev free name resolves to Exodus | **hypothesis** — needs unit-by-unit map |
| Torah “runs” as a computer program in a mechanical sense | **metaphor only** — do not overclaim as religious or technical fact |

---

## 8. What this file is / is not

**Is:** architecture discussion for Torah_Grok derivation strategy.  
**Is not:** binding religious law; not a claim that the Torah is software; not a replacement for Pre-Code YAML units or ta’amim trees.

**Next optional steps:**

- Pointer inventory for Lev 1:1–9 only (each major noun → resolve target).  
- Fold type-registry / imported-state fields into Lev 1 logic units.  
- Later: same pattern for purity spine (12–15) and whether it imports from Exod/Lev earlier blocks.

---

## 9. One-sentence summary

**Run the Written in order; treat names and prior commands as lookups into earlier Written data (often Exodus for sanctuary); keep local offering types and pipelines in Leviticus; attach Oral only as named validators when the Written key is incomplete.**
