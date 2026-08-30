#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_55_two_camps_wrestled_name — 32:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_55_two_camps_wrestled_name.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The two camps, the gift, and the wrestled name (32:1-33)"""
from machine import Machine

m = Machine("gen_55_two_camps_wrestled_name")

# -------------------------- Gen.32.1 · THE_FAREWELL_KISS -------------------
# וַיַּשְׁכֵּם לָבָן בַּבֹּקֶר וַיְנַשֵּׁק לְבָנָיו וְלִבְנוֹתָיו וַיְבָרֶךְ
# אֶתְהֶם וַיֵּלֶךְ וַיָּשָׁב לָבָן לִמְקֹמוֹ
# "[EN-AID] And Laban rose early in the morning and kissed his sons and his
# daughters and blessed them; and Laban went and returned to his place."
m.step("Gen.32.1")
# ‹וַיַּשְׁכֵּם לָבָן בַּבֹּקֶר וַיְנַשֵּׁק› (“and-rise-early Laban in-
# morning and-kiss”) — fact holds: and-kiss-and-bless-and-return(Laban, to-
# me-meqomo)
m.fact("va_yenasheq_va_yevarekh_va_yashav(lavan, li_meqomo)")

# -------------------------- Gen.32.2 · THE_ANGEL_ENCOUNTER -----------------
# וְיַעֲקֹב הָלַךְ לְדַרְכּוֹ וַיִּפְגְּעוּ־בוֹ מַלְאֲכֵי אֱלֹהִים
# "[EN-AID] And Jacob went on his way, and messengers of God met him."
m.step("Gen.32.2")
# ‹וַיִּפְגְּעוּ־בוֹ מַלְאֲכֵי אֱלֹהִים› (“and-impinge in-him/its messenger
# God”) — fact holds: and-impinge-vo-messenger-God(Jacob, come/bring-derekh)
m.fact("va_yifgu_vo_malakhe_Elohim(yaaqov, ba_derekh)")

# -------------------------- Gen.32.3 · THE_DUAL_NAME -----------------------
# וַיֹּאמֶר יַעֲקֹב כַּאֲשֶׁר רָאָם מַחֲנֵה אֱלֹהִים זֶה וַיִּקְרָא
# שֵׁם־הַמָּקוֹם הַהוּא מַחֲנָיִם
# "[EN-AID] And Jacob said when he saw them: This is God's camp. And he
# called the name of that place Machanayim [Two Camps]."
m.step("Gen.32.3")
# ‹מַחֲנֵה אֱלֹהִים זֶה› (“camp God this”) — the world gains: place-Mahanaim
m.install("maqom_machanayim")
# ‹וַיִּקְרָא שֵׁם־הַמָּקוֹם הַהוּא מַחֲנָיִם› (“and-call name the-place
# that Mahanaim”) — named: place-Mahanaim := Mahanaim
m.name("maqom_machanayim", "machanayim")

# -------------------------- Gen.32.4 · THE_ENVOYS --------------------------
# וַיִּשְׁלַח יַעֲקֹב מַלְאָכִים לְפָנָיו אֶל־עֵשָׂו אָחִיו אַרְצָה שֵׂעִיר
# שְׂדֵה אֱדוֹם
# "[EN-AID] And Jacob sent messengers before him to Esau his brother, to the
# land of Seir, the field of Edom."
m.step("Gen.32.4")
# ‹וַיִּשְׁלַח יַעֲקֹב מַלְאָכִים לְפָנָיו› (“and-send Jacob messenger to-
# face-him/its”) — fact holds: and-send-messenger-to-Esau(Jacob, artza-Seir)
m.fact("va_yishlach_malakhim_el_esav(yaaqov, artza_seir)")

# -------------------------- Gen.32.5 · THE_SAY_INSTRUCTION -----------------
# וַיְצַו אֹתָם לֵאמֹר כֹּה תֹאמְרוּן לַאדֹנִי לְעֵשָׂו כֹּה אָמַר עַבְדְּךָ
# יַעֲקֹב עִם־לָבָן גַּרְתִּי וָאֵחַר עַד־עָתָּה
# "[EN-AID] And he commanded them, saying: Thus shall you say to my lord, to
# Esau: Thus said your servant Jacob: With Laban I have sojourned, and I
# have tarried until now."
m.step("Gen.32.5")
# ‹כֹּה תֹאמְרוּן לַאדֹנִי לְעֵשָׂו› (“like-this say-ward to-lord-me/my to-
# Esau”) — Jacob speaks a demand — LET?: tomrun(the-messenger, to-doni-to-
# Esau)
m.declare("yaaqov", "LET?",
          "tomrun(ha_malakhim, la_doni_le_esav)")
# witness-tier presupposed read: priced_in_dynasties_and_paid_at_gen_59 on
# my_lord_eight_times — read, not installed
m.witness_read("my_lord_eight_times", "priced_in_dynasties_and_paid_at_gen_59",
                cites=["Bereshit Rabbah 75:11"])
