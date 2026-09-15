import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 10 — THE VOWS (2026-09-12): the appends — the stamp row, NUMBERS_WALK.md "Sitting 10", the state doc's #142,
# World/RESUME.md. THE_STEPS, THE_BRIEFING, COMPILE_DEBT, MIDDOT, RESEARCH_LOG and the memory files are edited by the Edit tool beside this
# script. The counts below are the tools' own prints (the ritual's PASS lines, the bake's hash, the truth's units), typed from them; the
# corpus tripwire is read back before a byte is appended.
import os
ROOT = _ROOT
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 205' in truth and 'assert len(W["standing"]) == 2103' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vows_ritual_num_30_vows.out'), encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_30_vows (205 frozen units)' in rit and rit.count('PASS ') >= 13 and 'FAIL' not in rit.split('=== RITUAL SUMMARY ===')[0].replace('FAILED 0', ''), 'the ritual is not complete'
def append(path, text):
    assert os.path.exists(path), path
    with open(path, 'a') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))

STAMP = ('| 2026-09-12 | num_30_vows | DELEGATED | FULL RULE | Numbers 30:1-17 derivation 2026-09-12 (THE NUMBERS WALK sitting 10 — THE VOWS; the owner: "Go" after the #141 rereads, on the ruling READ THEN COMPILE; the FORTY-SECOND NUMBERS UNIT — the portion Matot\'s first chapter as one draft, 30:1 the portion Pinchas\'s last verse read with it by the draft\'s-grain rule, the next draft opening at 31:1): declared reading COMPLETE — Onkelos Numbers 30:1-17 whole, 17 verses fresh, and the Sifrei on Numbers piskaot 153-156 FOUND BY POSITION (17 rows at the shelf\'s row grain; NO piska on 30:1 — 152:1\'s, read whole at sitting 9 and credited with a quick look; the rows\' own defects — the export\'s seventh mistyped head (156 "30:14" for 30:15), the English supplying the Mishnah at two rows, a citation and a speaker wrong (2 Kings "4:20", "King David"), the Hebrew\'s "R. Yochanan" and "so the father" garbled, an attribution, a conclusion and a lemma dropped by the English — read to their verses; no prior ledger had read a row of the chapter — grepped); coverage COMPUTED by script against the shelf\'s own counts (missing 0, extra 0); every quotation cut from the DB\'s and the shelf\'s bytes by consonants in glossed pieces of at most six tokens (no cut miss on the writer\'s first run; gloss_lint 0 on the first write; the ledger regenerated once inside its writing step for a middah label — the likening has no code among the thirteen); the ink facts computed and asserted (ONE failure on the first typed pass — the Chronicles-Psalm parallel\'s word index typed from memory, retyped from the print); the engine\'s parser measured on the chapter (no cardinal, no ordinal; the three oath-tokens STARRED as the seven-stem\'s refused homograph — 3b\'s rule at three new seats, no gap); 7 claims VERIFIED 0 FAILED (verify_claims from the repo root on the manifest\'s path — the first run from the scratchpad\'s cwd found no table: the cd lesson\'s eighth instance; every check the word\'s longest store-piece whole), claim_labels_census --strict GREEN (Numbers 325 labeled, debt 0; one I2), 7 WITNESS_READ operators seated by script on steps 1, 3, 4, 7, 10, 14, 17 with every cite checked against the ledger\'s cite index, verify_text GREEN (17 steps, 7 scenarios), freeze_ritual PASS on every gate (13 PASS — RITUAL COMPLETE, the forty-second frozen unit of the walk\'s count: 205 in all), the corpus rebaked once (205 units, standing 2103 = 2096 + 7 as predicted, hash 8b8fff1fa28953af unmoved), the Python rendering layer written (257 lines) and self-proved. Machine-administered under the 2026-09-01 delegation; labeled DELEGATED; the owner may overrule. |\n')

