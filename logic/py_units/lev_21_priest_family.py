#!/usr/bin/env python3
# =============================================================================
# lev_21_priest_family — 21:1-15
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_21_priest_family.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Priest mourning and marriage limits; high priest (21:1–15)"""
from machine import Machine

m = Machine("lev_21_priest_family")

# -------------------------- Lev.21.1 · ETNACHTA_SPLIT ----------------------
# ויאמר יהוה אל משה אמר אל הכהנים בני אהרן … ואמרת אלהם לנפש לא יטמא בעמיו
# "[EN-AID] From top split: LEFT «ויאמר יהוה אל משה אמר אל הכהנים בני אהרן»
# / RIGHT «ואמרת אלהם לנפש לא יטמא בעמיו». Derive claim from Hebrew arms.
# Lev 21:1."
m.step("Lev.21.1")
# witness-tier presupposed read: addressee_census_and_override on
# emor_el_hakohanim — read, not installed
m.witness_read("emor_el_hakohanim", "addressee_census_and_override",
                cites=["Sifra, Emor, Section 1 1", "Sifra, Emor, Section 1 2", "Sifra, Emor, Section 1 3"])

# -------------------------- Lev.21.2 · COND_כי -----------------------------
# כי אם לשארו הקרב אליו … לאמו ולאביו ולבנו ולבתו ולאחיו
# "[EN-AID] From top split: LEFT «כי אם לשארו הקרב אליו» / RIGHT «לאמו
# ולאביו ולבנו ולבתו ולאחיו». Derive claim from Hebrew arms. Lev 21:2."
m.step("Lev.21.2")
# witness-tier presupposed read: relative_table_by_token_pairs on
# lisheero_hakarov — read, not installed
m.witness_read("lisheero_hakarov", "relative_table_by_token_pairs",
                cites=["Sifra, Emor, Section 1 4", "Sifra, Emor, Section 1 5", "Sifra, Emor, Section 1 6", "Sifra, Emor, Section 1 7", "Sifra, Emor, Section 1 8"])

# -------------------------- Lev.21.3 · ETNACHTA_SPLIT ----------------------
# ולאחתו הבתולה הקרובה אליו אשר לא היתה לאיש … לה יטמא
# "[EN-AID] From top split: LEFT «ולאחתו הבתולה הקרובה אליו אשר לא היתה
# לאיש» / RIGHT «לה יטמא». Derive claim from Hebrew arms. Lev 21:3."
m.step("Lev.21.3")
# witness-tier presupposed read: sister_carve_and_forced_defilement on
# achoto_habetulah — read, not installed
m.witness_read("achoto_habetulah", "sister_carve_and_forced_defilement",
                cites=["Sifra, Emor, Section 1 9", "Sifra, Emor, Section 1 10", "Sifra, Emor, Section 1 11", "Sifra, Emor, Section 1 12", "Sifra, Emor, Section 1 13", "Sifra, Emor, Section 1 14"])

# -------------------------- Lev.21.4 · ETNACHTA_SPLIT ----------------------
# לא יטמא בעל בעמיו
# "[EN-AID] From top split: LEFT «לא יטמא בעל בעמיו» / RIGHT «». Derive
# claim from Hebrew arms. Lev 21:4."
m.step("Lev.21.4")
# witness-tier presupposed read: husband_split_toggle_onkelos_fork on
# lo_yitama_baal — read, not installed
m.witness_read("lo_yitama_baal", "husband_split_toggle_onkelos_fork",
                cites=["Sifra, Emor, Section 1 15", "Sifra, Emor, Section 1 16", "Onkelos Lev 21:4"])

# -------------------------- Lev.21.5 · ETNACHTA_SPLIT ----------------------
# לא יקרחה יקרחו קרחה בראשם ופאת זקנם לא יגלחו … ובבשרם לא ישרטו שרטת
# "[EN-AID] From top split: LEFT «לא יקרחה יקרחו קרחה בראשם ופאת זקנם לא
# יגלחו» / RIGHT «ובבשרם לא ישרטו שרטת». Derive claim from Hebrew arms. Lev
# 21:5."
m.step("Lev.21.5")
# witness-tier presupposed read: mourning_marks_two_way_transfer on
# lo_yikrechu_korchah — read, not installed
m.witness_read("lo_yikrechu_korchah", "mourning_marks_two_way_transfer",
                cites=["Sifra, Emor, Chapter 1 1", "Sifra, Emor, Chapter 1 2", "Sifra, Emor, Chapter 1 3", "Sifra, Emor, Chapter 1 4", "Sifra, Emor, Chapter 1 5"])

# -------------------------- Lev.21.6 · ETNACHTA_SPLIT ----------------------
# קדשים יהיו לאלהיהם ולא יחללו שם אלהיהם … כי את אשי יהוה לחם אלהיהם הם
# מקריבם והיו קדש
# "[EN-AID] From top split: LEFT «קדשים יהיו לאלהיהם ולא יחללו שם אלהיהם» /
# RIGHT «כי את אשי יהוה לחם אלהיהם הם מקריבם והיו קדש». Derive claim from
# Hebrew arms. Lev 21:6."
m.step("Lev.21.6")
# witness-tier presupposed read: holy_by_compulsion on kedoshim_yihyu —
# read, not installed
m.witness_read("kedoshim_yihyu", "holy_by_compulsion",
                cites=["Sifra, Emor, Chapter 1 6", "Onkelos Lev 21:6"])

# -------------------------- Lev.21.7 · ETNACHTA_SPLIT ----------------------
# אשה זנה וחללה לא יקחו ואשה גרושה מאישה לא יקחו … כי קדש הוא לאלהיו
# "[EN-AID] From top split: LEFT «אשה זנה וחללה לא יקחו ואשה גרושה מאישה לא
# יקחו» / RIGHT «כי קדש הוא לאלהיו». Derive claim from Hebrew arms. Lev
# 21:7."
m.step("Lev.21.7")
# witness-tier presupposed read: the_forbidden_wives_file on
# zonah_chalalah_gerushah — read, not installed
m.witness_read("zonah_chalalah_gerushah", "the_forbidden_wives_file",
                cites=["Sifra, Emor, Chapter 1 7", "Sifra, Emor, Chapter 1 8", "Sifra, Emor, Chapter 1 9", "Sifra, Emor, Chapter 1 10", "Sifra, Emor, Chapter 1 11", "Sifra, Emor, Chapter 1 12", "Onkelos Lev 21:7"])

# -------------------------- Lev.21.8 · COND_כי -----------------------------
# וקדשתו כי את לחם אלהיך הוא מקריב … קדש יהיה לך כי קדוש אני יהוה מקדשכם
# "[EN-AID] From top split: LEFT «וקדשתו כי את לחם אלהיך הוא מקריב» / RIGHT
# «קדש יהיה לך כי קדוש אני יהוה מקדשכם». Derive claim from Hebrew arms. Lev
# 21:8."
m.step("Lev.21.8")
# witness-tier presupposed read: sanctify_him_by_force on vekidashto — read,
# not installed
m.witness_read("vekidashto", "sanctify_him_by_force",
                cites=["Sifra, Emor, Chapter 1 13"])

# -------------------------- Lev.21.9 · COND_כי -----------------------------
# ובת איש כהן כי תחל לזנות … את אביה היא מחללת באש תשרף
# "[EN-AID] From top split: LEFT «ובת איש כהן כי תחל לזנות» / RIGHT «את אביה
# היא מחללת באש תשרף». Derive claim from Hebrew arms. Lev 21:9."
m.step("Lev.21.9")
# witness-tier presupposed read: the_priests_daughter_file on
# bat_kohen_ki_techel — read, not installed
m.witness_read("bat_kohen_ki_techel", "the_priests_daughter_file",
                cites=["Sifra, Emor, Chapter 1 14", "Sifra, Emor, Chapter 1 15", "Sifra, Emor, Chapter 1 16", "Sifra, Emor, Chapter 1 17", "Sifra, Emor, Chapter 1 18", "Onkelos Lev 21:9"])

# -------------------------- Lev.21.10 · ETNACHTA_SPLIT ---------------------
# והכהן הגדול מאחיו אשר יוצק על ראשו שמן המשחה ומלא את ידו ללב … את ראשו לא
# יפרע ובגדיו לא יפרם
# "[EN-AID] From top split: LEFT «והכהן הגדול מאחיו אשר יוצק על ראשו שמן
# המשחה ומלא את ידו ללבש את הבגדים» / RIGHT «את ראשו לא יפרע ובגדיו לא
# יפרם». Derive claim from Hebrew arms. Lev 21:10."
m.step("Lev.21.10")
# witness-tier presupposed read: greatness_and_the_one_hour_rule on
# hakohen_hagadol — read, not installed
m.witness_read("hakohen_hagadol", "greatness_and_the_one_hour_rule",
                cites=["Sifra, Emor, Section 2 1", "Sifra, Emor, Section 2 2", "Sifra, Emor, Section 2 3", "Onkelos Lev 21:10"])

# -------------------------- Lev.21.11 · ETNACHTA_SPLIT ---------------------
# ועל כל נפשת מת לא יבא … לאביו ולאמו לא יטמא
# "[EN-AID] From top split: LEFT «ועל כל נפשת מת לא יבא» / RIGHT «לאביו
# ולאמו לא יטמא». Derive claim from Hebrew arms. Lev 21:11."
m.step("Lev.21.11")
# witness-tier presupposed read: the_dead_the_sanctuary_and_the_onen_split
# on al_kol_nafshot_met — read, not installed
m.witness_read("al_kol_nafshot_met", "the_dead_the_sanctuary_and_the_onen_split",
                cites=["Sifra, Emor, Section 2 4", "Sifra, Emor, Section 2 5", "Sifra, Emor, Section 2 6", "Onkelos Lev 21:12"])

# -------------------------- Lev.21.12 · ETNACHTA_SPLIT ---------------------
# ומן המקדש לא יצא ולא יחלל את מקדש אלהיו … כי נזר שמן משחת אלהיו עליו אני
# יהוה
# "[EN-AID] From top split: LEFT «ומן המקדש לא יצא ולא יחלל את מקדש אלהיו» /
# RIGHT «כי נזר שמן משחת אלהיו עליו אני יהוה». Derive claim from Hebrew
# arms. Lev 21:12."
m.step("Lev.21.12")

# -------------------------- Lev.21.13 · TREE_CLAIM -------------------------
# … אשה בבתוליה יקח
# "[EN-AID] From top split: LEFT «» / RIGHT «אשה בבתוליה יקח». Derive claim
# from Hebrew arms. Lev 21:13."
m.step("Lev.21.13")
# witness-tier presupposed read: the_virgin_command on ishah_bivtuleha —
# read, not installed
m.witness_read("ishah_bivtuleha", "the_virgin_command",
                cites=["Sifra, Emor, Section 2 7", "Sifra, Emor, Chapter 2 6"])

# -------------------------- Lev.21.14 · ETNACHTA_SPLIT ---------------------
# אלמנה וגרושה וחללה זנה את אלה לא יקח … כי אם בתולה מעמיו יקח אשה
# "[EN-AID] From top split: LEFT «אלמנה וגרושה וחללה זנה את אלה לא יקח» /
# RIGHT «כי אם בתולה מעמיו יקח אשה». Derive claim from Hebrew arms. Lev
# 21:14."
m.step("Lev.21.14")
# witness-tier presupposed read: the_profaned_seed_layer on almanah_ugrushah
# — read, not installed
m.witness_read("almanah_ugrushah", "the_profaned_seed_layer",
                cites=["Sifra, Emor, Chapter 2 1", "Sifra, Emor, Chapter 2 2", "Sifra, Emor, Chapter 2 4", "Sifra, Emor, Chapter 2 5", "Sifra, Emor, Chapter 2 7", "Sifra, Emor, Chapter 2 8", "Onkelos Lev 21:14"])

# -------------------------- Lev.21.15 · ETNACHTA_SPLIT ---------------------
# ולא יחלל זרעו בעמיו … כי אני יהוה מקדשו
# "[EN-AID] From top split: LEFT «ולא יחלל זרעו בעמיו» / RIGHT «כי אני יהוה
# מקדשו». Derive claim from Hebrew arms. Lev 21:15."
m.step("Lev.21.15")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('emor_el_hakohanim', 'addressee_census_and_override'), ('lisheero_hakarov', 'relative_table_by_token_pairs'), ('achoto_habetulah', 'sister_carve_and_forced_defilement'), ('lo_yitama_baal', 'husband_split_toggle_onkelos_fork'), ('lo_yikrechu_korchah', 'mourning_marks_two_way_transfer'), ('kedoshim_yihyu', 'holy_by_compulsion'), ('zonah_chalalah_gerushah', 'the_forbidden_wives_file'), ('vekidashto', 'sanctify_him_by_force'), ('bat_kohen_ki_techel', 'the_priests_daughter_file'), ('hakohen_hagadol', 'greatness_and_the_one_hour_rule'), ('al_kol_nafshot_met', 'the_dead_the_sanctuary_and_the_onen_split'), ('ishah_bivtuleha', 'the_virgin_command'), ('almanah_ugrushah', 'the_profaned_seed_layer')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Emor, Section 1 1', 'Sifra, Emor, Section 1 2', 'Sifra, Emor, Section 1 3']
    assert all('addressee_census_and_override' not in f for f in m.WORLD["facts"])
    assert 'emor_el_hakohanim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Emor, Section 1 4', 'Sifra, Emor, Section 1 5', 'Sifra, Emor, Section 1 6', 'Sifra, Emor, Section 1 7', 'Sifra, Emor, Section 1 8']
    assert all('relative_table_by_token_pairs' not in f for f in m.WORLD["facts"])
    assert 'lisheero_hakarov' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Emor, Section 1 9', 'Sifra, Emor, Section 1 10', 'Sifra, Emor, Section 1 11', 'Sifra, Emor, Section 1 12', 'Sifra, Emor, Section 1 13', 'Sifra, Emor, Section 1 14']
    assert all('sister_carve_and_forced_defilement' not in f for f in m.WORLD["facts"])
    assert 'achoto_habetulah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Emor, Section 1 15', 'Sifra, Emor, Section 1 16', 'Onkelos Lev 21:4']
    assert all('husband_split_toggle_onkelos_fork' not in f for f in m.WORLD["facts"])
    assert 'lo_yitama_baal' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Emor, Chapter 1 1', 'Sifra, Emor, Chapter 1 2', 'Sifra, Emor, Chapter 1 3', 'Sifra, Emor, Chapter 1 4', 'Sifra, Emor, Chapter 1 5']
    assert all('mourning_marks_two_way_transfer' not in f for f in m.WORLD["facts"])
    assert 'lo_yikrechu_korchah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Emor, Chapter 1 6', 'Onkelos Lev 21:6']
    assert all('holy_by_compulsion' not in f for f in m.WORLD["facts"])
    assert 'kedoshim_yihyu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Emor, Chapter 1 7', 'Sifra, Emor, Chapter 1 8', 'Sifra, Emor, Chapter 1 9', 'Sifra, Emor, Chapter 1 10', 'Sifra, Emor, Chapter 1 11', 'Sifra, Emor, Chapter 1 12', 'Onkelos Lev 21:7']
    assert all('the_forbidden_wives_file' not in f for f in m.WORLD["facts"])
    assert 'zonah_chalalah_gerushah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Emor, Chapter 1 13']
    assert all('sanctify_him_by_force' not in f for f in m.WORLD["facts"])
    assert 'vekidashto' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Emor, Chapter 1 14', 'Sifra, Emor, Chapter 1 15', 'Sifra, Emor, Chapter 1 16', 'Sifra, Emor, Chapter 1 17', 'Sifra, Emor, Chapter 1 18', 'Onkelos Lev 21:9']
    assert all('the_priests_daughter_file' not in f for f in m.WORLD["facts"])
    assert 'bat_kohen_ki_techel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Emor, Section 2 1', 'Sifra, Emor, Section 2 2', 'Sifra, Emor, Section 2 3', 'Onkelos Lev 21:10']
    assert all('greatness_and_the_one_hour_rule' not in f for f in m.WORLD["facts"])
    assert 'hakohen_hagadol' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Sifra, Emor, Section 2 4', 'Sifra, Emor, Section 2 5', 'Sifra, Emor, Section 2 6', 'Onkelos Lev 21:12']
    assert all('the_dead_the_sanctuary_and_the_onen_split' not in f for f in m.WORLD["facts"])
    assert 'al_kol_nafshot_met' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Sifra, Emor, Section 2 7', 'Sifra, Emor, Chapter 2 6']
    assert all('the_virgin_command' not in f for f in m.WORLD["facts"])
    assert 'ishah_bivtuleha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Sifra, Emor, Chapter 2 1', 'Sifra, Emor, Chapter 2 2', 'Sifra, Emor, Chapter 2 4', 'Sifra, Emor, Chapter 2 5', 'Sifra, Emor, Chapter 2 7', 'Sifra, Emor, Chapter 2 8', 'Onkelos Lev 21:14']
    assert all('the_profaned_seed_layer' not in f for f in m.WORLD["facts"])
    assert 'almanah_ugrushah' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
