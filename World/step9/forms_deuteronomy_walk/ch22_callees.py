import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): THE CALLEES' FACTS printed before any assert is typed (10b's lesson 2 — every CALL's ask read at the cell's own source):
# the runners the design names, each cell's asks READ FROM ITS SOURCE by regex (never typed), every ask called and its value printed whole by repr (16b's lesson 6 —
# never str); a failing call prints its error; THE TAPE'S KINDS at the reference verses read from the sequence file's own submit lines; the near-name effects' counts
# on the running world. ch19_callees.py's form over four chapters. RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, traceback, inspect
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
NAMES = ['ordinances', 'mishpatim', 'mishpatim_2', 'mishpatim_3', 'holiness', 'holiness_b', 'sanctions', 'priesthood', 'yovel', 'vows', 'naso', 'negaim', 'metzora', 'beha', 'balak', 'exodus_story', 'family', 'zelophehad', 'mekoshesh', 'hear_o_israel', 'seducers', 'refuge_war_family', 'courts_prophet', 'festivals_judges', 'second_tablets', 'release_firstborn', 'covenant_at_horeb', 'seven_nations', 'place_name', 'primeval', 'mamre', 'joseph', 'lev24', 'chukat', 'good_land', 'obey_horeb', 'musafim', 'incense_shekel']
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
def cell(n, name, only=None):
    if n not in M: print('SKIP', n, name, '(not loaded)'); return
    a, q = asks_of(n, name)
    print('CELL %s.%s: asks %d %s | keys %d %s' % (n, name, len(a), a[:40], len(q), q[:20]))
    for x in (only or a):
        show('%s.%s(%s)' % (n, name, x), lambda x=x: (lambda v: v[:2] if isinstance(v, (list, tuple)) else ((v.get('v'), v.get('p'), v.get('fx'), str(v.get('why', ''))[:240]) if isinstance(v, dict) and 'v' in v else (str(v)[:400] if not isinstance(v, dict) else {k: str(t)[:240] for k, t in v.items()})))(call_cell(n, name, x)))
    if not a and q:
        for x in (only or q)[:24]:
            show('%s.%s(%s)' % (n, name, x), lambda x=x: (lambda v: (v.get('v'), v.get('p'), v.get('fx'), str(v.get('why', ''))[:240]) if isinstance(v, dict) and 'v' in v else (str(v)[:400] if not isinstance(v, dict) else {k: str(t)[:240] for k, t in v.items()}))(getattr(M[n], name)(x)))
def drow(n, keys):
    for k in keys:
        show('%s.DATA[%s]' % (n, k), lambda k=k: (lambda r: {kk: (str(vv)[:400] if kk != 'settings' else {s: str(t)[:200] for s, t in vv.items()}) for kk, vv in r.items()} if isinstance(r, dict) else str(r)[:400])(D(M[n])[k]))
def dkeys(n, pat):
    if n in M: print('DATA KEYS %s ~ %s: %s' % (n, pat, [k for k in D(M[n]) if re.search(pat, k)][:60]))
# ---- the property laws ----
cell('ordinances', 'courts'); cell('ordinances', 'loan'); cell('ordinances', 'stranger'); cell('ordinances', 'gifts'); cell('ordinances', 'capital')
dkeys('ordinances', 'ox|ass|burden|enemy|pledge|garment|sunset|interest|widow|orphan|stranger|bribe|lend')
dkeys('mishpatim', 'kidnap|steal|soul|wrestl|strive|hurt|talion|eye|tooth'); dkeys('mishpatim_2', 'seduc|virgin|betroth|dowry|fifty|wife|refuse|father'); dkeys('mishpatim_3', 'kidnap|steal|soul|maid|servant')
for nm in ('mishpatim', 'mishpatim_2', 'mishpatim_3'):
    if nm in M: print('DEFS', nm, [f for f in dir(M[nm]) if callable(getattr(M[nm], f)) and not f.startswith('_')][:60])
