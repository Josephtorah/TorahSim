# Architecture Pass 1 — Five Books of the Written Torah

**Date:** 2026-07-19  
**Kind:** architecture scan (hypothesis / working model — not binding law)  
**Pass:** 1 of a planned multi-pass series  
**Lens:** Sequential run + internal data + content pointers (see `ARCHITECTURE_discussion_2026-07-19.md`)  
**Corpus:** `Data/Gen.xml` … `Data/Deut.xml` (OSHB-style; ~Gen 50 ch / Exod 40 / Lev 27 / Num 36 / Deut 34)

**Related:**  
- `ARCHITECTURE_discussion_2026-07-19.md` — theory of code + data + pointers  
- `logic/SYSTEM.md` — Pre-Code derivation  
- Lev 1 work under `reviews/talmud_structure/`  

On substantive update: rename to today’s date and fix links (`STANDING_DECISIONS` §0).

---

## 0. Method recommendation (read this first)

### Should we break into segments?

**Yes as work units, no as permanent silos.**

| Approach | Good for | Risk |
|----------|----------|------|
| **Segments only** (one parasha / one chapter forever) | Deep Pre-Code units, ta’amim trees | Miss book-to-book installs and pointers |
| **One giant single pass forever** | Big picture | Too shallow; no feedback |
| **Passes over all five books** (recommended) | Architecture + interconnections | Needs note discipline between passes |
| **Segments inside a pass** | Execution | Fine if each segment still asks “what does this import/export?” |

**Recommendation:**

1. **Pass over all five books** with a fixed question (this file is Pass 1).  
2. **Write notes** (exports, imports, pointer types, open questions).  
3. **Pass again** with those notes in hand (Pass 2: pointer inventory; Pass 3: type registries; etc.).  
4. **Only then** drop into segment-deep Pre-Code (e.g. Lev 1) without losing the map.

Breaking into segments **too early** does limit interconnection vision. Breaking into **passes** does not: each pass still sees the whole corpus, at increasing resolution.

### Suggested pass ladder

| Pass | Question | Output |
|------|----------|--------|
| **1 (this file)** | How does each **book** fit the overall architecture? | Book roles + major blocks + import/export sketch |
| **2** | What **pointer styles** dominate (names, “as commanded,” joins, narrative state)? | **Done:** `ARCHITECTURE_pass2_pointers_2026-07-19.md` |
| **3** | What **type registries / data tables** live where (animals, pure/impure, festivals, offices)? | Registry map Written-first |
| **4** | **Sanctuary spine** only: Exodus install → Lev operate → Num stress → Deut restate | Flow diagram + free-name resolve rates |
| **5** | **Legal case genres** (casuistic IF, pure sequence, speech frame) by book | Genre mix for Pre-Code templates |
| Later | Segment units under `logic/units/` guided by the map | YAML, dual-track Oral |

Pass 1 deliberately stays **book- and block-level**. It does not replace verse trees or Sifra.

### Confidence for Pass 1

| Claim type | Label |
|------------|--------|
| Traditional major block outlines | **well-known structure** (orientation) |
| Architectural role (install / run / rest) | **hypothesis** (project model) |
| Exact cross-verse pointer census | **not done** — Pass 2+ |
| Keyword frequency from OSHB XML in this pass | **unreliable** this run (encoding/markup); do not trust numeric token counts here |

---

## 1. Whole-system picture (Pass 1 view)

Think of the five books as **one long run** with phases:

```text
Genesis     →  world + people + covenant patterns (bootstrap / seed data)
Exodus      →  people under pressure + Sinai law + **build the sanctuary machine**
Leviticus   →  **operate** the machine (offerings, purity, holiness calendar)
Numbers     →  **move** the machine through space/time; stress, revolt, war, land edge
Deuteronomy →  **restate / recompile** for life after Moses, in the land
```

**Data** is not only at the end of a book. Each phase **writes** something later phases **read**:

- Genesis writes family lines, promises, early offering gestures, Egypt setup.  
- Exodus writes law tables, covenant, and especially **Tabernacle + priesthood state**.  
- Leviticus writes offering **types**, purity **tables**, holiness **rules**.  
- Numbers writes census **data**, camp **layout**, travel **log**, some additional statutes.  
- Deuteronomy **reads** the journey and law and **re-emits** a land-facing constitution.

**Pointers** in Pass 1 sense: later text assumes earlier names and states (Tent, Aaron, “as YHWH commanded,” “remember what Amalek did,” etc.) without always redefining them.

---

## 2. Genesis — bootstrap, seed narrative, pre-machine world

**Span:** Gen 1:1 – 50:26 (~50 chapters, ~1500+ verses)  
**Architectural role:** **Bootstrap and seed data.** Creates the world, humanity, families, land promise, and recurring patterns (offering, covenant, exile/return, brother conflict) **before** the national sanctuary system exists.

