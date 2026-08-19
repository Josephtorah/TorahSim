#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_66_second_descent — 43:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_66_second_descent.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The second descent: Benjamin before Joseph (43:1-34)"""
from machine import Machine

m = Machine("gen_66_second_descent")

# -------------------------- Gen.43.1 · THE_FAMINE_HEAVY --------------------
# וְהָרָעָב כָּבֵד בָּאָרֶץ
# "[EN-AID] And the famine was heavy in the land."
m.step("Gen.43.1")
# ‹וְהָרָעָב כָּבֵד בָּאָרֶץ› (“and-the-hunger heavy in-earth”) — fact
# holds: and-the-hunger-heavy-come/bring-earth
m.fact("ve_ha_raav_kaved_ba_aretz")

# -------------------------- Gen.43.2 · RETURN_AND_BUY_A_LITTLE -------------
# וַיְהִי כַּאֲשֶׁר כִּלּוּ לֶאֱכֹל אֶת־הַשֶּׁבֶר אֲשֶׁר הֵבִיאוּ
# מִמִּצְרָיִם וַיֹּאמֶר אֲלֵיהֶם אֲבִיהֶם שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל
# "[EN-AID] And it was, when they had finished eating the grain which they
# brought from Egypt, that their father said to them: Return, buy us a
# little food."
m.step("Gen.43.2")
# ‹שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“return deal-in-grain to-us/our
# little food”) — yaaqov speaks a demand — LET: return-deal-in-grain-lanu-
# little-food
m.declare("yaaqov", "LET",
          "shuvu_shivru_lanu_meat_okhel")

# -------------------------- Gen.43.3 · THE_WITNESS_WARNING -----------------
# וַיֹּאמֶר אֵלָיו יְהוּדָה לֵאמֹר הָעֵד הֵעִד בָּנוּ הָאִישׁ לֵאמֹר
# לֹא־תִרְאוּ פָנַי בִּלְתִּי אֲחִיכֶם אִתְּכֶם
# "[EN-AID] And Judah said to him, saying: The man solemnly warned us,
# saying: You shall not see my face without your brother with you."
m.step("Gen.43.3")
# ‹הָעֵד הֵעִד בָּנוּ הָאִישׁ› (“duplicate duplicate in-us/our the-man”) —
# fact holds: duplicate-duplicate-banu-the-man
m.fact("haed_heid_banu_ha_ish")

# -------------------------- Gen.43.4 · IF_YOU_SEND -------------------------
# אִם־יֶשְׁךָ מְשַׁלֵּחַ אֶת־אָחִינוּ אִתָּנוּ נֵרְדָה וְנִשְׁבְּרָה לְךָ
# אֹכֶל
# "[EN-AID] If you are sending our brother with us, we will go down and buy
# you food."
m.step("Gen.43.4")
# ‹אִם־יֶשְׁךָ מְשַׁלֵּחַ אֶת־אָחִינוּ אִתָּנוּ נֵרְדָה› (“if there-is-
# you/your send obj-marker brother-us/our with-us/our go-down”) — fact
# holds: if-yeshkha-meshaleach-go-down
m.fact("im_yeshkha_meshaleach_nerda")

# -------------------------- Gen.43.5 · IF_YOU_SEND_NOT ---------------------
# וְאִם־אֵינְךָ מְשַׁלֵּחַ לֹא נֵרֵד כִּי־הָאִישׁ אָמַר אֵלֵינוּ לֹא־תִרְאוּ
# פָנַי בִּלְתִּי אֲחִיכֶם אִתְּכֶם
# "[EN-AID] And if you are not sending — we will not go down; for the man
# said to us: You shall not see my face without your brother with you."
m.step("Gen.43.5")
# ‹וְאִם־אֵינְךָ מְשַׁלֵּחַ לֹא נֵרֵד› (“and-if there-is-not-you/your send
# not go-down”) — fact holds: and-if-enkha-meshaleach-not-go-down
m.fact("ve_im_enkha_meshaleach_lo_nered")

