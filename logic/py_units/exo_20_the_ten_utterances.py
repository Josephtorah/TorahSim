#!/usr/bin/env python3
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
# ‹וַיְדַבֵּר אֱלֹהִים אֵת› (“and-speak God obj-marker”)
# ‹כָּל־הַדְּבָרִים הָאֵלֶּה לֵאמֹר› (“all the-word/thing the-these to-say”)
# "[EN-AID] And God spoke all these words, saying:"
m.step("Exod.20.1")
# ‹וַיְדַבֵּר אֱלֹהִים אֵת› (“and-speak God obj-marker”)
# ‹כָּל־הַדְּבָרִים הָאֵלֶּה לֵאמֹר› (“all the-word/thing the-these to-say”)
# — fact holds: and-speak-God
m.fact("va_yedaber_elohim")

# -------------------------- Exod.20.2 · I_AM -------------------------------
# ‹אָנֹכִי יְהוָה אֱלֹהֶיךָ› (“YHWH God-you/your”)
# ‹אֲשֶׁר הוֹצֵאתִיךָ מֵאֶרֶץ› (“which bring-forth-you/your from-earth”)
# ‹מִצְרַיִם מִבֵּית עֲבָדִים› (“Egypt from-house servant”)
# "[EN-AID] I am the LORD your God, who brought you out of the land of
# Egypt, out of the house of slaves."
m.step("Exod.20.2")
# ‹אָנֹכִי יְהוָה אֱלֹהֶיךָ› (“YHWH God-you/your”)
m.statute("BIND", "anokhi_YHWH_elohekha")

# -------------------------- Exod.20.3 · NO_OTHER_GODS ----------------------
# ‹לֹא יִהְיֶה־לְךָ אֱלֹהִים› (“not be to-you/your God”)
# ‹אֲחֵרִים עַל־פָּנָיַ› (“other over face-me/my”)
# "[EN-AID] There shall not be to you other gods before My face."
m.step("Exod.20.3")
# ‹לֹא יִהְיֶה־לְךָ אֱלֹהִים› (“not be to-you/your God”)
# ‹אֲחֵרִים› (“other”)
m.statute("FORBID", "elohim_acherim")

# -------------------------- Exod.20.4 · NO_GRAVEN_IMAGE --------------------
# ‹לֹא תַעֲשֶׂה־לְךָ פֶסֶל› (“not make to-you/your idol”)
# ‹וְכָל־תְּמוּנָה אֲשֶׁר בַּשָּׁמַיִם› (“and-all something-portioned-out
# which in-heavens”)
# ‹מִמַּעַל וַאֲשֶׁר בָּאָרֶץ› (“from-upper-part and-which in-earth”)
# ‹מִתָּחַת וַאֲשֶׁר בַּמַּיִם› (“from-under and-which in-waters”)
# ‹מִתַּחַת לָאָרֶץ› (“from-under to-earth”)
# "[EN-AID] You shall not make yourself a graven image, or any likeness of
# what is in the heavens above, or what is in the earth beneath, or what is
# in the waters beneath the earth."
m.step("Exod.20.4")
# ‹לֹא תַעֲשֶׂה־לְךָ פֶסֶל› (“not make to-you/your idol”)
# ‹וְכָל־תְּמוּנָה› (“and-all something-portioned-out”)
# — fact holds: not-make-to-you-idol
m.fact("lo_taase_lekha_fesel")

# -------------------------- Exod.20.5 · A_JEALOUS_GOD ----------------------
# ‹לֹא־תִשְׁתַּחֲוֶה לָהֶם וְלֹא› (“not afflict to-them/their and-not”)
# ‹תָעָבְדֵם כִּי אָנֹכִי› (“work/serve-them/their that”)
# ‹יְהוָה אֱלֹהֶיךָ אֵל› (“YHWH God-you/your strength”)
# ‹קַנָּא פֹּקֵד עֲוֺן› (“jealous count/visit perversity”)
# ‹אָבֹת עַל־בָּנִים עַל־שִׁלֵּשִׁים› (“father over son over descendant-of-
# the-third-degr”)
# ‹וְעַל־רִבֵּעִים לְשֹׂנְאָי› (“and-over descendant-of-the-fourth-gen to-
# hate-me/my”)
# "[EN-AID] You shall not bow down to them, and you shall not serve them;
# for I the LORD your God am a jealous God, visiting the iniquity of fathers
# on sons, on the third and on the fourth generation, to those who hate Me."
m.step("Exod.20.5")
# ‹כִּי אָנֹכִי יְהוָה› (“that YHWH”)
# ‹אֱלֹהֶיךָ אֵל קַנָּא› (“God-you/your strength jealous”)
# — fact holds: strength-jealous
m.fact("el_qana")
# witness-tier presupposed read: utterance_rider_file on poqed_avon_avot —
# read, not installed
m.witness_read("poqed_avon_avot", "utterance_rider_file",
                cites=["Berakhot 7a:26", "Berakhot 7a:27", "Sanhedrin 99a:20", "Sanhedrin 99a:21", "Bava Metzia 5b:18", "Bava Metzia 5b:19", "Bava Metzia 5b:20", "Beitzah 15b:4", "Beitzah 15b:5", "Bava Kamma 74b:7", "Bava Kamma 74b:8", "Bava Kamma 74b:9", "Sanhedrin 86a:15", "Sanhedrin 86a:16", "Sanhedrin 86a:17"])

