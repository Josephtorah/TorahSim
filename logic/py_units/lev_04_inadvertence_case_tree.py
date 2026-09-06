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
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Lev.4.1")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# — event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# ‹אֶל־מֹשֶׁה› (“to Moses”)
# — reads without prior install (flag, not fix): Moses
m.presupposed("moshe")

# -------------------------- Lev.4.2 · THE_RELAY_AND_THE_INTAKE -------------
# ‹דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל› (“speak to son Israel”)
# ‹לֵאמֹר נֶפֶשׁ כִּי־תֶחֱטָא› (“to-say living-being that sin”)
# ‹בִשְׁגָגָה מִכֹּל מִצְוֺת› (“in-mistake from-all commandment”)
# ‹יְהוָה אֲשֶׁר לֹא› (“YHWH which not”)
# ‹תֵעָשֶׂינָה וְעָשָׂה מֵאַחַת› (“make and-make from-one”)
# ‹מֵהֵנָּה› (“from-themselves”)
# "[EN-AID] Speak to the sons of Israel, saying: a soul, when it sins in
# inadvertence from any of the commandments of the LORD which shall not be
# done, and does from one of them -"
m.step("Lev.4.2")
# ‹דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל› (“speak to son Israel”)
# ‹לֵאמֹר› (“to-say”)
# — the-LORD speaks a demand — LET: speak-to-son-Israel(Moses)
m.declare("YHWH", "LET",
          "daber_el_bene_yisrael(moshe)")
# ‹נֶפֶשׁ כִּי־תֶחֱטָא בִשְׁגָגָה› (“living-being that sin in-mistake”)
# ‹מִכֹּל מִצְוֺת יְהוָה› (“from-all commandment YHWH”)
# ‹אֲשֶׁר לֹא תֵעָשֶׂינָה› (“which not make”)
# ‹וְעָשָׂה מֵאַחַת מֵהֵנָּה› (“and-make from-one from-themselves”)
# — case living-being, sin-vi-shegaga-from-all-commandment routes to and-
# make-from-one-from-themselves
m.case("nefesh, techeta_vi_shegaga_mi_kol_mitzvot", "ve_asa_me_achat_me_hena")
# witness-tier presupposed read: knowledge_indexed_counts on
# aggregation_keys — read, not installed
m.witness_read("aggregation_keys", "knowledge_indexed_counts",
                cites=["Sifra, Vayikra Dibbura DeChovah, Chapter 1 7", "Sifra, Vayikra Dibbura DeChovah, Chapter 1 4", "Sifra, Vayikra Dibbura DeChovah, Chapter 1 5", "Sifra, Vayikra Dibbura DeChovah, Section 5 4", "Sifra, Vayikra Dibbura DeChovah, Section 7 8", "Sifra, Vayikra Dibbura DeChovah, Section 7 9", "Sifra, Vayikra Dibbura DeChovah, Chapter 1 8", "Sifra, Vayikra Dibbura DeChovah, Chapter 1 13"])

# -------------------------- Lev.4.3 · BRANCH_ONE_THE_ANOINTED --------------
# ‹אִם הַכֹּהֵן הַמָּשִׁיחַ› (“if the-priest the-anointed”)
# ‹יֶחֱטָא לְאַשְׁמַת הָעָם› (“sin to-guiltiness the-people”)
# ‹וְהִקְרִיב עַל חַטָּאתוֹ› (“and-bring-near over sin-offering-him/its”)
# ‹אֲשֶׁר חָטָא פַּר› (“which sin bullock”)
# ‹בֶּן־בָּקָר תָּמִים לַיהוָה› (“son herd entire to-YHWH”)
# ‹לְחַטָּאת› (“to-sin-offering”)
# "[EN-AID] If the anointed priest sins to the guilt of the people, he shall
# offer for his sin which he has sinned a bull, a son of the herd,
# unblemished, to the LORD for a sin-offering."
m.step("Lev.4.3")
# ‹אִם הַכֹּהֵן הַמָּשִׁיחַ› (“if the-priest the-anointed”)
# ‹יֶחֱטָא לְאַשְׁמַת הָעָם› (“sin to-guiltiness the-people”)
# — case the-priest-the-mashiach, if-sin-to-guiltiness-the-people routes to
# bullock-son-herd-entire-to-sin-offering
m.case("ha_kohen_ha_mashiach, im_yecheta_le_ashmat_ha_am", "par_ben_baqar_tamim_le_chatat")

# -------------------------- Lev.4.4 · TO_THE_DOOR --------------------------
# ‹וְהֵבִיא אֶת־הַפָּר אֶל־פֶּתַח› (“and-come/bring obj-marker the-bullock
# to opening”)
# ‹אֹהֶל מוֹעֵד לִפְנֵי› (“tent seasons to-face”)
# ‹יְהוָה וְסָמַךְ אֶת־יָדוֹ› (“YHWH and-lay obj-marker hand-him/its”)
# ‹עַל־רֹאשׁ הַפָּר וְשָׁחַט› (“over head the-bullock and-slaughter”)
# ‹אֶת־הַפָּר לִפְנֵי יְהוָה› (“obj-marker the-bullock to-face YHWH”)
# "[EN-AID] And he shall bring the bull to the entrance of the tent of
# meeting before the LORD, and lean his hand on the bull's head, and
# slaughter the bull before the LORD."
m.step("Lev.4.4")
# ‹וְהֵבִיא אֶת־הַפָּר אֶל־פֶּתַח› (“and-come/bring obj-marker the-bullock
# to opening”)
# ‹אֹהֶל מוֹעֵד לִפְנֵי› (“tent seasons to-face”)
# ‹יְהוָה› (“YHWH”)
# — standing handler — if bullock-the-sin-offering then come/bring-to-
# opening-tent-seasons ∧ lay-his-hand-over-head ∧ slaughter-to-me-fene-the-
# LORD
m.handler("par_ha_chatat",
          "hevi_el_petach_ohel_moed ∧ samakh_yado_al_rosh ∧ shachat_li_fene_YHWH")

# -------------------------- Lev.4.5 · BLOOD_ENTERS -------------------------
# ‹וְלָקַח הַכֹּהֵן הַמָּשִׁיחַ› (“and-take the-priest the-anointed”)
# ‹מִדַּם הַפָּר וְהֵבִיא› (“from-blood the-bullock and-come/bring”)
# ‹אֹתוֹ אֶל־אֹהֶל מוֹעֵד› (“obj-marker-him/its to tent seasons”)
# "[EN-AID] And the anointed priest shall take of the bull's blood and bring
# it into the tent of meeting."
m.step("Lev.4.5")
# ‹וְלָקַח הַכֹּהֵן הַמָּשִׁיחַ› (“and-take the-priest the-anointed”)
# ‹מִדַּם הַפָּר וְהֵבִיא› (“from-blood the-bullock and-come/bring”)
# ‹אֹתוֹ אֶל־אֹהֶל מוֹעֵד› (“obj-marker-him/its to tent seasons”)
# — standing handler — if blood-the-bullock then take-the-mashiach ∧
# come/bring-it-to-tent-seasons
m.handler("dam_ha_par",
          "laqach_ha_mashiach ∧ hevi_oto_el_ohel_moed")

# -------------------------- Lev.4.6 · SEVEN_BEFORE_THE_VEIL ----------------
# ‹וְטָבַל הַכֹּהֵן אֶת־אֶצְבָּעוֹ› (“and-dip the-priest obj-marker
# something-to-sieze-with-him/its”)
# ‹בַּדָּם וְהִזָּה מִן־הַדָּם› (“in-blood and-spirt from the-blood”)
# ‹שֶׁבַע פְּעָמִים לִפְנֵי› (“seven stroke to-face”)
# ‹יְהוָה אֶת־פְּנֵי פָּרֹכֶת› (“YHWH with face separatrix”)
# ‹הַקֹּדֶשׁ› (“the-holiness”)
# "[EN-AID] And the priest shall dip his finger in the blood and sprinkle of
# the blood seven times before the LORD, before the veil of the sanctuary."
m.step("Lev.4.6")
# ‹וְטָבַל הַכֹּהֵן אֶת־אֶצְבָּעוֹ› (“and-dip the-priest obj-marker
# something-to-sieze-with-him/its”)
# ‹בַּדָּם וְהִזָּה מִן־הַדָּם› (“in-blood and-spirt from the-blood”)
# ‹שֶׁבַע פְּעָמִים לִפְנֵי› (“seven stroke to-face”)
# ‹יְהוָה אֶת־פְּנֵי פָּרֹכֶת› (“YHWH with face separatrix”)
# ‹הַקֹּדֶשׁ› (“the-holiness”)
# — standing handler — if blood then dip-etzbao ∧ spirt-seven-stroke-obj-
# marker-face-separatrix-the-holiness
m.handler("ba_dam",
          "taval_etzbao ∧ hiza_sheva_peamim_et_pene_parokhet_ha_qodesh")
