import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): THE CALLEES' SECOND PASS — the q-style cells' values and the DATA rows the fifteen cells will read, PRINTED BEFORE ANY ASSERT IS TYPED
# (the callees' way — 10b's lesson 2; 18b's ch26b_callees2.py the form): the keys read from the callees' sources at RUN B (mamre, erection, family, primeval, exodus_story, vestments,
# tochacha, calendar, yovel, moadim, chukat, beha, second_tablets, not_righteousness, obey_horeb, journeys, firstfruits_ebal_curses, seven_nations, opening_speech, festivals_judges,
# courts_prophet, gad_reuben, hear_o_israel, musafim, shelach, release_firstborn, food_tithe, place_name, refuge_war_family, seducers, blessing_and_curse, good_land, covenant_at_horeb).
# RUN FROM THE REPO ROOT.
import sys, os, io, contextlib, importlib, subprocess
ROOT = _ROOT
sys.path.insert(0, f'{ROOT}/World/step9'); os.chdir(f'{ROOT}/World/step9')
def load(n):
    with contextlib.redirect_stdout(io.StringIO()): return importlib.import_module('cold_run_' + n)
def S(x, n=260):
    s = repr(x); return s if len(s) <= n else s[:n] + ' …[%d]' % len(s)
def DD(m): return getattr(m, 'DATA', {})
def A(m, cell, ask): return getattr(m, cell)({'ask': ask}, DD(m))
MA, ER, FA, PV, ES, VE, TC, CA, YV, MD, CK, BH, ST, NR, OH, JR, FE, SN, OS, FJ, CP, GR, HI, MU, SH, RF, FT, PN, RW, SE, BC, GL, CH = [load(n) for n in ('mamre', 'erection', 'family', 'primeval', 'exodus_story', 'vestments', 'tochacha', 'calendar', 'yovel', 'moadim', 'chukat', 'beha', 'second_tablets', 'not_righteousness', 'obey_horeb', 'journeys', 'firstfruits_ebal_curses', 'seven_nations', 'opening_speech', 'festivals_judges', 'courts_prophet', 'gad_reuben', 'hear_o_israel', 'musafim', 'shelach', 'release_firstborn', 'food_tithe', 'place_name', 'refuge_war_family', 'seducers', 'blessing_and_curse', 'good_land', 'covenant_at_horeb')]
print('loaded 33')
# the q-style cells (a question key -> a dict)
for lab, fn in [('MA.mamre(outcry_closed_by)', lambda: MA.mamre('outcry_closed_by')), ('MA.mamre(appearance_seats)', lambda: MA.mamre('appearance_seats')),
                ('ER.presence(pillar_face)', lambda: ER.presence('pillar_face')), ('ER.presence(tent_outside)', lambda: ER.presence('tent_outside')), ('ER.calf(saru_stiff)', lambda: ER.calf('saru_stiff')), ('ER.calf(three_books)', lambda: ER.calf('three_books')),
                ('FA.testament(burial_command)', lambda: FA.testament('burial_command')), ('FA.testament(buried_named)', lambda: FA.testament('buried_named')),
                ('PV.prologue(reprieve_number)', lambda: PV.prologue('reprieve_number')), ('PV.prologue(wickedness_great)', lambda: PV.prologue('wickedness_great')), ('PV.prologue(reading_row)', lambda: PV.prologue('reading_row')),
                ('ES.birth(birthday)', lambda: ES.birth('birthday')), ('ES.birth(jochebed_age)', lambda: ES.birth('jochebed_age')), ('ES.plagues(ten)', lambda: ES.plagues('ten')), ('ES.sinai(treasure_seats)', lambda: ES.sinai('treasure_seats')),
                ('VE.breastplate(urim)', lambda: VE.breastplate('urim')), ('VE.breastplate(urim_end)', lambda: VE.breastplate('urim_end')),
                ('TC.covenant(F,F,F)', lambda: TC.covenant(False, False, False)), ('TC.covenant(T,T,T)', lambda: TC.covenant(True, True, True)), ('TC.cascade(5)', lambda: TC.cascade(5)), ('TC.measures()', lambda: TC.measures()),
                ('YV.cycle(7)', lambda: YV.cycle(7)), ('YV.cycle(8)', lambda: YV.cycle(8)), ('MD.sukkot()', lambda: MD.sukkot()),
                ('CA.sabbatical(home_engine)', lambda: CA.sabbatical({'ask': 'home_engine'}, DD(CA))), ('CA.sabbatical(timer)', lambda: CA.sabbatical({'ask': 'timer'}, DD(CA))), ('CA.pilgrimage(able_male)', lambda: CA.pilgrimage({'kind': 'able_male'}, DD(CA))), ('CA.pilgrimage(woman)', lambda: CA.pilgrimage({'kind': 'woman'}, DD(CA))),
                ('MU.sukkot(the_eighth)', lambda: A(MU, 'sukkot', 'the_eighth')), ('MU.sukkot(the_dates)', lambda: A(MU, 'sukkot', 'the_dates')),
                ('CK.edom_and_hor(death_dates)', lambda: A(CK, 'edom_and_hor', 'death_dates')), ('CK.edom_and_hor(succession)', lambda: A(CK, 'edom_and_hor', 'succession')), ('CK.edom_and_hor(thirty_days)', lambda: A(CK, 'edom_and_hor', 'thirty_days')),
                ('CK.well_and_kings(joshua_refrain)', lambda: A(CK, 'well_and_kings', 'joshua_refrain')), ('CK.well_and_kings(og_lore)', lambda: A(CK, 'well_and_kings', 'og_lore')), ('CK.well_and_kings(then_sang)', lambda: A(CK, 'well_and_kings', 'then_sang')),
                ('SH.spies(joshua_name)', lambda: A(SH, 'spies', 'joshua_name'))]:
    try:
        v = fn(); print('Q', lab, '=', S(v, 420))
    except Exception as e:
        print('Q', lab, 'FAILED', repr(e)[:200])