# -------------------------- Gen.43.6 · WHY_DID_YOU_TELL --------------------
# וַיֹּאמֶר יִשְׂרָאֵל לָמָה הֲרֵעֹתֶם לִי לְהַגִּיד לָאִישׁ הַעוֹד לָכֶם
# אָח
# "[EN-AID] And Israel said: Why did you deal ill with me, to tell the man
# you had yet a brother?"
m.step("Gen.43.6")
# ‹וַיֹּאמֶר יִשְׂרָאֵל לָמָה הֲרֵעֹתֶם לִי› (“and-say Israel to-what spoil
# to-me/my”) — fact holds: lama-spoil-to-me-lehagid
m.fact("lama_hareotem_li_lehagid")

# -------------------------- Gen.43.7 · THE_MAN_ASKED_AND_ASKED -------------
# וַיֹּאמְרוּ שָׁאוֹל שָׁאַל־הָאִישׁ לָנוּ וּלְמוֹלַדְתֵּנוּ לֵאמֹר הַעוֹד
# אֲבִיכֶם חַי הֲיֵשׁ לָכֶם אָח וַנַגֶּד־לוֹ עַל־פִּי הַדְּבָרִים הָאֵלֶּה
# הֲיָדוֹעַ נֵדַע כִּי יֹאמַר הוֹרִידוּ אֶת־אֲחִיכֶם
# "[EN-AID] And they said: The man asked and asked about us and about our
# kindred, saying: Is your father yet alive? Have you a brother? And we told
# him according to these words. Could we know, knowing that he would say:
# Bring your brother down?"
m.step("Gen.43.7")
# ‹שָׁאוֹל שָׁאַל־הָאִישׁ› (“inquire inquire the-man”) — fact holds:
# inquire-inquire-the-man-lanu
m.fact("shaol_shaal_ha_ish_lanu")

# -------------------------- Gen.43.8 · SEND_THE_LAD_WITH_ME ----------------
# וַיֹּאמֶר יְהוּדָה אֶל־יִשְׂרָאֵל אָבִיו שִׁלְחָה הַנַּעַר אִתִּי
# וְנָקוּמָה וְנֵלֵכָה וְנִחְיֶה וְלֹא נָמוּת גַּם־אֲנַחְנוּ גַם־אַתָּה
# גַּם־טַפֵּנוּ
# "[EN-AID] And Judah said to Israel his father: Send the lad with me, and
# we will arise and go, and we will live and not die — we, and you, and our
# little ones."
m.step("Gen.43.8")
# ‹שִׁלְחָה הַנַּעַר אִתִּי› (“send-ward the-boy with-me/my”) — Judah speaks
# a demand — LET: shilcha-the-boy-iti
m.declare("yehuda", "LET",
          "shilcha_ha_naar_iti")

# -------------------------- Gen.43.9 · I_AM_THE_SURETY ---------------------
# אָנֹכִי אֶעֶרְבֶנּוּ מִיָּדִי תְּבַקְשֶׁנּוּ אִם־לֹא הֲבִיאֹתִיו אֵלֶיךָ
# וְהִצַּגְתִּיו לְפָנֶיךָ וְחָטָאתִי לְךָ כָּל־הַיָּמִים
# "[EN-AID] I will be surety for him; from my hand you shall require him: if
# I do not bring him to you and set him before you, I shall have sinned
# against you all the days."
m.step("Gen.43.9")
# ‹אָנֹכִי אֶעֶרְבֶנּוּ מִיָּדִי תְּבַקְשֶׁנּוּ› (“braid-him/its from-hand-
# me/my search-out-him/its”) — fact holds: anokhi-eervenu-who?-yadi-
# tevaqshenu
m.fact("anokhi_eervenu_mi_yadi_tevaqshenu")

