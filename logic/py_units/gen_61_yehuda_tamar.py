#!/usr/bin/env python3
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
# ‹וַיְהִי בָּעֵת הַהִוא› (“and-be in-time that”)
# ‹וַיֵּרֶד יְהוּדָה מֵאֵת› (“and-go-down Judah from-with”)
# ‹אֶחָיו וַיֵּט עַד־אִישׁ› (“brother-him/its and-stretch until man”)
# ‹עֲדֻלָּמִי וּשְׁמוֹ חִירָה› (“Adullamite and-name-him/its Hirah”)
# "[EN-AID] And it came to pass at that time that Judah went down from his
# brothers, and turned aside to an Adullamite man, and his name was Hirah."
m.step("Gen.38.1")
# ‹וַיְהִי בָּעֵת הַהִוא› (“and-be in-time that”)
# ‹וַיֵּרֶד יְהוּדָה מֵאֵת› (“and-go-down Judah from-with”)
# ‹אֶחָיו› (“brother-him/its”)
# — fact holds: yarad-from-with-echay-v(Judah)
m.fact("yarad_me_et_echay_v(yehuda)")

# -------------------------- Gen.38.2 · THE_CANAANITE_WIFE ------------------
# ‹וַיַּרְא־שָׁם יְהוּדָה בַּת־אִישׁ› (“and-see there Judah daughter man”)
# ‹כְּנַעֲנִי וּשְׁמוֹ שׁוּעַ› (“Kenaanite and-name-him/its Shua”)
# ‹וַיִּקָּחֶהָ וַיָּבֹא אֵלֶיהָ› (“and-take-her/its and-come/bring to-
# her/its”)
# "[EN-AID] And Judah saw there the daughter of a Canaanite man, and his
# name was Shua; and he took her and came to her."
m.step("Gen.38.2")
# ‹וַיַּרְא־שָׁם יְהוּדָה בַּת־אִישׁ› (“and-see there Judah daughter man”)
# ‹כְּנַעֲנִי וּשְׁמוֹ שׁוּעַ› (“Kenaanite and-name-him/its Shua”)
# — fact holds: laqach-daughter-Shua(Judah)
m.fact("laqach_bat_shua(yehuda)")

# -------------------------- Gen.38.3 · THE_FATHER_NAMES_ER -----------------
# ‹וַתַּהַר וַתֵּלֶד בֵּן› (“and-be-pregnant and-bear-young son”)
# ‹וַיִּקְרָא אֶת־שְׁמוֹ עֵר› (“and-call obj-marker name-him/its Er”)
# "[EN-AID] And she conceived and bore a son; and he called his name Er."
m.step("Gen.38.3")
# ‹וַתַּהַר וַתֵּלֶד בֵּן› (“and-be-pregnant and-bear-young son”)
# — the world gains: Er
m.install("er")
# ‹וַיִּקְרָא אֶת־שְׁמוֹ עֵר› (“and-call obj-marker name-him/its Er”)
# — named: Er := Er
m.name("er", "er")

# -------------------------- Gen.38.4 · THE_MOTHER_NAMES_ONAN ---------------
# ‹וַתַּהַר עוֹד וַתֵּלֶד› (“and-be-pregnant still/again and-bear-young”)
# ‹בֵּן וַתִּקְרָא אֶת־שְׁמוֹ› (“son and-call obj-marker name-him/its”)
# ‹אוֹנָן› (“Onan”)
# "[EN-AID] And she conceived again and bore a son; and she called his name
# Onan."
m.step("Gen.38.4")
# ‹וַתַּהַר עוֹד וַתֵּלֶד› (“and-be-pregnant still/again and-bear-young”)
# ‹בֵּן› (“son”)
# — the world gains: Onan
m.install("onan")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ אוֹנָן› (“and-call obj-marker name-him/its Onan”)
# — named: Onan := Onan
m.name("onan", "onan")

# -------------------------- Gen.38.5 · THE_MOTHER_NAMES_SHELAH -------------
# ‹וַתֹּסֶף עוֹד וַתֵּלֶד› (“and-add still/again and-bear-young”)
# ‹בֵּן וַתִּקְרָא אֶת־שְׁמוֹ› (“son and-call obj-marker name-him/its”)
# ‹שֵׁלָה וְהָיָה בִכְזִיב› (“Shelah and-be in-Chezib”)
# ‹בְּלִדְתָּהּ אֹתוֹ› (“in-bear-young-her/its obj-marker-him/its”)
# "[EN-AID] And she yet again bore a son, and she called his name Shelah;
# and he was at Cheziv when she bore him."
m.step("Gen.38.5")
# ‹וַתֹּסֶף עוֹד וַתֵּלֶד› (“and-add still/again and-bear-young”)
# ‹בֵּן› (“son”)
# — the world gains: Shelah
m.install("shela")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ שֵׁלָה› (“and-call obj-marker name-him/its Shelah”)
# — named: Shelah := Shelah
m.name("shela", "shela")

