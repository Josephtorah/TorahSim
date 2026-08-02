# Resume prompt — TWENTY frozen; the exit and the altar next · 2026-08-01

Paste the block below into the compacted session to resume exactly where
we left off. (Supersedes PROMPT_continue_gen19; gen_19 is agent-derived,
reviewed, and frozen — the remembering is in.)

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, on
**main**; last PUSHED commit 60a8a7d — the gen_14-16 wave + the Python
layer; the gen_17 + gen_18 + gen_19 waves are frozen ON DISK, NOT yet
committed). Local dev server: `python3 dev_server.py` (port 8011 —
RESTARTED 2026-08-01, fresh process, full regen chain).

**ABSOLUTE RULE (memory: chat-hebrew-glossing, owner order):** NEVER
reference Hebrew anywhere — script, transliteration, OR Hebrew-derived
jargon — without its English counterpart inline. Every time. All outputs.

**STANDING RULE (memory: compaction-protocol):** owner compacts at ~700k
tokens; keep THIS resume file current at every milestone, unprompted;
announce clean compaction points.

**STANDING RULES (memory: auto-freeze-process + agent-derivation-trial +
python-rendering-layer):** inline derivations auto-freeze on green;
AGENT-drafted units freeze-AFTER-REVIEW (agent delivers status:draft,
NEVER freezes; main loop reviews prose — glossing, independent census
re-verification against the raw snapshot, [OPEN] discipline, no
invention — then flips, real-gate re-verifies, regresses ALL frozen,
renders logic/py_units/<uid>.py GREEN, renders the page **passing the
date-less canonical name as arg 2** (render_unit_html.py's default is
date-suffixed!), runs index_units.py at REPO ROOT +
render_coverage_index.py, export_web.py in background, updates this
file). Amend/narrative/triage/COMMIT gates: owner order only.

**THE AGENT PROCESS (verdict KEEP — two units in: gen_18 trial passed,
gen_19 passed with zero corrections needed):** ONE persistent
derivation agent (continue via SendMessage — it has derived gen_18 +
gen_19 and carries the corpus). PIPELINE: it pre-stages the NEXT
span's DB-static evidence while the main loop reviews; fetches,
watch-list prose, YAML wait for the seed. DEBUT MAP: build_debut_map.py
-> gitignored debut_map sqlite (acceptance-gated); debut_scan.py <book>
<ch> <v1> <v2> gives COMPLETE span surveys; join dm.token_ordinals to
words.id for careers. Reviewer INDEPENDENTLY re-queries the raw
snapshot for crown finds. Sequential blocks only — never parallel.
Reviewer calibration notes sent to the agent after gen_19: name
sibling lemmas on stem-splits (nuach 5117 vs yanach 3240 — 2:15
garden-placing vs 8:4 ark-rest, itself a find); say "near-verbatim"
when a pronoun shifts (the manoach clause).

