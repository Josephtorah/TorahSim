# Research: Valid Oral Torah — core documents, chronology, links, and “possible Oral”

**Date:** 2026-07-19  
**Kind:** research deep dive + project framing (not binding religious law)  
**Status:** living research; **single canonical Oral-validity doc**  
**MH clause:** **no Mesorat haShas reference ruled out** — all are **possible Oral** (see §6)  
**Related:** architecture series; Pre-Code `logic/SYSTEM.md`; `STANDING_DECISIONS.md` §5  

On substantive update: rename to today’s date and fix links.

---

## 0. What this document is

This is the **full** research write-up on:

1. How to tell **classical Oral Torah literature** from later commentary and modern study  
2. What the **core Oral documents** are and how they **link** (names, schools, loaders, Mesorat haShas)  
3. **What was “first”** (Mishnah? Sifra? Talmud?) — traditional vs historical answers  
4. Clues from **document openings** (especially Sifra’s 13 middot)  
5. How **Mesorat haShas** defines **possible Oral** for this project (nothing in MH ruled out)  
6. Practical tiers and job preference for Torah_Grok derivation  

It is **not** a claim that any academic dating is dogma, and **not** a substitute for dual-track Pre-Code units.

---

## 1. Three questions (keep them separate)

### A. Traditional / religious  
What does the tradition call **Oral Torah** (*Torah she-be‘al peh*) as received teaching later written down?

### B. Historical / philological  
When were the books **redacted**, and how do they depend on each other? (Scholarly ranges; useful for order, not for “inspiration meters.”)

### C. Torah_Grok engineering  
What may we attach as **named Oral** when deriving logic from **Written Hebrew**?

Mixing A/B/C causes either over-trust of a modern essay or under-use of Sifra.

**Project constants (already standing):**

- Written Hebrew = derivation source of truth  
- Oral = **named location only**; never silent merge into Written  
- English = secondary aid only  
- Confidence labels required  

---

## 2. What was “first”?

### 2.1 Living Oral first  
Before Mishnah, Sifra, or Talmud as *books*, there was **oral teaching** (practice, case resolution, verse reading).  
So **none** of those books is “the first Oral Torah.” They are **crystallizations**.

### 2.2 As finished literature (rough scholarly consensus)

| Work | Rough redaction window | Genre / job |
|------|------------------------|-------------|
| **Mishnah** | ~200 CE (R. Judah ha-Nasi) | Topical law modules — first major closed **legal code** of Oral in writing |
| **Tosefta** | Same era / slightly later | Parallel / expansion next to Mishnah |
| **Halakhic midrash** (Mekhilta, **Sifra**, Sifrei) | Tannaitic material; redaction often late Tannaitic / early Amoraic (debated) | Verse-sequential **decoder** of Torah books |
| **Yerushalmi** | ~4th–5th c. | Gemara on Mishnah (Land of Israel) |
| **Bavli** | ~5th–7th c. | Gemara on Mishnah (Babylonia) — **later** |
| **Classic aggadic midrash** (Rabbah, etc.) | Varies; often later than core midreshei halakhah | Homily / narrative / ethics |
| **Rishonim** (Rashi, Rambam, Tosafot…) | Medieval | Commentary / codes **on** the above — not peer “Oral books” equal to Mishnah |
| **Modern academic studies** | 19th c.–now | Study *of* the sources — not Oral Torah texts |

### 2.3 Direct answers

| Question | Answer |
|----------|--------|
| Was Talmud first? | **No** — it presupposes Mishnah and loads baraitot/verses |
| Was Mishnah first as a major *code*? | **Yes** (as literary legal code ~200 CE) |
| Was Sifra “the book before everything”? | **No** — **sister Tannaitic genre** (midrash on Leviticus), not a simple pre-Mishnah parent of Talmud |
| What was first for *verse decoding* on Lev? | **Sifra-shaped midrash** (right *job*), not “oldest file on disk” |
| Dependency that is clear | Mishnah → Talmud comments on it; midrash ↔ same Tannaitic world; MH later wires parallels |

