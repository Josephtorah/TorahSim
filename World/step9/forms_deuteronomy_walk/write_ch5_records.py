#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3 — CHAPTER 5 (2026-09-16; the owner: "go" after the rereads): THE RECORDS at the close, from the sheet
# World/step9/RECORD_FORMS.md in ONE call — the map's "Sitting 3" section, COMPILE_DEBT's box (owed to the compile 3b), MIDDOT's block (the
# Sifrei's case law on the chapter), RESEARCH_LOG's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, RESUME's note, the state doc's
# #187 addendum 1, the recovery page's section 2 (the whole file rewritten, under 10 KB), the recovery addenda's section 36, the stamp row, the
# memory file and the index line (under 17,000 bytes). Every number parsed from a print named beside it (--check prints them and writes nothing);
# every insert on a unique anchor asserted present once; the lints before and after. Sitting 2's form (write_ch4_records.py) on the sheet.
import os, re, subprocess, sys, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-16'
UID = 'deu_05_decalogue'
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
# ---- THE NUMBERS, PARSED FROM THE PRINTS ----
truth = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py')
assert 'assert len(W["units"]) == 219' in truth and 'assert len(W["standing"]) == 2197' in truth and "8b8fff1fa28953af" in truth
CT = rd(f'{SP}/corpus_truth_ch5.out'); CB = rd(f'{SP}/corpus_bake_ch5.out')
rit = rd(f'{SP}/ch5_ritual_{UID}.out'); N_PASS = len(re.findall(r'^PASS', rit, re.M))
assert 'RITUAL COMPLETE' in rit and N_PASS == 13 and not re.search(r'^FAIL', rit, re.M), N_PASS
vt = rd(f'{SP}/ch5_vt_{UID}.out')
assert '  status: frozen' in rd(f'{ROOT}/logic/units/{UID}.yaml') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json') and 'ALL_DONE' in rd(f'{SP}/ch5_chain.log')
JG = rd(f'{SP}/journal_gate_ch5.out'); RG = rd(f'{SP}/register_gate_ch5.out'); BW = rd(f'{SP}/build_world_ch5.out'); CL = rd(f'{SP}/ch5_close.out')
assert 'GATE GREEN' in JG and 'ALL GREEN' in BW and 'scrub exit 0' in CL and 'FOLD_DONE' in CL, (JG[-200:], BW[-200:])
mj = re.search(r'(\d+) kinds, ([\d,]+) rows', JG); J_KINDS, J_ROWS = mj.group(1), mj.group(2)
mr = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', RG); R_DECL, R_DEBT, R_FAIL = mr.groups()
assert R_DEBT == '0' and R_FAIL == '0', mr.groups()
mc = re.search(r'(\d+) units.*?(\d+) facts.*?(\d+) demands.*?\((\d+) open\)', CT + CB, re.S)
LED = rd(f'{ROOT}/logic/oral_triage/deu_05_vaetchanan_{DATE}.md')
ml = re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\* \((\d+) Onkelos verses and (\d+) Sifrei rows.*?MATERIAL (\d+) Onkelos, CONTEXT (\d+) Onkelos, MATERIAL (\d+) Sifrei, CONTEXT (\d+) Sifrei', LED, re.S)
L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC = ml.groups()
L_BYTES = len(LED.encode())
d_ov = yaml.safe_load(rd(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'))
OV_REF5 = len([k for k in d_ov['by_ref'] if k.startswith('Deut.5.')]); OV_REF, OV_GL = len(d_ov['by_ref']), len(d_ov['by_gloss'])
assert OV_REF5 == 58 and OV_REF == 472 and OV_GL == 352, (OV_REF5, OV_REF, OV_GL)
N_CLAIMS = len(__import__('json').load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8')))
print('PARSED:', dict(ritual_pass=N_PASS, verify_text_tail=vt.strip().split('\n')[-1][:80], journal=(J_KINDS, J_ROWS), register=(R_DECL, R_DEBT, R_FAIL), corpus=mc.groups() if mc else CT[-160:], ledger=(L_ALL, L_ONK, L_SIF, L_OM, L_OC, L_SM, L_SC, L_BYTES), overrides=(OV_REF5, OV_REF, OV_GL), claims=N_CLAIMS))
C_UNITS, C_FACTS, C_DEM, C_OPEN = mc.groups() if mc else ('219', '?', '?', '?')
assert C_UNITS == '219', C_UNITS

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

STAMP = (f'| {DATE} | {UID} | DELEGATED | FULL RULE | Deuteronomy 5:1-33 derivation {DATE} (THE DEUTERONOMY WALK sitting 3 — CHAPTER 5; the owner: "go" after the rereads, on the rulings READ THEN COMPILE PER PORTION and CHAPTER NUMBERS NOT PORTION NAMES; the book\'s third reading — chapter 5 as one draft, the 219th frozen unit): declared reading COMPLETE (one ledger logic/oral_triage/deu_05_vaetchanan_{DATE}.md, {L_ALL} sources — Onkelos 5:1-33 whole and fresh through the map of the two divisions (the export\'s thirty rows against the DB\'s thirty-three: its 17 the DB\'s 17-20, computed by a monotone alignment over token and negation counts), the Sifrei on Deuteronomy\'s FIVE rows citing the chapter found by the scan of the whole export in both files and read fresh (41:1, 41:4, 233:1, 306:16, 357:40), one credited from sitting 1 (20:1); NO PISKA on the chapter — 30 heads on 3:29, 31 on 6:4; coverage computed by script, missing 0 extra 0; the ink facts computed from the Tanakh DB, the snapshot store and the shelf\'s bytes — every fact an assert, three fell on the first typed pass (a Hosea citation inside a continuation row, Job\'s count, the two spellings of "forever") and were retyped from the print, none after; every quotation cut by consonants, no cut miss; gloss_lint 0), claims DV05-01..06 verified {N_CLAIMS}/{N_CLAIMS} (every check the word\'s longest store-piece whole), claim_labels_census --strict GREEN, seated as six WITNESS_READ operators at the claims\' first verses (5:1, 6, 12, 16, 22, 28), verify_text GREEN (33 steps, 7 scenarios), the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2197 = 2191 + 6 as predicted, hash 8b8fff1fa28953af UNMOVED), build_world ALL GREEN, the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}). THE PARSER: three number verses read, NO GAP (5:13 [6], 5:14 the ordinal [7], 5:22 [2]); 5:9\'s third generation STARRED, not thirty. THE TWO COPIES DIFFED verse by verse (172 tokens and 620 letters at Exodus 20:2-17 against 189 and 708 at 5:6-21): five verses verbatim, one letter at 5:8, the ketiv at 5:10 (the chapter\'s one written-and-read pair — "his" written, "my" read), KEEP for REMEMBER at 5:12 with the receipt "as the LORD your God commanded you" (5:12, 5:16 — the register gate\'s seats), the two beasts and the servants\' rest at 5:14, the ground changed whole at 5:15 (the exodus for the creation), "and" on the four short words, the VAIN witness for the FALSE, the wife first and a second verb at 5:21. The finds: the two divisions; face to face the Bible\'s one seat (Onkelos "speech with speech", the Memra between); the ten words in the singular; the Sifrei 233:1\'s "remember and keep in one utterance"; "added no more" read "did not cease"; the mob and the elders (1:22, 5:23); "we will hear and do" against "we will do and hear"; Moses standing (Sifrei 357:40); the first copy never read on its spine. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = f'''

## Sitting 3 — CHAPTER 5, Deuteronomy 5:1-33 (2026-09-16; the owner: "go" after the rereads, on the rulings READ THEN COMPILE PER PORTION and CHAPTER NUMBERS): the reading and the unit

THE DRAFT: one covers the chapter exactly — computed from the Tanakh DB's verse table: 33 of 33 verses, missing 0 — deu_05_decalogue 5:1-33 (the
next draft, deu_06_shema, opens at 6:1; the step ids STEP_Dt_5_<v>; the scenarios in the tree form before the seat; 70 "comment" lines, two per
step and four of the log, counted from the print). The chapter is the sitting's unit, per the ruling. Read in ONE pass, one ledger. The forms:
sitting 2's scripts edited (ch5_dump0.py with THE ALIGNMENT as its first section; ch5_measure1.py — the two copies diffed, the censuses, the
Onkelos seats, the gloss families; ch5_ink.py with assert_driver.py and deu_legs.py; ch5_rows_onkelos_a/b.py; ch5_rows_sifrei.py;
write_ch5_ledger.py; ch5_patch_overrides.py; write_ch5_manifest.py; seat_ch5.py; ch5_chain.sh; copy_ch5_forms.py; write_ch5_records.py — the
records from the sheet RECORD_FORMS.md in one call), copied at the close into World/step9/forms_deuteronomy_walk/ with their prints.

THE TWO DIVISIONS, MEASURED FIRST (the owner's word for the sitting): Onkelos Deuteronomy's export gives chapter 5 THIRTY verses against the DB's
THIRTY-THREE — the one chapter of the book where they disagree. THE MAP COMPUTED, never typed: a monotone alignment of the export's thirty rows to
the DB's thirty-three over token counts and negation counts (the cost 27): the export's 1-16 are the DB's 1-16; ITS 17 IS THE DB'S 17-20 — the four
short words (murder, adultery, theft, false witness) one row in the export, twelve tokens and four negations against the DB's 2+2+2+5 and four;
its 18 the DB's 21; its 19-30 the DB's 22-33 (the offset three). Every export address in the sitting is mapped: the Sifrei's citations "(דברים ה
כ)" ("Deuteronomy 5:20") = the DB's 5:23, "ה יט" = 5:22, "ה כח" = 5:31; the Onkelos rows are read by the DB's verse (5:18-20 on the export's row
17, the Aramaic quoted once at 5:17); the ink module recomputes the alignment and asserts the map (ch5_ink.py). The recorder and the stitcher
address verses by the DB — the compile inherits the map for the shelf's citations only.

THE SHELF, BY POSITION (ch5_ink.py's asserts): THE SIFREI ON DEUTERONOMY HAS NO PISKA ON CHAPTER 5 either — piska 30 heads on 3:29, piska 31 on
6:4; no head in chapters 4 or 5 (computed on all 357 heads). THE "FOUND BY POSITION" CLAUSE the whole spine again: the whole export scanned in
both files — FIVE Hebrew rows cite chapter 5, SIX English: 20:1 (on 1:22; the mob and the elders — 5:23), 41:1 (on 11:13; 5:1), 41:4 (on 11:13;
5:1 — THE ENGLISH'S ALONE: a continuation row whose Hebrew quotes the verse whole with no parenthesis and cites only Hosea 4:1 — a FOURTH form of
the export's citation habit, after sitting 2's three), 233:1 (on 22:11; 5:12 WITH Exodus 20:8 — the two copies cited together), 306:16 (on 32:2;
5:22), 357:40 (on 34:10; 5:31). THE PRIOR READS (213 prior rows): 20:1 read FRESH at sitting 1 — CREDITED here; the five others FRESH in both
files; no ledger had read an Onkelos row of chapter 5, AND NONE OF EXODUS 20 — the first copy was read EXAM-FIRST (2026-09-04), never
spine-by-position; twenty ledgers name a verse of Exodus 20 and ten a verse of Deuteronomy 5 (names, not reads).

THE INK, COMPUTED (the measurement passes FIRST — ch5_dump0.py, ch5_measure1.py — the asserts typed from the print; three fell on the first typed
pass: a Hosea citation inside 41:4 read as "no citation", Job's "who would give" nine not ten, "forever" spelled two ways in the book; each retyped
from the leg print; none after):
- THE PARSER MEASURED FIRST: THREE number verses in 33 read, NO GAP — 5:13 "six days" [6], 5:14 "the seventh day" the ordinal [7], 5:22 "two
  tablets of stone" [2] (the construct marked ^); 5:9's "the third generation" STARRED — not thirty (rule 15: no holam under the lamed; the pointed
  form שִׁלֵּשִׁים "third-generation ones" the same at all five seats); 5:10's "to thousands" a bare plural, no number (1b's rule); the same phrases
  read the same elsewhere (six days [6] at all twelve Torah seats; 7:9 [1000]; 9:10, Exodus 31:18 [2]; 10:4 [10] and "the first" [1]; 4:13 [10, 2]).
  The tokens 472; THE STORE'S TOKENS THE DB'S AT EVERY VERSE BUT ONE — 5:10, the chapter's written-and-read pair (the DB's "his commandments"
  flagged x-ketiv, one of the Bible's 1,268; the store's seventh token the read "my"; Exodus 20:6 writes "my").