# witness-tier presupposed read:
# criticized_by_the_chain_against_its_own_subject on the_embassy — read, not
# installed
m.witness_read("the_embassy", "criticized_by_the_chain_against_its_own_subject",
                cites=["Bereshit Rabbah 75:2", "Bereshit Rabbah 75:3"])

# -------------------------- Gen.32.6 · THE_INVENTORY_MESSAGE ---------------
# וַיְהִי־לִי שׁוֹר וַחֲמוֹר צֹאן וְעֶבֶד וְשִׁפְחָה וָאֶשְׁלְחָה לְהַגִּיד
# לַאדֹנִי לִמְצֹא־חֵן בְּעֵינֶיךָ
# "[EN-AID] And I have ox and donkey, flock and servant and maid; and I send
# to tell my lord, to find grace in your eyes."
m.step("Gen.32.6")
# ‹וַיְהִי־לִי שׁוֹר וַחֲמוֹר צֹאן וְעֶבֶד וְשִׁפְחָה› (“and-be to-me/my
# bullock and-male-ass flock and-servant and-female-slave”) — fact holds:
# and-be-to-me-bullock-and-male-ass(divre-the-shelichut)
m.fact("va_yehi_li_shor_va_chamor(divre_ha_shelichut)")

# -------------------------- Gen.32.7 · THE_FOUR_HUNDRED --------------------
# וַיָּשֻׁבוּ הַמַּלְאָכִים אֶל־יַעֲקֹב לֵאמֹר בָּאנוּ אֶל־אָחִיךָ
# אֶל־עֵשָׂו וְגַם הֹלֵךְ לִקְרָאתְךָ וְאַרְבַּע־מֵאוֹת אִישׁ עִמּוֹ
# "[EN-AID] And the messengers returned to Jacob, saying: We came to your
# brother, to Esau — and he also is coming to meet you, and four hundred men
# with him."
m.step("Gen.32.7")
# ‹בָּאנוּ אֶל־אָחִיךָ אֶל־עֵשָׂו› (“come/bring to brother-you/your to
# Esau”) — fact holds: come/bring-to-your-brother-and-four-hundred-
# man(report)
m.fact("banu_el_achikha_ve_arba_meot_ish(report)")

# -------------------------- Gen.32.8 · THE_SPLIT ---------------------------
# וַיִּירָא יַעֲקֹב מְאֹד וַיֵּצֶר לוֹ וַיַּחַץ אֶת־הָעָם אֲשֶׁר־אִתּוֹ
# וְאֶת־הַצֹּאן וְאֶת־הַבָּקָר וְהַגְּמַלִּים לִשְׁנֵי מַחֲנוֹת
# "[EN-AID] And Jacob feared greatly, and it distressed him; and he divided
# the people that were with him, and the flock and the herd and the camels,
# into two camps."
m.step("Gen.32.8")
# ‹וַיִּירָא יַעֲקֹב מְאֹד וַיֵּצֶר› (“and-fear Jacob very and-press”) —
# fact holds: and-fear-and-cut-to-me-shene-camp(Jacob)
m.fact("va_yira_va_yachatz_li_shene_machanot(yaaqov)")
# witness-tier presupposed read: risk_distribution_maxim_minted_here on
# divided_the_camp — read, not installed
m.witness_read("divided_the_camp", "risk_distribution_maxim_minted_here",
                cites=["Bereshit Rabbah 76:3"])

# -------------------------- Gen.32.9 · THE_REMNANT_ARITHMETIC --------------
# וַיֹּאמֶר אִם־יָבוֹא עֵשָׂו אֶל־הַמַּחֲנֶה הָאַחַת וְהִכָּהוּ וְהָיָה
# הַמַּחֲנֶה הַנִּשְׁאָר לִפְלֵיטָה
# "[EN-AID] And he said: If Esau comes to the one camp and strikes it, the
# remaining camp will become a remnant."
m.step("Gen.32.9")
# ‹וְהָיָה הַמַּחֲנֶה הַנִּשְׁאָר לִפְלֵיטָה› (“and-be the-camp the-swell-up
# to-deliverance”) — fact holds: with-come/bring-and-hikahu-and-be-to-me-
# feleta(tokhnit)
m.fact("im_yavo_ve_hikahu_ve_haya_li_feleta(tokhnit)")

# -------------------------- Gen.32.10 · THE_REQUOTE_LADDER_OPENS -----------
# וַיֹּאמֶר יַעֲקֹב אֱלֹהֵי אָבִי אַבְרָהָם וֵאלֹהֵי אָבִי יִצְחָק יְהוָה
# הָאֹמֵר אֵלַי שׁוּב לְאַרְצְךָ וּלְמוֹלַדְתְּךָ וְאֵיטִיבָה עִמָּךְ
# "[EN-AID] And Jacob said: God of my father Abraham and God of my father
# Isaac, YHWH, who says to me: Return to your land and to your kindred, and
# I will do good with you."
m.step("Gen.32.10")
# ‹שׁוּב לְאַרְצְךָ וּלְמוֹלַדְתְּךָ וְאֵיטִיבָה עִמָּךְ› (“return to-earth-
# you/your and-to-nativity-you/your and-be-make-well with-you/your”) — fact
# holds: retell-return-to-artzekha-and-be-make-well(tefila, delta-x2)
m.fact("retell_shuv_le_artzekha_ve_etiva(tefila, delta_x2)")
# witness-tier presupposed read: descent_does_not_secure_the_name on
# God_of_my_fathers_and_not_of_esau — read, not installed
m.witness_read("God_of_my_fathers_and_not_of_esau", "descent_does_not_secure_the_name",
                cites=["Bereshit Rabbah 76:4"])

