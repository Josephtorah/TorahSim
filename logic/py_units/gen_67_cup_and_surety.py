#!/usr/bin/env python3
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
# ‹וַיְצַו אֶת־אֲשֶׁר עַל־בֵּיתוֹ› (“and-command obj-marker which over
# house-him/its”)
# ‹לֵאמֹר מַלֵּא אֶת־אַמְתְּחֹת› (“to-say fill obj-marker something-
# expansive”)
# ‹הָאֲנָשִׁים אֹכֶל כַּאֲשֶׁר› (“the-man food like-as/which”)
# ‹יוּכְלוּן שְׂאֵת וְשִׂים› (“be-able-ward lift/carry and-put/set”)
# ‹כֶּסֶף־אִישׁ בְּפִי אַמְתַּחְתּוֹ› (“silver man in-mouth something-
# expansive-him/its”)
# "[EN-AID] And he commanded the one over his house, saying: Fill the men's
# bags with food, as much as they can carry, and put each man's silver in
# the mouth of his bag."
m.step("Gen.44.1")
# ‹מַלֵּא אֶת־אַמְתְּחֹת הָאֲנָשִׁים› (“fill obj-marker something-expansive
# the-man”)
# — Joseph speaks a demand — LET: fill-amtechot-and-put/set-silver
m.declare("yosef", "LET",
          "male_amtechot_ve_sim_kesef")

# -------------------------- Gen.44.2 · MY_CUP_THE_SILVER_CUP ---------------
# ‹וְאֶת־גְּבִיעִי גְּבִיעַ הַכֶּסֶף› (“and-obj-marker goblet-me/my goblet
# the-silver”)
# ‹תָּשִׂים בְּפִי אַמְתַּחַת› (“put/set in-mouth something-expansive”)
# ‹הַקָּטֹן וְאֵת כֶּסֶף› (“the-small and-obj-marker silver”)
# ‹שִׁבְרוֹ וַיַּעַשׂ כִּדְבַר› (“grain-him/its and-make like-word/thing”)
# ‹יוֹסֵף אֲשֶׁר דִּבֵּר› (“Joseph which speak”)
# "[EN-AID] And my cup — the silver cup — you shall put in the mouth of the
# youngest one's bag, and the silver of his grain. And he did according to
# the word of Joseph which he spoke."
m.step("Gen.44.2")
# ‹וַיַּעַשׂ כִּדְבַר יוֹסֵף› (“and-make like-word/thing Joseph”)
# ‹אֲשֶׁר דִּבֵּר› (“which speak”)
# — demand settled (popped from the queue): fill-amtechot-and-put/set-silver
m.result("male_amtechot_ve_sim_kesef", tmark="t1")

# -------------------------- Gen.44.3 · THE_MORNING_LIGHT -------------------
# ‹הַבֹּקֶר אוֹר וְהָאֲנָשִׁים› (“the-morning give-light and-the-man”)
# ‹שֻׁלְּחוּ הֵמָּה וַחֲמֹרֵיהֶם› (“send they and-male-ass-them/their”)
# "[EN-AID] The morning was light, and the men were sent away — they and
# their donkeys."
m.step("Gen.44.3")
# ‹הַבֹּקֶר אוֹר וְהָאֲנָשִׁים› (“the-morning give-light and-the-man”)
# ‹שֻׁלְּחוּ› (“send”)
# — fact holds: the-morning-give-light-and-the-man-send
m.fact("ha_boqer_or_ve_ha_anashim_shulchu")

# -------------------------- Gen.44.4 · ARISE_PURSUE_OVERTAKE ---------------
# ‹הֵם יָצְאוּ אֶת־הָעִיר› (“they bring-forth obj-marker the-city”)
# ‹לֹא הִרְחִיקוּ וְיוֹסֵף› (“not widen and-Joseph”)
# ‹אָמַר לַאֲשֶׁר עַל־בֵּיתוֹ› (“say to-which over house-him/its”)
# ‹קוּם רְדֹף אַחֲרֵי› (“arise run-after-gone-by) after”)
# ‹הָאֲנָשִׁים וְהִשַּׂגְתָּם וְאָמַרְתָּ› (“the-man and-reach-them/their
# and-say”)
# ‹אֲלֵהֶם לָמָּה שִׁלַּמְתֶּם› (“to-them/their to-what be-safe”)
# ‹רָעָה תַּחַת טוֹבָה› (“bad under good-in-the-widest-sense”)
# "[EN-AID] They had gone out of the city — they were not far — and Joseph
# said to the one over his house: Arise, pursue after the men; and overtake
# them, and say to them: Why have you repaid evil for good?"
m.step("Gen.44.4")
# ‹קוּם רְדֹף אַחֲרֵי› (“arise run-after-gone-by) after”)
# ‹הָאֲנָשִׁים וְהִשַּׂגְתָּם› (“the-man and-reach-them/their”)
# — Joseph speaks a demand — LET: arise-run-after-gone-by)-and-hisagtam
m.declare("yosef", "LET",
          "qum_redof_ve_hisagtam")