WALK = '''
## Sitting 10 — THE VOWS, Numbers 30:1-17 (2026-09-12; the owner: "Go" after the #141 rereads, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_30_vows 30:1-17 (17 of 17 verses, computed): 30:1 is the portion Pinchas's last verse (the calendar's receipt-closer) read with this
draft by the draft's-grain rule; 30:2-17 open the portion Matot; the next draft, num_31_midian, opens at 31:1 (asserted). Read in ONE pass, one ledger.

THE SHELF, BY POSITION (vows_ink.py's asserts): the Sifrei on Numbers has FOUR piskaot on the chapter — 153 (30:2, ten rows), 154 (30:10, three), 155
(30:14, one), 156 (headed "30:14", opening on 30:15 — THE SEVENTH MISTYPED HEAD of the export, found by the row's own quotation: "from day to day" stands
at 30:15 alone in the Torah; three rows) — SEVENTEEN rows; NO piska on 30:1 (152:1's, read whole at sitting 9 and CREDITED here with a quick look: its
standing row speaks of 30:1 exactly); the next head, 157, is 31:1; every head asserted between its neighbors. THE ROWS' OWN DEFECTS, read to their verses
(RESEARCH_LOG.md's entry): 153:3's English cites "II Kings 4:20" and glosses "(King David)" for the Hebrew's 2 Kings 2 — the words at 2:2, 2:4, 2:6 and 4:30,
never at 4:20, never David's; THE ENGLISH SUPPLIES THE MISHNAH at 153:3 and 153:4 ("his vows are examined", "a girl of eleven", the identity's content "ki
yafli") where the Hebrew rows carry neither (the inserted-clause class); 153:7's Hebrew names "R. Yochanan" for R. Yonatan and concludes "so the FATHER" for
the husband; 154:1's Hebrew closes "the words of R. Yishmael" and the English DROPS THE ATTRIBUTION (the sixth class again); 154:2's English drops the
Hebrew's conclusion ("leave to annul all the day"); 154:3's English drops the Hebrew's opening lemma (the caretaker excluded); 155:1's Hebrew breaks off
"so the father can". Onkelos 30 whole: 17. No prior ledger had read a row of the chapter (nine name verses of it as cross-references); FRESH.

THE READING (six modules — scratchpad vows_dump.py the first measurement pass; vows_measure1.py the second, printing every candidate fact; vows_ink.py the
ink with every fact an assert (assert_driver.py: ONE failure on the first typed pass — the Chronicles-Psalm parallel's word index typed from memory — then
0) and the piece-wise cutters HP / AP; vows_rows_onkelos.py the 17 rows; vows_rows_sifrei.py the 17 rows; write_vows_ledger.py the writer → ONE ledger
logic/oral_triage/num_30_vows_2026-09-12.md (34 sources: Onkelos MATERIAL 14 / CONTEXT 3; the Sifrei 17 / 0; coverage computed, missing 0, extra 0; NO cut
miss on the writer's first run; gloss_lint 0 on the first write; the ledger regenerated ONCE inside its writing step to fix a middah label — the likening
(hekkesh) has no code among the thirteen, I5 being particular-then-general: MIDDOT.md checked before a code is typed).

THE INK, COMPUTED (the measurement pass FIRST, the asserts typed from the print):
- THE PARSER MEASURED AGAIN (the standing rule): NO cardinal and NO ordinal in seventeen verses; the three OATH-tokens (30:3, 30:11, 30:14 — spelled with
  the letters of "seven") STARRED as refused homographs — 3b's rule on the seven-stem holding at three new seats: silent-and-right, NO GAP. The chapter's
  numbers are its clocks: "on the day of his hearing" (four seats, all here), "from day to day" (30:15), "after his hearing" (30:16).
- THE FRAMES AND THE REGISTER: TWO narrative verbs, both Moses' — 30:1 "and Moses SAID ... according to all that the LORD commanded Moses" (the receipt
  formula's seven Bible seats: six close ACTS, this alone closes a SPEECH — computed on the first word of every seat; the 9b debt (v)'s measurement: a class
  of one for the register gate) and 30:2 "and Moses SPOKE to the heads of the tribes ... this is the thing which the LORD commanded" — NO DIVINE FRAME: the
  formula's eight Bible seats, and its two Numbers seats (30:2, 36:6) are exactly the book's two law chapters without "the LORD spoke to Moses" (computed on
  the frames of every chapter); "the heads of the tribes" three Bible seats (Solomon's assembly the other two); 30:17 "these are the statutes" the footer
  (three Bible seats, this alone without "and the judgments"; "between a man and his wife", "between a father and his daughter" one seat each).
- THE CASE STRUCTURE: TWO "when" cases at the first word (30:3, 30:4; the chapter's other two "ki" are "because") and SEVEN "and if" branches (30:6, 7, 9,
  11, 13, 15, 16) — the draft's decision table's nine rows exactly; "and a woman, when" three Torah seats (the woman with a discharge and this).
- THE ROOTS: "vow" fourteen tokens (Numbers holds twenty-two of the Torah's forty), the bond-root twenty-two, the oath four; FIVE DOUBLED VERBS — "swear
  an oath", "be, she shall be" (Jeremiah 15:18 its kin), "annul, he annuls" (the form's two Bible seats, both here), "be silent, he is silent" — every one
  kept by Onkelos; the stand-root twelve tokens, the annul-root six, the silence-verb four, the restrain-verb three (its fourth Torah seat the spies', 32:9).
- THE CLOCK WORDS: "on the day of his hearing" ×4 all here; the hearing-infinitive six tokens; "FROM DAY TO DAY" two Bible seats — this and 1 Chronicles
  16:23, whose Psalm parallel (96:2) writes the words with the other preposition (Esther 3:7 the Psalm's): the Chronicler keeps the Torah's form; Onkelos
  renders 30:15 with the Psalm's; "after his hearing" one seat.
- THE FORGIVENESS AND THE INIQUITY: "and the LORD will forgive her" THREE seats, all in this chapter; the verb's fourth Bible token Naaman's (2 Kings
  5:18); Onkelos passive behind the buffer; "he shall bear HER iniquity" one seat — "her iniquity" five Torah seats, the suspected wife's (5:31) among them.
- THE PERSONS: "her husband" nine tokens, "her father" six; "in her youth" two seats, both here (the priest's daughter "AS in her youth", Leviticus
  22:13); "her father's house" seven Bible seats; "her husband's house" here and Ruth 1:9; "a widow or a divorced woman" THREE Torah seats — the high
  priest's forbidden wives, the priest's daughter sent home, and this; Onkelos "her OWNER" at all nine seats.
- THE UTTERANCE: "the utterance of her lips" (the noun) two seats, both here; the oath-verb "to utter with the lips" one seat (Leviticus 5:4) — the Sifrei's
  identity; "all that proceeds from her lips" one seat and its pair Deuteronomy 23:24; "he shall not profane his word" one seat in this sense; "all that
  proceeds from his mouth he shall do" one seat with its two echoes (32:24, Judges 11:36); "to afflict a soul" two Bible seats (Pharaoh's and this).
- ONKELOS' ONE ROOT: the oath, the confirming and the statutes all by the stand-root (the Hebrew's three roots one in the Aramaic); "restrained" turned
  away; "annul" void; "before the LORD".
- THE SHELF'S CITATIONS READ TO THEIR VERSES: 6:2's "clearly utters" (four Bible seats); Deuteronomy 23:22's "you shall not delay"; Leviticus 5:4; the
  trumpets 10:3-4; Exodus 11:4; Exodus 34:31-32; 2 Kings 2:2.

THE SIFREI'S OWN CASE LAW (twenty-three entries appended to MIDDOT.md "The middot's own case law"): the heads first by the identity "blowing" and the
release of vows by experts on a FREED phrase (the Sifrei's own addition, labeled); "this is the thing" as a limiter against two a-fortiori; the minor
excluded and the age fixed by the identity with the nazirite; "in any event"; a hint, not a proof; R. Eliezer's refused a-fortiori and the parallel reach
of two verbs; two transgressions on one vow; the woman likened by adjacency; the age by two exclusions; the chapter glossing itself; the three limiters on
hearing; confirmed for one hour; THE ENGINE OF THE FOOTER — the induction refused, the a-fortiori refused, the likening (hekkesh) of 30:17 "you are
compelled to liken" at four rows; "I REASONED AND REVERSED" — the Sifrei naming its own move; the forgiveness a-fortiori; the messenger dispute; the two
silences; THE DEADLINE'S TWO SETTINGS; the affliction filter; the part is the whole on a doubled object; "after his hearing" freed by its neighbor; the
measure of good; the father's reach bounded. No new move (MOVE_CATALOG unchanged).

THE CLAIMS (write_vows_manifest.py → one manifest, 7 claims MT30A-01..07, every check the word's LONGEST STORE-PIECE WHOLE — the chapter has no six-letter
stem, so sitting 9's rule is kept in its content (a prefix fragment is no check word) with its floor measured at four letters; the ID prefix asserted absent;
every cite checked against the ledger's CITE INDEX): verify_claims 7 VERIFIED / 0 FAILED (from the repo root on the manifest's path — the first run inside a
compound command after a cd to the scratchpad found no table: THE cd LESSON, THE EIGHTH INSTANCE); claim_labels_census --strict GREEN (Numbers 325 labeled
325, debt 0; one I2 — the utterance = oath identity, the Sifrei 153:7's). THE SEATS (seat_vows.py num_30_vows): 7 WITNESS_READ operators at the claims'
first verses (steps 1, 3, 4, 7, 10, 14, 17), step E, the scenarios in the anchor form; verify_text GREEN (17 steps, 7 scenarios). THE RITUAL (vows_chain.sh):
every gate PASS (13 PASS) — RITUAL COMPLETE for the 205th frozen unit; the Python rendering layer written (257 lines) and self-proved. THE CORPUS REBAKED
(predicted before the fold: units 205, standing 2096 + 7 = 2103, hash unmoved — the tripwire's literals set to the prediction before the bake): units 205,
facts 1809, demands 341 (191 open), standing 2103, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE
row (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep, the journal gate and the register gate stand as at 9b's close.

OWED TO THE COMPILE (sitting 30b; the box in COMPILE_DEBT.md, items (a)-(l)): the vow as a ledger entry with the CONFIRM / ANNUL state machine; the
day-of-hearing timer with TWO RECORDED SETTINGS (to nightfall; twenty-four hours); the authority table (father / husband / none) with 30:17's likening as its
rule; annulment after confirmation — "he shall bear her iniquity" on the husband's ledger (5:31 by CALL); the delay ban by CALL (the 9b debt (iv)); 30:1's
receipt a class of one for the register gate (the 9b debt (v)); the sage's release an answer-sheet row, never code; the two dispute forks (partial annulment;
the messenger); the docket by the union rule (Mishnah Nedarim 9-11 + Nedarim 66a-87b + the link rows); the parser's starred oath-tokens in the probes; the
edges (naso ×2, lev_05, the priesthood runner, Deuteronomy 23 not compiled, 32:24 forward); law_vows' installed_by for a law with NO divine frame; the tape
without a narrative event.

⚠ LESSONS (10): THE MEASUREMENT PRINT HAS THE INDEX — the one assert that fell was a word position typed from memory for a parallel the print had spelled
out (1 Chronicles 16:23 / Psalm 96:2). THE cd LESSON, THE EIGHTH INSTANCE — a cd at the head of a compound command reaches its tail; the repo-root tools by
absolute path in their own subshell. THE STORE'S SHORT STEMS — a check word is the word's longest store-piece taken whole; the six-letter floor was the
sitting-9 chapter's, the rule is "never a prefix fragment". A MIDDAH CODE IS CHECKED IN MIDDOT.md BEFORE IT IS TYPED — the likening (hekkesh) has no
I-code (I5 is particular-then-general); the ledger regenerated inside its writing step. THE MISTYPED HEAD IS FOUND BY THE ROW'S OWN QUOTATION (156 "30:14"
quoting 30:15's "from day to day", one Torah seat). THE ENGLISH SUPPLIES THE MISHNAH — read the Hebrew row before crediting an identity's content to the
Sifrei. THE READING SITTING'S SHAPE HELD: dump → measure → asserts (1 → 0) → rows → writer (0 misses; lint 0 first run; one regeneration inside the step)
→ manifest (7/7) → seat → ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF THE VOWS (30b) on 1b's order — the docket by the union rule, the vow's ledger entry and its machine, the day-of-hearing
timer with its two settings, the authority table, the delay ban by CALL, the register gate at the gates step, the installed_by form for a law in Moses'
voice — before chapter 31 (Midian), never the next reading first.
'''

