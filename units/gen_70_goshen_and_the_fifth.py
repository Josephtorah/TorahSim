#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_70_goshen_and_the_fifth — 47:1-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_70_goshen_and_the_fifth.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Goshen and the fifth (47:1-31)"""
from machine import Machine

m = Machine("gen_70_goshen_and_the_fifth")

# -------------------------- Gen.47.1 · THE_BRIEFING_DELIVERED --------------
# וַיָּבֹא יוֹסֵף וַיַּגֵּד לְפַרְעֹה וַיֹּאמֶר אָבִי וְאַחַי וְצֹאנָם
# וּבְקָרָם וְכָל־אֲשֶׁר לָהֶם בָּאוּ מֵאֶרֶץ כְּנָעַן וְהִנָּם בְּאֶרֶץ
# גֹּשֶׁן
# "[EN-AID] And Joseph came and told Pharaoh, and said: My father and my
# brothers, with their flocks and their herds and all that is theirs, have
# come from the land of Canaan; and behold, they are in the land of Goshen."
m.step("Gen.47.1")
# ‹וַיָּבֹא יוֹסֵף וַיַּגֵּד לְפַרְעֹה› (“and-come/bring Joseph and-tell to-
# Pharaoh”) — fact holds: and-tell-to-Pharaoh-come/bring-from-earth-Canaan
m.fact("va_yaged_le_faro_bau_me_eretz_kenaan")

# -------------------------- Gen.47.2 · FIVE_FROM_THE_EDGE ------------------
# וּמִקְצֵה אֶחָיו לָקַח חֲמִשָּׁה אֲנָשִׁים וַיַּצִּגֵם לִפְנֵי פַרְעֹה
# "[EN-AID] And from the edge of his brothers he took five men, and
# presented them before Pharaoh."
m.step("Gen.47.2")
# ‹וּמִקְצֵה אֶחָיו לָקַח חֲמִשָּׁה אֲנָשִׁים› (“and-from-end brother-
# him/its take five man”) — fact holds: five-man-lifne-Pharaoh
m.fact("chamisha_anashim_lifne_faro")

# -------------------------- Gen.47.3 · THE_SCRIPT_PERFORMED ----------------
# וַיֹּאמֶר פַּרְעֹה אֶל־אֶחָיו מַה־מַּעֲשֵׂיכֶם וַיֹּאמְרוּ אֶל־פַּרְעֹה
# רֹעֵה צֹאן עֲבָדֶיךָ גַּם־אֲנַחְנוּ גַּם־אֲבוֹתֵינוּ
# "[EN-AID] And Pharaoh said to his brothers: What is your work? And they
# said to Pharaoh: Your servants are a shepherd of flocks, both we and our
# fathers."
m.step("Gen.47.3")
# ‹רֹעֵה צֹאן עֲבָדֶיךָ גַּם־אֲנַחְנוּ גַּם־אֲבוֹתֵינוּ› (“graze flock
# servant-you/your also we also father-us/our”) — fact holds: graze-flock-
# avadekha-also-we-also-avotenu
m.fact("roe_tzon_avadekha_gam_anachnu_gam_avotenu")

# -------------------------- Gen.47.4 · LET_US_DWELL_IN_GOSHEN --------------
# וַיֹּאמְרוּ אֶל־פַּרְעֹה לָגוּר בָּאָרֶץ בָּאנוּ כִּי־אֵין מִרְעֶה לַצֹּאן
# אֲשֶׁר לַעֲבָדֶיךָ כִּי־כָבֵד הָרָעָב בְּאֶרֶץ כְּנָעַן וְעַתָּה
# יֵשְׁבוּ־נָא עֲבָדֶיךָ בְּאֶרֶץ גֹּשֶׁן
# "[EN-AID] And they said to Pharaoh: To sojourn in the land we have come,
# for there is no pasture for the flock of your servants, for the famine is
# heavy in the land of Canaan; and now, let your servants dwell, pray, in
# the land of Goshen."
m.step("Gen.47.4")
# ‹וְעַתָּה יֵשְׁבוּ־נָא עֲבָדֶיךָ בְּאֶרֶץ גֹּשֶׁן› (“and-now dwell/sit
# please servant-you/your in-earth Goshen”) — bene-Jacob speaks a demand —
# LET: dwell/sit-please-avadekha-in-earth-Goshen
m.declare("bene_yaaqov", "LET",
          "yeshvu_na_avadekha_be_eretz_goshen")

