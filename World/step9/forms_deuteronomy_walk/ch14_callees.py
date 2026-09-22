import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 11b's form ch13_callees.py; 10b's lesson 2: a regex's silence is not
# a cell's — every cell's asks read at its own source): every CALL the design names (eighteen runners), its signature, its asks-in-source and EVERY ask's result repr'd
# (cut) — the older runners' cells take q (or a case dict, or a default parameter), the Deuteronomy runners' take (case, data): the print settles each form; the
# classifier called on the four exceptions, a pure beast and a fish in the sanctions engine's own dict form; the tape's lines the readback references, their kinds,
# subjects and first verses read off the sequence file's TAPE block; the one database's ledgers for the kin. RUN FROM THE REPO ROOT.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_shemini as SH, cold_run_sanctions as SA, cold_run_calendar as CA, cold_run_erection as ER, cold_run_ordinances as OR, cold_run_priesthood as PR
    import cold_run_holiness as HO, cold_run_holiness_b as HB, cold_run_moadim as MO, cold_run_temurah as TM, cold_run_korach as KO, cold_run_yovel as YO
    import cold_run_seven_nations as SN, cold_run_second_tablets as ST, cold_run_place_name as PN, cold_run_primeval as PV, cold_run_mamre as MM, cold_run_seducers as SE
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f, cut=260):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-64s %s' % (label, repr(r)[:cut]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def asks_in(src): return sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \(|\bq == |\bq in \(|case\['ask'\] == )'([a-z_0-9]+)'", src, re.M)))
def cell(M, name, asks=None, head_n=220, cut=260):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); found = asks_in(src)
    print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), found, src[:head_n].replace('\n', '\n    ')))
    for a in (asks if asks is not None else found):
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2], cut)
        elif len(sig(f)) == 1 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}), cut)
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a), cut)
for M, names in ((SH, ['classify', 'touch_effect']), (SA, ['carcass']), (CA, ['kid_in_milk', 'sabbatical']), (ER, ['repeats']), (OR, ['torn', 'firstling']), (PR, ['family', 'holy_food']),
                 (HO, ['gifts']), (HB, ['body']), (MO, ['harvest_reaped']), (TM, ['tithe', 'redeem']), (KO, ['the_tithe', 'the_gifts']), (YO, ['cycle', 'sabbatical', 'tithe_naming']),
                 (SN, ['the_holy_people']), (ST, ['the_levites_separated', 'the_god_of_gods_and_the_stranger']), (PN, ['the_place_chosen', 'the_profane_slaughter_the_blood_and_the_gates', 'the_border_enlarged_and_the_altar']),
                 (MM, ['bethel']), (SE, ['the_header'])):
    for n in names: cell(M, n)
print('==== SH.classify in the sanctions engine\'s dict form (the four exceptions, a pure beast, a fish, a bird by name):')
for d in ({'clazz': 'land', 'hoof': True, 'cud': True}, {'clazz': 'land', 'hoof': False, 'cud': True, 'name': 'camel'}, {'clazz': 'land', 'hoof': False, 'cud': True, 'name': 'hare'}, {'clazz': 'land', 'hoof': False, 'cud': True, 'name': 'coney'}, {'clazz': 'land', 'hoof': True, 'cud': False, 'name': 'swine'}, {'clazz': 'water', 'fins': True, 'scales': True}, {'clazz': 'water', 'fins': False, 'scales': True}, {'clazz': 'water', 'fins': True, 'scales': False}, {'clazz': 'bird', 'name': 'eagle'}, {'clazz': 'bird', 'name': 'dove'}, {'clazz': 'bird', 'name': 'raven'}, {'clazz': 'bird', 'name': 'hoopoe'}, {'clazz': 'bird', 'name': 'bat'}, {'clazz': 'swarm', 'name': 'locust', 'legs_above_feet': True}):
    show('  SH.classify(%r)' % (d,), lambda d=d: SH.classify(d), 300)
print('==== the runners\' cells and DATA keys:')
for M in (SH, SA, CA, ER, OR, PR, HO, HB, MO, TM, KO, YO, SN, ST, PN, PV, MM, SE):
    show('%s cells' % M.__name__[9:], lambda M=M: cells_of(M), 900)
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:60], 1200)
print('==== PV (primeval) — the cells naming the tithe, the clean beasts or the altar:')
for n in cells_of(PV):
    src = inspect.getsource(getattr(PV, n))
    if re.search(r'tithe|Melchizedek|clean|olah|altar|14:20|8:20|7:2', src): cell(PV, n, head_n=160)
print('==== HO.gifts and the import table:'); show('HO.GIFTS_IMPORT', lambda: getattr(HO, 'GIFTS_IMPORT', None), 400)
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['tithe_given', 'vowed', 'olah_offered', 'covenant_offered', 'portion_declared', 'tithe_of_the_tithe_commanded', 'nations_devoted', 'stranger_love_commanded', 'place_chosen_declared', 'profane_slaughter_permitted', 'kid_boiled_in_milk', 'carcass_eaten', 'carcass_touched', 'forbidden_kind_eaten', 'flesh_torn', 'herd_tithed', 'tithe_case', 'harvest_reaped', 'firstling_born', 'condemned_city_law_declared', 'word_sealed', 'demolition_restated']
print('==== THE TAPE\'S LINES (kind | subject | first verse | the source head | the line\'s other fields):')
import ast
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    if e.get('kind') in KINDS:
        cs = str(e.get('case_source', ''))
        print('  %-32s %-18s %-12s %-60s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:60], {k: (v if len(repr(v)) < 70 else repr(v)[:70]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== the tape\'s last Deuteronomy 13 lines (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 13:' in l[:140] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-2:]: print('  ' + l.strip()[:160])
print('==== the kin\'s ledgers on the one database (the counts the checkpoints and the probes read):')
import sqlite3, os
_WDB = os.path.join(ROOT, 'World', 'journal', 'data', 'world.sqlite')
if os.path.exists(_WDB):
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    for eff in ('rejoicing_before_the_lord_commanded', 'levite_forsaking_barred', 'holy_things_in_the_gates_barred', 'profane_slaughter_permitted', 'place_chosen_required', 'tithe_granted', 'inheritance_barred', 'tithe_given', 'tithe_vowed', 'treasured_people', 'left_for_the_poor', 'barred_from_it', 'impure_until_evening', 'torn_flesh_to_dogs', 'love_owed', 'lashes', 'high_places_banned', 'cuttings_for_the_dead_barred', 'abomination_eating_barred', 'carcass_eating_barred', 'second_tithe_owed', 'poor_tithe_owed', 'terumah_of_the_tithe_owed', 'same_day_slaughter_barred'):
        print('  %-36s %s' % (eff, [(e, n, str(v)[:24]) for e, n, v in c_.execute("SELECT entity, count(*), min(verse) FROM run_ledger WHERE effect=? GROUP BY entity", (eff,)).fetchall()[:8]]))
    print('  the open debits on israel_people', c_.execute("SELECT count(*) FROM run_ledger WHERE entity='israel_people' AND op='debit' AND (closed_by IS NULL OR closed_by='')").fetchall())
    print('  the ledger table\'s columns', [r[1] for r in c_.execute('PRAGMA table_info(run_ledger)').fetchall()])
