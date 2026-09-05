#!/usr/bin/env python3
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
# ‹וַיִּהְיוּ חַיֵּי שָׂרָה› (“and-be alive Sarah”)
# ‹מֵאָה שָׁנָה וְעֶשְׂרִים› (“hundred years and-twenty”)
# ‹שָׁנָה וְשֶׁבַע שָׁנִים› (“years and-seven years”)
# ‹שְׁנֵי חַיֵּי שָׂרָה› (“years alive Sarah”)
# "And the life of Sarah was a hundred and seven and twenty years; these
# were the years of the life of Sarah."
m.step("Gen.23.1")
# ‹חַיֵּי שָׂרָה› (“alive Sarah”)
# — the world gains: sarah
m.install("sarah")
# ‹מֵאָה שָׁנָה וְעֶשְׂרִים› (“hundred years and-twenty”)
# ‹שָׁנָה וְשֶׁבַע שָׁנִים› (“years and-seven years”)
# — fact holds: chayei-sarah-hundred-and-twenty-and-seven-years
m.fact("chayei_sarah_meah_ve_esrim_ve_sheva_shanim")
# witness-tier presupposed read: parsed_clause_against_clause on
# split_lifespan — read, not installed
m.witness_read("split_lifespan", "parsed_clause_against_clause",
                cites=["Bereshit Rabbah 58:1"])
# witness-tier presupposed read: inheritance_wire_to_a_later_reign on
# one_hundred_twenty_seven — read, not installed
m.witness_read("one_hundred_twenty_seven", "inheritance_wire_to_a_later_reign",
                cites=["Bereshit Rabbah 58:3"])

# -------------------------- Gen.23.2 · THE_DEATH_AND_THE_MOURNING ----------
# ‹וַתָּמָת שָׂרָה בְּקִרְיַת› (“and-die Sarah in”)
# ‹אַרְבַּע הִוא חֶבְרוֹן› (“Kirjath-Arba he/it Hebron”)
# ‹בְּאֶרֶץ כְּנָעַן וַיָּבֹא› (“in-earth Canaan and-come/bring”)
# ‹אַבְרָהָם לִסְפֹּד לְשָׂרָה› (“Abraham to-tear-the-hair-and-beat-the-b
# to-Sarah”)
# ‹וְלִבְכֹּתָהּ› (“and-to-weep-her/its”)
# "And Sarah died in Kiriatharba—the same is Hebron—in the land of Canaan;
# and Abraham came to mourn for Sarah, and to weep for her."
m.step("Gen.23.2")
# ‹וַתָּמָת שָׂרָה› (“and-die Sarah”)
# — event: die — theme sarah
m.event("die", themes=["sarah"])
# ‹לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ› (“to-tear-the-hair-and-beat-the-b to-
# Sarah and-to-weep-her/its”)
# — event: mourn-weep — agent Abraham; theme sarah
m.event("mourn_weep", agent="avraham", themes=["sarah"])
# ‹וַתָּמָת שָׂרָה … לִסְפֹּד› (“and-die Sarah … to-tear-the-hair-and-beat-
# the-b”)
# ‹לְשָׂרָה וְלִבְכֹּתָהּ› (“to-Sarah and-to-weep-her/its”)
# — fact holds: and-die-sarah-in-in-Kirjath-Arba-hi-Hebron; to-me-sepod-to-
# sarah-and-livkotah
m.fact("va_tamat_sarah_be_qiryat_arba_hi_chevron",
       "li_sepod_le_sarah_ve_livkotah")
# ‹הִוא חֶבְרוֹן› (“he/it Hebron”)
# — reads without prior install (flag, not fix): Hebron
m.presupposed("chevron")
# witness-tier presupposed read: cause_supplied_by_adjacency on
# came_to_mourn — read, not installed
m.witness_read("came_to_mourn", "cause_supplied_by_adjacency",
                cites=["Bereshit Rabbah 58:5"])
# witness-tier presupposed read: eulogy_question on lispod_le_sarah — read,
# not installed
m.witness_read("lispod_le_sarah", "eulogy_question",
                cites=["Sanhedrin 46b:20", "Sanhedrin 46b:21", "Sanhedrin 46b:22"])

