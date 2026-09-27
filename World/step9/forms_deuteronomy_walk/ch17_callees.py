import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (2026-09-24): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the twenty runners the design names, each ask the cells will consume, its value printed whole (a failing call prints its error, never hides it); THE TAPE'S KINDS at the
# reference verses read from the sequence file's own submit lines. ch16_callees.py's form over two chapters. RUN FROM THE REPO ROOT.
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
SE = load('seducers'); FJ = load('festivals_judges'); OP = load('opening_speech'); ES = load('exodus_story'); OR = load('ordinances'); SA = load('sanctions'); HB = load('holiness_b'); PR = load('priesthood'); RF = load('release_firstborn'); KO = load('korach')
ST = load('second_tablets'); PN = load('place_name'); SN = load('seven_nations'); CH = load('covenant_at_horeb'); OH = load('obey_horeb'); RG = load('refuge'); MK = load('mekoshesh'); GL = load('good_land'); BK = load('balak'); PS_ = load('pre_sinai')
print('loaded twenty runners')
D = lambda m: getattr(m, 'DATA', {})
def cell(M, name, asks, label):
    fn = getattr(M, name)
    for a in asks:
        show('%s.%s(%s)' % (label, name, a), lambda a=a: fn({'ask': a}, D(M))[:2])
def qcell(M, name, qs, label, **kw):
    fn = getattr(M, name)
    for q in qs:
        show('%s.%s(%s)' % (label, name, q), lambda q=q: (lambda c: (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))[:160]) if isinstance(c, dict) else c)(fn(q, **kw)))
def drow(M, keys, label):
    for k in keys:
        show('%s.DATA[%s]' % (label, k), lambda k=k: (lambda r: {kk: (str(vv)[:400] if kk != 'settings' else {s: str(t)[:200] for s, t in vv.items()}) for kk, vv in r.items()} if isinstance(r, dict) else str(r)[:400])(D(M)[k]))
cell(SE, 'the_prophet_and_the_test', ['the_prophet_and_the_dreamer', 'the_sign_and_the_wonder', 'the_false_prophets_table', 'the_prophets_death', 'the_evil_purged', 'elijah_at_carmel', 'the_established_prophet'], 'SE')
cell(SE, 'the_inciter', ['the_hand_first', 'the_stoning_rite', 'the_courts_rule_inverted', 'the_execution_timing'], 'SE')
cell(SE, 'the_city_heard_of_the_inquiry_and_the_sword', ['the_seven_interrogations', 'the_congruence_rule', 'the_sword'], 'SE')
cell(SE, 'the_readback', ['the_purge_formulas_nine_seats', 'the_two_verbs_of_stoning'], 'SE')
cell(FJ, 'the_judges_in_every_gate', ['the_court_for_all_israel', 'the_three_tiers', 'justice_justice'], 'FJ')
cell(OP, 'the_officers_and_the_judges', ['the_hard_matter', 'the_court_of_three', 'money_and_capital', 'the_judgment_is_gods'], 'OP')
qcell(ES, 'jethro', ['sanhedrin_sizes', 'judges'], 'ES')
qcell(OR, 'courts', ['twenty_three', 'one_vs_two', 'no_retrial_acquitted', 'circumstantial'], 'OR')
qcell(OR, 'capital', ['sorceress_gender', 'sorceress_mode', 'sorceress_deed', 'sorceress_warning', 'idolater_row'], 'OR')
qcell(SA, 'molech', ['predicate', 'who_stones', 'seed_scope', 'effects_chain'], 'SA')
show('SA.three_are_one()', lambda: (lambda c: {k: str(v)[:200] for k, v in c.items()} if isinstance(c, dict) else str(c)[:600])(SA.three_are_one()))
show('SA.ov signature', lambda: __import__('inspect').signature(SA.ov))
for q in ('predicate', 'mode', 'asker', 'warning', 'definitions', 'stoning', 'court'):
    show('SA.ov(%s)' % q, lambda q=q: (lambda c: (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))[:160]) if isinstance(c, dict) else str(c)[:300])(SA.ov(q)))
