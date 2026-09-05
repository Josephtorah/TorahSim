#!/usr/bin/env python3
# =============================================================================
# gen_66_second_descent — 43:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_66_second_descent.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The second descent: Benjamin before Joseph (43:1-34)"""
from machine import Machine

m = Machine("gen_66_second_descent")

# -------------------------- Gen.43.1 · THE_FAMINE_HEAVY --------------------
# ‹וְהָרָעָב כָּבֵד בָּאָרֶץ› (“and-the-hunger heavy in-earth”)
# "[EN-AID] And the famine was heavy in the land."
m.step("Gen.43.1")
# ‹וְהָרָעָב כָּבֵד בָּאָרֶץ› (“and-the-hunger heavy in-earth”)
# — fact holds: and-the-hunger-heavy-come/bring-earth
m.fact("ve_ha_raav_kaved_ba_aretz")
# witness-tier presupposed read: an_enumerated_member_of_the_paved_way on
# the_famine_was_severe — read, not installed
m.witness_read("the_famine_was_severe", "an_enumerated_member_of_the_paved_way",
                cites=["Bereshit Rabbah 40:6"])

# -------------------------- Gen.43.2 · RETURN_AND_BUY_A_LITTLE -------------
# ‹וַיְהִי כַּאֲשֶׁר כִּלּוּ› (“and-be like-as/which be-complete”)
# ‹לֶאֱכֹל אֶת־הַשֶּׁבֶר אֲשֶׁר› (“to-eat obj-marker the-grain which”)
# ‹הֵבִיאוּ מִמִּצְרָיִם וַיֹּאמֶר› (“come/bring from-Egypt and-say”)
# ‹אֲלֵיהֶם אֲבִיהֶם שֻׁבוּ› (“to-them/their father-them/their return”)
# ‹שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“deal-in-grain to-us/our little food”)
# "[EN-AID] And it was, when they had finished eating the grain which they
# brought from Egypt, that their father said to them: Return, buy us a
# little food."
m.step("Gen.43.2")
# ‹שֻׁבוּ שִׁבְרוּ־לָנוּ מְעַט־אֹכֶל› (“return deal-in-grain to-us/our
# little food”)
# — yaaqov speaks a demand — LET: return-deal-in-grain-lanu-little-food
m.declare("yaaqov", "LET",
          "shuvu_shivru_lanu_meat_okhel")

# -------------------------- Gen.43.3 · THE_WITNESS_WARNING -----------------
# ‹וַיֹּאמֶר אֵלָיו יְהוּדָה› (“and-say to-him/its Judah”)
# ‹לֵאמֹר הָעֵד הֵעִד› (“to-say duplicate duplicate”)
# ‹בָּנוּ הָאִישׁ לֵאמֹר› (“in-us/our the-man to-say”)
# ‹לֹא־תִרְאוּ פָנַי בִּלְתִּי› (“not see face-me/my failure-of”)
# ‹אֲחִיכֶם אִתְּכֶם› (“brother-you/your(pl) with-you/your(pl)”)
# "[EN-AID] And Judah said to him, saying: The man solemnly warned us,
# saying: You shall not see my face without your brother with you."
m.step("Gen.43.3")
# ‹הָעֵד הֵעִד בָּנוּ› (“duplicate duplicate in-us/our”)
# ‹הָאִישׁ› (“the-man”)
# — fact holds: duplicate-duplicate-banu-the-man
m.fact("haed_heid_banu_ha_ish")

# -------------------------- Gen.43.4 · IF_YOU_SEND -------------------------
# ‹אִם־יֶשְׁךָ מְשַׁלֵּחַ אֶת־אָחִינוּ› (“if there-is-you/your send obj-
# marker brother-us/our”)
# ‹אִתָּנוּ נֵרְדָה וְנִשְׁבְּרָה› (“with-us/our go-down and-deal-in-grain”)
# ‹לְךָ אֹכֶל› (“to-you/your food”)
# "[EN-AID] If you are sending our brother with us, we will go down and buy
# you food."
m.step("Gen.43.4")
# ‹אִם־יֶשְׁךָ מְשַׁלֵּחַ אֶת־אָחִינוּ› (“if there-is-you/your send obj-
# marker brother-us/our”)
# ‹אִתָּנוּ נֵרְדָה› (“with-us/our go-down”)
# — fact holds: if-yeshkha-meshaleach-go-down
m.fact("im_yeshkha_meshaleach_nerda")

# -------------------------- Gen.43.5 · IF_YOU_SEND_NOT ---------------------
# ‹וְאִם־אֵינְךָ מְשַׁלֵּחַ לֹא› (“and-if there-is-not-you/your send not”)
# ‹נֵרֵד כִּי־הָאִישׁ אָמַר› (“go-down that the-man say”)
# ‹אֵלֵינוּ לֹא־תִרְאוּ פָנַי› (“to-us/our not see face-me/my”)
# ‹בִּלְתִּי אֲחִיכֶם אִתְּכֶם› (“failure-of brother-you/your(pl) with-
# you/your(pl)”)
# "[EN-AID] And if you are not sending — we will not go down; for the man
# said to us: You shall not see my face without your brother with you."
m.step("Gen.43.5")
# ‹וְאִם־אֵינְךָ מְשַׁלֵּחַ לֹא› (“and-if there-is-not-you/your send not”)
# ‹נֵרֵד› (“go-down”)
# — fact holds: and-if-enkha-meshaleach-not-go-down
m.fact("ve_im_enkha_meshaleach_lo_nered")

# -------------------------- Gen.43.6 · WHY_DID_YOU_TELL --------------------
# ‹וַיֹּאמֶר יִשְׂרָאֵל לָמָה› (“and-say Israel to-what”)
# ‹הֲרֵעֹתֶם לִי לְהַגִּיד› (“spoil to-me/my to-tell”)
# ‹לָאִישׁ הַעוֹד לָכֶם› (“to-man the-still/again to-you/your(pl)”)
# ‹אָח› (“brother”)
# "[EN-AID] And Israel said: Why did you deal ill with me, to tell the man
# you had yet a brother?"
m.step("Gen.43.6")
# ‹וַיֹּאמֶר יִשְׂרָאֵל לָמָה› (“and-say Israel to-what”)
# ‹הֲרֵעֹתֶם לִי› (“spoil to-me/my”)
# — fact holds: lama-spoil-to-me-lehagid
m.fact("lama_hareotem_li_lehagid")