# -------------------------- Gen.47.5 · THEY_HAVE_COME_TO_YOU ---------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף לֵאמֹר אָבִיךָ וְאַחֶיךָ בָּאוּ אֵלֶיךָ
# "[EN-AID] And Pharaoh said to Joseph, saying: Your father and your
# brothers have come to you."
m.step("Gen.47.5")
# ‹אָבִיךָ וְאַחֶיךָ בָּאוּ אֵלֶיךָ› (“father-you/your and-brother-you/your
# come/bring to-you/your”) — fact holds: avikha-and-achekha-come/bring-to-
# you
m.fact("avikha_ve_achekha_bau_elekha")

# -------------------------- Gen.47.6 · THE_LAND_BEFORE_YOU -----------------
# אֶרֶץ מִצְרַיִם לְפָנֶיךָ הִוא בְּמֵיטַב הָאָרֶץ הוֹשֵׁב אֶת־אָבִיךָ
# וְאֶת־אַחֶיךָ יֵשְׁבוּ בְּאֶרֶץ גֹּשֶׁן וְאִם־יָדַעְתָּ וְיֶשׁ־בָּם
# אַנְשֵׁי־חַיִל וְשַׂמְתָּם שָׂרֵי מִקְנֶה עַל־אֲשֶׁר־לִי
# "[EN-AID] The land of Egypt is before you: in the best of the land settle
# your father and your brothers; let them dwell in the land of Goshen. And
# if you know that there are able men among them, set them as chiefs of
# livestock over what is mine."
m.step("Gen.47.6")
# ‹יֵשְׁבוּ בְּאֶרֶץ גֹּשֶׁן› (“dwell/sit in-earth Goshen”) — demand settled
# (popped from the queue): dwell/sit-please-avadekha-in-earth-Goshen
m.result("yeshvu_na_avadekha_be_eretz_goshen", tmark="t1")

# -------------------------- Gen.47.7 · JACOB_BLESSES_PHARAOH ---------------
# וַיָּבֵא יוֹסֵף אֶת־יַעֲקֹב אָבִיו וַיַּעֲמִדֵהוּ לִפְנֵי פַרְעֹה
# וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה
# "[EN-AID] And Joseph brought Jacob his father, and stood him before
# Pharaoh; and Jacob blessed Pharaoh."
m.step("Gen.47.7")
# ‹וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה› (“and-bless Jacob obj-marker Pharaoh”) —
# blessing: Jacob blesses Pharaoh
m.bless("yaaqov", "paro")

# -------------------------- Gen.47.8 · HOW_MANY_YOUR_DAYS ------------------
# וַיֹּאמֶר פַּרְעֹה אֶל־יַעֲקֹב כַּמָּה יְמֵי שְׁנֵי חַיֶּיךָ
# "[EN-AID] And Pharaoh said to Jacob: How many are the days of the years of
# your life?"
m.step("Gen.47.8")
# ‹כַּמָּה יְמֵי שְׁנֵי חַיֶּיךָ› (“like-what day years alive-you/your”) —
# fact holds: kama-day-years-your-life
m.fact("kama_yeme_shene_chayekha")

