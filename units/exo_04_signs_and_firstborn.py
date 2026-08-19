#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_04_signs_and_firstborn — 4:1-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_04_signs_and_firstborn.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The signs and the firstborn (4:1-31)"""
from machine import Machine

m = Machine("exo_04_signs_and_firstborn")

# -------------------------- Exod.4.1 · THEY_WILL_NOT_BELIEVE ---------------
# וַיַּעַן מֹשֶׁה וַיֹּאמֶר וְהֵן לֹא־יַאֲמִינוּ לִי וְלֹא יִשְׁמְעוּ
# בְּקֹלִי כִּי יֹאמְרוּ לֹא־נִרְאָה אֵלֶיךָ יְהוָה
# "[EN-AID] And Moses answered and said: But behold, they will not believe
# me, and will not hear my voice; for they will say: The LORD has not
# appeared to you."
m.step("Exod.4.1")
# ‹וְהֵן לֹא־יַאֲמִינוּ לִי וְלֹא יִשְׁמְעוּ בְּקֹלִי› (“and-lo! not build-
# up to-me/my and-not hear in-voice/sound-me/my”) — fact holds: and-lo!-not-
# build-up-to-me
m.fact("ve_hen_lo_yaaminu_li")

# -------------------------- Exod.4.2 · WHAT_IS_THIS_IN_YOUR_HAND -----------
# וַיֹּאמֶר אֵלָיו יְהוָה מזה מַה־זֶּה בְיָדֶךָ וַיֹּאמֶר מַטֶּה
# "[EN-AID] And the LORD said to him: What is this in your hand? And he
# said: A staff."
m.step("Exod.4.2")
# ‹מזה מַה־זֶּה בְיָדֶךָ› (“from-this what this in-hand-you/your”) — fact
# holds: what-this-and-yadekha-staff/tribe
m.fact("ma_ze_ve_yadekha_mate")

# -------------------------- Exod.4.3 · THROW_IT_AND_HE_THREW ---------------
# וַיֹּאמֶר הַשְׁלִיכֵהוּ אַרְצָה וַיַּשְׁלִיכֵהוּ אַרְצָה וַיְהִי לְנָחָשׁ
# וַיָּנָס מֹשֶׁה מִפָּנָיו
# "[EN-AID] And He said: Throw it to the ground. And he threw it to the
# ground, and it became a serpent; and Moses fled from before it."
m.step("Exod.4.3")
# ‹הַשְׁלִיכֵהוּ אַרְצָה› (“throw-out-him/its earth-ward”) — the-LORD speaks
# a demand — LET: hashlikhehu-artzah
m.declare("YHWH", "LET",
          "hashlikhehu_artzah")
# ‹וַיַּשְׁלִיכֵהוּ אַרְצָה וַיְהִי לְנָחָשׁ› (“and-throw-out-him/its earth-
# ward and-be to-snake”) — demand settled (popped from the queue):
# hashlikhehu-artzah
m.result("hashlikhehu_artzah", tmark="t1")

# -------------------------- Exod.4.4 · SEIZE_THE_TAIL ----------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה שְׁלַח יָדְךָ וֶאֱחֹז בִּזְנָבוֹ וַיִּשְׁלַח
# יָדוֹ וַיַּחֲזֶק בּוֹ וַיְהִי לְמַטֶּה בְּכַפּוֹ
# "[EN-AID] And the LORD said to Moses: Send your hand, and seize it by the
# tail. And he sent his hand, and held it fast, and it became a staff in his
# palm."
m.step("Exod.4.4")
# ‹שְׁלַח יָדְךָ וֶאֱחֹז בִּזְנָבוֹ› (“send hand-you/your and-seize in-tail-
# him/its”) — the-LORD speaks a demand — LET: send-yadekha-and-seize-oh-
# that!-zenavo
m.declare("YHWH", "LET",
          "shelach_yadekha_ve_echoz_bi_zenavo")
