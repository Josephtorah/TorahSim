#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# בַּחֹדֶשׁ הַשְּׁלִישִׁי לְצֵאת בְּנֵי־יִשְׂרָאֵל מֵאֶרֶץ מִצְרָיִם
# בַּיּוֹם הַזֶּה בָּאוּ מִדְבַּר סִינָי
# "[EN-AID] In the third month of the going-out of the sons of Israel from
# the land of Egypt — on this day they came to the wilderness of Sinai."
m.step("Exod.19.1")
# ‹בַּיּוֹם הַזֶּה בָּאוּ מִדְבַּר סִינָי› (“in-day the-this come/bring
# pasture Sinai”) — fact holds: come/bring-pasture-Sinai
m.fact("bau_midbar_sinay")

# -------------------------- Exod.19.2 · AS_ONE_MAN -------------------------
# וַיִּסְעוּ מֵרְפִידִים וַיָּבֹאוּ מִדְבַּר סִינַי וַיַּחֲנוּ בַּמִּדְבָּר
# וַיִּחַן־שָׁם יִשְׂרָאֵל נֶגֶד הָהָר
# "[EN-AID] And they set out from Rephidim, and came to the wilderness of
# Sinai, and camped in the wilderness — and Israel camped there before the
# mountain."
m.step("Exod.19.2")
# ‹וַיִּחַן־שָׁם יִשְׂרָאֵל נֶגֶד הָהָר› (“and-encamp there Israel front
# the-mountain”) — fact holds: and-encamp-there-Israel
m.fact("va_yichan_sham_yisrael")

# -------------------------- Exod.19.3 · HOUSE_OF_JACOB_SONS_OF_ISRAEL ------
# וּמֹשֶׁה עָלָה אֶל־הָאֱלֹהִים וַיִּקְרָא אֵלָיו יְהוָה מִן־הָהָר לֵאמֹר
# כֹּה תֹאמַר לְבֵית יַעֲקֹב וְתַגֵּיד לִבְנֵי יִשְׂרָאֵל
# "[EN-AID] And Moses went up to God; and the LORD called to him from the
# mountain, saying: So shall you say to the house of Jacob, and tell the
# sons of Israel."
m.step("Exod.19.3")
# ‹כֹּה תֹאמַר לְבֵית יַעֲקֹב וְתַגֵּיד לִבְנֵי יִשְׂרָאֵל› (“like-this say
# to-house Jacob and-tell to-son Israel”) — fact holds: and-Moses-go-up-to-
# the-God
m.fact("u_moshe_ala_el_ha_elohim")

# -------------------------- Exod.19.4 · ON_EAGLES_WINGS --------------------
# אַתֶּם רְאִיתֶם אֲשֶׁר עָשִׂיתִי לְמִצְרָיִם וָאֶשָּׂא אֶתְכֶם
# עַל־כַּנְפֵי נְשָׁרִים וָאָבִא אֶתְכֶם אֵלָי
# "[EN-AID] You have seen what I did to Egypt; and I bore you on eagles'
# wings, and brought you to Me."
m.step("Exod.19.4")
# ‹וָאֶשָּׂא אֶתְכֶם עַל־כַּנְפֵי נְשָׁרִים וָאָבִא אֶתְכֶם אֵלָי› (“and-
# lift/carry obj-marker-you/your(pl) over wing eagle and-come/bring obj-
# marker-you/your(pl) to-me/my”) — fact holds: and-lift/carry-etkhem-over-
# wing-eagle
m.fact("va_esa_etkhem_al_kanfe_nesharim")

# -------------------------- Exod.19.5 · IF_YOU_WILL_HEAR -------------------
# וְעַתָּה אִם־שָׁמוֹעַ תִּשְׁמְעוּ בְּקֹלִי וּשְׁמַרְתֶּם אֶת־בְּרִיתִי
# וִהְיִיתֶם לִי סְגֻלָּה מִכָּל־הָעַמִּים כִּי־לִי כָּל־הָאָרֶץ
# "[EN-AID] And now, if you will surely hear My voice, and keep My covenant
# — then you shall be to Me a treasure out of all the peoples, for all the
# earth is Mine."
m.step("Exod.19.5")
# ‹אִם־שָׁמוֹעַ תִּשְׁמְעוּ בְּקֹלִי וּשְׁמַרְתֶּם אֶת־בְּרִיתִי› (“if hear
# hear in-voice/sound-me/my and-keep/guard obj-marker covenant-me/my”) —
# the-LORD speaks a demand — LET: if-hear-tishmeu-in-qoli
m.declare("YHWH", "LET",
          "im_shamoa_tishmeu_be_qoli")

