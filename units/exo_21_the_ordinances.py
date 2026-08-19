#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וְאֵלֶּה הַמִּשְׁפָּטִים אֲשֶׁר תָּשִׂים לִפְנֵיהֶם
# "[EN-AID] And these are the ordinances which you shall set before them."
m.step("Exod.21.1")
# ‹וְאֵלֶּה הַמִּשְׁפָּטִים אֲשֶׁר תָּשִׂים לִפְנֵיהֶם› (“and-these the-
# judgment which put/set to-face-them/their”) — fact holds: and-these-the-
# judgment
m.fact("ve_ele_ha_mishpatim")

# -------------------------- Exod.21.2 · THE_HEBREW_SLAVE -------------------
# כִּי תִקְנֶה עֶבֶד עִבְרִי שֵׁשׁ שָׁנִים יַעֲבֹד וּבַשְּׁבִעִת יֵצֵא
# לַחָפְשִׁי חִנָּם
# "[EN-AID] When you acquire a Hebrew slave, six years he shall serve; and
# in the seventh he shall go out free, for nothing."
m.step("Exod.21.2")
# ‹כִּי תִקְנֶה עֶבֶד עִבְרִי› (“that possessor servant Hebrew”) — case that
# possessor servant Hebrew routes to servant-Hebrew
m.case("ki tiqne eved ivri", "eved_ivri")

# -------------------------- Exod.21.3 · AS_HE_CAME -------------------------
# אִם־בְּגַפּוֹ יָבֹא בְּגַפּוֹ יֵצֵא אִם־בַּעַל אִשָּׁה הוּא וְיָצְאָה
# אִשְׁתּוֹ עִמּוֹ
# "[EN-AID] If he came in by himself, he shall go out by himself; if he was
# the husband of a wife, then his wife shall go out with him."
m.step("Exod.21.3")
# ‹אִם־בְּגַפּוֹ יָבֹא בְּגַפּוֹ יֵצֵא› (“if in-back-him/its come/bring in-
# back-him/its bring-forth”) — fact holds: in-gapo-come/bring-in-gapo-bring-
# forth
m.fact("be_gapo_yavo_be_gapo_yetze")

# -------------------------- Exod.21.4 · THE_MASTERS_WIFE -------------------
# אִם־אֲדֹנָיו יִתֶּן־לוֹ אִשָּׁה וְיָלְדָה־לוֹ בָנִים אוֹ בָנוֹת הָאִשָּׁה
# וִילָדֶיהָ תִּהְיֶה לַאדֹנֶיהָ וְהוּא יֵצֵא בְגַפּוֹ
# "[EN-AID] If his master gives him a wife, and she bears him sons or
# daughters — the wife and her children shall be her master's, and he shall
# go out by himself."
m.step("Exod.21.4")
# ‹הָאִשָּׁה וִילָדֶיהָ תִּהְיֶה לַאדֹנֶיהָ וְהוּא יֵצֵא בְגַפּוֹ› (“the-
# woman and-child-her/its be to-lord-her/its and-he/it bring-forth in-back-
# him/its”) — fact holds: the-woman-vi-yladeha-be-to-adoneha
m.fact("ha_isha_vi_yladeha_tihye_la_adoneha")

# -------------------------- Exod.21.5 · I_LOVE_MY_MASTER -------------------
# וְאִם־אָמֹר יֹאמַר הָעֶבֶד אָהַבְתִּי אֶת־אֲדֹנִי אֶת־אִשְׁתִּי
# וְאֶת־בָּנָי לֹא אֵצֵא חָפְשִׁי
# "[EN-AID] And if the slave shall plainly say: I love my master, my wife,
# and my sons — I will not go out free."
m.step("Exod.21.5")
# ‹אָמֹר יֹאמַר הָעֶבֶד אָהַבְתִּי אֶת־אֲדֹנִי אֶת־אִשְׁתִּי וְאֶת־בָּנָי›
# (“say say the-servant have-affection-for obj-marker lord-me/my obj-marker
# woman-me/my and-obj-marker son-me/my”) — fact holds: have-affection-for-
# obj-marker-adoni
m.fact("ahavti_et_adoni")