# the DATA rows
for lab, m, k in [('ST', ST, 'the_arks_contents_two_arms'), ('ST', ST, 'kings_reads_the_ark'), ('ST', ST, 'the_charge_to_joshua'), ('ST', ST, 'the_two_arks'), ('NR', NR, 'the_stiff_necks_six_seats'), ('NR', NR, 'the_merit_of_the_fathers'), ('OH', OH, 'the_witnesses_chain'), ('OH', OH, 'the_exile_case'), ('OH', OH, 'the_host_apportioned'),
                  ('JR', JR, 'the_four_writings'), ('JR', JR, 'the_death_date'), ('FE', FE, 'the_false_six'), ('FE', FE, 'the_three_covenants'), ('FE', FE, 'the_hearkening_state'), ('SN', SN, 'the_name_from_under_heaven'), ('SN', SN, 'the_fewest'), ('CK', CK, 'well_by_merit'), ('CK', CK, 'manna_absorbed'), ('CK', CK, 'miriam_death_day'), ('CK', CK, 'death_by_the_kiss'),
                  ('BH', BH, 'seven_clouds'), ('OS', OS, 'joshuas_charge'), ('OS', OS, 'the_judges_charge'), ('GL', GL, 'the_garment_and_the_foot'), ('FJ', FJ, 'the_exempt_from_appearing'), ('CP', CP, 'the_copys_form'), ('CP', CP, 'the_kings_condition'), ('RF', RF, 'the_release_date'), ('FT', FT, 'the_removal_date'), ('SE', SE, 'the_anger_keyed'), ('HI', HI, 'the_oath_by_the_name'), ('CH', CH, 'the_hear_and_do'), ('RW', RW, 'the_priests_saying'), ('GR', GR, 'the_oath_supplied')]:
    d = DD(m).get(k, '<ABSENT>'); print('DATA %s.%s =' % (lab, k), S(d, 420))
print('DATA KEYS OS', [k for k in DD(OS)][:40])
print('DATA KEYS CK', [k for k in DD(CK)][:40])
print('CALLEES2 DONE')