# -------------------------- Gen.38.6 · TAMAR_TAKEN_FOR_ER ------------------
# ‹וַיִּקַּח יְהוּדָה אִשָּׁה› (“and-take Judah woman”)
# ‹לְעֵר בְּכוֹרוֹ וּשְׁמָהּ› (“to-Er firstborn-him/its and-name-her/its”)
# ‹תָּמָר› (“Tamar”)
# "[EN-AID] And Judah took a wife for Er his firstborn, and her name was
# Tamar."
m.step("Gen.38.6")
# ‹וַיִּקַּח יְהוּדָה אִשָּׁה› (“and-take Judah woman”)
# ‹לְעֵר בְּכוֹרוֹ› (“to-Er firstborn-him/its”)
# — fact holds: laqach-woman-to-Er-bekhoro(Judah, Tamar)
m.fact("laqach_isha_le_er_bekhoro(yehuda, tamar)")

# -------------------------- Gen.38.7 · ER_DIES -----------------------------
# ‹וַיְהִי עֵר בְּכוֹר› (“and-be Er firstborn”)
# ‹יְהוּדָה רַע בְּעֵינֵי› (“Judah bad in-eye”)
# ‹יְהוָה וַיְמִתֵהוּ יְהוָה› (“YHWH and-die-him/its YHWH”)
# "[EN-AID] And Er, Judah's firstborn, was evil in the eyes of the LORD; and
# the LORD put him to death."
m.step("Gen.38.7")
# ‹וַיְהִי עֵר בְּכוֹר› (“and-be Er firstborn”)
# ‹יְהוּדָה רַע בְּעֵינֵי› (“Judah bad in-eye”)
# ‹יְהוָה וַיְמִתֵהוּ יְהוָה› (“YHWH and-die-him/its YHWH”)
# — fact holds: bad-in-eye-the-LORD-and-yemitehu(Er)
m.fact("ra_be_ene_YHWH_va_yemitehu(er)")

# -------------------------- Gen.38.8 · THE_LEVIRATE_DEMAND -----------------
# ‹וַיֹּאמֶר יְהוּדָה לְאוֹנָן› (“and-say Judah to-Onan”)
# ‹בֹּא אֶל־אֵשֶׁת אָחִיךָ› (“come/bring to woman brother-you/your”)
# ‹וְיַבֵּם אֹתָהּ וְהָקֵם› (“and-marry-a-brother's-widow obj-marker-her/its
# and-arise”)
# ‹זֶרַע לְאָחִיךָ› (“seed to-brother-you/your”)
# "[EN-AID] And Judah said to Onan: Come to your brother's wife, and perform
# the brother's duty to her, and raise up seed for your brother."
m.step("Gen.38.8")
# ‹בֹּא אֶל־אֵשֶׁת אָחִיךָ› (“come/bring to woman brother-you/your”)
# ‹וְיַבֵּם אֹתָהּ וְהָקֵם› (“and-marry-a-brother's-widow obj-marker-her/its
# and-arise”)
# ‹זֶרַע לְאָחִיךָ› (“seed to-brother-you/your”)
# — Judah speaks a demand — LET: arise-seed-to-your-brother
m.declare("yehuda", "LET",
          "haqem_zera_le_achikha")
# witness-tier presupposed read: first_performance on yibum — read, not
# installed
m.witness_read("yibum", "first_performance",
                cites=["Bereshit Rabbah 85:5"])

# -------------------------- Gen.38.9 · THE_SUBVERSION ----------------------
# ‹וַיֵּדַע אוֹנָן כִּי› (“and-know Onan that”)
# ‹לֹּא לוֹ יִהְיֶה› (“not to-him/its be”)
# ‹הַזָּרַע וְהָיָה אִם־בָּא› (“the-seed and-be if come/bring”)
# ‹אֶל־אֵשֶׁת אָחִיו וְשִׁחֵת› (“to woman brother-him/its and-decay”)
# ‹אַרְצָה לְבִלְתִּי נְתָן־זֶרַע› (“earth-ward to-failure-of set seed”)
# ‹לְאָחִיו› (“to-brother-him/its”)
# "[EN-AID] And Onan knew that the seed would not be his; and it was, when
# he came to his brother's wife, he wasted it to the ground, so as not to
# give seed to his brother."
m.step("Gen.38.9")
# ‹וְשִׁחֵת אַרְצָה לְבִלְתִּי› (“and-decay earth-ward to-failure-of”)
# ‹נְתָן־זֶרַע לְאָחִיו› (“set seed to-brother-him/its”)
# — fact holds: decay-artza-so-as-not-set-seed(Onan)
m.fact("shichet_artza_levilti_netan_zera(onan)")
# witness-tier presupposed read: er_onan_acts on ve_shichet_artzah — read,
# not installed
m.witness_read("ve_shichet_artzah", "er_onan_acts",
                cites=["Yevamot 34b:2", "Yevamot 34b:3", "Yevamot 34b:4", "Yevamot 34b:5"])

