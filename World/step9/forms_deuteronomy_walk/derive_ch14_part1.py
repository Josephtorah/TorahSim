#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b: cold_run_food_tithe.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-13 runner by content markers
# (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W13 made W14); THE INK BLOCK COPIED from the reading's own instrument
# ch14_ink.py by content markers — THREE blocks (the kin by computation, the ink facts censused over the DB, the register computed on the morphology; the parser's
# facts typed in the tail from the ink's own asserts — the ink script reads them through the sequence module, a runner cannot import it), the store-, shelf- and
# Onkelos-bound lines DROPPED by name (10b's lesson 6 — the patterns listed; the count read from the print); the counter's day, the FIVE parameters, the one-database
# scans, the DB's own seats for the DATA rows, and THE CALLEES' FACTS (typed in ch14_callees_facts.py from ch14_callees.out — read before any assert was typed).
# Asserted substitutions throughout. derive_ch13_part1.py's form. RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
SE = open(f'{ROOT}/World/step9/cold_run_seducers.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch14_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the print (ch14_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 14:1-29 — THE SONS AND THE CUTTINGS, THE FOOD LAW (THE BEASTS, THE WATER, THE BIRDS — THE TWIN CHAPTER LEVITICUS 11 BY CALL), THE CARCASS AND THE
# KID, THE SECOND TITHE WITH THE FAR PLACE, THE MONEY, THE REJOICING AND THE LEVITE, THE THIRD YEAR'S TITHE; THE READBACK'S FORMS ON FILE, NO NEW FORM (THE
# DEUTERONOMY WALK sitting 12b, 2026-09-22; World/step9/DEUTERONOMY_WALK.md "Sitting 12b"; the state doc's #205). THE CODE'S FIVE HOLES compiled at the counter's
# day (40, 11, 1), FIVE own-day lines, NO marker: the sons and the cuttings (14:1-2 — cuttings_for_the_dead_barred a BLOCK: the cut and the factions from one word,
# the baldness by the analogy run both ways with the priests'), the food law (14:3-20 — abomination_eating_barred a BLOCK over the twin chapter's classifier by
# CALL; the ten named and no more, the four closed by 'it', the fetus from 14:6's own words; the_birds_signs a PARAMETER in three layers — the code/data separation
# law's own case), the carcass and the kid (14:21 — carcass_eating_barred a BLOCK, the ban's seat named by the sanctions engine itself; the_carcass_table a PARAMETER
# with the precedence; the kid NO NEW WRITE — the third seat's gain the assignment, calendar.kid_in_milk by CALL), the second tithe (14:22-27 — second_tithe_owed
# a STATUS: the liabilities, the wall's two capacities, the House standing, the exile's arm; the_moneys_form a PARAMETER with the possession clause; the class
# from the four named by general-particular-general — Nazir 35b:3 the chapter's verse the source of the method; rejoicing_before_the_lord_commanded and
# levite_forsaking_barred REUSED — second entries), the third year (14:28-29 — poor_tithe_owed a STATUS: one tithe not two, the Levite never interrupted;
# the_removal_date and the_tithes_new_year CLOCK DATA, the count's year by CALL to the cycle). THE KIN'S CELLS BY CALL (eighteen runners); THE TAPE'S LINES BY
# KIND (Abram's tenth, Jacob's vow, Noah's altar, the treasured people, the Levites' portion, the nations devoted, the stranger loved, the place chosen, the
# profane slaughter). Seven cells and the table; every token probed (zero-report law); effects on every cell (the effects law); the DATA rows the docket added.
# The daemon law_food_tithe given_at Deut 14:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_14_reeh_2026-09-21.md;
# the exam's docket: deu_14_reeh_exam_2026-09-21.md (991 rows — 771 READ WHOLE in two runs, 220 carried with their ledgers' own verdicts: LAW 188 / DERIVATION 394
# / DISPUTE 117 / CONTEXT 109 / OUTSIDE 183).

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
import cold_run_shemini as SHM                 # THE EDGE: food_tithe -> shemini CALL, reference (14:3-20 THE TWIN CHAPTER'S CLASSIFIER — the beasts' two signs, the water's two, the birds by name; the four the classifier's own exception rows; 14:8's carcass touched)
import cold_run_sanctions as SA                # THE EDGE: food_tithe -> sanctions CALL, reference (14:21's carcass ban named by the sanctions engine's own lashed cell — 'the ban is Deut 14:21 / Exod 22:30'; the lashes by CALL)
import cold_run_calendar as CA                 # THE EDGE: food_tithe -> calendar CALL, reference (14:21's kid the third seat — cook, eat, benefit; 14:28's seventh year the sabbatical's timer)
import cold_run_erection as ER                 # THE EDGE: food_tithe -> erection CALL, reference (34:26 the kid's second seat across files)
import cold_run_ordinances as OR               # THE EDGE: food_tithe -> ordinances CALL, reference (Exodus 22:30's torn — to the dogs; 14:23's firstlings)
import cold_run_priesthood as PR               # THE EDGE: food_tithe -> priesthood CALL, reference (21:5's baldness per spot and the whole head — the analogy both ways; 22:8's priest and the carcass)
import cold_run_holiness as HO                 # THE EDGE: food_tithe -> holiness CALL, reference (19:9-10's gifts — left_for_the_poor; GIFTS_IMPORT names 14:28 already)
import cold_run_holiness_b as HB               # THE EDGE: food_tithe -> holiness_b CALL, reference (19:27-28's cuttings for a soul — 14:1's kin)
import cold_run_moadim as MO                   # THE EDGE: food_tithe -> moadim CALL, reference (23:22's harvest left for the poor and the stranger)
import cold_run_temurah as TM                  # THE EDGE: food_tithe -> temurah CALL, reference (27:32's tenth an ordinal; the cattle tithe's answer sheet; no animal tithe now by decree)
import cold_run_korach as KO                   # THE EDGE: food_tithe -> korach CALL, reference (Numbers 18's first tithe — the second named against it; the Levites' portion; the courtyard's liability)
import cold_run_yovel as YO                    # THE EDGE: food_tithe -> yovel CALL, reference (the sabbatical cycle — the third and the sixth year the poor man's, the seventh exempt)
import cold_run_seven_nations as SN            # THE EDGE: food_tithe -> seven_nations CALL, reference (7:6's holy people — 14:2 and 14:21's clause; treasured_people unmoved)
import cold_run_second_tablets as ST           # THE EDGE: food_tithe -> second_tablets CALL, reference (10:9's Levites separated; 10:18's stranger, fatherless and widow)
import cold_run_place_name as PN               # THE EDGE: food_tithe -> place_name CALL, reference (12:5-14's place chosen — the formula's fourth and fifth seats; 12:15-19's gates; 12:21's far clause; the two reuses)
import cold_run_primeval as PV                 # THE EDGE: food_tithe -> primeval CALL, reference (Genesis 14:20's tithe_given — Abram's tenth; 8:20's clean beasts)
import cold_run_mamre as MM                    # THE EDGE: food_tithe -> mamre CALL, reference (Genesis 28:20-22's vowed — Jacob's tithe, the debit open)
import cold_run_seducers as SE                 # THE EDGE: food_tithe -> seducers CALL, reference (13:1's word sealed — the block's header; the tape's last Deuteronomy 13 line the five new lines' predecessor)

'''
# ---- the generic helper block from the chapter-13 runner, by content markers ----
a = SE.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = SE.index('def LEN(b, c, v): return len(words(b, c, v))'); b = SE.index('\n', b) + 1
helpers = SE[a:b]
assert helpers.count("def W13(v): return words('Deut', 13, v)") == 1
helpers = helpers.replace("def W13(v): return words('Deut', 13, v)", "def W14(v): return words('Deut', 14, v)")
assert 'W13' not in helpers and '13' not in re.sub(r'0x0591|0x05C7|0x05AF|0x05B0|0x05BD', '', helpers), [l for l in helpers.split('\n') if '13' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D14 = lambda v: ('Deut', 14, v)
NEG = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure (the shemini module is SHM)
NV = len({v for (b, c, v) in by if b == 'Deut' and c == 14}); assert NV == 29, NV   # twenty-nine verses in both numberings

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch14_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
SPAN = [(14, v) for v in range(1, 30)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 14, v)) for v in range(1, 30)}
ORDS = {v: ink_ordinals(verse_words('Deut', 14, v)) for v in range(1, 30)}
PARSED = {(14, v): n for v, n in NUMS.items() if n}
KINNUM = {k: ink_numbers(verse_words(*k)) for k in [('Deut', 15, 1), ('Deut', 31, 10), ('Exod', 23, 10), ('Lev', 11, 3), ('Lev', 27, 30), ('Num', 18, 21), ('Deut', 26, 12), ('Deut', 12, 17)]}
STARRED = sorted({(c, v, t) for (b, c, v) in by if b == 'Deut' for t in verse_words(b, c, v) if (t.startswith('מעשר') or t.startswith('עשר') or t.startswith('תעשר')) and t[-1] in '#~^%@|*'})
TOKN = sum(len(W14(v)) for v in range(1, 30)); LETN = sum(len(x) for v in range(1, 30) for x in W14(v))
print('THE INK (printed before it is asserted): PARSED %s, ORDS %s, MARKS %s, TOKN %d, LETN %d, KINNUM %s, STARRED %s' % (PARSED, {v: o for v, o in ORDS.items() if o}, {v: MARKS(14, v) for v in range(1, 30) if MARKS(14, v)}, TOKN, LETN, KINNUM, STARRED))
assert PARSED == {(14, 6): [2], (14, 28): [3]} and all(o == [] for o in ORDS.values()) and {v: MARKS(14, v) for v in range(1, 30) if MARKS(14, v)} == {6: ['שתי^'], 22: ['עשר*'], 23: ['מעשר*'], 28: ['שנים*', 'מעשר*']} and TOKN == 351, (PARSED, ORDS, TOKN)   # TWO NUMBER VERSES (14:6 "two hoofs" [2], 14:28 "three years" [3]); THE STARRED TITHE TOKENS at 14:22, 23, 28 (the number word "ten" inside "tithe", marked, no number read); 351 tokens (measured at the reading)
assert KINNUM[('Deut', 15, 1)] == [7] and KINNUM[('Deut', 31, 10)] == [7] and KINNUM[('Exod', 23, 10)] == [6] and KINNUM[('Lev', 11, 3)] == [] and KINNUM[('Lev', 27, 30)] == [] and KINNUM[('Num', 18, 21)] == [], KINNUM   # the reading's parser facts on the kin (15:1's and 31:10's seven, Exodus 23:10's six; the others no number)
assert [(c, v) for c, v, _ in STARRED] == [(12, 17), (14, 22), (14, 23), (14, 28), (26, 12)] or [(c, v) for c, v, _ in STARRED][:4] == [(12, 17), (14, 22), (14, 23), (14, 28)], STARRED   # the starred tithe tokens in the book — 14:22, 23, 28 the chapter's three (12:17 and 26:12 the book's others)
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers — three blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# ---- THE TWO DIVISIONS AND THE VERSES ----", "# ---- THE REGISTER (the D print)") + block("# ---- THE REGISTER (the D print)", "# ---- THE PARSER (the C print)")
lines = ink_block.split('\n')
DROP_PATTERNS = ('byw[', 'SG[', 'sg(', 'STORE_', 'VC[', 'LED[', 'LED ', 'sif[', 'sif_he', 'onk', 'Hb(', 'HB0(', 'SP_(', 'aramaic(', 'arm(', 'arm_e(', 'E(', 'kinrows(', 'heads[', 'CS.')
drop = [l for l in lines if any(p in l for p in DROP_PATTERNS)]
print('dropped (the store-, shelf- and Onkelos-bound lines):', len(drop), [d[:70] for d in drop])
assert len(drop) == 2, len(drop)   # READ FROM THE PRINT — the two divisions' Onkelos assert (onk, VC) and the register's store assert (byw, STORE_MISMATCH)
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
assert 'CS.' not in ink_block and 'SG[' not in ink_block and 'byw' not in ink_block and 'VC[' not in ink_block and 'STORE_' not in ink_block and 'sg(' not in ink_block and 'onk' not in ink_block and 'LED' not in ink_block and 'heads[' not in ink_block, 'a store-, shelf- or Onkelos-bound name survived'
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 40, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE FIVE PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch; the calendar's own keys read for the clock data) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 14 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
BIRDS = WE.CAL_PARAMS['the_birds_signs']['value']; CARC = WE.CAL_PARAMS['the_carcass_table']['value']; MONEY = WE.CAL_PARAMS['the_moneys_form']['value']; REMOVAL = WE.CAL_PARAMS['the_removal_date']['value']; NEWYEAR = WE.CAL_PARAMS['the_tithes_new_year']['value']   # THE FIVE PARAMETERS read (exercised_by food_tithe) — never a constant in the code: the disputes recorded, the clock data the calendar's
FEST = WE.CAL_PARAMS['festival_dates']['value']
CLOCK = {'counter': DATE(COUNTER), 'birds_layers': sorted(BIRDS), 'carcass_arms': sorted(CARC), 'money_arms': sorted(MONEY), 'removal_keys': sorted(REMOVAL), 'new_year_keys': sorted(NEWYEAR), 'the_removal_eve_key': 'passover_7', 'the_tithes_new_year_key': 'rosh_hashanah', 'no_marker': True}
assert CLOCK == {'counter': (40, 11, 1), 'birds_layers': ['the_four_signs', 'the_lists', 'the_ruling', 'the_tradition'], 'carcass_arms': ['r_meir', 'r_yehuda', 'the_carcass_defined', 'the_customs_bar', 'the_precedence', 'the_sanction'], 'money_arms': ['r_akiva', 'r_yishmael', 'the_possession', 'the_three_moneys'], 'removal_keys': ['one_tithe_not_two', 'the_eve', 'the_uses', 'the_years'], 'new_year_keys': ['shevat_15', 'the_first_third', 'tishri_1', 'year_by_year'], 'the_removal_eve_key': 'passover_7', 'the_tithes_new_year_key': 'rosh_hashanah', 'no_marker': True}, CLOCK
assert BIRDS['the_four_signs'].startswith('an extra toe') and BIRDS['the_ruling'].startswith('ONE SIGN AND NO CLAWING') and BIRDS['the_tradition'].startswith('A CLEAN BIRD IS EATEN BY TRADITION') and CARC['r_meir'].startswith('BOTH TO BOTH') and CARC['r_yehuda'].startswith('AS WRITTEN') and CARC['the_precedence'].startswith('GIVING TO THE RESIDENT ALIEN COMES FIRST') and MONEY['r_yishmael'].startswith('THE BLANK') and MONEY['r_akiva'].startswith('THE IMPRINT') and MONEY['the_possession'].startswith('IN ONE') and REMOVAL['the_eve'].startswith('THE EVE OF THE LAST FESTIVAL DAY OF PASSOVER') and REMOVAL['one_tithe_not_two'].startswith('the poor man') and NEWYEAR['tishri_1'].startswith('THE FIRST OF TISHRI') and NEWYEAR['the_first_third'].startswith('THE FIRST THIRD') and NEWYEAR['shevat_15'].startswith('THE FIFTEENTH OF SHEVAT'), (BIRDS, CARC, MONEY, REMOVAL, NEWYEAR)
assert FEST['passover_7'] == {'from': 'passover_1', 'plus': 6} and FEST['passover_1'] == {'month': 1, 'day': 15} and FEST['rosh_hashanah'] == {'month': 7, 'day': 1}, FEST   # the removal's eve the calendar's own key (the seventh day of Passover, the eve before it); the tithes' new year the calendar's key — read, never typed

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the cuttings for the dead, the abomination's eating, the carcass's eating, the second tithe or the poor man's tithe on Israel before this sitting; the two reused effects on israel_people alone) ----
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
OWN5 = ('cuttings_for_the_dead_barred', 'abomination_eating_barred', 'carcass_eating_barred', 'second_tithe_owed', 'poor_tithe_owed')
FOOD_WORDS = r"\\b(cuttings_for_the_dead\\w*|abomination_eating\\w*|carcass_eating\\w*|second_tithe\\w*|poor_tithe\\w*)\\b"
_fs = ledger_scan('israel_people', FOOD_WORDS); FOOD_SCAN = None if _fs is None else [e for e in _fs if e not in OWN5]   # this sitting's own five excluded once the fold carries them
_rs = [effect_scan(e) for e in ('rejoicing_before_the_lord_commanded', 'levite_forsaking_barred')]; REUSE_SCAN = None if any(r is None for r in _rs) else _rs
del _fs, _rs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
assert FOOD_SCAN in ([], None), FOOD_SCAN   # THE HOLES' GROUND — nothing on Israel named the five before this sitting (DF4)
assert REUSE_SCAN in ([['israel_people'], ['israel_people']], None), REUSE_SCAN   # the two reused effects on israel_people alone before the second entries
assert all(k in _FXV for k in OWN5) and _FXV['cuttings_for_the_dead_barred']['ledger_op'] == 'block' and _FXV['second_tithe_owed']['ledger_op'] == 'status' and all('THE DEUTERONOMY WALK 12b' in _FXV[e]['ink'] for e in ('rejoicing_before_the_lord_commanded', 'levite_forsaking_barred')), 'the five on the registry; the two reuses amended (add_types_ch14.py)'
# THE DB'S OWN SEATS for the DATA rows (every one computed here — the ink block above proves them at the reading's grain)
INF_ABS = [(v, x) for v in range(1, 30) for x, m in by[('Deut', 14, v)] if m and re.match(r'^H(?:C/)?V.a$', m)]
KID_SEATS = P('לא', 'תבשל', 'גדי', 'בחלב', 'אמו'); HOLY_PEOPLE = P('כי', 'עם', 'קדוש', 'אתה', 'ליהוה', 'אלהיך'); PORTION = P('חלק', 'ונחלה'); FOUR_AT_GATE = P('והגר', 'והיתום', 'והאלמנה')
PLACE_FORMULA = P('במקום', 'אשר', 'יבחר', books=DT); TITHE_TOKENS = [(s, x) for s, x, _ in LEMT('4643', books=T)]; REJOICE = U('ושמחת', 'ושמחתם', books=DT); THREE_YEARS = P('מקצה', 'שלש', 'שנים'); SEVEN_YEARS = P('מקץ', 'שבע', 'שנים')
TWIN = {'14:6 vs 11:3': SH(D14(6), ('Lev', 11, 3)), '14:7 vs 11:4': SH(D14(7), ('Lev', 11, 4)), '14:8 vs 11:7': SH(D14(8), ('Lev', 11, 7)), '14:9 vs 11:9': SH(D14(9), ('Lev', 11, 9)), '14:15 vs 11:16': SH(D14(15), ('Lev', 11, 16)), '14:15 == 11:16': W14(15) == words('Lev', 11, 16), '14:2 vs 7:6': SH(D14(2), ('Deut', 7, 6)), '14:24 vs 12:21': SH(D14(24), ('Deut', 12, 21)), '14:29 vs 24:19': SH(D14(29), ('Deut', 24, 19)), '14:29 vs 14:27': SH(D14(29), D14(27)), '14:21 vs 23:19': SH(D14(21), ('Exod', 23, 19))}
print('THE DB\\'S OWN SEATS (printed before they are asserted): INF_ABS %s; the kid %s; the holy people %s; portion and inheritance %d; the four at the gate %s; the place formula %d; the tithe tokens %d; rejoice %d; three years %s; seven years %s; TWIN %s' % (INF_ABS, KID_SEATS, HOLY_PEOPLE, len(PORTION), FOUR_AT_GATE, len(PLACE_FORMULA), len(TITHE_TOKENS), len(REJOICE), THREE_YEARS, SEVEN_YEARS, TWIN))
assert INF_ABS == [(21, 'מכר'), (22, 'עשר')] and KID_SEATS == ['Deut 14:21', 'Exod 23:19', 'Exod 34:26'] and HOLY_PEOPLE == ['Deut 14:2', 'Deut 14:21', 'Deut 7:6'] and len(PORTION) == 6 and FOUR_AT_GATE == ['Deut 14:29', 'Deut 16:11', 'Deut 16:14'] and len(PLACE_FORMULA) == 11 and len(TITHE_TOKENS) == 17 and len(REJOICE) == 8 and THREE_YEARS == ['2Kgs 18:10', 'Deut 14:28'] and SEVEN_YEARS == ['Deut 15:1', 'Deut 31:10', 'Jer 34:14'], (INF_ABS, KID_SEATS, HOLY_PEOPLE, PORTION, FOUR_AT_GATE, PLACE_FORMULA, TITHE_TOKENS, REJOICE, THREE_YEARS, SEVEN_YEARS)
assert TWIN['14:6 vs 11:3'] == 9 and TWIN['14:7 vs 11:4'] == 16 and TWIN['14:8 vs 11:7'] == 10 and TWIN['14:9 vs 11:9'] == 12 and TWIN['14:15 vs 11:16'] == 10 and TWIN['14:15 == 11:16'] is True and TWIN['14:2 vs 7:6'] == 18 and TWIN['14:29 vs 24:19'] == 7 and TWIN['14:29 vs 14:27'] == 6 and TWIN['14:21 vs 23:19'] == 6, TWIN   # the twin diffed on the DB (DF8) — 14:15 = 11:16 to the letter; 14:2 = 7:6 eighteen of nineteen; 14:24's twelve with 12:21 read from the print
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B + FACTS
open(f'{SP}/ch14_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch14_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS)))