# -------------------------- Exod.20.6 · MERCY_TO_THOUSANDS -----------------
# ‹וְעֹשֶׂה חֶסֶד לַאֲלָפִים› (“and-make kindness to-thousand”)
# ‹לְאֹהֲבַי וּלְשֹׁמְרֵי מִצְוֺתָי› (“to-have-affection-for-me/my and-to-
# keep/guard commandment-me/my”)
# "[EN-AID] And doing kindness to thousands — to those who love Me, and to
# those who keep My commandments."
m.step("Exod.20.6")
# ‹וְעֹשֶׂה חֶסֶד לַאֲלָפִים› (“and-make kindness to-thousand”)
# — fact holds: and-make-kindness-to-thousand
m.fact("ve_ose_chesed_la_alafim")

# -------------------------- Exod.20.7 · THE_NAME_IN_VAIN -------------------
# ‹לֹא תִשָּׂא אֶת־שֵׁם־יְהוָה› (“not lift/carry obj-marker name YHWH”)
# ‹אֱלֹהֶיךָ לַשָּׁוְא כִּי› (“God-you/your to-evil that”)
# ‹לֹא יְנַקֶּה יְהוָה› (“not be-clean YHWH”)
# ‹אֵת אֲשֶׁר־יִשָּׂא אֶת־שְׁמוֹ› (“obj-marker which lift/carry obj-marker
# name-him/its”)
# ‹לַשָּׁוְא› (“to-evil”)
# "[EN-AID] You shall not take up the name of the LORD your God in vain; for
# the LORD will not hold him guiltless who takes up His name in vain."
m.step("Exod.20.7")
# ‹לֹא תִשָּׂא אֶת־שֵׁם־יְהוָה› (“not lift/carry obj-marker name YHWH”)
# ‹אֱלֹהֶיךָ לַשָּׁוְא› (“God-you/your to-evil”)
m.statute("FORBID", "shem_la_shav")
# witness-tier presupposed read: vain_clause_oath_file on lo_tisa_et_shem —
# read, not installed
m.witness_read("lo_tisa_et_shem", "vain_clause_oath_file",
                cites=["Shevuot 20b:5", "Shevuot 20b:6", "Shevuot 20b:7", "Shevuot 20b:8", "Shevuot 20b:9", "Shevuot 20b:10", "Shevuot 21a:5", "Shevuot 21a:6", "Shevuot 21a:7", "Shevuot 29a:12", "Shevuot 29a:13", "Shevuot 29a:14"])

# -------------------------- Exod.20.8 · REMEMBER_THE_SABBATH ---------------
# ‹זָכוֹר אֶת־יוֹם הַשַּׁבָּת› (“mark obj-marker day the-intermission”)
# ‹לְקַדְּשׁוֹ› (“to-sanctify-him/its”)
# "[EN-AID] Remember the sabbath day, to keep it holy."
m.step("Exod.20.8")
# ‹זָכוֹר אֶת־יוֹם הַשַּׁבָּת› (“mark obj-marker day the-intermission”)
# ‹לְקַדְּשׁוֹ› (“to-sanctify-him/its”)
m.statute("BIND", "zakhor_et_yom_ha_shabat")
# witness-tier presupposed read: kiddush_file on zakhor_et_yom_ha_shabat —
# read, not installed
m.witness_read("zakhor_et_yom_ha_shabat", "kiddush_file",
                cites=["Pesachim 106a:5", "Pesachim 106a:6", "Pesachim 106a:7", "Pesachim 117b:8", "Berakhot 20b:7", "Berakhot 20b:8", "Berakhot 20b:9", "Berakhot 20b:10", "Berakhot 20b:11", "Berakhot 20b:12", "Berakhot 20b:13", "Berakhot 20b:14"])