### What it “writes” for later books

- **Cosmos and humans** — creation, image, blessing/curse patterns.  
- **Covenant prototypes** — Noah; Abrahamic promise (seed, land, nations); circumcision as mark.  
- **People graph** — patriarchs, twelve sons → tribes (raw material for Exodus/Numbers census and camps).  
- **Egypt state** — Joseph story ends with Israel **in Egypt**, which Exodus continues without re-explaining.  
- **Early cultic gestures** — altars, burnt offerings, tithes, “called on the name of YHWH” — **not** yet the Levitical system, but vocabulary and practice seeds.

### What it largely does **not** install

- No standing **Tent of Meeting / mishkan** operating system.  
- No Aaronic **priestly office** as in Exodus–Leviticus.  
- No full **casuistic purity code** of Lev 11–15.

So Genesis is not “empty of law-like material,” but it is **not the sanctuary runtime**. It is **precondition and genealogy**.

### Internal architecture (major movements)

1. **Primeval** (roughly 1–11) — creation to Babel; universal scope.  
2. **Abraham cycle** (12–25) — promise, land, covenant cut, tests.  
3. **Jacob cycle** (25–36) — rivalry, Bethel, name Israel, twelve sons.  
4. **Joseph / Egypt** (37–50) — descent, survival, setup for Exodus.

### Pass 1 export list (for later pointer passes)

| Export | Likely consumers |
|--------|------------------|
| Israel-in-Egypt end state | Exodus 1+ |
| Tribal ancestors | Numbers census, camp, land inheritance |
| Covenant/land promise language | Deuteronomy sermons; Numbers edge of land |
| Offering / altar vocabulary (seed) | Later refined in Exod–Lev |

### Pass 1 caution

Genre is mostly **narrative**. PureV9 lesson still holds: do not force IF/THEN control-flow everywhere in Genesis. Architecture role = **seed**, not **Lev-style procedure compiler**.

---

## 3. Exodus — pressure, covenant law block, and machine install

**Span:** Exod 1:1 – 40:38 (~40 chapters)  
**Architectural role:** **National formation + dual payload:** (A) liberation and covenant law, (B) **construction and activation of the sanctuary system** that Leviticus will operate.

### Two major architectural halves (classic, still useful)

**A. Narrative + covenant (roughly 1–24)**  
- Slavery, Moses, plagues, Passover, sea, wilderness start.  
- Sinai: theophany, **Decalogue**, covenant code (mishpatim), blood of covenant.  
- This half **writes law tables** and **national identity** under YHWH.

**B. Sanctuary install (roughly 25–40)**  
- Command to build **mishkan / Tent**, vessels, altar, priestly garments, consecration materials.  
- Golden calf interruption (32–34) — covenant breach and renewal; shows the system can fail.  
- Construction report and **glory fills the Tabernacle** (40) — **machine online**.

Leviticus 1:1 (“speaks from the Tent of Meeting”) is almost unintelligible as architecture without Exodus 40’s end state.

### What Exodus exports

| Export | Consumers |
|--------|-----------|
| YHWH–Israel covenant and basic mishpatim | Deuteronomy restatement; ongoing narrative |
| Passover / unleavened patterns | Later festival law (Lev 23, Num, Deut) |
| **Tent, furniture, altar** | Leviticus offerings and purity “where” |
| **Aaronic priesthood design** | Lev rites; Num duties; later crises |
| “As YHWH commanded Moses” compliance motif | Lev execution language; Num builds |
| Cloud/glory presence pattern | Num travel; Lev access rules |

### What Exodus still under-specifies (left for Lev / Oral)

- Full **menu of korban types** and disqualification detail (Lev).  
- Long **purity body/house/scale** codes (Lev 12–15).  
- Day-to-day **blood placement matrices** for chatat grades (Lev 4–5).  

Exodus **builds the stage and the cast**; Leviticus **writes most of the playbook**.

### Pass 1 architectural judgment

Exodus is the **installer and linker**: it connects narrative Israel to a **portable sacred OS**. If Genesis is seed data, Exodus is **platform build**.

---

## 4. Leviticus — runtime for the sanctuary: types, validators, holiness

**Span:** Lev 1:1 – 27:34 (~27 chapters, densest legal surface for this project)  
**Architectural role:** **Operate the Exodus-installed system.** Assumes Tent and priests. Speaks from the Tent. Defines **what may be brought**, **how**, **who is pure enough**, and **how Israel stays holy** around that center.

### Major blocks (Pass 1 map)

