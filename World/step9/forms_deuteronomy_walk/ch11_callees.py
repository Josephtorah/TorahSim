import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 9b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 8b's form): every CALL the design names, its signature,
# its asks-in-source and EVERY ask's result repr'd (cut) — the older runners' cells take q (or booleans), the Deuteronomy runners' take (case, data): the print
# settles each form; and the tape's lines the readback references, their kinds, subjects and first verses read off the sequence file's TAPE block.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_hear_o_israel as HI, cold_run_good_land as GL, cold_run_seven_nations as SN, cold_run_not_righteousness as NR, cold_run_obey_horeb as OH
    import cold_run_second_tablets as ST, cold_run_covenant_at_horeb as CH, cold_run_tochacha as TC, cold_run_ordinances as OR, cold_run_borders as BR
    import cold_run_korach as KR, cold_run_second_census as SC, cold_run_exodus_story as ES, cold_run_primeval as PR, cold_run_calendar as CA
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f, cut=360):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-64s %s' % (label, repr(r)[:cut]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def asks_in(src): return sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \(|\bq == |\bq in \()'([a-z_0-9]+)'", src, re.M)))
def cell(M, name, asks=None, head_n=300, cut=360):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); found = asks_in(src)
    print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), found, src[:head_n].replace('\n', '\n    ')))
    for a in (asks if asks is not None else found):
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2], cut)
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a), cut)
for M, names in ((HI, ['the_four_duties', 'the_header', 'the_creed', 'the_gift_and_the_warning']), (GL, ['the_frame', 'the_way_of_forty_years', 'the_good_land', 'the_testimony']),
                 (SN, ['the_seven_nations', 'the_holy_people', 'because_you_hear', 'do_not_fear']), (NR, ['the_frame']), (OH, ['the_one_god', 'the_exhortation']),
                 (ST, ['what_the_lord_asks', 'the_god_of_gods_and_the_stranger']), (CH, ['the_second_word']), (BR, ['the_four_sides', 'the_land_and_its_fall', 'moses_restatement']),
                 (KR, ['rebellion']), (SC, ['the_roll']), (ES, ['sea', 'plagues', 'night']), (PR, ['flood', 'nations']), (OR, ['land'])):
    for n in names: cell(M, n)
print('==== TC cells:', cells_of(TC)); print('    covenant sig', sig(TC.covenant), '| cascade sig', sig(TC.cascade))
print(inspect.getsource(TC.covenant)[:1400]); print(inspect.getsource(TC.cascade)[:1400])
show('TC.covenant(True, True, True)', lambda: TC.covenant(True, True, True), 700); show('TC.covenant(False, False, False)', lambda: TC.covenant(False, False, False), 700)
for k in (0, 1, 2, 5): show('TC.cascade(%d)' % k, lambda k=k: TC.cascade(k), 500)
print('==== CA cells:', cells_of(CA))
for n in cells_of(CA):
    if 'pilgrim_land_guarded' in inspect.getsource(getattr(CA, n)): cell(CA, n)
for M in (HI, GL, SN, NR, OH, ST, CH, TC, OR, BR, KR, SC, ES, PR, CA):
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:48], 900)
for M in (HI, GL, SN, NR, OH, ST, CH):
    show('%s.READBACK len / grades' % M.__name__[9:], lambda M=M: (len(M.READBACK), dict(getattr(M, 'RB_GRADES', {}))))
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['plague_struck', 'brought_out', 'pursued', 'sea_split', 'sea_returned', 'earth_swallowed', 'korach_gathered_against', 'dathan_and_abiram_refused', 'fire_consumed_the_two_hundred_fifty', 'all_flesh_expired', 'lot_chose', 'covenant_cut_with_abram', 'journeyed', 'borders_commanded', 'shema_declared', 'nations_devoted', 'hearing_blessed', 'demand_declared', 'cleaving_commanded', 'sworn_by_himself', 'testing_barred']
print('==== THE TAPE\'S LINES (kind | subject | first verse | the source head | the line\'s other fields):')
import ast
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    if e.get('kind') in KINDS:
        cs = str(e.get('case_source', ''))
        if e['kind'] == 'journeyed' and 'Shechem' not in cs and 'shechem' not in repr(e).lower(): continue
        print('  %-36s %-22s %-18s %-60s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:60], {k: (v if len(repr(v)) < 90 else repr(v)[:90]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== the tape\'s last Deuteronomy 10 lines (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 10:' in l[:140] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-2:]: print('  ' + l.strip()[:200])
