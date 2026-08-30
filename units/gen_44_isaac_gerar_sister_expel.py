#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וַיְהִי רָעָב בָּאָרֶץ› (“and-be hunger in-earth”) — event: famine
m.event("famine")
# ‹מִלְּבַד הָרָעָב הָרִאשׁוֹן אֲשֶׁר הָיָה בִּימֵי אַבְרָהָם› (“from-to-
# separation the-hunger the-first which be in-day Abraham”) — fact holds:
# echo-first-famine-days-fowl-Abraham
m.fact("echo_first_famine_days_of_avraham")
# ‹וַיֵּלֶךְ יִצְחָק אֶל־אֲבִימֶּלֶךְ … גְּרָרָה› (“and-go Isaac to
# Abimelech … Gerar-ward”) — event: go — agent Isaac
m.event("go", agent="yitzchaq")
# ‹יִצְחָק … אַבְרָהָם … אֲבִימֶּלֶךְ … גְּרָרָה› (“Isaac … Abraham …
# Abimelech … Gerar-ward”) — reads without prior install (flag, not fix):
# Isaac, Abraham, Abimelech, gerar, Pelishtite
m.presupposed("yitzchaq", "avraham", "avimelekh", "gerar", "pelishtim")
# witness-tier presupposed read: member_of_the_ten_famines_census on
# this_famine — read, not installed
m.witness_read("this_famine", "member_of_the_ten_famines_census",
                cites=["Bereshit Rabbah 25:3", "Bereshit Rabbah 64:2"])

# -------------------------- Gen.26.2 · THE_APPEARANCE_THE_LET_NOT_AND_THE_DWELL -
# וַיֵּרָ֤א אֵלָי֙ו יְהוָ֔ה וַיֹּ֖אמֶר אַל־תֵּרֵ֣ד מִצְרָ֑יְמָה שְׁכֹ֣ן
# בָּאָ֔רֶץ אֲשֶׁ֖ר אֹמַ֥ר אֵלֶֽיךָ
# "[EN-AID] And YHWH appeared to him and said: Do not go down to Egypt;
# dwell in the land that I say to you."
m.step("Gen.26.2")
# ‹וַיֵּרָא אֵלָיו יְהוָה וַיֹּאמֶר› (“and-see to-him/its YHWH and-say”) —
# event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹אַל־תֵּרֵד מִצְרָיְמָה› (“do-not go-down Egypt-ward”) — the-LORD speaks a
# demand — LET-NOT: over-go-down(Isaac, mitzrayim)
m.declare("YHWH", "LET-NOT",
          "al_tered(yitzchaq, mitzrayim)")
# ‹שְׁכֹן בָּאָרֶץ אֲשֶׁר אֹמַר אֵלֶיךָ› (“reside in-earth which say to-
# you/your”) — the-LORD speaks a demand — LET: reside(Isaac, in-the-earth-
# which-say-to-you)
m.declare("YHWH", "LET",
          "shekhon(yitzchaq, ba_aretz_asher_omar_elekha)")
# witness-tier presupposed read:
# offering_disqualification_rule_applied_to_geography on remain_in_this_land
# — read, not installed
m.witness_read("remain_in_this_land", "offering_disqualification_rule_applied_to_geography",
                cites=["Bereshit Rabbah 64:3"])

# -------------------------- Gen.26.3 · THE_SOJOURN_THE_PROMISE_AND_THE_PAST_OATH -
# גּ֚וּר בָּאָ֣רֶץ הַזֹּ֔את וְאֶֽהְיֶ֥ה עִמְּךָ֖ וַאֲבָרְכֶ֑ךָּ כִּֽי־לְךָ֣
# וּֽלְזַרְעֲךָ֗ אֶתֵּן֙ אֶת־כָּל־הָֽאֲרָצֹ֣ת הָאֵ֔ל וַהֲקִֽמֹתִי֙
# אֶת־הַשְּׁבֻעָ֔ה אֲשֶׁ֥ר נִשְׁבַּ֖עְתִּי לְאַבְרָהָ֥ם אָבִֽיךָ
# "[EN-AID] Sojourn in this land, and I will be with you and will bless you;
# for to you and to your seed I will give all these lands, and I will
# establish the oath that I swore to Abraham your father."
m.step("Gen.26.3")
# ‹גּוּר בָּאָרֶץ הַזֹּאת› (“turn-aside-from-the-road in-earth the-this”) —
# the-LORD speaks a demand — LET: turn-aside-from-the-road(Isaac, in-the-
# earth-the-this)
m.declare("YHWH", "LET",
          "gur(yitzchaq, ba_aretz_ha_zot)")
