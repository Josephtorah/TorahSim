#!/usr/bin/env python3
# =============================================================================
# lev_22_holy_food — 22:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_22_holy_food.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Who may eat holy things; purity gates (22:1–16)"""
from machine import Machine

m = Machine("lev_22_holy_food")

# -------------------------- Lev.22.1 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 22:1."
m.step("Lev.22.1")

# -------------------------- Lev.22.2 · ETNACHTA_SPLIT ----------------------
# דבר אל אהרן ואל בניו וינזרו מקדשי בני ישראל ולא יחללו את שם  … אשר הם
# מקדשים לי אני יהוה
# "[EN-AID] From top split: LEFT «דבר אל אהרן ואל בניו וינזרו מקדשי בני
# ישראל ולא יחללו את שם קדשי» / RIGHT «אשר הם מקדשים לי אני יהוה». Derive
# claim from Hebrew arms. Lev 22:2."
m.step("Lev.22.2")
# witness-tier presupposed read: separation_and_the_triple_import on
# veyinazru — read, not installed
m.witness_read("veyinazru", "separation_and_the_triple_import",
                cites=["Sifra, Emor, Section 4 1", "Sifra, Emor, Section 4 2", "Sifra, Emor, Section 4 3", "Sifra, Emor, Section 4 4", "Onkelos Lev 22:2"])

# -------------------------- Lev.22.3 · ETNACHTA_SPLIT ----------------------
# אמר אלהם לדרתיכם כל איש אשר יקרב מכל זרעכם אל הקדשים אשר יקד … ונכרתה הנפש
# ההוא מלפני אני יהוה
# "[EN-AID] From top split: LEFT «אמר אלהם לדרתיכם כל איש אשר יקרב מכל זרעכם
# אל הקדשים אשר יקדישו בני ישראל ליהוה » / RIGHT «ונכרתה הנפש ההוא מלפני אני
# יהוה». Derive claim from Hebrew arms. Lev 22:3."
m.step("Lev.22.3")
# witness-tier presupposed read: karet_extension_and_readiness_threshold on
# asher_yikrav_vetumato_alav — read, not installed
m.witness_read("asher_yikrav_vetumato_alav", "karet_extension_and_readiness_threshold",
                cites=["Sifra, Emor, Section 4 5", "Sifra, Emor, Section 4 6", "Sifra, Emor, Section 4 7", "Sifra, Emor, Section 4 8", "Onkelos Lev 22:3"])

# -------------------------- Lev.22.4 · ETNACHTA_SPLIT ----------------------
# איש איש מזרע אהרן והוא צרוע או זב בקדשים לא יאכל עד אשר יטהר … והנגע בכל
# טמא נפש או איש אשר תצא ממנו שכבת זרע
# "[EN-AID] From top split: LEFT «איש איש מזרע אהרן והוא צרוע או זב בקדשים
# לא יאכל עד אשר יטהר» / RIGHT «והנגע בכל טמא נפש או איש אשר תצא ממנו שכבת
# זרע». Derive claim from Hebrew arms. Lev 22:4."
m.step("Lev.22.4")
# witness-tier presupposed read: the_impurity_measures_census on
# tzarua_o_zav — read, not installed
m.witness_read("tzarua_o_zav", "the_impurity_measures_census",
                cites=["Sifra, Emor, Chapter 4 1", "Sifra, Emor, Chapter 4 2", "Sifra, Emor, Chapter 4 3", "Sifra, Emor, Chapter 4 4", "Onkelos Lev 22:4"])

# -------------------------- Lev.22.5 · ETNACHTA_SPLIT ----------------------
# או איש אשר יגע בכל שרץ אשר יטמא לו … או באדם אשר יטמא לו לכל טמאתו
# "[EN-AID] From top split: LEFT «או איש אשר יגע בכל שרץ אשר יטמא לו» /
# RIGHT «או באדם אשר יטמא לו לכל טמאתו». Derive claim from Hebrew arms. Lev
# 22:5."
m.step("Lev.22.5")

