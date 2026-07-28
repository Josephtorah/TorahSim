# Architecture Pass 2 — Written→Written pointers

**Date:** 2026-07-19  
**Kind:** architecture scan (hypothesis / working model — not binding law)  
**Pass:** 2 of multi-pass series  
**Question:** How does later Written text **know where to look** for earlier data/state/commands?  
**Prior:** `ARCHITECTURE_pass1_five_books_2026-07-19.md`, `ARCHITECTURE_discussion_2026-07-19.md`  

**Corpus:** `Data/{Gen,Exod,Lev,Num,Deut}.xml` (OSHB-style). Counts use **normalized** Hebrew (morph `/` and cantillation stripped) so phrase search works.

On update: rename file to today’s date; fix links (`STANDING_DECISIONS` §0).

---

## 0. Pass 2 in one sentence

The Written Torah rarely uses modern “see verse X:Y” syntax; it uses **content pointers** — shared names, “as YHWH commanded,” memory formulas, narrative continuity, and class-word joins — so a sequential run can **resolve** earlier install/data without leaving the five books.

---

## 1. Pointer style catalog

| ID | Style | What it does | Rough scale (this corpus scan) |
|----|--------|--------------|--------------------------------|
| **P-NAME** | Shared proper/class name | Later verse uses a name defined/installed earlier | e.g. אהל מועד ~129; משכן ~91; בני אהרן ~27 |
| **P-CMD** | Command compliance | “as he commanded” binds act to prior instruction | כאשר צוה ~64; אשר צוה ~108 |
| **P-SPEAK** | Speech fulfillment | “as he spoke/said” binds to prior promise/speech | כאשר דבר ~39 |
| **P-STATE** | Narrative continuity | Next book/unit assumes prior end-state | Gen 50 → Exod 1; Exod 40 → Lev 1 |
| **P-MEM** | Memory / do-not-forget | Explicit “remember / lest you forget” | זכור/וזכרת ~20; פן תשכח cluster mostly Deut |
| **P-TODAY** | “Which I command you today” | Live re-bind of law under Moses’ voice | אשר אנכי מצוך ~37 (almost all Deut) |
| **P-JOIN** | Same class word, multi-table | Same Hebrew type joins different lists | בהמה in Lev 1 vs Lev 11 vs Deut 14 |
| **P-PLACE** | Chosen place / entrance | Location key for rites | פתח אהל מועד ~42; Deut “place YHWH will choose” |
| **P-PARALLEL** | Restated law | Second formulation points at first | Sabbath Exod 20 ↔ Deut 5; Pesach calendar |

**Not found as primary system:** formal numeric cross-references inside the scroll (those are later reader apparatus).

**Confidence:** style inventory = **tested (observable)**; “this is how the Torah computes” = **hypothesis**.

---

## 2. Worked spine: sanctuary install → operate → move

This is the clearest Written→Written pointer chain for the project.

### 2.1 Install (Exodus) — writes the symbol table

**Command to build / pattern**

- **Exod 25:8** — וְעָשׂוּ לִי מִקְדָּשׁ / *ve’asu li mikdash* / “They shall make me a sanctuary” … וְשָׁכַנְתִּי בְּתוֹכָם / *veshakhanti betokham* / “and I will dwell among them.”  
  **Writes:** goal state = sacred dwelling among Israel.

- **Exod 25:9** — כְּכֹל אֲשֶׁר אֲנִי מַרְאֶה אוֹתְךָ … תַּבְנִית הַמִּשְׁכָּן / *kekhol asher ani mar’eh otkha … tavnit ha-mishkan* / “according to all that I show you… the pattern of the mishkan.”  
  **Pointer type:** P-CMD + visual pattern (blueprint as data).

**Where speech will happen**

