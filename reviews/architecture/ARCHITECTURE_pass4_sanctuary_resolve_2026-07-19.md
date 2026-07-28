# Architecture Pass 4 — Sanctuary spine: free-name resolve (Lev 1–16 sample)

**Date:** 2026-07-19  
**Kind:** architecture scan (hypothesis + measured sample — not binding law)  
**Pass:** 4 of multi-pass series  
**Question:** When Leviticus runs sanctuary law, how often do key terms **import** earlier install (esp. **Exodus**) vs stay **local Leviticus data/code**?  
**Scope:** **Lev 1–16** only (offerings → priest inauguration → purity → Day of Atonement) — the core “operate the machine” block.  
**Prior:** Passes 1–3; theory in `ARCHITECTURE_discussion_2026-07-19.md`  
**Machine dump:** `ARCHITECTURE_pass4_data_2026-07-19.json`

On update: rename to today’s date; fix links.

---

## 0. Bottom line first

For a sample of **57** key symbols that actually appear in Lev 1–16:

| Resolve class | Symbols | Sum of verse-hits in Lev 1–16 |
|---------------|--------:|------------------------------:|
| **EXOD_IMPORT** (sanctuary environment / office) | 17 | **377** |
| **LEV_LOCAL** (types, purity, rite mechanics) | 22 | **519** |
| **MULTI** (common nouns / multi-book) | 17 | **405** |
| **GEN_SEED** (people graph) | 1 | **19** |

**Reading (architecture, not etymology):**

- Leviticus is **not** “all imported.” It is **busy writing local registries and pipelines** (purity, offering types, slaughter/smoke/atonement verbs, Day of Atonement specifics).  
- But the **stage and cast** of the sanctuary — Tent, entrance, veil, incense system, Aaron/sons, priest office, glory/cloud, most-holy space — are **read from Exodus install**.  
- So the owner model holds in a **split** form:

```text
Exodus  →  environment + office keys
Leviticus → local type tables + procedure code + purity state machines
            while resolving environment keys outward to Exodus
```

**Important method caveat:** “first time the string appears in the Torah” ≠ “where the sanctuary system installs it.”  
Example: **מזבח** / *mizbeach* / altar appears in Genesis (Noah, patriarchs), but the **Tabernacle altar system** Lev assumes is **Exodus-built**. Pass 4 classifies by **system install**, and reports first-string only as a secondary fact.

---

## 1. Method

1. Take **Lev 1–16** (490 verses in our OSHB extract).  
2. Define a **symbol list** of sanctuary/cult free names and key technical terms (Tent, priests, offering types, purity labels, rite verbs, etc.).  
3. For each symbol:  
   - count **how many Lev 1–16 verses** contain it (normalized Hebrew);  
   - record **first string hit** anywhere in Gen–Deut;  
   - assign **architectural resolve class** (manual, documented rules below).  
4. Aggregate by class (unweighted symbol count + verse-hit weighted).

**Classes**

| Class | Meaning |
|-------|---------|
| **EXOD_IMPORT** | Sanctuary/office **system** is installed or blueprinted in Exodus; Lev **uses** the key |
| **LEV_LOCAL** | Type, purity module, or rite mechanic is **primarily declared/operated as system** in Leviticus |
| **GEN_SEED** | People/identity seed from Genesis trajectory (via Exodus nation) |
| **MULTI** | Widespread common noun or multi-book phrase; not a clean single-book import |

**Not done this pass:** full word-by-word parse of every Lev 1–16 token; Oral-only edges; Numbers camp graph.

---

## 2. Headline measurements

### 2.1 Symbol counts

Among symbols with ≥1 hit in Lev 1–16:

- **EXOD_IMPORT:** 17 / 57 ≈ **30%** of symbols  
- **LEV_LOCAL:** 22 / 57 ≈ **39%**  
- **MULTI:** 17 / 57 ≈ **30%**  
- **GEN_SEED:** 1 / 57 ≈ **2%** (`בני ישראל` / children of Israel)

### 2.2 Weighted by Lev 1–16 verse frequency

If we weight by how often Lev **talks** using that key:

- **LEV_LOCAL** leads (**519** hit-verses) — purity + offering mechanics dominate discussion volume.  
- **MULTI** next (**405**) — blood, fire, holy, cattle, before YHWH, etc.  
- **EXOD_IMPORT** still large (**377**) — priests + altar + Tent language is constant background.

**Interpretation:** Local code/data gets **more airtime**; Exodus imports are fewer **keys** but **structurally load-bearing** (without them the local procedures have no stage).

### 2.3 Environment-only subtotal (clearest import set)

These are hard to re-read as “invented in Lev 1–16”:

אהל מועד, פתח אהל מועד, משכן, פרכת, כפרת, ארון (ark), קטרת (system), אפוד, חשן, אורים, כבוד/ענן presence, קדש קדשים, בני אהרן, אהרן (office cast), כהן (Aaronic office use), מזבח (sanctuary altar system).

