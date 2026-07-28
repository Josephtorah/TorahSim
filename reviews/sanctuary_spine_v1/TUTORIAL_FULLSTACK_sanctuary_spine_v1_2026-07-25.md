# Full-stack tutorial: Sanctuary spine V1 as declare / use architecture

### For developers · Hebrew always shown with translit + English

**Date:** 2026-07-25  
**Folder:** `reviews/sanctuary_spine_v1/`  
**Kind:** engineering walkthrough of the completed V1 demo  
**Not:** binding religious law · not a production runtime  

**Beginner version (no programming):** `TUTORIAL_BEGINNERS_sanctuary_spine_v1_2026-07-25.md`  
**Method deep-dive (any book):** `../../logic/TUTORIAL_TORAH_AS_PROGRAM_FULLSTACK_2026-07-25.md`  
**Five-book map:** `../../logic/TUTORIAL_FIVE_BOOKS_INTERLOCK_FULLSTACK_2026-07-25.md`

---

## Table of contents

1. [Executive summary](#1-executive-summary)  
2. [Repo package map](#2-repo-package-map)  
3. [Architecture of the demo](#3-architecture-of-the-demo)  
4. [Domain model (free names)](#4-domain-model-free-names)  
5. [Layer: Install (Exodus writes)](#5-layer-install-exodus-writes)  
6. [Layer: Operate (Lev 1 cattle olah)](#6-layer-operate-lev-1-cattle-olah)  
7. [Layer: Ops (Num cloud FSM)](#7-layer-ops-num-cloud-fsm)  
8. [Layer: Recompile (Deut place)](#8-layer-recompile-deut-place)  
9. [How variables were derived](#9-how-variables-were-derived)  
10. [Trees, glue, and particles](#10-trees-glue-and-particles)  
11. [Mapping to software systems](#11-mapping-to-software-systems)  
12. [Resolve matrix (copy-paste reference)](#12-resolve-matrix-copy-paste-reference)  
13. [Dry-run and verification](#13-dry-run-and-verification)  
14. [What we did *not* build](#14-what-we-did-not-build)  
15. [How to extend V1](#15-how-to-extend-v1)  
16. [Reading order for implementers](#16-reading-order-for-implementers)

---

## 1. Executive summary

### Claim under test

```text
Written Torah can be modeled as sequential phases that
WRITE sanctuary symbols, then READ them under new jobs,
without reinstalling the machine at each phase.
```

### V1 vertical slice (frozen)

```text
Exod install  →  Lev 1:1–9 operate  →  Num 9:15–23 + 10:11–13 ops  →  Deut 12:5–14 recompile
                 (~42 verses, ~10 free names)
```

### Outcome

| Layer | Deliverable | Status |
|-------|-------------|--------|
| Charter | Verse + name freeze | done |
| Symbol WRITES | Exod loci | done |
| Symbol USES | Lev/Num/Deut matrix | done |
| Procedure | Cattle olah pipeline | done |
| FSM | Cloud stay/go | done |
| Hub | Diagram + audit | done |

**Confidence:** free-name presence and tree splits = **tested** on cited verses; “Torah is a program” = **hypothesis** (useful architecture, not dogma).

---

## 2. Repo package map

```text
reviews/sanctuary_spine_v1/
├── README.md
├── DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md
├── DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md
├── DEMO_sanctuary_spine_v1_USES_2026-07-25.md
├── DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md
├── DEMO_sanctuary_spine_v1_CLOUD_FSM_2026-07-25.md
├── DEMO_sanctuary_spine_v1_HUB_2026-07-25.md
├── TUTORIAL_BEGINNERS_sanctuary_spine_v1_2026-07-25.md
└── TUTORIAL_FULLSTACK_sanctuary_spine_v1_2026-07-25.md  ← this file
```

**Background units (already tree_derived_v1, not re-bulked for V1):**  
`logic/units/exo_25_*` … `exo_40_*`, `lev_01_*`, `num_09_*`, `num_10_*`, `deu_12_*`

**Parser:**

```bash
python3 taamim_tree_parse.py Exod.29.4 --tree
python3 taamim_tree_parse.py Lev.1.5 --tree
python3 taamim_tree_parse.py Num.9.17 --tree
```

---

## 3. Architecture of the demo

### 3.1 Pipeline

```text
┌─────────────┐    free names     ┌─────────────┐
│  EXODUS     │ ───────────────►  │  LEV 1      │  operate
│  INSTALL    │                   │  procedure  │
│  + go-live  │ ───────────────►  │  NUM 9–10   │  ops FSM
│             │                   │  cloud      │
│             │ ──(role only)──►  │  DEUT 12    │  recompile
└─────────────┘                   └─────────────┘
```

### 3.2 Interfaces (conceptual)

| Interface | Producer | Consumers |
|-----------|----------|-----------|
| `SanctuaryEnv` | Exodus 25–40 (V1 subset) | Lev 1, Num 9–10 |
| `OlahCattleHandler` | Lev 1:1–9 | — (demo endpoint) |
| `TravelController` | Num 9 rules; 10:11–13 instance | — |
| `LandPlacePolicy` | Deut 12:5–14 | land-era worship routing |

### 3.3 Failure mode if install missing

If you delete Exodus install from the mental model:

- Lev 1 “from the Tent” / “to the entrance” / “priests” / “altar” become **unresolved free names**.  
- Num cloud has nothing authorized to cover.  
That is the interdependence the demo is built to show.

---

## 4. Domain model (free names)

### 4.1 Identity rule

```text
canonical_id  = Hebrew surface (often multi-leaf)
handle        = SYM_*  (doc convenience only)
display       = he + he_translit + en  (always)
```

### 4.2 Install set (environment)

| Handle | he | translit | en |
|--------|----|----------|-----|
| `SYM_mikdash` | מִקְדָּשׁ | *mikdash* | sanctuary |
| `SYM_tavnit` | תַּבְנִית | *tavnit* | pattern |
| `SYM_mishkan` | מִשְׁכָּן | *mishkan* | dwelling |
| `SYM_ohel_moed` | אֹהֶל מוֹעֵד | *ohel mo’ed* | Tent of Meeting |
| `SYM_petach_ohel` | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of the Tent |
| `SYM_mizbeach` | מִזְבֵּחַ | *mizbeach* | altar |
| `SYM_benei_aharon` | בְּנֵי אַהֲרֹן | *benei Aharon* | sons of Aaron |
| `SYM_kohen` | כֹּהֵן / כֹּהֲנִים | *kohen(im)* | priest(s) |
| `SYM_anan` | עָנָן | *anan* | cloud |
| `SYM_kavod` | כָּבוֹד | *kavod* | glory |

### 4.3 Recompile key

| Handle | he | translit | en |
|--------|----|----------|-----|
| `SYM_makom_yivchar` | הַמָּקוֹם אֲשֶׁר־יִבְחַר | *ha-makom asher-yivchar* | the place He will choose |

**Policy:** do **not** assert string equality with `SYM_ohel_moed`. Link as **role continuity** (`PASS_recompile`, hypothesis).

### 4.4 Result enum (resolve)

| Result | Meaning |
|--------|---------|
| `PASS` | USE resolves to prior WRITE |
| `PASS_alias` | Surface variant (e.g. האהל vs אהל מועד) |
| `PASS_recompile` | New surface, same architectural role (hypothesis) |
| `INSTALL_ONLY` | Written in Exod V1; no USE in V1 consume range |
| `LOCAL` | First declared at use module (e.g. קרבן / *korban*) |

---

## 5. Layer: Install (Exodus writes)

**Detail file:** [WRITES](DEMO_sanctuary_spine_v1_WRITES_2026-07-25.md)

### Ordered ops

```text
DECLARE_GOAL     25:8   mikdash + dwell intent
DECLARE_PATTERN  25:9   tavnit of mishkan + vessels
DESIGN           27:1   mizbeach
NAME             27:21  ohel mo'ed
APPOINT          28:1   benei Aharon / kohen
DECLARE_PLACE    29:4   petach ohel mo'ed
BIND_FUNCTION    29:42  meet/speak + olah tamid at entrance
PLACE            40:6   mizbeach ha-olah before petach
ACTIVATE         40:34–35  anan cover + kavod fill → ONLINE
```

### Example write card (pattern for all)

**Exod 29:4** — `SYM_petach_ohel`

| Field | Value |
|-------|--------|
| Linear | ואת אהרן ואת בניו תקריב אל פתח אהל מועד … |
| Top tree | **L** bring to *petach ohel mo’ed* · **R** wash |
| Op | `DECLARE_PLACE` |
| Consumers | Lev 1:3, 1:5 |

Think: `export const PETACH_OHEL_MOED = installEntrance(...)`.

---

## 6. Layer: Operate (Lev 1 cattle olah)

**Detail file:** [OLAH_CATTLE](DEMO_sanctuary_spine_v1_OLAH_CATTLE_2026-07-25.md)

### Dependency injection view

```text
function runCattleOlah(env: SanctuaryEnv, offering: CattleOlah) {
  require(env.ohel_moed.online)
  require(env.petach, env.mizbeach, env.kohanim)

  // 1:1 speech already opened law from ohel_moed
  // 1:2 type menu (local korban)
  assert(offering.type == olah && offering.class == bakar
         && offering.male && offering.tamim)

  bringer.bringTo(env.petach)           // 1:3
  bringer.leanOnHead(offering)          // 1:4
  bringer.slaughter(before_YHWH)        // 1:5 L
  env.kohanim.dashBlood(env.mizbeach)   // 1:5 R
  bringer.flayAndCut()                  // 1:6
  env.kohanim.fireAndWood(env.mizbeach) // 1:7
  env.kohanim.arrangeParts()            // 1:8
  bringer.wash(); env.kohanim.smoke()   // 1:9
}
```

The pseudo-code is **pedagogy**. Evidence is Hebrew + trees in Step 4.

### Critical structural fact: Lev 1:5

| Tree arm | Content | Agent |
|----------|---------|-------|
| **LEFT** | slaughter cattle-young before YHWH | bringer |
| **RIGHT** | sons of Aaron the priests + blood + altar + petach | priests |

Cantillation enforces **agent partition**. That is stronger than an English outline.

### Local vs imported

| Kind | Example |
|------|---------|
| Imported env | ohel, petach, mizbeach, kohanim |
| Local declare | קָרְבָּן / *korban* (first major legal surface Lev 1:2) |
| Local guards | זָכָר / *zakhar* male · תָּמִים / *tamim* unblemished |

---

## 7. Layer: Ops (Num cloud FSM)

**Detail file:** [CLOUD_FSM](DEMO_sanctuary_spine_v1_CLOUD_FSM_2026-07-25.md)

### Symbol job migration

| Phase | `SYM_anan` job |
|-------|----------------|
| Exod 40 | Presence / go-live flag |
| Num 9–10 | Travel control input |

Same object, **new interface** — common in real systems (feature flag → scheduler signal).

### States

```text
CAMPED  ← cloud dwells on mishkan
MARCHING ← cloud lifted from tent/mishkan
SETTLE  ← cloud dwells at place P → CAMPED(P)
```

Authority wrapper: עַל־פִּי יְהוָה / *al-pi YHWH* / by the mouth of YHWH.

### Key verse AST: Num 9:17

| LEFT | RIGHT |
|------|-------|
| lift cloud from tent → journey | dwell cloud at place → camp |

### Instance log: Num 10:11–13

```text
timestamp: year 2 month 2 day 20
event:     na'alah he-anan me-al mishkan ha-edut
action:    Israel marches from Sinai
settle:    cloud in Paran
```

= execution of Num 9 rules, not a second control plane.

---

## 8. Layer: Recompile (Deut place)

**Detail file:** [USES](DEMO_sanctuary_spine_v1_USES_2026-07-25.md) § makom

### Problem

Deut 12:5–14 uses:

הַמָּקוֹם אֲשֶׁר־יִבְחַר יְהוָה / *ha-makom asher-yivchar YHWH* / “the place YHWH will choose”

not the string אֹהֶל מוֹעֵד.

### V1 resolution policy

```text
PASS_recompile:
  role  = authorized cult / name-of-YHWH place
  surface_match = false
  confidence = hypothesis
```

### Software analogy

```text
// Exodus era
const place = portableSanctuary.ohelMoed

// Deuteronomy era (land)
const place = landConfig.placeYHWHWillChoose  // migration of policy key
```

Do not silently rewrite history as if Exodus used Deut’s phrase.

---

## 9. How variables were derived

### 9.1 Not forward-only magic

| Pass | Question |
|------|----------|
| Forward | “Does this look like an install?” (Exod build language) |
| Backward | “This free name in Lev/Num — where written?” |
| Together | WRITE/USE matrix |

Cross-book **variablehood** requires **reuse**, not a single install-looking sentence.

### 9.2 Not tree-only

| Tree gives | Tree does not give |
|------------|-------------------|
| Multi-leaf chunks | Cross-book resolve |
| Agent L/R splits | Seed vs install |
| Leaf path + mark | “This is a global symbol” |

### 9.3 Pipeline used in V1

```text
1. Charter freeze (verses + names)
2. WRITE table from Exod
3. USE hits in Lev/Num/Deut + paths
4. Procedure deepening (olah)
5. FSM deepening (cloud)
6. Hub + success audit
```

Prior art reused: Lev 1 leaf ledger, Onkelos/OSHB disambig, Phase B write sites under `reviews/`.

---

## 10. Trees, glue, and particles

### 10.1 Path notation

`L` / `R` = binary children · `C0`… = flat multi-child index.

Example: Lev 1:5 path `RLLRC2` ≈ הַכֹּהֲנִים / *ha-kohanim* / the priests.

### 10.2 Glue

| Token | Job |
|-------|-----|
| את / *et* | Definite object marker → following NP is payload |
| אל / *el* | “to” → often place |
| על / *al* | “on” → often altar / fire |
| מן / *min* | “from” → type source |

**את is not a variable.** BR particle school (את / גם / אך / רק) is dual-track **include/limit**, not a free-name detector. See `../RESEARCH_BR_particles_2026-07-21.md`.

### 10.3 Soft heuristics (not gates)

```text
preposition|et + content NP  →  candidate payload
multi-leaf with weak first mark + strong last mark → phrase chunk
reuse without redefine → variable
```

---

## 11. Mapping to software systems

| Torah V1 piece | Software analogue | Fit quality |
|----------------|-------------------|-------------|
| Exod 25–40 install | Infra as code + deploy | Strong |
| Free names | Exported symbols / env vars | Strong |
| Lev 1 procedure | Application service method | Strong |
| Agent split in tree | Separate services (bringer vs priest) | Medium–strong |
| Cloud FSM | Event-driven orchestrator | Strong |
| Deut place | Config migration / multi-env | Medium (role link) |
| Seed (Gen altar) | Legacy type same name | Strong as caution |
| Ta'amim tree | Per-statement AST | Strong for structure |
| Dual-track Oral | Annotated comments / RFCs | Medium |

**Do not cargo-cult:** no claim of a historical Python VM; no English-first schema.

---

## 12. Resolve matrix (copy-paste reference)

| SYM | WRITE | USE | Result |
|-----|-------|-----|--------|
| mikdash | Exod 25:8 | — | INSTALL_ONLY |
| tavnit | Exod 25:9 | — | INSTALL_ONLY |
| mishkan | 25:9 · 40:34–35 | Num 9–10 | PASS |
| ohel_moed | 27:21 · 40:34 | Lev 1:1 (+ Num ha-ohel) | PASS / PASS_alias |
| petach_ohel | 29:4 · 29:42 · 40:6 | Lev 1:3, 1:5 | PASS |
| mizbeach | 27:1 · 40:6 | Lev 1:5–9 | PASS |
| benei_aharon | 28:1 | Lev 1:5–8 | PASS |
| kohen | 28:1 | Lev 1:5–9 | PASS |
| anan | 40:34–35 | Num 9–10 | PASS |
| kavod | 40:34–35 | — V1 use | INSTALL_ONLY |
| makom_yivchar | — | Deut 12:5,11,14 | PASS_recompile |

---

## 13. Dry-run and verification

### 13.1 Manual checklist

See [HUB §5](DEMO_sanctuary_spine_v1_HUB_2026-07-25.md) (15 checks).

### 13.2 Structural spot-checks

```bash
# Install go-live
python3 taamim_tree_parse.py Exod.40.34 --tree
# Expect top L: cloud covers ohel mo'ed; R: kavod fills mishkan

# Operate agent split
python3 taamim_tree_parse.py Lev.1.5 --tree
# Expect top L: slaughter; R: priests + blood + altar + petach

# Ops stay/go split
python3 taamim_tree_parse.py Num.9.17 --tree
# Expect top L: lift → journey; R: dwell → camp

# Recompile surface
python3 taamim_tree_parse.py Deut.12.5 --tree
# Expect makom + yivchar language, not ohel mo'ed string
```

### 13.3 Future automated dry-run (not implemented)

```text
load WRITES.yaml + USES.yaml
for each USE row:
  assert WRITE exists OR result in {INSTALL_ONLY, LOCAL, PASS_recompile}
print coverage report
```

---

## 14. What we did *not* build

| Missing | Why |
|---------|-----|
| Full Exod furniture graph | Charter cut for thin vertical slice |
| Flock/bird olah | Same pattern; deferred |
| Executable interpreter | Spec first |
| Full TIR 100% leaf roles | Aspiration |
| Forced Oral→Written merge | Project policy |

Bulk `tree_derived_v1` units remain **structure coverage**, not this demo’s deepened procedure logic.

---

## 15. How to extend V1

| Extension | Add |
|-----------|-----|
| V1.1 | Lev 1:10–17 flock/bird branches on same env |
| V1.2 | Num 10:1–10 trumpets as additional signals |
| V1.3 | Deut 12 remainder with place key held fixed |
| Tooling | `registry_dry_run.py` over Steps 2–3 tables |
| Oral | Named Sifra on Lev 1 cattle; dual-track only |

Keep charter discipline: freeze verse lists before expanding.

---

## 16. Reading order for implementers

| Order | Doc | Goal |
|------:|-----|------|
| 1 | This tutorial | Architecture + code mental model |
| 2 | [HUB](DEMO_sanctuary_spine_v1_HUB_2026-07-25.md) | Single diagram + audit |
| 3 | [CHARTER](DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md) | Scope freeze |
| 4 | WRITES → USES | Symbol table |
| 5 | OLAH_CATTLE | Procedure |
| 6 | CLOUD_FSM | Ops |
| 7 | Beginner tutorial | Teach others without jargon |
| 8 | Method tutorials in `logic/` | Generalize beyond this spine |

---

## Appendix A — One-screen pseudo system

```text
// INSTALL
SanctuaryEnv env = Exodus.install({
  mikdash, tavnit, mishkan, ohel_moed, petach,
  mizbeach, kohanim: benei_aharon,
  anan, kavod
})
env.goLive()  // 40:34–35

// OPERATE
Leviticus.runCattleOlah(env, offering)  // 1:1–9

// OPS
while (wilderness) {
  if (env.anan.lifts()) Israel.march()
  if (env.anan.dwells(at)) Israel.camp(at)
}

// RECOMPILE (land)
LandPolicy.place = "where YHWH will choose"  // not env.ohel_moed string
```

---

## Appendix B — Confidence legend

| Label | Use |
|-------|-----|
| tested | Hebrew surface + parse observed in cited verse |
| hypothesis | Architectural packaging (FSM ids, recompile role link) |
| open | Not claimed in V1 |

---

## Changelog

- 2026-07-25: Full-stack tutorial for completed sanctuary spine V1 demo package.
