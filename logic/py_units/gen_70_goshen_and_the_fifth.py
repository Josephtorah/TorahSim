#!/usr/bin/env python3
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
# ‹וַיָּבֹא יוֹסֵף וַיַּגֵּד› (“and-come/bring Joseph and-tell”)
# ‹לְפַרְעֹה וַיֹּאמֶר אָבִי› (“to-Pharaoh and-say father-me/my”)
# ‹וְאַחַי וְצֹאנָם וּבְקָרָם› (“and-brother-me/my and-flock-them/their and-
# herd-them/their”)
# ‹וְכָל־אֲשֶׁר לָהֶם בָּאוּ› (“and-all which to-them/their come/bring”)
# ‹מֵאֶרֶץ כְּנָעַן וְהִנָּם› (“from-earth Canaan and-lo!-them/their”)
# ‹בְּאֶרֶץ גֹּשֶׁן› (“in-earth Goshen”)
# "[EN-AID] And Joseph came and told Pharaoh, and said: My father and my
# brothers, with their flocks and their herds and all that is theirs, have
# come from the land of Canaan; and behold, they are in the land of Goshen."
m.step("Gen.47.1")
# ‹וַיָּבֹא יוֹסֵף וַיַּגֵּד› (“and-come/bring Joseph and-tell”)
# ‹לְפַרְעֹה› (“to-Pharaoh”)
# — fact holds: and-tell-to-Pharaoh-come/bring-from-earth-Canaan
m.fact("va_yaged_le_faro_bau_me_eretz_kenaan")

# -------------------------- Gen.47.2 · FIVE_FROM_THE_EDGE ------------------
# ‹וּמִקְצֵה אֶחָיו לָקַח› (“and-from-end brother-him/its take”)
# ‹חֲמִשָּׁה אֲנָשִׁים וַיַּצִּגֵם› (“five man and-place-permanently-
# them/their”)
# ‹לִפְנֵי פַרְעֹה› (“to-face Pharaoh”)
# "[EN-AID] And from the edge of his brothers he took five men, and
# presented them before Pharaoh."
m.step("Gen.47.2")
# ‹וּמִקְצֵה אֶחָיו לָקַח› (“and-from-end brother-him/its take”)
# ‹חֲמִשָּׁה אֲנָשִׁים› (“five man”)
# — fact holds: five-man-lifne-Pharaoh
m.fact("chamisha_anashim_lifne_faro")
# witness-grounded state (its own tier):
# a_roster_decided_by_a_spelling_pattern_in_deuteronomy on
# five_men_from_the_edge
m.witness_state("five_men_from_the_edge", "a_roster_decided_by_a_spelling_pattern_in_deuteronomy",
                cites=["Bereshit Rabbah 95:4"])

# -------------------------- Gen.47.3 · THE_SCRIPT_PERFORMED ----------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־אֶחָיו› (“and-say Pharaoh to brother-him/its”)
# ‹מַה־מַּעֲשֵׂיכֶם וַיֹּאמְרוּ אֶל־פַּרְעֹה› (“what deed/work-you/your(pl)
# and-say to Pharaoh”)
# ‹רֹעֵה צֹאן עֲבָדֶיךָ› (“graze flock servant-you/your”)
# ‹גַּם־אֲנַחְנוּ גַּם־אֲבוֹתֵינוּ› (“also we also father-us/our”)
# "[EN-AID] And Pharaoh said to his brothers: What is your work? And they
# said to Pharaoh: Your servants are a shepherd of flocks, both we and our
# fathers."
m.step("Gen.47.3")
# ‹רֹעֵה צֹאן עֲבָדֶיךָ› (“graze flock servant-you/your”)
# ‹גַּם־אֲנַחְנוּ גַּם־אֲבוֹתֵינוּ› (“also we also father-us/our”)
# — fact holds: graze-flock-avadekha-also-we-also-avotenu
m.fact("roe_tzon_avadekha_gam_anachnu_gam_avotenu")

# -------------------------- Gen.47.4 · LET_US_DWELL_IN_GOSHEN --------------
# ‹וַיֹּאמְרוּ אֶל־פַּרְעֹה לָגוּר› (“and-say to Pharaoh to-turn-aside-from-
# the-road”)
# ‹בָּאָרֶץ בָּאנוּ כִּי־אֵין› (“in-earth come/bring that there-is-not”)
# ‹מִרְעֶה לַצֹּאן אֲשֶׁר› (“pasture to-flock which”)
# ‹לַעֲבָדֶיךָ כִּי־כָבֵד הָרָעָב› (“to-servant-you/your that heavy the-
# hunger”)
# ‹בְּאֶרֶץ כְּנָעַן וְעַתָּה› (“in-earth Canaan and-now”)
# ‹יֵשְׁבוּ־נָא עֲבָדֶיךָ בְּאֶרֶץ› (“dwell/sit please servant-you/your in-
# earth”)
# ‹גֹּשֶׁן› (“Goshen”)
# "[EN-AID] And they said to Pharaoh: To sojourn in the land we have come,
# for there is no pasture for the flock of your servants, for the famine is
# heavy in the land of Canaan; and now, let your servants dwell, pray, in
# the land of Goshen."
m.step("Gen.47.4")
# ‹וְעַתָּה יֵשְׁבוּ־נָא עֲבָדֶיךָ› (“and-now dwell/sit please servant-
# you/your”)
# ‹בְּאֶרֶץ גֹּשֶׁן› (“in-earth Goshen”)
# — bene-Jacob speaks a demand — LET: dwell/sit-please-avadekha-in-earth-
# Goshen
m.declare("bene_yaaqov", "LET",
          "yeshvu_na_avadekha_be_eretz_goshen")
