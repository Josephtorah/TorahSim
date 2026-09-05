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
# ‹וידבר יהוה … אל› (“and-speak YHWH … to”)
# ‹משה לאמר› (“Moses to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:22."
m.step("Lev.7.22")

# -------------------------- Lev.7.23 · ETNACHTA_SPLIT ----------------------
# ‹דבר אל בני› (“speak to son”)
# ‹ישראל לאמר … כל› (“Israel to-say … all”)
# ‹חלב שור וכשב› (“fat bullock and-young-sheep”)
# ‹ועז לא תאכלו› (“and-she-goat not eat”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:23."
m.step("Lev.7.23")
# witness-tier presupposed read: israel_scope on cheilev_ban — read, not
# installed
m.witness_read("cheilev_ban", "israel_scope",
                cites=["Sifra, Tzav, Section 10 1", "Sifra, Tzav, Section 10 2", "Sifra, Tzav, Section 10 4"])

# -------------------------- Lev.7.24 · ETNACHTA_SPLIT ----------------------
# ‹וחלב נבלה וחלב› (“and-fat flabby-thing and-fat”)
# ‹טרפה יעשה לכל› (“prey make to-all”)
# ‹מלאכה … ואכל לא› (“work … and-eat not”)
# ‹תאכלהו› (“eat-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:24."
m.step("Lev.7.24")
# witness-tier presupposed read: inversion on carrion_fat — read, not
# installed
m.witness_read("carrion_fat", "inversion",
                cites=["Sifra, Tzav, Section 10 5", "Sifra, Tzav, Section 10 6", "Sifra, Tzav, Section 10 7", "Sifra, Tzav, Section 10 8"])

# -------------------------- Lev.7.25 · COND_כי (“that”) --------------------
# ‹כי כל אכל› (“that all eat”)
# ‹חלב מן הבהמה› (“fat from the-livestock”)
# ‹אשר יקריב ממנה› (“which bring-near from-her/its”)
# ‹אשה ליהוה … ונכרתה› (“fire-offering to-YHWH … and-cut”)
# ‹הנפש האכלת מעמיה› (“the-living-being the-eat from-people-her/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:25."
m.step("Lev.7.25")
# witness-tier presupposed read: sacrificial_type on cheilev_karet — read,
# not installed
m.witness_read("cheilev_karet", "sacrificial_type",
                cites=["Sifra, Tzav, Section 10 9", "Sifra, Tzav, Section 10 10"])

# -------------------------- Lev.7.26 · ETNACHTA_SPLIT ----------------------
# ‹וכל דם לא› (“and-all blood not”)
# ‹תאכלו בכל מושבתיכם› (“eat in-all seat-you/your(pl)”)
# ‹… לעוף ולבהמה› (“to-flying-creature and-to-livestock”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:26."
m.step("Lev.7.26")
# witness-tier presupposed read: species_criteria on blood_ban — read, not
# installed
m.witness_read("blood_ban", "species_criteria",
                cites=["Sifra, Tzav, Section 10 11"])

# -------------------------- Lev.7.27 · ETNACHTA_SPLIT ----------------------
# ‹כל נפש אשר› (“all living-being which”)
# ‹תאכל כל דם› (“eat all blood”)
# ‹… ונכרתה הנפש ההוא› (“and-cut the-living-being that”)
# ‹מעמיה› (“from-people-her/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:27."
m.step("Lev.7.27")

# -------------------------- Lev.7.28 · TREE_CLAIM --------------------------
# ‹וידבר יהוה … אל› (“and-speak YHWH … to”)
# ‹משה לאמר› (“Moses to-say”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:28."
m.step("Lev.7.28")

# -------------------------- Lev.7.29 · ETNACHTA_SPLIT ----------------------
# ‹דבר אל בני› (“speak to son”)
# ‹ישראל לאמר … המקריב› (“Israel to-say … the-bring-near”)
# ‹את זבח שלמיו› (“obj-marker sacrifice requital-him/its”)
# ‹ליהוה יביא את› (“to-YHWH come/bring obj-marker”)
# ‹קרבנו ליהוה מזבח› (“offering-him/its to-YHWH from-sacrifice”)
# ‹שלמיו› (“requital-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:29."
m.step("Lev.7.29")

# -------------------------- Lev.7.30 · ETNACHTA_SPLIT ----------------------
# ‹ידיו תביאינה את› (“hand-him/its come/bring obj-marker”)
# ‹אשי יהוה … את› (“fire-offering YHWH … obj-marker”)
# ‹החלב על החזה› (“the-fat over the-breast”)
# ‹יביאנו את החזה› (“come/bring-him/its obj-marker the-breast”)
# ‹להניף אתו תנופה› (“to-quiver obj-marker-him/its brandishing”)
# ‹לפני יהוה› (“to-face YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:30."
m.step("Lev.7.30")
# witness-tier presupposed read: stacked_hands on tenufah_engine — read, not
# installed
m.witness_read("tenufah_engine", "stacked_hands",
                cites=["Sifra, Tzav, Section 11 1", "Sifra, Tzav, Section 11 2", "Sifra, Tzav, Section 11 3", "Sifra, Tzav, Section 11 6", "Sifra, Tzav, Section 11 9", "Sifra, Tzav, Section 11 10", "Sifra, Tzav, Section 11 11", "Sifra, Tzav, Chapter 16 2", "Sifra, Tzav, Chapter 16 3", "Onkelos Lev 7:30"])

