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
# ‹ויאמר יהוה אל› (“and-say YHWH to”)
# ‹משה אמר אל› (“Moses say to”)
# ‹הכהנים בני אהרן› (“the-priest son Aaron”)
# ‹… ואמרת אלהם לנפש› (“and-say to-them/their to-living-being”)
# ‹לא יטמא בעמיו› (“not be-foul in-people-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:1."
m.step("Lev.21.1")
# witness-tier presupposed read: addressee_census_and_override on
# emor_el_hakohanim — read, not installed
m.witness_read("emor_el_hakohanim", "addressee_census_and_override",
                cites=["Sifra, Emor, Section 1 1", "Sifra, Emor, Section 1 2", "Sifra, Emor, Section 1 3"])

# -------------------------- Lev.21.2 · COND_כי (“very-widely-used-as-a-relati”) -
# ‹כי אם לשארו› (“very-widely-used-as-a-relati as-demonstrative to-flesh-
# him/its”)
# ‹הקרב אליו … לאמו› (“the-near to-him/its … to-mother-him/its”)
# ‹ולאביו ולבנו ולבתו› (“and-to-father-him/its and-to-son-him/its and-to-
# daughter-him/its”)
# ‹ולאחיו› (“and-to-brother-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:2."
m.step("Lev.21.2")
# witness-tier presupposed read: relative_table_by_token_pairs on
# lisheero_hakarov — read, not installed
m.witness_read("lisheero_hakarov", "relative_table_by_token_pairs",
                cites=["Sifra, Emor, Section 1 4", "Sifra, Emor, Section 1 5", "Sifra, Emor, Section 1 6", "Sifra, Emor, Section 1 7", "Sifra, Emor, Section 1 8"])

# -------------------------- Lev.21.3 · ETNACHTA_SPLIT ----------------------
# ‹ולאחתו הבתולה הקרובה› (“and-to-sister-him/its the-virgin the-near”)
# ‹אליו אשר לא› (“to-him/its which not”)
# ‹היתה לאיש … לה› (“be to-man … to-her/its”)
# ‹יטמא› (“be-foul”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:3."
m.step("Lev.21.3")
# witness-tier presupposed read: sister_carve_and_forced_defilement on
# achoto_habetulah — read, not installed
m.witness_read("achoto_habetulah", "sister_carve_and_forced_defilement",
                cites=["Sifra, Emor, Section 1 9", "Sifra, Emor, Section 1 10", "Sifra, Emor, Section 1 11", "Sifra, Emor, Section 1 12", "Sifra, Emor, Section 1 13", "Sifra, Emor, Section 1 14"])

# -------------------------- Lev.21.4 · ETNACHTA_SPLIT ----------------------
# ‹לא יטמא בעל› (“not be-foul master”)
# ‹בעמיו› (“in-people-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms. Lev 21:4."
m.step("Lev.21.4")
# witness-tier presupposed read: husband_split_toggle_onkelos_fork on
# lo_yitama_baal — read, not installed
m.witness_read("lo_yitama_baal", "husband_split_toggle_onkelos_fork",
                cites=["Sifra, Emor, Section 1 15", "Sifra, Emor, Section 1 16", "Onkelos Lev 21:4"])

# -------------------------- Lev.21.5 · ETNACHTA_SPLIT ----------------------
# ‹לא יקרחה יקרחו› (“not depilate depilate”)
# ‹קרחה בראשם ופאת› (“baldness in-head-them/their and-mouth-in-a-figurative-
# sense”)
# ‹זקנם לא יגלחו› (“beard-them/their not be-bald”)
# ‹… ובבשרם לא ישרטו› (“and-in-flesh-them/their not gash”)
# ‹שרטת› (“incision”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:5."
m.step("Lev.21.5")
# witness-tier presupposed read: mourning_marks_two_way_transfer on
# lo_yikrechu_korchah — read, not installed
m.witness_read("lo_yikrechu_korchah", "mourning_marks_two_way_transfer",
                cites=["Sifra, Emor, Chapter 1 1", "Sifra, Emor, Chapter 1 2", "Sifra, Emor, Chapter 1 3", "Sifra, Emor, Chapter 1 4", "Sifra, Emor, Chapter 1 5"])