# -------------------------- Gen.47.9 · FEW_AND_EVIL ------------------------
# וַיֹּאמֶר יַעֲקֹב אֶל־פַּרְעֹה יְמֵי שְׁנֵי מְגוּרַי שְׁלֹשִׁים וּמְאַת
# שָׁנָה מְעַט וְרָעִים הָיוּ יְמֵי שְׁנֵי חַיַּי וְלֹא הִשִּׂיגוּ אֶת־יְמֵי
# שְׁנֵי חַיֵּי אֲבֹתַי בִּימֵי מְגוּרֵיהֶם
# "[EN-AID] And Jacob said to Pharaoh: The days of the years of my
# sojournings are a hundred and thirty years; few and evil have been the
# days of the years of my life, and they have not reached the days of the
# years of the lives of my fathers in the days of their sojournings."
m.step("Gen.47.9")
# ‹מְעַט וְרָעִים הָיוּ יְמֵי שְׁנֵי חַיַּי› (“little and-bad be day years
# alive-me/my”) — fact holds: hundred-and-bad-day-years-chayai
m.fact("meat_ve_raim_yeme_shene_chayai")

# -------------------------- Gen.47.10 · THE_SECOND_BLESSING ----------------
# וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה וַיֵּצֵא מִלִּפְנֵי פַרְעֹה
# "[EN-AID] And Jacob blessed Pharaoh, and went out from before Pharaoh."
m.step("Gen.47.10")
# ‹וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה› (“and-bless Jacob obj-marker Pharaoh”) —
# event: berakh — agent Jacob; theme Pharaoh
m.event("berakh", agent="yaaqov", themes=["paro"])

# -------------------------- Gen.47.11 · SETTLED_IN_RAMESES -----------------
# וַיּוֹשֵׁב יוֹסֵף אֶת־אָבִיו וְאֶת־אֶחָיו וַיִּתֵּן לָהֶם אֲחֻזָּה
# בְּאֶרֶץ מִצְרַיִם בְּמֵיטַב הָאָרֶץ בְּאֶרֶץ רַעְמְסֵס כַּאֲשֶׁר צִוָּה
# פַרְעֹה
# "[EN-AID] And Joseph settled his father and his brothers, and gave them a
# holding in the land of Egypt, in the best of the land, in the land of
# Rameses, as Pharaoh had commanded."
m.step("Gen.47.11")
# ‹בְּמֵיטַב הָאָרֶץ בְּאֶרֶץ רַעְמְסֵס› (“in-best-part the-earth in-earth
# Raamses”) — fact holds: something-seized-in-earth-Raamses-kaasher-command-
# Pharaoh
m.fact("achuza_be_eretz_ramses_kaasher_tziva_faro")

# -------------------------- Gen.47.12 · BREAD_FOR_THE_MOUTHS ---------------
# וַיְכַלְכֵּל יוֹסֵף אֶת־אָבִיו וְאֶת־אֶחָיו וְאֵת כָּל־בֵּית אָבִיו לֶחֶם
# לְפִי הַטָּף
# "[EN-AID] And Joseph sustained his father, and his brothers, and all his
# father's house, with bread, by the mouth of the little ones."
m.step("Gen.47.12")
# ‹לֶחֶם לְפִי הַטָּף› (“food to-mouth the-family”) — fact holds: and-keep-
# in-food-lefi-hataf
m.fact("va_yekhalkel_lechem_lefi_hataf")

# -------------------------- Gen.47.13 · THE_LAND_LANGUISHES ----------------
# וְלֶחֶם אֵין בְּכָל־הָאָרֶץ כִּי־כָבֵד הָרָעָב מְאֹד וַתֵּלַהּ אֶרֶץ
# מִצְרַיִם וְאֶרֶץ כְּנַעַן מִפְּנֵי הָרָעָב
# "[EN-AID] And there was no bread in all the land, for the famine was very
# heavy; and the land of Egypt and the land of Canaan languished before the
# famine."
m.step("Gen.47.13")
# ‹וַתֵּלַהּ אֶרֶץ מִצְרַיִם וְאֶרֶץ כְּנַעַן מִפְּנֵי הָרָעָב› (“and-be-
# rabid earth Egypt and-earth Canaan from-face the-hunger”) — fact holds:
# and-telah-earth-Egypt-and-earth-Canaan
m.fact("va_telah_eretz_mitzrayim_ve_eretz_kenaan")

