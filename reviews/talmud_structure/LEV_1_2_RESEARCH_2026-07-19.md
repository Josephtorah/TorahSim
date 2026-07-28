# Research pack: Leviticus 1:2 — all relevant links

**Verse:** Lev 1:2  
**Date:** 2026-07-19  
**Purpose:** Map every useful link layer for coding this verse (Oral → Pre-Code).  
**Machine dump:** `lev_1_2_research_2026-07-19.json`  
**Existing unit (partial):** `logic/units/lev_01_call_and_korban_opening.yaml` (already has Oral notes on adam/mikem/behemah)

**Not binding law** — research for derivation.

---

## 0. Written text (source of truth)

| | |
|--|--|
| **he** | דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם אָדָם כִּי־יַקְרִיב מִכֶּם קָרְבָּן לַיהוָה מִן־הַבְּהֵמָה מִן־הַבָּקָר וּמִן־הַצֹּאן תַּקְרִיבוּ אֶת־קָרְבַּנְכֶם |
| **he_translit** | *Daber el-benei Yisrael ve’amarta alehem: adam ki-yakriv mikem korban la-YHWH; min-ha-behemah min-ha-bakar u-min-ha-tzon takrivu et-korbanchem* |
| **en** | “Speak to the children of Israel and say to them: A person, when he will offer from you an offering to Hashem — from the animal, from the cattle and from the flock, you shall offer your offering.” |

**Logic atoms (Written face):**

| Atom | he | translit | en | Candidate role |
|------|-----|----------|-----|----------------|
| address | בני ישראל | *benei yisrael* | children of Israel | audience / agent class |
| person | אדם | *adam* | person | agent expand |
| from you | מכם | *mikem* | from you | agent filter |
| when offers | כי יקריב | *ki yakriv* | when one offers | trigger / modal |
| offering | קרבן לה׳ | *korban la-YHWH* | offering to Hashem | object class |
| from animals | מן הבהמה | *min ha-behemah* | from the animal | species superclass |
| cattle | מן הבקר | *min ha-bakar* | from cattle | species |
| flock | מן הצאן | *min ha-tzon* | from flock | species |

---

## 1. Link layers (what we searched)

| Layer | Source | Count | Role for coding |
|-------|--------|------:|-----------------|
| **A. Sifra walk** | Nedavah **Section 2** (11 segs) | 11 | **Primary coder** on this verse |
| **B. Mesorat haShas** | MH edges from Sifra Sec 2 | **50** | Oral rooms to open next |
| **C. Bavli paren cite** | `cite_index` `Lev.1.2` | **18** | Bavli lines that quote `(ויקרא א, ב)` |
| **D. All Sefaria links** to “Leviticus 1:2” | `Data/links*.csv` | **737** | Full web (mostly commentary + Tanakh) |
| **D′. Oral-only filter** of D | Talmud/Midrash/Mishnah | **~216** | Still noisy; prefer A–C first |

### Full 737 by connection type

| Type | ~N | Use? |
|------|---:|------|
| (empty) | 417 | Mixed; includes Talmud/midrash + chasidut/tanakh |
| commentary | 279 | Rashi/Malbim/etc. on the verse — secondary for us |
| midrash | 27 | Sifra + Vayikra Rabbah — **high** |
| reference | 7 | Jastrow — dictionary only |
| targum | 3 | Onkelos / Rasag — translation aid |
| allusion / parshanut | 4 | low priority |

**Policy:** For Pre-Code, read **A → B → C** first. Use D only when hunting a missing parallel. Do **not** treat 737 commentaries as coding sources.

---

## 2. Layer A — Sifra Section 2 (primary code sheet)

**Address:** `Sifra, Vayikra Dibbura d'Nedavah, Section 2`  
**Text:** `Data/sifra_he.json`