STATE = '''
═══ COMPACTION POINT #142 (2026-09-12 — written at THE NUMBERS WALK sitting 10's close; THE VOWS 30:1-17 READ AND FROZEN; NUMBERS 1:1-30:17 READ, 27 BY THE TENT; 1:1-29:39 COMPILED AND ON THE TAPE; 30 NOT YET COMPILED) ═══
STATE: 205 frozen units (204 + 1), standing 2103 (2096 + 7 as predicted), hash 8b8fff1fa28953af UNMOVED; 51 runners, 56 daemons, the sweep 51/51 at 5,898 UNMOVED (no runner changed); the journal gate and the register gate GREEN as at 9b's close; RUN (1245, 60, 52, 0, 12, 1469, 27, 302, the four pairs, 114). LAST COMMIT a42f518; UNCOMMITTED: sitting 8's, 8b's, the discussion step's, the register gate's, 9's, 9b's and this sitting's paths — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #141 rereads; NUMBERS_WALK.md "Sitting 10"): chapter 30 read as ONE draft (num_30_vows 30:1-17; 30:1 the calendar's closer with it; 31:1 the next draft's): the Sifrei's FOUR piskaot 153-156 BY POSITION (17 rows; NO piska on 30:1 — 152:1 credited; THE SEVENTH MISTYPED HEAD — 156 "30:14" opening on 30:15; the English SUPPLYING THE MISHNAH at two rows; 2 Kings "4:20" / "King David" wrong; the Hebrew's "R. Yochanan" and "so the father" garbled; an attribution, a conclusion and a lemma dropped — all read to their verses) + Onkelos whole (17) = 34 sources in one ledger (six modules; ONE assert fell on the first typed pass — an index typed from memory; no cut miss; lint 0 first write; the ledger regenerated once inside its writing step for a middah label); 7 claims MT30A verified 7/7 and labeled (one I2), 7 operators seated, the ritual COMPLETE (13 PASS; the 205th unit), the corpus rebaked once (205, 2103, hash unmoved — predicted); THE PARSER MEASURED — no cardinal, no ordinal, the three oath-tokens STARRED (the seven-stem's homograph at three new seats): NO GAP; THE CROWNS: THE LAW IN MOSES' VOICE (no divine frame; the formula "this is the thing which the LORD commanded" at eight seats, its two Numbers seats the book's two such chapters — 30 and 36), the receipt that closes a SPEECH (30:1 alone of seven), two "when" cases and seven "and if" branches = the draft's nine rows, FIVE DOUBLED VERBS, THE CLOCK THE CHAPTER'S ONLY NUMBER ("on the day of his hearing" ×4; "from day to day" — the Chronicler keeps the Torah's preposition where the Psalm's differs; the Sifrei's two settings), the forgiveness clause's three seats all here, the widow and the priest's daughter sharing a pair of words, ONKELOS' ONE ROOT for oath, confirmation and statute, THE SIFREI'S ENGINE the footer's likening at four rows and "I REASONED AND REVERSED" named; twenty-three case-law entries in MIDDOT.md; the cd lesson's EIGHTH instance.
THE RECORDS: NUMBERS_WALK.md "Sitting 10"; the ledger, manifest and py rendering; MIDDOT.md's twenty-three entries; RESEARCH_LOG.md's twelve-finding entry; COMPILE_DEBT.md's sitting-10 box (a)-(l); STAMP_LEDGER's row; THE_STEPS' sitting-10 paragraph; THE_BRIEFING's scoreboard bullet; World/RESUME.md; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); this entry. MOVE_CATALOG unchanged (no new move).
NEXT on the ruling: SITTING 30b — THE COMPILE OF THE VOWS on 1b's order (COMPILE_DEBT's sitting-10 box: the docket by the union rule — Mishnah Nedarim 9-11 by topic + Nedarim 66a-87b + the link rows; the vow as a ledger entry with the CONFIRM / ANNUL state machine; the day-of-hearing timer with TWO RECORDED SETTINGS as a calendar_parameters row; the authority table (father / husband / none) with 30:17's likening its rule; "he shall bear her iniquity" on the husband's ledger by CALL to the sotah cell; the delay ban by CALL (the 9b debt (iv)); 30:1's receipt a class of one for the register gate (the 9b debt (v)); the sage's release an answer-sheet row; law_vows' installed_by for a law with NO divine frame (36:6 the same class); the tape with no narrative event; the gates with THE REGISTER GATE at the gates step — `python3 World/step9/register_census.py --strict`; the sweep 52), THEN CHAPTER 31 — Midian's reading (31:1-54; the Sifrei's 157-158 by position) — never the next reading first.
POST-COMPACTION REREADS (mandatory, first sitting): numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 9b — AS BUILT" (the compile's form with the timers) + NUMBERS_WALK.md "Sitting 10" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-10 paragraph first); before the gate's step: THE_LOOP.md "THE REGISTER GATE" (the dispositions' law — a paid seat's KEY AND BODY deleted); at the types step: daemon_dispositions.yaml's installed_by values (the form for a law in Moses' voice). WATCHES: as #141's + THE MEASUREMENT PRINT HAS THE INDEX + THE cd LESSON (the eighth instance — the tools in their own subshell from the root) + THE STORE'S SHORT STEMS (the longest piece whole) + A MIDDAH CODE IS CHECKED IN MIDDOT.md BEFORE IT IS TYPED (the hekkesh has none) + THE ENGLISH SUPPLIES THE MISHNAH (read the Hebrew row) + THE DEADLINE'S TWO SETTINGS ARE A PARAMETER + NO DIVINE FRAME (installed_by).
'''

