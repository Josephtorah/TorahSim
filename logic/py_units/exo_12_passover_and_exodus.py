#!/usr/bin/env python3
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
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹וְאֶל־אַהֲרֹן בְּאֶרֶץ מִצְרַיִם› (“and-to Aaron in-earth Egypt”)
# ‹לֵאמֹר› (“to-say”)
# "[EN-AID] And the LORD said to Moses and to Aaron in the land of Egypt,
# saying:"
m.step("Exod.12.1")
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹וְאֶל־אַהֲרֹן בְּאֶרֶץ מִצְרַיִם› (“and-to Aaron in-earth Egypt”)
# ‹לֵאמֹר› (“to-say”)
# — fact holds: daber-in-earth-Egypt
m.fact("daber_be_eretz_mitzrayim")

# -------------------------- Exod.12.2 · HEAD_OF_MONTHS ---------------------
# ‹הַחֹדֶשׁ הַזֶּה לָכֶם› (“the-new-moon the-this to-you/your(pl)”)
# ‹רֹאשׁ חֳדָשִׁים רִאשׁוֹן› (“head new-moon first”)
# ‹הוּא לָכֶם לְחָדְשֵׁי› (“he/it to-you/your(pl) to-new-moon”)
# ‹הַשָּׁנָה› (“the-years”)
# "[EN-AID] This month is for you the head of months; first is it for you of
# the months of the year."
m.step("Exod.12.2")
# ‹הַחֹדֶשׁ הַזֶּה לָכֶם› (“the-new-moon the-this to-you/your(pl)”)
# ‹רֹאשׁ חֳדָשִׁים› (“head new-moon”)
# — the-LORD speaks a demand — LET: the-new-moon-the-this-head
m.declare("YHWH", "LET",
          "ha_chodesh_ha_ze_rosh")
# witness-tier presupposed read: court_procedure on calendar_commission —
# read, not installed
m.witness_read("calendar_commission", "court_procedure",
                cites=["Mishnah Rosh Hashanah 3:1", "Mishnah Rosh Hashanah 1:7", "Mishnah Pesachim 4:9", "Mishnah Yevamot 8:1"])
# witness-tier presupposed read: calendar_machine_derivations on
# calendar_commission — read, not installed
m.witness_read("calendar_commission", "calendar_machine_derivations",
                cites=["Rosh Hashanah 20a:14", "Rosh Hashanah 20a:15", "Rosh Hashanah 20a:16", "Rosh Hashanah 20b:9", "Rosh Hashanah 20b:10", "Rosh Hashanah 20b:11", "Rosh Hashanah 20b:12", "Sanhedrin 12b:8", "Sanhedrin 12b:9", "Sanhedrin 12b:10", "Rosh Hashanah 7a:17", "Rosh Hashanah 7a:18"])

# -------------------------- Exod.12.3 · A_LAMB_FOR_A_HOUSE -----------------
# ‹דַּבְּרוּ אֶל־כָּל־עֲדַת יִשְׂרָאֵל› (“speak to all congregation Israel”)
# ‹לֵאמֹר בֶּעָשֹׂר לַחֹדֶשׁ› (“to-say in-ten to-new-moon”)
# ‹הַזֶּה וְיִקְחוּ לָהֶם› (“the-this and-take to-them/their”)
# ‹אִישׁ שֶׂה לְבֵית־אָבֹת› (“man member-of-a-flock to-house father”)
# ‹שֶׂה לַבָּיִת› (“member-of-a-flock to-house”)
# "[EN-AID] Speak to all the congregation of Israel, saying: On the tenth of
# this month let them take, each man, a lamb for a fathers' house, a lamb
# for a house."
m.step("Exod.12.3")
# ‹וְיִקְחוּ לָהֶם אִישׁ› (“and-take to-them/their man”)
# ‹שֶׂה לְבֵית־אָבֹת שֶׂה› (“member-of-a-flock to-house father member-of-a-
# flock”)
# ‹לַבָּיִת› (“to-house”)
# — the-LORD speaks a demand — LET: and-take-man-member-of-a-flock-to-house
m.declare("YHWH", "LET",
          "ve_yiqchu_ish_se_la_bayit")

# -------------------------- Exod.12.4 · ACCORDING_TO_HIS_EATING ------------
# ‹וְאִם־יִמְעַט הַבַּיִת מִהְיֹת› (“and-if pare-off the-house from-be”)
# ‹מִשֶּׂה וְלָקַח הוּא› (“from-member-of-a-flock and-take he/it”)
# ‹וּשְׁכֵנוֹ הַקָּרֹב אֶל־בֵּיתוֹ› (“and-resident-him/its the-near to
# house-him/its”)
# ‹בְּמִכְסַת נְפָשֹׁת אִישׁ› (“in-enumeration living-being man”)
# ‹לְפִי אָכְלוֹ תָּכֹסּוּ› (“to-mouth food-him/its estimate”)
# ‹עַל־הַשֶּׂה› (“over the-member-of-a-flock”)
# "[EN-AID] And if the house be too little for a lamb, then he and his
# neighbor next to his house shall take, by the count of souls; each man
# according to his eating you shall count for the lamb."
m.step("Exod.12.4")
# ‹בְּמִכְסַת נְפָשֹׁת אִישׁ› (“in-enumeration living-being man”)
# ‹לְפִי אָכְלוֹ› (“to-mouth food-him/its”)
# — fact holds: in-enumeration-living-being
m.fact("be_mikhsat_nefashot")
# witness-tier presupposed read: registration_derivations on count_clause —
# read, not installed
m.witness_read("count_clause", "registration_derivations",
                cites=["Pesachim 61a:9", "Pesachim 61a:10", "Pesachim 89a:22", "Pesachim 90a:12", "Pesachim 88a:6", "Pesachim 91b:3", "Pesachim 99a:2", "Pesachim 59a:1", "Pesachim 61b:6", "Pesachim 78b:10"])

# -------------------------- Exod.12.5 · A_LAMB_UNBLEMISHED -----------------
# ‹שֶׂה תָמִים זָכָר› (“member-of-a-flock entire male”)
# ‹בֶּן־שָׁנָה יִהְיֶה לָכֶם› (“son years be to-you/your(pl)”)
# ‹מִן־הַכְּבָשִׂים וּמִן־הָעִזִּים תִּקָּחוּ› (“from the-ram and-from the-
# she-goat take”)
# "[EN-AID] An unblemished lamb, a male, a year old shall it be for you;
# from the sheep and from the goats shall you take it."
m.step("Exod.12.5")
# ‹שֶׂה תָמִים זָכָר› (“member-of-a-flock entire male”)
# ‹בֶּן־שָׁנָה יִהְיֶה לָכֶם› (“son years be to-you/your(pl)”)
# — fact holds: member-of-a-flock-entire-male-son-years
m.fact("se_tamim_zakhar_ben_shana")
# witness-tier presupposed read: validity_eras_and_the_rider on lamb_spec —
# read, not installed
m.witness_read("lamb_spec", "validity_eras_and_the_rider",
                cites=["Zevachim 25b:15", "Pesachim 96a:8", "Arakhin 13b:2", "Pesachim 96a:7", "Pesachim 95b:1", "Pesachim 95b:2", "Pesachim 70a:5", "Pesachim 70b:6", "Zevachim 7b:17"])

# -------------------------- Exod.12.6 · BETWEEN_THE_EVENINGS ---------------
# ‹וְהָיָה לָכֶם לְמִשְׁמֶרֶת› (“and-be to-you/your(pl) to-watch”)
# ‹עַד אַרְבָּעָה עָשָׂר› (“until four -teen”)
# ‹יוֹם לַחֹדֶשׁ הַזֶּה› (“day to-new-moon the-this”)
# ‹וְשָׁחֲטוּ אֹתוֹ כֹּל› (“and-slaughter obj-marker-him/its all”)
# ‹קְהַל עֲדַת־יִשְׂרָאֵל בֵּין› (“assemblage congregation Israel between”)
# ‹הָעַרְבָּיִם› (“the-evening”)
# "[EN-AID] And it shall be for you for a keeping until the fourteenth day
# of this month; and the whole assembly of the congregation of Israel shall
# slaughter it between the evenings."
m.step("Exod.12.6")
# ‹וְשָׁחֲטוּ אֹתוֹ כֹּל› (“and-slaughter obj-marker-him/its all”)
# ‹קְהַל עֲדַת־יִשְׂרָאֵל בֵּין› (“assemblage congregation Israel between”)
# ‹הָעַרְבָּיִם› (“the-evening”)
# — fact holds: and-slaughter-son-the-evening
m.fact("ve_shachatu_ben_ha_arbayim")
# witness-tier presupposed read: service_laws on slaughter_clause — read,
# not installed
m.witness_read("slaughter_clause", "service_laws",
                cites=["Mishnah Pesachim 5:5", "Mishnah Pesachim 5:3", "Mishnah Pesachim 5:2", "Mishnah Pesachim 7:4", "Mishnah Kiddushin 2:1"])

