#!/usr/bin/env python3
# =============================================================================
# gen_46_isaac_blessing_demandee_mismatch — 27:1-40
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_46_isaac_blessing_demandee_mismatch.yaml) is
# CANONICAL (Pre-Code); this file is a derived, runnable rendering. Do not
# edit — regenerate. The assertion block at the bottom is baked from the
# Stage D interpreter's actual final state: running this file re-proves the
# unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Isaac's hunt-command and the blessing — demandee-mismatch machine (27:1-40)"""
from machine import Machine

m = Machine("gen_46_isaac_blessing_demandee_mismatch")

# -------------------------- Gen.27.1 · THE_AGE_DIM_AND_CALL_ESAU -----------
# ‹וַיְהִי כִּי־זָקֵן יִצְחָק› (“and-be that be-old Isaac”)
# ‹וַתִּכְהֶיןָ עֵינָיו מֵרְאֹת› (“and-be-weak eye-him/its from-see”)
# ‹וַיִּקְרָא אֶת־עֵשָׂו בְּנוֹ› (“and-call obj-marker Esau son-him/its”)
# ‹הַגָּדֹל וַיֹּאמֶר אֵלָיו› (“the-great and-say to-him/its”)
# ‹בְּנִי וַיֹּאמֶר אֵלָיו› (“son-me/my and-say to-him/its”)
# ‹הִנֵּנִי› (“behold-me/my”)
# "[EN-AID] And it came to pass that Isaac was old, and his eyes were dim
# from seeing; and he called Esau his great son and said to him, My son; and
# he said to him, Here I am."
m.step("Gen.27.1")
# ‹זָקֵן יִצְחָק … עֵינָיו› (“be-old Isaac … eye-him/its”)
# ‹מֵרְאֹת … עֵשָׂו בְּנוֹ› (“from-see … Esau son-him/its”)
# ‹הַגָּדֹל› (“the-great”)
# — fact holds: Isaac-old-eyes-dim; Esau-called-as-great-son
m.fact("yitzchaq_old_eyes_dim",
       "esav_called_as_great_son")
# witness-grounded state (its own tier):
# one_leg_exact_one_false_one_uncheckable on three_demands_ladder
m.witness_state("three_demands_ladder", "one_leg_exact_one_false_one_uncheckable",
                cites=["Bereshit Rabbah 65:9"])
# witness-tier presupposed read: four_incompatible_causes_all_kept on
# the_dimmed_eyes — read, not installed
m.witness_read("the_dimmed_eyes", "four_incompatible_causes_all_kept",
                cites=["Bereshit Rabbah 65:5", "Bereshit Rabbah 65:8", "Bereshit Rabbah 65:10"])

# -------------------------- Gen.27.2 · THE_DEATH_DAY_UNKNOWN ---------------
# ‹וַיֹּאמֶר הִנֵּה־נָא זָקַנְתִּי› (“and-say behold please be-old”)
# ‹לֹא יָדַעְתִּי יוֹם› (“not know day”)
# ‹מוֹתִי› (“death-me/my”)
# "[EN-AID] And he said: Behold, please, I am old; I do not know the day of
# my death."
m.step("Gen.27.2")
# ‹זָקַנְתִּי … לֹא יָדַעְתִּי› (“be-old … not know”)
# ‹יוֹם מוֹתִי› (“day death-me/my”)
# — fact holds: Isaac-does-not-know-death-day
m.fact("yitzchaq_does_not_know_death_day")
# witness-tier presupposed read:
# death_anxiety_rule_with_an_arithmetic_trigger on i_know_not_my_day — read,
# not installed
m.witness_read("i_know_not_my_day", "death_anxiety_rule_with_an_arithmetic_trigger",
                cites=["Bereshit Rabbah 65:12"])

# -------------------------- Gen.27.3 · THE_HUNT_CHAIN_OPENS ----------------
# ‹וְעַתָּה שָׂא־נָא כֵלֶיךָ› (“and-now lift/carry please vessel-you/your”)
# ‹תֶּלְיְךָ וְקַשְׁתֶּךָ וְצֵא› (“quiver-you/your and-bow-you/your and-
# bring-forth”)
# ‹הַשָּׂדֶה וְצוּדָה לִּי› (“the-field and-lie-alongside-ward to-me/my”)
# ‹צָיִד› (“food”)
# "[EN-AID] And now, please take your gear, your quiver and your bow, and go
# out to the field and hunt game for me."
m.step("Gen.27.3")
# ‹שָׂא … וְצֵא … וְצוּדָה› (“lift/carry … and-bring-forth … and-lie-
# alongside-ward”)
# — fact holds: hunt-chain-opening-volitives-on-Esau
m.fact("hunt_chain_opening_volitives_on_esav")

# -------------------------- Gen.27.4 · THE_COMPOUND_HUNT_MEAL_ON_ESAU ------
# ‹וַעֲשֵׂה־לִי מַטְעַמִּים כַּאֲשֶׁר› (“and-make to-me/my delicacy like-
# as/which”)
# ‹אָהַבְתִּי וְהָבִיאָה לִּי› (“have-affection-for and-come/bring-ward to-
# me/my”)
# ‹וְאֹכֵלָה בַּעֲבוּר תְּבָרֶכְךָ› (“and-eat for-the-sake-of bless-
# you/your”)
# ‹נַפְשִׁי בְּטֶרֶם אָמוּת› (“living-being-me/my in-non-occurrence die”)
# "[EN-AID] And make me delicacies such as I love, and bring them to me,
# that I may eat, so that my soul may bless you before I die."
m.step("Gen.27.4")
# ‹שָׂא … וְצֵא … וְצוּדָה› (“lift/carry … and-bring-forth … and-lie-
# alongside-ward”)
# ‹… וַעֲשֵׂה … וְהָבִיאָה› (“and-make … and-come/bring-ward”)
# — Isaac speaks a demand — LET: lift/carry-bring-forth-tzuda-make-
# havia(Esau)
m.declare("yitzchaq", "LET",
          "sa_tze_tzuda_ase_havia(esav)")

# -------------------------- Gen.27.5 · THE_OVERHEAR_AND_ESAU_GOES ----------
# ‹וְרִבְקָה שֹׁמַעַת בְּדַבֵּר› (“and-Rebekah hear in-speak”)
# ‹יִצְחָק אֶל־עֵשָׂו בְּנוֹ› (“Isaac to Esau son-him/its”)
# ‹וַיֵּלֶךְ עֵשָׂו הַשָּׂדֶה› (“and-go Esau the-field”)
# ‹לָצוּד צַיִד לְהָבִיא› (“to-lie-alongside chase to-come/bring”)
# "[EN-AID] And Rivqah was listening as Isaac spoke to Esau his son; and
# Esau went to the field to hunt game to bring."
m.step("Gen.27.5")
# ‹שֹׁמַעַת … וַיֵּלֶךְ … לָצוּד› (“hear … and-go … to-lie-alongside”)
# ‹צַיִד› (“chase”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.6 · THE_FENCE_OPENS_TO_JACOB ------------
# ‹וְרִבְקָה אָמְרָה אֶל־יַעֲקֹב› (“and-Rebekah say to Jacob”)
# ‹בְּנָהּ לֵאמֹר הִנֵּה› (“son-her/its to-say behold”)
# ‹שָׁמַעְתִּי אֶת־אָבִיךָ מְדַבֵּר› (“hear obj-marker father-you/your
# speak”)
# ‹אֶל־עֵשָׂו אָחִיךָ לֵאמֹר› (“to Esau brother-you/your to-say”)
# "[EN-AID] And Rivqah said to Jacob her son, saying: Behold, I heard your
# father speaking to Esau your brother, saying:"
m.step("Gen.27.6")
# ‹אָמְרָה אֶל־יַעֲקֹב … שָׁמַעְתִּי› (“say to Jacob … hear”)
# ‹אֶת־אָבִיךָ מְדַבֵּר אֶל־עֵשָׂו› (“obj-marker father-you/your speak to
# Esau”)
# — fact holds: retelling-fence-open-rivqah-to-Jacob
m.fact("retelling_fence_open_rivqah_to_yaaqov")