# -------------------------- Lev.21.6 · ETNACHTA_SPLIT ----------------------
# ‹קדשים יהיו לאלהיהם› (“sacred be to-God-them/their”)
# ‹ולא יחללו שם› (“and-not bore name”)
# ‹אלהיהם … כי את› (“God-them/their … that obj-marker”)
# ‹אשי יהוה לחם› (“fire-offering YHWH food”)
# ‹אלהיהם הם מקריבם› (“God-them/their they bring-near”)
# ‹והיו קדש› (“and-be holiness”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:6."
m.step("Lev.21.6")
# witness-tier presupposed read: holy_by_compulsion on kedoshim_yihyu —
# read, not installed
m.witness_read("kedoshim_yihyu", "holy_by_compulsion",
                cites=["Sifra, Emor, Chapter 1 6", "Onkelos Lev 21:6"])

# -------------------------- Lev.21.7 · ETNACHTA_SPLIT ----------------------
# ‹אשה זנה וחללה› (“woman commit-adultery and-pierced”)
# ‹לא יקחו ואשה› (“not take and-woman”)
# ‹גרושה מאישה לא› (“drive-out-from-a-possession from-man-her/its not”)
# ‹יקחו … כי קדש› (“take … that sacred”)
# ‹הוא לאלהיו› (“he/it to-God-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:7."
m.step("Lev.21.7")
# witness-tier presupposed read: the_forbidden_wives_file on
# zonah_chalalah_gerushah — read, not installed
m.witness_read("zonah_chalalah_gerushah", "the_forbidden_wives_file",
                cites=["Sifra, Emor, Chapter 1 7", "Sifra, Emor, Chapter 1 8", "Sifra, Emor, Chapter 1 9", "Sifra, Emor, Chapter 1 10", "Sifra, Emor, Chapter 1 11", "Sifra, Emor, Chapter 1 12", "Onkelos Lev 21:7"])

# -------------------------- Lev.21.8 · COND_כי (“that”) --------------------
# ‹וקדשתו כי את› (“and-sanctify-him/its that obj-marker”)
# ‹לחם אלהיך הוא› (“food God-you/your he/it”)
# ‹מקריב … קדש יהיה› (“bring-near … sacred be”)
# ‹לך כי קדוש› (“to-you/your that sacred”)
# ‹אני יהוה מקדשכם› (“YHWH sanctify-you/your(pl)”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:8."
m.step("Lev.21.8")
# witness-tier presupposed read: sanctify_him_by_force on vekidashto — read,
# not installed
m.witness_read("vekidashto", "sanctify_him_by_force",
                cites=["Sifra, Emor, Chapter 1 13"])

# -------------------------- Lev.21.9 · COND_כי (“that”) --------------------
# ‹ובת איש כהן› (“and-daughter man priest”)
# ‹כי תחל לזנות› (“that bore to-commit-adultery”)
# ‹… את אביה היא› (“obj-marker father-her/its he/it”)
# ‹מחללת באש תשרף› (“bore in-fire be-on-fire”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:9."
m.step("Lev.21.9")
# witness-tier presupposed read: the_priests_daughter_file on
# bat_kohen_ki_techel — read, not installed
m.witness_read("bat_kohen_ki_techel", "the_priests_daughter_file",
                cites=["Sifra, Emor, Chapter 1 14", "Sifra, Emor, Chapter 1 15", "Sifra, Emor, Chapter 1 16", "Sifra, Emor, Chapter 1 17", "Sifra, Emor, Chapter 1 18", "Onkelos Lev 21:9"])