# -------------------------- Gen.43.10 · WE_COULD_HAVE_RETURNED_TWICE -------
# כִּי לוּלֵא הִתְמַהְמָהְנוּ כִּי־עַתָּה שַׁבְנוּ זֶה פַעֲמָיִם
# "[EN-AID] For had we not lingered, surely by now we could have returned
# these two times."
m.step("Gen.43.10")
# ‹כִּי לוּלֵא הִתְמַהְמָהְנוּ› (“that if-not question”) — fact holds: that-
# if-not-question
m.fact("ki_lule_hitmahmahnu")

# -------------------------- Gen.43.11 · THE_FATHERS_CARAVAN_PLAN -----------
# וַיֹּאמֶר אֲלֵהֶם יִשְׂרָאֵל אֲבִיהֶם אִם־כֵּן אֵפוֹא זֹאת עֲשׂוּ קְחוּ
# מִזִּמְרַת הָאָרֶץ בִּכְלֵיכֶם וְהוֹרִידוּ לָאִישׁ מִנְחָה מְעַט צֳרִי
# וּמְעַט דְּבַשׁ נְכֹאת וָלֹט בָּטְנִים וּשְׁקֵדִים
# "[EN-AID] And Israel their father said to them: If so, then, this do: take
# of the land's best fruits in your vessels, and carry down to the man a
# gift — a little balm and a little honey, gum and ladanum, pistachios and
# almonds."
m.step("Gen.43.11")
# ‹זֹאת עֲשׂוּ קְחוּ מִזִּמְרַת הָאָרֶץ בִּכְלֵיכֶם וְהוֹרִידוּ› (“this make
# take from-pruned-fruit the-earth in-vessel-you/your(pl) and-go-down”) —
# Israel speaks a demand — LET: this-make-take-and-go-down
m.declare("yisrael", "LET",
          "zot_asu_qechu_ve_horidu")

# -------------------------- Gen.43.12 · DOUBLE_SILVER_AND_THE_RETURNED -----
# וְכֶסֶף מִשְׁנֶה קְחוּ בְיֶדְכֶם וְאֶת־הַכֶּסֶף הַמּוּשָׁב בְּפִי
# אַמְתְּחֹתֵיכֶם תָּשִׁיבוּ בְיֶדְכֶם אוּלַי מִשְׁגֶּה הוּא
# "[EN-AID] And double silver take in your hand; and the silver that was
# returned in the mouth of your bags return in your hand — perhaps it was an
# error."
m.step("Gen.43.12")
# ‹וְכֶסֶף מִשְׁנֶה קְחוּ בְיֶדְכֶם› (“and-silver repetition take in-hand-
# you/your(pl)”) — fact holds: silver-repetition-and-the-silver-the-return
m.fact("kesef_mishne_ve_ha_kesef_ha_mushav")

# -------------------------- Gen.43.13 · TAKE_YOUR_BROTHER_ARISE_RETURN -----
# וְאֶת־אֲחִיכֶם קָחוּ וְקוּמוּ שׁוּבוּ אֶל־הָאִישׁ
# "[EN-AID] And your brother take; and arise, return to the man."
m.step("Gen.43.13")
# ‹וְאֶת־אֲחִיכֶם קָחוּ וְקוּמוּ שׁוּבוּ› (“and-obj-marker brother-
# you/your(pl) take and-arise return”) — fact holds: and-obj-marker-
# achikhem-take-and-arise-return
m.fact("ve_et_achikhem_qachu_ve_qumu_shuvu")

# -------------------------- Gen.43.14 · EL_SHADDAI_GIVE_YOU_MERCY ----------
# וְאֵל שַׁדַּי יִתֵּן לָכֶם רַחֲמִים לִפְנֵי הָאִישׁ וְשִׁלַּח לָכֶם
# אֶת־אֲחִיכֶם אַחֵר וְאֶת־בִּנְיָמִין וַאֲנִי כַּאֲשֶׁר שָׁכֹלְתִּי
# שָׁכָלְתִּי
# "[EN-AID] And El Shaddai give you mercy before the man, that he may
# release to you your other brother, and Benjamin. And I — as I am bereaved,
# I am bereaved."
m.step("Gen.43.14")
# ‹וְאֵל שַׁדַּי יִתֵּן לָכֶם רַחֲמִים› (“and-strength Almighty set to-
# you/your(pl) compassion”) — Israel speaks a demand — LET: to-Almighty-set-
# lakhem-compassion
m.declare("yisrael", "LET",
          "el_shaday_yiten_lakhem_rachamim")

