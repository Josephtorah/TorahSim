#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_37_laughter_wilderness_oath — 21:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_37_laughter_wilderness_oath.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The visitation, the expulsion, the well-oath (21:1-34)"""
from machine import Machine

m = Machine("gen_37_laughter_wilderness_oath")

# -------------------------- Gen.21.1 · THE_VISITATION_PAYS_TWICE -----------
# וַיהוָה פָּקַד אֶת־שָׂרָה כַּאֲשֶׁר אָמָר וַיַּעַשׂ יְהוָה לְשָׂרָה
# כַּאֲשֶׁר דִּבֵּר
# "And the LORD remembered Sarah as He had said, and the LORD did unto Sarah
# as He had spoken."
m.step("Gen.21.1")
# ‹פָּקַד … כַּאֲשֶׁר אָמָר … כַּאֲשֶׁר דִּבֵּר› (“count/visit … like-
# as/which say … like-as/which speak”) — fact holds: count/visit-like-which-
# say-and-make-like-which-speak
m.fact("paqad_ka_asher_amar_va_yaas_ka_asher_diber")

# -------------------------- Gen.21.2 · THE_BIRTH_AT_THE_APPOINTED_TIME -----
# וַתַּהַר וַתֵּלֶד שָׂרָה לְאַבְרָהָם בֵּן לִזְקֻנָיו לַמּוֹעֵד
# אֲשֶׁר־דִּבֶּר אֹתוֹ אֱלֹהִים
# "And Sarah conceived, and bore Abraham a son in his old age, at the set
# time of which God had spoken to him."
m.step("Gen.21.2")
# ‹וַתֵּלֶד שָׂרָה לְאַבְרָהָם בֵּן› (“and-bear-young Sarah to-Abraham son”)
# — the world gains: Isaac
m.install("yitzchaq")
# ‹בֵּן לִזְקֻנָיו לַמּוֹעֵד אֲשֶׁר־דִּבֶּר› (“son to-old-age-him/its to-
# seasons which speak”) — fact holds: son-to-me-zequnayv; to-seasons-which-
# speak-God
m.fact("ben_li_zequnayv",
       "la_moed_asher_diber_elohim")

# -------------------------- Gen.21.3 · THE_DECREE_EXECUTED_IN_FORMULA ------
# וַיִּקְרָא אַבְרָהָם אֶת־שֶׁם־בְּנוֹ הַנּוֹלַד־לוֹ אֲשֶׁר־יָלְדָה־לּוֹ
# שָׂרָה יִצְחָק
# "And Abraham called the name of his son that was born unto him, whom Sarah
# bore to him, Isaac."
m.step("Gen.21.3")
# ‹וַיִּקְרָא אַבְרָהָם אֶת־שֶׁם־בְּנוֹ … יִצְחָק› (“and-call Abraham obj-
# marker name son-him/its … Isaac”) — named: Isaac := Yitzchaq
m.name("yitzchaq", "Yitzchaq")

# -------------------------- Gen.21.4 · THE_LAWS_SECOND_CASE_EXECUTES -------
# וַיָּמָל אַבְרָהָם אֶת־יִצְחָק בְּנוֹ בֶּן־שְׁמֹנַת יָמִים כַּאֲשֶׁר
# צִוָּה אֹתוֹ אֱלֹהִים
# "And Abraham circumcised his son Isaac when he was eight days old, as God
# had commanded him."
m.step("Gen.21.4")
# ‹וַיָּמָל אַבְרָהָם אֶת־יִצְחָק … כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› (“and-
# circumcise Abraham obj-marker Isaac … like-as/which command obj-marker-
# him/its God”) — event: circumcise — agent Abraham; theme Isaac
m.event("circumcise", agent="avraham", themes=["yitzchaq"])
# ‹כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› (“like-as/which command obj-marker-
# him/its God”) — fact holds: like-which-command-it-God
m.fact("ka_asher_tziva_oto_elohim")

# -------------------------- Gen.21.5 · THE_HUNDRED_YEAR_FRAME --------------
# וְאַבְרָהָם בֶּן־מְאַת שָׁנָה בְּהִוָּלֶד לוֹ אֵת יִצְחָק בְּנוֹ
# "And Abraham was a hundred years old, when his son Isaac was born unto
# him."
m.step("Gen.21.5")
# ‹בֶּן־מְאַת שָׁנָה› (“son hundred years”) — fact holds: son-hundred-year
m.fact("ben_meat_shanah")

