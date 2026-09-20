#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b: cold_run_second_tablets.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-9 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W9 made W10); THE INK BLOCK COPIED from the reading's own
# instrument ch10_ink_body.py by content markers (the parser's five number verses through the seventy's forms — every assert PROVEN at sitting 8, the
# sequence module's names made the exec'd parser's); the clock's arithmetic and the one-database scans typed. Asserted substitutions throughout.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
NR = open(f'{ROOT}/World/step9/cold_run_not_righteousness.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_ink_body.py', encoding='utf-8').read()
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 10:1-22 — THE SECOND TABLETS AND THE ARK, THE STATIONS AND AARON'S DEATH, THE LEVITES SEPARATED, THE THIRD FORTY AND THE GO, WHAT THE LORD
# ASKS, THE GOD OF GODS AND THE STRANGER — THE READBACK'S FORMS COMBINED, NO SEVENTH (THE DEUTERONOMY WALK sitting 8b, 2026-09-20; World/step9/DEUTERONOMY_WALK.md
# "Sitting 8b"; the state doc's #197). The chapter is the retelling's tail (10:1-11) and the laws' head (10:12-22): its rows take the forms already on file —
# T1 reference rows against the tape's lines by kind and first verse or the kin's cells by CALL; T2 SUPPLIED WITH A WRITE, TWICE — THE FRAGMENTS IN THE ARK
# (10:2 'and you shall put them in the ark', read of both sets by Menachot 99a:12 and Bava Batra 14b:6) and AARON'S BURIAL (10:6 'and he was buried there',
# the Torah's one seat), two acts TOLD ONLY HERE, each written ONCE at its own day by a RETROGRADE marker (Deut 10:2 at the erection's day (2, 1, 1) —
# M['fragments_told'] = M['erected']; Deut 10:6 at Aaron's death (40, 5, 1) — M['burial_told'] = M['aaron_death']; reading_placed), the writes
# fragments_in_the_ark (a STATUS on the ark — THE VALUE FROM THE DOCKET: the tablets and the fragments, the scroll inside or beside) and buried (the STATUS
# REUSED — Aaron the world's ninth); T6 ONE stretch row — 10:10's third forty measured on the clock (the second ascent's marker at Exod 34:4 to the timers'
# fire at (1, 7, 10) = 40; THE SECOND ASCENT'S DATE MATCHES SEDER OLAM RABBAH 6:2 — 7b's OPEN row CLOSED); T4 THE LAWS' FORM on 10:12-22 — every row against
# the cell that compiles it, by CALL, and THE CODE'S FOUR HOLES compiled at the chapter's own day (40, 11, 1) after the FORWARD marker at 10:12: the demand
# (fear_of_heaven_asked — THE SHELF'S NAME, Berakhot 33b:23), the heart and the neck (heart_circumcision_commanded — the evil inclination, Sukkah 52a:7;
# stiffening_barred — the chapter's one prohibition, no lashes), the stranger's love (love_owed — Leviticus 19:34's effect written on the tape for the
# first time), the cleaving (cleaving_commanded — the scholars, Ketubot 111b:7; the positive form, Temurah 4a:2); an OPEN row (the place of the death —
# Moserah / Mount Hor, the retreat of seven stations already a parameter); a HOLE outside the span (the go — Exodus 32:34's and 33:1's speeches have no
# line). The daemon law_second_tablets given_at Deut 10:1, installed_by boot (the Deuteronomy daemons' form). Six cells; every token probed (zero-report
# law); effects on every cell (the effects law); the DATA rows the docket added (the two arks of the Tosefta, the ark's contents' two arms, the grammar
# guard, the inclination's name, the burial among the attributes, the positive form, the intake, the editor's 'first of Tammuz' variant). Reading ledger:
# logic/oral_triage/deu_10_ekev_2026-09-19.md (25 sources, 6 claims); the exam's docket: deu_10_ekev_exam_2026-09-20.md (532 rows READ WHOLE FROM THE
# START: LAW 78 / DERIVATION 76 / DISPUTE 14 / CONTEXT 117 / OUTSIDE 247).

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
import cold_run_erection as ER                 # THE EDGE: second_tablets -> erection CALL, reference (the second ascent's marker and the timers' fire — the third forty on the clock; the fragments by call; the breaking ratified; the finger and the forms; the Levites gathered at the calf)
import cold_run_sanctuary_build as SB          # THE EDGE: second_tablets -> sanctuary_build CALL, reference (the ark's spec and making — both in the ark, the named maker, the hands on the ark; the testimony placed)
import cold_run_covenant_at_horeb as CH        # THE EDGE: second_tablets -> covenant_at_horeb CALL, reference (5:22's tablets given to me — 10:4's row)
import cold_run_obey_horeb as OH               # THE EDGE: second_tablets -> obey_horeb CALL, reference (4:1's 'and now, Israel'; 4:39's heaven and earth; 4:37's chosen seed; 4:4's cleaving STATE; 4:13's tablets_given; 4:9's 'your eyes have seen')
import cold_run_not_righteousness as NR        # THE EDGE: second_tablets -> not_righteousness CALL, reference (chapter 9's continuation — the finger, the breaking, the fragments owed, the forties, the hearkening)
import cold_run_journeys as JO                 # THE EDGE: second_tablets -> journeys CALL, reference (the stations in another order — Moseroth seven camps before Hor; the retreat of seven stations the parameter; Aaron's death retold)
import cold_run_chukat as CK                   # THE EDGE: second_tablets -> chukat CALL, reference (Aaron's death and succession at Hor; Moserah the parameter; Arad heard; the death's dates)
import cold_run_bamidbar as BM                 # THE EDGE: second_tablets -> bamidbar CALL, reference (the Kohathites carry the ark — 10:8's first office; the Levites given instead of the firstborn)
import cold_run_beha as BH                     # THE EDGE: second_tablets -> beha CALL, reference (the ark's bearers on the march; the Levites' rite and service)
import cold_run_korach as KR                   # THE EDGE: second_tablets -> korach CALL, reference (the watch — 'to stand before the LORD to minister'; 'separated' at 16:9; the portion declared and the tithe)
import cold_run_naso as NS                     # THE EDGE: second_tablets -> naso CALL, reference (the blessing in His name — 10:8's third office; the face lifted thrice reconciled against 10:17)
import cold_run_joseph as JS                   # THE EDGE: second_tablets -> joseph CALL, reference (the seventy — 10:22's count by CALL; Jochebed the seventieth)
import cold_run_hear_o_israel as HI            # THE EDGE: second_tablets -> hear_o_israel CALL, reference (6:5's creed against 10:12's five infinitives; 6:13's three clauses against 10:20's four; 6:1's header)
import cold_run_good_land as GL                # THE EDGE: second_tablets -> good_land CALL, reference (8:6's keep, walk, fear; 8:7's brooks of water at Jotbathah)
import cold_run_seven_nations as SN            # THE EDGE: second_tablets -> seven_nations CALL, reference (7:7's delight and choice; 7:9's faithful God; 7:19's great trials your eyes saw)
import cold_run_ordinances as OR               # THE EDGE: second_tablets -> ordinances CALL, reference (Exodus 23:8's bribe never written; 22:21's widow and orphan; 22:20's and 23:9's 'you were strangers')
import cold_run_holiness_b as HB               # THE EDGE: second_tablets -> holiness_b CALL, reference (Leviticus 19:34's love of the convert — the cell whose effect is written on the tape for the first time here)