# -------------------------- Gen.44.5 · THE_DIVINING_CUP --------------------
# ‹הֲלוֹא זֶה אֲשֶׁר› (“is-it-not this which”)
# ‹יִשְׁתֶּה אֲדֹנִי בּוֹ› (“drink lord-me/my in-him/its”)
# ‹וְהוּא נַחֵשׁ יְנַחֵשׁ› (“and-he/it hiss hiss”)
# ‹בּוֹ הֲרֵעֹתֶם אֲשֶׁר› (“in-him/its spoil which”)
# ‹עֲשִׂיתֶם› (“make”)
# "[EN-AID] Is not this that from which my lord drinks, and by which he
# surely divines? You have done evil in what you have done."
m.step("Gen.44.5")
# ‹וְהוּא נַחֵשׁ יְנַחֵשׁ› (“and-he/it hiss hiss”)
# ‹בּוֹ› (“in-him/its”)
# — fact holds: hiss-hiss-in-it
m.fact("nachesh_yenachesh_bo")
# witness-grounded state (its own tier):
# converted_to_investigation_at_both_seats on he_surely_divines
m.witness_state("he_surely_divines", "converted_to_investigation_at_both_seats",
                cites=["Onkelos Genesis 44:5", "Onkelos Genesis 44:15"])

# -------------------------- Gen.44.6 · HE_OVERTOOK_THEM --------------------
# ‹וַיַּשִּׂגֵם וַיְדַבֵּר אֲלֵהֶם› (“and-reach-them/their and-speak to-
# them/their”)
# ‹אֶת־הַדְּבָרִים הָאֵלֶּה› (“obj-marker the-word/thing the-these”)
# "[EN-AID] And he overtook them, and spoke to them these words."
m.step("Gen.44.6")
# ‹וַיַּשִּׂגֵם וַיְדַבֵּר אֲלֵהֶם› (“and-reach-them/their and-speak to-
# them/their”)
# — demand settled (popped from the queue): arise-run-after-gone-by)-and-
# hisagtam
m.result("qum_redof_ve_hisagtam", tmark="t2")

# -------------------------- Gen.44.7 · FAR_BE_IT_FROM_YOUR_SERVANTS --------
# ‹וַיֹּאמְרוּ אֵלָיו לָמָּה› (“and-say to-him/its to-what”)
# ‹יְדַבֵּר אֲדֹנִי כַּדְּבָרִים› (“speak lord-me/my like-word/thing”)
# ‹הָאֵלֶּה חָלִילָה לַעֲבָדֶיךָ› (“the-these literal-fora-profaned-thing-
# ward to-servant-you/your”)
# ‹מֵעֲשׂוֹת כַּדָּבָר הַזֶּה› (“from-make like-word/thing the-this”)
# "[EN-AID] And they said to him: Why does my lord speak according to these
# words? Far be it from your servants to do according to this thing."
m.step("Gen.44.7")
# ‹חָלִילָה לַעֲבָדֶיךָ מֵעֲשׂוֹת› (“literal-fora-profaned-thing-ward to-
# servant-you/your from-make”)
# ‹כַּדָּבָר הַזֶּה› (“like-word/thing the-this”)
# — fact holds: chalila-to-avadekha
m.fact("chalila_la_avadekha")

# -------------------------- Gen.44.8 · THE_SILVER_WE_RETURNED --------------
# ‹הֵן כֶּסֶף אֲשֶׁר› (“lo! silver which”)
# ‹מָצָאנוּ בְּפִי אַמְתְּחֹתֵינוּ› (“find in-mouth something-expansive-
# us/our”)
# ‹הֱשִׁיבֹנוּ אֵלֶיךָ מֵאֶרֶץ› (“return to-you/your from-earth”)
# ‹כְּנָעַן וְאֵיךְ נִגְנֹב› (“Canaan and-how? steal”)
# ‹מִבֵּית אֲדֹנֶיךָ כֶּסֶף› (“from-house lord-you/your silver”)
# ‹אוֹ זָהָב› (“or gold”)
# "[EN-AID] Behold, the silver which we found in the mouth of our bags we
# brought back to you from the land of Canaan; and how should we steal from
# your lord's house silver or gold?"
m.step("Gen.44.8")
# ‹הֵן כֶּסֶף אֲשֶׁר› (“lo! silver which”)
# ‹מָצָאנוּ› (“find”)
# — fact holds: lo!-silver-return-and-how?-steal
m.fact("hen_kesef_heshivonu_ve_ekh_nignov")
# witness-grounded state (its own tier):
# the_type_specimen_of_the_inference_rule on how_then_should_we_steal
m.witness_state("how_then_should_we_steal", "the_type_specimen_of_the_inference_rule",
                cites=["Bereshit Rabbah 92:7", "Onkelos Genesis 44:8"])

# -------------------------- Gen.44.9 · THE_RASH_SENTENCE -------------------
# ‹אֲשֶׁר יִמָּצֵא אִתּוֹ› (“which find with-him/its”)
# ‹מֵעֲבָדֶיךָ וָמֵת וְגַם־אֲנַחְנוּ› (“from-servant-you/your and-die and-
# also we”)
# ‹נִהְיֶה לַאדֹנִי לַעֲבָדִים› (“be to-lord-me/my to-servant”)
# "[EN-AID] With whomever of your servants it be found — let him die; and we
# also will be my lord's slaves."
m.step("Gen.44.9")
# ‹אֲשֶׁר יִמָּצֵא אִתּוֹ› (“which find with-him/its”)
# ‹מֵעֲבָדֶיךָ וָמֵת› (“from-servant-you/your and-die”)
# — fact holds: which-find-with-him-and-die
m.fact("asher_yimatze_ito_va_met")

