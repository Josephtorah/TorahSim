import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 1 — BAMIDBAR (2026-09-09): SEAT the 31 claims of the nine manifests into their draft units as
# WITNESS_READ operators (THE TENT sitting 4's rhythm, seat_num27_36.py: one operator per claim at its FIRST verse's step, the
# [claim ID] marker in the prose, the cites the ledgers' own names), append derivation_log step E, and REWRITE THE TREE-DERIVED
# SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the ritual. Every cite is checked against the
# ledger's CITE INDEX before a byte is written; each yaml is re-loaded after. The prose is the manifest's own claim_en, so the
# operator and the claim cannot drift apart.
import json, re, yaml
ROOT = _ROOT
DATE = '2026-09-09'
UNITS = [  # (uid, chapter, lo, hi, [(claim id, step verse, anchor, name)])
 ('num_01_census_command', 1, 1, 19, [('NM01A-01', 1, 'beechad_lachodesh_hasheni', 'the_date_stamp_and_the_retrograde'), ('NM01A-02', 2, 'seu_et_rosh', 'the_count_of_names_the_threshold'),
                                     ('NM01A-03', 5, 'veeleh_shemot_haanashim', 'the_princes_the_three_orders_the_ketiv_qere'), ('NM01A-04', 17, 'vayikach_moshe_veaharon', 'the_run_designated_pedigreed_the_same_day')]),
 ('num_01_tribe_counts', 1, 20, 46, [('NM01B-01', 20, 'vayihyu_venei_reuven', 'the_twelve_counts_computed'), ('NM01B-02', 44, 'eleh_hapekudim', 'the_total_is_the_sum_on_three_seats'),
                                    ('NM01B-03', 21, 'pekudeihem_lemateh_reuven', 'the_census_number_grammar_and_the_parser')]),
 ('num_01_levites_exempt', 1, 47, 54, [('NM01C-01', 47, 'vehaleviyim_lo_hotpakdu', 'the_exclusion'), ('NM01C-02', 50, 'hafked_et_haleviyim', 'the_appointment_and_the_stranger'),
                                      ('NM01C-03', 52, 'ish_al_diglo', 'the_banner_the_wrath_shield_the_run')]),
 ('num_02_camp_east_south', 2, 1, 16, [('NM02A-01', 2, 'ish_al_diglo_veotot', 'the_banner_the_signs_the_distance'), ('NM02A-02', 3, 'kedmah_mizrachah_yehudah', 'east_judah_first'),
                                      ('NM02A-03', 10, 'degel_machaneh_reuven_teimanah', 'south_reuben_second_reuel')]),
 ('num_02_camp_west_north', 2, 17, 34, [('NM02B-01', 17, 'venasa_ohel_moed', 'the_march_order_is_the_camp_order'), ('NM02B-02', 18, 'degel_machaneh_efrayim_yamah', 'west_ephraim_third'),
                                       ('NM02B-03', 25, 'degel_machaneh_dan_tzafonah', 'north_dan_last'), ('NM02B-04', 32, 'eleh_pekudei_venei_yisrael', 'the_totals_third_seat_one_verse_two_runs')]),
 ('num_03_aaron_levi_replace', 3, 1, 13, [('NM03A-01', 1, 'veeleh_toledot_aharon_umoshe', 'the_genesis_heading_on_aaron_and_moses'), ('NM03A-02', 3, 'hakohanim_hameshuchim', 'the_filled_hand_the_sonlessness_upon_the_face'),
                                         ('NM03A-03', 6, 'hakrev_et_mateh_levi', 'the_tribe_brought_near_two_charges_given_given'), ('NM03A-04', 12, 'lakachti_et_haleviyim', 'the_substitution_as_a_reference_its_ground_dated')]),
 ('num_03_levite_clans_count', 3, 14, 39, [('NM03B-01', 14, 'bemidbar_sinai_lemor', 'the_placed_frame_the_month_by_the_mouth'), ('NM03B-02', 18, 'venei_gershon_livni_veshimi', 'gershon_west_the_soft_charge'),
                                          ('NM03B-03', 27, 'velikhat_mishpachat_amrami', 'kohath_south_the_holy_charge_the_amarkal_the_three_hundred'), ('NM03B-04', 33, 'limrari_mishpachat_hamachli', 'merari_north_east_the_leaders_the_total_as_written')]),
 ('num_03_firstborn_redeem', 3, 40, 51, [('NM03C-01', 40, 'pekod_kol_bekhor_zakhar', 'the_said_frame_the_firstborn_counted'), ('NM03C-02', 44, 'kach_et_haleviyim_tachat', 'the_excess_five_five_the_shekel_and_its_gerah'),
                                        ('NM03C-03', 49, 'vayikach_moshe_et_kesef', 'the_money_and_a_thousand_the_double_formula')]),
 ('num_04_kehat', 4, 1, 20, [('NM04A-01', 2, 'naso_et_rosh_benei_kehat', 'the_houses_head_the_works_ages_the_sifreis_row'), ('NM04A-02', 5, 'uva_aharon_uvanav_binsoa', 'the_priests_cover_the_veil_on_the_ark'),
                            ('NM04A-03', 15, 'vekhilah_aharon_uvanav', 'the_order_is_the_law_eleazars_charge'), ('NM04A-04', 18, 'al_takhritu', 'cut_not_off_the_remedy_the_swallowing')]),
]
TITLES = {'NM01A-01': 'THE DATE STAMP AND THE RETROGRADE', 'NM01A-02': 'THE COUNT OF NAMES; THE THRESHOLD; ONE MAN PER TRIBE', 'NM01A-03': 'THE PRINCES, THE THREE ORDERS, THE KETIV-QERE', 'NM01A-04': 'THE RUN: DESIGNATED, PEDIGREED, THE SAME DAY',
          'NM01B-01': 'THE TWELVE COUNTS, COMPUTED', 'NM01B-02': 'THE TOTAL IS THE SUM, ON THREE SEATS', 'NM01B-03': "THE CENSUS'S NUMBER GRAMMAR AND THE ENGINE'S PARSER",
          'NM01C-01': 'THE EXCLUSION', 'NM01C-02': 'THE APPOINTMENT AND THE STRANGER', 'NM01C-03': 'THE BANNER, THE WRATH-SHIELD, THE RUN',
          'NM02A-01': 'THE BANNER, THE SIGNS, THE DISTANCE', 'NM02A-02': 'EAST: JUDAH, FIRST', 'NM02A-03': 'SOUTH: REUBEN, SECOND; REUEL',
          'NM02B-01': 'THE MARCH ORDER IS THE CAMP ORDER', 'NM02B-02': 'WEST: EPHRAIM, THIRD', 'NM02B-03': 'NORTH: DAN, LAST', 'NM02B-04': "THE TOTAL'S THIRD SEAT; ONE VERSE, TWO RUNS",
          'NM03A-01': 'THE GENESIS HEADING ON AARON AND MOSES', 'NM03A-02': 'THE FILLED HAND, THE SONLESSNESS, UPON THE FACE', 'NM03A-03': 'THE TRIBE BROUGHT NEAR; GIVEN, GIVEN; THE PRIESTHOOD KEPT', 'NM03A-04': 'THE SUBSTITUTION AS A REFERENCE; ITS GROUND DATED',
          'NM03B-01': 'THE PLACED FRAME; THE MONTH; BY THE MOUTH OF THE LORD', 'NM03B-02': 'GERSHON: WEST, THE SOFT CHARGE', 'NM03B-03': 'KOHATH: SOUTH, THE HOLY CHARGE; THE AMARKAL; THE THREE HUNDRED', 'NM03B-04': 'MERARI: NORTH; EAST THE LEADERS; THE TOTAL AS WRITTEN',
          'NM03C-01': 'THE SAID-FRAME; THE FIRSTBORN COUNTED', 'NM03C-02': 'THE EXCESS; FIVE, FIVE; THE SHEKEL AND ITS GERAH', 'NM03C-03': "THE MONEY; 'AND A THOUSAND'; THE DOUBLE FORMULA",
          'NM04A-01': "THE HOUSE'S HEAD; THE WORK'S AGES — THE SIFREI'S ROW; THE HOLY OF HOLIES", 'NM04A-02': 'THE PRIESTS COVER; BLUE OUTSIDE ONLY THE ARK; THE ALTAR ASHED', 'NM04A-03': "THE ORDER IS THE LAW; ELEAZAR'S CHARGE", 'NM04A-04': 'CUT NOT OFF; THE REMEDY; NOT TO SEE THE SWALLOWING'}

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
    return f'''
  - step: E
    name_en: "Numbers {ch}:{lo}-{hi} derivation {DATE} — THE NUMBERS WALK sitting 1, Bamidbar"
    comment: >
      The walk's first reading, at the parashah grain (Bamidbar 1:1-4:20
      in one pass, nine ledgers per block): Onkelos Numbers {ch}:{lo}-{hi}
      whole and fresh; the Sifrei on Numbers has NO piska on the portion
      by position (it opens at 5:1 — computed; its export's piska 62,
      headed 3:24, is the row on 8:24 and is read at num_04_kehat where
      4:3's thirty is its subject). Ledger {uid}_{DATE}.md,
      coverage computed by script, the ink facts computed from the Tanakh
      DB and the numbers of the census computed from the ink's own
      numerals. Seated as claims {ids[0]}..{ids[-1][-2:]}: {', '.join(TITLES[i].lower() for i in ids)}.
      The compile (the census's arithmetic, the engine's numeral parser
      taught the thousands) and the tape (Num 1:1's forward marker) follow
      in their own sitting (World/step9/NUMBERS_WALK.md).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
total = 0
for uid, ch, lo, hi, seats in UNITS: total += seat(uid, ch, lo, hi, seats)
assert total == 32, total   # the manifests' own count (the hand said 31)
print(f'BAMIDBAR: {total} operators seated across {len(UNITS)} units')
