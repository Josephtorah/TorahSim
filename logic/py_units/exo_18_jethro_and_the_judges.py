#!/usr/bin/env python3
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
# ‹וַיִּשְׁמַע יִתְרוֹ כֹהֵן› (“and-hear Jethro priest”)
# ‹מִדְיָן חֹתֵן מֹשֶׁה› (“Midian give-away-in-marriage Moses”)
# ‹אֵת כָּל־אֲשֶׁר עָשָׂה› (“obj-marker all which make”)
# ‹אֱלֹהִים לְמֹשֶׁה וּלְיִשְׂרָאֵל› (“God to-Moses and-to-Israel”)
# ‹עַמּוֹ כִּי־הוֹצִיא יְהוָה› (“people-him/its that bring-forth YHWH”)
# ‹אֶת־יִשְׂרָאֵל מִמִּצְרָיִם› (“obj-marker Israel from-Egypt”)
# "[EN-AID] And Jethro, priest of Midian, Moses' father-in-law, heard all
# that God had done for Moses and for Israel His people — that the LORD had
# brought Israel out from Egypt."
m.step("Exod.18.1")
# ‹וַיִּשְׁמַע יִתְרוֹ כֹהֵן› (“and-hear Jethro priest”)
# ‹מִדְיָן חֹתֵן מֹשֶׁה› (“Midian give-away-in-marriage Moses”)
# — fact holds: and-hear-Jethro
m.fact("va_yishma_yitro")

# -------------------------- Exod.18.2 · AFTER_HER_SENDING ------------------
# ‹וַיִּקַּח יִתְרוֹ חֹתֵן› (“and-take Jethro give-away-in-marriage”)
# ‹מֹשֶׁה אֶת־צִפֹּרָה אֵשֶׁת› (“Moses obj-marker Zipporah woman”)
# ‹מֹשֶׁה אַחַר שִׁלּוּחֶיהָ› (“Moses after dismissal-her/its”)
# "[EN-AID] And Jethro, Moses' father-in-law, took Zipporah, Moses' wife —
# after her being sent away."
m.step("Exod.18.2")
# ‹אֶת־צִפֹּרָה אֵשֶׁת מֹשֶׁה› (“obj-marker Zipporah woman Moses”)
# ‹אַחַר שִׁלּוּחֶיהָ› (“after dismissal-her/its”)
# — fact holds: after-shilucheha
m.fact("achar_shilucheha")

# -------------------------- Exod.18.3 · GERSHOM ----------------------------
# ‹וְאֵת שְׁנֵי בָנֶיהָ› (“and-obj-marker two son-her/its”)
# ‹אֲשֶׁר שֵׁם הָאֶחָד› (“which name the-one”)
# ‹גֵּרְשֹׁם כִּי אָמַר› (“Gershom that say”)
# ‹גֵּר הָיִיתִי בְּאֶרֶץ› (“sojourner be in-earth”)
# ‹נָכְרִיָּה› (“strange”)
# "[EN-AID] And her two sons — of whom the name of the one was Gershom, for
# he said: A stranger have I been in a foreign land."
m.step("Exod.18.3")
# ‹הָאֶחָד גֵּרְשֹׁם כִּי› (“the-one Gershom that”)
# ‹אָמַר גֵּר הָיִיתִי› (“say sojourner be”)
# ‹בְּאֶרֶץ נָכְרִיָּה› (“in-earth strange”)
# — fact holds: sojourner-be-in-earth-strange
m.fact("ger_hayiti_be_eretz_nakhriya")

# -------------------------- Exod.18.4 · ELIEZER ----------------------------
# ‹וְשֵׁם הָאֶחָד אֱלִיעֶזֶר› (“and-name the-one Eliezer”)
# ‹כִּי־אֱלֹהֵי אָבִי בְּעֶזְרִי› (“that God father-me/my in-aid-me/my”)
# ‹וַיַּצִּלֵנִי מֵחֶרֶב פַּרְעֹה› (“and-snatch-away-me/my from-drought
# Pharaoh”)
# "[EN-AID] And the name of the one was Eliezer — for the God of my father
# was my help, and delivered me from the sword of Pharaoh."
m.step("Exod.18.4")
# ‹כִּי־אֱלֹהֵי אָבִי בְּעֶזְרִי› (“that God father-me/my in-aid-me/my”)
# ‹וַיַּצִּלֵנִי מֵחֶרֶב פַּרְעֹה› (“and-snatch-away-me/my from-drought
# Pharaoh”)
# — fact holds: God-avi-in-ezri
m.fact("elohe_avi_be_ezri")

