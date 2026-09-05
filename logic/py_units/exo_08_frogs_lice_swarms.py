#!/usr/bin/env python3
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
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹אֱמֹר אֶל־אַהֲרֹן נְטֵה› (“say to Aaron stretch”)
# ‹אֶת־יָדְךָ בְּמַטֶּךָ עַל־הַנְּהָרֹת› (“obj-marker hand-you/your in-
# staff/tribe-you/your over the-river”)
# ‹עַל־הַיְאֹרִים וְעַל־הָאֲגַמִּים וְהַעַל› (“over the-Nile and-over the-
# marsh and-go-up”)
# ‹אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ מִצְרָיִם› (“obj-marker the-marsh-leaper
# over earth Egypt”)
# "[EN-AID] And the LORD said to Moses: Say to Aaron: Stretch out your hand
# with your staff over the rivers, over the Niles, and over the pools, and
# bring up the frogs onto the land of Egypt."
m.step("Exod.8.1")
# ‹וְהַעַל אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ› (“and-go-up obj-marker the-marsh-
# leaper over earth”)
# ‹מִצְרָיִם› (“Egypt”)
# — the-LORD speaks a demand — LET: and-go-up-obj-marker-the-tzfardeim
m.declare("YHWH", "LET",
          "ve_haal_et_ha_tzfardeim")

# -------------------------- Exod.8.2 · THE_FROG_CAME_UP --------------------
# ‹וַיֵּט אַהֲרֹן אֶת־יָדוֹ› (“and-stretch Aaron obj-marker hand-him/its”)
# ‹עַל מֵימֵי מִצְרָיִם› (“over waters Egypt”)
# ‹וַתַּעַל הַצְּפַרְדֵּעַ וַתְּכַס› (“and-go-up the-marsh-leaper and-
# plump”)
# ‹אֶת־אֶרֶץ מִצְרָיִם› (“obj-marker earth Egypt”)
# "[EN-AID] And Aaron stretched out his hand over the waters of Egypt; and
# the frog came up, and covered the land of Egypt."
m.step("Exod.8.2")
# ‹וַתַּעַל הַצְּפַרְדֵּעַ וַתְּכַס› (“and-go-up the-marsh-leaper and-
# plump”)
# ‹אֶת־אֶרֶץ מִצְרָיִם› (“obj-marker earth Egypt”)
# — demand settled (popped from the queue): and-go-up-obj-marker-the-
# tzfardeim
m.result("ve_haal_et_ha_tzfardeim", tmark="t1")

# -------------------------- Exod.8.3 · THE_MAGICIANS_MATCH_FROGS -----------
# ‹וַיַּעֲשׂוּ־כֵן הַחֲרְטֻמִּים בְּלָטֵיהֶם› (“and-make so the-horoscopist
# in-covered-them/their”)
# ‹וַיַּעֲלוּ אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ› (“and-go-up obj-marker the-
# marsh-leaper over earth”)
# ‹מִצְרָיִם› (“Egypt”)
# "[EN-AID] And the magicians did so with their secret arts, and brought up
# the frogs onto the land of Egypt."
m.step("Exod.8.3")
# ‹וַיַּעֲלוּ אֶת־הַצְפַרְדְּעִים עַל־אֶרֶץ› (“and-go-up obj-marker the-
# marsh-leaper over earth”)
# ‹מִצְרָיִם› (“Egypt”)
# — fact holds: and-go-up-the-horoscopist
m.fact("va_yaalu_ha_chartumim")

