#!/usr/bin/env python3
# =============================================================================
# exo_13_consecration_and_pillars — 13:1-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_13_consecration_and_pillars.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Consecration and pillars (13:1-22)"""
from machine import Machine

m = Machine("exo_13_consecration_and_pillars")

# -------------------------- Exod.13.1 · THE_FRAME --------------------------
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Exod.13.1")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# — fact holds: and-speak-to-Moses
m.fact("va_yedaber_el_moshe")

# -------------------------- Exod.13.2 · CONSECRATE_THE_FIRSTBORN -----------
# ‹קַדֶּשׁ־לִי כָל־בְּכוֹר פֶּטֶר› (“sanctify to-me/my all firstborn
# fissure”)
# ‹כָּל־רֶחֶם בִּבְנֵי יִשְׂרָאֵל› (“all womb in-son Israel”)
# ‹בָּאָדָם וּבַבְּהֵמָה לִי› (“in-human and-in-livestock to-me/my”)
# ‹הוּא› (“he/it”)
# "[EN-AID] Consecrate to Me every firstborn, opener of every womb among the
# sons of Israel, in man and in beast — Mine is it."
m.step("Exod.13.2")
# ‹קַדֶּשׁ־לִי כָל־בְּכוֹר› (“sanctify to-me/my all firstborn”)
# — the-LORD speaks a demand — LET: sanctify-to-me-all-firstborn
m.declare("YHWH", "LET",
          "qadesh_li_khol_bekhor")

# -------------------------- Exod.13.3 · REMEMBER_THIS_DAY ------------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־הָעָם› (“and-say Moses to the-people”)
# ‹זָכוֹר אֶת־הַיּוֹם הַזֶּה› (“mark obj-marker the-day the-this”)
# ‹אֲשֶׁר יְצָאתֶם מִמִּצְרַיִם› (“which bring-forth from-Egypt”)
# ‹מִבֵּית עֲבָדִים כִּי› (“from-house servant that”)
# ‹בְּחֹזֶק יָד הוֹצִיא› (“in-power hand bring-forth”)
# ‹יְהֹוָה אֶתְכֶם מִזֶּה› (“YHWH obj-marker-you/your(pl) from-this”)
# ‹וְלֹא יֵאָכֵל חָמֵץ› (“and-not eat ferment”)
# "[EN-AID] And Moses said to the people: Remember this day on which you
# went out from Egypt, from the house of slaves — for by strength of hand
# the LORD brought you out from this place; and no leavened bread shall be
# eaten."
m.step("Exod.13.3")
# ‹זָכוֹר אֶת־הַיּוֹם הַזֶּה› (“mark obj-marker the-day the-this”)
# — Moses speaks a demand — LET: mark-obj-marker-the-day-the-this
m.declare("moshe", "LET",
          "zakhor_et_ha_yom_ha_ze")
# witness-tier presupposed read: recorded_routes on benefit_ban — read, not
# installed
m.witness_read("benefit_ban", "recorded_routes",
                cites=["Pesachim 21b:5", "Pesachim 21b:11", "Pesachim 23a:12", "Pesachim 24a:4", "Pesachim 28b:4", "Pesachim 29a:4"])

# -------------------------- Exod.13.4 · IN_THE_MONTH_OF_AVIV ---------------
# ‹הַיּוֹם אַתֶּם יֹצְאִים› (“the-day you bring-forth”)
# ‹בְּחֹדֶשׁ הָאָבִיב› (“in-new-moon the-green”)
# "[EN-AID] Today you are going out, in the month of the Aviv."
m.step("Exod.13.4")
# ‹הַיּוֹם אַתֶּם יֹצְאִים› (“the-day you bring-forth”)
# ‹בְּחֹדֶשׁ הָאָבִיב› (“in-new-moon the-green”)
# — fact holds: in-new-moon-the-green
m.fact("be_chodesh_ha_aviv")

