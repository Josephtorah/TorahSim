#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם … הִנֵּנִי› (“and-the-God test obj-
# marker Abraham … behold-me/my”) — fact holds: after-the-word/thing-and-
# the-God-nisah-obj-marker-Abraham; and-say-behold-I
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
# ‹קַח־נָא … וְלֶךְ־לְךָ … וְהַעֲלֵהוּ שָׁם לְעֹלָה› (“take please … and-go
# to-you/your … and-go-up-him/its there to-burnt-offering”) — God speaks a
# demand — LET: take-go-and-haalehu(obj-marker-binkha, to-burnt-offering)
m.declare("elohim", "LET",
          "qach_lekh_ve_haalehu(et_binkha, le_olah)")
# ‹אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק› (“obj-marker son-
# you/your obj-marker united-you/your which have-affection-for obj-marker
# Isaac”) — fact holds: obj-marker-binkha-obj-marker-yechidkha-which-have-
# affection-for-obj-marker-Isaac; to-earth-the-moriyah-which-say-to-you
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
# ‹וְאֵת יִצְחָק בְּנוֹ› (“and-obj-marker Isaac son-him/its”) — the world
# gains: Isaac
m.install("yitzchaq")
# ‹אֶת־שְׁנֵי נְעָרָיו› (“obj-marker two boy-him/its”) — the world gains:
# shnei-nearav
m.install("shnei_nearav")
# ‹וַיַּשְׁכֵּם … וַיַּחֲבֹשׁ … וַיִּקַּח … וַיְבַקַּע … וַיָּקָם וַיֵּלֶךְ›
# (“and-rise-early … and-wrap-firmly … and-take … and-cleave … and-arise
# and-go”) — event: dawn-journey — agent Abraham
m.event("dawn_journey", agent="avraham")
# ‹וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת־חֲמֹרוֹ› (“and-rise-
# early Abraham in-morning and-wrap-firmly obj-marker male-ass-him/its”) —
# fact holds: and-rise-early-in-the-morning-and-wrap-firmly-obj-marker-
# chamoro
m.fact("va_yashkem_ba_boqer_va_yachavosh_et_chamoro")

# -------------------------- Gen.22.4 · THE_THIRD_DAY_SIGHTING --------------
# בַּיּוֹם הַשְּׁלִישִׁי וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו וַיַּרְא
# אֶת־הַמָּקוֹם מֵרָחֹק
# "On the third day Abraham lifted up his eyes, and saw the place afar off."
m.step("Gen.22.4")
# ‹בַּיּוֹם הַשְּׁלִישִׁי … מֵרָחֹק› (“in-day the-third … from-remote”) —
# fact holds: in-the-day-the-third-and-see-obj-marker-the-place-from-remote
m.fact("ba_yom_ha_shelishi_va_yar_et_ha_maqom_me_rachoq")

# -------------------------- Gen.22.5 · THE_STAY_DEMAND_AND_THE_EXCLUSIVE_WE -
# וַיֹּאמֶר אַבְרָהָם אֶל־נְעָרָיו שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר וַאֲנִי
# וְהַנַּעַר נֵלְכָה עַד־כֹּה וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם
# "And Abraham said unto his young men: 'Abide ye here with the ass, and I
# and the lad will go yonder; and we will worship, and come back to you.'"
m.step("Gen.22.5")
# ‹שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר› (“dwell/sit to-you/your(pl) this-place
# with the-male-ass”) — Abraham speaks a demand — LET: dwell/sit(this-place-
# with-the-male-ass)
m.declare("avraham", "LET",
          "shevu(po_im_ha_chamor)")
# ‹נֵלְכָה … וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם› (“go … and-afflict and-
# return to-you/your(pl)”) — fact holds: go-and-nishtachaveh-and-nashuvah-
# aleikhem
m.fact("nelkha_ve_nishtachaveh_ve_nashuvah_aleikhem")

# -------------------------- Gen.22.6 · THE_LOADED_WALK_TOGETHER ------------
# וַיִּקַּח אַבְרָהָם אֶת־עֲצֵי הָעֹלָה וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ
# וַיִּקַּח בְּיָדוֹ אֶת־הָאֵשׁ וְאֶת־הַמַּאֲכֶלֶת וַיֵּלְכוּ שְׁנֵיהֶם
# יַחְדָּו
# "And Abraham took the wood of the burnt-offering, and laid it upon Isaac
# his son; and he took in his hand the fire and the knife; and they went
# both of them together."
m.step("Gen.22.6")
# ‹וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ … וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו› (“and-
# put/set over Isaac son-him/its … and-go two-them/their unit”) — event:
# load-and-walk — agent Abraham
m.event("load_and_walk", agent="avraham")

