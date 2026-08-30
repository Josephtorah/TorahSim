#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_29_separation_promise — 13:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_29_separation_promise.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The separation and the promise: the return, the strife, the plain, the land forever (13:1-18)"""
from machine import Machine

m = Machine("gen_29_separation_promise")

# -------------------------- Gen.13.1 · THE_ASCENT_WITH_ALL -----------------
# וַיַּעַל אַבְרָם מִמִּצְרַיִם הוּא וְאִשְׁתּוֹ וְכָל־אֲשֶׁר־לוֹ וְלוֹט
# עִמּוֹ הַנֶּגְבָּה
# "And Abram went up out of Egypt, he, and his wife, and all that he had,
# and Lot with him, into the South."
m.step("Gen.13.1")
# ‹וַיַּעַל אַבְרָם מִמִּצְרַיִם› (“and-go-up Abram from-Egypt”) — event:
# go-up — agent Abram
m.event("go_up", agent="avram")
# ‹הוּא וְאִשְׁתּוֹ וְכָל־אֲשֶׁר־לוֹ וְלוֹט עִמּוֹ› (“he/it and-woman-
# him/its and-all which to-him/its and-Lot with-him/its”) — fact holds:
# he/it-and-his-wife-and-all-which-not-and-Lot-imo
m.fact("hu_ve_ishto_ve_khol_asher_lo_ve_lot_imo")
# reads without prior install (flag, not fix): Egypt, the-south
m.presupposed("mitzrayim", "ha_negev")

# -------------------------- Gen.13.2 · THE_HEAVY_WEALTH --------------------
# וְאַבְרָם כָּבֵד מְאֹד בַּמִּקְנֶה בַּכֶּסֶף וּבַזָּהָב
# "And Abram was very rich in cattle, in silver, and in gold."
m.step("Gen.13.2")
# ‹כָּבֵד מְאֹד בַּמִּקְנֶה בַּכֶּסֶף וּבַזָּהָב› (“be-heavy very in-
# something-bought in-silver and-in-gold”) — fact holds: be-heavy-very-in-
# the-miqneh-in-the-kesef-and-and-gold
m.fact("kaved_meod_ba_miqneh_ba_kesef_u_va_zahav")

# -------------------------- Gen.13.3 · THE_RETRACED_STAGES -----------------
# וַיֵּלֶךְ לְמַסָּעָיו מִנֶּגֶב וְעַד־בֵּית־אֵל עַד־הַמָּקוֹם אֲשֶׁר־הָיָה
# שָׁם אהלה אָהֳלוֹ בַּתְּחִלָּה בֵּין בֵּית־אֵל וּבֵין הָעָי
# "And he went on his journeys from the South even to Beth-el, unto the
# place where his tent had been at the beginning, between Beth-el and Ai;"
m.step("Gen.13.3")
# ‹וַיֵּלֶךְ לְמַסָּעָיו› (“and-go to-departure-him/its”) — event: go —
# agent Abram
m.event("go", agent="avram")
# ‹אֲשֶׁר־הָיָה שָׁם אהלה אָהֳלוֹ בַּתְּחִלָּה› (“which be there tent-
# him/its tent-him/its in-commencement”) — fact holds: which-was-there-
# aholo-in-the-techillah
m.fact("asher_hayah_sham_aholo_ba_techillah")
# reads without prior install (flag, not fix): beit-Beth-el, the-ai
m.presupposed("beit_el", "ha_ai")
# witness-tier presupposed read: lodging_law_derived_twice on
# return_to_the_place — read, not installed
m.witness_read("return_to_the_place", "lodging_law_derived_twice",
                cites=["Arakhin 16b:17", "Arakhin 16b:18"])

