#!/usr/bin/env python3
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
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹בֹּא אֶל־פַּרְעֹה כִּי־אֲנִי› (“come/bring to Pharaoh that”)
# ‹הִכְבַּדְתִּי אֶת־לִבּוֹ וְאֶת־לֵב› (“be-heavy obj-marker heart-him/its
# and-obj-marker heart”)
# ‹עֲבָדָיו לְמַעַן שִׁתִי› (“servant-him/its so-that place-me/my”)
# ‹אֹתֹתַי אֵלֶּה בְּקִרְבּוֹ› (“signs-me/my these in-nearest-part-him/its”)
# "[EN-AID] And the LORD said to Moses: Come to Pharaoh; for I have made his
# heart heavy, and the heart of his servants, in order to set these My signs
# in his midst."
m.step("Exod.10.1")
# ‹בֹּא אֶל־פַּרְעֹה› (“come/bring to Pharaoh”)
# — the-LORD speaks a demand — LET: come/bring-to-Pharaoh-locust
m.declare("YHWH", "LET",
          "bo_el_paro_arbe")

# -------------------------- Exod.10.2 · TELL_YOUR_SON ----------------------
# ‹וּלְמַעַן תְּסַפֵּר בְּאָזְנֵי› (“and-so-that count in-
# broadness.-i.e.-the-ear”)
# ‹בִנְךָ וּבֶן־בִּנְךָ אֵת› (“son-you/your and-son son-you/your obj-
# marker”)
# ‹אֲשֶׁר הִתְעַלַּלְתִּי בְּמִצְרַיִם› (“which effect-thoroughly in-Egypt”)
# ‹וְאֶת־אֹתֹתַי אֲשֶׁר־שַׂמְתִּי בָם› (“and-obj-marker signs-me/my which
# put/set in-them/their”)
# ‹וִידַעְתֶּם כִּי־אֲנִי יְהוָה› (“and-know that YHWH”)
# "[EN-AID] And in order that you may tell in the ears of your son, and your
# son's son, how I dealt with Egypt, and My signs which I set among them —
# and you shall know that I am the LORD."
m.step("Exod.10.2")
# ‹וּלְמַעַן תְּסַפֵּר בְּאָזְנֵי› (“and-so-that count in-
# broadness.-i.e.-the-ear”)
# ‹בִנְךָ וּבֶן־בִּנְךָ› (“son-you/your and-son son-you/your”)
# — fact holds: so-that-count-in-ozne-binkha
m.fact("lemaan_tesaper_be_ozne_binkha")

# -------------------------- Exod.10.3 · THE_DELIVERY_ON_STAGE --------------
# ‹וַיָּבֹא מֹשֶׁה וְאַהֲרֹן› (“and-come/bring Moses and-Aaron”)
# ‹אֶל־פַּרְעֹה וַיֹּאמְרוּ אֵלָיו› (“to Pharaoh and-say to-him/its”)
# ‹כֹּה־אָמַר יְהוָה אֱלֹהֵי› (“like-this say YHWH God”)
# ‹הָעִבְרִים עַד־מָתַי מֵאַנְתָּ› (“the-Hebrew until extent refuse”)
# ‹לֵעָנֹת מִפָּנָי שַׁלַּח› (“to-afflict-literally from-face-me/my send”)
# ‹עַמִּי וְיַעַבְדֻנִי› (“people-me/my and-work/serve-me/my”)
# "[EN-AID] And Moses and Aaron came to Pharaoh, and said to him: Thus says
# the LORD, the God of the Hebrews: How long have you refused to humble
# yourself before Me? Send My people, that they may serve Me."
m.step("Exod.10.3")
# ‹וַיָּבֹא מֹשֶׁה וְאַהֲרֹן› (“and-come/bring Moses and-Aaron”)
# ‹אֶל־פַּרְעֹה› (“to Pharaoh”)
# — demand settled (popped from the queue): come/bring-to-Pharaoh-locust
m.result("bo_el_paro_arbe", tmark="t1")

