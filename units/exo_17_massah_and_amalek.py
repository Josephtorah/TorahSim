#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_17_massah_and_amalek — 17:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_17_massah_and_amalek.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Massah-Meribah and Amalek (17:1-16)"""
from machine import Machine

m = Machine("exo_17_massah_and_amalek")

# -------------------------- Exod.17.1 · NO_WATER_IN_REPHIDIM ---------------
# וַיִּסְעוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל מִמִּדְבַּר־סִין לְמַסְעֵיהֶם
# עַל־פִּי יְהוָה וַיַּחֲנוּ בִּרְפִידִים וְאֵין מַיִם לִשְׁתֹּת הָעָם
# "[EN-AID] And all the congregation of the sons of Israel journeyed from
# the wilderness of Sin, by their journeys, according to the mouth of the
# LORD; and they camped in Rephidim — and there was no water for the people
# to drink."
m.step("Exod.17.1")
# ‹וַיַּחֲנוּ בִּרְפִידִים וְאֵין מַיִם לִשְׁתֹּת הָעָם› (“and-encamp in-
# Rephidim and-there-is-not waters to-drink the-people”) — fact holds: and-
# encamp-bi-refidim-and-there-is-not-waters
m.fact("va_yachanu_bi_refidim_ve_en_mayim")

# -------------------------- Exod.17.2 · GIVE_US_WATER ----------------------
# וַיָּרֶב הָעָם עִם־מֹשֶׁה וַיֹּאמְרוּ תְּנוּ־לָנוּ מַיִם וְנִשְׁתֶּה
# וַיֹּאמֶר לָהֶם מֹשֶׁה מַה־תְּרִיבוּן עִמָּדִי מַה־תְּנַסּוּן אֶת־יְהוָה
# "[EN-AID] And the people quarreled with Moses, and said: Give us water,
# that we may drink. And Moses said to them: Why do you quarrel with me? Why
# do you test the LORD?"
m.step("Exod.17.2")
# ‹תְּנוּ־לָנוּ מַיִם וְנִשְׁתֶּה› (“set to-us/our waters and-drink”) — the-
# people speaks a demand — LET: set-lanu-waters
m.declare("ha_am", "LET",
          "tenu_lanu_mayim")

# -------------------------- Exod.17.3 · WHY_DID_YOU_BRING_US_UP ------------
# וַיִּצְמָא שָׁם הָעָם לַמַּיִם וַיָּלֶן הָעָם עַל־מֹשֶׁה וַיֹּאמֶר לָמָּה
# זֶּה הֶעֱלִיתָנוּ מִמִּצְרַיִם לְהָמִית אֹתִי וְאֶת־בָּנַי וְאֶת־מִקְנַי
# בַּצָּמָא
# "[EN-AID] And the people thirsted there for water, and the people murmured
# against Moses, and said: Why is this — you brought us up from Egypt, to
# kill me and my sons and my cattle with thirst?"
m.step("Exod.17.3")
# ‹וַיָּלֶן הָעָם עַל־מֹשֶׁה› (“and-stop the-people over Moses”) — fact
# holds: and-stop-the-people-over-Moses
m.fact("va_yalen_ha_am_al_moshe")

# -------------------------- Exod.17.4 · THEY_WILL_STONE_ME -----------------
# וַיִּצְעַק מֹשֶׁה אֶל־יְהוָה לֵאמֹר מָה אֶעֱשֶׂה לָעָם הַזֶּה עוֹד מְעַט
# וּסְקָלֻנִי
# "[EN-AID] And Moses cried to the LORD, saying: What shall I do for this
# people? Yet a little — and they will stone me."
m.step("Exod.17.4")
# ‹עוֹד מְעַט וּסְקָלֻנִי› (“still/again little and-be-weighty-me/my”) —
# fact holds: still/again-little-and-seqaluni
m.fact("od_meat_u_seqaluni")

