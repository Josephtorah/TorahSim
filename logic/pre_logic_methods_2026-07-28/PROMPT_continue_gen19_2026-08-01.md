# Resume prompt — NINETEEN frozen; the remembering next · 2026-08-01

Paste the block below into the compacted session to resume exactly where we
left off. (Supersedes PROMPT_continue_gen18; gen_18 is derived BY THE
AGENT, reviewed, and frozen — the trial ran and PASSED.)

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, on
**main**; last PUSHED commit 60a8a7d — the gen_14-16 wave + the Python
layer; gen_17 AND gen_18 and their waves are frozen ON DISK, NOT yet
committed). Local dev server: `python3 dev_server.py` (port 8011).

**ABSOLUTE RULE (memory: chat-hebrew-glossing, owner order):** NEVER
reference Hebrew anywhere — script, transliteration, OR Hebrew-derived
jargon — without its English counterpart inline. Every time. All outputs.

**STANDING RULE (memory: compaction-protocol):** owner compacts at ~700k
tokens; keep THIS resume file current at every milestone, unprompted;
announce clean compaction points.

**STANDING RULE (memory: auto-freeze-process + agent-derivation-trial):**
freeze on green pre-flight is AUTOMATIC for inline derivations; for
AGENT-drafted units it is freeze-AFTER-REVIEW (the agent delivers
status:draft and never freezes; the main loop reviews prose — glossing,
census spot-reverification, [OPEN] discipline, no invention — then
freezes). Stop ONLY on interpreter extension or RED regression.
Amend/narrative/triage/COMMIT gates: owner order only.

**STANDING RULE (memory: python-rendering-layer):** every frozen unit
gets a generated `logic/py_units/<uid>.py` (must run GREEN), embedded at
the BOTTOM of its unit page. YAML canonical; never hand-edit py_units.

**THE AGENT PROCESS (trial PASSED on gen_18 — owner verdict: KEEP,
pending explicit owner confirmation if not yet given):** ONE persistent
general-purpose derivation agent runs the mechanics (watch-list with
DB-verified censuses -> morph dump -> trees -> Onkelos Tier-A fetch,
sequential 0.5s + FETCHLOG -> 4-part YAML draft -> pre-flight vs the
UNMODIFIED interpreter). It must deliver status:draft — NEVER freeze,
never touch the interpreter, machine.py, other units, or git. The main
loop writes the seed, REVIEWS the draft prose, freezes on a passing
review, then runs the chain (real gate -> regression -> render_unit_py
-> render page -> index_units.py at REPO ROOT + render_coverage_index
-> export_web background -> update this file). CONTINUE THE SAME AGENT
via SendMessage for corpus familiarity (it has derived gen_18; ask it
for gen_19 with a fresh seed). Sequential blocks only — never parallel
(finds chain across freezes; span boundaries; Sefaria rate discipline;
shared ledger files).

**TWO PROCESS UPGRADES (owner-ordered 2026-08-01, live):**
1. **PIPELINE:** the agent pre-stages the NEXT span's DB-static
   evidence (morph, trees, debut scan, cache check — scratchpad only)
   while the main loop reviews/seeds the current block. Fetches,
   watch-list, YAML always wait for the seed. gen_19's evidence was
   ORDERED PRE-STAGED 2026-08-01 (check the agent's staging report /
   scratchpad gen19_* files before re-ordering it).