# -------------------------- Gen.47.14 · THE_SILVER_GATHERED ----------------
# וַיְלַקֵּט יוֹסֵף אֶת־כָּל־הַכֶּסֶף הַנִּמְצָא בְאֶרֶץ־מִצְרַיִם וּבְאֶרֶץ
# כְּנַעַן בַּשֶּׁבֶר אֲשֶׁר־הֵם שֹׁבְרִים וַיָּבֵא יוֹסֵף אֶת־הַכֶּסֶף
# בֵּיתָה פַרְעֹה
# "[EN-AID] And Joseph gleaned all the silver found in the land of Egypt and
# in the land of Canaan for the grain which they were buying; and Joseph
# brought the silver into Pharaoh's house."
m.step("Gen.47.14")
# ‹וַיָּבֵא יוֹסֵף אֶת־הַכֶּסֶף בֵּיתָה פַרְעֹה› (“and-come/bring Joseph
# obj-marker the-silver house-ward Pharaoh”) — fact holds: all-the-silver-
# beta-Pharaoh
m.fact("kol_ha_kesef_beta_faro")

# -------------------------- Gen.47.15 · GIVE_US_BREAD ----------------------
# וַיִּתֹּם הַכֶּסֶף מֵאֶרֶץ מִצְרַיִם וּמֵאֶרֶץ כְּנַעַן וַיָּבֹאוּ
# כָל־מִצְרַיִם אֶל־יוֹסֵף לֵאמֹר הָבָה־לָּנוּ לֶחֶם וְלָמָּה נָמוּת
# נֶגְדֶּךָ כִּי אָפֵס כָּסֶף
# "[EN-AID] And the silver was spent from the land of Egypt and from the
# land of Canaan; and all Egypt came to Joseph, saying: Give us bread — and
# why should we die before you, for the silver is gone."
m.step("Gen.47.15")
# ‹הָבָה־לָּנוּ לֶחֶם› (“give-ward to-us/our food”) — Egypt speaks a demand
# — LET: hava-lanu-food
m.declare("mitzrayim", "LET",
          "hava_lanu_lechem")

# -------------------------- Gen.47.16 · GIVE_YOUR_LIVESTOCK ----------------
# וַיֹּאמֶר יוֹסֵף הָבוּ מִקְנֵיכֶם וְאֶתְּנָה לָכֶם בְּמִקְנֵיכֶם אִם־אָפֵס
# כָּסֶף
# "[EN-AID] And Joseph said: Give your livestock, and I will give you for
# your livestock, if the silver is gone."
m.step("Gen.47.16")
# ‹הָבוּ מִקְנֵיכֶם וְאֶתְּנָה לָכֶם בְּמִקְנֵיכֶם› (“give something-bought-
# you/your(pl) and-set to-you/your(pl) in-something-bought-you/your”) — fact
# holds: give-miqnekhem-and-set-lakhem
m.fact("havu_miqnekhem_ve_etna_lakhem")

# -------------------------- Gen.47.17 · BREAD_FOR_THE_HERDS ----------------
# וַיָּבִיאוּ אֶת־מִקְנֵיהֶם אֶל־יוֹסֵף וַיִּתֵּן לָהֶם יוֹסֵף לֶחֶם
# בַּסּוּסִים וּבְמִקְנֵה הַצֹּאן וּבְמִקְנֵה הַבָּקָר וּבַחֲמֹרִים
# וַיְנַהֲלֵם בַּלֶּחֶם בְּכָל־מִקְנֵהֶם בַּשָּׁנָה הַהִוא
# "[EN-AID] And they brought their livestock to Joseph; and Joseph gave them
# bread for the horses, and for the livestock of the flocks, and for the
# livestock of the herds, and for the donkeys; and he carried them with
# bread for all their livestock that year."
m.step("Gen.47.17")
# ‹וַיְנַהֲלֵם בַּלֶּחֶם בְּכָל־מִקְנֵהֶם› (“and-run-with-asparkle-
# them/their in-food in-all something-bought-them/their”) — demand settled
# (popped from the queue): hava-lanu-food
m.result("hava_lanu_lechem", tmark="t2")