# -------------------------- Gen.43.7 · THE_MAN_ASKED_AND_ASKED -------------
# ‹וַיֹּאמְרוּ שָׁאוֹל שָׁאַל־הָאִישׁ› (“and-say inquire inquire the-man”)
# ‹לָנוּ וּלְמוֹלַדְתֵּנוּ לֵאמֹר› (“to-us/our and-to-nativity-us/our to-
# say”)
# ‹הַעוֹד אֲבִיכֶם חַי› (“the-still/again father-you/your(pl) living”)
# ‹הֲיֵשׁ לָכֶם אָח› (“the-there-is to-you/your(pl) brother”)
# ‹וַנַגֶּד־לוֹ עַל־פִּי הַדְּבָרִים› (“and-tell to-him/its over mouth the-
# word/thing”)
# ‹הָאֵלֶּה הֲיָדוֹעַ נֵדַע› (“the-these the-know know”)
# ‹כִּי יֹאמַר הוֹרִידוּ› (“that say go-down”)
# ‹אֶת־אֲחִיכֶם› (“obj-marker brother-you/your(pl)”)
# "[EN-AID] And they said: The man asked and asked about us and about our
# kindred, saying: Is your father yet alive? Have you a brother? And we told
# him according to these words. Could we know, knowing that he would say:
# Bring your brother down?"
m.step("Gen.43.7")
# ‹שָׁאוֹל שָׁאַל־הָאִישׁ› (“inquire inquire the-man”)
# — fact holds: inquire-inquire-the-man-lanu
m.fact("shaol_shaal_ha_ish_lanu")

# -------------------------- Gen.43.8 · SEND_THE_LAD_WITH_ME ----------------
# ‹וַיֹּאמֶר יְהוּדָה אֶל־יִשְׂרָאֵל› (“and-say Judah to Israel”)
# ‹אָבִיו שִׁלְחָה הַנַּעַר› (“father-him/its send-ward the-boy”)
# ‹אִתִּי וְנָקוּמָה וְנֵלֵכָה› (“with-me/my and-arise and-go”)
# ‹וְנִחְיֶה וְלֹא נָמוּת› (“and-live and-not die”)
# ‹גַּם־אֲנַחְנוּ גַם־אַתָּה גַּם־טַפֵּנוּ› (“also we also you also family-
# us/our”)
# "[EN-AID] And Judah said to Israel his father: Send the lad with me, and
# we will arise and go, and we will live and not die — we, and you, and our
# little ones."
m.step("Gen.43.8")
# ‹שִׁלְחָה הַנַּעַר אִתִּי› (“send-ward the-boy with-me/my”)
# — Judah speaks a demand — LET: shilcha-the-boy-iti
m.declare("yehuda", "LET",
          "shilcha_ha_naar_iti")

# -------------------------- Gen.43.9 · I_AM_THE_SURETY ---------------------
# ‹אָנֹכִי אֶעֶרְבֶנּוּ מִיָּדִי› (“braid-him/its from-hand-me/my”)
# ‹תְּבַקְשֶׁנּוּ אִם־לֹא הֲבִיאֹתִיו› (“search-out-him/its if not
# come/bring-him/its”)
# ‹אֵלֶיךָ וְהִצַּגְתִּיו לְפָנֶיךָ› (“to-you/your and-place-permanently-
# him/its to-face-you/your”)
# ‹וְחָטָאתִי לְךָ כָּל־הַיָּמִים› (“and-sin to-you/your all the-day”)
# "[EN-AID] I will be surety for him; from my hand you shall require him: if
# I do not bring him to you and set him before you, I shall have sinned
# against you all the days."
m.step("Gen.43.9")
# ‹אָנֹכִי אֶעֶרְבֶנּוּ מִיָּדִי› (“braid-him/its from-hand-me/my”)
# ‹תְּבַקְשֶׁנּוּ› (“search-out-him/its”)
# — fact holds: anokhi-eervenu-who?-yadi-tevaqshenu
m.fact("anokhi_eervenu_mi_yadi_tevaqshenu")
# witness-tier presupposed read: read_clause_by_clause_through_a_proverb on
# judahs_pledge — read, not installed
m.witness_read("judahs_pledge", "read_clause_by_clause_through_a_proverb",
                cites=["Bereshit Rabbah 93:1", "Onkelos Genesis 43:9"])
# witness-tier presupposed read: surety_root on anokhi_eervenu — read, not
# installed
m.witness_read("anokhi_eervenu", "surety_root",
                cites=["Bava Batra 173b:8", "Bava Batra 173b:9", "Bava Batra 173b:10", "Bava Batra 173b:11"])
# witness-tier presupposed read: conditional_ban on ve_chatati_kol_ha_yamim
# — read, not installed
m.witness_read("ve_chatati_kol_ha_yamim", "conditional_ban",
                cites=["Makkot 11b:1", "Makkot 11b:2"])

# -------------------------- Gen.43.10 · WE_COULD_HAVE_RETURNED_TWICE -------
# ‹כִּי לוּלֵא הִתְמַהְמָהְנוּ› (“that if-not question”)
# ‹כִּי־עַתָּה שַׁבְנוּ זֶה› (“that now return this”)
# ‹פַעֲמָיִם› (“stroke”)
# "[EN-AID] For had we not lingered, surely by now we could have returned
# these two times."
m.step("Gen.43.10")
# ‹כִּי לוּלֵא הִתְמַהְמָהְנוּ› (“that if-not question”)
# — fact holds: that-if-not-question
m.fact("ki_lule_hitmahmahnu")
# witness-grounded state (its own tier):
# a_standing_rule_meeting_its_own_objection on had_we_not_delayed
m.witness_state("had_we_not_delayed", "a_standing_rule_meeting_its_own_objection",
                cites=["Bereshit Rabbah 74:12"])

