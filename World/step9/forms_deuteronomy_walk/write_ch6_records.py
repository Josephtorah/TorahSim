#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4 — CHAPTER 6 (2026-09-17; the owner: "ok lets start the next chapter", then "go" / "Continue" / "Go" for runs 2-4 —
# the FIRST sitting under THE FOUR-RUN RULE): THE RECORDS at the close, from the sheet World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 4
# — AS BUILT", COMPILE_DEBT's box (owed to the compile 4b), MIDDOT's block (the Sifrei's case law on the chapter), RESEARCH_LOG's entry, THE_STEPS'
# paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's #190 addendum 3, the recovery page (rewritten whole, under 10 KB), the
# recovery addenda's section 38, the stamp row, the memory file and the index line (under 17,000 bytes). Every number parsed from a print named
# beside it (--check prints them and writes nothing); every insert on a unique anchor asserted present once; the lints before and after.
# Sitting 3's form (write_ch5_records.py) on the sheet.
import os, re, subprocess, sys, yaml, json
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-17'
UID = 'deu_06_shema'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 220' in truth and 'assert len(W["standing"]) == 2203' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/ch6_truth.out'); CB = rd(f'{SP}/ch6_bake.out'); C1 = rd(f'{SP}/ch6_fold_check1.out')
assert 'CORPUS TRUTH GREEN' in CT and 'CORPUS TRUTH GREEN' in C1 and 'wrote corpus_world.sqlite' in CB
rit = rd(f'{SP}/ch6_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch6_vt_{UID}.out'); assert 'TEXT LAYER GREEN: 25 steps, 7 scenarios' in vt
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch6_chain.log')
JG = rd(f'{SP}/ch6_journal.out'); RG = rd(f'{SP}/ch6_register.out'); BW = rd(f'{SP}/ch6_build.out')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'THE REGISTER GATE: GREEN' in RG, (JG[-200:], BW[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units, (\d+) facts, (\d+) demands \((\d+) open\)', CT); C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups()
assert C_UNITS == '220', C_UNITS
HG = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True).stdout
assert 'GREEN' in HG, HG[-200:]
LED = rd(f'{ROOT}/logic/oral_triage/deu_06_vaetchanan_{DATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei spine, CONTEXT (\d+) Sifrei spine, MATERIAL (\d+) Sifrei outside, CONTEXT (\d+) Sifrei outside', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC = ml.groups()
assert L_ALL == '97' and L_ONK == '25' and L_SIF == '72'
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF6 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.6.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF6 == 24 and OV_REF == 496 and OV_GL == 385, (OV_REF6, OV_REF, OV_GL)
N_CLAIMS = len(json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))); assert N_CLAIMS == 6
LL = subprocess.run([sys.executable, f'{ROOT}/World/step9/large_letter_probes.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]
assert LL.endswith('6/6'), LL
print('PARSED:', dict(ritual_pass=N_PASS, journal=(J_KINDS, J_ROWS), register=(R_DECL, R_DEBT, R_FAIL), corpus=(C_UNITS, C_FACTS, C_DEM, C_OPEN), ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_XM, L_XC, L_BYTES), overrides=(OV_REF6, OV_REF, OV_GL), claims=N_CLAIMS, large_letters=LL))

def append(path, text):
    s = rd(path); assert text not in s
    with open(path, 'a', encoding='utf-8') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))
def insert_before(path, anchor, text):
    s = rd(path); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, text + anchor)); print('inserted %d bytes before %r -> %s' % (len(text.encode()), anchor[:30], path))