# -------------------------- Gen.47.18 · BODY_AND_GROUND --------------------
# וַתִּתֹּם הַשָּׁנָה הַהִוא וַיָּבֹאוּ אֵלָיו בַּשָּׁנָה הַשֵּׁנִית
# וַיֹּאמְרוּ לוֹ לֹא־נְכַחֵד מֵאֲדֹנִי כִּי אִם־תַּם הַכֶּסֶף וּמִקְנֵה
# הַבְּהֵמָה אֶל־אֲדֹנִי לֹא נִשְׁאַר לִפְנֵי אֲדֹנִי בִּלְתִּי
# אִם־גְּוִיָּתֵנוּ וְאַדְמָתֵנוּ
# "[EN-AID] And that year ended, and they came to him the second year and
# said to him: We will not hide from my lord that the silver is spent, and
# the herds of beasts are my lord's; nothing is left before my lord but our
# body and our ground."
m.step("Gen.47.18")
# ‹בִּלְתִּי אִם־גְּוִיָּתֵנוּ וְאַדְמָתֵנוּ› (“failure-of if body-us/our
# and-ground-us/our”) — fact holds: failure-of-if-geviyatenu-and-admatenu
m.fact("bilti_im_geviyatenu_ve_admatenu")

# -------------------------- Gen.47.19 · BUY_US_GIVE_SEED -------------------
# לָמָּה נָמוּת לְעֵינֶיךָ גַּם־אֲנַחְנוּ גַּם אַדְמָתֵנוּ קְנֵה־אֹתָנוּ
# וְאֶת־אַדְמָתֵנוּ בַּלָּחֶם וְנִהְיֶה אֲנַחְנוּ וְאַדְמָתֵנוּ עֲבָדִים
# לְפַרְעֹה וְתֶן־זֶרַע וְנִחְיֶה וְלֹא נָמוּת וְהָאֲדָמָה לֹא תֵשָׁם
# "[EN-AID] Why should we die before your eyes, both we and our ground too?
# Buy us and our ground for bread, and we with our ground will be servants
# to Pharaoh; and give seed, that we may live and not die, and the ground
# not be desolate."
m.step("Gen.47.19")
# ‹קְנֵה־אֹתָנוּ וְאֶת־אַדְמָתֵנוּ בַּלָּחֶם› (“possessor obj-marker-us/our
# and-obj-marker ground-us/our in-food”) — Egypt speaks a demand — LET:
# possessor-otanu-and-set-seed
m.declare("mitzrayim", "LET",
          "qene_otanu_ve_ten_zera")

# -------------------------- Gen.47.20 · THE_LAND_TO_PHARAOH ----------------
# וַיִּקֶן יוֹסֵף אֶת־כָּל־אַדְמַת מִצְרַיִם לְפַרְעֹה כִּי־מָכְרוּ
# מִצְרַיִם אִישׁ שָׂדֵהוּ כִּי־חָזַק עֲלֵהֶם הָרָעָב וַתְּהִי הָאָרֶץ
# לְפַרְעֹה
# "[EN-AID] And Joseph bought all the ground of Egypt for Pharaoh, for Egypt
# sold every man his field, for the famine was strong upon them; and the
# land became Pharaoh's."
m.step("Gen.47.20")
# ‹וַיִּקֶן יוֹסֵף אֶת־כָּל־אַדְמַת מִצְרַיִם לְפַרְעֹה› (“and-erect Joseph
# obj-marker all ground Egypt to-Pharaoh”) — fact holds: and-be-the-earth-
# to-Pharaoh
m.fact("va_tehi_ha_aretz_le_faro")