# -------------------------- Gen.21.6 · THE_LAUGHTER_MADE_AND_CONJUGATED ----
# וַתֹּאמֶר שָׂרָה צְחֹק עָשָׂה לִי אֱלֹהִים כָּל־הַשֹּׁמֵעַ יִצְחַק־לִי
# "And Sarah said: 'God hath made laughter for me; every one that heareth
# will laugh on account of me.'"
m.step("Gen.21.6")
# ‹צְחֹק עָשָׂה לִי אֱלֹהִים כָּל־הַשֹּׁמֵעַ יִצְחַק־לִי› (“laughter make
# to-me/my God all the-hear laugh-outright to-me/my”) — fact holds:
# laughter-make-to-me-God-all-the-hear-Isaac-to-me
m.fact("tzechoq_asah_li_elohim_kol_ha_shomea_yitzchaq_li")

# -------------------------- Gen.21.7 · THE_WHO_WOULD_HAVE_SAID -------------
# וַתֹּאמֶר מִי מִלֵּל לְאַבְרָהָם הֵינִיקָה בָנִים שָׂרָה כִּי־יָלַדְתִּי
# בֵן לִזְקֻנָיו
# "And she said: 'Who would have said unto Abraham, that Sarah should give
# children suck? for I have borne him a son in his old age.'"
m.step("Gen.21.7")
# ‹מִי מִלֵּל לְאַבְרָהָם› (“who? speak to-Abraham”) — fact holds:
# who?-speak-to-Abraham-heniqah-son-sarah
m.fact("mi_milel_le_avraham_heniqah_vanim_sarah")

# -------------------------- Gen.21.8 · THE_WEANING_FEAST -------------------
# וַיִּגְדַּל הַיֶּלֶד וַיִּגָּמַל וַיַּעַשׂ אַבְרָהָם מִשְׁתֶּה גָדוֹל
# בְּיוֹם הִגָּמֵל אֶת־יִצְחָק
# "And the child grew, and was weaned. And Abraham made a great feast on the
# day that Isaac was weaned."
m.step("Gen.21.8")
# ‹וַיַּעַשׂ אַבְרָהָם מִשְׁתֶּה גָדוֹל› (“and-make Abraham drink great”) —
# event: feast — agent Abraham; theme Isaac
m.event("feast", agent="avraham", themes=["yitzchaq"])

# -------------------------- Gen.21.9 · THE_MOCKING_SEEN --------------------
# וַתֵּרֶא שָׂרָה אֶת־בֶּן־הָגָר הַמִּצְרִית אֲשֶׁר־יָלְדָה לְאַבְרָהָם
# מְצַחֵק
# "And Sarah saw the son of Hagar the Egyptian, whom she had borne unto
# Abraham, making sport."
m.step("Gen.21.9")
# ‹הָגָר הַמִּצְרִית› (“Hagar the-Egyptian”) — the world gains: Hagar
m.install("hagar")
# ‹בֶּן־הָגָר› (“son Hagar”) — the world gains: the-boy
m.install("ha_naar")
# ‹וַתֵּרֶא שָׂרָה … מְצַחֵק› (“and-see Sarah … laugh-outright”) — event:
# see — agent sarah; theme the-boy
m.event("see", agent="sarah", themes=["ha_naar"])

# -------------------------- Gen.21.10 · THE_EXPULSION_DEMAND ---------------
# וַתֹּאמֶר לְאַבְרָהָם גָּרֵשׁ הָאָמָה הַזֹּאת וְאֶת־בְּנָהּ כִּי לֹא
# יִירַשׁ בֶּן־הָאָמָה הַזֹּאת עִם־בְּנִי עִם־יִצְחָק
# "Wherefore she said unto Abraham: 'Cast out this bondwoman and her son;
# for the son of this bondwoman shall not be heir with my son, even with
# Isaac.'"
m.step("Gen.21.10")
# ‹גָּרֵשׁ הָאָמָה הַזֹּאת וְאֶת־בְּנָהּ› (“drive-out-from-a-possession the-
# maidservant the-this and-obj-marker son-her/its”) — sarah speaks a demand
# — LET: drive-out-from-a-possession(the-cubit-and-obj-marker-benah)
m.declare("sarah", "LET",
          "garesh(ha_amah_ve_et_benah)")