# ‹וְאֶהְיֶה עִמְּךָ וַאֲבָרְכֶךָּ› (“and-be with-you/your and-bless-
# you/your”) — fact holds: and-be-if-you/your; and-avarkhe-like
m.fact("ve_ehye_im_kha",
       "va_avarkhe_ka")
# ‹כִּי־לְךָ וּלְזַרְעֲךָ אֶתֵּן אֶת־כָּל־הָאֲרָצֹת הָאֵל› (“that to-
# you/your and-to-seed-you/your set obj-marker all the-earth the-these”) —
# fact holds: set-to-you/your-and-to-zara-you/your-obj-marker-all-the-earth-
# the-to
m.fact("eten_le_kha_u_le_zara_kha_et_kal_ha_aratzot_ha_el")
# ‹וַהֲקִמֹתִי אֶת־הַשְּׁבֻעָה אֲשֶׁר נִשְׁבַּעְתִּי לְאַבְרָהָם אָבִיךָ›
# (“and-arise obj-marker the-something-sworn which swear to-Abraham father-
# you/your”) — fact holds: and-arise-obj-marker-the-something-sworn; past-
# oath-swear-to-Abraham
m.fact("va_haqimoti_et_ha_shevua",
       "past_oath_nishbati_le_avraham")
# witness-tier presupposed read: partial_grant_with_a_future_instalment on
# these_lands_short_form — read, not installed
m.witness_read("these_lands_short_form", "partial_grant_with_a_future_instalment",
                cites=["Bereshit Rabbah 64:3", "Onkelos Genesis 26:3"])

# -------------------------- Gen.26.4 · THE_SEED_STARS_AND_THE_NATIONS_BLESSING -
# וְהִרְבֵּיתִ֤י אֶֽת־זַרְעֲךָ֙ כְּכוֹכְבֵ֣י הַשָּׁמַ֔יִם וְנָתַתִּ֣י
# לְזַרְעֲךָ֔ אֵ֥ת כָּל־הָאֲרָצֹ֖ת הָאֵ֑ל וְהִתְבָּרֲכ֣וּ בְזַרְעֲךָ֔ כֹּ֖ל
# גּוֹיֵ֥י הָאָֽרֶץ
# "[EN-AID] And I will multiply your seed as the stars of the heavens, and I
# will give to your seed all these lands; and in your seed all nations of
# the earth shall bless themselves."
m.step("Gen.26.4")
# ‹וְהִרְבֵּיתִי … וְנָתַתִּי לְזַרְעֲךָ אֵת כָּל־הָאֲרָצֹת הָאֵל› (“and-
# multiply … and-set to-seed-you/your obj-marker all the-earth the-these”) —
# fact holds: and-multiply-zara-you/your-like-stars-the-heavens; and-set-to-
# zara-you/your-the-earth
m.fact("ve_hirbeti_zara_kha_ke_khokhve_ha_shamayim",
       "ve_natati_le_zara_kha_ha_aratzot")
# ‹וְהִתְבָּרֲכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ› (“and-bless in-seed-
# you/your all nation the-earth”) — fact holds: and-bless-and-zara-you/your-
# all-nation-the-earth
m.fact("ve_hitbarakhu_ve_zara_kha_kol_goye_ha_aretz")

# -------------------------- Gen.26.5 · THE_GROUNDS_BECAUSE_ABRAHAM_LISTENED -
# עֵ֕קֶב אֲשֶׁר־שָׁמַ֥ע אַבְרָהָ֖ם בְּקֹלִ֑י וַיִּשְׁמֹר֙ מִשְׁמַרְתִּ֔י
# מִצְוֺתַ֖י חֻקּוֹתַ֥י וְתוֹרֹתָֽי
# "[EN-AID] because Abraham listened to My voice and kept My charge, My
# commandments, My statutes, and My teachings."
m.step("Gen.26.5")
# ‹עֵקֶב אֲשֶׁר־שָׁמַע אַבְרָהָם בְּקֹלִי› (“heel which hear Abraham in-
# voice/sound-me/my”) — fact holds: heel-which-hear-Abraham-in-qoli
m.fact("eqev_asher_shama_avraham_be_qoli")
# ‹וַיִּשְׁמֹר מִשְׁמַרְתִּי מִצְוֺתַי חֻקּוֹתַי וְתוֹרֹתָי› (“and-
# keep/guard watch-me/my commandment-me/my statute-me/my and-precept-me/my”)
# — fact holds: and-keep/guard-mishmarti-mitzvotai-chuqqotai-and-torotai
m.fact("va_yishmor_mishmarti_mitzvotai_chuqqotai_ve_torotai")
# witness-tier presupposed read: numeric_value_172_and_the_age_of_three on
# the_opening_word — read, not installed
m.witness_read("the_opening_word", "numeric_value_172_and_the_age_of_three",
                cites=["Bereshit Rabbah 64:4"])
