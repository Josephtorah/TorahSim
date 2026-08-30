#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_32_hagar_angel — 16:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_32_hagar_angel.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Hagar: the maid given, the flight, the angel, the names (16:1-16)"""
from machine import Machine

m = Machine("gen_32_hagar_angel")

# -------------------------- Gen.16.1 · THE_BARREN_WIFE_AND_THE_MAID --------
# וְשָׂרַי אֵשֶׁת אַבְרָם לֹא יָלְדָה לוֹ וְלָהּ שִׁפְחָה מִצְרִית וּשְׁמָהּ
# הָגָר
# "Now Sarai Abram's wife bore him no children; and she had a handmaid, an
# Egyptian, whose name was Hagar."
m.step("Gen.16.1")
# ‹לֹא יָלְדָה לוֹ וְלָהּ שִׁפְחָה מִצְרִית וּשְׁמָהּ הָגָר› (“not bear-
# young to-him/its and-to-her/its female-slave Egyptian and-name-her/its
# Hagar”) — fact holds: Sarai-not-yaldah-not; and-lah-shifchah-Egyptian-and-
# shemah-Hagar
m.fact("saray_lo_yaldah_lo",
       "ve_lah_shifchah_mitzrit_u_shemah_hagar")

# -------------------------- Gen.16.2 · THE_INITIATIVE_AND_THE_LISTENING ----
# וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם הִנֵּה־נָא עֲצָרַנִי יְהוָה מִלֶּדֶת בֹּא־נָא
# אֶל־שִׁפְחָתִי אוּלַי אִבָּנֶה מִמֶּנָּה וַיִּשְׁמַע אַבְרָם לְקוֹל שָׂרָי
# "And Sarai said unto Abram: 'Behold now, the LORD hath restrained me from
# bearing; go in, I pray thee, unto my handmaid; it may be that I shall be
# builded up through her.' And Abram hearkened to the voice of Sarai."
m.step("Gen.16.2")
# ‹וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם› (“and-say Sarai to Abram”) — event: say —
# agent Sarai
m.event("say", agent="saray")
# ‹בֹּא־נָא אֶל־שִׁפְחָתִי› (“come/bring please to female-slave-me/my”) —
# Sarai speaks a demand — LET: come/bring(Abram, to-shifchati)
m.declare("saray", "LET",
          "bo(avram, el_shifchati)")
# ‹עֲצָרַנִי יְהוָה מִלֶּדֶת … אוּלַי אִבָּנֶה מִמֶּנָּה› (“close-me/my YHWH
# from-bear-young … if-not build from-her/its”) — fact holds: atzarani-the-
# LORD-from-bear-young; if-not-ibaneh-mimenah
m.fact("atzarani_YHWH_mi_ledet",
       "ulay_ibaneh_mimenah")
# ‹וַיִּשְׁמַע אַבְרָם לְקוֹל שָׂרָי› (“and-hear Abram to-voice/sound
# Sarai”) — event: hear — agent Abram; theme voice/sound-Sarai
m.event("hear", agent="avram", themes=["qol_saray"])

# -------------------------- Gen.16.3 · THE_TAKE_AND_THE_GIVE ---------------
# וַתִּקַּח שָׂרַי אֵשֶׁת־אַבְרָם אֶת־הָגָר הַמִּצְרִית שִׁפְחָתָהּ מִקֵּץ
# עֶשֶׂר שָׁנִים לְשֶׁבֶת אַבְרָם בְּאֶרֶץ כְּנָעַן וַתִּתֵּן אֹתָהּ
# לְאַבְרָם אִישָׁהּ לוֹ לְאִשָּׁה
# "And Sarai Abram's wife took Hagar the Egyptian, her handmaid, after Abram
# had dwelt ten years in the land of Canaan, and gave her to Abram her
# husband to be his wife."
m.step("Gen.16.3")
# ‹וַתִּקַּח שָׂרַי … אֶת־הָגָר› (“and-take Sarai … obj-marker Hagar”) —
# event: take — agent Sarai; theme Hagar
m.event("take", agent="saray", themes=["hagar"])
# ‹וַתִּתֵּן אֹתָהּ לְאַבְרָם אִישָׁהּ לוֹ לְאִשָּׁה› (“and-set obj-marker-
# her/its to-Abram man-her/its to-him/its to-woman”) — event: give — agent
# Sarai; theme Hagar
m.event("give", agent="saray", themes=["hagar"])
# ‹מִקֵּץ עֶשֶׂר שָׁנִים לְשֶׁבֶת אַבְרָם בְּאֶרֶץ כְּנָעַן› (“from-end ten
# years to-dwell/sit Abram in-earth Canaan”) — fact holds: from-end-ten-
# years-to-dwell/sit-Abram-in-earth-Canaan
m.fact("mi_qetz_eser_shanim_le_shevet_avram_be_eretz_kenaan")
# witness-tier presupposed read: binding_rule_on_a_self_graded_hint on
# ten_years_clause — read, not installed
m.witness_read("ten_years_clause", "binding_rule_on_a_self_graded_hint",
                cites=["Tosefta Yevamot 8:4", "Yevamot 64a:5", "Bereshit Rabbah 45:3", "Jerusalem Talmud Yevamot 6:6:3", "Mishnah Yevamot 6:6"])