# -------------------------- Exod.12.7 · BLOOD_ON_THE_DOORPOSTS -------------
# ‹וְלָקְחוּ מִן־הַדָּם וְנָתְנוּ› (“and-take from the-blood and-set”)
# ‹עַל־שְׁתֵּי הַמְּזוּזֹת וְעַל־הַמַּשְׁקוֹף› (“over two the-door-post and-
# over the-lintel”)
# ‹עַל הַבָּתִּים אֲשֶׁר־יֹאכְלוּ› (“over the-house which eat”)
# ‹אֹתוֹ בָּהֶם› (“obj-marker-him/its in-them/their”)
# "[EN-AID] And they shall take of the blood, and put it on the two
# doorposts and on the lintel, on the houses in which they eat it."
m.step("Exod.12.7")
# ‹וְנָתְנוּ עַל־שְׁתֵּי הַמְּזוּזֹת› (“and-set over two the-door-post”)
# ‹וְעַל־הַמַּשְׁקוֹף› (“and-over the-lintel”)
# — fact holds: and-set-over-two-of-the-door-post
m.fact("ve_natnu_al_shte_ha_mezuzot")
# witness-tier presupposed read: doorway_altars on egypt_rite_file — read,
# not installed
m.witness_read("egypt_rite_file", "doorway_altars",
                cites=["Pesachim 96a:4", "Pesachim 96a:5", "Pesachim 96a:6"])

# -------------------------- Exod.12.8 · ROASTED_IN_FIRE --------------------
# ‹וְאָכְלוּ אֶת־הַבָּשָׂר בַּלַּיְלָה› (“and-eat obj-marker the-flesh in-
# night”)
# ‹הַזֶּה צְלִי־אֵשׁ וּמַצּוֹת› (“the-this roasted fire and-sweetness”)
# ‹עַל־מְרֹרִים יֹאכְלֻהוּ› (“over bitter-herb eat-him/its”)
# "[EN-AID] And they shall eat the flesh in this night, roasted in fire; and
# unleavened bread, with bitter herbs they shall eat it."
m.step("Exod.12.8")
# ‹וְאָכְלוּ אֶת־הַבָּשָׂר בַּלַּיְלָה› (“and-eat obj-marker the-flesh in-
# night”)
# ‹הַזֶּה› (“the-this”)
# — fact holds: and-eat-obj-marker-the-flesh-in-the-night
m.fact("ve_akhlu_et_ha_basar_ba_layla")

# -------------------------- Exod.12.9 · NOT_RAW_NOR_BOILED -----------------
# ‹אַל־תֹּאכְלוּ מִמֶּנּוּ נָא› (“do-not eat from-us/our tough”)
# ‹וּבָשֵׁל מְבֻשָּׁל בַּמָּיִם› (“and-boiled boil-up in-waters”)
# ‹כִּי אִם־צְלִי־אֵשׁ רֹאשׁוֹ› (“very-widely-used-as-a-relati as-
# demonstrative roasted fire head-him/its”)
# ‹עַל־כְּרָעָיו וְעַל־קִרְבּוֹ› (“over leg-of-men-him/its and-over nearest-
# part-him/its”)
# "[EN-AID] Do not eat of it raw, nor boiled at all in water — but roasted
# in fire, its head with its legs and with its inner parts."
m.step("Exod.12.9")
# ‹אַל־תֹּאכְלוּ מִמֶּנּוּ נָא› (“do-not eat from-us/our tough”)
# ‹וּבָשֵׁל מְבֻשָּׁל בַּמָּיִם› (“and-boiled boil-up in-waters”)
# — fact holds: over-eat-tough-and-boiled
m.fact("al_tokhlu_na_u_vashel")
# witness-tier presupposed read: eating_regime on roast_clause — read, not
# installed
m.witness_read("roast_clause", "eating_regime",
                cites=["Mishnah Pesachim 2:8", "Mishnah Pesachim 7:1", "Mishnah Beitzah 2:7", "Mishnah Pesachim 10:9", "Mishnah Makkot 3:3"])
# witness-tier presupposed read: derivation_layer on roast_clause — read,
# not installed
m.witness_read("roast_clause", "derivation_layer",
                cites=["Pesachim 41a:8", "Pesachim 41b:1", "Pesachim 41b:11", "Pesachim 74a:2", "Pesachim 75a:4", "Pesachim 76a:2"])

# -------------------------- Exod.12.10 · NOTHING_LEFT_TILL_MORNING ---------
# ‹וְלֹא־תוֹתִירוּ מִמֶּנּוּ עַד־בֹּקֶר› (“and-not jut-over from-us/our
# until morning”)
# ‹וְהַנֹּתָר מִמֶּנּוּ עַד־בֹּקֶר› (“and-the-jut-over from-us/our until
# morning”)
# ‹בָּאֵשׁ תִּשְׂרֹפוּ› (“in-fire be-on-fire”)
# "[EN-AID] And you shall not leave any of it until morning; and what
# remains of it until morning you shall burn in fire."
m.step("Exod.12.10")
# ‹וְהַנֹּתָר מִמֶּנּוּ עַד־בֹּקֶר› (“and-the-jut-over from-us/our until
# morning”)
# ‹בָּאֵשׁ תִּשְׂרֹפוּ› (“in-fire be-on-fire”)
# — fact holds: and-the-jut-over-in-the-fire-be-on-fire
m.fact("ve_ha_notar_ba_esh_tisrofu")
# witness-tier presupposed read: includes_and_overrides on
# second_passover_statute_engine — read, not installed
m.witness_read("second_passover_statute_engine", "includes_and_overrides",
                cites=["Pesachim 95a:1", "Pesachim 95a:2", "Pesachim 95a:3", "Pesachim 95a:4", "Pesachim 95a:7", "Pesachim 95a:8", "Pesachim 95a:11", "Pesachim 95a:12", "Pesachim 95a:13", "Pesachim 95a:14", "Pesachim 95b:1", "Pesachim 95b:3", "Pesachim 95b:5", "Pesachim 95b:6", "Pesachim 95b:8", "Pesachim 95b:9", "Pesachim 95b:10", "Pesachim 95b:11", "Pesachim 95b:12", "Pesachim 95b:13", "Pesachim 95b:14", "Pesachim 95b:15", "Pesachim 95b:16", "Pesachim 96a:2", "Pesachim 96a:3"])

# -------------------------- Exod.12.11 · EAT_IT_IN_HASTE -------------------
# ‹וְכָכָה תֹּאכְלוּ אֹתוֹ› (“and-just-so eat obj-marker-him/its”)
# ‹מָתְנֵיכֶם חֲגֻרִים נַעֲלֵיכֶם› (“waist-you/your(pl) gird-on sandal-
# tongue-you/your(pl)”)
# ‹בְּרַגְלֵיכֶם וּמַקֶּלְכֶם בְּיֶדְכֶם› (“in-foot-you/your(pl) and-shoot-
# you/your(pl) in-hand-you/your(pl)”)
# ‹וַאֲכַלְתֶּם אֹתוֹ בְּחִפָּזוֹן› (“and-eat obj-marker-him/its in-hasty-
# flight”)
# ‹פֶּסַח הוּא לַיהוָה› (“pretermission he/it to-YHWH”)
# "[EN-AID] And thus shall you eat it: your loins girded, your shoes on your
# feet, and your staff in your hand; and you shall eat it in haste — it is a
# passover to the LORD."
m.step("Exod.12.11")
# ‹פֶּסַח הוּא לַיהוָה› (“pretermission he/it to-YHWH”)
# — fact holds: pretermission-he/it-to-the-LORD
m.fact("pesach_hu_la_YHWH")
# witness-tier presupposed read: two_era_table on haste_clause — read, not
# installed
m.witness_read("haste_clause", "two_era_table",
                cites=["Mishnah Pesachim 9:5"])

# -------------------------- Exod.12.12 · JUDGMENTS_ON_ALL_THE_GODS ---------
# ‹וְעָבַרְתִּי בְאֶרֶץ־מִצְרַיִם בַּלַּיְלָה› (“and-pass-over in-earth
# Egypt in-night”)
# ‹הַזֶּה וְהִכֵּיתִי כָל־בְּכוֹר› (“the-this and-strike all firstborn”)
# ‹בְּאֶרֶץ מִצְרַיִם מֵאָדָם› (“in-earth Egypt from-human”)
# ‹וְעַד־בְּהֵמָה וּבְכָל־אֱלֹהֵי מִצְרַיִם› (“and-until livestock and-in-
# all God Egypt”)
# ‹אֶעֱשֶׂה שְׁפָטִים אֲנִי› (“make sentence”)
# ‹יְהוָה› (“YHWH”)
# "[EN-AID] And I will pass through the land of Egypt in this night, and I
# will strike every firstborn in the land of Egypt, from man to beast; and
# on all the gods of Egypt I will do judgments — I am the LORD."
m.step("Exod.12.12")
# ‹וּבְכָל־אֱלֹהֵי מִצְרַיִם אֶעֱשֶׂה› (“and-in-all God Egypt make”)
# ‹שְׁפָטִים אֲנִי יְהוָה› (“sentence YHWH”)
# — fact holds: and-pass-over-and-strike-all-firstborn
m.fact("ve_avarti_ve_hiketi_khol_bekhor")