# -------------------------- Exod.20.9 · SIX_DAYS_SHALL_YOU_LABOR -----------
# ‹שֵׁשֶׁת יָמִים תַּעֲבֹד› (“six day work/serve”)
# ‹וְעָשִׂיתָ כָּל־מְלַאכְתֶּךָ› (“and-make all work-you/your”)
# "[EN-AID] Six days shall you labor, and do all your work."
m.step("Exod.20.9")
# ‹שֵׁשֶׁת יָמִים תַּעֲבֹד› (“six day work/serve”)
# ‹וְעָשִׂיתָ› (“and-make”)
# — fact holds: six-day-work/serve
m.fact("sheshet_yamim_taavod")

# -------------------------- Exod.20.10 · THE_SEVENTH_IS_REST ---------------
# ‹וְיוֹם הַשְּׁבִיעִי שַׁבָּת› (“and-day the-seventh intermission”)
# ‹לַיהוָה אֱלֹהֶיךָ לֹא־תַעֲשֶׂה› (“to-YHWH God-you/your not make”)
# ‹כָל־מְלָאכָה אַתָּה וּבִנְךָ־וּבִתֶּךָ› (“all work you and-son-you/your
# and-daughter-you/your”)
# ‹עַבְדְּךָ וַאֲמָתְךָ וּבְהֶמְתֶּךָ› (“servant-you/your and-maidservant-
# you/your and-livestock-you/your”)
# ‹וְגֵרְךָ אֲשֶׁר בִּשְׁעָרֶיךָ› (“and-sojourner-you/your which in-gate-
# you/your”)
# "[EN-AID] And the seventh day is a sabbath to the LORD your God; you shall
# not do any work — you, and your son and your daughter, your servant and
# your maid, and your beast, and your stranger who is within your gates."
m.step("Exod.20.10")
# ‹אַתָּה וּבִנְךָ־וּבִתֶּךָ עַבְדְּךָ› (“you and-son-you/your and-daughter-
# you/your servant-you/your”)
# ‹וַאֲמָתְךָ וּבְהֶמְתֶּךָ וְגֵרְךָ› (“and-maidservant-you/your and-
# livestock-you/your and-sojourner-you/your”)
# — fact holds: intermission-to-the-LORD-elohekha
m.fact("shabat_la_YHWH_elohekha")
# witness-tier presupposed read: recorded_runs on rest_roster — read, not
# installed
m.witness_read("rest_roster", "recorded_runs",
                cites=["Bava Kamma 54b:13", "Bava Kamma 54b:14", "Shabbat 153b:7", "Shabbat 153b:8", "Shabbat 120b:11", "Shabbat 120b:12", "Shabbat 117b:8", "Bava Metzia 32a:15", "Bava Metzia 32a:16"])

# -------------------------- Exod.20.11 · THE_CREATION_WARRANT --------------
# ‹כִּי שֵׁשֶׁת־יָמִים עָשָׂה› (“that six day make”)
# ‹יְהוָה אֶת־הַשָּׁמַיִם וְאֶת־הָאָרֶץ› (“YHWH obj-marker the-heavens and-
# obj-marker the-earth”)
# ‹אֶת־הַיָּם וְאֶת־כָּל־אֲשֶׁר־בָּם וַיָּנַח› (“obj-marker the-seas and-
# obj-marker all which in-them/their and-rest”)
# ‹בַּיּוֹם הַשְּׁבִיעִי עַל־כֵּן› (“in-day the-seventh over so”)
# ‹בֵּרַךְ יְהוָה אֶת־יוֹם› (“bless YHWH obj-marker day”)
# ‹הַשַּׁבָּת וַיְקַדְּשֵׁהוּ› (“the-intermission and-sanctify-him/its”)
# "[EN-AID] For six days the LORD made the heavens and the earth, the sea
# and all that is in them, and He rested on the seventh day; therefore the
# LORD blessed the sabbath day, and sanctified it."
m.step("Exod.20.11")
# ‹עַל־כֵּן בֵּרַךְ יְהוָה› (“over so bless YHWH”)
# ‹אֶת־יוֹם הַשַּׁבָּת וַיְקַדְּשֵׁהוּ› (“obj-marker day the-intermission
# and-sanctify-him/its”)
# — fact holds: over-so-bless-the-LORD
m.fact("al_ken_berakh_YHWH")

