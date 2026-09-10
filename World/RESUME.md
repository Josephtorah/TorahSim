# ⚠ MOVED INTO THE REPO (owner's word, 2026-08-31: "I think we should add
# the world to this repository") — this folder now lives at
# Torah_Grok/World/, superseding the 2026-08-30 keep-it-separate
# instruction quoted below (kept for the record). A symlink at
# <world-link> preserves every old path. world.sqlite and
# __pycache__ are gitignored — the model layer is rebuilt, not archived
# (python3 run_genesis.py --quiet). The read-only-over-the-corpus and
# never-invent rules are UNCHANGED.

# RESUME — read this first

**This folder is its own project.** Owner's instruction, 2026-08-30: *"You
create a folder that we can refer to that is separate from the rest. This is
where the world gets built. Keep it to itself. Not in Torah_Grok, that grok
created."*

It is not inside `Torah_Grok` and not inside `Torah_Grok_local`. Grok's earlier
attempt lives at `Torah_Grok_local/genesis_world/` and is **untouched** — leave
it that way; it is a record of a different approach, not a thing to edit.

## Where it stands

`world.sqlite` is BUILT and GREEN. Run `python3 build_world.py --check` to
confirm before doing anything else — it reconciles the database against
`corpus_world.fold()` on ten counts plus the state hash. Everything matched at
last run.

**The three books (as rebuilt 2026-09-08 at O10 THE PEOPLE-TOKENS, the fold's
journal revision 127):** 163 units · 2,639 verse refs · 439 entities · 1,809
facts · 557 events · 740 relations · 341 demands (191 open) · 1,778 standing ·
hash `8b8fff1fa28953af` (unmoved by the fold's identity table — the hash's basis
is facts, open demands and names; the seventeen re-homed mentions live in the
mentions and entities tables). The Genesis-only build of 2026-08-30 read: 97
units · 2,074 verses · 278 entities · 905 standing, the same hash.

Source corpus: `<repo-old>`, HEAD `b3a11fc`, read-only. Genesis is
derived end to end, stamped full rule by the owner, and published.

## The standing rules of this place

1. **Never write back to the corpus.** Read-only, always.
2. **Never invent data.** Every row cites the operator that produced it.
   `relations` and `entity_state` are projections, not inferences.
3. **Reconcile every build.** Disagreement with the fold is a finding.
4. This is the **model layer** — freely rewritable, allowed to be wrong,
   allowed to be deleted. The corpus is the evidence layer and is none of
   those things.


## run_genesis.py — THE TEACHING RUN (2026-08-31, owner: "recreate what I
tried to create with opus in world")

The missing organ, built: the same world, played back one row at a time so a
person can watch it grow and learn what each row kind means.

    python3 run_genesis.py             # full Genesis, pause at each parashah
    python3 run_genesis.py --no-pause  # stream straight through
    python3 run_genesis.py --quiet     # rebuild + save narration, no terminal

- Narration SAVED to a `narration` table (lessons, blocks, parashah
  summaries): re-read any stretch with
  `python3 ask.py sql "SELECT line FROM narration WHERE parashah='Vayetze'"`
- HEBREW RULE enforced by design: quote-never-compose — every Hebrew shown
  is lifted from the verse the row cites, with the corpus's own gloss; the
  machine's own notation stays English; no match -> English, never a guess.
  Ink coverage is measured and stored in meta (ink_hits / ink_misses).
- First-occurrence LESSONS teach each row kind (fact, event, demand,
  settlement, naming, witness, test, block close).
- The run ENDS by reconciling against corpus_world.fold() on every count and
  the state hash — the slow run provably builds the same world as
  build_world.py. 18 demands are recorded settled with no clock pointer;
  they never enter the live open-count, which closes the book at exactly
  the fold's 191.
- Owner picks 2026-08-31: pause at parashah grain; narration persisted.

## journal/ — THE WORLD JOURNAL, MOVED IN 2026-09-09 (read step9/THE_LOOP.md first)

