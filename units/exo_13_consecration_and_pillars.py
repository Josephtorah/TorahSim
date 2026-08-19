#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Exod.13.1")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר› (“and-speak YHWH to Moses to-say”)
# — fact holds: and-speak-to-Moses
m.fact("va_yedaber_el_moshe")

# -------------------------- Exod.13.2 · CONSECRATE_THE_FIRSTBORN -----------
# קַדֶּשׁ־לִי כָל־בְּכוֹר פֶּטֶר כָּל־רֶחֶם בִּבְנֵי יִשְׂרָאֵל בָּאָדָם
# וּבַבְּהֵמָה לִי הוּא
# "[EN-AID] Consecrate to Me every firstborn, opener of every womb among the
# sons of Israel, in man and in beast — Mine is it."
m.step("Exod.13.2")
# ‹קַדֶּשׁ־לִי כָל־בְּכוֹר› (“sanctify to-me/my all firstborn”) — the-LORD
# speaks a demand — LET: sanctify-to-me-all-firstborn
m.declare("YHWH", "LET",
          "qadesh_li_khol_bekhor")

# -------------------------- Exod.13.3 · REMEMBER_THIS_DAY ------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־הָעָם זָכוֹר אֶת־הַיּוֹם הַזֶּה אֲשֶׁר יְצָאתֶם
# מִמִּצְרַיִם מִבֵּית עֲבָדִים כִּי בְּחֹזֶק יָד הוֹצִיא יְהֹוָה אֶתְכֶם
# מִזֶּה וְלֹא יֵאָכֵל חָמֵץ
# "[EN-AID] And Moses said to the people: Remember this day on which you
# went out from Egypt, from the house of slaves — for by strength of hand
# the LORD brought you out from this place; and no leavened bread shall be
# eaten."
m.step("Exod.13.3")
# ‹זָכוֹר אֶת־הַיּוֹם הַזֶּה› (“mark obj-marker the-day the-this”) — Moses
# speaks a demand — LET: mark-obj-marker-the-day-the-this
m.declare("moshe", "LET",
          "zakhor_et_ha_yom_ha_ze")

# -------------------------- Exod.13.4 · IN_THE_MONTH_OF_AVIV ---------------
# הַיּוֹם אַתֶּם יֹצְאִים בְּחֹדֶשׁ הָאָבִיב
# "[EN-AID] Today you are going out, in the month of the Aviv."
m.step("Exod.13.4")
# ‹הַיּוֹם אַתֶּם יֹצְאִים בְּחֹדֶשׁ הָאָבִיב› (“the-day you bring-forth in-
# new-moon the-green”) — fact holds: in-new-moon-the-green
m.fact("be_chodesh_ha_aviv")

# -------------------------- Exod.13.5 · THE_SERVICE_IN_THE_LAND ------------
# וְהָיָה כִי־יְבִיאֲךָ יְהוָה אֶל־אֶרֶץ הַכְּנַעֲנִי וְהַחִתִּי וְהָאֱמֹרִי
# וְהַחִוִּי וְהַיְבוּסִי אֲשֶׁר נִשְׁבַּע לַאֲבֹתֶיךָ לָתֶת לָךְ אֶרֶץ
# זָבַת חָלָב וּדְבָשׁ וְעָבַדְתָּ אֶת־הָעֲבֹדָה הַזֹּאת בַּחֹדֶשׁ הַזֶּה
# "[EN-AID] And it shall be, when the LORD brings you to the land of the
# Canaanite and the Hittite and the Amorite and the Hivvite and the
# Jebusite, which He swore to your fathers to give you, a land flowing with
# milk and honey — you shall serve this service in this month."
m.step("Exod.13.5")
# ‹אֶת־הָעֲבֹדָה הַזֹּאת בַּחֹדֶשׁ הַזֶּה› (“obj-marker the-service/work
# the-this in-new-moon the-this”) — fact holds: and-work/serve-obj-marker-
# the-service/work
m.fact("ve_avadta_et_ha_avoda")

# -------------------------- Exod.13.6 · SEVEN_DAYS_AND_A_FEAST -------------
# שִׁבְעַת יָמִים תֹּאכַל מַצֹּת וּבַיּוֹם הַשְּׁבִיעִי חַג לַיהוָה
# "[EN-AID] Seven days you shall eat unleavened bread, and on the seventh
# day is a feast to the LORD."
m.step("Exod.13.6")
# ‹שִׁבְעַת יָמִים תֹּאכַל מַצֹּת› (“seven day eat sweetness”) — fact holds:
# seven-day-eat-sweetness
m.fact("shivat_yamim_tokhal_matzot")