# witness-tier presupposed read: the_paved_way_taking_its_third_seat on
# we_have_come_to_sojourn — read, not installed
m.witness_read("we_have_come_to_sojourn", "the_paved_way_taking_its_third_seat",
                cites=["Bereshit Rabbah 40:6", "Onkelos Genesis 47:4"])

# -------------------------- Gen.47.5 · THEY_HAVE_COME_TO_YOU ---------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹לֵאמֹר אָבִיךָ וְאַחֶיךָ› (“to-say father-you/your and-brother-you/your”)
# ‹בָּאוּ אֵלֶיךָ› (“come/bring to-you/your”)
# "[EN-AID] And Pharaoh said to Joseph, saying: Your father and your
# brothers have come to you."
m.step("Gen.47.5")
# ‹אָבִיךָ וְאַחֶיךָ בָּאוּ› (“father-you/your and-brother-you/your
# come/bring”)
# ‹אֵלֶיךָ› (“to-you/your”)
# — fact holds: avikha-and-achekha-come/bring-to-you
m.fact("avikha_ve_achekha_bau_elekha")

# -------------------------- Gen.47.6 · THE_LAND_BEFORE_YOU -----------------
# ‹אֶרֶץ מִצְרַיִם לְפָנֶיךָ› (“earth Egypt to-face-you/your”)
# ‹הִוא בְּמֵיטַב הָאָרֶץ› (“he/it in-best-part the-earth”)
# ‹הוֹשֵׁב אֶת־אָבִיךָ וְאֶת־אַחֶיךָ› (“dwell/sit obj-marker father-you/your
# and-obj-marker brother-you/your”)
# ‹יֵשְׁבוּ בְּאֶרֶץ גֹּשֶׁן› (“dwell/sit in-earth Goshen”)
# ‹וְאִם־יָדַעְתָּ וְיֶשׁ־בָּם אַנְשֵׁי־חַיִל› (“and-if know and-there-is
# in-them/their man force”)
# ‹וְשַׂמְתָּם שָׂרֵי מִקְנֶה› (“and-put/set-them/their officer something-
# bought”)
# ‹עַל־אֲשֶׁר־לִי› (“over which to-me/my”)
# "[EN-AID] The land of Egypt is before you: in the best of the land settle
# your father and your brothers; let them dwell in the land of Goshen. And
# if you know that there are able men among them, set them as chiefs of
# livestock over what is mine."
m.step("Gen.47.6")
# ‹יֵשְׁבוּ בְּאֶרֶץ גֹּשֶׁן› (“dwell/sit in-earth Goshen”)
# — demand settled (popped from the queue): dwell/sit-please-avadekha-in-
# earth-Goshen
m.result("yeshvu_na_avadekha_be_eretz_goshen", tmark="t1")

# -------------------------- Gen.47.7 · JACOB_BLESSES_PHARAOH ---------------
# ‹וַיָּבֵא יוֹסֵף אֶת־יַעֲקֹב› (“and-come/bring Joseph obj-marker Jacob”)
# ‹אָבִיו וַיַּעֲמִדֵהוּ לִפְנֵי› (“father-him/its and-stand-him/its to-
# face”)
# ‹פַרְעֹה וַיְבָרֶךְ יַעֲקֹב› (“Pharaoh and-bless Jacob”)
# ‹אֶת־פַּרְעֹה› (“obj-marker Pharaoh”)
# "[EN-AID] And Joseph brought Jacob his father, and stood him before
# Pharaoh; and Jacob blessed Pharaoh."
m.step("Gen.47.7")
# ‹וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה› (“and-bless Jacob obj-marker Pharaoh”)
# — blessing: Jacob blesses Pharaoh
m.bless("yaaqov", "paro")

# -------------------------- Gen.47.8 · HOW_MANY_YOUR_DAYS ------------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יַעֲקֹב› (“and-say Pharaoh to Jacob”)
# ‹כַּמָּה יְמֵי שְׁנֵי› (“like-what day years”)
# ‹חַיֶּיךָ› (“alive-you/your”)
# "[EN-AID] And Pharaoh said to Jacob: How many are the days of the years of
# your life?"
m.step("Gen.47.8")
# ‹כַּמָּה יְמֵי שְׁנֵי› (“like-what day years”)
# ‹חַיֶּיךָ› (“alive-you/your”)
# — fact holds: kama-day-years-your-life
m.fact("kama_yeme_shene_chayekha")

# -------------------------- Gen.47.9 · FEW_AND_EVIL ------------------------
# ‹וַיֹּאמֶר יַעֲקֹב אֶל־פַּרְעֹה› (“and-say Jacob to Pharaoh”)
# ‹יְמֵי שְׁנֵי מְגוּרַי› (“day years sojourning-me/my”)
# ‹שְׁלֹשִׁים וּמְאַת שָׁנָה› (“thirty and-hundred years”)
# ‹מְעַט וְרָעִים הָיוּ› (“little and-bad be”)
# ‹יְמֵי שְׁנֵי חַיַּי› (“day years alive-me/my”)
# ‹וְלֹא הִשִּׂיגוּ אֶת־יְמֵי› (“and-not reach obj-marker day”)
# ‹שְׁנֵי חַיֵּי אֲבֹתַי› (“years alive father-me/my”)
# ‹בִּימֵי מְגוּרֵיהֶם› (“in-day sojourning-them/their”)
# "[EN-AID] And Jacob said to Pharaoh: The days of the years of my
# sojournings are a hundred and thirty years; few and evil have been the
# days of the years of my life, and they have not reached the days of the
# years of the lives of my fathers in the days of their sojournings."
m.step("Gen.47.9")
# ‹מְעַט וְרָעִים הָיוּ› (“little and-bad be”)
# ‹יְמֵי שְׁנֵי חַיַּי› (“day years alive-me/my”)
# — fact holds: hundred-and-bad-day-years-chayai
m.fact("meat_ve_raim_yeme_shene_chayai")

