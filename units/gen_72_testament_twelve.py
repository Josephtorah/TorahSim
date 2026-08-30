#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_72_testament_twelve — 49:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_72_testament_twelve.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The testament of the twelve (49:1-33)"""
from machine import Machine

m = Machine("gen_72_testament_twelve")

# -------------------------- Gen.49.1 · GATHER_AND_I_WILL_TELL --------------
# וַיִּקְרָא יַעֲקֹב אֶל־בָּנָיו וַיֹּאמֶר הֵאָסְפוּ וְאַגִּידָה לָכֶם אֵת
# אֲשֶׁר־יִקְרָא אֶתְכֶם בְּאַחֲרִית הַיָּמִים
# "[EN-AID] And Jacob called to his sons, and said: Gather, and I will tell
# you that which shall befall you in the end of days."
m.step("Gen.49.1")
# ‹הֵאָסְפוּ וְאַגִּידָה לָכֶם› (“gather-for-any-purpose and-tell to-
# you/your(pl)”) — section divre-Jacob-to-vanav: son-Leah, son-the-
# shefachot, son-rachel
m.section("divre_yaaqov_le_vanav", "bene_lea", "bene_ha_shefachot", "bene_rachel")
# witness-grounded state (its own tier): revealed_then_sealed_mid_sentence
# on the_end_of_days
m.witness_state("the_end_of_days", "revealed_then_sealed_mid_sentence",
                cites=["Bereshit Rabbah 98:2", "Bereshit Rabbah 99:5"])

# -------------------------- Gen.49.2 · HEAR_TO_ISRAEL_YOUR_FATHER ----------
# הִקָּבְצוּ וְשִׁמְעוּ בְּנֵי יַעֲקֹב וְשִׁמְעוּ אֶל־יִשְׂרָאֵל אֲבִיכֶם
# "[EN-AID] Assemble and hear, sons of Jacob; and hear to Israel your
# father."
m.step("Gen.49.2")
# ‹וְשִׁמְעוּ אֶל־יִשְׂרָאֵל אֲבִיכֶם› (“and-hear to Israel father-
# you/your(pl)”) — fact holds: hear-to-Israel-avikhem
m.fact("shimu_el_yisrael_avikhem")
# witness-tier presupposed read: the_daily_liturgy_sourced_to_this_verse on
# hear_israel_your_father — read, not installed
m.witness_read("hear_israel_your_father", "the_daily_liturgy_sourced_to_this_verse",
                cites=["Bereshit Rabbah 98:3", "Onkelos Genesis 49:2"])

# -------------------------- Gen.49.3 · REUBEN_MY_FIRSTBORN -----------------
# רְאוּבֵן בְּכֹרִי אַתָּה כֹּחִי וְרֵאשִׁית אוֹנִי יֶתֶר שְׂאֵת וְיֶתֶר עָז
# "[EN-AID] Reuben, my firstborn are you — my strength and the first of my
# vigor: excess of dignity and excess of power."
m.step("Gen.49.3")
# ‹רְאוּבֵן בְּכֹרִי אַתָּה› (“Reuben firstborn-me/my you”) — fact holds:
# Reuben-bekhori-you
m.fact("reuven_bekhori_ata")

# -------------------------- Gen.49.4 · UNSTABLE_AS_WATER -------------------
# פַּחַז כַּמַּיִם אַל־תּוֹתַר כִּי עָלִיתָ מִשְׁכְּבֵי אָבִיךָ אָז
# חִלַּלְתָּ יְצוּעִי עָלָה
# "[EN-AID] Unstable as water, you shall not excel — for you went up to your
# father's bed; then you profaned — he went up to my couch!"
m.step("Gen.49.4")
# ‹פַּחַז כַּמַּיִם אַל־תּוֹתַר› (“ebullition like-waters do-not jut-over”)
# — fact holds: ebullition-like-waters-over-jut-over
m.fact("pachaz_ka_mayim_al_totar")

# -------------------------- Gen.49.5 · SIMEON_AND_LEVI_BROTHERS ------------
# שִׁמְעוֹן וְלֵוִי אַחִים כְּלֵי חָמָס מְכֵרֹתֵיהֶם
# "[EN-AID] Simeon and Levi are brothers — instruments of violence their
# trade."
m.step("Gen.49.5")
# ‹שִׁמְעוֹן וְלֵוִי אַחִים› (“Simeon and-Levi brother”) — fact holds:
# Simeon-and-Levi-brother
m.fact("shimon_ve_levi_achim")