- **Exod 29:42** — עֹלַת תָּמִיד … פֶּתַח אֹהֶל מוֹעֵד לִפְנֵי יְהוָה אֲשֶׁר אִוָּעֵד לָכֶם שָׁמָּה לְדַבֵּר אֵלֶיךָ שָׁם / *olat tamid … petach ohel mo’ed lifnei YHWH asher ivva’ed lakhem shammah ledabber eleikha sham* / continual burnt offering at the entrance of the Tent of Meeting… where I will meet you to speak with you.  
  **Writes:** location key **פתח אהל מועד** + meeting/speech function.

**Activation**

- **Exod 40:34–35** — cloud covers אֹהֶל מוֹעֵד; כְּבוֹד יְהוָה fills הַמִּשְׁכָּן; Moses cannot enter.  
  **Writes:** runtime state = presence online; machine is live.

### 2.2 Operate (Leviticus) — resolves those names without re-installing

- **Lev 1:1** — וַיְדַבֵּר יְהוָה אֵלָיו מֵאֹהֶל מוֹעֵד / *vayedabber YHWH elav me-ohel mo’ed* / YHWH spoke to him **from the Tent of Meeting**.  
  **P-NAME + P-STATE:** speech location only makes sense after Exod 29:42 / 40:34–35. No rebuild of the Tent in Lev 1.

- **Lev 1:3** — אֶל פֶּתַח אֹהֶל מוֹעֵד יַקְרִיב אֹתוֹ / *el petach ohel mo’ed yakriv oto* / he shall bring it to the **entrance of the Tent of Meeting**.  
  **P-PLACE** resolving the Exodus location key into an offering procedure.

- **Lev 1:5, 1:7** — בְּנֵי אַהֲרֹן הַכֹּהֲנִים / *benei Aharon ha-kohanim* / sons of Aaron the priests (blood, fire).  
  **P-NAME** resolving **Exod 28+** priest design into operators of the pipeline.

- **Lev 8:4–5, 8:36; 9:6** — וַיַּעַשׂ מֹשֶׁה כַּאֲשֶׁר צִוָּה יְהוָה / *vaya’as Moshe ka’asher tzivvah YHWH* / Moses did as YHWH commanded; “this is the thing YHWH commanded to do.”  
  **P-CMD:** execution phase explicitly binds to prior command payload (Exodus consecration instructions).

- **Lev 10:1** — Nadav and Avihu bring unauthorized fire.  
  **Architecture:** failed input against installed protocol; shows resolution is not optional.

### 2.3 Move (Numbers) — same symbols, new logistics

- **Num 1:1** — speech בְּמִדְבַּר סִינַי בְּאֹהֶל מוֹעֵד / *be-midbar Sinai be-ohel mo’ed* / in the wilderness of Sinai, in the Tent of Meeting + **calendar stamp** (second year, second month).  
  **P-NAME + P-STATE:** Tent still the center; time index continues after Exodus.

- **Num 9:15–17; 10:11** — cloud on the mishkan; when cloud lifts, they journey.  
  **P-STATE:** travel control linked to presence object installed in Exodus.

### 2.4 Restate (Deuteronomy) — policy pointer shift

- **Deut 12:5, 12:11** — הַמָּקוֹם אֲשֶׁר יִבְחַר יְהוָה / *ha-makom asher yivchar YHWH* / the place YHWH will choose, to set his name there — bring offerings **there**.  
  **Not** “go to the portable Tent entrance” as in Lev 1:3.  
  **Architecture:** forward/land pointer that **rebinds** cult location policy for settled life, while still assuming the prior history of presence and law.

**Pass 2 claim:** Sanctuary nouns in Lev/Num are **imported keys**. Exodus is the main **writer** of that table; Lev/Num are **readers**; Deut **rebinds** place for the land.

---

## 3. Book-to-book continuity pointers (P-STATE)

### Genesis → Exodus

- **Gen 50:26** — Joseph dies, embalmed, placed in a coffin **in Egypt**.  
- **Exod 1:1** — וְאֵלֶּה שְׁמוֹת בְּנֵי יִשְׂרָאֵל הַבָּאִים מִצְרָיְמָה / *ve’elleh shemot benei Yisrael ha-ba’im mitzraymah* / “And these are the names of the sons of Israel who came to Egypt…”  