# -------------------------- Gen.43.15 · THE_CARAVAN_DESCENDS ---------------
# וַיִּקְחוּ הָאֲנָשִׁים אֶת־הַמִּנְחָה הַזֹּאת וּמִשְׁנֶה־כֶּסֶף לָקְחוּ
# בְיָדָם וְאֶת־בִּנְיָמִן וַיָּקֻמוּ וַיֵּרְדוּ מִצְרַיִם וַיַּעַמְדוּ
# לִפְנֵי יוֹסֵף
# "[EN-AID] And the men took this gift, and double silver they took in their
# hand, and Benjamin; and they arose and went down to Egypt, and stood
# before Joseph."
m.step("Gen.43.15")
# ‹וְאֶת־בִּנְיָמִן› (“and-obj-marker Benjamin”) — demand settled (popped
# from the queue): shilcha-the-boy-iti
m.result("shilcha_ha_naar_iti", tmark="t1")
# ‹וַיִּקְחוּ הָאֲנָשִׁים אֶת־הַמִּנְחָה הַזֹּאת וּמִשְׁנֶה־כֶּסֶף לָקְחוּ
# בְיָדָם› (“and-take the-man obj-marker the-grain-offering the-this and-
# repetition silver take in-hand-them/their”) — demand settled (popped from
# the queue): this-make-take-and-go-down
m.result("zot_asu_qechu_ve_horidu", tmark="t1")

# -------------------------- Gen.43.16 · SLAUGHTER_AND_PREPARE --------------
# וַיַּרְא יוֹסֵף אִתָּם אֶת־בִּנְיָמִין וַיֹּאמֶר לַאֲשֶׁר עַל־בֵּיתוֹ
# הָבֵא אֶת־הָאֲנָשִׁים הַבָּיְתָה וּטְבֹחַ טֶבַח וְהָכֵן כִּי אִתִּי
# יֹאכְלוּ הָאֲנָשִׁים בַּצָּהֳרָיִם
# "[EN-AID] And Joseph saw Benjamin with them, and said to the one over his
# house: Bring the men home, and slaughter a slaughtering and prepare — for
# with me the men shall eat at noon."
m.step("Gen.43.16")
# ‹הָבֵא אֶת־הָאֲנָשִׁים הַבָּיְתָה› (“come/bring obj-marker the-man the-
# house-ward”) — Joseph speaks a demand — LET: come/bring-obj-marker-the-
# man-the-baita
m.declare("yosef", "LET",
          "have_et_ha_anashim_ha_baita")

# -------------------------- Gen.43.17 · AS_JOSEPH_SAID ---------------------
# וַיַּעַשׂ הָאִישׁ כַּאֲשֶׁר אָמַר יוֹסֵף וַיָּבֵא הָאִישׁ אֶת־הָאֲנָשִׁים
# בֵּיתָה יוֹסֵף
# "[EN-AID] And the man did as Joseph said; and the man brought the men to
# Joseph's house."
m.step("Gen.43.17")
# ‹וַיַּעַשׂ הָאִישׁ כַּאֲשֶׁר אָמַר יוֹסֵף› (“and-make the-man like-
# as/which say Joseph”) — demand settled (popped from the queue):
# come/bring-obj-marker-the-man-the-baita
m.result("have_et_ha_anashim_ha_baita", tmark="t2")

