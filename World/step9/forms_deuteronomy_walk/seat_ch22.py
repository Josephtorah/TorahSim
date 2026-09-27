import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 17 — CHAPTERS 22-25 (LEAN, 2026-09-26): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch22.py <uid>.
# Sitting 16's form (seat_ch19.py) over four units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-25'
UID = sys.argv[1]
SPEC = {
 'deu_22_return_sex_laws': (22, 1, 29, [('DV22-01', 1, 'the_lost_thing_returned', 'return_your_brothers_straying_ox_and_sheep_keep_the_lost_thing_until_he_seeks_it_raise_the_fallen_ass_with_him'), ('DV22-02', 5, 'the_garments_the_nest_and_the_parapet', 'no_mans_gear_on_a_woman_send_the_mother_bird_away_and_take_the_young_make_a_parapet_for_the_new_roof'), ('DV22-03', 9, 'the_mixtures_and_the_tassels', 'sow_not_mixed_seed_plow_not_ox_and_ass_together_wear_not_wool_and_linen_make_tassels_on_the_four_corners'), ('DV22-04', 13, 'the_slandered_bride', 'the_charges_of_words_the_tokens_before_the_elders_the_hundred_of_silver_and_the_wife_never_sent_away_or_the_stoning_at_her_fathers_door'), ('DV22-05', 22, 'the_adulterer_the_betrothed_girl_and_the_seducer', 'both_die_for_the_married_woman_the_city_and_the_field_for_the_betrothed_girl_fifty_of_silver_for_the_seized_virgin')],
  'the lost thing returned and the fallen beast raised; the garments, the nest and the parapet; the mixtures and the tassels; the slandered bride; the adulterer, the betrothed girl and the seducer'),
 'deu_23_qahal_purity_vows': (23, 1, 26, [('DV23-01', 1, 'the_excluded_from_the_assembly', 'the_fathers_wife_the_crushed_the_mamzer_ammon_and_moab_for_ever_edom_and_egypt_to_the_third_generation'), ('DV23-02', 10, 'the_camps_holiness', 'the_nights_chance_outside_the_camp_the_bath_and_the_sunset_the_peg_and_the_place_for_the_lord_walks_in_your_camp'), ('DV23-03', 16, 'the_slave_the_harlots_hire_and_the_interest', 'the_escaped_slave_not_returned_no_harlots_hire_or_dogs_price_in_the_house_no_bite_to_your_brother_to_the_foreigner_bite'), ('DV23-04', 22, 'the_vows', 'delay_not_to_pay_a_vow_to_refrain_is_no_sin_what_your_lips_utter_keep_and_do'), ('DV23-05', 25, 'the_laborer_in_the_vineyard_and_the_grain', 'eat_grapes_your_fill_but_none_in_your_vessel_pluck_ears_by_hand_but_swing_no_sickle')],
  'the father\'s wife and the excluded from the assembly; the camp\'s holiness; the slave, the harlot\'s hire and the interest; the vows; the laborer in the vineyard and the standing grain'),
 'deu_24_divorce_poor': (24, 1, 22, [('DV24-01', 1, 'the_divorce_and_the_return_forbidden', 'the_bill_of_cutting_off_in_her_hand_she_becomes_anothers_the_first_husband_may_not_take_her_again'), ('DV24-02', 5, 'the_newlywed_the_millstone_and_the_kidnapper', 'one_year_free_for_his_house_no_mill_in_pledge_for_it_is_a_life_the_thief_of_a_soul_dies'), ('DV24-03', 8, 'leprosy_by_the_priests_and_miriam', 'take_heed_in_the_plague_as_the_priests_teach_remember_miriam_on_the_way'), ('DV24-04', 10, 'the_pledge_and_the_hirelings_wage', 'stand_outside_for_the_pledge_return_the_poor_mans_pledge_at_sunset_give_the_wage_on_its_day_before_the_sun_sets'), ('DV24-05', 16, 'fathers_and_sons_the_strangers_justice_and_the_gleanings', 'each_dies_for_his_own_sin_pervert_not_the_sojourners_judgment_the_forgotten_sheaf_the_olive_and_the_vineyard_for_the_sojourner_orphan_and_widow')],
  'the divorce and the return forbidden; the newlywed, the millstone and the kidnapper; leprosy by the priests and Miriam remembered; the pledge and the hireling\'s wage; fathers and sons, the stranger\'s justice, the sheaf and the gleanings'),
 'deu_25_courts_yibbum': (25, 1, 19, [('DV25-01', 1, 'the_lashes', 'the_judges_justify_and_condemn_the_wicked_flogged_before_the_judge_by_number_forty_and_no_more'), ('DV25-02', 4, 'the_muzzle', 'muzzle_not_an_ox_in_its_threshing'), ('DV25-03', 5, 'the_levirate_and_the_shoe', 'brothers_dwelling_together_one_dies_without_a_son_her_levir_takes_her_the_firstborn_on_the_dead_name_or_the_refusal_at_the_gate_the_shoe_drawn_and_the_spitting'), ('DV25-04', 11, 'the_wrestlers_shame_and_the_just_weights', 'cut_off_her_hand_without_pity_no_stone_and_stone_no_ephah_and_ephah_a_whole_and_just_measure'), ('DV25-05', 17, 'amalek_remembered', 'remember_what_amalek_did_on_the_way_blot_out_his_memory_when_the_lord_gives_you_rest_forget_not')],
  'the lashes; the muzzle; the levirate and the shoe; the wrestlers\' shame and the just weights; Amalek remembered'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 17, chapters 22-25, LEAN"
    comment: >
      The book's seventeenth reading, at the chapter's grain (chapter {CH} as
      one draft — {WHAT}; no portion edge inside the four — Ki Teitzei
      21:10-25:19 holds them whole; the chapter the unit; four chapters read
      at one sitting in three runs under the cost rules' cap, four units,
      one ledger), THE SEVENTH SITTING OF THE LEAN PASS (ruled 2026-09-23):
      every row whole under the whole-row rule: Onkelos Deuteronomy
      {CH}:{LO}-{HI} whole and fresh (the export's rows the DB's — the
      identity, asserted); THE SIFREI ON DEUTERONOMY ON THE FOUR CHAPTERS —
      seventy-five piskaot 222-296 (twenty-four heads in chapter 22 with 222
      headless at the chapter's head opening on Exodus 23:5 and 236 headless
      inside the father's words, twenty-two in chapter 23, eighteen in
      chapter 24 with 269 headless on the grounds of divorce and 283 on the
      forgotten sheaf, eleven in chapter 25 with 295 headless; every head in
      verse order): four hundred and thirty-four rows read whole in both
      files (twelve rows read before found in the earlier ledgers by
      computation and reread whole — the Sabbath's remember, the Shema, the
      blood, the clean bird, the cry, the bribe, the blemish, the peace
      call, the slave's gate, the pity formula, the herdsmen's strife
      twice), fourteen rows outside the spine citing the chapters read
      whole (ten reread whole from chapters 11-15, 17-18 and 19-21; four
      EXCLUDED — the translator's "Dt.23:12" for the blessing of Benjamin),
      the kin (Exodus 22, 23; Leviticus 13, 14, 19, 21, 25; Numbers 5, 12,
      15, 22, 23, 30; Genesis 13; Deuteronomy 5, 15, 16, 17, 19-21) credited
      by name from the earlier ledgers. Ledger
      deu_22_25_ki_teitzei_{DATE}.md, coverage computed by script (540
      sources over the four chapters), the ink facts computed from the
      Tanakh DB and the snapshot store (49 asserts: 4 fell on the first
      typed pass — the English's prefix on every piska's first row, three
      other chapters' spine rows among a dump's outside set, a list's order,
      the girl written twice; 0 on the second), the engine's numeral parser
      measured on every verse (eleven number verses and four ordinals), the
      store the DB at every verse but chapter 22's eleven where the girl is
      written as a boy, every quotation cut by consonants (zero misses on
      540 rows over the three runs' checks). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (17b); the
      full process (the docket whole, the full records) OWED to these
      chapters under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_22_25_ki_teitzei_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
