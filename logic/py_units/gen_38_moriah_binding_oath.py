#!/usr/bin/env python3
# =============================================================================
# gen_38_moriah_binding_oath — 22:1-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_38_moriah_binding_oath.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The test, the binding, the oath (22:1-24)"""
from machine import Machine

m = Machine("gen_38_moriah_binding_oath")

# -------------------------- Gen.22.1 · THE_FRAME_AND_THE_TEST --------------
# וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם
# וַיֹּאמֶר אֵלָיו אַבְרָהָם וַיֹּאמֶר הִנֵּנִי
# "And it came to pass after these things, that God did prove Abraham, and
# said unto him: 'Abraham'; and he said: 'Here am I.'"
m.step("Gen.22.1")
# ‹וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם … הִנֵּנִי› fact holds: achar-the-
# devarim-and-the-God-nisah-avraham; and-yomer-behold-I
m.fact("achar_ha_devarim_ve_ha_elohim_nisah_et_avraham",
       "va_yomer_hineni")

# -------------------------- Gen.22.2 · THE_CROWN_COMMAND -------------------
# וַיֹּאמֶר קַח־נָא אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק
# וְלֶךְ־לְךָ אֶל־אֶרֶץ הַמֹּרִיָּה וְהַעֲלֵהוּ שָׁם לְעֹלָה עַל אַחַד
# הֶהָרִים אֲשֶׁר אֹמַר אֵלֶיךָ
# "And He said: 'Take now thy son, thine only son, whom thou lovest, even
# Isaac, and get thee into the land of Moriah; and offer him there for a
# burnt-offering upon one of the mountains which I will tell thee of.'"
m.step("Gen.22.2")
# ‹קַח־נָא … וְלֶךְ־לְךָ … וְהַעֲלֵהוּ שָׁם לְעֹלָה› God speaks a demand —
# LET: qach-lekh-and-haalehu(binkha, to-burnt-offering)
m.declare("elohim", "LET",
          "qach_lekh_ve_haalehu(et_binkha, le_olah)")
# ‹אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק› fact holds:
# binkha-yechidkha-which-ahavta-yitzchaq; to-earth-the-moriyah-which-omar-
# to-you
m.fact("et_binkha_et_yechidkha_asher_ahavta_et_yitzchaq",
       "el_eretz_ha_moriyah_asher_omar_elekha")

# -------------------------- Gen.22.3 · THE_DAWN_OBEDIENCE_TWO_ROOTS_RETURN -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת־חֲמֹרוֹ וַיִּקַּח
# אֶת־שְׁנֵי נְעָרָיו אִתּוֹ וְאֵת יִצְחָק בְּנוֹ וַיְבַקַּע עֲצֵי עֹלָה
# וַיָּקָם וַיֵּלֶךְ אֶל־הַמָּקוֹם אֲשֶׁר־אָמַר־לוֹ הָאֱלֹהִים
# "And Abraham rose early in the morning, and saddled his ass, and took two
# of his young men with him, and Isaac his son; and he cleaved the wood for
# the burnt-offering, and rose up, and went unto the place of which God had
# told him."
m.step("Gen.22.3")
# ‹וְאֵת יִצְחָק בְּנוֹ› the world gains: yitzchaq
m.install("yitzchaq")
# ‹אֶת־שְׁנֵי נְעָרָיו› the world gains: shnei-nearav
m.install("shnei_nearav")
# ‹וַיַּשְׁכֵּם … וַיַּחֲבֹשׁ … וַיִּקַּח … וַיְבַקַּע … וַיָּקָם וַיֵּלֶךְ›
# event: dawn-journey — agent avraham
m.event("dawn_journey", agent="avraham")
# ‹וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת־חֲמֹרוֹ› fact holds:
# and-yashkem-in-the-morning-and-yachavosh-chamoro
m.fact("va_yashkem_ba_boqer_va_yachavosh_et_chamoro")

# -------------------------- Gen.22.4 · THE_THIRD_DAY_SIGHTING --------------
# בַּיּוֹם הַשְּׁלִישִׁי וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו וַיַּרְא
# אֶת־הַמָּקוֹם מֵרָחֹק
# "On the third day Abraham lifted up his eyes, and saw the place afar off."
m.step("Gen.22.4")
# ‹בַּיּוֹם הַשְּׁלִישִׁי … מֵרָחֹק› fact holds: in-the-day-the-shelishi-
# and-yar-the-maqom-from-rachoq
m.fact("ba_yom_ha_shelishi_va_yar_et_ha_maqom_me_rachoq")