# -------------------------- Exod.8.4 · PHARAOHS_FIRST_BARGAIN --------------
# ‹וַיִּקְרָא פַרְעֹה לְמֹשֶׁה› (“and-call Pharaoh to-Moses”)
# ‹וּלְאַהֲרֹן וַיֹּאמֶר הַעְתִּירוּ› (“and-to-Aaron and-say burn-incense-
# in-worship”)
# ‹אֶל־יְהוָה וְיָסֵר הַצְפַרְדְּעִים› (“to YHWH and-turn-aside the-marsh-
# leaper”)
# ‹מִמֶּנִּי וּמֵעַמִּי וַאֲשַׁלְּחָה› (“from-me/my and-from-people-me/my
# and-send”)
# ‹אֶת־הָעָם וְיִזְבְּחוּ לַיהוָה› (“obj-marker the-people and-slaughter-an-
# animal to-YHWH”)
# "[EN-AID] And Pharaoh called for Moses and for Aaron, and said: Entreat
# the LORD, that He take away the frogs from me and from my people; and I
# will send the people, that they may sacrifice to the LORD."
m.step("Exod.8.4")
# ‹הַעְתִּירוּ אֶל־יְהוָה וְיָסֵר› (“burn-incense-in-worship to YHWH and-
# turn-aside”)
# ‹הַצְפַרְדְּעִים מִמֶּנִּי וּמֵעַמִּי› (“the-marsh-leaper from-me/my and-
# from-people-me/my”)
# — Pharaoh speaks a demand — LET: burn-incense-in-worship-to-the-LORD
m.declare("paro", "LET",
          "hatiru_el_YHWH")

# -------------------------- Exod.8.5 · GLORY_OVER_ME -----------------------
# ‹וַיֹּאמֶר מֹשֶׁה לְפַרְעֹה› (“and-say Moses to-Pharaoh”)
# ‹הִתְפָּאֵר עָלַי לְמָתַי› (“gleam over-me/my to-extent”)
# ‹אַעְתִּיר לְךָ וְלַעֲבָדֶיךָ› (“burn-incense-in-worship to-you/your and-
# to-servant-you/your”)
# ‹וּלְעַמְּךָ לְהַכְרִית הַצֲפַרְדְּעִים› (“and-to-people-you/your to-cut
# the-marsh-leaper”)
# ‹מִמְּךָ וּמִבָּתֶּיךָ רַק› (“from-you/your and-from-house-you/your
# leanness”)
# ‹בַּיְאֹר תִּשָּׁאַרְנָה› (“in-Nile swell-up”)
# "[EN-AID] And Moses said to Pharaoh: Glory over me — for when shall I
# entreat for you, and for your servants, and for your people, to cut off
# the frogs from you and from your houses? Only in the Nile shall they
# remain."
m.step("Exod.8.5")
# ‹הִתְפָּאֵר עָלַי לְמָתַי› (“gleam over-me/my to-extent”)
# ‹אַעְתִּיר לְךָ› (“burn-incense-in-worship to-you/your”)
# — fact holds: gleam-alai-to-matai
m.fact("hitpaer_alai_le_matai")

# -------------------------- Exod.8.6 · FOR_TOMORROW ------------------------
# ‹וַיֹּאמֶר לְמָחָר וַיֹּאמֶר› (“and-say to-deferred and-say”)
# ‹כִּדְבָרְךָ לְמַעַן תֵּדַע› (“like-word/thing-you/your so-that know”)
# ‹כִּי־אֵין כַּיהוָה אֱלֹהֵינוּ› (“that there-is-not like-YHWH God-us/our”)
# "[EN-AID] And he said: For tomorrow. And he said: According to your word —
# that you may know that there is none like the LORD our God."
m.step("Exod.8.6")
# ‹לְמַעַן תֵּדַע כִּי־אֵין› (“so-that know that there-is-not”)
# ‹כַּיהוָה אֱלֹהֵינוּ› (“like-YHWH God-us/our”)
# — fact holds: that-devarkha-so-that-know
m.fact("ki_devarkha_lemaan_teda")

# -------------------------- Exod.8.7 · THE_REMOVAL_FORECAST ----------------
# ‹וְסָרוּ הַצְפַרְדְּעִים מִמְּךָ› (“and-turn-aside the-marsh-leaper from-
# you/your”)
# ‹וּמִבָּתֶּיךָ וּמֵעֲבָדֶיךָ וּמֵעַמֶּךָ› (“and-from-house-you/your and-
# from-servant-you/your and-from-people-you/your”)
# ‹רַק בַּיְאֹר תִּשָּׁאַרְנָה› (“leanness in-Nile swell-up”)
# "[EN-AID] And the frogs shall turn aside from you, and from your houses,
# and from your servants, and from your people; only in the Nile shall they
# remain."
m.step("Exod.8.7")
# ‹וְסָרוּ הַצְפַרְדְּעִים מִמְּךָ› (“and-turn-aside the-marsh-leaper from-
# you/your”)
# ‹וּמִבָּתֶּיךָ וּמֵעֲבָדֶיךָ וּמֵעַמֶּךָ› (“and-from-house-you/your and-
# from-servant-you/your and-from-people-you/your”)
# — fact holds: and-turn-aside-the-tzfardeim
m.fact("ve_saru_ha_tzfardeim")

