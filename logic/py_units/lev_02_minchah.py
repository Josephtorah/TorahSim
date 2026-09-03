#!/usr/bin/env python3
# =============================================================================
# lev_02_minchah — 2:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_02_minchah.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Minchah grain offerings: flour, oven, pan, firstfruits (2:1–16)"""
from machine import Machine

m = Machine("lev_02_minchah")

# -------------------------- Lev.2.1 · COND_כי ------------------------------
# ונפש כי תקריב קרבן מנחה ליהוה סלת יהיה קרבנו … ויצק עליה שמן ונתן עליה
# לבנה
# "[EN-AID] From top split: LEFT «ונפש כי תקריב קרבן מנחה ליהוה סלת יהיה
# קרבנו» / RIGHT «ויצק עליה שמן ונתן עליה לבנה». Derive claim from Hebrew
# arms. Lev 2:1."
m.step("Lev.2.1")
# witness-tier presupposed read: menu_closed_at_incense on single_caller —
# read, not installed
m.witness_read("single_caller", "menu_closed_at_incense",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 8 2", "Sifra, Vayikra Dibbura DeNedavah, Section 8 3", "Sifra, Vayikra Dibbura DeNedavah, Section 8 5", "Sifra, Vayikra Dibbura DeNedavah, Section 8 7", "Sifra, Vayikra Dibbura DeNedavah, Section 8 8", "Sifra, Vayikra Dibbura DeNedavah, Section 8 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6"])
# witness-tier presupposed read: placement_follows_sample on two_adjuncts —
# read, not installed
m.witness_read("two_adjuncts", "placement_follows_sample",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 8", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 9", "Sifra, Vayikra Dibbura DeNedavah, Chapter 10 10", "Sifra, Vayikra Dibbura DeNedavah, Section 9 2"])