# -------------------------- Exod.13.7 · NO_LEAVEN_SEEN ---------------------
# מַצּוֹת יֵאָכֵל אֵת שִׁבְעַת הַיָּמִים וְלֹא־יֵרָאֶה לְךָ חָמֵץ
# וְלֹא־יֵרָאֶה לְךָ שְׂאֹר בְּכָל־גְּבֻלֶךָ
# "[EN-AID] Unleavened bread shall be eaten the seven days; and nothing
# leavened shall be seen for you, and no leaven shall be seen for you in all
# your border."
m.step("Exod.13.7")
# ‹וְלֹא־יֵרָאֶה לְךָ חָמֵץ וְלֹא־יֵרָאֶה› (“and-not see to-you/your ferment
# and-not see”) — fact holds: not-see-to-you-ferment
m.fact("lo_yerae_lekha_chametz")

# -------------------------- Exod.13.8 · AND_YOU_SHALL_TELL_YOUR_SON --------
# וְהִגַּדְתָּ לְבִנְךָ בַּיּוֹם הַהוּא לֵאמֹר בַּעֲבוּר זֶה עָשָׂה יְהוָה
# לִי בְּצֵאתִי מִמִּצְרָיִם
# "[EN-AID] And you shall tell your son in that day, saying: For the sake of
# this the LORD acted for me in my going out from Egypt."
m.step("Exod.13.8")
# ‹וְהִגַּדְתָּ לְבִנְךָ בַּיּוֹם הַהוּא לֵאמֹר› (“and-tell to-son-you/your
# in-day that to-say”) — fact holds: and-tell-to-vinkha
m.fact("ve_higadta_le_vinkha")

# -------------------------- Exod.13.9 · A_SIGN_ON_YOUR_HAND ----------------
# וְהָיָה לְךָ לְאוֹת עַל־יָדְךָ וּלְזִכָּרוֹן בֵּין עֵינֶיךָ לְמַעַן
# תִּהְיֶה תּוֹרַת יְהוָה בְּפִיךָ כִּי בְּיָד חֲזָקָה הוֹצִאֲךָ יְהֹוָה
# מִמִּצְרָיִם
# "[EN-AID] And it shall be for you for a sign on your hand and for a
# memorial between your eyes, in order that the Torah of the LORD be in your
# mouth — for with a strong hand the LORD brought you out from Egypt."
m.step("Exod.13.9")
# ‹וְהָיָה לְךָ לְאוֹת עַל־יָדְךָ וּלְזִכָּרוֹן בֵּין עֵינֶיךָ› (“and-be to-
# you/your to-signs over hand-you/your and-to-memento between eye-you/your”)
# — fact holds: to-signs-over-yadkha-and-to-memento
m.fact("le_ot_al_yadkha_u_le_zikaron")

# -------------------------- Exod.13.10 · AT_ITS_SEASON ---------------------
# וְשָׁמַרְתָּ אֶת־הַחֻקָּה הַזֹּאת לְמוֹעֲדָהּ מִיָּמִים יָמִימָה
# "[EN-AID] And you shall keep this statute at its season, from days to
# days."
m.step("Exod.13.10")
# ‹הַזֹּאת לְמוֹעֲדָהּ מִיָּמִים יָמִימָה› (“the-this to-seasons-her/its
# from-day day-ward”) — fact holds: to-moada-from-day-yamima
m.fact("la_moada_mi_yamim_yamima")

# -------------------------- Exod.13.11 · WHEN_HE_BRINGS_YOU_LEAN -----------
# וְהָיָה כִּי־יְבִאֲךָ יְהוָה אֶל־אֶרֶץ הַכְּנַעֲנִי כַּאֲשֶׁר נִשְׁבַּע
# לְךָ וְלַאֲבֹתֶיךָ וּנְתָנָהּ לָךְ
# "[EN-AID] And it shall be, when the LORD brings you to the land of the
# Canaanite, as He swore to you and to your fathers, and gives it to you:"
m.step("Exod.13.11")
# ‹וְהָיָה כִּי־יְבִאֲךָ יְהוָה› (“and-be that come/bring-you/your YHWH”) —
# fact holds: that-yeviakha-lean
m.fact("ki_yeviakha_lean")

# -------------------------- Exod.13.12 · PASS_THE_WOMB_OPENERS -------------
# וְהַעֲבַרְתָּ כָל־פֶּטֶר־רֶחֶם לַיהֹוָה וְכָל־פֶּטֶר שֶׁגֶר בְּהֵמָה
# אֲשֶׁר יִהְיֶה לְךָ הַזְּכָרִים לַיהוָה
# "[EN-AID] Then you shall pass every opener of the womb to the LORD; and
# every firstling dropped of beast which you have, the males — to the LORD."
m.step("Exod.13.12")
# ‹וְהַעֲבַרְתָּ כָל־פֶּטֶר־רֶחֶם לַיהֹוָה› (“and-pass-over all fissure womb
# to-YHWH”) — fact holds: and-pass-over-all-fissure-womb
m.fact("ve_haavarta_khol_peter_rechem")

