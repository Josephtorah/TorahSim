#!/usr/bin/env python3
# =============================================================================
# lev_01_olah_bird — 1:14-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_01_olah_bird.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Olah bird (turtledove/pigeon) procedure (1:14–17)"""
from machine import Machine

m = Machine("lev_01_olah_bird")

# -------------------------- Lev.1.14 · COND_ואם ----------------------------
# ואם מן העוף עלה קרבנו ליהוה … והקריב מן התרים או מן בני היונה את קרבנו
# "[EN-AID] From top split: LEFT «ואם מן העוף עלה קרבנו ליהוה» / RIGHT
# «והקריב מן התרים או מן בני היונה את קרבנו». Derive claim from Hebrew arms.
# Lev 1:14."
m.step("Lev.1.14")
# witness-tier presupposed read: complementary_windows_no_sex_predicate on
# bird_spec — read, not installed
m.witness_read("bird_spec", "complementary_windows_no_sex_predicate",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 8 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 8 5", "Sifra, Vayikra Dibbura DeNedavah, Section 6 3", "Sifra, Vayikra Dibbura DeNedavah, Section 6 5", "Sifra, Vayikra Dibbura DeNedavah, Section 6 6", "Sifra, Vayikra Dibbura DeNedavah, Chapter 8 1", "Sifra, Vayikra Dibbura DeNedavah, Section 7 1"])

# -------------------------- Lev.1.15 · ETNACHTA_SPLIT ----------------------
# והקריבו הכהן אל המזבח ומלק את ראשו והקטיר המזבחה … ונמצה דמו על קיר המזבח
# "[EN-AID] From top split: LEFT «והקריבו הכהן אל המזבח ומלק את ראשו והקטיר
# המזבחה» / RIGHT «ונמצה דמו על קיר המזבח». Derive claim from Hebrew arms.
# Lev 1:15."
m.step("Lev.1.15")
# witness-tier presupposed read: fingernail_majority_blood on pinch_rite —
# read, not installed
m.witness_read("pinch_rite", "fingernail_majority_blood",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 7 3", "Sifra, Vayikra Dibbura DeNedavah, Section 7 4", "Sifra, Vayikra Dibbura DeNedavah, Section 7 6", "Sifra, Vayikra Dibbura DeNedavah, Section 7 7", "Sifra, Vayikra Dibbura DeNedavah, Section 7 8", "Sifra, Vayikra Dibbura DeNedavah, Chapter 9 7"])

# -------------------------- Lev.1.16 · ETNACHTA_SPLIT ----------------------
# והסיר את מראתו בנצתה … והשליך אתה אצל המזבח קדמה אל מקום הדשן
# "[EN-AID] From top split: LEFT «והסיר את מראתו בנצתה» / RIGHT «והשליך אתה
# אצל המזבח קדמה אל מקום הדשן». Derive claim from Hebrew arms. Lev 1:16."
m.step("Lev.1.16")
# witness-tier presupposed read: contents_vote_two_depositories on
# crop_registry — read, not installed
m.witness_read("crop_registry", "contents_vote_two_depositories",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 7 9", "Sifra, Vayikra Dibbura DeNedavah, Chapter 9 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 9 3", "Onkelos Lev 1:16"])

# -------------------------- Lev.1.17 · ETNACHTA_SPLIT ----------------------
# ושסע אתו בכנפיו לא יבדיל והקטיר אתו הכהן המזבחה על העצים אשר … עלה הוא אשה
# ריח ניחח ליהוה
# "[EN-AID] From top split: LEFT «ושסע אתו בכנפיו לא יבדיל והקטיר אתו הכהן
# המזבחה על העצים אשר על האש» / RIGHT «עלה הוא אשה ריח ניחח ליהוה». Derive
# claim from Hebrew arms. Lev 1:17."
m.step("Lev.1.17")
# witness-tier presupposed read: feathers_up_knife_fatal on rend_severity —
# read, not installed
m.witness_read("rend_severity", "feathers_up_knife_fatal",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 9 5", "Sifra, Vayikra Dibbura DeNedavah, Chapter 9 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 9 6"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('bird_spec', 'complementary_windows_no_sex_predicate'), ('pinch_rite', 'fingernail_majority_blood'), ('crop_registry', 'contents_vote_two_depositories'), ('rend_severity', 'feathers_up_knife_fatal')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 8 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 8 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 6 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 6 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 6 6', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 8 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 7 1']
    assert all('complementary_windows_no_sex_predicate' not in f for f in m.WORLD["facts"])
    assert 'bird_spec' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 7 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 7 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 7 6', 'Sifra, Vayikra Dibbura DeNedavah, Section 7 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 7 8', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 9 7']
    assert all('fingernail_majority_blood' not in f for f in m.WORLD["facts"])
    assert 'pinch_rite' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 7 9', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 9 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 9 3', 'Onkelos Lev 1:16']
    assert all('contents_vote_two_depositories' not in f for f in m.WORLD["facts"])
    assert 'crop_registry' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 9 5', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 9 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 9 6']
    assert all('feathers_up_knife_fatal' not in f for f in m.WORLD["facts"])
    assert 'rend_severity' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
