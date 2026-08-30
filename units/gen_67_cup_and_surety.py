#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_67_cup_and_surety — 44:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_67_cup_and_surety.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The cup and the surety: Judah's speech (44:1-34)"""
from machine import Machine

m = Machine("gen_67_cup_and_surety")

# -------------------------- Gen.44.1 · FILL_AND_PLANT ----------------------
# וַיְצַו אֶת־אֲשֶׁר עַל־בֵּיתוֹ לֵאמֹר מַלֵּא אֶת־אַמְתְּחֹת הָאֲנָשִׁים
# אֹכֶל כַּאֲשֶׁר יוּכְלוּן שְׂאֵת וְשִׂים כֶּסֶף־אִישׁ בְּפִי אַמְתַּחְתּוֹ
# "[EN-AID] And he commanded the one over his house, saying: Fill the men's
# bags with food, as much as they can carry, and put each man's silver in
# the mouth of his bag."
m.step("Gen.44.1")
# ‹מַלֵּא אֶת־אַמְתְּחֹת הָאֲנָשִׁים› (“fill obj-marker something-expansive
# the-man”) — Joseph speaks a demand — LET: fill-amtechot-and-put/set-silver
m.declare("yosef", "LET",
          "male_amtechot_ve_sim_kesef")

# -------------------------- Gen.44.2 · MY_CUP_THE_SILVER_CUP ---------------
# וְאֶת־גְּבִיעִי גְּבִיעַ הַכֶּסֶף תָּשִׂים בְּפִי אַמְתַּחַת הַקָּטֹן
# וְאֵת כֶּסֶף שִׁבְרוֹ וַיַּעַשׂ כִּדְבַר יוֹסֵף אֲשֶׁר דִּבֵּר
# "[EN-AID] And my cup — the silver cup — you shall put in the mouth of the
# youngest one's bag, and the silver of his grain. And he did according to
# the word of Joseph which he spoke."
m.step("Gen.44.2")
# ‹וַיַּעַשׂ כִּדְבַר יוֹסֵף אֲשֶׁר דִּבֵּר› (“and-make like-word/thing
# Joseph which speak”) — demand settled (popped from the queue): fill-
# amtechot-and-put/set-silver
m.result("male_amtechot_ve_sim_kesef", tmark="t1")

# -------------------------- Gen.44.3 · THE_MORNING_LIGHT -------------------
# הַבֹּקֶר אוֹר וְהָאֲנָשִׁים שֻׁלְּחוּ הֵמָּה וַחֲמֹרֵיהֶם
# "[EN-AID] The morning was light, and the men were sent away — they and
# their donkeys."
m.step("Gen.44.3")
# ‹הַבֹּקֶר אוֹר וְהָאֲנָשִׁים שֻׁלְּחוּ› (“the-morning give-light and-the-
# man send”) — fact holds: the-morning-give-light-and-the-man-send
m.fact("ha_boqer_or_ve_ha_anashim_shulchu")

# -------------------------- Gen.44.4 · ARISE_PURSUE_OVERTAKE ---------------
# הֵם יָצְאוּ אֶת־הָעִיר לֹא הִרְחִיקוּ וְיוֹסֵף אָמַר לַאֲשֶׁר עַל־בֵּיתוֹ
# קוּם רְדֹף אַחֲרֵי הָאֲנָשִׁים וְהִשַּׂגְתָּם וְאָמַרְתָּ אֲלֵהֶם לָמָּה
# שִׁלַּמְתֶּם רָעָה תַּחַת טוֹבָה
# "[EN-AID] They had gone out of the city — they were not far — and Joseph
# said to the one over his house: Arise, pursue after the men; and overtake
# them, and say to them: Why have you repaid evil for good?"
m.step("Gen.44.4")
# ‹קוּם רְדֹף אַחֲרֵי הָאֲנָשִׁים וְהִשַּׂגְתָּם› (“arise run-after-gone-by)
# after the-man and-reach-them/their”) — Joseph speaks a demand — LET:
# arise-run-after-gone-by)-and-hisagtam
m.declare("yosef", "LET",
          "qum_redof_ve_hisagtam")

# -------------------------- Gen.44.5 · THE_DIVINING_CUP --------------------
# הֲלוֹא זֶה אֲשֶׁר יִשְׁתֶּה אֲדֹנִי בּוֹ וְהוּא נַחֵשׁ יְנַחֵשׁ בּוֹ
# הֲרֵעֹתֶם אֲשֶׁר עֲשִׂיתֶם
# "[EN-AID] Is not this that from which my lord drinks, and by which he
# surely divines? You have done evil in what you have done."
m.step("Gen.44.5")
# ‹וְהוּא נַחֵשׁ יְנַחֵשׁ בּוֹ› (“and-he/it hiss hiss in-him/its”) — fact
# holds: hiss-hiss-in-it
m.fact("nachesh_yenachesh_bo")
# witness-grounded state (its own tier):
# converted_to_investigation_at_both_seats on he_surely_divines
m.witness_state("he_surely_divines", "converted_to_investigation_at_both_seats",
                cites=["Onkelos Genesis 44:5", "Onkelos Genesis 44:15"])

