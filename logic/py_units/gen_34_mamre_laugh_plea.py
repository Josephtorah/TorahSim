#!/usr/bin/env python3
# =============================================================================
# gen_34_mamre_laugh_plea — 18:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_34_mamre_laugh_plea.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The visitors at Mamre, the laugh within, the plea for Sodom (18:1-33)"""
from machine import Machine

m = Machine("gen_34_mamre_laugh_plea")

# -------------------------- Gen.18.1 · THE_THIRD_APPEARANCE ----------------
# ‹וַיֵּרָא אֵלָיו יְהוָה› (“and-see to-him/its YHWH”)
# ‹בְּאֵלֹנֵי מַמְרֵא וְהוּא› (“in-oak Mamre and-he/it”)
# ‹יֹשֵׁב פֶּתַח־הָאֹהֶל כְּחֹם› (“dwell/sit opening the-tent like-heat”)
# ‹הַיּוֹם› (“the-day”)
# "And the LORD appeared unto him by the terebinths of Mamre, as he sat in
# the tent door in the heat of the day;"
m.step("Gen.18.1")
# ‹וַיֵּרָא אֵלָיו יְהוָה› (“and-see to-him/its YHWH”)
# — event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹בְּאֵלֹנֵי מַמְרֵא› (“in-oak Mamre”)
# — reads without prior install (flag, not fix): Mamre
m.presupposed("mamre")
# ‹וְהוּא יֹשֵׁב פֶּתַח־הָאֹהֶל› (“and-he/it dwell/sit opening the-tent”)
# ‹כְּחֹם הַיּוֹם› (“like-heat the-day”)
# — fact holds: dwell/sit-opening-the-tent-like-heat-the-day
m.fact("yoshev_petach_ha_ohel_ke_chom_ha_yom")
# witness-tier presupposed read: six_hours_by_comparison on heat_of_the_day
# — read, not installed
m.witness_read("heat_of_the_day", "six_hours_by_comparison",
                cites=["Bereshit Rabbah 48:8", "Bereshit Rabbah 48:7"])

# -------------------------- Gen.18.2 · THREE_MEN_AND_THE_BOW ---------------
# ‹וַיִּשָּׂא עֵינָיו וַיַּרְא› (“and-lift/carry eye-him/its and-see”)
# ‹וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים› (“and-behold three man”)
# ‹נִצָּבִים עָלָיו וַיַּרְא› (“stand over-him/its and-see”)
# ‹וַיָּרָץ לִקְרָאתָם מִפֶּתַח› (“and-run to-encountering-them/their from-
# opening”)
# ‹הָאֹהֶל וַיִּשְׁתַּחוּ אָרְצָה› (“the-tent and-afflict earth-ward”)
# "and he lifted up his eyes and looked, and, lo, three men stood over
# against him; and when he saw them, he ran to meet them from the tent door,
# and bowed down to the earth,"
m.step("Gen.18.2")
# ‹וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים› (“and-behold three man”)
# ‹נִצָּבִים עָלָיו› (“stand over-him/its”)
# — the world gains: three-man
m.install("shelosha_anashim")
# ‹וַיָּרָץ לִקְרָאתָם› (“and-run to-encountering-them/their”)
# — event: run — agent Abraham
m.event("run", agent="avraham")
# ‹וַיִּשְׁתַּחוּ אָרְצָה› (“and-afflict earth-ward”)
# — event: bow — agent Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.18.3 · THE_DOOR_PETITION -------------------
# ‹וַיֹּאמַר אֲדֹנָי אִם־נָא› (“and-say lord-me/my if please”)
# ‹מָצָאתִי חֵן בְּעֵינֶיךָ› (“find graciousness in-eye-you/your”)
# ‹אַל־נָא תַעֲבֹר מֵעַל› (“do-not please pass-over from-over”)
# ‹עַבְדֶּךָ› (“servant-you/your”)
# "and said: 'My lord, if now I have found favour in thy sight, pass not
# away, I pray thee, from thy servant."
m.step("Gen.18.3")
# ‹אַל־נָא תַעֲבֹר מֵעַל› (“do-not please pass-over from-over”)
# ‹עַבְדֶּךָ› (“servant-you/your”)
# — Abraham speaks a demand — LET-NOT: pass-over(from-over-avdekha)
m.declare("avraham", "LET-NOT",
          "taavor(me_al_avdekha)")
# witness-grounded state (its own tier): spine_members_in_recorded_dispute
# on adonai_address
m.witness_state("adonai_address", "spine_members_in_recorded_dispute",
                cites=["Onkelos Genesis 18:3", "Bereshit Rabbah 48:10", "Onkelos Genesis 18:21", "Bereshit Rabbah 49:6"])
# witness-tier presupposed read: name_exception_and_adornment on
# adonai_im_na — read, not installed
m.witness_read("adonai_im_na", "name_exception_and_adornment",
                cites=["Shevuot 35b:8", "Shevuot 35b:9", "Shevuot 35b:10", "Nedarim 37b:7", "Nedarim 37b:8", "Nedarim 37b:9"])
# witness-tier presupposed read: hospitality_rank on al_na_taavor — read,
# not installed
m.witness_read("al_na_taavor", "hospitality_rank",
                cites=["Shabbat 127a:12", "Shabbat 127a:13", "Shabbat 127a:14"])

# -------------------------- Gen.18.4 · WATER_AND_THE_RARE_PASSIVE ----------
# ‹יֻקַּח־נָא מְעַט־מַיִם וְרַחֲצוּ› (“take please little waters and-lave”)
# ‹רַגְלֵיכֶם וְהִשָּׁעֲנוּ תַּחַת› (“foot-you/your(pl) and-support-
# one's-self under”)
# ‹הָעֵץ› (“the-tree”)
# "Let now a little water be fetched, and wash your feet, and recline
# yourselves under the tree."
m.step("Gen.18.4")
# ‹יֻקַּח־נָא מְעַט־מַיִם› (“take please little waters”)
# — Abraham speaks a demand — LET: take(little-waters)
m.declare("avraham", "LET",
          "yuqach(meat_mayim)")
