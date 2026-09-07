#!/usr/bin/env python3
# =============================================================================
# gen_41_retelling_release_meeting — 24:34-67
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_41_retelling_release_meeting.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The retelling, the release, and the meeting (24:34-67)"""
from machine import Machine

m = Machine("gen_41_retelling_release_meeting")

# -------------------------- Gen.24.34 · THE_SERVANT_IDENTIFIES -------------
# ‹וַיֹּאמַ֑ר עֶ֥בֶד אַבְרָהָ֖ם› (“and-say servant Abraham”)
# ‹אָנֹֽכִי› (“?”)
# "[EN-AID] And he said: I am Abraham's servant."
m.step("Gen.24.34")
# ‹וַיֹּאמַר› (“and-say”)
# — event: say — agent the-servant
m.event("say", agent="ha_eved")
# ‹עֶבֶד אַבְרָהָם אָנֹכִי› (“servant Abraham”)
# — fact holds: servant-Abraham-anokhi
m.fact("eved_avraham_anokhi")
# ‹עֶבֶד אַבְרָהָם› (“servant Abraham”)
# — reads without prior install (flag, not fix): the-servant, Abraham
m.presupposed("ha_eved", "avraham")

# -------------------------- Gen.24.35 · THE_RETELLING_OF_THE_BLESSING ------
# ‹וַיהוָ֞ה בֵּרַ֧ךְ אֶת־אֲדֹנִ֛י› (“and-YHWH bless obj-marker lord-me/my”)
# ‹מְאֹ֖ד וַיִּגְדָּ֑ל וַיִּתֶּן־ל֞וֹ› (“very and-be-large and-set to-
# him/its”)
# ‹צֹ֤אן וּבָקָר֙ וְכֶ֣סֶף› (“flock and-herd and-silver”)
# ‹וְזָהָ֔ב וַעֲבָדִם֙ וּשְׁפָחֹ֔ת› (“and-gold and-servant and-female-
# slave”)
# ‹וּגְמַלִּ֖ים וַחֲמֹרִֽים› (“and-camel and-male-ass”)
# "[EN-AID] And YHWH has blessed my master greatly, and he has become great;
# and He gave him flocks and herds, silver and gold, male and female
# servants, camels and donkeys."
m.step("Gen.24.35")
# ‹וַיהוָה בֵּרַךְ אֶת־אֲדֹנִי› (“and-YHWH bless obj-marker lord-me/my”)
# ‹… וַיִּתֶּן־לוֹ› (“and-set to-him/its”)
# — fact holds: the-LORD-bless-obj-marker-adoni-very-and-be-large-and-set-
# wealth
m.fact("YHWH_berakh_et_adoni_meod_va_yigdal_va_yiten_wealth")

# -------------------------- Gen.24.36 · THE_RETELLING_OF_THE_HEIR ----------
# ‹וַתֵּ֡לֶד שָׂרָה֩ אֵ֨שֶׁת› (“and-bear-young Sarah woman”)
# ‹אֲדֹנִ֥י בֵן֙ לַֽאדֹנִ֔י› (“lord-me/my son to-lord-me/my”)
# ‹אַחֲרֵ֖י זִקְנָתָ֑הּ וַיִּתֶּן־לּ֖וֹ› (“after old-age-her/its and-set to-
# him/its”)
# ‹אֶת־כָּל־אֲשֶׁר־לֽוֹ› (“obj-marker all which to-him/its”)
# "[EN-AID] And Sarah my master's wife bore a son to my master after her old
# age; and he has given him all that he has."
m.step("Gen.24.36")
# ‹וַתֵּלֶד שָׂרָה … בֵן› (“and-bear-young Sarah … son”)
# ‹… אַחֲרֵי זִקְנָתָהּ וַיִּתֶּן› (“after old-age-her/its and-set”)
# ‹לוֹ אֶת־כָּל־אֲשֶׁר־לוֹ› (“to-him/its obj-marker all which to-him/its”)
# — fact holds: Sarah-bear-young-son-after-ziqnah-and-gave-all
m.fact("sara_teled_ben_achare_ziqnah_and_gave_all")

# -------------------------- Gen.24.37 · THE_RETELLING_OF_THE_NOT_TAKE ------
# ‹וַיַּשְׁבִּעֵ֥נִי אֲדֹנִ֖י לֵאמֹ֑ר› (“and-swear-me/my lord-me/my to-say”)
# ‹לֹא־תִקַּ֤ח אִשָּׁה֙ לִבְנִ֔י› (“not take woman to-son-me/my”)
# ‹מִבְּנוֹת֙ הַֽכְּנַעֲנִ֔י אֲשֶׁ֥ר› (“from-daughter the-Kenaanite which”)
# ‹אָנֹכִ֖י יֹשֵׁ֥ב בְּאַרְצֽוֹ› (“dwell/sit in-earth-him/its”)
# "[EN-AID] And my master made me swear, saying: You shall not take a wife
# for my son from the daughters of the Canaanite among whom I dwell."
m.step("Gen.24.37")
# ‹וַיַּשְׁבִּעֵנִי אֲדֹנִי לֵאמֹר› (“and-swear-me/my lord-me/my to-say”)
# — fact holds: and-yashbie-ni-adoni-to-say
m.fact("va_yashbie_ni_adoni_le_mor")
# ‹לֹא־תִקַּח אִשָּׁה לִבְנִי› (“not take woman to-son-me/my”)
# ‹מִבְּנוֹת הַכְּנַעֲנִי› (“from-daughter the-Kenaanite”)
# — fact holds: not-take-woman-to-me-veni-who?-daughter-the-Kenaanite
m.fact("lo_tiqach_isha_li_veni_mi_benot_ha_kenaani")

# -------------------------- Gen.24.38 · THE_RETELLING_OF_THE_GO_AND_TAKE ---
# ‹אִם־לֹ֧א אֶל־בֵּית־אָבִ֛י תֵּלֵ֖ךְ› (“if not to house father-me/my go”)
# ‹וְאֶל־מִשְׁפַּחְתִּ֑י וְלָקַחְתָּ֥ אִשָּׁ֖ה› (“and-to family-me/my and-
# take woman”)
# ‹לִבְנִֽי› (“to-son-me/my”)
# "[EN-AID] But you shall go to my father's house and to my family, and take
# a wife for my son."
m.step("Gen.24.38")
# ‹אֶל־בֵּית־אָבִי תֵּלֵךְ וְאֶל־מִשְׁפַּחְתִּי› (“to house father-me/my go
# and-to family-me/my”)
# — fact holds: go-to-house-avi-and-to-mishpachti
m.fact("telekh_el_bet_avi_ve_el_mishpachti")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי› (“and-take woman to-son-me/my”)
# — fact holds: and-take-woman-to-me-veni
m.fact("ve_laqachta_isha_li_veni")

# -------------------------- Gen.24.39 · THE_RETELLING_OF_ULAI --------------
# ‹וָאֹמַ֖ר אֶל־אֲדֹנִ֑י אֻלַ֛י› (“and-say to lord-me/my if-not”)
# ‹לֹא־תֵלֵ֥ךְ הָאִשָּׁ֖ה אַחֲרָֽי› (“not go the-woman after-me/my”)
# "[EN-AID] And I said to my master: Perhaps the woman will not follow me."
m.step("Gen.24.39")
# ‹אֻלַי לֹא־תֵלֵךְ הָאִשָּׁה› (“if-not not go the-woman”)
# ‹אַחֲרָי› (“after-me/my”)
# — fact holds: if-not-not-go-the-woman-achara-y-retell
m.fact("ulay_lo_telekh_ha_isha_achara_y_retell")
# witness-tier presupposed read:
# the_giving_the_consent_the_handover_the_gifts_and_the_marriage_formula on
# the_retellings_deltas_are_the_sugyots_ground — read, not installed
m.witness_read("the_retellings_deltas_are_the_sugyots_ground", "the_giving_the_consent_the_handover_the_gifts_and_the_marriage_formula",
                cites=["Mishnah Kiddushin 3:1", "Mishnah Kiddushin 2:6", "Mishnah Ketubot 4:4", "Mishnah Ketubot 4:5", "Mishnah Ketubot 5:1", "Mishnah Ketubot 5:2", "Mishnah Ketubot 1:2", "Kiddushin 50b:4", "Moed Katan 18b:15", "Ketubot 57b:2", "Ketubot 57b:3", "Nedarim 37b:8", "Berakhot 61a:24", "Eruvin 18b:8", "Pesachim 3a:14", "Bava Kamma 92b:9", "Berakhot 26b:6", "Avodah Zarah 7b:14", "Pesachim 88a:4", "Yevamot 61b:13", "Bava Kamma 92b:6"])

# -------------------------- Gen.24.40 · THE_RETELLING_OF_THE_ANGEL_PROMISE -
# ‹וַיֹּ֖אמֶר אֵלָ֑י יְהוָ֞ה› (“and-say to-me/my YHWH”)
# ‹אֲשֶׁר־הִתְהַלַּ֣כְתִּי לְפָנָ֗יו יִשְׁלַ֨ח› (“which walk/go to-face-
# him/its send”)
# ‹מַלְאָכ֤וֹ אִתָּךְ֙ וְהִצְלִ֣יחַ› (“messenger-him/its with-you/your and-
# push-forward”)
# ‹דַּרְכֶּ֔ךָ וְלָקַחְתָּ֤ אִשָּׁה֙› (“way/road-you/your and-take woman”)
# ‹לִבְנִ֔י מִמִּשְׁפַּחְתִּ֖י וּמִבֵּ֥ית› (“to-son-me/my from-family-me/my
# and-from-house”)
# ‹אָבִֽי› (“father-me/my”)
# "[EN-AID] And he said to me: YHWH, before whom I walk, will send His angel
# with you and prosper your way; and you shall take a wife for my son from
# my family and from my father's house."
m.step("Gen.24.40")
# ‹יְהוָה … יִשְׁלַח מַלְאָכוֹ› (“YHWH … send messenger-him/its”)
# ‹… וְלָקַחְתָּ אִשָּׁה› (“and-take woman”)
# — fact holds: retold-angel-promise-and-take-from-family
m.fact("retold_angel_promise_and_take_from_family")

# -------------------------- Gen.24.41 · THE_ALAH_DELTA_RELEASE -------------
# ‹אָ֤ז תִּנָּקֶה֙ מֵאָ֣לָתִ֔י› (“at-that-time be-clean from-imprecation-
# me/my”)
# ‹כִּ֥י תָב֖וֹא אֶל־מִשְׁפַּחְתִּ֑י› (“that come/bring to family-me/my”)
# ‹וְאִם־לֹ֤א יִתְּנוּ֙ לָ֔ךְ› (“and-if not set to-you/your”)
# ‹וְהָיִ֥יתָ נָקִ֖י מֵאָלָתִֽי› (“and-be innocent from-imprecation-me/my”)
# "[EN-AID] Then you shall be free from my imprecation when you come to my
# family; and if they will not give her to you, you shall be free from my
# imprecation."
m.step("Gen.24.41")
# ‹תִּנָּקֶה מֵאָלָתִי … נָקִי› (“be-clean from-imprecation-me/my …
# innocent”)
# ‹מֵאָלָתִי› (“from-imprecation-me/my”)
# — fact holds: alah-delta-release-content
m.fact("alah_delta_release_content")

# -------------------------- Gen.24.42 · THE_RETELLING_OF_ARRIVAL_AND_PRAYER -
# ‹וָאָבֹ֥א הַיּ֖וֹם אֶל־הָעָ֑יִן› (“and-come/bring the-day to the-eye”)
# ‹וָאֹמַ֗ר יְהוָה֙ אֱלֹהֵי֙› (“and-say YHWH God”)
# ‹אֲדֹנִ֣י אַבְרָהָ֔ם אִם־יֶשְׁךָ־נָּא֙› (“lord-me/my Abraham if there-is-
# you/your please”)
# ‹מַצְלִ֣יחַ דַּרְכִּ֔י אֲשֶׁ֥ר› (“push-forward way/road-me/my which”)
# ‹אָנֹכִ֖י הֹלֵ֥ךְ עָלֶֽיהָ› (“walk/go over-her/its”)
# "[EN-AID] And I came today to the spring and said: YHWH, God of my master
# Abraham, if You are prospering my way on which I go—"
m.step("Gen.24.42")
# ‹וָאָבֹא … וָאֹמַר … אִם־יֶשְׁךָ› (“and-come/bring … and-say … if there-
# is-you/your”)
# ‹נָא מַצְלִיחַ דַּרְכִּי› (“please push-forward way/road-me/my”)
# — fact holds: retold-arrival-and-prosper-prayer
m.fact("retold_arrival_and_prosper_prayer")

# -------------------------- Gen.24.43 · THE_ALMAH_DELTA_IN_RETELLING -------
# ‹הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב› (“behold stand”)
# ‹עַל־עֵ֣ין הַמָּ֑יִם וְהָיָ֤ה› (“over eye the-waters and-be”)
# ‹הָֽעַלְמָה֙ הַיֹּצֵ֣את לִשְׁאֹ֔ב› (“the-lass the-bring-forth to-bale-up-
# water”)
# ‹וְאָמַרְתִּ֣י אֵלֶ֔יהָ הַשְׁקִֽינִי־נָ֥א› (“and-say to-her/its give-
# drink-me/my please”)
# ‹מְעַט־מַ֖יִם מִכַּדֵּֽךְ› (“little waters from-pail-you/your”)
# "[EN-AID] Behold, I stand by the spring of water; and let it be that the
# maiden who comes out to draw, to whom I say, Please let me drink a little
# water from your jar—"
m.step("Gen.24.43")
# ‹הָעַלְמָה› (“the-lass”)
# — fact holds: almah-debut-and-naarah-delta
m.fact("almah_debut_and_naarah_delta")
# ‹הַשְׁקִינִי נָא מְעַט› (“give-drink-me/my please little”)
# ‹מַיִם מִכַּדֵּךְ› (“waters from-pail-you/your”)
# — fact holds: retold-design-hashqi-ni-sign
m.fact("retold_design_hashqi_ni_sign")

# -------------------------- Gen.24.44 · THE_RETELLING_OF_THE_SIGN_ANSWER ---
# ‹וְאָמְרָ֤ה אֵלַי֙ גַּם־אַתָּ֣ה› (“and-say to-me/my also you”)
# ‹שְׁתֵ֔ה וְגַ֥ם לִגְמַלֶּ֖יךָ› (“drink and-also to-camel-you/your”)
# ‹אֶשְׁאָ֑ב הִ֣וא הָֽאִשָּׁ֔ה› (“bale-up-water he/it the-woman”)
# ‹אֲשֶׁר־הֹכִ֥יחַ יְהוָ֖ה לְבֶן־אֲדֹנִֽי› (“which be-right YHWH to-son
# lord-me/my”)
# "[EN-AID] and she says to me, Drink, and I will also draw for your camels
# — she is the woman whom YHWH has appointed for my master's son."
m.step("Gen.24.44")
# ‹גַּם־אַתָּה שְׁתֵה … אֶשְׁאָב› (“also you drink … bale-up-water”)
# ‹… הִוא הָאִשָּׁה אֲשֶׁר־הֹכִיחַ› (“he/it the-woman which be-right”)
# ‹יְהוָה› (“YHWH”)
# — fact holds: retold-sign-drink-bale-up-water-and-appoint
m.fact("retold_sign_shete_eshav_and_appoint")

# -------------------------- Gen.24.45 · THE_RETELLING_BEFORE_I_FINISHED ----
# ‹אֲנִי֩ טֶ֨רֶם אֲכַלֶּ֜ה› (“non-occurrence be-complete”)
# ‹לְדַבֵּ֣ר אֶל־לִבִּ֗י וְהִנֵּ֨ה› (“to-speak to heart-me/my and-behold”)
# ‹רִבְקָ֤ה יֹצֵאת֙ וְכַדָּ֣הּ› (“Rebekah bring-forth and-pail-her/its”)
# ‹עַל־שִׁכְמָ֔הּ וַתֵּ֥רֶד הָעַ֖יְנָה› (“over neck-as-the-place-of-burden-
# her/its and-go-down the-eye-ward”)
# ‹וַתִּשְׁאָ֑ב וָאֹמַ֥ר אֵלֶ֖יהָ› (“and-bale-up-water and-say to-her/its”)
# ‹הַשְׁקִ֥ינִי נָֽא› (“give-drink-me/my please”)
# "[EN-AID] I had not yet finished speaking to my heart, and behold Rivqah
# came out with her jar on her shoulder, went down to the spring and drew;
# and I said to her: Please let me drink."
m.step("Gen.24.45")
# ‹רִבְקָה יֹצֵאת … הַשְׁקִינִי› (“Rebekah bring-forth … give-drink-me/my”)
# ‹נָא› (“please”)
# — fact holds: retold-rivqah-arrival-and-hashqi-ni
m.fact("retold_rivqah_arrival_and_hashqi_ni")

# -------------------------- Gen.24.46 · THE_RETELLING_OF_THE_DRINK_OFFER ---
# ‹וַתְּמַהֵ֗ר וַתּ֤וֹרֶד כַּדָּהּ֙› (“and-hasten and-go-down pail-her/its”)
# ‹מֵֽעָלֶ֔יהָ וַתֹּ֣אמֶר שְׁתֵ֔ה› (“from-over-her/its and-say drink”)
# ‹וְגַם־גְּמַלֶּ֖יךָ אַשְׁקֶ֑ה וָאֵ֕שְׁתְּ› (“and-also camel-you/your give-
# drink and-drink”)
# ‹וְגַ֥ם הַגְּמַלִּ֖ים הִשְׁקָֽתָה› (“and-also the-camel give-drink”)
# "[EN-AID] And she hurried and lowered her jar and said: Drink, and I will
# also water your camels; and I drank, and she also watered the camels."
m.step("Gen.24.46")
# ‹שְׁתֵה … אַשְׁקֶה … הִשְׁקָתָה› (“drink … give-drink … give-drink”)
# — fact holds: retold-drink-and-watering
m.fact("retold_shete_and_watering")

# -------------------------- Gen.24.47 · THE_RETELLING_OF_IDENTITY_AND_GIFTS -
# ‹וָאֶשְׁאַ֣ל אֹתָ֗הּ וָאֹמַר֮› (“and-inquire obj-marker-her/its and-say”)
# ‹בַּת־מִ֣י אַתְּ֒ וַתֹּ֗אמֶר› (“daughter who? thou-and-thee and-say”)
# ‹בַּת־בְּתוּאֵל֙ בֶּן־נָח֔וֹר אֲשֶׁ֥ר› (“daughter Bethuel son Nahor
# which”)
# ‹יָֽלְדָה־לּ֖וֹ מִלְכָּ֑ה וָאָשִׂ֤ם› (“bear-young to-him/its Milcah and-
# put/set”)
# ‹הַנֶּ֨זֶם֙ עַל־אַפָּ֔הּ וְהַצְּמִידִ֖ים› (“the-nose-ring over nose-
# her/its and-the-bracelet”)
# ‹עַל־יָדֶֽיהָ› (“over hand-her/its”)
# "[EN-AID] And I asked her: Whose daughter are you? And she said: Daughter
# of Betuel son of Nahor, whom Milcah bore him. And I put the ring on her
# nose and the bracelets on her hands."
m.step("Gen.24.47")
# ‹בַּת־בְּתוּאֵל … וָאָשִׂם הַנֶּזֶם› (“daughter Bethuel … and-put/set the-
# nose-ring”)
# — fact holds: retold-identity-and-gifts
m.fact("retold_identity_and_gifts")

# -------------------------- Gen.24.48 · THE_RETELLING_OF_THE_BOW_AND_CHOICE -
# ‹וָאֶקֹּ֥ד וָֽאֶשְׁתַּחֲוֶ֖ה לַיהוָ֑ה› (“and-shrivel-up and-afflict to-
# YHWH”)
# ‹וָאֲבָרֵךְ֙ אֶת־יְהוָ֔ה אֱלֹהֵי֙› (“and-bless obj-marker YHWH God”)
# ‹אֲדֹנִ֣י אַבְרָהָ֔ם אֲשֶׁ֤ר› (“lord-me/my Abraham which”)
# ‹הִנְחַ֙נִי֙ בְּדֶ֣רֶךְ אֱמֶ֔ת› (“guide-me/my in-way/road stability”)
# ‹לָקַ֛חַת אֶת־בַּת־אֲחִ֥י אֲדֹנִ֖י› (“to-take obj-marker daughter brother
# lord-me/my”)
# ‹לִבְנֽוֹ› (“to-son-him/its”)
# "[EN-AID] And I bowed and prostrated to YHWH and blessed YHWH, God of my
# master Abraham, who led me in the true way to take my master's brother's
# daughter for his son."
m.step("Gen.24.48")
# ‹וָאֶקֹּד וָאֶשְׁתַּחֲוֶה … וָאֲבָרֵךְ› (“and-shrivel-up and-afflict …
# and-bless”)
# ‹… בְּדֶרֶךְ אֱמֶת› (“in-way/road stability”)
# — fact holds: retold-bow-bless-and-true-way
m.fact("retold_bow_bless_and_true_way")

# -------------------------- Gen.24.49 · THE_LIVE_HAGIDU_FENCE_ENDS ---------
# ‹וְעַתָּ֗ה אִם־יֶשְׁכֶ֨ם עֹשִׂ֜ים› (“and-now if there-is-you/your(pl)
# make”)
# ‹חֶ֧סֶד וֶֽאֱמֶ֛ת אֶת־אֲדֹנִ֖י› (“kindness and-stability with lord-me/my”)
# ‹הַגִּ֣ידוּ לִ֑י וְאִם־לֹ֕א› (“tell to-me/my and-if not”)
# ‹הַגִּ֣ידוּ לִ֔י וְאֶפְנֶ֥ה› (“tell to-me/my and-turn”)
# ‹עַל־יָמִ֖ין א֥וֹ עַל־שְׂמֹֽאל› (“over right-hand or over dark”)
# "[EN-AID] And now, if you will deal kindly and truly with my master, tell
# me; and if not, tell me, that I may turn to the right or to the left."
m.step("Gen.24.49")
# ‹הַגִּידוּ לִי› (“tell to-me/my”)
# — the-servant speaks a demand — LET: tell(to-me, the-bayit)
m.declare("ha_eved", "LET",
          "hagidu(li, ha_bayit)")
# ‹אִם־יֶשְׁכֶם עֹשִׂים חֶסֶד› (“if there-is-you/your(pl) make kindness”)
# ‹וֶאֱמֶת› (“and-stability”)
# — fact holds: if-kindness-and-stability-branch
m.fact("im_chesed_ve_emet_branch")
# witness-tier presupposed read: alternative_brides_on_the_family_map on
# right_or_left — read, not installed
m.witness_read("right_or_left", "alternative_brides_on_the_family_map",
                cites=["Bereshit Rabbah 60:9"])

# -------------------------- Gen.24.50 · THE_FROM_YHWH_VERDICT --------------
# ‹וַיַּ֨עַן לָבָ֤ן וּבְתוּאֵל֙› (“and-eye Laban and-Bethuel”)
# ‹וַיֹּ֣אמְר֔וּ מֵיְהוָ֖ה יָצָ֣א› (“and-say from-YHWH bring-forth”)
# ‹הַדָּבָ֑ר לֹ֥א נוּכַ֛ל› (“the-word/thing not be-able”)
# ‹דַּבֵּ֥ר אֵלֶ֖יךָ רַ֥ע› (“speak to-you/your bad”)
# ‹אוֹ־טֽוֹב› (“or good”)
# "[EN-AID] And Laban and Betuel answered and said: The matter has come out
# from YHWH; we cannot speak to you bad or good."
m.step("Gen.24.50")
# ‹וַיַּעַן לָבָן וּבְתוּאֵל› (“and-eye Laban and-Bethuel”)
# ‹וַיֹּאמְרוּ› (“and-say”)
# — event: answer
m.event("answer")
# ‹מֵיְהוָה יָצָא הַדָּבָר› (“from-YHWH bring-forth the-word/thing”)
# — fact holds: from-the-LORD-bring-forth-the-word/thing
m.fact("me_YHWH_yatza_ha_davar")
# witness-tier presupposed read: traced_to_moriah_and_disputed on
# the_matter_came_from_the_LORD — read, not installed
m.witness_read("the_matter_came_from_the_LORD", "traced_to_moriah_and_disputed",
                cites=["Bereshit Rabbah 60:10"])

# -------------------------- Gen.24.51 · THE_COMPOUND_QACH_VA_LEKH ----------
# ‹הִנֵּֽה־רִבְקָ֥ה לְפָנֶ֖יךָ קַ֣ח› (“behold Rebekah to-face-you/your
# take”)
# ‹וָלֵ֑ךְ וּתְהִ֤י אִשָּׁה֙› (“and-go and-be woman”)
# ‹לְבֶן־אֲדֹנֶ֔יךָ כַּאֲשֶׁ֖ר דִּבֶּ֥ר› (“to-son lord-you/your like-
# as/which speak”)
# ‹יְהוָֽה› (“YHWH”)
# "[EN-AID] Behold, Rivqah is before you; take and go, and let her be a wife
# to your master's son, as YHWH has spoken."
m.step("Gen.24.51")
# ‹קַח וָלֵךְ› (“take and-go”)
# — Laban-Bethuel speaks a demand — LET: take-and-go(rivqah)
m.declare("lavan_betuel", "LET",
          "qach_va_lekh(rivqah)")
# ‹וּתְהִי אִשָּׁה לְבֶן־אֲדֹנֶיךָ› (“and-be woman to-son lord-you/your”)
# — Laban-Bethuel speaks a demand — LET: be(rivqah, woman-to-son-adonekha)
m.declare("lavan_betuel", "LET",
          "tehi(rivqah, isha_le_ven_adonekha)")

# -------------------------- Gen.24.52 · THE_BOW_TO_YHWH --------------------
# ‹וַיְהִ֕י כַּאֲשֶׁ֥ר שָׁמַ֛ע› (“and-be like-as/which hear”)
# ‹עֶ֥בֶד אַבְרָהָ֖ם אֶת־דִּבְרֵיהֶ֑ם› (“servant Abraham obj-marker
# word/thing-them/their”)
# ‹וַיִּשְׁתַּ֥חוּ אַ֖רְצָה לַֽיהוָֽה› (“and-afflict earth-ward to-YHWH”)
# "[EN-AID] And when Abraham's servant heard their words, he bowed to the
# ground to YHWH."
m.step("Gen.24.52")
# ‹שָׁמַע … וַיִּשְׁתַּחוּ אַרְצָה› (“hear … and-afflict earth-ward”)
# ‹לַיהוָה› (“to-YHWH”)
# — event: hear-and-bow — agent the-servant
m.event("hear_and_bow", agent="ha_eved")

# -------------------------- Gen.24.53 · THE_GIFTS --------------------------
# ‹וַיּוֹצֵ֨א הָעֶ֜בֶד כְּלֵי־כֶ֨סֶף› (“and-bring-forth the-servant vessel
# silver”)
# ‹וּכְלֵ֤י זָהָב֙ וּבְגָדִ֔ים› (“and-vessel gold and-garment”)
# ‹וַיִּתֵּ֖ן לְרִבְקָ֑ה וּמִ֨גְדָּנֹ֔ת› (“and-set to-Rebekah and-
# preciousness”)
# ‹נָתַ֥ן לְאָחִ֖יהָ וּלְאִמָּֽהּ› (“set to-brother-her/its and-to-mother-
# her/its”)
# "[EN-AID] And the servant brought out vessels of silver and vessels of
# gold and garments and gave to Rivqah; and precious gifts he gave to her
# brother and to her mother."
m.step("Gen.24.53")
# ‹וַיּוֹצֵא … וַיִּתֵּן לְרִבְקָה› (“and-bring-forth … and-set to-Rebekah”)
# ‹… מִגְדָּנֹת נָתַן› (“precious-things set”)
# — event: give-gifts — agent the-servant; theme vessel-and-begadim-and-
# preciousness
m.event("give_gifts", agent="ha_eved", themes=["kele_u_begadim_u_migdanot"])

# -------------------------- Gen.24.54 · THE_HOSPITALITY_AND_SHALCHUNI ------
# ‹וַיֹּאכְל֣וּ וַיִּשְׁתּ֗וּ ה֛וּא› (“and-eat and-drink he/it”)
# ‹וְהָאֲנָשִׁ֥ים אֲשֶׁר־עִמּ֖וֹ וַיָּלִ֑ינוּ› (“and-the-man which with-
# him/its and-stop”)
# ‹וַיָּק֣וּמוּ בַבֹּ֔קֶר וַיֹּ֖אמֶר› (“and-arise in-morning and-say”)
# ‹שַׁלְּחֻ֥נִי לַֽאדֹנִֽי› (“send-me/my to-lord-me/my”)
# "[EN-AID] And they ate and drank, he and the men who were with him, and
# lodged; and they rose in the morning and he said: Send me to my master."
m.step("Gen.24.54")
# ‹וַיֹּאכְלוּ וַיִּשְׁתּוּ … וַיָּלִינוּ› (“and-eat and-drink … and-stop”)
# — event: eat-drink-lodge — agent the-servant-and-man
m.event("eat_drink_lodge", agent="ha_eved_u_anashim")
# ‹שַׁלְּחֻנִי לַאדֹנִי› (“send-me/my to-lord-me/my”)
# — the-servant speaks a demand — LET: shalchuni(the-servant, to-adoni)
m.declare("ha_eved", "LET",
          "shalchuni(ha_eved, la_adoni)")

# -------------------------- Gen.24.55 · THE_FAMILY_COUNTER_PROPOSAL --------
# ‹וַיֹּ֤אמֶר אָחִ֨יהָ֙ וְאִמָּ֔הּ› (“and-say brother-her/its and-mother-
# her/its”)
# ‹תֵּשֵׁ֨ב הַנַּעֲרָ֥ אִתָּ֛נוּ› (“dwell/sit the-girl with-us/our”)
# ‹יָמִ֖ים א֣וֹ עָשׂ֑וֹר› (“day or ten”)
# ‹אַחַ֖ר תֵּלֵֽךְ› (“after go”)
# "[EN-AID] And her brother and her mother said: Let the young woman stay
# with us days or ten; afterward you may go."
m.step("Gen.24.55")
# ‹תֵּשֵׁב הַנַּעֲרָ אִתָּנוּ› (“dwell/sit the-girl with-us/our”)
# ‹יָמִים אוֹ עָשׂוֹר› (“day or ten”)
# — fact holds: family-counter-dwell/sit-day-or-ten
m.fact("family_counter_teshev_yamim_o_asor")
# witness-tier presupposed read:
# death_overnight_and_the_delay_reread_as_mourning on missing_father — read,
# not installed
m.witness_read("missing_father", "death_overnight_and_the_delay_reread_as_mourning",
                cites=["Bereshit Rabbah 60:12", "Mishnah Ketubot 5:2"])
# witness-tier presupposed read: bride_year on yamim_o_asor — read, not
# installed
m.witness_read("yamim_o_asor", "bride_year",
                cites=["Ketubot 57b:1", "Ketubot 57b:2", "Ketubot 57b:3", "Ketubot 57b:4", "Yevamot 61b:12", "Yevamot 61b:13", "Yevamot 61b:14"])

# -------------------------- Gen.24.56 · THE_AL_TEACHARU_AND_SHALCHUNI_REPEAT -
# ‹וַיֹּ֤אמֶר אֲלֵהֶם֙ אַל־תְּאַחֲר֣וּ› (“and-say to-them/their do-not
# loiter”)
# ‹אֹתִ֔י וַֽיהוָ֖ה הִצְלִ֣יחַ› (“obj-marker-me/my and-YHWH push-forward”)
# ‹דַּרְכִּ֑י שַׁלְּח֕וּנִי וְאֵלְכָ֖ה› (“way/road-me/my send-me/my and-go”)
# ‹לַֽאדֹנִֽי› (“to-lord-me/my”)
# "[EN-AID] And he said to them: Do not delay me, since YHWH has made my way
# prosper; send me and I will go to my master."
m.step("Gen.24.56")
# ‹אַל־תְּאַחֲרוּ אֹתִי› (“do-not loiter obj-marker-me/my”)
# — the-servant speaks a demand — LET-NOT: over-loiter(me)
m.declare("ha_eved", "LET-NOT",
          "al_teacharu(oti)")
# ‹שַׁלְּחוּנִי וְאֵלְכָה לַאדֹנִי› (“send-me/my and-go to-lord-me/my”)
# — fact holds: shalchuni-resound-and-and-go-purpose
m.fact("shalchuni_resound_and_ve_elkha_purpose")

# -------------------------- Gen.24.57 · THE_CONSENT_QUESTION_NISHALA -------
# ‹וַיֹּאמְר֖וּ נִקְרָ֣א לַֽנַּעֲרָ֑› (“and-say call to-girl”)
# ‹וְנִשְׁאֲלָ֖ה אֶת־פִּֽיהָ› (“and-inquire obj-marker mouth-her/its”)
# "[EN-AID] And they said: Let us call the young woman and ask her mouth."
m.step("Gen.24.57")
# ‹נִקְרָא … וְנִשְׁאֲלָה אֶת־פִּיהָ› (“call … and-inquire obj-marker mouth-
# her/its”)
# — the-bayit speaks a demand — CMD-US?: inquire(obj-marker-pi-the)
m.declare("ha_bayit", "CMD-US?",
          "nishala(et_pi_ha)")
# witness-tier presupposed read: consent_law_and_translation_converging on
# we_will_ask_her — read, not installed
m.witness_read("we_will_ask_her", "consent_law_and_translation_converging",
                cites=["Bereshit Rabbah 60:12", "Onkelos Genesis 24:57"])

# -------------------------- Gen.24.58 · THE_ELEKH_CONSENT ------------------
# ‹וַיִּקְרְא֤וּ לְרִבְקָה֙ וַיֹּאמְר֣וּ› (“and-call to-Rebekah and-say”)
# ‹אֵלֶ֔יהָ הֲתֵלְכִ֖י עִם־הָאִ֣ישׁ› (“to-her/its the-go with the-man”)
# ‹הַזֶּ֑ה וַתֹּ֖אמֶר אֵלֵֽךְ› (“the-this and-say go”)
# "[EN-AID] And they called Rivqah and said to her: Will you go with this
# man? And she said: I will go."
m.step("Gen.24.58")
# ‹הֲתֵלְכִי … אֵלֵךְ› (“the-go … go”)
# — event: ask-and-consent
m.event("ask_and_consent")
# witness-tier presupposed read: read_as_defiance_of_the_questioners on
# her_single_word — read, not installed
m.witness_read("her_single_word", "read_as_defiance_of_the_questioners",
                cites=["Bereshit Rabbah 60:12"])

# -------------------------- Gen.24.59 · THE_SEND_POP -----------------------
# ‹וַֽיְשַׁלְּח֛וּ אֶת־רִבְקָ֥ה אֲחֹתָ֖ם› (“and-send obj-marker Rebekah
# sister-them/their”)
# ‹וְאֶת־מֵנִקְתָּ֑הּ וְאֶת־עֶ֥בֶד אַבְרָהָ֖ם› (“and-obj-marker suck-her/its
# and-obj-marker servant Abraham”)
# ‹וְאֶת־אֲנָשָֽׁיו› (“and-obj-marker man-him/its”)
# "[EN-AID] And they sent Rivqah their sister and her nurse and Abraham's
# servant and his men."
m.step("Gen.24.59")
# ‹וַיְשַׁלְּחוּ … עֶבֶד אַבְרָהָם› (“and-send … servant Abraham”)
# — demand settled (popped from the queue): shalchuni(the-servant, to-adoni)
m.result("shalchuni(ha_eved, la_adoni)", tmark="t1")

# -------------------------- Gen.24.60 · THE_HAYI_BLESSING ------------------
# ‹וַיְבָרֲכ֤וּ אֶת־רִבְקָה֙ וַיֹּ֣אמְרוּ› (“and-bless obj-marker Rebekah
# and-say”)
# ‹לָ֔הּ אֲחֹתֵ֕נוּ אַ֥תְּ› (“to-her/its sister-us/our thou-and-thee”)
# ‹הֲיִ֖י לְאַלְפֵ֣י רְבָבָ֑ה› (“be to-thousand abundance”)
# ‹וְיִירַ֣שׁ זַרְעֵ֔ךְ אֵ֖ת› (“and-possess/inherit seed-you/your obj-
# marker”)
# ‹שַׁ֥עַר שֹׂנְאָֽיו› (“gate hate-him/its”)
# "[EN-AID] And they blessed Rivqah and said to her: Our sister, be you
# thousands of myriads, and may your seed possess the gate of its haters."
m.step("Gen.24.60")
# ‹הֲיִי לְאַלְפֵי רְבָבָה› (“be to-thousand abundance”)
# — the-bayit speaks a demand — LET: be(rivqah, to-thousand-abundance)
m.declare("ha_bayit", "LET",
          "hayi(rivqah, le_alfe_revava)")
# ‹וְיִירַשׁ זַרְעֵךְ אֵת› (“and-possess/inherit seed-you/your obj-marker”)
# ‹שַׁעַר שֹׂנְאָיו› (“gate hate-him/its”)
# — fact holds: gate-fowl-haters-blessing-content
m.fact("gate_of_haters_blessing_content")
# witness-tier presupposed read:
# insincere_and_therefore_needing_a_later_prayer on farewell_blessing —
# read, not installed
m.witness_read("farewell_blessing", "insincere_and_therefore_needing_a_later_prayer",
                cites=["Bereshit Rabbah 60:13"])
# witness-tier presupposed read: divided_by_one_member_joined_by_the_other
# on thousands_and_myriads — read, not installed
m.witness_read("thousands_and_myriads", "divided_by_one_member_joined_by_the_other",
                cites=["Bereshit Rabbah 60:13", "Onkelos Genesis 24:60"])

# -------------------------- Gen.24.61 · THE_COMPOUND_POP_AND_DEPARTURE -----
# ‹וַתָּ֨קָם רִבְקָ֜ה וְנַעֲרֹתֶ֗יהָ› (“and-arise Rebekah and-girl-her/its”)
# ‹וַתִּרְכַּ֨בְנָה֙ עַל־הַגְּמַלִּ֔ים וַתֵּלַ֖כְנָה› (“and-ride over the-
# camel and-go”)
# ‹אַחֲרֵ֣י הָאִ֑ישׁ וַיִּקַּ֥ח› (“after the-man and-take”)
# ‹הָעֶ֛בֶד אֶת־רִבְקָ֖ה וַיֵּלַֽךְ› (“the-servant obj-marker Rebekah and-
# go”)
# "[EN-AID] And Rivqah and her young women rose and rode on the camels and
# went after the man; and the servant took Rivqah and went."
m.step("Gen.24.61")
# ‹וַתָּקָם … וַתֵּלַכְנָה אַחֲרֵי› (“and-arise … and-go after”)
# ‹הָאִישׁ› (“the-man”)
# — event: ?
m.event("?")
# ‹וַיִּקַּח הָעֶבֶד אֶת־רִבְקָה› (“and-take the-servant obj-marker
# Rebekah”)
# ‹וַיֵּלַךְ› (“and-go”)
# — demand settled (popped from the queue): take-and-go(rivqah)
m.result("qach_va_lekh(rivqah)", tmark="t2")
# witness-tier presupposed read:
# twins_foreshadowed_with_the_plain_answer_kept on the_camel_marks — read,
# not installed
m.witness_read("the_camel_marks", "twins_foreshadowed_with_the_plain_answer_kept",
                cites=["Bereshit Rabbah 60:14"])
# witness-tier presupposed read: riding_order on va_telakhna_acharei_ha_ish
# — read, not installed
m.witness_read("va_telakhna_acharei_ha_ish", "riding_order",
                cites=["Berakhot 61a:23", "Berakhot 61a:24", "Berakhot 61a:25"])

# -------------------------- Gen.24.62 · THE_BEER_LACHAI_ROI_ADDRESS --------
# ‹וְיִצְחָק֙ בָּ֣א מִבּ֔וֹא› (“and-Isaac come/bring from-come/bring”)
# ‹בְּאֵ֥ר לַחַ֖י רֹאִ֑י› (“Beer-lahai-roi”)
# ‹וְה֥וּא יוֹשֵׁ֖ב בְּאֶ֥רֶץ› (“and-he/it dwell/sit in-earth”)
# ‹הַנֶּֽגֶב› (“the-south”)
# "[EN-AID] And Isaac came from coming to Beer-lachai-roi; and he was
# dwelling in the land of the Negev."
m.step("Gen.24.62")
# ‹בְּאֵר לַחַי רֹאִי› (“Beer-lahai-roi”)
# — fact holds: Isaac-address-beer-lachai-Beer-lahai-roi
m.fact("yitzchaq_address_beer_lachai_roi")

# -------------------------- Gen.24.63 · THE_SUACH_HAPAX_AND_CAMELS ---------
# ‹וַיֵּצֵ֥א יִצְחָ֛ק לָשׂ֥וּחַ› (“and-bring-forth Isaac to-muse-pensively”)
# ‹בַּשָּׂדֶ֖ה לִפְנ֣וֹת עָ֑רֶב› (“in-field to-turn evening”)
# ‹וַיִּשָּׂ֤א עֵינָיו֙ וַיַּ֔רְא› (“and-lift/carry eye-him/its and-see”)
# ‹וְהִנֵּ֥ה גְמַלִּ֖ים בָּאִֽים› (“and-behold camel come/bring”)
# "[EN-AID] And Isaac went out to meditate in the field toward evening; and
# he lifted his eyes and saw, and behold, camels were coming."
m.step("Gen.24.63")
# ‹לָשׂוּחַ … וְהִנֵּה גְמַלִּים› (“to-muse-pensively … and-behold camel”)
# ‹בָּאִים› (“come/bring”)
# — event: meditate-and-see-camels — agent Isaac
m.event("meditate_and_see_camels", agent="yitzchaq")
# witness-tier presupposed read: afternoon_prayer_instituted_by_both_members
# on went_out_toward_evening — read, not installed
m.witness_read("went_out_toward_evening", "afternoon_prayer_instituted_by_both_members",
                cites=["Bereshit Rabbah 68:9", "Onkelos Genesis 24:63"])

# -------------------------- Gen.24.64 · THE_RIVQAH_SEES_ISAAC --------------
# ‹וַתִּשָּׂ֤א רִבְקָה֙ אֶת־עֵינֶ֔יהָ› (“and-lift/carry Rebekah obj-marker
# eye-her/its”)
# ‹וַתֵּ֖רֶא אֶת־יִצְחָ֑ק וַתִּפֹּ֖ל› (“and-see obj-marker Isaac and-fall”)
# ‹מֵעַ֥ל הַגָּמָֽל› (“from-over the-camel”)
# "[EN-AID] And Rivqah lifted her eyes and saw Isaac, and she fell from upon
# the camel."
m.step("Gen.24.64")
# ‹וַתֵּרֶא אֶת־יִצְחָק וַתִּפֹּל› (“and-see obj-marker Isaac and-fall”)
# ‹מֵעַל הַגָּמָל› (“from-over the-camel”)
# — event: see-and-dismount — agent rivqah; theme Isaac
m.event("see_and_dismount", agent="rivqah", themes=["yitzchaq"])
# witness-tier presupposed read: softened_to_inclined_by_two_devices on
# she_fell — read, not installed
m.witness_read("she_fell", "softened_to_inclined_by_two_devices",
                cites=["Bereshit Rabbah 60:15", "Onkelos Genesis 24:64"])

# -------------------------- Gen.24.65 · THE_TZAIF_VEIL ---------------------
# ‹וַתֹּ֣אמֶר אֶל־הָעֶ֗בֶד מִֽי־הָאִ֤ישׁ› (“and-say to the-servant who? the-
# man”)
# ‹הַלָּזֶה֙ הַהֹלֵ֤ךְ בַּשָּׂדֶה֙› (“this-very the-walk/go in-field”)
# ‹לִקְרָאתֵ֔נוּ וַיֹּ֥אמֶר הָעֶ֖בֶד› (“to-encountering-us/our and-say the-
# servant”)
# ‹ה֣וּא אֲדֹנִ֑י וַתִּקַּ֥ח› (“he/it lord-me/my and-take”)
# ‹הַצָּעִ֖יף וַתִּתְכָּֽס› (“the-veil and-plump”)
# "[EN-AID] And she said to the servant: Who is that man walking in the
# field to meet us? And the servant said: He is my master. And she took the
# veil and covered herself."
m.step("Gen.24.65")
# ‹ה֣וּא אֲדֹנִי … הַצָּעִיף› (“he/it lord-me/my … the-veil”)
# ‹וַתִּתְכָּס› (“and-plump”)
# — event: identify-and-veil
m.event("identify_and_veil")

# -------------------------- Gen.24.66 · THE_SERVANT_RECOUNTS ---------------
# ‹וַיְסַפֵּ֥ר הָעֶ֖בֶד לְיִצְחָ֑ק› (“and-count the-servant to-Isaac”)
# ‹אֵ֥ת כָּל־הַדְּבָרִ֖ים אֲשֶׁ֥ר› (“obj-marker all the-word/thing which”)
# ‹עָשָֽׂה› (“make”)
# "[EN-AID] And the servant recounted to Isaac all the things that he had
# done."
m.step("Gen.24.66")
# ‹וַיְסַפֵּר … כָּל־הַדְּבָרִים אֲשֶׁר› (“and-count … all the-word/thing
# which”)
# ‹עָשָׂה› (“make”)
# — event: recount — agent the-servant
m.event("recount", agent="ha_eved")
# witness-grounded state (its own tier):
# generalities_exceed_details_second_seat on all_the_matters_he_had_done
m.witness_state("all_the_matters_he_had_done", "generalities_exceed_details_second_seat",
                cites=["Bereshit Rabbah 60:15"])

# -------------------------- Gen.24.67 · THE_WIFE_LOVE_AND_COMFORT ----------
# ‹וַיְבִאֶ֣הָ יִצְחָ֗ק הָאֹ֨הֱלָה֙› (“and-come/bring-her/its Isaac the-
# tent-ward”)
# ‹שָׂרָ֣ה אִמּ֔וֹ וַיִּקַּ֧ח› (“Sarah mother-him/its and-take”)
# ‹אֶת־רִבְקָ֛ה וַתְּהִי־ל֥וֹ לְאִשָּׁ֖ה› (“obj-marker Rebekah and-be to-
# him/its to-woman”)
# ‹וַיֶּאֱהָבֶ֑הָ וַיִּנָּחֵ֥ם יִצְחָ֖ק› (“and-have-affection-for-her/its
# and-sigh Isaac”)
# ‹אַחֲרֵ֥י אִמּֽוֹ› (“after mother-him/its”)
# "[EN-AID] And Isaac brought her into the tent of Sarah his mother; and he
# took Rivqah and she became his wife, and he loved her; and Isaac was
# comforted after his mother."
m.step("Gen.24.67")
# ‹וַיְבִאֶהָ יִצְחָק הָאֹהֱלָה› (“and-come/bring-her/its Isaac the-tent-
# ward”)
# ‹שָׂרָה אִמּוֹ› (“Sarah mother-him/its”)
# — event: ?
m.event("?")
# ‹וַיִּקַּח אֶת־רִבְקָה וַתְּהִי־לוֹ› (“and-take obj-marker Rebekah and-be
# to-him/its”)
# ‹לְאִשָּׁה› (“to-woman”)
# — demand settled (popped from the queue): be(rivqah, woman-to-son-
# adonekha)
m.result("tehi(rivqah, isha_le_ven_adonekha)", tmark="t3")
# ‹וַיֶּאֱהָבֶהָ … וַיִּנָּחֵם יִצְחָק› (“and-have-affection-for-her/its …
# and-sigh Isaac”)
# ‹אַחֲרֵי אִמּוֹ› (“after mother-him/its”)
# — event: ?
m.event("?")
# witness-grounded state (its own tier): four_conditions_ceased_and_returned
# on the_tent
m.witness_state("the_tent", "four_conditions_ceased_and_returned",
                cites=["Bereshit Rabbah 60:16", "Onkelos Genesis 24:67"])
# witness-tier presupposed read: precedence_read_off_verse_order on
# marriage_before_remarriage — read, not installed
m.witness_read("marriage_before_remarriage", "precedence_read_off_verse_order",
                cites=["Bereshit Rabbah 60:16"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'avraham', 'ha_eved'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hagidu(li, ha_bayit)', 'al_teacharu(oti)', 'nishala(et_pi_ha)', 'hayi(rivqah, le_alfe_revava)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['eved_avraham_anokhi', 'YHWH_berakh_et_adoni_meod_va_yigdal_va_yiten_wealth', 'sara_teled_ben_achare_ziqnah_and_gave_all', 'va_yashbie_ni_adoni_le_mor', 'lo_tiqach_isha_li_veni_mi_benot_ha_kenaani', 'telekh_el_bet_avi_ve_el_mishpachti', 've_laqachta_isha_li_veni', 'ulay_lo_telekh_ha_isha_achara_y_retell', 'retold_angel_promise_and_take_from_family', 'alah_delta_release_content', 'retold_arrival_and_prosper_prayer', 'almah_debut_and_naarah_delta', 'retold_design_hashqi_ni_sign', 'retold_sign_shete_eshav_and_appoint', 'retold_rivqah_arrival_and_hashqi_ni', 'retold_shete_and_watering', 'retold_identity_and_gifts', 'retold_bow_bless_and_true_way', 'im_chesed_ve_emet_branch', 'me_YHWH_yatza_ha_davar', 'family_counter_teshev_yamim_o_asor', 'shalchuni_resound_and_ve_elkha_purpose', 'gate_of_haters_blessing_content', 'yitzchaq_address_beer_lachai_roi'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    assert sorted(m.WORLD["witnessed"]) == ['all_the_matters_he_had_done', 'the_tent']
    assert m.WORLD["witnessed"]['all_the_matters_he_had_done']["cites"] == ['Bereshit Rabbah 60:15']
    assert all('generalities_exceed_details_second_seat' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_tent']["cites"] == ['Bereshit Rabbah 60:16', 'Onkelos Genesis 24:67']
    assert all('four_conditions_ceased_and_returned' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_retellings_deltas_are_the_sugyots_ground', 'the_giving_the_consent_the_handover_the_gifts_and_the_marriage_formula'), ('right_or_left', 'alternative_brides_on_the_family_map'), ('the_matter_came_from_the_LORD', 'traced_to_moriah_and_disputed'), ('missing_father', 'death_overnight_and_the_delay_reread_as_mourning'), ('yamim_o_asor', 'bride_year'), ('we_will_ask_her', 'consent_law_and_translation_converging'), ('her_single_word', 'read_as_defiance_of_the_questioners'), ('farewell_blessing', 'insincere_and_therefore_needing_a_later_prayer'), ('thousands_and_myriads', 'divided_by_one_member_joined_by_the_other'), ('the_camel_marks', 'twins_foreshadowed_with_the_plain_answer_kept'), ('va_telakhna_acharei_ha_ish', 'riding_order'), ('went_out_toward_evening', 'afternoon_prayer_instituted_by_both_members'), ('she_fell', 'softened_to_inclined_by_two_devices'), ('marriage_before_remarriage', 'precedence_read_off_verse_order')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Kiddushin 3:1', 'Mishnah Kiddushin 2:6', 'Mishnah Ketubot 4:4', 'Mishnah Ketubot 4:5', 'Mishnah Ketubot 5:1', 'Mishnah Ketubot 5:2', 'Mishnah Ketubot 1:2', 'Kiddushin 50b:4', 'Moed Katan 18b:15', 'Ketubot 57b:2', 'Ketubot 57b:3', 'Nedarim 37b:8', 'Berakhot 61a:24', 'Eruvin 18b:8', 'Pesachim 3a:14', 'Bava Kamma 92b:9', 'Berakhot 26b:6', 'Avodah Zarah 7b:14', 'Pesachim 88a:4', 'Yevamot 61b:13', 'Bava Kamma 92b:6']
    assert all('the_giving_the_consent_the_handover_the_gifts_and_the_marriage_formula' not in f for f in m.WORLD["facts"])
    assert 'the_retellings_deltas_are_the_sugyots_ground' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 60:9']
    assert all('alternative_brides_on_the_family_map' not in f for f in m.WORLD["facts"])
    assert 'right_or_left' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 60:10']
    assert all('traced_to_moriah_and_disputed' not in f for f in m.WORLD["facts"])
    assert 'the_matter_came_from_the_LORD' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 60:12', 'Mishnah Ketubot 5:2']
    assert all('death_overnight_and_the_delay_reread_as_mourning' not in f for f in m.WORLD["facts"])
    assert 'missing_father' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Ketubot 57b:1', 'Ketubot 57b:2', 'Ketubot 57b:3', 'Ketubot 57b:4', 'Yevamot 61b:12', 'Yevamot 61b:13', 'Yevamot 61b:14']
    assert all('bride_year' not in f for f in m.WORLD["facts"])
    assert 'yamim_o_asor' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 60:12', 'Onkelos Genesis 24:57']
    assert all('consent_law_and_translation_converging' not in f for f in m.WORLD["facts"])
    assert 'we_will_ask_her' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 60:12']
    assert all('read_as_defiance_of_the_questioners' not in f for f in m.WORLD["facts"])
    assert 'her_single_word' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 60:13']
    assert all('insincere_and_therefore_needing_a_later_prayer' not in f for f in m.WORLD["facts"])
    assert 'farewell_blessing' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 60:13', 'Onkelos Genesis 24:60']
    assert all('divided_by_one_member_joined_by_the_other' not in f for f in m.WORLD["facts"])
    assert 'thousands_and_myriads' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 60:14']
    assert all('twins_foreshadowed_with_the_plain_answer_kept' not in f for f in m.WORLD["facts"])
    assert 'the_camel_marks' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Berakhot 61a:23', 'Berakhot 61a:24', 'Berakhot 61a:25']
    assert all('riding_order' not in f for f in m.WORLD["facts"])
    assert 'va_telakhna_acharei_ha_ish' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 68:9', 'Onkelos Genesis 24:63']
    assert all('afternoon_prayer_instituted_by_both_members' not in f for f in m.WORLD["facts"])
    assert 'went_out_toward_evening' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 60:15', 'Onkelos Genesis 24:64']
    assert all('softened_to_inclined_by_two_devices' not in f for f in m.WORLD["facts"])
    assert 'she_fell' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Bereshit Rabbah 60:16']
    assert all('precedence_read_off_verse_order' not in f for f in m.WORLD["facts"])
    assert 'marriage_before_remarriage' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