# -------------------------- Lev.22.6 · ETNACHTA_SPLIT ----------------------
# נפש אשר תגע בו וטמאה עד הערב … ולא יאכל מן הקדשים כי אם רחץ בשרו במים
# "[EN-AID] From top split: LEFT «נפש אשר תגע בו וטמאה עד הערב» / RIGHT «ולא
# יאכל מן הקדשים כי אם רחץ בשרו במים». Derive claim from Hebrew arms. Lev
# 22:6."
m.step("Lev.22.6")
# witness-tier presupposed read: mixture_grid_and_two_gates on
# nefesh_asher_tiga_bo — read, not installed
m.witness_read("nefesh_asher_tiga_bo", "mixture_grid_and_two_gates",
                cites=["Sifra, Emor, Chapter 4 5", "Sifra, Emor, Chapter 4 6", "Sifra, Emor, Chapter 4 7", "Sifra, Emor, Chapter 4 8", "Sifra, Emor, Chapter 4 9", "Sifra, Emor, Chapter 4 10", "Sifra, Emor, Chapter 4 11", "Onkelos Lev 22:7"])

# -------------------------- Lev.22.7 · ETNACHTA_SPLIT ----------------------
# ובא השמש וטהר … ואחר יאכל מן הקדשים כי לחמו הוא
# "[EN-AID] From top split: LEFT «ובא השמש וטהר» / RIGHT «ואחר יאכל מן
# הקדשים כי לחמו הוא». Derive claim from Hebrew arms. Lev 22:7."
m.step("Lev.22.7")

# -------------------------- Lev.22.8 · ETNACHTA_SPLIT ----------------------
# נבלה וטרפה לא יאכל לטמאה בה … אני יהוה
# "[EN-AID] From top split: LEFT «נבלה וטרפה לא יאכל לטמאה בה» / RIGHT «אני
# יהוה». Derive claim from Hebrew arms. Lev 22:8."
m.step("Lev.22.8")
# witness-tier presupposed read: gullet_carve_and_the_courts_charge on
# nevelah_utrefah_lo_yochal — read, not installed
m.witness_read("nevelah_utrefah_lo_yochal", "gullet_carve_and_the_courts_charge",
                cites=["Sifra, Emor, Chapter 4 12", "Sifra, Emor, Chapter 4 13", "Sifra, Emor, Chapter 4 14", "Sifra, Emor, Chapter 4 15", "Onkelos Lev 22:9"])

# -------------------------- Lev.22.9 · ETNACHTA_SPLIT ----------------------
# ושמרו את משמרתי ולא ישאו עליו חטא ומתו בו כי יחללהו … אני יהוה מקדשם
# "[EN-AID] From top split: LEFT «ושמרו את משמרתי ולא ישאו עליו חטא ומתו בו
# כי יחללהו» / RIGHT «אני יהוה מקדשם». Derive claim from Hebrew arms. Lev
# 22:9."
m.step("Lev.22.9")

# -------------------------- Lev.22.10 · ETNACHTA_SPLIT ---------------------
# וכל זר לא יאכל קדש … תושב כהן ושכיר לא יאכל קדש
# "[EN-AID] From top split: LEFT «וכל זר לא יאכל קדש» / RIGHT «תושב כהן
# ושכיר לא יאכל קדש». Derive claim from Hebrew arms. Lev 22:10."
m.step("Lev.22.10")
# witness-tier presupposed read: the_stranger_and_the_uncircumcised on
# kol_zar_toshav_vesachir — read, not installed
m.witness_read("kol_zar_toshav_vesachir", "the_stranger_and_the_uncircumcised",
                cites=["Sifra, Emor, Chapter 4 16", "Sifra, Emor, Chapter 4 17", "Sifra, Emor, Chapter 4 18", "Onkelos Lev 22:10"])

# -------------------------- Lev.22.11 · COND_כי ----------------------------
# וכהן כי יקנה נפש קנין כספו הוא יאכל בו … ויליד ביתו הם יאכלו בלחמו
# "[EN-AID] From top split: LEFT «וכהן כי יקנה נפש קנין כספו הוא יאכל בו» /
# RIGHT «ויליד ביתו הם יאכלו בלחמו». Derive claim from Hebrew arms. Lev
# 22:11."
m.step("Lev.22.11")
# witness-tier presupposed read: the_household_feeder on
# kinyan_kaspo_yelid_beito — read, not installed
m.witness_read("kinyan_kaspo_yelid_beito", "the_household_feeder",
                cites=["Sifra, Emor, Section 5 1", "Sifra, Emor, Section 5 2", "Sifra, Emor, Section 5 3", "Sifra, Emor, Section 5 4", "Sifra, Emor, Section 5 5", "Sifra, Emor, Section 5 6"])

