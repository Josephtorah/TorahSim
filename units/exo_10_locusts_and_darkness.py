#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_10_locusts_and_darkness — 10:1-29
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_10_locusts_and_darkness.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Locusts and darkness (10:1-29)"""
from machine import Machine

m = Machine("exo_10_locusts_and_darkness")

# -------------------------- Exod.10.1 · COME_FOR_I_HAVE_HARDENED -----------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה בֹּא אֶל־פַּרְעֹה כִּי־אֲנִי הִכְבַּדְתִּי
# אֶת־לִבּוֹ וְאֶת־לֵב עֲבָדָיו לְמַעַן שִׁתִי אֹתֹתַי אֵלֶּה בְּקִרְבּוֹ
# "[EN-AID] And the LORD said to Moses: Come to Pharaoh; for I have made his
# heart heavy, and the heart of his servants, in order to set these My signs
# in his midst."
m.step("Exod.10.1")
# ‹בֹּא אֶל־פַּרְעֹה› (“come/bring to Pharaoh”) — the-LORD speaks a demand —
# LET: come/bring-to-Pharaoh-locust
m.declare("YHWH", "LET",
          "bo_el_paro_arbe")

# -------------------------- Exod.10.2 · TELL_YOUR_SON ----------------------
# וּלְמַעַן תְּסַפֵּר בְּאָזְנֵי בִנְךָ וּבֶן־בִּנְךָ אֵת אֲשֶׁר
# הִתְעַלַּלְתִּי בְּמִצְרַיִם וְאֶת־אֹתֹתַי אֲשֶׁר־שַׂמְתִּי בָם
# וִידַעְתֶּם כִּי־אֲנִי יְהוָה
# "[EN-AID] And in order that you may tell in the ears of your son, and your
# son's son, how I dealt with Egypt, and My signs which I set among them —
# and you shall know that I am the LORD."
m.step("Exod.10.2")
# ‹וּלְמַעַן תְּסַפֵּר בְּאָזְנֵי בִנְךָ וּבֶן־בִּנְךָ› (“and-so-that count
# in-broadness.-i.e.-the-ear son-you/your and-son son-you/your”) — fact
# holds: so-that-count-in-ozne-binkha
m.fact("lemaan_tesaper_be_ozne_binkha")

# -------------------------- Exod.10.3 · THE_DELIVERY_ON_STAGE --------------
# וַיָּבֹא מֹשֶׁה וְאַהֲרֹן אֶל־פַּרְעֹה וַיֹּאמְרוּ אֵלָיו כֹּה־אָמַר
# יְהוָה אֱלֹהֵי הָעִבְרִים עַד־מָתַי מֵאַנְתָּ לֵעָנֹת מִפָּנָי שַׁלַּח
# עַמִּי וְיַעַבְדֻנִי
# "[EN-AID] And Moses and Aaron came to Pharaoh, and said to him: Thus says
# the LORD, the God of the Hebrews: How long have you refused to humble
# yourself before Me? Send My people, that they may serve Me."
m.step("Exod.10.3")
# ‹וַיָּבֹא מֹשֶׁה וְאַהֲרֹן אֶל־פַּרְעֹה› (“and-come/bring Moses and-Aaron
# to Pharaoh”) — demand settled (popped from the queue): come/bring-to-
# Pharaoh-locust
m.result("bo_el_paro_arbe", tmark="t1")

# -------------------------- Exod.10.4 · LOCUSTS_IN_YOUR_BORDER -------------
# כִּי אִם־מָאֵן אַתָּה לְשַׁלֵּחַ אֶת־עַמִּי הִנְנִי מֵבִיא מָחָר אַרְבֶּה
# בִּגְבֻלֶךָ
# "[EN-AID] For if you refuse to send My people — behold, tomorrow I bring
# locusts into your border."
m.step("Exod.10.4")
# ‹הִנְנִי מֵבִיא מָחָר אַרְבֶּה בִּגְבֻלֶךָ› (“lo!-me/my come/bring
# deferred locust in-cord-you/your”) — fact holds: behold-I-come/bring-
# deferred-locust
m.fact("hineni_mevi_machar_arbe")

# -------------------------- Exod.10.5 · THE_EYE_OF_THE_LAND ----------------
# וְכִסָּה אֶת־עֵין הָאָרֶץ וְלֹא יוּכַל לִרְאֹת אֶת־הָאָרֶץ וְאָכַל
# אֶת־יֶתֶר הַפְּלֵטָה הַנִּשְׁאֶרֶת לָכֶם מִן־הַבָּרָד וְאָכַל
# אֶת־כָּל־הָעֵץ הַצֹּמֵחַ לָכֶם מִן־הַשָּׂדֶה
# "[EN-AID] And it shall cover the eye of the land, and none shall be able
# to see the land; and it shall eat the remnant of what escaped, what
# remains to you from the hail, and shall eat every tree that sprouts for
# you from the field."
m.step("Exod.10.5")
# ‹וְכִסָּה אֶת־עֵין הָאָרֶץ וְלֹא› (“and-plump obj-marker eye the-earth
# and-not”) — fact holds: and-plump-obj-marker-eye-the-earth
m.fact("ve_khisa_et_en_ha_aretz")

# -------------------------- Exod.10.6 · YOUR_FATHERS_NEVER_SAW -------------
# וּמָלְאוּ בָתֶּיךָ וּבָתֵּי כָל־עֲבָדֶיךָ וּבָתֵּי כָל־מִצְרַיִם אֲשֶׁר
# לֹא־רָאוּ אֲבֹתֶיךָ וַאֲבוֹת אֲבֹתֶיךָ מִיּוֹם הֱיוֹתָם עַל־הָאֲדָמָה עַד
# הַיּוֹם הַזֶּה וַיִּפֶן וַיֵּצֵא מֵעִם פַּרְעֹה
# "[EN-AID] And your houses shall be filled, and the houses of all your
# servants, and the houses of all Egypt — such as your fathers and your
# fathers' fathers have not seen, from the day of their being on the ground
# until this day. And he turned, and went out from Pharaoh."
m.step("Exod.10.6")
# ‹רָאוּ אֲבֹתֶיךָ וַאֲבוֹת אֲבֹתֶיךָ מִיּוֹם› (“see father-you/your and-
# father father-you/your from-day”) — fact holds: which-not-see-avotekha
m.fact("asher_lo_rau_avotekha")

# -------------------------- Exod.10.7 · THE_SERVANTS_REVOLT ----------------
# וַיֹּאמְרוּ עַבְדֵי פַרְעֹה אֵלָיו עַד־מָתַי יִהְיֶה זֶה לָנוּ לְמוֹקֵשׁ
# שַׁלַּח אֶת־הָאֲנָשִׁים וְיַעַבְדוּ אֶת־יְהוָה אֱלֹהֵיהֶם הֲטֶרֶם תֵּדַע
# כִּי אָבְדָה מִצְרָיִם
# "[EN-AID] And the servants of Pharaoh said to him: How long shall this one
# be a snare to us? Send the men, that they may serve the LORD their God. Do
# you not yet know that Egypt is destroyed?"
m.step("Exod.10.7")
# ‹הֲטֶרֶם תֵּדַע כִּי אָבְדָה מִצְרָיִם› (“the-non-occurrence know that
# wander-away Egypt”) — fact holds: the-non-occurrence-know-that-wander-
# away-Egypt
m.fact("ha_terem_teda_ki_avda_mitzrayim")

# -------------------------- Exod.10.8 · WHO_AND_WHO_ARE_GOING --------------
# וַיּוּשַׁב אֶת־מֹשֶׁה וְאֶת־אַהֲרֹן אֶל־פַּרְעֹה וַיֹּאמֶר אֲלֵהֶם לְכוּ
# עִבְדוּ אֶת־יְהוָה אֱלֹהֵיכֶם מִי וָמִי הַהֹלְכִים
# "[EN-AID] And Moses and Aaron were brought back to Pharaoh, and he said to
# them: Go, serve the LORD your God — who and who are the ones going?"
m.step("Exod.10.8")
# ‹אֱלֹהֵיכֶם מִי וָמִי הַהֹלְכִים› (“God-you/your(pl) who? and-who? the-
# walk/go”) — fact holds: who?-and-who?-the-walk/go
m.fact("mi_va_mi_ha_holkhim")

# -------------------------- Exod.10.9 · WITH_OUR_YOUNG_AND_OLD -------------
# וַיֹּאמֶר מֹשֶׁה בִּנְעָרֵינוּ וּבִזְקֵנֵינוּ נֵלֵךְ בְּבָנֵינוּ
# וּבִבְנוֹתֵנוּ בְּצֹאנֵנוּ וּבִבְקָרֵנוּ נֵלֵךְ כִּי חַג־יְהוָה לָנוּ
# "[EN-AID] And Moses said: With our young and with our old we will go; with
# our sons and with our daughters, with our flocks and with our herds we
# will go — for it is the LORD's feast for us."
m.step("Exod.10.9")
# ‹כִּי חַג־יְהוָה לָנוּ› (“that festival YHWH to-us/our”) — fact holds:
# that-festival-the-LORD-lanu
m.fact("ki_chag_YHWH_lanu")

# -------------------------- Exod.10.10 · THE_BLOOD_STAR --------------------
# וַיֹּאמֶר אֲלֵהֶם יְהִי כֵן יְהוָה עִמָּכֶם כַּאֲשֶׁר אֲשַׁלַּח אֶתְכֶם
# וְאֶת־טַפְּכֶם רְאוּ כִּי רָעָה נֶגֶד פְּנֵיכֶם
# "[EN-AID] And he said to them: So be the LORD with you, as I send you and
# your little ones — see, for evil is before your faces."
m.step("Exod.10.10")
# ‹רְאוּ כִּי רָעָה נֶגֶד פְּנֵיכֶם› (“see that bad front face-
# you/your(pl)”) — fact holds: see-that-bad-front-penekhem
m.fact("reu_ki_raa_neged_penekhem")

# -------------------------- Exod.10.11 · THE_EXPULSION ---------------------
# לֹא כֵן לְכוּ־נָא הַגְּבָרִים וְעִבְדוּ אֶת־יְהוָה כִּי אֹתָהּ אַתֶּם
# מְבַקְשִׁים וַיְגָרֶשׁ אֹתָם מֵאֵת פְּנֵי פַרְעֹה
# "[EN-AID] Not so — go now, you men, and serve the LORD, for that is what
# you are seeking. And they were driven out from before Pharaoh."
m.step("Exod.10.11")
# ‹וַיְגָרֶשׁ אֹתָם מֵאֵת פְּנֵי› (“and-drive-out-from-a-possession obj-
# marker-them/their from-with face”) — event: gerush
m.event("gerush")

# -------------------------- Exod.10.12 · STRETCH_FOR_THE_LOCUSTS -----------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה נְטֵה יָדְךָ עַל־אֶרֶץ מִצְרַיִם בָּאַרְבֶּה
# וְיַעַל עַל־אֶרֶץ מִצְרָיִם וְיֹאכַל אֶת־כָּל־עֵשֶׂב הָאָרֶץ אֵת
# כָּל־אֲשֶׁר הִשְׁאִיר הַבָּרָד
# "[EN-AID] And the LORD said to Moses: Stretch out your hand over the land
# of Egypt for the locusts, that they may come up over the land of Egypt,
# and eat every herb of the land — all that the hail left."
m.step("Exod.10.12")
# ‹נְטֵה יָדְךָ עַל־אֶרֶץ מִצְרַיִם› (“stretch hand-you/your over earth
# Egypt”) — the-LORD speaks a demand — LET: stretch-yadkha-in-the-locust
m.declare("YHWH", "LET",
          "nete_yadkha_ba_arbe")

# -------------------------- Exod.10.13 · THE_EAST_WIND ---------------------
# וַיֵּט מֹשֶׁה אֶת־מַטֵּהוּ עַל־אֶרֶץ מִצְרַיִם וַיהוָה נִהַג רוּחַ קָדִים
# בָּאָרֶץ כָּל־הַיּוֹם הַהוּא וְכָל־הַלָּיְלָה הַבֹּקֶר הָיָה וְרוּחַ
# הַקָּדִים נָשָׂא אֶת־הָאַרְבֶּה
# "[EN-AID] And Moses stretched out his staff over the land of Egypt, and
# the LORD drove an east wind through the land all that day and all the
# night; the morning came — and the east wind had borne the locusts."
m.step("Exod.10.13")
# ‹וַיהוָה נִהַג רוּחַ קָדִים› (“and-YHWH drive-forth spirit east-wind”) —
# demand settled (popped from the queue): stretch-yadkha-in-the-locust
m.result("nete_yadkha_ba_arbe", tmark="t1")

# -------------------------- Exod.10.14 · THE_LOCUST_RESTS ------------------
# וַיַּעַל הָאַרְבֶּה עַל כָּל־אֶרֶץ מִצְרַיִם וַיָּנַח בְּכֹל גְּבוּל
# מִצְרָיִם כָּבֵד מְאֹד לְפָנָיו לֹא־הָיָה כֵן אַרְבֶּה כָּמֹהוּ וְאַחֲרָיו
# לֹא יִהְיֶה־כֵּן
# "[EN-AID] And the locust came up over all the land of Egypt, and rested in
# all the border of Egypt — very heavy: before it there was no locust like
# it, and after it there shall be none such."
m.step("Exod.10.14")
# ‹וַיָּנַח בְּכֹל גְּבוּל מִצְרָיִם› (“and-rest in-all cord Egypt”) — fact
# holds: and-rest-in-all-cord
m.fact("va_yanach_be_khol_gevul")

# -------------------------- Exod.10.15 · NOTHING_GREEN ---------------------
# וַיְכַס אֶת־עֵין כָּל־הָאָרֶץ וַתֶּחְשַׁךְ הָאָרֶץ וַיֹּאכַל
# אֶת־כָּל־עֵשֶׂב הָאָרֶץ וְאֵת כָּל־פְּרִי הָעֵץ אֲשֶׁר הוֹתִיר הַבָּרָד
# וְלֹא־נוֹתַר כָּל־יֶרֶק בָּעֵץ וּבְעֵשֶׂב הַשָּׂדֶה בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And it covered the eye of all the land, and the land was
# darkened; and it ate every herb of the land and all the fruit of the trees
# which the hail had left; and nothing green was left in the tree or in the
# herb of the field in all the land of Egypt."
m.step("Exod.10.15")
# ‹וַיְכַס אֶת־עֵין כָּל־הָאָרֶץ וַתֶּחְשַׁךְ הָאָרֶץ› (“and-plump obj-
# marker eye all the-earth and-be-dark the-earth”) — fact holds: and-be-
# dark-the-earth
m.fact("va_techshakh_ha_aretz")

# -------------------------- Exod.10.16 · I_HAVE_SINNED_AGAINST_BOTH --------
# וַיְמַהֵר פַּרְעֹה לִקְרֹא לְמֹשֶׁה וּלְאַהֲרֹן וַיֹּאמֶר חָטָאתִי לַיהוָה
# אֱלֹהֵיכֶם וְלָכֶם
# "[EN-AID] And Pharaoh hurried to call for Moses and for Aaron; and he
# said: I have sinned against the LORD your God, and against you."
m.step("Exod.10.16")
# ‹וַיֹּאמֶר חָטָאתִי לַיהוָה אֱלֹהֵיכֶם וְלָכֶם› (“and-say sin to-YHWH God-
# you/your(pl) and-to-you/your(pl)”) — fact holds: sin-to-the-LORD-and-
# lakhem
m.fact("chatati_la_YHWH_ve_lakhem")

# -------------------------- Exod.10.17 · REMOVE_THIS_DEATH -----------------
# וְעַתָּה שָׂא נָא חַטָּאתִי אַךְ הַפַּעַם וְהַעְתִּירוּ לַיהוָה אֱלֹהֵיכֶם
# וְיָסֵר מֵעָלַי רַק אֶת־הַמָּוֶת הַזֶּה
# "[EN-AID] And now, forgive, pray, my sin only this once, and entreat the
# LORD your God, that He remove from me only this death."
m.step("Exod.10.17")
# ‹וְיָסֵר מֵעָלַי רַק אֶת־הַמָּוֶת הַזֶּה› (“and-turn-aside from-over-me/my
# leanness obj-marker the-death the-this”) — Pharaoh speaks a demand — LET:
# burn-incense-in-worship-4
m.declare("paro", "LET",
          "hatiru_4")

# -------------------------- Exod.10.18 · THE_NAMELESS_EXIT -----------------
# וַיֵּצֵא מֵעִם פַּרְעֹה וַיֶּעְתַּר אֶל־יְהוָה
# "[EN-AID] And he went out from Pharaoh, and entreated the LORD."
m.step("Exod.10.18")
# ‹וַיֵּצֵא מֵעִם פַּרְעֹה› (“and-bring-forth from-with Pharaoh”) — demand
# settled (popped from the queue): burn-incense-in-worship-4
m.result("hatiru_4", tmark="t1")

# -------------------------- Exod.10.19 · INTO_THE_REED_SEA -----------------
# וַיַּהֲפֹךְ יְהוָה רוּחַ־יָם חָזָק מְאֹד וַיִּשָּׂא אֶת־הָאַרְבֶּה
# וַיִּתְקָעֵהוּ יָמָּה סּוּף לֹא נִשְׁאַר אַרְבֶּה אֶחָד בְּכֹל גְּבוּל
# מִצְרָיִם
# "[EN-AID] And the LORD turned a very strong sea-wind, and it bore the
# locusts and thrust them into the Reed Sea; not one locust was left in all
# the border of Egypt."
m.step("Exod.10.19")
# ‹נִשְׁאַר אַרְבֶּה אֶחָד בְּכֹל› (“swell-up locust one in-all”) — fact
# holds: and-yitqaehu-yama-reed
m.fact("va_yitqaehu_yama_suf")

# -------------------------- Exod.10.20 · HARDENED_AGAIN --------------------
# וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה וְלֹא שִׁלַּח אֶת־בְּנֵי יִשְׂרָאֵל
# "[EN-AID] And the LORD strengthened Pharaoh's heart, and he did not send
# the sons of Israel."
m.step("Exod.10.20")
# ‹וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה› (“and-fasten-upon YHWH obj-marker
# heart Pharaoh”) — fact holds: and-fasten-upon-2
m.fact("va_yechazeq_2")

# -------------------------- Exod.10.21 · DARKNESS_THAT_IS_FELT -------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה נְטֵה יָדְךָ עַל־הַשָּׁמַיִם וִיהִי חֹשֶׁךְ
# עַל־אֶרֶץ מִצְרָיִם וְיָמֵשׁ חֹשֶׁךְ
# "[EN-AID] And the LORD said to Moses: Stretch out your hand toward heaven,
# and there shall be darkness over the land of Egypt — and the darkness
# shall be felt."
m.step("Exod.10.21")
# ‹חֹשֶׁךְ עַל־אֶרֶץ מִצְרָיִם וְיָמֵשׁ חֹשֶׁךְ› (“darkness over earth Egypt
# and-feel-of darkness”) — the-LORD speaks a demand — LET: stretch-yadkha-
# darkness
m.declare("YHWH", "LET",
          "nete_yadkha_choshekh")

# -------------------------- Exod.10.22 · THREE_DAYS_OF_DARK ----------------
# וַיֵּט מֹשֶׁה אֶת־יָדוֹ עַל־הַשָּׁמָיִם וַיְהִי חֹשֶׁךְ־אֲפֵלָה
# בְּכָל־אֶרֶץ מִצְרַיִם שְׁלֹשֶׁת יָמִים
# "[EN-AID] And Moses stretched out his hand toward heaven; and there was
# thick darkness in all the land of Egypt three days."
m.step("Exod.10.22")
# ‹וַיְהִי חֹשֶׁךְ־אֲפֵלָה בְּכָל־אֶרֶץ מִצְרַיִם שְׁלֹשֶׁת יָמִים› (“and-be
# darkness duskiness in-all earth Egypt three day”) — demand settled (popped
# from the queue): stretch-yadkha-darkness
m.result("nete_yadkha_choshekh", tmark="t1")

# -------------------------- Exod.10.23 · LIGHT_IN_THE_DWELLINGS ------------
# לֹא־רָאוּ אִישׁ אֶת־אָחִיו וְלֹא־קָמוּ אִישׁ מִתַּחְתָּיו שְׁלֹשֶׁת יָמִים
# וּלְכָל־בְּנֵי יִשְׂרָאֵל הָיָה אוֹר בְּמוֹשְׁבֹתָם
# "[EN-AID] No man saw his brother, nor did any man rise from his place,
# three days; but for all the sons of Israel there was light in their
# dwellings."
m.step("Exod.10.23")
# ‹וּלְכָל־בְּנֵי יִשְׂרָאֵל הָיָה אוֹר בְּמוֹשְׁבֹתָם› (“and-to-all son
# Israel be light in-seat-them/their”) — fact holds: light-in-moshvotam
m.fact("or_be_moshvotam")

# -------------------------- Exod.10.24 · ONLY_YOUR_FLOCKS_STAY -------------
# וַיִּקְרָא פַרְעֹה אֶל־מֹשֶׁה וַיֹּאמֶר לְכוּ עִבְדוּ אֶת־יְהוָה רַק
# צֹאנְכֶם וּבְקַרְכֶם יֻצָּג גַּם־טַפְּכֶם יֵלֵךְ עִמָּכֶם
# "[EN-AID] And Pharaoh called to Moses, and said: Go, serve the LORD — only
# your flocks and your herds shall be held back; your little ones shall also
# go with you."
m.step("Exod.10.24")
# ‹לְכוּ עִבְדוּ אֶת־יְהוָה רַק צֹאנְכֶם וּבְקַרְכֶם יֻצָּג› (“go work/serve
# obj-marker YHWH leanness flock-you/your(pl) and-herd-you/your(pl) place-
# permanently”) — Pharaoh speaks a demand — LET: go-leanness-tzonkhem-place-
# permanently
m.declare("paro", "LET",
          "lekhu_raq_tzonkhem_yutzag")

# -------------------------- Exod.10.25 · YOU_YOURSELF_WILL_GIVE ------------
# וַיֹּאמֶר מֹשֶׁה גַּם־אַתָּה תִּתֵּן בְּיָדֵנוּ זְבָחִים וְעֹלוֹת
# וְעָשִׂינוּ לַיהוָה אֱלֹהֵינוּ
# "[EN-AID] And Moses said: You yourself will also give into our hand
# sacrifices and burnt-offerings, and we will offer them to the LORD our
# God."
m.step("Exod.10.25")
# ‹גַּם־אַתָּה תִּתֵּן בְּיָדֵנוּ זְבָחִים וְעֹלוֹת› (“also you set in-hand-
# us/our sacrifice and-burnt-offering”) — fact holds: also-you-set-in-our-
# hands
m.fact("gam_ata_titen_be_yadenu")

# -------------------------- Exod.10.26 · NOT_A_HOOF ------------------------
# וְגַם־מִקְנֵנוּ יֵלֵךְ עִמָּנוּ לֹא תִשָּׁאֵר פַּרְסָה כִּי מִמֶּנּוּ
# נִקַּח לַעֲבֹד אֶת־יְהוָה אֱלֹהֵינוּ וַאֲנַחְנוּ לֹא־נֵדַע מַה־נַּעֲבֹד
# אֶת־יְהוָה עַד־בֹּאֵנוּ שָׁמָּה
# "[EN-AID] And our cattle shall also go with us — not a hoof shall be left
# — for from it we must take to serve the LORD our God; and we do not know
# with what we shall serve the LORD until we come there."
m.step("Exod.10.26")
# ‹לֹא תִשָּׁאֵר פַּרְסָה› (“not swell-up claw”) — fact holds: not-swell-up-
# claw
m.fact("lo_tishaer_parsa")

# -------------------------- Exod.10.27 · NOT_WILLING -----------------------
# וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה וְלֹא אָבָה לְשַׁלְּחָם
# "[EN-AID] And the LORD strengthened Pharaoh's heart, and he was not
# willing to send them."
m.step("Exod.10.27")
# ‹וְלֹא אָבָה לְשַׁלְּחָם› (“and-not breathe-after to-send-them/their”) —
# fact holds: and-not-breathe-after-to-shalcham
m.fact("ve_lo_ava_le_shalcham")

# -------------------------- Exod.10.28 · SEE_MY_FACE_NO_MORE ---------------
# וַיֹּאמֶר־לוֹ פַרְעֹה לֵךְ מֵעָלָי הִשָּׁמֶר לְךָ אֶל־תֹּסֶף רְאוֹת פָּנַי
# כִּי בְּיוֹם רְאֹתְךָ פָנַי תָּמוּת
# "[EN-AID] And Pharaoh said to him: Go from me! Guard yourself — do not
# again see my face, for on the day you see my face you shall die."
m.step("Exod.10.28")
# ‹מֵעָלָי הִשָּׁמֶר לְךָ אֶל־תֹּסֶף› (“from-over-me/my keep/guard to-
# you/your do-not add”) — Pharaoh speaks a demand — LET: over-add-see-panai
m.declare("paro", "LET",
          "al_tosef_reot_panai")

# -------------------------- Exod.10.29 · I_WILL_NOT_AGAIN ------------------
# וַיֹּאמֶר מֹשֶׁה כֵּן דִּבַּרְתָּ לֹא־אֹסִף עוֹד רְאוֹת פָּנֶיךָ
# "[EN-AID] And Moses said: You have spoken well — I will not again see your
# face."
m.step("Exod.10.29")
# ‹דִּבַּרְתָּ לֹא־אֹסִף עוֹד רְאוֹת פָּנֶיךָ› (“speak not add still/again
# see face-you/your”) — demand settled (popped from the queue): over-add-
# see-panai
m.result("al_tosef_reot_panai", tmark="t1")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['lekhu_raq_tzonkhem_yutzag']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['lemaan_tesaper_be_ozne_binkha', 'hineni_mevi_machar_arbe', 've_khisa_et_en_ha_aretz', 'asher_lo_rau_avotekha', 'ha_terem_teda_ki_avda_mitzrayim', 'mi_va_mi_ha_holkhim', 'ki_chag_YHWH_lanu', 'reu_ki_raa_neged_penekhem', 'va_yanach_be_khol_gevul', 'va_techshakh_ha_aretz', 'chatati_la_YHWH_ve_lakhem', 'va_yitqaehu_yama_suf', 'va_yechazeq_2', 'or_be_moshvotam', 'gam_ata_titen_be_yadenu', 'lo_tishaer_parsa', 've_lo_ava_le_shalcham'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