# -------------------------- Gen.49.6 · LET_MY_HONOR_NOT_UNITE --------------
# בְּסֹדָם אַל־תָּבֹא נַפְשִׁי בִּקְהָלָם אַל־תֵּחַד כְּבֹדִי כִּי בְאַפָּם
# הָרְגוּ אִישׁ וּבִרְצֹנָם עִקְּרוּ־שׁוֹר
# "[EN-AID] Into their council let my soul not come; with their assembly let
# my honor not unite — for in their anger they killed a man, and in their
# pleasure they hamstrung an ox."
m.step("Gen.49.6")
# ‹בִּקְהָלָם אַל־תֵּחַד כְּבֹדִי› (“in-assemblage-them/their do-not be-one
# weight-me/my”) — fact holds: bi-qhalam-over-be-one-kevodi
m.fact("bi_qhalam_al_techad_kevodi")
# witness-grounded state (its own tier): three_layers_standing_on_one_verse
# on they_hamstrung_an_ox
m.witness_state("they_hamstrung_an_ox", "three_layers_standing_on_one_verse",
                cites=["Bereshit Rabbah 98:5", "Onkelos Genesis 49:5"])

# -------------------------- Gen.49.7 · CURSED_THEIR_ANGER ------------------
# אָרוּר אַפָּם כִּי עָז וְעֶבְרָתָם כִּי קָשָׁתָה אֲחַלְּקֵם בְּיַעֲקֹב
# וַאֲפִיצֵם בְּיִשְׂרָאֵל
# "[EN-AID] Cursed be their anger, for it is fierce, and their fury, for it
# is hard: I will divide them in Jacob, and scatter them in Israel."
m.step("Gen.49.7")
# ‹אֲחַלְּקֵם בְּיַעֲקֹב וַאֲפִיצֵם בְּיִשְׂרָאֵל› (“be-smooth-them/their
# in-Jacob and-dash-in-pieces-them/their in-Israel”) — fact holds: achalqem-
# in-Jacob-and-afitzem-in-Israel
m.fact("achalqem_be_yaaqov_va_afitzem_be_yisrael")

# -------------------------- Gen.49.8 · JUDAH_YOUR_BROTHERS_PRAISE_YOU ------
# יְהוּדָה אַתָּה יוֹדוּךָ אַחֶיךָ יָדְךָ בְּעֹרֶף אֹיְבֶיךָ יִשְׁתַּחֲוּוּ
# לְךָ בְּנֵי אָבִיךָ
# "[EN-AID] Judah — you, your brothers shall praise you; your hand on the
# neck of your enemies; the sons of your father shall bow to you."
m.step("Gen.49.8")
# ‹יְהוּדָה אַתָּה יוֹדוּךָ אַחֶיךָ› (“Judah you physically-you/your
# brother-you/your”) — fact holds: yodukha-achekha
m.fact("yodukha_achekha")
# witness-tier presupposed read: the_name_read_to_the_confession on
# your_brothers_shall_praise_you — read, not installed
m.witness_read("your_brothers_shall_praise_you", "the_name_read_to_the_confession",
                cites=["Onkelos Genesis 49:8", "Bereshit Rabbah 98:7"])

# -------------------------- Gen.49.9 · LION_WHELP_JUDAH --------------------
# גּוּר אַרְיֵה יְהוּדָה מִטֶּרֶף בְּנִי עָלִיתָ כָּרַע רָבַץ כְּאַרְיֵה
# וּכְלָבִיא מִי יְקִימֶנּוּ
# "[EN-AID] A lion's whelp is Judah — from the prey, my son, you went up; he
# crouched, he lay as a lion, and as a lioness — who shall raise him?"
m.step("Gen.49.9")
# ‹מִטֶּרֶף בְּנִי עָלִיתָ› (“from-something-torn son-me/my go-up”) — fact
# holds: who?-something-torn-son-go-up
m.fact("mi_teref_beni_alita")