# -------------------------- Gen.43.18 · THE_FEAR_AT_THE_DOOR ---------------
# וַיִּירְאוּ הָאֲנָשִׁים כִּי הוּבְאוּ בֵּית יוֹסֵף וַיֹּאמְרוּ עַל־דְּבַר
# הַכֶּסֶף הַשָּׁב בְּאַמְתְּחֹתֵינוּ בַּתְּחִלָּה אֲנַחְנוּ מוּבָאִים
# לְהִתְגֹּלֵל עָלֵינוּ וּלְהִתְנַפֵּל עָלֵינוּ וְלָקַחַת אֹתָנוּ לַעֲבָדִים
# וְאֶת־חֲמֹרֵינוּ
# "[EN-AID] And the men feared, for they were brought to Joseph's house; and
# they said: On the matter of the silver returned in our bags at the first
# are we brought — to roll upon us, and to fall upon us, and to take us for
# slaves, and our donkeys."
m.step("Gen.43.18")
# ‹וַיִּירְאוּ הָאֲנָשִׁים כִּי הוּבְאוּ› (“and-fear the-man that
# come/bring”) — fact holds: and-fear-the-man-that-come/bring
m.fact("va_yiru_ha_anashim_ki_huvu")

# -------------------------- Gen.43.19 · AT_THE_DOOR_THEY_DRAW_NEAR ---------
# וַיִּגְּשׁוּ אֶל־הָאִישׁ אֲשֶׁר עַל־בֵּית יוֹסֵף וַיְדַבְּרוּ אֵלָיו
# פֶּתַח הַבָּיִת
# "[EN-AID] And they drew near to the man who was over Joseph's house, and
# spoke to him at the door of the house."
m.step("Gen.43.19")
# ‹וַיִּגְּשׁוּ אֶל־הָאִישׁ› (“and-be to the-man”) — fact holds: and-be-to-
# the-man-opening-the-house
m.fact("va_yigshu_el_ha_ish_petach_ha_bayit")

# -------------------------- Gen.43.20 · WE_SURELY_CAME_DOWN ----------------
# וַיֹּאמְרוּ בִּי אֲדֹנִי יָרֹד יָרַדְנוּ בַּתְּחִלָּה לִשְׁבָּר־אֹכֶל
# "[EN-AID] And they said: Please, my lord — we surely came down at the
# first to buy food."
m.step("Gen.43.20")
# ‹יָרֹד יָרַדְנוּ בַּתְּחִלָּה› (“go-down go-down in-commencement”) — fact
# holds: go-down-go-down-come/bring-techila
m.fact("yarod_yaradnu_ba_techila")

# -------------------------- Gen.43.21 · THE_SILVER_BY_ITS_WEIGHT -----------
# וַיְהִי כִּי־בָאנוּ אֶל־הַמָּלוֹן וַנִּפְתְּחָה אֶת־אַמְתְּחֹתֵינוּ
# וְהִנֵּה כֶסֶף־אִישׁ בְּפִי אַמְתַּחְתּוֹ כַּסְפֵּנוּ בְּמִשְׁקָלוֹ
# וַנָּשֶׁב אֹתוֹ בְּיָדֵנוּ
# "[EN-AID] And it was, when we came to the lodging place and opened our
# bags — behold, each man's silver in the mouth of his bag, our silver by
# its weight; and we have brought it back in our hand."
m.step("Gen.43.21")
# ‹כַּסְפֵּנוּ בְּמִשְׁקָלוֹ וַנָּשֶׁב אֹתוֹ בְּיָדֵנוּ› (“silver-us/our in-
# weight-him/its and-return obj-marker-him/its in-hand-us/our”) — fact
# holds: kaspenu-in-mishkalo-and-return-it
m.fact("kaspenu_be_mishkalo_va_nashev_oto")

# -------------------------- Gen.43.22 · OTHER_SILVER_IN_HAND ---------------
# וְכֶסֶף אַחֵר הוֹרַדְנוּ בְיָדֵנוּ לִשְׁבָּר־אֹכֶל לֹא יָדַעְנוּ מִי־שָׂם
# כַּסְפֵּנוּ בְּאַמְתְּחֹתֵינוּ
# "[EN-AID] And other silver we have brought down in our hand to buy food;
# we do not know who put our silver in our bags."
m.step("Gen.43.22")
# ‹לֹא יָדַעְנוּ מִי־שָׂם כַּסְפֵּנוּ בְּאַמְתְּחֹתֵינוּ› (“not know who?
# put/set silver-us/our in-something-expansive-us/our”) — fact holds: not-
# know-who?-put/set-kaspenu
m.fact("lo_yadanu_mi_sam_kaspenu")