# -------------------------- Gen.47.21 · THE_PEOPLE_TO_CITIES ---------------
# וְאֶת־הָעָם הֶעֱבִיר אֹתוֹ לֶעָרִים מִקְצֵה גְבוּל־מִצְרַיִם וְעַד־קָצֵהוּ
# "[EN-AID] And the people — he moved them to the cities, from one end of
# the border of Egypt to its other end."
m.step("Gen.47.21")
# ‹וְאֶת־הָעָם הֶעֱבִיר אֹתוֹ לֶעָרִים› (“and-obj-marker the-people pass-
# over obj-marker-him/its to-city”) — fact holds: pass-over-it-to-city
m.fact("heevir_oto_le_arim")

# -------------------------- Gen.47.22 · THE_PRIESTS_EXEMPT -----------------
# רַק אַדְמַת הַכֹּהֲנִים לֹא קָנָה כִּי חֹק לַכֹּהֲנִים מֵאֵת פַּרְעֹה
# וְאָכְלוּ אֶת־חֻקָּם אֲשֶׁר נָתַן לָהֶם פַּרְעֹה עַל־כֵּן לֹא מָכְרוּ
# אֶת־אַדְמָתָם
# "[EN-AID] Only the ground of the priests he did not buy, for the priests
# had a statute-portion from Pharaoh, and they ate their statute-portion
# which Pharaoh gave them; therefore they did not sell their ground."
m.step("Gen.47.22")
# ‹רַק אַדְמַת הַכֹּהֲנִים לֹא קָנָה› (“leanness ground the-priest not
# possessor”) — fact holds: leanness-ground-the-priest-not-possessor
m.fact("raq_admat_ha_kohanim_lo_qana")

# -------------------------- Gen.47.23 · HERE_IS_SEED -----------------------
# וַיֹּאמֶר יוֹסֵף אֶל־הָעָם הֵן קָנִיתִי אֶתְכֶם הַיּוֹם וְאֶת־אַדְמַתְכֶם
# לְפַרְעֹה הֵא־לָכֶם זֶרַע וּזְרַעְתֶּם אֶת־הָאֲדָמָה
# "[EN-AID] And Joseph said to the people: Behold, I have bought you this
# day and your ground for Pharaoh; here is seed for you — and you shall sow
# the ground."
m.step("Gen.47.23")
# ‹הֵא־לָכֶם זֶרַע› (“lo! to-you/your(pl) seed”) — demand settled (popped
# from the queue): possessor-otanu-and-set-seed
m.result("qene_otanu_ve_ten_zera", tmark="t3")

# -------------------------- Gen.47.24 · THE_FIFTH_NAMED --------------------
# וְהָיָה בַּתְּבוּאֹת וּנְתַתֶּם חֲמִישִׁית לְפַרְעֹה וְאַרְבַּע הַיָּדֹת
# יִהְיֶה לָכֶם לְזֶרַע הַשָּׂדֶה וּלְאָכְלְכֶם וְלַאֲשֶׁר בְּבָתֵּיכֶם
# וְלֶאֱכֹל לְטַפְּכֶם
# "[EN-AID] And it shall be at the ingatherings, that you shall give a fifth
# to Pharaoh; and four hands shall be yours: for seed of the field, and for
# your food, and for those in your houses, and for your little ones to eat."
m.step("Gen.47.24")
# ‹וּנְתַתֶּם חֲמִישִׁית לְפַרְעֹה› (“and-set fifth to-Pharaoh”) — fact
# holds: and-set-fifth-to-Pharaoh
m.fact("u_netatem_chamishit_le_faro")