- THE TWO COPIES DIFFED, verse by verse against Exodus 20:2-17 in the DB's division: five verses VERBATIM (6, 7, 11, 13, 17); ONE LETTER at 5:8
  ("any form" for "and any form"); 5:9 "fathers" plene, "AND upon the third"; 5:10 the ketiv; 5:12 KEEP for REMEMBER and the receipt "AS THE LORD
  YOUR GOD COMMANDED YOU" added; 5:14 "AND your servant", "YOUR OX AND YOUR ASS AND ALL your cattle", "THAT YOUR SERVANT AND MAIDSERVANT MAY REST
  LIKE YOU" (twenty-six words for eighteen); 5:15 THE GROUND CHANGED WHOLE — the exodus for the creation; 5:16 the receipt and "AND THAT IT MAY GO
  WELL WITH YOU"; 5:18-20 "AND not"; 5:20 a VAIN witness for a FALSE; 5:21 the wife first, DESIRE for the second "covet", HIS FIELD. The counts
  172 tokens / 620 letters against 189 / 708 (the peer thread's numbers of 2026-09-16 confirmed on the DB).
- THE FRAMES AND THE REGISTER: ONE divine frame ("and the LORD said to me", 5:28); ONE "saying" — Moses' at 5:5, opening the ten words; THE TEN
  WORDS IN THE SINGULAR (singular only 6-9, 11-21; plural only 4, 5, 22-24, 32, 33); TWO INFINITIVE ABSOLUTES, "keep" (5:12) and "honor" (5:16);
  TWELVE PROHIBITIONS; the case tokens "for" eight, ONE "if" (5:25, the people's), no "lest", no "or"; the first person Moses' and the LORD's by
  turns inside one report. THE REGISTER GATE: Deut 5:12, 5:16, 5:32 NONE declared — the receipts inside the ten words and the closing plural
  receipt, paid at the compile.
- THE CROWNS (fourteen, the ledger's finds): THE TWO DIVISIONS; THE SECOND COPY DIFFED; THE RECEIPT INSIDE THE CODE; KEEP AND REMEMBER IN ONE
  UTTERANCE (the Sifrei 233:1 — the shelf naming the diff's first word; the Mekhilta, Bahodesh 7, the first copy's spine, unopened); THE WRITTEN
  AND THE READ AT 5:10; FACE TO FACE, ONE SEAT (5:4 the Bible's one "face IN face"; Onkelos "speech with speech", the Memra between at 5:5); THE TEN
  WORDS IN THE SINGULAR; THE THIRD GENERATION STARRED; ADDED NO MORE, DID NOT CEASE (5:22 — four seats of the phrase; Onkelos the unending voice;
  the tablets defective here, plene at 4:13); THE MOB AND THE ELDERS ("you came near to me" 1:22 and 5:23 alone; "the LORD heard the voice of your
  words" 1:34 and 5:28 alone); WE WILL HEAR AND DO (5:27 against Exodus 24:7's order; Onkelos "accept and do"); STAND HERE WITH ME (5:31; the
  Sifrei 357:40 — Moses standing, Balaam fallen); THE FIRST COPY UNREAD ON THE SPINE; THE SIFREI'S SIX ROWS (41:4 by the English file alone).

THE SIFREI'S OWN CASE LAW (the block in MIDDOT.md, five rows): the study before the deed (41:1 on 11:13 from 5:1, I2's form); the deed hangs on the
study (41:4, E12's kin — Hosea 4:1 the weight); "remember" and "keep" in one utterance (233:1 on 22:11-12 with 5:12 and Exodus 20:8, I13's kin);
"words" are words of Torah (306:16 on 32:2 from 5:22, E7); Moses prophesied standing (357:40 on 34:10 from 5:31, E28's kin with E26's parable).
MOVE_CATALOG unchanged; MISHNAH_TOPICS unchanged (no Mishnah opened at a reading sitting — the tractates routed to the docket).

THE CLAIMS (write_ch5_manifest.py → one manifest, {N_CLAIMS} claims DV05-01..06 — 5:1-5 the covenant at Horeb, 6-11 the first words, 12-15 the
sabbath word, 16-21 honor and the five, 22-27 the voice and the request, 28-33 the answer and the charge — every check the word's LONGEST
STORE-PIECE WHOLE (5:4 "face in face", 5:7 "other", 5:12 "keep", 5:21 "desire", 5:22 "and he wrote them", 5:28 "they have done well"); the ID prefix
asserted absent; every cite checked against the ledger's CITE INDEX and every name of the index used, asserted): verify_claims {N_CLAIMS} VERIFIED /
0 FAILED; claim_labels_census --strict GREEN on the first run. THE SEATS (seat_ch5.py): six WITNESS_READ operators at the claims' first verses (5:1,
6, 12, 16, 22, 28), step E, the scenarios in the anchor form; verify_text GREEN (33 steps, 7 scenarios). THE RITUAL (ch5_chain.sh — the chain's ROOT
from the cwd's git after a first run with an empty ROOT found the tools at "/logic/…"; the seat once, the chain rerun past it): {N_PASS} PASS — RITUAL
COMPLETE for the 219th frozen unit; the Python rendering layer written and self-proved. THE CORPUS REBAKED (predicted before the fold: units 219,
standing 2191 + 6 = 2197, hash unmoved — the tripwire's literals set to the prediction before the bake): CORPUS TRUTH GREEN — {C_UNITS} units,
{C_FACTS} facts, {C_DEM} demands ({C_OPEN} open), hash 8b8fff1fa28953af — the prediction matched; build_world ALL GREEN; the journal gate GREEN
({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL} — the chapter's three seats
standing as filed until the compile); the home-path gate GREEN. THE STAMP: one delegated FULL RULE row (logic/findings/STAMP_LEDGER.md). THE DISPLAY
LAYER: {OV_REF5} rows by reference and 54 by gloss (by_ref {OV_REF}, by_gloss {OV_GL} after). No engine file changed at this sitting — the sweep as at
2b's close. THE LEDGER: {L_ALL} sources — Onkelos MATERIAL {L_OM} / CONTEXT {L_OC}, the Sifrei MATERIAL {L_SM}; {L_BYTES:,} bytes; gloss_lint 0 on the
first write.

OWED TO THE COMPILE (sitting 3b; the box in COMPILE_DEBT.md, items (a)-(k)): THE LAWS' READBACK — the second copy 5:6-21 a REFERENCE ROW per word
graded against the DECALOGUE RUNNER'S CELLS (code against code, the readback's form (R1)-(R6) on law, not narrative: VERBATIM 5:6, 5:7, 5:11, 5:13,
5:17; EXPANDED 5:12, 5:14, 5:16; the ground TURNED at 5:15; the wife first at 5:21 — each row's cell named); THE SECOND WORD (the 2b box's debt:
Exodus 20:3-6 has no cell in any runner — 5:7-10 its second copy, 4:16-19 its parameter table; the sitting that compiles it, or the schema's);
THE RECEIPTS' SEATS (Deut 5:12, 5:16 — "as the LORD your God commanded you" INSIDE the ten words: a law citing its prior giving — RUN_CITATION of
Exodus 20:8 and 20:12 on the tape; 5:32 the plural — the class declared from the tape); THE KETIV AT 5:10 (a DATA note: the written "his" the DB's
token, the read "my" the store's — no line, no cell moves); THE SABBATH'S TWO GROUNDS (the fourth word's parameter table carries the creation at
Exodus 20:11 and the exodus at 5:15 — a DATA row, the readback's TURNED); THE VAIN WITNESS (5:20 against Exodus 20:16's false witness — the ninth
word's parameter, Onkelos levelling it; the cell's ink names both); THE VOICE AND THE TABLETS (5:22 retells the two lines 2b wrote by retrograde
markers — ten_words_declared (1, 3, 7), tablets_given (1, 4, 17): the readback's rows FOUND on the running world, no new write; "added no more" a
DATA note with Onkelos's "did not cease"); THE PEOPLE'S REQUEST (5:23-27 against Exodus 20:18-21 and 24:3-7 — reference rows; "we will hear and do"
against the covenant's "do and hear" a REFERENCE the ink makes, the Mekhilta's and Shabbat 88a's the docket's); THE ANSWER AND THE CHARGE (5:28-31
— "they have done well" cited at 18:17 forward; 5:31 the charge that opens Moses' teaching at 6:1: the block's edge (Deut 4:45, Deut 5:33] and
whether chapter 5 installs a daemon at all — the reading found no law of its own outside the copy, 5:32-33 the frame's charge); THE CHAPTER-5
DIVISION IN THE COMPILE (the recorder and the stitcher by the DB's verses; the shelf's citations through the map); THE DOCKET by the union rule
(the TESTING paragraph's tractates: the Decalogue exam's rows on the first copy; Shevuot 3:8-9; Shabbat 88a; Sanhedrin 17a; Makkot 24a; Berakhot
12a; Kiddushin 30b-31b; Sanhedrin 86a; Bava Metzia 5b; Yoma 4b, Sotah 37b; 5:3's and 5:29's open topics); THE SCHEMA SITTING ON THE TABLE (its
seat this chapter — the Sifrei 233:1 the tradition's own filing of one commandment's two seats under one header, an exhibit for the first decision).

⚠ LESSONS (7): THE EXPORT'S DIVISION IS MAPPED BY AN INSTRUMENT — a monotone alignment over token and negation counts found the fold (17 = 17-20)
with no table typed; assert the map, then address everything by the DB. A CONTINUATION ROW CITES IN ONE FILE ONLY — 41:4's Hebrew quotes the verse
with no parenthesis; the scan's union of both files is the finder, and a Hebrew regex for "no citation" must exclude other books' cites (the first
fallen assert). A CHAIN'S ROOT COMES FROM THE CWD'S GIT — a scratch script's own folder is not the repo; the first chain found "/logic/…" and the
seat had already written, so the chain reruns past the seat (an idempotent seat step: skip when operators are present). A SED ON A FORM RENAMES BY
WHOLE WORDS — "ch4_" left "seat_ch4.py" untouched and the chain ran the old seat (a KeyError, nothing written); grep the derived script for the old
name before running it. THE SPELLING SPLITS A CENSUS — "forever" plene and defective in one book (23:7 against 5:29, 32:40); a token census is per
spelling, type both. THE ROWS IN THREE FILES, THE CUTS CHECKED AT LOAD — 38 rows, no cut miss on the first load (the consonants typed from the
dump's own lines). THE READING SHAPE HELD ON THE DECALOGUE'S COPY: measure (the alignment, the diff) → asserts (3 → 0) → rows (33 + 5) → writer (lint
0) → patch (58 + 54) → manifest (6/6, the labels gate first run) → seat → the ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF CHAPTER 5 (sitting 3b) on the walk's order — the measurements (the tape's state at Deut 4:49; the decalogue
runner's cells and the ten words' line; the register gate's seats 5:12, 5:16, 5:32), THE DESIGN in this file before any code (the laws' readback
per word; the receipts; the block's edge), the probes to FAIL, the runner or the reference rows, the tape, the gates chain, the sweep — or THE
DECALOGUE-SCHEMA SITTING first, on the owner's word (its seat this chapter; the first decision: a filing under a header a REFERENCE or a cited
TRANSFER). Then chapter 6, and on in order.
'''

DEBT = f'''
## DEUTERONOMY SITTING 3 — CHAPTER 5, Deuteronomy 5:1-33 READ AND FROZEN ({DATE}; DEUTERONOMY_WALK.md "Sitting 3"; the ledger deu_05_vaetchanan_{DATE}.md,
## {L_ALL} sources; one unit deu_05_decalogue FROZEN, the 219th) — OWED TO THE COMPILE (sitting 3b): (a) THE LAWS' READBACK — the second copy 5:6-21 a
## REFERENCE ROW per word graded against the decalogue runner's cells, code against code (VERBATIM 5:6, 7, 11, 13, 17; EXPANDED 5:12, 14, 16; the
## ground TURNED at 5:15; the wife first at 5:21); (b) THE SECOND WORD — Exodus 20:3-6 with no cell in any runner (the 2b box's debt; 5:7-10 its
## second copy, 4:16-19 its table); (c) THE RECEIPTS' SEATS — Deut 5:12, 5:16 NONE ("as the LORD your God commanded you" INSIDE the ten words: a law
## citing its prior giving — RUN_CITATION of Exodus 20:8, 20:12) and 5:32 the plural; (d) THE KETIV AT 5:10 — "his" written, "my" read: a DATA note,
## no line; (e) THE SABBATH'S TWO GROUNDS — the creation (Exodus 20:11) and the exodus (5:15) in the fourth word's parameter table; (f) THE VAIN
## WITNESS — 5:20 against 20:16's false witness, the ninth word's parameter (Onkelos levels it); (g) THE VOICE AND THE TABLETS — 5:22's two lines
## already on the tape by 2b's retrograde markers (1, 3, 7) and (1, 4, 17): FOUND, no write; "added no more" a DATA note ("did not cease"); (h) THE
## REQUEST AND THE ANSWER — 5:23-31 reference rows against Exodus 19-20, 24 and 1:22, 1:34; "hear and do" against "do and hear" (Exodus 24:7) a
## REFERENCE; "they have done well" cited forward at 18:17; (i) THE BLOCK'S EDGE — 5:31 the charge that opens Moses' teaching at 6:1; whether chapter
## 5 installs any daemon (the reading found no law of its own outside the copy); the block (Deut 4:45, Deut 5:33]; (j) THE DOCKET by the union rule —
## the Decalogue exam's rows on the first copy (2026-09-04), Shevuot 3:8-9, Shabbat 88a, Sanhedrin 17a, Makkot 24a, Berakhot 12a, Kiddushin 30b-31b,
## Sanhedrin 86a, Bava Metzia 5b, Yoma 4b, Sotah 37b; 5:3's "not with our fathers" and 5:29's "who would give" open topics; (k) THE SCHEMA SITTING ON
## THE TABLE — its seat this chapter; the Sifrei 233:1 (remember and keep in one utterance) the tradition's own filing of two seats under one header,
## the exhibit for the first decision (REFERENCE or cited TRANSFER). NOTHING ELSE IN CHAPTER 5 IS OWED TO A LATER SITTING OF ITS OWN.
'''

MIDDOT = f'''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 5 (Deuteronomy 5:1-33; THE DEUTERONOMY WALK sitting 3, {DATE};
  the ledger logic/oral_triage/deu_05_vaetchanan_{DATE}.md — NO PISKA on the chapter, its five fresh rows found by citation in
  the whole export, each read in both files):**
  · THE STUDY BEFORE THE DEED (41:1 on 11:13 from 5:1 "and you shall learn them and keep to do them"): the doubt whether the
    duty to study waits on the duty to do, closed by 11:13's "hearken" — I2's form, a REFERENCE the Sifrei draws by the verb.
  · THE DEED HANGS ON THE STUDY (41:4 on 11:13 from 5:1): the order of two verbs in one verse read as a dependency, Hosea 4:1's
    three absences (truth, kindness, KNOWLEDGE) the weight of the punishment — E12's kin (the sequence of the ink as its logic);
    the row's Hebrew cites nothing of Deuteronomy, the English "(Dt.5:1)" — found by the English file alone.
  · REMEMBER AND KEEP IN ONE UTTERANCE (233:1 on 22:11-12 with 5:12 and Exodus 20:8): the two copies' first divergent word declared
    one saying, beside the mingled stuff and the fringes — I13's kin (the contradiction resolved by one voice, not a third verse);
    the Mekhilta, Bahodesh 7, named by the export's footnote — the first copy's spine, unopened by any ledger.
  · "WORDS" ARE WORDS OF TORAH (306:16 on 32:2 from 5:22 "these words the LORD spoke"): the ten words the lexicon entry for the
    word — E7 (the term fixed from its defining seat, the Sifrei's "nothing but"); the row cites the export's 5:19 = the DB's 5:22.
  · MOSES PROPHESIED STANDING (357:40 on 34:10 from 5:31 "stand here with me"): Moses against Balaam seat by seat (who spoke, when,
    in what posture) — E28's kin, with E26's parable of the king's cook; the row cites the export's 5:28 = the DB's 5:31.
'''

RESEARCH = f'''
## {DATE} — DEUTERONOMY 5 READ (THE DEUTERONOMY WALK sitting 3 — CHAPTER 5): THE TWO DIVISIONS MAPPED BY ALIGNMENT; THE SECOND COPY OF THE TEN WORDS DIFFED
## VERSE BY VERSE — FIVE VERBATIM, THE GROUND OF THE SABBATH CHANGED WHOLE, THE RECEIPT INSIDE THE CODE; KEEP AND REMEMBER IN ONE UTTERANCE (THE SIFREI 233:1);
## THE WRITTEN AND THE READ AT 5:10; FACE TO FACE THE BIBLE'S ONE SEAT; THE THIRD GENERATION STARRED; THE FIRST COPY NEVER READ ON ITS SPINE

THE TWO DIVISIONS MAPPED BY ALIGNMENT. Onkelos Deuteronomy's export gives chapter 5 thirty verses; the DB (the Open Scriptures text) thirty-three.
A monotone alignment over token counts and negation counts (the cost 27) found the fold with no table typed: the export's 17 holds the DB's 17-20
(twelve tokens, four negations — the four short words one row), then the offset of three to the chapter's end. Every citation of the shelf on the
chapter is read through the map (the Sifrei's "5:19" is the DB's 5:22; its "5:28" the DB's 5:31), the Onkelos rows by the DB's verse; the ink module
recomputes and asserts the map. The recorder and the stitcher address the DB.

THE SECOND COPY DIFFED. Deuteronomy 5:6-21 against Exodus 20:2-17, token by token in the DB's division: 5:6, 7, 11, 13, 17 VERBATIM; one letter at
5:8 ("any form" for "and any form"); 5:9 "fathers" plene, "and upon the third"; 5:10 "his commandments" written for "my"; 5:12 KEEP for REMEMBER and
"as the LORD your God commanded you" added; 5:14 "and your servant", "your ox and your ass and all your cattle", "that your servant and maidservant
may rest like you" (26 words for 18); 5:15 the whole ground — the slave in Egypt and the exodus for the six days of creation, the diff keeping "for",
"the LORD", "therefore", "the sabbath day"; 5:16 the receipt and "and that it may go well with you"; 5:18-20 "and not"; 5:20 a VAIN witness for a
FALSE; 5:21 the wife first, "desire" a second root, "his field". The counts 172 tokens / 620 letters against 189 / 708 (the peer thread's figures of
2026-09-16 confirmed on the DB). The compile grades the copy as CODE AGAINST CODE — a reference row per word against the decalogue runner's cells.

THE RECEIPT INSIDE THE CODE. "As the LORD your God commanded you" at 5:12 and 5:16 — a law citing its own prior giving, absent from the first copy
(20:17 the third seat); the register gate's seats Deut 5:12, 5:16 (and 5:32's plural) filed NONE at Numbers meet their verses — RUN_CITATIONs of
Exodus 20:8 and 20:12 on the tape, paid at the compile.

KEEP AND REMEMBER IN ONE UTTERANCE. The Sifrei 233:1 (on the mingled stuff and the fringes) names the diff's first word: 5:12's "keep" and Exodus
20:8's "remember" were said as one — both infinitive absolutes on the morphology; the export's footnote sends to the Mekhilta, Bahodesh 7 — the first
copy's spine, which no ledger has opened (the Decalogue was read exam-first on 2026-09-04). The tradition filing one commandment's two seats under
one header: an exhibit for the schema question on the table.

THE WRITTEN AND THE READ AT 5:10. The DB's one token "his commandments" carries the flag x-ketiv (one of 1,268 in the Bible); the store holds the read
"my commandments" as a seventh token; Exodus 20:6 writes "my"; Onkelos reads "my". The chapter's one written-and-read pair — a DATA note for the compile.

FACE TO FACE, ONE SEAT. 5:4's "face IN face" is the Bible's one seat of the form (the five "face TO face" elsewhere — Jacob's, Moses' at the tent,
34:10, Gideon's, Ezekiel's); Onkelos "speech with speech", and at 5:5 "between the Memra of the LORD and you" — the mediator's verse resolving the
two by the Word. The ten words in the singular (the morphology: singular only 6-21), the frame plural before and after.

THE THIRD GENERATION STARRED. 5:9's "third" the parser marks by the missing holam — not thirty; the pointed form the same at all five seats (Joseph's
great-grandsons first); "to thousands" a bare noun; three number verses read (5:13 [6], 5:14 [7], 5:22 [2]), no gap.

ADDED NO MORE, DID NOT CEASE. 5:22's "and he added no more" (four seats — Judah, the angel, Samuel) read by Onkelos as "and did not cease"; the
tablets defective here, plene at 4:13; the two lines 5:22 retells (the ten words spoken, the tablets given) are on the tape since 2b's retrograde
markers. "You came near to me" 1:22 and 5:23 alone (the Sifrei 20:1: the mob and the elders); "the LORD heard the voice of your words" 1:34 and 5:28
alone; "we will hear and do" against Exodus 24:7's "do and hear"; "stand here with me" 5:31 (the Sifrei 357:40: Moses standing, Balaam fallen).

THE STORE'S GLOSSES READ BACK (the display layer): {OV_REF5} rows by reference and 54 by gloss — "the-intermission" THE SABBATH, "to-evil" IN VAIN,
"depress" BOW DOWN, "delight-in" COVET, "eye" for TESTIFY at 5:20 (by reference — the eye itself elsewhere), "be-heavy" for HONOR, "cut" for MADE a
covenant, "descendant-of-the-third-degr" THE THIRD GENERATION, "associate-you/your" YOUR NEIGHBOR, "along-with-me/my" WITH ME, "hinder" OTHER left
as rewritten at sitting 1; by_ref {OV_REF}, by_gloss {OV_GL} after.
'''

STEPS = f'''DEUTERONOMY — SITTING 3 — CHAPTER 5, Deuteronomy 5:1-33 ({DATE}, on Brian's "go" after the rereads; World/step9/DEUTERONOMY_WALK.md "Sitting 3").
The chapter where Moses says the ten words again. Before a row was written we measured the one thing the last sitting flagged: the translation's
copy of the chapter has thirty verses and our Bible has thirty-three. A small instrument lined the two up by counting words and "not"s, and found
the fold without anyone typing a table — the translation keeps the four short words (murder, adultery, theft, false witness) on one line. From
there every address in the sitting went through that map. Then the reading: Onkelos on every verse, the Sifrei's five rows that speak to the
chapter from elsewhere (it has no section of its own on chapters 4 or 5), and the two copies of the ten words laid side by side word for word.
Five verses match exactly. The differences are the finds: "keep" for "remember" on the sabbath, and the Sifrei says the two were spoken as one;
the sabbath's reason changes whole — creation there, the slave in Egypt here; the second copy twice says "as the LORD your God commanded you"
inside a commandment — a law citing its own earlier giving, which our register had been waiting to see; the false witness becomes a vain
witness; the wife is named before the house; one word is written "his" and read "my". The chapter is frozen as one unit, the 219th, every gate
green, the world's count of standing facts up by six as predicted and its hash unmoved. Next: the compile of chapter 5 — the laws read back as
code against code — or the ten-commandments schema first, on your word.

'''
BRIEF = f'''- **CHAPTER 5 READ AND FROZEN — THE TEN WORDS SAID AGAIN: FIVE VERSES MATCH EXACTLY, THE SABBATH'S REASON CHANGES WHOLE, AND TWICE THE LAW CITES ITS OWN GIVING** ({DATE}, on your "go" after the rereads; World/step9/DEUTERONOMY_WALK.md "Sitting 3"): the translation's thirty verses mapped to the Bible's thirty-three by an instrument before a row was written (the four short words one line there); Onkelos on all 33 verses, the Sifrei's five rows from elsewhere; the two copies diffed word for word — 172 words against 189; "keep" for "remember" (the Sifrei: one utterance), the exodus for the creation, the receipt "as the LORD your God commanded you" inside two commandments, the vain witness for the false, the wife first, "his" written and "my" read; one unit frozen (the 219th), 6 claims verified, the ritual 13 PASS, the world's standing facts 2197 (+6 as predicted), hash unmoved, every gate green. NEXT: the compile of chapter 5 (the laws read back as code against code), or the schema sitting first, on your word.
'''
BRIEF_ENTRY = f'''### {DATE} — CHAPTER 5 READ: THE TEN WORDS SAID AGAIN, AND THE DIFFERENCES ARE THE FINDS

Moses repeats the ten commandments, and for the first time the machine has both copies side by side, word for word. Before that could happen a
small problem had to be measured rather than guessed: the translation we read (Onkelos) divides this chapter into thirty verses and our Bible text
into thirty-three. An instrument lined them up by counting words and negations and found where the fold is — the translation keeps "you shall not
murder, commit adultery, steal, bear false witness" on one line where our text gives each its own verse. Everything else in the sitting went through
that map. The comparison itself: five verses are identical; the rest differ in small, deliberate ways. The sabbath commandment says "keep" instead
of "remember" (and the Sifrei says both were spoken in one breath), and its reason changes entirely — in Exodus the sabbath remembers creation, here
it remembers the slavery in Egypt. Twice the second copy says "as the LORD your God commanded you" inside a commandment: a law pointing back at its
own earlier giving. That matters for the machine, because our register of who-speaks-when had been waiting since Numbers to classify exactly those
two verses. One word is written "his" and read "my" — the only such pair in the chapter. The chapter is frozen as one unit, the world's count of
standing facts rose by six as predicted, and every gate is green. What comes next is the interesting part: at chapter 4 we graded a story against
the tape; at chapter 5 the readback grades code against code — the second copy of each commandment against the compiled cells of the first.

'''
RESUME_NOTE = f'''# ⚠ THE DEUTERONOMY WALK sitting 3 ({DATE}; step9/DEUTERONOMY_WALK.md "Sitting 3"): CHAPTER 5 READ AND FROZEN as one unit (the 219th —
# deu_05_decalogue 5:1-33): THE TWO DIVISIONS mapped by alignment (the export's 17 = the DB's 17-20, then the offset three); Onkelos on all 33
# verses through the map, the Sifrei's five rows by citation (no piska on the chapter); the two copies of the ten words DIFFED verse by verse (five
# verbatim; keep for remember; the exodus for the creation at 5:15; the receipts inside the words at 5:12, 5:16 — the register gate's seats; the
# ketiv at 5:10; the vain witness; the wife first); the ritual {N_PASS} PASS, CORPUS TRUTH GREEN ({C_UNITS} units, standing 2197 = 2191 + 6, hash
# unmoved), build_world, the journal gate ({J_KINDS} kinds, {J_ROWS} rows), the register gate --strict (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}) GREEN.
# NEXT on the ruling: the compile of chapter 5 (3b — the laws' readback, code against code) or the schema sitting first, on the owner's word.
'''
STATE = f'''
#187 ADDENDUM 1 ({DATE}, at the close of THE DEUTERONOMY WALK sitting 3 — CHAPTER 5's READING — A CLEAN COMPACTION POINT): THE SITTING RAN on the owner's "reread" then "go" in the reading shape on sitting 2's forms. THE FIRST MEASUREMENT (his word for the sitting): the export's thirty-verse chapter 5 against the DB's thirty-three — mapped by a monotone alignment over token and negation counts (ch5_dump0.py section A0; the ink recomputes and asserts it): the export's 17 = the DB's 17-20 (the four short words one row), 18 = 21, 19-30 = 22-33; every shelf citation and every Onkelos row read through the map. THE READING: 33 Onkelos rows + 5 fresh Sifrei rows (41:1, 41:4, 233:1, 306:16, 357:40) + 20:1 credited — the ledger deu_05_vaetchanan_{DATE}.md ({L_ALL} sources, {L_BYTES:,} bytes, lint 0); the two copies of the ten words diffed verse by verse (five verbatim; 172/620 against 189/708); the ink module ch5_ink.py 0 failing after three retypes; the display layer patched ({OV_REF5} by reference, 54 by gloss); the manifest {N_CLAIMS} claims verified, the labels gate green; the seat, verify_text, the ritual {N_PASS} PASS; the corpus tripwire set to the prediction (219 units, standing 2197, hash unmoved) and matched; build_world ALL GREEN; the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); the home-path gate GREEN. THE RECORDS from the sheet in one call (the map "Sitting 3", COMPILE_DEBT's 3b box (a)-(k), MIDDOT's five rows, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, RESUME, this addendum, the recovery page's section 2, the addenda's §36, the stamp, the memory). THE LESSONS (seven, in the map): the export's division mapped by an instrument; a continuation row cites in one file only; a chain's ROOT from the cwd's git (the first chain found "/logic/…" after the seat had written — the seat step made idempotent); a sed renames by whole words (the derived chain ran the old seat script); a spelling splits a census; the rows' cuts checked at load; the reading shape held. THE COST: the sitting ran without a wait loop — the chain and the fold in the background, each read once on the harness's notice; the records in one call. THE TREE: uncommitted since 834602b (the tutorial, the epub, the builder, sitting 3's files); the owner's commit word awaited. NEXT ON THE RULING: the compile of chapter 5 (3b — the laws' readback, code against code; the design in the map first) or the Decalogue-schema sitting first, on his word. IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 3" (the owed list (a)-(k)), MEMORY.md — nothing else unasked; THE_STEPS Step 5 + the compiler block before 3b's design.
'''
ADDENDA = f'''
## 36. ADDENDUM ({DATE}, THE DEUTERONOMY WALK sitting 3 — CHAPTER 5, Deuteronomy 5:1-33 READ AND FROZEN; the owner: "reread", "go"; the state doc's #187 addendum 1)
THE STATE: chapter 5 read and frozen as one unit (deu_05_decalogue, the 219th); the corpus 219 units, standing 2197 (2191 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED (no engine file changed — RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126), markers 165);
the journal gate GREEN ({J_KINDS} kinds, {J_ROWS} rows); the register gate --strict GREEN (DECLARED {R_DECL}, DEBT {R_DEBT}, FAILS {R_FAIL}); uncommitted since 834602b.
WHAT THE SITTING FOUND: the two divisions mapped by alignment (the export's 17 = the DB's 17-20); the second copy of the ten words diffed verse by
verse — five verbatim, one letter at 5:8, the ketiv at 5:10, KEEP for REMEMBER at 5:12 with the receipt "as the LORD your God commanded you" (5:12,
5:16 — the register gate's seats), the two beasts and the servants' rest at 5:14, the ground changed whole at 5:15, "and" on the four short words,
the vain witness for the false, the wife first and a second verb at 5:21; the Sifrei 233:1's "remember and keep in one utterance" (the Mekhilta
named, the first copy's spine unopened by any ledger); face to face the Bible's one seat, Onkelos "speech with speech"; the ten words in the
singular; the third generation starred by the parser; "added no more" read "did not cease"; the mob and the elders (1:22, 5:23); "hear and do"
against "do and hear"; Moses standing (357:40).
THE FILES CHANGED: logic/oral_triage/deu_05_vaetchanan_{DATE}.md (new); logic/units/deu_05_decalogue.yaml (draft → frozen, six operators, step E,
the scenarios in the anchor form) and logic/py_units/deu_05_decalogue.py; logic/oral_audit/manifests/deu_05_decalogue_claims.json (new);
logic/glosses/word_gloss_overrides.yaml (+58 by reference, +54 by gloss); logic/corpus/CORPUS_TRUTH.py (219, 2197); the records (the map,
COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, RESUME, the state doc, the recovery page, this file, STAMP_LEDGER, the memory);
World/step9/forms_deuteronomy_walk/ (the sitting's scripts and prints).
NEXT ON THE RULING: the compile of chapter 5 (3b) — or the Decalogue-schema sitting first — on the owner's word.
'''
MEMPAR = f'''
SITTING 3 DONE {DATE} (the owner: "reread", "go"; the map's "Sitting 3"): CHAPTER 5 READ AND FROZEN as one unit (deu_05_decalogue, the 219th). THE
TWO DIVISIONS mapped by alignment FIRST (the export's 17 = the DB's 17-20, then the offset three; every citation and row through the map). The two
copies of the ten words DIFFED verse by verse (five verbatim; keep for remember — the Sifrei 233:1: one utterance; the exodus for the creation at
5:15; the receipts "as the LORD your God commanded you" INSIDE the words at 5:12, 5:16 — the register gate's seats, paid at the compile; the ketiv at
5:10; the vain witness; the wife first). Every gate green; the corpus 219 / 2197 / hash unmoved; the tape unmoved. ⚠ LESSONS: a chain's ROOT from
the cwd's git (a scratch script's folder is not the repo); a sed renames by whole words — grep the derived script for the old name first; the seat
step idempotent. OWED TO 3b (COMPILE_DEBT's box (a)-(k)): the laws' readback code against code; the second word; the receipts' seats; the block's
edge. NOT COMMITTED (since 834602b). NEXT on the ruling: 3b, or the schema sitting first, on the owner's word.
'''
MEMLINE_OLD_START = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — '
MEMLINE_NEW = '- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — map World/step9/DEUTERONOMY_WALK.md; SITTINGS 1-3 DONE 2026-09-16 (chapters 1-4 COMPILED, 5 READ; COMMITTED 834602b through 2b, not pushed); NEXT: 3b or the schema sitting, on his word\n'
REC2_OLD_START = '## 2. WHERE IT STANDS'
REC2_NEW = f'''## 2. WHERE IT STANDS ({DATE}, after sitting 3 — chapter 5's reading; the state doc #187 addendum 1)
- NUMBERS CLOSED. DEUTERONOMY 1:1-4:49 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-2b); 5:1-33 READ AND FROZEN (sitting 3).
- 219 frozen units, standing 2197, hash 8b8fff1fa28953af. 59 runners, 64 daemons, 441 functions; registries 1119 kinds / 1019 effects.
- THE TAPE unmoved at 3 (2b's RUN; markers 165; the counter (40, 11, 1)); the sweep 59/59 at 6,527 cells; every gate GREEN; the register
  gate DECLARED {R_DECL} / DEBT 0 (the seats 5:12, 5:16, 5:32 owed to 3b).
- THE TWO DIVISIONS: the export's chapter 5 has 30 verses, the DB 33 — its 17 = the DB's 17-20, then the offset three (ch5_ink.py asserts it).
- LAST COMMIT 834602b (NOT pushed). Uncommitted: sitting 3's files; the schema tutorial, its epub and the builder (ARCHITECTURE/).
- ON THE TABLE, NOT A RULING: the Decalogue as a SCHEMA (seat chapter 5; the Sifrei 233:1 the exhibit).
- NEXT ON HIS WORD: 3b — THE COMPILE OF CHAPTER 5 (the laws' readback, code against code; COMPILE_DEBT's box (a)-(k)); or the schema sitting first.
'''

LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run([sys.executable, LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; RECP = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', RECP, f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', f'{MEM}/MEMORY.md']
# ---- THE ANCHORS, ASSERTED PRESENT ONCE BEFORE ANY WRITE ----
ANCH = [(WALKP, '## Sitting 2b — THE COMPILE OF CHAPTER 4 — AS BUILT'), (f'{ROOT}/World/RESUME.md', '# ⚠ THE DEUTERONOMY WALK sitting 2b (2026-09-16;'), (f'{ROOT}/THE_STEPS.md', '\n## Step 6 — Publish\n'), (f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-16, latest)\n'), (f'{ROOT}/THE_BRIEFING.md', '- **CHAPTER 4 COMPILED — THE TAPE HAD A HOLE'), (f'{ROOT}/THE_BRIEFING.md', '### 2026-09-16 — CHAPTER 4 COMPILED: THE TAPE HAD A HOLE'), (f'{ROOT}/logic/MIDDOT.md', '\n## Exodus block campaign — owner\'s word "Do 3")\n'), (RECP, REC2_OLD_START), (RECP, '\n## 3. THE STANDING LAWS'), (f'{MEM}/MEMORY.md', MEMLINE_OLD_START)]
for p, a in ANCH: assert rd(p).count(a) == 1, (p, a[:40], rd(p).count(a))
assert rd(f'{MEM}/deuteronomy-walk.md').count("COMMITTED 834602b on 'commit', NOT pushed); NEXT: chapter 5's reading\"") == 1
assert '## Sitting 3 — CHAPTER 5' not in rd(WALKP) and '#187 ADDENDUM 1' not in rd(TOUCH[1]) and '## 36. ADDENDUM' not in rd(TOUCH[9]) and 'SITTING 3 DONE' not in rd(f'{MEM}/deuteronomy-walk.md')
s = rd(RECP); i = s.index(REC2_OLD_START); j = s.index('\n## 3. THE STANDING LAWS'); REC_NEW = s[:i] + REC2_NEW + s[j:]
assert REC_NEW.count('- Deuteronomy\'s sittings: the map; the addenda §31-34. The cost cuts: §35 and memory cost-rules-no-polling.md.') == 1
REC_NEW = REC_NEW.replace('- Deuteronomy\'s sittings: the map; the addenda §31-34. The cost cuts: §35 and memory cost-rules-no-polling.md.', '- Deuteronomy\'s sittings: the map; the addenda §31-36. The cost cuts: §35.')
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
insert_before(TOUCH[2], '# ⚠ THE DEUTERONOMY WALK sitting 2b (2026-09-16;', RESUME_NOTE)
insert_before(TOUCH[3], '\n## Step 6 — Publish\n', STEPS)
insert_before(TOUCH[4], '- **CHAPTER 4 COMPILED — THE TAPE HAD A HOLE', BRIEF)
insert_before(TOUCH[4], '### 2026-09-16 — CHAPTER 4 COMPILED: THE TAPE HAD A HOLE', BRIEF_ENTRY)
append(TOUCH[5], DEBT)
append(TOUCH[6], RESEARCH)
insert_before(TOUCH[7], '\n## Exodus block campaign — owner\'s word "Do 3")\n', MIDDOT)
open(RECP, 'w', encoding='utf-8').write(REC_NEW); print('recovery page rewritten', len(REC_NEW.encode()), 'bytes')
append(TOUCH[9], ADDENDA)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
replace_once(f'{MEM}/deuteronomy-walk.md', "COMMITTED 834602b on 'commit', NOT pushed); NEXT: chapter 5's reading\"", "COMMITTED 834602b on 'commit', NOT pushed); SITTING 3 DONE 2026-09-16 (chapter 5 READ AND FROZEN as one unit, the 219th; the export's 30 verses mapped to the DB's 33 by alignment; the two copies of the ten words diffed; uncommitted); NEXT: 3b the compile of chapter 5 (the laws' readback) or the schema sitting, on the owner's word\"")
open(f'{MEM}/MEMORY.md', 'w', encoding='utf-8').write(MEM_NEW); print('MEMORY.md', len(MEM_NEW.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0 and len(rd(RECP).encode()) <= 10240
print('records written; the lints at or under their baselines; the map and the memory file lint 0; the page under its cap')
