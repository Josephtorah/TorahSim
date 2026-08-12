# SESSION LOG — 2026-08-12: chapter gate + pass-1 harvest

**Purpose:** raw process record of this session, kept for the owner's
later narrative write-up (owner request, end of session). Chronological;
owner words quoted verbatim as section anchors; decisions, mechanics,
mistakes, and numbers all kept. Findings themselves live in the scan
notes and the harvest report — this file records HOW the day went.

**The day in one line:** finished the last verse of the Exodus 21 oral
scan (chapter gate GREEN), answered the morphology question with a
discovery (the work was already done), made the sequencing call
(harvest-first), and ran pass 1 of the TANAKH RUN — 929 chapters
funneled to 57 scenes. Compaction points #22 → #23 → #24 stamped.

---

## Part 0 — carried in from before the mid-session compaction

Same calendar day, earlier context window: owner word "Do the rest of
the block" finished the block-3 scan (Exod 21:28-36, bites 11-22 + the
tanakh close; ledger 4,331 → 4,731 EXACT). Then the owner asked whether
we had enough to TEST the law code, and across two discussion turns the
TANAKH RUN was designed: compile Exod 21, sweep all 24 books for the
data it runs on, two passes (world-init, then code-run), both execution
modes (per-scene fixtures + sequential replay) with cross-validation
between them as a finding-generator. Owner: "create the folder, put a
plan doc in it, and when you are done I need to compact." →
`PLAN_tanakh_run_2026-08-12.md`, COMPACTION POINT #22, /compact.

## Part 1 — "read the tanakh_run plan and lets discuss… can you extract the data from the places in the 24 books without having to process all of the trees, morphology?"

First move after compaction: re-read the plan from disk (the stamped
record is the memory that survives; this is the compaction protocol
working as designed).

The morphology question got a better answer than hoped, found by
LOOKING before answering: `.schema` on `elijah_docket/tanakh.sqlite`
showed a `words` table with `lemma` and `morph` columns — the full
Tanakh ships pre-tagged (23,213 verses; 305,507 words; every word
carries a Strong's-style lemma + a morph code like HVqi3ms = verb, qal,
imperfect, 3ms; clitic prefixes pre-split; an INDEX on lemma). So: no
tree-parsing, no parser to build — a root sweep is one indexed SQL
query. Proved live on נגח ("gore"): 13 hits in the entire Tanakh, six
inside our own block 3, and the other seven all blessing/oracle/vision/
psalm — the plan's expected negative finding confirmed in one query,
before the harvest even started.

Also flagged in the same turn: the honest sequencing caveat (scan done
≠ code done) and the observation that pass 1 (harvest) depends only on
the scans, not the code — setting up the next owner turn.

## Part 2 — "you make the call."

Owner delegated the sequencing. Call recorded: **21:37 tail now, then
harvest-first** — plan step order becomes 1 → 5 → 2 → 3 → 4 → 6.
Rationale as stated: the harvest is what the owner actually wants to
see; it depends only on scans; the scene catalog gives the coding days
real fixtures; block-1 scenes can run early against the existing
block-1 machine. Pass 2 still waits on the assembled machine.