**State: TWENTY units FROZEN and green** (gen_01..gen_19 — Gen 1:1-8:14
GAPLESS — plus lev_13; regression 20/20; TEN consecutive extension-free
derivations). Newest:
- `gen_19_the_remembering` (Gen 8:1-14, freeze-after-review #2, agent
  unit 2, first under pipeline+map): ZAKHAR ('remember') Torah-debut
  on Noach AND the animals — the Name back (Elohim ×2, the span's only
  name-tokens), speech NOT (second speechless span, zero
  speech/imperatives, but not nameless like gen_18); AVAR ('pass
  over') debuts carrying 1:2's RUACH ('wind/spirit') — hover set
  moving; the shut-mirror NEAR-verbatim (totalizers KOL/RABBAH
  dropped) with TORAH-HAPAX stop-up verb sakhar ≠ door-verb sagar;
  150-bracket closed; the ark RESTS (nuach debut) on its builder's
  name-sound, month 7 day 17, on gen_18's drowned-at-debut mountains;
  the tops APPEAR by 1:9's own niphal see-verb (verified
  creation-mirror); the decree's end-word (qetz token 3) counts down
  to the window HE MADE (gen_16 receipt; chalon ≠ tzohar, [OPEN]
  stands); SHALACH ('send') tokens 1-2 = EDEN EXPULSION, 3-7 = the
  five sendings (birds piel, hand qal); the dove finds no MANOACH —
  two-token word, the exile-curse (Deut 28:65) re-uses the clause
  near-verbatim; held as FACT not the first FAIL (TESTS keeps its
  verdict-formula discipline — decision recorded); the leaf at the
  FIRST EVENING since the week (erev tokens 1-6 = the creation
  refrain); aleh ('leaf') 3 tokens = shame/hope/terror; TARAF + the
  second wait-verb both TORAH HAPAXES; QALAL ('abate') tokens 1-2
  in-span, token 3 = 8:21's never-again-CURSE (one root); t0 :=
  year-601/month-1/day-1 (the SECOND calendar anchor — single-anchor
  decision, other date-ladder rungs as facts); RISHON ('first')
  debuts inside the date; CHAREV both tokens in one verse; MIKHSEH
  ('covering') token 1 — all 15 others sanctuary fabric; the earth
  dry ten days past the entry-slot one year on — ends dry, silent,
  SEALED-IN (exit-word = 8:15). Onkelos: remember → mindful STATE +
  Elohim leveled to the LORD-name ×2; waters given the rest-verb
  early; Ararat → Kardu; sky-lattice + ark-window merged; hand-send
  broken from the send-run; wait-verbs leveled; taraf absorbed; KEPT:
  hapax stop-up cognate, abate-root, appearance-passive, menach (the
  Deut 28:65 echo), exact dates, the knowing, the speechlessness.
  Machine: t0 anchored, 0 installs (+3 presupposed), 0 writes, 0
  queue traffic (second in a row), 0 tests, 23 events, 18 facts, 3
  read-flags. Watch-list: THIRTEENTH consecutive zero-cache tripwire.