# witness-tier presupposed read: dip_per_sprinkle_staves on blood_algorithms
# — read, not installed
m.witness_read("blood_algorithms", "dip_per_sprinkle_staves",
                cites=["Sifra, Vayikra Dibbura DeChovah, Section 3 5", "Sifra, Vayikra Dibbura DeChovah, Section 3 7", "Sifra, Vayikra Dibbura DeChovah, Section 3 8", "Sifra, Vayikra Dibbura DeChovah, Section 3 10", "Sifra, Vayikra Dibbura DeChovah, Section 3 11", "Sifra, Vayikra Dibbura DeChovah, Section 3 13", "Sifra, Vayikra Dibbura DeChovah, Chapter 10 4", "Sifra, Vayikra Dibbura DeChovah, Chapter 9 1"])

# -------------------------- Lev.4.7 · HORNS_AND_BASE -----------------------
# ‹וְנָתַן הַכֹּהֵן מִן־הַדָּם› (“and-set the-priest from the-blood”)
# ‹עַל־קַרְנוֹת מִזְבַּח קְטֹרֶת› (“over horn altar fumigation”)
# ‹הַסַּמִּים לִפְנֵי יְהוָה› (“the-aroma to-face YHWH”)
# ‹אֲשֶׁר בְּאֹהֶל מוֹעֵד› (“which in-tent seasons”)
# ‹וְאֵת כָּל־דַּם הַפָּר› (“and-obj-marker all blood the-bullock”)
# ‹יִשְׁפֹּךְ אֶל־יְסוֹד מִזְבַּח› (“spill-forth to foundation altar”)
# ‹הָעֹלָה אֲשֶׁר־פֶּתַח אֹהֶל› (“the-burnt-offering which opening tent”)
# ‹מוֹעֵד› (“seasons”)
# "[EN-AID] And the priest shall put of the blood on the horns of the altar
# of fragrant incense before the LORD in the tent of meeting; and all the
# bull's blood he shall pour out at the base of the altar of burnt-offering
# which is at the entrance of the tent of meeting."
m.step("Lev.4.7")
# ‹וְנָתַן הַכֹּהֵן מִן־הַדָּם› (“and-set the-priest from the-blood”)
# ‹עַל־קַרְנוֹת מִזְבַּח קְטֹרֶת› (“over horn altar fumigation”)
# ‹הַסַּמִּים לִפְנֵי יְהוָה› (“the-aroma to-face YHWH”)
# ‹אֲשֶׁר בְּאֹהֶל מוֹעֵד› (“which in-tent seasons”)
# — standing handler — if from-the-blood then set-over-horn-altar-the-
# fumigation ∧ spill-forth-to-foundation-altar-the-burnt-offering
m.handler("min_ha_dam",
          "natan_al_qarnot_mizbach_ha_qetoret ∧ yishpokh_el_yesod_mizbach_ha_ola")

# -------------------------- Lev.4.8 · THE_FAT_LIFTED -----------------------
# ‹וְאֶת־כָּל־חֵלֶב פַּר הַחַטָּאת› (“and-obj-marker all fat bullock the-
# sin-offering”)
# ‹יָרִים מִמֶּנּוּ אֶת־הַחֵלֶב› (“rise-high from-us/our obj-marker the-
# fat”)
# ‹הַמְכַסֶּה עַל־הַקֶּרֶב וְאֵת› (“the-plump over the-nearest-part and-obj-
# marker”)
# ‹כָּל־הַחֵלֶב אֲשֶׁר עַל־הַקֶּרֶב› (“all the-fat which over the-nearest-
# part”)
# "[EN-AID] And all the fat of the sin-offering bull he shall lift from it:
# the fat that covers the entrails, and all the fat that is on the
# entrails,"
m.step("Lev.4.8")
# ‹וְאֶת־כָּל־חֵלֶב פַּר הַחַטָּאת› (“and-obj-marker all fat bullock the-
# sin-offering”)
# ‹יָרִים מִמֶּנּוּ› (“rise-high from-us/our”)
# — standing handler — if fat-bullock-the-sin-offering then rise-high-obj-
# marker-the-fat-the-plump
m.handler("chelev_par_ha_chatat",
          "yarim_et_ha_chelev_ha_mekhase")

# -------------------------- Lev.4.9 · KIDNEYS_AND_LOBE ---------------------
# ‹וְאֵת שְׁתֵּי הַכְּלָיֹת› (“and-obj-marker two the-kidney”)
# ‹וְאֶת־הַחֵלֶב אֲשֶׁר עֲלֵיהֶן› (“and-obj-marker the-fat which over-
# them/their”)
# ‹אֲשֶׁר עַל־הַכְּסָלִים וְאֶת־הַיֹּתֶרֶת› (“which over the-fatness and-
# obj-marker the-lobe”)
# ‹עַל־הַכָּבֵד עַל־הַכְּלָיוֹת יְסִירֶנָּה› (“over the-liver over the-
# kidney turn-aside-her/its”)
# "[EN-AID] and the two kidneys and the fat that is on them, which is on the
# flanks, and the lobe on the liver - with the kidneys he shall remove it -"
m.step("Lev.4.9")
# ‹וְאֵת שְׁתֵּי הַכְּלָיֹת› (“and-obj-marker two the-kidney”)
# ‹וְאֶת־הַחֵלֶב אֲשֶׁר עֲלֵיהֶן› (“and-obj-marker the-fat which over-
# them/their”)
# ‹אֲשֶׁר עַל־הַכְּסָלִים וְאֶת־הַיֹּתֶרֶת› (“which over the-fatness and-
# obj-marker the-lobe”)
# ‹עַל־הַכָּבֵד עַל־הַכְּלָיוֹת יְסִירֶנָּה› (“over the-liver over the-
# kidney turn-aside-her/its”)
# — standing handler — if two-the-kidney-and-the-lobe-over-the-liver then
# yesirena
m.handler("shete_ha_kelayot_ve_ha_yoteret_al_ha_kaved",
          "yesirena")

# -------------------------- Lev.4.10 · THE_FIRST_SUBROUTINE ----------------
# ‹כַּאֲשֶׁר יוּרַם מִשּׁוֹר› (“like-as/which rise-high from-bullock”)
# ‹זֶבַח הַשְּׁלָמִים וְהִקְטִירָם› (“sacrifice the-requital and-smoke-
# them/their”)
# ‹הַכֹּהֵן עַל מִזְבַּח› (“the-priest over altar”)
# ‹הָעֹלָה› (“the-burnt-offering”)
# "[EN-AID] as it is lifted from the ox of the sacrifice of well-being - and
# the priest shall burn them on the altar of burnt-offering."
m.step("Lev.4.10")
# ‹כַּאֲשֶׁר יוּרַם מִשּׁוֹר› (“like-as/which rise-high from-bullock”)
# ‹זֶבַח הַשְּׁלָמִים וְהִקְטִירָם› (“sacrifice the-requital and-smoke-
# them/their”)
# ‹הַכֹּהֵן עַל מִזְבַּח› (“the-priest over altar”)
# ‹הָעֹלָה› (“the-burnt-offering”)
# — standing handler — if like-which-rise-high-from-bullock-sacrifice-the-
# requital then hiqtiram-over-altar-the-burnt-offering
m.handler("ka_asher_yuram_mi_shor_zevach_ha_shelamim",
          "hiqtiram_al_mizbach_ha_ola")