# -------------------------- Exod.20.12 · HONOR_FATHER_AND_MOTHER -----------
# ‹כַּבֵּד אֶת־אָבִיךָ וְאֶת־אִמֶּךָ› (“be-heavy obj-marker father-you/your
# and-obj-marker mother-you/your”)
# ‹לְמַעַן יַאֲרִכוּן יָמֶיךָ› (“so-that be-long-ward day-you/your”)
# ‹עַל הָאֲדָמָה אֲשֶׁר־יְהוָה› (“over the-ground which YHWH”)
# ‹אֱלֹהֶיךָ נֹתֵן לָךְ› (“God-you/your set to-you/your”)
# "[EN-AID] Honor your father and your mother — that your days may be long
# on the land which the LORD your God gives you."
m.step("Exod.20.12")
# ‹כַּבֵּד אֶת־אָבִיךָ וְאֶת־אִמֶּךָ› (“be-heavy obj-marker father-you/your
# and-obj-marker mother-you/your”)
m.statute("BIND", "kabed_av_va_em")
# witness-tier presupposed read: equal_weight on honor_utterance — read, not
# installed
m.witness_read("honor_utterance", "equal_weight",
                cites=["Mishnah Keritot 6:9"])

# -------------------------- Exod.20.13 · NO_MURDER -------------------------
# ‹לֹא תִּרְצָח› (“not dash-in-pieces”)
# "[EN-AID] You shall not murder."
m.step("Exod.20.13")
# ‹לֹא תִּרְצָח› (“not dash-in-pieces”)
m.statute("FORBID", "retzach")
# witness-tier presupposed read: plotting_rows on false_witness_utterance —
# read, not installed
m.witness_read("false_witness_utterance", "plotting_rows",
                cites=["Mishnah Makkot 1:2", "Mishnah Makkot 1:3"])

# -------------------------- Exod.20.14 · NO_ADULTERY -----------------------
# ‹לֹא תִּנְאָף› (“not commit-adultery”)
# "[EN-AID] You shall not commit adultery."
m.step("Exod.20.14")
# ‹לֹא תִּנְאָף› (“not commit-adultery”)
m.statute("FORBID", "niuf")

# -------------------------- Exod.20.15 · NO_THEFT --------------------------
# ‹לֹא תִּגְנֹב› (“not steal”)
# "[EN-AID] You shall not steal."
m.step("Exod.20.15")
# ‹לֹא תִּגְנֹב› (“not steal”)
m.statute("FORBID", "geneva")

# -------------------------- Exod.20.16 · NO_FALSE_WITNESS ------------------
# ‹לֹא־תַעֲנֶה בְרֵעֲךָ עֵד› (“not eye in-associate-you/your concretely”)
# ‹שָׁקֶר› (“untruth”)
# "[EN-AID] You shall not answer against your fellow as a false witness."
m.step("Exod.20.16")
# ‹לֹא־תַעֲנֶה בְרֵעֲךָ עֵד› (“not eye in-associate-you/your concretely”)
# ‹שָׁקֶר› (“untruth”)
m.statute("FORBID", "ed_shaqer")

# -------------------------- Exod.20.17 · NO_COVETING -----------------------
# ‹לֹא תַחְמֹד בֵּית› (“not delight-in house”)
# ‹רֵעֶךָ לֹא־תַחְמֹד אֵשֶׁת› (“associate-you/your not delight-in woman”)
# ‹רֵעֶךָ וְעַבְדּוֹ וַאֲמָתוֹ› (“associate-you/your and-servant-him/its
# and-maidservant-him/its”)
# ‹וְשׁוֹרוֹ וַחֲמֹרוֹ וְכֹל› (“and-bullock-him/its and-male-ass-him/its
# and-all”)
# ‹אֲשֶׁר לְרֵעֶךָ› (“which to-associate-you/your”)
# "[EN-AID] You shall not covet your fellow's house; you shall not covet
# your fellow's wife, or his servant, or his maid, or his ox, or his donkey,
# or anything that is your fellow's."
m.step("Exod.20.17")
# ‹לֹא תַחְמֹד בֵּית› (“not delight-in house”)
# ‹רֵעֶךָ› (“associate-you/your”)
m.statute("FORBID", "chimud")

