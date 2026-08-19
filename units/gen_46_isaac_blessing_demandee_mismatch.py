#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיְהִי כִּי־זָקֵן יִצְחָק וַתִּכְהֶיןָ עֵינָיו מֵרְאֹת וַיִּקְרָא
# אֶת־עֵשָׂו בְּנוֹ הַגָּדֹל וַיֹּאמֶר אֵלָיו בְּנִי וַיֹּאמֶר אֵלָיו
# הִנֵּנִי
# "[EN-AID] And it came to pass that Isaac was old, and his eyes were dim
# from seeing; and he called Esau his great son and said to him, My son; and
# he said to him, Here I am."
m.step("Gen.27.1")
# ‹זָקֵן יִצְחָק … עֵינָיו מֵרְאֹת … עֵשָׂו בְּנוֹ הַגָּדֹל› (“be-old Isaac
# … eye-him/its from-see … Esau son-him/its the-great”) — fact holds: Isaac-
# old-eyes-dim; Esau-called-as-great-son
m.fact("yitzchaq_old_eyes_dim",
       "esav_called_as_great_son")

# -------------------------- Gen.27.2 · THE_DEATH_DAY_UNKNOWN ---------------
# וַיֹּאמֶר הִנֵּה־נָא זָקַנְתִּי לֹא יָדַעְתִּי יוֹם מוֹתִי
# "[EN-AID] And he said: Behold, please, I am old; I do not know the day of
# my death."
m.step("Gen.27.2")
# ‹זָקַנְתִּי … לֹא יָדַעְתִּי יוֹם מוֹתִי› (“be-old … not know day death-
# me/my”) — fact holds: Isaac-does-not-know-death-day
m.fact("yitzchaq_does_not_know_death_day")

# -------------------------- Gen.27.3 · THE_HUNT_CHAIN_OPENS ----------------
# וְעַתָּה שָׂא־נָא כֵלֶיךָ תֶּלְיְךָ וְקַשְׁתֶּךָ וְצֵא הַשָּׂדֶה וְצוּדָה
# לִּי צָיִד
# "[EN-AID] And now, please take your gear, your quiver and your bow, and go
# out to the field and hunt game for me."
m.step("Gen.27.3")
# ‹שָׂא … וְצֵא … וְצוּדָה› (“lift/carry … and-bring-forth … and-lie-
# alongside-ward”) — fact holds: hunt-chain-opening-volitives-on-Esau
m.fact("hunt_chain_opening_volitives_on_esav")

# -------------------------- Gen.27.4 · THE_COMPOUND_HUNT_MEAL_ON_ESAU ------
# וַעֲשֵׂה־לִי מַטְעַמִּים כַּאֲשֶׁר אָהַבְתִּי וְהָבִיאָה לִּי וְאֹכֵלָה
# בַּעֲבוּר תְּבָרֶכְךָ נַפְשִׁי בְּטֶרֶם אָמוּת
# "[EN-AID] And make me delicacies such as I love, and bring them to me,
# that I may eat, so that my soul may bless you before I die."
m.step("Gen.27.4")
# ‹שָׂא … וְצֵא … וְצוּדָה … וַעֲשֵׂה … וְהָבִיאָה› (“lift/carry … and-
# bring-forth … and-lie-alongside-ward … and-make … and-come/bring-ward”) —
# Isaac speaks a demand — LET: lift/carry-bring-forth-tzuda-make-havia(Esau)
m.declare("yitzchaq", "LET",
          "sa_tze_tzuda_ase_havia(esav)")

# -------------------------- Gen.27.5 · THE_OVERHEAR_AND_ESAU_GOES ----------
# וְרִבְקָה שֹׁמַעַת בְּדַבֵּר יִצְחָק אֶל־עֵשָׂו בְּנוֹ וַיֵּלֶךְ עֵשָׂו
# הַשָּׂדֶה לָצוּד צַיִד לְהָבִיא
# "[EN-AID] And Rivqah was listening as Isaac spoke to Esau his son; and
# Esau went to the field to hunt game to bring."
m.step("Gen.27.5")
# ‹שֹׁמַעַת … וַיֵּלֶךְ … לָצוּד צַיִד› (“hear … and-go … to-lie-alongside
# chase”) — event: ?
m.event("?")

