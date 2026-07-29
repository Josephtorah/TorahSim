# Pre-code logic methods (2026-07-28)

**Folder:** `logic/pre_logic_methods_2026-07-28/`
**Kind:** display formats → roles → pre-code logic track (moved here from `logic/Parse_tree_2026-07-27/` on 2026-07-28) · experiments + tutorials · **not** binding law
**Rule set:** ta'amim `v3` · morphology = OSHB `@lemma/@morph` (#IMPOSED labeled aid)

---

## Start here

| Doc | Role |
|------|------|
| **[TUTORIAL_precode_logic_methods_BEGINNERS_2026-07-28.md](TUTORIAL_precode_logic_methods_BEGINNERS_2026-07-28.md)** | **Beginner lesson** on all methods used here: predicate logic, speech acts, deontic LET, Hoare triples, event roles/et, temporal COMMIT, invariants, casuistic IF/THEN, registry naming, dry-run machine |
| **[TUTORIAL_precode_logic_methods_AUDIO_2026-07-28.md](TUTORIAL_precode_logic_methods_AUDIO_2026-07-28.md)** | **Audio narration** of the same lesson — flowing prose, no tables/symbols; drop into an audio reader |
| **[WALKTHROUGH_week_findings_beginner_2026-07-28.md](WALKTHROUGH_week_findings_beginner_2026-07-28.md)** | **Beginner walkthrough of the week findings** — the 7 discoveries in plain language (checklist metaphor); audio-friendly |
| **[PROPOSAL_TIR_026_033_form_operators_2026-07-28.md](PROPOSAL_TIR_026_033_form_operators_2026-07-28.md)** | **Stage B: PROPOSED TIR-026…033** — verb-form → logic-operator rules (LET/CMD!/LET?/THEN/PURPOSE/ONGOING/agentless/CMD-US) · whole-Torah counts + cross-book examples · **APPROVED 2026-07-28**, merged into `../TREE_INTERPRETATION_RULES.md`; kept as evidence record |
| **[PLAN_fullstack_architecture_2026-07-28.md](PLAN_fullstack_architecture_2026-07-28.md)** | **Engineering plan:** source-of-truth = YAML (Pre-Code rule) · SQLite as derived index · schema v1 · build order 1–5 · git/GitHub workflow (private `Josephtorah/Torah_Grok`) · **roadmap §8 status:** A ✅ · B ✅ · C ▶ pilot (`../units/gen_01_creation_boot.yaml` frozen) · D ▶ pilot green (`run_unit.py`, repo root) |
| **[PROMPT_continue_stage_D_2026-07-28.md](PROMPT_continue_stage_D_2026-07-28.md)** | Resume prompt for a fresh session: read-first list · stage state · Stage D task spec + exit criteria · standing rules |
| **[EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md](EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md)** | **Applied — FULL WEEK:** all 34 verses (Gen 1:1–2:3) in these logics · 9-cycle pattern matrix · naming ledger · named-Oral verified for both collisions + day-2 missing test, day-3b delta, na'aseh, oto/otam, tov me'od, taninim, Shabbat blessing · hypothesis |
| **[GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html](GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html)** | **Full-week data run** (HTML): 34 verses · 237 bricks · FLAT parens + LEAF LEDGER + morpheme MORPH + auto roles incl. day-7 ops (SANCTIFY, COMPLETE, CEASE/REST, CMD-US, INTENSIFIER) |
| **[GEN_1_1_20_flat_ledger_morph_2026-07-27.html](GEN_1_1_20_flat_ledger_morph_2026-07-27.html)** | Earlier Gen 1:1–20 run (superseded by the full-week file above) |
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