# -------------------------- Exod.18.5 · TO_THE_MOUNT_OF_GOD ----------------
# ‹וַיָּבֹא יִתְרוֹ חֹתֵן› (“and-come/bring Jethro give-away-in-marriage”)
# ‹מֹשֶׁה וּבָנָיו וְאִשְׁתּוֹ› (“Moses and-son-him/its and-woman-him/its”)
# ‹אֶל־מֹשֶׁה אֶל־הַמִּדְבָּר אֲשֶׁר־הוּא› (“to Moses to the-pasture which
# he/it”)
# ‹חֹנֶה שָׁם הַר› (“encamp there mountain”)
# ‹הָאֱלֹהִים› (“the-God”)
# "[EN-AID] And Jethro, Moses' father-in-law, came, and his sons and his
# wife, to Moses — to the wilderness where he was camping, the mount of
# God."
m.step("Exod.18.5")
# ‹אֶל־הַמִּדְבָּר אֲשֶׁר־הוּא חֹנֶה› (“to the-pasture which he/it encamp”)
# ‹שָׁם הַר הָאֱלֹהִים› (“there mountain the-God”)
# — fact holds: to-mountain-the-God
m.fact("el_har_ha_elohim")

# -------------------------- Exod.18.6 · I_YOUR_FATHER_IN_LAW ---------------
# ‹וַיֹּאמֶר אֶל־מֹשֶׁה אֲנִי› (“and-say to Moses”)
# ‹חֹתֶנְךָ יִתְרוֹ בָּא› (“give-away-in-marriage-you/your Jethro
# come/bring”)
# ‹אֵלֶיךָ וְאִשְׁתְּךָ וּשְׁנֵי› (“to-you/your and-woman-you/your and-two”)
# ‹בָנֶיהָ עִמָּהּ› (“son-her/its with-her/its”)
# "[EN-AID] And he said to Moses: I, your father-in-law Jethro, am coming to
# you — and your wife, and her two sons with her."
m.step("Exod.18.6")
# ‹אֲנִי חֹתֶנְךָ יִתְרוֹ› (“give-away-in-marriage-you/your Jethro”)
# ‹בָּא אֵלֶיךָ› (“come/bring to-you/your”)
# — fact holds: ani-chotenkha-come/bring-to-you
m.fact("ani_chotenkha_ba_elekha")

# -------------------------- Exod.18.7 · THE_GREETING -----------------------
# ‹וַיֵּצֵא מֹשֶׁה לִקְרַאת› (“and-bring-forth Moses to-encountering”)
# ‹חֹתְנוֹ וַיִּשְׁתַּחוּ וַיִּשַּׁק־לוֹ› (“give-away-in-marriage-him/its
# and-afflict and-kiss to-him/its”)
# ‹וַיִּשְׁאֲלוּ אִישׁ־לְרֵעֵהוּ לְשָׁלוֹם› (“and-inquire man to-associate-
# him/its to-safe”)
# ‹וַיָּבֹאוּ הָאֹהֱלָה› (“and-come/bring the-tent-ward”)
# "[EN-AID] And Moses went out to meet his father-in-law, and bowed, and
# kissed him, and they asked each man his fellow of peace — and they came
# into the tent."
m.step("Exod.18.7")
# ‹וַיִּשְׁאֲלוּ אִישׁ־לְרֵעֵהוּ לְשָׁלוֹם› (“and-inquire man to-associate-
# him/its to-safe”)
# — fact holds: and-inquire-man-to-reehu-to-safe
m.fact("va_yishalu_ish_le_reehu_le_shalom")