# -------------------------- Gen.44.6 · HE_OVERTOOK_THEM --------------------
# וַיַּשִּׂגֵם וַיְדַבֵּר אֲלֵהֶם אֶת־הַדְּבָרִים הָאֵלֶּה
# "[EN-AID] And he overtook them, and spoke to them these words."
m.step("Gen.44.6")
# ‹וַיַּשִּׂגֵם וַיְדַבֵּר אֲלֵהֶם› (“and-reach-them/their and-speak to-
# them/their”) — demand settled (popped from the queue): arise-run-after-
# gone-by)-and-hisagtam
m.result("qum_redof_ve_hisagtam", tmark="t2")

# -------------------------- Gen.44.7 · FAR_BE_IT_FROM_YOUR_SERVANTS --------
# וַיֹּאמְרוּ אֵלָיו לָמָּה יְדַבֵּר אֲדֹנִי כַּדְּבָרִים הָאֵלֶּה חָלִילָה
# לַעֲבָדֶיךָ מֵעֲשׂוֹת כַּדָּבָר הַזֶּה
# "[EN-AID] And they said to him: Why does my lord speak according to these
# words? Far be it from your servants to do according to this thing."
m.step("Gen.44.7")
# ‹חָלִילָה לַעֲבָדֶיךָ מֵעֲשׂוֹת כַּדָּבָר הַזֶּה› (“literal-fora-profaned-
# thing-ward to-servant-you/your from-make like-word/thing the-this”) — fact
# holds: chalila-to-avadekha
m.fact("chalila_la_avadekha")

# -------------------------- Gen.44.8 · THE_SILVER_WE_RETURNED --------------
# הֵן כֶּסֶף אֲשֶׁר מָצָאנוּ בְּפִי אַמְתְּחֹתֵינוּ הֱשִׁיבֹנוּ אֵלֶיךָ
# מֵאֶרֶץ כְּנָעַן וְאֵיךְ נִגְנֹב מִבֵּית אֲדֹנֶיךָ כֶּסֶף אוֹ זָהָב
# "[EN-AID] Behold, the silver which we found in the mouth of our bags we
# brought back to you from the land of Canaan; and how should we steal from
# your lord's house silver or gold?"
m.step("Gen.44.8")
# ‹הֵן כֶּסֶף אֲשֶׁר מָצָאנוּ› (“lo! silver which find”) — fact holds:
# lo!-silver-return-and-how?-steal
m.fact("hen_kesef_heshivonu_ve_ekh_nignov")
# witness-grounded state (its own tier):
# the_type_specimen_of_the_inference_rule on how_then_should_we_steal
m.witness_state("how_then_should_we_steal", "the_type_specimen_of_the_inference_rule",
                cites=["Bereshit Rabbah 92:7", "Onkelos Genesis 44:8"])

# -------------------------- Gen.44.9 · THE_RASH_SENTENCE -------------------
# אֲשֶׁר יִמָּצֵא אִתּוֹ מֵעֲבָדֶיךָ וָמֵת וְגַם־אֲנַחְנוּ נִהְיֶה לַאדֹנִי
# לַעֲבָדִים
# "[EN-AID] With whomever of your servants it be found — let him die; and we
# also will be my lord's slaves."
m.step("Gen.44.9")
# ‹אֲשֶׁר יִמָּצֵא אִתּוֹ מֵעֲבָדֶיךָ וָמֵת› (“which find with-him/its from-
# servant-you/your and-die”) — fact holds: which-find-with-him-and-die
m.fact("asher_yimatze_ito_va_met")

# -------------------------- Gen.44.10 · THE_STEWARDS_SOFTENING -------------
# וַיֹּאמֶר גַּם־עַתָּה כְדִבְרֵיכֶם כֶּן־הוּא אֲשֶׁר יִמָּצֵא אִתּוֹ
# יִהְיֶה־לִּי עָבֶד וְאַתֶּם תִּהְיוּ נְקִיִּם
# "[EN-AID] And he said: Now also, according to your words, so be it: with
# whom it is found shall be my slave, and you shall be clean."
m.step("Gen.44.10")
# ‹אֲשֶׁר יִמָּצֵא אִתּוֹ יִהְיֶה־לִּי עָבֶד וְאַתֶּם תִּהְיוּ נְקִיִּם›
# (“which find with-him/its be to-me/my servant and-you be innocent”) — fact
# holds: be-to-me-servant-and-you-be-innocent
m.fact("yihye_li_aved_ve_atem_tihyu_neqiyim")

