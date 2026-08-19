#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיִּפֹּל יוֹסֵף עַל־פְּנֵי אָבִיו וַיֵּבְךְּ עָלָיו וַיִּשַּׁק־לוֹ
# "[EN-AID] And Joseph fell on his father's face, and wept on him, and
# kissed him."
m.step("Gen.50.1")
# ‹וַיֵּבְךְּ עָלָיו וַיִּשַּׁק־לוֹ› (“and-weep over-him/its and-kiss to-
# him/its”) — fact holds: and-weep-alav-and-kiss-not
m.fact("va_yevk_alav_va_yishaq_lo")

# -------------------------- Gen.50.2 · THE_PHYSICIANS_EMBALM ---------------
# וַיְצַו יוֹסֵף אֶת־עֲבָדָיו אֶת־הָרֹפְאִים לַחֲנֹט אֶת־אָבִיו וַיַּחַנְטוּ
# הָרֹפְאִים אֶת־יִשְׂרָאֵל
# "[EN-AID] And Joseph commanded his servants the physicians to embalm his
# father; and the physicians embalmed Israel."
m.step("Gen.50.2")
# ‹וַיַּחַנְטוּ הָרֹפְאִים אֶת־יִשְׂרָאֵל› (“and-spice the-mend obj-marker
# Israel”) — fact holds: and-spice-the-mend-obj-marker-Israel
m.fact("va_yachantu_ha_rofim_et_yisrael")

# -------------------------- Gen.50.3 · FORTY_AND_SEVENTY_DAYS --------------
# וַיִּמְלְאוּ־לוֹ אַרְבָּעִים יוֹם כִּי כֵּן יִמְלְאוּ יְמֵי הַחֲנֻטִים
# וַיִּבְכּוּ אֹתוֹ מִצְרַיִם שִׁבְעִים יוֹם
# "[EN-AID] And forty days were fulfilled for him, for so are fulfilled the
# days of the embalmed; and Egypt wept for him seventy days."
m.step("Gen.50.3")
# ‹וַיִּבְכּוּ אֹתוֹ מִצְרַיִם שִׁבְעִים יוֹם› (“and-weep obj-marker-him/its
# Egyptian seventy day”) — fact holds: and-weep-it-Egyptian-seventy-day
m.fact("va_yivku_oto_mitzrayim_shivim_yom")

# -------------------------- Gen.50.4 · SPEAK_IN_PHARAOHS_EARS --------------
# וַיַּעַבְרוּ יְמֵי בְכִיתוֹ וַיְדַבֵּר יוֹסֵף אֶל־בֵּית פַּרְעֹה לֵאמֹר
# אִם־נָא מָצָאתִי חֵן בְּעֵינֵיכֶם דַּבְּרוּ־נָא בְּאָזְנֵי פַרְעֹה לֵאמֹר
# "[EN-AID] And the days of his weeping passed, and Joseph spoke to the
# house of Pharaoh, saying: If, pray, I have found favor in your eyes,
# speak, pray, in the ears of Pharaoh, saying:"
m.step("Gen.50.4")
# ‹דַּבְּרוּ־נָא בְּאָזְנֵי פַרְעֹה לֵאמֹר› (“speak please in-
# broadness.-i.e.-the-ear Pharaoh to-say”) — fact holds: speak-please-in-
# broadness.-i.e.-the-ear-Pharaoh
m.fact("dabru_na_be_azne_faro")

# -------------------------- Gen.50.5 · MY_FATHER_MADE_ME_SWEAR -------------
# אָבִי הִשְׁבִּיעַנִי לֵאמֹר הִנֵּה אָנֹכִי מֵת בְּקִבְרִי אֲשֶׁר כָּרִיתִי
# לִי בְּאֶרֶץ כְּנַעַן שָׁמָּה תִּקְבְּרֵנִי וְעַתָּה אֶעֱלֶה־נָּא
# וְאֶקְבְּרָה אֶת־אָבִי וְאָשׁוּבָה
# "[EN-AID] My father made me swear, saying: Behold, I die — in my grave
# which I dug for myself in the land of Canaan, there shall you bury me. And
# now, let me go up, pray, and bury my father, and return."
m.step("Gen.50.5")
# ‹וְעַתָּה אֶעֱלֶה־נָּא וְאֶקְבְּרָה אֶת־אָבִי וְאָשׁוּבָה› (“and-now go-up
# please and-bury obj-marker father-me/my and-return”) — Joseph speaks a
# demand — LET: go-up-please-and-eqbera-obj-marker-avi
m.declare("yosef", "LET",
          "eele_na_ve_eqbera_et_avi")