# ‹כִּי לֹא יִירַשׁ בֶּן־הָאָמָה הַזֹּאת עִם־בְּנִי עִם־יִצְחָק› (“that not
# possess/inherit son the-maidservant the-this with son-me/my with Isaac”) —
# fact holds: not-possess/inherit-son-the-cubit-with-beni-with-Isaac
m.fact("lo_yirash_ben_ha_amah_im_beni_im_yitzchaq")

# -------------------------- Gen.21.11 · THE_EVIL_IN_THE_FATHERS_EYES -------
# וַיֵּרַע הַדָּבָר מְאֹד בְּעֵינֵי אַבְרָהָם עַל אוֹדֹת בְּנוֹ
# "And the thing was very grievous in Abraham's sight on account of his
# son."
m.step("Gen.21.11")
# ‹וַיֵּרַע הַדָּבָר מְאֹד בְּעֵינֵי אַבְרָהָם› (“and-spoil the-word/thing
# very in-eye Abraham”) — fact holds: and-spoil-the-word/thing-very-in-eyes-
# of-Abraham
m.fact("va_yera_ha_davar_meod_be_einei_avraham")

# -------------------------- Gen.21.12 · THE_ARBITRATION_IN_THREE_MOODS -----
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם אַל־יֵרַע בְּעֵינֶיךָ עַל־הַנַּעַר
# וְעַל־אֲמָתֶךָ כֹּל אֲשֶׁר תֹּאמַר אֵלֶיךָ שָׂרָה שְׁמַע בְּקֹלָהּ כִּי
# בְיִצְחָק יִקָּרֵא לְךָ זָרַע
# "And God said unto Abraham: 'Let it not be grievous in thy sight because
# of the lad, and because of thy bondwoman; in all that Sarah saith unto
# thee, hearken unto her voice; for in Isaac shall seed be called to thee."
m.step("Gen.21.12")
# ‹אַל־יֵרַע בְּעֵינֶיךָ› (“do-not spoil in-eye-you/your”) — God speaks a
# demand — LET-NOT: spoil(in-einekha)
m.declare("elohim", "LET-NOT",
          "yera(be_einekha)")
# ‹כֹּל אֲשֶׁר תֹּאמַר אֵלֶיךָ שָׂרָה שְׁמַע בְּקֹלָהּ› (“all which say to-
# you/your Sarah hear in-voice/sound-her/its”) — God speaks a demand — LET:
# hear(in-voice/sound-sarah)
m.declare("elohim", "LET",
          "shema(be_qol_sarah)")
# ‹כִּי בְיִצְחָק יִקָּרֵא לְךָ זָרַע› (“that in-Isaac call to-you/your
# seed”) — fact holds: that-and-Isaac-call-to-you-seed
m.fact("ki_ve_yitzchaq_yiqare_lekha_zara")

# -------------------------- Gen.21.13 · THE_OTHER_NATION_PROMISE -----------
# וְגַם אֶת־בֶּן־הָאָמָה לְגוֹי אֲשִׂימֶנּוּ כִּי זַרְעֲךָ הוּא
# "And also of the son of the bondwoman will I make a nation, because he is
# thy seed.'"
m.step("Gen.21.13")
# ‹לְגוֹי אֲשִׂימֶנּוּ כִּי זַרְעֲךָ הוּא› (“to-nation put/set-him/its that
# seed-you/your he/it”) — fact holds: to-nation-asimenu-that-zarakha-he/it
m.fact("le_goy_asimenu_ki_zarakha_hu")

