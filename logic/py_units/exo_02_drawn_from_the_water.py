#!/usr/bin/env python3
# =============================================================================
# exo_02_drawn_from_the_water — 2:1-25
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_02_drawn_from_the_water.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Drawn from the water (2:1-25)"""
from machine import Machine

m = Machine("exo_02_drawn_from_the_water")

# -------------------------- Exod.2.1 · A_MAN_WENT --------------------------
# ‹וַיֵּלֶךְ אִישׁ מִבֵּית› (“and-go man from-house”)
# ‹לֵוִי וַיִּקַּח אֶת־בַּת־לֵוִי› (“Levi and-take obj-marker daughter
# Levi”)
# "[EN-AID] And a man went from the house of Levi, and took a daughter of
# Levi."
m.step("Exod.2.1")
# ‹וַיֵּלֶךְ אִישׁ מִבֵּית› (“and-go man from-house”)
# ‹לֵוִי› (“Levi”)
# — fact holds: man-who?-house-Levi-obj-marker-daughter-Levi
m.fact("ish_mi_bet_levi_et_bat_levi")

# -------------------------- Exod.2.2 · GOOD_AND_HIDDEN ---------------------
# ‹וַתַּהַר הָאִשָּׁה וַתֵּלֶד› (“and-be-pregnant the-woman and-bear-young”)
# ‹בֵּן וַתֵּרֶא אֹתוֹ› (“son and-see obj-marker-him/its”)
# ‹כִּי־טוֹב הוּא וַתִּצְפְּנֵהוּ› (“that good he/it and-hide-him/its”)
# ‹שְׁלֹשָׁה יְרָחִים› (“three lunation”)
# "[EN-AID] And the woman conceived, and bore a son; and she saw him, that
# he was good; and she hid him three months."
m.step("Exod.2.2")
# ‹וַתֵּרֶא אֹתוֹ כִּי־טוֹב› (“and-see obj-marker-him/its that good”)
# ‹הוּא› (“he/it”)
# — fact holds: and-see-it-that-good-he/it
m.fact("va_tere_oto_ki_tov_hu")

# -------------------------- Exod.2.3 · AN_ARK_OF_REEDS ---------------------
# ‹וְלֹא־יָכְלָה עוֹד הַצְּפִינוֹ› (“and-not be-able still/again hide-
# him/its”)
# ‹וַתִּקַּח־לוֹ תֵּבַת גֹּמֶא› (“and-take to-him/its ark absorbent”)
# ‹וַתַּחְמְרָה בַחֵמָר וּבַזָּפֶת› (“and-boil-up-her/its in-bitumen and-in-
# asphalt”)
# ‹וַתָּשֶׂם בָּהּ אֶת־הַיֶּלֶד› (“and-put/set in-her/its obj-marker the-
# child”)
# ‹וַתָּשֶׂם בַּסּוּף עַל־שְׂפַת› (“and-put/set in-reed over lip”)
# ‹הַיְאֹר› (“the-Nile”)
# "[EN-AID] And when she could no longer hide him, she took for him an ark
# of reeds, and daubed it with mortar and with pitch; and she placed the
# child in it, and placed it in the rushes by the bank of the Nile."
m.step("Exod.2.3")
# ‹וַתִּקַּח־לוֹ תֵּבַת גֹּמֶא› (“and-take to-him/its ark absorbent”)
# ‹וַתַּחְמְרָה בַחֵמָר וּבַזָּפֶת› (“and-boil-up-her/its in-bitumen and-in-
# asphalt”)
# — fact holds: ark-absorbent-over-lip-the-Nile
m.fact("tevat_gome_al_sefat_ha_yeor")

# -------------------------- Exod.2.4 · THE_SISTER_STATIONED ----------------
# ‹וַתֵּתַצַּב אֲחֹתוֹ מֵרָחֹק› (“and-place sister-him/its from-remote”)
# ‹לְדֵעָה מַה־יֵּעָשֶׂה לוֹ› (“to-know what make to-him/its”)
# "[EN-AID] And his sister stationed herself far off, to know what would be
# done to him."
m.step("Exod.2.4")
# ‹וַתֵּתַצַּב אֲחֹתוֹ מֵרָחֹק› (“and-place sister-him/its from-remote”)
# — fact holds: and-place-achoto-from-remote
m.fact("va_tetatzav_achoto_me_rachoq")
# witness-tier presupposed read: good_measure on station_afar — read, not
# installed
m.witness_read("station_afar", "good_measure",
                cites=["Mishnah Sotah 1:9"])

# -------------------------- Exod.2.5 · THE_DESCENT_THAT_CHANGED_HER_LAW ----
# ‹וַתֵּרֶד בַּת־פַּרְעֹה לִרְחֹץ› (“and-go-down daughter Pharaoh to-lave”)
# ‹עַל־הַיְאֹר וְנַעֲרֹתֶיהָ הֹלְכֹת› (“over the-Nile and-girl-her/its
# walk/go”)
# ‹עַל־יַד הַיְאֹר וַתֵּרֶא› (“over hand the-Nile and-see”)
# ‹אֶת־הַתֵּבָה בְּתוֹךְ הַסּוּף› (“obj-marker the-ark in-midst the-reed”)
# ‹וַתִּשְׁלַח אֶת־אֲמָתָהּ וַתִּקָּחֶהָ› (“and-send obj-marker maidservant-
# her/its and-take-her/its”)
# "[EN-AID] And Pharaoh's daughter went down to bathe at the Nile, and her
# maidens walked by the Nile's side; and she saw the ark among the rushes,
# and sent her maidservant, and took it."
m.step("Exod.2.5")
# ‹וַתִּשְׁלַח אֶת־אֲמָתָהּ וַתִּקָּחֶהָ› (“and-send obj-marker maidservant-
# her/its and-take-her/its”)
# — fact holds: and-send-obj-marker-amatah-and-tiqacheha
m.fact("va_tishlach_et_amatah_va_tiqacheha")

# -------------------------- Exod.2.6 · A_WEEPING_YOUTH ---------------------
# ‹וַתִּפְתַּח וַתִּרְאֵהוּ אֶת־הַיֶּלֶד› (“and-open-wide and-see-him/its
# obj-marker the-child”)
# ‹וְהִנֵּה־נַעַר בֹּכֶה וַתַּחְמֹל› (“and-behold boy weep and-commiserate”)
# ‹עָלָיו וַתֹּאמֶר מִיַּלְדֵי› (“over-him/its and-say from-child”)
# ‹הָעִבְרִים זֶה› (“the-Hebrew this”)
# "[EN-AID] And she opened it, and saw him — the child, and behold, a youth
# weeping; and she had pity on him, and said: This is one of the Hebrews'
# children."
m.step("Exod.2.6")
# ‹וַתַּחְמֹל עָלָיו› (“and-commiserate over-him/its”)
# — fact holds: and-commiserate-alav
m.fact("va_tachmol_alav")

# -------------------------- Exod.2.7 · SHALL_I_GO_AND_CALL -----------------
# ‹וַתֹּאמֶר אֲחֹתוֹ אֶל־בַּת־פַּרְעֹה› (“and-say sister-him/its to daughter
# Pharaoh”)
# ‹הַאֵלֵךְ וְקָרָאתִי לָךְ› (“the-go and-call to-you/your”)
# ‹אִשָּׁה מֵינֶקֶת מִן› (“woman suck from”)
# ‹הָעִבְרִיֹּת וְתֵינִק לָךְ› (“the-Hebrew and-suck to-you/your”)
# ‹אֶת־הַיָּלֶד› (“obj-marker the-child”)
# "[EN-AID] And his sister said to Pharaoh's daughter: Shall I go and call
# you a nursing woman of the Hebrews, that she may nurse the child for you?"
m.step("Exod.2.7")
# ‹הַאֵלֵךְ וְקָרָאתִי לָךְ› (“the-go and-call to-you/your”)
# ‹אִשָּׁה מֵינֶקֶת› (“woman suck”)
# — fact holds: the-go-and-call-suck
m.fact("ha_elekh_ve_qarati_meneqet")

# -------------------------- Exod.2.8 · GO_AND_SHE_WENT ---------------------
# ‹וַתֹּאמֶר־לָהּ בַּת־פַּרְעֹה לֵכִי› (“and-say to-her/its daughter Pharaoh
# go”)
# ‹וַתֵּלֶךְ הָעַלְמָה וַתִּקְרָא› (“and-go the-lass and-call”)
# ‹אֶת־אֵם הַיָּלֶד› (“obj-marker mother the-child”)
# "[EN-AID] And Pharaoh's daughter said to her: Go. And the maiden went, and
# called the child's mother."
m.step("Exod.2.8")
# ‹לֵכִי› (“go”)
# — daughter-Pharaoh speaks a demand — LET: go
m.declare("bat_paro", "LET",
          "lekhi")
# ‹וַתֵּלֶךְ הָעַלְמָה וַתִּקְרָא› (“and-go the-lass and-call”)
# ‹אֶת־אֵם הַיָּלֶד› (“obj-marker mother the-child”)
# — demand settled (popped from the queue): go
m.result("lekhi", tmark="t1")

# -------------------------- Exod.2.9 · NURSE_HIM_FOR_ME --------------------
# ‹וַתֹּאמֶר לָהּ בַּת־פַּרְעֹה› (“and-say to-her/its daughter Pharaoh”)
# ‹הֵילִיכִי אֶת־הַיֶּלֶד הַזֶּה› (“go obj-marker the-child the-this”)
# ‹וְהֵינִקִהוּ לִי וַאֲנִי› (“and-suck-him/its to-me/my and-I”)
# ‹אֶתֵּן אֶת־שְׂכָרֵךְ וַתִּקַּח› (“set obj-marker wage-you/your and-take”)
# ‹הָאִשָּׁה הַיֶּלֶד וַתְּנִיקֵהוּ› (“the-woman the-child and-suckle-
# him/its”)
# "[EN-AID] And Pharaoh's daughter said to her: Take this child, and nurse
# him for me, and I will give your wages. And the woman took the child, and
# nursed him."
m.step("Exod.2.9")
# ‹הֵילִיכִי אֶת־הַיֶּלֶד הַזֶּה› (“go obj-marker the-child the-this”)
# ‹וְהֵינִקִהוּ לִי› (“and-suck-him/its to-me/my”)
# — daughter-Pharaoh speaks a demand — LET: go-obj-marker-the-child-and-
# heniqihu
m.declare("bat_paro", "LET",
          "helikhi_et_ha_yeled_ve_heniqihu")
# ‹וַתִּקַּח הָאִשָּׁה הַיֶּלֶד› (“and-take the-woman the-child”)
# ‹וַתְּנִיקֵהוּ› (“and-suckle-him/its”)
# — demand settled (popped from the queue): go-obj-marker-the-child-and-
# heniqihu
m.result("helikhi_et_ha_yeled_ve_heniqihu", tmark="t2")

# -------------------------- Exod.2.10 · MOSES_NAMED ------------------------
# ‹וַיִגְדַּל הַיֶּלֶד וַתְּבִאֵהוּ› (“and-be-large the-child and-
# come/bring-him/its”)
# ‹לְבַת־פַּרְעֹה וַיְהִי־לָהּ לְבֵן› (“to-daughter Pharaoh and-be to-
# her/its to-son”)
# ‹וַתִּקְרָא שְׁמוֹ מֹשֶׁה› (“and-call name-him/its Moses”)
# ‹וַתֹּאמֶר כִּי מִן־הַמַּיִם› (“and-say that from the-waters”)
# ‹מְשִׁיתִהוּ› (“pull-out-him/its”)
# "[EN-AID] And the child grew, and she brought him to Pharaoh's daughter,
# and he became her son; and she called his name Moses, and said: For from
# the water I drew him."
m.step("Exod.2.10")
# ‹וַתִּקְרָא שְׁמוֹ מֹשֶׁה› (“and-call name-him/its Moses”)
# — named: the-child := Moses
m.name("ha_yeled", "moshe")

# -------------------------- Exod.2.11 · HE_SAW_THEIR_BURDENS ---------------
# ‹וַיְהִי בַּיָּמִים הָהֵם› (“and-be in-day the-they”)
# ‹וַיִּגְדַּל מֹשֶׁה וַיֵּצֵא› (“and-be-large Moses and-bring-forth”)
# ‹אֶל־אֶחָיו וַיַּרְא בְּסִבְלֹתָם› (“to brother-him/its and-see in-
# porterage-them/their”)
# ‹וַיַּרְא אִישׁ מִצְרִי› (“and-see man Egyptian”)
# ‹מַכֶּה אִישׁ־עִבְרִי מֵאֶחָיו› (“strike man Hebrew from-brother-him/its”)
# "[EN-AID] And it was in those days, and Moses grew, and went out to his
# brothers, and saw their burdens; and he saw an Egyptian man striking a
# Hebrew man, of his brothers."
m.step("Exod.2.11")
# ‹וַיַּרְא בְּסִבְלֹתָם› (“and-see in-porterage-them/their”)
# — fact holds: and-see-in-sivlotam
m.fact("va_yar_be_sivlotam")

# -------------------------- Exod.2.12 · HE_STRUCK_THE_EGYPTIAN -------------
# ‹וַיִּפֶן כֹּה וָכֹה› (“and-turn like-this and-like-this”)
# ‹וַיַּרְא כִּי אֵין› (“and-see that there-is-not”)
# ‹אִישׁ וַיַּךְ אֶת־הַמִּצְרִי› (“man and-strike obj-marker the-Egyptian”)
# ‹וַיִּטְמְנֵהוּ בַּחוֹל› (“and-hide-him/its in-sand”)
# "[EN-AID] And he turned this way and that way, and saw that there was no
# man; and he struck the Egyptian, and hid him in the sand."
m.step("Exod.2.12")
# ‹וַיַּךְ אֶת־הַמִּצְרִי› (“and-strike obj-marker the-Egyptian”)
# — event: hika — agent Moses
m.event("hika", agent="moshe")
# witness-tier presupposed read: the_two_moses_satellite_laws on
# strike_and_rebuke — read, not installed
m.witness_read("strike_and_rebuke", "the_two_moses_satellite_laws",
                cites=["Sanhedrin 58b:16", "Sanhedrin 58b:17", "Sanhedrin 58b:18", "Sanhedrin 58b:19", "Sanhedrin 58b:20"])

# -------------------------- Exod.2.13 · TWO_HEBREWS_STRIVING ---------------
# ‹וַיֵּצֵא בַּיּוֹם הַשֵּׁנִי› (“and-bring-forth in-day the-second”)
# ‹וְהִנֵּה שְׁנֵי־אֲנָשִׁים עִבְרִים› (“and-behold two man Hebrew”)
# ‹נִצִּים וַיֹּאמֶר לָרָשָׁע› (“go-forth and-say to-wrong”)
# ‹לָמָּה תַכֶּה רֵעֶךָ› (“to-what strike associate-you/your”)
# "[EN-AID] And he went out on the second day, and behold, two Hebrew men
# striving; and he said to the wicked one: Why do you strike your fellow?"
m.step("Exod.2.13")
# ‹וַיֹּאמֶר לָרָשָׁע לָמָּה› (“and-say to-wrong to-what”)
# ‹תַכֶּה רֵעֶךָ› (“strike associate-you/your”)
# — fact holds: lama-strike-reekha
m.fact("lama_take_reekha")

# -------------------------- Exod.2.14 · WHO_SET_YOU ------------------------
# ‹וַיֹּאמֶר מִי שָׂמְךָ› (“and-say who? put/set-you/your”)
# ‹לְאִישׁ שַׂר וְשֹׁפֵט› (“to-man officer and-judge”)
# ‹עָלֵינוּ הַלְהָרְגֵנִי אַתָּה› (“over-us/our the-to-smite-with-deadly-
# intent-me/my you”)
# ‹אֹמֵר כַּאֲשֶׁר הָרַגְתָּ› (“say like-as/which smite-with-deadly-intent”)
# ‹אֶת־הַמִּצְרִי וַיִּירָא מֹשֶׁה› (“obj-marker the-Egyptian and-fear
# Moses”)
# ‹וַיֹּאמַר אָכֵן נוֹדַע› (“and-say firmly know”)
# ‹הַדָּבָר› (“the-word/thing”)
# "[EN-AID] And he said: Who set you as a man, prince and judge over us? Do
# you say to kill me, as you killed the Egyptian? And Moses feared, and
# said: Surely the thing is known."
m.step("Exod.2.14")
# ‹אָכֵן נוֹדַע הַדָּבָר› (“firmly know the-word/thing”)
# — fact holds: firmly-know-the-word/thing
m.fact("akhen_noda_ha_davar")

# -------------------------- Exod.2.15 · PHARAOH_SEEKS_MOSES_FLEES ----------
# ‹וַיִּשְׁמַע פַּרְעֹה אֶת־הַדָּבָר› (“and-hear Pharaoh obj-marker the-
# word/thing”)
# ‹הַזֶּה וַיְבַקֵּשׁ לַהֲרֹג› (“the-this and-search-out to-smite-with-
# deadly-intent”)
# ‹אֶת־מֹשֶׁה וַיִּבְרַח מֹשֶׁה› (“obj-marker Moses and-bolt Moses”)
# ‹מִפְּנֵי פַרְעֹה וַיֵּשֶׁב› (“from-face Pharaoh and-dwell/sit”)
# ‹בְּאֶרֶץ־מִדְיָן וַיֵּשֶׁב עַל־הַבְּאֵר› (“in-earth Midian and-dwell/sit
# over the-pit”)
# "[EN-AID] And Pharaoh heard this thing, and sought to kill Moses; and
# Moses fled from before Pharaoh, and dwelt in the land of Midian, and sat
# by the well."
m.step("Exod.2.15")
# ‹וַיִּבְרַח מֹשֶׁה מִפְּנֵי› (“and-bolt Moses from-face”)
# ‹פַרְעֹה› (“Pharaoh”)
# — fact holds: and-search-out-to-smite-with-deadly-intent-obj-marker-Moses
m.fact("va_yevaqesh_la_harog_et_moshe")

# -------------------------- Exod.2.16 · SEVEN_DAUGHTERS --------------------
# ‹וּלְכֹהֵן מִדְיָן שֶׁבַע› (“and-to-priest Midian seven”)
# ‹בָּנוֹת וַתָּבֹאנָה וַתִּדְלֶנָה› (“daughter and-come/bring and-dangle”)
# ‹וַתְּמַלֶּאנָה אֶת־הָרְהָטִים לְהַשְׁקוֹת› (“and-fill obj-marker the-
# channel to-give-drink”)
# ‹צֹאן אֲבִיהֶן› (“flock father-them/their”)
# "[EN-AID] And the priest of Midian had seven daughters; and they came, and
# drew, and filled the troughs, to water their father's flock."
m.step("Exod.2.16")
# ‹וּלְכֹהֵן מִדְיָן שֶׁבַע› (“and-to-priest Midian seven”)
# ‹בָּנוֹת› (“daughter”)
# — fact holds: and-to-priest-Midian-seven-daughter
m.fact("u_le_khohen_midyan_sheva_banot")

# -------------------------- Exod.2.17 · MOSES_SAVES_AND_WATERS -------------
# ‹וַיָּבֹאוּ הָרֹעִים וַיְגָרְשׁוּם› (“and-come/bring the-graze and-drive-
# out-from-a-possession-them/their”)
# ‹וַיָּקָם מֹשֶׁה וַיּוֹשִׁעָן› (“and-arise Moses and-be-open-them/their”)
# ‹וַיַּשְׁקְ אֶת־צֹאנָם› (“and-give-drink obj-marker flock-them/their”)
# "[EN-AID] And the shepherds came and drove them off; and Moses rose, and
# saved them, and watered their flock."
m.step("Exod.2.17")
# ‹וַיָּקָם מֹשֶׁה וַיּוֹשִׁעָן› (“and-arise Moses and-be-open-them/their”)
# ‹וַיַּשְׁקְ אֶת־צֹאנָם› (“and-give-drink obj-marker flock-them/their”)
# — fact holds: and-yoshian-and-give-drink-obj-marker-tzonam
m.fact("va_yoshian_va_yashq_et_tzonam")

# -------------------------- Exod.2.18 · WHY_SO_SOON_TODAY ------------------
# ‹וַתָּבֹאנָה אֶל־רְעוּאֵל אֲבִיהֶן› (“and-come/bring to Raguel father-
# them/their”)
# ‹וַיֹּאמֶר מַדּוּעַ מִהַרְתֶּן› (“and-say what-known? hasten”)
# ‹בֹּא הַיּוֹם› (“come/bring the-day”)
# "[EN-AID] And they came to Reuel their father; and he said: Why have you
# hurried to come today?"
m.step("Exod.2.18")
# ‹וַיֹּאמֶר מַדּוּעַ מִהַרְתֶּן› (“and-say what-known? hasten”)
# ‹בֹּא הַיּוֹם› (“come/bring the-day”)
# — fact holds: what-known?-hasten-come/bring-the-day
m.fact("madua_miharten_bo_ha_yom")

# -------------------------- Exod.2.19 · AN_EGYPTIAN_MAN_DELIVERED_US -------
# ‹וַתֹּאמַרְןָ אִישׁ מִצְרִי› (“and-say man Egyptian”)
# ‹הִצִּילָנוּ מִיַּד הָרֹעִים› (“snatch-away-us/our from-hand the-graze”)
# ‹וְגַם־דָּלֹה דָלָה לָנוּ› (“and-also dangle dangle to-us/our”)
# ‹וַיַּשְׁקְ אֶת־הַצֹּאן› (“and-give-drink obj-marker the-flock”)
# "[EN-AID] And they said: An Egyptian man delivered us from the hand of the
# shepherds; and he also surely drew for us, and watered the flock."
m.step("Exod.2.19")
# ‹אִישׁ מִצְרִי הִצִּילָנוּ› (“man Egyptian snatch-away-us/our”)
# ‹מִיַּד הָרֹעִים› (“from-hand the-graze”)
# — fact holds: man-Egyptian-hitzilanu
m.fact("ish_mitzri_hitzilanu")

# -------------------------- Exod.2.20 · CALL_HIM_TO_EAT_BREAD --------------
# ‹וַיֹּאמֶר אֶל־בְּנֹתָיו וְאַיּוֹ› (“and-say to daughter-him/its and-
# where?-him/its”)
# ‹לָמָּה זֶּה עֲזַבְתֶּן› (“to-what this loosen”)
# ‹אֶת־הָאִישׁ קִרְאֶן לוֹ› (“obj-marker the-man call to-him/its”)
# ‹וְיֹאכַל לָחֶם› (“and-eat food”)
# "[EN-AID] And he said to his daughters: And where is he? Why is it that
# you left the man? Call him, and let him eat bread."
m.step("Exod.2.20")
# ‹קִרְאֶן לוֹ וְיֹאכַל› (“call to-him/its and-eat”)
# ‹לָחֶם› (“food”)
# — Raguel speaks a demand — LET: call-not-and-eat-food
m.declare("reuel", "LET",
          "qiren_lo_ve_yokhal_lachem")

# -------------------------- Exod.2.21 · MOSES_CONSENTS_ZIPPORAH_GIVEN ------
# ‹וַיּוֹאֶל מֹשֶׁה לָשֶׁבֶת› (“and-yield Moses to-dwell/sit”)
# ‹אֶת־הָאִישׁ וַיִּתֵּן אֶת־צִפֹּרָה› (“with the-man and-set obj-marker
# Zipporah”)
# ‹בִתּוֹ לְמֹשֶׁה› (“daughter-him/its to-Moses”)
# "[EN-AID] And Moses consented to dwell with the man; and he gave Zipporah
# his daughter to Moses."
m.step("Exod.2.21")
# ‹וַיּוֹאֶל מֹשֶׁה לָשֶׁבֶת› (“and-yield Moses to-dwell/sit”)
# ‹אֶת־הָאִישׁ› (“with the-man”)
# — demand settled (popped from the queue): call-not-and-eat-food
m.result("qiren_lo_ve_yokhal_lachem", tmark="t3")

# -------------------------- Exod.2.22 · GERSHOM_NAMED ----------------------
# ‹וַתֵּלֶד בֵּן וַיִּקְרָא› (“and-bear-young son and-call”)
# ‹אֶת־שְׁמוֹ גֵּרְשֹׁם כִּי› (“obj-marker name-him/its Gershom that”)
# ‹אָמַר גֵּר הָיִיתִי› (“say sojourner be”)
# ‹בְּאֶרֶץ נָכְרִיָּה› (“in-earth strange”)
# "[EN-AID] And she bore a son, and he called his name Gershom; for he said:
# A stranger have I been in a foreign land."
m.step("Exod.2.22")
# ‹וַיִּקְרָא אֶת־שְׁמוֹ גֵּרְשֹׁם› (“and-call obj-marker name-him/its
# Gershom”)
# — named: son-Moses := Gershom
m.name("ben_moshe", "gershom")

# -------------------------- Exod.2.23 · THE_KING_DIES_THE_CRY_GOES_UP ------
# ‹וַיְהִי בַיָּמִים הָרַבִּים› (“and-be in-day the-many/great”)
# ‹הָהֵם וַיָּמָת מֶלֶךְ› (“the-they and-die king”)
# ‹מִצְרַיִם וַיֵּאָנְחוּ בְנֵי־יִשְׂרָאֵל› (“Egypt and-sigh son Israel”)
# ‹מִן־הָעֲבֹדָה וַיִּזְעָקוּ וַתַּעַל› (“from the-service/work and-shriek
# and-go-up”)
# ‹שַׁוְעָתָם אֶל־הָאֱלֹהִים מִן־הָעֲבֹדָה› (“hallooing-them/their to the-
# God from the-service/work”)
# "[EN-AID] And it was in those many days, and the king of Egypt died; and
# the sons of Israel groaned from the service, and cried out; and their
# outcry went up to God from the service."
m.step("Exod.2.23")
# ‹וַיָּמָת מֶלֶךְ מִצְרַיִם› (“and-die king Egypt”)
# — event: met — agent king-Egypt
m.event("met", agent="melekh_mitzrayim")

# -------------------------- Exod.2.24 · GOD_REMEMBERED_THE_COVENANT --------
# ‹וַיִּשְׁמַע אֱלֹהִים אֶת־נַאֲקָתָם› (“and-hear God obj-marker groan-
# them/their”)
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־בְּרִיתוֹ› (“and-mark God obj-marker covenant-
# him/its”)
# ‹אֶת־אַבְרָהָם אֶת־יִצְחָק וְאֶת־יַעֲקֹב› (“with Abraham with Isaac and-
# with Jacob”)
# "[EN-AID] And God heard their groaning; and God remembered His covenant
# with Abraham, with Isaac, and with Jacob."
m.step("Exod.2.24")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־בְּרִיתוֹ› (“and-mark God obj-marker covenant-
# him/its”)
# — fact holds: and-mark-God-obj-marker-brito
m.fact("va_yizkor_elohim_et_brito")

# -------------------------- Exod.2.25 · AND_GOD_KNEW -----------------------
# ‹וַיַּרְא אֱלֹהִים אֶת־בְּנֵי› (“and-see God obj-marker son”)
# ‹יִשְׂרָאֵל וַיֵּדַע אֱלֹהִים› (“Israel and-know God”)
# "[EN-AID] And God saw the sons of Israel; and God knew."
m.step("Exod.2.25")
# ‹וַיֵּדַע אֱלֹהִים› (“and-know God”)
# — fact holds: and-know-God
m.fact("va_yeda_elohim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha_yeled': 'moshe', 'ben_moshe': 'gershom'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['ish_mi_bet_levi_et_bat_levi', 'va_tere_oto_ki_tov_hu', 'tevat_gome_al_sefat_ha_yeor', 'va_tetatzav_achoto_me_rachoq', 'va_tishlach_et_amatah_va_tiqacheha', 'va_tachmol_alav', 'ha_elekh_ve_qarati_meneqet', 'va_yar_be_sivlotam', 'lama_take_reekha', 'akhen_noda_ha_davar', 'va_yevaqesh_la_harog_et_moshe', 'u_le_khohen_midyan_sheva_banot', 'va_yoshian_va_yashq_et_tzonam', 'madua_miharten_bo_ha_yom', 'ish_mitzri_hitzilanu', 'va_yizkor_elohim_et_brito', 'va_yeda_elohim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('station_afar', 'good_measure'), ('strike_and_rebuke', 'the_two_moses_satellite_laws')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Sotah 1:9']
    assert all('good_measure' not in f for f in m.WORLD["facts"])
    assert 'station_afar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sanhedrin 58b:16', 'Sanhedrin 58b:17', 'Sanhedrin 58b:18', 'Sanhedrin 58b:19', 'Sanhedrin 58b:20']
    assert all('the_two_moses_satellite_laws' not in f for f in m.WORLD["facts"])
    assert 'strike_and_rebuke' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
