import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the runners the song's design names, each cell's asks READ FROM ITS SOURCE by regex (never typed), every ask called and its value printed whole by repr (16b's lesson 6 —
# never str); a failing call prints its error; a missing cell prints NO CELL; the near-name effects COMPUTED from the registry by the song's roots and counted on the
# running world at the end. ch29_callees.py's form over chapter 32 (the witnesses and the court law, the Name and the Rock, the nations divided and the LORD's portion,
# the desert and the manna, the eagle, the honey from the rock, Jeshurun fat, the demons and the new gods, the hidden face, the evils heaped and the rule of war and
# famine, the enemy's boast, the joined thousand, the vine of Sodom, the cup in store, I kill and I make alive, the land atones; the frame — the song spoken with Hoshea,
# the charge with Peah 1:1 and Chagigah 1:8, the summons to Nebo on the selfsame day, Aaron's death, Meribah's sentence). RUN FROM THE REPO ROOT (the background wrapper writes the DONE file).
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
NAMES = ['obey_horeb', 'covenant_return_charge', 'good_land', 'exodus_story', 'refuge_war_family', 'persons_poor_court', 'courts_prophet', 'refuge', 'ordinances', 'chukat', 'opening_speech', 'journeys',
         'second_tablets', 'primeval', 'pre_sinai', 'mamre', 'family', 'balak', 'beha', 'shelach', 'not_righteousness', 'seven_nations', 'hear_o_israel', 'blessing_and_curse', 'firstfruits_ebal_curses',
         'tochacha', 'seducers', 'decalogue', 'covenant_at_horeb', 'naso', 'incense_shekel', 'festivals_judges', 'holiness', 'vows', 'food_tithe', 'gad_reuben', 'borders', 'erection', 'sanctions', 'vayikra5', 'moadim', 'mekoshesh', 'place_name']
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
    print('CELL %s.%s: asks %d %s | keys %d %s' % (n, name, len(a), a[:60], len(q), q[:24]))
    for x in (only or a):
        show('%s.%s(%s)' % (n, name, x), lambda x=x: fmt(call_cell(n, name, x)))
    if not a and q:
        for x in (only or q)[:24]:
            show('%s.%s(%s)' % (n, name, x), lambda x=x: fmt(getattr(M[n], name)(x)))
def cellf(n, name, pat):
    # the asks READ from the source, the ones matching the pattern called (the cell's whole ask list printed first)
    if n not in M: print('SKIP', n, name, '(not loaded)'); return
    if not hasattr(M[n], name): print('NO CELL %s.%s (defs: %s)' % (n, name, [f for f in dir(M[n]) if callable(getattr(M[n], f)) and not f.startswith('_')][:40])); return
    a, q = asks_of(n, name)
    hit = [x for x in a if re.search(pat, x)]
    print('CELL %s.%s: asks %d %s | keys %d %s | matching %r: %s' % (n, name, len(a), a[:80], len(q), q[:24], pat, hit))
    for x in hit:
        show('%s.%s(%s)' % (n, name, x), lambda x=x: fmt(call_cell(n, name, x)))
def drow(n, keys):
    for k in keys:
        show('%s.DATA[%s]' % (n, k), lambda k=k: (lambda r: {kk: (str(vv)[:400] if kk != 'settings' else {s: str(t)[:200] for s, t in vv.items()}) for kk, vv in r.items()} if isinstance(r, dict) else str(r)[:400])(D(M[n])[k]))
def dkeys(n, pat):
    if n in M: print('DATA KEYS %s ~ %s: %s' % (n, pat, [k for k in D(M[n]) if re.search(pat, k)][:60]))
def defs(n):
    if n in M: print('DEFS', n, [f for f in dir(M[n]) if callable(getattr(M[n], f)) and not f.startswith('_') and f not in ('main',)][:70])
# ---- 32:1-4 the witnesses, the four rains, the Name and the response, the Rock — the court law's three rows (306:9, 306:12, 323:5 — Numbers 35:23) ----
cell('obey_horeb', 'the_exile_case'); cell('obey_horeb', 'no_image', ['the_host_apportioned', 'the_covenant_not_forgotten', 'consuming_fire_jealous_god']); cell('obey_horeb', 'the_one_god', ['the_former_days', 'from_heaven_the_voice', 'know_this_day', 'to_dispossess_nations'])
drow('obey_horeb', ['the_witnesses_chain', 'the_host_apportioned', 'the_exile_case', 'the_creed', 'the_instruments']); dkeys('obey_horeb', 'witness|host|apportion|jealous|fire|creed|scatter|seek')
cell('covenant_return_charge', 'the_song_commanded'); cell('covenant_return_charge', 'the_apostasy_foretold'); cell('covenant_return_charge', 'the_charge_and_the_crossing', ['a_hundred_and_twenty_years_old_this_day', 'moses_went_and_spoke_these_words_to_all_israel'])
drow('covenant_return_charge', ['the_receipts', 'the_kin_on_the_running_world', 'the_counter_and_the_parameters', 'the_twin_diffed', 'the_parsers_hits']); dkeys('covenant_return_charge', 'song|witness|face|hidden|inclination|death|adar|gift|readback')
cell('refuge_war_family', 'the_landmark_and_the_witnesses'); drow('refuge_war_family', ['the_parsers_ten_verses']); dkeys('refuge_war_family', 'witness|two|plot|enemy|hate|talion|nest|bird')
cell('courts_prophet', 'the_idolaters_trial'); cellf('courts_prophet', 'the_high_court', 'witness|two|three|inquir|hard|judge'); dkeys('courts_prophet', 'witness|two|three|stoning|inquiry')
defs('refuge'); drow('refuge', ['the_one_witness', 'the_lands_atonement', 'the_case_table', 'the_ransom_rows', 'the_avengers_hand', 'the_court_of_twenty_three']); dkeys('refuge', 'enemy|hate|witness|atone|ransom|kofer|blood|judge')
cellf('ordinances', 'courts', 'judge|pelil|ransom|kofer|witness|enemy|hate'); dkeys('ordinances', 'judge|pelilim|ransom|kofer|witness|enemy|hate')
defs('persons_poor_court'); dkeys('persons_poor_court', 'nest|bird|peah|gleaning|corner|measure|mixed|kilayim|vineyard|readback')
defs('sanctions'); dkeys('sanctions', 'burn|behead|sword|strangl|stoning|four_deaths|modes')
# ---- 32:5-9 the crooked generation, the Father who acquired, the days of old, the nations divided by the number of Israel, the LORD's portion ----
cellf('primeval', 'prologue', 'inclin|yetzer|hundred|twenty'); defs('primeval'); dkeys('primeval', 'babel|nations|divid|scatter|tongue|seventy|peleg|selfsame|inclin|flood|dust|shem|generations')
cell('seven_nations', 'the_holy_people'); drow('seven_nations', ['the_fewest', 'the_name_from_under_heaven', 'the_blessing_list', 'the_three_readings_of_favor']); dkeys('seven_nations', 'portion|treasure|chose|fewest|name|blot|seventy')
drow('food_tithe', ['the_holy_people_three_seats']); dkeys('food_tithe', 'treasure|holy|portion|sons')
drow('balak', ['seventy_nations', 'shema_candidate', 'gentile_prophets', 'balaam_share', 'gentile_share', 'star_reading']); cellf('balak', 'the_stands', 'jeshurun|king|seventy|nation|shema|dwell|alone'); dkeys('balak', 'seventy|nations|jeshurun|king|stands|shema|alone')
drow('not_righteousness', ['the_stiff_necks_six_seats', 'the_taunts_four_forms', 'the_merit_of_the_fathers', 'the_ten_names_of_prayer', 'the_three_voices_on_one_pronoun']); cell('not_righteousness', 'the_four_provocations'); cellf('not_righteousness', 'the_intercession', 'lest|say|hand|enemy|egypt|power|destroy|blot'); dkeys('not_righteousness', 'lest|say|hand|enemy|egypt|stiff|crooked|corrupt|taunt')
# ---- 32:10-14 the desert the Torah's school, the apple of the eye, the eagle, the LORD alone, the heights, the honey from the rock, the feast (317:2's offering classes) ----
cell('good_land', 'the_chain_and_the_covenant'); cell('good_land', 'the_way_of_forty_years'); cell('good_land', 'take_heed_lest_you_forget', ['the_triad', 'the_growth_list']); drow('good_land', ['the_two_rocks', 'honey_without_milk', 'the_garment_and_the_foot', 'not_by_bread_alone', 'the_credits', 'the_four_blessings', 'the_seven_species_seat']); dkeys('good_land', 'rock|honey|oil|manna|forget|fat|sated|serpent|flint|wilderness|eagle')
cell('exodus_story', 'sinai'); cellf('exodus_story', 'trials', 'trial|ten|massah|meribah|manna|quail'); cellf('exodus_story', 'birth', 'adar|hundred|twenty|nursing'); dkeys('exodus_story', 'eagle|treasure|manna|rock|horeb|massah|trial|selfsame|midst|host|song|sang|shira|pillar')
cell('beha', 'taberah_and_quail', ['manna_taste', 'manna_form', 'manna_fell', 'three_gifts', 'trials', 'six_hundred_thousand', 'nursing_father', 'graves', 'dew']); cellf('beha', 'seventy_elders', 'seventy|spirit|eldad'); dkeys('beha', 'gift|manna|cloud|well|trial|eagle|seventy')
drow('journeys', ['the_four_writings', 'the_death_date', 'aarons_age', 'the_eras_stamps', 'the_morrow_of_the_passover', 'the_judgments_on_the_gods', 'the_three_objects']); cell('journeys', 'aarons_death_retold'); dkeys('journeys', 'death|aaron|hor|adar|writ|selfsame|manna|forty')
cellf('festivals_judges', 'the_three_pilgrimages', 'appear|gift|hand|empty|measure|reiyah|chagig'); dkeys('festivals_judges', 'appear|reiyah|gift|hand|measure|chagigah|booth')
cellf('firstfruits_ebal_curses', 'the_first_fruits', 'measure|amount|species|seven|basket|time|shiur'); cell('firstfruits_ebal_curses', 'the_curses_of_the_siege_and_the_exile', ['a_nation_from_the_end_of_the_earth_as_the_eagle_flies', 'left_few_in_number', 'scattered_among_all_peoples_to_serve_wood_and_stone', 'the_sword_without_and_terror_within', 'as_he_rejoiced_so_he_rejoices_to_destroy'])
drow('firstfruits_ebal_curses', ['the_false_six', 'the_receipts', 'the_hearkening_state']); dkeys('firstfruits_ebal_curses', 'eagle|nation|siege|sword|terror|famine|blight|plague|first_fruits|bikkurim|measure')
defs('holiness'); dkeys('holiness', 'peah|corner|gleaning|kilayim|mixed|seed|measure|sixtieth|edge')
defs('moadim'); dkeys('moadim', 'chagigah|festival_offering|appear|peace|shelamim|booth'); defs('vayikra5'); dkeys('vayikra5', 'meilah|trespass|sacrileg|holies|asham'); defs('mekoshesh'); dkeys('mekoshesh', 'sabbath|labor|thirty_nine|gather|wood')
defs('vows'); dkeys('vows', 'substitut|kinnui|konam|dissol|annul|sage|hair|mountain|release'); defs('decalogue'); dkeys('decalogue', 'other_gods|before_me|second_word|jealous|vain|name|sabbath|labor')
# ---- 32:15-18 Jeshurun grew fat (the false eight), the demons and the new gods, the Rock forgotten — the idolatry predicate (13, 17), the jealous God ----
cell('seducers', 'the_inciter', ['the_inciters_kin', 'gods_you_have_not_known', 'near_or_far']); cell('seducers', 'the_whole_offering_the_heap_and_the_mercy', ['the_anger_keyed_to_idolatry', 'the_mercy_two_armed', 'as_he_swore_to_your_fathers']); drow('seducers', ['the_inciters_kin', 'the_five_prohibitions', 'the_signs_status']); dkeys('seducers', 'other_gods|new|near|fathers|knew|demon|abomination')
dkeys('covenant_at_horeb', 'other_gods|jealous|face|witness|thousand|generation'); defs('covenant_at_horeb'); cellf('covenant_at_horeb', 'the_ten_words', 'other_gods|jealous|second|thousand'); cellf('decalogue', 'vain_name', 'vain|name|profan|clear')
cellf('erection', 'calf', 'blot|book|stiff|lest|egypt|say|enemy|destroy|face'); cellf('erection', 'presence', 'face|cloud|door|glory|hidden|see'); dkeys('erection', 'blot|book|face|lest|egypt|say|stiff|glory')
cell('hear_o_israel', 'the_creed'); cell('hear_o_israel', 'the_four_duties'); drow('hear_o_israel', ['the_recitation_times', 'the_two_sets', 'the_seven', 'the_oath_by_the_name', 'the_list', 'the_four_sons']); dkeys('hear_o_israel', 'one|creed|teach|children|shema|evening|recit|time|love')
drow('blessing_and_curse', ['rain_dates', 'the_two_named_rains_added', 'every_living_thing_three_seats', 'the_counter_and_the_parameters']); cellf('blessing_and_curse', 'the_land_watered_by_heaven', 'rain|dew|former|latter|season|days|prolong|eyes'); cellf('blessing_and_curse', 'the_second_paragraph', 'days|prolong|children|teach|heaven|shut|rain'); dkeys('blessing_and_curse', 'rain|dew|days|prolong|latter|former|malkosh|teach|children')
# ---- 32:19-33 the hidden face, the no-people, the fire to Sheol, the evils heaped (321:9's rule of war and famine), the enemy's boast, the joined thousand (Leviticus 26:8), the vine of Sodom ----
cell('tochacha', 'cascade'); cell('tochacha', 'measures'); cellf('tochacha', 'covenant', 'remember|atone|land|enemies|confess|humble'); dkeys('tochacha', 'beast|sword|famine|pestilence|five|hundred|chase|flee|scatter|remember|atone|enemies|desolate|sabbath')
cellf('mamre', 'sodom', 'brimstone|overthrow|salt|vine|sin|outcry|ten|righteous|fire'); dkeys('mamre', 'sodom|gomorrah|vine|brimstone|salt|overthrow|outcry|zeboiim')
cell('pre_sinai', 'noahide'); cellf('pre_sinai', 'circumcision', 'selfsame|day|thirteen|ninety|ishmael'); drow('pre_sinai', ['the_seven', 'noahide']); dkeys('pre_sinai', 'noah|seven|command|selfsame|circumcis|rainbow|court|blood|limb|flesh')
cellf('naso', 'sotah', 'measure|thigh|belly|adorn|expos|order|first|mida'); dkeys('naso', 'measure|thigh|belly|adorn|sotah|mida')
# ---- 32:34-43 the cup in store, vengeance is Mine, the LORD judges His people, I kill and I make alive (no ransom), the land atones (21:8's atonement; Numbers 35:33) ----
cellf('incense_shekel', 'shekel', 'atone|kofer|ransom|soul|half|rich|poor'); cellf('incense_shekel', 'succession', 'aaron|garments|eleazar|hor|died'); dkeys('incense_shekel', 'atone|ransom|crown|succession|soul|kofer')
cellf('ordinances', 'courts', 'ransom|kofer|thirty|life|soul'); dkeys('refuge', 'atone|ransom|kofer|blood|pollut|expiat')
# ---- 32:44-52 the frame: the song spoken with Hoshea, the charge, the summons to Nebo on the selfsame day, Aaron's death, Meribah, the seeing and the entering ----
cell('shelach', 'spies', ['joshua_name', 'joshua_caleb_equal', 'named_after_deeds', 'forty_days', 'going_like_coming']); cellf('shelach', 'decree', 'forty|year|carcass|generation|twenty|caleb|joshua|day_for'); dkeys('shelach', 'joshua|hoshea|name|forty|generation|carcass|caleb')
cell('opening_speech', 'the_commission'); cell('opening_speech', 'the_bypass', ['forty_years_lacking_nothing', 'the_route']); drow('opening_speech', ['the_frame', 'the_date', 'the_dispossessions', 'the_thirty_eight']); dkeys('opening_speech', 'nebo|abarim|commission|sentence|debit|receipt|joshua|hoshea|pisgah|see')
cell('chukat', 'meribah', ['sentence', 'died_for_sin', 'meribah_seats', 'first_meribah_clauses', 'sin', 'death_by_the_kiss', 'burial_near_death', 'struck_twice', 'disgrace_written']); cell('chukat', 'edom_and_hor', ['death_dates', 'succession', 'aaron_age', 'thirty_days', 'seder_olam_walk', 'two_mount_hors', 'moserah']); dkeys('chukat', 'death|adar|aaron|hor|gift|cloud|well|manna|kiss|sanctif|meribah|zin|kadesh')
cell('second_tablets', 'the_stations_and_the_death'); drow('second_tablets', ['the_heaven_of_heavens_six', 'the_clock_read_back', 'the_place_of_the_death', 'the_stations_reversed', 'the_three_receipt_forms']); dkeys('second_tablets', 'heaven|aaron|death|choose|fathers|stations|moserah')
cellf('family', 'testament', 'gathered|fathers|sleep|bury|reuben|judah|joseph|expired|blessed|foot'); dkeys('family', 'gathered|fathers|sleep|bury|reuben|judah|joseph|testament')
drow('gad_reuben', ['moses_grave', 'deaths_ceased', 'the_oath_supplied', 'the_land_east_status']); dkeys('gad_reuben', 'grave|nebo|reuben|oath|death')
defs('borders'); dkeys('borders', 'hor|aaron|stem|border|see|land|canaan|four_sides'); cellf('borders', 'the_land_and_its_fall', 'canaan|inherit|fall|lot|see')
cellf('place_name', 'the_place_chosen', 'stations|entry|name|three_commandments|amalek|temple'); dkeys('place_name', 'stations|entry|witness')
print('==== THE NEAR NAMES ON THE RUNNING WORLD (the effects COMPUTED from the registry by the song\'s roots; counted on the world) ====')
try:
    import yaml as _y
    E = _y.safe_load(open(ROOT + '/World/step9/effect_vocabulary.yaml', encoding='utf-8')); eff = E.get('effects', E)
    PAT = re.compile(r'witness|song|face|hidden|forsak|manna|rock|eagle|treasure|portion|other_gods|demon|jealous|anger|fire|famine|beast|sword|terror|plague|scatter|exile|few|vengeance|aton|kill|alive|heal|days_on|prolong|teach|children|heart|nebo|abarim|gathered|aaron|meribah|sanctif|barred_from|see_the|selfsame|noah|seven|nations|divid|babel|inherit|sodom|vine|cup|treasur|seal|sold|deliver|judge|counsel|understand|wise|fat|rich|forgot|dew|rain|rebel|spurn|apple|wilderness|honey|wine|grape|sacrific|idol|abomin|provok|enemy|boast|arrow|sheol|hunger|pestil|venom|serpent|memory|cease|foot|slip|calamity|repent|servant|help|shelter|lift|live_forever|whet|blood|flesh|captive|expiat|lords_people|holy_people|acquired|father|generation|crooked|corrupt|foolish|two_witnesses|one_witness|three_witnesses|nest|peah|gleaning|mixed|measure|ransom|kofer|pollut|zimmun|amen|shema|recit|world_to_come|sheol')
    NEAR = sorted(n for n in eff if PAT.search(n))
    print(' NEAR effects', len(NEAR), 'of', len(eff))
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(e_): return [(k, e.get('op'), str(e.get('case_source', ''))[:14]) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == e_]
    for e_ in NEAR:
        n = nall(e_)
        if n: print(' W', e_, len(n), n[:8])
    print(' NEAR effects with NO entry on the world:', [e_ for e_ in NEAR if not nall(e_)])
    for who in ('moses', 'yehoshua', 'aaron', 'israel_people', 'the_levites', 'the_earth', 'the_land_of_canaan', 'the_lands', 'sodom', 'the_tent_of_meeting', 'jacob', 'noah_and_sons', 'egypt_people', 'moab'):
        ent = w.entities.get(who); print(' LEDGER', who, len(ent.ledger) if ent else 'NO ENTITY', [(e['effect'], e.get('op'), str(e.get('case_source', ''))[:10]) for e in ent.ledger][-14:] if ent else '')
    print(' entities', len(w.entities), '| events', sum(1 for l in w.log if l[0] == 'EVENT'), '| markers', sum(1 for l in w.log if l[0] == 'MARKER'), '| the day', w.clock.today() if hasattr(w.clock, 'today') else '(no today())')
except Exception as ex:
    traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('CALLEES DONE')