# -------------------------- Gen.38.10 · ONAN_DIES --------------------------
# ‹וַיֵּרַע בְּעֵינֵי יְהוָה› (“and-spoil in-eye YHWH”)
# ‹אֲשֶׁר עָשָׂה וַיָּמֶת› (“which make and-die”)
# ‹גַּם־אֹתוֹ› (“also obj-marker-him/its”)
# "[EN-AID] And what he did was evil in the eyes of the LORD; and He put him
# to death also."
m.step("Gen.38.10")
# ‹וַיָּמֶת גַּם־אֹתוֹ› (“and-die also obj-marker-him/its”)
# — fact holds: and-die-also-it(the-LORD)
m.fact("va_yamet_gam_oto(YHWH)")

# -------------------------- Gen.38.11 · THE_WIDOW_SEATED -------------------
# ‹וַיֹּאמֶר יְהוּדָה לְתָמָר› (“and-say Judah to-Tamar”)
# ‹כַּלָּתוֹ שְׁבִי אַלְמָנָה› (“bride-him/its dwell/sit widow”)
# ‹בֵית־אָבִיךְ עַד־יִגְדַּל שֵׁלָה› (“house father-you/your until be-large
# Shelah”)
# ‹בְנִי כִּי אָמַר› (“son-me/my that say”)
# ‹פֶּן־יָמוּת גַּם־הוּא כְּאֶחָיו› (“lest die also he/it like-brother-
# him/its”)
# ‹וַתֵּלֶךְ תָּמָר וַתֵּשֶׁב› (“and-go Tamar and-dwell/sit”)
# ‹בֵּית אָבִיהָ› (“house father-her/its”)
# "[EN-AID] And Judah said to Tamar his daughter-in-law: Sit as a widow in
# your father's house until Shelah my son grows — for he said, lest he too
# die like his brothers. And Tamar went and sat in her father's house."
m.step("Gen.38.11")
# ‹שְׁבִי אַלְמָנָה בֵית־אָבִיךְ› (“dwell/sit widow house father-you/your”)
# — Judah speaks a demand — LET: dwell/sit-widow-house-avikh
m.declare("yehuda", "LET",
          "shevi_almana_vet_avikh")
# ‹וַתֵּלֶךְ תָּמָר וַתֵּשֶׁב› (“and-go Tamar and-dwell/sit”)
# ‹בֵּית אָבִיהָ› (“house father-her/its”)
# — demand settled (popped from the queue): dwell/sit-widow-house-avikh
m.result("shevi_almana_vet_avikh", tmark="t1")

# -------------------------- Gen.38.12 · THE_TIME_PASSES --------------------
# ‹וַיִּרְבּוּ הַיָּמִים וַתָּמָת› (“and-multiply the-day and-die”)
# ‹בַּת־שׁוּעַ אֵשֶׁת־יְהוּדָה וַיִּנָּחֶם› (“daughter Shua woman Judah and-
# sigh”)
# ‹יְהוּדָה וַיַּעַל עַל־גֹּזֲזֵי› (“Judah and-go-up over cut-off”)
# ‹צֹאנוֹ הוּא וְחִירָה› (“flock-him/its he/it and-Hirah”)
# ‹רֵעֵהוּ הָעֲדֻלָּמִי תִּמְנָתָה› (“associate-him/its the-Adullamite
# Timnah-ward”)
# "[EN-AID] And the days multiplied, and the daughter of Shua, Judah's wife,
# died; and Judah was comforted, and went up to his sheepshearers, he and
# Hirah his friend the Adullamite, to Timnah."
m.step("Gen.38.12")
# ‹וַיִּרְבּוּ הַיָּמִים וַתָּמָת› (“and-multiply the-day and-die”)
# ‹בַּת־שׁוּעַ אֵשֶׁת־יְהוּדָה וַיִּנָּחֶם› (“daughter Shua woman Judah and-
# sigh”)
# ‹יְהוּדָה› (“Judah”)
# — fact holds: and-die-daughter-Shua-and-sigh(Judah)
m.fact("va_tamat_bat_shua_va_yinachem(yehuda)")

# -------------------------- Gen.38.13 · THE_TELLING ------------------------
# ‹וַיֻּגַּד לְתָמָר לֵאמֹר› (“and-tell to-Tamar to-say”)
# ‹הִנֵּה חָמִיךְ עֹלֶה› (“behold father-in-law-you/your go-up”)
# ‹תִמְנָתָה לָגֹז צֹאנוֹ› (“Timnah-ward to-cut-off flock-him/its”)
# "[EN-AID] And it was told to Tamar, saying: Behold, your father-in-law
# goes up to Timnah to shear his flock."
m.step("Gen.38.13")
# ‹וַיֻּגַּד לְתָמָר לֵאמֹר› (“and-tell to-Tamar to-say”)
# — fact holds: hugad-to-Tamar-chamikh-go-up-timnata
m.fact("hugad_le_tamar_chamikh_ole_timnata")