```text
Living Oral practice
    → Tannaitic crystallization in TWO main literary shapes:
         Mishnah/Tosefta (topical modules)
         Midreshei halakhah (verse-order: Mekhilta / Sifra / Sifrei)
    → Talmudim (Amoraic) debate Mishnah + baraitot + verses
    → Medieval commentary & codes explain / reorganize
    → Modern scholarship studies the pile
```

---

## 3. Clues from how the documents open

### 3.1 Sifra (clue = method, not chronology)

Sifra opens with **ברייתא דרבי ישמעאל** / *Braita de-Rabbi Yishma’el*:

- **רבי ישמעאל אומר** / *Rabbi Yishma’el omer* / “Rabbi Ishmael says”  
- **בשלש עשרה מדות התורה נדרשת** / *bi-shlosh esreh middot ha-Torah nidreshet* / “by thirteen measures the Torah is interpreted”

Then kal va-ḥomer, gezerah shavah, binyan av, kelal u-ferat, etc., with worked examples.

**Clue:** Halakhic midrash presents itself as a **named-school rule-engine for reading Written Torah**.  
That is the Oral “decoder” charter for our architecture metaphor.

### 3.2 Mishnah (clue = operations + transmission)

- Often starts **in practice** (e.g. when to say Shema) — **operational modules**.  
- **Pirkei Avot** gives a **chain of transmission** (Moses → sages) — legitimacy narrative, not 13 middot.

### 3.3 Talmud (clue = second-order system)

Assumes **מתני׳** / *matni’* / Mishnah lemma on the page; runs dispute, proof, baraita load around it.

**Summary:**  
- First as **code modules** → Mishnah-shaped  
- First as **verse decoder** → midrash-shaped (Sifra on Lev)  
- First as **dispute engine** → Talmud  

---

## 4. How Oral documents link (names, schools, loaders, MH)

### 4.1 Named sages and schools (primary internal graph)

| Link type | Example | Role |
|-----------|---------|------|
| Sage name | רבי עקיבא, רבי ישמעאל | Attribution / dispute poles |
| School | דבי רבי ישמעאל / *de-vei R. Yishmael* | Method family (frequent in Bavli) |
| School contrast | Ishmael-style vs Akiva-style midrash (scholarly framing) | Different derash habits |
| Generation labels | Tanna / Amora (later metalanguage) | Period of voice |

**Schools and names matter more inside the corpus than modern book titles.**  
Bavli rarely says “Sifra 3:2”; it says school/baraita formulas.

### 4.2 Genre loaders (Oral → Oral)

| Formula | Loads |
|---------|--------|
| מתני׳ / *matni’* | This Mishnah |
| תנן / דתנן | We learned (Mishnah) |
| תניא / דתניא | Taught (baraita — Tosefta / midrash / free baraita) |
| תנו רבנן | Our rabbis taught |
| תנא דבי ר׳ ישמעאל | School baraita |

### 4.3 Written loaders

| Formula | Loads |
|---------|--------|
| שנאמר / דכתיב / תלמוד לומר | Written verse / teaching from verse |
| Parenthetical (ויקרא א, ב) | Verse address (in our editions; see cite_index) |

### 4.4 Mesorat haShas (external traditional parallel graph)

Local: `Data/links*.csv`, type `mesorat hashas` (~48k edges).

Stitches **Talmud, Midrash, Mishnah, Tanaitic (Tosefta-world)** almost exclusively.  
Full policy for MH as **possible Oral** is §6 below.

### 4.5 Architecture diagram

```text
                 Written Torah (Tanakh)
                        ▲
                        │  שנאמר / cites / ת״ל
     ┌──────────────────┼──────────────────┐
     │                  │                  │
Halakhic midrash    Mishnah            Baraita pool
Sifra/Mekhilta/     (modules)          (Tosefta / free)
Sifrei                  │
     │                  ▼
     │            Talmud (Bavli / Yerushalmi)
     │            matni’ + tanya + verses
     │                  │
     └──── Mesorat haShas parallels ────┘

  Schools (e.g. R. Yishmael) cut across midrash & baraitot
  Sage names cut across all
```

---

## 5. Core documents by job (for this project)