# -------------------------- Exod.12.13 · THE_BLOOD_A_SIGN ------------------
# ‹וְהָיָה הַדָּם לָכֶם› (“and-be the-blood to-you/your(pl)”)
# ‹לְאֹת עַל הַבָּתִּים› (“to-signs over the-house”)
# ‹אֲשֶׁר אַתֶּם שָׁם› (“which you there”)
# ‹וְרָאִיתִי אֶת־הַדָּם וּפָסַחְתִּי› (“and-see obj-marker the-blood and-
# hop”)
# ‹עֲלֵכֶם וְלֹא־יִהְיֶה בָכֶם› (“over-you/your(pl) and-not be in-
# you/your(pl)”)
# ‹נֶגֶף לְמַשְׁחִית בְּהַכֹּתִי› (“trip to-destructive in-strike-me/my”)
# ‹בְּאֶרֶץ מִצְרָיִם› (“in-earth Egypt”)
# "[EN-AID] And the blood shall be for you a sign on the houses where you
# are; and I will see the blood and pass over you, and there shall be no
# plague on you for a destroyer, when I strike in the land of Egypt."
m.step("Exod.12.13")
# ‹וְרָאִיתִי אֶת־הַדָּם וּפָסַחְתִּי› (“and-see obj-marker the-blood and-
# hop”)
# ‹עֲלֵכֶם› (“over-you/your(pl)”)
# — fact holds: and-evil-iti-obj-marker-the-blood-and-hop
m.fact("ve_ra_iti_et_ha_dam_u_fasachti")

# -------------------------- Exod.12.14 · A_MEMORIAL_FEAST_FOREVER ----------
# ‹וְהָיָה הַיּוֹם הַזֶּה› (“and-be the-day the-this”)
# ‹לָכֶם לְזִכָּרוֹן וְחַגֹּתֶם› (“to-you/your(pl) to-memento and-move-in-
# acircle”)
# ‹אֹתוֹ חַג לַיהוָה› (“obj-marker-him/its festival to-YHWH”)
# ‹לְדֹרֹתֵיכֶם חֻקַּת עוֹלָם› (“to-generation-you/your(pl) statute
# forever”)
# ‹תְּחָגֻּהוּ› (“move-in-acircle-him/its”)
# "[EN-AID] And this day shall be for you for a memorial, and you shall
# feast it as a feast to the LORD; through your generations, an everlasting
# statute you shall feast it."
m.step("Exod.12.14")
# ‹וְהָיָה הַיּוֹם הַזֶּה› (“and-be the-day the-this”)
# ‹לָכֶם לְזִכָּרוֹן וְחַגֹּתֶם› (“to-you/your(pl) to-memento and-move-in-
# acircle”)
# ‹אֹתוֹ חַג לַיהוָה› (“obj-marker-him/its festival to-YHWH”)
# — the-LORD speaks a demand — LET: and-move-in-acircle-it-festival
m.declare("YHWH", "LET",
          "ve_chagotem_oto_chag")

# -------------------------- Exod.12.15 · SEVEN_DAYS_UNLEAVENED -------------
# ‹שִׁבְעַת יָמִים מַצּוֹת› (“seven day sweetness”)
# ‹תֹּאכֵלוּ אַךְ בַּיּוֹם› (“eat indeed in-day”)
# ‹הָרִאשׁוֹן תַּשְׁבִּיתוּ שְּׂאֹר› (“the-first cease barm”)
# ‹מִבָּתֵּיכֶם כִּי כָּל־אֹכֵל› (“from-house-you/your(pl) that all eat”)
# ‹חָמֵץ וְנִכְרְתָה הַנֶּפֶשׁ› (“ferment and-cut the-living-being”)
# ‹הַהִוא מִיִּשְׂרָאֵל מִיּוֹם› (“that from-Israel from-day”)
# ‹הָרִאשֹׁן עַד־יוֹם הַשְּׁבִעִי› (“the-first until day the-seventh”)
# "[EN-AID] Seven days you shall eat unleavened bread; but on the first day
# you shall remove leaven from your houses — for whoever eats leavened
# bread, that soul shall be cut off from Israel, from the first day until
# the seventh day."
m.step("Exod.12.15")
# ‹שִׁבְעַת יָמִים מַצּוֹת› (“seven day sweetness”)
# ‹תֹּאכֵלוּ› (“eat”)
# — the-LORD speaks a demand — LET: seven-day-sweetness-eat
m.declare("YHWH", "LET",
          "shivat_yamim_matzot_tokhelu")
# witness-tier presupposed read: derivation_cluster on removal_deadline —
# read, not installed
m.witness_read("removal_deadline", "derivation_cluster",
                cites=["Pesachim 4b:9", "Pesachim 5a:5", "Pesachim 5a:6", "Pesachim 5a:16", "Pesachim 5a:19", "Pesachim 5b:1", "Pesachim 27b:9"])

# -------------------------- Exod.12.16 · HOLY_CONVOCATIONS -----------------
# ‹וּבַיּוֹם הָרִאשׁוֹן מִקְרָא־קֹדֶשׁ› (“and-in-day the-first something-
# called-out holiness”)
# ‹וּבַיּוֹם הַשְּׁבִיעִי מִקְרָא־קֹדֶשׁ› (“and-in-day the-seventh
# something-called-out holiness”)
# ‹יִהְיֶה לָכֶם כָּל־מְלָאכָה› (“be to-you/your(pl) all work”)
# ‹לֹא־יֵעָשֶׂה בָהֶם אַךְ› (“not make in-them/their indeed”)
# ‹אֲשֶׁר יֵאָכֵל לְכָל־נֶפֶשׁ› (“which eat to-all living-being”)
# ‹הוּא לְבַדּוֹ יֵעָשֶׂה› (“he/it to-separation-him/its make”)
# ‹לָכֶם› (“to-you/your(pl)”)
# "[EN-AID] And on the first day a holy convocation, and on the seventh day
# a holy convocation shall be for you; no work shall be done on them — only
# what is eaten by every soul, that alone may be done for you."
m.step("Exod.12.16")
# ‹וּבַיּוֹם הָרִאשׁוֹן מִקְרָא־קֹדֶשׁ› (“and-in-day the-first something-
# called-out holiness”)
# ‹וּבַיּוֹם הַשְּׁבִיעִי מִקְרָא־קֹדֶשׁ› (“and-in-day the-seventh
# something-called-out holiness”)
# ‹יִהְיֶה לָכֶם› (“be to-you/your(pl)”)
# — fact holds: something-called-out-holiness-first-and-seventh
m.fact("miqra_qodesh_rishon_u_shevii")
# witness-tier presupposed read:
# the_licenses_boundary_and_the_second_morning on food_exception — read, not
# installed
m.witness_read("food_exception", "the_licenses_boundary_and_the_second_morning",
                cites=["Pesachim 47a:5", "Pesachim 47a:6", "Pesachim 47a:7", "Shabbat 24b:6", "Shabbat 24b:7"])

# -------------------------- Exod.12.17 · GUARD_THE_MATZOT ------------------
# ‹וּשְׁמַרְתֶּם אֶת־הַמַּצּוֹת כִּי› (“and-keep/guard obj-marker the-
# sweetness that”)
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה› (“in-bone the-day the-this”)
# ‹הוֹצֵאתִי אֶת־צִבְאוֹתֵיכֶם מֵאֶרֶץ› (“bring-forth obj-marker host-
# you/your(pl) from-earth”)
# ‹מִצְרָיִם וּשְׁמַרְתֶּם אֶת־הַיּוֹם› (“Egypt and-keep/guard obj-marker
# the-day”)
# ‹הַזֶּה לְדֹרֹתֵיכֶם חֻקַּת› (“the-this to-generation-you/your(pl)
# statute”)
# ‹עוֹלָם› (“forever”)
# "[EN-AID] And you shall guard the unleavened bread, for on this very day I
# brought out your hosts from the land of Egypt; and you shall guard this
# day through your generations, an everlasting statute."
m.step("Exod.12.17")
# ‹וּשְׁמַרְתֶּם אֶת־הַמַּצּוֹת› (“and-keep/guard obj-marker the-sweetness”)
# — fact holds: and-keep/guard-obj-marker-the-sweetness
m.fact("u_shemartem_et_ha_matzot")

# -------------------------- Exod.12.18 · THE_FOUR_LEAN_MATZOT --------------
# ‹בָּרִאשֹׁן בְּאַרְבָּעָה עָשָׂר› (“in-first in-four -teen”)
# ‹יוֹם לַחֹדֶשׁ בָּעֶרֶב› (“day to-new-moon in-evening”)
# ‹תֹּאכְלוּ מַצֹּת עַד› (“eat sweetness until”)
# ‹יוֹם הָאֶחָד וְעֶשְׂרִים› (“day the-one and-twenty”)
# ‹לַחֹדֶשׁ בָּעָרֶב› (“to-new-moon in-evening”)
# "[EN-AID] In the first month, on the fourteenth day of the month in the
# evening, you shall eat unleavened bread, until the twenty-first day of the
# month in the evening."
m.step("Exod.12.18")
# ‹בָּרִאשֹׁן בְּאַרְבָּעָה עָשָׂר› (“in-first in-four -teen”)
# ‹יוֹם לַחֹדֶשׁ בָּעֶרֶב› (“day to-new-moon in-evening”)
# ‹תֹּאכְלוּ מַצֹּת› (“eat sweetness”)
# — fact holds: in-the-web-eat-sweetness
m.fact("ba_erev_tokhlu_matzot")
# witness-tier presupposed read: obligation_and_material on matza_statute —
# read, not installed
m.witness_read("matza_statute", "obligation_and_material",
                cites=["Pesachim 120a:6", "Pesachim 120a:7", "Pesachim 120a:11", "Pesachim 120a:12", "Pesachim 120a:13", "Pesachim 28b:10", "Pesachim 28b:11", "Pesachim 28b:12", "Kiddushin 37b:12", "Pesachim 38b:1", "Pesachim 38b:2", "Pesachim 40a:14", "Pesachim 40a:15", "Pesachim 36a:18", "Pesachim 36a:19", "Pesachim 39a:13", "Pesachim 39a:14", "Pesachim 120b:5", "Pesachim 109b:5", "Pesachim 108a:4", "Pesachim 42a:5"])