# -------------------------- Exod.13.13 · THE_DONKEY_AND_THE_LAMB -----------
# וְכָל־פֶּטֶר חֲמֹר תִּפְדֶּה בְשֶׂה וְאִם־לֹא תִפְדֶּה וַעֲרַפְתּוֹ וְכֹל
# בְּכוֹר אָדָם בְּבָנֶיךָ תִּפְדֶּה
# "[EN-AID] And every firstling of a donkey you shall redeem with a lamb,
# and if you do not redeem — you shall break its neck; and every firstborn
# of man among your sons you shall redeem."
m.step("Exod.13.13")
# ‹וְכָל־פֶּטֶר חֲמֹר תִּפְדֶּה בְשֶׂה› (“and-all fissure male-ass sever in-
# member-of-a-flock”) — fact holds: fissure-male-ass-sever-and-member-of-a-
# flock
m.fact("peter_chamor_tifde_ve_se")

# -------------------------- Exod.13.14 · WHEN_YOUR_SON_ASKS_TOMORROW -------
# וְהָיָה כִּי־יִשְׁאָלְךָ בִנְךָ מָחָר לֵאמֹר מַה־זֹּאת וְאָמַרְתָּ אֵלָיו
# בְּחֹזֶק יָד הוֹצִיאָנוּ יְהוָה מִמִּצְרַיִם מִבֵּית עֲבָדִים
# "[EN-AID] And it shall be, when your son asks you tomorrow, saying: What
# is this? — you shall say to him: By strength of hand the LORD brought us
# out from Egypt, from the house of slaves."
m.step("Exod.13.14")
# ‹וְהָיָה כִּי־יִשְׁאָלְךָ בִנְךָ מָחָר לֵאמֹר› (“and-be that inquire-
# you/your son-you/your deferred to-say”) — fact holds: that-yishalkha-
# vinkha-deferred
m.fact("ki_yishalkha_vinkha_machar")

# -------------------------- Exod.13.15 · WHEN_PHARAOH_HARDENED -------------
# וַיְהִי כִּי־הִקְשָׁה פַרְעֹה לְשַׁלְּחֵנוּ וַיַּהֲרֹג יְהֹוָה
# כָּל־בְּכוֹר בְּאֶרֶץ מִצְרַיִם מִבְּכֹר אָדָם וְעַד־בְּכוֹר בְּהֵמָה
# עַל־כֵּן אֲנִי זֹבֵחַ לַיהוָה כָּל־פֶּטֶר רֶחֶם הַזְּכָרִים וְכָל־בְּכוֹר
# בָּנַי אֶפְדֶּה
# "[EN-AID] And it was, when Pharaoh hardened against sending us, the LORD
# slew every firstborn in the land of Egypt, from the firstborn of man to
# the firstborn of beast; therefore I sacrifice to the LORD every opener of
# the womb, the males, and every firstborn of my sons I redeem."
m.step("Exod.13.15")
# ‹וַיְהִי כִּי־הִקְשָׁה פַרְעֹה לְשַׁלְּחֵנוּ וַיַּהֲרֹג› (“and-be that be-
# dense Pharaoh to-send-us/our and-smite-with-deadly-intent”) — fact holds:
# and-be-that-be-dense-Pharaoh
m.fact("va_yehi_ki_hiqsha_paro")

# -------------------------- Exod.13.16 · THE_WEAK_HAND ---------------------
# וְהָיָה לְאוֹת עַל־יָדְכָה וּלְטוֹטָפֹת בֵּין עֵינֶיךָ כִּי בְּחֹזֶק יָד
# הוֹצִיאָנוּ יְהוָה מִמִּצְרָיִם
# "[EN-AID] And it shall be for a sign on your hand and for frontlets
# between your eyes — for by strength of hand the LORD brought us out from
# Egypt."
m.step("Exod.13.16")
# ‹וְהָיָה לְאוֹת עַל־יָדְכָה וּלְטוֹטָפֹת› (“and-be to-signs over hand-
# you/your and-to-fillet-for-the-forehead”) — fact holds: to-signs-over-
# yadkha-he
m.fact("le_ot_al_yadkha_he")