**No reset.** Exodus opens by **continuing** the Egypt state and the people-list. Classic sequential run.

### Exodus → Leviticus

- End Exod 40: presence fills mishkan.  
- Start Lev 1:1: speech **from** Tent of Meeting.  

**Pointer:** presence-state → legal speech channel.

### Across the wilderness books

Numbers stamps time/location on speech (Num 1:1). Deuteronomy opens with Moses’ words **beyond the Jordan** (Deut 1:1) and dates the address (Deut 1:3) — **geographical program counter** after the journey.

---

## 4. Command pointers (P-CMD) — “as commanded”

### Scale (normalized search)

| Phrase family | ~Hits | Heaviest books |
|---------------|------:|----------------|
| כַּאֲשֶׁר צִוָּה / *ka’asher tzivvah* / “as he commanded” | ~64 | Exod 23, Num 19, Lev 12, Deut 6, Gen 4 |
| אֲשֶׁר צִוָּה / *asher tzivvah* / “which he commanded” | ~108 | Exod 37, Num 34, Lev 20, Deut 11, Gen 6 |

### Behavior

These formulas do **not** always name the target verse. They mean: **bind this act to an already-issued instruction.** Resolution is:

1. Nearby prior speech in the same unit, or  
2. Known install block (e.g. Exod 25–31 / 35–40 for Tabernacle doing), or  
3. Earlier book’s standing command.

### Examples

- **Gen 6:22; 7:5** — Noah does כְּכֹל אֲשֶׁר צִוָּה / *kekhol asher tzivvah* / according to all he was commanded.  
  **Local:** command in the flood speech; compliance pointer inside Genesis.

- **Lev 8:4** — Moses assembles the congregation at Tent entrance כַּאֲשֶׁר צִוָּה יְהוָה / *ka’asher tzivvah YHWH*.  
  **Cross-block:** points at consecration commands (Exod + Lev 8’s own framing).

- **Deut 5:12** — שָׁמוֹר אֶת יוֹם הַשַּׁבָּת … כַּאֲשֶׁר צִוְּךָ יְהוָה אֱלֹהֶיךָ / *shamor et yom ha-shabbat … ka’asher tzivvekha YHWH elohekha* / guard the Sabbath day… **as YHWH your God commanded you**.  
  **P-CMD + P-PARALLEL:** explicit that this restatement binds to a **prior** Sabbath command (reader lands on Exod 20:8 זָכוֹר / *zakhor* / “remember,” with wording shift shamor/zakhor).

**Pass 2 insight:** P-CMD is the Written’s main **“call prior function”** operator. High density in Exod–Num = build/operate compliance culture.

---

## 5. Memory pointers (P-MEM) — remember / do not forget

### Scale

- זָכוֹר / וְזָכַרְתָּ family ~20 (Deut heavy).  
- “Lest you forget” cluster concentrated in **Deuteronomy** (~6 clear פן תשכח hits in scan).

### Examples

- **Exod 13:3** — זָכוֹר אֶת הַיּוֹם הַזֶּה / *zakhor et ha-yom ha-zeh* / remember this day you left Egypt.  
  **Writes a memory key** for festival identity.

- **Exod 20:8** — זָכוֹר אֶת יוֹם הַשַּׁבָּת / *zakhor et yom ha-shabbat* / remember the Sabbath day.

- **Deut 8:2** — וְזָכַרְתָּ אֶת כָּל הַדֶּרֶךְ / *vezakharta et kol ha-derekh* / you shall remember the whole way YHWH led you forty years.  
  **P-MEM → Numbers/Exodus journey as data.**

- **Deut 25:17–19** — זָכוֹר אֵת אֲשֶׁר עָשָׂה לְךָ עֲמָלֵק / *zakhor et asher asah lekha Amalek* / remember what Amalek did… when YHWH gives rest in the land, blot out Amalek.  
  **P-MEM** to Exod 17 war narrative + **forward** land condition.

