#!/usr/bin/env python3
# =============================================================================
# exo_25_ark_table_menorah — 25:1-40
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_25_ark_table_menorah.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Terumah: gifts; ark; table; menorah (25:1–40)"""
from machine import Machine

m = Machine("exo_25_ark_table_menorah")

# -------------------------- Exod.25.1 · TREE_CLAIM -------------------------
# וידבר יהוה … אל משה לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה» / RIGHT «אל משה לאמר». Derive
# claim from Hebrew arms, not English alone. Exod 25:1."
m.step("Exod.25.1")

# -------------------------- Exod.25.2 · ETNACHTA_SPLIT ---------------------
# דבר אל בני ישראל ויקחו לי תרומה … מאת כל איש אשר ידבנו לבו תקחו את תרומתי
# "[EN-AID] From top split: LEFT «דבר אל בני ישראל ויקחו לי תרומה» / RIGHT
# «מאת כל איש אשר ידבנו לבו תקחו את תרומתי». Derive claim from Hebrew arms,
# not English alone. Exod 25:2."
m.step("Exod.25.2")
# witness-tier presupposed read: separation_before on take_offering — read,
# not installed
m.witness_read("take_offering", "separation_before",
                cites=["Onkelos Exod 25"])
# witness-tier presupposed read: five_disqualified on separation_clause —
# read, not installed
m.witness_read("separation_clause", "five_disqualified",
                cites=["Midrash Tanchuma, Terumah 1", "Midrash Tanchuma, Terumah 3", "Mishnah Shekalim 4:6"])

# -------------------------- Exod.25.3 · ETNACHTA_SPLIT ---------------------
# וזאת התרומה אשר תקחו מאתם … זהב וכסף ונחשת
# "[EN-AID] From top split: LEFT «וזאת התרומה אשר תקחו מאתם» / RIGHT «זהב
# וכסף ונחשת». Derive claim from Hebrew arms, not English alone. Exod 25:3."
m.step("Exod.25.3")

# -------------------------- Exod.25.4 · TREE_CLAIM -------------------------
# ותכלת וארגמן ותולעת שני … ושש ועזים
# "[EN-AID] From top split: LEFT «ותכלת וארגמן ותולעת שני» / RIGHT «ושש
# ועזים». Derive claim from Hebrew arms, not English alone. Exod 25:4."
m.step("Exod.25.4")

# -------------------------- Exod.25.5 · TREE_CLAIM -------------------------
# וערת אילם מאדמים וערת תחשים … ועצי שטים
# "[EN-AID] From top split: LEFT «וערת אילם מאדמים וערת תחשים» / RIGHT «ועצי
# שטים». Derive claim from Hebrew arms, not English alone. Exod 25:5."
m.step("Exod.25.5")
# witness-tier presupposed read: thirteen_and_tachash on materials_list —
# read, not installed
m.witness_read("materials_list", "thirteen_and_tachash",
                cites=["Midrash Tanchuma, Terumah 5", "Midrash Tanchuma, Terumah 6"])

# -------------------------- Exod.25.6 · ETNACHTA_SPLIT ---------------------
# שמן למאר … בשמים לשמן המשחה ולקטרת הסמים
# "[EN-AID] From top split: LEFT «שמן למאר» / RIGHT «בשמים לשמן המשחה ולקטרת
# הסמים». Derive claim from Hebrew arms, not English alone. Exod 25:6."
m.step("Exod.25.6")

# -------------------------- Exod.25.7 · ETNACHTA_SPLIT ---------------------
# אבני שהם ואבני מלאים … לאפד ולחשן
# "[EN-AID] From top split: LEFT «אבני שהם ואבני מלאים» / RIGHT «לאפד
# ולחשן». Derive claim from Hebrew arms, not English alone. Exod 25:7."
m.step("Exod.25.7")

# -------------------------- Exod.25.8 · ETNACHTA_SPLIT ---------------------
# ועשו לי מקדש … ושכנתי בתוכם
# "[EN-AID] From top split: LEFT «ועשו לי מקדש» / RIGHT «ושכנתי בתוכם».
# Derive claim from Hebrew arms, not English alone. Exod 25:8."
m.step("Exod.25.8")
# witness-tier presupposed read: presence_among_them on sanctuary_command —
# read, not installed
m.witness_read("sanctuary_command", "presence_among_them",
                cites=["Onkelos Exod 25"])
# witness-tier presupposed read: yom_kippur_timestamp on sanctuary_command —
# read, not installed
m.witness_read("sanctuary_command", "yom_kippur_timestamp",
                cites=["Midrash Tanchuma, Terumah 8"])

# -------------------------- Exod.25.9 · ETNACHTA_SPLIT ---------------------
# ככל אשר אני מראה אותך את תבנית המשכן ואת תבנית כל כליו … וכן תעשו
# "[EN-AID] From top split: LEFT «ככל אשר אני מראה אותך את תבנית המשכן ואת
# תבנית כל כליו» / RIGHT «וכן תעשו». Derive claim from Hebrew arms, not
# English alone. Exod 25:9."
m.step("Exod.25.9")
# witness-tier presupposed read: constitutional_so_shall_you_make on
# pattern_clause — read, not installed
m.witness_read("pattern_clause", "constitutional_so_shall_you_make",
                cites=["Mishnah Sanhedrin 1:5", "Mishnah Shevuot 2:2", "Onkelos Exod 25"])

# -------------------------- Exod.25.10 · ETNACHTA_SPLIT --------------------
# ועשו ארון עצי שטים … אמתים וחצי ארכו ואמה וחצי רחבו ואמה וחצי קמתו
# "[EN-AID] From top split: LEFT «ועשו ארון עצי שטים» / RIGHT «אמתים וחצי
# ארכו ואמה וחצי רחבו ואמה וחצי קמתו». Derive claim from Hebrew arms, not
# English alone. Exod 25:10."
m.step("Exod.25.10")

# -------------------------- Exod.25.11 · ETNACHTA_SPLIT --------------------
# וצפית אתו זהב טהור מבית ומחוץ תצפנו … ועשית עליו זר זהב סביב
# "[EN-AID] From top split: LEFT «וצפית אתו זהב טהור מבית ומחוץ תצפנו» /
# RIGHT «ועשית עליו זר זהב סביב». Derive claim from Hebrew arms, not English
# alone. Exod 25:11."
m.step("Exod.25.11")

# -------------------------- Exod.25.12 · ETNACHTA_SPLIT --------------------
# ויצקת לו ארבע טבעת זהב ונתתה על ארבע פעמתיו … ושתי טבעת על צלעו האחת ושתי
# טבעת על צלעו השנית
# "[EN-AID] From top split: LEFT «ויצקת לו ארבע טבעת זהב ונתתה על ארבע
# פעמתיו» / RIGHT «ושתי טבעת על צלעו האחת ושתי טבעת על צלעו השנית». Derive
# claim from Hebrew arms, not English alone. Exod 25:12."
m.step("Exod.25.12")

# -------------------------- Exod.25.13 · ETNACHTA_SPLIT --------------------
# ועשית בדי עצי שטים … וצפית אתם זהב
# "[EN-AID] From top split: LEFT «ועשית בדי עצי שטים» / RIGHT «וצפית אתם
# זהב». Derive claim from Hebrew arms, not English alone. Exod 25:13."
m.step("Exod.25.13")

# -------------------------- Exod.25.14 · ETNACHTA_SPLIT --------------------
# והבאת את הבדים בטבעת על צלעת הארן … לשאת את הארן בהם
# "[EN-AID] From top split: LEFT «והבאת את הבדים בטבעת על צלעת הארן» / RIGHT
# «לשאת את הארן בהם». Derive claim from Hebrew arms, not English alone. Exod
# 25:14."
m.step("Exod.25.14")

# -------------------------- Exod.25.15 · ETNACHTA_SPLIT --------------------
# בטבעת הארן יהיו הבדים … לא יסרו ממנו
# "[EN-AID] From top split: LEFT «בטבעת הארן יהיו הבדים» / RIGHT «לא יסרו
# ממנו». Derive claim from Hebrew arms, not English alone. Exod 25:15."
m.step("Exod.25.15")
# witness-tier presupposed read: never_removed on poles_clause — read, not
# installed
m.witness_read("poles_clause", "never_removed",
                cites=["Onkelos Exod 25"])

# -------------------------- Exod.25.16 · ETNACHTA_SPLIT --------------------
# ונתת אל הארן … את העדת אשר אתן אליך
# "[EN-AID] From top split: LEFT «ונתת אל הארן» / RIGHT «את העדת אשר אתן
# אליך». Derive claim from Hebrew arms, not English alone. Exod 25:16."
m.step("Exod.25.16")

# -------------------------- Exod.25.17 · ETNACHTA_SPLIT --------------------
# ועשית כפרת זהב טהור … אמתים וחצי ארכה ואמה וחצי רחבה
# "[EN-AID] From top split: LEFT «ועשית כפרת זהב טהור» / RIGHT «אמתים וחצי
# ארכה ואמה וחצי רחבה». Derive claim from Hebrew arms, not English alone.
# Exod 25:17."
m.step("Exod.25.17")

# -------------------------- Exod.25.18 · ETNACHTA_SPLIT --------------------
# ועשית שנים כרבים זהב … מקשה תעשה אתם משני קצות הכפרת
# "[EN-AID] From top split: LEFT «ועשית שנים כרבים זהב» / RIGHT «מקשה תעשה
# אתם משני קצות הכפרת». Derive claim from Hebrew arms, not English alone.
# Exod 25:18."
m.step("Exod.25.18")

# -------------------------- Exod.25.19 · ETNACHTA_SPLIT --------------------
# ועשה כרוב אחד מקצה מזה וכרוב אחד מקצה מזה … מן הכפרת תעשו את הכרבים על שני
# קצותיו
# "[EN-AID] From top split: LEFT «ועשה כרוב אחד מקצה מזה וכרוב אחד מקצה מזה»
# / RIGHT «מן הכפרת תעשו את הכרבים על שני קצותיו». Derive claim from Hebrew
# arms, not English alone. Exod 25:19."
m.step("Exod.25.19")

# -------------------------- Exod.25.20 · ETNACHTA_SPLIT --------------------
# והיו הכרבים פרשי כנפים למעלה סככים בכנפיהם על הכפרת ופניהם א … אל הכפרת
# יהיו פני הכרבים
# "[EN-AID] From top split: LEFT «והיו הכרבים פרשי כנפים למעלה סככים בכנפיהם
# על הכפרת ופניהם איש אל אחיו» / RIGHT «אל הכפרת יהיו פני הכרבים». Derive
# claim from Hebrew arms, not English alone. Exod 25:20."
m.step("Exod.25.20")

# -------------------------- Exod.25.21 · ETNACHTA_SPLIT --------------------
# ונתת את הכפרת על הארן מלמעלה … ואל הארן תתן את העדת אשר אתן אליך
# "[EN-AID] From top split: LEFT «ונתת את הכפרת על הארן מלמעלה» / RIGHT «ואל
# הארן תתן את העדת אשר אתן אליך». Derive claim from Hebrew arms, not English
# alone. Exod 25:21."
m.step("Exod.25.21")

# -------------------------- Exod.25.22 · ETNACHTA_SPLIT --------------------
# ונועדתי לך שם ודברתי אתך מעל הכפרת מבין שני הכרבים אשר על אר … את כל אשר
# אצוה אותך אל בני ישראל
# "[EN-AID] From top split: LEFT «ונועדתי לך שם ודברתי אתך מעל הכפרת מבין
# שני הכרבים אשר על ארן העדת» / RIGHT «את כל אשר אצוה אותך אל בני ישראל».
# Derive claim from Hebrew arms, not English alone. Exod 25:22."
m.step("Exod.25.22")
# witness-tier presupposed read: word_appointed on meeting_clause — read,
# not installed
m.witness_read("meeting_clause", "word_appointed",
                cites=["Onkelos Exod 25"])

# -------------------------- Exod.25.23 · ETNACHTA_SPLIT --------------------
# ועשית שלחן עצי שטים … אמתים ארכו ואמה רחבו ואמה וחצי קמתו
# "[EN-AID] From top split: LEFT «ועשית שלחן עצי שטים» / RIGHT «אמתים ארכו
# ואמה רחבו ואמה וחצי קמתו». Derive claim from Hebrew arms, not English
# alone. Exod 25:23."
m.step("Exod.25.23")
# witness-tier presupposed read: conversion_dispute on table_dimensions —
# read, not installed
m.witness_read("table_dimensions", "conversion_dispute",
                cites=["Mishnah Menachot 11:5", "Mishnah Menachot 11:4"])

# -------------------------- Exod.25.24 · ETNACHTA_SPLIT --------------------
# וצפית אתו זהב טהור … ועשית לו זר זהב סביב
# "[EN-AID] From top split: LEFT «וצפית אתו זהב טהור» / RIGHT «ועשית לו זר
# זהב סביב». Derive claim from Hebrew arms, not English alone. Exod 25:24."
m.step("Exod.25.24")

# -------------------------- Exod.25.25 · ETNACHTA_SPLIT --------------------
# ועשית לו מסגרת טפח סביב … ועשית זר זהב למסגרתו סביב
# "[EN-AID] From top split: LEFT «ועשית לו מסגרת טפח סביב» / RIGHT «ועשית זר
# זהב למסגרתו סביב». Derive claim from Hebrew arms, not English alone. Exod
# 25:25."
m.step("Exod.25.25")

# -------------------------- Exod.25.26 · ETNACHTA_SPLIT --------------------
# ועשית לו ארבע טבעת זהב … ונתת את הטבעת על ארבע הפאת אשר לארבע רגליו
# "[EN-AID] From top split: LEFT «ועשית לו ארבע טבעת זהב» / RIGHT «ונתת את
# הטבעת על ארבע הפאת אשר לארבע רגליו». Derive claim from Hebrew arms, not
# English alone. Exod 25:26."
m.step("Exod.25.26")

# -------------------------- Exod.25.27 · ETNACHTA_SPLIT --------------------
# לעמת המסגרת תהיין הטבעת … לבתים לבדים לשאת את השלחן
# "[EN-AID] From top split: LEFT «לעמת המסגרת תהיין הטבעת» / RIGHT «לבתים
# לבדים לשאת את השלחן». Derive claim from Hebrew arms, not English alone.
# Exod 25:27."
m.step("Exod.25.27")

# -------------------------- Exod.25.28 · ETNACHTA_SPLIT --------------------
# ועשית את הבדים עצי שטים וצפית אתם זהב … ונשא בם את השלחן
# "[EN-AID] From top split: LEFT «ועשית את הבדים עצי שטים וצפית אתם זהב» /
# RIGHT «ונשא בם את השלחן». Derive claim from Hebrew arms, not English
# alone. Exod 25:28."
m.step("Exod.25.28")

# -------------------------- Exod.25.29 · ETNACHTA_SPLIT --------------------
# ועשית קערתיו וכפתיו וקשותיו ומנקיתיו אשר יסך בהן … זהב טהור תעשה אתם
# "[EN-AID] From top split: LEFT «ועשית קערתיו וכפתיו וקשותיו ומנקיתיו אשר
# יסך בהן» / RIGHT «זהב טהור תעשה אתם». Derive claim from Hebrew arms, not
# English alone. Exod 25:29."
m.step("Exod.25.29")

# -------------------------- Exod.25.30 · TREE_CLAIM ------------------------
# ונתת על השלחן לחם פנים … לפני תמיד
# "[EN-AID] From top split: LEFT «ונתת על השלחן לחם פנים» / RIGHT «לפני
# תמיד». Derive claim from Hebrew arms, not English alone. Exod 25:30."
m.step("Exod.25.30")
# witness-tier presupposed read: continual_duty on showbread_clause — read,
# not installed
m.witness_read("showbread_clause", "continual_duty",
                cites=["Mishnah Menachot 11:4", "Mishnah Menachot 11:5", "Mishnah Menachot 11:7", "Onkelos Exod 25"])
# witness-tier presupposed read: exchange_dispute on tamid_token — read, not
# installed
m.witness_read("tamid_token", "exchange_dispute",
                cites=["Mishnah Menachot 11:7", "Mishnah Menachot 11:6"])

# -------------------------- Exod.25.31 · ETNACHTA_SPLIT --------------------
# ועשית מנרת זהב טהור … מקשה תעשה המנורה ירכה וקנה גביעיה כפתריה ופרחיה ממנה
# יהיו
# "[EN-AID] From top split: LEFT «ועשית מנרת זהב טהור» / RIGHT «מקשה תעשה
# המנורה ירכה וקנה גביעיה כפתריה ופרחיה ממנה יהיו». Derive claim from Hebrew
# arms, not English alone. Exod 25:31."
m.step("Exod.25.31")

# -------------------------- Exod.25.32 · ETNACHTA_SPLIT --------------------
# וששה קנים יצאים מצדיה … שלשה קני מנרה מצדה האחד ושלשה קני מנרה מצדה השני
# "[EN-AID] From top split: LEFT «וששה קנים יצאים מצדיה» / RIGHT «שלשה קני
# מנרה מצדה האחד ושלשה קני מנרה מצדה השני». Derive claim from Hebrew arms,
# not English alone. Exod 25:32."
m.step("Exod.25.32")

# -------------------------- Exod.25.33 · ETNACHTA_SPLIT --------------------
# שלשה גבעים משקדים בקנה האחד כפתר ופרח ושלשה גבעים משקדים בקנ … כן לששת
# הקנים היצאים מן המנרה
# "[EN-AID] From top split: LEFT «שלשה גבעים משקדים בקנה האחד כפתר ופרח
# ושלשה גבעים משקדים בקנה האחד כפתר ופרח» / RIGHT «כן לששת הקנים היצאים מן
# המנרה». Derive claim from Hebrew arms, not English alone. Exod 25:33."
m.step("Exod.25.33")

# -------------------------- Exod.25.34 · ETNACHTA_SPLIT --------------------
# ובמנרה ארבעה גבעים … משקדים כפתריה ופרחיה
# "[EN-AID] From top split: LEFT «ובמנרה ארבעה גבעים» / RIGHT «משקדים כפתריה
# ופרחיה». Derive claim from Hebrew arms, not English alone. Exod 25:34."
m.step("Exod.25.34")

# -------------------------- Exod.25.35 · ETNACHTA_SPLIT --------------------
# וכפתר תחת שני הקנים ממנה וכפתר תחת שני הקנים ממנה וכפתר תחת  … לששת הקנים
# היצאים מן המנרה
# "[EN-AID] From top split: LEFT «וכפתר תחת שני הקנים ממנה וכפתר תחת שני
# הקנים ממנה וכפתר תחת שני הקנים ממנה» / RIGHT «לששת הקנים היצאים מן המנרה».
# Derive claim from Hebrew arms, not English alone. Exod 25:35."
m.step("Exod.25.35")

# -------------------------- Exod.25.36 · ETNACHTA_SPLIT --------------------
# כפתריהם וקנתם ממנה יהיו … כלה מקשה אחת זהב טהור
# "[EN-AID] From top split: LEFT «כפתריהם וקנתם ממנה יהיו» / RIGHT «כלה מקשה
# אחת זהב טהור». Derive claim from Hebrew arms, not English alone. Exod
# 25:36."
m.step("Exod.25.36")
# witness-tier presupposed read: one_piece_seven on menorah_clauses — read,
# not installed
m.witness_read("menorah_clauses", "one_piece_seven",
                cites=["Mishnah Menachot 3:7", "Onkelos Exod 25"])

# -------------------------- Exod.25.37 · ETNACHTA_SPLIT --------------------
# ועשית את נרתיה שבעה … והעלה את נרתיה והאיר על עבר פניה
# "[EN-AID] From top split: LEFT «ועשית את נרתיה שבעה» / RIGHT «והעלה את
# נרתיה והאיר על עבר פניה». Derive claim from Hebrew arms, not English
# alone. Exod 25:37."
m.step("Exod.25.37")

# -------------------------- Exod.25.38 · TREE_CLAIM ------------------------
# ומלקחיה ומחתתיה … זהב טהור
# "[EN-AID] From top split: LEFT «ומלקחיה ומחתתיה» / RIGHT «זהב טהור».
# Derive claim from Hebrew arms, not English alone. Exod 25:38."
m.step("Exod.25.38")

# -------------------------- Exod.25.39 · ETNACHTA_SPLIT --------------------
# ככר זהב טהור יעשה אתה … את כל הכלים האלה
# "[EN-AID] From top split: LEFT «ככר זהב טהור יעשה אתה» / RIGHT «את כל
# הכלים האלה». Derive claim from Hebrew arms, not English alone. Exod
# 25:39."
m.step("Exod.25.39")

# -------------------------- Exod.25.40 · ETNACHTA_SPLIT --------------------
# וראה ועשה … בתבניתם אשר אתה מראה בהר
# "[EN-AID] From top split: LEFT «וראה ועשה» / RIGHT «בתבניתם אשר אתה מראה
# בהר». Derive claim from Hebrew arms, not English alone. Exod 25:40."
m.step("Exod.25.40")

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('take_offering', 'separation_before'), ('separation_clause', 'five_disqualified'), ('materials_list', 'thirteen_and_tachash'), ('sanctuary_command', 'presence_among_them'), ('sanctuary_command', 'yom_kippur_timestamp'), ('pattern_clause', 'constitutional_so_shall_you_make'), ('poles_clause', 'never_removed'), ('meeting_clause', 'word_appointed'), ('table_dimensions', 'conversion_dispute'), ('showbread_clause', 'continual_duty'), ('tamid_token', 'exchange_dispute'), ('menorah_clauses', 'one_piece_seven')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Exod 25']
    assert all('separation_before' not in f for f in m.WORLD["facts"])
    assert 'take_offering' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Midrash Tanchuma, Terumah 1', 'Midrash Tanchuma, Terumah 3', 'Mishnah Shekalim 4:6']
    assert all('five_disqualified' not in f for f in m.WORLD["facts"])
    assert 'separation_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Midrash Tanchuma, Terumah 5', 'Midrash Tanchuma, Terumah 6']
    assert all('thirteen_and_tachash' not in f for f in m.WORLD["facts"])
    assert 'materials_list' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Onkelos Exod 25']
    assert all('presence_among_them' not in f for f in m.WORLD["facts"])
    assert 'sanctuary_command' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Midrash Tanchuma, Terumah 8']
    assert all('yom_kippur_timestamp' not in f for f in m.WORLD["facts"])
    assert 'sanctuary_command' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Sanhedrin 1:5', 'Mishnah Shevuot 2:2', 'Onkelos Exod 25']
    assert all('constitutional_so_shall_you_make' not in f for f in m.WORLD["facts"])
    assert 'pattern_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Onkelos Exod 25']
    assert all('never_removed' not in f for f in m.WORLD["facts"])
    assert 'poles_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Exod 25']
    assert all('word_appointed' not in f for f in m.WORLD["facts"])
    assert 'meeting_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Mishnah Menachot 11:5', 'Mishnah Menachot 11:4']
    assert all('conversion_dispute' not in f for f in m.WORLD["facts"])
    assert 'table_dimensions' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Mishnah Menachot 11:4', 'Mishnah Menachot 11:5', 'Mishnah Menachot 11:7', 'Onkelos Exod 25']
    assert all('continual_duty' not in f for f in m.WORLD["facts"])
    assert 'showbread_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Mishnah Menachot 11:7', 'Mishnah Menachot 11:6']
    assert all('exchange_dispute' not in f for f in m.WORLD["facts"])
    assert 'tamid_token' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Mishnah Menachot 3:7', 'Onkelos Exod 25']
    assert all('one_piece_seven' not in f for f in m.WORLD["facts"])
    assert 'menorah_clauses' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