# -------------------------- Gen.13.4 · THE_RETURN_CALL_AT_THE_FIRST_ALTAR --
# אֶל־מְקוֹם הַמִּזְבֵּחַ אֲשֶׁר־עָשָׂה שָׁם בָּרִאשֹׁנָה וַיִּקְרָא שָׁם
# אַבְרָם בְּשֵׁם יְהוָה
# "unto the place of the altar, which he had made there at the first; and
# Abram called there on the name of the LORD."
m.step("Gen.13.4")
# ‹מְקוֹם הַמִּזְבֵּחַ אֲשֶׁר־עָשָׂה שָׁם› (“place the-altar which make
# there”) — reads without prior install (flag, not fix): altar-beit-Beth-el
m.presupposed("mizbeach_beit_el")
# ‹וַיִּקְרָא שָׁם אַבְרָם בְּשֵׁם יְהוָה› (“and-call there Abram in-name
# YHWH”) — event: call — agent Abram; theme name-the-LORD
m.event("call", agent="avram", themes=["shem_YHWH"])

# -------------------------- Gen.13.5 · LOTS_HOLDINGS -----------------------
# וְגַם־לְלוֹט הַהֹלֵךְ אֶת־אַבְרָם הָיָה צֹאן־וּבָקָר וְאֹהָלִים
# "And Lot also, who went with Abram, had flocks, and herds, and tents."
m.step("Gen.13.5")
# ‹וְגַם־לְלוֹט ... הָיָה צֹאן־וּבָקָר וְאֹהָלִים› (“and-also to-Lot be
# flock and-herd and-tent”) — fact holds: and-also-to-Lot-flock-and-herd-
# and-tent
m.fact("ve_gam_le_lot_tzon_u_vaqar_ve_ohalim")

# -------------------------- Gen.13.6 · THE_LAND_THAT_COULD_NOT_BEAR --------
# וְלֹא־נָשָׂא אֹתָם הָאָרֶץ לָשֶׁבֶת יַחְדָּו כִּי־הָיָה רְכוּשָׁם רָב
# וְלֹא יָכְלוּ לָשֶׁבֶת יַחְדָּו
# "And the land was not able to bear them, that they might dwell together;
# for their substance was great, so that they could not dwell together."
m.step("Gen.13.6")
# ‹וְלֹא־נָשָׂא אֹתָם הָאָרֶץ ... כִּי־הָיָה רְכוּשָׁם רָב› (“and-not
# lift/carry obj-marker-them/their the-earth that be property-them/their
# many/great”) — fact holds: not-lift/carry-otam-the-earth-to-dwell/sit-
# unit; that-was-rekhusham-many/great
m.fact("lo_nasa_otam_ha_aretz_la_shevet_yachdav",
       "ki_hayah_rekhusham_rav")

# -------------------------- Gen.13.7 · THE_STRIFE_AND_THE_WATCHING_LAND ----
# וַיְהִי־רִיב בֵּין רֹעֵי מִקְנֵה־אַבְרָם וּבֵין רֹעֵי מִקְנֵה־לוֹט
# וְהַכְּנַעֲנִי וְהַפְּרִזִּי אָז יֹשֵׁב בָּאָרֶץ
# "And there was a strife between the herdmen of Abram's cattle and the
# herdmen of Lot's cattle. And the Canaanite and the Perizzite dwelt then in
# the land."
m.step("Gen.13.7")
# ‹וַיְהִי־רִיב ... וְהַכְּנַעֲנִי וְהַפְּרִזִּי אָז יֹשֵׁב בָּאָרֶץ› (“and-
# be contest and-the-Kenaanite and-the-Perizzite at-that-time dwell/sit in-
# earth”) — fact holds: and-be-contest-between-roei-miqneh-Abram-and-vein-
# roei-miqneh-Lot; and-the-Kenaanite-and-the-Perizzite-at-that-time-
# dwell/sit-in-the-earth
m.fact("va_yehi_riv_bein_roei_miqneh_avram_u_vein_roei_miqneh_lot",
       "ve_ha_kenaani_ve_ha_perizi_az_yoshev_ba_aretz")
# witness-tier presupposed read: paradigm_at_the_head_of_two_laws on
# herdsmen_quarrel — read, not installed
m.witness_read("herdsmen_quarrel", "paradigm_at_the_head_of_two_laws",
                cites=["Mekhilta DeRabbi Shimon Ben Yochai 21:18", "Sifrei Devarim 286:1"])