# -------------------------- Exod.17.5 · PASS_BEFORE_THE_PEOPLE -------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה עֲבֹר לִפְנֵי הָעָם וְקַח אִתְּךָ מִזִּקְנֵי
# יִשְׂרָאֵל וּמַטְּךָ אֲשֶׁר הִכִּיתָ בּוֹ אֶת־הַיְאֹר קַח בְּיָדְךָ
# וְהָלָכְתָּ
# "[EN-AID] And the LORD said to Moses: Pass before the people, and take
# with you of the elders of Israel; and your staff, with which you struck
# the Nile, take in your hand — and go."
m.step("Exod.17.5")
# ‹עֲבֹר לִפְנֵי הָעָם וְקַח אִתְּךָ מִזִּקְנֵי יִשְׂרָאֵל› (“pass-over to-
# face the-people and-take with-you/your from-old Israel”) — the-LORD speaks
# a demand — LET: pass-over-lifne-the-people-and-strike
m.declare("YHWH", "LET",
          "avor_lifne_ha_am_ve_hikita")

# -------------------------- Exod.17.6 · THE_ROCK_AT_HOREB ------------------
# הִנְנִי עֹמֵד לְפָנֶיךָ שָּׁם עַל־הַצּוּר בְּחֹרֵב וְהִכִּיתָ בַצּוּר
# וְיָצְאוּ מִמֶּנּוּ מַיִם וְשָׁתָה הָעָם וַיַּעַשׂ כֵּן מֹשֶׁה לְעֵינֵי
# זִקְנֵי יִשְׂרָאֵל
# "[EN-AID] Behold, I stand before you there on the rock at Horeb; and you
# shall strike the rock, and water shall come out of it, and the people
# shall drink. And Moses did so before the eyes of the elders of Israel."
m.step("Exod.17.6")
# ‹וַיַּעַשׂ כֵּן מֹשֶׁה› (“and-make so Moses”) — demand settled (popped
# from the queue): pass-over-lifne-the-people-and-strike
m.result("avor_lifne_ha_am_ve_hikita", tmark="t1")
# ‹וְיָצְאוּ מִמֶּנּוּ מַיִם וְשָׁתָה הָעָם› (“and-bring-forth from-us/our
# waters and-drink the-people”) — demand settled (popped from the queue):
# set-lanu-waters
m.result("tenu_lanu_mayim", tmark="t1")

# -------------------------- Exod.17.7 · MASSAH_AND_MERIBAH -----------------
# וַיִּקְרָא שֵׁם הַמָּקוֹם מַסָּה וּמְרִיבָה עַל־רִיב בְּנֵי יִשְׂרָאֵל
# וְעַל נַסֹּתָם אֶת־יְהוָה לֵאמֹר הֲיֵשׁ יְהוָה בְּקִרְבֵּנוּ אִם־אָיִן
# "[EN-AID] And he called the name of the place Massah and Meribah, for the
# quarrel of the sons of Israel, and for their testing the LORD, saying: Is
# the LORD in our midst, or not?"
m.step("Exod.17.7")
# ‹וַיִּקְרָא שֵׁם הַמָּקוֹם מַסָּה וּמְרִיבָה› (“and-call name the-place
# Massah and-Meribah”) — named: place-refidim := Masa-and-Meriva
m.name("maqom_refidim", "Masa_u_Meriva")

# -------------------------- Exod.17.8 · AMALEK_COMES -----------------------
# וַיָּבֹא עֲמָלֵק וַיִּלָּחֶם עִם־יִשְׂרָאֵל בִּרְפִידִם
# "[EN-AID] And Amalek came, and fought with Israel in Rephidim."
m.step("Exod.17.8")
# ‹וַיָּבֹא עֲמָלֵק וַיִּלָּחֶם עִם־יִשְׂרָאֵל בִּרְפִידִם› (“and-come/bring
# Amalek and-feed-on with Israel in-Rephidim”) — event: milchemet-Amalek —
# agent Amalek; theme Israel
m.event("milchemet_amaleq", agent="amaleq", themes=["yisrael"])