# -------------------------- Exod.10.4 · LOCUSTS_IN_YOUR_BORDER -------------
# ‹כִּי אִם־מָאֵן אַתָּה› (“very-widely-used-as-a-relati as-demonstrative
# unwilling you”)
# ‹לְשַׁלֵּחַ אֶת־עַמִּי הִנְנִי› (“to-send obj-marker people-me/my
# lo!-me/my”)
# ‹מֵבִיא מָחָר אַרְבֶּה› (“come/bring deferred locust”)
# ‹בִּגְבֻלֶךָ› (“in-cord-you/your”)
# "[EN-AID] For if you refuse to send My people — behold, tomorrow I bring
# locusts into your border."
m.step("Exod.10.4")
# ‹הִנְנִי מֵבִיא מָחָר› (“lo!-me/my come/bring deferred”)
# ‹אַרְבֶּה בִּגְבֻלֶךָ› (“locust in-cord-you/your”)
# — fact holds: behold-I-come/bring-deferred-locust
m.fact("hineni_mevi_machar_arbe")

# -------------------------- Exod.10.5 · THE_EYE_OF_THE_LAND ----------------
# ‹וְכִסָּה אֶת־עֵין הָאָרֶץ› (“and-plump obj-marker eye the-earth”)
# ‹וְלֹא יוּכַל לִרְאֹת› (“and-not be-able to-see”)
# ‹אֶת־הָאָרֶץ וְאָכַל אֶת־יֶתֶר› (“obj-marker the-earth and-eat obj-marker
# overhanging”)
# ‹הַפְּלֵטָה הַנִּשְׁאֶרֶת לָכֶם› (“the-deliverance the-swell-up to-
# you/your(pl)”)
# ‹מִן־הַבָּרָד וְאָכַל אֶת־כָּל־הָעֵץ› (“from the-hail and-eat obj-marker
# all the-tree”)
# ‹הַצֹּמֵחַ לָכֶם מִן־הַשָּׂדֶה› (“the-sprout to-you/your(pl) from the-
# field”)
# "[EN-AID] And it shall cover the eye of the land, and none shall be able
# to see the land; and it shall eat the remnant of what escaped, what
# remains to you from the hail, and shall eat every tree that sprouts for
# you from the field."
m.step("Exod.10.5")
# ‹וְכִסָּה אֶת־עֵין הָאָרֶץ› (“and-plump obj-marker eye the-earth”)
# ‹וְלֹא› (“and-not”)
# — fact holds: and-plump-obj-marker-eye-the-earth
m.fact("ve_khisa_et_en_ha_aretz")

# -------------------------- Exod.10.6 · YOUR_FATHERS_NEVER_SAW -------------
# ‹וּמָלְאוּ בָתֶּיךָ וּבָתֵּי› (“and-fill house-you/your and-house”)
# ‹כָל־עֲבָדֶיךָ וּבָתֵּי כָל־מִצְרַיִם› (“all servant-you/your and-house
# all Egyptian”)
# ‹אֲשֶׁר לֹא־רָאוּ אֲבֹתֶיךָ› (“which not see father-you/your”)
# ‹וַאֲבוֹת אֲבֹתֶיךָ מִיּוֹם› (“and-father father-you/your from-day”)
# ‹הֱיוֹתָם עַל־הָאֲדָמָה עַד› (“be-them/their over the-ground until”)
# ‹הַיּוֹם הַזֶּה וַיִּפֶן› (“the-day the-this and-turn”)
# ‹וַיֵּצֵא מֵעִם פַּרְעֹה› (“and-bring-forth from-with Pharaoh”)
# "[EN-AID] And your houses shall be filled, and the houses of all your
# servants, and the houses of all Egypt — such as your fathers and your
# fathers' fathers have not seen, from the day of their being on the ground
# until this day. And he turned, and went out from Pharaoh."
m.step("Exod.10.6")
# ‹רָאוּ אֲבֹתֶיךָ וַאֲבוֹת› (“see father-you/your and-father”)
# ‹אֲבֹתֶיךָ מִיּוֹם› (“father-you/your from-day”)
# — fact holds: which-not-see-avotekha
m.fact("asher_lo_rau_avotekha")