# -------------------------- Gen.44.10 · THE_STEWARDS_SOFTENING -------------
# ‹וַיֹּאמֶר גַּם־עַתָּה כְדִבְרֵיכֶם› (“and-say also now like-word/thing-
# you/your(pl)”)
# ‹כֶּן־הוּא אֲשֶׁר יִמָּצֵא› (“so he/it which find”)
# ‹אִתּוֹ יִהְיֶה־לִּי עָבֶד› (“with-him/its be to-me/my servant”)
# ‹וְאַתֶּם תִּהְיוּ נְקִיִּם› (“and-you be innocent”)
# "[EN-AID] And he said: Now also, according to your words, so be it: with
# whom it is found shall be my slave, and you shall be clean."
m.step("Gen.44.10")
# ‹אֲשֶׁר יִמָּצֵא אִתּוֹ› (“which find with-him/its”)
# ‹יִהְיֶה־לִּי עָבֶד וְאַתֶּם› (“be to-me/my servant and-you”)
# ‹תִּהְיוּ נְקִיִּם› (“be innocent”)
# — fact holds: be-to-me-servant-and-you-be-innocent
m.fact("yihye_li_aved_ve_atem_tihyu_neqiyim")

# -------------------------- Gen.44.11 · BAGS_LOWERED -----------------------
# ‹וַיְמַהֲרוּ וַיּוֹרִדוּ אִישׁ› (“and-hasten and-go-down man”)
# ‹אֶת־אַמְתַּחְתּוֹ אָרְצָה וַיִּפְתְּחוּ› (“obj-marker something-
# expansive-him/its earth-ward and-open-wide”)
# ‹אִישׁ אַמְתַּחְתּוֹ› (“man something-expansive-him/its”)
# "[EN-AID] And they hurried, and each man lowered his bag to the earth, and
# each man opened his bag."
m.step("Gen.44.11")
# ‹וַיְמַהֲרוּ וַיּוֹרִדוּ אִישׁ› (“and-hasten and-go-down man”)
# ‹אֶת־אַמְתַּחְתּוֹ› (“obj-marker something-expansive-him/its”)
# — fact holds: and-go-down-man-obj-marker-amtachto
m.fact("va_yoridu_ish_et_amtachto")

# -------------------------- Gen.44.12 · FOUND_IN_BENJAMINS_BAG -------------
# ‹וַיְחַפֵּשׂ בַּגָּדוֹל הֵחֵל› (“and-seek in-great bore”)
# ‹וּבַקָּטֹן כִּלָּה וַיִּמָּצֵא› (“and-in-small be-complete and-find”)
# ‹הַגָּבִיעַ בְּאַמְתַּחַת בִּנְיָמִן› (“the-goblet in-something-expansive
# Benjamin”)
# "[EN-AID] And he searched — at the eldest he began, and at the youngest he
# ended; and the cup was found in Benjamin's bag."
m.step("Gen.44.12")
# ‹וַיִּמָּצֵא הַגָּבִיעַ בְּאַמְתַּחַת› (“and-find the-goblet in-something-
# expansive”)
# ‹בִּנְיָמִן› (“Benjamin”)
# — fact holds: and-find-the-goblet-in-something-expansive-Benjamin
m.fact("va_yimatze_ha_gavia_be_amtachat_binyamin")
# witness-tier presupposed read: an_old_theft_thrown_back on
# the_goblet_found_in_benjamins_sack — read, not installed
m.witness_read("the_goblet_found_in_benjamins_sack", "an_old_theft_thrown_back",
                cites=["Bereshit Rabbah 92:8"])
# witness-tier presupposed read: found_found on va_yechapes_va_yimatze —
# read, not installed
m.witness_read("va_yechapes_va_yimatze", "found_found",
                cites=["Pesachim 7b:13", "Pesachim 7b:14", "Pesachim 7b:15"])

# -------------------------- Gen.44.13 · THE_GARMENTS_TORN ------------------
# ‹וַיִּקְרְעוּ שִׂמְלֹתָם וַיַּעֲמֹס› (“and-rend dress-them/their and-
# load”)
# ‹אִישׁ עַל־חֲמֹרוֹ וַיָּשֻׁבוּ› (“man over male-ass-him/its and-return”)
# ‹הָעִירָה› (“the-city-ward”)
# "[EN-AID] And they tore their garments; and each man loaded his donkey,
# and they returned to the city."
m.step("Gen.44.13")
# ‹וַיִּקְרְעוּ שִׂמְלֹתָם› (“and-rend dress-them/their”)
# — event: qara — agent the-achim; theme simlotam
m.event("qara", agent="ha_achim", themes=["simlotam"])
# witness-tier presupposed read: the_first_installment_of_the_rending_table
# on they_rent_their_garments — read, not installed
m.witness_read("they_rent_their_garments", "the_first_installment_of_the_rending_table",
                cites=["Bereshit Rabbah 84:20"])