**First string in Torah for several true Tent keys is already Exodus**, e.g.:

| Key | First string (scan) | Architectural home |
|-----|---------------------|--------------------|
| אהל מועד / Tent of Meeting | **Exod 27:21** | Exodus install |
| פתח אהל מועד / entrance | **Exod 29:4** | Exodus |
| בני אהרן / sons of Aaron | **Exod 28:1** | Exodus |
| משכן / mishkan (as system word) | Exodus build block | Exodus |
| כפרת / kapporet | Exodus | Exodus |

---

## 3. EXOD_IMPORT set (what Lev is reading)

### 3.1 Place / furniture / presence

| Symbol | en | Lev 1–16 verse hits (approx) | Notes |
|--------|-----|-------------------------------:|-------|
| ohel_moed | Tent of Meeting | 35 | Speech/from, rites at |
| petach_ohel | entrance of Tent | 18 | Lev 1:3 bring-near location |
| mizbeach | altar | 74 | Constant rite target (system from Exod; word older) |
| mishkan | tabernacle | lower | Used; Exod definition |
| paroket | veil | present | Inner boundary |
| kapporet | cover / kapporet | present | Holy of holies furniture |
| aron | ark | present | |
| ketoret | incense | present | Exod incense system |
| qodesh_qodashim | most holy | present | Space grade from Exod plan |
| kavod / anan | glory / cloud | present | Activation state from Exod 40 |

### 3.2 Office / cast

| Symbol | en | Hits | Notes |
|--------|-----|-----:|-------|
| kohen | priest | 130 | Highest hit count in sample; office install Exod, ops Lev |
| aharon | Aaron | 67 | Cast |
| benei_aharon | sons of Aaron | 21 | Operators of blood/fire in Lev 1 |

### 3.3 Pass 4 claim A

**Without Exodus, Lev 1–16 has nowhere to stand.**  
The **coordinates** (Tent, entrance, altar-as-sanctuary-object, priestly operators, presence) are imported keys.

---

## 4. LEV_LOCAL set (what Lev is writing)

### 4.1 Offering type registry (R2 from Pass 3)

| Symbol | en | Hits | Role |
|--------|-----|-----:|------|
| olah | burnt offering | 55 | type + pipeline |
| chatat | sin offering | 60 | type |
| asham | guilt offering | 27 | type |
| minchah | grain offering | 24 | type |
| shelamim | peace offering | present | type |
| torim | turtledoves | present | named bird input |
| seir | goat (incl. kippur) | 19 | local cult animal role |
| azazel | Azazel | present | Lev 16-only key |

### 4.2 Purity modules (R3)

| Symbol | en | Hits | Role |
|--------|-----|-----:|------|
| tame | impure | **84** | purity namespace capital |
| tahor | pure / purify | 34 | |
| tzaraat | scale disease | 27 | Lev 13–14 module |
| zav | discharge | present | Lev 15 |
| metzora | person with scale disease | present | |
| yoledet | woman after childbirth | present | Lev 12 |

### 4.3 Rite mechanics (local pipelines)

| Symbol | en | Hits | Role |
|--------|-----|-----:|------|
| shachat | slaughter | 27 | cult procedure verb |
| hiktir | turn to smoke | 20 | |
| zarak | dash blood | present | |
| semikhah | lean hands | present | offering lean system |
| kipper | atone | 41 | atonement outcomes/mechanics |
| tamim | unblemished | present | acceptance flag on animals |
| solet / levonah | fine flour / frankincense | present | minchah materials as offering data |

### 4.4 Pass 4 claim B

**Leviticus is not a thin client.**  
It **authors** the offering menu, purity state machines, and the verb-chain of sacrifice. Those are **local registries + code**, not Exodus reprints.

---

## 5. MULTI and GEN_SEED (do not over-import)

### MULTI (handle carefully)

Examples: **דם** / blood, **אש** / fire, **בקר** / cattle, **צאן** / flock, **לפני יהוה** / before YHWH, **קדש** / holy, **משה** / Moses, **גר** / sojourner.

- As **Hebrew words**, they exist earlier.  
- As **sanctuary operating constraints**, Lev specializes them.  
- Pass 4 does **not** force them into EXOD_IMPORT; that would inflate the import thesis dishonestly.

### GEN_SEED

- **בני ישראל** / children of Israel — people key from Genesis→Exodus trajectory (19 hits in sample scope).  
  Not Tent data; **who is addressed**.

---

## 6. Worked verse: Lev 1:1–5 as resolve table