# -------------------------- Gen.21.14 · THE_DAWN_COMPLIANCE_IN_OTHER_VERBS -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיִּקַּח־לֶחֶם וְחֵמַת מַיִם וַיִּתֵּן
# אֶל־הָגָר שָׂם עַל־שִׁכְמָהּ וְאֶת־הַיֶּלֶד וַיְשַׁלְּחֶהָ וַתֵּלֶךְ
# וַתֵּתַע בְּמִדְבַּר בְּאֵר שָׁבַע
# "And Abraham arose up early in the morning, and took bread and a bottle of
# water, and gave it unto Hagar, putting it on her shoulder, and the child,
# and sent her away; and she departed, and strayed in the wilderness of
# Beer-sheba."
m.step("Gen.21.14")
# ‹וַיַּשְׁכֵּם … וַיִּקַּח … וַיִּתֵּן … וַיְשַׁלְּחֶהָ› (“and-rise-early …
# and-take … and-set … and-send-her/its”) — event: send-away — agent
# Abraham; theme Hagar
m.event("send_away", agent="avraham", themes=["hagar"])
# ‹וַיְשַׁלְּחֶהָ … וַתֵּתַע› (“and-send-her/its … and-vacillate”) — fact
# holds: and-rise-early-and-yeshalcheha-and-vacillate
m.fact("va_yashkem_va_yeshalcheha_va_teta")
# ‹בְּמִדְבַּר בְּאֵר שָׁבַע› (“in-pasture Beer-shebah”) — reads without
# prior install (flag, not fix): pit-seven
m.presupposed("beer_sheva")

# -------------------------- Gen.21.15 · THE_SPENT_SKIN_AND_THE_CAST_CHILD --
# וַיִּכְלוּ הַמַּיִם מִן־הַחֵמֶת וַתַּשְׁלֵךְ אֶת־הַיֶּלֶד תַּחַת אַחַד
# הַשִּׂיחִם
# "And the water in the bottle was spent, and she cast the child under one
# of the shrubs."
m.step("Gen.21.15")
# ‹וַתַּשְׁלֵךְ אֶת־הַיֶּלֶד› (“and-throw-out obj-marker the-child”) —
# event: cast — agent Hagar; theme the-boy
m.event("cast", agent="hagar", themes=["ha_naar"])

# -------------------------- Gen.21.16 · THE_BOWSHOT_AND_THE_WEEPING --------
# וַתֵּלֶךְ וַתֵּשֶׁב לָהּ מִנֶּגֶד הַרְחֵק כִּמְטַחֲוֵי קֶשֶׁת כִּי אָמְרָה
# אַל־אֶרְאֶה בְּמוֹת הַיָּלֶד וַתֵּשֶׁב מִנֶּגֶד וַתִּשָּׂא אֶת־קֹלָהּ
# וַתֵּבְךְּ
# "And she went, and sat her down over against him a good way off, as it
# were a bow-shot; for she said: 'Let me not look upon the death of the
# child.' And she sat over against him, and lifted up her voice, and wept."
m.step("Gen.21.16")
# ‹אַל־אֶרְאֶה בְּמוֹת הַיָּלֶד› (“do-not see in-death the-child”) — fact
# holds: over-ereh-in-death-the-child
m.fact("al_ereh_be_mot_ha_yaled")
# ‹וַתִּשָּׂא אֶת־קֹלָהּ וַתֵּבְךְּ› (“and-lift/carry obj-marker
# voice/sound-her/its and-weep”) — event: weep — agent Hagar
m.event("weep", agent="hagar")

# -------------------------- Gen.21.17 · THE_SKY_CALL_AND_THE_HEARD_NAME ----
# וַיִּשְׁמַע אֱלֹהִים אֶת־קוֹל הַנַּעַר וַיִּקְרָא מַלְאַךְ אֱלֹהִים
# אֶל־הָגָר מִן־הַשָּׁמַיִם וַיֹּאמֶר לָהּ מַה־לָּךְ הָגָר אַל־תִּירְאִי
# כִּי־שָׁמַע אֱלֹהִים אֶל־קוֹל הַנַּעַר בַּאֲשֶׁר הוּא־שָׁם
# "And God heard the voice of the lad; and the angel of God called to Hagar
# out of heaven, and said unto her: 'What aileth thee, Hagar? fear not; for
# God hath heard the voice of the lad where he is."
m.step("Gen.21.17")
# ‹מַלְאַךְ אֱלֹהִים … מִן־הַשָּׁמַיִם› (“messenger God … from the-heavens”)
# — the world gains: messenger-God
m.install("malakh_elohim")
# ‹אַל־תִּירְאִי› (“do-not fear”) — messenger-God speaks a demand — LET-NOT:
# fear(Hagar)
m.declare("malakh_elohim", "LET-NOT",
          "tiri(hagar)")
