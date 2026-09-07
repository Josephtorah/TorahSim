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
# ‹ואתה הקרב אליך› (“and-you bring-near to-you/your”)
# ‹את אהרן אחיך› (“obj-marker Aaron brother-you/your”)
# ‹ואת בניו אתו› (“and-obj-marker son-him/its with-him/its”)
# ‹מתוך בני ישראל› (“from-midst son Israel”)
# ‹לכהנ … אהרן נדב› (“? … Aaron Nadab”)
# ‹ואביהוא אלעזר ואיתמר› (“and-Abihu Eleazar and-Ithamar”)
# ‹בני אהרן› (“son Aaron”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:1."
m.step("Exod.28.1")
# witness-tier presupposed read: service_before_me on priest_verb — read,
# not installed
m.witness_read("priest_verb", "service_before_me",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.2 · ETNACHTA_SPLIT ---------------------
# ‹ועשית בגדי קדש› (“and-make garment holiness”)
# ‹לאהרן אחיך … לכבוד› (“to-Aaron brother-you/your … to-weight”)
# ‹ולתפארת› (“and-to-ornament”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:2."
m.step("Exod.28.2")
# witness-tier presupposed read: honor_splendor_census on garment_purpose —
# read, not installed
m.witness_read("garment_purpose", "honor_splendor_census",
                cites=["Mishnah Yoma 7:5", "Onkelos Exod 28"])

# -------------------------- Exod.28.3 · ETNACHTA_SPLIT ---------------------
# ‹ואתה תדבר אל› (“and-you speak to”)
# ‹כל חכמי לב› (“all wise heart”)
# ‹אשר מלאתיו רוח› (“which fill-him/its spirit”)
# ‹חכמה … ועשו את› (“wisdom … and-make obj-marker”)
# ‹בגדי אהרן לקדשו› (“garment Aaron to-sanctify-him/its”)
# ‹לכהנו לי› (“to-officiate-as-a-priest-him/its to-me/my”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:3."
m.step("Exod.28.3")

# -------------------------- Exod.28.4 · ETNACHTA_SPLIT ---------------------
# ‹ואלה הבגדים אשר› (“and-these the-garment which”)
# ‹יעשו חשן ואפוד› (“make perhaps-a-pocket and-girdle”)
# ‹ומעיל וכתנת תשבץ› (“and-robe and-shirt checkered-stuff”)
# ‹מצנפת ואבנט … ועשו› (“tiara and-belt … and-make”)
# ‹בגדי קדש לאהרן› (“garment holiness to-Aaron”)
# ‹אחיך ולבניו לכהנו› (“brother-you/your and-to-son-him/its to-officiate-as-
# a-priest-him/its”)
# ‹לי› (“to-me/my”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:4."
m.step("Exod.28.4")
# witness-tier presupposed read: mirror_table on garment_list — read, not
# installed
m.witness_read("garment_list", "mirror_table",
                cites=["Midrash Tanchuma, Tetzaveh 1"])
# witness-tier presupposed read: access_list on oracle_protocol — read, not
# installed
m.witness_read("oracle_protocol", "access_list",
                cites=["Mishnah Yoma 7:5"])
# witness-tier presupposed read:
# the_runs_added_tokens_are_the_specs_parameters on
# the_spec_graded_against_its_run — read, not installed
m.witness_read("the_spec_graded_against_its_run", "the_runs_added_tokens_are_the_specs_parameters",
                cites=["Onkelos Exod 28:1 + 28:3 + 28:4 + 28:41", "Onkelos Exod 28:2 + 28:40", "Onkelos Exod 28:11 + 28:21 + 28:36", "Onkelos Exod 28:15 + 28:29-30", "Onkelos Exod 28:28 + 28:32", "Onkelos Exod 28:33-35", "Onkelos Exod 28:38", "Onkelos Exod 28:42-43", "Midrash Tanchuma, Tetzaveh 1", "Yoma 71b:6", "Yoma 71b:7", "Yoma 71b:10", "Yoma 71b:12", "Yoma 71b:13", "Yoma 71b:14", "Yoma 72a:1", "Yoma 72a:5", "Yoma 72a:6", "Yoma 72a:7", "Yoma 72a:8", "Yoma 72a:9", "Yoma 72b:3", "Yoma 7b:4", "Yoma 7b:5", "Yoma 44b:16", "Yoma 5b:4", "Zevachim 88b:2", "Zevachim 88b:3", "Zevachim 88b:5", "Zevachim 88b:6", "Zevachim 88b:7", "Zevachim 88b:8", "Arakhin 16a:13", "Arakhin 16a:16", "Zevachim 26a:21", "Zevachim 95a:4", "Zevachim 119b:18", "Sanhedrin 83b:13", "Sanhedrin 83b:14", "Sotah 36a:12", "Bava Batra 8b:9", "Megillah 12a:7", "Megillah 12b:10", "Shabbat 31a:7", "Gittin 20b:1", "Makkot 22a:8", "Menachot 25a:2", "Menachot 11a:5", "Menachot 42b:13", "Chullin 138a:6", "Sotah 9b:22", "Yevamot 60b:13", "Shabbat 12a:4", "Mishnah Yoma 7:5", "Mishnah Yoma 7:3", "Mishnah Yoma 7:4", "Mishnah Yoma 7:1", "Mishnah Yoma 3:4", "Mishnah Yoma 3:7", "Mishnah Yoma 1:1", "Mishnah Zevachim 2:1", "Mishnah Zevachim 8:12", "Mishnah Horayot 3:4", "Mishnah Horayot 3:5", "Mishnah Megillah 1:9", "Mishnah Sotah 9:12", "Mishnah Sanhedrin 2:1", "Mishnah Tamid 5:3", "Mishnah Shekalim 5:1", "Mishnah Shekalim 5:2", "Mishnah Middot 1:4", "Mishnah Kelim 1:9", "Mishnah Shabbat 6:9"])

# -------------------------- Exod.28.5 · ETNACHTA_SPLIT ---------------------
# ‹והם יקחו את› (“and-they take obj-marker”)
# ‹הזהב ואת התכלת› (“the-gold and-obj-marker the-cerulean-mussel”)
# ‹ואת הארגמן … ואת› (“and-obj-marker the-purple … and-obj-marker”)
# ‹תולעת השני ואת› (“crimson-grub the-crimson and-obj-marker”)
# ‹השש› (“the-bleached-stuff”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:5."
m.step("Exod.28.5")
# witness-tier presupposed read: fiscal_plurality on plural_take — read, not
# installed
m.witness_read("plural_take", "fiscal_plurality",
                cites=["Mishnah Shekalim 5:2"])

# -------------------------- Exod.28.6 · ETNACHTA_SPLIT ---------------------
# ‹ועשו את האפד› (“and-make obj-marker the-girdle”)
# ‹… זהב תכלת וארגמן› (“gold cerulean-mussel and-purple”)
# ‹תולעת שני ושש› (“crimson-grub crimson and-bleached-stuff”)
# ‹משזר מעשה חשב› (“twist deed/work plait”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:6."
m.step("Exod.28.6")

# -------------------------- Exod.28.7 · TREE_CLAIM -------------------------
# ‹שתי כתפת חברת› (“two shoulder join”)
# ‹יהיה לו אל› (“be to-him/its to”)
# ‹שני קצותיו› (“two termination-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms, not English alone. Exod 28:7."
m.step("Exod.28.7")

# -------------------------- Exod.28.8 · ETNACHTA_SPLIT ---------------------
# ‹וחשב אפדתו אשר› (“and-belt girding-on-him/its which”)
# ‹עליו כמעשהו ממנו› (“over-him/its like-deed/work-him/its from-us/our”)
# ‹יהיה … זהב תכלת› (“be … gold cerulean-mussel”)
# ‹וארגמן ותולעת שני› (“and-purple and-crimson-grub crimson”)
# ‹ושש משזר› (“and-bleached-stuff twist”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:8."
m.step("Exod.28.8")

# -------------------------- Exod.28.9 · ETNACHTA_SPLIT ---------------------
# ‹ולקחת את שתי› (“and-take obj-marker two”)
# ‹אבני שהם … ופתחת› (“stone gem … and-open-wide”)
# ‹עליהם שמות בני› (“over-them/their name son”)
# ‹ישראל› (“Israel”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:9."
m.step("Exod.28.9")

# -------------------------- Exod.28.10 · ETNACHTA_SPLIT --------------------
# ‹ששה משמתם על› (“six from-name-them/their over”)
# ‹האבן האחת … ואת› (“the-stone the-one … and-obj-marker”)
# ‹שמות הששה הנותרים› (“name the-six the-jut-over”)
# ‹על האבן השנית› (“over the-stone the-second”)
# ‹כתולדתם› (“like-generations-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:10."
m.step("Exod.28.10")
# witness-tier presupposed read: the_vestments_form_file on stones_and_form
# — read, not installed
m.witness_read("stones_and_form", "the_vestments_form_file",
                cites=["Sotah 36a:11", "Sotah 36a:12", "Sotah 36a:13", "Yoma 72b:2", "Yoma 72b:3", "Arakhin 3b:13", "Arakhin 3b:14", "Zevachim 19a:25", "Zevachim 19a:26", "Yoma 44b:15", "Yoma 44b:16", "Zevachim 119b:18"])

# -------------------------- Exod.28.11 · ETNACHTA_SPLIT --------------------
# ‹מעשה חרש אבן› (“deed/work fabricator stone”)
# ‹פתוחי חתם תפתח› (“sculpture signature-ring open-wide”)
# ‹את שתי האבנים› (“obj-marker two the-stone”)
# ‹על שמת בני› (“over name son”)
# ‹ישראל … מסבת משבצות› (“Israel … reversal brocade”)
# ‹זהב תעשה אתם› (“gold make obj-marker-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:11."
m.step("Exod.28.11")

# -------------------------- Exod.28.12 · ETNACHTA_SPLIT --------------------
# ‹ושמת את שתי› (“and-put/set obj-marker two”)
# ‹האבנים על כתפת› (“the-stone over shoulder”)
# ‹האפד אבני זכרן› (“the-girdle stone memento”)
# ‹לבני ישראל … ונשא› (“to-son Israel … and-lift/carry”)
# ‹אהרן את שמותם› (“Aaron obj-marker name-them/their”)
# ‹לפני יהוה על› (“to-face YHWH over”)
# ‹שתי כתפיו לזכרן› (“two shoulder-him/its to-memento”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:12."
m.step("Exod.28.12")

# -------------------------- Exod.28.13 · TREE_CLAIM ------------------------
# ‹ועשית משבצת› (“and-make brocade”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «». Derive claim from Hebrew
# arms, not English alone. Exod 28:13."
m.step("Exod.28.13")

# -------------------------- Exod.28.14 · ETNACHTA_SPLIT --------------------
# ‹ושתי שרשרת זהב› (“and-two chain gold”)
# ‹טהור מגבלת תעשה› (“pure border make”)
# ‹אתם מעשה עבת› (“obj-marker-them/their deed/work something-intwined”)
# ‹… ונתתה את שרשרת› (“and-set obj-marker chain”)
# ‹העבתת על המשבצת› (“the-something-intwined over the-brocade”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:14."
m.step("Exod.28.14")

# -------------------------- Exod.28.15 · ETNACHTA_SPLIT --------------------
# ‹ועשית חשן משפט› (“and-make perhaps-a-pocket judgment”)
# ‹מעשה חשב כמעשה› (“deed/work plait like-deed/work”)
# ‹אפד תעשנו … זהב› (“girdle make-him/its … gold”)
# ‹תכלת וארגמן ותולעת› (“cerulean-mussel and-purple and-crimson-grub”)
# ‹שני ושש משזר› (“crimson and-bleached-stuff twist”)
# ‹תעשה אתו› (“make obj-marker-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:15."
m.step("Exod.28.15")

# -------------------------- Exod.28.16 · ETNACHTA_SPLIT --------------------
# ‹רבוע יהיה כפול› (“be-quadrate be fold-together”)
# ‹… זרת ארכו וזרת› (“spread-of-the-fingers length-him/its and-spread-of-
# the-fingers”)
# ‹רחבו› (“width-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:16."
m.step("Exod.28.16")

# -------------------------- Exod.28.17 · ETNACHTA_SPLIT --------------------
# ‹ומלאת בו מלאת› (“and-fill in-him/its filling”)
# ‹אבן ארבעה טורים› (“stone four row”)
# ‹אבן … טור אדם› (“stone … row redness”)
# ‹פטדה וברקת הטור› (“gem and-gem the-row”)
# ‹האחד› (“the-one”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:17."
m.step("Exod.28.17")

# -------------------------- Exod.28.18 · ETNACHTA_SPLIT --------------------
# ‹והטור השני … נפך› (“and-the-row the-second … shining”)
# ‹ספיר ויהלם› (“gem and-precious-stone”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:18."
m.step("Exod.28.18")

# -------------------------- Exod.28.19 · ETNACHTA_SPLIT --------------------
# ‹והטור השלישי … לשם› (“and-the-row the-third … gem”)
# ‹שבו ואחלמה› (“gem and-gem”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:19."
m.step("Exod.28.19")

# -------------------------- Exod.28.20 · ETNACHTA_SPLIT --------------------
# ‹והטור הרביעי תרשיש› (“and-the-row the-fourth gem”)
# ‹ושהם וישפה … משבצים› (“and-gem and-gem-supposed-to-be-jasper …
# interweave-threads-in-squar”)
# ‹זהב יהיו במלואתם› (“gold be in-filling-them/their”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:20."
m.step("Exod.28.20")
# witness-tier presupposed read: shamir_engraving on stones_fullness — read,
# not installed
m.witness_read("stones_fullness", "shamir_engraving",
                cites=["Babylonian Talmud Sotah 48b", "Mishnah Pirkei Avot 5:6"])

# -------------------------- Exod.28.21 · ETNACHTA_SPLIT --------------------
# ‹והאבנים תהיין על› (“and-the-stone be over”)
# ‹שמת בני ישראל› (“name son Israel”)
# ‹שתים עשרה על› (“two -teen over”)
# ‹שמתם … פתוחי חותם› (“name-them/their … sculpture signature-ring”)
# ‹איש על שמו› (“man over name-him/its”)
# ‹תהיין לשני עשר› (“be to-two -teen”)
# ‹שבט› (“scion”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:21."
m.step("Exod.28.21")

# -------------------------- Exod.28.22 · ETNACHTA_SPLIT --------------------
# ‹ועשית על החשן› (“and-make over the-perhaps-a-pocket”)
# ‹שרשת גבלת מעשה› (“chain twisted-chain deed/work”)
# ‹עבת … זהב טהור› (“something-intwined … gold pure”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:22."
m.step("Exod.28.22")

# -------------------------- Exod.28.23 · ETNACHTA_SPLIT --------------------
# ‹ועשית על החשן› (“and-make over the-perhaps-a-pocket”)
# ‹שתי טבעות זהב› (“two seal gold”)
# ‹… ונתת את שתי› (“and-set obj-marker two”)
# ‹הטבעות על שני› (“the-seal over two”)
# ‹קצות החשן› (“termination the-perhaps-a-pocket”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:23."
m.step("Exod.28.23")

# -------------------------- Exod.28.24 · ETNACHTA_SPLIT --------------------
# ‹ונתתה את שתי› (“and-set obj-marker two”)
# ‹עבתת הזהב על› (“something-intwined the-gold over”)
# ‹שתי הטבעת … אל› (“two the-seal … to”)
# ‹קצות החשן› (“termination the-perhaps-a-pocket”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:24."
m.step("Exod.28.24")

# -------------------------- Exod.28.25 · ETNACHTA_SPLIT --------------------
# ‹ואת שתי קצות› (“and-obj-marker two termination”)
# ‹שתי העבתת תתן› (“two the-something-intwined set”)
# ‹על שתי המשבצות› (“over two the-brocade”)
# ‹… ונתתה על כתפות› (“and-set over shoulder”)
# ‹האפד אל מול› (“the-girdle to abrupt”)
# ‹פניו› (“face-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:25."
m.step("Exod.28.25")

# -------------------------- Exod.28.26 · ETNACHTA_SPLIT --------------------
# ‹ועשית שתי טבעות› (“and-make two seal”)
# ‹זהב ושמת אתם› (“gold and-put/set obj-marker-them/their”)
# ‹על שני קצות› (“over two termination”)
# ‹החשן … על שפתו› (“the-perhaps-a-pocket … over lip-him/its”)
# ‹אשר אל עבר› (“which to region-across”)
# ‹האפד ביתה› (“the-girdle house-ward”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:26."
m.step("Exod.28.26")

# -------------------------- Exod.28.27 · ETNACHTA_SPLIT --------------------
# ‹ועשית שתי טבעות› (“and-make two seal”)
# ‹זהב ונתתה אתם› (“gold and-set obj-marker-them/their”)
# ‹על שתי כתפות› (“over two shoulder”)
# ‹האפוד מלמטה ממול› (“the-girdle from-to-downward from-abrupt”)
# ‹… ממעל לחשב האפוד› (“from-upper-part to-belt the-girdle”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:27."
m.step("Exod.28.27")

# -------------------------- Exod.28.28 · ETNACHTA_SPLIT --------------------
# ‹וירכסו את החשן› (“and-tie obj-marker the-perhaps-a-pocket”)
# ‹מטבעתו מטבעתיו אל› (“from-seal-him/its from-seal-him/its to”)
# ‹טבעת האפד בפתיל› (“seal the-girdle in-twine”)
# ‹תכלת להיות … ולא› (“cerulean-mussel to-be … and-not”)
# ‹יזח החשן מעל› (“shove the-perhaps-a-pocket from-over”)
# ‹האפוד› (“the-girdle”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:28."
m.step("Exod.28.28")
# witness-tier presupposed read: standing_prohibitions on vestment_clauses —
# read, not installed
m.witness_read("vestment_clauses", "standing_prohibitions",
                cites=["Babylonian Talmud Yoma 72a", "Onkelos Exod 28"])

# -------------------------- Exod.28.29 · ETNACHTA_SPLIT --------------------
# ‹ונשא אהרן את› (“and-lift/carry Aaron obj-marker”)
# ‹שמות בני ישראל› (“name son Israel”)
# ‹בחשן המשפט על› (“in-perhaps-a-pocket the-judgment over”)
# ‹לבו בבאו אל› (“heart-him/its in-come/bring-him/its to”)
# ‹הקדש … לזכרן לפני› (“the-holiness … to-memento to-face”)
# ‹יהוה תמיד› (“YHWH continuance”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:29."
m.step("Exod.28.29")

# -------------------------- Exod.28.30 · ETNACHTA_SPLIT --------------------
# ‹ונתת אל חשן› (“and-set to perhaps-a-pocket”)
# ‹המשפט את האורים› (“the-judgment obj-marker the-Urim”)
# ‹ואת התמים והיו› (“and-obj-marker the-perfections and-be”)
# ‹על לב אהרן› (“over heart Aaron”)
# ‹בבאו ל … ונשא› (“in-come/bring-him/its ? … and-lift/carry”)
# ‹אהרן את משפט› (“Aaron obj-marker judgment”)
# ‹בני ישראל על› (“son Israel over”)
# ‹לבו לפני יהוה› (“heart-him/its to-face YHWH”)
# ‹תמיד› (“continuance”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:30."
m.step("Exod.28.30")
# witness-tier presupposed read: judgment_organ on breastplate_clauses —
# read, not installed
m.witness_read("breastplate_clauses", "judgment_organ",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.31 · TREE_CLAIM ------------------------
# ‹ועשית את מעיל› (“and-make obj-marker robe”)
# ‹האפוד … כליל תכלת› (“the-girdle … complete cerulean-mussel”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:31."
m.step("Exod.28.31")

# -------------------------- Exod.28.32 · ETNACHTA_SPLIT --------------------
# ‹והיה פי ראשו› (“and-be mouth head-him/its”)
# ‹בתוכו … שפה יהיה› (“in-midst-him/its … lip be”)
# ‹לפיו סביב מעשה› (“to-mouth-him/its circle deed/work”)
# ‹ארג כפי תחרא› (“plait like-mouth linen-corslet”)
# ‹יהיה לו לא› (“be to-him/its not”)
# ‹יקרע› (“rend”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:32."
m.step("Exod.28.32")

# -------------------------- Exod.28.33 · ETNACHTA_SPLIT --------------------
# ‹ועשית על שוליו› (“and-make over skirt-him/its”)
# ‹רמני תכלת וארגמן› (“pomegranate cerulean-mussel and-purple”)
# ‹ותולעת שני על› (“and-crimson-grub crimson over”)
# ‹שוליו סביב … ופעמני› (“skirt-him/its circle … and-bell”)
# ‹זהב בתוכם סביב› (“gold in-midst-them/their circle”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:33."
m.step("Exod.28.33")

# -------------------------- Exod.28.34 · ETNACHTA_SPLIT --------------------
# ‹פעמן זהב ורמון› (“bell gold and-pomegranate”)
# ‹פעמן זהב ורמון› (“bell gold and-pomegranate”)
# ‹… על שולי המעיל› (“over skirt the-robe”)
# ‹סביב› (“circle”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:34."
m.step("Exod.28.34")

# -------------------------- Exod.28.35 · ETNACHTA_SPLIT --------------------
# ‹והיה על אהרן› (“and-be over Aaron”)
# ‹לשרת … ונשמע קולו› (“to-attend-as-a-menial … and-hear voice/sound-
# him/its”)
# ‹בבאו אל הקדש› (“in-come/bring-him/its to the-holiness”)
# ‹לפני יהוה ובצאתו› (“to-face YHWH and-in-bring-forth-him/its”)
# ‹ולא ימות› (“and-not die”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:35."
m.step("Exod.28.35")
# witness-tier presupposed read: announced_entry on bells_clause — read, not
# installed
m.witness_read("bells_clause", "announced_entry",
                cites=["Onkelos Exod 28"])

# -------------------------- Exod.28.36 · ETNACHTA_SPLIT --------------------
# ‹ועשית ציץ זהב› (“and-make glistening gold”)
# ‹טהור … ופתחת עליו› (“pure … and-open-wide over-him/its”)
# ‹פתוחי חתם קדש› (“sculpture signature-ring holiness”)
# ‹ליהוה› (“to-YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:36."
m.step("Exod.28.36")

# -------------------------- Exod.28.37 · ETNACHTA_SPLIT --------------------
# ‹ושמת אתו על› (“and-put/set obj-marker-him/its over”)
# ‹פתיל תכלת והיה› (“twine cerulean-mussel and-be”)
# ‹על המצנפת … אל› (“over the-tiara … to”)
# ‹מול פני המצנפת› (“abrupt face the-tiara”)
# ‹יהיה› (“be”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:37."
m.step("Exod.28.37")

# -------------------------- Exod.28.38 · ETNACHTA_SPLIT --------------------
# ‹והיה על מצח› (“and-be over forehead”)
# ‹אהרן ונשא אהרן› (“Aaron and-lift/carry Aaron”)
# ‹את עון הקדשים› (“obj-marker perversity the-holiness”)
# ‹אשר יקדישו בני› (“which sanctify son”)
# ‹ישרא … והיה על› (“? … and-be over”)
# ‹מצחו תמיד לרצון› (“forehead-him/its continuance to-delight”)
# ‹להם לפני יהוה› (“to-them/their to-face YHWH”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:38."
m.step("Exod.28.38")
# witness-tier presupposed read: written_acceptance on plate_clauses — read,
# not installed
m.witness_read("plate_clauses", "written_acceptance",
                cites=["Mishnah Zevachim 8:12", "Onkelos Exod 28"])
# witness-tier presupposed read: propitiation_scope on plate_function —
# read, not installed
m.witness_read("plate_function", "propitiation_scope",
                cites=["Mishnah Zevachim 8:12"])
# witness-tier presupposed read: the_frontplates_state_machine on
# plate_clauses — read, not installed
m.witness_read("plate_clauses", "the_frontplates_state_machine",
                cites=["Yoma 7b:3", "Yoma 7b:4", "Yoma 7b:5", "Pesachim 77a:11", "Pesachim 77a:12", "Pesachim 77a:13", "Yevamot 60b:13", "Shabbat 12a:4"])

# -------------------------- Exod.28.39 · ETNACHTA_SPLIT --------------------
# ‹ושבצת הכתנת שש› (“and-interweave-threads-in-squar the-shirt bleached-
# stuff”)
# ‹ועשית מצנפת שש› (“and-make tiara bleached-stuff”)
# ‹… ואבנט תעשה מעשה› (“and-belt make deed/work”)
# ‹רקם› (“variegate-color”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:39."
m.step("Exod.28.39")

# -------------------------- Exod.28.40 · ETNACHTA_SPLIT --------------------
# ‹ולבני אהרן תעשה› (“and-to-son Aaron make”)
# ‹כתנת ועשית להם› (“shirt and-make to-them/their”)
# ‹אבנטים … ומגבעות תעשה› (“belt … and-cap make”)
# ‹להם לכבוד ולתפארת› (“to-them/their to-weight and-to-ornament”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:40."
m.step("Exod.28.40")

# -------------------------- Exod.28.41 · ETNACHTA_SPLIT --------------------
# ‹והלבשת אתם את› (“and-wrap-around obj-marker-them/their obj-marker”)
# ‹אהרן אחיך ואת› (“Aaron brother-you/your and-obj-marker”)
# ‹בניו אתו … ומשחת› (“son-him/its with-him/its … and-rub-with-oil”)
# ‹אתם ומלאת את› (“obj-marker-them/their and-fill obj-marker”)
# ‹ידם וקדשת אתם› (“hand-them/their and-sanctify obj-marker-them/their”)
# ‹וכהנו לי› (“and-officiate-as-a-priest to-me/my”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:41."
m.step("Exod.28.41")

# -------------------------- Exod.28.42 · ETNACHTA_SPLIT --------------------
# ‹ועשה להם מכנסי› (“and-make to-them/their drawers”)
# ‹בד לכסות בשר› (“flaxen-thread to-plump flesh”)
# ‹ערוה … ממתנים ועד› (“nudity … from-waist and-until”)
# ‹ירכים יהיו› (“thigh be”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:42."
m.step("Exod.28.42")

# -------------------------- Exod.28.43 · ETNACHTA_SPLIT --------------------
# ‹והיו על אהרן› (“and-be over Aaron”)
# ‹ועל בניו בבאם› (“and-over son-him/its in-come/bring-them/their”)
# ‹אל אהל מועד› (“to tent seasons”)
# ‹או בגשתם אל› (“or in-be-them/their to”)
# ‹המזבח לשר … חקת› (“the-altar to-officer … statute”)
# ‹עולם לו ולזרעו› (“forever to-him/its and-to-seed-him/its”)
# ‹אחריו› (“after-him/its”)
# "[EN-AID] From top split: LEFT «…» / RIGHT «…». Derive claim from Hebrew
# arms, not English alone. Exod 28:43."
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('priest_verb', 'service_before_me'), ('garment_purpose', 'honor_splendor_census'), ('garment_list', 'mirror_table'), ('oracle_protocol', 'access_list'), ('the_spec_graded_against_its_run', 'the_runs_added_tokens_are_the_specs_parameters'), ('plural_take', 'fiscal_plurality'), ('stones_and_form', 'the_vestments_form_file'), ('stones_fullness', 'shamir_engraving'), ('vestment_clauses', 'standing_prohibitions'), ('breastplate_clauses', 'judgment_organ'), ('bells_clause', 'announced_entry'), ('plate_clauses', 'written_acceptance'), ('plate_function', 'propitiation_scope'), ('plate_clauses', 'the_frontplates_state_machine'), ('closing_clause', 'wear_or_die')]
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
    assert m.WITNESS_READS[4]["cites"] == ['Onkelos Exod 28:1 + 28:3 + 28:4 + 28:41', 'Onkelos Exod 28:2 + 28:40', 'Onkelos Exod 28:11 + 28:21 + 28:36', 'Onkelos Exod 28:15 + 28:29-30', 'Onkelos Exod 28:28 + 28:32', 'Onkelos Exod 28:33-35', 'Onkelos Exod 28:38', 'Onkelos Exod 28:42-43', 'Midrash Tanchuma, Tetzaveh 1', 'Yoma 71b:6', 'Yoma 71b:7', 'Yoma 71b:10', 'Yoma 71b:12', 'Yoma 71b:13', 'Yoma 71b:14', 'Yoma 72a:1', 'Yoma 72a:5', 'Yoma 72a:6', 'Yoma 72a:7', 'Yoma 72a:8', 'Yoma 72a:9', 'Yoma 72b:3', 'Yoma 7b:4', 'Yoma 7b:5', 'Yoma 44b:16', 'Yoma 5b:4', 'Zevachim 88b:2', 'Zevachim 88b:3', 'Zevachim 88b:5', 'Zevachim 88b:6', 'Zevachim 88b:7', 'Zevachim 88b:8', 'Arakhin 16a:13', 'Arakhin 16a:16', 'Zevachim 26a:21', 'Zevachim 95a:4', 'Zevachim 119b:18', 'Sanhedrin 83b:13', 'Sanhedrin 83b:14', 'Sotah 36a:12', 'Bava Batra 8b:9', 'Megillah 12a:7', 'Megillah 12b:10', 'Shabbat 31a:7', 'Gittin 20b:1', 'Makkot 22a:8', 'Menachot 25a:2', 'Menachot 11a:5', 'Menachot 42b:13', 'Chullin 138a:6', 'Sotah 9b:22', 'Yevamot 60b:13', 'Shabbat 12a:4', 'Mishnah Yoma 7:5', 'Mishnah Yoma 7:3', 'Mishnah Yoma 7:4', 'Mishnah Yoma 7:1', 'Mishnah Yoma 3:4', 'Mishnah Yoma 3:7', 'Mishnah Yoma 1:1', 'Mishnah Zevachim 2:1', 'Mishnah Zevachim 8:12', 'Mishnah Horayot 3:4', 'Mishnah Horayot 3:5', 'Mishnah Megillah 1:9', 'Mishnah Sotah 9:12', 'Mishnah Sanhedrin 2:1', 'Mishnah Tamid 5:3', 'Mishnah Shekalim 5:1', 'Mishnah Shekalim 5:2', 'Mishnah Middot 1:4', 'Mishnah Kelim 1:9', 'Mishnah Shabbat 6:9']
    assert all('the_runs_added_tokens_are_the_specs_parameters' not in f for f in m.WORLD["facts"])
    assert 'the_spec_graded_against_its_run' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Shekalim 5:2']
    assert all('fiscal_plurality' not in f for f in m.WORLD["facts"])
    assert 'plural_take' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sotah 36a:11', 'Sotah 36a:12', 'Sotah 36a:13', 'Yoma 72b:2', 'Yoma 72b:3', 'Arakhin 3b:13', 'Arakhin 3b:14', 'Zevachim 19a:25', 'Zevachim 19a:26', 'Yoma 44b:15', 'Yoma 44b:16', 'Zevachim 119b:18']
    assert all('the_vestments_form_file' not in f for f in m.WORLD["facts"])
    assert 'stones_and_form' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Babylonian Talmud Sotah 48b', 'Mishnah Pirkei Avot 5:6']
    assert all('shamir_engraving' not in f for f in m.WORLD["facts"])
    assert 'stones_fullness' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Babylonian Talmud Yoma 72a', 'Onkelos Exod 28']
    assert all('standing_prohibitions' not in f for f in m.WORLD["facts"])
    assert 'vestment_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Exod 28']
    assert all('judgment_organ' not in f for f in m.WORLD["facts"])
    assert 'breastplate_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Exod 28']
    assert all('announced_entry' not in f for f in m.WORLD["facts"])
    assert 'bells_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Mishnah Zevachim 8:12', 'Onkelos Exod 28']
    assert all('written_acceptance' not in f for f in m.WORLD["facts"])
    assert 'plate_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Mishnah Zevachim 8:12']
    assert all('propitiation_scope' not in f for f in m.WORLD["facts"])
    assert 'plate_function' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Yoma 7b:3', 'Yoma 7b:4', 'Yoma 7b:5', 'Pesachim 77a:11', 'Pesachim 77a:12', 'Pesachim 77a:13', 'Yevamot 60b:13', 'Shabbat 12a:4']
    assert all('the_frontplates_state_machine' not in f for f in m.WORLD["facts"])
    assert 'plate_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Onkelos Exod 28']
    assert all('wear_or_die' not in f for f in m.WORLD["facts"])
    assert 'closing_clause' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
