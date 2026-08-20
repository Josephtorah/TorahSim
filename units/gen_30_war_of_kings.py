#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_30_war_of_kings — 14:1-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_30_war_of_kings.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The war of the kings: the annal, the rescue, the priest, the refused spoils (14:1-24)"""
from machine import Machine

m = Machine("gen_30_war_of_kings")

# -------------------------- Gen.14.1 · THE_COALITION_AND_THE_VALE ----------
# וַיְהִי בִּימֵי אַמְרָפֶל מֶלֶךְ־שִׁנְעָר אַרְיוֹךְ מֶלֶךְ אֶלָּסָר
# כְּדָרְלָעֹמֶר מֶלֶךְ עֵילָם וְתִדְעָל מֶלֶךְ גּוֹיִם … כָּל־אֵלֶּה
# חָבְרוּ אֶל־עֵמֶק הַשִּׂדִּים הוּא יָם הַמֶּלַח
# "[EN-AID/JPS 14:1-3] And it came to pass in the days of Amraphel king of
# Shinar, Arioch king of Ellasar, Chedorlaomer king of Elam, and Tidal king
# of Goiim, that they made war with Bera king of Sodom, and with Birsha king
# of Gomorrah, Shinab king of Admah, and Shemeber king of Zeboiim, and the
# king of Bela — the same is Zoar. All these came as allies unto the vale of
# Siddim — the same is the Salt Sea."
m.step("Gen.14.1")
# ‹עָשׂוּ מִלְחָמָה אֶת־בֶּרַע מֶלֶךְ סְדֹם› (“Esau battle obj-marker in-bad
# king Sodom”) — event: make-war — agent arbaat-the-king
m.event("make_war", agent="arbaat_ha_melakhim")
# ‹כָּל־אֵלֶּה חָבְרוּ אֶל־עֵמֶק הַשִּׂדִּים הוּא יָם הַמֶּלַח› (“all these
# join to deep the-Siddim he/it seas the-powder”) — fact holds: all-these-
# chavru-to-vale-the-Siddim-he/it-yam-the-melach
m.fact("kol_eleh_chavru_el_emeq_ha_sidim_hu_yam_ha_melach")
# reads without prior install (flag, not fix): Shinar, Ellasar, Elam, Sodom,
# Gomorrah, admah, Zeboiim, Zoar, vale-the-Siddim, yam-the-melach
m.presupposed("shinar", "elasar", "elam", "sedom", "amora", "admah", "tzevoyim", "tzoar", "emeq_ha_sidim", "yam_ha_melach")

# -------------------------- Gen.14.4 · THE_CLOCK_AND_THE_SWEEP -------------
# שְׁתֵּים עֶשְׂרֵה שָׁנָה עָבְדוּ אֶת־כְּדָרְלָעֹמֶר וּשְׁלֹשׁ־עֶשְׂרֵה
# שָׁנָה מָרָדוּ … וַיַּכּוּ אֶת־כָּל־שְׂדֵה הָעֲמָלֵקִי וְגַם אֶת־הָאֱמֹרִי
# הַיֹּשֵׁב בְּחַצְצֹן תָּמָר
# "[EN-AID/JPS 14:4-7] Twelve years they served Chedorlaomer, and in the
# thirteenth year they rebelled. And in the fourteenth year came
# Chedorlaomer and the kings that were with him, and smote the Rephaim in
# Ashteroth-karnaim, and the Zuzim in Ham, and the Emim in Shaveh-
# kiriathaim, and the Horites in their mount Seir, unto El-paran, which is
# by the wilderness. And they turned back, and came to En-mishpat — the same
# is Kadesh — and smote all the country of the Amalekites, and also the
# Amorites, that dwelt in Hazazon-tamar."
m.step("Gen.14.4")
# ‹שְׁתֵּים עֶשְׂרֵה שָׁנָה עָבְדוּ … וּשְׁלֹשׁ־עֶשְׂרֵה שָׁנָה מָרָדוּ›
# (“two -teen years work/serve … and-three -teen years rebel”) — fact holds:
# shtem--teen-year-work/serve-obj-marker-Chedorlaomer-and-three--teen-rebel
m.fact("shtem_esreh_shanah_avdu_et_kedarlaomer_u_shelosh_esreh_maradu")
# ‹וַיַּכּוּ אֶת־רְפָאִים … וְאֶת־הַזּוּזִים … וְאֵת הָאֵימִים …
# וְאֶת־הַחֹרִי … אֶת־כָּל־שְׂדֵה הָעֲמָלֵקִי וְגַם אֶת־הָאֱמֹרִי› (“and-
# strike obj-marker Rapha' … and-obj-marker the-Zuzites … and-obj-marker
# the-Emims … and-obj-marker the-Chorite … obj-marker all field the-
# Amalekite and-also obj-marker the-Emorite”) — event: strike — agent
# Chedorlaomer-and-the-king; theme refaim-zuzim-emim-chori-amaleqi-Emorite
m.event("strike", agent="kedarlaomer_ve_ha_melakhim", themes=["refaim_zuzim_emim_chori_amaleqi_emori"])
# reads without prior install (flag, not fix): ashterot-qarnayim, ham,
# shaveh-qiryatayim, har-seir, to-paran, en-mishpat-qadesh, chatzetzon-tamar
m.presupposed("ashterot_qarnayim", "ham", "shaveh_qiryatayim", "har_seir", "el_paran", "en_mishpat_qadesh", "chatzetzon_tamar")

