#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_24_nations_table — 10:1-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_24_nations_table.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The nations table: of these the nations divided after the flood (10:1-32)"""
from machine import Machine

m = Machine("gen_24_nations_table")

# -------------------------- Gen.10.1 · THE_FOURTH_TOLEDOT_HEADING ----------
# וְאֵלֶּה תּוֹלְדֹת בְּנֵי־נֹחַ שֵׁם חָם וָיָפֶת וַיִּוָּלְדוּ לָהֶם
# בָּנִים אַחַר הַמַּבּוּל
# "Now these are the generations of the sons of Noah: Shem, Ham, and
# Japheth; and unto them were sons born after the flood."
m.step("Gen.10.1")
# ‹וְאֵלֶּה תּוֹלְדֹת בְּנֵי־נֹחַ שֵׁם חָם וָיָפֶת› (“and-these generations-
# of sons-of Noah Sem Ham and-Japheth”) — section generations-sons-of-Noach:
# Sem, Ham, Japheth
m.section("toledot_bnei_noach", "shem", "cham", "yefet")
# ‹וַיִּוָּלְדוּ לָהֶם בָּנִים אַחַר הַמַּבּוּל› (“and-were-born to-them
# sons-of after the-deluge”) — event: in-born — theme sons-of-after-the-
# deluge
m.event("be_born", themes=["banim_achar_ha_mabul"])
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")

# -------------------------- Gen.10.2-5 · YEFET_ROWS_AND_THE_ANOMALOUS_CLOSE -
# בְּנֵי יֶפֶת גֹּמֶר וּמָגוֹג וּמָדַי וְיָוָן וְתֻבָל וּמֶשֶׁךְ וְתִירָס …
# מֵאֵלֶּה נִפְרְדוּ אִיֵּי הַגּוֹיִם בְּאַרְצֹתָם אִישׁ לִלְשֹׁנוֹ
# לְמִשְׁפְּחֹתָם בְּגוֹיֵהֶם
# "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshech, Tiras —
# and the sons of Gomer and of Javan — of these were the isles of the
# nations divided in their lands, every one after his tongue, after their
# families, in their nations."
m.step("Gen.10.2-5")
# ‹בְּנֵי יֶפֶת גֹּמֶר וּמָגוֹג וּמָדַי וְיָוָן וְתֻבָל וּמֶשֶׁךְ וְתִירָס›
# (“son Japheth Gomer and-Magog and-Madai and-Javan and-Tubal and-Mesech
# and-Tiras”) — fact holds: sons-of-Japheth-Gomer-and-Magog-and-Madai-and-
# Javan
m.fact("bnei_yefet_gomer_u_magog_u_maday_ve_yavan")
# ‹מֵאֵלֶּה נִפְרְדוּ אִיֵּי הַגּוֹיִם … אִישׁ לִלְשֹׁנוֹ› (“from-these
# break-through habitable-spot the-nation … man to-tongue-him/its”) — fact
# holds: and-from-these-nifredu-iyei-the-nations-in-artzotam; each-to-me-
# leshono-to-mishpechotam-in-goyehem
m.fact("u_me_eleh_nifredu_iyei_ha_goyim_be_artzotam",
       "ish_li_leshono_le_mishpechotam_be_goyehem")

# -------------------------- Gen.10.6-7 · HAM_ROWS_KUSH_TO_DEDAN ------------
# וּבְנֵי חָם כּוּשׁ וּמִצְרַיִם וּפוּט וּכְנָעַן וּבְנֵי כוּשׁ סְבָא
# וַחֲוִילָה וְסַבְתָּה וְרַעְמָה וְסַבְתְּכָא וּבְנֵי רַעְמָה שְׁבָא
# וּדְדָן
# "And the sons of Ham: Cush, and Mizraim, and Put, and Canaan. And the sons
# of Cush: Seba, and Havilah, and Sabtah, and Raamah, and Sabteca; and the
# sons of Raamah: Sheba, and Dedan."
m.step("Gen.10.6-7")
# ‹וּבְנֵי חָם כּוּשׁ וּמִצְרַיִם וּפוּט וּכְנָעַן …› (“and-son Ham Chush
# and-Egypt and-Phut and-Canaan”) — fact holds: sons-of-Ham-Chush-and-Egypt-
# and-Phut-and-Canaan; sons-of-Chush-Seba-and-Havilah-and-vnei-ramah
m.fact("bnei_cham_kush_u_mitzrayim_u_fut_u_khenaan",
       "bnei_khush_seva_va_chavilah_u_vnei_ramah")

