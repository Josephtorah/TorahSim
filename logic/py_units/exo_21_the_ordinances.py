#!/usr/bin/env python3
# =============================================================================
# exo_21_the_ordinances — 21:1-37
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_21_the_ordinances.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The ordinances (21:1-37)"""
from machine import Machine

m = Machine("exo_21_the_ordinances")

# -------------------------- Exod.21.1 · AND_THESE_ARE_THE_ORDINANCES -------
# ‹וְאֵלֶּה הַמִּשְׁפָּטִים אֲשֶׁר› (“and-these the-judgment which”)
# ‹תָּשִׂים לִפְנֵיהֶם› (“put/set to-face-them/their”)
# "[EN-AID] And these are the ordinances which you shall set before them."
m.step("Exod.21.1")
# ‹וְאֵלֶּה הַמִּשְׁפָּטִים אֲשֶׁר› (“and-these the-judgment which”)
# ‹תָּשִׂים לִפְנֵיהֶם› (“put/set to-face-them/their”)
# — fact holds: and-these-the-judgment
m.fact("ve_ele_ha_mishpatim")

# -------------------------- Exod.21.2 · THE_HEBREW_SLAVE -------------------
# ‹כִּי תִקְנֶה עֶבֶד› (“that possessor servant”)
# ‹עִבְרִי שֵׁשׁ שָׁנִים› (“Hebrew six years”)
# ‹יַעֲבֹד וּבַשְּׁבִעִת יֵצֵא› (“work/serve and-in-seventh bring-forth”)
# ‹לַחָפְשִׁי חִנָּם› (“to-exempt gratis”)
# "[EN-AID] When you acquire a Hebrew slave, six years he shall serve; and
# in the seventh he shall go out free, for nothing."
m.step("Exod.21.2")
# ‹כִּי תִקְנֶה עֶבֶד› (“that possessor servant”)
# ‹עִבְרִי› (“Hebrew”)
# — case that possessor servant Hebrew routes to servant-Hebrew
m.case("ki tiqne eved ivri", "eved_ivri")
# witness-tier presupposed read: the_codes_first_case on
# case_syntax_and_release_list — read, not installed
m.witness_read("case_syntax_and_release_list", "the_codes_first_case",
                cites=["Gittin 90a:10", "Mekhilta DeRabbi Yishmael, Tractate Bachodesh 11:11", "Mishnah Kiddushin 1:2", "Kiddushin 16a:11", "Kiddushin 15a:19"])
# witness-tier presupposed read: calendar_semantics_and_family_law on
# slave_clock — read, not installed
m.witness_read("slave_clock", "calendar_semantics_and_family_law",
                cites=["Niddah 48a:2", "Kiddushin 17a:1", "Kiddushin 18a:8", "Kiddushin 19a:8", "Sotah 23b:9", "Bekhorot 50b:7", "Yevamot 70a:5", "Temurah 25b:4", "Bava Batra 50a:8"])

# -------------------------- Exod.21.3 · AS_HE_CAME -------------------------
# ‹אִם־בְּגַפּוֹ יָבֹא בְּגַפּוֹ› (“if in-back-him/its come/bring in-back-
# him/its”)
# ‹יֵצֵא אִם־בַּעַל אִשָּׁה› (“bring-forth if master woman”)
# ‹הוּא וְיָצְאָה אִשְׁתּוֹ› (“he/it and-bring-forth woman-him/its”)
# ‹עִמּוֹ› (“with-him/its”)
# "[EN-AID] If he came in by himself, he shall go out by himself; if he was
# the husband of a wife, then his wife shall go out with him."
m.step("Exod.21.3")
# ‹אִם־בְּגַפּוֹ יָבֹא בְּגַפּוֹ› (“if in-back-him/its come/bring in-back-
# him/its”)
# ‹יֵצֵא› (“bring-forth”)
# — fact holds: in-gapo-come/bring-in-gapo-bring-forth
m.fact("be_gapo_yavo_be_gapo_yetze")

# -------------------------- Exod.21.4 · THE_MASTERS_WIFE -------------------
# ‹אִם־אֲדֹנָיו יִתֶּן־לוֹ אִשָּׁה› (“if lord-him/its set to-him/its woman”)
# ‹וְיָלְדָה־לוֹ בָנִים אוֹ› (“and-bear-young to-him/its son or”)
# ‹בָנוֹת הָאִשָּׁה וִילָדֶיהָ› (“daughter the-woman and-child-her/its”)
# ‹תִּהְיֶה לַאדֹנֶיהָ וְהוּא› (“be to-lord-her/its and-he/it”)
# ‹יֵצֵא בְגַפּוֹ› (“bring-forth in-back-him/its”)
# "[EN-AID] If his master gives him a wife, and she bears him sons or
# daughters — the wife and her children shall be her master's, and he shall
# go out by himself."
m.step("Exod.21.4")
# ‹הָאִשָּׁה וִילָדֶיהָ תִּהְיֶה› (“the-woman and-child-her/its be”)
# ‹לַאדֹנֶיהָ וְהוּא יֵצֵא› (“to-lord-her/its and-he/it bring-forth”)
# ‹בְגַפּוֹ› (“in-back-him/its”)
# — fact holds: the-woman-vi-yladeha-be-to-adoneha
m.fact("ha_isha_vi_yladeha_tihye_la_adoneha")

# -------------------------- Exod.21.5 · I_LOVE_MY_MASTER -------------------
# ‹וְאִם־אָמֹר יֹאמַר הָעֶבֶד› (“and-if say say the-servant”)
# ‹אָהַבְתִּי אֶת־אֲדֹנִי אֶת־אִשְׁתִּי› (“have-affection-for obj-marker
# lord-me/my obj-marker woman-me/my”)
# ‹וְאֶת־בָּנָי לֹא אֵצֵא› (“and-obj-marker son-me/my not bring-forth”)
# ‹חָפְשִׁי› (“exempt”)
# "[EN-AID] And if the slave shall plainly say: I love my master, my wife,
# and my sons — I will not go out free."
m.step("Exod.21.5")
# ‹אָמֹר יֹאמַר הָעֶבֶד› (“say say the-servant”)
# ‹אָהַבְתִּי אֶת־אֲדֹנִי אֶת־אִשְׁתִּי› (“have-affection-for obj-marker
# lord-me/my obj-marker woman-me/my”)
# ‹וְאֶת־בָּנָי› (“and-obj-marker son-me/my”)
# — fact holds: have-affection-for-obj-marker-adoni
m.fact("ahavti_et_adoni")

# -------------------------- Exod.21.6 · THE_AWL_AND_THE_DOOR ---------------
# ‹וְהִגִּישׁוֹ אֲדֹנָיו אֶל־הָאֱלֹהִים› (“and-be-him/its lord-him/its to
# the-God”)
# ‹וְהִגִּישׁוֹ אֶל־הַדֶּלֶת אוֹ› (“and-be-him/its to the-something-swinging
# or”)
# ‹אֶל־הַמְּזוּזָה וְרָצַע אֲדֹנָיו› (“to the-door-post and-pierce lord-
# him/its”)
# ‹אֶת־אָזְנוֹ בַּמַּרְצֵעַ וַעֲבָדוֹ› (“obj-marker broadness.-i.e.-the-ear-
# him/its in-awl and-work/serve-him/its”)
# ‹לְעֹלָם› (“to-forever”)
# "[EN-AID] Then his master shall bring him to God, and bring him to the
# door, or to the doorpost; and his master shall pierce his ear with the awl
# — and he shall serve him forever."
m.step("Exod.21.6")
# ‹וְרָצַע אֲדֹנָיו אֶת־אָזְנוֹ› (“and-pierce lord-him/its obj-marker
# broadness.-i.e.-the-ear-him/its”)
# ‹בַּמַּרְצֵעַ וַעֲבָדוֹ לְעֹלָם› (“in-awl and-work/serve-him/its to-
# forever”)
# — standing handler — if say say the-servant have-affection-for then and-
# pierce obj-marker-azno in-the-martzea, and-avado to-forever
m.handler("amor yomar ha-eved ahavti",
          "ve-ratza et-azno ba-martzea, va-avado le-olam")

# -------------------------- Exod.21.7 · THE_DAUGHTER_SOLD ------------------
# ‹וְכִי־יִמְכֹּר אִישׁ אֶת־בִּתּוֹ› (“and-that sell man obj-marker
# daughter-him/its”)
# ‹לְאָמָה לֹא תֵצֵא› (“to-maidservant not bring-forth”)
# ‹כְּצֵאת הָעֲבָדִים› (“like-bring-forth the-servant”)
# "[EN-AID] And when a man sells his daughter as a maidservant, she shall
# not go out as the slaves go out."
m.step("Exod.21.7")
# ‹וְכִי־יִמְכֹּר אִישׁ אֶת־בִּתּוֹ› (“and-that sell man obj-marker
# daughter-him/its”)
# ‹לְאָמָה› (“to-maidservant”)
# — case and-khi sell man obj-marker bito to-maidservant routes to
# maidservant-ivriya
m.case("ve-khi yimkor ish et bito le-ama", "ama_ivriya")

# -------------------------- Exod.21.8 · THE_QERE_OF_MERCY ------------------
# ‹אִם־רָעָה בְּעֵינֵי אֲדֹנֶיהָ› (“if bad in-eye lord-her/its”)
# ‹אֲשֶׁר־לא לוֹ יְעָדָהּ› (“which not to-him/its fix-upon-her/its”)
# ‹וְהֶפְדָּהּ לְעַם נָכְרִי› (“and-sever-her/its to-people strange”)
# ‹לֹא־יִמְשֹׁל לְמָכְרָהּ בְּבִגְדוֹ־בָהּ› (“not rule to-sell-her/its in-
# cover-him/its in-her/its”)
# "[EN-AID] If she is bad in the eyes of her master, who has not designated
# her — then he shall let her be redeemed; to a foreign people he shall not
# rule to sell her, since he has dealt treacherously with her."
m.step("Exod.21.8")
# ‹אֲשֶׁר־לא לוֹ יְעָדָהּ› (“which not to-him/its fix-upon-her/its”)
# ‹וְהֶפְדָּהּ› (“and-sever-her/its”)
# — fact holds: and-hefda
m.fact("ve_hefda")

# -------------------------- Exod.21.9 · AS_THE_DAUGHTERS -------------------
# ‹וְאִם־לִבְנוֹ יִיעָדֶנָּה כְּמִשְׁפַּט› (“and-if to-son-him/its fix-upon-
# her/its like-judgment”)
# ‹הַבָּנוֹת יַעֲשֶׂה־לָּהּ› (“the-daughter make to-her/its”)
# "[EN-AID] And if he designates her for his son — according to the
# ordinance of the daughters he shall do for her."
m.step("Exod.21.9")
# ‹כְּמִשְׁפַּט הַבָּנוֹת יַעֲשֶׂה־לָּהּ› (“like-judgment the-daughter make
# to-her/its”)
# — fact holds: like-judgment-the-daughter
m.fact("ke_mishpat_ha_banot")

# -------------------------- Exod.21.10 · HER_THREE_RIGHTS ------------------
# ‹אִם־אַחֶרֶת יִקַּח־לוֹ שְׁאֵרָהּ› (“if other take to-him/its flesh-
# her/its”)
# ‹כְּסוּתָהּ וְעֹנָתָהּ לֹא› (“cover-her/its and-sexual-her/its not”)
# ‹יִגְרָע› (“scrape-off”)
# "[EN-AID] If he takes himself another — her flesh, her covering, and her
# season he shall not diminish."
m.step("Exod.21.10")
# ‹שְׁאֵרָהּ כְּסוּתָהּ וְעֹנָתָהּ› (“flesh-her/its cover-her/its and-
# sexual-her/its”)
# ‹לֹא יִגְרָע› (“not scrape-off”)
# — fact holds: sheera-kesuta-and-onata
m.fact("sheera_kesuta_ve_onata")

# -------------------------- Exod.21.11 · OUT_FREE_WITHOUT_MONEY ------------
# ‹וְאִם־שְׁלָשׁ־אֵלֶּה לֹא יַעֲשֶׂה› (“and-if three these not make”)
# ‹לָהּ וְיָצְאָה חִנָּם› (“to-her/its and-bring-forth gratis”)
# ‹אֵין כָּסֶף› (“there-is-not silver”)
# "[EN-AID] And if these three he does not do for her — then she shall go
# out for nothing, without money."
m.step("Exod.21.11")
# ‹וְיָצְאָה חִנָּם אֵין› (“and-bring-forth gratis there-is-not”)
# ‹כָּסֶף› (“silver”)
# — standing handler — if three these not make lah then and-bring-forth
# gratis there-is-not silver
m.handler("shelash ele lo yaase lah",
          "ve-yatza chinam en kasef")

# -------------------------- Exod.21.12 · THE_STRIKER_OF_MAN ----------------
# ‹מַכֵּה אִישׁ וָמֵת› (“strike man and-die”)
# ‹מוֹת יוּמָת› (“die die”)
# "[EN-AID] He who strikes a man, and he dies — shall surely be put to
# death."
m.step("Exod.21.12")
# ‹מַכֵּה אִישׁ וָמֵת› (“strike man and-die”)
# ‹מוֹת יוּמָת› (“die die”)
m.statute("FORBID", "makkeh_ish")

# -------------------------- Exod.21.13 · THE_PLACE_TO_FLEE -----------------
# ‹וַאֲשֶׁר לֹא צָדָה› (“and-which not chase”)
# ‹וְהָאֱלֹהִים אִנָּה לְיָדוֹ› (“and-the-God approach to-hand-him/its”)
# ‹וְשַׂמְתִּי לְךָ מָקוֹם› (“and-put/set to-you/your place”)
# ‹אֲשֶׁר יָנוּס שָׁמָּה› (“which flit there-ward”)
# "[EN-AID] And he who did not lie in wait, but God caused it to come to his
# hand — I will set for you a place where he may flee."
m.step("Exod.21.13")
# ‹וְשַׂמְתִּי לְךָ מָקוֹם› (“and-put/set to-you/your place”)
# ‹אֲשֶׁר יָנוּס שָׁמָּה› (“which flit there-ward”)
# — standing handler — if not chase, and-the-God approach to-his-hand then
# and-put/set to-you place which flit shama
m.handler("lo tzada, ve-ha-elohim ina le-yado",
          "ve-samti lekha maqom asher yanus shama")

# -------------------------- Exod.21.14 · FROM_MY_ALTAR ---------------------
# ‹וְכִי־יָזִד אִישׁ עַל־רֵעֵהוּ› (“and-that seethe man over associate-
# him/its”)
# ‹לְהָרְגוֹ בְעָרְמָה מֵעִם› (“to-smite-with-deadly-intent-him/its in-
# trickery from-with”)
# ‹מִזְבְּחִי תִּקָּחֶנּוּ לָמוּת› (“altar-me/my take-him/its to-die”)
# "[EN-AID] And when a man presumes against his fellow, to kill him by
# scheme — from My altar you shall take him, to die."
m.step("Exod.21.14")
# ‹מֵעִם מִזְבְּחִי תִּקָּחֶנּוּ› (“from-with altar-me/my take-him/its”)
# ‹לָמוּת› (“to-die”)
# — standing handler — if seethe man over reehu to-horgo and-trickery then
# from-if mizbechi tiqachenu to-die
m.handler("yazid ish al reehu le-horgo ve-arma",
          "me-im mizbechi tiqachenu la-mut")
# witness-tier presupposed read: forewarning_and_strike_grammar on
# intent_word — read, not installed
m.witness_read("intent_word", "forewarning_and_strike_grammar",
                cites=["Sanhedrin 41a:2", "Sanhedrin 84b:5", "Sanhedrin 52b:13", "Makkot 8b:14", "Bava Kamma 90b:14", "Sanhedrin 78a:19", "Sanhedrin 85b:10"])

# -------------------------- Exod.21.15 · THE_STRIKER_OF_PARENTS ------------
# ‹וּמַכֵּה אָבִיו וְאִמּוֹ› (“and-strike father-him/its and-mother-
# him/its”)
# ‹מוֹת יוּמָת› (“die die”)
# "[EN-AID] And he who strikes his father and his mother shall surely be put
# to death."
m.step("Exod.21.15")
# ‹וּמַכֵּה אָבִיו וְאִמּוֹ› (“and-strike father-him/its and-mother-
# him/its”)
# ‹מוֹת יוּמָת› (“die die”)
m.statute("FORBID", "makkeh_aviv_ve_imo")

# -------------------------- Exod.21.16 · THE_MAN_STEALER -------------------
# ‹וְגֹנֵב אִישׁ וּמְכָרוֹ› (“and-steal man and-sell-him/its”)
# ‹וְנִמְצָא בְיָדוֹ מוֹת› (“and-find in-hand-him/its die”)
# ‹יוּמָת› (“die”)
# "[EN-AID] And he who steals a man, and sells him, and he is found in his
# hand — shall surely be put to death."
m.step("Exod.21.16")
# ‹וְגֹנֵב אִישׁ וּמְכָרוֹ› (“and-steal man and-sell-him/its”)
# ‹וְנִמְצָא בְיָדוֹ› (“and-find in-hand-him/its”)
m.statute("FORBID", "gonev_ish")
# witness-tier presupposed read: scope_closure_and_context_middah on
# abduction_clause — read, not installed
m.witness_read("abduction_clause", "scope_closure_and_context_middah",
                cites=["Sanhedrin 85b:22", "Sanhedrin 86a:14", "Sanhedrin 85b:21", "Sanhedrin 86a:16"])

# -------------------------- Exod.21.17 · THE_CURSER_OF_PARENTS -------------
# ‹וּמְקַלֵּל אָבִיו וְאִמּוֹ› (“and-be-light father-him/its and-mother-
# him/its”)
# ‹מוֹת יוּמָת› (“die die”)
# "[EN-AID] And he who curses his father and his mother shall surely be put
# to death."
m.step("Exod.21.17")
# ‹וּמְקַלֵּל אָבִיו וְאִמּוֹ› (“and-be-light father-him/its and-mother-
# him/its”)
# ‹מוֹת יוּמָת› (“die die”)
m.statute("FORBID", "meqalel_aviv_ve_imo")

# -------------------------- Exod.21.18 · THE_BRAWL -------------------------
# ‹וְכִי־יְרִיבֻן אֲנָשִׁים וְהִכָּה־אִישׁ› (“and-that toss-ward man and-
# strike man”)
# ‹אֶת־רֵעֵהוּ בְּאֶבֶן אוֹ› (“obj-marker associate-him/its in-stone or”)
# ‹בְאֶגְרֹף וְלֹא יָמוּת› (“in-clenched-hand and-not die”)
# ‹וְנָפַל לְמִשְׁכָּב› (“and-fall to-bed”)
# "[EN-AID] And when men quarrel, and a man strikes his fellow with a stone
# or with a fist, and he does not die, but falls to bed —"
m.step("Exod.21.18")
# ‹וְכִי־יְרִיבֻן אֲנָשִׁים וְהִכָּה־אִישׁ› (“and-that toss-ward man and-
# strike man”)
# ‹אֶת־רֵעֵהוּ› (“obj-marker associate-him/its”)
# — case and-khi yerivun man and-strike man obj-marker reehu routes to
# makkeh-reehu
m.case("ve-khi yerivun anashim ve-hika ish et reehu", "makkeh_reehu")

# -------------------------- Exod.21.19 · THE_HEALING_LICENSE ---------------
# ‹אִם־יָקוּם וְהִתְהַלֵּךְ בַּחוּץ› (“if arise and-walk/go in-outside”)
# ‹עַל־מִשְׁעַנְתּוֹ וְנִקָּה הַמַּכֶּה› (“over support-him/its and-be-clean
# the-strike”)
# ‹רַק שִׁבְתּוֹ יִתֵּן› (“leanness rest-him/its set”)
# ‹וְרַפֹּא יְרַפֵּא› (“and-mend mend”)
# "[EN-AID] If he rises, and walks outside on his staff, then the striker
# shall be cleared; only his sitting he shall give — and he shall surely
# heal."
m.step("Exod.21.19")
# ‹רַק שִׁבְתּוֹ יִתֵּן› (“leanness rest-him/its set”)
# ‹וְרַפֹּא יְרַפֵּא› (“and-mend mend”)
# — standing handler — if arise and-walk/go in-the-chutz over mishanto then
# and-be-clean the-makke, shivto set and-mend mend
m.handler("yaqum ve-hithalekh ba-chutz al mishanto",
          "ve-niqa ha-makke, shivto yiten ve-rapo yerape")
# witness-tier presupposed read: two_of_five_in_the_ink on
# injury_indemnities — read, not installed
m.witness_read("injury_indemnities", "two_of_five_in_the_ink",
                cites=["Mishnah Bava Kamma 8:1"])

# -------------------------- Exod.21.20 · THE_STRUCK_SLAVE ------------------
# ‹וְכִי־יַכֶּה אִישׁ אֶת־עַבְדּוֹ› (“and-that strike man obj-marker
# servant-him/its”)
# ‹אוֹ אֶת־אֲמָתוֹ בַּשֵּׁבֶט› (“or obj-marker maidservant-him/its in-
# scion”)
# ‹וּמֵת תַּחַת יָדוֹ› (“and-die under hand-him/its”)
# ‹נָקֹם יִנָּקֵם› (“grudge grudge”)
# "[EN-AID] And when a man strikes his slave or his maidservant with the
# rod, and he dies under his hand — he shall surely be avenged."
m.step("Exod.21.20")
# ‹וְכִי־יַכֶּה אִישׁ אֶת־עַבְדּוֹ› (“and-that strike man obj-marker
# servant-him/its”)
# ‹אוֹ אֶת־אֲמָתוֹ בַּשֵּׁבֶט› (“or obj-marker maidservant-him/its in-
# scion”)
# ‹וּמֵת תַּחַת יָדוֹ› (“and-die under hand-him/its”)
# — case and-khi strike man obj-marker avdo o obj-marker amato in-the-shevet
# u-die routes to makkeh-avdo
m.case("ve-khi yake ish et avdo o et amato ba-shevet u-met", "makkeh_avdo")

# -------------------------- Exod.21.21 · A_DAY_OR_TWO_DAYS -----------------
# ‹אַךְ אִם־יוֹם אוֹ› (“indeed if day or”)
# ‹יוֹמַיִם יַעֲמֹד לֹא› (“day stand not”)
# ‹יֻקַּם כִּי כַסְפּוֹ› (“grudge that silver-him/its”)
# ‹הוּא› (“he/it”)
# "[EN-AID] But if he stand a day or two days, he shall not be avenged — for
# he is his money."
m.step("Exod.21.21")
# ‹יַעֲמֹד לֹא יֻקַּם› (“stand not grudge”)
# ‹כִּי כַסְפּוֹ הוּא› (“that silver-him/its he/it”)
# — standing handler — if day o day stand then not grudge, that khaspo he/it
m.handler("yom o yomayim yaamod",
          "lo yuqam, ki khaspo hu")

# -------------------------- Exod.21.22 · THE_STRUCK_MOTHER -----------------
# ‹וְכִי־יִנָּצוּ אֲנָשִׁים וְנָגְפוּ› (“and-that go-forth man and-push”)
# ‹אִשָּׁה הָרָה וְיָצְאוּ› (“woman pregnant and-bring-forth”)
# ‹יְלָדֶיהָ וְלֹא יִהְיֶה› (“child-her/its and-not be”)
# ‹אָסוֹן עָנוֹשׁ יֵעָנֵשׁ› (“hurt urge urge”)
# ‹כַּאֲשֶׁר יָשִׁית עָלָיו› (“like-as/which place over-him/its”)
# ‹בַּעַל הָאִשָּׁה וְנָתַן› (“master the-woman and-set”)
# ‹בִּפְלִלִים› (“in-magistrate”)
# "[EN-AID] And when men fight, and strike a pregnant woman, and her
# children go out, and there is no harm — he shall surely be fined, as the
# woman's husband lays on him, and he shall give by the judges."
m.step("Exod.21.22")
# ‹וְכִי־יִנָּצוּ אֲנָשִׁים וְנָגְפוּ› (“and-that go-forth man and-push”)
# ‹אִשָּׁה הָרָה וְיָצְאוּ› (“woman pregnant and-bring-forth”)
# ‹יְלָדֶיהָ וְלֹא יִהְיֶה› (“child-her/its and-not be”)
# ‹אָסוֹן› (“hurt”)
# — case and-khi go-forth man and-push woman pregnant and-bring-forth
# yeladeha routes to hurt-or-not
m.case("ve-khi yinatzu anashim ve-nagfu isha hara ve-yatzu yeladeha", "ason_o_lo")
# witness-tier presupposed read: the_courts_algorithm on
# miscarriage_valuation — read, not installed
m.witness_read("miscarriage_valuation", "the_courts_algorithm",
                cites=["Mishnah Bava Kamma 5:4"])
# witness-tier presupposed read: pursuer_and_ox_riders on striving_men —
# read, not installed
m.witness_read("striving_men", "pursuer_and_ox_riders",
                cites=["Sanhedrin 74a:3", "Sanhedrin 79a:10", "Bava Kamma 43a:4", "Arakhin 7a:12", "Bava Kamma 44b:16", "Sanhedrin 78a:14", "Sanhedrin 79b:13", "Bava Kamma 43a:9", "Gittin 42b:8", "Bava Kamma 11a:4", "Bava Kamma 71a:8"])

# -------------------------- Exod.21.23 · LIFE_FOR_LIFE ---------------------
# ‹וְאִם־אָסוֹן יִהְיֶה וְנָתַתָּה› (“and-if hurt be and-set”)
# ‹נֶפֶשׁ תַּחַת נָפֶשׁ› (“living-being under living-being”)
# "[EN-AID] And if there is harm — then you shall give life for life."
m.step("Exod.21.23")
# ‹וְנָתַתָּה נֶפֶשׁ תַּחַת› (“and-set living-being under”)
# ‹נָפֶשׁ› (“living-being”)
# — standing handler — if hurt be then and-set living-being under living-
# being
m.handler("ason yihye",
          "ve-natata nefesh tachat nafesh")

# -------------------------- Exod.21.24 · EYE_FOR_EYE -----------------------
# ‹עַיִן תַּחַת עַיִן› (“eye under eye”)
# ‹שֵׁן תַּחַת שֵׁן› (“tooth under tooth”)
# ‹יָד תַּחַת יָד› (“hand under hand”)
# ‹רֶגֶל תַּחַת רָגֶל› (“foot under foot”)
# "[EN-AID] Eye for eye, tooth for tooth, hand for hand, foot for foot,"
m.step("Exod.21.24")
# ‹עַיִן תַּחַת עַיִן› (“eye under eye”)
# ‹שֵׁן תַּחַת שֵׁן› (“tooth under tooth”)
# — fact holds: eye-under-eye
m.fact("ayin_tachat_ayin")
# witness-tier presupposed read: compiled_through_leviticus_24 on
# tariff_call_site — read, not installed
m.witness_read("tariff_call_site", "compiled_through_leviticus_24",
                cites=["Bava Kamma 83b:10", "Bava Kamma 84a:1"])

# -------------------------- Exod.21.25 · BURN_FOR_BURN ---------------------
# ‹כְּוִיָּה תַּחַת כְּוִיָּה› (“branding under branding”)
# ‹פֶּצַע תַּחַת פָּצַע› (“wound under wound”)
# ‹חַבּוּרָה תַּחַת חַבּוּרָה› (“bound under bound”)
# "[EN-AID] burn for burn, wound for wound, bruise for bruise."
m.step("Exod.21.25")
# ‹כְּוִיָּה תַּחַת כְּוִיָּה› (“branding under branding”)
# ‹פֶּצַע תַּחַת פָּצַע› (“wound under wound”)
# — fact holds: kviya-under-kviya
m.fact("kviya_tachat_kviya")

# -------------------------- Exod.21.26 · THE_EYE_THAT_FREES ----------------
# ‹וְכִי־יַכֶּה אִישׁ אֶת־עֵין› (“and-that strike man obj-marker eye”)
# ‹עַבְדּוֹ אוֹ־אֶת־עֵין אֲמָתוֹ› (“servant-him/its or obj-marker eye
# maidservant-him/its”)
# ‹וְשִׁחֲתָהּ לַחָפְשִׁי יְשַׁלְּחֶנּוּ› (“and-decay-her/its to-exempt
# send-him/its”)
# ‹תַּחַת עֵינוֹ› (“under eye-him/its”)
# "[EN-AID] And when a man strikes the eye of his slave, or the eye of his
# maidservant, and destroys it — he shall let him go free for his eye."
m.step("Exod.21.26")
# ‹לַחָפְשִׁי יְשַׁלְּחֶנּוּ תַּחַת› (“to-exempt send-him/its under”)
# ‹עֵינוֹ› (“eye-him/its”)
# — standing handler — if strike man obj-marker there-is-not avdo and-
# shichatah then to-exempt yeshalchenu under eno
m.handler("yake ish et en avdo ve-shichatah",
          "la-chafshi yeshalchenu tachat eno")
# witness-tier presupposed read: eye_and_tooth_as_exemplars on limb_class —
# read, not installed
m.witness_read("limb_class", "eye_and_tooth_as_exemplars",
                cites=["Kiddushin 24a:6", "Mishnah Negaim 6:7"])

# -------------------------- Exod.21.27 · THE_TOOTH_THAT_FREES --------------
# ‹וְאִם־שֵׁן עַבְדּוֹ אוֹ־שֵׁן› (“and-if tooth servant-him/its or tooth”)
# ‹אֲמָתוֹ יַפִּיל לַחָפְשִׁי› (“maidservant-him/its fall to-exempt”)
# ‹יְשַׁלְּחֶנּוּ תַּחַת שִׁנּוֹ› (“send-him/its under tooth-him/its”)
# "[EN-AID] And if he makes the tooth of his slave, or the tooth of his
# maidservant, fall out — he shall let him go free for his tooth."
m.step("Exod.21.27")
# ‹לַחָפְשִׁי יְשַׁלְּחֶנּוּ תַּחַת› (“to-exempt send-him/its under”)
# ‹שִׁנּוֹ› (“tooth-him/its”)
# — standing handler — if tooth avdo o tooth amato fall then to-exempt
# yeshalchenu under shino
m.handler("shen avdo o shen amato yapil",
          "la-chafshi yeshalchenu tachat shino")

# -------------------------- Exod.21.28 · THE_GORING_OX ---------------------
# ‹וְכִי־יִגַּח שׁוֹר אֶת־אִישׁ› (“and-that butt-with-the-horns bullock obj-
# marker man”)
# ‹אוֹ אֶת־אִשָּׁה וָמֵת› (“or obj-marker woman and-die”)
# ‹סָקוֹל יִסָּקֵל הַשּׁוֹר› (“be-weighty be-weighty the-bullock”)
# ‹וְלֹא יֵאָכֵל אֶת־בְּשָׂרוֹ› (“and-not eat obj-marker flesh-him/its”)
# ‹וּבַעַל הַשּׁוֹר נָקִי› (“and-master the-bullock innocent”)
# "[EN-AID] And when an ox gores a man or a woman, and he dies — the ox
# shall surely be stoned, and its flesh shall not be eaten; and the owner of
# the ox is clear."
m.step("Exod.21.28")
# ‹וְכִי־יִגַּח שׁוֹר אֶת־אִישׁ› (“and-that butt-with-the-horns bullock obj-
# marker man”)
# ‹אוֹ אֶת־אִשָּׁה וָמֵת› (“or obj-marker woman and-die”)
# — case and-khi butt-with-the-horns bullock obj-marker man o obj-marker
# woman and-die routes to bullock-butting
m.case("ve-khi yigach shor et ish o et isha va-met", "shor_nagach")
# witness-tier presupposed read: backfill_legs on stoning_statute — read,
# not installed
m.witness_read("stoning_statute", "backfill_legs",
                cites=["Mishnah Eduyot 6:1", "Mishnah Makkot 1:6"])
# witness-tier presupposed read: the_answer_keys_module_list on
# four_damages_class_map — read, not installed
m.witness_read("four_damages_class_map", "the_answer_keys_module_list",
                cites=["Mishnah Bava Kamma 1:1", "Bava Kamma 2a:1", "Bava Kamma 6b:11"])

# -------------------------- Exod.21.29 · THE_WARNED_OX ---------------------
# ‹וְאִם שׁוֹר נַגָּח› (“and-if bullock butting”)
# ‹הוּא מִתְּמֹל שִׁלְשֹׁם› (“he/it from-ago trebly”)
# ‹וְהוּעַד בִּבְעָלָיו וְלֹא› (“and-duplicate in-master-him/its and-not”)
# ‹יִשְׁמְרֶנּוּ וְהֵמִית אִישׁ› (“keep/guard-him/its and-die man”)
# ‹אוֹ אִשָּׁה הַשּׁוֹר› (“or woman the-bullock”)
# ‹יִסָּקֵל וְגַם־בְּעָלָיו יוּמָת› (“be-weighty and-also master-him/its
# die”)
# "[EN-AID] And if it was a goring ox from yesterday and the day before, and
# its owner was warned, and he did not guard it, and it killed a man or a
# woman — the ox shall be stoned, and its owner shall also die."
m.step("Exod.21.29")
# ‹וְאִם שׁוֹר נַגָּח› (“and-if bullock butting”)
# ‹הוּא מִתְּמֹל שִׁלְשֹׁם› (“he/it from-ago trebly”)
# ‹וְהוּעַד בִּבְעָלָיו וְלֹא› (“and-duplicate in-master-him/its and-not”)
# ‹יִשְׁמְרֶנּוּ› (“keep/guard-him/its”)
# — standing handler — if bullock butting he/it from-ago trebly, and-
# duplicate bi-vealav and-not yishmerenu, and-die then the-bullock be-
# weighty and-also bealav die
m.handler("shor nagach hu mi-temol shilshom, ve-huad bi-vealav ve-lo yishmerenu, ve-hemit",
          "ha-shor yisaqel ve-gam bealav yumat")
# witness-tier presupposed read: parsed_from_the_temporal_tokens on
# forewarned_threshold — read, not installed
m.witness_read("forewarned_threshold", "parsed_from_the_temporal_tokens",
                cites=["Bava Kamma 23b:17", "Bava Kamma 23b:18", "Mishnah Bava Kamma 2:4", "Bava Kamma 24a:9"])

# -------------------------- Exod.21.30 · THE_RANSOM ------------------------
# ‹אִם־כֹּפֶר יוּשַׁת עָלָיו› (“if cover place over-him/its”)
# ‹וְנָתַן פִּדְיֹן נַפְשׁוֹ› (“and-set ransom living-being-him/its”)
# ‹כְּכֹל אֲשֶׁר־יוּשַׁת עָלָיו› (“like-all which place over-him/its”)
# "[EN-AID] If a ransom be laid on him — then he shall give the redemption
# of his life, according to all that is laid on him."
m.step("Exod.21.30")
# ‹וְנָתַן פִּדְיֹן נַפְשׁוֹ› (“and-set ransom living-being-him/its”)
# — standing handler — if cover place alav then and-set ransom nafsho
m.handler("kofer yushat alav",
          "ve-natan pidyon nafsho")

# -------------------------- Exod.21.31 · SON_OR_DAUGHTER -------------------
# ‹אוֹ־בֵן יִגָּח אוֹ־בַת› (“or son butt-with-the-horns or daughter”)
# ‹יִגָּח כַּמִּשְׁפָּט הַזֶּה› (“butt-with-the-horns like-judgment the-
# this”)
# ‹יֵעָשֶׂה לּוֹ› (“make to-him/its”)
# "[EN-AID] Whether it gore a son, or gore a daughter — according to this
# ordinance shall it be done to him."
m.step("Exod.21.31")
# ‹כַּמִּשְׁפָּט הַזֶּה יֵעָשֶׂה› (“like-judgment the-this make”)
# ‹לּוֹ› (“to-him/its”)
# — fact holds: like-judgment-the-this
m.fact("ka_mishpat_ha_ze")

# -------------------------- Exod.21.32 · THIRTY_SHEKELS --------------------
# ‹אִם־עֶבֶד יִגַּח הַשּׁוֹר› (“if servant butt-with-the-horns the-bullock”)
# ‹אוֹ אָמָה כֶּסֶף› (“or maidservant silver”)
# ‹שְׁלֹשִׁים שְׁקָלִים יִתֵּן› (“thirty weight set”)
# ‹לַאדֹנָיו וְהַשּׁוֹר יִסָּקֵל› (“to-lord-him/its and-the-bullock be-
# weighty”)
# "[EN-AID] If the ox gore a slave or a maidservant — thirty shekels of
# silver he shall give to his master, and the ox shall be stoned."
m.step("Exod.21.32")
# ‹כֶּסֶף שְׁלֹשִׁים שְׁקָלִים› (“silver thirty weight”)
# ‹יִתֵּן לַאדֹנָיו וְהַשּׁוֹר› (“set to-lord-him/its and-the-bullock”)
# ‹יִסָּקֵל› (“be-weighty”)
# — standing handler — if servant butt-with-the-horns the-bullock o
# maidservant then silver thirty weight set to-adonav, and-the-bullock be-
# weighty
m.handler("eved yigach ha-shor o ama",
          "kesef sheloshim sheqalim yiten la-adonav, ve-ha-shor yisaqel")

# -------------------------- Exod.21.33 · THE_OPEN_PIT ----------------------
# ‹וְכִי־יִפְתַּח אִישׁ בּוֹר› (“and-that open-wide man pit”)
# ‹אוֹ כִּי־יִכְרֶה אִישׁ› (“or that dig man”)
# ‹בֹּר וְלֹא יְכַסֶּנּוּ› (“pit and-not plump-him/its”)
# ‹וְנָפַל־שָׁמָּה שּׁוֹר אוֹ› (“and-fall there-ward bullock or”)
# ‹חֲמוֹר› (“male-ass”)
# "[EN-AID] And when a man opens a pit, or when a man digs a pit, and does
# not cover it — and an ox or a donkey falls in there:"
m.step("Exod.21.33")
# ‹וְכִי־יִפְתַּח אִישׁ בּוֹר› (“and-that open-wide man pit”)
# ‹אוֹ כִּי־יִכְרֶה אִישׁ› (“or that dig man”)
# ‹בֹּר וְלֹא יְכַסֶּנּוּ› (“pit and-not plump-him/its”)
# — case and-khi open-wide man pit o that dig man pit and-not yekhasenu
# routes to master-the-pit
m.case("ve-khi yiftach ish bor o ki yikhre ish bor ve-lo yekhasenu", "baal_ha_bor")

# -------------------------- Exod.21.34 · THE_PIT_PAYS ----------------------
# ‹בַּעַל הַבּוֹר יְשַׁלֵּם› (“master the-pit be-safe”)
# ‹כֶּסֶף יָשִׁיב לִבְעָלָיו› (“silver return to-master-him/its”)
# ‹וְהַמֵּת יִהְיֶה־לּוֹ› (“and-the-die be to-him/its”)
# "[EN-AID] The owner of the pit shall pay; silver he shall return to its
# owner — and the dead shall be his."
m.step("Exod.21.34")
# ‹בַּעַל הַבּוֹר יְשַׁלֵּם› (“master the-pit be-safe”)
# ‹כֶּסֶף יָשִׁיב לִבְעָלָיו› (“silver return to-master-him/its”)
# — standing handler — if fall shama bullock o male-ass then master the-pit
# be-safe, silver return to-me-vealav
m.handler("nafal shama shor o chamor",
          "baal ha-bor yeshalem, kesef yashiv li-vealav")

# -------------------------- Exod.21.35 · OX_AGAINST_OX ---------------------
# ‹וְכִי־יִגֹּף שׁוֹר־אִישׁ אֶת־שׁוֹר› (“and-that push bullock man obj-
# marker bullock”)
# ‹רֵעֵהוּ וָמֵת וּמָכְרוּ› (“associate-him/its and-die and-sell”)
# ‹אֶת־הַשּׁוֹר הַחַי וְחָצוּ› (“obj-marker the-bullock the-living and-cut”)
# ‹אֶת־כַּסְפּוֹ וְגַם אֶת־הַמֵּת› (“obj-marker silver-him/its and-also obj-
# marker the-die”)
# ‹יֶחֱצוּן› (“cut-ward”)
# "[EN-AID] And when a man's ox strikes his fellow's ox, and it dies — they
# shall sell the living ox and divide its silver, and the dead one they
# shall also divide."
m.step("Exod.21.35")
# ‹וְכִי־יִגֹּף שׁוֹר־אִישׁ אֶת־שׁוֹר› (“and-that push bullock man obj-
# marker bullock”)
# ‹רֵעֵהוּ וָמֵת› (“associate-him/its and-die”)
# — case and-khi push bullock man obj-marker bullock reehu and-die routes to
# bullock-obj-marker-bullock
m.case("ve-khi yigof shor ish et shor reehu va-met", "shor_et_shor")

# -------------------------- Exod.21.36 · THE_KNOWN_GORER -------------------
# ‹אוֹ נוֹדַע כִּי› (“or know that”)
# ‹שׁוֹר נַגָּח הוּא› (“bullock butting he/it”)
# ‹מִתְּמוֹל שִׁלְשֹׁם וְלֹא› (“from-ago trebly and-not”)
# ‹יִשְׁמְרֶנּוּ בְּעָלָיו שַׁלֵּם› (“keep/guard-him/its master-him/its be-
# safe”)
# ‹יְשַׁלֵּם שׁוֹר תַּחַת› (“be-safe bullock under”)
# ‹הַשּׁוֹר וְהַמֵּת יִהְיֶה־לּוֹ› (“the-bullock and-the-die be to-him/its”)
# "[EN-AID] Or it was known that it was a goring ox from yesterday and the
# day before, and its owner did not guard it — he shall surely pay ox for
# ox, and the dead shall be his."
m.step("Exod.21.36")
# ‹שַׁלֵּם יְשַׁלֵּם שׁוֹר› (“be-safe be-safe bullock”)
# ‹תַּחַת הַשּׁוֹר› (“under the-bullock”)
# — standing handler — if know that bullock butting he/it from-ago trebly
# and-not yishmerenu bealav then be-safe be-safe bullock under the-bullock
m.handler("noda ki shor nagach hu mi-temol shilshom ve-lo yishmerenu bealav",
          "shalem yeshalem shor tachat ha-shor")

# -------------------------- Exod.21.37 · FIVE_OXEN_FOUR_SHEEP --------------
# ‹כִּי יִגְנֹב־אִישׁ שׁוֹר› (“that steal man bullock”)
# ‹אוֹ־שֶׂה וּטְבָחוֹ אוֹ› (“or member-of-a-flock and-slaughter-him/its or”)
# ‹מְכָרוֹ חֲמִשָּׁה בָקָר› (“sell-him/its five herd”)
# ‹יְשַׁלֵּם תַּחַת הַשּׁוֹר› (“be-safe under the-bullock”)
# ‹וְאַרְבַּע־צֹאן תַּחַת הַשֶּׂה› (“and-four flock under the-member-of-a-
# flock”)
# "[EN-AID] When a man steals an ox or a sheep, and slaughters it or sells
# it — five oxen he shall pay for the ox, and four sheep for the sheep."
m.step("Exod.21.37")
# ‹כִּי יִגְנֹב־אִישׁ שׁוֹר› (“that steal man bullock”)
# ‹אוֹ־שֶׂה וּטְבָחוֹ אוֹ› (“or member-of-a-flock and-slaughter-him/its or”)
# ‹מְכָרוֹ› (“sell-him/its”)
# — case that steal man bullock o member-of-a-flock u-tevacho o mekharo
# routes to ganav-bullock-or-member-of-a-flock
m.case("ki yignov ish shor o se u-tevacho o mekharo", "ganav_shor_o_se")
# witness-tier presupposed read: constants_with_their_scope_in_ink on
# theft_multiples — read, not installed
m.witness_read("theft_multiples", "constants_with_their_scope_in_ink",
                cites=["Mishnah Bava Kamma 7:1"])

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
    assert sorted(m.WORLD["facts"]) == sorted(['ve_ele_ha_mishpatim', 'case: ki tiqne eved ivri -> eved_ivri', 'be_gapo_yavo_be_gapo_yetze', 'ha_isha_vi_yladeha_tihye_la_adoneha', 'ahavti_et_adoni', 'handler: IF(amor yomar ha-eved ahavti) THEN(ve-ratza et-azno ba-martzea, va-avado le-olam)', 'case: ve-khi yimkor ish et bito le-ama -> ama_ivriya', 've_hefda', 'ke_mishpat_ha_banot', 'sheera_kesuta_ve_onata', 'handler: IF(shelash ele lo yaase lah) THEN(ve-yatza chinam en kasef)', 'statute: FORBID(makkeh_ish)', 'handler: IF(lo tzada, ve-ha-elohim ina le-yado) THEN(ve-samti lekha maqom asher yanus shama)', 'handler: IF(yazid ish al reehu le-horgo ve-arma) THEN(me-im mizbechi tiqachenu la-mut)', 'statute: FORBID(makkeh_aviv_ve_imo)', 'statute: FORBID(gonev_ish)', 'statute: FORBID(meqalel_aviv_ve_imo)', 'case: ve-khi yerivun anashim ve-hika ish et reehu -> makkeh_reehu', 'handler: IF(yaqum ve-hithalekh ba-chutz al mishanto) THEN(ve-niqa ha-makke, shivto yiten ve-rapo yerape)', 'case: ve-khi yake ish et avdo o et amato ba-shevet u-met -> makkeh_avdo', 'handler: IF(yom o yomayim yaamod) THEN(lo yuqam, ki khaspo hu)', 'case: ve-khi yinatzu anashim ve-nagfu isha hara ve-yatzu yeladeha -> ason_o_lo', 'handler: IF(ason yihye) THEN(ve-natata nefesh tachat nafesh)', 'ayin_tachat_ayin', 'kviya_tachat_kviya', 'handler: IF(yake ish et en avdo ve-shichatah) THEN(la-chafshi yeshalchenu tachat eno)', 'handler: IF(shen avdo o shen amato yapil) THEN(la-chafshi yeshalchenu tachat shino)', 'case: ve-khi yigach shor et ish o et isha va-met -> shor_nagach', 'handler: IF(shor nagach hu mi-temol shilshom, ve-huad bi-vealav ve-lo yishmerenu, ve-hemit) THEN(ha-shor yisaqel ve-gam bealav yumat)', 'handler: IF(kofer yushat alav) THEN(ve-natan pidyon nafsho)', 'ka_mishpat_ha_ze', 'handler: IF(eved yigach ha-shor o ama) THEN(kesef sheloshim sheqalim yiten la-adonav, ve-ha-shor yisaqel)', 'case: ve-khi yiftach ish bor o ki yikhre ish bor ve-lo yekhasenu -> baal_ha_bor', 'handler: IF(nafal shama shor o chamor) THEN(baal ha-bor yeshalem, kesef yashiv li-vealav)', 'case: ve-khi yigof shor ish et shor reehu va-met -> shor_et_shor', 'handler: IF(noda ki shor nagach hu mi-temol shilshom ve-lo yishmerenu bealav) THEN(shalem yeshalem shor tachat ha-shor)', 'case: ki yignov ish shor o se u-tevacho o mekharo -> ganav_shor_o_se'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 27
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('case_syntax_and_release_list', 'the_codes_first_case'), ('slave_clock', 'calendar_semantics_and_family_law'), ('intent_word', 'forewarning_and_strike_grammar'), ('abduction_clause', 'scope_closure_and_context_middah'), ('injury_indemnities', 'two_of_five_in_the_ink'), ('miscarriage_valuation', 'the_courts_algorithm'), ('striving_men', 'pursuer_and_ox_riders'), ('tariff_call_site', 'compiled_through_leviticus_24'), ('limb_class', 'eye_and_tooth_as_exemplars'), ('stoning_statute', 'backfill_legs'), ('four_damages_class_map', 'the_answer_keys_module_list'), ('forewarned_threshold', 'parsed_from_the_temporal_tokens'), ('theft_multiples', 'constants_with_their_scope_in_ink')]
    assert m.WITNESS_READS[0]["cites"] == ['Gittin 90a:10', 'Mekhilta DeRabbi Yishmael, Tractate Bachodesh 11:11', 'Mishnah Kiddushin 1:2', 'Kiddushin 16a:11', 'Kiddushin 15a:19']
    assert all('the_codes_first_case' not in f for f in m.WORLD["facts"])
    assert 'case_syntax_and_release_list' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Niddah 48a:2', 'Kiddushin 17a:1', 'Kiddushin 18a:8', 'Kiddushin 19a:8', 'Sotah 23b:9', 'Bekhorot 50b:7', 'Yevamot 70a:5', 'Temurah 25b:4', 'Bava Batra 50a:8']
    assert all('calendar_semantics_and_family_law' not in f for f in m.WORLD["facts"])
    assert 'slave_clock' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sanhedrin 41a:2', 'Sanhedrin 84b:5', 'Sanhedrin 52b:13', 'Makkot 8b:14', 'Bava Kamma 90b:14', 'Sanhedrin 78a:19', 'Sanhedrin 85b:10']
    assert all('forewarning_and_strike_grammar' not in f for f in m.WORLD["facts"])
    assert 'intent_word' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sanhedrin 85b:22', 'Sanhedrin 86a:14', 'Sanhedrin 85b:21', 'Sanhedrin 86a:16']
    assert all('scope_closure_and_context_middah' not in f for f in m.WORLD["facts"])
    assert 'abduction_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mishnah Bava Kamma 8:1']
    assert all('two_of_five_in_the_ink' not in f for f in m.WORLD["facts"])
    assert 'injury_indemnities' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Mishnah Bava Kamma 5:4']
    assert all('the_courts_algorithm' not in f for f in m.WORLD["facts"])
    assert 'miscarriage_valuation' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sanhedrin 74a:3', 'Sanhedrin 79a:10', 'Bava Kamma 43a:4', 'Arakhin 7a:12', 'Bava Kamma 44b:16', 'Sanhedrin 78a:14', 'Sanhedrin 79b:13', 'Bava Kamma 43a:9', 'Gittin 42b:8', 'Bava Kamma 11a:4', 'Bava Kamma 71a:8']
    assert all('pursuer_and_ox_riders' not in f for f in m.WORLD["facts"])
    assert 'striving_men' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bava Kamma 83b:10', 'Bava Kamma 84a:1']
    assert all('compiled_through_leviticus_24' not in f for f in m.WORLD["facts"])
    assert 'tariff_call_site' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Kiddushin 24a:6', 'Mishnah Negaim 6:7']
    assert all('eye_and_tooth_as_exemplars' not in f for f in m.WORLD["facts"])
    assert 'limb_class' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Mishnah Eduyot 6:1', 'Mishnah Makkot 1:6']
    assert all('backfill_legs' not in f for f in m.WORLD["facts"])
    assert 'stoning_statute' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Mishnah Bava Kamma 1:1', 'Bava Kamma 2a:1', 'Bava Kamma 6b:11']
    assert all('the_answer_keys_module_list' not in f for f in m.WORLD["facts"])
    assert 'four_damages_class_map' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bava Kamma 23b:17', 'Bava Kamma 23b:18', 'Mishnah Bava Kamma 2:4', 'Bava Kamma 24a:9']
    assert all('parsed_from_the_temporal_tokens' not in f for f in m.WORLD["facts"])
    assert 'forewarned_threshold' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Mishnah Bava Kamma 7:1']
    assert all('constants_with_their_scope_in_ink' not in f for f in m.WORLD["facts"])
    assert 'theft_multiples' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