# -------------------------- Gen.27.7 · THE_REPORT_DELTA_BEFORE_YHWH --------
# ‹הָבִיאָה לִּי צַיִד› (“come/bring-ward to-me/my chase”)
# ‹וַעֲשֵׂה־לִי מַטְעַמִּים וְאֹכֵלָה› (“and-make to-me/my delicacy and-
# eat”)
# ‹וַאֲבָרֶכְכָה לִפְנֵי יְהוָה› (“and-bless-you/your to-face YHWH”)
# ‹לִפְנֵי מוֹתִי› (“to-face death-me/my”)
# "[EN-AID] Bring me game and make me delicacies, that I may eat, and I will
# bless you before YHWH before my death."
m.step("Gen.27.7")
# ‹הָבִיאָה … וַעֲשֵׂה … וְאֹכֵלָה› (“come/bring-ward … and-make … and-eat”)
# ‹… וַאֲבָרֶכְכָה לִפְנֵי יְהוָה› (“and-bless-you/your to-face YHWH”)
# — fact holds: retold-isaac-speech-with-delta
m.fact("retold_isaac_speech_with_delta")

# -------------------------- Gen.27.8 · THE_SHEMA_BE_QOLI_ON_JACOB ----------
# ‹וְעַתָּה בְנִי שְׁמַע› (“and-now son-me/my hear”)
# ‹בְּקֹלִי לַאֲשֶׁר אֲנִי› (“in-voice/sound-me/my to-which”)
# ‹מְצַוָּה אֹתָךְ› (“command obj-marker-you/your”)
# "[EN-AID] And now, my son, listen to my voice, to what I am commanding
# you."
m.step("Gen.27.8")
# ‹שְׁמַע בְּקֹלִי› (“hear in-voice/sound-me/my”)
# — rivqah speaks a demand — LET: hear-in-qoli(Jacob)
m.declare("rivqah", "LET",
          "shema_be_qoli(yaaqov)")

# -------------------------- Gen.27.9 · THE_LEKH_QACH_COMPOUND_ON_JACOB -----
# ‹לֶךְ־נָא אֶל־הַצֹּאן וְקַח־לִי› (“go please to the-flock and-take to-
# me/my”)
# ‹מִשָּׁם שְׁנֵי גְּדָיֵי› (“from-there two young-goat”)
# ‹עִזִּים טֹבִים וְאֶעֱשֶׂה› (“she-goat good and-make”)
# ‹אֹתָם מַטְעַמִּים לְאָבִיךָ› (“obj-marker-them/their delicacy to-father-
# you/your”)
# ‹כַּאֲשֶׁר אָהֵב› (“like-as/which have-affection-for”)
# "[EN-AID] Go now to the flock and take for me from there two good kids of
# the goats, and I will make them delicacies for your father as he loves."
m.step("Gen.27.9")
# ‹לֶךְ … וְקַח› (“go … and-take”)
# — rivqah speaks a demand — LET: go-take-come/bring(Jacob)
m.declare("rivqah", "LET",
          "lekh_qach_heveta(yaaqov)")
# ‹גְּדָיֵי עִזִּים טֹבִים› (“young-goat she-goat good”)
# ‹… וְאֶעֱשֶׂה … כַּאֲשֶׁר אָהֵב› (“and-make … like-as/which have-
# affection-for”)
# — fact holds: good-attribute-fenced-kids; rivqah-will-make-delicacy
m.fact("tovim_attribute_fenced_kids",
       "rivqah_will_make_matamim")
# witness-tier presupposed read:
# licensed_by_a_marriage_contract_and_typologized_to_the_rite on two_kids —
# read, not installed
m.witness_read("two_kids", "licensed_by_a_marriage_contract_and_typologized_to_the_rite",
                cites=["Bereshit Rabbah 65:14"])

# -------------------------- Gen.27.10 · THE_WEQATAL_DUTY_AND_BLESS_CONTENT -
# ‹וְהֵבֵאתָ לְאָבִיךָ וְאָכָל› (“and-come/bring to-father-you/your and-
# eat”)
# ‹בַּעֲבֻר אֲשֶׁר יְבָרֶכְךָ› (“for-the-sake-of which bless-you/your”)
# ‹לִפְנֵי מוֹתוֹ› (“to-face death-him/its”)
# "[EN-AID] And you shall bring it to your father, and he will eat, so that
# he may bless you before his death."
m.step("Gen.27.10")
# ‹וְהֵבֵאתָ … וְאָכָל … יְבָרֶכְךָ› (“and-come/bring … and-eat … bless-
# you/your”)
# ‹לִפְנֵי מוֹתוֹ› (“to-face death-him/its”)
# — fact holds: weqatal-come/bring-third-member-fowl-go-take-compound
m.fact("weqatal_heveta_third_member_of_lekh_qach_compound")

# -------------------------- Gen.27.11 · THE_HAIRY_VS_SMOOTH_OBJECTION ------
# ‹וַיֹּאמֶר יַעֲקֹב אֶל־רִבְקָה› (“and-say Jacob to Rebekah”)
# ‹אִמּוֹ הֵן עֵשָׂו› (“mother-him/its lo! Esau”)
# ‹אָחִי אִישׁ שָׂעִר› (“brother-me/my man shaggy”)
# ‹וְאָנֹכִי אִישׁ חָלָק› (“and-I man smooth”)
# "[EN-AID] And Jacob said to Rivqah his mother: Behold, Esau my brother is
# a hairy man, and I am a smooth man."
m.step("Gen.27.11")
# ‹אִישׁ שָׂעִר … אִישׁ› (“man shaggy … man”)
# ‹חָלָק› (“smooth”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.12 · THE_ULAY_FEEL_CURSE_FRAME ----------
# ‹אוּלַי יְמֻשֵּׁנִי אָבִי› (“if-not feel-of-me/my father-me/my”)
# ‹וְהָיִיתִי בְעֵינָיו כִּמְתַעְתֵּעַ› (“and-be in-eye-him/its like-cheat”)
# ‹וְהֵבֵאתִי עָלַי קְלָלָה› (“and-come/bring over-me/my vilification”)
# ‹וְלֹא בְרָכָה› (“and-not blessing”)
# "[EN-AID] Perhaps my father will feel me, and I shall be in his eyes as a
# mocker, and I shall bring on myself a curse and not a blessing."
m.step("Gen.27.12")
# ‹אוּלַי יְמֻשֵּׁנִי … כִּמְתַעְתֵּעַ› (“if-not feel-of-me/my … like-
# cheat”)
# ‹… קְלָלָה וְלֹא בְרָכָה› (“vilification and-not blessing”)
# — fact holds: if-not-hypothetical-feel-curse-not-blessing
m.fact("ulay_hypothetical_feel_curse_not_blessing")