# -------------------------- Gen.10.8-9 · NIMROD_AND_THE_PROVERB ------------
# וְכוּשׁ יָלַד אֶת־נִמְרֹד הוּא הֵחֵל לִהְיוֹת גִּבֹּר בָּאָרֶץ הוּא־הָיָה
# גִבֹּר־צַיִד לִפְנֵי יְהוָה עַל־כֵּן יֵאָמַר כְּנִמְרֹד גִּבּוֹר צַיִד
# לִפְנֵי יְהוָה
# "And Cush begot Nimrod; he began to be a mighty one in the earth. He was a
# mighty hunter before the LORD; wherefore it is said: 'Like Nimrod a mighty
# hunter before the LORD.'"
m.step("Gen.10.8-9")
# ‹וְכוּשׁ יָלַד אֶת־נִמְרֹד› (“and-Chush bear-young obj-marker Nimrod”) —
# event: beget — agent Chush; theme Nimrod
m.event("beget", agent="kush", themes=["nimrod"])
# ‹הוּא הֵחֵל לִהְיוֹת גִּבֹּר בָּאָרֶץ … גִבֹּר־צַיִד לִפְנֵי יְהוָה›
# (“he/it bore to-be powerful in-earth … powerful chase to-face YHWH”) —
# fact holds: he-began-lihyot-gibbor-in-the-earth; gibbor-hunter-lifnei-yhwh
m.fact("hu_hechel_lihyot_gibbor_ba_aretz",
       "gibbor_tzayid_lifnei_yhwh")
# ‹עַל־כֵּן יֵאָמַר כְּנִמְרֹד גִּבּוֹר צַיִד לִפְנֵי יְהוָה› (“over so say
# like-Nimrod powerful chase to-face YHWH”) — pattern recorded: like-Nimrod-
# gibbor-hunter-lifnei-yhwh
m.pattern("ke_nimrod_gibbor_tzayid_lifnei_yhwh")

# -------------------------- Gen.10.10-12 · THE_KINGDOM_AND_THE_FOUR_CITIES -
# וַתְּהִי רֵאשִׁית מַמְלַכְתּוֹ בָּבֶל וְאֶרֶךְ וְאַכַּד וְכַלְנֵה בְּאֶרֶץ
# שִׁנְעָר מִן־הָאָרֶץ הַהִוא יָצָא אַשּׁוּר וַיִּבֶן אֶת־נִינְוֵה
# וְאֶת־רְחֹבֹת עִיר וְאֶת־כָּלַח וְאֶת־רֶסֶן בֵּין נִינְוֵה וּבֵין כָּלַח
# הִוא הָעִיר הַגְּדֹלָה
# "And the beginning of his kingdom was Babel, and Erech, and Accad, and
# Calneh, in the land of Shinar. Out of that land went forth Asshur, and
# builded Nineveh, and Rehoboth-ir, and Calah, and Resen between Nineveh and
# Calah — the same is the great city."
m.step("Gen.10.10-12")
# ‹וַתְּהִי רֵאשִׁית מַמְלַכְתּוֹ בָּבֶל … בְּאֶרֶץ שִׁנְעָר› (“and-be
# beginning dominion-him/its Babel … in-earth Shinar”) — fact holds:
# beginning-of-mamlakhto-Babel-in-land-Shinar; from-the-earth-the-hi-went-
# out-Ashur
m.fact("reshit_mamlakhto_bavel_be_eretz_shinar",
       "min_ha_aretz_ha_hi_yatza_ashur")
# ‹וַיִּבֶן אֶת־נִינְוֵה וְאֶת־רְחֹבֹת עִיר וְאֶת־כָּלַח וְאֶת־רֶסֶן› (“and-
# build obj-marker Nineveh and-obj-marker Rehoboth city and-obj-marker Calah
# and-obj-marker Resen”) — event: build — theme ninveh, Rehoboth-city,
# Calah, Resen
m.event("build", themes=["ninveh", "rechovot_ir", "kalach", "resen"])
# ‹וַיִּבֶן אֶת־נִינְוֵה וְאֶת־רְחֹבֹת עִיר וְאֶת־כָּלַח וְאֶת־רֶסֶן› (“and-
# build obj-marker Nineveh and-obj-marker Rehoboth city and-obj-marker Calah
# and-obj-marker Resen”) — the world gains: ninveh, Rehoboth-city, Calah,
# Resen
m.install("ninveh", "rechovot_ir", "kalach", "resen")
# ‹הִוא הָעִיר הַגְּדֹלָה› (“he/it the-city the-great”) — fact holds: hi-
# the-city-the-gedolah
m.fact("hi_ha_ir_ha_gedolah")