# -------------------------- Gen.43.11 · THE_FATHERS_CARAVAN_PLAN -----------
# ‹וַיֹּאמֶר אֲלֵהֶם יִשְׂרָאֵל› (“and-say to-them/their Israel”)
# ‹אֲבִיהֶם אִם־כֵּן אֵפוֹא› (“father-them/their if so strictly-a-
# demonstrative-par”)
# ‹זֹאת עֲשׂוּ קְחוּ› (“this make take”)
# ‹מִזִּמְרַת הָאָרֶץ בִּכְלֵיכֶם› (“from-pruned-fruit the-earth in-vessel-
# you/your(pl)”)
# ‹וְהוֹרִידוּ לָאִישׁ מִנְחָה› (“and-go-down to-man grain-offering”)
# ‹מְעַט צֳרִי וּמְעַט› (“little distillation and-little”)
# ‹דְּבַשׁ נְכֹאת וָלֹט› (“honey smiting and-gum”)
# ‹בָּטְנִים וּשְׁקֵדִים› (“pistachio-nut and-almond”)
# "[EN-AID] And Israel their father said to them: If so, then, this do: take
# of the land's best fruits in your vessels, and carry down to the man a
# gift — a little balm and a little honey, gum and ladanum, pistachios and
# almonds."
m.step("Gen.43.11")
# ‹זֹאת עֲשׂוּ קְחוּ› (“this make take”)
# ‹מִזִּמְרַת הָאָרֶץ בִּכְלֵיכֶם› (“from-pruned-fruit the-earth in-vessel-
# you/your(pl)”)
# ‹וְהוֹרִידוּ› (“and-go-down”)
# — Israel speaks a demand — LET: this-make-take-and-go-down
m.declare("yisrael", "LET",
          "zot_asu_qechu_ve_horidu")
# witness-grounded state (its own tier):
# the_particle_that_wires_deception_to_repayment on if_so_then_do_this
m.witness_state("if_so_then_do_this", "the_particle_that_wires_deception_to_repayment",
                cites=["Bereshit Rabbah 91:11"])

# -------------------------- Gen.43.12 · DOUBLE_SILVER_AND_THE_RETURNED -----
# ‹וְכֶסֶף מִשְׁנֶה קְחוּ› (“and-silver repetition take”)
# ‹בְיֶדְכֶם וְאֶת־הַכֶּסֶף הַמּוּשָׁב› (“in-hand-you/your(pl) and-obj-
# marker the-silver the-return”)
# ‹בְּפִי אַמְתְּחֹתֵיכֶם תָּשִׁיבוּ› (“in-mouth something-expansive-
# you/your(pl) return”)
# ‹בְיֶדְכֶם אוּלַי מִשְׁגֶּה› (“in-hand-you/your(pl) if-not error”)
# ‹הוּא› (“he/it”)
# "[EN-AID] And double silver take in your hand; and the silver that was
# returned in the mouth of your bags return in your hand — perhaps it was an
# error."
m.step("Gen.43.12")
# ‹וְכֶסֶף מִשְׁנֶה קְחוּ› (“and-silver repetition take”)
# ‹בְיֶדְכֶם› (“in-hand-you/your(pl)”)
# — fact holds: silver-repetition-and-the-silver-the-return
m.fact("kesef_mishne_ve_ha_kesef_ha_mushav")

# -------------------------- Gen.43.13 · TAKE_YOUR_BROTHER_ARISE_RETURN -----
# ‹וְאֶת־אֲחִיכֶם קָחוּ וְקוּמוּ› (“and-obj-marker brother-you/your(pl) take
# and-arise”)
# ‹שׁוּבוּ אֶל־הָאִישׁ› (“return to the-man”)
# "[EN-AID] And your brother take; and arise, return to the man."
m.step("Gen.43.13")
# ‹וְאֶת־אֲחִיכֶם קָחוּ וְקוּמוּ› (“and-obj-marker brother-you/your(pl) take
# and-arise”)
# ‹שׁוּבוּ› (“return”)
# — fact holds: and-obj-marker-achikhem-take-and-arise-return
m.fact("ve_et_achikhem_qachu_ve_qumu_shuvu")

# -------------------------- Gen.43.14 · EL_SHADDAI_GIVE_YOU_MERCY ----------
# ‹וְאֵל שַׁדַּי יִתֵּן› (“and-strength Almighty set”)
# ‹לָכֶם רַחֲמִים לִפְנֵי› (“to-you/your(pl) compassion to-face”)
# ‹הָאִישׁ וְשִׁלַּח לָכֶם› (“the-man and-send to-you/your(pl)”)
# ‹אֶת־אֲחִיכֶם אַחֵר וְאֶת־בִּנְיָמִין› (“obj-marker brother-you/your(pl)
# other and-obj-marker Benjamin”)
# ‹וַאֲנִי כַּאֲשֶׁר שָׁכֹלְתִּי› (“and-I like-as/which miscarry”)
# ‹שָׁכָלְתִּי› (“miscarry”)
# "[EN-AID] And El Shaddai give you mercy before the man, that he may
# release to you your other brother, and Benjamin. And I — as I am bereaved,
# I am bereaved."
m.step("Gen.43.14")
# ‹וְאֵל שַׁדַּי יִתֵּן› (“and-strength Almighty set”)
# ‹לָכֶם רַחֲמִים› (“to-you/your(pl) compassion”)
# — Israel speaks a demand — LET: to-Almighty-set-lakhem-compassion
m.declare("yisrael", "LET",
          "el_shaday_yiten_lakhem_rachamim")
# witness-tier presupposed read: prayer_sited_where_the_accounting_ends on
# may_god_almighty_give_you_mercy — read, not installed
m.witness_read("may_god_almighty_give_you_mercy", "prayer_sited_where_the_accounting_ends",
                cites=["Bereshit Rabbah 92:2"])
# witness-grounded state (its own tier):
# one_verse_carrying_a_domestic_and_a_national_register on as_i_am_bereaved
m.witness_state("as_i_am_bereaved", "one_verse_carrying_a_domestic_and_a_national_register",
                cites=["Bereshit Rabbah 92:3"])