# -------------------------- Gen.27.13 · THE_CURSE_ABSORPTION_AND_REISSUE ---
# ‹וַתֹּאמֶר לוֹ אִמּוֹ› (“and-say to-him/its mother-him/its”)
# ‹עָלַי קִלְלָתְךָ בְּנִי› (“over-me/my vilification-you/your son-me/my”)
# ‹אַךְ שְׁמַע בְּקֹלִי› (“indeed hear in-voice/sound-me/my”)
# ‹וְלֵךְ קַח־לִי› (“and-go take to-me/my”)
# "[EN-AID] And his mother said to him: Upon me be your curse, my son; only
# listen to my voice, and go, take for me."
m.step("Gen.27.13")
# ‹עָלַי קִלְלָתְךָ בְּנִי› (“over-me/my vilification-you/your son-me/my”)
# — fact holds: curse-transfer-speech-alai-qillat-you/your
m.fact("curse_transfer_speech_alai_qillat_kha")
# ‹אַךְ שְׁמַע בְּקֹלִי› (“indeed hear in-voice/sound-me/my”)
# ‹וְלֵךְ קַח› (“and-go take”)
# — fact holds: reissue-hear-and-go-take-same-stack
m.fact("reissue_shema_and_lekh_qach_same_stack")
# witness-tier presupposed read: replaced_by_a_prophecy_licence on
# the_self_curse — read, not installed
m.witness_read("the_self_curse", "replaced_by_a_prophecy_licence",
                cites=["Bereshit Rabbah 65:6", "Onkelos Genesis 27:13"])

# -------------------------- Gen.27.14 · THE_POP_WEIGH_THREE_ROOT_TO_MOTHER -
# ‹וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא› (“and-go and-take and-come/bring”)
# ‹לְאִמּוֹ וַתַּעַשׂ אִמּוֹ› (“to-mother-him/its and-make mother-him/its”)
# ‹מַטְעַמִּים כַּאֲשֶׁר אָהֵב› (“delicacy like-as/which have-affection-
# for”)
# ‹אָבִיו› (“father-him/its”)
# "[EN-AID] And he went and took and brought to his mother; and his mother
# made delicacies as his father loves."
m.step("Gen.27.14")
# ‹וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא› (“and-go and-take and-come/bring”)
# ‹לְאִמּוֹ› (“to-mother-him/its”)
# — event: ?
m.event("?")
# ‹וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא› (“and-go and-take and-come/bring”)
# ‹לְאִמּוֹ› (“to-mother-him/its”)
# — fact holds: go-take-come/bring-still-OPEN-object-mismatch
m.fact("lekh_qach_heveta_still_OPEN_object_mismatch")
# ‹וַתַּעַשׂ אִמּוֹ מַטְעַמִּים› (“and-make mother-him/its delicacy”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.15 · THE_DRESS_SMALL_AS_GREAT -----------
# ‹וַתִּקַּח רִבְקָה אֶת־בִּגְדֵי› (“and-take Rebekah obj-marker garment”)
# ‹עֵשָׂו בְּנָהּ הַגָּדֹל› (“Esau son-her/its the-great”)
# ‹הַחֲמֻדֹת אֲשֶׁר אִתָּהּ› (“the-delight which with-her/its”)
# ‹בַּבָּיִת וַתַּלְבֵּשׁ אֶת־יַעֲקֹב› (“in-house and-wrap-around obj-marker
# Jacob”)
# ‹בְּנָהּ הַקָּטָן› (“son-her/its the-abbreviated”)
# "[EN-AID] And Rivqah took the garments of Esau her great son, the precious
# ones that were with her in the house, and clothed Jacob her small son."
m.step("Gen.27.15")
# ‹בִּגְדֵי עֵשָׂו … הַגָּדֹל› (“garment Esau … the-great”)
# ‹… וַתַּלְבֵּשׁ … הַקָּטָן› (“and-wrap-around … the-abbreviated”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.16 · THE_SKINS_ON_HANDS_AND_NECK --------
# ‹וְאֵת עֹרֹת גְּדָיֵי› (“and-obj-marker skin young-goat”)
# ‹הָעִזִּים הִלְבִּישָׁה עַל־יָדָיו› (“the-she-goat wrap-around over hand-
# him/its”)
# ‹וְעַל חֶלְקַת צַוָּארָיו› (“and-over smoothness back-of-the-neck-
# him/its”)
# "[EN-AID] And the skins of the kids of the goats she put on his hands and
# on the smooth of his neck."
m.step("Gen.27.16")
# ‹עֹרֹת … הִלְבִּישָׁה עַל־יָדָיו› (“skin … wrap-around over hand-him/its”)
# ‹… חֶלְקַת צַוָּארָיו› (“smoothness back-of-the-neck-him/its”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.17 · THE_HANDOFF_INTO_JACOBS_HAND -------
# ‹וַתִּתֵּן אֶת־הַמַּטְעַמִּים וְאֶת־הַלֶּחֶם› (“and-set obj-marker the-
# delicacy and-obj-marker the-food”)
# ‹אֲשֶׁר עָשָׂתָה בְּיַד› (“which make in-hand”)
# ‹יַעֲקֹב בְּנָהּ› (“Jacob son-her/its”)
# "[EN-AID] And she gave the delicacies and the bread that she had made into
# the hand of Jacob her son."
m.step("Gen.27.17")
# ‹וַתִּתֵּן … בְּיַד יַעֲקֹב› (“and-set … in-hand Jacob”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.18 · THE_QAL_ARRIVAL_AND_WHO_ARE_YOU ----
# ‹וַיָּבֹא אֶל־אָבִיו וַיֹּאמֶר› (“and-come/bring to father-him/its and-
# say”)
# ‹אָבִי וַיֹּאמֶר הִנֶּנִּי› (“father-me/my and-say behold-me/my”)
# ‹מִי אַתָּה בְּנִי› (“who? you son-me/my”)
# "[EN-AID] And he came to his father and said, My father; and he said, Here
# I am; who are you, my son?"
m.step("Gen.27.18")
# ‹וַיָּבֹא … מִי אַתָּה› (“and-come/bring … who? you”)
# ‹בְּנִי› (“son-me/my”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.19 · THE_FALSE_IDENTITY_AND_QUM_COMPOUND -
# ‹וַיֹּאמֶר יַעֲקֹב אֶל־אָבִיו› (“and-say Jacob to father-him/its”)
# ‹אָנֹכִי עֵשָׂו בְּכֹרֶךָ› (“Esau firstborn-you/your”)
# ‹עָשִׂיתִי כַּאֲשֶׁר דִּבַּרְתָּ› (“make like-as/which speak”)
# ‹אֵלָי קוּם־נָא שְׁבָה› (“to-me/my arise please dwell/sit-ward”)
# ‹וְאָכְלָה מִצֵּידִי בַּעֲבוּר› (“and-eat-ward from-chase-me/my for-the-
# sake-of”)
# ‹תְּבָרֲכַנִּי נַפְשֶׁךָ› (“bless-me/my living-being-you/your”)
# "[EN-AID] And Jacob said to his father: I am Esau your firstborn; I have
# done as you spoke to me; arise please, sit, and eat of my hunt, so that
# your soul may bless me."
m.step("Gen.27.19")
# ‹אָנֹכִי עֵשָׂו בְּכֹרֶךָ› (“Esau firstborn-you/your”)
# ‹… עָשִׂיתִי› (“make”)
# — fact holds: spoken-claim-I-Esau-bekhore-you/your
m.fact("spoken_claim_anokhi_esav_bekhore_kha")
# ‹קוּם … שְׁבָה … וְאָכְלָה› (“arise … dwell/sit-ward … and-eat-ward”)
# — Jacob speaks a demand — LET: arise-seven-akhla(Isaac)
m.declare("yaaqov", "LET",
          "qum_sheva_akhla(yitzchaq)")