# -------------------------- Exod.20.18 · SEEING_THE_VOICES -----------------
# ‹וְכָל־הָעָם רֹאִים אֶת־הַקּוֹלֹת› (“and-all the-people see obj-marker
# the-voice/sound”)
# ‹וְאֶת־הַלַּפִּידִם וְאֵת קוֹל› (“and-obj-marker the-flambeau and-obj-
# marker voice/sound”)
# ‹הַשֹּׁפָר וְאֶת־הָהָר עָשֵׁן› (“the-cornet and-obj-marker the-mountain
# smoky”)
# ‹וַיַּרְא הָעָם וַיָּנֻעוּ› (“and-see the-people and-waver”)
# ‹וַיַּעַמְדוּ מֵרָחֹק› (“and-stand from-remote”)
# "[EN-AID] And all the people were seeing the voices and the torches, and
# the voice of the shofar, and the mountain smoking; and the people saw, and
# they swayed, and stood far off."
m.step("Exod.20.18")
# ‹וְכָל־הָעָם רֹאִים אֶת־הַקּוֹלֹת› (“and-all the-people see obj-marker
# the-voice/sound”)
# ‹וְאֶת־הַלַּפִּידִם וְאֵת קוֹל› (“and-obj-marker the-flambeau and-obj-
# marker voice/sound”)
# ‹הַשֹּׁפָר וְאֶת־הָהָר עָשֵׁן› (“the-cornet and-obj-marker the-mountain
# smoky”)
# — event: see-obj-marker-the-voice/sound — theme ha-qolot
m.event("roim_et_ha_qolot", themes=["ha-qolot"])

# -------------------------- Exod.20.19 · SPEAK_YOU_WITH_US -----------------
# ‹וַיֹּאמְרוּ אֶל־מֹשֶׁה דַּבֵּר־אַתָּה› (“and-say to Moses speak you”)
# ‹עִמָּנוּ וְנִשְׁמָעָה וְאַל־יְדַבֵּר› (“with-us/our and-hear and-do-not
# speak”)
# ‹עִמָּנוּ אֱלֹהִים פֶּן־נָמוּת› (“with-us/our God lest die”)
# "[EN-AID] And they said to Moses: Speak you with us, and we will hear; and
# let God not speak with us, lest we die."
m.step("Exod.20.19")
# ‹דַּבֵּר־אַתָּה עִמָּנוּ וְנִשְׁמָעָה› (“speak you with-us/our and-hear”)
# — the-people speaks a demand — LET: speak-you-imanu
m.declare("ha_am", "LET",
          "daber_ata_imanu")

# -------------------------- Exod.20.20 · FEAR_NOT_THE_TEST -----------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־הָעָם› (“and-say Moses to the-people”)
# ‹אַל־תִּירָאוּ כִּי לְבַעֲבוּר› (“do-not fear that to-in-crossed”)
# ‹נַסּוֹת אֶתְכֶם בָּא› (“test obj-marker-you/your(pl) come/bring”)
# ‹הָאֱלֹהִים וּבַעֲבוּר תִּהְיֶה› (“the-God and-in-crossed be”)
# ‹יִרְאָתוֹ עַל־פְּנֵיכֶם לְבִלְתִּי› (“fear-him/its over face-you/your(pl)
# to-failure-of”)
# ‹תֶחֱטָאוּ› (“sin”)
# "[EN-AID] And Moses said to the people: Fear not, for in order to test you
# God has come — and in order that His fear be on your faces, that you sin
# not."
m.step("Exod.20.20")
# ‹כִּי לְבַעֲבוּר נַסּוֹת› (“that to-in-crossed test”)
# ‹אֶתְכֶם בָּא הָאֱלֹהִים› (“obj-marker-you/your(pl) come/bring the-God”)
# — fact holds: to-vaavur-test-etkhem
m.fact("le_vaavur_nasot_etkhem")

# -------------------------- Exod.20.21 · INTO_THE_THICK_CLOUD --------------
# ‹וַיַּעֲמֹד הָעָם מֵרָחֹק› (“and-stand the-people from-remote”)
# ‹וּמֹשֶׁה נִגַּשׁ אֶל־הָעֲרָפֶל› (“and-Moses be to the-gloom”)
# ‹אֲשֶׁר־שָׁם הָאֱלֹהִים› (“which there the-God”)
# "[EN-AID] And the people stood far off — and Moses drew near to the thick
# cloud where God was."
m.step("Exod.20.21")
# ‹וּמֹשֶׁה נִגַּשׁ אֶל־הָעֲרָפֶל› (“and-Moses be to the-gloom”)
# ‹אֲשֶׁר־שָׁם הָאֱלֹהִים› (“which there the-God”)
# — demand settled (popped from the queue): speak-you-imanu
m.result("daber_ata_imanu", tmark="t1")
# witness-tier presupposed read: standing_rows on altar_speech — read, not
# installed
m.witness_read("altar_speech", "standing_rows",
                cites=["Mishnah Chagigah 3:8", "Pirkei Avot 3:6", "Mishnah Tamid 5:1", "Mishnah Shabbat 24:1"])