| Job | Prefer among possibles | Local `Data/` examples |
|-----|------------------------|-------------------------|
| Decode **Leviticus** verse-by-verse | **Sifra** | `sifra_he.json` |
| Decode **Exodus** | **Mekhilta** (R. Yishmael / Rashbi) | `mekhilta*_he.json` |
| Decode **Num / Deut** | **Sifrei** | `sifrei_bamidbar_he.json`, `sifrei_devarim_he.json` |
| Modular standing ruling | **Mishnah** (+ **Tosefta**) | `mishnah_*`, `tosefta_*` |
| Dispute / edge / integration | **Bavli** | `bavli_*_he.json` |
| Second Talmud | **Yerushalmi** when needed | `yerushalmi_*_he.json` |
| Narrative / homiletic midrash | **Rabbah** etc. when unit wants that genre | e.g. `vayikra_rabbah_he.json` |
| Parallel navigation | **Mesorat haShas** | `Data/links*.csv` |

**We have ~200+ Oral-ish JSON files** already (Mishnah, Tosefta, Bavli, Yerushalmi, midrash, Sifra, Mekhilta, Sifrei). The problem is **policy**, not missing shelves.

---

## 6. Mesorat haShas → “possible Oral” (adopted — full policy)

This section is the **only** project home for the MH “possible Oral” rule (no separate MH-only doc).

### 6.1 Naming / project language

| Say | Avoid |
|-----|--------|
| **possible Oral** (Mesorat haShas member) | ruled out / invalid Oral (for MH endpoints) |
| preferred for this job | the only real Oral |
| secondary aid (non-MH commentary we choose to read) | “uninspired” as a technical filter |
| Written source of truth | MH as law source |

**Optional short label in units/notes:** `oral_possible_mh`

### 6.2 Decision (plain)

**We do not rule out any reference that appears in Mesorat haShas.**

If tradition put a work on the MH graph, we treat it as **possible Oral Torah material** for this project — at least as something we may open, cite, and attach with a named location.

We still:

- Derive logic from **Written Hebrew** first.  
- Prefer the best **job fit** for a unit (e.g. Sifra for Lev verse coding).  
- Never **silent-merge** Oral into Written.  
- Label confidence.

We do **not** use MH non-membership alone to declare a classical work “not Oral” (title spelling / under-index can miss peers). MH is a **strong positive** signal for “possible,” not a complete negative census.

### 6.3 Why this makes sense

Mesorat haShas is the traditional **see-also / parallel** apparatus among classical texts. Local dump: `Data/links*.csv`, `Conection Type` = `mesorat hashas`.

| Category (side hits) | ~Count | Role |
|----------------------|-------:|------|
| Talmud | ~40,041 | Bavli (etc.) |
| Midrash | ~37,097 | Halakhic + aggadic midrash |
| Tanaitic | ~10,568 | Tosefta and related |
| Mishnah | ~8,756 | Mishnah |
| Tanakh | ~66 | noise / edge (often commentary mis-tagged) |
| Halakhah | ~7 | medieval codes (rare) |
| Chasidut | ~1 | rare |

**~99.8%** of MH sides are the classical rabbinic library.  
Modern academic monographs and random blogs essentially **do not** appear as MH nodes.

**Also measured:** ~48,268 edges; ~781 unique works on the graph; heavy nodes include Bavli tractates, Mekhilta, Sifrei, Sifra (title variants), Rabbahs, Tosefta, Mishnah. Sifra↔Talmud has thousands of edges (`reviews/talmud_structure/sifra_talmud_links_*`).

MH answers: “What did the tradition treat as part of the same Oral conversation?”  
→ Those works are **possible Oral** for us.

### 6.4 What “possible” means (and does not)

**Means — allowed:**

| Allowed | Example |
|---------|---------|
| Open the locus | Sifra unit, Bavli daf, Mishnah, Tosefta, Rabbah, Mekhilta… |
| Name it on a unit | `source: Sifra …` / `Bavli Temurah 28a` |
| Use as parallel navigation | MH edge Sifra ↔ Zevachim |
| Keep on the allow-list even if genre is aggadic | Bereishit Rabbah stays **possible** |

**Does not mean:**

| Not implied | Why |
|-------------|-----|
| Best source for this unit | Job fit still matters |
| Equal to Written | Written remains derivation source |
| Automatic IF/THEN row | Still need Hebrew + dual-track + confidence |
| Ranked authority | MH is parallel, not a vote tally |
| Only MH works exist | Manual add if a classical work is missing from the graph |