# ‹וַיִּשְׁלַח יָדוֹ וַיַּחֲזֶק בּוֹ› (“and-send hand-him/its and-fasten-
# upon in-him/its”) — demand settled (popped from the queue): send-yadekha-
# and-seize-oh-that!-zenavo
m.result("shelach_yadekha_ve_echoz_bi_zenavo", tmark="t2")

# -------------------------- Exod.4.5 · THAT_THEY_MAY_BELIEVE ---------------
# לְמַעַן יַאֲמִינוּ כִּי־נִרְאָה אֵלֶיךָ יְהוָה אֱלֹהֵי אֲבֹתָם אֱלֹהֵי
# אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי יַעֲקֹב
# "[EN-AID] That they may believe that the LORD, the God of their fathers —
# the God of Abraham, the God of Isaac, and the God of Jacob — has appeared
# to you."
m.step("Exod.4.5")
# ‹לְמַעַן יַאֲמִינוּ› (“so-that build-up”) — fact holds: so-that-build-up
m.fact("lemaan_yaaminu")

# -------------------------- Exod.4.6 · THE_HAND_IN_THE_BOSOM ---------------
# וַיֹּאמֶר יְהוָה לוֹ עוֹד הָבֵא־נָא יָדְךָ בְּחֵיקֶךָ וַיָּבֵא יָדוֹ
# בְּחֵיקוֹ וַיּוֹצִאָהּ וְהִנֵּה יָדוֹ מְצֹרַעַת כַּשָּׁלֶג
# "[EN-AID] And the LORD said to him further: Bring, pray, your hand into
# your bosom. And he brought his hand into his bosom; and he took it out,
# and behold, his hand was leprous, as snow."
m.step("Exod.4.6")
# ‹הָבֵא־נָא יָדְךָ בְּחֵיקֶךָ› (“come/bring please hand-you/your in-bosom-
# you/your”) — the-LORD speaks a demand — LET: come/bring-please-yadekha-in-
# cheqekha
m.declare("YHWH", "LET",
          "have_na_yadekha_be_cheqekha")
# ‹וַיָּבֵא יָדוֹ בְּחֵיקוֹ› (“and-come/bring hand-him/its in-bosom-
# him/its”) — demand settled (popped from the queue): come/bring-please-
# yadekha-in-cheqekha
m.result("have_na_yadekha_be_cheqekha", tmark="t3")

# -------------------------- Exod.4.7 · THE_HAND_RESTORED -------------------
# וַיֹּאמֶר הָשֵׁב יָדְךָ אֶל־חֵיקֶךָ וַיָּשֶׁב יָדוֹ אֶל־חֵיקוֹ
# וַיּוֹצִאָהּ מֵחֵיקוֹ וְהִנֵּה־שָׁבָה כִּבְשָׂרוֹ
# "[EN-AID] And He said: Return your hand to your bosom. And he returned his
# hand to his bosom; and he took it out from his bosom, and behold, it
# returned as his flesh."
m.step("Exod.4.7")
# ‹הָשֵׁב יָדְךָ אֶל־חֵיקֶךָ› (“return hand-you/your to bosom-you/your”) —
# the-LORD speaks a demand — LET: return-yadekha-to-cheqekha
m.declare("YHWH", "LET",
          "hashev_yadekha_el_cheqekha")
# ‹וַיָּשֶׁב יָדוֹ אֶל־חֵיקוֹ› (“and-return hand-him/its to bosom-him/its”)
# — demand settled (popped from the queue): return-yadekha-to-cheqekha
m.result("hashev_yadekha_el_cheqekha", tmark="t4")

