#!/usr/bin/env python3
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
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי› (“and-these name son”)
# ‹יִשְׂרָאֵל הַבָּאִים מִצְרָיְמָה› (“Israel the-come/bring Egypt-ward”)
# ‹אֵת יַעֲקֹב אִישׁ› (“with Jacob man”)
# ‹וּבֵיתוֹ בָּאוּ› (“and-house-him/its come/bring”)
# "[EN-AID] And these are the names of the sons of Israel who came to Egypt;
# with Jacob, each man and his household, they came."
m.step("Exod.1.1")
# ‹וְאֵלֶּה שְׁמוֹת בְּנֵי› (“and-these name son”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — section name-son-Israel: son-lea, son-rachel, son-the-shefachot
m.section("shemot_bene_yisrael", "bene_lea", "ben_rachel", "bene_ha_shefachot")

# -------------------------- Exod.1.2 · LEAHS_FOUR --------------------------
# ‹רְאוּבֵן שִׁמְעוֹן לֵוִי› (“Reuben Simeon Levi”)
# ‹וִיהוּדָה› (“and-Judah”)
# "[EN-AID] Reuben, Simeon, Levi, and Judah;"
m.step("Exod.1.2")
# ‹רְאוּבֵן שִׁמְעוֹן לֵוִי› (“Reuben Simeon Levi”)
# ‹וִיהוּדָה› (“and-Judah”)
# — fact holds: Reuben-Simeon-Levi-vi-yhuda
m.fact("reuven_shimon_levi_vi_yhuda")

# -------------------------- Exod.1.3 · LEAHS_LAST_AND_RACHELS --------------
# ‹יִשָּׂשכָר זְבוּלֻן וּבְנְיָמִן› (“Issachar Zebulun and-Benjamin”)
# "[EN-AID] Issachar, Zebulun, and Benjamin;"
m.step("Exod.1.3")
# ‹יִשָּׂשכָר זְבוּלֻן וּבְנְיָמִן› (“Issachar Zebulun and-Benjamin”)
# — fact holds: Issachar-Zebulun-and-Benjamin
m.fact("yisashkhar_zevulun_u_venyamin")

# -------------------------- Exod.1.4 · THE_HANDMAIDS_FOUR ------------------
# ‹דָּן וְנַפְתָּלִי גָּד› (“Daniel and-Naphtali Gad”)
# ‹וְאָשֵׁר› (“and-Asher”)
# "[EN-AID] Dan, and Naphtali; Gad, and Asher."
m.step("Exod.1.4")
# ‹דָּן וְנַפְתָּלִי גָּד› (“Daniel and-Naphtali Gad”)
# ‹וְאָשֵׁר› (“and-Asher”)
# — fact holds: Daniel-and-Naphtali-Gad-and-Asher
m.fact("dan_ve_naftali_gad_ve_asher")

# -------------------------- Exod.1.5 · SEVENTY_SOULS_AND_JOSEPH ------------
# ‹וַיְהִי כָּל־נֶפֶשׁ יֹצְאֵי› (“and-be all living-being bring-forth”)
# ‹יֶרֶךְ־יַעֲקֹב שִׁבְעִים נָפֶשׁ› (“thigh Jacob seventy living-being”)
# ‹וְיוֹסֵף הָיָה בְמִצְרָיִם› (“and-Joseph be in-Egypt”)
# "[EN-AID] And all the souls that came out of the loins of Jacob were
# seventy souls; and Joseph was in Egypt."
m.step("Exod.1.5")
# ‹יַעֲקֹב שִׁבְעִים נָפֶשׁ› (“Jacob seventy living-being”)
# ‹וְיוֹסֵף הָיָה בְמִצְרָיִם› (“and-Joseph be in-Egypt”)
# — fact holds: seventy-living-being-and-Joseph-in-Egypt
m.fact("shivim_nefesh_ve_yosef_be_mitzrayim")

# -------------------------- Exod.1.6 · THE_DEATH_RETOLD --------------------
# ‹וַיָּמָת יוֹסֵף וְכָל־אֶחָיו› (“and-die Joseph and-all brother-him/its”)
# ‹וְכֹל הַדּוֹר הַהוּא› (“and-all the-generation that”)
# "[EN-AID] And Joseph died, and all his brothers, and all that generation."
m.step("Exod.1.6")
# ‹וַיָּמָת יוֹסֵף› (“and-die Joseph”)
# — fact holds: and-die-Joseph-and-all-the-generation
m.fact("va_yamat_yosef_ve_khol_ha_dor")

