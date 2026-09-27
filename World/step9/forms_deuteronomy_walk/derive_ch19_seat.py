import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN, 2026-09-24; RUN 2): seat_ch19.py DERIVED from the forms' seat_ch17.py by asserted substitutions — the SPEC block
# for THREE units (four claims at 19:1, 4, 14, 15; four at 20:1, 10, 16, 19; five at 21:1, 10, 15, 18, 22), the ledger's name, the STEP_E text (the lean sitting's, one
# per unit by the CH/LO/HI/WHAT the unit's own), the portable header made a scratch script's ROOT from git. RUN FROM THE REPO ROOT; the seat runs once per unit.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/seat_ch17.py', encoding='utf-8').read()
lines = src.split('\n'); assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
def sub(t, old, new, n=1):
    c = t.count(old); assert c == n, (c, n, old[:70]); return t.replace(old, new)
s = sub(s, "ROOT = _ROOT", "ROOT = _ROOT")
s = sub(s, "# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): SEAT the claims", "# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21 (LEAN, 2026-09-24): SEAT the claims")
s = sub(s, "# Sitting 14's form (seat_ch16.py) over two units. RUN FROM THE REPO ROOT.", "# Sitting 15's form (seat_ch17.py) over three units. RUN FROM THE REPO ROOT.")
s = sub(s, "Usage: seat_ch15.py <uid>.", "Usage: seat_ch19.py <uid>.")
i = s.index('SPEC = {'); j = s.index('\n}\n', i) + 3
SPEC = """SPEC = {
 'deu_19_miklat_witness': (19, 1, 21, [('DV19-01', 1, 'the_three_cities_separated', 'three_cities_separated_in_the_land_the_way_prepared_and_the_border_divided_in_three_three_more_if_the_border_is_enlarged'), ('DV19-02', 4, 'the_unwitting_killer_and_the_avenger', 'the_killer_without_hatred_from_yesterday_flees_and_lives_the_avenger_of_blood_pursues_the_hater_is_given_up_by_the_elders'), ('DV19-03', 14, 'the_landmark', 'you_shall_not_move_your_neighbors_landmark_which_the_first_ones_bounded'), ('DV19-04', 15, 'the_witnesses_and_the_plotting_witness', 'one_witness_stands_not_two_or_three_stand_the_judges_inquire_well_and_do_to_the_plotter_as_he_plotted_life_for_life_eye_for_eye')],
  'the three cities separated with the way prepared and the border divided in three, three more on the enlargement; the unwitting killer\\'s flight and the avenger\\'s pursuit, the hater given up by his city\\'s elders; the landmark; one witness standing for nothing, two or three standing, and the plotting witness done to as he plotted'),
 'deu_20_war_rules': (20, 1, 20, [('DV20-01', 1, 'the_priests_speech_and_the_four_exemptions', 'fear_not_the_horse_and_chariot_the_priest_speaks_hear_israel_the_officers_send_home_the_new_house_the_vineyard_the_betrothed_and_the_fearful'), ('DV20-02', 10, 'the_call_for_peace_and_the_siege', 'call_the_city_to_peace_for_tribute_and_service_else_besiege_it_smite_the_males_and_take_the_women_children_and_spoil'), ('DV20-03', 16, 'the_seven_nations_banned', 'of_the_cities_of_these_peoples_let_no_breath_live_utterly_destroy_the_six_nations_as_the_lord_commanded_lest_they_teach_their_abominations'), ('DV20-04', 19, 'the_trees_of_the_siege', 'the_fruit_tree_not_cut_in_a_long_siege_for_the_tree_is_not_a_man_the_barren_tree_cut_for_the_siege_works_until_the_city_falls')],
  'the priest\\'s speech and the officers\\' four exemptions before the battle; the call for peace, the tribute and the siege\\'s spoil; the seven nations banned as the LORD commanded; the trees of the siege'),
 'deu_21_eglah_family': (21, 1, 23, [('DV21-01', 1, 'the_broken_necked_heifer', 'the_slain_one_found_the_measuring_to_the_nearest_city_the_heifer_of_the_herd_broken_necked_in_the_rough_valley_the_priests_present_the_elders_wash_and_declare_and_the_blood_is_atoned'), ('DV21-02', 10, 'the_captive_woman', 'the_beautiful_captive_brought_home_shaved_and_weeping_a_month_then_a_wife_released_not_sold_if_unwanted'), ('DV21-03', 15, 'the_firstborns_double', 'the_firstborn_of_the_hated_wife_recognized_for_double_of_all_the_father_cannot_prefer_the_loved_wifes_son'), ('DV21-04', 18, 'the_stubborn_and_rebellious_son', 'the_son_who_heeds_neither_parent_chastised_then_brought_to_the_elders_a_glutton_and_a_drunkard_stoned_by_his_city_the_evil_purged'), ('DV21-05', 22, 'the_hanged_buried_the_same_day', 'the_executed_man_hanged_on_a_tree_not_left_overnight_buried_that_day_for_a_hanged_one_is_a_curse_of_god')],
  'the broken-necked heifer for the slain one whose killer is unknown, the measuring, the rite in the valley and the elders\\' declaration; the captive woman\\'s month and her release; the firstborn\\'s double for the hated wife\\'s son; the stubborn and rebellious son stoned; the hanged man buried the same day'),
}
"""
s = s[:i] + SPEC + s[j:]
i = s.index("    name_en: \"Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 15, chapters 17-18, LEAN\""); j = s.index("    confidence: tested\n", i)
STEPE = """    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 16, chapters 19-21, LEAN"
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
"""
s = s[:i] + STEPE + s[j:]
s = sub(s, "led = open(f'{ROOT}/logic/oral_triage/deu_17_18_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]", "led = open(f'{ROOT}/logic/oral_triage/deu_19_21_shoftim_ki_teitzei_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]")
assert 'deu_17' not in s and 'sitting 15' not in s.replace("Sitting 15's form", '') and 'chapters 17-18' not in s and '_ROOT' not in s, re.findall(r'.{30}(?:deu_17|sitting 15|chapters 17-18|_ROOT).{30}', s)
open(f'{SP}/seat_ch19.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s); print('seat_ch19.py derived:', len(s), 'bytes; three units, 4 + 4 + 5 seats')
