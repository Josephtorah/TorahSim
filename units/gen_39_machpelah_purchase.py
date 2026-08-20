#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_39_machpelah_purchase — 23:1-20
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_39_machpelah_purchase.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Sarah's death and the Machpelah purchase (23:1-20)"""
from machine import Machine

m = Machine("gen_39_machpelah_purchase")

# -------------------------- Gen.23.1 · THE_LIFE_COUNT ----------------------
# וַיִּהְיוּ חַיֵּי שָׂרָה מֵאָה שָׁנָה וְעֶשְׂרִים שָׁנָה וְשֶׁבַע שָׁנִים
# שְׁנֵי חַיֵּי שָׂרָה
# "And the life of Sarah was a hundred and seven and twenty years; these
# were the years of the life of Sarah."
m.step("Gen.23.1")
# ‹חַיֵּי שָׂרָה› (“alive Sarah”) — the world gains: sarah
m.install("sarah")
# ‹מֵאָה שָׁנָה וְעֶשְׂרִים שָׁנָה וְשֶׁבַע שָׁנִים› (“hundred years and-
# twenty years and-seven years”) — fact holds: chayei-sarah-hundred-and-
# twenty-and-seven-years
m.fact("chayei_sarah_meah_ve_esrim_ve_sheva_shanim")

# -------------------------- Gen.23.2 · THE_DEATH_AND_THE_MOURNING ----------
# וַתָּמָת שָׂרָה בְּקִרְיַת אַרְבַּע הִוא חֶבְרוֹן בְּאֶרֶץ כְּנָעַן
# וַיָּבֹא אַבְרָהָם לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ
# "And Sarah died in Kiriatharba—the same is Hebron—in the land of Canaan;
# and Abraham came to mourn for Sarah, and to weep for her."
m.step("Gen.23.2")
# ‹וַתָּמָת שָׂרָה› (“and-die Sarah”) — event: die — theme sarah
m.event("die", themes=["sarah"])
# ‹לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ› (“to-tear-the-hair-and-beat-the-b to-
# Sarah and-to-weep-her/its”) — event: mourn-weep — agent Abraham; theme
# sarah
m.event("mourn_weep", agent="avraham", themes=["sarah"])
# ‹וַתָּמָת שָׂרָה … לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ› (“and-die Sarah … to-
# tear-the-hair-and-beat-the-b to-Sarah and-to-weep-her/its”) — fact holds:
# and-die-sarah-in-in-Kirjath-Arba-hi-Hebron; to-me-sepod-to-sarah-and-
# livkotah
m.fact("va_tamat_sarah_be_qiryat_arba_hi_chevron",
       "li_sepod_le_sarah_ve_livkotah")
# ‹הִוא חֶבְרוֹן› (“he/it Hebron”) — reads without prior install (flag, not
# fix): Hebron
m.presupposed("chevron")

# -------------------------- Gen.23.3 · THE_RISING_FROM_THE_DEAD_FACE -------
# וַיָּקָם אַבְרָהָם מֵעַל פְּנֵי מֵתוֹ וַיְדַבֵּר אֶל־בְּנֵי־חֵת לֵאמֹר
# "And Abraham rose up from before his dead, and spoke unto the children of
# Heth, saying:"
m.step("Gen.23.3")
# ‹וַיָּקָם … מֵעַל פְּנֵי מֵתוֹ וַיְדַבֵּר› (“and-arise … from-over face
# die-him/its and-speak”) — event: rise-speak — agent Abraham
m.event("rise_speak", agent="avraham")

# -------------------------- Gen.23.4 · THE_SOJOURNER_ASKS_FOR_A_GRAVE ------
# גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם תְּנוּ לִי אֲחֻזַּת־קֶבֶר עִמָּכֶם
# וְאֶקְבְּרָה מֵתִי מִלְּפָנָי
# "'I am a stranger and a sojourner with you: give me a possession of a
# burying-place with you, that I may bury my dead out of my sight.'"
m.step("Gen.23.4")
# ‹גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם› (“sojourner and-resident-alien with-
# you/your(pl)”) — fact holds: sojourner-and-resident-alien-anokhi-imakhem
m.fact("ger_ve_toshav_anokhi_imakhem")
# ‹תְּנוּ לִי אֲחֻזַּת־קֶבֶר עִמָּכֶם› (“set to-me/my something-seized
# sepulchre with-you/your(pl)”) — Abraham speaks a demand — LET:
# set(something-seized-sepulchre)
m.declare("avraham", "LET",
          "tenu(achuzat_qever)")