# -------------------------- Gen.22.7 · THE_WHERE_IS_THE_LAMB ---------------
# וַיֹּאמֶר יִצְחָק אֶל־אַבְרָהָם אָבִיו וַיֹּאמֶר אָבִי וַיֹּאמֶר הִנֶּנִּי
# בְנִי וַיֹּאמֶר הִנֵּה הָאֵשׁ וְהָעֵצִים וְאַיֵּה הַשֶּׂה לְעֹלָה
# "And Isaac spoke unto Abraham his father, and said: 'My father.' And he
# said: 'Here am I, my son.' And he said: 'Behold the fire and the wood; but
# where is the lamb for a burnt-offering?'"
m.step("Gen.22.7")
# ‹אָבִי … הִנֶּנִּי בְנִי … וְאַיֵּה הַשֶּׂה לְעֹלָה› (“father-me/my …
# behold-me/my son-me/my … and-where? the-member-of-a-flock to-burnt-
# offering”) — fact holds: father-and-say-behold-I-veni; and-ayeh-the-seh-
# to-burnt-offering
m.fact("avi_va_yomer_hineni_veni",
       "ve_ayeh_ha_seh_le_olah")

# -------------------------- Gen.22.8 · THE_PROVIDE_ANSWER ------------------
# וַיֹּאמֶר אַבְרָהָם אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי
# וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו
# "And Abraham said: 'God will provide Himself the lamb for a burnt-
# offering, my son.' So they went both of them together."
m.step("Gen.22.8")
# ‹אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי› (“God see to-him/its the-
# member-of-a-flock to-burnt-offering son-me/my”) — fact holds: God-yireh-
# not-the-seh-to-burnt-offering-beni
m.fact("elohim_yireh_lo_ha_seh_le_olah_beni")