# -------------------------- Exod.17.9 · CHOOSE_US_MEN ----------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־יְהוֹשֻׁעַ בְּחַר־לָנוּ אֲנָשִׁים וְצֵא הִלָּחֵם
# בַּעֲמָלֵק מָחָר אָנֹכִי נִצָּב עַל־רֹאשׁ הַגִּבְעָה וּמַטֵּה הָאֱלֹהִים
# בְּיָדִי
# "[EN-AID] And Moses said to Joshua: Choose us men, and go out, fight
# against Amalek; tomorrow I stand on the top of the hill, and the staff of
# God in my hand."
m.step("Exod.17.9")
# ‹בְּחַר־לָנוּ אֲנָשִׁים וְצֵא הִלָּחֵם בַּעֲמָלֵק› (“try to-us/our man
# and-bring-forth feed-on in-Amalek”) — Moses speaks a demand — LET: try-
# lanu-man-and-bring-forth
m.declare("moshe", "LET",
          "bechar_lanu_anashim_ve_tze")

# -------------------------- Exod.17.10 · UP_THE_HILL -----------------------
# וַיַּעַשׂ יְהוֹשֻׁעַ כַּאֲשֶׁר אָמַר־לוֹ מֹשֶׁה לְהִלָּחֵם בַּעֲמָלֵק
# וּמֹשֶׁה אַהֲרֹן וְחוּר עָלוּ רֹאשׁ הַגִּבְעָה
# "[EN-AID] And Joshua did as Moses had said to him, to fight against
# Amalek; and Moses, Aaron, and Hur went up the top of the hill."
m.step("Exod.17.10")
# ‹וַיַּעַשׂ יְהוֹשֻׁעַ כַּאֲשֶׁר אָמַר־לוֹ מֹשֶׁה› (“and-make Jehoshua
# like-as/which say to-him/its Moses”) — demand settled (popped from the
# queue): try-lanu-man-and-bring-forth
m.result("bechar_lanu_anashim_ve_tze", tmark="t1")

# -------------------------- Exod.17.11 · THE_HANDS_AND_THE_BATTLE ----------
# וְהָיָה כַּאֲשֶׁר יָרִים מֹשֶׁה יָדוֹ וְגָבַר יִשְׂרָאֵל וְכַאֲשֶׁר
# יָנִיחַ יָדוֹ וְגָבַר עֲמָלֵק
# "[EN-AID] And it was, when Moses would raise his hand, that Israel
# prevailed; and when he would rest his hand, that Amalek prevailed."
m.step("Exod.17.11")
# ‹וְהָיָה כַּאֲשֶׁר יָרִים מֹשֶׁה יָדוֹ וְגָבַר יִשְׂרָאֵל› (“and-be like-
# as/which rise-high Moses hand-him/its and-be-strong Israel”) — fact holds:
# like-which-rise-high-and-be-strong-Israel
m.fact("ka_asher_yarim_ve_gavar_yisrael")

# -------------------------- Exod.17.12 · HANDS_OF_FAITHFULNESS -------------
# וִידֵי מֹשֶׁה כְּבֵדִים וַיִּקְחוּ־אֶבֶן וַיָּשִׂימוּ תַחְתָּיו וַיֵּשֶׁב
# עָלֶיהָ וְאַהֲרֹן וְחוּר תָּמְכוּ בְיָדָיו מִזֶּה אֶחָד וּמִזֶּה אֶחָד
# וַיְהִי יָדָיו אֱמוּנָה עַד־בֹּא הַשָּׁמֶשׁ
# "[EN-AID] And Moses' hands were heavy; and they took a stone and put it
# under him, and he sat on it; and Aaron and Hur supported his hands, from
# this side one and from this side one; and his hands were faithfulness
# until the coming of the sun."
m.step("Exod.17.12")
# ‹וַיְהִי יָדָיו אֱמוּנָה עַד־בֹּא הַשָּׁמֶשׁ› (“and-be hand-him/its
# firmness until come/bring the-sun”) — fact holds: yadav-firmness-until-
# come/bring-the-sun
m.fact("yadav_emuna_ad_bo_ha_shamesh")

