# Progress notes — general observations (Genesis complete draft → Exodus next)

**Date:** 2026-07-20  
**Kind:** working notes / observations (not binding religious law; not frozen units)  
**Status:** session capture so next thread does not re-derive from chat  

**Context:** Full Genesis Pre-Code draft units (`logic/units/gen_*`, packages 0–6 through Joseph). Lev units already exist for opening + cattle olah (+ Lev 12 v0). Turning toward Exodus sanctuary install.

On substantive update: rename to today’s date and fix links.

---

## 1. What Genesis looked like as a whole

After walking the book as sequential Pre-Code packages (boot → garden → early humanity → flood → nations/Babel → patriarchs → Joseph), Genesis did **not** feel like disconnected tales.

**Working picture:**

- One **long run that never reboots the cosmos** after week 1.  
- Install world → test humans → nearly wipe → re-license world → register nations → follow one family → park them in Egypt.  
- Ends as a **handoff**, not a finish: people in Egypt, promises unpaid, bones to be carried up → Exodus can load.

**Logic shape by stretch:**

| Stretch | Shape |
|---------|--------|
| Gen 1:1–2:3 | Ordered **boot** (create/speech/make/name/tick/rest) |
| 2:4–3:24 | Narrative **FSM** (guard, breach, judgment, exile) |
| 4–11 | Society recovery + **registries** (lineages, nations) + language shard |
| 12–36 | Multi-generation **saga** (promise, conflict, rename, Edom dump) |
| 37–50 | Migration **pipeline** to Egypt (fault → foreign power → famine → household install) |

**Habits of the book (observed):** speech that does things; naming; kinds/lines as tables; blessing/curse as force; brother conflict; promise under delay (open tickets).

**Not found:** Leviticus-style dense korban IF tables as the main job of Genesis. Story can still be “code” as ordered state change without being casuistic law.

**Related units:** all `logic/units/gen_*.yaml` · stack map `ARCHITECTURE_genesis_stack_2026-07-21.md` · approach `GENESIS_BUILD_2026-07-20.md`.

---

## 2. What Genesis creates that Leviticus uses

**Observation:** Lev’s **tight** free names (Tent, priests, Tabernacle altar system) resolve mainly to **Exodus**. Genesis supplies **ambient prerequisites** for a full system run — not re-run inside every offering.

```text
Genesis   →  world + kinds + people + time + some moral/cosmic seeds
Exodus    →  sanctuary machine + nation/Sinai install
Leviticus →  apps (offerings, purity) assuming world + stage already exist
```

**Ambient Gen → Lev (examples):**

| Genesis “export” (conceptual) | How Lev leans on it |
|-------------------------------|---------------------|
| Day cycle / mo'adim seed / seasons | Time fabric for day-counts and calendar ambient |
| Living kinds (*le-mino*), behemah/flock/bird world | Offerable animals only make sense if creatures exist by class |
| *Adam* / male–female / image | “Person when offers”; male cattle; human blood seriousness |
| Blood = life (flood covenant) | Deep warrant; Lev writes blood *procedures* |
| Israel family graph | “Speak to the children of Israel” (people key; Pass 4 GEN_SEED) |
| Land/covenant trajectory | Ambient history of *who* this law is for |

**Not Gen-install for Lev stage:**

- אֹהֶל מוֹעֵד / *ohel mo'ed* / Tent of Meeting  
- Aaronic priest office as system  
- Tabernacle altar/veil/incense **system** (word “altar” can be older; **system** is Exodus)

**Pass 4 reminder:** first string hit in Genesis ≠ system install book.  
**Wiring lesson:** later `import:` on Lev units should mark **ambient Gen** vs **tight Exod** separately; do not pretend each rite re-boots creation.

---

## 3. Oral Torah: Exodus vs Genesis

**Observation:** Exodus is **not** Gen-like for Oral workflow. It is closer to **Lev-like** plus narrative midrash.

| | Genesis | Exodus |
|--|---------|--------|
| Written mix | Mostly narrative | Story + **law** + **build specs** |
| Prefer first Oral open | Aggadic midrash (e.g. BR) | **Mekhilta** (halakhic midrash decoder) |
| Also heavy | Bavli/midrash peers | Mishnah, Bavli, Tosefta, Mekhilta, Rabbah-style for story |
| Local data | BR, Bavli, etc. | `mekhilta*_he.json`, Bavli/Mishnah shelves, `Exod.xml` |

