#!/usr/bin/env python3
# =============================================================================
# lev_12_childbirth — 12:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_12_childbirth.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Childbirth purity: male/female durations; birds if poor (12:1–8) v1 schedule rewrite"""
from machine import Machine

m = Machine("lev_12_childbirth")

# -------------------------- Lev.12.1 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 12:1."
m.step("Lev.12.1")

# -------------------------- Lev.12.2 · ETNACHTA_SPLIT ----------------------
# דבר אל בני ישראל לאמר אשה כי תזריע וילדה זכר … וטמאה שבעת ימים כימי נדת
# דותה תטמא
# "[EN-AID] From top split: LEFT «דבר אל בני ישראל לאמר אשה כי תזריע וילדה
# זכר» / RIGHT «וטמאה שבעת ימים כימי נדת דותה תטמא». Derive claim from
# Hebrew arms. Lev 12:2."
m.step("Lev.12.2")
# witness-tier presupposed read: last_child_consecutive on shivat_yamim —
# read, not installed
m.witness_read("shivat_yamim", "last_child_consecutive",
                cites=["Sifra, Tazria Parashat Yoledet, Section 1 4", "Sifra, Tazria Parashat Yoledet, Section 1 9", "Sifra, Tazria Parashat Yoledet, Section 1 11", "Sifra, Tazria Parashat Yoledet, Section 1 12", "Sifra, Tazria Parashat Yoledet, Section 1 13", "Sifra, Tazria Parashat Yoledet, Section 1 14"])

# -------------------------- Lev.12.3 · ETNACHTA_SPLIT ----------------------
# וביום השמיני … ימול בשר ערלתו
# "[EN-AID] From top split: LEFT «וביום השמיני» / RIGHT «ימול בשר ערלתו».
# Derive claim from Hebrew arms. Lev 12:3."
m.step("Lev.12.3")
# witness-tier presupposed read: milah_overrides_shabbat on uvayom_hashmini
# — read, not installed
m.witness_read("uvayom_hashmini", "milah_overrides_shabbat",
                cites=["Sifra, Tazria Parashat Yoledet, Chapter 1 1", "Sifra, Tazria Parashat Yoledet, Chapter 1 3", "Sifra, Tazria Parashat Yoledet, Chapter 1 5", "Sifra, Tazria Parashat Yoledet, Chapter 1 6"])

# -------------------------- Lev.12.4 · ETNACHTA_SPLIT ----------------------
# ושלשים יום ושלשת ימים תשב בדמי טהרה … בכל קדש לא תגע ואל המקדש לא תבא עד
# מלאת ימי טהרה
# "[EN-AID] From top split: LEFT «ושלשים יום ושלשת ימים תשב בדמי טהרה» /
# RIGHT «בכל קדש לא תגע ואל המקדש לא תבא עד מלאת ימי טהרה». Derive claim
# from Hebrew arms. Lev 12:4."
m.step("Lev.12.4")
# witness-tier presupposed read: middah_case_law on dayo — read, not
# installed
m.witness_read("dayo", "middah_case_law",
                cites=["Sifra, Tazria Parashat Yoledet, Chapter 2 4", "Sifra, Tazria Parashat Yoledet, Section 1 5"])

# -------------------------- Lev.12.5 · COND_ואם ----------------------------
# ואם נקבה תלד וטמאה שבעים כנדתה … וששים יום וששת ימים תשב על דמי טהרה
# "[EN-AID] From top split: LEFT «ואם נקבה תלד וטמאה שבעים כנדתה» / RIGHT
# «וששים יום וששת ימים תשב על דמי טהרה». Derive claim from Hebrew arms. Lev
# 12:5."
m.step("Lev.12.5")
# witness-tier presupposed read: the_vocalization_seat on shvuayim — read,
# not installed
m.witness_read("shvuayim", "the_vocalization_seat",
                cites=["Sifra, Tazria Parashat Yoledet, Chapter 2 2", "Onkelos Lev 12:5"])

# -------------------------- Lev.12.6 · ETNACHTA_SPLIT ----------------------
# ובמלאת ימי טהרה לבן או לבת תביא כבש בן שנתו לעלה ובן יונה או … אל פתח אהל
# מועד אל הכהן
# "[EN-AID] From top split: LEFT «ובמלאת ימי טהרה לבן או לבת תביא כבש בן
# שנתו לעלה ובן יונה או תר לחטאת» / RIGHT «אל פתח אהל מועד אל הכהן». Derive
# claim from Hebrew arms. Lev 12:6."
m.step("Lev.12.6")

