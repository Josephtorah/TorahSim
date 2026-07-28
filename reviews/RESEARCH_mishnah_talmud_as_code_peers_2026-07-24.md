# Research: peers studying Mishnah / Talmud “as code”

**Date:** 2026-07-24  
**Kind:** web intake + project fit · **not** binding law  
**Status:** first pass for Mishnah chapter-summary track  

**Related:** `mishnah_chapter_summaries/` · `reviews/Talmudic-Logic-Project/` · Pre-Code `logic/`  

---

## 0. Language policy (corrected 2026-07-24)

| Rule | Detail |
|------|--------|
| **Hebrew first** | Always show Hebrew when a term/phrase is discussed |
| **Then English** | Same place: transliteration + plain English so a non-reader of Hebrew can follow |
| **Never bare Hebrew** | Matches `Agents.md` / Pre-Code rules |
| **Not “English first”** | That was a mistaken agent gloss of “translate to English.” Owner: Hebrew first, English explains. |

Form: `עברית / translit / "English gloss"` or structured `he` + `he_translit` + `en`.

---

## 1. What שְׁמַע / *Shema* means

**שְׁמַע / she-MA / “Hear!” / “Listen!”**

In Jewish practice the name **Shema** refers to the **core daily declaration of God’s oneness and loyalty**, built from Torah passages (mainly Deuteronomy 6:4–9, plus following paragraphs, and Numbers 15:37–41). People often call the whole recitation package “the Shema.”

**Mishnah Berakhot chapter 1** is not a midrash essay on the word “hear.” It specifies **when and how you perform that daily recitation** (time windows, posture debate, blessing wrappers, mentioning the Exodus at night).

---

## 2. Peer landscape (who treats this like code / logic / systems)

### A. Talmudic Logic Project (strongest scholarly peer)

| | |
|--|--|
| **Who** | Michael Abraham, Dov Gabbay, Uri Schild (+ volumes by others) |
| **What** | Long-running series: formal logic models of Talmudic reasoning |
| **Home** | College Publications — *Studies in Talmudic Logic* |
| **Topics (examples)** | Non-deductive inference; *klal u-prat* as set definition; **deontic** logic (obligation/permission); **temporal** logic; conflict / normative loops |
| **In our repo** | `reviews/Talmudic-Logic-Project/` (PDF samples already) |
| **Take for us** | Model **dispute, time windows, obligation, fences** — not “BR OS.” Closest academic match to “law as logic.” |

### B. Digital Mishnah (text engineering, not rules engine)

| | |
|--|--|
| **Who** | Hayim Lapin et al. |
| **What** | Born-digital critical edition; witnesses, variants, analysis tools |
| **Home** | digitalmishnah.org |
| **Take for us** | Text infrastructure; we already have Sefaria-style JSON dumps — don’t reinvent critical edition |

### C. Data / AI study tools (access + graph, not din compiler)

| | |
|--|--|
| **Ezra Brand / ChavrutAI** | Talmud+tech: entity counts, densest aggadah, Sefaria API tooling, AI study partner prototypes |
| **Sefaria ecosystem** | API + community readers (e.g. talmud.page) |
| **Take for us** | Indexing, search, bipartite cite graphs — we already do similar for BR/MH |

### D. “Computational Gemara” (individual / educational)

| | |
|--|--|
| **What** | Programmers formalizing Gemara *argument flow* (set notation, educational software dreams) |
| **Example** | Mi Yodeya threads on formal logic + Gemara |
| **Take for us** | Flowchart the *machloket* (dispute), not claim the Amoraim used set theory |

### E. Novelty / adjacent (use carefully)

| | |
|--|--|
| **Codesh** | Esoteric language whose *syntax* is modeled on biblical Hebrew; “Talmud” = library name — **not** a Mishnah rules engine |
| **Bar-Ilan Responsa Project** (classic) | Full-text search for poskim — retrieval, not formal verification |
| **Torah-* family in our reviews/** | Prior experiments (v6–v8, PureV9…) — kill-lists already in STANDING_DECISIONS |

---

## 3. What to steal vs refuse

| Steal | Refuse |
|-------|--------|
| Deontic framing: obligated / exempt / forbidden / permitted | Silent merge of midrash into Written |
| Temporal windows (Berakhot 1 is textbook) | “Talmud is a programming language” as ontology |
| Fence = soft deadline vs hard deadline | Import foreign compiled DBs as truth |
| Explicit dispute parties (Eliezer / Sages / Gamliel) | One merged “correct” opinion without labeling |
| Scenario tests (“sons came from feast…”) | ELS / gematria-as-structure |
| Gabbay-style *named* inference patterns as dual-track notes | Re-run PureV9 Nehemiah-as-OS |

---

## 4. Do external projects compile **Written Torah** using Mishnah/Talmud?

**Short answer: No serious peer project does what that question literally asks.**

| Direction people actually take | Examples | Is it “compile Written *using* Oral”? |
|--------------------------------|----------|----------------------------------------|
| Formalize **Talmudic reasoning** (how disputes, time, obligation work) | Talmudic Logic Project (Gabbay / Abraham / Schild) | **No** — models Oral logic itself |
| Digital critical **Mishnah text** | Digital Mishnah | **No** — edition / variants |
| Search / NLP / study tools | Sefaria API, ChavrutAI, Responsa Project | **No** — retrieve and assist reading |
| Esoteric “Bible-syntax” languages | Codesh | **No** — novelty; not a Written←Oral compiler |
| Traditional human “compile” of law | Mishnah, Talmud, Rambam’s *Mishneh Torah* | Human legal codification; **not** a software pipeline that regenerates Chumash from Oral |

**What almost everyone does instead:**

```text
Written Torah  →  (human / midrash / halakhah)  →  practice rules, disputes, codes
     ↑________________ rarely reverse as software _________________│
```

- **Oral expands / decides practice around Written** (classic religious and academic picture).  
- Software peers formalize **that Oral layer** (deontic/temporal logic, search, graphs).  
- Nobody reputable claims: “feed Mishnah + Talmud into a compiler → emit Genesis–Deuteronomy.”

**Closest human analogue (not software):** Rambam and other codifiers **compile applied law** from Talmudic tradition into orderly codes. That is **halakhah out**, not **regenerating the Written text**.

**Implication for Torah_Grok (aligned with standing policy):**

- **Derive Written logic from Hebrew Written** (Pre-Code).  
- Attach Mishnah/Talmud as **named dual-track Oral**, never silent-merge into Written.  
- Do **not** expect peer projects to hand us a “Oral → Written” compiler; that path is not what the field builds — and our standing rules already reject silent Oral→Written rewrite.

---

## 5. Fit to Torah_Grok

```text
Written Pre-Code (Lev/Exod law)  ← primary “compile & run” target (from Hebrew Written)
        ↑ dual-track only
Mishnah chapter summaries        ← practice-shaped Oral (Berakhot, later Zevachim/Niddah…)
        ↑ optional formal notes
Talmudic Logic peer patterns     ← deontic/temporal/conflict vocabulary
        ≠
BR chapter summaries             ← Genesis meaning / ops literacy (not law VM)
```

**Language:** Hebrew first + transliteration + English explanation (never bare Hebrew; never English-only as derivation source).

---

## 6. Next experiments (if we learn by doing)

1. Encode Berakhot 1 as a tiny **scenario table** (time → in_window?) using Gabbay-style temporal/deontic labels — still dual-track, not psak.  
2. One-page **glossary** with he + translit + en: obligated / exempt / fence / majority / Beit Hillel.  
3. When touching Lev purity units, open **Niddah** or **Negaim** Mishnah chapters the same way as Berakhot 1.