1. **Offerings (1–7)**  
   - Type channels: olah, minchah, shelamim, chatat, asham.  
   - **Input protocol** (animal classes, male/unblemished, voluntary vs required).  
   - **Pipelines** (lean, slaughter, blood, burn, eat portions).  
   - Our Lev 1 work lives here.

2. **Priestly inauguration narrative (8–10)**  
   - Execution of Exodus consecration patterns.  
   - Nadav/Avihu — invalid “input” / unauthorized fire: runtime error with lethal outcome.  
   - Architecture lesson: procedure is not optional decoration.

3. **Purity system (11–15)**  
   - Food creatures (11) — **species data table**.  
   - Childbirth (12), scale disease (13–14), genital discharges (15) — **state machines** over time and ritual.  
   - Strong Pre-Code FSM territory (Lev 12 track already started).

4. **Day of Atonement (16)**  
   - Annual system reset for sanctuary + people.  
   - Imports blood logic and holy/common distinctions.

5. **Holiness code and social law (17–22, roughly)**  
   - Blood, slaughter place, sexual boundaries, neighbor law, priestly holiness, festival calendar seeds.  
   - “Be holy” as system invariant.

6. **Time and land economics (23–25)**  
   - Festival calendar (23), lamp/bread (24), sabbatical/jubilee (25).  
   - Time as data + law.

7. **Covenant sanctions and vows (26–27)**  
   - Blessing/curse matrix; dedication valuations.  
   - Closing of the “runtime manual” with covenant consequences.

### Imports (reads from earlier Written)

- **Exodus:** Tent, priests, altar, “commanded” construction, presence.  
- **Genesis (lighter):** people as Israel; land promise backdrop; some offering vocabulary.  
- **Local:** most type lists for korban and purity are **declared here**.

### Exports

| Export | Consumers |
|--------|-----------|
| Offering types and procedures | Num additional offerings; Deut worship rules; later practice |
| Purity states and periods | Num camp purity; war/camp laws |
| Holiness / calendar | Num/Deut festivals; life structure |
| Priestly rights/duties detail | Num Korah etc.; Deut levitical provisions |

### Pass 1 architectural judgment

Leviticus is the **application layer** on the Exodus platform: **schemas (types), validators, pipelines, purity state, calendar.**  
Best fit for “Written = code + data”: **data tables and procedures co-located** in one book, while **environment** was installed previously.

---

## 5. Numbers — mobile runtime, stress tests, and logistics data

**Span:** Num 1:1 – 36:13 (~36 chapters)  
**Architectural role:** Take the **installed + regulated** system and **move it** through the wilderness. Add **military/logistical data**, narrative **failure modes**, and **edge-of-land** law. Not a pure second Leviticus; a **field deployment** of the same OS.

### Major movements

1. **Census, camp, levites (1–4)**  
   - **Data:** headcounts, tribal placement around the Tent.  
   - Architecture: the sanctuary is the **center of a spatial graph**.

2. **Camp purity and nazir, priestly blessing (5–6)**  
   - Imports Lev purity ideas into camp life.  
   - Nazir as special vow state.

3. **Dedication of altar / levites / Passover second chance (7–9)**  
   - Ritual logistics; calendar edge cases.

4. **Travel, complaint, spies, rebellion (10–17, roughly)**  
   - Stress: food, leadership, land fear, Korah (challenge to priestly install).  
   - Architecture: **what happens when operators reject the OS**.

5. **Priestly dues, red heifer, deaths of Miriam/Aaron (18–20)**  
   - Maintenance of priest/levite economy; corpse impurity water — new rite data.  
   - Generation transition.

6. **Wars, Balaam, Baal Peor, second census (21–26)**  
   - External threat + internal apostasy; new count for land inheritance.

7. **Offerings calendar expansion, vows, Midian, land inheritance (27–36)**  
   - Daily/festival offerings detail (28–29) **extends** Lev calendar.  
   - Zelophehad daughters — inheritance edge case (data + rule).  
   - Cities of refuge, tribal boundaries — **land OS** before entry.

### Imports

- Exodus sanctuary and priesthood (still center).  
- Leviticus purity and offering categories.  
- Genesis tribal names as census keys.

### Exports

| Export | Consumers |
|--------|-----------|
| Wilderness failure memory | Deuteronomy sermons (“you rebelled…”) |
| Second generation census | Land division logic |
| Cities of refuge / inheritance patterns | Deuteronomy; later narrative |
| Expanded public offering schedule | Ongoing cult |

### Pass 1 architectural judgment

Numbers is **runtime in motion**: same Tent-centered system, plus **logistics tables**, **failure narratives**, and **pre-land legal patches**. Interconnections are strongest **backward** to Exod–Lev and **forward** into Deut’s memory of the road.

---

## 6. Deuteronomy — recompile for the land; Moses as interface