# -------------------------- Gen.47.10 · THE_SECOND_BLESSING ----------------
# ‹וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה› (“and-bless Jacob obj-marker Pharaoh”)
# ‹וַיֵּצֵא מִלִּפְנֵי פַרְעֹה› (“and-bring-forth from-to-face Pharaoh”)
# "[EN-AID] And Jacob blessed Pharaoh, and went out from before Pharaoh."
m.step("Gen.47.10")
# ‹וַיְבָרֶךְ יַעֲקֹב אֶת־פַּרְעֹה› (“and-bless Jacob obj-marker Pharaoh”)
# — event: berakh — agent Jacob; theme Pharaoh
m.event("berakh", agent="yaaqov", themes=["paro"])

# -------------------------- Gen.47.11 · SETTLED_IN_RAMESES -----------------
# ‹וַיּוֹשֵׁב יוֹסֵף אֶת־אָבִיו› (“and-dwell/sit Joseph obj-marker father-
# him/its”)
# ‹וְאֶת־אֶחָיו וַיִּתֵּן לָהֶם› (“and-obj-marker brother-him/its and-set
# to-them/their”)
# ‹אֲחֻזָּה בְּאֶרֶץ מִצְרַיִם› (“something-seized in-earth Egypt”)
# ‹בְּמֵיטַב הָאָרֶץ בְּאֶרֶץ› (“in-best-part the-earth in-earth”)
# ‹רַעְמְסֵס כַּאֲשֶׁר צִוָּה› (“Raamses like-as/which command”)
# ‹פַרְעֹה› (“Pharaoh”)
# "[EN-AID] And Joseph settled his father and his brothers, and gave them a
# holding in the land of Egypt, in the best of the land, in the land of
# Rameses, as Pharaoh had commanded."
m.step("Gen.47.11")
# ‹בְּמֵיטַב הָאָרֶץ בְּאֶרֶץ› (“in-best-part the-earth in-earth”)
# ‹רַעְמְסֵס› (“Raamses”)
# — fact holds: something-seized-in-earth-Raamses-kaasher-command-Pharaoh
m.fact("achuza_be_eretz_ramses_kaasher_tziva_faro")
# witness-grounded state (its own tier):
# a_decree_of_chains_executing_in_its_softened_form on
# settled_in_the_best_of_the_land
m.witness_state("settled_in_the_best_of_the_land", "a_decree_of_chains_executing_in_its_softened_form",
                cites=["Bereshit Rabbah 86:2"])

# -------------------------- Gen.47.12 · BREAD_FOR_THE_MOUTHS ---------------
# ‹וַיְכַלְכֵּל יוֹסֵף אֶת־אָבִיו› (“and-keep-in Joseph obj-marker father-
# him/its”)
# ‹וְאֶת־אֶחָיו וְאֵת כָּל־בֵּית› (“and-obj-marker brother-him/its and-obj-
# marker all house”)
# ‹אָבִיו לֶחֶם לְפִי› (“father-him/its food to-mouth”)
# ‹הַטָּף› (“the-family”)
# "[EN-AID] And Joseph sustained his father, and his brothers, and all his
# father's house, with bread, by the mouth of the little ones."
m.step("Gen.47.12")
# ‹לֶחֶם לְפִי הַטָּף› (“food to-mouth the-family”)
# — fact holds: and-keep-in-food-lefi-hataf
m.fact("va_yekhalkel_lechem_lefi_hataf")

# -------------------------- Gen.47.13 · THE_LAND_LANGUISHES ----------------
# ‹וְלֶחֶם אֵין בְּכָל־הָאָרֶץ› (“and-food there-is-not in-all the-earth”)
# ‹כִּי־כָבֵד הָרָעָב מְאֹד› (“that heavy the-hunger very”)
# ‹וַתֵּלַהּ אֶרֶץ מִצְרַיִם› (“and-be-rabid earth Egypt”)
# ‹וְאֶרֶץ כְּנַעַן מִפְּנֵי› (“and-earth Canaan from-face”)
# ‹הָרָעָב› (“the-hunger”)
# "[EN-AID] And there was no bread in all the land, for the famine was very
# heavy; and the land of Egypt and the land of Canaan languished before the
# famine."
m.step("Gen.47.13")
# ‹וַתֵּלַהּ אֶרֶץ מִצְרַיִם› (“and-be-rabid earth Egypt”)
# ‹וְאֶרֶץ כְּנַעַן מִפְּנֵי› (“and-earth Canaan from-face”)
# ‹הָרָעָב› (“the-hunger”)
# — fact holds: and-telah-earth-Egypt-and-earth-Canaan
m.fact("va_telah_eretz_mitzrayim_ve_eretz_kenaan")

