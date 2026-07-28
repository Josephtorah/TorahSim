# Architecture Pass 5 — Legal genres across the five books

**Date:** 2026-07-19  
**Kind:** architecture scan (hypothesis + measured signals — not binding law)  
**Pass:** 5 of multi-pass series  
**Question:** What **shapes** does Written “code” take (speech frame, casuistic IF, procedure sequence, registry header, narrative, sermon…), and how does the mix change by book?  
**Prior:** Passes 1–4; `ARCHITECTURE_discussion_2026-07-19.md`  
**Data:** `ARCHITECTURE_pass5_data_2026-07-19.json`

On update: rename to today’s date; fix links.

---

## 0. Bottom line

The five books do **not** all speak in the same genre. That matters for Pre-Code: **the right logic format depends on genre**.

| Book | Dominant surface (Pass 5 view) | Best Pre-Code instincts |
|------|--------------------------------|-------------------------|
| **Genesis** | Narrative + occasional speech; sparse case law | Story state, not dense IF tables |
| **Exodus** | Narrative interleaved with speech; covenant **mishpatim**; **build specs**; compliance | Mixed: narrative state + case code + inventory/procedure for Tabernacle |
| **Leviticus** | Speech frames + **casuistic** + **procedure sequences** + **registry headers**; little story | Decision tables, pipelines, FSMs, type registries |
| **Numbers** | Speech + narrative stress + logistics lists + some cases | Mixed; census tables; narrative failure modes |
| **Deuteronomy** | Long **sermon/address**; restated law; memory; prohibitions | Recompiled rules + historical pointer prose |

**Measured highlight (heuristic verse vote — see limits §8):**  
Only **Leviticus** shows clear elevation of **PROCEDURE_SEQ** and **CASUISTIC** together; **Genesis** is ~80%+ “other/narrative world”; **Deuteronomy** is speech/prohibition-heavy rather than “וסמך…ושחט…” pipeline text.

---

## 1. Genre catalog (what we mean)

### G1 — Speech frame
YHWH (or Moses) opens a unit: “And YHWH spoke… saying,” “Speak to the children of Israel…”

- **he examples:** וַיְדַבֵּר יְהוָה / *vayedabber YHWH* / “and YHWH spoke”; דַּבֵּר אֶל בְּנֵי יִשְׂרָאֵל / *daber el benei Yisrael* / “speak to the children of Israel”; לֵאמֹר / *lemor* / “saying.”  
- **Role:** packet header — not the IF body. Aligns with TIR-style “address = header.”  
- **Architecture:** marks a new **command payload** (Pass 2 P-CMD related).

### G2 — Casuistic case (IF / when)
Case law: if/when a situation holds, then a result.

- **Markers:** כִּי / *ki* / “when/if” in legal person-formulas; אִם / וְאִם / *im / ve-im* / “if / and if”; אָדָם כִּי / נֶפֶשׁ כִּי / אִישׁ כִּי / *adam ki / nefesh ki / ish ki*.  
- **Role:** decision-table rows.  
- **Example:** Lev 1:2–3 — person when offers…; if olah from cattle…

### G3 — Procedure sequence
Ordered cult actions: lean, slaughter, dash blood, flay, arrange, burn…

- **Markers:** chains of narrative-imperfect cult verbs (וְסָמַךְ, וְשָׁחַט, וְזָרְקוּ, וְהִקְטִיר…).  
- **Role:** pipeline / protocol after a case is selected.  
- **Example:** Lev 1:4–9 cattle olah steps.

### G4 — Registry / list header
Opens a data table or named module.

- **Markers:** זֹאת תּוֹרַת / *zot torat* / “this is the torah of…”; אֵלֶּה מוֹעֲדֵי / *elleh mo’adei* / “these are the appointed times”; זֹאת הַחַיָּה / *zot ha-chayyah* / “this is the living thing…”; וְאֵלֶּה הַמִּשְׁפָּטִים / *ve’elleh ha-mishpatim*.  
- **Role:** type registry entry point (Pass 3).

### G5 — Prohibition / apodictic
Direct “you shall not…” without full story case.

- **Markers:** לֹא + legal verb (eat, do, bring, approach…).  
- **Role:** hard constraints / guards.  
- Dense in holiness and Deuteronomy social law.

### G6 — Compliance report
“As YHWH commanded” — execution audit (Pass 2 P-CMD).

- **Example:** Lev 8 inauguration — Moses/Aaron did as commanded.

### G7 — Narrative
Story progression: travel, birth, death, battle, complaint.

- **Role:** state changes and stress tests (Pass 1 Numbers); not always IF/THEN.

### G8 — Sermon / hortatory address
Moses exhorts: remember, do not forget, love YHWH, choose life.

- **Home:** Deuteronomy.  
- **Role:** wraps recompiled law in **memory and motive** (Pass 2 P-MEM).