### 6.5 Two gates (preference does not delete possible)

**Gate A — Possible (corpus)**

```text
IF work/locus appears in Mesorat haShas
THEN status = possible_oral
```

No subcategory ban: Midrash includes Sifra **and** Rabbah; both remain possible.

Rare categories (Tanakh-tagged Rashi, Halakhah codes, Chasidut) that appear on MH edges are still **possible under MH membership**; handle with clear labeling (commentary / code / etc.), not exclusion from the MH set.

**Gate B — Preferred for this job (guidance only)**

| Job | Prefer among possibles |
|-----|------------------------|
| Decode Leviticus verse word-by-word | Sifra (halakhic midrash) |
| Decode Exodus | Mekhilta |
| Modular standing ruling | Mishnah / Tosefta |
| Dispute, edge, integration | Bavli (via MH + cite_index) |
| Narrative / homiletic midrash | Rabbah-type midrash when unit wants that |
| Navigation only | MH edges themselves |

**Preferred** = “open first.”  
**Possible** = “never forbidden because it showed up in MH.”  
**Preferred ⊆ possible.** Never “ruled out because not preferred.”

### 6.6 Limits of MH alone

| MH does | MH does not |
|---------|-------------|
| Mark traditional library membership | Rank which parallel is “truer” |
| Navigate Sifra ↔ Bavli | Replace Written derivation |
| Keep Rabbah as possible | Force Rabbah into every legal IF |
| Positive signal for possible | Complete census (title variants may under-index) |

### 6.7 Implementation hooks (when we build)

Without inventing a new parallel index:

1. **Allow navigation** to any MH endpoint for a unit’s Written/Sifra locus.  
2. In Pre-Code Oral attachments, allow any MH-linked work with full `he` + translit + en + named locus.  
3. Optionally tag `oral_status: possible_mh` vs `oral_status: preferred_job` (preferred ⊆ possible).  
4. Non-MH sources (e.g. modern notes, pure Rashi without MH) remain **outside** “possible_mh”; may still be labeled secondary aids if explicitly used — separate channel.

---

## 7. How to separate classical Oral from “extra studies”

Without using “uninspired” as a technical filter:

### Strong positive signals for classical Oral *texts*

1. Inside traditional corpora (Mishnah, Tosefta, Talmudim, midreshei halakhah/aggadah)  
2. **MH member** → automatic **possible Oral**  
3. Hebrew/Aramaic primary in our `_he` files  
4. Citeable traditional locus (tractate/daf, midrash section, mishnah chapter)  
5. Speaks in sage/school/baraita voice, not “I, Professor X, argue…”

### Secondary aids (not peer Oral books)

- Medieval commentaries (Rashi, Tosafot, Ramban…) — explain Tier classical texts  
- Codes (Mishneh Torah, Shulchan Arukh) — reorganize law  
- English editions (Steinsaltz, etc.) — accessibility  

Use with label; **not** as silent Oral source equal to Sifra.

### Meta only (not Oral Torah)

- Modern academic dating, literary theory, source criticism as *primary rule input*  
- Blogs, ELS, gematria-as-structure, anonymous summaries  

May inform our **method notes**; must not fill unit IF/THEN as Oral.

### Ambiguous edges

| Item | Handling |
|------|----------|
| Baraita only in Bavli | Possible Oral **as Bavli baraita**; don’t invent “= Sifra” without match |
| Minor tractates / Avot de-R. Natan | Classical periphery — name them; use carefully |
| Zohar / later Kabbalah | Out of default Lev legal path unless unit explicitly wants that corpus |
| Work classical but missing from MH graph | May still be classical; MH absence ≠ ban |

---

## 8. Earlier “tier” language vs “possible”

Research first sketched **tiers** (0 core, 1 aggadah, 2 commentary, 3 academic).  

**Update under MH policy:**

| Old tier idea | Current framing |
|---------------|-----------------|
| Tier 0 must-use only | **Possible** = all MH members; **preferred** by job |
| Tier 1 “weaker Oral” | Still **possible** if MH; genre-aware use |
| Tier 2 commentary | Secondary aid unless it appears on MH (then possible with label) |
| Tier 3 modern study | Meta — not Oral text |