# -------------------------- Exod.8.8 · MOSES_CRIES_TO_YHWH -----------------
# ‹וַיֵּצֵא מֹשֶׁה וְאַהֲרֹן› (“and-bring-forth Moses and-Aaron”)
# ‹מֵעִם פַּרְעֹה וַיִּצְעַק› (“from-with Pharaoh and-shriek”)
# ‹מֹשֶׁה אֶל־יְהוָה עַל־דְּבַר› (“Moses to YHWH over word/thing”)
# ‹הַצְפַרְדְּעִים אֲשֶׁר־שָׂם לְפַרְעֹה› (“the-marsh-leaper which put/set
# to-Pharaoh”)
# "[EN-AID] And Moses and Aaron went out from Pharaoh; and Moses cried to
# the LORD over the matter of the frogs which He had set upon Pharaoh."
m.step("Exod.8.8")
# ‹וַיִּצְעַק מֹשֶׁה אֶל־יְהוָה› (“and-shriek Moses to YHWH”)
# — demand settled (popped from the queue): burn-incense-in-worship-to-the-
# LORD
m.result("hatiru_el_YHWH", tmark="t1")

# -------------------------- Exod.8.9 · PER_THE_WORD_OF_MOSES ---------------
# ‹וַיַּעַשׂ יְהוָה כִּדְבַר› (“and-make YHWH like-word/thing”)
# ‹מֹשֶׁה וַיָּמֻתוּ הַצְפַרְדְּעִים› (“Moses and-die the-marsh-leaper”)
# ‹מִן־הַבָּתִּים מִן־הַחֲצֵרֹת וּמִן־הַשָּׂדֹת› (“from the-house from the-
# yard and-from the-field”)
# "[EN-AID] And the LORD did according to the word of Moses; and the frogs
# died from the houses, from the courtyards, and from the fields."
m.step("Exod.8.9")
# ‹וַיַּעַשׂ יְהוָה כִּדְבַר› (“and-make YHWH like-word/thing”)
# ‹מֹשֶׁה› (“Moses”)
# — fact holds: and-make-the-LORD-that-word/thing-Moses
m.fact("va_yaas_YHWH_ki_devar_moshe")

# -------------------------- Exod.8.10 · HEAPS_UPON_HEAPS -------------------
# ‹וַיִּצְבְּרוּ אֹתָם חֳמָרִם› (“and-aggregate obj-marker-them/their
# bubbling-up”)
# ‹חֳמָרִם וַתִּבְאַשׁ הָאָרֶץ› (“bubbling-up and-smell-bad the-earth”)
# "[EN-AID] And they gathered them heaps upon heaps; and the land stank."
m.step("Exod.8.10")
# ‹חֳמָרִם חֳמָרִם› (“bubbling-up bubbling-up”)
# — fact holds: bubbling-up-bubbling-up
m.fact("chomarim_chomarim")

# -------------------------- Exod.8.11 · THE_BREATHING_SPACE ----------------
# ‹וַיַּרְא פַּרְעֹה כִּי› (“and-see Pharaoh that”)
# ‹הָיְתָה הָרְוָחָה וְהַכְבֵּד› (“be the-relief and-be-heavy”)
# ‹אֶת־לִבּוֹ וְלֹא שָׁמַע› (“obj-marker heart-him/its and-not hear”)
# ‹אֲלֵהֶם כַּאֲשֶׁר דִּבֶּר› (“to-them/their like-as/which speak”)
# ‹יְהוָה› (“YHWH”)
# "[EN-AID] And Pharaoh saw that there was relief, and he made his heart
# heavy, and did not hear them, as the LORD had spoken."
m.step("Exod.8.11")
# ‹וְהַכְבֵּד אֶת־לִבּוֹ› (“and-be-heavy obj-marker heart-him/its”)
# — fact holds: and-be-heavy-obj-marker-His-heart
m.fact("ve_hakhbed_et_libo")