# -------------------------- Gen.23.3 · THE_RISING_FROM_THE_DEAD_FACE -------
# ‹וַיָּקָם אַבְרָהָם מֵעַל› (“and-arise Abraham from-over”)
# ‹פְּנֵי מֵתוֹ וַיְדַבֵּר› (“face die-him/its and-speak”)
# ‹אֶל־בְּנֵי־חֵת לֵאמֹר› (“to son Heth to-say”)
# "And Abraham rose up from before his dead, and spoke unto the children of
# Heth, saying:"
m.step("Gen.23.3")
# ‹וַיָּקָם … מֵעַל פְּנֵי› (“and-arise … from-over face”)
# ‹מֵתוֹ וַיְדַבֵּר› (“die-him/its and-speak”)
# — event: rise-speak — agent Abraham
m.event("rise_speak", agent="avraham")
# witness-tier presupposed read: mourner_exemption_law_seated_here on
# rose_from_before_his_dead — read, not installed
m.witness_read("rose_from_before_his_dead", "mourner_exemption_law_seated_here",
                cites=["Bereshit Rabbah 58:6", "Mishnah Berakhot 3:1"])
# witness-tier presupposed read: premourner_exemption on me_al_pene_meto —
# read, not installed
m.witness_read("me_al_pene_meto", "premourner_exemption",
                cites=["Berakhot 18a:2", "Berakhot 18a:3", "Berakhot 18a:4"])

# -------------------------- Gen.23.4 · THE_SOJOURNER_ASKS_FOR_A_GRAVE ------
# ‹גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם› (“sojourner and-resident-alien with-
# you/your(pl)”)
# ‹תְּנוּ לִי אֲחֻזַּת־קֶבֶר› (“set to-me/my something-seized sepulchre”)
# ‹עִמָּכֶם וְאֶקְבְּרָה מֵתִי› (“with-you/your(pl) and-bury die-me/my”)
# ‹מִלְּפָנָי› (“from-to-face-me/my”)
# "'I am a stranger and a sojourner with you: give me a possession of a
# burying-place with you, that I may bury my dead out of my sight.'"
m.step("Gen.23.4")
# ‹גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם› (“sojourner and-resident-alien with-
# you/your(pl)”)
# — fact holds: sojourner-and-resident-alien-anokhi-imakhem
m.fact("ger_ve_toshav_anokhi_imakhem")
# ‹תְּנוּ לִי אֲחֻזַּת־קֶבֶר› (“set to-me/my something-seized sepulchre”)
# ‹עִמָּכֶם› (“with-you/your(pl)”)
# — Abraham speaks a demand — LET: set(something-seized-sepulchre)
m.declare("avraham", "LET",
          "tenu(achuzat_qever)")

# -------------------------- Gen.23.5 · THE_ANSWER_FRAME --------------------
# ‹וַיַּעֲנוּ בְנֵי־חֵת אֶת־אַבְרָהָם› (“and-eye son Heth obj-marker
# Abraham”)
# ‹לֵאמֹר לוֹ› (“to-say to-him/its”)
# "And the children of Heth answered Abraham, saying unto him:"
m.step("Gen.23.5")
# ‹בְנֵי־חֵת› (“son Heth”)
# — the world gains: sons-of-Heth
m.install("bnei_chet")

# -------------------------- Gen.23.6 · THE_PRINCE_AND_THE_CHOICE_GRAVES ----
# ‹שְׁמָעֵנוּ אֲדֹנִי נְשִׂיא› (“hear-us/our lord-me/my prince”)
# ‹אֱלֹהִים אַתָּה בְּתוֹכֵנוּ› (“God you in-midst-us/our”)
# ‹בְּמִבְחַר קְבָרֵינוּ קְבֹר› (“in-select sepulchre-us/our bury”)
# ‹אֶת־מֵתֶךָ אִישׁ מִמֶּנּוּ› (“obj-marker die-you/your man from-us/our”)
# ‹אֶת־קִבְרוֹ לֹא־יִכְלֶה מִמְּךָ› (“obj-marker sepulchre-him/its not
# restrict from-you/your”)
# ‹מִקְּבֹר מֵתֶךָ› (“from-inter die-you/your”)
# "'Hear us, my lord: thou art a mighty prince among us; in the choice of
# our sepulchres bury thy dead; none of us shall withhold from thee his
# sepulchre, but that thou mayest bury thy dead.'"
m.step("Gen.23.6")
# ‹שְׁמָעֵנוּ אֲדֹנִי› (“hear-us/our lord-me/my”)
# — sons-of-Heth speaks a demand — LET: shemaenu(adoni)
m.declare("bnei_chet", "LET",
          "shemaenu(adoni)")
