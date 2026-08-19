#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיֵּרָא אֵלָיו יְהוָה בְּאֵלֹנֵי מַמְרֵא וְהוּא יֹשֵׁב פֶּתַח־הָאֹהֶל
# כְּחֹם הַיּוֹם
# "And the LORD appeared unto him by the terebinths of Mamre, as he sat in
# the tent door in the heat of the day;"
m.step("Gen.18.1")
# ‹וַיֵּרָא אֵלָיו יְהוָה› (“and-see to-him/its YHWH”) — event: appear —
# agent the-LORD
m.event("appear", agent="YHWH")
# ‹בְּאֵלֹנֵי מַמְרֵא› (“in-oak Mamre”) — reads without prior install (flag,
# not fix): Mamre
m.presupposed("mamre")
# ‹וְהוּא יֹשֵׁב פֶּתַח־הָאֹהֶל כְּחֹם הַיּוֹם› (“and-he/it dwell/sit
# opening the-tent like-heat the-day”) — fact holds: dwell/sit-opening-the-
# tent-like-heat-the-day
m.fact("yoshev_petach_ha_ohel_ke_chom_ha_yom")

# -------------------------- Gen.18.2 · THREE_MEN_AND_THE_BOW ---------------
# וַיִּשָּׂא עֵינָיו וַיַּרְא וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים נִצָּבִים עָלָיו
# וַיַּרְא וַיָּרָץ לִקְרָאתָם מִפֶּתַח הָאֹהֶל וַיִּשְׁתַּחוּ אָרְצָה
# "and he lifted up his eyes and looked, and, lo, three men stood over
# against him; and when he saw them, he ran to meet them from the tent door,
# and bowed down to the earth,"
m.step("Gen.18.2")
# ‹וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים נִצָּבִים עָלָיו› (“and-behold three man
# stand over-him/its”) — the world gains: three-man
m.install("shelosha_anashim")
# ‹וַיָּרָץ לִקְרָאתָם› (“and-run to-encountering-them/their”) — event: run
# — agent Abraham
m.event("run", agent="avraham")
# ‹וַיִּשְׁתַּחוּ אָרְצָה› (“and-afflict earth-ward”) — event: bow — agent
# Abraham
m.event("bow", agent="avraham")

# -------------------------- Gen.18.3 · THE_DOOR_PETITION -------------------
# וַיֹּאמַר אֲדֹנָי אִם־נָא מָצָאתִי חֵן בְּעֵינֶיךָ אַל־נָא תַעֲבֹר מֵעַל
# עַבְדֶּךָ
# "and said: 'My lord, if now I have found favour in thy sight, pass not
# away, I pray thee, from thy servant."
m.step("Gen.18.3")
# ‹אַל־נָא תַעֲבֹר מֵעַל עַבְדֶּךָ› (“do-not please pass-over from-over
# servant-you/your”) — Abraham speaks a demand — LET-NOT: pass-over(from-
# over-avdekha)
m.declare("avraham", "LET-NOT",
          "taavor(me_al_avdekha)")

# -------------------------- Gen.18.4 · WATER_AND_THE_RARE_PASSIVE ----------
# יֻקַּח־נָא מְעַט־מַיִם וְרַחֲצוּ רַגְלֵיכֶם וְהִשָּׁעֲנוּ תַּחַת הָעֵץ
# "Let now a little water be fetched, and wash your feet, and recline
# yourselves under the tree."
m.step("Gen.18.4")
# ‹יֻקַּח־נָא מְעַט־מַיִם› (“take please little waters”) — Abraham speaks a
# demand — LET: take(little-waters)
m.declare("avraham", "LET",
          "yuqach(meat_mayim)")
# ‹וְרַחֲצוּ רַגְלֵיכֶם וְהִשָּׁעֲנוּ תַּחַת הָעֵץ› (“and-lave foot-
# you/your(pl) and-support-one's-self under the-tree”) — Abraham speaks a
# demand — LET: lave-and-support-one's-self(raglekhem)
m.declare("avraham", "LET",
          "rachatzu_ve_hishaanu(raglekhem)")

