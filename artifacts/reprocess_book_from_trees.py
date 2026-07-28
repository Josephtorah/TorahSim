#!/usr/bin/env python3
"""
Tree-first reprocess for Genesis / Leviticus / Numbers / Deuteronomy (tree_derived_v1).

Order: Hebrew verse → ta'amim tree v1 → top-split arms → one STEP per verse
       → maps_to → tree_coverage.

For Deuteronomy (and any unit listed in UNIT_SPECS), first-draft meta may come
from UNIT_SPECS when no prior YAML exists — full tree_derived unit is written.

Not binding law. English [EN-AID] only.
See reviews/*_TREE_DERIVE_*.md
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from taamim_tree_parse import parse_verse, tree_ascii_string, strip_taamim_and_points  # noqa: E402

UNITS = ROOT / "logic" / "units"

BOOKS: dict[str, dict[str, Any]] = {
    "gen": {
        "osis": "Gen",
        "prefix": "gen",
        "step_prefix": "STEP_Gn",
        "book_he": "בְּרֵאשִׁית",
        "book_tr": "Be-reshit",
        "book_en": "Genesis",
        "data": "Data/Gen.xml",
        "build_track": "genesis_stack",
        "oral_name": "Bereshit Rabbah / midrash",
        "oral_file": ROOT / "Data" / "bereshit_rabbah_he.json",  # optional; empty ok
        "oral_tag": "[BR]",
        "counts": {
            1: 31, 2: 25, 3: 24, 4: 26, 5: 32, 6: 22, 7: 24, 8: 22, 9: 29, 10: 32,
            11: 32, 12: 20, 13: 18, 14: 24, 15: 21, 16: 16, 17: 27, 18: 33, 19: 38, 20: 18,
            21: 34, 22: 24, 23: 20, 24: 67, 25: 34, 26: 35, 27: 46, 28: 22, 29: 35, 30: 43,
            31: 54, 32: 33, 33: 20, 34: 31, 35: 29, 36: 43, 37: 36, 38: 30, 39: 23, 40: 23,
            41: 57, 42: 38, 43: 34, 44: 34, 45: 28, 46: 34, 47: 31, 48: 22, 49: 33, 50: 26,
        },
        # Phases align with ARCHITECTURE_genesis_stack packages
        "phases": {
            "A": [  # Package 0 — creation week
                "gen_01_creation_boot",
                "gen_01_day2_raqia",
                "gen_01_day3_land_plants",
                "gen_01_day4_lights",
                "gen_01_day5_sea_birds",
                "gen_01_day6_land_human",
                "gen_01_day7_shabbat",
            ],
            "B": ["gen_02_03_garden"],
            "C": ["gen_04_05_early_humanity"],
            "D": ["gen_06_09_flood_covenant"],
            "E": ["gen_10_11_nations_babel"],
            "F": [  # Abraham package
                "gen_12_14_call_and_lot",
                "gen_15_17_covenant_brit",
                "gen_18_19_sodom",
                "gen_20_22_isaac_binding",
                "gen_23_25_abraham_close",
            ],
            "G": [  # Isaac / Jacob
                "gen_26_isaac",
                "gen_27_28_blessing_bethel",
                "gen_29_30_laban_children",
                "gen_31_33_return_esau",
                "gen_34_36_shechem_edom",
            ],
            "H": [  # Joseph → Egypt handoff
                "gen_37_38_sold_judah",
                "gen_39_41_egypt_rise",
                "gen_42_45_brothers",
                "gen_46_47_migrate",
                "gen_48_50_blessings_death",
            ],
        },
    },
    "lev": {
        "osis": "Lev",
        "prefix": "lev",
        "step_prefix": "STEP_Lv",
        "book_he": "וַיִּקְרָא",
        "book_tr": "Vayikra",
        "book_en": "Leviticus",
        "data": "Data/Lev.xml",
        "build_track": "leviticus_apps",
        "oral_name": "Sifra",
        "oral_file": ROOT / "Data" / "sifra_he.json",
        "oral_tag": "[SIFRA]",
        "counts": {
            1: 17, 2: 16, 3: 17, 4: 35, 5: 26, 6: 23, 7: 38, 8: 36, 9: 24, 10: 20,
            11: 47, 12: 8, 13: 59, 14: 57, 15: 33, 16: 34, 17: 16, 18: 30, 19: 37,
            20: 27, 21: 24, 22: 33, 23: 44, 24: 23, 25: 55, 26: 46, 27: 34,
        },
        "phases": {
            "A": [  # offerings 1–7
                "lev_01_call_and_korban_opening",
                "lev_01_olah_cattle_procedure",
                "lev_01_olah_flock",
                "lev_01_olah_bird",
                "lev_02_minchah",
                "lev_03_shelamim",
                "lev_04_chatat_priest",
                "lev_04_chatat_congregation",
                "lev_04_chatat_leader",
                "lev_04_chatat_common",
                "lev_05_asham_graded",
                "lev_05_asham_sancta",
                "lev_06_olah_minchah_torah",
                "lev_07_asham_procedure",
                "lev_07_shelamim_types",
                "lev_07_fat_blood_dues",
            ],
            "B": [  # 8–10
                "lev_08_milluim",
                "lev_09_eighth_day",
                "lev_10_nadav_avihu",
            ],
            "C": [  # 11–15
                "lev_11_animals_water_birds",
                "lev_11_carcass_swarm_close",
                "lev_12_childbirth",
                "lev_13_skin_initial",
                "lev_13_boil_burn",
                "lev_13_head_isolation",
                "lev_13_garment",
                "lev_14_metzora_cleanse",
                "lev_14_house_nega",
                "lev_15_male_discharge",
                "lev_15_female_discharge",
            ],
            "D": ["lev_16_yk_entry_blood", "lev_16_yk_goat_statute", "lev_17_blood_center"],
            "E": [
                "lev_18_sexual_land",
                "lev_19_holiness_neighbor",
                "lev_19_mixtures_weights",
                "lev_20_sanctions",
            ],
            "F": [
                "lev_21_priest_family",
                "lev_21_priest_blemish",
                "lev_22_holy_food",
                "lev_22_acceptable_offerings",
            ],
            "G": [
                "lev_23_spring_festivals",
                "lev_23_fall_festivals",
                "lev_24_lamp_bread",
                "lev_24_blasphemer_talion",
            ],
            "H": [
                "lev_25_shemittah",
                "lev_25_redeem_poor",
                "lev_25_slave_jubilee",
                "lev_26_bless_curse",
                "lev_27_vows_valuations",
            ],
        },
    },
    "num": {
        "osis": "Num",
        "prefix": "num",
        "step_prefix": "STEP_Nm",
        "book_he": "בְּמִדְבַּר",
        "book_tr": "Be-midbar",
        "book_en": "Numbers",
        "data": "Data/Num.xml",
        "build_track": "numbers_ops",
        "oral_name": "Sifrei Bamidbar",
        "oral_file": ROOT / "Data" / "sifrei_bamidbar_he.json",
        "oral_tag": "[SIFREI]",
        "counts": {
            1: 54, 2: 34, 3: 51, 4: 49, 5: 31, 6: 27, 7: 89, 8: 26, 9: 23, 10: 36,
            11: 35, 12: 16, 13: 33, 14: 45, 15: 41, 16: 35, 17: 28, 18: 32, 19: 22, 20: 29,
            21: 35, 22: 41, 23: 30, 24: 25, 25: 19, 26: 65, 27: 23, 28: 31, 29: 39, 30: 17,
            31: 54, 32: 42, 33: 56, 34: 29, 35: 34, 36: 13,
        },
        "phases": {
            "A": [
                "num_01_census_command",
                "num_01_tribe_counts",
                "num_01_levites_exempt",
                "num_02_camp_east_south",
                "num_02_camp_west_north",
                "num_03_aaron_levi_replace",
                "num_03_levite_clans_count",
                "num_03_firstborn_redeem",
                "num_04_kehat",
                "num_04_gershon_merari",
            ],
            "B": [
                "num_05_camp_pure_theft",
                "num_05_sotah",
                "num_06_nazir",
                "num_06_priest_blessing",
                "num_07_carts_offerings_a",
                "num_07_offerings_b_total",
            ],
            "C": [
                "num_08_menorah_levites",
                "num_09_pesach_cloud",
                "num_10_trumpets_depart",
            ],
            "D": [
                "num_11_complaint_quail",
                "num_12_miriam",
                "num_13_spies_sent",
                "num_14_rejection",
            ],
            "E": [
                "num_15_offerings_laws",
                "num_15_wood_tzitzit",
                "num_16_korach",
                "num_17_plague_staff",
            ],
            "F": ["num_18_priest_levite_dues", "num_19_parah"],
            "G": ["num_20_meribah_edom_aaron", "num_21_snakes_conquest"],
            "H": [
                "num_22_balak_bilam_call",
                "num_23_oracles_1_2",
                "num_24_oracles_3_4",
            ],
            "I": [
                "num_25_peor_pinchas",
                "num_26_second_census",
                "num_27_zelophehad_joshua",
            ],
            "J": [
                "num_28_daily_shabbat_rosh",
                "num_28_pesach_shavuot",
                "num_29_fall_festivals",
                "num_30_vows",
            ],
            "K": [
                "num_31_midian",
                "num_32_gad_reuben",
                "num_33_journeys",
            ],
            "L": [
                "num_34_borders",
                "num_35_refuge_cities",
                "num_36_heiresses",
            ],
        },
    },
    "deu": {
        "osis": "Deut",
        "prefix": "deu",
        "step_prefix": "STEP_Dt",
        "book_he": "דְּבָרִים",
        "book_tr": "Devarim",
        "book_en": "Deuteronomy",
        "data": "Data/Deut.xml",
        "build_track": "deuteronomy_recompile",
        "oral_name": "Sifrei Devarim",
        "oral_file": ROOT / "Data" / "sifrei_devarim_he.json",
        "oral_tag": "[SIFREI-D]",
        "counts": {
            1: 46, 2: 37, 3: 29, 4: 49, 5: 33, 6: 25, 7: 26, 8: 20, 9: 29, 10: 22,
            11: 32, 12: 31, 13: 19, 14: 29, 15: 23, 16: 22, 17: 20, 18: 22, 19: 21, 20: 20,
            21: 23, 22: 29, 23: 26, 24: 22, 25: 19, 26: 19, 27: 26, 28: 69, 29: 28, 30: 20,
            31: 30, 32: 52, 33: 29, 34: 12,
        },
        # 10 phases (owner choice 2026-07-24): A–J
        "phases": {
            "A": [  # 1–3 historical prologue
                "deu_01_frame_officers",
                "deu_01_spies_refuse",
                "deu_02_bypass_nations",
                "deu_02_sihon",
                "deu_03_og_gilead",
                "deu_03_moses_barred",
            ],
            "B": [  # 4–6 law frame / Decalogue / Shema
                "deu_04_obey_horeb",
                "deu_04_refuge_east",
                "deu_05_decalogue",
                "deu_06_shema",
            ],
            "C": [  # 7–11 loyalty / land / second tablets
                "deu_07_nations_cherem",
                "deu_08_manna_humility",
                "deu_09_not_righteousness",
                "deu_10_second_tablets",
                "deu_11_bless_curse_set",
            ],
            "D": [  # 12–14 centralization / seducers / food-tithe
                "deu_12_place_name",
                "deu_13_seducers",
                "deu_14_food_tithe",
            ],
            "E": [  # 15–18 release / festivals / king / prophet
                "deu_15_release_firstborn",
                "deu_16_festivals_judges",
                "deu_17_courts_king",
                "deu_18_levi_prophet",
            ],
            "F": [  # 19–22 refuge / war / family / social
                "deu_19_miklat_witness",
                "deu_20_war_rules",
                "deu_21_eglah_family",
                "deu_22_return_sex_laws",
            ],
            "G": [  # 23–26 assembly / divorce / courts / firstfruits
                "deu_23_qahal_purity_vows",
                "deu_24_divorce_poor",
                "deu_25_courts_yibbum",
                "deu_26_bikkurim_close",
            ],
            "H": [  # 27–28 ceremony + blessings/curses
                "deu_27_ebal_curses",
                "deu_28_blessings",
                "deu_28_curses_a",
                "deu_28_curses_b",
            ],
            "I": [  # 29–30 Moab covenant
                "deu_29_moab_covenant",
                "deu_30_teshuvah_choice",
            ],
            "J": [  # 31–34 succession / song / blessing / death
                "deu_31_charge_torah",
                "deu_32_haazinu",
                "deu_32_song_aftermath",
                "deu_33_ve_zot",
                "deu_34_moses_death",
            ],
        },
    },
}

# First-draft unit specs (used when no prior YAML exists). reprocess rewrites full tree_derived_v1.
# Keys: unit_id → meta fields required by emit_unit.
UNIT_SPECS: dict[str, dict[str, Any]] = {
    # --- Phase A: 1–3 ---
    "deu_01_frame_officers": {
        "refs": "1:1-18",
        "title_en": "These words; Horeb frame; officers appointed (1:1–18)",
        "title_he": "אֵלֶּה הַדְּבָרִים",
        "title_he_translit": "eleh ha-devarim",
        "title_he_en": "These are the words",
        "genre": "narrative_fsm",
        "depends_on": ["num_36_heiresses", "exo_18_yitro"],
    },
    "deu_01_spies_refuse": {
        "refs": "1:19-46",
        "title_en": "Kadesh; spies; refusal; doomed generation (1:19–46)",
        "title_he": "וַתִּקְרְבוּן",
        "title_he_translit": "va-tikrevun",
        "title_he_en": "And you approached",
        "genre": "narrative_fsm",
        "depends_on": ["deu_01_frame_officers", "num_13_spies_sent", "num_14_rejection"],
    },
    "deu_02_bypass_nations": {
        "refs": "2:1-25",
        "title_en": "Circuit Seir/Moab/Ammon; do not provoke kin nations (2:1–25)",
        "title_he": "וַנֵּפֶן וַנִּסַּע",
        "title_he_translit": "va-nefen va-nissa",
        "title_he_en": "And we turned and journeyed",
        "genre": "narrative_fsm",
        "depends_on": ["deu_01_spies_refuse"],
    },
    "deu_02_sihon": {
        "refs": "2:26-37",
        "title_en": "Sihon of Heshbon; war grant (2:26–37)",
        "title_he": "סִיחֹן מֶלֶךְ חֶשְׁבּוֹן",
        "title_he_translit": "sichon melech cheshbon",
        "title_he_en": "Sihon king of Heshbon",
        "genre": "narrative_fsm",
        "depends_on": ["deu_02_bypass_nations", "num_21_snakes_conquest"],
    },
    "deu_03_og_gilead": {
        "refs": "3:1-22",
        "title_en": "Og of Bashan; east allotment; charge to Joshua (3:1–22)",
        "title_he": "עוֹג מֶלֶךְ הַבָּשָׁן",
        "title_he_translit": "og melech ha-bashan",
        "title_he_en": "Og king of the Bashan",
        "genre": "narrative_fsm",
        "depends_on": ["deu_02_sihon", "num_32_gad_reuben"],
    },
    "deu_03_moses_barred": {
        "refs": "3:23-29",
        "title_en": "Moses pleads; barred from land; view from Pisgah (3:23–29)",
        "title_he": "וָאֶתְחַנַּן",
        "title_he_translit": "va-etchanan",
        "title_he_en": "And I pleaded",
        "genre": "narrative_fsm",
        "depends_on": ["deu_03_og_gilead"],
    },
    # --- Phase B: 4–6 ---
    "deu_04_obey_horeb": {
        "refs": "4:1-40",
        "title_en": "Hear statutes; Horeb theophany; no image; YHWH alone (4:1–40)",
        "title_he": "וְעַתָּה יִשְׂרָאֵל שְׁמַע",
        "title_he_translit": "ve-atah yisrael shema",
        "title_he_en": "And now Israel hear",
        "genre": "decision_table",
        "depends_on": ["deu_03_moses_barred", "exo_20_decalogue_altar"],
    },
    "deu_04_refuge_east": {
        "refs": "4:41-49",
        "title_en": "Three east refuge cities; frame of this torah (4:41–49)",
        "title_he": "אָז יַבְדִּיל מֹשֶׁה",
        "title_he_translit": "az yavdil mosheh",
        "title_he_en": "Then Moses set apart",
        "genre": "boot_steps",
        "depends_on": ["deu_04_obey_horeb", "num_35_refuge_cities"],
    },
    "deu_05_decalogue": {
        "refs": "5:1-33",
        "title_en": "Covenant at Horeb; Decalogue restatement; mediate (5:1–33)",
        "title_he": "שְׁמַע יִשְׂרָאֵל אֶת־הַחֻקִּים",
        "title_he_translit": "shema yisrael et-ha-chukkim",
        "title_he_en": "Hear Israel the statutes",
        "genre": "decision_table",
        "depends_on": ["deu_04_refuge_east", "exo_20_decalogue_altar"],
    },
    "deu_06_shema": {
        "refs": "6:1-25",
        "title_en": "Shema; love; teach; when you enter; not test (6:1–25)",
        "title_he": "שְׁמַע יִשְׂרָאֵל",
        "title_he_translit": "shema yisrael",
        "title_he_en": "Hear O Israel",
        "genre": "decision_table",
        "depends_on": ["deu_05_decalogue"],
    },
    # --- Phase C: 7–11 ---
    "deu_07_nations_cherem": {
        "refs": "7:1-26",
        "title_en": "Seven nations; cherem; not for your greatness (7:1–26)",
        "title_he": "כִּי יְבִיאֲךָ",
        "title_he_translit": "ki yevi'acha",
        "title_he_en": "When He brings you",
        "genre": "decision_table",
        "depends_on": ["deu_06_shema"],
    },
    "deu_08_manna_humility": {
        "refs": "8:1-20",
        "title_en": "Remember wilderness; manna; do not forget (8:1–20)",
        "title_he": "כָּל־הַמִּצְוָה",
        "title_he_translit": "kol-ha-mitzvah",
        "title_he_en": "All the commandment",
        "genre": "decision_table",
        "depends_on": ["deu_07_nations_cherem", "exo_16_manna_shabbat"],
    },
    "deu_09_not_righteousness": {
        "refs": "9:1-29",
        "title_en": "Not your righteousness; calf; Moses intercedes (9:1–29)",
        "title_he": "לֹא בְצִדְקָתְךָ",
        "title_he_translit": "lo ve-tzidkatecha",
        "title_he_en": "Not by your righteousness",
        "genre": "narrative_fsm",
        "depends_on": ["deu_08_manna_humility", "exo_32_golden_calf"],
    },
    "deu_10_second_tablets": {
        "refs": "10:1-22",
        "title_en": "Second tablets; ark; Levi; circumcise heart (10:1–22)",
        "title_he": "בָּעֵת הַהִוא אָמַר",
        "title_he_translit": "ba-et ha-hi amar",
        "title_he_en": "At that time He said",
        "genre": "boot_steps",
        "depends_on": ["deu_09_not_righteousness", "exo_34_second_tablets"],
    },
    "deu_11_bless_curse_set": {
        "refs": "11:1-32",
        "title_en": "Love and keep; rain; bless/curse set on mountains (11:1–32)",
        "title_he": "וְאָהַבְתָּ אֵת יְהוָה",
        "title_he_translit": "ve-ahavta et YHWH",
        "title_he_en": "And you shall love YHWH",
        "genre": "decision_table",
        "depends_on": ["deu_10_second_tablets"],
    },
    # --- Phase D: 12–14 ---
    "deu_12_place_name": {
        "refs": "12:1-31",
        "title_en": "Destroy high places; the place He chooses; blood/meat rules (12:1–31)",
        "title_he": "הַמָּקוֹם אֲשֶׁר־יִבְחַר",
        "title_he_translit": "ha-makom asher-yivchar",
        "title_he_en": "The place that He will choose",
        "genre": "decision_table",
        "depends_on": ["deu_11_bless_curse_set", "lev_17_blood_center"],
    },
    "deu_13_seducers": {
        "refs": "13:1-19",
        "title_en": "False prophet; family seducer; apostate city (13:1–19)",
        "title_he": "כִּי־יָקוּם בְּקִרְבְּךָ נָבִיא",
        "title_he_translit": "ki-yakum be-kirbecha navi",
        "title_he_en": "If a prophet arises in your midst",
        "genre": "decision_table",
        "depends_on": ["deu_12_place_name"],
    },
    "deu_14_food_tithe": {
        "refs": "14:1-29",
        "title_en": "Holy people; clean animals; tithe year cycle (14:1–29)",
        "title_he": "בָּנִים אַתֶּם לַיהוָה",
        "title_he_translit": "banim atem la-YHWH",
        "title_he_en": "You are children to YHWH",
        "genre": "decision_table",
        "depends_on": ["deu_13_seducers", "lev_11_animals_water_birds"],
    },
    # --- Phase E: 15–18 ---
    "deu_15_release_firstborn": {
        "refs": "15:1-23",
        "title_en": "Shemittah release; open hand; Hebrew slave; firstborn (15:1–23)",
        "title_he": "מִקֵּץ שֶׁבַע־שָׁנִים",
        "title_he_translit": "mi-ketz sheva-shanim",
        "title_he_en": "At the end of seven years",
        "genre": "decision_table",
        "depends_on": ["deu_14_food_tithe", "lev_25_shemittah", "exo_21_slave_person"],
    },
    "deu_16_festivals_judges": {
        "refs": "16:1-22",
        "title_en": "Pesach/Shavuot/Sukkot; judges; no asherah/pillar (16:1–22)",
        "title_he": "שָׁמוֹר אֶת־חֹדֶשׁ הָאָבִיב",
        "title_he_translit": "shamor et-chodesh ha-aviv",
        "title_he_en": "Keep the month of Aviv",
        "genre": "decision_table",
        "depends_on": ["deu_15_release_firstborn", "lev_23_spring_festivals", "lev_23_fall_festivals"],
    },
    "deu_17_courts_king": {
        "refs": "17:1-20",
        "title_en": "Blemished offering ban; court; king law (17:1–20)",
        "title_he": "שׂוֹם תָּשִׂים עָלֶיךָ מֶלֶךְ",
        "title_he_translit": "som tasim alecha melech",
        "title_he_en": "You shall surely set a king over you",
        "genre": "decision_table",
        "depends_on": ["deu_16_festivals_judges"],
    },
    "deu_18_levi_prophet": {
        "refs": "18:1-22",
        "title_en": "Levi portion; abominations ban; prophet like Moses (18:1–22)",
        "title_he": "נָבִיא מִקִּרְבְּךָ",
        "title_he_translit": "navi mi-kirbecha",
        "title_he_en": "A prophet from your midst",
        "genre": "decision_table",
        "depends_on": ["deu_17_courts_king", "num_18_priest_levite_dues"],
    },
    # --- Phase F: 19–22 ---
    "deu_19_miklat_witness": {
        "refs": "19:1-21",
        "title_en": "Cities of refuge west; boundary; witnesses; talion (19:1–21)",
        "title_he": "שָׁלוֹשׁ עָרִים תַּבְדִּיל",
        "title_he_translit": "shalosh arim tavdil",
        "title_he_en": "Three cities you shall set apart",
        "genre": "decision_table",
        "depends_on": ["deu_18_levi_prophet", "num_35_refuge_cities", "deu_04_refuge_east"],
    },
    "deu_20_war_rules": {
        "refs": "20:1-20",
        "title_en": "War exemptions; peace offer; cherem cities; trees (20:1–20)",
        "title_he": "כִּי־תֵצֵא לַמִּלְחָמָה",
        "title_he_translit": "ki-tetze la-milchamah",
        "title_he_en": "When you go out to war",
        "genre": "decision_table",
        "depends_on": ["deu_19_miklat_witness"],
    },
    "deu_21_eglah_family": {
        "refs": "21:1-23",
        "title_en": "Eglah arufah; captive woman; inheritance; rebel son; hanging (21:1–23)",
        "title_he": "עֶגְלָה עֲרוּפָה",
        "title_he_translit": "eglah arufah",
        "title_he_en": "Broken-neck heifer (unsolved murder)",
        "genre": "decision_table",
        "depends_on": ["deu_20_war_rules"],
    },
    "deu_22_return_sex_laws": {
        "refs": "22:1-29",
        "title_en": "Return lost; mixtures; tzitzit; sexual/marriage cases (22:1–29)",
        "title_he": "לֹא־תִרְאֶה אֶת־שׁוֹר",
        "title_he_translit": "lo-tir'eh et-shor",
        "title_he_en": "You shall not see the ox",
        "genre": "decision_table",
        "depends_on": ["deu_21_eglah_family", "num_15_wood_tzitzit"],
    },
    # --- Phase G: 23–26 ---
    "deu_23_qahal_purity_vows": {
        "refs": "23:1-26",
        "title_en": "Assembly exclusions; camp purity; vows; neighbor produce (23:1–26)",
        "title_he": "לֹא־יָבֹא ... בִּקְהַל יְהוָה",
        "title_he_translit": "lo-yavo ... bi-kehal YHWH",
        "title_he_en": "Shall not enter the assembly of YHWH",
        "genre": "decision_table",
        "depends_on": ["deu_22_return_sex_laws"],
    },
    "deu_24_divorce_poor": {
        "refs": "24:1-22",
        "title_en": "Divorce bill; newlywed; pledges; wages; gleanings (24:1–22)",
        "title_he": "סֵפֶר כְּרִיתֻת",
        "title_he_translit": "sefer keritut",
        "title_he_en": "Document of cutting-off (divorce)",
        "genre": "decision_table",
        "depends_on": ["deu_23_qahal_purity_vows"],
    },
    "deu_25_courts_yibbum": {
        "refs": "25:1-19",
        "title_en": "Lashes limit; ox muzzle; yibbum; Amalek (25:1–19)",
        "title_he": "יִבּוּם",
        "title_he_translit": "yibbum",
        "title_he_en": "Levirate marriage duty",
        "genre": "decision_table",
        "depends_on": ["deu_24_divorce_poor", "exo_17_water_amalek"],
    },
    "deu_26_bikkurim_close": {
        "refs": "26:1-19",
        "title_en": "Firstfruits declaration; third-year tithe; covenant close (26:1–19)",
        "title_he": "בִּכּוּרִים",
        "title_he_translit": "bikkurim",
        "title_he_en": "Firstfruits",
        "genre": "decision_table",
        "depends_on": ["deu_25_courts_yibbum"],
    },
    # --- Phase H: 27–28 ---
    "deu_27_ebal_curses": {
        "refs": "27:1-26",
        "title_en": "Altar on Ebal; tribes on Gerizim/Ebal; twelve curses (27:1–26)",
        "title_he": "אָרוּר",
        "title_he_translit": "arur",
        "title_he_en": "Cursed",
        "genre": "boot_steps",
        "depends_on": ["deu_26_bikkurim_close", "deu_11_bless_curse_set"],
    },
    "deu_28_blessings": {
        "refs": "28:1-14",
        "title_en": "If you hearken: blessing cascade (28:1–14)",
        "title_he": "וְהָיָה אִם־שָׁמוֹעַ",
        "title_he_translit": "ve-hayah im-shamoa",
        "title_he_en": "And it shall be if you hearken",
        "genre": "decision_table",
        "depends_on": ["deu_27_ebal_curses", "lev_26_bless_curse"],
    },
    "deu_28_curses_a": {
        "refs": "28:15-44",
        "title_en": "If not hearken: curse cascade A (28:15–44)",
        "title_he": "וְהָיָה אִם־לֹא תִשְׁמַע",
        "title_he_translit": "ve-hayah im-lo tishma",
        "title_he_en": "And it shall be if you do not hearken",
        "genre": "decision_table",
        "depends_on": ["deu_28_blessings"],
    },
    "deu_28_curses_b": {
        "refs": "28:45-69",
        "title_en": "Curse cascade B; siege; exile; covenant words (28:45–69)",
        "title_he": "וּבָאוּ עָלֶיךָ כָּל־הַקְּלָלוֹת",
        "title_he_translit": "u-va'u alecha kol-ha-kelalot",
        "title_he_en": "And all the curses shall come upon you",
        "genre": "decision_table",
        "depends_on": ["deu_28_curses_a"],
    },
    # --- Phase I: 29–30 ---
    "deu_29_moab_covenant": {
        "refs": "29:1-28",
        "title_en": "Covenant in Moab; hidden/revealed; land warning (29:1–28)",
        "title_he": "אַתֶּם נִצָּבִים",
        "title_he_translit": "atem nitzavim",
        "title_he_en": "You are standing",
        "genre": "boot_steps",
        "depends_on": ["deu_28_curses_b"],
    },
    "deu_30_teshuvah_choice": {
        "refs": "30:1-20",
        "title_en": "Return; circumcise heart; life and death choice (30:1–20)",
        "title_he": "וְשַׁבְתָּ עַד־יְהוָה",
        "title_he_translit": "ve-shavta ad-YHWH",
        "title_he_en": "And you shall return to YHWH",
        "genre": "decision_table",
        "depends_on": ["deu_29_moab_covenant"],
    },
    # --- Phase J: 31–34 ---
    "deu_31_charge_torah": {
        "refs": "31:1-30",
        "title_en": "Joshua charged; Torah written; song as witness (31:1–30)",
        "title_he": "חִזְקוּ וְאִמְצוּ",
        "title_he_translit": "chizku ve-imtzu",
        "title_he_en": "Be strong and courageous",
        "genre": "narrative_fsm",
        "depends_on": ["deu_30_teshuvah_choice", "num_27_zelophehad_joshua"],
    },
    "deu_32_haazinu": {
        "refs": "32:1-43",
        "title_en": "Ha'azinu song (32:1–43)",
        "title_he": "הַאֲזִינוּ הַשָּׁמַיִם",
        "title_he_translit": "ha'azinu ha-shamayim",
        "title_he_en": "Give ear O heavens",
        "genre": "narrative_fsm",
        "depends_on": ["deu_31_charge_torah"],
    },
    "deu_32_song_aftermath": {
        "refs": "32:44-52",
        "title_en": "Song taught; ascend Abarim; view land (32:44–52)",
        "title_he": "וַיָּבֹא מֹשֶׁה",
        "title_he_translit": "va-yavo mosheh",
        "title_he_en": "And Moses came",
        "genre": "narrative_fsm",
        "depends_on": ["deu_32_haazinu"],
    },
    "deu_33_ve_zot": {
        "refs": "33:1-29",
        "title_en": "Moses' blessing of the tribes (33:1–29)",
        "title_he": "וְזֹאת הַבְּרָכָה",
        "title_he_translit": "ve-zot ha-berachah",
        "title_he_en": "And this is the blessing",
        "genre": "narrative_fsm",
        "depends_on": ["deu_32_song_aftermath", "gen_48_50_blessings_death"],
    },
    "deu_34_moses_death": {
        "refs": "34:1-12",
        "title_en": "Moses views land; dies; Joshua filled; no prophet like Moses (34:1–12)",
        "title_he": "וַיָּמָת שָׁם מֹשֶׁה",
        "title_he_translit": "va-yamot sham mosheh",
        "title_he_en": "And Moses died there",
        "genre": "narrative_fsm",
        "depends_on": ["deu_33_ve_zot"],
    },
}

_HE_MAP = {
    "א": "'", "ב": "b", "ג": "g", "ד": "d", "ה": "h", "ו": "v", "ז": "z",
    "ח": "ch", "ט": "t", "י": "y", "כ": "k", "ך": "k", "ל": "l", "מ": "m",
    "ם": "m", "נ": "n", "ן": "n", "ס": "s", "ע": "'", "פ": "p", "ף": "p",
    "צ": "tz", "ץ": "tz", "ק": "q", "ר": "r", "ש": "sh", "ת": "t",
    "־": "-", " ": " ", "/": "/",
}


def yaml_quote(s: Optional[str]) -> str:
    if s is None:
        return '""'
    if any(c in s for c in ':"\'\n#{}[]|&*>!%@`') or s == "" or s.strip() != s:
        return json.dumps(s, ensure_ascii=False)
    return s


def translit_plain(he_plain: str) -> str:
    p = he_plain.replace("/", "")
    out = []
    for ch in p:
        if ch in _HE_MAP:
            out.append(_HE_MAP[ch])
        elif "\u05B0" <= ch <= "\u05BD" or "\u05C1" <= ch <= "\u05C7":
            continue
        else:
            if ord(ch) < 0x0590 or ord(ch) > 0x05FF:
                out.append(ch)
    s = re.sub(r"'+", "'", "".join(out))
    return re.sub(r"\s+", " ", s).strip() or "x"


def extract_meta_block(text: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in (
        "id", "title_en", "title_he", "title_he_translit", "title_he_en",
        "refs", "genre", "build_track",
    ):
        m = re.search(rf'^\s*{key}:\s*(.+)$', text, re.M)
        if not m:
            continue
        val = m.group(1).strip()
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            out[key] = val[1:-1]
        else:
            out[key] = val
    dm = re.search(r"depends_on:\n((?:\s+-\s+.+\n)+)", text)
    deps = []
    if dm:
        deps = re.findall(r'-\s*"?([^"\n]+)"?', dm.group(1))
    out["depends_on"] = deps
    om = re.search(r"oral_policy_note_en:\s*>\n((?:\s{4}.+\n)+)", text)
    if om:
        out["oral_policy_note_en"] = " ".join(
            ln.strip() for ln in om.group(1).splitlines() if ln.strip()
        )
    else:
        out["oral_policy_note_en"] = (
            "Written trees first. Dual-track Oral only when named; never silent-merge."
        )
    exports = []
    for m in re.finditer(
        r"-\s+id:\s*(EXPORT\S+)\n(?:\s+he:\s*(.+)\n)?(?:\s+he_translit:\s*(.+)\n)?\s+en:\s*(.+)",
        text,
    ):
        he = (m.group(2) or "").strip().strip('"')
        tr = (m.group(3) or "").strip().strip('"')
        en = (m.group(4) or "").strip().strip('"')
        exports.append((m.group(1), he or None, tr or None, en))
    out["exports"] = exports[:12]
    return out


def parse_refs(refs: str) -> tuple[int, int, int, int]:
    refs = refs.strip().strip('"')
    m = re.match(r"(\d+):(\d+)-(\d+):(\d+)$", refs)
    if m:
        return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    m = re.match(r"(\d+):(\d+)-(\d+)$", refs)
    if m:
        ch = int(m.group(1))
        return ch, int(m.group(2)), ch, int(m.group(3))
    m = re.match(r"(\d+):(\d+)$", refs)
    if m:
        ch, v = int(m.group(1)), int(m.group(2))
        return ch, v, ch, v
    raise ValueError(f"bad refs: {refs}")


def verse_list(counts: dict, ch_s: int, v_s: int, ch_e: int, v_e: int) -> list[tuple[int, int]]:
    out = []
    for ch in range(ch_s, ch_e + 1):
        lo = v_s if ch == ch_s else 1
        hi = v_e if ch == ch_e else counts[ch]
        for v in range(lo, hi + 1):
            out.append((ch, v))
    return out


def top_arms(tree: dict, words: list[dict]) -> dict[str, Any]:
    children = tree.get("children") or []
    if len(children) >= 2:
        left, right = children[0], children[1]
    elif len(children) == 1:
        left, right = children[0], {"he_span": "", "word_indices": []}
    else:
        left = right = {
            "he_span": tree.get("he_span", ""),
            "word_indices": tree.get("word_indices", []),
        }

    def arm(node: dict) -> dict[str, Any]:
        idxs = node.get("word_indices") or []
        plains, trs = [], []
        for i in idxs:
            if 0 <= i < len(words):
                hp = words[i]["he_plain"].replace("/", "")
                plains.append(hp)
                trs.append(translit_plain(words[i]["he_plain"]))
        head_i = idxs[-1] if idxs else 0
        head_mark = ""
        for i in idxs:
            w = words[i]
            if "etnachta" in (w.get("mark_en") or ""):
                head_i = i
                head_mark = w.get("mark_en") or ""
                break
        else:
            if idxs:
                head_mark = words[idxs[-1]].get("mark_en") or ""
        head_he = words[head_i]["he_plain"].replace("/", "") if idxs and head_i < len(words) else ""
        return {
            "he": " ".join(plains),
            "he_translit": " ".join(trs),
            "head_he": head_he,
            "head_i": head_i,
            "head_mark": head_mark,
        }

    return {"left": arm(left), "right": arm(right)}


def role_for_plain(he_plain: str) -> tuple[str, str]:
    p0 = strip_taamim_and_points(he_plain.replace("/", "").replace("־", ""))
    glue = {
        "את", "אל", "על", "מן", "עם", "או", "אם", "כי", "גם", "אשר", "לא", "כל",
        "זה", "זו", "זאת", "בן", "בין", "ו", "ה", "ב", "כ", "ל", "מ",
    }
    if p0 in glue or len(p0) <= 1:
        return "glue", "glue"
    people = (
        "משה", "אהרן", "ישראל", "אלעזר", "איתמר", "יהושע", "כלב", "קרח",
        "בלעם", "בלק", "פנחס", "מרים", "נדב", "אביהוא",
    )
    if any(x in p0 for x in people):
        return "agent_or_person", "logic_bearing"
    return "logic_bearing_leaf", "logic_bearing"


def has_condition_marker(words: list[dict]) -> Optional[str]:
    for w in words[:4]:
        p = strip_taamim_and_points(w["he_plain"].replace("/", ""))
        if p in ("אם", "ואם", "כי", "וכי", "הן"):
            return p
    return None


def oral_samples(path: Path, max_paras: int = 3) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    text = data.get("text") or data
    out: list[dict] = []

    def walk(o, section: str):
        if len(out) >= max_paras:
            return
        if isinstance(o, str) and o.strip():
            out.append({"section": section, "he": o.strip()[:240]})
            return
        if isinstance(o, list):
            for x in o:
                walk(x, section)
                if len(out) >= max_paras:
                    return
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, str(k)[:80])
                if len(out) >= max_paras:
                    return

    walk(text, path.stem)
    return out


def emit_unit(book_key: str, unit_id: str, phase: str) -> Path:
    cfg = BOOKS[book_key]
    path = UNITS / f"{unit_id}.yaml"
    # Prefer UNIT_SPECS (first-draft map) when present; else re-read existing meta.
    if unit_id in UNIT_SPECS:
        spec = UNIT_SPECS[unit_id]
        meta = {
            "id": unit_id,
            "refs": spec["refs"],
            "title_en": spec["title_en"],
            "title_he": spec.get("title_he") or "",
            "title_he_translit": spec.get("title_he_translit") or "",
            "title_he_en": spec.get("title_he_en") or "",
            "genre": spec.get("genre") or "decision_table",
            "depends_on": list(spec.get("depends_on") or []),
            "exports": [],
            "oral_policy_note_en": (
                f"Written trees first. Prefer {cfg['oral_name']} dual-track on law densification; "
                "MH endpoints possible Oral; never silent-merge. Free names import Gen/Exod/Lev/Num."
            ),
        }
    elif path.exists():
        old = path.read_text(encoding="utf-8")
        meta = extract_meta_block(old)
    else:
        raise FileNotFoundError(
            f"{path} not found and no UNIT_SPECS entry for {unit_id}"
        )
    refs = str(meta.get("refs") or "").strip().strip('"')
    ch_s, v_s, ch_e, v_e = parse_refs(refs)
    verses = verse_list(cfg["counts"], ch_s, v_s, ch_e, v_e)
    genre = str(meta.get("genre") or "decision_table").strip().strip('"')
    title_en = str(meta.get("title_en") or unit_id)
    title_he = str(meta.get("title_he") or "")
    title_tr = str(meta.get("title_he_translit") or "")
    title_he_en = str(meta.get("title_he_en") or "")
    depends = meta.get("depends_on") or []
    exports = meta.get("exports") or []
    if not exports:
        exports = [(f"EXPORT_{unit_id}_tree_derived", None, None, f"Tree-derived v1 for {refs}")]

    osis_book = cfg["osis"]
    step_pfx = cfg["step_prefix"]
    parsed_verses: list[dict[str, Any]] = []

    for ch, v in verses:
        osis = f"{osis_book}.{ch}.{v}"
        sid = f"{step_pfx}_{ch}_{v}"
        try:
            pr = parse_verse(osis)
            arms = top_arms(pr["tree"], pr["words"])
            ascii_t = tree_ascii_string(pr["tree"])
            pure = "false" if ("3-ary" in ascii_t or "n-ary" in ascii_t) else "true"
            cond = has_condition_marker(pr["words"])
            left, right = arms["left"], arms["right"]
            plain_words = [w["he_plain"].replace("/", "") for w in pr["words"]]
            linear_he = " ".join(plain_words)
            linear_tr = " ".join(translit_plain(w["he_plain"]) for w in pr["words"])
            op = "TREE_CLAIM"
            if cond:
                op = f"COND_{cond}"
            elif any("etnachta" in (w.get("mark_en") or "") for w in pr["words"]):
                op = "ETNACHTA_SPLIT"
            step_en = (
                f"[EN-AID] From top split: LEFT «{left['he'][:80]}» "
                f"/ RIGHT «{right['he'][:80]}». "
                f"Derive claim from Hebrew arms. {osis_book} {ch}:{v}."
            )
            step_he = f"{left['he'][:60]} … {right['he'][:60]}" if right["he"] else left["he"][:120]
            step_tr = (
                f"{left['he_translit'][:50]} … {right['he_translit'][:50]}"
                if right["he_translit"]
                else left["he_translit"][:100]
            )
            parsed_verses.append(
                {
                    "ch": ch, "v": v, "osis": osis, "sid": sid, "op": op, "cond": cond,
                    "pr": pr, "arms": arms, "ascii": ascii_t, "pure": pure,
                    "linear_he": linear_he, "linear_tr": linear_tr,
                    "step_he": step_he, "step_tr": step_tr, "step_en": step_en,
                    "words": pr["words"],
                }
            )
        except Exception as e:
            parsed_verses.append(
                {
                    "ch": ch, "v": v, "osis": osis, "sid": sid, "op": "PARSE_ERROR",
                    "error": str(e), "pr": None,
                }
            )

    lines: list[str] = []
    lines.append("# =============================================================================")
    lines.append(f"# LOGIC UNIT: {cfg['book_en']} {refs} — {title_en}")
    lines.append(f"# TREE-DERIVED v1 (phase {phase}) — steps from ta'amim top splits")
    lines.append("# =============================================================================")
    lines.append("# Experimental model — not binding religious law.")
    lines.append("# Process: tree → arm-cited STEP per verse → maps_to → coverage.")
    lines.append("")
    lines.append("meta:")
    lines.append(f'  id: "{unit_id}"')
    lines.append(f"  title_en: {yaml_quote(title_en)}")
    lines.append(f"  title_he: {yaml_quote(title_he)}")
    lines.append(f"  title_he_translit: {yaml_quote(title_tr)}")
    lines.append(f"  title_he_en: {yaml_quote(title_he_en)}")
    lines.append(f'  book_he: {yaml_quote(cfg["book_he"])}')
    lines.append(f'  book_he_translit: {yaml_quote(cfg["book_tr"])}')
    lines.append(f'  book_en: {yaml_quote(cfg["book_en"])}')
    lines.append(f'  refs: "{refs}"')
    lines.append("  data_paths_he:")
    lines.append(f'    - "{cfg["data"]}"')
    lines.append("  status: draft")
    lines.append("  tree_derive_version: tree_derived_v1")
    lines.append(f'  tree_derive_phase: "{phase}"')
    lines.append("  confidence_overall: hypothesis")
    lines.append(f'  genre: "{genre}"')
    lines.append(f'  build_track: {yaml_quote(cfg["build_track"])}')
    lines.append("  depends_on:")
    for d in depends:
        lines.append(f'    - "{d.strip()}"')
    lines.append("  owner_language_note: >")
    lines.append("    English for reading only. Hebrew is the derivation source.")
    lines.append("  oral_policy_note_en: >")
    for chunk in re.findall(r".{1,90}(?:\s|$)", str(meta.get("oral_policy_note_en") or "")):
        lines.append(f"    {chunk.rstrip()}")
    lines.append("  method_note_en: >")
    lines.append("    Tree-derived v1: each verse top binary split (left/right) grounds one STEP.")
    lines.append("    Not multi-verse English smear. Not full TIR yet.")
    lines.append("")
    lines.append("derivation_log:")
    lines.append("  - step: A")
    lines.append('    name_en: "Block choice"')
    lines.append("    comment: >")
    lines.append(f"      Reprocess {unit_id} ({refs}, {len(verses)} vv) tree-first phase {phase}.")
    lines.append("    confidence: established")
    lines.append("  - step: B")
    lines.append('    name_en: "Trees"')
    lines.append("    comment: >")
    lines.append("      Every verse via taamim_tree_parse.py v1; full tree_ascii recorded.")
    lines.append("    confidence: tested")
    lines.append('    tags: ["[HE-STRUCT]"]')
    lines.append("  - step: C")
    lines.append('    name_en: "Tree → steps"')
    lines.append("    comment: >")
    lines.append("      One STEP per verse citing left/right top-split arms. English [EN-AID] only.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[HE-WRITTEN]","[HE-STRUCT]"]')
    lines.append("  - step: D")
    lines.append('    name_en: "Oral dual-track"')
    lines.append("    comment: >")
    lines.append(f"      {cfg['oral_name']} samples when available; dual-track only; never silent-merge.")
    lines.append("    confidence: hypothesis")
    lines.append('    tags: ["[ORAL]"]')
    lines.append("")
    lines.append("boot_steps:")
    order = 0
    decision_rows: list[tuple[str, str, str]] = []
    for pv in parsed_verses:
        order += 1
        if pv.get("error"):
            lines.append(f"  - id: {pv['sid']}")
            lines.append(f"    order: {order}")
            lines.append(f'    ref: "{osis_book}.{pv["ch"]}.{pv["v"]}"')
            lines.append("    op: PARSE_ERROR")
            lines.append(f"    en: {yaml_quote('Parse error: ' + pv['error'])}")
            lines.append("    confidence: failed")
            lines.append('    source: "[HE-STRUCT]"')
            lines.append("")
            continue
        left, right = pv["arms"]["left"], pv["arms"]["right"]
        lines.append(f"  - id: {pv['sid']}")
        lines.append(f"    order: {order}")
        lines.append(f'    ref: "{osis_book}.{pv["ch"]}.{pv["v"]}"')
        lines.append(f"    op: {pv['op']}")
        lines.append(f"    he: {yaml_quote(pv['step_he'])}")
        lines.append(f"    he_translit: {yaml_quote(pv['step_tr'])}")
        lines.append(f"    en: {yaml_quote(pv['step_en'])}")
        lines.append("    tree_left:")
        lines.append(f"      he: {yaml_quote(left['he'][:200])}")
        lines.append(f"      he_translit: {yaml_quote(left['he_translit'][:200])}")
        lines.append('      en: "Left arm of top binary split [EN-AID]"')
        lines.append("    tree_right:")
        lines.append(f"      he: {yaml_quote(right['he'][:200])}")
        lines.append(f"      he_translit: {yaml_quote(right['he_translit'][:200])}")
        lines.append('      en: "Right arm of top binary split [EN-AID]"')
        lines.append("    comment: >")
        lines.append(
            f"      Top split L mark={left.get('head_mark') or 'n/a'}; maps_to this verse only."
        )
        lines.append("    confidence: hypothesis")
        lines.append('    source: "[HE-WRITTEN][HE-STRUCT]"')
        lines.append("")
        if pv.get("cond") and genre in ("decision_table", "decision / procedure", "decision"):
            decision_rows.append(
                (
                    f"ROW_{osis_book}_{pv['ch']}_{pv['v']}",
                    f"Marker {pv['cond']} in {osis_book} {pv['ch']}:{pv['v']}",
                    f"Apply claim of {pv['sid']} from Hebrew arms — hypothesis only",
                )
            )

    if "decision" in genre.lower() or genre == "decision_table":
        lines.append("decision_table:")
        lines.append("  comment_en: >")
        lines.append("    Hypothesis rows from tree-flagged condition markers / structure.")
        lines.append("    Not binding law.")
        lines.append("  rows:")
        if decision_rows:
            for rid, ifr, thenr in decision_rows:
                lines.append(f"    - id: {rid}")
                lines.append(f"      if_en: {yaml_quote(ifr)}")
                lines.append(f"      then_en: {yaml_quote(thenr)}")
                lines.append("      confidence: hypothesis")
                lines.append('      source: "[HE-WRITTEN][HE-STRUCT]"')
        else:
            lines.append("    - id: ROW_STRUCTURAL")
            lines.append(
                '      if_en: "When this block\'s case conditions hold (read per-verse tree arms)"'
            )
            lines.append(
                f'      then_en: "Follow sequential {step_pfx}_* for verses in this unit (hypothesis)"'
            )
            lines.append("      confidence: hypothesis")
            lines.append('      source: "[HE-WRITTEN][HE-STRUCT]"')
        lines.append("")

    lines.append("state_machine:")
    lines.append(f'  comment_en: "Coarse states for {unit_id} after tree-derived steps."')
    lines.append("  states:")
    lines.append("    - id: S_block_open")
    lines.append(f'      en: "Entered {refs}"')
    lines.append("    - id: S_block_mid")
    lines.append('      en: "Mid-block after ~half of verse steps"')
    lines.append("    - id: S_block_closed")
    lines.append(f'      en: "Completed tree-derived steps for {refs}"')
    lines.append("  transitions:")
    if parsed_verses:
        mid = parsed_verses[len(parsed_verses) // 2]["sid"]
        last = parsed_verses[-1]["sid"]
        lines.append("    - from: S_block_open")
        lines.append("      to: S_block_mid")
        lines.append(f"      via: {mid}")
        lines.append("    - from: S_block_mid")
        lines.append("      to: S_block_closed")
        lines.append(f"      via: {last}")
    lines.append("")
    lines.append("state_after:")
    lines.append("  - id: AFTER_S_block_closed")
    lines.append(f'    en: "Tree-derived v1 complete for {unit_id}"')
    lines.append("")
    lines.append("exports:")
    for item in exports:
        lines.append(f"  - id: {item[0]}")
        if len(item) > 1 and item[1]:
            lines.append(f"    he: {yaml_quote(item[1])}")
        if len(item) > 2 and item[2]:
            lines.append(f"    he_translit: {yaml_quote(item[2])}")
        lines.append(f"    en: {yaml_quote(item[3] if len(item) > 3 else '')}")
    lines.append(f"  - id: EXPORT_tree_derived_v1_{unit_id}")
    lines.append('    en: "Unit reprocessed tree-first (one STEP per verse, arm-cited)"')
    lines.append("")
    lines.append("oral_notes:")
    lines.append("  - id: ORAL_policy")
    lines.append("    status: observation")
    lines.append(f'    work_en: "{cfg["book_en"]} tree-derive oral policy"')
    lines.append("    comment_en: >")
    lines.append(
        f"      Written trees first. Prefer {cfg['oral_name']} on law densification; "
        "MH possible; never silent-merge."
    )
    lines.append('    source: "[PROJECT]"')
    lawish = "decision" in genre.lower() or genre in ("boot_steps", "procedure")
    if lawish:
        for i, s in enumerate(oral_samples(cfg["oral_file"], 3), 1):
            lines.append(f"  - id: ORAL_sample_{i}")
            lines.append("    status: dual_track")
            lines.append(f'    work_en: {yaml_quote(cfg["oral_name"])}')
            lines.append(f'    locus_en: {yaml_quote(cfg["oral_name"] + ": " + s["section"])}')
            lines.append(f"    he_sample: {yaml_quote(s['he'])}")
            lines.append('    he_translit: "see Hebrew sample in local Data dump"')
            lines.append(
                '    en_sample: "[EN-AID] Sample only; not derivation source; dual-track."'
            )
            lines.append("    comment_en: >")
            lines.append("      Dual-track sample — does not rewrite Written tree-derived STEPs.")
            lines.append(f'    source: "[ORAL]{cfg["oral_tag"]}"')
            lines.append("    confidence: hypothesis")
    else:
        lines.append("  - id: ORAL_possible")
        lines.append("    status: possible_oral")
        lines.append('    work_en: "Midrash / Bavli / MH (named when quoted)"')
        lines.append("    comment_en: Dual-track only; Written first.")
        lines.append('    source: "[ORAL]"')
    lines.append("")
    lines.append("scenarios:")
    for i, pv in enumerate(parsed_verses[:6], 1):
        lines.append(f"  - id: S{i}")
        lines.append(f'    title_en: "After {osis_book} {pv["ch"]}:{pv["v"]} ({pv["sid"]})"')
        lines.append(
            f'    expect_en: "Advances via tree-derived {pv["sid"]}; arms in boot_steps."'
        )
    if parsed_verses:
        last = parsed_verses[-1]
        lines.append("  - id: S_last")
        lines.append(f'    title_en: "After final verse {last["ch"]}:{last["v"]}"')
        lines.append(f'    expect_en: "Block closed via {last["sid"]}."')
    lines.append("")
    lines.append("binary_trees:")
    lines.append("  display_policy_en: >")
    lines.append("    Always he + he_translit + en. Full tree_ascii per verse.")
    lines.append("  method_note_en: >")
    lines.append(f"    taamim_tree_parse.py v1; STEPs from top splits (tree_derived_v1).")
    lines.append(f'  data_source: "{cfg["data"]}"')
    lines.append('  parser: "taamim_tree_parse.py"')
    lines.append('  rule_set_version: "v1"')
    lines.append('  tags: ["[HE-STRUCT]"]')
    lines.append("  verse_trees:")

    coverage_blocks: list[str] = []
    word_total = 0
    key_pfx = osis_book  # Lev_1_1 or Num_1_1
    for pv in parsed_verses:
        ch, v = pv["ch"], pv["v"]
        if pv.get("error") or not pv.get("pr"):
            lines.append(f"    {key_pfx}_{ch}_{v}:")
            lines.append(f'      verse: "{ch}:{v}"')
            lines.append(f'      osis_id: "{pv["osis"]}"')
            lines.append("      parser_status: error")
            lines.append(f"      error: {yaml_quote(pv.get('error', 'unknown'))}")
            continue
        words = pv["words"]
        arms = pv["arms"]
        wc = len(words)
        word_total += wc
        lines.append(f"    {key_pfx}_{ch}_{v}:")
        lines.append(f'      verse: "{ch}:{v}"')
        lines.append(f'      osis_id: "{pv["osis"]}"')
        lines.append(f'      parser_status: {pv["pr"].get("status", "unique")}')
        lines.append(f"      pure_binary: {pv['pure']}")
        lines.append(f"      word_count: {wc}")
        lines.append("      linear:")
        lines.append(f"        he: {yaml_quote(pv['linear_he'])}")
        lines.append(f"        he_translit: {yaml_quote(pv['linear_tr'])}")
        lines.append(
            f'        en: "Free gloss [EN-AID] — structure from Hebrew tree. {ch}:{v}."'
        )
        lines.append("      top_binary_split:")
        lines.append("        comment: >")
        lines.append(f"          Top split ta'amim v1; maps_to ['{pv['sid']}'].")
        lines.append("        left_half:")
        lines.append('          side_en: "Left of top split"')
        lines.append("          head:")
        lines.append(f"            he: {yaml_quote(arms['left']['head_he'])}")
        lines.append(
            f'            he_translit: "{translit_plain(arms["left"]["head_he"])}"'
        )
        lines.append(f'            en: "left-end leaf {arms["left"]["head_i"]}"')
        lines.append(f"            mark_en: {yaml_quote(arms['left']['head_mark'])}")
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(arms['left']['he'][:200])}")
        lines.append(
            f"            he_translit: {yaml_quote(arms['left']['he_translit'][:200])}"
        )
        lines.append('            en: "left phrase arm (see tree_ascii)"')
        lines.append("        right_half:")
        lines.append('          side_en: "Right of top split"')
        lines.append("          phrase:")
        lines.append(f"            he: {yaml_quote(arms['right']['he'][:200])}")
        lines.append(
            f"            he_translit: {yaml_quote(arms['right']['he_translit'][:200])}"
        )
        lines.append('            en: "right phrase arm (see tree_ascii)"')
        lines.append("      tree_ascii: |")
        for al in pv["ascii"].splitlines():
            lines.append(f"        {al}")
        lines.append(f'      maps_to: ["{pv["sid"]}"]')
        lines.append("      confidence: tested")
        lines.append('      source: "[HE-STRUCT][HE-WRITTEN]"')
        lines.append("")
        cov = [f'  - ref: "{pv["osis"]}"', "    words:"]
        for w in words:
            role, kind = role_for_plain(w["he_plain"])
            he_p = w["he_plain"].replace("/", "")
            tr = translit_plain(w["he_plain"])
            cov.append(
                f'      - {{index: {w["index"]}, he: {yaml_quote(he_p)}, he_translit: {yaml_quote(tr)}, '
                f'en: "leaf {w["index"]} ({he_p})", role: {role}, kind: {kind}, feeds: [{pv["sid"]}]}}'
            )
        coverage_blocks.append("\n".join(cov))

    lines.append("tree_coverage:")
    lines.append("  aspiration_en: >")
    lines.append("    100% word use; roles provisional pending TIR.")
    lines.append(f"  word_total: {word_total}")
    lines.append("  verses:")
    for cb in coverage_blocks:
        lines.append(cb)
    lines.append("")
    lines.append("confidence: hypothesis")
    lines.append("status_note_en: >")
    lines.append(
        f"  Tree-derived v1 (phase {phase}). One STEP per verse from top-split arms. "
        "Not binding religious law."
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--book", required=True, choices=list(BOOKS.keys()) + ["all"])
    ap.add_argument("--phase", default="all", help="Phase letter or all")
    ap.add_argument("--only", help="Single unit id")
    args = ap.parse_args()

    books = list(BOOKS.keys()) if args.book == "all" else [args.book]

    for bk in books:
        cfg = BOOKS[bk]
        phases = cfg["phases"]
        if args.only:
            # find phase tag
            ph = args.phase if args.phase != "all" else "manual"
            for p, us in phases.items():
                if args.only in us:
                    ph = p
                    break
            pth = emit_unit(bk, args.only, ph)
            print(f"{bk} phase {ph}: wrote {pth.name}")
            continue

        phase_order = list(phases.keys())
        if args.phase != "all":
            if args.phase not in phases:
                print("unknown phase", args.phase, "for", bk, list(phases), file=sys.stderr)
                sys.exit(1)
            phase_order = [args.phase]

        total = 0
        for ph in phase_order:
            for u in phases[ph]:
                pth = emit_unit(bk, u, ph)
                print(f"{bk} phase {ph}: wrote {pth.name}")
                total += 1
        print(f"done book={bk} units={total}")


if __name__ == "__main__":
    main()
