#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_13_cain_line_seth — 4:17-26
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_13_cain_line_seth.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Cain's line and Seth: the first city, the crafts, seventy-seven, calling on the Name (4:17-26)"""
from machine import Machine

m = Machine("gen_13_cain_line_seth")

# -------------------------- Gen.4.17 · FIRST_CITY_BUILT_NAMED --------------
# וַיֵּדַע קַיִן אֶת־אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת־חֲנוֹךְ וַיְהִי בֹּנֶה
# עִיר וַיִּקְרָא שֵׁם הָעִיר כְּשֵׁם בְּנוֹ חֲנוֹךְ
# "And Cain knew his wife; and she conceived, and bore Enoch; and he builded
# a city, and called the name of the city after the name of his son Enoch."
m.step("Gen.4.17")
# ‹וַיֵּדַע קַיִן אֶת־אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת־חֲנוֹךְ› (“and-he-knew
# Cain obj-marker his-wife and-she-conceived and-she-bore obj-marker Enoch”)
# — event: bear — agent wife-of-Cain; theme Enoch
m.event("bear", agent="eshet_kayin", themes=["chanokh"])
# ‹וַיְהִי בֹּנֶה עִיר› (“and-he-was building city”) — the world gains: city
m.install("ir")
# ‹וַיִּקְרָא שֵׁם הָעִיר כְּשֵׁם בְּנוֹ חֲנוֹךְ› (“and-he-called name-of
# the-city like-name-of his-son Enoch”) — named: city := Chanokh
m.name("ir", "Chanokh")
# reads without prior install (flag, not fix): Cain, wife-of-Cain
m.presupposed("kayin", "eshet_kayin")

# -------------------------- Gen.4.18 · BEGETTING_CHAIN_FOUR_LINKS ----------
# וַיִּוָּלֵד לַחֲנוֹךְ אֶת־עִירָד וְעִירָד יָלַד אֶת־מְחוּיָאֵל
# וּמְחִיּיָאֵל יָלַד אֶת־מְתוּשָׁאֵל וּמְתוּשָׁאֵל יָלַד אֶת־לָמֶךְ
# "And unto Enoch was born Irad; and Irad begot Mehujael; and Mehujael begot
# Methushael; and Methushael begot Lamech."
m.step("Gen.4.18")
# ‹וַיִּוָּלֵד לַחֲנוֹךְ אֶת־עִירָד› (“and-was-born to-Enoch obj-marker
# Irad”) — event: born — theme Irad
m.event("born", themes=["irad"])
# ‹וְעִירָד יָלַד אֶת־מְחוּיָאֵל› (“and-Irad begot obj-marker Mehujael”) —
# event: beget — agent Irad; theme Mehujael
m.event("beget", agent="irad", themes=["mechuyael"])
# ‹וּמְחִיּיָאֵל יָלַד אֶת־מְתוּשָׁאֵל› (“and-Mehijael begot obj-marker
# Methusael”) — event: beget — agent Mehujael; theme Methusael
m.event("beget", agent="mechuyael", themes=["metushael"])
# ‹וּמְתוּשָׁאֵל יָלַד אֶת־לָמֶךְ› (“and-Methusael begot obj-marker Lamech”)
# — event: beget — agent Methusael; theme Lamech
m.event("beget", agent="metushael", themes=["lemekh"])

# -------------------------- Gen.4.19 · FIRST_POLYGAMY ----------------------
# וַיִּקַּח־לוֹ לֶמֶךְ שְׁתֵּי נָשִׁים שֵׁם הָאַחַת עָדָה וְשֵׁם הַשֵּׁנִית
# צִלָּה
# "And Lamech took unto him two wives; the name of the one was Adah, and the
# name of the other Zillah."
m.step("Gen.4.19")
# ‹וַיִּקַּח־לוֹ לֶמֶךְ שְׁתֵּי נָשִׁים› (“and-he-took for-himself Lamech
# two wives”) — event: take — agent Lamech; theme two-of-wives
m.event("take", agent="lemekh", themes=["shte_nashim"])
# ‹שֵׁם הָאַחַת עָדָה וְשֵׁם הַשֵּׁנִית צִלָּה› (“name-of the-first Adah
# and-name-of the-second Tzillah”) — fact holds: two-of-wives-to-Lamech;
# name-of-the-first-Adah; name-of-the-second-Tzillah
m.fact("shte_nashim_le_lemekh",
       "shem_ha_achat_adah",
       "shem_ha_shenit_tzilah")

# -------------------------- Gen.4.20 · OFFICE_TENT_AND_HERD ----------------
# וַתֵּלֶד עָדָה אֶת־יָבָל הוּא הָיָה אֲבִי יֹשֵׁב אֹהֶל וּמִקְנֶה
# "And Adah bore Jabal; he was the father of such as dwell in tents and have
# cattle."
m.step("Gen.4.20")
# ‹וַתֵּלֶד עָדָה אֶת־יָבָל› (“and-she-bore Adah obj-marker Yaval”) — event:
# bear — agent Adah; theme Yaval
m.event("bear", agent="adah", themes=["yaval"])
# ‹הוּא הָיָה אֲבִי יֹשֵׁב אֹהֶל וּמִקְנֶה› (“he was father-of dweller-of
# tent and-herds”) — fact holds: father-of-dweller-of-tent-and-
# livestock(Yaval)
m.fact("avi_yoshev_ohel_u_mikneh(yaval)")

