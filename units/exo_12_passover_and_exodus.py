#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_12_passover_and_exodus — 12:1-51
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_12_passover_and_exodus.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The passover and the exodus (12:1-51)"""
from machine import Machine

m = Machine("exo_12_passover_and_exodus")

# -------------------------- Exod.12.1 · IN_THE_LAND_OF_EGYPT ---------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן בְּאֶרֶץ מִצְרַיִם לֵאמֹר
# "[EN-AID] And the LORD said to Moses and to Aaron in the land of Egypt,
# saying:"
m.step("Exod.12.1")
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן בְּאֶרֶץ מִצְרַיִם לֵאמֹר›
# (“and-say YHWH to Moses and-to Aaron in-earth Egypt to-say”) — fact holds:
# daber-in-earth-Egypt
m.fact("daber_be_eretz_mitzrayim")

# -------------------------- Exod.12.2 · HEAD_OF_MONTHS ---------------------
# הַחֹדֶשׁ הַזֶּה לָכֶם רֹאשׁ חֳדָשִׁים רִאשׁוֹן הוּא לָכֶם לְחָדְשֵׁי
# הַשָּׁנָה
# "[EN-AID] This month is for you the head of months; first is it for you of
# the months of the year."
m.step("Exod.12.2")
# ‹הַחֹדֶשׁ הַזֶּה לָכֶם רֹאשׁ חֳדָשִׁים› (“the-new-moon the-this to-
# you/your(pl) head new-moon”) — the-LORD speaks a demand — LET: the-new-
# moon-the-this-head
m.declare("YHWH", "LET",
          "ha_chodesh_ha_ze_rosh")

# -------------------------- Exod.12.3 · A_LAMB_FOR_A_HOUSE -----------------
# דַּבְּרוּ אֶל־כָּל־עֲדַת יִשְׂרָאֵל לֵאמֹר בֶּעָשֹׂר לַחֹדֶשׁ הַזֶּה
# וְיִקְחוּ לָהֶם אִישׁ שֶׂה לְבֵית־אָבֹת שֶׂה לַבָּיִת
# "[EN-AID] Speak to all the congregation of Israel, saying: On the tenth of
# this month let them take, each man, a lamb for a fathers' house, a lamb
# for a house."
m.step("Exod.12.3")
# ‹וְיִקְחוּ לָהֶם אִישׁ שֶׂה לְבֵית־אָבֹת שֶׂה לַבָּיִת› (“and-take to-
# them/their man member-of-a-flock to-house father member-of-a-flock to-
# house”) — the-LORD speaks a demand — LET: and-take-man-member-of-a-flock-
# to-house
m.declare("YHWH", "LET",
          "ve_yiqchu_ish_se_la_bayit")

# -------------------------- Exod.12.4 · ACCORDING_TO_HIS_EATING ------------
# וְאִם־יִמְעַט הַבַּיִת מִהְיֹת מִשֶּׂה וְלָקַח הוּא וּשְׁכֵנוֹ הַקָּרֹב
# אֶל־בֵּיתוֹ בְּמִכְסַת נְפָשֹׁת אִישׁ לְפִי אָכְלוֹ תָּכֹסּוּ עַל־הַשֶּׂה
# "[EN-AID] And if the house be too little for a lamb, then he and his
# neighbor next to his house shall take, by the count of souls; each man
# according to his eating you shall count for the lamb."
m.step("Exod.12.4")
# ‹בְּמִכְסַת נְפָשֹׁת אִישׁ לְפִי אָכְלוֹ› (“in-enumeration living-being
# man to-mouth food-him/its”) — fact holds: in-enumeration-living-being
m.fact("be_mikhsat_nefashot")

# -------------------------- Exod.12.5 · A_LAMB_UNBLEMISHED -----------------
# שֶׂה תָמִים זָכָר בֶּן־שָׁנָה יִהְיֶה לָכֶם מִן־הַכְּבָשִׂים
# וּמִן־הָעִזִּים תִּקָּחוּ
# "[EN-AID] An unblemished lamb, a male, a year old shall it be for you;
# from the sheep and from the goats shall you take it."
m.step("Exod.12.5")
# ‹שֶׂה תָמִים זָכָר בֶּן־שָׁנָה יִהְיֶה לָכֶם› (“member-of-a-flock entire
# male son years be to-you/your(pl)”) — fact holds: member-of-a-flock-
# entire-male-son-years
m.fact("se_tamim_zakhar_ben_shana")

# -------------------------- Exod.12.6 · BETWEEN_THE_EVENINGS ---------------
# וְהָיָה לָכֶם לְמִשְׁמֶרֶת עַד אַרְבָּעָה עָשָׂר יוֹם לַחֹדֶשׁ הַזֶּה
# וְשָׁחֲטוּ אֹתוֹ כֹּל קְהַל עֲדַת־יִשְׂרָאֵל בֵּין הָעַרְבָּיִם
# "[EN-AID] And it shall be for you for a keeping until the fourteenth day
# of this month; and the whole assembly of the congregation of Israel shall
# slaughter it between the evenings."
m.step("Exod.12.6")
# ‹וְשָׁחֲטוּ אֹתוֹ כֹּל קְהַל עֲדַת־יִשְׂרָאֵל בֵּין הָעַרְבָּיִם› (“and-
# slaughter obj-marker-him/its all assemblage congregation Israel between
# the-evening”) — fact holds: and-slaughter-son-the-evening
m.fact("ve_shachatu_ben_ha_arbayim")

# -------------------------- Exod.12.7 · BLOOD_ON_THE_DOORPOSTS -------------
# וְלָקְחוּ מִן־הַדָּם וְנָתְנוּ עַל־שְׁתֵּי הַמְּזוּזֹת וְעַל־הַמַּשְׁקוֹף
# עַל הַבָּתִּים אֲשֶׁר־יֹאכְלוּ אֹתוֹ בָּהֶם
# "[EN-AID] And they shall take of the blood, and put it on the two
# doorposts and on the lintel, on the houses in which they eat it."
m.step("Exod.12.7")
# ‹וְנָתְנוּ עַל־שְׁתֵּי הַמְּזוּזֹת וְעַל־הַמַּשְׁקוֹף› (“and-set over two
# the-door-post and-over the-lintel”) — fact holds: and-set-over-two-of-the-
# door-post
m.fact("ve_natnu_al_shte_ha_mezuzot")

# -------------------------- Exod.12.8 · ROASTED_IN_FIRE --------------------
# וְאָכְלוּ אֶת־הַבָּשָׂר בַּלַּיְלָה הַזֶּה צְלִי־אֵשׁ וּמַצּוֹת
# עַל־מְרֹרִים יֹאכְלֻהוּ
# "[EN-AID] And they shall eat the flesh in this night, roasted in fire; and
# unleavened bread, with bitter herbs they shall eat it."
m.step("Exod.12.8")
# ‹וְאָכְלוּ אֶת־הַבָּשָׂר בַּלַּיְלָה הַזֶּה› (“and-eat obj-marker the-
# flesh in-night the-this”) — fact holds: and-eat-obj-marker-the-flesh-in-
# the-night
m.fact("ve_akhlu_et_ha_basar_ba_layla")

# -------------------------- Exod.12.9 · NOT_RAW_NOR_BOILED -----------------
# אַל־תֹּאכְלוּ מִמֶּנּוּ נָא וּבָשֵׁל מְבֻשָּׁל בַּמָּיִם כִּי
# אִם־צְלִי־אֵשׁ רֹאשׁוֹ עַל־כְּרָעָיו וְעַל־קִרְבּוֹ
# "[EN-AID] Do not eat of it raw, nor boiled at all in water — but roasted
# in fire, its head with its legs and with its inner parts."
m.step("Exod.12.9")
# ‹אַל־תֹּאכְלוּ מִמֶּנּוּ נָא וּבָשֵׁל מְבֻשָּׁל בַּמָּיִם› (“do-not eat
# from-us/our tough and-boiled boil-up in-waters”) — fact holds: over-eat-
# tough-and-boiled
m.fact("al_tokhlu_na_u_vashel")

# -------------------------- Exod.12.10 · NOTHING_LEFT_TILL_MORNING ---------
# וְלֹא־תוֹתִירוּ מִמֶּנּוּ עַד־בֹּקֶר וְהַנֹּתָר מִמֶּנּוּ עַד־בֹּקֶר
# בָּאֵשׁ תִּשְׂרֹפוּ
# "[EN-AID] And you shall not leave any of it until morning; and what
# remains of it until morning you shall burn in fire."
m.step("Exod.12.10")
# ‹וְהַנֹּתָר מִמֶּנּוּ עַד־בֹּקֶר בָּאֵשׁ תִּשְׂרֹפוּ› (“and-the-jut-over
# from-us/our until morning in-fire be-on-fire”) — fact holds: and-the-jut-
# over-in-the-fire-be-on-fire
m.fact("ve_ha_notar_ba_esh_tisrofu")

# -------------------------- Exod.12.11 · EAT_IT_IN_HASTE -------------------
# וְכָכָה תֹּאכְלוּ אֹתוֹ מָתְנֵיכֶם חֲגֻרִים נַעֲלֵיכֶם בְּרַגְלֵיכֶם
# וּמַקֶּלְכֶם בְּיֶדְכֶם וַאֲכַלְתֶּם אֹתוֹ בְּחִפָּזוֹן פֶּסַח הוּא
# לַיהוָה
# "[EN-AID] And thus shall you eat it: your loins girded, your shoes on your
# feet, and your staff in your hand; and you shall eat it in haste — it is a
# passover to the LORD."
m.step("Exod.12.11")
# ‹פֶּסַח הוּא לַיהוָה› (“pretermission he/it to-YHWH”) — fact holds:
# pretermission-he/it-to-the-LORD
m.fact("pesach_hu_la_YHWH")

# -------------------------- Exod.12.12 · JUDGMENTS_ON_ALL_THE_GODS ---------
# וְעָבַרְתִּי בְאֶרֶץ־מִצְרַיִם בַּלַּיְלָה הַזֶּה וְהִכֵּיתִי כָל־בְּכוֹר
# בְּאֶרֶץ מִצְרַיִם מֵאָדָם וְעַד־בְּהֵמָה וּבְכָל־אֱלֹהֵי מִצְרַיִם
# אֶעֱשֶׂה שְׁפָטִים אֲנִי יְהוָה
# "[EN-AID] And I will pass through the land of Egypt in this night, and I
# will strike every firstborn in the land of Egypt, from man to beast; and
# on all the gods of Egypt I will do judgments — I am the LORD."
m.step("Exod.12.12")
# ‹וּבְכָל־אֱלֹהֵי מִצְרַיִם אֶעֱשֶׂה שְׁפָטִים אֲנִי יְהוָה› (“and-in-all
# God Egypt make sentence YHWH”) — fact holds: and-pass-over-and-strike-all-
# firstborn
m.fact("ve_avarti_ve_hiketi_khol_bekhor")

# -------------------------- Exod.12.13 · THE_BLOOD_A_SIGN ------------------
# וְהָיָה הַדָּם לָכֶם לְאֹת עַל הַבָּתִּים אֲשֶׁר אַתֶּם שָׁם וְרָאִיתִי
# אֶת־הַדָּם וּפָסַחְתִּי עֲלֵכֶם וְלֹא־יִהְיֶה בָכֶם נֶגֶף לְמַשְׁחִית
# בְּהַכֹּתִי בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And the blood shall be for you a sign on the houses where you
# are; and I will see the blood and pass over you, and there shall be no
# plague on you for a destroyer, when I strike in the land of Egypt."
m.step("Exod.12.13")
# ‹וְרָאִיתִי אֶת־הַדָּם וּפָסַחְתִּי עֲלֵכֶם› (“and-see obj-marker the-
# blood and-hop over-you/your(pl)”) — fact holds: and-evil-iti-obj-marker-
# the-blood-and-hop
m.fact("ve_ra_iti_et_ha_dam_u_fasachti")

# -------------------------- Exod.12.14 · A_MEMORIAL_FEAST_FOREVER ----------
# וְהָיָה הַיּוֹם הַזֶּה לָכֶם לְזִכָּרוֹן וְחַגֹּתֶם אֹתוֹ חַג לַיהוָה
# לְדֹרֹתֵיכֶם חֻקַּת עוֹלָם תְּחָגֻּהוּ
# "[EN-AID] And this day shall be for you for a memorial, and you shall
# feast it as a feast to the LORD; through your generations, an everlasting
# statute you shall feast it."
m.step("Exod.12.14")
# ‹וְהָיָה הַיּוֹם הַזֶּה לָכֶם לְזִכָּרוֹן וְחַגֹּתֶם אֹתוֹ חַג לַיהוָה›
# (“and-be the-day the-this to-you/your(pl) to-memento and-move-in-acircle
# obj-marker-him/its festival to-YHWH”) — the-LORD speaks a demand — LET:
# and-move-in-acircle-it-festival
m.declare("YHWH", "LET",
          "ve_chagotem_oto_chag")

# -------------------------- Exod.12.15 · SEVEN_DAYS_UNLEAVENED -------------
# שִׁבְעַת יָמִים מַצּוֹת תֹּאכֵלוּ אַךְ בַּיּוֹם הָרִאשׁוֹן תַּשְׁבִּיתוּ
# שְּׂאֹר מִבָּתֵּיכֶם כִּי כָּל־אֹכֵל חָמֵץ וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא
# מִיִּשְׂרָאֵל מִיּוֹם הָרִאשֹׁן עַד־יוֹם הַשְּׁבִעִי
# "[EN-AID] Seven days you shall eat unleavened bread; but on the first day
# you shall remove leaven from your houses — for whoever eats leavened
# bread, that soul shall be cut off from Israel, from the first day until
# the seventh day."
m.step("Exod.12.15")
# ‹שִׁבְעַת יָמִים מַצּוֹת תֹּאכֵלוּ› (“seven day sweetness eat”) — the-LORD
# speaks a demand — LET: seven-day-sweetness-eat
m.declare("YHWH", "LET",
          "shivat_yamim_matzot_tokhelu")

# -------------------------- Exod.12.16 · HOLY_CONVOCATIONS -----------------
# וּבַיּוֹם הָרִאשׁוֹן מִקְרָא־קֹדֶשׁ וּבַיּוֹם הַשְּׁבִיעִי מִקְרָא־קֹדֶשׁ
# יִהְיֶה לָכֶם כָּל־מְלָאכָה לֹא־יֵעָשֶׂה בָהֶם אַךְ אֲשֶׁר יֵאָכֵל
# לְכָל־נֶפֶשׁ הוּא לְבַדּוֹ יֵעָשֶׂה לָכֶם
# "[EN-AID] And on the first day a holy convocation, and on the seventh day
# a holy convocation shall be for you; no work shall be done on them — only
# what is eaten by every soul, that alone may be done for you."
m.step("Exod.12.16")
# ‹וּבַיּוֹם הָרִאשׁוֹן מִקְרָא־קֹדֶשׁ וּבַיּוֹם הַשְּׁבִיעִי מִקְרָא־קֹדֶשׁ
# יִהְיֶה לָכֶם› (“and-in-day the-first something-called-out holiness and-
# in-day the-seventh something-called-out holiness be to-you/your(pl)”) —
# fact holds: something-called-out-holiness-first-and-seventh
m.fact("miqra_qodesh_rishon_u_shevii")

# -------------------------- Exod.12.17 · GUARD_THE_MATZOT ------------------
# וּשְׁמַרְתֶּם אֶת־הַמַּצּוֹת כִּי בְּעֶצֶם הַיּוֹם הַזֶּה הוֹצֵאתִי
# אֶת־צִבְאוֹתֵיכֶם מֵאֶרֶץ מִצְרָיִם וּשְׁמַרְתֶּם אֶת־הַיּוֹם הַזֶּה
# לְדֹרֹתֵיכֶם חֻקַּת עוֹלָם
# "[EN-AID] And you shall guard the unleavened bread, for on this very day I
# brought out your hosts from the land of Egypt; and you shall guard this
# day through your generations, an everlasting statute."
m.step("Exod.12.17")
# ‹וּשְׁמַרְתֶּם אֶת־הַמַּצּוֹת› (“and-keep/guard obj-marker the-sweetness”)
# — fact holds: and-keep/guard-obj-marker-the-sweetness
m.fact("u_shemartem_et_ha_matzot")

# -------------------------- Exod.12.18 · THE_FOUR_LEAN_MATZOT --------------
# בָּרִאשֹׁן בְּאַרְבָּעָה עָשָׂר יוֹם לַחֹדֶשׁ בָּעֶרֶב תֹּאכְלוּ מַצֹּת
# עַד יוֹם הָאֶחָד וְעֶשְׂרִים לַחֹדֶשׁ בָּעָרֶב
# "[EN-AID] In the first month, on the fourteenth day of the month in the
# evening, you shall eat unleavened bread, until the twenty-first day of the
# month in the evening."
m.step("Exod.12.18")
# ‹בָּרִאשֹׁן בְּאַרְבָּעָה עָשָׂר יוֹם לַחֹדֶשׁ בָּעֶרֶב תֹּאכְלוּ מַצֹּת›
# (“in-first in-four -teen day to-new-moon in-evening eat sweetness”) — fact
# holds: in-the-web-eat-sweetness
m.fact("ba_erev_tokhlu_matzot")

# -------------------------- Exod.12.19 · NO_LEAVEN_IN_YOUR_HOUSES ----------
# שִׁבְעַת יָמִים שְׂאֹר לֹא יִמָּצֵא בְּבָתֵּיכֶם כִּי כָּל־אֹכֵל מַחְמֶצֶת
# וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא מֵעֲדַת יִשְׂרָאֵל בַּגֵּר וּבְאֶזְרַח
# הָאָרֶץ
# "[EN-AID] Seven days leaven shall not be found in your houses; for whoever
# eats what is leavened, that soul shall be cut off from the congregation of
# Israel — among the sojourner and among the native of the land."
m.step("Exod.12.19")
# ‹בַּגֵּר וּבְאֶזְרַח הָאָרֶץ› (“in-sojourner and-in-spontaneous-growth
# the-earth”) — fact holds: in-the-sojourner-and-and-spontaneous-growth-the-
# earth
m.fact("ba_ger_u_ve_ezrach_ha_aretz")

# -------------------------- Exod.12.20 · IN_ALL_YOUR_DWELLINGS -------------
# כָּל־מַחְמֶצֶת לֹא תֹאכֵלוּ בְּכֹל מוֹשְׁבֹתֵיכֶם תֹּאכְלוּ מַצּוֹת
# "[EN-AID] You shall eat nothing leavened; in all your dwellings you shall
# eat unleavened bread."
m.step("Exod.12.20")
# ‹בְּכֹל מוֹשְׁבֹתֵיכֶם תֹּאכְלוּ מַצּוֹת› (“in-all seat-you/your(pl) eat
# sweetness”) — fact holds: in-all-moshvotekhem-sweetness
m.fact("be_khol_moshvotekhem_matzot")

# -------------------------- Exod.12.21 · DRAW_OUT_AND_TAKE -----------------
# וַיִּקְרָא מֹשֶׁה לְכָל־זִקְנֵי יִשְׂרָאֵל וַיֹּאמֶר אֲלֵהֶם מִשְׁכוּ
# וּקְחוּ לָכֶם צֹאן לְמִשְׁפְּחֹתֵיכֶם וְשַׁחֲטוּ הַפָּסַח
# "[EN-AID] And Moses called for all the elders of Israel, and said to them:
# Draw out and take for yourselves flocks according to your families, and
# slaughter the passover."
m.step("Exod.12.21")
# ‹מִשְׁכוּ וּקְחוּ לָכֶם צֹאן לְמִשְׁפְּחֹתֵיכֶם וְשַׁחֲטוּ הַפָּסַח›
# (“draw and-take to-you/your(pl) flock to-family-you/your(pl) and-slaughter
# the-pretermission”) — Moses speaks a demand — LET: draw-and-take-flock
m.declare("moshe", "LET",
          "mishkhu_u_qechu_tzon")

# -------------------------- Exod.12.22 · HYSSOP_AND_THRESHOLD --------------
# וּלְקַחְתֶּם אֲגֻדַּת אֵזוֹב וּטְבַלְתֶּם בַּדָּם אֲשֶׁר־בַּסַּף
# וְהִגַּעְתֶּם אֶל־הַמַּשְׁקוֹף וְאֶל־שְׁתֵּי הַמְּזוּזֹת מִן־הַדָּם אֲשֶׁר
# בַּסָּף וְאַתֶּם לֹא תֵצְאוּ אִישׁ מִפֶּתַח־בֵּיתוֹ עַד־בֹּקֶר
# "[EN-AID] And you shall take a bundle of hyssop, and dip it in the blood
# that is in the basin, and touch the lintel and the two doorposts with the
# blood that is in the basin; and you — none of you shall go out from the
# opening of his house until morning."
m.step("Exod.12.22")
# ‹וְאַתֶּם לֹא תֵצְאוּ אִישׁ מִפֶּתַח־בֵּיתוֹ עַד־בֹּקֶר› (“and-you not
# bring-forth man from-opening house-him/its until morning”) — fact holds:
# not-bring-forth-man-from-opening-beto
m.fact("lo_tetzu_ish_mi_petach_beto")

# -------------------------- Exod.12.23 · HE_WILL_NOT_LET_THE_DESTROYER -----
# וְעָבַר יְהוָה לִנְגֹּף אֶת־מִצְרַיִם וְרָאָה אֶת־הַדָּם עַל־הַמַּשְׁקוֹף
# וְעַל שְׁתֵּי הַמְּזוּזֹת וּפָסַח יְהוָה עַל־הַפֶּתַח וְלֹא יִתֵּן
# הַמַּשְׁחִית לָבֹא אֶל־בָּתֵּיכֶם לִנְגֹּף
# "[EN-AID] And the LORD will pass through to strike Egypt, and He will see
# the blood on the lintel and on the two doorposts; and the LORD will pass
# over the opening, and will not let the destroyer come into your houses to
# strike."
m.step("Exod.12.23")
# ‹וּפָסַח יְהוָה עַל־הַפֶּתַח› (“and-hop YHWH over the-opening”) — fact
# holds: and-hop-the-LORD-over-the-opening
m.fact("u_fasach_YHWH_al_ha_petach")

# -------------------------- Exod.12.24 · A_STATUTE_FOREVER -----------------
# וּשְׁמַרְתֶּם אֶת־הַדָּבָר הַזֶּה לְחָק־לְךָ וּלְבָנֶיךָ עַד־עוֹלָם
# "[EN-AID] And you shall guard this thing as a statute for you and for your
# sons, forever."
m.step("Exod.12.24")
# ‹לְחָק־לְךָ וּלְבָנֶיךָ עַד־עוֹלָם› (“to-enactment to-you/your and-to-son-
# you/your until forever”) — fact holds: to-enactment-to-you-and-to-your-
# sons
m.fact("le_chaq_lekha_u_le_vanekha")

# -------------------------- Exod.12.25 · WHEN_YOU_COME_TO_THE_LAND ---------
# וְהָיָה כִּי־תָבֹאוּ אֶל־הָאָרֶץ אֲשֶׁר יִתֵּן יְהוָה לָכֶם כַּאֲשֶׁר
# דִּבֵּר וּשְׁמַרְתֶּם אֶת־הָעֲבֹדָה הַזֹּאת
# "[EN-AID] And it shall be, when you come to the land which the LORD will
# give you, as He has spoken, that you shall guard this service."
m.step("Exod.12.25")
# ‹וְהָיָה כִּי־תָבֹאוּ אֶל־הָאָרֶץ› (“and-be that come/bring to the-earth”)
# — fact holds: very-widely-used-as-a-relati-come/bring-to-the-earth
m.fact("ki_tavou_el_ha_aretz")

# -------------------------- Exod.12.26 · WHEN_YOUR_SONS_ASK ----------------
# וְהָיָה כִּי־יֹאמְרוּ אֲלֵיכֶם בְּנֵיכֶם מָה הָעֲבֹדָה הַזֹּאת לָכֶם
# "[EN-AID] And it shall be, when your sons say to you: What is this service
# to you?"
m.step("Exod.12.26")
# ‹וְהָיָה כִּי־יֹאמְרוּ אֲלֵיכֶם בְּנֵיכֶם› (“and-be that say to-
# you/your(pl) son-you/your(pl)”) — the-LORD speaks a demand — LET: and-say-
# sacrifice-pretermission
m.declare("YHWH", "LET",
          "va_amartem_zevach_pesach")

# -------------------------- Exod.12.27 · THE_ANSWER_AND_THE_BOW ------------
# וַאֲמַרְתֶּם זֶבַח־פֶּסַח הוּא לַיהוָה אֲשֶׁר פָּסַח עַל־בָּתֵּי
# בְנֵי־יִשְׂרָאֵל בְּמִצְרַיִם בְּנָגְפּוֹ אֶת־מִצְרַיִם וְאֶת־בָּתֵּינוּ
# הִצִּיל וַיִּקֹּד הָעָם וַיִּשְׁתַּחֲוּוּ
# "[EN-AID] Then you shall say: It is a passover-sacrifice to the LORD, who
# passed over the houses of the sons of Israel in Egypt when He struck
# Egypt, and our houses He rescued. And the people bowed and prostrated
# themselves."
m.step("Exod.12.27")
# ‹וַיִּקֹּד הָעָם וַיִּשְׁתַּחֲוּוּ› (“and-shrivel-up the-people and-
# afflict”) — fact holds: and-shrivel-up-the-people-and-yishtachavu
m.fact("va_yiqod_ha_am_va_yishtachavu")

# -------------------------- Exod.12.28 · AND_THEY_DID_SO -------------------
# וַיֵּלְכוּ וַיַּעֲשׂוּ בְּנֵי יִשְׂרָאֵל כַּאֲשֶׁר צִוָּה יְהוָה
# אֶת־מֹשֶׁה וְאַהֲרֹן כֵּן עָשׂוּ
# "[EN-AID] And the sons of Israel went and did as the LORD had commanded
# Moses and Aaron — so they did."
m.step("Exod.12.28")
# ‹וַיֵּלְכוּ וַיַּעֲשׂוּ בְּנֵי יִשְׂרָאֵל› (“and-go and-make son Israel”)
# — demand settled (popped from the queue): and-take-man-member-of-a-flock-
# to-house
m.result("ve_yiqchu_ish_se_la_bayit", tmark="t1")
# ‹כֵּן עָשׂוּ› (“so make”) — demand settled (popped from the queue): draw-
# and-take-flock
m.result("mishkhu_u_qechu_tzon", tmark="t1")

# -------------------------- Exod.12.29 · MIDNIGHT --------------------------
# וַיְהִי בַּחֲצִי הַלַּיְלָה וַיהוָה הִכָּה כָל־בְּכוֹר בְּאֶרֶץ מִצְרַיִם
# מִבְּכֹר פַּרְעֹה הַיֹּשֵׁב עַל־כִּסְאוֹ עַד בְּכוֹר הַשְּׁבִי אֲשֶׁר
# בְּבֵית הַבּוֹר וְכֹל בְּכוֹר בְּהֵמָה
# "[EN-AID] And it was at half of the night: the LORD struck every firstborn
# in the land of Egypt, from the firstborn of Pharaoh sitting on his throne
# to the firstborn of the captive in the dungeon-house, and every firstborn
# of beast."
m.step("Exod.12.29")
# ‹וַיְהִי בַּחֲצִי הַלַּיְלָה וַיהוָה הִכָּה כָל־בְּכוֹר בְּאֶרֶץ
# מִצְרַיִם› (“and-be in-half the-night and-YHWH strike all firstborn in-
# earth Egypt”) — event: makat-bekhorot — agent the-LORD
m.event("makat_bekhorot", agent="YHWH")

# -------------------------- Exod.12.30 · NO_HOUSE_WITHOUT_A_DEAD -----------
# וַיָּקָם פַּרְעֹה לַיְלָה הוּא וְכָל־עֲבָדָיו וְכָל־מִצְרַיִם וַתְּהִי
# צְעָקָה גְדֹלָה בְּמִצְרָיִם כִּי־אֵין בַּיִת אֲשֶׁר אֵין־שָׁם מֵת
# "[EN-AID] And Pharaoh rose at night, he and all his servants and all
# Egypt, and there was a great cry in Egypt — for there was no house where
# there was not a dead one."
m.step("Exod.12.30")
# ‹וַתְּהִי צְעָקָה גְדֹלָה בְּמִצְרָיִם› (“and-be shriek great in-Egypt”) —
# fact holds: shriek-great-in-Egypt
m.fact("tzeaqa_gedola_be_mitzrayim")

# -------------------------- Exod.12.31 · RISE_GO_OUT -----------------------
# וַיִּקְרָא לְמֹשֶׁה וּלְאַהֲרֹן לַיְלָה וַיֹּאמֶר קוּמוּ צְּאוּ מִתּוֹךְ
# עַמִּי גַּם־אַתֶּם גַּם־בְּנֵי יִשְׂרָאֵל וּלְכוּ עִבְדוּ אֶת־יְהוָה
# כְּדַבֶּרְכֶם
# "[EN-AID] And he called for Moses and for Aaron by night, and said: Rise,
# go out from among my people, both you and the sons of Israel — and go,
# serve the LORD as you have spoken."
m.step("Exod.12.31")
# ‹וַיֹּאמֶר קוּמוּ צְּאוּ מִתּוֹךְ עַמִּי› (“and-say arise bring-forth
# from-midst people-me/my”) — fact holds: arise-bring-forth-work/serve-
# khedaberkhem
m.fact("qumu_tzeu_ivdu_khedaberkhem")

# -------------------------- Exod.12.32 · BLESS_ME_ALSO ---------------------
# גַּם־צֹאנְכֶם גַּם־בְּקַרְכֶם קְחוּ כַּאֲשֶׁר דִּבַּרְתֶּם וָלֵכוּ
# וּבֵרַכְתֶּם גַּם־אֹתִי
# "[EN-AID] Both your flocks and your herds take, as you have spoken, and go
# — and bless me also."
m.step("Exod.12.32")
# ‹וּבֵרַכְתֶּם גַּם־אֹתִי› (“and-bless also obj-marker-me/my”) — fact
# holds: and-bless-also-me
m.fact("u_verakhtem_gam_oti")

# -------------------------- Exod.12.33 · EGYPT_PRESSES ---------------------
# וַתֶּחֱזַק מִצְרַיִם עַל־הָעָם לְמַהֵר לְשַׁלְּחָם מִן־הָאָרֶץ כִּי
# אָמְרוּ כֻּלָּנוּ מֵתִים
# "[EN-AID] And Egypt pressed hard upon the people, to hasten to send them
# out of the land — for they said: We are all dead men."
m.step("Exod.12.33")
# ‹כִּי אָמְרוּ כֻּלָּנוּ מֵתִים› (“that say all-us/our die”) — fact holds:
# kulanu-die
m.fact("kulanu_metim")

# -------------------------- Exod.12.34 · DOUGH_BEFORE_LEAVENING ------------
# וַיִּשָּׂא הָעָם אֶת־בְּצֵקוֹ טֶרֶם יֶחְמָץ מִשְׁאֲרֹתָם צְרֻרֹת
# בְּשִׂמְלֹתָם עַל־שִׁכְמָם
# "[EN-AID] And the people carried their dough before it could leaven, their
# kneading-troughs bound in their garments on their shoulders."
m.step("Exod.12.34")
# ‹וַיִּשָּׂא הָעָם אֶת־בְּצֵקוֹ טֶרֶם יֶחְמָץ› (“and-lift/carry the-people
# obj-marker dough-him/its non-occurrence be-pungent”) — fact holds: non-
# occurrence-be-pungent
m.fact("terem_yechmatz")

# -------------------------- Exod.12.35 · THEY_ASKED_AS_MOSES_SAID ----------
# וּבְנֵי־יִשְׂרָאֵל עָשׂוּ כִּדְבַר מֹשֶׁה וַיִּשְׁאֲלוּ מִמִּצְרַיִם
# כְּלֵי־כֶסֶף וּכְלֵי זָהָב וּשְׂמָלֹת
# "[EN-AID] And the sons of Israel did according to the word of Moses: they
# asked of Egypt vessels of silver and vessels of gold, and garments."
m.step("Exod.12.35")
# ‹וַיִּשְׁאֲלוּ מִמִּצְרַיִם כְּלֵי־כֶסֶף וּכְלֵי זָהָב וּשְׂמָלֹת› (“and-
# inquire from-Egypt vessel silver and-vessel gold and-dress”) — fact holds:
# and-inquire-vessel-silver-and-gold
m.fact("va_yishalu_kele_khesef_u_zahav")

# -------------------------- Exod.12.36 · THEY_STRIPPED_EGYPT ---------------
# וַיהוָה נָתַן אֶת־חֵן הָעָם בְּעֵינֵי מִצְרַיִם וַיַּשְׁאִלוּם
# וַיְנַצְּלוּ אֶת־מִצְרָיִם
# "[EN-AID] And the LORD gave the people favor in the eyes of Egypt, and
# they granted their request — and they stripped Egypt."
m.step("Exod.12.36")
# ‹וַיְנַצְּלוּ אֶת־מִצְרָיִם› (“and-snatch-away obj-marker Egypt”) — fact
# holds: and-snatch-away-obj-marker-Egypt
m.fact("va_yenatzlu_et_mitzrayim")

# -------------------------- Exod.12.37 · RAMESES_TO_SUCCOTH ----------------
# וַיִּסְעוּ בְנֵי־יִשְׂרָאֵל מֵרַעְמְסֵס סֻכֹּתָה כְּשֵׁשׁ־מֵאוֹת אֶלֶף
# רַגְלִי הַגְּבָרִים לְבַד מִטָּף
# "[EN-AID] And the sons of Israel journeyed from Rameses toward Succoth,
# about six hundred thousand on foot, the men, besides children."
m.step("Exod.12.37")
# ‹וַיִּסְעוּ בְנֵי־יִשְׂרָאֵל מֵרַעְמְסֵס סֻכֹּתָה› (“and-journey son
# Israel from-Raamses Succoth-ward”) — fact holds: and-journey-from-Raamses-
# sukota
m.fact("va_yisu_me_ramses_sukota")

# -------------------------- Exod.12.38 · THE_MIXED_MULTITUDE ---------------
# וְגַם־עֵרֶב רַב עָלָה אִתָּם וְצֹאן וּבָקָר מִקְנֶה כָּבֵד מְאֹד
# "[EN-AID] And also a mixed multitude went up with them, and flocks and
# herds — very heavy livestock."
m.step("Exod.12.38")
# ‹וְגַם־עֵרֶב רַב עָלָה אִתָּם› (“and-also web many/great go-up with-
# them/their”) — fact holds: web-many/great-go-up-itam
m.fact("erev_rav_ala_itam")

# -------------------------- Exod.12.39 · CAKES_OF_MATZA --------------------
# וַיֹּאפוּ אֶת־הַבָּצֵק אֲשֶׁר הוֹצִיאוּ מִמִּצְרַיִם עֻגֹת מַצּוֹת כִּי
# לֹא חָמֵץ כִּי־גֹרְשׁוּ מִמִּצְרַיִם וְלֹא יָכְלוּ לְהִתְמַהְמֵהַּ
# וְגַם־צֵדָה לֹא־עָשׂוּ לָהֶם
# "[EN-AID] And they baked the dough which they brought out of Egypt into
# cakes of unleavened bread, for it had not leavened — for they were driven
# out of Egypt and could not delay, and also provisions they had not made
# for themselves."
m.step("Exod.12.39")
# ‹כִּי־גֹרְשׁוּ מִמִּצְרַיִם› (“that drive-out-from-a-possession from-
# Egypt”) — fact holds: very-widely-used-as-a-relati-drive-out-from-a-
# possession-from-Egypt
m.fact("ki_gorshu_mi_mitzrayim")

# -------------------------- Exod.12.40 · FOUR_HUNDRED_THIRTY_YEARS ---------
# וּמוֹשַׁב בְּנֵי יִשְׂרָאֵל אֲשֶׁר יָשְׁבוּ בְּמִצְרָיִם שְׁלֹשִׁים שָׁנָה
# וְאַרְבַּע מֵאוֹת שָׁנָה
# "[EN-AID] And the dwelling of the sons of Israel, which they dwelt in
# Egypt, was thirty years and four hundred years."
m.step("Exod.12.40")
# ‹שְׁלֹשִׁים שָׁנָה וְאַרְבַּע מֵאוֹת שָׁנָה› (“thirty years and-four
# hundred years”) — fact holds: seat-430-years
m.fact("moshav_430_shana")

# -------------------------- Exod.12.41 · THE_VERY_DAY_THE_HOSTS_WENT_OUT ---
# וַיְהִי מִקֵּץ שְׁלֹשִׁים שָׁנָה וְאַרְבַּע מֵאוֹת שָׁנָה וַיְהִי בְּעֶצֶם
# הַיּוֹם הַזֶּה יָצְאוּ כָּל־צִבְאוֹת יְהוָה מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And it was at the end of thirty years and four hundred years —
# and it was on this very day: all the hosts of the LORD went out from the
# land of Egypt."
m.step("Exod.12.41")
# ‹וַיְהִי בְּעֶצֶם הַיּוֹם הַזֶּה יָצְאוּ כָּל־צִבְאוֹת יְהוָה› (“and-be
# in-bone the-day the-this bring-forth all host YHWH”) — fact holds: bring-
# forth-all-host-the-LORD
m.fact("yatzu_kol_tzivot_YHWH")

# -------------------------- Exod.12.42 · NIGHT_OF_WATCHINGS ----------------
# לֵיל שִׁמֻּרִים הוּא לַיהוָה לְהוֹצִיאָם מֵאֶרֶץ מִצְרָיִם הוּא־הַלַּיְלָה
# הַזֶּה לַיהוָה שִׁמֻּרִים לְכָל־בְּנֵי יִשְׂרָאֵל לְדֹרֹתָם
# "[EN-AID] A night of watchings is it to the LORD, to bring them out from
# the land of Egypt; it is this night to the LORD — watchings for all the
# sons of Israel through their generations."
m.step("Exod.12.42")
# ‹לֵיל שִׁמֻּרִים הוּא לַיהוָה› (“night observance he/it to-YHWH”) — fact
# holds: night-observance-to-dorotam
m.fact("lel_shimurim_le_dorotam")

# -------------------------- Exod.12.43 · THE_ORDINANCE_OF_THE_PASSOVER -----
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה וְאַהֲרֹן זֹאת חֻקַּת הַפָּסַח כָּל־בֶּן־נֵכָר
# לֹא־יֹאכַל בּוֹ
# "[EN-AID] And the LORD said to Moses and Aaron: This is the ordinance of
# the passover: no foreigner shall eat of it."
m.step("Exod.12.43")
# ‹זֹאת חֻקַּת הַפָּסַח› (“this statute the-pretermission”) — the-LORD
# speaks a demand — LET: this-statute-the-pretermission
m.declare("YHWH", "LET",
          "zot_chuqat_ha_pasach")

# -------------------------- Exod.12.44 · BOUGHT_AND_CIRCUMCISED ------------
# וְכָל־עֶבֶד אִישׁ מִקְנַת־כָּסֶף וּמַלְתָּה אֹתוֹ אָז יֹאכַל בּוֹ
# "[EN-AID] And every man's servant, bought with silver — you shall
# circumcise him; then he may eat of it."
m.step("Exod.12.44")
# ‹וּמַלְתָּה אֹתוֹ אָז יֹאכַל בּוֹ› (“and-circumcise obj-marker-him/its at-
# that-time eat in-him/its”) — fact holds: and-circumcise-it-at-that-time-
# eat
m.fact("u_malta_oto_az_yokhal")

# -------------------------- Exod.12.45 · SOJOURNER_AND_HIRELING ------------
# תּוֹשָׁב וְשָׂכִיר לֹא־יֹאכַל־בּוֹ
# "[EN-AID] A settler and a hireling shall not eat of it."
m.step("Exod.12.45")
# ‹תּוֹשָׁב וְשָׂכִיר לֹא־יֹאכַל־בּוֹ› (“resident-alien and-man-at-wages-by-
# the-day not eat in-him/its”) — fact holds: resident-alien-and-man-at-
# wages-by-the-day-not-eat
m.fact("toshav_ve_sakhir_lo_yokhal")

# -------------------------- Exod.12.46 · NO_BONE_BROKEN --------------------
# בְּבַיִת אֶחָד יֵאָכֵל לֹא־תוֹצִיא מִן־הַבַּיִת מִן־הַבָּשָׂר חוּצָה
# וְעֶצֶם לֹא תִשְׁבְּרוּ־בוֹ
# "[EN-AID] In one house shall it be eaten; you shall not take any of the
# flesh outside from the house; and a bone you shall not break in it."
m.step("Exod.12.46")
# ‹וְעֶצֶם לֹא תִשְׁבְּרוּ־בוֹ› (“and-bone not burst in-him/its”) — fact
# holds: and-bone-not-tishberu-come/bring
m.fact("ve_etzem_lo_tishberu_vo")

# -------------------------- Exod.12.47 · ALL_THE_CONGREGATION --------------
# כָּל־עֲדַת יִשְׂרָאֵל יַעֲשׂוּ אֹתוֹ
# "[EN-AID] All the congregation of Israel shall do it."
m.step("Exod.12.47")
# ‹כָּל־עֲדַת יִשְׂרָאֵל יַעֲשׂוּ אֹתוֹ› (“all congregation Israel make obj-
# marker-him/its”) — fact holds: all-congregation-Israel-make
m.fact("kol_adat_yisrael_yaasu")

# -------------------------- Exod.12.48 · THE_GER_WHO_DRAWS_NEAR ------------
# וְכִי־יָגוּר אִתְּךָ גֵּר וְעָשָׂה פֶסַח לַיהוָה הִמּוֹל לוֹ כָל־זָכָר
# וְאָז יִקְרַב לַעֲשֹׂתוֹ וְהָיָה כְּאֶזְרַח הָאָרֶץ וְכָל־עָרֵל לֹא־יֹאכַל
# בּוֹ
# "[EN-AID] And when a sojourner sojourns with you and would do a passover
# to the LORD, every male of his shall be circumcised, and then he may draw
# near to do it, and he shall be as a native of the land; and no
# uncircumcised one shall eat of it."
m.step("Exod.12.48")
# ‹וְהָיָה כְּאֶזְרַח הָאָרֶץ› (“and-be like-spontaneous-growth the-earth”)
# — fact holds: and-be-like-spontaneous-growth-the-earth
m.fact("ve_haya_ke_ezrach_ha_aretz")

# -------------------------- Exod.12.49 · ONE_TORAH -------------------------
# תּוֹרָה אַחַת יִהְיֶה לָאֶזְרָח וְלַגֵּר הַגָּר בְּתוֹכְכֶם
# "[EN-AID] One law shall there be for the native and for the sojourner who
# sojourns in your midst."
m.step("Exod.12.49")
# ‹תּוֹרָה אַחַת יִהְיֶה לָאֶזְרָח› (“precept one be to-spontaneous-growth”)
# — fact holds: precept-one-to-spontaneous-growth-and-to-sojourner
m.fact("tora_achat_la_ezrach_ve_la_ger")

# -------------------------- Exod.12.50 · AS_COMMANDED_SO_THEY_DID ----------
# וַיַּעֲשׂוּ כָּל־בְּנֵי יִשְׂרָאֵל כַּאֲשֶׁר צִוָּה יְהוָה אֶת־מֹשֶׁה
# וְאֶת־אַהֲרֹן כֵּן עָשׂוּ
# "[EN-AID] And all the sons of Israel did as the LORD had commanded Moses
# and Aaron — so they did."
m.step("Exod.12.50")
# ‹וַיַּעֲשׂוּ כָּל־בְּנֵי יִשְׂרָאֵל› (“and-make all son Israel”) — demand
# settled (popped from the queue): this-statute-the-pretermission
m.result("zot_chuqat_ha_pasach", tmark="t1")

# -------------------------- Exod.12.51 · ON_THIS_VERY_DAY_HE_BROUGHT_THEM_OUT -
# וַיְהִי בְּעֶצֶם הַיּוֹם הַזֶּה הוֹצִיא יְהוָה אֶת־בְּנֵי יִשְׂרָאֵל
# מֵאֶרֶץ מִצְרַיִם עַל־צִבְאֹתָם
# "[EN-AID] And it was on this very day: the LORD brought out the sons of
# Israel from the land of Egypt, by their hosts."
m.step("Exod.12.51")
# ‹הוֹצִיא יְהוָה אֶת־בְּנֵי יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם עַל־צִבְאֹתָם›
# (“bring-forth YHWH obj-marker son Israel from-earth Egypt over host-
# them/their”) — event: yetziat-Egypt — agent the-LORD
m.event("yetziat_mitzrayim", agent="YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['ha_chodesh_ha_ze_rosh', 've_chagotem_oto_chag', 'shivat_yamim_matzot_tokhelu', 'va_amartem_zevach_pesach']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['daber_be_eretz_mitzrayim', 'be_mikhsat_nefashot', 'se_tamim_zakhar_ben_shana', 've_shachatu_ben_ha_arbayim', 've_natnu_al_shte_ha_mezuzot', 've_akhlu_et_ha_basar_ba_layla', 'al_tokhlu_na_u_vashel', 've_ha_notar_ba_esh_tisrofu', 'pesach_hu_la_YHWH', 've_avarti_ve_hiketi_khol_bekhor', 've_ra_iti_et_ha_dam_u_fasachti', 'miqra_qodesh_rishon_u_shevii', 'u_shemartem_et_ha_matzot', 'ba_erev_tokhlu_matzot', 'ba_ger_u_ve_ezrach_ha_aretz', 'be_khol_moshvotekhem_matzot', 'lo_tetzu_ish_mi_petach_beto', 'u_fasach_YHWH_al_ha_petach', 'le_chaq_lekha_u_le_vanekha', 'ki_tavou_el_ha_aretz', 'va_yiqod_ha_am_va_yishtachavu', 'tzeaqa_gedola_be_mitzrayim', 'qumu_tzeu_ivdu_khedaberkhem', 'u_verakhtem_gam_oti', 'kulanu_metim', 'terem_yechmatz', 'va_yishalu_kele_khesef_u_zahav', 'va_yenatzlu_et_mitzrayim', 'va_yisu_me_ramses_sukota', 'erev_rav_ala_itam', 'ki_gorshu_mi_mitzrayim', 'moshav_430_shana', 'yatzu_kol_tzivot_YHWH', 'lel_shimurim_le_dorotam', 'u_malta_oto_az_yokhal', 'toshav_ve_sakhir_lo_yokhal', 've_etzem_lo_tishberu_vo', 'kol_adat_yisrael_yaasu', 've_haya_ke_ezrach_ha_aretz', 'tora_achat_la_ezrach_ve_la_ger'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