# -------------------------- Gen.27.6 · THE_FENCE_OPENS_TO_JACOB ------------
# וְרִבְקָה אָמְרָה אֶל־יַעֲקֹב בְּנָהּ לֵאמֹר הִנֵּה שָׁמַעְתִּי
# אֶת־אָבִיךָ מְדַבֵּר אֶל־עֵשָׂו אָחִיךָ לֵאמֹר
# "[EN-AID] And Rivqah said to Jacob her son, saying: Behold, I heard your
# father speaking to Esau your brother, saying:"
m.step("Gen.27.6")
# ‹אָמְרָה אֶל־יַעֲקֹב … שָׁמַעְתִּי אֶת־אָבִיךָ מְדַבֵּר אֶל־עֵשָׂו› (“say
# to Jacob … hear obj-marker father-you/your speak to Esau”) — fact holds:
# retelling-fence-open-rivqah-to-Jacob
m.fact("retelling_fence_open_rivqah_to_yaaqov")

# -------------------------- Gen.27.7 · THE_REPORT_DELTA_BEFORE_YHWH --------
# הָבִיאָה לִּי צַיִד וַעֲשֵׂה־לִי מַטְעַמִּים וְאֹכֵלָה וַאֲבָרֶכְכָה
# לִפְנֵי יְהוָה לִפְנֵי מוֹתִי
# "[EN-AID] Bring me game and make me delicacies, that I may eat, and I will
# bless you before YHWH before my death."
m.step("Gen.27.7")
# ‹הָבִיאָה … וַעֲשֵׂה … וְאֹכֵלָה … וַאֲבָרֶכְכָה לִפְנֵי יְהוָה›
# (“come/bring-ward … and-make … and-eat … and-bless-you/your to-face YHWH”)
# — fact holds: retold-isaac-speech-with-delta
m.fact("retold_isaac_speech_with_delta")

# -------------------------- Gen.27.8 · THE_SHEMA_BE_QOLI_ON_JACOB ----------
# וְעַתָּה בְנִי שְׁמַע בְּקֹלִי לַאֲשֶׁר אֲנִי מְצַוָּה אֹתָךְ
# "[EN-AID] And now, my son, listen to my voice, to what I am commanding
# you."
m.step("Gen.27.8")
# ‹שְׁמַע בְּקֹלִי› (“hear in-voice/sound-me/my”) — rivqah speaks a demand —
# LET: hear-in-qoli(Jacob)
m.declare("rivqah", "LET",
          "shema_be_qoli(yaaqov)")

# -------------------------- Gen.27.9 · THE_LEKH_QACH_COMPOUND_ON_JACOB -----
# לֶךְ־נָא אֶל־הַצֹּאן וְקַח־לִי מִשָּׁם שְׁנֵי גְּדָיֵי עִזִּים טֹבִים
# וְאֶעֱשֶׂה אֹתָם מַטְעַמִּים לְאָבִיךָ כַּאֲשֶׁר אָהֵב
# "[EN-AID] Go now to the flock and take for me from there two good kids of
# the goats, and I will make them delicacies for your father as he loves."
m.step("Gen.27.9")
# ‹לֶךְ … וְקַח› (“go … and-take”) — rivqah speaks a demand — LET: go-take-
# come/bring(Jacob)
m.declare("rivqah", "LET",
          "lekh_qach_heveta(yaaqov)")
# ‹גְּדָיֵי עִזִּים טֹבִים … וְאֶעֱשֶׂה … כַּאֲשֶׁר אָהֵב› (“young-goat she-
# goat good … and-make … like-as/which have-affection-for”) — fact holds:
# good-attribute-fenced-kids; rivqah-will-make-delicacy
m.fact("tovim_attribute_fenced_kids",
       "rivqah_will_make_matamim")

# -------------------------- Gen.27.10 · THE_WEQATAL_DUTY_AND_BLESS_CONTENT -
# וְהֵבֵאתָ לְאָבִיךָ וְאָכָל בַּעֲבֻר אֲשֶׁר יְבָרֶכְךָ לִפְנֵי מוֹתוֹ
# "[EN-AID] And you shall bring it to your father, and he will eat, so that
# he may bless you before his death."
m.step("Gen.27.10")
# ‹וְהֵבֵאתָ … וְאָכָל … יְבָרֶכְךָ לִפְנֵי מוֹתוֹ› (“and-come/bring … and-
# eat … bless-you/your to-face death-him/its”) — fact holds: weqatal-
# come/bring-third-member-fowl-go-take-compound
m.fact("weqatal_heveta_third_member_of_lekh_qach_compound")

# -------------------------- Gen.27.11 · THE_HAIRY_VS_SMOOTH_OBJECTION ------
# וַיֹּאמֶר יַעֲקֹב אֶל־רִבְקָה אִמּוֹ הֵן עֵשָׂו אָחִי אִישׁ שָׂעִר
# וְאָנֹכִי אִישׁ חָלָק
# "[EN-AID] And Jacob said to Rivqah his mother: Behold, Esau my brother is
# a hairy man, and I am a smooth man."
m.step("Gen.27.11")
# ‹אִישׁ שָׂעִר … אִישׁ חָלָק› (“man shaggy … man smooth”) — event: ?
m.event("?")