# -------------------------- Gen.50.6 · GO_UP_AND_BURY ----------------------
# וַיֹּאמֶר פַּרְעֹה עֲלֵה וּקְבֹר אֶת־אָבִיךָ כַּאֲשֶׁר הִשְׁבִּיעֶךָ
# "[EN-AID] And Pharaoh said: Go up, and bury your father, as he made you
# swear."
m.step("Gen.50.6")
# ‹עֲלֵה וּקְבֹר אֶת־אָבִיךָ כַּאֲשֶׁר הִשְׁבִּיעֶךָ› (“go-up and-bury obj-
# marker father-you/your like-as/which swear-you/your”) — demand settled
# (popped from the queue): go-up-please-and-eqbera-obj-marker-avi
m.result("eele_na_ve_eqbera_et_avi", tmark="t1")

# -------------------------- Gen.50.7 · ALL_THE_ELDERS_GO_UP ----------------
# וַיַּעַל יוֹסֵף לִקְבֹּר אֶת־אָבִיו וַיַּעֲלוּ אִתּוֹ כָּל־עַבְדֵי פַרְעֹה
# זִקְנֵי בֵיתוֹ וְכֹל זִקְנֵי אֶרֶץ־מִצְרָיִם
# "[EN-AID] And Joseph went up to bury his father; and there went up with
# him all the servants of Pharaoh, the elders of his house, and all the
# elders of the land of Egypt."
m.step("Gen.50.7")
# ‹וַיַּעֲלוּ אִתּוֹ כָּל־עַבְדֵי פַרְעֹה› (“and-go-up with-him/its all
# servant Pharaoh”) — fact holds: and-go-up-with-him-all-servant-Pharaoh
m.fact("va_yaalu_ito_kol_avde_faro")

# -------------------------- Gen.50.8 · ONLY_THE_LITTLE_ONES_REMAIN ---------
# וְכֹל בֵּית יוֹסֵף וְאֶחָיו וּבֵית אָבִיו רַק טַפָּם וְצֹאנָם וּבְקָרָם
# עָזְבוּ בְּאֶרֶץ גֹּשֶׁן
# "[EN-AID] And all the house of Joseph, and his brothers, and his father's
# house; only their little ones, and their flocks, and their herds, they
# left in the land of Goshen."
m.step("Gen.50.8")
# ‹רַק טַפָּם וְצֹאנָם וּבְקָרָם עָזְבוּ בְּאֶרֶץ גֹּשֶׁן› (“leanness
# family-them/their and-flock-them/their and-herd-them/their loosen in-earth
# Goshen”) — fact holds: leanness-tapam-and-tzonam-loosen-in-Goshen
m.fact("raq_tapam_ve_tzonam_azvu_be_goshen")

# -------------------------- Gen.50.9 · CHARIOTS_AND_HORSEMEN ---------------
# וַיַּעַל עִמּוֹ גַּם־רֶכֶב גַּם־פָּרָשִׁים וַיְהִי הַמַּחֲנֶה כָּבֵד מְאֹד
# "[EN-AID] And there went up with him both chariots and horsemen; and the
# camp was very heavy."
m.step("Gen.50.9")
# ‹וַיְהִי הַמַּחֲנֶה כָּבֵד מְאֹד› (“and-be the-camp heavy very”) — fact
# holds: and-be-the-camp-heavy-very
m.fact("va_yehi_ha_machane_kaved_meod")

# -------------------------- Gen.50.10 · THE_MOURNING_AT_THE_THRESHING_FLOOR -
# וַיָּבֹאוּ עַד־גֹּרֶן הָאָטָד אֲשֶׁר בְּעֵבֶר הַיַּרְדֵּן
# וַיִּסְפְּדוּ־שָׁם מִסְפֵּד גָּדוֹל וְכָבֵד מְאֹד וַיַּעַשׂ לְאָבִיו אֵבֶל
# שִׁבְעַת יָמִים
# "[EN-AID] And they came to the threshing floor of Atad, which is across
# the Jordan, and they mourned there a great and very heavy mourning; and he
# made for his father a mourning of seven days."
m.step("Gen.50.10")
# ‹וַיַּעַשׂ לְאָבִיו אֵבֶל שִׁבְעַת יָמִים› (“and-make to-father-him/its
# lamentation seven day”) — fact holds: lamentation-seven-day
m.fact("evel_shivat_yamim")

