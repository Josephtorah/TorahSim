import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the twenty-three runners the design names, each ask the cells will consume, its value printed whole (a failing call prints its error, never hides it); THE TAPE'S
# KINDS at the reference verses read from the sequence file's own submit lines. ch17_callees.py's form over three chapters. RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, traceback
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
NAMES = ['place_name', 'obey_horeb', 'refuge', 'ordinances', 'courts_prophet', 'seducers', 'festivals_judges', 'lev24', 'seven_nations', 'midian', 'opening_speech', 'chukat', 'incense_shekel', 'primeval', 'family', 'zelophehad', 'mamre', 'release_firstborn', 'mekoshesh', 'balak', 'sanctions', 'pre_sinai', 'good_land']
M = {}
for n in NAMES:
    try: M[n] = load(n); print('loaded', n)
    except Exception as ex: print('LOAD FAIL', n, type(ex).__name__, str(ex)[:200])
D = lambda m: getattr(m, 'DATA', {})
def cell(n, name, asks):
    fn = getattr(M[n], name)
    for a in asks:
        show('%s.%s(%s)' % (n, name, a), lambda a=a: fn({'ask': a}, D(M[n]))[:2])
def qcell(n, name, qs, **kw):
    fn = getattr(M[n], name)
    for q in qs:
        show('%s.%s(%s)' % (n, name, q), lambda q=q: (lambda c: (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))[:200]) if isinstance(c, dict) else c)(fn(q, **kw)))
def drow(n, keys):
    for k in keys:
        show('%s.DATA[%s]' % (n, k), lambda k=k: (lambda r: {kk: (str(vv)[:400] if kk != 'settings' else {s: str(t)[:200] for s, t in vv.items()}) for kk, vv in r.items()} if isinstance(r, dict) else str(r)[:400])(D(M[n])[k]))