# -------------------------- Gen.44.14 · THEY_FALL_BEFORE_HIM ---------------
# ‹וַיָּבֹא יְהוּדָה וְאֶחָיו› (“and-come/bring Judah and-brother-him/its”)
# ‹בֵּיתָה יוֹסֵף וְהוּא› (“house-ward Joseph and-he/it”)
# ‹עוֹדֶנּוּ שָׁם וַיִּפְּלוּ› (“still/again-him/its there and-fall”)
# ‹לְפָנָיו אָרְצָה› (“to-face-him/its earth-ward”)
# "[EN-AID] And Judah and his brothers came to Joseph's house — and he was
# yet there — and they fell before him to the earth."
m.step("Gen.44.14")
# ‹וַיִּפְּלוּ לְפָנָיו אָרְצָה› (“and-fall to-face-him/its earth-ward”)
# — event: naflu — agent Judah-and-echav
m.event("naflu", agent="yehuda_ve_echav")
# witness-tier presupposed read: the_second_of_three_crowning_speeches on
# judah_and_his_brothers_came — read, not installed
m.witness_read("judah_and_his_brothers_came", "the_second_of_three_crowning_speeches",
                cites=["Bereshit Rabbah 84:17"])

# -------------------------- Gen.44.15 · A_MAN_LIKE_ME ----------------------
# ‹וַיֹּאמֶר לָהֶם יוֹסֵף› (“and-say to-them/their Joseph”)
# ‹מָה־הַמַּעֲשֶׂה הַזֶּה אֲשֶׁר› (“what the-deed/work the-this which”)
# ‹עֲשִׂיתֶם הֲלוֹא יְדַעְתֶּם› (“make is-it-not know”)
# ‹כִּי־נַחֵשׁ יְנַחֵשׁ אִישׁ› (“that hiss hiss man”)
# ‹אֲשֶׁר כָּמֹנִי› (“which form-of-the-prefix-'k-'-me/my”)
# "[EN-AID] And Joseph said to them: What is this deed you have done? Did
# you not know that a man like me surely divines?"
m.step("Gen.44.15")
# ‹כִּי־נַחֵשׁ יְנַחֵשׁ אִישׁ› (“that hiss hiss man”)
# ‹אֲשֶׁר כָּמֹנִי› (“which form-of-the-prefix-'k-'-me/my”)
# — fact holds: hiss-hiss-man-which-kamoni
m.fact("nachesh_yenachesh_ish_asher_kamoni")

# -------------------------- Gen.44.16 · GOD_HAS_FOUND_THE_GUILT ------------
# ‹וַיֹּאמֶר יְהוּדָה מַה־נֹּאמַר› (“and-say Judah what say”)
# ‹לַאדֹנִי מַה־נְּדַבֵּר וּמַה־נִּצְטַדָּק› (“to-lord-me/my what speak and-
# what be-right”)
# ‹הָאֱלֹהִים מָצָא אֶת־עֲוֺן› (“the-God find obj-marker perversity”)
# ‹עֲבָדֶיךָ הִנֶּנּוּ עֲבָדִים› (“servant-you/your lo!-us/our servant”)
# ‹לַאדֹנִי גַּם־אֲנַחְנוּ גַּם› (“to-lord-me/my also we also”)
# ‹אֲשֶׁר־נִמְצָא הַגָּבִיעַ בְּיָדוֹ› (“which find the-goblet in-hand-
# him/its”)
# "[EN-AID] And Judah said: What shall we say to my lord? What shall we
# speak, and how shall we clear ourselves? God has found the guilt of your
# servants: behold, we are my lord's slaves — both we and he in whose hand
# the cup was found."
m.step("Gen.44.16")
# ‹הָאֱלֹהִים מָצָא אֶת־עֲוֺן› (“the-God find obj-marker perversity”)
# ‹עֲבָדֶיךָ› (“servant-you/your”)
# — fact holds: the-God-find-obj-marker-perversity-avadekha
m.fact("ha_Elohim_matza_et_avon_avadekha")
# witness-tier presupposed read:
# the_chain_personalizes_where_the_buffer_depersonalizes on
# god_has_found_the_iniquity — read, not installed
m.witness_read("god_has_found_the_iniquity", "the_chain_personalizes_where_the_buffer_depersonalizes",
                cites=["Onkelos Genesis 44:16", "Bereshit Rabbah 92:9"])

# -------------------------- Gen.44.17 · GO_UP_IN_PEACE ---------------------
# ‹וַיֹּאמֶר חָלִילָה לִּי› (“and-say literal-fora-profaned-thing-ward to-
# me/my”)
# ‹מֵעֲשׂוֹת זֹאת הָאִישׁ› (“from-make this the-man”)
# ‹אֲשֶׁר נִמְצָא הַגָּבִיעַ› (“which find the-goblet”)
# ‹בְּיָדוֹ הוּא יִהְיֶה־לִּי› (“in-hand-him/its he/it be to-me/my”)
# ‹עָבֶד וְאַתֶּם עֲלוּ› (“servant and-you go-up”)
# ‹לְשָׁלוֹם אֶל־אֲבִיכֶם› (“to-safe to father-you/your(pl)”)
# "[EN-AID] And he said: Far be it from me to do this; the man in whose hand
# the cup was found — he shall be my slave; and you — go up in peace to your
# father."
m.step("Gen.44.17")
# ‹וְאַתֶּם עֲלוּ לְשָׁלוֹם› (“and-you go-up to-safe”)
# ‹אֶל־אֲבִיכֶם› (“to father-you/your(pl)”)
# — Joseph speaks a demand — LET: go-up-to-safe-to-avikhem
m.declare("yosef", "LET",
          "alu_le_shalom_el_avikhem")