# -------------------------- Gen.47.14 · THE_SILVER_GATHERED ----------------
# ‹וַיְלַקֵּט יוֹסֵף אֶת־כָּל־הַכֶּסֶף› (“and-pick-up Joseph obj-marker all
# the-silver”)
# ‹הַנִּמְצָא בְאֶרֶץ־מִצְרַיִם וּבְאֶרֶץ› (“the-find in-earth Egypt and-in-
# earth”)
# ‹כְּנַעַן בַּשֶּׁבֶר אֲשֶׁר־הֵם› (“Canaan in-grain which they”)
# ‹שֹׁבְרִים וַיָּבֵא יוֹסֵף› (“deal-in-grain and-come/bring Joseph”)
# ‹אֶת־הַכֶּסֶף בֵּיתָה פַרְעֹה› (“obj-marker the-silver house-ward
# Pharaoh”)
# "[EN-AID] And Joseph gleaned all the silver found in the land of Egypt and
# in the land of Canaan for the grain which they were buying; and Joseph
# brought the silver into Pharaoh's house."
m.step("Gen.47.14")
# ‹וַיָּבֵא יוֹסֵף אֶת־הַכֶּסֶף› (“and-come/bring Joseph obj-marker the-
# silver”)
# ‹בֵּיתָה פַרְעֹה› (“house-ward Pharaoh”)
# — fact holds: all-the-silver-beta-Pharaoh
m.fact("kol_ha_kesef_beta_faro")

# -------------------------- Gen.47.15 · GIVE_US_BREAD ----------------------
# ‹וַיִּתֹּם הַכֶּסֶף מֵאֶרֶץ› (“and-complete the-silver from-earth”)
# ‹מִצְרַיִם וּמֵאֶרֶץ כְּנַעַן› (“Egypt and-from-earth Canaan”)
# ‹וַיָּבֹאוּ כָל־מִצְרַיִם אֶל־יוֹסֵף› (“and-come/bring all Egyptian to
# Joseph”)
# ‹לֵאמֹר הָבָה־לָּנוּ לֶחֶם› (“to-say give-ward to-us/our food”)
# ‹וְלָמָּה נָמוּת נֶגְדֶּךָ› (“and-to-what die front-you/your”)
# ‹כִּי אָפֵס כָּסֶף› (“that disappear silver”)
# "[EN-AID] And the silver was spent from the land of Egypt and from the
# land of Canaan; and all Egypt came to Joseph, saying: Give us bread — and
# why should we die before you, for the silver is gone."
m.step("Gen.47.15")
# ‹הָבָה־לָּנוּ לֶחֶם› (“give-ward to-us/our food”)
# — Egypt speaks a demand — LET: hava-lanu-food
m.declare("mitzrayim", "LET",
          "hava_lanu_lechem")

# -------------------------- Gen.47.16 · GIVE_YOUR_LIVESTOCK ----------------
# ‹וַיֹּאמֶר יוֹסֵף הָבוּ› (“and-say Joseph give”)
# ‹מִקְנֵיכֶם וְאֶתְּנָה לָכֶם› (“something-bought-you/your(pl) and-set to-
# you/your(pl)”)
# ‹בְּמִקְנֵיכֶם אִם־אָפֵס כָּסֶף› (“in-something-bought-you/your if
# disappear silver”)
# "[EN-AID] And Joseph said: Give your livestock, and I will give you for
# your livestock, if the silver is gone."
m.step("Gen.47.16")
# ‹הָבוּ מִקְנֵיכֶם וְאֶתְּנָה› (“give something-bought-you/your(pl) and-
# set”)
# ‹לָכֶם בְּמִקְנֵיכֶם› (“to-you/your(pl) in-something-bought-you/your”)
# — fact holds: give-miqnekhem-and-set-lakhem
m.fact("havu_miqnekhem_ve_etna_lakhem")

# -------------------------- Gen.47.17 · BREAD_FOR_THE_HERDS ----------------
# ‹וַיָּבִיאוּ אֶת־מִקְנֵיהֶם אֶל־יוֹסֵף› (“and-come/bring obj-marker
# something-bought-them/their to Joseph”)
# ‹וַיִּתֵּן לָהֶם יוֹסֵף› (“and-set to-them/their Joseph”)
# ‹לֶחֶם בַּסּוּסִים וּבְמִקְנֵה› (“food in-horse and-in-something-bought”)
# ‹הַצֹּאן וּבְמִקְנֵה הַבָּקָר› (“the-flock and-in-something-bought the-
# herd”)
# ‹וּבַחֲמֹרִים וַיְנַהֲלֵם בַּלֶּחֶם› (“and-in-male-ass and-run-with-
# asparkle-them/their in-food”)
# ‹בְּכָל־מִקְנֵהֶם בַּשָּׁנָה הַהִוא› (“in-all something-bought-them/their
# in-years that”)
# "[EN-AID] And they brought their livestock to Joseph; and Joseph gave them
# bread for the horses, and for the livestock of the flocks, and for the
# livestock of the herds, and for the donkeys; and he carried them with
# bread for all their livestock that year."
m.step("Gen.47.17")
# ‹וַיְנַהֲלֵם בַּלֶּחֶם בְּכָל־מִקְנֵהֶם› (“and-run-with-asparkle-
# them/their in-food in-all something-bought-them/their”)
# — demand settled (popped from the queue): hava-lanu-food
m.result("hava_lanu_lechem", tmark="t2")