The owner's PERMANENT ruling of 2026-09-09: the step-9 engine becomes a running simulation with memory — its log
written to this journal (the 2026-08-24 envelope, hash-chained, one segment per run), indexed in sqlite, gated by
installation, resumed at a cursor, taking scenarios. `journal/` holds the August build moved out of the mockups:
`worldledger.py` (the envelope, the chain, `index_sqlite`), `build_world.py` (the L0/L1 fold over the frozen units,
`--selftest` the byte-identical determinism gate), `run_cases.py` (the L2 scenes), `registers/`, `primary/scenes.yaml`;
`data/` is derived and gitignored — rebuild with the two scripts. As rebuilt 2026-09-09: 6,601 rows indexed, determinism
GREEN, one August tree checklist line (the forming/filling symmetry of days 4-6) FAILING against today's units —
filed for the loop's first sitting. The five steps, their order and gates: step9/THE_LOOP.md. STEP 1 THE SINK BUILT 2026-09-09:
`python3 step9/cold_run_sequence.py` now writes four L3 segments here (`data/L3_run_cold_run_sequence_<world>.jsonl` — the running
setting, the fork's two, THE REST; 2,494 / 2,494 / 2,494 / 1,844 lines) and rebuilds `data/world.sqlite` from every segment on
disk (15,927 rows: L0 4,517, L1 2,041, L2 43, L3 9,326); `python3 step9/world_journal.py --gate` runs the tape twice in two
processes and demands byte-identical segments (GREEN); `--reindex` rebuilds the index alone; `--verify <segment>` checks a chain.
The eight run kinds are in `registers/event_kinds.yaml` (run.skip the eighth, step 3's). STEP 3 INSTALLATION BUILT 2026-09-09: the
sequence worlds opt in (`installation=True`), every daemon carries given_at + installed_by (step9/daemon_dispositions.yaml; the gate
demands both), the institutions are registry entities whose in_force the tent daemon writes at the acts of step9/installation_parameters.yaml,
and the engine asks before every call; the running setting is boot (nothing skipped, the would-skip count printed: 34,729 of 46,552);
the segments are +5 lines each (the five in_force writes), the index 15,947 rows. `python3 step9/installation_probes.py` runs the six probes.
STEP 2'S REMAINDER BUILT 2026-09-09: the events table carries `source`; the four run VIEWS (run_ledger, run_timers, run_clock,
run_docket — `journal/run_views.sql`, created at every reindex); `python3 step9/world_journal.py --views` checks every view's count against
the table's on every world; `--ask ledger <entity> [<day>] | open <verse> | who <entity> <effect> | custody [--world <source>]` answers the
four questions; `python3 step9/view_probes.py` runs its six probes. NUMBERS' OPENING BLOCK OPENED 2026-09-09 (step9/THE_TENT.md):
the blasphemer's four acts on the tape, the docket's first row (`--ask who the_court declaration_owed`), the tent daemon's halt, output and
execution branches real; the three Numbers cases next, each after its reading and its unit. SITTING 2 DONE 2026-09-09 (the unclean men at
Passover, Num 9:1-14): the first Numbers unit frozen (num_09_pesach_cloud), the first Numbers runner (step9/cold_run_pesach_sheni.py), the
second case-born law (statute_declared) on the tape; the tape now spans FOUR books (its first Numbers marker at 9:5; the index 16,691 rows
over seven segments); `--ask ledger the_unclean_men` shows the wait written and closed by the output's verse, and the men's second Passover
a PENDING timer (`run_timers`, outcome pending) — the readback's first open item. SITTING 3 DONE 2026-09-09 (the wood-gatherer, Num
15:32-36): the unit num_15_wood_tzitzit frozen, the runner step9/cold_run_mekoshesh.py (the procedure from the guard to the grave; the
death mode was already a cell of the Exodus Sabbath engine, given its home), the third case-born law installing A RULE INSIDE A LAW
(`--ask who the_tent_of_meeting rule_installed`: three rows — Lev 24:13-14, Num 9:9-14, Num 15:35); `--ask ledger the_wood_gatherer`
shows five entries, the three body entries closed by the execution's verse (the death sentence among them — found open by this very
question after the first run, then closed by the amended branch); the docket's covered_by names two daemons. SITTING 4 DONE 2026-09-09 (the daughters of Zelophehad, Num 27:1-11 + 36:1-12; THE_TENT.md section 4 + 4a): the halt's third form,
the second output relayed, a reading-placed marker in the fortieth year whose walk FIRED the men's second Passover (open on the ledger —
the readback's item, with the daughters' holding owed, given in Joshua); RUN (1077, 44, 44, 0, 0, 1257, 18, 260, four pairs, 84); THE
LOOP's steps 4 and 5 built (World/step9/cold_run_sequence.py --cursor <verse>; World/step9/scenarios.yaml; cursor_probes.py 6/6) — the
first scenario 3/3 at the left edge of Num 27:5. The block closes. THE NUMBERS WALK OPENED 2026-09-09 (the owner: in order from 1:1;
the map step9/NUMBERS_WALK.md): SITTING 1 DONE — Bamidbar 1:1-4:20 read at the parashah grain (nine ledgers by one script, 160 sources,
coverage computed; the Sifrei on Numbers has no row on the portion, its export's piska 62 a mislabel for 8:24), nine units frozen (176),
32 claims seated and machine-checked, standing 1844 (predicted), hash unmoved; the census's arithmetic computed from the ink (603,550 on
three seats; 22,300 against 22,000; 273 × 5 = 1,365); the engine's numeral parser measured UNABLE to read the census (1:21 → 1,546) — the
compile sitting's item with Num 1:1's forward marker; next Naso 4:21-7:89. SITTING 1b DONE 2026-09-09 (THE COMPILE OF
BAMIDBAR; step9/NUMBERS_WALK.md "Sitting 1b"): the exam docket 159 rows (num_01_04_bamidbar_exam_2026-09-09.md); the parser
taught the census's grammar (step9/census_probes.py 17/17; every marker verified; the old-against-new diff over the four books
read — 155 verses moved, none a marker; the two homographs by the points on the stem); step9/cold_run_bamidbar.py 66/66, the
48th daemon law_census; the tape's thirteen lines and the 1:1 marker (9:5 RETROGRADE; CB1-CB8 MATCH; RUN (1090, 44, 44, 0, 0,
1277, 19, 261, four pairs, 89); THE REST exact); the cursor's bound rule (a forward marker at the cursor closes the bounds
behind it — cursor_probes 6/6; a cursor inside a bound refused, recorded in THE_LOOP.md); the journal gate GREEN; the sweep
43/43 at 4,699. Next: Naso 4:21-7:89, the reading sitting.

