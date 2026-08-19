#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_01_names_and_midwives — 1:1-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_01_names_and_midwives.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The names and the midwives (1:1-22)"""
from machine import Machine

m = Machine("exo_01_names_and_midwives")

# -------------------------- Exod.1.1 · THE_NAMES_REOPENED ------------------
# וְאֵלֶּה שְׁמוֹת בְּנֵי יִשְׂרָאֵל הַבָּאִים מִצְרָיְמָה אֵת יַעֲקֹב אִישׁ
# וּבֵיתוֹ בָּאוּ
# "[EN-AID] And these are the names of the sons of Israel who came to Egypt;
# with Jacob, each man and his household, they came."
m.step("Exod.1.1")
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי יִשְׂרָאֵל› (“and-these name son Israel”) —
# section name-son-Israel: son-lea, son-rachel, son-the-shefachot
m.section("shemot_bene_yisrael", "bene_lea", "ben_rachel", "bene_ha_shefachot")

# -------------------------- Exod.1.2 · LEAHS_FOUR --------------------------
# רְאוּבֵן שִׁמְעוֹן לֵוִי וִיהוּדָה
# "[EN-AID] Reuben, Simeon, Levi, and Judah;"
m.step("Exod.1.2")
# ‹רְאוּבֵן שִׁמְעוֹן לֵוִי וִיהוּדָה› (“Reuben Simeon Levi and-Judah”) —
# fact holds: Reuben-Simeon-Levi-vi-yhuda
m.fact("reuven_shimon_levi_vi_yhuda")

# -------------------------- Exod.1.3 · LEAHS_LAST_AND_RACHELS --------------
# יִשָּׂשכָר זְבוּלֻן וּבְנְיָמִן
# "[EN-AID] Issachar, Zebulun, and Benjamin;"
m.step("Exod.1.3")
# ‹יִשָּׂשכָר זְבוּלֻן וּבְנְיָמִן› (“Issachar Zebulun and-Benjamin”) — fact
# holds: Issachar-Zebulun-and-Benjamin
m.fact("yisashkhar_zevulun_u_venyamin")

# -------------------------- Exod.1.4 · THE_HANDMAIDS_FOUR ------------------
# דָּן וְנַפְתָּלִי גָּד וְאָשֵׁר
# "[EN-AID] Dan, and Naphtali; Gad, and Asher."
m.step("Exod.1.4")
# ‹דָּן וְנַפְתָּלִי גָּד וְאָשֵׁר› (“Daniel and-Naphtali Gad and-Asher”) —
# fact holds: Daniel-and-Naphtali-Gad-and-Asher
m.fact("dan_ve_naftali_gad_ve_asher")

# -------------------------- Exod.1.5 · SEVENTY_SOULS_AND_JOSEPH ------------
# וַיְהִי כָּל־נֶפֶשׁ יֹצְאֵי יֶרֶךְ־יַעֲקֹב שִׁבְעִים נָפֶשׁ וְיוֹסֵף הָיָה
# בְמִצְרָיִם
# "[EN-AID] And all the souls that came out of the loins of Jacob were
# seventy souls; and Joseph was in Egypt."
m.step("Exod.1.5")
# ‹יַעֲקֹב שִׁבְעִים נָפֶשׁ וְיוֹסֵף הָיָה בְמִצְרָיִם› (“Jacob seventy
# living-being and-Joseph be in-Egypt”) — fact holds: seventy-living-being-
# and-Joseph-in-Egypt
m.fact("shivim_nefesh_ve_yosef_be_mitzrayim")

# -------------------------- Exod.1.6 · THE_DEATH_RETOLD --------------------
# וַיָּמָת יוֹסֵף וְכָל־אֶחָיו וְכֹל הַדּוֹר הַהוּא
# "[EN-AID] And Joseph died, and all his brothers, and all that generation."
m.step("Exod.1.6")
# ‹וַיָּמָת יוֹסֵף› (“and-die Joseph”) — fact holds: and-die-Joseph-and-all-
# the-generation
m.fact("va_yamat_yosef_ve_khol_ha_dor")

# -------------------------- Exod.1.7 · THE_SIX_INCREASE_WORDS --------------
# וּבְנֵי יִשְׂרָאֵל פָּרוּ וַיִּשְׁרְצוּ וַיִּרְבּוּ וַיַּעַצְמוּ בִּמְאֹד
# מְאֹד וַתִּמָּלֵא הָאָרֶץ אֹתָם
# "[EN-AID] And the sons of Israel were fruitful, and swarmed, and
# multiplied, and grew mighty — exceedingly, exceedingly; and the land was
# filled with them."
m.step("Exod.1.7")
# ‹פָּרוּ וַיִּשְׁרְצוּ וַיִּרְבּוּ וַיַּעַצְמוּ בִּמְאֹד מְאֹד› (“be-
# fruitful and-swarm and-multiply and-bind-fast in-very very”) — fact holds:
# and-fill-the-earth-otam
m.fact("va_timale_ha_aretz_otam")