cell('holiness', 'gifts'); cell('holiness', 'wage'); cell('holiness', 'conduct'); dkeys('holiness', 'glean|corner|forgot|sheaf|wage|hire|morning|justice|weight|measure|balance|ephah')
cell('holiness_b', 'mixtures'); cell('holiness_b', 'maidservant'); cell('holiness_b', 'convert_measures'); dkeys('holiness_b', 'mix|kilay|wool|linen|seed|plow|weight|measure|convert|stranger|harlot|daughter')
cell('yovel', 'interest'); cell('yovel', 'interest_scope'); cell('yovel', 'support_duty'); cell('yovel', 'sale_manner'); dkeys('yovel', 'interest|bite|increase|foreign|brother|slave|rigor')
# ---- the family and sex laws ----
cell('sanctions', 'grade'); cell('sanctions', 'levirate'); cell('sanctions', 'cowives'); cell('sanctions', 'unions_misc'); cell('sanctions', 'curser'); cell('sanctions', 'frame'); cell('sanctions', 'blood'); cell('sanctions', 'census'); dkeys('sanctions', 'father|wife|adulter|lash|forty|stripe|levir|brother|union|mamzer|crush|assembly|kahal')
cell('priesthood', 'family'); cell('priesthood', 'acceptable'); cell('priesthood', 'holy_food'); dkeys('priesthood', 'divorc|harlot|hire|dog|profan|crush|kahal|assembly')
cell('family', 'levirate'); cell('family', 'commission'); cell('family', 'purchase'); cell('family', 'inheritance'); cell('family', 'testament'); dkeys('family', 'levir|yavam|onan|tamar|shoe|sandal|name|seed|widow|divorc|bill|get|betroth|seduc')
cell('zelophehad', 'the_daughters', ['levirate_dilemma', 'name_is_inheritance', 'child_of_any_kind', 'reach'])
cell('primeval', 'hagar'); cell('primeval', 'separation'); cell('mamre', 'law_mamre') if False else None; dkeys('mamre', 'husband|baal|married|sarah|wife'); dkeys('primeval', 'humbl|afflict|hagar')
cell('joseph', 'dinah'); cell('joseph', 'potiphar'); dkeys('joseph', 'folly|nevalah|dinah|shechem|seduc|garment|potiphar')
cell('mishpatim_2', 'grade') if 'mishpatim_2' in M and hasattr(M['mishpatim_2'], 'grade') else None
# ---- the assembly, the camp, the persons ----
cell('balak', 'the_call'); cell('balak', 'the_stands'); dkeys('balak', 'hire|curse|bless|moab|ammon|bread|water|way|love')
cell('naso', 'camp_purity'); dkeys('naso', 'camp|unclean|leper|zav|corpse|sent')
cell('negaim', 'law_negaim') if 'negaim' in M and hasattr(M['negaim'], 'law_negaim') else None; dkeys('negaim', 'priest|teach|declar|shut|quarant|leprous'); dkeys('metzora', 'priest|cleans|shav|bird')
cell('beha', 'miriam', ['remember_miriam', 'kin_rule', 'quarantine', 'days', 'as_one_dead', 'measure_for_measure'])
cell('courts_prophet', 'the_blemished_sacrifice', ['the_mounter_and_the_harlots_hire', 'the_sacrifice_not_the_sacrificer']); cell('courts_prophet', 'the_diviners', ['learn_to_understand_not_to_do'])
cell('seven_nations', 'the_images_and_the_devoted', ['abomination_to_the_lord', 'into_your_house', 'devoted_like_it'])
cell('place_name', 'the_nations_cut_off_and_the_abomination', ['lest_you_inquire_after_their_gods', 'their_sons_and_their_daughters'])
cell('vows', 'the_man', ['delay_clocks', 'sin_in_you', 'lips_or_heart', 'vow_vs_gift', 'vower_a_sinner', 'frame', 'this_is_the_thing']); cell('vows', 'hearing_due'); cell('vows', 'the_widow', ['levirate']); cell('vows', 'the_betrothed', ['levirate_widow'])
dkeys('musafim', 'vow|deadline|feast|three')
cell('hear_o_israel', 'rb'); dkeys('hear_o_israel', 'tzitzit|fringe|tassel|corner|thread|blue')
cell('mekoshesh', 'capital_procedure', ['stoning', 'hanging', 'burial', 'mode']); dkeys('mekoshesh', 'tzitzit|fringe|tassel|corner|thread|blue|garment|wing')
for nm in ('mekoshesh', 'hear_o_israel', 'naso', 'negaim', 'metzora', 'exodus_story', 'beha', 'balak', 'sanctions', 'priesthood', 'family', 'holiness', 'holiness_b', 'ordinances', 'yovel', 'vows', 'covenant_at_horeb', 'obey_horeb', 'second_tablets', 'seducers'):
    if nm in M: print('DEFS', nm, [f for f in dir(M[nm]) if callable(getattr(M[nm], f)) and not f.startswith('_') and f not in ('main',)][:70])
