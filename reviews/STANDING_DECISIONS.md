# Standing decisions (agent-owned)

Owner may not track cross-project questions. **Agents decide and update this file** when new evidence arrives. Do not re-ask the owner for these unless a decision would delete work or rewrite `Data/`.

Last updated: 2026-08-06 (§1a Claude guides every derivation — permanent; supersedes solo auto-freeze)

---

## 1a. Derivation process — Claude guides and checks every derivation (PERMANENT · 2026-08-06)

| Decision | **"Claude guides and checks every derivation."** Binding on the chair (Grok and any deriving agent), permanent — not a remediation-era measure. |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **(1) Care-points first** | No span is derived until Claude's **pre-derivation care-points** arrive through the owner. Do not open a new piece or unit span without them. |
| **(2) Pieces + STOP** | All derivation proceeds in **4–5-verse pieces**. Each piece **STOP**s for Claude's external verification before the next piece is authorized. |
| **(3) Freeze gate** | **No unit freezes** without Claude's **whole-unit review**. A green preflight / green scenarios alone **never** freezes anything, ever again. |
| Supersedes | Solo **auto-freeze** provisions in older continue-prompts / charters (e.g. green → freeze without external review). Those are **void**. |
| Unchanged (owner-only) | Commit / push · next-block authorization · amendments · triage — still owner gates. |
| Scope | Every Written-logic unit derivation from now on (amendment wave and post-wave corpus build). |
| Current posture | Match the protocol already in use on gen_41 amend: care-points → piece → STOP → verify → next piece → whole-unit review → freeze ritual only after Claude green → owner commit. |

---

## 0. Dated filenames (reports, research, indexes)

| Decision | **Date goes in the filename. When a dated file is updated, rename it so the date is the current update day.** |
|----------|---------------------------------------------------------------------------------------------------------------|
| Format | `REPORT_<topic>_YYYY-MM-DD.md`, `RESEARCH_…`, `NOTES_…`, or topic names with suffix `_YYYY-MM-DD` (e.g. `DISCOVERIES_2026-07-19.md`, `cite_index_2026-07-18.json`). |
| New file | Use **today’s calendar date** (day the file is written/saved). |
| **Update** | On **substantive** edit of a dated file: **rename** so the suffix becomes **today’s date**, then update all in-repo links to the new name. Do not leave a stale date on a freshly edited file. |
| Prefer | One current file per topic (rename in place) rather than forever keeping every old date, unless the owner asks to archive a snapshot. |
| Why | Filenames show what is current; “Last updated” inside the body alone is easy to miss. |
| **Hub exceptions (stable names)** | `README.md`, `Agents.md` / `AGENTS.md`, `reviews/STANDING_DECISIONS.md` — keep stable names so links and habits work; always set **Last updated: YYYY-MM-DD** in the body when changed. |
| Scope | Project research under `reviews/<topic>/`, reports, research packs, and built index artifacts we own. Not `Data/` source dumps. |
| Example | `reviews/talmud_structure/REPORT_lev_1_2_oral_coding_2026-07-19.md`. If edited next on 2026-07-20 → rename to `…_2026-07-20.md` and fix links. |

### 0a. Research placement — **topic subfolders only**

