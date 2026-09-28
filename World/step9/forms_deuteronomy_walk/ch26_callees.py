import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the runners the design names, each cell's asks READ FROM ITS SOURCE by regex (never typed), every ask called and its value printed whole by repr (16b's lesson 6 —
# never str); a failing call prints its error; a missing cell prints NO CELL; the near-name effects' counts on the running world at the end. ch22_callees.py's form
# over three chapters. RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, traceback, inspect, collections
ROOT = _ROOT
sys.path.insert(0, ROOT + '/World/step9')
def load(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__('cold_run_' + name)
def show(label, fn):
    try:
        v = fn(); print('FACT %s = %r' % (label, v))
    except Exception as ex:
        print('FAIL %s: %s: %s' % (label, type(ex).__name__, str(ex)[:300]))
NAMES = ['food_tithe', 'release_firstborn', 'blessing_and_curse', 'seven_nations', 'place_name', 'festivals_judges', 'persons_poor_court', 'refuge_war_family', 'sanctions', 'mishpatim_3', 'holiness', 'second_tablets', 'courts_prophet', 'obey_horeb', 'good_land', 'decalogue', 'ordinances', 'tochacha', 'calendar', 'korach', 'chukat', 'naso', 'joseph', 'exodus_story', 'covenant_at_horeb', 'hear_o_israel', 'priesthood', 'chatat', 'borders', 'opening_speech', 'seducers', 'primeval', 'journeys', 'sanctuary_build', 'not_righteousness']
M = {}
for n in NAMES:
    try: M[n] = load(n); print('loaded', n)
    except Exception as ex: print('LOAD FAIL', n, type(ex).__name__, str(ex)[:200])
D = lambda m: getattr(m, 'DATA', {})
def asks_of(n, name):
    src = inspect.getsource(getattr(M[n], name))
    a = re.findall(r"if ask == '([a-z_0-9]+)':", src)
    q = re.findall(r"^\s+'([a-z_0-9]+)':\s*\{", src, re.M)
    return a, q
def call_cell(n, name, a):
    fn = getattr(M[n], name)
    try: return fn({'ask': a}, D(M[n]))
    except TypeError: return fn(a)
def fmt(v):
    if isinstance(v, dict) and 'v' in v: return (v.get('v'), v.get('p'), v.get('fx'), str(v.get('why', ''))[:260])
    if isinstance(v, dict): return {k: str(t)[:240] for k, t in v.items()}
    if isinstance(v, (list, tuple)): return v[:3]
    return str(v)[:400]
def cell(n, name, only=None):
    if n not in M: print('SKIP', n, name, '(not loaded)'); return
    if not hasattr(M[n], name): print('NO CELL %s.%s (defs: %s)' % (n, name, [f for f in dir(M[n]) if callable(getattr(M[n], f)) and not f.startswith('_')][:40])); return
    a, q = asks_of(n, name)
    print('CELL %s.%s: asks %d %s | keys %d %s' % (n, name, len(a), a[:40], len(q), q[:24]))
    for x in (only or a):
        show('%s.%s(%s)' % (n, name, x), lambda x=x: fmt(call_cell(n, name, x)))
    if not a and q:
        for x in (only or q)[:24]:
            show('%s.%s(%s)' % (n, name, x), lambda x=x: fmt(getattr(M[n], name)(x)))
def drow(n, keys):
    for k in keys:
        show('%s.DATA[%s]' % (n, k), lambda k=k: (lambda r: {kk: (str(vv)[:400] if kk != 'settings' else {s: str(t)[:200] for s, t in vv.items()}) for kk, vv in r.items()} if isinstance(r, dict) else str(r)[:400])(D(M[n])[k]))
def dkeys(n, pat):
    if n in M: print('DATA KEYS %s ~ %s: %s' % (n, pat, [k for k in D(M[n]) if re.search(pat, k)][:60]))
def defs(n):
    if n in M: print('DEFS', n, [f for f in dir(M[n]) if callable(getattr(M[n], f)) and not f.startswith('_') and f not in ('main',)][:70])
# ---- the first fruits, the tithes, the confession ----
cell('food_tithe', 'the_third_year'); cell('food_tithe', 'the_far_place_the_money_the_rejoicing_and_the_levite'); cell('food_tithe', 'the_second_tithe', ['the_liabilities', 'year_by_year', 'the_wall_two_capacities', 'the_house_standing', 'heavens_property']); cell('food_tithe', 'the_sons_and_the_cuttings', ['for_the_dead', 'the_holy_people', 'the_mourner_who_cuts'])
dkeys('food_tithe', 'tithe|remov|confess|levite|stranger|orphan|widow|third|second|first|holy|treasur|rejoic')
cell('calendar', 'first_fruits'); defs('calendar'); dkeys('calendar', 'first|fruit|bikkur|weeks|shavuot|omer|harvest')
cell('korach', 'the_gifts'); cell('korach', 'the_tithe'); dkeys('korach', 'first|fruit|bikkur|terumah|tithe|twenty|best|fat')
cell('chukat', 'edom_and_hor', ['firstfruits_clauses', 'edom_passage', 'two_messages'])
cell('priesthood', 'holy_food'); dkeys('priesthood', 'holy|tithe|first|fruit|bikkur|dead|mourn')
cell('chatat', 'share'); dkeys('chatat', 'share|dead|mourn|tithe')
cell('release_firstborn', 'the_needy_and_the_blessing'); dkeys('release_firstborn', 'receipt|pointer|lend|borrow|bless|hearken|28')
cell('place_name', 'the_place_chosen', ['eat_there_and_rejoice', 'the_three_commandments_of_the_entry', 'the_womans_rejoicing', 'the_stations_six_rows', 'the_name_pronounced_only_there']); cell('place_name', 'the_profane_slaughter_the_blood_and_the_gates', ['the_two_tithes', 'the_impure_tithes_warning', 'lest_you_forsake_the_levite', 'before_the_lord_you_shall_eat_it'])
cell('festivals_judges', 'the_three_pilgrimages'); cell('festivals_judges', 'the_judges_in_every_gate', ['take_no_bribe', 'wrest_no_judgment'])
cell('joseph', 'seventy'); cell('second_tablets', 'the_god_of_gods_and_the_stranger', ['seventy_persons', 'takes_no_bribe', 'the_orphan_and_the_widow', 'lifts_no_face'])
# ---- the covenant formula, the holy people, the treasure ----
cell('seven_nations', 'the_holy_people'); cell('seven_nations', 'because_you_hear'); dkeys('seven_nations', 'treasur|holy|chose|few|oath|bless|disease|barren')
cell('exodus_story', 'sinai'); dkeys('exodus_story', 'treasur|holy_nation|priests|covenant|offer|eagle|bondage|afflict|cry|sign|wonder|boil|disease|healer')
cell('covenant_at_horeb', 'the_assembly_called'); cell('covenant_at_horeb', 'the_second_tablet'); dkeys('covenant_at_horeb', 'honor|father|mother|reward|receipt|image|secret|mighty|arm')
cell('good_land', 'the_testimony'); cell('good_land', 'take_heed_lest_you_forget', ['the_triad', 'the_growth_list', 'the_exodus_formula']); dkeys('good_land', 'species|honey|milk|bless|forget|nation|perish|receipt')
cell('obey_horeb', 'the_exile_case'); cell('obey_horeb', 'no_image'); dkeys('obey_horeb', 'exile|scatter|few|wood|stone|image|witness|heaven|earth|nation|wise')
# ---- the stones, the altar, the writing ----
cell('decalogue', 'altar_rules'); cell('ordinances', 'altar_rules'); dkeys('ordinances', 'altar|stone|hewn|iron|earth|steps|sword'); dkeys('decalogue', 'altar|stone|hewn|iron|earth')
cell('sanctuary_build', 'altar'); dkeys('sanctuary_build', 'altar|whole|stone|iron')
cell('hear_o_israel', 'the_four_duties'); dkeys('hear_o_israel', 'mezuzah|doorpost|write|gate|stone|frontlet')
defs('opening_speech'); dkeys('opening_speech', 'explain|plain|baer|beer|language|seventy|tongue')
cell('journeys', 'lemma_seats') if False else None; dkeys('journeys', 'image|idol|judgment|gods')
# ---- the ceremony ----
cell('blessing_and_curse', 'the_blessing_and_the_curse'); cell('blessing_and_curse', 'the_second_paragraph'); dkeys('blessing_and_curse', 'gerizim|ebal|ceremony|rain|heaven|shut|yoke|order|tribe|tongue|amen|covenant')
cell('naso', 'blessing', ['form', 'language', 'who_blesses', 'translated', 'face_lifted', 'name'])
defs('borders'); dkeys('borders', 'order|tribe|reuben|ebal|gerizim')
# ---- the twelve curses' kin ----
cell('sanctions', 'grade'); cell('sanctions', 'curser'); cell('sanctions', 'unions_misc'); dkeys('sanctions', 'father|wife|beast|sister|mother_in_law|law|curse|secret|smit|murder')
cell('mishpatim_3', 'parent_curser'); dkeys('mishpatim_3', 'curs|parent|father|mother|kill|smit')
cell('holiness', 'conduct'); dkeys('holiness', 'blind|stumbl|deaf|curse|judgment|weight|neighbor|secret')
cell('refuge_war_family', 'the_landmark_and_the_witnesses', ['the_landmark_of_the_first_ones', 'the_talion_in_be']); cell('refuge_war_family', 'the_priests_speech', ['the_four_exemptions'])
cell('persons_poor_court', 'fathers_and_sons_the_stranger_and_the_gleanings', ['the_strangers_and_the_orphans_justice']); cell('persons_poor_court', 'the_fathers_wife_and_the_assembly', ['his_fathers_wife_and_his_fathers_skirt'])
cell('seducers', 'the_inciter', ['the_inciters_kin', 'the_hand_first']); cell('seducers', 'the_whole_offering_the_heap_and_the_mercy', ['as_he_swore_to_your_fathers'])
cell('courts_prophet', 'the_king'); dkeys('courts_prophet', 'egypt|ship|horse|return|king|way')
# ---- the curses' twin: Leviticus 26 ----
for c in ('covenant', 'cascade', 'measures', 'scaling', 'sabbath_debt', 'seventy_timer', 'jubilee_count'): cell('tochacha', c)
dkeys('tochacha', '.'); defs('tochacha')
cell('primeval', 'call'); dkeys('primeval', 'star|dust|nation|seed|few|call')
cell('not_righteousness', 'the_forty_days', ['prolong_without_expecting']) if False else None
print('==== THE NEAR NAMES ON THE RUNNING WORLD ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(k, e.get('op'), str(e.get('case_source', ''))[:14]) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in ('gerizim_ebal_ceremony_owed', 'blessing_and_curse_set', 'rain_in_its_season', 'heavens_shut_for_turning', 'treasured_people', 'poor_tithe_owed', 'second_tithe_owed', 'terumah_of_the_tithe_owed', 'rejoicing_before_the_lord_commanded', 'confessed', 'scattered_among_nations', 'land_desolate', 'chastised_sevenfold', 'return_to_egypt_barred', 'heaven_and_earth_witness', 'bless_after_eating_commanded', 'yoke_of_the_commandments_accepted', 'first_fleece_owed', 'tithe_given', 'tithe_granted', 'levites_portion_given', 'levite_forsaking_barred', 'three_pilgrimages_commanded', 'appearance_owed', 'appearance_gift_owed', 'blessings_for_hearing', 'work_of_the_hand_blessed', 'bribe_barred', 'landmark_removal_barred', 'stranger_orphan_justice_commanded', 'fathers_wife_barred', 'molten_image_barred', 'forgetting_barred', 'house_abomination_barred', 'israel_hears_and_fears', 'covenant_cut', 'covenant_declared', 'covenant_upheld', 'covenant_remembered', 'entered_the_covenant', 'seed_as_stars', 'seed_as_dust', 'great_nation_promised', 'came_to_egypt', 'enslaved', 'hard_bondage', 'cry_heard', 'sold_into_egypt', 'returned_to_egypt', 'struck_with_blindness', 'wombs_shut', 'plague_struck', 'death_by_heaven', 'slain_by_heaven', 'altar_built', 'altars_built', 'shema_commanded', 'high_court_at_the_place_commanded', 'place_chosen_required', 'horses_multiplying_barred', 'sabbath_debt', 'land_repays_sabbaths', 'ground_and_scattered'):
        n = nall(eff); print(' W', eff, len(n), n[:5])
    print(' the tribes as entities:', sorted(k for k in w.entities if k in ('reuben', 'simeon', 'levi', 'judah', 'issachar', 'zebulun', 'joseph', 'benjamin', 'dan', 'naphtali', 'gad', 'asher', 'ephraim', 'manasseh', 'the_levites', 'the_priests', 'the-priest', 'the-priests', 'the_priesthood', 'laban', 'moab', 'egypt_people', 'the_ground', 'the_land_of_canaan')))
except Exception as ex:
    traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('CALLEES DONE')