# -------------------------- Gen.16.4 · THE_COMPLIANCE_AND_THE_CONTEMPT -----
# וַיָּבֹא אֶל־הָגָר וַתַּהַר וַתֵּרֶא כִּי הָרָתָה וַתֵּקַל גְּבִרְתָּהּ
# בְּעֵינֶיהָ
# "And he went in unto Hagar, and she conceived; and when she saw that she
# had conceived, her mistress was despised in her eyes."
m.step("Gen.16.4")
# ‹וַיָּבֹא אֶל־הָגָר› (“and-come/bring to Hagar”) — event: come — agent
# Abram
m.event("come", agent="avram")
# ‹וַיָּבֹא אֶל־הָגָר› (“and-come/bring to Hagar”) — demand settled (popped
# from the queue): come/bring(Abram, to-shifchati)
m.result("bo(avram, el_shifchati)", tmark="t1")
# ‹וַתַּהַר› (“and-be-pregnant”) — event: conceive — agent Hagar
m.event("conceive", agent="hagar")
# ‹וַתֵּקַל גְּבִרְתָּהּ בְּעֵינֶיהָ› (“and-be-light mistress-her/its in-
# eye-her/its”) — fact holds: and-be-light-gevirtah-in-eineha
m.fact("va_teqal_gevirtah_be_eineha")

# -------------------------- Gen.16.5 · THE_GRIEVANCE_AND_THE_DEMAND_ON_GOD -
# וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם חֲמָסִי עָלֶיךָ אָנֹכִי נָתַתִּי שִׁפְחָתִי
# בְּחֵיקֶךָ וַתֵּרֶא כִּי הָרָתָה וָאֵקַל בְּעֵינֶיהָ יִשְׁפֹּט יְהוָה
# בֵּינִי וּבֵינֶיךָ
# "And Sarai said unto Abram: 'My wrong be upon thee: I gave my handmaid
# into thy bosom; and when she saw that she had conceived, I was despised in
# her eyes: the LORD judge between me and thee.'"
m.step("Gen.16.5")
# ‹וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם› (“and-say Sarai to Abram”) — event: say —
# agent Sarai
m.event("say", agent="saray")
# ‹חֲמָסִי עָלֶיךָ אָנֹכִי נָתַתִּי שִׁפְחָתִי בְּחֵיקֶךָ› (“violence-me/my
# over-you/your set female-slave-me/my in-bosom-you/your”) — fact holds:
# chamasi-alekha; anokhi-set-shifchati-in-cheqekha
m.fact("chamasi_alekha",
       "anokhi_natati_shifchati_be_cheqekha")
# ‹יִשְׁפֹּט יְהוָה בֵּינִי וּבֵינֶיךָ› (“judge YHWH between-me/my and-
# between-you/your”) — Sarai speaks a demand — LET: judge(the-LORD, beini-
# and-veinekha)
m.declare("saray", "LET",
          "yishpot(YHWH, beini_u_veinekha)")
# witness-tier presupposed read: rule_stated_then_narrowed on
# let_the_lord_judge — read, not installed
m.witness_read("let_the_lord_judge", "rule_stated_then_narrowed",
                cites=["Bava Kamma 93a:3", "Rosh Hashanah 16b:5"])