# ‹וְרַחֲצוּ רַגְלֵיכֶם וְהִשָּׁעֲנוּ› (“and-lave foot-you/your(pl) and-
# support-one's-self”)
# ‹תַּחַת הָעֵץ› (“under the-tree”)
# — Abraham speaks a demand — LET: lave-and-support-one's-self(raglekhem)
m.declare("avraham", "LET",
          "rachatzu_ve_hishaanu(raglekhem)")

# -------------------------- Gen.18.5 · BREAD_PROMISED_ASSENT_GIVEN ---------
# ‹וְאֶקְחָה פַת־לֶחֶם וְסַעֲדוּ› (“and-take bit food and-suport”)
# ‹לִבְּכֶם אַחַר תַּעֲבֹרוּ› (“heart-you/your(pl) after pass-over”)
# ‹כִּי־עַל־כֵּן עֲבַרְתֶּם עַל־עַבְדְּכֶם› (“very-widely-used-as-a-relati
# above set-upright pass-over over servant-you/your(pl)”)
# ‹וַיֹּאמְרוּ כֵּן תַּעֲשֶׂה› (“and-say so make”)
# ‹כַּאֲשֶׁר דִּבַּרְתָּ› (“like-as/which speak”)
# "And I will fetch a morsel of bread, and stay ye your heart; after that ye
# shall pass on; forasmuch as ye are come to your servant.' And they said:
# 'So do, as thou hast said.'"
m.step("Gen.18.5")
# ‹וְאֶקְחָה פַת־לֶחֶם› (“and-take bit food”)
# — fact holds: and-eqchah-bit-food
m.fact("ve_eqchah_fat_lechem")
# ‹וְסַעֲדוּ לִבְּכֶם› (“and-suport heart-you/your(pl)”)
# — Abraham speaks a demand — LET: suport(libkhem)
m.declare("avraham", "LET",
          "saadu(libkhem)")
# ‹כֵּן תַּעֲשֶׂה כַּאֲשֶׁר› (“so make like-as/which”)
# ‹דִּבַּרְתָּ› (“speak”)
# — fact holds: set-upright-taaseh-like-which-speak
m.fact("ken_taaseh_ka_asher_dibarta")
# witness-tier presupposed read: visitors_without_the_inclination on
# single_bet_heart — read, not installed
m.witness_read("single_bet_heart", "visitors_without_the_inclination",
                cites=["Bereshit Rabbah 48:11"])
# witness-tier presupposed read: little_much on pat_lechem — read, not
# installed
m.witness_read("pat_lechem", "little_much",
                cites=["Bava Metzia 87a:2", "Bava Metzia 87a:3"])

# -------------------------- Gen.18.6 · THE_TRIPLE_TO_SARAH -----------------
# ‹וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה› (“and-hasten Abraham the-tent-ward”)
# ‹אֶל־שָׂרָה וַיֹּאמֶר מַהֲרִי› (“to Sarah and-say hasten”)
# ‹שְׁלֹשׁ סְאִים קֶמַח› (“three seah flour”)
# ‹סֹלֶת לוּשִׁי וַעֲשִׂי› (“flour knead and-make”)
# ‹עֻגוֹת› (“ash-cake”)
# "And Abraham hastened into the tent unto Sarah, and said: 'Make ready
# quickly three measures of fine meal, knead it, and make cakes.'"
m.step("Gen.18.6")
# ‹וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה› (“and-hasten Abraham the-tent-ward”)
# ‹אֶל־שָׂרָה› (“to Sarah”)
# — event: hurry — agent Abraham
m.event("hurry", agent="avraham")
# ‹מַהֲרִי שְׁלֹשׁ סְאִים› (“hasten three seah”)
# ‹קֶמַח סֹלֶת לוּשִׁי› (“flour flour knead”)
# ‹וַעֲשִׂי עֻגוֹת› (“and-make ash-cake”)
# — Abraham speaks a demand — LET: hasten-knead-and-make(ash-cake)
m.declare("avraham", "LET",
          "mahari_lushi_va_asi(ugot)")

# -------------------------- Gen.18.7 · THE_RUN_TO_THE_HERD -----------------
# ‹וְאֶל־הַבָּקָר רָץ אַבְרָהָם› (“and-to the-herd run Abraham”)
# ‹וַיִּקַּח בֶּן־בָּקָר רַךְ› (“and-take son herd tender”)
# ‹וָטוֹב וַיִּתֵּן אֶל־הַנַּעַר› (“and-good and-set to the-boy”)
# ‹וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ› (“and-hasten to-make obj-marker-him/its”)
# "And Abraham ran unto the herd, and fetched a calf tender and good, and
# gave it unto the servant; and he hastened to dress it."
m.step("Gen.18.7")
# ‹וַיִּקַּח בֶּן־בָּקָר רַךְ› (“and-take son herd tender”)
# ‹וָטוֹב› (“and-good”)
# — event: take — agent Abraham; theme son-herd
m.event("take", agent="avraham", themes=["ben_baqar"])
# ‹וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ› (“and-hasten to-make obj-marker-him/its”)
# — event: hurry-prepare — agent the-boy; theme son-herd
m.event("hurry_prepare", agent="ha_naar", themes=["ben_baqar"])

