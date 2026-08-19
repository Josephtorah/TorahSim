#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_18_jethro_and_the_judges — 18:1-27
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_18_jethro_and_the_judges.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Jethro and the judges (18:1-27)"""
from machine import Machine

m = Machine("exo_18_jethro_and_the_judges")

# -------------------------- Exod.18.1 · JETHRO_HEARS -----------------------
# וַיִּשְׁמַע יִתְרוֹ כֹהֵן מִדְיָן חֹתֵן מֹשֶׁה אֵת כָּל־אֲשֶׁר עָשָׂה
# אֱלֹהִים לְמֹשֶׁה וּלְיִשְׂרָאֵל עַמּוֹ כִּי־הוֹצִיא יְהוָה אֶת־יִשְׂרָאֵל
# מִמִּצְרָיִם
# "[EN-AID] And Jethro, priest of Midian, Moses' father-in-law, heard all
# that God had done for Moses and for Israel His people — that the LORD had
# brought Israel out from Egypt."
m.step("Exod.18.1")
# ‹וַיִּשְׁמַע יִתְרוֹ כֹהֵן מִדְיָן חֹתֵן מֹשֶׁה› (“and-hear Jethro priest
# Midian give-away-in-marriage Moses”) — fact holds: and-hear-Jethro
m.fact("va_yishma_yitro")

# -------------------------- Exod.18.2 · AFTER_HER_SENDING ------------------
# וַיִּקַּח יִתְרוֹ חֹתֵן מֹשֶׁה אֶת־צִפֹּרָה אֵשֶׁת מֹשֶׁה אַחַר
# שִׁלּוּחֶיהָ
# "[EN-AID] And Jethro, Moses' father-in-law, took Zipporah, Moses' wife —
# after her being sent away."
m.step("Exod.18.2")
# ‹אֶת־צִפֹּרָה אֵשֶׁת מֹשֶׁה אַחַר שִׁלּוּחֶיהָ› (“obj-marker Zipporah
# woman Moses after dismissal-her/its”) — fact holds: after-shilucheha
m.fact("achar_shilucheha")

# -------------------------- Exod.18.3 · GERSHOM ----------------------------
# וְאֵת שְׁנֵי בָנֶיהָ אֲשֶׁר שֵׁם הָאֶחָד גֵּרְשֹׁם כִּי אָמַר גֵּר
# הָיִיתִי בְּאֶרֶץ נָכְרִיָּה
# "[EN-AID] And her two sons — of whom the name of the one was Gershom, for
# he said: A stranger have I been in a foreign land."
m.step("Exod.18.3")
# ‹הָאֶחָד גֵּרְשֹׁם כִּי אָמַר גֵּר הָיִיתִי בְּאֶרֶץ נָכְרִיָּה› (“the-one
# Gershom that say sojourner be in-earth strange”) — fact holds: sojourner-
# be-in-earth-strange
m.fact("ger_hayiti_be_eretz_nakhriya")

# -------------------------- Exod.18.4 · ELIEZER ----------------------------
# וְשֵׁם הָאֶחָד אֱלִיעֶזֶר כִּי־אֱלֹהֵי אָבִי בְּעֶזְרִי וַיַּצִּלֵנִי
# מֵחֶרֶב פַּרְעֹה
# "[EN-AID] And the name of the one was Eliezer — for the God of my father
# was my help, and delivered me from the sword of Pharaoh."
m.step("Exod.18.4")
# ‹כִּי־אֱלֹהֵי אָבִי בְּעֶזְרִי וַיַּצִּלֵנִי מֵחֶרֶב פַּרְעֹה› (“that God
# father-me/my in-aid-me/my and-snatch-away-me/my from-drought Pharaoh”) —
# fact holds: God-avi-in-ezri
m.fact("elohe_avi_be_ezri")

# -------------------------- Exod.18.5 · TO_THE_MOUNT_OF_GOD ----------------
# וַיָּבֹא יִתְרוֹ חֹתֵן מֹשֶׁה וּבָנָיו וְאִשְׁתּוֹ אֶל־מֹשֶׁה
# אֶל־הַמִּדְבָּר אֲשֶׁר־הוּא חֹנֶה שָׁם הַר הָאֱלֹהִים
# "[EN-AID] And Jethro, Moses' father-in-law, came, and his sons and his
# wife, to Moses — to the wilderness where he was camping, the mount of
# God."
m.step("Exod.18.5")
# ‹אֶל־הַמִּדְבָּר אֲשֶׁר־הוּא חֹנֶה שָׁם הַר הָאֱלֹהִים› (“to the-pasture
# which he/it encamp there mountain the-God”) — fact holds: to-mountain-the-
# God
m.fact("el_har_ha_elohim")

# -------------------------- Exod.18.6 · I_YOUR_FATHER_IN_LAW ---------------
# וַיֹּאמֶר אֶל־מֹשֶׁה אֲנִי חֹתֶנְךָ יִתְרוֹ בָּא אֵלֶיךָ וְאִשְׁתְּךָ
# וּשְׁנֵי בָנֶיהָ עִמָּהּ
# "[EN-AID] And he said to Moses: I, your father-in-law Jethro, am coming to
# you — and your wife, and her two sons with her."
m.step("Exod.18.6")
# ‹אֲנִי חֹתֶנְךָ יִתְרוֹ בָּא אֵלֶיךָ› (“give-away-in-marriage-you/your
# Jethro come/bring to-you/your”) — fact holds: ani-chotenkha-come/bring-to-
# you
m.fact("ani_chotenkha_ba_elekha")

# -------------------------- Exod.18.7 · THE_GREETING -----------------------
# וַיֵּצֵא מֹשֶׁה לִקְרַאת חֹתְנוֹ וַיִּשְׁתַּחוּ וַיִּשַּׁק־לוֹ
# וַיִּשְׁאֲלוּ אִישׁ־לְרֵעֵהוּ לְשָׁלוֹם וַיָּבֹאוּ הָאֹהֱלָה
# "[EN-AID] And Moses went out to meet his father-in-law, and bowed, and
# kissed him, and they asked each man his fellow of peace — and they came
# into the tent."
m.step("Exod.18.7")
# ‹וַיִּשְׁאֲלוּ אִישׁ־לְרֵעֵהוּ לְשָׁלוֹם› (“and-inquire man to-associate-
# him/its to-safe”) — fact holds: and-inquire-man-to-reehu-to-safe
m.fact("va_yishalu_ish_le_reehu_le_shalom")

# -------------------------- Exod.18.8 · MOSES_RECOUNTS ---------------------
# וַיְסַפֵּר מֹשֶׁה לְחֹתְנוֹ אֵת כָּל־אֲשֶׁר עָשָׂה יְהוָה לְפַרְעֹה
# וּלְמִצְרַיִם עַל אוֹדֹת יִשְׂרָאֵל אֵת כָּל־הַתְּלָאָה אֲשֶׁר מְצָאָתַם
# בַּדֶּרֶךְ וַיַּצִּלֵם יְהוָה
# "[EN-AID] And Moses recounted to his father-in-law all that the LORD had
# done to Pharaoh and to Egypt on account of Israel; all the travail that
# had found them on the way — and the LORD delivered them."
m.step("Exod.18.8")
# ‹וַיְסַפֵּר מֹשֶׁה לְחֹתְנוֹ› (“and-count Moses to-give-away-in-marriage-
# him/its”) — fact holds: and-count-Moses
m.fact("va_yesaper_moshe")

# -------------------------- Exod.18.9 · JETHRO_REJOICES --------------------
# וַיִּחַדְּ יִתְרוֹ עַל כָּל־הַטּוֹבָה אֲשֶׁר־עָשָׂה יְהוָה לְיִשְׂרָאֵל
# אֲשֶׁר הִצִּילוֹ מִיַּד מִצְרָיִם
# "[EN-AID] And Jethro rejoiced over all the good which the LORD had done
# for Israel — that He had delivered him from the hand of Egypt."
m.step("Exod.18.9")
# ‹וַיִּחַדְּ יִתְרוֹ› (“and-rejoice Jethro”) — fact holds: and-rejoice-
# Jethro
m.fact("va_yichad_yitro")

# -------------------------- Exod.18.10 · BLESSED_BE_THE_LORD ---------------
# וַיֹּאמֶר יִתְרוֹ בָּרוּךְ יְהוָה אֲשֶׁר הִצִּיל אֶתְכֶם מִיַּד מִצְרַיִם
# וּמִיַּד פַּרְעֹה אֲשֶׁר הִצִּיל אֶת־הָעָם מִתַּחַת יַד־מִצְרָיִם
# "[EN-AID] And Jethro said: Blessed be the LORD, who delivered you from the
# hand of Egypt and from the hand of Pharaoh — who delivered the people from
# under the hand of Egypt."
m.step("Exod.18.10")
# ‹בָּרוּךְ יְהוָה אֲשֶׁר הִצִּיל אֶתְכֶם מִיַּד מִצְרַיִם וּמִיַּד
# פַּרְעֹה› (“bless YHWH which snatch-away obj-marker-you/your(pl) from-hand
# Egypt and-from-hand Pharaoh”) — fact holds: bless-the-LORD
m.fact("barukh_YHWH")

# -------------------------- Exod.18.11 · NOW_I_KNOW ------------------------
# עַתָּה יָדַעְתִּי כִּי־גָדוֹל יְהוָה מִכָּל־הָאֱלֹהִים כִּי בַדָּבָר
# אֲשֶׁר זָדוּ עֲלֵיהֶם
# "[EN-AID] Now I know that the LORD is greater than all the gods — for in
# the thing in which they dealt proudly, against them."
m.step("Exod.18.11")
# ‹עַתָּה יָדַעְתִּי כִּי־גָדוֹל יְהוָה מִכָּל־הָאֱלֹהִים› (“now know that
# great YHWH from-all the-God”) — fact holds: now-know
m.fact("ata_yadati")

# -------------------------- Exod.18.12 · THE_MEAL_BEFORE_GOD ---------------
# וַיִּקַּח יִתְרוֹ חֹתֵן מֹשֶׁה עֹלָה וּזְבָחִים לֵאלֹהִים וַיָּבֹא אַהֲרֹן
# וְכֹל זִקְנֵי יִשְׂרָאֵל לֶאֱכָל־לֶחֶם עִם־חֹתֵן מֹשֶׁה לִפְנֵי הָאֱלֹהִים
# "[EN-AID] And Jethro, Moses' father-in-law, took a burnt-offering and
# sacrifices for God; and Aaron came, and all the elders of Israel, to eat
# bread with Moses' father-in-law before God."
m.step("Exod.18.12")
# ‹וַיִּקַּח יִתְרוֹ חֹתֵן מֹשֶׁה עֹלָה וּזְבָחִים לֵאלֹהִים› (“and-take
# Jethro give-away-in-marriage Moses burnt-offering and-sacrifice to-God”) —
# event: zevach-Jethro — agent Jethro; theme burnt-offering-and-zvachim
m.event("zevach_yitro", agent="yitro", themes=["ola_u_zvachim"])

# -------------------------- Exod.18.13 · THE_COURT_DAY ---------------------
# וַיְהִי מִמָּחֳרָת וַיֵּשֶׁב מֹשֶׁה לִשְׁפֹּט אֶת־הָעָם וַיַּעֲמֹד הָעָם
# עַל־מֹשֶׁה מִן־הַבֹּקֶר עַד־הָעָרֶב
# "[EN-AID] And it was on the morrow, that Moses sat to judge the people;
# and the people stood over Moses from the morning until the evening."
m.step("Exod.18.13")
# ‹וַיַּעֲמֹד הָעָם עַל־מֹשֶׁה מִן־הַבֹּקֶר עַד־הָעָרֶב› (“and-stand the-
# people over Moses from the-morning until the-evening”) — fact holds: and-
# dwell/sit-Moses-lishpot
m.fact("va_yeshev_moshe_lishpot")

# -------------------------- Exod.18.14 · WHY_ALONE -------------------------
# וַיַּרְא חֹתֵן מֹשֶׁה אֵת כָּל־אֲשֶׁר־הוּא עֹשֶׂה לָעָם וַיֹּאמֶר
# מָה־הַדָּבָר הַזֶּה אֲשֶׁר אַתָּה עֹשֶׂה לָעָם מַדּוּעַ אַתָּה יוֹשֵׁב
# לְבַדֶּךָ וְכָל־הָעָם נִצָּב עָלֶיךָ מִן־בֹּקֶר עַד־עָרֶב
# "[EN-AID] And Moses' father-in-law saw all that he was doing for the
# people — and he said: What is this thing that you are doing for the
# people? Why do you sit alone, and all the people stand over you from
# morning until evening?"
m.step("Exod.18.14")
# ‹מַדּוּעַ אַתָּה יוֹשֵׁב לְבַדֶּךָ› (“what-known? you dwell/sit to-
# separation-you/your”) — fact holds: what-known?-now-dwell/sit-levadekha
m.fact("madua_ata_yoshev_levadekha")

# -------------------------- Exod.18.15 · TO_SEEK_GOD -----------------------
# וַיֹּאמֶר מֹשֶׁה לְחֹתְנוֹ כִּי־יָבֹא אֵלַי הָעָם לִדְרֹשׁ אֱלֹהִים
# "[EN-AID] And Moses said to his father-in-law — because the people come to
# me to seek God."
m.step("Exod.18.15")
# ‹כִּי־יָבֹא אֵלַי הָעָם לִדְרֹשׁ אֱלֹהִים› (“that come/bring to-me/my the-
# people to-tread God”) — fact holds: lidrosh-God
m.fact("lidrosh_elohim")

# -------------------------- Exod.18.16 · STATUTES_AND_TORAHS ---------------
# כִּי־יִהְיֶה לָהֶם דָּבָר בָּא אֵלַי וְשָׁפַטְתִּי בֵּין אִישׁ וּבֵין
# רֵעֵהוּ וְהוֹדַעְתִּי אֶת־חֻקֵּי הָאֱלֹהִים וְאֶת־תּוֹרֹתָיו
# "[EN-AID] When they have a matter, it comes to me, and I judge between a
# man and his fellow — and I make known the statutes of God, and His
# torahs."
m.step("Exod.18.16")
# ‹וְהוֹדַעְתִּי אֶת־חֻקֵּי הָאֱלֹהִים וְאֶת־תּוֹרֹתָיו› (“and-know obj-
# marker enactment the-God and-obj-marker precept-him/its”) — fact holds:
# and-know-obj-marker-enactment-the-God
m.fact("ve_hodati_et_chuqe_ha_elohim")

# -------------------------- Exod.18.17 · NOT_GOOD --------------------------
# וַיֹּאמֶר חֹתֵן מֹשֶׁה אֵלָיו לֹא־טוֹב הַדָּבָר אֲשֶׁר אַתָּה עֹשֶׂה
# "[EN-AID] And Moses' father-in-law said to him: Not good is the thing that
# you are doing."
m.step("Exod.18.17")
# ‹לֹא־טוֹב הַדָּבָר אֲשֶׁר אַתָּה עֹשֶׂה› (“not good the-word/thing which
# you make”) — fact holds: not-good-the-word/thing
m.fact("lo_tov_ha_davar")

# -------------------------- Exod.18.18 · YOU_WILL_WILT ---------------------
# נָבֹל תִּבֹּל גַּם־אַתָּה גַּם־הָעָם הַזֶּה אֲשֶׁר עִמָּךְ כִּי־כָבֵד
# מִמְּךָ הַדָּבָר לֹא־תוּכַל עֲשֹׂהוּ לְבַדֶּךָ
# "[EN-AID] You will surely wilt — both you and this people that is with
# you; for the thing is too heavy for you — you cannot do it alone."
m.step("Exod.18.18")
# ‹כִּי־כָבֵד מִמְּךָ הַדָּבָר לֹא־תוּכַל עֲשֹׂהוּ לְבַדֶּךָ› (“that heavy
# from-you/your the-word/thing not be-able make-him/its to-separation-
# you/your”) — fact holds: wilt-wilt
m.fact("navol_tibol")

# -------------------------- Exod.18.19 · HEAR_MY_VOICE ---------------------
# עַתָּה שְׁמַע בְּקֹלִי אִיעָצְךָ וִיהִי אֱלֹהִים עִמָּךְ הֱיֵה אַתָּה
# לָעָם מוּל הָאֱלֹהִים וְהֵבֵאתָ אַתָּה אֶת־הַדְּבָרִים אֶל־הָאֱלֹהִים
# "[EN-AID] Now hear my voice — I will counsel you, and God be with you; be
# you for the people toward God, and bring you the matters to God."
m.step("Exod.18.19")
# ‹עַתָּה שְׁמַע בְּקֹלִי אִיעָצְךָ וִיהִי אֱלֹהִים עִמָּךְ› (“now hear in-
# voice/sound-me/my advise-you/your and-be God with-you/your”) — Jethro
# speaks a demand — LET: hear-in-qoli-iatzkha
m.declare("yitro", "LET",
          "shema_be_qoli_iatzkha")

# -------------------------- Exod.18.20 · WARN_AND_TEACH --------------------
# וְהִזְהַרְתָּה אֶתְהֶם אֶת־הַחֻקִּים וְאֶת־הַתּוֹרֹת וְהוֹדַעְתָּ לָהֶם
# אֶת־הַדֶּרֶךְ יֵלְכוּ בָהּ וְאֶת־הַמַּעֲשֶׂה אֲשֶׁר יַעֲשׂוּן
# "[EN-AID] And you shall warn them of the statutes and the torahs — and
# make known to them the way they shall walk in, and the deed they shall
# do."
m.step("Exod.18.20")
# ‹וְהִזְהַרְתָּה אֶתְהֶם אֶת־הַחֻקִּים וְאֶת־הַתּוֹרֹת› (“and-gleam obj-
# marker-them/their obj-marker the-enactment and-obj-marker the-precept”) —
# fact holds: and-gleam-ethem
m.fact("ve_hizharta_ethem")

# -------------------------- Exod.18.21 · MEN_OF_WORTH ----------------------
# וְאַתָּה תֶחֱזֶה מִכָּל־הָעָם אַנְשֵׁי־חַיִל יִרְאֵי אֱלֹהִים אַנְשֵׁי
# אֱמֶת שֹׂנְאֵי בָצַע וְשַׂמְתָּ עֲלֵהֶם שָׂרֵי אֲלָפִים שָׂרֵי מֵאוֹת
# שָׂרֵי חֲמִשִּׁים וְשָׂרֵי עֲשָׂרֹת
# "[EN-AID] And you shall see out of all the people men of worth, fearers of
# God, men of truth, haters of gain — and set over them princes of
# thousands, princes of hundreds, princes of fifties, and princes of tens."
m.step("Exod.18.21")
# ‹אַנְשֵׁי־חַיִל יִרְאֵי אֱלֹהִים אַנְשֵׁי אֱמֶת שֹׂנְאֵי בָצַע› (“man
# force fearing God man stability hate plunder”) — fact holds: man-force-
# fearing-God
m.fact("anshe_chayil_yire_elohim")

# -------------------------- Exod.18.22 · GREAT_AND_SMALL -------------------
# וְשָׁפְטוּ אֶת־הָעָם בְּכָל־עֵת וְהָיָה כָּל־הַדָּבָר הַגָּדֹל יָבִיאוּ
# אֵלֶיךָ וְכָל־הַדָּבָר הַקָּטֹן יִשְׁפְּטוּ־הֵם וְהָקֵל מֵעָלֶיךָ
# וְנָשְׂאוּ אִתָּךְ
# "[EN-AID] And they shall judge the people at every time; and it shall be:
# every great matter they shall bring to you, and every small matter they
# shall judge themselves — and lighten it from off you, and they shall bear
# with you."
m.step("Exod.18.22")
# ‹וְהָקֵל מֵעָלֶיךָ וְנָשְׂאוּ אִתָּךְ› (“and-be-light from-over-you/your
# and-lift/carry with-you/your”) — fact holds: and-be-light-from-alekha
m.fact("ve_haqel_me_alekha")

# -------------------------- Exod.18.23 · TO_ITS_PLACE_IN_PEACE -------------
# אִם אֶת־הַדָּבָר הַזֶּה תַּעֲשֶׂה וְצִוְּךָ אֱלֹהִים וְיָכָלְתָּ עֲמֹד
# וְגַם כָּל־הָעָם הַזֶּה עַל־מְקֹמוֹ יָבֹא בְשָׁלוֹם
# "[EN-AID] If you do this thing, and God command you, then you will be able
# to stand — and also all this people will come to its place in peace."
m.step("Exod.18.23")
# ‹וְגַם כָּל־הָעָם הַזֶּה עַל־מְקֹמוֹ יָבֹא בְשָׁלוֹם› (“and-also all the-
# people the-this over place-him/its come/bring in-safe”) — fact holds:
# over-meqomo-come/bring-and-safe
m.fact("al_meqomo_yavo_ve_shalom")

# -------------------------- Exod.18.24 · MOSES_HEARS -----------------------
# וַיִּשְׁמַע מֹשֶׁה לְקוֹל חֹתְנוֹ וַיַּעַשׂ כֹּל אֲשֶׁר אָמָר
# "[EN-AID] And Moses heard the voice of his father-in-law — and did all
# that he had said."
m.step("Exod.18.24")
# ‹וַיִּשְׁמַע מֹשֶׁה לְקוֹל חֹתְנוֹ וַיַּעַשׂ כֹּל אֲשֶׁר אָמָר› (“and-hear
# Moses to-voice/sound give-away-in-marriage-him/its and-make all which
# say”) — demand settled (popped from the queue): hear-in-qoli-iatzkha
m.result("shema_be_qoli_iatzkha", tmark="t1")

# -------------------------- Exod.18.25 · THE_JUDGES_INSTALLED --------------
# וַיִּבְחַר מֹשֶׁה אַנְשֵׁי־חַיִל מִכָּל־יִשְׂרָאֵל וַיִּתֵּן אֹתָם
# רָאשִׁים עַל־הָעָם שָׂרֵי אֲלָפִים שָׂרֵי מֵאוֹת שָׂרֵי חֲמִשִּׁים
# וְשָׂרֵי עֲשָׂרֹת
# "[EN-AID] And Moses chose men of worth out of all Israel, and gave them
# heads over the people — princes of thousands, princes of hundreds, princes
# of fifties, and princes of tens."
m.step("Exod.18.25")
# ‹וַיִּבְחַר מֹשֶׁה אַנְשֵׁי־חַיִל מִכָּל־יִשְׂרָאֵל וַיִּתֵּן אֹתָם
# רָאשִׁים› (“and-try Moses man force from-all Israel and-set obj-marker-
# them/their head”) — fact holds: and-set-otam-head
m.fact("va_yiten_otam_rashim")

# -------------------------- Exod.18.26 · THE_HARD_TO_MOSES -----------------
# וְשָׁפְטוּ אֶת־הָעָם בְּכָל־עֵת אֶת־הַדָּבָר הַקָּשֶׁה יְבִיאוּן
# אֶל־מֹשֶׁה וְכָל־הַדָּבָר הַקָּטֹן יִשְׁפּוּטוּ הֵם
# "[EN-AID] And they judged the people at every time; the hard matter they
# would bring to Moses, and every small matter they would judge themselves."
m.step("Exod.18.26")
# ‹וְכָל־הַדָּבָר הַקָּטֹן יִשְׁפּוּטוּ הֵם› (“and-all the-word/thing the-
# small judge they”) — fact holds: judge-them/their
m.fact("yishputu_hem")

# -------------------------- Exod.18.27 · THE_SEND_OFF ----------------------
# וַיְשַׁלַּח מֹשֶׁה אֶת־חֹתְנוֹ וַיֵּלֶךְ לוֹ אֶל־אַרְצוֹ
# "[EN-AID] And Moses sent his father-in-law away — and he went him to his
# land."
m.step("Exod.18.27")
# ‹וַיֵּלֶךְ לוֹ אֶל־אַרְצוֹ› (“and-go to-him/its to earth-him/its”) — fact
# holds: and-go-not-to-artzo
m.fact("va_yelekh_lo_el_artzo")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yishma_yitro', 'achar_shilucheha', 'ger_hayiti_be_eretz_nakhriya', 'elohe_avi_be_ezri', 'el_har_ha_elohim', 'ani_chotenkha_ba_elekha', 'va_yishalu_ish_le_reehu_le_shalom', 'va_yesaper_moshe', 'va_yichad_yitro', 'barukh_YHWH', 'ata_yadati', 'va_yeshev_moshe_lishpot', 'madua_ata_yoshev_levadekha', 'lidrosh_elohim', 've_hodati_et_chuqe_ha_elohim', 'lo_tov_ha_davar', 'navol_tibol', 've_hizharta_ethem', 'anshe_chayil_yire_elohim', 've_haqel_me_alekha', 'al_meqomo_yavo_ve_shalom', 'va_yiten_otam_rashim', 'yishputu_hem', 'va_yelekh_lo_el_artzo'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 3
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