- **Deut 4:9; 6:12; 8:11** — guard yourself **lest you forget** what eyes saw / YHWH who brought you out.  
  **Negative pointer:** do not drop the import of prior revelation.

**Pass 2 insight:** Deuteronomy is the **memory management** book — it forces the run to keep earlier phases loaded.

---

## 6. “I command you today” (P-TODAY) — rebind under Moses

~37 hits for אָנֹכִי מְצַוְּךָ / *anokhi metzavvekha* style; **~36 in Deuteronomy**.

- **Deut 4:2** — do not add/subtract from the word אֲשֶׁר אָנֹכִי מְצַוֶּה אֶתְכֶם / *asher anokhi metzavveh etkhem* / that I command you.  
- **Deut 6:2; 4:40**, etc. — statutes “which I command you **today**.”

**Architecture:** not “ignore Exodus–Numbers,” but **re-present** the law as a live command stream at the edge of the land. Pointer target = the Torah corpus Moses is delivering **now**, which itself summarizes prior history (P-MEM + P-STATE).

---

## 7. Class-word joins (P-JOIN) — data tables sharing keys

### Animal / behemah

| Locus | Role |
|-------|------|
| **Lev 1:2** | Offering input: מִן הַבְּהֵמָה מִן הַבָּקָר וּמִן הַצֹּאן / *min ha-behemah min ha-bakar u-min ha-tzon* |
| **Lev 11:2** | Food: זֹאת הַחַיָּה אֲשֶׁר תֹּאכְלוּ מִכָּל הַבְּהֵמָה / *zot ha-chayyah asher tokhelu mi-kol ha-behemah* |
| **Deut 14:4** | Food list: זֹאת הַבְּהֵמָה אֲשֶׁר תֹּאכֵלוּ שׁוֹר שֵׂה כְשָׂבִים… / *zot ha-behemah asher tokhelu shor seh khesavim…* |

**Same key, different tables.** Oral (Sifra on Lev 1) treats the join as a risk: if offering-behemah meant food-behemah’s full scope, wild game might enter; local cattle/flock locks the offering table.

**Pass 2 insight:** P-JOIN is where “Written is data” becomes operational — **multiple registries, one vocabulary.**

### Festival / Pesach

| Locus | Role |
|-------|------|
| **Exod 12:14** | Day as memorial; perpetual statute |
| **Lev 23:5** | Calendar: 1st month, 14th, between evenings — Pesach to YHWH |
| **Num 28:16** | Public offering schedule restates date |
| **Deut 16:1** | Guard Aviv month; do Pesach — because YHWH brought you out of Egypt in Aviv |

**Join on “Pesach” + date + Egypt memory.** Different books write **ritual**, **calendar**, **public korban schedule**, **land-facing festival law** on the same festival key.

### Sabbath restatement

- **Exod 20:8** זָכוֹר / remember  
- **Deut 5:12** שָׁמוֹר … כַּאֲשֶׁר צִוְּךָ / guard … as he commanded you  

**P-PARALLEL + P-CMD** in one pair.

---

## 8. Promise / speech fulfillment (P-SPEAK)

כַּאֲשֶׁר דִּבֶּר / *ka’asher dibber* / “as he spoke” ~39 hits (Deut 16, Exod 9, Gen 6, Num 7…).

Example:

- **Gen 12:4** — Abram goes כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה / *ka’asher dibber elav YHWH* / as YHWH spoke to him (command of 12:1).  
- **Gen 21:1** — YHWH visits Sarah as he said / does as he spoke.

**Pointer:** narrative compliance to prior **speech acts**, not only legal code blocks. Genesis uses this heavily for covenant trajectory that Deut later **remembers**.

Land promise data root:

- **Gen 15:18** — covenant: to your seed I give this land…  
  Later books resolve “the land YHWH swore” language against this kind of root (P-NAME/P-SPEAK hybrid).