# -------------------------- Exod.1.8 · A_KING_WHO_KNEW_NOT -----------------
# וַיָּקָם מֶלֶךְ־חָדָשׁ עַל־מִצְרָיִם אֲשֶׁר לֹא־יָדַע אֶת־יוֹסֵף
# "[EN-AID] And there arose a new king over Egypt, who knew not Joseph."
m.step("Exod.1.8")
# ‹וַיָּקָם מֶלֶךְ־חָדָשׁ עַל־מִצְרָיִם› (“and-arise king new over Egypt”) —
# event: qam — agent king-new
m.event("qam", agent="melekh_chadash")

# -------------------------- Exod.1.9 · BEHOLD_THE_PEOPLE -------------------
# וַיֹּאמֶר אֶל־עַמּוֹ הִנֵּה עַם בְּנֵי יִשְׂרָאֵל רַב וְעָצוּם מִמֶּנּוּ
# "[EN-AID] And he said to his people: Behold, the people of the sons of
# Israel are more numerous and mightier than we."
m.step("Exod.1.9")
# ‹רַב וְעָצוּם מִמֶּנּוּ› (“many/great and-powerful from-us/our”) — fact
# holds: many/great-and-powerful-from-it
m.fact("rav_ve_atzum_mimenu")

# -------------------------- Exod.1.10 · COME_LET_US_OUTWIT -----------------
# הָבָה נִתְחַכְּמָה לוֹ פֶּן־יִרְבֶּה וְהָיָה כִּי־תִקְרֶאנָה מִלְחָמָה
# וְנוֹסַף גַּם־הוּא עַל־שֹׂנְאֵינוּ וְנִלְחַם־בָּנוּ וְעָלָה מִן־הָאָרֶץ
# "[EN-AID] Come, let us deal wisely with him, lest he multiply, and it come
# to pass, when war befalls, that he too be added to our enemies, and fight
# against us, and go up from the land."
m.step("Exod.1.10")
# ‹הָבָה נִתְחַכְּמָה לוֹ› (“give-ward be-wise to-him/its”) — king-new
# speaks a demand — LET: hava-be-wise-not
m.declare("melekh_chadash", "LET",
          "hava_nitchakma_lo")

# -------------------------- Exod.1.11 · TASKMASTERS_SET --------------------
# וַיָּשִׂימוּ עָלָיו שָׂרֵי מִסִּים לְמַעַן עַנֹּתוֹ בְּסִבְלֹתָם וַיִּבֶן
# עָרֵי מִסְכְּנוֹת לְפַרְעֹה אֶת־פִּתֹם וְאֶת־רַעַמְסֵס
# "[EN-AID] And they set over him taskmasters of levies, in order to afflict
# him with their burdens; and he built store-cities for Pharaoh: Pitom, and
# Raamses."
m.step("Exod.1.11")
# ‹וַיָּשִׂימוּ עָלָיו שָׂרֵי מִסִּים לְמַעַן עַנֹּתוֹ בְּסִבְלֹתָם› (“and-
# put/set over-him/its officer burden so-that afflict-literally-him/its in-
# porterage-them/their”) — demand settled (popped from the queue): hava-be-
# wise-not
m.result("hava_nitchakma_lo", tmark="t1")

# -------------------------- Exod.1.12 · THE_MORE_AFFLICTED_THE_MORE --------
# וְכַאֲשֶׁר יְעַנּוּ אֹתוֹ כֵּן יִרְבֶּה וְכֵן יִפְרֹץ וַיָּקֻצוּ מִפְּנֵי
# בְּנֵי יִשְׂרָאֵל
# "[EN-AID] And as they afflicted him, so he multiplied and so he spread;
# and they dreaded because of the sons of Israel."
m.step("Exod.1.12")
# ‹כֵּן יִרְבֶּה וְכֵן יִפְרֹץ› (“so multiply and-so break-out”) — fact
# holds: so-multiply-and-so-break-out
m.fact("ken_yirbe_ve_khen_yifrotz")

