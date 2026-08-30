#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_40_servant_oath_well — 24:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_40_servant_oath_well.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The servant's oath and the well (24:1-33)"""
from machine import Machine

m = Machine("gen_40_servant_oath_well")

# -------------------------- Gen.24.1 · THE_OLD_AND_THE_BLESSED -------------
# וְאַבְרָהָ֣ם זָקֵ֔ן בָּ֖א בַּיָּמִ֑ים וַֽיהוָ֛ה בֵּרַ֥ךְ אֶת־אַבְרָהָ֖ם
# בַּכֹּֽל
# "[EN-AID] And Abraham was old, advanced in days; and YHWH had blessed
# Abraham in all."
m.step("Gen.24.1")
# ‹אַבְרָהָם … יְהוָה› (“Abraham … YHWH”) — reads without prior install
# (flag, not fix): Abraham, the-LORD
m.presupposed("avraham", "YHWH")
# ‹זָקֵן בָּא בַּיָּמִים … בֵּרַךְ אֶת־אַבְרָהָם בַּכֹּל› (“be-old
# come/bring in-day … bless obj-marker Abraham in-all”) — fact holds:
# Abraham-be-old-come/bring-come/bring-seas; the-LORD-bless-obj-marker-
# Abraham-come/bring-all
m.fact("avraham_zaqen_ba_ba_yamim",
       "YHWH_berakh_et_avraham_ba_kol")
# witness-tier presupposed read: chain_premise_not_carried_by_our_ink on
# first_aging_census — read, not installed
m.witness_read("first_aging_census", "chain_premise_not_carried_by_our_ink",
                cites=["Bereshit Rabbah 65:9"])
# witness-tier presupposed read: read_as_a_compressed_sentence on
# the_word_old — read, not installed
m.witness_read("the_word_old", "read_as_a_compressed_sentence",
                cites=["Bereshit Rabbah 59:6"])
# witness-tier presupposed read: four_way_dispute_wired_to_two_blocks on
# blessed_with_everything — read, not installed
m.witness_read("blessed_with_everything", "four_way_dispute_wired_to_two_blocks",
                cites=["Bereshit Rabbah 59:7", "Bereshit Rabbah 43:8"])

# -------------------------- Gen.24.2 · THE_THIGH_GESTURE_DEMAND ------------
# וַיֹּ֣אמֶר אַבְרָהָ֗ם אֶל־עַבְדּוֹ֙ זְקַ֣ן בֵּית֔וֹ הַמֹּשֵׁ֖ל
# בְּכָל־אֲשֶׁר־ל֑וֹ שִֽׂים־נָ֥א יָדְךָ֖ תַּ֥חַת יְרֵכִֽי
# "[EN-AID] And Abraham said to his servant, the elder of his house, who
# ruled over all that was his: Place, please, your hand under my thigh."
m.step("Gen.24.2")
# ‹וַיֹּאמֶר אַבְרָהָם אֶל־עַבְדּוֹ› (“and-say Abraham to servant-him/its”)
# — event: say — agent Abraham
m.event("say", agent="avraham")
# ‹עַבְדּוֹ … הַמֹּשֵׁל בְּכָל־אֲשֶׁר־לוֹ› (“servant-him/its … the-rule in-
# all which to-him/its”) — the world gains: the-servant
m.install("ha_eved")
# ‹שִׂים־נָא יָדְךָ תַּחַת יְרֵכִי› (“put/set please hand-you/your under
# thigh-me/my”) — Abraham speaks a demand — LET: put/set(the-servant, yad-
# under-thigh)
m.declare("avraham", "LET",
          "sim(ha_eved, yad_tachat_yerekh)")
# witness-tier presupposed read: oath_object_procedure on
# hand_under_the_thigh — read, not installed
m.witness_read("hand_under_the_thigh", "oath_object_procedure",
                cites=["Bereshit Rabbah 59:8"])

# -------------------------- Gen.24.3 · THE_OATH_FRAME_AND_THE_NOT_TAKE -----
# וְאַשְׁבִּ֣יעֲךָ֔ בַּֽיהוָה֙ אֱלֹהֵ֣י הַשָּׁמַ֔יִם וֵֽאלֹהֵ֖י הָאָ֑רֶץ
# אֲשֶׁ֨ר לֹֽא־תִקַּ֤ח אִשָּׁה֙ לִבְנִ֔י מִבְּנוֹת֙ הַֽכְּנַעֲנִ֔י אֲשֶׁ֥ר
# אָנֹכִ֖י יוֹשֵׁ֥ב בְּקִרְבּֽוֹ
# "[EN-AID] And I will make you swear by YHWH, God of the heavens and God of
# the earth, that you shall not take a wife for my son from the daughters of
# the Canaanite among whom I dwell."
m.step("Gen.24.3")
# ‹וְאַשְׁבִּיעֲךָ בַּיהוָה› (“and-swear-you/your in-YHWH”) — fact holds:
# and-ashbia-you/your-come/bring-the-LORD
m.fact("ve_ashbia_kha_ba_YHWH")
# ‹לֹא־תִקַּח אִשָּׁה לִבְנִי מִבְּנוֹת הַכְּנַעֲנִי› (“not take woman to-
# son-me/my from-daughter the-Kenaanite”) — fact holds: not-take-woman-to-
# me-veni-who?-daughter-the-Kenaanite
m.fact("lo_tiqach_isha_li_veni_mi_benot_ha_kenaani")
# witness-tier presupposed read: reverence_buffer_supplies_the_object on
# oath_by_the_word — read, not installed
m.witness_read("oath_by_the_word", "reverence_buffer_supplies_the_object",
                cites=["Onkelos Genesis 24:3"])