# -------------------------- Exod.8.12 · STRIKE_THE_DUST --------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹אֱמֹר אֶל־אַהֲרֹן נְטֵה› (“say to Aaron stretch”)
# ‹אֶת־מַטְּךָ וְהַךְ אֶת־עֲפַר› (“obj-marker staff/tribe-you/your and-
# strike obj-marker dust”)
# ‹הָאָרֶץ וְהָיָה לְכִנִּם› (“the-earth and-be to-gnat”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם› (“in-all earth Egypt”)
# "[EN-AID] And the LORD said to Moses: Say to Aaron: Stretch out your
# staff, and strike the dust of the earth, and it shall become lice in all
# the land of Egypt."
m.step("Exod.8.12")
# ‹נְטֵה אֶת־מַטְּךָ וְהַךְ› (“stretch obj-marker staff/tribe-you/your and-
# strike”)
# ‹אֶת־עֲפַר הָאָרֶץ› (“obj-marker dust the-earth”)
# — the-LORD speaks a demand — LET: and-strike-obj-marker-dust-the-earth
m.declare("YHWH", "LET",
          "ve_hakh_et_afar_ha_aretz")

# -------------------------- Exod.8.13 · THE_DUST_BECOMES_LICE --------------
# ‹וַיַּעֲשׂוּ־כֵן וַיֵּט אַהֲרֹן› (“and-make so and-stretch Aaron”)
# ‹אֶת־יָדוֹ בְמַטֵּהוּ וַיַּךְ› (“obj-marker hand-him/its in-staff/tribe-
# him/its and-strike”)
# ‹אֶת־עֲפַר הָאָרֶץ וַתְּהִי› (“obj-marker dust the-earth and-be”)
# ‹הַכִּנָּם בָּאָדָם וּבַבְּהֵמָה› (“the-gnat in-human and-in-livestock”)
# ‹כָּל־עֲפַר הָאָרֶץ הָיָה› (“all dust the-earth be”)
# ‹כִנִּים בְּכָל־אֶרֶץ מִצְרָיִם› (“gnat in-all earth Egypt”)
# "[EN-AID] And they did so: and Aaron stretched out his hand with his
# staff, and struck the dust of the earth, and the lice came on man and on
# beast; all the dust of the earth became lice in all the land of Egypt."
m.step("Exod.8.13")
# ‹כָּל־עֲפַר הָאָרֶץ הָיָה› (“all dust the-earth be”)
# ‹כִנִּים בְּכָל־אֶרֶץ מִצְרָיִם› (“gnat in-all earth Egypt”)
# — demand settled (popped from the queue): and-strike-obj-marker-dust-the-
# earth
m.result("ve_hakh_et_afar_ha_aretz", tmark="t1")

# -------------------------- Exod.8.14 · THE_CRAFT_FAILS --------------------
# ‹וַיַּעֲשׂוּ־כֵן הַחַרְטֻמִּים בְּלָטֵיהֶם› (“and-make so the-horoscopist
# in-covered-them/their”)
# ‹לְהוֹצִיא אֶת־הַכִּנִּים וְלֹא› (“to-bring-forth obj-marker the-gnat and-
# not”)
# ‹יָכֹלוּ וַתְּהִי הַכִּנָּם› (“be-able and-be the-gnat”)
# ‹בָּאָדָם וּבַבְּהֵמָה› (“in-human and-in-livestock”)
# "[EN-AID] And the magicians did so with their secret arts, to bring forth
# the lice — but they could not; and the lice were on man and on beast."
m.step("Exod.8.14")
# ‹וְלֹא יָכֹלוּ› (“and-not be-able”)
# — fact holds: and-not-be-able
m.fact("ve_lo_yakholu")

