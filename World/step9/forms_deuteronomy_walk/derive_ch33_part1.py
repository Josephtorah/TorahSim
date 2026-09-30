#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b: cold_run_blessing_of_moses.py PART 1 derived — the head typed here; the generic helper block COPIED from the song's runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W32 made W33); THE INK BLOCKS COPIED from the reading's own instrument
# ch33_ink.py by content markers — SIX blocks (the kin found by computation; the kin re-scored; the twins diffed; the formulas over the Torah and the Bible; the words;
# the frames, the register and the parser), the store-, shelf-, Onkelos- and register-bound lines DROPPED by name (10b's lesson 6 — the count read from the print); every
# Hebrew token GLOSSED from the store's own print (ch33_store_glosses.txt) with a small table for the tokens of other verses; THE COUNTER'S DAY (Moses' last day — NO MARKER),
# the one-database scans over the TWELVE ledgers the blessing writes on, and THE CALLEES' FACTS (ch33_callees_facts.py — printed at the first pass, asserted from the print at the
# second; every callee CALLED by its literal name, the bindings assignments). Asserted substitutions throughout. derive_ch32_part1.py's form over one chapter with NO MARKER
# and NO REUSE. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import subprocess, re, os, sys, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, SP)
import ch33b_spec as S
SCN = open(f'{ROOT}/World/step9/cold_run_song_charge_nebo.py', encoding='utf-8').read()
INKB = open(f'{SP}/ch33_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch33_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts (ch33_callees_facts.py)'
FA_ASSERTS = open(f'{SP}/ch33_fact_asserts.py', encoding='utf-8').read() if os.path.exists(f'{SP}/ch33_fact_asserts.py') else "# (the facts' asserts — written from the first pass's print at the second derive)\n"
FACTS = FACTS.replace('_FACT_ASSERTS_', FA_ASSERTS)
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 33:1-29 — THE BLESSING (and this is the blessing which Moses the man of God blessed the children of Israel before his death; the LORD came from Sinai, rose from Seir,
# shone from mount Paran, a fiery law at His right hand; He loves the peoples, all His holy ones in Your hand; Moses commanded us a law, the inheritance of the congregation of Jacob;
# a king in Jeshurun when the heads of the people gathered. Let Reuben live and not die; hear, LORD, the voice of Judah; Levi's Thummim and Urim, proved at Massah, the father and
# mother unseen, the covenant kept, the teaching, the incense and the whole offering, the substance blessed and the risers smitten; Benjamin the beloved between His shoulders; Joseph's
# land blessed with the precious things, the bush dweller's favor on the crown of him separate from his brethren, the firstling ox's horns with Ephraim's myriads and Manasseh's
# thousands; Zebulun in his going out and Issachar in his tents, the peoples called to the mountain; Gad enlarged, the lioness, the first part and the lawgiver's portion, the heads of
# the people; Dan the lion's whelp, Naphtali sated with favor, Asher's foot in oil, the bars of iron and brass; none like the God of Jeshurun, the rider of the heaven, the everlasting
# arms, the enemy driven out; Israel dwells in safety alone, the fountain of Jacob; happy are you, O Israel — the shield and the sword, the high places trodden); THE READBACK'S FORMS
# ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 21b — THE LEAN PASS, 2026-09-29; World/step9/DEUTERONOMY_WALK.md "Sitting 21b"; the state doc's #241). ONE RUNNER OVER ONE
# CHAPTER AND ONE UNIT (deu_33_ve_zot — the blessing 33:1-29; the span one range); ELEVEN own-day lines IN TWO FORMS — 1 ACT (the frame 33:1-2) and 10 SPEECHES (the prologue 33:3-5,
# the ten blessings at the reading's seats, the coda's two): EVERY LINE AT MOSES' LAST DAY (40, 12, 7) after 19b's ONE MARKER at 31:1 — NO MARKER HERE ('before his death' THAT day;
# the Sifrei 342:1 — the hard words first, the blessing after): moses_blessed_israel_before_his_death (33:1-2), blessing_prologue_law_and_king_declared (33:3-5),
# blessing_reuben_and_judah_declared (33:6-7), blessing_levi_declared (33:8-11), blessing_benjamin_declared (33:12), blessing_joseph_declared (33:13-17),
# blessing_zebulun_and_issachar_declared (33:18-19), blessing_gad_declared (33:20-21), blessing_dan_naphtali_asher_declared (33:22-25), blessing_rider_of_the_heaven_declared (33:26-27),
# blessing_israel_dwells_alone_declared (33:28-29) — TWENTY-EIGHT writes on TWELVE ledgers (twenty-eight NEW, all STATUSES, no block, no heaven entry — Israel 10 and THE TRIBES' OWN:
# reuben 1, judah 1, levi 4, benjamin 1, joseph 3, zebulun 1, issachar 1, gad 2, dan_son 1, naphtali 1, asher 2 — the sons' entities Genesis 49's testament wrote on; Simeon named
# nowhere, no write; NO REUSE). THE PARSER'S FALSE SEVEN as a DATA row (33:23's 'sated' — seven's consonants, MARKED and counted as nothing), no guard, no count in the world. THE
# KIN'S CELLS BY CALL (thirty-nine runners, every edge REFERENCE — the kin read this chapter forward: the death 34:5 ahead, Moses' grave in Gad's field, the six Meribah seats, the
# commission's debit OPEN to 34:1-4); THE TAPE'S LINES BY KIND (Sinai's descent, Massah and Meribah, the calf's sword, the bush, the crossed hands, Isaac's dew and corn, the
# testament, the law written and delivered); MOSES' GRAVE at 33:21 FORWARD to 34:6 (the death's sitting's — READ THEN COMPILE PER PORTION); THE TWO POINTER ROWS 33:5 and 33:28
# (20b's owed pointers PAID, grade R). Eleven cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE FIFTEEN MISHNAH AND
# TOSEFTA ROWS THE LEDGER CITES (Avot 1:1, 3:6, 5:6; Bava Kamma 4:3; Berakhot 4:3; Eduyot 8:6; Keritot 2:1; Menachot 8:3; Rosh Hashanah 2:8, 2:9; Sanhedrin 10:1; Shekalim 1:1;
# Sotah 7:5; Tosefta Avodah Zarah 9:4, Tosefta Eduyot 1:1 — read whole; four rows the regex misread, read whole and excluded; no docket, the lean form); the parameters the runner's
# DATA rows (sixteen — the sanctuary's tribe an OPEN parameter), NO clock datum (19b's death date THE DAY). The daemon law_blessing_of_moses given_at Deut 33:1, installed_by boot
# (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_33_ve_zot_2026-09-29.md; the lean exam: deu_33_ve_zot_exam_2026-09-29.md.

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 0, ("the guard counted %d expectations, the tripwire holds 0" % GUARDED)   # RETYPED after the generator (the cells' asks summed)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml, inspect
from collections import Counter
from fractions import Fraction
import effects_layer as FX
import world_engine as WE
import cold_run_song_charge_nebo as SC            # THE EDGE: blessing_of_moses -> song_charge_nebo CALL, reference (32:50's death commanded — 33:1's 'before his death', the event 34:5 AHEAD; the_readback's form; 32:15's Jeshurun — 33:5, 33:26; 32:13's high places — 33:29 by sense)
import cold_run_covenant_return_charge as CR    # THE EDGE: blessing_of_moses -> covenant_return_charge CALL, reference (31:9's law written and delivered — 33:4's handing-over; 31:14's days approach to die; the marker's day (40, 12, 7); the three gifts owed at 34:5)
import cold_run_gad_reuben as GR                 # THE EDGE: blessing_of_moses -> gad_reuben CALL, reference (Numbers 32:38's Nebo — MOSES' GRAVE in Gad's field, Sotah 13b: the pointer 33:21 FORWARD to 34:6; 32:33's land east — 33:20's enlarged Gad)
import cold_run_joseph as JO                     # THE EDGE: blessing_of_moses -> joseph CALL, reference (Genesis 49:25-26 five in order and 49:26's line whole — 33:13-16; 48:19's crossed hands — 33:17's Ephraim before Manasseh; the sons' ledgers the testament wrote on)
import cold_run_family as FA                     # THE EDGE: blessing_of_moses -> family CALL, reference (Genesis 27:10's 'before his death' — 33:1; 27:28's dew and corn THE KIN ONKELOS NAMES at 33:28; 35:22 Bilhah and 38:26 Tamar — 347:1, 348:1; 35:20 Rachel's grave — 352:16)
import cold_run_chukat as CK                     # THE EDGE: blessing_of_moses -> chukat CALL, reference (Numbers 20:12-13 the sentence at Meribah — 33:8's waters of Meribah, the six seats; 20:22-29 Aaron's death and the succession)
import cold_run_exodus_story as ES               # THE EDGE: blessing_of_moses -> exodus_story CALL, reference (Exodus 19:18-20 the descent — 33:2's Sinai; 17:7 Massah — 33:8; 3:2-4 the bush — 33:16; the seventh of Adar Moses' birthday)
import cold_run_erection as ER                   # THE EDGE: blessing_of_moses -> erection CALL, reference (Exodus 32:26-29 the calf's sword on the maternal kin — 33:9's father and mother unseen; 349:1's Levi repaid at the calf)
import cold_run_second_tablets as ST             # THE EDGE: blessing_of_moses -> second_tablets CALL, reference (10:6 Aaron died there and was buried there — Levi's tribe; Sotah 14a's burying the dead the callee's row on 34:6, cited never read)
import cold_run_incense_shekel as IS             # THE EDGE: blessing_of_moses -> incense_shekel CALL, reference (Exodus 30:7-8 the continual incense — 33:10's incense before You; 30:13 the half-shekel — Shekalim 1:1 at 352:14)
import cold_run_balak as BK                      # THE EDGE: blessing_of_moses -> balak CALL, reference (Numbers 23:22, 24:8's wild ox — 33:17's horns; 23:9's 'a people that dwells alone' — 33:28, the Sifrei 356:5; 23:24's lioness — 33:20; 25's Zimri — 349:1)
import cold_run_opening_speech as OS             # THE EDGE: blessing_of_moses -> opening_speech CALL, reference (2:8's Seir — 33:2's stations; Numbers 27:20's splendor — 33:17's majesty; the commission's debit OPEN to 34:1-4)
import cold_run_refuge_war_family as RW          # THE EDGE: blessing_of_moses -> refuge_war_family CALL, reference (21:5's 'by their word shall every controversy be' — 33:10's teaching; 351:1 every ruling from the Levites' mouth)
import cold_run_courts_prophet as CP             # THE EDGE: blessing_of_moses -> courts_prophet CALL, reference (17:8-11's high court at the place — 33:10's teaching; 352:6's sanctuary higher than the world with 17:8 at 33:12)
import cold_run_festivals_judges as FJ           # THE EDGE: blessing_of_moses -> festivals_judges CALL, reference (16:16's three times — 33:18's Issachar 'to make the times of the festivals in Jerusalem' (Onkelos); Rosh Hashanah 2:8-9 the cases)
import cold_run_good_land as GL                  # THE EDGE: blessing_of_moses -> good_land CALL, reference (8:8's olive oil — 33:24's foot in oil; 8:9's hills of brass — 33:25's iron and brass; the receipt finder [] over 33)
import cold_run_blessing_and_curse as BC         # THE EDGE: blessing_of_moses -> blessing_and_curse CALL, reference (11:14's rain in its season — 33:28's dew and 33:13's dew of heaven; 356:8's dew with 32:2's four rains)
import cold_run_release_firstborn as RL          # THE EDGE: blessing_of_moses -> release_firstborn CALL, reference (15:7's poor law — MOSES' RIGHTEOUSNESS at 33:21, the Sifrei 355:9: hand_opening_commanded on Israel)
import cold_run_persons_poor_court as PP         # THE EDGE: blessing_of_moses -> persons_poor_court CALL, reference (the compiled poor and court laws of 22-25 — 33:21's ordinances with Israel; 355:9-10's righteousness under the throne)
import cold_run_bamidbar as BM                   # THE EDGE: blessing_of_moses -> bamidbar CALL, reference (Numbers 1's census — 33:6's 'let his men be a number', counted 22 on the world; 33:17's myriads; the Levites' strip — 352:10)
import cold_run_naso as NS                       # THE EDGE: blessing_of_moses -> naso CALL, reference (Numbers 6's nazirite — 33:16's 'separate' THE HOMOGRAPH named at 353:8, FALSE for the nazirite's law)
import cold_run_korach as KO                     # THE EDGE: blessing_of_moses -> korach CALL, reference (Numbers 16's Korah the riser — 33:11's loins smitten, 352:1-4; 18's gifts and tithe — the Levites' portion unmoved)
import cold_run_vestments as VE                  # THE EDGE: blessing_of_moses -> vestments CALL, reference (Exodus 28:30's breastplate of judgment with the Urim and the Thummim — 33:8's one Torah seat of wearing)
import cold_run_priesthood as PR                 # THE EDGE: blessing_of_moses -> priesthood CALL, reference (Leviticus 21:11's high priest 'to his father and to his mother' — 33:9's one phrase; the priests' altar service — 33:10)
import cold_run_zelophehad as ZE                 # THE EDGE: blessing_of_moses -> zelophehad CALL, reference (Numbers 27:20's 'put of your splendor upon him' — 33:17's majesty, 353:9; Moses to Joshua the handing — Avot 1:1 at 33:4)
import cold_run_second_census as SC2             # THE EDGE: blessing_of_moses -> second_census CALL, reference (Numbers 26's second count — Reuben's number at 33:6; no number line here)
import cold_run_borders as BR                    # THE EDGE: blessing_of_moses -> borders CALL, reference (Numbers 34's borders — 33:23's sea and south, 33:19's seas; Onkelos's Gennesar 355:14-17)
import cold_run_place_name as PN                 # THE EDGE: blessing_of_moses -> place_name CALL, reference (12:5's place chosen 'in one of your tribes' — 33:12's sanctuary between Benjamin's shoulders: the strip, Zevachim 118b, 352:10's dispute the OPEN parameter; 12:2's high places — 33:29 FALSE)
import cold_run_obey_horeb as OH                 # THE EDGE: blessing_of_moses -> obey_horeb CALL, reference (4:44's frame 'and this is the law' — 33:1's frame five in order; 4:35, 4:39's creed — 33:26's 'none like'; 4:26's 'destroy' — 33:27)
import cold_run_seven_nations as SN              # THE EDGE: blessing_of_moses -> seven_nations CALL, reference (7:1-2's seven nations destroyed — 33:27's enemy driven out, 356:3's two fates; 7:6-7's chose you — 33:3's love)
import cold_run_hear_o_israel as HI              # THE EDGE: blessing_of_moses -> hear_o_israel CALL, reference (6:16's Massah inside the book — 33:8; 6:4's creed — 33:26's 'none like the God of Jeshurun')
import cold_run_moadim as MD                     # THE EDGE: blessing_of_moses -> moadim CALL, reference (Leviticus 23's appointed seasons — 33:18's festivals' times, Onkelos's; the registry's festival_dates unmoved)
import cold_run_offerings as OF                  # THE EDGE: blessing_of_moses -> offerings CALL, reference (Leviticus 1's burnt offering — 33:10's whole offering, 351:3-4's limbs; the peace offerings — 33:19's sacrifices of righteousness)
import cold_run_firstfruits_ebal_curses as FE    # THE EDGE: blessing_of_moses -> firstfruits_ebal_curses CALL, reference (27's stones on Ebal in seventy tongues — Sotah 7:5 the case at 343:5; six_tribes_on_gerizim_to_bless, six_tribes_on_ebal_for_the_curse unmoved)
import cold_run_shelach as SHL                   # THE EDGE: blessing_of_moses -> shelach CALL, reference (Numbers 13-14 the spies — 350:3's covenant kept 'at the spies'; 14:17's pointer on the chapter's words the recon found)
import cold_run_journeys as JR                   # THE EDGE: blessing_of_moses -> journeys CALL, reference (Numbers 33's stations — 33:2's Seir and Paran; 33:38-40 Aaron's death the retelling that never writes)
import cold_run_midian as MI                     # THE EDGE: blessing_of_moses -> midian CALL, reference (Numbers 25 and 31 — 349:1's Simeon borrowed again at Zimri: Simeon under Judah the DATA row, no write on simeon)
import cold_run_mamre as MA                      # THE EDGE: blessing_of_moses -> mamre CALL, reference (Genesis 15:1's 'I am your shield' — 33:29's shield of your help, shield_promised on abraham; 22:14's house seen — 352:9)
import cold_run_pre_sinai as PS                  # THE EDGE: blessing_of_moses -> pre_sinai CALL, reference (Genesis 9's sons of Noah — the seven commandments the nations refused, 343:6; Tosefta Avodah Zarah 9:4 the case)

'''
# ---- the generic helper block from the song's runner, by content markers ----
a = SCN.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = SCN.index('def LEN(b, c, v): return len(words(b, c, v))'); b = SCN.index('\n', b) + 1
helpers = SCN[a:b]
OLDW = "def W32(v): return words('Deut', 32, v)\ndef W(c, v): return words('Deut', c, v)"
assert helpers.count(OLDW) == 1
helpers = helpers.replace(OLDW, "def W33(v): return words('Deut', 33, v)\ndef W(c, v): return words('Deut', c, v)")
left = [l for l in helpers.split('\n') if re.search(r'(?<!\d)32(?!\d)', re.sub(r'2026-09-\d\d|0x05[0-9A-F]{2}', '', l))]
print('helper lines still naming 32:', len(left), [l[:100] for l in left][:4]); assert not left, left[:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
def _G(s): return s.split(' (')[0]   # a Hebrew token typed WITH ITS GLOSS beside it — the token alone returned (the lint's ninety-character window; 18b's form for the copied ink asserts)
DV = lambda c, v: ('Deut', c, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
CHS = (33,)
NV = {c: len({v for (b, cc, v) in by if b == 'Deut' and cc == c}) for c in CHS}; assert NV == {33: 29}, NV   # twenty-nine verses (the reading's divisions assert — the identity)
TOKN = {c: sum(len(W(c, v)) for v in range(1, NV[c] + 1)) for c in CHS}
print('THE TOKENS (printed before they are asserted):', TOKN)
TOKN_EXPECTED = _TOKN_EXPECTED_   # typed from the first derive's print (the callees' way — printed before typed)
if TOKN_EXPECTED: assert TOKN == TOKN_EXPECTED, (TOKN, TOKN_EXPECTED)
SPAN = [(33, v) for v in range(1, 30)]
assert len(SPAN) == 29

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch33_ink.py — COPIED from the reading's instrument by content markers in six blocks; the store-, shelf-, Onkelos- and register-bound asserts left to the reading; the parser's facts typed from the measure's print as the ink instrument asserted them) ----
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {(c, v): (ink_numbers(verse_words('Deut', c, v)), ink_ordinals(verse_words('Deut', c, v)), MARKS(c, v)) for (c, v) in SPAN}
NUMV = [k for k in PARSE if PARSE[k][0]]; ORDV = [k for k in PARSE if PARSE[k][1]]; STARV = [k for k in PARSE if PARSE[k][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %s' % ({k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]} == {(33, 23): ([], [], ['שבע*'])}, {k: p for k, p in PARSE.items() if p[0] or p[1] or p[2]}   # the reading's parser assert (ch33_ink.py from ch33_measure_lean.out): 33:23 THE FALSE SEVEN (sated with favor) MARKED, NOT COUNTED — no number in the chapter
assert NUMV == [] and ORDV == [] and STARV == [(33, 23)]
FALSE_SEVEN = W(33, 23)[3]; assert FALSE_SEVEN == 'שבע' and W(33, 23)[0:3] == ['ולנפתלי', 'אמר', 'נפתלי'] and W(33, 23)[4:6] == ['רצון', 'ומלא']   # (sated — seven's consonants, an adjective: of Naphtali he said, Naphtali sated with favor and full) — the parser's one mark, a DATA row
NEG = {(c, v): [x for x in W(c, v) if x in NEG_T] for (c, v) in SPAN if any(x in NEG_T for x in W(c, v))}
NAME_BARE = sum(1 for (c, v) in SPAN for x in W(c, v) if x == 'יהוה')   # (the LORD)
print('THE NEGATIONS AND THE NAME (printed before they are asserted):', NEG, NAME_BARE)
NAME_BARE_EXPECTED = _NAME_BARE_EXPECTED_   # typed from the first derive's print
if NAME_BARE_EXPECTED: assert NAME_BARE == NAME_BARE_EXPECTED, (NAME_BARE, NAME_BARE_EXPECTED)
NEG_EXPECTED = _NEG_EXPECTED_   # the negations per verse, typed from the first derive's print
if NEG_EXPECTED: assert {'%d:%d' % k: len(v) for k, v in NEG.items()} == NEG_EXPECTED, {'%d:%d' % k: len(v) for k, v in NEG.items()}
assert [f'{c}:{v}' for c, v in SPAN if 'לאמר' in W(c, v)] == [] and [(c, v) for c, v in SPAN if 'אם' in W(c, v)] == [] and [(c, v, x) for c, v in SPAN for x in W(c, v) if x == 'פן'] == [] and [(c, v) for c, v in SPAN if 'לא' in W(c, v)] == [(33, 9)]   # ("saying" — none; "if" — none; "lest" — none; "not" — 33:9 alone, thrice) — the reading's frames assert
assert [(v, x) for c, v in SPAN for x in W(c, v) if x in ('אמר', 'ויאמר')] == [(2, 'ויאמר'), (7, 'ויאמר'), (8, 'אמר'), (12, 'אמר'), (13, 'אמר'), (18, 'אמר'), (20, 'אמר'), (22, 'אמר'), (23, 'אמר'), (24, 'אמר'), (27, 'ויאמר')]   # ("he said" eleven — nine tribal frames, 33:2's theophany and 33:27's "destroy"; Reuben unframed)
'''
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = (block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE ASSERTS TYPED FROM THE PRINTS (block a")
             + block("# THE KIN BY COMPUTATION: the frame's kin 4:44", "# THE TWINS DIFFED (shared / the longest run)")
             + block("# THE TWINS DIFFED (shared / the longest run)", "# THE FORMULAS (phrase seats by consonants")
             + block("# THE FORMULAS (phrase seats by consonants", "# THE WORDS: the Name SEVEN times bare")
             + block("# THE WORDS: the Name SEVEN times bare", "# ONKELOS WRITING THE MEANING")
             + block("# THE FRAMES, THE REGISTER AND THE PARSER", "# THE PRIOR READS"))
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|ARM|SEATS|clean|heads|SP_|aramaic|arm|arm_e|E|kinrows|CS|_CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB|store|FAIL|_DUMP|_RC|_rink|DT|_MP|SPINE_PRIOR|FRESH|PRIOR_READ)(?![A-Za-z_0-9])")
drop = [l for l in lines if not l.lstrip().startswith('#') and DROP_RX.search(l.split('   #')[0])]
print('dropped (the store-, shelf-, Onkelos- and register-bound lines):', len(drop), [d[:90] for d in drop])
N_DROP_EXPECTED = int(os.environ.get('N_DROP', '-1'))
if N_DROP_EXPECTED >= 0: assert len(drop) == N_DROP_EXPECTED, (len(drop), [d[:100] for d in drop])   # READ FROM THE PRINT at the first derive, typed into the shell's N_DROP at the second
lines = [l for l in lines if l not in drop]
STOP_OLD = "STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן ואת זה וזה הם המה'.split())"
STOP_NEW = ("STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)\n"
            "            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)\n"
            "            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)\n"
            "            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)\n"
            "            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)\n"
            "            'בארץ הארץ אשר ואם או פן ופן '   # (in the land, the land, which, and if, or, lest)\n"
            "            'ואת זה וזה הם המה').split())   # (and-it, this, and this, they, they) — the stopword set glossed piece by piece (the lint's ninety-character window)")
assert lines.count(STOP_OLD) == 1, lines.count(STOP_OLD)
lines[lines.index(STOP_OLD)] = STOP_NEW
ink_block = '\n'.join(lines)
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 8, n_as
KIN47 = tuple(S.KIN_UNMOVED); KIN_EXPECTED = tuple(S.KIN_UNMOVED[k] for k in KIN47); OWN28 = tuple(S.NEW_EFFECTS)
LEDGERS12 = ('israel_people', 'reuben', 'judah', 'levi', 'benjamin', 'joseph', 'zebulun', 'issachar', 'gad', 'dan_son', 'naphtali', 'asher')
assert set(sub for _, _, sub in S.NEW_E) == set(LEDGERS12)
HOLE_WORDS = r"^(" + '|'.join(sorted({'_'.join(n.split('_')[:3]) + r'\w*' for n in OWN28})) + r")$"
TAIL_B = '''
# ---- THE COUNTER'S DAY (a bare world on the exodus epoch; Moses' last day (40, 12, 7) — 19b's ONE MARKER at 31:1 stands, NO MARKER here; 33:1's 'before his death' THAT day; the death date 19b's clock datum on the calendar's keys, read here) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='Moses\\' last day — chapter 33 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
MOSES_120 = DAY(40, 12, 7); COUNTER = MOSES_120
CLOCK = {'counter': DATE(COUNTER), 'marker': None, 'marker_verse': None, 'marker_at': None, 'days_walked': 0, 'the_day_by': "19b's marker at Deut 31:1 (the number's verse 31:2) — the_death_date_of_moses on the calendar's keys", 'clock_data': ['the_death_date_of_moses']}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 12, 7) and CLOCK['marker'] is None and CLOCK['days_walked'] == 0, CLOCK
assert all(k in WE.CAL_PARAMS for k in CLOCK['clock_data']), [k for k in CLOCK['clock_data'] if k not in WE.CAL_PARAMS]   # 19b's calendar parameter on file — the received channel
assert WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by'] == ['covenant_return_charge'], WE.CAL_PARAMS['the_death_date_of_moses']['exercised_by']   # 19b's row UNTOUCHED (add_types_ch33_b.py — the calendar untouched)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the twenty-eight on their twelve ledgers before this sitting; the references' entities and counts as the recon read them — DO4) ----
_WDB = _os.path.join(_ROOT, 'World', 'journal', 'data', 'world.sqlite')
def ledger_scan(entity, pattern):
    """the effects on an entity in the one database whose name or value matches the pattern — None where the database is not built (a fresh clone before build_world)"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    rx = re.compile(pattern, re.I)
    return sorted({e for e, v in c_.execute("SELECT DISTINCT effect, value FROM run_ledger WHERE entity=?", (entity,)).fetchall() if rx.search('%s %s' % (e, v if v is not None else ''))})
def effect_scan(effect):
    """the entities holding an effect in the one database — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    return sorted({e for (e,) in c_.execute("SELECT DISTINCT entity FROM run_ledger WHERE effect=?", (effect,)).fetchall()})
def count_scan(effect):
    """the entries of an effect in ONE full run of the tape (DO4's counts — the running world's): the one database folds several runs' rows under their sources (the checkpoint sections' names); the largest source is a whole run — None where the database is not built"""
    if not _os.path.exists(_WDB): return None
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (effect, src)).fetchone()[0]
OWN28 = %(OWN28)r
assert len(OWN28) == 28 and len(set(OWN28)) == 28
LEDGERS12 = %(LEDGERS12)r
HOLE_WORDS = r"%(HOLE_WORDS)s"
_hs = {ent: ledger_scan(ent, HOLE_WORDS) for ent in LEDGERS12}; HOLE_SCAN = None if any(v is None for v in _hs.values()) else {ent: [e for e in v if e not in OWN28] for ent, v in _hs.items()}   # this sitting's own names excluded once the fold carries them
KIN47 = %(KIN47)r
KIN_EXPECTED = %(KIN_EXPECTED)r   # DO4 — the recon's and the callees' counts on the running world (ch33b_recon.out section H; ch33_callees.out THE NEAR NAMES; the probe Q50's KIN tuple)
assert len(KIN47) == 47 == len(KIN_EXPECTED)
KIN_COUNTS = {k: count_scan(k) for k in KIN47}
REUSE3 = ()   # NO REUSE this sitting — no effect's own forward seat lies in the chapter (20b had three)
REUSE_BEFORE = {}
REUSE_AFTER = {}
REUSE_COUNTS = {}
SCANS = {k: effect_scan(k) for k in KIN47[:8] + ('garments_transferred_and_aaron_died', 'invested_office', 'demoted', 'scepter_held', 'birthright_transferred', 'scattered_in_israel', 'younger_set_first', 'concubine_lain_with')}
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %%s; the kin counts %%s; the reuses %%s; the entities %%s' %% (HOLE_SCAN, KIN_COUNTS, REUSE_COUNTS, SCANS))
assert HOLE_SCAN is None or all(v == [] for v in HOLE_SCAN.values()), HOLE_SCAN   # THE HOLES' GROUND — nothing on the twelve ledgers named the twenty-eight before this sitting (DO4)
assert all(v is None for v in KIN_COUNTS.values()) or tuple(KIN_COUNTS.values()) == KIN_EXPECTED, [(k, KIN_COUNTS[k], e) for k, e in zip(KIN47, KIN_EXPECTED) if KIN_COUNTS[k] != e]   # the references' counts as the recon read them (DO4 — no second write)
SCANS_EXPECTED = _SCANS_EXPECTED_   # the entities per effect — typed from the first derive's print (the callees' way — printed before typed)
if SCANS_EXPECTED and any(v is not None for v in SCANS.values()): assert SCANS == SCANS_EXPECTED, [(k, SCANS[k], SCANS_EXPECTED.get(k)) for k in SCANS if SCANS[k] != SCANS_EXPECTED.get(k)]
assert all(k in _FXV for k in OWN28) and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'block') == 0 and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'status') == 28 and sum(1 for k in OWN28 if _FXV[k]['ledger_op'] == 'heaven') == 0, 'the twenty-eight on the registry (add_types_ch33_a.py)'
assert _FXV['barred_from_the_land']['ledger_op'] == 'heaven' and _FXV['gathered_to_his_people']['ledger_op'] == 'status' and _FXV['shield_promised']['ledger_op'] in ('status', 'heaven') and _FXV['blessed_with_dew_and_fat']['ledger_op'] in ('status', 'heaven'), 'the referenced rows\\' ops (read from the registry\\'s print at the types)'
# THE TWINS DIFFED on the DB (the reading's kin asserts read again here — DO4; the shared run SH)
TWIN = {'33:16 vs Gen 49:26': SH(DV(33, 16), ('Gen', 49, 26)), '33:13 vs Gen 49:25': SH(DV(33, 13), ('Gen', 49, 25)), '33:15 vs Hab 3:6': SH(DV(33, 15), ('Hab', 3, 6)), '33:2 vs Hab 3:3': SH(DV(33, 2), ('Hab', 3, 3)), '33:1 vs Josh 14:6': SH(DV(33, 1), ('Josh', 14, 6)), '33:1 vs 4:44': SH(DV(33, 1), DV(4, 44)),
        '33:1 vs Gen 27:10': SH(DV(33, 1), ('Gen', 27, 10)), '33:8 vs Num 20:13': SH(DV(33, 8), ('Num', 20, 13)), '33:8 vs Exod 17:7': SH(DV(33, 8), ('Exod', 17, 7)), '33:9 vs Lev 21:11': SH(DV(33, 9), ('Lev', 21, 11)), '33:5 vs 32:15': SH(DV(33, 5), DV(32, 15)), '33:28 vs 32:2': SH(DV(33, 28), DV(32, 2)),
        '33:12 vs Gen 49:27': SH(DV(33, 12), ('Gen', 49, 27)), '33:6 vs Gen 49:4': SH(DV(33, 6), ('Gen', 49, 4)), '33:6 vs Gen 49:3': SH(DV(33, 6), ('Gen', 49, 3)), '33:7 vs Gen 49:8': SH(DV(33, 7), ('Gen', 49, 8)), '33:24 vs Gen 49:20': SH(DV(33, 24), ('Gen', 49, 20)), '33:21 vs Num 32:33': SH(DV(33, 21), ('Num', 32, 33)),
        '33:22 vs Gen 49:9': SH(DV(33, 22), ('Gen', 49, 9)), '33:17 vs Gen 48:20': SH(DV(33, 17), ('Gen', 48, 20)), '33:17 vs Num 27:20': SH(DV(33, 17), ('Num', 27, 20)), '33:29 vs Gen 15:1': SH(DV(33, 29), ('Gen', 15, 1)), '33:28 vs Num 23:9': SH(DV(33, 28), ('Num', 23, 9)), '33:28 vs Gen 27:28': SH(DV(33, 28), ('Gen', 27, 28)),
        '33:26 vs 4:35': SH(DV(33, 26), DV(4, 35)), '33:29 vs 32:13': SH(DV(33, 29), DV(32, 13)), '33:19 vs Ps 4:6': SH(DV(33, 19), ('Ps', 4, 6)), '33:4 vs 31:9': SH(DV(33, 4), DV(31, 9)), '33:16 vs Exod 3:2': SH(DV(33, 16), ('Exod', 3, 2)), '33:27 vs 7:2': SH(DV(33, 27), DV(7, 2)),
        '33:23 vs Gen 49:21': SH(DV(33, 23), ('Gen', 49, 21)), '33:20 vs Gen 49:19': SH(DV(33, 20), ('Gen', 49, 19)), '33:18 vs Gen 49:13': SH(DV(33, 18), ('Gen', 49, 13)), '33:10 vs 21:5': SH(DV(33, 10), DV(21, 5)), '33:10 vs 17:8': SH(DV(33, 10), DV(17, 8)), '33:8 vs Exod 28:30': SH(DV(33, 8), ('Exod', 28, 30)),
        '33:8 vs 6:16': SH(DV(33, 8), DV(6, 16)), '33:12 vs 12:5': SH(DV(33, 12), DV(12, 5)), '33:21 vs 15:7': SH(DV(33, 21), DV(15, 7)), '33:24 vs 8:8': SH(DV(33, 24), DV(8, 8)), '33:25 vs 8:9': SH(DV(33, 25), DV(8, 9)), '33:27 vs Exod 24:5': SH(DV(33, 27), ('Exod', 24, 5)), '33:27 vs Exod 24:11': SH(DV(33, 27), ('Exod', 24, 11))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
TWIN_EXPECTED = _TWIN_EXPECTED_
if TWIN_EXPECTED: assert TWIN == TWIN_EXPECTED, [(k, TWIN[k], TWIN_EXPECTED.get(k)) for k in TWIN if TWIN[k] != TWIN_EXPECTED.get(k)]   # typed from the first derive's print (the callees' way — printed before typed)
assert TWIN['33:16 vs Gen 49:26'] >= 5 and TWIN['33:1 vs 4:44'] >= 5 and TWIN['33:13 vs Gen 49:25'] >= 3 and TWIN['33:1 vs Josh 14:6'] >= 3 and TWIN['33:22 vs Gen 49:9'] >= 2, TWIN   # the reading's largest twins (Joseph's crown five in order, the frame five, the deep three, the man of God three, the lion's whelp two)
'''
for _k, _v in (('%(OWN28)r', repr(OWN28)), ('%(LEDGERS12)r', repr(LEDGERS12)), ('%(HOLE_WORDS)s', HOLE_WORDS), ('%(KIN47)r', repr(KIN47)), ('%(KIN_EXPECTED)r', repr(KIN_EXPECTED))): TAIL_B = TAIL_B.replace(_k, _v)
TAIL_B = TAIL_B.replace('%%', '%')   # the print's own %s escaped inside the template
def _read(name):
    p = f'{SP}/{name}'; return open(p).read().strip() if os.path.exists(p) else 'None'
TWIN_EXPECTED = _read('ch33_twin_expected.txt'); SCANS_EXPECTED = _read('ch33_scans_expected.txt'); TOKN_EXPECTED = _read('ch33_tokn_expected.txt'); NAME_BARE_EXPECTED = _read('ch33_name_bare_expected.txt'); NEG_EXPECTED = _read('ch33_neg_expected.txt')   # the first derive's prints, parsed by ast from the fast checker's output and written to the files — never typed by hand
# THE GLOSS TABLE — the store's own glosses for the chapter's tokens (ch33_store_glosses.txt, the reading's print), a small table for the tokens of other verses the copied asserts name
GLOSS = {}
for _l in open(f'{SP}/ch33_store_glosses.txt', encoding='utf-8'):
    for _i, _tok, _g in ast.literal_eval(_l.split(': ', 1)[1]):
        GLOSS.setdefault(_tok, _g.replace('-', ' ').replace('/', ' or ').replace("'", '').replace('"', ''))   # the store's apostrophes dropped (a quoted gloss inside a quoted token)
GLOSS.update({'לוי': 'Levi', 'בנימן': 'Benjamin', 'שמעון': 'Simeon', 'יששכר': 'Issachar', 'כאשר': 'as', 'מגד': 'precious thing, the letters of Gad', 'אלוה': 'God', 'אלהים': 'God', 'אלהיו': 'his God', 'אלהיהם': 'their God', 'ליהוה': 'to the LORD', 'ויהוה': 'and the LORD', 'מיהוה': 'from the LORD',
              'אלהיך': 'your God', 'אלהיכם': 'your God', 'את': 'the object marker', 'ואת': 'and-it', 'כל': 'all', 'וכל': 'and all', 'על': 'on', 'ועל': 'and on', 'אל': 'to', 'ואל': 'and not', 'לא': 'not', 'ולא': 'and not', 'כי': 'for', 'אם': 'if', 'פן': 'lest', 'לאמר': 'saying', 'יהוה': 'the LORD', 'האלהים': 'God',
              'אלהי': 'the God of', 'כאל': 'like God', 'אש': 'fire', 'דת': 'law', 'ישרון': 'Jeshurun', 'לפני': 'before', 'מותו': 'his death', 'מי': 'who', 'כמוך': 'like you', 'נזיר': 'separate', 'אחיו': 'his brethren', 'גור': 'whelp', 'אריה': 'lion', 'כלביא': 'as a lioness', 'ראשי': 'the heads of', 'עם': 'the people', 'השמד': 'destroy',
              'איש': 'man', 'הבשן': 'Bashan', 'ישכן': 'shall dwell', 'לבטח': 'in safety', 'זבחי': 'sacrifices of', 'צדק': 'righteousness', 'במסה': 'at Massah', 'אמר': 'he said', 'ויאמר': 'and he said', 'שבע': 'sated, the consonants of seven', 'ישראל': 'Israel', 'יעקב': 'Jacob', 'משה': 'Moses', 'ותירש': 'and wine, the defective spelling of Genesis 27:28'})
MISSING = []
def glossify(text):
    def repl(m):
        tok = m.group(1); key = tok.rstrip('*%|')
        if key not in GLOSS: MISSING.append(tok); return m.group(0)
        return "_G('%s (%s)')" % (tok, GLOSS[key])
    out_ = []
    for l in text.split('\n'):
        if l.lstrip().startswith('#') or 'STOP = set((' in l or l.lstrip().startswith("'") and '   # (' in l: out_.append(l); continue   # the comments and the glossed STOP set kept
        out_.append(re.sub(r"'([א-תװ-״]+[*%|]?)'", repl, l))
    return '\n'.join(out_)
TAIL_A = glossify(TAIL_A); ink_block = glossify(ink_block)
assert not MISSING, ('a Hebrew token without a gloss in the table', sorted(set(MISSING)))
src = HEAD + helpers + TAIL_A.replace('_TOKN_EXPECTED_', TOKN_EXPECTED).replace('_NAME_BARE_EXPECTED_', NAME_BARE_EXPECTED).replace('_NEG_EXPECTED_', NEG_EXPECTED) + ink_block + TAIL_B.replace('_TWIN_EXPECTED_', TWIN_EXPECTED).replace('_SCANS_EXPECTED_', SCANS_EXPECTED) + FACTS
open(f'{SP}/ch33_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch33_part1.py', doraise=True)
lint = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', f'{SP}/ch33_part1.py'], capture_output=True, text=True).stdout.strip().split('\n')[-1]; print('the lint on part 1:', lint); assert lint.endswith('0 flag(s)'), lint
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes; TWIN_EXPECTED %s; SCANS_EXPECTED %s; TOKN %s; NAME_BARE %s; NEG %s' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS), TWIN_EXPECTED[:40], SCANS_EXPECTED[:40], TOKN_EXPECTED, NAME_BARE_EXPECTED, NEG_EXPECTED[:40]))
