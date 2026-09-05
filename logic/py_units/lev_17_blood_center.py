#!/usr/bin/env python3
# =============================================================================
# lev_17_blood_center — 17:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_17_blood_center.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Slaughter at Tent; blood is life; no eating blood/neveilah (17:1–16)"""
from machine import Machine

m = Machine("lev_17_blood_center")

# -------------------------- Lev.17.1 · TREE_CLAIM --------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms. Lev 17:1."
m.step("Lev.17.1")

# -------------------------- Lev.17.2 · ETNACHTA_SPLIT ----------------------
# דבר אל אהרן ואל בניו ואל כל בני ישראל ואמרת אליהם … זה הדבר אשר צוה יהוה
# לאמר
# "[EN-AID] From top split: LEFT «דבר אל אהרן ואל בניו ואל כל בני ישראל
# ואמרת אליהם» / RIGHT «זה הדבר אשר צוה יהוה לאמר». Derive claim from Hebrew
# arms. Lev 17:2."
m.step("Lev.17.2")

# -------------------------- Lev.17.3 · ETNACHTA_SPLIT ----------------------
# איש איש מבית ישראל אשר ישחט שור או כשב או עז במחנה … או אשר ישחט מחוץ
# למחנה
# "[EN-AID] From top split: LEFT «איש איש מבית ישראל אשר ישחט שור או כשב או
# עז במחנה» / RIGHT «או אשר ישחט מחוץ למחנה». Derive claim from Hebrew arms.
# Lev 17:3."
m.step("Lev.17.3")
# witness-tier presupposed read: outside_slaughter_scope on asher_yishchat —
# read, not installed
m.witness_read("asher_yishchat", "outside_slaughter_scope",
                cites=["Sifra, Acharei Mot, Section 6 1", "Sifra, Acharei Mot, Section 6 3", "Sifra, Acharei Mot, Section 6 4", "Sifra, Acharei Mot, Section 6 5", "Sifra, Acharei Mot, Section 6 6", "Sifra, Acharei Mot, Section 6 7"])

# -------------------------- Lev.17.4 · ETNACHTA_SPLIT ----------------------
# ואל פתח אהל מועד לא הביאו להקריב קרבן ליהוה לפני משכן יהוה … דם יחשב לאיש
# ההוא דם שפך ונכרת האיש ההוא מקרב עמו
# "[EN-AID] From top split: LEFT «ואל פתח אהל מועד לא הביאו להקריב קרבן
# ליהוה לפני משכן יהוה» / RIGHT «דם יחשב לאיש ההוא דם שפך ונכרת האיש ההוא
# מקרב עמו». Derive claim from Hebrew arms. Lev 17:4."
m.step("Lev.17.4")
# witness-tier presupposed read: blood_reckoned on dam_yechashev — read, not
# installed
m.witness_read("dam_yechashev", "blood_reckoned",
                cites=["Sifra, Acharei Mot, Chapter 9 1", "Sifra, Acharei Mot, Chapter 9 2", "Sifra, Acharei Mot, Chapter 9 3", "Onkelos Lev 17:4"])

# -------------------------- Lev.17.5 · ETNACHTA_SPLIT ----------------------
# למען אשר יביאו בני ישראל את זבחיהם אשר הם זבחים על פני השדה  … וזבחו זבחי
# שלמים ליהוה אותם
# "[EN-AID] From top split: LEFT «למען אשר יביאו בני ישראל את זבחיהם אשר הם
# זבחים על פני השדה והביאם ליהוה אל פתח » / RIGHT «וזבחו זבחי שלמים ליהוה
# אותם». Derive claim from Hebrew arms. Lev 17:5."
m.step("Lev.17.5")
# witness-tier presupposed read: the_platform_table on al_pnei_hasadeh —
# read, not installed
m.witness_read("al_pnei_hasadeh", "the_platform_table",
                cites=["Sifra, Acharei Mot, Chapter 9 4", "Sifra, Acharei Mot, Chapter 9 5", "Sifra, Acharei Mot, Chapter 9 6", "Sifra, Acharei Mot, Chapter 9 7", "Onkelos Lev 17:6"])