# ‹כִּי־שָׁמַע אֱלֹהִים אֶל־קוֹל הַנַּעַר בַּאֲשֶׁר הוּא־שָׁם› (“that hear
# God to voice/sound the-boy in-who he/it there”) — fact holds: hear-God-to-
# voice/sound-the-boy-in-the-which-he/it-there
m.fact("shama_elohim_el_qol_ha_naar_ba_asher_hu_sham")

# -------------------------- Gen.21.18 · THE_COMPOUND_TRIPLE_THIRD_TOKEN ----
# קוּמִי שְׂאִי אֶת־הַנַּעַר וְהַחֲזִיקִי אֶת־יָדֵךְ בּוֹ כִּי־לְגוֹי
# גָּדוֹל אֲשִׂימֶנּוּ
# "Arise, lift up the lad, and hold him fast by thy hand; for I will make
# him a great nation.'"
m.step("Gen.21.18")
# ‹קוּמִי שְׂאִי אֶת־הַנַּעַר וְהַחֲזִיקִי אֶת־יָדֵךְ בּוֹ› (“arise
# lift/carry obj-marker the-boy and-fasten-upon obj-marker hand-you/your in-
# him/its”) — messenger-God speaks a demand — LET: arise-lift/carry-and-
# fasten-upon(obj-marker-the-boy)
m.declare("malakh_elohim", "LET",
          "qumi_sei_ve_hachaziqi(et_ha_naar)")
# ‹כִּי־לְגוֹי גָּדוֹל אֲשִׂימֶנּוּ› (“that to-nation great put/set-
# him/its”) — fact holds: that-to-nation-great-asimenu
m.fact("ki_le_goy_gadol_asimenu")

# -------------------------- Gen.21.19 · THE_EYES_OPENED_AT_THE_WELL --------
# וַיִּפְקַח אֱלֹהִים אֶת־עֵינֶיהָ וַתֵּרֶא בְּאֵר מָיִם וַתֵּלֶךְ
# וַתְּמַלֵּא אֶת־הַחֵמֶת מַיִם וַתַּשְׁקְ אֶת־הַנָּעַר
# "And God opened her eyes, and she saw a well of water; and she went, and
# filled the bottle with water, and gave the lad drink."
m.step("Gen.21.19")
# ‹וַיִּפְקַח אֱלֹהִים אֶת־עֵינֶיהָ› (“and-open God obj-marker eye-her/its”)
# — event: open-eyes — agent God
m.event("open_eyes", agent="elohim")
# ‹וַתְּמַלֵּא אֶת־הַחֵמֶת מַיִם וַתַּשְׁקְ אֶת־הַנָּעַר› (“and-fill obj-
# marker the-skin-bottle waters and-give-drink obj-marker the-boy”) — event:
# water — agent Hagar
m.event("water", agent="hagar")

# -------------------------- Gen.21.20 · GOD_WITH_THE_LAD -------------------
# וַיְהִי אֱלֹהִים אֶת־הַנַּעַר וַיִּגְדָּל וַיֵּשֶׁב בַּמִּדְבָּר וַיְהִי
# רֹבֶה קַשָּׁת
# "And God was with the lad, and he grew; and he dwelt in the wilderness,
# and became an archer."
m.step("Gen.21.20")
# ‹וַיְהִי אֱלֹהִים אֶת־הַנַּעַר וַיִּגְדָּל› (“and-be God with the-boy and-
# be-large”) — fact holds: God-obj-marker-the-boy-and-be-large
m.fact("elohim_et_ha_naar_va_yigdal")

# -------------------------- Gen.21.21 · PARAN_AND_THE_EGYPTIAN_WIFE --------
# וַיֵּשֶׁב בְּמִדְבַּר פָּארָן וַתִּקַּח־לוֹ אִמּוֹ אִשָּׁה מֵאֶרֶץ
# מִצְרָיִם
# "And he dwelt in the wilderness of Paran; and his mother took him a wife
# out of the land of Egypt."
m.step("Gen.21.21")
# ‹וַתִּקַּח־לוֹ אִמּוֹ אִשָּׁה› (“and-take to-him/its mother-him/its
# woman”) — event: take-wife — agent Hagar
m.event("take_wife", agent="hagar")
# ‹בְּמִדְבַּר פָּארָן … מֵאֶרֶץ מִצְרָיִם› (“in-pasture Paran … from-earth
# Egypt”) — reads without prior install (flag, not fix): Paran, Egypt
m.presupposed("paran", "mitzrayim")

