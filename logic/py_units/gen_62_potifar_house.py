#!/usr/bin/env python3
# =============================================================================
# gen_62_potifar_house — 39:1-23
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_62_potifar_house.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Potiphar's house: the refusal on the chain (39:1-23)"""
from machine import Machine

m = Machine("gen_62_potifar_house")

# -------------------------- Gen.39.1 · BOUGHT_BY_POTIPHAR ------------------
# ‹וְיוֹסֵף הוּרַד מִצְרָיְמָה› (“and-Joseph go-down Egypt-ward”)
# ‹וַיִּקְנֵהוּ פּוֹטִיפַר סְרִיס› (“and-erect-him/its Potiphar eunuch”)
# ‹פַּרְעֹה שַׂר הַטַּבָּחִים› (“Pharaoh officer the-butcher”)
# ‹אִישׁ מִצְרִי מִיַּד› (“man Egyptian from-hand”)
# ‹הַיִּשְׁמְעֵאלִים אֲשֶׁר הוֹרִדֻהוּ› (“the-Jishmaelite which go-down-
# him/its”)
# ‹שָׁמָּה› (“there-ward”)
# "[EN-AID] And Joseph was brought down to Egypt; and Potiphar, Pharaoh's
# officer, the chief of the slaughterers, an Egyptian man, bought him from
# the hand of the Ishmaelites who had brought him down there."
m.step("Gen.39.1")
# ‹וְיוֹסֵף הוּרַד מִצְרָיְמָה› (“and-Joseph go-down Egypt-ward”)
# ‹וַיִּקְנֵהוּ פּוֹטִיפַר› (“and-erect-him/its Potiphar”)
# — fact holds: go-down-mitzrayma-and-yiqnehu-Potiphar(Joseph)
m.fact("hurad_mitzrayma_va_yiqnehu_potifar(yosef)")

# -------------------------- Gen.39.2 · THE_LORD_WITH_HIM -------------------
# ‹וַיְהִי יְהוָה אֶת־יוֹסֵף› (“and-be YHWH with Joseph”)
# ‹וַיְהִי אִישׁ מַצְלִיחַ› (“and-be man push-forward”)
# ‹וַיְהִי בְּבֵית אֲדֹנָיו› (“and-be in-house lord-him/its”)
# ‹הַמִּצְרִי› (“the-Egyptian”)
# "[EN-AID] And the LORD was with Joseph, and he was a prospering man; and
# he was in the house of his master the Egyptian."
m.step("Gen.39.2")
# ‹וַיְהִי יְהוָה אֶת־יוֹסֵף› (“and-be YHWH with Joseph”)
# ‹וַיְהִי אִישׁ מַצְלִיחַ› (“and-be man push-forward”)
# — fact holds: the-LORD-with-Joseph-man-matzliach
m.fact("YHWH_et_yosef_ish_matzliach")
# witness-tier presupposed read: four_seat_frame on accompaniment_formula —
# read, not installed
m.witness_read("accompaniment_formula", "four_seat_frame",
                cites=["Onkelos Genesis 39:2"])

# -------------------------- Gen.39.3 · THE_MASTER_SEES ---------------------
# ‹וַיַּרְא אֲדֹנָיו כִּי› (“and-see lord-him/its that”)
# ‹יְהוָה אִתּוֹ וְכֹל› (“YHWH with-him/its and-all”)
# ‹אֲשֶׁר־הוּא עֹשֶׂה יְהוָה› (“which he/it make YHWH”)
# ‹מַצְלִיחַ בְּיָדוֹ› (“push-forward in-hand-him/its”)
# "[EN-AID] And his master saw that the LORD was with him, and all that he
# did the LORD made prosper in his hand."
m.step("Gen.39.3")
# ‹וַיַּרְא אֲדֹנָיו כִּי› (“and-see lord-him/its that”)
# ‹יְהוָה אִתּוֹ› (“YHWH with-him/its”)
# — fact holds: bad-adonav-that-the-LORD-with-him
m.fact("raa_adonav_ki_YHWH_ito")