# -------------------------- Exod.12.19 · NO_LEAVEN_IN_YOUR_HOUSES ----------
# ‹שִׁבְעַת יָמִים שְׂאֹר› (“seven day barm”)
# ‹לֹא יִמָּצֵא בְּבָתֵּיכֶם› (“not find in-house-you/your(pl)”)
# ‹כִּי כָּל־אֹכֵל מַחְמֶצֶת› (“that all eat ferment”)
# ‹וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא› (“and-cut the-living-being that”)
# ‹מֵעֲדַת יִשְׂרָאֵל בַּגֵּר› (“from-congregation Israel in-sojourner”)
# ‹וּבְאֶזְרַח הָאָרֶץ› (“and-in-spontaneous-growth the-earth”)
# "[EN-AID] Seven days leaven shall not be found in your houses; for whoever
# eats what is leavened, that soul shall be cut off from the congregation of
# Israel — among the sojourner and among the native of the land."
m.step("Exod.12.19")
# ‹בַּגֵּר וּבְאֶזְרַח הָאָרֶץ› (“in-sojourner and-in-spontaneous-growth
# the-earth”)
# — fact holds: in-the-sojourner-and-and-spontaneous-growth-the-earth
m.fact("ba_ger_u_ve_ezrach_ha_aretz")
# witness-tier presupposed read: implementing_rows on leaven_ban — read, not
# installed
m.witness_read("leaven_ban", "implementing_rows",
                cites=["Mishnah Pesachim 1:1", "Mishnah Pesachim 2:2", "Mishnah Beitzah 1:1", "Mishnah Makkot 3:2", "Mishnah Pesachim 3:3", "Mishnah Pesachim 9:3"])
# witness-tier presupposed read: two_phrase_machine on seen_found_division —
# read, not installed
m.witness_read("seen_found_division", "two_phrase_machine",
                cites=["Pesachim 5b:2", "Pesachim 6a:6", "Pesachim 10b:15", "Pesachim 43a:18"])

# -------------------------- Exod.12.20 · IN_ALL_YOUR_DWELLINGS -------------
# ‹כָּל־מַחְמֶצֶת לֹא תֹאכֵלוּ› (“all ferment not eat”)
# ‹בְּכֹל מוֹשְׁבֹתֵיכֶם תֹּאכְלוּ› (“in-all seat-you/your(pl) eat”)
# ‹מַצּוֹת› (“sweetness”)
# "[EN-AID] You shall eat nothing leavened; in all your dwellings you shall
# eat unleavened bread."
m.step("Exod.12.20")
# ‹בְּכֹל מוֹשְׁבֹתֵיכֶם תֹּאכְלוּ› (“in-all seat-you/your(pl) eat”)
# ‹מַצּוֹת› (“sweetness”)
# — fact holds: in-all-moshvotekhem-sweetness
m.fact("be_khol_moshvotekhem_matzot")

# -------------------------- Exod.12.21 · DRAW_OUT_AND_TAKE -----------------
# ‹וַיִּקְרָא מֹשֶׁה לְכָל־זִקְנֵי› (“and-call Moses to-all old”)
# ‹יִשְׂרָאֵל וַיֹּאמֶר אֲלֵהֶם› (“Israel and-say to-them/their”)
# ‹מִשְׁכוּ וּקְחוּ לָכֶם› (“draw and-take to-you/your(pl)”)
# ‹צֹאן לְמִשְׁפְּחֹתֵיכֶם וְשַׁחֲטוּ› (“flock to-family-you/your(pl) and-
# slaughter”)
# ‹הַפָּסַח› (“the-pretermission”)
# "[EN-AID] And Moses called for all the elders of Israel, and said to them:
# Draw out and take for yourselves flocks according to your families, and
# slaughter the passover."
m.step("Exod.12.21")
# ‹מִשְׁכוּ וּקְחוּ לָכֶם› (“draw and-take to-you/your(pl)”)
# ‹צֹאן לְמִשְׁפְּחֹתֵיכֶם וְשַׁחֲטוּ› (“flock to-family-you/your(pl) and-
# slaughter”)
# ‹הַפָּסַח› (“the-pretermission”)
# — Moses speaks a demand — LET: draw-and-take-flock
m.declare("moshe", "LET",
          "mishkhu_u_qechu_tzon")

# -------------------------- Exod.12.22 · HYSSOP_AND_THRESHOLD --------------
# ‹וּלְקַחְתֶּם אֲגֻדַּת אֵזוֹב› (“and-take band hyssop”)
# ‹וּטְבַלְתֶּם בַּדָּם אֲשֶׁר־בַּסַּף› (“and-dip in-blood which in-
# vestibule”)
# ‹וְהִגַּעְתֶּם אֶל־הַמַּשְׁקוֹף וְאֶל־שְׁתֵּי› (“and-touch to the-lintel
# and-to two”)
# ‹הַמְּזוּזֹת מִן־הַדָּם אֲשֶׁר› (“the-door-post from the-blood which”)
# ‹בַּסָּף וְאַתֶּם לֹא› (“in-vestibule and-you not”)
# ‹תֵצְאוּ אִישׁ מִפֶּתַח־בֵּיתוֹ› (“bring-forth man from-opening house-
# him/its”)
# ‹עַד־בֹּקֶר› (“until morning”)
# "[EN-AID] And you shall take a bundle of hyssop, and dip it in the blood
# that is in the basin, and touch the lintel and the two doorposts with the
# blood that is in the basin; and you — none of you shall go out from the
# opening of his house until morning."
m.step("Exod.12.22")
# ‹וְאַתֶּם לֹא תֵצְאוּ› (“and-you not bring-forth”)
# ‹אִישׁ מִפֶּתַח־בֵּיתוֹ עַד־בֹּקֶר› (“man from-opening house-him/its until
# morning”)
# — fact holds: not-bring-forth-man-from-opening-beto
m.fact("lo_tetzu_ish_mi_petach_beto")

# -------------------------- Exod.12.23 · HE_WILL_NOT_LET_THE_DESTROYER -----
# ‹וְעָבַר יְהוָה לִנְגֹּף› (“and-pass-over YHWH to-push”)
# ‹אֶת־מִצְרַיִם וְרָאָה אֶת־הַדָּם› (“obj-marker Egypt and-see obj-marker
# the-blood”)
# ‹עַל־הַמַּשְׁקוֹף וְעַל שְׁתֵּי› (“over the-lintel and-over two”)
# ‹הַמְּזוּזֹת וּפָסַח יְהוָה› (“the-door-post and-hop YHWH”)
# ‹עַל־הַפֶּתַח וְלֹא יִתֵּן› (“over the-opening and-not set”)
# ‹הַמַּשְׁחִית לָבֹא אֶל־בָּתֵּיכֶם› (“the-decay to-come/bring to house-
# you/your(pl)”)
# ‹לִנְגֹּף› (“to-push”)
# "[EN-AID] And the LORD will pass through to strike Egypt, and He will see
# the blood on the lintel and on the two doorposts; and the LORD will pass
# over the opening, and will not let the destroyer come into your houses to
# strike."
m.step("Exod.12.23")
# ‹וּפָסַח יְהוָה עַל־הַפֶּתַח› (“and-hop YHWH over the-opening”)
# — fact holds: and-hop-the-LORD-over-the-opening
m.fact("u_fasach_YHWH_al_ha_petach")

# -------------------------- Exod.12.24 · A_STATUTE_FOREVER -----------------
# ‹וּשְׁמַרְתֶּם אֶת־הַדָּבָר הַזֶּה› (“and-keep/guard obj-marker the-
# word/thing the-this”)
# ‹לְחָק־לְךָ וּלְבָנֶיךָ עַד־עוֹלָם› (“to-enactment to-you/your and-to-son-
# you/your until forever”)
# "[EN-AID] And you shall guard this thing as a statute for you and for your
# sons, forever."
m.step("Exod.12.24")
# ‹לְחָק־לְךָ וּלְבָנֶיךָ עַד־עוֹלָם› (“to-enactment to-you/your and-to-son-
# you/your until forever”)
# — fact holds: to-enactment-to-you-and-to-your-sons
m.fact("le_chaq_lekha_u_le_vanekha")