Delegation was read as authorization to EXECUTE step 1 (the owner had
already said "I think we have to finish a verse or two, then start on
the plan right?"), so the tail scan started the same turn without
asking again.

## Part 3 — the 21:37 tail scan (block-3b)

Mechanics (the kit pattern, unchanged from blocks 1-3):

- **Census widened, not rebuilt:** edited `law03_census.py` span from
  `BETWEEN 28 AND 36` to `28 AND 37`, reran → queue + side DB rebuilt
  for the wider span. Safe because the **ledger is the cursor**: every
  already-read ref is skipped at dump time, so widening a census never
  re-reads or double-counts. Queue resolved to 169 readable + 3 tanakh
  = 172 new rows (the prior throwaway estimate said 185+4 with 17
  dual-anchors — same 172 total, different split; the queue is the
  truth).
- **Four clips:** bite 24 (75 listings — Torah Temimah's 18-note run,
  both Mekhiltas, Mishnah/Tosefta, Bavli core, MT Theft ch.1), bite 25
  (35 — the codes: SeMaG/Chinukh/Tur CM 348, both targums, Rashi,
  Lekach Tov, Chizkuni, Shemot Rabbah), bite 26 (37 — the parshanim:
  Bahya, Abarbanel on 2 Sam 12 itself, Chatam Sofer, Meshekh Chokhmah,
  Malbim, Hirsch opener), bite 27 (22 — Hirsch's nine-part essay,
  Rasag, Yalkut). Every dump redirected to a file (standing rule after
  an earlier-session loss); oversized batches read in two parts at
  `grep -n "^=== "` listing boundaries; ledger arithmetic verified with
  `wc -l` after every clip; digest + marquee entries written to the
  notes after every bite (lean-record: read-then-record, no orphans).
- **The tanakh close:** 3 verses — Exod 22:1, Exod 22:3, and
  **2 Sam 12:6**, David's ארבעתים ("fourfold") verdict, which thereby
  became the final row of the chapter ledger on its own. Noted at the
  time as the day's best omen.
- **Landing:** ledger 4,731 → **4,903 = census target EXACT**;
  `--status` 0 readable / 0 tanakh. **EXOD 21 CHAPTER GATE GREEN —
  coverage continuous 21:1-37**, the full span of frozen unit
  exo_21_the_ordinances. Notes + census mirrored to
  `logic/law_era/scratch_mirror/`; TOP10 row updated; state doc 14th
  update + COMPACTION POINT #23.

Tail marquee headlines (details in `law03_scan_notes.md` digests
24-28): Hirsch's public-trust theory of the double (confession restores
the principle → the confession-exemption DERIVED); his dissolution of
the three agency-in-sin exceptions (liability rides personal status,
not the acting hand); the composed tariff (4/5 contains the double —
hekdesh/gentile collapse it); the golden calf paid at the ox-rate three
ways; David's fourfold pre-computed by the tradition (child, Amnon,
Tamar the dignity-unit, Absalom; no-pity = the din-rate five); gezerat
melekh ("a king's decree") vs FOUR competing derivations of the 5/4
constants; the Tur's jurisdiction decay (no fines-courts today; thief
self-sale only while Yovel runs) — which became the tanakh_run's
application_mode flags found sitting in the sources.

## Part 4 — "how many chapters total do we have for this test?" / "oh no I meant how many chapters for exodus are we testing"

Two-beat clarification, worth keeping for the narrative because the
misread produced the test's best framing line: first answer 929
chapters (the whole sweep corpus, counted live from the DB); corrected
answer **one** — Exodus 21 alone is compiled. "The machine is 1
chapter; the world is 929. The asymmetry is the point."

## Part 5 — "ok pass one harvest go"

Pass 1 executed in one run, all three channels, everything in
`logic/law_era/tanakh_run/`:

- **Format anchors first:** read a gork fixture to match the scene
  schema; checked `entity_registry.yaml` conventions — registry ends at
  Exod 21 (the world so far), so scene entities were kept as
  scene-local snake_case tokens with the join deferred to pass-2
  world-init (linked, not merged — the registry's own law).
- **Channel 3 design decision (the day's best trick):** instead of
  hand-picking roots, the lemma list was DERIVED FROM THE STATUTE —
  pull every lemma occurring in Exod 21:1-37 (+22:1-3 border), sweep
  exhaustively every one with whole-Tanakh frequency ≤ 90. 31 lemmas +
  5 surface patterns (מות יומת "he shall surely die", ארבעתים
  "fourfold", שבעתים "sevenfold", אין לו דמים "no blood-claim", דמיו בו
  "his blood on him") → ~700 candidate verses. Nothing operative could
  be missed by MY choice of roots — the statute chose.
- **Channel 1 surprise + fix:** `export_links` category='Tanakh' also
  holds commentaries-ON-Tanakh (Sefaria's category tree), so the first
  query returned 3,826 rows of Abarbanel etc. Fix: filter through
  `tanakh_ref()` to true verse refs → **70 crossrefs**, and they were
  the right seed (both patch chapters, both refuge chapters, the three
  narrative flagships, Judah's substitute-offer anchored at the injury
  law, Rahab's נפשנו תחתיכם "our life in place of yours" at the talion
  clause). Row 6 handed the catalog its epigraph: Exod 21:1 ↔ Ps 105:7
  בכל הארץ משפטיו ("His judgments are in all the earth").
- **Channel 2:** grep-mined the law01/02 notes mirrors for narrative
  refs + carried the block-3/tail digests. Confirmed all nine plan
  flagships; added Zech 11's thirty, the calf-tariff triple, 1 Kgs
  20:35's strike-refuser, Job 31's slave manifesto, and SeMaG's pointer
  to the borrowed axe (2 Kgs 6:5, והוא שאול "and it was borrowed!").
- **Homograph discipline** (kept honest in the report): כפר as
  village/henna/pitch excluded; שבעתים at 2 Sam 21:9 = "the seven of
  them"; גף at Prov 9:3 = "heights"; and one real slip — Strong's 4835
  (מרוצה "oppression", Jer 22:17) initially glossed as the awl; the
  real awl is 4836 (2 hits: Exod 21:6 + Deut 15:17, exactly the statute
  and its patch). Fixed in the script, rerun. Even the slip paid: Jer
  22:17 led to Jehoiakim's gratis-labor scene.
- **Synthesis:** `scene_catalog_tanakh_run_2026-08-12.json` — **57
  scenes** (21 P0 / 22 P1 / 14 P2), 157 refs, 50 chronology-keyed for
  the replay fold + 7 achronic doctrine scenes, 5 FORWARD-touching
  stubs. Modes: binding 17, prophetic_figurative 14, doctrine 7,
  pre_sinai_typology 6, foreign_comparative 5, lexicon 4, patch 3,
  gen9_noahide 1. Report: `HARVEST_PASS1_REPORT_2026-08-12.md`. Plan
  steps 1+5 stamped DONE; state doc 15th update + COMPACTION POINT #24.

New-find headlines (beyond the nine planned): Achan's oxen stoned WITH
him (Josh 7 — cherem jurisdiction inverting 21:28); Sinai's perimeter
running the ox-stoning protocol before the statute is spoken (Exod
19:12-13); Samuel's clearance audit in the statute's own nouns (1 Sam
12:3 — whose ox, whose kofer; Amos 5:12 the same audit failed); Jer
2:34 citing the burglar clause's LIMITS as indictment (the מחתרת
lemma's only non-statute hit); Zech 5's flying scroll = heavenly
enforcement of the theft-parashah's pair exactly where the Tur's
jurisdiction-decay leaves courts dark; Esther pleading the sale-SCALE;
Yehosheba's rescue-theft of Joash; the goblet plant's graded verdicts.
Negative finding now mechanical: 13 נגח hits total, zero narrative
ox-gores-man.

## Errors and fixes (honest ledger, this session)

1. Channel-1 category assumption — 'Tanakh' includes commentaries;
   caught by looking at the output, fixed with the resolver filter.
2. Strong's 4835/4836 awl mix-up — caught because the "awl" hit list
   looked wrong (Jer 22:17 is not an awl verse); fixed + rerun.
3. Earlier estimate vs queue (185+4 vs 169+3, same 172 total) — the
   census queue treated as truth, estimate noted and discarded.
4. Registry membership NOT claimed for monarchy-era figures — checked
   the registry first instead of assuming; join deferred honestly.

## Craft notes for the narrative (what made the day work)

- **The ledger-as-cursor pattern** let the census span widen with zero
  re-read risk — the same idempotence that let the whole 4,903-row
  chapter accumulate across four scans without one orphan row.
- **Look before answering:** both discussion questions (morphology,
  chapter counts) were answered by querying the corpus live, not from
  memory — and the morphology answer changed the plan's cost model.
- **Derive the sweep from the object of study** (statute-derived lemma
  list) — the method removes the researcher's blind spots by
  construction.
- **The stamped record as memory:** compaction hit mid-day; the plan
  doc, state doc, and notes mirrors carried everything across; the
  session resumed from disk without a step lost. Three compaction
  points stamped in one day (#22, #23, #24), each at a gate.
- **Owner-word cadence:** every phase started on an explicit owner
  word ("do the rest", "you make the call", "harvest go"), and the one
  delegation was recorded as a call with rationale before execution.

## Where everything lives

- Scan notes (27 digests + 2 closes + ~120 marquee):
  `logic/law_era/scratch_mirror/law03_scan_notes.md` (mirror; live copy
  in scratchpad session 4ca32657…)
- Ledger: `logic/oral_audit/ledgers/Exod_21.jsonl` — 4,903 rows
- The test folder: `logic/law_era/tanakh_run/` — plan, harvest tool,
  two channel JSONs, scene catalog (57), harvest report, this log
- State doc (the authority):
  `logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md`
  — updates 13-15, compaction points #22-#24
- Block list: `logic/law_era/TOP10_LAW_BLOCKS.md` (block-3 row carries
  the tail + gate)

**State at the pass-1 milestone** (superseded — the day continued):
chapter gate GREEN, pass 1 done, next move owner-paced — block-3 coding
day was the front of the queue. Everything above was then UNCOMMITTED.

---
---

# THE SECOND HALF — coding days and the assembly
*(appended per owner word "add more narrative to the log file so we can
later generate a how to for my learning benefit" — this half is written
deliberately as process-narrative: every phase carries its recipe.)*

**The second half in one line:** the three block machines got coded
(block 3, then block 2), the whole day's work was committed and pushed
on owner word, and the chapter was ASSEMBLED into one machine — Exodus
21:1-37 running as a single program with a persistent world, seven
cross-block seam laws, and a 60-edge dependency proof. Compaction
points #25 → #26 → #27.

## Part 6 — "ok continue next task": the block-3 coding day

The first CODING day of the law era's second phase, and the day the
repeatable recipe crystallized. What a "coding day" is: the scan
produced a few thousand ledger rows and a notes file full of digests;
the coding day compresses that into (a) a CLAIMS MANIFEST — the
strongest multi-witnessed legal claims, each with its sources — and
(b) a MACHINE — a runnable Python file where every rule carries its
claim-ID, every claim traces to named sources, and an assert battery
proves the rules compose.

How block 3 went, concretely:

1. **Read the spec.** The scan notes' marquee index (the running list
   of the strongest finds, maintained bite by bite during the scan) was
   read IN FULL as the coding spec. The digests hold the details; the
   marquee is the map.
2. **Distill the manifest.** 28 claims (L28-01..L37-06 + two L0 system
   claims) under the lean-record rule: only multi-witnessed or
   marquee-grade rows, each claim one sentence of law + one line of
   sources pointing back into the digests.
3. **Copy the architecture, not the content.** The block-1 machine
   (from the previous coding day) supplied the shape: constants with
   claim-tags, case functions returning dict-verdicts with the claim-ID
   in the note, a run() that asserts the tradition's own worked
   examples, and the DEPENDS table + verify_dependencies() that checks
   every declared cross-verse edge against the frozen corpus in
   torah_grok.sqlite.
4. **Code the law as state machines where the law IS one.** Block 3's
   heart: the תם→מועד ("innocent"→"forewarned") escalation with
   hysteresis (three gorings on three days vest the state; ONE clean
   petting day reverts it), context-indexed (Sabbath-only forewarning,
   per-species). The sources describe a state machine in words; the
   coding day just writes it down.
5. **Run.** All asserts green FIRST run; dependency proof: 14 edges,
   6 resolved into frozen units (Gen 9:5's beast-answerability; the
   Joseph pit), 8 forward — three of them (Zech 11:12, 2 Sam 12:6,
   1 Kgs 20:39) being tanakh-run scene verses, now formal machine
   demands. The test plan and the derivation line converged on the
   same verses from two directions — logged at the time as the day's
   structural rhyme.
6. **Stamp.** TOP10 row, plan-doc step 2 (with the PLACEMENT ruling —
   owner asked "should we have put the block 3 results in the tanakh
   folder": answer NO, machines/manifests live in the law-era line
   because they head for the frozen layer; tanakh_run/ only CONSUMES),
   state doc 16th update, COMPACTION POINT #25. Then owner: "are you
   ready for compact" → yes → /compact.

## Part 7 — "commit and push": the commit ritual

First owner word after compaction resumed the session. The ritual, as
it has settled:

1. `git status --porcelain` FIRST — never stage blind.
2. Stage the day's files EXPLICITLY by path; the standing exclusions
   (elijah_docket submodule, DISPOSABLE_scan/, the grok-mockups
   (UI-sketch) folder, open_ledger/, and the still-untracked
   logic/gork/) stay out without
   needing .gitignore gymnastics.
3. One commit for the day's substance with a story-shaped message
   (three milestones, numbered), the standing trailer, and push.
4. THEN the stamp commit: write the commit's own hash into the state
   doc as a new ★ entry ("everything from updates 14-16 landed in
   ce0deeb") and commit that one-liner separately. The repo's history
   shows the pattern: every milestone commit is followed by its
   state-doc stamp commit. The record records itself being recorded.

Result: `ce0deeb` (15 files, +8,963 lines) + `20f192e` (the stamp).

## Part 8 — "block 2 go": the biggest block's coding day

Block 2 (Exod 21:12-27, homicide & injury) was the largest scan (1,639
rows, 36 digests, a 4,260-line notes file) and became the largest
manifest (43 claims) and machine (~14 case engines). Same recipe as
Part 6, with the day's own lessons:

- **Read the WHOLE spec, in chunks.** The notes file exceeded the
  single-read limit; it was mapped first (`grep -n` on digest headers),
  then read completely in five slices. Lean-record applies to what gets
  WRITTEN, never to what gets READ — the full-inversion law's spirit
  carries into the coding day.
- **Check dependency coverage BEFORE declaring edges.** A quick SQL
  probe against the frozen-units table tested every candidate back-edge
  first. Two landed that were not planned: Gen 42:38 (Jacob's פן
  יקראנו אסון "lest calamity befall him" — the word the law uses to
  weld Heaven's docket to the court's) resolves into
  gen_65_first_descent, and Gen 44:33 (Judah's ישב נא עבדך תחת הנער
  "let your servant remain IN PLACE OF the lad" — the tachat
  substitution-idiom offered in person) resolves into
  gen_67_cup_and_surety. Lesson: probing the corpus finds inheritance
  the plan didn't know about.
- **Machloket is DATA, not a bug.** Where the tradition preserves a
  live fork (transferred intent: the sages vs Rebbi; the altar-vs-crown
  interface: the GRA vs the Netziv), the machine returns the fork
  itself as the verdict object. A machine that silently picked a side
  would be falsifying its witness layer.
- **One assert came up RED on first run** — the shogeg five-heads test
  passed contradictory inputs (an unintentional injurer flagged as
  intending the shame). The failing assert was doing its job: the test
  was wrong, not the law; fixed the test, green. Kept honestly in this
  ledger because "green first run" on block 3 was luck as well as
  method.
- **Match the manifest FORMAT to its siblings.** First write wrapped
  the claims in a metadata object; the block-1/3 manifests are raw
  JSON arrays. Checked, flattened, moved on. Format drift between
  sibling artifacts is a tax on every later consumer.
- **Run gloss_lint EARLY, treat it as a gate.** 26 flags on first
  lint (Hebrew spans and Hebrew-derived jargon without an English
  counterpart within the lint's 90-character window). All fixed — 13
  in the manifest, 4 in the machine — plus one lesson about the tool:
  an ellipsis ("...") between a Hebrew word and its gloss BREAKS the
  lint's window (the regex stops at periods), so the gloss must hug
  its word. Zero flags after; the absolute Hebrew-glossing rule is
  machine-checked, not honor-system.
- **Stamps:** TOP10 (block-2 row: ALL THREE BLOCKS CODED), plan step 3,
  state doc 18th update, COMPACTION POINT #26.

## Part 9 — two owner questions, kept because a how-to needs the WHY

**"what is chapter assembly"** — answered before building it, and the
answer is the design doc in miniature: three self-contained block
drafts become ONE machine by (1) a shared persistent runtime (the
statute-0 forum of 21:1 carrying slave clocks, ox registries, standing
verdicts — the state layer replay mode needs), (2) the cross-block
seams becoming internal law (rules whose two ends live in different
blocks of the same chapter), (3) one merged dependency table where
edges pointing INSIDE the chapter reclassify as self-supplied, and
(4) chapter-level asserts for laws that only exist ACROSS blocks.

**"and this will prove the inheritance and dependancies and how the
hebrew bible is interconnected right?"** — the honest scope answer,
recorded verbatim in spirit: YES in the mechanical sense — inheritance
= machine-verified backward edges into the frozen corpus (the assert
fails if the source is missing); dependency = the forward-demand
ledger (every claimed connection is RESOLVED, OPEN, or fails loudly);
interconnection = pass 2's execution test (does the rest of the Tanakh
RUN on this chapter's code — CONFIRM / DIVERGE / NO-VERDICT per
scene). NOT proven: authorship, theology — the model stays stamped
experimental. A DIVERGE is a finding, not an embarrassment; the
falsifiability is what makes the CONFIRMs worth something.

## Part 10 — "ok contiue to next step": the chapter assembly

Built in one pass, green on the first execution. The design decisions,
each a how-to point:

1. **Import the blocks UNCHANGED.** The assembly file loads the three
   drafts as modules (importlib against the sibling files) and adds
   layers on top. Zero edits to proven code — if assembly required
   touching a block, the block's API was wrong, not the assembly.
2. **The World.** A class holding `runtime` (block 1's statute-0 dict:
   ordained forum, gender parity, promulgation), a single `day` clock,
   slave records, ox records, and `standing_verdicts`. Events are thin
   methods delegating to block functions but stamping WORLD time — an
   ox vests מועד ("forewarned") on world-days, a slave's six-year term
   expires on the same clock. Verdicts are STATE-WRITES: condemn()
   appends a standing verdict (the benefit-ban rides it, per Keritot
   6:2), execute() spends it. `snapshot()` returns the read-model the
   web app's timeline scrubber will render.
3. **Seven seam laws, asserted.** The chapter-only laws: BK 8:2 (man
   pays five heads, the ox pays damage alone); the forewarned-template
   isomorphism (man is BORN mu'ad — the ox must acquire the state);
   the slave victim's two tracks (master → sword; ox → the flat 30);
   both legs of BK 3:10's chiasmus (the master's blow frees the
   slave's eye, his ox's blow frees no one; the ox pays the wounded
   parent, the son is capital with payment absorbed); Rav Ashi's
   תחת↔תחת ("in place of" ↔ "in place of") anchor — block 2's
   eye-for-eye money proof leans on 21:36, a block-3 verse, so inside
   the assembled chapter the proof-anchor is SELF-SUPPLIED; and
   statute-0's gender parity instantiated in all three blocks.
4. **The merged proof.** 60 edges from the three DEPENDS tables:
   2 reclassified INTERNAL (the 21:11 kim-leih seam, the 21:37
   tariff verse — this is assembly's signature move: a dependency on
   the frozen v1 unit becomes self-supply), 31 RESOLVED across 28
   unique verses in 17 frozen units, 27 FORWARD across 26 open verses
   — the chapter's official demand ledger, Lev 25 to Zech 11:12. One
   surprise resolution surfaced by the merge: block 1's shifchah edge
   lands in lev_19_holiness_duty_ledger (a frozen Leviticus unit not
   previously on the map).
5. **Gates:** all green first run; gloss_lint 0 flags. Stamps: plan
   step 4, TOP10 assembly note, state doc 19th update, COMPACTION
   POINT #27. The v2 FREEZE was NOT taken — freeze runs only on
   explicit owner word, and none was given; the assembly stops at the
   draft line deliberately.

## THE RECIPES (the how-to distilled)

**The coding-day recipe** (ran three times: blocks 1, 3, 2):
1. Read the scan notes COMPLETELY (marquee index + digests) — the spec
   is the record, not memory.
2. Distill the claims manifest: multi-witnessed rows only, one
   sentence of law + sources per claim, IDs keyed to verses; match the
   sibling manifests' format exactly.
3. Probe the frozen corpus for candidate dependency edges BEFORE
   declaring them.
4. Build the machine on the established architecture: claim-tagged
   constants → case functions returning verdict-dicts → run() assert
   battery using the tradition's own worked examples → DEPENDS +
   verify_dependencies().
5. Encode live machloket as returned data, never as a silent choice.
6. Run; fix; run. A red assert is information — check the TEST before
   the law.
7. gloss_lint both files to zero flags (Hebrew never without inline
   English; the gloss hugs its word).
8. Stamp everything (block list, plan doc, state doc + compaction
   point) BEFORE reporting done.

**The assembly recipe** (ran once, chapter exo_21):
1. Import the proven parts unchanged.
2. Add the shared state runtime with ONE clock; make verdicts
   state-writes; expose a snapshot read-model for the next consumer.
3. Find the seams — every rule whose proof or counterpart lives in
   another block — and assert each at chapter level.
4. Merge the dependency tables; reclassify in-span edges INTERNAL;
   re-verify everything external against the corpus.
5. Same gates (asserts + gloss_lint), same stamps, and STOP at the
   draft line — freeze is the owner's word, not the builder's.

## Errors and fixes (second-half ledger)

5. Block-2 shogeg assert red on first run — contradictory test inputs;
   fixed the test, not the law.
6. Manifest format drift (metadata wrapper vs raw array) — caught by
   diffing against the block-3 manifest, flattened.
7. gloss_lint 26 → 0: the ellipsis-breaks-the-window lesson; glosses
   now hug their Hebrew.
8. First DB probe hit the wrong path (logic/torah_grok.sqlite vs the
   repo root) — the block-3 resolver's relative path was the documented
   truth; read the existing code before guessing paths.

## Where everything lives (second-half additions)

- Block-2 claims: `logic/oral_audit/manifests/law02_exo_21_12_27_claims.json` (43)
- Block-2 machine: `logic/law_era/exo_21_v2_block2_DRAFT.py`
- THE CHAPTER: `logic/law_era/exo_21_v2_DRAFT.py` (World + seams +
  60-edge proof; blocks imported unchanged)
- Commits: `ce0deeb` (the first half's work) + `20f192e` (state-doc
  stamp); the second half's work UNCOMMITTED as of this writing
- State doc updates 16-19, compaction points #25-#27

**Session end state (second half):** all three blocks coded, chapter
assembled and green, freeze awaiting owner word, pass-2 web app the
front of the queue. Uncommitted: block-2 manifest + machine, the
assembly, TOP10 + plan + state-doc stamps, and this log's second half.