2. **DEBUT MAP:** precomputed census cache — every Torah token's
   ordinal within its lemma + lemma totals. Build:
   `python3 logic/pre_logic_methods_2026-07-28/build_debut_map.py`
   (acceptance-gated against gen_18's verified censuses) -> gitignored
   `debut_map.SNAPSHOT-main-51801ca.sqlite` at repo root. Span survey:
   `python3 logic/pre_logic_methods_2026-07-28/debut_scan.py Gen 8 1 14`
   (flags DEBUT / EARLY≤6 / RARE≤8 / CLUSTER≥3 lemmas — COMPLETE, not
   curated). First fruit: AKH ('only'), Strong 389, has its OWN Torah
   debut at 7:23 riding the remnant line — a find both the gen_18 seed
   and the targeted censuses missed. Reviewer still spot-re-queries
   the raw snapshot for crown finds (independence). gen_18 review-quality evidence: ALL censuses
verified real on independent re-run; the agent self-corrected a
pre-drafted Onkelos guess from the actual fetches and disclosed it;
found NEW finds the seed missed (rise-verb debut, mountains/high-word
debut drowned, cover-verb debut, dry-land two-token twin, the
three-token face-of-the-waters phrase, the fully SILENT span).

**State: NINETEEN units FROZEN and green** (gen_01..gen_18 — Gen
1:1-7:24 GAPLESS — plus lev_13; regression 19/19; NINE consecutive
extension-free derivations). Newest:
- `gen_18_the_rise` (Gen 7:17-24, freeze-after-review #1, AGENT-drafted):
  the judgment waters LIFT the ark (bear-verb token 2 — token 1 was
  Cain's too-heavy bearing — ACTIVE, waters as agent; the seed expected
  a passive and the letter overruled it) and it RISES (rise-verb's
  Torah debut; career: raised-hand oath, staff over the Nile, high
  hand); the ark WALKS (go-stem token 2; token 1 = the serpent's crawl)
  the face-of-the-waters — a THREE-token phrase (1:2 hover / 7:18 walk
  / Exod 32:20 calf-dust); GAVAR ('prevail') BORN as the span — 7
  Torah tokens, tokens 1-4 in-span, ringed event/state/state/event;
  mountains + high-word DEBUT drowned under the cover-verb's first two
  agentless tokens (next token: a father's nakedness covered, 9:23);
  fifteen cubits — the ark-blueprint's own unit measures the flood
  (amah token 5; token 6 = the ark of the covenant, Exod 25:10); THREE
  death-orders (dying-list humankind LAST alone on the verse-end arm;
  wipe-scope = 6:7's decree VERBATIM humankind FIRST; neither =
  creation's) held unharmonized; 2:7's breath-formula quoted one word
  WIDER at the drowning (nishmat-RUACH chayim — prose-held quote-diff,
  translation-stable in Onkelos; [OPEN] what the inserted spirit-word
  marks); the wipe EXECUTED twice in one verse (active + niphal
  agentless, machah tokens 3 AND 4) in a span with ZERO divine names,
  ZERO speech, ZERO imperatives (first fully silent unit — executioner
  covert, antecedent = 7:16's YHWH across the unit boundary; gen_15's
  wipe-demand NOT popped — standalone queues; Stage E test case); and
  THE CROWN: VA-YISHAER AKH-NOACH — SHAAR, the REMNANT-root, FIRST
  TOKEN of 29, born naming one man and a boat's company. Onkelos: rise
  passivized, walk de-animated, expire-verb leveled (decree-echo
  lost), crawl-words leveled, dry-land word leveled, BUT the compound
  breath-formula kept word for word, wipe kept double, remnant kept
  cognate, zero names inserted; NEW: Aramaic renders 'high mountains'
  with the RUM-root — tying peaks to the ark-lift with one root where
  the Hebrew uses two. Machine: t0 EMPTY (durations, not dates —
  decision), 0 installs (+3 presupposed), 0 writes, 0 queue traffic
  (first zero-traffic queue), 0 tests, 11 events, 10 facts, 3
  read-flags. Watch-list: TWELFTH consecutive zero-cache tripwire.
- `gen_17_boarding` (Gen 7:1-16): first PERSON-verdict (PASS tzaddik);
  TAHOR debut in cargo arithmetic; settled cycle #2 (bo->va-yavo);
  first full calendar date (t0 := year-600/month-2/day-17); double
  breach; Elohim-commands/YHWH-shuts name-split which Onkelos levels
  while rewriting shutting as SHIELDING.
- `gen_16_ark_spec` (6:9-22): first fully-settled command cycle (two
  imperatives popped by 6:22 receipt); WORLD += tevah; BRIT token 1.

**KNOWN COSMETIC DEFECT (owner decision pending):** frozen gen_14's 32
boot-step `he:` lines are UNPOINTED (generator slip; content identical;
gen_15+ fixed). Fix is amend-gated.

**UNCOMMITTED pile (on disk — awaiting owner's commit order):** the
ENTIRE gen_17 + gen_18 waves: gen_17_boarding.yaml + gen_18_the_rise.yaml
(both frozen); WATCHLIST_gen17 + WATCHLIST_gen18; FETCHLOG += 24 lines
(16 + 8); logic/py_units/gen_17_boarding.py + gen_18_the_rise.py;
UNIT_gen_17_boarding.html + UNIT_gen_18_the_rise_2026-08-01.html +
UNIT_INDEX.html (19); PROMPT_continue_gen18 + THIS file; the user-level
subagent status line (~/.claude/subagent-statusline.sh + settings —
outside the repo). Protected untracked (NEVER commit): Disclosure/,
reviews/architecture/NARRATIVE_theory_of_disclosure_intro,
TEMP_return_to_main.

**Read these first, in order:**
1. `logic/units/gen_18_the_rise.yaml` — freshest frozen (agent-drafted
   format — identical house style; the silent-unit encoding, the
   duration-vs-date TIME decision, the cross-unit [OPEN] wipe).
2. `logic/units/gen_17_boarding.yaml` — the execution-log format.
3. `run_unit.py` header + `logic/py_units/machine.py`.
4. `logic/middot_scan/WATCHLIST_gen18_prospective_2026-08-01.md`.
5. Scratchpad gen18_* scripts (the agent's assembly pattern — clones of
   the gen17 pattern; preflight_gen18.py harness).

**TASK 1 — derive gen_19 = Gen 8:1-14 (the remembering) VIA THE AGENT**
(continue the SAME agent by SendMessage; fresh seed from the main loop;
freeze-after-review). Expected content to DB-verify at seed time (all
UNVERIFIED — the agent must census them): VA-YIZKOR ELOHIM ET-NOACH
(8:1 — 'and God REMEMBERED Noach': the zakhar remember-verb's first
token toward a person? census; the silence of gen_18 BROKEN by the
remembering, not by speech); the RUACH ('wind/spirit') God passes over
the earth — 1:2's hovering word returning as the flood's off-switch;
VA-YASHOKU ha-mayim ('the waters ASSUAGED' — shakhakh census); the
fountains and windows SHUT (8:2 — the 7:11 double breach REVERSED:
sealed from both sides; heaven's-windows token 2 of 2); the waters
going and RETURNING (halokh va-shov — the go-verb in the infinitive
pair); 150 days CLOSED (8:3 — the 7:24 bracket's other end); the ark
RESTS (VA-TANACH, 8:4 — the nuach rest-root ON NOACH'S OWN NAME
etymology, on the mountains of Ararat, month 7 day 17 — CALENDAR
RETURNS: TIME_ANCHOR candidate); mountains' tops SEEN (8:5, month 10
day 1); the forty days (8:6 — another forty); the RAVEN out (orev
debut, yatzo va-shov 'going and returning'); the DOVE x3 (yonah debut
— no rest for her foot / the olive leaf TORN at evening / returns no
more: 8:8-12, the seven-day rhythms); the ground DRIED (charvu — the
charav root vs yavshah, 8:13-14, two different dry-words, two dates —
year 601 day 1 month 1 vs month 2 day 27; Noach removes the COVER
(mikhseh — the kasah cover-root as a NOUN) and SEES. Genre: the
un-creation's reversal begins — expect TIME_ANCHOR(s) (the calendar
resumes), the shut events mirroring gen_17's breaches, the first
divine-interior event since gen_15 (remember), bird events, and the
two-stage drying. Span decision: 8:1-14 (the drying, 14 verses) with
8:15 opening the EXIT COMMAND (speech returns) as gen_20's natural
seam — the agent may confirm or propose the alternative at watch-list
time. Ninth… tenth extension-free candidate expected.

**TASK 2 — standing queue (all owner-gated):** triages owed — days 6-7,
lev_13, gen_08 (Sanhedrin 56b), gen_09 (58a), gen_10 (ADRN 1; 29a),
gen_11 (BR 20:12), gen_12 (Mishnah Sanhedrin 4:5), gen_13 (Rambam AZ
1:1; BR 23), gen_14 (BR 24-25 klal; the 5:24 fork), gen_15 (BR 26
bnei-elohim; the 6:3 rebuild), gen_16 (Sanhedrin 108a
robbery-as-lexicon; be-dorotav diyyuk; tzohar fork), gen_17 (BR 32:5
praise-delta), gen_18 (BR 32:11 akh-diminution; Zevachim 113
Israel-exemption; Rashi 7:20 draft-arithmetic) — THIRTEEN owed and
compounding; days 2-3 backfill; narratives since day 5 (ASK OWNER
FIRST, each); PUBLIC REPORT; middot v2; Stage E linker (gen_15 -> 7:23
wipe execution = its test case, now BOTH ends frozen); repo-tools
decision; the gen_14 pointing fix; gen_boot renderings (offered).

**State notes:** dev server on 8011 RESTARTED 2026-08-01 (fresh process
with the full regen chain: py-then-html per-unit regen +
render_coverage_index). render_unit_html.py's default output name is
DATE-SUFFIXED — always pass the canonical date-less path as arg 2
(logic/pre_logic_methods_2026-07-28/UNIT_<uid>.html). index_units.py
lives at REPO ROOT (not in pre_logic_methods).
Web: `/units/UNIT_INDEX.html` (19), Python rendering at page bottom.
Stepper: `python3 step_unit.py gen_18_the_rise`. Onkelos cache: Gen
1:1-7:24 + Lev 13:1-8 (gitignored; FETCHLOG is provenance). DB snapshot
torah_grok.SNAPSHOT-main-51801ca.sqlite (words.he_plain keeps morpheme
slashes — strip before phrase searches; beware lemma substring
false-positives: match lemma parts exactly, e.g. Strong 7430 'creep'
contains 430 'God'). Subagent status line: installed at user level
(shows running agents below the prompt; /tasks lists them).

**Standing rules (non-negotiable):** Pre-Code (logic hand-authored in
frozen YAML; code only interprets; flags never auto-resolve;
dual-track, never merge). FREEZE: automatic on green for inline;
freeze-AFTER-REVIEW for agent drafts. Hebrew ALWAYS glossed in English
— absolute, everywhere, forever. Oral: named location only; verified
from local corpus; machine never derives law (ein adam dan me-atzmo —
"one may not derive on his own"). Sefaria: sequential, 0.5s, small
ranges, EVERY fetch logged in Data/FETCHLOG.md. Commit trailer:
`Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`. Repo PRIVATE
(Sefaria licensing). gh account Josephtorah. Disclosure/ +
reviews/architecture/NARRATIVE_theory_of_disclosure_intro are the
owner's own docs — NEVER commit them.