# ---- the court, the poor, the remembrances ----
cell('seducers', 'the_prophet_and_the_test', ['the_evil_purged']); cell('seducers', 'the_readback', ['the_purge_formulas_nine_seats', 'the_two_verbs_of_stoning']); cell('seducers', 'the_inciter', ['the_hand_first', 'the_stoning_rite'])
cell('refuge_war_family', 'the_landmark_and_the_witnesses', ['the_talion_in_be', 'one_witness_for_any_iniquity', 'the_violent_witness_and_the_woman']); cell('refuge_war_family', 'the_priests_speech', ['the_four_exemptions', 'the_fearful_and_the_faint_of_heart']) ; cell('refuge_war_family', 'the_captive', ['the_release_a_divorce'] if False else None)
cell('festivals_judges', 'the_judges_in_every_gate', ['wrest_no_judgment', 'respect_no_person', 'take_no_bribe', 'justice_justice'])
cell('second_tablets', 'the_god_of_gods_and_the_stranger', ['the_orphan_and_the_widow', 'and_you_shall_love_the_stranger', 'the_thirty_six_warnings'])
cell('release_firstborn', 'the_needy', None) if 'release_firstborn' in M and hasattr(M['release_firstborn'], 'the_needy') else None
dkeys('release_firstborn', 'sin|cry|slave|remember|needy|hand|bless|work'); print('DEFS release_firstborn', [f for f in dir(M['release_firstborn']) if callable(getattr(M['release_firstborn'], f)) and not f.startswith('_')][:40] if 'release_firstborn' in M else None)
cell('covenant_at_horeb', 'the_first_tablet', ['the_fourth_word', 'keep_and_remember', 'the_ox_and_the_ass', 'the_servants_rest', 'the_two_grounds']); dkeys('covenant_at_horeb', 'reward|long|days|well|honor|slave')
dkeys('obey_horeb', 'long|days|well|reward'); dkeys('good_land', 'receipt|bless|work|hand')
show('good_land.receipt_seats(22..25)', lambda: [M['good_land'].receipt_seats(c) for c in (22, 23, 24, 25)])
cell('exodus_story', 'amalek'); dkeys('exodus_story', 'amalek|blot|remember|memory|generation|hand|throne')
show('lev24.talion(hand)', lambda: {k: str(v)[:300] for k, v in M['lev24'].talion('hand').items()})
cell('chukat', 'arad_and_the_serpent', ['bite_and_burn', 'cherem_law'])
cell('incense_shekel', 'shekel', ['ransom', 'atone_souls'])
print('==== THE TAPE\'S KINDS AT THE REFERENCE VERSES (cold_run_sequence.py — the submit lines by case_source) ====')
seq = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
subs = re.findall(r"^\s+w\.submit\(\{'kind': '(\w+)'.*?'case_source': (?:'([^']*)'|\"([^\"]*)\")", seq, re.M)
print('submit lines with a case_source:', len(subs))
for pref in ('Exod 23:4', 'Exod 23:5', 'Exod 22:15', 'Exod 22:16', 'Exod 22:20', 'Exod 22:21', 'Exod 22:24', 'Exod 22:25', 'Exod 21:16', 'Exod 21:22', 'Exod 21:24', 'Lev 19:9', 'Lev 19:13', 'Lev 19:15', 'Lev 19:19', 'Lev 19:29', 'Lev 19:33', 'Lev 19:35', 'Lev 18:8', 'Lev 20:10', 'Lev 21:7', 'Lev 22:24', 'Lev 25:35', 'Lev 25:36', 'Lev 13:', 'Lev 14:', 'Lev 15:16', 'Num 15:37', 'Num 15:38', 'Num 30:', 'Num 12:', 'Num 22:', 'Num 23:', 'Num 24:', 'Num 5:1', 'Num 5:2', 'Num 5:4', 'Exod 17:8', 'Exod 17:14', 'Exod 17:16', 'Gen 38:', 'Gen 20:3', 'Gen 34:7', 'Deut 5:12', 'Deut 5:15', 'Deut 7:25', 'Deut 7:26', 'Deut 10:18', 'Deut 12:31', 'Deut 13:6', 'Deut 15:9', 'Deut 15:10', 'Deut 15:15', 'Deut 16:19', 'Deut 16:20', 'Deut 17:1', 'Deut 18:12', 'Deut 19:13', 'Deut 19:15', 'Deut 19:21', 'Deut 20:7', 'Deut 21:14', 'Deut 21:22', 'Deut 2:9', 'Deut 2:19', 'Deut 2:26', 'Deut 4:40', 'Deut 5:16', 'Deut 6:2', 'Deut 8:11', 'Deut 9:7', 'Deut 11:9', 'Deut 14:29', 'Num 35:30', 'Num 35:31', 'Lev 24:19', 'Lev 24:20', 'Deut 21:1', 'Deut 21:15', 'Deut 21:18'):
    hits = [(k, (a or b)[:44]) for k, a, b in subs if (a or b).startswith(pref)]
    print(' TAPE %-10s %d %s' % (pref, len(hits), hits[:10]))