# -------------------------- Gen.16.6 · THE_PERMISSION_THE_AFFLICTION_THE_FLIGHT -
# וַיֹּאמֶר אַבְרָם אֶל־שָׂרַי הִנֵּה שִׁפְחָתֵךְ בְּיָדֵךְ עֲשִׂי־לָהּ
# הַטּוֹב בְּעֵינָיִךְ וַתְּעַנֶּהָ שָׂרַי וַתִּבְרַח מִפָּנֶיהָ
# "But Abram said unto Sarai: 'Behold, thy maid is in thy hand; do to her
# that which is good in thine eyes.' And Sarai dealt harshly with her, and
# she fled from her face."
m.step("Gen.16.6")
# ‹וַיֹּאמֶר אַבְרָם אֶל־שָׂרַי› (“and-say Abram to Sarai”) — event: say —
# agent Abram
m.event("say", agent="avram")
# ‹עֲשִׂי־לָהּ הַטּוֹב בְּעֵינָיִךְ› (“make to-her/its the-good in-eye-
# you/your”) — Abram speaks a demand — LET: make(Sarai, to-Hagar-the-good-
# in-einayikh)
m.declare("avram", "LET",
          "asi(saray, la_hagar_ha_tov_be_einayikh)")
# ‹וַתְּעַנֶּהָ שָׂרַי› (“and-afflict-literally-her/its Sarai”) — event:
# afflict — agent Sarai; theme Hagar
m.event("afflict", agent="saray", themes=["hagar"])
# ‹וַתִּבְרַח מִפָּנֶיהָ› (“and-bolt from-face-her/its”) — event: flee —
# agent Hagar
m.event("flee", agent="hagar")
# witness-tier presupposed read: statutes_pleaded_and_precedent_set on
# affliction_scene — read, not installed
m.witness_read("affliction_scene", "statutes_pleaded_and_precedent_set",
                cites=["Bereshit Rabbah 45:6", "Bereshit Rabbah 71:7", "Bava Kamma 92b:5"])

# -------------------------- Gen.16.7 · THE_ANGEL_FINDS_HER -----------------
# וַיִּמְצָאָהּ מַלְאַךְ יְהוָה עַל־עֵין הַמַּיִם בַּמִּדְבָּר עַל־הָעַיִן
# בְּדֶרֶךְ שׁוּר
# "And the angel of the LORD found her by a fountain of water in the
# wilderness, by the fountain in the way to Shur."
m.step("Gen.16.7")
# ‹וַיִּמְצָאָהּ מַלְאַךְ יְהוָה› (“and-find-her/its messenger YHWH”) —
# event: find — agent messenger-the-LORD; theme Hagar
m.event("find", agent="malakh_YHWH", themes=["hagar"])
# reads without prior install (flag, not fix): Shur
m.presupposed("shur")
# witness-tier presupposed read: divine_name_marks_the_mode on
# angel_of_the_lord — read, not installed
m.witness_read("angel_of_the_lord", "divine_name_marks_the_mode",
                cites=["Mekhilta DeRabbi Yishmael, Tractate Vayehi Beshalach 5:4"])

# -------------------------- Gen.16.8 · THE_WHERE_QUESTIONS_AND_THE_RUNAWAY_ANSWER -
# וַיֹּאמַר הָגָר שִׁפְחַת שָׂרַי אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי וַתֹּאמֶר
# מִפְּנֵי שָׂרַי גְּבִרְתִּי אָנֹכִי בֹּרַחַת
# "And he said: 'Hagar, Sarai's handmaid, whence camest thou? and whither
# goest thou?' And she said: 'I flee from the face of my mistress Sarai.'"
m.step("Gen.16.8")
# ‹וַיֹּאמַר הָגָר שִׁפְחַת שָׂרַי אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי› (“and-
# say Hagar female-slave Sarai how? from-this come/bring and-where? go”) —
# event: say — agent messenger-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי› (“how? from-this come/bring and-where?
# go”) — fact holds: ei-mizeh-come/bring-and-anah-go
m.fact("ei_mizeh_vat_ve_anah_telekhi")
# ‹וַתֹּאמֶר› (“and-say”) — event: say — agent Hagar
m.event("say", agent="hagar")
# ‹מִפְּנֵי שָׂרַי גְּבִרְתִּי אָנֹכִי בֹּרַחַת› (“from-face Sarai mistress-
# me/my bolt”) — fact holds: from-face-of-Sarai-gevirti-anokhi-bolt
m.fact("mi_pnei_saray_gevirti_anokhi_borachat")

