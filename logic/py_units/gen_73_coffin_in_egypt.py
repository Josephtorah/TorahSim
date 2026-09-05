#!/usr/bin/env python3
# =============================================================================
# gen_73_coffin_in_egypt — 50:1-26
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_73_coffin_in_egypt.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""A coffin in Egypt (50:1-26)"""
from machine import Machine

m = Machine("gen_73_coffin_in_egypt")

# -------------------------- Gen.50.1 · WEEPING_ON_THE_FACE -----------------
# ‹וַיִּפֹּל יוֹסֵף עַל־פְּנֵי› (“and-fall Joseph over face”)
# ‹אָבִיו וַיֵּבְךְּ עָלָיו› (“father-him/its and-weep over-him/its”)
# ‹וַיִּשַּׁק־לוֹ› (“and-kiss to-him/its”)
# "[EN-AID] And Joseph fell on his father's face, and wept on him, and
# kissed him."
m.step("Gen.50.1")
# ‹וַיֵּבְךְּ עָלָיו וַיִּשַּׁק־לוֹ› (“and-weep over-him/its and-kiss to-
# him/its”)
# — fact holds: and-weep-alav-and-kiss-not
m.fact("va_yevk_alav_va_yishaq_lo")
# witness-tier presupposed read: the_bill_for_the_silences_falling_due on
# he_fell_on_his_fathers_face — read, not installed
m.witness_read("he_fell_on_his_fathers_face", "the_bill_for_the_silences_falling_due",
                cites=["Bereshit Rabbah 100:3"])

# -------------------------- Gen.50.2 · THE_PHYSICIANS_EMBALM ---------------
# ‹וַיְצַו יוֹסֵף אֶת־עֲבָדָיו› (“and-command Joseph obj-marker servant-
# him/its”)
# ‹אֶת־הָרֹפְאִים לַחֲנֹט אֶת־אָבִיו› (“obj-marker the-mend to-spice obj-
# marker father-him/its”)
# ‹וַיַּחַנְטוּ הָרֹפְאִים אֶת־יִשְׂרָאֵל› (“and-spice the-mend obj-marker
# Israel”)
# "[EN-AID] And Joseph commanded his servants the physicians to embalm his
# father; and the physicians embalmed Israel."
m.step("Gen.50.2")
# ‹וַיַּחַנְטוּ הָרֹפְאִים אֶת־יִשְׂרָאֵל› (“and-spice the-mend obj-marker
# Israel”)
# — fact holds: and-spice-the-mend-obj-marker-Israel
m.fact("va_yachantu_ha_rofim_et_yisrael")

# -------------------------- Gen.50.3 · FORTY_AND_SEVENTY_DAYS --------------
# ‹וַיִּמְלְאוּ־לוֹ אַרְבָּעִים יוֹם› (“and-fill to-him/its forty day”)
# ‹כִּי כֵּן יִמְלְאוּ› (“that so fill”)
# ‹יְמֵי הַחֲנֻטִים וַיִּבְכּוּ› (“day the-spice and-weep”)
# ‹אֹתוֹ מִצְרַיִם שִׁבְעִים› (“obj-marker-him/its Egyptian seventy”)
# ‹יוֹם› (“day”)
# "[EN-AID] And forty days were fulfilled for him, for so are fulfilled the
# days of the embalmed; and Egypt wept for him seventy days."
m.step("Gen.50.3")
# ‹וַיִּבְכּוּ אֹתוֹ מִצְרַיִם› (“and-weep obj-marker-him/its Egyptian”)
# ‹שִׁבְעִים יוֹם› (“seventy day”)
# — fact holds: and-weep-it-Egyptian-seventy-day
m.fact("va_yivku_oto_mitzrayim_shivim_yom")

# -------------------------- Gen.50.4 · SPEAK_IN_PHARAOHS_EARS --------------
# ‹וַיַּעַבְרוּ יְמֵי בְכִיתוֹ› (“and-pass-over day weeping-him/its”)
# ‹וַיְדַבֵּר יוֹסֵף אֶל־בֵּית› (“and-speak Joseph to house”)
# ‹פַּרְעֹה לֵאמֹר אִם־נָא› (“Pharaoh to-say if please”)
# ‹מָצָאתִי חֵן בְּעֵינֵיכֶם› (“find graciousness in-eye-you/your(pl)”)
# ‹דַּבְּרוּ־נָא בְּאָזְנֵי פַרְעֹה› (“speak please in-broadness.-i.e.-the-
# ear Pharaoh”)
# ‹לֵאמֹר› (“to-say”)
# "[EN-AID] And the days of his weeping passed, and Joseph spoke to the
# house of Pharaoh, saying: If, pray, I have found favor in your eyes,
# speak, pray, in the ears of Pharaoh, saying:"
m.step("Gen.50.4")
# ‹דַּבְּרוּ־נָא בְּאָזְנֵי פַרְעֹה› (“speak please in-broadness.-i.e.-the-
# ear Pharaoh”)
# ‹לֵאמֹר› (“to-say”)
# — fact holds: speak-please-in-broadness.-i.e.-the-ear-Pharaoh
m.fact("dabru_na_be_azne_faro")
# witness-grounded state (its own tier):
# a_verb_chosen_by_who_else_is_in_the_room on the_days_of_weeping_passed
m.witness_state("the_days_of_weeping_passed", "a_verb_chosen_by_who_else_is_in_the_room",
                cites=["Bereshit Rabbah 100:4"])

# -------------------------- Gen.50.5 · MY_FATHER_MADE_ME_SWEAR -------------
# ‹אָבִי הִשְׁבִּיעַנִי לֵאמֹר› (“father-me/my swear-me/my to-say”)
# ‹הִנֵּה אָנֹכִי מֵת› (“behold die”)
# ‹בְּקִבְרִי אֲשֶׁר כָּרִיתִי› (“in-sepulchre-me/my which dig”)
# ‹לִי בְּאֶרֶץ כְּנַעַן› (“to-me/my in-earth Canaan”)
# ‹שָׁמָּה תִּקְבְּרֵנִי וְעַתָּה› (“there-ward inter-me/my and-now”)
# ‹אֶעֱלֶה־נָּא וְאֶקְבְּרָה אֶת־אָבִי› (“go-up please and-bury obj-marker
# father-me/my”)
# ‹וְאָשׁוּבָה› (“and-return”)
# "[EN-AID] My father made me swear, saying: Behold, I die — in my grave
# which I dug for myself in the land of Canaan, there shall you bury me. And
# now, let me go up, pray, and bury my father, and return."
m.step("Gen.50.5")
# ‹וְעַתָּה אֶעֱלֶה־נָּא וְאֶקְבְּרָה› (“and-now go-up please and-bury”)
# ‹אֶת־אָבִי וְאָשׁוּבָה› (“obj-marker father-me/my and-return”)
# — Joseph speaks a demand — LET: go-up-please-and-eqbera-obj-marker-avi
m.declare("yosef", "LET",
          "eele_na_ve_eqbera_et_avi")

# -------------------------- Gen.50.6 · GO_UP_AND_BURY ----------------------
# ‹וַיֹּאמֶר פַּרְעֹה עֲלֵה› (“and-say Pharaoh go-up”)
# ‹וּקְבֹר אֶת־אָבִיךָ כַּאֲשֶׁר› (“and-bury obj-marker father-you/your
# like-as/which”)
# ‹הִשְׁבִּיעֶךָ› (“swear-you/your”)
# "[EN-AID] And Pharaoh said: Go up, and bury your father, as he made you
# swear."
m.step("Gen.50.6")
# ‹עֲלֵה וּקְבֹר אֶת־אָבִיךָ› (“go-up and-bury obj-marker father-you/your”)
# ‹כַּאֲשֶׁר הִשְׁבִּיעֶךָ› (“like-as/which swear-you/your”)
# — demand settled (popped from the queue): go-up-please-and-eqbera-obj-
# marker-avi
m.result("eele_na_ve_eqbera_et_avi", tmark="t1")

# -------------------------- Gen.50.7 · ALL_THE_ELDERS_GO_UP ----------------
# ‹וַיַּעַל יוֹסֵף לִקְבֹּר› (“and-go-up Joseph to-inter”)
# ‹אֶת־אָבִיו וַיַּעֲלוּ אִתּוֹ› (“obj-marker father-him/its and-go-up with-
# him/its”)
# ‹כָּל־עַבְדֵי פַרְעֹה זִקְנֵי› (“all servant Pharaoh old”)
# ‹בֵיתוֹ וְכֹל זִקְנֵי› (“house-him/its and-all old”)
# ‹אֶרֶץ־מִצְרָיִם› (“earth Egypt”)
# "[EN-AID] And Joseph went up to bury his father; and there went up with
# him all the servants of Pharaoh, the elders of his house, and all the
# elders of the land of Egypt."
m.step("Gen.50.7")
# ‹וַיַּעֲלוּ אִתּוֹ כָּל־עַבְדֵי› (“and-go-up with-him/its all servant”)
# ‹פַרְעֹה› (“Pharaoh”)
# — fact holds: and-go-up-with-him-all-servant-Pharaoh
m.fact("va_yaalu_ito_kol_avde_faro")

# -------------------------- Gen.50.8 · ONLY_THE_LITTLE_ONES_REMAIN ---------
# ‹וְכֹל בֵּית יוֹסֵף› (“and-all house Joseph”)
# ‹וְאֶחָיו וּבֵית אָבִיו› (“and-brother-him/its and-house father-him/its”)
# ‹רַק טַפָּם וְצֹאנָם› (“leanness family-them/their and-flock-them/their”)
# ‹וּבְקָרָם עָזְבוּ בְּאֶרֶץ› (“and-herd-them/their loosen in-earth”)
# ‹גֹּשֶׁן› (“Goshen”)
# "[EN-AID] And all the house of Joseph, and his brothers, and his father's
# house; only their little ones, and their flocks, and their herds, they
# left in the land of Goshen."
m.step("Gen.50.8")
# ‹רַק טַפָּם וְצֹאנָם› (“leanness family-them/their and-flock-them/their”)
# ‹וּבְקָרָם עָזְבוּ בְּאֶרֶץ› (“and-herd-them/their loosen in-earth”)
# ‹גֹּשֶׁן› (“Goshen”)
# — fact holds: leanness-tapam-and-tzonam-loosen-in-Goshen
m.fact("raq_tapam_ve_tzonam_azvu_be_goshen")

# -------------------------- Gen.50.9 · CHARIOTS_AND_HORSEMEN ---------------
# ‹וַיַּעַל עִמּוֹ גַּם־רֶכֶב› (“and-go-up with-him/its also vehicle”)
# ‹גַּם־פָּרָשִׁים וַיְהִי הַמַּחֲנֶה› (“also steed and-be the-camp”)
# ‹כָּבֵד מְאֹד› (“heavy very”)
# "[EN-AID] And there went up with him both chariots and horsemen; and the
# camp was very heavy."
m.step("Gen.50.9")
# ‹וַיְהִי הַמַּחֲנֶה כָּבֵד› (“and-be the-camp heavy”)
# ‹מְאֹד› (“very”)
# — fact holds: and-be-the-camp-heavy-very
m.fact("va_yehi_ha_machane_kaved_meod")

# -------------------------- Gen.50.10 · THE_MOURNING_AT_THE_THRESHING_FLOOR -
# ‹וַיָּבֹאוּ עַד־גֹּרֶן הָאָטָד› (“and-come/bring until threshing-floor
# thorn-tree”)
# ‹אֲשֶׁר בְּעֵבֶר הַיַּרְדֵּן› (“which in-region-across the-Jordan”)
# ‹וַיִּסְפְּדוּ־שָׁם מִסְפֵּד גָּדוֹל› (“and-tear-the-hair-and-beat-the-b
# there lamentation great”)
# ‹וְכָבֵד מְאֹד וַיַּעַשׂ› (“and-heavy very and-make”)
# ‹לְאָבִיו אֵבֶל שִׁבְעַת› (“to-father-him/its lamentation seven”)
# ‹יָמִים› (“day”)
# "[EN-AID] And they came to the threshing floor of Atad, which is across
# the Jordan, and they mourned there a great and very heavy mourning; and he
# made for his father a mourning of seven days."
m.step("Gen.50.10")
# ‹וַיַּעַשׂ לְאָבִיו אֵבֶל› (“and-make to-father-him/its lamentation”)
# ‹שִׁבְעַת יָמִים› (“seven day”)
# — fact holds: lamentation-seven-day
m.fact("evel_shivat_yamim")
# witness-grounded state (its own tier):
# a_search_of_scripture_reported_and_confirmed_where_we_can_see on
# the_threshing_floor_of_atad
m.witness_state("the_threshing_floor_of_atad", "a_search_of_scripture_reported_and_confirmed_where_we_can_see",
                cites=["Bereshit Rabbah 100:6", "Bereshit Rabbah 100:7"])
# witness-tier presupposed read: mourning_duration on evel_shivat_yamim —
# read, not installed
m.witness_read("evel_shivat_yamim", "mourning_duration",
                cites=["Shabbat 152a:14", "Shabbat 152a:15", "Shabbat 152a:16"])

# -------------------------- Gen.50.11 · MOURNING_OF_EGYPT ------------------
# ‹וַיַּרְא יוֹשֵׁב הָאָרֶץ› (“and-see dwell/sit the-earth”)
# ‹הַכְּנַעֲנִי אֶת־הָאֵבֶל בְּגֹרֶן› (“the-Kenaanite obj-marker the-
# lamentation in-threshing-floor”)
# ‹הָאָטָד וַיֹּאמְרוּ אֵבֶל־כָּבֵד› (“thorn-tree and-say lamentation
# heavy”)
# ‹זֶה לְמִצְרָיִם עַל־כֵּן› (“this to-Egyptian over so”)
# ‹קָרָא שְׁמָהּ אָבֵל› (“call name-her/its”)
# ‹מִצְרַיִם אֲשֶׁר בְּעֵבֶר› (“Abel-mizraim which in-region-across”)
# ‹הַיַּרְדֵּן› (“the-Jordan”)
# "[EN-AID] And the Canaanite inhabitant of the land saw the mourning at the
# threshing floor of Atad, and they said: This is a heavy mourning for
# Egypt. Therefore its name was called Avel Mitzrayim, which is across the
# Jordan."
m.step("Gen.50.11")
# ‹כֵּן קָרָא שְׁמָהּ› (“so call name-her/its”)
# ‹אָבֵל מִצְרַיִם› (“Abel-mizraim”)
# — named: threshing-floor-the-atad := avel-Egyptian
m.name("goren_ha_atad", "avel_mitzrayim")

# -------------------------- Gen.50.12 · AS_HE_CHARGED_THEM -----------------
# ‹וַיַּעֲשׂוּ בָנָיו לוֹ› (“and-make son-him/its to-him/its”)
# ‹כֵּן כַּאֲשֶׁר צִוָּם› (“so like-as/which command-them/their”)
# "[EN-AID] And his sons did for him so, exactly as he charged them."
m.step("Gen.50.12")
# ‹וַיַּעֲשׂוּ בָנָיו לוֹ› (“and-make son-him/its to-him/its”)
# ‹כֵּן כַּאֲשֶׁר צִוָּם› (“so like-as/which command-them/their”)
# — fact holds: and-make-vanav-not-so-kaasher-tzivam
m.fact("va_yaasu_vanav_lo_ken_kaasher_tzivam")

# -------------------------- Gen.50.13 · BURIED_IN_MACHPELAH ----------------
# ‹וַיִּשְׂאוּ אֹתוֹ בָנָיו› (“and-lift/carry obj-marker-him/its son-
# him/its”)
# ‹אַרְצָה כְּנַעַן וַיִּקְבְּרוּ› (“earth-ward Canaan and-bury”)
# ‹אֹתוֹ בִּמְעָרַת שְׂדֵה› (“obj-marker-him/its in-cavern field”)
# ‹הַמַּכְפֵּלָה אֲשֶׁר קָנָה› (“the-Machpelah which possessor”)
# ‹אַבְרָהָם אֶת־הַשָּׂדֶה לַאֲחֻזַּת־קֶבֶר› (“Abraham obj-marker the-field
# to-something-seized sepulchre”)
# ‹מֵאֵת עֶפְרֹן הַחִתִּי› (“from-with Ephron the-Chittite”)
# ‹עַל־פְּנֵי מַמְרֵא› (“over face Mamre”)
# "[EN-AID] And his sons carried him to the land of Canaan, and buried him
# in the cave of the field of Machpelah — which field Abraham had bought for
# a burial holding from Ephron the Hittite, before Mamre."
m.step("Gen.50.13")
# ‹וַיִּקְבְּרוּ אֹתוֹ בִּמְעָרַת› (“and-bury obj-marker-him/its in-cavern”)
# ‹שְׂדֵה הַמַּכְפֵּלָה› (“field the-Machpelah”)
# — fact holds: and-yiqberu-it-bi-mearat-field-the-Machpelah
m.fact("va_yiqberu_oto_bi_mearat_sede_ha_makhpela")
# witness-tier presupposed read: the_deed_produced_against_a_contest on
# they_buried_him_in_the_cave — read, not installed
m.witness_read("they_buried_him_in_the_cave", "the_deed_produced_against_a_contest",
                cites=["Bereshit Rabbah 98:17", "Bereshit Rabbah 100:5"])

# -------------------------- Gen.50.14 · THE_RETURN_KEPT --------------------
# ‹וַיָּשָׁב יוֹסֵף מִצְרַיְמָה› (“and-return Joseph Egypt-ward”)
# ‹הוּא וְאֶחָיו וְכָל־הָעֹלִים› (“he/it and-brother-him/its and-all the-go-
# up”)
# ‹אִתּוֹ לִקְבֹּר אֶת־אָבִיו› (“with-him/its to-inter obj-marker father-
# him/its”)
# ‹אַחֲרֵי קָבְרוֹ אֶת־אָבִיו› (“after inter-him/its obj-marker father-
# him/its”)
# "[EN-AID] And Joseph returned to Egypt, he and his brothers, and all who
# went up with him to bury his father, after he had buried his father."
m.step("Gen.50.14")
# ‹וַיָּשָׁב יוֹסֵף מִצְרַיְמָה› (“and-return Joseph Egypt-ward”)
# — fact holds: and-return-Joseph-mitzrayma
m.fact("va_yashav_yosef_mitzrayma")

# -------------------------- Gen.50.15 · WHAT_IF_JOSEPH_HATES_US ------------
# ‹וַיִּרְאוּ אֲחֵי־יוֹסֵף כִּי־מֵת› (“and-see brother Joseph that die”)
# ‹אֲבִיהֶם וַיֹּאמְרוּ לוּ› (“father-them/their and-say conditional-
# particle”)
# ‹יִשְׂטְמֵנוּ יוֹסֵף וְהָשֵׁב› (“lurk-for-us/our Joseph and-return”)
# ‹יָשִׁיב לָנוּ אֵת› (“return to-us/our obj-marker”)
# ‹כָּל־הָרָעָה אֲשֶׁר גָּמַלְנוּ› (“all the-bad which treat-a-person”)
# ‹אֹתוֹ› (“obj-marker-him/its”)
# "[EN-AID] And Joseph's brothers saw that their father was dead, and they
# said: What if Joseph hates us, and surely returns to us all the evil which
# we dealt him."
m.step("Gen.50.15")
# ‹וַיֹּאמְרוּ לוּ יִשְׂטְמֵנוּ› (“and-say conditional-particle lurk-for-
# us/our”)
# ‹יוֹסֵף› (“Joseph”)
# — fact holds: conditional-particle-yistemenu-Joseph
m.fact("lu_yistemenu_yosef")

# -------------------------- Gen.50.16 · THE_FABRICATED_CHARGE --------------
# ‹וַיְצַוּוּ אֶל־יוֹסֵף לֵאמֹר› (“and-command to Joseph to-say”)
# ‹אָבִיךָ צִוָּה לִפְנֵי› (“father-you/your command to-face”)
# ‹מוֹתוֹ לֵאמֹר› (“death-him/its to-say”)
# "[EN-AID] And they commanded to Joseph, saying: Your father charged before
# his death, saying:"
m.step("Gen.50.16")
# ‹אָבִיךָ צִוָּה לִפְנֵי› (“father-you/your command to-face”)
# ‹מוֹתוֹ› (“death-him/its”)
# — fact holds: avikha-command-lifne-moto
m.fact("avikha_tziva_lifne_moto")
# witness-grounded state (its own tier):
# an_untruth_licensed_by_its_absence_from_the_record on
# your_father_commanded
m.witness_state("your_father_commanded", "an_untruth_licensed_by_its_absence_from_the_record",
                cites=["Bereshit Rabbah 100:8"])

# -------------------------- Gen.50.17 · FORGIVE_THE_CRIME ------------------
# ‹כֹּה־תֹאמְרוּ לְיוֹסֵף אָנָּא› (“like-this say to-Joseph oh-now!”)
# ‹שָׂא נָא פֶּשַׁע› (“lift/carry please revolt”)
# ‹אַחֶיךָ וְחַטָּאתָם כִּי־רָעָה› (“brother-you/your and-sin-offering-
# them/their that bad”)
# ‹גְמָלוּךָ וְעַתָּה שָׂא› (“treat-a-person-you/your and-now lift/carry”)
# ‹נָא לְפֶשַׁע עַבְדֵי› (“please to-revolt servant”)
# ‹אֱלֹהֵי אָבִיךָ וַיֵּבְךְּ› (“God father-you/your and-weep”)
# ‹יוֹסֵף בְּדַבְּרָם אֵלָיו› (“Joseph in-speak-them/their to-him/its”)
# "[EN-AID] So shall you say to Joseph: Please, forgive, pray, the crime of
# your brothers and their sin, for evil they dealt you; and now, forgive,
# pray, the crime of the servants of the God of your father. And Joseph wept
# at their speaking to him."
m.step("Gen.50.17")
# ‹וְעַתָּה שָׂא נָא› (“and-now lift/carry please”)
# ‹לְפֶשַׁע עַבְדֵי אֱלֹהֵי› (“to-revolt servant God”)
# ‹אָבִיךָ› (“father-you/your”)
# — brother-Joseph speaks a demand — LET: lift/carry-please-to-revolt-
# servant-God-avikha
m.declare("ache_yosef", "LET",
          "sa_na_le_fesha_avde_elohe_avikha")
# witness-tier presupposed read: forgiveness_ask_limit on sa_na_ve_ata_sa_na
# — read, not installed
m.witness_read("sa_na_ve_ata_sa_na", "forgiveness_ask_limit",
                cites=["Yoma 87a:12", "Yoma 87a:13", "Yoma 87a:14"])

# -------------------------- Gen.50.18 · BEHOLD_US_AS_SERVANTS --------------
# ‹וַיֵּלְכוּ גַּם־אֶחָיו וַיִּפְּלוּ› (“and-go also brother-him/its and-
# fall”)
# ‹לְפָנָיו וַיֹּאמְרוּ הִנֶּנּוּ› (“to-face-him/its and-say behold-us/our”)
# ‹לְךָ לַעֲבָדִים› (“to-you/your to-servant”)
# "[EN-AID] And his brothers went also and fell before him; and they said:
# Behold us — yours, as servants."
m.step("Gen.50.18")
# ‹וַיֹּאמְרוּ הִנֶּנּוּ לְךָ› (“and-say behold-us/our to-you/your”)
# ‹לַעֲבָדִים› (“to-servant”)
# — fact holds: hinenu-to-you-to-servant
m.fact("hinenu_lekha_la_avadim")

# -------------------------- Gen.50.19 · AM_I_IN_PLACE_OF_GOD ---------------
# ‹וַיֹּאמֶר אֲלֵהֶם יוֹסֵף› (“and-say to-them/their Joseph”)
# ‹אַל־תִּירָאוּ כִּי הֲתַחַת› (“do-not fear that the-under”)
# ‹אֱלֹהִים אָנִי› (“God”)
# "[EN-AID] And Joseph said to them: Fear not — for am I in place of God?"
m.step("Gen.50.19")
# ‹כִּי הֲתַחַת אֱלֹהִים› (“that the-under God”)
# ‹אָנִי› (“?”)
# — fact holds: the-under-God-ani
m.fact("ha_tachat_elohim_ani")
# witness-grounded state (its own tier):
# a_question_turned_into_a_declaration on am_i_in_the_place_of_god
m.witness_state("am_i_in_the_place_of_god", "a_question_turned_into_a_declaration",
                cites=["Onkelos Genesis 50:19"])

# -------------------------- Gen.50.20 · YOU_DEVISED_GOD_DEVISED ------------
# ‹וְאַתֶּם חֲשַׁבְתֶּם עָלַי› (“and-you plait over-me/my”)
# ‹רָעָה אֱלֹהִים חֲשָׁבָהּ› (“bad God plait-her/its”)
# ‹לְטֹבָה לְמַעַן עֲשֹׂה› (“to-good-in-the-widest-sense so-that make”)
# ‹כַּיּוֹם הַזֶּה לְהַחֲיֹת› (“like-day the-this to-live”)
# ‹עַם־רָב› (“people many/great”)
# "[EN-AID] And you — you devised evil against me; God devised it for good,
# in order to do as this day — to keep alive a great people."
m.step("Gen.50.20")
# ‹אֱלֹהִים חֲשָׁבָהּ לְטֹבָה› (“God plait-her/its to-good-in-the-widest-
# sense”)
# — fact holds: God-chashavah-to-tovah
m.fact("elohim_chashavah_le_tovah")

# -------------------------- Gen.50.21 · I_WILL_SUSTAIN_YOU -----------------
# ‹וְעַתָּה אַל־תִּירָאוּ אָנֹכִי› (“and-now do-not fear”)
# ‹אֲכַלְכֵּל אֶתְכֶם וְאֶת־טַפְּכֶם› (“keep-in obj-marker-you/your(pl) and-
# obj-marker family-you/your(pl)”)
# ‹וַיְנַחֵם אוֹתָם וַיְדַבֵּר› (“and-sigh obj-marker-them/their and-speak”)
# ‹עַל־לִבָּם› (“over heart-them/their”)
# "[EN-AID] And now, fear not — I will sustain you, and your little ones.
# And he comforted them, and spoke to their heart."
m.step("Gen.50.21")
# ‹וַיְנַחֵם אוֹתָם וַיְדַבֵּר› (“and-sigh obj-marker-them/their and-speak”)
# ‹עַל־לִבָּם› (“over heart-them/their”)
# — demand settled (popped from the queue): lift/carry-please-to-revolt-
# servant-God-avikha
m.result("sa_na_le_fesha_avde_elohe_avikha", tmark="t2")
# witness-tier presupposed read:
# consolation_argued_from_cosmology_and_self_interest on
# he_spoke_to_their_heart — read, not installed
m.witness_read("he_spoke_to_their_heart", "consolation_argued_from_cosmology_and_self_interest",
                cites=["Bereshit Rabbah 100:9"])

# -------------------------- Gen.50.22 · A_HUNDRED_AND_TEN ------------------
# ‹וַיֵּשֶׁב יוֹסֵף בְּמִצְרַיִם› (“and-dwell/sit Joseph in-Egypt”)
# ‹הוּא וּבֵית אָבִיו› (“he/it and-house father-him/its”)
# ‹וַיְחִי יוֹסֵף מֵאָה› (“and-live Joseph hundred”)
# ‹וָעֶשֶׂר שָׁנִים› (“and-ten years”)
# "[EN-AID] And Joseph dwelt in Egypt, he and his father's house; and Joseph
# lived a hundred and ten years."
m.step("Gen.50.22")
# ‹וַיְחִי יוֹסֵף מֵאָה› (“and-live Joseph hundred”)
# ‹וָעֶשֶׂר שָׁנִים› (“and-ten years”)
# — fact holds: and-live-Joseph-hundred-and-ten-years
m.fact("va_yechi_yosef_mea_va_eser_shanim")
# witness-grounded state (its own tier): a_census_of_equal_lifespans_graded
# on one_hundred_and_ten_years
m.witness_state("one_hundred_and_ten_years", "a_census_of_equal_lifespans_graded",
                cites=["Bereshit Rabbah 100:10"])

# -------------------------- Gen.50.23 · ON_JOSEPHS_KNEES -------------------
# ‹וַיַּרְא יוֹסֵף לְאֶפְרַיִם› (“and-see Joseph to-Ephraim”)
# ‹בְּנֵי שִׁלֵּשִׁים גַּם› (“son descendant-of-the-third-degr also”)
# ‹בְּנֵי מָכִיר בֶּן־מְנַשֶּׁה› (“son Machir son Manasseh”)
# ‹יֻלְּדוּ עַל־בִּרְכֵּי יוֹסֵף› (“bear-young over knee Joseph”)
# "[EN-AID] And Joseph saw, of Ephraim, children of the third generation;
# also the sons of Machir, son of Manasseh, were born on Joseph's knees."
m.step("Gen.50.23")
# ‹יֻלְּדוּ עַל־בִּרְכֵּי יוֹסֵף› (“bear-young over knee Joseph”)
# — fact holds: bear-young-over-knee-Joseph
m.fact("yuldu_al_birke_yosef")

# -------------------------- Gen.50.24 · GOD_WILL_SURELY_VISIT --------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו› (“and-say Joseph to brother-him/its”)
# ‹אָנֹכִי מֵת וֵאלֹהִים› (“die and-God”)
# ‹פָּקֹד יִפְקֹד אֶתְכֶם› (“count/visit count/visit obj-marker-
# you/your(pl)”)
# ‹וְהֶעֱלָה אֶתְכֶם מִן־הָאָרֶץ› (“and-go-up obj-marker-you/your(pl) from
# the-earth”)
# ‹הַזֹּאת אֶל־הָאָרֶץ אֲשֶׁר› (“the-this to the-earth which”)
# ‹נִשְׁבַּע לְאַבְרָהָם לְיִצְחָק› (“swear to-Abraham to-Isaac”)
# ‹וּלְיַעֲקֹב› (“and-to-Jacob”)
# "[EN-AID] And Joseph said to his brothers: I die; and God will surely
# visit you, and bring you up from this land to the land which He swore to
# Abraham, to Isaac, and to Jacob."
m.step("Gen.50.24")
# ‹וֵאלֹהִים פָּקֹד יִפְקֹד› (“and-God count/visit count/visit”)
# ‹אֶתְכֶם› (“obj-marker-you/your(pl)”)
# — fact holds: God-count/visit-count/visit-etkhem
m.fact("elohim_paqod_yifqod_etkhem")

# -------------------------- Gen.50.25 · THE_BONES_OATH ---------------------
# ‹וַיַּשְׁבַּע יוֹסֵף אֶת־בְּנֵי› (“and-swear Joseph obj-marker son”)
# ‹יִשְׂרָאֵל לֵאמֹר פָּקֹד› (“Israel to-say count/visit”)
# ‹יִפְקֹד אֱלֹהִים אֶתְכֶם› (“count/visit God obj-marker-you/your(pl)”)
# ‹וְהַעֲלִתֶם אֶת־עַצְמֹתַי מִזֶּה› (“and-go-up obj-marker bone-me/my from-
# this”)
# "[EN-AID] And Joseph made the sons of Israel swear, saying: God will
# surely visit you — and you shall bring up my bones from here."
m.step("Gen.50.25")
# ‹וְהַעֲלִתֶם אֶת־עַצְמֹתַי מִזֶּה› (“and-go-up obj-marker bone-me/my from-
# this”)
# — Joseph speaks a demand — LET: and-go-up-obj-marker-atzmotai-from-this
m.declare("yosef", "LET",
          "ve_haalitem_et_atzmotai_mi_ze")
# witness-grounded state (its own tier): the_hinge_into_the_next_book on
# you_shall_carry_my_bones_up
m.witness_state("you_shall_carry_my_bones_up", "the_hinge_into_the_next_book",
                cites=["Bereshit Rabbah 100:11"])

# -------------------------- Gen.50.26 · A_COFFIN_IN_EGYPT ------------------
# ‹וַיָּמָת יוֹסֵף בֶּן־מֵאָה› (“and-die Joseph son hundred”)
# ‹וָעֶשֶׂר שָׁנִים וַיַּחַנְטוּ› (“and-ten years and-spice”)
# ‹אֹתוֹ וַיִּישֶׂם בָּאָרוֹן› (“obj-marker-him/its and-place in-ark”)
# ‹בְּמִצְרָיִם› (“in-Egypt”)
# "[EN-AID] And Joseph died, a hundred and ten years old; and they embalmed
# him, and he was placed in a coffin in Egypt."
m.step("Gen.50.26")
# ‹וַיַּחַנְטוּ אֹתוֹ וַיִּישֶׂם› (“and-spice obj-marker-him/its and-place”)
# ‹בָּאָרוֹן בְּמִצְרָיִם› (“in-ark in-Egypt”)
# — event: die — agent Joseph
m.event("met", agent="yosef")
# witness-grounded state (its own tier):
# present_in_the_reading_shelf_absent_from_our_layer on the_closing_token
m.witness_state("the_closing_token", "present_in_the_reading_shelf_absent_from_our_layer",
                cites=["Onkelos Genesis 50:26", "Bereshit Rabbah 100:12"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'goren_ha_atad': 'avel_mitzrayim'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['ve_haalitem_et_atzmotai_mi_ze']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yevk_alav_va_yishaq_lo', 'va_yachantu_ha_rofim_et_yisrael', 'va_yivku_oto_mitzrayim_shivim_yom', 'dabru_na_be_azne_faro', 'va_yaalu_ito_kol_avde_faro', 'raq_tapam_ve_tzonam_azvu_be_goshen', 'va_yehi_ha_machane_kaved_meod', 'evel_shivat_yamim', 'va_yaasu_vanav_lo_ken_kaasher_tzivam', 'va_yiqberu_oto_bi_mearat_sede_ha_makhpela', 'va_yashav_yosef_mitzrayma', 'lu_yistemenu_yosef', 'avikha_tziva_lifne_moto', 'hinenu_lekha_la_avadim', 'ha_tachat_elohim_ani', 'elohim_chashavah_le_tovah', 'va_yechi_yosef_mea_va_eser_shanim', 'yuldu_al_birke_yosef', 'elohim_paqod_yifqod_etkhem'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    assert sorted(m.WORLD["witnessed"]) == ['am_i_in_the_place_of_god', 'one_hundred_and_ten_years', 'the_closing_token', 'the_days_of_weeping_passed', 'the_threshing_floor_of_atad', 'you_shall_carry_my_bones_up', 'your_father_commanded']
    assert m.WORLD["witnessed"]['am_i_in_the_place_of_god']["cites"] == ['Onkelos Genesis 50:19']
    assert all('a_question_turned_into_a_declaration' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['one_hundred_and_ten_years']["cites"] == ['Bereshit Rabbah 100:10']
    assert all('a_census_of_equal_lifespans_graded' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_closing_token']["cites"] == ['Onkelos Genesis 50:26', 'Bereshit Rabbah 100:12']
    assert all('present_in_the_reading_shelf_absent_from_our_layer' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_days_of_weeping_passed']["cites"] == ['Bereshit Rabbah 100:4']
    assert all('a_verb_chosen_by_who_else_is_in_the_room' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_threshing_floor_of_atad']["cites"] == ['Bereshit Rabbah 100:6', 'Bereshit Rabbah 100:7']
    assert all('a_search_of_scripture_reported_and_confirmed_where_we_can_see' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['you_shall_carry_my_bones_up']["cites"] == ['Bereshit Rabbah 100:11']
    assert all('the_hinge_into_the_next_book' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['your_father_commanded']["cites"] == ['Bereshit Rabbah 100:8']
    assert all('an_untruth_licensed_by_its_absence_from_the_record' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('he_fell_on_his_fathers_face', 'the_bill_for_the_silences_falling_due'), ('evel_shivat_yamim', 'mourning_duration'), ('they_buried_him_in_the_cave', 'the_deed_produced_against_a_contest'), ('sa_na_ve_ata_sa_na', 'forgiveness_ask_limit'), ('he_spoke_to_their_heart', 'consolation_argued_from_cosmology_and_self_interest')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 100:3']
    assert all('the_bill_for_the_silences_falling_due' not in f for f in m.WORLD["facts"])
    assert 'he_fell_on_his_fathers_face' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Shabbat 152a:14', 'Shabbat 152a:15', 'Shabbat 152a:16']
    assert all('mourning_duration' not in f for f in m.WORLD["facts"])
    assert 'evel_shivat_yamim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 98:17', 'Bereshit Rabbah 100:5']
    assert all('the_deed_produced_against_a_contest' not in f for f in m.WORLD["facts"])
    assert 'they_buried_him_in_the_cave' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Yoma 87a:12', 'Yoma 87a:13', 'Yoma 87a:14']
    assert all('forgiveness_ask_limit' not in f for f in m.WORLD["facts"])
    assert 'sa_na_ve_ata_sa_na' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 100:9']
    assert all('consolation_argued_from_cosmology_and_self_interest' not in f for f in m.WORLD["facts"])
    assert 'he_spoke_to_their_heart' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