# -------------------------- Gen.14.8 · THE_BATTLE_THE_PITS_THE_PLUNDER -----
# וַיֵּצֵא מֶלֶךְ־סְדֹם … וַיַּעַרְכוּ אִתָּם מִלְחָמָה בְּעֵמֶק הַשִּׂדִּים
# … אַרְבָּעָה מְלָכִים אֶת־הַחֲמִשָּׁה … וַיִּקְחוּ אֶת־כָּל־רְכֻשׁ סְדֹם
# וַעֲמֹרָה וְאֶת־כָּל־אָכְלָם וַיֵּלֵכוּ
# "[EN-AID/JPS 14:8-11] And there went out the king of Sodom... and they set
# the battle in array against them in the vale of Siddim; against
# Chedorlaomer... four kings against the five. Now the vale of Siddim was
# full of slime pits; and the kings of Sodom and Gomorrah fled, and they
# fell there, and they that remained fled to the mountain. And they took all
# the goods of Sodom and Gomorrah, and all their victuals, and went their
# way."
m.step("Gen.14.8")
# ‹וַיַּעַרְכוּ אִתָּם מִלְחָמָה› (“and-set-in-a-row with-them/their
# battle”) — event: array-battle — agent chameshet-the-king
m.event("array_battle", agent="chameshet_ha_melakhim")
# ‹אַרְבָּעָה מְלָכִים אֶת־הַחֲמִשָּׁה … וְעֵמֶק הַשִׂדִּים בֶּאֱרֹת
# בֶּאֱרֹת חֵמָר› (“four king obj-marker the-five … and-vale the-Siddim pit
# pit male-ass”) — fact holds: four-king-obj-marker-the-chamishah; vale-the-
# Siddim-beerot-beerot-chemar
m.fact("arbaah_melakhim_et_ha_chamishah",
       "emeq_ha_sidim_beerot_beerot_chemar")
# ‹וַיָּנֻסוּ מֶלֶךְ־סְדֹם וַעֲמֹרָה וַיִּפְּלוּ־שָׁמָּה› (“and-flit king
# Sodom and-Gomorrah and-fall there-ward”) — event: flee — agent king-Sodom-
# and-amorah
m.event("flee", agent="melekh_sedom_va_amorah")
# ‹וַיִּקְחוּ אֶת־כָּל־רְכֻשׁ סְדֹם וַעֲמֹרָה וְאֶת־כָּל־אָכְלָם וַיֵּלֵכוּ›
# (“and-take obj-marker all lay-up Sodom and-Gomorrah and-obj-marker all
# food-them/their and-go”) — event: take — agent arbaat-the-king; theme all-
# property-Sodom-and-amorah
m.event("take", agent="arbaat_ha_melakhim", themes=["kol_rekhush_sedom_va_amorah"])
# reads without prior install (flag, not fix): Gentile-land
m.presupposed("goyim_land")