# -------------------------- Exod.1.7 · THE_SIX_INCREASE_WORDS --------------
# ‹וּבְנֵי יִשְׂרָאֵל פָּרוּ› (“and-son Israel be-fruitful”)
# ‹וַיִּשְׁרְצוּ וַיִּרְבּוּ וַיַּעַצְמוּ› (“and-swarm and-multiply and-
# bind-fast”)
# ‹בִּמְאֹד מְאֹד וַתִּמָּלֵא› (“in-very very and-fill”)
# ‹הָאָרֶץ אֹתָם› (“the-earth obj-marker-them/their”)
# "[EN-AID] And the sons of Israel were fruitful, and swarmed, and
# multiplied, and grew mighty — exceedingly, exceedingly; and the land was
# filled with them."
m.step("Exod.1.7")
# ‹פָּרוּ וַיִּשְׁרְצוּ וַיִּרְבּוּ› (“be-fruitful and-swarm and-multiply”)
# ‹וַיַּעַצְמוּ בִּמְאֹד מְאֹד› (“and-bind-fast in-very very”)
# — fact holds: and-fill-the-earth-otam
m.fact("va_timale_ha_aretz_otam")

# -------------------------- Exod.1.8 · A_KING_WHO_KNEW_NOT -----------------
# ‹וַיָּקָם מֶלֶךְ־חָדָשׁ עַל־מִצְרָיִם› (“and-arise king new over Egypt”)
# ‹אֲשֶׁר לֹא־יָדַע אֶת־יוֹסֵף› (“which not know obj-marker Joseph”)
# "[EN-AID] And there arose a new king over Egypt, who knew not Joseph."
m.step("Exod.1.8")
# ‹וַיָּקָם מֶלֶךְ־חָדָשׁ עַל־מִצְרָיִם› (“and-arise king new over Egypt”)
# — event: qam — agent king-new
m.event("qam", agent="melekh_chadash")

# -------------------------- Exod.1.9 · BEHOLD_THE_PEOPLE -------------------
# ‹וַיֹּאמֶר אֶל־עַמּוֹ הִנֵּה› (“and-say to people-him/its behold”)
# ‹עַם בְּנֵי יִשְׂרָאֵל› (“people son Israel”)
# ‹רַב וְעָצוּם מִמֶּנּוּ› (“many/great and-powerful from-us/our”)
# "[EN-AID] And he said to his people: Behold, the people of the sons of
# Israel are more numerous and mightier than we."
m.step("Exod.1.9")
# ‹רַב וְעָצוּם מִמֶּנּוּ› (“many/great and-powerful from-us/our”)
# — fact holds: many/great-and-powerful-from-it
m.fact("rav_ve_atzum_mimenu")

# -------------------------- Exod.1.10 · COME_LET_US_OUTWIT -----------------
# ‹הָבָה נִתְחַכְּמָה לוֹ› (“give-ward be-wise to-him/its”)
# ‹פֶּן־יִרְבֶּה וְהָיָה כִּי־תִקְרֶאנָה› (“lest multiply and-be that
# encounter”)
# ‹מִלְחָמָה וְנוֹסַף גַּם־הוּא› (“battle and-add also he/it”)
# ‹עַל־שֹׂנְאֵינוּ וְנִלְחַם־בָּנוּ וְעָלָה› (“over hate-us/our and-feed-on
# in-us/our and-go-up”)
# ‹מִן־הָאָרֶץ› (“from the-earth”)
# "[EN-AID] Come, let us deal wisely with him, lest he multiply, and it come
# to pass, when war befalls, that he too be added to our enemies, and fight
# against us, and go up from the land."
m.step("Exod.1.10")
# ‹הָבָה נִתְחַכְּמָה לוֹ› (“give-ward be-wise to-him/its”)
# — king-new speaks a demand — LET: hava-be-wise-not
m.declare("melekh_chadash", "LET",
          "hava_nitchakma_lo")