# -------------------------- Gen.27.12 · THE_ULAY_FEEL_CURSE_FRAME ----------
# אוּלַי יְמֻשֵּׁנִי אָבִי וְהָיִיתִי בְעֵינָיו כִּמְתַעְתֵּעַ וְהֵבֵאתִי
# עָלַי קְלָלָה וְלֹא בְרָכָה
# "[EN-AID] Perhaps my father will feel me, and I shall be in his eyes as a
# mocker, and I shall bring on myself a curse and not a blessing."
m.step("Gen.27.12")
# ‹אוּלַי יְמֻשֵּׁנִי … כִּמְתַעְתֵּעַ … קְלָלָה וְלֹא בְרָכָה› (“if-not
# feel-of-me/my … like-cheat … vilification and-not blessing”) — fact holds:
# if-not-hypothetical-feel-curse-not-blessing
m.fact("ulay_hypothetical_feel_curse_not_blessing")

# -------------------------- Gen.27.13 · THE_CURSE_ABSORPTION_AND_REISSUE ---
# וַתֹּאמֶר לוֹ אִמּוֹ עָלַי קִלְלָתְךָ בְּנִי אַךְ שְׁמַע בְּקֹלִי וְלֵךְ
# קַח־לִי
# "[EN-AID] And his mother said to him: Upon me be your curse, my son; only
# listen to my voice, and go, take for me."
m.step("Gen.27.13")
# ‹עָלַי קִלְלָתְךָ בְּנִי› (“over-me/my vilification-you/your son-me/my”) —
# fact holds: curse-transfer-speech-alai-qillat-you/your
m.fact("curse_transfer_speech_alai_qillat_kha")
# ‹אַךְ שְׁמַע בְּקֹלִי וְלֵךְ קַח› (“indeed hear in-voice/sound-me/my and-
# go take”) — fact holds: reissue-hear-and-go-take-same-stack
m.fact("reissue_shema_and_lekh_qach_same_stack")

# -------------------------- Gen.27.14 · THE_POP_WEIGH_THREE_ROOT_TO_MOTHER -
# וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא לְאִמּוֹ וַתַּעַשׂ אִמּוֹ מַטְעַמִּים
# כַּאֲשֶׁר אָהֵב אָבִיו
# "[EN-AID] And he went and took and brought to his mother; and his mother
# made delicacies as his father loves."
m.step("Gen.27.14")
# ‹וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא לְאִמּוֹ› (“and-go and-take and-come/bring
# to-mother-him/its”) — event: ?
m.event("?")
# ‹וַיֵּלֶךְ וַיִּקַּח וַיָּבֵא לְאִמּוֹ› (“and-go and-take and-come/bring
# to-mother-him/its”) — fact holds: go-take-come/bring-still-OPEN-object-
# mismatch
m.fact("lekh_qach_heveta_still_OPEN_object_mismatch")
# ‹וַתַּעַשׂ אִמּוֹ מַטְעַמִּים› (“and-make mother-him/its delicacy”) —
# event: ?
m.event("?")

# -------------------------- Gen.27.15 · THE_DRESS_SMALL_AS_GREAT -----------
# וַתִּקַּח רִבְקָה אֶת־בִּגְדֵי עֵשָׂו בְּנָהּ הַגָּדֹל הַחֲמֻדֹת אֲשֶׁר
# אִתָּהּ בַּבָּיִת וַתַּלְבֵּשׁ אֶת־יַעֲקֹב בְּנָהּ הַקָּטָן
# "[EN-AID] And Rivqah took the garments of Esau her great son, the precious
# ones that were with her in the house, and clothed Jacob her small son."
m.step("Gen.27.15")
# ‹בִּגְדֵי עֵשָׂו … הַגָּדֹל … וַתַּלְבֵּשׁ … הַקָּטָן› (“garment Esau …
# the-great … and-wrap-around … the-abbreviated”) — event: ?
m.event("?")

# -------------------------- Gen.27.16 · THE_SKINS_ON_HANDS_AND_NECK --------
# וְאֵת עֹרֹת גְּדָיֵי הָעִזִּים הִלְבִּישָׁה עַל־יָדָיו וְעַל חֶלְקַת
# צַוָּארָיו
# "[EN-AID] And the skins of the kids of the goats she put on his hands and
# on the smooth of his neck."
m.step("Gen.27.16")
# ‹עֹרֹת … הִלְבִּישָׁה עַל־יָדָיו … חֶלְקַת צַוָּארָיו› (“skin … wrap-
# around over hand-him/its … smoothness back-of-the-neck-him/its”) — event:
# ?
m.event("?")