# -------------------------- Gen.13.8 · THE_PEACE_PLEA_WE_ARE_BROTHERS ------
# וַיֹּאמֶר אַבְרָם אֶל־לוֹט אַל־נָא תְהִי מְרִיבָה בֵּינִי וּבֵינֶיךָ
# וּבֵין רֹעַי וּבֵין רֹעֶיךָ כִּי־אֲנָשִׁים אַחִים אֲנָחְנוּ
# "And Abram said unto Lot: 'Let there be no strife, I pray thee, between me
# and thee, and between my herdmen and thy herdmen; for we are brethren."
m.step("Gen.13.8")
# ‹וַיֹּאמֶר אַבְרָם אֶל־לוֹט› (“and-say Abram to Lot”) — event: say — agent
# Abram
m.event("say", agent="avram")
# ‹אַל־נָא תְהִי מְרִיבָה בֵּינִי וּבֵינֶיךָ› (“do-not please be quarrel
# between-me/my and-between-you/your”) — Abram speaks a demand — LET-NOT:
# be(merivah, between-Abram-and-between-Lot)
m.declare("avram", "LET-NOT",
          "tehi(merivah, bein_avram_u_ven_lot)")
# ‹כִּי־אֲנָשִׁים אַחִים אֲנָחְנוּ› (“that man brother we”) — fact holds:
# that-man-brother-we
m.fact("ki_anashim_achim_anachnu")
# witness-grounded state (its own tier): analogy_candidate_declined on
# we_are_brothers
m.witness_state("we_are_brothers", "analogy_candidate_declined",
                cites=["Yevamot 17b:6"])

# -------------------------- Gen.13.9 · THE_OFFER_OF_THE_WHOLE_LAND ---------
# הֲלֹא כָל־הָאָרֶץ לְפָנֶיךָ הִפָּרֶד נָא מֵעָלָי אִם־הַשְּׂמֹאל וְאֵימִנָה
# וְאִם־הַיָּמִין וְאַשְׂמְאִילָה
# "Is not the whole land before thee? separate thyself, I pray thee, from
# me; if thou wilt take the left hand, then I will go to the right; or if
# thou take the right hand, then I will go to the left.'"
m.step("Gen.13.9")
# ‹הֲלֹא כָל־הָאָרֶץ לְפָנֶיךָ› (“is-it-not all the-earth to-face-you/your”)
# — fact holds: the-not-all-the-earth-lefanekha
m.fact("ha_lo_khol_ha_aretz_lefanekha")
# ‹הִפָּרֶד נָא מֵעָלָי› (“break-through please from-over-me/my”) — Abram
# speaks a demand — LET: break-through(Lot, from-over-Abram)
m.declare("avram", "LET",
          "hipared(lot, me_al_avram)")
# ‹אִם־הַשְּׂמֹאל וְאֵימִנָה וְאִם־הַיָּמִין וְאַשְׂמְאִילָה› (“if the-dark
# and-be-right-handed and-if the-right-hand and-use-the-left-hand”) — fact
# holds: if-the-dark-and-eminah-and-if-the-right-hand-and-asmilah
m.fact("im_ha_semol_ve_eminah_ve_im_ha_yamin_ve_asmilah")

