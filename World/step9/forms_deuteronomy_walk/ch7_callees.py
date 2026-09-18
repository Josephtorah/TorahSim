import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 5b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6): every CALL the design names, its signature, its
# source head and its result repr'd (cut), so the runner's asks copy the print. ch6_callees.py's form.
import sys, io, contextlib, subprocess, inspect
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_ordinances as OR, cold_run_erection as ER, cold_run_journeys as JO, cold_run_covenant_at_horeb as CH, cold_run_exodus_story as ES
    import cold_run_obey_horeb as OH, cold_run_opening_speech as OS, cold_run_balak as BK, cold_run_shemini as SH, cold_run_mamre as MA, cold_run_joseph as JS
    import cold_run_hear_o_israel as HI, cold_run_decalogue as DC
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-46s %s' % (label, repr(r)[:420]))
def cell(M, name, asks, head_n=900):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__][:40])); return
    src = inspect.getsource(f); print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), sorted(set(__import__('re').findall(r"(?:ask == |^\s*if a == |\bask\b == )'([a-z_0-9]+)'", src, __import__('re').M))), src[:head_n]))
    for a in asks:
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2])
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a))
cell(OR, 'land', ['hornet', 'little_by_little', 'no_barren', 'no_covenant', 'not_dwell', 'break_pillars', 'bread_water', 'serve_before', 'angel', 'borders', 'not_forgive'], 1400)
cell(ER, 'covenant', ['nations_seven_orders', 'no_covenant_by_call', 'daughters_two_seats', 'intermarriage_channels', 'child_follows_mother', 'cut_four', 'pillars_exod', 'molten_two_seats', 'demolition_first_seat', 'demolition_grows', 'sheet_az_2_3', 'sheet_az_3_5', 'sheet_az_4_2', 'sheet_az_4_4'], 1400)
cell(JO, 'the_command', ['drive_out', 'figured_stones', 'molten_images', 'high_places', 'three_objects_own', 'negative_arm', 'when_you_pass', 'possess_and_dwell'], 1400)
cell(CH, 'the_second_word', ['no_other_gods', 'the_visiting'], 700); cell(CH, 'the_tenth_word', ['covet_and_desire', 'the_coveter_who_pays', 'the_wife_first'], 700)
for n, asks in (('plagues', ['ten', 'the_ten', 'count', 'list']), ('sea', ['split', 'the_sea', 'crossing']), ('marah', ['healer_condition']), ('trials', ['ten_list', 'count_by_exodus']), ('amalek', ['blotting']), ('sinai', ['treasure_seats'])): cell(ES, n, asks, 700)
cell(OH, 'the_one_god', ['because_he_loved_your_fathers', 'to_dispossess_nations', 'you_were_shown'], 900)
cell(OS, 'the_spies_read_back', ['the_fear', 'greater_and_taller', 'the_doubt', 'our_brothers_melted'], 900)
cell(BK, 'peor', ['the_whoring', 'the_yoke', 'shittim', 'the_daughters'], 900)
cell(SH, 'classify', ['detest', 'the_verb', 'sheketz', 'creeping'], 900)
cell(MA, 'moriah', ['test_verb_seats']); cell(MA, 'isaac_gerar', ['famine_ordinal']); cell(JS, 'the_oath', ['kindness_and_truth'])
cell(HI, 'the_header', ['the_triad']); cell(HI, 'the_gift_and_the_warning', ['the_jealous_god'])
print('==== DC cells:', [n for n in dir(DC) if not n.startswith('_') and callable(getattr(DC, n)) and getattr(getattr(DC, n), '__module__', '') == DC.__name__])
print('==== ES cells:', [n for n in dir(ES) if not n.startswith('_') and callable(getattr(ES, n)) and getattr(getattr(ES, n), '__module__', '') == ES.__name__])
for M in (OR, ER, JO, CH, OH, OS, BK, SH, HI):
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:30])
show('CH.READBACK len / grades', lambda: (len(CH.READBACK), dict(CH.RB_GRADES)))
show('HI.READBACK len / grades', lambda: (len(HI.READBACK), dict(HI.RB_GRADES)))
show('OS.READBACK len', lambda: len(OS.READBACK)); show('OH.READBACK len', lambda: len(OH.READBACK))