# -------------------------- Gen.27.17 · THE_HANDOFF_INTO_JACOBS_HAND -------
# וַתִּתֵּן אֶת־הַמַּטְעַמִּים וְאֶת־הַלֶּחֶם אֲשֶׁר עָשָׂתָה בְּיַד יַעֲקֹב
# בְּנָהּ
# "[EN-AID] And she gave the delicacies and the bread that she had made into
# the hand of Jacob her son."
m.step("Gen.27.17")
# ‹וַתִּתֵּן … בְּיַד יַעֲקֹב› (“and-set … in-hand Jacob”) — event: ?
m.event("?")

# -------------------------- Gen.27.18 · THE_QAL_ARRIVAL_AND_WHO_ARE_YOU ----
# וַיָּבֹא אֶל־אָבִיו וַיֹּאמֶר אָבִי וַיֹּאמֶר הִנֶּנִּי מִי אַתָּה בְּנִי
# "[EN-AID] And he came to his father and said, My father; and he said, Here
# I am; who are you, my son?"
m.step("Gen.27.18")
# ‹וַיָּבֹא … מִי אַתָּה בְּנִי› (“and-come/bring … who? you son-me/my”) —
# event: ?
m.event("?")

# -------------------------- Gen.27.19 · THE_FALSE_IDENTITY_AND_QUM_COMPOUND -
# וַיֹּאמֶר יַעֲקֹב אֶל־אָבִיו אָנֹכִי עֵשָׂו בְּכֹרֶךָ עָשִׂיתִי כַּאֲשֶׁר
# דִּבַּרְתָּ אֵלָי קוּם־נָא שְׁבָה וְאָכְלָה מִצֵּידִי בַּעֲבוּר
# תְּבָרֲכַנִּי נַפְשֶׁךָ
# "[EN-AID] And Jacob said to his father: I am Esau your firstborn; I have
# done as you spoke to me; arise please, sit, and eat of my hunt, so that
# your soul may bless me."
m.step("Gen.27.19")
# ‹אָנֹכִי עֵשָׂו בְּכֹרֶךָ … עָשִׂיתִי› (“Esau firstborn-you/your … make”)
# — fact holds: spoken-claim-I-Esau-bekhore-you/your
m.fact("spoken_claim_anokhi_esav_bekhore_kha")
# ‹קוּם … שְׁבָה … וְאָכְלָה› (“arise … dwell/sit-ward … and-eat-ward”) —
# Jacob speaks a demand — LET: arise-seven-akhla(Isaac)
m.declare("yaaqov", "LET",
          "qum_sheva_akhla(yitzchaq)")

# -------------------------- Gen.27.20 · THE_YHWH_ELOHEKHA_AND_HIQRA_DEBUTS -
# וַיֹּאמֶר יִצְחָק אֶל־בְּנוֹ מַה־זֶּה מִהַרְתָּ לִמְצֹא בְּנִי וַיֹּאמֶר
# כִּי הִקְרָה יְהוָה אֱלֹהֶיךָ לְפָנָי
# "[EN-AID] And Isaac said to his son: How is it that you found so quickly,
# my son? And he said: Because YHWH your God made it happen before me."
m.step("Gen.27.20")
# ‹הִקְרָה יְהוָה אֱלֹהֶיךָ לְפָנָי› (“light-upon YHWH God-you/your to-face-
# me/my”) — fact holds: spoken-light-upon-the-LORD-elohekha-before-Me
m.fact("spoken_hiqra_YHWH_elohekha_lefanai")

# -------------------------- Gen.27.21 · THE_GESHA_PUSH_AND_FEEL_HAPAX ------
# וַיֹּאמֶר יִצְחָק אֶל־יַעֲקֹב גְּשָׁה־נָּא וַאֲמֻשְׁךָ בְּנִי הַאַתָּה זֶה
# בְּנִי עֵשָׂו אִם־לֹא
# "[EN-AID] And Isaac said to Jacob: Draw near please, that I may feel you,
# my son; are you this my son Esau or not?"
m.step("Gen.27.21")
# ‹גְּשָׁה נָּא› (“be-ward please”) — Isaac speaks a demand — LET:
# gesha(Jacob)
m.declare("yitzchaq", "LET",
          "gesha(yaaqov)")