## step9/ — THE FIRST EXAM RAN (2026-08-31, read step9/REPORT.md)

TOOLING AS OF THE SAME EVENING: vocabulary.yaml (the case-input registry —
discovered not designed, every value source-introduced with its own ink,
also_attested rosters for the 24-book horizon); pose_case.py (interactive
menus = the registry, or key=value args; verdicts with full pedigree; a
case in unregistered vocabulary is REFUSED); tractate routing on modules
(the Mishnah's organization = the code's). Findings loop + stamp law are
standing law in the workshop (logic/findings/). Two-pass horizon recorded
in THE_WORLD.md: when Exodus law spans land, the engine goes data-driven.

Ten Mishnah case rows faced the machine: A=0 / B=7 / C=3 before any engine;
two modules compiled; 8 of 8 answered with 0 mismatches, disputes carried as
labeled dual verdicts, every verdict carrying provenance. The engine caught
one error in the exam spec itself and the Mishnah adjudicated for the
engine. The rule-engine architecture decisions are recorded in REPORT.md.

## The placement layer — PILOTED 2026-08-30, read `placement/PILOT_RESULT.md`

Vayetze was run through all four phases. **The estimate below was wrong and the
pilot says why**, so read PILOT_RESULT.md before trusting any number in this
section — it is kept as written so the correction is legible.

Three things it established:

1. **The 72% proposable figure counted PERSON names as targets.** Separating
   persons from places drops it to **21% across Genesis, 7% in Vayetze.**
2. **Machine precision on the full triple (who + relation + where) is 33%;
   recall is 29%.** This is a reading task with machine assistance, not a
   machine task with review.
3. **Placement is STATE, not a tag.** Vayetze places Jacob once and says nothing
   for the next 88 verses. With propagation, "where is Jacob at 30:25?" answers
   *Haran, placed 29:4* from a verse that names no place. The 255-verse reading
   queue is mostly not a backlog — propagation already covers it.

Revised estimate: **~12 sittings, not 6.** Phases 1, 2 and 4 are built and
reusable; phase 3, the reading, is what does not compress. Vayetze is one long
stay in one unnamed place, so travel parashiyot should score better — by how
much is not measured.

`world.sqlite` now carries a `placement` table (7 Vayetze rows) and still
reconciles green on all ten counts and the state hash.

## The original plan, kept for the record

⚠ **THE FINDING THAT MOTIVATED THIS WAS PARTLY WRONG. CORRECTED 2026-08-30**
(owner asked "did you run the test on the movement" — it had not been re-run).
Re-test: `research/MOVEMENT_TEST.py`, probe-validated, full enumeration.

~~The corpus has almost no geography... Zero movement verbs. Three of 557
events have a place-like theme.~~