# -------------------------- Lev.4.11 · THE_CARCASS_LIST --------------------
# ‹וְאֶת־עוֹר הַפָּר וְאֶת־כָּל־בְּשָׂרוֹ› (“and-obj-marker skin the-bullock
# and-obj-marker all flesh-him/its”)
# ‹עַל־רֹאשׁוֹ וְעַל־כְּרָעָיו וְקִרְבּוֹ› (“over head-him/its and-over leg-
# of-men-him/its and-nearest-part-him/its”)
# ‹וּפִרְשׁוֹ› (“and-excrement-him/its”)
# "[EN-AID] And the bull's hide and all its flesh, with its head and with
# its legs, and its entrails and its dung -"
m.step("Lev.4.11")
# ‹וְאֶת־עוֹר הַפָּר וְאֶת־כָּל־בְּשָׂרוֹ› (“and-obj-marker skin the-bullock
# and-obj-marker all flesh-him/its”)
# ‹עַל־רֹאשׁוֹ וְעַל־כְּרָעָיו וְקִרְבּוֹ› (“over head-him/its and-over leg-
# of-men-him/its and-nearest-part-him/its”)
# ‹וּפִרְשׁוֹ› (“and-excrement-him/its”)
# — note: zero events in this verse
m.note_zero_events()

# -------------------------- Lev.4.12 · OUTSIDE_THE_CAMP --------------------
# ‹וְהוֹצִיא אֶת־כָּל־הַפָּר אֶל־מִחוּץ› (“and-bring-forth obj-marker all
# the-bullock to from-outside”)
# ‹לַמַּחֲנֶה אֶל־מָקוֹם טָהוֹר› (“to-camp to place pure”)
# ‹אֶל־שֶׁפֶךְ הַדֶּשֶׁן וְשָׂרַף› (“to emptying-place the-fat and-be-on-
# fire”)
# ‹אֹתוֹ עַל־עֵצִים בָּאֵשׁ› (“obj-marker-him/its over tree in-fire”)
# ‹עַל־שֶׁפֶךְ הַדֶּשֶׁן יִשָּׂרֵף› (“over emptying-place the-fat be-on-
# fire”)
# "[EN-AID] he shall carry out the whole bull outside the camp to a clean
# place, to the pouring-place of the ashes, and burn it on wood in fire; on
# the pouring-place of the ashes it shall be burned."
m.step("Lev.4.12")
# ‹וְהוֹצִיא אֶת־כָּל־הַפָּר אֶל־מִחוּץ› (“and-bring-forth obj-marker all
# the-bullock to from-outside”)
# ‹לַמַּחֲנֶה אֶל־מָקוֹם טָהוֹר› (“to-camp to place pure”)
# ‹אֶל־שֶׁפֶךְ הַדֶּשֶׁן וְשָׂרַף› (“to emptying-place the-fat and-be-on-
# fire”)
# ‹אֹתוֹ עַל־עֵצִים בָּאֵשׁ› (“obj-marker-him/its over tree in-fire”)
# ‹עַל־שֶׁפֶךְ הַדֶּשֶׁן יִשָּׂרֵף› (“over emptying-place the-fat be-on-
# fire”)
# — standing handler — if all-the-bullock then bring-forth-to-from-outside-
# to-camp-to-place-pure ∧ be-on-fire-over-emptying-place-the-fat
m.handler("kol_ha_par",
          "hotzi_el_mi_chutz_la_machane_el_maqom_tahor ∧ saraf_al_shefekh_ha_deshen")

# -------------------------- Lev.4.13 · BRANCH_TWO_THE_CONGREGATION ---------
# ‹וְאִם כָּל־עֲדַת יִשְׂרָאֵל› (“and-if all congregation Israel”)
# ‹יִשְׁגּוּ וְנֶעְלַם דָּבָר› (“stray and-veil-from-sight word/thing”)
# ‹מֵעֵינֵי הַקָּהָל וְעָשׂוּ› (“from-eye the-assemblage and-make”)
# ‹אַחַת מִכָּל־מִצְוֺת יְהוָה› (“one from-all commandment YHWH”)
# ‹אֲשֶׁר לֹא־תֵעָשֶׂינָה וְאָשֵׁמוּ› (“which not make and-be-guilty”)
# "[EN-AID] And if the whole congregation of Israel errs, and a thing is
# hidden from the eyes of the assembly, and they do one of all the
# commandments of the LORD which shall not be done, and become guilty -"
m.step("Lev.4.13")
# ‹וְאִם כָּל־עֲדַת יִשְׂרָאֵל› (“and-if all congregation Israel”)
# ‹יִשְׁגּוּ וְנֶעְלַם דָּבָר› (“stray and-veil-from-sight word/thing”)
# ‹מֵעֵינֵי הַקָּהָל› (“from-eye the-assemblage”)
# — case all-congregation-Israel, stray-and-veil-from-sight-word/thing
# routes to and-be-guilty
m.case("kal_adat_yisrael, yishgu_ve_nelam_davar", "ve_ashemu")
# witness-tier presupposed read: unanimity_partial_located on
# court_error_machine — read, not installed
m.witness_read("court_error_machine", "unanimity_partial_located",
                cites=["Sifra, Vayikra Dibbura DeChovah, Section 4 2", "Sifra, Vayikra Dibbura DeChovah, Section 4 3", "Sifra, Vayikra Dibbura DeChovah, Section 4 4", "Sifra, Vayikra Dibbura DeChovah, Section 4 5", "Sifra, Vayikra Dibbura DeChovah, Section 4 7", "Sifra, Vayikra Dibbura DeChovah, Section 4 8", "Sifra, Vayikra Dibbura DeChovah, Section 4 10", "Sifra, Vayikra Dibbura DeChovah, Section 4 12"])

# -------------------------- Lev.4.14 · THE_SIN_BECOMES_KNOWN ---------------
# ‹וְנוֹדְעָה הַחַטָּאת אֲשֶׁר› (“and-know the-sin-offering which”)
# ‹חָטְאוּ עָלֶיהָ וְהִקְרִיבוּ› (“sin over-her/its and-bring-near”)
# ‹הַקָּהָל פַּר בֶּן־בָּקָר› (“the-assemblage bullock son herd”)
# ‹לְחַטָּאת וְהֵבִיאוּ אֹתוֹ› (“to-sin-offering and-come/bring obj-marker-
# him/its”)
# ‹לִפְנֵי אֹהֶל מוֹעֵד› (“to-face tent seasons”)
# "[EN-AID] and the sin which they sinned against it becomes known - then
# the assembly shall offer a bull, a son of the herd, for a sin-offering,
# and bring it before the tent of meeting."
m.step("Lev.4.14")
# ‹וְנוֹדְעָה הַחַטָּאת אֲשֶׁר› (“and-know the-sin-offering which”)
# ‹חָטְאוּ עָלֶיהָ וְהִקְרִיבוּ› (“sin over-her/its and-bring-near”)
# ‹הַקָּהָל פַּר בֶּן־בָּקָר› (“the-assemblage bullock son herd”)
# ‹לְחַטָּאת וְהֵבִיאוּ אֹתוֹ› (“to-sin-offering and-come/bring obj-marker-
# him/its”)
# ‹לִפְנֵי אֹהֶל מוֹעֵד› (“to-face tent seasons”)
# — standing handler — if and-know-the-sin-offering then bring-near-the-
# assemblage-bullock ∧ come/bring-it-to-me-fene-tent-seasons
m.handler("ve_noda_ha_chatat",
          "hiqrivu_ha_qahal_par ∧ heviu_oto_li_fene_ohel_moed")
# witness-tier presupposed read: four_positions on tribal_arithmetic — read,
# not installed
m.witness_read("tribal_arithmetic", "four_positions",
                cites=["Sifra, Vayikra Dibbura DeChovah, Section 4 13", "Sifra, Vayikra Dibbura DeChovah, Section 4 14", "Sifra, Vayikra Dibbura DeChovah, Section 4 15", "Sifra, Vayikra Dibbura DeChovah, Section 4 16", "Sifra, Vayikra Dibbura DeChovah, Section 4 17"])

# -------------------------- Lev.4.15 · THE_ELDERS_HANDS --------------------
# ‹וְסָמְכוּ זִקְנֵי הָעֵדָה› (“and-lay elders-of the-congregation”)
# ‹אֶת־יְדֵיהֶם עַל־רֹאשׁ הַפָּר› (“obj-marker hand-them/their over head
# the-bullock”)
# ‹לִפְנֵי יְהוָה וְשָׁחַט› (“to-face YHWH and-slaughter”)
# ‹אֶת־הַפָּר לִפְנֵי יְהוָה› (“obj-marker the-bullock to-face YHWH”)
# "[EN-AID] And the elders of the congregation shall lean their hands on the
# bull's head before the LORD, and one shall slaughter the bull before the
# LORD."
m.step("Lev.4.15")
# ‹וְסָמְכוּ זִקְנֵי הָעֵדָה› (“and-lay elders-of the-congregation”)
# ‹אֶת־יְדֵיהֶם עַל־רֹאשׁ הַפָּר› (“obj-marker hand-them/their over head
# the-bullock”)
# ‹לִפְנֵי יְהוָה› (“to-face YHWH”)
# — standing handler — if bullock-the-assemblage then lay-elders-of-the-
# congregation-yedehem ∧ slaughter-to-me-fene-the-LORD
m.handler("par_ha_qahal",
          "samkhu_ziqne_ha_eda_yedehem ∧ shachat_li_fene_YHWH")
