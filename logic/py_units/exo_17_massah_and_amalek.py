#!/usr/bin/env python3
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
# ‹וַיִּסְעוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל› (“and-journey all congregation
# son Israel”)
# ‹מִמִּדְבַּר־סִין לְמַסְעֵיהֶם עַל־פִּי› (“from-pasture Sin to-departure-
# them/their over mouth”)
# ‹יְהוָה וַיַּחֲנוּ בִּרְפִידִים› (“YHWH and-encamp in-Rephidim”)
# ‹וְאֵין מַיִם לִשְׁתֹּת› (“and-there-is-not waters to-drink”)
# ‹הָעָם› (“the-people”)
# "[EN-AID] And all the congregation of the sons of Israel journeyed from
# the wilderness of Sin, by their journeys, according to the mouth of the
# LORD; and they camped in Rephidim — and there was no water for the people
# to drink."
m.step("Exod.17.1")
# ‹וַיַּחֲנוּ בִּרְפִידִים וְאֵין› (“and-encamp in-Rephidim and-there-is-
# not”)
# ‹מַיִם לִשְׁתֹּת הָעָם› (“waters to-drink the-people”)
# — fact holds: and-encamp-bi-refidim-and-there-is-not-waters
m.fact("va_yachanu_bi_refidim_ve_en_mayim")

# -------------------------- Exod.17.2 · GIVE_US_WATER ----------------------
# ‹וַיָּרֶב הָעָם עִם־מֹשֶׁה› (“and-toss the-people with Moses”)
# ‹וַיֹּאמְרוּ תְּנוּ־לָנוּ מַיִם› (“and-say set to-us/our waters”)
# ‹וְנִשְׁתֶּה וַיֹּאמֶר לָהֶם› (“and-drink and-say to-them/their”)
# ‹מֹשֶׁה מַה־תְּרִיבוּן עִמָּדִי› (“Moses what toss-ward along-with-me/my”)
# ‹מַה־תְּנַסּוּן אֶת־יְהוָה› (“what test-ward obj-marker YHWH”)
# "[EN-AID] And the people quarreled with Moses, and said: Give us water,
# that we may drink. And Moses said to them: Why do you quarrel with me? Why
# do you test the LORD?"
m.step("Exod.17.2")
# ‹תְּנוּ־לָנוּ מַיִם וְנִשְׁתֶּה› (“set to-us/our waters and-drink”)
# — the-people speaks a demand — LET: set-lanu-waters
m.declare("ha_am", "LET",
          "tenu_lanu_mayim")

# -------------------------- Exod.17.3 · WHY_DID_YOU_BRING_US_UP ------------
# ‹וַיִּצְמָא שָׁם הָעָם› (“and-thirst there the-people”)
# ‹לַמַּיִם וַיָּלֶן הָעָם› (“to-waters and-stop the-people”)
# ‹עַל־מֹשֶׁה וַיֹּאמֶר לָמָּה› (“over Moses and-say to-what”)
# ‹זֶּה הֶעֱלִיתָנוּ מִמִּצְרַיִם› (“this go-up-us/our from-Egypt”)
# ‹לְהָמִית אֹתִי וְאֶת־בָּנַי› (“to-die obj-marker-me/my and-obj-marker
# son-me/my”)
# ‹וְאֶת־מִקְנַי בַּצָּמָא› (“and-obj-marker something-bought-me/my in-
# thirst”)
# "[EN-AID] And the people thirsted there for water, and the people murmured
# against Moses, and said: Why is this — you brought us up from Egypt, to
# kill me and my sons and my cattle with thirst?"
m.step("Exod.17.3")
# ‹וַיָּלֶן הָעָם עַל־מֹשֶׁה› (“and-stop the-people over Moses”)
# — fact holds: and-stop-the-people-over-Moses
m.fact("va_yalen_ha_am_al_moshe")