# -------------------------- Gen.43.15 · THE_CARAVAN_DESCENDS ---------------
# ‹וַיִּקְחוּ הָאֲנָשִׁים אֶת־הַמִּנְחָה› (“and-take the-man obj-marker the-
# grain-offering”)
# ‹הַזֹּאת וּמִשְׁנֶה־כֶּסֶף לָקְחוּ› (“the-this and-repetition silver
# take”)
# ‹בְיָדָם וְאֶת־בִּנְיָמִן וַיָּקֻמוּ› (“in-hand-them/their and-obj-marker
# Benjamin and-arise”)
# ‹וַיֵּרְדוּ מִצְרַיִם וַיַּעַמְדוּ› (“and-go-down Egypt and-stand”)
# ‹לִפְנֵי יוֹסֵף› (“to-face Joseph”)
# "[EN-AID] And the men took this gift, and double silver they took in their
# hand, and Benjamin; and they arose and went down to Egypt, and stood
# before Joseph."
m.step("Gen.43.15")
# ‹וְאֶת־בִּנְיָמִן› (“and-obj-marker Benjamin”)
# — demand settled (popped from the queue): shilcha-the-boy-iti
m.result("shilcha_ha_naar_iti", tmark="t1")
# ‹וַיִּקְחוּ הָאֲנָשִׁים אֶת־הַמִּנְחָה› (“and-take the-man obj-marker the-
# grain-offering”)
# ‹הַזֹּאת וּמִשְׁנֶה־כֶּסֶף לָקְחוּ› (“the-this and-repetition silver
# take”)
# ‹בְיָדָם› (“in-hand-them/their”)
# — demand settled (popped from the queue): this-make-take-and-go-down
m.result("zot_asu_qechu_ve_horidu", tmark="t1")

# -------------------------- Gen.43.16 · SLAUGHTER_AND_PREPARE --------------
# ‹וַיַּרְא יוֹסֵף אִתָּם› (“and-see Joseph with-them/their”)
# ‹אֶת־בִּנְיָמִין וַיֹּאמֶר לַאֲשֶׁר› (“obj-marker Benjamin and-say to-
# which”)
# ‹עַל־בֵּיתוֹ הָבֵא אֶת־הָאֲנָשִׁים› (“over house-him/its come/bring obj-
# marker the-man”)
# ‹הַבָּיְתָה וּטְבֹחַ טֶבַח› (“the-house-ward and-slaughter something-
# slaughtered”)
# ‹וְהָכֵן כִּי אִתִּי› (“and-be-erect that with-me/my”)
# ‹יֹאכְלוּ הָאֲנָשִׁים בַּצָּהֳרָיִם› (“eat the-man in-light”)
# "[EN-AID] And Joseph saw Benjamin with them, and said to the one over his
# house: Bring the men home, and slaughter a slaughtering and prepare — for
# with me the men shall eat at noon."
m.step("Gen.43.16")
# ‹הָבֵא אֶת־הָאֲנָשִׁים הַבָּיְתָה› (“come/bring obj-marker the-man the-
# house-ward”)
# — Joseph speaks a demand — LET: come/bring-obj-marker-the-man-the-baita
m.declare("yosef", "LET",
          "have_et_ha_anashim_ha_baita")
# witness-tier presupposed read: a_sabbath_kept_before_it_was_given on
# slaughter_and_prepare — read, not installed
m.witness_read("slaughter_and_prepare", "a_sabbath_kept_before_it_was_given",
                cites=["Bereshit Rabbah 92:4", "Onkelos Genesis 43:16"])
# witness-tier presupposed read: fitting_slaughter on
# u_tvoach_tevach_ve_hakhen — read, not installed
m.witness_read("u_tvoach_tevach_ve_hakhen", "fitting_slaughter",
                cites=["Chullin 85a:11", "Chullin 85a:12", "Chullin 85a:13"])

# -------------------------- Gen.43.17 · AS_JOSEPH_SAID ---------------------
# ‹וַיַּעַשׂ הָאִישׁ כַּאֲשֶׁר› (“and-make the-man like-as/which”)
# ‹אָמַר יוֹסֵף וַיָּבֵא› (“say Joseph and-come/bring”)
# ‹הָאִישׁ אֶת־הָאֲנָשִׁים בֵּיתָה› (“the-man obj-marker the-man house-
# ward”)
# ‹יוֹסֵף› (“Joseph”)
# "[EN-AID] And the man did as Joseph said; and the man brought the men to
# Joseph's house."
m.step("Gen.43.17")
# ‹וַיַּעַשׂ הָאִישׁ כַּאֲשֶׁר› (“and-make the-man like-as/which”)
# ‹אָמַר יוֹסֵף› (“say Joseph”)
# — demand settled (popped from the queue): come/bring-obj-marker-the-man-
# the-baita
m.result("have_et_ha_anashim_ha_baita", tmark="t2")

# -------------------------- Gen.43.18 · THE_FEAR_AT_THE_DOOR ---------------
# ‹וַיִּירְאוּ הָאֲנָשִׁים כִּי› (“and-fear the-man that”)
# ‹הוּבְאוּ בֵּית יוֹסֵף› (“come/bring house Joseph”)
# ‹וַיֹּאמְרוּ עַל־דְּבַר הַכֶּסֶף› (“and-say over word/thing the-silver”)
# ‹הַשָּׁב בְּאַמְתְּחֹתֵינוּ בַּתְּחִלָּה› (“the-return in-something-
# expansive-us/our in-commencement”)
# ‹אֲנַחְנוּ מוּבָאִים לְהִתְגֹּלֵל› (“we come/bring to-roll”)
# ‹עָלֵינוּ וּלְהִתְנַפֵּל עָלֵינוּ› (“over-us/our and-to-fall over-us/our”)
# ‹וְלָקַחַת אֹתָנוּ לַעֲבָדִים› (“and-to-take obj-marker-us/our to-
# servant”)
# ‹וְאֶת־חֲמֹרֵינוּ› (“and-obj-marker male-ass-us/our”)
# "[EN-AID] And the men feared, for they were brought to Joseph's house; and
# they said: On the matter of the silver returned in our bags at the first
# are we brought — to roll upon us, and to fall upon us, and to take us for
# slaves, and our donkeys."
m.step("Gen.43.18")
# ‹וַיִּירְאוּ הָאֲנָשִׁים כִּי› (“and-fear the-man that”)
# ‹הוּבְאוּ› (“come/bring”)
# — fact holds: and-fear-the-man-that-come/bring
m.fact("va_yiru_ha_anashim_ki_huvu")
# witness-tier presupposed read: resolved_into_domination_and_false_charge
# on to_roll_and_to_fall_upon_us — read, not installed
m.witness_read("to_roll_and_to_fall_upon_us", "resolved_into_domination_and_false_charge",
                cites=["Onkelos Genesis 43:18"])

