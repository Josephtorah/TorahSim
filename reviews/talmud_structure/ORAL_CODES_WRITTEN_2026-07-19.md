# Can Mesorat haShas teach us how Oral Torah “codes” Written Torah?

**Short answer:**  
**Partly.** Mesorat haShas is the **map** of where Oral texts talk about the same material.  
The **coding rules** are not in the link edges — they are in the **midrash moves** at those places (especially **Sifra** on Leviticus, then Bavli baraitot that reuse the same moves).

**Standing decision (related):** MH is our parallel index — do not reinvent (`README.md`, DISCOVERIES Pass 7).  
**This note:** how to **read** those places as a **coding language** for Written Torah → Pre-Code logic.

**Not:** Binding religious law. Experimental derivation method for this repo.  
**Owner:** English-only — every Hebrew string below has translit + English.

---

## 1. What MH can and cannot do

| MH can | MH cannot |
|--------|-----------|
| Point: “Sifra unit X ↔ Talmud daf Y” | Tell you the rule in one click |
| Show densest Oral neighborhoods for a Lev stretch | Replace reading Hebrew midrash |
| Prioritize which Bavli/midrash pages to open | Act as IF/THEN source by itself |
| Link Oral ↔ Oral at scale (~48k edges) | Link Written verse nodes (almost never) |

**Path we use:**

```text
Written verse (Lev)
    → Sifra (walks Lev in order)     ← primary “coder”
    → Mesorat haShas                 ← map of related Oral places
    → Bavli / other midrash / Tosefta ← debate, reuse, edge cases
    → Pre-Code logic unit (YAML)     ← our frozen IF/THEN
```

---

## 2. What “coding the Written” means here

Oral midrash treats each Written word as a **signal** that can:

| Code action | Hebrew cue | Translit | English | Effect on logic |
|-------------|------------|----------|---------|-----------------|
| **Expand / include** | לרבות | *lerabot* | “to include” | Add class to WHEN/scope |
| **Exclude / filter out** | להוציא / מיעט | *lehotzi / mi’et* | “to exclude / restrict” | Remove class from scope |
| **You might think… but no** | יכול … תלמוד לומר | *yakhol … talmud lomar* | “you might think… the verse teaches” | Reject over-reading; lock rule |
| **Only this case so far** | אין לי אלא | *ein li ela* | “I only have…” | Start narrow; then expand |
| **From where do we know?** | מנין | *minayin* | “from where?” | Demand a Written source |
| **Surplus word** | שאין תלמוד לומר | *she’ein talmud lomar* | “the verse didn’t need to say this” | Extra word = extra rule |
| **Analogy (build-father)** | בנין אב | *binyan av* | “prototype case” | Copy rule across similar cases |
| **A fortiori** | קל וחומר | *kal va-ḥomer* | “light and heavy” | Infer stricter/weaker case |
| **Equal side** | הצד השוה | *ha-tzad ha-shaveh* | “the common side” | Shared property → shared rule |
| **Voluntary vs forced** | רשות / גזירה | *reshut / gezerah* | “optional / obligatory” | Modal on WHEN |
| **Coerce until consent** | כופין … רוצה אני | *kofin … rotzeh ani* | “coerce… ‘I want’” | Procedure on will |

These are the **global operators** — the same ones we measured dense in Sifra and Bavli.  
That is the Oral “instruction set” for turning Written wording into scope/procedure rules.

---

## 3. Pilot read: first of Leviticus (Sifra Nedavah)

Source: `Data/sifra_he.json` → `Vayikra Dibbura d'Nedavah`.  
MH neighborhood: `LEV1_OPENING_MESORAT_2026-07-19.md` (early units → parallels).

### 3.1 Chapter 1 — Lev 1:1 area (call before speech)

Written hook: **ויקרא…וידבר** / *vayikra…vayedaber* / “He called… and He spoke”

| Seg | Oral move (plain English) | Coding lesson |
|-----|---------------------------|---------------|
| א–ה | Call **before** speech — proved by bush / Sinai analogies; **הצד השוה** then **ת״ל** locks it for Ohel Moed | **Sequence rule:** event order in Written is load-bearing |
| ו | **יכול** only this speech? **מנין** all speeches from Tent? **ת״ל** “from Tent of Meeting” | **Scope expand** from local phrase to whole class |
| ז–ח | Call applies to “speak/say/command” but **not** to section breaks | **Include/exclude** by target of the verb |
| ט | Breaks give Moses time to reflect between units | **Structural comment** on Written segmentation (P/S-like spacing) |
| י–יב | Every call was “Moses, Moses”; answer “Here I am”; affection/urgency | **Protocol of address** (header, not sacrificial IF) |

**Logic-layer takeaway:** Opening is mostly **header / communication protocol**, not sacrifice IF/THEN (aligns with TIR-007 style “address = header”).

**MH note:** Chapter 1 MH links are **midrash-heavy, not Talmud** — coding here is midrash-to-midrash first.

### 3.2 Chapter 2 — “to him” (אליו)

| Seg | Move | Coding lesson |
|-----|------|---------------|
| א | **אליו** / *elav* / “to him” → **למעט** Aaron | **Pronoun = filter** (who is in the address set) |
| ב–ד | List of 13 exclusions parallel 13 joint speeches | **Count alignment** as evidence pattern |
| ו–ט | Who hears voice vs who is excluded (Israel, elders, Aaron’s sons, angels) | **Audience layers** on the same Written speech |
| י–יב | Voice stops at Tent; from between cherubim | **Location constraints** on revelation event |
| יג | **לאמר** / *lemor* / “saying” → tell Israel “for your sake…” | **Relay instruction** (Moses → people) |

