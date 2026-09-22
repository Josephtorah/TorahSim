#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b: cold_run_seducers.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-12 runner by content markers
# (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W12 made W13); THE INK BLOCK COPIED from the reading's own instrument
# ch13_ink.py by content markers — THREE blocks (the kin by computation, the phrases censused over the DB, the register computed on the morphology; the Onkelos,
# the shelf-by-position, the store's glosses and the parser sections left to the reading), the store-bound lines DROPPED by name (10b's lesson 6 — the patterns
# listed; the count read from the print); the counter's day, the four parameters, the one-database scans and THE CALLEES' FACTS (asserted from ch13_callees.out —
# read before any assert was typed) typed. Asserted substitutions throughout. derive_ch12_part1.py's form. RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
PN = open(f'{ROOT}/World/step9/cold_run_place_name.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch13_ink.py', encoding='utf-8').read()
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 13:1-19 — THE HEADER'S SEAL, THE PROPHET AND THE TEST, THE INCITER, THE CITY HEARD OF, THE INQUIRY AND THE SWORD, THE WHOLE OFFERING, THE HEAP AND
# THE MERCY, THE FOOTER — THE SEDUCERS' ONE SENTENCE SAID THREE TIMES; THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 11b, 2026-09-21;
# World/step9/DEUTERONOMY_WALK.md "Sitting 11b"; the state doc's #203). THE CODE'S FOUR HOLES compiled at the counter's day (40, 11, 1), FOUR own-day lines, NO
# marker: the header's seal (13:1 — A REUSE: adding_barred's second entry, 4:2's twin in the singular), the prophet's test and the false prophet's death (13:2-6 —
# false_prophet_hearing_barred a BLOCK with the_signs_status a PARAMETER, tested_by_the_lord a STATUS, cleaving_commanded REUSED for the six verbs; the death
# the case's — the_prophets_death a PARAMETER: stoning / strangling, the answer sheet's arm; evil_purged_from_the_midst NAMED at THE PURGE FORMULA'S FIRST SEAT OF
# NINE), the inciter's law (13:7-12 — pity_barred REUSED with the five prohibitions against the standing duties and the court's rule inverted; israel_hears_and_fears
# THE FORMULA'S FIRST SEAT OF FOUR with the_execution_timing a PARAMETER; the entrapment, the fifteen utterances, the hand first, the stoning's rite by CALL), the
# condemned city's law (13:13-19 — condemned_city_inquiry_required a STATUS: the seducers' parameters from one noun, Jerusalem excluded, the venue, THE SEVEN
# INTERROGATIONS with the_inquiries a PARAMETER; devoted_thing_cleaving_barred a BLOCK: the benefit ban's source and reach; the case's city_devoted — the sword,
# the property table, Heaven's spoil, the heap forever with Jericho and Hiel; the footer the condition, no write). THE KIN'S CELLS BY CALL (twenty runners); THE
# TAPE'S LINES BY KIND (the calf, the testing, the cloud, the stonings, Hormah, Peor, the not-adding, the cleaving, the nations devoted). Six cells and the table;
# every token probed (zero-report law); effects on every cell (the effects law); the DATA rows the docket added. The daemon law_seducers given_at Deut 13:1,
# installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_13_reeh_2026-09-21.md; the exam's docket: deu_13_reeh_exam_2026-09-21.md
# (565 rows — 409 READ WHOLE in one run, 156 carried with their ledgers' own verdicts: LAW 127 / DERIVATION 103 / DISPUTE 88 / CONTEXT 111 / OUTSIDE 136).