# -------------------------- Exod.10.7 · THE_SERVANTS_REVOLT ----------------
# ‹וַיֹּאמְרוּ עַבְדֵי פַרְעֹה› (“and-say servant Pharaoh”)
# ‹אֵלָיו עַד־מָתַי יִהְיֶה› (“to-him/its until extent be”)
# ‹זֶה לָנוּ לְמוֹקֵשׁ› (“this to-us/our to-noose”)
# ‹שַׁלַּח אֶת־הָאֲנָשִׁים וְיַעַבְדוּ› (“send obj-marker the-man and-
# work/serve”)
# ‹אֶת־יְהוָה אֱלֹהֵיהֶם הֲטֶרֶם› (“obj-marker YHWH God-them/their the-non-
# occurrence”)
# ‹תֵּדַע כִּי אָבְדָה› (“know that wander-away”)
# ‹מִצְרָיִם› (“Egypt”)
# "[EN-AID] And the servants of Pharaoh said to him: How long shall this one
# be a snare to us? Send the men, that they may serve the LORD their God. Do
# you not yet know that Egypt is destroyed?"
m.step("Exod.10.7")
# ‹הֲטֶרֶם תֵּדַע כִּי› (“the-non-occurrence know that”)
# ‹אָבְדָה מִצְרָיִם› (“wander-away Egypt”)
# — fact holds: the-non-occurrence-know-that-wander-away-Egypt
m.fact("ha_terem_teda_ki_avda_mitzrayim")

# -------------------------- Exod.10.8 · WHO_AND_WHO_ARE_GOING --------------
# ‹וַיּוּשַׁב אֶת־מֹשֶׁה וְאֶת־אַהֲרֹן› (“and-return obj-marker Moses and-
# obj-marker Aaron”)
# ‹אֶל־פַּרְעֹה וַיֹּאמֶר אֲלֵהֶם› (“to Pharaoh and-say to-them/their”)
# ‹לְכוּ עִבְדוּ אֶת־יְהוָה› (“go work/serve obj-marker YHWH”)
# ‹אֱלֹהֵיכֶם מִי וָמִי› (“God-you/your(pl) who? and-who?”)
# ‹הַהֹלְכִים› (“the-walk/go”)
# "[EN-AID] And Moses and Aaron were brought back to Pharaoh, and he said to
# them: Go, serve the LORD your God — who and who are the ones going?"
m.step("Exod.10.8")
# ‹אֱלֹהֵיכֶם מִי וָמִי› (“God-you/your(pl) who? and-who?”)
# ‹הַהֹלְכִים› (“the-walk/go”)
# — fact holds: who?-and-who?-the-walk/go
m.fact("mi_va_mi_ha_holkhim")

# -------------------------- Exod.10.9 · WITH_OUR_YOUNG_AND_OLD -------------
# ‹וַיֹּאמֶר מֹשֶׁה בִּנְעָרֵינוּ› (“and-say Moses in-boy-us/our”)
# ‹וּבִזְקֵנֵינוּ נֵלֵךְ בְּבָנֵינוּ› (“and-in-old-us/our go in-son-us/our”)
# ‹וּבִבְנוֹתֵנוּ בְּצֹאנֵנוּ וּבִבְקָרֵנוּ› (“and-in-daughter-us/our in-
# flock-us/our and-in-herd-us/our”)
# ‹נֵלֵךְ כִּי חַג־יְהוָה› (“go that festival YHWH”)
# ‹לָנוּ› (“to-us/our”)
# "[EN-AID] And Moses said: With our young and with our old we will go; with
# our sons and with our daughters, with our flocks and with our herds we
# will go — for it is the LORD's feast for us."
m.step("Exod.10.9")
# ‹כִּי חַג־יְהוָה לָנוּ› (“that festival YHWH to-us/our”)
# — fact holds: that-festival-the-LORD-lanu
m.fact("ki_chag_YHWH_lanu")

# -------------------------- Exod.10.10 · THE_BLOOD_STAR --------------------
# ‹וַיֹּאמֶר אֲלֵהֶם יְהִי› (“and-say to-them/their be”)
# ‹כֵן יְהוָה עִמָּכֶם› (“so YHWH with-you/your(pl)”)
# ‹כַּאֲשֶׁר אֲשַׁלַּח אֶתְכֶם› (“like-as/which send obj-marker-
# you/your(pl)”)
# ‹וְאֶת־טַפְּכֶם רְאוּ כִּי› (“and-obj-marker family-you/your(pl) see
# that”)
# ‹רָעָה נֶגֶד פְּנֵיכֶם› (“bad front face-you/your(pl)”)
# "[EN-AID] And he said to them: So be the LORD with you, as I send you and
# your little ones — see, for evil is before your faces."
m.step("Exod.10.10")
# ‹רְאוּ כִּי רָעָה› (“see that bad”)
# ‹נֶגֶד פְּנֵיכֶם› (“front face-you/your(pl)”)
# — fact holds: see-that-bad-front-penekhem
m.fact("reu_ki_raa_neged_penekhem")