# -------------------------- Exod.12.25 · WHEN_YOU_COME_TO_THE_LAND ---------
# ‹וְהָיָה כִּי־תָבֹאוּ אֶל־הָאָרֶץ› (“and-be that come/bring to the-earth”)
# ‹אֲשֶׁר יִתֵּן יְהוָה› (“which set YHWH”)
# ‹לָכֶם כַּאֲשֶׁר דִּבֵּר› (“to-you/your(pl) like-as/which speak”)
# ‹וּשְׁמַרְתֶּם אֶת־הָעֲבֹדָה הַזֹּאת› (“and-keep/guard obj-marker the-
# service/work the-this”)
# "[EN-AID] And it shall be, when you come to the land which the LORD will
# give you, as He has spoken, that you shall guard this service."
m.step("Exod.12.25")
# ‹וְהָיָה כִּי־תָבֹאוּ אֶל־הָאָרֶץ› (“and-be that come/bring to the-earth”)
# — fact holds: very-widely-used-as-a-relati-come/bring-to-the-earth
m.fact("ki_tavou_el_ha_aretz")

# -------------------------- Exod.12.26 · WHEN_YOUR_SONS_ASK ----------------
# ‹וְהָיָה כִּי־יֹאמְרוּ אֲלֵיכֶם› (“and-be that say to-you/your(pl)”)
# ‹בְּנֵיכֶם מָה הָעֲבֹדָה› (“son-you/your(pl) what the-service/work”)
# ‹הַזֹּאת לָכֶם› (“the-this to-you/your(pl)”)
# "[EN-AID] And it shall be, when your sons say to you: What is this service
# to you?"
m.step("Exod.12.26")
# ‹וְהָיָה כִּי־יֹאמְרוּ אֲלֵיכֶם› (“and-be that say to-you/your(pl)”)
# ‹בְּנֵיכֶם› (“son-you/your(pl)”)
# — the-LORD speaks a demand — LET: and-say-sacrifice-pretermission
m.declare("YHWH", "LET",
          "va_amartem_zevach_pesach")

# -------------------------- Exod.12.27 · THE_ANSWER_AND_THE_BOW ------------
# ‹וַאֲמַרְתֶּם זֶבַח־פֶּסַח הוּא› (“and-say sacrifice pretermission he/it”)
# ‹לַיהוָה אֲשֶׁר פָּסַח› (“to-YHWH which hop”)
# ‹עַל־בָּתֵּי בְנֵי־יִשְׂרָאֵל בְּמִצְרַיִם› (“over house son Israel in-
# Egypt”)
# ‹בְּנָגְפּוֹ אֶת־מִצְרַיִם וְאֶת־בָּתֵּינוּ› (“in-push-him/its obj-marker
# Egypt and-obj-marker house-us/our”)
# ‹הִצִּיל וַיִּקֹּד הָעָם› (“snatch-away and-shrivel-up the-people”)
# ‹וַיִּשְׁתַּחֲוּוּ› (“and-afflict”)
# "[EN-AID] Then you shall say: It is a passover-sacrifice to the LORD, who
# passed over the houses of the sons of Israel in Egypt when He struck
# Egypt, and our houses He rescued. And the people bowed and prostrated
# themselves."
m.step("Exod.12.27")
# ‹וַיִּקֹּד הָעָם וַיִּשְׁתַּחֲוּוּ› (“and-shrivel-up the-people and-
# afflict”)
# — fact holds: and-shrivel-up-the-people-and-yishtachavu
m.fact("va_yiqod_ha_am_va_yishtachavu")
# witness-tier presupposed read: seder_trio on pesach_answer — read, not
# installed
m.witness_read("pesach_answer", "seder_trio",
                cites=["Mishnah Pesachim 10:5", "Mishnah Pesachim 2:5"])

# -------------------------- Exod.12.28 · AND_THEY_DID_SO -------------------
# ‹וַיֵּלְכוּ וַיַּעֲשׂוּ בְּנֵי› (“and-go and-make son”)
# ‹יִשְׂרָאֵל כַּאֲשֶׁר צִוָּה› (“Israel like-as/which command”)
# ‹יְהוָה אֶת־מֹשֶׁה וְאַהֲרֹן› (“YHWH obj-marker Moses and-Aaron”)
# ‹כֵּן עָשׂוּ› (“so make”)
# "[EN-AID] And the sons of Israel went and did as the LORD had commanded
# Moses and Aaron — so they did."
m.step("Exod.12.28")
# ‹וַיֵּלְכוּ וַיַּעֲשׂוּ בְּנֵי› (“and-go and-make son”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — demand settled (popped from the queue): and-take-man-member-of-a-flock-
# to-house
m.result("ve_yiqchu_ish_se_la_bayit", tmark="t1")
# ‹כֵּן עָשׂוּ› (“so make”)
# — demand settled (popped from the queue): draw-and-take-flock
m.result("mishkhu_u_qechu_tzon", tmark="t1")

# -------------------------- Exod.12.29 · MIDNIGHT --------------------------
# ‹וַיְהִי בַּחֲצִי הַלַּיְלָה› (“and-be in-half the-night”)
# ‹וַיהוָה הִכָּה כָל־בְּכוֹר› (“and-YHWH strike all firstborn”)
# ‹בְּאֶרֶץ מִצְרַיִם מִבְּכֹר› (“in-earth Egypt from-firstborn”)
# ‹פַּרְעֹה הַיֹּשֵׁב עַל־כִּסְאוֹ› (“Pharaoh the-dwell/sit over covered-
# him/its”)
# ‹עַד בְּכוֹר הַשְּׁבִי› (“until firstborn the-exiled”)
# ‹אֲשֶׁר בְּבֵית הַבּוֹר› (“which in-house the-pit”)
# ‹וְכֹל בְּכוֹר בְּהֵמָה› (“and-all firstborn livestock”)
# "[EN-AID] And it was at half of the night: the LORD struck every firstborn
# in the land of Egypt, from the firstborn of Pharaoh sitting on his throne
# to the firstborn of the captive in the dungeon-house, and every firstborn
# of beast."
m.step("Exod.12.29")
# ‹וַיְהִי בַּחֲצִי הַלַּיְלָה› (“and-be in-half the-night”)
# ‹וַיהוָה הִכָּה כָל־בְּכוֹר› (“and-YHWH strike all firstborn”)
# ‹בְּאֶרֶץ מִצְרַיִם› (“in-earth Egypt”)
# — event: makat-bekhorot — agent the-LORD
m.event("makat_bekhorot", agent="YHWH")

# -------------------------- Exod.12.30 · NO_HOUSE_WITHOUT_A_DEAD -----------
# ‹וַיָּקָם פַּרְעֹה לַיְלָה› (“and-arise Pharaoh night”)
# ‹הוּא וְכָל־עֲבָדָיו וְכָל־מִצְרַיִם› (“he/it and-all servant-him/its and-
# all Egypt”)
# ‹וַתְּהִי צְעָקָה גְדֹלָה› (“and-be shriek great”)
# ‹בְּמִצְרָיִם כִּי־אֵין בַּיִת› (“in-Egypt that there-is-not house”)
# ‹אֲשֶׁר אֵין־שָׁם מֵת› (“which there-is-not there die”)
# "[EN-AID] And Pharaoh rose at night, he and all his servants and all
# Egypt, and there was a great cry in Egypt — for there was no house where
# there was not a dead one."
m.step("Exod.12.30")
# ‹וַתְּהִי צְעָקָה גְדֹלָה› (“and-be shriek great”)
# ‹בְּמִצְרָיִם› (“in-Egypt”)
# — fact holds: shriek-great-in-Egypt
m.fact("tzeaqa_gedola_be_mitzrayim")

# -------------------------- Exod.12.31 · RISE_GO_OUT -----------------------
# ‹וַיִּקְרָא לְמֹשֶׁה וּלְאַהֲרֹן› (“and-call to-Moses and-to-Aaron”)
# ‹לַיְלָה וַיֹּאמֶר קוּמוּ› (“night and-say arise”)
# ‹צְּאוּ מִתּוֹךְ עַמִּי› (“bring-forth from-midst people-me/my”)
# ‹גַּם־אַתֶּם גַּם־בְּנֵי יִשְׂרָאֵל› (“also you also son Israel”)
# ‹וּלְכוּ עִבְדוּ אֶת־יְהוָה› (“and-go work/serve obj-marker YHWH”)
# ‹כְּדַבֶּרְכֶם› (“like-speak-you/your(pl)”)
# "[EN-AID] And he called for Moses and for Aaron by night, and said: Rise,
# go out from among my people, both you and the sons of Israel — and go,
# serve the LORD as you have spoken."
m.step("Exod.12.31")
# ‹וַיֹּאמֶר קוּמוּ צְּאוּ› (“and-say arise bring-forth”)
# ‹מִתּוֹךְ עַמִּי› (“from-midst people-me/my”)
# — fact holds: arise-bring-forth-work/serve-khedaberkhem
m.fact("qumu_tzeu_ivdu_khedaberkhem")