# -------------------------- Lev.2.2 · ETNACHTA_SPLIT -----------------------
# והביאה אל בני אהרן הכהנים וקמץ משם מלא קמצו מסלתה ומשמנה על  … והקטיר הכהן
# את אזכרתה המזבחה אשה ריח ניחח ליהוה
# "[EN-AID] From top split: LEFT «והביאה אל בני אהרן הכהנים וקמץ משם מלא
# קמצו מסלתה ומשמנה על כל לבנתה» / RIGHT «והקטיר הכהן את אזכרתה המזבחה אשה
# ריח ניחח ליהוה». Derive claim from Hebrew arms. Lev 2:2."
m.step("Lev.2.2")
# witness-tier presupposed read: constant_scaling_level_measure on fistful —
# read, not installed
m.witness_read("fistful", "constant_scaling_level_measure",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 9 3", "Sifra, Vayikra Dibbura DeNedavah, Section 9 5", "Sifra, Vayikra Dibbura DeNedavah, Section 9 6", "Sifra, Vayikra Dibbura DeNedavah, Section 9 7", "Sifra, Vayikra Dibbura DeNedavah, Section 9 9", "Sifra, Vayikra Dibbura DeNedavah, Section 9 10"])
# witness-tier presupposed read: tenth_and_log_full on quantity_floors —
# read, not installed
m.witness_read("quantity_floors", "tenth_and_log_full",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 9 8", "Sifra, Vayikra Dibbura DeNedavah, Section 9 11", "Sifra, Vayikra Dibbura DeNedavah, Section 9 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 11 1"])

# -------------------------- Lev.2.3 · ETNACHTA_SPLIT -----------------------
# והנותרת מן המנחה לאהרן ולבניו … קדש קדשים מאשי יהוה
# "[EN-AID] From top split: LEFT «והנותרת מן המנחה לאהרן ולבניו» / RIGHT
# «קדש קדשים מאשי יהוה». Derive claim from Hebrew arms. Lev 2:3."
m.step("Lev.2.3")

# -------------------------- Lev.2.4 · COND_וכי -----------------------------
# וכי תקרב קרבן מנחה מאפה תנור … סלת חלות מצת בלולת בשמן ורקיקי מצות משחים
# בשמן
# "[EN-AID] From top split: LEFT «וכי תקרב קרבן מנחה מאפה תנור» / RIGHT «סלת
# חלות מצת בלולת בשמן ורקיקי מצות משחים בשמן». Derive claim from Hebrew
# arms. Lev 2:4."
m.step("Lev.2.4")
# witness-tier presupposed read: normalize_or_void on vow_parser — read, not
# installed
m.witness_read("vow_parser", "normalize_or_void",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 10 2", "Sifra, Vayikra Dibbura DeNedavah, Section 10 1", "Sifra, Vayikra Dibbura DeNedavah, Section 10 2", "Sifra, Vayikra Dibbura DeNedavah, Section 10 3"])

# -------------------------- Lev.2.5 · COND_ואם -----------------------------
# ואם מנחה על המחבת קרבנך … סלת בלולה בשמן מצה תהיה
# "[EN-AID] From top split: LEFT «ואם מנחה על המחבת קרבנך» / RIGHT «סלת
# בלולה בשמן מצה תהיה». Derive claim from Hebrew arms. Lev 2:5."
m.step("Lev.2.5")

# -------------------------- Lev.2.6 · ETNACHTA_SPLIT -----------------------
# פתות אתה פתים ויצקת עליה שמן … מנחה הוא
# "[EN-AID] From top split: LEFT «פתות אתה פתים ויצקת עליה שמן» / RIGHT
# «מנחה הוא». Derive claim from Hebrew arms. Lev 2:6."
m.step("Lev.2.6")
# witness-tier presupposed read: three_by_caller_class on folding_paths —
# read, not installed
m.witness_read("folding_paths", "three_by_caller_class",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 12 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 5", "Sifra, Vayikra Dibbura DeNedavah, Chapter 12 7"])

# -------------------------- Lev.2.7 · COND_ואם -----------------------------
# ואם מנחת מרחשת קרבנך … סלת בשמן תעשה
# "[EN-AID] From top split: LEFT «ואם מנחת מרחשת קרבנך» / RIGHT «סלת בשמן
# תעשה». Derive claim from Hebrew arms. Lev 2:7."
m.step("Lev.2.7")

# -------------------------- Lev.2.8 · ETNACHTA_SPLIT -----------------------
# והבאת את המנחה אשר יעשה מאלה ליהוה … והקריבה אל הכהן והגישה אל המזבח
# "[EN-AID] From top split: LEFT «והבאת את המנחה אשר יעשה מאלה ליהוה» /
# RIGHT «והקריבה אל הכהן והגישה אל המזבח». Derive claim from Hebrew arms.
# Lev 2:8."
m.step("Lev.2.8")

# -------------------------- Lev.2.9 · ETNACHTA_SPLIT -----------------------
# והרים הכהן מן המנחה את אזכרתה והקטיר המזבחה … אשה ריח ניחח ליהוה
# "[EN-AID] From top split: LEFT «והרים הכהן מן המנחה את אזכרתה והקטיר
# המזבחה» / RIGHT «אשה ריח ניחח ליהוה». Derive claim from Hebrew arms. Lev
# 2:9."
m.step("Lev.2.9")

# -------------------------- Lev.2.10 · ETNACHTA_SPLIT ----------------------
# והנותרת מן המנחה לאהרן ולבניו … קדש קדשים מאשי יהוה
# "[EN-AID] From top split: LEFT «והנותרת מן המנחה לאהרן ולבניו» / RIGHT
# «קדש קדשים מאשי יהוה». Derive claim from Hebrew arms. Lev 2:10."
m.step("Lev.2.10")

# -------------------------- Lev.2.11 · ETNACHTA_SPLIT ----------------------
# כל המנחה אשר תקריבו ליהוה לא תעשה חמץ … כי כל שאר וכל דבש לא תקטירו ממנו
# אשה ליהוה
# "[EN-AID] From top split: LEFT «כל המנחה אשר תקריבו ליהוה לא תעשה חמץ» /
# RIGHT «כי כל שאר וכל דבש לא תקטירו ממנו אשה ליהוה». Derive claim from
# Hebrew arms. Lev 2:11."
m.step("Lev.2.11")
# witness-tier presupposed read: per_step_liability on leaven_ban — read,
# not installed
m.witness_read("leaven_ban", "per_step_liability",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 12 1", "Sifra, Vayikra Dibbura DeNedavah, Section 12 3", "Sifra, Vayikra Dibbura DeNedavah, Section 12 4", "Sifra, Vayikra Dibbura DeNedavah, Section 12 5", "Sifra, Vayikra Dibbura DeNedavah, Section 12 6"])

# -------------------------- Lev.2.12 · ETNACHTA_SPLIT ----------------------
# קרבן ראשית תקריבו אתם ליהוה … ואל המזבח לא יעלו לריח ניחח
# "[EN-AID] From top split: LEFT «קרבן ראשית תקריבו אתם ליהוה» / RIGHT «ואל
# המזבח לא יעלו לריח ניחח». Derive claim from Hebrew arms. Lev 2:12."
m.step("Lev.2.12")

# -------------------------- Lev.2.13 · ETNACHTA_SPLIT ----------------------
# וכל קרבן מנחתך במלח תמלח ולא תשבית מלח ברית אלהיך מעל מנחתך … על כל קרבנך
# תקריב מלח
# "[EN-AID] From top split: LEFT «וכל קרבן מנחתך במלח תמלח ולא תשבית מלח
# ברית אלהיך מעל מנחתך» / RIGHT «על כל קרבנך תקריב מלח». Derive claim from
# Hebrew arms. Lev 2:13."
m.step("Lev.2.13")
# witness-tier presupposed read: overrides_schedulers on salt_covenant —
# read, not installed
m.witness_read("salt_covenant", "overrides_schedulers",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 14 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 14 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 14 7", "Onkelos Lev 2:13"])

# -------------------------- Lev.2.14 · COND_ואם ----------------------------
# ואם תקריב מנחת בכורים ליהוה … אביב קלוי באש גרש כרמל תקריב את מנחת בכוריך
# "[EN-AID] From top split: LEFT «ואם תקריב מנחת בכורים ליהוה» / RIGHT «אביב
# קלוי באש גרש כרמל תקריב את מנחת בכוריך». Derive claim from Hebrew arms.
# Lev 2:14."
m.step("Lev.2.14")
# witness-tier presupposed read: barley_word_order_if_grading on omer —
# read, not installed
m.witness_read("omer", "barley_word_order_if_grading",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Section 13 4", "Sifra, Vayikra Dibbura DeNedavah, Section 13 7", "Sifra, Vayikra Dibbura DeNedavah, Section 13 3", "Sifra, Vayikra Dibbura DeNedavah, Section 13 2", "Sifra, Vayikra Dibbura DeNedavah, Section 13 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 1", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 2", "Onkelos Lev 2:14"])

# -------------------------- Lev.2.15 · ETNACHTA_SPLIT ----------------------
# ונתת עליה שמן ושמת עליה לבנה … מנחה הוא
# "[EN-AID] From top split: LEFT «ונתת עליה שמן ושמת עליה לבנה» / RIGHT
# «מנחה הוא». Derive claim from Hebrew arms. Lev 2:15."
m.step("Lev.2.15")
# witness-tier presupposed read: closed_member_by_member on adjunct_matrix —
# read, not installed
m.witness_read("adjunct_matrix", "closed_member_by_member",
                cites=["Sifra, Vayikra Dibbura DeNedavah, Chapter 15 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 15 5", "Sifra, Vayikra Dibbura DeNedavah, Section 12 7", "Sifra, Vayikra Dibbura DeNedavah, Section 12 9"])

# -------------------------- Lev.2.16 · ETNACHTA_SPLIT ----------------------
# והקטיר הכהן את אזכרתה מגרשה ומשמנה על כל לבנתה … אשה ליהוה
# "[EN-AID] From top split: LEFT «והקטיר הכהן את אזכרתה מגרשה ומשמנה על כל
# לבנתה» / RIGHT «אשה ליהוה». Derive claim from Hebrew arms. Lev 2:16."
m.step("Lev.2.16")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('single_caller', 'menu_closed_at_incense'), ('two_adjuncts', 'placement_follows_sample'), ('fistful', 'constant_scaling_level_measure'), ('quantity_floors', 'tenth_and_log_full'), ('vow_parser', 'normalize_or_void'), ('folding_paths', 'three_by_caller_class'), ('leaven_ban', 'per_step_liability'), ('salt_covenant', 'overrides_schedulers'), ('omer', 'barley_word_order_if_grading'), ('adjunct_matrix', 'closed_member_by_member')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 8 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 8', 'Sifra, Vayikra Dibbura DeNedavah, Section 8 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 6']
    assert all('menu_closed_at_incense' not in f for f in m.WORLD["facts"])
    assert 'single_caller' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 10 7', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 8', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 9', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 10 10', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 2']
    assert all('placement_follows_sample' not in f for f in m.WORLD["facts"])
    assert 'two_adjuncts' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 9 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 6', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 9', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 10']
    assert all('constant_scaling_level_measure' not in f for f in m.WORLD["facts"])
    assert 'fistful' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 9 8', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 11', 'Sifra, Vayikra Dibbura DeNedavah, Section 9 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 11 1']
    assert all('tenth_and_log_full' not in f for f in m.WORLD["facts"])
    assert 'quantity_floors' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 10 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 10 3']
    assert all('normalize_or_void' not in f for f in m.WORLD["facts"])
    assert 'vow_parser' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 12 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 5', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 12 7']
    assert all('three_by_caller_class' not in f for f in m.WORLD["facts"])
    assert 'folding_paths' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 12 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 6']
    assert all('per_step_liability' not in f for f in m.WORLD["facts"])
    assert 'leaven_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 14 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 14 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 14 7', 'Onkelos Lev 2:13']
    assert all('overrides_schedulers' not in f for f in m.WORLD["facts"])
    assert 'salt_covenant' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Section 13 4', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 3', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 2', 'Sifra, Vayikra Dibbura DeNedavah, Section 13 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 1', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 2', 'Onkelos Lev 2:14']
    assert all('barley_word_order_if_grading' not in f for f in m.WORLD["facts"])
    assert 'omer' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Vayikra Dibbura DeNedavah, Chapter 15 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 15 5', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 7', 'Sifra, Vayikra Dibbura DeNedavah, Section 12 9']
    assert all('closed_member_by_member' not in f for f in m.WORLD["facts"])
    assert 'adjunct_matrix' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