# -------------------------- Gen.4.21 · OFFICE_HARP_AND_PIPE ----------------
# וְשֵׁם אָחִיו יוּבָל הוּא הָיָה אֲבִי כָּל־תֹּפֵשׂ כִּנּוֹר וְעוּגָב
# "And his brother's name was Jubal; he was the father of all such as handle
# the harp and pipe."
m.step("Gen.4.21")
# ‹וְשֵׁם אָחִיו יוּבָל הוּא הָיָה אֲבִי כָּל־תֹּפֵשׂ כִּנּוֹר וְעוּגָב›
# (“and-name-of his-brother Yuval he was father-of all handler-of harp and-
# pipe”) — fact holds: name-of-his-brother-Yuval; father-of-all-handler-of-
# harp-and-pipe(Yuval)
m.fact("shem_achiv_yuval",
       "avi_kol_tofes_kinor_ve_ugav(yuval)")

# -------------------------- Gen.4.22 · OFFICE_BRONZE_IRON_SISTER -----------
# וְצִלָּה גַם־הִוא יָלְדָה אֶת־תּוּבַל קַיִן לֹטֵשׁ כָּל־חֹרֵשׁ נְחֹשֶׁת
# וּבַרְזֶל וַאֲחוֹת תּוּבַל־קַיִן נַעֲמָה
# "And Zillah, she also bore Tubal-cain, the forger of every cutting
# instrument of brass and iron; and the sister of Tubal-cain was Naamah."
m.step("Gen.4.22")
# ‹וְצִלָּה גַם־הִוא יָלְדָה אֶת־תּוּבַל קַיִן› (“and-Tzillah also she bore
# obj-marker Tuval Kayin”) — event: bear — agent Tzillah; theme Tuval-Cain
m.event("bear", agent="tzilah", themes=["tuval_kayin"])
# ‹לֹטֵשׁ כָּל־חֹרֵשׁ נְחֹשֶׁת וּבַרְזֶל וַאֲחוֹת תּוּבַל־קַיִן נַעֲמָה›
# (“hammerer-of every craftsman-of bronze and-iron and-sister-of Tuval Kayin
# Naamah”) — fact holds: hammerer-of-all-craftsman-of-bronze-and-iron(Tuval-
# Cain); sister-of-Tuval-Cain-Naamah
m.fact("lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)",
       "achot_tuval_kayin_naamah")

# -------------------------- Gen.4.23 · SWORD_SONG_FIRST_HUMAN_IMPERATIVES --
# וַיֹּאמֶר לֶמֶךְ לְנָשָׁיו עָדָה וְצִלָּה שְׁמַעַן קוֹלִי נְשֵׁי לֶמֶךְ
# הַאְזֵנָּה אִמְרָתִי כִּי אִישׁ הָרַגְתִּי לְפִצְעִי וְיֶלֶד לְחַבֻּרָתִי
# "And Lamech said unto his wives: Adah and Zillah, hear my voice; ye wives
# of Lamech, hearken unto my speech; for I have slain a man for wounding me,
# and a young man for bruising me."
m.step("Gen.4.23")
# ‹וַיֹּאמֶר לֶמֶךְ לְנָשָׁיו עָדָה וְצִלָּה› (“and-he-said Lamech to-his-
# wives Adah and-Tzillah”) — event: say — agent Lamech; theme wives-of-
# Lamech
m.event("say", agent="lemekh", themes=["neshei_lemekh"])
# ‹שְׁמַעַן קוֹלִי … הַאְזֵנָּה אִמְרָתִי› (“hear my-voice … give-ear my-
# speech”) — Lamech speaks a demand — LET: hear(wives-of-Lamech, voice-
# Lamech)
m.declare("lemekh", "LET",
          "shema(neshei_lemekh, qol_lemekh)")
# ‹כִּי אִישׁ הָרַגְתִּי לְפִצְעִי וְיֶלֶד לְחַבֻּרָתִי› (“for a-man I-have-
# killed for-my-wound and-a-boy for-my-bruise”) — fact holds: a-man-I-have-
# killed-to-fitzi-and-a-boy-to-my-wound
m.fact("ish_haragti_le_fitzi_ve_yeled_le_chaburati")