# -------------------------- Gen.49.10 · UNTIL_SHILOH_COMES -----------------
# לֹא־יָסוּר שֵׁבֶט מִיהוּדָה וּמְחֹקֵק מִבֵּין רַגְלָיו עַד כִּי־יָבֹא שילה
# שִׁילוֹ וְלוֹ יִקְּהַת עַמִּים
# "[EN-AID] The scepter shall not depart from Judah, nor the ruler's staff
# from between his feet, until Shiloh comes; and to him the obedience of
# peoples."
m.step("Gen.49.10")
# ‹לֹא־יָסוּר שֵׁבֶט מִיהוּדָה וּמְחֹקֵק מִבֵּין רַגְלָיו› (“not turn-aside
# scion from-Judah and-hack from-between foot-him/its”) — fact holds: not-
# turn-aside-scion-who?-Judah-until-that-come/bring-Shiloh
m.fact("lo_yasur_shevet_mi_yhuda_ad_ki_yavo_shilo")
# witness-tier presupposed read: a_place_name_resolved_into_a_person on
# until_shiloh_comes — read, not installed
m.witness_read("until_shiloh_comes", "a_place_name_resolved_into_a_person",
                cites=["Onkelos Genesis 49:10", "Bereshit Rabbah 98:8"])

# -------------------------- Gen.49.11 · BINDING_HIS_FOAL_TO_THE_VINE -------
# אֹסְרִי לַגֶּפֶן עירה עִירוֹ וְלַשֹּׂרֵקָה בְּנִי אֲתֹנוֹ כִּבֵּס
# בַּיַּיִן לְבֻשׁוֹ וּבְדַם־עֲנָבִים סותה סוּתוֹ
# "[EN-AID] Binding his foal to the vine, and his donkey's colt to the
# choice tendril; he washes his garment in wine, and his robe in the blood
# of grapes."
m.step("Gen.49.11")
# ‹אֹסְרִי לַגֶּפֶן עירה עִירוֹ› (“yoke to-vine young-ass-him/its young-ass-
# him/its”) — fact holds: yoke-to-vine-iro
m.fact("osri_la_gefen_iro")

# -------------------------- Gen.49.12 · EYES_DARK_FROM_WINE ----------------
# חַכְלִילִי עֵינַיִם מִיָּיִן וּלְבֶן־שִׁנַּיִם מֵחָלָב
# "[EN-AID] Eyes darkened from wine, and teeth white from milk."
m.step("Gen.49.12")
# ‹חַכְלִילִי עֵינַיִם מִיָּיִן› (“darkly-flashing eye from-wine”) — fact
# holds: darkly-flashing-eye-who?-wine
m.fact("chakhlili_enayim_mi_yayin")

# -------------------------- Gen.49.13 · ZEBULUN_AT_THE_SHORE ---------------
# זְבוּלֻן לְחוֹף יַמִּים יִשְׁכֹּן וְהוּא לְחוֹף אֳנִיּוֹת וְיַרְכָתוֹ
# עַל־צִידֹן
# "[EN-AID] Zebulun shall dwell at the shore of seas — and he is at the
# shore of ships, and his flank upon Sidon."
m.step("Gen.49.13")
# ‹זְבוּלֻן לְחוֹף יַמִּים יִשְׁכֹּן› (“Zebulun to-cove seas reside”) — fact
# holds: Zebulun-to-cove-day-reside
m.fact("zevulun_le_chof_yamim_yishkon")
# witness-tier presupposed read: a_prophets_parentage_and_a_patronage_rule
# on zebulun_at_the_shore — read, not installed
m.witness_read("zebulun_at_the_shore", "a_prophets_parentage_and_a_patronage_rule",
                cites=["Bereshit Rabbah 98:11", "Bereshit Rabbah 99:9"])

# -------------------------- Gen.49.14 · ISSACHAR_STRONG_DONKEY -------------
# יִשָּׂשכָר חֲמֹר גָּרֶם רֹבֵץ בֵּין הַמִּשְׁפְּתָיִם
# "[EN-AID] Issachar is a strong-boned donkey, crouching between the
# sheepfolds."
m.step("Gen.49.14")
# ‹יִשָּׂשכָר חֲמֹר גָּרֶם› (“Issachar male-ass bone”) — fact holds:
# Issachar-male-ass-bone
m.fact("yisashkhar_chamor_garem")