### G9 — Build / inventory specification
Materials, measurements, parts lists for Tabernacle and garments.

- **Home:** Exodus 25–31, 35–40.  
- **Role:** environment **data** (Pass 3 R7), not casuistic person-law.

---

## 2. Measured signals (corpus scan)

Normalized Hebrew verse counts (presence of pattern). **Not perfect classifiers** — `כי` especially is noisy outside law.

| Signal | Gen | Exod | Lev | Num | Deut | Comment |
|--------|----:|-----:|----:|----:|-----:|---------|
| וידבר/ויאמר יהוה אל… | 11 | **58** | 37 | **66** | 17 | Divine speech openings |
| דבר אל בני ישראל / אהרן… | 0 | 6 | **20** | 13 | 0 | Relay-to-Israel formula (Lev peak) |
| לאמר | 74 | 49 | 51 | **84** | 40 | “saying” frame particle |
| אדם/נפש/איש/אשה כי | 6 | 0 | **29** | 9 | 3 | Strong casuistic person-formula |
| ואם | 17 | 16 | **70** | 28 | 8 | Branching “and if” (Lev peak) |
| אם (broader) | 70 | 53 | **83** | 59 | 33 | Case branching |
| זאת תורת | 0 | 0 | **11** | 3 | 0 | Named procedure modules |
| כאשר צוה | 4 | **23** | 12 | 19 | 6 | Compliance / as-commanded |
| ויהי narrative openers | **100** | 28 | 1 | 30 | 6 | Story time (Gen peak; Lev almost none) |
| לא + prohibition-ish | 130 | 144 | 174 | 99 | **247** | Deut heaviest “shall not” surface |

**Heuristic primary-genre vote** (each verse forced into one bucket — many land in OTHER because law is multi-signal):

| Book | Top non-OTHER signals (heuristic) |
|------|-----------------------------------|
| Gen | NARRATIVE 9%; SPEECH 5%; case markers low |
| Exod | SPEECH 8%; NARRATIVE 7%; COMPLIANCE 3% |
| **Lev** | **CASUISTIC_IM 9%; PROCEDURE_SEQ 7%; SPEECH 6%; CASUISTIC_KI 4%; REGISTRY 2%** |
| Num | SPEECH 8%; CASUISTIC_IM 4%; NARRATIVE 3% |
| Deut | SPEECH 5%; PROHIBITION 3%; casuistic lower in this vote |

Treat percentages as **directional**, not gospel. The **signal table** is more trustworthy than the forced single label.

---

## 3. Book-by-book genre architecture

### Genesis — narrative OS with law seeds

**Mix:** Story dominates. Speech bursts (covenant, commands to patriarchs). Rare casuistic density.

**Architectural job:** write world/people/state (Pass 1); seed vocabulary (Pass 3).

**Pre-Code caution (PureV9 lesson):** do not force decision tables onto pure narrative. When law-like moments appear (e.g. circumcision command), treat as **speech-framed command**, not Lev-style case matrix.

---

### Exodus — three genre engines in one book

1. **Narrative liberation** (1–15-ish) — state machine of oppression → exit.  
2. **Covenant speech + mishpatim** (19–24) — Decalogue (often more apodictic) + case code (21:1 “these are the mishpatim”).  
3. **Build inventory + compliance** (25–40) — G9 specifications; “as YHWH commanded” when built (P-CMD).

**Architectural job:** install sanctuary data (Pass 3–4) **and** deliver first major law corpus.

**Pre-Code:**  
- mishpatim → decision rows;  
- Tabernacle → inventory/assembly procedure;  
- calf narrative → failure story, not a type registry.

---

### Leviticus — legal application layer (genre capital for this project)

**Mix:** speech frames open packets; casuistic opens cases; sequences execute rites; registry headers index modules; narrative almost only ch. 8–10 (+ bits).

**Lev block profile (heuristic vote inside chapters):**

| Block | Genre feel |
|-------|------------|
| **1–7 offerings** | Casuistic openers + **heavy PROCEDURE_SEQ** |
| **8–10 inauguration** | Narrative + **COMPLIANCE** (“as commanded”) |
| **11–15 purity** | Casuistic + procedure + **registry headers** |
| **16 kippur** | Procedure sequence (annual pipeline) |
| **17–22 holiness** | Speech + prohibitions + some cases |
| **23–25 time/land** | Speech + calendar registry + some cases |
| **26–27** | Casuistic branches (sanctions/vows) |

**Architectural job:** operate Exodus machine with **local registries + pipelines** (Pass 4).

**Pre-Code mapping:**

| Genre in Lev | Prefer format |
|--------------|----------------|
| G2 casuistic | Decision table / production rules |
| G3 sequence | Ordered protocol / steps |
| G4 registry | Type enum + constraints |
| G5 prohibition | Guards / NOT allowed |
| G1 speech | Header only (TIR-007 style) |
| G6 compliance | Provenance link to prior command |

