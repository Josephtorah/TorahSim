# Resume prompt — FIFTEEN frozen (first auto-freeze); the flood prologue next · 2026-08-01

Paste the block below into the compacted session to resume exactly where we
left off. (Supersedes PROMPT_continue_gen14_2026-08-01.md — gen_14 is derived
and auto-frozen.)

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, on
**main**; last PUSHED commit 44988e0 — the gen_11/12/13 freeze wave;
gen_14 and its wave are frozen ON DISK, NOT yet committed). Local dev
server: `python3 dev_server.py` (port 8011).

**ABSOLUTE RULE (memory: chat-hebrew-glossing, owner order):** NEVER
reference Hebrew anywhere — script, transliteration, OR Hebrew-derived
jargon — without its English counterpart inline. Every time. All
outputs. The rule is also CODE: step_unit.py and the unit-page renderer
share one gloss engine — keep them in sync.

**STANDING RULE (memory: compaction-protocol):** owner compacts at
~700k tokens; keep THIS resume file current at every milestone,
unprompted; announce clean compaction points.

**STANDING RULE (memory: auto-freeze-process, owner order 2026-08-01):**
FREEZE IS AUTOMATIC — green pre-flight -> flip to frozen -> re-verify
through the real gate -> regression-run all frozen -> PYTHON RENDERING
-> re-render + re-index -> update this file. Stop for the owner ONLY on
an interpreter extension or a RED regression. Amend/narrative/triage/
COMMIT gates unchanged (owner order only).

**STANDING RULE (memory: python-rendering-layer, owner order
2026-08-01):** every frozen unit gets a GENERATED Python rendering —
`logic/py_units/<uid>.py` (shared `machine.py` mirrors run_unit.py;
per-verse comments carry translit + English gloss; assertion block
baked from the interpreter's machine truth; the generator RUNS the
file and must print "ran GREEN"). Generator: `logic/pre_logic_methods_
2026-07-28/render_unit_py.py` (no args = all frozen). The web renderer
embeds it at the BOTTOM of each unit page; dev_server's per-unit regen
runs py-then-html. Pre-Code holds: YAML canonical, Python derived —
never hand-edit a py_units file.