# -------------------------- Gen.16.9 · THE_RETURN_AND_SUBMIT_COMMAND -------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה שׁוּבִי אֶל־גְּבִרְתֵּךְ וְהִתְעַנִּי
# תַּחַת יָדֶיהָ
# "And the angel of the LORD said unto her: 'Return to thy mistress, and
# submit thyself under her hands.'"
m.step("Gen.16.9")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› (“and-say to-her/its messenger YHWH”) —
# event: say — agent messenger-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹שׁוּבִי אֶל־גְּבִרְתֵּךְ וְהִתְעַנִּי תַּחַת יָדֶיהָ› (“return to
# mistress-you/your and-afflict-literally under hand-her/its”) — messenger-
# the-LORD speaks a demand — LET: return-and-afflict-literally(Hagar, to-
# gevirtekh-under-yadeha)
m.declare("malakh_YHWH", "LET",
          "shuvi_ve_hitani(hagar, el_gevirtekh_tachat_yadeha)")

# -------------------------- Gen.16.10 · THE_UNCOUNTABLE_SEED ---------------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה הַרְבָּה אַרְבֶּה אֶת־זַרְעֵךְ וְלֹא
# יִסָּפֵר מֵרֹב
# "And the angel of the LORD said unto her: 'I will greatly multiply thy
# seed, that it shall not be numbered for multitude.'"
m.step("Gen.16.10")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› (“and-say to-her/its messenger YHWH”) —
# event: say — agent messenger-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹הַרְבָּה אַרְבֶּה אֶת־זַרְעֵךְ וְלֹא יִסָּפֵר מֵרֹב› (“multiply multiply
# obj-marker seed-you/your and-not count from-abundance”) — fact holds:
# greatly-I-will-multiply-obj-marker-zarekh; and-not-count-from-abundance
m.fact("harbah_arbeh_et_zarekh",
       "ve_lo_yisafer_me_rov")

# -------------------------- Gen.16.11 · THE_ANNUNCIATION -------------------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה הִנָּךְ הָרָה וְיֹלַדְתְּ בֵּן וְקָרָאת
# שְׁמוֹ יִשְׁמָעֵאל כִּי־שָׁמַע יְהוָה אֶל־עָנְיֵךְ
# "And the angel of the LORD said unto her: 'Behold, thou art with child,
# and shalt bear a son; and thou shalt call his name Ishmael, because the
# LORD hath heard thy affliction.'"
m.step("Gen.16.11")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› (“and-say to-her/its messenger YHWH”) —
# event: say — agent messenger-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹הִנָּךְ הָרָה וְיֹלַדְתְּ בֵּן וְקָרָאת שְׁמוֹ יִשְׁמָעֵאל כִּי־שָׁמַע
# יְהוָה אֶל־עָנְיֵךְ› (“behold-you/your pregnant and-bear-young son and-
# call name-him/its Ishmael that hear YHWH to affliction-you/your”) — fact
# holds: hinakh-harah-and-bear-young-son; and-call-shemo-Ishmael; that-hear-
# the-LORD-to-onyekh
m.fact("hinakh_harah_ve_yoladt_ben",
       "ve_qarat_shemo_yishmael",
       "ki_shama_YHWH_el_onyekh")
# witness-grounded state (its own tier): both_disputed on
# angel_and_naming_censuses
m.witness_state("angel_and_naming_censuses", "both_disputed",
                cites=["Bereshit Rabbah 45:7", "Jerusalem Talmud Berakhot 1:6:10", "Bereshit Rabbah 45:8"])