# -------------------------- Gen.14.12 · THE_TAKING_OF_LOT ------------------
# וַיִּקְחוּ אֶת־לוֹט וְאֶת־רְכֻשׁוֹ בֶּן־אֲחִי אַבְרָם וַיֵּלֵכוּ וְהוּא
# יֹשֵׁב בִּסְדֹם
# "And they took Lot, Abram's brother's son, who dwelt in Sodom, and his
# goods, and departed."
m.step("Gen.14.12")
# ‹וַיִּקְחוּ אֶת־לוֹט וְאֶת־רְכֻשׁוֹ› (“and-take obj-marker Lot and-obj-
# marker property-him/its”) — event: take — agent arbaat-the-king; theme Lot
m.event("take", agent="arbaat_ha_melakhim", themes=["lot"])
# ‹וְהוּא יֹשֵׁב בִּסְדֹם› (“and-he/it dwell/sit in-Sodom”) — fact holds:
# and-he/it-dwell/sit-bi-Sodom
m.fact("ve_hu_yoshev_bi_sedom")

# -------------------------- Gen.14.13 · THE_REFUGEE_AND_THE_HEBREW ---------
# וַיָּבֹא הַפָּלִיט וַיַּגֵּד לְאַבְרָם הָעִבְרִי וְהוּא שֹׁכֵן בְּאֵלֹנֵי
# מַמְרֵא הָאֱמֹרִי אֲחִי אֶשְׁכֹּל וַאֲחִי עָנֵר וְהֵם בַּעֲלֵי
# בְרִית־אַבְרָם
# "And there came one that had escaped, and told Abram the Hebrew — now he
# dwelt by the terebinths of Mamre the Amorite, brother of Eshcol, and
# brother of Aner; and these were confederate with Abram."
m.step("Gen.14.13")
# ‹וַיָּבֹא הַפָּלִיט› (“and-come/bring the-refugee”) — event: come — agent
# the-refugee
m.event("come", agent="ha_palit")
# ‹וַיַּגֵּד לְאַבְרָם הָעִבְרִי› (“and-tell to-Abram the-Hebrew”) — event:
# tell — agent the-refugee
m.event("tell", agent="ha_palit")
# ‹וְהֵם בַּעֲלֵי בְרִית־אַבְרָם› (“and-they master covenant Abram”) — fact
# holds: and-they-baalei-covenant-Abram
m.fact("ve_hem_baalei_verit_avram")

# -------------------------- Gen.14.14 · THE_MUSTER_OF_THE_318 --------------
# וַיִּשְׁמַע אַבְרָם כִּי נִשְׁבָּה אָחִיו וַיָּרֶק אֶת־חֲנִיכָיו יְלִידֵי
# בֵיתוֹ שְׁמֹנָה עָשָׂר וּשְׁלֹשׁ מֵאוֹת וַיִּרְדֹּף עַד־דָּן
# "And when Abram heard that his brother was taken captive, he led forth his
# trained men, born in his house, three hundred and eighteen, and pursued as
# far as Dan."
m.step("Gen.14.14")
# ‹וַיִּשְׁמַע אַבְרָם כִּי נִשְׁבָּה אָחִיו› (“and-hear Abram that
# transport-into-captivity brother-him/its”) — event: hear — agent Abram
m.event("hear", agent="avram")
# ‹וַיָּרֶק אֶת־חֲנִיכָיו יְלִידֵי בֵיתוֹ› (“and-pour-out obj-marker
# initiated-him/its born house-him/its”) — event: muster — agent Abram;
# theme chanikhav
m.event("muster", agent="avram", themes=["chanikhav"])
# ‹שְׁמֹנָה עָשָׂר וּשְׁלֹשׁ מֵאוֹת› (“number -teen and-three hundred”) —
# fact holds: chanikhav-yelidei-veito-shmonah--teen-and-three-hundred
m.fact("chanikhav_yelidei_veito_shmonah_asar_u_shelosh_meot")
# ‹וַיִּרְדֹּף עַד־דָּן› (“and-run-after-gone-by) until Daniel”) — event:
# pursue — agent Abram
m.event("pursue", agent="avram")
# reads without prior install (flag, not fix): Daniel
m.presupposed("dan")