# -------------------------- Gen.44.18 · JUDAH_DRAWS_NEAR -------------------
# ‹וַיִּגַּשׁ אֵלָיו יְהוּדָה› (“and-be to-him/its Judah”)
# ‹וַיֹּאמֶר בִּי אֲדֹנִי› (“and-say oh-that! lord-me/my”)
# ‹יְדַבֶּר־נָא עַבְדְּךָ דָבָר› (“speak please servant-you/your
# word/thing”)
# ‹בְּאָזְנֵי אֲדֹנִי וְאַל־יִחַר› (“in-broadness.-i.e.-the-ear lord-me/my
# and-do-not glow”)
# ‹אַפְּךָ בְּעַבְדֶּךָ כִּי› (“nose-you/your in-servant-you/your that”)
# ‹כָמוֹךָ כְּפַרְעֹה› (“form-of-the-prefix-'k-'-you/your like-Pharaoh”)
# "[EN-AID] And Judah drew near to him and said: Please, my lord, let your
# servant speak a word in my lord's ears, and let not your anger burn
# against your servant — for you are as Pharaoh."
m.step("Gen.44.18")
# ‹וַיִּגַּשׁ אֵלָיו יְהוּדָה› (“and-be to-him/its Judah”)
# — event: nigash — agent Judah
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
# ‹אֲדֹנִי שָׁאַל אֶת־עֲבָדָיו› (“lord-me/my inquire obj-marker servant-
# him/its”)
# ‹לֵאמֹר הֲיֵשׁ־לָכֶם אָב› (“to-say the-there-is to-you/your(pl) father”)
# ‹אוֹ־אָח› (“or brother”)
# "[EN-AID] My lord asked his servants, saying: Have you a father, or a
# brother?"
m.step("Gen.44.19")
# ‹אֲדֹנִי שָׁאַל אֶת־עֲבָדָיו› (“lord-me/my inquire obj-marker servant-
# him/its”)
# — fact holds: adoni-inquire-obj-marker-avadav
m.fact("adoni_shaal_et_avadav")

# -------------------------- Gen.44.20 · A_CHILD_OF_OLD_AGE -----------------
# ‹וַנֹּאמֶר אֶל־אֲדֹנִי יֶשׁ־לָנוּ› (“and-say to lord-me/my there-is to-
# us/our”)
# ‹אָב זָקֵן וְיֶלֶד› (“father old and-child”)
# ‹זְקֻנִים קָטָן וְאָחִיו› (“old-age abbreviated and-brother-him/its”)
# ‹מֵת וַיִּוָּתֵר הוּא› (“die and-jut-over he/it”)
# ‹לְבַדּוֹ לְאִמּוֹ וְאָבִיו› (“to-separation-him/its to-mother-him/its
# and-father-him/its”)
# ‹אֲהֵבוֹ› (“have-affection-for-him/its”)
# "[EN-AID] And we said to my lord: We have an old father, and a child of
# old age, a little one; and his brother is dead, and he alone is left of
# his mother, and his father loves him."
m.step("Gen.44.20")
# ‹וְיֶלֶד זְקֻנִים קָטָן› (“and-child old-age abbreviated”)
# — fact holds: child-old-age-abbreviated-and-his-brother-die
m.fact("yeled_zequnim_qatan_ve_achiv_met")

# -------------------------- Gen.44.21 · BRING_HIM_DOWN_TO_ME ---------------
# ‹וַתֹּאמֶר אֶל־עֲבָדֶיךָ הוֹרִדֻהוּ› (“and-say to servant-you/your go-
# down-him/its”)
# ‹אֵלָי וְאָשִׂימָה עֵינִי› (“to-me/my and-put/set eye-me/my”)
# ‹עָלָיו› (“over-him/its”)
# "[EN-AID] And you said to your servants: Bring him down to me, that I may
# set my eye upon him."
m.step("Gen.44.21")
# ‹וַתֹּאמֶר אֶל־עֲבָדֶיךָ הוֹרִדֻהוּ› (“and-say to servant-you/your go-
# down-him/its”)
# ‹אֵלָי› (“to-me/my”)
# — fact holds: horiduhu-elai-and-put/set-eni-alav
m.fact("horiduhu_elai_ve_asima_eni_alav")

# -------------------------- Gen.44.22 · HE_CANNOT_LEAVE_HIS_FATHER ---------
# ‹וַנֹּאמֶר אֶל־אֲדֹנִי לֹא־יוּכַל› (“and-say to lord-me/my not be-able”)
# ‹הַנַּעַר לַעֲזֹב אֶת־אָבִיו› (“the-boy to-loosen obj-marker father-
# him/its”)
# ‹וְעָזַב אֶת־אָבִיו וָמֵת› (“and-loosen obj-marker father-him/its and-
# die”)
# "[EN-AID] And we said to my lord: The lad cannot leave his father; should
# he leave his father, he would die."
m.step("Gen.44.22")
# ‹לֹא־יוּכַל הַנַּעַר לַעֲזֹב› (“not be-able the-boy to-loosen”)
# ‹אֶת־אָבִיו› (“obj-marker father-him/its”)
# — fact holds: not-be-able-the-boy-laazov-obj-marker-aviv
m.fact("lo_yukhal_ha_naar_laazov_et_aviv")