# -------------------------- Exod.18.8 · MOSES_RECOUNTS ---------------------
# ‹וַיְסַפֵּר מֹשֶׁה לְחֹתְנוֹ› (“and-count Moses to-give-away-in-marriage-
# him/its”)
# ‹אֵת כָּל־אֲשֶׁר עָשָׂה› (“obj-marker all which make”)
# ‹יְהוָה לְפַרְעֹה וּלְמִצְרַיִם› (“YHWH to-Pharaoh and-to-Egypt”)
# ‹עַל אוֹדֹת יִשְׂרָאֵל› (“over turnings Israel”)
# ‹אֵת כָּל־הַתְּלָאָה אֲשֶׁר› (“obj-marker all the-distress which”)
# ‹מְצָאָתַם בַּדֶּרֶךְ וַיַּצִּלֵם› (“find-them/their in-way/road and-
# snatch-away-them/their”)
# ‹יְהוָה› (“YHWH”)
# "[EN-AID] And Moses recounted to his father-in-law all that the LORD had
# done to Pharaoh and to Egypt on account of Israel; all the travail that
# had found them on the way — and the LORD delivered them."
m.step("Exod.18.8")
# ‹וַיְסַפֵּר מֹשֶׁה לְחֹתְנוֹ› (“and-count Moses to-give-away-in-marriage-
# him/its”)
# — fact holds: and-count-Moses
m.fact("va_yesaper_moshe")

# -------------------------- Exod.18.9 · JETHRO_REJOICES --------------------
# ‹וַיִּחַדְּ יִתְרוֹ עַל› (“and-rejoice Jethro over”)
# ‹כָּל־הַטּוֹבָה אֲשֶׁר־עָשָׂה יְהוָה› (“all the-good-in-the-widest-sense
# which make YHWH”)
# ‹לְיִשְׂרָאֵל אֲשֶׁר הִצִּילוֹ› (“to-Israel which snatch-away-him/its”)
# ‹מִיַּד מִצְרָיִם› (“from-hand Egypt”)
# "[EN-AID] And Jethro rejoiced over all the good which the LORD had done
# for Israel — that He had delivered him from the hand of Egypt."
m.step("Exod.18.9")
# ‹וַיִּחַדְּ יִתְרוֹ› (“and-rejoice Jethro”)
# — fact holds: and-rejoice-Jethro
m.fact("va_yichad_yitro")

# -------------------------- Exod.18.10 · BLESSED_BE_THE_LORD ---------------
# ‹וַיֹּאמֶר יִתְרוֹ בָּרוּךְ› (“and-say Jethro bless”)
# ‹יְהוָה אֲשֶׁר הִצִּיל› (“YHWH which snatch-away”)
# ‹אֶתְכֶם מִיַּד מִצְרַיִם› (“obj-marker-you/your(pl) from-hand Egypt”)
# ‹וּמִיַּד פַּרְעֹה אֲשֶׁר› (“and-from-hand Pharaoh which”)
# ‹הִצִּיל אֶת־הָעָם מִתַּחַת› (“snatch-away obj-marker the-people from-
# under”)
# ‹יַד־מִצְרָיִם› (“hand Egypt”)
# "[EN-AID] And Jethro said: Blessed be the LORD, who delivered you from the
# hand of Egypt and from the hand of Pharaoh — who delivered the people from
# under the hand of Egypt."
m.step("Exod.18.10")
# ‹בָּרוּךְ יְהוָה אֲשֶׁר› (“bless YHWH which”)
# ‹הִצִּיל אֶתְכֶם מִיַּד› (“snatch-away obj-marker-you/your(pl) from-hand”)
# ‹מִצְרַיִם וּמִיַּד פַּרְעֹה› (“Egypt and-from-hand Pharaoh”)
# — fact holds: bless-the-LORD
m.fact("barukh_YHWH")

# -------------------------- Exod.18.11 · NOW_I_KNOW ------------------------
# ‹עַתָּה יָדַעְתִּי כִּי־גָדוֹל› (“now know that great”)
# ‹יְהוָה מִכָּל־הָאֱלֹהִים כִּי› (“YHWH from-all the-God that”)
# ‹בַדָּבָר אֲשֶׁר זָדוּ› (“in-word/thing which seethe”)
# ‹עֲלֵיהֶם› (“over-them/their”)
# "[EN-AID] Now I know that the LORD is greater than all the gods — for in
# the thing in which they dealt proudly, against them."
m.step("Exod.18.11")
# ‹עַתָּה יָדַעְתִּי כִּי־גָדוֹל› (“now know that great”)
# ‹יְהוָה מִכָּל־הָאֱלֹהִים› (“YHWH from-all the-God”)
# — fact holds: now-know
m.fact("ata_yadati")

