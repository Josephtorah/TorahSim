import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33, THE BLESSING (LEAN, 2026-09-29; RUN 4): seat_ch33.py DERIVED from the forms' seat_ch32.py by asserted substitutions — the
# SPEC for ONE unit (33:1, 3, 6, 8, 12, 13, 18, 20, 22, 26, 28 — eleven seats), the ledger's name, the DATE (2026-09-29), the STEP_E text (the lean sitting's, one unit by
# the CH/LO/HI/WHAT), the portable header stripped, ROOT from git. RUN FROM THE REPO ROOT; the seat runs once per unit. Sitting 20's form (derive_ch32_seat.py).
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/seat_ch32.py', encoding='utf-8').read()
lines = src.split('\n'); assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
def sub(t, old, new, n=1):
    c = t.count(old); assert c == n, (c, n, old[:70]); return t.replace(old, new)
s = sub(s, "ROOT = _ROOT", "ROOT = _ROOT")
s = sub(s, "# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32, THE SONG (LEAN, 2026-09-27/28): SEAT the claims", "# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33, THE BLESSING (LEAN, 2026-09-29): SEAT the claims")
s = sub(s, "# Sitting 19's form (seat_ch29.py) over two units. RUN FROM THE REPO ROOT.", "# Sitting 20's form (seat_ch32.py) over one unit. RUN FROM THE REPO ROOT.")
s = sub(s, "Usage: seat_ch32.py <uid>.", "Usage: seat_ch33.py <uid>.")
s = sub(s, "DATE = '2026-09-27'", "DATE = '2026-09-29'")
i = s.index('SPEC = {'); j = s.index('\n}\n', i) + 3
SPEC = """SPEC = {
 'deu_33_ve_zot': (33, 1, 29, [('DV33-01', 1, 'and_this_is_the_blessing_the_lord_came_from_sinai', 'and_this_is_the_blessing_moses_the_man_of_god_blessed_israel_before_his_death_the_lord_came_from_sinai_rose_from_seir_shone_from_paran_with_myriads_of_holy_ones_a_fiery_law'), ('DV33-02', 3, 'he_loves_the_peoples_a_law_moses_commanded_a_king_in_jeshurun', 'he_loves_the_peoples_all_his_holy_ones_in_your_hand_they_sat_at_your_feet_a_law_moses_commanded_us_the_inheritance_of_the_congregation_of_jacob_a_king_in_jeshurun_when_the_heads_gathered_the_tribes_together'), ('DV33-03', 6, 'let_reuben_live_hear_lord_the_voice_of_judah', 'let_reuben_live_and_not_die_his_men_a_number_and_this_for_judah_hear_lord_the_voice_of_judah_bring_him_to_his_people_his_hands_contend_a_help_against_his_adversaries'), ('DV33-04', 8, 'levi_the_thummim_and_the_urim_they_shall_teach_jacob', 'levi_your_thummim_and_your_urim_proved_at_massah_meribah_the_father_and_mother_unseen_the_covenant_kept_they_shall_teach_jacob_incense_and_whole_offering_bless_his_substance_smite_the_loins'), ('DV33-05', 12, 'benjamin_the_beloved_dwells_between_his_shoulders', 'benjamin_the_beloved_of_the_lord_dwells_in_safety_by_him_covered_all_the_day_and_he_dwells_between_his_shoulders'), ('DV33-06', 13, 'joseph_the_precious_things_the_crown_of_him_separate', 'joseph_blessed_of_the_lord_his_land_the_precious_things_of_heaven_the_dew_the_deep_the_sun_and_the_moons_the_ancient_mountains_him_that_dwelt_in_the_bush_the_crown_of_him_separate_from_his_brethren_the_firstling_bullock_the_horns_of_the_wild_ox_ephraim_and_manasseh'), ('DV33-07', 18, 'zebulun_in_going_out_issachar_in_tents_the_mountain', 'rejoice_zebulun_in_your_going_out_and_issachar_in_your_tents_they_call_peoples_to_the_mountain_sacrifices_of_righteousness_the_abundance_of_the_seas_the_treasures_of_the_sand'), ('DV33-08', 20, 'gad_the_lioness_the_lawgivers_portion', 'blessed_be_he_that_enlarges_gad_he_dwells_as_a_lioness_tears_the_arm_and_the_crown_he_chose_a_first_part_the_lawgivers_portion_hidden_the_heads_of_the_people_the_righteousness_of_the_lord'), ('DV33-09', 22, 'dan_the_lions_whelp_naphtali_sated_asher_blessed_above_sons', 'dan_a_lions_whelp_from_bashan_naphtali_sated_with_favor_possess_the_sea_and_the_south_asher_blessed_above_sons_dips_his_foot_in_oil_iron_and_brass_your_bars_as_your_days_your_strength'), ('DV33-10', 26, 'none_like_the_god_of_jeshurun_the_everlasting_arms', 'none_like_the_god_of_jeshurun_who_rides_upon_the_heaven_as_your_help_the_eternal_god_a_dwelling_place_underneath_the_everlasting_arms_he_drove_out_the_enemy_and_said_destroy'), ('DV33-11', 28, 'israel_dwells_in_safety_happy_are_you_o_israel', 'israel_dwells_in_safety_the_fountain_of_jacob_a_land_of_corn_and_wine_dew_happy_are_you_o_israel_who_is_like_you_a_people_saved_by_the_lord_the_shield_and_the_sword_tread_upon_their_high_places')],
  'and this is the blessing — Moses the man of God before his death, the LORD came from Sinai with myriads of holy ones and a fiery law; He loves the peoples, a law Moses commanded us, a king in Jeshurun; let Reuben live and not die, hear, LORD, the voice of Judah; Levi — the Thummim and the Urim, the father and mother unseen, they shall teach Jacob, incense and whole offering; Benjamin the beloved dwells between His shoulders; Joseph — the precious things of heaven and earth, the bush, the crown of him separate from his brethren, the horns of the wild ox; Zebulun in going out and Issachar in tents, the mountain and the seas; Gad the lioness and the lawgiver\\'s portion; Dan the lion\\'s whelp, Naphtali sated with favor, Asher blessed above sons, iron and brass; none like the God of Jeshurun — the rider of the heaven, the everlasting arms, destroy; Israel dwells in safety — happy are you, O Israel, who is like you, the shield and the sword, tread upon their high places'),
}
"""
s = s[:i] + SPEC + s[j:]
i = s.index("    name_en: \"Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 20, chapter 32, THE SONG, LEAN\""); j = s.index("    confidence: tested", i)
STEPE = """    name_en: "Deuteronomy {CH}:{LO}-{HI} derivation {DATE} — THE DEUTERONOMY WALK sitting 21, chapter 33, THE BLESSING, LEAN"
    comment: >
      The book's twenty-first reading, at the chapter's grain (chapter {CH}
      verses {LO}-{HI} as one draft — {WHAT}; the portion Vezot Habrachah
      runs 33:1-34:12 — chapter 33 the unit, CHAPTER NUMBERS, chapter 34
      the next sitting's; one chapter read at one sitting in four runs
      under the cost rules' cap by the split's byte plan, one unit, one
      ledger), THE FIFTEENTH SITTING OF THE LEAN PASS (ruled 2026-09-23)
      and its eighth reading, THE SPINE IN FORCE: every row whole under the
      whole-row rule: Onkelos Deuteronomy {CH}:{LO}-{HI} whole and fresh
      (the export's rows the DB's — the identity, asserted); THE SIFREI ON
      DEUTERONOMY IN FORCE — fifteen piskaot 342-356 on 33:1-29 (142 rows
      read whole in both files, 355 on 33:20 the longest with thirty rows;
      every head present once the instrument tolerated the comma in 342's
      head — the export's one comma head, read as headless by sittings 19
      and 20; fifteen rows read before over eleven ledgers REREAD WHOLE and
      marked by computation; the rows seated at the verse each cites in the
      Hebrew — THE SEAT RULE BY ROW — so Benjamin's rows inside Levi's piska
      seat at 33:12 and Gad's piska carries Dan, Naphtali, Asher and the
      rider); five rows outside the spine citing the chapter read whole
      (every one reread whole from chapters 6, 11, 29-31 and 32 — the walk's
      first reading without a fresh outside row), the kin (Genesis 47-49;
      Exodus 28, 32; Numbers 1, 2, 25, 27, 32; Deuteronomy 10, 26-28, 32)
      credited by name from the earlier ledgers. Ledger
      deu_33_ve_zot_{DATE}.md, coverage computed by script (176 sources
      over the chapter: 29 Onkelos + 142 spine + 5 outside), the ink facts
      computed from the Tanakh DB and the snapshot store (53 asserts: 0
      fell on the first typed pass of block a, 1 of block b — the Torah's
      third Aramaic seat at 33:10 past the measure's cut; 0 on the third),
      the engine's numeral parser measured on every verse (33:23's "sated"
      MARKED as seven's homograph and counted as nothing — no number in the
      chapter, the myriads and thousands construct plurals unread), the
      store the DB at every verse but 33:2 and 33:9 (the ketiv and the qere
      both kept — the fiery law one word and two, "his son" and "his sons"),
      every quotation cut by consonants (zero misses on 176 rows in the
      whole-spine check). Seated as claims {ids[0]}..{ids[-1][-2:]}: {'; '.join(TITLES[i].lower() for i in ids)}.
      The Mishnah and Tosefta rows the spine names (Avot 5:6 the twilight
      creations at 355:6; Berakhot 4:3 the eighteen at 343:3; Avot 3:6 at
      346:2; Shekalim 1:1 at 352:14; Eduyot 8:6 at 352:8; Sanhedrin 10:1 at
      347:2; Keritot 2:1 at 354:5; Menachot 8:3 at 355:20; Sheviit at 355:23;
      Rosh Hashanah 2:8-9 at 33:18's Onkelos; Tosefta Sotah 11:11 at 352:11,
      Tosefta Eduyot 1:1 at 48:9, Tosefta Avodah Zarah 8:4 at 343:6) are the
      compile's cases (21b); the full process (the docket whole, the full
      records) OWED to this chapter under the lean pass
      (World/step9/COMPILE_DEBT.md's lean-pass box).
"""
s = s[:i] + STEPE + s[j:]
s = sub(s, "led = open(f'{ROOT}/logic/oral_triage/deu_32_haazinu_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]", "led = open(f'{ROOT}/logic/oral_triage/deu_33_ve_zot_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]")
left = re.findall(r'.{30}(?:deu_32|sitting 20|chapter 32|THE SONG|_ROOT|haazinu|seat_ch32).{30}', s.replace("Sitting 20's form (seat_ch32.py)", ''))
assert not left, left
open(f'{SP}/seat_ch33.py', 'w', encoding='utf-8').write(s)
ast.parse(s); print('seat_ch33.py derived:', len(s), 'bytes; one unit, 11 seats')