| Seg | Written hook | Oral operator | Rule (plain English) | Confidence |
|-----|--------------|---------------|----------------------|------------|
| **א** | דבר אל בני ישראל…וסמכו | membership | Israelites lean (**סמיכה** / *semikhah*); idolaters do not | tested (Sifra) |
| **ב** | בני ישראל | membership | Men lean; women — R. Yose/Shimon: optional leaning | tested |
| **ג** | אדם / מכם | לרבות / להוציא | **אדם** includes converts (**גרים** / *gerim*); **מכם** excludes apostates (**מומרים** / *mumarim*); locked via בני ישראל = covenant-receivers | tested |
| **ד** | אדם כי יקריב | יכול…ת״ל | Not obligatory decree → **רשות** / *reshut* / voluntary; also order: dedicate before offer (R. Yehudah) | tested |
| **ה** | קרבן | orthography | Always write divine Name properly (anti-heretic) | low for logic unit |
| **ו** | בהמה | יכול…ת״ל | Not wild game even if called behemah in Deut 14; need בקר+צאן | tested |
| **ז–ח** | מן הבהמה | להוציא | Exclude **רובע/נרבע** / *rovea/nirba* (sexually violated animals) | tested |
| **ט** | מן הבקר | להוציא | Exclude **נעבד** / *ne’evad* (worshipped animal) | tested |
| **י** | מן הבקר (also 1:3) | surplus word | Exclude **טריפה** / *terefah* (fatally injured) | tested |
| **יא** | מן הצאן / ומן הצאן | להוציא | Exclude **מוקצה** / *mukteh* (set aside for idolatry) and **נוגח** / *nogeakh* (goring) | tested |

**Coding pattern (global):** each surplus/restrictive word → include or exclude a class → lock with תלמוד לומר.

---

## 3. Layer B — Mesorat haShas from Sifra Section 2

**50 unique pairs** (Oral ↔ Oral).

### By category

| Category | N |
|----------|--:|
| Talmud | 24 |
| Midrash | 20 |
| Mishnah | 4 |
| Tanaitic | 2 |

### B1. Talmud (priority reading list)

| Sifra passage | ↔ Talmud | Likely theme (from nearby cites / Sifra) |
|---------------|----------|------------------------------------------|
| Sec 2:8–9, 10–11 | **Bava Kamma 40b:16–19** | Disqualified animals (violated / goring) |
| Sec 2:1 | Bava Kamma 62b:7 | (related damage / animal domain) |
| Sec 2:11 | Bekhorot 41a:15 | Flock exclusions |
| Sec 2:1–2 | **Chagigah 16b:15** | Women / leaning |
| Sec 2:2 | Chullin 85a:2–3 | (leaning / shelamim anecdote area) |
| Sec 2:1, 9, 1–2 | Eruvin 15a:20, 15b:3, 96b:7 | Scope / signs / women mitzvot parallels |
| Sec 2:9 | Gittin 21b:3 | |
| Sec 2:1–2, 8 | Kiddushin 36a:16, 66a:1 | Semikhah gender; apostate themes |
| Sec 2:10, 1 | Menachot 5b:7, 94a:1 | Terefah / lean |
| Sec 2:4 | Nedarim 10a:14–10b:1 | How one names an offering |
| Sec 2:11 | Niddah 41a:8 | |
| Sec 2:1–2 | **Rosh Hashanah 33a:6** | Women leaning baraita |
| Sec 2:9 | Sukkah 24b:3 | |
| Sec 2:7–10 | **Temurah 28a–29a** (several) | **Core:** rovea, ne’evad, mukteh, nogeakh |
| Sec 2:6 | **Zevachim 34a:15** | Behemah ≠ wild game |

### B2. Mishnah

| Sifra | ↔ Mishnah |
|-------|-----------|
| Sec 2:9 | Avodah Zarah 3:5 |
| Sec 2:1 | Bava Kamma 7:1 |
| Sec 2:1 | Eruvin 1:7 |
| Sec 2:1 | Menachot 9:9 |

### B3. Tosefta

| Sifra | ↔ Tosefta |
|-------|-----------|
| Sec 2:9 | Gittin 2:6 |
| Sec 2:1 | Zavim 5:4 |