# -------------------------- Lev.21.10 · ETNACHTA_SPLIT ---------------------
# ‹והכהן הגדול מאחיו› (“and-the-priest the-great from-brother-him/its”)
# ‹אשר יוצק על› (“which pour-out over”)
# ‹ראשו שמן המשחה› (“head-him/its oil the-unction”)
# ‹ומלא את ידו› (“and-fill obj-marker hand-him/its”)
# ‹ללב … את ראשו› (“? … obj-marker head-him/its”)
# ‹לא יפרע ובגדיו› (“not loosen and-garment-him/its”)
# ‹לא יפרם› (“not tear”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:10."
m.step("Lev.21.10")
# witness-tier presupposed read: greatness_and_the_one_hour_rule on
# hakohen_hagadol — read, not installed
m.witness_read("hakohen_hagadol", "greatness_and_the_one_hour_rule",
                cites=["Sifra, Emor, Section 2 1", "Sifra, Emor, Section 2 2", "Sifra, Emor, Section 2 3", "Onkelos Lev 21:10"])

# -------------------------- Lev.21.11 · ETNACHTA_SPLIT ---------------------
# ‹ועל כל נפשת› (“and-over all living-being”)
# ‹מת לא יבא› (“die not come/bring”)
# ‹… לאביו ולאמו לא› (“to-father-him/its and-to-mother-him/its not”)
# ‹יטמא› (“be-foul”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:11."
m.step("Lev.21.11")
# witness-tier presupposed read: the_dead_the_sanctuary_and_the_onen_split
# on al_kol_nafshot_met — read, not installed
m.witness_read("al_kol_nafshot_met", "the_dead_the_sanctuary_and_the_onen_split",
                cites=["Sifra, Emor, Section 2 4", "Sifra, Emor, Section 2 5", "Sifra, Emor, Section 2 6", "Onkelos Lev 21:12"])

# -------------------------- Lev.21.12 · ETNACHTA_SPLIT ---------------------
# ‹ומן המקדש לא› (“and-from the-consecrated-thing not”)
# ‹יצא ולא יחלל› (“bring-forth and-not bore”)
# ‹את מקדש אלהיו› (“obj-marker consecrated-thing God-him/its”)
# ‹… כי נזר שמן› (“that something-set-apart oil”)
# ‹משחת אלהיו עליו› (“unction God-him/its over-him/its”)
# ‹אני יהוה› (“YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:12."
m.step("Lev.21.12")

# -------------------------- Lev.21.13 · TREE_CLAIM -------------------------
# ‹… אשה בבתוליה יקח› (“woman in-virginity-her/its take”)
# "[EN-AID] From top split: LEFT «» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:13."
m.step("Lev.21.13")
# witness-tier presupposed read: the_virgin_command on ishah_bivtuleha —
# read, not installed
m.witness_read("ishah_bivtuleha", "the_virgin_command",
                cites=["Sifra, Emor, Section 2 7", "Sifra, Emor, Chapter 2 6"])

# -------------------------- Lev.21.14 · ETNACHTA_SPLIT ---------------------
# ‹אלמנה וגרושה וחללה› (“widow and-drive-out-from-a-possession and-pierced”)
# ‹זנה את אלה› (“commit-adultery obj-marker these”)
# ‹לא יקח … כי› (“not take … very-widely-used-as-a-relati”)
# ‹אם בתולה מעמיו› (“as-demonstrative virgin from-people-him/its”)
# ‹יקח אשה› (“take woman”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:14."
m.step("Lev.21.14")
# witness-tier presupposed read: the_profaned_seed_layer on almanah_ugrushah
# — read, not installed
m.witness_read("almanah_ugrushah", "the_profaned_seed_layer",
                cites=["Sifra, Emor, Chapter 2 1", "Sifra, Emor, Chapter 2 2", "Sifra, Emor, Chapter 2 4", "Sifra, Emor, Chapter 2 5", "Sifra, Emor, Chapter 2 7", "Sifra, Emor, Chapter 2 8", "Onkelos Lev 21:14"])

# -------------------------- Lev.21.15 · ETNACHTA_SPLIT ---------------------
# ‹ולא יחלל זרעו› (“and-not bore seed-him/its”)
# ‹בעמיו … כי אני› (“in-people-him/its … that”)
# ‹יהוה מקדשו› (“YHWH sanctify-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 21:15."
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