# witness-tier presupposed read: five_or_three on elders_quorum — read, not
# installed
m.witness_read("elders_quorum", "five_or_three",
                cites=["Sifra, Vayikra Dibbura DeChovah, Chapter 6 1", "Sifra, Vayikra Dibbura DeChovah, Chapter 6 2", "Sifra, Vayikra Dibbura DeChovah, Chapter 6 3"])

# -------------------------- Lev.4.16 · THE_ANOINTED_CARRIES_AGAIN ----------
# ‹וְהֵבִיא הַכֹּהֵן הַמָּשִׁיחַ› (“and-come/bring the-priest the-anointed”)
# ‹מִדַּם הַפָּר אֶל־אֹהֶל› (“from-blood the-bullock to tent”)
# ‹מוֹעֵד› (“seasons”)
# "[EN-AID] And the anointed priest shall bring of the bull's blood into the
# tent of meeting."
m.step("Lev.4.16")
# ‹וְהֵבִיא הַכֹּהֵן הַמָּשִׁיחַ› (“and-come/bring the-priest the-anointed”)
# ‹מִדַּם הַפָּר אֶל־אֹהֶל› (“from-blood the-bullock to tent”)
# ‹מוֹעֵד› (“seasons”)
# — standing handler — if blood-the-bullock then come/bring-the-mashiach-to-
# tent-seasons
m.handler("dam_ha_par",
          "hevi_ha_mashiach_el_ohel_moed")

# -------------------------- Lev.4.17 · SEVEN_AGAIN -------------------------
# ‹וְטָבַל הַכֹּהֵן אֶצְבָּעוֹ› (“and-dip the-priest something-to-sieze-
# with-him/its”)
# ‹מִן־הַדָּם וְהִזָּה שֶׁבַע› (“from the-blood and-spirt seven”)
# ‹פְּעָמִים לִפְנֵי יְהוָה› (“stroke to-face YHWH”)
# ‹אֵת פְּנֵי הַפָּרֹכֶת› (“with face the-separatrix”)
# "[EN-AID] And the priest shall dip his finger from the blood and sprinkle
# seven times before the LORD, before the veil."
m.step("Lev.4.17")
# ‹וְטָבַל הַכֹּהֵן אֶצְבָּעוֹ› (“and-dip the-priest something-to-sieze-
# with-him/its”)
# ‹מִן־הַדָּם וְהִזָּה שֶׁבַע› (“from the-blood and-spirt seven”)
# ‹פְּעָמִים לִפְנֵי יְהוָה› (“stroke to-face YHWH”)
# ‹אֵת פְּנֵי הַפָּרֹכֶת› (“with face the-separatrix”)
# — standing handler — if from-the-blood then dip-etzbao ∧ spirt-seven-
# stroke-obj-marker-face-the-separatrix
m.handler("min_ha_dam",
          "taval_etzbao ∧ hiza_sheva_peamim_et_pene_ha_parokhet")

# -------------------------- Lev.4.18 · HORNS_AND_BASE_AGAIN ----------------
# ‹וּמִן־הַדָּם יִתֵּן עַל־קַרְנֹת› (“and-from the-blood set over horn”)
# ‹הַמִּזְבֵּחַ אֲשֶׁר לִפְנֵי› (“the-altar which to-face”)
# ‹יְהוָה אֲשֶׁר בְּאֹהֶל› (“YHWH which in-tent”)
# ‹מוֹעֵד וְאֵת כָּל־הַדָּם› (“seasons and-obj-marker all the-blood”)
# ‹יִשְׁפֹּךְ אֶל־יְסוֹד מִזְבַּח› (“spill-forth to foundation altar”)
# ‹הָעֹלָה אֲשֶׁר־פֶּתַח אֹהֶל› (“the-burnt-offering which opening tent”)
# ‹מוֹעֵד› (“seasons”)
# "[EN-AID] And of the blood he shall put on the horns of the altar which is
# before the LORD, which is in the tent of meeting; and all the blood he
# shall pour out at the base of the altar of burnt-offering which is at the
# entrance of the tent of meeting."
m.step("Lev.4.18")
# ‹וּמִן־הַדָּם יִתֵּן עַל־קַרְנֹת› (“and-from the-blood set over horn”)
# ‹הַמִּזְבֵּחַ אֲשֶׁר לִפְנֵי› (“the-altar which to-face”)
# ‹יְהוָה אֲשֶׁר בְּאֹהֶל› (“YHWH which in-tent”)
# ‹מוֹעֵד› (“seasons”)
# — standing handler — if and-from-the-blood then set-over-horn-the-altar ∧
# spill-forth-to-foundation-altar-the-burnt-offering
m.handler("u_min_ha_dam",
          "yiten_al_qarnot_ha_mizbecha ∧ yishpokh_el_yesod_mizbach_ha_ola")

# -------------------------- Lev.4.19 · ALL_ITS_FAT -------------------------
# ‹וְאֵת כָּל־חֶלְבּוֹ יָרִים› (“and-obj-marker all fat-him/its rise-high”)
# ‹מִמֶּנּוּ וְהִקְטִיר הַמִּזְבֵּחָה› (“from-us/our and-smoke the-altar-
# ward”)
# "[EN-AID] And all its fat he shall lift from it and burn on the altar."
m.step("Lev.4.19")
# ‹וְאֵת כָּל־חֶלְבּוֹ יָרִים› (“and-obj-marker all fat-him/its rise-high”)
# ‹מִמֶּנּוּ וְהִקְטִיר הַמִּזְבֵּחָה› (“from-us/our and-smoke the-altar-
# ward”)
# — standing handler — if all-chelbo then rise-high-from-it ∧ smoke-the-
# altar
m.handler("kol_chelbo",
          "yarim_mimenu ∧ hiqtir_ha_mizbecha")

# -------------------------- Lev.4.20 · AS_THE_FIRST_AND_FORGIVEN -----------
# ‹וְעָשָׂה לַפָּר כַּאֲשֶׁר› (“and-make to-bullock like-as/which”)
# ‹עָשָׂה לְפַר הַחַטָּאת› (“make to-bullock the-sin-offering”)
# ‹כֵּן יַעֲשֶׂה־לּוֹ וְכִפֶּר› (“so make to-him/its and-atone”)
# ‹עֲלֵהֶם הַכֹּהֵן וְנִסְלַח› (“over-them/their the-priest and-forgive”)
# ‹לָהֶם› (“to-them/their”)
# "[EN-AID] And he shall do to the bull as he did to the sin-offering bull -
# so shall he do to it; and the priest shall atone for them, and it shall be
# forgiven them."
m.step("Lev.4.20")
# ‹וְעָשָׂה לַפָּר כַּאֲשֶׁר› (“and-make to-bullock like-as/which”)
# ‹עָשָׂה לְפַר הַחַטָּאת› (“make to-bullock the-sin-offering”)
# ‹כֵּן יַעֲשֶׂה־לּוֹ וְכִפֶּר› (“so make to-him/its and-atone”)
# ‹עֲלֵהֶם הַכֹּהֵן וְנִסְלַח› (“over-them/their the-priest and-forgive”)
# ‹לָהֶם› (“to-them/their”)
# — standing handler — if like-which-make-to-bullock-the-sin-offering then
# so-make-not ∧ kiper-the-priest ∧ forgive-to-them
m.handler("ka_asher_asa_le_far_ha_chatat",
          "ken_yaase_lo ∧ kiper_ha_kohen ∧ nislach_lahem")