# -------------------------- Gen.50.11 · MOURNING_OF_EGYPT ------------------
# וַיַּרְא יוֹשֵׁב הָאָרֶץ הַכְּנַעֲנִי אֶת־הָאֵבֶל בְּגֹרֶן הָאָטָד
# וַיֹּאמְרוּ אֵבֶל־כָּבֵד זֶה לְמִצְרָיִם עַל־כֵּן קָרָא שְׁמָהּ אָבֵל
# מִצְרַיִם אֲשֶׁר בְּעֵבֶר הַיַּרְדֵּן
# "[EN-AID] And the Canaanite inhabitant of the land saw the mourning at the
# threshing floor of Atad, and they said: This is a heavy mourning for
# Egypt. Therefore its name was called Avel Mitzrayim, which is across the
# Jordan."
m.step("Gen.50.11")
# ‹כֵּן קָרָא שְׁמָהּ אָבֵל מִצְרַיִם› (“so call name-her/its Abel-mizraim”)
# — named: threshing-floor-the-atad := avel-Egyptian
m.name("goren_ha_atad", "avel_mitzrayim")

# -------------------------- Gen.50.12 · AS_HE_CHARGED_THEM -----------------
# וַיַּעֲשׂוּ בָנָיו לוֹ כֵּן כַּאֲשֶׁר צִוָּם
# "[EN-AID] And his sons did for him so, exactly as he charged them."
m.step("Gen.50.12")
# ‹וַיַּעֲשׂוּ בָנָיו לוֹ כֵּן כַּאֲשֶׁר צִוָּם› (“and-make son-him/its to-
# him/its so like-as/which command-them/their”) — fact holds: and-make-
# vanav-not-so-kaasher-tzivam
m.fact("va_yaasu_vanav_lo_ken_kaasher_tzivam")

# -------------------------- Gen.50.13 · BURIED_IN_MACHPELAH ----------------
# וַיִּשְׂאוּ אֹתוֹ בָנָיו אַרְצָה כְּנַעַן וַיִּקְבְּרוּ אֹתוֹ בִּמְעָרַת
# שְׂדֵה הַמַּכְפֵּלָה אֲשֶׁר קָנָה אַבְרָהָם אֶת־הַשָּׂדֶה לַאֲחֻזַּת־קֶבֶר
# מֵאֵת עֶפְרֹן הַחִתִּי עַל־פְּנֵי מַמְרֵא
# "[EN-AID] And his sons carried him to the land of Canaan, and buried him
# in the cave of the field of Machpelah — which field Abraham had bought for
# a burial holding from Ephron the Hittite, before Mamre."
m.step("Gen.50.13")
# ‹וַיִּקְבְּרוּ אֹתוֹ בִּמְעָרַת שְׂדֵה הַמַּכְפֵּלָה› (“and-bury obj-
# marker-him/its in-cavern field the-Machpelah”) — fact holds: and-yiqberu-
# it-bi-mearat-field-the-Machpelah
m.fact("va_yiqberu_oto_bi_mearat_sede_ha_makhpela")

# -------------------------- Gen.50.14 · THE_RETURN_KEPT --------------------
# וַיָּשָׁב יוֹסֵף מִצְרַיְמָה הוּא וְאֶחָיו וְכָל־הָעֹלִים אִתּוֹ לִקְבֹּר
# אֶת־אָבִיו אַחֲרֵי קָבְרוֹ אֶת־אָבִיו
# "[EN-AID] And Joseph returned to Egypt, he and his brothers, and all who
# went up with him to bury his father, after he had buried his father."
m.step("Gen.50.14")
# ‹וַיָּשָׁב יוֹסֵף מִצְרַיְמָה› (“and-return Joseph Egypt-ward”) — fact
# holds: and-return-Joseph-mitzrayma
m.fact("va_yashav_yosef_mitzrayma")

# -------------------------- Gen.50.15 · WHAT_IF_JOSEPH_HATES_US ------------
# וַיִּרְאוּ אֲחֵי־יוֹסֵף כִּי־מֵת אֲבִיהֶם וַיֹּאמְרוּ לוּ יִשְׂטְמֵנוּ
# יוֹסֵף וְהָשֵׁב יָשִׁיב לָנוּ אֵת כָּל־הָרָעָה אֲשֶׁר גָּמַלְנוּ אֹתוֹ
# "[EN-AID] And Joseph's brothers saw that their father was dead, and they
# said: What if Joseph hates us, and surely returns to us all the evil which
# we dealt him."
m.step("Gen.50.15")
# ‹וַיֹּאמְרוּ לוּ יִשְׂטְמֵנוּ יוֹסֵף› (“and-say conditional-particle lurk-
# for-us/our Joseph”) — fact holds: conditional-particle-yistemenu-Joseph
m.fact("lu_yistemenu_yosef")