# witness-tier presupposed read: whole_system_known_before_sinai on
# the_stacked_law_words — read, not installed
m.witness_read("the_stacked_law_words", "whole_system_known_before_sinai",
                cites=["Bereshit Rabbah 64:4", "Onkelos Genesis 26:5"])

# -------------------------- Gen.26.6 · THE_DWELL_OTHER_VERB_CENTERPIECE ----
# וַיֵּ֥שֶׁב יִצְחָ֖ק בִּגְרָֽר
# "[EN-AID] And Isaac dwelt in Gerar."
m.step("Gen.26.6")
# ‹וַיֵּשֶׁב יִצְחָק בִּגְרָר› (“and-dwell/sit Isaac in-Gerar”) — event:
# dwell — agent Isaac
m.event("dwell", agent="yitzchaq")
# ‹וַיֵּשֶׁב ← שְׁכֹן / גּוּר› (“and-dwell/sit reside cub”) — fact holds:
# other-verb-non-pop-reside-and-turn-aside-from-the-road
m.fact("other_verb_non_pop_shekhon_and_gur")

# -------------------------- Gen.26.7 · THE_SISTER_CLAIM_ISAAC_LIVE ---------
# וַֽיִּשְׁאֲל֞וּ אַנְשֵׁ֤י הַמָּקוֹם֙ לְאִשְׁתּ֔וֹ וַיֹּ֖אמֶר אֲחֹ֣תִי
# הִ֑וא כִּ֤י יָרֵא֙ לֵאמֹ֣ר אִשְׁתִּ֔י פֶּן־יַֽהַרְגֻ֜נִי אַנְשֵׁ֤י
# הַמָּקוֹם֙ עַל־רִבְקָ֔ה כִּֽי־טוֹבַ֥ת מַרְאֶ֖ה הִֽיא
# "[EN-AID] And the men of the place asked about his wife; and he said: She
# is my sister — for he feared to say, My wife, lest the men of the place
# kill me on account of Rivqah, for she is good of appearance."
m.step("Gen.26.7")
# ‹וַיִּשְׁאֲלוּ … וַיֹּאמֶר› (“and-inquire … and-say”) — event: ?
m.event("?")
# ‹אֲחֹתִי הִוא› (“sister-me/my he/it”) — fact holds: achoti-he/it-claim-by-
# Isaac
m.fact("achoti_hi_claim_by_yitzchaq")
# ‹כִּי יָרֵא … כִּי־טוֹבַת מַרְאֶה הִיא› (“that fear … that good appearance
# he/it”) — fact holds: fear-to-say-ishti-lest-yahargu; good-appearance-
# he/it
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
# ‹אָרְכוּ … וַיַּשְׁקֵף … וַיַּרְא› (“be-long … and-lean-out … and-see”) —
# event: ?
m.event("?")
# ‹יִצְחָק מְצַחֵק אֵת רִבְקָה אִשְׁתּוֹ› (“Isaac laugh-outright with
# Rebekah woman-him/its”) — fact holds: Isaac-laugh-outright-obj-marker-
# rivqah-his-wife
m.fact("yitzchaq_metzacheq_et_rivqah_ishto")
# witness-tier presupposed read: modesty_law_cluster_with_its_exception on
# the_word_playing — read, not installed
m.witness_read("the_word_playing", "modesty_law_cluster_with_its_exception",
                cites=["Bereshit Rabbah 64:5"])

