#!/usr/bin/env python3
# =============================================================================
# gen_68_i_am_yosef — 45:1-28
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_68_i_am_yosef.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""I am Joseph: the unmasking (45:1-28)"""
from machine import Machine

m = Machine("gen_68_i_am_yosef")

# -------------------------- Gen.45.1 · SEND_EVERY_MAN_OUT ------------------
# ‹וְלֹא־יָכֹל יוֹסֵף לְהִתְאַפֵּק› (“and-not be-able Joseph to-contain”)
# ‹לְכֹל הַנִּצָּבִים עָלָיו› (“to-all the-station over-him/its”)
# ‹וַיִּקְרָא הוֹצִיאוּ כָל־אִישׁ› (“and-call bring-forth all man”)
# ‹מֵעָלָי וְלֹא־עָמַד אִישׁ› (“from-over-me/my and-not stand man”)
# ‹אִתּוֹ בְּהִתְוַדַּע יוֹסֵף› (“with-him/its in-know Joseph”)
# ‹אֶל־אֶחָיו› (“to brother-him/its”)
# "[EN-AID] And Joseph could not restrain himself before all who stood by
# him, and he called: Send every man out from me! And no man stood with him
# when Joseph made himself known to his brothers."
m.step("Gen.45.1")
# ‹הוֹצִיאוּ כָל־אִישׁ מֵעָלָי› (“bring-forth all man from-over-me/my”)
# — Joseph speaks a demand — LET: bring-forth-all-man-mealai
m.declare("yosef", "LET",
          "hotziu_khol_ish_mealai")
# ‹וְלֹא־עָמַד אִישׁ אִתּוֹ› (“and-not stand man with-him/its”)
# — demand settled (popped from the queue): bring-forth-all-man-mealai
m.result("hotziu_khol_ish_mealai", tmark="t1")
# witness-tier presupposed read: the_speech_of_gen_67_completing_here on
# he_could_not_restrain_himself — read, not installed
m.witness_read("he_could_not_restrain_himself", "the_speech_of_gen_67_completing_here",
                cites=["Bereshit Rabbah 93:9", "Bereshit Rabbah 93:8"])

# -------------------------- Gen.45.2 · THE_VOICE_IN_WEEPING ----------------
# ‹וַיִּתֵּן אֶת־קֹלוֹ בִּבְכִי› (“and-set obj-marker voice/sound-him/its
# in-weeping”)
# ‹וַיִּשְׁמְעוּ מִצְרַיִם וַיִּשְׁמַע› (“and-hear Egyptian and-hear”)
# ‹בֵּית פַּרְעֹה› (“house Pharaoh”)
# "[EN-AID] And he gave his voice in weeping; and Egypt heard, and the house
# of Pharaoh heard."
m.step("Gen.45.2")
# ‹וַיִּתֵּן אֶת־קֹלוֹ בִּבְכִי› (“and-set obj-marker voice/sound-him/its
# in-weeping”)
# — event: weep — agent Joseph
m.event("bakha", agent="yosef")

# -------------------------- Gen.45.3 · I_AM_JOSEPH -------------------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו› (“and-say Joseph to brother-him/its”)
# ‹אֲנִי יוֹסֵף הַעוֹד› (“Joseph the-still/again”)
# ‹אָבִי חָי וְלֹא־יָכְלוּ› (“father-me/my living and-not be-able”)
# ‹אֶחָיו לַעֲנוֹת אֹתוֹ› (“brother-him/its to-eye obj-marker-him/its”)
# ‹כִּי נִבְהֲלוּ מִפָּנָיו› (“that tremble-inwardly from-face-him/its”)
# "[EN-AID] And Joseph said to his brothers: I am Joseph! Is my father yet
# alive? And his brothers could not answer him, for they were terrified
# before his face."
m.step("Gen.45.3")
# ‹אֲנִי יוֹסֵף הַעוֹד› (“Joseph the-still/again”)
# ‹אָבִי חָי› (“father-me/my living”)
# — fact holds: ani-Joseph-the-still/again-avi-living
m.fact("ani_yosef_ha_od_avi_chai")
# witness-tier presupposed read:
# one_inference_stated_twice_by_two_authorities on
# his_brothers_could_not_answer_him — read, not installed
m.witness_read("his_brothers_could_not_answer_him", "one_inference_stated_twice_by_two_authorities",
                cites=["Bereshit Rabbah 93:10", "Bereshit Rabbah 93:11", "Bereshit Rabbah 93:2"])

# -------------------------- Gen.45.4 · DRAW_NEAR_TO_ME ---------------------
# ‹וַיֹּאמֶר יוֹסֵף אֶל־אֶחָיו› (“and-say Joseph to brother-him/its”)
# ‹גְּשׁוּ־נָא אֵלַי וַיִּגָּשׁוּ› (“be please to-me/my and-be”)
# ‹וַיֹּאמֶר אֲנִי יוֹסֵף› (“and-say Joseph”)
# ‹אֲחִיכֶם אֲשֶׁר־מְכַרְתֶּם אֹתִי› (“brother-you/your(pl) which sell obj-
# marker-me/my”)
# ‹מִצְרָיְמָה› (“Egypt-ward”)
# "[EN-AID] And Joseph said to his brothers: Draw near to me. And they drew
# near. And he said: I am Joseph your brother, whom you sold into Egypt."
m.step("Gen.45.4")
# ‹גְּשׁוּ־נָא אֵלַי› (“be please to-me/my”)
# — Joseph speaks a demand — LET: be-please-elai
m.declare("yosef", "LET",
          "geshu_na_elai")
# ‹וַיִּגָּשׁוּ› (“and-be”)
# — demand settled (popped from the queue): be-please-elai
m.result("geshu_na_elai", tmark="t2")
# witness-tier presupposed read: the_body_entered_as_evidence on
# come_near_to_me — read, not installed
m.witness_read("come_near_to_me", "the_body_entered_as_evidence",
                cites=["Bereshit Rabbah 93:10"])

# -------------------------- Gen.45.5 · LET_IT_NOT_BURN ---------------------
# ‹וְעַתָּה אַל־תֵּעָצְבוּ וְאַל־יִחַר› (“and-now do-not carve and-do-not
# glow”)
# ‹בְּעֵינֵיכֶם כִּי־מְכַרְתֶּם אֹתִי› (“in-eye-you/your(pl) that sell obj-
# marker-me/my”)
# ‹הֵנָּה כִּי לְמִחְיָה› (“hither that to-preservation-of-life”)
# ‹שְׁלָחַנִי אֱלֹהִים לִפְנֵיכֶם› (“send-me/my God to-face-you/your(pl)”)
# "[EN-AID] And now, do not be grieved, and let it not burn in your eyes
# that you sold me here — for God sent me before you for the preservation of
# life."
m.step("Gen.45.5")
# ‹אַל־תֵּעָצְבוּ וְאַל־יִחַר› (“do-not carve and-do-not glow”)
# — fact holds: over-carve-and-over-glow
m.fact("al_teatzvu_ve_al_yichar")

# -------------------------- Gen.45.6 · NO_PLOWING_NO_HARVEST ---------------
# ‹כִּי־זֶה שְׁנָתַיִם הָרָעָב› (“that this years the-hunger”)
# ‹בְּקֶרֶב הָאָרֶץ וְעוֹד› (“in-nearest-part the-earth and-still/again”)
# ‹חָמֵשׁ שָׁנִים אֲשֶׁר› (“five years which”)
# ‹אֵין־חָרִישׁ וְקָצִּיר› (“there-is-not ploughing and-severed”)
# "[EN-AID] For these two years the famine has been in the midst of the
# land, and there are yet five years in which there will be no plowing and
# harvest."
m.step("Gen.45.6")
# ‹אֲשֶׁר אֵין־חָרִישׁ וְקָצִּיר› (“which there-is-not ploughing and-
# severed”)
# — fact holds: still/again-five-years-there-is-not-ploughing-and-severed
m.fact("od_chamesh_shanim_en_charish_ve_qatzir")

# -------------------------- Gen.45.7 · A_REMNANT_IN_THE_EARTH --------------
# ‹וַיִּשְׁלָחֵנִי אֱלֹהִים לִפְנֵיכֶם› (“and-send-me/my God to-face-
# you/your(pl)”)
# ‹לָשׂוּם לָכֶם שְׁאֵרִית› (“to-put/set to-you/your(pl) remainder”)
# ‹בָּאָרֶץ וּלְהַחֲיוֹת לָכֶם› (“in-earth and-to-live to-you/your(pl)”)
# ‹לִפְלֵיטָה גְּדֹלָה› (“to-deliverance great”)
# "[EN-AID] And God sent me before you to set for you a remnant in the
# earth, and to keep alive for you a great deliverance."
m.step("Gen.45.7")
# ‹לָשׂוּם לָכֶם שְׁאֵרִית› (“to-put/set to-you/your(pl) remainder”)
# ‹בָּאָרֶץ› (“in-earth”)
# — fact holds: to-put/set-lakhem-remainder-in-the-earth
m.fact("la_sum_lakhem_sheerit_ba_aretz")

# -------------------------- Gen.45.8 · NOT_YOU_BUT_GOD ---------------------
# ‹וְעַתָּה לֹא־אַתֶּם שְׁלַחְתֶּם› (“and-now not you send”)
# ‹אֹתִי הֵנָּה כִּי› (“obj-marker-me/my hither that”)
# ‹הָאֱלֹהִים וַיְשִׂימֵנִי לְאָב› (“the-God and-put/set-me/my to-father”)
# ‹לְפַרְעֹה וּלְאָדוֹן לְכָל־בֵּיתוֹ› (“to-Pharaoh and-to-lord to-all
# house-him/its”)
# ‹וּמֹשֵׁל בְּכָל־אֶרֶץ מִצְרָיִם› (“and-rule in-all earth Egypt”)
# "[EN-AID] And now — it was not you who sent me here, but God; and He has
# set me as a father to Pharaoh, and as lord to all his house, and ruler
# over all the land of Egypt."
m.step("Gen.45.8")
# ‹וְעַתָּה לֹא־אַתֶּם שְׁלַחְתֶּם› (“and-now not you send”)
# ‹אֹתִי הֵנָּה כִּי› (“obj-marker-me/my hither that”)
# ‹הָאֱלֹהִים› (“the-God”)
# — fact holds: not-you-send-that-the-God
m.fact("lo_atem_shelachtem_ki_ha_Elohim")

# -------------------------- Gen.45.9 · HURRY_GO_UP_TO_MY_FATHER ------------
# ‹מַהֲרוּ וַעֲלוּ אֶל־אָבִי› (“hasten and-go-up to father-me/my”)
# ‹וַאֲמַרְתֶּם אֵלָיו כֹּה› (“and-say to-him/its like-this”)
# ‹אָמַר בִּנְךָ יוֹסֵף› (“say son-you/your Joseph”)
# ‹שָׂמַנִי אֱלֹהִים לְאָדוֹן› (“put/set-me/my God to-lord”)
# ‹לְכָל־מִצְרָיִם רְדָה אֵלַי› (“to-all Egypt go-down-ward to-me/my”)
# ‹אַל־תַּעֲמֹד› (“do-not stand”)
# "[EN-AID] Hurry, and go up to my father, and say to him: Thus says your
# son Joseph: God has set me as lord of all Egypt; come down to me, do not
# stand still."
m.step("Gen.45.9")
# ‹מַהֲרוּ וַעֲלוּ אֶל־אָבִי› (“hasten and-go-up to father-me/my”)
# — Joseph speaks a demand — LET: hasten-and-go-up-to-avi
m.declare("yosef", "LET",
          "maharu_va_alu_el_avi")

# -------------------------- Gen.45.10 · GOSHEN_NEAR_ME ---------------------
# ‹וְיָשַׁבְתָּ בְאֶרֶץ־גֹּשֶׁן וְהָיִיתָ› (“and-dwell/sit in-earth Goshen
# and-be”)
# ‹קָרוֹב אֵלַי אַתָּה› (“near to-me/my you”)
# ‹וּבָנֶיךָ וּבְנֵי בָנֶיךָ› (“and-son-you/your and-son son-you/your”)
# ‹וְצֹאנְךָ וּבְקָרְךָ וְכָל־אֲשֶׁר־לָךְ› (“and-flock-you/your and-herd-
# you/your and-all which to-you/your”)
# "[EN-AID] And you shall dwell in the land of Goshen, and you shall be near
# to me — you, and your sons, and your sons' sons, and your flocks, and your
# herds, and all that is yours."
m.step("Gen.45.10")
# ‹וְיָשַׁבְתָּ בְאֶרֶץ־גֹּשֶׁן› (“and-dwell/sit in-earth Goshen”)
# — fact holds: and-dwell/sit-in-earth-Goshen
m.fact("ve_yashavta_be_eretz_goshen")

# -------------------------- Gen.45.11 · I_WILL_SUSTAIN_YOU -----------------
# ‹וְכִלְכַּלְתִּי אֹתְךָ שָׁם› (“and-keep-in obj-marker-you/your there”)
# ‹כִּי־עוֹד חָמֵשׁ שָׁנִים› (“that still/again five years”)
# ‹רָעָב פֶּן־תִּוָּרֵשׁ אַתָּה› (“hunger lest possess/inherit you”)
# ‹וּבֵיתְךָ וְכָל־אֲשֶׁר־לָךְ› (“and-house-you/your and-all which to-
# you/your”)
# "[EN-AID] And I will sustain you there — for there are yet five years of
# famine — lest you be impoverished, you, and your household, and all that
# is yours."
m.step("Gen.45.11")
# ‹וְכִלְכַּלְתִּי אֹתְךָ שָׁם› (“and-keep-in obj-marker-you/your there”)
# — fact holds: and-keep-in-otkha-lest-possess/inherit
m.fact("ve_khilkalti_otkha_pen_tivaresh")

# -------------------------- Gen.45.12 · YOUR_EYES_SEE ----------------------
# ‹וְהִנֵּה עֵינֵיכֶם רֹאוֹת› (“and-behold eye-you/your(pl) see”)
# ‹וְעֵינֵי אָחִי בִנְיָמִין› (“and-eye brother-me/my Benjamin”)
# ‹כִּי־פִי הַמְדַבֵּר אֲלֵיכֶם› (“that mouth-me/my the-speak to-
# you/your(pl)”)
# "[EN-AID] And behold, your eyes see, and the eyes of my brother Benjamin,
# that it is my mouth that speaks to you."
m.step("Gen.45.12")
# ‹וְהִנֵּה עֵינֵיכֶם רֹאוֹת› (“and-behold eye-you/your(pl) see”)
# ‹וְעֵינֵי אָחִי בִנְיָמִין› (“and-eye brother-me/my Benjamin”)
# — fact holds: enekhem-see-and-eye-my-brother-Benjamin
m.fact("enekhem_root_ve_ene_achi_vinyamin")
# witness-tier presupposed read: the_language_itself_as_credential on
# my_mouth_speaking_to_you — read, not installed
m.witness_read("my_mouth_speaking_to_you", "the_language_itself_as_credential",
                cites=["Bereshit Rabbah 93:10", "Onkelos Genesis 45:12"])

# -------------------------- Gen.45.13 · TELL_AND_BRING_DOWN ----------------
# ‹וְהִגַּדְתֶּם לְאָבִי אֶת־כָּל־כְּבוֹדִי› (“and-tell to-father-me/my obj-
# marker all weight-me/my”)
# ‹בְּמִצְרַיִם וְאֵת כָּל־אֲשֶׁר› (“in-Egypt and-obj-marker all which”)
# ‹רְאִיתֶם וּמִהַרְתֶּם וְהוֹרַדְתֶּם› (“see and-hasten and-go-down”)
# ‹אֶת־אָבִי הֵנָּה› (“obj-marker father-me/my hither”)
# "[EN-AID] And you shall tell my father all my honor in Egypt, and all that
# you have seen; and you shall hurry and bring my father down here."
m.step("Gen.45.13")
# ‹וּמִהַרְתֶּם וְהוֹרַדְתֶּם אֶת־אָבִי› (“and-hasten and-go-down obj-marker
# father-me/my”)
# ‹הֵנָּה› (“hither”)
# — fact holds: and-tell-and-go-down-obj-marker-avi
m.fact("ve_higadtem_ve_horadtem_et_avi")

# -------------------------- Gen.45.14 · ON_BENJAMINS_NECK ------------------
# ‹וַיִּפֹּל עַל־צַוְּארֵי בִנְיָמִן־אָחִיו› (“and-fall over back-of-the-
# neck Benjamin brother-him/its”)
# ‹וַיֵּבְךְּ וּבִנְיָמִן בָּכָה› (“and-weep and-Benjamin weep”)
# ‹עַל־צַוָּארָיו› (“over back-of-the-neck-him/its”)
# "[EN-AID] And he fell on the neck of Benjamin his brother and wept; and
# Benjamin wept on his neck."
m.step("Gen.45.14")
# ‹וַיִּפֹּל עַל־צַוְּארֵי בִנְיָמִן־אָחִיו› (“and-fall over back-of-the-
# neck Benjamin brother-him/its”)
# ‹וַיֵּבְךְּ› (“and-weep”)
# — event: weep — agent Joseph-and-Benjamin
m.event("bakha", agent="yosef_u_vinyamin")
# witness-grounded state (its own tier):
# a_form_that_stands_once_in_the_torah on the_necks_written_plural
m.witness_state("the_necks_written_plural", "a_form_that_stands_once_in_the_torah",
                cites=["Bereshit Rabbah 93:12"])

# -------------------------- Gen.45.15 · THE_SPEECH_HEALED ------------------
# ‹וַיְנַשֵּׁק לְכָל־אֶחָיו וַיֵּבְךְּ› (“and-kiss to-all brother-him/its
# and-weep”)
# ‹עֲלֵיהֶם וְאַחֲרֵי כֵן› (“over-them/their and-after so”)
# ‹דִּבְּרוּ אֶחָיו אִתּוֹ› (“speak brother-him/its with-him/its”)
# "[EN-AID] And he kissed all his brothers, and wept upon them; and after
# that his brothers spoke with him."
m.step("Gen.45.15")
# ‹וְאַחֲרֵי כֵן דִּבְּרוּ› (“and-after so speak”)
# ‹אֶחָיו אִתּוֹ› (“brother-him/its with-him/its”)
# — fact holds: and-after-so-speak-echav-with-him
m.fact("ve_achare_khen_dibru_echav_ito")

# -------------------------- Gen.45.16 · THE_LEAN_VOICE_IN_PHARAOHS_HOUSE ---
# ‹וְהַקֹּל נִשְׁמַע בֵּית› (“and-the-voice/sound hear house”)
# ‹פַּרְעֹה לֵאמֹר בָּאוּ› (“Pharaoh to-say come/bring”)
# ‹אֲחֵי יוֹסֵף וַיִּיטַב› (“brother Joseph and-be-make-well”)
# ‹בְּעֵינֵי פַרְעֹה וּבְעֵינֵי› (“in-eye Pharaoh and-in-eye”)
# ‹עֲבָדָיו› (“servant-him/its”)
# "[EN-AID] And the voice was heard in Pharaoh's house, saying: Joseph's
# brothers have come. And it was good in the eyes of Pharaoh and in the eyes
# of his servants."
m.step("Gen.45.16")
# ‹וְהַקֹּל נִשְׁמַע בֵּית› (“and-the-voice/sound hear house”)
# ‹פַּרְעֹה› (“Pharaoh”)
# — fact holds: and-the-voice/sound-hear-house-Pharaoh
m.fact("ve_ha_qol_nishma_bet_paro")
# witness-tier presupposed read: a_seat_predicted_four_chapters_early on
# the_news_heard_in_pharaohs_house — read, not installed
m.witness_read("the_news_heard_in_pharaohs_house", "a_seat_predicted_four_chapters_early",
                cites=["Bereshit Rabbah 94:1", "Bereshit Rabbah 90:1"])

# -------------------------- Gen.45.17 · LOAD_AND_GO ------------------------
# ‹וַיֹּאמֶר פַּרְעֹה אֶל־יוֹסֵף› (“and-say Pharaoh to Joseph”)
# ‹אֱמֹר אֶל־אַחֶיךָ זֹאת› (“say to brother-you/your this”)
# ‹עֲשׂוּ טַעֲנוּ אֶת־בְּעִירְכֶם› (“make load-a-beast obj-marker cattle-
# you/your(pl)”)
# ‹וּלְכוּ־בֹאוּ אַרְצָה כְּנָעַן› (“and-go come/bring earth-ward Canaan”)
# "[EN-AID] And Pharaoh said to Joseph: Say to your brothers: This do — load
# your beasts, and go, come to the land of Canaan."
m.step("Gen.45.17")
# ‹זֹאת עֲשׂוּ טַעֲנוּ› (“this make load-a-beast”)
# — fact holds: this-make-load-a-beast-obj-marker-beirkhem
m.fact("zot_asu_taanu_et_beirkhem")

# -------------------------- Gen.45.18 · COME_TO_ME -------------------------
# ‹וּקְחוּ אֶת־אֲבִיכֶם וְאֶת־בָּתֵּיכֶם› (“and-take obj-marker father-
# you/your(pl) and-obj-marker house-you/your(pl)”)
# ‹וּבֹאוּ אֵלָי וְאֶתְּנָה› (“and-come/bring to-me/my and-set”)
# ‹לָכֶם אֶת־טוּב אֶרֶץ› (“to-you/your(pl) obj-marker good earth”)
# ‹מִצְרַיִם וְאִכְלוּ אֶת־חֵלֶב› (“Egypt and-eat obj-marker fat”)
# ‹הָאָרֶץ› (“the-earth”)
# "[EN-AID] And take your father and your households, and come to me; and I
# will give you the good of the land of Egypt, and eat the fat of the land."
m.step("Gen.45.18")
# ‹וּקְחוּ אֶת־אֲבִיכֶם וְאֶת־בָּתֵּיכֶם› (“and-take obj-marker father-
# you/your(pl) and-obj-marker house-you/your(pl)”)
# ‹וּבֹאוּ אֵלָי› (“and-come/bring to-me/my”)
# — Pharaoh speaks a demand — LET: and-qchu-obj-marker-avikhem-and-
# come/bring-elai
m.declare("paro", "LET",
          "u_qchu_et_avikhem_u_vou_elai")

# -------------------------- Gen.45.19 · WAGONS_FOR_THE_LITTLE_ONES ---------
# ‹וְאַתָּה צֻוֵּיתָה זֹאת› (“and-you command this”)
# ‹עֲשׂוּ קְחוּ־לָכֶם מֵאֶרֶץ› (“make take to-you/your(pl) from-earth”)
# ‹מִצְרַיִם עֲגָלוֹת לְטַפְּכֶם› (“Egypt something-revolving to-family-
# you/your(pl)”)
# ‹וְלִנְשֵׁיכֶם וּנְשָׂאתֶם אֶת־אֲבִיכֶם› (“and-to-woman-you/your(pl) and-
# lift/carry obj-marker father-you/your(pl)”)
# ‹וּבָאתֶם› (“and-come/bring”)
# "[EN-AID] And you are commanded: this do — take for yourselves from the
# land of Egypt wagons for your little ones and for your wives; and carry
# your father, and come."
m.step("Gen.45.19")
# ‹קְחוּ־לָכֶם מֵאֶרֶץ מִצְרַיִם› (“take to-you/your(pl) from-earth Egypt”)
# ‹עֲגָלוֹת› (“something-revolving”)
# — Pharaoh speaks a demand — LET: take-lakhem-something-revolving
m.declare("paro", "LET",
          "qechu_lakhem_agalot")

# -------------------------- Gen.45.20 · LET_YOUR_EYE_NOT_SPARE -------------
# ‹וְעֵינְכֶם אַל־תָּחֹס עַל־כְּלֵיכֶם› (“and-eye-you/your(pl) do-not cover
# over vessel-you/your(pl)”)
# ‹כִּי־טוּב כָּל־אֶרֶץ מִצְרַיִם› (“that good all earth Egypt”)
# ‹לָכֶם הוּא› (“to-you/your(pl) he/it”)
# "[EN-AID] And let your eye not spare your vessels — for the good of all
# the land of Egypt, yours it is."
m.step("Gen.45.20")
# ‹וְעֵינְכֶם אַל־תָּחֹס› (“and-eye-you/your(pl) do-not cover”)
# — fact holds: and-enkhem-over-cover
m.fact("ve_enkhem_al_tachos")

# -------------------------- Gen.45.21 · THE_WAGONS_GIVEN -------------------
# ‹וַיַּעֲשׂוּ־כֵן בְּנֵי יִשְׂרָאֵל› (“and-make so son Israel”)
# ‹וַיִּתֵּן לָהֶם יוֹסֵף› (“and-set to-them/their Joseph”)
# ‹עֲגָלוֹת עַל־פִּי פַרְעֹה› (“something-revolving over mouth Pharaoh”)
# ‹וַיִּתֵּן לָהֶם צֵדָה› (“and-set to-them/their food”)
# ‹לַדָּרֶךְ› (“to-way/road”)
# "[EN-AID] And the sons of Israel did so; and Joseph gave them wagons
# according to the mouth of Pharaoh, and gave them provisions for the way."
m.step("Gen.45.21")
# ‹וַיַּעֲשׂוּ־כֵן בְּנֵי יִשְׂרָאֵל› (“and-make so son Israel”)
# — demand settled (popped from the queue): take-lakhem-something-revolving
m.result("qechu_lakhem_agalot", tmark="t3")

# -------------------------- Gen.45.22 · FIVE_CHANGES_FOR_BENJAMIN ----------
# ‹לְכֻלָּם נָתַן לָאִישׁ› (“to-all-them/their set to-man”)
# ‹חֲלִפוֹת שְׂמָלֹת וּלְבִנְיָמִן› (“alternation dress and-to-Benjamin”)
# ‹נָתַן שְׁלֹשׁ מֵאוֹת› (“set three hundred”)
# ‹כֶּסֶף וְחָמֵשׁ חֲלִפֹת› (“silver and-five alternation”)
# ‹שְׂמָלֹת› (“dress”)
# "[EN-AID] To all of them he gave, to each man, changes of garments; and to
# Benjamin he gave three hundred pieces of silver, and five changes of
# garments."
m.step("Gen.45.22")
# ‹לְכֻלָּם נָתַן לָאִישׁ› (“to-all-them/their set to-man”)
# ‹חֲלִפוֹת שְׂמָלֹת› (“alternation dress”)
# — fact holds: alternation-dress-and-to-Benjamin-five
m.fact("chalifot_semalot_u_le_vinyamin_chamesh")

# -------------------------- Gen.45.23 · TEN_DONKEYS_TEN_SHE_ASSES ----------
# ‹וּלְאָבִיו שָׁלַח כְּזֹאת› (“and-to-father-him/its send like-this”)
# ‹עֲשָׂרָה חֲמֹרִים נֹשְׂאִים› (“ten male-ass lift/carry”)
# ‹מִטּוּב מִצְרָיִם וְעֶשֶׂר› (“from-good Egypt and-ten”)
# ‹אֲתֹנֹת נֹשְׂאֹת בָּר› (“female-donkey lift/carry grain-of-any-kind”)
# ‹וָלֶחֶם וּמָזוֹן לְאָבִיו› (“and-food and-food to-father-him/its”)
# ‹לַדָּרֶךְ› (“to-way/road”)
# "[EN-AID] And to his father he sent after this manner: ten donkeys
# carrying of the good of Egypt, and ten she-asses carrying grain and bread
# and sustenance for his father for the way."
m.step("Gen.45.23")
# ‹עֲשָׂרָה חֲמֹרִים נֹשְׂאִים› (“ten male-ass lift/carry”)
# — fact holds: ten-male-ass-and-ten-female-donkey
m.fact("asara_chamorim_ve_eser_atonot")
# witness-tier presupposed read: a_vow_rule_grounded_on_an_inventory on
# grain_and_bread_and_food — read, not installed
m.witness_read("grain_and_bread_and_food", "a_vow_rule_grounded_on_an_inventory",
                cites=["Bereshit Rabbah 94:2"])

# -------------------------- Gen.45.24 · DO_NOT_QUARREL_ON_THE_WAY ----------
# ‹וַיְשַׁלַּח אֶת־אֶחָיו וַיֵּלֵכוּ› (“and-send obj-marker brother-him/its
# and-go”)
# ‹וַיֹּאמֶר אֲלֵהֶם אַל־תִּרְגְּזוּ› (“and-say to-them/their do-not
# quiver”)
# ‹בַּדָּרֶךְ› (“in-way/road”)
# "[EN-AID] And he sent his brothers away, and they went; and he said to
# them: Do not quarrel on the way."
m.step("Gen.45.24")
# ‹אַל־תִּרְגְּזוּ בַּדָּרֶךְ› (“do-not quiver in-way/road”)
# — Joseph speaks a demand — LET-NOT: over-tirgezu-in-the-way/road
m.declare("yosef", "LET-NOT",
          "al_tirgezu_ba_darekh")
# witness-tier presupposed read: three_travel_rules_and_the_buffers_premise
# on do_not_be_agitated_on_the_way — read, not installed
m.witness_read("do_not_be_agitated_on_the_way", "three_travel_rules_and_the_buffers_premise",
                cites=["Bereshit Rabbah 94:2", "Onkelos Genesis 45:24"])
# witness-tier presupposed read: road_engrossment on al_tirgezu_va_darekh —
# read, not installed
m.witness_read("al_tirgezu_va_darekh", "road_engrossment",
                cites=["Taanit 10b:7", "Taanit 10b:8"])

# -------------------------- Gen.45.25 · UP_FROM_EGYPT ----------------------
# ‹וַיַּעֲלוּ מִמִּצְרָיִם וַיָּבֹאוּ› (“and-go-up from-Egypt and-
# come/bring”)
# ‹אֶרֶץ כְּנַעַן אֶל־יַעֲקֹב› (“earth Canaan to Jacob”)
# ‹אֲבִיהֶם› (“father-them/their”)
# "[EN-AID] And they went up from Egypt, and they came to the land of
# Canaan, to Jacob their father."
m.step("Gen.45.25")
# ‹וַיַּעֲלוּ מִמִּצְרָיִם וַיָּבֹאוּ› (“and-go-up from-Egypt and-
# come/bring”)
# ‹אֶרֶץ כְּנַעַן אֶל־יַעֲקֹב› (“earth Canaan to Jacob”)
# ‹אֲבִיהֶם› (“father-them/their”)
# — demand settled (popped from the queue): hasten-and-go-up-to-avi
m.result("maharu_va_alu_el_avi", tmark="t4")

# -------------------------- Gen.45.26 · JOSEPH_STILL_LIVES -----------------
# ‹וַיַּגִּדוּ לוֹ לֵאמֹר› (“and-tell to-him/its to-say”)
# ‹עוֹד יוֹסֵף חַי› (“still/again Joseph living”)
# ‹וְכִי־הוּא מֹשֵׁל בְּכָל־אֶרֶץ› (“and-that he/it rule in-all earth”)
# ‹מִצְרָיִם וַיָּפָג לִבּוֹ› (“Egypt and-be-sluggish heart-him/its”)
# ‹כִּי לֹא־הֶאֱמִין לָהֶם› (“that not build-up to-them/their”)
# "[EN-AID] And they told him, saying: Joseph still lives! — and that he
# rules over all the land of Egypt. And his heart went numb, for he did not
# believe them."
m.step("Gen.45.26")
# ‹לֵאמֹר עוֹד יוֹסֵף› (“to-say still/again Joseph”)
# ‹חַי› (“living”)
# — fact holds: still/again-Joseph-living-and-be-sluggish-His-heart
m.fact("od_yosef_chai_va_yafag_libo")
# witness-tier presupposed read: the_liars_penalty_and_the_faculty_named on
# he_did_not_believe_them — read, not installed
m.witness_read("he_did_not_believe_them", "the_liars_penalty_and_the_faculty_named",
                cites=["Bereshit Rabbah 94:3", "Onkelos Genesis 45:26"])

# -------------------------- Gen.45.27 · THE_WAGONS_SEEN --------------------
# ‹וַיְדַבְּרוּ אֵלָיו אֵת› (“and-speak to-him/its obj-marker”)
# ‹כָּל־דִּבְרֵי יוֹסֵף אֲשֶׁר› (“all word/thing Joseph which”)
# ‹דִּבֶּר אֲלֵהֶם וַיַּרְא› (“speak to-them/their and-see”)
# ‹אֶת־הָעֲגָלוֹת אֲשֶׁר־שָׁלַח יוֹסֵף› (“obj-marker the-something-revolving
# which send Joseph”)
# ‹לָשֵׂאת אֹתוֹ וַתְּחִי› (“to-lift/carry obj-marker-him/its and-live”)
# ‹רוּחַ יַעֲקֹב אֲבִיהֶם› (“spirit Jacob father-them/their”)
# "[EN-AID] And they spoke to him all the words of Joseph which he had
# spoken to them; and he saw the wagons which Joseph had sent to carry him;
# and the spirit of Jacob their father revived."
m.step("Gen.45.27")
# ‹וַתְּחִי רוּחַ יַעֲקֹב› (“and-live spirit Jacob”)
# ‹אֲבִיהֶם› (“father-them/their”)
# — fact holds: and-see-obj-marker-the-something-revolving-and-live-spirit-
# wind
m.fact("va_yar_et_ha_agalot_va_techi_ruach")
# witness-grounded state (its own tier):
# a_password_whose_two_ends_are_both_in_the_torah on the_wagons
m.witness_state("the_wagons", "a_password_whose_two_ends_are_both_in_the_torah",
                cites=["Bereshit Rabbah 94:3", "Onkelos Genesis 45:27"])

# -------------------------- Gen.45.28 · ENOUGH_JOSEPH_MY_SON_LIVES ---------
# ‹וַיֹּאמֶר יִשְׂרָאֵל רַב› (“and-say Israel many/great”)
# ‹עוֹד־יוֹסֵף בְּנִי חָי› (“still/again Joseph son-me/my living”)
# ‹אֵלְכָה וְאֶרְאֶנּוּ בְּטֶרֶם› (“go and-see-him/its in-non-occurrence”)
# ‹אָמוּת› (“die”)
# "[EN-AID] And Israel said: Enough! Joseph my son still lives; I will go
# and see him before I die."
m.step("Gen.45.28")
# ‹רַב עוֹד־יוֹסֵף בְּנִי› (“many/great still/again Joseph son-me/my”)
# ‹חָי› (“living”)
# — fact holds: many/great-still/again-Joseph-beni-living
m.fact("rav_od_yosef_beni_chai")
# witness-tier presupposed read: two_refusals_of_the_plain_sense on
# rav_yosef_beni_chai — read, not installed
m.witness_read("rav_yosef_beni_chai", "two_refusals_of_the_plain_sense",
                cites=["Bereshit Rabbah 94:3", "Onkelos Genesis 45:28"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['u_qchu_et_avikhem_u_vou_elai', 'al_tirgezu_ba_darekh']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ani_yosef_ha_od_avi_chai', 'al_teatzvu_ve_al_yichar', 'od_chamesh_shanim_en_charish_ve_qatzir', 'la_sum_lakhem_sheerit_ba_aretz', 'lo_atem_shelachtem_ki_ha_Elohim', 've_yashavta_be_eretz_goshen', 've_khilkalti_otkha_pen_tivaresh', 'enekhem_root_ve_ene_achi_vinyamin', 've_higadtem_ve_horadtem_et_avi', 've_achare_khen_dibru_echav_ito', 've_ha_qol_nishma_bet_paro', 'zot_asu_taanu_et_beirkhem', 've_enkhem_al_tachos', 'chalifot_semalot_u_le_vinyamin_chamesh', 'asara_chamorim_ve_eser_atonot', 'od_yosef_chai_va_yafag_libo', 'va_yar_et_ha_agalot_va_techi_ruach', 'rav_od_yosef_beni_chai'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    assert sorted(m.WORLD["witnessed"]) == ['the_necks_written_plural', 'the_wagons']
    assert m.WORLD["witnessed"]['the_necks_written_plural']["cites"] == ['Bereshit Rabbah 93:12']
    assert all('a_form_that_stands_once_in_the_torah' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_wagons']["cites"] == ['Bereshit Rabbah 94:3', 'Onkelos Genesis 45:27']
    assert all('a_password_whose_two_ends_are_both_in_the_torah' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('he_could_not_restrain_himself', 'the_speech_of_gen_67_completing_here'), ('his_brothers_could_not_answer_him', 'one_inference_stated_twice_by_two_authorities'), ('come_near_to_me', 'the_body_entered_as_evidence'), ('my_mouth_speaking_to_you', 'the_language_itself_as_credential'), ('the_news_heard_in_pharaohs_house', 'a_seat_predicted_four_chapters_early'), ('grain_and_bread_and_food', 'a_vow_rule_grounded_on_an_inventory'), ('do_not_be_agitated_on_the_way', 'three_travel_rules_and_the_buffers_premise'), ('al_tirgezu_va_darekh', 'road_engrossment'), ('he_did_not_believe_them', 'the_liars_penalty_and_the_faculty_named'), ('rav_yosef_beni_chai', 'two_refusals_of_the_plain_sense')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 93:9', 'Bereshit Rabbah 93:8']
    assert all('the_speech_of_gen_67_completing_here' not in f for f in m.WORLD["facts"])
    assert 'he_could_not_restrain_himself' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 93:10', 'Bereshit Rabbah 93:11', 'Bereshit Rabbah 93:2']
    assert all('one_inference_stated_twice_by_two_authorities' not in f for f in m.WORLD["facts"])
    assert 'his_brothers_could_not_answer_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 93:10']
    assert all('the_body_entered_as_evidence' not in f for f in m.WORLD["facts"])
    assert 'come_near_to_me' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 93:10', 'Onkelos Genesis 45:12']
    assert all('the_language_itself_as_credential' not in f for f in m.WORLD["facts"])
    assert 'my_mouth_speaking_to_you' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 94:1', 'Bereshit Rabbah 90:1']
    assert all('a_seat_predicted_four_chapters_early' not in f for f in m.WORLD["facts"])
    assert 'the_news_heard_in_pharaohs_house' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 94:2']
    assert all('a_vow_rule_grounded_on_an_inventory' not in f for f in m.WORLD["facts"])
    assert 'grain_and_bread_and_food' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 94:2', 'Onkelos Genesis 45:24']
    assert all('three_travel_rules_and_the_buffers_premise' not in f for f in m.WORLD["facts"])
    assert 'do_not_be_agitated_on_the_way' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Taanit 10b:7', 'Taanit 10b:8']
    assert all('road_engrossment' not in f for f in m.WORLD["facts"])
    assert 'al_tirgezu_va_darekh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 94:3', 'Onkelos Genesis 45:26']
    assert all('the_liars_penalty_and_the_faculty_named' not in f for f in m.WORLD["facts"])
    assert 'he_did_not_believe_them' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 94:3', 'Onkelos Genesis 45:28']
    assert all('two_refusals_of_the_plain_sense' not in f for f in m.WORLD["facts"])
    assert 'rav_yosef_beni_chai' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