# -------------------------- Exod.17.4 · THEY_WILL_STONE_ME -----------------
# ‹וַיִּצְעַק מֹשֶׁה אֶל־יְהוָה› (“and-shriek Moses to YHWH”)
# ‹לֵאמֹר מָה אֶעֱשֶׂה› (“to-say what make”)
# ‹לָעָם הַזֶּה עוֹד› (“to-people the-this still/again”)
# ‹מְעַט וּסְקָלֻנִי› (“little and-be-weighty-me/my”)
# "[EN-AID] And Moses cried to the LORD, saying: What shall I do for this
# people? Yet a little — and they will stone me."
m.step("Exod.17.4")
# ‹עוֹד מְעַט וּסְקָלֻנִי› (“still/again little and-be-weighty-me/my”)
# — fact holds: still/again-little-and-seqaluni
m.fact("od_meat_u_seqaluni")

# -------------------------- Exod.17.5 · PASS_BEFORE_THE_PEOPLE -------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹עֲבֹר לִפְנֵי הָעָם› (“pass-over to-face the-people”)
# ‹וְקַח אִתְּךָ מִזִּקְנֵי› (“and-take with-you/your from-old”)
# ‹יִשְׂרָאֵל וּמַטְּךָ אֲשֶׁר› (“Israel and-staff/tribe-you/your which”)
# ‹הִכִּיתָ בּוֹ אֶת־הַיְאֹר› (“strike in-him/its obj-marker the-Nile”)
# ‹קַח בְּיָדְךָ וְהָלָכְתָּ› (“take in-hand-you/your and-walk/go”)
# "[EN-AID] And the LORD said to Moses: Pass before the people, and take
# with you of the elders of Israel; and your staff, with which you struck
# the Nile, take in your hand — and go."
m.step("Exod.17.5")
# ‹עֲבֹר לִפְנֵי הָעָם› (“pass-over to-face the-people”)
# ‹וְקַח אִתְּךָ מִזִּקְנֵי› (“and-take with-you/your from-old”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — the-LORD speaks a demand — LET: pass-over-lifne-the-people-and-strike
m.declare("YHWH", "LET",
          "avor_lifne_ha_am_ve_hikita")

# -------------------------- Exod.17.6 · THE_ROCK_AT_HOREB ------------------
# ‹הִנְנִי עֹמֵד לְפָנֶיךָ› (“lo!-me/my stand to-face-you/your”)
# ‹שָּׁם עַל־הַצּוּר בְּחֹרֵב› (“there over the-cliff in-Horeb”)
# ‹וְהִכִּיתָ בַצּוּר וְיָצְאוּ› (“and-strike in-cliff and-bring-forth”)
# ‹מִמֶּנּוּ מַיִם וְשָׁתָה› (“from-us/our waters and-drink”)
# ‹הָעָם וַיַּעַשׂ כֵּן› (“the-people and-make so”)
# ‹מֹשֶׁה לְעֵינֵי זִקְנֵי› (“Moses to-eye old”)
# ‹יִשְׂרָאֵל› (“Israel”)
# "[EN-AID] Behold, I stand before you there on the rock at Horeb; and you
# shall strike the rock, and water shall come out of it, and the people
# shall drink. And Moses did so before the eyes of the elders of Israel."
m.step("Exod.17.6")
# ‹וַיַּעַשׂ כֵּן מֹשֶׁה› (“and-make so Moses”)
# — demand settled (popped from the queue): pass-over-lifne-the-people-and-
# strike
m.result("avor_lifne_ha_am_ve_hikita", tmark="t1")
# ‹וְיָצְאוּ מִמֶּנּוּ מַיִם› (“and-bring-forth from-us/our waters”)
# ‹וְשָׁתָה הָעָם› (“and-drink the-people”)
# — demand settled (popped from the queue): set-lanu-waters
m.result("tenu_lanu_mayim", tmark="t1")