| Token | Class | Resolves to |
|-------|--------|-------------|
| מֵאֹהֶל מוֹעֵד / from Tent of Meeting | EXOD_IMPORT | Exod meeting/presence install |
| בְּנֵי יִשְׂרָאֵל / children of Israel | GEN_SEED | People graph |
| בְּהֵמָה / בָּקָר / צֹאן / animal classes | MULTI → specialized **LEV_LOCAL use** | Local offering registry (Pass 3 R1); join risk to Lev 11 |
| פֶּתַח אֹהֶל מוֹעֵד / Tent entrance | EXOD_IMPORT | Exod 29:42 et al. |
| זָכָר תָּמִים / male unblemished | LEV_LOCAL flags | Local constraints on input |
| בְּנֵי אַהֲרֹן הַכֹּהֲנִים / sons of Aaron the priests | EXOD_IMPORT | Exod 28+ office |
| דָּם / blood, זְרִיקָה / dashing | MULTI + LEV_LOCAL mechanics | Substance old; **cult matrix** Lev |

This is the split model in one unit: **import stage/cast; declare types; run local pipeline.**

---

## 7. String-first vs system-install (examples)

| Symbol | First string (scan) | System install (architecture) |
|--------|---------------------|--------------------------------|
| מזבח altar | Gen 8:20 (Noah) | Sanctuary altar: **Exodus** |
| כהן priest | Gen 14:18 (Melchizedek) | Aaronic priestly system: **Exodus** |
| חטאת | Gen 4:7 (different sense/noise) | Chatat **offering system**: **Leviticus** |
| עולה | early string noise / patriarchal offerings | Olah **type menu + blood pipeline**: **Leviticus** |
| טמא | early narrative uses | Purity **code density**: **Leviticus** |
| אהל מועד | **Exod 27:21** | Matches install book |
| בני אהרן | **Exod 28:1** | Matches install book |

**Rule for later agents:** when tagging Pre-Code `import:`, use **system install**, not raw first-string, unless studying etymology.

---

## 8. Quantitative answer to the Pass 4 question

**Q:** Does Lev mostly read Exodus data?

**A (nuanced):**

1. **Structurally yes for environment/office keys** (~30% of sampled symbols; constant background hits on priest/altar/Tent).  
2. **Quantitatively no for “most of what Lev talks about”** — local purity + offering types + rite verbs dominate **verse-hit volume**.  
3. **Best formula:**

```text
Lev 1–16 ≈ (Exodus environment/office) + (Leviticus registries + procedures)
```

That matches Pass 1–3 and the owner “run looks up data” model: **lookup is real**, and **local data is also real**.

---

## 9. Implications for Pre-Code / Lev curriculum

When freezing a Lev unit, default tags:

```yaml
imports:
  - key: ohel_moed
    from: Exodus_sanctuary_install
  - key: benei_aharon_kohanim
    from: Exodus_priest_office
local_registry:
  - offering_types: [bakar, tzon, of...]
  - constraints: [zakhar, tamim]
local_pipeline:
  - steps: [semikhah, shachat, dam, ...]
join_risk:
  - behemah: [Lev.11, Deut.14]
```

Do **not** mark `chatat` / `tame` / `tzaraat` as Exodus imports without evidence.

---

## 10. Limits of this pass

- Sampled **symbols**, not 100% of words in Lev 1–16.  
- Pattern noise on some terms (olah/esh/dam).  
- Manual classes are **hypothesis labels** with high confidence on Tent/Aaron, medium on MULTI.  
- Did not measure reverse pointers (does Exodus ever “need” Lev? generally no for install).  
- Num/Deut not in the hit window (by design).

---

## 11. Confidence

| Claim | Label |
|-------|--------|
| Tent / sons of Aaron / priest office are Exodus system imports into Lev | **tested** |
| Purity + offering-type vocabulary is Lev-authored system | **tested** (density + loci) |
| ~30/39/30 split of symbol classes | **tested on this sample only** |
| Weighted hit totals exact for all Hebrew synonyms | **approximate** |
| “Torah is software” | **metaphor only** |

---

## 12. Series status

| Pass | File | Status |
|------|------|--------|
| Theory | `ARCHITECTURE_discussion_2026-07-19.md` | done |
| 1 Books | `ARCHITECTURE_pass1_five_books_2026-07-19.md` | done |
| 2 Pointers | `ARCHITECTURE_pass2_pointers_2026-07-19.md` | done |
| 3 Registries | `ARCHITECTURE_pass3_registries_2026-07-19.md` | done |
| **4 Resolve sample** | **this file** + `ARCHITECTURE_pass4_data_2026-07-19.json` | **done** |

**Pass 5:** legal genre mix — **done:** `ARCHITECTURE_pass5_genres_2026-07-19.md`.

---

## 13. One-sentence summary

**Lev 1–16 imports its sanctuary stage and priestly cast from Exodus, but authors most of its offering types, purity states, and rite mechanics locally — so the Written run both looks up earlier data and carries large local tables.**