# -------------------------- Exod.13.5 · THE_SERVICE_IN_THE_LAND ------------
# ‹וְהָיָה כִי־יְבִיאֲךָ יְהוָה› (“and-be that come/bring-you/your YHWH”)
# ‹אֶל־אֶרֶץ הַכְּנַעֲנִי וְהַחִתִּי› (“to earth the-Kenaanite and-the-
# Chittite”)
# ‹וְהָאֱמֹרִי וְהַחִוִּי וְהַיְבוּסִי› (“and-the-Emorite and-the-Chivvite
# and-the-Jebusite”)
# ‹אֲשֶׁר נִשְׁבַּע לַאֲבֹתֶיךָ› (“which swear to-father-you/your”)
# ‹לָתֶת לָךְ אֶרֶץ› (“to-set to-you/your earth”)
# ‹זָבַת חָלָב וּדְבָשׁ› (“flow-freely milk and-honey”)
# ‹וְעָבַדְתָּ אֶת־הָעֲבֹדָה הַזֹּאת› (“and-work/serve obj-marker the-
# service/work the-this”)
# ‹בַּחֹדֶשׁ הַזֶּה› (“in-new-moon the-this”)
# "[EN-AID] And it shall be, when the LORD brings you to the land of the
# Canaanite and the Hittite and the Amorite and the Hivvite and the
# Jebusite, which He swore to your fathers to give you, a land flowing with
# milk and honey — you shall serve this service in this month."
m.step("Exod.13.5")
# ‹אֶת־הָעֲבֹדָה הַזֹּאת בַּחֹדֶשׁ› (“obj-marker the-service/work the-this
# in-new-moon”)
# ‹הַזֶּה› (“the-this”)
# — fact holds: and-work/serve-obj-marker-the-service/work
m.fact("ve_avadta_et_ha_avoda")
# witness-tier presupposed read: all_services_as_this on export_operator —
# read, not installed
m.witness_read("export_operator", "all_services_as_this",
                cites=["Pesachim 96a:11", "Pesachim 96a:12", "Pesachim 96a:13", "Pesachim 96a:14", "Pesachim 96a:15", "Pesachim 96a:16", "Pesachim 96a:17", "Pesachim 96a:18", "Pesachim 96a:19", "Pesachim 96a:20", "Pesachim 96a:21", "Pesachim 96a:22", "Pesachim 96a:23", "Pesachim 96a:24", "Pesachim 96b:1", "Pesachim 96b:2"])

# -------------------------- Exod.13.6 · SEVEN_DAYS_AND_A_FEAST -------------
# ‹שִׁבְעַת יָמִים תֹּאכַל› (“seven day eat”)
# ‹מַצֹּת וּבַיּוֹם הַשְּׁבִיעִי› (“sweetness and-in-day the-seventh”)
# ‹חַג לַיהוָה› (“festival to-YHWH”)
# "[EN-AID] Seven days you shall eat unleavened bread, and on the seventh
# day is a feast to the LORD."
m.step("Exod.13.6")
# ‹שִׁבְעַת יָמִים תֹּאכַל› (“seven day eat”)
# ‹מַצֹּת› (“sweetness”)
# — fact holds: seven-day-eat-sweetness
m.fact("shivat_yamim_tokhal_matzot")

# -------------------------- Exod.13.7 · NO_LEAVEN_SEEN ---------------------
# ‹מַצּוֹת יֵאָכֵל אֵת› (“sweetness eat obj-marker”)
# ‹שִׁבְעַת הַיָּמִים וְלֹא־יֵרָאֶה› (“seven the-day and-not see”)
# ‹לְךָ חָמֵץ וְלֹא־יֵרָאֶה› (“to-you/your ferment and-not see”)
# ‹לְךָ שְׂאֹר בְּכָל־גְּבֻלֶךָ› (“to-you/your barm in-all cord-you/your”)
# "[EN-AID] Unleavened bread shall be eaten the seven days; and nothing
# leavened shall be seen for you, and no leaven shall be seen for you in all
# your border."
m.step("Exod.13.7")
# ‹וְלֹא־יֵרָאֶה לְךָ חָמֵץ› (“and-not see to-you/your ferment”)
# ‹וְלֹא־יֵרָאֶה› (“and-not see”)
# — fact holds: not-see-to-you-ferment
m.fact("lo_yerae_lekha_chametz")