# -------------------------- Gen.16.12 · THE_WILD_ASS_ORACLE ----------------
# וְהוּא יִהְיֶה פֶּרֶא אָדָם יָדוֹ בַכֹּל וְיַד כֹּל בּוֹ וְעַל־פְּנֵי
# כָל־אֶחָיו יִשְׁכֹּן
# "And he shall be a wild ass of a man: his hand shall be against every man,
# and every man's hand against him; and he shall dwell in the face of all
# his brethren.'"
m.step("Gen.16.12")
# ‹פֶּרֶא אָדָם יָדוֹ בַכֹּל וְיַד כֹּל בּוֹ וְעַל־פְּנֵי כָל־אֶחָיו
# יִשְׁכֹּן› (“onager human hand-him/its in-all and-hand all in-him/its and-
# over face all brother-him/its reside”) — fact holds: onager-human-his-
# hand-and-all-and-hand-all-come/bring; over-face-of-all-echav-reside
m.fact("pere_adam_yado_va_khol_ve_yad_kol_bo",
       "al_pnei_khol_echav_yishkon")

# -------------------------- Gen.16.13 · SHE_NAMES_YHWH ---------------------
# וַתִּקְרָא שֵׁם־יְהוָה הַדֹּבֵר אֵלֶיהָ אַתָּה אֵל רֳאִי כִּי אָמְרָה
# הֲגַם הֲלֹם רָאִיתִי אַחֲרֵי רֹאִי
# "And she called the name of the LORD that spoke unto her, Thou art a God
# of seeing; for she said: 'Have I even here seen Him that seeth Me?'"
m.step("Gen.16.13")
# ‹וַתִּקְרָא שֵׁם־יְהוָה הַדֹּבֵר אֵלֶיהָ אַתָּה אֵל רֳאִי› (“and-call name
# YHWH the-speak to-her/its you strength sight”) — named: the-LORD := El-Roi
m.name("YHWH", "El_Roi")
# ‹כִּי אָמְרָה הֲגַם הֲלֹם רָאִיתִי אַחֲרֵי רֹאִי› (“that say the-also
# hither see after see-me/my”) — fact holds: hagam-hither-see-acharei-sight
m.fact("hagam_halom_raiti_acharei_roi")
# witness-tier presupposed read: name_coined_here_still_in_use on el_roi —
# read, not installed
m.witness_read("el_roi", "name_coined_here_still_in_use",
                cites=["Jerusalem Talmud Peah 8:8:13", "Bereshit Rabbah 45:10"])

# -------------------------- Gen.16.14 · THE_WELL_OF_THE_LIVING_ONE_WHO_SEES -
# עַל־כֵּן קָרָא לַבְּאֵר בְּאֵר לַחַי רֹאִי הִנֵּה בֵין־קָדֵשׁ וּבֵין
# בָּרֶד
# "Wherefore the well was called 'Beer-lahai-roi; behold, it is between
# Kadesh and Bered."
m.step("Gen.16.14")
# ‹עַל־כֵּן קָרָא לַבְּאֵר בְּאֵר לַחַי רֹאִי› (“over so call to-pit Beer-
# lahai-roi”) — pattern recorded: over-so-call-to-pit-pit-lachai-sight
m.pattern("al_ken_qara_la_beer_beer_lachai_roi")
# ‹הִנֵּה בֵין־קָדֵשׁ וּבֵין בָּרֶד› (“behold between Kadesh and-between
# Bered”) — fact holds: hineh-vein-Kadesh-and-vein-Bered
m.fact("hineh_vein_qadesh_u_vein_bared")
# reads without prior install (flag, not fix): Kadesh, bered
m.presupposed("qadesh", "bered")

# -------------------------- Gen.16.15 · THE_BIRTH_AND_THE_FATHERS_NAMING ---
# וַתֵּלֶד הָגָר לְאַבְרָם בֵּן וַיִּקְרָא אַבְרָם שֶׁם־בְּנוֹ
# אֲשֶׁר־יָלְדָה הָגָר יִשְׁמָעֵאל
# "And Hagar bore Abram a son; and Abram called the name of his son, whom
# Hagar bore, Ishmael."
m.step("Gen.16.15")
# ‹וַתֵּלֶד הָגָר לְאַבְרָם בֵּן› (“and-bear-young Hagar to-Abram son”) —
# event: bear — agent Hagar; theme Ishmael
m.event("bear", agent="hagar", themes=["yishmael"])
# ‹וַיִּקְרָא אַבְרָם שֶׁם־בְּנוֹ … יִשְׁמָעֵאל› (“and-call Abram name son-
# him/its … Ishmael”) — named: Ishmael := Yishmael
m.name("yishmael", "Yishmael")