# -------------------------- Exod.21.6 · THE_AWL_AND_THE_DOOR ---------------
# וְהִגִּישׁוֹ אֲדֹנָיו אֶל־הָאֱלֹהִים וְהִגִּישׁוֹ אֶל־הַדֶּלֶת אוֹ
# אֶל־הַמְּזוּזָה וְרָצַע אֲדֹנָיו אֶת־אָזְנוֹ בַּמַּרְצֵעַ וַעֲבָדוֹ
# לְעֹלָם
# "[EN-AID] Then his master shall bring him to God, and bring him to the
# door, or to the doorpost; and his master shall pierce his ear with the awl
# — and he shall serve him forever."
m.step("Exod.21.6")
# ‹וְרָצַע אֲדֹנָיו אֶת־אָזְנוֹ בַּמַּרְצֵעַ וַעֲבָדוֹ לְעֹלָם› (“and-pierce
# lord-him/its obj-marker broadness.-i.e.-the-ear-him/its in-awl and-
# work/serve-him/its to-forever”) — standing handler — if say say the-
# servant have-affection-for then and-pierce obj-marker-azno in-the-martzea,
# and-avado to-forever
m.handler("amor yomar ha-eved ahavti",
          "ve-ratza et-azno ba-martzea, va-avado le-olam")

# -------------------------- Exod.21.7 · THE_DAUGHTER_SOLD ------------------
# וְכִי־יִמְכֹּר אִישׁ אֶת־בִּתּוֹ לְאָמָה לֹא תֵצֵא כְּצֵאת הָעֲבָדִים
# "[EN-AID] And when a man sells his daughter as a maidservant, she shall
# not go out as the slaves go out."
m.step("Exod.21.7")
# ‹וְכִי־יִמְכֹּר אִישׁ אֶת־בִּתּוֹ לְאָמָה› (“and-that sell man obj-marker
# daughter-him/its to-maidservant”) — case and-khi sell man obj-marker bito
# to-maidservant routes to maidservant-ivriya
m.case("ve-khi yimkor ish et bito le-ama", "ama_ivriya")

# -------------------------- Exod.21.8 · THE_QERE_OF_MERCY ------------------
# אִם־רָעָה בְּעֵינֵי אֲדֹנֶיהָ אֲשֶׁר־לא לוֹ יְעָדָהּ וְהֶפְדָּהּ לְעַם
# נָכְרִי לֹא־יִמְשֹׁל לְמָכְרָהּ בְּבִגְדוֹ־בָהּ
# "[EN-AID] If she is bad in the eyes of her master, who has not designated
# her — then he shall let her be redeemed; to a foreign people he shall not
# rule to sell her, since he has dealt treacherously with her."
m.step("Exod.21.8")
# ‹אֲשֶׁר־לא לוֹ יְעָדָהּ וְהֶפְדָּהּ› (“which not to-him/its fix-upon-
# her/its and-sever-her/its”) — fact holds: and-hefda
m.fact("ve_hefda")

# -------------------------- Exod.21.9 · AS_THE_DAUGHTERS -------------------
# וְאִם־לִבְנוֹ יִיעָדֶנָּה כְּמִשְׁפַּט הַבָּנוֹת יַעֲשֶׂה־לָּהּ
# "[EN-AID] And if he designates her for his son — according to the
# ordinance of the daughters he shall do for her."
m.step("Exod.21.9")
# ‹כְּמִשְׁפַּט הַבָּנוֹת יַעֲשֶׂה־לָּהּ› (“like-judgment the-daughter make
# to-her/its”) — fact holds: like-judgment-the-daughter
m.fact("ke_mishpat_ha_banot")

