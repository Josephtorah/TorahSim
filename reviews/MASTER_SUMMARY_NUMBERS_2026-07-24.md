# Master summary — Numbers (Pre-Code draft)

**Date:** 2026-07-24  
**Kind:** book summary for Torah_Grok stack (Written Pre-Code) — **not** binding religious law  
**Status:** first-draft complete · 47 units · 1289 verse trees  
**Hebrew book:** בְּמִדְבַּר / *Be-midbar* / “In the wilderness”  
**Data:** `Data/Num.xml` · Oral densify dump: `Data/sifrei_bamidbar_he.json`  
**Units:** `logic/units/num_*.yaml` · Build: `NUMBERS_BUILD_2026-07-24.md`

On substantive update: rename to today’s date and fix links.

---

## 1. One-line role in the five-book stack

```text
Genesis (platform) → Exodus (nation + Tent install) → Leviticus (sanctuary apps)
  → Numbers (ops: census, camp, march, tests, land prep) → Deuteronomy (recompile / speech)
```

Numbers does **not** re-boot the mishkan or re-author Leviticus purity/korban type systems. It runs the **already-installed** people + Tent **in motion**: count them, arrange them, move them, test them, and prepare inheritance west (and some east) of the Jordan.

---

## 2. Book shape (content arc)

| Segment | Ch. | What it is (English) | Code flavor |
|---------|-----|----------------------|-------------|
| **A. Ops install** | 1–4 | War census; camp by standards; Levites replace firstborn; clan duties ages 30–50 | Registries + layout boot + procedure |
| **B. Camp holiness** | 5–7 | Send impure out; sotah; nazir; priest blessing; 12-day altar dedication | Decision/procedure islands + registry |
| **C. Go live** | 8–10 | Menorah; Levite purify/wave; Pesach II; cloud rule; trumpets; leave Sinai | Procedure + march FSM |
| **D. Crisis core** | 11–14 | Complaints/quail; Miriam; spies; rejection + 40-year decree | Narrative FSM |
| **E. Law + Korach** | 15–17 | Land-entry offerings, challah, high-hand; wood-gatherer + tzitzit; Korach; staff | Decision + crisis FSM |
| **F. Support systems** | 18–19 | Priest/Levite dues & tithes; red heifer / corpse impurity water | Decision + purity FSM |
| **G. Generation turn** | 20–21 | Meribah; Edom block; Aaron dies; copper snake; Sihon & Og | Narrative FSM |
| **H. Outside view** | 22–24 | Bilʿam: cannot curse; blesses; star from Jacob | Narrative / oracles |
| **I. Reset for land** | 25–27 | Peor / Pinchas; second census; heiresses; Joshua appointed | Narrative + inheritance law |
| **J. Calendar + vows** | 28–30 | Tamid / Shabbat / months / moʿadim musafim; vow annulment matrix | Calendar decision tables |
| **K. Close logistics** | 31–33 | Midian war & spoil; Gad/Reuben east; full itinerary + drive-out | Narrative + logistics |
| **L. Land law close** | 34–36 | Borders; allotment princes; refuge cities; heiress same-tribe rule | Registry + decision |

**OSIS size:** 36 chapters · **1289** verses (Num 25 has **19** vv in local XML).

---

## 3. What Numbers “exports” (systems worth remembering)

### 3.1 Nation as runtime object
- **Census I** (ch. 1): males 20+ war-ready → **603,550**; Levites **not** in that count.  
- **Camp geometry** (ch. 2): four standards around the Tent; march order mirrors camp.  
- **Levi as mishkan crew** (ch. 3–4, 8): given instead of firstborn; Gershon / Kehat / Merari charges; Kehat carry-only after priests cover holy things.  
- **Census II** (ch. 26): after Peor plague → **601,730**; land by lot scaled to counts; Sinai generation gone except **Caleb** and **Joshua**.

### 3.2 Camp purity & person-status law (islands)
- Impure (tzaraʿat / zav / corpse) **sent outside** the camp (5).  
- **Sotah** / jealousy ordeal (5).  
- **Nazir** vow: wine, hair, corpse; restart if defiled; completion offerings (6).  
- **Priestly blessing** formula (6).  
- **Pesach sheni** for impure or distant (9).  
- **Red heifer** ash → *mei niddah* for corpse impurity days 3 & 7 (19).  
- **Cities of refuge** + murder vs error + high-priest gate (35).  
- **Vows:** man bound; father/husband same-day silence or annul (30).  
- **Heiresses:** daughters inherit if no son (27); must marry **within father’s tribe** so inheritance stays (36).

### 3.3 March & presence control
- **Cloud** settles → camp; lifts → journey; “by the mouth of YHWH” (9).  
- **Silver trumpets:** assemble, march alarms, war, moʿadim (10).  
- Ark formulas: *kumah* / *shuvah* (10).  
- Full **masʿei** itinerary Egypt → plains of Moab (33).

### 3.4 Crisis / test pattern (hypothesis label)
Repeated pattern in narrative blocks: **complaint or challenge → judgment or plague → mediation (Moses/Aaron/Pinchas) → named place or decree**. Major nodes: Taberah / Kivrot ha-Taʾavah (11), Miriam (12), spies + 40 years (13–14), Korach (16–17), Meribah (20), Peor (25).

