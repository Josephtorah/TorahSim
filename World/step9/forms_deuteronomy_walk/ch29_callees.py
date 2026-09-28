import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the runners the design names, each cell's asks READ FROM ITS SOURCE by regex (never typed), every ask called and its value printed whole by repr (16b's lesson 6 —
# never str); a failing call prints its error; a missing cell prints NO CELL; the near-name effects' counts on the running world at the end. ch26_callees.py's form
# over chapters 29-31 (the covenant, the return, the charge, the hakhel, the tent, the song, the book). RUN FROM THE REPO ROOT.
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
NAMES = ['opening_speech', 'gad_reuben', 'good_land', 'exodus_story', 'covenant_at_horeb', 'hear_o_israel', 'seven_nations', 'obey_horeb', 'second_tablets', 'not_righteousness', 'blessing_and_curse', 'seducers', 'food_tithe', 'release_firstborn', 'festivals_judges', 'courts_prophet', 'firstfruits_ebal_curses', 'refuge_war_family', 'tochacha', 'yovel', 'calendar', 'moadim', 'musafim', 'mamre', 'primeval', 'family', 'erection', 'beha', 'chukat', 'journeys', 'vestments', 'shelach', 'place_name', 'decalogue']
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
# ---- the recital (29:1-8): the signs, the forty years, Sihon and Og, the two and a half ----
cell('opening_speech', 'the_commission'); cell('opening_speech', 'sihon_and_og'); cell('opening_speech', 'the_bypass', ['forty_years_lacking_nothing', 'the_route', 'sihon_commanded']); dkeys('opening_speech', 'garment|forty|sihon|og|commission|joshua|hand|honor|urim|charge|strong')
cell('gad_reuben', 'the_acceptance_and_the_charge'); dkeys('gad_reuben', 'commission|land_east|nine|half|oath')
cell('good_land', 'the_way_of_forty_years'); cell('good_land', 'the_testimony'); cell('good_land', 'take_heed_lest_you_forget', ['the_triad', 'the_growth_list']); drow('good_land', ['the_garment_and_the_foot', 'not_by_bread_alone']); dkeys('good_land', 'garment|foot|bread|manna|forget|perish|receipt|satiet|fat')
cell('exodus_story', 'birth'); cell('exodus_story', 'sinai'); dkeys('exodus_story', 'birth|adar|hundred|twenty|pillar|cloud|sign|wonder|trial')
# ---- the covenant and the oath (29:9-14), the curse (29:15-20), the land (29:21-27), the hidden (29:28) ----
cell('covenant_at_horeb', 'the_assembly_called'); dkeys('covenant_at_horeb', 'assembly|hear|receipt|mediator|return_to_tents')
cell('hear_o_israel', 'the_gift_and_the_warning'); cell('hear_o_israel', 'the_creed'); dkeys('hear_o_israel', 'love|heart|soul|oath|cleave|swear')
cell('seven_nations', 'the_holy_people'); cell('seven_nations', 'because_you_hear'); dkeys('seven_nations', 'name|blot|heaven|fear|oath|fewest')
cell('obey_horeb', 'the_exile_case'); cell('obey_horeb', 'no_image', ['the_host_apportioned', 'the_covenant_not_forgotten', 'consuming_fire_jealous_god']); drow('obey_horeb', ['the_exile_case', 'the_witnesses_chain', 'the_host_apportioned']); dkeys('obey_horeb', 'exile|return|witness|scatter|wood|stone|host|apportion|seek')
cell('seducers', 'the_whole_offering_the_heap_and_the_mercy', ['as_he_swore_to_your_fathers', 'the_mercy_two_armed', 'the_anger_keyed_to_idolatry']); cell('seducers', 'the_inciter', ['the_inciters_kin']); dkeys('seducers', 'oath|swore|secret|other_gods|anger')
cell('mamre', 'mamre'); dkeys('mamre', 'sodom|gomorrah|brimstone|overthrow|salt|zeboiim|admah|fire')
cell('tochacha', 'covenant'); cell('tochacha', 'cascade'); cell('tochacha', 'measures'); dkeys('tochacha', 'confess|return|remember|recover|scatter|desolate|humble|uncircumcised')
cell('erection', 'calf'); cell('erection', 'presence'); dkeys('erection', 'pillar|cloud|door|tent|stiff|neck|whor|blot|book|face')
# ---- the return and the heart (30:1-10), not in heaven (30:11-14), life and death (30:15-20) ----
cell('second_tablets', 'the_levites_separated'); cell('second_tablets', 'the_third_forty_and_the_go'); dkeys('second_tablets', 'ark|carry|stiff|neck|circumcis|heart|joshua|charge|strong')
defs('not_righteousness'); drow('not_righteousness', ['the_stiff_necks_six_seats']); dkeys('not_righteousness', 'stiff|neck|rebel|oath|fathers|swore')
cell('firstfruits_ebal_curses', 'the_curses_of_the_siege_and_the_exile', ['as_he_rejoiced_so_he_rejoices_to_destroy', 'if_you_keep_not_all_the_words_of_this_law', 'left_few_in_number', 'scattered_among_all_peoples_to_serve_wood_and_stone']); cell('firstfruits_ebal_curses', 'the_people_this_day'); cell('firstfruits_ebal_curses', 'the_removal_and_the_confession', ['when_you_have_finished_tithing_in_the_third_year']); cell('firstfruits_ebal_curses', 'the_blessings', ['plenteous_in_goods_womb_beast_and_ground', 'if_you_diligently_hearken_all_these_blessings']); drow('firstfruits_ebal_curses', ['the_false_six', 'the_hearkening_state', 'the_three_covenants']); dkeys('firstfruits_ebal_curses', 'false_six|rejoic|hearkening_state|three_covenants|receipts|stiff|ketiv')
cell('blessing_and_curse', 'the_blessing_and_the_curse', ['see_i_set_before_you', 'the_blessing_if', 'the_curse_if', 'keep_to_do', 'study_and_deed']); dkeys('blessing_and_curse', 'life|death|choose|witness|set_before')
cell('primeval', 'prologue'); dkeys('primeval', 'hundred|twenty|inclin|yetzer|flood|reprieve|imagination')
# ---- the charge (31:1-8), the law written and the hakhel (31:9-13) ----
cell('shelach', 'spies', ['joshua_name', 'joshua_caleb_equal', 'forty_days']); dkeys('shelach', 'joshua|caleb')
cell('refuge_war_family', 'the_priests_speech'); dkeys('refuge_war_family', 'fear|priest|speech')
cell('journeys', 'lemma_seats') if False else None; drow('journeys', ['the_four_writings', 'the_death_date', 'the_eras_stamps']); dkeys('journeys', 'writ|death|date|adar|stamp')
cell('release_firstborn', 'the_release'); dkeys('release_firstborn', 'end|year|release|calendar|onset|hakhel|31|swore')
cell('food_tithe', 'the_third_year', ['the_removal_date', 'one_tithe_not_two']); dkeys('food_tithe', 'end|remov|hakhel|31|analogy')
cell('festivals_judges', 'the_feast_of_booths'); cell('festivals_judges', 'the_three_pilgrimages'); dkeys('festivals_judges', 'booth|appear|sukkot|eighth|hakhel|gather')
cell('courts_prophet', 'the_king'); dkeys('courts_prophet', 'copy|read|king|hakhel|agrippa|brother')
cell('place_name', 'the_place_chosen', ['the_stations_six_rows', 'the_name_pronounced_only_there', 'the_three_commandments_of_the_entry'])
defs('yovel'); dkeys('yovel', 'count|release|jubilee|seventh|shemitt|sabbatical|fifty')
cell('calendar', 'sabbatical'); dkeys('calendar', 'sabbatical|seventh|release|pilgrim|appear|year')
defs('moadim'); dkeys('moadim', 'sukkot|booth|eighth|fifteenth|seventh_month|atzeret')
cell('musafim', 'sukkot', ['the_dates', 'the_eighth', 'eighth_head', 'stay', 'seventy_nations', 'the_rite']); dkeys('musafim', 'sukkot|eighth|dates|stay')
# ---- the tent and the commission (31:14-15, 23), the apostasy (31:16-18), the song (31:19-22), the book (31:24-30) ----
cell('vestments', 'breastplate'); dkeys('vestments', 'urim|breastplate|judgment')
cell('chukat', 'edom_and_hor', ['death_dates', 'succession', 'thirty_days', 'aaron_age', 'moserah']); cell('chukat', 'well_and_kings', ['og_lore', 'deut3_delta', 'joshua_refrain', 'sihon_refused', 'lawgiver']); dkeys('chukat', 'cloud|well|manna|death|adar|miriam|gift')
defs('beha'); dkeys('beha', 'cloud|door|tent|miriam|twelve')
cell('family', 'testament'); dkeys('family', 'sleep|fathers|gathered|bury|testament|jacob')
dkeys('decalogue', 'other_gods|before_me|second_word')
print('==== THE NEAR NAMES ON THE RUNNING WORLD ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(k, e.get('op'), str(e.get('case_source', ''))[:14]) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in ('entered_the_covenant', 'became_the_lords_people_this_day', 'heaven_and_earth_witness', 'blessing_and_curse_set', 'cleaving_commanded', 'other_gods_barred', 'covenant_cut', 'covenant_declared', 'covenant_words_in_moab_declared', 'confessed', 'scattered_among_nations', 'scattered_among_all_peoples', 'land_desolate', 'return_to_egypt_barred', 'debt_release_owed', 'three_pilgrimages_commanded', 'appearance_owed', 'appearance_gift_owed', 'booths_at_the_place_commanded', 'law_copy_commanded', 'king_from_the_brothers_commanded', 'heart_circumcision_commanded', 'shema_commanded', 'forgetting_barred', 'israel_hears_and_fears', 'song_sung', 'fear_not_promised', 'love_owed', 'blotted_from_the_book', 'whored_after', 'reprieve_of_a_hundred_and_twenty', 'pillar_leads', 'camp_moves_by_the_cloud', 'fragments_in_the_ark', 'tablets_delivered', 'oath_sworn', 'agent_commissioned', 'commanded', 'return_promised', 'stiffening_barred', 'high_above_all_nations_promised', 'blessings_for_hearing', 'curses_for_not_hearkening', 'few_in_number_left', 'serving_wood_and_stone_among_nations', 'exiled_with_king_to_serve_wood_and_stone', 'plague_struck', 'seed_as_stars', 'witness_declared', 'ark_built', 'staves_fixed', 'rested_on_ararat', 'joshua_encouraged', 'covenant_upheld', 'covenant_remembered', 'oath_to_abraham_upheld', 'great_nation_promised', 'multiplied_on_the_earth'):
        n = nall(eff); print(' W', eff, len(n), n[:6])
    for who in ('moses', 'the-cloud', 'the_levites', 'the_ark', 'the_tent_of_meeting', 'sihon', 'og', 'sodom', 'the_half_tribe_of_manasseh', 'the_sons_of_gad_and_reuben', 'the_seventy_elders'):
        ent = w.entities.get(who); print(' LEDGER', who, len(ent.ledger) if ent else 'NO ENTITY', [(e['effect'], e.get('op'), str(e.get('case_source', ''))[:10]) for e in ent.ledger] if ent else '')
    print(' joshua entity:', 'joshua' in w.entities, '| entities naming joshua:', [k for k in w.entities if 'joshua' in k])
except Exception as ex:
    traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('CALLEES DONE')
