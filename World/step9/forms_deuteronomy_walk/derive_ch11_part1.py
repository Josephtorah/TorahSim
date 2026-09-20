#!/usr/bin/env python3
# THE DEUTERONOMY WALK 9b: cold_run_blessing_and_curse.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-10 runner by
# content markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W10 made W11); THE INK BLOCK COPIED from the reading's own
# instrument ch11_ink.py by content markers (the parser measured on every verse — NO NUMBER VERSE — through the blessing-and-curse census: every assert PROVEN at
# sitting 9; the sequence module's names made the exec'd parser's; the store-bound asserts (the snapshot's glosses) left to the reading); the counter's day, the two
# parameters and the one-database scans typed. Asserted substitutions throughout. derive_ch10_part1.py's form.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
ST = open(f'{ROOT}/World/step9/cold_run_second_tablets.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_ink.py', encoding='utf-8').read()
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 11:1-32 — THE DISCIPLINE RETOLD, THE LAND WATERED BY HEAVEN, THE SECOND PARAGRAPH, THE BORDERS AND THE DREAD, THE BLESSING AND THE CURSE —
# THE READBACK'S FORMS ON FILE, NO NEW FORM (THE DEUTERONOMY WALK sitting 9b, 2026-09-20; World/step9/DEUTERONOMY_WALK.md "Sitting 9b"; the state doc's #199).
# The chapter retells the discipline (11:1-7 — the exodus, the sea, Dathan and Abiram, the wilderness: EVERY ACT WITH A LINE ON THE TAPE, measured — no retrograde
# marker; the tape already leaves Korah unnamed at the swallowing as the chapter does; 11:5 the STATE row, SUPPLIED with no write — chapter 8's fifth form),
# praises the land (11:8-12 by CALL — the land watered by heaven, first: Ta'anit 10a:2-3), gives THE SECOND PARAGRAPH (11:13-21 — THE RAIN CONDITIONAL WITH NO
# CELL ANYWHERE IN THE MACHINE, compiled at the chapter's own day (40, 11, 1): the line second_paragraph_declared writing rain_in_its_season and
# heavens_shut_for_turning — conditional HEAVEN entries, Leviticus 26:4 and 26:19-20 by CALL — and yoke_of_the_commandments_accepted, THE ANSWER SHEET'S OWN NAME
# (Mishnah Berakhot 2:2; Berakhot 14b:11); the duties 6:6-9's said again by CALL, no second shema line; 11:16's warning by CALL, no second block), restates the
# borders and the dread (11:22-25 by CALL; 11:25's 'as He spoke to you' A RUN_CITATION POINTER to Exodus 23:27 — the fourth receipt shape, two teachers: the
# Sifrei 52:4, Tosefta Sotah 8:6), and sets THE BLESSING AND THE CURSE (11:26-32 — THE CHAPTER'S LAW compiled at its own day: the line blessing_and_curse_set
# writing blessing_and_curse_set — a STATUS — and gerizim_ebal_ceremony_owed — a DEBIT on Israel toward Heaven OPEN to Joshua 8:30-35, the run outside the
# Torah's tape; the ceremony's form, tongue, day and forty-eight covenants from the shelf; its place a three-arm PARAMETER). TWO own-day lines, NO marker;
# FIVE writes; the open debits on Israel 9 -> 10. The daemon law_blessing_and_curse given_at Deut 11:1, installed_by boot (the Deuteronomy daemons' form).
# Six cells; every token probed (zero-report law); effects on every cell (the effects law); the DATA rows the docket added (the shutting's value and threshold,
# 'in its season' the free variable after the decree, the cattle before the man, the pointer's second teacher, the place's three arms, the ceremony's day and
# tongue and count, the dispossession the crossing's condition, the Samaritan variant, the rain's source a dispute, the causes a parameter, the empty export
# row). Reading ledger: logic/oral_triage/deu_11_ekev_reeh_2026-09-20.md (210 sources, 6 claims); the exam's docket: deu_11_ekev_reeh_exam_2026-09-20.md
# (1,048 rows — 477 READ WHOLE here, 571 carried with their ledgers' own verdicts: LAW 258 / DERIVATION 150 / DISPUTE 113 / CONTEXT 423 / OUTSIDE 104).

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
import cold_run_hear_o_israel as HI            # THE EDGE: blessing_and_curse -> hear_o_israel CALL, reference (11:18-20's duties 6:6-9's said again; 11:9's milk and honey; 11:21's sons; 11:13's heart and soul; 11:1's love)
import cold_run_good_land as GL                # THE EDGE: blessing_and_curse -> good_land CALL, reference (11:8-9 = 8:1's frame; 11:2's discipline; 11:5's wilderness the state row; 11:10-12's land; 11:15's eat and be satisfied; 11:16's serve and bow; 11:28's not hearken)
import cold_run_seven_nations as SN            # THE EDGE: blessing_and_curse -> seven_nations CALL, reference (11:23's nations; 11:14's grain, wine and oil; 11:27's blessing; 11:25's no man shall stand; 11:7's trials)
import cold_run_not_righteousness as NR        # THE EDGE: blessing_and_curse -> not_righteousness CALL, reference (11:23's 'greater and mightier than you' 9:1's; 11:28's 'turn aside from the way' the calf's; 11:5's wilderness 9:7's)
import cold_run_obey_horeb as OH               # THE EDGE: blessing_and_curse -> obey_horeb CALL, reference (11:23's dispossession 4:38's; 11:32's statutes and judgments 4:8's; 4:4's cleaving the state; 11:16's 'take heed' 4:23's form)
import cold_run_second_tablets as ST           # THE EDGE: blessing_and_curse -> second_tablets CALL, reference (11:1's five duties 10:12's; 11:22's cleaving 10:20's; 11:25's receipt shape beside 10:9's)
import cold_run_covenant_at_horeb as CH        # THE EDGE: blessing_and_curse -> covenant_at_horeb CALL, reference (11:16's 'serve other gods and bow' the second word's pair — the block other_gods_barred standing, no second block)
import cold_run_tochacha as TC                 # THE EDGE: blessing_and_curse -> tochacha CALL, reference (11:14's rains in their season Leviticus 26:4's; 11:17's shut heavens 26:19-20's iron heavens — no line on the tape, the cells)
import cold_run_ordinances as OR               # THE EDGE: blessing_and_curse -> ordinances CALL, reference (11:25's terror Exodus 23:27's — the pointer's target; 11:24's extents 23:31's; the hornet, little by little)
import cold_run_borders as BR                  # THE EDGE: blessing_and_curse -> borders CALL, reference (11:24's four extents against Numbers 34's spec; the land-bound rule; Joshua's receipts)
import cold_run_korach as KR                   # THE EDGE: blessing_and_curse -> korach CALL, reference (11:6's Dathan and Abiram swallowed — Korah unnamed on the tape as in the chapter; the death mode the open row; Korah's wealth)
import cold_run_second_census as SC            # THE EDGE: blessing_and_curse -> second_census CALL, reference (11:6's 'this is Dathan and Abiram' 26:9-11's; 11:2's children who have not known the census's generation)
import cold_run_exodus_story as ES             # THE EDGE: blessing_and_curse -> exodus_story CALL, reference (11:3's signs and deeds the ten plagues; 11:4's sea — saved at the sea, the song, the ten miracles)
import cold_run_primeval as PR                 # THE EDGE: blessing_and_curse -> primeval CALL, reference (11:6's 'every living thing' the flood's word; 11:10's 'like the land of Egypt' Lot's clause; 11:30's terebinths of Moreh Abram's)