# -------------------------- Gen.23.5 · THE_ANSWER_FRAME --------------------
# וַיַּעֲנוּ בְנֵי־חֵת אֶת־אַבְרָהָם לֵאמֹר לוֹ
# "And the children of Heth answered Abraham, saying unto him:"
m.step("Gen.23.5")
# ‹בְנֵי־חֵת› (“son Heth”) — the world gains: sons-of-Heth
m.install("bnei_chet")

# -------------------------- Gen.23.6 · THE_PRINCE_AND_THE_CHOICE_GRAVES ----
# שְׁמָעֵנוּ אֲדֹנִי נְשִׂיא אֱלֹהִים אַתָּה בְּתוֹכֵנוּ בְּמִבְחַר
# קְבָרֵינוּ קְבֹר אֶת־מֵתֶךָ אִישׁ מִמֶּנּוּ אֶת־קִבְרוֹ לֹא־יִכְלֶה
# מִמְּךָ מִקְּבֹר מֵתֶךָ
# "'Hear us, my lord: thou art a mighty prince among us; in the choice of
# our sepulchres bury thy dead; none of us shall withhold from thee his
# sepulchre, but that thou mayest bury thy dead.'"
m.step("Gen.23.6")
# ‹שְׁמָעֵנוּ אֲדֹנִי› (“hear-us/our lord-me/my”) — sons-of-Heth speaks a
# demand — LET: shemaenu(adoni)
m.declare("bnei_chet", "LET",
          "shemaenu(adoni)")
# ‹בְּמִבְחַר קְבָרֵינוּ קְבֹר אֶת־מֵתֶךָ› (“in-select sepulchre-us/our bury
# obj-marker die-you/your”) — sons-of-Heth speaks a demand — LET: bury(in-
# select-qevareinu)
m.declare("bnei_chet", "LET",
          "qevor(be_mivchar_qevareinu)")
# ‹נְשִׂיא אֱלֹהִים אַתָּה בְּתוֹכֵנוּ› (“prince God you in-midst-us/our”) —
# fact holds: prince-God-you-in-tokhenu
m.fact("nesi_elohim_atah_be_tokhenu")

# -------------------------- Gen.23.7 · THE_FIRST_BOW -----------------------
# וַיָּקָם אַבְרָהָם וַיִּשְׁתַּחוּ לְעַם־הָאָרֶץ לִבְנֵי־חֵת
# "And Abraham rose up, and bowed down to the people of the land, even to
# the children of Heth."
m.step("Gen.23.7")
# ‹וַיִּשְׁתַּחוּ לְעַם־הָאָרֶץ› (“and-afflict to-people the-earth”) —
# event: bow — agent Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.8 · THE_ENTREATY_COMPOUND ---------------
# וַיְדַבֵּר אִתָּם לֵאמֹר אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר אֶת־מֵתִי
# מִלְּפָנַי שְׁמָעוּנִי וּפִגְעוּ־לִי בְּעֶפְרוֹן בֶּן־צֹחַר
# "And he spoke with them, saying: 'If it be your mind that I should bury my
# dead out of my sight, hear me, and entreat for me to Ephron the son of
# Zohar,"
m.step("Gen.23.8")
# ‹שְׁמָעוּנִי וּפִגְעוּ־לִי בְּעֶפְרוֹן› (“hear-me/my and-impinge to-me/my
# in-Ephron”) — Abraham speaks a demand — LET: shimuni-and-impinge(in-
# Ephron)
m.declare("avraham", "LET",
          "shimuni_u_figu(be_efron)")
# ‹אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר אֶת־מֵתִי› (“if there-is with living-
# being-you/your(pl) to-inter obj-marker die-me/my”) — fact holds: if-there-
# is-obj-marker-nafshekhem-liqbor-obj-marker-meti
m.fact("im_yesh_et_nafshekhem_liqbor_et_meti")

# -------------------------- Gen.23.9 · THE_FULL_PRICE_CLAUSE ---------------
# וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה אֲשֶׁר־לוֹ אֲשֶׁר בִּקְצֵה שָׂדֵהוּ
# בְּכֶסֶף מָלֵא יִתְּנֶנָּה לִי בְּתוֹכְכֶם לַאֲחֻזַּת־קָבֶר
# "that he may give me the cave of Machpelah, which he hath, which is in the
# end of his field; for the full price let him give it to me in the midst of
# you for a possession of a burying-place.'"
m.step("Gen.23.9")
# ‹וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה … בְּכֶסֶף מָלֵא› (“and-set to-
# me/my obj-marker cavern the-Machpelah … in-silver full”) — fact holds:
# and-set-to-me-obj-marker-cavern-the-makhpelah; in-silver-full-yitnenah-to-
# me
m.fact("ve_yiten_li_et_mearat_ha_makhpelah",
       "be_khesef_male_yitnenah_li")