# -------------------------- Gen.18.8 · THE_DELIVERED_FEAST -----------------
# ‹וַיִּקַּח חֶמְאָה וְחָלָב› (“and-take curdled-milk and-milk”)
# ‹וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה› (“and-son the-herd which make”)
# ‹וַיִּתֵּן לִפְנֵיהֶם וְהוּא־עֹמֵד› (“and-set to-face-them/their and-he/it
# stand”)
# ‹עֲלֵיהֶם תַּחַת הָעֵץ› (“over-them/their under the-tree”)
# ‹וַיֹּאכֵלוּ› (“and-eat”)
# "And he took curd, and milk, and the calf which he had dressed, and set it
# before them; and he stood by them under the tree, and they did eat."
m.step("Gen.18.8")
# ‹וַיִּקַּח חֶמְאָה וְחָלָב› (“and-take curdled-milk and-milk”)
# ‹וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה› (“and-son the-herd which make”)
# ‹וַיִּתֵּן לִפְנֵיהֶם› (“and-set to-face-them/their”)
# — event: serve — agent Abraham; theme chemah-milk-and-son-the-herd
m.event("serve", agent="avraham", themes=["chemah_chalav_u_ven_ha_baqar"])
# ‹פַת־לֶחֶם … חֶמְאָה וְחָלָב› (“bit food … curdled-milk and-milk”)
# ‹וּבֶן־הַבָּקָר› (“and-son the-herd”)
# — spec-delta — spec said bit-food (a morsel fowl bread), delivery says
# chemah-milk-and-son-the-herd (curds, milk, the dressed calf)
m.spec_delta("fat_lechem (a morsel of bread)",
             "chemah_chalav_u_ven_ha_baqar (curds, milk, the dressed calf)")
# ‹וְהוּא־עֹמֵד עֲלֵיהֶם תַּחַת› (“and-he/it stand over-them/their under”)
# ‹הָעֵץ וַיֹּאכֵלוּ› (“the-tree and-eat”)
# — fact holds: and-he/it-stand-aleihem-under-the-tree
m.fact("ve_hu_omed_aleihem_tachat_ha_etz")

# -------------------------- Gen.18.9 · THE_FOURTH_WHERE --------------------
# ‹וַיֹּאמְרוּ אֵלָיו אַיֵּה› (“and-say to-him/its where?”)
# ‹שָׂרָה אִשְׁתֶּךָ וַיֹּאמֶר› (“Sarah woman-you/your and-say”)
# ‹הִנֵּה בָאֹהֶל› (“behold in-tent”)
# "And they said unto him: 'Where is Sarah thy wife?' And he said: 'Behold,
# in the tent.'"
m.step("Gen.18.9")
# ‹וַיֹּאמְרוּ אֵלָיו אַיֵּה› (“and-say to-him/its where?”)
# ‹שָׂרָה אִשְׁתֶּךָ› (“Sarah woman-you/your”)
# — event: say — agent three-man
m.event("say", agent="shelosha_anashim")
# witness-tier presupposed read: expound_the_dots_meta_rule on dotted_elav —
# read, not installed
m.witness_read("dotted_elav", "expound_the_dots_meta_rule",
                cites=["Bereshit Rabbah 48:15"])

# -------------------------- Gen.18.10 · THE_RETURN_PROMISE -----------------
# ‹וַיֹּאמֶר שׁוֹב אָשׁוּב› (“and-say return return”)
# ‹אֵלֶיךָ כָּעֵת חַיָּה› (“to-you/your like-time living”)
# ‹וְהִנֵּה־בֵן לְשָׂרָה אִשְׁתֶּךָ› (“and-behold son to-Sarah woman-
# you/your”)
# ‹וְשָׂרָה שֹׁמַעַת פֶּתַח› (“and-Sarah hear opening”)
# ‹הָאֹהֶל וְהוּא אַחֲרָיו› (“the-tent and-he/it after-him/its”)
# "And He said: 'I will certainly return unto thee when the season cometh
# round; and, lo, Sarah thy wife shall have a son.' And Sarah heard in the
# tent door, which was behind him.—"
m.step("Gen.18.10")
# ‹שׁוֹב אָשׁוּב אֵלֶיךָ› (“return return to-you/your”)
# ‹כָּעֵת חַיָּה וְהִנֵּה־בֵן› (“like-time living and-behold son”)
# ‹לְשָׂרָה› (“to-Sarah”)
# — fact holds: return-return-to-you-like-obj-marker-beast; behold-son-to-
# sarah
m.fact("shov_ashuv_elekha_ka_et_chayah",
       "hinneh_ven_le_sarah")
# ‹וְשָׂרָה שֹׁמַעַת פֶּתַח› (“and-Sarah hear opening”)
# ‹הָאֹהֶל› (“the-tent”)
# — event: hear — agent sarah
m.event("hear", agent="sarah")

# -------------------------- Gen.18.11 · THE_AGE_PARENTHESIS ----------------
# ‹וְאַבְרָהָם וְשָׂרָה זְקֵנִים› (“and-Abraham and-Sarah old”)
# ‹בָּאִים בַּיָּמִים חָדַל› (“come/bring in-day cease”)
# ‹לִהְיוֹת לְשָׂרָה אֹרַח› (“to-be to-Sarah well-trodden-road”)
# ‹כַּנָּשִׁים› (“like-woman”)
# "Now Abraham and Sarah were old, and well stricken in age; it had ceased
# to be with Sarah after the manner of women.—"
m.step("Gen.18.11")
# ‹זְקֵנִים בָּאִים בַּיָּמִים› (“old come/bring in-day”)
# ‹… חָדַל לִהְיוֹת לְשָׂרָה› (“cease to-be to-Sarah”)
# ‹אֹרַח כַּנָּשִׁים› (“well-trodden-road like-woman”)
# — fact holds: old-come/bring-in-the-seas; cease-well-trodden-road-like-
# nashim
m.fact("zeqenim_baim_ba_yamim",
       "chadal_orach_ka_nashim")
