#!/usr/bin/env python3
"""o8_s2_predict.py — O8 S2 FROM EDEN TO HAGAR (2026-09-08; NARRATIVE_GAPS.md section 6i): the TUPLE prediction for the runner's
own scene, computed from a HAND-MODEL of every submit's expected writes BEFORE the runner is typed (print-then-type). The
model consults the OP CLASS of every effect from the registry itself (S1's lesson) and the WRITE TIME of the two timers
(O7's): the reprieve of a hundred and twenty years is due beyond the bare scene's end (set, not written); the seven days'
reprieve is due inside it (set, fired, written as a timer entry — not open). The scene's rows (subject -> the effects the
daemon writes per the declaration 6d) and the slot order are fixed HERE; the runner types them."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import yaml
FX = yaml.safe_load(open((_ROOT + '/World/step9/effect_vocabulary.yaml'), encoding='utf-8'))['effects']
OP = {k: v['ledger_op'] for k, v in FX.items()}
# ---- the rows in the text's order: (subject, effect, count) — every write the daemon makes on the bare scene ----
ROWS = [
 # Gen 2
 ('adam', 'living_soul', 1), ('adam', 'to_work_and_keep', 1), ('the-beasts', 'name_given', 1), ('adam', 'deep_sleep_fell', 1), ('adam', 'dread_and_darkness', 0), ('adam', 'helper_made', 1),
 ('eve', 'name_given', 2),                                   # 2:23 'she shall be called Woman', 3:20 'Eve'
 # Gen 3
 ('eve', 'breached_the_first_rule', 1), ('adam', 'breached_the_first_rule', 1), ('adam-and-eve', 'eyes_opened', 1), ('adam-and-eve', 'girdles_made', 1), ('eve', 'deceived', 1),
 ('the-serpent', 'serpent_cursed', 1), ('the-serpent', 'enmity_set', 1), ('eve', 'pain_multiplied', 1), ('eve', 'ruled_by_the_husband', 1), ('the-ground', 'ground_cursed', 1),
 ('adam', 'sweat_bread', 1), ('adam', 'return_to_dust', 1), ('adam-and-eve', 'clothed_in_skins', 1), ('adam-and-eve', 'expelled', 1), ('the-garden', 'way_guarded', 1),
 # Gen 4
 ('cain', 'begotten', 1), ('abel', 'begotten', 1), ('cain', 'not_regarded', 1), ('abel', 'regarded', 1), ('cain', 'sin_at_the_door', 1), ('abel', 'slain', 1), ('cain', 'bloods_cry', 1),
 ('cain', 'cursed_from_the_ground', 1), ('cain', 'fugitive_and_wanderer', 1), ('cain', 'mark_set', 1), ('cain', 'sevenfold_vengeance', 1), ('cain', 'settled_in_nod', 1),
 ('enoch-son-of-cain', 'begotten', 1), ('the-city-of-enoch', 'city_built', 1), ('the-city-of-enoch', 'name_given', 1),
 ('irad', 'begotten', 1), ('mehujael', 'begotten', 1), ('methushael', 'begotten', 1), ('lamech-son-of-methushael', 'begotten', 1),
 ('adah', 'wife_taken', 1), ('zillah', 'wife_taken', 1), ('jabal', 'begotten', 1), ('tubal-cain', 'begotten', 1), ('lamech-son-of-methushael', 'seventy_sevenfold_claimed', 1),
 ('seth', 'begotten', 2),                                    # 4:25 Eve bore; 5:3 Adam begot — the ink's two statements, two parents
 ('seth', 'name_given', 2),                                  # 4:25 by Eve, 5:3 by Adam
 ('enosh', 'name_given', 1), ('the-generation-of-enosh', 'idolatry_begun', 1),
 # Gen 5
 ('adam-and-eve', 'name_given', 1),                          # 5:2 'called their name Adam'
 ('enosh', 'begotten', 1), ('kenan', 'begotten', 1), ('mahalalel', 'begotten', 1), ('jared', 'begotten', 1), ('enoch', 'begotten', 1), ('methuselah', 'begotten', 1), ('lamech', 'begotten', 1),
 ('enoch', 'taken_by_god', 1), ('noah', 'begotten', 1), ('noah', 'name_given', 1), ('noah', 'comfort_named', 0),
 ('shem', 'begotten', 1), ('ham', 'begotten', 1), ('japheth', 'begotten', 1),
 # Gen 6
 ('humankind', 'multiplied_on_the_earth', 1), ('the-daughters-of-men', 'wife_taken', 1), ('the-generation-of-the-flood', 'reprieve_of_a_hundred_and_twenty', 0),   # due beyond the scene: a timer set, never written
 ('humankind', 'wickedness_great', 1), ('god', 'regretted_making_man', 1), ('the-generation-of-the-flood', 'to_be_wiped', 1), ('noah', 'found_favor', 1),
 ('the-earth', 'earth_corrupted', 1), ('the-generation-of-the-flood', 'sealed_for_violence', 1), ('noah', 'ark_owed', 1), ('the-ark', 'ark_spec', 1), ('noah', 'covenant_promised', 1), ('the-ark', 'ark_built', 1),
 # Gen 7
 ('noah', 'boarding_owed', 1), ('the-generation-of-the-flood', 'seven_days_reprieve', 1),   # due inside the scene: set and FIRED — written at the fire (a timer entry, not open)
 ('noah-and-sons', 'in_the_ark', 1), ('noah-and-sons', 'ark_intercourse_barred', 1), ('noah', 'shut_in', 1), ('the-earth', 'fountains_split', 1),
 ('the-generation-of-the-flood', 'wiped_out', 1), ('noah', 'only_noah_remained', 1), ('the-generation-of-the-flood', 'no_share_in_the_world_to_come', 1), ('the-earth', 'waters_prevailed_a_hundred_and_fifty', 1),
 # Gen 8
 ('noah', 'remembered_by_god', 1), ('the-earth', 'waters_receding', 1), ('the-ark', 'rested_on_ararat', 1), ('the-raven', 'raven_sent', 1), ('the-dove', 'dove_returned', 3), ('noah', 'ground_seen_dry', 1),
 ('noah', 'exit_owed', 1), ('noah-and-sons', 'intercourse_permitted', 1), ('noah-and-sons', 'out_of_the_ark', 1), ('the-altar-of-noah', 'altar_built', 1), ('noah', 'olah_offered', 1), ('god', 'savor_smelled', 1),
 ('the-ground', 'ground_not_cursed_again', 1), ('the-earth', 'seasons_pledged', 1),
 # Gen 9:18-29
 ('noah', 'vineyard_planted', 1), ('noah', 'drunk', 1), ('noah', 'uncovered', 1), ('ham', 'saw_and_told', 1), ('shem-and-japheth', 'covered_the_father', 1), ('canaan', 'canaan_cursed', 1),
 ('shem', 'shem_blessed', 1), ('japheth', 'japheth_enlarged', 1),
 # Gen 10
 ('nimrod', 'begotten', 1), ('nimrod', 'kingdom_founded', 1), ('asshur', 'cities_built', 1), ('peleg', 'begotten', 1), ('joktan', 'begotten', 1), ('peleg', 'peleg_named_for_the_division', 1),
 # Gen 11
 ('the-builders', 'encamped_at', 1), ('the-builders', 'tower_undertaken', 1), ('the-city-and-tower', 'descended_to_see', 1), ('the-builders', 'language_confounded', 1), ('the-builders', 'scattered', 1),
 ('the-city-and-tower', 'building_ceased', 1), ('the-builders', 'no_share_in_the_world_to_come', 1), ('the-city-and-tower', 'name_given', 1),
 ('arpachshad', 'begotten', 1), ('shelah', 'begotten', 1), ('eber', 'begotten', 1), ('reu', 'begotten', 1), ('serug', 'begotten', 1), ('nahor', 'begotten', 1), ('terah', 'begotten', 1),
 ('abram', 'begotten', 1), ('nahor-son-of-terah', 'begotten', 1), ('haran', 'begotten', 1), ('lot', 'begotten', 1), ('haran', 'died_before_his_father', 1),
 ('sarai', 'wife_taken', 1), ('milcah', 'wife_taken', 1), ('sarai', 'barren', 1), ('terah', 'encamped_at', 1),
 # Gen 12
 ('abram', 'go_owed', 1), ('abram', 'great_nation_promised', 1), ('abram', 'blessing_promised', 1), ('abram', 'encamped_at', 8),   # 12:5, 12:6, 12:8, 12:9, 12:10, 13:1-3, 13:18 = 7 ... and Hebron counted: see the list in the runner
 ('abram', 'land_promised', 3), ('the-altar-at-shechem', 'altar_built', 1), ('the-altar-at-bethel', 'altar_built', 1), ('abram', 'called_on_the_name', 2), ('the-land-of-canaan', 'famine', 1),
 ('sarai', 'presented_as_sister', 1), ('sarai', 'taken_to_pharaohs_house', 1), ('abram', 'enriched_for_her_sake', 1), ('pharaoh-of-abram', 'plague_struck', 1), ('abram', 'sent_out', 1),
 # Gen 13
 ('the-herdsmen', 'strife_between_herdsmen', 1), ('lot', 'chose_the_plain', 1), ('abram', 'parted', 1), ('lot', 'parted', 1), ('lot', 'encamped_at', 1), ('the-men-of-sodom', 'no_share_in_the_world_to_come', 1),
 ('abram', 'seed_as_dust', 1), ('abram', 'land_walk_commanded', 1), ('the-altar-at-hebron', 'altar_built', 1),
 # Gen 14
 ('the-five-kings', 'rebelled', 1), ('the-five-kings', 'defeated', 1), ('lot', 'taken_captive', 1), ('abram', 'called_the_hebrew', 1), ('abram', 'muster_of_three_hundred_and_eighteen', 1), ('abram', 'night_divided', 1),
 ('the-four-kings', 'kings_smitten', 1), ('the-king-of-sodom', 'goods_brought_back', 1), ('abram', 'bread_and_wine', 1), ('abram', 'blessed_by_the_priest', 1), ('melchizedek', 'priesthood_removed', 1),
 ('abram', 'tithe_given', 1), ('abram', 'sworn_to_take_nothing', 1), ('the-allies', 'portion_reserved', 1),
 # Gen 15
 ('abram', 'shield_promised', 1), ('abram', 'childless', 1), ('abram', 'heir_from_the_loins', 1), ('abram', 'seed_as_stars', 1), ('abram', 'believed', 1), ('abram', 'reckoned_righteousness', 1),
 ('abram', 'brought_out_of_ur', 1), ('abram', 'pieces_owed', 1), ('the-pieces', 'pieces_cut', 1), ('abram', 'deep_sleep_fell', 1), ('abram', 'dread_and_darkness', 1),
 ('the-seed-of-abraham', 'seed_to_serve_four_hundred', 1), ('the-seed-of-abraham', 'nation_to_be_judged', 1), ('the-seed-of-abraham', 'to_go_out_with_substance', 1), ('abram', 'buried_in_peace', 1),
 ('the-seed-of-abraham', 'fourth_generation_return', 1), ('the-amorite', 'amorite_not_full', 1), ('the-pieces', 'passed_between_the_pieces', 1), ('abram', 'covenant_cut', 1), ('the-seed-of-abraham', 'land_granted', 1),
 # Gen 16
 ('hagar', 'wife_taken', 1), ('sarai', 'ten_years_childless', 1), ('hagar', 'conceived', 1), ('hagar', 'mistress_despised', 1), ('sarai', 'judgment_invoked', 1), ('hagar', 'afflicted', 1),
 ('hagar', 'fled_from_the_mistress', 1), ('hagar', 'return_owed', 1), ('hagar', 'seed_multiplied', 1), ('hagar', 'ishmael_announced', 1), ('ishmael', 'wild_ass_of_a_man', 1),
 ('god', 'name_given', 1), ('the-well-lachai-roi', 'name_given', 1), ('ishmael', 'begotten', 1), ('ishmael', 'name_given', 1),
]
# the stations of Abram on the bare scene (the runner's list): Canaan 12:5, Shechem 12:6, Bethel 12:8, the Negev 12:9, Egypt 12:10, Bethel again 13:1-3, Hebron 13:18 = SEVEN — the row above says 8: CORRECTED here, in the open
FIX = {('abram', 'encamped_at'): 7}
# comfort_named: no watch writes it in 6d (the naming's reason rides name_given's value) — 0; dread_and_darkness on adam — 0 (the 2:21 seat is the sleep of sleep, not the dread)
counts = {}
for s, e, n in ROWS:
    counts[(s, e)] = counts.get((s, e), 0) + n
counts.update(FIX)
SLOTS = [k for k in dict.fromkeys((s, e) for s, e, n in ROWS) if counts[k] > 0]
tup = tuple(counts[k] for k in SLOTS)
# ---- THE OPENS at the scene's end: the closable ops (debit / heaven / body) written, minus the closes the scene performs ----
CLOSES = [('noah', 'ark_owed', 'Gen 6:22'), ('noah', 'boarding_owed', 'Gen 7:7'), ('the-generation-of-the-flood', 'to_be_wiped', 'Gen 7:23'), ('noah', 'exit_owed', 'Gen 8:18'),
          ('noah', 'covenant_promised', 'Gen 9:11'), ('abram', 'go_owed', 'Gen 12:4'), ('sarai', 'taken_to_pharaohs_house', 'Gen 12:20'), ('lot', 'taken_captive', 'Gen 14:16'),
          ('abram', 'pieces_owed', 'Gen 15:10'), ('abram', 'land_promised', 'Gen 15:18'), ('abram', 'land_promised', 'Gen 15:18'), ('abram', 'land_promised', 'Gen 15:18'),
          ('abram', 'childless', 'Gen 16:15'), ('hagar', 'ishmael_announced', 'Gen 16:15')]
open_total = 0
for (s, e), n in counts.items():
    if OP[e] in ('debit', 'heaven', 'body'):
        open_total += n
for s, e, _ in CLOSES:
    assert OP[e] in ('debit', 'heaven', 'body'), (e, OP[e])
    open_total -= 1
tset = 2      # reprieve_of_a_hundred_and_twenty (beyond the end), seven_days_reprieve (inside)
fired = 1     # the seven days
closes = len(CLOSES)
day = 366
PRED = tup + (open_total, tset, fired, closes, day)
print('PREDICTED primeval SCENE (%d slots = %d effect slots + opens, set, fired, closes, day) = %r' % (len(PRED), len(SLOTS), PRED))
print('opens by op:', sorted(((s, e), n) for (s, e), n in counts.items() if OP[e] in ('debit', 'heaven', 'body') and n))
print('the slot names, for the runner:'); print(SLOTS)