# -------------------------- Gen.21.22-24 · THE_PACT_OPENING_DEMAND_AND_COMMITMENT -
# וַיְהִי בָּעֵת הַהִוא וַיֹּאמֶר אֲבִימֶלֶךְ וּפִיכֹל שַׂר־צְבָאוֹ
# אֶל־אַבְרָהָם לֵאמֹר אֱלֹהִים עִמְּךָ בְּכֹל אֲשֶׁר־אַתָּה עֹשֶׂה …
# וְעַתָּה הִשָּׁבְעָה לִּי בֵאלֹהִים הֵנָּה … וַיֹּאמֶר אַבְרָהָם אָנֹכִי
# אִשָּׁבֵעַ
# "And it came to pass at that time, that Abimelech and Phicol the captain
# of his host spoke unto Abraham, saying: 'God is with thee in all that thou
# doest. Now therefore swear unto me here by God that thou wilt not deal
# falsely with me, nor with my son, nor with my son's son; but according to
# the kindness that I have done unto thee, thou shalt do unto me, and to the
# land wherein thou hast sojourned.' And Abraham said: 'I will swear.'"
m.step("Gen.21.22-24")
# ‹אֲבִימֶלֶךְ› (“Abimelech”) — the world gains: Abimelech
m.install("avimelekh")
# ‹וּפִיכֹל שַׂר־צְבָאוֹ› (“and-Phichol officer host-him/its”) — the world
# gains: Phichol
m.install("fikhol")
# ‹אֱלֹהִים עִמְּךָ בְּכֹל אֲשֶׁר־אַתָּה עֹשֶׂה … כַּחֶסֶד אֲשֶׁר־עָשִׂיתִי
# עִמְּךָ› (“God with-you/your in-all which you make … like-kindness which
# make with-you/your”) — fact holds: God-imkha-in-all-which-you-oseh; like-
# chesed-which-make-imkha
m.fact("elohim_imkha_be_khol_asher_atah_oseh",
       "ka_chesed_asher_asiti_imkha")
# ‹וְעַתָּה הִשָּׁבְעָה לִּי בֵאלֹהִים הֵנָּה› (“and-now swear-ward to-me/my
# in-God hither”) — Abimelech speaks a demand — LET: hishava(to-me-and-God)
m.declare("avimelekh", "LET",
          "hishava(li_ve_elohim)")
# ‹אָנֹכִי אִשָּׁבֵעַ› (“swear”) — fact holds: anokhi-swear
m.fact("anokhi_ishavea")

# -------------------------- Gen.21.25 · THE_REPROOF_OVER_THE_STOLEN_WELL ---
# וְהוֹכִחַ אַבְרָהָם אֶת־אֲבִימֶלֶךְ עַל־אֹדוֹת בְּאֵר הַמַּיִם אֲשֶׁר
# גָּזְלוּ עַבְדֵי אֲבִימֶלֶךְ
# "And Abraham reproved Abimelech because of the well of water, which
# Abimelech's servants had violently taken away."
m.step("Gen.21.25")
# ‹וְהוֹכִחַ אַבְרָהָם אֶת־אֲבִימֶלֶךְ› (“and-be-right Abraham obj-marker
# Abimelech”) — event: reprove — agent Abraham; theme Abimelech
m.event("reprove", agent="avraham", themes=["avimelekh"])

# -------------------------- Gen.21.26 · THE_TRIPLE_DENIAL ------------------
# וַיֹּאמֶר אֲבִימֶלֶךְ לֹא יָדַעְתִּי מִי עָשָׂה אֶת־הַדָּבָר הַזֶּה
# וְגַם־אַתָּה לֹא־הִגַּדְתָּ לִּי וְגַם אָנֹכִי לֹא שָׁמַעְתִּי בִּלְתִּי
# הַיּוֹם
# "And Abimelech said: 'I know not who hath done this thing; neither didst
# thou tell me, neither yet heard I of it, but to-day.'"
m.step("Gen.21.26")
# ‹לֹא יָדַעְתִּי … לֹא־הִגַּדְתָּ … לֹא שָׁמַעְתִּי› (“not know … not tell
# … not hear”) — fact holds: not-know-not-tell-not-hear-failure-of-the-day
m.fact("lo_yadati_lo_higadta_lo_shamati_bilti_ha_yom")

