#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b: cold_run_release_firstborn.py PART 1 derived — the head typed here; the generic helper block COPIED from the chapter-14 runner by content
# markers (HERE = … through def LEN — the parser exec, the DB, the phrase/lemma/diff helpers; W14 made W15); THE INK BLOCK COPIED from the reading's own instrument
# ch15_ink.py by content markers — THREE blocks (the kin by computation, the ink facts censused over the DB with the chapter's counts, the register computed on the
# morphology; the parser's facts typed in the tail from the ink's own asserts — the ink script reads them through the sequence module, a runner cannot import it),
# the store-, shelf- and Onkelos-bound lines DROPPED by name (10b's lesson 6 — the patterns listed; the count read from the print); the counter's day, the TWO clock
# parameters, the one-database scans, the DB's own seats for the DATA rows, and THE CALLEES' FACTS (typed in ch15_callees_facts.py from ch15_callees.out — read
# before any assert was typed). Asserted substitutions throughout. derive_ch14_part1.py's form. RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FT = open(f'{ROOT}/World/step9/cold_run_food_tithe.py', encoding='utf-8').read()
INKB = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch15_ink.py', encoding='utf-8').read()
FACTS = open(f'{SP}/ch15_callees_facts.py', encoding='utf-8').read()
assert FACTS.startswith('\n# ---- THE CALLEES\' FACTS'), 'the callees\' facts typed from the print (ch15_callees_facts.py)'
HEAD = '''#!/usr/bin/env python3
# DEUTERONOMY 15:1-23 — THE RELEASE (the seventh year's end, one calendar for the whole world; the exaction barred; Hillel's prozbul from the answer sheet), THE NEEDY
# AND THE BLESSING (the two verses a state variable; the receipt's referent ahead), THE HAND OPENED (the ranks, the measure of need, the base thought), THE HEBREW
# SLAVE (the three cases, the term by call to Exodus 21's clock, the furnishing and the severance gift priced by call), THE AWL AND THE DOUBLE HIRE (the ear by the
# leper's, 'for ever' the master's lifetime with the jubilee's override on file), THE FIRSTLING (sanctified for its value against 27:26, its year by the clock) and
# THE BLEMISH AND THE BLOOD (the list by call to the priests' table, the blood by call to chapter 12's cells); THE READBACK'S FORMS ON FILE, NO NEW FORM (THE
# DEUTERONOMY WALK sitting 13b, 2026-09-23; World/step9/DEUTERONOMY_WALK.md "Sitting 13b"; the state doc's #207). FOUR own-day lines at the counter's day (40, 11, 1),
# NO marker: release_law_declared (15:1-6 — debt_release_owed a STATUS, exaction_barred a BLOCK, blessings_for_hearing REUSED), hand_opening_commanded (15:7-11 —
# hand_opening_commanded a STATUS, hand_shutting_barred and base_thought_barred BLOCKS, work_of_the_hand_blessed a HEAVEN entry, cry_heard and bears_sin REUSED),
# hebrew_slave_law_declared (15:12-18 — furnishing_commanded a STATUS, empty_sending_barred a BLOCK, work_of_the_hand_blessed's second seat), firstling_law_declared
# (15:19-23 — firstling_sanctification_commanded a STATUS, firstling_work_and_shearing_barred a BLOCK, holy_things_in_the_gates_barred REUSED); the case's writes
# severance_gift_owed (a DEBIT) and serves_for_ever (a STATUS) at the runner's own scene. THE KIN'S CELLS BY CALL (twenty-one runners — nineteen REFERENCE, two
# TRANSFER labeled with their teachers); THE TAPE'S LINES BY KIND (the hearing blessed, the second paragraph, the cry, the third year's tithe, the wealth promised,
# the sojourn decreed, Pharaoh's sending out, Abel's firstlings, the profane slaughter). Seven cells and the table; every token probed (zero-report law); effects
# on every cell (the effects law); the DATA rows the docket added; twenty-seven parameters (two clock data in the registry, twenty-five here). The daemon
# law_release_firstborn given_at Deut 15:1, installed_by boot (the Deuteronomy daemons' form). Reading ledger: logic/oral_triage/deu_15_reeh_2026-09-22.md; the
# exam's docket: deu_15_reeh_exam_2026-09-23.md (974 rows — 814 READ WHOLE in three runs, 160 carried with their ledgers' own verdicts: LAW 192 / DERIVATION 244 /
# DISPUTE 99 / CONTEXT 235 / OUTSIDE 204).

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
import cold_run_yovel as YO                    # THE EDGE: release_firstborn -> yovel CALL, reference (15:1's release on the sabbatical cycle — the seventh year's class; 15:12's sold brother; the jubilee's override on the pierced; the valuation's fifty; the interest's scope for the foreigner)
import cold_run_calendar as CA                 # THE EDGE: release_firstborn -> calendar CALL, reference (Exodus 23:10-11's release by name — the land's release turned to the money's)
import cold_run_mishpatim as MP                # THE EDGE: release_firstborn -> mishpatim CALL, reference (Exodus 21:2-6's term clock — the F1 table's three rows; the case kinds on file)
import cold_run_mishpatim_2 as M2              # THE EDGE: release_firstborn -> mishpatim_2 CALL, reference (Exodus 21:26-27's released — the slave sent free by kind)
import cold_run_mishpatim_3 as M3              # THE EDGE: release_firstborn -> mishpatim_3 CALL, reference (Exodus 21:7-11's maidservant — the exits' two tables; the DISAGREES row resolved)
import cold_run_ordinances as OR               # THE EDGE: release_firstborn -> ordinances CALL, reference (Exodus 22:24's loan — lending_is_obligation names 15:8; the priority ladder; the pledge's sunset; 22:29's firstling; the firstborn's five sela)
import cold_run_erection as ER                 # THE EDGE: release_firstborn -> erection CALL, reference (the severance gift already priced — Kiddushin 17a:7's five selas by 'empty'/'empty'; 34:19-20's firstborn)
import cold_run_korach as KO                   # THE EDGE: release_firstborn -> korach CALL, reference (Numbers 18:15-18's firstling — consecrated from the womb; the window; the blemished's keeping; the expert)
import cold_run_temurah as TM                  # THE EDGE: release_firstborn -> temurah CALL, reference (Leviticus 27:26's 'no man shall sanctify' — for value yes; the herd's tithe)
import cold_run_priesthood as PR               # THE EDGE: release_firstborn -> priesthood CALL, reference (Leviticus 22:20-25's list — one list serves the firstling; the priest's ear)
import cold_run_place_name as PN               # THE EDGE: release_firstborn -> place_name CALL, reference (12:15-16, 12:22-24's clauses verbatim at 15:22-23; the place formula; the gates' bar reused)
import cold_run_sanctions as SA                # THE EDGE: release_firstborn -> sanctions CALL, reference (Leviticus 17's blood ban and its covering; the witnesses' warning)
import cold_run_holiness as HO                 # THE EDGE: release_firstborn -> holiness CALL, reference (Leviticus 19:9-10's poor defined; 19:13's hireling's wage — the double hire)
import cold_run_food_tithe as FT               # THE EDGE: release_firstborn -> food_tithe CALL, reference (14:29's 'in all the work of your hand'; the count's year by the cycle; the year passed; the firstling from outside)
import cold_run_covenant_at_horeb as CH        # THE EDGE: release_firstborn -> covenant_at_horeb CALL, reference (5:15's 'remember that you were a slave' — 15:15 verbatim in kind)
import cold_run_blessing_and_curse as BC       # THE EDGE: release_firstborn -> blessing_and_curse CALL, reference (11:13's conditional in the same form as 15:5)
import cold_run_exodus_story as ES             # THE EDGE: release_firstborn -> exodus_story CALL, reference (the release demanded and closed — sent_out at 12:31; the spoil the slaves' wage)
import cold_run_primeval as PV                 # THE EDGE: release_firstborn -> primeval CALL, reference (Genesis 4:4's firstlings — Abel's, on the tape)
import cold_run_good_land as GL                # THE EDGE: release_firstborn -> good_land CALL, reference (the receipt seats' finder — none at chapter 15; 15:6's pointer row)
import cold_run_seducers as SE                 # THE EDGE: release_firstborn -> seducers CALL, TRANSFER taught by the Sifrei 117:3 (13:14's Belial for 15:9's base thought — 'base'/'base')
import cold_run_metzora as MZ                  # THE EDGE: release_firstborn -> metzora CALL, TRANSFER taught by the Sifrei 122:5-6 and Kiddushin 15a (the leper's right ear for the awl's — 'ear'/'ear')

'''
# ---- the generic helper block from the chapter-14 runner, by content markers ----
a = FT.index('HERE = _os.path.dirname(_os.path.abspath(__file__))'); b = FT.index('def LEN(b, c, v): return len(words(b, c, v))'); b = FT.index('\n', b) + 1
helpers = FT[a:b]
assert helpers.count("def W14(v): return words('Deut', 14, v)") == 1
helpers = helpers.replace("def W14(v): return words('Deut', 14, v)", "def W15(v): return words('Deut', 15, v)")
assert 'W14' not in helpers and '14' not in re.sub(r'0x0591|0x05C7|0x05AF|0x05B0|0x05BD', '', helpers), [l for l in helpers.split('\n') if '14' in l][:3]
TAIL_A = '''def verse_text(ch, vs, book='Deut'): return ' '.join(words(book, ch, vs))
D15 = lambda v: ('Deut', 15, v)
NEG = ('לא', 'ולא')   # (not; and not)
NAME = ('יהוה', 'ליהוה', 'ויהוה', 'ביהוה', 'מיהוה')   # (the LORD; to the LORD; and the LORD; in the LORD; from the LORD)
import difflib
def SH(a, b_): return sum(s for _, _, s in difflib.SequenceMatcher(a=words(*a), b=words(*b_)).get_matching_blocks())   # the reading's shared-run measure
NV = len({v for (b, c, v) in by if b == 'Deut' and c == 15}); assert NV == 23, NV   # twenty-three verses in both numberings

P_ = []   # the provenance trail of the case being run
def ink(ref, note):  P_.append(('INK',  'Deut %s — %s' % (ref, note) if not ref[:1].isupper() else '%s — %s' % (ref, note)))
def move(src, note): P_.append(('MOVE', '%s — %s' % (src, note)))
def dat(note):       P_.append(('DATA', note))
def hyp(note):       P_.append(('HYP',  note))     # THE LINK REVIEW LAW: a hypothesis — no teacher; counted apart, never as compiled
def out(verdict, effects):
    """verdict + registry-validated effects (the engine contract)"""
    FX.validate([e for e in effects if e != FX.NONE])
    return verdict, effects, list(P_)

# ---- THE INK, computed (the parser and the tokens; the reading's facts the expectations — every assert PROVEN at the reading, ch15_ink.py — COPIED from the reading's instrument by content markers in three blocks; the store-, shelf- and Onkelos-bound asserts left to the reading; the parser's facts typed from the ink's own asserts) ----
SPAN = [(15, v) for v in range(1, 24)]
def MARKS(c, v): return [t for t in verse_words('Deut', c, v) if t[-1] in '#~^%@|*']
def N(b, c, v): return ink_numbers(verse_words(b, c, v))
NUMS = {v: ink_numbers(verse_words('Deut', 15, v)) for v in range(1, 24)}
ORDS = {v: ink_ordinals(verse_words('Deut', 15, v)) for v in range(1, 24)}
PARSED = {(15, v): n for v, n in NUMS.items() if n}
KINNUM = {k: ink_numbers(verse_words(*k)) for k in [('Exod', 21, 2), ('Exod', 23, 10), ('Lev', 25, 3), ('Lev', 25, 8), ('Deut', 31, 10), ('Jer', 34, 14), ('Exod', 22, 29), ('Lev', 22, 27), ('Deut', 14, 28), ('Deut', 16, 9)]}
STARRED = sorted({(c, v, t) for (b, c, v) in by if b == 'Deut' for t in verse_words(b, c, v) if (t.startswith('שנים') or t.startswith('שנה') or t.startswith('ושנ')) and t[-1] in '#~^%@|*'})
TOKN = sum(len(W15(v)) for v in range(1, 24)); LETN = sum(len(x) for v in range(1, 24) for x in W15(v))
print('THE INK (printed before it is asserted): PARSED %s, ORDS %s, MARKS %s, TOKN %d, LETN %d, KINNUM %s, STARRED %s' % (PARSED, {v: o for v, o in ORDS.items() if o}, {v: MARKS(15, v) for v in range(1, 24) if MARKS(15, v)}, TOKN, LETN, KINNUM, STARRED))
assert PARSED == {(15, 1): [7], (15, 7): [1], (15, 12): [6], (15, 18): [6]} and {v: o for v, o in ORDS.items() if o} == {9: [7]} and {v: MARKS(15, v) for v in range(1, 24) if MARKS(15, v)} == {1: ['שנים*'], 12: ['שנים*'], 18: ['שנים*']} and TOKN == 354 and LETN == 1294, (PARSED, ORDS, TOKN, LETN)   # FOUR NUMBER VERSES (15:1 "seven years" [7], 15:12 and 15:18 "six years" [6], 15:7 "one of your brothers … one of your gates" [1]), ONE ORDINAL (15:9 "the seventh" [7]); THE STARRED "years" TOKENS at 15:1, 12, 18; 354 tokens, 1294 letters (measured at the reading)
assert KINNUM[('Exod', 21, 2)] == [6] and KINNUM[('Exod', 23, 10)] == [6] and KINNUM[('Lev', 25, 3)] == [6, 6] and KINNUM[('Lev', 25, 8)] == [7, 7, 7, 7, 49] and KINNUM[('Deut', 31, 10)] == [7] and KINNUM[('Jer', 34, 14)] == [7, 6] and KINNUM[('Exod', 22, 29)] == [7] and KINNUM[('Lev', 22, 27)] == [7] and KINNUM[('Deut', 14, 28)] == [3] and KINNUM[('Deut', 16, 9)] == [7, 7], KINNUM   # the reading's parser facts on the kin (Exodus 21:2's six, 23:10's six, the jubilee's sevens and forty-nine, Jeremiah's seven and six, the firstling's seven days)
assert [(c, v) for c, v, _ in STARRED] == [(9, 15), (10, 3), (14, 28), (15, 1), (15, 12), (15, 18), (31, 10)], STARRED   # the starred "years" tokens in the book — 15:1, 12, 18 the chapter's three (9:15 and 10:3 the carets, 14:28 and 31:10 the stars)
'''
# ---- THE INK BLOCK from the reading's instrument, by content markers — three blocks ----
def block(start, end):
    i = INKB.index(start); j = INKB.index(end, i); assert i < j, (start[:40], end[:40]); return INKB[i:j]