**MEASURED: 91 of 557 events (16%) carry a movement verb**, across 30 distinct
labels — take (20), come (10), go_out (5), send (5), bring (4), dwell (4),
settle, pass, return, go, descend, journey, flee, pursue, go_up, tent,
bring_out. The event stream is NOT movement-free. Probable cause of the
original zero: the events table's `verb` column holds ENGLISH labels ("come",
"go_out"), and a query written against Hebrew roots or Strong's numbers returns
nothing — the same class of miss as the first verb probe, but unnoticed, so it
reached this file and the state doc.

**What survives the correction, and it is still the reason for this layer:**
the corpus records THAT someone moved, but rarely WHERE TO. The destination is
mostly not carried as a theme. So the gap is not movement — it is
**destinations**. "Jacob went down to Egypt" has the going; it lacks the Egypt.

(The second half — "3 of 557 events have a place-like theme" — is also too low:
a name-shaped scan finds ~22 candidate themes, though that filter is loose and
several are people-of-a-place rather than places. Treat both the 3 and the 22
as unreliable; only the 91 figure above is probe-validated.)

**The pilot's own numbers are unaffected** — it measured proposals from the
TEXT, not from the event stream.

Measured, and recorded in `research/VERB_REVIEW.md` (all 464 Genesis verb
lemmas enumerated from the morphology, 83 classified as location-bearing —
the enumeration is measured, the classification is a judgement):

| | verses |
|---|---|
| location-bearing verb present | **909 of 1,533 (59%)** |
| …also naming a target — machine can propose a placement | **654 (72%)** |
| …verb but no named target — needs reading | **255 (28%)** |
| verb + directional ending + proper noun (highest confidence) | 84 |

Also already free: **133 directional "toward X" tokens are tagged in the
morphology**, across 109 verses.

**The four phases:** (1) gazetteer — split 643 proper nouns into persons and
places, give places parents; bootstrap by treating anything the fold records
as agent or speaker as a person. (2) extractor — emit the 654 proposals, flag
the 255. (3) review and read, at parashah grain. (4) emit claims, gate, fold
into a `placement` table with validity ranges.

**Estimate: six to seven sittings** — but that rests on a false-positive rate
I have NOT measured. "Abraham took Sarah" has a verb and a proper noun and no
destination.

⚠ **NEXT ACTION IF THE OWNER SAYS GO: pilot ONE parashah — Vayetze.** Jacob
leaves, serves fourteen years, flees, is pursued, crosses a river: the densest
movement in the book. Run all four phases on it, measure the real proposal
accuracy, and the estimate stops being a guess. One sitting, and it de-risks
the whole thing.

**Build it BESIDE the frozen units, never inside them.** New operators would
take all 73 blocks to rev 5 and every stamp the owner gave would need
re-affirming — the gen_08 problem, seventy-three times. He stamped the book
hours before this was written.

## What the chain says about movement — do not skip this

Checked against the ledgers, not recalled. 46 Genesis ledgers carry descent
material; 58 touch journey or way. Two rows matter for the design:

- **Bereshit Rabbah 40:6, THE PAVED-WAY MACHINE** — *"go and pave the way
  before your descendants"* — **eleven matched ink-pairs, Abraham against
  Israel**: famine=famine, descended=descended, to-sojourn=to-sojourn,
  severe=severe, arrival=arrival, wealth=the silver-and-gold exit, and
  his-journeys=their-journeys. **The chain reads movement as TYPOLOGY** — the
  ancestor's route is the nation's route, matched verb for verb. This corpus
  already fired that table three times in one sweep (43:1, 45:6, 47:4).
- **Bereshit Rabbah 86:2** — Jacob was *liable to descend IN CHAINS* under the
  decree at 15:13, drawn down by his son instead. A descent recorded as a
  **commuted sentence**. The same row carries a **directional-ending census**
  (Sodom-ward, Seir-ward, Egypt-ward) — the tradition and the morphology layer
  counting the same feature.

**Design consequence:** placement is not just coordinates. The layer needs a
link between matched journeys (typology) and a way to carry WHY a placement
holds. Recording that Jacob arrived in Egypt loses that he arrived under a
decree, drawn rather than dragged.

## Owner's standing instructions as of this writing

- **This folder stays separate and self-contained.**
- **Do NOT mirror the stamps into the workshop tree.** He was asked and said no.
- **Forget torahsim / the public repo for now.** Focus here.
- The world is ultimately meant to encompass **the whole Hebrew Bible**;
  Genesis only for now, because it is the only book derived end to end. Verse
  ordering is already corpus-scoped, so nothing needs redoing when Exodus lands.
