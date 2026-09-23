import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 12b's form ch14_callees.py; 10b's lesson 2: a regex's silence is not
# a cell's — every cell's asks read at its own source): every CALL the design names (twenty-one runners — nineteen REFERENCE, two TRANSFER: seducers' Belial row,
# metzora's ear), its signature, its asks-in-source and EVERY ask's result repr'd (cut) — the older runners' cells take q (or a case dict, or positional data), the
# Deuteronomy runners' take (case, data): the print settles each form; yovel's clock cells called on the design's values (the cycle's years, the Hebrew slave's sale,
# the valuation, the going out); the tape's lines the readback references read off the sequence file's TAPE block by their verses; the one database's ledgers for
# the kin BY SOURCE (the tape's own run 'cold_run_sequence/rest' and the others each ONE). RUN FROM THE REPO ROOT.
import sys, io, contextlib, subprocess, inspect, re, os
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_yovel as YO, cold_run_calendar as CA, cold_run_mishpatim as MP, cold_run_mishpatim_2 as M2, cold_run_mishpatim_3 as M3, cold_run_ordinances as OR
    import cold_run_erection as ER, cold_run_korach as KO, cold_run_temurah as TM, cold_run_priesthood as PR, cold_run_place_name as PN, cold_run_sanctions as SA
    import cold_run_holiness as HO, cold_run_food_tithe as FT, cold_run_covenant_at_horeb as CH, cold_run_blessing_and_curse as BC, cold_run_exodus_story as ES
    import cold_run_primeval as PV, cold_run_good_land as GL, cold_run_seducers as SE, cold_run_metzora as MZ
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f, cut=300):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:200])
    print('%-72s %s' % (label, repr(r)[:cut]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def asks_in(src): return sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \(|\bq == |\bq in \(|case\['ask'\] == |\bcase == |\bthing == |\bmanner == |\bstate == |\bborrower == |\bwhere == )'([a-z_0-9]+)'", src, re.M)))
def cell(M, name, asks=None, head_n=240, cut=300):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); found = asks_in(src)
    print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), found, src[:head_n].replace('\n', '\n    ')))
    for a in (asks if asks is not None else found):
        s = sig(f)
        if len(s) >= 2 and s[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2], cut)
        elif len(s) == 1 and s[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}), cut)
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a), cut)
for M, names in ((YO, ['cycle', 'jubilee', 'sabbatical', 'interest', 'interest_scope', 'hebrew_slave', 'gentile_slave', 'going_out', 'valuation', 'support_duty', 'sale_manner', 'arrival_unredeemed']), (CA, ['sabbatical']),
                 (M3, ['maidservant', 'slave_struck']), (OR, ['loan', 'firstling', 'gifts', 'torn', 'stranger']), (ER, ['repeats']), (KO, ['the_gifts', 'the_tithe']), (TM, ['consecrate', 'tithe', 'redeem', 'firstborn_trick', 'devote']),
                 (PR, ['acceptable', 'blemish', 'family', 'holy_food']), (PN, ['the_place_chosen', 'the_profane_slaughter_the_blood_and_the_gates', 'the_border_enlarged_and_the_altar']), (SA, ['blood', 'covering', 'frame', 'carcass']),
                 (HO, ['gifts', 'wage', 'warning']), (FT, ['the_third_year', 'the_second_tithe', 'the_far_place_the_money_the_rejoicing_and_the_levite']), (CH, ['the_first_tablet', 'the_second_word', 'the_assembly_called']), (BC, ['the_second_paragraph', 'the_blessing_and_the_curse', 'the_land_watered_by_heaven']),
                 (ES, ['oppression', 'bricks', 'night', 'birth', 'plagues']), (PV, ['cain', 'lines', 'war']), (GL, ['the_testimony', 'the_frame', 'the_good_land', 'take_heed_lest_you_forget']), (SE, ['the_inciter', 'the_header', 'the_prophet_and_the_test']), (MZ, ['eighth', 'poor', 'shave'])):
    for n in names: cell(M, n)