'''
# ---- the generic helper block from the chapter-9 runner, by content markers ----
a = NR.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = NR.index('def LEN(b, c, v): return len(words(b, c, v))'); b = NR.index('\n', b) + 1
helpers = NR[a:b]
assert helpers.count("def W9(v): return words('Deut', 9, v)") == 1
helpers = helpers.replace("def W9(v): return words('Deut', 9, v)", "def W10(v): return words('Deut', 10, v)")
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D10 = lambda v: ('Deut', 10, v)

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch10_ink.py — COPIED from the reading's instrument by content markers, the sequence module's names made the exec'd parser's) ----
SPAN = [(10, v) for v in range(1, 23)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 10, v)) for v in range(1, 23)}
ORDS = {v: ink_ordinals(verse_words('Deut', 10, v)) for v in range(1, 23)}
PARSED = {(10, v): n for v, n in NUMS.items() if n}
TOK = sum(len(W10(v)) for v in range(1, 23)); LET = sum(len(x) for v in range(1, 23) for x in W10(v))
assert TOK == 324 and LET == 1252, (TOK, LET)
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers ----
i = INKB.index("assert {v: n for v, n in NUMS.items() if n} == {1: [2], 3: [2, 2], 4: [10], 10: [40, 40], 22: [70]}")
j = INKB.index("assert P('ירדו', 'אבתיך', 'מצרימה') == ['Deut 10:22']"); j = INKB.index('\n', j) + 1
ink_block = INKB[i:j]
n_cs = ink_block.count('CS.'); assert n_cs >= 6, n_cs
ink_block = ink_block.replace('CS.ink_numbers', 'ink_numbers').replace('CS.verse_words', 'verse_words').replace('CS.ink_ordinals', 'ink_ordinals')
assert 'CS.' not in ink_block
vc = [l for l in ink_block.split('\n') if 'VC[c]' in l]; assert len(vc) == 1, vc
ink_block = ink_block.replace(vc[0] + '\n', '')   # the verse-count table VC is the reading's (the store); the runner reads the DB alone
assert 'VC[' not in ink_block and ink_block.count('\nassert ') >= 60, ink_block.count('\nassert ')
TAIL_B = '''
# ---- THE CLOCK'S OWN ARITHMETIC (a bare world on the exodus epoch; the tape's markers reproduce these days — asserted on the running world at DB4) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the clock — the third forty, the erection and Aaron\\'s death on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
SECOND_TABLETS = DAY(1, WE.CAL_PARAMS['second_tablets_given']['value']['month'], WE.CAL_PARAMS['second_tablets_given']['value']['day']); SECOND_ASCENT = SECOND_TABLETS - 40
ERECTED = DAY(2, 1, 1); AARON_DEATH = DAY(ink_ordinals(verse_words('Num', 33, 38))[0], ink_ordinals(verse_words('Num', 33, 38))[1], ink_numbers(verse_words('Num', 33, 38))[0]); HOR_ARRIVAL = DAY(40, 4, 1); COUNTER = DAY(40, 11, 1)
CLOCK = {'second_ascent': DATE(SECOND_ASCENT), 'second_tablets': DATE(SECOND_TABLETS), 'third_forty': SECOND_TABLETS - SECOND_ASCENT, 'erected': DATE(ERECTED), 'aaron_death': DATE(AARON_DEATH), 'hor_arrival': DATE(HOR_ARRIVAL), 'hor_to_death': AARON_DEATH - HOR_ARRIVAL, 'counter': DATE(COUNTER),
         'av_days': DAY(1, 6, 1) - DAY(1, 5, 1), 'from_29_av_to_10_tishri': SECOND_TABLETS - DAY(1, 5, 29), 'seder_olam_6_2': (1, 5, 29)}