# ‹בְּמִבְחַר קְבָרֵינוּ קְבֹר› (“in-select sepulchre-us/our bury”)
# ‹אֶת־מֵתֶךָ› (“obj-marker die-you/your”)
# — sons-of-Heth speaks a demand — LET: bury(in-select-qevareinu)
m.declare("bnei_chet", "LET",
          "qevor(be_mivchar_qevareinu)")
# ‹נְשִׂיא אֱלֹהִים אַתָּה› (“prince God you”)
# ‹בְּתוֹכֵנוּ› (“in-midst-us/our”)
# — fact holds: prince-God-you-in-tokhenu
m.fact("nesi_elohim_atah_be_tokhenu")
# witness-tier presupposed read: honorific_solved_two_ways on prince_of_God
# — read, not installed
m.witness_read("prince_of_God", "honorific_solved_two_ways",
                cites=["Onkelos Genesis 23:6", "Bereshit Rabbah 43:5"])

# -------------------------- Gen.23.7 · THE_FIRST_BOW -----------------------
# ‹וַיָּקָם אַבְרָהָם וַיִּשְׁתַּחוּ› (“and-arise Abraham and-afflict”)
# ‹לְעַם־הָאָרֶץ לִבְנֵי־חֵת› (“to-people the-earth to-son Heth”)
# "And Abraham rose up, and bowed down to the people of the land, even to
# the children of Heth."
m.step("Gen.23.7")
# ‹וַיִּשְׁתַּחוּ לְעַם־הָאָרֶץ› (“and-afflict to-people the-earth”)
# — event: bow — agent Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.8 · THE_ENTREATY_COMPOUND ---------------
# ‹וַיְדַבֵּר אִתָּם לֵאמֹר› (“and-speak with-them/their to-say”)
# ‹אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר› (“if there-is with living-being-
# you/your(pl) to-inter”)
# ‹אֶת־מֵתִי מִלְּפָנַי שְׁמָעוּנִי› (“obj-marker die-me/my from-to-face-
# me/my hear-me/my”)
# ‹וּפִגְעוּ־לִי בְּעֶפְרוֹן בֶּן־צֹחַר› (“and-impinge to-me/my in-Ephron
# son Zohar”)
# "And he spoke with them, saying: 'If it be your mind that I should bury my
# dead out of my sight, hear me, and entreat for me to Ephron the son of
# Zohar,"
m.step("Gen.23.8")
# ‹שְׁמָעוּנִי וּפִגְעוּ־לִי בְּעֶפְרוֹן› (“hear-me/my and-impinge to-me/my
# in-Ephron”)
# — Abraham speaks a demand — LET: shimuni-and-impinge(in-Ephron)
m.declare("avraham", "LET",
          "shimuni_u_figu(be_efron)")
# ‹אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר› (“if there-is with living-being-
# you/your(pl) to-inter”)
# ‹אֶת־מֵתִי› (“obj-marker die-me/my”)
# — fact holds: if-there-is-obj-marker-nafshekhem-liqbor-obj-marker-meti
m.fact("im_yesh_et_nafshekhem_liqbor_et_meti")

# -------------------------- Gen.23.9 · THE_FULL_PRICE_CLAUSE ---------------
# ‹וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה› (“and-set to-me/my obj-marker
# cavern the-Machpelah”)
# ‹אֲשֶׁר־לוֹ אֲשֶׁר בִּקְצֵה› (“which to-him/its which in-end”)
# ‹שָׂדֵהוּ בְּכֶסֶף מָלֵא› (“field-him/its in-silver full”)
# ‹יִתְּנֶנָּה לִי בְּתוֹכְכֶם› (“set-her/its to-me/my in-midst-
# you/your(pl)”)
# ‹לַאֲחֻזַּת־קָבֶר› (“to-something-seized sepulchre”)
# "that he may give me the cave of Machpelah, which he hath, which is in the
# end of his field; for the full price let him give it to me in the midst of
# you for a possession of a burying-place.'"
m.step("Gen.23.9")
# ‹וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה› (“and-set to-me/my obj-marker
# cavern the-Machpelah”)
# ‹… בְּכֶסֶף מָלֵא› (“in-silver full”)
# — fact holds: and-set-to-me-obj-marker-cavern-the-makhpelah; in-silver-
# full-yitnenah-to-me
m.fact("ve_yiten_li_et_mearat_ha_makhpelah",
       "be_khesef_male_yitnenah_li")