# -------------------------- Lev.7.31 · ETNACHTA_SPLIT ----------------------
# ‹והקטיר הכהן את› (“and-smoke the-priest obj-marker”)
# ‹החלב המזבחה … והיה› (“the-fat the-altar-ward … and-be”)
# ‹החזה לאהרן ולבניו› (“the-breast to-Aaron and-to-son-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:31."
m.step("Lev.7.31")

# -------------------------- Lev.7.32 · ETNACHTA_SPLIT ----------------------
# ‹ואת שוק הימין› (“and-obj-marker leg the-right-hand”)
# ‹תתנו תרומה לכהן› (“set present to-priest”)
# ‹… מזבחי שלמיכם› (“from-sacrifice requital-you/your(pl)”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:32."
m.step("Lev.7.32")

# -------------------------- Lev.7.33 · ETNACHTA_SPLIT ----------------------
# ‹המקריב את דם› (“the-bring-near obj-marker blood”)
# ‹השלמים ואת החלב› (“the-requital and-obj-marker the-fat”)
# ‹מבני אהרן … לו› (“from-son Aaron … to-him/its”)
# ‹תהיה שוק הימין› (“be leg the-right-hand”)
# ‹למנה› (“to-something-weighed-out”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:33."
m.step("Lev.7.33")
# witness-tier presupposed read: consent_and_acknowledgment on dues_gates —
# read, not installed
m.witness_read("dues_gates", "consent_and_acknowledgment",
                cites=["Sifra, Tzav, Chapter 16 4", "Sifra, Tzav, Chapter 16 5", "Sifra, Tzav, Chapter 16 7", "Sifra, Tzav, Chapter 16 8", "Sifra, Tzav, Chapter 16 9", "Sifra, Tzav, Chapter 17 5", "Sifra, Tzav, Chapter 17 6"])

# -------------------------- Lev.7.34 · COND_כי (“that”) --------------------
# ‹כי את חזה› (“that obj-marker breast”)
# ‹התנופה ואת שוק› (“the-brandishing and-obj-marker leg”)
# ‹התרומה לקחתי מאת› (“the-present take from-with”)
# ‹בני ישראל מזבחי› (“son Israel from-sacrifice”)
# ‹של … ואתן אתם› (“pluck-off … and-set obj-marker-them/their”)
# ‹לאהרן הכהן ולבניו› (“to-Aaron the-priest and-to-son-him/its”)
# ‹לחק עולם מאת› (“to-enactment forever from-with”)
# ‹בני ישראל› (“son Israel”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:34."
m.step("Lev.7.34")

# -------------------------- Lev.7.35 · ETNACHTA_SPLIT ----------------------
# ‹זאת משחת אהרן› (“this unction Aaron”)
# ‹ומשחת בניו מאשי› (“and-unction son-him/its from-fire-offering”)
# ‹יהוה … ביום הקריב› (“YHWH … in-day bring-near”)
# ‹אתם לכהן ליהוה› (“obj-marker-them/their to-officiate-as-a-priest to-
# YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:35."
m.step("Lev.7.35")

# -------------------------- Lev.7.36 · ETNACHTA_SPLIT ----------------------
# ‹אשר צוה יהוה› (“which command YHWH”)
# ‹לתת להם ביום› (“to-set to-them/their in-day”)
# ‹משחו אתם מאת› (“rub-with-oil-him/its obj-marker-them/their from-with”)
# ‹בני ישראל … חקת› (“son Israel … statute”)
# ‹עולם לדרתם› (“forever to-generation-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:36."
m.step("Lev.7.36")

# -------------------------- Lev.7.37 · ETNACHTA_SPLIT ----------------------
# ‹זאת התורה לעלה› (“this the-precept to-burnt-offering”)
# ‹למנחה ולחטאת ולאשם› (“to-grain-offering and-to-sin-offering and-to-
# guilt”)
# ‹… ולמלואים ולזבח השלמים› (“and-to-fulfilling and-to-sacrifice the-
# requital”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:37."
m.step("Lev.7.37")
# witness-tier presupposed read: two_channel_charter on sinai_colophon —
# read, not installed
m.witness_read("sinai_colophon", "two_channel_charter",
                cites=["Sifra, Tzav, Chapter 18 2", "Sifra, Tzav, Chapter 18 3", "Sifra, Tzav, Chapter 18 4", "Sifra, Tzav, Chapter 18 6", "Sifra, Tzav, Chapter 18 7", "Sifra, Tzav, Chapter 18 8", "Sifra, Tzav, Chapter 18 10", "Onkelos Lev 7:35"])

# -------------------------- Lev.7.38 · ETNACHTA_SPLIT ----------------------
# ‹אשר צוה יהוה› (“which command YHWH”)
# ‹את משה בהר› (“obj-marker Moses in-mountain”)
# ‹סיני … ביום צותו› (“Sinai … in-day command-him/its”)
# ‹את בני ישראל› (“obj-marker son Israel”)
# ‹להקריב את קרבניהם› (“to-bring-near obj-marker offering-them/their”)
# ‹ליהוה במדבר סיני› (“to-YHWH in-pasture Sinai”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms. Lev 7:38."
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