# -------------------------- Exod.21.10 · HER_THREE_RIGHTS ------------------
# אִם־אַחֶרֶת יִקַּח־לוֹ שְׁאֵרָהּ כְּסוּתָהּ וְעֹנָתָהּ לֹא יִגְרָע
# "[EN-AID] If he takes himself another — her flesh, her covering, and her
# season he shall not diminish."
m.step("Exod.21.10")
# ‹שְׁאֵרָהּ כְּסוּתָהּ וְעֹנָתָהּ לֹא יִגְרָע› (“flesh-her/its cover-
# her/its and-sexual-her/its not scrape-off”) — fact holds: sheera-kesuta-
# and-onata
m.fact("sheera_kesuta_ve_onata")

# -------------------------- Exod.21.11 · OUT_FREE_WITHOUT_MONEY ------------
# וְאִם־שְׁלָשׁ־אֵלֶּה לֹא יַעֲשֶׂה לָהּ וְיָצְאָה חִנָּם אֵין כָּסֶף
# "[EN-AID] And if these three he does not do for her — then she shall go
# out for nothing, without money."
m.step("Exod.21.11")
# ‹וְיָצְאָה חִנָּם אֵין כָּסֶף› (“and-bring-forth gratis there-is-not
# silver”) — standing handler — if three these not make lah then and-bring-
# forth gratis there-is-not silver
m.handler("shelash ele lo yaase lah",
          "ve-yatza chinam en kasef")

# -------------------------- Exod.21.12 · THE_STRIKER_OF_MAN ----------------
# מַכֵּה אִישׁ וָמֵת מוֹת יוּמָת
# "[EN-AID] He who strikes a man, and he dies — shall surely be put to
# death."
m.step("Exod.21.12")
# ‹מַכֵּה אִישׁ וָמֵת מוֹת יוּמָת› (“strike man and-die die die”) —
m.statute("FORBID", "makkeh_ish")

# -------------------------- Exod.21.13 · THE_PLACE_TO_FLEE -----------------
# וַאֲשֶׁר לֹא צָדָה וְהָאֱלֹהִים אִנָּה לְיָדוֹ וְשַׂמְתִּי לְךָ מָקוֹם
# אֲשֶׁר יָנוּס שָׁמָּה
# "[EN-AID] And he who did not lie in wait, but God caused it to come to his
# hand — I will set for you a place where he may flee."
m.step("Exod.21.13")
# ‹וְשַׂמְתִּי לְךָ מָקוֹם אֲשֶׁר יָנוּס שָׁמָּה› (“and-put/set to-you/your
# place which flit there-ward”) — standing handler — if not chase, and-the-
# God approach to-his-hand then and-put/set to-you place which flit shama
m.handler("lo tzada, ve-ha-elohim ina le-yado",
          "ve-samti lekha maqom asher yanus shama")

# -------------------------- Exod.21.14 · FROM_MY_ALTAR ---------------------
# וְכִי־יָזִד אִישׁ עַל־רֵעֵהוּ לְהָרְגוֹ בְעָרְמָה מֵעִם מִזְבְּחִי
# תִּקָּחֶנּוּ לָמוּת
# "[EN-AID] And when a man presumes against his fellow, to kill him by
# scheme — from My altar you shall take him, to die."
m.step("Exod.21.14")
# ‹מֵעִם מִזְבְּחִי תִּקָּחֶנּוּ לָמוּת› (“from-with altar-me/my take-
# him/its to-die”) — standing handler — if seethe man over reehu to-horgo
# and-trickery then from-if mizbechi tiqachenu to-die
m.handler("yazid ish al reehu le-horgo ve-arma",
          "me-im mizbechi tiqachenu la-mut")

# -------------------------- Exod.21.15 · THE_STRIKER_OF_PARENTS ------------
# וּמַכֵּה אָבִיו וְאִמּוֹ מוֹת יוּמָת
# "[EN-AID] And he who strikes his father and his mother shall surely be put
# to death."
m.step("Exod.21.15")
# ‹וּמַכֵּה אָבִיו וְאִמּוֹ מוֹת יוּמָת› (“and-strike father-him/its and-
# mother-him/its die die”) —
m.statute("FORBID", "makkeh_aviv_ve_imo")