# ‹וְאַבְרָהָם וְשָׂרָה זְקֵנִים› (“and-Abraham and-Sarah old”)
# — note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.18.12 · THE_INTERIOR_LAUGH -----------------
# ‹וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ› (“and-laugh-outright Sarah in-nearest-
# part-her/its”)
# ‹לֵאמֹר אַחֲרֵי בְלֹתִי› (“to-say after fail-me/my”)
# ‹הָיְתָה־לִּי עֶדְנָה וַאדֹנִי› (“be to-me/my pleasure and-lord-me/my”)
# ‹זָקֵן› (“be-old”)
# "And Sarah laughed within herself, saying: 'After I am waxed old shall I
# have pleasure, my lord being old also?'"
m.step("Gen.18.12")
# ‹וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ› (“and-laugh-outright Sarah in-nearest-
# part-her/its”)
# ‹לֵאמֹר› (“to-say”)
# — event: say — agent sarah
m.event("say", agent="sarah")
# ‹אַחֲרֵי בְלֹתִי הָיְתָה־לִּי› (“after fail-me/my be to-me/my”)
# ‹עֶדְנָה וַאדֹנִי זָקֵן› (“pleasure and-lord-me/my be-old”)
# — fact holds: acharei-veloti-haytah-to-me-ednah-and-adoni-be-old
m.fact("acharei_veloti_haytah_li_ednah_va_adoni_zaqen")

# -------------------------- Gen.18.13 · THE_QUOTED_LAUGH -------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם› (“and-say YHWH to Abraham”)
# ‹לָמָּה זֶּה צָחֲקָה› (“to-what this laugh-outright”)
# ‹שָׂרָה לֵאמֹר הַאַף› (“Sarah to-say the-meaning-accession”)
# ‹אֻמְנָם אֵלֵד וַאֲנִי› (“verily bear-young and-I”)
# ‹זָקַנְתִּי› (“be-old”)
# "And the LORD said unto Abraham: 'Wherefore did Sarah laugh, saying: Shall
# I of a surety bear a child, who am old?"
m.step("Gen.18.13")
# ‹וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם› (“and-say YHWH to Abraham”)
# ‹לָמָּה זֶּה צָחֲקָה› (“to-what this laugh-outright”)
# ‹שָׂרָה› (“Sarah”)
# — event: say — agent the-LORD
m.event("say", agent="YHWH")
# witness-tier presupposed read: canon_edits_for_peace on altered_quotation
# — read, not installed
m.witness_read("altered_quotation", "canon_edits_for_peace",
                cites=["Bereshit Rabbah 48:18"])

# -------------------------- Gen.18.14 · TOO_WONDROUS -----------------------
# ‹הֲיִפָּלֵא מֵיְהוָה דָּבָר› (“the-perhaps-to-separate from-YHWH
# word/thing”)
# ‹לַמּוֹעֵד אָשׁוּב אֵלֶיךָ› (“to-seasons return to-you/your”)
# ‹כָּעֵת חַיָּה וּלְשָׂרָה› (“like-time living and-to-Sarah”)
# ‹בֵן› (“son”)
# "Is any thing too hard for the LORD. At the set time I will return unto
# thee, when the season cometh round, and Sarah shall have a son.'"
m.step("Gen.18.14")
# ‹הֲיִפָּלֵא מֵיְהוָה דָּבָר› (“the-perhaps-to-separate from-YHWH
# word/thing”)
# — fact holds: the-perhaps-to-separate-from-the-LORD-word/thing
m.fact("ha_yipale_me_YHWH_davar")
# ‹לַמּוֹעֵד אָשׁוּב אֵלֶיךָ› (“to-seasons return to-you/your”)
# ‹כָּעֵת חַיָּה וּלְשָׂרָה› (“like-time living and-to-Sarah”)
# ‹בֵן› (“son”)
# — fact holds: to-seasons-return-to-you-and-to-sarah-son
m.fact("la_moed_ashuv_elekha_u_le_sarah_ven")

# -------------------------- Gen.18.15 · THE_DENIAL_AND_THE_CORRECTION ------
# ‹וַתְּכַחֵשׁ שָׂרָה לֵאמֹר› (“and-be-untrue Sarah to-say”)
# ‹לֹא צָחַקְתִּי כִּי› (“not laugh-outright that”)
# ‹יָרֵאָה וַיֹּאמֶר לֹא› (“fear and-say not”)
# ‹כִּי צָחָקְתְּ› (“that laugh-outright”)
# "Then Sarah denied, saying: 'I laughed not'; for she was afraid. And He
# said: 'Nay; but thou didst laugh.'"
m.step("Gen.18.15")
# ‹וַתְּכַחֵשׁ שָׂרָה לֵאמֹר› (“and-be-untrue Sarah to-say”)
# ‹לֹא צָחַקְתִּי› (“not laugh-outright”)
# — event: deny — agent sarah
m.event("deny", agent="sarah")
# ‹וַיֹּאמֶר לֹא כִּי› (“and-say not that”)
# ‹צָחָקְתְּ› (“laugh-outright”)
# — event: correct — agent the-LORD
m.event("correct", agent="YHWH")