---

### Numbers — speech + logistics + stress narrative

**Mix:** many divine speech openings (scan peak ~66); narrative of complaint/war/spies; list-like census/camp data; some casuistic; nazir/sotah modules with torah-of headers.

**Architectural job:** field-deploy the system; log failures for Deuteronomy memory.

**Pre-Code:** census = data tables; nazir = FSM; journey = narrative state, not IF/THEN spam.

---

### Deuteronomy — sermon shell + recompiled law

**Mix:** Moses’ long address (G8); restated commands; high prohibition surface; “which I command you today”; remember/forget; less “וסמך…ושחט” pipeline prose than Lev.

**Architectural job:** recompile for land; attach motive and memory (Pass 2).

**Pre-Code:** expect **parallel rows** to earlier law (not always new pipelines); tag `restates:` / `rebinds_place:` (Deut 12).

---

## 4. How genres connect to architecture passes 1–4

```text
G1 Speech frame     → opens command payload (pointer target for later "as commanded")
G2 Casuistic        → reads registries (Pass 3 types) into WHEN/THEN
G3 Procedure seq    → runs on EXOD environment keys (Pass 4 imports)
G4 Registry header  → declares local data tables (Pass 3)
G5 Prohibition      → validators / guards
G6 Compliance       → P-CMD audit (Pass 2)
G7 Narrative        → state transitions; stress tests
G8 Sermon           → memory load of prior run (Pass 2 P-MEM)
G9 Build inventory  → writes EXOD_IMPORT data (Pass 4)
```

**Genre is how the Written “code” is packaged.**  
**Registries/pointers are what it packages.**

---

## 5. Pattern: case then pipeline (Lev 1 template)

A recurring **composite genre** in offerings:

1. **G1** — Speak to Israel…  
2. **G2** — When a person offers / if from cattle…  
3. **G3** — He shall lean… slaughter… blood… burn…  
4. Optional **G4** — “this is the torah of the olah” (summary module)

That composite is why Lev 1 needed both a **scope unit** and a **procedure unit** in Pre-Code work — different genres, same chapter family.

---

## 6. Implications for Torah_Grok method

1. **Detect genre before choosing YAML shape** (table vs FSM vs protocol vs header-only).  
2. **Do not score Genesis/Deut “failure”** for lacking Lev pipelines.  
3. **Speech frames are not rules** — strip to header in tree coverage.  
4. **ואם chains** = sibling decision rows (cattle / flock / bird).  
5. **זאת תורת** = good unit boundary candidates (Pass 3 list).  
6. **Compliance verses** in Lev 8 = links to Exodus install, not new type data.

---

## 7. Confidence

| Claim | Label |
|-------|--------|
| Lev is uniquely dense in procedure + casuistic cult law among the five | **tested** (signals + block profile) |
| Gen is narrative-dominant | **tested** |
| Deut is address/recompile-dominant vs Lev pipelines | **tested** (directional) |
| Exact % genre per verse | **approximate** (heuristic; OTHER large) |
| `כי` counts as pure casuistic | **noisy** — prefer ish/adam/nefesh ki and ve-im |

---

## 8. Limits

- One-label-per-verse undercounts multi-genre verses (speech + case + procedure in one breath).  
- Build-spec genre in Exodus not fully separated by the auto vote (often OTHER).  
- Sermon genre in Deut not a separate auto tag (falls into SPEECH/OTHER/PROHIBITION).  
- No Oral genre pass here (baraita vs midrash vs sugya) — different stack.

---

## 9. Series complete (1–5)

| Pass | File | Result |
|------|------|--------|
| Theory | `ARCHITECTURE_discussion_2026-07-19.md` | Sequential run + data + pointers |
| 1 | `ARCHITECTURE_pass1_five_books_2026-07-19.md` | Book roles |
| 2 | `ARCHITECTURE_pass2_pointers_2026-07-19.md` | Pointer styles |
| 3 | `ARCHITECTURE_pass3_registries_2026-07-19.md` | Type registries |
| 4 | `ARCHITECTURE_pass4_sanctuary_resolve_2026-07-19.md` | Lev imports Exod stage; writes local code/data |
| **5** | **this file** | **Genre packaging of that code/data by book** |

**Natural next (outside pass ladder):** apply genre tags inside `logic/units` for Lev 1 (G1/G2/G3 already match your split units), or start a thin unit on a `זאת תורת` module.

---

## 10. One-sentence summary

**Written law is multi-genre: Genesis narrates, Exodus narrates and installs, Leviticus cases and pipelines, Numbers fields and lists, Deuteronomy preaches and recompiles — and Pre-Code should match format to genre.**
