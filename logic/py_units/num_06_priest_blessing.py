#!/usr/bin/env python3
# =============================================================================
# num_06_priest_blessing — 6:22-27
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/num_06_priest_blessing.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Priestly blessing (birkat kohanim) (6:22–27)"""
from machine import Machine

m = Machine("num_06_priest_blessing")

# -------------------------- Num.6.22 · TREE_CLAIM --------------------------
# ‹וידבר יהוה … אל› (“and-speak YHWH … to”)
# ‹משה לאמר› (“Moses to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 6:22."
m.step("Num.6.22")

# -------------------------- Num.6.23 · ETNACHTA_SPLIT ----------------------
# ‹דבר אל אהרן› (“speak to Aaron”)
# ‹ואל בניו לאמר› (“and-to son-him/its to-say”)
# ‹כה תברכו את› (“like-this bless obj-marker”)
# ‹בני ישראל … אמור› (“son Israel … say”)
# ‹להם› (“to-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 6:23."
m.step("Num.6.23")
# witness-tier presupposed read:
# the_speech_to_the_priests_the_blessings_form on thus_shall_you_bless —
# read, not installed
m.witness_read("thus_shall_you_bless", "the_speech_to_the_priests_the_blessings_form",
                cites=["Sifrei Bamidbar 39:1", "Onkelos Num 6:23"])

# -------------------------- Num.6.24 · TREE_CLAIM --------------------------
# ‹יברכך יהוה› (“bless-you/your YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms. Num 6:24."
m.step("Num.6.24")
# witness-tier presupposed read: the_blessings_form_counted on
# the_lord_bless_you — read, not installed
m.witness_read("the_lord_bless_you", "the_blessings_form_counted",
                cites=["Onkelos Num 6:24", "Onkelos Num 6:25", "Onkelos Num 6:26"])

# -------------------------- Num.6.25 · TREE_CLAIM --------------------------
# ‹יאר יהוה פניו› (“give-light YHWH face-him/its”)
# ‹אליך› (“to-you/your”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms. Num 6:25."
m.step("Num.6.25")
# witness-tier presupposed read: one_word_two_renderings on
# make_his_face_shine — read, not installed
m.witness_read("make_his_face_shine", "one_word_two_renderings",
                cites=["Onkelos Num 6:25", "Onkelos Num 6:26", "Sifrei Bamidbar 41:1"])

# -------------------------- Num.6.26 · TREE_CLAIM --------------------------
# ‹ישא יהוה פניו› (“lift/carry YHWH face-him/its”)
# ‹אליך … וישם לך› (“to-you/your … and-put/set to-you/your”)
# ‹שלום› (“safe”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 6:26."
m.step("Num.6.26")
# witness-tier presupposed read:
# lifts_his_face_lifts_no_face_the_sealed_decree on lift_his_face — read,
# not installed
m.witness_read("lift_his_face", "lifts_his_face_lifts_no_face_the_sealed_decree",
                cites=["Sifrei Bamidbar 42:1", "Sifrei Bamidbar 42:2", "Onkelos Num 6:26"])

# -------------------------- Num.6.27 · ETNACHTA_SPLIT ----------------------
# ‹ושמו את שמי› (“and-put/set obj-marker name-me/my”)
# ‹על בני ישראל› (“over son Israel”)
# ‹… ואני אברכם› (“and-I bless-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Num 6:27."
m.step("Num.6.27")
# witness-tier presupposed read:
# the_explicit_name_in_the_temple_the_blessing_of_my_name on place_my_name —
# read, not installed
m.witness_read("place_my_name", "the_explicit_name_in_the_temple_the_blessing_of_my_name",
                cites=["Sifrei Bamidbar 43:1", "Onkelos Num 6:27"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('thus_shall_you_bless', 'the_speech_to_the_priests_the_blessings_form'), ('the_lord_bless_you', 'the_blessings_form_counted'), ('make_his_face_shine', 'one_word_two_renderings'), ('lift_his_face', 'lifts_his_face_lifts_no_face_the_sealed_decree'), ('place_my_name', 'the_explicit_name_in_the_temple_the_blessing_of_my_name')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifrei Bamidbar 39:1', 'Onkelos Num 6:23']
    assert all('the_speech_to_the_priests_the_blessings_form' not in f for f in m.WORLD["facts"])
    assert 'thus_shall_you_bless' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Onkelos Num 6:24', 'Onkelos Num 6:25', 'Onkelos Num 6:26']
    assert all('the_blessings_form_counted' not in f for f in m.WORLD["facts"])
    assert 'the_lord_bless_you' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Num 6:25', 'Onkelos Num 6:26', 'Sifrei Bamidbar 41:1']
    assert all('one_word_two_renderings' not in f for f in m.WORLD["facts"])
    assert 'make_his_face_shine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifrei Bamidbar 42:1', 'Sifrei Bamidbar 42:2', 'Onkelos Num 6:26']
    assert all('lifts_his_face_lifts_no_face_the_sealed_decree' not in f for f in m.WORLD["facts"])
    assert 'lift_his_face' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifrei Bamidbar 43:1', 'Onkelos Num 6:27']
    assert all('the_explicit_name_in_the_temple_the_blessing_of_my_name' not in f for f in m.WORLD["facts"])
    assert 'place_my_name' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