# -------------------------- Exod.4.8 · THE_VOICE_OF_THE_LATTER_SIGN --------
# וְהָיָה אִם־לֹא יַאֲמִינוּ לָךְ וְלֹא יִשְׁמְעוּ לְקֹל הָאֹת הָרִאשׁוֹן
# וְהֶאֱמִינוּ לְקֹל הָאֹת הָאַחֲרוֹן
# "[EN-AID] And it shall be, if they will not believe you, and will not hear
# the voice of the first sign, that they will believe the voice of the
# latter sign."
m.step("Exod.4.8")
# ‹וְהֶאֱמִינוּ לְקֹל הָאֹת הָאַחֲרוֹן› (“and-build-up to-voice/sound the-
# signs the-hinder”) — fact holds: and-build-up-to-voice/sound-the-ot-the-
# hinder
m.fact("ve_heeminu_le_qol_ha_ot_ha_acharon")

# -------------------------- Exod.4.9 · THE_NILE_ON_THE_DRY_LAND ------------
# וְהָיָה אִם־לֹא יַאֲמִינוּ גַּם לִשְׁנֵי הָאֹתוֹת הָאֵלֶּה וְלֹא
# יִשְׁמְעוּן לְקֹלֶךָ וְלָקַחְתָּ מִמֵּימֵי הַיְאֹר וְשָׁפַכְתָּ
# הַיַּבָּשָׁה וְהָיוּ הַמַּיִם אֲשֶׁר תִּקַּח מִן־הַיְאֹר וְהָיוּ לְדָם
# בַּיַּבָּשֶׁת
# "[EN-AID] And it shall be, if they will not believe even these two signs,
# and will not hear your voice, that you shall take of the water of the
# Nile, and pour it on the dry land; and the water which you take from the
# Nile shall become blood on the dry land."
m.step("Exod.4.9")
# ‹וְלָקַחְתָּ מִמֵּימֵי הַיְאֹר וְשָׁפַכְתָּ הַיַּבָּשָׁה› (“and-take from-
# waters the-Nile and-spill-forth the-dry-land”) — fact holds: and-be-to-
# blood-in-the-yabashet
m.fact("ve_hayu_le_dam_ba_yabashet")

# -------------------------- Exod.4.10 · HEAVY_OF_MOUTH ---------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־יְהוָה בִּי אֲדֹנָי לֹא אִישׁ דְּבָרִים אָנֹכִי גַּם
# מִתְּמוֹל גַּם מִשִּׁלְשֹׁם גַּם מֵאָז דַּבֶּרְךָ אֶל־עַבְדֶּךָ כִּי
# כְבַד־פֶּה וּכְבַד לָשׁוֹן אָנֹכִי
# "[EN-AID] And Moses said to the LORD: Please, my Lord, I am not a man of
# words — also from yesterday, also from the day before, also since You have
# spoken to Your servant; for heavy of mouth and heavy of tongue am I."
m.step("Exod.4.10")
# ‹כִּי כְבַד־פֶּה וּכְבַד לָשׁוֹן אָנֹכִי› (“that heavy mouth and-heavy
# tongue”) — fact holds: heavy-mouth-and-heavy-tongue
m.fact("khevad_pe_u_khevad_lashon")

# -------------------------- Exod.4.11 · WHO_SET_A_MOUTH --------------------
# וַיֹּאמֶר יְהוָה אֵלָיו מִי שָׂם פֶּה לָאָדָם אוֹ מִי־יָשׂוּם אִלֵּם אוֹ
# חֵרֵשׁ אוֹ פִקֵּחַ אוֹ עִוֵּר הֲלֹא אָנֹכִי יְהוָה
# "[EN-AID] And the LORD said to him: Who set a mouth for man, or who makes
# dumb, or deaf, or seeing, or blind? Is it not I, the LORD?"
m.step("Exod.4.11")
# ‹הֲלֹא אָנֹכִי יְהוָה› (“is-it-not YHWH”) — fact holds: the-not-I-the-LORD
m.fact("ha_lo_anokhi_YHWH")