**Span:** Deut 1:1 – 34:12 (~34 chapters)  
**Architectural role:** **Restatement and re-orientation.** Not primarily “build the Tent again.” Moses **reviews the journey**, **re-gives law** for life **in the land**, and closes the Torah. Architecture-wise: a **second compilation pass** over history + law, with different emphasis (centralization, heart, land tenure, leadership succession).

### Major movements

1. **Historical prologue (1–3)** — pointer-heavy narrative: “you did… YHWH did…” (reads Numbers/Exodus memory).  
2. **Covenant and Decalogue restatement (4–11)** — theology of loyalty; “hear O Israel.”  
3. **Deuteronomic law corpus (12–26)** — worship place, officials, war, family, social justice; **overlaps and reframes** earlier codes.  
4. **Covenant ceremony, blessings/curses (27–30)** — public bind; choose life.  
5. **Succession, song, blessing, death of Moses (31–34)** — transfer to Joshua; Torah as written witness.

### Imports

- Heavy **narrative memory** of Exodus–Numbers.  
- Law themes from Exodus covenant code and Leviticus holiness/calendar (not always copy-paste; often **recompiled**).  
- Land promise from Genesis.

### Exports

| Export | Consumers |
|--------|-----------|
| Land-facing constitution | Joshua+ (outside Torah) and later reading |
| Central sanctuary ideal | Tension with portable Tent history — architectural **policy shift** to note |
| “This Torah” as document | Self-reference: the run becomes a **file** Israel must keep |

### Pass 1 architectural judgment

Deuteronomy is the **linker and packager**: it teaches Israel to **carry the whole prior run** into a new environment (settled land), with Moses as the human interface and the written Torah as the artifact. It is the worst book to treat as isolated “just more cases” without the prior four.

---

## 7. Interconnections Pass 1 can already see (without segment silos)

### A. Sanctuary spine

```text
Exod 25–40 install → Lev 1–16 operate → Num camp around Tent → Deut re-aims worship for land
```

### B. People / data spine

```text
Gen tribes → Exod nation → Num census ×2 → Deut “all Israel” address → land inheritance logic
```

### C. Covenant spine

```text
Gen promise → Exod Sinai + calf crisis → Lev holiness/sanctions → Num breach stories → Deut renew + choose
```

### D. Law genre mix (sketch)

| Book | Dominant surface |
|------|------------------|
| Gen | Narrative; sparse law-like seeds |
| Exod | Narrative + covenant code + **build specs** |
| Lev | **Dense legal procedure + purity tables** |
| Num | Narrative + logistics + **patches** |
| Deut | Sermon + **recompiled law** + covenant rite |

### E. Pointer styles preview (for Pass 2)

- **Name resolve:** Tent, Aaron, Passover, Amalek, …  
- **Narrative state:** “Israel is in Egypt” / “glory filled” / “this generation will not enter.”  
- **Command echo:** “as YHWH commanded.”  
- **Memory pointer:** Deut “remember / do not forget.”  
- **Join on class words:** animal, pure/impure, land, firstborn.

---

## 8. Implications for Torah_Grok work

1. **Keep multi-pass architecture docs** (this series) separate from **segment Pre-Code units**.  
2. **Lev curriculum remains right for deep units**, but each unit should eventually tag **imports** (esp. Exodus state).  
3. **Do not isolate Deuteronomy or Genesis** when studying “how law works”; they bookend the machine.  
4. **Mesorat haShas** maps Oral↔Oral; this pass maps **Written phase roles**. Different layers.  
5. **Next concrete architecture work:** Pass 2 pointer examples (10–20 free names across the spine), not another full book essay until Pass 1 is accepted.

---

## 9. Open questions for Pass 2+

1. Which Lev free names resolve **almost always** to Exodus vs stay local?  
2. How much of Deut 12–26 is **rewrite**, **pointer**, or **new table**?  
3. Are pe/samekh section breaks (OSHB marks present in our XML) useful as **module boundaries** for architecture, or only for reading?  
4. Where do **type registries** (animals, blemishes, kinship) sit—single book vs multi-book joins?  
5. Does Numbers 28–29 “override” or “detail” Lev 23 public offerings? (detail vs second table)

---

## 10. Bottom line

**Method:** Prefer **passes over all five books** with notes between passes. Use **segments for deep derivation**, not as the only architectural view.

**Pass 1 result:**  
- **Genesis** bootstraps people and promise.  
- **Exodus** forms the nation and **installs the sanctuary OS**.  
- **Leviticus** is the **runtime manual** (types, purity, holiness).  
- **Numbers** is **field deployment** and stress.  
- **Deuteronomy** is **recompile for the land** and closes the run.

That is the detailed book-level map Pass 1 was for. Pass 2 should stop summarizing books and start **listing real pointer instances**.