# -------------------------- Gen.18.16 · THE_TURN_TOWARD_SODOM --------------
# ‹וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים› (“and-arise from-there the-man”)
# ‹וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם› (“and-lean-out over face Sodom”)
# ‹וְאַבְרָהָם הֹלֵךְ עִמָּם› (“and-Abraham walk/go with-them/their”)
# ‹לְשַׁלְּחָם› (“to-send-them/their”)
# "And the men rose up from thence, and looked out toward Sodom; and Abraham
# went with them to bring them on the way."
m.step("Gen.18.16")
# ‹וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים› (“and-arise from-there the-man”)
# ‹וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם› (“and-lean-out over face Sodom”)
# — event: rise-look — agent three-man
m.event("rise_look", agent="shelosha_anashim")
# ‹סְדֹם› (“Sodom”)
# — reads without prior install (flag, not fix): Sodom
m.presupposed("sedom")
# ‹וְאַבְרָהָם הֹלֵךְ עִמָּם› (“and-Abraham walk/go with-them/their”)
# ‹לְשַׁלְּחָם› (“to-send-them/their”)
# — event: escort — agent Abraham
m.event("escort", agent="avraham")

# -------------------------- Gen.18.17 · THE_SOLILOQUY_OPENS ----------------
# ‹וַיהֹוָה אָמָר הַמְכַסֶּה› (“and-YHWH say the-plump”)
# ‹אֲנִי מֵאַבְרָהָם אֲשֶׁר› (“from-Abraham which”)
# ‹אֲנִי עֹשֶׂה› (“make”)
# "And the LORD said: 'Shall I hide from Abraham that which I am doing;"
m.step("Gen.18.17")
# ‹וַיהֹוָה אָמָר הַמְכַסֶּה› (“and-YHWH say the-plump”)
# ‹אֲנִי מֵאַבְרָהָם› (“from-Abraham”)
# — event: say — agent the-LORD
m.event("say", agent="YHWH")

# -------------------------- Gen.18.18 · THE_GUARD_FORMULA_RESOUNDED --------
# ‹וְאַבְרָהָם הָיוֹ יִהְיֶה› (“and-Abraham be be”)
# ‹לְגוֹי גָּדוֹל וְעָצוּם› (“to-nation great and-powerful”)
# ‹וְנִבְרְכוּ בוֹ כֹּל› (“and-bless in-him/its all”)
# ‹גּוֹיֵי הָאָרֶץ› (“nation the-earth”)
# "seeing that Abraham shall surely become a great and mighty nation, and
# all the nations of the earth shall be blessed in him?"
m.step("Gen.18.18")
# ‹הָיוֹ יִהְיֶה לְגוֹי› (“be be to-nation”)
# ‹גָּדוֹל וְעָצוּם וְנִבְרְכוּ› (“great and-powerful and-bless”)
# ‹בוֹ כֹּל גּוֹיֵי› (“in-him/its all nation”)
# ‹הָאָרֶץ› (“the-earth”)
# — fact holds: be-yihyeh-to-nation-great-and-powerful; and-nivrekhu-vo-all-
# goyei-the-earth
m.fact("hayo_yihyeh_le_goy_gadol_ve_atzum",
       "ve_nivrekhu_vo_kol_goyei_ha_aretz")

# -------------------------- Gen.18.19 · THE_HOUSE_CHARGE -------------------
# ‹כִּי יְדַעְתִּיו לְמַעַן› (“that know-him/its so-that”)
# ‹אֲשֶׁר יְצַוֶּה אֶת־בָּנָיו› (“which command obj-marker son-him/its”)
# ‹וְאֶת־בֵּיתוֹ אַחֲרָיו וְשָׁמְרוּ› (“and-obj-marker house-him/its after-
# him/its and-keep/guard”)
# ‹דֶּרֶךְ יְהוָה לַעֲשׂוֹת› (“way/road YHWH to-make”)
# ‹צְדָקָה וּמִשְׁפָּט לְמַעַן› (“rightness and-judgment so-that”)
# ‹הָבִיא יְהוָה עַל־אַבְרָהָם› (“come/bring YHWH over Abraham”)
# ‹אֵת אֲשֶׁר־דִּבֶּר עָלָיו› (“obj-marker which speak over-him/its”)
# "For I have known him, to the end that he may command his children and his
# household after him, that they may keep the way of the LORD, to do
# righteousness and justice; to the end that the LORD may bring upon Abraham
# that which He hath spoken of him.'"
m.step("Gen.18.19")
# ‹כִּי יְדַעְתִּיו› (“that know-him/its”)
# — fact holds: very-widely-used-as-a-relati-yedativ
m.fact("ki_yedativ")
# ‹וְשָׁמְרוּ דֶּרֶךְ יְהוָה› (“and-keep/guard way/road YHWH”)
# ‹לַעֲשׂוֹת צְדָקָה וּמִשְׁפָּט› (“to-make rightness and-judgment”)
# — fact holds: and-keep/guard-way/road-the-LORD-to-make-tzedaqah-and-
# judgment
m.fact("ve_shamru_derekh_YHWH_la_asot_tzedaqah_u_mishpat")
# ‹לְמַעַן הָבִיא יְהוָה› (“so-that come/bring YHWH”)
# ‹עַל־אַבְרָהָם אֵת אֲשֶׁר־דִּבֶּר› (“over Abraham obj-marker which speak”)
# ‹עָלָיו› (“over-him/its”)
# — fact holds: so-that-come/bring-the-LORD-over-Abraham-obj-marker-which-
# speak
m.fact("lemaan_havi_YHWH_al_avraham_et_asher_diber")
# witness-tier presupposed read: consolation_formula on ki_yedativ — read,
# not installed
m.witness_read("ki_yedativ", "consolation_formula",
                cites=["Ketubot 8b:9", "Ketubot 8b:10", "Ketubot 8b:11"])