# -------------------------- Exod.4.12 · GO_AND_I_AM_WITH_YOUR_MOUTH --------
# וְעַתָּה לֵךְ וְאָנֹכִי אֶהְיֶה עִם־פִּיךָ וְהוֹרֵיתִיךָ אֲשֶׁר תְּדַבֵּר
# "[EN-AID] And now, go — and I will be with your mouth, and will teach you
# what you shall speak."
m.step("Exod.4.12")
# ‹וְאָנֹכִי אֶהְיֶה עִם־פִּיךָ› (“and-I be with mouth-you/your”) — fact
# holds: and-I-be-if-pikha
m.fact("ve_anokhi_ehye_im_pikha")

# -------------------------- Exod.4.13 · SEND_BY_WHOSE_HAND -----------------
# וַיֹּאמֶר בִּי אֲדֹנָי שְׁלַח־נָא בְּיַד־תִּשְׁלָח
# "[EN-AID] And he said: Please, my Lord — send, pray, by the hand You will
# send."
m.step("Exod.4.13")
# ‹שְׁלַח־נָא בְּיַד־תִּשְׁלָח› (“send please in-hand send”) — Moses speaks
# a demand — LET: send-please-in-hand-send
m.declare("moshe", "LET",
          "shelach_na_be_yad_tishlach")

# -------------------------- Exod.4.14 · AARON_IS_COMING --------------------
# וַיִּחַר־אַף יְהוָה בְּמֹשֶׁה וַיֹּאמֶר הֲלֹא אַהֲרֹן אָחִיךָ הַלֵּוִי
# יָדַעְתִּי כִּי־דַבֵּר יְדַבֵּר הוּא וְגַם הִנֵּה־הוּא יֹצֵא לִקְרָאתֶךָ
# וְרָאֲךָ וְשָׂמַח בְּלִבּוֹ
# "[EN-AID] And the anger of the LORD burned against Moses, and He said: Is
# there not Aaron your brother, the Levite? I know that he will surely speak
# — he; and also, behold, he is coming out to meet you, and he will see you
# and rejoice in his heart."
m.step("Exod.4.14")
# ‹כִּי־דַבֵּר יְדַבֵּר הוּא וְגַם הִנֵּה־› (“that speak speak he/it and-
# also behold”) — fact holds: and-raakha-and-brighten-up-in-His-heart
m.fact("ve_raakha_ve_samach_be_libo")

# -------------------------- Exod.4.15 · WORDS_IN_HIS_MOUTH -----------------
# וְדִבַּרְתָּ אֵלָיו וְשַׂמְתָּ אֶת־הַדְּבָרִים בְּפִיו וְאָנֹכִי אֶהְיֶה
# עִם־פִּיךָ וְעִם־פִּיהוּ וְהוֹרֵיתִי אֶתְכֶם אֵת אֲשֶׁר תַּעֲשׂוּן
# "[EN-AID] And you shall speak to him, and put the words in his mouth; and
# I will be with your mouth and with his mouth, and will teach you both what
# you shall do."
m.step("Exod.4.15")
# ‹וְשַׂמְתָּ אֶת־הַדְּבָרִים בְּפִיו› (“and-put/set obj-marker the-
# word/thing in-mouth-him/its”) — the-LORD speaks a demand — LET: and-
# put/set-signs-the-word/thing-in-fiv
m.declare("YHWH", "LET",
          "ve_samta_et_ha_devarim_be_fiv")

# -------------------------- Exod.4.16 · MOUTH_AND_GOD ----------------------
# וְדִבֶּר־הוּא לְךָ אֶל־הָעָם וְהָיָה הוּא יִהְיֶה־לְּךָ לְפֶה וְאַתָּה
# תִּהְיֶה־לּוֹ לֵאלֹהִים
# "[EN-AID] And he shall speak for you to the people; and it shall be — he
# shall be for you a mouth, and you shall be for him as God."
m.step("Exod.4.16")
# ‹וְהָיָה הוּא יִהְיֶה־לְּךָ לְפֶה› (“and-be he/it be to-you/your to-
# mouth”) — fact holds: he/it-be-to-you-to-mouth
m.fact("hu_yihye_lekha_le_fe")