**Same standing rules for both:**

- Every Mesorat haShas endpoint = **possible Oral** (job preference only chooses open order).  
- Derive from **Written Hebrew** first.  
- **Never silent-merge** Oral into Written face.  
- Do not reinvent a global Oral↔Oral index (use links / MH / cite_index).

**Exodus Oral path (working):**

```text
Written Exod → trees → Pre-Code
  narrative blocks  → optional Rabbah-style / Bavli aggadah
  law / sanctuary   → Mekhilta first → MH + Bavli → optional Mishnah/Tosefta
```

Research home: `RESEARCH_valid_oral_torah_2026-07-19.md` (§5 jobs, §6 MH).

---

## 4. Narrative vs law — owner speculation (refined)

**Owner speculation:**  
When a verse/verses are mostly **narrative**, the code is **simple**. When the verse contains **law** that Oral debates, Oral is defining **edge cases** and **database** (types, members, boundaries).

**Verdict:** **Close — adopt as working hypothesis** with refinements.

### Affirmed

- Narrative → mostly **sequential state change** (boot, FSM, saga).  
- Law → **rules + types + procedures**; Oral often fills **who/what counts**, exceptions, disputes — registry/edge-suite behavior.  
- Matches genre → logic-shape intuition (Pass 5) and Sifra/Mekhilta vs Rabbah job split.

### Refinements recorded

1. Narrative can be deep **meaning** with simple **shape** (not “trivial”).  
2. Narrative still has lots of Oral — different **job** (story color), not absence of Oral.  
3. Law Oral is not only database: also **pipeline/order** disputes.  
4. Written already has registry seeds (*le-mino*, clean/unclean ops); Oral expands/stresses.  
5. Exodus sits in the middle: plagues ≈ Gen-like sequential + midrash; mishpatim/mishkan ≈ Lev-like edges + Mekhilta/Talmud.

### Sharper one-liner (project wording)

> When Written is mostly narrative, executable logic is mainly sequential state change and Oral often elaborates story. When Written is law, executable logic is rules, types, and procedures, and Oral often defines boundaries, set membership, and hard cases — like completing a schema and edge-case suite.

---

## 5. Progress snapshot (for next thread)

| Done | Status |
|------|--------|
| Genesis packages 0–6 as draft `gen_*` units (1–50) | draft / hypothesis |
| Lev 1 opening + cattle olah (+ Lev 12 v0) | earlier draft |
| Standing: MH = possible Oral; show-all-work trees; Gen stack map | in `STANDING_DECISIONS` / logic docs |

| Natural next | Notes |
|--------------|--------|
| **Exodus started** | `EXODUS_BUILD_2026-07-20.md` · first unit `exo_01_israel_egypt_oppression` (1:1–22 narrative) |
| Next Exod block | Moses birth / Nile (ch.2) — still narrative; law later |
| Sanctuary install | Later thin blocks for Tent/priests/altar (Lev free names) |
| Oral on Exod | Mekhilta when **law**; ch.1 dual-track midwives midrash only if named |
| Optional later | Wire Lev `import:` ambient Gen vs tight Exod |

---

## 6. Related files

| File | Role |
|------|------|
| `GENESIS_BUILD_2026-07-20.md` | Genesis boot track |
| `ARCHITECTURE_genesis_stack_2026-07-21.md` | Full-stack package map + SY comparative |
| `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md` | Exod import vs Lev local |
| `ARCHITECTURE_pass5_genres_2026-07-19.md` | Genre → logic shape |
| `RESEARCH_valid_oral_torah_2026-07-19.md` | Oral policy + Mekhilta/Sifra jobs |
| `logic/SHOW_WORK_TREES_2026-07-20.md` | Trees live in unit `binary_trees` |
| `STANDING_DECISIONS.md` | Agent defaults |

---

## Changelog

- 2026-07-20: Initial notes — Gen whole-book read; Gen→Lev ambient exports; Exodus Oral vs Gen; narrative/law speculation refined.