# -------------------------- Gen.43.23 · YOUR_GOD_GAVE_YOU_TREASURE ---------
# וַיֹּאמֶר שָׁלוֹם לָכֶם אַל־תִּירָאוּ אֱלֹהֵיכֶם וֵאלֹהֵי אֲבִיכֶם נָתַן
# לָכֶם מַטְמוֹן בְּאַמְתְּחֹתֵיכֶם כַּסְפְּכֶם בָּא אֵלָי וַיּוֹצֵא אֲלֵהֶם
# אֶת־שִׁמְעוֹן
# "[EN-AID] And he said: Peace to you, fear not; your God and the God of
# your father gave you treasure in your bags — your silver came to me. And
# he brought Simeon out to them."
m.step("Gen.43.23")
# ‹אַל־תִּירָאוּ› (“do-not fear”) — man-over-beit-Joseph speaks a demand —
# LET-NOT: over-fear
m.declare("ish_al_beit_yosef", "LET-NOT",
          "al_tirau")

# -------------------------- Gen.43.24 · WATER_AND_FODDER -------------------
# וַיָּבֵא הָאִישׁ אֶת־הָאֲנָשִׁים בֵּיתָה יוֹסֵף וַיִּתֶּן־מַיִם
# וַיִּרְחֲצוּ רַגְלֵיהֶם וַיִּתֵּן מִסְפּוֹא לַחֲמֹרֵיהֶם
# "[EN-AID] And the man brought the men into Joseph's house; and he gave
# water, and they washed their feet; and he gave fodder to their donkeys."
m.step("Gen.43.24")
# ‹וַיִּתֶּן־מַיִם וַיִּרְחֲצוּ רַגְלֵיהֶם› (“and-set waters and-lave foot-
# them/their”) — fact holds: and-set-waters-and-lave-raglehem
m.fact("va_yiten_mayim_va_yirchatzu_raglehem")

# -------------------------- Gen.43.25 · THE_GIFT_MADE_READY ----------------
# וַיָּכִינוּ אֶת־הַמִּנְחָה עַד־בּוֹא יוֹסֵף בַּצָּהֳרָיִם כִּי שָׁמְעוּ
# כִּי־שָׁם יֹאכְלוּ לָחֶם
# "[EN-AID] And they made ready the gift against Joseph's coming at noon,
# for they heard that there they should eat bread."
m.step("Gen.43.25")
# ‹וַיָּכִינוּ אֶת־הַמִּנְחָה› (“and-be-erect obj-marker the-grain-
# offering”) — fact holds: and-be-erect-obj-marker-the-grain-offering
m.fact("va_yakhinu_et_ha_mincha")

# -------------------------- Gen.43.26 · THE_ELEVEN_BOW ---------------------
# וַיָּבֹא יוֹסֵף הַבַּיְתָה וַיָּבִיאּוּ לוֹ אֶת־הַמִּנְחָה אֲשֶׁר־בְּיָדָם
# הַבָּיְתָה וַיִּשְׁתַּחֲווּ־לוֹ אָרְצָה
# "[EN-AID] And Joseph came home, and they brought him the gift which was in
# their hand, into the house, and they bowed down to him to the earth."
m.step("Gen.43.26")
# ‹וַיִּשְׁתַּחֲווּ־לוֹ אָרְצָה› (“and-afflict to-him/its earth-ward”) —
# event: hishtachavu — agent the-achim
m.event("hishtachavu", agent="ha_achim")