# -------------------------- Exod.4.17 · TAKE_THIS_STAFF --------------------
# וְאֶת־הַמַּטֶּה הַזֶּה תִּקַּח בְּיָדֶךָ אֲשֶׁר תַּעֲשֶׂה־בּוֹ אֶת־הָאֹתֹת
# "[EN-AID] And this staff you shall take in your hand, with which you shall
# do the signs."
m.step("Exod.4.17")
# ‹וְאֶת־הַמַּטֶּה הַזֶּה תִּקַּח בְּיָדֶךָ› (“and-obj-marker the-
# staff/tribe the-this take in-hand-you/your”) — the-LORD speaks a demand —
# LET: and-signs-the-staff/tribe-take-in-yadekha
m.declare("YHWH", "LET",
          "ve_et_ha_mate_tiqach_be_yadekha")

# -------------------------- Exod.4.18 · LET_ME_GO_AND_GO_IN_PEACE ----------
# וַיֵּלֶךְ מֹשֶׁה וַיָּשָׁב אֶל־יֶתֶר חֹתְנוֹ וַיֹּאמֶר לוֹ אֵלֲכָה נָּא
# וְאָשׁוּבָה אֶל־אַחַי אֲשֶׁר־בְּמִצְרַיִם וְאֶרְאֶה הַעוֹדָם חַיִּים
# וַיֹּאמֶר יִתְרוֹ לְמֹשֶׁה לֵךְ לְשָׁלוֹם
# "[EN-AID] And Moses went and returned to Jether his father-in-law, and
# said to him: Let me go, pray, and return to my brothers who are in Egypt,
# and see whether they still live. And Jethro said to Moses: Go in peace."
m.step("Exod.4.18")
# ‹אֵלֲכָה נָּא וְאָשׁוּבָה אֶל־אַחַי› (“go please and-return to brother-
# me/my”) — Moses speaks a demand — LET: elkha-please-and-return-to-achai
m.declare("moshe", "LET",
          "elkha_na_ve_ashuva_el_achai")
# ‹לֵךְ לְשָׁלוֹם› (“go to-safe”) — demand settled (popped from the queue):
# elkha-please-and-return-to-achai
m.result("elkha_na_ve_ashuva_el_achai", tmark="t5")

# -------------------------- Exod.4.19 · THE_SEEKERS_ARE_DEAD ---------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה בְּמִדְיָן לֵךְ שֻׁב מִצְרָיִם כִּי־מֵתוּ
# כָּל־הָאֲנָשִׁים הַמְבַקְשִׁים אֶת־נַפְשֶׁךָ
# "[EN-AID] And the LORD said to Moses in Midian: Go, return to Egypt; for
# all the men who sought your life have died."
m.step("Exod.4.19")
# ‹לֵךְ שֻׁב מִצְרָיִם› (“go return Egypt”) — the-LORD speaks a demand —
# LET: go-return-Egypt
m.declare("YHWH", "LET",
          "lekh_shuv_mitzrayim")

# -------------------------- Exod.4.20 · THE_DONKEY_AND_THE_STAFF -----------
# וַיִּקַּח מֹשֶׁה אֶת־אִשְׁתּוֹ וְאֶת־בָּנָיו וַיַּרְכִּבֵם עַל־הַחֲמֹר
# וַיָּשָׁב אַרְצָה מִצְרָיִם וַיִּקַּח מֹשֶׁה אֶת־מַטֵּה הָאֱלֹהִים
# בְּיָדוֹ
# "[EN-AID] And Moses took his wife and his sons, and mounted them on the
# donkey, and returned to the land of Egypt; and Moses took the staff of God
# in his hand."
m.step("Exod.4.20")
# ‹וַיָּשָׁב אַרְצָה מִצְרָיִם› (“and-return earth-ward Egypt”) — demand
# settled (popped from the queue): go-return-Egypt
m.result("lekh_shuv_mitzrayim", tmark="t6")
# ‹וַיִּקַּח מֹשֶׁה אֶת־מַטֵּה הָאֱלֹהִים בְּיָדוֹ› (“and-take Moses obj-
# marker staff/tribe the-God in-hand-him/its”) — demand settled (popped from
# the queue): and-signs-the-staff/tribe-take-in-yadekha
m.result("ve_et_ha_mate_tiqach_be_yadekha", tmark="t7")

