#!/usr/bin/env python3
# =============================================================================
# gen_44_isaac_gerar_sister_expel — 26:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_44_isaac_gerar_sister_expel.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Isaac in Gerar — sister-claim, decree, hundredfold, expulsion seam (26:1-16)"""
from machine import Machine

m = Machine("gen_44_isaac_gerar_sister_expel")

# -------------------------- Gen.26.1 · THE_FAMINE_ECHO_AND_THE_PATH_TO_GERAR -
# וַיְהִ֤י רָעָב֙ בָּאָ֔רֶץ מִלְּבַד֙ הָרָעָ֣ב הָרִאשׁ֔וֹן אֲשֶׁ֥ר הָיָ֖ה
# בִּימֵ֣י אַבְרָהָ֑ם וַיֵּ֧לֶךְ יִצְחָ֛ק אֶל־אֲבִימֶּ֥לֶךְ
# מֶֽלֶךְ־פְּלִשְׁתִּ֖ים גְּרָֽרָה
# "[EN-AID] And there was a famine in the land, besides the first famine
# that was in the days of Abraham; and Isaac went to Abimelech king of the
# Philistines, to Gerar."
m.step("Gen.26.1")
# ‹וַיְהִי רָעָב בָּאָרֶץ› event: famine
m.event("famine")
# ‹מִלְּבַד הָרָעָב הָרִאשׁוֹן אֲשֶׁר הָיָה בִּימֵי אַבְרָהָם› fact holds:
# echo-first-famine-days-fowl-avraham
m.fact("echo_first_famine_days_of_avraham")
# ‹וַיֵּלֶךְ יִצְחָק אֶל־אֲבִימֶּלֶךְ … גְּרָרָה› event: go — agent yitzchaq
m.event("go", agent="yitzchaq")
# ‹יִצְחָק … אַבְרָהָם … אֲבִימֶּלֶךְ … גְּרָרָה› reads without prior
# install (flag, not fix): yitzchaq, avraham, avimelekh, gerar, pelishtim
m.presupposed("yitzchaq", "avraham", "avimelekh", "gerar", "pelishtim")

# -------------------------- Gen.26.2 · THE_APPEARANCE_THE_LET_NOT_AND_THE_DWELL -
# וַיֵּרָ֤א אֵלָי֙ו יְהוָ֔ה וַיֹּ֖אמֶר אַל־תֵּרֵ֣ד מִצְרָ֑יְמָה שְׁכֹ֣ן
# בָּאָ֔רֶץ אֲשֶׁ֖ר אֹמַ֥ר אֵלֶֽיךָ
# "[EN-AID] And YHWH appeared to him and said: Do not go down to Egypt;
# dwell in the land that I say to you."
m.step("Gen.26.2")
# ‹וַיֵּרָא אֵלָיו יְהוָה וַיֹּאמֶר› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹אַל־תֵּרֵד מִצְרָיְמָה› the-LORD speaks a demand — LET-NOT: upon-
# tered(yitzchaq, mitzrayim)
m.declare("YHWH", "LET-NOT",
          "al_tered(yitzchaq, mitzrayim)")
# ‹שְׁכֹן בָּאָרֶץ אֲשֶׁר אֹמַר אֵלֶיךָ› the-LORD speaks a demand — LET:
# shekhon(yitzchaq, in-the-earth-which-omar-to-you)
m.declare("YHWH", "LET",
          "shekhon(yitzchaq, ba_aretz_asher_omar_elekha)")

# -------------------------- Gen.26.3 · THE_SOJOURN_THE_PROMISE_AND_THE_PAST_OATH -
# גּ֚וּר בָּאָ֣רֶץ הַזֹּ֔את וְאֶֽהְיֶ֥ה עִמְּךָ֖ וַאֲבָרְכֶ֑ךָּ כִּֽי־לְךָ֣
# וּֽלְזַרְעֲךָ֗ אֶתֵּן֙ אֶת־כָּל־הָֽאֲרָצֹ֣ת הָאֵ֔ל וַהֲקִֽמֹתִי֙
# אֶת־הַשְּׁבֻעָ֔ה אֲשֶׁ֥ר נִשְׁבַּ֖עְתִּי לְאַבְרָהָ֥ם אָבִֽיךָ
# "[EN-AID] Sojourn in this land, and I will be with you and will bless you;
# for to you and to your seed I will give all these lands, and I will
# establish the oath that I swore to Abraham your father."
m.step("Gen.26.3")
# ‹גּוּר בָּאָרֶץ הַזֹּאת› the-LORD speaks a demand — LET: gur(yitzchaq, in-
# the-earth-the-this)
m.declare("YHWH", "LET",
          "gur(yitzchaq, ba_aretz_ha_zot)")