# -------------------------- Exod.20.22 · FROM_THE_HEAVENS ------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹כֹּה תֹאמַר אֶל־בְּנֵי› (“like-this say to son”)
# ‹יִשְׂרָאֵל אַתֶּם רְאִיתֶם› (“Israel you see”)
# ‹כִּי מִן־הַשָּׁמַיִם דִּבַּרְתִּי› (“that from the-heavens speak”)
# ‹עִמָּכֶם› (“with-you/your(pl)”)
# "[EN-AID] And the LORD said to Moses: So shall you say to the sons of
# Israel: You have seen that from the heavens I spoke with you."
m.step("Exod.20.22")
# ‹אַתֶּם רְאִיתֶם כִּי› (“you see that”)
# ‹מִן־הַשָּׁמַיִם דִּבַּרְתִּי עִמָּכֶם› (“from the-heavens speak with-
# you/your(pl)”)
# — fact holds: from-the-heavens-speak
m.fact("min_ha_shamayim_dibarti")

# -------------------------- Exod.20.23 · NO_GODS_OF_SILVER -----------------
# ‹לֹא תַעֲשׂוּן אִתִּי› (“not make-ward with-me/my”)
# ‹אֱלֹהֵי כֶסֶף וֵאלֹהֵי› (“God silver and-God”)
# ‹זָהָב לֹא תַעֲשׂוּ› (“gold not make”)
# ‹לָכֶם› (“to-you/your(pl)”)
# "[EN-AID] You shall not make with Me gods of silver, and gods of gold you
# shall not make for yourselves."
m.step("Exod.20.23")
# ‹לֹא תַעֲשׂוּן אִתִּי› (“not make-ward with-me/my”)
# ‹אֱלֹהֵי כֶסֶף וֵאלֹהֵי› (“God silver and-God”)
# ‹זָהָב› (“gold”)
m.statute("FORBID", "elohe_khesef_ve_zahav")
# witness-tier presupposed read: image_making_scope_machine on lo_taasun_iti
# — read, not installed
m.witness_read("lo_taasun_iti", "image_making_scope_machine",
                cites=["Rosh Hashanah 24a:18", "Rosh Hashanah 24a:19", "Rosh Hashanah 24a:20", "Rosh Hashanah 24b:1", "Rosh Hashanah 24b:2", "Rosh Hashanah 24b:3", "Rosh Hashanah 24b:4", "Rosh Hashanah 24b:5", "Rosh Hashanah 24b:6", "Rosh Hashanah 24b:7", "Rosh Hashanah 24b:8", "Rosh Hashanah 24b:9", "Rosh Hashanah 24b:10", "Rosh Hashanah 24b:11", "Rosh Hashanah 24b:12", "Rosh Hashanah 24b:13", "Avodah Zarah 43b:4", "Avodah Zarah 43b:5", "Avodah Zarah 43b:6", "Avodah Zarah 43b:7", "Avodah Zarah 43b:8", "Avodah Zarah 43b:9", "Avodah Zarah 43b:10", "Avodah Zarah 43b:11", "Avodah Zarah 43b:12", "Avodah Zarah 43b:13", "Avodah Zarah 43b:14", "Avodah Zarah 43b:15", "Avodah Zarah 54a:3", "Avodah Zarah 54a:4", "Avodah Zarah 54a:5"])