# -------------------------- Exod.21.16 · THE_MAN_STEALER -------------------
# וְגֹנֵב אִישׁ וּמְכָרוֹ וְנִמְצָא בְיָדוֹ מוֹת יוּמָת
# "[EN-AID] And he who steals a man, and sells him, and he is found in his
# hand — shall surely be put to death."
m.step("Exod.21.16")
# ‹וְגֹנֵב אִישׁ וּמְכָרוֹ וְנִמְצָא בְיָדוֹ› (“and-steal man and-sell-
# him/its and-find in-hand-him/its”) —
m.statute("FORBID", "gonev_ish")

# -------------------------- Exod.21.17 · THE_CURSER_OF_PARENTS -------------
# וּמְקַלֵּל אָבִיו וְאִמּוֹ מוֹת יוּמָת
# "[EN-AID] And he who curses his father and his mother shall surely be put
# to death."
m.step("Exod.21.17")
# ‹וּמְקַלֵּל אָבִיו וְאִמּוֹ מוֹת יוּמָת› (“and-be-light father-him/its
# and-mother-him/its die die”) —
m.statute("FORBID", "meqalel_aviv_ve_imo")

# -------------------------- Exod.21.18 · THE_BRAWL -------------------------
# וְכִי־יְרִיבֻן אֲנָשִׁים וְהִכָּה־אִישׁ אֶת־רֵעֵהוּ בְּאֶבֶן אוֹ בְאֶגְרֹף
# וְלֹא יָמוּת וְנָפַל לְמִשְׁכָּב
# "[EN-AID] And when men quarrel, and a man strikes his fellow with a stone
# or with a fist, and he does not die, but falls to bed —"
m.step("Exod.21.18")
# ‹וְכִי־יְרִיבֻן אֲנָשִׁים וְהִכָּה־אִישׁ אֶת־רֵעֵהוּ› (“and-that toss-ward
# man and-strike man obj-marker associate-him/its”) — case and-khi yerivun
# man and-strike man obj-marker reehu routes to makkeh-reehu
m.case("ve-khi yerivun anashim ve-hika ish et reehu", "makkeh_reehu")

# -------------------------- Exod.21.19 · THE_HEALING_LICENSE ---------------
# אִם־יָקוּם וְהִתְהַלֵּךְ בַּחוּץ עַל־מִשְׁעַנְתּוֹ וְנִקָּה הַמַּכֶּה רַק
# שִׁבְתּוֹ יִתֵּן וְרַפֹּא יְרַפֵּא
# "[EN-AID] If he rises, and walks outside on his staff, then the striker
# shall be cleared; only his sitting he shall give — and he shall surely
# heal."
m.step("Exod.21.19")
# ‹רַק שִׁבְתּוֹ יִתֵּן וְרַפֹּא יְרַפֵּא› (“leanness rest-him/its set and-
# mend mend”) — standing handler — if arise and-walk/go in-the-chutz over
# mishanto then and-be-clean the-makke, shivto set and-mend mend
m.handler("yaqum ve-hithalekh ba-chutz al mishanto",
          "ve-niqa ha-makke, shivto yiten ve-rapo yerape")

# -------------------------- Exod.21.20 · THE_STRUCK_SLAVE ------------------
# וְכִי־יַכֶּה אִישׁ אֶת־עַבְדּוֹ אוֹ אֶת־אֲמָתוֹ בַּשֵּׁבֶט וּמֵת תַּחַת
# יָדוֹ נָקֹם יִנָּקֵם
# "[EN-AID] And when a man strikes his slave or his maidservant with the
# rod, and he dies under his hand — he shall surely be avenged."
m.step("Exod.21.20")
# ‹וְכִי־יַכֶּה אִישׁ אֶת־עַבְדּוֹ אוֹ אֶת־אֲמָתוֹ בַּשֵּׁבֶט וּמֵת תַּחַת
# יָדוֹ› (“and-that strike man obj-marker servant-him/its or obj-marker
# maidservant-him/its in-scion and-die under hand-him/its”) — case and-khi
# strike man obj-marker avdo o obj-marker amato in-the-shevet u-die routes
# to makkeh-avdo
m.case("ve-khi yake ish et avdo o et amato ba-shevet u-met", "makkeh_avdo")