# -------------------------- Exod.10.11 · THE_EXPULSION ---------------------
# ‹לֹא כֵן לְכוּ־נָא› (“not so go please”)
# ‹הַגְּבָרִים וְעִבְדוּ אֶת־יְהוָה› (“the-valiant-man and-work/serve obj-
# marker YHWH”)
# ‹כִּי אֹתָהּ אַתֶּם› (“that obj-marker-her/its you”)
# ‹מְבַקְשִׁים וַיְגָרֶשׁ אֹתָם› (“search-out and-drive-out-from-a-
# possession obj-marker-them/their”)
# ‹מֵאֵת פְּנֵי פַרְעֹה› (“from-with face Pharaoh”)
# "[EN-AID] Not so — go now, you men, and serve the LORD, for that is what
# you are seeking. And they were driven out from before Pharaoh."
m.step("Exod.10.11")
# ‹וַיְגָרֶשׁ אֹתָם מֵאֵת› (“and-drive-out-from-a-possession obj-marker-
# them/their from-with”)
# ‹פְּנֵי› (“face”)
# — event: gerush
m.event("gerush")

# -------------------------- Exod.10.12 · STRETCH_FOR_THE_LOCUSTS -----------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹נְטֵה יָדְךָ עַל־אֶרֶץ› (“stretch hand-you/your over earth”)
# ‹מִצְרַיִם בָּאַרְבֶּה וְיַעַל› (“Egypt in-locust and-go-up”)
# ‹עַל־אֶרֶץ מִצְרָיִם וְיֹאכַל› (“over earth Egypt and-eat”)
# ‹אֶת־כָּל־עֵשֶׂב הָאָרֶץ אֵת› (“obj-marker all herb the-earth obj-marker”)
# ‹כָּל־אֲשֶׁר הִשְׁאִיר הַבָּרָד› (“all which swell-up the-hail”)
# "[EN-AID] And the LORD said to Moses: Stretch out your hand over the land
# of Egypt for the locusts, that they may come up over the land of Egypt,
# and eat every herb of the land — all that the hail left."
m.step("Exod.10.12")
# ‹נְטֵה יָדְךָ עַל־אֶרֶץ› (“stretch hand-you/your over earth”)
# ‹מִצְרַיִם› (“Egypt”)
# — the-LORD speaks a demand — LET: stretch-yadkha-in-the-locust
m.declare("YHWH", "LET",
          "nete_yadkha_ba_arbe")

# -------------------------- Exod.10.13 · THE_EAST_WIND ---------------------
# ‹וַיֵּט מֹשֶׁה אֶת־מַטֵּהוּ› (“and-stretch Moses obj-marker staff/tribe-
# him/its”)
# ‹עַל־אֶרֶץ מִצְרַיִם וַיהוָה› (“over earth Egypt and-YHWH”)
# ‹נִהַג רוּחַ קָדִים› (“drive-forth spirit east-wind”)
# ‹בָּאָרֶץ כָּל־הַיּוֹם הַהוּא› (“in-earth all the-day that”)
# ‹וְכָל־הַלָּיְלָה הַבֹּקֶר הָיָה› (“and-all the-night the-morning be”)
# ‹וְרוּחַ הַקָּדִים נָשָׂא› (“and-spirit the-east lift/carry”)
# ‹אֶת־הָאַרְבֶּה› (“obj-marker the-locust”)
# "[EN-AID] And Moses stretched out his staff over the land of Egypt, and
# the LORD drove an east wind through the land all that day and all the
# night; the morning came — and the east wind had borne the locusts."
m.step("Exod.10.13")
# ‹וַיהוָה נִהַג רוּחַ› (“and-YHWH drive-forth spirit”)
# ‹קָדִים› (“east-wind”)
# — demand settled (popped from the queue): stretch-yadkha-in-the-locust
m.result("nete_yadkha_ba_arbe", tmark="t1")