# witness-tier presupposed read:
# equivocation_defence_declined_by_the_other_member on
# i_am_esau_your_firstborn — read, not installed
m.witness_read("i_am_esau_your_firstborn", "equivocation_defence_declined_by_the_other_member",
                cites=["Bereshit Rabbah 65:18", "Onkelos Genesis 27:19", "Onkelos Genesis 27:24"])

# -------------------------- Gen.27.20 · THE_YHWH_ELOHEKHA_AND_HIQRA_DEBUTS -
# ‹וַיֹּאמֶר יִצְחָק אֶל־בְּנוֹ› (“and-say Isaac to son-him/its”)
# ‹מַה־זֶּה מִהַרְתָּ לִמְצֹא› (“what this hasten to-find”)
# ‹בְּנִי וַיֹּאמֶר כִּי› (“son-me/my and-say that”)
# ‹הִקְרָה יְהוָה אֱלֹהֶיךָ› (“light-upon YHWH God-you/your”)
# ‹לְפָנָי› (“to-face-me/my”)
# "[EN-AID] And Isaac said to his son: How is it that you found so quickly,
# my son? And he said: Because YHWH your God made it happen before me."
m.step("Gen.27.20")
# ‹הִקְרָה יְהוָה אֱלֹהֶיךָ› (“light-upon YHWH God-you/your”)
# ‹לְפָנָי› (“to-face-me/my”)
# — fact holds: spoken-light-upon-the-LORD-elohekha-before-Me
m.fact("spoken_hiqra_YHWH_elohekha_lefanai")

# -------------------------- Gen.27.21 · THE_GESHA_PUSH_AND_FEEL_HAPAX ------
# ‹וַיֹּאמֶר יִצְחָק אֶל־יַעֲקֹב› (“and-say Isaac to Jacob”)
# ‹גְּשָׁה־נָּא וַאֲמֻשְׁךָ בְּנִי› (“be-ward please and-touch-you/your son-
# me/my”)
# ‹הַאַתָּה זֶה בְּנִי› (“the-you this son-me/my”)
# ‹עֵשָׂו אִם־לֹא› (“Esau if not”)
# "[EN-AID] And Isaac said to Jacob: Draw near please, that I may feel you,
# my son; are you this my son Esau or not?"
m.step("Gen.27.21")
# ‹גְּשָׁה נָּא› (“be-ward please”)
# — Isaac speaks a demand — LET: gesha(Jacob)
m.declare("yitzchaq", "LET",
          "gesha(yaaqov)")

# -------------------------- Gen.27.22 · THE_GESHA_POP_AND_VOICE_HANDS_VERDICT -
# ‹וַיִּגַּשׁ יַעֲקֹב אֶל־יִצְחָק› (“and-be Jacob to Isaac”)
# ‹אָבִיו וַיְמֻשֵּׁהוּ וַיֹּאמֶר› (“father-him/its and-feel-of-him/its and-
# say”)
# ‹הַקֹּל קוֹל יַעֲקֹב› (“the-voice/sound voice/sound Jacob”)
# ‹וְהַיָּדַיִם יְדֵי עֵשָׂו› (“and-the-hand hand Esau”)
# "[EN-AID] And Jacob drew near to Isaac his father, and he felt him; and he
# said: The voice is Jacob's voice, but the hands are Esau's hands."
m.step("Gen.27.22")
# ‹וַיִּגַּשׁ יַעֲקֹב› (“and-be Jacob”)
# — demand settled (popped from the queue): gesha(Jacob)
m.result("gesha(yaaqov)", tmark="t1")
# ‹וַיְמֻשֵּׁהוּ … הַקֹּל קוֹל› (“and-feel-of-him/its … the-voice/sound
# voice/sound”)
# ‹יַעֲקֹב וְהַיָּדַיִם יְדֵי› (“Jacob and-the-hand hand”)
# ‹עֵשָׂו› (“Esau”)
# — event: ?
m.event("?")
# witness-grounded state (its own tier):
# dominance_mechanism_with_an_explicit_toggle on voice_and_hands
m.witness_state("voice_and_hands", "dominance_mechanism_with_an_explicit_toggle",
                cites=["Bereshit Rabbah 65:20", "Bereshit Rabbah 65:21"])

# -------------------------- Gen.27.23 · THE_NAKAR_DEBUT_AND_FIRST_BLESS_EVENT -
# ‹וְלֹא הִכִּירוֹ כִּי־הָיוּ› (“and-not scrutinize-him/its that be”)
# ‹יָדָיו כִּידֵי עֵשָׂו› (“hand-him/its like-hand Esau”)
# ‹אָחִיו שְׂעִרֹת וַיְבָרְכֵהוּ› (“brother-him/its shaggy and-bless-
# him/its”)
# "[EN-AID] And he did not recognize him, because his hands were like Esau
# his brother's hands, hairy; and he blessed him."
m.step("Gen.27.23")
# ‹וְלֹא הִכִּירוֹ› (“and-not scrutinize-him/its”)
# — fact holds: failed-recognition-and-not-hikiro
m.fact("failed_recognition_ve_lo_hikiro")
# ‹וַיְבָרְכֵהוּ› (“and-bless-him/its”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.24 · THE_SECOND_FALSE_IDENTITY_ANI ------
# ‹וַיֹּאמֶר אַתָּה זֶה› (“and-say you this”)
# ‹בְּנִי עֵשָׂו וַיֹּאמֶר› (“son-me/my Esau and-say”)
# ‹אָנִי› (“?”)
# "[EN-AID] And he said: Are you this my son Esau? And he said: I am."
m.step("Gen.27.24")
# ‹אַתָּה זֶה בְּנִי› (“you this son-me/my”)
# ‹עֵשָׂו … אָנִי› (“Esau … ”)
# — fact holds: spoken-short-false-confirmation-ani
m.fact("spoken_short_false_confirmation_ani")

# -------------------------- Gen.27.25 · THE_HAGISHA_PUSH_POP_AND_HEVETA_REWEIGH -
# ‹וַיֹּאמֶר הַגִּשָׁה לִּי› (“and-say be-ward to-me/my”)
# ‹וְאֹכְלָה מִצֵּיד בְּנִי› (“and-eat from-chase son-me/my”)
# ‹לְמַעַן תְּבָרֶכְךָ נַפְשִׁי› (“so-that bless-you/your living-being-
# me/my”)
# ‹וַיַּגֶּשׁ־לוֹ וַיֹּאכַל וַיָּבֵא־לוֹ› (“and-be to-him/its and-eat and-
# come/bring to-him/its”)
# ‹יַיִן וַיֵּשְׁתְּ› (“wine and-drink”)
# "[EN-AID] And he said: Bring it near to me, and I will eat of my son's
# hunt, so that my soul may bless you. And he brought it near to him, and he
# ate; and he brought him wine, and he drank."
m.step("Gen.27.25")
# ‹הַגִּשָׁה לִּי› (“be-ward to-me/my”)
# — Isaac speaks a demand — LET: hagisha(Jacob)
m.declare("yitzchaq", "LET",
          "hagisha(yaaqov)")