# -------------------------- Exod.18.12 · THE_MEAL_BEFORE_GOD ---------------
# ‹וַיִּקַּח יִתְרוֹ חֹתֵן› (“and-take Jethro give-away-in-marriage”)
# ‹מֹשֶׁה עֹלָה וּזְבָחִים› (“Moses burnt-offering and-sacrifice”)
# ‹לֵאלֹהִים וַיָּבֹא אַהֲרֹן› (“to-God and-come/bring Aaron”)
# ‹וְכֹל זִקְנֵי יִשְׂרָאֵל› (“and-all old Israel”)
# ‹לֶאֱכָל־לֶחֶם עִם־חֹתֵן מֹשֶׁה› (“to-eat food with give-away-in-marriage
# Moses”)
# ‹לִפְנֵי הָאֱלֹהִים› (“to-face the-God”)
# "[EN-AID] And Jethro, Moses' father-in-law, took a burnt-offering and
# sacrifices for God; and Aaron came, and all the elders of Israel, to eat
# bread with Moses' father-in-law before God."
m.step("Exod.18.12")
# ‹וַיִּקַּח יִתְרוֹ חֹתֵן› (“and-take Jethro give-away-in-marriage”)
# ‹מֹשֶׁה עֹלָה וּזְבָחִים› (“Moses burnt-offering and-sacrifice”)
# ‹לֵאלֹהִים› (“to-God”)
# — event: zevach-Jethro — agent Jethro; theme burnt-offering-and-zvachim
m.event("zevach_yitro", agent="yitro", themes=["ola_u_zvachim"])

# -------------------------- Exod.18.13 · THE_COURT_DAY ---------------------
# ‹וַיְהִי מִמָּחֳרָת וַיֵּשֶׁב› (“and-be from-morrow and-dwell/sit”)
# ‹מֹשֶׁה לִשְׁפֹּט אֶת־הָעָם› (“Moses to-judge obj-marker the-people”)
# ‹וַיַּעֲמֹד הָעָם עַל־מֹשֶׁה› (“and-stand the-people over Moses”)
# ‹מִן־הַבֹּקֶר עַד־הָעָרֶב› (“from the-morning until the-evening”)
# "[EN-AID] And it was on the morrow, that Moses sat to judge the people;
# and the people stood over Moses from the morning until the evening."
m.step("Exod.18.13")
# ‹וַיַּעֲמֹד הָעָם עַל־מֹשֶׁה› (“and-stand the-people over Moses”)
# ‹מִן־הַבֹּקֶר עַד־הָעָרֶב› (“from the-morning until the-evening”)
# — fact holds: and-dwell/sit-Moses-lishpot
m.fact("va_yeshev_moshe_lishpot")

# -------------------------- Exod.18.14 · WHY_ALONE -------------------------
# ‹וַיַּרְא חֹתֵן מֹשֶׁה› (“and-see give-away-in-marriage Moses”)
# ‹אֵת כָּל־אֲשֶׁר־הוּא עֹשֶׂה› (“obj-marker all which he/it make”)
# ‹לָעָם וַיֹּאמֶר מָה־הַדָּבָר› (“to-people and-say what the-word/thing”)
# ‹הַזֶּה אֲשֶׁר אַתָּה› (“the-this which you”)
# ‹עֹשֶׂה לָעָם מַדּוּעַ› (“make to-people what-known?”)
# ‹אַתָּה יוֹשֵׁב לְבַדֶּךָ› (“you dwell/sit to-separation-you/your”)
# ‹וְכָל־הָעָם נִצָּב עָלֶיךָ› (“and-all the-people stand over-you/your”)
# ‹מִן־בֹּקֶר עַד־עָרֶב› (“from morning until evening”)
# "[EN-AID] And Moses' father-in-law saw all that he was doing for the
# people — and he said: What is this thing that you are doing for the
# people? Why do you sit alone, and all the people stand over you from
# morning until evening?"
m.step("Exod.18.14")
# ‹מַדּוּעַ אַתָּה יוֹשֵׁב› (“what-known? you dwell/sit”)
# ‹לְבַדֶּךָ› (“to-separation-you/your”)
# — fact holds: what-known?-now-dwell/sit-levadekha
m.fact("madua_ata_yoshev_levadekha")