# -------------------------- Gen.50.16 · THE_FABRICATED_CHARGE --------------
# וַיְצַוּוּ אֶל־יוֹסֵף לֵאמֹר אָבִיךָ צִוָּה לִפְנֵי מוֹתוֹ לֵאמֹר
# "[EN-AID] And they commanded to Joseph, saying: Your father charged before
# his death, saying:"
m.step("Gen.50.16")
# ‹אָבִיךָ צִוָּה לִפְנֵי מוֹתוֹ› (“father-you/your command to-face death-
# him/its”) — fact holds: avikha-command-lifne-moto
m.fact("avikha_tziva_lifne_moto")

# -------------------------- Gen.50.17 · FORGIVE_THE_CRIME ------------------
# כֹּה־תֹאמְרוּ לְיוֹסֵף אָנָּא שָׂא נָא פֶּשַׁע אַחֶיךָ וְחַטָּאתָם
# כִּי־רָעָה גְמָלוּךָ וְעַתָּה שָׂא נָא לְפֶשַׁע עַבְדֵי אֱלֹהֵי אָבִיךָ
# וַיֵּבְךְּ יוֹסֵף בְּדַבְּרָם אֵלָיו
# "[EN-AID] So shall you say to Joseph: Please, forgive, pray, the crime of
# your brothers and their sin, for evil they dealt you; and now, forgive,
# pray, the crime of the servants of the God of your father. And Joseph wept
# at their speaking to him."
m.step("Gen.50.17")
# ‹וְעַתָּה שָׂא נָא לְפֶשַׁע עַבְדֵי אֱלֹהֵי אָבִיךָ› (“and-now lift/carry
# please to-revolt servant God father-you/your”) — brother-Joseph speaks a
# demand — LET: lift/carry-please-to-revolt-servant-God-avikha
m.declare("ache_yosef", "LET",
          "sa_na_le_fesha_avde_elohe_avikha")

# -------------------------- Gen.50.18 · BEHOLD_US_AS_SERVANTS --------------
# וַיֵּלְכוּ גַּם־אֶחָיו וַיִּפְּלוּ לְפָנָיו וַיֹּאמְרוּ הִנֶּנּוּ לְךָ
# לַעֲבָדִים
# "[EN-AID] And his brothers went also and fell before him; and they said:
# Behold us — yours, as servants."
m.step("Gen.50.18")
# ‹וַיֹּאמְרוּ הִנֶּנּוּ לְךָ לַעֲבָדִים› (“and-say behold-us/our to-
# you/your to-servant”) — fact holds: hinenu-to-you-to-servant
m.fact("hinenu_lekha_la_avadim")

# -------------------------- Gen.50.19 · AM_I_IN_PLACE_OF_GOD ---------------
# וַיֹּאמֶר אֲלֵהֶם יוֹסֵף אַל־תִּירָאוּ כִּי הֲתַחַת אֱלֹהִים אָנִי
# "[EN-AID] And Joseph said to them: Fear not — for am I in place of God?"
m.step("Gen.50.19")
# ‹כִּי הֲתַחַת אֱלֹהִים אָנִי› (“that the-under God”) — fact holds: the-
# under-God-ani
m.fact("ha_tachat_elohim_ani")

# -------------------------- Gen.50.20 · YOU_DEVISED_GOD_DEVISED ------------
# וְאַתֶּם חֲשַׁבְתֶּם עָלַי רָעָה אֱלֹהִים חֲשָׁבָהּ לְטֹבָה לְמַעַן עֲשֹׂה
# כַּיּוֹם הַזֶּה לְהַחֲיֹת עַם־רָב
# "[EN-AID] And you — you devised evil against me; God devised it for good,
# in order to do as this day — to keep alive a great people."
m.step("Gen.50.20")
# ‹אֱלֹהִים חֲשָׁבָהּ לְטֹבָה› (“God plait-her/its to-good-in-the-widest-
# sense”) — fact holds: God-chashavah-to-tovah
m.fact("elohim_chashavah_le_tovah")

# -------------------------- Gen.50.21 · I_WILL_SUSTAIN_YOU -----------------
# וְעַתָּה אַל־תִּירָאוּ אָנֹכִי אֲכַלְכֵּל אֶתְכֶם וְאֶת־טַפְּכֶם וַיְנַחֵם
# אוֹתָם וַיְדַבֵּר עַל־לִבָּם
# "[EN-AID] And now, fear not — I will sustain you, and your little ones.
# And he comforted them, and spoke to their heart."
m.step("Gen.50.21")
# ‹וַיְנַחֵם אוֹתָם וַיְדַבֵּר עַל־לִבָּם› (“and-sigh obj-marker-them/their
# and-speak over heart-them/their”) — demand settled (popped from the
# queue): lift/carry-please-to-revolt-servant-God-avikha
m.result("sa_na_le_fesha_avde_elohe_avikha", tmark="t2")

