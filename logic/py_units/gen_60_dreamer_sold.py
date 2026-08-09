#!/usr/bin/env python3
# =============================================================================
# gen_60_dreamer_sold — 37:1-36
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_60_dreamer_sold.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The dreamer sent, stripped, and sold (37:1-36)"""
from machine import Machine

m = Machine("gen_60_dreamer_sold")

# -------------------------- Gen.37.1 · THE_SOJOURN_LAND_SETTLED ------------
# וַיֵּשֶׁב יַעֲקֹב בְּאֶרֶץ מְגוּרֵי אָבִיו בְּאֶרֶץ כְּנָעַן
# "[EN-AID] And Jacob dwelt in the land of his father's sojournings, in the
# land of Canaan."
m.step("Gen.37.1")
# ‹וַיֵּשֶׁב יַעֲקֹב בְּאֶרֶץ מְגוּרֵי אָבִיו› fact holds: yashav-in-earth-
# megure-aviv(yaaqov)
m.fact("yashav_be_eretz_megure_aviv(yaaqov)")

# -------------------------- Gen.37.2 · THE_HEADER_AND_THE_REPORT -----------
# אֵלֶּה תֹּלְדוֹת יַעֲקֹב יוֹסֵף בֶּן־שְׁבַע־עֶשְׂרֵה שָׁנָה הָיָה רֹעֶה
# אֶת־אֶחָיו בַּצֹּאן וְהוּא נַעַר אֶת־בְּנֵי בִלְהָה וְאֶת־בְּנֵי זִלְפָּה
# נְשֵׁי אָבִיו וַיָּבֵא יוֹסֵף אֶת־דִּבָּתָם רָעָה אֶל־אֲבִיהֶם
# "[EN-AID] These are the generations of Jacob: Joseph, seventeen years old,
# was shepherding with his brothers among the flock — a lad with the sons of
# Bilhah and Zilpah, his father's wives — and Joseph brought their evil
# report to their father."
m.step("Gen.37.2")
# ‹אֵלֶּה תֹּלְדוֹת יַעֲקֹב יוֹסֵף› fact holds: toldot-yaaqov(yosef-ben-
# seven-esre)
m.fact("toldot_yaaqov(yosef_ben_sheva_esre)")
# ‹וַיָּבֵא יוֹסֵף אֶת־דִּבָּתָם רָעָה אֶל־אֲבִיהֶם› fact holds: hevi-
# dibata-m-raa-to-avi-hem(yosef)
m.fact("hevi_dibata_m_raa_el_avi_hem(yosef)")

# -------------------------- Gen.37.3 · THE_LOVE_AND_THE_COAT ---------------
# וְיִשְׂרָאֵל אָהַב אֶת־יוֹסֵף מִכָּל־בָּנָיו כִּי־בֶן־זְקֻנִים הוּא לוֹ
# וְעָשָׂה לוֹ כְּתֹנֶת פַּסִּים
# "[EN-AID] And Israel loved Joseph more than all his sons, for he was to
# him a son of old age; and he made him a coat of stripes."
m.step("Gen.37.3")
# ‹וְיִשְׂרָאֵל אָהַב אֶת־יוֹסֵף מִכָּל־בָּנָיו› fact holds: ahav-yosef-
# from-kal-banay-v(yisrael)
m.fact("ahav_et_yosef_mi_kal_banay_v(yisrael)")
# ‹וְעָשָׂה לוֹ כְּתֹנֶת פַּסִּים› event: asa — agent yisrael; theme
# ketonet-pasim
m.event("asa", agent="yisrael", themes=["ketonet_pasim"])

# -------------------------- Gen.37.4 · THE_LEAN_PEACE ----------------------
# וַיִּרְאוּ אֶחָיו כִּי־אֹתוֹ אָהַב אֲבִיהֶם מִכָּל־אֶחָיו וַיִּשְׂנְאוּ
# אֹתוֹ וְלֹא יָכְלוּ דַּבְּרוֹ לְשָׁלֹם
# "[EN-AID] And his brothers saw that their father loved him more than all
# his brothers, and they hated him, and could not speak to him toward
# peace."
m.step("Gen.37.4")
# ‹וַיִּשְׂנְאוּ אֹתוֹ וְלֹא יָכְלוּ דַּבְּרוֹ לְשָׁלֹם› fact holds: sanu-
# it-and-not-yakhlu-dabro-to-shalom(echay-v)
m.fact("sanu_oto_ve_lo_yakhlu_dabro_le_shalom(echay_v)")

# -------------------------- Gen.37.5 · THE_FIRST_DREAM_TOLD ----------------
# וַיַּחֲלֹם יוֹסֵף חֲלוֹם וַיַּגֵּד לְאֶחָיו וַיּוֹסִפוּ עוֹד שְׂנֹא אֹתוֹ
# "[EN-AID] And Joseph dreamed a dream and told it to his brothers, and they
# hated him yet more."
m.step("Gen.37.5")
# ‹וַיַּחֲלֹם יוֹסֵף חֲלוֹם וַיַּגֵּד› event: chalam — agent yosef; theme
# chalom-rishon
m.event("chalam", agent="yosef", themes=["chalom_rishon"])

# -------------------------- Gen.37.6 · THE_HEAR_DEMAND ---------------------
# וַיֹּאמֶר אֲלֵיהֶם שִׁמְעוּ־נָא הַחֲלוֹם הַזֶּה אֲשֶׁר חָלָמְתִּי
# "[EN-AID] And he said to them: Hear, please, this dream which I have
# dreamed."
m.step("Gen.37.6")
# ‹שִׁמְעוּ־נָא הַחֲלוֹם הַזֶּה› yosef speaks a demand — LET: shimu-na-the-
# chalom
m.declare("yosef", "LET",
          "shimu_na_ha_chalom")

# -------------------------- Gen.37.7 · THE_SHEAVES_BOW ---------------------
# וְהִנֵּה אֲנַחְנוּ מְאַלְּמִים אֲלֻמִּים בְּתוֹךְ הַשָּׂדֶה וְהִנֵּה קָמָה
# אֲלֻמָּתִי וְגַם־נִצָּבָה וְהִנֵּה תְסֻבֶּינָה אֲלֻמֹּתֵיכֶם
# וַתִּשְׁתַּחֲוֶיןָ לַאֲלֻמָּתִי
# "[EN-AID] Behold, we were binding sheaves in the field, and behold, my
# sheaf arose and stood upright; and behold, your sheaves gathered round and
# bowed to my sheaf."
m.step("Gen.37.7")
# ‹וְהִנֵּה קָמָה אֲלֻמָּתִי וְגַם־נִצָּבָה› fact holds: alumati-qama-
# nitzava-and-alumot-tishtachavena(chalom-rishon)
m.fact("alumati_qama_nitzava_ve_alumot_tishtachavena(chalom_rishon)")

# -------------------------- Gen.37.8 · THE_ANSWER_OF_KINGS -----------------
# וַיֹּאמְרוּ לוֹ אֶחָיו הֲמָלֹךְ תִּמְלֹךְ עָלֵינוּ אִם־מָשׁוֹל תִּמְשֹׁל
# בָּנוּ וַיּוֹסִפוּ עוֹד שְׂנֹא אֹתוֹ עַל־חֲלֹמֹתָיו וְעַל־דְּבָרָיו
# "[EN-AID] And his brothers said to him: Will you indeed reign over us, or
# indeed rule over us? And they hated him yet more for his dreams and for
# his words."
m.step("Gen.37.8")
# ‹וַיֹּאמְרוּ לוֹ אֶחָיו הֲמָלֹךְ תִּמְלֹךְ עָלֵינוּ אִם־מָשׁוֹל תִּמְשֹׁל
# בָּנוּ› demand settled (popped from the queue): shimu-na-the-chalom
m.result("shimu_na_ha_chalom", tmark="t1")

# -------------------------- Gen.37.9 · THE_SECOND_DREAM --------------------
# וַיַּחֲלֹם עוֹד חֲלוֹם אַחֵר וַיְסַפֵּר אֹתוֹ לְאֶחָיו וַיֹּאמֶר הִנֵּה
# חָלַמְתִּי חֲלוֹם עוֹד וְהִנֵּה הַשֶּׁמֶשׁ וְהַיָּרֵחַ וְאַחַד עָשָׂר
# כּוֹכָבִים מִשְׁתַּחֲוִים לִי
# "[EN-AID] And he dreamed yet another dream and told it to his brothers,
# and said: Behold, I have dreamed a dream again — and behold, the sun and
# the moon and eleven stars bowing to me."
m.step("Gen.37.9")
# ‹וְהִנֵּה הַשֶּׁמֶשׁ וְהַיָּרֵחַ וְאַחַד עָשָׂר כּוֹכָבִים מִשְׁתַּחֲוִים›
# event: chalam — agent yosef; theme chalom-sheni
m.event("chalam", agent="yosef", themes=["chalom_sheni"])

# -------------------------- Gen.37.10 · THE_REBUKE_THAT_KEEPS --------------
# וַיְסַפֵּר אֶל־אָבִיו וְאֶל־אֶחָיו וַיִּגְעַר־בּוֹ אָבִיו וַיֹּאמֶר לוֹ
# מָה הַחֲלוֹם הַזֶּה אֲשֶׁר חָלָמְתָּ הֲבוֹא נָבוֹא אֲנִי וְאִמְּךָ
# וְאַחֶיךָ לְהִשְׁתַּחֲוֺת לְךָ אָרְצָה
# "[EN-AID] And he told it to his father and to his brothers; and his father
# rebuked him and said to him: What is this dream that you have dreamed?
# Shall we indeed come, I and your mother and your brothers, to bow to you
# to the ground?"
m.step("Gen.37.10")
# ‹וַיִּגְעַר־בּוֹ אָבִיו וַיֹּאמֶר› fact holds: gaar-in-it-aviv-ma-the-
# chalom(yaaqov)
m.fact("gaar_bo_aviv_ma_ha_chalom(yaaqov)")

# -------------------------- Gen.37.11 · THE_KEPT_WORD ----------------------
# וַיְקַנְאוּ־בוֹ אֶחָיו וְאָבִיו שָׁמַר אֶת־הַדָּבָר
# "[EN-AID] And his brothers envied him; and his father kept the word."
m.step("Gen.37.11")
# ‹וַיְקַנְאוּ־בוֹ אֶחָיו וְאָבִיו שָׁמַר אֶת־הַדָּבָר› fact holds: qinu-in-
# it-echay-v-and-aviv-shamar-the-davar
m.fact("qinu_bo_echay_v_ve_aviv_shamar_et_ha_davar")

# -------------------------- Gen.37.12 · THE_DOTTED_ET ----------------------
# וַיֵּלְכוּ אֶחָיו לִרְעוֹת אֶׄתׄ־צֹאן אֲבִיהֶם בִּשְׁכֶם
# "[EN-AID] And his brothers went to pasture their father's flock in
# Shechem."
m.step("Gen.37.12")
# ‹וַיֵּלְכוּ אֶחָיו לִרְעוֹת אֶׄתׄ־צֹאן אֲבִיהֶם› fact holds: halkhu-
# lireot-tzon-avi-hem-bi-shekhem(echay-v)
m.fact("halkhu_lireot_et_tzon_avi_hem_bi_shekhem(echay_v)")

# -------------------------- Gen.37.13 · THE_SUMMONS_AND_HINENI -------------
# וַיֹּאמֶר יִשְׂרָאֵל אֶל־יוֹסֵף הֲלוֹא אַחֶיךָ רֹעִים בִּשְׁכֶם לְכָה
# וְאֶשְׁלָחֲךָ אֲלֵיהֶם וַיֹּאמֶר לוֹ הִנֵּנִי
# "[EN-AID] And Israel said to Joseph: Are not your brothers pasturing in
# Shechem? Come, and I will send you to them. And he said to him: Here I
# am."
m.step("Gen.37.13")
# ‹לְכָה וְאֶשְׁלָחֲךָ אֲלֵיהֶם› yisrael speaks a demand — LET: to-you-to-
# achekha
m.declare("yisrael", "LET",
          "lekha_el_achekha")

# -------------------------- Gen.37.14 · THE_ERRAND_AND_THE_OPEN_WORD -------
# וַיֹּאמֶר לוֹ לֶךְ־נָא רְאֵה אֶת־שְׁלוֹם אַחֶיךָ וְאֶת־שְׁלוֹם הַצֹּאן
# וַהֲשִׁבֵנִי דָּבָר וַיִּשְׁלָחֵהוּ מֵעֵמֶק חֶבְרוֹן וַיָּבֹא שְׁכֶמָה
# "[EN-AID] And he said to him: Go now, see the peace of your brothers and
# the peace of the flock, and bring me back word. And he sent him from the
# valley of Hebron, and he came to Shechem."
m.step("Gen.37.14")
# ‹לֶךְ־נָא רְאֵה אֶת־שְׁלוֹם אַחֶיךָ וְאֶת־שְׁלוֹם הַצֹּאן› yisrael speaks
# a demand — LET: ree-shelom-achekha
m.declare("yisrael", "LET",
          "ree_et_shelom_achekha")
# ‹וַהֲשִׁבֵנִי דָּבָר› yisrael speaks a demand — LET: hashiveni-davar
m.declare("yisrael", "LET",
          "hashiveni_davar")
# ‹וַיִּשְׁלָחֵהוּ מֵעֵמֶק חֶבְרוֹן וַיָּבֹא שְׁכֶמָה› demand settled
# (popped from the queue): to-you-to-achekha
m.result("lekha_el_achekha", tmark="t1")

# -------------------------- Gen.37.15 · THE_WANDERER_FOUND -----------------
# וַיִּמְצָאֵהוּ אִישׁ וְהִנֵּה תֹעֶה בַּשָּׂדֶה וַיִּשְׁאָלֵהוּ הָאִישׁ
# לֵאמֹר מַה־תְּבַקֵּשׁ
# "[EN-AID] And a man found him — and behold, wandering in the field; and
# the man asked him: What do you seek?"
m.step("Gen.37.15")
# ‹וַיִּמְצָאֵהוּ אִישׁ וְהִנֵּה תֹעֶה בַּשָּׂדֶה› fact holds: toe-in-the-
# sade-and-yishale-that-the-man(yosef)
m.fact("toe_ba_sade_va_yishale_hu_ha_ish(yosef)")

# -------------------------- Gen.37.16 · THE_WHERE_WORD ---------------------
# וַיֹּאמֶר אֶת־אַחַי אָנֹכִי מְבַקֵּשׁ הַגִּידָה־נָּא לִי אֵיפֹה הֵם רֹעִים
# "[EN-AID] And he said: My brothers I seek; tell me, please, where they are
# pasturing."
m.step("Gen.37.16")
# ‹הַגִּידָה־נָּא לִי אֵיפֹה הֵם רֹעִים› yosef speaks a demand — LET:
# hagida-na-efo-hem-roim
m.declare("yosef", "LET",
          "hagida_na_efo_hem_roim")

# -------------------------- Gen.37.17 · THE_ANSWER_DOTHAN ------------------
# וַיֹּאמֶר הָאִישׁ נָסְעוּ מִזֶּה כִּי שָׁמַעְתִּי אֹמְרִים נֵלְכָה
# דֹּתָיְנָה וַיֵּלֶךְ יוֹסֵף אַחַר אֶחָיו וַיִּמְצָאֵם בְּדֹתָן
# "[EN-AID] And the man said: They have journeyed from here, for I heard
# them saying, Let us go to Dothan. And Joseph went after his brothers and
# found them at Dothan."
m.step("Gen.37.17")
# ‹וַיֹּאמֶר הָאִישׁ נָסְעוּ מִזֶּה כִּי שָׁמַעְתִּי אֹמְרִים נֵלְכָה
# דֹּתָיְנָה› demand settled (popped from the queue): hagida-na-efo-hem-roim
m.result("hagida_na_efo_hem_roim", tmark="t1")
# ‹וַיֵּלֶךְ יוֹסֵף אַחַר אֶחָיו וַיִּמְצָאֵם› demand settled (popped from
# the queue): ree-shelom-achekha
m.result("ree_et_shelom_achekha", tmark="t1")

# -------------------------- Gen.37.18 · THE_CONSPIRACY ---------------------
# וַיִּרְאוּ אֹתוֹ מֵרָחֹק וּבְטֶרֶם יִקְרַב אֲלֵיהֶם וַיִּתְנַכְּלוּ אֹתוֹ
# לַהֲמִיתוֹ
# "[EN-AID] And they saw him from afar; and before he drew near to them,
# they conspired against him to put him to death."
m.step("Gen.37.18")
# ‹וַיִּתְנַכְּלוּ אֹתוֹ› fact holds: yitnaklu-it-to-hamito(echay-v)
m.fact("yitnaklu_oto_la_hamito(echay_v)")

# -------------------------- Gen.37.19 · THE_DREAMER_NAMED ------------------
# וַיֹּאמְרוּ אִישׁ אֶל־אָחִיו הִנֵּה בַּעַל הַחֲלֹמוֹת הַלָּזֶה בָּא
# "[EN-AID] And they said each to his brother: Behold, this master of dreams
# comes."
m.step("Gen.37.19")
# ‹הִנֵּה בַּעַל הַחֲלֹמוֹת הַלָּזֶה בָּא› fact holds: baal-the-chalomot-
# halaze-in-the(man-to-his-brother)
m.fact("baal_ha_chalomot_halaze_ba(ish_el_achiv)")

# -------------------------- Gen.37.20 · THE_PLOT_PUSHED --------------------
# וְעַתָּה לְכוּ וְנַהַרְגֵהוּ וְנַשְׁלִכֵהוּ בְּאַחַד הַבֹּרוֹת וְאָמַרְנוּ
# חַיָּה רָעָה אֲכָלָתְהוּ וְנִרְאֶה מַה־יִּהְיוּ חֲלֹמֹתָיו
# "[EN-AID] And now, come, let us kill him and throw him into one of the
# pits, and we will say: an evil beast devoured him — and we shall see what
# his dreams will be."
m.step("Gen.37.20")
# ‹לְכוּ וְנַהַרְגֵהוּ› achim speaks a demand — CMD-US: naharge-that
m.declare("achim", "CMD-US",
          "naharge_hu")
# ‹וְנַשְׁלִכֵהוּ בְּאַחַד הַבֹּרוֹת› achim speaks a demand — CMD-US:
# nashlikhe-that
m.declare("achim", "CMD-US",
          "nashlikhe_hu")
# ‹וְאָמַרְנוּ חַיָּה רָעָה אֲכָלָתְהוּ› achim speaks a demand — CMD-US:
# amarnu-living-raa-akhalat-that
m.declare("achim", "CMD-US",
          "amarnu_chaya_raa_akhalat_hu")

# -------------------------- Gen.37.21 · REUBEN_HEARS -----------------------
# וַיִּשְׁמַע רְאוּבֵן וַיַּצִּלֵהוּ מִיָּדָם וַיֹּאמֶר לֹא נַכֶּנּוּ נָפֶשׁ
# "[EN-AID] And Reuben heard, and rescued him from their hand, and said: Let
# us not strike a soul."
m.step("Gen.37.21")
# ‹וַיֹּאמֶר לֹא נַכֶּנּוּ נָפֶשׁ› reuven speaks a demand — LET-NOT: nake-
# nu-nafesh
m.declare("reuven", "LET-NOT",
          "nake_nu_nafesh")

# -------------------------- Gen.37.22 · REUBENS_REDIRECT -------------------
# וַיֹּאמֶר אֲלֵהֶם רְאוּבֵן אַל־תִּשְׁפְּכוּ־דָם הַשְׁלִיכוּ אֹתוֹ
# אֶל־הַבּוֹר הַזֶּה אֲשֶׁר בַּמִּדְבָּר וְיָד אַל־תִּשְׁלְחוּ־בוֹ לְמַעַן
# הַצִּיל אֹתוֹ מִיָּדָם לַהֲשִׁיבוֹ אֶל־אָבִיו
# "[EN-AID] And Reuben said to them: Shed no blood; throw him into this pit
# which is in the wilderness, and lay no hand on him — in order to rescue
# him from their hand, to return him to his father."
m.step("Gen.37.22")
# ‹אַל־תִּשְׁפְּכוּ־דָם› reuven speaks a demand — LET-NOT: tishpekhu-blood
m.declare("reuven", "LET-NOT",
          "tishpekhu_dam")
# ‹הַשְׁלִיכוּ אֹתוֹ אֶל־הַבּוֹר הַזֶּה› reuven speaks a demand — LET:
# hashlikhu-it-to-the-bor
m.declare("reuven", "LET",
          "hashlikhu_oto_el_ha_bor")
# ‹וְיָד אַל־תִּשְׁלְחוּ־בוֹ› reuven speaks a demand — LET-NOT: yad-upon-
# tishlechu-vo
m.declare("reuven", "LET-NOT",
          "yad_al_tishlechu_vo")

# -------------------------- Gen.37.23 · THE_STRIPPING ----------------------
# וַיְהִי כַּאֲשֶׁר־בָּא יוֹסֵף אֶל־אֶחָיו וַיַּפְשִׁיטוּ אֶת־יוֹסֵף
# אֶת־כֻּתָּנְתּוֹ אֶת־כְּתֹנֶת הַפַּסִּים אֲשֶׁר עָלָיו
# "[EN-AID] And it came to pass, when Joseph came to his brothers, that they
# stripped Joseph of his coat, the coat of stripes that was on him."
m.step("Gen.37.23")
# ‹וַיַּפְשִׁיטוּ אֶת־יוֹסֵף אֶת־כֻּתָּנְתּוֹ אֶת־כְּתֹנֶת הַפַּסִּים›
# event: hifshitu — agent echay-v; theme ketonet-the-pasim
m.event("hifshitu", agent="echay_v", themes=["ketonet_ha_pasim"])

# -------------------------- Gen.37.24 · THE_PIT_TAKES_HIM ------------------
# וַיִּקָּחֻהוּ וַיַּשְׁלִכוּ אֹתוֹ הַבֹּרָה וְהַבּוֹר רֵק אֵין בּוֹ מָיִם
# "[EN-AID] And they took him and threw him into the pit; and the pit was
# empty — no water in it."
m.step("Gen.37.24")
# ‹וַיִּקָּחֻהוּ וַיַּשְׁלִכוּ אֹתוֹ הַבֹּרָה› demand settled (popped from
# the queue): hashlikhu-it-to-the-bor
m.result("hashlikhu_oto_el_ha_bor", tmark="t2")
# ‹וַיַּשְׁלִכוּ אֹתוֹ הַבֹּרָה› demand settled (popped from the queue):
# nashlikhe-that
m.result("nashlikhe_hu", tmark="t2")

# -------------------------- Gen.37.25 · BREAD_AND_THE_CARAVAN --------------
# וַיֵּשְׁבוּ לֶאֱכָל־לֶחֶם וַיִּשְׂאוּ עֵינֵיהֶם וַיִּרְאוּ וְהִנֵּה
# אֹרְחַת יִשְׁמְעֵאלִים בָּאָה מִגִּלְעָד וּגְמַלֵּיהֶם נֹשְׂאִים נְכֹאת
# וּצְרִי וָלֹט הוֹלְכִים לְהוֹרִיד מִצְרָיְמָה
# "[EN-AID] And they sat down to eat bread; and they lifted their eyes and
# saw — behold, a caravan of Ishmaelites coming from Gilead, their camels
# bearing gum, balm, and ladanum, going to carry it down to Egypt."
m.step("Gen.37.25")
# ‹וְהִנֵּה אֹרְחַת יִשְׁמְעֵאלִים בָּאָה מִגִּלְעָד› fact holds: orchat-
# yishmeelim-baa-holkhim-mitzrayma
m.fact("orchat_yishmeelim_baa_holkhim_mitzrayma")

# -------------------------- Gen.37.26 · JUDAHS_QUESTION --------------------
# וַיֹּאמֶר יְהוּדָה אֶל־אֶחָיו מַה־בֶּצַע כִּי נַהֲרֹג אֶת־אָחִינוּ
# וְכִסִּינוּ אֶת־דָּמוֹ
# "[EN-AID] And Judah said to his brothers: What profit if we kill our
# brother and cover his blood?"
m.step("Gen.37.26")
# ‹מַה־בֶּצַע כִּי נַהֲרֹג אֶת־אָחִינוּ וְכִסִּינוּ אֶת־דָּמוֹ› fact holds:
# ma-betza-when-naharog-my-brother-nu(yehuda)
m.fact("ma_betza_ki_naharog_et_achi_nu(yehuda)")

# -------------------------- Gen.37.27 · THE_SALE_PROPOSED ------------------
# לְכוּ וְנִמְכְּרֶנּוּ לַיִּשְׁמְעֵאלִים וְיָדֵנוּ אַל־תְּהִי־בוֹ
# כִּי־אָחִינוּ בְשָׂרֵנוּ הוּא וַיִּשְׁמְעוּ אֶחָיו
# "[EN-AID] Come, let us sell him to the Ishmaelites, and let our hand not
# be upon him, for he is our brother, our flesh. And his brothers heeded."
m.step("Gen.37.27")
# ‹לְכוּ וְנִמְכְּרֶנּוּ לַיִּשְׁמְעֵאלִים› yehuda speaks a demand — CMD-US:
# nimkere-nu-to-yishmeelim
m.declare("yehuda", "CMD-US",
          "nimkere_nu_la_yishmeelim")
# ‹וְיָדֵנוּ אַל־תְּהִי־בוֹ› yehuda speaks a demand — LET-NOT: yade-nu-upon-
# tehi-vo
m.declare("yehuda", "LET-NOT",
          "yade_nu_al_tehi_vo")

# -------------------------- Gen.37.28 · THE_SALE_WITH_NO_NAMED_SELLER ------
# וַיַּעַבְרוּ אֲנָשִׁים מִדְיָנִים סֹחֲרִים וַיִּמְשְׁכוּ וַיַּעֲלוּ
# אֶת־יוֹסֵף מִן־הַבּוֹר וַיִּמְכְּרוּ אֶת־יוֹסֵף לַיִּשְׁמְעֵאלִים
# בְּעֶשְׂרִים כָּסֶף וַיָּבִיאוּ אֶת־יוֹסֵף מִצְרָיְמָה
# "[EN-AID] And Midianite men, merchants, passed by; and they drew and
# lifted Joseph out of the pit, and sold Joseph to the Ishmaelites for
# twenty pieces of silver; and they brought Joseph to Egypt."
m.step("Gen.37.28")
# ‹וַיִּמְשְׁכוּ וַיַּעֲלוּ אֶת־יוֹסֵף מִן־הַבּוֹר וַיִּמְכְּרוּ אֶת־יוֹסֵף
# לַיִּשְׁמְעֵאלִים בְּעֶשְׂרִים כָּסֶף› demand settled (popped from the
# queue): nimkere-nu-to-yishmeelim
m.result("nimkere_nu_la_yishmeelim", tmark="t2")

# -------------------------- Gen.37.29 · REUBEN_AT_THE_EMPTY_PIT ------------
# וַיָּשָׁב רְאוּבֵן אֶל־הַבּוֹר וְהִנֵּה אֵין־יוֹסֵף בַּבּוֹר וַיִּקְרַע
# אֶת־בְּגָדָיו
# "[EN-AID] And Reuben returned to the pit — and behold, Joseph was not in
# the pit; and he tore his garments."
m.step("Gen.37.29")
# ‹וַיָּשָׁב רְאוּבֵן אֶל־הַבּוֹר וְהִנֵּה אֵין־יוֹסֵף בַּבּוֹר› fact holds:
# shav-to-the-bor-and-en-yosef(reuven)
m.fact("shav_el_ha_bor_ve_en_yosef(reuven)")

# -------------------------- Gen.37.30 · THE_CHILD_IS_NOT -------------------
# וַיָּשָׁב אֶל־אֶחָיו וַיֹּאמַר הַיֶּלֶד אֵינֶנּוּ וַאֲנִי אָנָה אֲנִי־בָא
# "[EN-AID] And he returned to his brothers and said: The child is not — and
# I, where shall I come?"
m.step("Gen.37.30")
# ‹הַיֶּלֶד אֵינֶנּוּ וַאֲנִי אָנָה אֲנִי־בָא› fact holds: the-yeled-ene-nu-
# and-ani-ana-ani-and(reuven)
m.fact("ha_yeled_ene_nu_va_ani_ana_ani_va(reuven)")

# -------------------------- Gen.37.31 · THE_COAT_DIPPED --------------------
# וַיִּקְחוּ אֶת־כְּתֹנֶת יוֹסֵף וַיִּשְׁחֲטוּ שְׂעִיר עִזִּים וַיִּטְבְּלוּ
# אֶת־הַכֻּתֹּנֶת בַּדָּם
# "[EN-AID] And they took Joseph's coat, and slaughtered a goat of the
# goats, and dipped the coat in the blood."
m.step("Gen.37.31")
# ‹וַיִּשְׁחֲטוּ שְׂעִיר עִזִּים וַיִּטְבְּלוּ אֶת־הַכֻּתֹּנֶת בַּדָּם›
# event: taval — agent achim; theme the-kutonet-in-the-blood
m.event("taval", agent="achim", themes=["ha_kutonet_ba_dam"])

# -------------------------- Gen.37.32 · THE_RECOGNIZE_DEMAND ---------------
# וַיְשַׁלְּחוּ אֶת־כְּתֹנֶת הַפַּסִּים וַיָּבִיאוּ אֶל־אֲבִיהֶם וַיֹּאמְרוּ
# זֹאת מָצָאנוּ הַכֶּר־נָא הַכְּתֹנֶת בִּנְךָ הִוא אִם־לֹא
# "[EN-AID] And they sent the coat of stripes and brought it to their
# father, and said: This we found; recognize, please — is it your son's coat
# or not?"
m.step("Gen.37.32")
# ‹הַכֶּר־נָא הַכְּתֹנֶת בִּנְךָ› achim speaks a demand — LET: haker-na-the-
# ketonet
m.declare("achim", "LET",
          "haker_na_ha_ketonet")

# -------------------------- Gen.37.33 · THE_FATHER_SPEAKS_THE_LIE ----------
# וַיַּכִּירָהּ וַיֹּאמֶר כְּתֹנֶת בְּנִי חַיָּה רָעָה אֲכָלָתְהוּ טָרֹף
# טֹרַף יוֹסֵף
# "[EN-AID] And he recognized it and said: My son's coat — an evil beast
# devoured him; torn, torn is Joseph."
m.step("Gen.37.33")
# ‹וַיַּכִּירָהּ וַיֹּאמֶר כְּתֹנֶת בְּנִי› demand settled (popped from the
# queue): haker-na-the-ketonet
m.result("haker_na_ha_ketonet", tmark="t3")
# ‹חַיָּה רָעָה אֲכָלָתְהוּ טָרֹף טֹרַף› fact holds: amar-living-raa-
# akhalat-that-tarof-toraf(yaaqov)
m.fact("amar_chaya_raa_akhalat_hu_tarof_toraf(yaaqov)")

# -------------------------- Gen.37.34 · THE_MOURNING -----------------------
# וַיִּקְרַע יַעֲקֹב שִׂמְלֹתָיו וַיָּשֶׂם שַׂק בְּמָתְנָיו וַיִּתְאַבֵּל
# עַל־בְּנוֹ יָמִים רַבִּים
# "[EN-AID] And Jacob tore his garments and put sackcloth on his loins, and
# mourned his son many days."
m.step("Gen.37.34")
# ‹וַיִּקְרַע יַעֲקֹב שִׂמְלֹתָיו וַיָּשֶׂם שַׂק בְּמָתְנָיו› fact holds:
# qara-simlotay-v-sam-saq-and-yitabel(yaaqov)
m.fact("qara_simlotay_v_sam_saq_va_yitabel(yaaqov)")

# -------------------------- Gen.37.35 · COMFORT_REFUSED --------------------
# וַיָּקֻמוּ כָל־בָּנָיו וְכָל־בְּנֹתָיו לְנַחֲמוֹ וַיְמָאֵן לְהִתְנַחֵם
# וַיֹּאמֶר כִּי־אֵרֵד אֶל־בְּנִי אָבֵל שְׁאֹלָה וַיֵּבְךְּ אֹתוֹ אָבִיו
# "[EN-AID] And all his sons and all his daughters rose to comfort him, and
# he refused to be comforted, and said: For I will go down to my son
# mourning, to Sheol. And his father wept for him."
m.step("Gen.37.35")
# ‹וַיְמָאֵן לְהִתְנַחֵם וַיֹּאמֶר כִּי־אֵרֵד אֶל־בְּנִי אָבֵל שְׁאֹלָה›
# fact holds: vayemaen-lehitnachem-ered-avel-sheola(yaaqov)
m.fact("vayemaen_lehitnachem_ered_avel_sheola(yaaqov)")

# -------------------------- Gen.37.36 · THE_SECOND_SALE --------------------
# וְהַמְּדָנִים מָכְרוּ אֹתוֹ אֶל־מִצְרָיִם לְפוֹטִיפַר סְרִיס פַּרְעֹה שַׂר
# הַטַּבָּחִים
# "[EN-AID] And the Medanites sold him to Egypt, to Potiphar, Pharaoh's
# officer, the chief of the slaughterers."
m.step("Gen.37.36")
# ‹וְהַמְּדָנִים מָכְרוּ אֹתוֹ אֶל־מִצְרָיִם› fact holds: makhru-it-to-
# mitzrayim-to-fotifar(medanim)
m.fact("makhru_oto_el_mitzrayim_le_fotifar(medanim)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hashiveni_davar', 'naharge_hu', 'amarnu_chaya_raa_akhalat_hu', 'nake_nu_nafesh', 'tishpekhu_dam', 'yad_al_tishlechu_vo', 'yade_nu_al_tehi_vo']
    assert len(m.SPECS["log"]) == 15
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['yashav_be_eretz_megure_aviv(yaaqov)', 'toldot_yaaqov(yosef_ben_sheva_esre)', 'hevi_dibata_m_raa_el_avi_hem(yosef)', 'ahav_et_yosef_mi_kal_banay_v(yisrael)', 'sanu_oto_ve_lo_yakhlu_dabro_le_shalom(echay_v)', 'alumati_qama_nitzava_ve_alumot_tishtachavena(chalom_rishon)', 'gaar_bo_aviv_ma_ha_chalom(yaaqov)', 'qinu_bo_echay_v_ve_aviv_shamar_et_ha_davar', 'halkhu_lireot_et_tzon_avi_hem_bi_shekhem(echay_v)', 'toe_ba_sade_va_yishale_hu_ha_ish(yosef)', 'yitnaklu_oto_la_hamito(echay_v)', 'baal_ha_chalomot_halaze_ba(ish_el_achiv)', 'orchat_yishmeelim_baa_holkhim_mitzrayma', 'ma_betza_ki_naharog_et_achi_nu(yehuda)', 'shav_el_ha_bor_ve_en_yosef(reuven)', 'ha_yeled_ene_nu_va_ani_ana_ani_va(reuven)', 'amar_chaya_raa_akhalat_hu_tarof_toraf(yaaqov)', 'qara_simlotay_v_sam_saq_va_yitabel(yaaqov)', 'vayemaen_lehitnachem_ered_avel_sheola(yaaqov)', 'makhru_oto_el_mitzrayim_le_fotifar(medanim)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 28
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
