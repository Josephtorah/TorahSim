#!/usr/bin/env python3
# =============================================================================
# gen_59_esau_edom_kings_ledger — 36:1-43
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_59_esau_edom_kings_ledger.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Esau is Edom: the ledger of chiefs and kings (36:1-43)"""
from machine import Machine

m = Machine("gen_59_esau_edom_kings_ledger")

# -------------------------- Gen.36.1 · THE_FIRST_HEADER --------------------
# ‹וְאֵלֶּה תֹּלְדוֹת עֵשָׂו› (“and-these generations Esau”)
# ‹הוּא אֱדוֹם› (“he/it Edom”)
# "[EN-AID] And these are the generations of Esau — he is Edom."
m.step("Gen.36.1")
# ‹וְאֵלֶּה תֹּלְדוֹת עֵשָׂו› (“and-these generations Esau”)
# — fact holds: generations-Esau-he/it-Edom(kotev-rishon)
m.fact("toldot_esav_hu_edom(kotev_rishon)")

# -------------------------- Gen.36.2 · THE_WIVES_OF_CANAAN -----------------
# ‹עֵשָׂו לָקַח אֶת־נָשָׁיו› (“Esau take obj-marker woman-him/its”)
# ‹מִבְּנוֹת כְּנָעַן אֶת־עָדָה› (“from-daughter Canaan obj-marker Adah”)
# ‹בַּת־אֵילוֹן הַחִתִּי וְאֶת־אָהֳלִיבָמָה› (“daughter Elon the-Chittite
# and-obj-marker Aholibamah”)
# ‹בַּת־עֲנָה בַּת־צִבְעוֹן הַחִוִּי› (“daughter Anah daughter Zibeon the-
# Chivvite”)
# "[EN-AID] Esau took his wives from the daughters of Canaan: Ada, daughter
# of Elon the Hittite; and Aholivamah, daughter of Ana, daughter of Tzivon
# the Hivite;"
m.step("Gen.36.2")
# ‹עֵשָׂו לָקַח אֶת־נָשָׁיו› (“Esau take obj-marker woman-him/its”)
# — fact holds: take-nashav-from-daughter-Canaan(Esau, Adah-and-Aholibamah)
m.fact("laqach_nashav_mi_benot_kenaan(esav, ada_ve_aholivama)")

# -------------------------- Gen.36.3 · THE_ISHMAEL_WIFE --------------------
# ‹וְאֶת־בָּשְׂמַת בַּת־יִשְׁמָעֵאל אֲחוֹת› (“and-obj-marker Bashemath
# daughter Ishmael sister”)
# ‹נְבָיוֹת› (“Nebaioth”)
# "[EN-AID] and Basmat, daughter of Ishmael, sister of Nevayot."
m.step("Gen.36.3")
# ‹וְאֶת־בָּשְׂמַת בַּת› (“and-obj-marker Bashemath daughter”)
# — fact holds: Bashemath-daughter-Ishmael(sister-Nebaioth)
m.fact("basmat_bat_yishmael(achot_nevayot)")
# witness-tier presupposed read:
# a_forgiveness_claim_left_standing_against_the_ledger on the_brides_name —
# read, not installed
m.witness_read("the_brides_name", "a_forgiveness_claim_left_standing_against_the_ledger",
                cites=["Bereshit Rabbah 67:13"])

# -------------------------- Gen.36.4 · THE_FIRSTBORN_SONS ------------------
# ‹וַתֵּלֶד עָדָה לְעֵשָׂו› (“and-bear-young Adah to-Esau”)
# ‹אֶת־אֱלִיפָז וּבָשְׂמַת יָלְדָה› (“obj-marker Eliphaz and-Bashemath bear-
# young”)
# ‹אֶת־רְעוּאֵל› (“obj-marker Raguel”)
# "[EN-AID] And Ada bore to Esau Elifaz; and Basmat bore Reuel;"
m.step("Gen.36.4")
# ‹וַתֵּלֶד עָדָה לְעֵשָׂו› (“and-bear-young Adah to-Esau”)
# ‹אֶת› (“obj-marker”)
# — fact holds: and-bear-young-Adah-and-Bashemath(Eliphaz-and-Raguel)
m.fact("va_teled_ada_u_vasmat(elifaz_u_reuel)")

# -------------------------- Gen.36.5 · THE_CANAAN_BORN_CLOSE ---------------
# ‹וְאָהֳלִיבָמָה יָלְדָה אֶת־יעיש› (“and-Aholibamah bear-young obj-marker
# Jeush”)
# ‹יְעוּשׁ וְאֶת־יַעְלָם וְאֶת־קֹרַח› (“Jehush and-obj-marker Jalam and-obj-
# marker Korah”)
# ‹אֵלֶּה בְּנֵי עֵשָׂו› (“these son Esau”)
# ‹אֲשֶׁר יֻלְּדוּ־לוֹ בְּאֶרֶץ› (“which bear-young to-him/its in-earth”)
# ‹כְּנָעַן› (“Canaan”)
# "[EN-AID] and Aholivamah bore Yeush and Yalam and Korach. These are the
# sons of Esau who were born to him in the land of Canaan."
m.step("Gen.36.5")
# ‹וְאָהֳלִיבָמָה יָלְדָה› (“and-Aholibamah bear-young”)
# — fact holds: these-son-Esau(bear-young-not-in-earth-Canaan)
m.fact("ele_bene_esav(yuldu_lo_be_eretz_kenaan)")

# -------------------------- Gen.36.6 · THE_WITHDRAWAL ----------------------
# ‹וַיִּקַּח עֵשָׂו אֶת־נָשָׁיו› (“and-take Esau obj-marker woman-him/its”)
# ‹וְאֶת־בָּנָיו וְאֶת־בְּנֹתָיו וְאֶת־כָּל־נַפְשׁוֹת› (“and-obj-marker son-
# him/its and-obj-marker daughter-him/its and-obj-marker all living-being”)
# ‹בֵּיתוֹ וְאֶת־מִקְנֵהוּ וְאֶת־כָּל־בְּהֶמְתּוֹ› (“house-him/its and-obj-
# marker something-bought-him/its and-obj-marker all livestock-him/its”)
# ‹וְאֵת כָּל־קִנְיָנוֹ אֲשֶׁר› (“and-obj-marker all creation-him/its
# which”)
# ‹רָכַשׁ בְּאֶרֶץ כְּנָעַן› (“lay-up in-earth Canaan”)
# ‹וַיֵּלֶךְ אֶל־אֶרֶץ מִפְּנֵי› (“and-go to earth from-face”)
# ‹יַעֲקֹב אָחִיו› (“Jacob brother-him/its”)
# "[EN-AID] And Esau took his wives and his sons and his daughters and all
# the souls of his house, and his livestock and all his beasts and all his
# property that he had acquired in the land of Canaan; and he went to a
# land, away from before Jacob his brother."
m.step("Gen.36.6")
# ‹וַיֵּלֶךְ אֶל־אֶרֶץ מִפְּנֵי› (“and-go to earth from-face”)
# ‹יַעֲקֹב› (“Jacob”)
# — fact holds: and-go-to-earth(Esau, from-face-Jacob-his-brother)
m.fact("va_yelekh_el_eretz(esav, mi_pene_yaaqov_achiv)")
# witness-tier presupposed read: read_as_escaping_the_covenant_debt on
# went_to_another_land — read, not installed
m.witness_read("went_to_another_land", "read_as_escaping_the_covenant_debt",
                cites=["Bereshit Rabbah 82:13", "Onkelos Genesis 36:6"])

# -------------------------- Gen.36.7 · THE_LAND_THAT_COULD_NOT_BEAR --------
# ‹כִּי־הָיָה רְכוּשָׁם רָב› (“that be property-them/their many/great”)
# ‹מִשֶּׁבֶת יַחְדָּו וְלֹא› (“from-dwell/sit unit and-not”)
# ‹יָכְלָה אֶרֶץ מְגוּרֵיהֶם› (“be-able earth sojourning-them/their”)
# ‹לָשֵׂאת אֹתָם מִפְּנֵי› (“to-lift/carry obj-marker-them/their from-face”)
# ‹מִקְנֵיהֶם› (“something-bought-them/their”)
# "[EN-AID] For their property was too great for dwelling together; and the
# land of their sojournings could not bear them, because of their
# livestock."
m.step("Gen.36.7")
# ‹כִּי־הָיָה רְכוּשָׁם רָב› (“that be property-them/their many/great”)
# — fact holds: not-be-able-earth-megurehem-to-lift/carry-otam(rekhusham-
# many/great)
m.fact("lo_yakhla_eretz_megurehem_la_set_otam(rekhusham_rav)")

# -------------------------- Gen.36.8 · SEIR_SETTLED ------------------------
# ‹וַיֵּשֶׁב עֵשָׂו בְּהַר› (“and-dwell/sit Esau in-mountain”)
# ‹שֵׂעִיר עֵשָׂו הוּא› (“Seir Esau he/it”)
# ‹אֱדוֹם› (“Edom”)
# "[EN-AID] And Esau dwelt in the hill-country of Seir — Esau, he is Edom."
m.step("Gen.36.8")
# ‹וַיֵּשֶׁב עֵשָׂו בְּהַר› (“and-dwell/sit Esau in-mountain”)
# ‹שֵׂעִיר› (“Seir”)
# — fact holds: and-dwell/sit-Esau-in-mountain-Seir(he/it-Edom)
m.fact("va_yeshev_esav_be_har_seir(hu_edom)")

# -------------------------- Gen.36.9 · THE_SECOND_HEADER -------------------
# ‹וְאֵלֶּה תֹּלְדוֹת עֵשָׂו› (“and-these generations Esau”)
# ‹אֲבִי אֱדוֹם בְּהַר› (“father Edom in-mountain”)
# ‹שֵׂעִיר› (“Seir”)
# "[EN-AID] And these are the generations of Esau, father of Edom, in the
# hill-country of Seir."
m.step("Gen.36.9")
# ‹וְאֵלֶּה תֹּלְדוֹת עֵשָׂו› (“and-these generations Esau”)
# ‹אֲבִי› (“father”)
# — fact holds: generations-Esau-father-Edom(kotev-sheni, in-mountain-Seir)
m.fact("toldot_esav_avi_edom(kotev_sheni, be_har_seir)")

# -------------------------- Gen.36.10 · THE_SONS_NAMED ---------------------
# ‹אֵלֶּה שְׁמוֹת בְּנֵי־עֵשָׂו› (“these name son Esau”)
# ‹אֱלִיפַז בֶּן־עָדָה אֵשֶׁת› (“Eliphaz son Adah woman”)
# ‹עֵשָׂו רְעוּאֵל בֶּן־בָּשְׂמַת› (“Esau Raguel son Bashemath”)
# ‹אֵשֶׁת עֵשָׂו› (“woman Esau”)
# "[EN-AID] These are the names of the sons of Esau: Elifaz son of Ada,
# Esau's wife; Reuel son of Basmat, Esau's wife."
m.step("Gen.36.10")
# ‹אֵלֶּה שְׁמוֹת בְּנֵי־עֵשָׂו› (“these name son Esau”)
# — fact holds: these-name-son-Esau(Eliphaz-and-Raguel)
m.fact("ele_shemot_bene_esav(elifaz_u_reuel)")

# -------------------------- Gen.36.11 · ELIFAZ_S_FIVE ----------------------
# ‹וַיִּהְיוּ בְּנֵי אֱלִיפָז› (“and-be son Eliphaz”)
# ‹תֵּימָן אוֹמָר צְפוֹ› (“Teyman Omar Zephi”)
# ‹וְגַעְתָּם וּקְנַז› (“and-Gatam and-Kenaz”)
# "[EN-AID] And the sons of Elifaz were: Teman, Omar, Tzefo, and Gatam, and
# Kenaz."
m.step("Gen.36.11")
# ‹וַיִּהְיוּ בְּנֵי אֱלִיפָז› (“and-be son Eliphaz”)
# — fact holds: son-Eliphaz(Teyman-until-Kenaz)
m.fact("bene_elifaz(teman_ad_qenaz)")

# -------------------------- Gen.36.12 · AMALEK_BORN ------------------------
# ‹וְתִמְנַע הָיְתָה פִילֶגֶשׁ› (“and-Timna be concubine”)
# ‹לֶאֱלִיפַז בֶּן־עֵשָׂו וַתֵּלֶד› (“to-Eliphaz son Esau and-bear-young”)
# ‹לֶאֱלִיפַז אֶת־עֲמָלֵק אֵלֶּה› (“to-Eliphaz obj-marker Amalek these”)
# ‹בְּנֵי עָדָה אֵשֶׁת› (“son Adah woman”)
# ‹עֵשָׂו› (“Esau”)
# "[EN-AID] And Timna was concubine to Elifaz, son of Esau, and she bore to
# Elifaz Amalek. These are the sons of Ada, Esau's wife."
m.step("Gen.36.12")
# ‹וְתִמְנַע הָיְתָה פִילֶגֶשׁ› (“and-Timna be concubine”)
# ‹לֶאֱלִיפַז› (“to-Eliphaz”)
# — fact holds: and-bear-young-Timna-to-Eliphaz(obj-marker-Amalek)
m.fact("va_teled_timna_le_elifaz(et_amaleq)")
# witness-tier presupposed read: audited_as_evidence_of_illegitimate_lines
# on the_roster — read, not installed
m.witness_read("the_roster", "audited_as_evidence_of_illegitimate_lines",
                cites=["Bereshit Rabbah 82:12", "Bereshit Rabbah 82:15"])

# -------------------------- Gen.36.13 · REUEL_S_FOUR -----------------------
# ‹וְאֵלֶּה בְּנֵי רְעוּאֵל› (“and-these son Raguel”)
# ‹נַחַת וָזֶרַח שַׁמָּה› (“Nahath and-Zarah Shammah”)
# ‹וּמִזָּה אֵלֶּה הָיוּ› (“and-Mizzah these be”)
# ‹בְּנֵי בָשְׂמַת אֵשֶׁת› (“son Bashemath woman”)
# ‹עֵשָׂו› (“Esau”)
# "[EN-AID] And these are the sons of Reuel: Nachat and Zerach, Shama and
# Miza. These were the sons of Basmat, Esau's wife."
m.step("Gen.36.13")
# ‹וְאֵלֶּה בְּנֵי רְעוּאֵל› (“and-these son Raguel”)
# — fact holds: son-Raguel(Nahath-until-Mizzah)
m.fact("bene_reuel(nachat_ad_miza)")

# -------------------------- Gen.36.14 · AHOLIVAMAH_S_THREE -----------------
# ‹וְאֵלֶּה הָיוּ בְּנֵי› (“and-these be son”)
# ‹אָהֳלִיבָמָה בַת־עֲנָה בַּת־צִבְעוֹן› (“Aholibamah daughter Anah daughter
# Zibeon”)
# ‹אֵשֶׁת עֵשָׂו וַתֵּלֶד› (“woman Esau and-bear-young”)
# ‹לְעֵשָׂו אֶת־יעיש יְעוּשׁ› (“to-Esau obj-marker Jeush Jehush”)
# ‹וְאֶת־יַעְלָם וְאֶת־קֹרַח› (“and-obj-marker Jalam and-obj-marker Korah”)
# "[EN-AID] And these were the sons of Aholivamah, daughter of Ana, daughter
# of Tzivon, Esau's wife: she bore to Esau Yeush and Yalam and Korach."
m.step("Gen.36.14")
# ‹וְאֵלֶּה הָיוּ בְּנֵי› (“and-these be son”)
# ‹אָהֳלִיבָמָה› (“Aholibamah”)
# — fact holds: son-Aholibamah(Jehush-Jalam-Korah)
m.fact("bene_aholivama(yeush_yalam_qorach)")

# -------------------------- Gen.36.15 · THE_CHIEF_TITLE_MINTED -------------
# ‹אֵלֶּה אַלּוּפֵי בְנֵי־עֵשָׂו› (“these familiar son Esau”)
# ‹בְּנֵי אֱלִיפַז בְּכוֹר› (“son Eliphaz firstborn”)
# ‹עֵשָׂו אַלּוּף תֵּימָן› (“Esau familiar Teyman”)
# ‹אַלּוּף אוֹמָר אַלּוּף› (“familiar Omar familiar”)
# ‹צְפוֹ אַלּוּף קְנַז› (“Zephi familiar Kenaz”)
# "[EN-AID] These are the chiefs of the sons of Esau. The sons of Elifaz,
# Esau's firstborn: chief Teman, chief Omar, chief Tzefo, chief Kenaz,"
m.step("Gen.36.15")
# ‹אֵלֶּה אַלּוּפֵי בְנֵי› (“these familiar son”)
# — fact holds: these-familiar-son-Esau(familiar-Eliphaz)
m.fact("ele_alufe_vene_esav(alufe_elifaz)")

# -------------------------- Gen.36.16 · ELIFAZ_S_CHIEFS_CLOSE --------------
# ‹אַלּוּף־קֹרַח אַלּוּף גַּעְתָּם› (“familiar Korah familiar Gatam”)
# ‹אַלּוּף עֲמָלֵק אֵלֶּה› (“familiar Amalek these”)
# ‹אַלּוּפֵי אֱלִיפַז בְּאֶרֶץ› (“familiar Eliphaz in-earth”)
# ‹אֱדוֹם אֵלֶּה בְּנֵי› (“Edom these son”)
# ‹עָדָה› (“Adah”)
# "[EN-AID] chief Korach, chief Gatam, chief Amalek. These are the chiefs of
# Elifaz in the land of Edom; these are the sons of Ada."
m.step("Gen.36.16")
# ‹אַלּוּף־קֹרַח אַלּוּף› (“familiar Korah familiar”)
# — fact holds: familiar-Eliphaz-in-earth-Edom(son-Adah)
m.fact("alufe_elifaz_be_eretz_edom(bene_ada)")

# -------------------------- Gen.36.17 · REUEL_S_CHIEFS ---------------------
# ‹וְאֵלֶּה בְּנֵי רְעוּאֵל› (“and-these son Raguel”)
# ‹בֶּן־עֵשָׂו אַלּוּף נַחַת› (“son Esau familiar Nahath”)
# ‹אַלּוּף זֶרַח אַלּוּף› (“familiar Zarah familiar”)
# ‹שַׁמָּה אַלּוּף מִזָּה› (“Shammah familiar Mizzah”)
# ‹אֵלֶּה אַלּוּפֵי רְעוּאֵל› (“these familiar Raguel”)
# ‹בְּאֶרֶץ אֱדוֹם אֵלֶּה› (“in-earth Edom these”)
# ‹בְּנֵי בָשְׂמַת אֵשֶׁת› (“son Bashemath woman”)
# ‹עֵשָׂו› (“Esau”)
# "[EN-AID] And these are the sons of Reuel, Esau's son: chief Nachat, chief
# Zerach, chief Shama, chief Miza. These are the chiefs of Reuel in the land
# of Edom; these are the sons of Basmat, Esau's wife."
m.step("Gen.36.17")
# ‹וְאֵלֶּה בְּנֵי רְעוּאֵל› (“and-these son Raguel”)
# ‹בֶּן־עֵשָׂו אַלּוּף› (“son Esau familiar”)
# — fact holds: familiar-Raguel-in-earth-Edom(son-Bashemath)
m.fact("alufe_reuel_be_eretz_edom(bene_vasmat)")

# -------------------------- Gen.36.18 · AHOLIVAMAH_S_CHIEFS ----------------
# ‹וְאֵלֶּה בְּנֵי אָהֳלִיבָמָה› (“and-these son Aholibamah”)
# ‹אֵשֶׁת עֵשָׂו אַלּוּף› (“woman Esau familiar”)
# ‹יְעוּשׁ אַלּוּף יַעְלָם› (“Jehush familiar Jalam”)
# ‹אַלּוּף קֹרַח אֵלֶּה› (“familiar Korah these”)
# ‹אַלּוּפֵי אָהֳלִיבָמָה בַּת־עֲנָה› (“familiar Aholibamah daughter Anah”)
# ‹אֵשֶׁת עֵשָׂו› (“woman Esau”)
# "[EN-AID] And these are the sons of Aholivamah, Esau's wife: chief Yeush,
# chief Yalam, chief Korach. These are the chiefs of Aholivamah, daughter of
# Ana, Esau's wife."
m.step("Gen.36.18")
# ‹וְאֵלֶּה בְּנֵי אָהֳלִיבָמָה› (“and-these son Aholibamah”)
# ‹אֵשֶׁת עֵשָׂו› (“woman Esau”)
# — fact holds: familiar-Aholibamah(Jehush-Jalam-Korah)
m.fact("alufe_aholivama(yeush_yalam_qorach)")

# -------------------------- Gen.36.19 · THE_FIRST_LEDGER_SEALS -------------
# ‹אֵלֶּה בְנֵי־עֵשָׂו וְאֵלֶּה› (“these son Esau and-these”)
# ‹אַלּוּפֵיהֶם הוּא אֱדוֹם› (“familiar-them/their he/it Edom”)
# "[EN-AID] These are the sons of Esau, and these their chiefs — he is
# Edom."
m.step("Gen.36.19")
# ‹אֵלֶּה בְנֵי› (“these son”)
# — fact holds: these-son-Esau-and-alufehem(he/it-Edom)
m.fact("ele_vene_esav_ve_alufehem(hu_edom)")

# -------------------------- Gen.36.20 · THE_HORITES_ENTER ------------------
# ‹אֵלֶּה בְנֵי־שֵׂעִיר הַחֹרִי› (“these son Seir the-Chorite”)
# ‹יֹשְׁבֵי הָאָרֶץ לוֹטָן› (“dwell/sit the-earth Lotan”)
# ‹וְשׁוֹבָל וְצִבְעוֹן וַעֲנָה› (“and-Shobal and-Zibeon and-Anah”)
# "[EN-AID] These are the sons of Seir the Horite, the dwellers of the land:
# Lotan and Shoval and Tzivon and Ana,"
m.step("Gen.36.20")
# ‹אֵלֶּה בְנֵי־שֵׂעִיר הַחֹרִי› (“these son Seir the-Chorite”)
# — fact holds: son-Seir-the-Chorite(dwell/sit-the-earth)
m.fact("bene_seir_ha_chori(yoshve_ha_aretz)")

# -------------------------- Gen.36.21 · THE_HORITE_SEVEN -------------------
# ‹וְדִשׁוֹן וְאֵצֶר וְדִישָׁן› (“and-Dishon and-Ezer and-Dishan”)
# ‹אֵלֶּה אַלּוּפֵי הַחֹרִי› (“these familiar the-Chorite”)
# ‹בְּנֵי שֵׂעִיר בְּאֶרֶץ› (“son Seir in-earth”)
# ‹אֱדוֹם› (“Edom”)
# "[EN-AID] and Dishon and Etzer and Dishan. These are the chiefs of the
# Horites, the sons of Seir, in the land of Edom."
m.step("Gen.36.21")
# ‹וְדִשׁוֹן וְאֵצֶר וְדִישָׁן› (“and-Dishon and-Ezer and-Dishan”)
# — fact holds: familiar-the-Chorite(son-Seir)
m.fact("alufe_ha_chori(bene_seir)")

# -------------------------- Gen.36.22 · TIMNA_THE_SISTER -------------------
# ‹וַיִּהְיוּ בְנֵי־לוֹטָן חֹרִי› (“and-be son Lotan Hori”)
# ‹וְהֵימָם וַאֲחוֹת לוֹטָן› (“and-Hemam and-sister Lotan”)
# ‹תִּמְנָע› (“Timna”)
# "[EN-AID] And the sons of Lotan were Chori and Hemam; and Lotan's sister
# was Timna."
m.step("Gen.36.22")
# ‹וַאֲחוֹת לוֹטָן תִּמְנָע› (“and-sister Lotan Timna”)
# — fact holds: and-sister-Lotan(Timna)
m.fact("va_achot_lotan(timna)")

# -------------------------- Gen.36.23 · SHOVAL_S_FIVE ----------------------
# ‹וְאֵלֶּה בְּנֵי שׁוֹבָל› (“and-these son Shobal”)
# ‹עַלְוָן וּמָנַחַת וְעֵיבָל› (“Alian and-Manahath and-Ebal”)
# ‹שְׁפוֹ וְאוֹנָם› (“Shephi and-Onam”)
# "[EN-AID] And these are the sons of Shoval: Alvan and Manachat and Eval,
# Shefo and Onam."
m.step("Gen.36.23")
# ‹וְאֵלֶּה בְּנֵי שׁוֹבָל› (“and-these son Shobal”)
# — fact holds: son-Shobal(Alian-until-Onam)
m.fact("bene_shoval(alvan_ad_onam)")

# -------------------------- Gen.36.24 · THE_YEMIM_FINDER -------------------
# ‹וְאֵלֶּה בְנֵי־צִבְעוֹן וְאַיָּה› (“and-these son Zibeon and-Aiah”)
# ‹וַעֲנָה הוּא עֲנָה› (“and-Anah he/it Anah”)
# ‹אֲשֶׁר מָצָא אֶת־הַיֵּמִם› (“which find obj-marker the-warm-spring”)
# ‹בַּמִּדְבָּר בִּרְעֹתוֹ אֶת־הַחֲמֹרִים› (“in-pasture in-graze-him/its
# obj-marker the-male-ass”)
# ‹לְצִבְעוֹן אָבִיו› (“to-Zibeon father-him/its”)
# "[EN-AID] And these are the sons of Tzivon: Aya and Ana — he is the Ana
# who found the yemim in the wilderness, while pasturing the donkeys for
# Tzivon his father."
m.step("Gen.36.24")
# ‹הוּא עֲנָה אֲשֶׁר› (“he/it Anah which”)
# ‹מָצָא› (“find”)
# — fact holds: he/it-Anah-which-find-obj-marker-the-warm-spring(pasture)
m.fact("hu_ana_asher_matza_et_ha_yemim(ba_midbar)")
# witness-tier presupposed read: a_third_reading_entered_by_the_translation
# on what_was_found — read, not installed
m.witness_read("what_was_found", "a_third_reading_entered_by_the_translation",
                cites=["Onkelos Genesis 36:24"])

# -------------------------- Gen.36.25 · ANA_S_TWO --------------------------
# ‹וְאֵלֶּה בְנֵי־עֲנָה דִּשֹׁן› (“and-these son Anah Dishon”)
# ‹וְאָהֳלִיבָמָה בַּת־עֲנָה› (“and-Aholibamah daughter Anah”)
# "[EN-AID] And these are the sons of Ana: Dishon; and Aholivamah, daughter
# of Ana."
m.step("Gen.36.25")
# ‹וְאֵלֶּה בְנֵי־עֲנָה› (“and-these son Anah”)
# — fact holds: son-Anah(Dishon-and-Aholibamah)
m.fact("bene_ana(dishon_ve_aholivama)")

# -------------------------- Gen.36.26 · DISHAN_S_FOUR ----------------------
# ‹וְאֵלֶּה בְּנֵי דִישָׁן› (“and-these son Dishan”)
# ‹חֶמְדָּן וְאֶשְׁבָּן וְיִתְרָן› (“Hemdan and-Eshban and-Ithran”)
# ‹וּכְרָן› (“and-Cheran”)
# "[EN-AID] And these are the sons of Dishan: Chemdan and Eshban and Yitran
# and Cheran."
m.step("Gen.36.26")
# ‹וְאֵלֶּה בְּנֵי דִישָׁן› (“and-these son Dishan”)
# — fact holds: son-Dishan-rishon(Hemdan-until-Cheran)
m.fact("bene_dishan_rishon(chemdan_ad_kheran)")

# -------------------------- Gen.36.27 · ETZER_S_THREE ----------------------
# ‹אֵלֶּה בְּנֵי־אֵצֶר בִּלְהָן› (“these son Ezer Bilhan”)
# ‹וְזַעֲוָן וַעֲקָן› (“and-Zaavan and-Akan”)
# "[EN-AID] These are the sons of Etzer: Bilhan and Zaavan and Akan."
m.step("Gen.36.27")
# ‹אֵלֶּה בְּנֵי־אֵצֶר› (“these son Ezer”)
# — fact holds: son-Ezer(Bilhan-Zaavan-Akan)
m.fact("bene_etzer(bilhan_zaavan_aqan)")

# -------------------------- Gen.36.28 · DISHAN_S_TWO -----------------------
# ‹אֵלֶּה בְנֵי־דִישָׁן עוּץ› (“these son Dishan Uz”)
# ‹וַאֲרָן› (“and-Aran”)
# "[EN-AID] These are the sons of Dishan: Utz and Aran."
m.step("Gen.36.28")
# ‹אֵלֶּה בְנֵי־דִישָׁן› (“these son Dishan”)
# — fact holds: son-Dishan(Uz-and-Aran)
m.fact("bene_dishan(utz_va_aran)")

# -------------------------- Gen.36.29 · THE_HORITE_CHIEFS ------------------
# ‹אֵלֶּה אַלּוּפֵי הַחֹרִי› (“these familiar the-Chorite”)
# ‹אַלּוּף לוֹטָן אַלּוּף› (“familiar Lotan familiar”)
# ‹שׁוֹבָל אַלּוּף צִבְעוֹן› (“Shobal familiar Zibeon”)
# ‹אַלּוּף עֲנָה› (“familiar Anah”)
# "[EN-AID] These are the chiefs of the Horites: chief Lotan, chief Shoval,
# chief Tzivon, chief Ana,"
m.step("Gen.36.29")
# ‹אֵלֶּה אַלּוּפֵי הַחֹרִי› (“these familiar the-Chorite”)
# — fact holds: familiar-the-Chorite-rishon(Lotan-until-Anah)
m.fact("alufe_ha_chori_rishon(lotan_ad_ana)")

# -------------------------- Gen.36.30 · THE_HORITE_LEDGER_SEALS ------------
# ‹אַלּוּף דִּשֹׁן אַלּוּף› (“familiar Dishon familiar”)
# ‹אֵצֶר אַלּוּף דִּישָׁן› (“Ezer familiar Dishan”)
# ‹אֵלֶּה אַלּוּפֵי הַחֹרִי› (“these familiar the-Hori”)
# ‹לְאַלֻּפֵיהֶם בְּאֶרֶץ שֵׂעִיר› (“to-familiar-them/their in-earth Seir”)
# "[EN-AID] chief Dishon, chief Etzer, chief Dishan. These are the chiefs of
# the Horites, by their chiefdoms, in the land of Seir."
m.step("Gen.36.30")
# ‹אַלּוּף דִּשֹׁן› (“familiar Dishon”)
# — fact holds: familiar-the-Chorite-to-alufehem(in-earth-Seir)
m.fact("alufe_ha_chori_le_alufehem(be_eretz_seir)")

# -------------------------- Gen.36.31 · THE_KINGS_BEFORE_THE_KINGS ---------
# ‹וְאֵלֶּה הַמְּלָכִים אֲשֶׁר› (“and-these the-king which”)
# ‹מָלְכוּ בְּאֶרֶץ אֱדוֹם› (“reign in-earth Edom”)
# ‹לִפְנֵי מְלָךְ־מֶלֶךְ לִבְנֵי› (“to-face reign king to-son”)
# ‹יִשְׂרָאֵל› (“Israel”)
# "[EN-AID] And these are the kings who reigned in the land of Edom, before
# a king reigned for the sons of Israel."
m.step("Gen.36.31")
# ‹וְאֵלֶּה הַמְּלָכִים אֲשֶׁר› (“and-these the-king which”)
# ‹מָלְכוּ בְּאֶרֶץ אֱדוֹם› (“reign in-earth Edom”)
# — fact holds: the-king-which-reign-in-Edom(to-me-fene-reign-king-to-me-
# son-Israel)
m.fact("ha_melakhim_asher_malkhu_be_edom(li_fene_melakh_melekh_li_vene_yisrael)")
# witness-grounded state (its own tier):
# the_penalty_minted_at_gen_55_counted_here on eight_kings
m.witness_state("eight_kings", "the_penalty_minted_at_gen_55_counted_here",
                cites=["Bereshit Rabbah 83:2"])
# witness-tier presupposed read: read_as_a_state_of_imported_parts on
# the_king_list — read, not installed
m.witness_read("the_king_list", "read_as_a_state_of_imported_parts",
                cites=["Bereshit Rabbah 83:1"])

# -------------------------- Gen.36.32 · THE_FIRST_KING ---------------------
# ‹וַיִּמְלֹךְ בֶּאֱדוֹם בֶּלַע› (“and-reign in-Edom Bela”)
# ‹בֶּן־בְּעוֹר וְשֵׁם עִירוֹ› (“son Beor and-name city-him/its”)
# ‹דִּנְהָבָה› (“Dinhaban”)
# "[EN-AID] And Bela son of Beor reigned in Edom; and the name of his city
# was Dinhava."
m.step("Gen.36.32")
# ‹וַיִּמְלֹךְ בֶּאֱדוֹם בֶּלַע› (“and-reign in-Edom Bela”)
# ‹בֶּן› (“son”)
# — fact holds: and-reign-Bela-son-Beor(ir-Dinhaban)
m.fact("va_yimlokh_bela_ben_beor(ir_dinhava)")

# -------------------------- Gen.36.33 · THE_CHAIN_BEGINS -------------------
# ‹וַיָּמָת בָּלַע וַיִּמְלֹךְ› (“and-die Bela and-reign”)
# ‹תַּחְתָּיו יוֹבָב בֶּן־זֶרַח› (“under-him/its Jobab son Zarah”)
# ‹מִבָּצְרָה› (“from-Bozrah”)
# "[EN-AID] And Bela died; and Yovav son of Zerach, from Botzra, reigned in
# his place."
m.step("Gen.36.33")
# ‹וַיָּמָת בָּלַע› (“and-die Bela”)
# — fact holds: and-die-Bela-and-reign(Jobab-from-Bozrah)
m.fact("va_yamat_bela_va_yimlokh(yovav_mi_batzra)")
# witness-tier presupposed read: supplier_liability_applied_to_a_state on
# the_king_from_botzra — read, not installed
m.witness_read("the_king_from_botzra", "supplier_liability_applied_to_a_state",
                cites=["Bereshit Rabbah 83:3"])

# -------------------------- Gen.36.34 · THE_THIRD_KING ---------------------
# ‹וַיָּמָת יוֹבָב וַיִּמְלֹךְ› (“and-die Jobab and-reign”)
# ‹תַּחְתָּיו חֻשָׁם מֵאֶרֶץ› (“under-him/its Husham from-earth”)
# ‹הַתֵּימָנִי› (“the-Temanite”)
# "[EN-AID] And Yovav died; and Chusham, from the land of the Temanite,
# reigned in his place."
m.step("Gen.36.34")
# ‹וַיָּמָת יוֹבָב› (“and-die Jobab”)
# — fact holds: and-die-Jobab-and-reign(Husham-the-Temanite)
m.fact("va_yamat_yovav_va_yimlokh(chusham_ha_temani)")

# -------------------------- Gen.36.35 · THE_KING_WHO_STRUCK_MIDIAN ---------
# ‹וַיָּמָת חֻשָׁם וַיִּמְלֹךְ› (“and-die Husham and-reign”)
# ‹תַּחְתָּיו הֲדַד בֶּן־בְּדַד› (“under-him/its Hadad son Bedad”)
# ‹הַמַּכֶּה אֶת־מִדְיָן בִּשְׂדֵה› (“the-strike obj-marker Midian in-
# field”)
# ‹מוֹאָב וְשֵׁם עִירוֹ› (“Moab and-name city-him/its”)
# ‹עֲוִית› (“Avith”)
# "[EN-AID] And Chusham died; and Hadad son of Bedad — who struck Midian in
# the field of Moab — reigned in his place; and the name of his city was
# Avit."
m.step("Gen.36.35")
# ‹הַמַּכֶּה אֶת־מִדְיָן בִּשְׂדֵה› (“the-strike obj-marker Midian in-
# field”)
# — fact holds: and-reign-Hadad(the-strike-obj-marker-Midian-bi-sede-Moab)
m.fact("va_yimlokh_hadad(ha_make_et_midyan_bi_sede_moav)")

# -------------------------- Gen.36.36 · THE_FIFTH_KING ---------------------
# ‹וַיָּמָת הֲדָד וַיִּמְלֹךְ› (“and-die Hadad and-reign”)
# ‹תַּחְתָּיו שַׂמְלָה מִמַּשְׂרֵקָה› (“under-him/its Samlah from-Masrekah”)
# "[EN-AID] And Hadad died; and Samla, from Masreka, reigned in his place."
m.step("Gen.36.36")
# ‹וַיָּמָת הֲדָד› (“and-die Hadad”)
# — fact holds: and-die-Hadad-and-reign(Samlah-from-Masrekah)
m.fact("va_yamat_hadad_va_yimlokh(samla_mi_masreqa)")

# -------------------------- Gen.36.37 · THE_KING_FROM_THE_WIDE_PLACES ------
# ‹וַיָּמָת שַׂמְלָה וַיִּמְלֹךְ› (“and-die Samlah and-reign”)
# ‹תַּחְתָּיו שָׁאוּל מֵרְחֹבוֹת› (“under-him/its Saul from-Rehoboth”)
# ‹הַנָּהָר› (“the-river”)
# "[EN-AID] And Samla died; and Shaul, from Rechovot-of-the-river, reigned
# in his place."
m.step("Gen.36.37")
# ‹וַיִּמְלֹךְ תַּחְתָּיו שָׁאוּל› (“and-reign under-him/its Saul”)
# ‹מֵרְחֹבוֹת› (“from-Rehoboth”)
# — fact holds: and-reign-Saul(from-Rehoboth-the-river)
m.fact("va_yimlokh_shaul(me_rechovot_ha_nahar)")

# -------------------------- Gen.36.38 · THE_SEVENTH_KING -------------------
# ‹וַיָּמָת שָׁאוּל וַיִּמְלֹךְ› (“and-die Saul and-reign”)
# ‹תַּחְתָּיו בַּעַל חָנָן› (“under-him/its Baal-hanan”)
# ‹בֶּן־עַכְבּוֹר› (“son Achbor”)
# "[EN-AID] And Shaul died; and Baal-Chanan son of Akhbor reigned in his
# place."
m.step("Gen.36.38")
# ‹וַיָּמָת שָׁאוּל› (“and-die Saul”)
# — fact holds: and-die-Saul-and-reign(baal-Baal-hanan-son-Achbor)
m.fact("va_yamat_shaul_va_yimlokh(baal_chanan_ben_akhbor)")

# -------------------------- Gen.36.39 · THE_LAST_KING_AND_THE_QUEEN_LINE ---
# ‹וַיָּמָת בַּעַל חָנָן› (“and-die Baal-hanan”)
# ‹בֶּן־עַכְבּוֹר וַיִּמְלֹךְ תַּחְתָּיו› (“son Achbor and-reign under-
# him/its”)
# ‹הֲדַר וְשֵׁם עִירוֹ› (“Hadar and-name city-him/its”)
# ‹פָּעוּ וְשֵׁם אִשְׁתּוֹ› (“Pai and-name woman-him/its”)
# ‹מְהֵיטַבְאֵל בַּת־מַטְרֵד בַּת› (“Mehetabeel daughter Matred daughter”)
# ‹מֵי זָהָב› (“Mezahab”)
# "[EN-AID] And Baal-Chanan son of Akhbor died; and Hadar reigned in his
# place; and the name of his city was Pau; and his wife's name was
# Mehetavel, daughter of Matred, daughter of Me-zahav."
m.step("Gen.36.39")
# ‹וְשֵׁם אִשְׁתּוֹ מְהֵיטַבְאֵל› (“and-name woman-him/its Mehetabeel”)
# ‹בַּת־מַטְרֵד בַּת מֵי› (“daughter Matred daughter”)
# ‹זָהָב› (“Mezahab”)
# — fact holds: and-reign-Hadar(his-wife-Mehetabeel-daughter-from-Mezahab)
m.fact("va_yimlokh_hadar(ishto_mehetavel_bat_me_zahav)")
# witness-tier presupposed read: read_as_a_countdown_and_an_escrow on
# the_last_names — read, not installed
m.witness_read("the_last_names", "read_as_a_countdown_and_an_escrow",
                cites=["Bereshit Rabbah 83:4", "Onkelos Genesis 36:39"])

# -------------------------- Gen.36.40 · THE_CLOSING_LIST_OPENS -------------
# ‹וְאֵלֶּה שְׁמוֹת אַלּוּפֵי› (“and-these name familiar”)
# ‹עֵשָׂו לְמִשְׁפְּחֹתָם לִמְקֹמֹתָם› (“Esau to-family-them/their to-place-
# them/their”)
# ‹בִּשְׁמֹתָם אַלּוּף תִּמְנָע› (“in-name-them/their familiar Timna”)
# ‹אַלּוּף עַלְוָה אַלּוּף› (“familiar Aliah familiar”)
# ‹יְתֵת› (“Jetheth”)
# "[EN-AID] And these are the names of the chiefs of Esau, by their
# families, by their places, by their names: chief Timna, chief Alva, chief
# Yetet,"
m.step("Gen.36.40")
# ‹וְאֵלֶּה שְׁמוֹת אַלּוּפֵי› (“and-these name familiar”)
# ‹עֵשָׂו לְמִשְׁפְּחֹתָם לִמְקֹמֹתָם› (“Esau to-family-them/their to-place-
# them/their”)
# — fact holds: familiar-Esau-to-mishpechotam(to-me-meqomotam-bi-shemotam)
m.fact("alufe_esav_le_mishpechotam(li_meqomotam_bi_shemotam)")

# -------------------------- Gen.36.41 · THE_LIST_RUNS ----------------------
# ‹אַלּוּף אָהֳלִיבָמָה אַלּוּף› (“familiar Aholibamah familiar”)
# ‹אֵלָה אַלּוּף פִּינֹן› (“Elah familiar Pinon”)
# "[EN-AID] chief Aholivamah, chief Ela, chief Pinon,"
m.step("Gen.36.41")
# ‹אַלּוּף אָהֳלִיבָמָה אַלּוּף› (“familiar Aholibamah familiar”)
# ‹אֵלָה› (“Elah”)
# — fact holds: familiar-Aholibamah-Elah-Pinon(reshima)
m.fact("aluf_aholivama_ela_pinon(reshima)")

# -------------------------- Gen.36.42 · THE_LIST_NEARS_ITS_END -------------
# ‹אַלּוּף קְנַז אַלּוּף› (“familiar Kenaz familiar”)
# ‹תֵּימָן אַלּוּף מִבְצָר› (“Teyman familiar Mibzar”)
# "[EN-AID] chief Kenaz, chief Teman, chief Mivtzar,"
m.step("Gen.36.42")
# ‹אַלּוּף קְנַז אַלּוּף› (“familiar Kenaz familiar”)
# ‹תֵּימָן› (“Teyman”)
# — fact holds: familiar-Kenaz-Teyman-Mibzar(reshima)
m.fact("aluf_qenaz_teman_mivtzar(reshima)")

# -------------------------- Gen.36.43 · THE_BRACKET_CLOSES -----------------
# ‹אַלּוּף מַגְדִּיאֵל אַלּוּף› (“familiar Magdiel familiar”)
# ‹עִירָם אֵלֶּה אַלּוּפֵי› (“Iram these familiar”)
# ‹אֱדוֹם לְמֹשְׁבֹתָם בְּאֶרֶץ› (“Edom to-seat-them/their in-earth”)
# ‹אֲחֻזָּתָם הוּא עֵשָׂו› (“something-seized-them/their he/it Esau”)
# ‹אֲבִי אֱדוֹם› (“father Edom”)
# "[EN-AID] chief Magdiel, chief Iram. These are the chiefs of Edom, by
# their dwellings, in the land of their holding — he is Esau, father of
# Edom."
m.step("Gen.36.43")
# ‹אֵלֶּה אַלּוּפֵי אֱדוֹם› (“these familiar Edom”)
# ‹לְמֹשְׁבֹתָם בְּאֶרֶץ אֲחֻזָּתָם› (“to-seat-them/their in-earth
# something-seized-them/their”)
# — fact holds: these-familiar-Edom-in-earth-achuzatam(he/it-Esau-father-
# Edom)
m.fact("ele_alufe_edom_be_eretz_achuzatam(hu_esav_avi_edom)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['toldot_esav_hu_edom(kotev_rishon)', 'laqach_nashav_mi_benot_kenaan(esav, ada_ve_aholivama)', 'basmat_bat_yishmael(achot_nevayot)', 'va_teled_ada_u_vasmat(elifaz_u_reuel)', 'ele_bene_esav(yuldu_lo_be_eretz_kenaan)', 'va_yelekh_el_eretz(esav, mi_pene_yaaqov_achiv)', 'lo_yakhla_eretz_megurehem_la_set_otam(rekhusham_rav)', 'va_yeshev_esav_be_har_seir(hu_edom)', 'toldot_esav_avi_edom(kotev_sheni, be_har_seir)', 'ele_shemot_bene_esav(elifaz_u_reuel)', 'bene_elifaz(teman_ad_qenaz)', 'va_teled_timna_le_elifaz(et_amaleq)', 'bene_reuel(nachat_ad_miza)', 'bene_aholivama(yeush_yalam_qorach)', 'ele_alufe_vene_esav(alufe_elifaz)', 'alufe_elifaz_be_eretz_edom(bene_ada)', 'alufe_reuel_be_eretz_edom(bene_vasmat)', 'alufe_aholivama(yeush_yalam_qorach)', 'ele_vene_esav_ve_alufehem(hu_edom)', 'bene_seir_ha_chori(yoshve_ha_aretz)', 'alufe_ha_chori(bene_seir)', 'va_achot_lotan(timna)', 'bene_shoval(alvan_ad_onam)', 'hu_ana_asher_matza_et_ha_yemim(ba_midbar)', 'bene_ana(dishon_ve_aholivama)', 'bene_dishan_rishon(chemdan_ad_kheran)', 'bene_etzer(bilhan_zaavan_aqan)', 'bene_dishan(utz_va_aran)', 'alufe_ha_chori_rishon(lotan_ad_ana)', 'alufe_ha_chori_le_alufehem(be_eretz_seir)', 'ha_melakhim_asher_malkhu_be_edom(li_fene_melakh_melekh_li_vene_yisrael)', 'va_yimlokh_bela_ben_beor(ir_dinhava)', 'va_yamat_bela_va_yimlokh(yovav_mi_batzra)', 'va_yamat_yovav_va_yimlokh(chusham_ha_temani)', 'va_yimlokh_hadad(ha_make_et_midyan_bi_sede_moav)', 'va_yamat_hadad_va_yimlokh(samla_mi_masreqa)', 'va_yimlokh_shaul(me_rechovot_ha_nahar)', 'va_yamat_shaul_va_yimlokh(baal_chanan_ben_akhbor)', 'va_yimlokh_hadar(ishto_mehetavel_bat_me_zahav)', 'alufe_esav_le_mishpechotam(li_meqomotam_bi_shemotam)', 'aluf_aholivama_ela_pinon(reshima)', 'aluf_qenaz_teman_mivtzar(reshima)', 'ele_alufe_edom_be_eretz_achuzatam(hu_esav_avi_edom)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 0
    assert sorted(m.WORLD["witnessed"]) == ['eight_kings']
    assert m.WORLD["witnessed"]['eight_kings']["cites"] == ['Bereshit Rabbah 83:2']
    assert all('the_penalty_minted_at_gen_55_counted_here' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_brides_name', 'a_forgiveness_claim_left_standing_against_the_ledger'), ('went_to_another_land', 'read_as_escaping_the_covenant_debt'), ('the_roster', 'audited_as_evidence_of_illegitimate_lines'), ('what_was_found', 'a_third_reading_entered_by_the_translation'), ('the_king_list', 'read_as_a_state_of_imported_parts'), ('the_king_from_botzra', 'supplier_liability_applied_to_a_state'), ('the_last_names', 'read_as_a_countdown_and_an_escrow')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 67:13']
    assert all('a_forgiveness_claim_left_standing_against_the_ledger' not in f for f in m.WORLD["facts"])
    assert 'the_brides_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 82:13', 'Onkelos Genesis 36:6']
    assert all('read_as_escaping_the_covenant_debt' not in f for f in m.WORLD["facts"])
    assert 'went_to_another_land' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 82:12', 'Bereshit Rabbah 82:15']
    assert all('audited_as_evidence_of_illegitimate_lines' not in f for f in m.WORLD["facts"])
    assert 'the_roster' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Onkelos Genesis 36:24']
    assert all('a_third_reading_entered_by_the_translation' not in f for f in m.WORLD["facts"])
    assert 'what_was_found' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 83:1']
    assert all('read_as_a_state_of_imported_parts' not in f for f in m.WORLD["facts"])
    assert 'the_king_list' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 83:3']
    assert all('supplier_liability_applied_to_a_state' not in f for f in m.WORLD["facts"])
    assert 'the_king_from_botzra' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 83:4', 'Onkelos Genesis 36:39']
    assert all('read_as_a_countdown_and_an_escrow' not in f for f in m.WORLD["facts"])
    assert 'the_last_names' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
