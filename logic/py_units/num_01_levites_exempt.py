#!/usr/bin/env python3
# =============================================================================
# num_01_levites_exempt — 1:47-54
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/num_01_levites_exempt.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Levites not in war census; camp charge of mishkan (1:47–54)"""
from machine import Machine

m = Machine("num_01_levites_exempt")

# -------------------------- Num.1.47 · ETNACHTA_SPLIT ----------------------
# ‹והלוים למטה אבתם› (“and-the-Levite to-staff/tribe father-them/their”)
# ‹… לא התפקדו בתוכם› (“not count/visit in-midst-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:47."
m.step("Num.1.47")
# witness-tier presupposed read: the_exclusion on vehaleviyim_lo_hotpakdu —
# read, not installed
m.witness_read("vehaleviyim_lo_hotpakdu", "the_exclusion",
                cites=["Onkelos Num 1:47", "Onkelos Num 1:48", "Onkelos Num 1:49"])

# -------------------------- Num.1.48 · TREE_CLAIM --------------------------
# ‹וידבר יהוה … אל› (“and-speak YHWH … to”)
# ‹משה לאמר› (“Moses to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:48."
m.step("Num.1.48")

# -------------------------- Num.1.49 · ETNACHTA_SPLIT ----------------------
# ‹אך את מטה› (“indeed obj-marker staff/tribe”)
# ‹לוי לא תפקד› (“Levi not count/visit”)
# ‹ואת ראשם לא› (“and-obj-marker head-them/their not”)
# ‹תשא … בתוך בני› (“lift/carry … in-midst son”)
# ‹ישראל› (“Israel”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:49."
m.step("Num.1.49")

# -------------------------- Num.1.50 · ETNACHTA_SPLIT ----------------------
# ‹ואתה הפקד את› (“and-you count/visit obj-marker”)
# ‹הלוים על משכן› (“the-Levite over tabernacle”)
# ‹העדת ועל כל› (“the-testimony and-over all”)
# ‹כליו ועל כל› (“vessel-him/its and-over all”)
# ‹אשר לו המ› (“which to-him/its ?”)
# ‹… וסביב למשכן יחנו› (“and-circle to-tabernacle encamp”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:50."
m.step("Num.1.50")
# witness-tier presupposed read: the_appointment_and_the_stranger on
# hafked_et_haleviyim — read, not installed
m.witness_read("hafked_et_haleviyim", "the_appointment_and_the_stranger",
                cites=["Onkelos Num 1:50", "Onkelos Num 1:51"])

# -------------------------- Num.1.51 · ETNACHTA_SPLIT ----------------------
# ‹ובנסע המשכן יורידו› (“and-in-journey the-tabernacle go-down”)
# ‹אתו הלוים ובחנת› (“obj-marker-him/its the-Levite and-in-encamp”)
# ‹המשכן יקימו אתו› (“the-tabernacle arise obj-marker-him/its”)
# ‹הלוים … והזר הקרב› (“the-Levite … and-the-turn-aside the-bring-near”)
# ‹יומת› (“die”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:51."
m.step("Num.1.51")

# -------------------------- Num.1.52 · ETNACHTA_SPLIT ----------------------
# ‹וחנו בני ישראל› (“and-encamp son Israel”)
# ‹… איש על מחנהו› (“man over camp-him/its”)
# ‹ואיש על דגלו› (“and-man over flag-him/its”)
# ‹לצבאתם› (“to-host-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:52."
m.step("Num.1.52")
# witness-tier presupposed read: the_banner_the_wrath_shield_the_run on
# ish_al_diglo — read, not installed
m.witness_read("ish_al_diglo", "the_banner_the_wrath_shield_the_run",
                cites=["Onkelos Num 1:52", "Onkelos Num 1:53", "Onkelos Num 1:54"])

# -------------------------- Num.1.53 · ETNACHTA_SPLIT ----------------------
# ‹והלוים יחנו סביב› (“and-the-Levite encamp circle”)
# ‹למשכן העדת ולא› (“to-tabernacle the-testimony and-not”)
# ‹יהיה קצף על› (“be splinter over”)
# ‹עדת בני ישראל› (“congregation son Israel”)
# ‹… ושמרו הלוים את› (“and-keep/guard the-Levite obj-marker”)
# ‹משמרת משכן העדות› (“watch tabernacle the-testimony”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:53."
m.step("Num.1.53")

# -------------------------- Num.1.54 · ETNACHTA_SPLIT ----------------------
# ‹ויעשו בני ישראל› (“and-make son Israel”)
# ‹… ככל אשר צוה› (“like-all which command”)
# ‹יהוה את משה› (“YHWH obj-marker Moses”)
# ‹כן עשו› (“so make”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 1:54."
m.step("Num.1.54")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('vehaleviyim_lo_hotpakdu', 'the_exclusion'), ('hafked_et_haleviyim', 'the_appointment_and_the_stranger'), ('ish_al_diglo', 'the_banner_the_wrath_shield_the_run')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Num 1:47', 'Onkelos Num 1:48', 'Onkelos Num 1:49']
    assert all('the_exclusion' not in f for f in m.WORLD["facts"])
    assert 'vehaleviyim_lo_hotpakdu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Onkelos Num 1:50', 'Onkelos Num 1:51']
    assert all('the_appointment_and_the_stranger' not in f for f in m.WORLD["facts"])
    assert 'hafked_et_haleviyim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Num 1:52', 'Onkelos Num 1:53', 'Onkelos Num 1:54']
    assert all('the_banner_the_wrath_shield_the_run' not in f for f in m.WORLD["facts"])
    assert 'ish_al_diglo' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
