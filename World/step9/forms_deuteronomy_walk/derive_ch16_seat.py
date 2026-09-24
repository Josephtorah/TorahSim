import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN, 2026-09-23): seat_ch16.py DERIVED from the forms' seat_ch15.py by asserted substitutions — the SPEC block
# (eight claims DV16-01..08 at 16:1, 3, 5, 9, 13, 16, 18, 21), the date, the ledger's name, the STEP_E text (the lean sitting's), the portable header made a
# scratch script's ROOT from git. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/seat_ch15.py', encoding='utf-8').read()
lines = src.split('\n'); assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
def sub(t, old, new, n=1):
    c = t.count(old); assert c == n, (c, n, old[:70]); return t.replace(old, new)
s = sub(s, "ROOT = _ROOT", "ROOT = _ROOT")
s = sub(s, "# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15 (2026-09-22, two runs and the tail): SEAT the claims", "# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN, 2026-09-23): SEAT the claims")
s = sub(s, "# Sitting 12's form (seat_ch14.py). RUN FROM THE REPO ROOT.", "# Sitting 13's form (seat_ch15.py). RUN FROM THE REPO ROOT.")
s = sub(s, "DATE = '2026-09-22'", "DATE = '2026-09-23'")
i = s.index('SPEC = {'); j = s.index('\n}\n', i) + 3
SPEC = """SPEC = {
 'deu_16_festivals_judges': (16, 1, 22, [('DV16-01', 1, 'the_month_of_aviv_and_the_passover', 'observe_the_month_of_aviv_and_keep_the_passover_for_by_night_he_brought_you_out_sacrifice_it_flock_and_herd_at_the_place_where_his_name_dwells'), ('DV16-02', 3, 'the_leaven_and_the_bread_of_affliction', 'eat_no_leaven_with_it_seven_days_unleavened_bread_of_affliction_for_in_haste_you_went_out_no_leaven_seen_in_your_border_none_of_the_flesh_left_until_morning'), ('DV16-03', 5, 'the_place_the_evening_and_the_seventh_day', 'not_within_your_gates_but_at_the_place_at_evening_at_sunset_the_season_of_your_going_out_cook_and_eat_and_turn_in_the_morning_six_days_and_a_solemn_assembly_on_the_seventh'), ('DV16-04', 9, 'the_weeks_from_the_sickle_and_the_feast_of_weeks', 'count_seven_weeks_from_the_sickle_on_the_standing_grain_keep_the_feast_of_weeks_with_the_measure_of_your_hand_rejoice_with_your_household_and_remember_the_slave'), ('DV16-05', 13, 'the_feast_of_booths', 'keep_the_feast_of_booths_seven_days_when_you_gather_in_rejoice_in_your_feast_seven_days_at_the_place_and_be_altogether_joyful'), ('DV16-06', 16, 'the_three_pilgrimages_and_the_gift_of_the_hand', 'three_times_a_year_all_your_males_shall_appear_at_the_three_feasts_and_none_empty_each_man_as_his_hand_gives'), ('DV16-07', 18, 'the_judges_and_officers', 'judges_and_officers_in_all_your_gates_tribe_by_tribe_righteous_judgment_no_wresting_no_respecting_of_persons_no_bribe_justice_justice_pursue_and_live_and_inherit'), ('DV16-08', 21, 'the_asherah_and_the_pillar', 'plant_no_asherah_of_any_tree_beside_the_altar_and_set_up_no_pillar_which_the_lord_your_god_hates')],
  'the month of Aviv observed and the Passover kept by night, sacrificed of flock and herd at the place; the leaven barred and the bread of affliction eaten seven days in haste\\'s memory, no leaven seen in the border and none of the flesh kept to morning; the Passover not in the gates but at the place at evening, cooked and eaten there, the morning\\'s return, six days and the seventh\\'s assembly; the weeks counted from the sickle and the feast of weeks with the hand\\'s measure, the household rejoicing and the slave remembered; the feast of booths seven days at the gathering, altogether joyful; the three pilgrimages of every male, none empty, each as his hand gives; the judges and officers in every gate tribe by tribe, the three prohibitions and the bribe, justice pursued for the land; the asherah and the pillar barred beside the altar'),
}
"""
s = s[:i] + SPEC + s[j:]
i = s.index("    name_en: \"Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 13, chapter 15\""); j = s.index("    confidence: tested\n", i)
STEPE = """    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 14, chapter 16, LEAN"
    comment: >
      The book's fourteenth reading, at the chapter's grain (chapter 16 as one
      draft — {WHAT}; a portion edge inside it — Re'eh ends at 16:17 and
      Shoftim opens at 16:18; the chapter the unit), THE FIRST SITTING OF THE
      LEAN PASS (ruled 2026-09-23): one reading window under the cost rules,
      every row whole under the whole-row rule: Onkelos Deuteronomy
      {CH}:{LO}-{HI} whole and fresh (the export's twenty-two rows the DB's
      twenty-two — the identity, asserted); THE SIFREI ON DEUTERONOMY ON THE
      CHAPTER — twenty piskaot 127-146 in verse order (nineteen heads in the
      chapter and 135 headless on 16:8, folded in by position; no tail folded
      in): one hundred and eleven rows read whole in both files (two prior
      reads found in chapter 12's ledger by computation and reread whole —
      the rejoicing by analogy, the asherah's a fortiori), three rows outside
      the spine citing the chapter read whole (52:4 and 147:2 reread whole
      from chapters 11 and 12 — the guard of the land, the order of
      offerings; 281:1 fresh — the sojourner's judgment), the kin (Leviticus
      23; Numbers 9, 28, 29; Exodus 23 and 34; Leviticus 19:15 and 26:1;
      Deuteronomy 1:16-17, 5:15, 7:5, 12, 15:15) credited by name from the
      earlier ledgers. Ledger deu_16_reeh_shoftim_{DATE}.md, coverage computed
      by script (136 sources), the ink facts computed from the Tanakh DB and
      the snapshot store (2 asserts fell on the first typed pass, both the
      instrument's shape; green on the second), the engine's numeral parser
      measured on every verse (eight number verses, two ordinals, one
      starred token; no gap), the store the DB at every verse, every
      quotation cut by consonants (three misses retyped from the print).
      Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (14b); the
      full process (the docket whole, the full records) OWED to this chapter
      under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
"""
s = s[:i] + STEPE + s[j:]
s = sub(s, "led = open(f'{ROOT}/logic/oral_triage/deu_15_reeh_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]", "led = open(f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]")
assert 'deu_15' not in s and 'sitting 13' not in s.replace("Sitting 13's form", '') and 'chapter 15' not in s and '_ROOT' not in s, re.findall(r'.{30}(?:deu_15|sitting 13|chapter 15|_ROOT).{30}', s)
open(f'{SP}/seat_ch16.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s); print('seat_ch16.py derived:', len(s), 'bytes; eight seats')