# -------------------------- Gen.10.13-14 · MITZRAYIM_ROWS_AND_THE_PHILISTINE_NOTE -
# וּמִצְרַיִם יָלַד אֶת־לוּדִים וְאֶת־עֲנָמִים וְאֶת־לְהָבִים
# וְאֶת־נַפְתֻּחִים וְאֶת־פַּתְרֻסִים וְאֶת־כַּסְלֻחִים אֲשֶׁר יָצְאוּ
# מִשָּׁם פְּלִשְׁתִּים וְאֶת־כַּפְתֹּרִים
# "And Mizraim begot Ludim, and Anamim, and Lehabim, and Naphtuhim, and
# Pathrusim, and Casluhim — whence went forth the Philistines — and
# Caphtorim."
m.step("Gen.10.13-14")
# ‹וּמִצְרַיִם יָלַד אֶת־לוּדִים …› (“and-Egypt bear-young obj-marker
# Ludite”) — event: beget — agent Egypt; theme seven-amamim
m.event("beget", agent="mitzrayim", themes=["shivat_amamim"])
# ‹אֲשֶׁר יָצְאוּ מִשָּׁם פְּלִשְׁתִּים› (“which bring-forth from-there
# Pelishtite”) — fact holds: who-bring-forth-from-there-Philistines
m.fact("asher_yatzu_mi_sham_pelishtim")

# -------------------------- Gen.10.15-19 · CANAAN_ROWS_SPREAD_AND_BORDER ---
# וּכְנַעַן יָלַד אֶת־צִידֹן בְּכֹרוֹ וְאֶת־חֵת … וְאַחַר נָפֹצוּ
# מִשְׁפְּחוֹת הַכְּנַעֲנִי וַיְהִי גְּבוּל הַכְּנַעֲנִי מִצִּידֹן …
# עַד־לָשַׁע
# "And Canaan begot Zidon his firstborn, and Heth; and the Jebusite, and the
# Amorite, and the Girgashite; and the Hivite, and the Arkite, and the
# Sinite; and the Arvadite, and the Zemarite, and the Hamathite; and
# afterward were the families of the Canaanite spread abroad. And the border
# of the Canaanite was from Zidon, as thou goest toward Gerar, unto Gaza; as
# thou goest toward Sodom and Gomorrah and Admah and Zeboiim, unto Lasha."
m.step("Gen.10.15-19")
# ‹וּכְנַעַן יָלַד אֶת־צִידֹן בְּכֹרוֹ וְאֶת־חֵת› (“and-Canaan bear-young
# obj-marker Sidon firstborn-him/its and-obj-marker Heth”) — event: beget —
# agent kenaan; theme Sidon-bekhoro, Heth
m.event("beget", agent="kenaan", themes=["tzidon_bekhoro", "chet"])
# ‹וְאֶת־הַיְבוּסִי וְאֶת־הָאֱמֹרִי … וְאַחַר נָפֹצוּ מִשְׁפְּחוֹת
# הַכְּנַעֲנִי› (“and-obj-marker the-Jebusite and-obj-marker the-Emorite …
# and-after dash-in-pieces family the-Kenaanite”) — fact holds: these-the-
# Canaanite-asarah-amamim; and-after-were-spread-mishpechot-the-Canaanite
m.fact("eleh_ha_kenaani_asarah_amamim",
       "ve_achar_nafotzu_mishpechot_ha_kenaani")
# ‹וַיְהִי גְּבוּל הַכְּנַעֲנִי מִצִּידֹן … עַד־לָשַׁע› (“and-be cord the-
# Kenaanite from-Sidon … until Lasha”) — fact holds: border-of-the-
# Canaanite-from-Sidon-until-azah-until-Lasha
m.fact("gevul_ha_kenaani_mi_tzidon_ad_azah_ad_lasha")

# -------------------------- Gen.10.20 · HAM_CLOSE --------------------------
# אֵלֶּה בְנֵי־חָם לְמִשְׁפְּחֹתָם לִלְשֹׁנֹתָם בְּאַרְצֹתָם בְּגוֹיֵהֶם
# "These are the sons of Ham, after their families, after their tongues, in
# their lands, in their nations."
m.step("Gen.10.20")
# ‹אֵלֶּה בְנֵי־חָם … בְּגוֹיֵהֶם› (“these sons-of Ham … in-their-nations”)
# — fact holds: these-vnei-Ham-to-mishpechotam-to-me-leshonotam-in-artzotam-
# in-goyehem
m.fact("eleh_vnei_cham_le_mishpechotam_li_leshonotam_be_artzotam_be_goyehem")