# -------------------------- Exod.10.14 · THE_LOCUST_RESTS ------------------
# ‹וַיַּעַל הָאַרְבֶּה עַל› (“and-go-up the-locust over”)
# ‹כָּל־אֶרֶץ מִצְרַיִם וַיָּנַח› (“all earth Egypt and-rest”)
# ‹בְּכֹל גְּבוּל מִצְרָיִם› (“in-all cord Egypt”)
# ‹כָּבֵד מְאֹד לְפָנָיו› (“heavy very to-face-him/its”)
# ‹לֹא־הָיָה כֵן אַרְבֶּה› (“not be so locust”)
# ‹כָּמֹהוּ וְאַחֲרָיו לֹא› (“form-of-the-prefix-'k-'-him/its and-after-
# him/its not”)
# ‹יִהְיֶה־כֵּן› (“be so”)
# "[EN-AID] And the locust came up over all the land of Egypt, and rested in
# all the border of Egypt — very heavy: before it there was no locust like
# it, and after it there shall be none such."
m.step("Exod.10.14")
# ‹וַיָּנַח בְּכֹל גְּבוּל› (“and-rest in-all cord”)
# ‹מִצְרָיִם› (“Egypt”)
# — fact holds: and-rest-in-all-cord
m.fact("va_yanach_be_khol_gevul")

# -------------------------- Exod.10.15 · NOTHING_GREEN ---------------------
# ‹וַיְכַס אֶת־עֵין כָּל־הָאָרֶץ› (“and-plump obj-marker eye all the-earth”)
# ‹וַתֶּחְשַׁךְ הָאָרֶץ וַיֹּאכַל› (“and-be-dark the-earth and-eat”)
# ‹אֶת־כָּל־עֵשֶׂב הָאָרֶץ וְאֵת› (“obj-marker all herb the-earth and-obj-
# marker”)
# ‹כָּל־פְּרִי הָעֵץ אֲשֶׁר› (“all fruit the-tree which”)
# ‹הוֹתִיר הַבָּרָד וְלֹא־נוֹתַר› (“jut-over the-hail and-not jut-over”)
# ‹כָּל־יֶרֶק בָּעֵץ וּבְעֵשֶׂב› (“all green in-tree and-in-herb”)
# ‹הַשָּׂדֶה בְּכָל־אֶרֶץ מִצְרָיִם› (“the-field in-all earth Egypt”)
# "[EN-AID] And it covered the eye of all the land, and the land was
# darkened; and it ate every herb of the land and all the fruit of the trees
# which the hail had left; and nothing green was left in the tree or in the
# herb of the field in all the land of Egypt."
m.step("Exod.10.15")
# ‹וַיְכַס אֶת־עֵין כָּל־הָאָרֶץ› (“and-plump obj-marker eye all the-earth”)
# ‹וַתֶּחְשַׁךְ הָאָרֶץ› (“and-be-dark the-earth”)
# — fact holds: and-be-dark-the-earth
m.fact("va_techshakh_ha_aretz")

# -------------------------- Exod.10.16 · I_HAVE_SINNED_AGAINST_BOTH --------
# ‹וַיְמַהֵר פַּרְעֹה לִקְרֹא› (“and-hasten Pharaoh to-call”)
# ‹לְמֹשֶׁה וּלְאַהֲרֹן וַיֹּאמֶר› (“to-Moses and-to-Aaron and-say”)
# ‹חָטָאתִי לַיהוָה אֱלֹהֵיכֶם› (“sin to-YHWH God-you/your(pl)”)
# ‹וְלָכֶם› (“and-to-you/your(pl)”)
# "[EN-AID] And Pharaoh hurried to call for Moses and for Aaron; and he
# said: I have sinned against the LORD your God, and against you."
m.step("Exod.10.16")
# ‹וַיֹּאמֶר חָטָאתִי לַיהוָה› (“and-say sin to-YHWH”)
# ‹אֱלֹהֵיכֶם וְלָכֶם› (“God-you/your(pl) and-to-you/your(pl)”)
# — fact holds: sin-to-the-LORD-and-lakhem
m.fact("chatati_la_YHWH_ve_lakhem")

# -------------------------- Exod.10.17 · REMOVE_THIS_DEATH -----------------
# ‹וְעַתָּה שָׂא נָא› (“and-now lift/carry please”)
# ‹חַטָּאתִי אַךְ הַפַּעַם› (“sin-offering-me/my indeed the-stroke”)
# ‹וְהַעְתִּירוּ לַיהוָה אֱלֹהֵיכֶם› (“and-burn-incense-in-worship to-YHWH
# God-you/your(pl)”)
# ‹וְיָסֵר מֵעָלַי רַק› (“and-turn-aside from-over-me/my leanness”)
# ‹אֶת־הַמָּוֶת הַזֶּה› (“obj-marker the-death the-this”)
# "[EN-AID] And now, forgive, pray, my sin only this once, and entreat the
# LORD your God, that He remove from me only this death."
m.step("Exod.10.17")
# ‹וְיָסֵר מֵעָלַי רַק› (“and-turn-aside from-over-me/my leanness”)
# ‹אֶת־הַמָּוֶת הַזֶּה› (“obj-marker the-death the-this”)
# — Pharaoh speaks a demand — LET: burn-incense-in-worship-4
m.declare("paro", "LET",
          "hatiru_4")