# -------------------------- Gen.38.14 · THE_GARMENTS_SWAPPED ---------------
# ‹וַתָּסַר בִּגְדֵי אַלְמְנוּתָהּ› (“and-turn-aside garment concrete-
# her/its”)
# ‹מֵעָלֶיהָ וַתְּכַס בַּצָּעִיף› (“from-over-her/its and-plump in-veil”)
# ‹וַתִּתְעַלָּף וַתֵּשֶׁב בְּפֶתַח› (“and-veil and-dwell/sit in-opening”)
# ‹עֵינַיִם אֲשֶׁר עַל־דֶּרֶךְ› (“Enaim which over way/road”)
# ‹תִּמְנָתָה כִּי רָאֲתָה› (“Timnah-ward that see”)
# ‹כִּי־גָדַל שֵׁלָה וְהִוא› (“that be-large Shelah and-he/it”)
# ‹לֹא־נִתְּנָה לוֹ לְאִשָּׁה› (“not set to-him/its to-woman”)
# "[EN-AID] And she removed her widow's garments from upon her, and covered
# herself with the veil and wrapped herself, and sat at the opening of Enaim
# which is on the road to Timnah — for she saw that Shelah was grown, and
# she had not been given to him as a wife."
m.step("Gen.38.14")
# ‹כִּי רָאֲתָה כִּי־גָדַל› (“that see that be-large”)
# ‹שֵׁלָה וְהִוא לֹא־נִתְּנָה› (“Shelah and-he/it not set”)
# ‹לוֹ לְאִשָּׁה› (“to-him/its to-woman”)
# — fact holds: yashva-in-opening-Enaim-that-be-large-Shelah(Tamar)
m.fact("yashva_be_fetach_enayim_ki_gadal_shela(tamar)")

# -------------------------- Gen.38.15 · THE_MISREADING ---------------------
# ‹וַיִּרְאֶהָ יְהוּדָה וַיַּחְשְׁבֶהָ› (“and-see-her/its Judah and-plait-
# her/its”)
# ‹לְזוֹנָה כִּי כִסְּתָה› (“to-commit-adultery that plump”)
# ‹פָּנֶיהָ› (“face-her/its”)
# "[EN-AID] And Judah saw her, and thought her a harlot, for she had covered
# her face."
m.step("Gen.38.15")
# ‹וַיִּרְאֶהָ יְהוּדָה וַיַּחְשְׁבֶהָ› (“and-see-her/its Judah and-plait-
# her/its”)
# ‹לְזוֹנָה› (“to-commit-adultery”)
# — fact holds: and-yachsheveha-to-commit-adultery(Judah)
m.fact("va_yachsheveha_le_zona(yehuda)")

# -------------------------- Gen.38.16 · THE_ROADSIDE_REQUEST ---------------
# ‹וַיֵּט אֵלֶיהָ אֶל־הַדֶּרֶךְ› (“and-stretch to-her/its to the-way/road”)
# ‹וַיֹּאמֶר הָבָה־נָּא אָבוֹא› (“and-say give-ward please come/bring”)
# ‹אֵלַיִךְ כִּי לֹא› (“to-you/your that not”)
# ‹יָדַע כִּי כַלָּתוֹ› (“know that bride-him/its”)
# ‹הִוא וַתֹּאמֶר מַה־תִּתֶּן־לִּי› (“he/it and-say what set to-me/my”)
# ‹כִּי תָבוֹא אֵלָי› (“that come/bring to-me/my”)
# "[EN-AID] And he turned to her by the road and said: Come now, let me come
# to you — for he did not know that she was his daughter-in-law. And she
# said: What will you give me, that you come to me?"
m.step("Gen.38.16")
# ‹וַיֹּאמֶר הָבָה־נָּא אָבוֹא› (“and-say give-ward please come/bring”)
# ‹אֵלַיִךְ› (“to-you/your”)
# — Judah speaks a demand — LET: hava-come/bring-elayikh
m.declare("yehuda", "LET",
          "hava_avo_elayikh")

# -------------------------- Gen.38.17 · THE_KID_AND_THE_PLEDGE_ASKED -------
# ‹וַיֹּאמֶר אָנֹכִי אֲשַׁלַּח› (“and-say send”)
# ‹גְּדִי־עִזִּים מִן־הַצֹּאן וַתֹּאמֶר› (“young-goat she-goat from the-
# flock and-say”)
# ‹אִם־תִּתֵּן עֵרָבוֹן עַד› (“if set pawn until”)
# ‹שָׁלְחֶךָ› (“send-you/your”)
# "[EN-AID] And he said: I will send a kid of the goats from the flock. And
# she said: If you give a pledge until you send it."
m.step("Gen.38.17")
# ‹וַיֹּאמֶר אָנֹכִי אֲשַׁלַּח› (“and-say send”)
# ‹גְּדִי־עִזִּים מִן־הַצֹּאן› (“young-goat she-goat from the-flock”)
# — fact holds: young-goat-she-goat-and-pawn(shrub)
m.fact("gedi_izim_ve_eravon(siach)")
# witness-tier presupposed read: repayment_pair on gedi_izzim — read, not
# installed
m.witness_read("gedi_izzim", "repayment_pair",
                cites=["Bereshit Rabbah 85:9"])