# -------------------------- Gen.16.16 · THE_AGE_FRAME ----------------------
# וְאַבְרָם בֶּן־שְׁמֹנִים שָׁנָה וְשֵׁשׁ שָׁנִים בְּלֶדֶת־הָגָר
# אֶת־יִשְׁמָעֵאל לְאַבְרָם
# "And Abram was fourscore and six years old, when Hagar bore Ishmael to
# Abram."
m.step("Gen.16.16")
# ‹וְאַבְרָם בֶּן־שְׁמֹנִים שָׁנָה וְשֵׁשׁ שָׁנִים› (“and-Abram son eighty
# years and-six years”) — fact holds: Abram-son-eighty-year-and-six-years
m.fact("avram_ben_shemonim_shanah_ve_shesh_shanim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'bered', 'qadesh', 'shur'}
    assert m.REGISTRY["names"] == {'YHWH': 'El_Roi', 'yishmael': 'Yishmael'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['yishpot(YHWH, beini_u_veinekha)', 'asi(saray, la_hagar_ha_tov_be_einayikh)', 'shuvi_ve_hitani(hagar, el_gevirtekh_tachat_yadeha)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['saray_lo_yaldah_lo', 've_lah_shifchah_mitzrit_u_shemah_hagar', 'atzarani_YHWH_mi_ledet', 'ulay_ibaneh_mimenah', 'mi_qetz_eser_shanim_le_shevet_avram_be_eretz_kenaan', 'va_teqal_gevirtah_be_eineha', 'chamasi_alekha', 'anokhi_natati_shifchati_be_cheqekha', 'ei_mizeh_vat_ve_anah_telekhi', 'mi_pnei_saray_gevirti_anokhi_borachat', 'harbah_arbeh_et_zarekh', 've_lo_yisafer_me_rov', 'hinakh_harah_ve_yoladt_ben', 've_qarat_shemo_yishmael', 'ki_shama_YHWH_el_onyekh', 'pere_adam_yado_va_khol_ve_yad_kol_bo', 'al_pnei_khol_echav_yishkon', 'hagam_halom_raiti_acharei_roi', 'pattern: al_ken_qara_la_beer_beer_lachai_roi', 'hineh_vein_qadesh_u_vein_bared', 'avram_ben_shemonim_shanah_ve_shesh_shanim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 25
    assert sorted(m.WORLD["witnessed"]) == ['angel_and_naming_censuses']
    assert m.WORLD["witnessed"]['angel_and_naming_censuses']["cites"] == ['Bereshit Rabbah 45:7', 'Jerusalem Talmud Berakhot 1:6:10', 'Bereshit Rabbah 45:8']
    assert all('both_disputed' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('ten_years_clause', 'binding_rule_on_a_self_graded_hint'), ('let_the_lord_judge', 'rule_stated_then_narrowed'), ('affliction_scene', 'statutes_pleaded_and_precedent_set'), ('angel_of_the_lord', 'divine_name_marks_the_mode'), ('el_roi', 'name_coined_here_still_in_use')]
    assert m.WITNESS_READS[0]["cites"] == ['Tosefta Yevamot 8:4', 'Yevamot 64a:5', 'Bereshit Rabbah 45:3', 'Jerusalem Talmud Yevamot 6:6:3', 'Mishnah Yevamot 6:6']
    assert all('binding_rule_on_a_self_graded_hint' not in f for f in m.WORLD["facts"])
    assert 'ten_years_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bava Kamma 93a:3', 'Rosh Hashanah 16b:5']
    assert all('rule_stated_then_narrowed' not in f for f in m.WORLD["facts"])
    assert 'let_the_lord_judge' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 45:6', 'Bereshit Rabbah 71:7', 'Bava Kamma 92b:5']
    assert all('statutes_pleaded_and_precedent_set' not in f for f in m.WORLD["facts"])
    assert 'affliction_scene' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Mekhilta DeRabbi Yishmael, Tractate Vayehi Beshalach 5:4']
    assert all('divine_name_marks_the_mode' not in f for f in m.WORLD["facts"])
    assert 'angel_of_the_lord' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Jerusalem Talmud Peah 8:8:13', 'Bereshit Rabbah 45:10']
    assert all('name_coined_here_still_in_use' not in f for f in m.WORLD["facts"])
    assert 'el_roi' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