---

## 9. Density map (where pointers are thick)

| Book | Pointer profile (Pass 2) |
|------|---------------------------|
| **Genesis** | P-STATE export to Exodus; P-SPEAK/P-CMD local compliance; seed P-JOIN vocabulary; little Tent |
| **Exodus** | **Writes** sanctuary name table; heavy P-CMD in build; memory keys (Pesach, Sabbath); priest names |
| **Leviticus** | **Reads** Tent/priests; P-CMD in inauguration; declares local type tables; P-JOIN risk with food lists |
| **Numbers** | Reuses Tent/cloud; logistics + time stamps; extends festival/offering schedules; stress narratives as data for Deut |
| **Deuteronomy** | **P-MEM capital**; P-TODAY rebind; P-CMD to prior commands; place-policy rebind; sermon as pointer-rich interface |

---

## 10. Implications for Torah_Grok

1. **When modeling Lev units**, tag free names with resolve targets:  
   `import: Exod.Tent`, `import: Exod.Priests`, `local: bakar/tzon types`.  

2. **P-CMD lines** in a unit are architectural gold — they mark “this step calls prior payload.”  

3. **Do not expect numeric hyperlinks** in Written; implement “pointers” as **name + prior-command + state** fields in Pre-Code notes.  

4. **Mesorat haShas** remains Oral↔Oral. Pass 2 is **Written↔Written**. Different index.  

5. **Pass 3:** type-registry inventory — **done:** `ARCHITECTURE_pass3_registries_2026-07-19.md`.  

6. **Pass 4 candidate:** sanctuary spine only, free-name resolve rate sample (count Lev 1–16 nouns → Exod vs local).  

---

## 11. Worked mini-example: Lev 1:1–5 as pointer resolution

| Token | he / translit / en | Resolve (Pass 2 hypothesis) | Style |
|-------|--------------------|-----------------------------|--------|
| from Tent | מֵאֹהֶל מוֹעֵד / *me-ohel mo’ed* / from Tent of Meeting | Exod 29:42; 40:34–35 | P-NAME, P-STATE |
| children of Israel | בְּנֵי יִשְׂרָאֵל / *benei Yisrael* | Gen people → Exod nation | P-NAME, P-STATE |
| animal/cattle/flock | בְּהֵמָה / בָּקָר / צֹאן | **Local type data** in Lev 1; join risk to Lev 11 / Deut 14 | P-JOIN (local write) |
| Tent entrance | פֶּתַח אֹהֶל מוֹעֵד | Exod 29:42 et al. | P-PLACE |
| sons of Aaron priests | בְּנֵי אַהֲרֹן הַכֹּהֲנִים | Exod 28+ install | P-NAME |
| before YHWH | לִפְנֵי יְהוָה | Presence at sanctuary (Exod activation) | P-STATE |

This is exactly “run Lev; look up data/state in earlier Written.”

---

## 12. Open questions (carry to Pass 3+)

1. How often does כַּאֲשֶׁר צִוָּה point **cross-book** vs **same-speech**? (needs sampled tagging)  
2. Is Deut 12’s “chosen place” best modeled as **new table** or **update** to Tent-entrance place key?  
3. Full registry list for **blemish / pure / kinship** home chapters.  
4. Can pe/samekh breaks mark **module boundaries** for pointer scope?  

---

## 13. Bottom line

**Pass 2 result:** Written “pointers” are real and classifiable. The densest architectural chain for this project is still:

```text
Exodus writes sanctuary keys and presence state
    → Leviticus resolves them into offering/purity procedures
    → Numbers runs them under travel/cloud logistics
    → Deuteronomy remembers the run and rebinds law/place for the land
```

Supporting operators: **as commanded**, **remember**, **as he spoke**, **shared class words**, **narrative end→start continuity**.

**Next pass (recommended):** Pass 3 — **type registries and data tables** (where animal, purity, office, and time lists live, and how they join).