# -------------------------- Gen.27.22 · THE_GESHA_POP_AND_VOICE_HANDS_VERDICT -
# וַיִּגַּשׁ יַעֲקֹב אֶל־יִצְחָק אָבִיו וַיְמֻשֵּׁהוּ וַיֹּאמֶר הַקֹּל קוֹל
# יַעֲקֹב וְהַיָּדַיִם יְדֵי עֵשָׂו
# "[EN-AID] And Jacob drew near to Isaac his father, and he felt him; and he
# said: The voice is Jacob's voice, but the hands are Esau's hands."
m.step("Gen.27.22")
# ‹וַיִּגַּשׁ יַעֲקֹב› (“and-be Jacob”) — demand settled (popped from the
# queue): gesha(Jacob)
m.result("gesha(yaaqov)", tmark="t1")
# ‹וַיְמֻשֵּׁהוּ … הַקֹּל קוֹל יַעֲקֹב וְהַיָּדַיִם יְדֵי עֵשָׂו› (“and-
# feel-of-him/its … the-voice/sound voice/sound Jacob and-the-hand hand
# Esau”) — event: ?
m.event("?")

# -------------------------- Gen.27.23 · THE_NAKAR_DEBUT_AND_FIRST_BLESS_EVENT -
# וְלֹא הִכִּירוֹ כִּי־הָיוּ יָדָיו כִּידֵי עֵשָׂו אָחִיו שְׂעִרֹת
# וַיְבָרְכֵהוּ
# "[EN-AID] And he did not recognize him, because his hands were like Esau
# his brother's hands, hairy; and he blessed him."
m.step("Gen.27.23")
# ‹וְלֹא הִכִּירוֹ› (“and-not scrutinize-him/its”) — fact holds: failed-
# recognition-and-not-hikiro
m.fact("failed_recognition_ve_lo_hikiro")
# ‹וַיְבָרְכֵהוּ› (“and-bless-him/its”) — event: ?
m.event("?")

# -------------------------- Gen.27.24 · THE_SECOND_FALSE_IDENTITY_ANI ------
# וַיֹּאמֶר אַתָּה זֶה בְּנִי עֵשָׂו וַיֹּאמֶר אָנִי
# "[EN-AID] And he said: Are you this my son Esau? And he said: I am."
m.step("Gen.27.24")
# ‹אַתָּה זֶה בְּנִי עֵשָׂו … אָנִי› (“you this son-me/my Esau … ”) — fact
# holds: spoken-short-false-confirmation-ani
m.fact("spoken_short_false_confirmation_ani")

# -------------------------- Gen.27.25 · THE_HAGISHA_PUSH_POP_AND_HEVETA_REWEIGH -
# וַיֹּאמֶר הַגִּשָׁה לִּי וְאֹכְלָה מִצֵּיד בְּנִי לְמַעַן תְּבָרֶכְךָ
# נַפְשִׁי וַיַּגֶּשׁ־לוֹ וַיֹּאכַל וַיָּבֵא־לוֹ יַיִן וַיֵּשְׁתְּ
# "[EN-AID] And he said: Bring it near to me, and I will eat of my son's
# hunt, so that my soul may bless you. And he brought it near to him, and he
# ate; and he brought him wine, and he drank."
m.step("Gen.27.25")
# ‹הַגִּשָׁה לִּי› (“be-ward to-me/my”) — Isaac speaks a demand — LET:
# hagisha(Jacob)
m.declare("yitzchaq", "LET",
          "hagisha(yaaqov)")
# ‹וַיַּגֶּשׁ לוֹ› (“and-be to-him/its”) — demand settled (popped from the
# queue): hagisha(Jacob)
m.result("hagisha(yaaqov)", tmark="t1")
# ‹וַיֹּאכַל … וַיָּבֵא לוֹ יַיִן וַיֵּשְׁתְּ› (“and-eat … and-come/bring
# to-him/its wine and-drink”) — event: ?
m.event("?")

# -------------------------- Gen.27.26 · THE_GESHA_SHQA_COMPOUND ------------
# וַיֹּאמֶר אֵלָיו יִצְחָק אָבִיו גְּשָׁה־נָּא וּשְׁקָה־לִּי בְּנִי
# "[EN-AID] And Isaac his father said to him: Draw near please and kiss me,
# my son."
m.step("Gen.27.26")
# ‹גְּשָׁה נָּא וּשְׁקָה› (“be-ward please and-kiss-ward”) — Isaac speaks a
# demand — LET: gesha-shqa(Jacob)
m.declare("yitzchaq", "LET",
          "gesha_shqa(yaaqov)")

# -------------------------- Gen.27.27 · THE_GESHA_SHQA_POP_AND_SMELL_BLESS -
# וַיִּגַּשׁ וַיִּשַּׁק־לוֹ וַיָּרַח אֶת־רֵיחַ בְּגָדָיו וַיְבָרֲכֵהוּ
# וַיֹּאמֶר רְאֵה רֵיחַ בְּנִי כְּרֵיחַ שָׂדֶה אֲשֶׁר בֵּרֲכוֹ יְהוָה
# "[EN-AID] And he drew near and kissed him; and he smelled the smell of his
# garments and blessed him; and he said: See, the smell of my son is as the
# smell of a field that YHWH has blessed."
m.step("Gen.27.27")
# ‹וַיִּגַּשׁ וַיִּשַּׁק› (“and-be and-kiss”) — demand settled (popped from
# the queue): gesha-shqa(Jacob)
m.result("gesha_shqa(yaaqov)", tmark="t1")
# ‹וַיָּרַח … רֵיחַ … וַיְבָרֲכֵהוּ› (“and-blow … odor … and-bless-him/its”)
# — event: ?
m.event("?")
# ‹רְאֵה› (“see”) — fact holds: see-exclamatory-opener
m.fact("ree_exclamatory_opener")