# -------------------------- Exod.18.15 · TO_SEEK_GOD -----------------------
# ‹וַיֹּאמֶר מֹשֶׁה לְחֹתְנוֹ› (“and-say Moses to-give-away-in-marriage-
# him/its”)
# ‹כִּי־יָבֹא אֵלַי הָעָם› (“that come/bring to-me/my the-people”)
# ‹לִדְרֹשׁ אֱלֹהִים› (“to-tread God”)
# "[EN-AID] And Moses said to his father-in-law — because the people come to
# me to seek God."
m.step("Exod.18.15")
# ‹כִּי־יָבֹא אֵלַי הָעָם› (“that come/bring to-me/my the-people”)
# ‹לִדְרֹשׁ אֱלֹהִים› (“to-tread God”)
# — fact holds: lidrosh-God
m.fact("lidrosh_elohim")

# -------------------------- Exod.18.16 · STATUTES_AND_TORAHS ---------------
# ‹כִּי־יִהְיֶה לָהֶם דָּבָר› (“that be to-them/their word/thing”)
# ‹בָּא אֵלַי וְשָׁפַטְתִּי› (“come/bring to-me/my and-judge”)
# ‹בֵּין אִישׁ וּבֵין› (“between man and-between”)
# ‹רֵעֵהוּ וְהוֹדַעְתִּי אֶת־חֻקֵּי› (“associate-him/its and-know obj-marker
# enactment”)
# ‹הָאֱלֹהִים וְאֶת־תּוֹרֹתָיו› (“the-God and-obj-marker precept-him/its”)
# "[EN-AID] When they have a matter, it comes to me, and I judge between a
# man and his fellow — and I make known the statutes of God, and His
# torahs."
m.step("Exod.18.16")
# ‹וְהוֹדַעְתִּי אֶת־חֻקֵּי הָאֱלֹהִים› (“and-know obj-marker enactment the-
# God”)
# ‹וְאֶת־תּוֹרֹתָיו› (“and-obj-marker precept-him/its”)
# — fact holds: and-know-obj-marker-enactment-the-God
m.fact("ve_hodati_et_chuqe_ha_elohim")

# -------------------------- Exod.18.17 · NOT_GOOD --------------------------
# ‹וַיֹּאמֶר חֹתֵן מֹשֶׁה› (“and-say give-away-in-marriage Moses”)
# ‹אֵלָיו לֹא־טוֹב הַדָּבָר› (“to-him/its not good the-word/thing”)
# ‹אֲשֶׁר אַתָּה עֹשֶׂה› (“which you make”)
# "[EN-AID] And Moses' father-in-law said to him: Not good is the thing that
# you are doing."
m.step("Exod.18.17")
# ‹לֹא־טוֹב הַדָּבָר אֲשֶׁר› (“not good the-word/thing which”)
# ‹אַתָּה עֹשֶׂה› (“you make”)
# — fact holds: not-good-the-word/thing
m.fact("lo_tov_ha_davar")

# -------------------------- Exod.18.18 · YOU_WILL_WILT ---------------------
# ‹נָבֹל תִּבֹּל גַּם־אַתָּה› (“wilt wilt also you”)
# ‹גַּם־הָעָם הַזֶּה אֲשֶׁר› (“also the-people the-this which”)
# ‹עִמָּךְ כִּי־כָבֵד מִמְּךָ› (“with-you/your that heavy from-you/your”)
# ‹הַדָּבָר לֹא־תוּכַל עֲשֹׂהוּ› (“the-word/thing not be-able make-him/its”)
# ‹לְבַדֶּךָ› (“to-separation-you/your”)
# "[EN-AID] You will surely wilt — both you and this people that is with
# you; for the thing is too heavy for you — you cannot do it alone."
m.step("Exod.18.18")
# ‹כִּי־כָבֵד מִמְּךָ הַדָּבָר› (“that heavy from-you/your the-word/thing”)
# ‹לֹא־תוּכַל עֲשֹׂהוּ לְבַדֶּךָ› (“not be-able make-him/its to-separation-
# you/your”)
# — fact holds: wilt-wilt
m.fact("navol_tibol")