# -------------------------- Gen.23.10 · THE_ANSWER_FROM_INSIDE_THE_ROOM ----
# ‹וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ› (“and-Ephron dwell/sit in-midst”)
# ‹בְּנֵי־חֵת וַיַּעַן עֶפְרוֹן› (“son Heth and-eye Ephron”)
# ‹הַחִתִּי אֶת־אַבְרָהָם בְּאָזְנֵי› (“the-Chittite obj-marker Abraham in-
# broadness.-i.e.-the-ear”)
# ‹בְנֵי־חֵת לְכֹל בָּאֵי› (“son Heth to-all come/bring”)
# ‹שַׁעַר־עִירוֹ לֵאמֹר› (“gate city-him/its to-say”)
# "Now Ephron was sitting in the midst of the children of Heth; and Ephron
# the Hittite answered Abraham in the hearing of the children of Heth, even
# of all that went in at the gate of his city, saying:"
m.step("Gen.23.10")
# ‹וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ› (“and-Ephron dwell/sit in-midst”)
# ‹בְּנֵי־חֵת› (“son Heth”)
# — the world gains: Ephron
m.install("efron")
# ‹בְּאָזְנֵי בְנֵי־חֵת לְכֹל› (“in-broadness.-i.e.-the-ear son Heth to-
# all”)
# ‹בָּאֵי שַׁעַר־עִירוֹ› (“come/bring gate city-him/its”)
# — fact holds: in-oznei-vnei-Heth-to-all-baei-gate-iro
m.fact("be_oznei_vnei_chet_le_khol_baei_shaar_iro")
# witness-tier presupposed read: seated_that_very_day on
# defective_participle_sitting — read, not installed
m.witness_read("defective_participle_sitting", "seated_that_very_day",
                cites=["Bereshit Rabbah 58:7"])

# -------------------------- Gen.23.11 · THE_GIFT_ROUND ---------------------
# ‹לֹא־אֲדֹנִי שְׁמָעֵנִי הַשָּׂדֶה› (“not lord-me/my hear-me/my the-field”)
# ‹נָתַתִּי לָךְ וְהַמְּעָרָה› (“set to-you/your and-the-cavern”)
# ‹אֲשֶׁר־בּוֹ לְךָ נְתַתִּיהָ› (“which in-him/its to-you/your set-her/its”)
# ‹לְעֵינֵי בְנֵי־עַמִּי נְתַתִּיהָ› (“to-eye son people-me/my set-her/its”)
# ‹לָּךְ קְבֹר מֵתֶךָ› (“to-you/your bury die-you/your”)
# "'Nay, my lord, hear me: the field give I thee, and the cave that is
# therein, I give it thee; in the presence of the sons of my people give I
# it thee; bury thy dead.'"
m.step("Gen.23.11")
# ‹לֹא־אֲדֹנִי שְׁמָעֵנִי› (“not lord-me/my hear-me/my”)
# — Ephron speaks a demand — LET: shemaeni(not-adoni)
m.declare("efron", "LET",
          "shemaeni(lo_adoni)")
# ‹קְבֹר מֵתֶךָ› (“bury die-you/your”)
# — Ephron speaks a demand — LET: bury(obj-marker-metekha)
m.declare("efron", "LET",
          "qevor(et_metekha)")
# ‹הַשָּׂדֶה נָתַתִּי לָךְ› (“the-field set to-you/your”)
# ‹… נְתַתִּיהָ› (“set-her/its”)
# — fact holds: the-field-set-to-you-netatiha
m.fact("ha_sadeh_natati_lakh_netatiha")