# -------------------------- Lev.12.7 · ETNACHTA_SPLIT ----------------------
# והקריבו לפני יהוה וכפר עליה וטהרה ממקר דמיה … זאת תורת הילדת לזכר או לנקבה
# "[EN-AID] From top split: LEFT «והקריבו לפני יהוה וכפר עליה וטהרה ממקר
# דמיה» / RIGHT «זאת תורת הילדת לזכר או לנקבה». Derive claim from Hebrew
# arms. Lev 12:7."
m.step("Lev.12.7")
# witness-tier presupposed read: five_bloods_and_the_market on mekor_dameha
# — read, not installed
m.witness_read("mekor_dameha", "five_bloods_and_the_market",
                cites=["Sifra, Tazria Parashat Yoledet, Chapter 3 6"])

# -------------------------- Lev.12.8 · COND_ואם ----------------------------
# ואם לא תמצא ידה די שה ולקחה שתי תרים או שני בני יונה אחד לעל … וכפר עליה
# הכהן וטהרה
# "[EN-AID] From top split: LEFT «ואם לא תמצא ידה די שה ולקחה שתי תרים או
# שני בני יונה אחד לעלה ואחד לחטאת» / RIGHT «וכפר עליה הכהן וטהרה». Derive
# claim from Hebrew arms. Lev 12:8."
m.step("Lev.12.8")
# witness-tier presupposed read: order_swap_and_dignity on seder_korban —
# read, not installed
m.witness_read("seder_korban", "order_swap_and_dignity",
                cites=["Sifra, Tazria Parashat Yoledet, Chapter 4 1", "Sifra, Tazria Parashat Yoledet, Chapter 4 2", "Sifra, Tazria Parashat Yoledet, Chapter 4 3", "Sifra, Tazria Parashat Yoledet, Chapter 3 5"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('shivat_yamim', 'last_child_consecutive'), ('uvayom_hashmini', 'milah_overrides_shabbat'), ('dayo', 'middah_case_law'), ('shvuayim', 'the_vocalization_seat'), ('mekor_dameha', 'five_bloods_and_the_market'), ('seder_korban', 'order_swap_and_dignity')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Tazria Parashat Yoledet, Section 1 4', 'Sifra, Tazria Parashat Yoledet, Section 1 9', 'Sifra, Tazria Parashat Yoledet, Section 1 11', 'Sifra, Tazria Parashat Yoledet, Section 1 12', 'Sifra, Tazria Parashat Yoledet, Section 1 13', 'Sifra, Tazria Parashat Yoledet, Section 1 14']
    assert all('last_child_consecutive' not in f for f in m.WORLD["facts"])
    assert 'shivat_yamim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Tazria Parashat Yoledet, Chapter 1 1', 'Sifra, Tazria Parashat Yoledet, Chapter 1 3', 'Sifra, Tazria Parashat Yoledet, Chapter 1 5', 'Sifra, Tazria Parashat Yoledet, Chapter 1 6']
    assert all('milah_overrides_shabbat' not in f for f in m.WORLD["facts"])
    assert 'uvayom_hashmini' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Tazria Parashat Yoledet, Chapter 2 4', 'Sifra, Tazria Parashat Yoledet, Section 1 5']
    assert all('middah_case_law' not in f for f in m.WORLD["facts"])
    assert 'dayo' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Tazria Parashat Yoledet, Chapter 2 2', 'Onkelos Lev 12:5']
    assert all('the_vocalization_seat' not in f for f in m.WORLD["facts"])
    assert 'shvuayim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Tazria Parashat Yoledet, Chapter 3 6']
    assert all('five_bloods_and_the_market' not in f for f in m.WORLD["facts"])
    assert 'mekor_dameha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Tazria Parashat Yoledet, Chapter 4 1', 'Sifra, Tazria Parashat Yoledet, Chapter 4 2', 'Sifra, Tazria Parashat Yoledet, Chapter 4 3', 'Sifra, Tazria Parashat Yoledet, Chapter 3 5']
    assert all('order_swap_and_dignity' not in f for f in m.WORLD["facts"])
    assert 'seder_korban' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