# -------------------------- Gen.50.22 · A_HUNDRED_AND_TEN ------------------
# וַיֵּשֶׁב יוֹסֵף בְּמִצְרַיִם הוּא וּבֵית אָבִיו וַיְחִי יוֹסֵף מֵאָה
# וָעֶשֶׂר שָׁנִים
# "[EN-AID] And Joseph dwelt in Egypt, he and his father's house; and Joseph
# lived a hundred and ten years."
m.step("Gen.50.22")
# ‹וַיְחִי יוֹסֵף מֵאָה וָעֶשֶׂר שָׁנִים› (“and-live Joseph hundred and-ten
# years”) — fact holds: and-live-Joseph-hundred-and-ten-years
m.fact("va_yechi_yosef_mea_va_eser_shanim")

# -------------------------- Gen.50.23 · ON_JOSEPHS_KNEES -------------------
# וַיַּרְא יוֹסֵף לְאֶפְרַיִם בְּנֵי שִׁלֵּשִׁים גַּם בְּנֵי מָכִיר
# בֶּן־מְנַשֶּׁה יֻלְּדוּ עַל־בִּרְכֵּי יוֹסֵף
# "[EN-AID] And Joseph saw, of Ephraim, children of the third generation;
# also the sons of Machir, son of Manasseh, were born on Joseph's knees."
m.step("Gen.50.23")
# ‹יֻלְּדוּ עַל־בִּרְכֵּי יוֹסֵף› (“bear-young over knee Joseph”) — fact
# holds: bear-young-over-knee-Joseph
m.fact("yuldu_al_birke_yosef")

# -------------------------- Gen.50.24 · GOD_WILL_SURELY_VISIT --------------
# וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו אָנֹכִי מֵת וֵאלֹהִים פָּקֹד יִפְקֹד אֶתְכֶם
# וְהֶעֱלָה אֶתְכֶם מִן־הָאָרֶץ הַזֹּאת אֶל־הָאָרֶץ אֲשֶׁר נִשְׁבַּע
# לְאַבְרָהָם לְיִצְחָק וּלְיַעֲקֹב
# "[EN-AID] And Joseph said to his brothers: I die; and God will surely
# visit you, and bring you up from this land to the land which He swore to
# Abraham, to Isaac, and to Jacob."
m.step("Gen.50.24")
# ‹וֵאלֹהִים פָּקֹד יִפְקֹד אֶתְכֶם› (“and-God count/visit count/visit obj-
# marker-you/your(pl)”) — fact holds: God-count/visit-count/visit-etkhem
m.fact("elohim_paqod_yifqod_etkhem")

# -------------------------- Gen.50.25 · THE_BONES_OATH ---------------------
# וַיַּשְׁבַּע יוֹסֵף אֶת־בְּנֵי יִשְׂרָאֵל לֵאמֹר פָּקֹד יִפְקֹד אֱלֹהִים
# אֶתְכֶם וְהַעֲלִתֶם אֶת־עַצְמֹתַי מִזֶּה
# "[EN-AID] And Joseph made the sons of Israel swear, saying: God will
# surely visit you — and you shall bring up my bones from here."
m.step("Gen.50.25")
# ‹וְהַעֲלִתֶם אֶת־עַצְמֹתַי מִזֶּה› (“and-go-up obj-marker bone-me/my from-
# this”) — Joseph speaks a demand — LET: and-go-up-obj-marker-atzmotai-from-
# this
m.declare("yosef", "LET",
          "ve_haalitem_et_atzmotai_mi_ze")

# -------------------------- Gen.50.26 · A_COFFIN_IN_EGYPT ------------------
# וַיָּמָת יוֹסֵף בֶּן־מֵאָה וָעֶשֶׂר שָׁנִים וַיַּחַנְטוּ אֹתוֹ וַיִּישֶׂם
# בָּאָרוֹן בְּמִצְרָיִם
# "[EN-AID] And Joseph died, a hundred and ten years old; and they embalmed
# him, and he was placed in a coffin in Egypt."
m.step("Gen.50.26")
# ‹וַיַּחַנְטוּ אֹתוֹ וַיִּישֶׂם בָּאָרוֹן בְּמִצְרָיִם› (“and-spice obj-
# marker-him/its and-place in-ark in-Egypt”) — event: die — agent Joseph
m.event("met", agent="yosef")

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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