qcell(HB, 'daughter_sanctuary', ['ov_consulter', 'ov_bearer', 'three_verses', 'definitions', 'turns_his_mind'], 'HB')
qcell(PR, 'acceptable', ['class_sweep', 'blemished_limb', 'cross_list', 'four_tokens', 'passing_blemish', 'everywhere'], 'PR')
qcell(PR, 'blemish', ['blemish_tokens', 'beast_unfits_in_man', 'other_blemishes'], 'PR')
cell(RF, 'the_blemish_and_the_blood', ['the_blemish_class', 'the_passing_blemish', 'the_blemished_in_the_gates'], 'RF')
cell(KO, 'the_gifts', ['twenty_four', 'most_holy_list', 'breast_and_thigh', 'the_best_triad', 'bikkurim', 'eaten_in_greatness'], 'KO')
cell(KO, 'the_tithe', ['no_inheritance', 'exclusion_table', 'tithe_to_levites'], 'KO')
cell(KO, 'the_watch', ['watch_places', 'lots', 'stranger_death'], 'KO')
cell(ST, 'the_levites_separated', ['to_stand_and_minister', 'levi_has_no_portion', 'as_the_lord_spoke_to_him', 'to_bless_in_his_name'], 'ST')
cell(PN, 'the_place_chosen', ['the_place_which_the_lord_will_choose', 'in_one_of_your_tribes'], 'PN')
cell(PN, 'the_profane_slaughter_the_blood_and_the_gates', ['you_may_not_eat_within_your_gates', 'lest_you_forsake_the_levite', 'the_levites_scope', 'the_blemished_consecrated'], 'PN')
cell(PN, 'the_nations_cut_off_and_the_abomination', ['lest_you_inquire_after_their_gods', 'their_sons_and_their_daughters', 'no_molech_named'], 'PN')
cell(SN, 'the_images_and_the_devoted', ['abomination_to_the_lord', 'utterly_detest'], 'SN')
cell(CH, 'the_voice_and_the_request', ['the_request', 'hear_and_do', 'added_no_more', 'you_came_near'], 'CH')
cell(CH, 'the_second_word', ['no_other_gods', 'bow_and_serve', 'in_its_way'], 'CH')
cell(OH, 'horeb_retold', ['the_day_at_horeb', 'the_voice_and_no_form', 'learn_and_teach'], 'OH')
drow(OH, ['the_host_apportioned', 'the_law_bal_tosif'], 'OH')
drow(RG, ['the_one_witness', 'the_court_of_twenty_three', 'the_presence_rows'], 'RG')
cell(MK, 'capital_procedure', ['stoning', 'stones_and_a_stone', 'venue', 'warning', 'mode', 'hanging'], 'MK')
drow(GL, ['the_kings_law_tokens', 'the_heart_lifted'], 'GL')
show('BK.the_stands signature', lambda: __import__('inspect').signature(BK.the_stands))
for q in ('no_divination', 'word_in_mouth_mode', 'judah_blessing', 'teruah_of_a_king'):
    show('BK.the_stands(%s)' % q, lambda q=q: BK.the_stands({'ask': q}, D(BK))[:2])
drow(BK, ['gentile_prophets', 'word_formula', 'star_reading'], 'BK')
qcell(PS_, 'circumcision', ['walk_whole', 'whole_read', 'kings', 'names_read'], 'PS_')
print('==== THE TAPE\'S KINDS AT THE REFERENCE VERSES (cold_run_sequence.py — the submit lines by case_source) ====')
seq = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
subs = re.findall(r"^\s+w\.submit\(\{'kind': '(\w+)'.*?'case_source': (?:'([^']*)'|\"([^\"]*)\")", seq, re.M)
print('submit lines with a case_source:', len(subs))
for pref in ('Exod 14:13', 'Exod 14:1', 'Deut 5:2', 'Deut 5:3', 'Deut 13:', 'Num 18:2', 'Num 18:8', 'Deut 10:8', 'Deut 10:9', 'Gen 35:1', 'Gen 20:7', 'Exod 18:2', 'Deut 1:1', 'Gen 17:1', 'Gen 49:10', 'Num 12:', 'Num 11:2', 'Deut 4:1', 'Deut 4:2', 'Deut 12:', 'Exod 22:1', 'Lev 20:', 'Lev 19:3', 'Num 35:3', 'Num 15:3', 'Lev 24:1', 'Exod 20:1', 'Deut 7:2', 'Deut 8:1', 'Deut 16:'):
    hits = [(k, (a or b)[:40]) for k, a, b in subs if (a or b).startswith(pref)]
    print(' TAPE %-10s %d %s' % (pref, len(hits), hits[:10]))
mk = re.findall(r"^\s+mk\('([^']+)'", seq, re.M)
print('markers naming Deut 5 / Exod 14 / Exod 20:', [x for x in mk if x.startswith(('Deut 5:', 'Exod 14:', 'Exod 20:', 'Deut 4:'))][:12])
print('CALLEES DONE')