# -------------------------- Gen.47.25 · YOU_HAVE_KEPT_US_ALIVE -------------
# וַיֹּאמְרוּ הֶחֱיִתָנוּ נִמְצָא־חֵן בְּעֵינֵי אֲדֹנִי וְהָיִינוּ עֲבָדִים
# לְפַרְעֹה
# "[EN-AID] And they said: You have kept us alive; let us find favor in the
# eyes of my lord, and we will be servants to Pharaoh."
m.step("Gen.47.25")
# ‹וַיֹּאמְרוּ הֶחֱיִתָנוּ› (“and-say live-us/our”) — fact holds:
# hecheyitanu-find-graciousness
m.fact("hecheyitanu_nimtza_chen")

# -------------------------- Gen.47.26 · THE_FIFTH_A_STATUTE ----------------
# וַיָּשֶׂם אֹתָהּ יוֹסֵף לְחֹק עַד־הַיּוֹם הַזֶּה עַל־אַדְמַת מִצְרַיִם
# לְפַרְעֹה לַחֹמֶשׁ רַק אַדְמַת הַכֹּהֲנִים לְבַדָּם לֹא הָיְתָה לְפַרְעֹה
# "[EN-AID] And Joseph set it as a statute to this day upon the ground of
# Egypt: to Pharaoh a fifth; only the ground of the priests alone did not
# become Pharaoh's."
m.step("Gen.47.26")
# ‹וַיָּשֶׂם אֹתָהּ יוֹסֵף לְחֹק עַד־הַיּוֹם הַזֶּה עַל־אַדְמַת מִצְרַיִם
# לְפַרְעֹה לַחֹמֶשׁ› (“and-put/set obj-marker-her/its Joseph to-enactment
# until the-day the-this over ground Egypt to-Pharaoh to-fifth-tax”) —
m.statute("BIND", "le_faro_la_chomesh")

# -------------------------- Gen.47.27 · FRUITFUL_IN_GOSHEN -----------------
# וַיֵּשֶׁב יִשְׂרָאֵל בְּאֶרֶץ מִצְרַיִם בְּאֶרֶץ גֹּשֶׁן וַיֵּאָחֲזוּ בָהּ
# וַיִּפְרוּ וַיִּרְבּוּ מְאֹד
# "[EN-AID] And Israel dwelt in the land of Egypt, in the land of Goshen;
# and they took holding in it, and were fruitful, and multiplied greatly."
m.step("Gen.47.27")
# ‹וַיֵּאָחֲזוּ בָהּ וַיִּפְרוּ וַיִּרְבּוּ מְאֹד› (“and-seize in-her/its
# and-be-fruitful and-multiply very”) — fact holds: and-be-fruitful-and-
# multiply-very
m.fact("va_yifru_va_yirbu_meod")

# -------------------------- Gen.47.28 · SEVENTEEN_YEARS --------------------
# וַיְחִי יַעֲקֹב בְּאֶרֶץ מִצְרַיִם שְׁבַע עֶשְׂרֵה שָׁנָה וַיְהִי
# יְמֵי־יַעֲקֹב שְׁנֵי חַיָּיו שֶׁבַע שָׁנִים וְאַרְבָּעִים וּמְאַת שָׁנָה
# "[EN-AID] And Jacob lived in the land of Egypt seventeen years; and the
# days of Jacob, the years of his life, were seven years and forty and a
# hundred years."
m.step("Gen.47.28")
# ‹וַיְחִי יַעֲקֹב בְּאֶרֶץ מִצְרַיִם שְׁבַע עֶשְׂרֵה שָׁנָה› (“and-live
# Jacob in-earth Egypt seven -teen years”) — fact holds: day-Jacob-seven-
# forty-and-hundred-years
m.fact("yeme_yaaqov_sheva_arbaim_u_meat_shana")