# -------------------------- Gen.43.27 · IS_YOUR_FATHER_WELL ----------------
# וַיִּשְׁאַל לָהֶם לְשָׁלוֹם וַיֹּאמֶר הֲשָׁלוֹם אֲבִיכֶם הַזָּקֵן אֲשֶׁר
# אֲמַרְתֶּם הַעוֹדֶנּוּ חָי
# "[EN-AID] And he asked them of their welfare, and said: Is your father
# well — the old man of whom you spoke? Is he yet alive?"
m.step("Gen.43.27")
# ‹וַיֹּאמֶר הֲשָׁלוֹם אֲבִיכֶם הַזָּקֵן› (“and-say the-safe father-
# you/your(pl) the-old”) — fact holds: the-safe-avikhem-the-old
m.fact("ha_shalom_avikhem_ha_zaqen")

# -------------------------- Gen.43.28 · THE_CLIPPED_BOW --------------------
# וַיֹּאמְרוּ שָׁלוֹם לְעַבְדְּךָ לְאָבִינוּ עוֹדֶנּוּ חָי וַיִּקְּדוּ
# וישתחו וַיִּשְׁתַּחֲוּוּ
# "[EN-AID] And they said: Your servant our father is well; he is yet alive.
# And they bowed their heads, and prostrated themselves."
m.step("Gen.43.28")
# ‹וַיִּקְּדוּ וישתחו וַיִּשְׁתַּחֲוּוּ› (“and-shrivel-up and-afflict and-
# afflict”) — fact holds: and-shrivel-up-and-afflict
m.fact("va_yiqdu_va_yishtachavu")

# -------------------------- Gen.43.29 · GOD_BE_GRACIOUS_TO_YOU_MY_SON ------
# וַיִּשָּׂא עֵינָיו וַיַּרְא אֶת־בִּנְיָמִין אָחִיו בֶּן־אִמּוֹ וַיֹּאמֶר
# הֲזֶה אֲחִיכֶם הַקָּטֹן אֲשֶׁר אֲמַרְתֶּם אֵלָי וַיֹּאמַר אֱלֹהִים
# יָחְנְךָ בְּנִי
# "[EN-AID] And he lifted his eyes and saw Benjamin his brother, his
# mother's son, and said: Is this your youngest brother of whom you spoke to
# me? And he said: God be gracious to you, my son."
m.step("Gen.43.29")
# ‹וַיֹּאמַר אֱלֹהִים יָחְנְךָ בְּנִי› (“and-say God bend-you/your son-
# me/my”) — blessing: Joseph blesses Benjamin
m.bless("yosef", "binyamin")

# -------------------------- Gen.43.30 · THE_CHAMBER_WEEPING ----------------
# וַיְמַהֵר יוֹסֵף כִּי־נִכְמְרוּ רַחֲמָיו אֶל־אָחִיו וַיְבַקֵּשׁ לִבְכּוֹת
# וַיָּבֹא הַחַדְרָה וַיֵּבְךְּ שָׁמָּה
# "[EN-AID] And Joseph hurried — for his compassion grew hot toward his
# brother, and he sought to weep; and he came into the chamber and wept
# there."
m.step("Gen.43.30")
# ‹וַיָּבֹא הַחַדְרָה וַיֵּבְךְּ שָׁמָּה› (“and-come/bring the-apartment-
# ward and-weep there-ward”) — event: bakha — agent Joseph
m.event("bakha", agent="yosef")

# -------------------------- Gen.43.31 · SET_BREAD --------------------------
# וַיִּרְחַץ פָּנָיו וַיֵּצֵא וַיִּתְאַפַּק וַיֹּאמֶר שִׂימוּ לָחֶם
# "[EN-AID] And he washed his face and went out, and restrained himself, and
# said: Set bread."
m.step("Gen.43.31")
# ‹שִׂימוּ לָחֶם› (“put/set food”) — Joseph speaks a demand — LET: put/set-
# food
m.declare("yosef", "LET",
          "simu_lachem")

