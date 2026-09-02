#!/usr/bin/env python3
# =============================================================================
# exo_28_priest_garments — 28:1-43
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_28_priest_garments.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Priest garments: ephod, breastpiece, robe, tzitz (28:1–43)"""
from machine import Machine

m = Machine("exo_28_priest_garments")

# -------------------------- Exod.28.1 · ETNACHTA_SPLIT ---------------------
# ואתה הקרב אליך את אהרן אחיך ואת בניו אתו מתוך בני ישראל לכהנ … אהרן נדב
# ואביהוא אלעזר ואיתמר בני אהרן
# "[EN-AID] From top split: LEFT «ואתה הקרב אליך את אהרן אחיך ואת בניו אתו
# מתוך בני ישראל לכהנו לי» / RIGHT «אהרן נדב ואביהוא אלעזר ואיתמר בני אהרן».
# Derive claim from Hebrew arms, not English alone. Exod 28:1."
m.step("Exod.28.1")
# witness-tier presupposed read: service_before_me on priest_verb — read,
# not installed
m.witness_read("priest_verb", "service_before_me",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.2 · ETNACHTA_SPLIT ---------------------
# ועשית בגדי קדש לאהרן אחיך … לכבוד ולתפארת
# "[EN-AID] From top split: LEFT «ועשית בגדי קדש לאהרן אחיך» / RIGHT «לכבוד
# ולתפארת». Derive claim from Hebrew arms, not English alone. Exod 28:2."
m.step("Exod.28.2")
# witness-tier presupposed read: honor_splendor_census on garment_purpose —
# read, not installed
m.witness_read("garment_purpose", "honor_splendor_census",
                cites=["Mishnah Yoma 7:5", "Onkelos Exod 28"])

# -------------------------- Exod.28.3 · ETNACHTA_SPLIT ---------------------
# ואתה תדבר אל כל חכמי לב אשר מלאתיו רוח חכמה … ועשו את בגדי אהרן לקדשו
# לכהנו לי
# "[EN-AID] From top split: LEFT «ואתה תדבר אל כל חכמי לב אשר מלאתיו רוח
# חכמה» / RIGHT «ועשו את בגדי אהרן לקדשו לכהנו לי». Derive claim from Hebrew
# arms, not English alone. Exod 28:3."
m.step("Exod.28.3")

# -------------------------- Exod.28.4 · ETNACHTA_SPLIT ---------------------
# ואלה הבגדים אשר יעשו חשן ואפוד ומעיל וכתנת תשבץ מצנפת ואבנט … ועשו בגדי
# קדש לאהרן אחיך ולבניו לכהנו לי
# "[EN-AID] From top split: LEFT «ואלה הבגדים אשר יעשו חשן ואפוד ומעיל וכתנת
# תשבץ מצנפת ואבנט» / RIGHT «ועשו בגדי קדש לאהרן אחיך ולבניו לכהנו לי».
# Derive claim from Hebrew arms, not English alone. Exod 28:4."
m.step("Exod.28.4")
# witness-tier presupposed read: mirror_table on garment_list — read, not
# installed
m.witness_read("garment_list", "mirror_table",
                cites=["Midrash Tanchuma, Tetzaveh 1"])
# witness-tier presupposed read: access_list on oracle_protocol — read, not
# installed
m.witness_read("oracle_protocol", "access_list",
                cites=["Mishnah Yoma 7:5"])

# -------------------------- Exod.28.5 · ETNACHTA_SPLIT ---------------------
# והם יקחו את הזהב ואת התכלת ואת הארגמן … ואת תולעת השני ואת השש
# "[EN-AID] From top split: LEFT «והם יקחו את הזהב ואת התכלת ואת הארגמן» /
# RIGHT «ואת תולעת השני ואת השש». Derive claim from Hebrew arms, not English
# alone. Exod 28:5."
m.step("Exod.28.5")
# witness-tier presupposed read: fiscal_plurality on plural_take — read, not
# installed
m.witness_read("plural_take", "fiscal_plurality",
                cites=["Mishnah Shekalim 5:2"])

# -------------------------- Exod.28.6 · ETNACHTA_SPLIT ---------------------
# ועשו את האפד … זהב תכלת וארגמן תולעת שני ושש משזר מעשה חשב
# "[EN-AID] From top split: LEFT «ועשו את האפד» / RIGHT «זהב תכלת וארגמן
# תולעת שני ושש משזר מעשה חשב». Derive claim from Hebrew arms, not English
# alone. Exod 28:6."
m.step("Exod.28.6")

# -------------------------- Exod.28.7 · TREE_CLAIM -------------------------
# שתי כתפת חברת יהיה לו אל שני קצותיו
# "[EN-AID] From top split: LEFT «שתי כתפת חברת יהיה לו אל שני קצותיו» /
# RIGHT «». Derive claim from Hebrew arms, not English alone. Exod 28:7."
m.step("Exod.28.7")

# -------------------------- Exod.28.8 · ETNACHTA_SPLIT ---------------------
# וחשב אפדתו אשר עליו כמעשהו ממנו יהיה … זהב תכלת וארגמן ותולעת שני ושש משזר
# "[EN-AID] From top split: LEFT «וחשב אפדתו אשר עליו כמעשהו ממנו יהיה» /
# RIGHT «זהב תכלת וארגמן ותולעת שני ושש משזר». Derive claim from Hebrew
# arms, not English alone. Exod 28:8."
m.step("Exod.28.8")

# -------------------------- Exod.28.9 · ETNACHTA_SPLIT ---------------------
# ולקחת את שתי אבני שהם … ופתחת עליהם שמות בני ישראל
# "[EN-AID] From top split: LEFT «ולקחת את שתי אבני שהם» / RIGHT «ופתחת
# עליהם שמות בני ישראל». Derive claim from Hebrew arms, not English alone.
# Exod 28:9."
m.step("Exod.28.9")

# -------------------------- Exod.28.10 · ETNACHTA_SPLIT --------------------
# ששה משמתם על האבן האחת … ואת שמות הששה הנותרים על האבן השנית כתולדתם
# "[EN-AID] From top split: LEFT «ששה משמתם על האבן האחת» / RIGHT «ואת שמות
# הששה הנותרים על האבן השנית כתולדתם». Derive claim from Hebrew arms, not
# English alone. Exod 28:10."
m.step("Exod.28.10")

# -------------------------- Exod.28.11 · ETNACHTA_SPLIT --------------------
# מעשה חרש אבן פתוחי חתם תפתח את שתי האבנים על שמת בני ישראל … מסבת משבצות
# זהב תעשה אתם
# "[EN-AID] From top split: LEFT «מעשה חרש אבן פתוחי חתם תפתח את שתי האבנים
# על שמת בני ישראל» / RIGHT «מסבת משבצות זהב תעשה אתם». Derive claim from
# Hebrew arms, not English alone. Exod 28:11."
m.step("Exod.28.11")

# -------------------------- Exod.28.12 · ETNACHTA_SPLIT --------------------
# ושמת את שתי האבנים על כתפת האפד אבני זכרן לבני ישראל … ונשא אהרן את שמותם
# לפני יהוה על שתי כתפיו לזכרן
# "[EN-AID] From top split: LEFT «ושמת את שתי האבנים על כתפת האפד אבני זכרן
# לבני ישראל» / RIGHT «ונשא אהרן את שמותם לפני יהוה על שתי כתפיו לזכרן».
# Derive claim from Hebrew arms, not English alone. Exod 28:12."
m.step("Exod.28.12")

# -------------------------- Exod.28.13 · TREE_CLAIM ------------------------
# ועשית משבצת
# "[EN-AID] From top split: LEFT «ועשית משבצת» / RIGHT «». Derive claim from
# Hebrew arms, not English alone. Exod 28:13."
m.step("Exod.28.13")

# -------------------------- Exod.28.14 · ETNACHTA_SPLIT --------------------
# ושתי שרשרת זהב טהור מגבלת תעשה אתם מעשה עבת … ונתתה את שרשרת העבתת על
# המשבצת
# "[EN-AID] From top split: LEFT «ושתי שרשרת זהב טהור מגבלת תעשה אתם מעשה
# עבת» / RIGHT «ונתתה את שרשרת העבתת על המשבצת». Derive claim from Hebrew
# arms, not English alone. Exod 28:14."
m.step("Exod.28.14")

# -------------------------- Exod.28.15 · ETNACHTA_SPLIT --------------------
# ועשית חשן משפט מעשה חשב כמעשה אפד תעשנו … זהב תכלת וארגמן ותולעת שני ושש
# משזר תעשה אתו
# "[EN-AID] From top split: LEFT «ועשית חשן משפט מעשה חשב כמעשה אפד תעשנו» /
# RIGHT «זהב תכלת וארגמן ותולעת שני ושש משזר תעשה אתו». Derive claim from
# Hebrew arms, not English alone. Exod 28:15."
m.step("Exod.28.15")

# -------------------------- Exod.28.16 · ETNACHTA_SPLIT --------------------
# רבוע יהיה כפול … זרת ארכו וזרת רחבו
# "[EN-AID] From top split: LEFT «רבוע יהיה כפול» / RIGHT «זרת ארכו וזרת
# רחבו». Derive claim from Hebrew arms, not English alone. Exod 28:16."
m.step("Exod.28.16")

# -------------------------- Exod.28.17 · ETNACHTA_SPLIT --------------------
# ומלאת בו מלאת אבן ארבעה טורים אבן … טור אדם פטדה וברקת הטור האחד
# "[EN-AID] From top split: LEFT «ומלאת בו מלאת אבן ארבעה טורים אבן» / RIGHT
# «טור אדם פטדה וברקת הטור האחד». Derive claim from Hebrew arms, not English
# alone. Exod 28:17."
m.step("Exod.28.17")

# -------------------------- Exod.28.18 · ETNACHTA_SPLIT --------------------
# והטור השני … נפך ספיר ויהלם
# "[EN-AID] From top split: LEFT «והטור השני» / RIGHT «נפך ספיר ויהלם».
# Derive claim from Hebrew arms, not English alone. Exod 28:18."
m.step("Exod.28.18")

# -------------------------- Exod.28.19 · ETNACHTA_SPLIT --------------------
# והטור השלישי … לשם שבו ואחלמה
# "[EN-AID] From top split: LEFT «והטור השלישי» / RIGHT «לשם שבו ואחלמה».
# Derive claim from Hebrew arms, not English alone. Exod 28:19."
m.step("Exod.28.19")

# -------------------------- Exod.28.20 · ETNACHTA_SPLIT --------------------
# והטור הרביעי תרשיש ושהם וישפה … משבצים זהב יהיו במלואתם
# "[EN-AID] From top split: LEFT «והטור הרביעי תרשיש ושהם וישפה» / RIGHT
# «משבצים זהב יהיו במלואתם». Derive claim from Hebrew arms, not English
# alone. Exod 28:20."
m.step("Exod.28.20")
# witness-tier presupposed read: shamir_engraving on stones_fullness — read,
# not installed
m.witness_read("stones_fullness", "shamir_engraving",
                cites=["Babylonian Talmud Sotah 48b", "Mishnah Pirkei Avot 5:6"])

# -------------------------- Exod.28.21 · ETNACHTA_SPLIT --------------------
# והאבנים תהיין על שמת בני ישראל שתים עשרה על שמתם … פתוחי חותם איש על שמו
# תהיין לשני עשר שבט
# "[EN-AID] From top split: LEFT «והאבנים תהיין על שמת בני ישראל שתים עשרה
# על שמתם» / RIGHT «פתוחי חותם איש על שמו תהיין לשני עשר שבט». Derive claim
# from Hebrew arms, not English alone. Exod 28:21."
m.step("Exod.28.21")

# -------------------------- Exod.28.22 · ETNACHTA_SPLIT --------------------
# ועשית על החשן שרשת גבלת מעשה עבת … זהב טהור
# "[EN-AID] From top split: LEFT «ועשית על החשן שרשת גבלת מעשה עבת» / RIGHT
# «זהב טהור». Derive claim from Hebrew arms, not English alone. Exod 28:22."
m.step("Exod.28.22")

# -------------------------- Exod.28.23 · ETNACHTA_SPLIT --------------------
# ועשית על החשן שתי טבעות זהב … ונתת את שתי הטבעות על שני קצות החשן
# "[EN-AID] From top split: LEFT «ועשית על החשן שתי טבעות זהב» / RIGHT «ונתת
# את שתי הטבעות על שני קצות החשן». Derive claim from Hebrew arms, not
# English alone. Exod 28:23."
m.step("Exod.28.23")

# -------------------------- Exod.28.24 · ETNACHTA_SPLIT --------------------
# ונתתה את שתי עבתת הזהב על שתי הטבעת … אל קצות החשן
# "[EN-AID] From top split: LEFT «ונתתה את שתי עבתת הזהב על שתי הטבעת» /
# RIGHT «אל קצות החשן». Derive claim from Hebrew arms, not English alone.
# Exod 28:24."
m.step("Exod.28.24")

# -------------------------- Exod.28.25 · ETNACHTA_SPLIT --------------------
# ואת שתי קצות שתי העבתת תתן על שתי המשבצות … ונתתה על כתפות האפד אל מול
# פניו
# "[EN-AID] From top split: LEFT «ואת שתי קצות שתי העבתת תתן על שתי המשבצות»
# / RIGHT «ונתתה על כתפות האפד אל מול פניו». Derive claim from Hebrew arms,
# not English alone. Exod 28:25."
m.step("Exod.28.25")

# -------------------------- Exod.28.26 · ETNACHTA_SPLIT --------------------
# ועשית שתי טבעות זהב ושמת אתם על שני קצות החשן … על שפתו אשר אל עבר האפד
# ביתה
# "[EN-AID] From top split: LEFT «ועשית שתי טבעות זהב ושמת אתם על שני קצות
# החשן» / RIGHT «על שפתו אשר אל עבר האפד ביתה». Derive claim from Hebrew
# arms, not English alone. Exod 28:26."
m.step("Exod.28.26")

# -------------------------- Exod.28.27 · ETNACHTA_SPLIT --------------------
# ועשית שתי טבעות זהב ונתתה אתם על שתי כתפות האפוד מלמטה ממול  … ממעל לחשב
# האפוד
# "[EN-AID] From top split: LEFT «ועשית שתי טבעות זהב ונתתה אתם על שתי כתפות
# האפוד מלמטה ממול פניו לעמת מחברתו» / RIGHT «ממעל לחשב האפוד». Derive claim
# from Hebrew arms, not English alone. Exod 28:27."
m.step("Exod.28.27")

# -------------------------- Exod.28.28 · ETNACHTA_SPLIT --------------------
# וירכסו את החשן מטבעתו מטבעתיו אל טבעת האפד בפתיל תכלת להיות  … ולא יזח
# החשן מעל האפוד
# "[EN-AID] From top split: LEFT «וירכסו את החשן מטבעתו מטבעתיו אל טבעת האפד
# בפתיל תכלת להיות על חשב האפוד» / RIGHT «ולא יזח החשן מעל האפוד». Derive
# claim from Hebrew arms, not English alone. Exod 28:28."
m.step("Exod.28.28")
# witness-tier presupposed read: standing_prohibitions on vestment_clauses —
# read, not installed
m.witness_read("vestment_clauses", "standing_prohibitions",
                cites=["Babylonian Talmud Yoma 72a", "Onkelos Exod 28"])

# -------------------------- Exod.28.29 · ETNACHTA_SPLIT --------------------
# ונשא אהרן את שמות בני ישראל בחשן המשפט על לבו בבאו אל הקדש … לזכרן לפני
# יהוה תמיד
# "[EN-AID] From top split: LEFT «ונשא אהרן את שמות בני ישראל בחשן המשפט על
# לבו בבאו אל הקדש» / RIGHT «לזכרן לפני יהוה תמיד». Derive claim from Hebrew
# arms, not English alone. Exod 28:29."
m.step("Exod.28.29")

# -------------------------- Exod.28.30 · ETNACHTA_SPLIT --------------------
# ונתת אל חשן המשפט את האורים ואת התמים והיו על לב אהרן בבאו ל … ונשא אהרן
# את משפט בני ישראל על לבו לפני יהוה תמיד
# "[EN-AID] From top split: LEFT «ונתת אל חשן המשפט את האורים ואת התמים והיו
# על לב אהרן בבאו לפני יהוה» / RIGHT «ונשא אהרן את משפט בני ישראל על לבו
# לפני יהוה תמיד». Derive claim from Hebrew arms, not English alone. Exod
# 28:30."
m.step("Exod.28.30")
# witness-tier presupposed read: judgment_organ on breastplate_clauses —
# read, not installed
m.witness_read("breastplate_clauses", "judgment_organ",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.31 · TREE_CLAIM ------------------------
# ועשית את מעיל האפוד … כליל תכלת
# "[EN-AID] From top split: LEFT «ועשית את מעיל האפוד» / RIGHT «כליל תכלת».
# Derive claim from Hebrew arms, not English alone. Exod 28:31."
m.step("Exod.28.31")

# -------------------------- Exod.28.32 · ETNACHTA_SPLIT --------------------
# והיה פי ראשו בתוכו … שפה יהיה לפיו סביב מעשה ארג כפי תחרא יהיה לו לא יקרע
# "[EN-AID] From top split: LEFT «והיה פי ראשו בתוכו» / RIGHT «שפה יהיה לפיו
# סביב מעשה ארג כפי תחרא יהיה לו לא יקרע». Derive claim from Hebrew arms,
# not English alone. Exod 28:32."
m.step("Exod.28.32")

# -------------------------- Exod.28.33 · ETNACHTA_SPLIT --------------------
# ועשית על שוליו רמני תכלת וארגמן ותולעת שני על שוליו סביב … ופעמני זהב
# בתוכם סביב
# "[EN-AID] From top split: LEFT «ועשית על שוליו רמני תכלת וארגמן ותולעת שני
# על שוליו סביב» / RIGHT «ופעמני זהב בתוכם סביב». Derive claim from Hebrew
# arms, not English alone. Exod 28:33."
m.step("Exod.28.33")

# -------------------------- Exod.28.34 · ETNACHTA_SPLIT --------------------
# פעמן זהב ורמון פעמן זהב ורמון … על שולי המעיל סביב
# "[EN-AID] From top split: LEFT «פעמן זהב ורמון פעמן זהב ורמון» / RIGHT «על
# שולי המעיל סביב». Derive claim from Hebrew arms, not English alone. Exod
# 28:34."
m.step("Exod.28.34")

# -------------------------- Exod.28.35 · ETNACHTA_SPLIT --------------------
# והיה על אהרן לשרת … ונשמע קולו בבאו אל הקדש לפני יהוה ובצאתו ולא ימות
# "[EN-AID] From top split: LEFT «והיה על אהרן לשרת» / RIGHT «ונשמע קולו
# בבאו אל הקדש לפני יהוה ובצאתו ולא ימות». Derive claim from Hebrew arms,
# not English alone. Exod 28:35."
m.step("Exod.28.35")
# witness-tier presupposed read: announced_entry on bells_clause — read, not
# installed
m.witness_read("bells_clause", "announced_entry",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.36 · ETNACHTA_SPLIT --------------------
# ועשית ציץ זהב טהור … ופתחת עליו פתוחי חתם קדש ליהוה
# "[EN-AID] From top split: LEFT «ועשית ציץ זהב טהור» / RIGHT «ופתחת עליו
# פתוחי חתם קדש ליהוה». Derive claim from Hebrew arms, not English alone.
# Exod 28:36."
m.step("Exod.28.36")

# -------------------------- Exod.28.37 · ETNACHTA_SPLIT --------------------
# ושמת אתו על פתיל תכלת והיה על המצנפת … אל מול פני המצנפת יהיה
# "[EN-AID] From top split: LEFT «ושמת אתו על פתיל תכלת והיה על המצנפת» /
# RIGHT «אל מול פני המצנפת יהיה». Derive claim from Hebrew arms, not English
# alone. Exod 28:37."
m.step("Exod.28.37")

# -------------------------- Exod.28.38 · ETNACHTA_SPLIT --------------------
# והיה על מצח אהרן ונשא אהרן את עון הקדשים אשר יקדישו בני ישרא … והיה על
# מצחו תמיד לרצון להם לפני יהוה
# "[EN-AID] From top split: LEFT «והיה על מצח אהרן ונשא אהרן את עון הקדשים
# אשר יקדישו בני ישראל לכל מתנת קדשיהם» / RIGHT «והיה על מצחו תמיד לרצון להם
# לפני יהוה». Derive claim from Hebrew arms, not English alone. Exod 28:38."
m.step("Exod.28.38")
# witness-tier presupposed read: written_acceptance on plate_clauses — read,
# not installed
m.witness_read("plate_clauses", "written_acceptance",
                cites=["Mishnah Zevachim 8:12", "Onkelos Exod 28"])
# witness-tier presupposed read: propitiation_scope on plate_function —
# read, not installed
m.witness_read("plate_function", "propitiation_scope",
                cites=["Mishnah Zevachim 8:12"])

# -------------------------- Exod.28.39 · ETNACHTA_SPLIT --------------------
# ושבצת הכתנת שש ועשית מצנפת שש … ואבנט תעשה מעשה רקם
# "[EN-AID] From top split: LEFT «ושבצת הכתנת שש ועשית מצנפת שש» / RIGHT
# «ואבנט תעשה מעשה רקם». Derive claim from Hebrew arms, not English alone.
# Exod 28:39."
m.step("Exod.28.39")

# -------------------------- Exod.28.40 · ETNACHTA_SPLIT --------------------
# ולבני אהרן תעשה כתנת ועשית להם אבנטים … ומגבעות תעשה להם לכבוד ולתפארת
# "[EN-AID] From top split: LEFT «ולבני אהרן תעשה כתנת ועשית להם אבנטים» /
# RIGHT «ומגבעות תעשה להם לכבוד ולתפארת». Derive claim from Hebrew arms, not
# English alone. Exod 28:40."
m.step("Exod.28.40")

# -------------------------- Exod.28.41 · ETNACHTA_SPLIT --------------------
# והלבשת אתם את אהרן אחיך ואת בניו אתו … ומשחת אתם ומלאת את ידם וקדשת אתם
# וכהנו לי
# "[EN-AID] From top split: LEFT «והלבשת אתם את אהרן אחיך ואת בניו אתו» /
# RIGHT «ומשחת אתם ומלאת את ידם וקדשת אתם וכהנו לי». Derive claim from
# Hebrew arms, not English alone. Exod 28:41."
m.step("Exod.28.41")

# -------------------------- Exod.28.42 · ETNACHTA_SPLIT --------------------
# ועשה להם מכנסי בד לכסות בשר ערוה … ממתנים ועד ירכים יהיו
# "[EN-AID] From top split: LEFT «ועשה להם מכנסי בד לכסות בשר ערוה» / RIGHT
# «ממתנים ועד ירכים יהיו». Derive claim from Hebrew arms, not English alone.
# Exod 28:42."
m.step("Exod.28.42")

# -------------------------- Exod.28.43 · ETNACHTA_SPLIT --------------------
# והיו על אהרן ועל בניו בבאם אל אהל מועד או בגשתם אל המזבח לשר … חקת עולם לו
# ולזרעו אחריו
# "[EN-AID] From top split: LEFT «והיו על אהרן ועל בניו בבאם אל אהל מועד או
# בגשתם אל המזבח לשרת בקדש ולא ישאו עון » / RIGHT «חקת עולם לו ולזרעו
# אחריו». Derive claim from Hebrew arms, not English alone. Exod 28:43."
m.step("Exod.28.43")
# witness-tier presupposed read: wear_or_die on closing_clause — read, not
# installed
m.witness_read("closing_clause", "wear_or_die",
                cites=["Onkelos Exod 28"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('priest_verb', 'service_before_me'), ('garment_purpose', 'honor_splendor_census'), ('garment_list', 'mirror_table'), ('oracle_protocol', 'access_list'), ('plural_take', 'fiscal_plurality'), ('stones_fullness', 'shamir_engraving'), ('vestment_clauses', 'standing_prohibitions'), ('breastplate_clauses', 'judgment_organ'), ('bells_clause', 'announced_entry'), ('plate_clauses', 'written_acceptance'), ('plate_function', 'propitiation_scope'), ('closing_clause', 'wear_or_die')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Exod 28']
    assert all('service_before_me' not in f for f in m.WORLD["facts"])
    assert 'priest_verb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Mishnah Yoma 7:5', 'Onkelos Exod 28']
    assert all('honor_splendor_census' not in f for f in m.WORLD["facts"])
    assert 'garment_purpose' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Midrash Tanchuma, Tetzaveh 1']
    assert all('mirror_table' not in f for f in m.WORLD["facts"])
    assert 'garment_list' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Mishnah Yoma 7:5']
    assert all('access_list' not in f for f in m.WORLD["facts"])
    assert 'oracle_protocol' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mishnah Shekalim 5:2']
    assert all('fiscal_plurality' not in f for f in m.WORLD["facts"])
    assert 'plural_take' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Babylonian Talmud Sotah 48b', 'Mishnah Pirkei Avot 5:6']
    assert all('shamir_engraving' not in f for f in m.WORLD["facts"])
    assert 'stones_fullness' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Babylonian Talmud Yoma 72a', 'Onkelos Exod 28']
    assert all('standing_prohibitions' not in f for f in m.WORLD["facts"])
    assert 'vestment_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Exod 28']
    assert all('judgment_organ' not in f for f in m.WORLD["facts"])
    assert 'breastplate_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Exod 28']
    assert all('announced_entry' not in f for f in m.WORLD["facts"])
    assert 'bells_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Mishnah Zevachim 8:12', 'Onkelos Exod 28']
    assert all('written_acceptance' not in f for f in m.WORLD["facts"])
    assert 'plate_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Mishnah Zevachim 8:12']
    assert all('propitiation_scope' not in f for f in m.WORLD["facts"])
    assert 'plate_function' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Onkelos Exod 28']
    assert all('wear_or_die' not in f for f in m.WORLD["facts"])
    assert 'closing_clause' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