# -------------------------- Gen.22.5 · THE_STAY_DEMAND_AND_THE_EXCLUSIVE_WE -
# וַיֹּאמֶר אַבְרָהָם אֶל־נְעָרָיו שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר וַאֲנִי
# וְהַנַּעַר נֵלְכָה עַד־כֹּה וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם
# "And Abraham said unto his young men: 'Abide ye here with the ass, and I
# and the lad will go yonder; and we will worship, and come back to you.'"
m.step("Gen.22.5")
# ‹שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר› avraham speaks a demand — LET: shevu(po-
# if-the-chamor)
m.declare("avraham", "LET",
          "shevu(po_im_ha_chamor)")
# ‹נֵלְכָה … וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם› fact holds: nelkha-and-
# nishtachaveh-and-nashuvah-aleikhem
m.fact("nelkha_ve_nishtachaveh_ve_nashuvah_aleikhem")

# -------------------------- Gen.22.6 · THE_LOADED_WALK_TOGETHER ------------
# וַיִּקַּח אַבְרָהָם אֶת־עֲצֵי הָעֹלָה וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ
# וַיִּקַּח בְּיָדוֹ אֶת־הָאֵשׁ וְאֶת־הַמַּאֲכֶלֶת וַיֵּלְכוּ שְׁנֵיהֶם
# יַחְדָּו
# "And Abraham took the wood of the burnt-offering, and laid it upon Isaac
# his son; and he took in his hand the fire and the knife; and they went
# both of them together."
m.step("Gen.22.6")
# ‹וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ … וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו› event:
# load-and-walk — agent avraham
m.event("load_and_walk", agent="avraham")

# -------------------------- Gen.22.7 · THE_WHERE_IS_THE_LAMB ---------------
# וַיֹּאמֶר יִצְחָק אֶל־אַבְרָהָם אָבִיו וַיֹּאמֶר אָבִי וַיֹּאמֶר הִנֶּנִּי
# בְנִי וַיֹּאמֶר הִנֵּה הָאֵשׁ וְהָעֵצִים וְאַיֵּה הַשֶּׂה לְעֹלָה
# "And Isaac spoke unto Abraham his father, and said: 'My father.' And he
# said: 'Here am I, my son.' And he said: 'Behold the fire and the wood; but
# where is the lamb for a burnt-offering?'"
m.step("Gen.22.7")
# ‹אָבִי … הִנֶּנִּי בְנִי … וְאַיֵּה הַשֶּׂה לְעֹלָה› fact holds: avi-and-
# yomer-behold-I-veni; and-ayeh-the-seh-to-burnt-offering
m.fact("avi_va_yomer_hineni_veni",
       "ve_ayeh_ha_seh_le_olah")

# -------------------------- Gen.22.8 · THE_PROVIDE_ANSWER ------------------
# וַיֹּאמֶר אַבְרָהָם אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי
# וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו
# "And Abraham said: 'God will provide Himself the lamb for a burnt-
# offering, my son.' So they went both of them together."
m.step("Gen.22.8")
# ‹אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי› fact holds: God-yireh-not-
# the-seh-to-burnt-offering-beni
m.fact("elohim_yireh_lo_ha_seh_le_olah_beni")

# -------------------------- Gen.22.9 · THE_BINDING -------------------------
# וַיָּבֹאוּ אֶל־הַמָּקוֹם אֲשֶׁר אָמַר־לוֹ הָאֱלֹהִים וַיִּבֶן שָׁם
# אַבְרָהָם אֶת־הַמִּזְבֵּחַ וַיַּעֲרֹךְ אֶת־הָעֵצִים וַיַּעֲקֹד אֶת־יִצְחָק
# בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ מִמַּעַל לָעֵצִים
# "And they came to the place which God had told him of; and Abraham built
# the altar there, and laid the wood in order, and bound Isaac his son, and
# laid him on the altar, upon the wood."
m.step("Gen.22.9")
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› event:
# bind — agent avraham; theme yitzchaq
m.event("bind", agent="avraham", themes=["yitzchaq"])
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› fact
# holds: and-yaaqod-yitzchaq-and-yasem-upon-the-altar
m.fact("va_yaaqod_et_yitzchaq_va_yasem_al_ha_mizbeach")