# -------------------------- Gen.23.12 · THE_SECOND_BOW ---------------------
# ‹וַיִּשְׁתַּחוּ אַבְרָהָם לִפְנֵי› (“and-afflict Abraham to-face”)
# ‹עַם הָאָרֶץ› (“people the-earth”)
# "And Abraham bowed down before the people of the land."
m.step("Gen.23.12")
# ‹וַיִּשְׁתַּחוּ … לִפְנֵי עַם› (“and-afflict … to-face people”)
# ‹הָאָרֶץ› (“the-earth”)
# — event: bow — agent Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.13 · THE_WISH_AND_THE_TAKE_DEMAND -------
# ‹וַיְדַבֵּר אֶל־עֶפְרוֹן בְּאָזְנֵי› (“and-speak to Ephron in-
# broadness.-i.e.-the-ear”)
# ‹עַם־הָאָרֶץ לֵאמֹר אַךְ› (“people the-earth to-say indeed”)
# ‹אִם־אַתָּה לוּ שְׁמָעֵנִי› (“if you conditional-particle hear-me/my”)
# ‹נָתַתִּי כֶּסֶף הַשָּׂדֶה› (“set silver the-field”)
# ‹קַח מִמֶּנִּי וְאֶקְבְּרָה› (“take from-me/my and-bury”)
# ‹אֶת־מֵתִי שָׁמָּה› (“obj-marker die-me/my there-ward”)
# "And he spoke unto Ephron in the hearing of the people of the land,
# saying: 'But if thou wilt, I pray thee, hear me: I will give the price of
# the field; take it of me, and I will bury my dead there.'"
m.step("Gen.23.13")
# ‹אַךְ אִם־אַתָּה לוּ› (“indeed if you conditional-particle”)
# ‹שְׁמָעֵנִי נָתַתִּי כֶּסֶף› (“hear-me/my set silver”)
# ‹הַשָּׂדֶה› (“the-field”)
# — fact holds: indeed-if-you-conditional-particle-shemaeni; set-silver-the-
# field
m.fact("akh_im_atah_lu_shemaeni",
       "natati_kesef_ha_sadeh")
# ‹קַח מִמֶּנִּי› (“take from-me/my”)
# — Abraham speaks a demand — LET: take(silver-the-field)
m.declare("avraham", "LET",
          "qach(kesef_ha_sadeh)")
# witness-tier presupposed read: rendered_as_offer_and_acceptance on
# hear_me_idiom — read, not installed
m.witness_read("hear_me_idiom", "rendered_as_offer_and_acceptance",
                cites=["Onkelos Genesis 23:13", "Onkelos Genesis 23:8"])
# witness-tier presupposed read: betrothal_money_machine on qach_mimeni —
# read, not installed
m.witness_read("qach_mimeni", "betrothal_money_machine",
                cites=["Kiddushin 2a:3", "Kiddushin 2a:4", "Kiddushin 2a:5", "Kiddushin 4b:2", "Kiddushin 4b:3", "Kiddushin 4b:4", "Kiddushin 11b:4", "Kiddushin 11b:5", "Kiddushin 11b:6"])

# -------------------------- Gen.23.14 · THE_SECOND_ANSWER_FRAME ------------
# ‹וַיַּעַן עֶפְרוֹן אֶת־אַבְרָהָם› (“and-eye Ephron obj-marker Abraham”)
# ‹לֵאמֹר לוֹ› (“to-say to-him/its”)
# "And Ephron answered Abraham, saying unto him:"
m.step("Gen.23.14")
# ‹וַיַּעַן עֶפְרוֹן› (“and-eye Ephron”)
# — event: answer — agent Ephron
m.event("answer", agent="efron")

# -------------------------- Gen.23.15 · THE_PRICE_ROUND --------------------
# ‹אֲדֹנִי שְׁמָעֵנִי אֶרֶץ› (“lord-me/my hear-me/my earth”)
# ‹אַרְבַּע מֵאֹת שֶׁקֶל־כֶּסֶף› (“four hundred weight silver”)
# ‹בֵּינִי וּבֵינְךָ מַה־הִוא› (“between-me/my and-between-you/your what
# he/it”)
# ‹וְאֶת־מֵתְךָ קְבֹר› (“and-obj-marker die-you/your bury”)
# "'My lord, hearken unto me: a piece of land worth four hundred shekels of
# silver, what is that betwixt me and thee? bury therefore thy dead.'"
m.step("Gen.23.15")
# ‹אֲדֹנִי שְׁמָעֵנִי› (“lord-me/my hear-me/my”)
# — Ephron speaks a demand — LET: shemaeni(adoni)
m.declare("efron", "LET",
          "shemaeni(adoni)")
# ‹אֶרֶץ אַרְבַּע מֵאֹת› (“earth four hundred”)
# ‹שֶׁקֶל־כֶּסֶף … וְאֶת־מֵתְךָ קְבֹר› (“weight silver … and-obj-marker die-
# you/your bury”)
# — fact holds: earth-Kirjath-Arba-hundred-weight-silver-beini-and-veinkha;
# and-obj-marker-metkha-bury-resound
m.fact("eretz_arba_meot_sheqel_kesef_beini_u_veinkha",
       "ve_et_metkha_qevor_resound")