# -------------------------- Exod.21.21 · A_DAY_OR_TWO_DAYS -----------------
# אַךְ אִם־יוֹם אוֹ יוֹמַיִם יַעֲמֹד לֹא יֻקַּם כִּי כַסְפּוֹ הוּא
# "[EN-AID] But if he stand a day or two days, he shall not be avenged — for
# he is his money."
m.step("Exod.21.21")
# ‹יַעֲמֹד לֹא יֻקַּם כִּי כַסְפּוֹ הוּא› (“stand not grudge that silver-
# him/its he/it”) — standing handler — if day o day stand then not grudge,
# that khaspo he/it
m.handler("yom o yomayim yaamod",
          "lo yuqam, ki khaspo hu")

# -------------------------- Exod.21.22 · THE_STRUCK_MOTHER -----------------
# וְכִי־יִנָּצוּ אֲנָשִׁים וְנָגְפוּ אִשָּׁה הָרָה וְיָצְאוּ יְלָדֶיהָ וְלֹא
# יִהְיֶה אָסוֹן עָנוֹשׁ יֵעָנֵשׁ כַּאֲשֶׁר יָשִׁית עָלָיו בַּעַל הָאִשָּׁה
# וְנָתַן בִּפְלִלִים
# "[EN-AID] And when men fight, and strike a pregnant woman, and her
# children go out, and there is no harm — he shall surely be fined, as the
# woman's husband lays on him, and he shall give by the judges."
m.step("Exod.21.22")
# ‹וְכִי־יִנָּצוּ אֲנָשִׁים וְנָגְפוּ אִשָּׁה הָרָה וְיָצְאוּ יְלָדֶיהָ
# וְלֹא יִהְיֶה אָסוֹן› (“and-that go-forth man and-push woman pregnant and-
# bring-forth child-her/its and-not be hurt”) — case and-khi go-forth man
# and-push woman pregnant and-bring-forth yeladeha routes to hurt-or-not
m.case("ve-khi yinatzu anashim ve-nagfu isha hara ve-yatzu yeladeha", "ason_o_lo")

# -------------------------- Exod.21.23 · LIFE_FOR_LIFE ---------------------
# וְאִם־אָסוֹן יִהְיֶה וְנָתַתָּה נֶפֶשׁ תַּחַת נָפֶשׁ
# "[EN-AID] And if there is harm — then you shall give life for life."
m.step("Exod.21.23")
# ‹וְנָתַתָּה נֶפֶשׁ תַּחַת נָפֶשׁ› (“and-set living-being under living-
# being”) — standing handler — if hurt be then and-set living-being under
# living-being
m.handler("ason yihye",
          "ve-natata nefesh tachat nafesh")

# -------------------------- Exod.21.24 · EYE_FOR_EYE -----------------------
# עַיִן תַּחַת עַיִן שֵׁן תַּחַת שֵׁן יָד תַּחַת יָד רֶגֶל תַּחַת רָגֶל
# "[EN-AID] Eye for eye, tooth for tooth, hand for hand, foot for foot,"
m.step("Exod.21.24")
# ‹עַיִן תַּחַת עַיִן שֵׁן תַּחַת שֵׁן› (“eye under eye tooth under tooth”)
# — fact holds: eye-under-eye
m.fact("ayin_tachat_ayin")

# -------------------------- Exod.21.25 · BURN_FOR_BURN ---------------------
# כְּוִיָּה תַּחַת כְּוִיָּה פֶּצַע תַּחַת פָּצַע חַבּוּרָה תַּחַת חַבּוּרָה
# "[EN-AID] burn for burn, wound for wound, bruise for bruise."
m.step("Exod.21.25")
# ‹כְּוִיָּה תַּחַת כְּוִיָּה פֶּצַע תַּחַת פָּצַע› (“branding under
# branding wound under wound”) — fact holds: kviya-under-kviya
m.fact("kviya_tachat_kviya")