# -------------------------- Gen.39.4 · APPOINTED_OVER_THE_HOUSE ------------
# ‹וַיִּמְצָא יוֹסֵף חֵן› (“and-find Joseph graciousness”)
# ‹בְּעֵינָיו וַיְשָׁרֶת אֹתוֹ› (“in-eye-him/its and-attend-as-a-menial obj-
# marker-him/its”)
# ‹וַיַּפְקִדֵהוּ עַל־בֵּיתוֹ וְכָל־יֶשׁ־לוֹ› (“and-count/visit-him/its over
# house-him/its and-all there-is to-him/its”)
# ‹נָתַן בְּיָדוֹ› (“set in-hand-him/its”)
# "[EN-AID] And Joseph found favor in his eyes, and he served him; and he
# appointed him over his house, and all he had he gave into his hand."
m.step("Gen.39.4")
# ‹וַיַּפְקִדֵהוּ עַל־בֵּיתוֹ וְכָל־יֶשׁ־לוֹ› (“and-count/visit-him/its over
# house-him/its and-all there-is to-him/its”)
# ‹נָתַן בְּיָדוֹ› (“set in-hand-him/its”)
# — fact holds: count/visit-over-beto-and-all-set-in-his-hand
m.fact("hifqid_al_beto_ve_khol_natan_be_yado")

# -------------------------- Gen.39.5 · THE_BLESSING_FOR_HIS_SAKE -----------
# ‹וַיְהִי מֵאָז הִפְקִיד› (“and-be from-at-that-time count/visit”)
# ‹אֹתוֹ בְּבֵיתוֹ וְעַל› (“obj-marker-him/its in-house-him/its and-over”)
# ‹כָּל־אֲשֶׁר יֶשׁ־לוֹ וַיְבָרֶךְ› (“all which there-is to-him/its and-
# bless”)
# ‹יְהוָה אֶת־בֵּית הַמִּצְרִי› (“YHWH obj-marker house the-Egyptian”)
# ‹בִּגְלַל יוֹסֵף וַיְהִי› (“in-circumstance Joseph and-be”)
# ‹בִּרְכַּת יְהוָה בְּכָל־אֲשֶׁר› (“blessing YHWH in-all which”)
# ‹יֶשׁ־לוֹ בַּבַּיִת וּבַשָּׂדֶה› (“there-is to-him/its in-house and-in-
# field”)
# "[EN-AID] And it was, from the time he appointed him in his house and over
# all that he had, the LORD blessed the Egyptian's house for Joseph's sake;
# and the LORD's blessing was on all he had, in the house and in the field."
m.step("Gen.39.5")
# ‹וַיְבָרֶךְ יְהוָה אֶת־בֵּית› (“and-bless YHWH obj-marker house”)
# ‹הַמִּצְרִי בִּגְלַל יוֹסֵף› (“the-Egyptian in-circumstance Joseph”)
# — fact holds: berakh-the-LORD-house-the-Egyptian-biglal-Joseph
m.fact("berakh_YHWH_bet_ha_mitzri_biglal_yosef")

# -------------------------- Gen.39.6 · THE_BEAUTY_NOTE ---------------------
# ‹וַיַּעֲזֹב כָּל־אֲשֶׁר־לוֹ בְּיַד־יוֹסֵף› (“and-loosen all which to-
# him/its in-hand Joseph”)
# ‹וְלֹא־יָדַע אִתּוֹ מְאוּמָה› (“and-not know with-him/its speck”)
# ‹כִּי אִם־הַלֶּחֶם אֲשֶׁר־הוּא› (“very-widely-used-as-a-relati as-
# demonstrative the-food which he/it”)
# ‹אוֹכֵל וַיְהִי יוֹסֵף› (“eat and-be Joseph”)
# ‹יְפֵה־תֹאַר וִיפֵה מַרְאֶה› (“beautiful outline and-beautiful
# appearance”)
# "[EN-AID] And he left all that he had in Joseph's hand, and knew nothing
# with him except the bread that he ate; and Joseph was beautiful of form
# and beautiful of appearance."
m.step("Gen.39.6")
# ‹וַיְהִי יוֹסֵף יְפֵה־תֹאַר› (“and-be Joseph beautiful outline”)
# ‹וִיפֵה מַרְאֶה› (“and-beautiful appearance”)
# — fact holds: beautiful-outline-vi-yfe-appearance(Joseph)
m.fact("yefe_toar_vi_yfe_mare(yosef)")