# -------------------------- Exod.4.21 · THE_WONDERS_AND_THE_HARDENING ------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה בְּלֶכְתְּךָ לָשׁוּב מִצְרַיְמָה רְאֵה
# כָּל־הַמֹּפְתִים אֲשֶׁר־שַׂמְתִּי בְיָדֶךָ וַעֲשִׂיתָם לִפְנֵי פַרְעֹה
# וַאֲנִי אֲחַזֵּק אֶת־לִבּוֹ וְלֹא יְשַׁלַּח אֶת־הָעָם
# "[EN-AID] And the LORD said to Moses: When you go to return to Egypt, see
# all the wonders which I have put in your hand, and do them before Pharaoh;
# and I will strengthen his heart, and he will not send the people out."
m.step("Exod.4.21")
# ‹רְאֵה כָּל־הַמֹּפְתִים אֲשֶׁר־שַׂמְתִּי בְיָדֶךָ וַעֲשִׂיתָם לִפְנֵי
# פַרְעֹה› (“see all the-miracle which put/set in-hand-you/your and-make-
# them/their to-face Pharaoh”) — the-LORD speaks a demand — LET: reeh-the-
# miracle-and-asitam-lifne-Pharaoh
m.declare("YHWH", "LET",
          "reeh_ha_moftim_va_asitam_lifne_faro")

# -------------------------- Exod.4.22 · MY_SON_MY_FIRSTBORN ----------------
# וְאָמַרְתָּ אֶל־פַּרְעֹה כֹּה אָמַר יְהוָה בְּנִי בְכֹרִי יִשְׂרָאֵל
# "[EN-AID] And you shall say to Pharaoh: Thus says the LORD: My son, My
# firstborn — Israel."
m.step("Exod.4.22")
# ‹כֹּה אָמַר יְהוָה בְּנִי בְכֹרִי יִשְׂרָאֵל› (“like-this say YHWH son-
# me/my firstborn-me/my Israel”) — the-LORD speaks a demand — LET: and-say-
# to-Pharaoh-beni-vekhori
m.declare("YHWH", "LET",
          "ve_amarta_el_paro_beni_vekhori")

# -------------------------- Exod.4.23 · I_KILL_YOUR_FIRSTBORN --------------
# וָאֹמַר אֵלֶיךָ שַׁלַּח אֶת־בְּנִי וְיַעַבְדֵנִי וַתְּמָאֵן לְשַׁלְּחוֹ
# הִנֵּה אָנֹכִי הֹרֵג אֶת־בִּנְךָ בְּכֹרֶךָ
# "[EN-AID] And I say to you: Send My son, that he may serve Me; and you
# refuse to send him — behold, I kill your son, your firstborn."
m.step("Exod.4.23")
# ‹הִנֵּה אָנֹכִי הֹרֵג אֶת־בִּנְךָ בְּכֹרֶךָ› (“behold smite-with-deadly-
# intent obj-marker son-you/your firstborn-you/your”) — fact holds: behold-
# I-smite-with-deadly-intent-signs-binkha-bekhorekha
m.fact("hine_anokhi_horeg_et_binkha_bekhorekha")

