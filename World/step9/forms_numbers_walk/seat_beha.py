#!/usr/bin/env python3
# THE NUMBERS WALK sitting 3 — BEHA'ALOTCHA (2026-09-10): SEAT the 34 claims of the four manifests into their draft units as WITNESS_READ
# operators (sitting 2's rhythm, seat_naso.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the
# cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the
# unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written;
# each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = '<repo-old>'
DATE = '2026-09-10'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_08_menorah_levites', 8, 1, 26, [('BH08A-01', 2, 'toward_the_face_of_the_lampstand', 'the_lamps_face_the_middle'), ('BH08A-02', 3, 'and_aaron_did_so', 'the_three_facet_paradigm_again'),
                                       ('BH08A-03', 4, 'beaten_work', 'the_lampstand_against_the_trumpets'), ('BH08A-04', 7, 'water_of_purification', 'the_levites_rite_on_the_translation_alone'),
                                       ('BH08A-05', 16, 'given_given', 'the_second_seats_delta'), ('BH08A-06', 19, 'the_children_of_israel_five_times', 'unto_me_is_forever_ten_seats'),
                                       ('BH08A-07', 24, 'from_twenty_five', 'the_age_a_three_setting_parameter_the_run_rewrites')]),
 ('num_10_trumpets_depart', 10, 1, 36, [('BH10A-01', 2, 'two_trumpets_of_silver', 'two_trumpets_three_spellings'), ('BH10A-02', 5, 'blow_a_teruah', 'tekiah_teruah_the_wail'),
                                        ('BH10A-03', 8, 'the_sons_of_aaron_shall_blow', 'tarfon_saw_and_forgot_not_for_the_generations'), ('BH10A-04', 9, 'war_in_your_land', 'oppression_gladness_kingship'),
                                        ('BH10A-05', 11, 'on_the_twentieth', 'the_tapes_next_forward_marker'), ('BH10A-06', 14, 'the_standard_of_judah', 'the_camps_order_four_spellings'),
                                        ('BH10A-07', 29, 'hobab_son_of_reuel', 'hobab_the_father_in_law_eyes_for_us'), ('BH10A-08', 33, 'a_journey_of_three_days', 'the_ark_spies_the_seven_clouds'),
                                        ('BH10A-09', 35, 'when_the_ark_journeyed', 'the_signs_eighty_five_letters'), ('BH10A-10', 35, 'your_haters', 'scriptures_euphemisms')]),
 ('num_11_complaint_quail', 11, 1, 35, [('BH11A-01', 1, 'the_murmurers', 'the_people_the_fire_sank_names_by_the_event'), ('BH11A-02', 4, 'the_rabble', 'the_mixed_multitude_the_five_foods'),
                                        ('BH11A-03', 6, 'only_to_the_manna', 'the_speaker_split'), ('BH11A-04', 8, 'the_moist_cake', 'the_manna_converted_two_tastes'),
                                        ('BH11A-05', 10, 'weeping_by_families', 'the_families_weep_why_have_you_dealt_ill'), ('BH11A-06', 16, 'seventy_men', 'unto_me_seventy_the_descents'),
                                        ('BH11A-07', 18, 'sanctify_yourselves_for_tomorrow', 'one_plague_two_timers'), ('BH11A-08', 25, 'did_not_continue', 'the_lots_did_not_cease'),
                                        ('BH11A-09', 31, 'the_quail', 'two_cubits_ten_homers_plene_defective')]),
 ('num_12_miriam', 12, 1, 16, [('BH12A-01', 1, 'and_miriam_spoke', 'miriam_first_the_beautiful_woman_distanced'), ('BH12A-02', 2, 'only_only_with_moses', 'humble_without_the_yod'),
                               ('BH12A-03', 4, 'suddenly', 'the_three_by_one_utterance_praise_to_the_face'), ('BH12A-04', 6, 'in_a_vision', 'mouth_to_mouth_the_likeness_beheld'),
                               ('BH12A-05', 9, 'anger_against_them', 'the_cloud_left_a_priest_not_his_kin'), ('BH12A-06', 13, 'god_heal_her', 'the_shortest_prayer_counted'),
                               ('BH12A-07', 14, 'if_her_father_had_spat', 'dayo'), ('BH12A-08', 15, 'the_people_did_not_journey', 'measure_for_measure_the_quarantine_verb')]),
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
    sifrei = {'num_08_menorah_levites': 'the Sifrei on Numbers piskaot 59-63 found BY POSITION (59 headless, on 8:2; 62 headed "3:24", the row on 8:24 — CREDITED to num_04_kehat\'s ledger; no row on 8:5-23 — computed)',
              'num_10_trumpets_depart': 'the Sifrei on Numbers piskaot 72-84 found BY POSITION (80 headed "10:30", the row on 10:31 — placed by its neighbors and its opening words, RESEARCH_LOG.md)',
              'num_11_complaint_quail': 'the Sifrei on Numbers piskaot 85-98 found BY POSITION, every row at the shelf\'s row grain',
              'num_12_miriam': 'the Sifrei on Numbers piskaot 99-106 found BY POSITION (102 headed "Ibid. 4", the row on 12:4)'}[uid]
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 3, Beha'alotcha"
    comment: >
      The walk's third reading, at the parashah grain (Beha'alotcha 8:1-12:16
      less the frozen chapter 9, four ledgers per block): Onkelos Numbers
      {ch}:{lo}-{hi} whole and fresh; {sifrei}. Ledger {uid}_{DATE}.md,
      coverage computed by script, the ink facts computed from the Tanakh DB
      and the snapshot store (every fact an assert), every number by the
      engine's own numeral parser (measured again on this portion), every
      quotation cut by consonants, every narrative verb glossed by the
      store's own words.gloss. Seated as claims {ids[0]}..{ids[-1][-2:]}:
      {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the date 10:11 as the forward marker, the month and the
      seven days as timers, the parser's dual-noun and construct gaps)
      follows in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 34, total
print(f'BEHA\'ALOTCHA: {total} operators seated across {len(UNITS)} units')
