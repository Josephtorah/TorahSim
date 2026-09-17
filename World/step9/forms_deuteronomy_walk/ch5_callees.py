import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 3b — THE CALLEES' FACTS PRINTED BEFORE ANY ASSERT IS TYPED (2b's lesson 6: a callee's ask is typed from the recon's print,
# never from memory): every CALL the design names, its result repr'd (cut), so the runner's asserts copy the print.
import sys, io, contextlib, subprocess
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_decalogue as DC, cold_run_obey_horeb as OH, cold_run_erection as ER, cold_run_exodus_story as ES, cold_run_opening_speech as OS
    import cold_run_holiness as HO, cold_run_mishpatim_3 as M3, cold_run_sanctions as SA, cold_run_refuge as RF, cold_run_ordinances as OR, cold_run_pre_sinai as PS
def show(label, f):
    try:
        r = f()
    except Exception as e:
        r = 'RAISED %s: %s' % (type(e).__name__, str(e)[:200])
    print('%-46s %s' % (label, repr(r)[:420]))
for a in ('vain_oath', 'false_future_oath', 'vain_and_false_utterance'): show('DC.vain_name %s' % a, lambda a=a: DC.vain_name({'ask': a}, DC.DATA)[:2])
for a in ('remember', 'labor_scope', 'causing', 'laden_beast'): show('DC.sabbath_clauses %s' % a, lambda a=a: DC.sabbath_clauses({'ask': a}, DC.DATA)[:2])
for a in ('kidnapper', 'money_theft_here'): show('DC.theft_commandment %s' % a, lambda a=a: DC.theft_commandment({'ask': a}, DC.DATA)[:2])
show('DC.GUARDED / len(DC.CASES)', lambda: (DC.GUARDED, len(DC.CASES)))
show("OH.DATA['the_no_image_list']['value']", lambda: OH.DATA['the_no_image_list']['value'])
show("OH.DATA['the_horeb_hole']['value']", lambda: OH.DATA['the_horeb_hole']['value'])
for a in ('the_voice_and_no_form', 'the_ten_words_and_the_tablets'): show('OH.horeb_retold %s' % a, lambda a=a: OH.horeb_retold({'ask': a}, OH.DATA)[:2])
show('len(OH.READBACK), dict(OH.RB_GRADES)', lambda: (len(OH.READBACK), dict(OH.RB_GRADES)))
show('OH.GRADES', lambda: OH.GRADES)
for a in ('speech_with_speech', 'horev_plene'): show('ER.presence %s' % a, lambda a=a: ER.presence(a))
for a in ('book_of_covenant', 'one_voice', 'blood_of_covenant'): show('ER.blood_covenant %s' % a, lambda a=a: ER.blood_covenant(a))
show("ER.tablets ten_words", lambda: ER.tablets('ten_words'))
show("ER.ascent torah_mitzvah", lambda: ER.ascent('torah_mitzvah'))
for a in ('days_r_yose', 'we_will_do_seats', 'tub', 'one_heart', 'descents'): show('ES.sinai %s' % a, lambda a=a: ES.sinai(a))
show("ES.marah statute_list", lambda: ES.marah('statute_list'))
for a in ('the_asking', 'the_oath'): show('OS.the_spies_read_back %s' % a, lambda a=a: OS.the_spies_read_back({'ask': a}, OS.DATA)[:2])
show("OS.the_frame the_write", lambda: OS.the_frame({'ask': 'the_write'}, OS.DATA)[:2])
show('len(OS.READBACK)', lambda: len(OS.READBACK))
show('OS._closed_by_prior_run', lambda: OS._closed_by_prior_run)
for a in ('honor_defined', 'fear_defined', 'parents_order', 'three_partners', 'woman_included', 'persons_all'): show('HO.frame %s' % a, lambda a=a: HO.frame(a))
for a in ('mode', 'forewarning', 'his_fellow'): show('M3.killer %s' % a, lambda a=a: M3.killer(a))
for a in ('mode', 'either_parent'): show('M3.parent_striker %s' % a, lambda a=a: M3.parent_striker(a))
show('M3.parent_curser the_woman', lambda: M3.parent_curser('the_woman'))
for a in ('mode', 'both', 'whose_wife'): show('SA.adultery %s' % a, lambda a=a: SA.adultery(a))
for a in ('mode', 'which_parent'): show('SA.curser %s' % a, lambda a=a: SA.curser(a))
for a in ('he_is_a_murderer', 'the_mode'): show('RF.the_murderer %s' % a, lambda a=a: RF.the_murderer({'ask': a}, RF.DATA)[:2])
for a in ('false_report', 'witness_of_violence', 'one_vs_two'): show('OR.courts %s' % a, lambda a=a: OR.courts(a))
show('OR.capital signature', lambda: OR.capital.__code__.co_varnames[:OR.capital.__code__.co_argcount])
for a in ('delta_20_11', 'remember_by_call', 'creation_reason_by_call'): show('PS.sabbath %s' % a, lambda a=a: PS.sabbath(a))
for a in ('repeated_at_sinai', 'procreation_israel', 'idolatry_by_call'): show('PS.noahide %s' % a, lambda a=a: PS.noahide(a))
print('the signatures: HO.frame %s; M3.killer %s; SA.adultery %s; OR.courts %s; PS.sabbath %s; ER.presence %s; ES.sinai %s' % tuple(f.__code__.co_varnames[:f.__code__.co_argcount] for f in (HO.frame, M3.killer, SA.adultery, OR.courts, PS.sabbath, ER.presence, ES.sinai)))