# -------------------------- Gen.4.24 · QUOTE_DIFF_SEVENTY_SEVEN ------------
# כִּי שִׁבְעָתַיִם יֻקַּם־קָיִן וְלֶמֶךְ שִׁבְעִים וְשִׁבְעָה
# "If Cain shall be avenged sevenfold, truly Lamech seventy and sevenfold."
m.step("Gen.4.24")
# ‹כִּי שִׁבְעָתַיִם יֻקַּם־קָיִן וְלֶמֶךְ שִׁבְעִים וְשִׁבְעָה› (“if
# sevenfold shall-be-avenged Cain then-Lamech seventy and-seven”) — spec-
# delta — spec said all-slayer Kayin sevenfold shall-be-avenged — issuer
# the-LORD, decree with mark (4:15, frozen gen-12), delivery says for
# sevenfold shall-be-avenged-Kayin and-Lemekh seventy and-seven — issuer
# Lamech, boast, multiplier x11, target self, ratification NONE (4:24)
m.spec_delta("kol-horeg Kayin shivatayim yukam — issuer YHWH, decree with mark (4:15, frozen gen_12)",
             "ki shivatayim yukam-Kayin ve-Lemekh shivim ve-shivah — issuer lemekh, boast, multiplier x11, target self, ratification NONE (4:24)")

# -------------------------- Gen.4.25 · SETH_REPLACEMENT_SEED ---------------
# וַיֵּדַע אָדָם עוֹד אֶת־אִשְׁתּוֹ וַתֵּלֶד בֵּן וַתִּקְרָא אֶת־שְׁמוֹ שֵׁת
# כִּי שָׁת־לִי אֱלֹהִים זֶרַע אַחֵר תַּחַת הֶבֶל כִּי הֲרָגוֹ קָיִן
# "And Adam knew his wife again; and she bore a son, and called his name
# Seth: 'for God hath appointed me another seed instead of Abel; for Cain
# slew him.'"
m.step("Gen.4.25")
# ‹וַיֵּדַע אָדָם עוֹד אֶת־אִשְׁתּוֹ וַתֵּלֶד בֵּן› (“and-he-knew Adam again
# obj-marker his-wife and-she-bore son”) — event: bear — agent wife-of-Adam;
# theme Shet
m.event("bear", agent="eshet_adam", themes=["shet"])
# ‹וַתִּקְרָא אֶת־שְׁמוֹ שֵׁת› (“and-she-called obj-marker his-name Shet”) —
# named: Shet := Shet
m.name("shet", "Shet")
# ‹כִּי שָׁת־לִי אֱלֹהִים זֶרַע אַחֵר תַּחַת הֶבֶל כִּי הֲרָגוֹ קָיִן› (“for
# Shet to-me God seed another in-place-of Abel for killed-him Cain”) — fact
# holds: has-SET-to-me-God-seed-another-place-of-Abel; slew-him-Cain-named-
# in-speech
m.fact("shat_li_elohim_zera_acher_tachat_hevel",
       "harago_kayin_named_in_speech")
# reads without prior install (flag, not fix): Adam, wife-of-Adam
m.presupposed("adam", "eshet_adam")

# -------------------------- Gen.4.26 · ENOSH_CALLING_ON_THE_NAME -----------
# וּלְשֵׁת גַּם־הוּא יֻלַּד־בֵּן וַיִּקְרָא אֶת־שְׁמוֹ אֱנוֹשׁ אָז הוּחַל
# לִקְרֹא בְּשֵׁם יְהוָה
# "And to Seth, to him also there was born a son; and he called his name
# Enosh; then began men to call upon the name of the LORD."
m.step("Gen.4.26")
# ‹וּלְשֵׁת גַּם־הוּא יֻלַּד־בֵּן› (“and-to-Seth also he was-born son”) —
# event: born — theme Enosh
m.event("born", themes=["enosh"])
# ‹וַיִּקְרָא אֶת־שְׁמוֹ אֱנוֹשׁ› (“and-he-called obj-marker his-name
# Enosh”) — named: Enosh := Enosh
m.name("enosh", "Enosh")
# ‹אָז הוּחַל לִקְרֹא בְּשֵׁם יְהוָה› (“then was-begun to-call in-name-of
# YHWH”) — fact holds: was-begun-to-call-in-name-of-the-LORD
m.fact("huchal_likro_be_shem_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ir'}
    assert m.presupposed_set() == {'adam', 'eshet_adam', 'eshet_kayin', 'kayin'}
    assert m.REGISTRY["names"] == {'ir': 'Chanokh', 'shet': 'Shet', 'enosh': 'Enosh'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == ['shema(neshei_lemekh, qol_lemekh)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4, 'spec_delta': 1, 'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['shte_nashim_le_lemekh', 'shem_ha_achat_adah', 'shem_ha_shenit_tzilah', 'avi_yoshev_ohel_u_mikneh(yaval)', 'shem_achiv_yuval', 'avi_kol_tofes_kinor_ve_ugav(yuval)', 'lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)', 'achot_tuval_kayin_naamah', 'ish_haragti_le_fitzi_ve_yeled_le_chaburati', 'shat_li_elohim_zera_acher_tachat_hevel', 'harago_kayin_named_in_speech', 'huchal_likro_be_shem_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