# -------------------------- Gen.27.28 · THE_DEMAND_ON_GOD_AND_AGRICULTURAL_DEBUTS -
# וְיִתֶּן־לְךָ הָאֱלֹהִים מִטַּל הַשָּׁמַיִם וּמִשְׁמַנֵּי הָאָרֶץ וְרֹב
# דָּגָן וְתִירֹשׁ
# "[EN-AID] And may God give you of the dew of heaven and of the fat places
# of the earth, and abundance of grain and new wine."
m.step("Gen.27.28")
# ‹וְיִתֶּן לְךָ הָאֱלֹהִים› (“and-set to-you/your the-God”) — Isaac speaks
# a demand — LET: set(the-God, to-Jacob)
m.declare("yitzchaq", "LET",
          "yiten(ha_Elohim, le_yaaqov)")

# -------------------------- Gen.27.29 · THE_JUSSIVE_CHAIN_HEVE_AND_CHIASM --
# יַעַבְדוּךָ עַמִּים וְיִשְׁתַּחֲווּ לְךָ לְאֻמִּים הֱוֵה גְבִיר לְאַחֶיךָ
# וְיִשְׁתַּחֲווּ לְךָ בְּנֵי אִמֶּךָ אֹרְרֶיךָ אָרוּר וּמְבָרֲכֶיךָ
# בָּרוּךְ
# "[EN-AID] May peoples serve you, and nations bow to you; be master to your
# brothers, and may your mother's sons bow to you; those who curse you be
# cursed, and those who bless you be blessed."
m.step("Gen.27.29")
# ‹יַעַבְדוּךָ עַמִּים› (“work/serve-you/your people”) — Isaac speaks a
# demand — LET: work/serve-you/your(people)
m.declare("yitzchaq", "LET",
          "yaavdu_kha(amim)")
# ‹וְיִשְׁתַּחֲווּ לְךָ לְאֻמִּים› (“and-afflict to-you/your community”) —
# Isaac speaks a demand — LET: afflict(community)
m.declare("yitzchaq", "LET",
          "yishtachavu(leumim)")
# ‹הֱוֵה גְבִיר› (“be master”) — Isaac speaks a demand — LET: be-
# master(Jacob)
m.declare("yitzchaq", "LET",
          "heve_gevir(yaaqov)")
# ‹וְיִשְׁתַּחֲווּ לְךָ בְּנֵי אִמֶּךָ› (“and-afflict to-you/your son
# mother-you/your”) — Isaac speaks a demand — LET: afflict(son-imekha)
m.declare("yitzchaq", "LET",
          "yishtachavu(bene_imekha)")
# ‹אֹרְרֶיךָ אָרוּר וּמְבָרֲכֶיךָ בָּרוּךְ› (“execrate-you/your execrate
# and-bless-you/your bless”) — fact holds: execrate-bless-state-formulas
m.fact("arur_barukh_state_formulas")

# -------------------------- Gen.27.30 · THE_JUST_GONE_AND_ESAU_RETURNS -----
# וַיְהִי כַּאֲשֶׁר כִּלָּה יִצְחָק לְבָרֵךְ אֶת־יַעֲקֹב וַיְהִי אַךְ יָצֹא
# יָצָא יַעֲקֹב מֵאֵת פְּנֵי יִצְחָק אָבִיו וְעֵשָׂו אָחִיו בָּא מִצֵּידוֹ
# "[EN-AID] And it came to pass as Isaac finished blessing Jacob, that Jacob
# had only just gone out from Isaac his father, and Esau his brother came in
# from his hunt."
m.step("Gen.27.30")
# ‹יָצֹא יָצָא … בָּא מִצֵּידוֹ› (“bring-forth bring-forth … come/bring
# from-chase-him/its”) — event: ?
m.event("?")