# -------------------------- Gen.49.15 · HE_BENT_HIS_SHOULDER ---------------
# וַיַּרְא מְנֻחָה כִּי טוֹב וְאֶת־הָאָרֶץ כִּי נָעֵמָה וַיֵּט שִׁכְמוֹ
# לִסְבֹּל וַיְהִי לְמַס־עֹבֵד
# "[EN-AID] And he saw a resting-place, that it was good, and the land, that
# it was pleasant; and he bent his shoulder to bear, and became a toiling
# serf."
m.step("Gen.49.15")
# ‹וַיֵּט שִׁכְמוֹ לִסְבֹּל› (“and-stretch neck-as-the-place-of-burden-
# him/its to-carry”) — fact holds: and-stretch-shikhmo-lisbol
m.fact("va_yet_shikhmo_lisbol")

# -------------------------- Gen.49.16 · DAN_SHALL_JUDGE --------------------
# דָּן יָדִין עַמּוֹ כְּאַחַד שִׁבְטֵי יִשְׂרָאֵל
# "[EN-AID] Dan shall judge his people, as one of the tribes of Israel."
m.step("Gen.49.16")
# ‹דָּן יָדִין עַמּוֹ› (“Daniel straight-course people-him/its”) — fact
# holds: Daniel-straight-course-amo
m.fact("dan_yadin_amo")

# -------------------------- Gen.49.17 · SERPENT_ON_THE_WAY -----------------
# יְהִי־דָן נָחָשׁ עֲלֵי־דֶרֶךְ שְׁפִיפֹן עֲלֵי־אֹרַח הַנֹּשֵׁךְ
# עִקְּבֵי־סוּס וַיִּפֹּל רֹכְבוֹ אָחוֹר
# "[EN-AID] May Dan be a serpent on the way, a horned viper on the path —
# that bites the horse's heels, and its rider falls backward."
m.step("Gen.49.17")
# ‹הַנֹּשֵׁךְ עִקְּבֵי־סוּס› (“the-strike-with-a-sting heel horse”) — fact
# holds: the-strike-with-a-sting-heel-horse
m.fact("ha_noshekh_iqve_sus")
# witness-grounded state (its own tier):
# the_blessings_distributed_then_pooled on dan_a_serpent
m.witness_state("dan_a_serpent", "the_blessings_distributed_then_pooled",
                cites=["Bereshit Rabbah 99:4"])

# -------------------------- Gen.49.18 · FOR_YOUR_SALVATION_I_WAIT ----------
# לִישׁוּעָתְךָ קִוִּיתִי יְהוָה
# "[EN-AID] For Your salvation I wait, O LORD."
m.step("Gen.49.18")
# ‹לִישׁוּעָתְךָ קִוִּיתִי יְהוָה› (“to-something-saved-you/your bind-
# together YHWH”) — fact holds: to-me-yshuatkha-bind-together-the-LORD
m.fact("li_yshuatkha_qiviti_YHWH")
# witness-grounded state (its own tier): one_cry_and_two_destinations on
# for_your_salvation_i_hope
m.witness_state("for_your_salvation_i_hope", "one_cry_and_two_destinations",
                cites=["Bereshit Rabbah 98:14", "Bereshit Rabbah 99:11"])

# -------------------------- Gen.49.19 · GAD_RAIDERS_RAID_HIM ---------------
# גָּד גְּדוּד יְגוּדֶנּוּ וְהוּא יָגֻד עָקֵב
# "[EN-AID] Gad — a raiding troop shall raid him; and he shall raid at the
# heel."
m.step("Gen.49.19")
# ‹גָּד גְּדוּד יְגוּדֶנּוּ› (“Gad crowd crowd-upon-him/its”) — fact holds:
# Gad-crowd-yegudenu
m.fact("gad_gedud_yegudenu")

# -------------------------- Gen.49.20 · ASHERS_BREAD_IS_RICH ---------------
# מֵאָשֵׁר שְׁמֵנָה לַחְמוֹ וְהוּא יִתֵּן מַעֲדַנֵּי־מֶלֶךְ
# "[EN-AID] From Asher — his bread is rich; and he shall give king's
# delicacies."
m.step("Gen.49.20")
# ‹מֵאָשֵׁר שְׁמֵנָה לַחְמוֹ› (“from-Asher greasy food-him/its”) — fact
# holds: from-which-greasy-lachmo
m.fact("me_asher_shemena_lachmo")