# -------------------------- Gen.23.16 · CYCLE_A_THE_HEARING_AND_THE_WEIGHING -
# ‹וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן› (“and-hear Abraham to Ephron”)
# ‹וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן› (“and-suspend Abraham to-Ephron”)
# ‹אֶת־הַכֶּסֶף אֲשֶׁר דִּבֶּר› (“obj-marker the-silver which speak”)
# ‹בְּאָזְנֵי בְנֵי־חֵת אַרְבַּע› (“in-broadness.-i.e.-the-ear son Heth
# four”)
# ‹מֵאוֹת שֶׁקֶל כֶּסֶף› (“hundred weight silver”)
# ‹עֹבֵר לַסֹּחֵר› (“pass-over to-travel-round”)
# "And Abraham hearkened unto Ephron; and Abraham weighed to Ephron the
# silver, which he had named in the hearing of the children of Heth, four
# hundred shekels of silver, current money with the merchant."
m.step("Gen.23.16")
# ‹וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן› (“and-hear Abraham to Ephron”)
# — demand settled (popped from the queue): shemaeni(adoni)
m.result("shemaeni(adoni)", tmark="t1")
# ‹וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן› (“and-suspend Abraham to-Ephron”)
# ‹אֶת־הַכֶּסֶף› (“obj-marker the-silver”)
# — event: weigh-silver — agent Abraham
m.event("weigh_silver", agent="avraham")
# ‹אַרְבַּע מֵאוֹת שֶׁקֶל› (“four hundred weight”)
# ‹כֶּסֶף עֹבֵר לַסֹּחֵר› (“silver pass-over to-travel-round”)
# — fact holds: and-suspend-Kirjath-Arba-hundred-weight-pass-over-to-travel-
# round
m.fact("va_yishqol_arba_meot_sheqel_over_la_socher")
# witness-tier presupposed read: diminished_where_he_takes_the_silver on
# vendor_name_defective_at_the_weighing — read, not installed
m.witness_read("vendor_name_defective_at_the_weighing", "diminished_where_he_takes_the_silver",
                cites=["Bereshit Rabbah 58:7"])
# witness-tier presupposed read: weight_table_applied_not_quoted on
# four_hundred_shekels — read, not installed
m.witness_read("four_hundred_shekels", "weight_table_applied_not_quoted",
                cites=["Onkelos Genesis 23:16", "Bereshit Rabbah 58:7"])
# witness-tier presupposed read: deed_file on over_la_socher — read, not
# installed
m.witness_read("over_la_socher", "deed_file",
                cites=["Bava Batra 69b:1", "Bava Batra 69b:2", "Bekhorot 50a:7", "Bekhorot 50a:8", "Bekhorot 50a:9"])

# -------------------------- Gen.23.17 · THE_FIELD_ARISES -------------------
# ‹וַיָּקָם שְׂדֵה עֶפְרוֹן› (“and-arise field Ephron”)
# ‹אֲשֶׁר בַּמַּכְפֵּלָה אֲשֶׁר› (“which in-Machpelah which”)
# ‹לִפְנֵי מַמְרֵא הַשָּׂדֶה› (“to-face Mamre the-field”)
# ‹וְהַמְּעָרָה אֲשֶׁר־בּוֹ וְכָל־הָעֵץ› (“and-the-cavern which in-him/its
# and-all the-tree”)
# ‹אֲשֶׁר בַּשָּׂדֶה אֲשֶׁר› (“which in-field which”)
# ‹בְּכָל־גְּבֻלוֹ סָבִיב› (“in-all cord-him/its circle”)
# "So the field of Ephron, which was in Machpelah, which was before Mamre,
# the field, and the cave which was therein, and all the trees that were in
# the field, that were in all the border thereof round about, were made
# sure"
m.step("Gen.23.17")
# ‹וַיָּקָם שְׂדֵה עֶפְרוֹן› (“and-arise field Ephron”)
# ‹… וְכָל־הָעֵץ … סָבִיב› (“and-all the-tree … circle”)
# — fact holds: and-arise-sdeh-Ephron-in-the-makhpelah; the-field-and-the-
# mearah-and-all-the-tree-circle
m.fact("va_yaqam_sdeh_efron_ba_makhpelah",
       "ha_sadeh_ve_ha_mearah_ve_khol_ha_etz_saviv")