# -------------------------- Exod.8.15 · THE_FINGER_OF_GOD ------------------
# ‹וַיֹּאמְרוּ הַחַרְטֻמִּים אֶל־פַּרְעֹה› (“and-say the-horoscopist to
# Pharaoh”)
# ‹אֶצְבַּע אֱלֹהִים הִוא› (“something-to-sieze-with God he/it”)
# ‹וַיֶּחֱזַק לֵב־פַּרְעֹה וְלֹא־שָׁמַע› (“and-fasten-upon heart Pharaoh
# and-not hear”)
# ‹אֲלֵהֶם כַּאֲשֶׁר דִּבֶּר› (“to-them/their like-as/which speak”)
# ‹יְהוָה› (“YHWH”)
# "[EN-AID] And the magicians said to Pharaoh: It is the finger of God. And
# Pharaoh's heart was strengthened, and he did not hear them, as the LORD
# had spoken."
m.step("Exod.8.15")
# ‹אֶצְבַּע אֱלֹהִים הִוא› (“something-to-sieze-with God he/it”)
# — fact holds: something-to-sieze-with-God-he/it
m.fact("etzba_elohim_hiv")

# -------------------------- Exod.8.16 · RISE_EARLY_STAND_BEFORE ------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב› (“rise-early in-morning and-place”)
# ‹לִפְנֵי פַרְעֹה הִנֵּה› (“to-face Pharaoh behold”)
# ‹יוֹצֵא הַמָּיְמָה וְאָמַרְתָּ› (“bring-forth the-waters-ward and-say”)
# ‹אֵלָיו כֹּה אָמַר› (“to-him/its like-this say”)
# ‹יְהוָה שַׁלַּח עַמִּי› (“YHWH send people-me/my”)
# ‹וְיַעַבְדֻנִי› (“and-work/serve-me/my”)
# "[EN-AID] And the LORD said to Moses: Rise early in the morning, and
# station yourself before Pharaoh — behold, he goes out to the water — and
# say to him: Thus says the LORD: Send My people, that they may serve Me."
m.step("Exod.8.16")
# ‹הַשְׁכֵּם בַּבֹּקֶר וְהִתְיַצֵּב› (“rise-early in-morning and-place”)
# ‹לִפְנֵי פַרְעֹה› (“to-face Pharaoh”)
# — the-LORD speaks a demand — LET: rise-early-and-place-lifne-Pharaoh
m.declare("YHWH", "LET",
          "hashkem_ve_hityatzev_lifne_paro")

# -------------------------- Exod.8.17 · THE_SWARMS_THREATENED --------------
# ‹כִּי אִם־אֵינְךָ מְשַׁלֵּחַ› (“very-widely-used-as-a-relati as-
# demonstrative there-is-not-you/your send”)
# ‹אֶת־עַמִּי הִנְנִי מַשְׁלִיחַ› (“obj-marker people-me/my lo!-me/my send”)
# ‹בְּךָ וּבַעֲבָדֶיךָ וּבְעַמְּךָ› (“in-you/your and-in-servant-you/your
# and-in-people-you/your”)
# ‹וּבְבָתֶּיךָ אֶת־הֶעָרֹב וּמָלְאוּ› (“and-in-house-you/your obj-marker
# the-mosquito and-fill”)
# ‹בָּתֵּי מִצְרַיִם אֶת־הֶעָרֹב› (“house Egyptian obj-marker the-mosquito”)
# ‹וְגַם הָאֲדָמָה אֲשֶׁר־הֵם› (“and-also the-ground which they”)
# ‹עָלֶיהָ› (“over-her/its”)
# "[EN-AID] For if you do not send My people — behold, I set loose upon you,
# and upon your servants, and upon your people, and into your houses, the
# swarms; and the houses of Egypt shall be full of the swarms, and also the
# ground on which they are."
m.step("Exod.8.17")
# ‹אֵינְךָ מְשַׁלֵּחַ אֶת־עַמִּי› (“there-is-not-you/your send obj-marker
# people-me/my”)
# ‹הִנְנִי מַשְׁלִיחַ בְּךָ› (“lo!-me/my send in-you/your”)
# — fact holds: behold-I-mashliach-obj-marker-he-mosquito
m.fact("hineni_mashliach_et_he_arov")