# -------------------------- Gen.13.10 · THE_EYES_LIFT_TOWARD_EDEN_GROUND ---
# וַיִּשָּׂא־לוֹט אֶת־עֵינָיו וַיַּרְא אֶת־כָּל־כִּכַּר הַיַּרְדֵּן כִּי
# כֻלָּהּ מַשְׁקֶה לִפְנֵי שַׁחֵת יְהוָה אֶת־סְדֹם וְאֶת־עֲמֹרָה
# כְּגַן־יְהוָה כְּאֶרֶץ מִצְרַיִם בֹּאֲכָה צֹעַר
# "And Lot lifted up his eyes, and beheld all the plain of the Jordan, that
# it was well watered every where, before the LORD destroyed Sodom and
# Gomorrah, like the garden of the LORD, like the land of Egypt, as thou
# goest unto Zoar."
m.step("Gen.13.10")
# ‹וַיִּשָּׂא־לוֹט אֶת־עֵינָיו› (“and-lift/carry Lot obj-marker eye-
# him/its”) — event: lift-eyes — agent Lot; theme einav
m.event("lift_eyes", agent="lot", themes=["einav"])
# ‹וַיַּרְא אֶת־כָּל־כִּכַּר הַיַּרְדֵּן› (“and-see obj-marker all circle
# the-Jordan”) — event: see — agent Lot; theme all-circle-the-Jordan
m.event("see", agent="lot", themes=["kol_kikar_ha_yarden"])
# ‹כִּי כֻלָּהּ מַשְׁקֶה לִפְנֵי שַׁחֵת יְהוָה אֶת־סְדֹם וְאֶת־עֲמֹרָה
# כְּגַן־יְהוָה כְּאֶרֶץ מִצְרַיִם› (“that all-her/its causing-to-drink to-
# face decay YHWH obj-marker Sodom and-obj-marker Gomorrah like-garden YHWH
# like-earth Egypt”) — fact holds: that-khulah-mashqeh-lifnei-decay-the-
# LORD-with-Sodom-and-with-amorah
m.fact("ki_khulah_mashqeh_lifnei_shachet_YHWH_et_sedom_ve_et_amorah")
# reads without prior install (flag, not fix): the-Jordan, Sodom, Gomorrah,
# Zoar
m.presupposed("ha_yarden", "sedom", "amora", "tzoar")
# witness-tier presupposed read: ruled_wholly_figurative_for_sin on
# kikar_description — read, not installed
m.witness_read("kikar_description", "ruled_wholly_figurative_for_sin",
                cites=["Bereshit Rabbah 41:7", "Nazir 23a:15", "Sifrei Devarim 36:10"])

# -------------------------- Gen.13.11 · THE_CHOICE_AND_THE_SEPARATION ------
# וַיִּבְחַר־לוֹ לוֹט אֵת כָּל־כִּכַּר הַיַּרְדֵּן וַיִּסַּע לוֹט מִקֶּדֶם
# וַיִּפָּרְדוּ אִישׁ מֵעַל אָחִיו
# "So Lot chose him all the plain of the Jordan; and Lot journeyed east; and
# they separated themselves the one from the other."
m.step("Gen.13.11")
# ‹וַיִּבְחַר־לוֹ לוֹט אֵת כָּל־כִּכַּר הַיַּרְדֵּן› (“and-try to-him/its
# Lot obj-marker all circle the-Jordan”) — event: choose — agent Lot; theme
# all-circle-the-Jordan
m.event("choose", agent="lot", themes=["kol_kikar_ha_yarden"])
# ‹וַיִּסַּע לוֹט מִקֶּדֶם› (“and-journey Lot from-the-east”) — event:
# journey — agent Lot
m.event("journey", agent="lot")
# ‹וַיִּפָּרְדוּ אִישׁ מֵעַל אָחִיו› (“and-break-through man from-over
# brother-him/its”) — demand settled (popped from the queue): break-
# through(Lot, from-over-Abram)
m.result("hipared(lot, me_al_avram)", tmark="t1")

# -------------------------- Gen.13.12 · THE_TWO_SETTLINGS ------------------
# אַבְרָם יָשַׁב בְּאֶרֶץ־כְּנָעַן וְלוֹט יָשַׁב בְּעָרֵי הַכִּכָּר
# וַיֶּאֱהַל עַד־סְדֹם
# "Abram dwelt in the land of Canaan, and Lot dwelt in the cities of the
# Plain, and moved his tent as far as Sodom."
m.step("Gen.13.12")
# ‹אַבְרָם יָשַׁב בְּאֶרֶץ־כְּנָעַן› (“Abram dwell/sit in-earth Canaan”) —
# event: dwell — agent Abram
m.event("dwell", agent="avram")
# ‹וְלוֹט יָשַׁב בְּעָרֵי הַכִּכָּר› (“and-Lot dwell/sit in-city the-
# circle”) — event: dwell — agent Lot
m.event("dwell", agent="lot")
# ‹וַיֶּאֱהַל עַד־סְדֹם› (“and-tent until Sodom”) — event: tent — agent Lot
m.event("tent", agent="lot")
# reads without prior install (flag, not fix): earth-Canaan
m.presupposed("eretz_kenaan")

