#!/usr/bin/env python3
# =============================================================================
# exo_07_staff_and_blood — 7:1-29
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_07_staff_and_blood.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The staff and the blood (7:1-29)"""
from machine import Machine

m = Machine("exo_07_staff_and_blood")

# -------------------------- Exod.7.1 · SEE_I_HAVE_SET_YOU ------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹רְאֵה נְתַתִּיךָ אֱלֹהִים› (“see set-you/your God”)
# ‹לְפַרְעֹה וְאַהֲרֹן אָחִיךָ› (“to-Pharaoh and-Aaron brother-you/your”)
# ‹יִהְיֶה נְבִיאֶךָ› (“be prophet-you/your”)
# "[EN-AID] And the LORD said to Moses: See, I have set you as God to
# Pharaoh; and Aaron your brother shall be your prophet."
m.step("Exod.7.1")
# ‹רְאֵה נְתַתִּיךָ אֱלֹהִים› (“see set-you/your God”)
# ‹לְפַרְעֹה› (“to-Pharaoh”)
# — fact holds: netaticha-God-to-Pharaoh
m.fact("netaticha_elohim_le_faro")

# -------------------------- Exod.7.2 · THE_RELAY_STATED --------------------
# ‹אַתָּה תְדַבֵּר אֵת› (“you speak obj-marker”)
# ‹כָּל־אֲשֶׁר אֲצַוֶּךָּ וְאַהֲרֹן› (“all which command-you/your and-
# Aaron”)
# ‹אָחִיךָ יְדַבֵּר אֶל־פַּרְעֹה› (“brother-you/your speak to Pharaoh”)
# ‹וְשִׁלַּח אֶת־בְּנֵי־יִשְׂרָאֵל מֵאַרְצוֹ› (“and-send obj-marker son
# Israel from-earth-him/its”)
# "[EN-AID] You shall speak all that I command you; and Aaron your brother
# shall speak to Pharaoh, that he send the sons of Israel out of his land."
m.step("Exod.7.2")
# ‹אַתָּה תְדַבֵּר אֵת› (“you speak obj-marker”)
# ‹כָּל־אֲשֶׁר אֲצַוֶּךָּ› (“all which command-you/your”)
# — fact holds: you-speak-obj-marker-all-which-atzaveka
m.fact("ata_tedaber_et_kol_asher_atzaveka")

# -------------------------- Exod.7.3 · I_WILL_HARDEN -----------------------
# ‹וַאֲנִי אַקְשֶׁה אֶת־לֵב› (“and-I be-dense obj-marker heart”)
# ‹פַּרְעֹה וְהִרְבֵּיתִי אֶת־אֹתֹתַי› (“Pharaoh and-multiply obj-marker
# signs-me/my”)
# ‹וְאֶת־מוֹפְתַי בְּאֶרֶץ מִצְרָיִם› (“and-obj-marker miracle-me/my in-
# earth Egypt”)
# "[EN-AID] And I will harden Pharaoh's heart, and multiply My signs and My
# wonders in the land of Egypt."
m.step("Exod.7.3")
# ‹וַאֲנִי אַקְשֶׁה אֶת־לֵב› (“and-I be-dense obj-marker heart”)
# ‹פַּרְעֹה› (“Pharaoh”)
# — fact holds: and-I-be-dense-obj-marker-heart-Pharaoh
m.fact("va_ani_aqshe_et_lev_paro")

# -------------------------- Exod.7.4 · HE_WILL_NOT_HEAR --------------------
# ‹וְלֹא־יִשְׁמַע אֲלֵכֶם פַּרְעֹה› (“and-not hear to-you/your(pl) Pharaoh”)
# ‹וְנָתַתִּי אֶת־יָדִי בְּמִצְרָיִם› (“and-set obj-marker hand-me/my in-
# Egypt”)
# ‹וְהוֹצֵאתִי אֶת־צִבְאֹתַי אֶת־עַמִּי› (“and-bring-forth obj-marker host-
# me/my obj-marker people-me/my”)
# ‹בְנֵי־יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם› (“son Israel from-earth Egypt”)
# ‹בִּשְׁפָטִים גְּדֹלִים› (“in-sentence great”)
# "[EN-AID] And Pharaoh will not hear you; and I will lay My hand on Egypt,
# and bring out My hosts, My people the sons of Israel, from the land of
# Egypt with great judgments."
m.step("Exod.7.4")
# ‹וְהוֹצֵאתִי אֶת־צִבְאֹתַי אֶת־עַמִּי› (“and-bring-forth obj-marker host-
# me/my obj-marker people-me/my”)
# ‹בְנֵי־יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם› (“son Israel from-earth Egypt”)
# — fact holds: and-not-hear-alekhem-Pharaoh
m.fact("ve_lo_yishma_alekhem_paro")

# -------------------------- Exod.7.5 · EGYPT_SHALL_KNOW --------------------
# ‹וְיָדְעוּ מִצְרַיִם כִּי־אֲנִי› (“and-know Egyptian that”)
# ‹יְהוָה בִּנְטֹתִי אֶת־יָדִי› (“YHWH in-stretch-me/my obj-marker hand-
# me/my”)
# ‹עַל־מִצְרָיִם וְהוֹצֵאתִי אֶת־בְּנֵי־יִשְׂרָאֵל› (“over Egypt and-bring-
# forth obj-marker son Israel”)
# ‹מִתּוֹכָם› (“from-midst-them/their”)
# "[EN-AID] And Egypt shall know that I am the LORD, when I stretch out My
# hand over Egypt; and I will bring out the sons of Israel from among them."
m.step("Exod.7.5")
# ‹וְיָדְעוּ מִצְרַיִם כִּי־אֲנִי› (“and-know Egyptian that”)
# ‹יְהוָה› (“YHWH”)
# — fact holds: and-know-Egypt-that-I-the-LORD
m.fact("ve_yadu_mitzrayim_ki_ani_YHWH")

# -------------------------- Exod.7.6 · THEY_DID_AS_COMMANDED ---------------
# ‹וַיַּעַשׂ מֹשֶׁה וְאַהֲרֹן› (“and-make Moses and-Aaron”)
# ‹כַּאֲשֶׁר צִוָּה יְהוָה› (“like-as/which command YHWH”)
# ‹אֹתָם כֵּן עָשׂוּ› (“obj-marker-them/their so make”)
# "[EN-AID] And Moses and Aaron did as the LORD commanded them; so they
# did."
m.step("Exod.7.6")
# ‹כַּאֲשֶׁר צִוָּה יְהוָה› (“like-as/which command YHWH”)
# ‹אֹתָם כֵּן עָשׂוּ› (“obj-marker-them/their so make”)
# — fact holds: like-which-command-the-LORD-so-make
m.fact("ka_asher_tziva_YHWH_ken_asu")

# -------------------------- Exod.7.7 · EIGHTY_AND_EIGHTY_THREE -------------
# ‹וּמֹשֶׁה בֶּן־שְׁמֹנִים שָׁנָה› (“and-Moses son eighty years”)
# ‹וְאַהֲרֹן בֶּן־שָׁלֹשׁ וּשְׁמֹנִים› (“and-Aaron son three and-eighty”)
# ‹שָׁנָה בְּדַבְּרָם אֶל־פַּרְעֹה› (“years in-speak-them/their to Pharaoh”)
# "[EN-AID] And Moses was eighty years old, and Aaron eighty-three years
# old, when they spoke to Pharaoh."
m.step("Exod.7.7")
# ‹וּמֹשֶׁה בֶּן־שְׁמֹנִים שָׁנָה› (“and-Moses son eighty years”)
# — fact holds: and-Moses-son-eighty-years
m.fact("u_moshe_ben_shemonim_shana")

# -------------------------- Exod.7.8 · THE_COMPOUND_FRAME ------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹וְאֶל־אַהֲרֹן לֵאמֹר› (“and-to Aaron to-say”)
# "[EN-AID] And the LORD said to Moses and to Aaron, saying:"
m.step("Exod.7.8")
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹וְאֶל־אַהֲרֹן לֵאמֹר› (“and-to Aaron to-say”)
# — fact holds: and-say-the-LORD-to-Moses-and-to-Aaron
m.fact("va_yomer_YHWH_el_moshe_ve_el_aharon")

# -------------------------- Exod.7.9 · THE_WONDER_SCRIPT -------------------
# ‹כִּי יְדַבֵּר אֲלֵכֶם› (“that speak to-you/your(pl)”)
# ‹פַּרְעֹה לֵאמֹר תְּנוּ› (“Pharaoh to-say set”)
# ‹לָכֶם מוֹפֵת וְאָמַרְתָּ› (“to-you/your(pl) miracle and-say”)
# ‹אֶל־אַהֲרֹן קַח אֶת־מַטְּךָ› (“to Aaron take obj-marker staff/tribe-
# you/your”)
# ‹וְהַשְׁלֵךְ לִפְנֵי־פַרְעֹה יְהִי› (“and-throw-out to-face Pharaoh be”)
# ‹לְתַנִּין› (“to-sea-monster”)
# "[EN-AID] When Pharaoh speaks to you, saying: Give a wonder for yourselves
# — then you shall say to Aaron: Take your staff and throw it before
# Pharaoh; let it become a serpent."
m.step("Exod.7.9")
# ‹קַח אֶת־מַטְּךָ וְהַשְׁלֵךְ› (“take obj-marker staff/tribe-you/your and-
# throw-out”)
# ‹לִפְנֵי־פַרְעֹה יְהִי לְתַנִּין› (“to-face Pharaoh be to-sea-monster”)
# — the-LORD speaks a demand — LET: take-obj-marker-matkha-and-throw-out
m.declare("YHWH", "LET",
          "qach_et_matkha_ve_hashlekh")

# -------------------------- Exod.7.10 · PERFORMED_AS_COMMANDED -------------
# ‹וַיָּבֹא מֹשֶׁה וְאַהֲרֹן› (“and-come/bring Moses and-Aaron”)
# ‹אֶל־פַּרְעֹה וַיַּעַשׂוּ כֵן› (“to Pharaoh and-make so”)
# ‹כַּאֲשֶׁר צִוָּה יְהוָה› (“like-as/which command YHWH”)
# ‹וַיַּשְׁלֵךְ אַהֲרֹן אֶת־מַטֵּהוּ› (“and-throw-out Aaron obj-marker
# staff/tribe-him/its”)
# ‹לִפְנֵי פַרְעֹה וְלִפְנֵי› (“to-face Pharaoh and-to-face”)
# ‹עֲבָדָיו וַיְהִי לְתַנִּין› (“servant-him/its and-be to-sea-monster”)
# "[EN-AID] And Moses and Aaron came to Pharaoh, and they did so, as the
# LORD had commanded; and Aaron threw his staff before Pharaoh and before
# his servants, and it became a serpent."
m.step("Exod.7.10")
# ‹וַיַּשְׁלֵךְ אַהֲרֹן אֶת־מַטֵּהוּ› (“and-throw-out Aaron obj-marker
# staff/tribe-him/its”)
# ‹לִפְנֵי פַרְעֹה וְלִפְנֵי› (“to-face Pharaoh and-to-face”)
# ‹עֲבָדָיו וַיְהִי לְתַנִּין› (“servant-him/its and-be to-sea-monster”)
# — demand settled (popped from the queue): take-obj-marker-matkha-and-
# throw-out
m.result("qach_et_matkha_ve_hashlekh", tmark="t1")

# -------------------------- Exod.7.11 · THE_MAGICIANS_MATCH ----------------
# ‹וַיִּקְרָא גַּם־פַּרְעֹה לַחֲכָמִים› (“and-call also Pharaoh to-wise”)
# ‹וְלַמְכַשְּׁפִים וַיַּעֲשׂוּ גַם־הֵם› (“and-to-whisper-aspell and-make
# also they”)
# ‹חַרְטֻמֵּי מִצְרַיִם בְּלַהֲטֵיהֶם› (“horoscopist Egypt in-blaze-
# them/their”)
# ‹כֵּן› (“so”)
# "[EN-AID] And Pharaoh also called the wise men and the sorcerers; and they
# also, the magicians of Egypt, did so with their secret arts."
m.step("Exod.7.11")
# ‹וַיַּעֲשׂוּ גַם־הֵם חַרְטֻמֵּי› (“and-make also they horoscopist”)
# ‹מִצְרַיִם בְּלַהֲטֵיהֶם› (“Egypt in-blaze-them/their”)
# — fact holds: and-make-also-they-in-lahatehem
m.fact("va_yaasu_gam_hem_be_lahatehem")

# -------------------------- Exod.7.12 · THE_SWALLOWING ---------------------
# ‹וַיַּשְׁלִיכוּ אִישׁ מַטֵּהוּ› (“and-throw-out man staff/tribe-him/its”)
# ‹וַיִּהְיוּ לְתַנִּינִם וַיִּבְלַע› (“and-be to-sea-monster and-swallow”)
# ‹מַטֵּה־אַהֲרֹן אֶת־מַטֹּתָם› (“staff/tribe Aaron obj-marker staff/tribe-
# them/their”)
# "[EN-AID] And they threw down every man his staff, and they became
# serpents; and Aaron's staff swallowed their staffs."
m.step("Exod.7.12")
# ‹וַיִּבְלַע מַטֵּה־אַהֲרֹן אֶת־מַטֹּתָם› (“and-swallow staff/tribe Aaron
# obj-marker staff/tribe-them/their”)
# — event: bala — agent staff/tribe-Aaron
m.event("bala", agent="mate_aharon")

# -------------------------- Exod.7.13 · THE_HEART_STRENGTHENED -------------
# ‹וַיֶּחֱזַק לֵב פַּרְעֹה› (“and-fasten-upon heart Pharaoh”)
# ‹וְלֹא שָׁמַע אֲלֵהֶם› (“and-not hear to-them/their”)
# ‹כַּאֲשֶׁר דִּבֶּר יְהוָה› (“like-as/which speak YHWH”)
# "[EN-AID] And Pharaoh's heart was strengthened, and he did not hear them,
# as the LORD had spoken."
m.step("Exod.7.13")
# ‹וַיֶּחֱזַק לֵב פַּרְעֹה› (“and-fasten-upon heart Pharaoh”)
# — fact holds: and-fasten-upon-heart-Pharaoh
m.fact("va_yechezaq_lev_paro")

# -------------------------- Exod.7.14 · THE_HEAVY_HEART --------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹כָּבֵד לֵב פַּרְעֹה› (“heavy heart Pharaoh”)
# ‹מֵאֵן לְשַׁלַּח הָעָם› (“refuse to-send the-people”)
# "[EN-AID] And the LORD said to Moses: Pharaoh's heart is heavy; he refuses
# to send the people."
m.step("Exod.7.14")
# ‹כָּבֵד לֵב פַּרְעֹה› (“heavy heart Pharaoh”)
# — fact holds: heavy-heart-Pharaoh
m.fact("kaved_lev_paro")

# -------------------------- Exod.7.15 · THE_MORNING_STATION ----------------
# ‹לֵךְ אֶל־פַּרְעֹה בַּבֹּקֶר› (“go to Pharaoh in-morning”)
# ‹הִנֵּה יֹצֵא הַמַּיְמָה› (“behold bring-forth the-waters-ward”)
# ‹וְנִצַּבְתָּ לִקְרָאתוֹ עַל־שְׂפַת› (“and-stand to-encountering-him/its
# over lip”)
# ‹הַיְאֹר וְהַמַּטֶּה אֲשֶׁר־נֶהְפַּךְ› (“the-Nile and-the-staff/tribe
# which turn-about”)
# ‹לְנָחָשׁ תִּקַּח בְּיָדֶךָ› (“to-snake take in-hand-you/your”)
# "[EN-AID] Go to Pharaoh in the morning — behold, he goes out to the water
# — and station yourself to meet him on the bank of the Nile; and the staff
# which was turned to a snake take in your hand."
m.step("Exod.7.15")
# ‹לֵךְ אֶל־פַּרְעֹה בַּבֹּקֶר› (“go to Pharaoh in-morning”)
# — the-LORD speaks a demand — LET: go-to-Pharaoh-in-the-morning
m.declare("YHWH", "LET",
          "lekh_el_paro_ba_boqer")

# -------------------------- Exod.7.16 · THE_RIVERSIDE_SCRIPT ---------------
# ‹וְאָמַרְתָּ אֵלָיו יְהוָה› (“and-say to-him/its YHWH”)
# ‹אֱלֹהֵי הָעִבְרִים שְׁלָחַנִי› (“God the-Hebrew send-me/my”)
# ‹אֵלֶיךָ לֵאמֹר שַׁלַּח› (“to-you/your to-say send”)
# ‹אֶת־עַמִּי וְיַעַבְדֻנִי בַּמִּדְבָּר› (“obj-marker people-me/my and-
# work/serve-me/my in-pasture”)
# ‹וְהִנֵּה לֹא־שָׁמַעְתָּ עַד־כֹּה› (“and-behold not hear until like-this”)
# "[EN-AID] And you shall say to him: The LORD, the God of the Hebrews, sent
# me to you, saying: Send My people, that they may serve Me in the
# wilderness; and behold, you have not heard until now."
m.step("Exod.7.16")
# ‹שַׁלַּח אֶת־עַמִּי וְיַעַבְדֻנִי› (“send obj-marker people-me/my and-
# work/serve-me/my”)
# ‹בַּמִּדְבָּר› (“in-pasture”)
# — fact holds: send-obj-marker-ami-and-yaavduni
m.fact("shalach_et_ami_ve_yaavduni")

# -------------------------- Exod.7.17 · BY_THIS_YOU_SHALL_KNOW -------------
# ‹כֹּה אָמַר יְהוָה› (“like-this say YHWH”)
# ‹בְּזֹאת תֵּדַע כִּי› (“in-this know that”)
# ‹אֲנִי יְהוָה הִנֵּה› (“YHWH behold”)
# ‹אָנֹכִי מַכֶּה בַּמַּטֶּה› (“strike in-staff/tribe”)
# ‹אֲשֶׁר־בְּיָדִי עַל־הַמַּיִם אֲשֶׁר› (“which in-hand-me/my over the-
# waters which”)
# ‹בַּיְאֹר וְנֶהֶפְכוּ לְדָם› (“in-Nile and-turn-about to-blood”)
# "[EN-AID] Thus says the LORD: By this you shall know that I am the LORD —
# behold, I strike with the staff that is in my hand upon the waters that
# are in the Nile, and they shall be turned to blood."
m.step("Exod.7.17")
# ‹בְּזֹאת תֵּדַע כִּי› (“in-this know that”)
# ‹אֲנִי יְהוָה› (“YHWH”)
# — fact holds: in-this-know-that-I-the-LORD
m.fact("be_zot_teda_ki_ani_YHWH")

# -------------------------- Exod.7.18 · THE_NILE_UNDRINKABLE ---------------
# ‹וְהַדָּגָה אֲשֶׁר־בַּיְאֹר תָּמוּת› (“and-the-fish which in-Nile die”)
# ‹וּבָאַשׁ הַיְאֹר וְנִלְאוּ› (“and-smell-bad the-Nile and-tire”)
# ‹מִצְרַיִם לִשְׁתּוֹת מַיִם› (“Egyptian to-drink waters”)
# ‹מִן־הַיְאֹר› (“from the-Nile”)
# "[EN-AID] And the fish that is in the Nile shall die, and the Nile shall
# stink; and Egypt shall be weary of drinking water from the Nile."
m.step("Exod.7.18")
# ‹וְנִלְאוּ מִצְרַיִם לִשְׁתּוֹת› (“and-tire Egyptian to-drink”)
# ‹מַיִם› (“waters”)
# — fact holds: and-tire-Egypt-lishtot
m.fact("ve_nilu_mitzrayim_lishtot")

# -------------------------- Exod.7.19 · STRETCH_OUT_YOUR_HAND --------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹אֱמֹר אֶל־אַהֲרֹן קַח› (“say to Aaron take”)
# ‹מַטְּךָ וּנְטֵה־יָדְךָ עַל־מֵימֵי› (“staff/tribe-you/your and-stretch
# hand-you/your over waters”)
# ‹מִצְרַיִם עַל־נַהֲרֹתָם עַל־יְאֹרֵיהֶם› (“Egypt over river-them/their
# over Nile-them/their”)
# ‹וְעַל־אַגְמֵיהֶם וְעַל כָּל־מִקְוֵה› (“and-over marsh-them/their and-over
# all gathering”)
# ‹מֵימֵיהֶם וְיִהְיוּ־דָם וְהָיָה› (“waters-them/their and-be blood and-
# be”)
# ‹דָם בְּכָל־אֶרֶץ מִצְרַיִם› (“blood in-all earth Egypt”)
# ‹וּבָעֵצִים וּבָאֲבָנִים› (“and-in-tree and-in-stone”)
# "[EN-AID] And the LORD said to Moses: Say to Aaron: Take your staff and
# stretch out your hand over the waters of Egypt — over their rivers, over
# their Niles, and over their pools, and over every gathering of their
# waters — and they shall become blood; and there shall be blood in all the
# land of Egypt, both in the wooden vessels and in the stone vessels."
m.step("Exod.7.19")
# ‹אֱמֹר אֶל־אַהֲרֹן קַח› (“say to Aaron take”)
# ‹מַטְּךָ וּנְטֵה־יָדְךָ עַל־מֵימֵי› (“staff/tribe-you/your and-stretch
# hand-you/your over waters”)
# ‹מִצְרַיִם› (“Egypt”)
# — the-LORD speaks a demand — LET: stretch-yadkha-over-waters-Egypt
m.declare("YHWH", "LET",
          "nete_yadkha_al_meme_mitzrayim")

# -------------------------- Exod.7.20 · THE_NILE_STRUCK --------------------
# ‹וַיַּעֲשׂוּ־כֵן מֹשֶׁה וְאַהֲרֹן› (“and-make so Moses and-Aaron”)
# ‹כַּאֲשֶׁר צִוָּה יְהוָה› (“like-as/which command YHWH”)
# ‹וַיָּרֶם בַּמַּטֶּה וַיַּךְ› (“and-rise-high in-staff/tribe and-strike”)
# ‹אֶת־הַמַּיִם אֲשֶׁר בַּיְאֹר› (“obj-marker the-waters which in-Nile”)
# ‹לְעֵינֵי פַרְעֹה וּלְעֵינֵי› (“to-eye Pharaoh and-to-eye”)
# ‹עֲבָדָיו וַיֵּהָפְכוּ כָּל־הַמַּיִם› (“servant-him/its and-turn-about all
# the-waters”)
# ‹אֲשֶׁר־בַּיְאֹר לְדָם› (“which in-Nile to-blood”)
# "[EN-AID] And Moses and Aaron did so, as the LORD commanded; and he raised
# the staff and struck the waters that were in the Nile, before the eyes of
# Pharaoh and before the eyes of his servants; and all the waters that were
# in the Nile were turned to blood."
m.step("Exod.7.20")
# ‹וַיָּרֶם בַּמַּטֶּה וַיַּךְ› (“and-rise-high in-staff/tribe and-strike”)
# ‹אֶת־הַמַּיִם אֲשֶׁר בַּיְאֹר› (“obj-marker the-waters which in-Nile”)
# — demand settled (popped from the queue): stretch-yadkha-over-waters-Egypt
m.result("nete_yadkha_al_meme_mitzrayim", tmark="t1")

# -------------------------- Exod.7.21 · THE_FISH_DIED ----------------------
# ‹וְהַדָּגָה אֲשֶׁר־בַּיְאֹר מֵתָה› (“and-the-fish which in-Nile die”)
# ‹וַיִּבְאַשׁ הַיְאֹר וְלֹא־יָכְלוּ› (“and-smell-bad the-Nile and-not be-
# able”)
# ‹מִצְרַיִם לִשְׁתּוֹת מַיִם› (“Egyptian to-drink waters”)
# ‹מִן־הַיְאֹר וַיְהִי הַדָּם› (“from the-Nile and-be the-blood”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם› (“in-all earth Egypt”)
# "[EN-AID] And the fish that was in the Nile died, and the Nile stank, and
# Egypt could not drink water from the Nile; and the blood was in all the
# land of Egypt."
m.step("Exod.7.21")
# ‹וַיִּבְאַשׁ הַיְאֹר› (“and-smell-bad the-Nile”)
# — fact holds: and-smell-bad-the-Nile
m.fact("va_yivash_ha_yeor")

# -------------------------- Exod.7.22 · THE_MAGICIANS_MATCH_AGAIN ----------
# ‹וַיַּעֲשׂוּ־כֵן חַרְטֻמֵּי מִצְרַיִם› (“and-make so horoscopist Egypt”)
# ‹בְּלָטֵיהֶם וַיֶּחֱזַק לֵב־פַּרְעֹה› (“in-covered-them/their and-fasten-
# upon heart Pharaoh”)
# ‹וְלֹא־שָׁמַע אֲלֵהֶם כַּאֲשֶׁר› (“and-not hear to-them/their like-
# as/which”)
# ‹דִּבֶּר יְהוָה› (“speak YHWH”)
# "[EN-AID] And the magicians of Egypt did so with their secret arts; and
# Pharaoh's heart was strengthened, and he did not hear them, as the LORD
# had spoken."
m.step("Exod.7.22")
# ‹וַיֶּחֱזַק לֵב־פַּרְעֹה וְלֹא־שָׁמַע› (“and-fasten-upon heart Pharaoh
# and-not hear”)
# ‹אֲלֵהֶם› (“to-them/their”)
# — fact holds: and-fasten-upon-heart-Pharaoh-2
m.fact("va_yechezaq_lev_paro_2")

# -------------------------- Exod.7.23 · PHARAOH_TURNS_HOME -----------------
# ‹וַיִּפֶן פַּרְעֹה וַיָּבֹא› (“and-turn Pharaoh and-come/bring”)
# ‹אֶל־בֵּיתוֹ וְלֹא־שָׁת לִבּוֹ› (“to house-him/its and-not place heart-
# him/its”)
# ‹גַּם־לָזֹאת› (“also to-this”)
# "[EN-AID] And Pharaoh turned and came into his house; and he did not set
# his heart even to this."
m.step("Exod.7.23")
# ‹וְלֹא־שָׁת לִבּוֹ גַּם־לָזֹאת› (“and-not place heart-him/its also to-
# this”)
# — fact holds: and-not-place-His-heart-also-to-this
m.fact("ve_lo_shat_libo_gam_la_zot")

# -------------------------- Exod.7.24 · EGYPT_DIGS -------------------------
# ‹וַיַּחְפְּרוּ כָל־מִצְרַיִם סְבִיבֹת› (“and-dig all Egyptian circle”)
# ‹הַיְאֹר מַיִם לִשְׁתּוֹת› (“the-Nile waters to-drink”)
# ‹כִּי לֹא יָכְלוּ› (“that not be-able”)
# ‹לִשְׁתֹּת מִמֵּימֵי הַיְאֹר› (“to-drink from-waters the-Nile”)
# "[EN-AID] And all Egypt dug round about the Nile for water to drink; for
# they could not drink of the waters of the Nile."
m.step("Exod.7.24")
# ‹וַיַּחְפְּרוּ כָל־מִצְרַיִם סְבִיבֹת› (“and-dig all Egyptian circle”)
# ‹הַיְאֹר מַיִם לִשְׁתּוֹת› (“the-Nile waters to-drink”)
# — fact holds: and-dig-all-Egypt
m.fact("va_yachpru_khol_mitzrayim")

# -------------------------- Exod.7.25 · SEVEN_DAYS_FILLED ------------------
# ‹וַיִּמָּלֵא שִׁבְעַת יָמִים› (“and-fill seven day”)
# ‹אַחֲרֵי הַכּוֹת־יְהוָה אֶת־הַיְאֹר› (“after strike YHWH obj-marker the-
# Nile”)
# "[EN-AID] And seven days were filled, after the LORD had struck the Nile."
m.step("Exod.7.25")
# ‹וַיִּמָּלֵא שִׁבְעַת יָמִים› (“and-fill seven day”)
# — fact holds: and-fill-seven-day
m.fact("va_yimale_shivat_yamim")

# -------------------------- Exod.7.26 · GO_SAY_SEND ------------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹בֹּא אֶל־פַּרְעֹה וְאָמַרְתָּ› (“come/bring to Pharaoh and-say”)
# ‹אֵלָיו כֹּה אָמַר› (“to-him/its like-this say”)
# ‹יְהוָה שַׁלַּח אֶת־עַמִּי› (“YHWH send obj-marker people-me/my”)
# ‹וְיַעַבְדֻנִי› (“and-work/serve-me/my”)
# "[EN-AID] And the LORD said to Moses: Come to Pharaoh, and say to him:
# Thus says the LORD: Send My people, that they may serve Me."
m.step("Exod.7.26")
# ‹בֹּא אֶל־פַּרְעֹה› (“come/bring to Pharaoh”)
# — the-LORD speaks a demand — LET: come/bring-to-Pharaoh-and-say
m.declare("YHWH", "LET",
          "bo_el_paro_ve_amarta")

# -------------------------- Exod.7.27 · IF_YOU_REFUSE_FROGS ----------------
# ‹וְאִם־מָאֵן אַתָּה לְשַׁלֵּחַ› (“and-if unwilling you to-send”)
# ‹הִנֵּה אָנֹכִי נֹגֵף› (“behold push”)
# ‹אֶת־כָּל־גְּבוּלְךָ בַּצְפַרְדְּעִים› (“obj-marker all cord-you/your in-
# marsh-leaper”)
# "[EN-AID] And if you refuse to send them — behold, I strike all your
# border with frogs."
m.step("Exod.7.27")
# ‹הִנֵּה אָנֹכִי נֹגֵף› (“behold push”)
# ‹אֶת־כָּל־גְּבוּלְךָ בַּצְפַרְדְּעִים› (“obj-marker all cord-you/your in-
# marsh-leaper”)
# — fact holds: and-if-unwilling-you-to-shaleach
m.fact("ve_im_maen_ata_le_shaleach")

# -------------------------- Exod.7.28 · THE_INVASION_ROUTE -----------------
# ‹וְשָׁרַץ הַיְאֹר צְפַרְדְּעִים› (“and-swarm the-Nile marsh-leaper”)
# ‹וְעָלוּ וּבָאוּ בְּבֵיתֶךָ› (“and-go-up and-come/bring in-house-
# you/your”)
# ‹וּבַחֲדַר מִשְׁכָּבְךָ וְעַל־מִטָּתֶךָ› (“and-in-apartment bed-you/your
# and-over bed-forsleeping-you/your”)
# ‹וּבְבֵית עֲבָדֶיךָ וּבְעַמֶּךָ› (“and-in-house servant-you/your and-in-
# people-you/your”)
# ‹וּבְתַנּוּרֶיךָ וּבְמִשְׁאֲרוֹתֶיךָ› (“and-in-fire-pot-you/your and-in-
# kneading-trough-you/your”)
# "[EN-AID] And the Nile shall swarm frogs, and they shall come up and come
# into your house, and into your bedchamber, and onto your bed, and into the
# house of your servants, and among your people, and into your ovens, and
# into your kneading-troughs."
m.step("Exod.7.28")
# ‹וְשָׁרַץ הַיְאֹר צְפַרְדְּעִים› (“and-swarm the-Nile marsh-leaper”)
# — fact holds: and-swarm-the-Nile-tzfardeim
m.fact("ve_sharatz_ha_yeor_tzfardeim")

# -------------------------- Exod.7.29 · AND_INTO_YOU -----------------------
# ‹וּבְכָה וּבְעַמְּךָ וּבְכָל־עֲבָדֶיךָ› (“and-in-you/your and-in-people-
# you/your and-in-all servant-you/your”)
# ‹יַעֲלוּ הַצְפַרְדְּעִים› (“go-up the-marsh-leaper”)
# "[EN-AID] And into you, and into your people, and into all your servants,
# the frogs shall come up."
m.step("Exod.7.29")
# ‹וּבְכָה וּבְעַמְּךָ וּבְכָל־עֲבָדֶיךָ› (“and-in-you/your and-in-people-
# you/your and-in-all servant-you/your”)
# — fact holds: and-vekha-and-and-amkha
m.fact("u_vekha_u_ve_amkha")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['lekh_el_paro_ba_boqer', 'bo_el_paro_ve_amarta']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['netaticha_elohim_le_faro', 'ata_tedaber_et_kol_asher_atzaveka', 'va_ani_aqshe_et_lev_paro', 've_lo_yishma_alekhem_paro', 've_yadu_mitzrayim_ki_ani_YHWH', 'ka_asher_tziva_YHWH_ken_asu', 'u_moshe_ben_shemonim_shana', 'va_yomer_YHWH_el_moshe_ve_el_aharon', 'va_yaasu_gam_hem_be_lahatehem', 'va_yechezaq_lev_paro', 'kaved_lev_paro', 'shalach_et_ami_ve_yaavduni', 'be_zot_teda_ki_ani_YHWH', 've_nilu_mitzrayim_lishtot', 'va_yivash_ha_yeor', 'va_yechezaq_lev_paro_2', 've_lo_shat_libo_gam_la_zot', 'va_yachpru_khol_mitzrayim', 'va_yimale_shivat_yamim', 've_im_maen_ata_le_shaleach', 've_sharatz_ha_yeor_tzfardeim', 'u_vekha_u_ve_amkha'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