# -------------------------- Gen.47.18 · BODY_AND_GROUND --------------------
# ‹וַתִּתֹּם הַשָּׁנָה הַהִוא› (“and-complete the-years that”)
# ‹וַיָּבֹאוּ אֵלָיו בַּשָּׁנָה› (“and-come/bring to-him/its in-years”)
# ‹הַשֵּׁנִית וַיֹּאמְרוּ לוֹ› (“the-second and-say to-him/its”)
# ‹לֹא־נְכַחֵד מֵאֲדֹנִי כִּי› (“not secrete from-lord-me/my very-widely-
# used-as-a-relati”)
# ‹אִם־תַּם הַכֶּסֶף וּמִקְנֵה› (“as-demonstrative complete the-silver and-
# something-bought”)
# ‹הַבְּהֵמָה אֶל־אֲדֹנִי לֹא› (“the-livestock to lord-me/my not”)
# ‹נִשְׁאַר לִפְנֵי אֲדֹנִי› (“swell-up to-face lord-me/my”)
# ‹בִּלְתִּי אִם־גְּוִיָּתֵנוּ וְאַדְמָתֵנוּ› (“failure-of if body-us/our
# and-ground-us/our”)
# "[EN-AID] And that year ended, and they came to him the second year and
# said to him: We will not hide from my lord that the silver is spent, and
# the herds of beasts are my lord's; nothing is left before my lord but our
# body and our ground."
m.step("Gen.47.18")
# ‹בִּלְתִּי אִם־גְּוִיָּתֵנוּ וְאַדְמָתֵנוּ› (“failure-of if body-us/our
# and-ground-us/our”)
# — fact holds: failure-of-if-geviyatenu-and-admatenu
m.fact("bilti_im_geviyatenu_ve_admatenu")

# -------------------------- Gen.47.19 · BUY_US_GIVE_SEED -------------------
# ‹לָמָּה נָמוּת לְעֵינֶיךָ› (“to-what die to-eye-you/your”)
# ‹גַּם־אֲנַחְנוּ גַּם אַדְמָתֵנוּ› (“also we also ground-us/our”)
# ‹קְנֵה־אֹתָנוּ וְאֶת־אַדְמָתֵנוּ בַּלָּחֶם› (“possessor obj-marker-us/our
# and-obj-marker ground-us/our in-food”)
# ‹וְנִהְיֶה אֲנַחְנוּ וְאַדְמָתֵנוּ› (“and-be we and-ground-us/our”)
# ‹עֲבָדִים לְפַרְעֹה וְתֶן־זֶרַע› (“servant to-Pharaoh and-set seed”)
# ‹וְנִחְיֶה וְלֹא נָמוּת› (“and-live and-not die”)
# ‹וְהָאֲדָמָה לֹא תֵשָׁם› (“and-the-ground not lie-waste”)
# "[EN-AID] Why should we die before your eyes, both we and our ground too?
# Buy us and our ground for bread, and we with our ground will be servants
# to Pharaoh; and give seed, that we may live and not die, and the ground
# not be desolate."
m.step("Gen.47.19")
# ‹קְנֵה־אֹתָנוּ וְאֶת־אַדְמָתֵנוּ בַּלָּחֶם› (“possessor obj-marker-us/our
# and-obj-marker ground-us/our in-food”)
# — Egypt speaks a demand — LET: possessor-otanu-and-set-seed
m.declare("mitzrayim", "LET",
          "qene_otanu_ve_ten_zera")

# -------------------------- Gen.47.20 · THE_LAND_TO_PHARAOH ----------------
# ‹וַיִּקֶן יוֹסֵף אֶת־כָּל־אַדְמַת› (“and-erect Joseph obj-marker all
# ground”)
# ‹מִצְרַיִם לְפַרְעֹה כִּי־מָכְרוּ› (“Egypt to-Pharaoh that sell”)
# ‹מִצְרַיִם אִישׁ שָׂדֵהוּ› (“Egyptian man field-him/its”)
# ‹כִּי־חָזַק עֲלֵהֶם הָרָעָב› (“that fasten-upon over-them/their the-
# hunger”)
# ‹וַתְּהִי הָאָרֶץ לְפַרְעֹה› (“and-be the-earth to-Pharaoh”)
# "[EN-AID] And Joseph bought all the ground of Egypt for Pharaoh, for Egypt
# sold every man his field, for the famine was strong upon them; and the
# land became Pharaoh's."
m.step("Gen.47.20")
# ‹וַיִּקֶן יוֹסֵף אֶת־כָּל־אַדְמַת› (“and-erect Joseph obj-marker all
# ground”)
# ‹מִצְרַיִם לְפַרְעֹה› (“Egypt to-Pharaoh”)
# — fact holds: and-be-the-earth-to-Pharaoh
m.fact("va_tehi_ha_aretz_le_faro")

# -------------------------- Gen.47.21 · THE_PEOPLE_TO_CITIES ---------------
# ‹וְאֶת־הָעָם הֶעֱבִיר אֹתוֹ› (“and-obj-marker the-people pass-over obj-
# marker-him/its”)
# ‹לֶעָרִים מִקְצֵה גְבוּל־מִצְרַיִם› (“to-city from-end cord Egypt”)
# ‹וְעַד־קָצֵהוּ› (“and-until end-him/its”)
# "[EN-AID] And the people — he moved them to the cities, from one end of
# the border of Egypt to its other end."
m.step("Gen.47.21")
# ‹וְאֶת־הָעָם הֶעֱבִיר אֹתוֹ› (“and-obj-marker the-people pass-over obj-
# marker-him/its”)
# ‹לֶעָרִים› (“to-city”)
# — fact holds: pass-over-it-to-city
m.fact("heevir_oto_le_arim")
# witness-tier presupposed read: urbanization_or_population_transfer on
# he_moved_the_people — read, not installed
m.witness_read("he_moved_the_people", "urbanization_or_population_transfer",
                cites=["Onkelos Genesis 47:21"])