# -------------------------- Gen.44.23 · YOU_SHALL_NOT_SEE_MY_FACE ----------
# ‹וַתֹּאמֶר אֶל־עֲבָדֶיךָ אִם־לֹא› (“and-say to servant-you/your if not”)
# ‹יֵרֵד אֲחִיכֶם הַקָּטֹן› (“go-down brother-you/your(pl) the-small”)
# ‹אִתְּכֶם לֹא תֹסִפוּן› (“with-you/your(pl) not add-ward”)
# ‹לִרְאוֹת פָּנָי› (“to-see face-me/my”)
# "[EN-AID] And you said to your servants: If your youngest brother does not
# come down with you, you shall not again see my face."
m.step("Gen.44.23")
# ‹לֹא תֹסִפוּן לִרְאוֹת› (“not add-ward to-see”)
# ‹פָּנָי› (“face-me/my”)
# — fact holds: not-tosifun-lirot-panai
m.fact("lo_tosifun_lirot_panai")

# -------------------------- Gen.44.24 · WE_TOLD_MY_FATHER ------------------
# ‹וַיְהִי כִּי עָלִינוּ› (“and-be that go-up”)
# ‹אֶל־עַבְדְּךָ אָבִי וַנַּגֶּד־לוֹ› (“to servant-you/your father-me/my
# and-tell to-him/its”)
# ‹אֵת דִּבְרֵי אֲדֹנִי› (“obj-marker word/thing lord-me/my”)
# "[EN-AID] And it was, when we went up to your servant my father, that we
# told him the words of my lord."
m.step("Gen.44.24")
# ‹וַנַּגֶּד־לוֹ אֵת דִּבְרֵי› (“and-tell to-him/its obj-marker word/thing”)
# ‹אֲדֹנִי› (“lord-me/my”)
# — fact holds: and-tell-not-obj-marker-word/thing-adoni
m.fact("va_naged_lo_et_divre_adoni")

# -------------------------- Gen.44.25 · OUR_FATHER_SAID_RETURN -------------
# ‹וַיֹּאמֶר אָבִינוּ שֻׁבוּ› (“and-say father-us/our return”)
# ‹שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“deal-in-grain to-us/our little food”)
# "[EN-AID] And our father said: Return, buy us a little food."
m.step("Gen.44.25")
# ‹שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“return deal-in-grain to-us/our
# little food”)
# — fact holds: return-deal-in-grain-lanu-little-food-requoted
m.fact("shuvu_shivru_lanu_meat_okhel_requoted")

# -------------------------- Gen.44.26 · WE_CANNOT_GO_DOWN ------------------
# ‹וַנֹּאמֶר לֹא נוּכַל› (“and-say not be-able”)
# ‹לָרֶדֶת אִם־יֵשׁ אָחִינוּ› (“to-go-down if there-is brother-us/our”)
# ‹הַקָּטֹן אִתָּנוּ וְיָרַדְנוּ› (“the-small with-us/our and-go-down”)
# ‹כִּי־לֹא נוּכַל לִרְאוֹת› (“that not be-able to-see”)
# ‹פְּנֵי הָאִישׁ וְאָחִינוּ› (“face the-man and-brother-us/our”)
# ‹הַקָּטֹן אֵינֶנּוּ אִתָּנוּ› (“the-small there-is-not-him/its with-
# us/our”)
# "[EN-AID] And we said: We cannot go down; if our youngest brother is with
# us, we will go down — for we cannot see the man's face and our youngest
# brother not with us."
m.step("Gen.44.26")
# ‹וַנֹּאמֶר לֹא נוּכַל› (“and-say not be-able”)
# ‹לָרֶדֶת› (“to-go-down”)
# — fact holds: not-be-able-laredet-if-there-is-not-achinu
m.fact("lo_nukhal_laredet_im_en_achinu")

# -------------------------- Gen.44.27 · TWO_MY_WIFE_BORE_ME ----------------
# ‹וַיֹּאמֶר עַבְדְּךָ אָבִי› (“and-say servant-you/your father-me/my”)
# ‹אֵלֵינוּ אַתֶּם יְדַעְתֶּם› (“to-us/our you know”)
# ‹כִּי שְׁנַיִם יָלְדָה־לִּי› (“that two bear-young to-me/my”)
# ‹אִשְׁתִּי› (“woman-me/my”)
# "[EN-AID] And your servant my father said to us: You know that my wife
# bore me two."
m.step("Gen.44.27")
# ‹כִּי שְׁנַיִם יָלְדָה־לִּי› (“that two bear-young to-me/my”)
# ‹אִשְׁתִּי› (“woman-me/my”)
# — fact holds: two-bear-young-to-me-ishti
m.fact("shenayim_yalda_li_ishti")

# -------------------------- Gen.44.28 · TORN_TORN --------------------------
# ‹וַיֵּצֵא הָאֶחָד מֵאִתִּי› (“and-bring-forth the-one from-with-me/my”)
# ‹וָאֹמַר אַךְ טָרֹף› (“and-say indeed pluck-off”)
# ‹טֹרָף וְלֹא רְאִיתִיו› (“pluck-off and-not see-him/its”)
# ‹עַד־הֵנָּה› (“until hither”)
# "[EN-AID] And the one went out from me, and I said: Surely torn, torn —
# and I have not seen him until now."
m.step("Gen.44.28")
# ‹אַךְ טָרֹף טֹרָף› (“indeed pluck-off pluck-off”)
# — fact holds: indeed-pluck-off-pluck-off-and-not-reitiv
m.fact("akh_tarof_toraf_ve_lo_reitiv")
# witness-grounded state (its own tier):
# two_seats_in_the_torah_one_rendering on surely_torn_torn
m.witness_state("surely_torn_torn", "two_seats_in_the_torah_one_rendering",
                cites=["Onkelos Genesis 44:28", "Bereshit Rabbah 93:8"])