# -------------------------- Exod.13.8 · AND_YOU_SHALL_TELL_YOUR_SON --------
# ‹וְהִגַּדְתָּ לְבִנְךָ בַּיּוֹם› (“and-tell to-son-you/your in-day”)
# ‹הַהוּא לֵאמֹר בַּעֲבוּר› (“that to-say for-the-sake-of”)
# ‹זֶה עָשָׂה יְהוָה› (“this make YHWH”)
# ‹לִי בְּצֵאתִי מִמִּצְרָיִם› (“to-me/my in-bring-forth-me/my from-Egypt”)
# "[EN-AID] And you shall tell your son in that day, saying: For the sake of
# this the LORD acted for me in my going out from Egypt."
m.step("Exod.13.8")
# ‹וְהִגַּדְתָּ לְבִנְךָ בַּיּוֹם› (“and-tell to-son-you/your in-day”)
# ‹הַהוּא לֵאמֹר› (“that to-say”)
# — fact holds: and-tell-to-vinkha
m.fact("ve_higadta_le_vinkha")
# witness-tier presupposed read: pointing_and_self_view on the_telling —
# read, not installed
m.witness_read("the_telling", "pointing_and_self_view",
                cites=["Pesachim 116b:3", "Pesachim 116b:7", "Pesachim 116b:8", "Pesachim 116b:9"])

# -------------------------- Exod.13.9 · A_SIGN_ON_YOUR_HAND ----------------
# ‹וְהָיָה לְךָ לְאוֹת› (“and-be to-you/your to-signs”)
# ‹עַל־יָדְךָ וּלְזִכָּרוֹן בֵּין› (“over hand-you/your and-to-memento
# between”)
# ‹עֵינֶיךָ לְמַעַן תִּהְיֶה› (“eye-you/your so-that be”)
# ‹תּוֹרַת יְהוָה בְּפִיךָ› (“precept YHWH in-mouth-you/your”)
# ‹כִּי בְּיָד חֲזָקָה› (“that in-hand strong”)
# ‹הוֹצִאֲךָ יְהֹוָה מִמִּצְרָיִם› (“bring-forth-you/your YHWH from-Egypt”)
# "[EN-AID] And it shall be for you for a sign on your hand and for a
# memorial between your eyes, in order that the Torah of the LORD be in your
# mouth — for with a strong hand the LORD brought you out from Egypt."
m.step("Exod.13.9")
# ‹וְהָיָה לְךָ לְאוֹת› (“and-be to-you/your to-signs”)
# ‹עַל־יָדְךָ וּלְזִכָּרוֹן בֵּין› (“over hand-you/your and-to-memento
# between”)
# ‹עֵינֶיךָ› (“eye-you/your”)
# — fact holds: to-signs-over-yadkha-and-to-memento
m.fact("le_ot_al_yadkha_u_le_zikaron")

# -------------------------- Exod.13.10 · AT_ITS_SEASON ---------------------
# ‹וְשָׁמַרְתָּ אֶת־הַחֻקָּה הַזֹּאת› (“and-keep/guard obj-marker the-
# statute the-this”)
# ‹לְמוֹעֲדָהּ מִיָּמִים יָמִימָה› (“to-seasons-her/its from-day day-ward”)
# "[EN-AID] And you shall keep this statute at its season, from days to
# days."
m.step("Exod.13.10")
# ‹הַזֹּאת לְמוֹעֲדָהּ מִיָּמִים› (“the-this to-seasons-her/its from-day”)
# ‹יָמִימָה› (“day-ward”)
# — fact holds: to-moada-from-day-yamima
m.fact("la_moada_mi_yamim_yamima")

# -------------------------- Exod.13.11 · WHEN_HE_BRINGS_YOU_LEAN -----------
# ‹וְהָיָה כִּי־יְבִאֲךָ יְהוָה› (“and-be that come/bring-you/your YHWH”)
# ‹אֶל־אֶרֶץ הַכְּנַעֲנִי כַּאֲשֶׁר› (“to earth the-Kenaanite like-
# as/which”)
# ‹נִשְׁבַּע לְךָ וְלַאֲבֹתֶיךָ› (“swear to-you/your and-to-father-
# you/your”)
# ‹וּנְתָנָהּ לָךְ› (“and-set-her/its to-you/your”)
# "[EN-AID] And it shall be, when the LORD brings you to the land of the
# Canaanite, as He swore to you and to your fathers, and gives it to you:"
m.step("Exod.13.11")
# ‹וְהָיָה כִּי־יְבִאֲךָ יְהוָה› (“and-be that come/bring-you/your YHWH”)
# — fact holds: that-yeviakha-lean
m.fact("ki_yeviakha_lean")