# -------------------------- Exod.18.19 · HEAR_MY_VOICE ---------------------
# ‹עַתָּה שְׁמַע בְּקֹלִי› (“now hear in-voice/sound-me/my”)
# ‹אִיעָצְךָ וִיהִי אֱלֹהִים› (“advise-you/your and-be God”)
# ‹עִמָּךְ הֱיֵה אַתָּה› (“with-you/your be you”)
# ‹לָעָם מוּל הָאֱלֹהִים› (“to-people abrupt the-God”)
# ‹וְהֵבֵאתָ אַתָּה אֶת־הַדְּבָרִים› (“and-come/bring you obj-marker the-
# word/thing”)
# ‹אֶל־הָאֱלֹהִים› (“to the-God”)
# "[EN-AID] Now hear my voice — I will counsel you, and God be with you; be
# you for the people toward God, and bring you the matters to God."
m.step("Exod.18.19")
# ‹עַתָּה שְׁמַע בְּקֹלִי› (“now hear in-voice/sound-me/my”)
# ‹אִיעָצְךָ וִיהִי אֱלֹהִים› (“advise-you/your and-be God”)
# ‹עִמָּךְ› (“with-you/your”)
# — Jethro speaks a demand — LET: hear-in-qoli-iatzkha
m.declare("yitro", "LET",
          "shema_be_qoli_iatzkha")

# -------------------------- Exod.18.20 · WARN_AND_TEACH --------------------
# ‹וְהִזְהַרְתָּה אֶתְהֶם אֶת־הַחֻקִּים› (“and-gleam obj-marker-them/their
# obj-marker the-enactment”)
# ‹וְאֶת־הַתּוֹרֹת וְהוֹדַעְתָּ לָהֶם› (“and-obj-marker the-precept and-know
# to-them/their”)
# ‹אֶת־הַדֶּרֶךְ יֵלְכוּ בָהּ› (“obj-marker the-way/road go in-her/its”)
# ‹וְאֶת־הַמַּעֲשֶׂה אֲשֶׁר יַעֲשׂוּן› (“and-obj-marker the-deed/work which
# make-ward”)
# "[EN-AID] And you shall warn them of the statutes and the torahs — and
# make known to them the way they shall walk in, and the deed they shall
# do."
m.step("Exod.18.20")
# ‹וְהִזְהַרְתָּה אֶתְהֶם אֶת־הַחֻקִּים› (“and-gleam obj-marker-them/their
# obj-marker the-enactment”)
# ‹וְאֶת־הַתּוֹרֹת› (“and-obj-marker the-precept”)
# — fact holds: and-gleam-ethem
m.fact("ve_hizharta_ethem")

# -------------------------- Exod.18.21 · MEN_OF_WORTH ----------------------
# ‹וְאַתָּה תֶחֱזֶה מִכָּל־הָעָם› (“and-you gaze-at from-all the-people”)
# ‹אַנְשֵׁי־חַיִל יִרְאֵי אֱלֹהִים› (“man force fearing God”)
# ‹אַנְשֵׁי אֱמֶת שֹׂנְאֵי› (“man stability hate”)
# ‹בָצַע וְשַׂמְתָּ עֲלֵהֶם› (“plunder and-put/set over-them/their”)
# ‹שָׂרֵי אֲלָפִים שָׂרֵי› (“officer thousand officer”)
# ‹מֵאוֹת שָׂרֵי חֲמִשִּׁים› (“hundred officer fifty”)
# ‹וְשָׂרֵי עֲשָׂרֹת› (“and-officer ten”)
# "[EN-AID] And you shall see out of all the people men of worth, fearers of
# God, men of truth, haters of gain — and set over them princes of
# thousands, princes of hundreds, princes of fifties, and princes of tens."
m.step("Exod.18.21")
# ‹אַנְשֵׁי־חַיִל יִרְאֵי אֱלֹהִים› (“man force fearing God”)
# ‹אַנְשֵׁי אֱמֶת שֹׂנְאֵי› (“man stability hate”)
# ‹בָצַע› (“plunder”)
# — fact holds: man-force-fearing-God
m.fact("anshe_chayil_yire_elohim")