# -------------------------- Lev.17.6 · ETNACHTA_SPLIT ----------------------
# וזרק הכהן את הדם על מזבח יהוה פתח אהל מועד … והקטיר החלב לריח ניחח ליהוה
# "[EN-AID] From top split: LEFT «וזרק הכהן את הדם על מזבח יהוה פתח אהל
# מועד» / RIGHT «והקטיר החלב לריח ניחח ליהוה». Derive claim from Hebrew
# arms. Lev 17:6."
m.step("Lev.17.6")

# -------------------------- Lev.17.7 · ETNACHTA_SPLIT ----------------------
# ולא יזבחו עוד את זבחיהם לשעירם אשר הם זנים אחריהם … חקת עולם תהיה זאת להם
# לדרתם
# "[EN-AID] From top split: LEFT «ולא יזבחו עוד את זבחיהם לשעירם אשר הם זנים
# אחריהם» / RIGHT «חקת עולם תהיה זאת להם לדרתם». Derive claim from Hebrew
# arms. Lev 17:7."
m.step("Lev.17.7")
# witness-tier presupposed read: the_demons on laseirim — read, not
# installed
m.witness_read("laseirim", "the_demons",
                cites=["Sifra, Acharei Mot, Chapter 9 8", "Sifra, Acharei Mot, Chapter 9 9", "Onkelos Lev 17:7"])

# -------------------------- Lev.17.8 · ETNACHTA_SPLIT ----------------------
# ואלהם תאמר איש איש מבית ישראל ומן הגר אשר יגור בתוכם … אשר יעלה עלה או זבח
# "[EN-AID] From top split: LEFT «ואלהם תאמר איש איש מבית ישראל ומן הגר אשר
# יגור בתוכם» / RIGHT «אשר יעלה עלה או זבח». Derive claim from Hebrew arms.
# Lev 17:8."
m.step("Lev.17.8")
# witness-tier presupposed read: the_completion_rule on asher_yaaleh — read,
# not installed
m.witness_read("asher_yaaleh", "the_completion_rule",
                cites=["Sifra, Acharei Mot, Chapter 10 2", "Sifra, Acharei Mot, Chapter 10 3", "Sifra, Acharei Mot, Chapter 10 4", "Sifra, Acharei Mot, Chapter 10 5", "Sifra, Acharei Mot, Chapter 10 8", "Sifra, Acharei Mot, Chapter 10 9", "Sifra, Acharei Mot, Chapter 10 10", "Sifra, Acharei Mot, Chapter 10 11"])

# -------------------------- Lev.17.9 · ETNACHTA_SPLIT ----------------------
# ואל פתח אהל מועד לא יביאנו לעשות אתו ליהוה … ונכרת האיש ההוא מעמיו
# "[EN-AID] From top split: LEFT «ואל פתח אהל מועד לא יביאנו לעשות אתו
# ליהוה» / RIGHT «ונכרת האיש ההוא מעמיו». Derive claim from Hebrew arms. Lev
# 17:9."
m.step("Lev.17.9")

# -------------------------- Lev.17.10 · ETNACHTA_SPLIT ---------------------
# ואיש איש מבית ישראל ומן הגר הגר בתוכם אשר יאכל כל דם … ונתתי פני בנפש
# האכלת את הדם והכרתי אתה מקרב עמה
# "[EN-AID] From top split: LEFT «ואיש איש מבית ישראל ומן הגר הגר בתוכם אשר
# יאכל כל דם» / RIGHT «ונתתי פני בנפש האכלת את הדם והכרתי אתה מקרב עמה».
# Derive claim from Hebrew arms. Lev 17:10."
m.step("Lev.17.10")
# witness-tier presupposed read: the_blood_ban on kol_dam — read, not
# installed
m.witness_read("kol_dam", "the_blood_ban",
                cites=["Sifra, Acharei Mot, Section 7 3", "Sifra, Acharei Mot, Section 7 4", "Sifra, Acharei Mot, Section 7 5", "Sifra, Acharei Mot, Section 7 6", "Sifra, Acharei Mot, Section 7 7", "Onkelos Lev 17:11"])

