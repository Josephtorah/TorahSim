# Pre-code logic methods (2026-07-28)

**Folder:** `logic/pre_logic_methods_2026-07-28/`
**Kind:** display formats → roles → pre-code logic track (moved here from `logic/Parse_tree_2026-07-27/` on 2026-07-28) · experiments + tutorials · **not** binding law
**Rule set:** ta'amim `v3` · morphology = OSHB `@lemma/@morph` (#IMPOSED labeled aid)

---

## Start here

| Doc | Role |
|------|------|
| **[grok-grok-audio_2026-07-28.epub](grok-grok-audio_2026-07-28.epub)** | **EPUB for ElevenReader** — full-build long narration (parser · morph · Masoretes · Pre-Code · verse examples) · **restored name after overwrite** |
| **[grok-grok-audio_2026-07-28.md](grok-grok-audio_2026-07-28.md)** | **Source markdown** for that EPUB — lengthy chaptered audio script (canonical restore of the full build) |
| **[claude-audio_2026-07-28.epub](claude-audio_2026-07-28.epub)** | **Claude's EPUB for ElevenReader** — full-build long narration, 11 chapters ≈9,700 words (Masoretes · parser · morphology · pre-code logics · day-one derivation · week deviations · build chronicle); rebuilt 2026-07-28 from the source below |
| **[TUTORIAL_grok_audio_full_build_2026-07-28.md](TUTORIAL_grok_audio_full_build_2026-07-28.md)** | Source markdown for **claude-audio** (verified intact 2026-07-28: 9,726 words, 11 chapters — distinct from the shorter grok-grok text above); original `grok-audio_*.epub` build now lives as owner-renamed `Claude-grok-audio_2026-07-28.epub` |
| **[METHOD_language_logic_derivation_2026-07-30.md](METHOD_language_logic_derivation_2026-07-30.md)** | **★ THE METHOD CHARTER (living document):** the 2 language-research layers (ta'amim · morphology) + 6 logic formalisms (Hoare · deontic · event · temporal · speech-act · casuistic) + the register machine · the 8-step derivation pipeline · 4 complex worked examples w/ DB-verified codes (Lev 1:3–4 · Gen 1:14–15 · Gen 1:26+28 · Deut 6:4–5) · §6 = how to revise the process |
| **[derivation-narrative_2026-07-30/](derivation-narrative_2026-07-30/)** | **Derivation narratives** (one per unit, standing process): each file = full-stack-developer telling + beginners telling of the same derivation; additions only on owner ask-first. So far: `NARRATIVE_gen_01_creation_boot` (day 1, baseline) · `NARRATIVE_gen_02_raqia_day` (day 2, flagged commit) · `NARRATIVE_gen_03_double_build` (day 3, delegation + spec delta) |
| **[TUTORIAL_precode_logic_methods_BEGINNERS_2026-07-28.md](TUTORIAL_precode_logic_methods_BEGINNERS_2026-07-28.md)** | **Beginner lesson** on all methods used here: predicate logic, speech acts, deontic LET, Hoare triples, event roles/et, temporal COMMIT, invariants, casuistic IF/THEN, registry naming, dry-run machine |
| **[TUTORIAL_precode_logic_methods_AUDIO_2026-07-28.md](TUTORIAL_precode_logic_methods_AUDIO_2026-07-28.md)** | **Shorter audio narration** of the eight classical methods only — flowing prose; drop into an audio reader |
| **[WALKTHROUGH_week_findings_beginner_2026-07-28.md](WALKTHROUGH_week_findings_beginner_2026-07-28.md)** | **Beginner walkthrough of the week findings** — the 7 discoveries in plain language (checklist metaphor); audio-friendly |
| **[PROPOSAL_TIR_026_033_form_operators_2026-07-28.md](PROPOSAL_TIR_026_033_form_operators_2026-07-28.md)** | **Stage B: PROPOSED TIR-026…033** — verb-form → logic-operator rules (LET/CMD!/LET?/THEN/PURPOSE/ONGOING/agentless/CMD-US) · whole-Torah counts + cross-book examples · **APPROVED 2026-07-28**, merged into `../TREE_INTERPRETATION_RULES.md`; kept as evidence record |
| **[PLAN_fullstack_architecture_2026-07-28.md](PLAN_fullstack_architecture_2026-07-28.md)** | **Engineering plan:** source-of-truth = YAML (Pre-Code rule) · SQLite as derived index · schema v1 · build order 1–5 · git/GitHub workflow (private `Josephtorah/Torah_Grok`) · **roadmap §8 status:** A ✅ · B ✅ · C ▶ pilot (`../units/gen_01_creation_boot.yaml` frozen) · D ▶ pilot green (`run_unit.py`, repo root) |
| **[PROMPT_continue_stage_D_2026-07-28.md](PROMPT_continue_stage_D_2026-07-28.md)** | Resume prompt for a fresh session: read-first list · stage state · Stage D task spec + exit criteria · standing rules |
| **[DB_INSPECTION_torah_grok_2026-07-28.html](DB_INSPECTION_torah_grok_2026-07-28.html)** | **DB inspection report** (open in browser): every table + live counts · sample rows per layer · genre fingerprint reproduced by query · all 20 oral_refs · FTS demos · Stage D run embedded (computed, not stored) |
| `report_db_html.py` | Generator for the DB report — every row queried live: `python3 logic/pre_logic_methods_2026-07-28/report_db_html.py` |
| **[DB_FLAT_LEDGER_MORPH_Gen_1_1to31_2_1to3_2026-07-28.html](DB_FLAT_LEDGER_MORPH_Gen_1_1to31_2_1to3_2026-07-28.html)** | **DB-backed flat-ledger report** — same FLAT · LEDGER · MORPH format, every row from SQLite (PLAN §4 upgrade); verified row-identical to the XML-parse original except the H3318 lexicon-v1 drift (DB side is current) |
| **[DB_FLAT_LEDGER_MORPH_Deut_6_4to5_2026-07-28.html](DB_FLAT_LEDGER_MORPH_Deut_6_4to5_2026-07-28.html)** | Proof of whole-Torah reach: the Shema (Deut 6:4–5) in the same format, one command, no re-parse |
| `render_flat_ledger_from_db.py` | DB-backed generator (any book/range): `python3 logic/pre_logic_methods_2026-07-28/render_flat_ledger_from_db.py Lev "1:1-9" out.html` — reuses CSS/VERSE_EN/decode_morph from the original renderer |
| **[UNIT_gen_01_creation_boot_2026-07-30.html](UNIT_gen_01_creation_boot_2026-07-30.html)** | **The frozen logic unit rendered** (open in browser): derivation log A–J · 14 owner-approved operator lines w/ TIR cites + Hebrew anchors · state machine · scenarios S1–S7 · Oral notes tiered · trees · 52-word coverage · live `run_unit.py` verification embedded |
| `render_unit_html.py` | Generator: any unit YAML → HTML (`python3 logic/pre_logic_methods_2026-07-28/render_unit_html.py <unit_id>`); works for day-2+ units as they freeze |
| **[EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md](EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md)** | **Applied — FULL WEEK:** all 34 verses (Gen 1:1–2:3) in these logics · 9-cycle pattern matrix · naming ledger · named-Oral verified for both collisions + day-2 missing test, day-3b delta, na'aseh, oto/otam, tov me'od, taninim, Shabbat blessing · hypothesis |
| **[GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html](GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html)** | **Full-week data run** (HTML): 34 verses · 237 bricks · FLAT parens + LEAF LEDGER + morpheme MORPH + auto roles incl. day-7 ops (SANCTIFY, COMPLETE, CEASE/REST, CMD-US, INTENSIFIER) |
| **[GEN_1_1_20_flat_ledger_morph_2026-07-27.html](GEN_1_1_20_flat_ledger_morph_2026-07-27.html)** | Earlier Gen 1:1–20 run (superseded by the full-week file above) |
| **[MOCKUP_webapp_scroll_2026-07-29.html](MOCKUP_webapp_scroll_2026-07-29.html)** | **Web-app mockup** (open in browser): public scroll site — sticky nav + jump picker, FLAT always visible, collapsible LEDGER/MORPH/CODE, ❄ frozen badges, infinite-scroll sentinel, provenance/attribution/disclaimer footer; real DB rows for Gen 1:1–5 |
| **[MOCKUP_flat_ledger_oshb_morph_2026-07-27.md](MOCKUP_flat_ledger_oshb_morph_2026-07-27.md)** | Format spec (owner-preferred candidate v2): FLAT + LEDGER + morpheme MORPH rows |
| **[MOCKUP_tree_display_flat_layers_ledger_2026-07-27.md](MOCKUP_tree_display_flat_layers_ledger_2026-07-27.md)** | Earlier composite mockup: FLAT → LAYERS (L\|R cuts) → LEDGER · Gen 1:3 + Lev 1:2 |
| `render_flat_ledger_morph_html.py` | Generator for the HTML runs: `python3 logic/pre_logic_methods_2026-07-28/render_flat_ledger_morph_html.py Gen 1 1 20 out.html` |

## Method chain (how the pieces connect)

1. **Trees:** ta'amim v3 leaves (conjunctive glue → disjunctive splits) — `taamim_tree_parse.py`
2. **Morph:** OSHB per-morpheme grammar (prefix letters + suffixes as own rows)
3. **Roles:** verb-form frames (CMD jussive · CMD? imperfect · THEN weqatal · PURPOSE ל+infinitive · ONGOING participle) + lemma rules + particle logic (et→OBJECT, bein→BETWEEN, asher→REL)
4. **Logic:** roles → well-known pre-code formalisms (deontic, Hoare, event semantics, temporal, casuistic) — see EXPERIMENT + tutorials

## Display lock note

Chat tree display remains governed by **`logic/TREE_DISPLAY.md`** (PERMANENT top-down B# GLUE|ATOM). The FLAT/LEDGER/MORPH format here is a **candidate report format**, adopted for these runs at owner request; it has not replaced the chat lock.

**Related:** `../Parse_tree_2026-07-27/` (parser verification + poetry checkpoint, incl. `REPORT_simple_leaf_en_he_oshb_morph_2026-07-27.md`, `GLUE_BRICKS_v2_MANDATORY_2026-07-27.md`) · `../TREE_INTERPRETATION_RULES.md` (TIR) · `../SYSTEM.md` (unit pipeline)

**Last updated:** 2026-07-28