# -------------------------- Gen.26.9 · THE_SUMMONS_AND_THE_RE_QUOTE --------
# וַיִּקְרָ֨א אֲבִימֶ֜לֶךְ לְיִצְחָ֗ק וַיֹּ֨אמֶר֙ אַ֣ךְ הִנֵּ֤ה אִשְׁתְּךָ֙
# הִ֔וא וְאֵ֥יךְ אָמַ֖רְתָּ אֲחֹ֣תִי הִ֑וא וַיֹּ֤אמֶר אֵלָי֙ו יִצְחָ֔ק כִּ֣י
# אָמַ֔רְתִּי פֶּן־אָמ֖וּת עָלֶֽיהָ
# "[EN-AID] And Abimelech called Isaac and said: Behold, of a surety she is
# your wife; and how did you say, She is my sister? And Isaac said to him:
# Because I said, Lest I die because of her."
m.step("Gen.26.9")
# ‹וַיִּקְרָא אֲבִימֶלֶךְ לְיִצְחָק וַיֹּאמֶר … וַיֹּאמֶר אֵלָיו יִצְחָק›
# (“and-call Abimelech to-Isaac and-say … and-say to-him/its Isaac”) —
# event: ?
m.event("?")
# ‹הִנֵּה אִשְׁתְּךָ הִוא … אָמַרְתָּ אֲחֹתִי הִוא› (“behold woman-you/your
# he/it … say sister-me/my he/it”) — fact holds: isht-you/your-he/it; say-
# achoti-he/it-requote
m.fact("isht_kha_hiv",
       "amarta_achoti_hi_requote")

# -------------------------- Gen.26.10 · THE_WHAT_HAVE_YOU_DONE_AND_THE_GUILT_DEBUT -
# וַיֹּ֣אמֶר אֲבִימֶ֔לֶךְ מַה־זֹּ֖את עָשִׂ֣יתָ לָּ֑נוּ כִּ֠מְעַט שָׁכַ֞ב
# אַחַ֤ד הָעָם֙ אֶת־אִשְׁתֶּ֔ךָ וְהֵבֵאתָ֥ עָלֵ֖ינוּ אָשָֽׁם
# "[EN-AID] And Abimelech said: What is this you have done to us? One of the
# people might easily have lain with your wife, and you would have brought
# guilt upon us."
m.step("Gen.26.10")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ› (“and-say Abimelech”) — event: say — agent
# Abimelech
m.event("say", agent="avimelekh")
# ‹מַה־זֹּאת עָשִׂיתָ לָּנוּ› (“what this make to-us/our”) — fact holds:
# what-this-make-to-us/our
m.fact("ma_zot_asita_la_nu")
# ‹כִּמְעַט שָׁכַב … וְהֵבֵאתָ עָלֵינוּ אָשָׁם› (“like-little lie-down …
# and-come/bring over-us/our guilt”) — fact holds: near-miss-lie-down-and-
# guilt-brought
m.fact("near_miss_shakhav_and_asham_brought")
# witness-tier presupposed read: rendered_as_the_distinguished_one on
# one_of_the_people — read, not installed
m.witness_read("one_of_the_people", "rendered_as_the_distinguished_one",
                cites=["Onkelos Genesis 26:10"])

# -------------------------- Gen.26.11 · THE_ROYAL_DECREE_MOT_YUMAT ---------
# וַיְצַ֣ו אֲבִימֶ֔לֶךְ אֶת־כָּל־הָעָ֖ם לֵאמֹ֑ר הַנֹּגֵ֜עַ בָּאִ֥ישׁ הַזֶּ֛ה
# וּבְאִשְׁתּ֖וֹ מ֥וֹת יוּמָֽת
# "[EN-AID] And Abimelech commanded all the people, saying: He who touches
# this man or his wife shall surely be put to death."
m.step("Gen.26.11")
# ‹וַיְצַו אֲבִימֶלֶךְ אֶת־כָּל־הָעָם› (“and-command Abimelech obj-marker
# all the-people”) — event: command — agent Abimelech
m.event("command", agent="avimelekh")
# ‹הַנֹּגֵעַ בָּאִישׁ הַזֶּה וּבְאִשְׁתּוֹ מוֹת יוּמָת› (“the-touch in-man
# the-this and-in-woman-him/its die die”) — fact holds: royal-decree-no-
# touch-die-die
m.fact("royal_decree_no_touch_mot_yumat")

