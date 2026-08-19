#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_06_i_am_the_lord — 6:1-30
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_06_i_am_the_lord.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""I am the LORD (6:1-30)"""
from machine import Machine

m = Machine("exo_06_i_am_the_lord")

# -------------------------- Exod.6.1 · NOW_YOU_SHALL_SEE -------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה עַתָּה תִרְאֶה אֲשֶׁר אֶעֱשֶׂה לְפַרְעֹה כִּי
# בְיָד חֲזָקָה יְשַׁלְּחֵם וּבְיָד חֲזָקָה יְגָרְשֵׁם מֵאַרְצוֹ
# "[EN-AID] And the LORD said to Moses: Now you shall see what I will do to
# Pharaoh; for by a strong hand he shall send them, and by a strong hand he
# shall drive them out of his land."
m.step("Exod.6.1")
# ‹עַתָּה תִרְאֶה אֲשֶׁר אֶעֱשֶׂה לְפַרְעֹה› (“now see which make to-
# Pharaoh”) — fact holds: now-see-which-make-to-Pharaoh
m.fact("ata_tire_asher_eese_le_faro")

# -------------------------- Exod.6.2 · I_AM_YHWH ---------------------------
# וַיְדַבֵּר אֱלֹהִים אֶל־מֹשֶׁה וַיֹּאמֶר אֵלָיו אֲנִי יְהוָה
# "[EN-AID] And God spoke to Moses, and said to him: I am the LORD."
m.step("Exod.6.2")
# ‹אֲנִי יְהוָה› (“YHWH”) — fact holds: I-the-LORD
m.fact("ani_YHWH")

# -------------------------- Exod.6.3 · NOT_BY_MY_NAME_KNOWN ----------------
# וָאֵרָא אֶל־אַבְרָהָם אֶל־יִצְחָק וְאֶל־יַעֲקֹב בְּאֵל שַׁדָּי וּשְׁמִי
# יְהוָה לֹא נוֹדַעְתִּי לָהֶם
# "[EN-AID] And I appeared to Abraham, to Isaac, and to Jacob as God
# Almighty; but by My name the LORD I was not known to them."
m.step("Exod.6.3")
# ‹וָאֵרָא אֶל־אַבְרָהָם› (“and-see to Abraham”) — fact holds: and-shemi-
# the-LORD-not-know-to-them
m.fact("u_shemi_YHWH_lo_nodati_lahem")

# -------------------------- Exod.6.4 · THE_COVENANT_STOOD ------------------
# וְגַם הֲקִמֹתִי אֶת־בְּרִיתִי אִתָּם לָתֵת לָהֶם אֶת־אֶרֶץ כְּנָעַן אֵת
# אֶרֶץ מְגֻרֵיהֶם אֲשֶׁר־גָּרוּ בָהּ
# "[EN-AID] And I also established My covenant with them, to give them the
# land of Canaan, the land of their sojournings, wherein they sojourned."
m.step("Exod.6.4")
# ‹אֵת אֶרֶץ מְגֻרֵיהֶם אֲשֶׁר־גָּרוּ בָהּ› (“obj-marker earth sojourning-
# them/their which turn-aside-from-the-road in-her/its”) — fact holds:
# arise-obj-marker-beriti
m.fact("haqimoti_et_beriti")

# -------------------------- Exod.6.5 · THE_GROANING_HEARD ------------------
# וְגַם אֲנִי שָׁמַעְתִּי אֶת־נַאֲקַת בְּנֵי יִשְׂרָאֵל אֲשֶׁר מִצְרַיִם
# מַעֲבִדִים אֹתָם וָאֶזְכֹּר אֶת־בְּרִיתִי
# "[EN-AID] And I also heard the groaning of the sons of Israel, whom Egypt
# holds in bondage; and I remembered My covenant."
m.step("Exod.6.5")
# ‹שָׁמַעְתִּי אֶת־נַאֲקַת בְּנֵי יִשְׂרָאֵל› (“hear obj-marker groan son
# Israel”) — fact holds: hear-and-mark
m.fact("shamati_va_ezkor")

# -------------------------- Exod.6.6 · THEREFORE_SAY -----------------------
# לָכֵן אֱמֹר לִבְנֵי־יִשְׂרָאֵל אֲנִי יְהוָה וְהוֹצֵאתִי אֶתְכֶם מִתַּחַת
# סִבְלֹת מִצְרַיִם וְהִצַּלְתִּי אֶתְכֶם מֵעֲבֹדָתָם וְגָאַלְתִּי אֶתְכֶם
# בִּזְרוֹעַ נְטוּיָה וּבִשְׁפָטִים גְּדֹלִים
# "[EN-AID] Therefore say to the sons of Israel: I am the LORD; and I will
# bring you out from under the burdens of Egypt, and I will deliver you from
# their bondage; and I will redeem you with an outstretched arm, and with
# great judgments."
m.step("Exod.6.6")
# ‹לָכֵן אֱמֹר לִבְנֵי־יִשְׂרָאֵל אֲנִי יְהוָה› (“to-so say to-son Israel
# YHWH”) — the-LORD speaks a demand — LET: say-to-me-son-Israel-I-the-LORD
m.declare("YHWH", "LET",
          "emor_li_vene_yisrael_ani_YHWH")

# -------------------------- Exod.6.7 · I_WILL_TAKE_YOU ---------------------
# וְלָקַחְתִּי אֶתְכֶם לִי לְעָם וְהָיִיתִי לָכֶם לֵאלֹהִים וִידַעְתֶּם כִּי
# אֲנִי יְהוָה אֱלֹהֵיכֶם הַמּוֹצִיא אֶתְכֶם מִתַּחַת סִבְלוֹת מִצְרָיִם
# "[EN-AID] And I will take you to Me for a people, and I will be to you a
# God; and you shall know that I am the LORD your God, who brings you out
# from under the burdens of Egypt."
m.step("Exod.6.7")
# ‹וְלָקַחְתִּי אֶתְכֶם לִי לְעָם› (“and-take obj-marker-you/your(pl) to-
# me/my to-people”) — fact holds: and-take-etkhem-to-me-to-people
m.fact("ve_laqachti_etkhem_li_le_am")

# -------------------------- Exod.6.8 · I_WILL_BRING_YOU_IN -----------------
# וְהֵבֵאתִי אֶתְכֶם אֶל־הָאָרֶץ אֲשֶׁר נָשָׂאתִי אֶת־יָדִי לָתֵת אֹתָהּ
# לְאַבְרָהָם לְיִצְחָק וּלְיַעֲקֹב וְנָתַתִּי אֹתָהּ לָכֶם מוֹרָשָׁה אֲנִי
# יְהוָה
# "[EN-AID] And I will bring you into the land which I lifted My hand to
# give to Abraham, to Isaac, and to Jacob; and I will give it to you as a
# heritage: I am the LORD."
m.step("Exod.6.8")
# ‹וְנָתַתִּי אֹתָהּ לָכֶם מוֹרָשָׁה אֲנִי יְהוָה› (“and-set obj-marker-
# her/its to-you/your(pl) possession YHWH”) — fact holds: and-come/bring-
# etkhem-to-the-earth
m.fact("ve_heveti_etkhem_el_ha_aretz")

# -------------------------- Exod.6.9 · MOSES_SPOKE_SO ----------------------
# וַיְדַבֵּר מֹשֶׁה כֵּן אֶל־בְּנֵי יִשְׂרָאֵל וְלֹא שָׁמְעוּ אֶל־מֹשֶׁה
# מִקֹּצֶר רוּחַ וּמֵעֲבֹדָה קָשָׁה
# "[EN-AID] And Moses spoke so to the sons of Israel; but they did not hear
# Moses, from shortness of breath and from hard bondage."
m.step("Exod.6.9")
# ‹וַיְדַבֵּר מֹשֶׁה כֵּן אֶל־בְּנֵי יִשְׂרָאֵל› (“and-speak Moses so to son
# Israel”) — demand settled (popped from the queue): say-to-me-son-Israel-I-
# the-LORD
m.result("emor_li_vene_yisrael_ani_YHWH", tmark="t1")

# -------------------------- Exod.6.10 · THE_GO_SPEAK_FRAME -----------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Exod.6.10")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר› (“and-speak YHWH to Moses to-say”)
# — fact holds: and-speak-the-LORD-to-Moses-lemor
m.fact("va_yedaber_YHWH_el_moshe_lemor")

# -------------------------- Exod.6.11 · GO_SPEAK_TO_PHARAOH ----------------
# בֹּא דַבֵּר אֶל־פַּרְעֹה מֶלֶךְ מִצְרָיִם וִישַׁלַּח אֶת־בְּנֵי־יִשְׂרָאֵל
# מֵאַרְצוֹ
# "[EN-AID] Go, speak to Pharaoh king of Egypt, that he send the sons of
# Israel out of his land."
m.step("Exod.6.11")
# ‹בֹּא דַבֵּר אֶל־פַּרְעֹה מֶלֶךְ מִצְרָיִם› (“come/bring speak to Pharaoh
# king Egypt”) — the-LORD speaks a demand — LET: come/bring-speak-to-Pharaoh
m.declare("YHWH", "LET",
          "bo_daber_el_paro")

# -------------------------- Exod.6.12 · UNCIRCUMCISED_LIPS -----------------
# וַיְדַבֵּר מֹשֶׁה לִפְנֵי יְהוָה לֵאמֹר הֵן בְּנֵי־יִשְׂרָאֵל לֹא־שָׁמְעוּ
# אֵלַי וְאֵיךְ יִשְׁמָעֵנִי פַרְעֹה וַאֲנִי עֲרַל שְׂפָתָיִם
# "[EN-AID] And Moses spoke before the LORD, saying: Behold, the sons of
# Israel have not heard me; how then shall Pharaoh hear me — and I am of
# uncircumcised lips."
m.step("Exod.6.12")
# ‹וְאֵיךְ יִשְׁמָעֵנִי פַרְעֹה וַאֲנִי עֲרַל שְׂפָתָיִם› (“and-how? hear-
# me/my Pharaoh and-I uncircumcised lip”) — fact holds: lo!-not-hear-elay
m.fact("hen_lo_shamu_elay")

# -------------------------- Exod.6.13 · THE_JOINT_CHARGE -------------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן וַיְצַוֵּם אֶל־בְּנֵי
# יִשְׂרָאֵל וְאֶל־פַּרְעֹה מֶלֶךְ מִצְרָיִם לְהוֹצִיא אֶת־בְּנֵי־יִשְׂרָאֵל
# מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And the LORD spoke to Moses and to Aaron, and gave them a charge
# to the sons of Israel, and to Pharaoh king of Egypt, to bring the sons of
# Israel out of the land of Egypt."
m.step("Exod.6.13")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן› (“and-speak YHWH to Moses
# and-to Aaron”) — the-LORD speaks a demand — LET: bring-forth-obj-marker-
# son-Israel-from-earth-Egypt
m.declare("YHWH", "LET",
          "hotzi_et_bene_yisrael_me_eretz_mitzrayim")

# -------------------------- Exod.6.14 · THE_REGISTRY_OPENS -----------------
# אֵלֶּה רָאשֵׁי בֵית־אֲבֹתָם בְּנֵי רְאוּבֵן בְּכֹר יִשְׂרָאֵל חֲנוֹךְ
# וּפַלּוּא חֶצְרוֹן וְכַרְמִי אֵלֶּה מִשְׁפְּחֹת רְאוּבֵן
# "[EN-AID] These are the heads of their fathers' houses: the sons of
# Reuben, Israel's firstborn — Enoch and Pallu, Hezron and Carmi; these are
# the families of Reuben."
m.step("Exod.6.14")
# ‹אֵלֶּה רָאשֵׁי בֵית־אֲבֹתָם› (“these head house father-them/their”) —
# fact holds: these-head-house-avotam
m.fact("ele_rashe_vet_avotam")

# -------------------------- Exod.6.15 · SIMEONS_SONS -----------------------
# וּבְנֵי שִׁמְעוֹן יְמוּאֵל וְיָמִין וְאֹהַד וְיָכִין וְצֹחַר וְשָׁאוּל
# בֶּן־הַכְּנַעֲנִית אֵלֶּה מִשְׁפְּחֹת שִׁמְעוֹן
# "[EN-AID] And the sons of Simeon: Jemuel, and Jamin, and Ohad, and Jachin,
# and Zohar, and Saul the son of the Canaanite woman; these are the families
# of Simeon."
m.step("Exod.6.15")
# ‹וּבְנֵי שִׁמְעוֹן› (“and-son Simeon”) — fact holds: these-mishpechot-
# Simeon
m.fact("ele_mishpechot_shimon")

# -------------------------- Exod.6.16 · LEVIS_YEARS ------------------------
# וְאֵלֶּה שְׁמוֹת בְּנֵי־לֵוִי לְתֹלְדֹתָם גֵּרְשׁוֹן וּקְהָת וּמְרָרִי
# וּשְׁנֵי חַיֵּי לֵוִי שֶׁבַע וּשְׁלֹשִׁים וּמְאַת שָׁנָה
# "[EN-AID] And these are the names of the sons of Levi by their
# generations: Gershon, and Kohath, and Merari; and the years of Levi's life
# were seven and thirty and a hundred years."
m.step("Exod.6.16")
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי־לֵוִי לְתֹלְדֹתָם› (“and-these name son Levi to-
# generations-them/their”) — fact holds: and-years-alive-Levi
m.fact("u_shene_chaye_levi")

# -------------------------- Exod.6.17 · GERSHONS_SONS ----------------------
# בְּנֵי גֵרְשׁוֹן לִבְנִי וְשִׁמְעִי לְמִשְׁפְּחֹתָם
# "[EN-AID] The sons of Gershon: Libni and Shimei, by their families."
m.step("Exod.6.17")
# ‹בְּנֵי גֵרְשׁוֹן לִבְנִי וְשִׁמְעִי› (“son Gershon Libni and-Shimeah”) —
# fact holds: son-Gershon
m.fact("bene_gershon")

# -------------------------- Exod.6.18 · KOHATHS_SONS -----------------------
# וּבְנֵי קְהָת עַמְרָם וְיִצְהָר וְחֶבְרוֹן וְעֻזִּיאֵל וּשְׁנֵי חַיֵּי
# קְהָת שָׁלֹשׁ וּשְׁלֹשִׁים וּמְאַת שָׁנָה
# "[EN-AID] And the sons of Kohath: Amram, and Izhar, and Hebron, and
# Uzziel; and the years of Kohath's life were three and thirty and a hundred
# years."
m.step("Exod.6.18")
# ‹עַמְרָם› (“Amram”) — fact holds: and-son-Kohath
m.fact("u_vene_qehat")

# -------------------------- Exod.6.19 · MERARIS_SONS -----------------------
# וּבְנֵי מְרָרִי מַחְלִי וּמוּשִׁי אֵלֶּה מִשְׁפְּחֹת הַלֵּוִי לְתֹלְדֹתָם
# "[EN-AID] And the sons of Merari: Machli and Mushi; these are the families
# of the Levite by their generations."
m.step("Exod.6.19")
# ‹מַחְלִי וּמוּשִׁי› (“Mahli and-Mushi”) — fact holds: and-son-Merari
m.fact("u_vene_merari")

# -------------------------- Exod.6.20 · AMRAM_TAKES_YOKHEVED ---------------
# וַיִּקַּח עַמְרָם אֶת־יוֹכֶבֶד דֹּדָתוֹ לוֹ לְאִשָּׁה וַתֵּלֶד לוֹ
# אֶת־אַהֲרֹן וְאֶת־מֹשֶׁה וּשְׁנֵי חַיֵּי עַמְרָם שֶׁבַע וּשְׁלֹשִׁים
# וּמְאַת שָׁנָה
# "[EN-AID] And Amram took Yokheved his father's sister to himself as wife,
# and she bore him Aaron and Moses; and the years of Amram's life were seven
# and thirty and a hundred years."
m.step("Exod.6.20")
# ‹וַיִּקַּח עַמְרָם אֶת־יוֹכֶבֶד דֹּדָתוֹ› (“and-take Amram obj-marker
# Jochebed aunt-him/its”) — fact holds: and-take-Amram-obj-marker-Jochebed
m.fact("va_yiqach_amram_et_yokheved")

# -------------------------- Exod.6.21 · IZHARS_SONS ------------------------
# וּבְנֵי יִצְהָר קֹרַח וָנֶפֶג וְזִכְרִי
# "[EN-AID] And the sons of Izhar: Korach, and Nepheg, and Zichri."
m.step("Exod.6.21")
# ‹קֹרַח› (“Korah”) — fact holds: and-son-Izhar
m.fact("u_vene_yitzhar")

# -------------------------- Exod.6.22 · UZZIELS_SONS -----------------------
# וּבְנֵי עֻזִּיאֵל מִישָׁאֵל וְאֶלְצָפָן וְסִתְרִי
# "[EN-AID] And the sons of Uzziel: Mishael, and Elzaphan, and Sithri."
m.step("Exod.6.22")
# ‹מִישָׁאֵל וְאֶלְצָפָן› (“Mishael and-Elizaphan”) — fact holds: and-son-
# Uzziel
m.fact("u_vene_uziel")

# -------------------------- Exod.6.23 · AARON_TAKES_ELISHEVA ---------------
# וַיִּקַּח אַהֲרֹן אֶת־אֱלִישֶׁבַע בַּת־עַמִּינָדָב אֲחוֹת נַחְשׁוֹן לוֹ
# לְאִשָּׁה וַתֵּלֶד לוֹ אֶת־נָדָב וְאֶת־אֲבִיהוּא אֶת־אֶלְעָזָר
# וְאֶת־אִיתָמָר
# "[EN-AID] And Aaron took Elisheva, daughter of Amminadav, sister of
# Nachshon, to himself as wife; and she bore him Nadav and Avihu, Elazar and
# Itamar."
m.step("Exod.6.23")
# ‹וַיִּקַּח אַהֲרֹן אֶת־אֱלִישֶׁבַע בַּת־עַמִּינָדָב אֲחוֹת נַחְשׁוֹן›
# (“and-take Aaron obj-marker Elisheba daughter Amminadab sister Naashon”) —
# fact holds: and-take-Aaron-obj-marker-Elisheba
m.fact("va_yiqach_aharon_et_elisheva")

# -------------------------- Exod.6.24 · KORACHS_SONS -----------------------
# וּבְנֵי קֹרַח אַסִּיר וְאֶלְקָנָה וַאֲבִיאָסָף אֵלֶּה מִשְׁפְּחֹת
# הַקָּרְחִי
# "[EN-AID] And the sons of Korach: Assir, and Elkanah, and Aviasaph; these
# are the families of the Korahite."
m.step("Exod.6.24")
# ‹אַסִּיר וְאֶלְקָנָה וַאֲבִיאָסָף› (“Assir and-Elkanah and-Abiasaph”) —
# fact holds: and-son-Korah
m.fact("u_vene_qorach")

# -------------------------- Exod.6.25 · ELAZAR_AND_PINCHAS -----------------
# וְאֶלְעָזָר בֶּן־אַהֲרֹן לָקַח־לוֹ מִבְּנוֹת פּוּטִיאֵל לוֹ לְאִשָּׁה
# וַתֵּלֶד לוֹ אֶת־פִּינְחָס אֵלֶּה רָאשֵׁי אֲבוֹת הַלְוִיִּם
# לְמִשְׁפְּחֹתָם
# "[EN-AID] And Elazar, Aaron's son, took for himself of the daughters of
# Putiel as wife; and she bore him Pinchas. These are the heads of the
# fathers of the Levites by their families."
m.step("Exod.6.25")
# ‹וַתֵּלֶד לוֹ אֶת־פִּינְחָס› (“and-bear-young to-him/its obj-marker
# Phinehas”) — fact holds: and-bear-young-not-obj-marker-Phinehas
m.fact("va_teled_lo_et_pinchas")

# -------------------------- Exod.6.26 · THAT_AARON_AND_MOSES ---------------
# הוּא אַהֲרֹן וּמֹשֶׁה אֲשֶׁר אָמַר יְהוָה לָהֶם הוֹצִיאוּ אֶת־בְּנֵי
# יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם עַל־צִבְאֹתָם
# "[EN-AID] This is that Aaron and Moses, to whom the LORD said: Bring out
# the sons of Israel from the land of Egypt by their hosts."
m.step("Exod.6.26")
# ‹הוּא אַהֲרֹן וּמֹשֶׁה› (“he/it Aaron and-Moses”) — fact holds: he/it-
# Aaron-and-Moses
m.fact("hu_aharon_u_moshe")

# -------------------------- Exod.6.27 · THE_SPEAKERS_FLIPPED ---------------
# הֵם הַמְדַבְּרִים אֶל־פַּרְעֹה מֶלֶךְ־מִצְרַיִם לְהוֹצִיא
# אֶת־בְּנֵי־יִשְׂרָאֵל מִמִּצְרָיִם הוּא מֹשֶׁה וְאַהֲרֹן
# "[EN-AID] They are the ones who speak to Pharaoh king of Egypt, to bring
# out the sons of Israel from Egypt: this is that Moses and Aaron."
m.step("Exod.6.27")
# ‹הוּא מֹשֶׁה וְאַהֲרֹן› (“he/it Moses and-Aaron”) — fact holds: he/it-
# Moses-and-Aaron
m.fact("hu_moshe_ve_aharon")

# -------------------------- Exod.6.28 · THE_RESUMPTION_DAY -----------------
# וַיְהִי בְּיוֹם דִּבֶּר יְהוָה אֶל־מֹשֶׁה בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And it came to pass, on the day the LORD spoke to Moses in the
# land of Egypt:"
m.step("Exod.6.28")
# ‹וַיְהִי בְּיוֹם דִּבֶּר יְהוָה אֶל־› (“and-be in-day speak YHWH to”) —
# fact holds: and-be-in-day-speak
m.fact("va_yehi_be_yom_diber")

# -------------------------- Exod.6.29 · SPEAK_ALL_THAT_I_SPEAK -------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר אֲנִי יְהוָה דַּבֵּר אֶל־פַּרְעֹה
# מֶלֶךְ מִצְרַיִם אֵת כָּל־אֲשֶׁר אֲנִי דֹּבֵר אֵלֶיךָ
# "[EN-AID] And the LORD spoke to Moses, saying: I am the LORD; speak to
# Pharaoh king of Egypt all that I speak to you."
m.step("Exod.6.29")
# ‹דַּבֵּר אֶל־פַּרְעֹה מֶלֶךְ מִצְרַיִם› (“speak to Pharaoh king Egypt”) —
# fact holds: speak-to-Pharaoh-obj-marker-all-which-I-speak
m.fact("daber_el_paro_et_kol_asher_ani_dover")

# -------------------------- Exod.6.30 · THE_SECOND_PLEA --------------------
# וַיֹּאמֶר מֹשֶׁה לִפְנֵי יְהוָה הֵן אֲנִי עֲרַל שְׂפָתַיִם וְאֵיךְ
# יִשְׁמַע אֵלַי פַּרְעֹה
# "[EN-AID] And Moses said before the LORD: Behold, I am of uncircumcised
# lips; how shall Pharaoh hear me?"
m.step("Exod.6.30")
# ‹הֵן אֲנִי עֲרַל שְׂפָתַיִם› (“lo! uncircumcised lip”) — fact holds:
# lo!-I-uncircumcised-lip
m.fact("hen_ani_aral_sefatayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['bo_daber_el_paro', 'hotzi_et_bene_yisrael_me_eretz_mitzrayim']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ata_tire_asher_eese_le_faro', 'ani_YHWH', 'u_shemi_YHWH_lo_nodati_lahem', 'haqimoti_et_beriti', 'shamati_va_ezkor', 've_laqachti_etkhem_li_le_am', 've_heveti_etkhem_el_ha_aretz', 'va_yedaber_YHWH_el_moshe_lemor', 'hen_lo_shamu_elay', 'ele_rashe_vet_avotam', 'ele_mishpechot_shimon', 'u_shene_chaye_levi', 'bene_gershon', 'u_vene_qehat', 'u_vene_merari', 'va_yiqach_amram_et_yokheved', 'u_vene_yitzhar', 'u_vene_uziel', 'va_yiqach_aharon_et_elisheva', 'u_vene_qorach', 'va_teled_lo_et_pinchas', 'hu_aharon_u_moshe', 'hu_moshe_ve_aharon', 'va_yehi_be_yom_diber', 'daber_el_paro_et_kol_asher_ani_dover', 'hen_ani_aral_sefatayim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