# -------------------------- Gen.23.10 · THE_ANSWER_FROM_INSIDE_THE_ROOM ----
# וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ בְּנֵי־חֵת וַיַּעַן עֶפְרוֹן הַחִתִּי
# אֶת־אַבְרָהָם בְּאָזְנֵי בְנֵי־חֵת לְכֹל בָּאֵי שַׁעַר־עִירוֹ לֵאמֹר
# "Now Ephron was sitting in the midst of the children of Heth; and Ephron
# the Hittite answered Abraham in the hearing of the children of Heth, even
# of all that went in at the gate of his city, saying:"
m.step("Gen.23.10")
# ‹וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ בְּנֵי־חֵת› (“and-Ephron dwell/sit in-midst
# son Heth”) — the world gains: Ephron
m.install("efron")
# ‹בְּאָזְנֵי בְנֵי־חֵת לְכֹל בָּאֵי שַׁעַר־עִירוֹ› (“in-
# broadness.-i.e.-the-ear son Heth to-all come/bring gate city-him/its”) —
# fact holds: in-oznei-vnei-Heth-to-all-baei-gate-iro
m.fact("be_oznei_vnei_chet_le_khol_baei_shaar_iro")

# -------------------------- Gen.23.11 · THE_GIFT_ROUND ---------------------
# לֹא־אֲדֹנִי שְׁמָעֵנִי הַשָּׂדֶה נָתַתִּי לָךְ וְהַמְּעָרָה אֲשֶׁר־בּוֹ
# לְךָ נְתַתִּיהָ לְעֵינֵי בְנֵי־עַמִּי נְתַתִּיהָ לָּךְ קְבֹר מֵתֶךָ
# "'Nay, my lord, hear me: the field give I thee, and the cave that is
# therein, I give it thee; in the presence of the sons of my people give I
# it thee; bury thy dead.'"
m.step("Gen.23.11")
# ‹לֹא־אֲדֹנִי שְׁמָעֵנִי› (“not lord-me/my hear-me/my”) — Ephron speaks a
# demand — LET: shemaeni(not-adoni)
m.declare("efron", "LET",
          "shemaeni(lo_adoni)")
# ‹קְבֹר מֵתֶךָ› (“bury die-you/your”) — Ephron speaks a demand — LET:
# bury(obj-marker-metekha)
m.declare("efron", "LET",
          "qevor(et_metekha)")
# ‹הַשָּׂדֶה נָתַתִּי לָךְ … נְתַתִּיהָ› (“the-field set to-you/your … set-
# her/its”) — fact holds: the-field-set-to-you-netatiha
m.fact("ha_sadeh_natati_lakh_netatiha")

# -------------------------- Gen.23.12 · THE_SECOND_BOW ---------------------
# וַיִּשְׁתַּחוּ אַבְרָהָם לִפְנֵי עַם הָאָרֶץ
# "And Abraham bowed down before the people of the land."
m.step("Gen.23.12")
# ‹וַיִּשְׁתַּחוּ … לִפְנֵי עַם הָאָרֶץ› (“and-afflict … to-face people the-
# earth”) — event: bow — agent Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.13 · THE_WISH_AND_THE_TAKE_DEMAND -------
# וַיְדַבֵּר אֶל־עֶפְרוֹן בְּאָזְנֵי עַם־הָאָרֶץ לֵאמֹר אַךְ אִם־אַתָּה לוּ
# שְׁמָעֵנִי נָתַתִּי כֶּסֶף הַשָּׂדֶה קַח מִמֶּנִּי וְאֶקְבְּרָה אֶת־מֵתִי
# שָׁמָּה
# "And he spoke unto Ephron in the hearing of the people of the land,
# saying: 'But if thou wilt, I pray thee, hear me: I will give the price of
# the field; take it of me, and I will bury my dead there.'"
m.step("Gen.23.13")
# ‹אַךְ אִם־אַתָּה לוּ שְׁמָעֵנִי נָתַתִּי כֶּסֶף הַשָּׂדֶה› (“indeed if you
# conditional-particle hear-me/my set silver the-field”) — fact holds:
# indeed-if-you-conditional-particle-shemaeni; set-silver-the-field
m.fact("akh_im_atah_lu_shemaeni",
       "natati_kesef_ha_sadeh")