# -------------------------- Exod.21.26 · THE_EYE_THAT_FREES ----------------
# וְכִי־יַכֶּה אִישׁ אֶת־עֵין עַבְדּוֹ אוֹ־אֶת־עֵין אֲמָתוֹ וְשִׁחֲתָהּ
# לַחָפְשִׁי יְשַׁלְּחֶנּוּ תַּחַת עֵינוֹ
# "[EN-AID] And when a man strikes the eye of his slave, or the eye of his
# maidservant, and destroys it — he shall let him go free for his eye."
m.step("Exod.21.26")
# ‹לַחָפְשִׁי יְשַׁלְּחֶנּוּ תַּחַת עֵינוֹ› (“to-exempt send-him/its under
# eye-him/its”) — standing handler — if strike man obj-marker there-is-not
# avdo and-shichatah then to-exempt yeshalchenu under eno
m.handler("yake ish et en avdo ve-shichatah",
          "la-chafshi yeshalchenu tachat eno")

# -------------------------- Exod.21.27 · THE_TOOTH_THAT_FREES --------------
# וְאִם־שֵׁן עַבְדּוֹ אוֹ־שֵׁן אֲמָתוֹ יַפִּיל לַחָפְשִׁי יְשַׁלְּחֶנּוּ
# תַּחַת שִׁנּוֹ
# "[EN-AID] And if he makes the tooth of his slave, or the tooth of his
# maidservant, fall out — he shall let him go free for his tooth."
m.step("Exod.21.27")
# ‹לַחָפְשִׁי יְשַׁלְּחֶנּוּ תַּחַת שִׁנּוֹ› (“to-exempt send-him/its under
# tooth-him/its”) — standing handler — if tooth avdo o tooth amato fall then
# to-exempt yeshalchenu under shino
m.handler("shen avdo o shen amato yapil",
          "la-chafshi yeshalchenu tachat shino")

# -------------------------- Exod.21.28 · THE_GORING_OX ---------------------
# וְכִי־יִגַּח שׁוֹר אֶת־אִישׁ אוֹ אֶת־אִשָּׁה וָמֵת סָקוֹל יִסָּקֵל
# הַשּׁוֹר וְלֹא יֵאָכֵל אֶת־בְּשָׂרוֹ וּבַעַל הַשּׁוֹר נָקִי
# "[EN-AID] And when an ox gores a man or a woman, and he dies — the ox
# shall surely be stoned, and its flesh shall not be eaten; and the owner of
# the ox is clear."
m.step("Exod.21.28")
# ‹וְכִי־יִגַּח שׁוֹר אֶת־אִישׁ אוֹ אֶת־אִשָּׁה וָמֵת› (“and-that butt-with-
# the-horns bullock obj-marker man or obj-marker woman and-die”) — case and-
# khi butt-with-the-horns bullock obj-marker man o obj-marker woman and-die
# routes to bullock-butting
m.case("ve-khi yigach shor et ish o et isha va-met", "shor_nagach")

# -------------------------- Exod.21.29 · THE_WARNED_OX ---------------------
# וְאִם שׁוֹר נַגָּח הוּא מִתְּמֹל שִׁלְשֹׁם וְהוּעַד בִּבְעָלָיו וְלֹא
# יִשְׁמְרֶנּוּ וְהֵמִית אִישׁ אוֹ אִשָּׁה הַשּׁוֹר יִסָּקֵל וְגַם־בְּעָלָיו
# יוּמָת
# "[EN-AID] And if it was a goring ox from yesterday and the day before, and
# its owner was warned, and he did not guard it, and it killed a man or a
# woman — the ox shall be stoned, and its owner shall also die."
m.step("Exod.21.29")
# ‹וְאִם שׁוֹר נַגָּח הוּא מִתְּמֹל שִׁלְשֹׁם וְהוּעַד בִּבְעָלָיו וְלֹא
# יִשְׁמְרֶנּוּ› (“and-if bullock butting he/it from-ago trebly and-
# duplicate in-master-him/its and-not keep/guard-him/its”) — standing
# handler — if bullock butting he/it from-ago trebly, and-duplicate bi-
# vealav and-not yishmerenu, and-die then the-bullock be-weighty and-also
# bealav die
m.handler("shor nagach hu mi-temol shilshom, ve-huad bi-vealav ve-lo yishmerenu, ve-hemit",
          "ha-shor yisaqel ve-gam bealav yumat")