# -------------------------- Exod.13.17 · NOT_BY_THE_NEAR_WAY ---------------
# וַיְהִי בְּשַׁלַּח פַּרְעֹה אֶת־הָעָם וְלֹא־נָחָם אֱלֹהִים דֶּרֶךְ אֶרֶץ
# פְּלִשְׁתִּים כִּי קָרוֹב הוּא כִּי אָמַר אֱלֹהִים פֶּן־יִנָּחֵם הָעָם
# בִּרְאֹתָם מִלְחָמָה וְשָׁבוּ מִצְרָיְמָה
# "[EN-AID] And it was, when Pharaoh sent the people, God did not lead them
# the way of the land of the Philistines, for it was near — for God said:
# Lest the people repent when they see war, and return to Egypt."
m.step("Exod.13.17")
# ‹וְלֹא־נָחָם אֱלֹהִים דֶּרֶךְ אֶרֶץ פְּלִשְׁתִּים› (“and-not guide-
# them/their God way/road earth Pelishtite”) — fact holds: and-not-nacham-
# way/road-Pelishtite
m.fact("ve_lo_nacham_derekh_pelishtim")

# -------------------------- Exod.13.18 · BY_THE_REED_SEA_ROAD --------------
# וַיַּסֵּב אֱלֹהִים אֶת־הָעָם דֶּרֶךְ הַמִּדְבָּר יַם־סוּף וַחֲמֻשִׁים
# עָלוּ בְנֵי־יִשְׂרָאֵל מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And God turned the people the way of the wilderness of the Reed
# Sea; and armed the sons of Israel went up from the land of Egypt."
m.step("Exod.13.18")
# ‹דֶּרֶךְ הַמִּדְבָּר יַם־סוּף› (“way/road the-pasture seas reed”) — fact
# holds: way/road-the-pasture-seas-reed
m.fact("derekh_ha_midbar_yam_suf")

# -------------------------- Exod.13.19 · THE_BONES_OF_JOSEPH ---------------
# וַיִּקַּח מֹשֶׁה אֶת־עַצְמוֹת יוֹסֵף עִמּוֹ כִּי הַשְׁבֵּעַ הִשְׁבִּיעַ
# אֶת־בְּנֵי יִשְׂרָאֵל לֵאמֹר פָּקֹד יִפְקֹד אֱלֹהִים אֶתְכֶם וְהַעֲלִיתֶם
# אֶת־עַצְמֹתַי מִזֶּה אִתְּכֶם
# "[EN-AID] And Moses took the bones of Joseph with him; for he had surely
# sworn the sons of Israel, saying: God will surely visit you, and you shall
# bring up my bones from here with you."
m.step("Exod.13.19")
# ‹וַיִּקַּח מֹשֶׁה אֶת־עַצְמוֹת יוֹסֵף› (“and-take Moses obj-marker bone
# Joseph”) — fact holds: and-take-Moses-obj-marker-bone-Joseph
m.fact("va_yiqach_moshe_et_atzmot_yosef")

# -------------------------- Exod.13.20 · ETHAM_AT_THE_WILDERNESS_EDGE ------
# וַיִּסְעוּ מִסֻּכֹּת וַיַּחֲנוּ בְאֵתָם בִּקְצֵה הַמִּדְבָּר
# "[EN-AID] And they journeyed from Succoth, and camped in Etham, at the
# edge of the wilderness."
m.step("Exod.13.20")
# ‹וַיִּסְעוּ מִסֻּכֹּת וַיַּחֲנוּ› (“and-journey from-Succoth and-encamp”)
# — fact holds: and-encamp-and-Etham
m.fact("va_yachanu_ve_etam")

# -------------------------- Exod.13.21 · PILLAR_OF_CLOUD_PILLAR_OF_FIRE ----
# וַיהוָה הֹלֵךְ לִפְנֵיהֶם יוֹמָם בְּעַמּוּד עָנָן לַנְחֹתָם הַדֶּרֶךְ
# וְלַיְלָה בְּעַמּוּד אֵשׁ לְהָאִיר לָהֶם לָלֶכֶת יוֹמָם וָלָיְלָה
# "[EN-AID] And the LORD was going before them: by day in a pillar of cloud
# to lead them the way, and by night in a pillar of fire to give them light
# — to go by day and by night."
m.step("Exod.13.21")
# ‹וַיהוָה הֹלֵךְ לִפְנֵיהֶם יוֹמָם בְּעַמּוּד עָנָן› (“and-YHWH walk/go to-
# face-them/their daily in-column cloud”) — fact holds: column-cloud-and-
# column-fire
m.fact("amud_anan_ve_amud_esh")

# -------------------------- Exod.13.22 · IT_SHALL_NOT_DEPART ---------------
# לֹא־יָמִישׁ עַמּוּד הֶעָנָן יוֹמָם וְעַמּוּד הָאֵשׁ לָיְלָה לִפְנֵי הָעָם
# "[EN-AID] The pillar of cloud shall not depart by day, nor the pillar of
# fire by night, before the people."
m.step("Exod.13.22")
# ‹לֹא־יָמִישׁ עַמּוּד הֶעָנָן› (“not withdraw column the-cloud”) — fact
# holds: not-withdraw-column-he-cloud
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