# -------------------------- Exod.1.11 · TASKMASTERS_SET --------------------
# ‹וַיָּשִׂימוּ עָלָיו שָׂרֵי› (“and-put/set over-him/its officer”)
# ‹מִסִּים לְמַעַן עַנֹּתוֹ› (“burden so-that afflict-literally-him/its”)
# ‹בְּסִבְלֹתָם וַיִּבֶן עָרֵי› (“in-porterage-them/their and-build city”)
# ‹מִסְכְּנוֹת לְפַרְעֹה אֶת־פִּתֹם› (“magazine to-Pharaoh obj-marker
# Pithom”)
# ‹וְאֶת־רַעַמְסֵס› (“and-obj-marker Raamses”)
# "[EN-AID] And they set over him taskmasters of levies, in order to afflict
# him with their burdens; and he built store-cities for Pharaoh: Pitom, and
# Raamses."
m.step("Exod.1.11")
# ‹וַיָּשִׂימוּ עָלָיו שָׂרֵי› (“and-put/set over-him/its officer”)
# ‹מִסִּים לְמַעַן עַנֹּתוֹ› (“burden so-that afflict-literally-him/its”)
# ‹בְּסִבְלֹתָם› (“in-porterage-them/their”)
# — demand settled (popped from the queue): hava-be-wise-not
m.result("hava_nitchakma_lo", tmark="t1")

# -------------------------- Exod.1.12 · THE_MORE_AFFLICTED_THE_MORE --------
# ‹וְכַאֲשֶׁר יְעַנּוּ אֹתוֹ› (“and-like-as/which afflict-literally obj-
# marker-him/its”)
# ‹כֵּן יִרְבֶּה וְכֵן› (“so multiply and-so”)
# ‹יִפְרֹץ וַיָּקֻצוּ מִפְּנֵי› (“break-out and-be-disgusted from-face”)
# ‹בְּנֵי יִשְׂרָאֵל› (“son Israel”)
# "[EN-AID] And as they afflicted him, so he multiplied and so he spread;
# and they dreaded because of the sons of Israel."
m.step("Exod.1.12")
# ‹כֵּן יִרְבֶּה וְכֵן› (“so multiply and-so”)
# ‹יִפְרֹץ› (“break-out”)
# — fact holds: so-multiply-and-so-break-out
m.fact("ken_yirbe_ve_khen_yifrotz")

# -------------------------- Exod.1.13 · WITH_CRUSHING_SERVICE --------------
# ‹וַיַּעֲבִדוּ מִצְרַיִם אֶת־בְּנֵי› (“and-work/serve Egyptian obj-marker
# son”)
# ‹יִשְׂרָאֵל בְּפָרֶךְ› (“Israel in-fracture”)
# "[EN-AID] And Egypt made the sons of Israel serve with crushing service."
m.step("Exod.1.13")
# ‹וַיַּעֲבִדוּ מִצְרַיִם אֶת־בְּנֵי› (“and-work/serve Egyptian obj-marker
# son”)
# ‹יִשְׂרָאֵל בְּפָרֶךְ› (“Israel in-fracture”)
# — fact holds: and-work/serve-Egypt-in-fracture
m.fact("va_yaavidu_mitzrayim_be_farekh")

# -------------------------- Exod.1.14 · THE_FOUR_AFFLICTIONS ---------------
# ‹וַיְמָרְרוּ אֶת־חַיֵּיהֶם בַּעֲבֹדָה› (“and-be-bitter obj-marker alive-
# them/their in-service/work”)
# ‹קָשָׁה בְּחֹמֶר וּבִלְבֵנִים› (“severe in-bubbling-up and-in-brick”)
# ‹וּבְכָל־עֲבֹדָה בַּשָּׂדֶה אֵת› (“and-in-all service/work in-field obj-
# marker”)
# ‹כָּל־עֲבֹדָתָם אֲשֶׁר־עָבְדוּ בָהֶם› (“all service/work-them/their which
# work/serve in-them/their”)
# ‹בְּפָרֶךְ› (“in-fracture”)
# "[EN-AID] And they made their lives bitter with hard service — with mortar
# and with bricks, and with all service in the field; all their service in
# which they made them serve with crushing service."
m.step("Exod.1.14")
# ‹וַיְמָרְרוּ אֶת־חַיֵּיהֶם בַּעֲבֹדָה› (“and-be-bitter obj-marker alive-
# them/their in-service/work”)
# ‹קָשָׁה› (“severe”)
# — fact holds: and-be-bitter-with-chayehem
m.fact("va_yemarru_et_chayehem")
# witness-tier presupposed read: maror_reason on embittered_verb — read, not
# installed
m.witness_read("embittered_verb", "maror_reason",
                cites=["Mishnah Pesachim 10:5"])