| Decision | **Never store research in the repo top folder (project root). Always create / use a topic subfolder.** |
|----------|--------------------------------------------------------------------------------------------------------|
| **Forbidden** | Putting research reports, scans, notes, caches, or exploration dumps in repo root (`Torah_Grok/*.md`, loose `SCAN_*`, `RESEARCH_*`, etc.). |
| **Required** | Research goes under a **topic directory**, usually `reviews/<topic>/` (e.g. `reviews/br_link_studies/`, `reviews/sanctuary_spine_v1/`, `reviews/talmud_structure/`, `reviews/br_genesis_packets/`). |
| New topic | If none fits: **create** `reviews/<short_topic_name>/` with an `INDEX.md` (or README) and put dated files there. |
| Logic units | Pre-Code YAML stays under `logic/units/` (derivation packages, not free-floating research essays). |
| Scripts | Prefer `artifacts/` or topic folder for one-off analysis scripts; long-lived interpreters at repo root only when they serve the whole project (`taamim_tree_parse.py`). |
| Why | Root stays navigable; topics accumulate without cross-contamination; agents can find “everything on X” in one place. |
| Legacy | Older flat files under `reviews/*.md` may remain until touched; **on substantive update**, prefer moving into a topic subfolder and fixing links. Do not add new flat research at `reviews/` root either when a topic folder is appropriate. |
| Architecture discussions | Hub **`reviews/architecture/`** (`INDEX.md` + passes + post-Torah scan). Not the same as `artifacts/hebrew_bible_architecture_summary.md` (older web-thread notes). |
| Genesis Build | **Full Gen 1–50 draft + tree_derived_v1** (26 `gen_*`; 1533 STEPs). See `GENESIS_TREE_DERIVE_2026-07-24.md` · `reprocess_book_from_trees.py --book gen`. |
| Exodus Build | `EXODUS_BUILD_2026-07-24.md` — **full draft + tree_derived_v1** (45 `exo_*` units, **1213** STEPs = 1213 trees). Reprocess: `EXODUS_TREE_DERIVE_2026-07-24.md` · `artifacts/reprocess_exodus_from_trees.py`. Prior bulk map: `EXODUS_BUILD_2026-07-21.md`. |
| **Leviticus Build** | `LEVITICUS_BUILD_2026-07-21.md` + **tree_derived_v1** (`LEVITICUS_TREE_DERIVE_2026-07-24.md`; 50 units, STEP_Lv per verse). Tool: `artifacts/reprocess_book_from_trees.py --book lev`. |
| **Numbers Build** | `NUMBERS_BUILD_2026-07-24.md` + **tree_derived_v1** (`NUMBERS_TREE_DERIVE_2026-07-24.md`; 47 units, STEP_Nm per verse). Tool: `artifacts/reprocess_book_from_trees.py --book num`. |
| **Deuteronomy Build** | `DEUTERONOMY_BUILD_2026-07-24.md` + **tree_derived_v1** (`DEUTERONOMY_TREE_DERIVE_2026-07-24.md`; **41** `deu_*` units, **959** STEP_Dt). Tool: `artifacts/reprocess_book_from_trees.py --book deu` (10 phases A–J). |
| Genesis package map | `reviews/architecture/ARCHITECTURE_genesis_stack_2026-07-21.md` — full-stack segment map (boot → Egypt handoff). |
| Sefer Yetzirah | **Not** a source for Written boot steps. Comparative dual-track only if pursued later. Family caution: Genesis-Experiment “do not pursue SY as ontology.” See stack doc §6. |
| **Narrative / BR research path** | `RESEARCH_narrative_model_br_ops_2026-07-21.md`. **Five rules:** (1) do not demand BR system diagram; (2) catalog BR **operations** on verses; (3) narrative units = first-class precision (state/agents/memory); (4) “narrative as generative model” = labeled **hypothesis** only; (5) SY/BR dual-track never write Written boot. First pass: Gen 1:1–5 Written cold + BR ch.1 ops map. |
| **God’s Intention frame** | `architecture/Gods_Intention_2026-07-21.md` — progressive-revelation / buried information-system thought experiment (not binding law). BR opening as plan+gates+chains; **small token → whole registry** rhymes with SY but is not identical (*et* expansion ≠ letter ontology). |
| **Bereshit Rabbah Plan for Genesis** | `Bereshit_Rabbah_Plan_for_Genesis_2026-07-21.md` — method: Written first; BR as **gates + models + ops + transmission**; pipeline for modern instrumentation; SY comparative only. |
| **BR Genesis Interface** | `BR_Genesis_Interface_2026-07-23.md` + `reviews/br_genesis_packets/` — **sequential** BR. **Ch.1–2 complete**. **Ch.3 started:** 3:1. Next: **BR 3:2**. Hebrew + translit + English. Name-scan: `reviews/br_name_scans/`. |

