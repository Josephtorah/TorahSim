# Resume prompt — SIXTEEN frozen; the ark spec next · 2026-08-01

Paste the block below into the compacted session to resume exactly where we
left off. (Supersedes PROMPT_continue_gen15_2026-08-01.md — gen_15 is derived
and auto-frozen.)

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, on
**main**; last PUSHED commit 44988e0 — the gen_11/12/13 freeze wave;
gen_14, gen_15, and the whole PYTHON LAYER are frozen/built ON DISK, NOT
yet committed). Local dev server: `python3 dev_server.py` (port 8011).

**ABSOLUTE RULE (memory: chat-hebrew-glossing, owner order):** NEVER
reference Hebrew anywhere — script, transliteration, OR Hebrew-derived
jargon — without its English counterpart inline. Every time. All
outputs. The rule is CODE in two places: the gloss engine (step_unit.py
+ web renderer) and the generated py_units comments.

**STANDING RULE (memory: compaction-protocol):** owner compacts at
~700k tokens; keep THIS resume file current at every milestone,
unprompted; announce clean compaction points.

**STANDING RULE (memory: auto-freeze-process):** FREEZE IS AUTOMATIC —
green pre-flight -> flip -> re-verify -> regression-run all frozen ->
PYTHON RENDERING (must run GREEN) -> render page (embeds it) +
re-index -> update this file. Stop ONLY on interpreter extension or
RED regression. Amend/narrative/triage/COMMIT gates: owner order only.

**STANDING RULE (memory: python-rendering-layer):** every frozen unit
gets a generated `logic/py_units/<uid>.py` (shared machine.py mirrors
run_unit.py; glossed verse comments; machine-truth assertion block;
generator runs it). Embedded at the BOTTOM of each unit page. YAML
canonical; never hand-edit py_units.