# -------------------------- Gen.21.27 · THE_FIRST_HUMAN_HUMAN_CUT ----------
# וַיִּקַּח אַבְרָהָם צֹאן וּבָקָר וַיִּתֵּן לַאֲבִימֶלֶךְ וַיִּכְרְתוּ
# שְׁנֵיהֶם בְּרִית
# "And Abraham took sheep and oxen, and gave them unto Abimelech; and they
# two made a covenant."
m.step("Gen.21.27")
# ‹וַיִּכְרְתוּ שְׁנֵיהֶם בְּרִית› (“and-cut two-them/their covenant”) —
# event: cut-covenant — agent Abraham
m.event("cut_covenant", agent="avraham")

# -------------------------- Gen.21.28-31 · THE_SEVEN_EWES_AND_THE_NAMING_REPORT -
# וַיַּצֵּב אַבְרָהָם אֶת־שֶׁבַע כִּבְשֹׂת הַצֹּאן לְבַדְּהֶן … מָה הֵנָּה
# שֶׁבַע כְּבָשֹׂת … כִּי אֶת־שֶׁבַע כְּבָשֹׂת תִּקַּח מִיָּדִי בַּעֲבוּר
# תִּהְיֶה־לִּי לְעֵדָה כִּי חָפַרְתִּי אֶת־הַבְּאֵר הַזֹּאת עַל־כֵּן קָרָא
# לַמָּקוֹם הַהוּא בְּאֵר שָׁבַע כִּי שָׁם נִשְׁבְּעוּ שְׁנֵיהֶם
# "And Abraham set seven ewe-lambs of the flock by themselves. And Abimelech
# said unto Abraham: 'What mean these seven ewe-lambs which thou hast set by
# themselves?' And he said: 'Verily, these seven ewe-lambs shalt thou take
# of my hand, that it may be a witness unto me, that I have digged this
# well.' Wherefore that place was called Beer-sheba; because there they
# swore both of them."
m.step("Gen.21.28-31")
# ‹וַיַּצֵּב אַבְרָהָם אֶת־שֶׁבַע כִּבְשֹׂת הַצֹּאן לְבַדְּהֶן› (“and-stand
# Abraham obj-marker seven ewe the-flock to-separation-them/their”) — event:
# station — agent Abraham; theme seven-ewe
m.event("station", agent="avraham", themes=["sheva_kivsot"])
# ‹תִּקַּח מִיָּדִי בַּעֲבוּר תִּהְיֶה־לִּי לְעֵדָה כִּי חָפַרְתִּי
# אֶת־הַבְּאֵר› (“take from-hand-me/my for-the-sake-of be to-me/my to-
# testimony that dig obj-marker the-pit”) — fact holds: seven-khevasot-take-
# who?-yadi-to-edah; that-dig-obj-marker-the-pit
m.fact("sheva_khevasot_tiqach_mi_yadi_le_edah",
       "ki_chafarti_et_ha_beer")
# ‹כִּי שָׁם נִשְׁבְּעוּ שְׁנֵיהֶם› (“that there swear two-them/their”) —
# demand settled (popped from the queue): hishava(to-me-and-God)
m.result("hishava(li_ve_elohim)", tmark="t1")
# ‹עַל־כֵּן קָרָא לַמָּקוֹם הַהוּא בְּאֵר שָׁבַע› (“over so call to-place
# that Beer-shebah”) — pattern recorded: over-so-call-to-place-pit-Beer-
# shebah
m.pattern("al_ken_qara_la_maqom_beer_shava")

# -------------------------- Gen.21.32 · THE_SECOND_CUT_AND_THE_RETURN ------
# וַיִּכְרְתוּ בְרִית בִּבְאֵר שָׁבַע וַיָּקָם אֲבִימֶלֶךְ וּפִיכֹל
# שַׂר־צְבָאוֹ וַיָּשֻׁבוּ אֶל־אֶרֶץ פְּלִשְׁתִּים
# "So they made a covenant at Beer-sheba; and Abimelech rose up, and Phicol
# the captain of his host, and they returned into the land of the
# Philistines."
m.step("Gen.21.32")
# ‹וַיִּכְרְתוּ בְרִית בִּבְאֵר שָׁבַע› (“and-cut covenant in Beer-shebah”)
# — event: cut-covenant — agent Abimelech
m.event("cut_covenant", agent="avimelekh")
# ‹אֶל־אֶרֶץ פְּלִשְׁתִּים› (“to earth Pelishtite”) — reads without prior
# install (flag, not fix): earth-Pelishtite
m.presupposed("eretz_pelishtim")