# -------------------------- Gen.32.11 · THE_TOO_SMALL ----------------------
# קָטֹנְתִּי מִכֹּל הַחֲסָדִים וּמִכָּל־הָאֱמֶת אֲשֶׁר עָשִׂיתָ
# אֶת־עַבְדֶּךָ כִּי בְמַקְלִי עָבַרְתִּי אֶת־הַיַּרְדֵּן הַזֶּה וְעַתָּה
# הָיִיתִי לִשְׁנֵי מַחֲנוֹת
# "[EN-AID] I am too small for all the kindnesses and all the truth that You
# have done for Your servant; for with my staff I crossed this Jordan, and
# now I have become two camps."
m.step("Gen.32.11")
# ‹קָטֹנְתִּי מִכֹּל הַחֲסָדִים וּמִכָּל־הָאֱמֶת› (“diminish from-all the-
# kindness and-from-all the-stability”) — fact holds: diminish-who?-all-the-
# kindness(tefila)
m.fact("qatonti_mi_kol_ha_chasadim(tefila)")
# witness-tier presupposed read: merit_as_a_finite_balance_drawn_down on
# i_am_small — read, not installed
m.witness_read("i_am_small", "merit_as_a_finite_balance_drawn_down",
                cites=["Bereshit Rabbah 76:5", "Onkelos Genesis 32:11"])

# -------------------------- Gen.32.12 · THE_RESCUE_DEMAND ------------------
# הַצִּילֵנִי נָא מִיַּד אָחִי מִיַּד עֵשָׂו כִּי־יָרֵא אָנֹכִי אֹתוֹ
# פֶּן־יָבוֹא וְהִכַּנִי אֵם עַל־בָּנִים
# "[EN-AID] Rescue me, please, from the hand of my brother, from the hand of
# Esau; for I fear him, lest he come and strike me, mother upon children."
m.step("Gen.32.12")
# ‹הַצִּילֵנִי נָא מִיַּד אָחִי מִיַּד עֵשָׂו› (“snatch-away-me/my please
# from-hand brother-me/my from-hand Esau”) — Jacob speaks a demand — LET:
# hatzileni(the-LORD, who?-hand-Esau)
m.declare("yaaqov", "LET",
          "hatzileni(YHWH, mi_yad_esav)")
# witness-tier presupposed read: argued_from_a_statute_not_yet_given on
# the_plea — read, not installed
m.witness_read("the_plea", "argued_from_a_statute_not_yet_given",
                cites=["Bereshit Rabbah 75:13"])

# -------------------------- Gen.32.13 · THE_UNSOURCED_DOUBLET --------------
# וְאַתָּה אָמַרְתָּ הֵיטֵב אֵיטִיב עִמָּךְ וְשַׂמְתִּי אֶת־זַרְעֲךָ כְּחוֹל
# הַיָּם אֲשֶׁר לֹא־יִסָּפֵר מֵרֹב
# "[EN-AID] And You said: Doing good I will do good with you, and I will
# make your seed as the sand of the sea, which cannot be counted for
# multitude."
m.step("Gen.32.13")
# ‹וְאַתָּה אָמַרְתָּ הֵיטֵב אֵיטִיב עִמָּךְ› (“and-you say do-well do-well
# with-you/your”) — fact holds: say-do-well-do-well-like-sand-the-
# seas(tefila, delta-x2)
m.fact("amarta_hetev_etiv_ke_chol_ha_yam(tefila, delta_x2)")

# -------------------------- Gen.32.14 · THE_GIFT_TAKEN ---------------------
# וַיָּלֶן שָׁם בַּלַּיְלָה הַהוּא וַיִּקַּח מִן־הַבָּא בְיָדוֹ מִנְחָה
# לְעֵשָׂו אָחִיו
# "[EN-AID] And he lodged there that night; and he took from what came to
# his hand a gift for Esau his brother."
m.step("Gen.32.14")
# ‹וַיִּקַּח מִן־הַבָּא בְיָדוֹ מִנְחָה לְעֵשָׂו אָחִיו› (“and-take from
# the-come/bring in-hand-him/its grain-offering to-Esau brother-him/its”) —
# fact holds: and-take-grain-offering-to-Esau(Jacob, from-the-come/bring-
# and-his-hand)
m.fact("va_yiqach_mincha_le_esav(yaaqov, min_ha_ba_ve_yado)")