# witness-tier presupposed read: deed_specification_law on
# field_cave_trees_borders — read, not installed
m.witness_read("field_cave_trees_borders", "deed_specification_law",
                cites=["Bereshit Rabbah 58:8"])

# -------------------------- Gen.23.18 · THE_PURCHASE_BEFORE_THE_GATE -------
# ‹לְאַבְרָהָם לְמִקְנָה לְעֵינֵי› (“to-Abraham to-buying to-eye”)
# ‹בְנֵי־חֵת בְּכֹל בָּאֵי› (“son Heth in-all come/bring”)
# ‹שַׁעַר־עִירוֹ› (“gate city-him/its”)
# "unto Abraham for a possession in the presence of the children of Heth,
# before all that went in at the gate of his city."
m.step("Gen.23.18")
# ‹לְאַבְרָהָם לְמִקְנָה› (“to-Abraham to-buying”)
# — fact holds: to-Abraham-to-miqnah-to-eyes-of-vnei-Heth
m.fact("le_avraham_le_miqnah_le_einei_vnei_chet")
# witness-tier presupposed read: standing_title_against_future_claim on
# purchase_on_the_record — read, not installed
m.witness_read("purchase_on_the_record", "standing_title_against_future_claim",
                cites=["Bereshit Rabbah 79:7"])

# -------------------------- Gen.23.19 · CYCLE_B_THE_BURIAL -----------------
# ‹וְאַחֲרֵי־כֵן קָבַר אַבְרָהָם› (“and-after so bury Abraham”)
# ‹אֶת־שָׂרָה אִשְׁתּוֹ אֶל־מְעָרַת› (“obj-marker Sarah woman-him/its to
# cavern”)
# ‹שְׂדֵה הַמַּכְפֵּלָה עַל־פְּנֵי› (“field the-Machpelah over face”)
# ‹מַמְרֵא הִוא חֶבְרוֹן› (“Mamre he/it Hebron”)
# ‹בְּאֶרֶץ כְּנָעַן› (“in-earth Canaan”)
# "And after this, Abraham buried Sarah his wife in the cave of the field of
# Machpelah before Mamre—the same is Hebron—in the land of Canaan."
m.step("Gen.23.19")
# ‹קָבַר אַבְרָהָם אֶת־שָׂרָה› (“bury Abraham obj-marker Sarah”)
# ‹אִשְׁתּוֹ› (“woman-him/its”)
# — demand settled (popped from the queue): bury(obj-marker-metekha)
m.result("qevor(et_metekha)", tmark="t2")
# ‹עַל־פְּנֵי מַמְרֵא הִוא› (“over face Mamre he/it”)
# ‹חֶבְרוֹן› (“Hebron”)
# — reads without prior install (flag, not fix): Mamre
m.presupposed("mamre")
# witness-grounded state (its own tier): standing_occupant_registry on
# the_cave
m.witness_state("the_cave", "standing_occupant_registry",
                cites=["Bereshit Rabbah 58:4", "Bereshit Rabbah 58:8"])