# -------------------------- Exod.4.24 · THE_ENCOUNTER_AT_THE_INN -----------
# וַיְהִי בַדֶּרֶךְ בַּמָּלוֹן וַיִּפְגְּשֵׁהוּ יְהוָה וַיְבַקֵּשׁ הֲמִיתוֹ
# "[EN-AID] And it was on the way, at the lodging-place; and the LORD met
# him, and sought to kill him."
m.step("Exod.4.24")
# ‹וַיִּפְגְּשֵׁהוּ יְהוָה וַיְבַקֵּשׁ הֲמִיתוֹ› (“and-come-in-contact-with-
# him/its YHWH and-search-out die-him/its”) — fact holds: and-search-out-
# hamito
m.fact("va_yevaqesh_hamito")

# -------------------------- Exod.4.25 · THE_FLINT --------------------------
# וַתִּקַּח צִפֹּרָה צֹר וַתִּכְרֹת אֶת־עָרְלַת בְּנָהּ וַתַּגַּע לְרַגְלָיו
# וַתֹּאמֶר כִּי חֲתַן־דָּמִים אַתָּה לִי
# "[EN-AID] And Zipporah took a flint, and cut off the foreskin of her son,
# and made it touch his feet; and she said: For a bridegroom of blood are
# you to me."
m.step("Exod.4.25")
# ‹וַתִּקַּח צִפֹּרָה צֹר וַתִּכְרֹת אֶת־עָרְלַת בְּנָהּ› (“and-take
# Zipporah stone and-cut obj-marker foreskin son-her/its”) — event: karta —
# agent Zipporah
m.event("karta", agent="tzipora")

# -------------------------- Exod.4.26 · HE_RELEASED ------------------------
# וַיִּרֶף מִמֶּנּוּ אָז אָמְרָה חֲתַן דָּמִים לַמּוּלֹת
# "[EN-AID] And He released him. Then she said: A bridegroom of blood — for
# the circumcisions."
m.step("Exod.4.26")
# ‹וַיִּרֶף מִמֶּנּוּ› (“and-slacken from-us/our”) — fact holds: and-
# slacken-from-it
m.fact("va_yiref_mimenu")

# -------------------------- Exod.4.27 · GO_MEET_MOSES ----------------------
# וַיֹּאמֶר יְהוָה אֶל־אַהֲרֹן לֵךְ לִקְרַאת מֹשֶׁה הַמִּדְבָּרָה וַיֵּלֶךְ
# וַיִּפְגְּשֵׁהוּ בְּהַר הָאֱלֹהִים וַיִּשַּׁק־לוֹ
# "[EN-AID] And the LORD said to Aaron: Go to meet Moses, to the wilderness.
# And he went, and met him at the mountain of God, and kissed him."
m.step("Exod.4.27")
# ‹לֵךְ לִקְרַאת מֹשֶׁה הַמִּדְבָּרָה› (“go to-encountering Moses the-
# pasture-ward”) — the-LORD speaks a demand — LET: go-liqrat-Moses-the-
# midbara
m.declare("YHWH", "LET",
          "lekh_liqrat_moshe_ha_midbara")
# ‹וַיֵּלֶךְ וַיִּפְגְּשֵׁהוּ בְּהַר הָאֱלֹהִים וַיִּשַּׁק־לוֹ› (“and-go
# and-come-in-contact-with-him/its in-mountain the-God and-kiss to-him/its”)
# — demand settled (popped from the queue): go-liqrat-Moses-the-midbara
m.result("lekh_liqrat_moshe_ha_midbara", tmark="t8")

# -------------------------- Exod.4.28 · HE_TOLD_HIM_ALL_THE_WORDS ----------
# וַיַּגֵּד מֹשֶׁה לְאַהֲרֹן אֵת כָּל־דִּבְרֵי יְהוָה אֲשֶׁר שְׁלָחוֹ וְאֵת
# כָּל־הָאֹתֹת אֲשֶׁר צִוָּהוּ
# "[EN-AID] And Moses told Aaron all the words of the LORD who had sent him,
# and all the signs which He had commanded him."
m.step("Exod.4.28")
# ‹וַיַּגֵּד מֹשֶׁה לְאַהֲרֹן אֵת כָּל־דִּבְרֵי יְהוָה אֲשֶׁר שְׁלָחוֹ›
# (“and-tell Moses to-Aaron obj-marker all word/thing YHWH which send-
# him/its”) — demand settled (popped from the queue): and-put/set-signs-the-
# word/thing-in-fiv
m.result("ve_samta_et_ha_devarim_be_fiv", tmark="t9")