# -------------------------- Gen.43.19 · AT_THE_DOOR_THEY_DRAW_NEAR ---------
# ‹וַיִּגְּשׁוּ אֶל־הָאִישׁ אֲשֶׁר› (“and-be to the-man which”)
# ‹עַל־בֵּית יוֹסֵף וַיְדַבְּרוּ› (“over house Joseph and-speak”)
# ‹אֵלָיו פֶּתַח הַבָּיִת› (“to-him/its opening the-house”)
# "[EN-AID] And they drew near to the man who was over Joseph's house, and
# spoke to him at the door of the house."
m.step("Gen.43.19")
# ‹וַיִּגְּשׁוּ אֶל־הָאִישׁ› (“and-be to the-man”)
# — fact holds: and-be-to-the-man-opening-the-house
m.fact("va_yigshu_el_ha_ish_petach_ha_bayit")

# -------------------------- Gen.43.20 · WE_SURELY_CAME_DOWN ----------------
# ‹וַיֹּאמְרוּ בִּי אֲדֹנִי› (“and-say oh-that! lord-me/my”)
# ‹יָרֹד יָרַדְנוּ בַּתְּחִלָּה› (“go-down go-down in-commencement”)
# ‹לִשְׁבָּר־אֹכֶל› (“to-deal-in-grain food”)
# "[EN-AID] And they said: Please, my lord — we surely came down at the
# first to buy food."
m.step("Gen.43.20")
# ‹יָרֹד יָרַדְנוּ בַּתְּחִלָּה› (“go-down go-down in-commencement”)
# — fact holds: go-down-go-down-come/bring-techila
m.fact("yarod_yaradnu_ba_techila")

# -------------------------- Gen.43.21 · THE_SILVER_BY_ITS_WEIGHT -----------
# ‹וַיְהִי כִּי־בָאנוּ אֶל־הַמָּלוֹן› (“and-be that come/bring to the-
# lodgment”)
# ‹וַנִּפְתְּחָה אֶת־אַמְתְּחֹתֵינוּ וְהִנֵּה› (“and-open-wide-ward obj-
# marker something-expansive-us/our and-behold”)
# ‹כֶסֶף־אִישׁ בְּפִי אַמְתַּחְתּוֹ› (“silver man in-mouth something-
# expansive-him/its”)
# ‹כַּסְפֵּנוּ בְּמִשְׁקָלוֹ וַנָּשֶׁב› (“silver-us/our in-weight-him/its
# and-return”)
# ‹אֹתוֹ בְּיָדֵנוּ› (“obj-marker-him/its in-hand-us/our”)
# "[EN-AID] And it was, when we came to the lodging place and opened our
# bags — behold, each man's silver in the mouth of his bag, our silver by
# its weight; and we have brought it back in our hand."
m.step("Gen.43.21")
# ‹כַּסְפֵּנוּ בְּמִשְׁקָלוֹ וַנָּשֶׁב› (“silver-us/our in-weight-him/its
# and-return”)
# ‹אֹתוֹ בְּיָדֵנוּ› (“obj-marker-him/its in-hand-us/our”)
# — fact holds: kaspenu-in-mishkalo-and-return-it
m.fact("kaspenu_be_mishkalo_va_nashev_oto")

# -------------------------- Gen.43.22 · OTHER_SILVER_IN_HAND ---------------
# ‹וְכֶסֶף אַחֵר הוֹרַדְנוּ› (“and-silver other go-down”)
# ‹בְיָדֵנוּ לִשְׁבָּר־אֹכֶל לֹא› (“in-hand-us/our to-deal-in-grain food
# not”)
# ‹יָדַעְנוּ מִי־שָׂם כַּסְפֵּנוּ› (“know who? put/set silver-us/our”)
# ‹בְּאַמְתְּחֹתֵינוּ› (“in-something-expansive-us/our”)
# "[EN-AID] And other silver we have brought down in our hand to buy food;
# we do not know who put our silver in our bags."
m.step("Gen.43.22")
# ‹לֹא יָדַעְנוּ מִי־שָׂם› (“not know who? put/set”)
# ‹כַּסְפֵּנוּ בְּאַמְתְּחֹתֵינוּ› (“silver-us/our in-something-expansive-
# us/our”)
# — fact holds: not-know-who?-put/set-kaspenu
m.fact("lo_yadanu_mi_sam_kaspenu")

# -------------------------- Gen.43.23 · YOUR_GOD_GAVE_YOU_TREASURE ---------
# ‹וַיֹּאמֶר שָׁלוֹם לָכֶם› (“and-say safe to-you/your(pl)”)
# ‹אַל־תִּירָאוּ אֱלֹהֵיכֶם וֵאלֹהֵי› (“do-not fear God-you/your(pl) and-
# God”)
# ‹אֲבִיכֶם נָתַן לָכֶם› (“father-you/your(pl) set to-you/your(pl)”)
# ‹מַטְמוֹן בְּאַמְתְּחֹתֵיכֶם כַּסְפְּכֶם› (“secret-storehouse in-
# something-expansive-you/your(pl) silver-you/your(pl)”)
# ‹בָּא אֵלָי וַיּוֹצֵא› (“come/bring to-me/my and-bring-forth”)
# ‹אֲלֵהֶם אֶת־שִׁמְעוֹן› (“to-them/their obj-marker Simeon”)
# "[EN-AID] And he said: Peace to you, fear not; your God and the God of
# your father gave you treasure in your bags — your silver came to me. And
# he brought Simeon out to them."
m.step("Gen.43.23")
# ‹אַל־תִּירָאוּ› (“do-not fear”)
# — man-over-beit-Joseph speaks a demand — LET-NOT: over-fear
m.declare("ish_al_beit_yosef", "LET-NOT",
          "al_tirau")