# -------------------------- Gen.10.21-24 · SHEM_OPENER_AND_ROWS ------------
# וּלְשֵׁם יֻלַּד גַּם־הוּא אֲבִי כָּל־בְּנֵי־עֵבֶר אֲחִי יֶפֶת הַגָּדוֹל
# בְּנֵי שֵׁם עֵילָם וְאַשּׁוּר וְאַרְפַּכְשַׁד וְלוּד וַאֲרָם …
# וְאַרְפַּכְשַׁד יָלַד אֶת־שָׁלַח וְשֶׁלַח יָלַד אֶת־עֵבֶר
# "And unto Shem, the father of all the children of Eber, the elder brother
# of Japheth, to him also were children born. The sons of Shem: Elam, and
# Asshur, and Arpachshad, and Lud, and Aram. And the sons of Aram: Uz, and
# Hul, and Gether, and Mash. And Arpachshad begot Shelah; and Shelah begot
# Eber."
m.step("Gen.10.21-24")
# ‹וּלְשֵׁם יֻלַּד גַּם־הוּא› (“and-to-Sem bear-young also he/it”) — event:
# in-born — theme to-Sem-also-he
m.event("be_born", themes=["le_shem_gam_hu"])
# ‹אֲבִי כָּל־בְּנֵי־עֵבֶר אֲחִי יֶפֶת הַגָּדוֹל … בְּנֵי שֵׁם עֵילָם
# וְאַשּׁוּר› (“father all son Eber brother Japheth the-great … son Sem Elam
# and-Asshur”) — fact holds: father-of-all-sons-of-Ever-brother-Japheth-the-
# elder; sons-of-Sem-eilam-and-Ashur-and-Arphaxad
m.fact("avi_kol_bnei_ever_achi_yefet_ha_gadol",
       "bnei_shem_eilam_ve_ashur_ve_arpakhshad")
# ‹וְאַרְפַּכְשַׁד יָלַד אֶת־שָׁלַח› (“and-Arphaxad bear-young obj-marker
# Salah”) — event: beget — agent Arphaxad; theme Salah
m.event("beget", agent="arpakhshad", themes=["shelach"])
# ‹וְשֶׁלַח יָלַד אֶת־עֵבֶר› (“and-Salah bear-young obj-marker Eber”) —
# event: beget — agent Salah; theme Ever
m.event("beget", agent="shelach", themes=["ever"])

# -------------------------- Gen.10.25-29 · PELEG_AND_THE_YOKTAN_ROWS -------
# וּלְעֵבֶר יֻלַּד שְׁנֵי בָנִים שֵׁם הָאֶחָד פֶּלֶג כִּי בְיָמָיו נִפְלְגָה
# הָאָרֶץ וְשֵׁם אָחִיו יָקְטָן וְיָקְטָן יָלַד … כָּל־אֵלֶּה בְּנֵי יָקְטָן
# "And unto Eber were born two sons; the name of the one was Peleg; for in
# his days was the earth divided; and his brother's name was Joktan. And
# Joktan begot Almodad, and Sheleph, and Hazarmaveth, and Jerah; and
# Hadoram, and Uzal, and Diklah; and Obal, and Abimael, and Sheba; and
# Ophir, and Havilah, and Jobab; all these were the sons of Joktan."
m.step("Gen.10.25-29")
# ‹וּלְעֵבֶר יֻלַּד שְׁנֵי בָנִים› (“and-to-Eber bear-young two son”) —
# event: in-born — theme to-Ever-shnei-sons-of
m.event("be_born", themes=["le_ever_shnei_vanim"])
# ‹שֵׁם הָאֶחָד פֶּלֶג כִּי בְיָמָיו נִפְלְגָה הָאָרֶץ› (“name the-one Peleg
# that in-day-him/its split the-earth”) — fact holds: Sem-the-one-Peleg-
# that-and-his-days-niflegah-the-earth; and-Sem-his-brother-yoktan
m.fact("shem_ha_echad_peleg_ki_ve_yamav_niflegah_ha_aretz",
       "ve_shem_achiv_yoktan")
# ‹וְיָקְטָן יָלַד אֶת־אַלְמוֹדָד … וְאֶת־יוֹבָב› (“and-Joktan bear-young
# obj-marker Almodad … and-obj-marker Jobab”) — event: beget — agent yoktan;
# theme shloshah-asar-sons-of
m.event("beget", agent="yoktan", themes=["shloshah_asar_banim"])
# ‹כָּל־אֵלֶּה בְּנֵי יָקְטָן› (“all these son Joktan”) — fact holds: all-
# these-sons-of-yoktan
m.fact("kol_eleh_bnei_yoktan")