# ‹וַיַּגֶּשׁ לוֹ› (“and-be to-him/its”)
# — demand settled (popped from the queue): hagisha(Jacob)
m.result("hagisha(yaaqov)", tmark="t1")
# ‹וַיֹּאכַל … וַיָּבֵא לוֹ› (“and-eat … and-come/bring to-him/its”)
# ‹יַיִן וַיֵּשְׁתְּ› (“wine and-drink”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.26 · THE_GESHA_SHQA_COMPOUND ------------
# ‹וַיֹּאמֶר אֵלָיו יִצְחָק› (“and-say to-him/its Isaac”)
# ‹אָבִיו גְּשָׁה־נָּא וּשְׁקָה־לִּי› (“father-him/its be-ward please and-
# kiss-ward to-me/my”)
# ‹בְּנִי› (“son-me/my”)
# "[EN-AID] And Isaac his father said to him: Draw near please and kiss me,
# my son."
m.step("Gen.27.26")
# ‹גְּשָׁה נָּא וּשְׁקָה› (“be-ward please and-kiss-ward”)
# — Isaac speaks a demand — LET: gesha-shqa(Jacob)
m.declare("yitzchaq", "LET",
          "gesha_shqa(yaaqov)")

# -------------------------- Gen.27.27 · THE_GESHA_SHQA_POP_AND_SMELL_BLESS -
# ‹וַיִּגַּשׁ וַיִּשַּׁק־לוֹ וַיָּרַח› (“and-be and-kiss to-him/its and-
# blow”)
# ‹אֶת־רֵיחַ בְּגָדָיו וַיְבָרֲכֵהוּ› (“obj-marker odor garment-him/its and-
# bless-him/its”)
# ‹וַיֹּאמֶר רְאֵה רֵיחַ› (“and-say see odor”)
# ‹בְּנִי כְּרֵיחַ שָׂדֶה› (“son-me/my like-odor field”)
# ‹אֲשֶׁר בֵּרֲכוֹ יְהוָה› (“which bless-him/its YHWH”)
# "[EN-AID] And he drew near and kissed him; and he smelled the smell of his
# garments and blessed him; and he said: See, the smell of my son is as the
# smell of a field that YHWH has blessed."
m.step("Gen.27.27")
# ‹וַיִּגַּשׁ וַיִּשַּׁק› (“and-be and-kiss”)
# — demand settled (popped from the queue): gesha-shqa(Jacob)
m.result("gesha_shqa(yaaqov)", tmark="t1")
# ‹וַיָּרַח … רֵיחַ … וַיְבָרֲכֵהוּ› (“and-blow … odor … and-bless-him/its”)
# — event: ?
m.event("?")
# ‹רְאֵה› (“see”)
# — fact holds: see-exclamatory-opener
m.fact("ree_exclamatory_opener")

# -------------------------- Gen.27.28 · THE_DEMAND_ON_GOD_AND_AGRICULTURAL_DEBUTS -
# ‹וְיִתֶּן־לְךָ הָאֱלֹהִים מִטַּל› (“and-set to-you/your the-God from-dew”)
# ‹הַשָּׁמַיִם וּמִשְׁמַנֵּי הָאָרֶץ› (“the-heavens and-from-fat the-earth”)
# ‹וְרֹב דָּגָן וְתִירֹשׁ› (“and-abundance increase and-must”)
# "[EN-AID] And may God give you of the dew of heaven and of the fat places
# of the earth, and abundance of grain and new wine."
m.step("Gen.27.28")
# ‹וְיִתֶּן לְךָ הָאֱלֹהִים› (“and-set to-you/your the-God”)
# — Isaac speaks a demand — LET: set(the-God, to-Jacob)
m.declare("yitzchaq", "LET",
          "yiten(ha_Elohim, le_yaaqov)")
# witness-tier presupposed read: the_chain_maps_its_own_canon_here on
# dew_fat_grain_wine — read, not installed
m.witness_read("dew_fat_grain_wine", "the_chain_maps_its_own_canon_here",
                cites=["Bereshit Rabbah 66:3"])

# -------------------------- Gen.27.29 · THE_JUSSIVE_CHAIN_HEVE_AND_CHIASM --
# ‹יַעַבְדוּךָ עַמִּים וְיִשְׁתַּחֲווּ› (“work/serve-you/your people and-
# afflict”)
# ‹לְךָ לְאֻמִּים הֱוֵה› (“to-you/your community be”)
# ‹גְבִיר לְאַחֶיךָ וְיִשְׁתַּחֲווּ› (“master to-brother-you/your and-
# afflict”)
# ‹לְךָ בְּנֵי אִמֶּךָ› (“to-you/your son mother-you/your”)
# ‹אֹרְרֶיךָ אָרוּר וּמְבָרֲכֶיךָ› (“execrate-you/your execrate and-bless-
# you/your”)
# ‹בָּרוּךְ› (“bless”)
# "[EN-AID] May peoples serve you, and nations bow to you; be master to your
# brothers, and may your mother's sons bow to you; those who curse you be
# cursed, and those who bless you be blessed."
m.step("Gen.27.29")
# ‹יַעַבְדוּךָ עַמִּים› (“work/serve-you/your people”)
# — Isaac speaks a demand — LET: work/serve-you/your(people)
m.declare("yitzchaq", "LET",
          "yaavdu_kha(amim)")
# ‹וְיִשְׁתַּחֲווּ לְךָ לְאֻמִּים› (“and-afflict to-you/your community”)
# — Isaac speaks a demand — LET: afflict(community)
m.declare("yitzchaq", "LET",
          "yishtachavu(leumim)")
# ‹הֱוֵה גְבִיר› (“be master”)
# — Isaac speaks a demand — LET: be-master(Jacob)
m.declare("yitzchaq", "LET",
          "heve_gevir(yaaqov)")
# ‹וְיִשְׁתַּחֲווּ לְךָ בְּנֵי› (“and-afflict to-you/your son”)
# ‹אִמֶּךָ› (“mother-you/your”)
# — Isaac speaks a demand — LET: afflict(son-imekha)
m.declare("yitzchaq", "LET",
          "yishtachavu(bene_imekha)")
# ‹אֹרְרֶיךָ אָרוּר וּמְבָרֲכֶיךָ› (“execrate-you/your execrate and-bless-
# you/your”)
# ‹בָּרוּךְ› (“bless”)
# — fact holds: execrate-bless-state-formulas
m.fact("arur_barukh_state_formulas")
# witness-tier presupposed read: amen_rule_seated_and_applied_both_ways on
# curse_and_bless_clause — read, not installed
m.witness_read("curse_and_bless_clause", "amen_rule_seated_and_applied_both_ways",
                cites=["Bereshit Rabbah 66:6"])

# -------------------------- Gen.27.30 · THE_JUST_GONE_AND_ESAU_RETURNS -----
# ‹וַיְהִי כַּאֲשֶׁר כִּלָּה› (“and-be like-as/which be-complete”)
# ‹יִצְחָק לְבָרֵךְ אֶת־יַעֲקֹב› (“Isaac to-bless obj-marker Jacob”)
# ‹וַיְהִי אַךְ יָצֹא› (“and-be indeed bring-forth”)
# ‹יָצָא יַעֲקֹב מֵאֵת› (“bring-forth Jacob from-with”)
# ‹פְּנֵי יִצְחָק אָבִיו› (“face Isaac father-him/its”)
# ‹וְעֵשָׂו אָחִיו בָּא› (“and-Esau brother-him/its come/bring”)
# ‹מִצֵּידוֹ› (“from-chase-him/its”)
# "[EN-AID] And it came to pass as Isaac finished blessing Jacob, that Jacob
# had only just gone out from Isaac his father, and Esau his brother came in
# from his hunt."
m.step("Gen.27.30")
# ‹יָצֹא יָצָא … בָּא› (“bring-forth bring-forth … come/bring”)
# ‹מִצֵּידוֹ› (“from-chase-him/its”)
# — event: ?
m.event("?")
# witness-tier presupposed read: glossed_by_the_homicide_statutes_own_verb
# on from_his_hunt — read, not installed
m.witness_read("from_his_hunt", "glossed_by_the_homicide_statutes_own_verb",
                cites=["Bereshit Rabbah 66:5"])

