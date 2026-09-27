import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN, 2026-09-24): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch19.py <uid>.
# Sitting 15's form (seat_ch17.py) over three units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-24'
UID = sys.argv[1]
SPEC = {
 'deu_19_miklat_witness': (19, 1, 21, [('DV19-01', 1, 'the_three_cities_separated', 'three_cities_separated_in_the_land_the_way_prepared_and_the_border_divided_in_three_three_more_if_the_border_is_enlarged'), ('DV19-02', 4, 'the_unwitting_killer_and_the_avenger', 'the_killer_without_hatred_from_yesterday_flees_and_lives_the_avenger_of_blood_pursues_the_hater_is_given_up_by_the_elders'), ('DV19-03', 14, 'the_landmark', 'you_shall_not_move_your_neighbors_landmark_which_the_first_ones_bounded'), ('DV19-04', 15, 'the_witnesses_and_the_plotting_witness', 'one_witness_stands_not_two_or_three_stand_the_judges_inquire_well_and_do_to_the_plotter_as_he_plotted_life_for_life_eye_for_eye')],
  'the three cities separated with the way prepared and the border divided in three, three more on the enlargement; the unwitting killer\'s flight and the avenger\'s pursuit, the hater given up by his city\'s elders; the landmark; one witness standing for nothing, two or three standing, and the plotting witness done to as he plotted'),
 'deu_20_war_rules': (20, 1, 20, [('DV20-01', 1, 'the_priests_speech_and_the_four_exemptions', 'fear_not_the_horse_and_chariot_the_priest_speaks_hear_israel_the_officers_send_home_the_new_house_the_vineyard_the_betrothed_and_the_fearful'), ('DV20-02', 10, 'the_call_for_peace_and_the_siege', 'call_the_city_to_peace_for_tribute_and_service_else_besiege_it_smite_the_males_and_take_the_women_children_and_spoil'), ('DV20-03', 16, 'the_seven_nations_banned', 'of_the_cities_of_these_peoples_let_no_breath_live_utterly_destroy_the_six_nations_as_the_lord_commanded_lest_they_teach_their_abominations'), ('DV20-04', 19, 'the_trees_of_the_siege', 'the_fruit_tree_not_cut_in_a_long_siege_for_the_tree_is_not_a_man_the_barren_tree_cut_for_the_siege_works_until_the_city_falls')],
  'the priest\'s speech and the officers\' four exemptions before the battle; the call for peace, the tribute and the siege\'s spoil; the seven nations banned as the LORD commanded; the trees of the siege'),
 'deu_21_eglah_family': (21, 1, 23, [('DV21-01', 1, 'the_broken_necked_heifer', 'the_slain_one_found_the_measuring_to_the_nearest_city_the_heifer_of_the_herd_broken_necked_in_the_rough_valley_the_priests_present_the_elders_wash_and_declare_and_the_blood_is_atoned'), ('DV21-02', 10, 'the_captive_woman', 'the_beautiful_captive_brought_home_shaved_and_weeping_a_month_then_a_wife_released_not_sold_if_unwanted'), ('DV21-03', 15, 'the_firstborns_double', 'the_firstborn_of_the_hated_wife_recognized_for_double_of_all_the_father_cannot_prefer_the_loved_wifes_son'), ('DV21-04', 18, 'the_stubborn_and_rebellious_son', 'the_son_who_heeds_neither_parent_chastised_then_brought_to_the_elders_a_glutton_and_a_drunkard_stoned_by_his_city_the_evil_purged'), ('DV21-05', 22, 'the_hanged_buried_the_same_day', 'the_executed_man_hanged_on_a_tree_not_left_overnight_buried_that_day_for_a_hanged_one_is_a_curse_of_god')],
  'the broken-necked heifer for the slain one whose killer is unknown, the measuring, the rite in the valley and the elders\' declaration; the captive woman\'s month and her release; the firstborn\'s double for the hated wife\'s son; the stubborn and rebellious son stoned; the hanged man buried the same day'),
}
CH, LO, HI, SEATS, WHAT = SPEC[UID]
claims = {c['id']: c for c in json.load(open(f'{ROOT}/logic/oral_audit/manifests/{UID}_claims.json', encoding='utf-8'))}
TITLES = {cid: c['claim_en'].split('. ')[0].rstrip('.') for cid, c in claims.items()}

def wrap(prose, indent=10):
    lines, cur = [], ''
    for w in prose.split(' '):
        if len(cur) + len(w) + 1 > 78 - indent and cur: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w) if cur else w
    lines.append(cur)
    return '\n'.join(' ' * indent + l for l in lines)