# -------------------------- Gen.18.5 · BREAD_PROMISED_ASSENT_GIVEN ---------
# וְאֶקְחָה פַת־לֶחֶם וְסַעֲדוּ לִבְּכֶם אַחַר תַּעֲבֹרוּ כִּי־עַל־כֵּן
# עֲבַרְתֶּם עַל־עַבְדְּכֶם וַיֹּאמְרוּ כֵּן תַּעֲשֶׂה כַּאֲשֶׁר דִּבַּרְתָּ
# "And I will fetch a morsel of bread, and stay ye your heart; after that ye
# shall pass on; forasmuch as ye are come to your servant.' And they said:
# 'So do, as thou hast said.'"
m.step("Gen.18.5")
# ‹וְאֶקְחָה פַת־לֶחֶם› (“and-take bit food”) — fact holds: and-eqchah-bit-
# food
m.fact("ve_eqchah_fat_lechem")
# ‹וְסַעֲדוּ לִבְּכֶם› (“and-suport heart-you/your(pl)”) — Abraham speaks a
# demand — LET: suport(libkhem)
m.declare("avraham", "LET",
          "saadu(libkhem)")
# ‹כֵּן תַּעֲשֶׂה כַּאֲשֶׁר דִּבַּרְתָּ› (“so make like-as/which speak”) —
# fact holds: set-upright-taaseh-like-which-speak
m.fact("ken_taaseh_ka_asher_dibarta")

# -------------------------- Gen.18.6 · THE_TRIPLE_TO_SARAH -----------------
# וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה אֶל־שָׂרָה וַיֹּאמֶר מַהֲרִי שְׁלֹשׁ סְאִים
# קֶמַח סֹלֶת לוּשִׁי וַעֲשִׂי עֻגוֹת
# "And Abraham hastened into the tent unto Sarah, and said: 'Make ready
# quickly three measures of fine meal, knead it, and make cakes.'"
m.step("Gen.18.6")
# ‹וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה אֶל־שָׂרָה› (“and-hasten Abraham the-tent-
# ward to Sarah”) — event: hurry — agent Abraham
m.event("hurry", agent="avraham")
# ‹מַהֲרִי שְׁלֹשׁ סְאִים קֶמַח סֹלֶת לוּשִׁי וַעֲשִׂי עֻגוֹת› (“hasten
# three seah flour flour knead and-make ash-cake”) — Abraham speaks a demand
# — LET: hasten-knead-and-make(ash-cake)
m.declare("avraham", "LET",
          "mahari_lushi_va_asi(ugot)")

# -------------------------- Gen.18.7 · THE_RUN_TO_THE_HERD -----------------
# וְאֶל־הַבָּקָר רָץ אַבְרָהָם וַיִּקַּח בֶּן־בָּקָר רַךְ וָטוֹב וַיִּתֵּן
# אֶל־הַנַּעַר וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ
# "And Abraham ran unto the herd, and fetched a calf tender and good, and
# gave it unto the servant; and he hastened to dress it."
m.step("Gen.18.7")
# ‹וַיִּקַּח בֶּן־בָּקָר רַךְ וָטוֹב› (“and-take son herd tender and-good”)
# — event: take — agent Abraham; theme son-herd
m.event("take", agent="avraham", themes=["ben_baqar"])
# ‹וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ› (“and-hasten to-make obj-marker-him/its”) —
# event: hurry-prepare — agent the-boy; theme son-herd
m.event("hurry_prepare", agent="ha_naar", themes=["ben_baqar"])

# -------------------------- Gen.18.8 · THE_DELIVERED_FEAST -----------------
# וַיִּקַּח חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה וַיִּתֵּן
# לִפְנֵיהֶם וְהוּא־עֹמֵד עֲלֵיהֶם תַּחַת הָעֵץ וַיֹּאכֵלוּ
# "And he took curd, and milk, and the calf which he had dressed, and set it
# before them; and he stood by them under the tree, and they did eat."
m.step("Gen.18.8")
# ‹וַיִּקַּח חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה וַיִּתֵּן
# לִפְנֵיהֶם› (“and-take curdled-milk and-milk and-son the-herd which make
# and-set to-face-them/their”) — event: serve — agent Abraham; theme chemah-
# milk-and-son-the-herd
m.event("serve", agent="avraham", themes=["chemah_chalav_u_ven_ha_baqar"])
# ‹פַת־לֶחֶם … חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר› (“bit food … curdled-milk
# and-milk and-son the-herd”) — spec-delta — spec said bit-food (a morsel
# fowl bread), delivery says chemah-milk-and-son-the-herd (curds, milk, the
# dressed calf)
m.spec_delta("fat_lechem (a morsel of bread)",
             "chemah_chalav_u_ven_ha_baqar (curds, milk, the dressed calf)")