# -------------------------- Exod.1.13 · WITH_CRUSHING_SERVICE --------------
# וַיַּעֲבִדוּ מִצְרַיִם אֶת־בְּנֵי יִשְׂרָאֵל בְּפָרֶךְ
# "[EN-AID] And Egypt made the sons of Israel serve with crushing service."
m.step("Exod.1.13")
# ‹וַיַּעֲבִדוּ מִצְרַיִם אֶת־בְּנֵי יִשְׂרָאֵל בְּפָרֶךְ› (“and-work/serve
# Egyptian obj-marker son Israel in-fracture”) — fact holds: and-work/serve-
# Egypt-in-fracture
m.fact("va_yaavidu_mitzrayim_be_farekh")

# -------------------------- Exod.1.14 · THE_FOUR_AFFLICTIONS ---------------
# וַיְמָרְרוּ אֶת־חַיֵּיהֶם בַּעֲבֹדָה קָשָׁה בְּחֹמֶר וּבִלְבֵנִים
# וּבְכָל־עֲבֹדָה בַּשָּׂדֶה אֵת כָּל־עֲבֹדָתָם אֲשֶׁר־עָבְדוּ בָהֶם
# בְּפָרֶךְ
# "[EN-AID] And they made their lives bitter with hard service — with mortar
# and with bricks, and with all service in the field; all their service in
# which they made them serve with crushing service."
m.step("Exod.1.14")
# ‹וַיְמָרְרוּ אֶת־חַיֵּיהֶם בַּעֲבֹדָה קָשָׁה› (“and-be-bitter obj-marker
# alive-them/their in-service/work severe”) — fact holds: and-be-bitter-
# with-chayehem
m.fact("va_yemarru_et_chayehem")

# -------------------------- Exod.1.15 · SHIFRA_AND_PUA ---------------------
# וַיֹּאמֶר מֶלֶךְ מִצְרַיִם לַמְיַלְּדֹת הָעִבְרִיֹּת אֲשֶׁר שֵׁם הָאַחַת
# שִׁפְרָה וְשֵׁם הַשֵּׁנִית פּוּעָה
# "[EN-AID] And the king of Egypt said to the midwives of the Hebrews, of
# whom the name of the one was Shifra, and the name of the second Pua:"
m.step("Exod.1.15")
# ‹הָאַחַת שִׁפְרָה וְשֵׁם הַשֵּׁנִית פּוּעָה› (“the-one Shiphrah and-name
# the-second Puah”) — fact holds: Shiphrah-and-fua
m.fact("shifra_u_fua")

# -------------------------- Exod.1.16 · THE_KILL_ORDER ---------------------
# וַיֹּאמֶר בְּיַלֶּדְכֶן אֶת־הָעִבְרִיּוֹת וּרְאִיתֶן עַל־הָאָבְנָיִם
# אִם־בֵּן הוּא וַהֲמִתֶּן אֹתוֹ וְאִם־בַּת הִיא וָחָיָה
# "[EN-AID] And he said: When you deliver the Hebrew women, and you see upon
# the birthstool: if it is a son, you shall kill him; and if it is a
# daughter, she shall live."
m.step("Exod.1.16")
# ‹אִם־בֵּן הוּא וַהֲמִתֶּן אֹתוֹ› (“if son he/it and-die obj-marker-
# him/its”) — king-Egypt speaks a demand — LET: if-son-that-and-die-it
m.declare("melekh_mitzrayim", "LET",
          "im_ben_hu_va_hamiten_oto")

# -------------------------- Exod.1.17 · THEY_DID_NOT_DO --------------------
# וַתִּירֶאןָ הַמְיַלְּדֹת אֶת־הָאֱלֹהִים וְלֹא עָשׂוּ כַּאֲשֶׁר דִּבֶּר
# אֲלֵיהֶן מֶלֶךְ מִצְרָיִם וַתְּחַיֶּיןָ אֶת־הַיְלָדִים
# "[EN-AID] And the midwives feared God, and did not do as the king of Egypt
# spoke to them; and they kept the children alive."
m.step("Exod.1.17")
# ‹וְלֹא עָשׂוּ כַּאֲשֶׁר דִּבֶּר אֲלֵיהֶן מֶלֶךְ מִצְרָיִם› (“and-not make
# like-as/which speak to-them/their king Egypt”) — fact holds: and-not-make-
# kaasher-speak
m.fact("ve_lo_asu_kaasher_diber")

