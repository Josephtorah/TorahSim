# Recovered artifacts from Grok web thread

These files recreate work from a Grok **web** conversation that could not be downloaded from the web UI. They were reconstructed from the full chat transcript (pasted into Grok terminal) plus local `Data/` extracts where appropriate.

## Rules (from project `AGENTS.md`)

- `Data/` is **source data** — not modified unless explicitly asked.
- Models and scripts live under `artifacts/` and repo-root Python as needed.
- Open mind: multiple methods allowed; Lev 12 used a stricter track (see `DERIVATION_METHOD.md`).

## File index

| File | Description |
|------|-------------|
| `DERIVATION_METHOD.md` | **Full modeling procedure + Lev 12 decision log** (see also root `AGENTS.md`) |
| `THREAD_SUMMARY.md` | Full readable summary of the web thread |
| `hebrew_bible_architecture_summary.md` | Cantillation / Tanakh architecture notes |
| `starting_point_summary.md` | Investigation methodology + Lev 12 start |
| `leviticus_12_analysis_process.md` | Full process: trees, variables, Oral layer |
| `leviticus_12_2_word_by_word.md` | Word/phrase → logic mapping for Lev 12:2 |
| `lev12_2_model.json` | Justified JSON model for Lev 12:2 |
| `leviticus_12_full_model.json` | Full-chapter JSON model (Lev 12:1–8) |
| `lev12_mishnah_mapping.md` | Torah → Mishnah Niddah mapping |
| `lev12_torah_model.py` | Layered Python representation (Ta'amim → Torah → Mishnah → Talmud) |
| `torah_test_scenarios.json` | Small scenario dataset for the Python model |
| `berakhot_ch2_model.json` | JSON model for Mishnah Berakhot ch. 2 |
| `oral_excerpts_niddah.md` | Niddah 31a + Mishnah 3:7 excerpts (web recovery) |
| `mishnah_niddah_ch1.md` … `ch3.md` | Hebrew extract of Mishnah Niddah 1–3 from `Data/` |
| `mishnah_berakhot_ch1.md`, `ch2.md` | Hebrew extract of Berakhot 1–2 from `Data/` |

**Recovery status:** **COMPLETE for text.** Web sandbox only ever retained 3 docs + 2 images (see `RECOVERY_STATUS.md`). Local `artifacts/` is the canonical store and is fuller than web. Optional: recover 2 JPEGs via base64 if needed.

## How to run the small model

```bash
cd <old-home>/code/Torah_Grok
python3 artifacts/lev12_torah_model.py
```

## Lev 12 track note

The recovered Lev 12 models used a tight provenance style (ta'amim / Written / named Oral). That is **scoped to that experiment**, not a rule for every future exploration. See root `AGENTS.md`.