# -------------------------- Gen.47.22 · THE_PRIESTS_EXEMPT -----------------
# ‹רַק אַדְמַת הַכֹּהֲנִים› (“leanness ground the-priest”)
# ‹לֹא קָנָה כִּי› (“not possessor that”)
# ‹חֹק לַכֹּהֲנִים מֵאֵת› (“enactment to-priest from-with”)
# ‹פַּרְעֹה וְאָכְלוּ אֶת־חֻקָּם› (“Pharaoh and-eat obj-marker enactment-
# them/their”)
# ‹אֲשֶׁר נָתַן לָהֶם› (“which set to-them/their”)
# ‹פַּרְעֹה עַל־כֵּן לֹא› (“Pharaoh over so not”)
# ‹מָכְרוּ אֶת־אַדְמָתָם› (“sell obj-marker ground-them/their”)
# "[EN-AID] Only the ground of the priests he did not buy, for the priests
# had a statute-portion from Pharaoh, and they ate their statute-portion
# which Pharaoh gave them; therefore they did not sell their ground."
m.step("Gen.47.22")
# ‹רַק אַדְמַת הַכֹּהֲנִים› (“leanness ground the-priest”)
# ‹לֹא קָנָה› (“not possessor”)
# — fact holds: leanness-ground-the-priest-not-possessor
m.fact("raq_admat_ha_kohanim_lo_qana")

# -------------------------- Gen.47.23 · HERE_IS_SEED -----------------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־הָעָם› (“and-say Joseph to the-people”)
# ‹הֵן קָנִיתִי אֶתְכֶם› (“lo! possessor obj-marker-you/your(pl)”)
# ‹הַיּוֹם וְאֶת־אַדְמַתְכֶם לְפַרְעֹה› (“the-day and-obj-marker ground-
# you/your(pl) to-Pharaoh”)
# ‹הֵא־לָכֶם זֶרַע וּזְרַעְתֶּם› (“lo! to-you/your(pl) seed and-yield-seed”)
# ‹אֶת־הָאֲדָמָה› (“obj-marker the-ground”)
# "[EN-AID] And Joseph said to the people: Behold, I have bought you this
# day and your ground for Pharaoh; here is seed for you — and you shall sow
# the ground."
m.step("Gen.47.23")
# ‹הֵא־לָכֶם זֶרַע› (“lo! to-you/your(pl) seed”)
# — demand settled (popped from the queue): possessor-otanu-and-set-seed
m.result("qene_otanu_ve_ten_zera", tmark="t3")

# -------------------------- Gen.47.24 · THE_FIFTH_NAMED --------------------
# ‹וְהָיָה בַּתְּבוּאֹת וּנְתַתֶּם› (“and-be in-income and-set”)
# ‹חֲמִישִׁית לְפַרְעֹה וְאַרְבַּע› (“fifth to-Pharaoh and-four”)
# ‹הַיָּדֹת יִהְיֶה לָכֶם› (“the-hand be to-you/your(pl)”)
# ‹לְזֶרַע הַשָּׂדֶה וּלְאָכְלְכֶם› (“to-seed the-field and-to-food-
# you/your(pl)”)
# ‹וְלַאֲשֶׁר בְּבָתֵּיכֶם וְלֶאֱכֹל› (“and-to-which in-house-you/your(pl)
# and-to-eat”)
# ‹לְטַפְּכֶם› (“to-family-you/your(pl)”)
# "[EN-AID] And it shall be at the ingatherings, that you shall give a fifth
# to Pharaoh; and four hands shall be yours: for seed of the field, and for
# your food, and for those in your houses, and for your little ones to eat."
m.step("Gen.47.24")
# ‹וּנְתַתֶּם חֲמִישִׁית לְפַרְעֹה› (“and-set fifth to-Pharaoh”)
# — fact holds: and-set-fifth-to-Pharaoh
m.fact("u_netatem_chamishit_le_faro")

# -------------------------- Gen.47.25 · YOU_HAVE_KEPT_US_ALIVE -------------
# ‹וַיֹּאמְרוּ הֶחֱיִתָנוּ נִמְצָא־חֵן› (“and-say live-us/our find
# graciousness”)
# ‹בְּעֵינֵי אֲדֹנִי וְהָיִינוּ› (“in-eye lord-me/my and-be”)
# ‹עֲבָדִים לְפַרְעֹה› (“servant to-Pharaoh”)
# "[EN-AID] And they said: You have kept us alive; let us find favor in the
# eyes of my lord, and we will be servants to Pharaoh."
m.step("Gen.47.25")
# ‹וַיֹּאמְרוּ הֶחֱיִתָנוּ› (“and-say live-us/our”)
# — fact holds: hecheyitanu-find-graciousness
m.fact("hecheyitanu_nimtza_chen")

# -------------------------- Gen.47.26 · THE_FIFTH_A_STATUTE ----------------
# ‹וַיָּשֶׂם אֹתָהּ יוֹסֵף› (“and-put/set obj-marker-her/its Joseph”)
# ‹לְחֹק עַד־הַיּוֹם הַזֶּה› (“to-enactment until the-day the-this”)
# ‹עַל־אַדְמַת מִצְרַיִם לְפַרְעֹה› (“over ground Egypt to-Pharaoh”)
# ‹לַחֹמֶשׁ רַק אַדְמַת› (“to-fifth-tax leanness ground”)
# ‹הַכֹּהֲנִים לְבַדָּם לֹא› (“the-priest to-separation-them/their not”)
# ‹הָיְתָה לְפַרְעֹה› (“be to-Pharaoh”)
# "[EN-AID] And Joseph set it as a statute to this day upon the ground of
# Egypt: to Pharaoh a fifth; only the ground of the priests alone did not
# become Pharaoh's."
m.step("Gen.47.26")
# ‹וַיָּשֶׂם אֹתָהּ יוֹסֵף› (“and-put/set obj-marker-her/its Joseph”)
# ‹לְחֹק עַד־הַיּוֹם הַזֶּה› (“to-enactment until the-day the-this”)
# ‹עַל־אַדְמַת מִצְרַיִם לְפַרְעֹה› (“over ground Egypt to-Pharaoh”)
# ‹לַחֹמֶשׁ› (“to-fifth-tax”)
m.statute("BIND", "le_faro_la_chomesh")
# witness-tier presupposed read: the_blocks_one_permanent_law on
# the_fifth_is_pharaohs — read, not installed
m.witness_read("the_fifth_is_pharaohs", "the_blocks_one_permanent_law",
                cites=["Onkelos Genesis 47:22", "Onkelos Genesis 47:26", "Bereshit Rabbah 90:6"])