# -------------------------- Exod.8.18 · GOSHEN_SET_APART -------------------
# ‹וְהִפְלֵיתִי בַיּוֹם הַהוּא› (“and-distinguish in-day that”)
# ‹אֶת־אֶרֶץ גֹּשֶׁן אֲשֶׁר› (“obj-marker earth Goshen which”)
# ‹עַמִּי עֹמֵד עָלֶיהָ› (“people-me/my stand over-her/its”)
# ‹לְבִלְתִּי הֱיוֹת־שָׁם עָרֹב› (“to-failure-of be there mosquito”)
# ‹לְמַעַן תֵּדַע כִּי› (“so-that know that”)
# ‹אֲנִי יְהוָה בְּקֶרֶב› (“YHWH in-nearest-part”)
# ‹הָאָרֶץ› (“the-earth”)
# "[EN-AID] And I will set apart on that day the land of Goshen, on which My
# people stands, that no swarm shall be there — that you may know that I am
# the LORD in the midst of the earth."
m.step("Exod.8.18")
# ‹וְהִפְלֵיתִי בַיּוֹם הַהוּא› (“and-distinguish in-day that”)
# ‹אֶת־אֶרֶץ גֹּשֶׁן› (“obj-marker earth Goshen”)
# — fact holds: and-distinguish-obj-marker-earth-Goshen
m.fact("ve_hifleti_et_eretz_goshen")

# -------------------------- Exod.8.19 · THE_DIVISION_SET -------------------
# ‹וְשַׂמְתִּי פְדֻת בֵּין› (“and-put/set distinction between”)
# ‹עַמִּי וּבֵין עַמֶּךָ› (“people-me/my and-between people-you/your”)
# ‹לְמָחָר יִהְיֶה הָאֹת› (“to-deferred be the-signs”)
# ‹הַזֶּה› (“the-this”)
# "[EN-AID] And I will set a division between My people and your people; for
# tomorrow shall this sign be."
m.step("Exod.8.19")
# ‹וְשַׂמְתִּי פְדֻת בֵּין› (“and-put/set distinction between”)
# ‹עַמִּי וּבֵין עַמֶּךָ› (“people-me/my and-between people-you/your”)
# — fact holds: and-put/set-distinction
m.fact("ve_samti_fedut")

# -------------------------- Exod.8.20 · THE_LAND_RUINED --------------------
# ‹וַיַּעַשׂ יְהוָה כֵּן› (“and-make YHWH so”)
# ‹וַיָּבֹא עָרֹב כָּבֵד› (“and-come/bring mosquito heavy”)
# ‹בֵּיתָה פַרְעֹה וּבֵית› (“house-ward Pharaoh and-house”)
# ‹עֲבָדָיו וּבְכָל־אֶרֶץ מִצְרַיִם› (“servant-him/its and-in-all earth
# Egypt”)
# ‹תִּשָּׁחֵת הָאָרֶץ מִפְּנֵי› (“decay the-earth from-face”)
# ‹הֶעָרֹב› (“the-mosquito”)
# "[EN-AID] And the LORD did so; and heavy swarms came into the house of
# Pharaoh, and the house of his servants, and in all the land of Egypt the
# land was ruined from before the swarms."
m.step("Exod.8.20")
# ‹תִּשָּׁחֵת הָאָרֶץ מִפְּנֵי› (“decay the-earth from-face”)
# ‹הֶעָרֹב› (“the-mosquito”)
# — fact holds: decay-the-earth
m.fact("tishachet_ha_aretz")

# -------------------------- Exod.8.21 · SACRIFICE_IN_THE_LAND --------------
# ‹וַיִּקְרָא פַרְעֹה אֶל־מֹשֶׁה› (“and-call Pharaoh to Moses”)
# ‹וּלְאַהֲרֹן וַיֹּאמֶר לְכוּ› (“and-to-Aaron and-say go”)
# ‹זִבְחוּ לֵאלֹהֵיכֶם בָּאָרֶץ› (“slaughter-an-animal to-God-you/your(pl)
# in-earth”)
# "[EN-AID] And Pharaoh called to Moses and to Aaron, and said: Go,
# sacrifice to your God — in the land."
m.step("Exod.8.21")
# ‹וַיֹּאמֶר לְכוּ זִבְחוּ› (“and-say go slaughter-an-animal”)
# ‹לֵאלֹהֵיכֶם בָּאָרֶץ› (“to-God-you/your(pl) in-earth”)
# — Pharaoh speaks a demand — LET: go-slaughter-an-animal-in-the-earth
m.declare("paro", "LET",
          "lekhu_zivchu_ba_aretz")