### 3.3 Section 2 — Lev 1:2 area (who brings / from animals)

This is where **sacrifice coding** starts (and MH → **Talmud** densifies).

| Seg | Written bit | Oral code | Logic sketch |
|-----|-------------|-----------|--------------|
| א–ב | בני ישראל / *benei yisrael* / “children of Israel” | Israelites lean; not idolaters; women disputed | `agent.lean` membership rules |
| ג | אדם / *adam* / “person” · מכם / *mikem* / “from you” | **לרבות** converts · **להוציא** apostates · locked via בני ישראל = covenant-receivers | include/exclude on `agent` |
| ד | כי יקריב / *ki yakriv* / “when one offers” | **יכול** obligation? **ת״ל** → **רשות** (voluntary) | modal: voluntary vs must |
| ו | בהמה / *behemah* / “animal” | Not wild game even if called behemah elsewhere; need cattle/flock | `species` filter via later words |
| ז–יא | מן הבהמה / מן הבקר / מן הצאן | Exclude violated, worshipped, terefah, set-aside, goring, etc. | **Disqualification list** on `animal` |

**Coding pattern (reusable):**

```text
FOR each surplus / restrictive Written word W on a verse:
  1. Propose default scope (יכול / plain reading)
  2. Include or exclude a class (לרבות / להוציא)
  3. Test by analogy (קל וחומר / בנין אב)
  4. LOCK with תלמוד לומר + the Written phrase
```

That four-step loop **is** how Oral is “telling us to code” Written.

### 3.4 Section 3 — olah / male / unblemished

| Seg | Code | Logic sketch |
|-----|------|--------------|
| א–ב | Word **עולה** extends disqualifiers from freewill to **obligatory** olah | Same filters, more offering types |
| ג–ד | Extend to **תמורה** / *temurah* / substitute | Class expansion |
| ז | **זכר** / *zakhar* / “male” → not female; second “male” excludes tumtum/androgynous | Gender + edge bodies |
| יב | **תמים** / *tamim* / “whole/unblemished” → must be checked before offer | Guard before ritual |
| טו | **יקריב אותו** force him; **לרצונו** / *lirtzono* / “of his will” → coerce until he says “I want” | Consent procedure |

---

## 4. Repeatable method (for this repo)

### Step A — Pick Written span
Hebrew only (`Data/Lev.xml` / OSHB). Ta’amim tree first when doing a unit.

### Step B — Read Sifra on that span
Sequential Nedavah / later sections. Extract every:
- יכול / ת״ל  
- לרבות / להוציא  
- מנין  
- בנין אב / קל וחומר  

Into a draft decision table (English comments + he/translit/en atoms).

### Step C — Use Mesorat haShas (map only)
Open `Data/links*.csv` / `sifra_talmud_links_2026-07-18.*` / `LEV1_OPENING_MESORAT_2026-07-19.md`:
- Which Bavli / Tosefta / midrash pages tradition ties here?
- Read those for **same operators** and edge cases — do not invent new links.

### Step D — Freeze Pre-Code unit
`logic/units/….yaml` with:
- phrase map / tree coverage  
- IF/THEN rows grounded in Hebrew  
- Oral attachments **named** (Sifra unit, MH-linked daf) — never silent merge  

### Step E — Optional later
Code may **interpret** frozen YAML. Code must **not** invent the rules.

---

## 5. Honest limits

1. **Not every MH edge is a coding lesson** — some are thematic or aggadic parallels.  
2. **Sifra is primary for Lev procedure coding**; Bavli often debates and reuses, not always first derivation.  
3. **School labels** (תנא דבי ר׳ ישמעאל) mark family of method, not automatic “paste this into YAML.”  
4. **Confidence labels** still required (hypothesis / tested / failed).  
5. We will **not** finish “all MH references” in one pass — we **sample by Written address** and grow units.

---

## 6. Practical next step (recommended)

Do **one thin slice** end-to-end:

| Slice | Written | Sifra | MH Talmud samples |
|-------|---------|-------|-------------------|
| Agent + animal filters | Lev 1:2 | Nedavah Section 2 | Bava Kamma 40b, Temurah 28a–29a, Zevachim 34a (from MH list) |
| Olah + male + will | Lev 1:3–4 | Nedavah Section 3 | Arakhin 21a, Menachot 5b, … |

Output: draft `logic/units/lev_01_agent_and_animal_filters.yaml` (or extend existing Lev 1 units) with operators from §2–3.

---

## 7. Files

| File | Role |
|------|------|
| `Data/links*.csv` | MH source of truth (parallels) |
| `LEV1_OPENING_MESORAT_2026-07-19.md` | MH neighborhood for Lev 1 opening |
| `SIFRA_TALMUD_LINKS_2026-07-19.md` | Sifra↔Talmud MH extract |
| `LINK_PHRASES_2026-07-18.md` / operator_index | Discourse moves inside Bavli lines |
| `logic/SYSTEM.md` | Where coded results must land |
| **This file** | Method: MH as map; midrash operators as coding ISA |

---

## 8. One-sentence policy

**Use Mesorat haShas to find the Oral rooms; read Sifra/Bavli inside those rooms to learn the coding operators; write the result as Pre-Code logic — never as a new parallel index and never as rules invented in Python.**