# ‹וְאֶהְיֶה עִמְּךָ וַאֲבָרְכֶךָּ› fact holds: and-ehye-if-kha; and-
# avarkhe-like
m.fact("ve_ehye_im_kha",
       "va_avarkhe_ka")
# ‹כִּי־לְךָ וּלְזַרְעֲךָ אֶתֵּן אֶת־כָּל־הָאֲרָצֹת הָאֵל› fact holds: eten-
# to-kha-and-to-zara-kha-kal-the-aratzot-the-to
m.fact("eten_le_kha_u_le_zara_kha_et_kal_ha_aratzot_ha_el")
# ‹וַהֲקִמֹתִי אֶת־הַשְּׁבֻעָה אֲשֶׁר נִשְׁבַּעְתִּי לְאַבְרָהָם אָבִיךָ›
# fact holds: and-haqimoti-the-shevua; past-oath-nishbati-to-avraham
m.fact("va_haqimoti_et_ha_shevua",
       "past_oath_nishbati_le_avraham")

# -------------------------- Gen.26.4 · THE_SEED_STARS_AND_THE_NATIONS_BLESSING -
# וְהִרְבֵּיתִ֤י אֶֽת־זַרְעֲךָ֙ כְּכוֹכְבֵ֣י הַשָּׁמַ֔יִם וְנָתַתִּ֣י
# לְזַרְעֲךָ֔ אֵ֥ת כָּל־הָאֲרָצֹ֖ת הָאֵ֑ל וְהִתְבָּרֲכ֣וּ בְזַרְעֲךָ֔ כֹּ֖ל
# גּוֹיֵ֥י הָאָֽרֶץ
# "[EN-AID] And I will multiply your seed as the stars of the heavens, and I
# will give to your seed all these lands; and in your seed all nations of
# the earth shall bless themselves."
m.step("Gen.26.4")
# ‹וְהִרְבֵּיתִי … וְנָתַתִּי לְזַרְעֲךָ אֵת כָּל־הָאֲרָצֹת הָאֵל› fact
# holds: and-hirbeti-zara-kha-like-khokhve-the-heavens; and-natati-to-zara-
# kha-the-aratzot
m.fact("ve_hirbeti_zara_kha_ke_khokhve_ha_shamayim",
       "ve_natati_le_zara_kha_ha_aratzot")
# ‹וְהִתְבָּרֲכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ› fact holds: and-
# hitbarakhu-and-zara-kha-all-goye-the-earth
m.fact("ve_hitbarakhu_ve_zara_kha_kol_goye_ha_aretz")

# -------------------------- Gen.26.5 · THE_GROUNDS_BECAUSE_ABRAHAM_LISTENED -
# עֵ֕קֶב אֲשֶׁר־שָׁמַ֥ע אַבְרָהָ֖ם בְּקֹלִ֑י וַיִּשְׁמֹר֙ מִשְׁמַרְתִּ֔י
# מִצְוֺתַ֖י חֻקּוֹתַ֥י וְתוֹרֹתָֽי
# "[EN-AID] because Abraham listened to My voice and kept My charge, My
# commandments, My statutes, and My teachings."
m.step("Gen.26.5")
# ‹עֵקֶב אֲשֶׁר־שָׁמַע אַבְרָהָם בְּקֹלִי› fact holds: eqev-which-shama-
# avraham-in-qoli
m.fact("eqev_asher_shama_avraham_be_qoli")
# ‹וַיִּשְׁמֹר מִשְׁמַרְתִּי מִצְוֺתַי חֻקּוֹתַי וְתוֹרֹתָי› fact holds:
# and-yishmor-mishmarti-mitzvotai-chuqqotai-and-torotai
m.fact("va_yishmor_mishmarti_mitzvotai_chuqqotai_ve_torotai")

# -------------------------- Gen.26.6 · THE_DWELL_OTHER_VERB_CENTERPIECE ----
# וַיֵּ֥שֶׁב יִצְחָ֖ק בִּגְרָֽר
# "[EN-AID] And Isaac dwelt in Gerar."
m.step("Gen.26.6")
# ‹וַיֵּשֶׁב יִצְחָק בִּגְרָר› event: dwell — agent yitzchaq
m.event("dwell", agent="yitzchaq")
# ‹וַיֵּשֶׁב ≠ שְׁכֹן / גּוּר› fact holds: other-verb-non-pop-shekhon-and-
# gur
m.fact("other_verb_non_pop_shekhon_and_gur")