ink_block = block("# THE KIN FOUND BY COMPUTATION (the measure's A section", "# ---- THE SHELF BY POSITION") + block("# ---- THE TWO DIVISIONS AND THE VERSES ----", "# ---- THE PARSER (the C print)") + block("# ---- THE REGISTER (the D print)", "# ---- ONKELOS (the E print")
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
# ---- THE COUNTER'S DAY, THE TWO CLOCK DATA AND THE RELEASE ON THE BARE WORLD (a bare world on the exodus epoch; no clock walk this chapter — no marker, no stretch; the count era's year read through the clock's own methods — 'no count' before the entry; the firstling's year twelve months by the clock, never a constant) ----
with contextlib.redirect_stdout(io.StringIO()):
    _WC = WE.World(era='the counter\\'s day — chapter 15 on a bare world (the exodus epoch)', epoch='exodus')
_EX = _WC.clock.eras['exodus']
def DAY(y, m, d): return _WC.clock.day_in('exodus', y, m, d)
def DATE(day): return _EX.date(day)
COUNTER = DAY(40, 11, 1)
RELDATE = WE.CAL_PARAMS['the_release_date']['value']; FYEAR = WE.CAL_PARAMS['the_firstlings_year']['value']   # THE TWO CLOCK DATA read (exercised_by release_firstborn) — never a constant in the code; the twenty-five other parameters the DATA rows below
if 'count' in _WC.clock.eras:   # the count era is set by a marker at the entry (calendar_parameters.yaml's eras row 'count'); the bare world has none — the clock's own method prints and exits on a missing era (the fast checker's first pass), so the era is asked for first
    _cy = _WC.clock.year_in('count')
    REL_BARE = YO.cycle(_cy)['v'] if isinstance(_cy, int) and _cy >= 1 else 'no count'
else:
    REL_BARE = 'no count'
FY_DAYS = DAY(41, 11, 1) - COUNTER   # twelve months from the counter's day by the clock's own count (the firstling born on the counter's day, its year by the calendar)
CLOCK = {'counter': DATE(COUNTER), 'release_keys': sorted(RELDATE), 'firstlings_year_keys': sorted(FYEAR), 'the_release_on_the_bare_world': REL_BARE, 'the_firstlings_year_days': FY_DAYS, 'the_two_day_edge': True, 'no_marker': True}
print('THE CLOCK (printed before it is asserted):', CLOCK)
assert CLOCK['counter'] == (40, 11, 1) and CLOCK['release_keys'] == ['the_end', 'the_onset', 'the_territory', 'the_year'] and CLOCK['firstlings_year_keys'] == ['its_own_year', 'the_blemished', 'the_exiles_arm', 'the_tending_term', 'the_two_day_edge'] and CLOCK['the_release_on_the_bare_world'] == 'no count' and 350 <= CLOCK['the_firstlings_year_days'] <= 385, CLOCK   # the release's year read through the clock on the bare world before the entry: NO COUNT (as the removal's date at 14:28); the firstling's year a twelve-month span by the clock (the days read from the print, never typed)
assert RELDATE['the_end'].startswith("THE YEAR'S END") and RELDATE['the_year'].startswith('THE YEAR WHOSE CLASS IS sabbath_of_the_land') and RELDATE['the_onset'].startswith('AFTER THE CONQUEST') and RELDATE['the_territory'].startswith('IN THE LAND AND OUTSIDE IT') and FYEAR['its_own_year'].startswith("THE FIRSTLING'S OWN YEAR") and FYEAR['the_two_day_edge'].startswith("'YEAR BY YEAR'") and FYEAR['the_blemished'].startswith('THE BLEMISHED FIRSTLING THIRTY DAYS') and FYEAR['the_tending_term'].startswith('THIRTY AND FIFTY DAYS') and FYEAR['the_exiles_arm'].startswith('NO TEMPLE'), (RELDATE, FYEAR)

# ---- THE ONE DATABASE SCANNED (the holes' ground — nothing names the release of debts, the exaction, the hand opened or shut, the base thought, the work of the hand, the furnishing, the empty sending, the firstling's sanctification or its work and shearing on Israel before this sitting; the four reused effects' entities before) ----
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
OWN12 = ('debt_release_owed', 'exaction_barred', 'hand_opening_commanded', 'hand_shutting_barred', 'base_thought_barred', 'work_of_the_hand_blessed', 'furnishing_commanded', 'empty_sending_barred', 'severance_gift_owed', 'serves_for_ever', 'firstling_sanctification_commanded', 'firstling_work_and_shearing_barred')
HOLE_WORDS = r"\\b(debt_release\\w*|exaction\\w*|hand_opening\\w*|hand_shutting\\w*|base_thought\\w*|work_of_the_hand\\w*|furnishing\\w*|empty_sending\\w*|severance\\w*|serves_for\\w*|firstling_sanctif\\w*|firstling_work\\w*)\\b"
_hs = ledger_scan('israel_people', HOLE_WORDS); HOLE_SCAN = None if _hs is None else [e for e in _hs if e not in OWN12]   # this sitting's own names excluded once the fold carries them
_rs = [effect_scan(e) for e in ('blessings_for_hearing', 'cry_heard', 'bears_sin', 'holy_things_in_the_gates_barred')]; REUSE_SCAN = None if any(r is None for r in _rs) else _rs
del _hs, _rs   # 9b's lesson: the raw scans are the database's state at import — the derived lists are equal on the cached and the full load
_FXV = yaml.safe_load(open(_os.path.join(HERE, 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
assert HOLE_SCAN in ([], None), HOLE_SCAN   # THE HOLES' GROUND — nothing on Israel named the twelve before this sitting (DG4)
assert REUSE_SCAN in ([['israel_people'], ['israel_people'], [], ['israel_people']], None), REUSE_SCAN   # the four reused effects' entities before the second entries — bears_sin on none (the running world held no entry)
assert all(k in _FXV for k in OWN12) and _FXV['debt_release_owed']['ledger_op'] == 'status' and _FXV['exaction_barred']['ledger_op'] == 'block' and _FXV['work_of_the_hand_blessed']['ledger_op'] == 'heaven' and _FXV['severance_gift_owed']['ledger_op'] == 'debit' and all('THE DEUTERONOMY WALK 13b' in _FXV[e]['ink'] for e in ('blessings_for_hearing', 'cry_heard', 'bears_sin', 'holy_things_in_the_gates_barred')), 'the twelve on the registry; the four reuses amended (add_types_ch15.py)'
# THE DB'S OWN SEATS for the DATA rows (every one computed here — the ink block above proves them at the reading's grain)
INF_ABS = [(v, x) for v in range(1, 24) for x, m in by[('Deut', 15, v)] if m and re.match(r'^H(?:C/)?V.a$', m)]
SEVEN_YEARS = P('מקץ', 'שבע', 'שנים'); RELEASE_NOUN = [(s, x) for s, x, _ in LEMT('8059')]; NEEDY = [(s, x) for s, x, _ in LEMT('34', books=T)]; PLEDGE_VERB = [(s, x) for s, x, _ in LEMT('5670')]; REMEMBER_SLAVE = P('וזכרת', 'כי', 'עבד', 'היית', books=DT)
AWL = [(s, x) for s, x, _ in LEMT('4836')]; SIX_YEARS = P('שש', 'שנים', books=T); FOR_EVER = P('עבד', 'עולם'); YEAR_BY_YEAR = P('שנה', 'בשנה'); PLACE_FORMULA = P('במקום', 'אשר', 'יבחר', books=DT); UNCLEAN_CLEAN = P('הטמא', 'והטהור'); AS_WATER = P('על', 'הארץ', 'תשפכנו', 'כמים'); SPOKE_TO_YOU = P('כאשר', 'דבר', 'לך', books=DT); BASE = [(s, x) for s, x, _ in LEMT('1100', books=T)]; SIN_IN_YOU = P('והיה', 'בך', 'חטא')
TWIN = {'15:12 vs Exod 21:2': SH(D15(12), ('Exod', 21, 2)), '15:12 vs Jer 34:14': SH(D15(12), ('Jer', 34, 14)), '15:16 vs Exod 21:5': SH(D15(16), ('Exod', 21, 5)), '15:17 vs Exod 21:6': SH(D15(17), ('Exod', 21, 6)), '15:15 vs 5:15': SH(D15(15), ('Deut', 5, 15)), '15:15 vs 24:18': SH(D15(15), ('Deut', 24, 18)), '15:5 vs 28:1': SH(D15(5), ('Deut', 28, 1)), '15:6 vs 28:12': SH(D15(6), ('Deut', 28, 12)), '15:9 vs 24:15': SH(D15(9), ('Deut', 24, 15)), '15:10 vs 14:29': SH(D15(10), ('Deut', 14, 29)), '15:21 vs 17:1': SH(D15(21), ('Deut', 17, 1)), '15:22 vs 12:15': SH(D15(22), ('Deut', 12, 15)), '15:22 vs 12:22': SH(D15(22), ('Deut', 12, 22)), '15:23 vs 12:16': SH(D15(23), ('Deut', 12, 16)), '15:23 vs 12:24': SH(D15(23), ('Deut', 12, 24)), '15:4 vs 15:11': SH(D15(4), D15(11)), '15:1 vs 31:10': SH(D15(1), ('Deut', 31, 10)), '15:20 vs 12:18': SH(D15(20), ('Deut', 12, 18))}
print('THE DB\\'S OWN SEATS (printed before they are asserted): INF_ABS %s; seven years %s; the release noun %d; needy %d; the pledge verb %d; remember-a-slave %s; the awl %s; six years %s; for ever %s; year by year %d; the place formula %d; unclean-clean %s; as water %s; spoke-to-you %s; base %s; sin-in-you %s; TWIN %s' % (INF_ABS, SEVEN_YEARS, len(RELEASE_NOUN), len(NEEDY), len(PLEDGE_VERB), REMEMBER_SLAVE, AWL, SIX_YEARS, FOR_EVER, len(YEAR_BY_YEAR), len(PLACE_FORMULA), UNCLEAN_CLEAN, AS_WATER, SPOKE_TO_YOU, BASE, SIN_IN_YOU, TWIN))
assert [v for v, _ in INF_ABS] == [2, 4, 5, 8, 8, 10, 11, 14] and SEVEN_YEARS == ['Deut 15:1', 'Deut 31:10', 'Jer 34:14'] and len(RELEASE_NOUN) == 5 and len(NEEDY) == 9 and len(PLEDGE_VERB) == 6 and REMEMBER_SLAVE == ['Deut 15:15', 'Deut 16:12', 'Deut 24:18', 'Deut 24:22', 'Deut 5:15'] and AWL == [('Deut 15:17', 'המרצע'), ('Exod 21:6', 'במרצע')] and SIX_YEARS == ['Deut 15:12', 'Deut 15:18', 'Exod 21:2', 'Lev 25:3'] and FOR_EVER == ['Deut 15:17'] and len(YEAR_BY_YEAR) == 11 and len(PLACE_FORMULA) == 11 and UNCLEAN_CLEAN == ['Deut 12:15', 'Deut 12:22', 'Deut 15:22'] and AS_WATER == ['Deut 12:16', 'Deut 12:24', 'Deut 15:23'] and SPOKE_TO_YOU == ['Deut 12:20', 'Deut 15:6', 'Deut 26:18', 'Deut 29:12'] and BASE == [('Deut 13:14', 'בליעל'), ('Deut 15:9', 'בליעל')] and SIN_IN_YOU == ['Deut 15:9', 'Deut 23:22', 'Deut 24:15'], (INF_ABS, SEVEN_YEARS, len(RELEASE_NOUN), len(NEEDY), AWL, SIX_YEARS, FOR_EVER, len(YEAR_BY_YEAR), UNCLEAN_CLEAN, SPOKE_TO_YOU, BASE)
assert TWIN == {'15:12 vs Exod 21:2': 3, '15:12 vs Jer 34:14': 7, '15:16 vs Exod 21:5': 3, '15:17 vs Exod 21:6': 1, '15:15 vs 5:15': 11, '15:15 vs 24:18': 14, '15:5 vs 28:1': 14, '15:6 vs 28:12': 6, '15:9 vs 24:15': 7, '15:10 vs 14:29': 6, '15:21 vs 17:1': 6, '15:22 vs 12:15': 4, '15:22 vs 12:22': 4, '15:23 vs 12:16': 6, '15:23 vs 12:24': 5, '15:4 vs 15:11': 3, '15:1 vs 31:10': 3, '15:20 vs 12:18': 9}, TWIN   # the twin laws diffed on the DB (DG8) — the reading's frame (ch15_ink.py's THE FRAME assert) read again here
'''
src = HEAD + helpers + TAIL_A + ink_block + TAIL_B + FACTS
open(f'{SP}/ch15_part1.py', 'w', encoding='utf-8').write(src)
import py_compile; py_compile.compile(f'{SP}/ch15_part1.py', doraise=True)
print('part1 derived: %d bytes; helpers %d, ink block %d (asserts %d); dropped %d store-bound lines; the callees\' facts %d bytes' % (len(src), len(helpers), len(ink_block), n_as, len(drop), len(FACTS)))