# -------------------------- Gen.22.9 · THE_BINDING -------------------------
# וַיָּבֹאוּ אֶל־הַמָּקוֹם אֲשֶׁר אָמַר־לוֹ הָאֱלֹהִים וַיִּבֶן שָׁם
# אַבְרָהָם אֶת־הַמִּזְבֵּחַ וַיַּעֲרֹךְ אֶת־הָעֵצִים וַיַּעֲקֹד אֶת־יִצְחָק
# בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ מִמַּעַל לָעֵצִים
# "And they came to the place which God had told him of; and Abraham built
# the altar there, and laid the wood in order, and bound Isaac his son, and
# laid him on the altar, upon the wood."
m.step("Gen.22.9")
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› (“and-
# tie-with-thongs obj-marker Isaac son-him/its and-put/set obj-marker-
# him/its over the-altar”) — event: bind — agent Abraham; theme Isaac
m.event("bind", agent="avraham", themes=["yitzchaq"])
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› (“and-
# tie-with-thongs obj-marker Isaac son-him/its and-put/set obj-marker-
# him/its over the-altar”) — fact holds: and-tie-with-thongs-obj-marker-
# Isaac-and-put/set-over-the-altar
m.fact("va_yaaqod_et_yitzchaq_va_yasem_al_ha_mizbeach")

# -------------------------- Gen.22.10 · THE_HAND_AND_THE_KNIFE -------------
# וַיִּשְׁלַח אַבְרָהָם אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט
# אֶת־בְּנוֹ
# "And Abraham stretched forth his hand, and took the knife to slay his
# son."
m.step("Gen.22.10")
# ‹וַיִּשְׁלַח … אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט› (“and-send …
# obj-marker hand-him/its and-take obj-marker the-something-to-eat-with to-
# slaughter”) — event: reach-knife — agent Abraham
m.event("reach_knife", agent="avraham")

# -------------------------- Gen.22.11 · THE_FIRST_DOUBLED_NAME_CALL --------
# וַיִּקְרָא אֵלָיו מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם וַיֹּאמֶר אַבְרָהָם
# אַבְרָהָם וַיֹּאמֶר הִנֵּנִי
# "And the angel of the LORD called unto him out of heaven, and said:
# 'Abraham, Abraham.' And he said: 'Here am I.'"
m.step("Gen.22.11")
# ‹מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם› (“messenger YHWH from the-heavens”) —
# the world gains: messenger-the-LORD
m.install("malakh_YHWH")
# ‹אַבְרָהָם אַבְרָהָם … הִנֵּנִי› (“Abraham Abraham … behold-me/my”) — fact
# holds: Abraham-Abraham-and-say-behold-I
m.fact("avraham_avraham_va_yomer_hineni")

# -------------------------- Gen.22.12 · THE_COUNTERMAND_AND_THE_CONFERRED_TITLE -
# וַיֹּאמֶר אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר וְאַל־תַּעַשׂ לוֹ מְאוּמָה
# כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ
# אֶת־בִּנְךָ אֶת־יְחִידְךָ מִמֶּנִּי
# "And he said: 'Lay not thy hand upon the lad, neither do thou any thing
# unto him; for now I know that thou art a God-fearing man, seeing thou hast
# not withheld thy son, thine only son, from Me.'"
m.step("Gen.22.12")
# ‹אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר› (“do-not send hand-you/your to the-
# boy”) — messenger-the-LORD speaks a demand — LET-NOT: send(yadkha-to-the-
# boy)
m.declare("malakh_YHWH", "LET-NOT",
          "tishlach(yadkha_el_ha_naar)")
# ‹וְאַל־תַּעַשׂ לוֹ מְאוּמָה› (“and-do-not make to-him/its speck”) —
# messenger-the-LORD speaks a demand — LET-NOT: make(not-meumah)
m.declare("malakh_YHWH", "LET-NOT",
          "taas(lo_meumah)")
# ‹כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ›
# (“that now know that fearing God you and-not restrain”) — fact holds: you-
# know-that-fearing-God-you; and-not-restrain-obj-marker-binkha-obj-marker-
# yechidkha
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
# ‹וְהִנֵּה־אַיִל אַחַר נֶאֱחַז בַּסְּבַךְ בְּקַרְנָיו› (“and-behold ram
# after seize in-copse in-horn-him/its”) — event: see-ram — agent Abraham
m.event("see_ram", agent="avraham")
# ‹וַיֵּלֶךְ אַבְרָהָם וַיִּקַּח אֶת־הָאַיִל וַיַּעֲלֵהוּ לְעֹלָה תַּחַת
# בְּנוֹ› (“and-go Abraham and-take obj-marker the-ram and-go-up-him/its to-
# burnt-offering under son-him/its”) — event: offer-substitute — agent
# Abraham; theme the-ram
m.event("offer_substitute", agent="avraham", themes=["ha_ayil"])
# ‹אַיִל … נֶאֱחַז בַּסְּבַךְ … וַיַּעֲלֵהוּ לְעֹלָה תַּחַת בְּנוֹ› (“ram …
# seize in-copse … and-go-up-him/its to-burnt-offering under son-him/its”) —
# fact holds: ram-seize-in-the-sevakh-in-qarnav; and-yaalehu-to-burnt-
# offering-under-beno
m.fact("ayil_neechaz_ba_sevakh_be_qarnav",
       "va_yaalehu_le_olah_tachat_beno")

# -------------------------- Gen.22.14 · THE_SENTENCE_NAME_AND_THE_SAYING ---
# וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה אֲשֶׁר יֵאָמֵר
# הַיּוֹם בְּהַר יְהוָה יֵרָאֶה
# "And Abraham called the name of that place Adonai-jireh; as it is said to
# this day: 'In the mount where the LORD is seen.'"
m.step("Gen.22.14")
# ‹וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה› (“and-call
# Abraham name the-place that YHWH see”) — named: the-place := the-LORD-
# Yireh
m.name("ha_maqom", "YHWH_Yireh")
# ‹אֲשֶׁר יֵאָמֵר הַיּוֹם בְּהַר יְהוָה יֵרָאֶה› (“which say the-day in-
# mountain YHWH see”) — pattern recorded: which-say-the-day-in-mountain-the-
# LORD-yeraeh
m.pattern("asher_yeamer_ha_yom_be_har_YHWH_yeraeh")

# -------------------------- Gen.22.15 · THE_SECOND_SKY_CALL ----------------
# וַיִּקְרָא מַלְאַךְ יְהוָה אֶל־אַבְרָהָם שֵׁנִית מִן־הַשָּׁמָיִם
# "And the angel of the LORD called unto Abraham a second time out of
# heaven,"
m.step("Gen.22.15")
# ‹וַיִּקְרָא … שֵׁנִית מִן־הַשָּׁמָיִם› (“and-call … second from the-
# heavens”) — event: sky-call — agent messenger-the-LORD
m.event("sky_call", agent="malakh_YHWH")

# -------------------------- Gen.22.16 · THE_DIVINE_SELF_OATH ---------------
# וַיֹּאמֶר בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה כִּי יַעַן אֲשֶׁר עָשִׂיתָ
# אֶת־הַדָּבָר הַזֶּה וְלֹא חָשַׂכְתָּ אֶת־בִּנְךָ אֶת־יְחִידֶךָ
# "and said: 'By Myself have I sworn, saith the LORD, because thou hast done
# this thing, and hast not withheld thy son, thine only son,"
m.step("Gen.22.16")
# ‹בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה … יַעַן אֲשֶׁר עָשִׂיתָ› (“in-me/my
# swear oracle YHWH … heed which make”) — fact holds: bi-swear-oracle-the-
# LORD; heed-which-make-and-not-restrain
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
# ‹בָרֵךְ אֲבָרֶכְךָ וְהַרְבָּה אַרְבֶּה … כְּכוֹכְבֵי … וְכַחוֹל› (“bless
# bless-you/your and-multiply multiply … like-stars … and-like-sand”) — fact
# holds: bless-avarekhkha-and-greatly-I-will-multiply; like-khokhvei-and-
# you/your-chol-and-possess/inherit-gate-oyvav
m.fact("varekh_avarekhkha_ve_harbah_arbeh",
       "ke_khokhvei_ve_kha_chol_ve_yirash_shaar_oyvav")

# -------------------------- Gen.22.18 · THE_LISTENED_VOICE_GROUND ----------
# וְהִתְבָּרְכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ עֵקֶב אֲשֶׁר שָׁמַעְתָּ
# בְּקֹלִי
# "and in thy seed shall all the nations of the earth be blessed; because
# thou hast hearkened to My voice.'"
m.step("Gen.22.18")
# ‹וְהִתְבָּרְכוּ … עֵקֶב אֲשֶׁר שָׁמַעְתָּ בְּקֹלִי› (“and-bless … heel
# which hear in-voice/sound-me/my”) — fact holds: and-bless-and-zarakha-all-
# goyei-the-earth; ekev-which-hear-in-qoli
m.fact("ve_hitbarakhu_ve_zarakha_kol_goyei_ha_aretz",
       "ekev_asher_shamata_be_qoli")

# -------------------------- Gen.22.19 · THE_RETURN_AND_THE_DWELL -----------
# וַיָּשָׁב אַבְרָהָם אֶל־נְעָרָיו וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו אֶל־בְּאֵר
# שָׁבַע וַיֵּשֶׁב אַבְרָהָם בִּבְאֵר שָׁבַע
# "So Abraham returned unto his young men, and they rose up and went
# together to Beer-sheba; and Abraham dwelt at Beer-sheba."
m.step("Gen.22.19")
# ‹וַיָּשָׁב … וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו … וַיֵּשֶׁב› (“and-return …
# and-arise and-go unit … and-return”) — event: return-dwell — agent Abraham
m.event("return_dwell", agent="avraham")
# ‹אֶל־בְּאֵר שָׁבַע … בִּבְאֵר שָׁבַע› (“to Beer-shebah … in Beer-shebah”)
# — reads without prior install (flag, not fix): beer-seven
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
# יָלַד אֶת־רִבְקָה› (“and-tell to-Abraham … behold bear-young Milcah also
# he/it … and-Bethuel bear-young obj-marker Rebekah”) — fact holds: and-
# tell-to-Abraham-behold-yaldah-milkah-also-hi; and-Bethuel-bear-young-obj-
# marker-rivqah
m.fact("va_yugad_le_avraham_hinneh_yaldah_milkah_gam_hi",
       "u_vetuel_yalad_et_rivqah")
# ‹שְׁמֹנָה אֵלֶּה יָלְדָה מִלְכָּה … וּפִילַגְשׁוֹ … וַתֵּלֶד גַּם־הִוא›
# (“number these bear-young Milcah … and-concubine-him/its … and-bear-young
# also he/it”) — fact holds: shmonah-these-yaldah-milkah-and-filagsho-
# reumah-four
m.fact("shmonah_ele_yaldah_milkah_u_filagsho_reumah_arbaah")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'yitzchaq', 'shnei_nearav', 'malakh_YHWH'}
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