# -------------------------- Gen.38.18 · THE_THREE_PLEDGES_AND_THE_CONCEPTION -
# ‹וַיֹּאמֶר מָה הָעֵרָבוֹן› (“and-say what the-pawn”)
# ‹אֲשֶׁר אֶתֶּן־לָּךְ וַתֹּאמֶר› (“which set to-you/your and-say”)
# ‹חֹתָמְךָ וּפְתִילֶךָ וּמַטְּךָ› (“signature-ring-you/your and-twine-
# you/your and-staff/tribe-you/your”)
# ‹אֲשֶׁר בְּיָדֶךָ וַיִּתֶּן־לָּהּ› (“which in-hand-you/your and-set to-
# her/its”)
# ‹וַיָּבֹא אֵלֶיהָ וַתַּהַר› (“and-come/bring to-her/its and-be-pregnant”)
# ‹לוֹ› (“to-him/its”)
# "[EN-AID] And he said: What is the pledge that I shall give you? And she
# said: Your seal and your cord and your staff that is in your hand. And he
# gave them to her, and came to her, and she conceived by him."
m.step("Gen.38.18")
# ‹וַיִּתֶּן־לָּהּ וַיָּבֹא אֵלֶיהָ› (“and-set to-her/its and-come/bring to-
# her/its”)
# ‹וַתַּהַר לוֹ› (“and-be-pregnant to-him/its”)
# — demand settled (popped from the queue): hava-come/bring-elayikh
m.result("hava_avo_elayikh", tmark="t1")
# ‹וַתֹּאמֶר חֹתָמְךָ וּפְתִילֶךָ› (“and-say signature-ring-you/your and-
# twine-you/your”)
# ‹וּמַטְּךָ אֲשֶׁר בְּיָדֶךָ› (“and-staff/tribe-you/your which in-hand-
# you/your”)
# — fact holds: chotam-petil-staff/tribe-in-hand-Tamar
m.fact("chotam_petil_mate_be_yad_tamar")
# witness-grounded state (its own tier): three_crowns on eravon
m.witness_state("eravon", "three_crowns",
                cites=["Bereshit Rabbah 85:9"])

# -------------------------- Gen.38.19 · THE_GARMENTS_RETURNED --------------
# ‹וַתָּקָם וַתֵּלֶךְ וַתָּסַר› (“and-arise and-go and-turn-aside”)
# ‹צְעִיפָהּ מֵעָלֶיהָ וַתִּלְבַּשׁ› (“veil-her/its from-over-her/its and-
# wrap-around”)
# ‹בִּגְדֵי אַלְמְנוּתָהּ› (“garment concrete-her/its”)
# "[EN-AID] And she arose and went, and removed her veil from upon her, and
# put on the garments of her widowhood."
m.step("Gen.38.19")
# ‹וַתָּקָם וַתֵּלֶךְ וַתָּסַר› (“and-arise and-go and-turn-aside”)
# ‹צְעִיפָהּ מֵעָלֶיהָ› (“veil-her/its from-over-her/its”)
# — fact holds: shava-to-vigde-almenuta(Tamar)
m.fact("shava_le_vigde_almenuta(tamar)")

# -------------------------- Gen.38.20 · THE_KID_SENT_SHE_IS_NOT_FOUND ------
# ‹וַיִּשְׁלַח יְהוּדָה אֶת־גְּדִי› (“and-send Judah obj-marker young-goat”)
# ‹הָעִזִּים בְּיַד רֵעֵהוּ› (“the-she-goat in-hand associate-him/its”)
# ‹הָעֲדֻלָּמִי לָקַחַת הָעֵרָבוֹן› (“the-Adullamite to-take the-pawn”)
# ‹מִיַּד הָאִשָּׁה וְלֹא› (“from-hand the-woman and-not”)
# ‹מְצָאָהּ› (“find-her/its”)
# "[EN-AID] And Judah sent the kid of the goats by the hand of his friend
# the Adullamite, to take the pledge from the woman's hand — and he did not
# find her."
m.step("Gen.38.20")
# ‹וַיִּשְׁלַח יְהוּדָה אֶת־גְּדִי› (“and-send Judah obj-marker young-goat”)
# ‹הָעִזִּים בְּיַד רֵעֵהוּ› (“the-she-goat in-hand associate-him/its”)
# ‹הָעֲדֻלָּמִי› (“the-Adullamite”)
# — fact holds: shalach-the-young-goat-and-not-metzaa(Hirah)
m.fact("shalach_ha_gedi_ve_lo_metzaa(chira)")
# witness-tier presupposed read: kid_definition on gedi_ha_izim — read, not
# installed
m.witness_read("gedi_ha_izim", "kid_definition",
                cites=["Chullin 113a:19", "Chullin 113a:20", "Chullin 113b:1", "Chullin 113b:2", "Chullin 113b:3"])

