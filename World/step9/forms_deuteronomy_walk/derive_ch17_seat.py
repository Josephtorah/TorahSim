import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): seat_ch17.py DERIVED from the forms' seat_ch16.py by asserted substitutions — the SPEC block
# for TWO units (four claims each at 17:1, 2, 8, 14 and 18:1, 6, 9, 15), the date, the ledger's name, the STEP_E text (the lean sitting's, one per unit by the
# CH/LO/HI/WHAT the unit's own), the portable header made a scratch script's ROOT from git. RUN FROM THE REPO ROOT; the seat runs once per unit (seat_ch17.py <uid>).
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/seat_ch16.py', encoding='utf-8').read()
lines = src.split('\n'); assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
def sub(t, old, new, n=1):
    c = t.count(old); assert c == n, (c, n, old[:70]); return t.replace(old, new)
s = sub(s, "ROOT = _ROOT", "ROOT = _ROOT")
s = sub(s, "# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16 (LEAN, 2026-09-23): SEAT the claims", "# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18 (LEAN, 2026-09-24): SEAT the claims")
s = sub(s, "# Sitting 13's form (seat_ch15.py). RUN FROM THE REPO ROOT.", "# Sitting 14's form (seat_ch16.py) over two units. RUN FROM THE REPO ROOT.")
s = sub(s, "DATE = '2026-09-23'", "DATE = '2026-09-24'")
i = s.index('SPEC = {'); j = s.index('\n}\n', i) + 3
SPEC = """SPEC = {
 'deu_17_courts_king': (17, 1, 20, [('DV17-01', 1, 'the_blemished_offering', 'no_ox_or_sheep_with_a_blemish_any_evil_thing_for_it_is_an_abomination'), ('DV17-02', 2, 'the_idolater_in_the_gate', 'the_man_or_woman_who_serves_other_gods_inquired_well_stoned_at_the_gate_by_two_witnesses_or_three_the_witnesses_hand_first_the_evil_purged'), ('DV17-03', 8, 'the_high_court_at_the_place', 'the_hard_case_brought_up_to_the_priests_the_levites_and_the_judge_the_sentence_not_turned_from_the_rebel_dies_and_the_people_hear_and_fear'), ('DV17-04', 14, 'the_king', 'a_king_chosen_from_among_your_brothers_no_foreigner_no_horses_wives_or_gold_his_copy_of_the_law_read_all_his_days_his_heart_not_lifted')],
  'the blemished offering an abomination; the idolater in the gate inquired, stoned by two witnesses or three with the witnesses\\' hand first and the evil purged; the hard case brought up to the high court at the place, its sentence not turned from and the rebel put to death; the king chosen from among the brothers with his three limits and his copy of the law'),
 'deu_18_levi_prophet': (18, 1, 22, [('DV18-01', 1, 'the_priests_portion_and_dues', 'no_portion_with_israel_the_fire_offerings_the_shoulder_cheeks_and_maw_the_firsts_of_grain_wine_oil_and_fleece_standing_to_minister'), ('DV18-02', 6, 'the_levite_from_the_gates', 'the_levite_who_comes_with_all_his_souls_desire_to_the_place_ministers_and_eats_portion_as_portion_besides_the_fathers_sales'), ('DV18-03', 9, 'the_diviners_barred', 'none_who_passes_through_the_fire_no_diviner_soothsayer_omen_reader_sorcerer_charmer_ghost_asker_or_necromancer_be_whole_with_the_lord'), ('DV18-04', 15, 'the_prophet_like_moses', 'a_prophet_from_among_the_brothers_as_asked_at_horeb_my_words_in_his_mouth_the_presumptuous_prophet_dies_the_word_tested_by_its_coming')],
  'the priests\\' portion the fire offerings and their dues the shoulder, the cheeks and the maw and the firsts; the Levite from the gates ministering at the place portion as portion; the diviners\\' nine barred and Israel whole with the LORD; the prophet like Moses raised as asked at Horeb, the false prophet dying and the word tested by its coming'),
}
"""
s = s[:i] + SPEC + s[j:]
i = s.index("    name_en: \"Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 14, chapter 16, LEAN\""); j = s.index("    confidence: tested\n", i)
STEPE = """    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 15, chapters 17-18, LEAN"
    comment: >
      The book's fifteenth reading, at the chapter's grain (chapter {CH} as one
      draft — {WHAT}; no portion edge inside it — Shoftim 16:18-21:9 holds
      the two chapters whole; two chapters read at one sitting, two units,
      one ledger), THE THIRD SITTING OF THE LEAN PASS (ruled 2026-09-23):
      one reading window under the cost rules, every row whole under the
      whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh (the
      export's rows the DB's — the identity, asserted); THE SIFREI ON
      DEUTERONOMY ON THE TWO CHAPTERS — thirty-two piskaot 147-178 in verse
      order (sixteen heads in each chapter, none headless, no tail folded
      in): one hundred and eighty-one rows read whole in both files (seven
      prior reads found in the earlier ledgers by computation and reread
      whole — the order of offerings, the blemish's class, the host of
      heaven apportioned, the seven investigations, the calf cut in two),
      eleven rows outside the spine citing the chapters read whole (six
      reread whole from chapters 11-14; five fresh — the witnesses male, the
      blemished priest's blessing, the dog's price, the Temple's height
      twice), the kin (Leviticus 7, 19, 20, 22; Numbers 18, 22, 23, 35;
      Exodus 22; Deuteronomy 1, 4, 5, 10, 12, 13, 14, 15) credited by name
      from the earlier ledgers. Ledger deu_17_18_shoftim_{DATE}.md, coverage
      computed by script (234 sources over the two chapters), the ink facts
      computed from the Tanakh DB and the snapshot store (1 assert fell on
      the first typed pass — a fact the print corrected; green on the
      second), the engine's numeral parser measured on every verse (two
      number verses in chapter 17, none in 18; no ordinal; "from one" at
      18:6 unread behind its prefix), the store the DB at every verse, every
      quotation cut by consonants (four misses retyped from the print at
      once). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah rows the spine cites are the compile's cases (15b); the
      full process (the docket whole, the full records) OWED to these
      chapters under the lean pass (World/step9/COMPILE_DEBT.md's lean-pass box).
"""
s = s[:i] + STEPE + s[j:]
s = sub(s, "led = open(f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]", "led = open(f'{ROOT}/logic/oral_triage/deu_17_18_shoftim_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]")
assert 'deu_16' not in s and 'sitting 14' not in s.replace("Sitting 14's form", '') and 'chapter 16' not in s and '_ROOT' not in s, re.findall(r'.{30}(?:deu_16|sitting 14|chapter 16|_ROOT).{30}', s)
open(f'{SP}/seat_ch17.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s); print('seat_ch17.py derived:', len(s), 'bytes; two units, four seats each')