# ‹קַח מִמֶּנִּי› (“take from-me/my”) — Abraham speaks a demand — LET:
# take(silver-the-field)
m.declare("avraham", "LET",
          "qach(kesef_ha_sadeh)")

# -------------------------- Gen.23.14 · THE_SECOND_ANSWER_FRAME ------------
# וַיַּעַן עֶפְרוֹן אֶת־אַבְרָהָם לֵאמֹר לוֹ
# "And Ephron answered Abraham, saying unto him:"
m.step("Gen.23.14")
# ‹וַיַּעַן עֶפְרוֹן› (“and-eye Ephron”) — event: answer — agent Ephron
m.event("answer", agent="efron")

# -------------------------- Gen.23.15 · THE_PRICE_ROUND --------------------
# אֲדֹנִי שְׁמָעֵנִי אֶרֶץ אַרְבַּע מֵאֹת שֶׁקֶל־כֶּסֶף בֵּינִי וּבֵינְךָ
# מַה־הִוא וְאֶת־מֵתְךָ קְבֹר
# "'My lord, hearken unto me: a piece of land worth four hundred shekels of
# silver, what is that betwixt me and thee? bury therefore thy dead.'"
m.step("Gen.23.15")
# ‹אֲדֹנִי שְׁמָעֵנִי› (“lord-me/my hear-me/my”) — Ephron speaks a demand —
# LET: shemaeni(adoni)
m.declare("efron", "LET",
          "shemaeni(adoni)")
# ‹אֶרֶץ אַרְבַּע מֵאֹת שֶׁקֶל־כֶּסֶף … וְאֶת־מֵתְךָ קְבֹר› (“earth four
# hundred weight silver … and-obj-marker die-you/your bury”) — fact holds:
# earth-Kirjath-Arba-hundred-weight-silver-beini-and-veinkha; and-obj-
# marker-metkha-bury-resound
m.fact("eretz_arba_meot_sheqel_kesef_beini_u_veinkha",
       "ve_et_metkha_qevor_resound")

# -------------------------- Gen.23.16 · CYCLE_A_THE_HEARING_AND_THE_WEIGHING -
# וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן
# אֶת־הַכֶּסֶף אֲשֶׁר דִּבֶּר בְּאָזְנֵי בְנֵי־חֵת אַרְבַּע מֵאוֹת שֶׁקֶל
# כֶּסֶף עֹבֵר לַסֹּחֵר
# "And Abraham hearkened unto Ephron; and Abraham weighed to Ephron the
# silver, which he had named in the hearing of the children of Heth, four
# hundred shekels of silver, current money with the merchant."
m.step("Gen.23.16")
# ‹וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן› (“and-hear Abraham to Ephron”) —
# demand settled (popped from the queue): shemaeni(adoni)
m.result("shemaeni(adoni)", tmark="t1")
# ‹וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן אֶת־הַכֶּסֶף› (“and-suspend Abraham to-
# Ephron obj-marker the-silver”) — event: weigh-silver — agent Abraham
m.event("weigh_silver", agent="avraham")
# ‹אַרְבַּע מֵאוֹת שֶׁקֶל כֶּסֶף עֹבֵר לַסֹּחֵר› (“four hundred weight
# silver pass-over to-travel-round”) — fact holds: and-suspend-Kirjath-Arba-
# hundred-weight-pass-over-to-travel-round
m.fact("va_yishqol_arba_meot_sheqel_over_la_socher")

# -------------------------- Gen.23.17 · THE_FIELD_ARISES -------------------
# וַיָּקָם שְׂדֵה עֶפְרוֹן אֲשֶׁר בַּמַּכְפֵּלָה אֲשֶׁר לִפְנֵי מַמְרֵא
# הַשָּׂדֶה וְהַמְּעָרָה אֲשֶׁר־בּוֹ וְכָל־הָעֵץ אֲשֶׁר בַּשָּׂדֶה אֲשֶׁר
# בְּכָל־גְּבֻלוֹ סָבִיב
# "So the field of Ephron, which was in Machpelah, which was before Mamre,
# the field, and the cave which was therein, and all the trees that were in
# the field, that were in all the border thereof round about, were made
# sure"
m.step("Gen.23.17")
# ‹וַיָּקָם שְׂדֵה עֶפְרוֹן … וְכָל־הָעֵץ … סָבִיב› (“and-arise field Ephron
# … and-all the-tree … circle”) — fact holds: and-arise-sdeh-Ephron-in-the-
# makhpelah; the-field-and-the-mearah-and-all-the-tree-circle
m.fact("va_yaqam_sdeh_efron_ba_makhpelah",
       "ha_sadeh_ve_ha_mearah_ve_khol_ha_etz_saviv")

