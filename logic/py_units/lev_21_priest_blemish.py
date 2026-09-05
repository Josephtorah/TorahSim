#!/usr/bin/env python3
# =============================================================================
# lev_21_priest_blemish — 21:16-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_21_priest_blemish.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Blemished priest: may eat holy; not approach to offer (21:16–24)"""
from machine import Machine

m = Machine("lev_21_priest_blemish")

# -------------------------- Lev.21.16 · TREE_CLAIM -------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 21:16."
m.step("Lev.21.16")

# -------------------------- Lev.21.17 · ETNACHTA_SPLIT ---------------------
# דבר אל אהרן לאמר … איש מזרעך לדרתם אשר יהיה בו מום לא יקרב להקריב לחם
# אלהיו
# "[EN-AID] From top split: LEFT «דבר אל אהרן לאמר» / RIGHT «איש מזרעך לדרתם
# אשר יהיה בו מום לא יקרב להקריב לחם אלהיו». Derive claim from Hebrew arms.
# Lev 21:17."
m.step("Lev.21.17")
# witness-tier presupposed read: age_ladder_and_service_census on
# asher_yihyeh_bo_mum — read, not installed
m.witness_read("asher_yihyeh_bo_mum", "age_ladder_and_service_census",
                cites=["Sifra, Emor, Section 3 1", "Sifra, Emor, Section 3 2", "Sifra, Emor, Section 3 3", "Sifra, Emor, Section 3 4", "Sifra, Emor, Section 3 5", "Onkelos Lev 21:17"])

# -------------------------- Lev.21.18 · COND_כי ----------------------------
# כי כל איש אשר בו מום לא יקרב … איש עור או פסח או חרם או שרוע
# "[EN-AID] From top split: LEFT «כי כל איש אשר בו מום לא יקרב» / RIGHT «איש
# עור או פסח או חרם או שרוע». Derive claim from Hebrew arms. Lev 21:18."
m.step("Lev.21.18")
# witness-tier presupposed read: the_first_blemish_row on iver_o_piseach —
# read, not installed
m.witness_read("iver_o_piseach", "the_first_blemish_row",
                cites=["Sifra, Emor, Section 3 6", "Sifra, Emor, Section 3 7", "Sifra, Emor, Section 3 8", "Sifra, Emor, Section 3 9", "Onkelos Lev 21:18"])

# -------------------------- Lev.21.19 · ETNACHTA_SPLIT ---------------------
# או איש אשר יהיה בו שבר רגל … או שבר יד
# "[EN-AID] From top split: LEFT «או איש אשר יהיה בו שבר רגל» / RIGHT «או
# שבר יד». Derive claim from Hebrew arms. Lev 21:19."
m.step("Lev.21.19")
# witness-tier presupposed read: the_fracture_row on shever_regel_o_yad —
# read, not installed
m.witness_read("shever_regel_o_yad", "the_fracture_row",
                cites=["Sifra, Emor, Section 3 10", "Sifra, Emor, Section 3 11"])

# -------------------------- Lev.21.20 · ETNACHTA_SPLIT ---------------------
# או גבן או דק או תבלל בעינו … או גרב או ילפת או מרוח אשך
# "[EN-AID] From top split: LEFT «או גבן או דק או תבלל בעינו» / RIGHT «או
# גרב או ילפת או מרוח אשך». Derive claim from Hebrew arms. Lev 21:20."
m.step("Lev.21.20")
# witness-tier presupposed read: eye_and_skin_row_onkelos_rulings on
# giben_dak_tevalul — read, not installed
m.witness_read("giben_dak_tevalul", "eye_and_skin_row_onkelos_rulings",
                cites=["Sifra, Emor, Section 3 12", "Sifra, Emor, Section 3 13", "Sifra, Emor, Section 3 14", "Sifra, Emor, Section 3 15", "Onkelos Lev 21:20"])

# -------------------------- Lev.21.21 · ETNACHTA_SPLIT ---------------------
# כל איש אשר בו מום מזרע אהרן הכהן לא יגש להקריב את אשי יהוה … מום בו את לחם
# אלהיו לא יגש להקריב
# "[EN-AID] From top split: LEFT «כל איש אשר בו מום מזרע אהרן הכהן לא יגש
# להקריב את אשי יהוה» / RIGHT «מום בו את לחם אלהיו לא יגש להקריב». Derive
# claim from Hebrew arms. Lev 21:21."
m.step("Lev.21.21")
# witness-tier presupposed read: man_beast_difference_table on
# kol_ish_asher_bo_mum — read, not installed
m.witness_read("kol_ish_asher_bo_mum", "man_beast_difference_table",
                cites=["Sifra, Emor, Chapter 3 1", "Sifra, Emor, Chapter 3 2", "Sifra, Emor, Chapter 3 3", "Sifra, Emor, Chapter 3 4", "Sifra, Emor, Chapter 3 5", "Sifra, Emor, Chapter 3 6", "Sifra, Emor, Chapter 3 7"])

