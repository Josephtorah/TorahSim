#!/usr/bin/env python3
# =============================================================================
# lev_07_fat_blood_dues — 7:22-38
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_07_fat_blood_dues.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Fat/blood ban detail; priest breast/thigh; summary of korban torot (7:22–38)"""
from machine import Machine

m = Machine("lev_07_fat_blood_dues")

# -------------------------- Lev.7.22 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 7:22."
m.step("Lev.7.22")

# -------------------------- Lev.7.23 · ETNACHTA_SPLIT ----------------------
# דבר אל בני ישראל לאמר … כל חלב שור וכשב ועז לא תאכלו
# "[EN-AID] From top split: LEFT «דבר אל בני ישראל לאמר» / RIGHT «כל חלב שור
# וכשב ועז לא תאכלו». Derive claim from Hebrew arms. Lev 7:23."
m.step("Lev.7.23")
# witness-tier presupposed read: israel_scope on cheilev_ban — read, not
# installed
m.witness_read("cheilev_ban", "israel_scope",
                cites=["Sifra, Tzav, Section 10 1", "Sifra, Tzav, Section 10 2", "Sifra, Tzav, Section 10 4"])

# -------------------------- Lev.7.24 · ETNACHTA_SPLIT ----------------------
# וחלב נבלה וחלב טרפה יעשה לכל מלאכה … ואכל לא תאכלהו
# "[EN-AID] From top split: LEFT «וחלב נבלה וחלב טרפה יעשה לכל מלאכה» /
# RIGHT «ואכל לא תאכלהו». Derive claim from Hebrew arms. Lev 7:24."
m.step("Lev.7.24")
# witness-tier presupposed read: inversion on carrion_fat — read, not
# installed
m.witness_read("carrion_fat", "inversion",
                cites=["Sifra, Tzav, Section 10 5", "Sifra, Tzav, Section 10 6", "Sifra, Tzav, Section 10 7", "Sifra, Tzav, Section 10 8"])

# -------------------------- Lev.7.25 · COND_כי -----------------------------
# כי כל אכל חלב מן הבהמה אשר יקריב ממנה אשה ליהוה … ונכרתה הנפש האכלת מעמיה
# "[EN-AID] From top split: LEFT «כי כל אכל חלב מן הבהמה אשר יקריב ממנה אשה
# ליהוה» / RIGHT «ונכרתה הנפש האכלת מעמיה». Derive claim from Hebrew arms.
# Lev 7:25."
m.step("Lev.7.25")
# witness-tier presupposed read: sacrificial_type on cheilev_karet — read,
# not installed
m.witness_read("cheilev_karet", "sacrificial_type",
                cites=["Sifra, Tzav, Section 10 9", "Sifra, Tzav, Section 10 10"])

# -------------------------- Lev.7.26 · ETNACHTA_SPLIT ----------------------
# וכל דם לא תאכלו בכל מושבתיכם … לעוף ולבהמה
# "[EN-AID] From top split: LEFT «וכל דם לא תאכלו בכל מושבתיכם» / RIGHT
# «לעוף ולבהמה». Derive claim from Hebrew arms. Lev 7:26."
m.step("Lev.7.26")
# witness-tier presupposed read: species_criteria on blood_ban — read, not
# installed
m.witness_read("blood_ban", "species_criteria",
                cites=["Sifra, Tzav, Section 10 11"])

# -------------------------- Lev.7.27 · ETNACHTA_SPLIT ----------------------
# כל נפש אשר תאכל כל דם … ונכרתה הנפש ההוא מעמיה
# "[EN-AID] From top split: LEFT «כל נפש אשר תאכל כל דם» / RIGHT «ונכרתה
# הנפש ההוא מעמיה». Derive claim from Hebrew arms. Lev 7:27."
m.step("Lev.7.27")

# -------------------------- Lev.7.28 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 7:28."
m.step("Lev.7.28")

# -------------------------- Lev.7.29 · ETNACHTA_SPLIT ----------------------
# דבר אל בני ישראל לאמר … המקריב את זבח שלמיו ליהוה יביא את קרבנו ליהוה מזבח
# שלמיו
# "[EN-AID] From top split: LEFT «דבר אל בני ישראל לאמר» / RIGHT «המקריב את
# זבח שלמיו ליהוה יביא את קרבנו ליהוה מזבח שלמיו». Derive claim from Hebrew
# arms. Lev 7:29."
m.step("Lev.7.29")

# -------------------------- Lev.7.30 · ETNACHTA_SPLIT ----------------------
# ידיו תביאינה את אשי יהוה … את החלב על החזה יביאנו את החזה להניף אתו תנופה
# לפני יהוה
# "[EN-AID] From top split: LEFT «ידיו תביאינה את אשי יהוה» / RIGHT «את החלב
# על החזה יביאנו את החזה להניף אתו תנופה לפני יהוה». Derive claim from
# Hebrew arms. Lev 7:30."
m.step("Lev.7.30")
# witness-tier presupposed read: stacked_hands on tenufah_engine — read, not
# installed
m.witness_read("tenufah_engine", "stacked_hands",
                cites=["Sifra, Tzav, Section 11 1", "Sifra, Tzav, Section 11 2", "Sifra, Tzav, Section 11 3", "Sifra, Tzav, Section 11 6", "Sifra, Tzav, Section 11 9", "Sifra, Tzav, Section 11 10", "Sifra, Tzav, Section 11 11", "Sifra, Tzav, Chapter 16 2", "Sifra, Tzav, Chapter 16 3", "Onkelos Lev 7:30"])

# -------------------------- Lev.7.31 · ETNACHTA_SPLIT ----------------------
# והקטיר הכהן את החלב המזבחה … והיה החזה לאהרן ולבניו
# "[EN-AID] From top split: LEFT «והקטיר הכהן את החלב המזבחה» / RIGHT «והיה
# החזה לאהרן ולבניו». Derive claim from Hebrew arms. Lev 7:31."
m.step("Lev.7.31")

# -------------------------- Lev.7.32 · ETNACHTA_SPLIT ----------------------
# ואת שוק הימין תתנו תרומה לכהן … מזבחי שלמיכם
# "[EN-AID] From top split: LEFT «ואת שוק הימין תתנו תרומה לכהן» / RIGHT
# «מזבחי שלמיכם». Derive claim from Hebrew arms. Lev 7:32."
m.step("Lev.7.32")

# -------------------------- Lev.7.33 · ETNACHTA_SPLIT ----------------------
# המקריב את דם השלמים ואת החלב מבני אהרן … לו תהיה שוק הימין למנה
# "[EN-AID] From top split: LEFT «המקריב את דם השלמים ואת החלב מבני אהרן» /
# RIGHT «לו תהיה שוק הימין למנה». Derive claim from Hebrew arms. Lev 7:33."
m.step("Lev.7.33")
# witness-tier presupposed read: consent_and_acknowledgment on dues_gates —
# read, not installed
m.witness_read("dues_gates", "consent_and_acknowledgment",
                cites=["Sifra, Tzav, Chapter 16 4", "Sifra, Tzav, Chapter 16 5", "Sifra, Tzav, Chapter 16 7", "Sifra, Tzav, Chapter 16 8", "Sifra, Tzav, Chapter 16 9", "Sifra, Tzav, Chapter 17 5", "Sifra, Tzav, Chapter 17 6"])

# -------------------------- Lev.7.34 · COND_כי -----------------------------
# כי את חזה התנופה ואת שוק התרומה לקחתי מאת בני ישראל מזבחי של … ואתן אתם
# לאהרן הכהן ולבניו לחק עולם מאת בני ישראל
# "[EN-AID] From top split: LEFT «כי את חזה התנופה ואת שוק התרומה לקחתי מאת
# בני ישראל מזבחי שלמיהם» / RIGHT «ואתן אתם לאהרן הכהן ולבניו לחק עולם מאת
# בני ישראל». Derive claim from Hebrew arms. Lev 7:34."
m.step("Lev.7.34")

# -------------------------- Lev.7.35 · ETNACHTA_SPLIT ----------------------
# זאת משחת אהרן ומשחת בניו מאשי יהוה … ביום הקריב אתם לכהן ליהוה
# "[EN-AID] From top split: LEFT «זאת משחת אהרן ומשחת בניו מאשי יהוה» /
# RIGHT «ביום הקריב אתם לכהן ליהוה». Derive claim from Hebrew arms. Lev
# 7:35."
m.step("Lev.7.35")

# -------------------------- Lev.7.36 · ETNACHTA_SPLIT ----------------------
# אשר צוה יהוה לתת להם ביום משחו אתם מאת בני ישראל … חקת עולם לדרתם
# "[EN-AID] From top split: LEFT «אשר צוה יהוה לתת להם ביום משחו אתם מאת בני
# ישראל» / RIGHT «חקת עולם לדרתם». Derive claim from Hebrew arms. Lev 7:36."
m.step("Lev.7.36")

# -------------------------- Lev.7.37 · ETNACHTA_SPLIT ----------------------
# זאת התורה לעלה למנחה ולחטאת ולאשם … ולמלואים ולזבח השלמים
# "[EN-AID] From top split: LEFT «זאת התורה לעלה למנחה ולחטאת ולאשם» / RIGHT
# «ולמלואים ולזבח השלמים». Derive claim from Hebrew arms. Lev 7:37."
m.step("Lev.7.37")
# witness-tier presupposed read: two_channel_charter on sinai_colophon —
# read, not installed
m.witness_read("sinai_colophon", "two_channel_charter",
                cites=["Sifra, Tzav, Chapter 18 2", "Sifra, Tzav, Chapter 18 3", "Sifra, Tzav, Chapter 18 4", "Sifra, Tzav, Chapter 18 6", "Sifra, Tzav, Chapter 18 7", "Sifra, Tzav, Chapter 18 8", "Sifra, Tzav, Chapter 18 10", "Onkelos Lev 7:35"])

# -------------------------- Lev.7.38 · ETNACHTA_SPLIT ----------------------
# אשר צוה יהוה את משה בהר סיני … ביום צותו את בני ישראל להקריב את קרבניהם
# ליהוה במדבר סיני
# "[EN-AID] From top split: LEFT «אשר צוה יהוה את משה בהר סיני» / RIGHT
# «ביום צותו את בני ישראל להקריב את קרבניהם ליהוה במדבר סיני». Derive claim
# from Hebrew arms. Lev 7:38."
m.step("Lev.7.38")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('cheilev_ban', 'israel_scope'), ('carrion_fat', 'inversion'), ('cheilev_karet', 'sacrificial_type'), ('blood_ban', 'species_criteria'), ('tenufah_engine', 'stacked_hands'), ('dues_gates', 'consent_and_acknowledgment'), ('sinai_colophon', 'two_channel_charter')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Tzav, Section 10 1', 'Sifra, Tzav, Section 10 2', 'Sifra, Tzav, Section 10 4']
    assert all('israel_scope' not in f for f in m.WORLD["facts"])
    assert 'cheilev_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Tzav, Section 10 5', 'Sifra, Tzav, Section 10 6', 'Sifra, Tzav, Section 10 7', 'Sifra, Tzav, Section 10 8']
    assert all('inversion' not in f for f in m.WORLD["facts"])
    assert 'carrion_fat' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Tzav, Section 10 9', 'Sifra, Tzav, Section 10 10']
    assert all('sacrificial_type' not in f for f in m.WORLD["facts"])
    assert 'cheilev_karet' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Tzav, Section 10 11']
    assert all('species_criteria' not in f for f in m.WORLD["facts"])
    assert 'blood_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Tzav, Section 11 1', 'Sifra, Tzav, Section 11 2', 'Sifra, Tzav, Section 11 3', 'Sifra, Tzav, Section 11 6', 'Sifra, Tzav, Section 11 9', 'Sifra, Tzav, Section 11 10', 'Sifra, Tzav, Section 11 11', 'Sifra, Tzav, Chapter 16 2', 'Sifra, Tzav, Chapter 16 3', 'Onkelos Lev 7:30']
    assert all('stacked_hands' not in f for f in m.WORLD["facts"])
    assert 'tenufah_engine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Tzav, Chapter 16 4', 'Sifra, Tzav, Chapter 16 5', 'Sifra, Tzav, Chapter 16 7', 'Sifra, Tzav, Chapter 16 8', 'Sifra, Tzav, Chapter 16 9', 'Sifra, Tzav, Chapter 17 5', 'Sifra, Tzav, Chapter 17 6']
    assert all('consent_and_acknowledgment' not in f for f in m.WORLD["facts"])
    assert 'dues_gates' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Tzav, Chapter 18 2', 'Sifra, Tzav, Chapter 18 3', 'Sifra, Tzav, Chapter 18 4', 'Sifra, Tzav, Chapter 18 6', 'Sifra, Tzav, Chapter 18 7', 'Sifra, Tzav, Chapter 18 8', 'Sifra, Tzav, Chapter 18 10', 'Onkelos Lev 7:35']
    assert all('two_channel_charter' not in f for f in m.WORLD["facts"])
    assert 'sinai_colophon' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
