# Resume prompt — SEVENTEEN frozen; the boarding next · 2026-08-01

Paste the block below into the compacted session to resume exactly where we
left off. (Supersedes PROMPT_continue_gen15; gen_15 AND gen_16 are derived
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

**State: SEVENTEEN units FROZEN and green** (gen_01..gen_16 — Gen
1:1-6:22 GAPLESS — plus lev_13; regression 17/17; SEVEN consecutive
extension-free derivations). Newest first:
- `gen_16_ark_spec` (Gen 6:9-22, auto-freeze #3): THE FIRST
  FULLY-SETTLED DIVINE COMMAND CYCLE — two imperatives (aseh 6:14,
  qach 6:21: TIR-027's first divine imperative-mood commands to a
  named individual) pushed and BOTH POPPED by 6:22's compliance
  formula (tzavah arc: 2:16 violated -> 3:11/17 indicted -> 6:22
  OBEYED -> 7:5/9/16 refrain -> Tabernacle); WORLD += tevah — the
  second human build, first RECEIPTED COMPLETE (vs gen_13's
  participle city); the SHACHAT root x5 in-span (crime-verb =
  sentence-verb; tokens 6-7 = the 9:11/15 never-again); the THIRD
  week-formula mutation (1:31 behold-very-good -> behold-corrupted,
  spec-delta); TEVAH = the two-rescues word (26 Gen tokens + Moses'
  basket ONLY); the kaphar/atonement root debuts as PITCH; first
  cubit blueprint (300x50x30; the flood measured in the same unit
  at 7:20); hapaxes held open (gofer, tzohar); BRIT's FIRST TOKEN
  (weqatal promise to one man; ratification = Gen 9); the manifest
  as creation-in-miniature (by-kind x3, male-female, the food-grant
  word), SELF-LOADING; sin's door-word (4:7 petach) as the ark's
  entrance. Onkelos: chamas -> ROBBERY (Sanhedrin 108a's doctrine
  as lexicon), corruption narrowed to "flesh OF MAN", hapaxes
  decided (light/cedar), Chanokh's fear-buffer on Noach's walk.
  Machine: 1 install, 0 registry writes, 0 tests, 2 flags, SPECS
  EMPTY BY SETTLEMENT.
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
gen_14 + gen_15 + gen_16 YAMLs (frozen); WATCHLIST_gen14/15/16;
FETCHLOG += 54 Onkelos entries (Gen 5 x32, 6:1-8 x8, 6:9-22 x14);
THE PYTHON LAYER (machine.py + 17 generated files;
render_unit_py.py; render_unit_html.py embeds + .pyblock CSS;
dev_server.py regen = py-then-html); ALL 17 UNIT_*.html with the
Python section + UNIT_INDEX.html (17 units); the three PROMPT files;
scroll data re-exported (gitignored). Protected untracked (NEVER
commit): Disclosure/, reviews/architecture/NARRATIVE_theory_of_
disclosure_intro, TEMP_return_to_main.

**Read these first, in order:**
1. `logic/units/gen_16_ark_spec.yaml` — freshest frozen (the
   build-spec format, the two-demand push/pop cycle, RESULT
   mechanics).
2. `logic/units/gen_15_flood_prologue.yaml` — the verdict-prologue
   format and the open CMD-US? un-creation push.
3. `run_unit.py` header micro-grammar + `logic/py_units/machine.py`
   (the friendly mirror).
4. `logic/middot_scan/WATCHLIST_gen15_prospective_2026-08-01.md`.
5. `logic/pre_logic_methods_2026-07-28/render_unit_py.py` — the
   Python-layer generator (no args = all frozen).

**TASK 1 — derive gen_17 = Gen 7:1-16** (the boarding), same ritual
(watch-list FIRST -> DB morph dump -> censuses -> DB trees -> Onkelos
Tier-A 0.5s FETCHLOG -> YAML -> pre-flight -> AUTO-FREEZE ->
regression -> PYTHON RENDERING -> render/index -> update this file).
Expected content to verify from DB at derive time: 7:1 BO el-ha-tevah
("COME into the ark" — imperative #3 to Noach; the come-verb, not
enter) + "for YOU have I seen TZADDIK before Me" — tzaddik token 2,
now SECOND PERSON (6:9's narrator-praise become divine address; the
letter's only direct you-are-righteous); SEVEN PAIRS of the CLEAN
(TAHOR — the pure-word's FIRST TOKEN: the law's central adjective
debuts in cargo arithmetic BEFORE any purity law exists [OPEN: how
does Noach know clean from unclean — the chain's question,
named-only]) vs two of the not-clean; "od shivat yamim" — a 7-day
countdown stacked on the 120; 40 days/nights announced; 7:4 "I will
wipe" (machah token 2 — the countdown repeats the resolve, YIQUM
["every living substance"] debut); 7:5 COMPLIANCE REFRAIN #2 (va-yaas
Noach ke-khol asher tzivahu YHWH — now with YHWH; expect a second
settled cycle: the boarding commands pushed and popped); 7:6 Noach
600; 7:8-9 "two by two came" — SELF-LOADING CONFIRMED (bau — they
CAME; refrain #3 "as Elohim commanded Noach"); 7:11 THE CORPUS'S
FIRST FULL CALENDAR DATE (year 600 of Noach's life, month 2, day 17)
— and the un-creation's plumbing: NIVKEU kol MAYENOT TEHOM rabbah
(the DEEP — 1:2's tehom — bursts from below) + ARUBOT ha-shamayim
niftachu (heaven's windows open from above): day 2's separation run
BACKWARD [the un-creation thread's biggest structural claim —
DB-verify tehom/arubah tokens]; 7:12 rain 40 day/night; 7:13 BE-ETZEM
HA-YOM HA-ZEH ("on this very day" — the phrase's debut? census; its
career: 17:23 circumcision, Exod 12:41 the exodus, Deut 32:48 Moses'
ascent — the corpus's solemn-date formula); 7:14-15 the full manifest
boards (by-kind list expanded, kol tzippor kol kanaf); 7:16 the
boarders doubled male-female "as ELOHIM commanded" + VA-YISGOR YHWH
BAADO ("and YHWH SHUT HIM IN" — the door-closer: sagar's token
[2:21's flesh-closing the only prior!]; the name SWITCH inside one
verse: Elohim commands, YHWH shuts [letter fact]; Onkelos expected
to buffer the shutting). Genre: execution narrative — the gen_16
spec run as boarding log with compliance refrains. NO new
interpreter ops expected (eighth extension-free candidate).

**TASK 2 — standing queue (all owner-gated):** triages owed — days
6-7, lev_13, gen_08 (Sanhedrin 56b), gen_09 (58a), gen_10 (ADRN 1;
29a), gen_11 (BR 20:12), gen_12 (Mishnah Sanhedrin 4:5), gen_13
(Rambam AZ 1:1; BR 23), gen_14 (BR 24-25 klal; the 5:24 fork),
gen_15 (BR 26 bnei-elohim; the 6:3 rebuild), gen_16 (Sanhedrin
108a robbery-as-lexicon; the be-dorotav diyyuk; the tzohar fork) —
ELEVEN owed and compounding; days 2-3 backfill; narratives since day 5 (ASK OWNER
FIRST, each); PUBLIC REPORT; middot v2; Stage E linker; repo-tools
decision; the gen_14 pointing fix (above); gen_boot renderings
(offered, not ordered).

**State notes:** dev server on 8011 may be the OLD process (restart
pending — regen chain gained render_coverage_index.py + the
py-then-html unit regen). Web: `/units/UNIT_INDEX.html` (17),
`/#Gen/6/22`-style deep links, frozen badges = switch buttons, the
Python rendering at the BOTTOM of every unit page. Stepper:
`python3 step_unit.py gen_16_ark_spec`. Onkelos cache: Gen 1:1-6:22
+ Lev 13:1-8 (gitignored; FETCHLOG is provenance). DB snapshot
torah_grok.SNAPSHOT-main-51801ca.sqlite held (gitignored).

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