# -------------------------- Gen.47.27 · FRUITFUL_IN_GOSHEN -----------------
# ‹וַיֵּשֶׁב יִשְׂרָאֵל בְּאֶרֶץ› (“and-dwell/sit Israel in-earth”)
# ‹מִצְרַיִם בְּאֶרֶץ גֹּשֶׁן› (“Egypt in-earth Goshen”)
# ‹וַיֵּאָחֲזוּ בָהּ וַיִּפְרוּ› (“and-seize in-her/its and-be-fruitful”)
# ‹וַיִּרְבּוּ מְאֹד› (“and-multiply very”)
# "[EN-AID] And Israel dwelt in the land of Egypt, in the land of Goshen;
# and they took holding in it, and were fruitful, and multiplied greatly."
m.step("Gen.47.27")
# ‹וַיֵּאָחֲזוּ בָהּ וַיִּפְרוּ› (“and-seize in-her/its and-be-fruitful”)
# ‹וַיִּרְבּוּ מְאֹד› (“and-multiply very”)
# — fact holds: and-be-fruitful-and-multiply-very
m.fact("va_yifru_va_yirbu_meod")

# -------------------------- Gen.47.28 · SEVENTEEN_YEARS --------------------
# ‹וַיְחִי יַעֲקֹב בְּאֶרֶץ› (“and-live Jacob in-earth”)
# ‹מִצְרַיִם שְׁבַע עֶשְׂרֵה› (“Egypt seven -teen”)
# ‹שָׁנָה וַיְהִי יְמֵי־יַעֲקֹב› (“years and-be day Jacob”)
# ‹שְׁנֵי חַיָּיו שֶׁבַע› (“years alive-him/its seven”)
# ‹שָׁנִים וְאַרְבָּעִים וּמְאַת› (“years and-forty and-hundred”)
# ‹שָׁנָה› (“years”)
# "[EN-AID] And Jacob lived in the land of Egypt seventeen years; and the
# days of Jacob, the years of his life, were seven years and forty and a
# hundred years."
m.step("Gen.47.28")
# ‹וַיְחִי יַעֲקֹב בְּאֶרֶץ› (“and-live Jacob in-earth”)
# ‹מִצְרַיִם שְׁבַע עֶשְׂרֵה› (“Egypt seven -teen”)
# ‹שָׁנָה› (“years”)
# — fact holds: day-Jacob-seven-forty-and-hundred-years
m.fact("yeme_yaaqov_sheva_arbaim_u_meat_shana")
# witness-grounded state (its own tier):
# the_approached_rule_confirmed_in_two_families on
# one_hundred_forty_seven_years
m.witness_state("one_hundred_forty_seven_years", "the_approached_rule_confirmed_in_two_families",
                cites=["Bereshit Rabbah 96:4"])
# witness-grounded state (its own tier):
# silent_in_this_layer_confirmed_in_the_fuller_one on the_closed_portion
m.witness_state("the_closed_portion", "silent_in_this_layer_confirmed_in_the_fuller_one",
                cites=["Bereshit Rabbah 96:1"])

# -------------------------- Gen.47.29 · THE_THIGH_AND_THE_BAN --------------
# ‹וַיִּקְרְבוּ יְמֵי־יִשְׂרָאֵל לָמוּת› (“and-bring-near day Israel to-
# die”)
# ‹וַיִּקְרָא לִבְנוֹ לְיוֹסֵף› (“and-call to-son-him/its to-Joseph”)
# ‹וַיֹּאמֶר לוֹ אִם־נָא› (“and-say to-him/its if please”)
# ‹מָצָאתִי חֵן בְּעֵינֶיךָ› (“find graciousness in-eye-you/your”)
# ‹שִׂים־נָא יָדְךָ תַּחַת› (“put/set please hand-you/your under”)
# ‹יְרֵכִי וְעָשִׂיתָ עִמָּדִי› (“thigh-me/my and-make along-with-me/my”)
# ‹חֶסֶד וֶאֱמֶת אַל־נָא› (“kindness and-stability do-not please”)
# ‹תִקְבְּרֵנִי בְּמִצְרָיִם› (“inter-me/my in-Egypt”)
# "[EN-AID] And the days of Israel drew near to die; and he called his son
# Joseph, and said to him: If, pray, I have found favor in your eyes, put,
# pray, your hand under my thigh, and do with me kindness and truth: do not,
# pray, bury me in Egypt."
m.step("Gen.47.29")
# ‹אַל־נָא תִקְבְּרֵנִי בְּמִצְרָיִם› (“do-not please inter-me/my in-Egypt”)
# — Israel speaks a demand — LET-NOT: over-please-tiqbreni-in-Egypt
m.declare("yisrael", "LET-NOT",
          "al_na_tiqbreni_be_mitzrayim")
# witness-tier presupposed read: the_father_becomes_a_petitioner_to_his_son
# on if_i_have_found_favor — read, not installed
m.witness_read("if_i_have_found_favor", "the_father_becomes_a_petitioner_to_his_son",
                cites=["Bereshit Rabbah 96:3", "Bereshit Rabbah 96:2"])