# -------------------------- Gen.32.15 · THE_HERD_LIST_ONE ------------------
# עִזִּים מָאתַיִם וּתְיָשִׁים עֶשְׂרִים רְחֵלִים מָאתַיִם וְאֵילִים
# עֶשְׂרִים
# "[EN-AID] Two hundred she-goats and twenty he-goats, two hundred ewes and
# twenty rams,"
m.step("Gen.32.15")
# ‹עִזִּים מָאתַיִם וּתְיָשִׁים עֶשְׂרִים› (“she-goat hundred and-buck
# twenty”) — fact holds: she-goat-buck-ewe-ram(minchat-the-flock)
m.fact("izim_teyashim_rechelim_elim(minchat_ha_tzon)")

# -------------------------- Gen.32.16 · THE_HERD_LIST_TWO ------------------
# גְּמַלִּים מֵינִיקוֹת וּבְנֵיהֶם שְׁלֹשִׁים פָּרוֹת אַרְבָּעִים וּפָרִים
# עֲשָׂרָה אֲתֹנֹת עֶשְׂרִים וַעְיָרִם עֲשָׂרָה
# "[EN-AID] Thirty nursing camels with their young, forty cows and ten
# bulls, twenty she-donkeys and ten colts."
m.step("Gen.32.16")
# ‹גְּמַלִּים מֵינִיקוֹת וּבְנֵיהֶם שְׁלֹשִׁים› (“camel suck and-son-
# them/their thirty”) — fact holds: camel-cow-parim-female-donkey-young-
# ass(minchat-the-beemot)
m.fact("gemalim_parot_parim_atonot_eyarim(minchat_ha_beemot)")

# -------------------------- Gen.32.17 · THE_PASS_ORDER ---------------------
# וַיִּתֵּן בְּיַד־עֲבָדָיו עֵדֶר עֵדֶר לְבַדּוֹ וַיֹּאמֶר אֶל־עֲבָדָיו
# עִבְרוּ לְפָנַי וְרֶוַח תָּשִׂימוּ בֵּין עֵדֶר וּבֵין עֵדֶר
# "[EN-AID] And he gave them into the hand of his servants, drove by drove
# alone, and said to his servants: Pass over before me, and put a space
# between drove and drove."
m.step("Gen.32.17")
# ‹עִבְרוּ לְפָנַי› (“pass-over to-face-me/my”) — Jacob speaks a demand —
# LET: pass-over(avadav, to-fanai)
m.declare("yaaqov", "LET",
          "ivru(avadav, le_fanai)")
# ‹וְרֶוַח תָּשִׂימוּ בֵּין עֵדֶר וּבֵין עֵדֶר› (“and-room put/set between
# arrangement and-between arrangement”) — Jacob speaks a demand — LET?:
# put/set(room, between-arrangement-and-between-arrangement)
m.declare("yaaqov", "LET?",
          "tasimu(revach, ben_eder_u_ven_eder)")

# -------------------------- Gen.32.18 · THE_FIRST_WAVE_SCRIPT --------------
# וַיְצַו אֶת־הָרִאשׁוֹן לֵאמֹר כִּי יִפְגָּשְׁךָ עֵשָׂו אָחִי וִשְׁאֵלְךָ
# לֵאמֹר לְמִי־אַתָּה וְאָנָה תֵלֵךְ וּלְמִי אֵלֶּה לְפָנֶיךָ
# "[EN-AID] And he commanded the first, saying: When Esau my brother meets
# you and asks you, saying: Whose are you, and where do you go, and whose
# are these before you?"
m.step("Gen.32.18")
# ‹כִּי יִפְגָּשְׁךָ עֵשָׂו אָחִי וִשְׁאֵלְךָ› (“that come-in-contact-with-
# you/your Esau brother-me/my and-inquire-you/your”) — fact holds: that-
# yifgashkha-Esau-and-sheelkha(tzav-first)
m.fact("ki_yifgashkha_esav_u_sheelkha(tzav_rishon)")

# -------------------------- Gen.32.19 · THE_SCRIPTED_ANSWER ----------------
# וְאָמַרְתָּ לְעַבְדְּךָ לְיַעֲקֹב מִנְחָה הִוא שְׁלוּחָה לַאדֹנִי לְעֵשָׂו
# וְהִנֵּה גַם־הוּא אַחֲרֵינוּ
# "[EN-AID] Then you shall say: Your servant Jacob's — it is a gift sent to
# my lord, to Esau; and behold, he also is behind us."
m.step("Gen.32.19")
# ‹מִנְחָה הִוא שְׁלוּחָה לַאדֹנִי› (“grain-offering he/it send to-lord-
# me/my”) — fact holds: grain-offering-hi-send-and-behold-that-
# acharenu(maane)
m.fact("mincha_hi_shelucha_ve_hine_hu_acharenu(maane)")