# -------------------------- Gen.13.13 · THE_SODOM_VERDICT ------------------
# וְאַנְשֵׁי סְדֹם רָעִים וְחַטָּאִים לַיהוָה מְאֹד
# "Now the men of Sodom were wicked and sinners against the LORD
# exceedingly."
m.step("Gen.13.13")
# ‹וְאַנְשֵׁי סְדֹם רָעִים וְחַטָּאִים לַיהוָה מְאֹד› (“and-man Sodom bad
# and-criminal to-YHWH very”) — fact holds: and-men-of-Sodom-bad-and-
# criminal-to-the-LORD-very
m.fact("ve_anshei_sedom_raim_ve_chataim_la_YHWH_meod")
# witness-grounded state (its own tier):
# split_by_tense_and_reversed_at_one_seat on sodom_verdict
m.witness_state("sodom_verdict", "split_by_tense_and_reversed_at_one_seat",
                cites=["Jerusalem Talmud Sanhedrin 10:3:4", "Sifra, Bechukotai, Section 2 2", "Tosefta Shabbat 8:12"])

# -------------------------- Gen.13.14 · THE_SPEECH_AFTER_THE_SEPARATING ----
# וַיהוָה אָמַר אֶל־אַבְרָם אַחֲרֵי הִפָּרֶד־לוֹט מֵעִמּוֹ שָׂא נָא עֵינֶיךָ
# וּרְאֵה מִן־הַמָּקוֹם אֲשֶׁר־אַתָּה שָׁם צָפֹנָה וָנֶגְבָּה וָקֵדְמָה
# וָיָמָּה
# "And the LORD said unto Abram, after that Lot was separated from him:
# 'Lift up now thine eyes, and look from the place where thou art, northward
# and southward and eastward and westward;"
m.step("Gen.13.14")
# ‹וַיהוָה אָמַר אֶל־אַבְרָם אַחֲרֵי הִפָּרֶד־לוֹט מֵעִמּוֹ› (“and-YHWH say
# to Abram after break-through Lot from-with-him/its”) — event: say — agent
# the-LORD
m.event("say", agent="YHWH")
# ‹שָׂא נָא עֵינֶיךָ וּרְאֵה ... צָפֹנָה וָנֶגְבָּה וָקֵדְמָה וָיָמָּה›
# (“lift/carry please eye-you/your and-see hidden-ward and-south-ward and-
# front-ward and-seas-ward”) — the-LORD speaks a demand — LET: lift/carry-
# and-see(Abram, tzafonah-and-negbah-and-qedmah-and-yamah)
m.declare("YHWH", "LET",
          "sa_u_ree(avram, tzafonah_va_negbah_va_qedmah_va_yamah)")

# -------------------------- Gen.13.15 · THE_GIFT_FOREVER -------------------
# כִּי אֶת־כָּל־הָאָרֶץ אֲשֶׁר־אַתָּה רֹאֶה לְךָ אֶתְּנֶנָּה וּלְזַרְעֲךָ
# עַד־עוֹלָם
# "for all the land which thou seest, to thee will I give it, and to thy
# seed for ever."
m.step("Gen.13.15")
# ‹כִּי אֶת־כָּל־הָאָרֶץ אֲשֶׁר־אַתָּה רֹאֶה לְךָ אֶתְּנֶנָּה וּלְזַרְעֲךָ
# עַד־עוֹלָם› (“that obj-marker all the-earth which you see to-you/your set-
# her/its and-to-seed-you/your until forever”) — fact holds: with-all-the-
# earth-which-you-shepherd-to-you-etnenah; and-to-zarakha-until-forever
m.fact("et_kol_ha_aretz_asher_ata_roeh_lekha_etnenah",
       "u_le_zarakha_ad_olam")