# -------------------------- Gen.44.11 · BAGS_LOWERED -----------------------
# וַיְמַהֲרוּ וַיּוֹרִדוּ אִישׁ אֶת־אַמְתַּחְתּוֹ אָרְצָה וַיִּפְתְּחוּ
# אִישׁ אַמְתַּחְתּוֹ
# "[EN-AID] And they hurried, and each man lowered his bag to the earth, and
# each man opened his bag."
m.step("Gen.44.11")
# ‹וַיְמַהֲרוּ וַיּוֹרִדוּ אִישׁ אֶת־אַמְתַּחְתּוֹ› (“and-hasten and-go-down
# man obj-marker something-expansive-him/its”) — fact holds: and-go-down-
# man-obj-marker-amtachto
m.fact("va_yoridu_ish_et_amtachto")

# -------------------------- Gen.44.12 · FOUND_IN_BENJAMINS_BAG -------------
# וַיְחַפֵּשׂ בַּגָּדוֹל הֵחֵל וּבַקָּטֹן כִּלָּה וַיִּמָּצֵא הַגָּבִיעַ
# בְּאַמְתַּחַת בִּנְיָמִן
# "[EN-AID] And he searched — at the eldest he began, and at the youngest he
# ended; and the cup was found in Benjamin's bag."
m.step("Gen.44.12")
# ‹וַיִּמָּצֵא הַגָּבִיעַ בְּאַמְתַּחַת בִּנְיָמִן› (“and-find the-goblet
# in-something-expansive Benjamin”) — fact holds: and-find-the-goblet-in-
# something-expansive-Benjamin
m.fact("va_yimatze_ha_gavia_be_amtachat_binyamin")
# witness-tier presupposed read: an_old_theft_thrown_back on
# the_goblet_found_in_benjamins_sack — read, not installed
m.witness_read("the_goblet_found_in_benjamins_sack", "an_old_theft_thrown_back",
                cites=["Bereshit Rabbah 92:8"])

# -------------------------- Gen.44.13 · THE_GARMENTS_TORN ------------------
# וַיִּקְרְעוּ שִׂמְלֹתָם וַיַּעֲמֹס אִישׁ עַל־חֲמֹרוֹ וַיָּשֻׁבוּ הָעִירָה
# "[EN-AID] And they tore their garments; and each man loaded his donkey,
# and they returned to the city."
m.step("Gen.44.13")
# ‹וַיִּקְרְעוּ שִׂמְלֹתָם› (“and-rend dress-them/their”) — event: qara —
# agent the-achim; theme simlotam
m.event("qara", agent="ha_achim", themes=["simlotam"])
# witness-tier presupposed read: the_first_installment_of_the_rending_table
# on they_rent_their_garments — read, not installed
m.witness_read("they_rent_their_garments", "the_first_installment_of_the_rending_table",
                cites=["Bereshit Rabbah 84:20"])

# -------------------------- Gen.44.14 · THEY_FALL_BEFORE_HIM ---------------
# וַיָּבֹא יְהוּדָה וְאֶחָיו בֵּיתָה יוֹסֵף וְהוּא עוֹדֶנּוּ שָׁם
# וַיִּפְּלוּ לְפָנָיו אָרְצָה
# "[EN-AID] And Judah and his brothers came to Joseph's house — and he was
# yet there — and they fell before him to the earth."
m.step("Gen.44.14")
# ‹וַיִּפְּלוּ לְפָנָיו אָרְצָה› (“and-fall to-face-him/its earth-ward”) —
# event: naflu — agent Judah-and-echav
m.event("naflu", agent="yehuda_ve_echav")
# witness-tier presupposed read: the_second_of_three_crowning_speeches on
# judah_and_his_brothers_came — read, not installed
m.witness_read("judah_and_his_brothers_came", "the_second_of_three_crowning_speeches",
                cites=["Bereshit Rabbah 84:17"])

# -------------------------- Gen.44.15 · A_MAN_LIKE_ME ----------------------
# וַיֹּאמֶר לָהֶם יוֹסֵף מָה־הַמַּעֲשֶׂה הַזֶּה אֲשֶׁר עֲשִׂיתֶם הֲלוֹא
# יְדַעְתֶּם כִּי־נַחֵשׁ יְנַחֵשׁ אִישׁ אֲשֶׁר כָּמֹנִי
# "[EN-AID] And Joseph said to them: What is this deed you have done? Did
# you not know that a man like me surely divines?"
m.step("Gen.44.15")
# ‹כִּי־נַחֵשׁ יְנַחֵשׁ אִישׁ אֲשֶׁר כָּמֹנִי› (“that hiss hiss man which
# form-of-the-prefix-'k-'-me/my”) — fact holds: hiss-hiss-man-which-kamoni
m.fact("nachesh_yenachesh_ish_asher_kamoni")