# witness-tier presupposed read: biography_read_off_an_ink_difference on
# double_divine_title — read, not installed
m.witness_read("double_divine_title", "biography_read_off_an_ink_difference",
                cites=["Bereshit Rabbah 59:8"])

# -------------------------- Gen.24.4 · THE_GO_AND_THE_TAKE_DUTY ------------
# כִּ֧י אֶל־אַרְצִ֛י וְאֶל־מוֹלַדְתִּ֖י תֵּלֵ֑ךְ וְלָקַחְתָּ֥ אִשָּׁ֖ה
# לִבְנִ֥י לְיִצְחָֽק
# "[EN-AID] But to my land and to my kindred you shall go, and you shall
# take a wife for my son, for Isaac."
m.step("Gen.24.4")
# ‹אֶל־אַרְצִי וְאֶל־מוֹלַדְתִּי תֵּלֵךְ› (“to earth-me/my and-to nativity-
# me/my go”) — fact holds: go-to-artzi-and-to-moladti
m.fact("telekh_el_artzi_ve_el_moladti")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי לְיִצְחָק› (“and-take woman to-son-me/my to-
# Isaac”) — fact holds: take(the-servant, woman-to-me-Isaac)
m.fact("laqachta(ha_eved, isha_li_yitzchaq)")

# -------------------------- Gen.24.5 · THE_SERVANT_ASKS_THE_RETURN_CASE ----
# וַיֹּ֤אמֶר אֵלָיו֙ הָעֶ֔בֶד אוּלַי֙ לֹא־תֹאבֶ֣ה הָֽאִשָּׁ֔ה לָלֶ֥כֶת
# אַחֲרַ֖י אֶל־הָאָ֣רֶץ הַזֹּ֑את הֶֽהָשֵׁ֤ב אָשִׁיב֙ אֶת־בִּנְךָ֔
# אֶל־הָאָ֖רֶץ אֲשֶׁר־יָצָ֥אתָ מִשָּֽׁם
# "[EN-AID] And the servant said to him: Perhaps the woman will not be
# willing to follow me to this land; shall I indeed bring your son back to
# the land from which you came?"
m.step("Gen.24.5")
# ‹וַיֹּאמֶר אֵלָיו הָעֶבֶד› (“and-say to-him/its the-servant”) — event: say
# — agent the-servant
m.event("say", agent="ha_eved")
# ‹אוּלַי לֹא־תֹאבֶה … הֶהָשֵׁב אָשִׁיב› (“if-not not breathe-after … the-
# return return”) — fact holds: if-not-not-breathe-after-the-woman-to-go;
# question-he-hashev-return
m.fact("ulay_lo_tove_ha_isha_la_lekhet",
       "question_he_hashev_ashiv")

# -------------------------- Gen.24.6 · THE_GUARD_LEST_YOU_RETURN -----------
# וַיֹּ֥אמֶר אֵלָ֖יו אַבְרָהָ֑ם הִשָּׁ֣מֶר לְךָ֔ פֶּן־תָּשִׁ֥יב אֶת־בְּנִ֖י
# שָֽׁמָּה
# "[EN-AID] And Abraham said to him: Guard yourself, lest you return my son
# there."
m.step("Gen.24.6")
# ‹וַיֹּאמֶר אֵלָיו אַבְרָהָם› (“and-say to-him/its Abraham”) — event: say —
# agent Abraham
m.event("say", agent="avraham")
# ‹הִשָּׁמֶר לְךָ פֶּן־תָּשִׁיב אֶת־בְּנִי שָׁמָּה› (“keep/guard to-you/your
# lest return obj-marker son-me/my there-ward”) — Abraham speaks a demand —
# LET: keep/guard(the-servant, lest-return-obj-marker-beni-shama)
m.declare("avraham", "LET",
          "hishamer(ha_eved, pen_tashiv_et_beni_shama)")

# -------------------------- Gen.24.7 · THE_PAST_OATH_AND_THE_ANGEL_PROMISE -
# יְהוָ֣ה אֱלֹהֵ֣י הַשָּׁמַ֗יִם אֲשֶׁ֨ר לְקָחַ֜נִי מִבֵּ֣ית אָבִי֮
# וּמֵאֶ֣רֶץ מֽוֹלַדְתִּי֒ וַאֲשֶׁ֨ר דִּבֶּר־לִ֜י וַאֲשֶׁ֤ר נִֽשְׁבַּֽע־לִי֙
# לֵאמֹ֔ר לְזַ֨רְעֲךָ֔ אֶתֵּ֖ן אֶת־הָאָ֣רֶץ הַזֹּ֑את ה֗וּא יִשְׁלַ֤ח
# מַלְאָכוֹ֙ לְפָנֶ֔יךָ וְלָקַחְתָּ֥ אִשָּׁ֛ה לִבְנִ֖י מִשָּֽׁם
# "[EN-AID] YHWH, God of the heavens, who took me from my father's house and
# from the land of my kindred, and who spoke to me and who swore to me,
# saying, To your seed I will give this land — He will send His angel before
# you, and you shall take a wife for my son from there."
m.step("Gen.24.7")
# ‹נִשְׁבַּע־לִי … אֶתֵּן אֶת־הָאָרֶץ הַזֹּאת› (“swear to-me/my … set obj-
# marker the-earth the-this”) — fact holds: past-oath-swear-to-me; quoted-
# set-to-zara-you/your
m.fact("past_oath_nishba_li",
       "quoted_eten_le_zara_kha")
# ‹הוּא יִשְׁלַח מַלְאָכוֹ לְפָנֶיךָ› (“he/it send messenger-him/its to-
# face-you/your”) — fact holds: send-malakh-o-to-fane-you/your
m.fact("yishlach_malakh_o_le_fane_kha")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי מִשָּׁם› (“and-take woman to-son-me/my from-
# there”) — fact holds: take(the-servant, woman-to-me-veni-who?-there)
m.fact("laqachta(ha_eved, isha_li_veni_mi_sham)")
# witness-tier presupposed read: registry_of_prior_events on oath_preamble —
# read, not installed
m.witness_read("oath_preamble", "registry_of_prior_events",
                cites=["Bereshit Rabbah 59:10"])

# -------------------------- Gen.24.8 · THE_RELEASE_CONDITION ---------------
# וְאִם־לֹ֨א תֹאבֶ֤ה הָֽאִשָּׁה֙ לָלֶ֣כֶת אַחֲרֶ֔יךָ וְנִקִּ֕יתָ
# מִשְּׁבֻעָתִ֖י זֹ֑את רַ֣ק אֶת־בְּנִ֔י לֹ֥א תָשֵׁ֖ב שָֽׁמָּה
# "[EN-AID] And if the woman is not willing to follow you, then you shall be
# free from this my oath; only my son you shall not return there."
m.step("Gen.24.8")
# ‹וְאִם־לֹא תֹאבֶה … וְנִקִּיתָ מִשְּׁבֻעָתִי זֹאת› (“and-if not breathe-
# after … and-be-clean from-something-sworn-me/my this”) — fact holds:
# release-if-not-breathe-after-then-be-clean-who?-shevuah
m.fact("release_if_lo_tove_then_niqita_mi_shevuah")
# ‹רַק אֶת־בְּנִי לֹא תָשֵׁב שָׁמָּה› (“leanness obj-marker son-me/my not
# return there-ward”) — fact holds: leanness-obj-marker-beni-not-return-
# shama
m.fact("raq_et_beni_lo_tashev_shama")

# -------------------------- Gen.24.9 · THE_THIGH_POP_AND_THE_SWEAR ---------
# וַיָּ֤שֶׂם הָעֶ֨בֶד֙ אֶת־יָד֔וֹ תַּ֛חַת יֶ֥רֶךְ אַבְרָהָ֖ם אֲדֹנָ֑יו
# וַיִּשָּׁ֣בַֽע ל֔וֹ עַל־הַדָּבָ֖ר הַזֶּֽה
# "[EN-AID] And the servant placed his hand under the thigh of Abraham his
# master, and swore to him concerning this matter."
m.step("Gen.24.9")
# ‹וַיָּשֶׂם הָעֶבֶד אֶת־יָדוֹ תַּחַת יֶרֶךְ אַבְרָהָם› (“and-put/set the-
# servant obj-marker hand-him/its under thigh Abraham”) — demand settled
# (popped from the queue): put/set(the-servant, yad-under-thigh)
m.result("sim(ha_eved, yad_tachat_yerekh)", tmark="t1")
# ‹וַיִּשָּׁבַע לוֹ עַל־הַדָּבָר הַזֶּה› (“and-swear to-him/its over the-
# word/thing the-this”) — event: swear — agent the-servant; theme the-
# word/thing-the-this
m.event("swear", agent="ha_eved", themes=["ha_davar_ha_ze"])

# -------------------------- Gen.24.10 · THE_JOURNEY_TO_ARAM_NAHARAYIM ------
# וַיִּקַּ֣ח הָ֠עֶבֶד עֲשָׂרָ֨ה גְמַלִּ֜ים מִגְּמַלֵּ֤י אֲדֹנָיו֙ וַיֵּ֔לֶךְ
# וְכָל־ט֥וּב אֲדֹנָ֖יו בְּיָד֑וֹ וַיָּ֗קָם וַיֵּ֛לֶךְ אֶל־אֲרַ֥ם
# נַֽהֲרַ֖יִם אֶל־עִ֥יר נָחֽוֹר
# "[EN-AID] And the servant took ten camels from his master's camels and
# went, with all his master's goods in his hand; and he rose and went to
# Aram-naharayim, to the city of Nahor."
m.step("Gen.24.10")
# ‹וַיִּקַּח … וַיֵּלֶךְ … וַיָּקָם וַיֵּלֶךְ› (“and-take … and-go … and-
# arise and-go”) — event: take-go-rise-go — agent the-servant; theme camel-
# good
m.event("take_go_rise_go", agent="ha_eved", themes=["gemalim_tuv"])
# ‹אֲרַם נַהֲרַיִם … עִיר נָחוֹר› (“Aham-naharaim … city Nahor”) — reads
# without prior install (flag, not fix): aram-Aham-naharaim, city-Nahor
m.presupposed("aram_naharayim", "ir_nachor")

# -------------------------- Gen.24.11 · THE_CAMELS_AT_THE_WELL -------------
# וַיַּבְרֵ֧ךְ הַגְּמַלִּ֛ים מִח֥וּץ לָעִ֖יר אֶל־בְּאֵ֣ר הַמָּ֑יִם לְעֵ֣ת
# עֶ֔רֶב לְעֵ֖ת צֵ֥את הַשֹּׁאֲבֹֽת
# "[EN-AID] And he made the camels kneel outside the city by the well of
# water, at evening time, the time the water-drawers go out."
m.step("Gen.24.11")
# ‹וַיַּבְרֵךְ הַגְּמַלִּים … אֶל־בְּאֵר הַמָּיִם› (“and-bless the-camel …
# to pit the-waters”) — event: kneel-camels — agent the-servant; theme the-
# camel
m.event("kneel_camels", agent="ha_eved", themes=["ha_gemalim"])
# witness-tier presupposed read: one_verb_three_readings_and_a_collision on
# made_the_camels_kneel — read, not installed
m.witness_read("made_the_camels_kneel", "one_verb_three_readings_and_a_collision",
                cites=["Bereshit Rabbah 59:11", "Bereshit Rabbah 60:8", "Onkelos Genesis 24:11", "Mishnah Demai 1:3"])

# -------------------------- Gen.24.12 · THE_PRAYER_IMPERATIVES_AT_YHWH -----
# וַיֹּאמַ֓ר יְהוָ֗ה אֱלֹהֵי֙ אֲדֹנִ֣י אַבְרָהָ֔ם הַקְרֵה־נָ֥א לְפָנַ֖י
# הַיּ֑וֹם וַעֲשֵׂה־חֶ֕סֶד עִ֖ם אֲדֹנִ֥י אַבְרָהָֽם
# "[EN-AID] And he said: YHWH, God of my master Abraham, cause it to happen
# before me today, and do kindness with my master Abraham."
m.step("Gen.24.12")
# ‹וַיֹּאמַר› (“and-say”) — event: say — agent the-servant
m.event("say", agent="ha_eved")
# ‹הַקְרֵה־נָא לְפָנַי הַיּוֹם› (“light-upon please to-face-me/my the-day”)
# — the-servant speaks a demand — LET: haqreh(the-LORD, before-Me-hayom)
m.declare("ha_eved", "LET",
          "haqreh(YHWH, lefanai_hayom)")
# ‹וַעֲשֵׂה־חֶסֶד עִם אֲדֹנִי אַבְרָהָם› (“and-make kindness with lord-me/my
# Abraham”) — the-servant speaks a demand — LET: make-kindness(the-LORD, if-
# adoni-Abraham)
m.declare("ha_eved", "LET",
          "aseh_chesed(YHWH, im_adoni_avraham)")

# -------------------------- Gen.24.13 · THE_STANDING_AT_THE_SPRING ---------
# הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב עַל־עֵ֣ין הַמָּ֑יִם וּבְנוֹת֙ אַנְשֵׁ֣י הָעִ֔יר
# יֹצְאֹ֖ת לִשְׁאֹ֥ב מָֽיִם
# "[EN-AID] Behold, I am standing by the spring of water, and the daughters
# of the men of the city are coming out to draw water."
m.step("Gen.24.13")
# ‹אָנֹכִי נִצָּב … יֹצְאֹת לִשְׁאֹב› (“stand … bring-forth to-bale-up-
# water”) — fact holds: I-stand-over-eye-the-waters; daughters-bring-forth-
# to-me-sheov
m.fact("anokhi_nitzav_al_en_ha_mayim",
       "banot_yotzot_li_sheov")

# -------------------------- Gen.24.14 · THE_DESIGNED_SIGN ------------------
# וְהָיָ֣ה הַֽנַּעֲרָ֗ אֲשֶׁ֨ר אֹמַ֤ר אֵלֶ֨יהָ֙ הַטִּי־נָ֤א כַדֵּךְ֙
# וְאֶשְׁתֶּ֔ה וְאָמְרָ֣ה שְׁתֵ֔ה וְגַם־גְּמַלֶּ֖יךָ אַשְׁקֶ֑ה אֹתָ֤הּ
# הֹכַ֨חְתָּ֙ לְעַבְדְּךָ֣ לְיִצְחָ֔ק וּבָ֣הּ אֵדַ֔ע כִּי־עָשִׂ֥יתָ חֶ֖סֶד
# עִם־אֲדֹנִֽי
# "[EN-AID] And let it be the girl to whom I say, Tip your pitcher please
# that I may drink, and she says, Drink, and I will also water your camels —
# her You have appointed for Your servant, for Isaac; and by her I shall
# know that You have done kindness with my master."
m.step("Gen.24.14")
# ‹הַטִּי־נָא … שְׁתֵה … אַשְׁקֶה› (“stretch please … drink … give-drink”) —
# fact holds: designed-sign-oracle
m.fact("designed_sign_oracle")
# ‹אֹתָהּ הֹכַחְתָּ לְעַבְדְּךָ לְיִצְחָק› (“obj-marker-her/its be-right to-
# servant-you/your to-Isaac”) — fact holds: be-right-appointment-criterion
m.fact("hokhachta_appointment_criterion")
# witness-tier presupposed read: enrolled_in_a_void_vow_class on
# open_conditional_request — read, not installed
m.witness_read("open_conditional_request", "enrolled_in_a_void_vow_class",
                cites=["Bereshit Rabbah 60:3", "Mishnah Temurah 5:6"])

# -------------------------- Gen.24.15 · RIVQAH_APPEARS ---------------------
# וַֽיְהִי־ה֗וּא טֶרֶם֮ כִּלָּ֣ה לְדַבֵּר֒ וְהִנֵּ֧ה רִבְקָ֣ה יֹצֵ֗את
# אֲשֶׁ֤ר יֻלְּדָה֙ לִבְתוּאֵ֣ל בֶּן־מִלְכָּ֔ה אֵ֥שֶׁת נָח֖וֹר אֲחִ֣י
# אַבְרָהָ֑ם וְכַדָּ֖הּ עַל־שִׁכְמָֽהּ
# "[EN-AID] And it was, before he had finished speaking, that behold Rivqah
# was coming out — who was born to Betuel son of Milcah, wife of Nahor
# brother of Abraham — and her pitcher on her shoulder."
m.step("Gen.24.15")
# ‹וַיְהִי … טֶרֶם כִּלָּה לְדַבֵּר וְהִנֵּה רִבְקָה יֹצֵאת› (“and-be … non-
# occurrence be-complete to-speak and-behold Rebekah bring-forth”) — event:
# appear — theme rivqah
m.event("appear", themes=["rivqah"])
# ‹רִבְקָה› (“Rebekah”) — the world gains: rivqah
m.install("rivqah")
# witness-tier presupposed read: answered_before_finishing_census on
# before_he_had_finished_speaking — read, not installed
m.witness_read("before_he_had_finished_speaking", "answered_before_finishing_census",
                cites=["Bereshit Rabbah 60:4"])

# -------------------------- Gen.24.16 · THE_GIRL_ATTRIBUTE_AND_THE_WELL_ACT -
# וְהַֽנַּעֲרָ֗ טֹבַ֤ת מַרְאֶה֙ מְאֹ֔ד בְּתוּלָ֕ה וְאִ֖ישׁ לֹ֣א יְדָעָ֑הּ
# וַתֵּ֣רֶד הָעַ֔יְנָה וַתְּמַלֵּ֥א כַדָּ֖הּ וַתָּֽעַל
# "[EN-AID] And the girl was very fair of appearance, a virgin, and no man
# had known her; and she went down to the spring and filled her pitcher and
# came up."
m.step("Gen.24.16")
# ‹טֹבַת מַרְאֶה› (“good appearance”) — fact holds: good-appearance-
# attribute
m.fact("tovat_mareh_attribute")
# ‹וַתֵּרֶד … וַתְּמַלֵּא … וַתָּעַל› (“and-go-down … and-fill … and-go-up”)
# — event: descend-fill-ascend — agent rivqah
m.event("descend_fill_ascend", agent="rivqah")

# -------------------------- Gen.24.17 · THE_LIVE_SIP_DEMAND ----------------
# וַיָּ֥רָץ הָעֶ֖בֶד לִקְרָאתָ֑הּ וַיֹּ֕אמֶר הַגְמִיאִ֥ינִי נָ֛א
# מְעַט־מַ֖יִם מִכַּדֵּֽךְ
# "[EN-AID] And the servant ran to meet her and said: Let me sip, please, a
# little water from your pitcher."
m.step("Gen.24.17")
# ‹וַיָּרָץ … וַיֹּאמֶר› (“and-run … and-say”) — event: run-say — agent the-
# servant
m.event("run_say", agent="ha_eved")
# ‹הַגְמִיאִינִי נָא› (“absorb-me/my please”) — the-servant speaks a demand
# — LET: hagmiini(rivqah, little-waters)
m.declare("ha_eved", "LET",
          "hagmiini(rivqah, meat_mayim)")

# -------------------------- Gen.24.18 · DRINK_MY_LORD_AND_THE_WATERING -----
# וַתֹּ֖אמֶר שְׁתֵ֣ה אֲדֹנִ֑י וַתְּמַהֵ֗ר וַתֹּ֧רֶד כַּדָּ֛הּ עַל־יָדָ֖הּ
# וַתַּשְׁקֵֽהוּ
# "[EN-AID] And she said: Drink, my lord; and she hurried and lowered her
# pitcher on her hand and gave him drink."
m.step("Gen.24.18")
# ‹שְׁתֵה אֲדֹנִי› (“drink lord-me/my”) — rivqah speaks a demand — LET:
# drink(the-servant)
m.declare("rivqah", "LET",
          "shete(ha_eved)")
# ‹וַתְּמַהֵר … וַתַּשְׁקֵהוּ› (“and-hasten … and-give-drink-him/its”) —
# event: water — agent rivqah
m.event("water", agent="rivqah")

# -------------------------- Gen.24.19 · THE_OVERPERFORMANCE_PROMISE --------
# וַתְּכַ֖ל לְהַשְׁקֹת֑וֹ וַתֹּ֗אמֶר גַּ֤ם לִגְמַלֶּ֨יךָ֙ אֶשְׁאָ֔ב עַ֥ד
# אִם־כִּלּ֖וּ לִשְׁתֹּֽת
# "[EN-AID] And she finished giving him drink, and said: Also for your
# camels I will draw until they have finished drinking."
m.step("Gen.24.19")
# ‹וַתְּכַל לְהַשְׁקֹתוֹ› (“and-be-complete to-give-drink-him/its”) — event:
# finish-watering — agent rivqah
m.event("finish_watering", agent="rivqah")
# ‹גַּם לִגְמַלֶּיךָ אֶשְׁאָב› (“also to-camel-you/your bale-up-water”) —
# fact holds: promise-bale-up-water-to-me-camel-you/your
m.fact("promise_eshav_li_gemale_kha")

# -------------------------- Gen.24.20 · THE_CAMELS_WATERED -----------------
# וַתְּמַהֵ֗ר וַתְּעַ֤ר כַּדָּהּ֙ אֶל־הַשֹּׁ֔קֶת וַתָּ֥רָץ ע֛וֹד
# אֶֽל־הַבְּאֵ֖ר לִשְׁאֹ֑ב וַתִּשְׁאַ֖ב לְכָל־גְּמַלָּֽיו
# "[EN-AID] And she hurried and emptied her pitcher into the trough and ran
# again to the well to draw, and she drew for all his camels."
m.step("Gen.24.20")
# ‹וַתְּמַהֵר וַתְּעַר … וַתָּרָץ … וַתִּשְׁאַב› (“and-hasten and-be-bare …
# and-run … and-bale-up-water”) — event: empty-run-draw — agent rivqah;
# theme all-camels
m.event("empty_run_draw", agent="rivqah", themes=["all_camels"])

# -------------------------- Gen.24.21 · THE_SILENT_GAZE --------------------
# וְהָאִ֥ישׁ מִשְׁתָּאֵ֖ה לָ֑הּ מַחֲרִ֕ישׁ לָדַ֗עַת הַֽהִצְלִ֧יחַ יְהוָ֛ה
# דַּרְכּ֖וֹ אִם־לֹֽא
# "[EN-AID] And the man was gazing at her, keeping silent, to know whether
# YHWH had prospered his way or not."
m.step("Gen.24.21")
# ‹מִשְׁתָּאֵה … מַחֲרִישׁ … הַהִצְלִיחַ› (“stun … scratch … the-push-
# forward”) — fact holds: gazing-silent-wonder
m.fact("gazing_silent_wonder")
# witness-tier presupposed read: rendered_as_observation_protocol on
# astonished_at_her — read, not installed
m.witness_read("astonished_at_her", "rendered_as_observation_protocol",
                cites=["Onkelos Genesis 24:21"])

# -------------------------- Gen.24.22 · THE_GIFTS_OF_GOLD ------------------
# וַיְהִ֗י כַּאֲשֶׁ֨ר כִּלּ֤וּ הַגְּמַלִּים֙ לִשְׁתּ֔וֹת וַיִּקַּ֤ח הָאִישׁ֙
# נֶ֣זֶם זָהָ֔ב בֶּ֖קַע מִשְׁקָל֑וֹ וּשְׁנֵ֤י צְמִידִים֙ עַל־יָדֶ֔יהָ
# עֲשָׂרָ֥ה זָהָ֖ב מִשְׁקָלָֽם
# "[EN-AID] And when the camels had finished drinking, the man took a gold
# nose-ring, a beqa its weight, and two bracelets on her hands, ten of gold
# their weight."
m.step("Gen.24.22")
# ‹וַיִּקַּח … נֶזֶם … צְמִידִים› (“and-take … nose-ring … bracelet”) —
# event: take-gifts — agent the-servant; theme nose-ring-tzamid
m.event("take_gifts", agent="ha_eved", themes=["nezem_tzamid"])
# witness-tier presupposed read: numeric_foreshadow_by_weight_and_count on
# betrothal_gifts — read, not installed
m.witness_read("betrothal_gifts", "numeric_foreshadow_by_weight_and_count",
                cites=["Bereshit Rabbah 60:6"])

# -------------------------- Gen.24.23 · TELL_ME_WHOSE_DAUGHTER -------------
# וַיֹּ֨אמֶר֙ בַּת־מִ֣י אַ֔תְּ הַגִּ֥ידִי נָ֖א לִ֑י הֲיֵ֧שׁ בֵּית־אָבִ֛יךְ
# מָק֥וֹם לָ֖נוּ לָלִֽין
# "[EN-AID] And he said: Whose daughter are you? Tell me, please. Is there
# in your father's house a place for us to lodge?"
m.step("Gen.24.23")
# ‹וַיֹּאמֶר› (“and-say”) — event: say — agent the-servant
m.event("say", agent="ha_eved")
# ‹הַגִּידִי נָא לִי› (“tell please to-me/my”) — the-servant speaks a demand
# — LET: tell(rivqah, daughter-who?)
m.declare("ha_eved", "LET",
          "hagidi(rivqah, bat_mi)")

# -------------------------- Gen.24.24 · THE_LINEAGE_ANSWER -----------------
# וַתֹּ֣אמֶר אֵלָ֔יו בַּת־בְּתוּאֵ֖ל אָנֹ֑כִי בֶּן־מִלְכָּ֕ה אֲשֶׁ֥ר
# יָלְדָ֖ה לְנָחֽוֹר
# "[EN-AID] And she said to him: I am the daughter of Betuel, son of Milcah,
# whom she bore to Nahor."
m.step("Gen.24.24")
# ‹וַתֹּאמֶר› (“and-say”) — event: say — agent rivqah
m.event("say", agent="rivqah")
# ‹בַּת־בְּתוּאֵל … לְנָחוֹר› (“daughter Bethuel … to-Nahor”) — fact holds:
# rivqah-daughter-Bethuel-line
m.fact("rivqah_bat_betuel_line")

# -------------------------- Gen.24.25 · STRAW_AND_FODDER_AND_ROOM ----------
# וַתֹּ֣אמֶר אֵלָ֔יו גַּם־תֶּ֥בֶן גַּם־מִסְפּ֖וֹא רַ֣ב עִמָּ֑נוּ
# גַּם־מָק֖וֹם לָלֽוּן
# "[EN-AID] And she said to him: Also straw, also fodder, much with us; also
# a place to lodge."
m.step("Gen.24.25")
# ‹וַתֹּאמֶר› (“and-say”) — event: say — agent rivqah
m.event("say", agent="rivqah")

# -------------------------- Gen.24.26 · THE_BOW_TO_YHWH --------------------
# וַיִּקֹּ֣ד הָאִ֔ישׁ וַיִּשְׁתַּ֖חוּ לַֽיהוָֽה
# "[EN-AID] And the man bowed the head and prostrated himself to YHWH."
m.step("Gen.24.26")
# ‹וַיִּקֹּד … וַיִּשְׁתַּחוּ לַיהוָה› (“and-shrivel-up … and-afflict to-
# YHWH”) — event: bow-prostrate — agent the-servant
m.event("bow_prostrate", agent="ha_eved")

# -------------------------- Gen.24.27 · BLESSED_BE_YHWH_KINDNESS_AND_TRUTH -
# וַיֹּ֗אמֶר בָּר֤וּךְ יְהוָה֙ אֱלֹהֵי֙ אֲדֹנִ֣י אַבְרָהָ֔ם אֲ֠שֶׁר
# לֹֽא־עָזַ֥ב חַסְדּ֛וֹ וַאֲמִתּ֖וֹ מֵעִ֣ם אֲדֹנִ֑י אָנֹכִ֗י בַּדֶּ֨רֶךְ֙
# נָחַ֣נִי יְהוָ֔ה בֵּ֖ית אֲחֵ֥י אֲדֹנִֽי
# "[EN-AID] And he said: Blessed be YHWH, God of my master Abraham, who has
# not forsaken His kindness and His truth from with my master; I being on
# the way, YHWH led me to the house of my master's brothers."
m.step("Gen.24.27")
# ‹וַיֹּאמֶר› (“and-say”) — event: say — agent the-servant
m.event("say", agent="ha_eved")
# ‹בָּרוּךְ יְהוָה … חַסְדּוֹ וַאֲמִתּוֹ› (“bless YHWH … kindness-him/its
# and-stability-him/its”) — fact holds: bless-the-LORD-kindness-and-emet
m.fact("barukh_YHWH_chesed_ve_emet")

# -------------------------- Gen.24.28 · SHE_RUNS_AND_TELLS -----------------
# וַתָּ֨רָץ֙ הַֽנַּעֲרָ֔ וַתַּגֵּ֖ד לְבֵ֣ית אִמָּ֑הּ כַּדְּבָרִ֖ים הָאֵֽלֶּה
# "[EN-AID] And the girl ran and told her mother's household these things."
m.step("Gen.24.28")
# ‹וַתָּרָץ … וַתַּגֵּד› (“and-run … and-tell”) — event: run-tell — agent
# rivqah
m.event("run_tell", agent="rivqah")

# -------------------------- Gen.24.29 · LABAN_RUNS -------------------------
# וּלְרִבְקָ֥ה אָ֖ח וּשְׁמ֣וֹ לָבָ֑ן וַיָּ֨רָץ לָבָ֧ן אֶל־הָאִ֛ישׁ הַח֖וּצָה
# אֶל־הָעָֽיִן
# "[EN-AID] And Rivqah had a brother, and his name was Laban; and Laban ran
# to the man outside, to the spring."
m.step("Gen.24.29")
# ‹וּשְׁמוֹ לָבָן› (“and-name-him/its Laban”) — the world gains: Laban
m.install("lavan")

# -------------------------- Gen.24.30 · HE_SEES_THE_GIFTS_AND_COMES --------
# וַיְהִ֣י כִּרְאֹ֣ת אֶת־הַנֶּ֗זֶם וְֽאֶת־הַצְּמִדִים֮ עַל־יְדֵ֣י אֲחֹתוֹ֒
# וּכְשָׁמְע֗וֹ אֶת־דִּבְרֵ֞י רִבְקָ֤ה אֲחֹתוֹ֙ לֵאמֹ֔ר כֹּֽה־דִבֶּ֥ר אֵלַ֖י
# הָאִ֑ישׁ וַיָּבֹא֙ אֶל־הָאִ֔ישׁ וְהִנֵּ֛ה עֹמֵ֥ד עַל־הַגְּמַלִּ֖ים
# עַל־הָעָֽיִן
# "[EN-AID] And when he saw the nose-ring and the bracelets on his sister's
# hands, and when he heard the words of Rivqah his sister saying, Thus the
# man spoke to me, he came to the man; and behold, standing by the camels at
# the spring."
m.step("Gen.24.30")
# ‹כִּרְאֹת … וּכְשָׁמְעוֹ … וַיָּבֹא› (“like-see … and-like-hear-him/its …
# and-come/bring”) — event: see-hear-come — agent Laban
m.event("see_hear_come", agent="lavan")

# -------------------------- Gen.24.31 · COME_IN_O_BLESSED_OF_YHWH ----------
# וַיֹּ֕אמֶר בּ֖וֹא בְּר֣וּךְ יְהוָ֑ה לָ֤מָּה תַעֲמֹד֙ בַּח֔וּץ וְאָנֹכִי֙
# פִּנִּ֣יתִי הַבַּ֔יִת וּמָק֖וֹם לַגְּמַלִּֽים
# "[EN-AID] And he said: Come in, O blessed of YHWH; why do you stand
# outside? And I have cleared the house, and a place for the camels."
m.step("Gen.24.31")
# ‹בּוֹא› (“come/bring”) — Laban speaks a demand — LET: come/bring(the-
# servant)
m.declare("lavan", "LET",
          "bo(ha_eved)")

# -------------------------- Gen.24.32 · HE_ENTERS_AND_IS_SERVED ------------
# וַיָּבֹ֤א הָאִישׁ֙ הַבַּ֔יְתָה וַיְפַתַּ֖ח הַגְּמַלִּ֑ים וַיִּתֵּ֨ן
# תֶּ֤בֶן וּמִסְפּוֹא֙ לַגְּמַלִּ֔ים וּמַ֨יִם֙ לִרְחֹ֣ץ רַגְלָ֔יו וְרַגְלֵ֥י
# הָאֲנָשִׁ֖ים אֲשֶׁ֥ר אִתּֽוֹ
# "[EN-AID] And the man came to the house and unmuzzled the camels; and he
# gave straw and fodder to the camels, and water to wash his feet and the
# feet of the men who were with him."
m.step("Gen.24.32")
# ‹וַיָּבֹא הָאִישׁ הַבַּיְתָה› (“and-come/bring the-man the-house-ward”) —
# demand settled (popped from the queue): come/bring(the-servant)
m.result("bo(ha_eved)", tmark="t2")
# ‹וַיְפַתַּח … וַיִּתֵּן … לִרְחֹץ› (“and-open-wide … and-set … to-lave”) —
# event: serve-camels-and-feet
m.event("serve_camels_and_feet")

# -------------------------- Gen.24.33 · THE_SEAM_SPEAK_DEMAND --------------
# ויישם וַיּוּשַׂ֤ם לְפָנָיו֙ לֶאֱכֹ֔ל וַיֹּ֨אמֶר֙ לֹ֣א אֹכַ֔ל עַ֥ד
# אִם־דִּבַּ֖רְתִּי דְּבָרָ֑י וַיֹּ֖אמֶר דַּבֵּֽר
# "[EN-AID] And food was set before him to eat; and he said: I will not eat
# until I have spoken my words. And he said: Speak."
m.step("Gen.24.33")
# ‹וַיּוּשַׂם … וַיֹּאמֶר לֹא אֹכַל … וַיֹּאמֶר דַּבֵּר› (“and-put/set …
# and-say not eat … and-say speak”) — event: food-set
m.event("food_set")
# ‹דַּבֵּר› (“speak”) — house-voice speaks a demand — LET: speak(the-
# servant)
m.declare("house_voice", "LET",
          "daber(ha_eved)")
# witness-tier presupposed read: disclosure_before_negotiation on
# will_not_eat_until_I_have_spoken — read, not installed
m.witness_read("will_not_eat_until_I_have_spoken", "disclosure_before_negotiation",
                cites=["Bereshit Rabbah 60:9"])
# witness-grounded state (its own tier): ink_economy_rule_stated_at_its_seat
# on the_repetition_ahead
m.witness_state("the_repetition_ahead", "ink_economy_rule_stated_at_its_seat",
                cites=["Bereshit Rabbah 60:8"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ha_eved', 'lavan', 'rivqah'}
    assert m.presupposed_set() == {'YHWH', 'aram_naharayim', 'avraham', 'ir_nachor'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hishamer(ha_eved, pen_tashiv_et_beni_shama)', 'haqreh(YHWH, lefanai_hayom)', 'aseh_chesed(YHWH, im_adoni_avraham)', 'hagmiini(rivqah, meat_mayim)', 'shete(ha_eved)', 'hagidi(rivqah, bat_mi)', 'daber(ha_eved)']
    assert len(m.SPECS["log"]) == 9
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['avraham_zaqen_ba_ba_yamim', 'YHWH_berakh_et_avraham_ba_kol', 've_ashbia_kha_ba_YHWH', 'lo_tiqach_isha_li_veni_mi_benot_ha_kenaani', 'telekh_el_artzi_ve_el_moladti', 'laqachta(ha_eved, isha_li_yitzchaq)', 'ulay_lo_tove_ha_isha_la_lekhet', 'question_he_hashev_ashiv', 'past_oath_nishba_li', 'quoted_eten_le_zara_kha', 'yishlach_malakh_o_le_fane_kha', 'laqachta(ha_eved, isha_li_veni_mi_sham)', 'release_if_lo_tove_then_niqita_mi_shevuah', 'raq_et_beni_lo_tashev_shama', 'anokhi_nitzav_al_en_ha_mayim', 'banot_yotzot_li_sheov', 'designed_sign_oracle', 'hokhachta_appointment_criterion', 'tovat_mareh_attribute', 'promise_eshav_li_gemale_kha', 'gazing_silent_wonder', 'rivqah_bat_betuel_line', 'barukh_YHWH_chesed_ve_emet'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 34
    assert sorted(m.WORLD["witnessed"]) == ['the_repetition_ahead']
    assert m.WORLD["witnessed"]['the_repetition_ahead']["cites"] == ['Bereshit Rabbah 60:8']
    assert all('ink_economy_rule_stated_at_its_seat' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('first_aging_census', 'chain_premise_not_carried_by_our_ink'), ('the_word_old', 'read_as_a_compressed_sentence'), ('blessed_with_everything', 'four_way_dispute_wired_to_two_blocks'), ('hand_under_the_thigh', 'oath_object_procedure'), ('oath_by_the_word', 'reverence_buffer_supplies_the_object'), ('double_divine_title', 'biography_read_off_an_ink_difference'), ('oath_preamble', 'registry_of_prior_events'), ('made_the_camels_kneel', 'one_verb_three_readings_and_a_collision'), ('open_conditional_request', 'enrolled_in_a_void_vow_class'), ('before_he_had_finished_speaking', 'answered_before_finishing_census'), ('astonished_at_her', 'rendered_as_observation_protocol'), ('betrothal_gifts', 'numeric_foreshadow_by_weight_and_count'), ('will_not_eat_until_I_have_spoken', 'disclosure_before_negotiation')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 65:9']
    assert all('chain_premise_not_carried_by_our_ink' not in f for f in m.WORLD["facts"])
    assert 'first_aging_census' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 59:6']
    assert all('read_as_a_compressed_sentence' not in f for f in m.WORLD["facts"])
    assert 'the_word_old' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 59:7', 'Bereshit Rabbah 43:8']
    assert all('four_way_dispute_wired_to_two_blocks' not in f for f in m.WORLD["facts"])
    assert 'blessed_with_everything' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 59:8']
    assert all('oath_object_procedure' not in f for f in m.WORLD["facts"])
    assert 'hand_under_the_thigh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Onkelos Genesis 24:3']
    assert all('reverence_buffer_supplies_the_object' not in f for f in m.WORLD["facts"])
    assert 'oath_by_the_word' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 59:8']
    assert all('biography_read_off_an_ink_difference' not in f for f in m.WORLD["facts"])
    assert 'double_divine_title' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 59:10']
    assert all('registry_of_prior_events' not in f for f in m.WORLD["facts"])
    assert 'oath_preamble' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 59:11', 'Bereshit Rabbah 60:8', 'Onkelos Genesis 24:11', 'Mishnah Demai 1:3']
    assert all('one_verb_three_readings_and_a_collision' not in f for f in m.WORLD["facts"])
    assert 'made_the_camels_kneel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 60:3', 'Mishnah Temurah 5:6']
    assert all('enrolled_in_a_void_vow_class' not in f for f in m.WORLD["facts"])
    assert 'open_conditional_request' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 60:4']
    assert all('answered_before_finishing_census' not in f for f in m.WORLD["facts"])
    assert 'before_he_had_finished_speaking' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Genesis 24:21']
    assert all('rendered_as_observation_protocol' not in f for f in m.WORLD["facts"])
    assert 'astonished_at_her' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 60:6']
    assert all('numeric_foreshadow_by_weight_and_count' not in f for f in m.WORLD["facts"])
    assert 'betrothal_gifts' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 60:9']
    assert all('disclosure_before_negotiation' not in f for f in m.WORLD["facts"])
    assert 'will_not_eat_until_I_have_spoken' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