# -------------------------- Gen.49.21 · NAPHTALI_A_HIND_SENT_FORTH ---------
# נַפְתָּלִי אַיָּלָה שְׁלֻחָה הַנֹּתֵן אִמְרֵי־שָׁפֶר
# "[EN-AID] Naphtali is a hind sent forth, who gives fair sayings."
m.step("Gen.49.21")
# ‹אַיָּלָה שְׁלֻחָה הַנֹּתֵן אִמְרֵי־שָׁפֶר› (“doe send the-set something-
# said beauty”) — fact holds: doe-send-the-set-something-said-beauty
m.fact("ayala_shelucha_ha_noten_imre_shafer")

# -------------------------- Gen.49.22 · FRUITFUL_SON_BY_THE_SPRING ---------
# בֵּן פֹּרָת יוֹסֵף בֵּן פֹּרָת עֲלֵי־עָיִן בָּנוֹת צָעֲדָה עֲלֵי־שׁוּר
# "[EN-AID] A fruitful son is Joseph, a fruitful son by the spring —
# daughters marched upon the wall."
m.step("Gen.49.22")
# ‹בֵּן פֹּרָת יוֹסֵף› (“son be-fruitful Joseph”) — fact holds: between-be-
# fruitful-Joseph
m.fact("ben_porat_yosef")

# -------------------------- Gen.49.23 · THE_ARCHERS_EMBITTERED_HIM ---------
# וַיְמָרֲרֻהוּ וָרֹבּוּ וַיִּשְׂטְמֻהוּ בַּעֲלֵי חִצִּים
# "[EN-AID] And they embittered him, and shot, and hated him — the masters
# of arrows."
m.step("Gen.49.23")
# ‹וַיְמָרֲרֻהוּ וָרֹבּוּ וַיִּשְׂטְמֻהוּ› (“and-be-bitter-him/its and-
# shoot-an-arrow and-lurk-for-him/its”) — fact holds: and-yemararuhu-and-
# shoot-an-arrow
m.fact("va_yemararuhu_va_robu")
# witness-tier presupposed read: the_slander_model_stated_in_full on
# they_embittered_him_and_shot_at_him — read, not installed
m.witness_read("they_embittered_him_and_shot_at_him", "the_slander_model_stated_in_full",
                cites=["Bereshit Rabbah 98:19"])

# -------------------------- Gen.49.24 · HIS_BOW_STAYED_FIRM ----------------
# וַתֵּשֶׁב בְּאֵיתָן קַשְׁתּוֹ וַיָּפֹזּוּ זְרֹעֵי יָדָיו מִידֵי אֲבִיר
# יַעֲקֹב מִשָּׁם רֹעֶה אֶבֶן יִשְׂרָאֵל
# "[EN-AID] And his bow stayed in strength, and the arms of his hands were
# made agile — from the hands of the Mighty One of Jacob, from there, the
# Shepherd, the Stone of Israel."
m.step("Gen.49.24")
# ‹וַתֵּשֶׁב בְּאֵיתָן קַשְׁתּוֹ› (“and-dwell/sit in-permanence bow-
# him/its”) — fact holds: and-dwell/sit-in-permanence-qashto
m.fact("va_teshev_be_etan_qashto")
# witness-tier presupposed read: one_noun_read_three_ways on
# his_bow_abode_in_strength — read, not installed
m.witness_read("his_bow_abode_in_strength", "one_noun_read_three_ways",
                cites=["Onkelos Genesis 49:24", "Bereshit Rabbah 98:20"])

# -------------------------- Gen.49.25 · BLESSINGS_OF_HEAVEN_AND_DEEP -------
# מֵאֵל אָבִיךָ וְיַעְזְרֶךָּ וְאֵת שַׁדַּי וִיבָרְכֶךָּ בִּרְכֹת שָׁמַיִם
# מֵעָל בִּרְכֹת תְּהוֹם רֹבֶצֶת תָּחַת בִּרְכֹת שָׁדַיִם וָרָחַם
# "[EN-AID] From the God of your father — may He help you — and with Shaddai
# — may He bless you: blessings of heaven above, blessings of the deep
# crouching below, blessings of breasts and womb."
m.step("Gen.49.25")
# ‹בִּרְכֹת שָׁמַיִם מֵעָל› (“blessing heavens from-over”) — fact holds:
# blessing-heavens-from-over
m.fact("birkhot_shamayim_me_al")