# -------------------------- Gen.18.20 · THE_OUTCRY_DOUBLED -----------------
# ‹וַיֹּאמֶר יְהוָה זַעֲקַת› (“and-say YHWH shriek”)
# ‹סְדֹם וַעֲמֹרָה כִּי־רָבָּה› (“Sodom and-Gomorrah that many/great”)
# ‹וְחַטָּאתָם כִּי כָבְדָה› (“and-sin-offering-them/their that be-heavy”)
# ‹מְאֹד› (“very”)
# "And the LORD said: 'Verily, the cry of Sodom and Gomorrah is great, and,
# verily, their sin is exceeding grievous."
m.step("Gen.18.20")
# ‹וַיֹּאמֶר יְהוָה› (“and-say YHWH”)
# — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹זַעֲקַת סְדֹם וַעֲמֹרָה› (“shriek Sodom and-Gomorrah”)
# ‹כִּי־רָבָּה וְחַטָּאתָם כִּי› (“that many/great and-sin-offering-
# them/their that”)
# ‹כָבְדָה מְאֹד› (“be-heavy very”)
# — fact holds: shriek-Sodom-and-amorah-very-widely-used-as-a-relati-rabah;
# chatatam-very-widely-used-as-a-relati-khavdah-very
m.fact("zaaqat_sedom_va_amorah_ki_rabah",
       "chatatam_ki_khavdah_meod")
# ‹וַעֲמֹרָה› (“and-Gomorrah”)
# — reads without prior install (flag, not fix): Gomorrah
m.presupposed("amora")

# -------------------------- Gen.18.21 · THE_DESCEND_COHORTATIVE_RETURNS ----
# ‹אֵרֲדָה־נָּא וְאֶרְאֶה הַכְּצַעֲקָתָהּ› (“go-down please and-see the-
# like-shriek-her/its”)
# ‹הַבָּאָה אֵלַי עָשׂוּ› (“the-come/bring to-me/my make”)
# ‹כָּלָה וְאִם־לֹא אֵדָעָה› (“completion and-if not know”)
# "I will go down now, and see whether they have done altogether according
# to the cry of it, which is come unto Me; and if not, I will know.'"
m.step("Gen.18.21")
# ‹אֵרֲדָה־נָּא וְאֶרְאֶה› (“go-down please and-see”)
# — fact holds: eradah-please-and-ereh
m.fact("eradah_na_ve_ereh")
# ‹הַכְּצַעֲקָתָהּ הַבָּאָה אֵלַי› (“the-like-shriek-her/its the-come/bring
# to-me/my”)
# ‹עָשׂוּ כָּלָה וְאִם־לֹא› (“make completion and-if not”)
# ‹אֵדָעָה› (“know”)
# — fact holds: the-like-tzaaqatah-make-kalah; and-if-not-edaah
m.fact("ha_ke_tzaaqatah_asu_kalah",
       "ve_im_lo_edaah")

# -------------------------- Gen.18.22 · STILL_STANDING_BEFORE_YHWH ---------
# ‹וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים› (“and-turn from-there the-man”)
# ‹וַיֵּלְכוּ סְדֹמָה וְאַבְרָהָם› (“and-go Sodom-ward and-Abraham”)
# ‹עוֹדֶנּוּ עֹמֵד לִפְנֵי› (“still/again-him/its stand to-face”)
# ‹יְהוָה› (“YHWH”)
# "And the men turned from thence, and went toward Sodom; but Abraham stood
# yet before the LORD."
m.step("Gen.18.22")
# ‹וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים› (“and-turn from-there the-man”)
# ‹וַיֵּלְכוּ סְדֹמָה› (“and-go Sodom-ward”)
# — event: turn-go — agent three-man
m.event("turn_go", agent="shelosha_anashim")
# ‹וְאַבְרָהָם עוֹדֶנּוּ עֹמֵד› (“and-Abraham still/again-him/its stand”)
# ‹לִפְנֵי יְהוָה› (“to-face YHWH”)
# — fact holds: and-Abraham-odenu-stand-lifnei-the-LORD
m.fact("ve_avraham_odenu_omed_lifnei_YHWH")
# witness-tier presupposed read: scribal_emendation_claim on
# standing_before_the_lord — read, not installed
m.witness_read("standing_before_the_lord", "scribal_emendation_claim",
                cites=["Bereshit Rabbah 49:7"])

# -------------------------- Gen.18.23 · THE_APPROACH_AND_THE_FIFTY ---------
# ‹וַיִּגַּשׁ אַבְרָהָם וַיֹּאמַר› (“and-be Abraham and-say”)
# ‹הַאַף תִּסְפֶּה צַדִּיק› (“the-meaning-accession scrape-together just”)
# ‹עִם־רָשָׁע … אוּלַי יֵשׁ› (“with wrong … if-not there-is”)
# ‹חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ› (“fifty just in-midst”)
# ‹הָעִיר … חָלִלָה לְּךָ› (“the-city … literal-fora-profaned-thing-ward to-
# you/your”)
# ‹מֵעֲשֹׂת כַּדָּבָר הַזֶּה› (“from-make like-word/thing the-this”)
# ‹… הֲשֹׁפֵט כָּל־הָאָרֶץ לֹא› (“the-judge all the-earth not”)
# ‹יַעֲשֶׂה מִשְׁפָּט … וַיֹּאמֶר› (“make judgment … and-say”)
# ‹יְהוָה אִם־אֶמְצָא בִסְדֹם› (“YHWH if find in-Sodom”)
# ‹חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ› (“fifty just in-midst”)
# ‹הָעִיר וְנָשָׂאתִי לְכָל־הַמָּקוֹם› (“the-city and-lift/carry to-all the-
# place”)
# ‹בַּעֲבוּרָם› (“in-crossed-them/their”)
# "[EN-AID/JPS 18:23-26] And Abraham drew near, and said: 'Will You indeed
# sweep away the righteous with the wicked? Peradventure there are fifty
# righteous within the city... That be far from Thee... shall not the judge
# of all the earth do justly?' And the LORD said: 'If I find in Sodom fifty
# righteous within the city, then I will forgive all the place for their
# sake.'"
m.step("Gen.18.23")
# ‹וַיִּגַּשׁ אַבְרָהָם› (“and-be Abraham”)
# — event: approach — agent Abraham
m.event("approach", agent="avraham")
# ‹הַאַף תִּסְפֶּה צַדִּיק› (“the-meaning-accession scrape-together just”)
# ‹עִם־רָשָׁע אוּלַי יֵשׁ› (“with wrong if-not there-is”)
# ‹חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ› (“fifty just in-midst”)
# ‹הָעִיר› (“the-city”)
# — fact holds: the-meaning-accession-tispeh-tzaddiq-if-wrong; ulay-yesh-
# chamishim-tzaddiqim
m.fact("ha_af_tispeh_tzaddiq_im_rasha",
       "ulay_yesh_chamishim_tzaddiqim")