# -------------------------- Lev.4.21 · THE_FIRST_BULL_CITED ----------------
# ‹וְהוֹצִיא אֶת־הַפָּר אֶל־מִחוּץ› (“and-bring-forth obj-marker the-bullock
# to from-outside”)
# ‹לַמַּחֲנֶה וְשָׂרַף אֹתוֹ› (“to-camp and-be-on-fire obj-marker-him/its”)
# ‹כַּאֲשֶׁר שָׂרַף אֵת› (“like-as/which be-on-fire obj-marker”)
# ‹הַפָּר הָרִאשׁוֹן חַטַּאת› (“the-bullock the-first sin-offering”)
# ‹הַקָּהָל הוּא› (“the-assemblage he/it”)
# "[EN-AID] And he shall carry the bull outside the camp and burn it as he
# burned the first bull: it is the sin-offering of the assembly."
m.step("Lev.4.21")
# ‹וְהוֹצִיא אֶת־הַפָּר אֶל־מִחוּץ› (“and-bring-forth obj-marker the-bullock
# to from-outside”)
# ‹לַמַּחֲנֶה וְשָׂרַף אֹתוֹ› (“to-camp and-be-on-fire obj-marker-him/its”)
# ‹כַּאֲשֶׁר שָׂרַף אֵת› (“like-as/which be-on-fire obj-marker”)
# ‹הַפָּר הָרִאשׁוֹן חַטַּאת› (“the-bullock the-first sin-offering”)
# ‹הַקָּהָל הוּא› (“the-assemblage he/it”)
# — standing handler — if like-which-be-on-fire-obj-marker-the-bullock-the-
# first then bring-forth-and-be-on-fire-from-outside-to-camp
m.handler("ka_asher_saraf_et_ha_par_ha_rishon",
          "hotzi_ve_saraf_mi_chutz_la_machane")