# -------------------------- Gen.32.20 · THE_SECOND_SAY_CARD ----------------
# וַיְצַו גַּם אֶת־הַשֵּׁנִי גַּם אֶת־הַשְּׁלִישִׁי גַּם אֶת־כָּל־הַהֹלְכִים
# אַחֲרֵי הָעֲדָרִים לֵאמֹר כַּדָּבָר הַזֶּה תְּדַבְּרוּן אֶל־עֵשָׂו
# בְּמֹצַאֲכֶם אֹתוֹ
# "[EN-AID] And he commanded also the second, also the third, also all who
# walked behind the droves, saying: According to this word shall you speak
# to Esau when you find him."
m.step("Gen.32.20")
# ‹כַּדָּבָר הַזֶּה תְּדַבְּרוּן אֶל־עֵשָׂו בְּמֹצַאֲכֶם אֹתוֹ› (“like-
# word/thing the-this speak-ward to Esau in-find-you/your(pl) obj-marker-
# him/its”) — Jacob speaks a demand — LET?: tedabrun(all-the-walk/go, to-
# Esau)
m.declare("yaaqov", "LET?",
          "tedabrun(kol_ha_holkhim, el_esav)")

# -------------------------- Gen.32.21 · THE_ATONEMENT_VERB -----------------
# וַאֲמַרְתֶּם גַּם הִנֵּה עַבְדְּךָ יַעֲקֹב אַחֲרֵינוּ כִּי־אָמַר
# אֲכַפְּרָה פָנָיו בַּמִּנְחָה הַהֹלֶכֶת לְפָנָי וְאַחֲרֵי־כֵן אֶרְאֶה
# פָנָיו אוּלַי יִשָּׂא פָנָי
# "[EN-AID] And you shall say: Also, behold, your servant Jacob is behind
# us. For he said: Let me cover his face with the gift that walks before my
# face; and afterwards I will see his face — perhaps he will lift my face."
m.step("Gen.32.21")
# ‹אֲכַפְּרָה פָנָיו בַּמִּנְחָה הַהֹלֶכֶת לְפָנָי› (“atone face-him/its in-
# grain-offering the-walk/go to-face-me/my”) — fact holds: atone-fanav-
# come/bring-grain-offering(machshevet-Jacob)
m.fact("akhapra_fanav_ba_mincha(machshevet_yaaqov)")

# -------------------------- Gen.32.22 · THE_WRONG_SUBJECT_PASSES -----------
# וַתַּעֲבֹר הַמִּנְחָה עַל־פָּנָיו וְהוּא לָן בַּלַּיְלָה־הַהוּא
# בַּמַּחֲנֶה
# "[EN-AID] And the gift passed over before his face; and he lodged that
# night in the camp."
m.step("Gen.32.22")
# ‹וַתַּעֲבֹר הַמִּנְחָה עַל־פָּנָיו› (“and-pass-over the-grain-offering
# over face-him/its”) — fact holds: and-pass-over-the-grain-offering-over-
# panav(that-stop-come/bring-camp)
m.fact("va_taavor_ha_mincha_al_panav(hu_lan_ba_machane)")

# -------------------------- Gen.32.23 · THE_NIGHT_CROSSING -----------------
# וַיָּקָם בַּלַּיְלָה הוּא וַיִּקַּח אֶת־שְׁתֵּי נָשָׁיו וְאֶת־שְׁתֵּי
# שִׁפְחֹתָיו וְאֶת־אַחַד עָשָׂר יְלָדָיו וַיַּעֲבֹר אֵת מַעֲבַר יַבֹּק
# "[EN-AID] And he rose that night and took his two wives and his two maids
# and his eleven children, and crossed the ford of the Jabbok."
m.step("Gen.32.23")
# ‹וַיַּעֲבֹר אֵת מַעֲבַר יַבֹּק› (“and-pass-over obj-marker crossing-place
# Jabbok”) — fact holds: and-pass-over-obj-marker-crossing-place-
# Jabbok(night, one--teen-yeladav)
m.fact("va_yaavor_et_maavar_yaboq(ba_layla, achad_asar_yeladav)")

# -------------------------- Gen.32.24 · THE_FERRYING -----------------------
# וַיִּקָּחֵם וַיַּעֲבִרֵם אֶת־הַנָּחַל וַיַּעֲבֵר אֶת־אֲשֶׁר־לוֹ
# "[EN-AID] And he took them and crossed them over the stream, and crossed
# over what was his."
m.step("Gen.32.24")
# ‹וַיִּקָּחֵם וַיַּעֲבִרֵם אֶת־הַנָּחַל› (“and-take-them/their and-pass-
# over-them/their obj-marker the-river”) — fact holds: and-yaavirem-obj-
# marker-the-river(all-which-not)
m.fact("va_yaavirem_et_ha_nachal(kol_asher_lo)")

# -------------------------- Gen.32.25 · THE_ALONE_AND_THE_WRESTLE ----------
# וַיִּוָּתֵר יַעֲקֹב לְבַדּוֹ וַיֵּאָבֵק אִישׁ עִמּוֹ עַד עֲלוֹת הַשָּׁחַר
# "[EN-AID] And Jacob was left alone; and a man wrestled with him until the
# rising of the dawn."
m.step("Gen.32.25")
# ‹וַיֵּאָבֵק אִישׁ עִמּוֹ עַד עֲלוֹת הַשָּׁחַר› (“and-bedust man with-
# him/its until go-up the-dawn”) — fact holds: and-bedust-man-imo(Jacob-
# alone, until-go-up-the-dawn)
m.fact("va_yeaveq_ish_imo(yaaqov_levado, ad_alot_ha_shachar)")
# witness-tier presupposed read: ignorance_stated_then_decided_by_a_verb on
# who_prevailed — read, not installed
m.witness_read("who_prevailed", "ignorance_stated_then_decided_by_a_verb",
                cites=["Bereshit Rabbah 77:3"])