# -------------------------- Exod.18.22 · GREAT_AND_SMALL -------------------
# ‹וְשָׁפְטוּ אֶת־הָעָם בְּכָל־עֵת› (“and-judge obj-marker the-people in-all
# time”)
# ‹וְהָיָה כָּל־הַדָּבָר הַגָּדֹל› (“and-be all the-word/thing the-great”)
# ‹יָבִיאוּ אֵלֶיךָ וְכָל־הַדָּבָר› (“come/bring to-you/your and-all the-
# word/thing”)
# ‹הַקָּטֹן יִשְׁפְּטוּ־הֵם וְהָקֵל› (“the-small judge they and-be-light”)
# ‹מֵעָלֶיךָ וְנָשְׂאוּ אִתָּךְ› (“from-over-you/your and-lift/carry with-
# you/your”)
# "[EN-AID] And they shall judge the people at every time; and it shall be:
# every great matter they shall bring to you, and every small matter they
# shall judge themselves — and lighten it from off you, and they shall bear
# with you."
m.step("Exod.18.22")
# ‹וְהָקֵל מֵעָלֶיךָ וְנָשְׂאוּ› (“and-be-light from-over-you/your and-
# lift/carry”)
# ‹אִתָּךְ› (“with-you/your”)
# — fact holds: and-be-light-from-alekha
m.fact("ve_haqel_me_alekha")
# witness-tier presupposed read: court_tiers on great_matter — read, not
# installed
m.witness_read("great_matter", "court_tiers",
                cites=["Mishnah Sanhedrin 1:5", "Mishnah Sanhedrin 4:1", "Mishnah Sanhedrin 4:2"])
# witness-tier presupposed read: appointment_constitution on great_matter —
# read, not installed
m.witness_read("great_matter", "appointment_constitution",
                cites=["Sanhedrin 16a:1", "Sanhedrin 16b:9", "Sanhedrin 17a:3", "Sanhedrin 17b:11", "Sanhedrin 18a:3", "Sanhedrin 34b:8", "Shevuot 30b:2"])

# -------------------------- Exod.18.23 · TO_ITS_PLACE_IN_PEACE -------------
# ‹אִם אֶת־הַדָּבָר הַזֶּה› (“if obj-marker the-word/thing the-this”)
# ‹תַּעֲשֶׂה וְצִוְּךָ אֱלֹהִים› (“make and-command-you/your God”)
# ‹וְיָכָלְתָּ עֲמֹד וְגַם› (“and-be-able stand and-also”)
# ‹כָּל־הָעָם הַזֶּה עַל־מְקֹמוֹ› (“all the-people the-this over place-
# him/its”)
# ‹יָבֹא בְשָׁלוֹם› (“come/bring in-safe”)
# "[EN-AID] If you do this thing, and God command you, then you will be able
# to stand — and also all this people will come to its place in peace."
m.step("Exod.18.23")
# ‹וְגַם כָּל־הָעָם הַזֶּה› (“and-also all the-people the-this”)
# ‹עַל־מְקֹמוֹ יָבֹא בְשָׁלוֹם› (“over place-him/its come/bring in-safe”)
# — fact holds: over-meqomo-come/bring-and-safe
m.fact("al_meqomo_yavo_ve_shalom")

# -------------------------- Exod.18.24 · MOSES_HEARS -----------------------
# ‹וַיִּשְׁמַע מֹשֶׁה לְקוֹל› (“and-hear Moses to-voice/sound”)
# ‹חֹתְנוֹ וַיַּעַשׂ כֹּל› (“give-away-in-marriage-him/its and-make all”)
# ‹אֲשֶׁר אָמָר› (“which say”)
# "[EN-AID] And Moses heard the voice of his father-in-law — and did all
# that he had said."
m.step("Exod.18.24")
# ‹וַיִּשְׁמַע מֹשֶׁה לְקוֹל› (“and-hear Moses to-voice/sound”)
# ‹חֹתְנוֹ וַיַּעַשׂ כֹּל› (“give-away-in-marriage-him/its and-make all”)
# ‹אֲשֶׁר אָמָר› (“which say”)
# — demand settled (popped from the queue): hear-in-qoli-iatzkha
m.result("shema_be_qoli_iatzkha", tmark="t1")