# -------------------------- Gen.44.16 · GOD_HAS_FOUND_THE_GUILT ------------
# וַיֹּאמֶר יְהוּדָה מַה־נֹּאמַר לַאדֹנִי מַה־נְּדַבֵּר וּמַה־נִּצְטַדָּק
# הָאֱלֹהִים מָצָא אֶת־עֲוֺן עֲבָדֶיךָ הִנֶּנּוּ עֲבָדִים לַאדֹנִי
# גַּם־אֲנַחְנוּ גַּם אֲשֶׁר־נִמְצָא הַגָּבִיעַ בְּיָדוֹ
# "[EN-AID] And Judah said: What shall we say to my lord? What shall we
# speak, and how shall we clear ourselves? God has found the guilt of your
# servants: behold, we are my lord's slaves — both we and he in whose hand
# the cup was found."
m.step("Gen.44.16")
# ‹הָאֱלֹהִים מָצָא אֶת־עֲוֺן עֲבָדֶיךָ› (“the-God find obj-marker
# perversity servant-you/your”) — fact holds: the-God-find-obj-marker-
# perversity-avadekha
m.fact("ha_Elohim_matza_et_avon_avadekha")
# witness-tier presupposed read:
# the_chain_personalizes_where_the_buffer_depersonalizes on
# god_has_found_the_iniquity — read, not installed
m.witness_read("god_has_found_the_iniquity", "the_chain_personalizes_where_the_buffer_depersonalizes",
                cites=["Onkelos Genesis 44:16", "Bereshit Rabbah 92:9"])

# -------------------------- Gen.44.17 · GO_UP_IN_PEACE ---------------------
# וַיֹּאמֶר חָלִילָה לִּי מֵעֲשׂוֹת זֹאת הָאִישׁ אֲשֶׁר נִמְצָא הַגָּבִיעַ
# בְּיָדוֹ הוּא יִהְיֶה־לִּי עָבֶד וְאַתֶּם עֲלוּ לְשָׁלוֹם אֶל־אֲבִיכֶם
# "[EN-AID] And he said: Far be it from me to do this; the man in whose hand
# the cup was found — he shall be my slave; and you — go up in peace to your
# father."
m.step("Gen.44.17")
# ‹וְאַתֶּם עֲלוּ לְשָׁלוֹם אֶל־אֲבִיכֶם› (“and-you go-up to-safe to father-
# you/your(pl)”) — Joseph speaks a demand — LET: go-up-to-safe-to-avikhem
m.declare("yosef", "LET",
          "alu_le_shalom_el_avikhem")

# -------------------------- Gen.44.18 · JUDAH_DRAWS_NEAR -------------------
# וַיִּגַּשׁ אֵלָיו יְהוּדָה וַיֹּאמֶר בִּי אֲדֹנִי יְדַבֶּר־נָא עַבְדְּךָ
# דָבָר בְּאָזְנֵי אֲדֹנִי וְאַל־יִחַר אַפְּךָ בְּעַבְדֶּךָ כִּי כָמוֹךָ
# כְּפַרְעֹה
# "[EN-AID] And Judah drew near to him and said: Please, my lord, let your
# servant speak a word in my lord's ears, and let not your anger burn
# against your servant — for you are as Pharaoh."
m.step("Gen.44.18")
# ‹וַיִּגַּשׁ אֵלָיו יְהוּדָה› (“and-be to-him/its Judah”) — event: nigash —
# agent Judah
m.event("nigash", agent="yehuda")
# witness-tier presupposed read: persuasion_as_incremental_extraction on
# judah_approached_him — read, not installed
m.witness_read("judah_approached_him", "persuasion_as_incremental_extraction",
                cites=["Bereshit Rabbah 93:4"])
# witness-tier presupposed read: a_rival_translator_named_inside_the_midrash
# on a_word_spoken_on_its_wheel — read, not installed
m.witness_read("a_word_spoken_on_its_wheel", "a_rival_translator_named_inside_the_midrash",
                cites=["Bereshit Rabbah 93:3"])
# witness-grounded state (its own tier):
# three_estrangements_discharged_at_once on the_whole_speech
m.witness_state("the_whole_speech", "three_estrangements_discharged_at_once",
                cites=["Bereshit Rabbah 93:9"])
# witness-tier presupposed read:
# a_test_of_strength_resolved_by_a_judgment_of_piety on the_confrontation —
# read, not installed
m.witness_read("the_confrontation", "a_test_of_strength_resolved_by_a_judgment_of_piety",
                cites=["Bereshit Rabbah 93:7", "Onkelos Genesis 44:18"])