# -------------------------- Gen.13.16 · THE_DUST_MEASURE -------------------
# וְשַׂמְתִּי אֶת־זַרְעֲךָ כַּעֲפַר הָאָרֶץ אֲשֶׁר אִם־יוּכַל אִישׁ לִמְנוֹת
# אֶת־עֲפַר הָאָרֶץ גַּם־זַרְעֲךָ יִמָּנֶה
# "And I will make thy seed as the dust of the earth; so that if a man can
# number the dust of the earth, then shall thy seed also be numbered."
m.step("Gen.13.16")
# ‹וְשַׂמְתִּי אֶת־זַרְעֲךָ כַּעֲפַר הָאָרֶץ ... גַּם־זַרְעֲךָ יִמָּנֶה›
# (“and-put/set obj-marker seed-you/your like-dust the-earth also seed-
# you/your weigh-out”) — fact holds: and-put/set-with-zarakha-like-dust-the-
# earth; if-be-able-man-limnot-also-zarakha-yimaneh
m.fact("ve_samti_et_zarakha_ka_afar_ha_aretz",
       "im_yukhal_ish_limnot_gam_zarakha_yimaneh")
# witness-tier presupposed read: graded_literal_not_hyperbole on dust_simile
# — read, not installed
m.witness_read("dust_simile", "graded_literal_not_hyperbole",
                cites=["Sifrei Devarim 25:4", "Bereshit Rabbah 41:9", "Megillah 16a:15"])

# -------------------------- Gen.13.17 · THE_WALK_COMMAND -------------------
# קוּם הִתְהַלֵּךְ בָּאָרֶץ לְאָרְכָּהּ וּלְרָחְבָּהּ כִּי לְךָ אֶתְּנֶנָּה
# "Arise, walk through the land in the length of it and in the breadth of
# it; for unto thee will I give it.'"
m.step("Gen.13.17")
# ‹קוּם הִתְהַלֵּךְ בָּאָרֶץ לְאָרְכָּהּ וּלְרָחְבָּהּ› (“arise walk/go in-
# earth to-length-her/its and-to-width-her/its”) — the-LORD speaks a demand
# — LET: arise-walk/go(Abram, in-the-earth-to-arkah-and-to-rachbah)
m.declare("YHWH", "LET",
          "qum_hithalekh(avram, ba_aretz_le_arkah_u_le_rachbah)")
# ‹כִּי לְךָ אֶתְּנֶנָּה› (“that to-you/your set-her/its”) — fact holds:
# that-to-you-etnenah
m.fact("ki_lekha_etnenah")
# witness-tier presupposed read: acquisition_by_walking on walk_the_land —
# read, not installed
m.witness_read("walk_the_land", "acquisition_by_walking",
                cites=["Bava Batra 100a:7", "Bereshit Rabbah 41:10", "Jerusalem Talmud Kiddushin 1:3:5"])

