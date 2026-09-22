import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6; 10b's form ch12_callees.py; 10b's lesson 2: a regex's silence is not
# a cell's — every cell's asks read at its own source): every CALL the design names, its signature, its asks-in-source and EVERY ask's result repr'd (cut) — the older
# runners' cells take q (or a case dict, or a default parameter), the Deuteronomy runners' take (case, data): the print settles each form; and the tape's lines the
# readback references, their kinds, subjects and first verses read off the sequence file's TAPE block; the one database's ledgers for the kin. RUN FROM THE REPO ROOT.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_obey_horeb as OH, cold_run_covenant_at_horeb as CH, cold_run_hear_o_israel as HI, cold_run_seven_nations as SN, cold_run_good_land as GL
    import cold_run_not_righteousness as NR, cold_run_second_tablets as ST, cold_run_blessing_and_curse as BC, cold_run_place_name as PN
    import cold_run_ordinances as OR, cold_run_erection as ER, cold_run_sanctions as SA, cold_run_lev24 as L24, cold_run_mekoshesh as MK, cold_run_temurah as TM
    import cold_run_chukat as CK, cold_run_balak as BK, cold_run_beha as BH, cold_run_mamre as MM, cold_run_holiness as HO
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
for M, names in ((OH, ['the_exhortation']), (CH, ['the_second_word', 'the_first_tablet']), (HI, ['the_test_and_the_right', 'the_four_duties', 'the_creed']), (SN, ['because_you_hear', 'the_seven_nations', 'the_images_and_the_devoted', 'the_holy_people']),
                 (GL, ['the_way_of_forty_years']), (NR, ['the_intercession', 'the_calf_retold']), (ST, ['the_god_of_gods_and_the_stranger', 'the_stations_and_the_death']), (BC, ['the_blessing_and_the_curse', 'the_second_paragraph']),
                 (PN, ['the_place_chosen', 'the_border_enlarged_and_the_altar', 'the_nations_cut_off_and_the_abomination']), (OR, ['capital', 'courts']), (ER, ['calf', 'cloud']), (SA, ['census', 'molech', 'frame', 'severity']),
                 (MK, ['capital_procedure']), (TM, ['devote']), (CK, ['arad_and_the_serpent']), (BK, ['peor']), (BH, ['miriam', 'march']), (MM, ['moriah']), (HO, ['conduct'])):
    for n in names: cell(M, n)
print('==== L24 cells:', cells_of(L24)); print('    talion sig', sig(L24.talion))
show('L24.talion()', lambda: L24.talion(), 500); show("L24.talion('tooth')", lambda: L24.talion('tooth'), 300)
for M in (OH, CH, HI, SN, GL, NR, ST, BC, PN, OR, ER, SA, L24, MK, TM, CK, BK, BH, MM, HO):
    show('%s cells' % M.__name__[9:], lambda M=M: cells_of(M), 700)
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:48], 900)
SRC = open(f'{ROOT}/World/step9/cold_run_sequence.py', encoding='utf-8').read().split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0]
KINDS = ['add_nothing_commanded', 'calf_made', 'calf_destroyed', 'tested', 'cloud_lifted', 'cleaving_commanded', 'stoned_as_commanded', 'stoning_carried_out', 'sentence_declared', 'canaanites_devoted_hormah_named', 'israel_vowed_the_cherem', 'hanging_commanded', 'nations_devoted', 'abomination_barred', 'hearing_blessed', 'nations_cut_off_warned', 'came_in_a_dream', 'dreamed', 'dream_told', 'sacrificed_to_gods', 'seed_given_to_molech', 'blasphemed_the_name', 'gathered_wood_on_the_sabbath', 'witnesses_called', 'thing_devoted', 'high_hand_case', 'peor_case', 'testing_barred', 'shema_declared', 'demand_declared']
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
print('==== the tape\'s last Deuteronomy 12 lines (the new lines go after them):')
tail = [l for l in SRC.split('\n') if 'Deut 12:' in l[:140] and ('w.submit' in l or 'w.marker' in l)]
for l in tail[-2:]: print('  ' + l.strip()[:160])
print('==== the kin\'s ledgers on the one database (the counts the checkpoints and the probes read):')
import sqlite3, os
_WDB = os.path.join(ROOT, 'World', 'journal', 'data', 'world.sqlite')
if os.path.exists(_WDB):
    c_ = sqlite3.connect('file:%s?mode=ro' % _WDB, uri=True)
    for eff in ('adding_barred', 'cleaving_commanded', 'pity_barred', 'other_gods_barred', 'test_barred', 'house_abomination_barred', 'destroyed', 'stoned', 'put_to_death', 'hanged', 'cherem_vowed', 'mark_of_anger', 'tested_the_lord', 'false_prophet_hearing_barred', 'devoted_thing_cleaving_barred', 'tested_by_the_lord', 'israel_hears_and_fears', 'condemned_city_inquiry_required', 'evil_purged_from_the_midst', 'city_devoted'):
        print('  %-32s %s' % (eff, [(e, n, str(v)[:24]) for e, n, v in c_.execute("SELECT entity, count(*), min(verse) FROM run_ledger WHERE effect=? GROUP BY entity", (eff,)).fetchall()[:8]]))
    print('  commanded devote_the_seven_nations', c_.execute("SELECT entity, count(*) FROM run_ledger WHERE effect='commanded' AND value LIKE '%devote_the_seven_nations%' GROUP BY entity").fetchall())