def replace_once(path, a, b):
    s = rd(path); assert s.count(a) == 1, (path, a[:40], s.count(a))
    open(path, 'w', encoding='utf-8').write(s.replace(a, b)); print('replaced %r -> %s' % (a[:30], path))

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 6:1-25 derivation {DATE} (THE DEUTERONOMY WALK sitting 4 — CHAPTER 6; the owner: "ok lets start the next chapter", then "go", "Continue", "Go" for the runs — the first sitting under THE FOUR-RUN RULE; the book\'s fourth reading — chapter 6 as one draft, the 220th frozen unit): declared reading COMPLETE (one ledger logic/oral_triage/deu_06_vaetchanan_{DATE}.md, {L_ALL} sources — Onkelos 6:1-25 whole and fresh (the export\'s twenty-five rows the DB\'s twenty-five, asserted), the Sifrei on Deuteronomy\'s PISKAOT 31-36 ON THE CHAPTER (the heads 6:4, 6:5, 6:6, 6:7, 6:8, 6:9 — one per verse of the Shema) read whole in both files — 67 rows, 64 fresh and 3 CREDITED from Genesis sittings with a quick look each (32:2, 33:4, 36:10 — where the export\'s two files DIVERGE: the Hebrew\'s parable of the king\'s wife, the English\'s own 37:2 repeated), and EIGHT rows outside the spine citing chapter 6 found by the scan of the whole export in both files (38:10, 41:14, 41:20, 104:8, 201:3, 258:1, 306:37, 355:27), one excluded (62:4, the English\'s slip for Numbers 6:27); coverage computed by script, missing 0 extra 0; the ink facts computed from the Tanakh DB, the snapshot store and the shelf\'s bytes — 113 asserts, six fell on the first typed pass (forms, not facts) and were retyped from the print, none after; every quotation cut by consonants, one miss on the first run (a "that-" prefix fused to its word) retyped; gloss_lint 0), claims DV06-01..06 verified {N_CLAIMS}/{N_CLAIMS} (every check the word\'s longest store-piece whole — never 6:4\'s two words, whose large letters the store drops), claim_labels_census --strict GREEN, seated as six WITNESS_READ operators at the claims\' first verses (6:1, 4, 6, 10, 16, 20), verify_text GREEN (25 steps, 7 scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2203 = 2197 + 6 as predicted, hash 8b8fff1fa28953af UNMOVED), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — no seat in the chapter). THE PARSER: one number verse in twenty-five, NO GAP — 6:4 "the LORD is one" [1], the creed\'s word the numeral; the seven-stem homographs refused. THE FINDS: the spine lands on the chapter (six piskaot on six verses; 6:1-3 and 6:10-25 without a piska); the creed\'s first utterance Jacob\'s sons\' answer at the deathbed (31:6); "the LORD is one" two seats in the Bible (6:4, Zechariah 14:9); the store drops 6:4\'s two large letters (the hypothesis parked); might = money = measure = thanks (32:6, 7, 21; Onkelos "your property"); the two sets recited and bound with the ten words in neither (34:2-3, 35:1-2); THE COUNT FROM THE SPELLINGS DIVERGES — the shelf\'s four compartments need 11:18 "frontlets" defective, the ink spells it plene (35:4; the compile\'s open row; RESEARCH_LOG {DATE}); the verbal analogy with two candidates (36:2 — the shelf\'s own exhibit of I2\'s reception rule); extension after extension on the one-letter pair 6:9 / 11:20 (36:3); the spoil permitted by 6:11 (201:3); singular against plural (41:20); the son\'s question verbatim with Exodus 13:14 and the answer in the first person plural (the readback\'s next form); the receipt without the Name at 6:25 (the register gate blind to it). Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = f'''

## Sitting 4 — CHAPTER 6 — AS BUILT ({DATE}; the design above stands as written — the four runs ran as designed, the RUN 2 and RUN 3 paragraphs their record; every departure from the design named here)

THE RESULT: Deuteronomy 6:1-25 READ AND FROZEN as one unit — deu_06_shema, the 220th frozen unit; the ledger logic/oral_triage/deu_06_vaetchanan_{DATE}.md
({L_ALL} sources: Onkelos {L_ONK} — MATERIAL {L_OM} / CONTEXT {L_OC}; the Sifrei's spine 64 fresh — MATERIAL {L_SM} / CONTEXT {L_SC} — and 3 credited; the outside rows
8 — MATERIAL {L_XM} / CONTEXT {L_XC}; {L_BYTES:,} bytes; lint 0); the manifest deu_06_shema_claims.json ({N_CLAIMS} claims DV06-01..06, verify_claims {N_CLAIMS}/0, the
labels census GREEN); six WITNESS_READ seats at 6:1, 4, 6, 10, 16, 20, step E, seven anchor scenarios; the ritual {N_PASS} PASS; the fold predicted and
matched before and after the bake ({C_UNITS} units, standing 2203, hash 8b8fff1fa28953af; {C_FACTS} facts, {C_DEM} demands, {C_OPEN} open); the display layer
+{OV_REF6} by reference and +33 by gloss (by_ref {OV_REF}, by_gloss {OV_GL} after); the stamp row delegated (FULL RULE). No engine file changed — the tape as
at 3b's close (RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127), markers 167, closes 127); the sweep as at 3b.

THE DEPARTURES FROM THE DESIGN: none in substance. THE FOUR RUNS held their edges — run 1 the rereads, the measurements, the ink (113 asserts, 0
failing on the second pass) and the design; run 2 the rows and the ledger (the checkpoint #190 addendum 1); run 3 the display layer, the manifest,
the seat, the chain, the fold and the gates (#190 addendum 2); run 4 the records (#190 addendum 3) — the owner compacted after run 1 only and said
"Continue" and "Go" for runs 3 and 4 at 349k and 445k. THE LARGE-LETTER QUESTION (run 1's discussion) became a HYPOTHESIS on his word and was
PARKED at his remark; World/step9/large_letter_probes.py rides the gates chain ({LL}). The credited row 36:10 turned out to be a row where THE TWO
FILES DIVERGE (the English's own 37:2 repeated); the Hebrew's parable read at the quick look. Two forms fell during the runs and were fixed in place
(run 2: the ink's ledger-list guard; run 3: the guard's one-sided compare, the claim verifier's argument).

THE GATES, COMPUTED FROM THEIR PRINTS: the ritual {N_PASS} PASS (RITUAL COMPLETE, 220 frozen units); CORPUS TRUTH GREEN twice ({C_UNITS} units, {C_FACTS}
facts, {C_DEM} demands ({C_OPEN} open), hash 8b8fff1fa28953af — the tripwire's literals set to the prediction before the bake, matched); build_world
ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows — 9660 at sitting 3); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT},
FAILS {R_FAIL}); the home-path gate GREEN; the labels census GREEN (385 claims labeled, debt 0); the lints at their baselines.

⚠ THE LESSONS (the three runs', gathered — the numbered list the sheet asks for): (1) THE HEBREW'S "IBID." FORM — a Sifrei row cites "there" after a
Deuteronomy citation in the same row; the union of both files is the finder. (2) THE ENGLISH EXPORT CAN MIS-CITE A BOOK — a cited verse beyond the
chapter's length is checked against the DB before it is counted. (3) A TRANSLATOR'S PARENTHESIS IS NOT THE SIFREI'S CITATION. (4) THE STORE'S LARGE
LETTERS — the defect report of 2026-09-09 named 6:4 in advance; the census is four tokens; no claim's check uses those words. (5) THE FIRST TYPED
PASS FALLS ON FORMS, NOT FACTS — the asserts typed from the print still need the FORM of the prior record read. (6) THE EXPORT'S TWO FILES CAN
DIVERGE ROW BY ROW — a credit is a credit on the file that was read; the quick look opens the other. (7) THE SHELF CAN COUNT A SPELLING THE INK DOES
NOT HAVE — 11:18 "frontlets" defective in the shelf's count, plene in the codex: a divergence filed to the compile, never resolved by the reading.
(8) A "THAT-" PREFIX IS PART OF THE SHELF'S TOKEN — the cut names the fused word. (9) A GUARD THAT FILTERS ONE SIDE OF A COMPARE MUST FILTER BOTH.
(10) THE CLAIM VERIFIER TAKES THE MANIFEST'S PATH. (11) THE FOLD SCRIPT WAITS ON THE UNIT'S INDENTED "status: frozen". (12) THE FOUR-RUN RULE
HELD ON A READING SITTING — each run's checkpoint named the next run's first step and the reread after the compaction was three files.

THE FORMS: World/step9/forms_deuteronomy_walk/ — the four runs' scripts (ch6_dump0.py, ch6_measure1.py, ch6_ink.py, the six row files, write_ch6_ledger.py,
ch6_patch_overrides.py, write_ch6_manifest.py, seat_ch6.py, ch6_chain.sh, ch6_fold.sh, write_ch6_design.py, write_large_letters.py, write_ch6_run2.py,
write_ch6_run3.py, write_ch6_records.py, copy_ch6_forms.py) and the prints (the dump, the measurement, the Onkelos dump, the ink runs, the chain log,
the ritual, verify_text, the fold's checks, the gates); the two large Sifrei dumps not copied (reproducible by ch6_dump0.py).

NEXT on the ruling: THE COMPILE OF CHAPTER 6 (sitting 4b) in four runs — (1) the rereads (THE_STEPS Step 5 + the compiler block; this section; the 4b
box in COMPILE_DEBT.md), the measurements (the tape's state at Deut 5:33; the runners' cells the chapter calls — the second word's cell at 3b, the
exodus story's lines for the son's answer) and THE DESIGN in this file before any code; (2) the docket by the union rule (Berakhot 2a-16a whole;
Menachot 28b-44a; Pesachim 56a, 116a-b; Kiddushin 30a-b; Sanhedrin 4b, 74a; Shabbat 103b; Yoma 11a; Bava Metzia 108a; Mishnah Berakhot 1:1-3:5, 9:5;
Pesachim 10:4; Sotah 7:1; Maaser Sheni 3:8) with the tefillin cell's open row on the spellings; (3) the runner (the four duties as cells; fear-serve-
swear; the test; the right and the good; the son's answer as THE READBACK'S THIRD FORM — a retelling told to a son graded against the tape's exodus
lines; the receipt without the Name declared or the finder taught), the stitch, the tape to 10/10; (4) the gates chain, the records, the forms. Or
THE DECALOGUE-SCHEMA SITTING first, on the owner's word. Then chapter 7, and on in order.
'''

DEBT = f'''
## DEUTERONOMY SITTING 4 — CHAPTER 6, Deuteronomy 6:1-25 READ AND FROZEN ({DATE}; DEUTERONOMY_WALK.md "Sitting 4" and "Sitting 4 — AS BUILT"; the ledger
## deu_06_vaetchanan_{DATE}.md, {L_ALL} sources; one unit deu_06_shema FROZEN, the 220th) — OWED TO THE COMPILE (sitting 4b): (a) THE SHEMA'S FOUR DUTIES AS
## LAW CELLS (6:6-9) — the words on the heart and THE RECITATION (its times, postures, audibility, places: Mishnah Berakhot 1:1-3:5, 9:5; Berakhot 2a-16a;
## the Sifrei 31:7, 34:8-10, 258:1), the teaching (34:1-4; Kiddushin 30a-b), THE TEFILLIN (the four passages 34:2-3, 35:1-2; the compartments 35:3-4; the
## arm, the side, the order, the head 35:5-12; Menachot 34b-37b) WITH THE SPELLINGS' OPEN ROW — the shelf's count of four needs 11:18 "frontlets" defective,
## the ink plene (RESEARCH_LOG {DATE}; the number a PARAMETER taught by the shelf, its derivation a recorded argument on another witness), THE MEZUZAH (36:1-8;
## Menachot 31b-34a; Shabbat 103b; Yoma 11a; Maaser Sheni 3:8); (b) FEAR, SERVE, SWEAR (6:13 = 10:20) — the oath by the Name (Shevuot; Temurah 4a); (c) NO
## OTHER GODS (6:14) — a CALL into 3b's second-word cell (cold_run_covenant_at_horeb); (d) THE TEST (6:16) — the run citation of Exodus 17 (Massah) the
## readback's form; (e) THE RIGHT AND THE GOOD (6:18) — Bava Metzia 108a's abutter, a rule beyond the letter seated in the ink; (f) THE SON'S ANSWER AS THE
## READBACK'S THIRD FORM (6:20-25) — a retelling told to a son in the first person plural, graded against the tape's exodus lines (Exodus 7-14); the four
## sons (Mishnah Pesachim 10:4; Pesachim 116a-b); (g) 6:1'S EDGE — the charge's teaching opens: a REFERENCE to the debit closed at 3b (Deut 1:5's close of
## the charge to teach); (h) 6:10-11'S LIST — a DATA row (the cities, houses, cisterns, vineyards; Joshua 24:13 and Nehemiah 9:25 the retellings; the Sifrei
## 38:10's merit, 201:3's spoil permitted — the war chapter's CALL into 6:11 when chapter 20 compiles); (i) "SWORE TO YOUR FATHERS" three times (6:10, 18, 23)
## — the oath's tape entries (Genesis 22:16, 26:3, 50:24; Exodus 13:5, 33:1) as run citations; (j) THE RECEIPT WITHOUT THE NAME (6:25 "as He commanded us",
## with Ezra 4:3) — the register gate's finder taught the form, or the seat declared by hand; (k) THE LARGE LETTERS — the PARKED hypothesis: no work unless
## the owner's word (the DB and the store rebuilt with the segment type; the 6:4 edge `link: hypothesis`); (l) THE DOCKET by the union rule (the TESTING
## paragraph's tractates above; Sanhedrin 4b and 74a; Sotah 7:1; the Mekhilta Pisha 17 named by the Sifrei 35:4-12's notes — the first copy's spine on
## the tefillin, unopened by any ledger). NOTHING ELSE IN CHAPTER 6 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 6 (Deuteronomy 6:1-25; THE DEUTERONOMY WALK sitting 4, {DATE};
  the ledger logic/oral_triage/deu_06_vaetchanan_{DATE}.md — PISKAOT 31-36 ON 6:4-9, one per verse of the Shema, 67 rows read in
  both files; the rows below the ones that argue by a numbered rule, each at its row):**
  · THE CREED'S FIRST UTTERANCE (31:6 on 6:4): the law's words given their narrative seat — Jacob's sons' answer at the deathbed
    ("Hear, O ISRAEL" the father), the response line supplied for the recitation — E28's kin; a history, not a mashal.
  · THE TWO EPITHETS (31:8, 31:10 on 6:4): "our God" beside "one" read as an addition (E10 — the repeated expression signifies), then
    the verse's two halves given two scopes and two times (E11's kin), Zechariah 14:9 the proof — THE INK AGREES: "the LORD one" two seats.
  · THE DOUBLED LETTER (32:3 on 6:5): "your heart" with its doubled bet read as two inclinations — E10's kin (a spelling as a count;
    Mishnah Berakhot 9:5); 32:4 the same word divided, "a heart in you" — E30's form.
  · MIGHT AS MONEY, MEASURE, THANKS (32:6, 32:7, 32:21 on 6:5): the one-seat word given three readings — 32:6 two terms each given a case
    (E10), 32:7 an a-fortiori STATED AND SET ASIDE as making the word idle (I1 refused), then the word read by its sound (the tradition's
    own play, outside the numbered rules); Onkelos's "your property" the same reading as 32:6.
  · THE TWO SETS, RECITED AND BOUND (34:2-3 on 6:7; 35:1-2 on 6:8): four a-fortiori arguments that would merge the Shema's passages and
    the tefillin's, each cut by the ink's "these" (I1 stated and refused — the restriction E2's kin); the ten words in neither set.
  · THE TIMES OF THE RECITATION (34:8-10 on 6:7): "when you lie down" and "when you rise" each bounded by the third clause "when you walk
    by the way" — I13's form (two decided by a third); the two houses' postures the dispute row (Mishnah Berakhot 1:3).
  · THE COUNT FROM THE SPELLINGS (35:4 on 6:8): "frontlets" at three seats counted 1 + 1 + 2 = four compartments — E10's kin (a spelling as
    a count) — WHERE THE INK DIVERGES: the codex spells 11:18 plene (the ink's FRONT asserts the three spellings); "memorial" singular
    (Exodus 13:9) the one case; Sanhedrin 4b, Menachot 34b the same count; the compile's open row.
  · THE TWO LIMBS BY ONE RULE (35:5, 35:12 on 6:8): the hand's place from the head's and the head's from the hand's — E8 (binyan av's form);
    35:11 the order of the acts from the order of the clauses — E11's kin.
  · THE PERFECT WRITING (36:1 on 6:9): "and you shall write them" divided into "a perfect writing" — E30 (notarikon); the scribe's rule of
    letter shapes (Shabbat 103b).
  · THE VERBAL ANALOGY WITH TWO CANDIDATES (36:2 on 6:9): "write" joined by the same word to 27:8's stones or to Numbers 5:23's scroll and
    ink — I2 (gezerah shavah, the Sifrei's own, LR1: taught), with a RULE OF CHOICE stated (the standing over the momentary) and the proof
    graded "a hint" — the shelf's own exhibit of I2's reception rule: the shared word an unbounded generator, the teacher picks.
  · EXTENSION AFTER EXTENSION (36:3 on 6:9): "doorposts" plural at 6:9 and again at 11:20 read as ONE post — E3 (the numbered rule itself,
    in R. Ishmael's name); THE INK: the two seats one letter apart, defective and plene. 36:4 R. Isaac's father from Exodus 12:7 — I3.
  · WHICH GATES (36:6-8 on 6:9): "your gates" bounded by "your house" — a dwelling, a place of honor, the profane — I6's form (the particular
    bounding the general); Mishnah Maaser Sheni 3:8 the case row.
  · SINGULAR AGAINST PLURAL (41:20 on 11:13 from 6:5): the suffix's number the reading — the individual's study, the community's deed —
    E10 (the repetition distinguished by its number); THE INK AGREES: seven singular seats, four plural.
  · THE SPOIL PERMITTED (201:3 on 20:17 from 6:11): a later law bounded by an earlier promise — I13's form (two verses reconciled), the
    Sifrei's own (LR1); the war chapter's CALL into 6:11 at its compile.
  · THE CREED ANSWERED (355:27 on 33:26 from 6:4): six antiphonal pairs, Israel's "the LORD is ONE" met by heaven's "ONE nation" — E27
    (symmetry); the row's Hebrew cites 6:4 as "ibid.".
'''

RESEARCH = f'''
## {DATE} — DEUTERONOMY 6 READ (THE DEUTERONOMY WALK sitting 4 — CHAPTER 6, the first sitting under THE FOUR-RUN RULE): THE SPINE LANDS ON THE SHEMA — SIX PISKAOT
## ON SIX VERSES; THE CREED'S FIRST UTTERANCE AT JACOB'S DEATHBED; THE EXPORT'S TWO FILES DIVERGE AT ONE ROW; THE TWO SETS RECITED AND BOUND; THE VERBAL ANALOGY
## WITH TWO CANDIDATES; THE RECEIPT WITHOUT THE NAME (the frontlets' spelling and the large letters at their own entries of this date)

THE SPINE LANDS ON THE SHEMA. The Sifrei on Deuteronomy, silent by position over chapters 4 and 5, heads piskaot 31-36 on 6:4, 6:5, 6:6, 6:7, 6:8, 6:9 —
one per verse of the Shema — and nothing else of the chapter (piska 37 heads on 11:10; chapters 7-10 have none): 67 rows in both files, 100 KB. The
shelf reads the creed and its four duties alone; 6:1-3 and 6:10-25 are read here through Onkelos and eight rows citing them from elsewhere. Read at a
short cut (the English capped, the Hebrew's opening for the cuts) under the four-run rule; 97 sources, coverage computed.

THE CREED'S FIRST UTTERANCE. Piska 31 reads "Israel" in 6:4 as Jacob's own name (31:1) and puts the creed's first saying in his sons' mouths at his
deathbed (31:6): "Hear, O Israel our father — the LORD our God, the LORD is one", the father's doubt answered; the response line "blessed be the name
of His glorious kingdom" supplied between 6:4 and 6:5 for the recitation (the export's note: not scriptural). The ink beside it: "hear, O Israel" four
seats, all this book's; "the LORD one" at 6:4 and Zechariah 14:9 alone in the Bible (31:10 quotes the one other seat); the parser reads the creed's word
as the numeral [1] and Zechariah's pair as [1, 1]; heaven answers Israel's "one" with "one nation" (355:27, 1 Chronicles 17:21).

THE EXPORT'S TWO FILES DIVERGE AT ONE ROW. At Sifrei 36:10 the Hebrew file carries the parable of the king who told his wife to adorn herself (the
close of 36:9's "beloved is Israel"); the English file carries the Hebron-and-Zoan paragraph — its own 37:2 repeated (both files sixteen rows in piska
37). A Genesis sitting had credited "36:10" on the English's text. The rule: a credit is a credit on the file that was read; the two files are compared
row by row, not row-counted; the quick look opens the other file.

THE TWO SETS RECITED AND BOUND. Piskaot 34 and 35 define the Shema's text and the tefillin's from the two verbs: "teach them diligently" — these are
recited (6:4-9, 11:13-21, Numbers 15:37-41), the two Exodus passages are not; "bind them" — these are bound (Exodus 13:1-10, 13:11-16, 6:4-9, 11:13-21),
the fringes are not; four a-fortiori arguments that would merge the sets are each cut by "these", and the ten words belong to neither (34:2-3, 35:1-2).
The ink: the four bound passages are the four seats of "for a sign upon your hand", in four spellings of "your hand".

THE VERBAL ANALOGY WITH TWO CANDIDATES. Piska 36:2 joins "write" at 6:9 by the same word to 27:8 (the stones) or to Numbers 5:23 (the scroll and ink)
and chooses by a stated rule (a thing for the generations from a thing for the generations), then grades its own proof "a hint": the shelf's own
exhibit of the reception rule the link review law rests on — the shared word generates two joins; the teacher picks. 36:3 reads the one-letter pair
"doorposts" (6:9 defective, 11:20 plene) by extension-after-extension as one post; 36:4 builds the father from Exodus 12:7's "two doorposts".

THE RECEIPT WITHOUT THE NAME. 6:25 closes the chapter with "as He commanded us" — with Ezra 4:3 the two seats of the form; the register gate's census
reads "as the LORD commanded" and does not see it: the chapter has no seat in the gate (no index line, no yaml key — computed). The finder taught the
form, or the seat declared by hand, owed to the compile; the son's question at 6:20 quotes 4:45's footer ("the testimonies, the statutes and the
judgments" — the two seats), and his answer (6:21-25) is a retelling of the exodus in the first person plural — the readback's next form.

THE STORE'S GLOSSES READ BACK (the display layer): 33 rows by gloss and {OV_REF6} by reference — "to-fillet-for-the-forehead" FOR FRONTLETS, "very-you/your"
YOUR MIGHT, "and-point-them/their" AND YOU SHALL TEACH THEM DILIGENTLY, "deferred" TOMORROW, "and-rightness" AND RIGHTEOUSNESS, "strike-in" PLANT, "glow"
BE KINDLED, "and-sate" AND BE SATISFIED, the two "?" made "I", "strength" made GOD and "nose" ANGER at 6:15; by_ref {OV_REF}, by_gloss {OV_GL} after.
'''

STEPS = f'''DEUTERONOMY — SITTING 4 — CHAPTER 6, Deuteronomy 6:1-25 ({DATE}, on Brian's "ok lets start the next chapter", then "go", "Continue" and "Go" for the
runs — the first sitting under the four-run rule; World/step9/DEUTERONOMY_WALK.md "Sitting 4" and "Sitting 4 — AS BUILT").
The chapter of the Shema. For the first time in this book the Sifrei's own sections land on the chapter: six of them, one for each verse from
"Hear, O Israel" to "write them on the doorposts", and nothing on the verses before or after. The sitting ran as four runs with a stopping point
after each — the measurements and the design; the rows and the ledger; the seat, the freeze and the fold; the records — and the reread after the
one compaction was three files. What the reading found: the Sifrei puts the creed's first saying in Jacob's sons' mouths at his deathbed, answering
their father's doubt; "the LORD is one" stands only here and once in Zechariah; the word "might" has one seat in the whole Bible, and the shelf
reads it three ways — money, measure, thanks — while Onkelos writes "property"; the Shema's text and the tefillin's text are two sets that share
two members, with the ten commandments in neither; one row of the shelf's English file turned out to be a different row than its Hebrew, so a
credit from a Genesis sitting stood on the wrong text and the Hebrew was read fresh; and the shelf counts the tefillin's four compartments from a
spelling our Bible text does not have — that goes to the compile as an open row, recorded and not resolved. Our machine's own store drops the two
large letters of "Hear" and "one" — a marker layer we named a hypothesis and parked. The chapter is frozen as one unit, the 220th, the world's
standing facts up by six as predicted, its hash unmoved, every gate green. Next: the compile of chapter 6 in four runs — the creed's duties as
code, the son's answer graded against the tape as a story told to a son — or the ten-commandments schema first, on your word.

'''
BRIEF = f'''- **CHAPTER 6 READ AND FROZEN — THE SHEMA: THE SIFREI'S SIX SECTIONS LAND ON SIX VERSES, THE CREED'S FIRST SAYING IS JACOB'S SONS' ANSWER, AND THE SHELF COUNTS A SPELLING OUR TEXT DOES NOT HAVE** ({DATE}, on your "ok lets start the next chapter" and the runs' "go", "Continue", "Go" — the first sitting in four runs; World/step9/DEUTERONOMY_WALK.md "Sitting 4"): Onkelos on all 25 verses, the Sifrei's 67 rows on 6:4-9 and eight rows from elsewhere — {L_ALL} sources, coverage computed; "the LORD is one" two seats in the Bible; "might" one seat, read as money, measure, thanks; the Shema's text and the tefillin's two sets with the ten commandments in neither; one row where the shelf's two files diverge; the tefillin's four compartments counted from a spelling of 11:18 our text writes differently — an open row for the compile; the store's dropped large letters a parked hypothesis; one unit frozen (the 220th), 6 claims verified, the ritual 13 PASS, standing facts 2203 (+6 as predicted), hash unmoved, every gate green. NEXT: the commit on your word; then the compile of chapter 6 in four runs, or the schema sitting first.
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 6 READ: THE SHEMA, AND THE FIRST SITTING IN FOUR RUNS

The chapter that holds "Hear, O Israel". Two things are new here. The first is the way the sitting ran: four runs with a clean stopping point after
each, as you ruled after chapter 5's compile ran too long in one piece — the measurements and the design, then the rows and the ledger, then the
seat and the freeze and the fold, then the records. You compacted once; the reread after it was three files; the later runs went on your "Continue"
and "Go". The second is the shelf itself: for the first time in Deuteronomy the Sifrei's own sections fall on the chapter, six of them on six verses,
from "Hear" to "write them on the doorposts", and nothing else. What they say is worth having in the machine. The creed's first saying is put in
Jacob's sons' mouths at his deathbed, answering his fear that one of them had strayed — "Hear, O Israel" is the father's name. "The LORD is one"
occurs only here and once in Zechariah, and the Sifrei quotes that one other place. The word "might" in "with all your might" has a single seat in
the whole Bible, and the tradition reads it three ways: money, measure, thanks. The text of the Shema and the text inside the tefillin are two
lists that overlap by two passages, with the ten commandments deliberately in neither. Two cautions came with the finds. One row of the shelf's
English file is not the same row as its Hebrew — a Genesis sitting had credited it on the English side, so the Hebrew was read fresh, and the rule
is now written: a credit belongs to the file that was read. And the shelf counts the tefillin's four compartments from the spellings of "frontlets"
in three verses, which needs one of them spelled short where our Bible text spells it long. That is not ours to settle; it is recorded as an open
row for the compile. The chapter is frozen as one unit, the 220th, every gate green.

'''
RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 4 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 4" + "Sitting 4 — AS BUILT"): CHAPTER 6 READ AND FROZEN as one
# unit (the 220th — deu_06_shema 6:1-25), THE FIRST SITTING IN FOUR RUNS (a clean point after each): the Sifrei's piskaot 31-36 ON 6:4-9 (67 rows,
# both files) + eight rows from elsewhere + Onkelos whole — {L_ALL} sources, coverage computed; the creed's first utterance at Jacob's deathbed (31:6);
# "the LORD is one" two seats; the two sets recited and bound; THE TWO FILES DIVERGE at 36:10; the four compartments counted from a spelling the ink
# does not have (11:18 plene) — the compile's open row; the large letters a PARKED hypothesis (large_letter_probes {LL}); the ritual {N_PASS} PASS,
# CORPUS TRUTH GREEN ({C_UNITS} units, standing 2203 = 2197 + 6, hash unmoved), build_world, the journal gate ({J_KINDS} kinds, {J_ROWS} rows), the register
# gate --strict (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}) GREEN. NEXT on the ruling: the commit; then 4b — the compile of chapter 6 in four runs.
'''
STATE = f'''

#190 ADDENDUM 3 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 4 — CHAPTER 6's READING, RUN 4 of four — A CLEAN COMPACTION POINT): THE STATE: chapter 6 read and frozen as one unit (deu_06_shema, the 220th); the corpus {C_UNITS} units, standing 2203 (2197 + 6 as predicted), hash 8b8fff1fa28953af unmoved; the tape unmoved since 3b (RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127), markers 167, closes 127); the ledger deu_06_vaetchanan_{DATE}.md ({L_ALL} sources, {L_BYTES:,} bytes, lint 0); the manifest {N_CLAIMS} claims verified; the display layer +{OV_REF6} / +33 (by_ref {OV_REF}, by_gloss {OV_GL}). THE GATES: the ritual {N_PASS} PASS; CORPUS TRUTH GREEN twice; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); the home-path gate GREEN; the labels census GREEN; large_letter_probes {LL}. THE RECORDS (write_ch6_records.py from the sheet, one call): the map's "Sitting 4 — AS BUILT" (twelve lessons gathered from the three runs), COMPILE_DEBT's 4b box (a)-(l), MIDDOT's block (fifteen rows of the Sifrei's case law on the chapter), RESEARCH_LOG's entry (with the two of this date already written at runs 1 and 2), THE_STEPS, THE_BRIEFING (the scoreboard and an entry), RESUME, the recovery page rewritten whole (section 2 to this close; under 10,240 bytes), the addenda's §38, the stamp row, the memory (the walk note and the index line under 17,000 bytes); the forms copied (copy_ch6_forms.py). THE FOUR-RUN RULE'S FIRST SITTING: run 1 closed at #190 (the compaction), run 2 at #190 addendum 1, run 3 at addendum 2, run 4 here — the owner compacted once and said "Continue" / "Go" for runs 3 and 4; every run's checkpoint named the next run's first step. NOT COMMITTED: the whole sitting since 7c8554e — the commit message drafted at <scratch>/commit_msg_ch6.txt for his word ("commit" = no push). NEXT ON THE RULING: the commit; then 4b — THE COMPILE OF CHAPTER 6 in four runs (the design first, in the map; the debt box (a)-(l) its list; the readback's third form for the son's answer) — or the Decalogue-schema sitting first, on his word. IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 4 — AS BUILT" (NEXT and the lessons), MEMORY.md — nothing else unasked; THE_STEPS Step 5 + the compiler block before 4b's design.
'''
ADDENDA = f'''
## 38. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 4 — CHAPTER 6, Deuteronomy 6:1-25 READ AND FROZEN in four runs; the owner: "ok lets start the next chapter", "go", "Continue", "Go"; the state doc's #190 and its addenda 1-3)
THE STATE: chapter 6 read and frozen as one unit (deu_06_shema, the 220th); the corpus {C_UNITS} units, standing 2203 (2197 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED since 3b (RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127), markers 167, closes 127); the
journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); uncommitted since 7c8554e.
WHAT THE SITTING FOUND: the Sifrei's piskaot 31-36 on 6:4-9, one per verse of the Shema (the first heads on the chapter since piska 30 on 3:29); the
creed's first utterance Jacob's sons' answer at his deathbed (31:6); "the LORD is one" at 6:4 and Zechariah 14:9 alone (the parser [1] / [1, 1]); the
store drops 6:4's two large letters (a HYPOTHESIS on the owner's word, PARKED); "might" the Bible's one seat, read as money, measure, thanks (Onkelos
"your property"); the two sets recited and bound with the ten words in neither; THE EXPORT'S TWO FILES DIVERGE at 36:10 (the Hebrew's parable, the
English's own 37:2 repeated — a credit is a credit on the file read); THE SHELF'S COUNT FROM THE SPELLINGS needs 11:18 "frontlets" defective where the
ink is plene (the compile's open row); the verbal analogy with two candidates (36:2); extension after extension on the one-letter pair 6:9 / 11:20;
the spoil permitted by 6:11 (201:3); the son's question verbatim with Exodus 13:14 and the answer in the first person plural; the receipt without the
Name at 6:25. THE FOUR-RUN RULE'S FIRST SITTING: the runs' edges held; the reread after the one compaction three files.
THE FILES CHANGED: logic/oral_triage/deu_06_vaetchanan_{DATE}.md (new); logic/units/deu_06_shema.yaml (draft → frozen, six operators, step E, the
scenarios in the anchor form) and logic/py_units/deu_06_shema.py; logic/oral_audit/manifests/deu_06_shema_claims.json (new);
logic/glosses/word_gloss_overrides.yaml (+{OV_REF6} by reference, +33 by gloss); logic/corpus/CORPUS_TRUTH.py (220, 2203); World/step9/large_letter_probes.py
(new) and gates_chain.sh; the records (the map, COMPILE_DEBT, MIDDOT, RESEARCH_LOG (three entries of this date), THE_STEPS, THE_BRIEFING, RESUME, the
state doc, the recovery page, this file, STAMP_LEDGER, the memory); World/step9/forms_deuteronomy_walk/ (the sitting's scripts and prints).
NEXT ON THE RULING: the commit; then the compile of chapter 6 (4b) in four runs — or the Decalogue-schema sitting first — on the owner's word.
'''
MEMPAR = f'''
SITTING 4 DONE {DATE} (the owner: "ok lets start the next chapter", "go", "Continue", "Go"; the map's "Sitting 4" and "Sitting 4 — AS BUILT"): CHAPTER 6
READ AND FROZEN as one unit (deu_06_shema, the 220th) — THE FIRST SITTING UNDER THE FOUR-RUN RULE (four clean points: #190, its addenda 1-3; the owner
compacted once). The Sifrei's piskaot 31-36 ON 6:4-9; the creed's first utterance at Jacob's deathbed; "the LORD is one" two seats; "might" one seat
read three ways; the two sets recited and bound; the two files DIVERGE at 36:10 (a credit is a credit on the file read); the four compartments counted
from a spelling the ink does not have (11:18 plene — the compile's open row); the large letters a PARKED hypothesis. Every gate green; the corpus 220 /
2203 / hash unmoved; the tape unmoved. ⚠ LESSONS (twelve in the map): the "ibid." form; a mis-cited book; a translator's parenthesis; a guard filters
both sides of a compare; the verifier takes the manifest's path. OWED TO 4b (COMPILE_DEBT's box (a)-(l)): the four duties as cells with the spellings'
open row; fear-serve-swear; the test; the right and the good; the son's answer as the readback's third form; the receipt without the Name. NOT
COMMITTED (since 7c8554e; the message drafted). NEXT on the ruling: the commit; then 4b in four runs, or the schema sitting, on the owner's word.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; chapters 1-5 COMPILED (7c8554e); SITTING 4 DONE 2026-09-17 (ch 6 FROZEN, 220 units; uncommitted); NEXT: commit, then 4b\n'
DESC_OLD = 'map World/step9/DEUTERONOMY_WALK.md; SITTING 3b DONE 2026-09-16'
DESC_NEW = 'map World/step9/DEUTERONOMY_WALK.md; SITTING 4 DONE 2026-09-17 (chapter 6 READ AND FROZEN as one unit, the 220th; the Sifrei on the Shema; the first sitting in four runs; uncommitted); SITTING 3b DONE 2026-09-16'
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 4 — chapter 6's reading in four runs; the state doc #190 addendum 3)
- NUMBERS CLOSED. DEUTERONOMY 1:1-5:33 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-3b); 6:1-25 READ AND FROZEN (sitting 4).
- 220 frozen units, standing 2203, hash 8b8fff1fa28953af. 60 runners, 65 daemons, 448 functions; registries 1122 kinds / 1023 effects.
- THE TAPE unmoved since 3b (markers 167, closes 127, the counter (40, 11, 1)); the sweep 60/60; every gate GREEN; the register gate
  DECLARED {R_DECL} / DEBT 0 (no seat in chapter 6).
- CHAPTER 6'S FINDS: the Sifrei's piskaot 31-36 ON 6:4-9; the export's two files DIVERGE at 36:10; the shelf's four compartments need 11:18
  "frontlets" defective where the ink is plene (the compile's open row); the large letters a PARKED hypothesis.
- LAST COMMIT 7c8554e (NOT pushed). Uncommitted: sitting 4 whole; the message drafted at <scratch>/commit_msg_ch6.txt.
- NEXT ON HIS WORD: the commit; then 4b — THE COMPILE OF CHAPTER 6 in four runs (COMPILE_DEBT's box (a)-(l); the design first); or the schema.
'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', f'{MEM}/MEMORY.md']
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
ANCH = [(f'{ROOT}/World/RESUME.md', '# ⚠ THE DEUTERONOMY WALK sitting 3b (2026-09-16;'), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-16, latest)\n'), (f'{ROOT}/THE_BRIEFING.md', '- **CHAPTER 5 COMPILED — THE CODE SAID AGAIN'), (f'{ROOT}/THE_BRIEFING.md', '### 2026-09-16 — CHAPTER 5 COMPILED: THE CODE GRADED AGAINST THE CODE'), (f'{ROOT}/logic/MIDDOT.md', '\n## Exodus block campaign — owner\'s word "Do 3")\n'), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (RECP, 'the newest instances: the map\'s "Sitting 3" and "Sitting 3b"'), (RECP, '- Deuteronomy\'s sittings: the map; the addenda §31-37. The cost cuts: §35.'), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START), (f'{MEM}/deuteronomy-walk.md', DESC_OLD)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
assert '## Sitting 4 — CHAPTER 6 — AS BUILT' not in rd(WALKP) and 'RUN 3 — AS RUN' in rd(WALKP) and '#190 ADDENDUM 3' not in rd(TOUCH[1]) and '## 38. ADDENDUM' not in rd(TOUCH[9]) and 'SITTING 4 DONE' not in rd(f'{MEM}/deuteronomy-walk.md') and 'DEUTERONOMY SITTING 4 — CHAPTER 6' not in rd(TOUCH[5]) and f'| {DATE} | {UID} |' not in rd(TOUCH[0])
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
REC_NEW = REC_NEW.replace('the newest instances: the map\'s "Sitting 3" and "Sitting 3b"', 'the newest instances: the map\'s "Sitting 4" and "Sitting 3b"').replace('- Deuteronomy\'s sittings: the map; the addenda §31-37. The cost cuts: §35.', '- Deuteronomy\'s sittings: the map; the addenda §31-38. The cost cuts: §35.')
assert len(REC_NEW.encode()) <= 10240, len(REC_NEW.encode())
m = rd(f'{MEM}/MEMORY.md'); i = m.index(MEMLINE_OLD_START); j = m.index('\n', i) + 1; MEM_NEW = m[:i] + MEMLINE_NEW + m[j:]
assert len(MEM_NEW.encode()) < 17000, len(MEM_NEW.encode())
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()}, '| recovery page bytes', len(REC_NEW.encode()), '| MEMORY.md bytes', len(MEM_NEW.encode()))
if CHECK: print('CHECK ONLY — nothing written'); sys.exit(0)
# ---- THE WRITES ----
append(TOUCH[0], STAMP)
append(WALKP, WALK)
append(TOUCH[1], STATE)
insert_before(TOUCH[2], '# ⚠ THE DEUTERONOMY WALK sitting 3b (2026-09-16;', RESUME_NOTE)
insert_before(TOUCH[3], '\n## Step 6 — Publish\n', STEPS)
replace_once(TOUCH[4], '## SCOREBOARD (as of 2026-09-16, latest)\n', f'## SCOREBOARD (as of {DATE}, latest)\n')
insert_before(TOUCH[4], '- **CHAPTER 5 COMPILED — THE CODE SAID AGAIN', BRIEF)
insert_before(TOUCH[4], '### 2026-09-16 — CHAPTER 5 COMPILED: THE CODE GRADED AGAINST THE CODE', BRIEF_ENTRY)
append(TOUCH[5], DEBT)
append(TOUCH[6], RESEARCH)
insert_before(TOUCH[7], '\n## Exodus block campaign — owner\'s word "Do 3")\n', MIDDOT)
open(RECP, 'w', encoding='utf-8').write(REC_NEW); print('recovery page rewritten', len(REC_NEW.encode()), 'bytes')
append(TOUCH[9], ADDENDA)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
replace_once(f'{MEM}/deuteronomy-walk.md', DESC_OLD, DESC_NEW)
open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(MEM_NEW); print('MEMORY.md', len(MEM_NEW.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0 and len(rd(RECP).encode()) <= 10240
print('records written; the lints at or under their baselines; the map and the memory file lint 0; the page under its cap')
