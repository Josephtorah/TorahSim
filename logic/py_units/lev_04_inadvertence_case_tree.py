#!/usr/bin/env python3
# =============================================================================
# lev_04_inadvertence_case_tree — 4:1-35
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_04_inadvertence_case_tree.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The inadvertence tree: four ranked cases, zero statutes (4:1-35) - the casuistic probe"""
from machine import Machine

m = Machine("lev_04_inadvertence_case_tree")

# -------------------------- Lev.4.1 · THE_FRAME ----------------------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Lev.4.1")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר› event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# ‹אֶל־מֹשֶׁה› reads without prior install (flag, not fix): Moses
m.presupposed("moshe")

# -------------------------- Lev.4.2 · THE_RELAY_AND_THE_INTAKE -------------
# דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל לֵאמֹר נֶפֶשׁ כִּי־תֶחֱטָא בִשְׁגָגָה מִכֹּל
# מִצְוֺת יְהוָה אֲשֶׁר לֹא תֵעָשֶׂינָה וְעָשָׂה מֵאַחַת מֵהֵנָּה
# "[EN-AID] Speak to the sons of Israel, saying: a soul, when it sins in
# inadvertence from any of the commandments of the LORD which shall not be
# done, and does from one of them -"
m.step("Lev.4.2")
# ‹דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל לֵאמֹר› the-LORD speaks a demand — LET:
# daber-to-bene-yisrael(Moses)
m.declare("YHWH", "LET",
          "daber_el_bene_yisrael(moshe)")
# ‹נֶפֶשׁ כִּי־תֶחֱטָא בִשְׁגָגָה מִכֹּל מִצְוֺת יְהוָה אֲשֶׁר לֹא
# תֵעָשֶׂינָה וְעָשָׂה מֵאַחַת מֵהֵנָּה› case nefesh, techeta-vi-shegaga-
# from-all-mitzvot routes to and-asa-from-achat-from-hena
m.case("nefesh, techeta_vi_shegaga_mi_kol_mitzvot", "ve_asa_me_achat_me_hena")

# -------------------------- Lev.4.3 · BRANCH_ONE_THE_ANOINTED --------------
# אִם הַכֹּהֵן הַמָּשִׁיחַ יֶחֱטָא לְאַשְׁמַת הָעָם וְהִקְרִיב עַל חַטָּאתוֹ
# אֲשֶׁר חָטָא פַּר בֶּן־בָּקָר תָּמִים לַיהוָה לְחַטָּאת
# "[EN-AID] If the anointed priest sins to the guilt of the people, he shall
# offer for his sin which he has sinned a bull, a son of the herd,
# unblemished, to the LORD for a sin-offering."
m.step("Lev.4.3")
# ‹אִם הַכֹּהֵן הַמָּשִׁיחַ יֶחֱטָא לְאַשְׁמַת הָעָם› case the-priest-the-
# mashiach, if-yecheta-to-ashmat-the-am routes to par-ben-baqar-tamim-to-
# chatat
m.case("ha_kohen_ha_mashiach, im_yecheta_le_ashmat_ha_am", "par_ben_baqar_tamim_le_chatat")

# -------------------------- Lev.4.4 · TO_THE_DOOR --------------------------
# וְהֵבִיא אֶת־הַפָּר אֶל־פֶּתַח אֹהֶל מוֹעֵד לִפְנֵי יְהוָה וְסָמַךְ
# אֶת־יָדוֹ עַל־רֹאשׁ הַפָּר וְשָׁחַט אֶת־הַפָּר לִפְנֵי יְהוָה
# "[EN-AID] And he shall bring the bull to the entrance of the tent of
# meeting before the LORD, and lean his hand on the bull's head, and
# slaughter the bull before the LORD."
m.step("Lev.4.4")
# ‹וְהֵבִיא אֶת־הַפָּר אֶל־פֶּתַח אֹהֶל מוֹעֵד לִפְנֵי יְהוָה› standing
# handler — if par-the-chatat then hevi-to-door-opening-ohel-moed ∧ samakh-
# his-hand-upon-rosh ∧ shachat-to-me-fene-the-LORD
m.handler("par_ha_chatat",
          "hevi_el_petach_ohel_moed ∧ samakh_yado_al_rosh ∧ shachat_li_fene_YHWH")

# -------------------------- Lev.4.5 · BLOOD_ENTERS -------------------------
# וְלָקַח הַכֹּהֵן הַמָּשִׁיחַ מִדַּם הַפָּר וְהֵבִיא אֹתוֹ אֶל־אֹהֶל מוֹעֵד
# "[EN-AID] And the anointed priest shall take of the bull's blood and bring
# it into the tent of meeting."
m.step("Lev.4.5")
# ‹וְלָקַח הַכֹּהֵן הַמָּשִׁיחַ מִדַּם הַפָּר וְהֵבִיא אֹתוֹ אֶל־אֹהֶל
# מוֹעֵד› standing handler — if blood-the-par then laqach-the-mashiach ∧
# hevi-it-to-ohel-moed
m.handler("dam_ha_par",
          "laqach_ha_mashiach ∧ hevi_oto_el_ohel_moed")

# -------------------------- Lev.4.6 · SEVEN_BEFORE_THE_VEIL ----------------
# וְטָבַל הַכֹּהֵן אֶת־אֶצְבָּעוֹ בַּדָּם וְהִזָּה מִן־הַדָּם שֶׁבַע
# פְּעָמִים לִפְנֵי יְהוָה אֶת־פְּנֵי פָּרֹכֶת הַקֹּדֶשׁ
# "[EN-AID] And the priest shall dip his finger in the blood and sprinkle of
# the blood seven times before the LORD, before the veil of the sanctuary."
m.step("Lev.4.6")
# ‹וְטָבַל הַכֹּהֵן אֶת־אֶצְבָּעוֹ בַּדָּם וְהִזָּה מִן־הַדָּם שֶׁבַע
# פְּעָמִים לִפְנֵי יְהוָה אֶת־פְּנֵי פָּרֹכֶת הַקֹּדֶשׁ› standing handler —
# if in-the-blood then taval-etzbao ∧ hiza-seven-peamim-pene-parokhet-the-
# qodesh
m.handler("ba_dam",
          "taval_etzbao ∧ hiza_sheva_peamim_et_pene_parokhet_ha_qodesh")

# -------------------------- Lev.4.7 · HORNS_AND_BASE -----------------------
# וְנָתַן הַכֹּהֵן מִן־הַדָּם עַל־קַרְנוֹת מִזְבַּח קְטֹרֶת הַסַּמִּים
# לִפְנֵי יְהוָה אֲשֶׁר בְּאֹהֶל מוֹעֵד וְאֵת כָּל־דַּם הַפָּר יִשְׁפֹּךְ
# אֶל־יְסוֹד מִזְבַּח הָעֹלָה אֲשֶׁר־פֶּתַח אֹהֶל מוֹעֵד
# "[EN-AID] And the priest shall put of the blood on the horns of the altar
# of fragrant incense before the LORD in the tent of meeting; and all the
# bull's blood he shall pour out at the base of the altar of burnt-offering
# which is at the entrance of the tent of meeting."
m.step("Lev.4.7")
# ‹וְנָתַן הַכֹּהֵן מִן־הַדָּם עַל־קַרְנוֹת מִזְבַּח קְטֹרֶת הַסַּמִּים
# לִפְנֵי יְהוָה אֲשֶׁר בְּאֹהֶל מוֹעֵד› standing handler — if from-the-
# blood then natan-upon-qarnot-mizbach-the-qetoret ∧ yishpokh-to-yesod-
# mizbach-the-ola
m.handler("min_ha_dam",
          "natan_al_qarnot_mizbach_ha_qetoret ∧ yishpokh_el_yesod_mizbach_ha_ola")

# -------------------------- Lev.4.8 · THE_FAT_LIFTED -----------------------
# וְאֶת־כָּל־חֵלֶב פַּר הַחַטָּאת יָרִים מִמֶּנּוּ אֶת־הַחֵלֶב הַמְכַסֶּה
# עַל־הַקֶּרֶב וְאֵת כָּל־הַחֵלֶב אֲשֶׁר עַל־הַקֶּרֶב
# "[EN-AID] And all the fat of the sin-offering bull he shall lift from it:
# the fat that covers the entrails, and all the fat that is on the
# entrails,"
m.step("Lev.4.8")
# ‹וְאֶת־כָּל־חֵלֶב פַּר הַחַטָּאת יָרִים מִמֶּנּוּ› standing handler — if
# chelev-par-the-chatat then yarim-the-chelev-the-mekhase
m.handler("chelev_par_ha_chatat",
          "yarim_et_ha_chelev_ha_mekhase")

# -------------------------- Lev.4.9 · KIDNEYS_AND_LOBE ---------------------
# וְאֵת שְׁתֵּי הַכְּלָיֹת וְאֶת־הַחֵלֶב אֲשֶׁר עֲלֵיהֶן אֲשֶׁר
# עַל־הַכְּסָלִים וְאֶת־הַיֹּתֶרֶת עַל־הַכָּבֵד עַל־הַכְּלָיוֹת יְסִירֶנָּה
# "[EN-AID] and the two kidneys and the fat that is on them, which is on the
# flanks, and the lobe on the liver - with the kidneys he shall remove it -"
m.step("Lev.4.9")
# ‹וְאֵת שְׁתֵּי הַכְּלָיֹת וְאֶת־הַחֵלֶב אֲשֶׁר עֲלֵיהֶן אֲשֶׁר
# עַל־הַכְּסָלִים וְאֶת־הַיֹּתֶרֶת עַל־הַכָּבֵד עַל־הַכְּלָיוֹת יְסִירֶנָּה›
# standing handler — if shete-the-kelayot-and-the-yoteret-upon-the-kaved
# then yesirena
m.handler("shete_ha_kelayot_ve_ha_yoteret_al_ha_kaved",
          "yesirena")

# -------------------------- Lev.4.10 · THE_FIRST_SUBROUTINE ----------------
# כַּאֲשֶׁר יוּרַם מִשּׁוֹר זֶבַח הַשְּׁלָמִים וְהִקְטִירָם הַכֹּהֵן עַל
# מִזְבַּח הָעֹלָה
# "[EN-AID] as it is lifted from the ox of the sacrifice of well-being - and
# the priest shall burn them on the altar of burnt-offering."
m.step("Lev.4.10")
# ‹כַּאֲשֶׁר יוּרַם מִשּׁוֹר זֶבַח הַשְּׁלָמִים וְהִקְטִירָם הַכֹּהֵן עַל
# מִזְבַּח הָעֹלָה› standing handler — if like-which-yuram-from-shor-zevach-
# the-shelamim then hiqtiram-upon-mizbach-the-ola
m.handler("ka_asher_yuram_mi_shor_zevach_ha_shelamim",
          "hiqtiram_al_mizbach_ha_ola")

# -------------------------- Lev.4.11 · THE_CARCASS_LIST --------------------
# וְאֶת־עוֹר הַפָּר וְאֶת־כָּל־בְּשָׂרוֹ עַל־רֹאשׁוֹ וְעַל־כְּרָעָיו
# וְקִרְבּוֹ וּפִרְשׁוֹ
# "[EN-AID] And the bull's hide and all its flesh, with its head and with
# its legs, and its entrails and its dung -"
m.step("Lev.4.11")
# ‹וְאֶת־עוֹר הַפָּר וְאֶת־כָּל־בְּשָׂרוֹ עַל־רֹאשׁוֹ וְעַל־כְּרָעָיו
# וְקִרְבּוֹ וּפִרְשׁוֹ› note: zero events in this verse
m.note_zero_events()

# -------------------------- Lev.4.12 · OUTSIDE_THE_CAMP --------------------
# וְהוֹצִיא אֶת־כָּל־הַפָּר אֶל־מִחוּץ לַמַּחֲנֶה אֶל־מָקוֹם טָהוֹר
# אֶל־שֶׁפֶךְ הַדֶּשֶׁן וְשָׂרַף אֹתוֹ עַל־עֵצִים בָּאֵשׁ עַל־שֶׁפֶךְ
# הַדֶּשֶׁן יִשָּׂרֵף
# "[EN-AID] he shall carry out the whole bull outside the camp to a clean
# place, to the pouring-place of the ashes, and burn it on wood in fire; on
# the pouring-place of the ashes it shall be burned."
m.step("Lev.4.12")
# ‹וְהוֹצִיא אֶת־כָּל־הַפָּר אֶל־מִחוּץ לַמַּחֲנֶה אֶל־מָקוֹם טָהוֹר
# אֶל־שֶׁפֶךְ הַדֶּשֶׁן וְשָׂרַף אֹתוֹ עַל־עֵצִים בָּאֵשׁ עַל־שֶׁפֶךְ
# הַדֶּשֶׁן יִשָּׂרֵף› standing handler — if all-the-par then hotzi-to-from-
# chutz-to-machane-to-maqom-pure ∧ saraf-upon-shefekh-the-deshen
m.handler("kol_ha_par",
          "hotzi_el_mi_chutz_la_machane_el_maqom_tahor ∧ saraf_al_shefekh_ha_deshen")

# -------------------------- Lev.4.13 · BRANCH_TWO_THE_CONGREGATION ---------
# וְאִם כָּל־עֲדַת יִשְׂרָאֵל יִשְׁגּוּ וְנֶעְלַם דָּבָר מֵעֵינֵי הַקָּהָל
# וְעָשׂוּ אַחַת מִכָּל־מִצְוֺת יְהוָה אֲשֶׁר לֹא־תֵעָשֶׂינָה וְאָשֵׁמוּ
# "[EN-AID] And if the whole congregation of Israel errs, and a thing is
# hidden from the eyes of the assembly, and they do one of all the
# commandments of the LORD which shall not be done, and become guilty -"
m.step("Lev.4.13")
# ‹וְאִם כָּל־עֲדַת יִשְׂרָאֵל יִשְׁגּוּ וְנֶעְלַם דָּבָר מֵעֵינֵי הַקָּהָל›
# case kal-adat-yisrael, yishgu-and-nelam-davar routes to and-ashemu
m.case("kal_adat_yisrael, yishgu_ve_nelam_davar", "ve_ashemu")

# -------------------------- Lev.4.14 · THE_SIN_BECOMES_KNOWN ---------------
# וְנוֹדְעָה הַחַטָּאת אֲשֶׁר חָטְאוּ עָלֶיהָ וְהִקְרִיבוּ הַקָּהָל פַּר
# בֶּן־בָּקָר לְחַטָּאת וְהֵבִיאוּ אֹתוֹ לִפְנֵי אֹהֶל מוֹעֵד
# "[EN-AID] and the sin which they sinned against it becomes known - then
# the assembly shall offer a bull, a son of the herd, for a sin-offering,
# and bring it before the tent of meeting."
m.step("Lev.4.14")
# ‹וְנוֹדְעָה הַחַטָּאת אֲשֶׁר חָטְאוּ עָלֶיהָ וְהִקְרִיבוּ הַקָּהָל פַּר
# בֶּן־בָּקָר לְחַטָּאת וְהֵבִיאוּ אֹתוֹ לִפְנֵי אֹהֶל מוֹעֵד› standing
# handler — if and-noda-the-chatat then hiqrivu-the-qahal-par ∧ heviu-it-to-
# me-fene-ohel-moed
m.handler("ve_noda_ha_chatat",
          "hiqrivu_ha_qahal_par ∧ heviu_oto_li_fene_ohel_moed")

# -------------------------- Lev.4.15 · THE_ELDERS_HANDS --------------------
# וְסָמְכוּ זִקְנֵי הָעֵדָה אֶת־יְדֵיהֶם עַל־רֹאשׁ הַפָּר לִפְנֵי יְהוָה
# וְשָׁחַט אֶת־הַפָּר לִפְנֵי יְהוָה
# "[EN-AID] And the elders of the congregation shall lean their hands on the
# bull's head before the LORD, and one shall slaughter the bull before the
# LORD."
m.step("Lev.4.15")
# ‹וְסָמְכוּ זִקְנֵי הָעֵדָה אֶת־יְדֵיהֶם עַל־רֹאשׁ הַפָּר לִפְנֵי יְהוָה›
# standing handler — if par-the-qahal then samkhu-ziqne-the-eda-yedehem ∧
# shachat-to-me-fene-the-LORD
m.handler("par_ha_qahal",
          "samkhu_ziqne_ha_eda_yedehem ∧ shachat_li_fene_YHWH")

# -------------------------- Lev.4.16 · THE_ANOINTED_CARRIES_AGAIN ----------
# וְהֵבִיא הַכֹּהֵן הַמָּשִׁיחַ מִדַּם הַפָּר אֶל־אֹהֶל מוֹעֵד
# "[EN-AID] And the anointed priest shall bring of the bull's blood into the
# tent of meeting."
m.step("Lev.4.16")
# ‹וְהֵבִיא הַכֹּהֵן הַמָּשִׁיחַ מִדַּם הַפָּר אֶל־אֹהֶל מוֹעֵד› standing
# handler — if blood-the-par then hevi-the-mashiach-to-ohel-moed
m.handler("dam_ha_par",
          "hevi_ha_mashiach_el_ohel_moed")

# -------------------------- Lev.4.17 · SEVEN_AGAIN -------------------------
# וְטָבַל הַכֹּהֵן אֶצְבָּעוֹ מִן־הַדָּם וְהִזָּה שֶׁבַע פְּעָמִים לִפְנֵי
# יְהוָה אֵת פְּנֵי הַפָּרֹכֶת
# "[EN-AID] And the priest shall dip his finger from the blood and sprinkle
# seven times before the LORD, before the veil."
m.step("Lev.4.17")
# ‹וְטָבַל הַכֹּהֵן אֶצְבָּעוֹ מִן־הַדָּם וְהִזָּה שֶׁבַע פְּעָמִים לִפְנֵי
# יְהוָה אֵת פְּנֵי הַפָּרֹכֶת› standing handler — if from-the-blood then
# taval-etzbao ∧ hiza-seven-peamim-pene-the-parokhet
m.handler("min_ha_dam",
          "taval_etzbao ∧ hiza_sheva_peamim_et_pene_ha_parokhet")

# -------------------------- Lev.4.18 · HORNS_AND_BASE_AGAIN ----------------
# וּמִן־הַדָּם יִתֵּן עַל־קַרְנֹת הַמִּזְבֵּחַ אֲשֶׁר לִפְנֵי יְהוָה אֲשֶׁר
# בְּאֹהֶל מוֹעֵד וְאֵת כָּל־הַדָּם יִשְׁפֹּךְ אֶל־יְסוֹד מִזְבַּח הָעֹלָה
# אֲשֶׁר־פֶּתַח אֹהֶל מוֹעֵד
# "[EN-AID] And of the blood he shall put on the horns of the altar which is
# before the LORD, which is in the tent of meeting; and all the blood he
# shall pour out at the base of the altar of burnt-offering which is at the
# entrance of the tent of meeting."
m.step("Lev.4.18")
# ‹וּמִן־הַדָּם יִתֵּן עַל־קַרְנֹת הַמִּזְבֵּחַ אֲשֶׁר לִפְנֵי יְהוָה אֲשֶׁר
# בְּאֹהֶל מוֹעֵד› standing handler — if and-from-the-blood then yiten-upon-
# qarnot-the-mizbecha ∧ yishpokh-to-yesod-mizbach-the-ola
m.handler("u_min_ha_dam",
          "yiten_al_qarnot_ha_mizbecha ∧ yishpokh_el_yesod_mizbach_ha_ola")

# -------------------------- Lev.4.19 · ALL_ITS_FAT -------------------------
# וְאֵת כָּל־חֶלְבּוֹ יָרִים מִמֶּנּוּ וְהִקְטִיר הַמִּזְבֵּחָה
# "[EN-AID] And all its fat he shall lift from it and burn on the altar."
m.step("Lev.4.19")
# ‹וְאֵת כָּל־חֶלְבּוֹ יָרִים מִמֶּנּוּ וְהִקְטִיר הַמִּזְבֵּחָה› standing
# handler — if all-chelbo then yarim-from-it ∧ hiqtir-the-mizbecha
m.handler("kol_chelbo",
          "yarim_mimenu ∧ hiqtir_ha_mizbecha")

# -------------------------- Lev.4.20 · AS_THE_FIRST_AND_FORGIVEN -----------
# וְעָשָׂה לַפָּר כַּאֲשֶׁר עָשָׂה לְפַר הַחַטָּאת כֵּן יַעֲשֶׂה־לּוֹ
# וְכִפֶּר עֲלֵהֶם הַכֹּהֵן וְנִסְלַח לָהֶם
# "[EN-AID] And he shall do to the bull as he did to the sin-offering bull -
# so shall he do to it; and the priest shall atone for them, and it shall be
# forgiven them."
m.step("Lev.4.20")
# ‹וְעָשָׂה לַפָּר כַּאֲשֶׁר עָשָׂה לְפַר הַחַטָּאת כֵּן יַעֲשֶׂה־לּוֹ
# וְכִפֶּר עֲלֵהֶם הַכֹּהֵן וְנִסְלַח לָהֶם› standing handler — if like-
# which-asa-to-far-the-chatat then ken-yaase-not ∧ kiper-the-priest ∧
# nislach-to-them
m.handler("ka_asher_asa_le_far_ha_chatat",
          "ken_yaase_lo ∧ kiper_ha_kohen ∧ nislach_lahem")

# -------------------------- Lev.4.21 · THE_FIRST_BULL_CITED ----------------
# וְהוֹצִיא אֶת־הַפָּר אֶל־מִחוּץ לַמַּחֲנֶה וְשָׂרַף אֹתוֹ כַּאֲשֶׁר שָׂרַף
# אֵת הַפָּר הָרִאשׁוֹן חַטַּאת הַקָּהָל הוּא
# "[EN-AID] And he shall carry the bull outside the camp and burn it as he
# burned the first bull: it is the sin-offering of the assembly."
m.step("Lev.4.21")
# ‹וְהוֹצִיא אֶת־הַפָּר אֶל־מִחוּץ לַמַּחֲנֶה וְשָׂרַף אֹתוֹ כַּאֲשֶׁר
# שָׂרַף אֵת הַפָּר הָרִאשׁוֹן חַטַּאת הַקָּהָל הוּא› standing handler — if
# like-which-saraf-the-par-the-rishon then hotzi-and-saraf-from-chutz-to-
# machane
m.handler("ka_asher_saraf_et_ha_par_ha_rishon",
          "hotzi_ve_saraf_mi_chutz_la_machane")

# -------------------------- Lev.4.22 · BRANCH_THREE_THE_LEADER -------------
# אֲשֶׁר נָשִׂיא יֶחֱטָא וְעָשָׂה אַחַת מִכָּל־מִצְוֺת יְהוָה אֱלֹהָיו
# אֲשֶׁר לֹא־תֵעָשֶׂינָה בִּשְׁגָגָה וְאָשֵׁם
# "[EN-AID] When a leader sins, and does one of all the commandments of the
# LORD his God which shall not be done, in inadvertence, and becomes guilty
# -"
m.step("Lev.4.22")
# ‹אֲשֶׁר נָשִׂיא יֶחֱטָא› case nasi, which-yecheta-bi-shegaga routes to
# and-ashem
m.case("nasi, asher_yecheta_bi_shegaga", "ve_ashem")

# -------------------------- Lev.4.23 · THE_KNOWLEDGE_TRIGGER ---------------
# אוֹ־הוֹדַע אֵלָיו חַטָּאתוֹ אֲשֶׁר חָטָא בָּהּ וְהֵבִיא אֶת־קָרְבָּנוֹ
# שְׂעִיר עִזִּים זָכָר תָּמִים
# "[EN-AID] or his sin which he sinned is made known to him - then he shall
# bring his offering: a goat of the goats, a male, unblemished."
m.step("Lev.4.23")
# ‹אוֹ־הוֹדַע אֵלָיו חַטָּאתוֹ אֲשֶׁר חָטָא בָּהּ› standing handler — if
# o-hoda-to-him-chatato then hevi-qarbano-seir-izim-male-tamim
m.handler("o_hoda_elav_chatato",
          "hevi_qarbano_seir_izim_zakhar_tamim")

# -------------------------- Lev.4.24 · AT_THE_OLAH_PLACE -------------------
# וְסָמַךְ יָדוֹ עַל־רֹאשׁ הַשָּׂעִיר וְשָׁחַט אֹתוֹ בִּמְקוֹם
# אֲשֶׁר־יִשְׁחַט אֶת־הָעֹלָה לִפְנֵי יְהוָה חַטָּאת הוּא
# "[EN-AID] And he shall lean his hand on the goat's head and slaughter it
# in the place where one slaughters the burnt-offering before the LORD: it
# is a sin-offering."
m.step("Lev.4.24")
# ‹וְסָמַךְ יָדוֹ עַל־רֹאשׁ הַשָּׂעִיר וְשָׁחַט אֹתוֹ בִּמְקוֹם
# אֲשֶׁר־יִשְׁחַט אֶת־הָעֹלָה לִפְנֵי יְהוָה› standing handler — if seir-
# the-chatat then samakh-his-hand ∧ shachat-bi-meqom-which-yishchat-the-ola
m.handler("seir_ha_chatat",
          "samakh_yado ∧ shachat_bi_meqom_asher_yishchat_et_ha_ola")

# -------------------------- Lev.4.25 · OUTER_HORNS -------------------------
# וְלָקַח הַכֹּהֵן מִדַּם הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת
# מִזְבַּח הָעֹלָה וְאֶת־דָּמוֹ יִשְׁפֹּךְ אֶל־יְסוֹד מִזְבַּח הָעֹלָה
# "[EN-AID] And the priest shall take of the sin-offering's blood with his
# finger and put it on the horns of the altar of burnt-offering; and its
# blood he shall pour out at the base of the altar of burnt-offering."
m.step("Lev.4.25")
# ‹וְלָקַח הַכֹּהֵן מִדַּם הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת
# מִזְבַּח הָעֹלָה וְאֶת־דָּמוֹ יִשְׁפֹּךְ אֶל־יְסוֹד מִזְבַּח הָעֹלָה›
# standing handler — if from-blood-the-chatat then natan-in-etzbao-upon-
# qarnot-mizbach-the-ola ∧ yishpokh-to-yesod
m.handler("mi_dam_ha_chatat",
          "natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod")

# -------------------------- Lev.4.26 · LEADER_FORGIVEN ---------------------
# וְאֶת־כָּל־חֶלְבּוֹ יַקְטִיר הַמִּזְבֵּחָה כְּחֵלֶב זֶבַח הַשְּׁלָמִים
# וְכִפֶּר עָלָיו הַכֹּהֵן מֵחַטָּאתוֹ וְנִסְלַח לוֹ
# "[EN-AID] And all its fat he shall burn on the altar like the fat of the
# sacrifice of well-being; and the priest shall atone for him from his sin,
# and he shall be forgiven."
m.step("Lev.4.26")
# ‹וְאֶת־כָּל־חֶלְבּוֹ יַקְטִיר הַמִּזְבֵּחָה כְּחֵלֶב זֶבַח הַשְּׁלָמִים
# וְכִפֶּר עָלָיו הַכֹּהֵן מֵחַטָּאתוֹ וְנִסְלַח לוֹ› standing handler — if
# all-chelbo-like-chelev-zevach-the-shelamim then yaqtir ∧ kiper ∧ nislach-
# not
m.handler("kol_chelbo_ke_chelev_zevach_ha_shelamim",
          "yaqtir ∧ kiper ∧ nislach_lo")

# -------------------------- Lev.4.27 · BRANCH_FOUR_THE_COMMONER ------------
# וְאִם־נֶפֶשׁ אַחַת תֶּחֱטָא בִשְׁגָגָה מֵעַם הָאָרֶץ בַּעֲשֹׂתָהּ אַחַת
# מִמִּצְוֺת יְהוָה אֲשֶׁר לֹא־תֵעָשֶׂינָה וְאָשֵׁם
# "[EN-AID] And if one soul of the people of the land sins in inadvertence,
# by doing one of the commandments of the LORD which shall not be done, and
# becomes guilty -"
m.step("Lev.4.27")
# ‹וְאִם־נֶפֶשׁ אַחַת תֶּחֱטָא בִשְׁגָגָה מֵעַם הָאָרֶץ› case nefesh-from-
# am-the-earth, techeta-vi-shegaga routes to and-ashem
m.case("nefesh_me_am_ha_aretz, techeta_vi_shegaga", "ve_ashem")

# -------------------------- Lev.4.28 · THE_SHE_GOAT ------------------------
# אוֹ הוֹדַע אֵלָיו חַטָּאתוֹ אֲשֶׁר חָטָא וְהֵבִיא קָרְבָּנוֹ שְׂעִירַת
# עִזִּים תְּמִימָה נְקֵבָה עַל־חַטָּאתוֹ אֲשֶׁר חָטָא
# "[EN-AID] or his sin which he sinned is made known to him - then he shall
# bring his offering: a she-goat of the goats, unblemished, a female, for
# his sin which he sinned."
m.step("Lev.4.28")
# ‹אוֹ הוֹדַע אֵלָיו חַטָּאתוֹ אֲשֶׁר חָטָא וְהֵבִיא קָרְבָּנוֹ שְׂעִירַת
# עִזִּים תְּמִימָה נְקֵבָה› standing handler — if o-hoda-to-him-chatato
# then hevi-qarbano-seirat-izim-temima-neqeva
m.handler("o_hoda_elav_chatato",
          "hevi_qarbano_seirat_izim_temima_neqeva")

# -------------------------- Lev.4.29 · LEAN_AND_SLAUGHTER ------------------
# וְסָמַךְ אֶת־יָדוֹ עַל רֹאשׁ הַחַטָּאת וְשָׁחַט אֶת־הַחַטָּאת בִּמְקוֹם
# הָעֹלָה
# "[EN-AID] And he shall lean his hand on the sin-offering's head and
# slaughter the sin-offering in the place of the burnt-offering."
m.step("Lev.4.29")
# ‹וְסָמַךְ אֶת־יָדוֹ עַל רֹאשׁ הַחַטָּאת וְשָׁחַט אֶת־הַחַטָּאת בִּמְקוֹם
# הָעֹלָה› standing handler — if the-chatat then samakh-his-hand ∧ shachat-
# bi-meqom-the-ola
m.handler("ha_chatat",
          "samakh_yado ∧ shachat_bi_meqom_ha_ola")

# -------------------------- Lev.4.30 · FINGER_HORNS_BASE -------------------
# וְלָקַח הַכֹּהֵן מִדָּמָהּ בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת מִזְבַּח
# הָעֹלָה וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ
# "[EN-AID] And the priest shall take of its blood with his finger and put
# it on the horns of the altar of burnt-offering; and all its blood he shall
# pour out at the base of the altar."
m.step("Lev.4.30")
# ‹וְלָקַח הַכֹּהֵן מִדָּמָהּ בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת מִזְבַּח
# הָעֹלָה וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ› standing
# handler — if from-damah then natan-in-etzbao-upon-qarnot-mizbach-the-ola ∧
# yishpokh-to-yesod-the-mizbecha
m.handler("mi_damah",
          "natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod_ha_mizbecha")

# -------------------------- Lev.4.31 · THE_PLEASING_AROMA ------------------
# וְאֶת־כָּל־חֶלְבָּהּ יָסִיר כַּאֲשֶׁר הוּסַר חֵלֶב מֵעַל זֶבַח
# הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן הַמִּזְבֵּחָה לְרֵיחַ נִיחֹחַ לַיהוָה
# וְכִפֶּר עָלָיו הַכֹּהֵן וְנִסְלַח לוֹ
# "[EN-AID] And all its fat he shall remove, as fat is removed from the
# sacrifice of well-being, and the priest shall burn it on the altar for a
# pleasing aroma to the LORD; and the priest shall atone for him, and he
# shall be forgiven."
m.step("Lev.4.31")
# ‹וְאֶת־כָּל־חֶלְבָּהּ יָסִיר כַּאֲשֶׁר הוּסַר חֵלֶב מֵעַל זֶבַח
# הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן הַמִּזְבֵּחָה לְרֵיחַ נִיחֹחַ לַיהוָה
# וְכִפֶּר עָלָיו הַכֹּהֵן וְנִסְלַח לוֹ› standing handler — if all-chelbah-
# like-which-husar-from-upon-zevach-the-shelamim then hiqtir-to-recha-
# nichocha ∧ kiper ∧ nislach-not
m.handler("kol_chelbah_ka_asher_husar_me_al_zevach_ha_shelamim",
          "hiqtir_le_recha_nichocha ∧ kiper ∧ nislach_lo")

# -------------------------- Lev.4.32 · THE_LAMB_ALTERNATIVE ----------------
# וְאִם־כֶּבֶשׂ יָבִיא קָרְבָּנוֹ לְחַטָּאת נְקֵבָה תְמִימָה יְבִיאֶנָּה
# "[EN-AID] And if he brings a lamb as his offering for a sin-offering, an
# unblemished female shall he bring."
m.step("Lev.4.32")
# ‹וְאִם־כֶּבֶשׂ יָבִיא קָרְבָּנוֹ לְחַטָּאת נְקֵבָה תְמִימָה יְבִיאֶנָּה›
# case keves, and-if-yavi-to-chatat routes to neqeva-temima-yeviena
m.case("keves, ve_im_yavi_le_chatat", "neqeva_temima_yeviena")

# -------------------------- Lev.4.33 · LEAN_AND_SLAUGHTER_HER --------------
# וְסָמַךְ אֶת־יָדוֹ עַל רֹאשׁ הַחַטָּאת וְשָׁחַט אֹתָהּ לְחַטָּאת בִּמְקוֹם
# אֲשֶׁר יִשְׁחַט אֶת־הָעֹלָה
# "[EN-AID] And he shall lean his hand on the sin-offering's head and
# slaughter it for a sin-offering in the place where one slaughters the
# burnt-offering."
m.step("Lev.4.33")
# ‹וְסָמַךְ אֶת־יָדוֹ עַל רֹאשׁ הַחַטָּאת וְשָׁחַט אֹתָהּ לְחַטָּאת
# בִּמְקוֹם אֲשֶׁר יִשְׁחַט אֶת־הָעֹלָה› standing handler — if the-chatat
# then samakh-his-hand ∧ shachat-her-to-chatat-bi-meqom-which-yishchat-the-
# ola
m.handler("ha_chatat",
          "samakh_yado ∧ shachat_otah_le_chatat_bi_meqom_asher_yishchat_et_ha_ola")

# -------------------------- Lev.4.34 · THE_LAST_BLOOD ----------------------
# וְלָקַח הַכֹּהֵן מִדַּם הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת
# מִזְבַּח הָעֹלָה וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ
# "[EN-AID] And the priest shall take of the sin-offering's blood with his
# finger and put it on the horns of the altar of burnt-offering; and all its
# blood he shall pour out at the base of the altar."
m.step("Lev.4.34")
# ‹וְלָקַח הַכֹּהֵן מִדַּם הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת
# מִזְבַּח הָעֹלָה וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ›
# standing handler — if from-blood-the-chatat then natan-in-etzbao-upon-
# qarnot ∧ yishpokh-kal-damah-to-yesod
m.handler("mi_dam_ha_chatat",
          "natan_be_etzbao_al_qarnot ∧ yishpokh_kal_damah_el_yesod")

# -------------------------- Lev.4.35 · THE_WALL_FOURTH_PARDON --------------
# וְאֶת־כָּל־חֶלְבָּה יָסִיר כַּאֲשֶׁר יוּסַר חֵלֶב־הַכֶּשֶׂב מִזֶּבַח
# הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן אֹתָם הַמִּזְבֵּחָה עַל אִשֵּׁי יְהוָה
# וְכִפֶּר עָלָיו הַכֹּהֵן עַל־חַטָּאתוֹ אֲשֶׁר־חָטָא וְנִסְלַח לוֹ
# "[EN-AID] And all its fat he shall remove, as the lamb's fat is removed
# from the sacrifice of well-being, and the priest shall burn them on the
# altar upon the fire-offerings of the LORD; and the priest shall atone for
# him, for his sin which he sinned, and he shall be forgiven."
m.step("Lev.4.35")
# ‹וְאֶת־כָּל־חֶלְבָּה יָסִיר כַּאֲשֶׁר יוּסַר חֵלֶב־הַכֶּשֶׂב מִזֶּבַח
# הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן אֹתָם הַמִּזְבֵּחָה עַל אִשֵּׁי יְהוָה
# וְכִפֶּר עָלָיו הַכֹּהֵן עַל־חַטָּאתוֹ אֲשֶׁר־חָטָא וְנִסְלַח לוֹ›
# standing handler — if all-chelbah-like-which-yusar-chelev-the-kesev then
# hiqtir-upon-ishe-the-LORD ∧ kiper ∧ nislach-not
m.handler("kol_chelbah_ka_asher_yusar_chelev_ha_kesev",
          "hiqtir_al_ishe_YHWH ∧ kiper ∧ nislach_lo")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'moshe'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['daber_el_bene_yisrael(moshe)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['case: nefesh, techeta_vi_shegaga_mi_kol_mitzvot -> ve_asa_me_achat_me_hena', 'case: ha_kohen_ha_mashiach, im_yecheta_le_ashmat_ha_am -> par_ben_baqar_tamim_le_chatat', 'handler: IF(par_ha_chatat) THEN(hevi_el_petach_ohel_moed ∧ samakh_yado_al_rosh ∧ shachat_li_fene_YHWH)', 'handler: IF(dam_ha_par) THEN(laqach_ha_mashiach ∧ hevi_oto_el_ohel_moed)', 'handler: IF(ba_dam) THEN(taval_etzbao ∧ hiza_sheva_peamim_et_pene_parokhet_ha_qodesh)', 'handler: IF(min_ha_dam) THEN(natan_al_qarnot_mizbach_ha_qetoret ∧ yishpokh_el_yesod_mizbach_ha_ola)', 'handler: IF(chelev_par_ha_chatat) THEN(yarim_et_ha_chelev_ha_mekhase)', 'handler: IF(shete_ha_kelayot_ve_ha_yoteret_al_ha_kaved) THEN(yesirena)', 'handler: IF(ka_asher_yuram_mi_shor_zevach_ha_shelamim) THEN(hiqtiram_al_mizbach_ha_ola)', 'handler: IF(kol_ha_par) THEN(hotzi_el_mi_chutz_la_machane_el_maqom_tahor ∧ saraf_al_shefekh_ha_deshen)', 'case: kal_adat_yisrael, yishgu_ve_nelam_davar -> ve_ashemu', 'handler: IF(ve_noda_ha_chatat) THEN(hiqrivu_ha_qahal_par ∧ heviu_oto_li_fene_ohel_moed)', 'handler: IF(par_ha_qahal) THEN(samkhu_ziqne_ha_eda_yedehem ∧ shachat_li_fene_YHWH)', 'handler: IF(dam_ha_par) THEN(hevi_ha_mashiach_el_ohel_moed)', 'handler: IF(min_ha_dam) THEN(taval_etzbao ∧ hiza_sheva_peamim_et_pene_ha_parokhet)', 'handler: IF(u_min_ha_dam) THEN(yiten_al_qarnot_ha_mizbecha ∧ yishpokh_el_yesod_mizbach_ha_ola)', 'handler: IF(kol_chelbo) THEN(yarim_mimenu ∧ hiqtir_ha_mizbecha)', 'handler: IF(ka_asher_asa_le_far_ha_chatat) THEN(ken_yaase_lo ∧ kiper_ha_kohen ∧ nislach_lahem)', 'handler: IF(ka_asher_saraf_et_ha_par_ha_rishon) THEN(hotzi_ve_saraf_mi_chutz_la_machane)', 'case: nasi, asher_yecheta_bi_shegaga -> ve_ashem', 'handler: IF(o_hoda_elav_chatato) THEN(hevi_qarbano_seir_izim_zakhar_tamim)', 'handler: IF(seir_ha_chatat) THEN(samakh_yado ∧ shachat_bi_meqom_asher_yishchat_et_ha_ola)', 'handler: IF(mi_dam_ha_chatat) THEN(natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod)', 'handler: IF(kol_chelbo_ke_chelev_zevach_ha_shelamim) THEN(yaqtir ∧ kiper ∧ nislach_lo)', 'case: nefesh_me_am_ha_aretz, techeta_vi_shegaga -> ve_ashem', 'handler: IF(o_hoda_elav_chatato) THEN(hevi_qarbano_seirat_izim_temima_neqeva)', 'handler: IF(ha_chatat) THEN(samakh_yado ∧ shachat_bi_meqom_ha_ola)', 'handler: IF(mi_damah) THEN(natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod_ha_mizbecha)', 'handler: IF(kol_chelbah_ka_asher_husar_me_al_zevach_ha_shelamim) THEN(hiqtir_le_recha_nichocha ∧ kiper ∧ nislach_lo)', 'case: keves, ve_im_yavi_le_chatat -> neqeva_temima_yeviena', 'handler: IF(ha_chatat) THEN(samakh_yado ∧ shachat_otah_le_chatat_bi_meqom_asher_yishchat_et_ha_ola)', 'handler: IF(mi_dam_ha_chatat) THEN(natan_be_etzbao_al_qarnot ∧ yishpokh_kal_damah_el_yesod)', 'handler: IF(kol_chelbah_ka_asher_yusar_chelev_ha_kesev) THEN(hiqtir_al_ishe_YHWH ∧ kiper ∧ nislach_lo)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 35
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