print('the last Deut 21 submit line:', [(i, l[:100]) for i, l in enumerate(seq.split('\n'), 1) if "'kind': 'hanged_burial_declared'" in l][:2])
print('==== THE NEAR NAMES ON THE RUNNING WORLD ====')
try:
    import register_census as R
    with contextlib.redirect_stdout(io.StringIO()):
        w = R.running_world()
    def nall(eff): return [(k, e.get('op'), str(e.get('case_source', ''))[:14]) for k, ent in w.entities.items() for e in ent.ledger if e['effect'] == eff]
    for eff in ('levirate_owed', 'waits_for_the_levir', 'amalek_to_be_blotted', 'amalek_weakened', 'interest_barred', 'pledge_returned_by_sunset', 'wage_due_by_morning', 'left_for_the_poor', 'mixture_barred', 'justice_pursuit_commanded', 'judgment_wresting_barred', 'person_respecting_barred', 'stranger_barred', 'forgetting_barred', 'name_erasure_barred', 'isolated_outside_camp', 'stricken_with_leprosy', 'canaanite_wife_barred', 'wives_multiplying_barred', 'vow_bound', 'vow_confirmed', 'finder_a_slave_ruled', 'seed_given', 'hand_opening_commanded', 'hand_shutting_barred', 'cry_heard', 'bears_sin', 'withheld_from_sin', 'house_abomination_barred', 'abomination_eating_barred', 'holy_things_in_the_gates_barred', 'passing_through_fire_barred', 'blessings_for_hearing', 'work_of_the_hand_blessed', 'profaned_seed', 'fined_by_assessment', 'gives_fixed_sum', 'forbidden_to_her_husband', 'intercourse_permitted', 'ketubah_forfeited', 'oath_imposed', 'sold_for_theft', 'restores', 'torn_flesh_to_dogs', 'exaction_barred', 'debt_release_owed', 'severance_gift_owed', 'wife_taken', 'widow_sent', 'garment_seized', 'garment_left', 'childless', 'loathed', 'cursing_barred', 'coveting_barred', 'majority_decides', 'name_given', 'name_profaned', 'released', 'goes_free', 'evil_speech_spoken', 'seasons_pledged', 'pledge_held', 'pledge_offered'):
        n = nall(eff); print(' W', eff, len(n), n[:5])
except Exception as ex:
    traceback.print_exc(); print(' THE SNAPSHOT FAILED:', repr(ex))
print('CALLEES DONE')