# -------------------------- Lev.17.11 · COND_כי ----------------------------
# כי נפש הבשר בדם הוא ואני נתתיו לכם על המזבח לכפר על נפשתיכם … כי הדם הוא
# בנפש יכפר
# "[EN-AID] From top split: LEFT «כי נפש הבשר בדם הוא ואני נתתיו לכם על
# המזבח לכפר על נפשתיכם» / RIGHT «כי הדם הוא בנפש יכפר». Derive claim from
# Hebrew arms. Lev 17:11."
m.step("Lev.17.11")

# -------------------------- Lev.17.12 · ETNACHTA_SPLIT ---------------------
# על כן אמרתי לבני ישראל כל נפש מכם לא תאכל דם … והגר הגר בתוככם לא יאכל דם
# "[EN-AID] From top split: LEFT «על כן אמרתי לבני ישראל כל נפש מכם לא תאכל
# דם» / RIGHT «והגר הגר בתוככם לא יאכל דם». Derive claim from Hebrew arms.
# Lev 17:12."
m.step("Lev.17.12")

# -------------------------- Lev.17.13 · ETNACHTA_SPLIT ---------------------
# ואיש איש מבני ישראל ומן הגר הגר בתוכם אשר יצוד ציד חיה או עו … ושפך את דמו
# וכסהו בעפר
# "[EN-AID] From top split: LEFT «ואיש איש מבני ישראל ומן הגר הגר בתוכם אשר
# יצוד ציד חיה או עוף אשר יאכל» / RIGHT «ושפך את דמו וכסהו בעפר». Derive
# claim from Hebrew arms. Lev 17:13."
m.step("Lev.17.13")
# witness-tier presupposed read: the_covering_machine on veshafach_vechisahu
# — read, not installed
m.witness_read("veshafach_vechisahu", "the_covering_machine",
                cites=["Sifra, Acharei Mot, Chapter 11 2", "Sifra, Acharei Mot, Chapter 11 4", "Sifra, Acharei Mot, Chapter 11 5", "Sifra, Acharei Mot, Chapter 11 6", "Sifra, Acharei Mot, Chapter 11 7", "Sifra, Acharei Mot, Chapter 11 8", "Sifra, Acharei Mot, Chapter 11 10", "Sifra, Acharei Mot, Chapter 11 11", "Onkelos Lev 17:13"])

# -------------------------- Lev.17.14 · COND_כי ----------------------------
# כי נפש כל בשר דמו בנפשו הוא ואמר לבני ישראל דם כל בשר לא תאכ … כי נפש כל
# בשר דמו הוא כל אכליו יכרת
# "[EN-AID] From top split: LEFT «כי נפש כל בשר דמו בנפשו הוא ואמר לבני
# ישראל דם כל בשר לא תאכלו» / RIGHT «כי נפש כל בשר דמו הוא כל אכליו יכרת».
# Derive claim from Hebrew arms. Lev 17:14."
m.step("Lev.17.14")

# -------------------------- Lev.17.15 · ETNACHTA_SPLIT ---------------------
# וכל נפש אשר תאכל נבלה וטרפה באזרח ובגר … וכבס בגדיו ורחץ במים וטמא עד הערב
# וטהר
# "[EN-AID] From top split: LEFT «וכל נפש אשר תאכל נבלה וטרפה באזרח ובגר» /
# RIGHT «וכבס בגדיו ורחץ במים וטמא עד הערב וטהר». Derive claim from Hebrew
# arms. Lev 17:15."
m.step("Lev.17.15")
# witness-tier presupposed read: the_swallow_house on nevelah_utrefah —
# read, not installed
m.witness_read("nevelah_utrefah", "the_swallow_house",
                cites=["Sifra, Acharei Mot, Chapter 12 2", "Sifra, Acharei Mot, Chapter 12 3", "Sifra, Acharei Mot, Chapter 12 4", "Sifra, Acharei Mot, Chapter 12 5", "Sifra, Acharei Mot, Chapter 12 7", "Sifra, Acharei Mot, Chapter 12 9", "Sifra, Acharei Mot, Chapter 12 13", "Onkelos Lev 17:15", "Onkelos Lev 17:16"])