# -------------------------- Exod.8.22 · NOT_RIGHT_TO_DO_SO -----------------
# ‹וַיֹּאמֶר מֹשֶׁה לֹא› (“and-say Moses not”)
# ‹נָכוֹן לַעֲשׂוֹת כֵּן› (“be-erect to-make so”)
# ‹כִּי תּוֹעֲבַת מִצְרַיִם› (“that something-disgusting Egyptian”)
# ‹נִזְבַּח לַיהוָה אֱלֹהֵינוּ› (“slaughter-an-animal to-YHWH God-us/our”)
# ‹הֵן נִזְבַּח אֶת־תּוֹעֲבַת› (“lo! slaughter-an-animal obj-marker
# something-disgusting”)
# ‹מִצְרַיִם לְעֵינֵיהֶם וְלֹא› (“Egyptian to-eye-them/their and-not”)
# ‹יִסְקְלֻנוּ› (“be-weighty-us/our”)
# "[EN-AID] And Moses said: It is not right to do so; for the abomination of
# Egypt we would sacrifice to the LORD our God — behold, if we sacrifice the
# abomination of Egypt before their eyes, will they not stone us?"
m.step("Exod.8.22")
# ‹לֹא נָכוֹן לַעֲשׂוֹת› (“not be-erect to-make”)
# ‹כֵּן› (“so”)
# — fact holds: not-be-erect-laasot-so
m.fact("lo_nakhon_laasot_ken")

# -------------------------- Exod.8.23 · THREE_DAYS_AS_HE_SAYS --------------
# ‹דֶּרֶךְ שְׁלֹשֶׁת יָמִים› (“way/road three day”)
# ‹נֵלֵךְ בַּמִּדְבָּר וְזָבַחְנוּ› (“go in-pasture and-slaughter-an-
# animal”)
# ‹לַיהוָה אֱלֹהֵינוּ כַּאֲשֶׁר› (“to-YHWH God-us/our like-as/which”)
# ‹יֹאמַר אֵלֵינוּ› (“say to-us/our”)
# "[EN-AID] A journey of three days we will go into the wilderness, and
# sacrifice to the LORD our God, as He shall say to us."
m.step("Exod.8.23")
# ‹דֶּרֶךְ שְׁלֹשֶׁת יָמִים› (“way/road three day”)
# ‹נֵלֵךְ בַּמִּדְבָּר› (“go in-pasture”)
# — fact holds: way/road-three-day-go
m.fact("derekh_sheloshet_yamim_nelekh")

# -------------------------- Exod.8.24 · ONLY_NOT_FAR -----------------------
# ‹וַיֹּאמֶר פַּרְעֹה אָנֹכִי› (“and-say Pharaoh”)
# ‹אֲשַׁלַּח אֶתְכֶם וּזְבַחְתֶּם› (“send obj-marker-you/your(pl) and-
# slaughter-an-animal”)
# ‹לַיהוָה אֱלֹהֵיכֶם בַּמִּדְבָּר› (“to-YHWH God-you/your(pl) in-pasture”)
# ‹רַק הַרְחֵק לֹא־תַרְחִיקוּ› (“leanness widen not widen”)
# ‹לָלֶכֶת הַעְתִּירוּ בַּעֲדִי› (“to-go burn-incense-in-worship in-up-to-
# me/my”)
# "[EN-AID] And Pharaoh said: I will send you, and you shall sacrifice to
# the LORD your God in the wilderness — only you shall not go far; entreat
# for me."
m.step("Exod.8.24")
# ‹הַעְתִּירוּ בַּעֲדִי› (“burn-incense-in-worship in-up-to-me/my”)
# — Pharaoh speaks a demand — LET: burn-incense-in-worship-baadi
m.declare("paro", "LET",
          "hatiru_baadi")