# -------------------------- Gen.14.15 · THE_NIGHT_SPLIT --------------------
# וַיֵּחָלֵק עֲלֵיהֶם לַיְלָה הוּא וַעֲבָדָיו וַיַּכֵּם וַיִּרְדְּפֵם
# עַד־חוֹבָה אֲשֶׁר מִשְּׂמֹאל לְדַמָּשֶׂק
# "And he divided himself against them by night, he and his servants, and
# smote them, and pursued them unto Hobah, which is on the left hand of
# Damascus."
m.step("Gen.14.15")
# ‹וַיֵּחָלֵק עֲלֵיהֶם לַיְלָה› (“and-be-smooth over-them/their night”) —
# event: split — agent Abram-and-avadav
m.event("split", agent="avram_va_avadav")
# ‹וַיַּכֵּם› (“and-strike-them/their”) — event: strike — agent Abram-and-
# avadav
m.event("strike", agent="avram_va_avadav")
# ‹וַיִּרְדְּפֵם עַד־חוֹבָה אֲשֶׁר מִשְּׂמֹאל לְדַמָּשֶׂק› (“and-run-after-
# gone-by)-them/their until Hobah which from-dark to-Damascus”) — event:
# pursue — agent Abram-and-avadav
m.event("pursue", agent="avram_va_avadav")
# reads without prior install (flag, not fix): chovah, Damascus
m.presupposed("chovah", "damaseq")

# -------------------------- Gen.14.16 · THE_BRINGING_BACK ------------------
# וַיָּשֶׁב אֵת כָּל־הָרְכֻשׁ וְגַם אֶת־לוֹט אָחִיו וּרְכֻשׁוֹ הֵשִׁיב וְגַם
# אֶת־הַנָּשִׁים וְאֶת־הָעָם
# "And he brought back all the goods, and also brought back his brother Lot,
# and his goods, and the women also, and the people."
m.step("Gen.14.16")
# ‹וַיָּשֶׁב אֵת כָּל־הָרְכֻשׁ … הֵשִׁיב› (“and-return obj-marker all the-
# property … return”) — event: bring-back — agent Abram; theme all-the-
# property-and-Lot-and-the-woman-and-the-people
m.event("bring_back", agent="avram", themes=["kol_ha_rekhush_ve_lot_ve_ha_nashim_ve_ha_am"])

# -------------------------- Gen.14.17 · THE_KINGS_MEETING ------------------
# וַיֵּצֵא מֶלֶךְ־סְדֹם לִקְרָאתוֹ אַחֲרֵי שׁוּבוֹ מֵהַכּוֹת
# אֶת־כְּדָרלָעֹמֶר וְאֶת־הַמְּלָכִים אֲשֶׁר אִתּוֹ אֶל־עֵמֶק שָׁוֵה הוּא
# עֵמֶק הַמֶּלֶךְ
# "And the king of Sodom went out to meet him, after his return from the
# slaughter of Chedorlaomer and the kings that were with him, at the vale of
# Shaveh — the same is the King's Vale."
m.step("Gen.14.17")
# ‹וַיֵּצֵא מֶלֶךְ־סְדֹם לִקְרָאתוֹ› (“and-bring-forth king Sodom to-
# encountering-him/its”) — event: go-out — agent king-Sodom
m.event("go_out", agent="melekh_sedom")
# reads without prior install (flag, not fix): vale-shaveh
m.presupposed("emeq_shaveh")

# -------------------------- Gen.14.18 · BREAD_WINE_AND_A_PRIEST ------------
# וּמַלְכִּי־צֶדֶק מֶלֶךְ שָׁלֵם הוֹצִיא לֶחֶם וָיָיִן וְהוּא כֹהֵן לְאֵל
# עֶלְיוֹן
# "And Melchizedek king of Salem brought forth bread and wine; and he was
# priest of God the Most High."
m.step("Gen.14.18")
# ‹הוֹצִיא לֶחֶם וָיָיִן› (“bring-forth food and-wine”) — event: bring-out —
# agent I-Melchizedek; theme food-and-wine
m.event("bring_out", agent="malki_tzedeq", themes=["lechem_va_yayin"])
# ‹וְהוּא כֹהֵן לְאֵל עֶלְיוֹן› (“and-he/it priest to-God Most-High”) — fact
# holds: and-he/it-priest-to-to-Most-High
m.fact("ve_hu_khohen_le_el_elyon")
# reads without prior install (flag, not fix): Salem
m.presupposed("shalem")