# -------------------------- Exod.19.6 · A_KINGDOM_OF_PRIESTS ---------------
# וְאַתֶּם תִּהְיוּ־לִי מַמְלֶכֶת כֹּהֲנִים וְגוֹי קָדוֹשׁ אֵלֶּה
# הַדְּבָרִים אֲשֶׁר תְּדַבֵּר אֶל־בְּנֵי יִשְׂרָאֵל
# "[EN-AID] And you — you shall be to Me a kingdom of priests and a holy
# nation; these are the words which you shall speak to the sons of Israel."
m.step("Exod.19.6")
# ‹וְאַתֶּם תִּהְיוּ־לִי מַמְלֶכֶת כֹּהֲנִים וְגוֹי קָדוֹשׁ› (“and-you be
# to-me/my dominion priest and-nation sacred”) — fact holds: dominion-
# priest-and-nation-sacred
m.fact("mamlekhet_kohanim_ve_goy_qadosh")

# -------------------------- Exod.19.7 · BEFORE_THE_ELDERS ------------------
# וַיָּבֹא מֹשֶׁה וַיִּקְרָא לְזִקְנֵי הָעָם וַיָּשֶׂם לִפְנֵיהֶם אֵת
# כָּל־הַדְּבָרִים הָאֵלֶּה אֲשֶׁר צִוָּהוּ יְהוָה
# "[EN-AID] And Moses came, and called for the elders of the people — and
# set before them all these words which the LORD had commanded him."
m.step("Exod.19.7")
# ‹וַיָּשֶׂם לִפְנֵיהֶם אֵת כָּל־הַדְּבָרִים הָאֵלֶּה› (“and-put/set to-
# face-them/their obj-marker all the-word/thing the-these”) — fact holds:
# and-put/set-lifnehem
m.fact("va_yasem_lifnehem")

# -------------------------- Exod.19.8 · ALL_THAT_THE_LORD_HAS_SPOKEN -------
# וַיַּעֲנוּ כָל־הָעָם יַחְדָּו וַיֹּאמְרוּ כֹּל אֲשֶׁר־דִּבֶּר יְהוָה
# נַעֲשֶׂה וַיָּשֶׁב מֹשֶׁה אֶת־דִּבְרֵי הָעָם אֶל־יְהוָה
# "[EN-AID] And all the people answered together, and said: All that the
# LORD has spoken, we will do. And Moses brought back the words of the
# people to the LORD."
m.step("Exod.19.8")
# ‹וַיַּעֲנוּ כָל־הָעָם יַחְדָּו וַיֹּאמְרוּ כֹּל אֲשֶׁר־דִּבֶּר יְהוָה
# נַעֲשֶׂה› (“and-eye all the-people unit and-say all which speak YHWH
# make”) — demand settled (popped from the queue): if-hear-tishmeu-in-qoli
m.result("im_shamoa_tishmeu_be_qoli", tmark="t1")

# -------------------------- Exod.19.9 · THE_THICK_CLOUD --------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה הִנֵּה אָנֹכִי בָּא אֵלֶיךָ בְּעַב הֶעָנָן
# בַּעֲבוּר יִשְׁמַע הָעָם בְּדַבְּרִי עִמָּךְ וְגַם־בְּךָ יַאֲמִינוּ
# לְעוֹלָם וַיַּגֵּד מֹשֶׁה אֶת־דִּבְרֵי הָעָם אֶל־יְהוָה
# "[EN-AID] And the LORD said to Moses: Behold, I come to you in the
# thickness of the cloud, that the people may hear in My speaking with you,
# and also believe in you forever. And Moses told the words of the people to
# the LORD."
m.step("Exod.19.9")
# ‹בַּעֲבוּר יִשְׁמַע הָעָם בְּדַבְּרִי עִמָּךְ וְגַם־בְּךָ יַאֲמִינוּ
# לְעוֹלָם› (“for-the-sake-of hear the-people in-speak-me/my with-you/your
# and-also in-you/your build-up to-forever”) — fact holds: baavur-hear-the-
# people
m.fact("baavur_yishma_ha_am")

# -------------------------- Exod.19.10 · SANCTIFY_THEM ---------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה לֵךְ אֶל־הָעָם וְקִדַּשְׁתָּם הַיּוֹם וּמָחָר
# וְכִבְּסוּ שִׂמְלֹתָם
# "[EN-AID] And the LORD said to Moses: Go to the people, and sanctify them
# today and tomorrow — and let them wash their garments."
m.step("Exod.19.10")
# ‹לֵךְ אֶל־הָעָם וְקִדַּשְׁתָּם הַיּוֹם וּמָחָר וְכִבְּסוּ שִׂמְלֹתָם› (“go
# to the-people and-sanctify-them/their the-day and-deferred and-trample
# dress-them/their”) — the-LORD speaks a demand — LET: and-qidashtam-the-
# day-and-deferred
m.declare("YHWH", "LET",
          "ve_qidashtam_ha_yom_u_machar")