# -------------------------- Gen.27.31 · THE_TRUE_BRING_WRONG_DEMANDEE_AND_YAQUM -
# ‹וַיַּעַשׂ גַּם־הוּא מַטְעַמִּים› (“and-make also he/it delicacy”)
# ‹וַיָּבֵא לְאָבִיו וַיֹּאמֶר› (“and-come/bring to-father-him/its and-say”)
# ‹לְאָבִיו יָקֻם אָבִי› (“to-father-him/its arise father-me/my”)
# ‹וְיֹאכַל מִצֵּיד בְּנוֹ› (“and-eat from-chase son-him/its”)
# ‹בַּעֲבוּר תְּבָרֲכַנִּי נַפְשֶׁךָ› (“for-the-sake-of bless-me/my living-
# being-you/your”)
# "[EN-AID] And he also made delicacies and brought them to his father; and
# he said to his father: Let my father arise and eat of his son's hunt, so
# that your soul may bless me."
m.step("Gen.27.31")
# ‹וַיַּעַשׂ … וַיָּבֵא לְאָבִיו› (“and-make … and-come/bring to-father-
# him/its”)
# — event: ?
m.event("?")
# ‹יָקֻם אָבִי וְיֹאכַל› (“arise father-me/my and-eat”)
# — Esau speaks a demand — LET: arise-eat(Isaac)
m.declare("esav", "LET",
          "yaqum_yokhal(yitzchaq)")

# -------------------------- Gen.27.32 · THE_TRUE_IDENTITY_SPEECH -----------
# ‹וַיֹּאמֶר לוֹ יִצְחָק› (“and-say to-him/its Isaac”)
# ‹אָבִיו מִי־אָתָּה וַיֹּאמֶר› (“father-him/its who? you and-say”)
# ‹אֲנִי בִּנְךָ בְכֹרְךָ› (“son-you/your firstborn-you/your”)
# ‹עֵשָׂו› (“Esau”)
# "[EN-AID] And Isaac his father said to him: Who are you? And he said: I am
# your son, your firstborn, Esau."
m.step("Gen.27.32")
# ‹אֲנִי בִּנְךָ בְכֹרְךָ› (“son-you/your firstborn-you/your”)
# ‹עֵשָׂו› (“Esau”)
# — fact holds: spoken-true-identity-ani-binkha-vekhorkha-Esau
m.fact("spoken_true_identity_ani_binkha_vekhorkha_esav")

# -------------------------- Gen.27.33 · THE_TREMBLE_AND_IRREVOCABILITY -----
# ‹וַיֶּחֱרַד יִצְחָק חֲרָדָה› (“and-shudder-with-terror Isaac fear”)
# ‹גְּדֹלָה עַד־מְאֹד וַיֹּאמֶר› (“great until very and-say”)
# ‹מִי־אֵפוֹא הוּא הַצָּד־צַיִד› (“who? strictly-a-demonstrative-par he/it
# the-lie-alongside chase”)
# ‹וַיָּבֵא לִי וָאֹכַל› (“and-come/bring to-me/my and-eat”)
# ‹מִכֹּל בְּטֶרֶם תָּבוֹא› (“from-all in-non-occurrence come/bring”)
# ‹וָאֲבָרֲכֵהוּ גַּם־בָּרוּךְ יִהְיֶה› (“and-bless-him/its also bless be”)
# "[EN-AID] And Isaac trembled a very great trembling, and said: Who then is
# he that hunted game and brought it to me, and I ate of all before you
# came, and blessed him? Indeed, he shall be blessed."
m.step("Gen.27.33")
# ‹וַיֶּחֱרַד יִצְחָק חֲרָדָה› (“and-shudder-with-terror Isaac fear”)
# ‹… וָאֲבָרֲכֵהוּ … גַּם־בָּרוּךְ יִהְיֶה› (“and-bless-him/its … also bless
# be”)
# — event: ?
m.event("?")
# witness-tier presupposed read: particle_repaid_at_the_same_particle on
# who_then — read, not installed
m.witness_read("who_then", "particle_repaid_at_the_same_particle",
                cites=["Bereshit Rabbah 91:11"])
# witness-tier presupposed read:
# middle_leg_of_the_three_word_blessing_census on i_ate_from_all — read, not
# installed
m.witness_read("i_ate_from_all", "middle_leg_of_the_three_word_blessing_census",
                cites=["Bereshit Rabbah 43:8"])
# witness-tier presupposed read: ratified_by_its_own_signatory on
# indeed_he_shall_be_blessed — read, not installed
m.witness_read("indeed_he_shall_be_blessed", "ratified_by_its_own_signatory",
                cites=["Bereshit Rabbah 67:2", "Bereshit Rabbah 67:12"])
# witness-tier presupposed read: re_explained_as_a_concealed_ending on
# the_trembling — read, not installed
m.witness_read("the_trembling", "re_explained_as_a_concealed_ending",
                cites=["Bereshit Rabbah 99:5", "Onkelos Genesis 27:33"])

# -------------------------- Gen.27.34 · THE_GREAT_BITTER_CRY_AND_BARAKHENI_1 -
# ‹כִּשְׁמֹעַ עֵשָׂו אֶת־דִּבְרֵי› (“like-hear Esau obj-marker word/thing”)
# ‹אָבִיו וַיִּצְעַק צְעָקָה› (“father-him/its and-shriek shriek”)
# ‹גְּדֹלָה וּמָרָה עַד־מְאֹד› (“great and-bitter until very”)
# ‹וַיֹּאמֶר לְאָבִיו בָּרֲכֵנִי› (“and-say to-father-him/its bless-me/my”)
# ‹גַם־אָנִי אָבִי› (“also father-me/my”)
# "[EN-AID] When Esau heard his father's words, he cried with a great and
# very bitter cry, and said to his father: Bless me, me also, my father."
m.step("Gen.27.34")
# ‹וַיִּצְעַק צְעָקָה גְּדֹלָה› (“and-shriek shriek great”)
# ‹וּמָרָה› (“and-bitter”)
# — event: ?
m.event("?")
# ‹בָּרֲכֵנִי גַם־אָנִי› (“bless-me/my also”)
# — Esau speaks a demand — LET: barakheni-1(Isaac)
m.declare("esav", "LET",
          "barakheni_1(yitzchaq)")
# witness-tier presupposed read: booked_against_a_later_cry_at_the_phrase on
# great_and_bitter_cry — read, not installed
m.witness_read("great_and_bitter_cry", "booked_against_a_later_cry_at_the_phrase",
                cites=["Bereshit Rabbah 67:4"])

# -------------------------- Gen.27.35 · THE_DECEIT_WORD_DEBUT --------------
# ‹וַיֹּאמֶר בָּא אָחִיךָ› (“and-say come/bring brother-you/your”)
# ‹בְּמִרְמָה וַיִּקַּח בִּרְכָתֶךָ› (“in-fraud and-take blessing-you/your”)
# "[EN-AID] And he said: Your brother came with deceit, and has taken away
# your blessing."
m.step("Gen.27.35")
# ‹בְּמִרְמָה … בִּרְכָתֶךָ› (“in-fraud … blessing-you/your”)
# — fact holds: spoken-fraud-and-took-blessing
m.fact("spoken_mirma_and_took_blessing")
# witness-tier presupposed read: re_graded_as_wisdom_by_both_members on
# with_cunning — read, not installed
m.witness_read("with_cunning", "re_graded_as_wisdom_by_both_members",
                cites=["Bereshit Rabbah 67:4", "Onkelos Genesis 27:35"])