# -------------------------- Gen.10.30-31 · THE_DWELLING_AND_SHEM_CLOSE -----
# וַיְהִי מוֹשָׁבָם מִמֵּשָׁא בֹּאֲכָה סְפָרָה הַר הַקֶּדֶם אֵלֶּה
# בְנֵי־שֵׁם לְמִשְׁפְּחֹתָם לִלְשֹׁנֹתָם בְּאַרְצֹתָם לְגוֹיֵהֶם
# "And their dwelling was from Mesha, as thou goest toward Sephar, unto the
# mountain of the east. These are the sons of Shem, after their families,
# after their tongues, in their lands, after their nations."
m.step("Gen.10.30-31")
# ‹וַיְהִי מוֹשָׁבָם מִמֵּשָׁא בֹּאֲכָה סְפָרָה הַר הַקֶּדֶם› (“and-be seat-
# them/their from-Mesha come/bring-you/your Sephar-ward mountain the-front”)
# — fact holds: moshavam-from-Mesha-mountain-the-east
m.fact("moshavam_mi_mesha_har_ha_qedem")
# ‹אֵלֶּה בְנֵי־שֵׁם … לְגוֹיֵהֶם› (“these son Sem … to-nation-them/their”)
# — fact holds: these-vnei-Sem-to-mishpechotam-to-me-leshonotam-in-artzotam-
# to-goyehem
m.fact("eleh_vnei_shem_le_mishpechotam_li_leshonotam_be_artzotam_le_goyehem")

# -------------------------- Gen.10.32 · THE_GRAND_CLOSE_SEALS_THE_INCLUSIO -
# אֵלֶּה מִשְׁפְּחֹת בְּנֵי־נֹחַ לְתוֹלְדֹתָם בְּגוֹיֵהֶם וּמֵאֵלֶּה
# נִפְרְדוּ הַגּוֹיִם בָּאָרֶץ אַחַר הַמַּבּוּל
# "These are the families of the sons of Noah, after their generations, in
# their nations; and of these were the nations divided in the earth after
# the flood."
m.step("Gen.10.32")
# ‹אֵלֶּה מִשְׁפְּחֹת בְּנֵי־נֹחַ … וּמֵאֵלֶּה נִפְרְדוּ הַגּוֹיִם בָּאָרֶץ
# אַחַר הַמַּבּוּל› (“these families-of sons-of Noah … and-from-these
# divided the-nations in-the-land after the-deluge”) — fact holds: these-
# mishpechot-sons-of-Noach-to-toledotam; and-from-these-nifredu-the-nations-
# in-the-earth-after-the-deluge
m.fact("eleh_mishpechot_bnei_noach_le_toledotam",
       "u_me_eleh_nifredu_ha_goyim_ba_aretz_achar_ha_mabul")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'kalach', 'ninveh', 'rechovot_ir', 'resen'}
    assert m.presupposed_set() == {'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['bnei_yefet_gomer_u_magog_u_maday_ve_yavan', 'u_me_eleh_nifredu_iyei_ha_goyim_be_artzotam', 'ish_li_leshono_le_mishpechotam_be_goyehem', 'bnei_cham_kush_u_mitzrayim_u_fut_u_khenaan', 'bnei_khush_seva_va_chavilah_u_vnei_ramah', 'hu_hechel_lihyot_gibbor_ba_aretz', 'gibbor_tzayid_lifnei_yhwh', 'pattern: ke_nimrod_gibbor_tzayid_lifnei_yhwh', 'reshit_mamlakhto_bavel_be_eretz_shinar', 'min_ha_aretz_ha_hi_yatza_ashur', 'hi_ha_ir_ha_gedolah', 'asher_yatzu_mi_sham_pelishtim', 'eleh_ha_kenaani_asarah_amamim', 've_achar_nafotzu_mishpechot_ha_kenaani', 'gevul_ha_kenaani_mi_tzidon_ad_azah_ad_lasha', 'eleh_vnei_cham_le_mishpechotam_li_leshonotam_be_artzotam_be_goyehem', 'avi_kol_bnei_ever_achi_yefet_ha_gadol', 'bnei_shem_eilam_ve_ashur_ve_arpakhshad', 'shem_ha_echad_peleg_ki_ve_yamav_niflegah_ha_aretz', 've_shem_achiv_yoktan', 'kol_eleh_bnei_yoktan', 'moshavam_mi_mesha_har_ha_qedem', 'eleh_vnei_shem_le_mishpechotam_li_leshonotam_be_artzotam_le_goyehem', 'eleh_mishpechot_bnei_noach_le_toledotam', 'u_me_eleh_nifredu_ha_goyim_ba_aretz_achar_ha_mabul'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