# -------------------------- Exod.4.29 · THE_ELDERS_GATHERED ----------------
# וַיֵּלֶךְ מֹשֶׁה וְאַהֲרֹן וַיַּאַסְפוּ אֶת־כָּל־זִקְנֵי בְּנֵי יִשְׂרָאֵל
# "[EN-AID] And Moses and Aaron went, and gathered all the elders of the
# sons of Israel."
m.step("Exod.4.29")
# ‹וַיַּאַסְפוּ אֶת־כָּל־זִקְנֵי בְּנֵי יִשְׂרָאֵל› (“and-gather-for-any-
# purpose obj-marker all old son Israel”) — fact holds: and-gather-for-any-
# purpose-signs-all-old-son-Israel
m.fact("va_yaasfu_et_kol_ziqne_bene_yisrael")

# -------------------------- Exod.4.30 · AARON_SPOKE_AND_DID_THE_SIGNS ------
# וַיְדַבֵּר אַהֲרֹן אֵת כָּל־הַדְּבָרִים אֲשֶׁר־דִּבֶּר יְהוָה אֶל־מֹשֶׁה
# וַיַּעַשׂ הָאֹתֹת לְעֵינֵי הָעָם
# "[EN-AID] And Aaron spoke all the words which the LORD had spoken to
# Moses; and he did the signs before the eyes of the people."
m.step("Exod.4.30")
# ‹וַיַּעַשׂ הָאֹתֹת לְעֵינֵי הָעָם› (“and-make the-signs to-eye the-
# people”) — fact holds: and-make-the-signs-to-eye-the-people
m.fact("va_yaas_ha_otot_le_ene_ha_am")

# -------------------------- Exod.4.31 · AND_THE_PEOPLE_BELIEVED ------------
# וַיַּאֲמֵן הָעָם וַיִּשְׁמְעוּ כִּי־פָקַד יְהוָה אֶת־בְּנֵי יִשְׂרָאֵל
# וְכִי רָאָה אֶת־עָנְיָם וַיִּקְּדוּ וַיִּשְׁתַּחֲוּוּ
# "[EN-AID] And the people believed; and they heard that the LORD had
# visited the sons of Israel, and that He had seen their affliction; and
# they bowed and prostrated themselves."
m.step("Exod.4.31")
# ‹וַיַּאֲמֵן הָעָם› (“and-build-up the-people”) — fact holds: and-build-up-
# the-people
m.fact("va_yaamen_ha_am")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shelach_na_be_yad_tishlach', 'reeh_ha_moftim_va_asitam_lifne_faro', 've_amarta_el_paro_beni_vekhori']
    assert len(m.SPECS["log"]) == 12
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_hen_lo_yaaminu_li', 'ma_ze_ve_yadekha_mate', 'lemaan_yaaminu', 've_heeminu_le_qol_ha_ot_ha_acharon', 've_hayu_le_dam_ba_yabashet', 'khevad_pe_u_khevad_lashon', 'ha_lo_anokhi_YHWH', 've_anokhi_ehye_im_pikha', 've_raakha_ve_samach_be_libo', 'hu_yihye_lekha_le_fe', 'hine_anokhi_horeg_et_binkha_bekhorekha', 'va_yevaqesh_hamito', 'va_yiref_mimenu', 'va_yaasfu_et_kol_ziqne_bene_yisrael', 'va_yaas_ha_otot_le_ene_ha_am', 'va_yaamen_ha_am'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 22
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