We **do not** use tiers to **exclude** MH midrash (including Rabbah).  
We **do** use job preference so legal units still lead with Sifra/Mishnah/Bavli appropriately.

---

## 9. Fit to Written architecture (Passes 1–5)

| Written architecture idea | Oral complement |
|---------------------------|-----------------|
| Sequential run | Halakhic midrash walks books in order |
| Registries / types | Sifra include/exclude fills edge members |
| Imports (Exod → Lev) | Bavli “as written” + environment names |
| Validators | Often Oral on Written hooks (e.g. animal bans) |
| Pipelines | Sifra on steps; Bavli disputes |
| Genres (case / sequence / speech) | Oral has matching packaging (midrash vs mishnah vs sugya) |
| Cross-links | MH = Oral↔Oral call graph |

Metaphor for build order (not theology):  
**Written ≈ OS + data + apps.**  
**Halakhic midrash ≈ decoder / typechecker.**  
**Mishnah ≈ exported API modules.**  
**Talmud ≈ debugger + integration + dispute log.**  
**MH ≈ possible-Oral membership + parallel edges.**

---

## 10. Local corpus inventory (snapshot)

Present under `Data/` (non-exhaustive):

- `sifra_he.json`  
- `mekhilta_he.json`, `mekhilta_rashbi_he.json`  
- `sifrei_bamidbar_he.json`, `sifrei_devarim_he.json`  
- `mishnah_*_he.json` (full set of tractates in dump)  
- `tosefta_*_he.json`  
- `bavli_*_he.json`  
- `yerushalmi_*_he.json`  
- selected Rabbah / other midrash  
- `links0.csv` … `links8.csv` (includes MH)

Extracts: `reviews/talmud_structure/sifra_talmud_links_*`, Lev 1:2 research, etc.

---

## 11. Practical rules for units (summary)

1. **Written Hebrew first** (tree/genre/registry tags from architecture).  
2. Attach Oral only with **named locus** + he + translit + en.  
3. Any **MH-linked** work is **possible Oral** — do not rule it out.  
4. **Prefer** by job (Sifra on Lev decode, etc.) without excluding other MH.  
5. Secondary non-MH commentary = aid only, labeled.  
6. Modern study = method notes only, not Oral rules.  
7. Baraita identity: “in Bavli” ≠ automatic “from Sifra” without text/MH support.  

---

## 12. Open research questions

1. Extract unique MH work list → `possible_oral_works_*.json`?  
2. Sample: Lev 1:2 Sifra ↔ MH Bavli baraita — match rate to Tosefta/Mishnah wording?  
3. School tags on units when de-vei R. Yishmael appears?  
4. How to record MH-possible but job-nonpreferred attachments without cluttering frozen units?  
5. Subtag rare MH Halakhah/Chasidut sides as `possible_mh_edge` vs main four categories? (Still not ruled out.)  
6. Align unit schema field names when next Lev unit is patched.

---

## 13. Related files

| File | Role |
|------|------|
| **This file** | **Single** canonical research doc: valid Oral + MH possible policy |
| `STANDING_DECISIONS.md` §5 | Standing rule pointer |
| Architecture pass 1–5 | Written system context |
| `ORAL_CODES_WRITTEN_*` | Midrash operators as coding language |
| `reviews/talmud_structure/sifra_talmud_links_*` | MH Sifra↔Talmud extract |

---

## 14. Bottom line

**Valid classical Oral for this project** is the traditional rabbinic library (Mishnah, Tosefta, Talmudim, midreshei halakhah and — as possible — aggadah), navigated especially via **names, schools, loaders, and Mesorat haShas**.

**What was first:** living Oral before books; **Mishnah** first as major written code; **midrash** as parallel Tannaitic decoder genre; **Talmud** later on Mishnah.

**Sifra’s opening** teaches **method** (13 middot, school of R. Yishmael).

**Mesorat haShas:** every reference is **possible Oral** — **none ruled out**; job preference only orders attention.

**Derivation order stays:** Written → preferred Oral decoder for that book → other possible Oral via MH/cites → dual-track Pre-Code freeze.