# -------------------------- Exod.17.7 · MASSAH_AND_MERIBAH -----------------
# ‹וַיִּקְרָא שֵׁם הַמָּקוֹם› (“and-call name the-place”)
# ‹מַסָּה וּמְרִיבָה עַל־רִיב› (“Massah and-Meribah over contest”)
# ‹בְּנֵי יִשְׂרָאֵל וְעַל› (“son Israel and-over”)
# ‹נַסֹּתָם אֶת־יְהוָה לֵאמֹר› (“test-them/their obj-marker YHWH to-say”)
# ‹הֲיֵשׁ יְהוָה בְּקִרְבֵּנוּ› (“the-there-is YHWH in-nearest-part-us/our”)
# ‹אִם־אָיִן› (“if there-is-not”)
# "[EN-AID] And he called the name of the place Massah and Meribah, for the
# quarrel of the sons of Israel, and for their testing the LORD, saying: Is
# the LORD in our midst, or not?"
m.step("Exod.17.7")
# ‹וַיִּקְרָא שֵׁם הַמָּקוֹם› (“and-call name the-place”)
# ‹מַסָּה וּמְרִיבָה› (“Massah and-Meribah”)
# — named: place-refidim := Masa-and-Meriva
m.name("maqom_refidim", "Masa_u_Meriva")

# -------------------------- Exod.17.8 · AMALEK_COMES -----------------------
# ‹וַיָּבֹא עֲמָלֵק וַיִּלָּחֶם› (“and-come/bring Amalek and-feed-on”)
# ‹עִם־יִשְׂרָאֵל בִּרְפִידִם› (“with Israel in-Rephidim”)
# "[EN-AID] And Amalek came, and fought with Israel in Rephidim."
m.step("Exod.17.8")
# ‹וַיָּבֹא עֲמָלֵק וַיִּלָּחֶם› (“and-come/bring Amalek and-feed-on”)
# ‹עִם־יִשְׂרָאֵל בִּרְפִידִם› (“with Israel in-Rephidim”)
# — event: milchemet-Amalek — agent Amalek; theme Israel
m.event("milchemet_amaleq", agent="amaleq", themes=["yisrael"])

# -------------------------- Exod.17.9 · CHOOSE_US_MEN ----------------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־יְהוֹשֻׁעַ› (“and-say Moses to Jehoshua”)
# ‹בְּחַר־לָנוּ אֲנָשִׁים וְצֵא› (“try to-us/our man and-bring-forth”)
# ‹הִלָּחֵם בַּעֲמָלֵק מָחָר› (“feed-on in-Amalek deferred”)
# ‹אָנֹכִי נִצָּב עַל־רֹאשׁ› (“stand over head”)
# ‹הַגִּבְעָה וּמַטֵּה הָאֱלֹהִים› (“the-hillock and-staff/tribe the-God”)
# ‹בְּיָדִי› (“in-hand-me/my”)
# "[EN-AID] And Moses said to Joshua: Choose us men, and go out, fight
# against Amalek; tomorrow I stand on the top of the hill, and the staff of
# God in my hand."
m.step("Exod.17.9")
# ‹בְּחַר־לָנוּ אֲנָשִׁים וְצֵא› (“try to-us/our man and-bring-forth”)
# ‹הִלָּחֵם בַּעֲמָלֵק› (“feed-on in-Amalek”)
# — Moses speaks a demand — LET: try-lanu-man-and-bring-forth
m.declare("moshe", "LET",
          "bechar_lanu_anashim_ve_tze")

# -------------------------- Exod.17.10 · UP_THE_HILL -----------------------
# ‹וַיַּעַשׂ יְהוֹשֻׁעַ כַּאֲשֶׁר› (“and-make Jehoshua like-as/which”)
# ‹אָמַר־לוֹ מֹשֶׁה לְהִלָּחֵם› (“say to-him/its Moses to-feed-on”)
# ‹בַּעֲמָלֵק וּמֹשֶׁה אַהֲרֹן› (“in-Amalek and-Moses Aaron”)
# ‹וְחוּר עָלוּ רֹאשׁ› (“and-Hur go-up head”)
# ‹הַגִּבְעָה› (“the-hillock”)
# "[EN-AID] And Joshua did as Moses had said to him, to fight against
# Amalek; and Moses, Aaron, and Hur went up the top of the hill."
m.step("Exod.17.10")
# ‹וַיַּעַשׂ יְהוֹשֻׁעַ כַּאֲשֶׁר› (“and-make Jehoshua like-as/which”)
# ‹אָמַר־לוֹ מֹשֶׁה› (“say to-him/its Moses”)
# — demand settled (popped from the queue): try-lanu-man-and-bring-forth
m.result("bechar_lanu_anashim_ve_tze", tmark="t1")