# -------------------------- Gen.39.7 · THE_DEMAND_PUSHED -------------------
# ‹וַיְהִי אַחַר הַדְּבָרִים› (“and-be after the-word/thing”)
# ‹הָאֵלֶּה וַתִּשָּׂא אֵשֶׁת־אֲדֹנָיו› (“the-these and-lift/carry woman
# lord-him/its”)
# ‹אֶת־עֵינֶיהָ אֶל־יוֹסֵף וַתֹּאמֶר› (“obj-marker eye-her/its to Joseph
# and-say”)
# ‹שִׁכְבָה עִמִּי› (“lie-down-ward with-me/my”)
# "[EN-AID] And it was after these things, and his master's wife lifted her
# eyes to Joseph, and said: Lie with me."
m.step("Gen.39.7")
# ‹וַתֹּאמֶר שִׁכְבָה עִמִּי› (“and-say lie-down-ward with-me/my”)
# — woman-adonav speaks a demand — LET: shikhva-imi
m.declare("eshet_adonav", "LET",
          "shikhva_imi")

# -------------------------- Gen.39.8 · THE_CHAIN_REFUSAL -------------------
# ‹וַיְמָאֵן וַיֹּאמֶר אֶל־אֵשֶׁת› (“and-refuse and-say to woman”)
# ‹אֲדֹנָיו הֵן אֲדֹנִי› (“lord-him/its lo! lord-me/my”)
# ‹לֹא־יָדַע אִתִּי מַה־בַּבָּיִת› (“not know with-me/my what in-house”)
# ‹וְכֹל אֲשֶׁר־יֶשׁ־לוֹ נָתַן› (“and-all which there-is to-him/its set”)
# ‹בְּיָדִי› (“in-hand-me/my”)
# "[EN-AID] And he refused, and said to his master's wife: Behold, my master
# knows not what is with me in the house, and all that he has he gave into
# my hand."
m.step("Gen.39.8")
# ‹וַיְמָאֵן וַיֹּאמֶר› (“and-refuse and-say”)
# — fact holds: and-refuse-lo!-adoni(Joseph)
m.fact("va_yemaen_hen_adoni(yosef)")

# -------------------------- Gen.39.9 · THE_GREAT_EVIL_NAMED ----------------
# ‹אֵינֶנּוּ גָדוֹל בַּבַּיִת› (“there-is-not-him/its great in-house”)
# ‹הַזֶּה מִמֶּנִּי וְלֹא־חָשַׂךְ› (“the-this from-me/my and-not restrain”)
# ‹מִמֶּנִּי מְאוּמָה כִּי› (“from-me/my speck very-widely-used-as-a-
# relati”)
# ‹אִם־אוֹתָךְ בַּאֲשֶׁר אַתְּ־אִשְׁתּוֹ› (“as-demonstrative obj-marker-
# you/your in-who thou-and-thee woman-him/its”)
# ‹וְאֵיךְ אֶעֱשֶׂה הָרָעָה› (“and-how? make the-bad”)
# ‹הַגְּדֹלָה הַזֹּאת וְחָטָאתִי› (“the-great the-this and-sin”)
# ‹לֵאלֹהִים› (“to-God”)
# "[EN-AID] There is none greater in this house than I, and he has withheld
# nothing from me except you, in that you are his wife; and how shall I do
# this great evil, and sin against God?"
m.step("Gen.39.9")
# ‹וְאֵיךְ אֶעֱשֶׂה הָרָעָה› (“and-how? make the-bad”)
# ‹הַגְּדֹלָה הַזֹּאת וְחָטָאתִי› (“the-great the-this and-sin”)
# ‹לֵאלֹהִים› (“to-God”)
# — fact holds: how?-make-the-bad-the-great-and-sin-to-God
m.fact("ekh_eese_ha_raa_ha_gedola_ve_chatati_le_Elohim")