# -------------------------- Gen.26.7 · THE_SISTER_CLAIM_ISAAC_LIVE ---------
# וַֽיִּשְׁאֲל֞וּ אַנְשֵׁ֤י הַמָּקוֹם֙ לְאִשְׁתּ֔וֹ וַיֹּ֖אמֶר אֲחֹ֣תִי
# הִ֑וא כִּ֤י יָרֵא֙ לֵאמֹ֣ר אִשְׁתִּ֔י פֶּן־יַֽהַרְגֻ֜נִי אַנְשֵׁ֤י
# הַמָּקוֹם֙ עַל־רִבְקָ֔ה כִּֽי־טוֹבַ֥ת מַרְאֶ֖ה הִֽיא
# "[EN-AID] And the men of the place asked about his wife; and he said: She
# is my sister — for he feared to say, My wife, lest the men of the place
# kill me on account of Rivqah, for she is good of appearance."
m.step("Gen.26.7")
# ‹וַיִּשְׁאֲלוּ … וַיֹּאמֶר› event: ?
m.event("?")
# ‹אֲחֹתִי הִוא› fact holds: achoti-hi-claim-by-yitzchaq
m.fact("achoti_hi_claim_by_yitzchaq")
# ‹כִּי יָרֵא … כִּי־טוֹבַת מַרְאֶה הִיא› fact holds: yare-to-mor-ishti-
# lest-yahargu; tovat-appearance-hi
m.fact("yare_le_mor_ishti_pen_yahargu",
       "tovat_mareh_hi")

# -------------------------- Gen.26.8 · THE_WINDOW_AND_THE_NAME_ROOT_LAUGH --
# וַיְהִ֗י כִּ֣י אָֽרְכוּ־ל֥וֹ שָׁם֙ הַיָּמִ֔ים וַיַּשְׁקֵ֗ף אֲבִימֶ֨לֶךְ֙
# מֶ֣לֶךְ פְּלִשְׁתִּ֔ים בְּעַ֖ד הַֽחַלּ֑וֹן וַיַּ֗רְא וְהִנֵּ֤ה יִצְחָק֙
# מְצַחֵ֔ק אֵ֖ת רִבְקָ֥ה אִשְׁתּֽוֹ
# "[EN-AID] And it came to pass, when he had been there a long time, that
# Abimelech king of the Philistines looked out through the window and saw,
# and behold, Isaac was laughing/playing with Rivqah his wife."
m.step("Gen.26.8")
# ‹אָרְכוּ … וַיַּשְׁקֵף … וַיַּרְא› event: ?
m.event("?")
# ‹יִצְחָק מְצַחֵק אֵת רִבְקָה אִשְׁתּוֹ› fact holds: yitzchaq-metzacheq-
# rivqah-his-wife
m.fact("yitzchaq_metzacheq_et_rivqah_ishto")

# -------------------------- Gen.26.9 · THE_SUMMONS_AND_THE_RE_QUOTE --------
# וַיִּקְרָ֨א אֲבִימֶ֜לֶךְ לְיִצְחָ֗ק וַיֹּ֨אמֶר֙ אַ֣ךְ הִנֵּ֤ה אִשְׁתְּךָ֙
# הִ֔וא וְאֵ֥יךְ אָמַ֖רְתָּ אֲחֹ֣תִי הִ֑וא וַיֹּ֤אמֶר אֵלָי֙ו יִצְחָ֔ק כִּ֣י
# אָמַ֔רְתִּי פֶּן־אָמ֖וּת עָלֶֽיהָ
# "[EN-AID] And Abimelech called Isaac and said: Behold, of a surety she is
# your wife; and how did you say, She is my sister? And Isaac said to him:
# Because I said, Lest I die because of her."
m.step("Gen.26.9")
# ‹וַיִּקְרָא אֲבִימֶלֶךְ לְיִצְחָק וַיֹּאמֶר … וַיֹּאמֶר אֵלָיו יִצְחָק›
# event: ?
m.event("?")
# ‹הִנֵּה אִשְׁתְּךָ הִוא … אָמַרְתָּ אֲחֹתִי הִוא› fact holds: isht-kha-
# hiv; amarta-achoti-hi-requote
m.fact("isht_kha_hiv",
       "amarta_achoti_hi_requote")

