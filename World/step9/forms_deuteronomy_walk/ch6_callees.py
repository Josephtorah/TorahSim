import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 4b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6): every CALL the design names, its result repr'd
# (cut), and the string-ask cells' source heads so the runner's asks copy the print. ch5_callees.py's form.
import sys, io, contextlib, subprocess, inspect
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_covenant_at_horeb as CH, cold_run_obey_horeb as OH, cold_run_decalogue as DC, cold_run_exodus_story as ES, cold_run_pesach as PE
    import cold_run_opening_speech as OS, cold_run_mamre as MA, cold_run_joseph as JS, cold_run_mekoshesh as MK, cold_run_erection as ER
def show(label, f):
    try: r = f()
    except Exception as e: r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:200])
    print('%-52s %s' % (label, repr(r)[:520]))
def head(label, f, n=1100):
    try: s = inspect.getsource(f)
    except Exception as e: s = 'RAISED %r' % e
    print('==== SOURCE %s (%d chars)\n%s\n' % (label, len(s), s[:n]))
for a in ('no_other_gods', 'the_visiting', 'the_write'): show('CH.the_second_word %s' % a, lambda a=a: CH.the_second_word({'ask': a}, CH.DATA)[:2])
for a in ('stand_here_with_me', 'the_charge', 'return_to_your_tents'): show('CH.the_answer_and_the_charge %s' % a, lambda a=a: CH.the_answer_and_the_charge({'ask': a}, CH.DATA)[:2])
show('len(CH.READBACK), dict(CH.RB_GRADES)', lambda: (len(CH.READBACK), dict(CH.RB_GRADES)))
show('CH.DATA keys', lambda: list(CH.DATA))
show('OH.horeb_retold take_heed_lest_you_forget', lambda: OH.horeb_retold({'ask': 'take_heed_lest_you_forget'}, OH.DATA)[:2])
show('OH.the_cities_and_the_frame the_second_frame', lambda: OH.the_cities_and_the_frame({'ask': 'the_second_frame'}, OH.DATA)[:2])
for a in ('seek_and_find', 'in_your_distress_return'): show('OH.the_exile_case %s' % a, lambda a=a: OH.the_exile_case({'ask': a}, OH.DATA)[:2])
show('OH.DATA keys', lambda: list(OH.DATA))
show("OH FORGET seats", lambda: [k for k in dir(OH) if 'FORGET' in k.upper()])
for a in ('vain_oath', 'false_future_oath'): show('DC.vain_name %s' % a, lambda a=a: DC.vain_name({'ask': a}, DC.DATA)[:2])
show('DC.DATA keys / len(DC.CASES)', lambda: (list(DC.DATA)[:12], len(DC.CASES)))
head('ES.trials', ES.trials); head('ES.plagues', ES.plagues, 700); head('ES.sea', ES.sea, 500)
for a in ('ten_list', 'count_by_exodus', 'tested'): show('ES.trials %s' % a, lambda a=a: ES.trials(a))
head('PE.firstborn', PE.firstborn, 1400)
show('PE.DATA keys', lambda: list(PE.DATA)[:20])
head('OS.the_frame', OS.the_frame, 900)
for a in ('the_write', 'the_oath', 'the_horeb_command', 'the_words'): show('OS.the_frame %s' % a, lambda a=a: OS.the_frame({'ask': a}, OS.DATA)[:2])
show('OS asks by cell', lambda: {c: [a for a in ('the_oath', 'the_horeb_command', 'the_regions', 'began_to_expound', 'the_words') if ("'%s'" % a) in inspect.getsource(getattr(OS, c))] for c in ('the_commission', 'the_frame', 'the_officers_and_the_judges', 'the_spies_read_back')})
head('MA.moriah', MA.moriah, 900); head('MA.isaac_gerar', MA.isaac_gerar, 700)
show('MA cell signature', lambda: MA.moriah.__code__.co_varnames[:MA.moriah.__code__.co_argcount])
head('JS.the_oath', JS.the_oath, 900)
head('MK.the_gatherer', MK.the_gatherer, 600)
show('MK.the_gatherer the_case', lambda: MK.the_gatherer({'ask': 'the_case'}, MK.DATA)[:2])
head('ER.ascent', ER.ascent, 700); head('ER.blood_covenant', ER.blood_covenant, 500)
show("ER.ascent torah_mitzvah", lambda: ER.ascent('torah_mitzvah'))
show("ER.blood_covenant book_of_covenant", lambda: ER.blood_covenant('book_of_covenant'))
show('CH.SCENE, CH.RUN-like', lambda: (getattr(CH, 'SCENE', None), getattr(CH, 'SCENE_PREDICTED', None)))
print('the signatures: %s' % {n: f.__code__.co_varnames[:f.__code__.co_argcount] for n, f in [('ES.trials', ES.trials), ('PE.firstborn', PE.firstborn), ('MA.moriah', MA.moriah), ('JS.the_oath', JS.the_oath), ('ER.ascent', ER.ascent), ('DC.vain_name', DC.vain_name), ('OS.the_frame', OS.the_frame)]})
