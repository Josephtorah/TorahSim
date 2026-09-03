#!/usr/bin/env python3
# =============================================================================
# lev_01_olah_flock — 1:10-13
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_01_olah_flock.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Olah flock (sheep/goat) procedure (1:10–13)"""
from machine import Machine

m = Machine("lev_01_olah_flock")

# -------------------------- Lev.1.10 · COND_ואם ----------------------------
# ואם מן הצאן קרבנו מן הכשבים או מן העזים לעלה … זכר תמים יקריבנו
# "[EN-AID] From top split: LEFT «ואם מן הצאן קרבנו מן הכשבים או מן העזים
# לעלה» / RIGHT «זכר תמים יקריבנו». Derive claim from Hebrew arms. Lev
# 1:10."
m.step("Lev.1.10")
# witness-tier presupposed read: seam_teaches on flock_filter — read, not
# installed
m.witness_read("flock_filter", "seam_teaches",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 5 2", "Sifra, Vayikra Dibbura DeNedavah, Section 5 1"])

# -------------------------- Lev.1.11 · ETNACHTA_SPLIT ----------------------
# ושחט אתו על ירך המזבח צפנה לפני יהוה … וזרקו בני אהרן הכהנים את דמו על
# המזבח סביב
# "[EN-AID] From top split: LEFT «ושחט אתו על ירך המזבח צפנה לפני יהוה» /
# RIGHT «וזרקו בני אהרן הכהנים את דמו על המזבח סביב». Derive claim from
# Hebrew arms. Lev 1:11."
m.step("Lev.1.11")
# witness-tier presupposed read: environment_dependent on north_rules —
# read, not installed
m.witness_read("north_rules", "environment_dependent",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 4 1", "Sifra, Vayikra Dibbura DeNedavah, Section 5 5", "Sifra, Vayikra Dibbura DeNedavah, Section 5 6", "Sifra, Vayikra Dibbura DeNedavah, Section 5 7", "Sifra, Vayikra Dibbura DeNedavah, Section 5 8", "Sifra, Vayikra Dibbura DeNedavah, Section 5 9", "Sifra, Vayikra Dibbura DeNedavah, Chapter 7 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 7 2"])

# -------------------------- Lev.1.12 · ETNACHTA_SPLIT ----------------------
# ונתח אתו לנתחיו ואת ראשו ואת פדרו … וערך הכהן אתם על העצים אשר על האש אשר
# על המזבח
# "[EN-AID] From top split: LEFT «ונתח אתו לנתחיו ואת ראשו ואת פדרו» / RIGHT
# «וערך הכהן אתם על העצים אשר על האש אשר על המזבח». Derive claim from Hebrew
# arms. Lev 1:12."
m.step("Lev.1.12")
# witness-tier presupposed read: one_priest_two_limbs on arrangement_roster
# — read, not installed
m.witness_read("arrangement_roster", "one_priest_two_limbs",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 6 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 6 2", "Sifra, Vayikra Dibbura DeNedavah, Chapter 6 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 5 7"])

# -------------------------- Lev.1.13 · ETNACHTA_SPLIT ----------------------
# והקרב והכרעים ירחץ במים … והקריב הכהן את הכל והקטיר המזבחה עלה הוא אשה ריח
# ניחח ליהוה
# "[EN-AID] From top split: LEFT «והקרב והכרעים ירחץ במים» / RIGHT «והקריב
# הכהן את הכל והקטיר המזבחה עלה הוא אשה ריח ניחח ליהוה». Derive claim from
# Hebrew arms. Lev 1:13."
m.step("Lev.1.13")
# witness-tier presupposed read: north_gates_rest_advisory on
# criticality_sort — read, not installed
m.witness_read("criticality_sort", "north_gates_rest_advisory",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 7 6", "Sifra, Vayikra Dibbura DeNedavah, Chapter 7 7", "Sifra, Vayikra Dibbura DeNedavah, Section 4 12", "Sifra, Vayikra Dibbura DeNedavah, Chapter 7 5"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('flock_filter', 'seam_teaches'), ('north_rules', 'environment_dependent'), ('arrangement_roster', 'one_priest_two_limbs'), ('criticality_sort', 'north_gates_rest_advisory')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 5 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 1']
    assert all('seam_teaches' not in f for f in m.WORLD["facts"])
    assert 'flock_filter' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 4 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 6', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 8', 'Sifra, Vayikra Dibbura DeNedavah, Section 5 9', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 7 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 7 2']
    assert all('environment_dependent' not in f for f in m.WORLD["facts"])
    assert 'north_rules' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 6 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 6 2', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 6 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 5 7']
    assert all('one_priest_two_limbs' not in f for f in m.WORLD["facts"])
    assert 'arrangement_roster' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 7 6', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 7 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 4 12', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 7 5']
    assert all('north_gates_rest_advisory' not in f for f in m.WORLD["facts"])
    assert 'criticality_sort' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