# ‹וְהוּא־עֹמֵד עֲלֵיהֶם תַּחַת הָעֵץ וַיֹּאכֵלוּ› (“and-he/it stand over-
# them/their under the-tree and-eat”) — fact holds: and-he/it-stand-aleihem-
# under-the-tree
m.fact("ve_hu_omed_aleihem_tachat_ha_etz")

# -------------------------- Gen.18.9 · THE_FOURTH_WHERE --------------------
# וַיֹּאמְרוּ אֵלָיו אַיֵּה שָׂרָה אִשְׁתֶּךָ וַיֹּאמֶר הִנֵּה בָאֹהֶל
# "And they said unto him: 'Where is Sarah thy wife?' And he said: 'Behold,
# in the tent.'"
m.step("Gen.18.9")
# ‹וַיֹּאמְרוּ אֵלָיו אַיֵּה שָׂרָה אִשְׁתֶּךָ› (“and-say to-him/its where?
# Sarah woman-you/your”) — event: say — agent three-man
m.event("say", agent="shelosha_anashim")

# -------------------------- Gen.18.10 · THE_RETURN_PROMISE -----------------
# וַיֹּאמֶר שׁוֹב אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וְהִנֵּה־בֵן לְשָׂרָה
# אִשְׁתֶּךָ וְשָׂרָה שֹׁמַעַת פֶּתַח הָאֹהֶל וְהוּא אַחֲרָיו
# "And He said: 'I will certainly return unto thee when the season cometh
# round; and, lo, Sarah thy wife shall have a son.' And Sarah heard in the
# tent door, which was behind him.—"
m.step("Gen.18.10")
# ‹שׁוֹב אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וְהִנֵּה־בֵן לְשָׂרָה› (“return
# return to-you/your like-time living and-behold son to-Sarah”) — fact
# holds: return-return-to-you-like-obj-marker-beast; behold-son-to-sarah
m.fact("shov_ashuv_elekha_ka_et_chayah",
       "hinneh_ven_le_sarah")
# ‹וְשָׂרָה שֹׁמַעַת פֶּתַח הָאֹהֶל› (“and-Sarah hear opening the-tent”) —
# event: hear — agent sarah
m.event("hear", agent="sarah")

# -------------------------- Gen.18.11 · THE_AGE_PARENTHESIS ----------------
# וְאַבְרָהָם וְשָׂרָה זְקֵנִים בָּאִים בַּיָּמִים חָדַל לִהְיוֹת לְשָׂרָה
# אֹרַח כַּנָּשִׁים
# "Now Abraham and Sarah were old, and well stricken in age; it had ceased
# to be with Sarah after the manner of women.—"
m.step("Gen.18.11")
# ‹זְקֵנִים בָּאִים בַּיָּמִים … חָדַל לִהְיוֹת לְשָׂרָה אֹרַח כַּנָּשִׁים›
# (“old come/bring in-day … cease to-be to-Sarah well-trodden-road like-
# woman”) — fact holds: old-come/bring-in-the-seas; cease-well-trodden-road-
# like-nashim
m.fact("zeqenim_baim_ba_yamim",
       "chadal_orach_ka_nashim")
# ‹וְאַבְרָהָם וְשָׂרָה זְקֵנִים› (“and-Abraham and-Sarah old”) — note: zero
# events in this verse
m.note_zero_events()

# -------------------------- Gen.18.12 · THE_INTERIOR_LAUGH -----------------
# וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ לֵאמֹר אַחֲרֵי בְלֹתִי הָיְתָה־לִּי עֶדְנָה
# וַאדֹנִי זָקֵן
# "And Sarah laughed within herself, saying: 'After I am waxed old shall I
# have pleasure, my lord being old also?'"
m.step("Gen.18.12")
# ‹וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ לֵאמֹר› (“and-laugh-outright Sarah in-
# nearest-part-her/its to-say”) — event: say — agent sarah
m.event("say", agent="sarah")
# ‹אַחֲרֵי בְלֹתִי הָיְתָה־לִּי עֶדְנָה וַאדֹנִי זָקֵן› (“after fail-me/my
# be to-me/my pleasure and-lord-me/my be-old”) — fact holds: acharei-veloti-
# haytah-to-me-ednah-and-adoni-be-old
m.fact("acharei_veloti_haytah_li_ednah_va_adoni_zaqen")

