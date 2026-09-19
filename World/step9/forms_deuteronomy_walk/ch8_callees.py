import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6): every CALL the design names, its signature, its
# source head and its result repr'd (cut), so the runner's asks copy the print. ch7_callees.py's form.
import sys, io, contextlib, subprocess, inspect, re
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_obey_horeb as OH, cold_run_exodus_story as ES, cold_run_shelach as SL, cold_run_beha as BH, cold_run_chukat as CK, cold_run_hear_o_israel as HI
    import cold_run_opening_speech as OS, cold_run_covenant_at_horeb as CH, cold_run_seven_nations as SN, cold_run_ordinances as OR, cold_run_sanctions as SA
    import cold_run_mamre as MA, cold_run_joseph as JS, cold_run_decalogue as DC
def sig(f): return f.__code__.co_varnames[:f.__code__.co_argcount]
def show(label, f):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:160])
    print('%-52s %s' % (label, repr(r)[:460]))
def cells_of(M): return [n for n in dir(M) if not n.startswith('_') and callable(getattr(M, n)) and getattr(getattr(M, n), '__module__', '') == M.__name__]
def cell(M, name, asks, head_n=700):
    f = getattr(M, name, None)
    if f is None: print('==== %s.%s MISSING; cells: %s' % (M.__name__, name, cells_of(M)[:40])); return
    src = inspect.getsource(f); print('==== %s.%s sig %s (%d chars) asks-in-source %s\n%s\n' % (M.__name__, name, sig(f), len(src), sorted(set(re.findall(r"(?:ask == |^\s*if a == |\bask\b == )'([a-z_0-9]+)'", src, re.M))), src[:head_n]))
    for a in asks:
        if len(sig(f)) >= 2 and sig(f)[0] == 'case': show('  %s.%s({ask:%s})' % (M.__name__[9:], name, a), lambda a=a: f({'ask': a}, M.DATA)[:2])
        else: show('  %s.%s(%r)' % (M.__name__[9:], name, a), lambda a=a: f(a))
cell(OH, 'the_exhortation', ['hear_and_do', 'live_and_possess', 'the_charge']); cell(OH, 'horeb_retold', ['take_heed_lest_you_forget', 'the_day_you_stood']); cell(OH, 'the_exile_case', ['the_witnesses', 'perish_and_scatter', 'serve_wood_and_stone']); cell(OH, 'the_one_god', ['because_he_loved_your_fathers', 'you_were_shown'])
cell(ES, 'manna', ['day_by_day', 'double', 'fifteenth_sabbath', 'forty_years', 'less_thirty', 'omer_before', 'sabbath', 'seventh_none', 'twilight', 'manna_form', 'test_clause']); cell(ES, 'trials', ['ten_list', 'count_by_exodus']); cell(ES, 'marah', ['healer_condition', 'statute_list']); cell(ES, 'sinai', ['treasure_seats'])
cell(BH, 'taberah_and_quail', ['dew', 'five_foods', 'manna_fell', 'manna_form', 'manna_taste'])
cell(SL, 'decree', ['day_for_year', 'count_from', 'deaths_ceased', 'due'])
cell(CK, 'meribah', ['first_meribah_clauses', 'meribah_seats', 'cattle_water']); cell(CK, 'arad_and_the_serpent', ['bite_and_burn', 'light_bread', 'nehushtan', 'pole_word', 'serpent_heals', 'singular_serpent'])
cell(HI, 'the_header', ['the_land_flowing', 'the_triad']); cell(HI, 'the_gift_and_the_warning', ['the_list', 'lest_you_forget', 'no_other_gods', 'fear_serve_swear']); cell(HI, 'the_sons_question', ['the_answer', 'the_question'])
cell(OS, 'the_bypass', ['forty_years_lacking_nothing']); cell(OS, 'the_spies_read_back', ['the_carrying', 'good_is_the_land', 'the_murmuring']); cell(OS, 'the_commission', ['the_great_and_terrible', 'the_wilderness', 'the_command'])
cell(CH, 'the_second_word', ['no_other_gods', 'bow_and_serve', 'the_visiting', 'the_header'])
cell(SN, 'the_holy_people', ['the_oath', 'brought_out_redeemed']); cell(SN, 'the_faithful_god', ['the_triad']); cell(SN, 'because_you_hear', ['the_heel']); cell(SN, 'the_seven_nations', ['the_ban'])
cell(OR, 'land', ['bread_water'])
cell(MA, 'moriah', ['test_verb_seats']); cell(MA, 'isaac_gerar', ['famine_ordinal']); cell(JS, 'the_oath', ['kindness_and_truth'])
print('==== SA cells:', cells_of(SA)); print('==== SA DATA keys:', list(getattr(SA, 'DATA', {}))[:60])
sa_live = [n for n in cells_of(SA) if 'live' in inspect.getsource(getattr(SA, n)).lower() and '18:5' in inspect.getsource(getattr(SA, n))]
print('==== SA cells mentioning 18:5 and live:', sa_live)
for n in sa_live[:3]:
    src = inspect.getsource(getattr(SA, n)); print('==== SA.%s sig %s asks %s\n%s\n' % (n, sig(getattr(SA, n)), sorted(set(re.findall(r"ask == '([a-z_0-9]+)'", src))), src[:900]))
print('==== DC cells:', cells_of(DC)); print('==== DC DATA keys:', list(getattr(DC, 'DATA', {}))[:60])
dc_second = [n for n in cells_of(DC) if '20:3' in inspect.getsource(getattr(DC, n)) or 'other gods' in inspect.getsource(getattr(DC, n))]
print('==== DC cells on the second word:', dc_second)
for n in dc_second[:2]:
    src = inspect.getsource(getattr(DC, n)); print('==== DC.%s sig %s asks %s\n%s\n' % (n, sig(getattr(DC, n)), sorted(set(re.findall(r"ask == '([a-z_0-9]+)'", src))), src[:900]))
print('==== ES cells:', cells_of(ES)); print('==== OS cells:', cells_of(OS)); print('==== OH cells:', cells_of(OH)); print('==== CK cells:', cells_of(CK)); print('==== SL cells:', cells_of(SL)); print('==== BH cells:', cells_of(BH))
for M in (OH, ES, SL, BH, CK, HI, OS, CH, SN):
    show('%s DATA keys' % M.__name__[9:], lambda M=M: list(getattr(M, 'DATA', {}))[:40])
show('SN.READBACK len / grades', lambda: (len(SN.READBACK), dict(SN.RB_GRADES)))
show('CH.READBACK len / grades', lambda: (len(CH.READBACK), dict(CH.RB_GRADES)))
show('HI.READBACK len / grades', lambda: (len(HI.READBACK), dict(HI.RB_GRADES)))
show('OS.READBACK len', lambda: len(OS.READBACK)); show('OH.READBACK len', lambda: len(OH.READBACK))