# -------------------------- Gen.47.29 · THE_THIGH_AND_THE_BAN --------------
# וַיִּקְרְבוּ יְמֵי־יִשְׂרָאֵל לָמוּת וַיִּקְרָא לִבְנוֹ לְיוֹסֵף וַיֹּאמֶר
# לוֹ אִם־נָא מָצָאתִי חֵן בְּעֵינֶיךָ שִׂים־נָא יָדְךָ תַּחַת יְרֵכִי
# וְעָשִׂיתָ עִמָּדִי חֶסֶד וֶאֱמֶת אַל־נָא תִקְבְּרֵנִי בְּמִצְרָיִם
# "[EN-AID] And the days of Israel drew near to die; and he called his son
# Joseph, and said to him: If, pray, I have found favor in your eyes, put,
# pray, your hand under my thigh, and do with me kindness and truth: do not,
# pray, bury me in Egypt."
m.step("Gen.47.29")
# ‹אַל־נָא תִקְבְּרֵנִי בְּמִצְרָיִם› (“do-not please inter-me/my in-Egypt”)
# — Israel speaks a demand — LET-NOT: over-please-tiqbreni-in-Egypt
m.declare("yisrael", "LET-NOT",
          "al_na_tiqbreni_be_mitzrayim")

# -------------------------- Gen.47.30 · CARRY_ME_AND_BURY_ME ---------------
# וְשָׁכַבְתִּי עִם־אֲבֹתַי וּנְשָׂאתַנִי מִמִּצְרַיִם וּקְבַרְתַּנִי
# בִּקְבֻרָתָם וַיֹּאמַר אָנֹכִי אֶעֱשֶׂה כִדְבָרֶךָ
# "[EN-AID] And I will lie with my fathers, and you shall carry me from
# Egypt, and bury me in their burying-place. And he said: I will do
# according to your word."
m.step("Gen.47.30")
# ‹וּנְשָׂאתַנִי מִמִּצְרַיִם וּקְבַרְתַּנִי בִּקְבֻרָתָם› (“and-lift/carry-
# me/my from-Egypt and-inter-me/my in-sepulture-them/their”) — Israel speaks
# a demand — LET: and-qevartani-bi-qvuratam
m.declare("yisrael", "LET",
          "u_qevartani_bi_qvuratam")

# -------------------------- Gen.47.31 · SWEAR_TO_ME ------------------------
# וַיֹּאמֶר הִשָּׁבְעָה לִי וַיִּשָּׁבַע לוֹ וַיִּשְׁתַּחוּ יִשְׂרָאֵל
# עַל־רֹאשׁ הַמִּטָּה
# "[EN-AID] And he said: Swear to me. And he swore to him. And Israel bowed
# upon the head of the bed."
m.step("Gen.47.31")
# ‹וַיֹּאמֶר הִשָּׁבְעָה לִי› (“and-say swear-ward to-me/my”) — Israel
# speaks a demand — LET: hishava-to-me
m.declare("yisrael", "LET",
          "hishava_li")
# ‹וַיִּשָּׁבַע לוֹ› (“and-swear to-him/its”) — demand settled (popped from
# the queue): hishava-to-me
m.result("hishava_li", tmark="t4")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['al_na_tiqbreni_be_mitzrayim', 'u_qevartani_bi_qvuratam']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yaged_le_faro_bau_me_eretz_kenaan', 'chamisha_anashim_lifne_faro', 'roe_tzon_avadekha_gam_anachnu_gam_avotenu', 'avikha_ve_achekha_bau_elekha', 'kama_yeme_shene_chayekha', 'meat_ve_raim_yeme_shene_chayai', 'achuza_be_eretz_ramses_kaasher_tziva_faro', 'va_yekhalkel_lechem_lefi_hataf', 'va_telah_eretz_mitzrayim_ve_eretz_kenaan', 'kol_ha_kesef_beta_faro', 'havu_miqnekhem_ve_etna_lakhem', 'bilti_im_geviyatenu_ve_admatenu', 'va_tehi_ha_aretz_le_faro', 'heevir_oto_le_arim', 'raq_admat_ha_kohanim_lo_qana', 'u_netatem_chamishit_le_faro', 'hecheyitanu_nimtza_chen', 'statute: BIND(le_faro_la_chomesh)', 'va_yifru_va_yirbu_meod', 'yeme_yaaqov_sheva_arbaim_u_meat_shana'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 13
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