# -------------------------- Gen.39.10 · DAY_BY_DAY -------------------------
# ‹וַיְהִי כְּדַבְּרָהּ אֶל־יוֹסֵף› (“and-be like-speak-her/its to Joseph”)
# ‹יוֹם יוֹם וְלֹא־שָׁמַע› (“day day and-not hear”)
# ‹אֵלֶיהָ לִשְׁכַּב אֶצְלָהּ› (“to-her/its to-lie-down side-her/its”)
# ‹לִהְיוֹת עִמָּהּ› (“to-be with-her/its”)
# "[EN-AID] And it was, as she spoke to Joseph day by day, he did not listen
# to her, to lie beside her, to be with her."
m.step("Gen.39.10")
# ‹וַיְהִי כְּדַבְּרָהּ אֶל־יוֹסֵף› (“and-be like-speak-her/its to Joseph”)
# ‹יוֹם יוֹם› (“day day”)
# — fact holds: and-not-hear-eleha-day-day(Joseph)
m.fact("ve_lo_shama_eleha_yom_yom(yosef)")

# -------------------------- Gen.39.11 · THE_EMPTY_HOUSE --------------------
# ‹וַיְהִי כְּהַיּוֹם הַזֶּה› (“and-be like-the-day the-this”)
# ‹וַיָּבֹא הַבַּיְתָה לַעֲשׂוֹת› (“and-come/bring the-house-ward to-make”)
# ‹מְלַאכְתּוֹ וְאֵין אִישׁ› (“work-him/its and-there-is-not man”)
# ‹מֵאַנְשֵׁי הַבַּיִת שָׁם› (“from-man the-house there”)
# ‹בַּבָּיִת› (“in-house”)
# "[EN-AID] And it was, on this day, that he came into the house to do his
# work; and no man of the men of the house was there in the house."
m.step("Gen.39.11")
# ‹וְאֵין אִישׁ מֵאַנְשֵׁי› (“and-there-is-not man from-man”)
# ‹הַבַּיִת שָׁם בַּבָּיִת› (“the-house there in-house”)
# — fact holds: and-there-is-not-man-come/bring-house
m.fact("ve_en_ish_ba_bayit")
# witness-tier presupposed read: errand_disputed on laasot_melakhto — read,
# not installed
m.witness_read("laasot_melakhto", "errand_disputed",
                cites=["Bereshit Rabbah 87:7", "Onkelos Genesis 39:11"])

# -------------------------- Gen.39.12 · THE_GARMENT_SEIZED -----------------
# ‹וַתִּתְפְּשֵׂהוּ בְּבִגְדוֹ לֵאמֹר› (“and-manipulate-him/its in-garment-
# him/its to-say”)
# ‹שִׁכְבָה עִמִּי וַיַּעֲזֹב› (“lie-down-ward with-me/my and-loosen”)
# ‹בִּגְדוֹ בְּיָדָהּ וַיָּנָס› (“garment-him/its in-hand-her/its and-flit”)
# ‹וַיֵּצֵא הַחוּצָה› (“and-bring-forth the-outside-ward”)
# "[EN-AID] And she seized him by his garment, saying: Lie with me. And he
# left his garment in her hand, and fled and went outside."
m.step("Gen.39.12")
# ‹וַתִּתְפְּשֵׂהוּ בְּבִגְדוֹ לֵאמֹר› (“and-manipulate-him/its in-garment-
# him/its to-say”)
# ‹שִׁכְבָה עִמִּי› (“lie-down-ward with-me/my”)
# — woman-adonav speaks a demand — LET: shikhva-imi
m.declare("eshet_adonav", "LET",
          "shikhva_imi")