# -------------------------- Exod.13.12 · PASS_THE_WOMB_OPENERS -------------
# ‹וְהַעֲבַרְתָּ כָל־פֶּטֶר־רֶחֶם לַיהֹוָה› (“and-pass-over all fissure womb
# to-YHWH”)
# ‹וְכָל־פֶּטֶר שֶׁגֶר בְּהֵמָה› (“and-all fissure fetus livestock”)
# ‹אֲשֶׁר יִהְיֶה לְךָ› (“which be to-you/your”)
# ‹הַזְּכָרִים לַיהוָה› (“the-male to-YHWH”)
# "[EN-AID] Then you shall pass every opener of the womb to the LORD; and
# every firstling dropped of beast which you have, the males — to the LORD."
m.step("Exod.13.12")
# ‹וְהַעֲבַרְתָּ כָל־פֶּטֶר־רֶחֶם לַיהֹוָה› (“and-pass-over all fissure womb
# to-YHWH”)
# — fact holds: and-pass-over-all-fissure-womb
m.fact("ve_haavarta_khol_peter_rechem")
# witness-tier presupposed read: the_firstborn_engines_babylonian_layer on
# passing_verb — read, not installed
m.witness_read("passing_verb", "the_firstborn_engines_babylonian_layer",
                cites=["Bekhorot 4b:2", "Bekhorot 4b:3", "Bekhorot 4b:11", "Bekhorot 4b:12", "Bekhorot 4b:13", "Bekhorot 4b:14", "Bekhorot 4b:17", "Bekhorot 4b:18", "Bekhorot 4b:22", "Bekhorot 4b:23", "Bekhorot 5a:2", "Bekhorot 5a:3", "Yoma 49b:7", "Yoma 49b:8", "Niddah 40a:14", "Niddah 40a:16", "Niddah 40a:17", "Temurah 5b:13", "Temurah 18b:4", "Temurah 18b:5", "Temurah 4a:3", "Temurah 4a:4", "Eruvin 96a:6", "Eruvin 96a:7"])

# -------------------------- Exod.13.13 · THE_DONKEY_AND_THE_LAMB -----------
# ‹וְכָל־פֶּטֶר חֲמֹר תִּפְדֶּה› (“and-all fissure male-ass sever”)
# ‹בְשֶׂה וְאִם־לֹא תִפְדֶּה› (“in-member-of-a-flock and-if not sever”)
# ‹וַעֲרַפְתּוֹ וְכֹל בְּכוֹר› (“and-break-the-neck-him/its and-all
# firstborn”)
# ‹אָדָם בְּבָנֶיךָ תִּפְדֶּה› (“human in-son-you/your sever”)
# "[EN-AID] And every firstling of a donkey you shall redeem with a lamb,
# and if you do not redeem — you shall break its neck; and every firstborn
# of man among your sons you shall redeem."
m.step("Exod.13.13")
# ‹וְכָל־פֶּטֶר חֲמֹר תִּפְדֶּה› (“and-all fissure male-ass sever”)
# ‹בְשֶׂה› (“in-member-of-a-flock”)
# — fact holds: fissure-male-ass-sever-and-member-of-a-flock
m.fact("peter_chamor_tifde_ve_se")
# witness-tier presupposed read: firstborn_cluster on donkey_firstling —
# read, not installed
m.witness_read("donkey_firstling", "firstborn_cluster",
                cites=["Mishnah Bekhorot 1:2", "Mishnah Bekhorot 1:7", "Mishnah Bekhorot 2:6", "Mishnah Bekhorot 2:9", "Mishnah Bekhorot 8:1", "Mishnah Avodah Zarah 5:9"])