# -------------------------- Gen.22.10 · THE_HAND_AND_THE_KNIFE -------------
# וַיִּשְׁלַח אַבְרָהָם אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט
# אֶת־בְּנוֹ
# "And Abraham stretched forth his hand, and took the knife to slay his
# son."
m.step("Gen.22.10")
# ‹וַיִּשְׁלַח … אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט› event:
# reach-knife — agent avraham
m.event("reach_knife", agent="avraham")

# -------------------------- Gen.22.11 · THE_FIRST_DOUBLED_NAME_CALL --------
# וַיִּקְרָא אֵלָיו מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם וַיֹּאמֶר אַבְרָהָם
# אַבְרָהָם וַיֹּאמֶר הִנֵּנִי
# "And the angel of the LORD called unto him out of heaven, and said:
# 'Abraham, Abraham.' And he said: 'Here am I.'"
m.step("Gen.22.11")
# ‹מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם› the world gains: malakh-the-LORD
m.install("malakh_YHWH")
# ‹אַבְרָהָם אַבְרָהָם … הִנֵּנִי› fact holds: avraham-avraham-and-yomer-
# behold-I
m.fact("avraham_avraham_va_yomer_hineni")

# -------------------------- Gen.22.12 · THE_COUNTERMAND_AND_THE_CONFERRED_TITLE -
# וַיֹּאמֶר אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר וְאַל־תַּעַשׂ לוֹ מְאוּמָה
# כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ
# אֶת־בִּנְךָ אֶת־יְחִידְךָ מִמֶּנִּי
# "And he said: 'Lay not thy hand upon the lad, neither do thou any thing
# unto him; for now I know that thou art a God-fearing man, seeing thou hast
# not withheld thy son, thine only son, from Me.'"
m.step("Gen.22.12")
# ‹אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר› malakh-the-LORD speaks a demand — LET-
# NOT: tishlach(yadkha-to-the-naar)
m.declare("malakh_YHWH", "LET-NOT",
          "tishlach(yadkha_el_ha_naar)")
# ‹וְאַל־תַּעַשׂ לוֹ מְאוּמָה› malakh-the-LORD speaks a demand — LET-NOT:
# taas(not-meumah)
m.declare("malakh_YHWH", "LET-NOT",
          "taas(lo_meumah)")
# ‹כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ› fact
# holds: you-yadati-when-yere-God-you; and-not-chasakhta-binkha-yechidkha
m.fact("atah_yadati_ki_yere_elohim_atah",
       "ve_lo_chasakhta_et_binkha_et_yechidkha")

# -------------------------- Gen.22.13 · THE_RAM_AND_THE_CROWN_FORK ---------
# וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו וַיַּרְא וְהִנֵּה־אַיִל אַחַר נֶאֱחַז
# בַּסְּבַךְ בְּקַרְנָיו וַיֵּלֶךְ אַבְרָהָם וַיִּקַּח אֶת־הָאַיִל
# וַיַּעֲלֵהוּ לְעֹלָה תַּחַת בְּנוֹ
# "And Abraham lifted up his eyes, and looked, and behold behind him a ram
# caught in the thicket by his horns. And Abraham went and took the ram, and
# offered him up for a burnt-offering in the stead of his son."
m.step("Gen.22.13")
# ‹וְהִנֵּה־אַיִל אַחַר נֶאֱחַז בַּסְּבַךְ בְּקַרְנָיו› event: see-ram —
# agent avraham
m.event("see_ram", agent="avraham")
# ‹וַיֵּלֶךְ אַבְרָהָם וַיִּקַּח אֶת־הָאַיִל וַיַּעֲלֵהוּ לְעֹלָה תַּחַת
# בְּנוֹ› event: offer-substitute — agent avraham; theme the-ayil
m.event("offer_substitute", agent="avraham", themes=["ha_ayil"])
# ‹אַיִל … נֶאֱחַז בַּסְּבַךְ … וַיַּעֲלֵהוּ לְעֹלָה תַּחַת בְּנוֹ› fact
# holds: ayil-neechaz-in-the-sevakh-in-qarnav; and-yaalehu-to-burnt-
# offering-tachat-beno
m.fact("ayil_neechaz_ba_sevakh_be_qarnav",
       "va_yaalehu_le_olah_tachat_beno")

# -------------------------- Gen.22.14 · THE_SENTENCE_NAME_AND_THE_SAYING ---
# וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה אֲשֶׁר יֵאָמֵר
# הַיּוֹם בְּהַר יְהוָה יֵרָאֶה
# "And Abraham called the name of that place Adonai-jireh; as it is said to
# this day: 'In the mount where the LORD is seen.'"
m.step("Gen.22.14")
# ‹וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה› named: the-
# maqom := the-LORD-Yireh
m.name("ha_maqom", "YHWH_Yireh")
# ‹אֲשֶׁר יֵאָמֵר הַיּוֹם בְּהַר יְהוָה יֵרָאֶה› pattern recorded: which-
# yeamer-the-day-in-har-the-LORD-yeraeh
m.pattern("asher_yeamer_ha_yom_be_har_YHWH_yeraeh")