# -------------------------- Exod.19.11 · READY_FOR_THE_THIRD_DAY -----------
# וְהָיוּ נְכֹנִים לַיּוֹם הַשְּׁלִישִׁי כִּי בַּיּוֹם הַשְּׁלִישִׁי יֵרֵד
# יְהוָה לְעֵינֵי כָל־הָעָם עַל־הַר סִינָי
# "[EN-AID] And they shall be ready for the third day — for on the third day
# the LORD will descend, before the eyes of all the people, on mount Sinai."
m.step("Exod.19.11")
# ‹כִּי בַּיּוֹם הַשְּׁלִישִׁי יֵרֵד יְהוָה לְעֵינֵי כָל־הָעָם עַל־הַר
# סִינָי› (“that in-day the-third go-down YHWH to-eye all the-people over
# mountain Sinai”) — fact holds: go-down-the-LORD-to-eye-all-the-people
m.fact("yered_YHWH_le_ene_khol_ha_am")

# -------------------------- Exod.19.12 · FENCE_THE_PEOPLE ------------------
# וְהִגְבַּלְתָּ אֶת־הָעָם סָבִיב לֵאמֹר הִשָּׁמְרוּ לָכֶם עֲלוֹת בָּהָר
# וּנְגֹעַ בְּקָצֵהוּ כָּל־הַנֹּגֵעַ בָּהָר מוֹת יוּמָת
# "[EN-AID] And you shall set bounds for the people round about, saying:
# Guard yourselves against going up into the mountain, or touching its edge;
# whoever touches the mountain shall surely be put to death."
m.step("Exod.19.12")
# ‹וְהִגְבַּלְתָּ אֶת־הָעָם סָבִיב לֵאמֹר› (“and-twist-as-arope obj-marker
# the-people circle to-say”) — the-LORD speaks a demand — LET: and-twist-as-
# arope-obj-marker-the-people
m.declare("YHWH", "LET",
          "ve_higbalta_et_ha_am")

# -------------------------- Exod.19.13 · WHEN_THE_HORN_DRAWS_OUT -----------
# לֹא־תִגַּע בּוֹ יָד כִּי־סָקוֹל יִסָּקֵל אוֹ־יָרֹה יִיָּרֶה אִם־בְּהֵמָה
# אִם־אִישׁ לֹא יִחְיֶה בִּמְשֹׁךְ הַיֹּבֵל הֵמָּה יַעֲלוּ בָהָר
# "[EN-AID] No hand shall touch him, but he shall surely be stoned, or
# surely shot; whether beast or man, it shall not live. When the ram's horn
# draws out — they shall come up on the mountain."
m.step("Exod.19.13")
# ‹בִּמְשֹׁךְ הַיֹּבֵל הֵמָּה יַעֲלוּ בָהָר› (“in-draw the-blast-of-a-horn
# they go-up in-mountain”) — fact holds: bimshokh-the-blast-of-a-horn-they-
# go-up
m.fact("bimshokh_ha_yovel_hema_yaalu")

# -------------------------- Exod.19.14 · MOSES_SANCTIFIES ------------------
# וַיֵּרֶד מֹשֶׁה מִן־הָהָר אֶל־הָעָם וַיְקַדֵּשׁ אֶת־הָעָם וַיְכַבְּסוּ
# שִׂמְלֹתָם
# "[EN-AID] And Moses went down from the mountain to the people — and he
# sanctified the people, and they washed their garments."
m.step("Exod.19.14")
# ‹וַיְקַדֵּשׁ אֶת־הָעָם וַיְכַבְּסוּ שִׂמְלֹתָם› (“and-sanctify obj-marker
# the-people and-trample dress-them/their”) — demand settled (popped from
# the queue): and-qidashtam-the-day-and-deferred
m.result("ve_qidashtam_ha_yom_u_machar", tmark="t1")

# -------------------------- Exod.19.15 · THREE_DAYS ------------------------
# וַיֹּאמֶר אֶל־הָעָם הֱיוּ נְכֹנִים לִשְׁלֹשֶׁת יָמִים אַל־תִּגְּשׁוּ
# אֶל־אִשָּׁה
# "[EN-AID] And he said to the people: Be ready for three days — approach
# not a woman."
m.step("Exod.19.15")
# ‹הֱיוּ נְכֹנִים לִשְׁלֹשֶׁת יָמִים אַל־תִּגְּשׁוּ אֶל־אִשָּׁה› (“be be-
# erect to-three day do-not be to woman”) — fact holds: heyu-be-erect-to-me-
# sheloshet-day
m.fact("heyu_nekhonim_li_sheloshet_yamim")