# -------------------------- Gen.14.19 · THE_BLESSING_OF_ABRAM --------------
# וַיְבָרְכֵהוּ וַיֹּאמַר בָּרוּךְ אַבְרָם לְאֵל עֶלְיוֹן קֹנֵה שָׁמַיִם
# וָאָרֶץ
# "And he blessed him, and said: 'Blessed be Abram of God Most High, Maker
# of heaven and earth;"
m.step("Gen.14.19")
# ‹וַיְבָרְכֵהוּ› (“and-bless-him/its”) — blessing: I-Melchizedek blesses
# Abram
m.bless("malki_tzedeq", "avram")
# ‹בָּרוּךְ אַבְרָם לְאֵל עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ› (“bless Abram to-
# God Most-High possessor heavens and-earth”) — fact holds: bless-Abram-to-
# to-Most-High-qoneh-heavens-and-earth
m.fact("barukh_avram_le_el_elyon_qoneh_shamayim_va_aretz")

# -------------------------- Gen.14.20 · THE_BLESSING_OF_EL_ELYON_AND_THE_TENTH -
# וּבָרוּךְ אֵל עֶלְיוֹן אֲשֶׁר־מִגֵּן צָרֶיךָ בְּיָדֶךָ וַיִּתֶּן־לוֹ
# מַעֲשֵׂר מִכֹּל
# "and blessed be God the Most High, who hath delivered thine enemies into
# thy hand.' And he gave him a tenth of all."
m.step("Gen.14.20")
# ‹וּבָרוּךְ אֵל עֶלְיוֹן› (“and-bless strength Most-High”) — blessing:
# I-Melchizedek blesses to-Most-High
m.bless("malki_tzedeq", "el_elyon")
# ‹אֲשֶׁר־מִגֵּן צָרֶיךָ בְּיָדֶךָ› (“which shield narrow-you/your in-hand-
# you/your”) — fact holds: which-miggen-tzarekha-in-yadekha
m.fact("asher_miggen_tzarekha_be_yadekha")
# ‹וַיִּתֶּן־לוֹ מַעֲשֵׂר מִכֹּל› (“and-set to-him/its tenth from-all”) —
# event: give — theme tenth-from-all
m.event("give", themes=["maaser_mi_kol"])

# -------------------------- Gen.14.21 · THE_KINGS_DEMANDS ------------------
# וַיֹּאמֶר מֶלֶךְ־סְדֹם אֶל־אַבְרָם תֶּן־לִי הַנֶּפֶשׁ וְהָרְכֻשׁ קַח־לָךְ
# "And the king of Sodom said unto Abram: 'Give me the persons, and take the
# goods to thyself.'"
m.step("Gen.14.21")
# ‹וַיֹּאמֶר מֶלֶךְ־סְדֹם אֶל־אַבְרָם› (“and-say king Sodom to Abram”) —
# event: say — agent king-Sodom
m.event("say", agent="melekh_sedom")
# ‹תֶּן־לִי הַנֶּפֶשׁ› (“set to-me/my the-living-being”) — king-Sodom speaks
# a demand — LET: set(Abram, the-living-being)
m.declare("melekh_sedom", "LET",
          "ten(avram, ha_nefesh)")
# ‹וְהָרְכֻשׁ קַח־לָךְ› (“and-the-property take to-you/your”) — king-Sodom
# speaks a demand — LET: take(Abram, the-property)
m.declare("melekh_sedom", "LET",
          "qach(avram, ha_rekhush)")

# -------------------------- Gen.14.22 · THE_RAISED_HAND --------------------
# וַיֹּאמֶר אַבְרָם אֶל־מֶלֶךְ סְדֹם הֲרִימֹתִי יָדִי אֶל־יְהוָה אֵל
# עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ
# "And Abram said to the king of Sodom: 'I have lifted up my hand unto the
# LORD, God Most High, Maker of heaven and earth,"
m.step("Gen.14.22")
# ‹וַיֹּאמֶר אַבְרָם אֶל־מֶלֶךְ סְדֹם› (“and-say Abram to king Sodom”) —
# event: say — agent Abram
m.event("say", agent="avram")
# ‹הֲרִימֹתִי יָדִי אֶל־יְהוָה אֵל עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ› (“rise-
# high hand-me/my to YHWH strength Most-High possessor heavens and-earth”) —
# fact holds: rise-high-yadi-to-the-LORD-to-Most-High-qoneh-heavens-and-
# earth
m.fact("harimoti_yadi_el_YHWH_el_elyon_qoneh_shamayim_va_aretz")