# -------------------------- Exod.17.13 · BY_THE_MOUTH_OF_THE_SWORD ---------
# וַיַּחֲלֹשׁ יְהוֹשֻׁעַ אֶת־עֲמָלֵק וְאֶת־עַמּוֹ לְפִי־חָרֶב
# "[EN-AID] And Joshua weakened Amalek and his people by the mouth of the
# sword."
m.step("Exod.17.13")
# ‹וַיַּחֲלֹשׁ יְהוֹשֻׁעַ אֶת־עֲמָלֵק וְאֶת־עַמּוֹ לְפִי־חָרֶב› (“and-
# prostrate Jehoshua obj-marker Amalek and-obj-marker people-him/its to-
# mouth drought”) — event: and-prostrate-Jehoshua — agent Jehoshua; theme
# Amalek
m.event("va_yachalosh_yehoshua", agent="yehoshua", themes=["amaleq"])

# -------------------------- Exod.17.14 · WRITE_THIS_IN_THE_BOOK ------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה כְּתֹב זֹאת זִכָּרוֹן בַּסֵּפֶר וְשִׂים
# בְּאָזְנֵי יְהוֹשֻׁעַ כִּי־מָחֹה אֶמְחֶה אֶת־זֵכֶר עֲמָלֵק מִתַּחַת
# הַשָּׁמָיִם
# "[EN-AID] And the LORD said to Moses: Write this, a memorial in the book,
# and set it in the ears of Joshua: that I will utterly blot out the memory
# of Amalek from under the heavens."
m.step("Exod.17.14")
# ‹כְּתֹב זֹאת זִכָּרוֹן בַּסֵּפֶר וְשִׂים בְּאָזְנֵי יְהוֹשֻׁעַ› (“grave
# this memento in-writing and-put/set in-broadness.-i.e.-the-ear Jehoshua”)
# — the-LORD speaks a demand — LET: grave-this-memento-in-the-sefer
m.declare("YHWH", "LET",
          "ketov_zot_zikaron_ba_sefer")

# -------------------------- Exod.17.15 · THE_LORD_IS_MY_BANNER -------------
# וַיִּבֶן מֹשֶׁה מִזְבֵּחַ וַיִּקְרָא שְׁמוֹ יְהוָה נִסִּי
# "[EN-AID] And Moses built an altar, and called its name: The LORD is my
# banner."
m.step("Exod.17.15")
# ‹וַיִּקְרָא שְׁמוֹ יְהוָה נִסִּי› (“and-call name-him/its Jehovah-Nissi-
# me/my”) — named: altar := the-LORD-Nisi
m.name("mizbeach", "YHWH_Nisi")

# -------------------------- Exod.17.16 · THE_THRONE_OATH -------------------
# וַיֹּאמֶר כִּי־יָד עַל־כֵּס יָהּ מִלְחָמָה לַיהוָה בַּעֲמָלֵק מִדֹּר דֹּר
# "[EN-AID] And he said: For a hand is upon the throne of YH — war for the
# LORD against Amalek, from generation to generation."
m.step("Exod.17.16")
# ‹וַיֹּאמֶר כִּי־יָד עַל־כֵּס יָהּ מִלְחָמָה לַיהוָה בַּעֲמָלֵק› (“and-say
# that hand over flag Jah battle to-YHWH in-Amalek”) — fact holds: battle-
# to-the-LORD-in-the-Amalek-from-generation-generation
m.fact("milchama_la_YHWH_ba_amaleq_mi_dor_dor")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'maqom_refidim': 'Masa_u_Meriva', 'mizbeach': 'YHWH_Nisi'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['ketov_zot_zikaron_ba_sefer']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yachanu_bi_refidim_ve_en_mayim', 'va_yalen_ha_am_al_moshe', 'od_meat_u_seqaluni', 'ka_asher_yarim_ve_gavar_yisrael', 'yadav_emuna_ad_bo_ha_shamesh', 'milchama_la_YHWH_ba_amaleq_mi_dor_dor'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
