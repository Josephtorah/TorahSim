import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (2026-09-23): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the fifteen runners the design names, each ask the cells will consume, its value printed whole (a failing call prints its error, never hides it). RUN FROM THE REPO ROOT.
import os, sys, io, contextlib, subprocess, traceback
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9')
def load(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__('cold_run_' + name)
def show(label, fn):
    try:
        v = fn()
        print('FACT %s = %r' % (label, v))
    except Exception as ex:
        print('FAIL %s: %s: %s' % (label, type(ex).__name__, str(ex)[:300]))
MO = load('moadim'); PS = load('pesach'); CA = load('calendar'); ER = load('erection'); MU = load('musafim'); PN = load('place_name'); OS_ = load('opening_speech'); ES = load('exodus_story'); OR = load('ordinances'); HO = load('holiness'); ST = load('second_tablets'); SN = load('seven_nations'); CH = load('covenant_at_horeb'); JR = load('journeys'); PSH = load('pesach_sheni')
print('loaded fifteen runners')
D = lambda m: getattr(m, 'DATA', {})
show('MO.passover()', lambda: {k: (v['v'], v['p']) for k, v in MO.passover().items()})
show('MO.omer()', lambda: {k: (v['v'], v['p']) for k, v in MO.omer().items()})
show('MO.sukkot()', lambda: {k: (v['v'], v['p']) for k, v in MO.sukkot().items()})
show("MO.work_class('passover_7')", lambda: (MO.work_class('passover_7')['v'], MO.work_class('passover_7')['why']))
show("MO.work_class('passover_1')", lambda: MO.work_class('passover_1')['v'])
show("MO.work_class('atzeret')", lambda: MO.work_class('atzeret')['v'])
show("MO.work_class('sukkot_1')", lambda: MO.work_class('sukkot_1')['v'])
for a in ('eating_time', 'preparation', 'leftover', 'for_its_sake'):
    show("PS.paschal_procedure(%s)" % a, lambda a=a: PS.paschal_procedure({'ask': a}, D(PS))[:2])
show("PS.leaven_machine keys", lambda: [l for l in open(ROOT + '/World/step9/cold_run_pesach.py', encoding='utf-8').read().split('\n') if "case['ask'] ==" in l or "ask == '" in l][:20])
for k in ('able_male', 'woman', 'lame', 'blind_one_eye'):
    show("CA.pilgrimage(%s)" % k, lambda k=k: CA.pilgrimage({'kind': k}, D(CA))[:2])
show("CA.matzah(as_commanded)", lambda: CA.matzah({'ask': 'as_commanded'}, D(CA))[:2])
show("CA.offering_windows(leaven_beside_offering)", lambda: CA.offering_windows({'ask': 'leaven_beside_offering'}, D(CA))[:2])
show("CA.offering_windows(fat_overnight)", lambda: CA.offering_windows({'ask': 'fat_overnight'}, D(CA))[:2])
for q in ('chagigah_of_the_fourteenth_not_overnight', 'all_night_on_the_altar', 'purge_before_the_slaughter', 'standing_liability_like_the_appearance_offering', 'ingathering_after_the_turn', 'cow_grazes_unharmed', 'two_loaves_of_wheat_precede_bikkurim', 'existed_before_the_utterance'):
    show("ER.repeats(%s)" % q, lambda q=q: (ER.repeats(q)['v'], ER.repeats(q)['p'], ER.repeats(q)['fx'], ER.repeats(q)['why'][:160]))
for q in ('made_objects_not_the_ground', 'altar_class_forbidden'):
    show("ER.covenant(%s)" % q, lambda q=q: (ER.covenant(q)['v'], ER.covenant(q)['p'], ER.covenant(q)['fx'], ER.covenant(q)['why'][:160]))
for a in ('the_dates', 'the_seventh', 'redress_days', 'day_of_slaughter'):
    show("MU.pesach_shavuot(%s)" % a, lambda a=a: MU.pesach_shavuot({'ask': a}, D(MU))[:2])
for a in ('the_dates', 'the_eighth'):
    show("MU.sukkot(%s)" % a, lambda a=a: MU.sukkot({'ask': a}, D(MU))[:2])
for a in ('the_place_which_the_lord_will_choose', 'eat_there_and_rejoice', 'your_households', 'the_womans_rejoicing'):
    show("PN.the_place_chosen(%s)" % a, lambda a=a: PN.the_place_chosen({'ask': a}, D(PN))[:2])
show("PN.the_header_and_the_demolition(the_three_asherim)", lambda: PN.the_header_and_the_demolition({'ask': 'the_three_asherim'}, D(PN))[:2])
show("PN.the_profane_slaughter_the_blood_and_the_gates(you_may_not_eat_within_your_gates)", lambda: PN.the_profane_slaughter_the_blood_and_the_gates({'ask': 'you_may_not_eat_within_your_gates'}, D(PN))[:2])
for a in ('the_qualities', 'the_charge', 'no_faces', 'the_court_of_three', 'the_perverting_judge', 'judge_righteously'):
    show("OS.the_officers_and_the_judges(%s)" % a, lambda a=a: OS_.the_officers_and_the_judges({'ask': a}, D(OS_))[:2])
for q in ('judges', 'denominations', 'sanhedrin_sizes'):
    show("ES.jethro(%s)" % q, lambda q=q: (ES.jethro(q)['v'], ES.jethro(q)['p'], ES.jethro(q)['fx']))
for q in ('poor_not_glorified', 'asymmetry', 'twenty_three', 'one_vs_two', 'dissenter', 'bribe', 'bribe_absolute'):
    show("OR.courts(%s)" % q, lambda q=q: (OR.courts(q)['v'], OR.courts(q)['p'], OR.courts(q)['fx'], OR.courts(q)['why'][:120]))
show("HO.conduct(no_favor, who=poor)", lambda: (HO.conduct('no_favor', who='poor')['v'], HO.conduct('no_favor', who='poor')['fx']))
for q in ('scale_of_merit', 'five_effects', 'judge_is_measurer', 'bribe', 'equal_treatment'):
    show("HO.conduct(%s)" % q, lambda q=q: (HO.conduct(q)['v'], HO.conduct(q)['p'], HO.conduct(q)['fx']))
for a in ('takes_no_bribe', 'the_permitted_fee', 'lifts_no_face', 'a_salary_voids'):
    show("ST.the_god_of_gods_and_the_stranger(%s)" % a, lambda a=a: ST.the_god_of_gods_and_the_stranger({'ask': a}, D(ST))[:2])
show("ST.BRIBE_SCAN", lambda: getattr(ST, 'BRIBE_SCAN', 'no such name'))
for a in ('the_asherah_shade', 'the_asherah_wood', 'the_four_objects'):
    show("SN.the_seven_nations(%s)" % a, lambda a=a: SN.the_seven_nations({'ask': a}, D(SN))[:2])
for a in ('the_fourth_word', 'keep_and_remember', 'the_servants_rest'):
    show("CH.the_first_tablet(%s)" % a, lambda a=a: CH.the_first_tablet({'ask': a}, D(CH))[:2])
for a in ('figured_stones', 'high_places', 'three_objects_own', 'private_altar_eras'):
    show("JR.the_command(%s)" % a, lambda a=a: JR.the_command({'ask': a}, D(JR))[:2])
for a in ('who_keeps', 'distance', 'scope'):
    show("PSH.second_passover(%s)" % a, lambda a=a: PSH.second_passover({'ask': a}, D(PSH))[:2])
show('WE.CAL_PARAMS keys with festival/omer/intercal', lambda: [k for k in __import__('world_engine').CAL_PARAMS if any(t in k for t in ('festival', 'omer', 'intercal', 'evening', 'night', 'twilight'))])
show('WE.CAL_PARAMS[festival_dates][value]', lambda: __import__('world_engine').CAL_PARAMS['festival_dates']['value'])
show('WE.CAL_PARAMS[intercalated_month][value], threshold, grounds', lambda: (__import__('world_engine').CAL_PARAMS['intercalated_month']['value'], __import__('world_engine').CAL_PARAMS['intercalation_threshold_days']['value'], __import__('world_engine').CAL_PARAMS['intercalation_grounds']['value']))
show('the day slots (WE)', lambda: [d['name'] for d in __import__('yaml').safe_load(open(ROOT + '/World/step9/calendar_parameters.yaml', encoding='utf-8'))['day_slots']])
print('CALLEES DONE')