# -------------------------- Exod.18.25 · THE_JUDGES_INSTALLED --------------
# ‹וַיִּבְחַר מֹשֶׁה אַנְשֵׁי־חַיִל› (“and-try Moses man force”)
# ‹מִכָּל־יִשְׂרָאֵל וַיִּתֵּן אֹתָם› (“from-all Israel and-set obj-marker-
# them/their”)
# ‹רָאשִׁים עַל־הָעָם שָׂרֵי› (“head over the-people officer”)
# ‹אֲלָפִים שָׂרֵי מֵאוֹת› (“thousand officer hundred”)
# ‹שָׂרֵי חֲמִשִּׁים וְשָׂרֵי› (“officer fifty and-officer”)
# ‹עֲשָׂרֹת› (“ten”)
# "[EN-AID] And Moses chose men of worth out of all Israel, and gave them
# heads over the people — princes of thousands, princes of hundreds, princes
# of fifties, and princes of tens."
m.step("Exod.18.25")
# ‹וַיִּבְחַר מֹשֶׁה אַנְשֵׁי־חַיִל› (“and-try Moses man force”)
# ‹מִכָּל־יִשְׂרָאֵל וַיִּתֵּן אֹתָם› (“from-all Israel and-set obj-marker-
# them/their”)
# ‹רָאשִׁים› (“head”)
# — fact holds: and-set-otam-head
m.fact("va_yiten_otam_rashim")

# -------------------------- Exod.18.26 · THE_HARD_TO_MOSES -----------------
# ‹וְשָׁפְטוּ אֶת־הָעָם בְּכָל־עֵת› (“and-judge obj-marker the-people in-all
# time”)
# ‹אֶת־הַדָּבָר הַקָּשֶׁה יְבִיאוּן› (“obj-marker the-word/thing the-severe
# come/bring-ward”)
# ‹אֶל־מֹשֶׁה וְכָל־הַדָּבָר הַקָּטֹן› (“to Moses and-all the-word/thing
# the-small”)
# ‹יִשְׁפּוּטוּ הֵם› (“judge they”)
# "[EN-AID] And they judged the people at every time; the hard matter they
# would bring to Moses, and every small matter they would judge themselves."
m.step("Exod.18.26")
# ‹וְכָל־הַדָּבָר הַקָּטֹן יִשְׁפּוּטוּ› (“and-all the-word/thing the-small
# judge”)
# ‹הֵם› (“they”)
# — fact holds: judge-them/their
m.fact("yishputu_hem")

# -------------------------- Exod.18.27 · THE_SEND_OFF ----------------------
# ‹וַיְשַׁלַּח מֹשֶׁה אֶת־חֹתְנוֹ› (“and-send Moses obj-marker give-away-in-
# marriage-him/its”)
# ‹וַיֵּלֶךְ לוֹ אֶל־אַרְצוֹ› (“and-go to-him/its to earth-him/its”)
# "[EN-AID] And Moses sent his father-in-law away — and he went him to his
# land."
m.step("Exod.18.27")
# ‹וַיֵּלֶךְ לוֹ אֶל־אַרְצוֹ› (“and-go to-him/its to earth-him/its”)
# — fact holds: and-go-not-to-artzo
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('great_matter', 'court_tiers'), ('great_matter', 'appointment_constitution')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Sanhedrin 1:5', 'Mishnah Sanhedrin 4:1', 'Mishnah Sanhedrin 4:2']
    assert all('court_tiers' not in f for f in m.WORLD["facts"])
    assert 'great_matter' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sanhedrin 16a:1', 'Sanhedrin 16b:9', 'Sanhedrin 17a:3', 'Sanhedrin 17b:11', 'Sanhedrin 18a:3', 'Sanhedrin 34b:8', 'Shevuot 30b:2']
    assert all('appointment_constitution' not in f for f in m.WORLD["facts"])
    assert 'great_matter' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