'''
# ---- the generic helper block from the chapter-10 runner, by content markers ----
a = ST.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = ST.index('def LEN(b, c, v): return len(words(b, c, v))'); b = ST.index('\n', b) + 1
helpers = ST[a:b]
assert helpers.count("def W10(v): return words('Deut', 10, v)") == 1
helpers = helpers.replace("def W10(v): return words('Deut', 10, v)", "def W11(v): return words('Deut', 11, v)")
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D11 = lambda v: ('Deut', 11, v)
NEG = ('לא', 'ולא')
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch11_ink.py — COPIED from the reading's instrument by content markers, the sequence module's names made the exec'd parser's; the store-bound asserts left to the reading) ----
SPAN = [(11, v) for v in range(1, 33)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 11, v)) for v in range(1, 33)}
ORDS = {v: ink_ordinals(verse_words('Deut', 11, v)) for v in range(1, 33)}
PARSED = {(11, v): n for v, n in NUMS.items() if n}
assert PARSED == {} and all(o == [] for o in ORDS.values()), (PARSED, ORDS)   # NO NUMBER VERSE IN THE CHAPTER (the book's first such chapter since the walk began — measured at the reading)
TOK = sum(len(W11(v)) for v in range(1, 33)); LET = sum(len(x) for v in range(1, 33) for x in W11(v))
assert TOK == 508 and LET == 1992, (TOK, LET)
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers ----
i = INKB.index("# ---- THE INK, computed from the Tanakh DB and the snapshot store ----")
j = INKB.index("assert P('ושמרתם', 'לעשות', 'את', 'כל', 'החקים', 'ואת', 'המשפטים')"); j = INKB.index('\n', j) + 1
ink_block = INKB[i:j]
lines = ink_block.split('\n')
drop = [l for l in lines if 'STORE_MISMATCH' in l or 'byw[' in l or "if '?' in g" in l or l.startswith('with contextlib.redirect_stdout(io.StringIO()):') or l.strip() == 'import cold_run_sequence as CS' or l.startswith('# ---- THE INK, computed from the Tanakh DB and the snapshot store') or l.startswith('# THE STORE = THE DB at EVERY verse')]
assert len(drop) == 7, (len(drop), [d[:60] for d in drop])
lines = [l for l in lines if l not in drop]
ink_block = '\n'.join(lines)
n_cs = ink_block.count('CS.'); assert n_cs >= 6, n_cs
ink_block = ink_block.replace('CS.ink_numbers', 'ink_numbers').replace('CS.verse_words', 'verse_words').replace('CS.ink_ordinals', 'ink_ordinals')
assert 'CS.' not in ink_block and 'SG[' not in ink_block and 'byw' not in ink_block and 'VC[' not in ink_block and 'STORE_' not in ink_block
assert ink_block.count('\nassert ') >= 60, ink_block.count('\nassert ')
TAIL_B = '''
# ---- THE COUNTER'S DAY AND THE TWO PARAMETERS (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 11 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
RAIN_DATES = WE.CAL_PARAMS['rain_dates']['value']; GERIZIM_EBAL_PLACE = WE.CAL_PARAMS['gerizim_ebal_place']['value']   # THE TWO PARAMETERS read (exercised_by blessing_and_curse) — never a constant in the code
CLOCK = {'counter': DATE(COUNTER), 'rain_dates_keys': sorted(RAIN_DATES), 'place_arms': sorted(GERIZIM_EBAL_PLACE), 'no_marker': True}
assert CLOCK == {'counter': (40, 11, 1), 'rain_dates_keys': ['early_rain', 'fasts_community', 'fasts_individuals', 'late_rain', 'mention_from', 'mention_to', 'request_from_diaspora', 'request_from_land'], 'place_arms': ['r_elazar', 'r_eliezer_ben_yaakov', 'r_yehuda'], 'no_marker': True}, CLOCK
assert RAIN_DATES['late_rain'].startswith('Nisan') and RAIN_DATES['early_rain'].startswith('Marcheshvan') and RAIN_DATES['request_from_land'].startswith('the seventh of Marcheshvan') and GERIZIM_EBAL_PLACE['r_yehuda'].startswith('Shechem'), (RAIN_DATES, GERIZIM_EBAL_PLACE)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the rain, the heavens shut, the yoke, the blessing-and-curse pair or the ceremony on Israel before this sitting) ----
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
OWN5 = ('rain_in_its_season', 'heavens_shut_for_turning', 'yoke_of_the_commandments_accepted', 'blessing_and_curse_set', 'gerizim_ebal_ceremony_owed')
RAIN_WORDS = r"\\b(rain\\w*|heavens? shut|shut up the heavens|yoke of the commandments|gerizim|ebal|blessing and (?:the )?curse|rain_in_its_season|heavens_shut_for_turning|yoke_of_the_commandments_accepted|blessing_and_curse_set|gerizim_ebal_ceremony_owed)\\b"
_rs = ledger_scan('israel_people', RAIN_WORDS); RAIN_SCAN = None if _rs is None else [e for e in _rs if e not in OWN5]   # this sitting's own five excluded once the fold carries them
_cs = effect_scan('gerizim_ebal_ceremony_owed'); CEREMONY_SCAN = None if _cs is None else [e for e in _cs if e != 'israel_people']
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
RAIN_VOCAB = sorted(k for k in _FXV if 'rain' in k)
assert RAIN_SCAN in ([], None), RAIN_SCAN   # THE HOLE'S GROUND — nothing on Israel named the rain, the heavens shut, the yoke, the pair or the ceremony before this sitting (DC4)
assert CEREMONY_SCAN in ([], None), CEREMONY_SCAN   # the ceremony's debit on no other entity
assert 'rain_in_its_season' in RAIN_VOCAB and [k for k in RAIN_VOCAB if k.startswith('rain_')] == ['rain_in_its_season'], RAIN_VOCAB   # the vocabulary's rain effects — this sitting's the one naming the rain of the land (the others the registry's own, read at add_types_ch11.out)
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B
open(f'{SP}/ch11_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch11_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines' % (len(src), len(helpers), len(ink_block), ink_block.count('\nassert '), len(drop)))