- `gen_18_the_rise` (Gen 7:17-24, freeze-after-review #1): the silent
  span (zero names/speech/imperatives); waters LIFT the ark (active,
  waters as agent); GAVAR born ×4 in-span; three death-orders held;
  wipe executed twice nameless; SHAAR remnant-root debut; AKH ('only')
  own debut at 7:23 (debut-map find, post-freeze note).
- `gen_17_boarding` (Gen 7:1-16): first PERSON-verdict (PASS tzaddik);
  first calendar t0; double breach; Elohim-commands/YHWH-shuts split.

**KNOWN COSMETIC DEFECT (owner decision pending):** gen_14's 32
boot-step he: lines UNPOINTED (amend-gated).

**UNCOMMITTED pile (on disk — awaiting owner's commit order):** the
gen_17 + gen_18 + gen_19 waves: three frozen YAMLs; WATCHLIST_gen17/18/
19; FETCHLOG += 38 lines (16+8+14); py_units gen_17/18/19;
UNIT_gen_17/18/19 pages + UNIT_INDEX (20); build_debut_map.py +
debut_scan.py (the map itself gitignored); PROMPT_continue_gen18/19/20;
dev_server.py regen-chain edits (from the earlier wave). Protected
untracked (NEVER commit): Disclosure/, reviews/architecture/NARRATIVE_
theory_of_disclosure_intro, TEMP_return_to_main.

**Read these first, in order:**
1. `logic/units/gen_19_the_remembering.yaml` — freshest frozen (the
   reversal-log format, the single-anchor date-ladder decision, the
   fact-not-FAIL dove decision).
2. `logic/units/gen_18_the_rise.yaml` — the silent-span encoding.
3. `run_unit.py` header + `logic/py_units/machine.py`.
4. `logic/middot_scan/WATCHLIST_gen19_prospective_2026-08-01.md`.
5. `logic/pre_logic_methods_2026-07-28/debut_scan.py` (+ the map).

**TASK 1 — derive gen_20 = Gen 8:15-22 (the exit and the altar) VIA THE
AGENT** (SendMessage to the persistent agent; its gen_20 EVIDENCE WAS
ORDERED PRE-STAGED 2026-08-01 — check the staging report / scratchpad
gen20_* files first). Seed leads (all to DB-verify): SPEECH RETURNS —
8:15 va-yedabber ('and God SPOKE') opens the first divine speech since
7:4 (and the SPEAK-verb dibber vs the say-verb amar — census the
debut); the EXIT COMMAND (tze, 'go out') mirroring 7:1's come-command
— the settled-cycle machinery returns (DECLARE + RESULT expected:
first SPECS traffic since gen_17!); the exit by families (le-mishpechot
— census); 8:20 THE ALTAR — mizbeach ('altar') TORAH DEBUT expected +
Noach BUILDS (banah token census; gen_13's city was the first human
build-verb) + the take-verb takes of EVERY CLEAN (gen_17's sevens PAY
OFF — the cargo arithmetic explained) + olah ('burnt-offering') debut
candidate; 8:21 the SMELL event (ruach/reach — divine sense-event
class) + the heart-speech (el-libo, 'to His heart' — the divine
INTERIOR speech: gen_15's heart-pair bookend) + YETZER token 2 (6:5's
inclination word — gen_15 PREDICTED this bookend: verify and close
the arc) + the never-again pair (lo osif ×2) + QALAL token 3 (gen_19
logged the abate/curse root arc — it closes here); 8:22 the seasons
pledge: od kol-yemei ha-aretz — seed/harvest/cold/heat/summer/winter
day/night 'shall not CEASE' (shavat — the SABBATH-root as the
never-stopping verb! census); expect debuts across the season-words.
Genre: command cycle resumed + first cult act + divine resolution.
Machine: DECLARE/RESULT return; possible LEDGER? (no — no day-count);
TESTS candidate at the smell? (no verdict-adjective expected — check);
t0 candidate NONE (no date in span — durations of 8:22 are cyclical).
Seam: 9:1 opens the blessing (gen_21).

**TASK 2 — standing queue (all owner-gated):** triages owed — days 6-7,
lev_13, gen_08 (Sanhedrin 56b), gen_09 (58a), gen_10 (ADRN 1; 29a),
gen_11 (BR 20:12), gen_12 (Mishnah Sanhedrin 4:5), gen_13 (Rambam AZ
1:1; BR 23), gen_14 (BR 24-25 klal; 5:24 fork), gen_15 (BR 26; 6:3
rebuild), gen_16 (Sanhedrin 108a; be-dorotav; tzohar), gen_17 (BR 32:5
praise-delta), gen_18 (BR 32:11 akh-diminution; Zevachim 113; Rashi
7:20), gen_19 (RH 11b-12a calendar; Sanhedrin 108b raven/dove; BR 33;
Rashi ×5) — FOURTEEN owed and compounding; days 2-3 backfill;
narratives since day 5 (ASK OWNER FIRST, each); PUBLIC REPORT; middot
v2; Stage E linker (gen_15→7:23 wipe = test case, both ends frozen;
now also gen_15 yetzer→8:21 + gen_19 qalal→8:21 arcs); repo-tools
decision; gen_14 pointing fix; gen_boot renderings (offered).

**State notes:** dev server fresh on 8011. index_units.py at REPO ROOT.
render_unit_html.py: PASS THE DATE-LESS OUTPUT NAME as arg 2. Web:
/units/UNIT_INDEX.html (20), Python rendering at page bottom. Stepper:
`python3 step_unit.py gen_19_the_remembering`. Onkelos cache: Gen
1:1-8:14 + Lev 13:1-8 (FETCHLOG is provenance). DB snapshot
torah_grok.SNAPSHOT-main-51801ca.sqlite (he_plain keeps morpheme
slashes — strip before phrase searches; match lemma parts EXACTLY —
Strong 7430 'creep' contains 430 'God'). Debut map:
debut_map.SNAPSHOT-main-51801ca.sqlite (rebuild via
build_debut_map.py if the snapshot ever changes). Subagent status
line installed at user level (visible from next session; /tasks now).

**Standing rules (non-negotiable):** Pre-Code (logic hand-authored in
frozen YAML; code only interprets; flags never auto-resolve;
dual-track, never merge). Freeze: auto for inline, AFTER-REVIEW for
agent drafts. Hebrew ALWAYS glossed in English — absolute, everywhere,
forever. Oral: named location only; machine never derives law (ein
adam dan me-atzmo — "one may not derive on his own"). Sefaria:
sequential, 0.5s, small ranges, EVERY fetch logged in Data/FETCHLOG.md.
Commit trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
Repo PRIVATE (Sefaria licensing). gh account Josephtorah. Disclosure/ +
reviews/architecture/NARRATIVE_theory_of_disclosure_intro are the
owner's own docs — NEVER commit them.
