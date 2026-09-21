import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 9b's form): every CALL the design names, its signature,
# its asks-in-source and EVERY ask's result repr'd (cut) — the older runners' cells take q (or booleans), the Deuteronomy runners' take (case, data): the print
# settles each form; and the tape's lines the readback references, their kinds, subjects and first verses read off the sequence file's TAPE block. RUN FROM
# THE REPO ROOT.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sanctions as SA, cold_run_korach as KR, cold_run_seven_nations as SN, cold_run_erection as ER, cold_run_ordinances as OR
    import cold_run_journeys as JO, cold_run_pre_sinai as PS, cold_run_calendar as CA, cold_run_shemini_day as SD, cold_run_tochacha as TC
    import cold_run_covenant_at_horeb as CH, cold_run_hear_o_israel as HI, cold_run_obey_horeb as OH, cold_run_good_land as GL
    import cold_run_blessing_and_curse as BC, cold_run_beha as BH, cold_run_borders as BR, cold_run_temurah as TM
    import world_engine as WE
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f, cut=240):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-60s %s' % (label, repr(r)[:cut]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def asks_in(src): return sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == |\bask in \(|\bq == |\bq in \()'([a-z_0-9]+)'", src, re.M)))
def cell(M, name, asks=None, head_n=220, cut=240):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); found = asks_in(src)
    print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), found, src[:head_n].replace('\n', '\n    ')))
    for a in (asks if asks is not None else found):
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2], cut)
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a), cut)
for M, names in ((SA, ['outside', 'blood', 'covering', 'molech', 'platform', 'frame']), (KR, ['the_gifts', 'the_tithe']), (SN, ['the_seven_nations', 'the_images_and_the_devoted']),
                 (ER, ['covenant', 'repeats']), (OR, ['altar', 'land']), (JO, ['the_command']), (PS, ['noahide']), (CA, ['matzah', 'kid_in_milk']), (SD, ['eras']),
                 (CH, ['the_first_tablet']), (HI, ['the_test_and_the_right']), (OH, ['the_exile_case']), (GL, ['the_testimony']), (BC, ['the_blessing_and_the_curse']),
                 (BH, ['march']), (BR, ['the_land_and_its_fall'])):
    for n in names: cell(M, n)
print('==== TC cells:', cells_of(TC)); print('    covenant sig', sig(TC.covenant), '| cascade sig', sig(TC.cascade))
show('TC.covenant(True, True, True)', lambda: TC.covenant(True, True, True), 500); show('TC.cascade(0)', lambda: TC.cascade(0), 400)
print('==== TM cells:', cells_of(TM))
for n in cells_of(TM):
    if 'substitut' in inspect.getsource(getattr(TM, n)).lower()[:3000]: cell(TM, n, head_n=160, cut=160)
for M in (SA, KR, SN, ER, OR, JO, PS, CA, SD, TC, CH, HI, OH, GL, BC, BH, BR, TM):
    show('%s cells' % M.__name__[9:], lambda M=M: cells_of(M), 700)
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:40], 700)
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['erected', 'gifts_granted', 'portion_declared', 'tithe_of_the_tithe_commanded', 'dispossession_commanded', 'limb_barred', 'nations_devoted', 'abomination_barred', 'perishing_testified', 'blessing_and_curse_set', 'second_paragraph_declared', 'hearing_blessed', 'blood_eaten', 'offering_slaughtered_outside', 'game_blood_poured', 'seed_given_to_molech', 'altar_built', 'herd_tithed', 'firstling_born']
print('==== THE TAPE\'S LINES (kind | subject | first verse | the source head | the line\'s other fields):')
import ast
for line in SRC.split('\n'):
    m = re.match(r"\s*w\.submit\((\{.*\})\)\s*#", line)
    if not m: continue
    try: e = ast.literal_eval(m.group(1))
    except Exception: continue
    if e.get('kind') in KINDS:
        cs = str(e.get('case_source', ''))
        print('  %-30s %-18s %-12s %-60s %s' % (e['kind'], e.get('subject'), WE.first_verse(cs), cs[:60], {k: (v if len(repr(v)) < 70 else repr(v)[:70]) for k, v in e.items() if k not in ('kind', 'subject', 'case_source')}))
print('==== the tape\'s last Deuteronomy 11 lines (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 11:' in l[:140] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-2:]: print('  ' + l.strip()[:160])
print('==== the-land\'s and the Levites\' ledgers on the one database (the kin the checkpoints count):')
import sqlite3, os
_WDB = os.path.join(ROOT, 'World', 'journal', 'data', 'world.sqlite')
if os.path.exists(_WDB):
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    for eff in ('high_places_banned', 'tithe_granted', 'inheritance_barred', 'house_abomination_barred', 'molten_image_barred', 'shema_commanded', 'blessing_and_curse_set', 'blood_reckoned', 'destroyed'):
        print('  %-28s %s' % (eff, c_.execute("SELECT entity, count(*), min(verse) FROM run_ledger WHERE effect=? GROUP BY entity", (eff,)).fetchall()[:6]))