# -------------------------- Exod.1.18 · WHY_HAVE_YOU_DONE ------------------
# וַיִּקְרָא מֶלֶךְ־מִצְרַיִם לַמְיַלְּדֹת וַיֹּאמֶר לָהֶן מַדּוּעַ
# עֲשִׂיתֶן הַדָּבָר הַזֶּה וַתְּחַיֶּיןָ אֶת־הַיְלָדִים
# "[EN-AID] And the king of Egypt called the midwives, and said to them: Why
# have you done this thing, and kept the children alive?"
m.step("Exod.1.18")
# ‹מַדּוּעַ עֲשִׂיתֶן הַדָּבָר הַזֶּה› (“what-known? make the-word/thing
# the-this”) — fact holds: what-known?-make
m.fact("madua_asiten")

# -------------------------- Exod.1.19 · FOR_THEY_ARE_LIVELY ----------------
# וַתֹּאמַרְןָ הַמְיַלְּדֹת אֶל־פַּרְעֹה כִּי לֹא כַנָּשִׁים הַמִּצְרִיֹּת
# הָעִבְרִיֹּת כִּי־חָיוֹת הֵנָּה בְּטֶרֶם תָּבוֹא אֲלֵהֶן הַמְיַלֶּדֶת
# וְיָלָדוּ
# "[EN-AID] And the midwives said to Pharaoh: Because the Hebrew women are
# not as the Egyptian women, for they are lively; before the midwife comes
# to them, they have given birth."
m.step("Exod.1.19")
# ‹כִּי־חָיוֹת הֵנָּה› (“that vigorous themselves”) — fact holds: that-
# vigorous-themselves
m.fact("ki_chayot_hena")

# -------------------------- Exod.1.20 · GOD_DEALT_WELL ---------------------
# וַיֵּיטֶב אֱלֹהִים לַמְיַלְּדֹת וַיִּרֶב הָעָם וַיַּעַצְמוּ מְאֹד
# "[EN-AID] And God dealt well with the midwives; and the people multiplied,
# and grew very mighty."
m.step("Exod.1.20")
# ‹וַיֵּיטֶב אֱלֹהִים לַמְיַלְּדֹת› (“and-be-make-well God to-bear-young”) —
# fact holds: and-be-make-well-God-to-bear-young
m.fact("va_yetev_elohim_la_meyaldot")

# -------------------------- Exod.1.21 · HE_MADE_THEM_HOUSES ----------------
# וַיְהִי כִּי־יָרְאוּ הַמְיַלְּדֹת אֶת־הָאֱלֹהִים וַיַּעַשׂ לָהֶם בָּתִּים
# "[EN-AID] And it was, because the midwives feared God, that He made them
# houses."
m.step("Exod.1.21")
# ‹וַיַּעַשׂ לָהֶם בָּתִּים› (“and-make to-them/their house”) — fact holds:
# and-make-to-them-house
m.fact("va_yaas_lahem_batim")

# -------------------------- Exod.1.22 · THE_NILE_DECREE --------------------
# וַיְצַו פַּרְעֹה לְכָל־עַמּוֹ לֵאמֹר כָּל־הַבֵּן הַיִּלּוֹד הַיְאֹרָה
# תַּשְׁלִיכֻהוּ וְכָל־הַבַּת תְּחַיּוּן
# "[EN-AID] And Pharaoh commanded all his people, saying: Every son that is
# born — into the Nile you shall cast him; and every daughter you shall keep
# alive."
m.step("Exod.1.22")
# ‹כָּל־הַבֵּן הַיִּלּוֹד הַיְאֹרָה תַּשְׁלִיכֻהוּ› (“all the-son the-born
# the-Nile-ward throw-out-him/its”) — Pharaoh speaks a demand — LET: all-
# the-son-the-born-the-yeora-tashlikhuhu
m.declare("paro", "LET",
          "kol_ha_ben_ha_yilod_ha_yeora_tashlikhuhu")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['im_ben_hu_va_hamiten_oto', 'kol_ha_ben_ha_yilod_ha_yeora_tashlikhuhu']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['reuven_shimon_levi_vi_yhuda', 'yisashkhar_zevulun_u_venyamin', 'dan_ve_naftali_gad_ve_asher', 'shivim_nefesh_ve_yosef_be_mitzrayim', 'va_yamat_yosef_ve_khol_ha_dor', 'va_timale_ha_aretz_otam', 'rav_ve_atzum_mimenu', 'ken_yirbe_ve_khen_yifrotz', 'va_yaavidu_mitzrayim_be_farekh', 'va_yemarru_et_chayehem', 'shifra_u_fua', 've_lo_asu_kaasher_diber', 'madua_asiten', 'ki_chayot_hena', 'va_yetev_elohim_la_meyaldot', 'va_yaas_lahem_batim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