# -------------------------- Exod.8.25 · LET_PHARAOH_NOT_DECEIVE ------------
# ‹וַיֹּאמֶר מֹשֶׁה הִנֵּה› (“and-say Moses behold”)
# ‹אָנֹכִי יוֹצֵא מֵעִמָּךְ› (“bring-forth from-with-you/your”)
# ‹וְהַעְתַּרְתִּי אֶל־יְהוָה וְסָר› (“and-burn-incense-in-worship to YHWH
# and-turn-aside”)
# ‹הֶעָרֹב מִפַּרְעֹה מֵעֲבָדָיו› (“the-mosquito from-Pharaoh from-servant-
# him/its”)
# ‹וּמֵעַמּוֹ מָחָר רַק› (“and-from-people-him/its deferred leanness”)
# ‹אַל־יֹסֵף פַּרְעֹה הָתֵל› (“do-not add Pharaoh deride”)
# ‹לְבִלְתִּי שַׁלַּח אֶת־הָעָם› (“to-failure-of send obj-marker the-
# people”)
# ‹לִזְבֹּחַ לַיהוָה› (“to-slaughter-an-animal to-YHWH”)
# "[EN-AID] And Moses said: Behold, I go out from you, and I will entreat
# the LORD, and the swarms shall turn aside from Pharaoh, from his servants,
# and from his people tomorrow — only let Pharaoh not continue to deceive,
# not to send the people to sacrifice to the LORD."
m.step("Exod.8.25")
# ‹רַק אַל־יֹסֵף פַּרְעֹה› (“leanness do-not add Pharaoh”)
# ‹הָתֵל› (“deride”)
# — fact holds: over-add-Pharaoh-deride
m.fact("al_yosef_paro_hatel")

# -------------------------- Exod.8.26 · MOSES_ENTREATS ---------------------
# ‹וַיֵּצֵא מֹשֶׁה מֵעִם› (“and-bring-forth Moses from-with”)
# ‹פַּרְעֹה וַיֶּעְתַּר אֶל־יְהוָה› (“Pharaoh and-burn-incense-in-worship to
# YHWH”)
# "[EN-AID] And Moses went out from Pharaoh, and entreated the LORD."
m.step("Exod.8.26")
# ‹וַיֶּעְתַּר אֶל־יְהוָה› (“and-burn-incense-in-worship to YHWH”)
# — demand settled (popped from the queue): burn-incense-in-worship-baadi
m.result("hatiru_baadi", tmark="t1")

# -------------------------- Exod.8.27 · NOT_ONE_REMAINED -------------------
# ‹וַיַּעַשׂ יְהוָה כִּדְבַר› (“and-make YHWH like-word/thing”)
# ‹מֹשֶׁה וַיָּסַר הֶעָרֹב› (“Moses and-turn-aside the-mosquito”)
# ‹מִפַּרְעֹה מֵעֲבָדָיו וּמֵעַמּוֹ› (“from-Pharaoh from-servant-him/its
# and-from-people-him/its”)
# ‹לֹא נִשְׁאַר אֶחָד› (“not swell-up one”)
# "[EN-AID] And the LORD did according to the word of Moses, and turned
# aside the swarms from Pharaoh, from his servants, and from his people; not
# one remained."
m.step("Exod.8.27")
# ‹לֹא נִשְׁאַר אֶחָד› (“not swell-up one”)
# — fact holds: not-swell-up-one
m.fact("lo_nishar_echad")

# -------------------------- Exod.8.28 · THIS_TIME_ALSO ---------------------
# ‹וַיַּכְבֵּד פַּרְעֹה אֶת־לִבּוֹ› (“and-be-heavy Pharaoh obj-marker heart-
# him/its”)
# ‹גַּם בַּפַּעַם הַזֹּאת› (“also in-stroke the-this”)
# ‹וְלֹא שִׁלַּח אֶת־הָעָם› (“and-not send obj-marker the-people”)
# "[EN-AID] And Pharaoh made his heart heavy this time also, and did not
# send the people."
m.step("Exod.8.28")
# ‹וַיַּכְבֵּד פַּרְעֹה אֶת־לִבּוֹ› (“and-be-heavy Pharaoh obj-marker heart-
# him/its”)
# ‹גַּם בַּפַּעַם הַזֹּאת› (“also in-stroke the-this”)
# — fact holds: and-be-heavy-Pharaoh-obj-marker-His-heart
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