# -------------------------- Gen.32.26 · THE_TOUCH --------------------------
# וַיַּרְא כִּי לֹא יָכֹל לוֹ וַיִּגַּע בְּכַף־יְרֵכוֹ וַתֵּקַע כַּף־יֶרֶךְ
# יַעֲקֹב בְּהֵאָבְקוֹ עִמּוֹ
# "[EN-AID] And he saw that he could not prevail against him, and he touched
# the socket of his thigh; and the socket of Jacob's thigh was wrenched as
# he wrestled with him."
m.step("Gen.32.26")
# ‹וַתֵּקַע כַּף־יֶרֶךְ יַעֲקֹב בְּהֵאָבְקוֹ עִמּוֹ› (“and-sever-oneself
# palm-of-hand thigh Jacob in-bedust-him/its with-him/its”) — fact holds:
# and-touch-in-palm-of-hand-yerekho(and-sever-oneself, in-heavqo)
m.fact("va_yiga_be_khaf_yerekho(va_teqa, be_heavqo)")

# -------------------------- Gen.32.27 · THE_WRESTLERS_SEND_ME --------------
# וַיֹּאמֶר שַׁלְּחֵנִי כִּי עָלָה הַשָּׁחַר וַיֹּאמֶר לֹא אֲשַׁלֵּחֲךָ כִּי
# אִם־בֵּרַכְתָּנִי
# "[EN-AID] And he said: Send me away, for the dawn has risen. And he said:
# I will not send you away unless you have blessed me."
m.step("Gen.32.27")
# ‹שַׁלְּחֵנִי כִּי עָלָה הַשָּׁחַר› (“send-me/my that go-up the-dawn”) —
# the-man speaks a demand — LET: shalcheni(Jacob)
m.declare("ha_ish", "LET",
          "shalcheni(yaaqov)")
# witness-tier presupposed read:
# precedence_table_and_a_penalty_in_the_angels_mouth on release_me — read,
# not installed
m.witness_read("release_me", "precedence_table_and_a_penalty_in_the_angels_mouth",
                cites=["Bereshit Rabbah 78:1", "Bereshit Rabbah 78:2"])

# -------------------------- Gen.32.28 · THE_NAME_SURRENDERED ---------------
# וַיֹּאמֶר אֵלָיו מַה־שְּׁמֶךָ וַיֹּאמֶר יַעֲקֹב
# "[EN-AID] And he said to him: What is your name? And he said: Jacob."
m.step("Gen.32.28")
# ‹מַה־שְּׁמֶךָ וַיֹּאמֶר יַעֲקֹב› (“what name-you/your and-say Jacob”) —
# fact holds: what-shemekha-and-say-Jacob(the-man-shoel)
m.fact("ma_shemekha_va_yomer_yaaqov(ha_ish_shoel)")

# -------------------------- Gen.32.29 · THE_DECREE_THAT_WRITES_NOTHING -----
# וַיֹּאמֶר לֹא יַעֲקֹב יֵאָמֵר עוֹד שִׁמְךָ כִּי אִם־יִשְׂרָאֵל
# כִּי־שָׂרִיתָ עִם־אֱלֹהִים וְעִם־אֲנָשִׁים וַתּוּכָל
# "[EN-AID] And he said: No more Jacob shall your name be said, but Israel;
# for you have striven with God and with men, and have prevailed."
m.step("Gen.32.29")
# ‹לֹא יַעֲקֹב יֵאָמֵר עוֹד שִׁמְךָ כִּי אִם־יִשְׂרָאֵל› (“not Jacob say
# still/again name-you/your very-widely-used-as-a-relati as-demonstrative
# Israel”) — fact holds: not-Jacob-say-still/again-that-with-Israel(decree-
# fact)
m.fact("lo_yaaqov_yeamer_od_ki_im_yisrael(decree_fact)")
# witness-tier presupposed read: etymology_refused_by_the_translation on
# the_new_name — read, not installed
m.witness_read("the_new_name", "etymology_refused_by_the_translation",
                cites=["Onkelos Genesis 32:29"])

# -------------------------- Gen.32.30 · THE_NAME_REFUSED -------------------
# וַיִּשְׁאַל יַעֲקֹב וַיֹּאמֶר הַגִּידָה־נָּא שְׁמֶךָ וַיֹּאמֶר לָמָּה זֶּה
# תִּשְׁאַל לִשְׁמִי וַיְבָרֶךְ אֹתוֹ שָׁם
# "[EN-AID] And Jacob asked and said: Tell, please, your name. And he said:
# Why is it that you ask my name? And he blessed him there."
m.step("Gen.32.30")
# ‹הַגִּידָה־נָּא שְׁמֶךָ› (“tell-ward please name-you/your”) — Jacob speaks
# a demand — LET: hagida(the-man, obj-marker-shimkha)
m.declare("yaaqov", "LET",
          "hagida(ha_ish, et_shimkha)")