**State: SIXTEEN units FROZEN and green** (gen_01..gen_15 — Gen
1:1-6:8 GAPLESS — plus lev_13; regression 16/16; SIX consecutive
extension-free derivations). Newest:
- `gen_15_flood_prologue` (Gen 6:1-8, auto-freeze #2): the week's
  inspection formula STOLEN at 6:2 (creature subjects, daughters as
  object, taking as sequel — creature-run TEST #2 + spec-delta;
  BACHAR/choice debuts as taking-from-ALL; bnei-elohim [OPEN],
  Onkelos votes "sons of the GREAT ONES") and INVERTED at 6:5
  (very-good -> great-evil, spec-delta #2; YETZER debuts, token 2 =
  8:21 bookend; MACHASHAVAH debuts -> Tabernacle design-word); the
  120-year decree with THREE forks open (yadon/be-shagam/
  cap-vs-countdown; Onkelos rebuilds as repentance window — the 4:7
  device); Nephilim = name+time+title, NOTHING invented (3 Torah
  tokens); the corpus's FIRST DIVINE-INTERIOR EVENTS — regret
  (nacham token 2: gen_14's fuse detonated) + grief (ATZAV first
  token = the ROOT of the Eden sentences' toil-noun, reaching HIS
  heart; heart-pair 6:5/6:6) — both DELETED by Onkelos ("turned in
  His Word to break their strength"); the WIPE-RESOLVE pushed as
  CMD-US?(machah(...)) — I-WILL-MAKE's mood grammar (gen_09
  precedent) now carrying UN-creation, popped by NOTHING (execution
  = 7:23, outside): queue debt FIVE; and the five-word
  counterweight: CHEN first token, Noach/chen letter-reversal, the
  find-verb arc, the eyes-thread — favor and the open wipe BOTH
  survive the unit. ZERO installs, ZERO registry writes (a first),
  3 flags. Machine truth matches state_after exactly.

**KNOWN COSMETIC DEFECT (owner decision pending):** frozen gen_14's
32 boot-step `he:` lines are UNPOINTED (consonants only — a
generator character-class slip; content identical, logic/coverage/
scenarios unaffected; gen_15 fixed the class with explicit
escapes). Fixing = amend-gated: on owner order, regenerate the he:
lines pointed, re-verify, re-render.

**UNCOMMITTED work pile (on disk — awaiting owner's commit order):**
gen_14 + gen_15 YAMLs (frozen); WATCHLIST_gen14/gen15; FETCHLOG +=
40 Onkelos entries (Gen 5 x32, Gen 6:1-8 x8); THE PYTHON LAYER
(logic/py_units/machine.py + 16 generated files; render_unit_py.py;
render_unit_html.py embeds + .pyblock CSS; dev_server.py regen =
py-then-html); ALL 16 UNIT_*.html with the Python section +
UNIT_INDEX.html (16 units); PROMPT_continue_gen15 + this file;
scroll data re-exported (gitignored). Protected untracked (NEVER
commit): Disclosure/, reviews/architecture/NARRATIVE_theory_of_
disclosure_intro, TEMP_return_to_main.

**Read these first, in order:**
1. `logic/units/gen_15_flood_prologue.yaml` — freshest frozen (the
   verdict-prologue format, the CMD-US? un-creation push, the
   two spec-deltas against week text).
2. `logic/units/gen_14_adam_line_ledger.yaml` — the ledger/template
   format.
3. `run_unit.py` header micro-grammar + `logic/py_units/machine.py`
   (the friendly mirror).
4. `logic/middot_scan/WATCHLIST_gen15_prospective_2026-08-01.md`.
5. `logic/pre_logic_methods_2026-07-28/render_unit_py.py` — the
   Python-layer generator (no args = all frozen).

**TASK 1 — derive gen_16 = Gen 6:9-22** (Noach's line and the ark
spec), same ritual (watch-list FIRST -> DB morph dump -> censuses ->
DB trees -> Onkelos Tier-A 0.5s FETCHLOG -> YAML -> pre-flight ->
AUTO-FREEZE -> regression -> PYTHON RENDERING -> render/index ->
update this file). Expected content to verify from DB at derive
time: toledot header #3 in our spans (6:9 — SECTION); TZADDIK
("righteous") FIRST TOKEN on Noach + TAMIM ("blameless") + the
walk-verb again (hithalekh et-ha-Elohim — Chanokh's verb, token 4);
the SHACHAT root cluster (6:11-13, 17): the SAME root for the
corruption (nishchatah/hishchit) and the destruction (mashchitam,
le-shachet) — the punishment word IS the crime word [expect x5-6
tokens: census]; CHAMAS ("violence") debut x2; ketz kol-basar ("the
END of all flesh" — qetz token 2 after 4:3's mi-qetz?); TEVAH
("ark") FIRST TOKEN — its ONLY other Torah context is Moses'
basket (Exod 2:3-5): the two rescues share one word; GOFER wood
(Torah hapax); KOFER ("pitch" — the KAPHAR/atonement root's debut
as waterproofing [letter fact!]); the DIMENSIONS (300 x 50 x 30
cubits — the corpus's first BUILD SPEC: amah "cubit" first tokens);
TZOHAR [OPEN — hapax: window/light]; MABUL ("flood") first token;
BRIT ("covenant") FIRST TOKEN at 6:18 — va-hakimoti et-briti
(weqatal promise, TIR-029; established at 9:9ff — promised to one
man before the un-creation); two-of-all + male-female (1:27's pair
in the cargo manifest); the food clause; and 6:22 THE FIRST
COMPLIANCE RECEIPT: va-yaas Noach ke-khol asher tzivah oto Elohim
("Noach did according to ALL that God commanded") — the
ka-asher-tzivah formula whose career is the TABERNACLE build
refrain (Exod 39-40): expect the ark commands as DECLARE
LET(aseh...) imperatives (TIR-027, divine issuer) POPPED by the
6:22 receipt — the corpus's first divine-imperative-to-human with
execution receipt (gen_09's echo-class: command verb returned in
the compliance line). Genre: BUILD-SPEC inside narrative — the
lev_13/gen_08 law kit + gen_09 receipt mechanics together. NO new
interpreter ops expected (seventh extension-free candidate).

**TASK 2 — standing queue (all owner-gated):** triages owed — days
6-7, lev_13, gen_08 (Sanhedrin 56b), gen_09 (58a), gen_10 (ADRN 1;
29a), gen_11 (BR 20:12), gen_12 (Mishnah Sanhedrin 4:5), gen_13
(Rambam AZ 1:1; BR 23), gen_14 (BR 24-25 klal; the 5:24 fork),
gen_15 (BR 26 bnei-elohim; the 6:3 rebuild) — TEN owed and
compounding; days 2-3 backfill; narratives since day 5 (ASK OWNER
FIRST, each); PUBLIC REPORT; middot v2; Stage E linker; repo-tools
decision; the gen_14 pointing fix (above); gen_boot renderings
(offered, not ordered).

**State notes:** dev server on 8011 may be the OLD process (restart
pending — regen chain gained render_coverage_index.py + the
py-then-html unit regen). Web: `/units/UNIT_INDEX.html` (16),
`/#Gen/6/8`-style deep links, frozen badges = switch buttons, the
Python rendering at the BOTTOM of every unit page. Stepper:
`python3 step_unit.py gen_15_flood_prologue`. Onkelos cache: Gen
1:1-6:8 + Lev 13:1-8 (gitignored; FETCHLOG is provenance). DB
snapshot torah_grok.SNAPSHOT-main-51801ca.sqlite held (gitignored).

**Standing rules (non-negotiable):** Pre-Code (logic hand-authored
in frozen YAML; code only interprets; flags never auto-resolve;
dual-track, never merge). FREEZE: AUTOMATIC on green pre-flight;
amend/narrative/triage/commit gates: owner order only (narratives:
ASK FIRST each time). Hebrew ALWAYS glossed in English — absolute,
everywhere, forever. Oral: named location only; verified from local
corpus; tier per the APPROVED provenance register (material =
chain_primary only); machine never derives law (ein adam dan
me-atzmo — "one may not derive on his own"). Sefaria: sequential,
0.5s, small ranges, EVERY fetch logged in Data/FETCHLOG.md. Commit
trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
Repo PRIVATE (Sefaria licensing). gh account Josephtorah.
Disclosure/ + reviews/architecture/NARRATIVE_theory_of_disclosure_
intro are the owner's own docs — NEVER commit them.
