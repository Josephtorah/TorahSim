# PROJECT REVIEW — 2026-09-13
# Ordered by the owner after Numbers closed and the ARCHITECTURE map was brought to the
# fourth book ("I want you to review the entire project. Look for errors or inconsistencies").
# Read-only: nothing was fixed. Every number below is from a print made this sitting; the
# prints are in the session scratchpad (review_*.out) and the commands are named so the
# sitting can be rerun.

## PART A — THE MECHANICAL GATES (every check the project owns, run this sitting)

| Check | Command | Result |
|---|---|---|
| The corpus gate | `python3 logic/corpus/CORPUS_TRUTH.py` | **GREEN** — 210 units, 1,809 facts, 341 demands (191 open), hash 8b8fff1fa28953af unmoved |
| The daemon gate | `python3 World/step9/daemon_census.py` | **GREEN** — 62 daemons watching 1,095 kinds; 427 functions WRAPPED, 0 OWED, 0 NONE; unfired 0, unconsumed 0, open aliases 3 (the same 3 the state doc has carried since 46 daemons) |
| The dependency gate | `python3 World/step9/dependency_census.py` | **GREEN** — reference 455 / transfer 48 / hypothesis 9 / none 143 of 482 edges + 173 pointers; 224 live edges beyond the census all on file |
| The register gate | `python3 World/step9/register_census.py --strict` | **GREEN** — DECLARED 102, DEBT 0, FAILS 0 |
| The journal gate | `python3 World/step9/world_journal.py --gate` | **GREEN** — 13,444 rows over 4 segments; ledger 1,539 = writes; timers 66 = sets (fired 52, pending 14); clock 157 = markers; population 148 = rows; closed 121 |
| The tape | `python3 World/step9/cold_run_sequence.py` | **10/10** — 1,279 events, 157 markers (forward 125 / proleptic 15 / retrograde 17), day 908,718 = creation 2488 = exodus (40, 6, 1); writes 1,527, entities 318, retro-writes 12; installation 62 = boot 22 / by an act 39 / pending 1; checkpoints 185 MATCH / 23 DIVERGE (the 23 the records name) |
| The parser's probes | `python3 World/step9/census_probes.py` | **208/208** |
| The probe files | installation 6/6, journal 7/7, views 6/6, cursor 6/6, sequence 4/4, clock (every row), population 9/9, register 7/7 | **all green** |
| The claim-labels gate | `python3 logic/solo_tools/claim_labels_census.py --strict` | **GREEN** — gen 1,663 / exo 545 / law 117 / lev 513 / num 385 labeled, debt 0 |
| The claims verifier | `verify_claims.py` over all 213 manifests | **0 failed** — 1,642 verified, 619 uncheckable, 962 no-check (the 619 unchanged since the 2026-09-02 audit) |
| The text layer | `verify_text.py` over all 210 frozen units | **210/210 TEXT LAYER GREEN** |
| The rendering layer | `python3 logic/py_units/ALL_UNITS.py` | **ALL ASSERTIONS GREEN** |
| The changelog gate | `python3 logic/solo_tools/changelog_gate.py` | **GREEN** — 10 unit YAMLs edited since HEAD, each with its changelog line |
| The vocabulary lint | `python3 World/step9/vocab_lint.py` | **0 flags** on 1,779 values / 150 dimensions |
| Syntax | `ast.parse` over 1,002 .py files | **1 file does not parse** (item 14) |
| Registries and data | `yaml.safe_load` 394 files, `json.load` 961 files; a duplicate-key loader over 372 registry and unit files | **0 parse errors, 0 duplicate keys** |
| The frozen set | 210 frozen of 309 unit files; each has its py_unit, its manifest and its render; UNIT_INDEX.html links 210 | **complete** |
| Path references | every `World/…`, `logic/…`, `ARCHITECTURE/…` path named in 174 records + 813 units/runners/registries/manifests | **2 dead paths**, both `logic/corpus/corpus_world.sqlite` (gitignored derived DB, not on disk; named in REPORT_EVENT_REGISTRY.md and memory step9-exam-era.md) |
| The sweep | `python3 World/step9/run_cold_all.py` | **57/57 runners green, 6,378 graded cells** (21 minutes; every runner's own N/N equal) |
| The exam runners | every `World/step9/run_*.py` but run_cold_all (47 files) | **47/47 exit 0**; the 46 case runners print 0 misses (1,585 cases summed from their own lines); run_exam.py prints its before/after table |
| The unit regression | `run_unit.py <uid> --scenarios` over 210 frozen | **210/210 ALL SCENARIOS GREEN** |
| The map against the sweep | catalog_facts.json score lines vs the sweep's 57 prints | **57/57 equal**; DEPENDENCIES.md's runner table carries no score column (nothing to compare); FUNCTION_CATALOG.md's cards: item 18 |

## PART B — ERRORS AND INCONSISTENCIES FOUND (ranked; nothing fixed)

### B1. Records that disagree with the tree

1. **World/step9/COMPILE_DEBT.md line 737 — a box unchecked that says PAID inside it.** The Num 27:1-11 + 36:1-12
   inheritance-order box is still `- [ ]`, while its own text (from "SITTING 4 THE DAUGHTERS OF ZELOPHEHAD — THIS BOX'S
   OWN ORDER PAID (2026-09-09…)") records the compile, cold_run_zelophehad.py 55/55. The other two open boxes (THE LOOP
   at line 649, step 6 owed; Deut 25:5-10 at line 785) are open by design.
   → PAID 2026-09-13 ("Yes"): the box ticked; the paragraph untouched.
2. **THE_BRIEFING.md line 17 — the scoreboard's date is stale.** "SCOREBOARD (as of 2026-09-12, latest)" heads a list whose
   top three entries are 2026-09-13 (sittings 14b, 15, 15b).
   → PAID 2026-09-13 ("Yes"): the heading retyped "as of 2026-09-13".
3. **The recovery file's lint baseline is wrong for thirteen files.** RECOVERY_new_thread_2026-09-12.md section 3 says
   "everything else 0 (… every … runner, probe file, registry)". Measured this sitting: cold_run_temurah.py 11,
   cold_run_moadim.py 7, cold_run_minchah.py 5, cold_run_yovel.py 2, cold_run_tzav.py 2, cold_run_pesach_sheni.py 1,
   cold_run_mekoshesh.py 1 (pre-walk runners whose Hebrew cell labels run past the 90-character window);
   dependency_census.py 8, daemon_census.py 1; DEPENDENCY_INDEX.md 8 (gate-written — the gate's own print carries the
   flags); EXAM_LEDGER.md 7, REPORT_CANON_HUNT.md 8, REPORT_FESTIVALS.md 2, CORE_SHELF.md 1. Every NAMED baseline holds
   exactly: the state doc 147, THE_STEPS 1, MIDDOT 1, THE_WORLD 5, STAMP_LEDGER 1, MOVE_CATALOG 5, RESEARCH_LOG 52,
   step9-exam-era.md 7, MEMORY.md 5, cold_run_sequence.py 7, census_probes.py 1; and THE_BRIEFING, COMPILE_DEBT,
   THE_LOOP, THE_TENT, NUMBERS_WALK, SEQUENTIAL_RUN, RESUME, MISHNAH_TOPICS, REGISTER_INDEX, DAEMON_INDEX are 0.
4. **The state doc's compaction numbering is not a sequence.** Of lines opening with "COMPACTION POINT #n": 14 numbers
   are used two or three times (#23-#26, #28-#30, #33-#35, #61, #62, #101, #103), 15 numbers are never used (#1-#4,
   #6-#12, #15, #18, #21, #40), and one stretch (lines 2314-3260) runs backwards from #35 to #19. #144-#168 are clean and
   in order. Historical; the ledger is append-only — recorded so a "reread #n" is known to be ambiguous below #104.

### B2. The git tree against the never-commit law

5. **ARCHITECTURE/ is eight days ahead of its last commit and the staging form excludes it.** CHRONICLE.md was rewritten
   2026-09-07 (+102/−129 lines against HEAD; "design, not yet built", 105 lines) — the folder's last commit is 632790c of
   2026-09-05. Untracked there: DATABASE_SPECULATION.md (2026-09-11), THE_TOUR / THE_EFFECTS / THE_CLOCK / TIME /
   THE_LINKS with six epubs, diagrams/08; modified: the README, DEPENDENCIES, STATE_MACHINES, FUNCTION_CATALOG,
   NARRATIVE, catalog_facts.json, two diagrams, the program pages, six tools. The standing form
   (`':!ARCHITECTURE'`) never carries any of it; whether it rides is the owner's call.
   → RULED 2026-09-13 ("Let's add it to all commits going forward"): the exclusion is dropped from the staging form;
   the folder rides the next "commit push" and every one after.
6. **.gitignore does not hold the never-commit set.** Data/discord_backup_codes.txt (SECRETS), DISPOSABLE_scan/*.zip (two
   zips), cases_pilot.yaml, logic/gork/, grok-mockups/ and open_ledger/ are all untracked AND unignored — only the
   staging form's exclusions keep them out. One `git add -A` typed without the exclusions stages the secrets file.
   (Nothing from the set is tracked today: checked by `git ls-files`.)
   → PAID 2026-09-13 on the owner's "Ok add them": the six patterns appended to .gitignore (cases_pilot.yaml,
   grok-mockups and open_ledger anchored to the root), each verified with `git check-ignore -v`.
7. **DISPOSABLE_scan/ is both tracked and excluded.** 20 files there are tracked (Deut_digest.md, Exod_formulas.md,
   Gen_symbols.md, …) while the staging form excludes the whole folder — a change to a tracked file there can never
   ride a commit.
   → RULED 2026-09-13 ("Keep them tracks and narrow"): the twenty files stay tracked and ride; the staging form is now
   `git add -A -- . ':!elijah_docket' ':!DISPOSABLE_scan/*.zip'` — the other exclusions dropped because git exits 1 when
   an exclusion names a path the ignore list already holds (dry run: exit 0, 667 adds, the set out, ARCHITECTURE aboard).
8. **The elijah_docket gitlink is permanently stale by construction.** The parent records commit 8d9eedb; the nested
   repo sits at 166f814 (2026-09-05) with one dirty line. "Never stage" means the pointer never updates. Information
   only — a fresh clone gets no content from it either way (no .gitmodules).

### B3. The corpus layer

9. **Three orphan manifests, and nine claim ids that are not unique.** logic/oral_audit/manifests/ holds
   law01_exo_21_1_11, law02_exo_21_12_27 and law03_exo_21_28_37 (the law era's, 2026-08) with no unit file under
   logic/units/ (the law-era drafts live in logic/law_era/). Their ids collide with frozen manifests: L13-01..L13-04
   (law02 against lev_13_intake_quarantine), L19-01..L19-03 (law02 against lev_19_holiness_duty_ledger), L0-01 and
   L0-02 (law02 against law03). 3,214 distinct ids over 3,223 claims. The claim-labels gate keys per file, so it does
   not see this; anything that keys claims by id alone would.
   → LEFT AS IT IS, by ruling 2026-09-13 ("Ok"), after measuring: the three are the gate's "law" group (117 labeled
   claims) and the LR1 ceilings file names them — not orphans; the shared ids are a naming coincidence (Exodus 21:13
   against Leviticus 13) and every citing record sits on one side. THE RULE: a join of claims across manifests keys by
   (manifest, id), never by id alone.
10. **The verifier's blind spot has a size: 619 of 3,223 claims are UNCHECKABLE** (a check no tool can run — manuscript
    pointing, midrashic readings, court-derivation claims) across 75 manifests, most of them the 2026-08 Genesis and
    Exodus units (exo_22 has 0 verified / 10 uncheckable; gen_08 17 / 13). 0 failed. Unchanged since the 2026-09-02
    audit; not an error, recorded as the number.
11. **71 stale renders beside the 210 current ones.** logic/pre_logic_methods_2026-07-28/ holds 282 UNIT_*.html; 71 are
    dated versions (60 of 2026-08-08, 5 of 07-30, 3 of 08-06, 2 of 08-23, 1 of 08-05) that UNIT_INDEX.html no longer
    links. Leftovers, not errors.
    → PAID 2026-09-13 ("Yes"): all 71 deleted by script after the check that none was a frozen unit's page or linked.
12. **One draft's id differs from its filename.** logic/units/br_1_1_amon_cluster_tree_logic_2026-07-26.yaml carries
    id br_1_1_amon_cluster_tree_logic (a July draft; status draft).

### B4. The Hebrew-gloss law (HEBREW NEVER WITHOUT ITS ENGLISH INLINE)

13. **797 of 2,223 .md/.py files carry flags — 20,483 flags — and the law's own baseline names eleven of them.**
    The bulk is pre-law content: reviews/, artifacts/, logic/middot_scan, web/taamim_tree, logic/law_era,
    logic/gen_boot, logic/Parse_tree, Disclosure — 389 files, 16,693 flags (MIDDOT_invocations_cached.md 2,344 alone).
    In the current era: logic/py_units — 70 files, 334 flags (ALL_UNITS.py 330): the Python rendering layer prints
    each unit's Hebrew without its gloss (the 2026-09-05 sitting glossed the HTML renders, not the .py renders);
    World/step9/gen_sweep_raw.md 1,373 (a raw shelf dump committed 2026-08); logic/oral_triage — 49 files, 151 flags
    (exodus_backfill_mishnah 16, gen_01_creation_boot 14, noahide_exam_reading 9, all 2026-07/09-01 ledgers);
    memory: oral-first-insight-pipeline.md 18, derivation-era.md 6, law-era-top10.md 3, the memory file on the two windows 3,
    and 18 files at 1-2. Every Numbers-walk ledger, docket, manifest, unit and runner is 0, as is every ARCHITECTURE file.
    → The py_units part measured 2026-09-13 and LEFT OPEN as its own sitting ("Ok next"): the 334 flags are
    transliteration fallbacks — about 350 machine-token pieces with no English in the gloss dictionary; the pay is
    their English in word_gloss_overrides.yaml, each read at its verse, then the 210 renders rerun.
    → gen_sweep_raw.md DELETED 2026-09-13 ("Yes"): the ledger GEN_SWEEP_LEDGER.md holds the reading at 0 flags.
    → THE CODE SIDE PAID 2026-09-13 ("Yes don't skip"): the seven runners, both gate scripts and the eight registry
    notes at 0 flags (patch_gloss_code.py in the forms folder); the cause was the lint's window stopping at a period,
    so a "..." inside a Hebrew quote stranded the words before it; the seven scores unchanged from the sweep, the
    dependency index regenerated at 0, the daemon index byte-identical.
    → THE MEMORY SIDE PAID 2026-09-13 ("Yes"): 23 files glossed in place (patch_gloss_memory.py); four flags remain,
    all MEMORY.md's own "- [Title](file.md)" links, whose hyphenated file names sit right before ".md" — unpayable
    under the window's period rule and the index's link form. New baselines: MEMORY.md 4, step9-exam-era.md 0.
    → THE LEDGER SIDE PAID 2026-09-14 on the RULING "a gloss is display, not content" ("ok first one go"): 169 places in
    the 49 older ledgers and four reports glossed in place (flag_places.py measured them with line and token;
    patch_gloss_ledgers.py paid them by asserted replacement); all 53 files at 0. What remains in the current era:
    the py_units renders (their own sitting) and MEMORY.md's four file-name links.

### B5. Small hygiene

14. **One .py that does not parse:** World/step9/forms_numbers_walk/architecture_2026-09-13/numbers_blocks.py — the ten
    BLOCKS rows saved as a fragment (unexpected indent, line 1). A form, never run; the one failure in 1,002 files.
    → PAID 2026-09-13 ("Yes"): renamed numbers_blocks.txt.
15. **The_Briefing.epub at the root is eleven days behind THE_BRIEFING.md** (baked on the owner's word only; the other
    29 epub/md pairs are current, the ARCHITECTURE seven among them).
    → PAID 2026-09-13 ("Yes update"): rebaked by the house builder under its old title; archive tested whole.
16. **The shelf mirror's manifest lists 134 pruned files as fetched rows.** Data/sefaria_export/MIRROR_MANIFEST.txt keeps
    the rows of the Tosefta Lieberman commentary layers (Brief Commentary, Masoret HaTosefta, Tosefta Kifshutah,
    Variants — 33 each; Chibbah Yeteirah 2) that its own PRUNED block of 2026-08-10 says were removed. 6,346 JSON files
    on disk, every one in the manifest; the 113 rows marked "skip" are present. A reader of the rows alone expects
    134 files that are gone.
17. **World/journal/registers/event_kinds.yaml is the August register** (version 0, 37 kinds) beside the engine's
    1,095 — still read by build_world.py, population_probes.py and journal_probes.py. By design until D7's merge.

### B6. Found after the sweep

18. **ARCHITECTURE/FUNCTION_CATALOG.md — thirteen of the fourteen 2026-09-05 cards carry a score their own table
    contradicts.** The cards' "Score" and "Provenance" lines still read as printed on 2026-09-05, while the file's own
    "The fourteen cards of 2026-09-05, checked again today" table and today's sweep print the current cell counts:
    calendar 14/14 → 17/17, decalogue 12/12 → 13/13, lev24 (2/2, 4/4 …) → 24/24, mishpatim (3/3, 5/5 …) → 24/24,
    mishpatim_2 (3/3 …) → 13/13, moadim 24/24 → 42/42, negaim 7/7 → 17/17, offerings 40/40 → 58/58, pesach 24/24 →
    25/25, shemini 19/19 → 20/20, tzav 33/33 → 54/54, vayikra5 27/27 → 32/32, yoma 18/18 → 23/23. The cells grew as
    later spans called these engines; the 43 cards generated on 2026-09-13 and catalog_facts.json are all current.
    (The card for cold_run_mamre.py, cold_run_joseph.py and cold_run_moadim.py carry no plain "Score" fraction at all.)
    → PAID 2026-09-13 ("Yes"): all 57 cards regenerated by the same script (build_catalog_review.py in the forms folder);
    verified before landing: every Score line equals the sweep, the 43 earlier cards byte-identical, only the fourteen
    bodies changed, titles and numbering unmoved, gloss lint 0.

## PART C — WHAT HELD

The whole compiled program stands as the records say: 210 frozen units, standing 2,163, hash 8b8fff1fa28953af;
57 runners at 6,378 cells, 62 daemons, 427 functions; 210/210 units green on their scenarios and their text layer; the tape's RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121); the
population 148; effects 1,012, kinds 1,095, entities 338; edges 482 + pointers 173; register seats 102; moves M-01..M-30
with no gap; findings F-001..F-268 with no gap across logic/; every label code in the manifests defined in MIDDOT.md or
MOVE_CATALOG.md; the sitting heads 1..15b each present in NUMBERS_WALK.md; RESUME's SITTING lines unique; no 2025 date
typo in the current records; no leftover scratch files in the tree; MEMORY.md 13,327 bytes (limit 17,000); the
DAEMON_INDEX / DEPENDENCY_INDEX regenerate byte-identical between the gate run and the sweep (md5 76213e33… and
da83295d… both times).

## PART D — NOT RE-VERIFIED THIS SITTING

The coverage lines of the reading ledgers and the cite indexes of the dockets (computed at their writing steps by
their own scripts; not recomputed here); the content of the epubs; the TorahSim mirror and the web export; the
ARCHITECTURE tutorials' prose numbers beyond the ones the map files share with the gates.
