# TANAKH RUN — Exodus 21 executed across the 24 books (PLAN)

**Folder:** `logic/law_era/tanakh_run/` — the test lives here, isolated.
**Status:** PLAN ONLY (owner discussion 2026-08-12). **No code yet.**
**Contract:** experimental, **not binding law** (same standing as `logic/gork/`);
nothing here touches the frozen layer; no mechanical gates bind on it;
commits only on owner word.

## The experiment (owner's theory, 2026-08-12)

Compile Exodus 21 into one runnable machine. Sweep the entire 24 books for
the data the chapter runs on. Harvest it. Run every harvested scene through
the code and watch it execute. Two passes over the Tanakh: **pass 1
initializes the world, pass 2 runs the code.**

## Agreed design

**Verdicts are per-scene; facts are sequential.** The law is a per-case
function over a persistent world: the תם→מועד ("innocent"→"forewarned")
flip is accumulated state, the six-year slave clock is state, ownership
must persist goring→verdict (abandon the ox after it gores and payment
lapses), the verdict itself is a state-write (the prohibition lands at
גמר דין, the sentencing — not at the stoning). So the two modes are not
rivals — same judgments, state supplied two ways. **One scene schema, two
executors:**

1. **FIXTURE MODE (per-scene):** every scene self-contained; statuses
   hand-declared in the fixture ("Joseph: slave, foreign jurisdiction").
   Deterministic, debuggable, each scene runs in isolation. Form is the
   proven gork catalog + runner.
2. **REPLAY MODE (sequential):** the same scenes ordered on a timeline
   become an event stream; the world folds over it — each event first
   CONSULTS state (is this ox forewarned? which slave-year is this man
   in?), gets judged, then WRITES state.

**Cross-validation between the modes is itself a finding-generator:** for
every scene, diff the fixture's hand-declared state against the
replay-derived state. Agreement → harvest sound. Divergence → either a
missed event in the harvest or narrative-implied state — a finding
either way.