# -------------------------- Gen.38.21 · THE_ASKING -------------------------
# ‹וַיִּשְׁאַל אֶת־אַנְשֵׁי מְקֹמָהּ› (“and-inquire obj-marker man place-
# her/its”)
# ‹לֵאמֹר אַיֵּה הַקְּדֵשָׁה› (“to-say where? the-female-devotee”)
# ‹הִוא בָעֵינַיִם עַל־הַדָּרֶךְ› (“he/it in-Enaim over the-way/road”)
# ‹וַיֹּאמְרוּ לֹא־הָיְתָה בָזֶה› (“and-say not be in-this”)
# ‹קְדֵשָׁה› (“female-devotee”)
# "[EN-AID] And he asked the men of her place, saying: Where is the
# consecrated one, she at Enaim by the road? And they said: There was no
# consecrated one here."
m.step("Gen.38.21")
# ‹לֵאמֹר אַיֵּה הַקְּדֵשָׁה› (“to-say where? the-female-devotee”)
# ‹הִוא בָעֵינַיִם עַל־הַדָּרֶךְ› (“he/it in-Enaim over the-way/road”)
# — fact holds: ayeh-the-female-devotee-not-be(man-meqoma)
m.fact("ayeh_ha_qedesha_lo_hayta(anshe_meqoma)")

# -------------------------- Gen.38.22 · THE_REPORT_BACK --------------------
# ‹וַיָּשָׁב אֶל־יְהוּדָה וַיֹּאמֶר› (“and-return to Judah and-say”)
# ‹לֹא מְצָאתִיהָ וְגַם› (“not find-her/its and-also”)
# ‹אַנְשֵׁי הַמָּקוֹם אָמְרוּ› (“man the-place say”)
# ‹לֹא־הָיְתָה בָזֶה קְדֵשָׁה› (“not be in-this female-devotee”)
# "[EN-AID] And he returned to Judah and said: I have not found her; and
# also the men of the place said, There was no consecrated one here."
m.step("Gen.38.22")
# ‹וַיָּשָׁב אֶל־יְהוּדָה וַיֹּאמֶר› (“and-return to Judah and-say”)
# ‹לֹא מְצָאתִיהָ› (“not find-her/its”)
# — fact holds: not-metzatiha-and-also-man-the-place(Hirah)
m.fact("lo_metzatiha_ve_gam_anshe_ha_maqom(chira)")

# -------------------------- Gen.38.23 · LEST_WE_BE_SCORNED -----------------
# ‹וַיֹּאמֶר יְהוּדָה תִּקַּח־לָהּ› (“and-say Judah take to-her/its”)
# ‹פֶּן נִהְיֶה לָבוּז› (“lest be to-disrespect”)
# ‹הִנֵּה שָׁלַחְתִּי הַגְּדִי› (“behold send the-young-goat”)
# ‹הַזֶּה וְאַתָּה לֹא› (“the-this and-you not”)
# ‹מְצָאתָהּ› (“find-her/its”)
# "[EN-AID] And Judah said: Let her keep them, lest we become a scorn;
# behold, I sent this kid, and you did not find her."
m.step("Gen.38.23")
# ‹תִּקַּח־לָהּ פֶּן נִהְיֶה› (“take to-her/its lest be”)
# ‹לָבוּז› (“to-disrespect”)
# — fact holds: take-lah-lest-be-to-disrespect(Judah)
m.fact("tiqach_lah_pen_nihye_la_vuz(yehuda)")

# -------------------------- Gen.38.24 · THE_VERDICT ------------------------
# ‹וַיְהִי כְּמִשְׁלֹשׁ חֳדָשִׁים› (“and-be like-from-three new-moon”)
# ‹וַיֻּגַּד לִיהוּדָה לֵאמֹר› (“and-tell to-Judah to-say”)
# ‹זָנְתָה תָּמָר כַּלָּתֶךָ› (“commit-adultery Tamar bride-you/your”)
# ‹וְגַם הִנֵּה הָרָה› (“and-also behold pregnant”)
# ‹לִזְנוּנִים וַיֹּאמֶר יְהוּדָה› (“to-adultery and-say Judah”)
# ‹הוֹצִיאוּהָ וְתִשָּׂרֵף› (“bring-forth-her/its and-be-on-fire”)
# "[EN-AID] And it was, about three months, and it was told to Judah,
# saying: Tamar your daughter-in-law has played the harlot, and behold, she
# is with child by harlotry. And Judah said: Bring her out and let her be
# burned."
m.step("Gen.38.24")
# ‹וַיֹּאמֶר יְהוּדָה הוֹצִיאוּהָ› (“and-say Judah bring-forth-her/its”)
# ‹וְתִשָּׂרֵף› (“and-be-on-fire”)
# — Judah speaks a demand — LET: hotziu-the-and-be-on-fire
m.declare("yehuda", "LET",
          "hotziu_ha_ve_tisaref")