# -------------------------- Exod.10.18 · THE_NAMELESS_EXIT -----------------
# ‹וַיֵּצֵא מֵעִם פַּרְעֹה› (“and-bring-forth from-with Pharaoh”)
# ‹וַיֶּעְתַּר אֶל־יְהוָה› (“and-burn-incense-in-worship to YHWH”)
# "[EN-AID] And he went out from Pharaoh, and entreated the LORD."
m.step("Exod.10.18")
# ‹וַיֵּצֵא מֵעִם פַּרְעֹה› (“and-bring-forth from-with Pharaoh”)
# — demand settled (popped from the queue): burn-incense-in-worship-4
m.result("hatiru_4", tmark="t1")

# -------------------------- Exod.10.19 · INTO_THE_REED_SEA -----------------
# ‹וַיַּהֲפֹךְ יְהוָה רוּחַ־יָם› (“and-turn-about YHWH spirit seas”)
# ‹חָזָק מְאֹד וַיִּשָּׂא› (“strong very and-lift/carry”)
# ‹אֶת־הָאַרְבֶּה וַיִּתְקָעֵהוּ יָמָּה› (“obj-marker the-locust and-
# clatter-him/its seas-ward”)
# ‹סּוּף לֹא נִשְׁאַר› (“reed not swell-up”)
# ‹אַרְבֶּה אֶחָד בְּכֹל› (“locust one in-all”)
# ‹גְּבוּל מִצְרָיִם› (“cord Egypt”)
# "[EN-AID] And the LORD turned a very strong sea-wind, and it bore the
# locusts and thrust them into the Reed Sea; not one locust was left in all
# the border of Egypt."
m.step("Exod.10.19")
# ‹נִשְׁאַר אַרְבֶּה אֶחָד› (“swell-up locust one”)
# ‹בְּכֹל› (“in-all”)
# — fact holds: and-yitqaehu-yama-reed
m.fact("va_yitqaehu_yama_suf")

# -------------------------- Exod.10.20 · HARDENED_AGAIN --------------------
# ‹וַיְחַזֵּק יְהוָה אֶת־לֵב› (“and-fasten-upon YHWH obj-marker heart”)
# ‹פַּרְעֹה וְלֹא שִׁלַּח› (“Pharaoh and-not send”)
# ‹אֶת־בְּנֵי יִשְׂרָאֵל› (“obj-marker son Israel”)
# "[EN-AID] And the LORD strengthened Pharaoh's heart, and he did not send
# the sons of Israel."
m.step("Exod.10.20")
# ‹וַיְחַזֵּק יְהוָה אֶת־לֵב› (“and-fasten-upon YHWH obj-marker heart”)
# ‹פַּרְעֹה› (“Pharaoh”)
# — fact holds: and-fasten-upon-2
m.fact("va_yechazeq_2")

# -------------------------- Exod.10.21 · DARKNESS_THAT_IS_FELT -------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹נְטֵה יָדְךָ עַל־הַשָּׁמַיִם› (“stretch hand-you/your over the-heavens”)
# ‹וִיהִי חֹשֶׁךְ עַל־אֶרֶץ› (“and-be darkness over earth”)
# ‹מִצְרָיִם וְיָמֵשׁ חֹשֶׁךְ› (“Egypt and-feel-of darkness”)
# "[EN-AID] And the LORD said to Moses: Stretch out your hand toward heaven,
# and there shall be darkness over the land of Egypt — and the darkness
# shall be felt."
m.step("Exod.10.21")
# ‹חֹשֶׁךְ עַל־אֶרֶץ מִצְרָיִם› (“darkness over earth Egypt”)
# ‹וְיָמֵשׁ חֹשֶׁךְ› (“and-feel-of darkness”)
# — the-LORD speaks a demand — LET: stretch-yadkha-darkness
m.declare("YHWH", "LET",
          "nete_yadkha_choshekh")