# -------------------------- Gen.26.12 · THE_HUNDREDFOLD_AND_THE_BLESSING ---
# וַיִּזְרַ֤ע יִצְחָק֙ בָּאָ֣רֶץ הַהִ֔וא וַיִּמְצָ֛א בַּשָּׁנָ֥ה הַהִ֖וא
# מֵאָ֣ה שְׁעָרִ֑ים וַֽיְבָרֲכֵ֖הוּ יְהוָֽה
# "[EN-AID] And Isaac sowed in that land and found in that year a hundred
# measures; and YHWH blessed him."
m.step("Gen.26.12")
# ‹וַיִּזְרַע … וַיִּמְצָא … מֵאָה שְׁעָרִים› (“and-yield-seed … and-find …
# hundred measure”) — event: sow-and-find — agent Isaac; theme hundred-
# measure
m.event("sow_and_find", agent="yitzchaq", themes=["mea_shearim"])
# ‹וַיְבָרֲכֵהוּ יְהוָה› (“and-bless-him/its YHWH”) — event: ?
m.event("?")
# witness-tier presupposed read:
# two_standing_rules_colliding_and_adjudicated on the_hundredfold — read,
# not installed
m.witness_read("the_hundredfold", "two_standing_rules_colliding_and_adjudicated",
                cites=["Bereshit Rabbah 64:6", "Onkelos Genesis 26:12"])
# witness-tier presupposed read: first_member_of_a_proximity_census on
# enrichment_of_the_host — read, not installed
m.witness_read("enrichment_of_the_host", "first_member_of_a_proximity_census",
                cites=["Bereshit Rabbah 73:8"])

# -------------------------- Gen.26.13 · THE_MAN_GREW_VERY_GREAT ------------
# וַיִּגְדַּ֖ל הָאִ֑ישׁ וַיֵּ֤לֶךְ הָלוֹךְ֙ וְגָדֵ֔ל עַ֥ד כִּֽי־גָדַ֖ל
# מְאֹֽד
# "[EN-AID] And the man became great, and grew more and more until he became
# very great."
m.step("Gen.26.13")
# ‹וַיִּגְדַּל … הָלוֹךְ וְגָדֵל … גָדַל מְאֹד› (“and-be-large … walk/go
# and-large … be-large very”) — event: grow-great
m.event("grow_great")

# -------------------------- Gen.26.14 · THE_FLOCKS_AND_THE_ENVY_DEBUT ------
# וַֽיְהִי־ל֤וֹ מִקְנֵה־צֹאן֙ וּמִקְנֵ֣ה בָקָ֔ר וַעֲבֻדָּ֖ה רַבָּ֑ה
# וַיְקַנְא֥וּ אֹת֖וֹ פְּלִשְׁתִּֽים
# "[EN-AID] And he had possessions of flocks and possessions of herds and a
# great household; and the Philistines envied him."
m.step("Gen.26.14")
# ‹מִקְנֵה־צֹאן וּמִקְנֵה בָקָר וַעֲבֻדָּה רַבָּה› (“something-bought flock
# and-something-bought herd and-something-wrought many/great”) — fact holds:
# something-bought-flock-herd-and-something-wrought-many/great
m.fact("miqne_tzon_vaqar_va_avuda_raba")
# ‹וַיְקַנְאוּ אֹתוֹ פְּלִשְׁתִּים› (“and-be-zealous obj-marker-him/its
# Pelishtite”) — event: envy — agent Pelishtite
m.event("envy", agent="pelishtim")
# witness-tier presupposed read: service_maxim_on_a_missing_letter on
# household_written_short — read, not installed
m.witness_read("household_written_short", "service_maxim_on_a_missing_letter",
                cites=["Bereshit Rabbah 64:7"])

# -------------------------- Gen.26.15 · THE_STOPPED_WELLS_OF_ABRAHAMS_DAYS -
# וְכָל־הַבְּאֵרֹ֗ת אֲשֶׁ֤ר חָֽפְרוּ֙ עַבְדֵ֣י אָבִ֔יו בִּימֵ֖י אַבְרָהָ֣ם
# אָבִ֑יו סִתְּמ֣וּם פְּלִשְׁתִּ֔ים וַיְמַלְא֖וּם עָפָֽר
# "[EN-AID] And all the wells that his father's servants had dug in the days
# of Abraham his father, the Philistines stopped them up and filled them
# with earth."
m.step("Gen.26.15")
# ‹הַבְּאֵרֹת אֲשֶׁר חָפְרוּ עַבְדֵי אָבִיו בִּימֵי אַבְרָהָם אָבִיו› (“the-
# pit which dig servant father-him/its in-day Abraham father-him/its”) —
# fact holds: wells-dug-by-servant-Abraham-bi-yme-Abraham
m.fact("wells_dug_by_avde_avraham_bi_yme_avraham")
# ‹סִתְּמוּם פְּלִשְׁתִּים וַיְמַלְאוּם עָפָר› (“stop-up-them/their
# Pelishtite and-fill-them/their dust”) — event: stop-up-and-fill — agent
# Pelishtite; theme the-pit
m.event("stop_up_and_fill", agent="pelishtim", themes=["ha_beerot"])