# -------------------------- Exod.12.32 · BLESS_ME_ALSO ---------------------
# ‹גַּם־צֹאנְכֶם גַּם־בְּקַרְכֶם קְחוּ› (“also flock-you/your(pl) also herd-
# you/your(pl) take”)
# ‹כַּאֲשֶׁר דִּבַּרְתֶּם וָלֵכוּ› (“like-as/which speak and-go”)
# ‹וּבֵרַכְתֶּם גַּם־אֹתִי› (“and-bless also obj-marker-me/my”)
# "[EN-AID] Both your flocks and your herds take, as you have spoken, and go
# — and bless me also."
m.step("Exod.12.32")
# ‹וּבֵרַכְתֶּם גַּם־אֹתִי› (“and-bless also obj-marker-me/my”)
# — fact holds: and-bless-also-me
m.fact("u_verakhtem_gam_oti")

# -------------------------- Exod.12.33 · EGYPT_PRESSES ---------------------
# ‹וַתֶּחֱזַק מִצְרַיִם עַל־הָעָם› (“and-fasten-upon Egyptian over the-
# people”)
# ‹לְמַהֵר לְשַׁלְּחָם מִן־הָאָרֶץ› (“to-hasten to-send-them/their from the-
# earth”)
# ‹כִּי אָמְרוּ כֻּלָּנוּ› (“that say all-us/our”)
# ‹מֵתִים› (“die”)
# "[EN-AID] And Egypt pressed hard upon the people, to hasten to send them
# out of the land — for they said: We are all dead men."
m.step("Exod.12.33")
# ‹כִּי אָמְרוּ כֻּלָּנוּ› (“that say all-us/our”)
# ‹מֵתִים› (“die”)
# — fact holds: kulanu-die
m.fact("kulanu_metim")

# -------------------------- Exod.12.34 · DOUGH_BEFORE_LEAVENING ------------
# ‹וַיִּשָּׂא הָעָם אֶת־בְּצֵקוֹ› (“and-lift/carry the-people obj-marker
# dough-him/its”)
# ‹טֶרֶם יֶחְמָץ מִשְׁאֲרֹתָם› (“non-occurrence be-pungent kneading-trough-
# them/their”)
# ‹צְרֻרֹת בְּשִׂמְלֹתָם עַל־שִׁכְמָם› (“cramp in-dress-them/their over
# neck-as-the-place-of-burden-them/their”)
# "[EN-AID] And the people carried their dough before it could leaven, their
# kneading-troughs bound in their garments on their shoulders."
m.step("Exod.12.34")
# ‹וַיִּשָּׂא הָעָם אֶת־בְּצֵקוֹ› (“and-lift/carry the-people obj-marker
# dough-him/its”)
# ‹טֶרֶם יֶחְמָץ› (“non-occurrence be-pungent”)
# — fact holds: non-occurrence-be-pungent
m.fact("terem_yechmatz")

# -------------------------- Exod.12.35 · THEY_ASKED_AS_MOSES_SAID ----------
# ‹וּבְנֵי־יִשְׂרָאֵל עָשׂוּ כִּדְבַר› (“and-son Israel make like-
# word/thing”)
# ‹מֹשֶׁה וַיִּשְׁאֲלוּ מִמִּצְרַיִם› (“Moses and-inquire from-Egypt”)
# ‹כְּלֵי־כֶסֶף וּכְלֵי זָהָב› (“vessel silver and-vessel gold”)
# ‹וּשְׂמָלֹת› (“and-dress”)
# "[EN-AID] And the sons of Israel did according to the word of Moses: they
# asked of Egypt vessels of silver and vessels of gold, and garments."
m.step("Exod.12.35")
# ‹וַיִּשְׁאֲלוּ מִמִּצְרַיִם כְּלֵי־כֶסֶף› (“and-inquire from-Egypt vessel
# silver”)
# ‹וּכְלֵי זָהָב וּשְׂמָלֹת› (“and-vessel gold and-dress”)
# — fact holds: and-inquire-vessel-silver-and-gold
m.fact("va_yishalu_kele_khesef_u_zahav")

# -------------------------- Exod.12.36 · THEY_STRIPPED_EGYPT ---------------
# ‹וַיהוָה נָתַן אֶת־חֵן› (“and-YHWH set obj-marker graciousness”)
# ‹הָעָם בְּעֵינֵי מִצְרַיִם› (“the-people in-eye Egypt”)
# ‹וַיַּשְׁאִלוּם וַיְנַצְּלוּ אֶת־מִצְרָיִם› (“and-inquire-them/their and-
# snatch-away obj-marker Egypt”)
# "[EN-AID] And the LORD gave the people favor in the eyes of Egypt, and
# they granted their request — and they stripped Egypt."
m.step("Exod.12.36")
# ‹וַיְנַצְּלוּ אֶת־מִצְרָיִם› (“and-snatch-away obj-marker Egypt”)
# — fact holds: and-snatch-away-obj-marker-Egypt
m.fact("va_yenatzlu_et_mitzrayim")

# -------------------------- Exod.12.37 · RAMESES_TO_SUCCOTH ----------------
# ‹וַיִּסְעוּ בְנֵי־יִשְׂרָאֵל מֵרַעְמְסֵס› (“and-journey son Israel from-
# Raamses”)
# ‹סֻכֹּתָה כְּשֵׁשׁ־מֵאוֹת אֶלֶף› (“Succoth-ward like-six hundred
# thousand”)
# ‹רַגְלִי הַגְּבָרִים לְבַד› (“footman the-valiant-man to-separation”)
# ‹מִטָּף› (“from-family”)
# "[EN-AID] And the sons of Israel journeyed from Rameses toward Succoth,
# about six hundred thousand on foot, the men, besides children."
m.step("Exod.12.37")
# ‹וַיִּסְעוּ בְנֵי־יִשְׂרָאֵל מֵרַעְמְסֵס› (“and-journey son Israel from-
# Raamses”)
# ‹סֻכֹּתָה› (“Succoth-ward”)
# — fact holds: and-journey-from-Raamses-sukota
m.fact("va_yisu_me_ramses_sukota")

# -------------------------- Exod.12.38 · THE_MIXED_MULTITUDE ---------------
# ‹וְגַם־עֵרֶב רַב עָלָה› (“and-also web many/great go-up”)
# ‹אִתָּם וְצֹאן וּבָקָר› (“with-them/their and-flock and-herd”)
# ‹מִקְנֶה כָּבֵד מְאֹד› (“something-bought heavy very”)
# "[EN-AID] And also a mixed multitude went up with them, and flocks and
# herds — very heavy livestock."
m.step("Exod.12.38")
# ‹וְגַם־עֵרֶב רַב עָלָה› (“and-also web many/great go-up”)
# ‹אִתָּם› (“with-them/their”)
# — fact holds: web-many/great-go-up-itam
m.fact("erev_rav_ala_itam")

# -------------------------- Exod.12.39 · CAKES_OF_MATZA --------------------
# ‹וַיֹּאפוּ אֶת־הַבָּצֵק אֲשֶׁר› (“and-cook obj-marker the-dough which”)
# ‹הוֹצִיאוּ מִמִּצְרַיִם עֻגֹת› (“bring-forth from-Egypt ash-cake”)
# ‹מַצּוֹת כִּי לֹא› (“sweetness that not”)
# ‹חָמֵץ כִּי־גֹרְשׁוּ מִמִּצְרַיִם› (“be-pungent that drive-out-from-a-
# possession from-Egypt”)
# ‹וְלֹא יָכְלוּ לְהִתְמַהְמֵהַּ› (“and-not be-able to-question”)
# ‹וְגַם־צֵדָה לֹא־עָשׂוּ לָהֶם› (“and-also food not make to-them/their”)
# "[EN-AID] And they baked the dough which they brought out of Egypt into
# cakes of unleavened bread, for it had not leavened — for they were driven
# out of Egypt and could not delay, and also provisions they had not made
# for themselves."
m.step("Exod.12.39")
# ‹כִּי־גֹרְשׁוּ מִמִּצְרַיִם› (“that drive-out-from-a-possession from-
# Egypt”)
# — fact holds: very-widely-used-as-a-relati-drive-out-from-a-possession-
# from-Egypt
m.fact("ki_gorshu_mi_mitzrayim")

# -------------------------- Exod.12.40 · FOUR_HUNDRED_THIRTY_YEARS ---------
# ‹וּמוֹשַׁב בְּנֵי יִשְׂרָאֵל› (“and-seat son Israel”)
# ‹אֲשֶׁר יָשְׁבוּ בְּמִצְרָיִם› (“which dwell/sit in-Egypt”)
# ‹שְׁלֹשִׁים שָׁנָה וְאַרְבַּע› (“thirty years and-four”)
# ‹מֵאוֹת שָׁנָה› (“hundred years”)
# "[EN-AID] And the dwelling of the sons of Israel, which they dwelt in
# Egypt, was thirty years and four hundred years."
m.step("Exod.12.40")
# ‹שְׁלֹשִׁים שָׁנָה וְאַרְבַּע› (“thirty years and-four”)
# ‹מֵאוֹת שָׁנָה› (“hundred years”)
# — fact holds: seat-430-years
m.fact("moshav_430_shana")