# -------------------------- Exod.21.30 · THE_RANSOM ------------------------
# אִם־כֹּפֶר יוּשַׁת עָלָיו וְנָתַן פִּדְיֹן נַפְשׁוֹ כְּכֹל אֲשֶׁר־יוּשַׁת
# עָלָיו
# "[EN-AID] If a ransom be laid on him — then he shall give the redemption
# of his life, according to all that is laid on him."
m.step("Exod.21.30")
# ‹וְנָתַן פִּדְיֹן נַפְשׁוֹ› (“and-set ransom living-being-him/its”) —
# standing handler — if cover place alav then and-set ransom nafsho
m.handler("kofer yushat alav",
          "ve-natan pidyon nafsho")

# -------------------------- Exod.21.31 · SON_OR_DAUGHTER -------------------
# אוֹ־בֵן יִגָּח אוֹ־בַת יִגָּח כַּמִּשְׁפָּט הַזֶּה יֵעָשֶׂה לּוֹ
# "[EN-AID] Whether it gore a son, or gore a daughter — according to this
# ordinance shall it be done to him."
m.step("Exod.21.31")
# ‹כַּמִּשְׁפָּט הַזֶּה יֵעָשֶׂה לּוֹ› (“like-judgment the-this make to-
# him/its”) — fact holds: like-judgment-the-this
m.fact("ka_mishpat_ha_ze")

# -------------------------- Exod.21.32 · THIRTY_SHEKELS --------------------
# אִם־עֶבֶד יִגַּח הַשּׁוֹר אוֹ אָמָה כֶּסֶף שְׁלֹשִׁים שְׁקָלִים יִתֵּן
# לַאדֹנָיו וְהַשּׁוֹר יִסָּקֵל
# "[EN-AID] If the ox gore a slave or a maidservant — thirty shekels of
# silver he shall give to his master, and the ox shall be stoned."
m.step("Exod.21.32")
# ‹כֶּסֶף שְׁלֹשִׁים שְׁקָלִים יִתֵּן לַאדֹנָיו וְהַשּׁוֹר יִסָּקֵל›
# (“silver thirty weight set to-lord-him/its and-the-bullock be-weighty”) —
# standing handler — if servant butt-with-the-horns the-bullock o
# maidservant then silver thirty weight set to-adonav, and-the-bullock be-
# weighty
m.handler("eved yigach ha-shor o ama",
          "kesef sheloshim sheqalim yiten la-adonav, ve-ha-shor yisaqel")

# -------------------------- Exod.21.33 · THE_OPEN_PIT ----------------------
# וְכִי־יִפְתַּח אִישׁ בּוֹר אוֹ כִּי־יִכְרֶה אִישׁ בֹּר וְלֹא יְכַסֶּנּוּ
# וְנָפַל־שָׁמָּה שּׁוֹר אוֹ חֲמוֹר
# "[EN-AID] And when a man opens a pit, or when a man digs a pit, and does
# not cover it — and an ox or a donkey falls in there:"
m.step("Exod.21.33")
# ‹וְכִי־יִפְתַּח אִישׁ בּוֹר אוֹ כִּי־יִכְרֶה אִישׁ בֹּר וְלֹא יְכַסֶּנּוּ›
# (“and-that open-wide man pit or that dig man pit and-not plump-him/its”) —
# case and-khi open-wide man pit o that dig man pit and-not yekhasenu routes
# to master-the-pit
m.case("ve-khi yiftach ish bor o ki yikhre ish bor ve-lo yekhasenu", "baal_ha_bor")