# -------------------------- Exod.10.22 · THREE_DAYS_OF_DARK ----------------
# ‹וַיֵּט מֹשֶׁה אֶת־יָדוֹ› (“and-stretch Moses obj-marker hand-him/its”)
# ‹עַל־הַשָּׁמָיִם וַיְהִי חֹשֶׁךְ־אֲפֵלָה› (“over the-heavens and-be
# darkness duskiness”)
# ‹בְּכָל־אֶרֶץ מִצְרַיִם שְׁלֹשֶׁת› (“in-all earth Egypt three”)
# ‹יָמִים› (“day”)
# "[EN-AID] And Moses stretched out his hand toward heaven; and there was
# thick darkness in all the land of Egypt three days."
m.step("Exod.10.22")
# ‹וַיְהִי חֹשֶׁךְ־אֲפֵלָה בְּכָל־אֶרֶץ› (“and-be darkness duskiness in-all
# earth”)
# ‹מִצְרַיִם שְׁלֹשֶׁת יָמִים› (“Egypt three day”)
# — demand settled (popped from the queue): stretch-yadkha-darkness
m.result("nete_yadkha_choshekh", tmark="t1")

# -------------------------- Exod.10.23 · LIGHT_IN_THE_DWELLINGS ------------
# ‹לֹא־רָאוּ אִישׁ אֶת־אָחִיו› (“not see man obj-marker brother-him/its”)
# ‹וְלֹא־קָמוּ אִישׁ מִתַּחְתָּיו› (“and-not arise man from-under-him/its”)
# ‹שְׁלֹשֶׁת יָמִים וּלְכָל־בְּנֵי› (“three day and-to-all son”)
# ‹יִשְׂרָאֵל הָיָה אוֹר› (“Israel be light”)
# ‹בְּמוֹשְׁבֹתָם› (“in-seat-them/their”)
# "[EN-AID] No man saw his brother, nor did any man rise from his place,
# three days; but for all the sons of Israel there was light in their
# dwellings."
m.step("Exod.10.23")
# ‹וּלְכָל־בְּנֵי יִשְׂרָאֵל הָיָה› (“and-to-all son Israel be”)
# ‹אוֹר בְּמוֹשְׁבֹתָם› (“light in-seat-them/their”)
# — fact holds: light-in-moshvotam
m.fact("or_be_moshvotam")

# -------------------------- Exod.10.24 · ONLY_YOUR_FLOCKS_STAY -------------
# ‹וַיִּקְרָא פַרְעֹה אֶל־מֹשֶׁה› (“and-call Pharaoh to Moses”)
# ‹וַיֹּאמֶר לְכוּ עִבְדוּ› (“and-say go work/serve”)
# ‹אֶת־יְהוָה רַק צֹאנְכֶם› (“obj-marker YHWH leanness flock-you/your(pl)”)
# ‹וּבְקַרְכֶם יֻצָּג גַּם־טַפְּכֶם› (“and-herd-you/your(pl) place-
# permanently also family-you/your(pl)”)
# ‹יֵלֵךְ עִמָּכֶם› (“go with-you/your(pl)”)
# "[EN-AID] And Pharaoh called to Moses, and said: Go, serve the LORD — only
# your flocks and your herds shall be held back; your little ones shall also
# go with you."
m.step("Exod.10.24")
# ‹לְכוּ עִבְדוּ אֶת־יְהוָה› (“go work/serve obj-marker YHWH”)
# ‹רַק צֹאנְכֶם וּבְקַרְכֶם› (“leanness flock-you/your(pl) and-herd-
# you/your(pl)”)
# ‹יֻצָּג› (“place-permanently”)
# — Pharaoh speaks a demand — LET: go-leanness-tzonkhem-place-permanently
m.declare("paro", "LET",
          "lekhu_raq_tzonkhem_yutzag")

# -------------------------- Exod.10.25 · YOU_YOURSELF_WILL_GIVE ------------
# ‹וַיֹּאמֶר מֹשֶׁה גַּם־אַתָּה› (“and-say Moses also you”)
# ‹תִּתֵּן בְּיָדֵנוּ זְבָחִים› (“set in-hand-us/our sacrifice”)
# ‹וְעֹלוֹת וְעָשִׂינוּ לַיהוָה› (“and-burnt-offering and-make to-YHWH”)
# ‹אֱלֹהֵינוּ› (“God-us/our”)
# "[EN-AID] And Moses said: You yourself will also give into our hand
# sacrifices and burnt-offerings, and we will offer them to the LORD our
# God."
m.step("Exod.10.25")
# ‹גַּם־אַתָּה תִּתֵּן בְּיָדֵנוּ› (“also you set in-hand-us/our”)
# ‹זְבָחִים וְעֹלוֹת› (“sacrifice and-burnt-offering”)
# — fact holds: also-you-set-in-our-hands
m.fact("gam_ata_titen_be_yadenu")