# -------------------------- Gen.18.13 · THE_QUOTED_LAUGH -------------------
# וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם לָמָּה זֶּה צָחֲקָה שָׂרָה לֵאמֹר הַאַף
# אֻמְנָם אֵלֵד וַאֲנִי זָקַנְתִּי
# "And the LORD said unto Abraham: 'Wherefore did Sarah laugh, saying: Shall
# I of a surety bear a child, who am old?"
m.step("Gen.18.13")
# ‹וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם לָמָּה זֶּה צָחֲקָה שָׂרָה› (“and-say YHWH
# to Abraham to-what this laugh-outright Sarah”) — event: say — agent the-
# LORD
m.event("say", agent="YHWH")

# -------------------------- Gen.18.14 · TOO_WONDROUS -----------------------
# הֲיִפָּלֵא מֵיְהוָה דָּבָר לַמּוֹעֵד אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה
# וּלְשָׂרָה בֵן
# "Is any thing too hard for the LORD. At the set time I will return unto
# thee, when the season cometh round, and Sarah shall have a son.'"
m.step("Gen.18.14")
# ‹הֲיִפָּלֵא מֵיְהוָה דָּבָר› (“the-perhaps-to-separate from-YHWH
# word/thing”) — fact holds: the-perhaps-to-separate-from-the-LORD-
# word/thing
m.fact("ha_yipale_me_YHWH_davar")
# ‹לַמּוֹעֵד אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וּלְשָׂרָה בֵן› (“to-seasons
# return to-you/your like-time living and-to-Sarah son”) — fact holds: to-
# seasons-return-to-you-and-to-sarah-son
m.fact("la_moed_ashuv_elekha_u_le_sarah_ven")

# -------------------------- Gen.18.15 · THE_DENIAL_AND_THE_CORRECTION ------
# וַתְּכַחֵשׁ שָׂרָה לֵאמֹר לֹא צָחַקְתִּי כִּי יָרֵאָה וַיֹּאמֶר לֹא כִּי
# צָחָקְתְּ
# "Then Sarah denied, saying: 'I laughed not'; for she was afraid. And He
# said: 'Nay; but thou didst laugh.'"
m.step("Gen.18.15")
# ‹וַתְּכַחֵשׁ שָׂרָה לֵאמֹר לֹא צָחַקְתִּי› (“and-be-untrue Sarah to-say
# not laugh-outright”) — event: deny — agent sarah
m.event("deny", agent="sarah")
# ‹וַיֹּאמֶר לֹא כִּי צָחָקְתְּ› (“and-say not that laugh-outright”) —
# event: correct — agent the-LORD
m.event("correct", agent="YHWH")

# -------------------------- Gen.18.16 · THE_TURN_TOWARD_SODOM --------------
# וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם וְאַבְרָהָם
# הֹלֵךְ עִמָּם לְשַׁלְּחָם
# "And the men rose up from thence, and looked out toward Sodom; and Abraham
# went with them to bring them on the way."
m.step("Gen.18.16")
# ‹וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם› (“and-
# arise from-there the-man and-lean-out over face Sodom”) — event: rise-look
# — agent three-man
m.event("rise_look", agent="shelosha_anashim")
# ‹סְדֹם› (“Sodom”) — reads without prior install (flag, not fix): Sodom
m.presupposed("sedom")
# ‹וְאַבְרָהָם הֹלֵךְ עִמָּם לְשַׁלְּחָם› (“and-Abraham walk/go with-
# them/their to-send-them/their”) — event: escort — agent Abraham
m.event("escort", agent="avraham")

# -------------------------- Gen.18.17 · THE_SOLILOQUY_OPENS ----------------
# וַיהֹוָה אָמָר הַמְכַסֶּה אֲנִי מֵאַבְרָהָם אֲשֶׁר אֲנִי עֹשֶׂה
# "And the LORD said: 'Shall I hide from Abraham that which I am doing;"
m.step("Gen.18.17")
# ‹וַיהֹוָה אָמָר הַמְכַסֶּה אֲנִי מֵאַבְרָהָם› (“and-YHWH say the-plump
# from-Abraham”) — event: say — agent the-LORD
m.event("say", agent="YHWH")