# -------------------------- Gen.44.19 · MY_LORD_ASKED ----------------------
# אֲדֹנִי שָׁאַל אֶת־עֲבָדָיו לֵאמֹר הֲיֵשׁ־לָכֶם אָב אוֹ־אָח
# "[EN-AID] My lord asked his servants, saying: Have you a father, or a
# brother?"
m.step("Gen.44.19")
# ‹אֲדֹנִי שָׁאַל אֶת־עֲבָדָיו› (“lord-me/my inquire obj-marker servant-
# him/its”) — fact holds: adoni-inquire-obj-marker-avadav
m.fact("adoni_shaal_et_avadav")

# -------------------------- Gen.44.20 · A_CHILD_OF_OLD_AGE -----------------
# וַנֹּאמֶר אֶל־אֲדֹנִי יֶשׁ־לָנוּ אָב זָקֵן וְיֶלֶד זְקֻנִים קָטָן וְאָחִיו
# מֵת וַיִּוָּתֵר הוּא לְבַדּוֹ לְאִמּוֹ וְאָבִיו אֲהֵבוֹ
# "[EN-AID] And we said to my lord: We have an old father, and a child of
# old age, a little one; and his brother is dead, and he alone is left of
# his mother, and his father loves him."
m.step("Gen.44.20")
# ‹וְיֶלֶד זְקֻנִים קָטָן› (“and-child old-age abbreviated”) — fact holds:
# child-old-age-abbreviated-and-his-brother-die
m.fact("yeled_zequnim_qatan_ve_achiv_met")

# -------------------------- Gen.44.21 · BRING_HIM_DOWN_TO_ME ---------------
# וַתֹּאמֶר אֶל־עֲבָדֶיךָ הוֹרִדֻהוּ אֵלָי וְאָשִׂימָה עֵינִי עָלָיו
# "[EN-AID] And you said to your servants: Bring him down to me, that I may
# set my eye upon him."
m.step("Gen.44.21")
# ‹וַתֹּאמֶר אֶל־עֲבָדֶיךָ הוֹרִדֻהוּ אֵלָי› (“and-say to servant-you/your
# go-down-him/its to-me/my”) — fact holds: horiduhu-elai-and-put/set-eni-
# alav
m.fact("horiduhu_elai_ve_asima_eni_alav")

# -------------------------- Gen.44.22 · HE_CANNOT_LEAVE_HIS_FATHER ---------
# וַנֹּאמֶר אֶל־אֲדֹנִי לֹא־יוּכַל הַנַּעַר לַעֲזֹב אֶת־אָבִיו וְעָזַב
# אֶת־אָבִיו וָמֵת
# "[EN-AID] And we said to my lord: The lad cannot leave his father; should
# he leave his father, he would die."
m.step("Gen.44.22")
# ‹לֹא־יוּכַל הַנַּעַר לַעֲזֹב אֶת־אָבִיו› (“not be-able the-boy to-loosen
# obj-marker father-him/its”) — fact holds: not-be-able-the-boy-laazov-obj-
# marker-aviv
m.fact("lo_yukhal_ha_naar_laazov_et_aviv")

# -------------------------- Gen.44.23 · YOU_SHALL_NOT_SEE_MY_FACE ----------
# וַתֹּאמֶר אֶל־עֲבָדֶיךָ אִם־לֹא יֵרֵד אֲחִיכֶם הַקָּטֹן אִתְּכֶם לֹא
# תֹסִפוּן לִרְאוֹת פָּנָי
# "[EN-AID] And you said to your servants: If your youngest brother does not
# come down with you, you shall not again see my face."
m.step("Gen.44.23")
# ‹לֹא תֹסִפוּן לִרְאוֹת פָּנָי› (“not add-ward to-see face-me/my”) — fact
# holds: not-tosifun-lirot-panai
m.fact("lo_tosifun_lirot_panai")

# -------------------------- Gen.44.24 · WE_TOLD_MY_FATHER ------------------
# וַיְהִי כִּי עָלִינוּ אֶל־עַבְדְּךָ אָבִי וַנַּגֶּד־לוֹ אֵת דִּבְרֵי
# אֲדֹנִי
# "[EN-AID] And it was, when we went up to your servant my father, that we
# told him the words of my lord."
m.step("Gen.44.24")
# ‹וַנַּגֶּד־לוֹ אֵת דִּבְרֵי אֲדֹנִי› (“and-tell to-him/its obj-marker
# word/thing lord-me/my”) — fact holds: and-tell-not-obj-marker-word/thing-
# adoni
m.fact("va_naged_lo_et_divre_adoni")