# -------------------------- Gen.47.30 · CARRY_ME_AND_BURY_ME ---------------
# ‹וְשָׁכַבְתִּי עִם־אֲבֹתַי וּנְשָׂאתַנִי› (“and-lie-down with father-me/my
# and-lift/carry-me/my”)
# ‹מִמִּצְרַיִם וּקְבַרְתַּנִי בִּקְבֻרָתָם› (“from-Egypt and-inter-me/my
# in-sepulture-them/their”)
# ‹וַיֹּאמַר אָנֹכִי אֶעֱשֶׂה› (“and-say make”)
# ‹כִדְבָרֶךָ› (“like-word/thing-you/your”)
# "[EN-AID] And I will lie with my fathers, and you shall carry me from
# Egypt, and bury me in their burying-place. And he said: I will do
# according to your word."
m.step("Gen.47.30")
# ‹וּנְשָׂאתַנִי מִמִּצְרַיִם וּקְבַרְתַּנִי› (“and-lift/carry-me/my from-
# Egypt and-inter-me/my”)
# ‹בִּקְבֻרָתָם› (“in-sepulture-them/their”)
# — Israel speaks a demand — LET: and-qevartani-bi-qvuratam
m.declare("yisrael", "LET",
          "u_qevartani_bi_qvuratam")
# witness-tier presupposed read: four_reasons_and_a_doctrine_of_transit on
# do_not_bury_me_in_egypt — read, not installed
m.witness_read("do_not_bury_me_in_egypt", "four_reasons_and_a_doctrine_of_transit",
                cites=["Bereshit Rabbah 96:5", "Onkelos Genesis 47:29"])

# -------------------------- Gen.47.31 · SWEAR_TO_ME ------------------------
# ‹וַיֹּאמֶר הִשָּׁבְעָה לִי› (“and-say swear-ward to-me/my”)
# ‹וַיִּשָּׁבַע לוֹ וַיִּשְׁתַּחוּ› (“and-swear to-him/its and-afflict”)
# ‹יִשְׂרָאֵל עַל־רֹאשׁ הַמִּטָּה› (“Israel over head the-bed-forsleeping”)
# "[EN-AID] And he said: Swear to me. And he swore to him. And Israel bowed
# upon the head of the bed."
m.step("Gen.47.31")
# ‹וַיֹּאמֶר הִשָּׁבְעָה לִי› (“and-say swear-ward to-me/my”)
# — Israel speaks a demand — LET: hishava-to-me
m.declare("yisrael", "LET",
          "hishava_li")
# ‹וַיִּשָּׁבַע לוֹ› (“and-swear to-him/its”)
# — demand settled (popped from the queue): hishava-to-me
m.result("hishava_li", tmark="t4")
# witness-grounded state (its own tier):
# a_translation_declining_a_move_on_offer on the_head_of_the_bed
m.witness_state("the_head_of_the_bed", "a_translation_declining_a_move_on_offer",
                cites=["Onkelos Genesis 47:31"])

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
    assert sorted(m.WORLD["witnessed"]) == ['five_men_from_the_edge', 'one_hundred_forty_seven_years', 'settled_in_the_best_of_the_land', 'the_closed_portion', 'the_head_of_the_bed']
    assert m.WORLD["witnessed"]['five_men_from_the_edge']["cites"] == ['Bereshit Rabbah 95:4']
    assert all('a_roster_decided_by_a_spelling_pattern_in_deuteronomy' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['one_hundred_forty_seven_years']["cites"] == ['Bereshit Rabbah 96:4']
    assert all('the_approached_rule_confirmed_in_two_families' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['settled_in_the_best_of_the_land']["cites"] == ['Bereshit Rabbah 86:2']
    assert all('a_decree_of_chains_executing_in_its_softened_form' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_closed_portion']["cites"] == ['Bereshit Rabbah 96:1']
    assert all('silent_in_this_layer_confirmed_in_the_fuller_one' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_head_of_the_bed']["cites"] == ['Onkelos Genesis 47:31']
    assert all('a_translation_declining_a_move_on_offer' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('we_have_come_to_sojourn', 'the_paved_way_taking_its_third_seat'), ('he_moved_the_people', 'urbanization_or_population_transfer'), ('the_fifth_is_pharaohs', 'the_blocks_one_permanent_law'), ('if_i_have_found_favor', 'the_father_becomes_a_petitioner_to_his_son'), ('do_not_bury_me_in_egypt', 'four_reasons_and_a_doctrine_of_transit')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 40:6', 'Onkelos Genesis 47:4']
    assert all('the_paved_way_taking_its_third_seat' not in f for f in m.WORLD["facts"])
    assert 'we_have_come_to_sojourn' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Onkelos Genesis 47:21']
    assert all('urbanization_or_population_transfer' not in f for f in m.WORLD["facts"])
    assert 'he_moved_the_people' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Onkelos Genesis 47:22', 'Onkelos Genesis 47:26', 'Bereshit Rabbah 90:6']
    assert all('the_blocks_one_permanent_law' not in f for f in m.WORLD["facts"])
    assert 'the_fifth_is_pharaohs' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 96:3', 'Bereshit Rabbah 96:2']
    assert all('the_father_becomes_a_petitioner_to_his_son' not in f for f in m.WORLD["facts"])
    assert 'if_i_have_found_favor' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 96:5', 'Onkelos Genesis 47:29']
    assert all('four_reasons_and_a_doctrine_of_transit' not in f for f in m.WORLD["facts"])
    assert 'do_not_bury_me_in_egypt' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
