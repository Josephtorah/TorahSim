#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_31_covenant_pieces — 15:1-21
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_31_covenant_pieces.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The covenant of the pieces: the vision, the stars, the rite, the decree, the grant (15:1-21)"""
from machine import Machine

m = Machine("gen_31_covenant_pieces")

# -------------------------- Gen.15.1 · THE_WORD_THE_SHIELD_AND_THE_FEAR_NOT -
# אַחַר הַדְּבָרִים הָאֵלֶּה הָיָה דְבַר־יְהוָה אֶל־אַבְרָם בַּמַּחֲזֶה
# לֵאמֹר אַל־תִּירָא אַבְרָם אָנֹכִי מָגֵן לָךְ שְׂכָרְךָ הַרְבֵּה מְאֹד
# "After these things the word of the LORD came unto Abram in a vision,
# saying: 'Fear not, Abram, I am thy shield, thy reward shall be exceeding
# great.'"
m.step("Gen.15.1")
# ‹הָיָה דְבַר־יְהוָה אֶל־אַבְרָם בַּמַּחֲזֶה› (“be word/thing YHWH to Abram
# in-vision”) — event: come — theme word/thing-the-LORD
m.event("come", themes=["devar_YHWH"])
# ‹אַל־תִּירָא אַבְרָם› (“do-not fear Abram”) — the-LORD speaks a demand —
# LET-NOT: fear(Abram)
m.declare("YHWH", "LET-NOT",
          "tira(avram)")
# ‹אָנֹכִי מָגֵן לָךְ שְׂכָרְךָ הַרְבֵּה מְאֹד› (“shield to-you/your wage-
# you/your multiply very”) — fact holds: I-shield-to-you; sekharkha-harbeh-
# very
m.fact("anokhi_magen_lakh",
       "sekharkha_harbeh_meod")

# -------------------------- Gen.15.2 · THE_FIRST_SPEECH_TO_GOD -------------
# וַיֹּאמֶר אַבְרָם אֲדֹנָי יֱהוִה מַה־תִּתֶּן־לִי וְאָנֹכִי הוֹלֵךְ
# עֲרִירִי וּבֶן־מֶשֶׁק בֵּיתִי הוּא דַּמֶּשֶׂק אֱלִיעֶזֶר
# "And Abram said: 'O Lord GOD, what wilt Thou give me, seeing I go hence
# childless, and he that shall be possessor of my house is Eliezer of
# Damascus?'"
m.step("Gen.15.2")
# ‹וַיֹּאמֶר אַבְרָם אֲדֹנָי יֱהוִה› (“and-say Abram Lord-me/my YHWH”) —
# event: say — agent Abram
m.event("say", agent="avram")
# ‹מַה־תִּתֶּן־לִי וְאָנֹכִי הוֹלֵךְ עֲרִירִי וּבֶן־מֶשֶׁק בֵּיתִי הוּא
# דַּמֶּשֶׂק אֱלִיעֶזֶר› (“what set to-me/my and-I walk/go bare and-son
# possession house-me/my he/it Damascus Eliezer”) — fact holds: mah-set-to-
# me-and-I-walk/go-bare; between-possession-beti-he/it-Damascus-Eliezer
m.fact("mah_titen_li_ve_anokhi_holekh_ariri",
       "ben_mesheq_beti_hu_dameseq_eliezer")
# reads without prior install (flag, not fix): Damascus
m.presupposed("dameseq")

# -------------------------- Gen.15.3 · THE_COMPLAINT_RELAUNCHED ------------
# וַיֹּאמֶר אַבְרָם הֵן לִי לֹא נָתַתָּה זָרַע וְהִנֵּה בֶן־בֵּיתִי יוֹרֵשׁ
# אֹתִי
# "And Abram said: 'Behold, to me Thou hast given no seed, and, lo, one born
# in my house is to be mine heir.'"
m.step("Gen.15.3")
# ‹וַיֹּאמֶר אַבְרָם› (“and-say Abram”) — event: say — agent Abram
m.event("say", agent="avram")
# ‹הֵן לִי לֹא נָתַתָּה זָרַע וְהִנֵּה בֶן־בֵּיתִי יוֹרֵשׁ אֹתִי› (“lo! to-
# me/my not set seed and-behold son house-me/my possess/inherit obj-marker-
# me/my”) — fact holds: lo!-to-me-not-set-seed; between-beti-
# possess/inherit-me
m.fact("hen_li_lo_natata_zara",
       "ben_beti_yoresh_oti")

# -------------------------- Gen.15.4 · THE_HEIR_CORRECTION -----------------
# וְהִנֵּה דְבַר־יְהוָה אֵלָיו לֵאמֹר לֹא יִירָשְׁךָ זֶה כִּי־אִם אֲשֶׁר
# יֵצֵא מִמֵּעֶיךָ הוּא יִירָשֶׁךָ
# "And, behold, the word of the LORD came unto him, saying: 'This man shall
# not be thine heir; but he that shall come forth out of thine own bowels
# shall be thine heir.'"
m.step("Gen.15.4")
# ‹וְהִנֵּה דְבַר־יְהוָה אֵלָיו לֵאמֹר› (“and-behold word/thing YHWH to-
# him/its to-say”) — event: come — theme word/thing-the-LORD
m.event("come", themes=["devar_YHWH"])
# ‹לֹא יִירָשְׁךָ זֶה כִּי־אִם אֲשֶׁר יֵצֵא מִמֵּעֶיךָ הוּא יִירָשֶׁךָ›
# (“not possess/inherit-you/your this that if which bring-forth from-used-
# only-in-plural-the-inte-you/your he/it possess/inherit-you/your”) — fact
# holds: not-yirashkha-this; which-bring-forth-from-meekha-he/it-yirashekha
m.fact("lo_yirashkha_zeh",
       "asher_yetze_mi_meekha_hu_yirashekha")

# -------------------------- Gen.15.5 · THE_STARS_AND_THE_COUNT_COMMAND -----
# וַיּוֹצֵא אֹתוֹ הַחוּצָה וַיֹּאמֶר הַבֶּט־נָא הַשָּׁמַיְמָה וּסְפֹר
# הַכּוֹכָבִים אִם־תּוּכַל לִסְפֹּר אֹתָם וַיֹּאמֶר לוֹ כֹּה יִהְיֶה
# זַרְעֶךָ
# "And He brought him forth abroad, and said: 'Look now toward heaven, and
# count the stars, if thou be able to count them'; and He said unto him: 'So
# shall thy seed be.'"
m.step("Gen.15.5")
# ‹וַיּוֹצֵא אֹתוֹ הַחוּצָה› (“and-bring-forth obj-marker-him/its the-
# outside-ward”) — event: bring-out — agent the-LORD; theme Abram
m.event("bring_out", agent="YHWH", themes=["avram"])
# ‹וַיֹּאמֶר› (“and-say”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹הַבֶּט־נָא הַשָּׁמַיְמָה וּסְפֹר הַכּוֹכָבִים› (“look please the-heavens-
# ward and-count the-stars”) — the-LORD speaks a demand — LET: look-and-
# count(Abram, the-shamaymah-and-the-stars)
m.declare("YHWH", "LET",
          "habet_u_sefor(avram, ha_shamaymah_ve_ha_kokhavim)")
# ‹וַיֹּאמֶר לוֹ› (“and-say to-him/its”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹כֹּה יִהְיֶה זַרְעֶךָ› (“like-this be seed-you/your”) — fact holds: koh-
# yihyeh-zarekha
m.fact("koh_yihyeh_zarekha")
# witness-tier presupposed read: exemption_from_astrology on
# brought_him_outside — read, not installed
m.witness_read("brought_him_outside", "exemption_from_astrology",
                cites=["Shabbat 156a:13", "Bereshit Rabbah 44:12"])

# -------------------------- Gen.15.6 · THE_BELIEF_AND_THE_RECKONING --------
# וְהֶאֱמִן בַּיהוָה וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה
# "And he believed in the LORD; and He counted it to him for righteousness."
m.step("Gen.15.6")
# ‹וְהֶאֱמִן בַּיהוָה וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה› (“and-build-up in-YHWH
# and-plait-her/its to-him/its rightness”) — fact holds: and-build-up-in-
# the-the-LORD; and-yachsheveha-not-tzedaqah
m.fact("ve_heemin_ba_YHWH",
       "va_yachsheveha_lo_tzedaqah")

# -------------------------- Gen.15.7 · ANI_YHWH_THE_SELF_NAMING ------------
# וַיֹּאמֶר אֵלָיו אֲנִי יְהוָה אֲשֶׁר הוֹצֵאתִיךָ מֵאוּר כַּשְׂדִּים לָתֶת
# לְךָ אֶת־הָאָרֶץ הַזֹּאת לְרִשְׁתָּהּ
# "And He said unto him: 'I am the LORD that brought thee out of Ur of the
# Chaldees, to give thee this land to inherit it.'"
m.step("Gen.15.7")
# ‹וַיֹּאמֶר אֵלָיו› (“and-say to-him/its”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹אֲנִי יְהוָה אֲשֶׁר הוֹצֵאתִיךָ מֵאוּר כַּשְׂדִּים לָתֶת לְךָ אֶת־הָאָרֶץ
# הַזֹּאת לְרִשְׁתָּהּ› (“YHWH which bring-forth-you/your from-Ur Chaldeans
# to-set to-you/your obj-marker the-earth the-this to-possess/inherit-
# her/its”) — fact holds: ani-the-LORD-which-hotzetikha-from-Ur-Chaldeans;
# to-set-to-you-obj-marker-the-earth-the-this-to-rishtah
m.fact("ani_YHWH_asher_hotzetikha_me_ur_kasdim",
       "la_tet_lekha_et_ha_aretz_ha_zot_le_rishtah")
# reads without prior install (flag, not fix): Ur-Chaldeans
m.presupposed("ur_kasdim")

# -------------------------- Gen.15.8 · THE_SECOND_QUESTION -----------------
# וַיֹּאמַר אֲדֹנָי יֱהוִה בַּמָּה אֵדַע כִּי אִירָשֶׁנָּה
# "And he said: 'O Lord GOD, whereby shall I know that I shall inherit it?'"
m.step("Gen.15.8")
# ‹וַיֹּאמַר› (“and-say”) — event: say — agent Abram
m.event("say", agent="avram")
# ‹אֲדֹנָי יֱהוִה בַּמָּה אֵדַע כִּי אִירָשֶׁנָּה› (“Lord-me/my YHWH in-what
# know that possess/inherit-her/its”) — fact holds: in-the-mah-know-that-
# irashena
m.fact("ba_mah_eda_ki_irashena")
# witness-tier presupposed read: order_of_offerings_instituted on
# bamah_eda_question — read, not installed
m.witness_read("bamah_eda_question", "order_of_offerings_instituted",
                cites=["Megillah 31b:5", "Berakhot 7b:1"])

# -------------------------- Gen.15.9 · THE_TAKE_COMMAND --------------------
# וַיֹּאמֶר אֵלָיו קְחָה לִי עֶגְלָה מְשֻׁלֶּשֶׁת וְעֵז מְשֻׁלֶּשֶׁת וְאַיִל
# מְשֻׁלָּשׁ וְתֹר וְגוֹזָל
# "And He said unto him: 'Take Me a heifer of three years old, and a she-
# goat of three years old, and a ram of three years old, and a turtle-dove,
# and a young pigeon.'"
m.step("Gen.15.9")
# ‹וַיֹּאמֶר אֵלָיו› (“and-say to-him/its”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹קְחָה לִי עֶגְלָה מְשֻׁלֶּשֶׁת וְעֵז מְשֻׁלֶּשֶׁת וְאַיִל מְשֻׁלָּשׁ
# וְתֹר וְגוֹזָל› (“take-ward to-me/my calf be-triplicate and-she-goat be-
# triplicate and-ram be-triplicate and-ring-dove and-nestling”) — the-LORD
# speaks a demand — LET: qechah(Abram, eglah-she-goat-ram-ring-dove-and-
# nestling)
m.declare("YHWH", "LET",
          "qechah(avram, eglah_ez_ayil_tor_ve_gozal)")
# witness-tier presupposed read: standing_covenant_form on pieces_rite —
# read, not installed
m.witness_read("pieces_rite", "standing_covenant_form",
                cites=["Sifrei Devarim 171:6"])

# -------------------------- Gen.15.10 · THE_COMPLIANCE_AND_THE_CUTTING -----
# וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה וַיְבַתֵּר אֹתָם בַּתָּוֶךְ וַיִּתֵּן
# אִישׁ־בִּתְרוֹ לִקְרַאת רֵעֵהוּ וְאֶת־הַצִפֹּר לֹא בָתָר
# "And he took him all these, and divided them in the midst, and laid each
# half over against the other; but the birds divided he not."
m.step("Gen.15.10")
# ‹וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה› (“and-take to-him/its obj-marker all
# these”) — event: take — agent Abram; theme all-these
m.event("take", agent="avram", themes=["kol_eleh"])
# ‹וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה› (“and-take to-him/its obj-marker all
# these”) — demand settled (popped from the queue): qechah(Abram, eglah-she-
# goat-ram-ring-dove-and-nestling)
m.result("qechah(avram, eglah_ez_ayil_tor_ve_gozal)", tmark="t1")
# ‹וַיְבַתֵּר אֹתָם בַּתָּוֶךְ› (“and-chop-up obj-marker-them/their in-
# midst”) — event: cut — agent Abram; theme the-behemot
m.event("cut", agent="avram", themes=["ha_behemot"])
# ‹וַיִּתֵּן אִישׁ־בִּתְרוֹ לִקְרַאת רֵעֵהוּ› (“and-set man section-him/its
# to-encountering associate-him/its”) — event: give — agent Abram; theme
# man-bitro
m.event("give", agent="avram", themes=["ish_bitro"])
# ‹וְאֶת־הַצִפֹּר לֹא בָתָר› (“and-obj-marker the-little-bird not chop-up”)
# — fact holds: and-obj-marker-the-little-bird-not-chop-up
m.fact("ve_et_ha_tzipor_lo_vatar")

# -------------------------- Gen.15.11 · THE_VULTURES_DRIVEN_OFF ------------
# וַיֵּרֶד הָעַיִט עַל־הַפְּגָרִים וַיַּשֵּׁב אֹתָם אַבְרָם
# "And the birds of prey came down upon the carcasses, and Abram drove them
# away."
m.step("Gen.15.11")
# ‹וַיֵּרֶד הָעַיִט עַל־הַפְּגָרִים› (“and-go-down the-hawk over the-
# carcase”) — event: descend — agent the-hawk
m.event("descend", agent="ha_ayit")
# ‹וַיַּשֵּׁב אֹתָם אַבְרָם› (“and-blow obj-marker-them/their Abram”) —
# event: drive-off — agent Abram; theme the-hawk
m.event("drive_off", agent="avram", themes=["ha_ayit"])

# -------------------------- Gen.15.12 · THE_SLEEP_AND_THE_DREAD ------------
# וַיְהִי הַשֶּׁמֶשׁ לָבוֹא וְתַרְדֵּמָה נָפְלָה עַל־אַבְרָם וְהִנֵּה אֵימָה
# חֲשֵׁכָה גְדֹלָה נֹפֶלֶת עָלָיו
# "And it came to pass, that, when the sun was going down, a deep sleep fell
# upon Abram; and, lo, a dread, even a great darkness, fell upon him."
m.step("Gen.15.12")
# ‹וְתַרְדֵּמָה נָפְלָה עַל־אַבְרָם› (“and-lethargy fall over Abram”) —
# event: fall — theme deep-sleep
m.event("fall", themes=["tardemah"])
# ‹וְהִנֵּה אֵימָה חֲשֵׁכָה גְדֹלָה נֹפֶלֶת עָלָיו› (“and-behold fright
# darkness great fall over-him/its”) — fact holds: emah-chashekhah-gedolah-
# fall-alav
m.fact("emah_chashekhah_gedolah_nofelet_alav")
# witness-grounded state (its own tier):
# decoded_three_ways_with_transposition on the_vision
m.witness_state("the_vision", "decoded_three_ways_with_transposition",
                cites=["Bereshit Rabbah 44:21", "Mekhilta DeRabbi Yishmael, Tractate Bachodesh 9:5", "Mekhilta DeRabbi Yishmael, Tractate Bachodesh 9:7"])

# -------------------------- Gen.15.13 · THE_DECREE_SOJOURN_SERVE_AFFLICT ---
# וַיֹּאמֶר לְאַבְרָם יָדֹעַ תֵּדַע כִּי־גֵר יִהְיֶה זַרְעֲךָ בְּאֶרֶץ לֹא
# לָהֶם וַעֲבָדוּם וְעִנּוּ אֹתָם אַרְבַּע מֵאוֹת שָׁנָה
# "And He said unto Abram: 'Know of a surety that thy seed shall be a
# stranger in a land that is not theirs, and shall serve them; and they
# shall afflict them four hundred years;"
m.step("Gen.15.13")
# ‹וַיֹּאמֶר לְאַבְרָם יָדֹעַ תֵּדַע› (“and-say to-Abram know know”) —
# event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹כִּי־גֵר יִהְיֶה זַרְעֲךָ בְּאֶרֶץ לֹא לָהֶם וַעֲבָדוּם וְעִנּוּ אֹתָם
# אַרְבַּע מֵאוֹת שָׁנָה› (“that sojourner be seed-you/your in-earth not to-
# them/their and-work/serve-them/their and-afflict-literally obj-marker-
# them/their four hundred years”) — fact holds: sojourner-yihyeh-zarakha-in-
# earth-not-to-them; and-avadum-and-afflict-literally-otam-four-hundred-year
m.fact("ger_yihyeh_zarakha_be_eretz_lo_lahem",
       "va_avadum_ve_inu_otam_arba_meot_shanah")
# witness-tier presupposed read: dated_before_the_call_by_arithmetic on
# four_hundred_years — read, not installed
m.witness_read("four_hundred_years", "dated_before_the_call_by_arithmetic",
                cites=["Mekhilta DeRabbi Yishmael, Tractate Pischa 14:15", "Bereshit Rabbah 39:8", "Bereshit Rabbah 53:4"])

# -------------------------- Gen.15.14 · THE_JUDGMENT_AND_THE_EXODUS_WEALTH -
# וְגַם אֶת־הַגּוֹי אֲשֶׁר יַעֲבֹדוּ דָּן אָנֹכִי וְאַחֲרֵי־כֵן יֵצְאוּ
# בִּרְכֻשׁ גָּדוֹל
# "and also that nation, whom they shall serve, will I judge; and afterward
# shall they come out with great substance."
m.step("Gen.15.14")
# ‹וְגַם אֶת־הַגּוֹי אֲשֶׁר יַעֲבֹדוּ דָּן אָנֹכִי וְאַחֲרֵי־כֵן יֵצְאוּ
# בִּרְכֻשׁ גָּדוֹל› (“and-also obj-marker the-nation which work/serve
# straight-course and-after so bring-forth in-property great”) — fact holds:
# straight-course-I-obj-marker-the-nation-which-work/serve; and-acharei-so-
# bring-forth-bi-rekhush-great
m.fact("dan_anokhi_et_ha_goy_asher_yaavodu",
       "ve_acharei_khen_yetzu_bi_rekhush_gadol")

# -------------------------- Gen.15.15 · THE_PEACE_AND_THE_BURIAL -----------
# וְאַתָּה תָּבוֹא אֶל־אֲבֹתֶיךָ בְּשָׁלוֹם תִּקָּבֵר בְּשֵׂיבָה טוֹבָה
# "But thou shalt go to thy fathers in peace; thou shalt be buried in a good
# old age."
m.step("Gen.15.15")
# ‹וְאַתָּה תָּבוֹא אֶל־אֲבֹתֶיךָ בְּשָׁלוֹם תִּקָּבֵר בְּשֵׂיבָה טוֹבָה›
# (“and-you come/bring to father-you/your in-safe bury in-old-age good”) —
# fact holds: come/bring-to-avotekha-in-safe; bury-in-sevah-tovah
m.fact("tavo_el_avotekha_be_shalom",
       "tiqaver_be_sevah_tovah")
# witness-tier presupposed read: leave_taking_formula on in_peace_clause —
# read, not installed
m.witness_read("in_peace_clause", "leave_taking_formula",
                cites=["Berakhot 64a:10"])

# -------------------------- Gen.15.16 · THE_FOURTH_GENERATION_AND_THE_UNFULL_INIQUITY -
# וְדוֹר רְבִיעִי יָשׁוּבוּ הֵנָּה כִּי לֹא־שָׁלֵם עֲוֺן הָאֱמֹרִי
# עַד־הֵנָּה
# "And in the fourth generation they shall come back hither; for the
# iniquity of the Amorite is not yet full.'"
m.step("Gen.15.16")
# ‹וְדוֹר רְבִיעִי יָשׁוּבוּ הֵנָּה כִּי לֹא־שָׁלֵם עֲוֺן הָאֱמֹרִי
# עַד־הֵנָּה› (“and-generation fourth return hither that not complete
# perversity the-Emorite until hither”) — fact holds: and-generation-fourth-
# return-henah; not-complete-perversity-the-Emorite-until-henah
m.fact("ve_dor_revii_yashuvu_henah",
       "lo_shalem_avon_ha_emori_ad_henah")
# witness-grounded state (its own tier): conditional_on_conduct on
# two_clocks
m.witness_state("two_clocks", "conditional_on_conduct",
                cites=["Mishnah Eduyot 2:9", "Tosefta Eduyot 1:11", "Mekhilta DeRabbi Yishmael, Tractate Pischa 14:16"])

# -------------------------- Gen.15.17 · THE_FIRE_BETWEEN_THE_PIECES --------
# וַיְהִי הַשֶּׁמֶשׁ בָּאָה וַעֲלָטָה הָיָה וְהִנֵּה תַנּוּר עָשָׁן
# וְלַפִּיד אֵשׁ אֲשֶׁר עָבַר בֵּין הַגְּזָרִים הָאֵלֶּה
# "And it came to pass, that, when the sun went down, and there was thick
# darkness, behold a smoking furnace, and a flaming torch that passed
# between these pieces."
m.step("Gen.15.17")
# ‹וַיְהִי הַשֶּׁמֶשׁ בָּאָה וַעֲלָטָה הָיָה› (“and-be the-sun come/bring
# and-dusk be”) — fact holds: and-alatah-was
m.fact("va_alatah_hayah")
# ‹וְהִנֵּה תַנּוּר עָשָׁן וְלַפִּיד אֵשׁ אֲשֶׁר עָבַר בֵּין הַגְּזָרִים
# הָאֵלֶּה› (“and-behold fire-pot smoke and-flambeau fire which pass-over
# between the-something-cut-off the-these”) — event: pass — agent fire-pot-
# smoke-and-flambeau-fire; theme between-the-something-cut-off
m.event("pass", agent="tanur_ashan_ve_lapid_esh", themes=["bein_ha_gezarim"])

# -------------------------- Gen.15.18 · THE_COVENANT_CUT_AND_THE_RECEIPT ---
# בַּיּוֹם הַהוּא כָּרַת יְהוָה אֶת־אַבְרָם בְּרִית לֵאמֹר לְזַרְעֲךָ
# נָתַתִּי אֶת־הָאָרֶץ הַזֹּאת מִנְּהַר מִצְרַיִם עַד־הַנָּהָר הַגָּדֹל
# נְהַר־פְּרָת
# "In that day the LORD made a covenant with Abram, saying: 'Unto thy seed
# have I given this land, from the river of Egypt unto the great river, the
# river Euphrates;"
m.step("Gen.15.18")
# ‹כָּרַת יְהוָה אֶת־אַבְרָם בְּרִית› (“cut YHWH with Abram covenant”) —
# event: cut-covenant — agent the-LORD; theme brit
m.event("cut_covenant", agent="YHWH", themes=["brit"])
# ‹לְזַרְעֲךָ נָתַתִּי אֶת־הָאָרֶץ הַזֹּאת› (“to-seed-you/your set obj-
# marker the-earth the-this”) — fact holds: to-zarakha-set-obj-marker-the-
# earth-the-this
m.fact("le_zarakha_natati_et_ha_aretz_ha_zot")
# ‹מִנְּהַר מִצְרַיִם עַד־הַנָּהָר הַגָּדֹל נְהַר־פְּרָת› (“from-river Egypt
# until the-river the-great river Euphrates”) — fact holds: from-river-
# Egypt-until-the-river-the-great-river-Euphrates
m.fact("mi_nehar_mitzrayim_ad_ha_nahar_ha_gadol_nehar_perat")
# reads without prior install (flag, not fix): river-Egypt, river-Euphrates
m.presupposed("nahar_mitzrayim", "nehar_perat")
# witness-tier presupposed read: statement_is_a_deed on natati_past_tense —
# read, not installed
m.witness_read("natati_past_tense", "statement_is_a_deed",
                cites=["Bereshit Rabbah 44:22", "Jerusalem Talmud Challah 2:1:3"])

# -------------------------- Gen.15.19 · THE_GRANT_ROSTER_ROW_ONE -----------
# אֶת־הַקֵּינִי וְאֶת־הַקְּנִזִּי וְאֵת הַקַּדְמֹנִי
# "the Kenite, and the Kenizzite, and the Kadmonite,"
m.step("Gen.15.19")
# ‹אֶת־הַקֵּינִי וְאֶת־הַקְּנִזִּי וְאֵת הַקַּדְמֹנִי› (“obj-marker the-
# Kenite and-obj-marker the-Kenizzite and-obj-marker the-Kadmonite”) — fact
# holds: obj-marker-the-Kenite-and-obj-marker-the-Kenizzite-and-obj-marker-
# the-Kadmonite
m.fact("et_ha_qeni_ve_et_ha_qenizi_ve_et_ha_qadmoni")

# -------------------------- Gen.15.20 · THE_GRANT_ROSTER_ROW_TWO -----------
# וְאֶת־הַחִתִּי וְאֶת־הַפְּרִזִּי וְאֶת־הָרְפָאִים
# "and the Hittite, and the Perizzite, and the Rephaim,"
m.step("Gen.15.20")
# ‹וְאֶת־הַחִתִּי וְאֶת־הַפְּרִזִּי וְאֶת־הָרְפָאִים› (“and-obj-marker the-
# Chittite and-obj-marker the-Perizzite and-obj-marker the-Rapha'”) — fact
# holds: and-obj-marker-the-Chittite-and-obj-marker-the-Perizzite-and-obj-
# marker-the-Rapha'
m.fact("ve_et_ha_chiti_ve_et_ha_perizi_ve_et_ha_refaim")

# -------------------------- Gen.15.21 · THE_GRANT_ROSTER_ROW_THREE ---------
# וְאֶת־הָאֱמֹרִי וְאֶת־הַכְּנַעֲנִי וְאֶת־הַגִּרְגָּשִׁי וְאֶת־הַיְבוּסִי
# "and the Amorite, and the Canaanite, and the Girgashite, and the
# Jebusite.'"
m.step("Gen.15.21")
# ‹וְאֶת־הָאֱמֹרִי וְאֶת־הַכְּנַעֲנִי וְאֶת־הַגִּרְגָּשִׁי וְאֶת־הַיְבוּסִי›
# (“and-obj-marker the-Emorite and-obj-marker the-Kenaanite and-obj-marker
# the-Girgashite and-obj-marker the-Jebusite”) — fact holds: and-obj-marker-
# the-Emorite-and-obj-marker-the-Kenaanite-and-obj-marker-the-Girgashite-
# and-obj-marker-the-Jebusite
m.fact("ve_et_ha_emori_ve_et_ha_kenaani_ve_et_ha_girgashi_ve_et_ha_yevusi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'dameseq', 'nahar_mitzrayim', 'nehar_perat', 'ur_kasdim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tira(avram)', 'habet_u_sefor(avram, ha_shamaymah_ve_ha_kokhavim)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['anokhi_magen_lakh', 'sekharkha_harbeh_meod', 'mah_titen_li_ve_anokhi_holekh_ariri', 'ben_mesheq_beti_hu_dameseq_eliezer', 'hen_li_lo_natata_zara', 'ben_beti_yoresh_oti', 'lo_yirashkha_zeh', 'asher_yetze_mi_meekha_hu_yirashekha', 'koh_yihyeh_zarekha', 've_heemin_ba_YHWH', 'va_yachsheveha_lo_tzedaqah', 'ani_YHWH_asher_hotzetikha_me_ur_kasdim', 'la_tet_lekha_et_ha_aretz_ha_zot_le_rishtah', 'ba_mah_eda_ki_irashena', 've_et_ha_tzipor_lo_vatar', 'emah_chashekhah_gedolah_nofelet_alav', 'ger_yihyeh_zarakha_be_eretz_lo_lahem', 'va_avadum_ve_inu_otam_arba_meot_shanah', 'dan_anokhi_et_ha_goy_asher_yaavodu', 've_acharei_khen_yetzu_bi_rekhush_gadol', 'tavo_el_avotekha_be_shalom', 'tiqaver_be_sevah_tovah', 've_dor_revii_yashuvu_henah', 'lo_shalem_avon_ha_emori_ad_henah', 'va_alatah_hayah', 'le_zarakha_natati_et_ha_aretz_ha_zot', 'mi_nehar_mitzrayim_ad_ha_nahar_ha_gadol_nehar_perat', 'et_ha_qeni_ve_et_ha_qenizi_ve_et_ha_qadmoni', 've_et_ha_chiti_ve_et_ha_perizi_ve_et_ha_refaim', 've_et_ha_emori_ve_et_ha_kenaani_ve_et_ha_girgashi_ve_et_ha_yevusi'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    assert sorted(m.WORLD["witnessed"]) == ['the_vision', 'two_clocks']
    assert m.WORLD["witnessed"]['the_vision']["cites"] == ['Bereshit Rabbah 44:21', 'Mekhilta DeRabbi Yishmael, Tractate Bachodesh 9:5', 'Mekhilta DeRabbi Yishmael, Tractate Bachodesh 9:7']
    assert all('decoded_three_ways_with_transposition' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['two_clocks']["cites"] == ['Mishnah Eduyot 2:9', 'Tosefta Eduyot 1:11', 'Mekhilta DeRabbi Yishmael, Tractate Pischa 14:16']
    assert all('conditional_on_conduct' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('brought_him_outside', 'exemption_from_astrology'), ('bamah_eda_question', 'order_of_offerings_instituted'), ('pieces_rite', 'standing_covenant_form'), ('four_hundred_years', 'dated_before_the_call_by_arithmetic'), ('in_peace_clause', 'leave_taking_formula'), ('natati_past_tense', 'statement_is_a_deed')]
    assert m.WITNESS_READS[0]["cites"] == ['Shabbat 156a:13', 'Bereshit Rabbah 44:12']
    assert all('exemption_from_astrology' not in f for f in m.WORLD["facts"])
    assert 'brought_him_outside' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Megillah 31b:5', 'Berakhot 7b:1']
    assert all('order_of_offerings_instituted' not in f for f in m.WORLD["facts"])
    assert 'bamah_eda_question' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifrei Devarim 171:6']
    assert all('standing_covenant_form' not in f for f in m.WORLD["facts"])
    assert 'pieces_rite' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Mekhilta DeRabbi Yishmael, Tractate Pischa 14:15', 'Bereshit Rabbah 39:8', 'Bereshit Rabbah 53:4']
    assert all('dated_before_the_call_by_arithmetic' not in f for f in m.WORLD["facts"])
    assert 'four_hundred_years' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Berakhot 64a:10']
    assert all('leave_taking_formula' not in f for f in m.WORLD["facts"])
    assert 'in_peace_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 44:22', 'Jerusalem Talmud Challah 2:1:3']
    assert all('statement_is_a_deed' not in f for f in m.WORLD["facts"])
    assert 'natati_past_tense' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