# -------------------------- Exod.17.11 · THE_HANDS_AND_THE_BATTLE ----------
# ‹וְהָיָה כַּאֲשֶׁר יָרִים› (“and-be like-as/which rise-high”)
# ‹מֹשֶׁה יָדוֹ וְגָבַר› (“Moses hand-him/its and-be-strong”)
# ‹יִשְׂרָאֵל וְכַאֲשֶׁר יָנִיחַ› (“Israel and-like-as/which rest”)
# ‹יָדוֹ וְגָבַר עֲמָלֵק› (“hand-him/its and-be-strong Amalek”)
# "[EN-AID] And it was, when Moses would raise his hand, that Israel
# prevailed; and when he would rest his hand, that Amalek prevailed."
m.step("Exod.17.11")
# ‹וְהָיָה כַּאֲשֶׁר יָרִים› (“and-be like-as/which rise-high”)
# ‹מֹשֶׁה יָדוֹ וְגָבַר› (“Moses hand-him/its and-be-strong”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — fact holds: like-which-rise-high-and-be-strong-Israel
m.fact("ka_asher_yarim_ve_gavar_yisrael")
# witness-tier presupposed read: instrument_reading on raised_hands — read,
# not installed
m.witness_read("raised_hands", "instrument_reading",
                cites=["Mishnah Rosh Hashanah 3:8"])

# -------------------------- Exod.17.12 · HANDS_OF_FAITHFULNESS -------------
# ‹וִידֵי מֹשֶׁה כְּבֵדִים› (“and-hand Moses heavy”)
# ‹וַיִּקְחוּ־אֶבֶן וַיָּשִׂימוּ תַחְתָּיו› (“and-take stone and-put/set
# under-him/its”)
# ‹וַיֵּשֶׁב עָלֶיהָ וְאַהֲרֹן› (“and-dwell/sit over-her/its and-Aaron”)
# ‹וְחוּר תָּמְכוּ בְיָדָיו› (“and-Hur sustain in-hand-him/its”)
# ‹מִזֶּה אֶחָד וּמִזֶּה› (“from-this one and-from-this”)
# ‹אֶחָד וַיְהִי יָדָיו› (“one and-be hand-him/its”)
# ‹אֱמוּנָה עַד־בֹּא הַשָּׁמֶשׁ› (“firmness until come/bring the-sun”)
# "[EN-AID] And Moses' hands were heavy; and they took a stone and put it
# under him, and he sat on it; and Aaron and Hur supported his hands, from
# this side one and from this side one; and his hands were faithfulness
# until the coming of the sun."
m.step("Exod.17.12")
# ‹וַיְהִי יָדָיו אֱמוּנָה› (“and-be hand-him/its firmness”)
# ‹עַד־בֹּא הַשָּׁמֶשׁ› (“until come/bring the-sun”)
# — fact holds: yadav-firmness-until-come/bring-the-sun
m.fact("yadav_emuna_ad_bo_ha_shamesh")