def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def STEP_E(ids):
    return f'''
  - step: E
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 16, chapters 19-21, LEAN"
    comment: >
      The book's sixteenth reading, at the chapter's grain (chapter {CH} as one
      draft — {WHAT}; the portion edge inside chapter 21 at 21:9|21:10 —
      Shoftim ends at the heifer, Ki Teitzei opens at the captive; the
      chapter the unit; three chapters read at one sitting in two runs
      under the cost rules' cap, three units, one ledger), THE FIFTH
      SITTING OF THE LEAN PASS (ruled 2026-09-23): every row whole under
      the whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh
      (the export's rows the DB's — the identity, asserted); THE SIFREI ON
      DEUTERONOMY ON THE THREE CHAPTERS — forty-three piskaot 179-221 (ten
      heads in chapter 19 with two headless piskaot inside it read whole
      from the export, fourteen in chapter 20 with a variant piska out of
      verse order, seventeen in chapter 21; 190 running past its chapter's
      end into 20:1): two hundred and sixty rows read whole in both files
      (nine prior reads of eight rows found in the earlier ledgers by
      computation and reread whole — the cutting off of the nations, the
      false witness and the inquiry, the two witnesses, the priests'
      standing, Sihon's peace, the full houses), eleven rows outside the
      spine citing the chapters read whole (five reread whole from chapters
      12, 15 and 17-18; six fresh — the captive, the rebellious son's
      analogies, the pitiless eye, the Song's "drop as rain" twice, the
      priests' blessing), the kin (Numbers 10, 19, 21, 25, 31, 35; Leviticus
      20, 24; Deuteronomy 4, 17) credited by name from the earlier ledgers.
      Ledger deu_19_21_shoftim_ki_teitzei_{DATE}.md, coverage computed by
      script (335 sources over the three chapters), the ink facts computed
      from the Tanakh DB and the snapshot store (56 asserts: 4 fell on the
      first typed pass — the English's prefix before a merged number, two
      hand-summed totals dropped as recitals, a slice off by one; 1 on the
      second; 0 on the third), the engine's numeral parser measured on
      every verse (ten number verses, none in chapter 20; no ordinal), the
      store the DB at every verse but 21:7's ketiv-qere, every quotation
      cut by consonants (zero misses on 335 rows over the two runs). Seated
      as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (16b); the
      full process (the docket whole, the full records) OWED to these
      chapters under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_19_21_shoftim_ki_teitzei_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
ci = set(re.findall(r'^(Onkelos Deut \d+:\d+|Sifrei Devarim \d+:\d+)$', led, re.M))
assert len(claims) == len(SEATS) and set(claims) == {s[0] for s in SEATS}, (sorted(claims), SEATS)
txt = open(unit, encoding='utf-8').read()
assert 'operators:' not in txt, 'the draft already carries operators'
by_step = {}
for cid, step, anchor, name in SEATS:
    assert LO <= step <= HI and re.fullmatch(r'[\w-]+', anchor) and re.fullmatch(r'[\w-]+', name), (cid, step, anchor, name)
    cites = claims[cid]['source'].split('; ')
    for c in cites: assert c in ci, (cid, c)
    prose = f"{TITLES[cid]} [claim {cid}]. {claims[cid]['claim_en']}"
    by_step.setdefault(step, []).append((anchor, name, cites, prose))
for step, ops in by_step.items():
    sid = f'  - id: STEP_Dt_{CH}_{step}\n'
    i = txt.index(sid)
    j = txt.index('    comment: >\n', i)
    nxt = txt.find(f'\n  - id: STEP_Dt_{CH}_', i + 1)
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
txt = txt[:k] + STEP_E([s[0] for s in SEATS]) + txt[k:]
a = txt.index('\nscenarios:\n'); b = txt.index('\nbinary_trees:', a)
scen = '\nscenarios:\n'
firsts = list(range(LO, min(LO + 6, HI + 1)))
for n, v in enumerate(firsts, 1):
    scen += f'  - id: S{n}\n    title_en: "after STEP_Dt_{CH}_{v} — Deut {CH}:{v}"\n    expect_en: "no test, no name."\n'
scen += f'  - id: S_last\n    title_en: "after STEP_Dt_{CH}_{HI} — Deut {CH}:{HI}"\n    expect_en: "no test, no name."\n'
txt = txt[:a] + scen + txt[b:]
open(unit, 'w', encoding='utf-8').write(txt)
d = yaml.safe_load(open(unit, encoding='utf-8'))
ops = [(s['id'], o) for s in d['boot_steps'] for o in s.get('operators', [])]
assert len(ops) == len(SEATS) and all(o['op'] == 'WITNESS_READ' for _, o in ops), len(ops)
assert d['derivation_log'][-1]['step'] == 'E' and len(d['boot_steps']) == HI - LO + 1
assert [s['id'] for s in d['scenarios']] == [f'S{n}' for n in range(1, len(firsts) + 1)] + ['S_last'] and all(s['expect_en'] == 'no test, no name.' for s in d['scenarios'])
print(f'{UID}: seated {len(ops)} operators on {len(by_step)} steps {sorted(by_step)}; scenarios {len(d["scenarios"])} in the anchor form')