# ‹וַיַּעֲזֹב בִּגְדוֹ בְּיָדָהּ› (“and-loosen garment-him/its in-hand-
# her/its”)
# ‹וַיָּנָס וַיֵּצֵא הַחוּצָה› (“and-flit and-bring-forth the-outside-ward”)
# — event: loosen — agent Joseph; theme beged
m.event("azav", agent="yosef", themes=["beged"])

# -------------------------- Gen.39.13 · THE_EVIDENCE_READ ------------------
# ‹וַיְהִי כִּרְאוֹתָהּ כִּי־עָזַב› (“and-be like-see-her/its that loosen”)
# ‹בִּגְדוֹ בְּיָדָהּ וַיָּנָס› (“garment-him/its in-hand-her/its and-flit”)
# ‹הַחוּצָה› (“the-outside-ward”)
# "[EN-AID] And it was, when she saw that he had left his garment in her
# hand, and fled outside,"
m.step("Gen.39.13")
# ‹וַיְהִי כִּרְאוֹתָהּ כִּי־עָזַב› (“and-be like-see-her/its that loosen”)
# ‹בִּגְדוֹ בְּיָדָהּ› (“garment-him/its in-hand-her/its”)
# — fact holds: raata-that-loosen-bigdo-in-yadah
m.fact("raata_ki_azav_bigdo_be_yadah")

# -------------------------- Gen.39.14 · THE_HOUSEHOLD_SPEECH ---------------
# ‹וַתִּקְרָא לְאַנְשֵׁי בֵיתָהּ› (“and-call to-man house-her/its”)
# ‹וַתֹּאמֶר לָהֶם לֵאמֹר› (“and-say to-them/their to-say”)
# ‹רְאוּ הֵבִיא לָנוּ› (“see come/bring to-us/our”)
# ‹אִישׁ עִבְרִי לְצַחֶק› (“man Hebrew to-laugh-outright”)
# ‹בָּנוּ בָּא אֵלַי› (“in-us/our come/bring to-me/my”)
# ‹לִשְׁכַּב עִמִּי וָאֶקְרָא› (“to-lie-down with-me/my and-call”)
# ‹בְּקוֹל גָּדוֹל› (“in-voice/sound great”)
# "[EN-AID] that she called to the men of her house and said to them,
# saying: See — he brought us a Hebrew man to mock us; he came to me to lie
# with me, and I called with a great voice."
m.step("Gen.39.14")
# ‹רְאוּ הֵבִיא לָנוּ› (“see come/bring to-us/our”)
# ‹אִישׁ עִבְרִי לְצַחֶק› (“man Hebrew to-laugh-outright”)
# ‹בָּנוּ› (“in-us/our”)
# — fact holds: qara-to-man-veta-come/bring-lanu-man-Hebrew
m.fact("qara_le_anshe_veta_hevi_lanu_ish_ivri")

# -------------------------- Gen.39.15 · THE_RAISED_VOICE -------------------
# ‹וַיְהִי כְשָׁמְעוֹ כִּי־הֲרִימֹתִי› (“and-be like-hear-him/its that rise-
# high”)
# ‹קוֹלִי וָאֶקְרָא וַיַּעֲזֹב› (“voice/sound-me/my and-call and-loosen”)
# ‹בִּגְדוֹ אֶצְלִי וַיָּנָס› (“garment-him/its side-me/my and-flit”)
# ‹וַיֵּצֵא הַחוּצָה› (“and-bring-forth the-outside-ward”)
# "[EN-AID] And it was, when he heard that I raised my voice and called,"
m.step("Gen.39.15")
# ‹כִּי־הֲרִימֹתִי קוֹלִי וָאֶקְרָא› (“that rise-high voice/sound-me/my and-
# call”)
# — fact holds: rise-high-qoli-and-call(woman-adonav)
m.fact("harimoti_qoli_va_eqra(eshet_adonav)")