# -------------------------- Gen.27.31 · THE_TRUE_BRING_WRONG_DEMANDEE_AND_YAQUM -
# וַיַּעַשׂ גַּם־הוּא מַטְעַמִּים וַיָּבֵא לְאָבִיו וַיֹּאמֶר לְאָבִיו יָקֻם
# אָבִי וְיֹאכַל מִצֵּיד בְּנוֹ בַּעֲבוּר תְּבָרֲכַנִּי נַפְשֶׁךָ
# "[EN-AID] And he also made delicacies and brought them to his father; and
# he said to his father: Let my father arise and eat of his son's hunt, so
# that your soul may bless me."
m.step("Gen.27.31")
# ‹וַיַּעַשׂ … וַיָּבֵא לְאָבִיו› (“and-make … and-come/bring to-father-
# him/its”) — event: ?
m.event("?")
# ‹יָקֻם אָבִי וְיֹאכַל› (“arise father-me/my and-eat”) — Esau speaks a
# demand — LET: arise-eat(Isaac)
m.declare("esav", "LET",
          "yaqum_yokhal(yitzchaq)")

# -------------------------- Gen.27.32 · THE_TRUE_IDENTITY_SPEECH -----------
# וַיֹּאמֶר לוֹ יִצְחָק אָבִיו מִי־אָתָּה וַיֹּאמֶר אֲנִי בִּנְךָ בְכֹרְךָ
# עֵשָׂו
# "[EN-AID] And Isaac his father said to him: Who are you? And he said: I am
# your son, your firstborn, Esau."
m.step("Gen.27.32")
# ‹אֲנִי בִּנְךָ בְכֹרְךָ עֵשָׂו› (“son-you/your firstborn-you/your Esau”) —
# fact holds: spoken-true-identity-ani-binkha-vekhorkha-Esau
m.fact("spoken_true_identity_ani_binkha_vekhorkha_esav")

# -------------------------- Gen.27.33 · THE_TREMBLE_AND_IRREVOCABILITY -----
# וַיֶּחֱרַד יִצְחָק חֲרָדָה גְּדֹלָה עַד־מְאֹד וַיֹּאמֶר מִי־אֵפוֹא הוּא
# הַצָּד־צַיִד וַיָּבֵא לִי וָאֹכַל מִכֹּל בְּטֶרֶם תָּבוֹא וָאֲבָרֲכֵהוּ
# גַּם־בָּרוּךְ יִהְיֶה
# "[EN-AID] And Isaac trembled a very great trembling, and said: Who then is
# he that hunted game and brought it to me, and I ate of all before you
# came, and blessed him? Indeed, he shall be blessed."
m.step("Gen.27.33")
# ‹וַיֶּחֱרַד חֲרָדָה … וָאֲבָרֲכֵהוּ … גַּם־בָּרוּךְ יִהְיֶה› (“and-
# shudder-with-terror fear … and-bless-him/its … also bless be”) — event: ?
m.event("?")

# -------------------------- Gen.27.34 · THE_GREAT_BITTER_CRY_AND_BARAKHENI_1 -
# כִּשְׁמֹעַ עֵשָׂו אֶת־דִּבְרֵי אָבִיו וַיִּצְעַק צְעָקָה גְּדֹלָה וּמָרָה
# עַד־מְאֹד וַיֹּאמֶר לְאָבִיו בָּרֲכֵנִי גַם־אָנִי אָבִי
# "[EN-AID] When Esau heard his father's words, he cried with a great and
# very bitter cry, and said to his father: Bless me, me also, my father."
m.step("Gen.27.34")
# ‹וַיִּצְעַק צְעָקָה גְּדֹלָה וּמָרָה› (“and-shriek shriek great and-
# bitter”) — event: ?
m.event("?")
# ‹בָּרֲכֵנִי גַם־אָנִי› (“bless-me/my also”) — Esau speaks a demand — LET:
# barakheni-1(Isaac)
m.declare("esav", "LET",
          "barakheni_1(yitzchaq)")

# -------------------------- Gen.27.35 · THE_DECEIT_WORD_DEBUT --------------
# וַיֹּאמֶר בָּא אָחִיךָ בְּמִרְמָה וַיִּקַּח בִּרְכָתֶךָ
# "[EN-AID] And he said: Your brother came with deceit, and has taken away
# your blessing."
m.step("Gen.27.35")
# ‹בְּמִרְמָה … בִּרְכָתֶךָ› (“in-fraud … blessing-you/your”) — fact holds:
# spoken-fraud-and-took-blessing
m.fact("spoken_mirma_and_took_blessing")