# -------------------------- Gen.23.18 · THE_PURCHASE_BEFORE_THE_GATE -------
# לְאַבְרָהָם לְמִקְנָה לְעֵינֵי בְנֵי־חֵת בְּכֹל בָּאֵי שַׁעַר־עִירוֹ
# "unto Abraham for a possession in the presence of the children of Heth,
# before all that went in at the gate of his city."
m.step("Gen.23.18")
# ‹לְאַבְרָהָם לְמִקְנָה› (“to-Abraham to-buying”) — fact holds: to-Abraham-
# to-miqnah-to-eyes-of-vnei-Heth
m.fact("le_avraham_le_miqnah_le_einei_vnei_chet")

# -------------------------- Gen.23.19 · CYCLE_B_THE_BURIAL -----------------
# וְאַחֲרֵי־כֵן קָבַר אַבְרָהָם אֶת־שָׂרָה אִשְׁתּוֹ אֶל־מְעָרַת שְׂדֵה
# הַמַּכְפֵּלָה עַל־פְּנֵי מַמְרֵא הִוא חֶבְרוֹן בְּאֶרֶץ כְּנָעַן
# "And after this, Abraham buried Sarah his wife in the cave of the field of
# Machpelah before Mamre—the same is Hebron—in the land of Canaan."
m.step("Gen.23.19")
# ‹קָבַר אַבְרָהָם אֶת־שָׂרָה אִשְׁתּוֹ› (“bury Abraham obj-marker Sarah
# woman-him/its”) — demand settled (popped from the queue): bury(obj-marker-
# metekha)
m.result("qevor(et_metekha)", tmark="t2")
# ‹עַל־פְּנֵי מַמְרֵא הִוא חֶבְרוֹן› (“over face Mamre he/it Hebron”) —
# reads without prior install (flag, not fix): Mamre
m.presupposed("mamre")

# -------------------------- Gen.23.20 · THE_CONVEYANCE_CODA ----------------
# וַיָּקָם הַשָּׂדֶה וְהַמְּעָרָה אֲשֶׁר־בּוֹ לְאַבְרָהָם לַאֲחֻזַּת־קָבֶר
# מֵאֵת בְּנֵי־חֵת
# "And the field, and the cave that is therein, were made sure unto Abraham
# for a possession of a burying-place by the children of Heth."
m.step("Gen.23.20")
# ‹וַיָּקָם הַשָּׂדֶה … לַאֲחֻזַּת־קָבֶר› (“and-arise the-field … to-
# something-seized sepulchre”) — fact holds: and-arise-the-field-to-
# something-seized-sepulchre-from-obj-marker-sons-of-Heth
m.fact("va_yaqam_ha_sadeh_la_achuzat_qaver_me_et_bnei_chet")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'bnei_chet', 'efron', 'sarah'}
    assert m.presupposed_set() == {'chevron', 'mamre'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tenu(achuzat_qever)', 'shemaenu(adoni)', 'qevor(be_mivchar_qevareinu)', 'shimuni_u_figu(be_efron)', 'shemaeni(lo_adoni)', 'qach(kesef_ha_sadeh)']
    assert len(m.SPECS["log"]) == 8
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['chayei_sarah_meah_ve_esrim_ve_sheva_shanim', 'va_tamat_sarah_be_qiryat_arba_hi_chevron', 'li_sepod_le_sarah_ve_livkotah', 'ger_ve_toshav_anokhi_imakhem', 'nesi_elohim_atah_be_tokhenu', 'im_yesh_et_nafshekhem_liqbor_et_meti', 've_yiten_li_et_mearat_ha_makhpelah', 'be_khesef_male_yitnenah_li', 'be_oznei_vnei_chet_le_khol_baei_shaar_iro', 'ha_sadeh_natati_lakh_netatiha', 'akh_im_atah_lu_shemaeni', 'natati_kesef_ha_sadeh', 'eretz_arba_meot_sheqel_kesef_beini_u_veinkha', 've_et_metkha_qevor_resound', 'va_yishqol_arba_meot_sheqel_over_la_socher', 'va_yaqam_sdeh_efron_ba_makhpelah', 'ha_sadeh_ve_ha_mearah_ve_khol_ha_etz_saviv', 'le_avraham_le_miqnah_le_einei_vnei_chet', 'va_yaqam_ha_sadeh_la_achuzat_qaver_me_et_bnei_chet'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 17
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