# -------------------------- Exod.19.16 · THUNDERS_AND_LIGHTNINGS -----------
# וַיְהִי בַיּוֹם הַשְּׁלִישִׁי בִּהְיֹת הַבֹּקֶר וַיְהִי קֹלֹת וּבְרָקִים
# וְעָנָן כָּבֵד עַל־הָהָר וְקֹל שֹׁפָר חָזָק מְאֹד וַיֶּחֱרַד כָּל־הָעָם
# אֲשֶׁר בַּמַּחֲנֶה
# "[EN-AID] And it was on the third day, when the morning was, that there
# were thunders and lightnings, and a heavy cloud on the mountain, and a
# shofar-voice exceedingly strong — and all the people that were in the camp
# trembled."
m.step("Exod.19.16")
# ‹וַיְהִי קֹלֹת וּבְרָקִים וְעָנָן כָּבֵד עַל־הָהָר וְקֹל שֹׁפָר חָזָק
# מְאֹד› (“and-be voice/sound and-lightning and-cloud heavy over the-
# mountain and-voice/sound cornet strong very”) — event: voice/sound-and-
# lightning — theme har-sinay
m.event("qolot_u_veraqim", themes=["har-sinay"])

# -------------------------- Exod.19.17 · TO_MEET_GOD -----------------------
# וַיּוֹצֵא מֹשֶׁה אֶת־הָעָם לִקְרַאת הָאֱלֹהִים מִן־הַמַּחֲנֶה
# וַיִּתְיַצְּבוּ בְּתַחְתִּית הָהָר
# "[EN-AID] And Moses brought the people out toward God, out of the camp —
# and they stationed themselves at the underside of the mountain."
m.step("Exod.19.17")
# ‹וַיִּתְיַצְּבוּ בְּתַחְתִּית הָהָר› (“and-place in-lowermost the-
# mountain”) — fact holds: and-place-in-lowermost-the-mountain
m.fact("va_yityatzvu_be_tachtit_ha_har")

# -------------------------- Exod.19.18 · THE_MOUNTAIN_SMOKED ---------------
# וְהַר סִינַי עָשַׁן כֻּלּוֹ מִפְּנֵי אֲשֶׁר יָרַד עָלָיו יְהוָה בָּאֵשׁ
# וַיַּעַל עֲשָׁנוֹ כְּעֶשֶׁן הַכִּבְשָׁן וַיֶּחֱרַד כָּל־הָהָר מְאֹד
# "[EN-AID] And mount Sinai smoked, all of it, because the LORD descended on
# it in fire; and its smoke went up like the smoke of the kiln — and the
# whole mountain trembled exceedingly."
m.step("Exod.19.18")
# ‹וְהַר סִינַי עָשַׁן כֻּלּוֹ מִפְּנֵי אֲשֶׁר יָרַד עָלָיו יְהוָה בָּאֵשׁ›
# (“and-mountain Sinai smoke all-him/its from-face which go-down over-
# him/its YHWH in-fire”) — fact holds: and-mountain-Sinai-smoke-kulo
m.fact("ve_har_sinay_ashan_kulo")

# -------------------------- Exod.19.19 · VOICE_FOR_VOICE -------------------
# וַיְהִי קוֹל הַשּׁוֹפָר הוֹלֵךְ וְחָזֵק מְאֹד מֹשֶׁה יְדַבֵּר וְהָאֱלֹהִים
# יַעֲנֶנּוּ בְקוֹל
# "[EN-AID] And the voice of the shofar went on, going and strengthening
# exceedingly; Moses would speak — and God would answer him in a voice."
m.step("Exod.19.19")
# ‹מֹשֶׁה יְדַבֵּר וְהָאֱלֹהִים יַעֲנֶנּוּ בְקוֹל› (“Moses speak and-the-God
# eye-him/its in-voice/sound”) — fact holds: Moses-speak-and-the-God-yaanenu
m.fact("moshe_yedaber_ve_ha_elohim_yaanenu")

