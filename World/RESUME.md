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

**Genesis, whole:** 97 units · 2,074 verses · 278 entities · 1,809 facts ·
557 events · 740 relations · 341 demands (191 open) · 905 standing ·
hash `8b8fff1fa28953af`.

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