---

## 1. Active project

| Decision | **Torah_Grok is the only active workspace.** |
|----------|-----------------------------------------------|
| Rationale | Pre-Code Logic + versioned ta'amim parser live here. Family repos are reference only. |
| Other repos | English reviews under `reviews/*` only. Do not re-run foreign pipelines. Do not write into foreign Torah* repos unless owner explicitly says so. |
| Family map (inactive) | Torah → MVP → 2nd-MVP → v3 → v4 → v5 → v6 → v7 → v7.5 → v8 → **PureV9** → …; side: Genesis-Experiment; also Cantillation-Paradox. |
| v8 status | Best-documented family rebuild; not our active codebase. `reviews/Torah-v8/`. |
| Genesis-Experiment | Word-level typing lessons. `reviews/Genesis-Experiment/`. |
| PureV9 | Nehemiah experiments: typing ≠ imperative code; pivot to Lev 13–14. `reviews/PureV9/`. |
| Cantillation-Paradox | Talmud-as-compiler pivot + Chagigah wiring. `reviews/Cantillation-Paradox/`. Do not merge. |

## 2. How we treat past Torah-* projects

| Decision | **English L0 reviews + PURSUE only.** |
|----------|----------------------------------------|
| Rationale | Owner asked to stop heavy audits and code re-runs. |
| Import policy | Methods and kill-lists yes. Compiled DBs, gate stats, OS metaphors, blind data dumps **no**. |
| Source of truth for “what they claimed” | `reviews/<Name>/SCORECARD.md` + `REVIEW-*.md`, not chat memory. |

## 3. כי / *ki* (IF vs BECAUSE)

| Decision | **No global frozen rule.** Per unit, from Hebrew + tree; label confidence. |
|----------|-----------------------------------------------------------------------------|
| Prior art | v6: verse-initial bare כי → BECAUSE, אם/ואם/וכי → IF (parser heuristic). v7: Oral multi-sense — don’t force BECAUSE-only. |
| Practice | In logic units, map the actual word + tree node; if ambiguous, `confidence: hypothesis` and note both readings. Never invent IF rows from English “if.” |

## 4. What to work on next (default track)

| Decision | **Five books full draft + tree_derived_v1 complete; default next = deepen / Oral / interpreter (owner pick).** |
|----------|--------------------------------------------------------------|
| Build docs | Gen · Exod · Lev · Num · **Deut** (`DEUTERONOMY_BUILD_2026-07-24.md`) |
| Continuity | `reviews/PROMPT_continue_numbers_2026-07-24.md` (historical mid-stack) |
| Numbers status | All 47 `num_*` tree_derived_v1 (1289 STEPs). |
| Deuteronomy status | All **41** `deu_*` tree_derived_v1 (**959** STEPs; phases A–J). |
| Prior stack | Gen 26 · Exod 45 · Lev 50 · Num 47 · **Deut 41** — first drafts + tree_derived_v1 done. Do not re-derive unless free-name import forces a check. |
| Genre rule (from PureV9) | Do not force korban IF tables onto pure narrative; absence of control flow in story does **not** falsify legal-tree logic. |
| Override | Owner names a different unit → follow that. |
| Default next | **Deepen track** (hand polish islands; Sifrei/Sifra densification; full TIR) or **interpreter scaffolding** — owner names. Optional: sequential BR packets; Mishnah peer work. |

## 5. Oral (Mishnah / Talmud / midrash)