# witness-tier presupposed read: a_class_with_no_fixed_names on
# why_ask_my_name — read, not installed
m.witness_read("why_ask_my_name", "a_class_with_no_fixed_names",
                cites=["Bereshit Rabbah 78:4"])

# -------------------------- Gen.32.31 · THE_FACE_AND_THE_WRONG_RESCUE ------
# וַיִּקְרָא יַעֲקֹב שֵׁם הַמָּקוֹם פְּנִיאֵל כִּי־רָאִיתִי אֱלֹהִים פָּנִים
# אֶל־פָּנִים וַתִּנָּצֵל נַפְשִׁי
# "[EN-AID] And Jacob called the name of the place Peniel: for I have seen
# God face to face, and my soul was delivered."
m.step("Gen.32.31")
# ‹וַיִּקְרָא יַעֲקֹב שֵׁם הַמָּקוֹם פְּנִיאֵל› (“and-call Jacob name the-
# place Peniel”) — the world gains: place-Peniel
m.install("maqom_peniel")
# ‹פְּנִיאֵל› (“Peniel”) — named: place-Peniel := Peniel
m.name("maqom_peniel", "peniel")

# -------------------------- Gen.32.32 · THE_SUNRISE_AND_THE_LIMP -----------
# וַיִּזְרַח־לוֹ הַשֶּׁמֶשׁ כַּאֲשֶׁר עָבַר אֶת־פְּנוּאֵל וְהוּא צֹלֵעַ
# עַל־יְרֵכוֹ
# "[EN-AID] And the sun rose upon him as he passed Penuel, and he was
# limping on his thigh."
m.step("Gen.32.32")
# ‹וַיִּזְרַח־לוֹ הַשֶּׁמֶשׁ› (“and-irradiate to-him/its the-sun”) — fact
# holds: and-irradiate-the-sun-and-that-limp(over-obj-marker-Peniel)
m.fact("va_yizrach_ha_shemesh_ve_hu_tzolea(over_et_penuel)")
# witness-tier presupposed read: borrowed_hours_repaid_with_interest on
# the_sun_rose_for_him — read, not installed
m.witness_read("the_sun_rose_for_him", "borrowed_hours_repaid_with_interest",
                cites=["Bereshit Rabbah 78:5", "Bereshit Rabbah 68:10"])

# -------------------------- Gen.32.33 · THE_FIRST_NARRATOR_LAW -------------
# עַל־כֵּן לֹא־יֹאכְלוּ בְנֵי־יִשְׂרָאֵל אֶת־גִּיד הַנָּשֶׁה אֲשֶׁר עַל־כַּף
# הַיָּרֵךְ עַד הַיּוֹם הַזֶּה כִּי נָגַע בְּכַף־יֶרֶךְ יַעֲקֹב בְּגִיד
# הַנָּשֶׁה
# "[EN-AID] Therefore the children of Israel eat not the sinew of the thigh-
# vein which is upon the socket of the thigh, to this day; for he touched
# the socket of Jacob's thigh in the sinew of the thigh-vein."
m.step("Gen.32.33")
# ‹עַל־כֵּן לֹא־יֹאכְלוּ בְנֵי־יִשְׂרָאֵל אֶת־גִּיד הַנָּשֶׁה› (“over so not
# eat son Israel obj-marker thong the-rheumatic”) — pattern recorded: not-
# eat-bene-Israel-obj-marker-thong-the-rheumatic
m.pattern("lo_yokhlu_bene_yisrael_et_gid_ha_nashe")
# witness-tier presupposed read:
# first_food_prohibition_with_an_admitted_self_stringency on the_sinew —
# read, not installed
m.witness_read("the_sinew", "first_food_prohibition_with_an_admitted_self_stringency",
                cites=["Bereshit Rabbah 78:6"])