# -------------------------- Lev.17.16 · COND_ואם ---------------------------
# ואם לא יכבס ובשרו לא ירחץ … ונשא עונו
# "[EN-AID] From top split: LEFT «ואם לא יכבס ובשרו לא ירחץ» / RIGHT «ונשא
# עונו». Derive claim from Hebrew arms. Lev 17:16."
m.step("Lev.17.16")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('asher_yishchat', 'outside_slaughter_scope'), ('dam_yechashev', 'blood_reckoned'), ('al_pnei_hasadeh', 'the_platform_table'), ('laseirim', 'the_demons'), ('asher_yaaleh', 'the_completion_rule'), ('kol_dam', 'the_blood_ban'), ('veshafach_vechisahu', 'the_covering_machine'), ('nevelah_utrefah', 'the_swallow_house')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Acharei Mot, Section 6 1', 'Sifra, Acharei Mot, Section 6 3', 'Sifra, Acharei Mot, Section 6 4', 'Sifra, Acharei Mot, Section 6 5', 'Sifra, Acharei Mot, Section 6 6', 'Sifra, Acharei Mot, Section 6 7']
    assert all('outside_slaughter_scope' not in f for f in m.WORLD["facts"])
    assert 'asher_yishchat' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Acharei Mot, Chapter 9 1', 'Sifra, Acharei Mot, Chapter 9 2', 'Sifra, Acharei Mot, Chapter 9 3', 'Onkelos Lev 17:4']
    assert all('blood_reckoned' not in f for f in m.WORLD["facts"])
    assert 'dam_yechashev' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Acharei Mot, Chapter 9 4', 'Sifra, Acharei Mot, Chapter 9 5', 'Sifra, Acharei Mot, Chapter 9 6', 'Sifra, Acharei Mot, Chapter 9 7', 'Onkelos Lev 17:6']
    assert all('the_platform_table' not in f for f in m.WORLD["facts"])
    assert 'al_pnei_hasadeh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Acharei Mot, Chapter 9 8', 'Sifra, Acharei Mot, Chapter 9 9', 'Onkelos Lev 17:7']
    assert all('the_demons' not in f for f in m.WORLD["facts"])
    assert 'laseirim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Acharei Mot, Chapter 10 2', 'Sifra, Acharei Mot, Chapter 10 3', 'Sifra, Acharei Mot, Chapter 10 4', 'Sifra, Acharei Mot, Chapter 10 5', 'Sifra, Acharei Mot, Chapter 10 8', 'Sifra, Acharei Mot, Chapter 10 9', 'Sifra, Acharei Mot, Chapter 10 10', 'Sifra, Acharei Mot, Chapter 10 11']
    assert all('the_completion_rule' not in f for f in m.WORLD["facts"])
    assert 'asher_yaaleh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Acharei Mot, Section 7 3', 'Sifra, Acharei Mot, Section 7 4', 'Sifra, Acharei Mot, Section 7 5', 'Sifra, Acharei Mot, Section 7 6', 'Sifra, Acharei Mot, Section 7 7', 'Onkelos Lev 17:11']
    assert all('the_blood_ban' not in f for f in m.WORLD["facts"])
    assert 'kol_dam' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Acharei Mot, Chapter 11 2', 'Sifra, Acharei Mot, Chapter 11 4', 'Sifra, Acharei Mot, Chapter 11 5', 'Sifra, Acharei Mot, Chapter 11 6', 'Sifra, Acharei Mot, Chapter 11 7', 'Sifra, Acharei Mot, Chapter 11 8', 'Sifra, Acharei Mot, Chapter 11 10', 'Sifra, Acharei Mot, Chapter 11 11', 'Onkelos Lev 17:13']
    assert all('the_covering_machine' not in f for f in m.WORLD["facts"])
    assert 'veshafach_vechisahu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Acharei Mot, Chapter 12 2', 'Sifra, Acharei Mot, Chapter 12 3', 'Sifra, Acharei Mot, Chapter 12 4', 'Sifra, Acharei Mot, Chapter 12 5', 'Sifra, Acharei Mot, Chapter 12 7', 'Sifra, Acharei Mot, Chapter 12 9', 'Sifra, Acharei Mot, Chapter 12 13', 'Onkelos Lev 17:15', 'Onkelos Lev 17:16']
    assert all('the_swallow_house' not in f for f in m.WORLD["facts"])
    assert 'nevelah_utrefah' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
