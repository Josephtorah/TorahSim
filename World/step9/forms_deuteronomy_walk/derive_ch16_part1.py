import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b: cold_run_festivals_judges.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-15 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W15 made W16); THE INK BLOCK COPIED from the reading's own instrument
# ch16_ink.py by content markers — FOUR blocks (the kin by computation, the frames and the register on the morphology, the kin re-scored and the twins diffed, the
# formulas over the Torah and the Bible; the parser's facts and the divisions' count typed in the tail from the ink's own asserts — the ink script reads them through
# the sequence module and the store, a runner cannot import them), the store-, shelf- and Onkelos-bound lines DROPPED by name (10b's lesson 6 — the patterns listed
# with word boundaries, the count read from the print), the frames block's MO (the morphs) renamed MORPH (the moadim alias); the counter's day, the calendar's rows
# read, the one-database scans, and THE CALLEES' FACTS (typed in ch16_callees_facts.py from ch16_callees.out and ch16_callees2.out — read before any assert was typed).
# Asserted substitutions throughout. derive_ch15_part1.py's form, cut to the lean pass. RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
RF = open(f'{ROOT}/World/step9/cold_run_release_firstborn.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch16_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch16_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the prints (ch16_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 16:1-22 — THE PASSOVER AT THE PLACE (the month of Aviv and the intercalation, the name, flock and herd, the leaven's sixth hour and the two measures, the
# night's flesh, the gates' bar, the three phrases of the clock, the cooking, the lodging, six and seven, the seventh day's assembly and the intermediate days handed
# to the sages), THE WEEKS FROM THE SICKLE (the omer's three rules, reaping by night, the freewill measure, the three commandments of the pilgrimage, the household,
# the slave remembered), THE FEAST OF BOOTHS (the gathering, the booth's ownership, the roofing, the seven days at the place, the compensation, the joy's offering),
# THE THREE PILGRIMAGES (all the males, who appears, the order of the names, none empty, the two amounts, the gift of the hand, the guard of the land), THE JUDGES IN
# EVERY GATE (the court for all Israel and the three tiers, the qualified judge, no wresting, no faces, no bribe — its first entry, justice pursued and the acquittal
# final) and THE ASHERAH AND THE PILLAR (beside the altar, any tree, the pillar hated — the fathers' love on the tape); THE READBACK'S FORMS ON FILE, NO NEW FORM
# (THE DEUTERONOMY WALK sitting 14b — THE LEAN PASS, 2026-09-23; World/step9/DEUTERONOMY_WALK.md "Sitting 14b"; the state doc's #210). FIVE own-day lines at the
# counter's day (40, 11, 1), NO marker: passover_at_the_place_declared (16:1-8 — passover_at_the_place_commanded and seventh_day_assembly_commanded STATUSES;
# passover_in_the_gates_barred, leaven_with_the_passover_barred, flesh_till_morning_barred BLOCKS), weeks_and_booths_declared (16:9-15 — weeks_at_the_place_commanded,
# booths_at_the_place_commanded STATUSES), three_pilgrimages_declared (16:16-17 — three_pilgrimages_commanded a STATUS, empty_appearance_barred a BLOCK),
# judges_in_every_gate_commanded (16:18-20 — judges_and_officers_commanded and justice_pursuit_commanded STATUSES; judgment_wresting_barred, person_respecting_barred
# BLOCKS; bribe_barred REUSED — its FIRST entry anywhere), asherah_and_pillar_barred (16:21-22 — asherah_beside_the_altar_barred, pillar_barred BLOCKS). THE KIN'S
# CELLS BY CALL (fifteen runners, every edge REFERENCE); THE TAPE'S LINES BY KIND (the Passover kept, the courts established, the judges charged, the place chosen,
# the second tithe's rejoicing). Six cells and the table; every token probed (zero-report law); effects on every cell (the effects law); THE EXAM THE EIGHT MISHNAH
# ROWS THE SPINE CITES (Berakhot 1:5, Pesachim 3:7, Beitzah 1:1, Sukkah 1:4, Chagigah 1:1, 1:2, 1:4, 1:5 — read whole; no docket, the lean form); the parameters the
# runner's DATA rows (no clock datum added — the festivals' dates and the intercalation on file). The daemon law_festivals_judges given_at Deut 16:1, installed_by boot
# (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_16_reeh_shoftim_2026-09-23.md; the lean exam: deu_16_reeh_shoftim_exam_2026-09-23.md.

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
import effects_layer as FX
import world_engine as WE
import cold_run_pesach as PS                   # THE EDGE: festivals_judges -> pesach CALL, reference (16:1-7's Passover by name — the name, the eating until midnight, roasted only, the remainder burned; the leaven's window)
import cold_run_moadim as MO                   # THE EDGE: festivals_judges -> moadim CALL, reference (Leviticus 23's feasts by name — the slaughter window, the omer's morrow and count, the booths' seven, the seventh day's work class)
import cold_run_musafim as MU                  # THE EDGE: festivals_judges -> musafim CALL, reference (Numbers 28-29's dates, the seventh, Shavuot's redress by Deut 16:16's own analogy, the eighth)
import cold_run_calendar as CA                 # THE EDGE: festivals_judges -> calendar CALL, reference (Exodus 23:14-18's three times, the males, the leaven and the fat)
import cold_run_erection as ER                 # THE EDGE: festivals_judges -> erection CALL, reference (Exodus 34:18-26's repeats — the empty appearance's standing liability, the fourteenth's festival offering, the ingathering's turn, the cow grazes; 34:13's asherim by the answer sheet)
import cold_run_place_name as PN               # THE EDGE: festivals_judges -> place_name CALL, reference (the place formula's six seats; the rejoicing and the household; 12:17's gates; 12:3's asherim)
import cold_run_opening_speech as OP           # THE EDGE: festivals_judges -> opening_speech CALL, reference (1:16-17's charge — the qualities, no faces, the court of three)
import cold_run_exodus_story as ES             # THE EDGE: festivals_judges -> exodus_story CALL, reference (Exodus 18:21-25's courts — 78,600 judges, the Sanhedrin's sizes)
import cold_run_ordinances as OR               # THE EDGE: festivals_judges -> ordinances CALL, reference (Exodus 23:2-8's court — the poor, the majority, the bribe's block declared and never written)
import cold_run_holiness as HO                 # THE EDGE: festivals_judges -> holiness CALL, reference (Leviticus 19:15's two faces, the judge's five effects, the bribed judge's eyes)
import cold_run_second_tablets as ST           # THE EDGE: festivals_judges -> second_tablets CALL, reference (10:17's 'lifts no face and takes no bribe' — DB7's declaration; the permitted fee)
import cold_run_seven_nations as SN            # THE EDGE: festivals_judges -> seven_nations CALL, reference (7:5's asherim — the shade, the wood, the four objects)
import cold_run_covenant_at_horeb as CH        # THE EDGE: festivals_judges -> covenant_at_horeb CALL, reference (5:15's slave remembered — 16:12 verbatim in kind)
import cold_run_journeys as JR                 # THE EDGE: festivals_judges -> journeys CALL, reference (Numbers 33:52's figured stones — Leviticus 26:1's pillar by name)
import cold_run_pesach_sheni as PSH            # THE EDGE: festivals_judges -> pesach_sheni CALL, reference (the Passover in its season; the distant way)

'''
# ---- the generic helper block from the chapter-15 runner, by content markers ----
a = RF.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = RF.index('def LEN(b, c, v): return len(words(b, c, v))'); b = RF.index('\n', b) + 1
helpers = RF[a:b]
assert helpers.count("def W15(v): return words('Deut', 15, v)") == 1
helpers = helpers.replace("def W15(v): return words('Deut', 15, v)", "def W16(v): return words('Deut', 16, v)")
assert 'W15' not in helpers and '15' not in re.sub(r'2026-09-15|0x0591|0x05C7|0x05AF|0x05B0|0x05BD', '', helpers), [l for l in helpers.split('\n') if '15' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D16 = lambda v: ('Deut', 16, v)
NEG_T = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
NV = len({v for (b, c, v) in by if b == 'Deut' and c == 16}); assert NV == 22, NV   # twenty-two verses in both numberings (the identity — the reading's divisions assert)
TOKN = sum(len(W16(v)) for v in range(1, 23)); assert TOKN == 334, TOKN   # the chapter's tokens (the reading's divisions assert)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch16_ink.py — COPIED from the reading's instrument by content markers in four blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
SPAN = [(16, v) for v in range(1, 23)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
PARSE = {v: (ink_numbers(verse_words('Deut', 16, v)), ink_ordinals(verse_words('Deut', 16, v)), MARKS(16, v)) for v in range(1, 23)}
NUMV = [v for v in PARSE if PARSE[v][0]]; ORDV = [v for v in PARSE if PARSE[v][1]]; STARV = [v for v in PARSE if PARSE[v][2]]
print('THE INK (printed before it is asserted): PARSE %s, NUMV %s, ORDV %s, STARV %s, TOKN %d' % ({v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}, NUMV, ORDV, STARV, TOKN))
assert {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]} == {3: ([7], [], []), 4: ([7], [1], []), 5: ([1], [], []), 8: ([6], [7], []), 9: ([7, 7], [], ['שבעת*']), 13: ([7], [], []), 15: ([7], [], []), 16: ([3], [], [])}, {v: p for v, p in PARSE.items() if p[0] or p[1] or p[2]}   # EIGHT NUMBER VERSES, TWO ORDINALS (16:4 the first day, 16:8 the seventh), ONE STARRED token (16:9 "weeks" — the number word inside it, the mark glossed at the reading); the reading's parser assert
assert NUMV == [3, 4, 5, 8, 9, 13, 15, 16] and ORDV == [4, 8] and STARV == [9]
'''
# ---- THE INK BLOCKS from the reading's instrument, by content markers — four blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# ---- THE FRAMES AND THE REGISTER", "# ---- THE KIN BY COMPUTATION (the closest three") + block("# ---- THE KIN BY COMPUTATION (the closest three", "# ---- THE FORMULAS OVER THE TORAH") + block("# ---- THE FORMULAS OVER THE TORAH", "# ---- ONKELOS OVER THE BOOK")
lines = ink_block.split('\n')
DROP_RX = re.compile(r"(?<![A-Za-z_0-9])(byw|SG|sg|STORE_MISMATCH|VC|LED|sif|sif_he|onk|onk_he|Hb|HB0|SP_|aramaic|arm|arm_e|E|kinrows|heads|CS|H|A|HP|AP|sidx|glob|UIDS|PATCHED|OUT|EXP2DB)(?![A-Za-z_0-9])")
drop = [l for l in lines if not l.lstrip().startswith('#') and DROP_RX.search(l.split('   #')[0])]   # the code before its trailing comment — a comment's 'A section' is not the helper A(
print('dropped (the store-, shelf- and Onkelos-bound lines):', len(drop), [d[:70] for d in drop])
assert len(drop) == 0, [d[:100] for d in drop]   # READ FROM THE PRINT — the four blocks carry no store-, shelf- or Onkelos-bound line (the divisions block, the shelf block and the Onkelos block were not copied)
assert sum(1 for l in lines if re.search(r'\bMO\b', l)) >= 3 and not any('MORPH' in l for l in lines)
lines = [re.sub(r'\bMO\b', 'MORPH', l) for l in lines]   # the frames block's MO (the morphs by verse) renamed — MO is the moadim alias in this runner
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
n_as = ink_block.count('\nassert '); print('the ink block: %d lines, %d asserts' % (ink_block.count('\n'), n_as)); assert n_as >= 24, n_as
TAIL_B = '''
# ---- THE COUNTER'S DAY, THE CALENDAR'S ROWS READ AND THE ONE DATABASE SCANNED (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch, no clock datum added: the festivals' dates, the omer's day and the intercalation on file, read here never typed) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 16 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
CAL_FEST = WE.CAL_PARAMS['festival_dates']['value']; CAL_OMER = WE.CAL_PARAMS['omer_day']['value']; CAL_LEAP = WE.CAL_PARAMS['intercalated_month']['value']; CAL_THRESH = WE.CAL_PARAMS['intercalation_threshold_days']['value']; CAL_GROUNDS = WE.CAL_PARAMS['intercalation_grounds']['value']
CAL_LEAP_BY = WE.CAL_PARAMS['intercalated_month'].get('exercised_by'); CAL_BTE = WE.CAL_PARAMS['between_the_evenings_from']['value']['hour']
SLOTS = [d['name'] for d in yaml.safe_load(open(_os.path.join(HERE, 'calendar_parameters.yaml'), encoding='utf-8'))['day_slots']]
CLOCK = {'counter': DATE(COUNTER), 'passover': (CAL_FEST['passover']['month'], CAL_FEST['passover']['day']), 'passover_1': (CAL_FEST['passover_1']['month'], CAL_FEST['passover_1']['day']), 'passover_7': CAL_FEST['passover_7'], 'atzeret': CAL_FEST['atzeret'], 'sukkot_1': (CAL_FEST['sukkot_1']['month'], CAL_FEST['sukkot_1']['day']), 'omer_day': (CAL_OMER['month'], CAL_OMER['day']), 'leap': CAL_LEAP, 'threshold': CAL_THRESH, 'grounds': CAL_GROUNDS, 'leap_by': CAL_LEAP_BY, 'slots': SLOTS, 'between_the_evenings_from': CAL_BTE, 'no_marker': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1) and CLOCK['passover'] == (1, 14) and CLOCK['passover_1'] == (1, 15) and CLOCK['passover_7'] == {'from': 'passover_1', 'plus': 6} and CLOCK['atzeret'] == {'from': 'omer', 'plus': 49} and CLOCK['sukkot_1'] == (7, 15) and CLOCK['omer_day'] == (1, 16), CLOCK   # Leviticus 23's own keys on the registry (exercised_by moadim and pesach_sheni); the omer's day the sixteenth (the Sages against the Boethusians)
assert CLOCK['leap'] == {'position': 'after_month_12', 'length': 30} and CLOCK['threshold'] == 16 and CLOCK['grounds'] == ['spring_grain', 'tree_fruit', 'season'] and CLOCK['leap_by'] == ['count'] and CLOCK['slots'] == ['evening', 'night', 'midnight', 'dawn', 'morning', 'noon', 'between_the_evenings', 'sunset'] and CLOCK['between_the_evenings_from'] == 6.5, CLOCK   # THE INTERCALATION ON FILE FOR THE COUNT ERA ALONE (Sanhedrin 12b, 13a, 11b) — the exodus era's Aviv OWED (the debt line); the day slots the three phrases' seats (16:6)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the Passover at the place, the gates' bar, the leaven with it, the flesh till morning, the seventh day's assembly, the weeks or the booths at the place, the three pilgrimages, the empty appearance, the judges and officers, the wresting, the faces, the pursuit of justice, the asherah or the pillar on Israel before this sitting; the bribe's block NEVER written before — DB7; the kin's entities before) ----
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
OWN15 = ('passover_at_the_place_commanded', 'passover_in_the_gates_barred', 'leaven_with_the_passover_barred', 'flesh_till_morning_barred', 'seventh_day_assembly_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'three_pilgrimages_commanded', 'empty_appearance_barred', 'judges_and_officers_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'justice_pursuit_commanded', 'asherah_beside_the_altar_barred', 'pillar_barred')
HOLE_WORDS = r"^(passover_at_the\\w*|passover_in_the_gates\\w*|leaven_with\\w*|flesh_till\\w*|seventh_day_assembly\\w*|weeks_at\\w*|booths_at\\w*|three_pilgrim\\w*|empty_appearance\\w*|judges_and_officers\\w*|judgment_wrest\\w*|person_respect\\w*|justice_pursuit\\w*|asherah\\w*|pillar_barred)\\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN15]   # this sitting's own names excluded once the fold carries them
BRIBE_SCAN = effect_scan('bribe_barred'); BURN_SCAN = effect_scan('burn_remainder'); PLACE_SCAN = effect_scan('place_chosen_required'); REJOICE_SCAN = effect_scan('rejoicing_before_the_lord_commanded'); BOOTHS_SCAN = effect_scan('dwells_in_booths'); OMER_SCAN = effect_scan('counts_omer')
COURTS_SCAN = effect_scan('courts_established'); JUDGES_SCAN = effect_scan('judges_charged'); APPEAR_SCAN = (effect_scan('appearance_owed'), effect_scan('appearance_gift_owed')); PILLAR_SCAN = (effect_scan('pillar_anointed'), effect_scan('pillar_raised')); PERVERT_SCAN = effect_scan('judgment_perverted')
del _hs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
print('THE SCANS (printed before they are asserted): holes %s; bribe %s; burn %s; place %s; rejoice %s; booths %s; omer %s; courts %s; judges %s; appear %s; pillars %s; pervert %s' % (HOLE_SCAN, BRIBE_SCAN, BURN_SCAN, PLACE_SCAN, REJOICE_SCAN, BOOTHS_SCAN, OMER_SCAN, COURTS_SCAN, JUDGES_SCAN, APPEAR_SCAN, PILLAR_SCAN, PERVERT_SCAN))
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the fifteen before this sitting (DH4)
assert BRIBE_SCAN in ([], None, ['israel_people']), BRIBE_SCAN   # bribe_barred NEVER written before this sitting (DB7); ['israel_people'] once the fold carries 16:19's line — the scan's ground moved by this chapter's own write (the second-tablets callee's assert widened the same way)
assert BURN_SCAN in (['aaron-and-sons'], None) and PLACE_SCAN in (['israel_people'], None) and REJOICE_SCAN in (['israel_people'], None) and BOOTHS_SCAN in ([], None) and OMER_SCAN in ([], None) and COURTS_SCAN in (['israel_people'], None) and (JUDGES_SCAN is None or JUDGES_SCAN in (['the_court'], ['the-court'])) and APPEAR_SCAN in (([], []), (None, None)) and PILLAR_SCAN in ((['the_pillar_of_bethel'], ['the_pillar_of_gilead']), (None, None)) and PERVERT_SCAN in ([], None), (BURN_SCAN, PLACE_SCAN, REJOICE_SCAN, BOOTHS_SCAN, OMER_SCAN, COURTS_SCAN, JUDGES_SCAN, APPEAR_SCAN, PILLAR_SCAN, PERVERT_SCAN)   # the kin's entities as the recon read them from the snapshot: the pillars JACOB'S — the fathers' love on the tape (146:1)
assert all(k in _FXV for k in OWN15) and sum(1 for k in OWN15 if _FXV[k]['ledger_op'] == 'block') == 8 and sum(1 for k in OWN15 if _FXV[k]['ledger_op'] == 'status') == 7 and _FXV['bribe_barred']['ledger_op'] == 'block' and 'THE DEUTERONOMY WALK 14b' in _FXV['bribe_barred']['ink'], 'the fifteen on the registry; the bribe amended (add_types_ch16_a.py)'
# THE DB'S OWN SEATS for the DATA rows (every one computed here — the ink block above proves them at the reading's grain)
INF_ABS = [(v, x) for v in range(1, 23) for x, m in by[('Deut', 16, v)] if m and re.match(r'^H(?:C/)?V.a$', m)]
assert INF_ABS == [(1, 'שמור')], INF_ABS   # ONE infinitive absolute — "observe", the chapter's first word (the reading's frames assert)
TWIN = {'16:1 vs Exod 34:18': SH(D16(1), ('Exod', 34, 18)), '16:1 vs Exod 23:15': SH(D16(1), ('Exod', 23, 15)), '16:4 vs Exod 13:7': SH(D16(4), ('Exod', 13, 7)), '16:4 vs Exod 34:25': SH(D16(4), ('Exod', 34, 25)), '16:6 vs Exod 12:6': SH(D16(6), ('Exod', 12, 6)), '16:8 vs Exod 13:6': SH(D16(8), ('Exod', 13, 6)), '16:9 vs Lev 23:15': SH(D16(9), ('Lev', 23, 15)), '16:11 vs 12:18': SH(D16(11), ('Deut', 12, 18)), '16:11 vs 16:14': SH(D16(11), D16(14)), '16:12 vs 5:15': SH(D16(12), ('Deut', 5, 15)), '16:12 vs 24:18': SH(D16(12), ('Deut', 24, 18)), '16:16 vs Exod 34:23': SH(D16(16), ('Exod', 34, 23)), '16:16 vs Exod 23:17': SH(D16(16), ('Exod', 23, 17)), '16:17 vs 12:15': SH(D16(17), ('Deut', 12, 15)), '16:18 vs 1:16': SH(D16(18), ('Deut', 1, 16)), '16:19 vs Exod 23:8': SH(D16(19), ('Exod', 23, 8)), '16:20 vs 4:1': SH(D16(20), ('Deut', 4, 1)), '16:21 vs 7:5': SH(D16(21), ('Deut', 7, 5)), '16:22 vs 12:31': SH(D16(22), ('Deut', 12, 31))}
print('THE TWINS DIFFED (printed before they are asserted):', TWIN)
assert TWIN == {'16:1 vs Exod 34:18': 7, '16:1 vs Exod 23:15': 5, '16:4 vs Exod 13:7': 6, '16:4 vs Exod 34:25': 3, '16:6 vs Exod 12:6': 0, '16:8 vs Exod 13:6': 5, '16:9 vs Lev 23:15': 0, '16:11 vs 12:18': 13, '16:11 vs 16:14': 11, '16:12 vs 5:15': 5, '16:12 vs 24:18': 6, '16:16 vs Exod 34:23': 8, '16:16 vs Exod 23:17': 7, '16:17 vs 12:15': 6, '16:18 vs 1:16': 2, '16:19 vs Exod 23:8': 7, '16:20 vs 4:1': 6, '16:21 vs 7:5': 0, '16:22 vs 12:31': 2}, TWIN   # the twin laws diffed on the DB (DH4) — the reading's kin asserts read again here (SHN at the reading = the shared run)
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B + FACTS
open(f'{SP}/ch16_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch16_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS)))