# -------------------------- Gen.18.18 · THE_GUARD_FORMULA_RESOUNDED --------
# וְאַבְרָהָם הָיוֹ יִהְיֶה לְגוֹי גָּדוֹל וְעָצוּם וְנִבְרְכוּ בוֹ כֹּל
# גּוֹיֵי הָאָרֶץ
# "seeing that Abraham shall surely become a great and mighty nation, and
# all the nations of the earth shall be blessed in him?"
m.step("Gen.18.18")
# ‹הָיוֹ יִהְיֶה לְגוֹי גָּדוֹל וְעָצוּם וְנִבְרְכוּ בוֹ כֹּל גּוֹיֵי
# הָאָרֶץ› (“be be to-nation great and-powerful and-bless in-him/its all
# nation the-earth”) — fact holds: be-yihyeh-to-nation-great-and-powerful;
# and-nivrekhu-vo-all-goyei-the-earth
m.fact("hayo_yihyeh_le_goy_gadol_ve_atzum",
       "ve_nivrekhu_vo_kol_goyei_ha_aretz")

# -------------------------- Gen.18.19 · THE_HOUSE_CHARGE -------------------
# כִּי יְדַעְתִּיו לְמַעַן אֲשֶׁר יְצַוֶּה אֶת־בָּנָיו וְאֶת־בֵּיתוֹ
# אַחֲרָיו וְשָׁמְרוּ דֶּרֶךְ יְהוָה לַעֲשׂוֹת צְדָקָה וּמִשְׁפָּט לְמַעַן
# הָבִיא יְהוָה עַל־אַבְרָהָם אֵת אֲשֶׁר־דִּבֶּר עָלָיו
# "For I have known him, to the end that he may command his children and his
# household after him, that they may keep the way of the LORD, to do
# righteousness and justice; to the end that the LORD may bring upon Abraham
# that which He hath spoken of him.'"
m.step("Gen.18.19")
# ‹כִּי יְדַעְתִּיו› (“that know-him/its”) — fact holds: very-widely-used-
# as-a-relati-yedativ
m.fact("ki_yedativ")
# ‹וְשָׁמְרוּ דֶּרֶךְ יְהוָה לַעֲשׂוֹת צְדָקָה וּמִשְׁפָּט› (“and-keep/guard
# way/road YHWH to-make rightness and-judgment”) — fact holds: and-
# keep/guard-way/road-the-LORD-to-make-tzedaqah-and-judgment
m.fact("ve_shamru_derekh_YHWH_la_asot_tzedaqah_u_mishpat")
# ‹לְמַעַן הָבִיא יְהוָה עַל־אַבְרָהָם אֵת אֲשֶׁר־דִּבֶּר עָלָיו› (“so-that
# come/bring YHWH over Abraham obj-marker which speak over-him/its”) — fact
# holds: so-that-come/bring-the-LORD-over-Abraham-obj-marker-which-speak
m.fact("lemaan_havi_YHWH_al_avraham_et_asher_diber")

# -------------------------- Gen.18.20 · THE_OUTCRY_DOUBLED -----------------
# וַיֹּאמֶר יְהוָה זַעֲקַת סְדֹם וַעֲמֹרָה כִּי־רָבָּה וְחַטָּאתָם כִּי
# כָבְדָה מְאֹד
# "And the LORD said: 'Verily, the cry of Sodom and Gomorrah is great, and,
# verily, their sin is exceeding grievous."
m.step("Gen.18.20")
# ‹וַיֹּאמֶר יְהוָה› (“and-say YHWH”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹זַעֲקַת סְדֹם וַעֲמֹרָה כִּי־רָבָּה וְחַטָּאתָם כִּי כָבְדָה מְאֹד›
# (“shriek Sodom and-Gomorrah that many/great and-sin-offering-them/their
# that be-heavy very”) — fact holds: shriek-Sodom-and-amorah-very-widely-
# used-as-a-relati-rabah; chatatam-very-widely-used-as-a-relati-khavdah-very
m.fact("zaaqat_sedom_va_amorah_ki_rabah",
       "chatatam_ki_khavdah_meod")