# -------------------------- Exod.17.13 · BY_THE_MOUTH_OF_THE_SWORD ---------
# ‹וַיַּחֲלֹשׁ יְהוֹשֻׁעַ אֶת־עֲמָלֵק› (“and-prostrate Jehoshua obj-marker
# Amalek”)
# ‹וְאֶת־עַמּוֹ לְפִי־חָרֶב› (“and-obj-marker people-him/its to-mouth
# drought”)
# "[EN-AID] And Joshua weakened Amalek and his people by the mouth of the
# sword."
m.step("Exod.17.13")
# ‹וַיַּחֲלֹשׁ יְהוֹשֻׁעַ אֶת־עֲמָלֵק› (“and-prostrate Jehoshua obj-marker
# Amalek”)
# ‹וְאֶת־עַמּוֹ לְפִי־חָרֶב› (“and-obj-marker people-him/its to-mouth
# drought”)
# — event: and-prostrate-Jehoshua — agent Jehoshua; theme Amalek
m.event("va_yachalosh_yehoshua", agent="yehoshua", themes=["amaleq"])

# -------------------------- Exod.17.14 · WRITE_THIS_IN_THE_BOOK ------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹כְּתֹב זֹאת זִכָּרוֹן› (“grave this memento”)
# ‹בַּסֵּפֶר וְשִׂים בְּאָזְנֵי› (“in-writing and-put/set in-
# broadness.-i.e.-the-ear”)
# ‹יְהוֹשֻׁעַ כִּי־מָחֹה אֶמְחֶה› (“Jehoshua that stroke stroke”)
# ‹אֶת־זֵכֶר עֲמָלֵק מִתַּחַת› (“obj-marker memento Amalek from-under”)
# ‹הַשָּׁמָיִם› (“the-heavens”)
# "[EN-AID] And the LORD said to Moses: Write this, a memorial in the book,
# and set it in the ears of Joshua: that I will utterly blot out the memory
# of Amalek from under the heavens."
m.step("Exod.17.14")
# ‹כְּתֹב זֹאת זִכָּרוֹן› (“grave this memento”)
# ‹בַּסֵּפֶר וְשִׂים בְּאָזְנֵי› (“in-writing and-put/set in-
# broadness.-i.e.-the-ear”)
# ‹יְהוֹשֻׁעַ› (“Jehoshua”)
# — the-LORD speaks a demand — LET: grave-this-memento-in-the-sefer
m.declare("YHWH", "LET",
          "ketov_zot_zikaron_ba_sefer")

# -------------------------- Exod.17.15 · THE_LORD_IS_MY_BANNER -------------
# ‹וַיִּבֶן מֹשֶׁה מִזְבֵּחַ› (“and-build Moses altar”)
# ‹וַיִּקְרָא שְׁמוֹ יְהוָה› (“and-call name-him/its”)
# ‹נִסִּי› (“Jehovah-Nissi-me/my”)
# "[EN-AID] And Moses built an altar, and called its name: The LORD is my
# banner."
m.step("Exod.17.15")
# ‹וַיִּקְרָא שְׁמוֹ יְהוָה› (“and-call name-him/its”)
# ‹נִסִּי› (“Jehovah-Nissi-me/my”)
# — named: altar := the-LORD-Nisi
m.name("mizbeach", "YHWH_Nisi")

# -------------------------- Exod.17.16 · THE_THRONE_OATH -------------------
# ‹וַיֹּאמֶר כִּי־יָד עַל־כֵּס› (“and-say that hand over flag”)
# ‹יָהּ מִלְחָמָה לַיהוָה› (“Jah battle to-YHWH”)
# ‹בַּעֲמָלֵק מִדֹּר דֹּר› (“in-Amalek from-generation generation”)
# "[EN-AID] And he said: For a hand is upon the throne of YH — war for the
# LORD against Amalek, from generation to generation."
m.step("Exod.17.16")
# ‹וַיֹּאמֶר כִּי־יָד עַל־כֵּס› (“and-say that hand over flag”)
# ‹יָהּ מִלְחָמָה לַיהוָה› (“Jah battle to-YHWH”)
# ‹בַּעֲמָלֵק› (“in-Amalek”)
# — fact holds: battle-to-the-LORD-in-the-Amalek-from-generation-generation
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('raised_hands', 'instrument_reading')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Rosh Hashanah 3:8']
    assert all('instrument_reading' not in f for f in m.WORLD["facts"])
    assert 'raised_hands' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