# witness-tier presupposed read: pregnancy_file on ke_mishlosh_chodashim —
# read, not installed
m.witness_read("ke_mishlosh_chodashim", "pregnancy_file",
                cites=["Niddah 8b:16", "Niddah 8b:17", "Niddah 8b:18", "Niddah 28a:8", "Niddah 28a:9", "Niddah 28a:10"])

# -------------------------- Gen.38.25 · HAKER_NA_RETURNS -------------------
# ‹הִוא מוּצֵאת וְהִיא› (“he/it bring-forth and-he/it”)
# ‹שָׁלְחָה אֶל־חָמִיהָ לֵאמֹר› (“send to father-in-law-her/its to-say”)
# ‹לְאִישׁ אֲשֶׁר־אֵלֶּה לּוֹ› (“to-man which these to-him/its”)
# ‹אָנֹכִי הָרָה וַתֹּאמֶר› (“pregnant and-say”)
# ‹הַכֶּר־נָא לְמִי הַחֹתֶמֶת› (“scrutinize please to-who? the-seal”)
# ‹וְהַפְּתִילִים וְהַמַּטֶּה הָאֵלֶּה› (“and-the-twine and-the-staff/tribe
# the-these”)
# "[EN-AID] She was brought out, and she sent to her father-in-law, saying:
# By the man whose these are, I am with child. And she said: Recognize,
# please, whose are the seal and the cords and the staff, these."
m.step("Gen.38.25")
# ‹וַתֹּאמֶר הַכֶּר־נָא לְמִי› (“and-say scrutinize please to-who?”)
# ‹הַחֹתֶמֶת› (“the-seal”)
# — Tamar speaks a demand — LET: scrutinize-please-to-who?
m.declare("tamar", "LET",
          "haker_na_le_mi")
# ‹הִוא מוּצֵאת› (“he/it bring-forth”)
# — fact holds: that-bring-forth-and-the-twine(Tamar)
m.fact("hiv_mutzet_ve_ha_petilim(tamar)")
# witness-tier presupposed read: shaming_furnace on hi_mutzet — read, not
# installed
m.witness_read("hi_mutzet", "shaming_furnace",
                cites=["Sotah 10b:5", "Sotah 10b:6", "Sotah 10b:7"])

# -------------------------- Gen.38.26 · THE_RECOGNITION_AND_CONFESSION -----
# ‹וַיַּכֵּר יְהוּדָה וַיֹּאמֶר› (“and-scrutinize Judah and-say”)
# ‹צָדְקָה מִמֶּנִּי כִּי־עַל־כֵּן› (“be-right from-me/my very-widely-used-
# as-a-relati above set-upright”)
# ‹לֹא־נְתַתִּיהָ לְשֵׁלָה בְנִי› (“not set-her/its to-Shelah son-me/my”)
# ‹וְלֹא־יָסַף עוֹד לְדַעְתָּה› (“and-not add still/again to-know-her/its”)
# "[EN-AID] And Judah recognized, and said: She is more righteous than I,
# for therefore I did not give her to Shelah my son. And he did not know her
# again any more."
m.step("Gen.38.26")
# ‹וַיַּכֵּר יְהוּדָה וַיֹּאמֶר› (“and-scrutinize Judah and-say”)
# ‹צָדְקָה מִמֶּנִּי› (“be-right from-me/my”)
# — demand settled (popped from the queue): scrutinize-please-to-who?
m.result("haker_na_le_mi", tmark="t2")
# witness-tier presupposed read: voice_testimony on tzadka_mimeni — read,
# not installed
m.witness_read("tzadka_mimeni", "voice_testimony",
                cites=["Bereshit Rabbah 85:12", "Onkelos Genesis 38:26"])

# -------------------------- Gen.38.27 · THE_TWINS_DISCOVERED ---------------
# ‹וַיְהִי בְּעֵת לִדְתָּהּ› (“and-be in-time bear-young-her/its”)
# ‹וְהִנֵּה תְאוֹמִים בְּבִטְנָהּ› (“and-behold twin in-belly-her/its”)
# "[EN-AID] And it came to pass at the time of her bearing, and behold,
# twins in her womb."
m.step("Gen.38.27")
# ‹וְהִנֵּה תְאוֹמִים בְּבִטְנָהּ› (“and-behold twin in-belly-her/its”)
# — demand settled (popped from the queue): arise-seed-to-your-brother
m.result("haqem_zera_le_achikha", tmark="t3")