# -------------------------- Exod.12.41 · THE_VERY_DAY_THE_HOSTS_WENT_OUT ---
# ‹וַיְהִי מִקֵּץ שְׁלֹשִׁים› (“and-be from-end thirty”)
# ‹שָׁנָה וְאַרְבַּע מֵאוֹת› (“years and-four hundred”)
# ‹שָׁנָה וַיְהִי בְּעֶצֶם› (“years and-be in-bone”)
# ‹הַיּוֹם הַזֶּה יָצְאוּ› (“the-day the-this bring-forth”)
# ‹כָּל־צִבְאוֹת יְהוָה מֵאֶרֶץ› (“all host YHWH from-earth”)
# ‹מִצְרָיִם› (“Egypt”)
# "[EN-AID] And it was at the end of thirty years and four hundred years —
# and it was on this very day: all the hosts of the LORD went out from the
# land of Egypt."
m.step("Exod.12.41")
# ‹וַיְהִי בְּעֶצֶם הַיּוֹם› (“and-be in-bone the-day”)
# ‹הַזֶּה יָצְאוּ כָּל־צִבְאוֹת› (“the-this bring-forth all host”)
# ‹יְהוָה› (“YHWH”)
# — fact holds: bring-forth-all-host-the-LORD
m.fact("yatzu_kol_tzivot_YHWH")

# -------------------------- Exod.12.42 · NIGHT_OF_WATCHINGS ----------------
# ‹לֵיל שִׁמֻּרִים הוּא› (“night observance he/it”)
# ‹לַיהוָה לְהוֹצִיאָם מֵאֶרֶץ› (“to-YHWH to-bring-forth-them/their from-
# earth”)
# ‹מִצְרָיִם הוּא־הַלַּיְלָה הַזֶּה› (“Egypt he/it the-night the-this”)
# ‹לַיהוָה שִׁמֻּרִים לְכָל־בְּנֵי› (“to-YHWH observance to-all son”)
# ‹יִשְׂרָאֵל לְדֹרֹתָם› (“Israel to-generation-them/their”)
# "[EN-AID] A night of watchings is it to the LORD, to bring them out from
# the land of Egypt; it is this night to the LORD — watchings for all the
# sons of Israel through their generations."
m.step("Exod.12.42")
# ‹לֵיל שִׁמֻּרִים הוּא› (“night observance he/it”)
# ‹לַיהוָה› (“to-YHWH”)
# — fact holds: night-observance-to-dorotam
m.fact("lel_shimurim_le_dorotam")

# -------------------------- Exod.12.43 · THE_ORDINANCE_OF_THE_PASSOVER -----
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹וְאַהֲרֹן זֹאת חֻקַּת› (“and-Aaron this statute”)
# ‹הַפָּסַח כָּל־בֶּן־נֵכָר לֹא־יֹאכַל› (“the-pretermission all son foreign
# not eat”)
# ‹בּוֹ› (“in-him/its”)
# "[EN-AID] And the LORD said to Moses and Aaron: This is the ordinance of
# the passover: no foreigner shall eat of it."
m.step("Exod.12.43")
# ‹זֹאת חֻקַּת הַפָּסַח› (“this statute the-pretermission”)
# — the-LORD speaks a demand — LET: this-statute-the-pretermission
m.declare("YHWH", "LET",
          "zot_chuqat_ha_pasach")

# -------------------------- Exod.12.44 · BOUGHT_AND_CIRCUMCISED ------------
# ‹וְכָל־עֶבֶד אִישׁ מִקְנַת־כָּסֶף› (“and-all servant man buying silver”)
# ‹וּמַלְתָּה אֹתוֹ אָז› (“and-circumcise obj-marker-him/its at-that-time”)
# ‹יֹאכַל בּוֹ› (“eat in-him/its”)
# "[EN-AID] And every man's servant, bought with silver — you shall
# circumcise him; then he may eat of it."
m.step("Exod.12.44")
# ‹וּמַלְתָּה אֹתוֹ אָז› (“and-circumcise obj-marker-him/its at-that-time”)
# ‹יֹאכַל בּוֹ› (“eat in-him/its”)
# — fact holds: and-circumcise-it-at-that-time-eat
m.fact("u_malta_oto_az_yokhal")

# -------------------------- Exod.12.45 · SOJOURNER_AND_HIRELING ------------
# ‹תּוֹשָׁב וְשָׂכִיר לֹא־יֹאכַל־בּוֹ› (“resident-alien and-man-at-wages-by-
# the-day not eat in-him/its”)
# "[EN-AID] A settler and a hireling shall not eat of it."
m.step("Exod.12.45")
# ‹תּוֹשָׁב וְשָׂכִיר לֹא־יֹאכַל־בּוֹ› (“resident-alien and-man-at-wages-by-
# the-day not eat in-him/its”)
# — fact holds: resident-alien-and-man-at-wages-by-the-day-not-eat
m.fact("toshav_ve_sakhir_lo_yokhal")

# -------------------------- Exod.12.46 · NO_BONE_BROKEN --------------------
# ‹בְּבַיִת אֶחָד יֵאָכֵל› (“in-house one eat”)
# ‹לֹא־תוֹצִיא מִן־הַבַּיִת מִן־הַבָּשָׂר› (“not bring-forth from the-house
# from the-flesh”)
# ‹חוּצָה וְעֶצֶם לֹא› (“outside-ward and-bone not”)
# ‹תִשְׁבְּרוּ־בוֹ› (“burst in-him/its”)
# "[EN-AID] In one house shall it be eaten; you shall not take any of the
# flesh outside from the house; and a bone you shall not break in it."
m.step("Exod.12.46")
# ‹וְעֶצֶם לֹא תִשְׁבְּרוּ־בוֹ› (“and-bone not burst in-him/its”)
# — fact holds: and-bone-not-tishberu-come/bring
m.fact("ve_etzem_lo_tishberu_vo")
# witness-tier presupposed read: scope_carry_and_burn on bone_clause — read,
# not installed
m.witness_read("bone_clause", "scope_carry_and_burn",
                cites=["Pesachim 85a:2", "Pesachim 84a:14", "Pesachim 84a:15", "Pesachim 84a:13", "Pesachim 85b:2", "Pesachim 86a:15", "Pesachim 83b:12", "Pesachim 83b:14", "Zevachim 36a:3"])

# -------------------------- Exod.12.47 · ALL_THE_CONGREGATION --------------
# ‹כָּל־עֲדַת יִשְׂרָאֵל יַעֲשׂוּ› (“all congregation Israel make”)
# ‹אֹתוֹ› (“obj-marker-him/its”)
# "[EN-AID] All the congregation of Israel shall do it."
m.step("Exod.12.47")
# ‹כָּל־עֲדַת יִשְׂרָאֵל יַעֲשׂוּ› (“all congregation Israel make”)
# ‹אֹתוֹ› (“obj-marker-him/its”)
# — fact holds: all-congregation-Israel-make
m.fact("kol_adat_yisrael_yaasu")

# -------------------------- Exod.12.48 · THE_GER_WHO_DRAWS_NEAR ------------
# ‹וְכִי־יָגוּר אִתְּךָ גֵּר› (“and-that turn-aside-from-the-road with-
# you/your sojourner”)
# ‹וְעָשָׂה פֶסַח לַיהוָה› (“and-make pretermission to-YHWH”)
# ‹הִמּוֹל לוֹ כָל־זָכָר› (“circumcise to-him/its all male”)
# ‹וְאָז יִקְרַב לַעֲשֹׂתוֹ› (“and-at-that-time bring-near to-make-him/its”)
# ‹וְהָיָה כְּאֶזְרַח הָאָרֶץ› (“and-be like-spontaneous-growth the-earth”)
# ‹וְכָל־עָרֵל לֹא־יֹאכַל בּוֹ› (“and-all uncircumcised not eat in-him/its”)
# "[EN-AID] And when a sojourner sojourns with you and would do a passover
# to the LORD, every male of his shall be circumcised, and then he may draw
# near to do it, and he shall be as a native of the land; and no
# uncircumcised one shall eat of it."
m.step("Exod.12.48")
# ‹וְהָיָה כְּאֶזְרַח הָאָרֶץ› (“and-be like-spontaneous-growth the-earth”)
# — fact holds: and-be-like-spontaneous-growth-the-earth
m.fact("ve_haya_ke_ezrach_ha_aretz")

# -------------------------- Exod.12.49 · ONE_TORAH -------------------------
# ‹תּוֹרָה אַחַת יִהְיֶה› (“precept one be”)
# ‹לָאֶזְרָח וְלַגֵּר הַגָּר› (“to-spontaneous-growth and-to-sojourner the-
# turn-aside-from-the-road”)
# ‹בְּתוֹכְכֶם› (“in-midst-you/your(pl)”)
# "[EN-AID] One law shall there be for the native and for the sojourner who
# sojourns in your midst."
m.step("Exod.12.49")
# ‹תּוֹרָה אַחַת יִהְיֶה› (“precept one be”)
# ‹לָאֶזְרָח› (“to-spontaneous-growth”)
# — fact holds: precept-one-to-spontaneous-growth-and-to-sojourner
m.fact("tora_achat_la_ezrach_ve_la_ger")