# -------------------------- Gen.43.32 · BREAD_SET_APART --------------------
# וַיָּשִׂימוּ לוֹ לְבַדּוֹ וְלָהֶם לְבַדָּם וְלַמִּצְרִים הָאֹכְלִים אִתּוֹ
# לְבַדָּם כִּי לֹא יוּכְלוּן הַמִּצְרִים לֶאֱכֹל אֶת־הָעִבְרִים לֶחֶם
# כִּי־תוֹעֵבָה הִוא לְמִצְרָיִם
# "[EN-AID] And they set for him alone, and for them alone, and for the
# Egyptians eating with him alone — for the Egyptians may not eat bread with
# the Hebrews, for it is an abomination to Egypt."
m.step("Gen.43.32")
# ‹וַיָּשִׂימוּ לוֹ לְבַדּוֹ› (“and-put/set to-him/its to-separation-
# him/its”) — demand settled (popped from the queue): put/set-food
m.result("simu_lachem", tmark="t3")

# -------------------------- Gen.43.33 · SEATED_BY_BIRTH_ORDER --------------
# וַיֵּשְׁבוּ לְפָנָיו הַבְּכֹר כִּבְכֹרָתוֹ וְהַצָּעִיר כִּצְעִרָתוֹ
# וַיִּתְמְהוּ הָאֲנָשִׁים אִישׁ אֶל־רֵעֵהוּ
# "[EN-AID] And they sat before him, the firstborn according to his
# birthright and the youngest according to his youth; and the men wondered,
# each to his fellow."
m.step("Gen.43.33")
# ‹הַבְּכֹר כִּבְכֹרָתוֹ וְהַצָּעִיר כִּצְעִרָתוֹ› (“the-firstborn like-
# firstling-of-man-him/its and-the-little like-smallness-him/its”) — fact
# holds: the-firstborn-that-vkhorato-and-the-little-that-tzeirato
m.fact("ha_bekhor_ki_vkhorato_ve_ha_tzair_ki_tzeirato")

# -------------------------- Gen.43.34 · FIVE_HANDS -------------------------
# וַיִּשָּׂא מַשְׂאֹת מֵאֵת פָּנָיו אֲלֵהֶם וַתֵּרֶב מַשְׂאַת בִּנְיָמִן
# מִמַּשְׂאֹת כֻּלָּם חָמֵשׁ יָדוֹת וַיִּשְׁתּוּ וַיִּשְׁכְּרוּ עִמּוֹ
# "[EN-AID] And he lifted portions from before his face to them; and
# Benjamin's portion was greater than the portions of them all — five hands.
# And they drank, and drank freely with him."
m.step("Gen.43.34")
# ‹וַתֵּרֶב מַשְׂאַת בִּנְיָמִן מִמַּשְׂאֹת כֻּלָּם› (“and-multiply raising
# Benjamin from-raising all-them/their”) — fact holds: and-multiply-raising-
# Benjamin-five-hand
m.fact("va_terev_masat_binyamin_chamesh_yadot")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shuvu_shivru_lanu_meat_okhel', 'el_shaday_yiten_lakhem_rachamim', 'al_tirau']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_ha_raav_kaved_ba_aretz', 'haed_heid_banu_ha_ish', 'im_yeshkha_meshaleach_nerda', 've_im_enkha_meshaleach_lo_nered', 'lama_hareotem_li_lehagid', 'shaol_shaal_ha_ish_lanu', 'anokhi_eervenu_mi_yadi_tevaqshenu', 'ki_lule_hitmahmahnu', 'kesef_mishne_ve_ha_kesef_ha_mushav', 've_et_achikhem_qachu_ve_qumu_shuvu', 'va_yiru_ha_anashim_ki_huvu', 'va_yigshu_el_ha_ish_petach_ha_bayit', 'yarod_yaradnu_ba_techila', 'kaspenu_be_mishkalo_va_nashev_oto', 'lo_yadanu_mi_sam_kaspenu', 'va_yiten_mayim_va_yirchatzu_raglehem', 'va_yakhinu_et_ha_mincha', 'ha_shalom_avikhem_ha_zaqen', 'va_yiqdu_va_yishtachavu', 'ha_bekhor_ki_vkhorato_ve_ha_tzair_ki_tzeirato', 'va_terev_masat_binyamin_chamesh_yadot'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
