import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (2026-09-26): THE CALLEES' FACTS, second pass — the q-style cells (the dispatch keys read from their sources by ch22_callees_keys.py, the
# asks typed from that print), every value printed whole by repr; the tape's kin lines by case_source prefix for the Exodus, Leviticus and Numbers laws. RUN FROM THE REPO ROOT.
import os, sys, io, re, contextlib, subprocess, inspect
ROOT = _ROOT; sys.path.insert(0, ROOT + '/World/step9')
def load(name):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__('cold_run_' + name)
M = {}
def show(label, fn):
    try:
        v = fn(); print('FACT %s = %r' % (label, v))
    except Exception as ex:
        print('FAIL %s: %s: %s' % (label, type(ex).__name__, str(ex)[:200]))
def q(n, name, keys, **kw):
    if n not in M: M[n] = load(n)
    fn = getattr(M[n], name)
    for k in keys:
        show('%s.%s(%s)' % (n, name, k), lambda k=k: (lambda c: (c.get('v'), c.get('p'), c.get('fx'), str(c.get('why', ''))[:260]) if isinstance(c, dict) and 'v' in c else (str(c)[:500] if not isinstance(c, dict) else {kk: str(t)[:200] for kk, t in c.items()}))(fn(k, **kw) if kw else fn(k)))
q('ordinances', 'courts', ['enemy_ox', 'who_is_enemy', 'enemy_three_days', 'straying', 'return_doubled', 'sign_and_claimant', 'deceiver', 'announce_duration', 'common_case_animals', 'lying_under', 'unload_doubled', 'with_him', 'measure', 'unload_load', 'ris', 'father_says_no', 'grudge', 'needy_in_his_cause', 'keep_far', 'no_retrial_acquitted', 'bribe', 'stranger_repeat', 'one_vs_two', 'witness_of_violence'])
q('ordinances', 'loan', ['im_obligation', 'priority_ladder', 'creditor_manner', 'bite_noun', 'interest_spec', 'foreigner', 'five_prohibitions', 'who_transgresses', 'pledge_sunset', 'day_night_garments', 'court_only', 'widow_not_pledged', 'covering_tokens', 'gracious'])
q('ordinances', 'stranger', ['two_verbs', 'words_vs_money', 'you_were_strangers', 'ger_seats', 'widow_orphan_scope', 'one_affliction', 'cry_doubled', 'measure_for_measure'])
q('ordinances', 'gifts', ['delay_is_reorder', 'order_sheet', 'fullness_outflow'])
q('holiness', 'gifts', ['kinds', 'recipients', 'measure', 'gentile_then_converted', 'moment', 'leket', 'heap', 'doubt', 'peret', 'olelet', 'olelet_edges', 'reaped_by', 'for_named_poor', 'renunciation', 'trees', 'three_times', 'no_sickles', 'seizing'])
q('holiness', 'wage', ['oppression_class', 'hire_kinds', 'first_morning', 'claimed', 'assigned', 'clock', 'day', 'night', 'hour', 'resident_alien', 'who_swears', 'in_kind'])
q('holiness', 'conduct', ['lender_at_interest', 'no_favor', 'equal_treatment', 'bribe', 'hate', 'five_effects', 'scale_of_merit', 'great_rule'])
q('holiness_b', 'mixtures', ['three_bans', 'noun_thrice', 'vineyard', 'seeds', 'garments', 'beasts', 'plowing', 'materials', 'shaatnez_defined', 'wearing_vs_covering', 'wear', 'cover', 'spread_beneath', 'admixture', 'class_table', 'mule_kind', 'dog', 'wild_ox', 'three_institutions', 'majority', 'temporary'])
q('holiness_b', 'maidservant', ['lashing_procedure', 'death_withheld', 'lashes', 'count', 'sex_punished', 'deliberate', 'minor'])
show('yovel.interest()', lambda: {k: (v.get('v'), v.get('p'), v.get('fx'), str(v.get('why', ''))[:200]) for k, v in load('yovel').interest().items()})
q('yovel', 'interest_scope', ['brother', 'foreigner']); q('yovel', 'support_duty', ['faltering', 'supported_four_or_five_times', 'your_life_against_his'])
q('sanctions', 'grade', ['second_degree', 'fathers_wife', 'brothers_wife', 'married_woman', 'menstruant', 'sister'])
q('sanctions', 'levirate', ['fifteen', 'six', 'count', 'rival_chain', 'release_timing', 'not_in_world', 'not_in_world_maamar', 'houses'])
q('sanctions', 'cowives', ['ervah_sister_free', 'zikah_sisters', 'stranger_cases', 'one_hour', 'maamar_houses', 'two_bonds', 'divorced_before'])
q('sanctions', 'unions_misc', ['brother_wife_window', 'father_clause', 'void_betrothal', 'maidservant_or_gentile_daughter', 'niddah', 'no_inference'])
q('sanctions', 'frame', ['lashes_discharge_karet', 'karet_persons', 'court_warned', 'disqualified', 'majority_threshold', 'live_by_them', 'sit_and_abstain'])
q('sanctions', 'census', ['stoned', 'burned', 'strangled', 'lashes', 'karet_count'])
q('sanctions', 'curser', ['mode', 'after_death', 'warning_source'])
q('priesthood', 'family', ['zonah', 'chalalah', 'chalutzah', 'husband', 'unfit', 'raped_or_seduced', 'sanctify_him', 'husband_fork'])
q('priesthood', 'acceptable', ['vows', 'freewill_or_vow', 'castration', 'sarua_kalut', 'whole_male', 'no_shekels', 'shekels'])
q('priesthood', 'holy_food', ['forbidden_union', 'daughter_to_stranger', 'stranger', 'seed_emitter', 'sunset', 'toshav_sachir', 'she_feeds'])
q('family', 'levirate', ['the_command', 'seed_vs_name', 'name_is_inheritance', 'name_on_inheritance_ruth', 'no_son_clause', 'levirate_alignment', 'sinai_seat_by_call', 'not_in_world_by_call', 'fifteen_by_call', 'kin_scope_narrowed', 'mamzer_definition', 'widow_waiting', 'no_release_form', 'onan_refused', 'slain_by_heaven', 'firstborn_er', 'kedesha', 'harlot_by_call', 'three_months_hint', 'sentence_burning', 'twins_two_spellings', 'firstborn_by_the_head', 'order_of_sons', 'father_takes_for_er'])
print('==== THE TAPE\'S KIN LINES BY CASE_SOURCE PREFIX (the laws of Exodus 20-23, Leviticus 13-25, Numbers 5, 15, 30) ====')
seq = open(ROOT + '/World/step9/cold_run_sequence.py', encoding='utf-8').read()
subs = re.findall(r"^\s+w\.submit\(\{'kind': '(\w+)'.*?'case_source': (?:'([^']*)'|\"([^\"]*)\")", seq, re.M)
for pref in ('Exod 20:', 'Exod 21:', 'Exod 22:', 'Exod 23:', 'Lev 13:', 'Lev 14:', 'Lev 15:', 'Lev 18:', 'Lev 19:', 'Lev 20:', 'Lev 21:', 'Lev 22:', 'Lev 24:', 'Lev 25:', 'Num 15:', 'Num 30:', 'Num 5:', 'Deut 5:', 'Deut 15:', 'Deut 16:', 'Deut 10:', 'Deut 12:', 'Deut 14:'):
    hits = [(k, (a or b)[:30]) for k, a, b in subs if (a or b).startswith(pref)]
    print(' TAPE %-9s %d %s' % (pref, len(hits), hits[:14]))
print('CALLEES2 DONE')