### B4. Midrash (same-family / internal)

Includes: Bereishit Rabbah 1:13; Mekhilta (Yishmael + Rashbi) 20:14; Sifra Emor / Metzora / Shemini / Tzav; **internal Nedavah** cross-links (Sec 2 ↔ Ch 4, Sec 3, Sec 8).

---

## 4. Layer C — Bavli lines that quote `(ויקרא א, ב)`

**18 hits** via `cite_index` (`Lev.1.2`). These are the strongest “Talmud is looking at this verse” signals.

| Tractate | daf_i / line | What the line does (plain English) |
|----------|--------------|-------------------------------------|
| **bava_kamma** | 79 / 15 | Objection: min ha-behemah excludes rovea/nirba; bakar → ne’evad; tzon → mukteh; u-min ha-tzon → nogeakh |
| **bekhorot** | 80 / 10 | From flock/lambs/goats — exclude old, sick, filthy |
| **bekhorot** | 80 / 14 | Same disqualifier chain as BK |
| **chagigah** | 31 / 14 | Speak to Israel and lean — men lean, women optional (Yose/Shimon) |
| **chullin** | 8 / 9 | **מכם** not all of you → exclude mumar; accept offerings from sinners except open mumar / libation / public Shabbat |
| **chullin** | 25 / 5 | Same mumar baraita (accept korban to encourage teshuvah) |
| **kiddushin** | 70 / 15 | Semikhah: Israel lean, women do not (lemma) |
| **menachot** | 9 / 6 | “From cattle” below is surplus → exclude terefah |
| **menachot** | 179 / 12 | adam ki yakriv… — may bring cattle **or** flock (not forced both) |
| **menachot** | 184 / 13 | Blind person / who leans — Israel lean, not idolaters |
| **menachot** | 207 / 6 | Grammar of “shall offer” vs freewill |
| **nazir** | 68 / 7 | **כלל ופרט** reading: min (detail) + behemah (general) + bakar/tzon (detail) |
| **niddah** | 80 / 7 | Same animal-disqualifier baraita |
| **rosh_hashanah** | 64 / 5 | Women leaning: Yehudah vs Yose/Shimon |
| **sukkah** | 58 / 1 | Stolen animal before/after despair — “from you” must be yours |
| **temurah** | 54–55 | Rovea/nirba barred for altar (same Sifra chain) |
| **zevachim** | 66 / 14 | If only “behemah” would include wild; **bakar u-tzon** lock domestic |

### Theme clusters (for logic rows)

| Theme | Key Bavli (cite layer) | Sifra seg |
|-------|------------------------|-----------|
| Animal disqualifiers | BK 79, Bekhorot 80, Temurah 54–55, Niddah 80 | ז–יא |
| Behemah ≠ wild | Zevachim 66 | ו |
| Mumar / mikem | Chullin 8, 25 | ג |
| Semikhah gender/nation | Chagigah 31, RH 64, Kiddushin 70, Menachot 184 | א–ב |
| Terefah surplus | Menachot 9 | י |
| Cattle or flock (not both required) | Menachot 179 | (related) |
| Ownership “from you” | Sukkah 58 | (mikem / mikkem sense) |
| Kelal u-perat structure | Nazir 68 | whole list |

---

## 5. Layer D — Direct “Leviticus 1:2” web (optional)

**737** edges. For coding, keep only Oral categories (~216 after filter).  
Many empty-type “Talmud” rows are Steinsaltz/Rashi-on-Talmud **wrappers** of the same dafim already in B/C.

**High-value midrash (connection type `midrash`):**

- Sifra Nedavah Section 2 (passages 2,4,5,7–10) and Chapter 3 (several)
- Vayikra Rabbah 2:1, 2:4–10
- Midrash Aggadah Lev 1:2:1–3

**Commentaries (secondary aids only):** Rashi, Or HaChaim, Malbim, Gur Aryeh, Kli Yakar, Chizkuni, Meshech Hochma, …