# -------------------------- Gen.27.36 · THE_BEKHORAH_TOK6_AND_SUPPLANT_HAPAX -
# ‹וַיֹּאמֶר הֲכִי קָרָא› (“and-say the-that call”)
# ‹שְׁמוֹ יַעֲקֹב וַיַּעְקְבֵנִי› (“name-him/its Jacob and-seize-by-the-
# heel-me/my”)
# ‹זֶה פַעֲמַיִם אֶת־בְּכֹרָתִי› (“this stroke obj-marker firstling-of-man-
# me/my”)
# ‹לָקָח וְהִנֵּה עַתָּה› (“take and-behold now”)
# ‹לָקַח בִּרְכָתִי וַיֹּאמַר› (“take blessing-me/my and-say”)
# ‹הֲלֹא־אָצַלְתָּ לִּי בְּרָכָה› (“is-it-not separate to-me/my blessing”)
# "[EN-AID] And he said: Is he not rightly named Jacob? For he has
# supplanted me these two times: he took my birthright, and behold now he
# has taken my blessing. And he said: Have you not reserved a blessing for
# me?"
m.step("Gen.27.36")
# ‹הֲכִי קָרָא שְׁמוֹ› (“the-that call name-him/its”)
# ‹יַעֲקֹב … בְּכֹרָתִי … בִּרְכָתִי› (“Jacob … firstling-of-man-me/my …
# blessing-me/my”)
# — fact holds: interrogative-etiology-no-name-write; bekhorah-tok6-lands
m.fact("interrogative_etiology_no_name_write",
       "bekhorah_tok6_lands")

# -------------------------- Gen.27.37 · THE_GEVIR_CLOSES_AND_ANTI_ANSWER ---
# ‹וַיַּעַן יִצְחָק וַיֹּאמֶר› (“and-eye Isaac and-say”)
# ‹לְעֵשָׂו הֵן גְּבִיר› (“to-Esau lo! master”)
# ‹שַׂמְתִּיו לָךְ וְאֶת־כָּל־אֶחָיו› (“put/set-him/its to-you/your and-obj-
# marker all brother-him/its”)
# ‹נָתַתִּי לוֹ לַעֲבָדִים› (“set to-him/its to-servant”)
# ‹וְדָגָן וְתִירֹשׁ סְמַכְתִּיו› (“and-increase and-must prop-him/its”)
# ‹וּלְכָה אֵפוֹא מָה› (“and-to-you/your strictly-a-demonstrative-par what”)
# ‹אֶעֱשֶׂה בְּנִי› (“make son-me/my”)
# "[EN-AID] And Isaac answered and said to Esau: Behold, I have made him
# master over you, and all his brothers I have given to him for servants,
# and with grain and new wine I have sustained him; and for you then, what
# can I do, my son?"
m.step("Gen.27.37")
# ‹גְּבִיר … וְדָגָן וְתִירֹשׁ› (“master … and-increase and-must”)
# — fact holds: anti-answer-master-increase-must
m.fact("anti_answer_gevir_dagan_tirosh")
# witness-tier presupposed read: slave_property_maxim_voiding_the_claim on
# lord_over_you — read, not installed
m.witness_read("lord_over_you", "slave_property_maxim_voiding_the_claim",
                cites=["Bereshit Rabbah 67:5"])

# -------------------------- Gen.27.38 · THE_BARAKHENI_2_AND_WEEPING --------
# ‹וַיֹּאמֶר עֵשָׂו אֶל־אָבִיו› (“and-say Esau to father-him/its”)
# ‹הַבְרָכָה אַחַת הִוא־לְךָ› (“the-blessing one he/it to-you/your”)
# ‹אָבִי בָּרֲכֵנִי גַם־אָנִי› (“father-me/my bless-me/my also”)
# ‹אָבִי וַיִּשָּׂא עֵשָׂו› (“father-me/my and-lift/carry Esau”)
# ‹קֹלוֹ וַיֵּבְךְּ› (“voice/sound-him/its and-weep”)
# "[EN-AID] And Esau said to his father: Have you but one blessing, my
# father? Bless me, me also, my father. And Esau lifted up his voice and
# wept."
m.step("Gen.27.38")
# ‹בָּרֲכֵנִי גַם־אָנִי› (“bless-me/my also”)
# — Esau speaks a demand — LET: barakheni-2(Isaac)
m.declare("esav", "LET",
          "barakheni_2(yitzchaq)")
# ‹וַיִּשָּׂא … קֹלוֹ וַיֵּבְךְּ› (“and-lift/carry … voice/sound-him/its
# and-weep”)
# — event: ?
m.event("?")

# -------------------------- Gen.27.39 · THE_ANTI_BLESSING_INDICATIVE_FAT_AND_DEW -
# ‹וַיַּעַן יִצְחָק אָבִיו› (“and-eye Isaac father-him/its”)
# ‹וַיֹּאמֶר אֵלָיו הִנֵּה› (“and-say to-him/its behold”)
# ‹מִשְׁמַנֵּי הָאָרֶץ יִהְיֶה› (“from-fat the-earth be”)
# ‹מוֹשָׁבֶךָ וּמִטַּל הַשָּׁמַיִם› (“seat-you/your and-from-dew the-
# heavens”)
# ‹מֵעָל› (“from-over”)
# "[EN-AID] And Isaac his father answered and said to him: Behold, of the
# fat places of the earth shall be your dwelling, and of the dew of heaven
# from above."
m.step("Gen.27.39")
# ‹מִשְׁמַנֵּי הָאָרֶץ יִהְיֶה› (“from-fat the-earth be”)
# ‹… וּמִטַּל› (“and-from-dew”)
# — fact holds: anti-blessing-indicative-fat-dew
m.fact("anti_blessing_indicative_fat_dew")

# -------------------------- Gen.27.40 · THE_SWORD_SERVE_YOKE_NECK_CLOSE ----
# ‹וְעַל־חַרְבְּךָ תִחְיֶה וְאֶת־אָחִיךָ› (“and-over drought-you/your live
# and-obj-marker brother-you/your”)
# ‹תַּעֲבֹד וְהָיָה כַּאֲשֶׁר› (“work/serve and-be like-as/which”)
# ‹תָּרִיד וּפָרַקְתָּ עֻלּוֹ› (“tramp-about and-break-off yoke-him/its”)
# ‹מֵעַל צַוָּארֶךָ› (“from-over back-of-the-neck-you/your”)
# "[EN-AID] And by your sword you shall live, and you shall serve your
# brother; and it shall be, when you shall break loose, that you shall break
# his yoke from off your neck."
m.step("Gen.27.40")
# ‹חַרְבְּךָ תִחְיֶה … תַּעֲבֹד› (“drought-you/your live … work/serve”)
# ‹… תָּרִיד וּפָרַקְתָּ עֻלּוֹ› (“tramp-about and-break-off yoke-him/its”)
# ‹… צַוָּארֶךָ› (“back-of-the-neck-you/your”)
# — fact holds: anti-blessing-sword-serve-yoke-neck
m.fact("anti_blessing_sword_serve_yoke_neck")
# witness-tier presupposed read: condition_written_in_as_plain_sense on
# you_will_remove_his_yoke — read, not installed
m.witness_read("you_will_remove_his_yoke", "condition_written_in_as_plain_sense",
                cites=["Bereshit Rabbah 67:7", "Onkelos Genesis 27:40"])
