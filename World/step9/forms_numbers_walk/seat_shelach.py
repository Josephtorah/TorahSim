#!/usr/bin/env python3
# THE NUMBERS WALK sitting 4 — SHELACH (2026-09-10): SEAT the 30 claims of the three manifests into their draft units as WITNESS_READ
# operators (sitting 3's rhythm, seat_beha.py: one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the
# cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the
# unit's first six verses + its last) before the ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written;
# each yaml is re-loaded after. The prose is the manifest's own claim_en, so the operator and the claim cannot drift apart.
import json, re, yaml
ROOT = '<repo-old>'
DATE = '2026-09-10'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_13_spies_sent', 13, 1, 33, [('SH13A-01', 2, 'send_for_yourself', 'the_spy_verb_is_the_arks_the_shelf_silent'), ('SH13A-02', 4, 'these_are_their_names', 'a_fourth_order_josephs_name_over_manasseh'),
                                   ('SH13A-03', 16, 'hoshea_called_joshua', 'the_new_name_before_the_old_name_after'), ('SH13A-04', 17, 'go_up_into_the_south', 'the_questionnaire_counted_the_season'),
                                   ('SH13A-05', 21, 'from_zin_to_hamath', 'they_went_up_he_came_to_hebron'), ('SH13A-06', 23, 'the_cluster_on_a_pole', 'the_dual_read_forty_days'),
                                   ('SH13A-07', 26, 'to_kadesh', 'rekem_milk_and_honey_the_maps_three_placements'), ('SH13A-08', 30, 'caleb_hushed', 'two_doubled_infinitives_than_we_than_he'),
                                   ('SH13A-09', 32, 'the_slander_of_the_land', 'josephs_word_the_nephilim_plene_and_defective')]),
 ('num_14_rejection', 14, 1, 45, [('SH14A-01', 1, 'that_night', 'the_ninth_of_av_the_murmur_root'), ('SH14A-02', 5, 'on_their_faces', 'our_bread_delivered_the_glory_at_six_seats'),
                                  ('SH14A-03', 11, 'how_long', 'the_scorn_verb_the_offers_second_seat'), ('SH14A-04', 13, 'egypt_will_hear', 'eye_to_eye_the_shekhinah'),
                                  ('SH14A-05', 18, 'slow_to_anger', 'the_attributes_abridged_the_translation_restores'), ('SH14A-06', 21, 'as_i_live', 'ten_times_calebs_formula'),
                                  ('SH14A-07', 27, 'this_evil_congregation', 'the_ten_measure_for_measure_the_census'), ('SH14A-08', 31, 'your_little_ones', 'a_day_for_a_year_ezekiel_runs_it'),
                                  ('SH14A-09', 36, 'the_men_who_slandered', 'the_ten_in_the_plague'), ('SH14A-10', 40, 'they_rose_early', 'the_ark_stays_hormah_named_later')]),
 ('num_15_offerings_laws', 15, 1, 31, [('SH15A-01', 2, 'your_settlings', 'libations_after_settlement_or_against_and'), ('SH15A-02', 4, 'a_tenth_a_quarter', 'the_table_the_fraction_class'),
                                       ('SH15A-03', 8, 'a_young_bull', 'the_bull_departs_on_bowls_the_mixing_rule'), ('SH15A-04', 13, 'all_the_native_born', 'libations_donated_the_gentiles'),
                                       ('SH15A-05', 14, 'a_stranger_sojourns', 'the_proselyte_by_blood_one_torah'), ('SH15A-06', 18, 'upon_your_coming', 'the_varied_formula_read_as_law'),
                                       ('SH15A-07', 20, 'the_first_of_your_dough', 'challah_the_analogys_target'), ('SH15A-08', 22, 'if_you_err', 'idolatry_by_the_delta_without_the_aleph'),
                                       ('SH15A-09', 25, 'atone_for_all', 'the_tribe_table_the_high_priest_excluded'), ('SH15A-10', 27, 'one_soul', 'the_she_goat_of_the_first_year_keritot_on_its_verse'),
                                       ('SH15A-11', 30, 'with_a_high_hand', 'the_exodus_posture_the_doubled_infinitives_fork')]),
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
    sifrei = {'num_13_spies_sent': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_14_rejection': 'the Sifrei on Numbers has NO PISKA on this chapter (computed on every head of the export) — the chapter read on the translation alone',
              'num_15_offerings_laws': 'the Sifrei on Numbers piskaot 107-112 found BY POSITION (110 headed "15:15-17", the row on 15:17-21 — placed by its neighbors and its opening words, RESEARCH_LOG.md)'}[uid]
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 4, Shelach"
    comment: >
      The walk's fourth reading, at the parashah grain (Shelach 13:1-15:31;
      15:32-41 frozen at the tent and skipped; three ledgers per block):
      Onkelos Numbers {ch}:{lo}-{hi} whole and fresh; {sifrei}. Ledger
      {uid}_{DATE}.md, coverage computed by script, the ink facts computed
      from the Tanakh DB and the snapshot store (every fact an assert), every
      number by the engine's own numeral parser (measured again on this
      portion — the fraction a new class), every quotation cut by consonants,
      every narrative verb glossed by the store's own words.gloss. Seated as
      claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The compile (the forty-day and forty-year timers, the ninth of Av as
      the reading-placed marker, the libation table, the fraction class)
      follows in its own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 30, total
print(f'SHELACH: {total} operators seated across {len(UNITS)} units')