assert CLOCK == {'second_ascent': (1, 5, 29), 'second_tablets': (1, 7, 10), 'third_forty': 40, 'erected': (2, 1, 1), 'aaron_death': (40, 5, 1), 'hor_arrival': (40, 4, 1), 'hor_to_death': 29, 'counter': (40, 11, 1), 'av_days': 30, 'from_29_av_to_10_tishri': 40, 'seder_olam_6_2': (1, 5, 29)}, CLOCK   # hor_to_death 29 READ from the fast checker's print (Tammuz twenty-nine days that year: the arrival at Hor (40, 4, 1) to the death (40, 5, 1))
# THE SECOND ASCENT'S DATE MATCHES THE SHELF — Seder Olam Rabbah 6:2 (read whole at the docket): down the 28th of Av and carved, UP THE 29TH OF AV, down the 10th of Tishri: the machine's
# (1, 5, 29) by subtraction from CAL_PARAMS second_tablets_given IS the shelf's own date — 7b's OPEN row on the clock CLOSED (the "first of Elul" was not this shelf's text); the second
# and the third forty each forty by the calendar (Av thirty days that year on the tape's calendar)

# ---- THE ONE DATABASE SCANNED (the SUPPLIED grades' ground and the holes' — no entry names the fragments, no entry buries Aaron, nothing written on the cleaving, the heart, the neck or the stranger's love) ----
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
FRAG_WORDS = r"\\b(fragments?|broken tablets|shards|fragments_in_the_ark)\\b"; BURIED_WORDS = r"\\b(buried|burial|aaron_buried)\\b"; LAW_WORDS = r"\\b(cleav\\w*|stiff\\w*|neck|nape|bribe\\w*|heart_circumcision\\w*|foreskin|fear_of_heaven\\w*)\\b"
_frag = ledger_scan('the_ark', FRAG_WORDS); FRAG_SCAN = None if _frag is None else [e for e in _frag if e != 'fragments_in_the_ark']   # this sitting's own write excluded once the fold carries it
_bur = ledger_scan('aaron', BURIED_WORDS); AARON_BURIED_SCAN = None if _bur is None else [e for e in _bur if e != 'buried']
_law = ledger_scan('israel_people', LAW_WORDS); LAW_SCAN = None if _law is None else [e for e in _law if e not in ('cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', 'love_owed')]   # this sitting's own five excluded once the fold carries them (love_owed's value names the bribe declaration — read at the tape's second attempt)
_lo = effect_scan('love_owed'); LOVE_OWED_SCAN = None if _lo is None else [e for e in _lo if e != 'israel_people']
_bb = effect_scan('bribe_barred'); BRIBE_SCAN = _bb
_bu = effect_scan('buried'); BURIED_ENTITIES = None if _bu is None else [e for e in _bu if e != 'aaron']
assert FRAG_SCAN in ([], None), FRAG_SCAN   # the hole's ground — no entry on the ark named the fragments before this write (7b's owed item (i))
assert AARON_BURIED_SCAN in ([], None), AARON_BURIED_SCAN   # no entry buried Aaron before this write (Numbers 20:28 the death, 33:39 the age, 20:29 the mourning)
assert LAW_SCAN in ([], None), LAW_SCAN   # nothing written on Israel for the cleaving, the heart, the neck, the bribe or the fear of Heaven before this sitting (the code's holes)
assert LOVE_OWED_SCAN in ([], None), LOVE_OWED_SCAN   # love_owed on NO entity of the tape before this sitting (holiness_b's effect on the exam's wronger alone, never on the world)
assert BRIBE_SCAN in ([], None), BRIBE_SCAN   # bribe_barred NEVER written (the ordinances' block on the judge at Exod 23:8 — 10:17 a declaration, no write)
assert BURIED_ENTITIES is None or len(BURIED_ENTITIES) == 8, BURIED_ENTITIES   # the world's eight buried before Aaron — Sarah, Abraham, Deborah, Rachel, Isaac, Jacob, the lusters, Miriam (the design's DB6)
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B
open(f'{SP}/ch10_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch10_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d)' % (len(src), len(helpers), len(ink_block), ink_block.count('\nassert ')))