# witness-tier presupposed read: ratification_by_the_losing_signatory on
# what_is_yours_shall_be_yours — read, not installed
m.witness_read("what_is_yours_shall_be_yours", "ratification_by_the_losing_signatory",
                cites=["Bereshit Rabbah 78:11"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'maqom_machanayim', 'maqom_peniel'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'maqom_machanayim': 'machanayim', 'maqom_peniel': 'peniel'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['tomrun(ha_malakhim, la_doni_le_esav)', 'hatzileni(YHWH, mi_yad_esav)', 'ivru(avadav, le_fanai)', 'tasimu(revach, ben_eder_u_ven_eder)', 'tedabrun(kol_ha_holkhim, el_esav)', 'shalcheni(yaaqov)', 'hagida(ha_ish, et_shimkha)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yenasheq_va_yevarekh_va_yashav(lavan, li_meqomo)', 'va_yifgu_vo_malakhe_Elohim(yaaqov, ba_derekh)', 'va_yishlach_malakhim_el_esav(yaaqov, artza_seir)', 'va_yehi_li_shor_va_chamor(divre_ha_shelichut)', 'banu_el_achikha_ve_arba_meot_ish(report)', 'va_yira_va_yachatz_li_shene_machanot(yaaqov)', 'im_yavo_ve_hikahu_ve_haya_li_feleta(tokhnit)', 'retell_shuv_le_artzekha_ve_etiva(tefila, delta_x2)', 'qatonti_mi_kol_ha_chasadim(tefila)', 'amarta_hetev_etiv_ke_chol_ha_yam(tefila, delta_x2)', 'va_yiqach_mincha_le_esav(yaaqov, min_ha_ba_ve_yado)', 'izim_teyashim_rechelim_elim(minchat_ha_tzon)', 'gemalim_parot_parim_atonot_eyarim(minchat_ha_beemot)', 'ki_yifgashkha_esav_u_sheelkha(tzav_rishon)', 'mincha_hi_shelucha_ve_hine_hu_acharenu(maane)', 'akhapra_fanav_ba_mincha(machshevet_yaaqov)', 'va_taavor_ha_mincha_al_panav(hu_lan_ba_machane)', 'va_yaavor_et_maavar_yaboq(ba_layla, achad_asar_yeladav)', 'va_yaavirem_et_ha_nachal(kol_asher_lo)', 'va_yeaveq_ish_imo(yaaqov_levado, ad_alot_ha_shachar)', 'va_yiga_be_khaf_yerekho(va_teqa, be_heavqo)', 'ma_shemekha_va_yomer_yaaqov(ha_ish_shoel)', 'lo_yaaqov_yeamer_od_ki_im_yisrael(decree_fact)', 'va_yizrach_ha_shemesh_ve_hu_tzolea(over_et_penuel)', 'pattern: lo_yokhlu_bene_yisrael_et_gid_ha_nashe'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('my_lord_eight_times', 'priced_in_dynasties_and_paid_at_gen_59'), ('the_embassy', 'criticized_by_the_chain_against_its_own_subject'), ('divided_the_camp', 'risk_distribution_maxim_minted_here'), ('God_of_my_fathers_and_not_of_esau', 'descent_does_not_secure_the_name'), ('i_am_small', 'merit_as_a_finite_balance_drawn_down'), ('the_plea', 'argued_from_a_statute_not_yet_given'), ('who_prevailed', 'ignorance_stated_then_decided_by_a_verb'), ('release_me', 'precedence_table_and_a_penalty_in_the_angels_mouth'), ('the_new_name', 'etymology_refused_by_the_translation'), ('why_ask_my_name', 'a_class_with_no_fixed_names'), ('the_sun_rose_for_him', 'borrowed_hours_repaid_with_interest'), ('the_sinew', 'first_food_prohibition_with_an_admitted_self_stringency'), ('what_is_yours_shall_be_yours', 'ratification_by_the_losing_signatory')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 75:11']
    assert all('priced_in_dynasties_and_paid_at_gen_59' not in f for f in m.WORLD["facts"])
    assert 'my_lord_eight_times' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 75:2', 'Bereshit Rabbah 75:3']
    assert all('criticized_by_the_chain_against_its_own_subject' not in f for f in m.WORLD["facts"])
    assert 'the_embassy' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 76:3']
    assert all('risk_distribution_maxim_minted_here' not in f for f in m.WORLD["facts"])
    assert 'divided_the_camp' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 76:4']
    assert all('descent_does_not_secure_the_name' not in f for f in m.WORLD["facts"])
    assert 'God_of_my_fathers_and_not_of_esau' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 76:5', 'Onkelos Genesis 32:11']
    assert all('merit_as_a_finite_balance_drawn_down' not in f for f in m.WORLD["facts"])
    assert 'i_am_small' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 75:13']
    assert all('argued_from_a_statute_not_yet_given' not in f for f in m.WORLD["facts"])
    assert 'the_plea' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 77:3']
    assert all('ignorance_stated_then_decided_by_a_verb' not in f for f in m.WORLD["facts"])
    assert 'who_prevailed' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 78:1', 'Bereshit Rabbah 78:2']
    assert all('precedence_table_and_a_penalty_in_the_angels_mouth' not in f for f in m.WORLD["facts"])
    assert 'release_me' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 32:29']
    assert all('etymology_refused_by_the_translation' not in f for f in m.WORLD["facts"])
    assert 'the_new_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 78:4']
    assert all('a_class_with_no_fixed_names' not in f for f in m.WORLD["facts"])
    assert 'why_ask_my_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 78:5', 'Bereshit Rabbah 68:10']
    assert all('borrowed_hours_repaid_with_interest' not in f for f in m.WORLD["facts"])
    assert 'the_sun_rose_for_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 78:6']
    assert all('first_food_prohibition_with_an_admitted_self_stringency' not in f for f in m.WORLD["facts"])
    assert 'the_sinew' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 78:11']
    assert all('ratification_by_the_losing_signatory' not in f for f in m.WORLD["facts"])
    assert 'what_is_yours_shall_be_yours' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