# -------------------------- Gen.38.28 · THE_SCARLET_THREAD -----------------
# ‹וַיְהִי בְלִדְתָּהּ וַיִּתֶּן־יָד› (“and-be in-bear-young-her/its and-set
# hand”)
# ‹וַתִּקַּח הַמְיַלֶּדֶת וַתִּקְשֹׁר› (“and-take the-bear-young and-tie”)
# ‹עַל־יָדוֹ שָׁנִי לֵאמֹר› (“over hand-him/its crimson to-say”)
# ‹זֶה יָצָא רִאשֹׁנָה› (“this bring-forth first”)
# "[EN-AID] And it was in her bearing, that one put out a hand; and the
# midwife took and bound on his hand scarlet, saying: This came out first."
m.step("Gen.38.28")
# ‹וַיִּתֶּן־יָד וַתִּקַּח הַמְיַלֶּדֶת› (“and-set hand and-take the-bear-
# young”)
# ‹וַתִּקְשֹׁר עַל־יָדוֹ שָׁנִי› (“and-tie over hand-him/its crimson”)
# — fact holds: and-set-hand-and-tie-crimson(the-bear-young)
m.fact("va_yiten_yad_va_tiqshor_shani(ha_meyaledet)")
# witness-tier presupposed read: four_forward on yad_count — read, not
# installed
m.witness_read("yad_count", "four_forward",
                cites=["Bereshit Rabbah 85:14"])

# -------------------------- Gen.38.29 · PERETZ_NAMED -----------------------
# ‹וַיְהִי כְּמֵשִׁיב יָדוֹ› (“and-be like-return hand-him/its”)
# ‹וְהִנֵּה יָצָא אָחִיו› (“and-behold bring-forth brother-him/its”)
# ‹וַתֹּאמֶר מַה־פָּרַצְתָּ עָלֶיךָ› (“and-say what break-out over-
# you/your”)
# ‹פָּרֶץ וַיִּקְרָא שְׁמוֹ› (“break and-call name-him/its”)
# ‹פָּרֶץ› (“break”)
# "[EN-AID] And it was, as he drew back his hand, behold, his brother came
# out; and she said: How have you breached! Upon you a breach. And he called
# his name Peretz."
m.step("Gen.38.29")
# ‹וְהִנֵּה יָצָא אָחִיו› (“and-behold bring-forth brother-him/its”)
# — the world gains: break
m.install("paretz")
# ‹וַיִּקְרָא שְׁמוֹ פָּרֶץ› (“and-call name-him/its Perez”)
# — named: break := break
m.name("paretz", "paretz")

# -------------------------- Gen.38.30 · ZERACH_NAMED -----------------------
# ‹וְאַחַר יָצָא אָחִיו› (“and-after bring-forth brother-him/its”)
# ‹אֲשֶׁר עַל־יָדוֹ הַשָּׁנִי› (“which over hand-him/its the-crimson”)
# ‹וַיִּקְרָא שְׁמוֹ זָרַח› (“and-call name-him/its Zarah”)
# "[EN-AID] And afterward his brother came out, on whose hand was the
# scarlet; and he called his name Zerach."
m.step("Gen.38.30")
# ‹וְאַחַר יָצָא אָחִיו› (“and-after bring-forth brother-him/its”)
# — the world gains: Zarah
m.install("zarach")
# ‹וַיִּקְרָא שְׁמוֹ זָרַח› (“and-call name-him/its Zarah”)
# — named: Zarah := Zarah
m.name("zarach", "zarach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'er', 'onan', 'paretz', 'shela', 'zarach'}
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
    assert sorted(m.WORLD["witnessed"]) == ['eravon']
    assert m.WORLD["witnessed"]['eravon']["cites"] == ['Bereshit Rabbah 85:9']
    assert all('three_crowns' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('yibum', 'first_performance'), ('ve_shichet_artzah', 'er_onan_acts'), ('gedi_izzim', 'repayment_pair'), ('gedi_ha_izim', 'kid_definition'), ('ke_mishlosh_chodashim', 'pregnancy_file'), ('hi_mutzet', 'shaming_furnace'), ('tzadka_mimeni', 'voice_testimony'), ('yad_count', 'four_forward')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 85:5']
    assert all('first_performance' not in f for f in m.WORLD["facts"])
    assert 'yibum' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Yevamot 34b:2', 'Yevamot 34b:3', 'Yevamot 34b:4', 'Yevamot 34b:5']
    assert all('er_onan_acts' not in f for f in m.WORLD["facts"])
    assert 've_shichet_artzah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 85:9']
    assert all('repayment_pair' not in f for f in m.WORLD["facts"])
    assert 'gedi_izzim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Chullin 113a:19', 'Chullin 113a:20', 'Chullin 113b:1', 'Chullin 113b:2', 'Chullin 113b:3']
    assert all('kid_definition' not in f for f in m.WORLD["facts"])
    assert 'gedi_ha_izim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Niddah 8b:16', 'Niddah 8b:17', 'Niddah 8b:18', 'Niddah 28a:8', 'Niddah 28a:9', 'Niddah 28a:10']
    assert all('pregnancy_file' not in f for f in m.WORLD["facts"])
    assert 'ke_mishlosh_chodashim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sotah 10b:5', 'Sotah 10b:6', 'Sotah 10b:7']
    assert all('shaming_furnace' not in f for f in m.WORLD["facts"])
    assert 'hi_mutzet' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 85:12', 'Onkelos Genesis 38:26']
    assert all('voice_testimony' not in f for f in m.WORLD["facts"])
    assert 'tzadka_mimeni' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 85:14']
    assert all('four_forward' not in f for f in m.WORLD["facts"])
    assert 'yad_count' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
