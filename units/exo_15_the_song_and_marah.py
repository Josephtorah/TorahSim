#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_15_the_song_and_marah — 15:1-27
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_15_the_song_and_marah.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The Song and Marah (15:1-27)"""
from machine import Machine

m = Machine("exo_15_the_song_and_marah")

# -------------------------- Exod.15.1 · THEN_SANG_MOSES --------------------
# אָז יָשִׁיר־מֹשֶׁה וּבְנֵי יִשְׂרָאֵל אֶת־הַשִּׁירָה הַזֹּאת לַיהוָה
# וַיֹּאמְרוּ לֵאמֹר אָשִׁירָה לַיהוָה כִּי־גָאֹה גָּאָה סוּס וְרֹכְבוֹ
# רָמָה בַיָּם
# "[EN-AID] Then sang Moses and the sons of Israel this song to the LORD,
# and they spoke, saying: I will sing to the LORD, for He is highly exalted;
# the horse and its rider He has thrown into the sea."
m.step("Exod.15.1")
# ‹אָז יָשִׁיר־מֹשֶׁה וּבְנֵי יִשְׂרָאֵל אֶת־הַשִּׁירָה הַזֹּאת לַיהוָה
# וַיֹּאמְרוּ לֵאמֹר› (“at-that-time sing Moses and-son Israel obj-marker
# the-song the-this to-YHWH and-say to-say”) — event: shirat-the-seas —
# agent Moses; theme bene-yisrael
m.event("shirat_ha_yam", agent="moshe", themes=["bene-yisrael"])
# ‹אָשִׁירָה לַיהוָה כִּי־גָאֹה גָּאָה סוּס וְרֹכְבוֹ רָמָה בַיָּם› (“sing
# to-YHWH that mount-up mount-up horse and-ride-him/its hurl in-seas”) —
# fact holds: that-mount-up-mount-up-horse-and-rokhvo
m.fact("ki_gao_gaa_sus_ve_rokhvo")

# -------------------------- Exod.15.2 · MY_STRENGTH_AND_SONG ---------------
# עָזִּי וְזִמְרָת יָהּ וַיְהִי־לִי לִישׁוּעָה זֶה אֵלִי וְאַנְוֵהוּ אֱלֹהֵי
# אָבִי וַאֲרֹמְמֶנְהוּ
# "[EN-AID] My strength and song is the LORD, and He has become my
# salvation; this is my God, and I will glorify Him — my father's God, and I
# will exalt Him."
m.step("Exod.15.2")
# ‹עָזִּי וְזִמְרָת יָהּ וַיְהִי־לִי לִישׁוּעָה› (“strength-in-various-
# applicat-me/my and-instrumental-music Jah and-be to-me/my to-something-
# saved”) — fact holds: uzi-and-instrumental-music-yah
m.fact("uzi_ve_zimrat_yah")
# ‹זֶה אֵלִי וְאַנְוֵהוּ אֱלֹהֵי אָבִי וַאֲרֹמְמֶנְהוּ› (“this strength-
# me/my and-rest-him/its God father-me/my and-rise-high-him/its”) — fact
# holds: this-eli-and-anvehu
m.fact("ze_eli_ve_anvehu")

# -------------------------- Exod.15.3 · A_MAN_OF_WAR -----------------------
# יְהוָה אִישׁ מִלְחָמָה יְהוָה שְׁמוֹ
# "[EN-AID] The LORD is a man of war; the LORD is His name."
m.step("Exod.15.3")
# ‹יְהוָה אִישׁ מִלְחָמָה יְהוָה שְׁמוֹ› (“YHWH man battle YHWH name-
# him/its”) — fact holds: the-LORD-man-battle
m.fact("YHWH_ish_milchama")

# -------------------------- Exod.15.4 · CAST_INTO_THE_SEA ------------------
# מַרְכְּבֹת פַּרְעֹה וְחֵילוֹ יָרָה בַיָּם וּמִבְחַר שָׁלִשָׁיו טֻבְּעוּ
# בְיַם־סוּף
# "[EN-AID] Pharaoh's chariots and his host He has cast into the sea; and
# the choice of his officers are sunk in the Reed Sea."
m.step("Exod.15.4")
# ‹וּמִבְחַר שָׁלִשָׁיו טֻבְּעוּ בְיַם־סוּף› (“and-select triple-him/its
# sink in-seas reed”) — fact holds: and-select-shalishav-sink
m.fact("u_mivchar_shalishav_tubu")

# -------------------------- Exod.15.5 · THE_DEEPS_COVER_THEM ---------------
# תְּהֹמֹת יְכַסְיֻמוּ יָרְדוּ בִמְצוֹלֹת כְּמוֹ־אָבֶן
# "[EN-AID] The deeps cover them — they went down into the depths like a
# stone."
m.step("Exod.15.5")
# ‹תְּהֹמֹת יְכַסְיֻמוּ› (“deep plump-them/their”) — fact holds: deep-
# yekhasyumu
m.fact("tehomot_yekhasyumu")

# -------------------------- Exod.15.6 · YOUR_RIGHT_HAND_DOUBLED ------------
# יְמִינְךָ יְהוָה נֶאְדָּרִי בַּכֹּחַ יְמִינְךָ יְהוָה תִּרְעַץ אוֹיֵב
# "[EN-AID] Your right hand, O LORD, majestic in power — Your right hand, O
# LORD, shatters the enemy."
m.step("Exod.15.6")
# ‹יְמִינְךָ יְהוָה נֶאְדָּרִי בַּכֹּחַ› (“right-hand-you/your YHWH expand
# in-vigor”) — fact holds: yeminkha-the-LORD-expand-come/bring-koach
m.fact("yeminkha_YHWH_nedari_va_koach")

# -------------------------- Exod.15.7 · LIKE_STUBBLE -----------------------
# וּבְרֹב גְּאוֹנְךָ תַּהֲרֹס קָמֶיךָ תְּשַׁלַּח חֲרֹנְךָ יֹאכְלֵמוֹ
# כַּקַּשׁ
# "[EN-AID] And in the greatness of Your exaltation You overthrow those who
# rise against You; You send forth Your burning — it consumes them like
# stubble."
m.step("Exod.15.7")
# ‹תְּשַׁלַּח חֲרֹנְךָ יֹאכְלֵמוֹ כַּקַּשׁ› (“send burning-of-anger-you/your
# eat-them/their like-straw”) — fact holds: send-charonkha
m.fact("teshalach_charonkha")

# -------------------------- Exod.15.8 · THE_WIND_OF_YOUR_NOSTRILS ----------
# וּבְרוּחַ אַפֶּיךָ נֶעֶרְמוּ מַיִם נִצְּבוּ כְמוֹ־נֵד נֹזְלִים קָפְאוּ
# תְהֹמֹת בְּלֶב־יָם
# "[EN-AID] And by the wind of Your nostrils the waters were heaped up — the
# streams stood like a mound; the deeps congealed in the heart of the sea."
m.step("Exod.15.8")
# ‹וּבְרוּחַ אַפֶּיךָ נֶעֶרְמוּ מַיִם נִצְּבוּ כְמוֹ־נֵד נֹזְלִים› (“and-in-
# spirit nose-you/your pile-up waters stand form-of-the-prefix-'k-' mound
# drip”) — fact holds: and-and-spirit-wind-your-nostrils-pile-up-waters
m.fact("u_ve_ruach_apekha_neermu_mayim")

# -------------------------- Exod.15.9 · THE_ENEMY_SAID ---------------------
# אָמַר אוֹיֵב אֶרְדֹּף אַשִּׂיג אֲחַלֵּק שָׁלָל תִּמְלָאֵמוֹ נַפְשִׁי
# אָרִיק חַרְבִּי תּוֹרִישֵׁמוֹ יָדִי
# "[EN-AID] The enemy said: I will pursue, I will overtake, I will divide
# spoil; my desire shall be filled of them — I will draw my sword, my hand
# shall dispossess them."
m.step("Exod.15.9")
# ‹אָמַר אוֹיֵב אֶרְדֹּף אַשִּׂיג אֲחַלֵּק שָׁלָל› (“say hating run-after-
# gone-by) reach be-smooth booty”) — fact holds: say-hating-run-after-gone-
# by)-reach
m.fact("amar_oyev_erdof_asig")

# -------------------------- Exod.15.10 · SANK_LIKE_LEAD --------------------
# נָשַׁפְתָּ בְרוּחֲךָ כִּסָּמוֹ יָם צָלֲלוּ כַּעוֹפֶרֶת בְּמַיִם אַדִּירִים
# "[EN-AID] You blew with Your wind — the sea covered them; they sank like
# lead in the mighty waters."
m.step("Exod.15.10")
# ‹צָלֲלוּ כַּעוֹפֶרֶת בְּמַיִם אַדִּירִים› (“tumble-down like-lead in-
# waters wide”) — fact holds: tumble-down-like-oferet
m.fact("tzalalu_ka_oferet")

# -------------------------- Exod.15.11 · WHO_IS_LIKE_YOU -------------------
# מִי־כָמֹכָה בָּאֵלִם יְהוָה מִי כָּמֹכָה נֶאְדָּר בַּקֹּדֶשׁ נוֹרָא
# תְהִלֹּת עֹשֵׂה פֶלֶא
# "[EN-AID] Who is like You among the mighty, O LORD? Who is like You,
# majestic in holiness — feared in praises, doing wonder?"
m.step("Exod.15.11")
# ‹מִי־כָמֹכָה בָּאֵלִם יְהוָה מִי כָּמֹכָה נֶאְדָּר בַּקֹּדֶשׁ› (“who?
# form-of-the-prefix-'k-'-you/your in-strength YHWH who? form-of-the-
# prefix-'k-'-you/your expand in-holiness”) — fact holds: who?-khamokha-in-
# the-elim
m.fact("mi_khamokha_ba_elim")
# ‹נוֹרָא תְהִלֹּת עֹשֵׂה פֶלֶא› (“fear laudation make miracle”) — fact
# holds: fear-laudation-make-miracle
m.fact("nora_tehilot_ose_fele")

# -------------------------- Exod.15.12 · THE_EARTH_SWALLOWED ---------------
# נָטִיתָ יְמִינְךָ תִּבְלָעֵמוֹ אָרֶץ
# "[EN-AID] You stretched out Your right hand — the earth swallowed them."
m.step("Exod.15.12")
# ‹נָטִיתָ יְמִינְךָ תִּבְלָעֵמוֹ אָרֶץ› (“stretch right-hand-you/your
# swallow-them/their earth”) — fact holds: tivlaemo-earth
m.fact("tivlaemo_aretz")

# -------------------------- Exod.15.13 · YOU_GUIDED_IN_KINDNESS ------------
# נָחִיתָ בְחַסְדְּךָ עַם־זוּ גָּאָלְתָּ נֵהַלְתָּ בְעָזְּךָ אֶל־נְוֵה
# קָדְשֶׁךָ
# "[EN-AID] You guided in Your kindness the people You redeemed; You led
# them in Your strength to Your holy habitation."
m.step("Exod.15.13")
# ‹נָחִיתָ בְחַסְדְּךָ עַם־זוּ גָּאָלְתָּ› (“guide in-kindness-you/your
# people this be-the-next-of-kin”) — fact holds: people-this-be-the-next-of-
# kin
m.fact("am_zu_gaalta")

# -------------------------- Exod.15.14 · THE_PEOPLES_HEARD -----------------
# שָׁמְעוּ עַמִּים יִרְגָּזוּן חִיל אָחַז יֹשְׁבֵי פְּלָשֶׁת
# "[EN-AID] The peoples heard — they tremble; pang seized the dwellers of
# Philistia."
m.step("Exod.15.14")
# ‹שָׁמְעוּ עַמִּים יִרְגָּזוּן› (“hear people quiver-ward”) — fact holds:
# hear-people-yirgazun
m.fact("shamu_amim_yirgazun")

# -------------------------- Exod.15.15 · THE_CHIEFS_DISMAYED ---------------
# אָז נִבְהֲלוּ אַלּוּפֵי אֱדוֹם אֵילֵי מוֹאָב יֹאחֲזֵמוֹ רָעַד נָמֹגוּ כֹּל
# יֹשְׁבֵי כְנָעַן
# "[EN-AID] Then were the chiefs of Edom dismayed; the rams of Moab —
# trembling seizes them; all the dwellers of Canaan are melted away."
m.step("Exod.15.15")
# ‹נָמֹגוּ כֹּל יֹשְׁבֵי כְנָעַן› (“melt all dwell/sit Canaan”) — fact
# holds: melt-all-dwell/sit-Canaan
m.fact("namogu_kol_yoshve_khenaan")

# -------------------------- Exod.15.16 · STILL_AS_A_STONE ------------------
# תִּפֹּל עֲלֵיהֶם אֵימָתָה וָפַחַד בִּגְדֹל זְרוֹעֲךָ יִדְּמוּ כָּאָבֶן
# עַד־יַעֲבֹר עַמְּךָ יְהוָה עַד־יַעֲבֹר עַם־זוּ קָנִיתָ
# "[EN-AID] Terror and dread fall upon them; by the greatness of Your arm
# they are still as a stone — till Your people cross over, O LORD, till the
# people You acquired cross over."
m.step("Exod.15.16")
# ‹עַד־יַעֲבֹר עַמְּךָ יְהוָה עַד־יַעֲבֹר עַם־זוּ קָנִיתָ› (“until pass-over
# people-you/your YHWH until pass-over people this possessor”) — fact holds:
# until-pass-over-people-this-possessor
m.fact("ad_yaavor_am_zu_qanita")

# -------------------------- Exod.15.17 · PLANT_THEM_ON_YOUR_MOUNTAIN -------
# תְּבִאֵמוֹ וְתִטָּעֵמוֹ בְּהַר נַחֲלָתְךָ מָכוֹן לְשִׁבְתְּךָ פָּעַלְתָּ
# יְהוָה מִקְּדָשׁ אֲדֹנָי כּוֹנְנוּ יָדֶיךָ
# "[EN-AID] You will bring them in and plant them on the mountain of Your
# inheritance — the place for Your dwelling which You made, O LORD; the
# sanctuary, O Lord, which Your hands established."
m.step("Exod.15.17")
# ‹מָכוֹן לְשִׁבְתְּךָ פָּעַלְתָּ יְהוָה› (“fixture to-dwell/sit-you/your do
# YHWH”) — fact holds: fixture-to-shivtekha-do
m.fact("makhon_le_shivtekha_paalta")

# -------------------------- Exod.15.18 · THE_REIGN_FOREVER -----------------
# יְהוָה יִמְלֹךְ לְעֹלָם וָעֶד
# "[EN-AID] The LORD shall reign forever and ever."
m.step("Exod.15.18")
# ‹יְהוָה יִמְלֹךְ לְעֹלָם וָעֶד› (“YHWH reign to-forever and-terminus”) —
# fact holds: the-LORD-reign-to-forever-come/bring-terminus
m.fact("YHWH_yimlokh_le_olam_va_ed")

# -------------------------- Exod.15.19 · THE_PROSE_SEAL --------------------
# כִּי בָא סוּס פַּרְעֹה בְּרִכְבּוֹ וּבְפָרָשָׁיו בַּיָּם וַיָּשֶׁב יְהוָה
# עֲלֵהֶם אֶת־מֵי הַיָּם וּבְנֵי יִשְׂרָאֵל הָלְכוּ בַיַּבָּשָׁה בְּתוֹךְ
# הַיָּם
# "[EN-AID] For the horse of Pharaoh came, with his chariots and with his
# horsemen, into the sea, and the LORD returned upon them the waters of the
# sea; and the sons of Israel walked on the dry ground in the midst of the
# sea."
m.step("Exod.15.19")
# ‹כִּי בָא סוּס פַּרְעֹה בְּרִכְבּוֹ וּבְפָרָשָׁיו בַּיָּם› (“that
# come/bring horse Pharaoh in-vehicle-him/its and-in-steed-him/its in-seas”)
# — fact holds: that-come/bring-horse-Pharaoh-in-the-seas
m.fact("ki_va_sus_paro_ba_yam")

# -------------------------- Exod.15.20 · MIRIAM_TAKES_THE_TIMBREL ----------
# וַתִּקַּח מִרְיָם הַנְּבִיאָה אֲחוֹת אַהֲרֹן אֶת־הַתֹּף בְּיָדָהּ
# וַתֵּצֶאןָ כָל־הַנָּשִׁים אַחֲרֶיהָ בְּתֻפִּים וּבִמְחֹלֹת
# "[EN-AID] And Miriam the prophetess, the sister of Aaron, took the timbrel
# in her hand; and all the women went out after her, with timbrels and with
# dances."
m.step("Exod.15.20")
# ‹וַתִּקַּח מִרְיָם הַנְּבִיאָה אֲחוֹת אַהֲרֹן אֶת־הַתֹּף בְּיָדָהּ› (“and-
# take Miriam the-prophetess sister Aaron obj-marker the-tambourine in-hand-
# her/its”) — fact holds: come/bring-take-Miriam-obj-marker-the-tambourine
m.fact("va_tiqach_miryam_et_ha_tof")

# -------------------------- Exod.15.21 · SING_TO_THE_LORD ------------------
# וַתַּעַן לָהֶם מִרְיָם שִׁירוּ לַיהוָה כִּי־גָאֹה גָּאָה סוּס וְרֹכְבוֹ
# רָמָה בַיָּם
# "[EN-AID] And Miriam answered them: Sing to the LORD, for He is highly
# exalted; the horse and its rider He has thrown into the sea."
m.step("Exod.15.21")
# ‹שִׁירוּ לַיהוָה כִּי־גָאֹה גָּאָה סוּס וְרֹכְבוֹ רָמָה בַיָּם› (“sing to-
# YHWH that mount-up mount-up horse and-ride-him/its hurl in-seas”) — Miriam
# speaks a demand — LET: sing-to-the-LORD
m.declare("miryam", "LET",
          "shiru_la_YHWH")

# -------------------------- Exod.15.22 · THREE_DAYS_NO_WATER ---------------
# וַיַּסַּע מֹשֶׁה אֶת־יִשְׂרָאֵל מִיַּם־סוּף וַיֵּצְאוּ אֶל־מִדְבַּר־שׁוּר
# וַיֵּלְכוּ שְׁלֹשֶׁת־יָמִים בַּמִּדְבָּר וְלֹא־מָצְאוּ מָיִם
# "[EN-AID] And Moses made Israel journey from the Reed Sea, and they went
# out to the wilderness of Shur; and they went three days in the wilderness,
# and found no water."
m.step("Exod.15.22")
# ‹וַיֵּלְכוּ שְׁלֹשֶׁת־יָמִים בַּמִּדְבָּר וְלֹא־מָצְאוּ מָיִם› (“and-go
# three day in-pasture and-not find waters”) — fact holds: three-day-and-
# not-find-waters
m.fact("sheloshet_yamim_ve_lo_matzu_mayim")

# -------------------------- Exod.15.23 · MARAH_NAMED -----------------------
# וַיָּבֹאוּ מָרָתָה וְלֹא יָכְלוּ לִשְׁתֹּת מַיִם מִמָּרָה כִּי מָרִים הֵם
# עַל־כֵּן קָרָא־שְׁמָהּ מָרָה
# "[EN-AID] And they came to Marah, and could not drink the waters of Marah,
# for they were bitter; therefore its name was called Marah."
m.step("Exod.15.23")
# ‹עַל־כֵּן קָרָא־שְׁמָהּ מָרָה› (“over so call name-her/its Marah”) —
# named: maqom := Mara
m.name("maqom", "Mara")

# -------------------------- Exod.15.24 · WHAT_SHALL_WE_DRINK ---------------
# וַיִּלֹּנוּ הָעָם עַל־מֹשֶׁה לֵּאמֹר מַה־נִּשְׁתֶּה
# "[EN-AID] And the people murmured against Moses, saying: What shall we
# drink?"
m.step("Exod.15.24")
# ‹וַיִּלֹּנוּ הָעָם עַל־מֹשֶׁה לֵּאמֹר מַה־נִּשְׁתֶּה› (“and-stop the-
# people over Moses to-say what drink”) — the-people speaks a demand — LET:
# what-drink
m.declare("ha_am", "LET",
          "ma_nishte")

# -------------------------- Exod.15.25 · THE_TREE_AND_THE_STATUTE ----------
# וַיִּצְעַק אֶל־יְהוָה וַיּוֹרֵהוּ יְהוָה עֵץ וַיַּשְׁלֵךְ אֶל־הַמַּיִם
# וַיִּמְתְּקוּ הַמָּיִם שָׁם שָׂם לוֹ חֹק וּמִשְׁפָּט וְשָׁם נִסָּהוּ
# "[EN-AID] And he cried out to the LORD, and the LORD showed him a tree;
# and he cast it into the waters, and the waters were sweetened. There He
# set for him a statute and an ordinance, and there He tested him."
m.step("Exod.15.25")
# ‹וַיִּצְעַק אֶל־יְהוָה וַיּוֹרֵהוּ יְהוָה עֵץ וַיַּשְׁלֵךְ אֶל־הַמַּיִם
# וַיִּמְתְּקוּ› (“and-shriek to YHWH and-flow-as-water-him/its YHWH tree
# and-throw-out to the-waters and-suck”) — event: hamtaqat-the-waters —
# agent Moses; theme ha-mayim
m.event("hamtaqat_ha_mayim", agent="moshe", themes=["ha-mayim"])
# ‹וַיִּמְתְּקוּ הַמָּיִם› (“and-suck the-waters”) — demand settled (popped
# from the queue): what-drink
m.result("ma_nishte", tmark="t1")
# ‹שָׁם שָׂם לוֹ חֹק וּמִשְׁפָּט› (“there put/set to-him/its enactment and-
# judgment”) — fact holds: there-put/set-not-enactment-and-judgment
m.fact("sham_sam_lo_choq_u_mishpat")
# ‹וְשָׁם נִסָּהוּ› (“and-there test-him/its”) — fact holds: and-there-
# nisahu
m.fact("ve_sham_nisahu")

# -------------------------- Exod.15.26 · I_AM_YOUR_HEALER ------------------
# וַיֹּאמֶר אִם־שָׁמוֹעַ תִּשְׁמַע לְקוֹל יְהוָה אֱלֹהֶיךָ וְהַיָּשָׁר
# בְּעֵינָיו תַּעֲשֶׂה וְהַאֲזַנְתָּ לְמִצְוֺתָיו וְשָׁמַרְתָּ כָּל־חֻקָּיו
# כָּל־הַמַּחֲלָה אֲשֶׁר־שַׂמְתִּי בְמִצְרַיִם לֹא־אָשִׂים עָלֶיךָ כִּי
# אֲנִי יְהוָה רֹפְאֶךָ
# "[EN-AID] And He said: If you diligently listen to the voice of the LORD
# your God, and do what is right in His eyes, and give ear to His
# commandments, and keep all His statutes — all the disease which I set upon
# Egypt I will not set upon you; for I am the LORD your healer."
m.step("Exod.15.26")
# ‹וַיֹּאמֶר אִם־שָׁמוֹעַ תִּשְׁמַע לְקוֹל יְהוָה אֱלֹהֶיךָ וְהַיָּשָׁר
# בְּעֵינָיו תַּעֲשֶׂה וְהַאֲזַנְתָּ לְמִצְוֺתָיו וְשָׁמַרְתָּ כָּל־חֻקָּיו›
# (“and-say if hear hear to-voice/sound YHWH God-you/your and-the-straight
# in-eye-him/its make and-broaden-out-the-ear to-commandment-him/its and-
# keep/guard all enactment-him/its”) — the-LORD speaks a demand — LET: if-
# hear-hear
m.declare("YHWH", "LET",
          "im_shamoa_tishma")
# ‹כָּל־הַמַּחֲלָה אֲשֶׁר־שַׂמְתִּי בְמִצְרַיִם לֹא־אָשִׂים עָלֶיךָ כִּי
# אֲנִי יְהוָה רֹפְאֶךָ› (“all the-sickness which put/set in-Egypt not
# put/set over-you/your that YHWH mend-you/your”) — fact holds: ani-the-
# LORD-rofekha
m.fact("ani_YHWH_rofekha")

# -------------------------- Exod.15.27 · TWELVE_SPRINGS_SEVENTY_PALMS ------
# וַיָּבֹאוּ אֵילִמָה וְשָׁם שְׁתֵּים עֶשְׂרֵה עֵינֹת מַיִם וְשִׁבְעִים
# תְּמָרִים וַיַּחֲנוּ־שָׁם עַל־הַמָּיִם
# "[EN-AID] And they came to Elim, and there — twelve springs of water and
# seventy palm trees; and they camped there by the waters."
m.step("Exod.15.27")
# ‹וְשָׁם שְׁתֵּים עֶשְׂרֵה עֵינֹת מַיִם וְשִׁבְעִים תְּמָרִים› (“and-there
# two -teen eye waters and-seventy palm-tree”) — fact holds: shtem--teen-
# eye-and-seventy-palm-tree
m.fact("shtem_esre_enot_ve_shivim_temarim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'maqom': 'Mara'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['shiru_la_YHWH', 'im_shamoa_tishma']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['ki_gao_gaa_sus_ve_rokhvo', 'uzi_ve_zimrat_yah', 'ze_eli_ve_anvehu', 'YHWH_ish_milchama', 'u_mivchar_shalishav_tubu', 'tehomot_yekhasyumu', 'yeminkha_YHWH_nedari_va_koach', 'teshalach_charonkha', 'u_ve_ruach_apekha_neermu_mayim', 'amar_oyev_erdof_asig', 'tzalalu_ka_oferet', 'mi_khamokha_ba_elim', 'nora_tehilot_ose_fele', 'tivlaemo_aretz', 'am_zu_gaalta', 'shamu_amim_yirgazun', 'namogu_kol_yoshve_khenaan', 'ad_yaavor_am_zu_qanita', 'makhon_le_shivtekha_paalta', 'YHWH_yimlokh_le_olam_va_ed', 'ki_va_sus_paro_ba_yam', 'va_tiqach_miryam_et_ha_tof', 'sheloshet_yamim_ve_lo_matzu_mayim', 'sham_sam_lo_choq_u_mishpat', 've_sham_nisahu', 'ani_YHWH_rofekha', 'shtem_esre_enot_ve_shivim_temarim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