# ‹וַעֲמֹרָה› (“and-Gomorrah”) — reads without prior install (flag, not
# fix): Gomorrah
m.presupposed("amora")

# -------------------------- Gen.18.21 · THE_DESCEND_COHORTATIVE_RETURNS ----
# אֵרֲדָה־נָּא וְאֶרְאֶה הַכְּצַעֲקָתָהּ הַבָּאָה אֵלַי עָשׂוּ כָּלָה
# וְאִם־לֹא אֵדָעָה
# "I will go down now, and see whether they have done altogether according
# to the cry of it, which is come unto Me; and if not, I will know.'"
m.step("Gen.18.21")
# ‹אֵרֲדָה־נָּא וְאֶרְאֶה› (“go-down please and-see”) — fact holds: eradah-
# please-and-ereh
m.fact("eradah_na_ve_ereh")
# ‹הַכְּצַעֲקָתָהּ הַבָּאָה אֵלַי עָשׂוּ כָּלָה וְאִם־לֹא אֵדָעָה› (“the-
# like-shriek-her/its the-come/bring to-me/my make completion and-if not
# know”) — fact holds: the-like-tzaaqatah-make-kalah; and-if-not-edaah
m.fact("ha_ke_tzaaqatah_asu_kalah",
       "ve_im_lo_edaah")

# -------------------------- Gen.18.22 · STILL_STANDING_BEFORE_YHWH ---------
# וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים וַיֵּלְכוּ סְדֹמָה וְאַבְרָהָם עוֹדֶנּוּ
# עֹמֵד לִפְנֵי יְהוָה
# "And the men turned from thence, and went toward Sodom; but Abraham stood
# yet before the LORD."
m.step("Gen.18.22")
# ‹וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים וַיֵּלְכוּ סְדֹמָה› (“and-turn from-there
# the-man and-go Sodom-ward”) — event: turn-go — agent three-man
m.event("turn_go", agent="shelosha_anashim")
# ‹וְאַבְרָהָם עוֹדֶנּוּ עֹמֵד לִפְנֵי יְהוָה› (“and-Abraham still/again-
# him/its stand to-face YHWH”) — fact holds: and-Abraham-odenu-stand-lifnei-
# the-LORD
m.fact("ve_avraham_odenu_omed_lifnei_YHWH")

# -------------------------- Gen.18.23 · THE_APPROACH_AND_THE_FIFTY ---------
# וַיִּגַּשׁ אַבְרָהָם וַיֹּאמַר הַאַף תִּסְפֶּה צַדִּיק עִם־רָשָׁע … אוּלַי
# יֵשׁ חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר … חָלִלָה לְּךָ מֵעֲשֹׂת
# כַּדָּבָר הַזֶּה … הֲשֹׁפֵט כָּל־הָאָרֶץ לֹא יַעֲשֶׂה מִשְׁפָּט …
# וַיֹּאמֶר יְהוָה אִם־אֶמְצָא בִסְדֹם חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר
# וְנָשָׂאתִי לְכָל־הַמָּקוֹם בַּעֲבוּרָם
# "[EN-AID/JPS 18:23-26] And Abraham drew near, and said: 'Will You indeed
# sweep away the righteous with the wicked? Peradventure there are fifty
# righteous within the city... That be far from Thee... shall not the judge
# of all the earth do justly?' And the LORD said: 'If I find in Sodom fifty
# righteous within the city, then I will forgive all the place for their
# sake.'"
m.step("Gen.18.23")
# ‹וַיִּגַּשׁ אַבְרָהָם› (“and-be Abraham”) — event: approach — agent
# Abraham
m.event("approach", agent="avraham")
# ‹הַאַף תִּסְפֶּה צַדִּיק עִם־רָשָׁע אוּלַי יֵשׁ חֲמִשִּׁים צַדִּיקִם
# בְּתוֹךְ הָעִיר› (“the-meaning-accession scrape-together just with wrong
# if-not there-is fifty just in-midst the-city”) — fact holds: the-meaning-
# accession-tispeh-tzaddiq-if-wrong; ulay-yesh-chamishim-tzaddiqim
m.fact("ha_af_tispeh_tzaddiq_im_rasha",
       "ulay_yesh_chamishim_tzaddiqim")