# -------------------------- Gen.14.23 · THE_THREAD_AND_THE_THONG -----------
# אִם־מִחוּט וְעַד שְׂרוֹךְ־נַעַל וְאִם־אֶקַּח מִכָּל־אֲשֶׁר־לָךְ וְלֹא
# תֹאמַר אֲנִי הֶעֱשַׁרְתִּי אֶת־אַבְרָם
# "that I will not take a thread nor a shoe-latchet nor aught that is thine,
# lest thou shouldest say: I have made Abram rich;"
m.step("Gen.14.23")
# ‹אִם־מִחוּט וְעַד שְׂרוֹךְ־נַעַל וְאִם־אֶקַּח … וְלֹא תֹאמַר אֲנִי
# הֶעֱשַׁרְתִּי אֶת־אַבְרָם› (“if from-string and-until thong sandal-tongue
# and-if take … and-not say accumulate obj-marker Abram”) — fact holds: if-
# from-string-and-until-thong-sandal-tongue-and-if-take-from-all-which-to-
# you; and-not-say-ani-accumulate-obj-marker-Abram
m.fact("im_mi_chut_ve_ad_serokh_naal_ve_im_eqach_mi_kol_asher_lakh",
       "ve_lo_tomar_ani_heesharti_et_avram")

# -------------------------- Gen.14.24 · THE_EXCEPTION_AND_THE_PORTION ------
# בִּלְעָדַי רַק אֲשֶׁר אָכְלוּ הַנְּעָרִים וְחֵלֶק הָאֲנָשִׁים אֲשֶׁר
# הָלְכוּ אִתִּי עָנֵר אֶשְׁכֹּל וּמַמְרֵא הֵם יִקְחוּ חֶלְקָם
# "save only that which the young men have eaten, and the portion of the men
# which went with me, Aner, Eshcol, and Mamre, let them take their
# portion.'"
m.step("Gen.14.24")
# ‹בִּלְעָדַי רַק אֲשֶׁר אָכְלוּ הַנְּעָרִים› (“except-me/my leanness which
# eat the-boy”) — fact holds: biladai-leanness-which-eat-the-boy
m.fact("biladai_raq_asher_akhlu_ha_nearim")
# ‹עָנֵר אֶשְׁכֹּל וּמַמְרֵא הֵם יִקְחוּ חֶלְקָם› (“Aner Eshcol and-Mamre
# they take smoothness-them/their”) — Abram speaks a demand — LET:
# take(Aner-Eshcol-Mamre, chelqam)
m.declare("avram", "LET",
          "yiqchu(aner_eshkol_mamre, chelqam)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'admah', 'amora', 'ashterot_qarnayim', 'chatzetzon_tamar', 'chovah', 'damaseq', 'dan', 'el_paran', 'elam', 'elasar', 'emeq_ha_sidim', 'emeq_shaveh', 'en_mishpat_qadesh', 'goyim_land', 'ham', 'har_seir', 'sedom', 'shalem', 'shaveh_qiryatayim', 'shinar', 'tzevoyim', 'tzoar', 'yam_ha_melach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['ten(avram, ha_nefesh)', 'qach(avram, ha_rekhush)', 'yiqchu(aner_eshkol_mamre, chelqam)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 23}
    assert sorted(m.WORLD["facts"]) == sorted(['kol_eleh_chavru_el_emeq_ha_sidim_hu_yam_ha_melach', 'shtem_esreh_shanah_avdu_et_kedarlaomer_u_shelosh_esreh_maradu', 'arbaah_melakhim_et_ha_chamishah', 'emeq_ha_sidim_beerot_beerot_chemar', 've_hu_yoshev_bi_sedom', 've_hem_baalei_verit_avram', 'chanikhav_yelidei_veito_shmonah_asar_u_shelosh_meot', 've_hu_khohen_le_el_elyon', 'barukh_avram_le_el_elyon_qoneh_shamayim_va_aretz', 'asher_miggen_tzarekha_be_yadekha', 'harimoti_yadi_el_YHWH_el_elyon_qoneh_shamayim_va_aretz', 'im_mi_chut_ve_ad_serokh_naal_ve_im_eqach_mi_kol_asher_lakh', 've_lo_tomar_ani_heesharti_et_avram', 'biladai_raq_asher_akhlu_ha_nearim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 25
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