# -------------------------- Exod.1.15 · SHIFRA_AND_PUA ---------------------
# ‹וַיֹּאמֶר מֶלֶךְ מִצְרַיִם› (“and-say king Egypt”)
# ‹לַמְיַלְּדֹת הָעִבְרִיֹּת אֲשֶׁר› (“to-bear-young the-Hebrew which”)
# ‹שֵׁם הָאַחַת שִׁפְרָה› (“name the-one Shiphrah”)
# ‹וְשֵׁם הַשֵּׁנִית פּוּעָה› (“and-name the-second Puah”)
# "[EN-AID] And the king of Egypt said to the midwives of the Hebrews, of
# whom the name of the one was Shifra, and the name of the second Pua:"
m.step("Exod.1.15")
# ‹הָאַחַת שִׁפְרָה וְשֵׁם› (“the-one Shiphrah and-name”)
# ‹הַשֵּׁנִית פּוּעָה› (“the-second Puah”)
# — fact holds: Shiphrah-and-fua
m.fact("shifra_u_fua")

# -------------------------- Exod.1.16 · THE_KILL_ORDER ---------------------
# ‹וַיֹּאמֶר בְּיַלֶּדְכֶן אֶת־הָעִבְרִיּוֹת› (“and-say in-bear-young-ward
# obj-marker the-Hebrew”)
# ‹וּרְאִיתֶן עַל־הָאָבְנָיִם אִם־בֵּן› (“and-see over the-pair-of-stones if
# son”)
# ‹הוּא וַהֲמִתֶּן אֹתוֹ› (“he/it and-die obj-marker-him/its”)
# ‹וְאִם־בַּת הִיא וָחָיָה› (“and-if daughter he/it and-live”)
# "[EN-AID] And he said: When you deliver the Hebrew women, and you see upon
# the birthstool: if it is a son, you shall kill him; and if it is a
# daughter, she shall live."
m.step("Exod.1.16")
# ‹אִם־בֵּן הוּא וַהֲמִתֶּן› (“if son he/it and-die”)
# ‹אֹתוֹ› (“obj-marker-him/its”)
# — king-Egypt speaks a demand — LET: if-son-that-and-die-it
m.declare("melekh_mitzrayim", "LET",
          "im_ben_hu_va_hamiten_oto")

# -------------------------- Exod.1.17 · THEY_DID_NOT_DO --------------------
# ‹וַתִּירֶאןָ הַמְיַלְּדֹת אֶת־הָאֱלֹהִים› (“and-fear the-bear-young obj-
# marker the-God”)
# ‹וְלֹא עָשׂוּ כַּאֲשֶׁר› (“and-not make like-as/which”)
# ‹דִּבֶּר אֲלֵיהֶן מֶלֶךְ› (“speak to-them/their king”)
# ‹מִצְרָיִם וַתְּחַיֶּיןָ אֶת־הַיְלָדִים› (“Egypt and-live obj-marker the-
# child”)
# "[EN-AID] And the midwives feared God, and did not do as the king of Egypt
# spoke to them; and they kept the children alive."
m.step("Exod.1.17")
# ‹וְלֹא עָשׂוּ כַּאֲשֶׁר› (“and-not make like-as/which”)
# ‹דִּבֶּר אֲלֵיהֶן מֶלֶךְ› (“speak to-them/their king”)
# ‹מִצְרָיִם› (“Egypt”)
# — fact holds: and-not-make-kaasher-speak
m.fact("ve_lo_asu_kaasher_diber")

# -------------------------- Exod.1.18 · WHY_HAVE_YOU_DONE ------------------
# ‹וַיִּקְרָא מֶלֶךְ־מִצְרַיִם לַמְיַלְּדֹת› (“and-call king Egypt to-bear-
# young”)
# ‹וַיֹּאמֶר לָהֶן מַדּוּעַ› (“and-say to-them/their what-known?”)
# ‹עֲשִׂיתֶן הַדָּבָר הַזֶּה› (“make the-word/thing the-this”)
# ‹וַתְּחַיֶּיןָ אֶת־הַיְלָדִים› (“and-live obj-marker the-child”)
# "[EN-AID] And the king of Egypt called the midwives, and said to them: Why
# have you done this thing, and kept the children alive?"
m.step("Exod.1.18")
# ‹מַדּוּעַ עֲשִׂיתֶן הַדָּבָר› (“what-known? make the-word/thing”)
# ‹הַזֶּה› (“the-this”)
# — fact holds: what-known?-make
m.fact("madua_asiten")