**Era / jurisdiction flags** (field already exists as `application_mode`
in the gork catalog): pre-Sinai → typology mode (soft asserts);
post-Sinai Israel → binding mode (hard asserts); foreign courts →
comparative mode. Exception with a source: the goring ox has a pre-Sinai
Noahide layer — Gen 9:5 מיד כל חיה אדרשנו ("from every beast I will
demand it"), Hirsch's delegated-judgment reading (block-3 scan, B19) —
so pre-Sinai goring scenes may legitimately run in "Gen 9:5 mode"
(the demand exists, the 30-shekel tariff does not).

**Three harvest channels:**
1. `export_links` Tanakh-category crossrefs anchored at Exod 21 (seed set,
   small — where the scan's tanakh-close verses came from).
2. The oral-scan digests' crossref index — 143 digests across blocks 1-3
   are full of narrative-legal crossrefs the tradition itself found
   (Joseph's 20 silver vs the halving clause; Zech 11:12's thirty as
   shepherd's wage; 1 Kgs 20:39 soul-or-talent; the Gibeonites' ransom
   grammar in 2 Sam 21).
3. Lexical sweep of `tanakh.sqlite` on the operative roots — נגח ("gore"),
   בור ("pit"), מכר ("sell"), גנב ("steal"), כפר ("ransom"), הכה
   ("strike"), עבד/אמה ("slave/maidservant"), שקל ("shekel") — to catch
   scenes the link graph missed.

**Flagship expected scenes** (the Tanakh executing Exod 21 itself):
- 1 Kgs 2:28-34 — Solomon executes 21:14 VERBATIM on Yoav at the altar
  (מעם מזבחי תקחנו למות, "from My altar you shall take him to die").
- 2 Sam 12 — Nathan's parable: David outputs ארבעתים ("fourfold") = the
  four-sheep tariff of 21:37.
- Jer 34 — slave-release breach with covenant sanction (gork already has
  it as the one `breach` fixture).
- 1 Kgs 20:39 — "your soul for his soul, or weigh a talent" (cofer
  structure in prophetic narrative).
- Neh 5 (daughters subjected), 2 Kgs 4:1 (creditor and children),
  2 Sam 21 (Gibeonites: ובמה אכפר "with what shall I atone" in the
  ransom-grammar of 21:30), Gen 37 (Joseph sale, typology), Exod 2
  (Moses' homicide — mens-rea fork, pre-statute).
- **Expected negative finding:** no ox ever gores a man in Tanakh
  narrative — block 3 runs only through parable, prophecy, ritual.
  Report it as a result.

**Forward demands:** scenes that hit Exod 22:1-14 logic (burglar,
guardians — block 4) route to stubs marked FORWARD, never faked. The
machine already has this pattern (the block-1 DEPENDS table's 7 forward
demands).

## Prerequisites (in order; each step starts on owner word)

**REORDERED 2026-08-12 (owner delegated the call): harvest-first.**
Step order is now 1 → 5 → 2 → 3 → 4 → 6: the harvest (pass 1) depends
only on the scans, so it runs before the coding days; pass 2 still
waits on the assembled machine. Rationale: the scene catalog gives the
coding days real fixtures, and block-1 scenes (Joseph, Jer 34, Neh 5,
2 Kgs 4:1) can run early against the existing block-1 machine.

1. **21:37 tail scan** — ✅ **DONE 2026-08-12**: 4 clips (bites 24-27 +
   tanakh close), 172 rows (169 readable + 3 tanakh — final split per
   the widened-census queue; the earlier estimate said 185+4 with 17
   dual-anchor, the queue resolved to 169+3 new), ledger 4,731 → 4,903
   = census EXACT, dump --status 0/0 → **exo_21 CHAPTER GATE GREEN,
   coverage continuous 21:1-37.** Notes: bites 24-27 digests + tanakh
   close in `scratch_mirror/law03_scan_notes.md`. The tanakh close's
   last row is 2 Sam 12:6 — David's ארבעתים ("fourfold") — the
   flagship scene closing the chapter ledger on its own.
2. **Block-3 coding day** — ✅ **DONE 2026-08-12**: claims manifest
   `logic/oral_audit/manifests/law03_exo_21_28_37_claims.json` (28
   multi-witnessed claims incl. the 21:37 tail) + the machine
   `logic/law_era/exo_21_v2_block3_DRAFT.py` — asserts GREEN first run;
   14-edge dependency proof (6 resolved into frozen units incl. Gen 9:5
   and Joseph's pit; 8 forward incl. Zech 11:12 / 2 Sam 12:6 /
   1 Kgs 20:39 — tanakh-run scene verses now formal machine demands).
   NOTE on placement (owner Q, 2026-08-12): machines + manifests live in
   the LAW-ERA line (`law_era/`, `oral_audit/manifests/`) like block 1,
   because they head for the frozen layer via chapter assembly; this
   folder stays experimental and only CONSUMES the machine — pass-2
   executors will import it from there, as gork imports block 1.
3. **Block-2 coding day** — 36 digests → homicide fork (mens rea),
   altar/refuge, עין תחת עין ("eye for eye") damages semantics, the five
   injury heads, slave-striking, fetus/כופר.
4. **Chapter assembly** — `exo_21_v2`: statute-0 runtime + blocks 1-3 +
   the 21:37 opener; all asserts green; freeze on owner word (chapter
   gate + preflight + gloss_lint per the forward-era law).
5. **PASS 1 — the harvest:** ✅ **DONE 2026-08-12** (owner word "pass
   one harvest go"; runs second under the harvest-first reorder). All
   three channels run: `harvest_pass1.py` → `harvest_ch1_links.json`
   (70 true verse crossrefs), `harvest_ch3_lexical.json` (31
   statute-derived lemmas ≤90 freq swept in full + 5 surface patterns,
   ~700 candidates), digests mined for channel 2 →
   **`scene_catalog_tanakh_run_2026-08-12.json`: 57 scenes** (21 P0),
   157 refs, 50 chronology-keyed + 7 achronic, 5 FORWARD-touching;
   report: `HARVEST_PASS1_REPORT_2026-08-12.md`. Negative finding
   confirmed mechanically (no narrative ox-gores-man in 13 total נגח
   "gore" hits). Entity-registry join deferred to pass-2 world-init
   (registry ends at Exod 21; scene entities are scene-local tokens).
6. **PASS 2 — the executors:** fixture runner + sequential replay; per
   scene record: the code's verdict, the narrative's own outcome, and a
   **CONFIRM / DIVERGE / NO-VERDICT-IN-TEXT** comparison. Divergences
   are the treasure: jurisdiction fact, pre-Sinai typology, or genuine
   finding. **Deliverable AMENDED by owner ruling 2026-08-12: a LIVE
   WEB APP, not a report** — the executors serve a local web UI: (a)
   run any catalog scene and show the machine's verdict beside the
   narrative outcome; (b) the form binder (gork's "not yet" item):
   enter custom facts, watch the chapter rule; (c) replay mode as a
   timeline scrubber over the chronology keys (world-state visible:
   the תם→מועד "innocent"→"forewarned" flip, Nathan's fourfold debt
   discharging). Architecture: small local Python server (stdlib or
   Flask) over the machine + tanakh.sqlite; Hebrew glossed via
   gloss_db.py per the absolute rule; UI sketches exist in
   grok-mockups/ (untracked). Public hosting = separate later
   decision. The chapter-level summary ("the law ran N times across
   the Tanakh") lives as a page IN the app.

## Open owner rulings (needed before pass 1)

- **Timeline semantics:** canonical book-order vs narrative chronology
  for the replay. Recommended: canonical order for the sweep, a separate
  chronology key per event for the fold.
- **Parallel accounts:** Samuel/Kings ↔ Chronicles tell events twice with
  different numbers (Araunah's floor: 50 silver shekels vs 600 gold —
  the exact contradiction R. Tam's coinage essay harmonizes, block-3
  scan B14). Recommended: merge parallels into ONE event with two
  witnesses (house multi-witness pattern).
- **Replay world scope:** Exod-21 lens only over the full timeline
  (recommended) — other chapters' laws stay forward demands.
- **21:37 routing:** read now as a block-3b tail (recommended — shortest
  path to the gate) vs fold into block 4's census.

## Existing assets this test stands on

- Machine (block 1): `logic/law_era/exo_21_v2_block1_DRAFT.py` — asserts
  green, DEPENDS table (22 edges) + `verify_dependencies()` against the
  frozen corpus.
- Fixture precedent: `logic/gork/scene_catalog_exo_21_block1_2026-08-11
  .json` (48 fixtures; modes gate_fixture/halakhic/typology/lexicon/
  measure/breach/patch) + `run_scene_catalog.py` (allowlisted handlers).
- Oral layer: `logic/oral_audit/ledgers/Exod_21.jsonl` — 4,731 rows,
  blocks 1-3 scans COMPLETE (gates green); notes mirrors
  `logic/law_era/scratch_mirror/law0{1,2,3}_scan_notes.md`.
- Claims (block 1): `logic/oral_audit/manifests/law01_exo_21_1_11_claims
  .json` (39 claims, multi-witnessed).
- World: `corpus_world.py` + entity_registry/settlement_links (ONE world,
  code-is-physics) — pass 1's natural substrate.
- Texts: `torah_grok.sqlite` (FTS 41,114 segments + 668,695 links);
  `elijah_docket/tanakh.sqlite` (the 24 books, he/en).

## Answer of record: "do we have enough Exodus?"

Not yet, and honestly so: scans are complete for 21:1-36 (one clip short
at 21:37); CODE exists only for block 1 (21:1-11). "Compile Exodus 21"
= steps 1-4 above. The test folder is step 5-6, not step 1.
