#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_08_frogs_lice_swarms — 8:1-28
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_08_frogs_lice_swarms.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Frogs, lice, swarms (8:1-28)"""
from machine import Machine

m = Machine("exo_08_frogs_lice_swarms")

# -------------------------- Exod.8.1 · BRING_UP_THE_FROGS ------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה אֱמֹר אֶל־אַהֲרֹן נְטֵה אֶת־יָדְךָ בְּמַטֶּךָ
# עַל־הַנְּהָרֹת עַל־הַיְאֹרִים וְעַל־הָאֲגַמִּים וְהַעַל
# אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And the LORD said to Moses: Say to Aaron: Stretch out your hand
# with your staff over the rivers, over the Niles, and over the pools, and
# bring up the frogs onto the land of Egypt."
m.step("Exod.8.1")
# ‹וְהַעַל אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ מִצְרָיִם› (“and-go-up obj-marker
# the-marsh-leaper over earth Egypt”) — the-LORD speaks a demand — LET: and-
# go-up-obj-marker-the-tzfardeim
m.declare("YHWH", "LET",
          "ve_haal_et_ha_tzfardeim")

# -------------------------- Exod.8.2 · THE_FROG_CAME_UP --------------------
# וַיֵּט אַהֲרֹן אֶת־יָדוֹ עַל מֵימֵי מִצְרָיִם וַתַּעַל הַצְּפַרְדֵּעַ
# וַתְּכַס אֶת־אֶרֶץ מִצְרָיִם
# "[EN-AID] And Aaron stretched out his hand over the waters of Egypt; and
# the frog came up, and covered the land of Egypt."
m.step("Exod.8.2")
# ‹וַתַּעַל הַצְּפַרְדֵּעַ וַתְּכַס אֶת־אֶרֶץ מִצְרָיִם› (“and-go-up the-
# marsh-leaper and-plump obj-marker earth Egypt”) — demand settled (popped
# from the queue): and-go-up-obj-marker-the-tzfardeim
m.result("ve_haal_et_ha_tzfardeim", tmark="t1")

# -------------------------- Exod.8.3 · THE_MAGICIANS_MATCH_FROGS -----------
# וַיַּעֲשׂוּ־כֵן הַחֲרְטֻמִּים בְּלָטֵיהֶם וַיַּעֲלוּ אֶת־הַצְפַרְדְּעִים
# עַל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And the magicians did so with their secret arts, and brought up
# the frogs onto the land of Egypt."
m.step("Exod.8.3")
# ‹וַיַּעֲלוּ אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ מִצְרָיִם› (“and-go-up obj-
# marker the-marsh-leaper over earth Egypt”) — fact holds: and-go-up-the-
# horoscopist
m.fact("va_yaalu_ha_chartumim")

# -------------------------- Exod.8.4 · PHARAOHS_FIRST_BARGAIN --------------
# וַיִּקְרָא פַרְעֹה לְמֹשֶׁה וּלְאַהֲרֹן וַיֹּאמֶר הַעְתִּירוּ אֶל־יְהוָה
# וְיָסֵר הַצְפַרְדְּעִים מִמֶּנִּי וּמֵעַמִּי וַאֲשַׁלְּחָה אֶת־הָעָם
# וְיִזְבְּחוּ לַיהוָה
# "[EN-AID] And Pharaoh called for Moses and for Aaron, and said: Entreat
# the LORD, that He take away the frogs from me and from my people; and I
# will send the people, that they may sacrifice to the LORD."
m.step("Exod.8.4")
# ‹הַעְתִּירוּ אֶל־יְהוָה וְיָסֵר הַצְפַרְדְּעִים מִמֶּנִּי וּמֵעַמִּי›
# (“burn-incense-in-worship to YHWH and-turn-aside the-marsh-leaper from-
# me/my and-from-people-me/my”) — Pharaoh speaks a demand — LET: burn-
# incense-in-worship-to-the-LORD
m.declare("paro", "LET",
          "hatiru_el_YHWH")

# -------------------------- Exod.8.5 · GLORY_OVER_ME -----------------------
# וַיֹּאמֶר מֹשֶׁה לְפַרְעֹה הִתְפָּאֵר עָלַי לְמָתַי אַעְתִּיר לְךָ
# וְלַעֲבָדֶיךָ וּלְעַמְּךָ לְהַכְרִית הַצֲפַרְדְּעִים מִמְּךָ וּמִבָּתֶּיךָ
# רַק בַּיְאֹר תִּשָּׁאַרְנָה
# "[EN-AID] And Moses said to Pharaoh: Glory over me — for when shall I
# entreat for you, and for your servants, and for your people, to cut off
# the frogs from you and from your houses? Only in the Nile shall they
# remain."
m.step("Exod.8.5")
# ‹הִתְפָּאֵר עָלַי לְמָתַי אַעְתִּיר לְךָ› (“gleam over-me/my to-extent
# burn-incense-in-worship to-you/your”) — fact holds: gleam-alai-to-matai
m.fact("hitpaer_alai_le_matai")

# -------------------------- Exod.8.6 · FOR_TOMORROW ------------------------
# וַיֹּאמֶר לְמָחָר וַיֹּאמֶר כִּדְבָרְךָ לְמַעַן תֵּדַע כִּי־אֵין כַּיהוָה
# אֱלֹהֵינוּ
# "[EN-AID] And he said: For tomorrow. And he said: According to your word —
# that you may know that there is none like the LORD our God."
m.step("Exod.8.6")
# ‹לְמַעַן תֵּדַע כִּי־אֵין כַּיהוָה אֱלֹהֵינוּ› (“so-that know that there-
# is-not like-YHWH God-us/our”) — fact holds: that-devarkha-so-that-know
m.fact("ki_devarkha_lemaan_teda")

# -------------------------- Exod.8.7 · THE_REMOVAL_FORECAST ----------------
# וְסָרוּ הַצְפַרְדְּעִים מִמְּךָ וּמִבָּתֶּיךָ וּמֵעֲבָדֶיךָ וּמֵעַמֶּךָ
# רַק בַּיְאֹר תִּשָּׁאַרְנָה
# "[EN-AID] And the frogs shall turn aside from you, and from your houses,
# and from your servants, and from your people; only in the Nile shall they
# remain."
m.step("Exod.8.7")
# ‹וְסָרוּ הַצְפַרְדְּעִים מִמְּךָ וּמִבָּתֶּיךָ וּמֵעֲבָדֶיךָ וּמֵעַמֶּךָ›
# (“and-turn-aside the-marsh-leaper from-you/your and-from-house-you/your
# and-from-servant-you/your and-from-people-you/your”) — fact holds: and-
# turn-aside-the-tzfardeim
m.fact("ve_saru_ha_tzfardeim")

# -------------------------- Exod.8.8 · MOSES_CRIES_TO_YHWH -----------------
# וַיֵּצֵא מֹשֶׁה וְאַהֲרֹן מֵעִם פַּרְעֹה וַיִּצְעַק מֹשֶׁה אֶל־יְהוָה
# עַל־דְּבַר הַצְפַרְדְּעִים אֲשֶׁר־שָׂם לְפַרְעֹה
# "[EN-AID] And Moses and Aaron went out from Pharaoh; and Moses cried to
# the LORD over the matter of the frogs which He had set upon Pharaoh."
m.step("Exod.8.8")
# ‹וַיִּצְעַק מֹשֶׁה אֶל־יְהוָה› (“and-shriek Moses to YHWH”) — demand
# settled (popped from the queue): burn-incense-in-worship-to-the-LORD
m.result("hatiru_el_YHWH", tmark="t1")

# -------------------------- Exod.8.9 · PER_THE_WORD_OF_MOSES ---------------
# וַיַּעַשׂ יְהוָה כִּדְבַר מֹשֶׁה וַיָּמֻתוּ הַצְפַרְדְּעִים מִן־הַבָּתִּים
# מִן־הַחֲצֵרֹת וּמִן־הַשָּׂדֹת
# "[EN-AID] And the LORD did according to the word of Moses; and the frogs
# died from the houses, from the courtyards, and from the fields."
m.step("Exod.8.9")
# ‹וַיַּעַשׂ יְהוָה כִּדְבַר מֹשֶׁה› (“and-make YHWH like-word/thing Moses”)
# — fact holds: and-make-the-LORD-that-word/thing-Moses
m.fact("va_yaas_YHWH_ki_devar_moshe")

# -------------------------- Exod.8.10 · HEAPS_UPON_HEAPS -------------------
# וַיִּצְבְּרוּ אֹתָם חֳמָרִם חֳמָרִם וַתִּבְאַשׁ הָאָרֶץ
# "[EN-AID] And they gathered them heaps upon heaps; and the land stank."
m.step("Exod.8.10")
# ‹חֳמָרִם חֳמָרִם› (“bubbling-up bubbling-up”) — fact holds: bubbling-up-
# bubbling-up
m.fact("chomarim_chomarim")

# -------------------------- Exod.8.11 · THE_BREATHING_SPACE ----------------
# וַיַּרְא פַּרְעֹה כִּי הָיְתָה הָרְוָחָה וְהַכְבֵּד אֶת־לִבּוֹ וְלֹא
# שָׁמַע אֲלֵהֶם כַּאֲשֶׁר דִּבֶּר יְהוָה
# "[EN-AID] And Pharaoh saw that there was relief, and he made his heart
# heavy, and did not hear them, as the LORD had spoken."
m.step("Exod.8.11")
# ‹וְהַכְבֵּד אֶת־לִבּוֹ› (“and-be-heavy obj-marker heart-him/its”) — fact
# holds: and-be-heavy-obj-marker-His-heart
m.fact("ve_hakhbed_et_libo")

# -------------------------- Exod.8.12 · STRIKE_THE_DUST --------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה אֱמֹר אֶל־אַהֲרֹן נְטֵה אֶת־מַטְּךָ וְהַךְ
# אֶת־עֲפַר הָאָרֶץ וְהָיָה לְכִנִּם בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And the LORD said to Moses: Say to Aaron: Stretch out your
# staff, and strike the dust of the earth, and it shall become lice in all
# the land of Egypt."
m.step("Exod.8.12")
# ‹נְטֵה אֶת־מַטְּךָ וְהַךְ אֶת־עֲפַר הָאָרֶץ› (“stretch obj-marker
# staff/tribe-you/your and-strike obj-marker dust the-earth”) — the-LORD
# speaks a demand — LET: and-strike-obj-marker-dust-the-earth
m.declare("YHWH", "LET",
          "ve_hakh_et_afar_ha_aretz")

# -------------------------- Exod.8.13 · THE_DUST_BECOMES_LICE --------------
# וַיַּעֲשׂוּ־כֵן וַיֵּט אַהֲרֹן אֶת־יָדוֹ בְמַטֵּהוּ וַיַּךְ אֶת־עֲפַר
# הָאָרֶץ וַתְּהִי הַכִּנָּם בָּאָדָם וּבַבְּהֵמָה כָּל־עֲפַר הָאָרֶץ הָיָה
# כִנִּים בְּכָל־אֶרֶץ מִצְרָיִם
# "[EN-AID] And they did so: and Aaron stretched out his hand with his
# staff, and struck the dust of the earth, and the lice came on man and on
# beast; all the dust of the earth became lice in all the land of Egypt."
m.step("Exod.8.13")
# ‹כָּל־עֲפַר הָאָרֶץ הָיָה כִנִּים בְּכָל־אֶרֶץ מִצְרָיִם› (“all dust the-
# earth be gnat in-all earth Egypt”) — demand settled (popped from the
# queue): and-strike-obj-marker-dust-the-earth
m.result("ve_hakh_et_afar_ha_aretz", tmark="t1")

# -------------------------- Exod.8.14 · THE_CRAFT_FAILS --------------------
# וַיַּעֲשׂוּ־כֵן הַחַרְטֻמִּים בְּלָטֵיהֶם לְהוֹצִיא אֶת־הַכִּנִּים וְלֹא
# יָכֹלוּ וַתְּהִי הַכִּנָּם בָּאָדָם וּבַבְּהֵמָה
# "[EN-AID] And the magicians did so with their secret arts, to bring forth
# the lice — but they could not; and the lice were on man and on beast."
m.step("Exod.8.14")
# ‹וְלֹא יָכֹלוּ› (“and-not be-able”) — fact holds: and-not-be-able
m.fact("ve_lo_yakholu")

# -------------------------- Exod.8.15 · THE_FINGER_OF_GOD ------------------
# וַיֹּאמְרוּ הַחַרְטֻמִּים אֶל־פַּרְעֹה אֶצְבַּע אֱלֹהִים הִוא וַיֶּחֱזַק
# לֵב־פַּרְעֹה וְלֹא־שָׁמַע אֲלֵהֶם כַּאֲשֶׁר דִּבֶּר יְהוָה
# "[EN-AID] And the magicians said to Pharaoh: It is the finger of God. And
# Pharaoh's heart was strengthened, and he did not hear them, as the LORD
# had spoken."
m.step("Exod.8.15")
# ‹אֶצְבַּע אֱלֹהִים הִוא› (“something-to-sieze-with God he/it”) — fact
# holds: something-to-sieze-with-God-he/it
m.fact("etzba_elohim_hiv")

# -------------------------- Exod.8.16 · RISE_EARLY_STAND_BEFORE ------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב לִפְנֵי
# פַרְעֹה הִנֵּה יוֹצֵא הַמָּיְמָה וְאָמַרְתָּ אֵלָיו כֹּה אָמַר יְהוָה
# שַׁלַּח עַמִּי וְיַעַבְדֻנִי
# "[EN-AID] And the LORD said to Moses: Rise early in the morning, and
# station yourself before Pharaoh — behold, he goes out to the water — and
# say to him: Thus says the LORD: Send My people, that they may serve Me."
m.step("Exod.8.16")
# ‹הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב לִפְנֵי פַרְעֹה› (“rise-early in-morning
# and-place to-face Pharaoh”) — the-LORD speaks a demand — LET: rise-early-
# and-place-lifne-Pharaoh
m.declare("YHWH", "LET",
          "hashkem_ve_hityatzev_lifne_paro")

# -------------------------- Exod.8.17 · THE_SWARMS_THREATENED --------------
# כִּי אִם־אֵינְךָ מְשַׁלֵּחַ אֶת־עַמִּי הִנְנִי מַשְׁלִיחַ בְּךָ
# וּבַעֲבָדֶיךָ וּבְעַמְּךָ וּבְבָתֶּיךָ אֶת־הֶעָרֹב וּמָלְאוּ בָּתֵּי
# מִצְרַיִם אֶת־הֶעָרֹב וְגַם הָאֲדָמָה אֲשֶׁר־הֵם עָלֶיהָ
# "[EN-AID] For if you do not send My people — behold, I set loose upon you,
# and upon your servants, and upon your people, and into your houses, the
# swarms; and the houses of Egypt shall be full of the swarms, and also the
# ground on which they are."
m.step("Exod.8.17")
# ‹אֵינְךָ מְשַׁלֵּחַ אֶת־עַמִּי הִנְנִי מַשְׁלִיחַ בְּךָ› (“there-is-not-
# you/your send obj-marker people-me/my lo!-me/my send in-you/your”) — fact
# holds: behold-I-mashliach-obj-marker-he-mosquito
m.fact("hineni_mashliach_et_he_arov")

# -------------------------- Exod.8.18 · GOSHEN_SET_APART -------------------
# וְהִפְלֵיתִי בַיּוֹם הַהוּא אֶת־אֶרֶץ גֹּשֶׁן אֲשֶׁר עַמִּי עֹמֵד עָלֶיהָ
# לְבִלְתִּי הֱיוֹת־שָׁם עָרֹב לְמַעַן תֵּדַע כִּי אֲנִי יְהוָה בְּקֶרֶב
# הָאָרֶץ
# "[EN-AID] And I will set apart on that day the land of Goshen, on which My
# people stands, that no swarm shall be there — that you may know that I am
# the LORD in the midst of the earth."
m.step("Exod.8.18")
# ‹וְהִפְלֵיתִי בַיּוֹם הַהוּא אֶת־אֶרֶץ גֹּשֶׁן› (“and-distinguish in-day
# that obj-marker earth Goshen”) — fact holds: and-distinguish-obj-marker-
# earth-Goshen
m.fact("ve_hifleti_et_eretz_goshen")

# -------------------------- Exod.8.19 · THE_DIVISION_SET -------------------
# וְשַׂמְתִּי פְדֻת בֵּין עַמִּי וּבֵין עַמֶּךָ לְמָחָר יִהְיֶה הָאֹת הַזֶּה
# "[EN-AID] And I will set a division between My people and your people; for
# tomorrow shall this sign be."
m.step("Exod.8.19")
# ‹וְשַׂמְתִּי פְדֻת בֵּין עַמִּי וּבֵין עַמֶּךָ› (“and-put/set distinction
# between people-me/my and-between people-you/your”) — fact holds: and-
# put/set-distinction
m.fact("ve_samti_fedut")

# -------------------------- Exod.8.20 · THE_LAND_RUINED --------------------
# וַיַּעַשׂ יְהוָה כֵּן וַיָּבֹא עָרֹב כָּבֵד בֵּיתָה פַרְעֹה וּבֵית
# עֲבָדָיו וּבְכָל־אֶרֶץ מִצְרַיִם תִּשָּׁחֵת הָאָרֶץ מִפְּנֵי הֶעָרֹב
# "[EN-AID] And the LORD did so; and heavy swarms came into the house of
# Pharaoh, and the house of his servants, and in all the land of Egypt the
# land was ruined from before the swarms."
m.step("Exod.8.20")
# ‹תִּשָּׁחֵת הָאָרֶץ מִפְּנֵי הֶעָרֹב› (“decay the-earth from-face the-
# mosquito”) — fact holds: decay-the-earth
m.fact("tishachet_ha_aretz")

# -------------------------- Exod.8.21 · SACRIFICE_IN_THE_LAND --------------
# וַיִּקְרָא פַרְעֹה אֶל־מֹשֶׁה וּלְאַהֲרֹן וַיֹּאמֶר לְכוּ זִבְחוּ
# לֵאלֹהֵיכֶם בָּאָרֶץ
# "[EN-AID] And Pharaoh called to Moses and to Aaron, and said: Go,
# sacrifice to your God — in the land."
m.step("Exod.8.21")
# ‹וַיֹּאמֶר לְכוּ זִבְחוּ לֵאלֹהֵיכֶם בָּאָרֶץ› (“and-say go slaughter-an-
# animal to-God-you/your(pl) in-earth”) — Pharaoh speaks a demand — LET: go-
# slaughter-an-animal-in-the-earth
m.declare("paro", "LET",
          "lekhu_zivchu_ba_aretz")

# -------------------------- Exod.8.22 · NOT_RIGHT_TO_DO_SO -----------------
# וַיֹּאמֶר מֹשֶׁה לֹא נָכוֹן לַעֲשׂוֹת כֵּן כִּי תּוֹעֲבַת מִצְרַיִם
# נִזְבַּח לַיהוָה אֱלֹהֵינוּ הֵן נִזְבַּח אֶת־תּוֹעֲבַת מִצְרַיִם
# לְעֵינֵיהֶם וְלֹא יִסְקְלֻנוּ
# "[EN-AID] And Moses said: It is not right to do so; for the abomination of
# Egypt we would sacrifice to the LORD our God — behold, if we sacrifice the
# abomination of Egypt before their eyes, will they not stone us?"
m.step("Exod.8.22")
# ‹לֹא נָכוֹן לַעֲשׂוֹת כֵּן› (“not be-erect to-make so”) — fact holds: not-
# be-erect-laasot-so
m.fact("lo_nakhon_laasot_ken")

# -------------------------- Exod.8.23 · THREE_DAYS_AS_HE_SAYS --------------
# דֶּרֶךְ שְׁלֹשֶׁת יָמִים נֵלֵךְ בַּמִּדְבָּר וְזָבַחְנוּ לַיהוָה
# אֱלֹהֵינוּ כַּאֲשֶׁר יֹאמַר אֵלֵינוּ
# "[EN-AID] A journey of three days we will go into the wilderness, and
# sacrifice to the LORD our God, as He shall say to us."
m.step("Exod.8.23")
# ‹דֶּרֶךְ שְׁלֹשֶׁת יָמִים נֵלֵךְ בַּמִּדְבָּר› (“way/road three day go in-
# pasture”) — fact holds: way/road-three-day-go
m.fact("derekh_sheloshet_yamim_nelekh")

# -------------------------- Exod.8.24 · ONLY_NOT_FAR -----------------------
# וַיֹּאמֶר פַּרְעֹה אָנֹכִי אֲשַׁלַּח אֶתְכֶם וּזְבַחְתֶּם לַיהוָה
# אֱלֹהֵיכֶם בַּמִּדְבָּר רַק הַרְחֵק לֹא־תַרְחִיקוּ לָלֶכֶת הַעְתִּירוּ
# בַּעֲדִי
# "[EN-AID] And Pharaoh said: I will send you, and you shall sacrifice to
# the LORD your God in the wilderness — only you shall not go far; entreat
# for me."
m.step("Exod.8.24")
# ‹הַעְתִּירוּ בַּעֲדִי› (“burn-incense-in-worship in-up-to-me/my”) —
# Pharaoh speaks a demand — LET: burn-incense-in-worship-baadi
m.declare("paro", "LET",
          "hatiru_baadi")

# -------------------------- Exod.8.25 · LET_PHARAOH_NOT_DECEIVE ------------
# וַיֹּאמֶר מֹשֶׁה הִנֵּה אָנֹכִי יוֹצֵא מֵעִמָּךְ וְהַעְתַּרְתִּי
# אֶל־יְהוָה וְסָר הֶעָרֹב מִפַּרְעֹה מֵעֲבָדָיו וּמֵעַמּוֹ מָחָר רַק
# אַל־יֹסֵף פַּרְעֹה הָתֵל לְבִלְתִּי שַׁלַּח אֶת־הָעָם לִזְבֹּחַ לַיהוָה
# "[EN-AID] And Moses said: Behold, I go out from you, and I will entreat
# the LORD, and the swarms shall turn aside from Pharaoh, from his servants,
# and from his people tomorrow — only let Pharaoh not continue to deceive,
# not to send the people to sacrifice to the LORD."
m.step("Exod.8.25")
# ‹רַק אַל־יֹסֵף פַּרְעֹה הָתֵל› (“leanness do-not add Pharaoh deride”) —
# fact holds: over-add-Pharaoh-deride
m.fact("al_yosef_paro_hatel")

# -------------------------- Exod.8.26 · MOSES_ENTREATS ---------------------
# וַיֵּצֵא מֹשֶׁה מֵעִם פַּרְעֹה וַיֶּעְתַּר אֶל־יְהוָה
# "[EN-AID] And Moses went out from Pharaoh, and entreated the LORD."
m.step("Exod.8.26")
# ‹וַיֶּעְתַּר אֶל־יְהוָה› (“and-burn-incense-in-worship to YHWH”) — demand
# settled (popped from the queue): burn-incense-in-worship-baadi
m.result("hatiru_baadi", tmark="t1")

# -------------------------- Exod.8.27 · NOT_ONE_REMAINED -------------------
# וַיַּעַשׂ יְהוָה כִּדְבַר מֹשֶׁה וַיָּסַר הֶעָרֹב מִפַּרְעֹה מֵעֲבָדָיו
# וּמֵעַמּוֹ לֹא נִשְׁאַר אֶחָד
# "[EN-AID] And the LORD did according to the word of Moses, and turned
# aside the swarms from Pharaoh, from his servants, and from his people; not
# one remained."
m.step("Exod.8.27")
# ‹לֹא נִשְׁאַר אֶחָד› (“not swell-up one”) — fact holds: not-swell-up-one
m.fact("lo_nishar_echad")

# -------------------------- Exod.8.28 · THIS_TIME_ALSO ---------------------
# וַיַּכְבֵּד פַּרְעֹה אֶת־לִבּוֹ גַּם בַּפַּעַם הַזֹּאת וְלֹא שִׁלַּח
# אֶת־הָעָם
# "[EN-AID] And Pharaoh made his heart heavy this time also, and did not
# send the people."
m.step("Exod.8.28")
# ‹וַיַּכְבֵּד פַּרְעֹה אֶת־לִבּוֹ גַּם בַּפַּעַם הַזֹּאת› (“and-be-heavy
# Pharaoh obj-marker heart-him/its also in-stroke the-this”) — fact holds:
# and-be-heavy-Pharaoh-obj-marker-His-heart
m.fact("va_yakhbed_paro_et_libo")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hashkem_ve_hityatzev_lifne_paro', 'lekhu_zivchu_ba_aretz']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yaalu_ha_chartumim', 'hitpaer_alai_le_matai', 'ki_devarkha_lemaan_teda', 've_saru_ha_tzfardeim', 'va_yaas_YHWH_ki_devar_moshe', 'chomarim_chomarim', 've_hakhbed_et_libo', 've_lo_yakholu', 'etzba_elohim_hiv', 'hineni_mashliach_et_he_arov', 've_hifleti_et_eretz_goshen', 've_samti_fedut', 'tishachet_ha_aretz', 'lo_nakhon_laasot_ken', 'derekh_sheloshet_yamim_nelekh', 'al_yosef_paro_hatel', 'lo_nishar_echad', 'va_yakhbed_paro_et_libo'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