# -------------------------- Gen.21.33 · THE_TAMARISK_AND_THE_EVERLASTING_NAME -
# וַיִּטַּע אֶשֶׁל בִּבְאֵר שָׁבַע וַיִּקְרָא־שָׁם בְּשֵׁם יְהוָה אֵל עוֹלָם
# "And Abraham planted a tamarisk-tree in Beer-sheba, and called there on
# the name of the LORD, the Everlasting God."
m.step("Gen.21.33")
# ‹וַיִּטַּע אֶשֶׁל … וַיִּקְרָא־שָׁם בְּשֵׁם יְהוָה› (“and-strike-in
# tamarisk-tree … and-call there in-name YHWH”) — event: plant-and-call —
# agent Abraham
m.event("plant_and_call", agent="avraham")
# ‹אֵל עוֹלָם› (“strength forever”) — fact holds: and-call-in-name-the-LORD-
# to-forever
m.fact("va_yiqra_be_shem_YHWH_el_olam")

# -------------------------- Gen.21.34 · THE_LONG_SOJOURN_CODA --------------
# וַיָּגָר אַבְרָהָם בְּאֶרֶץ פְּלִשְׁתִּים יָמִים רַבִּים
# "And Abraham sojourned in the land of the Philistines many days."
m.step("Gen.21.34")
# ‹וַיָּגָר אַבְרָהָם בְּאֶרֶץ פְּלִשְׁתִּים יָמִים רַבִּים› (“and-turn-
# aside-from-the-road Abraham in-earth Pelishtite day many/great”) — fact
# holds: and-turn-aside-from-the-road-in-earth-Pelishtite-day-many/great
m.fact("va_yagar_be_eretz_pelishtim_yamim_rabim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'avimelekh', 'fikhol', 'ha_naar', 'hagar', 'malakh_elohim', 'yitzchaq'}
    assert m.presupposed_set() == {'beer_sheva', 'eretz_pelishtim', 'mitzrayim', 'paran'}
    assert m.REGISTRY["names"] == {'yitzchaq': 'Yitzchaq'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['garesh(ha_amah_ve_et_benah)', 'yera(be_einekha)', 'shema(be_qol_sarah)', 'tiri(hagar)', 'qumi_sei_ve_hachaziqi(et_ha_naar)']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['paqad_ka_asher_amar_va_yaas_ka_asher_diber', 'ben_li_zequnayv', 'la_moed_asher_diber_elohim', 'ka_asher_tziva_oto_elohim', 'ben_meat_shanah', 'tzechoq_asah_li_elohim_kol_ha_shomea_yitzchaq_li', 'mi_milel_le_avraham_heniqah_vanim_sarah', 'lo_yirash_ben_ha_amah_im_beni_im_yitzchaq', 'va_yera_ha_davar_meod_be_einei_avraham', 'ki_ve_yitzchaq_yiqare_lekha_zara', 'le_goy_asimenu_ki_zarakha_hu', 'va_yashkem_va_yeshalcheha_va_teta', 'al_ereh_be_mot_ha_yaled', 'shama_elohim_el_qol_ha_naar_ba_asher_hu_sham', 'ki_le_goy_gadol_asimenu', 'elohim_et_ha_naar_va_yigdal', 'elohim_imkha_be_khol_asher_atah_oseh', 'ka_chesed_asher_asiti_imkha', 'anokhi_ishavea', 'lo_yadati_lo_higadta_lo_shamati_bilti_ha_yom', 'sheva_khevasot_tiqach_mi_yadi_le_edah', 'ki_chafarti_et_ha_beer', 'pattern: al_ken_qara_la_maqom_beer_shava', 'va_yiqra_be_shem_YHWH_el_olam', 'va_yagar_be_eretz_pelishtim_yamim_rabim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