# -------------------------- Gen.44.29 · GRAY_HAIR_IN_EVIL ------------------
# ‹וּלְקַחְתֶּם גַּם־אֶת־זֶה מֵעִם› (“and-take also obj-marker this from-
# with”)
# ‹פָּנַי וְקָרָהוּ אָסוֹן› (“face-me/my and-light-upon-him/its hurt”)
# ‹וְהוֹרַדְתֶּם אֶת־שֵׂיבָתִי בְּרָעָה› (“and-go-down obj-marker old-age-
# me/my in-bad”)
# ‹שְׁאֹלָה› (“Shᵉ'Owl-ward”)
# "[EN-AID] And should you take this one also from before my face, and harm
# befall him — you will bring down my gray hair in evil to Sheol."
m.step("Gen.44.29")
# ‹וְהוֹרַדְתֶּם אֶת־שֵׂיבָתִי בְּרָעָה› (“and-go-down obj-marker old-age-
# me/my in-bad”)
# ‹שְׁאֹלָה› (“Shᵉ'Owl-ward”)
# — fact holds: and-go-down-obj-marker-sevati-in-bad-sheola
m.fact("ve_horadtem_et_sevati_be_raa_sheola")
# witness-tier presupposed read:
# the_third_seat_of_the_word_that_lives_in_one_law on lest_harm_befall_him —
# read, not installed
m.witness_read("lest_harm_befall_him", "the_third_seat_of_the_word_that_lives_in_one_law",
                cites=["Onkelos Genesis 44:29", "Onkelos Genesis 42:4"])

# -------------------------- Gen.44.30 · SOUL_BOUND_TO_SOUL -----------------
# ‹וְעַתָּה כְּבֹאִי אֶל־עַבְדְּךָ› (“and-now like-come/bring-me/my to
# servant-you/your”)
# ‹אָבִי וְהַנַּעַר אֵינֶנּוּ› (“father-me/my and-the-boy there-is-not-
# him/its”)
# ‹אִתָּנוּ וְנַפְשׁוֹ קְשׁוּרָה› (“with-us/our and-living-being-him/its
# tie”)
# ‹בְנַפְשׁוֹ› (“in-living-being-him/its”)
# "[EN-AID] And now, when I come to your servant my father and the lad is
# not with us — and his soul is bound to his soul —"
m.step("Gen.44.30")
# ‹וְנַפְשׁוֹ קְשׁוּרָה בְנַפְשׁוֹ› (“and-living-being-him/its tie in-
# living-being-him/its”)
# — fact holds: and-nafsho-tie-and-nafsho
m.fact("ve_nafsho_qeshura_ve_nafsho")
# witness-tier presupposed read:
# rendered_as_love_which_is_the_arguments_premise on
# his_soul_is_bound_up_with_his_soul — read, not installed
m.witness_read("his_soul_is_bound_up_with_his_soul", "rendered_as_love_which_is_the_arguments_premise",
                cites=["Onkelos Genesis 44:30", "Onkelos Genesis 44:32"])

# -------------------------- Gen.44.31 · WHEN_HE_SEES_THE_LAD_IS_NOT --------
# ‹וְהָיָה כִּרְאוֹתוֹ כִּי־אֵין› (“and-be like-see-him/its that there-is-
# not”)
# ‹הַנַּעַר וָמֵת וְהוֹרִידוּ› (“the-boy and-die and-go-down”)
# ‹עֲבָדֶיךָ אֶת־שֵׂיבַת עַבְדְּךָ› (“servant-you/your obj-marker old-age
# servant-you/your”)
# ‹אָבִינוּ בְּיָגוֹן שְׁאֹלָה› (“father-us/our in-affliction Shᵉ'Owl-ward”)
# "[EN-AID] then it will be, when he sees that the lad is not — he will die;
# and your servants will bring down the gray hair of your servant our father
# in sorrow to Sheol."
m.step("Gen.44.31")
# ‹כִּרְאוֹתוֹ כִּי־אֵין הַנַּעַר› (“like-see-him/its that there-is-not the-
# boy”)
# ‹וָמֵת› (“and-die”)
# — fact holds: that-there-is-not-the-boy-and-die
m.fact("ki_en_ha_naar_va_met")

# -------------------------- Gen.44.32 · YOUR_SERVANT_IS_SURETY -------------
# ‹כִּי עַבְדְּךָ עָרַב› (“that servant-you/your braid”)
# ‹אֶת־הַנַּעַר מֵעִם אָבִי› (“obj-marker the-boy from-with father-me/my”)
# ‹לֵאמֹר אִם־לֹא אֲבִיאֶנּוּ› (“to-say if not come/bring-him/its”)
# ‹אֵלֶיךָ וְחָטָאתִי לְאָבִי› (“to-you/your and-sin to-father-me/my”)
# ‹כָּל־הַיָּמִים› (“all the-day”)
# "[EN-AID] For your servant became surety for the lad from my father,
# saying: If I do not bring him to you, I shall have sinned against my
# father all the days."
m.step("Gen.44.32")
# ‹כִּי עַבְדְּךָ עָרַב› (“that servant-you/your braid”)
# ‹אֶת־הַנַּעַר› (“obj-marker the-boy”)
# — fact holds: that-avdekha-braid-obj-marker-the-boy
m.fact("ki_avdekha_arav_et_ha_naar")