# -------------------------- Gen.23.20 · THE_CONVEYANCE_CODA ----------------
# ‹וַיָּקָם הַשָּׂדֶה וְהַמְּעָרָה› (“and-arise the-field and-the-cavern”)
# ‹אֲשֶׁר־בּוֹ לְאַבְרָהָם לַאֲחֻזַּת־קָבֶר› (“which in-him/its to-Abraham
# to-something-seized sepulchre”)
# ‹מֵאֵת בְּנֵי־חֵת› (“from-with son Heth”)
# "And the field, and the cave that is therein, were made sure unto Abraham
# for a possession of a burying-place by the children of Heth."
m.step("Gen.23.20")
# ‹וַיָּקָם הַשָּׂדֶה … לַאֲחֻזַּת־קָבֶר› (“and-arise the-field … to-
# something-seized sepulchre”)
# — fact holds: and-arise-the-field-to-something-seized-sepulchre-from-obj-
# marker-sons-of-Heth
m.fact("va_yaqam_ha_sadeh_la_achuzat_qaver_me_et_bnei_chet")
# witness-tier presupposed read: ten_and_every_one_a_title_mention on
# sons_of_chet_census — read, not installed
m.witness_read("sons_of_chet_census", "ten_and_every_one_a_title_mention",
                cites=["Bereshit Rabbah 58:8"])

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
    assert sorted(m.WORLD["witnessed"]) == ['the_cave']
    assert m.WORLD["witnessed"]['the_cave']["cites"] == ['Bereshit Rabbah 58:4', 'Bereshit Rabbah 58:8']
    assert all('standing_occupant_registry' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('split_lifespan', 'parsed_clause_against_clause'), ('one_hundred_twenty_seven', 'inheritance_wire_to_a_later_reign'), ('came_to_mourn', 'cause_supplied_by_adjacency'), ('lispod_le_sarah', 'eulogy_question'), ('rose_from_before_his_dead', 'mourner_exemption_law_seated_here'), ('me_al_pene_meto', 'premourner_exemption'), ('prince_of_God', 'honorific_solved_two_ways'), ('defective_participle_sitting', 'seated_that_very_day'), ('hear_me_idiom', 'rendered_as_offer_and_acceptance'), ('qach_mimeni', 'betrothal_money_machine'), ('vendor_name_defective_at_the_weighing', 'diminished_where_he_takes_the_silver'), ('four_hundred_shekels', 'weight_table_applied_not_quoted'), ('over_la_socher', 'deed_file'), ('field_cave_trees_borders', 'deed_specification_law'), ('purchase_on_the_record', 'standing_title_against_future_claim'), ('sons_of_chet_census', 'ten_and_every_one_a_title_mention')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 58:1']
    assert all('parsed_clause_against_clause' not in f for f in m.WORLD["facts"])
    assert 'split_lifespan' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 58:3']
    assert all('inheritance_wire_to_a_later_reign' not in f for f in m.WORLD["facts"])
    assert 'one_hundred_twenty_seven' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 58:5']
    assert all('cause_supplied_by_adjacency' not in f for f in m.WORLD["facts"])
    assert 'came_to_mourn' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sanhedrin 46b:20', 'Sanhedrin 46b:21', 'Sanhedrin 46b:22']
    assert all('eulogy_question' not in f for f in m.WORLD["facts"])
    assert 'lispod_le_sarah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 58:6', 'Mishnah Berakhot 3:1']
    assert all('mourner_exemption_law_seated_here' not in f for f in m.WORLD["facts"])
    assert 'rose_from_before_his_dead' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Berakhot 18a:2', 'Berakhot 18a:3', 'Berakhot 18a:4']
    assert all('premourner_exemption' not in f for f in m.WORLD["facts"])
    assert 'me_al_pene_meto' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Onkelos Genesis 23:6', 'Bereshit Rabbah 43:5']
    assert all('honorific_solved_two_ways' not in f for f in m.WORLD["facts"])
    assert 'prince_of_God' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 58:7']
    assert all('seated_that_very_day' not in f for f in m.WORLD["facts"])
    assert 'defective_participle_sitting' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 23:13', 'Onkelos Genesis 23:8']
    assert all('rendered_as_offer_and_acceptance' not in f for f in m.WORLD["facts"])
    assert 'hear_me_idiom' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Kiddushin 2a:3', 'Kiddushin 2a:4', 'Kiddushin 2a:5', 'Kiddushin 4b:2', 'Kiddushin 4b:3', 'Kiddushin 4b:4', 'Kiddushin 11b:4', 'Kiddushin 11b:5', 'Kiddushin 11b:6']
    assert all('betrothal_money_machine' not in f for f in m.WORLD["facts"])
    assert 'qach_mimeni' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 58:7']
    assert all('diminished_where_he_takes_the_silver' not in f for f in m.WORLD["facts"])
    assert 'vendor_name_defective_at_the_weighing' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Onkelos Genesis 23:16', 'Bereshit Rabbah 58:7']
    assert all('weight_table_applied_not_quoted' not in f for f in m.WORLD["facts"])
    assert 'four_hundred_shekels' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bava Batra 69b:1', 'Bava Batra 69b:2', 'Bekhorot 50a:7', 'Bekhorot 50a:8', 'Bekhorot 50a:9']
    assert all('deed_file' not in f for f in m.WORLD["facts"])
    assert 'over_la_socher' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Bereshit Rabbah 58:8']
    assert all('deed_specification_law' not in f for f in m.WORLD["facts"])
    assert 'field_cave_trees_borders' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Bereshit Rabbah 79:7']
    assert all('standing_title_against_future_claim' not in f for f in m.WORLD["facts"])
    assert 'purchase_on_the_record' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[15]["cites"] == ['Bereshit Rabbah 58:8']
    assert all('ten_and_every_one_a_title_mention' not in f for f in m.WORLD["facts"])
    assert 'sons_of_chet_census' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
