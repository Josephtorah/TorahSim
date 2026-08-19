#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_20_the_ten_utterances — 20:1-26
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_20_the_ten_utterances.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The Ten Utterances (20:1-26)"""
from machine import Machine

m = Machine("exo_20_the_ten_utterances")

# -------------------------- Exod.20.1 · GOD_SPOKE_ALL_THESE_WORDS ----------
# וַיְדַבֵּר אֱלֹהִים אֵת כָּל־הַדְּבָרִים הָאֵלֶּה לֵאמֹר
# "[EN-AID] And God spoke all these words, saying:"
m.step("Exod.20.1")
# ‹וַיְדַבֵּר אֱלֹהִים אֵת כָּל־הַדְּבָרִים הָאֵלֶּה לֵאמֹר› (“and-speak God
# obj-marker all the-word/thing the-these to-say”) — fact holds: and-speak-
# God
m.fact("va_yedaber_elohim")

# -------------------------- Exod.20.2 · I_AM -------------------------------
# אָנֹכִי יְהוָה אֱלֹהֶיךָ אֲשֶׁר הוֹצֵאתִיךָ מֵאֶרֶץ מִצְרַיִם מִבֵּית
# עֲבָדִים
# "[EN-AID] I am the LORD your God, who brought you out of the land of
# Egypt, out of the house of slaves."
m.step("Exod.20.2")
# ‹אָנֹכִי יְהוָה אֱלֹהֶיךָ› (“YHWH God-you/your”) —
m.statute("BIND", "anokhi_YHWH_elohekha")

# -------------------------- Exod.20.3 · NO_OTHER_GODS ----------------------
# לֹא יִהְיֶה־לְךָ אֱלֹהִים אֲחֵרִים עַל־פָּנָיַ
# "[EN-AID] There shall not be to you other gods before My face."
m.step("Exod.20.3")
# ‹לֹא יִהְיֶה־לְךָ אֱלֹהִים אֲחֵרִים› (“not be to-you/your God other”) —
m.statute("FORBID", "elohim_acherim")

# -------------------------- Exod.20.4 · NO_GRAVEN_IMAGE --------------------
# לֹא תַעֲשֶׂה־לְךָ פֶסֶל וְכָל־תְּמוּנָה אֲשֶׁר בַּשָּׁמַיִם מִמַּעַל
# וַאֲשֶׁר בָּאָרֶץ מִתָּחַת וַאֲשֶׁר בַּמַּיִם מִתַּחַת לָאָרֶץ
# "[EN-AID] You shall not make yourself a graven image, or any likeness of
# what is in the heavens above, or what is in the earth beneath, or what is
# in the waters beneath the earth."
m.step("Exod.20.4")
# ‹לֹא תַעֲשֶׂה־לְךָ פֶסֶל וְכָל־תְּמוּנָה› (“not make to-you/your idol and-
# all something-portioned-out”) — fact holds: not-make-to-you-idol
m.fact("lo_taase_lekha_fesel")

# -------------------------- Exod.20.5 · A_JEALOUS_GOD ----------------------
# לֹא־תִשְׁתַּחֲוֶה לָהֶם וְלֹא תָעָבְדֵם כִּי אָנֹכִי יְהוָה אֱלֹהֶיךָ אֵל
# קַנָּא פֹּקֵד עֲוֺן אָבֹת עַל־בָּנִים עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים
# לְשֹׂנְאָי
# "[EN-AID] You shall not bow down to them, and you shall not serve them;
# for I the LORD your God am a jealous God, visiting the iniquity of fathers
# on sons, on the third and on the fourth generation, to those who hate Me."
m.step("Exod.20.5")
# ‹כִּי אָנֹכִי יְהוָה אֱלֹהֶיךָ אֵל קַנָּא› (“that YHWH God-you/your
# strength jealous”) — fact holds: strength-jealous
m.fact("el_qana")

# -------------------------- Exod.20.6 · MERCY_TO_THOUSANDS -----------------
# וְעֹשֶׂה חֶסֶד לַאֲלָפִים לְאֹהֲבַי וּלְשֹׁמְרֵי מִצְוֺתָי
# "[EN-AID] And doing kindness to thousands — to those who love Me, and to
# those who keep My commandments."
m.step("Exod.20.6")
# ‹וְעֹשֶׂה חֶסֶד לַאֲלָפִים› (“and-make kindness to-thousand”) — fact
# holds: and-make-kindness-to-thousand
m.fact("ve_ose_chesed_la_alafim")

# -------------------------- Exod.20.7 · THE_NAME_IN_VAIN -------------------
# לֹא תִשָּׂא אֶת־שֵׁם־יְהוָה אֱלֹהֶיךָ לַשָּׁוְא כִּי לֹא יְנַקֶּה יְהוָה
# אֵת אֲשֶׁר־יִשָּׂא אֶת־שְׁמוֹ לַשָּׁוְא
# "[EN-AID] You shall not take up the name of the LORD your God in vain; for
# the LORD will not hold him guiltless who takes up His name in vain."
m.step("Exod.20.7")
# ‹לֹא תִשָּׂא אֶת־שֵׁם־יְהוָה אֱלֹהֶיךָ לַשָּׁוְא› (“not lift/carry obj-
# marker name YHWH God-you/your to-evil”) —
m.statute("FORBID", "shem_la_shav")

# -------------------------- Exod.20.8 · REMEMBER_THE_SABBATH ---------------
# זָכוֹר אֶת־יוֹם הַשַּׁבָּת לְקַדְּשׁוֹ
# "[EN-AID] Remember the sabbath day, to keep it holy."
m.step("Exod.20.8")
# ‹זָכוֹר אֶת־יוֹם הַשַּׁבָּת לְקַדְּשׁוֹ› (“mark obj-marker day the-
# intermission to-sanctify-him/its”) —
m.statute("BIND", "zakhor_et_yom_ha_shabat")

# -------------------------- Exod.20.9 · SIX_DAYS_SHALL_YOU_LABOR -----------
# שֵׁשֶׁת יָמִים תַּעֲבֹד וְעָשִׂיתָ כָּל־מְלַאכְתֶּךָ
# "[EN-AID] Six days shall you labor, and do all your work."
m.step("Exod.20.9")
# ‹שֵׁשֶׁת יָמִים תַּעֲבֹד וְעָשִׂיתָ› (“six day work/serve and-make”) —
# fact holds: six-day-work/serve
m.fact("sheshet_yamim_taavod")

# -------------------------- Exod.20.10 · THE_SEVENTH_IS_REST ---------------
# וְיוֹם הַשְּׁבִיעִי שַׁבָּת לַיהוָה אֱלֹהֶיךָ לֹא־תַעֲשֶׂה כָל־מְלָאכָה
# אַתָּה וּבִנְךָ־וּבִתֶּךָ עַבְדְּךָ וַאֲמָתְךָ וּבְהֶמְתֶּךָ וְגֵרְךָ
# אֲשֶׁר בִּשְׁעָרֶיךָ
# "[EN-AID] And the seventh day is a sabbath to the LORD your God; you shall
# not do any work — you, and your son and your daughter, your servant and
# your maid, and your beast, and your stranger who is within your gates."
m.step("Exod.20.10")
# ‹אַתָּה וּבִנְךָ־וּבִתֶּךָ עַבְדְּךָ וַאֲמָתְךָ וּבְהֶמְתֶּךָ וְגֵרְךָ›
# (“you and-son-you/your and-daughter-you/your servant-you/your and-
# maidservant-you/your and-livestock-you/your and-sojourner-you/your”) —
# fact holds: intermission-to-the-LORD-elohekha
m.fact("shabat_la_YHWH_elohekha")

# -------------------------- Exod.20.11 · THE_CREATION_WARRANT --------------
# כִּי שֵׁשֶׁת־יָמִים עָשָׂה יְהוָה אֶת־הַשָּׁמַיִם וְאֶת־הָאָרֶץ אֶת־הַיָּם
# וְאֶת־כָּל־אֲשֶׁר־בָּם וַיָּנַח בַּיּוֹם הַשְּׁבִיעִי עַל־כֵּן בֵּרַךְ
# יְהוָה אֶת־יוֹם הַשַּׁבָּת וַיְקַדְּשֵׁהוּ
# "[EN-AID] For six days the LORD made the heavens and the earth, the sea
# and all that is in them, and He rested on the seventh day; therefore the
# LORD blessed the sabbath day, and sanctified it."
m.step("Exod.20.11")
# ‹עַל־כֵּן בֵּרַךְ יְהוָה אֶת־יוֹם הַשַּׁבָּת וַיְקַדְּשֵׁהוּ› (“over so
# bless YHWH obj-marker day the-intermission and-sanctify-him/its”) — fact
# holds: over-so-bless-the-LORD
m.fact("al_ken_berakh_YHWH")

# -------------------------- Exod.20.12 · HONOR_FATHER_AND_MOTHER -----------
# כַּבֵּד אֶת־אָבִיךָ וְאֶת־אִמֶּךָ לְמַעַן יַאֲרִכוּן יָמֶיךָ עַל הָאֲדָמָה
# אֲשֶׁר־יְהוָה אֱלֹהֶיךָ נֹתֵן לָךְ
# "[EN-AID] Honor your father and your mother — that your days may be long
# on the land which the LORD your God gives you."
m.step("Exod.20.12")
# ‹כַּבֵּד אֶת־אָבִיךָ וְאֶת־אִמֶּךָ› (“be-heavy obj-marker father-you/your
# and-obj-marker mother-you/your”) —
m.statute("BIND", "kabed_av_va_em")

# -------------------------- Exod.20.13 · NO_MURDER -------------------------
# לֹא תִּרְצָח
# "[EN-AID] You shall not murder."
m.step("Exod.20.13")
# ‹לֹא תִּרְצָח› (“not dash-in-pieces”) —
m.statute("FORBID", "retzach")

# -------------------------- Exod.20.14 · NO_ADULTERY -----------------------
# לֹא תִּנְאָף
# "[EN-AID] You shall not commit adultery."
m.step("Exod.20.14")
# ‹לֹא תִּנְאָף› (“not commit-adultery”) —
m.statute("FORBID", "niuf")

# -------------------------- Exod.20.15 · NO_THEFT --------------------------
# לֹא תִּגְנֹב
# "[EN-AID] You shall not steal."
m.step("Exod.20.15")
# ‹לֹא תִּגְנֹב› (“not steal”) —
m.statute("FORBID", "geneva")

# -------------------------- Exod.20.16 · NO_FALSE_WITNESS ------------------
# לֹא־תַעֲנֶה בְרֵעֲךָ עֵד שָׁקֶר
# "[EN-AID] You shall not answer against your fellow as a false witness."
m.step("Exod.20.16")
# ‹לֹא־תַעֲנֶה בְרֵעֲךָ עֵד שָׁקֶר› (“not eye in-associate-you/your
# concretely untruth”) —
m.statute("FORBID", "ed_shaqer")

# -------------------------- Exod.20.17 · NO_COVETING -----------------------
# לֹא תַחְמֹד בֵּית רֵעֶךָ לֹא־תַחְמֹד אֵשֶׁת רֵעֶךָ וְעַבְדּוֹ וַאֲמָתוֹ
# וְשׁוֹרוֹ וַחֲמֹרוֹ וְכֹל אֲשֶׁר לְרֵעֶךָ
# "[EN-AID] You shall not covet your fellow's house; you shall not covet
# your fellow's wife, or his servant, or his maid, or his ox, or his donkey,
# or anything that is your fellow's."
m.step("Exod.20.17")
# ‹לֹא תַחְמֹד בֵּית רֵעֶךָ› (“not delight-in house associate-you/your”) —
m.statute("FORBID", "chimud")

# -------------------------- Exod.20.18 · SEEING_THE_VOICES -----------------
# וְכָל־הָעָם רֹאִים אֶת־הַקּוֹלֹת וְאֶת־הַלַּפִּידִם וְאֵת קוֹל הַשֹּׁפָר
# וְאֶת־הָהָר עָשֵׁן וַיַּרְא הָעָם וַיָּנֻעוּ וַיַּעַמְדוּ מֵרָחֹק
# "[EN-AID] And all the people were seeing the voices and the torches, and
# the voice of the shofar, and the mountain smoking; and the people saw, and
# they swayed, and stood far off."
m.step("Exod.20.18")
# ‹וְכָל־הָעָם רֹאִים אֶת־הַקּוֹלֹת וְאֶת־הַלַּפִּידִם וְאֵת קוֹל הַשֹּׁפָר
# וְאֶת־הָהָר עָשֵׁן› (“and-all the-people see obj-marker the-voice/sound
# and-obj-marker the-flambeau and-obj-marker voice/sound the-cornet and-obj-
# marker the-mountain smoky”) — event: see-obj-marker-the-voice/sound —
# theme ha-qolot
m.event("roim_et_ha_qolot", themes=["ha-qolot"])

# -------------------------- Exod.20.19 · SPEAK_YOU_WITH_US -----------------
# וַיֹּאמְרוּ אֶל־מֹשֶׁה דַּבֵּר־אַתָּה עִמָּנוּ וְנִשְׁמָעָה וְאַל־יְדַבֵּר
# עִמָּנוּ אֱלֹהִים פֶּן־נָמוּת
# "[EN-AID] And they said to Moses: Speak you with us, and we will hear; and
# let God not speak with us, lest we die."
m.step("Exod.20.19")
# ‹דַּבֵּר־אַתָּה עִמָּנוּ וְנִשְׁמָעָה› (“speak you with-us/our and-hear”)
# — the-people speaks a demand — LET: speak-you-imanu
m.declare("ha_am", "LET",
          "daber_ata_imanu")

# -------------------------- Exod.20.20 · FEAR_NOT_THE_TEST -----------------
# וַיֹּאמֶר מֹשֶׁה אֶל־הָעָם אַל־תִּירָאוּ כִּי לְבַעֲבוּר נַסּוֹת אֶתְכֶם
# בָּא הָאֱלֹהִים וּבַעֲבוּר תִּהְיֶה יִרְאָתוֹ עַל־פְּנֵיכֶם לְבִלְתִּי
# תֶחֱטָאוּ
# "[EN-AID] And Moses said to the people: Fear not, for in order to test you
# God has come — and in order that His fear be on your faces, that you sin
# not."
m.step("Exod.20.20")
# ‹כִּי לְבַעֲבוּר נַסּוֹת אֶתְכֶם בָּא הָאֱלֹהִים› (“that to-in-crossed
# test obj-marker-you/your(pl) come/bring the-God”) — fact holds: to-vaavur-
# test-etkhem
m.fact("le_vaavur_nasot_etkhem")

# -------------------------- Exod.20.21 · INTO_THE_THICK_CLOUD --------------
# וַיַּעֲמֹד הָעָם מֵרָחֹק וּמֹשֶׁה נִגַּשׁ אֶל־הָעֲרָפֶל אֲשֶׁר־שָׁם
# הָאֱלֹהִים
# "[EN-AID] And the people stood far off — and Moses drew near to the thick
# cloud where God was."
m.step("Exod.20.21")
# ‹וּמֹשֶׁה נִגַּשׁ אֶל־הָעֲרָפֶל אֲשֶׁר־שָׁם הָאֱלֹהִים› (“and-Moses be to
# the-gloom which there the-God”) — demand settled (popped from the queue):
# speak-you-imanu
m.result("daber_ata_imanu", tmark="t1")

# -------------------------- Exod.20.22 · FROM_THE_HEAVENS ------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה כֹּה תֹאמַר אֶל־בְּנֵי יִשְׂרָאֵל אַתֶּם
# רְאִיתֶם כִּי מִן־הַשָּׁמַיִם דִּבַּרְתִּי עִמָּכֶם
# "[EN-AID] And the LORD said to Moses: So shall you say to the sons of
# Israel: You have seen that from the heavens I spoke with you."
m.step("Exod.20.22")
# ‹אַתֶּם רְאִיתֶם כִּי מִן־הַשָּׁמַיִם דִּבַּרְתִּי עִמָּכֶם› (“you see
# that from the-heavens speak with-you/your(pl)”) — fact holds: from-the-
# heavens-speak
m.fact("min_ha_shamayim_dibarti")

# -------------------------- Exod.20.23 · NO_GODS_OF_SILVER -----------------
# לֹא תַעֲשׂוּן אִתִּי אֱלֹהֵי כֶסֶף וֵאלֹהֵי זָהָב לֹא תַעֲשׂוּ לָכֶם
# "[EN-AID] You shall not make with Me gods of silver, and gods of gold you
# shall not make for yourselves."
m.step("Exod.20.23")
# ‹לֹא תַעֲשׂוּן אִתִּי אֱלֹהֵי כֶסֶף וֵאלֹהֵי זָהָב› (“not make-ward with-
# me/my God silver and-God gold”) —
m.statute("FORBID", "elohe_khesef_ve_zahav")

# -------------------------- Exod.20.24 · AN_ALTAR_OF_EARTH -----------------
# מִזְבַּח אֲדָמָה תַּעֲשֶׂה־לִּי וְזָבַחְתָּ עָלָיו אֶת־עֹלֹתֶיךָ
# וְאֶת־שְׁלָמֶיךָ אֶת־צֹאנְךָ וְאֶת־בְּקָרֶךָ בְּכָל־הַמָּקוֹם אֲשֶׁר
# אַזְכִּיר אֶת־שְׁמִי אָבוֹא אֵלֶיךָ וּבֵרַכְתִּיךָ
# "[EN-AID] An altar of earth shall you make for Me, and you shall sacrifice
# on it your burnt-offerings and your peace-offerings, your flock and your
# herd; in every place where I cause My name to be mentioned, I will come to
# you and bless you."
m.step("Exod.20.24")
# ‹מִזְבַּח אֲדָמָה תַּעֲשֶׂה־לִּי› (“altar ground make to-me/my”) —
m.statute("BIND", "mizbach_adama")

# -------------------------- Exod.20.25 · NO_HEWN_STONES --------------------
# וְאִם־מִזְבַּח אֲבָנִים תַּעֲשֶׂה־לִּי לֹא־תִבְנֶה אֶתְהֶן גָּזִית כִּי
# חַרְבְּךָ הֵנַפְתָּ עָלֶיהָ וַתְּחַלְלֶהָ
# "[EN-AID] And if an altar of stones you make for Me, you shall not build
# them hewn; for you have lifted your sword upon it, and profaned it."
m.step("Exod.20.25")
# ‹לֹא־תִבְנֶה אֶתְהֶן גָּזִית› (“not build obj-marker-them/their something-
# cut”) —
m.statute("FORBID", "gazit")

# -------------------------- Exod.20.26 · NO_STEPS --------------------------
# וְלֹא־תַעֲלֶה בְמַעֲלֹת עַל־מִזְבְּחִי אֲשֶׁר לֹא־תִגָּלֶה עֶרְוָתְךָ
# עָלָיו
# "[EN-AID] And you shall not go up by steps onto My altar — that your
# nakedness be not uncovered on it."
m.step("Exod.20.26")
# ‹וְלֹא־תַעֲלֶה בְמַעֲלֹת עַל־מִזְבְּחִי› (“and-not go-up in-Most-High over
# altar-me/my”) —
m.statute("FORBID", "maalot")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yedaber_elohim', 'statute: BIND(anokhi_YHWH_elohekha)', 'statute: FORBID(elohim_acherim)', 'lo_taase_lekha_fesel', 'el_qana', 've_ose_chesed_la_alafim', 'statute: FORBID(shem_la_shav)', 'statute: BIND(zakhor_et_yom_ha_shabat)', 'sheshet_yamim_taavod', 'shabat_la_YHWH_elohekha', 'al_ken_berakh_YHWH', 'statute: BIND(kabed_av_va_em)', 'statute: FORBID(retzach)', 'statute: FORBID(niuf)', 'statute: FORBID(geneva)', 'statute: FORBID(ed_shaqer)', 'statute: FORBID(chimud)', 'le_vaavur_nasot_etkhem', 'min_ha_shamayim_dibarti', 'statute: FORBID(elohe_khesef_ve_zahav)', 'statute: BIND(mizbach_adama)', 'statute: FORBID(gazit)', 'statute: FORBID(maalot)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 17
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