# ---- THE HONEST-PAIRING GUARD ----------------------------------------------------------------------------
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO: the repo root from this file's own place
from compile_guards import check_honest_pairing as _chp
_P = _os.path.abspath(__file__)
GUARDED = _chp(_P, 'CASES', 2)
assert GUARDED == 0, ("the guard counted %d expectations, the tripwire holds 0" % GUARDED)   # RETYPED after the generator (the cells' asks summed)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, io, re, contextlib, collections, unicodedata, yaml
from collections import Counter
import effects_layer as FX
import world_engine as WE
import cold_run_obey_horeb as OH               # THE EDGE: seducers -> obey_horeb CALL, reference (13:1's seal 4:2's law in the singular — add_nothing, diminish_nothing, add_beside, add_out_of_its_time; adding_barred REUSED; add_nothing_commanded 4:1 on the tape)
import cold_run_covenant_at_horeb as CH       # THE EDGE: seducers -> covenant_at_horeb CALL, reference (13:3, 7, 14's 'other gods' the second word's object; 13:6, 11's exodus formula the preamble's 5:6)
import cold_run_hear_o_israel as HI           # THE EDGE: seducers -> hear_o_israel CALL, reference (13:4's testing against 6:16's test_barred; 13:5's six verbs against 6:13's three; 13:8's gods round about 6:14's; 13:19's right 6:18's)
import cold_run_seven_nations as SN           # THE EDGE: seducers -> seven_nations CALL, reference (13:9's pity 7:16's — pity_barred REUSED; 13:16's devoting 7:2's ban; 13:18's devoted thing 7:26's house_abomination_barred; the oath and the redeeming 7:8's)
import cold_run_good_land as GL               # THE EDGE: seducers -> good_land CALL, reference (13:4's testing 8:2 and 8:16's forty years — 'to know')
import cold_run_not_righteousness as NR       # THE EDGE: seducers -> not_righteousness CALL, reference (13:6's redeeming 9:26's; the calf 13:3's run case; the fathers' merit 7b's parameter at 13:18)
import cold_run_second_tablets as ST          # THE EDGE: seducers -> second_tablets CALL, reference (13:5's six verbs 10:20's four — cleaving_commanded REUSED; Sotah 14a's attributes)
import cold_run_blessing_and_curse as BC      # THE EDGE: seducers -> blessing_and_curse CALL, reference (13:3 and 13:14's 'other gods which you have not known' 11:28's; 13:4's heart and soul 11:13's; 13:19's 'if you hearken')
import cold_run_place_name as PN              # THE EDGE: seducers -> place_name CALL, reference (13:13's [1] 12:14's form; 13:19's right 12:25 and 12:28's; the tape's last Deuteronomy 12 line the four new lines' predecessor)
import cold_run_ordinances as OR              # THE EDGE: seducers -> ordinances CALL, reference (13:16's devoting Exodus 22:19's ban at its first seat; 13:9's inverted rule the court's ordinary one; the four services)
import cold_run_erection as ER                # THE EDGE: seducers -> erection CALL, reference (13:3's formula the calf's — calf_made Exod 32:4 on the tape; 13:5's first verb the cloud — cloud_lifted)
import cold_run_sanctions as SA               # THE EDGE: seducers -> sanctions CALL, reference (13:6's death the four deaths' census — the strangled; 13:10's people who stone at Molech; the forewarning)
import cold_run_lev24 as L24                  # THE EDGE: seducers -> lev24 CALL, reference (13:10's hand first Leviticus 24:14's hands laid; the blasphemer's stoning — stoned_as_commanded Lev 24:23 on the tape)
import cold_run_mekoshesh as MK               # THE EDGE: seducers -> mekoshesh CALL, reference (13:11's stoning's rite THE WOOD-GATHERER'S CELL — the stones and the stone; stoned_as_commanded Num 15:36 on the tape)
import cold_run_temurah as TM                 # THE EDGE: seducers -> temurah CALL, reference (13:16's devoting Leviticus 27:28-29's devoted thing — the person put to death, the thing most holy)
import cold_run_chukat as CK                  # THE EDGE: seducers -> chukat CALL, reference (13:16's devoting Numbers 21:2-3's Hormah — the ban performed, cherem_vowed closed, destroyed on the king of Arad)
import cold_run_balak as BK                   # THE EDGE: seducers -> balak CALL, reference (13:18's anger Peor's — hanging_commanded Num 25:4 on the tape; the anger keyed to idolatry)
import cold_run_beha as BH                    # THE EDGE: seducers -> beha CALL, reference (13:2's dream Numbers 12:6-8's channel; 13:5's cloud the march's — cloud_lifted Num 10:11)
import cold_run_mamre as MM                   # THE EDGE: seducers -> mamre CALL, reference (13:4's testing Genesis 22:1's first seat — tested on the tape; Isaac at Moriah on the prophet's presumption)
import cold_run_holiness as HO                # THE EDGE: seducers -> holiness CALL, reference (13:9's five prohibitions against Leviticus 19:16 and 19:18's standing duties — the neighbor's blood, the great rule)