# -------------------------- Exod.20.24 · AN_ALTAR_OF_EARTH -----------------
# ‹מִזְבַּח אֲדָמָה תַּעֲשֶׂה־לִּי› (“altar ground make to-me/my”)
# ‹וְזָבַחְתָּ עָלָיו אֶת־עֹלֹתֶיךָ› (“and-slaughter-an-animal over-him/its
# obj-marker burnt-offering-you/your”)
# ‹וְאֶת־שְׁלָמֶיךָ אֶת־צֹאנְךָ וְאֶת־בְּקָרֶךָ› (“and-obj-marker requital-
# you/your obj-marker flock-you/your and-obj-marker herd-you/your”)
# ‹בְּכָל־הַמָּקוֹם אֲשֶׁר אַזְכִּיר› (“in-all the-place which mark”)
# ‹אֶת־שְׁמִי אָבוֹא אֵלֶיךָ› (“obj-marker name-me/my come/bring to-
# you/your”)
# ‹וּבֵרַכְתִּיךָ› (“and-bless-you/your”)
# "[EN-AID] An altar of earth shall you make for Me, and you shall sacrifice
# on it your burnt-offerings and your peace-offerings, your flock and your
# herd; in every place where I cause My name to be mentioned, I will come to
# you and bless you."
m.step("Exod.20.24")
# ‹מִזְבַּח אֲדָמָה תַּעֲשֶׂה־לִּי› (“altar ground make to-me/my”)
m.statute("BIND", "mizbach_adama")
# witness-tier presupposed read: name_mention_dual_law on
# be_khol_ha_maqom_asher_azkir — read, not installed
m.witness_read("be_khol_ha_maqom_asher_azkir", "name_mention_dual_law",
                cites=["Sotah 38a:9", "Sotah 38a:10", "Sotah 38a:11", "Sotah 38a:12", "Sotah 38a:13", "Berakhot 6a:13", "Berakhot 6a:14", "Berakhot 54a:9"])
# witness-tier presupposed read: altar_paragraph_babylonian_layer on
# ve_zavachta_alav — read, not installed
m.witness_read("ve_zavachta_alav", "altar_paragraph_babylonian_layer",
                cites=["Zevachim 54a:7", "Zevachim 54a:8", "Zevachim 54a:9", "Zevachim 58a:4", "Zevachim 58a:5", "Zevachim 58a:6", "Zevachim 59a:10", "Zevachim 59a:11", "Zevachim 59a:12", "Zevachim 61b:3", "Zevachim 61b:4", "Zevachim 61b:5"])

# -------------------------- Exod.20.25 · NO_HEWN_STONES --------------------
# ‹וְאִם־מִזְבַּח אֲבָנִים תַּעֲשֶׂה־לִּי› (“and-if altar stone make to-
# me/my”)
# ‹לֹא־תִבְנֶה אֶתְהֶן גָּזִית› (“not build obj-marker-them/their something-
# cut”)
# ‹כִּי חַרְבְּךָ הֵנַפְתָּ› (“that drought-you/your quiver”)
# ‹עָלֶיהָ וַתְּחַלְלֶהָ› (“over-her/its and-bore-her/its”)
# "[EN-AID] And if an altar of stones you make for Me, you shall not build
# them hewn; for you have lifted your sword upon it, and profaned it."
m.step("Exod.20.25")
# ‹לֹא־תִבְנֶה אֶתְהֶן גָּזִית› (“not build obj-marker-them/their something-
# cut”)
m.statute("FORBID", "gazit")