# -------------------------- Lev.4.22 · BRANCH_THREE_THE_LEADER -------------
# ‹אֲשֶׁר נָשִׂיא יֶחֱטָא› (“which prince sin”)
# ‹וְעָשָׂה אַחַת מִכָּל־מִצְוֺת› (“and-make one from-all commandment”)
# ‹יְהוָה אֱלֹהָיו אֲשֶׁר› (“YHWH God-him/its which”)
# ‹לֹא־תֵעָשֶׂינָה בִּשְׁגָגָה וְאָשֵׁם› (“not make in-mistake and-be-
# guilty”)
# "[EN-AID] When a leader sins, and does one of all the commandments of the
# LORD his God which shall not be done, in inadvertence, and becomes guilty
# -"
m.step("Lev.4.22")
# ‹אֲשֶׁר נָשִׂיא יֶחֱטָא› (“which prince sin”)
# — case prince, which-sin-bi-shegaga routes to and-be-guilty
m.case("nasi, asher_yecheta_bi_shegaga", "ve_ashem")
# witness-tier presupposed read: cold_compile on
# chatat_censuses_at_their_talmud_seats — read, not installed
m.witness_read("chatat_censuses_at_their_talmud_seats", "cold_compile",
                cites=["Mishnah Horayot 3:3", "Mishnah Keritot 6:3", "Mishnah Keritot 6:4", "Mishnah Keritot 2:4", "Mishnah Keritot 6:9", "Mishnah Keritot 4:3", "Mishnah Horayot 3:6", "Horayot 11a:20", "Horayot 11b:1", "Horayot 11b:2", "Keritot 25b:4", "Keritot 26a:19", "Yoma 68a:6", "Yoma 68a:7", "Yoma 68a:8", "Sifra, Vayikra Dibbura DeChovah, Section 4 13", "Sifra, Vayikra Dibbura DeChovah, Section 7 1", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 9"])

# -------------------------- Lev.4.23 · THE_KNOWLEDGE_TRIGGER ---------------
# ‹אוֹ־הוֹדַע אֵלָיו חַטָּאתוֹ› (“or know to-him/its sin-offering-him/its”)
# ‹אֲשֶׁר חָטָא בָּהּ› (“which sin in-her/its”)
# ‹וְהֵבִיא אֶת־קָרְבָּנוֹ שְׂעִיר› (“and-come/bring obj-marker offering-
# him/its shaggy”)
# ‹עִזִּים זָכָר תָּמִים› (“she-goat male entire”)
# "[EN-AID] or his sin which he sinned is made known to him - then he shall
# bring his offering: a goat of the goats, a male, unblemished."
m.step("Lev.4.23")
# ‹אוֹ־הוֹדַע אֵלָיו חַטָּאתוֹ› (“or know to-him/its sin-offering-him/its”)
# ‹אֲשֶׁר חָטָא בָּהּ› (“which sin in-her/its”)
# — standing handler — if or-know-to-him-chatato then come/bring-qarbano-
# shaggy-she-goat-male-entire
m.handler("o_hoda_elav_chatato",
          "hevi_qarbano_seir_izim_zakhar_tamim")
# witness-tier presupposed read: self_knowledge_specificity on
# epistemic_triggers — read, not installed
m.witness_read("epistemic_triggers", "self_knowledge_specificity",
                cites=["Sifra, Vayikra Dibbura DeChovah, Chapter 7 1", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 3", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 4", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 6", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 7", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 8", "Sifra, Vayikra Dibbura DeChovah, Chapter 7 9"])

# -------------------------- Lev.4.24 · AT_THE_OLAH_PLACE -------------------
# ‹וְסָמַךְ יָדוֹ עַל־רֹאשׁ› (“and-lay hand-him/its over head”)
# ‹הַשָּׂעִיר וְשָׁחַט אֹתוֹ› (“the-shaggy and-slaughter obj-marker-
# him/its”)
# ‹בִּמְקוֹם אֲשֶׁר־יִשְׁחַט אֶת־הָעֹלָה› (“in-place which slaughter obj-
# marker the-burnt-offering”)
# ‹לִפְנֵי יְהוָה חַטָּאת› (“to-face YHWH sin-offering”)
# ‹הוּא› (“he/it”)
# "[EN-AID] And he shall lean his hand on the goat's head and slaughter it
# in the place where one slaughters the burnt-offering before the LORD: it
# is a sin-offering."
m.step("Lev.4.24")
# ‹וְסָמַךְ יָדוֹ עַל־רֹאשׁ› (“and-lay hand-him/its over head”)
# ‹הַשָּׂעִיר וְשָׁחַט אֹתוֹ› (“the-shaggy and-slaughter obj-marker-
# him/its”)
# ‹בִּמְקוֹם אֲשֶׁר־יִשְׁחַט אֶת־הָעֹלָה› (“in-place which slaughter obj-
# marker the-burnt-offering”)
# ‹לִפְנֵי יְהוָה› (“to-face YHWH”)
# — standing handler — if shaggy-the-sin-offering then lay-his-hand ∧
# slaughter-bi-meqom-which-slaughter-obj-marker-the-burnt-offering
m.handler("seir_ha_chatat",
          "samakh_yado ∧ shachat_bi_meqom_asher_yishchat_et_ha_ola")

# -------------------------- Lev.4.25 · OUTER_HORNS -------------------------
# ‹וְלָקַח הַכֹּהֵן מִדַּם› (“and-take the-priest from-blood”)
# ‹הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן› (“the-sin-offering in-something-to-
# sieze-with-him/its and-set”)
# ‹עַל־קַרְנֹת מִזְבַּח הָעֹלָה› (“over horn altar the-burnt-offering”)
# ‹וְאֶת־דָּמוֹ יִשְׁפֹּךְ אֶל־יְסוֹד› (“and-obj-marker blood-him/its spill-
# forth to foundation”)
# ‹מִזְבַּח הָעֹלָה› (“altar the-burnt-offering”)
# "[EN-AID] And the priest shall take of the sin-offering's blood with his
# finger and put it on the horns of the altar of burnt-offering; and its
# blood he shall pour out at the base of the altar of burnt-offering."
m.step("Lev.4.25")
# ‹וְלָקַח הַכֹּהֵן מִדַּם› (“and-take the-priest from-blood”)
# ‹הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן› (“the-sin-offering in-something-to-
# sieze-with-him/its and-set”)
# ‹עַל־קַרְנֹת מִזְבַּח הָעֹלָה› (“over horn altar the-burnt-offering”)
# ‹וְאֶת־דָּמוֹ יִשְׁפֹּךְ אֶל־יְסוֹד› (“and-obj-marker blood-him/its spill-
# forth to foundation”)
# ‹מִזְבַּח הָעֹלָה› (“altar the-burnt-offering”)
# — standing handler — if from-blood-the-sin-offering then set-in-etzbao-
# over-horn-altar-the-burnt-offering ∧ spill-forth-to-foundation
m.handler("mi_dam_ha_chatat",
          "natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod")

# -------------------------- Lev.4.26 · LEADER_FORGIVEN ---------------------
# ‹וְאֶת־כָּל־חֶלְבּוֹ יַקְטִיר הַמִּזְבֵּחָה› (“and-obj-marker all fat-
# him/its smoke the-altar-ward”)
# ‹כְּחֵלֶב זֶבַח הַשְּׁלָמִים› (“like-fat sacrifice the-requital”)
# ‹וְכִפֶּר עָלָיו הַכֹּהֵן› (“and-atone over-him/its the-priest”)
# ‹מֵחַטָּאתוֹ וְנִסְלַח לוֹ› (“from-sin-offering-him/its and-forgive to-
# him/its”)
# "[EN-AID] And all its fat he shall burn on the altar like the fat of the
# sacrifice of well-being; and the priest shall atone for him from his sin,
# and he shall be forgiven."
m.step("Lev.4.26")
# ‹וְאֶת־כָּל־חֶלְבּוֹ יַקְטִיר הַמִּזְבֵּחָה› (“and-obj-marker all fat-
# him/its smoke the-altar-ward”)
# ‹כְּחֵלֶב זֶבַח הַשְּׁלָמִים› (“like-fat sacrifice the-requital”)
# ‹וְכִפֶּר עָלָיו הַכֹּהֵן› (“and-atone over-him/its the-priest”)
# ‹מֵחַטָּאתוֹ וְנִסְלַח לוֹ› (“from-sin-offering-him/its and-forgive to-
# him/its”)
# — standing handler — if all-chelbo-like-fat-sacrifice-the-requital then
# smoke ∧ kiper ∧ forgive-not
m.handler("kol_chelbo_ke_chelev_zevach_ha_shelamim",
          "yaqtir ∧ kiper ∧ nislach_lo")

# -------------------------- Lev.4.27 · BRANCH_FOUR_THE_COMMONER ------------
# ‹וְאִם־נֶפֶשׁ אַחַת תֶּחֱטָא› (“and-if living-being one sin”)
# ‹בִשְׁגָגָה מֵעַם הָאָרֶץ› (“in-mistake from-people the-earth”)
# ‹בַּעֲשֹׂתָהּ אַחַת מִמִּצְוֺת› (“in-make-her/its one from-commandment”)
# ‹יְהוָה אֲשֶׁר לֹא־תֵעָשֶׂינָה› (“YHWH which not make”)
# ‹וְאָשֵׁם› (“and-be-guilty”)
# "[EN-AID] And if one soul of the people of the land sins in inadvertence,
# by doing one of the commandments of the LORD which shall not be done, and
# becomes guilty -"
m.step("Lev.4.27")
# ‹וְאִם־נֶפֶשׁ אַחַת תֶּחֱטָא› (“and-if living-being one sin”)
# ‹בִשְׁגָגָה מֵעַם הָאָרֶץ› (“in-mistake from-people the-earth”)
# — case living-being-from-people-the-earth, sin-vi-shegaga routes to and-
# be-guilty
m.case("nefesh_me_am_ha_aretz, techeta_vi_shegaga", "ve_ashem")
# witness-tier presupposed read: dependent_actor_exempt on tier_fences —
# read, not installed
m.witness_read("tier_fences", "dependent_actor_exempt",
                cites=["Sifra, Vayikra Dibbura DeChovah, Section 7 1", "Sifra, Vayikra Dibbura DeChovah, Section 7 2", "Sifra, Vayikra Dibbura DeChovah, Section 7 3", "Sifra, Vayikra Dibbura DeChovah, Section 7 4", "Sifra, Vayikra Dibbura DeChovah, Section 7 6", "Sifra, Vayikra Dibbura DeChovah, Section 7 7", "Sifra, Vayikra Dibbura DeChovah, Section 6 1", "Sifra, Vayikra Dibbura DeChovah, Section 6 9"])

# -------------------------- Lev.4.28 · THE_SHE_GOAT ------------------------
# ‹אוֹ הוֹדַע אֵלָיו› (“or know to-him/its”)
# ‹חַטָּאתוֹ אֲשֶׁר חָטָא› (“sin-offering-him/its which sin”)
# ‹וְהֵבִיא קָרְבָּנוֹ שְׂעִירַת› (“and-come/bring offering-him/its she-
# goat”)
# ‹עִזִּים תְּמִימָה נְקֵבָה› (“she-goat entire female”)
# ‹עַל־חַטָּאתוֹ אֲשֶׁר חָטָא› (“over sin-offering-him/its which sin”)
# "[EN-AID] or his sin which he sinned is made known to him - then he shall
# bring his offering: a she-goat of the goats, unblemished, a female, for
# his sin which he sinned."
m.step("Lev.4.28")
# ‹אוֹ הוֹדַע אֵלָיו› (“or know to-him/its”)
# ‹חַטָּאתוֹ אֲשֶׁר חָטָא› (“sin-offering-him/its which sin”)
# ‹וְהֵבִיא קָרְבָּנוֹ שְׂעִירַת› (“and-come/bring offering-him/its she-
# goat”)
# ‹עִזִּים תְּמִימָה נְקֵבָה› (“she-goat entire female”)
# — standing handler — if or-know-to-him-chatato then come/bring-qarbano-
# she-goat-she-goat-entire-female
m.handler("o_hoda_elav_chatato",
          "hevi_qarbano_seirat_izim_temima_neqeva")

# -------------------------- Lev.4.29 · LEAN_AND_SLAUGHTER ------------------
# ‹וְסָמַךְ אֶת־יָדוֹ עַל› (“and-lay obj-marker hand-him/its over”)
# ‹רֹאשׁ הַחַטָּאת וְשָׁחַט› (“head the-sin-offering and-slaughter”)
# ‹אֶת־הַחַטָּאת בִּמְקוֹם הָעֹלָה› (“obj-marker the-sin-offering in-place
# the-burnt-offering”)
# "[EN-AID] And he shall lean his hand on the sin-offering's head and
# slaughter the sin-offering in the place of the burnt-offering."
m.step("Lev.4.29")
# ‹וְסָמַךְ אֶת־יָדוֹ עַל› (“and-lay obj-marker hand-him/its over”)
# ‹רֹאשׁ הַחַטָּאת וְשָׁחַט› (“head the-sin-offering and-slaughter”)
# ‹אֶת־הַחַטָּאת בִּמְקוֹם הָעֹלָה› (“obj-marker the-sin-offering in-place
# the-burnt-offering”)
# — standing handler — if the-sin-offering then lay-his-hand ∧ slaughter-bi-
# meqom-the-burnt-offering
m.handler("ha_chatat",
          "samakh_yado ∧ shachat_bi_meqom_ha_ola")

# -------------------------- Lev.4.30 · FINGER_HORNS_BASE -------------------
# ‹וְלָקַח הַכֹּהֵן מִדָּמָהּ› (“and-take the-priest from-blood-her/its”)
# ‹בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת› (“in-something-to-sieze-with-him/its
# and-set over horn”)
# ‹מִזְבַּח הָעֹלָה וְאֶת־כָּל־דָּמָהּ› (“altar the-burnt-offering and-obj-
# marker all blood-her/its”)
# ‹יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ› (“spill-forth to foundation the-
# altar”)
# "[EN-AID] And the priest shall take of its blood with his finger and put
# it on the horns of the altar of burnt-offering; and all its blood he shall
# pour out at the base of the altar."
m.step("Lev.4.30")
# ‹וְלָקַח הַכֹּהֵן מִדָּמָהּ› (“and-take the-priest from-blood-her/its”)
# ‹בְּאֶצְבָּעוֹ וְנָתַן עַל־קַרְנֹת› (“in-something-to-sieze-with-him/its
# and-set over horn”)
# ‹מִזְבַּח הָעֹלָה וְאֶת־כָּל־דָּמָהּ› (“altar the-burnt-offering and-obj-
# marker all blood-her/its”)
# ‹יִשְׁפֹּךְ אֶל־יְסוֹד הַמִּזְבֵּחַ› (“spill-forth to foundation the-
# altar”)
# — standing handler — if from-damah then set-in-etzbao-over-horn-altar-the-
# burnt-offering ∧ spill-forth-to-foundation-the-altar
m.handler("mi_damah",
          "natan_be_etzbao_al_qarnot_mizbach_ha_ola ∧ yishpokh_el_yesod_ha_mizbecha")

# -------------------------- Lev.4.31 · THE_PLEASING_AROMA ------------------
# ‹וְאֶת־כָּל־חֶלְבָּהּ יָסִיר כַּאֲשֶׁר› (“and-obj-marker all fat-her/its
# turn-aside like-as/which”)
# ‹הוּסַר חֵלֶב מֵעַל› (“turn-aside fat from-over”)
# ‹זֶבַח הַשְּׁלָמִים וְהִקְטִיר› (“sacrifice the-requital and-smoke”)
# ‹הַכֹּהֵן הַמִּזְבֵּחָה לְרֵיחַ› (“the-priest the-altar-ward to-odor”)
# ‹נִיחֹחַ לַיהוָה וְכִפֶּר› (“restful to-YHWH and-atone”)
# ‹עָלָיו הַכֹּהֵן וְנִסְלַח› (“over-him/its the-priest and-forgive”)
# ‹לוֹ› (“to-him/its”)
# "[EN-AID] And all its fat he shall remove, as fat is removed from the
# sacrifice of well-being, and the priest shall burn it on the altar for a
# pleasing aroma to the LORD; and the priest shall atone for him, and he
# shall be forgiven."
m.step("Lev.4.31")
# ‹וְאֶת־כָּל־חֶלְבָּהּ יָסִיר כַּאֲשֶׁר› (“and-obj-marker all fat-her/its
# turn-aside like-as/which”)
# ‹הוּסַר חֵלֶב מֵעַל› (“turn-aside fat from-over”)
# ‹זֶבַח הַשְּׁלָמִים וְהִקְטִיר› (“sacrifice the-requital and-smoke”)
# ‹הַכֹּהֵן הַמִּזְבֵּחָה לְרֵיחַ› (“the-priest the-altar-ward to-odor”)
# ‹נִיחֹחַ לַיהוָה וְכִפֶּר› (“restful to-YHWH and-atone”)
# ‹עָלָיו הַכֹּהֵן וְנִסְלַח› (“over-him/its the-priest and-forgive”)
# ‹לוֹ› (“to-him/its”)
# — standing handler — if all-chelbah-like-which-turn-aside-from-over-
# sacrifice-the-requital then smoke-to-odor-restful ∧ kiper ∧ forgive-not
m.handler("kol_chelbah_ka_asher_husar_me_al_zevach_ha_shelamim",
          "hiqtir_le_recha_nichocha ∧ kiper ∧ nislach_lo")

# -------------------------- Lev.4.32 · THE_LAMB_ALTERNATIVE ----------------
# ‹וְאִם־כֶּבֶשׂ יָבִיא קָרְבָּנוֹ› (“and-if ram come/bring offering-
# him/its”)
# ‹לְחַטָּאת נְקֵבָה תְמִימָה› (“to-sin-offering female entire”)
# ‹יְבִיאֶנָּה› (“come/bring-her/its”)
# "[EN-AID] And if he brings a lamb as his offering for a sin-offering, an
# unblemished female shall he bring."
m.step("Lev.4.32")
# ‹וְאִם־כֶּבֶשׂ יָבִיא קָרְבָּנוֹ› (“and-if ram come/bring offering-
# him/its”)
# ‹לְחַטָּאת נְקֵבָה תְמִימָה› (“to-sin-offering female entire”)
# ‹יְבִיאֶנָּה› (“come/bring-her/its”)
# — case ram, and-if-come/bring-to-sin-offering routes to female-entire-
# yeviena
m.case("keves, ve_im_yavi_le_chatat", "neqeva_temima_yeviena")
# witness-tier presupposed read: no_rank_lost_replaced on order_equivalence
# — read, not installed
m.witness_read("order_equivalence", "no_rank_lost_replaced",
                cites=["Sifra, Vayikra Dibbura DeChovah, Chapter 10 9", "Sifra, Vayikra Dibbura DeChovah, Chapter 10 10", "Sifra, Vayikra Dibbura DeChovah, Chapter 11 1", "Sifra, Vayikra Dibbura DeChovah, Chapter 11 2"])

# -------------------------- Lev.4.33 · LEAN_AND_SLAUGHTER_HER --------------
# ‹וְסָמַךְ אֶת־יָדוֹ עַל› (“and-lay obj-marker hand-him/its over”)
# ‹רֹאשׁ הַחַטָּאת וְשָׁחַט› (“head the-sin-offering and-slaughter”)
# ‹אֹתָהּ לְחַטָּאת בִּמְקוֹם› (“obj-marker-her/its to-sin-offering in-
# place”)
# ‹אֲשֶׁר יִשְׁחַט אֶת־הָעֹלָה› (“which slaughter obj-marker the-burnt-
# offering”)
# "[EN-AID] And he shall lean his hand on the sin-offering's head and
# slaughter it for a sin-offering in the place where one slaughters the
# burnt-offering."
m.step("Lev.4.33")
# ‹וְסָמַךְ אֶת־יָדוֹ עַל› (“and-lay obj-marker hand-him/its over”)
# ‹רֹאשׁ הַחַטָּאת וְשָׁחַט› (“head the-sin-offering and-slaughter”)
# ‹אֹתָהּ לְחַטָּאת בִּמְקוֹם› (“obj-marker-her/its to-sin-offering in-
# place”)
# ‹אֲשֶׁר יִשְׁחַט אֶת־הָעֹלָה› (“which slaughter obj-marker the-burnt-
# offering”)
# — standing handler — if the-sin-offering then lay-his-hand ∧ slaughter-
# her-to-sin-offering-bi-meqom-which-slaughter-obj-marker-the-burnt-offering
m.handler("ha_chatat",
          "samakh_yado ∧ shachat_otah_le_chatat_bi_meqom_asher_yishchat_et_ha_ola")

# -------------------------- Lev.4.34 · THE_LAST_BLOOD ----------------------
# ‹וְלָקַח הַכֹּהֵן מִדַּם› (“and-take the-priest from-blood”)
# ‹הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן› (“the-sin-offering in-something-to-
# sieze-with-him/its and-set”)
# ‹עַל־קַרְנֹת מִזְבַּח הָעֹלָה› (“over horn altar the-burnt-offering”)
# ‹וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד› (“and-obj-marker all blood-
# her/its spill-forth to foundation”)
# ‹הַמִּזְבֵּחַ› (“the-altar”)
# "[EN-AID] And the priest shall take of the sin-offering's blood with his
# finger and put it on the horns of the altar of burnt-offering; and all its
# blood he shall pour out at the base of the altar."
m.step("Lev.4.34")
# ‹וְלָקַח הַכֹּהֵן מִדַּם› (“and-take the-priest from-blood”)
# ‹הַחַטָּאת בְּאֶצְבָּעוֹ וְנָתַן› (“the-sin-offering in-something-to-
# sieze-with-him/its and-set”)
# ‹עַל־קַרְנֹת מִזְבַּח הָעֹלָה› (“over horn altar the-burnt-offering”)
# ‹וְאֶת־כָּל־דָּמָהּ יִשְׁפֹּךְ אֶל־יְסוֹד› (“and-obj-marker all blood-
# her/its spill-forth to foundation”)
# ‹הַמִּזְבֵּחַ› (“the-altar”)
# — standing handler — if from-blood-the-sin-offering then set-in-etzbao-
# over-horn ∧ spill-forth-all-damah-to-foundation
m.handler("mi_dam_ha_chatat",
          "natan_be_etzbao_al_qarnot ∧ yishpokh_kal_damah_el_yesod")

# -------------------------- Lev.4.35 · THE_WALL_FOURTH_PARDON --------------
# ‹וְאֶת־כָּל־חֶלְבָּה יָסִיר כַּאֲשֶׁר› (“and-obj-marker all fat-her/its
# turn-aside like-as/which”)
# ‹יוּסַר חֵלֶב־הַכֶּשֶׂב מִזֶּבַח› (“turn-aside fat the-young-sheep from-
# sacrifice”)
# ‹הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן› (“the-requital and-smoke the-priest”)
# ‹אֹתָם הַמִּזְבֵּחָה עַל› (“obj-marker-them/their the-altar-ward over”)
# ‹אִשֵּׁי יְהוָה וְכִפֶּר› (“fire-offering YHWH and-atone”)
# ‹עָלָיו הַכֹּהֵן עַל־חַטָּאתוֹ› (“over-him/its the-priest over sin-
# offering-him/its”)
# ‹אֲשֶׁר־חָטָא וְנִסְלַח לוֹ› (“which sin and-forgive to-him/its”)
# "[EN-AID] And all its fat he shall remove, as the lamb's fat is removed
# from the sacrifice of well-being, and the priest shall burn them on the
# altar upon the fire-offerings of the LORD; and the priest shall atone for
# him, for his sin which he sinned, and he shall be forgiven."
m.step("Lev.4.35")
# ‹וְאֶת־כָּל־חֶלְבָּה יָסִיר כַּאֲשֶׁר› (“and-obj-marker all fat-her/its
# turn-aside like-as/which”)
# ‹יוּסַר חֵלֶב־הַכֶּשֶׂב מִזֶּבַח› (“turn-aside fat the-young-sheep from-
# sacrifice”)
# ‹הַשְּׁלָמִים וְהִקְטִיר הַכֹּהֵן› (“the-requital and-smoke the-priest”)
# ‹אֹתָם הַמִּזְבֵּחָה עַל› (“obj-marker-them/their the-altar-ward over”)
# ‹אִשֵּׁי יְהוָה וְכִפֶּר› (“fire-offering YHWH and-atone”)
# ‹עָלָיו הַכֹּהֵן עַל־חַטָּאתוֹ› (“over-him/its the-priest over sin-
# offering-him/its”)
# ‹אֲשֶׁר־חָטָא וְנִסְלַח לוֹ› (“which sin and-forgive to-him/its”)
# — standing handler — if all-chelbah-like-which-turn-aside-fat-the-young-
# sheep then smoke-over-fire-offering-the-LORD ∧ kiper ∧ forgive-not
m.handler("kol_chelbah_ka_asher_yusar_chelev_ha_kesev",
          "hiqtir_al_ishe_YHWH ∧ kiper ∧ nislach_lo")
# witness-tier presupposed read:
# four_as_the_fat_clauses_resolved_by_live_call on
# the_pointer_names_the_species — read, not installed
m.witness_read("the_pointer_names_the_species", "four_as_the_fat_clauses_resolved_by_live_call",
                cites=["Sifra, Vayikra Dibbura DeChovah, Chapter 4 2", "Sifra, Vayikra Dibbura DeChovah, Chapter 4 3", "Sifra, Vayikra Dibbura DeChovah, Chapter 9 4", "Sifra, Vayikra Dibbura DeNedavah, Chapter 19 3", "Sifra, Vayikra Dibbura DeNedavah, Chapter 20 1", "Sifra, Vayikra Dibbura DeNedavah, Section 14 10", "Mishnah Tamid 4:3", "Mishnah Chullin 8:6", "Mishnah Zevachim 10:2"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('aggregation_keys', 'knowledge_indexed_counts'), ('blood_algorithms', 'dip_per_sprinkle_staves'), ('court_error_machine', 'unanimity_partial_located'), ('tribal_arithmetic', 'four_positions'), ('elders_quorum', 'five_or_three'), ('chatat_censuses_at_their_talmud_seats', 'cold_compile'), ('epistemic_triggers', 'self_knowledge_specificity'), ('tier_fences', 'dependent_actor_exempt'), ('order_equivalence', 'no_rank_lost_replaced'), ('the_pointer_names_the_species', 'four_as_the_fat_clauses_resolved_by_live_call')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Chapter 1 7', 'Sifra, Vayikra Dibbura DeChovah, Chapter 1 4', 'Sifra, Vayikra Dibbura DeChovah, Chapter 1 5', 'Sifra, Vayikra Dibbura DeChovah, Section 5 4', 'Sifra, Vayikra Dibbura DeChovah, Section 7 8', 'Sifra, Vayikra Dibbura DeChovah, Section 7 9', 'Sifra, Vayikra Dibbura DeChovah, Chapter 1 8', 'Sifra, Vayikra Dibbura DeChovah, Chapter 1 13']
    assert all('knowledge_indexed_counts' not in f for f in m.WORLD["facts"])
    assert 'aggregation_keys' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Section 3 5', 'Sifra, Vayikra Dibbura DeChovah, Section 3 7', 'Sifra, Vayikra Dibbura DeChovah, Section 3 8', 'Sifra, Vayikra Dibbura DeChovah, Section 3 10', 'Sifra, Vayikra Dibbura DeChovah, Section 3 11', 'Sifra, Vayikra Dibbura DeChovah, Section 3 13', 'Sifra, Vayikra Dibbura DeChovah, Chapter 10 4', 'Sifra, Vayikra Dibbura DeChovah, Chapter 9 1']
    assert all('dip_per_sprinkle_staves' not in f for f in m.WORLD["facts"])
    assert 'blood_algorithms' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Section 4 2', 'Sifra, Vayikra Dibbura DeChovah, Section 4 3', 'Sifra, Vayikra Dibbura DeChovah, Section 4 4', 'Sifra, Vayikra Dibbura DeChovah, Section 4 5', 'Sifra, Vayikra Dibbura DeChovah, Section 4 7', 'Sifra, Vayikra Dibbura DeChovah, Section 4 8', 'Sifra, Vayikra Dibbura DeChovah, Section 4 10', 'Sifra, Vayikra Dibbura DeChovah, Section 4 12']
    assert all('unanimity_partial_located' not in f for f in m.WORLD["facts"])
    assert 'court_error_machine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Section 4 13', 'Sifra, Vayikra Dibbura DeChovah, Section 4 14', 'Sifra, Vayikra Dibbura DeChovah, Section 4 15', 'Sifra, Vayikra Dibbura DeChovah, Section 4 16', 'Sifra, Vayikra Dibbura DeChovah, Section 4 17']
    assert all('four_positions' not in f for f in m.WORLD["facts"])
    assert 'tribal_arithmetic' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Chapter 6 1', 'Sifra, Vayikra Dibbura DeChovah, Chapter 6 2', 'Sifra, Vayikra Dibbura DeChovah, Chapter 6 3']
    assert all('five_or_three' not in f for f in m.WORLD["facts"])
    assert 'elders_quorum' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Horayot 3:3', 'Mishnah Keritot 6:3', 'Mishnah Keritot 6:4', 'Mishnah Keritot 2:4', 'Mishnah Keritot 6:9', 'Mishnah Keritot 4:3', 'Mishnah Horayot 3:6', 'Horayot 11a:20', 'Horayot 11b:1', 'Horayot 11b:2', 'Keritot 25b:4', 'Keritot 26a:19', 'Yoma 68a:6', 'Yoma 68a:7', 'Yoma 68a:8', 'Sifra, Vayikra Dibbura DeChovah, Section 4 13', 'Sifra, Vayikra Dibbura DeChovah, Section 7 1', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 9']
    assert all('cold_compile' not in f for f in m.WORLD["facts"])
    assert 'chatat_censuses_at_their_talmud_seats' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Chapter 7 1', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 3', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 4', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 6', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 7', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 8', 'Sifra, Vayikra Dibbura DeChovah, Chapter 7 9']
    assert all('self_knowledge_specificity' not in f for f in m.WORLD["facts"])
    assert 'epistemic_triggers' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Section 7 1', 'Sifra, Vayikra Dibbura DeChovah, Section 7 2', 'Sifra, Vayikra Dibbura DeChovah, Section 7 3', 'Sifra, Vayikra Dibbura DeChovah, Section 7 4', 'Sifra, Vayikra Dibbura DeChovah, Section 7 6', 'Sifra, Vayikra Dibbura DeChovah, Section 7 7', 'Sifra, Vayikra Dibbura DeChovah, Section 6 1', 'Sifra, Vayikra Dibbura DeChovah, Section 6 9']
    assert all('dependent_actor_exempt' not in f for f in m.WORLD["facts"])
    assert 'tier_fences' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Chapter 10 9', 'Sifra, Vayikra Dibbura DeChovah, Chapter 10 10', 'Sifra, Vayikra Dibbura DeChovah, Chapter 11 1', 'Sifra, Vayikra Dibbura DeChovah, Chapter 11 2']
    assert all('no_rank_lost_replaced' not in f for f in m.WORLD["facts"])
    assert 'order_equivalence' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Vayikra Dibbura DeChovah, Chapter 4 2', 'Sifra, Vayikra Dibbura DeChovah, Chapter 4 3', 'Sifra, Vayikra Dibbura DeChovah, Chapter 9 4', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 19 3', 'Sifra, Vayikra Dibbura DeNedavah, Chapter 20 1', 'Sifra, Vayikra Dibbura DeNedavah, Section 14 10', 'Mishnah Tamid 4:3', 'Mishnah Chullin 8:6', 'Mishnah Zevachim 10:2']
    assert all('four_as_the_fat_clauses_resolved_by_live_call' not in f for f in m.WORLD["facts"])
    assert 'the_pointer_names_the_species' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