# -------------------------- Exod.13.14 · WHEN_YOUR_SON_ASKS_TOMORROW -------
# ‹וְהָיָה כִּי־יִשְׁאָלְךָ בִנְךָ› (“and-be that inquire-you/your son-
# you/your”)
# ‹מָחָר לֵאמֹר מַה־זֹּאת› (“deferred to-say what this”)
# ‹וְאָמַרְתָּ אֵלָיו בְּחֹזֶק› (“and-say to-him/its in-power”)
# ‹יָד הוֹצִיאָנוּ יְהוָה› (“hand bring-forth-us/our YHWH”)
# ‹מִמִּצְרַיִם מִבֵּית עֲבָדִים› (“from-Egypt from-house servant”)
# "[EN-AID] And it shall be, when your son asks you tomorrow, saying: What
# is this? — you shall say to him: By strength of hand the LORD brought us
# out from Egypt, from the house of slaves."
m.step("Exod.13.14")
# ‹וְהָיָה כִּי־יִשְׁאָלְךָ בִנְךָ› (“and-be that inquire-you/your son-
# you/your”)
# ‹מָחָר לֵאמֹר› (“deferred to-say”)
# — fact holds: that-yishalkha-vinkha-deferred
m.fact("ki_yishalkha_vinkha_machar")

# -------------------------- Exod.13.15 · WHEN_PHARAOH_HARDENED -------------
# ‹וַיְהִי כִּי־הִקְשָׁה פַרְעֹה› (“and-be that be-dense Pharaoh”)
# ‹לְשַׁלְּחֵנוּ וַיַּהֲרֹג יְהֹוָה› (“to-send-us/our and-smite-with-deadly-
# intent YHWH”)
# ‹כָּל־בְּכוֹר בְּאֶרֶץ מִצְרַיִם› (“all firstborn in-earth Egypt”)
# ‹מִבְּכֹר אָדָם וְעַד־בְּכוֹר› (“from-firstborn human and-until
# firstborn”)
# ‹בְּהֵמָה עַל־כֵּן אֲנִי› (“livestock over so”)
# ‹זֹבֵחַ לַיהוָה כָּל־פֶּטֶר› (“slaughter-an-animal to-YHWH all fissure”)
# ‹רֶחֶם הַזְּכָרִים וְכָל־בְּכוֹר› (“womb the-male and-all firstborn”)
# ‹בָּנַי אֶפְדֶּה› (“son-me/my sever”)
# "[EN-AID] And it was, when Pharaoh hardened against sending us, the LORD
# slew every firstborn in the land of Egypt, from the firstborn of man to
# the firstborn of beast; therefore I sacrifice to the LORD every opener of
# the womb, the males, and every firstborn of my sons I redeem."
m.step("Exod.13.15")
# ‹וַיְהִי כִּי־הִקְשָׁה פַרְעֹה› (“and-be that be-dense Pharaoh”)
# ‹לְשַׁלְּחֵנוּ וַיַּהֲרֹג› (“to-send-us/our and-smite-with-deadly-intent”)
# — fact holds: and-be-that-be-dense-Pharaoh
m.fact("va_yehi_ki_hiqsha_paro")

# -------------------------- Exod.13.16 · THE_WEAK_HAND ---------------------
# ‹וְהָיָה לְאוֹת עַל־יָדְכָה› (“and-be to-signs over hand-you/your”)
# ‹וּלְטוֹטָפֹת בֵּין עֵינֶיךָ› (“and-to-fillet-for-the-forehead between
# eye-you/your”)
# ‹כִּי בְּחֹזֶק יָד› (“that in-power hand”)
# ‹הוֹצִיאָנוּ יְהוָה מִמִּצְרָיִם› (“bring-forth-us/our YHWH from-Egypt”)
# "[EN-AID] And it shall be for a sign on your hand and for frontlets
# between your eyes — for by strength of hand the LORD brought us out from
# Egypt."
m.step("Exod.13.16")
# ‹וְהָיָה לְאוֹת עַל־יָדְכָה› (“and-be to-signs over hand-you/your”)
# ‹וּלְטוֹטָפֹת› (“and-to-fillet-for-the-forehead”)
# — fact holds: to-signs-over-yadkha-he
m.fact("le_ot_al_yadkha_he")
# witness-tier presupposed read: received_form on frontlets — read, not
# installed
m.witness_read("frontlets", "received_form",
                cites=["Mishnah Sanhedrin 11:3", "Mishnah Megillah 4:8"])