RESUME = '''SITTING 10 DONE 2026-09-12 (THE VOWS 30:1-17 READ AND FROZEN; NUMBERS_WALK.md "Sitting 10"; the owner: "Go" after the #141 rereads): the Sifrei's four piskaot 153-156 by position (17 rows; none on 30:1 — 152:1 credited; the export's seventh mistyped head; the English supplying the Mishnah at two rows; a citation and a speaker wrong) + Onkelos whole (17) = 34 sources in one ledger (one assert fell on the first typed pass — an index typed from memory; no cut miss; lint 0 first write); 7 claims verified and labeled, 7 operators seated, the ritual COMPLETE → 205 units, standing 2103, hash unmoved (predicted); THE PARSER no cardinal, no ordinal, the three oath-tokens starred — no gap; THE LAW IN MOSES' VOICE (no divine frame — the formula's two Numbers seats the book's two such chapters); five doubled verbs; the clock the chapter's only number ("from day to day" — the Chronicler keeps the Torah's form; the Sifrei's two settings); Onkelos' one root for oath, confirmation and statute; the Sifrei's engine the footer's likening, "I reasoned and reversed" named. NEXT: 30b — THE COMPILE OF THE VOWS (COMPILE_DEBT's sitting-10 box; the register gate at the gates step), THEN chapter 31 — never the next reading first.
'''
append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append(((_ROOT + '/World') + '/RESUME.md'), RESUME)
