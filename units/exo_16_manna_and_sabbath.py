#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_16_manna_and_sabbath — 16:1-36
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_16_manna_and_sabbath.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The manna and the Sabbath (16:1-36)"""
from machine import Machine

m = Machine("exo_16_manna_and_sabbath")

# -------------------------- Exod.16.1 · INTO_THE_WILDERNESS_OF_SIN ---------
# וַיִּסְעוּ מֵאֵילִם וַיָּבֹאוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל
# אֶל־מִדְבַּר־סִין אֲשֶׁר בֵּין־אֵילִם וּבֵין סִינָי בַּחֲמִשָּׁה עָשָׂר
# יוֹם לַחֹדֶשׁ הַשֵּׁנִי לְצֵאתָם מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And they journeyed from Elim, and all the congregation of the
# sons of Israel came to the wilderness of Sin, which is between Elim and
# Sinai, on the fifteenth day of the second month after their going out from
# the land of Egypt."
m.step("Exod.16.1")
# ‹וַיִּסְעוּ מֵאֵילִם וַיָּבֹאוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל
# אֶל־מִדְבַּר־סִין אֲשֶׁר בֵּין־אֵילִם וּבֵין סִינָי› (“and-journey from-
# Elim and-come/bring all congregation son Israel to pasture Sin which
# between Elim and-between Sinai”) — fact holds: and-come/bring-to-pasture-
# Sin
m.fact("va_yavou_el_midbar_sin")

# -------------------------- Exod.16.2 · THE_WHOLE_CONGREGATION_MURMURS -----
# וילינו וַיִּלּוֹנוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל עַל־מֹשֶׁה וְעַל־אַהֲרֹן
# בַּמִּדְבָּר
# "[EN-AID] And all the congregation of the sons of Israel murmured against
# Moses and against Aaron in the wilderness."
m.step("Exod.16.2")
# ‹וילינו וַיִּלּוֹנוּ כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל עַל־מֹשֶׁה וְעַל־אַהֲרֹן
# בַּמִּדְבָּר› (“and-stop and-stop all congregation son Israel over Moses
# and-over Aaron in-pasture”) — fact holds: and-stop-over-Moses-and-over-
# Aaron
m.fact("va_yilonu_al_moshe_ve_al_aharon")

# -------------------------- Exod.16.3 · THE_FLESH_POTS ---------------------
# וַיֹּאמְרוּ אֲלֵהֶם בְּנֵי יִשְׂרָאֵל מִי־יִתֵּן מוּתֵנוּ בְיַד־יְהוָה
# בְּאֶרֶץ מִצְרַיִם בְּשִׁבְתֵּנוּ עַל־סִיר הַבָּשָׂר בְּאָכְלֵנוּ לֶחֶם
# לָשֹׂבַע כִּי־הוֹצֵאתֶם אֹתָנוּ אֶל־הַמִּדְבָּר הַזֶּה לְהָמִית
# אֶת־כָּל־הַקָּהָל הַזֶּה בָּרָעָב
# "[EN-AID] And the sons of Israel said to them: Would that we had died by
# the hand of the LORD in the land of Egypt, when we sat by the flesh-pot,
# when we ate bread to the full — for you have brought us out to this
# wilderness, to kill this whole assembly with hunger."
m.step("Exod.16.3")
# ‹מִי־יִתֵּן מוּתֵנוּ בְיַד־יְהוָה בְּאֶרֶץ מִצְרַיִם בְּשִׁבְתֵּנוּ
# עַל־סִיר הַבָּשָׂר בְּאָכְלֵנוּ לֶחֶם לָשֹׂבַע› (“who? set die-us/our in-
# hand YHWH in-earth Egypt in-dwell/sit-us/our over pot the-flesh in-eat-
# us/our food to-satisfaction-joy)”) — fact holds: who?-set-mutenu
m.fact("mi_yiten_mutenu")

# -------------------------- Exod.16.4 · BREAD_FROM_HEAVEN ------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה הִנְנִי מַמְטִיר לָכֶם לֶחֶם מִן־הַשָּׁמָיִם
# וְיָצָא הָעָם וְלָקְטוּ דְּבַר־יוֹם בְּיוֹמוֹ לְמַעַן אֲנַסֶּנּוּ הֲיֵלֵךְ
# בְּתוֹרָתִי אִם־לֹא
# "[EN-AID] And the LORD said to Moses: Behold, I rain for you bread from
# the heavens; and the people shall go out and gather the day's portion in
# its day, that I may test him — will he walk in My law, or not?"
m.step("Exod.16.4")
# ‹הִנְנִי מַמְטִיר לָכֶם לֶחֶם מִן־הַשָּׁמָיִם› (“lo!-me/my rain to-
# you/your(pl) food from the-heavens”) — the-LORD speaks a demand — LET:
# and-pick-up-word/thing-day-in-yomo
m.declare("YHWH", "LET",
          "ve_laqtu_devar_yom_be_yomo")

# -------------------------- Exod.16.5 · DOUBLE_ON_THE_SIXTH ----------------
# וְהָיָה בַּיּוֹם הַשִּׁשִּׁי וְהֵכִינוּ אֵת אֲשֶׁר־יָבִיאוּ וְהָיָה
# מִשְׁנֶה עַל אֲשֶׁר־יִלְקְטוּ יוֹם יוֹם
# "[EN-AID] And it shall be on the sixth day, that they shall prepare that
# which they bring in; and it shall be double what they gather day by day."
m.step("Exod.16.5")
# ‹וְהָיָה בַּיּוֹם הַשִּׁשִּׁי וְהֵכִינוּ אֵת אֲשֶׁר־יָבִיאוּ וְהָיָה
# מִשְׁנֶה› (“and-be in-day the-sixth and-be-erect obj-marker which
# come/bring and-be repetition”) — the-LORD speaks a demand — LET: and-be-
# erect-repetition
m.declare("YHWH", "LET",
          "ve_hekhinu_mishne")

# -------------------------- Exod.16.6 · EVENING_AND_YOU_SHALL_KNOW ---------
# וַיֹּאמֶר מֹשֶׁה וְאַהֲרֹן אֶל־כָּל־בְּנֵי יִשְׂרָאֵל עֶרֶב וִידַעְתֶּם
# כִּי יְהוָה הוֹצִיא אֶתְכֶם מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And Moses and Aaron said to all the sons of Israel: At evening —
# and you shall know that the LORD has brought you out from the land of
# Egypt."
m.step("Exod.16.6")
# ‹עֶרֶב וִידַעְתֶּם כִּי יְהוָה הוֹצִיא אֶתְכֶם מֵאֶרֶץ מִצְרָיִם›
# (“evening and-know that YHWH bring-forth obj-marker-you/your(pl) from-
# earth Egypt”) — fact holds: evening-vi-ydatem
m.fact("erev_vi_ydatem")

# -------------------------- Exod.16.7 · MORNING_AND_THE_GLORY --------------
# וּבֹקֶר וּרְאִיתֶם אֶת־כְּבוֹד יְהוָה בְּשָׁמְעוֹ אֶת־תְּלֻנֹּתֵיכֶם
# עַל־יְהוָה וְנַחְנוּ מָה כִּי תלונו תַלִּינוּ עָלֵינוּ
# "[EN-AID] And at morning — and you shall see the glory of the LORD, in His
# hearing your murmurings against the LORD; and we — what are we, that you
# murmur against us?"
m.step("Exod.16.7")
# ‹וּבֹקֶר וּרְאִיתֶם אֶת־כְּבוֹד יְהוָה בְּשָׁמְעוֹ אֶת־תְּלֻנֹּתֵיכֶם
# עַל־יְהוָה› (“and-morning and-see obj-marker weight YHWH in-hear-him/its
# obj-marker grumbling-you/your(pl) over YHWH”) — fact holds: and-see-obj-
# marker-weight-the-LORD
m.fact("u_reitem_et_kevod_YHWH")

# -------------------------- Exod.16.8 · NOT_AGAINST_US ---------------------
# וַיֹּאמֶר מֹשֶׁה בְּתֵת יְהוָה לָכֶם בָּעֶרֶב בָּשָׂר לֶאֱכֹל וְלֶחֶם
# בַּבֹּקֶר לִשְׂבֹּעַ בִּשְׁמֹעַ יְהוָה אֶת־תְּלֻנֹּתֵיכֶם אֲשֶׁר־אַתֶּם
# מַלִּינִם עָלָיו וְנַחְנוּ מָה לֹא־עָלֵינוּ תְלֻנֹּתֵיכֶם כִּי עַל־יְהוָה
# "[EN-AID] And Moses said: In the LORD's giving you flesh at evening to
# eat, and bread at morning to the full — in the LORD's hearing your
# murmurings which you murmur against Him; and we — what are we? Not against
# us are your murmurings, but against the LORD."
m.step("Exod.16.8")
# ‹וְנַחְנוּ מָה לֹא־עָלֵינוּ תְלֻנֹּתֵיכֶם כִּי עַל־יְהוָה› (“and-we what
# not over-us/our grumbling-you/your(pl) that over YHWH”) — fact holds: not-
# alenu-telunotekhem
m.fact("lo_alenu_telunotekhem")

# -------------------------- Exod.16.9 · DRAW_NEAR --------------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־אַהֲרֹן אֱמֹר אֶל־כָּל־עֲדַת בְּנֵי יִשְׂרָאֵל
# קִרְבוּ לִפְנֵי יְהוָה כִּי שָׁמַע אֵת תְּלֻנֹּתֵיכֶם
# "[EN-AID] And Moses said to Aaron: Say to all the congregation of the sons
# of Israel: Draw near before the LORD — for He has heard your murmurings."
m.step("Exod.16.9")
# ‹אֱמֹר אֶל־כָּל־עֲדַת בְּנֵי יִשְׂרָאֵל קִרְבוּ לִפְנֵי יְהוָה› (“say to
# all congregation son Israel bring-near to-face YHWH”) — Moses speaks a
# demand — LET: bring-near-lifne-the-LORD
m.declare("moshe", "LET",
          "qirvu_lifne_YHWH")

# -------------------------- Exod.16.10 · THE_GLORY_IN_THE_CLOUD ------------
# וַיְהִי כְּדַבֵּר אַהֲרֹן אֶל־כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל וַיִּפְנוּ
# אֶל־הַמִּדְבָּר וְהִנֵּה כְּבוֹד יְהוָה נִרְאָה בֶּעָנָן
# "[EN-AID] And it was, as Aaron spoke to all the congregation of the sons
# of Israel, that they turned toward the wilderness; and behold — the glory
# of the LORD appeared in the cloud."
m.step("Exod.16.10")
# ‹וַיְהִי כְּדַבֵּר אַהֲרֹן אֶל־כָּל־עֲדַת בְּנֵי־יִשְׂרָאֵל› (“and-be
# like-speak Aaron to all congregation son Israel”) — demand settled (popped
# from the queue): bring-near-lifne-the-LORD
m.result("qirvu_lifne_YHWH", tmark="t1")
# ‹וְהִנֵּה כְּבוֹד יְהוָה נִרְאָה בֶּעָנָן› (“and-behold weight YHWH see
# in-cloud”) — event: nirat-weight-the-LORD — theme kevod-YHWH
m.event("nirat_kevod_YHWH", themes=["kevod-YHWH"])

# -------------------------- Exod.16.11 · THE_FRAME -------------------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Exod.16.11")
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה לֵּאמֹר› (“and-speak YHWH to Moses to-say”)
# — fact holds: and-speak-16
m.fact("va_yedaber_16")

# -------------------------- Exod.16.12 · I_HAVE_HEARD ----------------------
# שָׁמַעְתִּי אֶת־תְּלוּנֹּת בְּנֵי יִשְׂרָאֵל דַּבֵּר אֲלֵהֶם לֵאמֹר בֵּין
# הָעַרְבַּיִם תֹּאכְלוּ בָשָׂר וּבַבֹּקֶר תִּשְׂבְּעוּ־לָחֶם וִידַעְתֶּם
# כִּי אֲנִי יְהוָה אֱלֹהֵיכֶם
# "[EN-AID] I have heard the murmurings of the sons of Israel — speak to
# them, saying: Between the evenings you shall eat flesh, and at morning you
# shall be filled with bread; and you shall know that I am the LORD your
# God."
m.step("Exod.16.12")
# ‹שָׁמַעְתִּי אֶת־תְּלוּנֹּת בְּנֵי יִשְׂרָאֵל› (“hear obj-marker grumbling
# son Israel”) — fact holds: hear-obj-marker-grumbling
m.fact("shamati_et_telunot")
# ‹וִידַעְתֶּם כִּי אֲנִי יְהוָה אֱלֹהֵיכֶם› (“and-know that YHWH God-
# you/your(pl)”) — fact holds: ani-the-LORD-elohekhem
m.fact("ani_YHWH_elohekhem")

# -------------------------- Exod.16.13 · QUAIL_AND_DEW ---------------------
# וַיְהִי בָעֶרֶב וַתַּעַל הַשְּׂלָו וַתְּכַס אֶת־הַמַּחֲנֶה וּבַבֹּקֶר
# הָיְתָה שִׁכְבַת הַטַּל סָבִיב לַמַּחֲנֶה
# "[EN-AID] And it was at evening, that the quail came up and covered the
# camp; and at morning there was a layer of dew around the camp."
m.step("Exod.16.13")
# ‹וַיְהִי בָעֶרֶב וַתַּעַל הַשְּׂלָו וַתְּכַס אֶת־הַמַּחֲנֶה› (“and-be in-
# evening and-go-up the-quail-collectively and-plump obj-marker the-camp”) —
# event: matan-flesh-and-food — agent the-LORD; theme ha-selav
m.event("matan_basar_va_lechem", agent="YHWH", themes=["ha-selav"])
# ‹וּבַבֹּקֶר הָיְתָה שִׁכְבַת הַטַּל סָבִיב לַמַּחֲנֶה› (“and-in-morning be
# lying-down the-dew circle to-camp”) — fact holds: lying-down-the-dew
m.fact("shikhvat_ha_tal")

# -------------------------- Exod.16.14 · FINE_AS_FROST ---------------------
# וַתַּעַל שִׁכְבַת הַטָּל וְהִנֵּה עַל־פְּנֵי הַמִּדְבָּר דַּק מְחֻסְפָּס
# דַּק כַּכְּפֹר עַל־הָאָרֶץ
# "[EN-AID] And the layer of dew went up, and behold — on the face of the
# wilderness a fine flake-like thing, fine as frost on the ground."
m.step("Exod.16.14")
# ‹וְהִנֵּה עַל־פְּנֵי הַמִּדְבָּר דַּק מְחֻסְפָּס דַּק כַּכְּפֹר
# עַל־הָאָרֶץ› (“and-behold over face the-pasture thin shred thin like-cover
# over the-earth”) — fact holds: thin-shred
m.fact("daq_mechuspas")

# -------------------------- Exod.16.15 · WHAT_IS_IT ------------------------
# וַיִּרְאוּ בְנֵי־יִשְׂרָאֵל וַיֹּאמְרוּ אִישׁ אֶל־אָחִיו מָן הוּא כִּי לֹא
# יָדְעוּ מַה־הוּא וַיֹּאמֶר מֹשֶׁה אֲלֵהֶם הוּא הַלֶּחֶם אֲשֶׁר נָתַן
# יְהוָה לָכֶם לְאָכְלָה
# "[EN-AID] And the sons of Israel saw, and said each to his brother: What
# is it? — for they knew not what it was; and Moses said to them: It is the
# bread which the LORD has given you to eat."
m.step("Exod.16.15")
# ‹מָן הוּא כִּי לֹא יָדְעוּ מַה־הוּא› (“whatness he/it that not know what
# he/it”) — fact holds: whatness-he/it
m.fact("man_hu")

# -------------------------- Exod.16.16 · AN_OMER_A_HEAD --------------------
# זֶה הַדָּבָר אֲשֶׁר צִוָּה יְהוָה לִקְטוּ מִמֶּנּוּ אִישׁ לְפִי אָכְלוֹ
# עֹמֶר לַגֻּלְגֹּלֶת מִסְפַּר נַפְשֹׁתֵיכֶם אִישׁ לַאֲשֶׁר בְּאָהֳלוֹ
# תִּקָּחוּ
# "[EN-AID] This is the thing which the LORD commanded: Gather of it, each
# man according to his eating; an omer a head, by the number of your souls —
# each man for those in his tent shall you take."
m.step("Exod.16.16")
# ‹זֶה הַדָּבָר אֲשֶׁר צִוָּה יְהוָה לִקְטוּ מִמֶּנּוּ אִישׁ לְפִי אָכְלוֹ›
# (“this the-word/thing which command YHWH pick-up from-us/our man to-mouth
# food-him/its”) — fact holds: heap-to-skull
m.fact("omer_la_gulgolet")

# -------------------------- Exod.16.17 · GREAT_AND_SMALL -------------------
# וַיַּעֲשׂוּ־כֵן בְּנֵי יִשְׂרָאֵל וַיִּלְקְטוּ הַמַּרְבֶּה וְהַמַּמְעִיט
# "[EN-AID] And the sons of Israel did so; and they gathered — he who took
# much, and he who took little."
m.step("Exod.16.17")
# ‹וַיַּעֲשׂוּ־כֵן בְּנֵי יִשְׂרָאֵל› (“and-make so son Israel”) — demand
# settled (popped from the queue): and-pick-up-word/thing-day-in-yomo
m.result("ve_laqtu_devar_yom_be_yomo", tmark="t1")

# -------------------------- Exod.16.18 · NO_LACK_NO_SURPLUS ----------------
# וַיָּמֹדּוּ בָעֹמֶר וְלֹא הֶעְדִּיף הַמַּרְבֶּה וְהַמַּמְעִיט לֹא הֶחְסִיר
# אִישׁ לְפִי־אָכְלוֹ לָקָטוּ
# "[EN-AID] And they measured with the omer, and he who took much had
# nothing over, and he who took little lacked nothing; each man according to
# his eating had they gathered."
m.step("Exod.16.18")
# ‹וַיָּמֹדּוּ בָעֹמֶר וְלֹא הֶעְדִּיף הַמַּרְבֶּה וְהַמַּמְעִיט לֹא
# הֶחְסִיר› (“and-stretch in-heap and-not be-redundant the-multiply and-the-
# pare-off not lack”) — fact holds: not-be-redundant-and-not-lack
m.fact("lo_hedif_ve_lo_hechsir")

# -------------------------- Exod.16.19 · LEAVE_NONE_TILL_MORNING -----------
# וַיֹּאמֶר מֹשֶׁה אֲלֵהֶם אִישׁ אַל־יוֹתֵר מִמֶּנּוּ עַד־בֹּקֶר
# "[EN-AID] And Moses said to them: Let no man leave over of it till
# morning."
m.step("Exod.16.19")
# ‹אִישׁ אַל־יוֹתֵר מִמֶּנּוּ עַד־בֹּקֶר› (“man do-not jut-over from-us/our
# until morning”) — Moses speaks a demand — LET: over-jut-over-from-it-
# until-morning
m.declare("moshe", "LET",
          "al_yoter_mimenu_ad_boqer")

# -------------------------- Exod.16.20 · WORMS_AND_WRATH -------------------
# וְלֹא־שָׁמְעוּ אֶל־מֹשֶׁה וַיּוֹתִרוּ אֲנָשִׁים מִמֶּנּוּ עַד־בֹּקֶר
# וַיָּרֻם תּוֹלָעִים וַיִּבְאַשׁ וַיִּקְצֹף עֲלֵהֶם מֹשֶׁה
# "[EN-AID] And they listened not to Moses, and men left over of it till
# morning, and it bred worms and stank; and Moses was angry with them."
m.step("Exod.16.20")
# ‹וַיּוֹתִרוּ אֲנָשִׁים מִמֶּנּוּ עַד־בֹּקֶר וַיָּרֻם תּוֹלָעִים
# וַיִּבְאַשׁ› (“and-jut-over man from-us/our until morning and-rise-high
# crimson-grub and-smell-bad”) — fact holds: and-rise-high-crimson-grub
m.fact("va_yarum_tolaim")

# -------------------------- Exod.16.21 · MORNING_BY_MORNING ----------------
# וַיִּלְקְטוּ אֹתוֹ בַּבֹּקֶר בַּבֹּקֶר אִישׁ כְּפִי אָכְלוֹ וְחַם
# הַשֶּׁמֶשׁ וְנָמָס
# "[EN-AID] And they gathered it morning by morning, each man according to
# his eating; and when the sun grew hot, it melted."
m.step("Exod.16.21")
# ‹וְחַם הַשֶּׁמֶשׁ וְנָמָס› (“and-be-hot the-sun and-liquefy”) — fact
# holds: and-be-hot-the-sun-and-liquefy
m.fact("ve_cham_ha_shemesh_ve_namas")

# -------------------------- Exod.16.22 · THE_SIXTH_DAY_DOUBLE --------------
# וַיְהִי בַּיּוֹם הַשִּׁשִּׁי לָקְטוּ לֶחֶם מִשְׁנֶה שְׁנֵי הָעֹמֶר לָאֶחָד
# וַיָּבֹאוּ כָּל־נְשִׂיאֵי הָעֵדָה וַיַּגִּידוּ לְמֹשֶׁה
# "[EN-AID] And it was on the sixth day, that they gathered double bread —
# two omers for the one; and all the princes of the congregation came and
# told Moses."
m.step("Exod.16.22")
# ‹וַיְהִי בַּיּוֹם הַשִּׁשִּׁי לָקְטוּ לֶחֶם מִשְׁנֶה שְׁנֵי הָעֹמֶר
# לָאֶחָד› (“and-be in-day the-sixth pick-up food repetition two the-heap
# to-one”) — demand settled (popped from the queue): and-be-erect-repetition
m.result("ve_hekhinu_mishne", tmark="t1")

# -------------------------- Exod.16.23 · TOMORROW_IS_THE_REST --------------
# וַיֹּאמֶר אֲלֵהֶם הוּא אֲשֶׁר דִּבֶּר יְהוָה שַׁבָּתוֹן שַׁבַּת־קֹדֶשׁ
# לַיהוָה מָחָר אֵת אֲשֶׁר־תֹּאפוּ אֵפוּ וְאֵת אֲשֶׁר־תְּבַשְּׁלוּ
# בַּשֵּׁלוּ וְאֵת כָּל־הָעֹדֵף הַנִּיחוּ לָכֶם לְמִשְׁמֶרֶת עַד־הַבֹּקֶר
# "[EN-AID] And he said to them: This is what the LORD spoke — a solemn
# rest, a holy sabbath to the LORD, is tomorrow; that which you would bake —
# bake, and that which you would boil — boil, and all the surplus lay up for
# yourselves in keeping until the morning."
m.step("Exod.16.23")
# ‹שַׁבָּתוֹן שַׁבַּת־קֹדֶשׁ לַיהוָה מָחָר› (“sabbatism intermission
# holiness to-YHWH deferred”) — Moses speaks a demand — LET: obj-marker-the-
# be-redundant-deposit-to-watch
m.declare("moshe", "LET",
          "et_ha_odef_hanichu_le_mishmeret")

# -------------------------- Exod.16.24 · IT_DID_NOT_STINK ------------------
# וַיַּנִּיחוּ אֹתוֹ עַד־הַבֹּקֶר כַּאֲשֶׁר צִוָּה מֹשֶׁה וְלֹא הִבְאִישׁ
# וְרִמָּה לֹא־הָיְתָה בּוֹ
# "[EN-AID] And they laid it up until the morning, as Moses commanded; and
# it did not stink, and no worm was in it."
m.step("Exod.16.24")
# ‹וַיַּנִּיחוּ אֹתוֹ עַד־הַבֹּקֶר כַּאֲשֶׁר צִוָּה מֹשֶׁה› (“and-deposit
# obj-marker-him/its until the-morning like-as/which command Moses”) —
# demand settled (popped from the queue): obj-marker-the-be-redundant-
# deposit-to-watch
m.result("et_ha_odef_hanichu_le_mishmeret", tmark="t1")

# -------------------------- Exod.16.25 · EAT_IT_TODAY ----------------------
# וַיֹּאמֶר מֹשֶׁה אִכְלֻהוּ הַיּוֹם כִּי־שַׁבָּת הַיּוֹם לַיהוָה הַיּוֹם
# לֹא תִמְצָאֻהוּ בַּשָּׂדֶה
# "[EN-AID] And Moses said: Eat it today, for today is a sabbath to the
# LORD; today you shall not find it in the field."
m.step("Exod.16.25")
# ‹אִכְלֻהוּ הַיּוֹם כִּי־שַׁבָּת הַיּוֹם לַיהוָה› (“eat-him/its the-day
# that intermission the-day to-YHWH”) — fact holds: intermission-the-day-to-
# the-LORD
m.fact("shabat_ha_yom_la_YHWH")

# -------------------------- Exod.16.26 · SIX_DAYS_AND_THE_SEVENTH ----------
# שֵׁשֶׁת יָמִים תִּלְקְטֻהוּ וּבַיּוֹם הַשְּׁבִיעִי שַׁבָּת לֹא
# יִהְיֶה־בּוֹ
# "[EN-AID] Six days you shall gather it; and on the seventh day — a
# sabbath: it shall not be in it."
m.step("Exod.16.26")
# ‹שֵׁשֶׁת יָמִים תִּלְקְטֻהוּ וּבַיּוֹם הַשְּׁבִיעִי שַׁבָּת לֹא
# יִהְיֶה־בּוֹ› (“six day pick-up-him/its and-in-day the-seventh
# intermission not be in-him/its”) — fact holds: six-day-tilqetuhu
m.fact("sheshet_yamim_tilqetuhu")

# -------------------------- Exod.16.27 · THEY_FOUND_NOTHING ----------------
# וַיְהִי בַּיּוֹם הַשְּׁבִיעִי יָצְאוּ מִן־הָעָם לִלְקֹט וְלֹא מָצָאוּ
# "[EN-AID] And it was on the seventh day, that some of the people went out
# to gather — and they found none."
m.step("Exod.16.27")
# ‹וַיְהִי בַּיּוֹם הַשְּׁבִיעִי יָצְאוּ מִן־הָעָם לִלְקֹט וְלֹא מָצָאוּ›
# (“and-be in-day the-seventh bring-forth from the-people to-pick-up and-not
# find”) — fact holds: bring-forth-from-the-people-lilqot
m.fact("yatzu_min_ha_am_lilqot")

# -------------------------- Exod.16.28 · HOW_LONG_DO_YOU_REFUSE ------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה עַד־אָנָה מֵאַנְתֶּם לִשְׁמֹר מִצְוֺתַי
# וְתוֹרֹתָי
# "[EN-AID] And the LORD said to Moses: How long do you refuse to keep My
# commandments and My laws?"
m.step("Exod.16.28")
# ‹עַד־אָנָה מֵאַנְתֶּם לִשְׁמֹר מִצְוֺתַי וְתוֹרֹתָי› (“until where? refuse
# to-keep/guard commandment-me/my and-precept-me/my”) — test FAIL — oracle-
# word anasenu, on the-go-in-torati
m.test("FAIL", "anasenu", "ha_yelekh_be_torati")

# -------------------------- Exod.16.29 · LET_NO_MAN_GO_OUT -----------------
# רְאוּ כִּי־יְהוָה נָתַן לָכֶם הַשַּׁבָּת עַל־כֵּן הוּא נֹתֵן לָכֶם
# בַּיּוֹם הַשִּׁשִּׁי לֶחֶם יוֹמָיִם שְׁבוּ אִישׁ תַּחְתָּיו אַל־יֵצֵא
# אִישׁ מִמְּקֹמוֹ בַּיּוֹם הַשְּׁבִיעִי
# "[EN-AID] See, that the LORD has given you the Sabbath — therefore He
# gives you on the sixth day bread for two days; sit every man in his place:
# let no man go out of his place on the seventh day."
m.step("Exod.16.29")
# ‹שְׁבוּ אִישׁ תַּחְתָּיו אַל־יֵצֵא אִישׁ מִמְּקֹמוֹ בַּיּוֹם הַשְּׁבִיעִי›
# (“dwell/sit man under-him/its do-not bring-forth man from-place-him/its
# in-day the-seventh”) — the-LORD speaks a demand — LET: over-bring-forth-
# man-who?-meqomo
m.declare("YHWH", "LET",
          "al_yetze_ish_mi_meqomo")

# -------------------------- Exod.16.30 · AND_THE_PEOPLE_RESTED -------------
# וַיִּשְׁבְּתוּ הָעָם בַּיּוֹם הַשְּׁבִעִי
# "[EN-AID] And the people rested on the seventh day."
m.step("Exod.16.30")
# ‹וַיִּשְׁבְּתוּ הָעָם בַּיּוֹם הַשְּׁבִעִי› (“and-cease the-people in-day
# the-seventh”) — demand settled (popped from the queue): over-bring-forth-
# man-who?-meqomo
m.result("al_yetze_ish_mi_meqomo", tmark="t1")

# -------------------------- Exod.16.31 · THE_HOUSE_NAMED_IT_MANNA ----------
# וַיִּקְרְאוּ בֵית־יִשְׂרָאֵל אֶת־שְׁמוֹ מָן וְהוּא כְּזֶרַע גַּד לָבָן
# וְטַעְמוֹ כְּצַפִּיחִת בִּדְבָשׁ
# "[EN-AID] And the house of Israel called its name Manna; and it was like
# coriander seed, white, and its taste like a wafer in honey."
m.step("Exod.16.31")
# ‹וַיִּקְרְאוּ בֵית־יִשְׂרָאֵל אֶת־שְׁמוֹ מָן› (“and-call house Israel obj-
# marker name-him/its whatness”) — named: ha-lechem := Man
m.name("ha-lechem", "Man")

# -------------------------- Exod.16.32 · A_KEEPSAKE_FOR_GENERATIONS --------
# וַיֹּאמֶר מֹשֶׁה זֶה הַדָּבָר אֲשֶׁר צִוָּה יְהוָה מְלֹא הָעֹמֶר מִמֶּנּוּ
# לְמִשְׁמֶרֶת לְדֹרֹתֵיכֶם לְמַעַן יִרְאוּ אֶת־הַלֶּחֶם אֲשֶׁר הֶאֱכַלְתִּי
# אֶתְכֶם בַּמִּדְבָּר בְּהוֹצִיאִי אֶתְכֶם מֵאֶרֶץ מִצְרָיִם
# "[EN-AID] And Moses said: This is the thing which the LORD commanded: The
# fill of the omer of it in keeping for your generations — that they may see
# the bread which I fed you in the wilderness, when I brought you out from
# the land of Egypt."
m.step("Exod.16.32")
# ‹לְמַעַן יִרְאוּ אֶת־הַלֶּחֶם› (“so-that see obj-marker the-food”) — fact
# holds: fulness-the-heap-to-watch
m.fact("melo_ha_omer_le_mishmeret")

# -------------------------- Exod.16.33 · THE_JAR ---------------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־אַהֲרֹן קַח צִנְצֶנֶת אַחַת וְתֶן־שָׁמָּה
# מְלֹא־הָעֹמֶר מָן וְהַנַּח אֹתוֹ לִפְנֵי יְהוָה לְמִשְׁמֶרֶת לְדֹרֹתֵיכֶם
# "[EN-AID] And Moses said to Aaron: Take one jar, and put there the fill of
# the omer of manna; and lay it before the LORD, in keeping for your
# generations."
m.step("Exod.16.33")
# ‹קַח צִנְצֶנֶת אַחַת וְתֶן־שָׁמָּה מְלֹא־הָעֹמֶר מָן› (“take vase one and-
# set there-ward fulness the-heap whatness”) — Moses speaks a demand — LET:
# take-vase-one
m.declare("moshe", "LET",
          "qach_tzintzenet_achat")

# -------------------------- Exod.16.34 · BEFORE_THE_TESTIMONY --------------
# כַּאֲשֶׁר צִוָּה יְהוָה אֶל־מֹשֶׁה וַיַּנִּיחֵהוּ אַהֲרֹן לִפְנֵי הָעֵדֻת
# לְמִשְׁמָרֶת
# "[EN-AID] As the LORD commanded Moses, so Aaron laid it before the
# Testimony, in keeping."
m.step("Exod.16.34")
# ‹וַיַּנִּיחֵהוּ אַהֲרֹן לִפְנֵי הָעֵדֻת לְמִשְׁמָרֶת› (“and-deposit-
# him/its Aaron to-face the-testimony to-watch”) — demand settled (popped
# from the queue): take-vase-one
m.result("qach_tzintzenet_achat", tmark="t1")

# -------------------------- Exod.16.35 · FORTY_YEARS -----------------------
# וּבְנֵי יִשְׂרָאֵל אָכְלוּ אֶת־הַמָּן אַרְבָּעִים שָׁנָה עַד־בֹּאָם
# אֶל־אֶרֶץ נוֹשָׁבֶת אֶת־הַמָּן אָכְלוּ עַד־בֹּאָם אֶל־קְצֵה אֶרֶץ כְּנָעַן
# "[EN-AID] And the sons of Israel ate the manna forty years, until their
# coming to an inhabited land; the manna they ate, until their coming to the
# edge of the land of Canaan."
m.step("Exod.16.35")
# ‹וּבְנֵי יִשְׂרָאֵל אָכְלוּ אֶת־הַמָּן אַרְבָּעִים שָׁנָה עַד־בֹּאָם
# אֶל־אֶרֶץ נוֹשָׁבֶת› (“and-son Israel eat obj-marker the-whatness forty
# years until come/bring-them/their to earth dwell/sit”) — fact holds: eat-
# obj-marker-the-whatness-forty-years
m.fact("akhlu_et_ha_man_arbaim_shana")

# -------------------------- Exod.16.36 · THE_OMER_GLOSS --------------------
# וְהָעֹמֶר עֲשִׂרִית הָאֵיפָה הוּא
# "[EN-AID] And the omer — a tenth of the efa it is."
m.step("Exod.16.36")
# ‹וְהָעֹמֶר עֲשִׂרִית הָאֵיפָה הוּא› (“and-the-heap tenth the-ephah he/it”)
# — fact holds: and-the-heap-tenth-the-ephah
m.fact("ve_ha_omer_asirit_ha_efa")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha-lechem': 'Man'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == [('FAIL', 'anasenu', 'ha_yelekh_be_torati')]
    assert m.open_demands() == ['al_yoter_mimenu_ad_boqer']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yavou_el_midbar_sin', 'va_yilonu_al_moshe_ve_al_aharon', 'mi_yiten_mutenu', 'erev_vi_ydatem', 'u_reitem_et_kevod_YHWH', 'lo_alenu_telunotekhem', 'va_yedaber_16', 'shamati_et_telunot', 'ani_YHWH_elohekhem', 'shikhvat_ha_tal', 'daq_mechuspas', 'man_hu', 'omer_la_gulgolet', 'lo_hedif_ve_lo_hechsir', 'va_yarum_tolaim', 've_cham_ha_shemesh_ve_namas', 'shabat_ha_yom_la_YHWH', 'sheshet_yamim_tilqetuhu', 'yatzu_min_ha_am_lilqot', 'melo_ha_omer_le_mishmeret', 'akhlu_et_ha_man_arbaim_shana', 've_ha_omer_asirit_ha_efa'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 16
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