# -------------------------- Gen.43.24 · WATER_AND_FODDER -------------------
# ‹וַיָּבֵא הָאִישׁ אֶת־הָאֲנָשִׁים› (“and-come/bring the-man obj-marker
# the-man”)
# ‹בֵּיתָה יוֹסֵף וַיִּתֶּן־מַיִם› (“house-ward Joseph and-set waters”)
# ‹וַיִּרְחֲצוּ רַגְלֵיהֶם וַיִּתֵּן› (“and-lave foot-them/their and-set”)
# ‹מִסְפּוֹא לַחֲמֹרֵיהֶם› (“fodder to-male-ass-them/their”)
# "[EN-AID] And the man brought the men into Joseph's house; and he gave
# water, and they washed their feet; and he gave fodder to their donkeys."
m.step("Gen.43.24")
# ‹וַיִּתֶּן־מַיִם וַיִּרְחֲצוּ רַגְלֵיהֶם› (“and-set waters and-lave foot-
# them/their”)
# — fact holds: and-set-waters-and-lave-raglehem
m.fact("va_yiten_mayim_va_yirchatzu_raglehem")

# -------------------------- Gen.43.25 · THE_GIFT_MADE_READY ----------------
# ‹וַיָּכִינוּ אֶת־הַמִּנְחָה עַד־בּוֹא› (“and-be-erect obj-marker the-
# grain-offering until come/bring”)
# ‹יוֹסֵף בַּצָּהֳרָיִם כִּי› (“Joseph in-light that”)
# ‹שָׁמְעוּ כִּי־שָׁם יֹאכְלוּ› (“hear that there eat”)
# ‹לָחֶם› (“food”)
# "[EN-AID] And they made ready the gift against Joseph's coming at noon,
# for they heard that there they should eat bread."
m.step("Gen.43.25")
# ‹וַיָּכִינוּ אֶת־הַמִּנְחָה› (“and-be-erect obj-marker the-grain-
# offering”)
# — fact holds: and-be-erect-obj-marker-the-grain-offering
m.fact("va_yakhinu_et_ha_mincha")

# -------------------------- Gen.43.26 · THE_ELEVEN_BOW ---------------------
# ‹וַיָּבֹא יוֹסֵף הַבַּיְתָה› (“and-come/bring Joseph the-house-ward”)
# ‹וַיָּבִיאּוּ לוֹ אֶת־הַמִּנְחָה› (“and-come/bring to-him/its obj-marker
# the-grain-offering”)
# ‹אֲשֶׁר־בְּיָדָם הַבָּיְתָה וַיִּשְׁתַּחֲווּ־לוֹ› (“which in-hand-
# them/their the-house-ward and-afflict to-him/its”)
# ‹אָרְצָה› (“earth-ward”)
# "[EN-AID] And Joseph came home, and they brought him the gift which was in
# their hand, into the house, and they bowed down to him to the earth."
m.step("Gen.43.26")
# ‹וַיִּשְׁתַּחֲווּ־לוֹ אָרְצָה› (“and-afflict to-him/its earth-ward”)
# — event: hishtachavu — agent the-achim
m.event("hishtachavu", agent="ha_achim")

# -------------------------- Gen.43.27 · IS_YOUR_FATHER_WELL ----------------
# ‹וַיִּשְׁאַל לָהֶם לְשָׁלוֹם› (“and-inquire to-them/their to-safe”)
# ‹וַיֹּאמֶר הֲשָׁלוֹם אֲבִיכֶם› (“and-say the-safe father-you/your(pl)”)
# ‹הַזָּקֵן אֲשֶׁר אֲמַרְתֶּם› (“the-old which say”)
# ‹הַעוֹדֶנּוּ חָי› (“the-still/again-him/its living”)
# "[EN-AID] And he asked them of their welfare, and said: Is your father
# well — the old man of whom you spoke? Is he yet alive?"
m.step("Gen.43.27")
# ‹וַיֹּאמֶר הֲשָׁלוֹם אֲבִיכֶם› (“and-say the-safe father-you/your(pl)”)
# ‹הַזָּקֵן› (“the-old”)
# — fact holds: the-safe-avikhem-the-old
m.fact("ha_shalom_avikhem_ha_zaqen")

# -------------------------- Gen.43.28 · THE_CLIPPED_BOW --------------------
# ‹וַיֹּאמְרוּ שָׁלוֹם לְעַבְדְּךָ› (“and-say safe to-servant-you/your”)
# ‹לְאָבִינוּ עוֹדֶנּוּ חָי› (“to-father-us/our still/again-him/its living”)
# ‹וַיִּקְּדוּ וישתחו וַיִּשְׁתַּחֲוּוּ› (“and-shrivel-up and-afflict and-
# afflict”)
# "[EN-AID] And they said: Your servant our father is well; he is yet alive.
# And they bowed their heads, and prostrated themselves."
m.step("Gen.43.28")
# ‹וַיִּקְּדוּ וישתחו וַיִּשְׁתַּחֲוּוּ› (“and-shrivel-up and-afflict and-
# afflict”)
# — fact holds: and-shrivel-up-and-afflict
m.fact("va_yiqdu_va_yishtachavu")
# witness-grounded state (its own tier):
# the_fifth_seat_and_the_reason_for_almost on your_servant_our_father
m.witness_state("your_servant_our_father", "the_fifth_seat_and_the_reason_for_almost",
                cites=["Bereshit Rabbah 100:3"])

# -------------------------- Gen.43.29 · GOD_BE_GRACIOUS_TO_YOU_MY_SON ------
# ‹וַיִּשָּׂא עֵינָיו וַיַּרְא› (“and-lift/carry eye-him/its and-see”)
# ‹אֶת־בִּנְיָמִין אָחִיו בֶּן־אִמּוֹ› (“obj-marker Benjamin brother-him/its
# son mother-him/its”)
# ‹וַיֹּאמֶר הֲזֶה אֲחִיכֶם› (“and-say the-this brother-you/your(pl)”)
# ‹הַקָּטֹן אֲשֶׁר אֲמַרְתֶּם› (“the-small which say”)
# ‹אֵלָי וַיֹּאמַר אֱלֹהִים› (“to-me/my and-say God”)
# ‹יָחְנְךָ בְּנִי› (“bend-you/your son-me/my”)
# "[EN-AID] And he lifted his eyes and saw Benjamin his brother, his
# mother's son, and said: Is this your youngest brother of whom you spoke to
# me? And he said: God be gracious to you, my son."
m.step("Gen.43.29")
# ‹וַיֹּאמַר אֱלֹהִים יָחְנְךָ› (“and-say God bend-you/your”)
# ‹בְּנִי› (“son-me/my”)
# — blessing: Joseph blesses Benjamin
m.bless("yosef", "binyamin")
# witness-tier presupposed read: a_withheld_grace_paid_by_another_hand on
# god_be_gracious_to_you_my_son — read, not installed
m.witness_read("god_be_gracious_to_you_my_son", "a_withheld_grace_paid_by_another_hand",
                cites=["Bereshit Rabbah 78:10", "Onkelos Genesis 43:29", "Bereshit Rabbah 95:1"])