**State: FIFTEEN units FROZEN and green** (gen_01..gen_14 — creation
week + Eden + Cain cycle + genealogy bridge + THE BOOK OF ADAM'S LINE,
Gen 1:1-5:32 GAPLESS — plus lev_13_intake_quarantine; regression 15/15
green; FIVE consecutive extension-free derivations — run_unit.py
untouched since the gen_09 freeze). Newest:
- `gen_14_adam_line_ledger` (Gen 5:1-32, 32 steps, 365/365 words — the
  FIRST AUTO-FREEZE and the largest span yet): the corpus's first
  LEDGER-genre unit — one template, ten rows, deviations load-bearing.
  The Torah's first BOOK-word (sefer, 5:1); the header quotes frozen
  day 6 MINUS the image-word (spec-delta #1) and row one returns the
  pair SWAPPED — order, prepositions, direction (spec-delta #2;
  Onkelos deletes the image there: "who RESEMBLED him"); the die-verb's
  FIRST NARRATIVE tokens (all earlier = command/quote): Adam's 930
  lands the 2:17 word nine centuries wide of in-the-day, refrain x8;
  the SEVENTH row swaps both template verbs (lived->WALKED-with-God,
  died->WAS-NOT, einenu's first token) and ends in a TAKING with no
  destination — and the ARAMAIC'S OWN MANUSCRIPTS FORK at 5:24 (a
  bracketed negation deciding whether the LORD caused him to die;
  both variants swap TAKE for the DEATH-verb; both walk-lines buffer
  with-God -> fear-of-the-LORD); row nine births a son NAMELESS, then
  names him NOACH wrapped around a quotation of the frozen 3:17 curse
  — curser ATTRIBUTED by name, comfort no one ratifies (spec-delta
  #3) — and the comfort-root's tokens 2-3 are 6:6-7: YHWH'S REGRET
  (the fuse into the next unit); 777 (three sevens) faces the
  Cain-line's 77; 969 the maximum; 365 the solar count; two singular
  totals-verbs (5:23, 5:31); NO woman named in the chapter; the last
  row never closes (Noach 500, Shem/Cham/Yafet first tokens, total
  held at 9:29). Machine state: ZERO installs, ZERO demands (queue
  debt stays four, all inherited), 3 registry writes (GOD's own
  species-write adam_species->Adam; Shet's SECOND naming — father's,
  vs mother's frozen 4:25; Noach), 7 flags, one missing death.

**UNCOMMITTED work pile (on disk — awaiting owner's commit order):**
logic/units/gen_14_adam_line_ledger.yaml (frozen);
WATCHLIST_gen14_prospective_2026-08-01.md; FETCHLOG += 32 Onkelos
entries (Gen 5:1-32); THE PYTHON LAYER (NEW: logic/py_units/machine.py
+ 15 generated <uid>.py files, all ran GREEN; render_unit_py.py NEW;
render_unit_html.py embeds the layer + .pyblock CSS; dev_server.py
per-unit regen now runs py-then-html); ALL 15 UNIT_*.html re-rendered
with the Python section + UNIT_INDEX.html; this prompt file; scroll
data re-exported (gitignored). Protected untracked (NEVER commit):
Disclosure/, reviews/architecture/NARRATIVE_theory_of_disclosure_
intro, TEMP_return_to_main.

**Read these first, in order:**
1. `logic/units/gen_14_adam_line_ledger.yaml` — freshest frozen (the
   ledger/template format, generated boot-steps pattern, the
   spec-delta trio, the missing-death device).
2. `logic/units/gen_13_cain_line_seth.yaml` — the genealogy-bridge
   format and the quote-diff #2 notation.
3. `run_unit.py` header micro-grammar — the operator vocabulary.
4. `logic/middot_scan/WATCHLIST_gen14_prospective_2026-08-01.md` —
   the prospective pattern; the klal-class and translation-variant
   tripwires.
5. `step_unit.py` — the verse stepper (frozen only; the shared gloss
   engine).

**TASK 1 — derive gen_15 = Gen 6:1-8** (the flood prologue), same
ritual (prospective watch-list FIRST -> DB morph dump -> DB-verified
censuses -> DB trees -> Onkelos Tier-A sequential 0.5s FETCHLOG ->
full YAML -> pre-flight -> AUTO-FREEZE on green -> regression ->
PYTHON RENDERING (render_unit_py.py, must run GREEN) -> render page
(embeds it) / index -> update this file). Expected content to verify from DB
at derive time: BNEI HA-ELOHIM ("sons of God" [OPEN] — the chain's
famous fork: divine beings vs judges; Onkelos expected to render
"sons of the GREAT ones" — buffer vote); the daughters TAKEN (laqach
again — 4:19's polygamy verb generalized: "wives of ALL they chose");
"My spirit shall not ABIDE/JUDGE (yadon [OPEN] — hapax-class lexical
fork) in man... his days 120 years" (a NEW divine time-decree — first
countdown since 2:17's in-the-day; handler-frame candidate);
NEPHILIM [OPEN — name only, nothing invented]; 6:5 the evil-diagnosis
(every imagination of the heart's devisings only evil all the day —
the corpus's first total-verdict on the species; yetzer's debut —
check); 6:6 VA-YINACHEM YHWH + VA-YITATZEV el-libo — the comfort-root
(5:29's hope, tokens 2-3) become REGRET, and the GRIEF-root reaching
God's own heart (verify root family vs itzavon 3:16/3:17/5:29 —
claim carefully: related roots, distinct lemmas); 6:7 EMCHEH ("I
will WIPE") — the wipe-verb's debut (its career: the flood, the
book of life Exod 32:32-33); man-to-beast scope (the un-creation
list runs day-6 backwards — check order vs 1:24-26); 6:8 VE-NOACH
MATZA CHEN — chen ("favor/grace") FIRST TOKEN, and the letter fact:
NOACH and CHEN are the same two letters REVERSED (nun-chet /
chet-nun — hold as letter fact); "found favor in the EYES of YHWH"
— the eyes-thread (3:6, 3:7). Genre: narrative verdict-prologue —
expect TEST/verdict machinery back (the first FAIL-class total
verdict on humankind?), a possible TIME decree, and the first
DIVINE-interior EVENTs (regret, grief) — decide operator treatment
letter-honestly; NO new interpreter ops expected (sixth
extension-free candidate).

**TASK 2 — standing queue (all owner-gated):** triages owed — days
6-7, lev_13, gen_08 (Sanhedrin 56b), gen_09 (58a), gen_10 (ADRN 1;
29a), gen_11 (BR 20:12), gen_12 (Mishnah Sanhedrin 4:5), gen_13
(Rambam Avodah Zarah 1:1; BR 23), gen_14 (BR 24-25 ben-Azzai klal;
the 5:24 fork) — the debt is NINE and compounding; days 2-3
backfill; narratives since day 5 (ASK OWNER FIRST, each); PUBLIC
REPORT (owner emphasis pass); middot v2; Stage E linker; repo-tools
decision (preflight template + fetch_onkelos_span.py — the gen_14
build reused session scripts; formalizing them is still owed a
decision); gen_boot renderings (offered, not ordered).

**State notes:** dev server on 8011 may be the OLD process (restart
pending — regen chain gained render_coverage_index.py). Web:
`/units/UNIT_INDEX.html` (15 units), `/#Gen/5/24`-style deep links,
frozen badges = switch buttons. Stepper: `python3 step_unit.py
gen_14_adam_line_ledger` now works (frozen). DB snapshot
torah_grok.SNAPSHOT-main-51801ca.sqlite held (gitignored). Onkelos
cache covers Gen 1:1-5:32 + Lev 13:1-8 (gitignored; FETCHLOG is
provenance).

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