# ‹חָלִלָה לְּךָ … הֲשֹׁפֵט› (“literal-fora-profaned-thing-ward to-you/your
# … the-judge”)
# ‹כָּל־הָאָרֶץ לֹא יַעֲשֶׂה› (“all the-earth not make”)
# ‹מִשְׁפָּט› (“judgment”)
# — fact holds: chalilah-to-you-the-shofet-all-the-earth-not-yaaseh-judgment
m.fact("chalilah_lekha_ha_shofet_kol_ha_aretz_lo_yaaseh_mishpat")
# ‹אִם־אֶמְצָא בִסְדֹם חֲמִשִּׁים› (“if find in-Sodom fifty”)
# ‹צַדִּיקִם בְּתוֹךְ הָעִיר› (“just in-midst the-city”)
# ‹וְנָשָׂאתִי לְכָל־הַמָּקוֹם בַּעֲבוּרָם› (“and-lift/carry to-all the-
# place in-crossed-them/their”)
# — fact holds: if-emtza-chamishim-and-nasati-to-all-the-maqom
m.fact("im_emtza_chamishim_ve_nasati_le_khol_ha_maqom")
# witness-tier presupposed read: courtroom_procedure_on_a_cited_precedent on
# the_plea — read, not installed
m.witness_read("the_plea", "courtroom_procedure_on_a_cited_precedent",
                cites=["Bereshit Rabbah 39:6", "Bereshit Rabbah 49:10", "Bereshit Rabbah 49:12", "Bereshit Rabbah 49:13"])

# -------------------------- Gen.18.27 · THE_DESCENDING_LADDER --------------
# ‹וַיַּעַן אַבְרָהָם וַיֹּאמַר› (“and-eye Abraham and-say”)
# ‹הִנֵּה־נָא הוֹאַלְתִּי לְדַבֵּר› (“behold please yield to-speak”)
# ‹אֶל־אֲדֹנָי וְאָנֹכִי עָפָר› (“to Lord-me/my and-I dust”)
# ‹וָאֵפֶר … אוּלַי יַחְסְרוּן› (“and-ashes … if-not lack-ward”)
# ‹חֲמִשִּׁים הַצַּדִּיקִם חֲמִשָּׁה› (“fifty the-just five”)
# ‹… לֹא אַשְׁחִית אִם־אֶמְצָא› (“not decay if find”)
# ‹שָׁם אַרְבָּעִים וַחֲמִשָּׁה› (“there forty and-five”)
# ‹… אַל־נָא יִחַר לַאדֹנָי› (“to please glow to-lord-me/my”)
# ‹וַאֲדַבֵּרָה … אַךְ־הַפַּעַם אוּלַי› (“and-speak … indeed the-stroke if-
# not”)
# ‹יִמָּצְאוּן שָׁם עֲשָׂרָה› (“find-ward there ten”)
# ‹וַיֹּאמֶר לֹא אַשְׁחִית› (“and-say not decay”)
# ‹בַּעֲבוּר הָעֲשָׂרָה› (“for-the-sake-of the-ten”)
# "[EN-AID/JPS 18:27-32] And Abraham answered and said: 'Behold now, I have
# taken upon me to speak unto the Lord, who am but dust and ashes.
# Peradventure there shall lack five of the fifty righteous...' ...'Oh, let
# not the Lord be angry, and I will speak yet but this once. Peradventure
# ten shall be found there.' And He said: 'I will not destroy it for the
# ten's sake.'"
m.step("Gen.18.27")
# ‹וַיַּעַן אַבְרָהָם וַיֹּאמַר› (“and-eye Abraham and-say”)
# — event: answer — agent Abraham
m.event("answer", agent="avraham")
# ‹אַל־נָא יִחַר לַאדֹנָי› (“to please glow to-lord-me/my”)
# ‹וַאֲדַבֵּרָה› (“and-speak”)
# — Abraham speaks a demand — LET-NOT: yichar(to-adonai)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai)")
# ‹אַל־נָא יִחַר לַאדֹנָי› (“to please glow to-lord-me/my”)
# ‹וַאֲדַבְּרָה אַךְ־הַפַּעַם› (“and-speak indeed the-stroke”)
# — Abraham speaks a demand — LET-NOT: yichar(to-adonai, akh-the-paam)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai, akh_ha_paam)")
# ‹לֹא אַשְׁחִית … לֹא› (“not decay … not”)
# ‹אֶעֱשֶׂה … לֹא אַשְׁחִית› (“make … not decay”)
# ‹בַּעֲבוּר הָעֲשָׂרָה› (“for-the-sake-of the-ten”)
# — fact holds: not-ashchit-in-the-avur-the-asarah
m.fact("lo_ashchit_ba_avur_ha_asarah")