# -------------------------- Exod.19.20 · THE_DESCENT -----------------------
# וַיֵּרֶד יְהוָה עַל־הַר סִינַי אֶל־רֹאשׁ הָהָר וַיִּקְרָא יְהוָה לְמֹשֶׁה
# אֶל־רֹאשׁ הָהָר וַיַּעַל מֹשֶׁה
# "[EN-AID] And the LORD descended on mount Sinai, to the top of the
# mountain; and the LORD called Moses to the top of the mountain — and Moses
# went up."
m.step("Exod.19.20")
# ‹וַיֵּרֶד יְהוָה עַל־הַר סִינַי אֶל־רֹאשׁ הָהָר› (“and-go-down YHWH over
# mountain Sinai to head the-mountain”) — event: yeridat-the-LORD — agent
# the-LORD
m.event("yeridat_YHWH", agent="YHWH")

# -------------------------- Exod.19.21 · GO_DOWN_WARN ----------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה רֵד הָעֵד בָּעָם פֶּן־יֶהֶרְסוּ אֶל־יְהוָה
# לִרְאוֹת וְנָפַל מִמֶּנּוּ רָב
# "[EN-AID] And the LORD said to Moses: Go down, warn the people — lest they
# break through to the LORD to see, and many of them fall."
m.step("Exod.19.21")
# ‹רֵד הָעֵד בָּעָם› (“go-down duplicate in-people”) — the-LORD speaks a
# demand — LET: go-down-duplicate-come/bring-people
m.declare("YHWH", "LET",
          "red_haed_ba_am")

# -------------------------- Exod.19.22 · THE_PRIESTS_TOO -------------------
# וְגַם הַכֹּהֲנִים הַנִּגָּשִׁים אֶל־יְהוָה יִתְקַדָּשׁוּ פֶּן־יִפְרֹץ
# בָּהֶם יְהוָה
# "[EN-AID] And also the priests, who approach the LORD, shall sanctify
# themselves — lest the LORD break out against them."
m.step("Exod.19.22")
# ‹וְגַם הַכֹּהֲנִים הַנִּגָּשִׁים אֶל־יְהוָה יִתְקַדָּשׁוּ› (“and-also the-
# priest the-be to YHWH sanctify”) — fact holds: and-also-the-priest-
# sanctify
m.fact("ve_gam_ha_kohanim_yitqadashu")

# -------------------------- Exod.19.23 · THE_FENCE_STANDS ------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־יְהוָה לֹא־יוּכַל הָעָם לַעֲלֹת אֶל־הַר סִינָי
# כִּי־אַתָּה הַעֵדֹתָה בָּנוּ לֵאמֹר הַגְבֵּל אֶת־הָהָר וְקִדַּשְׁתּוֹ
# "[EN-AID] And Moses said to the LORD: The people cannot come up to mount
# Sinai — for You warned us, saying: Fence the mountain, and sanctify it."
m.step("Exod.19.23")
# ‹כִּי־אַתָּה הַעֵדֹתָה בָּנוּ לֵאמֹר הַגְבֵּל אֶת־הָהָר וְקִדַּשְׁתּוֹ›
# (“that you duplicate in-us/our to-say twist-as-arope obj-marker the-
# mountain and-sanctify-him/its”) — fact holds: not-be-able-the-people-to-
# go-up
m.fact("lo_yukhal_ha_am_la_alot")

# -------------------------- Exod.19.24 · BARRIERS_BY_RANK ------------------
# וַיֹּאמֶר אֵלָיו יְהוָה לֶךְ־רֵד וְעָלִיתָ אַתָּה וְאַהֲרֹן עִמָּךְ
# וְהַכֹּהֲנִים וְהָעָם אַל־יֶהֶרְסוּ לַעֲלֹת אֶל־יְהוָה פֶּן־יִפְרָץ־בָּם
# "[EN-AID] And the LORD said to him: Go, descend — and you shall come up,
# you and Aaron with you; and the priests and the people shall not break
# through to come up to the LORD, lest He break out against them."
m.step("Exod.19.24")
# ‹לֶךְ־רֵד וְעָלִיתָ אַתָּה וְאַהֲרֹן עִמָּךְ› (“go go-down and-go-up you
# and-Aaron with-you/your”) — fact holds: and-go-up-now-and-Aaron-imakh
m.fact("ve_alita_ata_ve_aharon_imakh")

# -------------------------- Exod.19.25 · AND_SAID_TO_THEM ------------------
# וַיֵּרֶד מֹשֶׁה אֶל־הָעָם וַיֹּאמֶר אֲלֵהֶם
# "[EN-AID] And Moses went down to the people — and said to them."
m.step("Exod.19.25")
# ‹וַיֵּרֶד מֹשֶׁה אֶל־הָעָם וַיֹּאמֶר אֲלֵהֶם› (“and-go-down Moses to the-
# people and-say to-them/their”) — demand settled (popped from the queue):
# go-down-duplicate-come/bring-people
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