print('==== YO — the clock cells on the design\'s values (the cycle\'s years; the Hebrew slave sold to an Israelite for 60 with 20 years to the jubilee, 6 elapsed; the valuation of a male 30; the going out; the interest\'s scope):')
for lab, f in (('YO.cycle(1)', lambda: YO.cycle(1)), ('YO.cycle(6)', lambda: YO.cycle(6)), ('YO.cycle(7)', lambda: YO.cycle(7)), ('YO.cycle(14)', lambda: YO.cycle(14)), ('YO.cycle(49)', lambda: YO.cycle(49)), ('YO.cycle(50)', lambda: YO.cycle(50)), ('YO.jubilee()', lambda: YO.jubilee()), ('YO.sabbatical()', lambda: YO.sabbatical()), ('YO.interest()', lambda: YO.interest()),
               ('YO.hebrew_slave("israelite", 60, 20, 6)', lambda: YO.hebrew_slave('israelite', 60, 20, 6)), ('YO.hebrew_slave("gentile", 60, 20, 6)', lambda: YO.hebrew_slave('gentile', 60, 20, 6)), ('YO.going_out()', lambda: YO.going_out()), ('YO.going_out(redeemed_by="brother")', lambda: YO.going_out(redeemed_by='brother')), ('YO.valuation("male", 30)', lambda: YO.valuation('male', 30)), ('YO.valuation("female", 30)', lambda: YO.valuation('female', 30)),
               ('YO.interest_scope("brother")', lambda: YO.interest_scope('brother')), ('YO.interest_scope("foreigner")', lambda: YO.interest_scope('foreigner')), ('YO.support_duty("grew_poor")', lambda: YO.support_duty('grew_poor')), ('YO.sale_manner("slave_sale")', lambda: YO.sale_manner('slave_sale')), ('YO.gentile_slave()', lambda: YO.gentile_slave()), ('YO.arrival_unredeemed()', lambda: YO.arrival_unredeemed())):
    show('  ' + lab, f, 420)
print('==== the runners\' cells and DATA keys:')
for M in (YO, CA, MP, M2, M3, OR, ER, KO, TM, PR, PN, SA, HO, FT, CH, BC, ES, PV, GL, SE, MZ):
    show('%s cells' % M.__name__[9:], lambda M=M: cells_of(M), 1200)
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:80], 1600)
print('==== MP (mishpatim) — the module\'s names holding the Hebrew slave (F1) and the term clock; M2\'s; the daemons\' branches:')
for M in (MP, M2):
    for n in dir(M):
        if n.startswith('_'): continue
        v = getattr(M, n)
        if callable(v) and getattr(v, '__module__', '') == M.__name__:
            src = inspect.getsource(v)
            if re.search(r'hebrew|slave|goes_free|six|jubilee|21:2|21:5|21:6|pierc|redeemed_by_deduction|released|21:26|maimed', src, re.I): cell(M, n, head_n=900, cut=300)
        elif isinstance(v, (dict, list, tuple)) and re.search(r'hebrew|slave|six|jubilee|pierc|21:2|21:6', repr(v)[:6000], re.I):
            print('==== %s.%s (%s): %s' % (M.__name__, n, type(v).__name__, repr(v)[:1400]))
print('==== SE (seducers) — the DATA rows naming Belial, the base thought or 15:9; MZ (metzora) — the ear:')
for k, v in getattr(SE, 'DATA', {}).items():
    if re.search(r'belial|base|15:9|turns his eyes|poor', repr(v), re.I): print('  SE.DATA[%r] = %s' % (k, repr(v)[:700]))
for n in ('eighth',):
    src = inspect.getsource(getattr(MZ, n)); print('  MZ.%s asks: %s; ear lines: %s' % (n, asks_in(src), [l.strip()[:160] for l in src.split('\n') if re.search(r'ear|thumb|toe|right', l, re.I)][:8]))
print('==== ES (exodus_story) — the cells/rows naming the release, "not empty" (3:21), the spoil:')
for n in cells_of(ES):
    src = inspect.getsource(getattr(ES, n))
    if re.search(r'3:21|empty|release|spoil|12:35|12:36|redeem', src, re.I): cell(ES, n, head_n=200)
