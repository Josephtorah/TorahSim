#!/usr/bin/env python3
# =============================================================================
# exo_19_sinai_and_the_covenant — 19:1-25
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_19_sinai_and_the_covenant.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Sinai and the covenant (19:1-25)"""
from machine import Machine

m = Machine("exo_19_sinai_and_the_covenant")

# -------------------------- Exod.19.1 · THE_THIRD_MONTH --------------------
# ‹בַּחֹדֶשׁ הַשְּׁלִישִׁי לְצֵאת› (“in-new-moon the-third to-bring-forth”)
# ‹בְּנֵי־יִשְׂרָאֵל מֵאֶרֶץ מִצְרָיִם› (“son Israel from-earth Egypt”)
# ‹בַּיּוֹם הַזֶּה בָּאוּ› (“in-day the-this come/bring”)
# ‹מִדְבַּר סִינָי› (“pasture Sinai”)
# "[EN-AID] In the third month of the going-out of the sons of Israel from
# the land of Egypt — on this day they came to the wilderness of Sinai."
m.step("Exod.19.1")
# ‹בַּיּוֹם הַזֶּה בָּאוּ› (“in-day the-this come/bring”)
# ‹מִדְבַּר סִינָי› (“pasture Sinai”)
# — fact holds: come/bring-pasture-Sinai
m.fact("bau_midbar_sinay")

# -------------------------- Exod.19.2 · AS_ONE_MAN -------------------------
# ‹וַיִּסְעוּ מֵרְפִידִים וַיָּבֹאוּ› (“and-journey from-Rephidim and-
# come/bring”)
# ‹מִדְבַּר סִינַי וַיַּחֲנוּ› (“pasture Sinai and-encamp”)
# ‹בַּמִּדְבָּר וַיִּחַן־שָׁם יִשְׂרָאֵל› (“in-pasture and-encamp there
# Israel”)
# ‹נֶגֶד הָהָר› (“front the-mountain”)
# "[EN-AID] And they set out from Rephidim, and came to the wilderness of
# Sinai, and camped in the wilderness — and Israel camped there before the
# mountain."
m.step("Exod.19.2")
# ‹וַיִּחַן־שָׁם יִשְׂרָאֵל נֶגֶד› (“and-encamp there Israel front”)
# ‹הָהָר› (“the-mountain”)
# — fact holds: and-encamp-there-Israel
m.fact("va_yichan_sham_yisrael")

# -------------------------- Exod.19.3 · HOUSE_OF_JACOB_SONS_OF_ISRAEL ------
# ‹וּמֹשֶׁה עָלָה אֶל־הָאֱלֹהִים› (“and-Moses go-up to the-God”)
# ‹וַיִּקְרָא אֵלָיו יְהוָה› (“and-call to-him/its YHWH”)
# ‹מִן־הָהָר לֵאמֹר כֹּה› (“from the-mountain to-say like-this”)
# ‹תֹאמַר לְבֵית יַעֲקֹב› (“say to-house Jacob”)
# ‹וְתַגֵּיד לִבְנֵי יִשְׂרָאֵל› (“and-tell to-son Israel”)
# "[EN-AID] And Moses went up to God; and the LORD called to him from the
# mountain, saying: So shall you say to the house of Jacob, and tell the
# sons of Israel."
m.step("Exod.19.3")
# ‹כֹּה תֹאמַר לְבֵית› (“like-this say to-house”)
# ‹יַעֲקֹב וְתַגֵּיד לִבְנֵי› (“Jacob and-tell to-son”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — fact holds: and-Moses-go-up-to-the-God
m.fact("u_moshe_ala_el_ha_elohim")

# -------------------------- Exod.19.4 · ON_EAGLES_WINGS --------------------
# ‹אַתֶּם רְאִיתֶם אֲשֶׁר› (“you see which”)
# ‹עָשִׂיתִי לְמִצְרָיִם וָאֶשָּׂא› (“make to-Egypt and-lift/carry”)
# ‹אֶתְכֶם עַל־כַּנְפֵי נְשָׁרִים› (“obj-marker-you/your(pl) over wing
# eagle”)
# ‹וָאָבִא אֶתְכֶם אֵלָי› (“and-come/bring obj-marker-you/your(pl) to-
# me/my”)
# "[EN-AID] You have seen what I did to Egypt; and I bore you on eagles'
# wings, and brought you to Me."
m.step("Exod.19.4")
# ‹וָאֶשָּׂא אֶתְכֶם עַל־כַּנְפֵי› (“and-lift/carry obj-marker-you/your(pl)
# over wing”)
# ‹נְשָׁרִים וָאָבִא אֶתְכֶם› (“eagle and-come/bring obj-marker-
# you/your(pl)”)
# ‹אֵלָי› (“to-me/my”)
# — fact holds: and-lift/carry-etkhem-over-wing-eagle
m.fact("va_esa_etkhem_al_kanfe_nesharim")

# -------------------------- Exod.19.5 · IF_YOU_WILL_HEAR -------------------
# ‹וְעַתָּה אִם־שָׁמוֹעַ תִּשְׁמְעוּ› (“and-now if hear hear”)
# ‹בְּקֹלִי וּשְׁמַרְתֶּם אֶת־בְּרִיתִי› (“in-voice/sound-me/my and-
# keep/guard obj-marker covenant-me/my”)
# ‹וִהְיִיתֶם לִי סְגֻלָּה› (“and-be to-me/my wealth”)
# ‹מִכָּל־הָעַמִּים כִּי־לִי כָּל־הָאָרֶץ› (“from-all the-people that to-
# me/my all the-earth”)
# "[EN-AID] And now, if you will surely hear My voice, and keep My covenant
# — then you shall be to Me a treasure out of all the peoples, for all the
# earth is Mine."
m.step("Exod.19.5")
# ‹אִם־שָׁמוֹעַ תִּשְׁמְעוּ בְּקֹלִי› (“if hear hear in-voice/sound-me/my”)
# ‹וּשְׁמַרְתֶּם אֶת־בְּרִיתִי› (“and-keep/guard obj-marker covenant-me/my”)
# — the-LORD speaks a demand — LET: if-hear-tishmeu-in-qoli
m.declare("YHWH", "LET",
          "im_shamoa_tishmeu_be_qoli")

# -------------------------- Exod.19.6 · A_KINGDOM_OF_PRIESTS ---------------
# ‹וְאַתֶּם תִּהְיוּ־לִי מַמְלֶכֶת› (“and-you be to-me/my dominion”)
# ‹כֹּהֲנִים וְגוֹי קָדוֹשׁ› (“priest and-nation sacred”)
# ‹אֵלֶּה הַדְּבָרִים אֲשֶׁר› (“these the-word/thing which”)
# ‹תְּדַבֵּר אֶל־בְּנֵי יִשְׂרָאֵל› (“speak to son Israel”)
# "[EN-AID] And you — you shall be to Me a kingdom of priests and a holy
# nation; these are the words which you shall speak to the sons of Israel."
m.step("Exod.19.6")
# ‹וְאַתֶּם תִּהְיוּ־לִי מַמְלֶכֶת› (“and-you be to-me/my dominion”)
# ‹כֹּהֲנִים וְגוֹי קָדוֹשׁ› (“priest and-nation sacred”)
# — fact holds: dominion-priest-and-nation-sacred
m.fact("mamlekhet_kohanim_ve_goy_qadosh")

# -------------------------- Exod.19.7 · BEFORE_THE_ELDERS ------------------
# ‹וַיָּבֹא מֹשֶׁה וַיִּקְרָא› (“and-come/bring Moses and-call”)
# ‹לְזִקְנֵי הָעָם וַיָּשֶׂם› (“to-old the-people and-put/set”)
# ‹לִפְנֵיהֶם אֵת כָּל־הַדְּבָרִים› (“to-face-them/their obj-marker all the-
# word/thing”)
# ‹הָאֵלֶּה אֲשֶׁר צִוָּהוּ› (“the-these which command-him/its”)
# ‹יְהוָה› (“YHWH”)
# "[EN-AID] And Moses came, and called for the elders of the people — and
# set before them all these words which the LORD had commanded him."
m.step("Exod.19.7")
# ‹וַיָּשֶׂם לִפְנֵיהֶם אֵת› (“and-put/set to-face-them/their obj-marker”)
# ‹כָּל־הַדְּבָרִים הָאֵלֶּה› (“all the-word/thing the-these”)
# — fact holds: and-put/set-lifnehem
m.fact("va_yasem_lifnehem")

# -------------------------- Exod.19.8 · ALL_THAT_THE_LORD_HAS_SPOKEN -------
# ‹וַיַּעֲנוּ כָל־הָעָם יַחְדָּו› (“and-eye all the-people unit”)
# ‹וַיֹּאמְרוּ כֹּל אֲשֶׁר־דִּבֶּר› (“and-say all which speak”)
# ‹יְהוָה נַעֲשֶׂה וַיָּשֶׁב› (“YHWH make and-return”)
# ‹מֹשֶׁה אֶת־דִּבְרֵי הָעָם› (“Moses obj-marker word/thing the-people”)
# ‹אֶל־יְהוָה› (“to YHWH”)
# "[EN-AID] And all the people answered together, and said: All that the
# LORD has spoken, we will do. And Moses brought back the words of the
# people to the LORD."
m.step("Exod.19.8")
# ‹וַיַּעֲנוּ כָל־הָעָם יַחְדָּו› (“and-eye all the-people unit”)
# ‹וַיֹּאמְרוּ כֹּל אֲשֶׁר־דִּבֶּר› (“and-say all which speak”)
# ‹יְהוָה נַעֲשֶׂה› (“YHWH make”)
# — demand settled (popped from the queue): if-hear-tishmeu-in-qoli
m.result("im_shamoa_tishmeu_be_qoli", tmark="t1")

# -------------------------- Exod.19.9 · THE_THICK_CLOUD --------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹הִנֵּה אָנֹכִי בָּא› (“behold come/bring”)
# ‹אֵלֶיךָ בְּעַב הֶעָנָן› (“to-you/your in-envelope the-cloud”)
# ‹בַּעֲבוּר יִשְׁמַע הָעָם› (“for-the-sake-of hear the-people”)
# ‹בְּדַבְּרִי עִמָּךְ וְגַם־בְּךָ› (“in-speak-me/my with-you/your and-also
# in-you/your”)
# ‹יַאֲמִינוּ לְעוֹלָם וַיַּגֵּד› (“build-up to-forever and-tell”)
# ‹מֹשֶׁה אֶת־דִּבְרֵי הָעָם› (“Moses obj-marker word/thing the-people”)
# ‹אֶל־יְהוָה› (“to YHWH”)
# "[EN-AID] And the LORD said to Moses: Behold, I come to you in the
# thickness of the cloud, that the people may hear in My speaking with you,
# and also believe in you forever. And Moses told the words of the people to
# the LORD."
m.step("Exod.19.9")
# ‹בַּעֲבוּר יִשְׁמַע הָעָם› (“for-the-sake-of hear the-people”)
# ‹בְּדַבְּרִי עִמָּךְ וְגַם־בְּךָ› (“in-speak-me/my with-you/your and-also
# in-you/your”)
# ‹יַאֲמִינוּ לְעוֹלָם› (“build-up to-forever”)
# — fact holds: baavur-hear-the-people
m.fact("baavur_yishma_ha_am")

# -------------------------- Exod.19.10 · SANCTIFY_THEM ---------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹לֵךְ אֶל־הָעָם וְקִדַּשְׁתָּם› (“go to the-people and-sanctify-
# them/their”)
# ‹הַיּוֹם וּמָחָר וְכִבְּסוּ› (“the-day and-deferred and-trample”)
# ‹שִׂמְלֹתָם› (“dress-them/their”)
# "[EN-AID] And the LORD said to Moses: Go to the people, and sanctify them
# today and tomorrow — and let them wash their garments."
m.step("Exod.19.10")
# ‹לֵךְ אֶל־הָעָם וְקִדַּשְׁתָּם› (“go to the-people and-sanctify-
# them/their”)
# ‹הַיּוֹם וּמָחָר וְכִבְּסוּ› (“the-day and-deferred and-trample”)
# ‹שִׂמְלֹתָם› (“dress-them/their”)
# — the-LORD speaks a demand — LET: and-qidashtam-the-day-and-deferred
m.declare("YHWH", "LET",
          "ve_qidashtam_ha_yom_u_machar")

# -------------------------- Exod.19.11 · READY_FOR_THE_THIRD_DAY -----------
# ‹וְהָיוּ נְכֹנִים לַיּוֹם› (“and-be be-erect to-day”)
# ‹הַשְּׁלִישִׁי כִּי בַּיּוֹם› (“the-third that in-day”)
# ‹הַשְּׁלִישִׁי יֵרֵד יְהוָה› (“the-third go-down YHWH”)
# ‹לְעֵינֵי כָל־הָעָם עַל־הַר› (“to-eye all the-people over mountain”)
# ‹סִינָי› (“Sinai”)
# "[EN-AID] And they shall be ready for the third day — for on the third day
# the LORD will descend, before the eyes of all the people, on mount Sinai."
m.step("Exod.19.11")
# ‹כִּי בַּיּוֹם הַשְּׁלִישִׁי› (“that in-day the-third”)
# ‹יֵרֵד יְהוָה לְעֵינֵי› (“go-down YHWH to-eye”)
# ‹כָל־הָעָם עַל־הַר סִינָי› (“all the-people over mountain Sinai”)
# — fact holds: go-down-the-LORD-to-eye-all-the-people
m.fact("yered_YHWH_le_ene_khol_ha_am")

# -------------------------- Exod.19.12 · FENCE_THE_PEOPLE ------------------
# ‹וְהִגְבַּלְתָּ אֶת־הָעָם סָבִיב› (“and-twist-as-arope obj-marker the-
# people circle”)
# ‹לֵאמֹר הִשָּׁמְרוּ לָכֶם› (“to-say keep/guard to-you/your(pl)”)
# ‹עֲלוֹת בָּהָר וּנְגֹעַ› (“go-up in-mountain and-touch”)
# ‹בְּקָצֵהוּ כָּל־הַנֹּגֵעַ בָּהָר› (“in-end-him/its all the-touch in-
# mountain”)
# ‹מוֹת יוּמָת› (“die die”)
# "[EN-AID] And you shall set bounds for the people round about, saying:
# Guard yourselves against going up into the mountain, or touching its edge;
# whoever touches the mountain shall surely be put to death."
m.step("Exod.19.12")
# ‹וְהִגְבַּלְתָּ אֶת־הָעָם סָבִיב› (“and-twist-as-arope obj-marker the-
# people circle”)
# ‹לֵאמֹר› (“to-say”)
# — the-LORD speaks a demand — LET: and-twist-as-arope-obj-marker-the-people
m.declare("YHWH", "LET",
          "ve_higbalta_et_ha_am")

# -------------------------- Exod.19.13 · WHEN_THE_HORN_DRAWS_OUT -----------
# ‹לֹא־תִגַּע בּוֹ יָד› (“not touch in-him/its hand”)
# ‹כִּי־סָקוֹל יִסָּקֵל אוֹ־יָרֹה› (“that be-weighty be-weighty or flow-as-
# water”)
# ‹יִיָּרֶה אִם־בְּהֵמָה אִם־אִישׁ› (“flow-as-water if livestock if man”)
# ‹לֹא יִחְיֶה בִּמְשֹׁךְ› (“not live in-draw”)
# ‹הַיֹּבֵל הֵמָּה יַעֲלוּ› (“the-blast-of-a-horn they go-up”)
# ‹בָהָר› (“in-mountain”)
# "[EN-AID] No hand shall touch him, but he shall surely be stoned, or
# surely shot; whether beast or man, it shall not live. When the ram's horn
# draws out — they shall come up on the mountain."
m.step("Exod.19.13")
# ‹בִּמְשֹׁךְ הַיֹּבֵל הֵמָּה› (“in-draw the-blast-of-a-horn they”)
# ‹יַעֲלוּ בָהָר› (“go-up in-mountain”)
# — fact holds: bimshokh-the-blast-of-a-horn-they-go-up
m.fact("bimshokh_ha_yovel_hema_yaalu")
# witness-tier presupposed read: boundary_and_covenant_file on
# bimshokh_ha_yovel_hema_yaalu — read, not installed
m.witness_read("bimshokh_ha_yovel_hema_yaalu", "boundary_and_covenant_file",
                cites=["Sanhedrin 45a:14", "Sanhedrin 45a:15", "Sanhedrin 15b:6", "Beitzah 5a:6", "Beitzah 5a:7", "Beitzah 5b:3", "Beitzah 5b:4", "Beitzah 5b:5", "Yevamot 46b:2", "Yevamot 46b:3", "Shabbat 86b:5", "Shabbat 87a:1", "Shabbat 87a:2", "Shabbat 87a:3", "Shabbat 87a:4", "Shabbat 87a:5", "Shabbat 86a:6"])

# -------------------------- Exod.19.14 · MOSES_SANCTIFIES ------------------
# ‹וַיֵּרֶד מֹשֶׁה מִן־הָהָר› (“and-go-down Moses from the-mountain”)
# ‹אֶל־הָעָם וַיְקַדֵּשׁ אֶת־הָעָם› (“to the-people and-sanctify obj-marker
# the-people”)
# ‹וַיְכַבְּסוּ שִׂמְלֹתָם› (“and-trample dress-them/their”)
# "[EN-AID] And Moses went down from the mountain to the people — and he
# sanctified the people, and they washed their garments."
m.step("Exod.19.14")
# ‹וַיְקַדֵּשׁ אֶת־הָעָם וַיְכַבְּסוּ› (“and-sanctify obj-marker the-people
# and-trample”)
# ‹שִׂמְלֹתָם› (“dress-them/their”)
# — demand settled (popped from the queue): and-qidashtam-the-day-and-
# deferred
m.result("ve_qidashtam_ha_yom_u_machar", tmark="t1")

# -------------------------- Exod.19.15 · THREE_DAYS ------------------------
# ‹וַיֹּאמֶר אֶל־הָעָם הֱיוּ› (“and-say to the-people be”)
# ‹נְכֹנִים לִשְׁלֹשֶׁת יָמִים› (“be-erect to-three day”)
# ‹אַל־תִּגְּשׁוּ אֶל־אִשָּׁה› (“do-not be to woman”)
# "[EN-AID] And he said to the people: Be ready for three days — approach
# not a woman."
m.step("Exod.19.15")
# ‹הֱיוּ נְכֹנִים לִשְׁלֹשֶׁת› (“be be-erect to-three”)
# ‹יָמִים אַל־תִּגְּשׁוּ אֶל־אִשָּׁה› (“day do-not be to woman”)
# — fact holds: heyu-be-erect-to-me-sheloshet-day
m.fact("heyu_nekhonim_li_sheloshet_yamim")
# witness-tier presupposed read: purity_window on three_days_ready — read,
# not installed
m.witness_read("three_days_ready", "purity_window",
                cites=["Mishnah Shabbat 9:3"])

# -------------------------- Exod.19.16 · THUNDERS_AND_LIGHTNINGS -----------
# ‹וַיְהִי בַיּוֹם הַשְּׁלִישִׁי› (“and-be in-day the-third”)
# ‹בִּהְיֹת הַבֹּקֶר וַיְהִי› (“in-be the-morning and-be”)
# ‹קֹלֹת וּבְרָקִים וְעָנָן› (“voice/sound and-lightning and-cloud”)
# ‹כָּבֵד עַל־הָהָר וְקֹל› (“heavy over the-mountain and-voice/sound”)
# ‹שֹׁפָר חָזָק מְאֹד› (“cornet strong very”)
# ‹וַיֶּחֱרַד כָּל־הָעָם אֲשֶׁר› (“and-shudder-with-terror all the-people
# which”)
# ‹בַּמַּחֲנֶה› (“in-camp”)
# "[EN-AID] And it was on the third day, when the morning was, that there
# were thunders and lightnings, and a heavy cloud on the mountain, and a
# shofar-voice exceedingly strong — and all the people that were in the camp
# trembled."
m.step("Exod.19.16")
# ‹וַיְהִי קֹלֹת וּבְרָקִים› (“and-be voice/sound and-lightning”)
# ‹וְעָנָן כָּבֵד עַל־הָהָר› (“and-cloud heavy over the-mountain”)
# ‹וְקֹל שֹׁפָר חָזָק› (“and-voice/sound cornet strong”)
# ‹מְאֹד› (“very”)
# — event: voice/sound-and-lightning — theme har-sinay
m.event("qolot_u_veraqim", themes=["har-sinay"])

# -------------------------- Exod.19.17 · TO_MEET_GOD -----------------------
# ‹וַיּוֹצֵא מֹשֶׁה אֶת־הָעָם› (“and-bring-forth Moses obj-marker the-
# people”)
# ‹לִקְרַאת הָאֱלֹהִים מִן־הַמַּחֲנֶה› (“to-encountering the-God from the-
# camp”)
# ‹וַיִּתְיַצְּבוּ בְּתַחְתִּית הָהָר› (“and-place in-lowermost the-
# mountain”)
# "[EN-AID] And Moses brought the people out toward God, out of the camp —
# and they stationed themselves at the underside of the mountain."
m.step("Exod.19.17")
# ‹וַיִּתְיַצְּבוּ בְּתַחְתִּית הָהָר› (“and-place in-lowermost the-
# mountain”)
# — fact holds: and-place-in-lowermost-the-mountain
m.fact("va_yityatzvu_be_tachtit_ha_har")

# -------------------------- Exod.19.18 · THE_MOUNTAIN_SMOKED ---------------
# ‹וְהַר סִינַי עָשַׁן› (“and-mountain Sinai smoke”)
# ‹כֻּלּוֹ מִפְּנֵי אֲשֶׁר› (“all-him/its from-face which”)
# ‹יָרַד עָלָיו יְהוָה› (“go-down over-him/its YHWH”)
# ‹בָּאֵשׁ וַיַּעַל עֲשָׁנוֹ› (“in-fire and-go-up smoke-him/its”)
# ‹כְּעֶשֶׁן הַכִּבְשָׁן וַיֶּחֱרַד› (“like-smoke the-smelting-furnace and-
# shudder-with-terror”)
# ‹כָּל־הָהָר מְאֹד› (“all the-mountain very”)
# "[EN-AID] And mount Sinai smoked, all of it, because the LORD descended on
# it in fire; and its smoke went up like the smoke of the kiln — and the
# whole mountain trembled exceedingly."
m.step("Exod.19.18")
# ‹וְהַר סִינַי עָשַׁן› (“and-mountain Sinai smoke”)
# ‹כֻּלּוֹ מִפְּנֵי אֲשֶׁר› (“all-him/its from-face which”)
# ‹יָרַד עָלָיו יְהוָה› (“go-down over-him/its YHWH”)
# ‹בָּאֵשׁ› (“in-fire”)
# — fact holds: and-mountain-Sinai-smoke-kulo
m.fact("ve_har_sinay_ashan_kulo")

# -------------------------- Exod.19.19 · VOICE_FOR_VOICE -------------------
# ‹וַיְהִי קוֹל הַשּׁוֹפָר› (“and-be voice/sound the-cornet”)
# ‹הוֹלֵךְ וְחָזֵק מְאֹד› (“walk/go and-powerful very”)
# ‹מֹשֶׁה יְדַבֵּר וְהָאֱלֹהִים› (“Moses speak and-the-God”)
# ‹יַעֲנֶנּוּ בְקוֹל› (“eye-him/its in-voice/sound”)
# "[EN-AID] And the voice of the shofar went on, going and strengthening
# exceedingly; Moses would speak — and God would answer him in a voice."
m.step("Exod.19.19")
# ‹מֹשֶׁה יְדַבֵּר וְהָאֱלֹהִים› (“Moses speak and-the-God”)
# ‹יַעֲנֶנּוּ בְקוֹל› (“eye-him/its in-voice/sound”)
# — fact holds: Moses-speak-and-the-God-yaanenu
m.fact("moshe_yedaber_ve_ha_elohim_yaanenu")
# witness-tier presupposed read: voice_protocol_file on
# moshe_yedaber_ve_ha_elohim_yaanenu — read, not installed
m.witness_read("moshe_yedaber_ve_ha_elohim_yaanenu", "voice_protocol_file",
                cites=["Sotah 33a:13", "Sotah 33a:14", "Berakhot 45a:7", "Berakhot 45a:8", "Berakhot 45a:9", "Sotah 27b:11", "Sotah 27b:12"])

# -------------------------- Exod.19.20 · THE_DESCENT -----------------------
# ‹וַיֵּרֶד יְהוָה עַל־הַר› (“and-go-down YHWH over mountain”)
# ‹סִינַי אֶל־רֹאשׁ הָהָר› (“Sinai to head the-mountain”)
# ‹וַיִּקְרָא יְהוָה לְמֹשֶׁה› (“and-call YHWH to-Moses”)
# ‹אֶל־רֹאשׁ הָהָר וַיַּעַל› (“to head the-mountain and-go-up”)
# ‹מֹשֶׁה› (“Moses”)
# "[EN-AID] And the LORD descended on mount Sinai, to the top of the
# mountain; and the LORD called Moses to the top of the mountain — and Moses
# went up."
m.step("Exod.19.20")
# ‹וַיֵּרֶד יְהוָה עַל־הַר› (“and-go-down YHWH over mountain”)
# ‹סִינַי אֶל־רֹאשׁ הָהָר› (“Sinai to head the-mountain”)
# — event: yeridat-the-LORD — agent the-LORD
m.event("yeridat_YHWH", agent="YHWH")

# -------------------------- Exod.19.21 · GO_DOWN_WARN ----------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹רֵד הָעֵד בָּעָם› (“go-down duplicate in-people”)
# ‹פֶּן־יֶהֶרְסוּ אֶל־יְהוָה לִרְאוֹת› (“lest pull-down to YHWH to-see”)
# ‹וְנָפַל מִמֶּנּוּ רָב› (“and-fall from-us/our many/great”)
# "[EN-AID] And the LORD said to Moses: Go down, warn the people — lest they
# break through to the LORD to see, and many of them fall."
m.step("Exod.19.21")
# ‹רֵד הָעֵד בָּעָם› (“go-down duplicate in-people”)
# — the-LORD speaks a demand — LET: go-down-duplicate-come/bring-people
m.declare("YHWH", "LET",
          "red_haed_ba_am")

# -------------------------- Exod.19.22 · THE_PRIESTS_TOO -------------------
# ‹וְגַם הַכֹּהֲנִים הַנִּגָּשִׁים› (“and-also the-priest the-be”)
# ‹אֶל־יְהוָה יִתְקַדָּשׁוּ פֶּן־יִפְרֹץ› (“to YHWH sanctify lest break-
# out”)
# ‹בָּהֶם יְהוָה› (“in-them/their YHWH”)
# "[EN-AID] And also the priests, who approach the LORD, shall sanctify
# themselves — lest the LORD break out against them."
m.step("Exod.19.22")
# ‹וְגַם הַכֹּהֲנִים הַנִּגָּשִׁים› (“and-also the-priest the-be”)
# ‹אֶל־יְהוָה יִתְקַדָּשׁוּ› (“to YHWH sanctify”)
# — fact holds: and-also-the-priest-sanctify
m.fact("ve_gam_ha_kohanim_yitqadashu")

# -------------------------- Exod.19.23 · THE_FENCE_STANDS ------------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־יְהוָה› (“and-say Moses to YHWH”)
# ‹לֹא־יוּכַל הָעָם לַעֲלֹת› (“not be-able the-people to-go-up”)
# ‹אֶל־הַר סִינָי כִּי־אַתָּה› (“to mountain Sinai that you”)
# ‹הַעֵדֹתָה בָּנוּ לֵאמֹר› (“duplicate in-us/our to-say”)
# ‹הַגְבֵּל אֶת־הָהָר וְקִדַּשְׁתּוֹ› (“twist-as-arope obj-marker the-
# mountain and-sanctify-him/its”)
# "[EN-AID] And Moses said to the LORD: The people cannot come up to mount
# Sinai — for You warned us, saying: Fence the mountain, and sanctify it."
m.step("Exod.19.23")
# ‹כִּי־אַתָּה הַעֵדֹתָה בָּנוּ› (“that you duplicate in-us/our”)
# ‹לֵאמֹר הַגְבֵּל אֶת־הָהָר› (“to-say twist-as-arope obj-marker the-
# mountain”)
# ‹וְקִדַּשְׁתּוֹ› (“and-sanctify-him/its”)
# — fact holds: not-be-able-the-people-to-go-up
m.fact("lo_yukhal_ha_am_la_alot")

# -------------------------- Exod.19.24 · BARRIERS_BY_RANK ------------------
# ‹וַיֹּאמֶר אֵלָיו יְהוָה› (“and-say to-him/its YHWH”)
# ‹לֶךְ־רֵד וְעָלִיתָ אַתָּה› (“go go-down and-go-up you”)
# ‹וְאַהֲרֹן עִמָּךְ וְהַכֹּהֲנִים› (“and-Aaron with-you/your and-the-
# priest”)
# ‹וְהָעָם אַל־יֶהֶרְסוּ לַעֲלֹת› (“and-the-people do-not pull-down to-go-
# up”)
# ‹אֶל־יְהוָה פֶּן־יִפְרָץ־בָּם› (“to YHWH lest break-out in-them/their”)
# "[EN-AID] And the LORD said to him: Go, descend — and you shall come up,
# you and Aaron with you; and the priests and the people shall not break
# through to come up to the LORD, lest He break out against them."
m.step("Exod.19.24")
# ‹לֶךְ־רֵד וְעָלִיתָ אַתָּה› (“go go-down and-go-up you”)
# ‹וְאַהֲרֹן עִמָּךְ› (“and-Aaron with-you/your”)
# — fact holds: and-go-up-now-and-Aaron-imakh
m.fact("ve_alita_ata_ve_aharon_imakh")

# -------------------------- Exod.19.25 · AND_SAID_TO_THEM ------------------
# ‹וַיֵּרֶד מֹשֶׁה אֶל־הָעָם› (“and-go-down Moses to the-people”)
# ‹וַיֹּאמֶר אֲלֵהֶם› (“and-say to-them/their”)
# "[EN-AID] And Moses went down to the people — and said to them."
m.step("Exod.19.25")
# ‹וַיֵּרֶד מֹשֶׁה אֶל־הָעָם› (“and-go-down Moses to the-people”)
# ‹וַיֹּאמֶר אֲלֵהֶם› (“and-say to-them/their”)
# — demand settled (popped from the queue): go-down-duplicate-come/bring-
# people
m.result("red_haed_ba_am", tmark="t1")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['ve_higbalta_et_ha_am']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['bau_midbar_sinay', 'va_yichan_sham_yisrael', 'u_moshe_ala_el_ha_elohim', 'va_esa_etkhem_al_kanfe_nesharim', 'mamlekhet_kohanim_ve_goy_qadosh', 'va_yasem_lifnehem', 'baavur_yishma_ha_am', 'yered_YHWH_le_ene_khol_ha_am', 'bimshokh_ha_yovel_hema_yaalu', 'heyu_nekhonim_li_sheloshet_yamim', 'va_yityatzvu_be_tachtit_ha_har', 've_har_sinay_ashan_kulo', 'moshe_yedaber_ve_ha_elohim_yaanenu', 've_gam_ha_kohanim_yitqadashu', 'lo_yukhal_ha_am_la_alot', 've_alita_ata_ve_aharon_imakh'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('bimshokh_ha_yovel_hema_yaalu', 'boundary_and_covenant_file'), ('three_days_ready', 'purity_window'), ('moshe_yedaber_ve_ha_elohim_yaanenu', 'voice_protocol_file')]
    assert m.WITNESS_READS[0]["cites"] == ['Sanhedrin 45a:14', 'Sanhedrin 45a:15', 'Sanhedrin 15b:6', 'Beitzah 5a:6', 'Beitzah 5a:7', 'Beitzah 5b:3', 'Beitzah 5b:4', 'Beitzah 5b:5', 'Yevamot 46b:2', 'Yevamot 46b:3', 'Shabbat 86b:5', 'Shabbat 87a:1', 'Shabbat 87a:2', 'Shabbat 87a:3', 'Shabbat 87a:4', 'Shabbat 87a:5', 'Shabbat 86a:6']
    assert all('boundary_and_covenant_file' not in f for f in m.WORLD["facts"])
    assert 'bimshokh_ha_yovel_hema_yaalu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Mishnah Shabbat 9:3']
    assert all('purity_window' not in f for f in m.WORLD["facts"])
    assert 'three_days_ready' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sotah 33a:13', 'Sotah 33a:14', 'Berakhot 45a:7', 'Berakhot 45a:8', 'Berakhot 45a:9', 'Sotah 27b:11', 'Sotah 27b:12']
    assert all('voice_protocol_file' not in f for f in m.WORLD["facts"])
    assert 'moshe_yedaber_ve_ha_elohim_yaanenu' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