# -------------------------- Gen.43.30 · THE_CHAMBER_WEEPING ----------------
# ‹וַיְמַהֵר יוֹסֵף כִּי־נִכְמְרוּ› (“and-hasten Joseph that intertwine”)
# ‹רַחֲמָיו אֶל־אָחִיו וַיְבַקֵּשׁ› (“compassion-him/its to brother-him/its
# and-search-out”)
# ‹לִבְכּוֹת וַיָּבֹא הַחַדְרָה› (“to-weep and-come/bring the-apartment-
# ward”)
# ‹וַיֵּבְךְּ שָׁמָּה› (“and-weep there-ward”)
# "[EN-AID] And Joseph hurried — for his compassion grew hot toward his
# brother, and he sought to weep; and he came into the chamber and wept
# there."
m.step("Gen.43.30")
# ‹וַיָּבֹא הַחַדְרָה וַיֵּבְךְּ› (“and-come/bring the-apartment-ward and-
# weep”)
# ‹שָׁמָּה› (“there-ward”)
# — event: bakha — agent Joseph
m.event("bakha", agent="yosef")

# -------------------------- Gen.43.31 · SET_BREAD --------------------------
# ‹וַיִּרְחַץ פָּנָיו וַיֵּצֵא› (“and-lave face-him/its and-bring-forth”)
# ‹וַיִּתְאַפַּק וַיֹּאמֶר שִׂימוּ› (“and-contain and-say put/set”)
# ‹לָחֶם› (“food”)
# "[EN-AID] And he washed his face and went out, and restrained himself, and
# said: Set bread."
m.step("Gen.43.31")
# ‹שִׂימוּ לָחֶם› (“put/set food”)
# — Joseph speaks a demand — LET: put/set-food
m.declare("yosef", "LET",
          "simu_lachem")

# -------------------------- Gen.43.32 · BREAD_SET_APART --------------------
# ‹וַיָּשִׂימוּ לוֹ לְבַדּוֹ› (“and-put/set to-him/its to-separation-
# him/its”)
# ‹וְלָהֶם לְבַדָּם וְלַמִּצְרִים› (“and-to-them/their to-separation-
# them/their and-to-Egyptian”)
# ‹הָאֹכְלִים אִתּוֹ לְבַדָּם› (“the-eat with-him/its to-separation-
# them/their”)
# ‹כִּי לֹא יוּכְלוּן› (“that not be-able-ward”)
# ‹הַמִּצְרִים לֶאֱכֹל אֶת־הָעִבְרִים› (“the-Egyptian to-eat with the-
# Hebrew”)
# ‹לֶחֶם כִּי־תוֹעֵבָה הִוא› (“food that something-disgusting he/it”)
# ‹לְמִצְרָיִם› (“to-Egyptian”)
# "[EN-AID] And they set for him alone, and for them alone, and for the
# Egyptians eating with him alone — for the Egyptians may not eat bread with
# the Hebrews, for it is an abomination to Egypt."
m.step("Gen.43.32")
# ‹וַיָּשִׂימוּ לוֹ לְבַדּוֹ› (“and-put/set to-him/its to-separation-
# him/its”)
# — demand settled (popped from the queue): put/set-food
m.result("simu_lachem", tmark="t3")
# witness-tier presupposed read: the_taboo_explained_rather_than_translated
# on an_abomination_to_the_egyptians — read, not installed
m.witness_read("an_abomination_to_the_egyptians", "the_taboo_explained_rather_than_translated",
                cites=["Onkelos Genesis 43:32"])

# -------------------------- Gen.43.33 · SEATED_BY_BIRTH_ORDER --------------
# ‹וַיֵּשְׁבוּ לְפָנָיו הַבְּכֹר› (“and-dwell/sit to-face-him/its the-
# firstborn”)
# ‹כִּבְכֹרָתוֹ וְהַצָּעִיר כִּצְעִרָתוֹ› (“like-firstling-of-man-him/its
# and-the-little like-smallness-him/its”)
# ‹וַיִּתְמְהוּ הָאֲנָשִׁים אִישׁ› (“and-be-in-consternation the-man man”)
# ‹אֶל־רֵעֵהוּ› (“to associate-him/its”)
# "[EN-AID] And they sat before him, the firstborn according to his
# birthright and the youngest according to his youth; and the men wondered,
# each to his fellow."
m.step("Gen.43.33")
# ‹הַבְּכֹר כִּבְכֹרָתוֹ וְהַצָּעִיר› (“the-firstborn like-firstling-of-man-
# him/its and-the-little”)
# ‹כִּצְעִרָתוֹ› (“like-smallness-him/its”)
# — fact holds: the-firstborn-that-vkhorato-and-the-little-that-tzeirato
m.fact("ha_bekhor_ki_vkhorato_ve_ha_tzair_ki_tzeirato")
# witness-tier presupposed read: the_duel_already_under_way on
# the_men_looked_at_one_another — read, not installed
m.witness_read("the_men_looked_at_one_another", "the_duel_already_under_way",
                cites=["Bereshit Rabbah 93:2", "Onkelos Genesis 43:33", "Bereshit Rabbah 92:5"])