# -------------------------- Gen.18.33 · THE_EXIT_FORMULA -------------------
# ‹וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר› (“and-go YHWH like-as/which”)
# ‹כִּלָּה לְדַבֵּר אֶל־אַבְרָהָם› (“be-complete to-speak to Abraham”)
# ‹וְאַבְרָהָם שָׁב לִמְקֹמוֹ› (“and-Abraham return to-place-him/its”)
# "And the LORD went His way, as soon as He had left off speaking to
# Abraham; and Abraham returned unto his place."
m.step("Gen.18.33")
# ‹וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר› (“and-go YHWH like-as/which”)
# ‹כִּלָּה לְדַבֵּר› (“be-complete to-speak”)
# — event: depart — agent the-LORD
m.event("depart", agent="YHWH")
# ‹וְאַבְרָהָם שָׁב לִמְקֹמוֹ› (“and-Abraham return to-place-him/its”)
# — event: return — agent Abraham
m.event("return", agent="avraham")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shelosha_anashim'}
    assert m.presupposed_set() == {'amora', 'mamre', 'sedom'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['taavor(me_al_avdekha)', 'yuqach(meat_mayim)', 'rachatzu_ve_hishaanu(raglekhem)', 'saadu(libkhem)', 'mahari_lushi_va_asi(ugot)', 'yichar(le_adonai)', 'yichar(le_adonai, akh_ha_paam)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['yoshev_petach_ha_ohel_ke_chom_ha_yom', 've_eqchah_fat_lechem', 'ken_taaseh_ka_asher_dibarta', 've_hu_omed_aleihem_tachat_ha_etz', 'shov_ashuv_elekha_ka_et_chayah', 'hinneh_ven_le_sarah', 'zeqenim_baim_ba_yamim', 'chadal_orach_ka_nashim', 'acharei_veloti_haytah_li_ednah_va_adoni_zaqen', 'ha_yipale_me_YHWH_davar', 'la_moed_ashuv_elekha_u_le_sarah_ven', 'hayo_yihyeh_le_goy_gadol_ve_atzum', 've_nivrekhu_vo_kol_goyei_ha_aretz', 'ki_yedativ', 've_shamru_derekh_YHWH_la_asot_tzedaqah_u_mishpat', 'lemaan_havi_YHWH_al_avraham_et_asher_diber', 'zaaqat_sedom_va_amorah_ki_rabah', 'chatatam_ki_khavdah_meod', 'eradah_na_ve_ereh', 'ha_ke_tzaaqatah_asu_kalah', 've_im_lo_edaah', 've_avraham_odenu_omed_lifnei_YHWH', 'ha_af_tispeh_tzaddiq_im_rasha', 'ulay_yesh_chamishim_tzaddiqim', 'chalilah_lekha_ha_shofet_kol_ha_aretz_lo_yaaseh_mishpat', 'im_emtza_chamishim_ve_nasati_le_khol_ha_maqom', 'lo_ashchit_ba_avur_ha_asarah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 29
    assert sorted(m.WORLD["witnessed"]) == ['adonai_address']
    assert m.WORLD["witnessed"]['adonai_address']["cites"] == ['Onkelos Genesis 18:3', 'Bereshit Rabbah 48:10', 'Onkelos Genesis 18:21', 'Bereshit Rabbah 49:6']
    assert all('spine_members_in_recorded_dispute' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('heat_of_the_day', 'six_hours_by_comparison'), ('adonai_im_na', 'name_exception_and_adornment'), ('al_na_taavor', 'hospitality_rank'), ('single_bet_heart', 'visitors_without_the_inclination'), ('pat_lechem', 'little_much'), ('dotted_elav', 'expound_the_dots_meta_rule'), ('altered_quotation', 'canon_edits_for_peace'), ('ki_yedativ', 'consolation_formula'), ('standing_before_the_lord', 'scribal_emendation_claim'), ('the_plea', 'courtroom_procedure_on_a_cited_precedent')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 48:8', 'Bereshit Rabbah 48:7']
    assert all('six_hours_by_comparison' not in f for f in m.WORLD["facts"])
    assert 'heat_of_the_day' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Shevuot 35b:8', 'Shevuot 35b:9', 'Shevuot 35b:10', 'Nedarim 37b:7', 'Nedarim 37b:8', 'Nedarim 37b:9']
    assert all('name_exception_and_adornment' not in f for f in m.WORLD["facts"])
    assert 'adonai_im_na' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Shabbat 127a:12', 'Shabbat 127a:13', 'Shabbat 127a:14']
    assert all('hospitality_rank' not in f for f in m.WORLD["facts"])
    assert 'al_na_taavor' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 48:11']
    assert all('visitors_without_the_inclination' not in f for f in m.WORLD["facts"])
    assert 'single_bet_heart' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bava Metzia 87a:2', 'Bava Metzia 87a:3']
    assert all('little_much' not in f for f in m.WORLD["facts"])
    assert 'pat_lechem' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 48:15']
    assert all('expound_the_dots_meta_rule' not in f for f in m.WORLD["facts"])
    assert 'dotted_elav' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 48:18']
    assert all('canon_edits_for_peace' not in f for f in m.WORLD["facts"])
    assert 'altered_quotation' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Ketubot 8b:9', 'Ketubot 8b:10', 'Ketubot 8b:11']
    assert all('consolation_formula' not in f for f in m.WORLD["facts"])
    assert 'ki_yedativ' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 49:7']
    assert all('scribal_emendation_claim' not in f for f in m.WORLD["facts"])
    assert 'standing_before_the_lord' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 39:6', 'Bereshit Rabbah 49:10', 'Bereshit Rabbah 49:12', 'Bereshit Rabbah 49:13']
    assert all('courtroom_procedure_on_a_cited_precedent' not in f for f in m.WORLD["facts"])
    assert 'the_plea' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