# -------------------------- Exod.21.34 · THE_PIT_PAYS ----------------------
# בַּעַל הַבּוֹר יְשַׁלֵּם כֶּסֶף יָשִׁיב לִבְעָלָיו וְהַמֵּת יִהְיֶה־לּוֹ
# "[EN-AID] The owner of the pit shall pay; silver he shall return to its
# owner — and the dead shall be his."
m.step("Exod.21.34")
# ‹בַּעַל הַבּוֹר יְשַׁלֵּם כֶּסֶף יָשִׁיב לִבְעָלָיו› (“master the-pit be-
# safe silver return to-master-him/its”) — standing handler — if fall shama
# bullock o male-ass then master the-pit be-safe, silver return to-me-vealav
m.handler("nafal shama shor o chamor",
          "baal ha-bor yeshalem, kesef yashiv li-vealav")

# -------------------------- Exod.21.35 · OX_AGAINST_OX ---------------------
# וְכִי־יִגֹּף שׁוֹר־אִישׁ אֶת־שׁוֹר רֵעֵהוּ וָמֵת וּמָכְרוּ אֶת־הַשּׁוֹר
# הַחַי וְחָצוּ אֶת־כַּסְפּוֹ וְגַם אֶת־הַמֵּת יֶחֱצוּן
# "[EN-AID] And when a man's ox strikes his fellow's ox, and it dies — they
# shall sell the living ox and divide its silver, and the dead one they
# shall also divide."
m.step("Exod.21.35")
# ‹וְכִי־יִגֹּף שׁוֹר־אִישׁ אֶת־שׁוֹר רֵעֵהוּ וָמֵת› (“and-that push bullock
# man obj-marker bullock associate-him/its and-die”) — case and-khi push
# bullock man obj-marker bullock reehu and-die routes to bullock-obj-marker-
# bullock
m.case("ve-khi yigof shor ish et shor reehu va-met", "shor_et_shor")

# -------------------------- Exod.21.36 · THE_KNOWN_GORER -------------------
# אוֹ נוֹדַע כִּי שׁוֹר נַגָּח הוּא מִתְּמוֹל שִׁלְשֹׁם וְלֹא יִשְׁמְרֶנּוּ
# בְּעָלָיו שַׁלֵּם יְשַׁלֵּם שׁוֹר תַּחַת הַשּׁוֹר וְהַמֵּת יִהְיֶה־לּוֹ
# "[EN-AID] Or it was known that it was a goring ox from yesterday and the
# day before, and its owner did not guard it — he shall surely pay ox for
# ox, and the dead shall be his."
m.step("Exod.21.36")
# ‹שַׁלֵּם יְשַׁלֵּם שׁוֹר תַּחַת הַשּׁוֹר› (“be-safe be-safe bullock under
# the-bullock”) — standing handler — if know that bullock butting he/it
# from-ago trebly and-not yishmerenu bealav then be-safe be-safe bullock
# under the-bullock
m.handler("noda ki shor nagach hu mi-temol shilshom ve-lo yishmerenu bealav",
          "shalem yeshalem shor tachat ha-shor")

# -------------------------- Exod.21.37 · FIVE_OXEN_FOUR_SHEEP --------------
# כִּי יִגְנֹב־אִישׁ שׁוֹר אוֹ־שֶׂה וּטְבָחוֹ אוֹ מְכָרוֹ חֲמִשָּׁה בָקָר
# יְשַׁלֵּם תַּחַת הַשּׁוֹר וְאַרְבַּע־צֹאן תַּחַת הַשֶּׂה
# "[EN-AID] When a man steals an ox or a sheep, and slaughters it or sells
# it — five oxen he shall pay for the ox, and four sheep for the sheep."
m.step("Exod.21.37")
# ‹כִּי יִגְנֹב־אִישׁ שׁוֹר אוֹ־שֶׂה וּטְבָחוֹ אוֹ מְכָרוֹ› (“that steal man
# bullock or member-of-a-flock and-slaughter-him/its or sell-him/its”) —
# case that steal man bullock o member-of-a-flock u-tevacho o mekharo routes
# to ganav-bullock-or-member-of-a-flock
m.case("ki yignov ish shor o se u-tevacho o mekharo", "ganav_shor_o_se")

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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