# -------------------------- Gen.27.36 · THE_BEKHORAH_TOK6_AND_SUPPLANT_HAPAX -
# וַיֹּאמֶר הֲכִי קָרָא שְׁמוֹ יַעֲקֹב וַיַּעְקְבֵנִי זֶה פַעֲמַיִם
# אֶת־בְּכֹרָתִי לָקָח וְהִנֵּה עַתָּה לָקַח בִּרְכָתִי וַיֹּאמַר
# הֲלֹא־אָצַלְתָּ לִּי בְּרָכָה
# "[EN-AID] And he said: Is he not rightly named Jacob? For he has
# supplanted me these two times: he took my birthright, and behold now he
# has taken my blessing. And he said: Have you not reserved a blessing for
# me?"
m.step("Gen.27.36")
# ‹הֲכִי קָרָא שְׁמוֹ יַעֲקֹב … בְּכֹרָתִי … בִּרְכָתִי› (“the-that call
# name-him/its Jacob … firstling-of-man-me/my … blessing-me/my”) — fact
# holds: interrogative-etiology-no-name-write; bekhorah-tok6-lands
m.fact("interrogative_etiology_no_name_write",
       "bekhorah_tok6_lands")

# -------------------------- Gen.27.37 · THE_GEVIR_CLOSES_AND_ANTI_ANSWER ---
# וַיַּעַן יִצְחָק וַיֹּאמֶר לְעֵשָׂו הֵן גְּבִיר שַׂמְתִּיו לָךְ
# וְאֶת־כָּל־אֶחָיו נָתַתִּי לוֹ לַעֲבָדִים וְדָגָן וְתִירֹשׁ סְמַכְתִּיו
# וּלְכָה אֵפוֹא מָה אֶעֱשֶׂה בְּנִי
# "[EN-AID] And Isaac answered and said to Esau: Behold, I have made him
# master over you, and all his brothers I have given to him for servants,
# and with grain and new wine I have sustained him; and for you then, what
# can I do, my son?"
m.step("Gen.27.37")
# ‹גְּבִיר … וְדָגָן וְתִירֹשׁ› (“master … and-increase and-must”) — fact
# holds: anti-answer-master-increase-must
m.fact("anti_answer_gevir_dagan_tirosh")

# -------------------------- Gen.27.38 · THE_BARAKHENI_2_AND_WEEPING --------
# וַיֹּאמֶר עֵשָׂו אֶל־אָבִיו הַבְרָכָה אַחַת הִוא־לְךָ אָבִי בָּרֲכֵנִי
# גַם־אָנִי אָבִי וַיִּשָּׂא עֵשָׂו קֹלוֹ וַיֵּבְךְּ
# "[EN-AID] And Esau said to his father: Have you but one blessing, my
# father? Bless me, me also, my father. And Esau lifted up his voice and
# wept."
m.step("Gen.27.38")
# ‹בָּרֲכֵנִי גַם־אָנִי› (“bless-me/my also”) — Esau speaks a demand — LET:
# barakheni-2(Isaac)
m.declare("esav", "LET",
          "barakheni_2(yitzchaq)")
# ‹וַיִּשָּׂא … קֹלוֹ וַיֵּבְךְּ› (“and-lift/carry … voice/sound-him/its
# and-weep”) — event: ?
m.event("?")

# -------------------------- Gen.27.39 · THE_ANTI_BLESSING_INDICATIVE_FAT_AND_DEW -
# וַיַּעַן יִצְחָק אָבִיו וַיֹּאמֶר אֵלָיו הִנֵּה מִשְׁמַנֵּי הָאָרֶץ
# יִהְיֶה מוֹשָׁבֶךָ וּמִטַּל הַשָּׁמַיִם מֵעָל
# "[EN-AID] And Isaac his father answered and said to him: Behold, of the
# fat places of the earth shall be your dwelling, and of the dew of heaven
# from above."
m.step("Gen.27.39")
# ‹מִשְׁמַנֵּי הָאָרֶץ יִהְיֶה … וּמִטַּל› (“from-fat the-earth be … and-
# from-dew”) — fact holds: anti-blessing-indicative-fat-dew
m.fact("anti_blessing_indicative_fat_dew")

# -------------------------- Gen.27.40 · THE_SWORD_SERVE_YOKE_NECK_CLOSE ----
# וְעַל־חַרְבְּךָ תִחְיֶה וְאֶת־אָחִיךָ תַּעֲבֹד וְהָיָה כַּאֲשֶׁר תָּרִיד
# וּפָרַקְתָּ עֻלּוֹ מֵעַל צַוָּארֶךָ
# "[EN-AID] And by your sword you shall live, and you shall serve your
# brother; and it shall be, when you shall break loose, that you shall break
# his yoke from off your neck."
m.step("Gen.27.40")
# ‹חַרְבְּךָ תִחְיֶה … תַּעֲבֹד … תָּרִיד וּפָרַקְתָּ עֻלּוֹ … צַוָּארֶךָ›
# (“drought-you/your live … work/serve … tramp-about and-break-off yoke-
# him/its … back-of-the-neck-you/your”) — fact holds: anti-blessing-sword-
# serve-yoke-neck
m.fact("anti_blessing_sword_serve_yoke_neck")

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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