**Targum:** Onkelos Lev 1:2 — gloss aid, not IF/THEN source.

---

## 6. Unified priority queue (what to read to code)

### Must-read (code-bearing)

1. **Sifra Nedavah Section 2** (full, 11 segs) — already summarized §2  
2. **Temurah 28a–29a** + **Bava Kamma 40b** — animal bans  
3. **Zevachim 34a / 66** (cite) — domestic animals only  
4. **Chullin 5a–area / 8 / 25** — mumar / mikem  
5. **Chagigah 16b + RH 33a/64** — women leaning  
6. **Menachot 5b, 9, 179** — terefah; cattle-or-flock  

### Should-read (structure / edge)

7. Nazir 35a / 68 — kelal u-perat  
8. Menachot 93–94 — leaning who  
9. Sukkah 30a / 58 — stolen / ownership  
10. Mishnah Menachot 9:9, Bava Kamma 7:1  

### Later / not for first YAML pass

- Full 279 commentaries  
- Chasidut / Zohar / Musar from the 737  
- Duplicate Steinsaltz rows  

---

## 7. Draft logic surface (from links — not yet frozen unit)

```text
WHEN person offers (Lev 1:2):
  AGENT:
    - Written: "person from you" among Israel-address
    - Oral: INCLUDE converts (adam); EXCLUDE mumarim (mikem)  [Sifra ג; Chullin]
    - Oral: leaning — Israel yes; idolaters no; women optional (dispute) [Sifra א–ב; Chagigah/RH]
  MODAL:
    - Oral: voluntary (reshut), not forced decree [Sifra ד]
  ANIMAL:
    - Written: behemah + bakar + tzon
    - Oral: EXCLUDE wild even if called behemah elsewhere [Sifra ו; Zevachim]
    - Oral: EXCLUDE rovea/nirba, ne'evad, terefah, mukteh, nogeakh [Sifra ז–יא; Temurah/BK]
  SPECIES CHOICE:
    - Oral: cattle OR flock OK (not required both) [Menachot 179]
```

**Provenance rule:** Written rows vs Oral rows stay **dual-track** (as in existing `lev_01_call_and_korban_opening.yaml`).

---

## 8. Relation to existing Pre-Code unit

`logic/units/lev_01_call_and_korban_opening.yaml` already records:

- ORAL_sifra_adam_mikem  
- ORAL_sifra_behemah_bakar_tzon_only  
- ORAL animal disqualifiers (partial)  
- Open Q on mikem Written-only vs Oral  

This research pack **grounds** those Oral notes with full MH + cite_index + Bavli snippets.  
Next derivation step: expand/freeze animal-filter + agent-filter rows with **explicit daf citations** from §3–4.

---

## 9. Files

| File | Contents |
|------|----------|
| `LEV_1_2_RESEARCH_2026-07-19.md` | This human report |
| `lev_1_2_research_2026-07-19.json` | Raw: Sifra segs, MH 50, cite 18 lines, 737 link rows |
| `Data/sifra_he.json` | Sifra text |
| `Data/links*.csv` | Full link graph |
| `cite_index_2026-07-18.json` | Bavli `(ויקרא א, ב)` map |
| `ORAL_CODES_WRITTEN_2026-07-19.md` | Method (MH = map, Sifra = code) |

---

## 10. Bottom line

For **Lev 1:2**, the Oral coding is concentrated in:

1. **Sifra Nedavah Section 2** (word-by-word filters)  
2. **~24 MH Talmud dafim** (especially Temurah 28–29, BK 40b, Zevachim, Chullin, Chagigah/RH)  
3. **18 Bavli paren cites** of the verse (same themes, some extra: Nazir kelal-u-perat, Sukkah ownership, Menachot or/flock)

The **737** full-web links are mostly commentary/Tanakh noise for our purpose.

**Recommended next:** turn §7 into an expanded Pre-Code unit (or patch `lev_01_call_and_korban_opening.yaml`) with named Oral loci from this pack.