'''
# ---- the generic helper block from the chapter-12 runner, by content markers ----
a = PN.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = PN.index('def LEN(b, c, v): return len(words(b, c, v))'); b = PN.index('\n', b) + 1
helpers = PN[a:b]
assert helpers.count("def W12(v): return words('Deut', 12, v)") == 1
helpers = helpers.replace("def W12(v): return words('Deut', 12, v)", "def W13(v): return words('Deut', 13, v)")
assert 'W12' not in helpers and '12' not in re.sub(r'0x0591|0x05C7|0x05AF|0x05B0|0x05BD', '', helpers), [l for l in helpers.split('\n') if '12' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D13 = lambda v: ('Deut', 13, v)
NEG = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())
NV = len({v for (b, c, v) in by if b == 'Deut' and c == 13}); assert NV == 19, NV   # nineteen verses in the DB's numbering (the English's 12:32 the Hebrew's 13:1)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch13_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-bound asserts left to the reading) ----
SPAN = [(13, v) for v in range(1, 20)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 13, v)) for v in range(1, 20)}
ORDS = {v: ink_ordinals(verse_words('Deut', 13, v)) for v in range(1, 20)}
PARSED = {(13, v): n for v, n in NUMS.items() if n}
KINNUM = {k: ink_numbers(verse_words(*k)) for k in [('Deut', 17, 6), ('Deut', 19, 15), ('Deut', 17, 7), ('Deut', 17, 2), ('Deut', 12, 14), ('Lev', 24, 16), ('Exod', 22, 19)]}
TOKN = sum(len(W13(v)) for v in range(1, 20)); LETN = sum(len(x) for v in range(1, 20) for x in W13(v))
print('THE INK (printed before it is asserted): PARSED %s, ORDS %s, MARKS %s, TOKN %d, LETN %d, KINNUM %s' % (PARSED, {v: o for v, o in ORDS.items() if o}, {v: MARKS(13, v) for v in range(1, 20) if MARKS(13, v)}, TOKN, LETN, KINNUM))
assert PARSED == {(13, 13): [1]} and all(o == [] for o in ORDS.values()) and not any(MARKS(13, v) for v in range(1, 20)) and TOKN == 328 and NUMS[18] == [], (PARSED, ORDS, TOKN)   # ONE NUMBER VERSE (13:13 "in one of your cities" [1]), no ordinal, NO starred token; 328 tokens (measured at the reading); 13:18's "swore" no number
assert KINNUM == {('Deut', 17, 6): [2, 3, 1], ('Deut', 19, 15): [1, 2, 3], ('Deut', 17, 7): [], ('Deut', 17, 2): [1], ('Deut', 12, 14): [1], ('Lev', 24, 16): [], ('Exod', 22, 19): []}, KINNUM   # the reading's parser facts on the kin
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers — three blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# ---- THE PHRASES, censused over the whole DB", "# ---- ONKELOS OVER THE BOOK") + block("# ---- THE REGISTER (the D print)", "# ---- THE PARSER (the C print)")
lines = ink_block.split('\n')
DROP_PATTERNS = ('byw[', 'SG[', 'sg(', 'STORE_', 'VC[', 'LED[', 'LED ', 'sif[', 'sif_he', 'onk', 'Hb(', 'HB0(', 'SP_(', 'aramaic(', 'arm(', 'arm_e(', 'E(', 'kinrows(')
drop = [l for l in lines if any(p in l for p in DROP_PATTERNS)]
print('dropped (the store-, shelf- and Onkelos-bound lines):', len(drop), [d[:70] for d in drop])
assert len(drop) == 1, len(drop)   # READ FROM THE PRINT — the ketiv assert on byw (the store's written/read pair) the one store-bound line in the three blocks
lines = [l for l in lines if l not in drop]
STOP_OLD = "STOP = set('את ואת אשר כל וכל על ועל אל ואל לא ולא כי אם יהוה אלהיך אלהיכם לך לכם בו שם שמה גם מן ממך עד הוא היא אתם אתה אנכי אני לו לה בכל כאשר כן הימים היום אלה האלה בארץ הארץ אשר ואם או פן ופן'.split())"
STOP_NEW = ("STOP = set(('את ואת אשר כל וכל על ועל אל ואל '   # (the object marker, and-it, which, all, on, to — the particles)\n"
            "            'לא ולא כי אם יהוה אלהיך אלהיכם '   # (not, for, if; the LORD, your God)\n"
            "            'לך לכם בו שם שמה גם מן ממך עד '   # (to you, in it, there, also, from, until)\n"
            "            'הוא היא אתם אתה אנכי אני לו לה '   # (he, she, you, I, to him, to her)\n"
            "            'בכל כאשר כן הימים היום אלה האלה '   # (in all, as, so, the days, today, these)\n"
            "            'בארץ הארץ אשר ואם או פן ופן').split())   # (in the land, the land, which, and if, or, lest) — the stopword set glossed piece by piece (the lint's ninety-character window)")
assert lines.count(STOP_OLD) == 1, lines.count(STOP_OLD)
lines[lines.index(STOP_OLD)] = STOP_NEW
ink_block = '\n'.join(lines)
assert 'CS.' not in ink_block and 'SG[' not in ink_block and 'byw' not in ink_block and 'VC[' not in ink_block and 'STORE_' not in ink_block and 'sg(' not in ink_block and 'onk' not in ink_block and 'LED' not in ink_block, 'a store-, shelf- or Onkelos-bound name survived'
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 40, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE FOUR PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 13 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
SIGNS = WE.CAL_PARAMS['the_signs_status']['value']; DEATH = WE.CAL_PARAMS['the_prophets_death']['value']; TIMING = WE.CAL_PARAMS['the_execution_timing']['value']; INQ = WE.CAL_PARAMS['the_inquiries']['value']   # THE FOUR PARAMETERS read (exercised_by seducers) — never a constant in the code: the disputes recorded, the table the cell reads as data
CLOCK = {'counter': DATE(COUNTER), 'signs_arms': sorted(SIGNS), 'death_arms': sorted(DEATH), 'timing_arms': sorted(TIMING), 'inquiry_keys': sorted(INQ), 'no_marker': True}
assert CLOCK == {'counter': (40, 11, 1), 'signs_arms': ['r_akiva', 'r_yosei_hagelili', 'the_hearing'], 'death_arms': ['stoning', 'strangling', 'the_default'], 'timing_arms': ['r_akiva', 'r_yehuda', 'the_formula'], 'inquiry_keys': ['diligently_free', 'the_clock_datum', 'the_congruence', 'the_examinations', 'the_order', 'the_seven', 'the_tolerance', 'the_voiding'], 'no_marker': True}, CLOCK
assert SIGNS['r_yosei_hagelili'].startswith('THE DOMINION') and SIGNS['r_akiva'].startswith('THE FALLEN PROPHET') and DEATH['strangling'].startswith('R. Shimon') and DEATH['the_default'].startswith("the answer sheet's") and TIMING['r_akiva'].startswith('KEPT TO THE FESTIVAL') and INQ['the_seven'].startswith('the seven-year cycle') and INQ['the_congruence'].startswith("'THE THING CERTAIN'"), (SIGNS, DEATH, TIMING, INQ)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the false prophet's hearing, the LORD's testing, Israel's hearing and fearing, the condemned city's inquiry or the devoted thing's cleaving on Israel before this sitting; the three reused effects on israel_people alone) ----
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
OWN5 = ('false_prophet_hearing_barred', 'tested_by_the_lord', 'israel_hears_and_fears', 'condemned_city_inquiry_required', 'devoted_thing_cleaving_barred')
SEDUCER_WORDS = r"\\b(false_prophet\\w*|tested_by_the_lord|hears_and_fears|condemned_city\\w*|devoted_thing\\w*|evil_purged\\w*|city_devoted)\\b"
_ss = ledger_scan('israel_people', SEDUCER_WORDS); SEDUCERS_SCAN = None if _ss is None else [e for e in _ss if e not in OWN5]   # this sitting's own five excluded once the fold carries them
_rs = [effect_scan(e) for e in ('adding_barred', 'cleaving_commanded', 'pity_barred')]; REUSE_SCAN = None if any(r is None for r in _rs) else _rs
del _ss, _rs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
assert SEDUCERS_SCAN in ([], None), SEDUCERS_SCAN   # THE HOLES' GROUND — nothing on Israel named the five before this sitting (DE4)
assert REUSE_SCAN in ([['israel_people'], ['israel_people'], ['israel_people']], None), REUSE_SCAN   # the three reused effects on israel_people alone before the second entries
assert all(k in _FXV for k in OWN5 + ('evil_purged_from_the_midst', 'city_devoted')) and _FXV['adding_barred']['ledger_op'] == 'block' and all('THE DEUTERONOMY WALK 11b' in _FXV[e]['ink'] for e in ('adding_barred', 'cleaving_commanded', 'pity_barred')), 'the seven on the registry; the three reuses amended (add_types_ch13.py)'
INF_ABS = [(v, x) for v in range(1, 20) for x, m in by[('Deut', 13, v)] if m and re.match(r'^H(?:C/)?V.a$', m)]
STONING_DEUT = [s for s, _, _ in LEMT('5619', books=DT)]; STONING_LEVNUM = [s for s, _, _ in LEMT('7275', books=('Lev', 'Num'))]; STONING_BOTH = [s for s, _, _ in LEMT('7275', books=DT)]
PURGE_SEATS = P('ובערת', 'הרע')   # (and you shall purge the evil) — the formula's seats on the DB
assert len(INF_ABS) == 4 and STONING_DEUT == ['Deut 13:11', 'Deut 17:5', 'Deut 22:21', 'Deut 22:24'] and STONING_BOTH == ['Deut 21:21'] and len(STONING_LEVNUM) == 9 and len(PURGE_SEATS) == 9 and PURGE_SEATS[0] == 'Deut 13:6', (INF_ABS, STONING_DEUT, STONING_LEVNUM, STONING_BOTH, PURGE_SEATS)

# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own print — ch13_callees.out, read before any assert was typed; the older runners' cells take q and return a dict, the Deuteronomy runners' take (case, data) and return a tuple, temurah's takes a string, lev24's a default parameter — the print settled each form) ----
def V(x):
    """a cell's verdict whatever its form — the dict's v (or verdict), the tuple's first member"""
    return x.get('v', x.get('verdict', x)) if isinstance(x, dict) else (x[0] if isinstance(x, tuple) else x)
def FOUND(r):
    """a kin cell CALLED and answering — a tuple (verdict, effects, trail) whose verdict is in span, or a dict with its value"""
    if isinstance(r, dict): return 'v' in r or 'verdict' in r
    return isinstance(r, tuple) and isinstance(r[0], str) and not r[0].startswith('no verdict')
OH_ADD = OH.the_exhortation({'ask': 'add_nothing'}, OH.DATA); OH_DIM = OH.the_exhortation({'ask': 'diminish_nothing'}, OH.DATA); OH_BESIDE = OH.the_exhortation({'ask': 'add_beside'}, OH.DATA); OH_TIME = OH.the_exhortation({'ask': 'add_out_of_its_time'}, OH.DATA)
CH_OTHER = CH.the_second_word({'ask': 'no_other_gods'}, CH.DATA); CH_FIRST = CH.the_first_tablet({'ask': 'the_first_word'}, CH.DATA)
HI_TEST = HI.the_test_and_the_right({'ask': 'you_shall_not_test'}, HI.DATA); HI_RIGHT = HI.the_test_and_the_right({'ask': 'the_right_and_the_good'}, HI.DATA); HI_FEAR = HI.the_gift_and_the_warning({'ask': 'fear_serve_swear'}, HI.DATA); HI_GODS = HI.the_gift_and_the_warning({'ask': 'no_other_gods'}, HI.DATA)
SN_PITY = SN.because_you_hear({'ask': 'consume_no_pity'}, SN.DATA); SN_BAN = SN.the_seven_nations({'ask': 'the_ban'}, SN.DATA); SN_COND = SN.the_seven_nations({'ask': 'the_bans_condition'}, SN.DATA); SN_WOOD = SN.the_seven_nations({'ask': 'the_asherah_wood'}, SN.DATA)
SN_DEVLIKE = SN.the_images_and_the_devoted({'ask': 'devoted_like_it'}, SN.DATA); SN_HOUSE = SN.the_images_and_the_devoted({'ask': 'into_your_house'}, SN.DATA); SN_SNARED = SN.the_images_and_the_devoted({'ask': 'lest_snared'}, SN.DATA); SN_OATH = SN.the_holy_people({'ask': 'the_oath'}, SN.DATA); SN_REDEEMED = SN.the_holy_people({'ask': 'brought_out_redeemed'}, SN.DATA)
GL_TEST = GL.the_way_of_forty_years({'ask': 'the_test'}, GL.DATA); GL_HUMBLE = GL.the_way_of_forty_years({'ask': 'the_humbling'}, GL.DATA)
NR_INTER = NR.the_intercession({'ask': 'do_not_destroy_your_people'}, NR.DATA); NR_MERIT = NR.the_intercession({'ask': 'remember_your_servants'}, NR.DATA); NR_CALF = NR.the_calf_retold({'ask': 'gods_word_verbatim'}, NR.DATA)
ST_FOUR = ST.the_god_of_gods_and_the_stranger({'ask': 'fear_serve_cleave_swear'}, ST.DATA); ST_SCHOLARS = ST.the_god_of_gods_and_the_stranger({'ask': 'cleave_to_the_scholars'}, ST.DATA); ST_ATTR = ST.the_stations_and_the_death({'ask': 'walk_after_his_attributes'}, ST.DATA)
BC_CURSE = BC.the_blessing_and_the_curse({'ask': 'the_curse_if'}, BC.DATA); BC_HEARKEN = BC.the_second_paragraph({'ask': 'if_you_hearken'}, BC.DATA)
PN_ONE = PN.the_place_chosen({'ask': 'in_one_of_your_tribes'}, PN.DATA); PN_RIGHT = PN.the_border_enlarged_and_the_altar({'ask': 'the_good_and_the_right'}, PN.DATA); PN_INQ = PN.the_nations_cut_off_and_the_abomination({'ask': 'lest_you_inquire_after_their_gods'}, PN.DATA)
OR_IDOL = OR.capital('idolater_row'); OR_DEV = OR.capital('devoted_seats'); OR_SERV = OR.capital('service_architecture'); OR_ACQ = OR.courts('asymmetry'); OR_CIRC = OR.courts('circumstantial'); OR_DISS = OR.courts('dissenter'); OR_SIDE = OR.courts('begin_from_side'); OR_ENEMY = OR.courts('enemy_ox')
ER_FOUR = ER.calf('four_verbs'); ER_BOW = ER.calf('bow_likened'); ER_JOURN = ER.cloud('journeys'); ER_LIFT = ER.cloud('first_lifting')
SA_STONED = SA.census('stoned'); SA_STRANG = SA.census('strangled'); SA_BURNED = SA.census('burned'); SA_LASHES = SA.census('lashes'); SA_KARET = SA.census('karet_count'); SA_WHO = SA.molech('who_stones'); SA_FAM = SA.molech('family'); SA_CONC = SA.molech('concealed'); SA_WARNED = SA.frame('court_warned'); SA_KPERS = SA.frame('karet_persons'); SA_ORDERS = SA.severity('orders')
L24_TALION = L24.talion()
MK_STONES = MK.capital_procedure({'ask': 'stones_and_a_stone'}, MK.DATA); MK_STONING = MK.capital_procedure({'ask': 'stoning', 'died_at': 'the_first_stone'}, MK.DATA); MK_WARN = MK.capital_procedure({'ask': 'warning'}, MK.DATA); MK_VENUE = MK.capital_procedure({'ask': 'venue'}, MK.DATA); MK_HANG = MK.capital_procedure({'ask': 'hanging'}, MK.DATA); MK_MODE = MK.capital_procedure({'ask': 'mode'}, MK.DATA); MK_CUST = MK.capital_procedure({'ask': 'custody'}, MK.DATA); MK_BURIAL = MK.capital_procedure({'ask': 'burial'}, MK.DATA); MK_CONF = MK.capital_procedure({'ask': 'confession'}, MK.DATA)
TM_DEV = TM.devote('person'); TM_STATUS = TM.devote('status')
CK_CHEREM = CK.arad_and_the_serpent({'ask': 'cherem_law'}, CK.DATA); CK_HORMAH = CK.arad_and_the_serpent({'ask': 'hormah'}, CK.DATA)
BK_ANGER = BK.peor({'ask': 'anger_third'}, BK.DATA); BK_HANG = BK.peor({'ask': 'hang_before_the_sun'}, BK.DATA)
BH_DREAMS = BH.miriam({'ask': 'dreams'}, BH.DATA); BH_DIBBUR = BH.miriam({'ask': 'dibbur'}, BH.DATA); BH_CLOUD = BH.march({'ask': 'cloud_and_trumpets'}, BH.DATA); BH_ORDER = BH.march({'ask': 'order'}, BH.DATA)
MM_MORIAH = MM.moriah('test_verb_seats'); MM_TRIALS = MM.moriah('ten_trials_sheet')
HO_RULE = HO.conduct('great_rule'); HO_HATE = HO.conduct('hate'); HO_GRUDGE = HO.conduct('grudge'); HO_BLOOD = HO.conduct('blood', case='knows_testimony'); HO_SECRECY = HO.conduct('secrecy')
# the values asserted from the callees' print (ch13_callees.out — read before any assert was typed)
assert OH_ADD[0].startswith('you shall not add (4:2)') and OH_ADD[1] == ['accepted'] and OH_DIM[0].startswith('nor diminish (4:2)') and OH_BESIDE[0].startswith('an addition placed beside') and OH_TIME[1] == ['exempt'], (OH_ADD[:2], OH_DIM[0][:30], OH_BESIDE[0][:30], OH_TIME[1])
assert CH_OTHER[0].startswith('no other gods before me (5:7)') and CH_FIRST[0].startswith('the first word (5:6)') and HI_TEST[0].startswith('you shall not test (6:16)') and HI_RIGHT[0].startswith('the right and the good (6:18)') and HI_FEAR[0].startswith('fear, serve, swear (6:13)') and HI_GODS[0].startswith('no other gods (6:14)'), (CH_OTHER[0][:40], CH_FIRST[0][:30], HI_TEST[0][:30], HI_RIGHT[0][:30], HI_FEAR[0][:30], HI_GODS[0][:30])
assert SN_PITY[0].startswith('consume without pity (7:16)') and SN_WOOD[1] == ['lashes'] and SN_BAN[0].startswith('the ban (7:2)') and SN_COND[1] == ['exempt'] and SN_DEVLIKE[0].startswith('devoted like it (7:26)') and SN_HOUSE[0].startswith('the abomination into the house (7:26)') and SN_SNARED[0].startswith('lest snared (7:25)') and SN_OATH[0].startswith('the oath (7:8)') and SN_REDEEMED[0].startswith('brought out and redeemed (7:8)'), (SN_PITY[0][:30], SN_WOOD[1], SN_BAN[0][:20], SN_COND[1], SN_DEVLIKE[0][:30], SN_HOUSE[0][:40], SN_SNARED[0][:20], SN_OATH[0][:20], SN_REDEEMED[0][:30])
assert GL_TEST[0].startswith('the test (8:2)') and GL_HUMBLE[0].startswith('the humbling (8:2-3, 8:16)') and NR_INTER[0].startswith('do not destroy Your people (9:26)') and NR_MERIT[0].startswith('remember Your servants (9:27)') and NR_CALF[0].startswith("God's word (9:12-13)"), (GL_TEST[0][:30], GL_HUMBLE[0][:30], NR_INTER[0][:40], NR_MERIT[0][:40], NR_CALF[0][:30])
assert ST_FOUR[0].startswith('fear, serve, cleave, swear (10:20)') and ST_SCHOLARS[0].startswith('cleave to the scholars (Ketubot 111b:6-8)') and ST_ATTR[0].startswith('walk after His attributes (Sotah 14a:3-4)') and BC_CURSE[0].startswith('the curse if (11:28)') and BC_HEARKEN[0].startswith('if you hearken (11:13)'), (ST_FOUR[0][:40], ST_SCHOLARS[0][:40], ST_ATTR[0][:40], BC_CURSE[0][:30], BC_HEARKEN[0][:30])
assert PN_ONE[0].startswith('in one of your tribes (12:14)') and PN_RIGHT[0].startswith('the good and the right (12:28)') and PN_INQ[0].startswith('lest you inquire after their gods (12:30)'), (PN_ONE[0][:40], PN_RIGHT[0][:40], PN_INQ[0][:40])
assert OR_IDOL['v'] == 'serves_sacrifices_incense_libation_bows_accepts_says' and OR_DEV['v'] == 4 and OR_SERV['v'] == 'temple_services_for_any_idol' and OR_ACQ['v'] == 'acquit_by_one_convict_by_two' and OR_CIRC['v'] == 'no_execution_without_witnesses' and OR_DISS['v'] == 'bound_and_silent' and OR_SIDE['v'] == 'capital_from_the_side' and OR_ENEMY['v'] == 'return_it', (OR_IDOL['v'], OR_DEV['v'], OR_SERV['v'], OR_ACQ['v'], OR_CIRC['v'], OR_DISS['v'], OR_SIDE['v'], OR_ENEMY['v'])
assert len(ER_FOUR['v']) == 4 and ER_BOW['v'] == 'bowing_likened_to_sacrificing' and ER_JOURN['v'][0] == 6 and ER_LIFT['v'] == '20_iyar_year_2', (ER_FOUR['v'], ER_BOW['v'], ER_JOURN['v'][0], ER_LIFT['v'])
assert len(SA_STONED['v']) == 9 and SA_STRANG['v'] == ["a man's wife"] and SA_BURNED['v'] == ['a woman and her mother'] and len(SA_LASHES['v']) == 7 and SA_KARET['v'] == 20 and SA_WHO['v'] == 'the_people_of_the_land' and SA_FAM['v'] == 'afflictions_not_karet' and SA_CONC['v'] == 'karet_by_Heaven_and_his_family' and SA_WARNED['v'] == 'the_court_warned_over_the_charge' and SA_KPERS['v'] == 'man_and_woman_the_doers_not_the_approach' and SA_ORDERS['v']['sages'] == ['stoning', 'burning', 'killing', 'strangling'], (len(SA_STONED['v']), SA_STRANG['v'], SA_BURNED['v'], len(SA_LASHES['v']), SA_KARET['v'], SA_WHO['v'], SA_FAM['v'], SA_CONC['v'], SA_WARNED['v'], SA_KPERS['v'], SA_ORDERS['v'])
assert L24_TALION['verdict'] == 'PAY-MONEY' and MK_STONES[0].startswith('both verses fulfilled') and MK_STONING[0].startswith('stoned by all the people') and MK_STONING[1] == ['stoned'] and MK_WARN[1] == ['exempt'] and MK_VENUE[0].startswith('outside the court') and MK_HANG[0].startswith('not hanged') and MK_MODE[0].startswith('stoning') and MK_CUST[0].startswith('confined') and MK_BURIAL[1] == ['buried'] and MK_CONF[1] == ['confessed'], (L24_TALION['verdict'], MK_STONES[0][:30], MK_STONING[:2], MK_WARN[1], MK_VENUE[0][:20], MK_HANG[0][:12], MK_MODE[0][:10], MK_CUST[0][:10], MK_BURIAL[1], MK_CONF[1])
assert TM_DEV['v'] == 'put_to_death_not_ransomed' and TM_STATUS['v'] == 'most_holy_not_sold_not_redeemed' and CK_CHEREM[1] == ['destroyed'] and CK_HORMAH[1] == ['hormah_named'] and BK_ANGER[1] == ['mark_of_anger', 'plague_struck'] and BK_HANG[1] == ['commanded'], (TM_DEV['v'], TM_STATUS['v'], CK_CHEREM[1], CK_HORMAH[1], BK_ANGER[1], BK_HANG[1])
assert BH_DREAMS[0] == 'the prophets in dreams; Moses mouth to mouth, not in riddles' and BH_DIBBUR[0].startswith('harsh speech') and BH_CLOUD[0] == 'both kept — the cloud and the trumpets' and BH_ORDER[0].startswith('judah, reuben') and MM_MORIAH['v'] == 1 and MM_TRIALS['v'] == 10, (BH_DREAMS[0], BH_DIBBUR[0][:20], BH_CLOUD[0], BH_ORDER[0][:20], MM_MORIAH['v'], MM_TRIALS['v'])
assert HO_RULE['v'] == ['R._Akiva_love_your_neighbor', 'ben_Azzai_the_book_of_the_generations_of_man'] and HO_HATE['v'] == 'in_the_heart_only_is_the_ban' and HO_GRUDGE['v'] == 'lend_with_the_barb_I_am_not_like_you' and HO_BLOOD['v'] == 'may_not_stay_silent' and HO_SECRECY['v'] == 'the_leaving_judge_may_not_reveal_the_vote', (HO_RULE['v'], HO_HATE['v'], HO_GRUDGE['v'], HO_BLOOD['v'], HO_SECRECY['v'])
assert all(FOUND(r) for r in (OH_ADD, OH_DIM, OH_BESIDE, OH_TIME, CH_OTHER, CH_FIRST, HI_TEST, HI_RIGHT, HI_FEAR, HI_GODS, SN_PITY, SN_BAN, SN_COND, SN_WOOD, SN_DEVLIKE, SN_HOUSE, SN_SNARED, SN_OATH, SN_REDEEMED, GL_TEST, GL_HUMBLE, NR_INTER, NR_MERIT, NR_CALF, ST_FOUR, ST_SCHOLARS, ST_ATTR, BC_CURSE, BC_HEARKEN, PN_ONE, PN_RIGHT, PN_INQ, OR_IDOL, OR_DEV, OR_SERV, OR_ACQ, OR_CIRC, OR_DISS, OR_SIDE, OR_ENEMY, ER_FOUR, ER_BOW, ER_JOURN, ER_LIFT, SA_STONED, SA_STRANG, SA_BURNED, SA_LASHES, SA_KARET, SA_WHO, SA_FAM, SA_CONC, SA_WARNED, SA_KPERS, SA_ORDERS, L24_TALION, MK_STONES, MK_STONING, MK_WARN, MK_VENUE, MK_HANG, MK_MODE, MK_CUST, MK_BURIAL, MK_CONF, TM_DEV, TM_STATUS, CK_CHEREM, CK_HORMAH, BK_ANGER, BK_HANG, BH_DREAMS, BH_DIBBUR, BH_CLOUD, BH_ORDER, MM_MORIAH, MM_TRIALS, HO_RULE, HO_HATE, HO_GRUDGE, HO_BLOOD, HO_SECRECY)), 'a kin cell answered out of span'
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B
open(f'{SP}/ch13_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch13_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines' % (len(src), len(helpers), len(ink_block), n_as, len(drop)))