# ‹חָלִלָה לְּךָ … הֲשֹׁפֵט כָּל־הָאָרֶץ לֹא יַעֲשֶׂה מִשְׁפָּט› (“literal-
# fora-profaned-thing-ward to-you/your … the-judge all the-earth not make
# judgment”) — fact holds: chalilah-to-you-the-shofet-all-the-earth-not-
# yaaseh-judgment
m.fact("chalilah_lekha_ha_shofet_kol_ha_aretz_lo_yaaseh_mishpat")
# ‹אִם־אֶמְצָא בִסְדֹם חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר וְנָשָׂאתִי
# לְכָל־הַמָּקוֹם בַּעֲבוּרָם› (“if find in-Sodom fifty just in-midst the-
# city and-lift/carry to-all the-place in-crossed-them/their”) — fact holds:
# if-emtza-chamishim-and-nasati-to-all-the-maqom
m.fact("im_emtza_chamishim_ve_nasati_le_khol_ha_maqom")

# -------------------------- Gen.18.27 · THE_DESCENDING_LADDER --------------
# וַיַּעַן אַבְרָהָם וַיֹּאמַר הִנֵּה־נָא הוֹאַלְתִּי לְדַבֵּר אֶל־אֲדֹנָי
# וְאָנֹכִי עָפָר וָאֵפֶר … אוּלַי יַחְסְרוּן חֲמִשִּׁים הַצַּדִּיקִם
# חֲמִשָּׁה … לֹא אַשְׁחִית אִם־אֶמְצָא שָׁם אַרְבָּעִים וַחֲמִשָּׁה …
# אַל־נָא יִחַר לַאדֹנָי וַאֲדַבֵּרָה … אַךְ־הַפַּעַם אוּלַי יִמָּצְאוּן
# שָׁם עֲשָׂרָה וַיֹּאמֶר לֹא אַשְׁחִית בַּעֲבוּר הָעֲשָׂרָה
# "[EN-AID/JPS 18:27-32] And Abraham answered and said: 'Behold now, I have
# taken upon me to speak unto the Lord, who am but dust and ashes.
# Peradventure there shall lack five of the fifty righteous...' ...'Oh, let
# not the Lord be angry, and I will speak yet but this once. Peradventure
# ten shall be found there.' And He said: 'I will not destroy it for the
# ten's sake.'"
m.step("Gen.18.27")
# ‹וַיַּעַן אַבְרָהָם וַיֹּאמַר› (“and-eye Abraham and-say”) — event: answer
# — agent Abraham
m.event("answer", agent="avraham")
# ‹אַל־נָא יִחַר לַאדֹנָי וַאֲדַבֵּרָה› (“to please glow to-lord-me/my and-
# speak”) — Abraham speaks a demand — LET-NOT: yichar(to-adonai)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai)")
# ‹אַל־נָא יִחַר לַאדֹנָי וַאֲדַבְּרָה אַךְ־הַפַּעַם› (“to please glow to-
# lord-me/my and-speak indeed the-stroke”) — Abraham speaks a demand — LET-
# NOT: yichar(to-adonai, akh-the-paam)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai, akh_ha_paam)")
# ‹לֹא אַשְׁחִית … לֹא אֶעֱשֶׂה … לֹא אַשְׁחִית בַּעֲבוּר הָעֲשָׂרָה› (“not
# decay … not make … not decay for-the-sake-of the-ten”) — fact holds: not-
# ashchit-in-the-avur-the-asarah
m.fact("lo_ashchit_ba_avur_ha_asarah")

# -------------------------- Gen.18.33 · THE_EXIT_FORMULA -------------------
# וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר כִּלָּה לְדַבֵּר אֶל־אַבְרָהָם וְאַבְרָהָם שָׁב
# לִמְקֹמוֹ
# "And the LORD went His way, as soon as He had left off speaking to
# Abraham; and Abraham returned unto his place."
m.step("Gen.18.33")
# ‹וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר כִּלָּה לְדַבֵּר› (“and-go YHWH like-as/which
# be-complete to-speak”) — event: depart — agent the-LORD
m.event("depart", agent="YHWH")
# ‹וְאַבְרָהָם שָׁב לִמְקֹמוֹ› (“and-Abraham return to-place-him/its”) —
# event: return — agent Abraham
m.event("return", agent="avraham")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shelosha_anashim'}
    assert m.presupposed_set() == {'sedom', 'mamre', 'amora'}
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