# -------------------------- Gen.26.16 · THE_EXPULSION_SEAM_LEKH ------------
# וַיֹּ֥אמֶר אֲבִימֶ֖לֶךְ אֶל־יִצְחָ֑ק לֵ֚ךְ מֵֽעִמָּ֔נוּ כִּֽי־עָצַֽמְתָּ
# מִמֶּ֖נּוּ מְאֹֽד
# "[EN-AID] And Abimelech said to Isaac: Go from us, for you have become
# much mightier than we."
m.step("Gen.26.16")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ אֶל־יִצְחָק› (“and-say Abimelech to Isaac”) —
# event: say — agent Abimelech
m.event("say", agent="avimelekh")
# ‹לֵךְ מֵעִמָּנוּ› (“go from-with-us/our”) — Abimelech speaks a demand —
# LET: go(Isaac, from-imanu)
m.declare("avimelekh", "LET",
          "lekh(yitzchaq, me_imanu)")
# ‹כִּי־עָצַמְתָּ מִמֶּנּוּ מְאֹד› (“that bind-fast from-us/our very”) —
# fact holds: bind-fast-mime-us/our-very
m.fact("atzamta_mime_nu_meod")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'avimelekh', 'avraham', 'gerar', 'pelishtim', 'yitzchaq'}
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('this_famine', 'member_of_the_ten_famines_census'), ('remain_in_this_land', 'offering_disqualification_rule_applied_to_geography'), ('these_lands_short_form', 'partial_grant_with_a_future_instalment'), ('the_opening_word', 'numeric_value_172_and_the_age_of_three'), ('the_stacked_law_words', 'whole_system_known_before_sinai'), ('the_word_playing', 'modesty_law_cluster_with_its_exception'), ('one_of_the_people', 'rendered_as_the_distinguished_one'), ('the_hundredfold', 'two_standing_rules_colliding_and_adjudicated'), ('enrichment_of_the_host', 'first_member_of_a_proximity_census'), ('household_written_short', 'service_maxim_on_a_missing_letter')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 25:3', 'Bereshit Rabbah 64:2']
    assert all('member_of_the_ten_famines_census' not in f for f in m.WORLD["facts"])
    assert 'this_famine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 64:3']
    assert all('offering_disqualification_rule_applied_to_geography' not in f for f in m.WORLD["facts"])
    assert 'remain_in_this_land' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 64:3', 'Onkelos Genesis 26:3']
    assert all('partial_grant_with_a_future_instalment' not in f for f in m.WORLD["facts"])
    assert 'these_lands_short_form' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 64:4']
    assert all('numeric_value_172_and_the_age_of_three' not in f for f in m.WORLD["facts"])
    assert 'the_opening_word' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 64:4', 'Onkelos Genesis 26:5']
    assert all('whole_system_known_before_sinai' not in f for f in m.WORLD["facts"])
    assert 'the_stacked_law_words' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 64:5']
    assert all('modesty_law_cluster_with_its_exception' not in f for f in m.WORLD["facts"])
    assert 'the_word_playing' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Onkelos Genesis 26:10']
    assert all('rendered_as_the_distinguished_one' not in f for f in m.WORLD["facts"])
    assert 'one_of_the_people' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 64:6', 'Onkelos Genesis 26:12']
    assert all('two_standing_rules_colliding_and_adjudicated' not in f for f in m.WORLD["facts"])
    assert 'the_hundredfold' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 73:8']
    assert all('first_member_of_a_proximity_census' not in f for f in m.WORLD["facts"])
    assert 'enrichment_of_the_host' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 64:7']
    assert all('service_maxim_on_a_missing_letter' not in f for f in m.WORLD["facts"])
    assert 'household_written_short' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