# -------------------------- Gen.44.25 · OUR_FATHER_SAID_RETURN -------------
# וַיֹּאמֶר אָבִינוּ שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל
# "[EN-AID] And our father said: Return, buy us a little food."
m.step("Gen.44.25")
# ‹שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“return deal-in-grain to-us/our
# little food”) — fact holds: return-deal-in-grain-lanu-little-food-requoted
m.fact("shuvu_shivru_lanu_meat_okhel_requoted")

# -------------------------- Gen.44.26 · WE_CANNOT_GO_DOWN ------------------
# וַנֹּאמֶר לֹא נוּכַל לָרֶדֶת אִם־יֵשׁ אָחִינוּ הַקָּטֹן אִתָּנוּ
# וְיָרַדְנוּ כִּי־לֹא נוּכַל לִרְאוֹת פְּנֵי הָאִישׁ וְאָחִינוּ הַקָּטֹן
# אֵינֶנּוּ אִתָּנוּ
# "[EN-AID] And we said: We cannot go down; if our youngest brother is with
# us, we will go down — for we cannot see the man's face and our youngest
# brother not with us."
m.step("Gen.44.26")
# ‹וַנֹּאמֶר לֹא נוּכַל לָרֶדֶת› (“and-say not be-able to-go-down”) — fact
# holds: not-be-able-laredet-if-there-is-not-achinu
m.fact("lo_nukhal_laredet_im_en_achinu")

# -------------------------- Gen.44.27 · TWO_MY_WIFE_BORE_ME ----------------
# וַיֹּאמֶר עַבְדְּךָ אָבִי אֵלֵינוּ אַתֶּם יְדַעְתֶּם כִּי שְׁנַיִם
# יָלְדָה־לִּי אִשְׁתִּי
# "[EN-AID] And your servant my father said to us: You know that my wife
# bore me two."
m.step("Gen.44.27")
# ‹כִּי שְׁנַיִם יָלְדָה־לִּי אִשְׁתִּי› (“that two bear-young to-me/my
# woman-me/my”) — fact holds: two-bear-young-to-me-ishti
m.fact("shenayim_yalda_li_ishti")

# -------------------------- Gen.44.28 · TORN_TORN --------------------------
# וַיֵּצֵא הָאֶחָד מֵאִתִּי וָאֹמַר אַךְ טָרֹף טֹרָף וְלֹא רְאִיתִיו
# עַד־הֵנָּה
# "[EN-AID] And the one went out from me, and I said: Surely torn, torn —
# and I have not seen him until now."
m.step("Gen.44.28")
# ‹אַךְ טָרֹף טֹרָף› (“indeed pluck-off pluck-off”) — fact holds: indeed-
# pluck-off-pluck-off-and-not-reitiv
m.fact("akh_tarof_toraf_ve_lo_reitiv")
# witness-grounded state (its own tier):
# two_seats_in_the_torah_one_rendering on surely_torn_torn
m.witness_state("surely_torn_torn", "two_seats_in_the_torah_one_rendering",
                cites=["Onkelos Genesis 44:28", "Bereshit Rabbah 93:8"])

# -------------------------- Gen.44.29 · GRAY_HAIR_IN_EVIL ------------------
# וּלְקַחְתֶּם גַּם־אֶת־זֶה מֵעִם פָּנַי וְקָרָהוּ אָסוֹן וְהוֹרַדְתֶּם
# אֶת־שֵׂיבָתִי בְּרָעָה שְׁאֹלָה
# "[EN-AID] And should you take this one also from before my face, and harm
# befall him — you will bring down my gray hair in evil to Sheol."
m.step("Gen.44.29")
# ‹וְהוֹרַדְתֶּם אֶת־שֵׂיבָתִי בְּרָעָה שְׁאֹלָה› (“and-go-down obj-marker
# old-age-me/my in-bad Shᵉ'Owl-ward”) — fact holds: and-go-down-obj-marker-
# sevati-in-bad-sheola
m.fact("ve_horadtem_et_sevati_be_raa_sheola")
# witness-tier presupposed read:
# the_third_seat_of_the_word_that_lives_in_one_law on lest_harm_befall_him —
# read, not installed
m.witness_read("lest_harm_befall_him", "the_third_seat_of_the_word_that_lives_in_one_law",
                cites=["Onkelos Genesis 44:29", "Onkelos Genesis 42:4"])