# -------------------------- Gen.49.26 · CROWN_OF_THE_SET_APART -------------
# בִּרְכֹת אָבִיךָ גָּבְרוּ עַל־בִּרְכֹת הוֹרַי עַד־תַּאֲוַת גִּבְעֹת עוֹלָם
# תִּהְיֶין לְרֹאשׁ יוֹסֵף וּלְקָדְקֹד נְזִיר אֶחָיו
# "[EN-AID] The blessings of your father have prevailed above the blessings
# of my parents, to the utmost bound of the everlasting hills: may they be
# for the head of Joseph, and for the crown of the one set apart from his
# brothers."
m.step("Gen.49.26")
# ‹תִּהְיֶין לְרֹאשׁ יוֹסֵף› (“be to-head Joseph”) — fact holds: tihyena-to-
# head-Joseph
m.fact("tihyena_le_rosh_yosef")

# -------------------------- Gen.49.27 · BENJAMIN_TEARING_WOLF --------------
# בִּנְיָמִין זְאֵב יִטְרָף בַּבֹּקֶר יֹאכַל עַד וְלָעֶרֶב יְחַלֵּק שָׁלָל
# "[EN-AID] Benjamin is a wolf that tears: in the morning he devours spoil,
# and at evening he divides plunder."
m.step("Gen.49.27")
# ‹בִּנְיָמִין זְאֵב יִטְרָף› (“Benjamin wolf pluck-off”) — fact holds:
# Benjamin-wolf-pluck-off
m.fact("binyamin_zeev_yitraf")
# witness-tier presupposed read:
# the_sanctuary_awarded_by_absence_from_a_crime on benjamin_a_ravening_wolf
# — read, not installed
m.witness_read("benjamin_a_ravening_wolf", "the_sanctuary_awarded_by_absence_from_a_crime",
                cites=["Bereshit Rabbah 99:1", "Onkelos Genesis 49:27", "Bereshit Rabbah 99:3"])

# -------------------------- Gen.49.28 · EACH_BY_HIS_BLESSING ---------------
# כָּל־אֵלֶּה שִׁבְטֵי יִשְׂרָאֵל שְׁנֵים עָשָׂר וְזֹאת אֲשֶׁר־דִּבֶּר לָהֶם
# אֲבִיהֶם וַיְבָרֶךְ אוֹתָם אִישׁ אֲשֶׁר כְּבִרְכָתוֹ בֵּרַךְ אֹתָם
# "[EN-AID] All these are the tribes of Israel, twelve; and this is what
# their father spoke to them, and he blessed them — each man according to
# his blessing he blessed them."
m.step("Gen.49.28")
# ‹כָּל־אֵלֶּה שִׁבְטֵי יִשְׂרָאֵל שְׁנֵים עָשָׂר› (“all these scion Israel
# two -teen”) — blessing: Jacob blesses scion-Israel-two--teen
m.bless("yaaqov", "shivte_yisrael_shenem_asar")
# witness-grounded state (its own tier):
# ceasing_to_translate_for_one_chapter on the_translation_itself
m.witness_state("the_translation_itself", "ceasing_to_translate_for_one_chapter",
                cites=["Onkelos Genesis 49:13", "Onkelos Genesis 49:10", "Onkelos Genesis 49:27"])

# -------------------------- Gen.49.29 · BURY_ME_WITH_MY_FATHERS ------------
# וַיְצַו אוֹתָם וַיֹּאמֶר אֲלֵהֶם אֲנִי נֶאֱסָף אֶל־עַמִּי קִבְרוּ אֹתִי
# אֶל־אֲבֹתָי אֶל־הַמְּעָרָה אֲשֶׁר בִּשְׂדֵה עֶפְרוֹן הַחִתִּי
# "[EN-AID] And he charged them, and said to them: I am being gathered to my
# people; bury me with my fathers, in the cave which is in the field of
# Ephron the Hittite."
m.step("Gen.49.29")
# ‹קִבְרוּ אֹתִי אֶל־אֲבֹתָי אֶל־הַמְּעָרָה› (“bury obj-marker-me/my to
# father-me/my to the-cavern”) — Jacob speaks a demand — LET: bury-me-to-
# avotai
m.declare("yaaqov", "LET",
          "qivru_oti_el_avotai")