# -------------------------- Gen.39.16 · THE_GARMENT_WAITS ------------------
# ‹וַתַּנַּח בִּגְדוֹ אֶצְלָהּ› (“and-deposit garment-him/its side-her/its”)
# ‹עַד־בּוֹא אֲדֹנָיו אֶל־בֵּיתוֹ› (“until come/bring lord-him/its to house-
# him/its”)
# "[EN-AID] And she laid his garment beside her until his master came to his
# house."
m.step("Gen.39.16")
# ‹וַתַּנַּח בִּגְדוֹ אֶצְלָהּ› (“and-deposit garment-him/its side-her/its”)
# — fact holds: and-deposit-bigdo-etzlah-until-come/bring-adonav
m.fact("va_tanach_bigdo_etzlah_ad_bo_adonav")

# -------------------------- Gen.39.17 · THE_SECOND_TELLING -----------------
# ‹וַתְּדַבֵּר אֵלָיו כַּדְּבָרִים› (“and-speak to-him/its like-word/thing”)
# ‹הָאֵלֶּה לֵאמֹר בָּא־אֵלַי› (“the-these to-say come/bring to-me/my”)
# ‹הָעֶבֶד הָעִבְרִי אֲשֶׁר־הֵבֵאתָ› (“the-servant the-Hebrew which
# come/bring”)
# ‹לָּנוּ לְצַחֶק בִּי› (“to-us/our to-laugh-outright in-me/my”)
# "[EN-AID] And she spoke to him according to these words, saying: The
# Hebrew slave whom you brought us came to me, to mock me."
m.step("Gen.39.17")
# ‹בָּא־אֵלַי הָעֶבֶד הָעִבְרִי› (“come/bring to-me/my the-servant the-
# Hebrew”)
# ‹אֲשֶׁר־הֵבֵאתָ לָּנוּ לְצַחֶק› (“which come/bring to-us/our to-laugh-
# outright”)
# — fact holds: come/bring-elay-the-servant-the-Hebrew-to-laugh-outright-bi
m.fact("ba_elay_ha_eved_ha_ivri_le_tzacheq_bi")

# -------------------------- Gen.39.18 · THE_QUOTED_CRY ---------------------
# ‹וַיְהִי כַּהֲרִימִי קוֹלִי› (“and-be like-rise-high-me/my voice/sound-
# me/my”)
# ‹וָאֶקְרָא וַיַּעֲזֹב בִּגְדוֹ› (“and-call and-loosen garment-him/its”)
# ‹אֶצְלִי וַיָּנָס הַחוּצָה› (“side-me/my and-flit the-outside-ward”)
# "[EN-AID] And it was, as I raised my voice and called, that he left his
# garment beside me and fled outside."
m.step("Gen.39.18")
# ‹וַיְהִי כַּהֲרִימִי קוֹלִי› (“and-be like-rise-high-me/my voice/sound-
# me/my”)
# ‹וָאֶקְרָא› (“and-call”)
# — fact holds: like-harimi-qoli-and-loosen-bigdo-etzli
m.fact("ka_harimi_qoli_va_yaazov_bigdo_etzli")