# -------------------------- Gen.13.18 · THE_HEBRON_ALTAR -------------------
# וַיֶּאֱהַל אַבְרָם וַיָּבֹא וַיֵּשֶׁב בְּאֵלֹנֵי מַמְרֵא אֲשֶׁר
# בְּחֶבְרוֹן וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה
# "And Abram moved his tent, and came and dwelt by the terebinths of Mamre,
# which are in Hebron, and built there an altar unto the LORD."
m.step("Gen.13.18")
# ‹וַיֶּאֱהַל אַבְרָם› (“and-tent Abram”) — event: tent — agent Abram
m.event("tent", agent="avram")
# ‹וַיָּבֹא› (“and-come/bring”) — event: come — agent Abram
m.event("come", agent="avram")
# ‹וַיֵּשֶׁב בְּאֵלֹנֵי מַמְרֵא› (“and-dwell/sit in-oak Mamre”) — event:
# dwell — agent Abram
m.event("dwell", agent="avram")
# ‹וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה› (“and-build there altar to-YHWH”) —
# event: build — agent Abram; theme altar
m.event("build", agent="avram", themes=["mizbeach"])
# ‹מִזְבֵּחַ› (“altar”) — the world gains: altar-Hebron
m.install("mizbeach_chevron")
# reads without prior install (flag, not fix): Mamre, Hebron
m.presupposed("mamre", "chevron")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach_chevron'}
    assert m.presupposed_set() == {'amora', 'beit_el', 'chevron', 'eretz_kenaan', 'ha_ai', 'ha_negev', 'ha_yarden', 'mamre', 'mitzrayim', 'mizbeach_beit_el', 'sedom', 'tzoar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tehi(merivah, bein_avram_u_ven_lot)', 'sa_u_ree(avram, tzafonah_va_negbah_va_qedmah_va_yamah)', 'qum_hithalekh(avram, ba_aretz_le_arkah_u_le_rachbah)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 12}
    assert sorted(m.WORLD["facts"]) == sorted(['hu_ve_ishto_ve_khol_asher_lo_ve_lot_imo', 'kaved_meod_ba_miqneh_ba_kesef_u_va_zahav', 'asher_hayah_sham_aholo_ba_techillah', 've_gam_le_lot_tzon_u_vaqar_ve_ohalim', 'lo_nasa_otam_ha_aretz_la_shevet_yachdav', 'ki_hayah_rekhusham_rav', 'va_yehi_riv_bein_roei_miqneh_avram_u_vein_roei_miqneh_lot', 've_ha_kenaani_ve_ha_perizi_az_yoshev_ba_aretz', 'ki_anashim_achim_anachnu', 'ha_lo_khol_ha_aretz_lefanekha', 'im_ha_semol_ve_eminah_ve_im_ha_yamin_ve_asmilah', 'ki_khulah_mashqeh_lifnei_shachet_YHWH_et_sedom_ve_et_amorah', 've_anshei_sedom_raim_ve_chataim_la_YHWH_meod', 'et_kol_ha_aretz_asher_ata_roeh_lekha_etnenah', 'u_le_zarakha_ad_olam', 've_samti_et_zarakha_ka_afar_ha_aretz', 'im_yukhal_ish_limnot_gam_zarakha_yimaneh', 'ki_lekha_etnenah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 21
    assert sorted(m.WORLD["witnessed"]) == ['sodom_verdict', 'we_are_brothers']
    assert m.WORLD["witnessed"]['sodom_verdict']["cites"] == ['Jerusalem Talmud Sanhedrin 10:3:4', 'Sifra, Bechukotai, Section 2 2', 'Tosefta Shabbat 8:12']
    assert all('split_by_tense_and_reversed_at_one_seat' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['we_are_brothers']["cites"] == ['Yevamot 17b:6']
    assert all('analogy_candidate_declined' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('return_to_the_place', 'lodging_law_derived_twice'), ('herdsmen_quarrel', 'paradigm_at_the_head_of_two_laws'), ('kikar_description', 'ruled_wholly_figurative_for_sin'), ('dust_simile', 'graded_literal_not_hyperbole'), ('walk_the_land', 'acquisition_by_walking')]
    assert m.WITNESS_READS[0]["cites"] == ['Arakhin 16b:17', 'Arakhin 16b:18']
    assert all('lodging_law_derived_twice' not in f for f in m.WORLD["facts"])
    assert 'return_to_the_place' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Mekhilta DeRabbi Shimon Ben Yochai 21:18', 'Sifrei Devarim 286:1']
    assert all('paradigm_at_the_head_of_two_laws' not in f for f in m.WORLD["facts"])
    assert 'herdsmen_quarrel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 41:7', 'Nazir 23a:15', 'Sifrei Devarim 36:10']
    assert all('ruled_wholly_figurative_for_sin' not in f for f in m.WORLD["facts"])
    assert 'kikar_description' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifrei Devarim 25:4', 'Bereshit Rabbah 41:9', 'Megillah 16a:15']
    assert all('graded_literal_not_hyperbole' not in f for f in m.WORLD["facts"])
    assert 'dust_simile' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bava Batra 100a:7', 'Bereshit Rabbah 41:10', 'Jerusalem Talmud Kiddushin 1:3:5']
    assert all('acquisition_by_walking' not in f for f in m.WORLD["facts"])
    assert 'walk_the_land' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