# -------------------------- Gen.44.30 · SOUL_BOUND_TO_SOUL -----------------
# וְעַתָּה כְּבֹאִי אֶל־עַבְדְּךָ אָבִי וְהַנַּעַר אֵינֶנּוּ אִתָּנוּ
# וְנַפְשׁוֹ קְשׁוּרָה בְנַפְשׁוֹ
# "[EN-AID] And now, when I come to your servant my father and the lad is
# not with us — and his soul is bound to his soul —"
m.step("Gen.44.30")
# ‹וְנַפְשׁוֹ קְשׁוּרָה בְנַפְשׁוֹ› (“and-living-being-him/its tie in-
# living-being-him/its”) — fact holds: and-nafsho-tie-and-nafsho
m.fact("ve_nafsho_qeshura_ve_nafsho")
# witness-tier presupposed read:
# rendered_as_love_which_is_the_arguments_premise on
# his_soul_is_bound_up_with_his_soul — read, not installed
m.witness_read("his_soul_is_bound_up_with_his_soul", "rendered_as_love_which_is_the_arguments_premise",
                cites=["Onkelos Genesis 44:30", "Onkelos Genesis 44:32"])

# -------------------------- Gen.44.31 · WHEN_HE_SEES_THE_LAD_IS_NOT --------
# וְהָיָה כִּרְאוֹתוֹ כִּי־אֵין הַנַּעַר וָמֵת וְהוֹרִידוּ עֲבָדֶיךָ
# אֶת־שֵׂיבַת עַבְדְּךָ אָבִינוּ בְּיָגוֹן שְׁאֹלָה
# "[EN-AID] then it will be, when he sees that the lad is not — he will die;
# and your servants will bring down the gray hair of your servant our father
# in sorrow to Sheol."
m.step("Gen.44.31")
# ‹כִּרְאוֹתוֹ כִּי־אֵין הַנַּעַר וָמֵת› (“like-see-him/its that there-is-
# not the-boy and-die”) — fact holds: that-there-is-not-the-boy-and-die
m.fact("ki_en_ha_naar_va_met")

# -------------------------- Gen.44.32 · YOUR_SERVANT_IS_SURETY -------------
# כִּי עַבְדְּךָ עָרַב אֶת־הַנַּעַר מֵעִם אָבִי לֵאמֹר אִם־לֹא אֲבִיאֶנּוּ
# אֵלֶיךָ וְחָטָאתִי לְאָבִי כָּל־הַיָּמִים
# "[EN-AID] For your servant became surety for the lad from my father,
# saying: If I do not bring him to you, I shall have sinned against my
# father all the days."
m.step("Gen.44.32")
# ‹כִּי עַבְדְּךָ עָרַב אֶת־הַנַּעַר› (“that servant-you/your braid obj-
# marker the-boy”) — fact holds: that-avdekha-braid-obj-marker-the-boy
m.fact("ki_avdekha_arav_et_ha_naar")

# -------------------------- Gen.44.33 · LET_ME_STAY_INSTEAD ----------------
# וְעַתָּה יֵשֶׁב־נָא עַבְדְּךָ תַּחַת הַנַּעַר עֶבֶד לַאדֹנִי וְהַנַּעַר
# יַעַל עִם־אֶחָיו
# "[EN-AID] And now — let your servant stay instead of the lad, a slave to
# my lord; and let the lad go up with his brothers."
m.step("Gen.44.33")
# ‹וְעַתָּה יֵשֶׁב־נָא עַבְדְּךָ תַּחַת הַנַּעַר› (“and-now dwell/sit please
# servant-you/your under the-boy”) — Judah speaks a demand — LET: dwell/sit-
# please-avdekha-under-the-boy
m.declare("yehuda", "LET",
          "yeshev_na_avdekha_tachat_ha_naar")