print('==== PV (primeval) — Abel\'s firstlings (4:4); CH (covenant_at_horeb) — 5:15; BC — 11:13; GL — the receipt seats:')
for n in cells_of(PV):
    src = inspect.getsource(getattr(PV, n))
    if re.search(r'4:4|firstling|Abel|firstborn', src, re.I): cell(PV, n, head_n=200)
for n in cells_of(CH):
    src = inspect.getsource(getattr(CH, n))
    if re.search(r'5:15|slave in|remember that', src, re.I): cell(CH, n, head_n=200)
show('GL.receipt_seats(15)', lambda: GL.receipt_seats(15), 900); show('GL.receipt_seats(12)', lambda: GL.receipt_seats(12), 600)
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
import ast
PFX = ('Exod 21:', 'Exod 23:10', 'Exod 23:11', 'Lev 25:', 'Exod 13:', 'Exod 22:2', 'Exod 22:3', 'Exod 34:19', 'Num 18:1', 'Lev 27:2', 'Lev 22:', 'Lev 21:1', 'Deut 5:', 'Deut 11:13', 'Deut 12:1', 'Deut 14:28', 'Gen 4:', 'Gen 15:13', 'Exod 5:1', 'Exod 12:31', 'Exod 2:23', 'Exod 3:21', 'Exod 19:5', 'Deut 7:12', 'Lev 19:9', 'Lev 19:13', 'Lev 14:14', 'Lev 14:2', 'Deut 13:1', 'Deut 8:1', 'Deut 10:1')
print('==== THE TAPE\'S LINES AT THE KIN VERSES (kind | subject | first verse | the source head | the other fields):')
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    cs = str(e.get('case_source', ''))
    if cs.startswith(PFX):
        print('  %-34s %-18s %-14s %-70s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:70], {k: (v if len(repr(v)) < 60 else repr(v)[:60]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== the tape\'s last Deuteronomy 14 lines (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 14:' in l[:160] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-2:]: print('  ' + l.strip()[:170])
print('==== the kin\'s ledgers on the one database BY SOURCE (the tape\'s own run and the others — the counts the checkpoints and the probes read):')
import sqlite3
_WDB = os.path.join(ROOT, 'World', 'journal', 'data', 'world.sqlite')
if os.path.exists(_WDB):
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    for eff in ('blessings_for_hearing', 'cry_heard', 'bears_sin', 'holy_things_in_the_gates_barred', 'consecrated_firstborn', 'jubilee_release', 'pledge_returned_by_sunset', 'work_of_the_hand_blessed', 'interest_barred', 'land_release', 'sabbath_debt', 'goes_out_in_the_jubilee', 'wage_due_by_morning', 'released', 'goes_free', 'love_owed', 'treasured_people', 'profane_slaughter_permitted', 'pity_barred', 'debt_release_owed', 'exaction_barred', 'hand_opening_commanded', 'hand_shutting_barred', 'base_thought_barred', 'furnishing_commanded', 'empty_sending_barred', 'severance_gift_owed', 'serves_for_ever', 'firstling_sanctification_commanded', 'firstling_work_and_shearing_barred'):
        print('  %-36s %s' % (eff, [(e, n, str(v)[:22]) for e, n, v in c_.execute("SELECT entity, count(*), min(verse) FROM run_ledger WHERE effect=? AND source='cold_run_sequence/rest' GROUP BY entity", (eff,)).fetchall()[:8]]))
    print('  the open debits on israel_people (the tape\'s run)', c_.execute("SELECT count(*) FROM run_ledger WHERE entity='israel_people' AND ledger_op='debit' AND open=1 AND source='cold_run_sequence/rest'").fetchall(), '| the blocks on israel_people', c_.execute("SELECT count(*) FROM run_ledger WHERE entity='israel_people' AND ledger_op='block' AND source='cold_run_sequence/rest'").fetchall())
    print('  the sources', c_.execute("SELECT source, count(*) FROM run_ledger GROUP BY source").fetchall())
print('==== THE CALLEES PRINTED')