# -------------------------- Lev.21.22 · ETNACHTA_SPLIT ---------------------
# לחם אלהיו מקדשי הקדשים … ומן הקדשים יאכל
# "[EN-AID] From top split: LEFT «לחם אלהיו מקדשי הקדשים» / RIGHT «ומן
# הקדשים יאכל». Derive claim from Hebrew arms. Lev 21:22."
m.step("Lev.21.22")
# witness-tier presupposed read: the_blemished_eat_everything on
# lechem_elohav_yochel — read, not installed
m.witness_read("lechem_elohav_yochel", "the_blemished_eat_everything",
                cites=["Sifra, Emor, Chapter 3 8", "Sifra, Emor, Chapter 3 9", "Onkelos Lev 21:22"])

# -------------------------- Lev.21.23 · ETNACHTA_SPLIT ---------------------
# אך אל הפרכת לא יבא ואל המזבח לא יגש כי מום בו … ולא יחלל את מקדשי כי אני
# יהוה מקדשם
# "[EN-AID] From top split: LEFT «אך אל הפרכת לא יבא ואל המזבח לא יגש כי מום
# בו» / RIGHT «ולא יחלל את מקדשי כי אני יהוה מקדשם». Derive claim from
# Hebrew arms. Lev 21:23."
m.step("Lev.21.23")
# witness-tier presupposed read: entry_hierarchy_and_transmission_chain on
# ach_el_haparochet — read, not installed
m.witness_read("ach_el_haparochet", "entry_hierarchy_and_transmission_chain",
                cites=["Sifra, Emor, Chapter 3 10", "Sifra, Emor, Chapter 3 11", "Sifra, Emor, Chapter 3 12", "Onkelos Lev 21:23"])

# -------------------------- Lev.21.24 · ETNACHTA_SPLIT ---------------------
# וידבר משה אל אהרן ואל בניו … ואל כל בני ישראל
# "[EN-AID] From top split: LEFT «וידבר משה אל אהרן ואל בניו» / RIGHT «ואל
# כל בני ישראל». Derive claim from Hebrew arms. Lev 21:24."
m.step("Lev.21.24")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('asher_yihyeh_bo_mum', 'age_ladder_and_service_census'), ('iver_o_piseach', 'the_first_blemish_row'), ('shever_regel_o_yad', 'the_fracture_row'), ('giben_dak_tevalul', 'eye_and_skin_row_onkelos_rulings'), ('kol_ish_asher_bo_mum', 'man_beast_difference_table'), ('lechem_elohav_yochel', 'the_blemished_eat_everything'), ('ach_el_haparochet', 'entry_hierarchy_and_transmission_chain')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Emor, Section 3 1', 'Sifra, Emor, Section 3 2', 'Sifra, Emor, Section 3 3', 'Sifra, Emor, Section 3 4', 'Sifra, Emor, Section 3 5', 'Onkelos Lev 21:17']
    assert all('age_ladder_and_service_census' not in f for f in m.WORLD["facts"])
    assert 'asher_yihyeh_bo_mum' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Emor, Section 3 6', 'Sifra, Emor, Section 3 7', 'Sifra, Emor, Section 3 8', 'Sifra, Emor, Section 3 9', 'Onkelos Lev 21:18']
    assert all('the_first_blemish_row' not in f for f in m.WORLD["facts"])
    assert 'iver_o_piseach' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Emor, Section 3 10', 'Sifra, Emor, Section 3 11']
    assert all('the_fracture_row' not in f for f in m.WORLD["facts"])
    assert 'shever_regel_o_yad' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Emor, Section 3 12', 'Sifra, Emor, Section 3 13', 'Sifra, Emor, Section 3 14', 'Sifra, Emor, Section 3 15', 'Onkelos Lev 21:20']
    assert all('eye_and_skin_row_onkelos_rulings' not in f for f in m.WORLD["facts"])
    assert 'giben_dak_tevalul' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Emor, Chapter 3 1', 'Sifra, Emor, Chapter 3 2', 'Sifra, Emor, Chapter 3 3', 'Sifra, Emor, Chapter 3 4', 'Sifra, Emor, Chapter 3 5', 'Sifra, Emor, Chapter 3 6', 'Sifra, Emor, Chapter 3 7']
    assert all('man_beast_difference_table' not in f for f in m.WORLD["facts"])
    assert 'kol_ish_asher_bo_mum' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Emor, Chapter 3 8', 'Sifra, Emor, Chapter 3 9', 'Onkelos Lev 21:22']
    assert all('the_blemished_eat_everything' not in f for f in m.WORLD["facts"])
    assert 'lechem_elohav_yochel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Emor, Chapter 3 10', 'Sifra, Emor, Chapter 3 11', 'Sifra, Emor, Chapter 3 12', 'Onkelos Lev 21:23']
    assert all('entry_hierarchy_and_transmission_chain' not in f for f in m.WORLD["facts"])
    assert 'ach_el_haparochet' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
