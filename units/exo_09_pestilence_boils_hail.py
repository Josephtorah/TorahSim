#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_09_pestilence_boils_hail — 9:1-35
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_09_pestilence_boils_hail.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Pestilence, boils, hail (9:1-35)"""
from machine import Machine

m = Machine("exo_09_pestilence_boils_hail")

# -------------------------- Exod.9.1 · THE_CATTLE_ERRAND -------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה בֹּא אֶל־פַּרְעֹה וְדִבַּרְתָּ אֵלָיו
# כֹּה־אָמַר יְהוָה אֱלֹהֵי הָעִבְרִים שַׁלַּח אֶת־עַמִּי וְיַעַבְדֻנִי
# "[EN-AID] And the LORD said to Moses: Come to Pharaoh, and speak to him:
# Thus says the LORD, the God of the Hebrews: Send My people, that they may
# serve Me."
m.step("Exod.9.1")
# ‹בֹּא אֶל־פַּרְעֹה› (“come/bring to Pharaoh”) — the-LORD speaks a demand —
# LET: come/bring-to-Pharaoh-and-speak
m.declare("YHWH", "LET",
          "bo_el_paro_ve_dibarta")

# -------------------------- Exod.9.2 · IF_YOU_REFUSE_TO_SEND ---------------
# כִּי אִם־מָאֵן אַתָּה לְשַׁלֵּחַ וְעוֹדְךָ מַחֲזִיק בָּם
# "[EN-AID] For if you refuse to send, and still hold them fast —"
m.step("Exod.9.2")
# ‹וְעוֹדְךָ מַחֲזִיק בָּם› (“and-still/again-you/your fasten-upon in-
# them/their”) — fact holds: and-odkha-fasten-upon-bam
m.fact("ve_odkha_machaziq_bam")

# -------------------------- Exod.9.3 · THE_HAND_ON_THE_CATTLE --------------
# הִנֵּה יַד־יְהוָה הוֹיָה בְּמִקְנְךָ אֲשֶׁר בַּשָּׂדֶה בַּסּוּסִים
# בַּחֲמֹרִים בַּגְּמַלִּים בַּבָּקָר וּבַצֹּאן דֶּבֶר כָּבֵד מְאֹד
# "[EN-AID] Behold, the hand of the LORD is upon your cattle which are in
# the field — upon the horses, upon the donkeys, upon the camels, upon the
# herds, and upon the flocks — a very heavy pestilence."
m.step("Exod.9.3")
# ‹הִנֵּה יַד־יְהוָה הוֹיָה› (“behold hand YHWH be”) — fact holds: hand-the-
# LORD-be-in-miqnekha
m.fact("yad_YHWH_hoya_be_miqnekha")

# -------------------------- Exod.9.4 · THE_SET_APART -----------------------
# וְהִפְלָה יְהוָה בֵּין מִקְנֵה יִשְׂרָאֵל וּבֵין מִקְנֵה מִצְרָיִם וְלֹא
# יָמוּת מִכָּל־לִבְנֵי יִשְׂרָאֵל דָּבָר
# "[EN-AID] And the LORD will set apart between the cattle of Israel and the
# cattle of Egypt; and nothing shall die of all that belongs to the sons of
# Israel."
m.step("Exod.9.4")
# ‹וְהִפְלָה יְהוָה בֵּין מִקְנֵה יִשְׂרָאֵל וּבֵין מִקְנֵה מִצְרָיִם›
# (“and-distinguish YHWH between something-bought Israel and-between
# something-bought Egypt”) — fact holds: and-distinguish-the-LORD-between-
# something-bought
m.fact("ve_hifla_YHWH_ben_miqne")

# -------------------------- Exod.9.5 · THE_APPOINTED_TIME ------------------
# וַיָּשֶׂם יְהוָה מוֹעֵד לֵאמֹר מָחָר יַעֲשֶׂה יְהוָה הַדָּבָר הַזֶּה
# בָּאָרֶץ
# "[EN-AID] And the LORD set an appointed time, saying: Tomorrow the LORD
# will do this thing in the land."
m.step("Exod.9.5")
# ‹וַיָּשֶׂם יְהוָה מוֹעֵד לֵאמֹר› (“and-put/set YHWH seasons to-say”) —
# fact holds: and-put/set-the-LORD-seasons
m.fact("va_yasem_YHWH_moed")

# -------------------------- Exod.9.6 · THE_CATTLE_DIE ----------------------
# וַיַּעַשׂ יְהוָה אֶת־הַדָּבָר הַזֶּה מִמָּחֳרָת וַיָּמָת כֹּל מִקְנֵה
# מִצְרָיִם וּמִמִּקְנֵה בְנֵי־יִשְׂרָאֵל לֹא־מֵת אֶחָד
# "[EN-AID] And the LORD did this thing on the morrow: and all the cattle of
# Egypt died; and of the cattle of the sons of Israel not one died."
m.step("Exod.9.6")
# ‹וַיָּמָת כֹּל מִקְנֵה מִצְרָיִם› (“and-die all something-bought
# Egyptian”) — fact holds: and-die-all-something-bought-Egypt
m.fact("va_yamat_kol_miqne_mitzrayim")

# -------------------------- Exod.9.7 · THE_AUDIT ---------------------------
# וַיִּשְׁלַח פַּרְעֹה וְהִנֵּה לֹא־מֵת מִמִּקְנֵה יִשְׂרָאֵל עַד־אֶחָד
# וַיִּכְבַּד לֵב פַּרְעֹה וְלֹא שִׁלַּח אֶת־הָעָם
# "[EN-AID] And Pharaoh sent — and behold, not even one of the cattle of
# Israel had died; and Pharaoh's heart grew heavy, and he did not send the
# people."
m.step("Exod.9.7")
# ‹וַיִּשְׁלַח פַּרְעֹה וְהִנֵּה› (“and-send Pharaoh and-behold”) — fact
# holds: and-send-Pharaoh-and-behold
m.fact("va_yishlach_paro_ve_hine")

# -------------------------- Exod.9.8 · SOOT_HEAVENWARD ---------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן קְחוּ לָכֶם מְלֹא חָפְנֵיכֶם
# פִּיחַ כִּבְשָׁן וּזְרָקוֹ מֹשֶׁה הַשָּׁמַיְמָה לְעֵינֵי פַרְעֹה
# "[EN-AID] And the LORD said to Moses and to Aaron: Take for yourselves
# handfuls of soot of the furnace, and let Moses throw it heavenward before
# the eyes of Pharaoh."
m.step("Exod.9.8")
# ‹קְחוּ לָכֶם מְלֹא חָפְנֵיכֶם פִּיחַ כִּבְשָׁן› (“take to-you/your(pl)
# fulness fist-you/your(pl) powder smelting-furnace”) — the-LORD speaks a
# demand — LET: take-piach-and-zeraqo
m.declare("YHWH", "LET",
          "qechu_piach_u_zeraqo")

# -------------------------- Exod.9.9 · THE_DUST_OF_BOILS -------------------
# וְהָיָה לְאָבָק עַל כָּל־אֶרֶץ מִצְרָיִם וְהָיָה עַל־הָאָדָם
# וְעַל־הַבְּהֵמָה לִשְׁחִין פֹּרֵחַ אֲבַעְבֻּעֹת בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And it shall become fine dust over all the land of Egypt, and it
# shall become on man and on beast boils blooming with blisters, in all the
# land of Egypt."
m.step("Exod.9.9")
# ‹לִשְׁחִין פֹּרֵחַ אֲבַעְבֻּעֹת› (“to-inflammation break-forth-as-a-bud
# inflammatory-pustule”) — fact holds: and-be-to-light-particles
m.fact("ve_haya_le_avaq")

# -------------------------- Exod.9.10 · THE_BOILS_BLOOM --------------------
# וַיִּקְחוּ אֶת־פִּיחַ הַכִּבְשָׁן וַיַּעַמְדוּ לִפְנֵי פַרְעֹה וַיִּזְרֹק
# אֹתוֹ מֹשֶׁה הַשָּׁמָיְמָה וַיְהִי שְׁחִין אֲבַעְבֻּעֹת פֹּרֵחַ בָּאָדָם
# וּבַבְּהֵמָה
# "[EN-AID] And they took the soot of the furnace, and stood before Pharaoh;
# and Moses threw it heavenward; and it became boils of blisters, blooming
# on man and on beast."
m.step("Exod.9.10")
# ‹וַיְהִי שְׁחִין אֲבַעְבֻּעֹת פֹּרֵחַ› (“and-be inflammation inflammatory-
# pustule break-forth-as-a-bud”) — demand settled (popped from the queue):
# take-piach-and-zeraqo
m.result("qechu_piach_u_zeraqo", tmark="t1")

# -------------------------- Exod.9.11 · THE_CRAFT_CANNOT_STAND -------------
# וְלֹא־יָכְלוּ הַחַרְטֻמִּים לַעֲמֹד לִפְנֵי מֹשֶׁה מִפְּנֵי הַשְּׁחִין
# כִּי־הָיָה הַשְּׁחִין בַּחֲרְטֻמִּם וּבְכָל־מִצְרָיִם
# "[EN-AID] And the magicians could not stand before Moses because of the
# boils; for the boils were on the magicians, and on all Egypt."
m.step("Exod.9.11")
# ‹וְלֹא־יָכְלוּ הַחַרְטֻמִּים לַעֲמֹד לִפְנֵי מֹשֶׁה› (“and-not be-able
# the-horoscopist to-stand to-face Moses”) — fact holds: and-not-be-able-
# the-horoscopist-laamod
m.fact("ve_lo_yakhlu_ha_chartumim_laamod")

# -------------------------- Exod.9.12 · THE_DIVINE_HARDENING ---------------
# וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה וְלֹא שָׁמַע אֲלֵהֶם כַּאֲשֶׁר דִּבֶּר
# יְהוָה אֶל־מֹשֶׁה
# "[EN-AID] And the LORD strengthened the heart of Pharaoh, and he did not
# hear them, as the LORD had spoken to Moses."
m.step("Exod.9.12")
# ‹וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה› (“and-fasten-upon YHWH obj-marker
# heart Pharaoh”) — fact holds: and-fasten-upon-the-LORD-obj-marker-heart-
# Pharaoh
m.fact("va_yechazeq_YHWH_et_lev_paro")

# -------------------------- Exod.9.13 · THE_HAIL_ERRAND --------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב לִפְנֵי
# פַרְעֹה וְאָמַרְתָּ אֵלָיו כֹּה־אָמַר יְהוָה אֱלֹהֵי הָעִבְרִים שַׁלַּח
# אֶת־עַמִּי וְיַעַבְדֻנִי
# "[EN-AID] And the LORD said to Moses: Rise early in the morning, and
# station yourself before Pharaoh, and say to him: Thus says the LORD, the
# God of the Hebrews: Send My people, that they may serve Me."
m.step("Exod.9.13")
# ‹הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב לִפְנֵי פַרְעֹה› (“rise-early in-morning
# and-place to-face Pharaoh”) — the-LORD speaks a demand — LET: rise-early-
# and-place-2
m.declare("YHWH", "LET",
          "hashkem_ve_hityatzev_2")

# -------------------------- Exod.9.14 · ALL_MY_PLAGUES_TO_YOUR_HEART -------
# כִּי בַּפַּעַם הַזֹּאת אֲנִי שֹׁלֵחַ אֶת־כָּל־מַגֵּפֹתַי אֶל־לִבְּךָ
# וּבַעֲבָדֶיךָ וּבְעַמֶּךָ בַּעֲבוּר תֵּדַע כִּי אֵין כָּמֹנִי
# בְּכָל־הָאָרֶץ
# "[EN-AID] For this time I send all My plagues to your heart, and on your
# servants, and on your people — in order that you may know that there is
# none like Me in all the earth."
m.step("Exod.9.14")
# ‹בַּעֲבוּר תֵּדַע כִּי אֵין כָּמֹנִי בְּכָל־הָאָרֶץ› (“for-the-sake-of
# know that there-is-not form-of-the-prefix-'k-'-me/my in-all the-earth”) —
# fact holds: there-is-not-kamoni-in-all-the-earth
m.fact("en_kamoni_be_khol_ha_aretz")

# -------------------------- Exod.9.15 · BY_NOW_I_COULD_HAVE ----------------
# כִּי עַתָּה שָׁלַחְתִּי אֶת־יָדִי וָאַךְ אוֹתְךָ וְאֶת־עַמְּךָ בַּדָּבֶר
# וַתִּכָּחֵד מִן־הָאָרֶץ
# "[EN-AID] For by now I could have sent out My hand, and struck you and
# your people with the pestilence; and you would have been effaced from the
# earth."
m.step("Exod.9.15")
# ‹כִּי עַתָּה שָׁלַחְתִּי אֶת־יָדִי› (“that now send obj-marker hand-
# me/my”) — fact holds: very-widely-used-as-a-relati-you-send-obj-marker-
# yadi
m.fact("ki_ata_shalachti_et_yadi")

# -------------------------- Exod.9.16 · I_MADE_YOU_STAND -------------------
# וְאוּלָם בַּעֲבוּר זֹאת הֶעֱמַדְתִּיךָ בַּעֲבוּר הַרְאֹתְךָ אֶת־כֹּחִי
# וּלְמַעַן סַפֵּר שְׁמִי בְּכָל־הָאָרֶץ
# "[EN-AID] But for this very cause I have made you stand: in order to show
# you My power, and that My Name be declared in all the earth."
m.step("Exod.9.16")
# ‹וּלְמַעַן סַפֵּר שְׁמִי בְּכָל־הָאָרֶץ› (“and-so-that count name-me/my
# in-all the-earth”) — fact holds: heemadtikha-baavur-harotkha
m.fact("heemadtikha_baavur_harotkha")

# -------------------------- Exod.9.17 · STILL_EXALTING_YOURSELF ------------
# עוֹדְךָ מִסְתּוֹלֵל בְּעַמִּי לְבִלְתִּי שַׁלְּחָם
# "[EN-AID] You still exalt yourself over My people, not to send them."
m.step("Exod.9.17")
# ‹עוֹדְךָ מִסְתּוֹלֵל בְּעַמִּי› (“still/again-you/your mound-up in-people-
# me/my”) — fact holds: odkha-mound-up-in-ami
m.fact("odkha_mistolel_be_ami")

# -------------------------- Exod.9.18 · HAIL_TOMORROW ----------------------
# הִנְנִי מַמְטִיר כָּעֵת מָחָר בָּרָד כָּבֵד מְאֹד אֲשֶׁר לֹא־הָיָה כָמֹהוּ
# בְּמִצְרַיִם לְמִן־הַיּוֹם הִוָּסְדָה וְעַד־עָתָּה
# "[EN-AID] Behold, about this time tomorrow I rain a very heavy hail, such
# as has not been in Egypt from the day it was founded until now."
m.step("Exod.9.18")
# ‹הִנְנִי מַמְטִיר כָּעֵת מָחָר› (“lo!-me/my rain like-time deferred”) —
# fact holds: behold-I-rain-kaet-deferred
m.fact("hineni_mamtir_kaet_machar")

# -------------------------- Exod.9.19 · THE_FLEE_WARNING -------------------
# וְעַתָּה שְׁלַח הָעֵז אֶת־מִקְנְךָ וְאֵת כָּל־אֲשֶׁר לְךָ בַּשָּׂדֶה
# כָּל־הָאָדָם וְהַבְּהֵמָה אֲשֶׁר־יִמָּצֵא בַשָּׂדֶה וְלֹא יֵאָסֵף
# הַבַּיְתָה וְיָרַד עֲלֵהֶם הַבָּרָד וָמֵתוּ
# "[EN-AID] And now — send, bring your cattle and all that is yours in the
# field into safety: every man and beast that is found in the field and not
# gathered into the house — the hail shall come down on them, and they shall
# die."
m.step("Exod.9.19")
# ‹וְעַתָּה שְׁלַח הָעֵז› (“and-now send be-strong”) — fact holds: and-you-
# send-be-strong
m.fact("ve_ata_shelach_haez")

# -------------------------- Exod.9.20 · THE_FEARER -------------------------
# הַיָּרֵא אֶת־דְּבַר יְהוָה מֵעַבְדֵי פַּרְעֹה הֵנִיס אֶת־עֲבָדָיו
# וְאֶת־מִקְנֵהוּ אֶל־הַבָּתִּים
# "[EN-AID] He who feared the word of the LORD among the servants of Pharaoh
# made his servants and his cattle flee into the houses."
m.step("Exod.9.20")
# ‹הַיָּרֵא אֶת־דְּבַר יְהוָה› (“the-fear obj-marker word/thing YHWH”) —
# fact holds: the-fear-obj-marker-word/thing-the-LORD
m.fact("ha_yare_et_devar_YHWH")

# -------------------------- Exod.9.21 · THE_HEEDLESS -----------------------
# וַאֲשֶׁר לֹא־שָׂם לִבּוֹ אֶל־דְּבַר יְהוָה וַיַּעֲזֹב אֶת־עֲבָדָיו
# וְאֶת־מִקְנֵהוּ בַּשָּׂדֶה
# "[EN-AID] And he who did not set his heart to the word of the LORD left
# his servants and his cattle in the field."
m.step("Exod.9.21")
# ‹וַאֲשֶׁר לֹא־שָׂם לִבּוֹ› (“and-which not put/set heart-him/its”) — fact
# holds: and-which-not-put/set-His-heart
m.fact("va_asher_lo_sam_libo")

# -------------------------- Exod.9.22 · STRETCH_TOWARD_HEAVEN --------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה נְטֵה אֶת־יָדְךָ עַל־הַשָּׁמַיִם וִיהִי בָרָד
# בְּכָל־אֶרֶץ מִצְרָיִם עַל־הָאָדָם וְעַל־הַבְּהֵמָה וְעַל כָּל־עֵשֶׂב
# הַשָּׂדֶה בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And the LORD said to Moses: Stretch out your hand toward heaven,
# and there shall be hail in all the land of Egypt — on man, and on beast,
# and on every herb of the field in the land of Egypt."
m.step("Exod.9.22")
# ‹נְטֵה אֶת־יָדְךָ עַל־הַשָּׁמַיִם› (“stretch obj-marker hand-you/your over
# the-heavens”) — the-LORD speaks a demand — LET: stretch-yadkha-over-the-
# heavens
m.declare("YHWH", "LET",
          "nete_yadkha_al_ha_shamayim")

# -------------------------- Exod.9.23 · FIRE_WALKS_TO_EARTH ----------------
# וַיֵּט מֹשֶׁה אֶת־מַטֵּהוּ עַל־הַשָּׁמַיִם וַיהוָה נָתַן קֹלֹת וּבָרָד
# וַתִּהֲלַךְ אֵשׁ אָרְצָה וַיַּמְטֵר יְהוָה בָּרָד עַל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And Moses stretched out his staff toward heaven; and the LORD
# gave voices and hail, and fire went walking to earth; and the LORD rained
# hail on the land of Egypt."
m.step("Exod.9.23")
# ‹וַיַּמְטֵר יְהוָה בָּרָד עַל־אֶרֶץ מִצְרָיִם› (“and-rain YHWH hail over
# earth Egypt”) — demand settled (popped from the queue): stretch-yadkha-
# over-the-heavens
m.result("nete_yadkha_al_ha_shamayim", tmark="t1")

# -------------------------- Exod.9.24 · FIRE_IN_THE_ICE --------------------
# וַיְהִי בָרָד וְאֵשׁ מִתְלַקַּחַת בְּתוֹךְ הַבָּרָד כָּבֵד מְאֹד אֲשֶׁר
# לֹא־הָיָה כָמֹהוּ בְּכָל־אֶרֶץ מִצְרַיִם מֵאָז הָיְתָה לְגוֹי
# "[EN-AID] And there was hail, and fire taking hold of itself within the
# hail, very heavy, such as had not been in all the land of Egypt since it
# became a nation."
m.step("Exod.9.24")
# ‹וְאֵשׁ מִתְלַקַּחַת בְּתוֹךְ הַבָּרָד› (“and-fire take in-midst the-
# hail”) — fact holds: and-fire-take-betokh-the-hail
m.fact("ve_esh_mitlaqachat_betokh_ha_barad")

# -------------------------- Exod.9.25 · THE_STRIKE_CENSUS ------------------
# וַיַּךְ הַבָּרָד בְּכָל־אֶרֶץ מִצְרַיִם אֵת כָּל־אֲשֶׁר בַּשָּׂדֶה מֵאָדָם
# וְעַד־בְּהֵמָה וְאֵת כָּל־עֵשֶׂב הַשָּׂדֶה הִכָּה הַבָּרָד וְאֶת־כָּל־עֵץ
# הַשָּׂדֶה שִׁבֵּר
# "[EN-AID] And the hail struck in all the land of Egypt all that was in the
# field, from man to beast; and every herb of the field the hail struck, and
# every tree of the field it shattered."
m.step("Exod.9.25")
# ‹וַיַּךְ הַבָּרָד› (“and-strike the-hail”) — fact holds: and-strike-the-
# hail
m.fact("va_yakh_ha_barad")

# -------------------------- Exod.9.26 · ONLY_GOSHEN ------------------------
# רַק בְּאֶרֶץ גֹּשֶׁן אֲשֶׁר־שָׁם בְּנֵי יִשְׂרָאֵל לֹא הָיָה בָּרָד
# "[EN-AID] Only in the land of Goshen, where the sons of Israel were, there
# was no hail."
m.step("Exod.9.26")
# ‹רַק בְּאֶרֶץ גֹּשֶׁן› (“leanness in-earth Goshen”) — fact holds:
# leanness-in-earth-Goshen
m.fact("raq_be_eretz_goshen")

# -------------------------- Exod.9.27 · I_HAVE_SINNED ----------------------
# וַיִּשְׁלַח פַּרְעֹה וַיִּקְרָא לְמֹשֶׁה וּלְאַהֲרֹן וַיֹּאמֶר אֲלֵהֶם
# חָטָאתִי הַפָּעַם יְהוָה הַצַּדִּיק וַאֲנִי וְעַמִּי הָרְשָׁעִים
# "[EN-AID] And Pharaoh sent and called for Moses and for Aaron, and said to
# them: I have sinned this time; the LORD is the righteous one, and I and my
# people are the wicked."
m.step("Exod.9.27")
# ‹חָטָאתִי הַפָּעַם יְהוָה הַצַּדִּיק וַאֲנִי וְעַמִּי הָרְשָׁעִים› (“sin
# the-stroke YHWH the-just and-I and-people-me/my the-wrong”) — fact holds:
# sin-the-stroke
m.fact("chatati_ha_paam")

# -------------------------- Exod.9.28 · ENTREAT_ENOUGH ---------------------
# הַעְתִּירוּ אֶל־יְהוָה וְרַב מִהְיֹת קֹלֹת אֱלֹהִים וּבָרָד וַאֲשַׁלְּחָה
# אֶתְכֶם וְלֹא תֹסִפוּן לַעֲמֹד
# "[EN-AID] Entreat the LORD — and enough of there being voices of God and
# hail — and I will send you, and you shall not continue to stand."
m.step("Exod.9.28")
# ‹הַעְתִּירוּ אֶל־יְהוָה› (“burn-incense-in-worship to YHWH”) — Pharaoh
# speaks a demand — LET: burn-incense-in-worship-to-the-LORD-3
m.declare("paro", "LET",
          "hatiru_el_YHWH_3")

# -------------------------- Exod.9.29 · PALMS_SPREAD_THE_PROMISE -----------
# וַיֹּאמֶר אֵלָיו מֹשֶׁה כְּצֵאתִי אֶת־הָעִיר אֶפְרֹשׂ אֶת־כַּפַּי
# אֶל־יְהוָה הַקֹּלוֹת יֶחְדָּלוּן וְהַבָּרָד לֹא יִהְיֶה־עוֹד לְמַעַן
# תֵּדַע כִּי לַיהוָה הָאָרֶץ
# "[EN-AID] And Moses said to him: As I go out of the city, I will spread
# out my palms to the LORD; the thunders shall cease, and the hail shall be
# no more — in order that you may know that the earth is the LORD's."
m.step("Exod.9.29")
# ‹הַקֹּלוֹת יֶחְדָּלוּן וְהַבָּרָד לֹא יִהְיֶה־עוֹד› (“the-voice/sound
# cease-ward and-the-hail not be still/again”) — fact holds: the-
# voice/sound-yechdalun
m.fact("ha_qolot_yechdalun")

# -------------------------- Exod.9.30 · NOT_YET_FEARING --------------------
# וְאַתָּה וַעֲבָדֶיךָ יָדַעְתִּי כִּי טֶרֶם תִּירְאוּן מִפְּנֵי יְהוָה
# אֱלֹהִים
# "[EN-AID] And you and your servants — I know that you do not yet fear
# before the LORD God."
m.step("Exod.9.30")
# ‹יָדַעְתִּי כִּי טֶרֶם תִּירְאוּן› (“know that non-occurrence fear-ward”)
# — fact holds: non-occurrence-tiraun
m.fact("terem_tiraun")

# -------------------------- Exod.9.31 · FLAX_AND_BARLEY --------------------
# וְהַפִּשְׁתָּה וְהַשְּׂעֹרָה נֻכָּתָה כִּי הַשְּׂעֹרָה אָבִיב
# וְהַפִּשְׁתָּה גִּבְעֹל
# "[EN-AID] And the flax and the barley were struck; for the barley was in
# the ear, and the flax was in bud."
m.step("Exod.9.31")
# ‹וְהַפִּשְׁתָּה וְהַשְּׂעֹרָה נֻכָּתָה› (“and-the-flax and-the-barley
# strike”) — fact holds: and-the-flax-and-the-barley-strike
m.fact("ve_ha_pishta_ve_ha_seora_nukata")

# -------------------------- Exod.9.32 · WHEAT_AND_SPELT --------------------
# וְהַחִטָּה וְהַכֻּסֶּמֶת לֹא נֻכּוּ כִּי אֲפִילֹת הֵנָּה
# "[EN-AID] And the wheat and the spelt were not struck; for they are late."
m.step("Exod.9.32")
# ‹כִּי אֲפִילֹת הֵנָּה› (“that unripe themselves”) — fact holds: very-
# widely-used-as-a-relati-unripe-themselves
m.fact("ki_afilot_hena")

# -------------------------- Exod.9.33 · THE_CEASING ------------------------
# וַיֵּצֵא מֹשֶׁה מֵעִם פַּרְעֹה אֶת־הָעִיר וַיִּפְרֹשׂ כַּפָּיו אֶל־יְהוָה
# וַיַּחְדְּלוּ הַקֹּלוֹת וְהַבָּרָד וּמָטָר לֹא־נִתַּךְ אָרְצָה
# "[EN-AID] And Moses went out of the city from Pharaoh, and spread out his
# palms to the LORD; and the thunders and the hail ceased, and rain was not
# poured to earth."
m.step("Exod.9.33")
# ‹וַיַּחְדְּלוּ הַקֹּלוֹת וְהַבָּרָד וּמָטָר לֹא־נִתַּךְ אָרְצָה› (“and-
# cease the-voice/sound and-the-hail and-rain not flow-forth earth-ward”) —
# demand settled (popped from the queue): burn-incense-in-worship-to-the-
# LORD-3
m.result("hatiru_el_YHWH_3", tmark="t1")

# -------------------------- Exod.9.34 · SINNING_AGAIN ----------------------
# וַיַּרְא פַּרְעֹה כִּי־חָדַל הַמָּטָר וְהַבָּרָד וְהַקֹּלֹת וַיֹּסֶף
# לַחֲטֹא וַיַּכְבֵּד לִבּוֹ הוּא וַעֲבָדָיו
# "[EN-AID] And Pharaoh saw that the rain and the hail and the thunders had
# ceased — and he continued to sin, and made his heart heavy, he and his
# servants."
m.step("Exod.9.34")
# ‹וַיֹּסֶף לַחֲטֹא› (“and-add to-sin”) — fact holds: and-add-to-sin
m.fact("va_yosef_la_chato")

# -------------------------- Exod.9.35 · THE_SEAL_BY_MOSES_HAND -------------
# וַיֶּחֱזַק לֵב פַּרְעֹה וְלֹא שִׁלַּח אֶת־בְּנֵי יִשְׂרָאֵל כַּאֲשֶׁר
# דִּבֶּר יְהוָה בְּיַד־מֹשֶׁה
# "[EN-AID] And the heart of Pharaoh was strengthened, and he did not send
# the sons of Israel, as the LORD had spoken by the hand of Moses."
m.step("Exod.9.35")
# ‹כַּאֲשֶׁר דִּבֶּר יְהוָה בְּיַד־מֹשֶׁה› (“like-as/which speak YHWH in-
# hand Moses”) — fact holds: like-which-speak-the-LORD-in-hand-Moses
m.fact("ka_asher_diber_YHWH_be_yad_moshe")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['bo_el_paro_ve_dibarta', 'hashkem_ve_hityatzev_2']
    assert len(m.SPECS["log"]) == 5
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_odkha_machaziq_bam', 'yad_YHWH_hoya_be_miqnekha', 've_hifla_YHWH_ben_miqne', 'va_yasem_YHWH_moed', 'va_yamat_kol_miqne_mitzrayim', 'va_yishlach_paro_ve_hine', 've_haya_le_avaq', 've_lo_yakhlu_ha_chartumim_laamod', 'va_yechazeq_YHWH_et_lev_paro', 'en_kamoni_be_khol_ha_aretz', 'ki_ata_shalachti_et_yadi', 'heemadtikha_baavur_harotkha', 'odkha_mistolel_be_ami', 'hineni_mamtir_kaet_machar', 've_ata_shelach_haez', 'ha_yare_et_devar_YHWH', 'va_asher_lo_sam_libo', 've_esh_mitlaqachat_betokh_ha_barad', 'va_yakh_ha_barad', 'raq_be_eretz_goshen', 'chatati_ha_paam', 'ha_qolot_yechdalun', 'terem_tiraun', 've_ha_pishta_ve_ha_seora_nukata', 'ki_afilot_hena', 'va_yosef_la_chato', 'ka_asher_diber_YHWH_be_yad_moshe'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 8
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