# -------------------------- Gen.39.19 · THE_ANGER --------------------------
# ‹וַיְהִי כִשְׁמֹעַ אֲדֹנָיו› (“and-be like-hear lord-him/its”)
# ‹אֶת־דִּבְרֵי אִשְׁתּוֹ אֲשֶׁר› (“obj-marker word/thing woman-him/its
# which”)
# ‹דִּבְּרָה אֵלָיו לֵאמֹר› (“speak to-him/its to-say”)
# ‹כַּדְּבָרִים הָאֵלֶּה עָשָׂהּ› (“like-word/thing the-these make”)
# ‹לִי עַבְדֶּךָ וַיִּחַר› (“to-me/my servant-you/your and-glow”)
# ‹אַפּוֹ› (“nose-him/its”)
# "[EN-AID] And it was, when his master heard the words of his wife which
# she spoke to him, saying: According to these words your slave did to me —
# his anger burned."
m.step("Gen.39.19")
# ‹עַבְדֶּךָ וַיִּחַר› (“servant-you/your and-glow”)
# — fact holds: and-glow-apo(adonav)
m.fact("va_yichar_apo(adonav)")
# witness-tier presupposed read: master_disbelief on charon_af — read, not
# installed
m.witness_read("charon_af", "master_disbelief",
                cites=["Bereshit Rabbah 87:9"])

# -------------------------- Gen.39.20 · INTO_THE_ROUND_HOUSE ---------------
# ‹וַיִּקַּח אֲדֹנֵי יוֹסֵף› (“and-take lord Joseph”)
# ‹אֹתוֹ וַיִּתְּנֵהוּ אֶל־בֵּית› (“obj-marker-him/its and-set-him/its to
# house”)
# ‹הַסֹּהַר מְקוֹם אֲשֶׁר־אסורי› (“the-dungeon place which yoke”)
# ‹אֲסִירֵי הַמֶּלֶךְ אֲסוּרִים› (“bound the-king yoke”)
# ‹וַיְהִי־שָׁם בְּבֵית הַסֹּהַר› (“and-be there in-house the-dungeon”)
# "[EN-AID] And Joseph's master took him and gave him to the prison-house,
# the place where the king's prisoners were bound; and he was there in the
# prison-house."
m.step("Gen.39.20")
# ‹מְקוֹם אֲשֶׁר־אסורי אֲסִירֵי› (“place which yoke bound”)
# ‹הַמֶּלֶךְ אֲסוּרִים› (“the-king yoke”)
# — fact holds: netano-to-house-the-dungeon(lord-Joseph)
m.fact("netano_el_bet_ha_sohar(adone_yosef)")

# -------------------------- Gen.39.21 · CHESED_IN_THE_PIT ------------------
# ‹וַיְהִי יְהוָה אֶת־יוֹסֵף› (“and-be YHWH with Joseph”)
# ‹וַיֵּט אֵלָיו חָסֶד› (“and-stretch to-him/its kindness”)
# ‹וַיִּתֵּן חִנּוֹ בְּעֵינֵי› (“and-set graciousness-him/its in-eye”)
# ‹שַׂר בֵּית־הַסֹּהַר› (“officer house the-dungeon”)
# "[EN-AID] And the LORD was with Joseph, and extended kindness to him, and
# gave his favor in the eyes of the chief of the prison-house."
m.step("Gen.39.21")
# ‹וַיְהִי יְהוָה אֶת־יוֹסֵף› (“and-be YHWH with Joseph”)
# ‹וַיֵּט אֵלָיו חָסֶד› (“and-stretch to-him/its kindness”)
# — fact holds: and-stretch-to-him-kindness-and-chino-in-eye-officer-house-
# the-dungeon
m.fact("va_yet_elav_chased_ve_chino_be_ene_sar_bet_ha_sohar")

# -------------------------- Gen.39.22 · ALL_IN_HIS_HAND_AGAIN --------------
# ‹וַיִּתֵּן שַׂר בֵּית־הַסֹּהַר› (“and-set officer house the-dungeon”)
# ‹בְּיַד־יוֹסֵף אֵת כָּל־הָאֲסִירִם› (“in-hand Joseph obj-marker all the-
# bound”)
# ‹אֲשֶׁר בְּבֵית הַסֹּהַר› (“which in-house the-dungeon”)
# ‹וְאֵת כָּל־אֲשֶׁר עֹשִׂים› (“and-obj-marker all which make”)
# ‹שָׁם הוּא הָיָה› (“there he/it be”)
# ‹עֹשֶׂה› (“make”)
# "[EN-AID] And the chief of the prison-house gave into Joseph's hand all
# the prisoners in the prison-house; and all that they did there, he was the
# doer."
m.step("Gen.39.22")
# ‹אֵת כָּל־הָאֲסִירִם אֲשֶׁר› (“obj-marker all the-bound which”)
# ‹בְּבֵית הַסֹּהַר› (“in-house the-dungeon”)
# — fact holds: set-in-hand-Joseph-with-all-the-bound
m.fact("natan_be_yad_yosef_et_kal_ha_asirim")