# -------------------------- Exod.12.50 · AS_COMMANDED_SO_THEY_DID ----------
# ‹וַיַּעֲשׂוּ כָּל־בְּנֵי יִשְׂרָאֵל› (“and-make all son Israel”)
# ‹כַּאֲשֶׁר צִוָּה יְהוָה› (“like-as/which command YHWH”)
# ‹אֶת־מֹשֶׁה וְאֶת־אַהֲרֹן כֵּן› (“obj-marker Moses and-obj-marker Aaron
# so”)
# ‹עָשׂוּ› (“make”)
# "[EN-AID] And all the sons of Israel did as the LORD had commanded Moses
# and Aaron — so they did."
m.step("Exod.12.50")
# ‹וַיַּעֲשׂוּ כָּל־בְּנֵי יִשְׂרָאֵל› (“and-make all son Israel”)
# — demand settled (popped from the queue): this-statute-the-pretermission
m.result("zot_chuqat_ha_pasach", tmark="t1")

# -------------------------- Exod.12.51 · ON_THIS_VERY_DAY_HE_BROUGHT_THEM_OUT -
# ‹וַיְהִי בְּעֶצֶם הַיּוֹם› (“and-be in-bone the-day”)
# ‹הַזֶּה הוֹצִיא יְהוָה› (“the-this bring-forth YHWH”)
# ‹אֶת־בְּנֵי יִשְׂרָאֵל מֵאֶרֶץ› (“obj-marker son Israel from-earth”)
# ‹מִצְרַיִם עַל־צִבְאֹתָם› (“Egypt over host-them/their”)
# "[EN-AID] And it was on this very day: the LORD brought out the sons of
# Israel from the land of Egypt, by their hosts."
m.step("Exod.12.51")
# ‹הוֹצִיא יְהוָה אֶת־בְּנֵי› (“bring-forth YHWH obj-marker son”)
# ‹יִשְׂרָאֵל מֵאֶרֶץ מִצְרַיִם› (“Israel from-earth Egypt”)
# ‹עַל־צִבְאֹתָם› (“over host-them/their”)
# — event: yetziat-Egypt — agent the-LORD
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('calendar_commission', 'court_procedure'), ('calendar_commission', 'calendar_machine_derivations'), ('count_clause', 'registration_derivations'), ('lamb_spec', 'validity_eras_and_the_rider'), ('slaughter_clause', 'service_laws'), ('egypt_rite_file', 'doorway_altars'), ('roast_clause', 'eating_regime'), ('roast_clause', 'derivation_layer'), ('second_passover_statute_engine', 'includes_and_overrides'), ('haste_clause', 'two_era_table'), ('removal_deadline', 'derivation_cluster'), ('food_exception', 'the_licenses_boundary_and_the_second_morning'), ('matza_statute', 'obligation_and_material'), ('leaven_ban', 'implementing_rows'), ('seen_found_division', 'two_phrase_machine'), ('pesach_answer', 'seder_trio'), ('bone_clause', 'scope_carry_and_burn')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Rosh Hashanah 3:1', 'Mishnah Rosh Hashanah 1:7', 'Mishnah Pesachim 4:9', 'Mishnah Yevamot 8:1']
    assert all('court_procedure' not in f for f in m.WORLD["facts"])
    assert 'calendar_commission' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Rosh Hashanah 20a:14', 'Rosh Hashanah 20a:15', 'Rosh Hashanah 20a:16', 'Rosh Hashanah 20b:9', 'Rosh Hashanah 20b:10', 'Rosh Hashanah 20b:11', 'Rosh Hashanah 20b:12', 'Sanhedrin 12b:8', 'Sanhedrin 12b:9', 'Sanhedrin 12b:10', 'Rosh Hashanah 7a:17', 'Rosh Hashanah 7a:18']
    assert all('calendar_machine_derivations' not in f for f in m.WORLD["facts"])
    assert 'calendar_commission' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Pesachim 61a:9', 'Pesachim 61a:10', 'Pesachim 89a:22', 'Pesachim 90a:12', 'Pesachim 88a:6', 'Pesachim 91b:3', 'Pesachim 99a:2', 'Pesachim 59a:1', 'Pesachim 61b:6', 'Pesachim 78b:10']
    assert all('registration_derivations' not in f for f in m.WORLD["facts"])
    assert 'count_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Zevachim 25b:15', 'Pesachim 96a:8', 'Arakhin 13b:2', 'Pesachim 96a:7', 'Pesachim 95b:1', 'Pesachim 95b:2', 'Pesachim 70a:5', 'Pesachim 70b:6', 'Zevachim 7b:17']
    assert all('validity_eras_and_the_rider' not in f for f in m.WORLD["facts"])
    assert 'lamb_spec' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mishnah Pesachim 5:5', 'Mishnah Pesachim 5:3', 'Mishnah Pesachim 5:2', 'Mishnah Pesachim 7:4', 'Mishnah Kiddushin 2:1']
    assert all('service_laws' not in f for f in m.WORLD["facts"])
    assert 'slaughter_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Pesachim 96a:4', 'Pesachim 96a:5', 'Pesachim 96a:6']
    assert all('doorway_altars' not in f for f in m.WORLD["facts"])
    assert 'egypt_rite_file' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Mishnah Pesachim 2:8', 'Mishnah Pesachim 7:1', 'Mishnah Beitzah 2:7', 'Mishnah Pesachim 10:9', 'Mishnah Makkot 3:3']
    assert all('eating_regime' not in f for f in m.WORLD["facts"])
    assert 'roast_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Pesachim 41a:8', 'Pesachim 41b:1', 'Pesachim 41b:11', 'Pesachim 74a:2', 'Pesachim 75a:4', 'Pesachim 76a:2']
    assert all('derivation_layer' not in f for f in m.WORLD["facts"])
    assert 'roast_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Pesachim 95a:1', 'Pesachim 95a:2', 'Pesachim 95a:3', 'Pesachim 95a:4', 'Pesachim 95a:7', 'Pesachim 95a:8', 'Pesachim 95a:11', 'Pesachim 95a:12', 'Pesachim 95a:13', 'Pesachim 95a:14', 'Pesachim 95b:1', 'Pesachim 95b:3', 'Pesachim 95b:5', 'Pesachim 95b:6', 'Pesachim 95b:8', 'Pesachim 95b:9', 'Pesachim 95b:10', 'Pesachim 95b:11', 'Pesachim 95b:12', 'Pesachim 95b:13', 'Pesachim 95b:14', 'Pesachim 95b:15', 'Pesachim 95b:16', 'Pesachim 96a:2', 'Pesachim 96a:3']
    assert all('includes_and_overrides' not in f for f in m.WORLD["facts"])
    assert 'second_passover_statute_engine' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Mishnah Pesachim 9:5']
    assert all('two_era_table' not in f for f in m.WORLD["facts"])
    assert 'haste_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Pesachim 4b:9', 'Pesachim 5a:5', 'Pesachim 5a:6', 'Pesachim 5a:16', 'Pesachim 5a:19', 'Pesachim 5b:1', 'Pesachim 27b:9']
    assert all('derivation_cluster' not in f for f in m.WORLD["facts"])
    assert 'removal_deadline' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Pesachim 47a:5', 'Pesachim 47a:6', 'Pesachim 47a:7', 'Shabbat 24b:6', 'Shabbat 24b:7']
    assert all('the_licenses_boundary_and_the_second_morning' not in f for f in m.WORLD["facts"])
    assert 'food_exception' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Pesachim 120a:6', 'Pesachim 120a:7', 'Pesachim 120a:11', 'Pesachim 120a:12', 'Pesachim 120a:13', 'Pesachim 28b:10', 'Pesachim 28b:11', 'Pesachim 28b:12', 'Kiddushin 37b:12', 'Pesachim 38b:1', 'Pesachim 38b:2', 'Pesachim 40a:14', 'Pesachim 40a:15', 'Pesachim 36a:18', 'Pesachim 36a:19', 'Pesachim 39a:13', 'Pesachim 39a:14', 'Pesachim 120b:5', 'Pesachim 109b:5', 'Pesachim 108a:4', 'Pesachim 42a:5']
    assert all('obligation_and_material' not in f for f in m.WORLD["facts"])
    assert 'matza_statute' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Mishnah Pesachim 1:1', 'Mishnah Pesachim 2:2', 'Mishnah Beitzah 1:1', 'Mishnah Makkot 3:2', 'Mishnah Pesachim 3:3', 'Mishnah Pesachim 9:3']
    assert all('implementing_rows' not in f for f in m.WORLD["facts"])
    assert 'leaven_ban' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Pesachim 5b:2', 'Pesachim 6a:6', 'Pesachim 10b:15', 'Pesachim 43a:18']
    assert all('two_phrase_machine' not in f for f in m.WORLD["facts"])
    assert 'seen_found_division' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[15]["cites"] == ['Mishnah Pesachim 10:5', 'Mishnah Pesachim 2:5']
    assert all('seder_trio' not in f for f in m.WORLD["facts"])
    assert 'pesach_answer' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[16]["cites"] == ['Pesachim 85a:2', 'Pesachim 84a:14', 'Pesachim 84a:15', 'Pesachim 84a:13', 'Pesachim 85b:2', 'Pesachim 86a:15', 'Pesachim 83b:12', 'Pesachim 83b:14', 'Zevachim 36a:3']
    assert all('scope_carry_and_burn' not in f for f in m.WORLD["facts"])
    assert 'bone_clause' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