# -------------------------- Exod.10.26 · NOT_A_HOOF ------------------------
# ‹וְגַם־מִקְנֵנוּ יֵלֵךְ עִמָּנוּ› (“and-also something-bought-us/our go
# with-us/our”)
# ‹לֹא תִשָּׁאֵר פַּרְסָה› (“not swell-up claw”)
# ‹כִּי מִמֶּנּוּ נִקַּח› (“that from-us/our take”)
# ‹לַעֲבֹד אֶת־יְהוָה אֱלֹהֵינוּ› (“to-work/serve obj-marker YHWH God-
# us/our”)
# ‹וַאֲנַחְנוּ לֹא־נֵדַע מַה־נַּעֲבֹד› (“and-we not know what work/serve”)
# ‹אֶת־יְהוָה עַד־בֹּאֵנוּ שָׁמָּה› (“obj-marker YHWH until come/bring-
# us/our there-ward”)
# "[EN-AID] And our cattle shall also go with us — not a hoof shall be left
# — for from it we must take to serve the LORD our God; and we do not know
# with what we shall serve the LORD until we come there."
m.step("Exod.10.26")
# ‹לֹא תִשָּׁאֵר פַּרְסָה› (“not swell-up claw”)
# — fact holds: not-swell-up-claw
m.fact("lo_tishaer_parsa")

# -------------------------- Exod.10.27 · NOT_WILLING -----------------------
# ‹וַיְחַזֵּק יְהוָה אֶת־לֵב› (“and-fasten-upon YHWH obj-marker heart”)
# ‹פַּרְעֹה וְלֹא אָבָה› (“Pharaoh and-not breathe-after”)
# ‹לְשַׁלְּחָם› (“to-send-them/their”)
# "[EN-AID] And the LORD strengthened Pharaoh's heart, and he was not
# willing to send them."
m.step("Exod.10.27")
# ‹וְלֹא אָבָה לְשַׁלְּחָם› (“and-not breathe-after to-send-them/their”)
# — fact holds: and-not-breathe-after-to-shalcham
m.fact("ve_lo_ava_le_shalcham")

# -------------------------- Exod.10.28 · SEE_MY_FACE_NO_MORE ---------------
# ‹וַיֹּאמֶר־לוֹ פַרְעֹה לֵךְ› (“and-say to-him/its Pharaoh go”)
# ‹מֵעָלָי הִשָּׁמֶר לְךָ› (“from-over-me/my keep/guard to-you/your”)
# ‹אֶל־תֹּסֶף רְאוֹת פָּנַי› (“do-not add see face-me/my”)
# ‹כִּי בְּיוֹם רְאֹתְךָ› (“that in-day see-you/your”)
# ‹פָנַי תָּמוּת› (“face-me/my die”)
# "[EN-AID] And Pharaoh said to him: Go from me! Guard yourself — do not
# again see my face, for on the day you see my face you shall die."
m.step("Exod.10.28")
# ‹מֵעָלָי הִשָּׁמֶר לְךָ› (“from-over-me/my keep/guard to-you/your”)
# ‹אֶל־תֹּסֶף› (“do-not add”)
# — Pharaoh speaks a demand — LET: over-add-see-panai
m.declare("paro", "LET",
          "al_tosef_reot_panai")

# -------------------------- Exod.10.29 · I_WILL_NOT_AGAIN ------------------
# ‹וַיֹּאמֶר מֹשֶׁה כֵּן› (“and-say Moses set-upright”)
# ‹דִּבַּרְתָּ לֹא־אֹסִף עוֹד› (“speak not add still/again”)
# ‹רְאוֹת פָּנֶיךָ› (“see face-you/your”)
# "[EN-AID] And Moses said: You have spoken well — I will not again see your
# face."
m.step("Exod.10.29")
# ‹דִּבַּרְתָּ לֹא־אֹסִף עוֹד› (“speak not add still/again”)
# ‹רְאוֹת פָּנֶיךָ› (“see face-you/your”)
# — demand settled (popped from the queue): over-add-see-panai
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