# -------------------------- Exod.1.19 · FOR_THEY_ARE_LIVELY ----------------
# ‹וַתֹּאמַרְןָ הַמְיַלְּדֹת אֶל־פַּרְעֹה› (“and-say the-bear-young to
# Pharaoh”)
# ‹כִּי לֹא כַנָּשִׁים› (“that not like-woman”)
# ‹הַמִּצְרִיֹּת הָעִבְרִיֹּת כִּי־חָיוֹת› (“the-Egyptian the-Hebrew that
# vigorous”)
# ‹הֵנָּה בְּטֶרֶם תָּבוֹא› (“themselves in-non-occurrence come/bring”)
# ‹אֲלֵהֶן הַמְיַלֶּדֶת וְיָלָדוּ› (“to-them/their the-bear-young and-bear-
# young”)
# "[EN-AID] And the midwives said to Pharaoh: Because the Hebrew women are
# not as the Egyptian women, for they are lively; before the midwife comes
# to them, they have given birth."
m.step("Exod.1.19")
# ‹כִּי־חָיוֹת הֵנָּה› (“that vigorous themselves”)
# — fact holds: that-vigorous-themselves
m.fact("ki_chayot_hena")

# -------------------------- Exod.1.20 · GOD_DEALT_WELL ---------------------
# ‹וַיֵּיטֶב אֱלֹהִים לַמְיַלְּדֹת› (“and-be-make-well God to-bear-young”)
# ‹וַיִּרֶב הָעָם וַיַּעַצְמוּ› (“and-multiply the-people and-bind-fast”)
# ‹מְאֹד› (“very”)
# "[EN-AID] And God dealt well with the midwives; and the people multiplied,
# and grew very mighty."
m.step("Exod.1.20")
# ‹וַיֵּיטֶב אֱלֹהִים לַמְיַלְּדֹת› (“and-be-make-well God to-bear-young”)
# — fact holds: and-be-make-well-God-to-bear-young
m.fact("va_yetev_elohim_la_meyaldot")

# -------------------------- Exod.1.21 · HE_MADE_THEM_HOUSES ----------------
# ‹וַיְהִי כִּי־יָרְאוּ הַמְיַלְּדֹת› (“and-be that fear the-bear-young”)
# ‹אֶת־הָאֱלֹהִים וַיַּעַשׂ לָהֶם› (“obj-marker the-God and-make to-
# them/their”)
# ‹בָּתִּים› (“house”)
# "[EN-AID] And it was, because the midwives feared God, that He made them
# houses."
m.step("Exod.1.21")
# ‹וַיַּעַשׂ לָהֶם בָּתִּים› (“and-make to-them/their house”)
# — fact holds: and-make-to-them-house
m.fact("va_yaas_lahem_batim")

# -------------------------- Exod.1.22 · THE_NILE_DECREE --------------------
# ‹וַיְצַו פַּרְעֹה לְכָל־עַמּוֹ› (“and-command Pharaoh to-all people-
# him/its”)
# ‹לֵאמֹר כָּל־הַבֵּן הַיִּלּוֹד› (“to-say all the-son the-born”)
# ‹הַיְאֹרָה תַּשְׁלִיכֻהוּ וְכָל־הַבַּת› (“the-Nile-ward throw-out-him/its
# and-all the-daughter”)
# ‹תְּחַיּוּן› (“live-ward”)
# "[EN-AID] And Pharaoh commanded all his people, saying: Every son that is
# born — into the Nile you shall cast him; and every daughter you shall keep
# alive."
m.step("Exod.1.22")
# ‹כָּל־הַבֵּן הַיִּלּוֹד הַיְאֹרָה› (“all the-son the-born the-Nile-ward”)
# ‹תַּשְׁלִיכֻהוּ› (“throw-out-him/its”)
# — Pharaoh speaks a demand — LET: all-the-son-the-born-the-yeora-
# tashlikhuhu
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('embittered_verb', 'maror_reason')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Pesachim 10:5']
    assert all('maror_reason' not in f for f in m.WORLD["facts"])
    assert 'embittered_verb' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