# -------------------------- Gen.44.33 · LET_ME_STAY_INSTEAD ----------------
# ‹וְעַתָּה יֵשֶׁב־נָא עַבְדְּךָ› (“and-now dwell/sit please servant-
# you/your”)
# ‹תַּחַת הַנַּעַר עֶבֶד› (“under the-boy servant”)
# ‹לַאדֹנִי וְהַנַּעַר יַעַל› (“to-lord-me/my and-the-boy go-up”)
# ‹עִם־אֶחָיו› (“with brother-him/its”)
# "[EN-AID] And now — let your servant stay instead of the lad, a slave to
# my lord; and let the lad go up with his brothers."
m.step("Gen.44.33")
# ‹וְעַתָּה יֵשֶׁב־נָא עַבְדְּךָ› (“and-now dwell/sit please servant-
# you/your”)
# ‹תַּחַת הַנַּעַר› (“under the-boy”)
# — Judah speaks a demand — LET: dwell/sit-please-avdekha-under-the-boy
m.declare("yehuda", "LET",
          "yeshev_na_avdekha_tachat_ha_naar")

# -------------------------- Gen.44.34 · HOW_SHALL_I_GO_UP ------------------
# ‹כִּי־אֵיךְ אֶעֱלֶה אֶל־אָבִי› (“that how? go-up to father-me/my”)
# ‹וְהַנַּעַר אֵינֶנּוּ אִתִּי› (“and-the-boy there-is-not-him/its with-
# me/my”)
# ‹פֶּן אֶרְאֶה בָרָע› (“lest see in-bad”)
# ‹אֲשֶׁר יִמְצָא אֶת־אָבִי› (“which find obj-marker father-me/my”)
# "[EN-AID] For how shall I go up to my father and the lad is not with me —
# lest I see the evil that would find my father?"
m.step("Gen.44.34")
# ‹כִּי־אֵיךְ אֶעֱלֶה אֶל־אָבִי› (“that how? go-up to father-me/my”)
# ‹וְהַנַּעַר אֵינֶנּוּ אִתִּי› (“and-the-boy there-is-not-him/its with-
# me/my”)
# — fact holds: how?-go-up-to-avi-and-the-boy-enennu
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_goblet_found_in_benjamins_sack', 'an_old_theft_thrown_back'), ('va_yechapes_va_yimatze', 'found_found'), ('they_rent_their_garments', 'the_first_installment_of_the_rending_table'), ('judah_and_his_brothers_came', 'the_second_of_three_crowning_speeches'), ('god_has_found_the_iniquity', 'the_chain_personalizes_where_the_buffer_depersonalizes'), ('judah_approached_him', 'persuasion_as_incremental_extraction'), ('a_word_spoken_on_its_wheel', 'a_rival_translator_named_inside_the_midrash'), ('the_confrontation', 'a_test_of_strength_resolved_by_a_judgment_of_piety'), ('lest_harm_befall_him', 'the_third_seat_of_the_word_that_lives_in_one_law'), ('his_soul_is_bound_up_with_his_soul', 'rendered_as_love_which_is_the_arguments_premise')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 92:8']
    assert all('an_old_theft_thrown_back' not in f for f in m.WORLD["facts"])
    assert 'the_goblet_found_in_benjamins_sack' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Pesachim 7b:13', 'Pesachim 7b:14', 'Pesachim 7b:15']
    assert all('found_found' not in f for f in m.WORLD["facts"])
    assert 'va_yechapes_va_yimatze' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 84:20']
    assert all('the_first_installment_of_the_rending_table' not in f for f in m.WORLD["facts"])
    assert 'they_rent_their_garments' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 84:17']
    assert all('the_second_of_three_crowning_speeches' not in f for f in m.WORLD["facts"])
    assert 'judah_and_his_brothers_came' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Onkelos Genesis 44:16', 'Bereshit Rabbah 92:9']
    assert all('the_chain_personalizes_where_the_buffer_depersonalizes' not in f for f in m.WORLD["facts"])
    assert 'god_has_found_the_iniquity' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 93:4']
    assert all('persuasion_as_incremental_extraction' not in f for f in m.WORLD["facts"])
    assert 'judah_approached_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 93:3']
    assert all('a_rival_translator_named_inside_the_midrash' not in f for f in m.WORLD["facts"])
    assert 'a_word_spoken_on_its_wheel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 93:7', 'Onkelos Genesis 44:18']
    assert all('a_test_of_strength_resolved_by_a_judgment_of_piety' not in f for f in m.WORLD["facts"])
    assert 'the_confrontation' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 44:29', 'Onkelos Genesis 42:4']
    assert all('the_third_seat_of_the_word_that_lives_in_one_law' not in f for f in m.WORLD["facts"])
    assert 'lest_harm_befall_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 44:30', 'Onkelos Genesis 44:32']
    assert all('rendered_as_love_which_is_the_arguments_premise' not in f for f in m.WORLD["facts"])
    assert 'his_soul_is_bound_up_with_his_soul' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