# -------------------------- Gen.49.30 · THE_DEED_RECITED -------------------
# בַּמְּעָרָה אֲשֶׁר בִּשְׂדֵה הַמַּכְפֵּלָה אֲשֶׁר עַל־פְּנֵי־מַמְרֵא
# בְּאֶרֶץ כְּנָעַן אֲשֶׁר קָנָה אַבְרָהָם אֶת־הַשָּׂדֶה מֵאֵת עֶפְרֹן
# הַחִתִּי לַאֲחֻזַּת־קָבֶר
# "[EN-AID] In the cave which is in the field of Machpelah, which is before
# Mamre, in the land of Canaan — which Abraham bought with the field from
# Ephron the Hittite for a holding of burial."
m.step("Gen.49.30")
# ‹אֲשֶׁר קָנָה אַבְרָהָם אֶת־הַשָּׂדֶה מֵאֵת עֶפְרֹן הַחִתִּי
# לַאֲחֻזַּת־קָבֶר› (“which possessor Abraham obj-marker the-field from-with
# Ephron the-Chittite to-something-seized sepulchre”) — fact holds: which-
# possessor-Abraham-to-something-seized-sepulchre
m.fact("asher_qana_avraham_la_achuzat_qaver")

# -------------------------- Gen.49.31 · THE_SIX_BURIED_THERE ---------------
# שָׁמָּה קָבְרוּ אֶת־אַבְרָהָם וְאֵת שָׂרָה אִשְׁתּוֹ שָׁמָּה קָבְרוּ
# אֶת־יִצְחָק וְאֵת רִבְקָה אִשְׁתּוֹ וְשָׁמָּה קָבַרְתִּי אֶת־לֵאָה
# "[EN-AID] There they buried Abraham and Sarah his wife; there they buried
# Isaac and Rebekah his wife; and there I buried Leah."
m.step("Gen.49.31")
# ‹וְשָׁמָּה קָבַרְתִּי אֶת־לֵאָה› (“and-there-ward bury obj-marker Leah”) —
# fact holds: and-shama-bury-obj-marker-Leah
m.fact("ve_shama_qavarti_et_lea")

# -------------------------- Gen.49.32 · PURCHASE_FROM_THE_SONS_OF_HET ------
# מִקְנֵה הַשָּׂדֶה וְהַמְּעָרָה אֲשֶׁר־בּוֹ מֵאֵת בְּנֵי־חֵת
# "[EN-AID] The purchase of the field and the cave which is in it — from the
# sons of Heth."
m.step("Gen.49.32")
# ‹מִקְנֵה הַשָּׂדֶה וְהַמְּעָרָה› (“something-bought the-field and-the-
# cavern”) — fact holds: something-bought-the-field-from-obj-marker-son-Heth
m.fact("miqne_ha_sade_me_et_bene_chet")