# witness-tier presupposed read: received_form_argued on
# tefillin_derivations — read, not installed
m.witness_read("tefillin_derivations", "received_form_argued",
                cites=["Menachot 34b:1", "Menachot 34b:2", "Menachot 34b:3", "Menachot 34b:5", "Menachot 37a:3", "Menachot 37a:4", "Menachot 44a:16", "Menachot 29b:1", "Menachot 29b:2", "Shabbat 108a:12", "Makkot 11a:8", "Arakhin 19b:6", "Eruvin 96a:10", "Eruvin 96a:11", "Kiddushin 35a:5", "Kiddushin 37b:13"])

# -------------------------- Exod.13.17 · NOT_BY_THE_NEAR_WAY ---------------
# ‹וַיְהִי בְּשַׁלַּח פַּרְעֹה› (“and-be in-send Pharaoh”)
# ‹אֶת־הָעָם וְלֹא־נָחָם אֱלֹהִים› (“obj-marker the-people and-not guide-
# them/their God”)
# ‹דֶּרֶךְ אֶרֶץ פְּלִשְׁתִּים› (“way/road earth Pelishtite”)
# ‹כִּי קָרוֹב הוּא› (“that near he/it”)
# ‹כִּי אָמַר אֱלֹהִים› (“that say God”)
# ‹פֶּן־יִנָּחֵם הָעָם בִּרְאֹתָם› (“lest sigh the-people in-see-
# them/their”)
# ‹מִלְחָמָה וְשָׁבוּ מִצְרָיְמָה› (“battle and-return Egypt-ward”)
# "[EN-AID] And it was, when Pharaoh sent the people, God did not lead them
# the way of the land of the Philistines, for it was near — for God said:
# Lest the people repent when they see war, and return to Egypt."
m.step("Exod.13.17")
# ‹וְלֹא־נָחָם אֱלֹהִים דֶּרֶךְ› (“and-not guide-them/their God way/road”)
# ‹אֶרֶץ פְּלִשְׁתִּים› (“earth Pelishtite”)
# — fact holds: and-not-nacham-way/road-Pelishtite
m.fact("ve_lo_nacham_derekh_pelishtim")

# -------------------------- Exod.13.18 · BY_THE_REED_SEA_ROAD --------------
# ‹וַיַּסֵּב אֱלֹהִים אֶת־הָעָם› (“and-revolve God obj-marker the-people”)
# ‹דֶּרֶךְ הַמִּדְבָּר יַם־סוּף› (“way/road the-pasture seas reed”)
# ‹וַחֲמֻשִׁים עָלוּ בְנֵי־יִשְׂרָאֵל› (“and-staunch go-up son Israel”)
# ‹מֵאֶרֶץ מִצְרָיִם› (“from-earth Egypt”)
# "[EN-AID] And God turned the people the way of the wilderness of the Reed
# Sea; and armed the sons of Israel went up from the land of Egypt."
m.step("Exod.13.18")
# ‹דֶּרֶךְ הַמִּדְבָּר יַם־סוּף› (“way/road the-pasture seas reed”)
# — fact holds: way/road-the-pasture-seas-reed
m.fact("derekh_ha_midbar_yam_suf")