# -------------------------- Lev.22.12 · COND_כי ----------------------------
# ובת כהן כי תהיה לאיש זר … הוא בתרומת הקדשים לא תאכל
# "[EN-AID] From top split: LEFT «ובת כהן כי תהיה לאיש זר» / RIGHT «הוא
# בתרומת הקדשים לא תאכל». Derive claim from Hebrew arms. Lev 22:12."
m.step("Lev.22.12")
# witness-tier presupposed read: the_daughter_to_a_stranger on
# bat_kohen_leish_zar — read, not installed
m.witness_read("bat_kohen_leish_zar", "the_daughter_to_a_stranger",
                cites=["Sifra, Emor, Section 5 7", "Sifra, Emor, Section 5 8", "Sifra, Emor, Section 5 9", "Sifra, Emor, Section 5 10", "Sifra, Emor, Section 6 1", "Onkelos Lev 22:12"])

# -------------------------- Lev.22.13 · COND_כי ----------------------------
# ובת כהן כי תהיה אלמנה וגרושה וזרע אין לה ושבה אל בית אביה כנ … וכל זר לא
# יאכל בו
# "[EN-AID] From top split: LEFT «ובת כהן כי תהיה אלמנה וגרושה וזרע אין לה
# ושבה אל בית אביה כנעוריה מלחם אביה תאכל» / RIGHT «וכל זר לא יאכל בו».
# Derive claim from Hebrew arms. Lev 22:13."
m.step("Lev.22.13")
# witness-tier presupposed read: the_return_and_the_seeds_seed on
# veshavah_el_beit_aviha — read, not installed
m.witness_read("veshavah_el_beit_aviha", "the_return_and_the_seeds_seed",
                cites=["Sifra, Emor, Chapter 5 1", "Sifra, Emor, Chapter 5 2", "Sifra, Emor, Chapter 5 3", "Sifra, Emor, Chapter 5 4", "Sifra, Emor, Chapter 5 5", "Sifra, Emor, Chapter 6 1", "Onkelos Lev 22:13"])

# -------------------------- Lev.22.14 · COND_כי ----------------------------
# ואיש כי יאכל קדש בשגגה … ויסף חמשיתו עליו ונתן לכהן את הקדש
# "[EN-AID] From top split: LEFT «ואיש כי יאכל קדש בשגגה» / RIGHT «ויסף
# חמשיתו עליו ונתן לכהן את הקדש». Derive claim from Hebrew arms. Lev 22:14."
m.step("Lev.22.14")
# witness-tier presupposed read: the_fifths_algebra on veyasaf_chamishito —
# read, not installed
m.witness_read("veyasaf_chamishito", "the_fifths_algebra",
                cites=["Sifra, Emor, Chapter 6 2", "Sifra, Emor, Chapter 6 3", "Sifra, Emor, Chapter 6 4", "Sifra, Emor, Chapter 6 5", "Sifra, Emor, Chapter 6 6", "Sifra, Emor, Chapter 6 7", "Onkelos Lev 22:14"])

# -------------------------- Lev.22.15 · ETNACHTA_SPLIT ---------------------
# ולא יחללו את קדשי בני ישראל … את אשר ירימו ליהוה
# "[EN-AID] From top split: LEFT «ולא יחללו את קדשי בני ישראל» / RIGHT «את
# אשר ירימו ליהוה». Derive claim from Hebrew arms. Lev 22:15."
m.step("Lev.22.15")
# witness-tier presupposed read: the_profaners_and_onkelos_condition on
# velo_yechalelu — read, not installed
m.witness_read("velo_yechalelu", "the_profaners_and_onkelos_condition",
                cites=["Sifra, Emor, Chapter 6 8", "Sifra, Emor, Chapter 6 9", "Sifra, Emor, Chapter 6 10", "Onkelos Lev 22:16"])