# -------------------------- Gen.49.33 · GATHERED_TO_HIS_PEOPLE -------------
# וַיְכַל יַעֲקֹב לְצַוֺּת אֶת־בָּנָיו וַיֶּאֱסֹף רַגְלָיו אֶל־הַמִּטָּה
# וַיִּגְוַע וַיֵּאָסֶף אֶל־עַמָּיו
# "[EN-AID] And Jacob finished charging his sons, and he gathered his feet
# into the bed; and he expired, and was gathered to his people."
m.step("Gen.49.33")
# ‹וַיִּגְוַע וַיֵּאָסֶף אֶל־עַמָּיו› (“and-breathe-out and-gather-for-any-
# purpose to people-him/its”) — event: gava — agent Jacob
m.event("gava", agent="yaaqov")
# witness-tier presupposed read: a_funeral_order_that_becomes_a_camp on
# he_finished_commanding_his_sons — read, not installed
m.witness_read("he_finished_commanding_his_sons", "a_funeral_order_that_becomes_a_camp",
                cites=["Bereshit Rabbah 100:2", "Bereshit Rabbah 100:1"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['qivru_oti_el_avotai']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['shimu_el_yisrael_avikhem', 'reuven_bekhori_ata', 'pachaz_ka_mayim_al_totar', 'shimon_ve_levi_achim', 'bi_qhalam_al_techad_kevodi', 'achalqem_be_yaaqov_va_afitzem_be_yisrael', 'yodukha_achekha', 'mi_teref_beni_alita', 'lo_yasur_shevet_mi_yhuda_ad_ki_yavo_shilo', 'osri_la_gefen_iro', 'chakhlili_enayim_mi_yayin', 'zevulun_le_chof_yamim_yishkon', 'yisashkhar_chamor_garem', 'va_yet_shikhmo_lisbol', 'dan_yadin_amo', 'ha_noshekh_iqve_sus', 'li_yshuatkha_qiviti_YHWH', 'gad_gedud_yegudenu', 'me_asher_shemena_lachmo', 'ayala_shelucha_ha_noten_imre_shafer', 'ben_porat_yosef', 'va_yemararuhu_va_robu', 'va_teshev_be_etan_qashto', 'birkhot_shamayim_me_al', 'tihyena_le_rosh_yosef', 'binyamin_zeev_yitraf', 'asher_qana_avraham_la_achuzat_qaver', 've_shama_qavarti_et_lea', 'miqne_ha_sade_me_et_bene_chet'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    assert sorted(m.WORLD["witnessed"]) == ['dan_a_serpent', 'for_your_salvation_i_hope', 'the_end_of_days', 'the_translation_itself', 'they_hamstrung_an_ox']
    assert m.WORLD["witnessed"]['dan_a_serpent']["cites"] == ['Bereshit Rabbah 99:4']
    assert all('the_blessings_distributed_then_pooled' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['for_your_salvation_i_hope']["cites"] == ['Bereshit Rabbah 98:14', 'Bereshit Rabbah 99:11']
    assert all('one_cry_and_two_destinations' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_end_of_days']["cites"] == ['Bereshit Rabbah 98:2', 'Bereshit Rabbah 99:5']
    assert all('revealed_then_sealed_mid_sentence' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_translation_itself']["cites"] == ['Onkelos Genesis 49:13', 'Onkelos Genesis 49:10', 'Onkelos Genesis 49:27']
    assert all('ceasing_to_translate_for_one_chapter' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['they_hamstrung_an_ox']["cites"] == ['Bereshit Rabbah 98:5', 'Onkelos Genesis 49:5']
    assert all('three_layers_standing_on_one_verse' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('hear_israel_your_father', 'the_daily_liturgy_sourced_to_this_verse'), ('your_brothers_shall_praise_you', 'the_name_read_to_the_confession'), ('until_shiloh_comes', 'a_place_name_resolved_into_a_person'), ('zebulun_at_the_shore', 'a_prophets_parentage_and_a_patronage_rule'), ('they_embittered_him_and_shot_at_him', 'the_slander_model_stated_in_full'), ('his_bow_abode_in_strength', 'one_noun_read_three_ways'), ('benjamin_a_ravening_wolf', 'the_sanctuary_awarded_by_absence_from_a_crime'), ('he_finished_commanding_his_sons', 'a_funeral_order_that_becomes_a_camp')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 98:3', 'Onkelos Genesis 49:2']
    assert all('the_daily_liturgy_sourced_to_this_verse' not in f for f in m.WORLD["facts"])
    assert 'hear_israel_your_father' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Onkelos Genesis 49:8', 'Bereshit Rabbah 98:7']
    assert all('the_name_read_to_the_confession' not in f for f in m.WORLD["facts"])
    assert 'your_brothers_shall_praise_you' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Genesis 49:10', 'Bereshit Rabbah 98:8']
    assert all('a_place_name_resolved_into_a_person' not in f for f in m.WORLD["facts"])
    assert 'until_shiloh_comes' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 98:11', 'Bereshit Rabbah 99:9']
    assert all('a_prophets_parentage_and_a_patronage_rule' not in f for f in m.WORLD["facts"])
    assert 'zebulun_at_the_shore' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 98:19']
    assert all('the_slander_model_stated_in_full' not in f for f in m.WORLD["facts"])
    assert 'they_embittered_him_and_shot_at_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Onkelos Genesis 49:24', 'Bereshit Rabbah 98:20']
    assert all('one_noun_read_three_ways' not in f for f in m.WORLD["facts"])
    assert 'his_bow_abode_in_strength' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 99:1', 'Onkelos Genesis 49:27', 'Bereshit Rabbah 99:3']
    assert all('the_sanctuary_awarded_by_absence_from_a_crime' not in f for f in m.WORLD["facts"])
    assert 'benjamin_a_ravening_wolf' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 100:2', 'Bereshit Rabbah 100:1']
    assert all('a_funeral_order_that_becomes_a_camp' not in f for f in m.WORLD["facts"])
    assert 'he_finished_commanding_his_sons' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