cell('place_name', 'the_nations_cut_off_and_the_abomination', ['when_the_lord_cuts_off_the_nations', 'lest_you_inquire_after_their_gods'])
cell('obey_horeb', 'the_cities_and_the_frame', ['then_moses_set_apart', 'not_until_all_six', 'the_manslayer_defined', 'the_three_names'])
drow('obey_horeb', ['the_three_cities', 'the_manslayer_definition'])
cell('refuge', 'the_refuge_law', ['six_cities', 'for_whom', 'unwittingly', 'until_he_stands'])
cell('refuge', 'the_murderer', ['the_iron', 'the_smiter', 'the_mode', 'the_intents', 'the_manners', 'the_avengers_hand'])
cell('refuge', 'the_manslayer', ['the_border', 'the_return', 'not_his_enemy', 'the_deliverance', 'the_levite_exiled', 'the_honor'])
drow('refuge', ['the_one_witness', 'the_avengers_hand', 'the_lands_atonement', 'the_court_of_twenty_three', 'the_blind_killer'])
qcell('ordinances', 'courts', ['witness_of_violence', 'false_report', 'one_vs_two', 'twenty_three', 'enemy_ox', 'who_is_enemy'])
qcell('ordinances', 'capital', ['idolater_row'])
cell('courts_prophet', 'the_idolaters_trial', ['found_means_witnesses', 'the_seven_investigations', 'two_witnesses_for_every_death', 'one_witness_and_the_disciple_silent', 'the_witnesses_hand_first'])
cell('courts_prophet', 'the_high_court', ['the_pairs', 'the_three_courts'])
cell('courts_prophet', 'the_levite_at_the_place', ['the_levite_who_is_a_priest'])
cell('courts_prophet', 'the_diviners', ['learn_to_understand_not_to_do'])
cell('seducers', 'the_city_heard_of_the_inquiry_and_the_sword', ['the_seven_interrogations', 'the_sword'])
cell('seducers', 'the_inciter', ['the_hand_first', 'the_stoning_rite'])
cell('seducers', 'the_readback', ['the_purge_formulas_nine_seats', 'the_two_verbs_of_stoning'])
cell('festivals_judges', 'the_judges_in_every_gate', ['the_court_for_all_israel', 'the_three_tiers'])
show('lev24.talion(eye)', lambda: {k: str(v)[:300] for k, v in M['lev24'].talion('eye').items()})
show('lev24.talion signature', lambda: __import__('inspect').signature(M['lev24'].talion))
cell('seven_nations', 'the_seven_nations', ['the_seven', 'the_ban', 'the_bans_condition'])
cell('seven_nations', 'do_not_fear', ['the_doubt', 'remember_pharaoh'])
cell('seven_nations', 'the_images_and_the_devoted', ['abomination_to_the_lord'])
cell('midian', 'the_vengeance', ['phinehas_anointed_for_war', 'the_trumpets', 'war_clause'])
cell('midian', 'the_war', ['every_male', 'captives', 'spoil'])
cell('midian', 'the_sentence', ['every_female_kept', 'the_sentence', 'deuteronomy_20'])
cell('midian', 'the_division', ['tribute_rate'])
cell('opening_speech', 'the_bypass', ['sihon_commanded', 'the_speech_resumed'])
drow('opening_speech', ['the_ban'])
cell('chukat', 'heifer_rite', ['yoke', 'blemish', 'age'])
qcell('incense_shekel', 'shekel', ['atone_souls', 'ransom'])
qcell('primeval', 'hagar', ['affliction_reading'])
qcell('family', 'inheritance', ['one_portion', 'given_as_gift', 'gift_returns_dispute', 'held_not_due', 'birthright_run', 'firstborn_by_call'])
qcell('family', 'testament', ['firstborn_my_strength', 'excess_named_denied'])
cell('zelophehad', 'inheritance_order', ['ladder', 'source_of_rule', 'firstborn_double'])
qcell('mamre', 'twins', ['firstborn_sheet', 'sale_with_oath'])
cell('release_firstborn', 'the_firstling', ['consecrated_from_the_womb'])
cell('mekoshesh', 'capital_procedure', ['stoning', 'stones_and_a_stone', 'hanging', 'burial', 'mode'])
cell('balak', 'peor', ['hang_before_the_sun', 'judges_count'])
qcell('sanctions', 'curser', ['mode', 'by_the_name'])
qcell('pre_sinai', 'noahide', ['bloodshed_seats', 'by_man'])
for ch in (19, 20, 21):
    show('good_land.receipt_seats(%d)' % ch, lambda ch=ch: M['good_land'].receipt_seats(ch))
print('==== THE TAPE\'S KINDS AT THE REFERENCE VERSES (cold_run_sequence.py — the submit lines by case_source) ====')
seq = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
subs = re.findall(r"^\s+w\.submit\(\{'kind': '(\w+)'.*?'case_source': (?:'([^']*)'|\"([^\"]*)\")", seq, re.M)
print('submit lines with a case_source:', len(subs))
for pref in ('Deut 12:29', 'Deut 4:41', 'Deut 17:2', 'Deut 13:', 'Deut 7:1', 'Deut 7:2', 'Deut 6:4', 'Num 21:21', 'Deut 2:24', 'Deut 2:26', 'Num 31:9', 'Num 31:13', 'Deut 18:9', 'Num 19:1', 'Gen 4:19', 'Gen 29:31', 'Gen 48:22', 'Gen 49:3', 'Num 27:6', 'Num 25:4', 'Lev 24:13', 'Lev 24:23', 'Gen 40:22', 'Gen 9:5', 'Num 35:9', 'Deut 16:18', 'Exod 30:1', 'Gen 16:', 'Gen 25:3', 'Exod 13:', 'Num 15:3', 'Deut 18:15', 'Deut 5:2'):
    hits = [(k, (a or b)[:44]) for k, a, b in subs if (a or b).startswith(pref)]
    print(' TAPE %-10s %d %s' % (pref, len(hits), hits[:10]))
print('the last Deut 18 submit line:', [(i, l[:100]) for i, l in enumerate(seq.split('\n'), 1) if "'kind': 'prophet_law_declared'" in l][:2])
print('CALLEES DONE')