# -------------------------- Gen.26.10 · THE_WHAT_HAVE_YOU_DONE_AND_THE_GUILT_DEBUT -
# וַיֹּ֣אמֶר אֲבִימֶ֔לֶךְ מַה־זֹּ֖את עָשִׂ֣יתָ לָּ֑נוּ כִּ֠מְעַט שָׁכַ֞ב
# אַחַ֤ד הָעָם֙ אֶת־אִשְׁתֶּ֔ךָ וְהֵבֵאתָ֥ עָלֵ֖ינוּ אָשָֽׁם
# "[EN-AID] And Abimelech said: What is this you have done to us? One of the
# people might easily have lain with your wife, and you would have brought
# guilt upon us."
m.step("Gen.26.10")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ› event: say — agent avimelekh
m.event("say", agent="avimelekh")
# ‹מַה־זֹּאת עָשִׂיתָ לָּנוּ› fact holds: ma-this-asita-to-nu
m.fact("ma_zot_asita_la_nu")
# ‹כִּמְעַט שָׁכַב … וְהֵבֵאתָ עָלֵינוּ אָשָׁם› fact holds: near-miss-
# shakhav-and-asham-brought
m.fact("near_miss_shakhav_and_asham_brought")

# -------------------------- Gen.26.11 · THE_ROYAL_DECREE_MOT_YUMAT ---------
# וַיְצַ֣ו אֲבִימֶ֔לֶךְ אֶת־כָּל־הָעָ֖ם לֵאמֹ֑ר הַנֹּגֵ֜עַ בָּאִ֥ישׁ הַזֶּ֛ה
# וּבְאִשְׁתּ֖וֹ מ֥וֹת יוּמָֽת
# "[EN-AID] And Abimelech commanded all the people, saying: He who touches
# this man or his wife shall surely be put to death."
m.step("Gen.26.11")
# ‹וַיְצַו אֲבִימֶלֶךְ אֶת־כָּל־הָעָם› event: command — agent avimelekh
m.event("command", agent="avimelekh")
# ‹הַנֹּגֵעַ בָּאִישׁ הַזֶּה וּבְאִשְׁתּוֹ מוֹת יוּמָת› fact holds: royal-
# decree-no-touch-dying-yumat
m.fact("royal_decree_no_touch_mot_yumat")

# -------------------------- Gen.26.12 · THE_HUNDREDFOLD_AND_THE_BLESSING ---
# וַיִּזְרַ֤ע יִצְחָק֙ בָּאָ֣רֶץ הַהִ֔וא וַיִּמְצָ֛א בַּשָּׁנָ֥ה הַהִ֖וא
# מֵאָ֣ה שְׁעָרִ֑ים וַֽיְבָרֲכֵ֖הוּ יְהוָֽה
# "[EN-AID] And Isaac sowed in that land and found in that year a hundred
# measures; and YHWH blessed him."
m.step("Gen.26.12")
# ‹וַיִּזְרַע … וַיִּמְצָא … מֵאָה שְׁעָרִים› event: sow-and-find — agent
# yitzchaq; theme mea-shearim
m.event("sow_and_find", agent="yitzchaq", themes=["mea_shearim"])
# ‹וַיְבָרֲכֵהוּ יְהוָה› event: ?
m.event("?")

# -------------------------- Gen.26.13 · THE_MAN_GREW_VERY_GREAT ------------
# וַיִּגְדַּ֖ל הָאִ֑ישׁ וַיֵּ֤לֶךְ הָלוֹךְ֙ וְגָדֵ֔ל עַ֥ד כִּֽי־גָדַ֖ל
# מְאֹֽד
# "[EN-AID] And the man became great, and grew more and more until he became
# very great."
m.step("Gen.26.13")
# ‹וַיִּגְדַּל … הָלוֹךְ וְגָדֵל … גָדַל מְאֹד› event: grow-great
m.event("grow_great")

# -------------------------- Gen.26.14 · THE_FLOCKS_AND_THE_ENVY_DEBUT ------
# וַֽיְהִי־ל֤וֹ מִקְנֵה־צֹאן֙ וּמִקְנֵ֣ה בָקָ֔ר וַעֲבֻדָּ֖ה רַבָּ֑ה
# וַיְקַנְא֥וּ אֹת֖וֹ פְּלִשְׁתִּֽים
# "[EN-AID] And he had possessions of flocks and possessions of herds and a
# great household; and the Philistines envied him."
m.step("Gen.26.14")
# ‹מִקְנֵה־צֹאן וּמִקְנֵה בָקָר וַעֲבֻדָּה רַבָּה› fact holds: miqne-tzon-
# vaqar-and-avuda-raba
m.fact("miqne_tzon_vaqar_va_avuda_raba")
# ‹וַיְקַנְאוּ אֹתוֹ פְּלִשְׁתִּים› event: envy — agent pelishtim
m.event("envy", agent="pelishtim")

