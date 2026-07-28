# Derivation method — Leviticus 12 / legal-phrase track

**Scope:** This document describes the method used for the **Lev 12** experiment and similar **legal-phrase** modeling. It is **not** a global rule for all of Torah_Grok.

Repo-wide rules (open-minded, multi-method) live in root `AGENTS.md`. Other approaches (shape scanners, keyword dictionaries, FSMs, comparative corpora, discovery notes from `~/code/Torah`, etc.) are welcome elsewhere in the project.

---

## Goal (this track)

Build **traceable** models of a legal unit so each field can answer: *where did this decision come from?*

```
Ta'amim-style tree  →  Torah rule  →  Mishnah ops  →  Talmud reason
     (syntax)            (data)         (procedures)     (why / midrash)
```

---

## Pipeline (for legal units using this track)

### 1. Choose a unit

Prefer a self-contained **legal/procedural** block (chapter or clear sub-unit).

- Good fit: purity, sacrifices, festivals, clear if→then case law (e.g. **Lev 12**).
- Harder fit: pure narrative, poetry, free midrash chains (different model types later).

### 2. Parse structure (ta'amim layer)

- Treat cantillation (**ta'amim**) as a syntactic parse layer: disjunctives divide; conjunctives link.
- Build a hierarchical tree: header / condition / consequence / reference / implication / ritual close.
- Prefer real Masoretic accent data when available; until then, document that ranks follow standard prose hierarchy patterns (LREC-style methodology), not free paraphrase.

### 3. Extract Written logic only from phrases

| Tree role | Maps to code | Example (Lev 12:2) |
|-----------|--------------|--------------------|
| Header / setup | Context only — not `if` | “Speak to Israel saying” |
| Condition pivot | `IF …` | birth + male (*zachar*) |
| Consequence | variables / THEN | 7 days impurity |
| Reference | link to known rule | “like niddah” |
| Implication | status / outcome | impure |

**Rule:** If it is not a ta'amim-delimited **content** phrase (or an explicit Oral cite), do not invent a variable. Glue words stay syntax.

### 4. Scale across the unit

Check:

- Same pattern for parallel cases (e.g. male vs female)?
- Verse splits align with logical boundaries?
- Variables self-evident from delimited phrases?

### 5. Attach Oral layers only with names

| Layer | Role | Example |
|-------|------|---------|
| Mishnah | Boot / operational procedures | Niddah counting, 3:7 edge cases |
| Talmud | Inference / “why” / expansion | Niddah 31a doubled-period reason |

Do not encode Oral content without **tractate + location** (and prefer local `Data/` or a standard edition).

### 6. Implement layers as separate functions/objects

Reference shape (`artifacts/lev12_torah_model.py`):

1. Tree / `make_tree` — structure + phrase-derived fields  
2. `torah_rule` — Written if→then only  
3. `mishnah_apply` — named operational tags  
4. `talmud_derive` — named reason only  
5. Scenarios JSON — test cases from text (+ named edges)

### 7. Test and document provenance

- Scenarios must state expected values from Written (or named Oral) sources.
- Every model file should include a `justification` / `provenance` note.
- If you cannot cite it, **do not code it**.

---

## Reference case: Leviticus 12

### Why this unit

Eight verses; gender-parallel timers; shared closing ritual; rich Oral expansion (Mishnah/Talmud Niddah).

### Phrase → logic (v2)

| Phrase (sense) | Code | Source class |
|----------------|------|--------------|
| Speak to Israel saying | (not in `if`) | Ta'amim header |
| Woman conceives and bears male | `birth_event`, `child_gender == male` | Written + condition pivot |
| Impure seven days | `impurity_days = 7` | Written |
| Like niddah | `reference = niddah` | Written |
| She shall be impure | `status = impure` | Written |

### Full chapter variables

| Variable | Male | Female | Written source |
|----------|------|--------|----------------|
| impurity_days | 7 | 14 | 12:2 / 12:5 |
| purification_days | 33 | 66 | 12:4 / 12:5 |
| circumcision day 8 | yes | — | 12:3 |
| restrictions | holy things / sanctuary | same | 12:4 |
| offerings / poor option | lamb+bird / two birds | same | 12:6–8 |
| outcome | pure after atonement | same | 12:7–8 |

### Oral attachments (named only)

| Code / note | Source |
|-------------|--------|
| Counting / examination style | Mishnah Niddah 1:1–3 area |
| Miscarriage day 40 vs 41 | Mishnah Niddah 3:7 |
| Why doubled periods | Talmud Niddah 31a |

### Artifacts for this case

| File | Role |
|------|------|
| `lev12_2_model.json` | Verse-level model |
| `leviticus_12_full_model.json` | Chapter model |
| `leviticus_12_2_word_by_word.md` | Phrase map |
| `leviticus_12_analysis_process.md` | Process log |
| `lev12_mishnah_mapping.md` | Torah ↔ Mishnah |
| `oral_excerpts_niddah.md` | Named Oral snippets |
| `lev12_torah_model.py` | Runnable layered representation |
| `torah_test_scenarios.json` | Test harness |

Run:

```bash
python3 artifacts/lev12_torah_model.py
```

---

## Decision log template (copy for new units)

For each field you add to JSON/Python, fill one row:

| Code element | Decision | Justification (A/B/C) | Citation |
|--------------|----------|------------------------|----------|
| e.g. `impurity_days` | 7 if male | B Written | Lev 12:2 |
| e.g. `talmud_reason` | remorse text | C Oral | Niddah 31a |

Justification classes:

- **A** — ta'amim phrase structure  
- **B** — explicit Written Torah wording  
- **C** — named Oral source  

---

## Scaling to more of the Torah

### Use this method for

- Legal-procedural prose units across the Pentateuch and purety/sacrifice law  
- Parallel constructions (shared tree, swapped variables)  
- Units with clear Mishnah operationalization  

### Do not naively force

- Narrative alone (needs event/plot models, not only if→then)  
- Poetry / different cantillation systems without a separate grammar  
- Unbounded midrash or “AI invents gezerah shavah” without encoding midot + limits  
- Claims of complete practical poskim-level output  

### Industrialized path (later)

1. Ingest Masoretic text with real ta'amim → trees  
2. Segment legal units  
3. Extract variables with provenance  
4. Link Oral sources by stable refs  
5. Emit JSON + tests  
6. Human review gate  

---

## Conventions for *this* track (not whole-repo law)

1. Prefer fields that map to A/B/C (ta'amim / Written / named Oral) so Lev-style work stays auditable.  
2. Label anything speculative as hypothesis.  
3. **Do not modify `Data/`** unless the user explicitly asks (repo-wide).  
4. Prefer root or `artifacts/` scripts; ask before bulk refactors (repo-wide).

When extending **this** legal-phrase track: open this file, fill a decision-log row, then write code.  
When exploring other methods: follow `AGENTS.md` and keep confidence labels.
