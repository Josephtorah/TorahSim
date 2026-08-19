#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_61_yehuda_tamar — 38:1-30
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_61_yehuda_tamar.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Judah and Tamar: the pledge that speaks (38:1-30)"""
from machine import Machine

m = Machine("gen_61_yehuda_tamar")

# -------------------------- Gen.38.1 · THE_DESCENT_TO_ADULLAM --------------
# וַיְהִי בָּעֵת הַהִוא וַיֵּרֶד יְהוּדָה מֵאֵת אֶחָיו וַיֵּט עַד־אִישׁ
# עֲדֻלָּמִי וּשְׁמוֹ חִירָה
# "[EN-AID] And it came to pass at that time that Judah went down from his
# brothers, and turned aside to an Adullamite man, and his name was Hirah."
m.step("Gen.38.1")
# ‹וַיְהִי בָּעֵת הַהִוא וַיֵּרֶד יְהוּדָה מֵאֵת אֶחָיו› (“and-be in-time
# that and-go-down Judah from-with brother-him/its”) — fact holds: yarad-
# from-with-echay-v(Judah)
m.fact("yarad_me_et_echay_v(yehuda)")

# -------------------------- Gen.38.2 · THE_CANAANITE_WIFE ------------------
# וַיַּרְא־שָׁם יְהוּדָה בַּת־אִישׁ כְּנַעֲנִי וּשְׁמוֹ שׁוּעַ וַיִּקָּחֶהָ
# וַיָּבֹא אֵלֶיהָ
# "[EN-AID] And Judah saw there the daughter of a Canaanite man, and his
# name was Shua; and he took her and came to her."
m.step("Gen.38.2")
# ‹וַיַּרְא־שָׁם יְהוּדָה בַּת־אִישׁ כְּנַעֲנִי וּשְׁמוֹ שׁוּעַ› (“and-see
# there Judah daughter man Kenaanite and-name-him/its Shua”) — fact holds:
# laqach-daughter-Shua(Judah)
m.fact("laqach_bat_shua(yehuda)")

# -------------------------- Gen.38.3 · THE_FATHER_NAMES_ER -----------------
# וַתַּהַר וַתֵּלֶד בֵּן וַיִּקְרָא אֶת־שְׁמוֹ עֵר
# "[EN-AID] And she conceived and bore a son; and he called his name Er."
m.step("Gen.38.3")
# ‹וַתַּהַר וַתֵּלֶד בֵּן› (“and-be-pregnant and-bear-young son”) — the
# world gains: Er
m.install("er")
# ‹וַיִּקְרָא אֶת־שְׁמוֹ עֵר› (“and-call obj-marker name-him/its Er”) —
# named: Er := Er
m.name("er", "er")

# -------------------------- Gen.38.4 · THE_MOTHER_NAMES_ONAN ---------------
# וַתַּהַר עוֹד וַתֵּלֶד בֵּן וַתִּקְרָא אֶת־שְׁמוֹ אוֹנָן
# "[EN-AID] And she conceived again and bore a son; and she called his name
# Onan."
m.step("Gen.38.4")
# ‹וַתַּהַר עוֹד וַתֵּלֶד בֵּן› (“and-be-pregnant still/again and-bear-young
# son”) — the world gains: Onan
m.install("onan")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ אוֹנָן› (“and-call obj-marker name-him/its Onan”) —
# named: Onan := Onan
m.name("onan", "onan")

# -------------------------- Gen.38.5 · THE_MOTHER_NAMES_SHELAH -------------
# וַתֹּסֶף עוֹד וַתֵּלֶד בֵּן וַתִּקְרָא אֶת־שְׁמוֹ שֵׁלָה וְהָיָה בִכְזִיב
# בְּלִדְתָּהּ אֹתוֹ
# "[EN-AID] And she yet again bore a son, and she called his name Shelah;
# and he was at Cheziv when she bore him."
m.step("Gen.38.5")
# ‹וַתֹּסֶף עוֹד וַתֵּלֶד בֵּן› (“and-add still/again and-bear-young son”) —
# the world gains: Shelah
m.install("shela")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ שֵׁלָה› (“and-call obj-marker name-him/its Shelah”)
# — named: Shelah := Shelah
m.name("shela", "shela")

# -------------------------- Gen.38.6 · TAMAR_TAKEN_FOR_ER ------------------
# וַיִּקַּח יְהוּדָה אִשָּׁה לְעֵר בְּכוֹרוֹ וּשְׁמָהּ תָּמָר
# "[EN-AID] And Judah took a wife for Er his firstborn, and her name was
# Tamar."
m.step("Gen.38.6")
# ‹וַיִּקַּח יְהוּדָה אִשָּׁה לְעֵר בְּכוֹרוֹ› (“and-take Judah woman to-Er
# firstborn-him/its”) — fact holds: laqach-woman-to-Er-bekhoro(Judah, Tamar)
m.fact("laqach_isha_le_er_bekhoro(yehuda, tamar)")

# -------------------------- Gen.38.7 · ER_DIES -----------------------------
# וַיְהִי עֵר בְּכוֹר יְהוּדָה רַע בְּעֵינֵי יְהוָה וַיְמִתֵהוּ יְהוָה
# "[EN-AID] And Er, Judah's firstborn, was evil in the eyes of the LORD; and
# the LORD put him to death."
m.step("Gen.38.7")
# ‹וַיְהִי עֵר בְּכוֹר יְהוּדָה רַע בְּעֵינֵי יְהוָה וַיְמִתֵהוּ יְהוָה›
# (“and-be Er firstborn Judah bad in-eye YHWH and-die-him/its YHWH”) — fact
# holds: bad-in-eye-the-LORD-and-yemitehu(Er)
m.fact("ra_be_ene_YHWH_va_yemitehu(er)")

# -------------------------- Gen.38.8 · THE_LEVIRATE_DEMAND -----------------
# וַיֹּאמֶר יְהוּדָה לְאוֹנָן בֹּא אֶל־אֵשֶׁת אָחִיךָ וְיַבֵּם אֹתָהּ
# וְהָקֵם זֶרַע לְאָחִיךָ
# "[EN-AID] And Judah said to Onan: Come to your brother's wife, and perform
# the brother's duty to her, and raise up seed for your brother."
m.step("Gen.38.8")
# ‹בֹּא אֶל־אֵשֶׁת אָחִיךָ וְיַבֵּם אֹתָהּ וְהָקֵם זֶרַע לְאָחִיךָ›
# (“come/bring to woman brother-you/your and-marry-a-brother's-widow obj-
# marker-her/its and-arise seed to-brother-you/your”) — Judah speaks a
# demand — LET: arise-seed-to-your-brother
m.declare("yehuda", "LET",
          "haqem_zera_le_achikha")

# -------------------------- Gen.38.9 · THE_SUBVERSION ----------------------
# וַיֵּדַע אוֹנָן כִּי לֹּא לוֹ יִהְיֶה הַזָּרַע וְהָיָה אִם־בָּא אֶל־אֵשֶׁת
# אָחִיו וְשִׁחֵת אַרְצָה לְבִלְתִּי נְתָן־זֶרַע לְאָחִיו
# "[EN-AID] And Onan knew that the seed would not be his; and it was, when
# he came to his brother's wife, he wasted it to the ground, so as not to
# give seed to his brother."
m.step("Gen.38.9")
# ‹וְשִׁחֵת אַרְצָה לְבִלְתִּי נְתָן־זֶרַע לְאָחִיו› (“and-decay earth-ward
# to-failure-of set seed to-brother-him/its”) — fact holds: decay-artza-so-
# as-not-set-seed(Onan)
m.fact("shichet_artza_levilti_netan_zera(onan)")

# -------------------------- Gen.38.10 · ONAN_DIES --------------------------
# וַיֵּרַע בְּעֵינֵי יְהוָה אֲשֶׁר עָשָׂה וַיָּמֶת גַּם־אֹתוֹ
# "[EN-AID] And what he did was evil in the eyes of the LORD; and He put him
# to death also."
m.step("Gen.38.10")
# ‹וַיָּמֶת גַּם־אֹתוֹ› (“and-die also obj-marker-him/its”) — fact holds:
# and-die-also-it(the-LORD)
m.fact("va_yamet_gam_oto(YHWH)")

# -------------------------- Gen.38.11 · THE_WIDOW_SEATED -------------------
# וַיֹּאמֶר יְהוּדָה לְתָמָר כַּלָּתוֹ שְׁבִי אַלְמָנָה בֵית־אָבִיךְ
# עַד־יִגְדַּל שֵׁלָה בְנִי כִּי אָמַר פֶּן־יָמוּת גַּם־הוּא כְּאֶחָיו
# וַתֵּלֶךְ תָּמָר וַתֵּשֶׁב בֵּית אָבִיהָ
# "[EN-AID] And Judah said to Tamar his daughter-in-law: Sit as a widow in
# your father's house until Shelah my son grows — for he said, lest he too
# die like his brothers. And Tamar went and sat in her father's house."
m.step("Gen.38.11")
# ‹שְׁבִי אַלְמָנָה בֵית־אָבִיךְ› (“dwell/sit widow house father-you/your”)
# — Judah speaks a demand — LET: dwell/sit-widow-house-avikh
m.declare("yehuda", "LET",
          "shevi_almana_vet_avikh")
# ‹וַתֵּלֶךְ תָּמָר וַתֵּשֶׁב בֵּית אָבִיהָ› (“and-go Tamar and-dwell/sit
# house father-her/its”) — demand settled (popped from the queue):
# dwell/sit-widow-house-avikh
m.result("shevi_almana_vet_avikh", tmark="t1")

# -------------------------- Gen.38.12 · THE_TIME_PASSES --------------------
# וַיִּרְבּוּ הַיָּמִים וַתָּמָת בַּת־שׁוּעַ אֵשֶׁת־יְהוּדָה וַיִּנָּחֶם
# יְהוּדָה וַיַּעַל עַל־גֹּזֲזֵי צֹאנוֹ הוּא וְחִירָה רֵעֵהוּ הָעֲדֻלָּמִי
# תִּמְנָתָה
# "[EN-AID] And the days multiplied, and the daughter of Shua, Judah's wife,
# died; and Judah was comforted, and went up to his sheepshearers, he and
# Hirah his friend the Adullamite, to Timnah."
m.step("Gen.38.12")
# ‹וַיִּרְבּוּ הַיָּמִים וַתָּמָת בַּת־שׁוּעַ אֵשֶׁת־יְהוּדָה וַיִּנָּחֶם
# יְהוּדָה› (“and-multiply the-day and-die daughter Shua woman Judah and-
# sigh Judah”) — fact holds: and-die-daughter-Shua-and-sigh(Judah)
m.fact("va_tamat_bat_shua_va_yinachem(yehuda)")

# -------------------------- Gen.38.13 · THE_TELLING ------------------------
# וַיֻּגַּד לְתָמָר לֵאמֹר הִנֵּה חָמִיךְ עֹלֶה תִמְנָתָה לָגֹז צֹאנוֹ
# "[EN-AID] And it was told to Tamar, saying: Behold, your father-in-law
# goes up to Timnah to shear his flock."
m.step("Gen.38.13")
# ‹וַיֻּגַּד לְתָמָר לֵאמֹר› (“and-tell to-Tamar to-say”) — fact holds:
# hugad-to-Tamar-chamikh-go-up-timnata
m.fact("hugad_le_tamar_chamikh_ole_timnata")

# -------------------------- Gen.38.14 · THE_GARMENTS_SWAPPED ---------------
# וַתָּסַר בִּגְדֵי אַלְמְנוּתָהּ מֵעָלֶיהָ וַתְּכַס בַּצָּעִיף
# וַתִּתְעַלָּף וַתֵּשֶׁב בְּפֶתַח עֵינַיִם אֲשֶׁר עַל־דֶּרֶךְ תִּמְנָתָה
# כִּי רָאֲתָה כִּי־גָדַל שֵׁלָה וְהִוא לֹא־נִתְּנָה לוֹ לְאִשָּׁה
# "[EN-AID] And she removed her widow's garments from upon her, and covered
# herself with the veil and wrapped herself, and sat at the opening of Enaim
# which is on the road to Timnah — for she saw that Shelah was grown, and
# she had not been given to him as a wife."
m.step("Gen.38.14")
# ‹כִּי רָאֲתָה כִּי־גָדַל שֵׁלָה וְהִוא לֹא־נִתְּנָה לוֹ לְאִשָּׁה› (“that
# see that be-large Shelah and-he/it not set to-him/its to-woman”) — fact
# holds: yashva-in-opening-Enaim-that-be-large-Shelah(Tamar)
m.fact("yashva_be_fetach_enayim_ki_gadal_shela(tamar)")

# -------------------------- Gen.38.15 · THE_MISREADING ---------------------
# וַיִּרְאֶהָ יְהוּדָה וַיַּחְשְׁבֶהָ לְזוֹנָה כִּי כִסְּתָה פָּנֶיהָ
# "[EN-AID] And Judah saw her, and thought her a harlot, for she had covered
# her face."
m.step("Gen.38.15")
# ‹וַיִּרְאֶהָ יְהוּדָה וַיַּחְשְׁבֶהָ לְזוֹנָה› (“and-see-her/its Judah
# and-plait-her/its to-commit-adultery”) — fact holds: and-yachsheveha-to-
# commit-adultery(Judah)
m.fact("va_yachsheveha_le_zona(yehuda)")

# -------------------------- Gen.38.16 · THE_ROADSIDE_REQUEST ---------------
# וַיֵּט אֵלֶיהָ אֶל־הַדֶּרֶךְ וַיֹּאמֶר הָבָה־נָּא אָבוֹא אֵלַיִךְ כִּי לֹא
# יָדַע כִּי כַלָּתוֹ הִוא וַתֹּאמֶר מַה־תִּתֶּן־לִּי כִּי תָבוֹא אֵלָי
# "[EN-AID] And he turned to her by the road and said: Come now, let me come
# to you — for he did not know that she was his daughter-in-law. And she
# said: What will you give me, that you come to me?"
m.step("Gen.38.16")
# ‹וַיֹּאמֶר הָבָה־נָּא אָבוֹא אֵלַיִךְ› (“and-say give-ward please
# come/bring to-you/your”) — Judah speaks a demand — LET: hava-come/bring-
# elayikh
m.declare("yehuda", "LET",
          "hava_avo_elayikh")

# -------------------------- Gen.38.17 · THE_KID_AND_THE_PLEDGE_ASKED -------
# וַיֹּאמֶר אָנֹכִי אֲשַׁלַּח גְּדִי־עִזִּים מִן־הַצֹּאן וַתֹּאמֶר
# אִם־תִּתֵּן עֵרָבוֹן עַד שָׁלְחֶךָ
# "[EN-AID] And he said: I will send a kid of the goats from the flock. And
# she said: If you give a pledge until you send it."
m.step("Gen.38.17")
# ‹וַיֹּאמֶר אָנֹכִי אֲשַׁלַּח גְּדִי־עִזִּים מִן־הַצֹּאן› (“and-say send
# young-goat she-goat from the-flock”) — fact holds: young-goat-she-goat-
# and-pawn(shrub)
m.fact("gedi_izim_ve_eravon(siach)")

# -------------------------- Gen.38.18 · THE_THREE_PLEDGES_AND_THE_CONCEPTION -
# וַיֹּאמֶר מָה הָעֵרָבוֹן אֲשֶׁר אֶתֶּן־לָּךְ וַתֹּאמֶר חֹתָמְךָ
# וּפְתִילֶךָ וּמַטְּךָ אֲשֶׁר בְּיָדֶךָ וַיִּתֶּן־לָּהּ וַיָּבֹא אֵלֶיהָ
# וַתַּהַר לוֹ
# "[EN-AID] And he said: What is the pledge that I shall give you? And she
# said: Your seal and your cord and your staff that is in your hand. And he
# gave them to her, and came to her, and she conceived by him."
m.step("Gen.38.18")
# ‹וַיִּתֶּן־לָּהּ וַיָּבֹא אֵלֶיהָ וַתַּהַר לוֹ› (“and-set to-her/its and-
# come/bring to-her/its and-be-pregnant to-him/its”) — demand settled
# (popped from the queue): hava-come/bring-elayikh
m.result("hava_avo_elayikh", tmark="t1")
# ‹וַתֹּאמֶר חֹתָמְךָ וּפְתִילֶךָ וּמַטְּךָ אֲשֶׁר בְּיָדֶךָ› (“and-say
# signature-ring-you/your and-twine-you/your and-staff/tribe-you/your which
# in-hand-you/your”) — fact holds: chotam-petil-staff/tribe-in-hand-Tamar
m.fact("chotam_petil_mate_be_yad_tamar")

# -------------------------- Gen.38.19 · THE_GARMENTS_RETURNED --------------
# וַתָּקָם וַתֵּלֶךְ וַתָּסַר צְעִיפָהּ מֵעָלֶיהָ וַתִּלְבַּשׁ בִּגְדֵי
# אַלְמְנוּתָהּ
# "[EN-AID] And she arose and went, and removed her veil from upon her, and
# put on the garments of her widowhood."
m.step("Gen.38.19")
# ‹וַתָּקָם וַתֵּלֶךְ וַתָּסַר צְעִיפָהּ מֵעָלֶיהָ› (“and-arise and-go and-
# turn-aside veil-her/its from-over-her/its”) — fact holds: shava-to-vigde-
# almenuta(Tamar)
m.fact("shava_le_vigde_almenuta(tamar)")

# -------------------------- Gen.38.20 · THE_KID_SENT_SHE_IS_NOT_FOUND ------
# וַיִּשְׁלַח יְהוּדָה אֶת־גְּדִי הָעִזִּים בְּיַד רֵעֵהוּ הָעֲדֻלָּמִי
# לָקַחַת הָעֵרָבוֹן מִיַּד הָאִשָּׁה וְלֹא מְצָאָהּ
# "[EN-AID] And Judah sent the kid of the goats by the hand of his friend
# the Adullamite, to take the pledge from the woman's hand — and he did not
# find her."
m.step("Gen.38.20")
# ‹וַיִּשְׁלַח יְהוּדָה אֶת־גְּדִי הָעִזִּים בְּיַד רֵעֵהוּ הָעֲדֻלָּמִי›
# (“and-send Judah obj-marker young-goat the-she-goat in-hand associate-
# him/its the-Adullamite”) — fact holds: shalach-the-young-goat-and-not-
# metzaa(Hirah)
m.fact("shalach_ha_gedi_ve_lo_metzaa(chira)")

# -------------------------- Gen.38.21 · THE_ASKING -------------------------
# וַיִּשְׁאַל אֶת־אַנְשֵׁי מְקֹמָהּ לֵאמֹר אַיֵּה הַקְּדֵשָׁה הִוא
# בָעֵינַיִם עַל־הַדָּרֶךְ וַיֹּאמְרוּ לֹא־הָיְתָה בָזֶה קְדֵשָׁה
# "[EN-AID] And he asked the men of her place, saying: Where is the
# consecrated one, she at Enaim by the road? And they said: There was no
# consecrated one here."
m.step("Gen.38.21")
# ‹לֵאמֹר אַיֵּה הַקְּדֵשָׁה הִוא בָעֵינַיִם עַל־הַדָּרֶךְ› (“to-say where?
# the-female-devotee he/it in-Enaim over the-way/road”) — fact holds: ayeh-
# the-female-devotee-not-be(man-meqoma)
m.fact("ayeh_ha_qedesha_lo_hayta(anshe_meqoma)")

# -------------------------- Gen.38.22 · THE_REPORT_BACK --------------------
# וַיָּשָׁב אֶל־יְהוּדָה וַיֹּאמֶר לֹא מְצָאתִיהָ וְגַם אַנְשֵׁי הַמָּקוֹם
# אָמְרוּ לֹא־הָיְתָה בָזֶה קְדֵשָׁה
# "[EN-AID] And he returned to Judah and said: I have not found her; and
# also the men of the place said, There was no consecrated one here."
m.step("Gen.38.22")
# ‹וַיָּשָׁב אֶל־יְהוּדָה וַיֹּאמֶר לֹא מְצָאתִיהָ› (“and-return to Judah
# and-say not find-her/its”) — fact holds: not-metzatiha-and-also-man-the-
# place(Hirah)
m.fact("lo_metzatiha_ve_gam_anshe_ha_maqom(chira)")

# -------------------------- Gen.38.23 · LEST_WE_BE_SCORNED -----------------
# וַיֹּאמֶר יְהוּדָה תִּקַּח־לָהּ פֶּן נִהְיֶה לָבוּז הִנֵּה שָׁלַחְתִּי
# הַגְּדִי הַזֶּה וְאַתָּה לֹא מְצָאתָהּ
# "[EN-AID] And Judah said: Let her keep them, lest we become a scorn;
# behold, I sent this kid, and you did not find her."
m.step("Gen.38.23")
# ‹תִּקַּח־לָהּ פֶּן נִהְיֶה לָבוּז› (“take to-her/its lest be to-
# disrespect”) — fact holds: take-lah-lest-be-to-disrespect(Judah)
m.fact("tiqach_lah_pen_nihye_la_vuz(yehuda)")

# -------------------------- Gen.38.24 · THE_VERDICT ------------------------
# וַיְהִי כְּמִשְׁלֹשׁ חֳדָשִׁים וַיֻּגַּד לִיהוּדָה לֵאמֹר זָנְתָה תָּמָר
# כַּלָּתֶךָ וְגַם הִנֵּה הָרָה לִזְנוּנִים וַיֹּאמֶר יְהוּדָה הוֹצִיאוּהָ
# וְתִשָּׂרֵף
# "[EN-AID] And it was, about three months, and it was told to Judah,
# saying: Tamar your daughter-in-law has played the harlot, and behold, she
# is with child by harlotry. And Judah said: Bring her out and let her be
# burned."
m.step("Gen.38.24")
# ‹וַיֹּאמֶר יְהוּדָה הוֹצִיאוּהָ וְתִשָּׂרֵף› (“and-say Judah bring-forth-
# her/its and-be-on-fire”) — Judah speaks a demand — LET: hotziu-the-and-be-
# on-fire
m.declare("yehuda", "LET",
          "hotziu_ha_ve_tisaref")

# -------------------------- Gen.38.25 · HAKER_NA_RETURNS -------------------
# הִוא מוּצֵאת וְהִיא שָׁלְחָה אֶל־חָמִיהָ לֵאמֹר לְאִישׁ אֲשֶׁר־אֵלֶּה לּוֹ
# אָנֹכִי הָרָה וַתֹּאמֶר הַכֶּר־נָא לְמִי הַחֹתֶמֶת וְהַפְּתִילִים
# וְהַמַּטֶּה הָאֵלֶּה
# "[EN-AID] She was brought out, and she sent to her father-in-law, saying:
# By the man whose these are, I am with child. And she said: Recognize,
# please, whose are the seal and the cords and the staff, these."
m.step("Gen.38.25")
# ‹וַתֹּאמֶר הַכֶּר־נָא לְמִי הַחֹתֶמֶת› (“and-say scrutinize please to-who?
# the-seal”) — Tamar speaks a demand — LET: scrutinize-please-to-who?
m.declare("tamar", "LET",
          "haker_na_le_mi")
# ‹הִוא מוּצֵאת› (“he/it bring-forth”) — fact holds: that-bring-forth-and-
# the-twine(Tamar)
m.fact("hiv_mutzet_ve_ha_petilim(tamar)")

# -------------------------- Gen.38.26 · THE_RECOGNITION_AND_CONFESSION -----
# וַיַּכֵּר יְהוּדָה וַיֹּאמֶר צָדְקָה מִמֶּנִּי כִּי־עַל־כֵּן
# לֹא־נְתַתִּיהָ לְשֵׁלָה בְנִי וְלֹא־יָסַף עוֹד לְדַעְתָּה
# "[EN-AID] And Judah recognized, and said: She is more righteous than I,
# for therefore I did not give her to Shelah my son. And he did not know her
# again any more."
m.step("Gen.38.26")
# ‹וַיַּכֵּר יְהוּדָה וַיֹּאמֶר צָדְקָה מִמֶּנִּי› (“and-scrutinize Judah
# and-say be-right from-me/my”) — demand settled (popped from the queue):
# scrutinize-please-to-who?
m.result("haker_na_le_mi", tmark="t2")

# -------------------------- Gen.38.27 · THE_TWINS_DISCOVERED ---------------
# וַיְהִי בְּעֵת לִדְתָּהּ וְהִנֵּה תְאוֹמִים בְּבִטְנָהּ
# "[EN-AID] And it came to pass at the time of her bearing, and behold,
# twins in her womb."
m.step("Gen.38.27")
# ‹וְהִנֵּה תְאוֹמִים בְּבִטְנָהּ› (“and-behold twin in-belly-her/its”) —
# demand settled (popped from the queue): arise-seed-to-your-brother
m.result("haqem_zera_le_achikha", tmark="t3")

# -------------------------- Gen.38.28 · THE_SCARLET_THREAD -----------------
# וַיְהִי בְלִדְתָּהּ וַיִּתֶּן־יָד וַתִּקַּח הַמְיַלֶּדֶת וַתִּקְשֹׁר
# עַל־יָדוֹ שָׁנִי לֵאמֹר זֶה יָצָא רִאשֹׁנָה
# "[EN-AID] And it was in her bearing, that one put out a hand; and the
# midwife took and bound on his hand scarlet, saying: This came out first."
m.step("Gen.38.28")
# ‹וַיִּתֶּן־יָד וַתִּקַּח הַמְיַלֶּדֶת וַתִּקְשֹׁר עַל־יָדוֹ שָׁנִי› (“and-
# set hand and-take the-bear-young and-tie over hand-him/its crimson”) —
# fact holds: and-set-hand-and-tie-crimson(the-bear-young)
m.fact("va_yiten_yad_va_tiqshor_shani(ha_meyaledet)")

# -------------------------- Gen.38.29 · PERETZ_NAMED -----------------------
# וַיְהִי כְּמֵשִׁיב יָדוֹ וְהִנֵּה יָצָא אָחִיו וַתֹּאמֶר מַה־פָּרַצְתָּ
# עָלֶיךָ פָּרֶץ וַיִּקְרָא שְׁמוֹ פָּרֶץ
# "[EN-AID] And it was, as he drew back his hand, behold, his brother came
# out; and she said: How have you breached! Upon you a breach. And he called
# his name Peretz."
m.step("Gen.38.29")
# ‹וְהִנֵּה יָצָא אָחִיו› (“and-behold bring-forth brother-him/its”) — the
# world gains: break
m.install("paretz")
# ‹וַיִּקְרָא שְׁמוֹ פָּרֶץ› (“and-call name-him/its Perez”) — named: break
# := break
m.name("paretz", "paretz")

# -------------------------- Gen.38.30 · ZERACH_NAMED -----------------------
# וְאַחַר יָצָא אָחִיו אֲשֶׁר עַל־יָדוֹ הַשָּׁנִי וַיִּקְרָא שְׁמוֹ זָרַח
# "[EN-AID] And afterward his brother came out, on whose hand was the
# scarlet; and he called his name Zerach."
m.step("Gen.38.30")
# ‹וְאַחַר יָצָא אָחִיו› (“and-after bring-forth brother-him/its”) — the
# world gains: Zarah
m.install("zarach")
# ‹וַיִּקְרָא שְׁמוֹ זָרַח› (“and-call name-him/its Zarah”) — named: Zarah
# := Zarah
m.name("zarach", "zarach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'zarach', 'onan', 'er', 'paretz', 'shela'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'er': 'er', 'onan': 'onan', 'shela': 'shela', 'paretz': 'paretz', 'zarach': 'zarach'}
    assert m.REGISTRY["writes"] == 5
    assert m.tests_list() == []
    assert m.open_demands() == ['hotziu_ha_ve_tisaref']
    assert len(m.SPECS["log"]) == 5
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['yarad_me_et_echay_v(yehuda)', 'laqach_bat_shua(yehuda)', 'laqach_isha_le_er_bekhoro(yehuda, tamar)', 'ra_be_ene_YHWH_va_yemitehu(er)', 'shichet_artza_levilti_netan_zera(onan)', 'va_yamet_gam_oto(YHWH)', 'va_tamat_bat_shua_va_yinachem(yehuda)', 'hugad_le_tamar_chamikh_ole_timnata', 'yashva_be_fetach_enayim_ki_gadal_shela(tamar)', 'va_yachsheveha_le_zona(yehuda)', 'gedi_izim_ve_eravon(siach)', 'chotam_petil_mate_be_yad_tamar', 'shava_le_vigde_almenuta(tamar)', 'shalach_ha_gedi_ve_lo_metzaa(chira)', 'ayeh_ha_qedesha_lo_hayta(anshe_meqoma)', 'lo_metzatiha_ve_gam_anshe_ha_maqom(chira)', 'tiqach_lah_pen_nihye_la_vuz(yehuda)', 'hiv_mutzet_ve_ha_petilim(tamar)', 'va_yiten_yad_va_tiqshor_shani(ha_meyaledet)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