# -------------------------- Gen.39.23 · THE_UNSEEN_OVERSEER ----------------
# ‹אֵין שַׂר בֵּית־הַסֹּהַר› (“there-is-not officer house the-dungeon”)
# ‹רֹאֶה אֶת־כָּל־מְאוּמָה בְּיָדוֹ› (“see obj-marker all speck in-hand-
# him/its”)
# ‹בַּאֲשֶׁר יְהוָה אִתּוֹ› (“in-who YHWH with-him/its”)
# ‹וַאֲשֶׁר־הוּא עֹשֶׂה יְהוָה› (“and-which he/it make YHWH”)
# ‹מַצְלִיחַ› (“push-forward”)
# "[EN-AID] The chief of the prison-house saw not any thing in his hand, in
# that the LORD was with him; and what he did, the LORD made prosper."
m.step("Gen.39.23")
# ‹בַּאֲשֶׁר יְהוָה אִתּוֹ› (“in-who YHWH with-him/its”)
# ‹וַאֲשֶׁר־הוּא עֹשֶׂה יְהוָה› (“and-which he/it make YHWH”)
# ‹מַצְלִיחַ› (“push-forward”)
# — fact holds: the-LORD-with-him-and-which-he/it-make-the-LORD-matzliach
m.fact("YHWH_ito_va_asher_hu_ose_YHWH_matzliach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shikhva_imi', 'shikhva_imi']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['hurad_mitzrayma_va_yiqnehu_potifar(yosef)', 'YHWH_et_yosef_ish_matzliach', 'raa_adonav_ki_YHWH_ito', 'hifqid_al_beto_ve_khol_natan_be_yado', 'berakh_YHWH_bet_ha_mitzri_biglal_yosef', 'yefe_toar_vi_yfe_mare(yosef)', 'va_yemaen_hen_adoni(yosef)', 'ekh_eese_ha_raa_ha_gedola_ve_chatati_le_Elohim', 've_lo_shama_eleha_yom_yom(yosef)', 've_en_ish_ba_bayit', 'raata_ki_azav_bigdo_be_yadah', 'qara_le_anshe_veta_hevi_lanu_ish_ivri', 'harimoti_qoli_va_eqra(eshet_adonav)', 'va_tanach_bigdo_etzlah_ad_bo_adonav', 'ba_elay_ha_eved_ha_ivri_le_tzacheq_bi', 'ka_harimi_qoli_va_yaazov_bigdo_etzli', 'va_yichar_apo(adonav)', 'netano_el_bet_ha_sohar(adone_yosef)', 'va_yet_elav_chased_ve_chino_be_ene_sar_bet_ha_sohar', 'natan_be_yad_yosef_et_kal_ha_asirim', 'YHWH_ito_va_asher_hu_ose_YHWH_matzliach'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 3
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('accompaniment_formula', 'four_seat_frame'), ('laasot_melakhto', 'errand_disputed'), ('charon_af', 'master_disbelief')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Genesis 39:2']
    assert all('four_seat_frame' not in f for f in m.WORLD["facts"])
    assert 'accompaniment_formula' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 87:7', 'Onkelos Genesis 39:11']
    assert all('errand_disputed' not in f for f in m.WORLD["facts"])
    assert 'laasot_melakhto' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 87:9']
    assert all('master_disbelief' not in f for f in m.WORLD["facts"])
    assert 'charon_af' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