### 3.5 Land prep
- East bank: Sihon & Og (21); Gad / Reuben / half-Menasheh under **armed-before-YHWH** condition (32).  
- West prep: borders (34); princes for lot (34); drive-out or “thorns” warning (33); refuge cities (35); tribe-locked heiresses (36).  
- Succession: **Joshua** leaned with majesty; **Eleazar** + Urim for go-out / come-in (27).

### 3.6 Calendar restatement (not first invention)
Ch. 28–29 restate **tamid**, Shabbat/month musafim, and moʿadim loads (esp. Sukkot bulls 13→7). Imports Lev 23 / Exod 29 as background; Numbers supplies **ops quantities** for the march generation and beyond.

---

## 4. Free-name imports (do not rebuild)

| Class | Resolve to | Examples in Numbers |
|-------|------------|---------------------|
| **EXOD_IMPORT** | Tent install, priesthood, cloud seed, firstborn Egypt memory | ohel moʿed, altar, Aaron/sons, cloud on mishkan |
| **LEV_IMPORT** | Purity grades, korban types, blood/fat, moʿadim skeleton | chatat/olah/shelamim, tumʾah types, YK as background |
| **GEN_AMBIENT** | People / land promise memory | Israel as people, land oath language |
| **NUM_LOCAL** | Authored mainly here | census rules, camp order, sotah/nazir/parah, miklat, heiress lock, masʿei |

---

## 5. Pre-Code packaging (what we built)

| Metric | Value |
|--------|--------|
| Units | **47** `num_*.yaml` |
| Verses / trees | **1289** (v1 taʾamim, full `tree_ascii`) |
| Status | **draft** (hypothesis overall; trees tested via parser) |
| Generator | `artifacts/generate_numbers_units.py` |
| Oral | Written first; **Sifrei Bamidbar** samples on primary/medium law blocks; dual-track only |
| BR required? | **No** |

Genre split (unit `genre` field):

- **boot_steps / registry:** census, camp, dedication, itinerary, borders  
- **decision_table:** sotah, nazir, offerings, dues, parah, calendar, vows, refuge, heiresses  
- **narrative_fsm:** complaints, spies, Korach, Meribah, Bilʿam, Peor, Midian, etc.

---

## 6. Phase map (quick index)

| Phase | Blocks | Unit range | Chapters |
|-------|--------|------------|----------|
| A | 01–10 | `num_01_*` … `num_04_*` | 1–4 |
| B | 11–16 | `num_05_*` … `num_07_*` | 5–7 |
| C | 17–19 | `num_08_*` … `num_10_*` | 8–10 |
| D | 20–23 | `num_11_*` … `num_14_*` | 11–14 |
| E | 24–27 | `num_15_*` … `num_17_*` | 15–17 |
| F | 28–29 | `num_18_*` … `num_19_*` | 18–19 |
| G | 30–31 | `num_20_*` … `num_21_*` | 20–21 |
| H | 32–34 | `num_22_*` … `num_24_*` | 22–24 |
| I | 35–37 | `num_25_*` … `num_27_*` | 25–27 |
| J | 38–41 | `num_28_*` … `num_30_*` | 28–30 |
| K | 42–44 | `num_31_*` … `num_33_*` | 31–33 |
| L | 45–47 | `num_34_*` … `num_36_*` | 34–36 |

Full refs table: `NUMBERS_BUILD_2026-07-24.md` §5.

---

## 7. High-value law islands (deepen later)

If a second pass is needed, prefer these for Sifrei / decision-table depth (not required for Deut start):

1. **Sotah** (5:11–31) · **Nazir** (6:1–21)  
2. **Pesach sheni** + cloud ops (9)  
3. **Shgagah vs yad ramah** + challah (15)  
4. **Priest/Levite dues** (18) · **Parah** (19)  
5. **Moʿadim musafim** (28–29) · **Vows** (30)  
6. **Miklat / murder matrix** (35) · **Heiress tribe lock** (36)  
7. **Zelophehad + Joshua** (27)

---

## 8. Handoff to Deuteronomy

Numbers leaves the system at:

- Plains of **Moab**, east of Jordan opposite Jericho  
- Second-census people ready for lot inheritance  
- **Joshua** designated; **Eleazar** high priest  
- East tribes conditioned; west borders named; miklat framework set  
- Sinai generation mostly dead; land entry still ahead  

Deuteronomy’s natural job: **recompile** (speech, covenant restatement, law migration brief) for that audience — not re-census the camp from zero.

---

## 9. Confidence / limits

- Experimental Pre-Code model; **not** binding religious law.  
- First draft: trees are parser-tested; logic steps and IF rows are **hypothesis** pending human deepen.  
- Sifrei samples are **dual-track** excerpts, not a full midrash alignment per verse.  
- English in units is gloss `[EN-AID]` only; derivation source remains Hebrew Written.

---

## Related

- Build: `reviews/NUMBERS_BUILD_2026-07-24.md`  
- Continuity: `reviews/PROMPT_continue_numbers_2026-07-24.md`  
- Standing: `reviews/STANDING_DECISIONS.md`  
- Prior books: `EXODUS_BUILD_2026-07-21.md` · `LEVITICUS_BUILD_2026-07-21.md` · `ARCHITECTURE_genesis_stack_2026-07-21.md`
