#!/usr/bin/env python3
# THE NUMBERS WALK sitting 2 — NASO (2026-09-09): SEAT the 52 claims of the seven manifests into their draft units as WITNESS_READ
# operators (sitting 1's rhythm, seat_bamidbar.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose,
# the cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM
# (the unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is
# written; each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = '<repo-old>'
DATE = '2026-09-09'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_04_gershon_merari', 4, 21, 49, [('NS04A-01', 34, 'the_princes_counted_with_moses', 'the_four_work_counts_and_their_sum'), ('NS04A-02', 28, 'in_the_hand_of_ithamar', 'the_two_sons_portfolios'),
                                      ('NS04A-03', 37, 'by_the_mouth_of_the_lord', 'the_closing_formulas_one_variant'), ('NS04A-04', 47, 'the_service_of_service', 'the_service_of_service'),
                                      ('NS04A-05', 46, 'the_princes_of_israel', 'the_princes_join_the_counters')]),
 ('num_05_camp_pure_theft', 5, 1, 10, [('NS05A-01', 2, 'send_out_of_the_camp', 'three_camp_words_three_camps'), ('NS05A-02', 3, 'they_shall_not_defile_their_camps', 'the_warning_for_the_punishment'),
                                      ('NS05A-03', 3, 'in_whose_midst_i_dwell', 'my_shekhinah_in_their_midst'), ('NS05A-04', 6, 'to_commit_a_trespass', 'trespass_is_lying_by_its_points'),
                                      ('NS05A-05', 8, 'no_redeemer', 'the_rule_of_repetition_the_proselytes_theft'), ('NS05A-06', 7, 'its_fifth', 'the_fifths_base_disputed'),
                                      ('NS05A-07', 9, 'every_heave_offering', 'the_tithe_inserted_the_first_fruits_the_thirty_days')]),
 ('num_05_sotah', 5, 11, 31, [('NS05B-01', 12, 'a_man_a_man', 'the_sections_purpose_doubt_after_warning'), ('NS05B-02', 13, 'and_a_man_lie_with_her', 'the_six_conditions_the_minimum_time'),
                             ('NS05B-03', 15, 'a_reminder_of_iniquity', 'merit_suspends_the_middots_case_law'), ('NS05B-04', 15, 'a_tenth_of_the_ephah', 'the_ephah_converted_the_laver_named'),
                             ('NS05B-05', 16, 'the_priest_shall_bring_her_near', 'stood_alone_the_hair_the_oath_in_any_language'), ('NS05B-06', 21, 'the_oath_of_the_curse', 'oath_is_curse_amen_amen_the_rolled_oath'),
                             ('NS05B-07', 23, 'and_erase', 'the_scroll_erased'), ('NS05B-08', 24, 'make_the_woman_drink', 'the_order_and_the_three_requirements'),
                             ('NS05B-09', 22, 'to_swell_belly', 'thigh_first_belly_first_the_limb_where_the_sin_began'), ('NS05B-10', 28, 'sown_with_seed', 'who_defiled_her_sown_with_seed'),
                             ('NS05B-11', 29, 'this_is_the_law_of_jealousies', 'this_is_the_law_obligatory_the_clean_husband')]),
 ('num_06_nazir', 6, 1, 21, [('NS06A-01', 2, 'if_he_declares_to_vow', 'the_thirty_days_the_default'), ('NS06A-02', 3, 'from_wine_and_strong_drink', 'wine_three_readings_the_taste_as_the_substance'),
                            ('NS06A-03', 4, 'from_kernels_to_skin', 'general_particular_combination'), ('NS06A-04', 5, 'a_razor_shall_not_pass', 'the_locks_by_the_identity_the_failed_a_fortiori'),
                            ('NS06A-05', 6, 'upon_a_dead_soul', 'not_for_kin_yes_for_the_unburied_the_crown'), ('NS06A-06', 9, 'if_one_die_on_him', 'the_defiled_nazirite_the_first_days_fall'),
                            ('NS06A-07', 12, 'the_first_days_shall_fall', 'the_argument_goes_round_the_extra_nazirite_decides'), ('NS06A-08', 13, 'he_shall_bring_himself', 'he_brings_himself_the_pot_where_he_cooks'),
                            ('NS06A-09', 15, 'a_basket_of_unleavened_bread', 'the_eleventh_rule_stated_libations_for_the_vowed'), ('NS06A-10', 21, 'what_his_hand_attains', 'the_third_this_is_the_law_the_leper_nazirite')]),
 ('num_06_priest_blessing', 6, 22, 27, [('NS06B-01', 24, 'the_lord_bless_you', 'the_blessings_form_counted'), ('NS06B-02', 23, 'thus_shall_you_bless', 'the_speech_to_the_priests_the_blessings_form'),
                                       ('NS06B-03', 25, 'make_his_face_shine', 'one_word_two_renderings'), ('NS06B-04', 26, 'lift_his_face', 'lifts_his_face_lifts_no_face_the_sealed_decree'),
                                       ('NS06B-05', 27, 'place_my_name', 'the_explicit_name_in_the_temple_the_blessing_of_my_name')]),
 ('num_07_carts_offerings_a', 7, 1, 47, [('NS07A-01', 1, 'the_day_moses_finished', 'the_day_runs_backward_again'), ('NS07A-02', 2, 'they_who_stood_over_the_counted', 'covered_wagons_a_wagon_for_two'),
                                        ('NS07A-03', 6, 'moses_took_the_wagons', 'on_the_shoulder_davids_error'), ('NS07A-04', 10, 'the_dedication_of_the_altar', 'the_order_by_the_journeying_each_on_his_day'),
                                        ('NS07A-05', 12, 'on_the_first_day_nahshon', 'the_twelve_offerings_are_one_text'), ('NS07A-06', 13, 'one_silver_dish', 'the_accents_parse_the_number_the_total_proves_it'),
                                        ('NS07A-07', 15, 'one_bull_one_ram_one_lamb', 'the_princes_four_exceptions')]),
 ('num_07_offerings_b_total', 7, 48, 89, [('NS07B-01', 84, 'this_is_the_dedication', 'the_totals_by_the_taught_parser'), ('NS07B-02', 88, 'after_it_was_anointed', 'on_the_day_and_after_the_same_day'),
                                         ('NS07B-03', 85, 'each_dish_a_hundred_and_thirty', 'temple_vessels_weights_each_credited_with_all'), ('NS07B-04', 89, 'the_voice_speaking_itself', 'the_voice_speaking_itself_by_the_points'),
                                         ('NS07B-05', 89, 'from_between_the_two_cherubim', 'two_verses_reconciled_by_a_third_thirteen_exclusions'), ('NS07B-06', 89, 'he_heard_the_voice', 'the_voice_great_not_low')]),
]
TITLES = {}
for uid, _, _, _, seats in UNITS:
    for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8')):
        TITLES[c['id']] = c['claim_en'].split('. ')[0].rstrip('.')

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def seat(uid, ch, lo, hi, seats):
    unit = f'{ROOT}/logic/units/{uid}.yaml'
    led = open(f'{ROOT}/logic/oral_triage/{uid}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
    ci = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
    claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{uid}_claims.json', encoding='utf-8'))}
    assert len(claims) == len(seats) and set(claims) == {s[0] for s in seats}, (uid, sorted(claims), seats)
    txt = open(unit, encoding='utf-8').read()
    assert 'operators:' not in txt, 'the draft already carries operators'
    by_step = {}
    for cid, step, anchor, name in seats:
        assert lo <= step <= hi and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
        cites = claims[cid]['source'].split('; ')
        for c in cites: assert c in ci, (cid, c)
        prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
        by_step.setdefault(step, []).append((anchor, name, cites, prose))
    for step, ops in by_step.items():
        sid = f'  - id: STEP_Nm_{ch}_{step}\n'
        i = txt.index(sid)
        j = txt.index('    comment: >\n', i)
        nxt = txt.find(f'\n  - id: STEP_Nm_{ch}_', i + 1)
        assert nxt == -1 or j < nxt, step
        block = '    operators:\n'
        for anchor, name, cites, prose in ops:
            block += ('      - op: WITNESS_READ\n'
                      f'        expr_en: "WITNESS-READ({anchor}, {name})"\n'
                      '        en: >\n' + wrap(prose) + '\n'
                      '        cites: [' + ', '.join(q(c) for c in cites) + ']\n'
                      '        confidence: witnessed\n')
        txt = txt[:j] + block + txt[j:]
    k = txt.index('\nboot_steps:\n')
    txt = txt[:k] + STEP_E(uid, ch, lo, hi, [s[0] for s in seats]) + txt[k:]
    a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
    scen = '\nscenarios:\n'
    firsts = list(range(lo, min(lo + 6, hi + 1)))
    for n, v in enumerate(firsts, 1):
        scen += f'  - id: S{n}\n    title_en: "after STEP_Nm_{ch}_{v} — Num {ch}:{v}"\n    expect_en: "no test, no name."\n'
    scen += f'  - id: S_last\n    title_en: "after STEP_Nm_{ch}_{hi} — Num {ch}:{hi}"\n    expect_en: "no test, no name."\n'
    txt = txt[:a] + scen + txt[b:]
    open(unit, 'w', encoding='utf-8').write(txt)
    d = yaml.safe_load(open(unit, encoding='utf-8'))
    ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
    assert len(ops) == len(seats) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
    assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == hi - lo + 1
    assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
    print(f'{uid}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
    return len(ops)

def STEP_E(uid, ch, lo, hi, ids):
    sifrei = ('the Sifrei on Numbers has NO piska on 4:21-49 by position (it opens at 5:1 — computed)' if uid == 'num_04_gershon_merari'
              else 'the Sifrei on Numbers piskaot found BY POSITION, every row at the shelf\'s row grain (two heads mistyped in the export — 19 for 5:28, 34 for 6:15 — placed by position, RESEARCH_LOG.md)')
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 2, Naso"
    comment: >
      The walk's second reading, at the parashah grain (Naso 4:21-7:89 in
      one pass, seven ledgers per block): Onkelos Numbers {ch}:{lo}-{hi} whole
      and fresh; {sifrei}. Ledger {uid}_{DATE}.md, coverage computed
      by script, the ink facts computed from the Tanakh DB and the snapshot
      store, every number by the engine's own numeral parser (taught the
      census at sitting 1b), every quotation cut by consonants. Seated as
      claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the four parser gaps measured here, the twelve days as
      timers, the 7:1 retrograde marker) follows in its own sitting
      (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 51, total   # the manifests' own count (the hand had said 52)
print(f'NASO: {total} operators seated across {len(UNITS)} units')