# -------------------------- Gen.44.34 · HOW_SHALL_I_GO_UP ------------------
# כִּי־אֵיךְ אֶעֱלֶה אֶל־אָבִי וְהַנַּעַר אֵינֶנּוּ אִתִּי פֶּן אֶרְאֶה
# בָרָע אֲשֶׁר יִמְצָא אֶת־אָבִי
# "[EN-AID] For how shall I go up to my father and the lad is not with me —
# lest I see the evil that would find my father?"
m.step("Gen.44.34")
# ‹כִּי־אֵיךְ אֶעֱלֶה אֶל־אָבִי וְהַנַּעַר אֵינֶנּוּ אִתִּי› (“that how? go-
# up to father-me/my and-the-boy there-is-not-him/its with-me/my”) — fact
# holds: how?-go-up-to-avi-and-the-boy-enennu
m.fact("ekh_eele_el_avi_ve_ha_naar_enennu")
# witness-grounded state (its own tier): breaking_off_at_an_open_edge on
# the_speech
m.witness_state("the_speech", "breaking_off_at_an_open_edge",
                cites=["Bereshit Rabbah 93:9", "Bereshit Rabbah 93:8"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['alu_le_shalom_el_avikhem', 'yeshev_na_avdekha_tachat_ha_naar']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ha_boqer_or_ve_ha_anashim_shulchu', 'nachesh_yenachesh_bo', 'chalila_la_avadekha', 'hen_kesef_heshivonu_ve_ekh_nignov', 'asher_yimatze_ito_va_met', 'yihye_li_aved_ve_atem_tihyu_neqiyim', 'va_yoridu_ish_et_amtachto', 'va_yimatze_ha_gavia_be_amtachat_binyamin', 'nachesh_yenachesh_ish_asher_kamoni', 'ha_Elohim_matza_et_avon_avadekha', 'adoni_shaal_et_avadav', 'yeled_zequnim_qatan_ve_achiv_met', 'horiduhu_elai_ve_asima_eni_alav', 'lo_yukhal_ha_naar_laazov_et_aviv', 'lo_tosifun_lirot_panai', 'va_naged_lo_et_divre_adoni', 'shuvu_shivru_lanu_meat_okhel_requoted', 'lo_nukhal_laredet_im_en_achinu', 'shenayim_yalda_li_ishti', 'akh_tarof_toraf_ve_lo_reitiv', 've_horadtem_et_sevati_be_raa_sheola', 've_nafsho_qeshura_ve_nafsho', 'ki_en_ha_naar_va_met', 'ki_avdekha_arav_et_ha_naar', 'ekh_eele_el_avi_ve_ha_naar_enennu'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    assert sorted(m.WORLD["witnessed"]) == ['he_surely_divines', 'how_then_should_we_steal', 'surely_torn_torn', 'the_speech', 'the_whole_speech']
    assert m.WORLD["witnessed"]['he_surely_divines']["cites"] == ['Onkelos Genesis 44:5', 'Onkelos Genesis 44:15']
    assert all('converted_to_investigation_at_both_seats' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['how_then_should_we_steal']["cites"] == ['Bereshit Rabbah 92:7', 'Onkelos Genesis 44:8']
    assert all('the_type_specimen_of_the_inference_rule' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['surely_torn_torn']["cites"] == ['Onkelos Genesis 44:28', 'Bereshit Rabbah 93:8']
    assert all('two_seats_in_the_torah_one_rendering' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_speech']["cites"] == ['Bereshit Rabbah 93:9', 'Bereshit Rabbah 93:8']
    assert all('breaking_off_at_an_open_edge' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_whole_speech']["cites"] == ['Bereshit Rabbah 93:9']
    assert all('three_estrangements_discharged_at_once' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_goblet_found_in_benjamins_sack', 'an_old_theft_thrown_back'), ('they_rent_their_garments', 'the_first_installment_of_the_rending_table'), ('judah_and_his_brothers_came', 'the_second_of_three_crowning_speeches'), ('god_has_found_the_iniquity', 'the_chain_personalizes_where_the_buffer_depersonalizes'), ('judah_approached_him', 'persuasion_as_incremental_extraction'), ('a_word_spoken_on_its_wheel', 'a_rival_translator_named_inside_the_midrash'), ('the_confrontation', 'a_test_of_strength_resolved_by_a_judgment_of_piety'), ('lest_harm_befall_him', 'the_third_seat_of_the_word_that_lives_in_one_law'), ('his_soul_is_bound_up_with_his_soul', 'rendered_as_love_which_is_the_arguments_premise')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 92:8']
    assert all('an_old_theft_thrown_back' not in f for f in m.WORLD["facts"])
    assert 'the_goblet_found_in_benjamins_sack' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 84:20']
    assert all('the_first_installment_of_the_rending_table' not in f for f in m.WORLD["facts"])
    assert 'they_rent_their_garments' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 84:17']
    assert all('the_second_of_three_crowning_speeches' not in f for f in m.WORLD["facts"])
    assert 'judah_and_his_brothers_came' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Onkelos Genesis 44:16', 'Bereshit Rabbah 92:9']
    assert all('the_chain_personalizes_where_the_buffer_depersonalizes' not in f for f in m.WORLD["facts"])
    assert 'god_has_found_the_iniquity' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 93:4']
    assert all('persuasion_as_incremental_extraction' not in f for f in m.WORLD["facts"])
    assert 'judah_approached_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 93:3']
    assert all('a_rival_translator_named_inside_the_midrash' not in f for f in m.WORLD["facts"])
    assert 'a_word_spoken_on_its_wheel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 93:7', 'Onkelos Genesis 44:18']
    assert all('a_test_of_strength_resolved_by_a_judgment_of_piety' not in f for f in m.WORLD["facts"])
    assert 'the_confrontation' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Genesis 44:29', 'Onkelos Genesis 42:4']
    assert all('the_third_seat_of_the_word_that_lives_in_one_law' not in f for f in m.WORLD["facts"])
    assert 'lest_harm_befall_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 44:30', 'Onkelos Genesis 44:32']
    assert all('rendered_as_love_which_is_the_arguments_premise' not in f for f in m.WORLD["facts"])
    assert 'his_soul_is_bound_up_with_his_soul' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