# -------------------------- Lev.22.16 · ETNACHTA_SPLIT ---------------------
# והשיאו אותם עון אשמה באכלם את קדשיהם … כי אני יהוה מקדשם
# "[EN-AID] From top split: LEFT «והשיאו אותם עון אשמה באכלם את קדשיהם» /
# RIGHT «כי אני יהוה מקדשם». Derive claim from Hebrew arms. Lev 22:16."
m.step("Lev.22.16")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 0
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('veyinazru', 'separation_and_the_triple_import'), ('asher_yikrav_vetumato_alav', 'karet_extension_and_readiness_threshold'), ('tzarua_o_zav', 'the_impurity_measures_census'), ('nefesh_asher_tiga_bo', 'mixture_grid_and_two_gates'), ('nevelah_utrefah_lo_yochal', 'gullet_carve_and_the_courts_charge'), ('kol_zar_toshav_vesachir', 'the_stranger_and_the_uncircumcised'), ('kinyan_kaspo_yelid_beito', 'the_household_feeder'), ('bat_kohen_leish_zar', 'the_daughter_to_a_stranger'), ('veshavah_el_beit_aviha', 'the_return_and_the_seeds_seed'), ('veyasaf_chamishito', 'the_fifths_algebra'), ('velo_yechalelu', 'the_profaners_and_onkelos_condition')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Emor, Section 4 1', 'Sifra, Emor, Section 4 2', 'Sifra, Emor, Section 4 3', 'Sifra, Emor, Section 4 4', 'Onkelos Lev 22:2']
    assert all('separation_and_the_triple_import' not in f for f in m.WORLD["facts"])
    assert 'veyinazru' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Emor, Section 4 5', 'Sifra, Emor, Section 4 6', 'Sifra, Emor, Section 4 7', 'Sifra, Emor, Section 4 8', 'Onkelos Lev 22:3']
    assert all('karet_extension_and_readiness_threshold' not in f for f in m.WORLD["facts"])
    assert 'asher_yikrav_vetumato_alav' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Emor, Chapter 4 1', 'Sifra, Emor, Chapter 4 2', 'Sifra, Emor, Chapter 4 3', 'Sifra, Emor, Chapter 4 4', 'Onkelos Lev 22:4']
    assert all('the_impurity_measures_census' not in f for f in m.WORLD["facts"])
    assert 'tzarua_o_zav' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Emor, Chapter 4 5', 'Sifra, Emor, Chapter 4 6', 'Sifra, Emor, Chapter 4 7', 'Sifra, Emor, Chapter 4 8', 'Sifra, Emor, Chapter 4 9', 'Sifra, Emor, Chapter 4 10', 'Sifra, Emor, Chapter 4 11', 'Onkelos Lev 22:7']
    assert all('mixture_grid_and_two_gates' not in f for f in m.WORLD["facts"])
    assert 'nefesh_asher_tiga_bo' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Emor, Chapter 4 12', 'Sifra, Emor, Chapter 4 13', 'Sifra, Emor, Chapter 4 14', 'Sifra, Emor, Chapter 4 15', 'Onkelos Lev 22:9']
    assert all('gullet_carve_and_the_courts_charge' not in f for f in m.WORLD["facts"])
    assert 'nevelah_utrefah_lo_yochal' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Emor, Chapter 4 16', 'Sifra, Emor, Chapter 4 17', 'Sifra, Emor, Chapter 4 18', 'Onkelos Lev 22:10']
    assert all('the_stranger_and_the_uncircumcised' not in f for f in m.WORLD["facts"])
    assert 'kol_zar_toshav_vesachir' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Emor, Section 5 1', 'Sifra, Emor, Section 5 2', 'Sifra, Emor, Section 5 3', 'Sifra, Emor, Section 5 4', 'Sifra, Emor, Section 5 5', 'Sifra, Emor, Section 5 6']
    assert all('the_household_feeder' not in f for f in m.WORLD["facts"])
    assert 'kinyan_kaspo_yelid_beito' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Emor, Section 5 7', 'Sifra, Emor, Section 5 8', 'Sifra, Emor, Section 5 9', 'Sifra, Emor, Section 5 10', 'Sifra, Emor, Section 6 1', 'Onkelos Lev 22:12']
    assert all('the_daughter_to_a_stranger' not in f for f in m.WORLD["facts"])
    assert 'bat_kohen_leish_zar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Emor, Chapter 5 1', 'Sifra, Emor, Chapter 5 2', 'Sifra, Emor, Chapter 5 3', 'Sifra, Emor, Chapter 5 4', 'Sifra, Emor, Chapter 5 5', 'Sifra, Emor, Chapter 6 1', 'Onkelos Lev 22:13']
    assert all('the_return_and_the_seeds_seed' not in f for f in m.WORLD["facts"])
    assert 'veshavah_el_beit_aviha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Emor, Chapter 6 2', 'Sifra, Emor, Chapter 6 3', 'Sifra, Emor, Chapter 6 4', 'Sifra, Emor, Chapter 6 5', 'Sifra, Emor, Chapter 6 6', 'Sifra, Emor, Chapter 6 7', 'Onkelos Lev 22:14']
    assert all('the_fifths_algebra' not in f for f in m.WORLD["facts"])
    assert 'veyasaf_chamishito' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Sifra, Emor, Chapter 6 8', 'Sifra, Emor, Chapter 6 9', 'Sifra, Emor, Chapter 6 10', 'Onkelos Lev 22:16']
    assert all('the_profaners_and_onkelos_condition' not in f for f in m.WORLD["facts"])
    assert 'velo_yechalelu' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