# -------------------------- Gen.26.15 · THE_STOPPED_WELLS_OF_ABRAHAMS_DAYS -
# וְכָל־הַבְּאֵרֹ֗ת אֲשֶׁ֤ר חָֽפְרוּ֙ עַבְדֵ֣י אָבִ֔יו בִּימֵ֖י אַבְרָהָ֣ם
# אָבִ֑יו סִתְּמ֣וּם פְּלִשְׁתִּ֔ים וַיְמַלְא֖וּם עָפָֽר
# "[EN-AID] And all the wells that his father's servants had dug in the days
# of Abraham his father, the Philistines stopped them up and filled them
# with earth."
m.step("Gen.26.15")
# ‹הַבְּאֵרֹת אֲשֶׁר חָפְרוּ עַבְדֵי אָבִיו בִּימֵי אַבְרָהָם אָבִיו› fact
# holds: wells-dug-by-avde-avraham-bi-yme-avraham
m.fact("wells_dug_by_avde_avraham_bi_yme_avraham")
# ‹סִתְּמוּם פְּלִשְׁתִּים וַיְמַלְאוּם עָפָר› event: stop-up-and-fill —
# agent pelishtim; theme the-beerot
m.event("stop_up_and_fill", agent="pelishtim", themes=["ha_beerot"])

# -------------------------- Gen.26.16 · THE_EXPULSION_SEAM_LEKH ------------
# וַיֹּ֥אמֶר אֲבִימֶ֖לֶךְ אֶל־יִצְחָ֑ק לֵ֚ךְ מֵֽעִמָּ֔נוּ כִּֽי־עָצַֽמְתָּ
# מִמֶּ֖נּוּ מְאֹֽד
# "[EN-AID] And Abimelech said to Isaac: Go from us, for you have become
# much mightier than we."
m.step("Gen.26.16")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ אֶל־יִצְחָק› event: say — agent avimelekh
m.event("say", agent="avimelekh")
# ‹לֵךְ מֵעִמָּנוּ› avimelekh speaks a demand — LET: lekh(yitzchaq, from-
# imanu)
m.declare("avimelekh", "LET",
          "lekh(yitzchaq, me_imanu)")
# ‹כִּי־עָצַמְתָּ מִמֶּנּוּ מְאֹד› fact holds: atzamta-mime-nu-very
m.fact("atzamta_mime_nu_meod")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'avimelekh', 'pelishtim', 'yitzchaq', 'avraham', 'gerar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['al_tered(yitzchaq, mitzrayim)', 'shekhon(yitzchaq, ba_aretz_asher_omar_elekha)', 'gur(yitzchaq, ba_aretz_ha_zot)', 'lekh(yitzchaq, me_imanu)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['echo_first_famine_days_of_avraham', 've_ehye_im_kha', 'va_avarkhe_ka', 'eten_le_kha_u_le_zara_kha_et_kal_ha_aratzot_ha_el', 'va_haqimoti_et_ha_shevua', 'past_oath_nishbati_le_avraham', 've_hirbeti_zara_kha_ke_khokhve_ha_shamayim', 've_natati_le_zara_kha_ha_aratzot', 've_hitbarakhu_ve_zara_kha_kol_goye_ha_aretz', 'eqev_asher_shama_avraham_be_qoli', 'va_yishmor_mishmarti_mitzvotai_chuqqotai_ve_torotai', 'other_verb_non_pop_shekhon_and_gur', 'achoti_hi_claim_by_yitzchaq', 'yare_le_mor_ishti_pen_yahargu', 'tovat_mareh_hi', 'yitzchaq_metzacheq_et_rivqah_ishto', 'isht_kha_hiv', 'amarta_achoti_hi_requote', 'ma_zot_asita_la_nu', 'near_miss_shakhav_and_asham_brought', 'royal_decree_no_touch_mot_yumat', 'miqne_tzon_vaqar_va_avuda_raba', 'wells_dug_by_avde_avraham_bi_yme_avraham', 'atzamta_mime_nu_meod'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