# -------------------------- Gen.43.34 · FIVE_HANDS -------------------------
# ‹וַיִּשָּׂא מַשְׂאֹת מֵאֵת› (“and-lift/carry raising from-with”)
# ‹פָּנָיו אֲלֵהֶם וַתֵּרֶב› (“face-him/its to-them/their and-multiply”)
# ‹מַשְׂאַת בִּנְיָמִן מִמַּשְׂאֹת› (“raising Benjamin from-raising”)
# ‹כֻּלָּם חָמֵשׁ יָדוֹת› (“all-them/their five hand”)
# ‹וַיִּשְׁתּוּ וַיִּשְׁכְּרוּ עִמּוֹ› (“and-drink and-become-tipsy with-
# him/its”)
# "[EN-AID] And he lifted portions from before his face to them; and
# Benjamin's portion was greater than the portions of them all — five hands.
# And they drank, and drank freely with him."
m.step("Gen.43.34")
# ‹וַתֵּרֶב מַשְׂאַת בִּנְיָמִן› (“and-multiply raising Benjamin”)
# ‹מִמַּשְׂאֹת כֻּלָּם› (“from-raising all-them/their”)
# — fact holds: and-multiply-raising-Benjamin-five-hand
m.fact("va_terev_masat_binyamin_chamesh_yadot")
# witness-grounded state (its own tier):
# twenty_two_years_hanging_on_one_suffix on they_drank_with_him
m.witness_state("they_drank_with_him", "twenty_two_years_hanging_on_one_suffix",
                cites=["Bereshit Rabbah 98:20", "Bereshit Rabbah 92:5"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shuvu_shivru_lanu_meat_okhel', 'el_shaday_yiten_lakhem_rachamim', 'al_tirau']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_ha_raav_kaved_ba_aretz', 'haed_heid_banu_ha_ish', 'im_yeshkha_meshaleach_nerda', 've_im_enkha_meshaleach_lo_nered', 'lama_hareotem_li_lehagid', 'shaol_shaal_ha_ish_lanu', 'anokhi_eervenu_mi_yadi_tevaqshenu', 'ki_lule_hitmahmahnu', 'kesef_mishne_ve_ha_kesef_ha_mushav', 've_et_achikhem_qachu_ve_qumu_shuvu', 'va_yiru_ha_anashim_ki_huvu', 'va_yigshu_el_ha_ish_petach_ha_bayit', 'yarod_yaradnu_ba_techila', 'kaspenu_be_mishkalo_va_nashev_oto', 'lo_yadanu_mi_sam_kaspenu', 'va_yiten_mayim_va_yirchatzu_raglehem', 'va_yakhinu_et_ha_mincha', 'ha_shalom_avikhem_ha_zaqen', 'va_yiqdu_va_yishtachavu', 'ha_bekhor_ki_vkhorato_ve_ha_tzair_ki_tzeirato', 'va_terev_masat_binyamin_chamesh_yadot'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    assert sorted(m.WORLD["witnessed"]) == ['as_i_am_bereaved', 'had_we_not_delayed', 'if_so_then_do_this', 'they_drank_with_him', 'your_servant_our_father']
    assert m.WORLD["witnessed"]['as_i_am_bereaved']["cites"] == ['Bereshit Rabbah 92:3']
    assert all('one_verse_carrying_a_domestic_and_a_national_register' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['had_we_not_delayed']["cites"] == ['Bereshit Rabbah 74:12']
    assert all('a_standing_rule_meeting_its_own_objection' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['if_so_then_do_this']["cites"] == ['Bereshit Rabbah 91:11']
    assert all('the_particle_that_wires_deception_to_repayment' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['they_drank_with_him']["cites"] == ['Bereshit Rabbah 98:20', 'Bereshit Rabbah 92:5']
    assert all('twenty_two_years_hanging_on_one_suffix' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['your_servant_our_father']["cites"] == ['Bereshit Rabbah 100:3']
    assert all('the_fifth_seat_and_the_reason_for_almost' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_famine_was_severe', 'an_enumerated_member_of_the_paved_way'), ('judahs_pledge', 'read_clause_by_clause_through_a_proverb'), ('anokhi_eervenu', 'surety_root'), ('ve_chatati_kol_ha_yamim', 'conditional_ban'), ('may_god_almighty_give_you_mercy', 'prayer_sited_where_the_accounting_ends'), ('slaughter_and_prepare', 'a_sabbath_kept_before_it_was_given'), ('u_tvoach_tevach_ve_hakhen', 'fitting_slaughter'), ('to_roll_and_to_fall_upon_us', 'resolved_into_domination_and_false_charge'), ('god_be_gracious_to_you_my_son', 'a_withheld_grace_paid_by_another_hand'), ('an_abomination_to_the_egyptians', 'the_taboo_explained_rather_than_translated'), ('the_men_looked_at_one_another', 'the_duel_already_under_way')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 40:6']
    assert all('an_enumerated_member_of_the_paved_way' not in f for f in m.WORLD["facts"])
    assert 'the_famine_was_severe' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 93:1', 'Onkelos Genesis 43:9']
    assert all('read_clause_by_clause_through_a_proverb' not in f for f in m.WORLD["facts"])
    assert 'judahs_pledge' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bava Batra 173b:8', 'Bava Batra 173b:9', 'Bava Batra 173b:10', 'Bava Batra 173b:11']
    assert all('surety_root' not in f for f in m.WORLD["facts"])
    assert 'anokhi_eervenu' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Makkot 11b:1', 'Makkot 11b:2']
    assert all('conditional_ban' not in f for f in m.WORLD["facts"])
    assert 've_chatati_kol_ha_yamim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 92:2']
    assert all('prayer_sited_where_the_accounting_ends' not in f for f in m.WORLD["facts"])
    assert 'may_god_almighty_give_you_mercy' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 92:4', 'Onkelos Genesis 43:16']
    assert all('a_sabbath_kept_before_it_was_given' not in f for f in m.WORLD["facts"])
    assert 'slaughter_and_prepare' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Chullin 85a:11', 'Chullin 85a:12', 'Chullin 85a:13']
    assert all('fitting_slaughter' not in f for f in m.WORLD["facts"])
    assert 'u_tvoach_tevach_ve_hakhen' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Genesis 43:18']
    assert all('resolved_into_domination_and_false_charge' not in f for f in m.WORLD["facts"])
    assert 'to_roll_and_to_fall_upon_us' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 78:10', 'Onkelos Genesis 43:29', 'Bereshit Rabbah 95:1']
    assert all('a_withheld_grace_paid_by_another_hand' not in f for f in m.WORLD["facts"])
    assert 'god_be_gracious_to_you_my_son' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 43:32']
    assert all('the_taboo_explained_rather_than_translated' not in f for f in m.WORLD["facts"])
    assert 'an_abomination_to_the_egyptians' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 93:2', 'Onkelos Genesis 43:33', 'Bereshit Rabbah 92:5']
    assert all('the_duel_already_under_way' not in f for f in m.WORLD["facts"])
    assert 'the_men_looked_at_one_another' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