# -------------------------- Exod.20.26 · NO_STEPS --------------------------
# ‹וְלֹא־תַעֲלֶה בְמַעֲלֹת עַל־מִזְבְּחִי› (“and-not go-up in-Most-High over
# altar-me/my”)
# ‹אֲשֶׁר לֹא־תִגָּלֶה עֶרְוָתְךָ› (“which not denude nudity-you/your”)
# ‹עָלָיו› (“over-him/its”)
# "[EN-AID] And you shall not go up by steps onto My altar — that your
# nakedness be not uncovered on it."
m.step("Exod.20.26")
# ‹וְלֹא־תַעֲלֶה בְמַעֲלֹת עַל־מִזְבְּחִי› (“and-not go-up in-Most-High over
# altar-me/my”)
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('poqed_avon_avot', 'utterance_rider_file'), ('lo_tisa_et_shem', 'vain_clause_oath_file'), ('zakhor_et_yom_ha_shabat', 'kiddush_file'), ('rest_roster', 'recorded_runs'), ('honor_utterance', 'equal_weight'), ('false_witness_utterance', 'plotting_rows'), ('altar_speech', 'standing_rows'), ('lo_taasun_iti', 'image_making_scope_machine'), ('be_khol_ha_maqom_asher_azkir', 'name_mention_dual_law'), ('ve_zavachta_alav', 'altar_paragraph_babylonian_layer')]
    assert m.WITNESS_READS[0]["cites"] == ['Berakhot 7a:26', 'Berakhot 7a:27', 'Sanhedrin 99a:20', 'Sanhedrin 99a:21', 'Bava Metzia 5b:18', 'Bava Metzia 5b:19', 'Bava Metzia 5b:20', 'Beitzah 15b:4', 'Beitzah 15b:5', 'Bava Kamma 74b:7', 'Bava Kamma 74b:8', 'Bava Kamma 74b:9', 'Sanhedrin 86a:15', 'Sanhedrin 86a:16', 'Sanhedrin 86a:17']
    assert all('utterance_rider_file' not in f for f in m.WORLD["facts"])
    assert 'poqed_avon_avot' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Shevuot 20b:5', 'Shevuot 20b:6', 'Shevuot 20b:7', 'Shevuot 20b:8', 'Shevuot 20b:9', 'Shevuot 20b:10', 'Shevuot 21a:5', 'Shevuot 21a:6', 'Shevuot 21a:7', 'Shevuot 29a:12', 'Shevuot 29a:13', 'Shevuot 29a:14']
    assert all('vain_clause_oath_file' not in f for f in m.WORLD["facts"])
    assert 'lo_tisa_et_shem' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Pesachim 106a:5', 'Pesachim 106a:6', 'Pesachim 106a:7', 'Pesachim 117b:8', 'Berakhot 20b:7', 'Berakhot 20b:8', 'Berakhot 20b:9', 'Berakhot 20b:10', 'Berakhot 20b:11', 'Berakhot 20b:12', 'Berakhot 20b:13', 'Berakhot 20b:14']
    assert all('kiddush_file' not in f for f in m.WORLD["facts"])
    assert 'zakhor_et_yom_ha_shabat' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bava Kamma 54b:13', 'Bava Kamma 54b:14', 'Shabbat 153b:7', 'Shabbat 153b:8', 'Shabbat 120b:11', 'Shabbat 120b:12', 'Shabbat 117b:8', 'Bava Metzia 32a:15', 'Bava Metzia 32a:16']
    assert all('recorded_runs' not in f for f in m.WORLD["facts"])
    assert 'rest_roster' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mishnah Keritot 6:9']
    assert all('equal_weight' not in f for f in m.WORLD["facts"])
    assert 'honor_utterance' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Makkot 1:2', 'Mishnah Makkot 1:3']
    assert all('plotting_rows' not in f for f in m.WORLD["facts"])
    assert 'false_witness_utterance' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Mishnah Chagigah 3:8', 'Pirkei Avot 3:6', 'Mishnah Tamid 5:1', 'Mishnah Shabbat 24:1']
    assert all('standing_rows' not in f for f in m.WORLD["facts"])
    assert 'altar_speech' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Rosh Hashanah 24a:18', 'Rosh Hashanah 24a:19', 'Rosh Hashanah 24a:20', 'Rosh Hashanah 24b:1', 'Rosh Hashanah 24b:2', 'Rosh Hashanah 24b:3', 'Rosh Hashanah 24b:4', 'Rosh Hashanah 24b:5', 'Rosh Hashanah 24b:6', 'Rosh Hashanah 24b:7', 'Rosh Hashanah 24b:8', 'Rosh Hashanah 24b:9', 'Rosh Hashanah 24b:10', 'Rosh Hashanah 24b:11', 'Rosh Hashanah 24b:12', 'Rosh Hashanah 24b:13', 'Avodah Zarah 43b:4', 'Avodah Zarah 43b:5', 'Avodah Zarah 43b:6', 'Avodah Zarah 43b:7', 'Avodah Zarah 43b:8', 'Avodah Zarah 43b:9', 'Avodah Zarah 43b:10', 'Avodah Zarah 43b:11', 'Avodah Zarah 43b:12', 'Avodah Zarah 43b:13', 'Avodah Zarah 43b:14', 'Avodah Zarah 43b:15', 'Avodah Zarah 54a:3', 'Avodah Zarah 54a:4', 'Avodah Zarah 54a:5']
    assert all('image_making_scope_machine' not in f for f in m.WORLD["facts"])
    assert 'lo_taasun_iti' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sotah 38a:9', 'Sotah 38a:10', 'Sotah 38a:11', 'Sotah 38a:12', 'Sotah 38a:13', 'Berakhot 6a:13', 'Berakhot 6a:14', 'Berakhot 54a:9']
    assert all('name_mention_dual_law' not in f for f in m.WORLD["facts"])
    assert 'be_khol_ha_maqom_asher_azkir' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Zevachim 54a:7', 'Zevachim 54a:8', 'Zevachim 54a:9', 'Zevachim 58a:4', 'Zevachim 58a:5', 'Zevachim 58a:6', 'Zevachim 59a:10', 'Zevachim 59a:11', 'Zevachim 59a:12', 'Zevachim 61b:3', 'Zevachim 61b:4', 'Zevachim 61b:5']
    assert all('altar_paragraph_babylonian_layer' not in f for f in m.WORLD["facts"])
    assert 've_zavachta_alav' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