# -------------------------- Exod.13.19 · THE_BONES_OF_JOSEPH ---------------
# ‹וַיִּקַּח מֹשֶׁה אֶת־עַצְמוֹת› (“and-take Moses obj-marker bone”)
# ‹יוֹסֵף עִמּוֹ כִּי› (“Joseph with-him/its that”)
# ‹הַשְׁבֵּעַ הִשְׁבִּיעַ אֶת־בְּנֵי› (“swear swear obj-marker son”)
# ‹יִשְׂרָאֵל לֵאמֹר פָּקֹד› (“Israel to-say count/visit”)
# ‹יִפְקֹד אֱלֹהִים אֶתְכֶם› (“count/visit God obj-marker-you/your(pl)”)
# ‹וְהַעֲלִיתֶם אֶת־עַצְמֹתַי מִזֶּה› (“and-go-up obj-marker bone-me/my
# from-this”)
# ‹אִתְּכֶם› (“obj-marker-you/your(pl)”)
# "[EN-AID] And Moses took the bones of Joseph with him; for he had surely
# sworn the sons of Israel, saying: God will surely visit you, and you shall
# bring up my bones from here with you."
m.step("Exod.13.19")
# ‹וַיִּקַּח מֹשֶׁה אֶת־עַצְמוֹת› (“and-take Moses obj-marker bone”)
# ‹יוֹסֵף› (“Joseph”)
# — fact holds: and-take-Moses-obj-marker-bone-Joseph
m.fact("va_yiqach_moshe_et_atzmot_yosef")

# -------------------------- Exod.13.20 · ETHAM_AT_THE_WILDERNESS_EDGE ------
# ‹וַיִּסְעוּ מִסֻּכֹּת וַיַּחֲנוּ› (“and-journey from-Succoth and-encamp”)
# ‹בְאֵתָם בִּקְצֵה הַמִּדְבָּר› (“in-Etham in-end the-pasture”)
# "[EN-AID] And they journeyed from Succoth, and camped in Etham, at the
# edge of the wilderness."
m.step("Exod.13.20")
# ‹וַיִּסְעוּ מִסֻּכֹּת וַיַּחֲנוּ› (“and-journey from-Succoth and-encamp”)
# — fact holds: and-encamp-and-Etham
m.fact("va_yachanu_ve_etam")

# -------------------------- Exod.13.21 · PILLAR_OF_CLOUD_PILLAR_OF_FIRE ----
# ‹וַיהוָה הֹלֵךְ לִפְנֵיהֶם› (“and-YHWH walk/go to-face-them/their”)
# ‹יוֹמָם בְּעַמּוּד עָנָן› (“daily in-column cloud”)
# ‹לַנְחֹתָם הַדֶּרֶךְ וְלַיְלָה› (“to-guide-them/their the-way/road and-
# night”)
# ‹בְּעַמּוּד אֵשׁ לְהָאִיר› (“in-column fire to-give-light”)
# ‹לָהֶם לָלֶכֶת יוֹמָם› (“to-them/their to-go daily”)
# ‹וָלָיְלָה› (“and-night”)
# "[EN-AID] And the LORD was going before them: by day in a pillar of cloud
# to lead them the way, and by night in a pillar of fire to give them light
# — to go by day and by night."
m.step("Exod.13.21")
# ‹וַיהוָה הֹלֵךְ לִפְנֵיהֶם› (“and-YHWH walk/go to-face-them/their”)
# ‹יוֹמָם בְּעַמּוּד עָנָן› (“daily in-column cloud”)
# — fact holds: column-cloud-and-column-fire
m.fact("amud_anan_ve_amud_esh")

