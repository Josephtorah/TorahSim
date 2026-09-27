import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28 (LEAN, 2026-09-26): SEAT the claims of the one manifest into the one draft unit as WITNESS_READ
# operators (one operator per claim at its FIRST verse's step, the [claim ID] marker in the prose, the cites the ledger's own names), append
# derivation_log step E, and REWRITE THE TREE-DERIVED SCENARIOS TO THE FROZEN ANCHOR FORM (the unit's first six verses + its last) before the
# ritual. Every cite is checked against the ledger's CITE INDEX before a byte is written; the yaml is re-loaded after. The prose is the
# manifest's own claim_en, so the operator and the claim cannot drift apart. THE STEP IDS ARE STEP_Dt_<c>_<v>. Usage: seat_ch26.py <uid>.
# Sitting 17's form (seat_ch22.py) over five units. RUN FROM THE REPO ROOT.
import subprocess
import json, re, sys, yaml
ROOT = _ROOT
DATE = '2026-09-26'
UID = sys.argv[1]
SPEC = {
 'deu_26_bikkurim_close': (26, 1, 19, [('DV26-01', 1, 'the_first_fruits_and_the_declaration', 'take_from_the_first_of_all_the_fruit_in_a_basket_to_the_place_declare_before_the_priest_recite_a_wandering_aramean_was_my_father_set_it_down_bow_and_rejoice'), ('DV26-02', 12, 'the_third_years_tithe_and_the_confession', 'when_you_finish_tithing_in_the_third_year_give_it_to_the_levite_the_stranger_the_orphan_and_the_widow_and_confess_i_have_removed_the_holy_from_the_house'), ('DV26-03', 16, 'the_covenant_formula', 'this_day_you_have_declared_him_your_god_and_he_has_declared_you_his_treasured_people_high_above_all_nations_a_holy_people')],
  'the first fruits brought in a basket and the declaration; the third year\'s tithe given and the confession; the covenant formula — His people, His treasure, high above all'),
 'deu_27_ebal_curses': (27, 1, 26, [('DV27-01', 1, 'the_stones_and_the_altar_on_ebal', 'on_the_crossing_day_set_up_great_stones_plaster_them_and_write_all_the_words_of_this_law_build_an_altar_of_whole_stones_without_iron_offer_and_rejoice'), ('DV27-02', 9, 'this_day_you_have_become_a_people', 'be_silent_and_hear_israel_this_day_you_have_become_the_people_of_the_lord_hearken_and_do'), ('DV27-03', 11, 'the_six_tribes_on_gerizim_and_the_six_on_ebal', 'simeon_levi_judah_issachar_joseph_and_benjamin_to_bless_reuben_gad_asher_zebulun_dan_and_naphtali_for_the_curse'), ('DV27-04', 14, 'the_twelve_curses_answered_amen', 'the_levites_answer_aloud_cursed_the_hidden_image_the_dishonored_parents_the_moved_landmark_the_misled_blind_the_perverted_judgment_the_four_lyings_the_secret_blow_the_bribe_and_the_unupheld_law')],
  'the stones plastered and written, the altar of whole stones on Ebal; this day you have become a people; the six tribes on Gerizim and the six on Ebal; the twelve curses answered Amen'),
 'deu_28_blessings': (28, 1, 14, [('DV28A-01', 1, 'the_condition_and_the_six_blessings', 'if_you_diligently_hearken_all_these_blessings_overtake_you_blessed_in_the_city_and_the_field_the_fruit_the_basket_and_the_trough_coming_in_and_going_out'), ('DV28A-02', 7, 'the_enemies_one_way_and_seven_the_storehouses', 'your_enemies_smitten_one_way_they_come_seven_ways_they_flee_the_blessing_in_your_storehouses'), ('DV28A-03', 9, 'the_holy_people_and_the_peoples_fear', 'the_lord_establishes_you_a_holy_people_as_he_swore_and_all_peoples_see_his_name_on_you_and_fear'), ('DV28A-04', 11, 'the_heavens_treasure_the_lending_the_head_and_not_the_tail', 'he_opens_his_good_treasure_the_heavens_for_rain_you_lend_and_do_not_borrow_the_head_and_not_the_tail_turn_not_right_or_left')],
  'the condition and the six blessings; the enemies one way and seven, the storehouses; the holy people and the peoples\' fear; the heavens\' treasure, the lending, the head and not the tail'),
 'deu_28_curses_a': (28, 15, 44, [('DV28B-01', 15, 'the_condition_and_the_six_curses', 'if_you_will_not_hearken_all_these_curses_overtake_you_cursed_in_the_city_and_the_field_the_basket_and_the_trough_the_fruit_coming_in_and_going_out'), ('DV28B-02', 20, 'the_curse_the_diseases_the_heavens_brass', 'the_curse_the_confusion_and_the_rebuke_the_pestilence_the_seven_strokes_the_heavens_brass_and_the_earth_iron_the_rain_dust'), ('DV28B-03', 25, 'the_defeat_the_carcass_the_boil_of_egypt_the_madness', 'smitten_one_way_out_and_seven_fleeing_the_carcass_for_the_birds_the_boil_of_egypt_and_the_hemorrhoids_madness_blindness_and_groping_at_noon'), ('DV28B-04', 30, 'the_wife_the_house_the_vineyard_the_beasts_the_sons_and_the_king_taken', 'another_lies_with_your_betrothed_your_house_and_vineyard_not_yours_your_ox_ass_and_flock_your_sons_and_daughters_given_led_with_your_king_to_serve_wood_and_stone'), ('DV28B-05', 38, 'the_harvests_failed_and_the_stranger_the_head', 'the_locust_the_worm_and_the_dropped_olives_the_sons_into_captivity_the_stranger_rises_and_lends_he_the_head_and_you_the_tail')],
  'the condition and the six curses; the curse, the diseases, the heavens brass; the defeat, the carcass, the boil of Egypt, the madness; the wife, the house, the vineyard, the beasts, the sons and the king taken; the harvests failed and the stranger the head'),
 'deu_28_curses_b': (28, 45, 69, [('DV28C-01', 45, 'the_curses_pursue_served_not_with_joy_the_iron_yoke', 'all_these_curses_pursue_you_a_sign_and_a_wonder_because_you_served_not_with_joy_you_serve_your_enemies_under_an_iron_yoke'), ('DV28C-02', 49, 'the_far_nation_as_the_eagle_and_the_siege', 'a_nation_from_the_end_of_the_earth_as_the_eagle_fierce_of_face_eats_your_fruit_and_besieges_you_in_all_your_gates_until_your_walls_fall'), ('DV28C-03', 53, 'the_flesh_of_sons_and_daughters_in_the_siege', 'you_eat_the_fruit_of_your_womb_in_the_siege_the_tender_man_and_the_delicate_woman_grudge_their_own_the_flesh_they_eat_in_secret'), ('DV28C-04', 58, 'the_book_not_kept_the_plagues_few_in_number_scattered', 'if_you_keep_not_the_words_written_in_this_book_the_plagues_made_wonderful_the_diseases_of_egypt_few_in_number_as_he_rejoiced_to_do_good_so_to_destroy_scattered_from_end_to_end'), ('DV28C-05', 65, 'the_trembling_heart_the_ships_to_egypt_and_the_covenants_words', 'no_rest_a_trembling_heart_morning_for_evening_back_to_egypt_in_ships_by_the_way_he_said_you_shall_not_see_again_sold_and_none_buys_these_are_the_words_of_the_covenant_in_moab_besides_horeb')],
  'the curses pursue — served not with joy, the iron yoke; the far nation as the eagle and the siege in all your gates; the flesh of sons and daughters in the siege; the book not kept — the plagues made wonderful, few in number, scattered; the trembling heart, the ships to Egypt and the covenant\'s words'),
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
    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 18, chapters 26-28, LEAN"
    comment: >
      The book's eighteenth reading, at the chapter's grain (chapter {CH}
      verses {LO}-{HI} as one draft — {WHAT}; the portion Ki Tavo 26:1-29:8
      holds the three chapters whole; the chapter the unit, chapter 28 in
      three by its own seams; three chapters read at one sitting in two
      runs under the cost rules' cap, five units, one ledger), THE NINTH
      SITTING OF THE LEAN PASS (ruled 2026-09-23) and the first on chapters
      WITHOUT A SPINE PISKA: every row whole under the whole-row rule:
      Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the export's rows
      the DB's — the identity, asserted); THE SIFREI ON DEUTERONOMY ON
      CHAPTER 26 ALONE — seven piskaot 297-303 (297 on 26:1, 298 headless
      inside the basket, 299 headless inside the declaration, 300 on 26:4,
      301 on 26:5 the recital with thirty-seven rows, 302 on 26:12, 303
      headless inside the confession with twenty; 304 opens on 31:14 — no
      piska on 26:16-31:13): seventy-seven rows read whole in both files
      (three rows read before found in the earlier ledgers by computation
      and reread whole — the species' analogy, the seventy, the mighty
      hand), twenty-six rows outside the spine citing the chapters read
      whole (twenty-five reread whole from chapters 6, 8, 11-17 and 22-25;
      one fresh; two EXCLUDED — the translator's "Dt.27:9" for 25:9), the
      kin (Leviticus 18, 20, 26; Exodus 22, 23, 34; Numbers 5, 14;
      Deuteronomy 4-7, 10-17, 19-25) credited by name from the earlier
      ledgers. Ledger deu_26_28_ki_tavo_{DATE}.md, coverage computed by
      script (215 sources over the three chapters), the ink facts computed
      from the Tanakh DB and the snapshot store (41 asserts: 1 fell on the
      first typed pass — a spine row citing 27:14 among chapter 27's outside
      set; 0 on the second), the engine's numeral parser measured on every
      verse (four number verses — one and seven twice, one, and the FALSE
      SIX of 28:63 "rejoiced", resolved by Onkelos), the store the DB at
      every verse but 28:27 and 28:30 (the ketiv and the qere), every
      quotation cut by consonants (zero misses on 217 rows over the two
      runs' checks). Seated as claims
      {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (18b); the
      full process (the docket whole, the full records) OWED to these
      chapters under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
    confidence: tested
    tags: ["[ORAL]","[HE-WRITTEN]"]
'''
unit = f'{ROOT}/logic/units/{UID}.yaml'
led = open(f'{ROOT}/logic/oral_triage/deu_26_28_ki_tavo_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
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