# -------------------------- Gen.22.15 · THE_SECOND_SKY_CALL ----------------
# וַיִּקְרָא מַלְאַךְ יְהוָה אֶל־אַבְרָהָם שֵׁנִית מִן־הַשָּׁמָיִם
# "And the angel of the LORD called unto Abraham a second time out of
# heaven,"
m.step("Gen.22.15")
# ‹וַיִּקְרָא … שֵׁנִית מִן־הַשָּׁמָיִם› event: sky-call — agent malakh-the-
# LORD
m.event("sky_call", agent="malakh_YHWH")

# -------------------------- Gen.22.16 · THE_DIVINE_SELF_OATH ---------------
# וַיֹּאמֶר בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה כִּי יַעַן אֲשֶׁר עָשִׂיתָ
# אֶת־הַדָּבָר הַזֶּה וְלֹא חָשַׂכְתָּ אֶת־בִּנְךָ אֶת־יְחִידֶךָ
# "and said: 'By Myself have I sworn, saith the LORD, because thou hast done
# this thing, and hast not withheld thy son, thine only son,"
m.step("Gen.22.16")
# ‹בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה … יַעַן אֲשֶׁר עָשִׂיתָ› fact holds: bi-
# nishbati-neum-the-LORD; yaan-which-asita-and-not-chasakhta
m.fact("bi_nishbati_neum_YHWH",
       "yaan_asher_asita_ve_lo_chasakhta")

# -------------------------- Gen.22.17 · THE_DOUBLED_BLESSINGS --------------
# כִּי־בָרֵךְ אֲבָרֶכְךָ וְהַרְבָּה אַרְבֶּה אֶת־זַרְעֲךָ כְּכוֹכְבֵי
# הַשָּׁמַיִם וְכַחוֹל אֲשֶׁר עַל־שְׂפַת הַיָּם וְיִרַשׁ זַרְעֲךָ אֵת שַׁעַר
# אֹיְבָיו
# "that in blessing I will bless thee, and in multiplying I will multiply
# thy seed as the stars of the heaven, and as the sand which is upon the
# seashore; and thy seed shall possess the gate of his enemies;"
m.step("Gen.22.17")
# ‹בָרֵךְ אֲבָרֶכְךָ וְהַרְבָּה אַרְבֶּה … כְּכוֹכְבֵי … וְכַחוֹל› fact
# holds: varekh-avarekhkha-and-greatly-I-will-multiply; like-khokhvei-and-
# kha-chol-and-yirash-shaar-oyvav
m.fact("varekh_avarekhkha_ve_harbah_arbeh",
       "ke_khokhvei_ve_kha_chol_ve_yirash_shaar_oyvav")

# -------------------------- Gen.22.18 · THE_LISTENED_VOICE_GROUND ----------
# וְהִתְבָּרְכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ עֵקֶב אֲשֶׁר שָׁמַעְתָּ
# בְּקֹלִי
# "and in thy seed shall all the nations of the earth be blessed; because
# thou hast hearkened to My voice.'"
m.step("Gen.22.18")
# ‹וְהִתְבָּרְכוּ … עֵקֶב אֲשֶׁר שָׁמַעְתָּ בְּקֹלִי› fact holds: and-
# hitbarakhu-and-zarakha-all-goyei-the-earth; ekev-which-shamata-in-qoli
m.fact("ve_hitbarakhu_ve_zarakha_kol_goyei_ha_aretz",
       "ekev_asher_shamata_be_qoli")

# -------------------------- Gen.22.19 · THE_RETURN_AND_THE_DWELL -----------
# וַיָּשָׁב אַבְרָהָם אֶל־נְעָרָיו וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו אֶל־בְּאֵר
# שָׁבַע וַיֵּשֶׁב אַבְרָהָם בִּבְאֵר שָׁבַע
# "So Abraham returned unto his young men, and they rose up and went
# together to Beer-sheba; and Abraham dwelt at Beer-sheba."
m.step("Gen.22.19")
# ‹וַיָּשָׁב … וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו … וַיֵּשֶׁב› event: return-
# dwell — agent avraham
m.event("return_dwell", agent="avraham")
# ‹אֶל־בְּאֵר שָׁבַע … בִּבְאֵר שָׁבַע› reads without prior install (flag,
# not fix): beer-seven
m.presupposed("beer_sheva")