| Decision | **Named location only; never silent merge into Written.** |
|----------|------------------------------------------------------------|
| **Possible Oral (MH)** | **Do not rule out any Mesorat haShas reference.** Every work/locus that appears on the MH graph is **possible Oral** for this project. Job preference (e.g. Sifra first on Lev) only chooses what to open first — it does not exile other MH members. Single research doc: `RESEARCH_valid_oral_torah_2026-07-19.md` (§6). |
| “Tests” | Scenario tables in logic YAML. Foreign “oracles” are not tests until they cite Hebrew Torah + pass here. |
| Verification style (from v7) | If claiming Oral support: quote Hebrew, cite tractate, keep tier: verified / observation / impl. |
| #IMPOSED (from v7.5) | Any external aid (morphology table, English gloss, OSHB) must be **labeled**, not silent. Lesson they recorded: outside impositions kept being wrong. |
| Roots | Pure text-only roots failed them (~37%). Prefer labeled morphology / tables over pretend purity. |

## 6. Trees / parser

| Decision | **Our versioned ta'amim rules win; OSHB `n=` optional cross-check.** |
|----------|----------------------------------------------------------------------|
| On wrong tree | Notes → golden test → new rule version. No per-verse hacks. |
| **Tree display (ACTIVE)** | **Leaf line `(en · he)` + per-word OSHB morph tables.** Spec + **Lev 1:2** example: **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`**. Index: `logic/TREE_DISPLAY.md`. Also `Agents.md`. **Do not re-quiz.** Name *et* consistently on both object phrases. CLI `--tree` = debug only. Multi-word leaf → one morph row per word. |
| From v8 | Prefer **determinism** + **anti-overfire** (rules local to evidence first). Keep **morph form** (not root-only) in role maps when useful. Do **not** import Nehemiah-compiler or Mishnah 3×5 grid as law. |
| From Genesis-Experiment | **Type at word level**, not leaf level. Leaf = container of typed words. OSHB/Strong’s lemma OK with provenance. **No type-registry inheritance.** **3-verse window** is optional narrative hypothesis — not default for legal units (Lev 12). |

### 6a. Show all work — where trees are recorded (2026-07-20)

| Decision | **Record full ta'amim trees inside each unit under `binary_trees`. Do not leave trees only in chat or only as a re-runnable command.** |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| Full procedure | `logic/SHOW_WORK_TREES_2026-07-20.md` |
| Long beginner/intermediate tutorial | `logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md` |
| Required fields | `rule_set_version`, per-verse `linear` (he+translit+en), `top_binary_split`, **`tree_ascii`** (from `--tree`), `maps_to` logic ids, `pure_binary`, `parser_status` |
| Companion | `tree_coverage` = every leaf role (100% aspiration); not a substitute for `binary_trees` |
| Reference unit | `logic/units/gen_01_day4_lights.yaml` |
| Backlog | `gen_01_day2_raqia`, `gen_01_day3_land_plants` still need full `binary_trees`+`tree_ascii` when next touched |
| Not home for verse trees | `TAAMIM_PARSE_NOTES.md` (parser rules only); free-floating global dumps that detach from the unit |
| **Display when showing a tree** | Same as §6 → **`logic/TREE_DISPLAY_LEAF_EN_HE_MORPH.md`**. Unit `tree_ascii` may still store machine CLI form. |
| **Poetry checkpoint CLOSED** | `logic/Parse_tree_2026-07-27/DONE_poetry_checkpoint_2026-07-27.md`. Smokes Prov/Ps/Job all ok_all. Units: trust_know, way_death, soft_harsh. TIR-023/025 tested; TIR-024 hypothesis. |

### 6b. Particles as set operators (include / limit) — 2026-07-25

| Decision | **Account for את / גם / אך / רק as first-class derivation ops (set include/limit), not silent glue to skip. They are not free-name install symbols.** |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rules** | `logic/TREE_INTERPRETATION_RULES.md` **TIR-014 … TIR-022** |
| **Written scan** | Genesis full book: `reviews/SCAN_gen_particles_et_gam_akh_raq_2026-07-25.md` |
| **Spine glue** | `reviews/sanctuary_spine_v1/SCAN_glue_morph_patterns_2026-07-25.md` |
| **Gold 100% words** | `reviews/sanctuary_spine_v1/GOLD_lev_1_5_full_word_coverage_2026-07-25.md` |
| **BR dual-track** | School pairs: *et*+*gam* = ribui (include); *akh*+*raq* = mi’ut (limit). Named Oral only; never silent-merge. `RESEARCH_BR_particles_2026-07-21.md` |
| **את / *et*** | Default: object marker → patient NP. Multi-*et*: inventory/list. *et kol*: maximize set. Re-*et* under new verb: re-bind object. *et*+divine: special branch (no auto domain-expand). |
| **גם / *gam*** | `set_add` — also include agent/object/time/goods; **וגם את** = also + mark another patient. |
| **אך / רק** | `set_limit` / `set_except` — only/except/sole condition (rare, high signal). |
| **Coverage ethic** | Every word accounted (incl. particles). Morph prefixes (ו-/ה-/מ-…) named when they carry a job. Letters that only spell a content word stay inside that word’s role. |
| **Not** | Particles ≠ `SYM_*` sanctuary free names. Not every *et* = BR Gen 1:1 domain expand. Not letter-opcode codegen. |
| **Sanctuary demo Python** | Teaching dry-run of free names / olah / cloud — **no rewrite required** for particle ops (olah already uses *et* only as implicit syntax). Optional later: annotate `glue_object_marker` on steps. |

### 6c. Verb-form → logic-operator rules (TIR-026–033) — owner-approved 2026-07-28

| Decision | **The eight form→operator mappings are frozen TIR rules, citable in units: jussive→LET (אל+jussive→LET-NOT) · imperative→CMD! · imperfect-in-command→LET? (`?` mandatory, never silently upgraded) · weqatal→THEN · ל+infinitive→PURPOSE · participle→ONGOING/INVARIANT · niphal/pual in directive/outcome→agentless constraint · cohortative→CMD-US.** |
|----------|------|
| **Rules** | `logic/TREE_INTERPRETATION_RULES.md` **TIR-026 … TIR-033** (+ TIR-014 Theme-slot amendment) |
| **Evidence** | `logic/pre_logic_methods_2026-07-28/PROPOSAL_TIR_026_033_form_operators_2026-07-28.md` — whole-Torah counts (genre fingerprint: wayyiqtol Gen 2107 vs Lev 189; weqatal Lev 707/Deut 632) + cross-book examples (Num 6:25 ya'er; Lev 1:4 ve-nirtza; Deut 6:4) |
| **Origin** | Gen 1:1–2:3 pre-code logic experiment (same folder) |
| **Mechanical layer** | `logic/role_rules/` (versioned, goldens) *implements* these as display labels; TIR = the citable interpretation layer. Independent versioning. |
| **Not** | Not a claim that Torah "is" deontic logic; operators are disciplined reading rules with stated limits; not binding religious law. |

## 7. Data

| Decision | **Use `Data/` here. Do not bulk-copy foreign corpora.** |
|----------|----------------------------------------------------------|
| License | Re-source if needed; don’t assume Sefaria dumps are free to republish. |

## 8. Epistemics (always on)

- Separate fact / interpretation / intent.  
- Prefer hypothesis labels over silence.  
- Reject: ELS, gematria-as-structure, temple-as-OS, dove/monitor roles as confirmed, whole-corpus fire/dead stats.  
- Experimental models ≠ binding religious law unless owner asks that framing.

## 9. Questions for the owner

| Ask owner only when | Destructive, irreversible, or product-direction choice they alone can make (delete branches, change religious framing, large refactors of `Data/`). |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Do not ask owner | Which old Torah repo “wins,” כי global policy, default next unit, whether to re-run v6 metrics, OS-metaphor truth, **how to display a ta’amim tree** (`TREE_DISPLAY_LEAF_EN_HE_MORPH.md` — en·he leaves + OSHB morph) — **use this file.** |

---

When a standing decision changes, edit this file and add one line to the bottom changelog.

## Changelog

- 2026-07-28: **§6c form→operator rules** — TIR-026–033 owner-approved + merged; whole-Torah SQLite index (build_db.py, all 5,853 verses unique); versioned logic/lexicon v1 (99.9% gloss coverage) + logic/role_rules v1 (goldens); units + Oral corpus indexed (213 units; 119,903 Oral segments FTS). Repo now on private GitHub Josephtorah/Torah_Grok.
- 2026-07-25: **§6b Particles as set operators** — TIR-014–022 in `TREE_INTERPRETATION_RULES.md`; Gen scan et/gam/akh/raq; gold Lev 1:5 word coverage; sanctuary spine V1 demo complete under `reviews/sanctuary_spine_v1/`. Python demo = teaching dry-run; **no mandatory rewrite** for particle ops.
- 2026-07-24: Deuteronomy **full first draft + tree_derived_v1** complete — 10 phases A–J, **41** units, **959** STEP_Dt; Sifrei Devarim dual-track. Tool: `reprocess_book_from_trees.py --book deu`. **Five books of Torah** now have tree_derived_v1 units.
- 2026-07-24: Genesis **tree_derived_v1** reprocess complete (26 units, 1533 STEPs; phases A–H). Tool: `reprocess_book_from_trees.py --book gen`.
- 2026-07-24: Lev + Num **tree_derived_v1** reprocess complete (phased; same contract as Exod). Tool: `reprocess_book_from_trees.py`.
- 2026-07-24: Exodus **tree_derived_v1** reprocess complete (45 units, 1213 STEPs from top-split arms); see `EXODUS_TREE_DERIVE_2026-07-24.md`.
- 2026-07-24: Numbers track opened and **full first draft complete** — 47-block map, generator, continuity prompt, 1289 trees.
- 2026-07-18: Initial decisions after Torah-v6 Q&A + Torah-v7 highlights intake.
- 2026-07-18: v7.5 arc — family map, #IMPOSED, root-resolution realism; frontier siblings stay unreviewed by default.
- 2026-07-18: v8 intake — engine docs reviewed English-only; take determinism/anti-overfire/form; leave Nehemiah/grid/runtime.
- 2026-07-18: Genesis-Experiment — word-level typing, OSHB lemmas, 3-verse window as narrative-only hypothesis.
- 2026-07-18: PureV9 — Nehemiah has typing not control flow; genre rule; Lev 13–14 remains conditional-logic testbed.
- 2026-07-18: Cantillation-Paradox — Talmud compiler pivot; take sliding-window + honesty; leave 100% cycle claims.
- 2026-07-18: Curriculum track — ordered Sifra/Lev learning; first unit Lev 1:1–3; Lev 12 demoted to v0.
- 2026-07-18: Patched 1:1–3 Q1–Q2 from Sifra; added 1:4–9 olah procedure unit; learning-as-we-go.
- 2026-07-20: Genesis Build day-4 unit `gen_01_day4_lights` (1:14–19); renamed approach note to `GENESIS_BUILD_2026-07-20.md`.
- 2026-07-20: §6a show-all-work — trees live in unit `binary_trees` (+ `tree_ascii`); procedure `logic/SHOW_WORK_TREES_2026-07-20.md`; day 4 backfilled.
- 2026-07-20: Genesis day-5 unit `gen_01_day5_sea_birds` (1:20–23; bara, le-mino animals, first blessing).
- 2026-07-20: `architecture/ARCHITECTURE_genesis_stack_2026-07-21.md` — package map + Sefer Yetzirah comparative (dual-track only; not Written source).
- 2026-07-20: day 6 `gen_01_day6_land_human` + day 7 `gen_01_day7_shabbat` — Package 0 kernel boot draft complete (1:1–2:3).
- 2026-07-20: Package 1 garden unit `gen_02_03_garden` (2:4–3:24; formation/breach/exile FSM).
- 2026-07-20: Package 2 `gen_04_05_early_humanity` (4–5; Cain/Abel + culture + Adam→Noah table).
- 2026-07-20: Package 3 `gen_06_09_flood_covenant` (6–9; flood disaster recovery + rainbow covenant).
- 2026-07-20: Package 4 `gen_10_11_nations_babel` (10–11; nations table + Babel + Abram stage).
- 2026-07-20: Package 5 Abraham split into 5 units (`gen_12_14_*` … `gen_23_25_*`; 5374 words).
- 2026-07-20: Isaac/Jacob package 5 units (`gen_26_isaac` … `gen_34_36_shechem_edom`; 5239 words).
- 2026-07-20: Joseph package 5 units completes **all Genesis** draft coverage (37–50; 6223 words; 26 gen_* files total).
- 2026-07-20: `NOTES_progress_observations_2026-07-20.md` — Gen whole-book, Gen→Lev ambient exports, Exodus Oral vs Gen, narrative/law hypothesis.
- 2026-07-20: Exodus track opened — `EXODUS_BUILD_2026-07-20.md`; unit `exo_01_israel_egypt_oppression` (1:1–22).
- 2026-07-20: `exo_02_moses_midian` (Exod 2:1–25).
- 2026-07-21: Exodus **full draft** — all remaining blocks exo_03…exo_40 via thorough schedule; 45 `exo_*` units; **1213** trees; Mekhilta samples on law spine; `EXODUS_BUILD_2026-07-21.md`; generator `artifacts/generate_exodus_units.py`.
- 2026-07-21: Narrative audio-oriented book of work so far: `BOOK_torah_grok_journey_so_far_2026-07-21.md` (Gen→Exod stack, method, density, Oral, debts); EPUB twin `BOOK_torah_grok_journey_so_far_2026-07-21.epub`.
- 2026-07-21: **Leviticus Build locked** — 50 thorough blocks; `LEVITICUS_BUILD_2026-07-21.md`; next `lev_01_olah_flock` 1:10–13; Sifra dual-track; Exod free-name imports.
- 2026-07-21: **Leviticus full draft** — autonomous pass wrote 48 units + kept 01; backfilled 1:4–9 trees; Lev 12 rewritten; generator `artifacts/generate_leviticus_units.py`; ~275 Sifra dual-track samples.
- 2026-07-21: Locked **narrative/BR research path** — `RESEARCH_narrative_model_br_ops_2026-07-21.md` (five rules; Gen 1:1–5 Written cold pass; BR ch.1 operations catalog; HYP_NARRATIVE_GENERATIVE_MODEL).
- 2026-07-21: Recorded **`architecture/Gods_Intention_2026-07-21.md`** — SI/progressive-revelation frame; BR core message under that frame; note that BR *et*/density claim **rhymes with Sefer Yetzirah** (small → registry) but differs in layer (verse-include vs letter ontology).
- 2026-07-21: Recorded **`Bereshit_Rabbah_Plan_for_Genesis_2026-07-21.md`** — gates/models definitions; BR open-pipeline for Genesis; links Gods_Intention + narrative/BR research path.
- 2026-07-21: **BR Genesis Interface** hub + first packet `br_genesis_packets/BR_1_10_bet.md` (Bet query firewall); non-sequential accumulation track.
- 2026-07-23: BR ch.1 **complete** (filled 1:2, 1:3, 1:7–9, 1:11–13); policy → **sequential** BR; hub `BR_Genesis_Interface_2026-07-23.md`; next **BR 2:1**.
- 2026-07-21: BR packets **`BR_1_5_honor`** + **`BR_1_14_et`** (honor/speech gate; *et* include-registry).