# -------------------------- Exod.13.22 · IT_SHALL_NOT_DEPART ---------------
# ‹לֹא־יָמִישׁ עַמּוּד הֶעָנָן› (“not withdraw column the-cloud”)
# ‹יוֹמָם וְעַמּוּד הָאֵשׁ› (“daily and-column the-fire”)
# ‹לָיְלָה לִפְנֵי הָעָם› (“night to-face the-people”)
# "[EN-AID] The pillar of cloud shall not depart by day, nor the pillar of
# fire by night, before the people."
m.step("Exod.13.22")
# ‹לֹא־יָמִישׁ עַמּוּד הֶעָנָן› (“not withdraw column the-cloud”)
# — fact holds: not-withdraw-column-he-cloud
m.fact("lo_yamish_amud_he_anan")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['qadesh_li_khol_bekhor', 'zakhor_et_ha_yom_ha_ze']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yedaber_el_moshe', 'be_chodesh_ha_aviv', 've_avadta_et_ha_avoda', 'shivat_yamim_tokhal_matzot', 'lo_yerae_lekha_chametz', 've_higadta_le_vinkha', 'le_ot_al_yadkha_u_le_zikaron', 'la_moada_mi_yamim_yamima', 'ki_yeviakha_lean', 've_haavarta_khol_peter_rechem', 'peter_chamor_tifde_ve_se', 'ki_yishalkha_vinkha_machar', 'va_yehi_ki_hiqsha_paro', 'le_ot_al_yadkha_he', 've_lo_nacham_derekh_pelishtim', 'derekh_ha_midbar_yam_suf', 'va_yiqach_moshe_et_atzmot_yosef', 'va_yachanu_ve_etam', 'amud_anan_ve_amud_esh', 'lo_yamish_amud_he_anan'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 2
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('benefit_ban', 'recorded_routes'), ('export_operator', 'all_services_as_this'), ('the_telling', 'pointing_and_self_view'), ('passing_verb', 'the_firstborn_engines_babylonian_layer'), ('donkey_firstling', 'firstborn_cluster'), ('frontlets', 'received_form'), ('tefillin_derivations', 'received_form_argued')]
    assert m.WITNESS_READS[0]["cites"] == ['Pesachim 21b:5', 'Pesachim 21b:11', 'Pesachim 23a:12', 'Pesachim 24a:4', 'Pesachim 28b:4', 'Pesachim 29a:4']
    assert all('recorded_routes' not in f for f in m.WORLD["facts"])
    assert 'benefit_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Pesachim 96a:11', 'Pesachim 96a:12', 'Pesachim 96a:13', 'Pesachim 96a:14', 'Pesachim 96a:15', 'Pesachim 96a:16', 'Pesachim 96a:17', 'Pesachim 96a:18', 'Pesachim 96a:19', 'Pesachim 96a:20', 'Pesachim 96a:21', 'Pesachim 96a:22', 'Pesachim 96a:23', 'Pesachim 96a:24', 'Pesachim 96b:1', 'Pesachim 96b:2']
    assert all('all_services_as_this' not in f for f in m.WORLD["facts"])
    assert 'export_operator' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Pesachim 116b:3', 'Pesachim 116b:7', 'Pesachim 116b:8', 'Pesachim 116b:9']
    assert all('pointing_and_self_view' not in f for f in m.WORLD["facts"])
    assert 'the_telling' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bekhorot 4b:2', 'Bekhorot 4b:3', 'Bekhorot 4b:11', 'Bekhorot 4b:12', 'Bekhorot 4b:13', 'Bekhorot 4b:14', 'Bekhorot 4b:17', 'Bekhorot 4b:18', 'Bekhorot 4b:22', 'Bekhorot 4b:23', 'Bekhorot 5a:2', 'Bekhorot 5a:3', 'Yoma 49b:7', 'Yoma 49b:8', 'Niddah 40a:14', 'Niddah 40a:16', 'Niddah 40a:17', 'Temurah 5b:13', 'Temurah 18b:4', 'Temurah 18b:5', 'Temurah 4a:3', 'Temurah 4a:4', 'Eruvin 96a:6', 'Eruvin 96a:7']
    assert all('the_firstborn_engines_babylonian_layer' not in f for f in m.WORLD["facts"])
    assert 'passing_verb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mishnah Bekhorot 1:2', 'Mishnah Bekhorot 1:7', 'Mishnah Bekhorot 2:6', 'Mishnah Bekhorot 2:9', 'Mishnah Bekhorot 8:1', 'Mishnah Avodah Zarah 5:9']
    assert all('firstborn_cluster' not in f for f in m.WORLD["facts"])
    assert 'donkey_firstling' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Sanhedrin 11:3', 'Mishnah Megillah 4:8']
    assert all('received_form' not in f for f in m.WORLD["facts"])
    assert 'frontlets' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Menachot 34b:1', 'Menachot 34b:2', 'Menachot 34b:3', 'Menachot 34b:5', 'Menachot 37a:3', 'Menachot 37a:4', 'Menachot 44a:16', 'Menachot 29b:1', 'Menachot 29b:2', 'Shabbat 108a:12', 'Makkot 11a:8', 'Arakhin 19b:6', 'Eruvin 96a:10', 'Eruvin 96a:11', 'Kiddushin 35a:5', 'Kiddushin 37b:13']
    assert all('received_form_argued' not in f for f in m.WORLD["facts"])
    assert 'tefillin_derivations' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