# -------------------------- Gen.22.20-24 · THE_CODA_REPORT_THE_BRIDE_MINTED -
# וַיְהִי אַחֲרֵי הַדְּבָרִים הָאֵלֶּה וַיֻּגַּד לְאַבְרָהָם לֵאמֹר הִנֵּה
# יָלְדָה מִלְכָּה גַם־הִוא בָּנִים לְנָחוֹר אָחִיךָ … וּבְתוּאֵל יָלַד
# אֶת־רִבְקָה … וּפִילַגְשׁוֹ וּשְׁמָהּ רְאוּמָה וַתֵּלֶד גַּם־הִוא
# "And it came to pass after these things, that it was told Abraham, saying:
# 'Behold, Milcah, she also hath borne children unto thy brother Nahor: Uz
# his first-born, and Buz his brother, and Kemuel the father of Aram; and
# Chesed, and Hazo, and Pildash, and Jidlaph, and Bethuel.' And Bethuel
# begot Rebekah; these eight Milcah bore to Nahor, Abraham's brother. And
# his concubine, whose name was Reumah, she also bore Tebah, and Gaham, and
# Tahash, and Maacah."
m.step("Gen.22.20-24")
# ‹וַיֻּגַּד לְאַבְרָהָם … הִנֵּה יָלְדָה מִלְכָּה גַם־הִוא … וּבְתוּאֵל
# יָלַד אֶת־רִבְקָה› fact holds: and-yugad-to-avraham-behold-yaldah-milkah-
# also-hi; and-vetuel-yalad-rivqah
m.fact("va_yugad_le_avraham_hinneh_yaldah_milkah_gam_hi",
       "u_vetuel_yalad_et_rivqah")
# ‹שְׁמֹנָה אֵלֶּה יָלְדָה מִלְכָּה … וּפִילַגְשׁוֹ … וַתֵּלֶד גַּם־הִוא›
# fact holds: shmonah-ele-yaldah-milkah-and-filagsho-reumah-four
m.fact("shmonah_ele_yaldah_milkah_u_filagsho_reumah_arbaah")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shnei_nearav', 'malakh_YHWH', 'yitzchaq'}
    assert m.presupposed_set() == {'beer_sheva'}
    assert m.REGISTRY["names"] == {'ha_maqom': 'YHWH_Yireh'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['qach_lekh_ve_haalehu(et_binkha, le_olah)', 'shevu(po_im_ha_chamor)', 'tishlach(yadkha_el_ha_naar)', 'taas(lo_meumah)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1, 'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['achar_ha_devarim_ve_ha_elohim_nisah_et_avraham', 'va_yomer_hineni', 'et_binkha_et_yechidkha_asher_ahavta_et_yitzchaq', 'el_eretz_ha_moriyah_asher_omar_elekha', 'va_yashkem_ba_boqer_va_yachavosh_et_chamoro', 'ba_yom_ha_shelishi_va_yar_et_ha_maqom_me_rachoq', 'nelkha_ve_nishtachaveh_ve_nashuvah_aleikhem', 'avi_va_yomer_hineni_veni', 've_ayeh_ha_seh_le_olah', 'elohim_yireh_lo_ha_seh_le_olah_beni', 'va_yaaqod_et_yitzchaq_va_yasem_al_ha_mizbeach', 'avraham_avraham_va_yomer_hineni', 'atah_yadati_ki_yere_elohim_atah', 've_lo_chasakhta_et_binkha_et_yechidkha', 'ayil_neechaz_ba_sevakh_be_qarnav', 'va_yaalehu_le_olah_tachat_beno', 'pattern: asher_yeamer_ha_yom_be_har_YHWH_yeraeh', 'bi_nishbati_neum_YHWH', 'yaan_asher_asita_ve_lo_chasakhta', 'varekh_avarekhkha_ve_harbah_arbeh', 'ke_khokhvei_ve_kha_chol_ve_yirash_shaar_oyvav', 've_hitbarakhu_ve_zarakha_kol_goyei_ha_aretz', 'ekev_asher_shamata_be_qoli', 'va_yugad_le_avraham_hinneh_yaldah_milkah_gam_hi', 'u_vetuel_yalad_et_rivqah', 'shmonah_ele_yaldah_milkah_u_filagsho_reumah_arbaah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