# witness-tier presupposed read: countersigned_from_above_one_by_one on
# the_blessing_clauses — read, not installed
m.witness_read("the_blessing_clauses", "countersigned_from_above_one_by_one",
                cites=["Bereshit Rabbah 75:8"])
# witness-tier presupposed read: prayer_argued_from_two_mercy_statutes on
# mother_with_children — read, not installed
m.witness_read("mother_with_children", "prayer_argued_from_two_mercy_statutes",
                cites=["Bereshit Rabbah 76:6"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['sa_tze_tzuda_ase_havia(esav)', 'shema_be_qoli(yaaqov)', 'lekh_qach_heveta(yaaqov)', 'qum_sheva_akhla(yitzchaq)', 'yiten(ha_Elohim, le_yaaqov)', 'yaavdu_kha(amim)', 'yishtachavu(leumim)', 'heve_gevir(yaaqov)', 'yishtachavu(bene_imekha)', 'yaqum_yokhal(yitzchaq)', 'barakheni_1(yitzchaq)', 'barakheni_2(yitzchaq)']
    assert len(m.SPECS["log"]) == 15
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['yitzchaq_old_eyes_dim', 'esav_called_as_great_son', 'yitzchaq_does_not_know_death_day', 'hunt_chain_opening_volitives_on_esav', 'retelling_fence_open_rivqah_to_yaaqov', 'retold_isaac_speech_with_delta', 'tovim_attribute_fenced_kids', 'rivqah_will_make_matamim', 'weqatal_heveta_third_member_of_lekh_qach_compound', 'ulay_hypothetical_feel_curse_not_blessing', 'curse_transfer_speech_alai_qillat_kha', 'reissue_shema_and_lekh_qach_same_stack', 'lekh_qach_heveta_still_OPEN_object_mismatch', 'spoken_claim_anokhi_esav_bekhore_kha', 'spoken_hiqra_YHWH_elohekha_lefanai', 'failed_recognition_ve_lo_hikiro', 'spoken_short_false_confirmation_ani', 'ree_exclamatory_opener', 'arur_barukh_state_formulas', 'spoken_true_identity_ani_binkha_vekhorkha_esav', 'spoken_mirma_and_took_blessing', 'interrogative_etiology_no_name_write', 'bekhorah_tok6_lands', 'anti_answer_gevir_dagan_tirosh', 'anti_blessing_indicative_fat_dew', 'anti_blessing_sword_serve_yoke_neck'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 35
    assert sorted(m.WORLD["witnessed"]) == ['three_demands_ladder', 'voice_and_hands']
    assert m.WORLD["witnessed"]['three_demands_ladder']["cites"] == ['Bereshit Rabbah 65:9']
    assert all('one_leg_exact_one_false_one_uncheckable' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['voice_and_hands']["cites"] == ['Bereshit Rabbah 65:20', 'Bereshit Rabbah 65:21']
    assert all('dominance_mechanism_with_an_explicit_toggle' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_dimmed_eyes', 'four_incompatible_causes_all_kept'), ('i_know_not_my_day', 'death_anxiety_rule_with_an_arithmetic_trigger'), ('two_kids', 'licensed_by_a_marriage_contract_and_typologized_to_the_rite'), ('the_self_curse', 'replaced_by_a_prophecy_licence'), ('i_am_esau_your_firstborn', 'equivocation_defence_declined_by_the_other_member'), ('dew_fat_grain_wine', 'the_chain_maps_its_own_canon_here'), ('curse_and_bless_clause', 'amen_rule_seated_and_applied_both_ways'), ('from_his_hunt', 'glossed_by_the_homicide_statutes_own_verb'), ('who_then', 'particle_repaid_at_the_same_particle'), ('i_ate_from_all', 'middle_leg_of_the_three_word_blessing_census'), ('indeed_he_shall_be_blessed', 'ratified_by_its_own_signatory'), ('the_trembling', 're_explained_as_a_concealed_ending'), ('great_and_bitter_cry', 'booked_against_a_later_cry_at_the_phrase'), ('with_cunning', 're_graded_as_wisdom_by_both_members'), ('lord_over_you', 'slave_property_maxim_voiding_the_claim'), ('you_will_remove_his_yoke', 'condition_written_in_as_plain_sense'), ('the_blessing_clauses', 'countersigned_from_above_one_by_one'), ('mother_with_children', 'prayer_argued_from_two_mercy_statutes')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 65:5', 'Bereshit Rabbah 65:8', 'Bereshit Rabbah 65:10']
    assert all('four_incompatible_causes_all_kept' not in f for f in m.WORLD["facts"])
    assert 'the_dimmed_eyes' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 65:12']
    assert all('death_anxiety_rule_with_an_arithmetic_trigger' not in f for f in m.WORLD["facts"])
    assert 'i_know_not_my_day' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 65:14']
    assert all('licensed_by_a_marriage_contract_and_typologized_to_the_rite' not in f for f in m.WORLD["facts"])
    assert 'two_kids' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 65:6', 'Onkelos Genesis 27:13']
    assert all('replaced_by_a_prophecy_licence' not in f for f in m.WORLD["facts"])
    assert 'the_self_curse' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 65:18', 'Onkelos Genesis 27:19', 'Onkelos Genesis 27:24']
    assert all('equivocation_defence_declined_by_the_other_member' not in f for f in m.WORLD["facts"])
    assert 'i_am_esau_your_firstborn' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 66:3']
    assert all('the_chain_maps_its_own_canon_here' not in f for f in m.WORLD["facts"])
    assert 'dew_fat_grain_wine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 66:6']
    assert all('amen_rule_seated_and_applied_both_ways' not in f for f in m.WORLD["facts"])
    assert 'curse_and_bless_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 66:5']
    assert all('glossed_by_the_homicide_statutes_own_verb' not in f for f in m.WORLD["facts"])
    assert 'from_his_hunt' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 91:11']
    assert all('particle_repaid_at_the_same_particle' not in f for f in m.WORLD["facts"])
    assert 'who_then' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 43:8']
    assert all('middle_leg_of_the_three_word_blessing_census' not in f for f in m.WORLD["facts"])
    assert 'i_ate_from_all' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 67:2', 'Bereshit Rabbah 67:12']
    assert all('ratified_by_its_own_signatory' not in f for f in m.WORLD["facts"])
    assert 'indeed_he_shall_be_blessed' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 99:5', 'Onkelos Genesis 27:33']
    assert all('re_explained_as_a_concealed_ending' not in f for f in m.WORLD["facts"])
    assert 'the_trembling' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 67:4']
    assert all('booked_against_a_later_cry_at_the_phrase' not in f for f in m.WORLD["facts"])
    assert 'great_and_bitter_cry' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Bereshit Rabbah 67:4', 'Onkelos Genesis 27:35']
    assert all('re_graded_as_wisdom_by_both_members' not in f for f in m.WORLD["facts"])
    assert 'with_cunning' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Bereshit Rabbah 67:5']
    assert all('slave_property_maxim_voiding_the_claim' not in f for f in m.WORLD["facts"])
    assert 'lord_over_you' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[15]["cites"] == ['Bereshit Rabbah 67:7', 'Onkelos Genesis 27:40']
    assert all('condition_written_in_as_plain_sense' not in f for f in m.WORLD["facts"])
    assert 'you_will_remove_his_yoke' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[16]["cites"] == ['Bereshit Rabbah 75:8']
    assert all('countersigned_from_above_one_by_one' not in f for f in m.WORLD["facts"])
    assert 'the_blessing_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[17]["cites"] == ['Bereshit Rabbah 76:6']
    assert all('prayer_argued_from_two_mercy_statutes' not in f for f in m.WORLD["facts"])
    assert 'mother_with_children' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
