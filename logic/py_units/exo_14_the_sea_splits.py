#!/usr/bin/env python3
# =============================================================================
# exo_14_the_sea_splits — 14:1-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_14_the_sea_splits.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The sea splits (14:1-31)"""
from machine import Machine

m = Machine("exo_14_the_sea_splits")

# -------------------------- Exod.14.1 · THE_FRAME --------------------------
# ‹וַיְדַבֵּר יְהֹוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# "[EN-AID] And the LORD spoke to Moses, saying:"
m.step("Exod.14.1")
# ‹וַיְדַבֵּר יְהֹוָה אֶל־מֹשֶׁה› (“and-speak YHWH to Moses”)
# ‹לֵּאמֹר› (“to-say”)
# — fact holds: and-speak-14
m.fact("va_yedaber_14")

# -------------------------- Exod.14.2 · TURN_BACK_AND_CAMP -----------------
# ‹דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל› (“speak to son Israel”)
# ‹וְיָשֻׁבוּ וְיַחֲנוּ לִפְנֵי› (“and-return and-encamp to-face”)
# ‹פִּי הַחִירֹת בֵּין› (“Pi-hahiroth between”)
# ‹מִגְדֹּל וּבֵין הַיָּם› (“Migdol and-between the-seas”)
# ‹לִפְנֵי בַּעַל צְפֹן› (“to-face Baal-zephon”)
# ‹נִכְחוֹ תַחֲנוּ עַל־הַיָּם› (“fore-part-him/its encamp over the-seas”)
# "[EN-AID] Speak to the sons of Israel, that they turn back and camp before
# Pi-hahiroth, between Migdol and the sea, before Baal-zephon; opposite it
# shall you camp, by the sea."
m.step("Exod.14.2")
# ‹דַּבֵּר אֶל־בְּנֵי יִשְׂרָאֵל› (“speak to son Israel”)
# ‹וְיָשֻׁבוּ וְיַחֲנוּ לִפְנֵי› (“and-return and-encamp to-face”)
# — the-LORD speaks a demand — LET: and-return-and-encamp
m.declare("YHWH", "LET",
          "ve_yashuvu_ve_yachanu")

# -------------------------- Exod.14.3 · THEY_ARE_ENTANGLED -----------------
# ‹וְאָמַר פַּרְעֹה לִבְנֵי› (“and-say Pharaoh to-son”)
# ‹יִשְׂרָאֵל נְבֻכִים הֵם› (“Israel involve they”)
# ‹בָּאָרֶץ סָגַר עֲלֵיהֶם› (“in-earth shut-up over-them/their”)
# ‹הַמִּדְבָּר› (“the-pasture”)
# "[EN-AID] And Pharaoh will say of the sons of Israel: They are entangled
# in the land — the wilderness has shut upon them."
m.step("Exod.14.3")
# ‹הֵם בָּאָרֶץ סָגַר› (“they in-earth shut-up”)
# ‹עֲלֵיהֶם הַמִּדְבָּר› (“over-them/their the-pasture”)
# — fact holds: involve-they-in-the-earth
m.fact("nevukhim_hem_ba_aretz")

# -------------------------- Exod.14.4 · I_WILL_BE_HONORED ------------------
# ‹וְחִזַּקְתִּי אֶת־לֵב־פַּרְעֹה וְרָדַף› (“and-fasten-upon obj-marker
# heart Pharaoh and-run-after-gone-by)”)
# ‹אַחֲרֵיהֶם וְאִכָּבְדָה בְּפַרְעֹה› (“after-them/their and-be-heavy in-
# Pharaoh”)
# ‹וּבְכָל־חֵילוֹ וְיָדְעוּ מִצְרַיִם› (“and-in-all force-him/its and-know
# Egyptian”)
# ‹כִּי־אֲנִי יְהוָה וַיַּעֲשׂוּ־כֵן› (“that YHWH and-make so”)
# "[EN-AID] And I will strengthen Pharaoh's heart, and he will pursue them;
# and I will be honored through Pharaoh and through all his host, and Egypt
# shall know that I am the LORD. And they did so."
m.step("Exod.14.4")
# ‹וַיַּעֲשׂוּ־כֵן› (“and-make so”)
# — demand settled (popped from the queue): and-return-and-encamp
m.result("ve_yashuvu_ve_yachanu", tmark="t1")

# -------------------------- Exod.14.5 · THE_HEART_TURNED -------------------
# ‹וַיֻּגַּד לְמֶלֶךְ מִצְרַיִם› (“and-tell to-king Egypt”)
# ‹כִּי בָרַח הָעָם› (“that bolt the-people”)
# ‹וַיֵּהָפֵךְ לְבַב פַּרְעֹה› (“and-turn-about heart Pharaoh”)
# ‹וַעֲבָדָיו אֶל־הָעָם וַיֹּאמרוּ› (“and-servant-him/its to the-people and-
# say”)
# ‹מַה־זֹּאת עָשִׂינוּ כִּי־שִׁלַּחְנוּ› (“what this make that send”)
# ‹אֶת־יִשְׂרָאֵל מֵעָבְדֵנוּ› (“obj-marker Israel from-work/serve-us/our”)
# "[EN-AID] And it was told the king of Egypt that the people had fled; and
# the heart of Pharaoh and his servants was turned about toward the people,
# and they said: What is this we have done, that we sent Israel from serving
# us?"
m.step("Exod.14.5")
# ‹וַיֵּהָפֵךְ לְבַב פַּרְעֹה› (“and-turn-about heart Pharaoh”)
# ‹וַעֲבָדָיו אֶל־הָעָם› (“and-servant-him/its to the-people”)
# — fact holds: and-turn-about-heart-Pharaoh
m.fact("va_yehafekh_levav_paro")

# -------------------------- Exod.14.6 · HE_HARNESSED_HIS_CHARIOT -----------
# ‹וַיֶּאְסֹר אֶת־רִכְבּוֹ וְאֶת־עַמּוֹ› (“and-yoke obj-marker vehicle-
# him/its and-obj-marker people-him/its”)
# ‹לָקַח עִמּוֹ› (“take with-him/its”)
# "[EN-AID] And he harnessed his chariot, and took his people with him."
m.step("Exod.14.6")
# ‹וַיֶּאְסֹר אֶת־רִכְבּוֹ› (“and-yoke obj-marker vehicle-him/its”)
# — fact holds: and-yoke-obj-marker-rikhbo
m.fact("va_yesor_et_rikhbo")

# -------------------------- Exod.14.7 · SIX_HUNDRED_CHOSEN -----------------
# ‹וַיִּקַּח שֵׁשׁ־מֵאוֹת רֶכֶב› (“and-take six hundred vehicle”)
# ‹בָּחוּר וְכֹל רֶכֶב› (“try and-all vehicle”)
# ‹מִצְרָיִם וְשָׁלִשִׁם עַל־כֻּלּוֹ› (“Egypt and-triple over all-him/its”)
# "[EN-AID] And he took six hundred chosen chariots, and all the chariots of
# Egypt, and officers over all of it."
m.step("Exod.14.7")
# ‹וַיִּקַּח שֵׁשׁ־מֵאוֹת רֶכֶב› (“and-take six hundred vehicle”)
# ‹בָּחוּר› (“try”)
# — fact holds: six-hundred-vehicle-try
m.fact("shesh_meot_rekhev_bachur")

# -------------------------- Exod.14.8 · WITH_A_HIGH_HAND -------------------
# ‹וַיְחַזֵּק יְהֹוָה אֶת־לֵב› (“and-fasten-upon YHWH obj-marker heart”)
# ‹פַּרְעֹה מֶלֶךְ מִצְרַיִם› (“Pharaoh king Egypt”)
# ‹וַיִּרְדֹּף אַחֲרֵי בְּנֵי› (“and-run-after-gone-by) after son”)
# ‹יִשְׂרָאֵל וּבְנֵי יִשְׂרָאֵל› (“Israel and-son Israel”)
# ‹יֹצְאִים בְּיָד רָמָה› (“bring-forth in-hand rise-high”)
# "[EN-AID] And the LORD strengthened the heart of Pharaoh king of Egypt,
# and he pursued the sons of Israel; and the sons of Israel were going out
# with a high hand."
m.step("Exod.14.8")
# ‹וּבְנֵי יִשְׂרָאֵל יֹצְאִים› (“and-son Israel bring-forth”)
# ‹בְּיָד רָמָה› (“in-hand rise-high”)
# — fact holds: bring-forth-in-hand-rise-high
m.fact("yotzim_be_yad_rama")

# -------------------------- Exod.14.9 · OVERTAKEN_AT_THE_CAMP --------------
# ‹וַיִּרְדְּפוּ מִצְרַיִם אַחֲרֵיהֶם› (“and-run-after-gone-by) Egyptian
# after-them/their”)
# ‹וַיַּשִּׂיגוּ אוֹתָם חֹנִים› (“and-reach obj-marker-them/their encamp”)
# ‹עַל־הַיָּם כָּל־סוּס רֶכֶב› (“over the-seas all horse vehicle”)
# ‹פַּרְעֹה וּפָרָשָׁיו וְחֵילוֹ› (“Pharaoh and-steed-him/its and-force-
# him/its”)
# ‹עַל־פִּי הַחִירֹת לִפְנֵי› (“over Pi-hahiroth to-face”)
# ‹בַּעַל צְפֹן› (“Baal-zephon”)
# "[EN-AID] And Egypt pursued after them — every chariot-horse of Pharaoh,
# and his horsemen, and his host — and overtook them camping by the sea, by
# Pi-hahiroth, before Baal-zephon."
m.step("Exod.14.9")
# ‹סוּס רֶכֶב פַּרְעֹה› (“horse vehicle Pharaoh”)
# ‹וּפָרָשָׁיו וְחֵילוֹ› (“and-steed-him/its and-force-him/its”)
# — fact holds: and-reach-otam-encamp
m.fact("va_yasigu_otam_chonim")

# -------------------------- Exod.14.10 · PHARAOH_DREW_NEAR -----------------
# ‹וּפַרְעֹה הִקְרִיב וַיִּשְׂאוּ› (“and-Pharaoh bring-near and-lift/carry”)
# ‹בְנֵי־יִשְׂרָאֵל אֶת־עֵינֵיהֶם וְהִנֵּה› (“son Israel obj-marker eye-
# them/their and-behold”)
# ‹מִצְרַיִם נֹסֵעַ אַחֲרֵיהֶם› (“Egyptian journey after-them/their”)
# ‹וַיִּירְאוּ מְאֹד וַיִּצְעֲקוּ› (“and-fear very and-shriek”)
# ‹בְנֵי־יִשְׂרָאֵל אֶל־יְהוָה› (“son Israel to YHWH”)
# "[EN-AID] And Pharaoh drew near; and the sons of Israel lifted their eyes,
# and behold — Egypt journeying after them; and they feared greatly, and the
# sons of Israel cried out to the LORD."
m.step("Exod.14.10")
# ‹וַיִּצְעֲקוּ בְנֵי־יִשְׂרָאֵל אֶל־יְהוָה› (“and-shriek son Israel to
# YHWH”)
# — fact holds: and-shriek-to-the-LORD
m.fact("va_yitzaqu_el_YHWH")

# -------------------------- Exod.14.11 · NO_GRAVES_IN_EGYPT ----------------
# ‹וַיֹּאמְרוּ אֶל־מֹשֶׁה הַמִבְּלִי› (“and-say to Moses the-from-failure”)
# ‹אֵין־קְבָרִים בְּמִצְרַיִם לְקַחְתָּנוּ› (“there-is-not sepulchre in-
# Egypt take-us/our”)
# ‹לָמוּת בַּמִּדְבָּר מַה־זֹּאת› (“to-die in-pasture what this”)
# ‹עָשִׂיתָ לָּנוּ לְהוֹצִיאָנוּ› (“make to-us/our to-bring-forth-us/our”)
# ‹מִמִּצְרָיִם› (“from-Egypt”)
# "[EN-AID] And they said to Moses: Is it from a lack of graves in Egypt
# that you took us to die in the wilderness? What is this you have done to
# us, to bring us out of Egypt?"
m.step("Exod.14.11")
# ‹מֹשֶׁה הַמִבְּלִי אֵין־קְבָרִים› (“Moses the-from-failure there-is-not
# sepulchre”)
# ‹בְּמִצְרַיִם לְקַחְתָּנוּ› (“in-Egypt take-us/our”)
# — fact holds: the-mibli-there-is-not-sepulchre
m.fact("ha_mibli_en_qevarim")

# -------------------------- Exod.14.12 · LEAVE_US_TO_SERVE_EGYPT -----------
# ‹הֲלֹא־זֶה הַדָּבָר אֲשֶׁר› (“is-it-not this the-word/thing which”)
# ‹דִּבַּרְנוּ אֵלֶיךָ בְמִצְרַיִם› (“speak to-you/your in-Egypt”)
# ‹לֵאמֹר חֲדַל מִמֶּנּוּ› (“to-say cease from-us/our”)
# ‹וְנַעַבְדָה אֶת־מִצְרָיִם כִּי› (“and-work/serve obj-marker Egyptian
# that”)
# ‹טוֹב לָנוּ עֲבֹד› (“good to-us/our work/serve”)
# ‹אֶת־מִצְרַיִם מִמֻּתֵנוּ בַּמִּדְבָּר› (“obj-marker Egyptian from-die-
# us/our in-pasture”)
# "[EN-AID] Is not this the word which we spoke to you in Egypt, saying:
# Leave us, and we will serve Egypt? For serving Egypt is better for us than
# our dying in the wilderness."
m.step("Exod.14.12")
# ‹חֲדַל מִמֶּנּוּ וְנַעַבְדָה› (“cease from-us/our and-work/serve”)
# ‹אֶת־מִצְרָיִם› (“obj-marker Egyptian”)
# — fact holds: cease-from-it-and-work/serve
m.fact("chadal_mimenu_ve_naavda")

# -------------------------- Exod.14.13 · STAND_STILL_AND_SEE ---------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־הָעָם› (“and-say Moses to the-people”)
# ‹אַל־תִּירָאוּ הִתְיַצְבוּ וּרְאוּ› (“do-not fear place and-see”)
# ‹אֶת־יְשׁוּעַת יְהוָה אֲשֶׁר־יַעֲשֶׂה› (“obj-marker something-saved YHWH
# which make”)
# ‹לָכֶם הַיּוֹם כִּי› (“to-you/your(pl) the-day that”)
# ‹אֲשֶׁר רְאִיתֶם אֶת־מִצְרַיִם› (“which see obj-marker Egyptian”)
# ‹הַיּוֹם לֹא תֹסִיפוּ› (“the-day not add”)
# ‹לִרְאֹתָם עוֹד עַד־עוֹלָם› (“to-see-them/their still/again until
# forever”)
# "[EN-AID] And Moses said to the people: Fear not — stand firm, and see the
# salvation of the LORD, which He will do for you today; for as you have
# seen Egypt today — you shall never see them again, forever."
m.step("Exod.14.13")
# ‹הִתְיַצְבוּ וּרְאוּ אֶת־יְשׁוּעַת› (“place and-see obj-marker something-
# saved”)
# ‹יְהוָה› (“YHWH”)
# — fact holds: see-obj-marker-something-saved-the-LORD
m.fact("reu_et_yeshuat_YHWH")

# -------------------------- Exod.14.14 · THE_LORD_WILL_FIGHT ---------------
# ‹יְהוָה יִלָּחֵם לָכֶם› (“YHWH feed-on to-you/your(pl)”)
# ‹וְאַתֶּם תַּחֲרִישׁוּן› (“and-you scratch-ward”)
# "[EN-AID] The LORD will fight for you — and you shall be silent."
m.step("Exod.14.14")
# ‹יְהוָה יִלָּחֵם לָכֶם› (“YHWH feed-on to-you/your(pl)”)
# ‹וְאַתֶּם תַּחֲרִישׁוּן› (“and-you scratch-ward”)
# — fact holds: the-LORD-feed-on-lakhem
m.fact("YHWH_yilachem_lakhem")

# -------------------------- Exod.14.15 · WHY_DO_YOU_CRY_TO_ME --------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹מַה־תִּצְעַק אֵלָי דַּבֵּר› (“what shriek to-me/my speak”)
# ‹אֶל־בְּנֵי־יִשְׂרָאֵל וְיִסָּעוּ› (“to son Israel and-journey”)
# "[EN-AID] And the LORD said to Moses: Why do you cry to Me? Speak to the
# sons of Israel, that they journey."
m.step("Exod.14.15")
# ‹דַּבֵּר אֶל־בְּנֵי־יִשְׂרָאֵל וְיִסָּעוּ› (“speak to son Israel and-
# journey”)
# — fact holds: speak-and-journey
m.fact("daber_ve_yisau")

# -------------------------- Exod.14.16 · LIFT_YOUR_STAFF_AND_SPLIT ---------
# ‹וְאַתָּה הָרֵם אֶת־מַטְּךָ› (“and-you rise-high obj-marker staff/tribe-
# you/your”)
# ‹וּנְטֵה אֶת־יָדְךָ עַל־הַיָּם› (“and-stretch obj-marker hand-you/your
# over the-seas”)
# ‹וּבְקָעֵהוּ וְיָבֹאוּ בְנֵי־יִשְׂרָאֵל› (“and-cleave-him/its and-
# come/bring son Israel”)
# ‹בְּתוֹךְ הַיָּם בַּיַּבָּשָׁה› (“in-midst the-seas in-dry-land”)
# "[EN-AID] And you — lift your staff, and stretch out your hand over the
# sea, and split it; and the sons of Israel shall come into the midst of the
# sea on the dry ground."
m.step("Exod.14.16")
# ‹וְאַתָּה הָרֵם אֶת־מַטְּךָ› (“and-you rise-high obj-marker staff/tribe-
# you/your”)
# ‹וּנְטֵה אֶת־יָדְךָ עַל־› (“and-stretch obj-marker hand-you/your over”)
# — the-LORD speaks a demand — LET: neteh-yadkha-and-veqaehu
m.declare("YHWH", "LET",
          "neteh_yadkha_u_veqaehu")

# -------------------------- Exod.14.17 · I_STRENGTHEN_EGYPT ----------------
# ‹וַאֲנִי הִנְנִי מְחַזֵּק› (“and-I lo!-me/my fasten-upon”)
# ‹אֶת־לֵב מִצְרַיִם וְיָבֹאוּ› (“obj-marker heart Egyptian and-come/bring”)
# ‹אַחֲרֵיהֶם וְאִכָּבְדָה בְּפַרְעֹה› (“after-them/their and-be-heavy in-
# Pharaoh”)
# ‹וּבְכָל־חֵילוֹ בְּרִכְבּוֹ וּבְפָרָשָׁיו› (“and-in-all force-him/its in-
# vehicle-him/its and-in-steed-him/its”)
# "[EN-AID] And I — behold, I strengthen the heart of Egypt, and they will
# come after them; and I will be honored through Pharaoh and through all his
# host, through his chariots and through his horsemen."
m.step("Exod.14.17")
# ‹וַאֲנִי הִנְנִי מְחַזֵּק› (“and-I lo!-me/my fasten-upon”)
# ‹אֶת־לֵב מִצְרַיִם› (“obj-marker heart Egyptian”)
# — fact holds: and-I-behold-I-fasten-upon
m.fact("va_ani_hineni_mechazeq")

# -------------------------- Exod.14.18 · EGYPT_SHALL_KNOW ------------------
# ‹וְיָדְעוּ מִצְרַיִם כִּי־אֲנִי› (“and-know Egyptian that”)
# ‹יְהוָה בְּהִכָּבְדִי בְּפַרְעֹה› (“YHWH in-be-heavy-me/my in-Pharaoh”)
# ‹בְּרִכְבּוֹ וּבְפָרָשָׁיו› (“in-vehicle-him/its and-in-steed-him/its”)
# "[EN-AID] And Egypt shall know that I am the LORD, when I am honored
# through Pharaoh, through his chariots and through his horsemen."
m.step("Exod.14.18")
# ‹וְיָדְעוּ מִצְרַיִם כִּי־אֲנִי› (“and-know Egyptian that”)
# ‹יְהוָה› (“YHWH”)
# — fact holds: and-know-Egyptian-2
m.fact("ve_yadu_mitzrayim_2")

# -------------------------- Exod.14.19 · THE_ANGEL_MOVES_BEHIND ------------
# ‹וַיִּסַּע מַלְאַךְ הָאֱלֹהִים› (“and-journey messenger the-God”)
# ‹הַהֹלֵךְ לִפְנֵי מַחֲנֵה› (“the-walk/go to-face camp”)
# ‹יִשְׂרָאֵל וַיֵּלֶךְ מֵאַחֲרֵיהֶם› (“Israel and-go from-after-
# them/their”)
# ‹וַיִּסַּע עַמּוּד הֶעָנָן› (“and-journey column the-cloud”)
# ‹מִפְּנֵיהֶם וַיַּעֲמֹד מֵאַחֲרֵיהֶם› (“from-face-them/their and-stand
# from-after-them/their”)
# "[EN-AID] And the angel of God, going before the camp of Israel, moved and
# went behind them; and the pillar of cloud moved from before them, and
# stood behind them."
m.step("Exod.14.19")
# ‹וַיִּסַּע מַלְאַךְ הָאֱלֹהִים› (“and-journey messenger the-God”)
# ‹הַהֹלֵךְ לִפְנֵי מַחֲנֵה› (“the-walk/go to-face camp”)
# ‹יִשְׂרָאֵל› (“Israel”)
# — fact holds: and-stand-from-acharehem
m.fact("va_yaamod_me_acharehem")

# -------------------------- Exod.14.20 · THE_NIGHT_OF_TWO_CAMPS ------------
# ‹וַיָּבֹא בֵּין מַחֲנֵה› (“and-come/bring between camp”)
# ‹מִצְרַיִם וּבֵין מַחֲנֵה› (“Egypt and-between camp”)
# ‹יִשְׂרָאֵל וַיְהִי הֶעָנָן› (“Israel and-be the-cloud”)
# ‹וְהַחֹשֶׁךְ וַיָּאֶר אֶת־הַלָּיְלָה› (“and-the-darkness and-give-light
# obj-marker the-night”)
# ‹וְלֹא־קָרַב זֶה אֶל־זֶה› (“and-not bring-near this to this”)
# ‹כָּל־הַלָּיְלָה› (“all the-night”)
# "[EN-AID] And it came between the camp of Egypt and the camp of Israel;
# and there was the cloud and the darkness, and it lit the night; and the
# one came not near the other all the night."
m.step("Exod.14.20")
# ‹וְלֹא־קָרַב זֶה אֶל־זֶה› (“and-not bring-near this to this”)
# — fact holds: and-is-it-not-bring-near-this-to-this
m.fact("ve_lo_qarav_ze_el_ze")

# -------------------------- Exod.14.21 · THE_SEA_SPLITS --------------------
# ‹וַיֵּט מֹשֶׁה אֶת־יָדוֹ› (“and-stretch Moses obj-marker hand-him/its”)
# ‹עַל־הַיָּם וַיּוֹלֶךְ יְהוָה› (“over the-seas and-go YHWH”)
# ‹אֶת־הַיָּם בְּרוּחַ קָדִים› (“obj-marker the-seas in-spirit east-wind”)
# ‹עַזָּה כָּל־הַלַּיְלָה וַיָּשֶׂם› (“strong all the-night and-put/set”)
# ‹אֶת־הַיָּם לֶחָרָבָה וַיִּבָּקְעוּ› (“obj-marker the-seas to-desert and-
# cleave”)
# ‹הַמָּיִם› (“the-waters”)
# "[EN-AID] And Moses stretched out his hand over the sea; and the LORD led
# the sea with a strong east wind all the night, and made the sea into dry
# land — and the waters were split."
m.step("Exod.14.21")
# ‹וַיֵּט מֹשֶׁה אֶת־יָדוֹ› (“and-stretch Moses obj-marker hand-him/its”)
# ‹עַל־הַיָּם› (“over the-seas”)
# — demand settled (popped from the queue): neteh-yadkha-and-veqaehu
m.result("neteh_yadkha_u_veqaehu", tmark="t1")
# ‹וַיּוֹלֶךְ יְהוָה אֶת־הַיָּם› (“and-go YHWH obj-marker the-seas”)
# ‹בְּרוּחַ קָדִים עַזָּה› (“in-spirit east-wind strong”)
# — event: qriat-seas-suf — agent the-LORD
m.event("qriat_yam_suf", agent="YHWH")

# -------------------------- Exod.14.22 · WALL_ON_RIGHT_AND_LEFT ------------
# ‹וַיָּבֹאוּ בְנֵי־יִשְׂרָאֵל בְּתוֹךְ› (“and-come/bring son Israel in-
# midst”)
# ‹הַיָּם בַּיַּבָּשָׁה וְהַמַּיִם› (“the-seas in-dry-land and-the-waters”)
# ‹לָהֶם חֹמָה מִימִינָם› (“to-them/their wall-of-protection from-right-
# hand-them/their”)
# ‹וּמִשְּׂמֹאלָם› (“and-from-dark-them/their”)
# "[EN-AID] And the sons of Israel came into the midst of the sea on the dry
# ground; and the waters were for them a wall on their right and on their
# left."
m.step("Exod.14.22")
# ‹לָהֶם חֹמָה מִימִינָם› (“to-them/their wall-of-protection from-right-
# hand-them/their”)
# ‹וּמִשְּׂמֹאלָם› (“and-from-dark-them/their”)
# — fact holds: and-the-waters-to-them-wall-of-protection
m.fact("ve_ha_mayim_lahem_choma")

# -------------------------- Exod.14.23 · EGYPT_COMES_IN_AFTER --------------
# ‹וַיִּרְדְּפוּ מִצְרַיִם וַיָּבֹאוּ› (“and-run-after-gone-by) Egyptian
# and-come/bring”)
# ‹אַחֲרֵיהֶם כֹּל סוּס› (“after-them/their all horse”)
# ‹פַּרְעֹה רִכְבּוֹ וּפָרָשָׁיו› (“Pharaoh vehicle-him/its and-steed-
# him/its”)
# ‹אֶל־תּוֹךְ הַיָּם› (“to midst the-seas”)
# "[EN-AID] And Egypt pursued, and came in after them — every horse of
# Pharaoh, his chariots and his horsemen — into the midst of the sea."
m.step("Exod.14.23")
# ‹וַיִּרְדְּפוּ מִצְרַיִם וַיָּבֹאוּ› (“and-run-after-gone-by) Egyptian
# and-come/bring”)
# ‹אַחֲרֵיהֶם כֹּל› (“after-them/their all”)
# — fact holds: and-come/bring-acharehem-to-midst-the-seas
m.fact("va_yavou_acharehem_el_tokh_ha_yam")

# -------------------------- Exod.14.24 · THE_MORNING_WATCH -----------------
# ‹וַיְהִי בְּאַשְׁמֹרֶת הַבֹּקֶר› (“and-be in-night-watch the-morning”)
# ‹וַיַּשְׁקֵף יְהוָה אֶל־מַחֲנֵה› (“and-lean-out YHWH to camp”)
# ‹מִצְרַיִם בְּעַמּוּד אֵשׁ› (“Egyptian in-column fire”)
# ‹וְעָנָן וַיָּהָם אֵת› (“and-cloud and-put-in-commotion obj-marker”)
# ‹מַחֲנֵה מִצְרָיִם› (“camp Egyptian”)
# "[EN-AID] And it was in the morning watch: the LORD looked down upon the
# camp of Egypt in a pillar of fire and cloud, and routed the camp of
# Egypt."
m.step("Exod.14.24")
# ‹אֶל־מַחֲנֵה מִצְרַיִם בְּעַמּוּד› (“to camp Egyptian in-column”)
# ‹אֵשׁ וְעָנָן וַיָּהָם› (“fire and-cloud and-put-in-commotion”)
# — fact holds: and-yahom-obj-marker-camp-Egyptian
m.fact("va_yahom_et_machane_mitzrayim")

# -------------------------- Exod.14.25 · LET_ME_FLEE -----------------------
# ‹וַיָּסַר אֵת אֹפַן› (“and-turn-aside obj-marker wheel”)
# ‹מַרְכְּבֹתָיו וַיְנַהֲגֵהוּ בִּכְבֵדֻת› (“chariot-him/its and-drive-
# forth-him/its in-difficulty”)
# ‹וַיֹּאמֶר מִצְרַיִם אָנוּסָה› (“and-say Egypt flit”)
# ‹מִפְּנֵי יִשְׂרָאֵל כִּי› (“from-face Israel that”)
# ‹יְהוָה נִלְחָם לָהֶם› (“YHWH feed-on to-them/their”)
# ‹בְּמִצְרָיִם› (“in-Egypt”)
# "[EN-AID] And He removed the wheel of his chariots, and drove them with
# heaviness; and Egypt said: Let me flee from before Israel — for the LORD
# fights for them against Egypt."
m.step("Exod.14.25")
# ‹וַיְנַהֲגֵהוּ בִּכְבֵדֻת וַיֹּאמֶר› (“and-drive-forth-him/its in-
# difficulty and-say”)
# ‹מִצְרַיִם› (“Egypt”)
# — fact holds: flit-mipne-Israel
m.fact("anusa_mipne_yisrael")

# -------------------------- Exod.14.26 · STRETCH_BACK_YOUR_HAND ------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹נְטֵה אֶת־יָדְךָ עַל־הַיָּם› (“stretch obj-marker hand-you/your over the-
# seas”)
# ‹וְיָשֻׁבוּ הַמַּיִם עַל־מִצְרַיִם› (“and-return the-waters over Egypt”)
# ‹עַל־רִכְבּוֹ וְעַל־פָּרָשָׁיו› (“over vehicle-him/its and-over steed-
# him/its”)
# "[EN-AID] And the LORD said to Moses: Stretch out your hand over the sea,
# and the waters shall return upon Egypt, upon his chariots and upon his
# horsemen."
m.step("Exod.14.26")
# ‹נְטֵה אֶת־יָדְךָ עַל־הַיָּם› (“stretch obj-marker hand-you/your over the-
# seas”)
# — the-LORD speaks a demand — LET: neteh-and-return-the-waters
m.declare("YHWH", "LET",
          "neteh_ve_yashuvu_ha_mayim")

# -------------------------- Exod.14.27 · BACK_TO_ITS_CONDITIONS ------------
# ‹וַיֵּט מֹשֶׁה אֶת־יָדוֹ› (“and-stretch Moses obj-marker hand-him/its”)
# ‹עַל־הַיָּם וַיָּשָׁב הַיָּם› (“over the-seas and-return the-seas”)
# ‹לִפְנוֹת בֹּקֶר לְאֵיתָנוֹ› (“to-turn morning to-permanence-him/its”)
# ‹וּמִצְרַיִם נָסִים לִקְרָאתוֹ› (“and-Egypt flit to-encountering-him/its”)
# ‹וַיְנַעֵר יְהוָה אֶת־מִצְרַיִם› (“and-tumble-about YHWH obj-marker
# Egypt”)
# ‹בְּתוֹךְ הַיָּם› (“in-midst the-seas”)
# "[EN-AID] And Moses stretched out his hand over the sea, and the sea
# returned, at the turn of morning, to its strength — and Egypt fleeing to
# meet it; and the LORD shook Egypt into the midst of the sea."
m.step("Exod.14.27")
# ‹עַל־הַיָּם וַיָּשָׁב הַיָּם› (“over the-seas and-return the-seas”)
# ‹לִפְנוֹת בֹּקֶר› (“to-turn morning”)
# — demand settled (popped from the queue): neteh-and-return-the-waters
m.result("neteh_ve_yashuvu_ha_mayim", tmark="t1")

# -------------------------- Exod.14.28 · NOT_ONE_OF_THEM_REMAINED ----------
# ‹וַיָּשֻׁבוּ הַמַּיִם וַיְכַסּוּ› (“and-return the-waters and-plump”)
# ‹אֶת־הָרֶכֶב וְאֶת־הַפָּרָשִׁים לְכֹל› (“obj-marker the-vehicle and-obj-
# marker the-steed to-all”)
# ‹חֵיל פַּרְעֹה הַבָּאִים› (“force Pharaoh the-come/bring”)
# ‹אַחֲרֵיהֶם בַּיָּם לֹא־נִשְׁאַר› (“after-them/their in-seas not swell-
# up”)
# ‹בָּהֶם עַד־אֶחָד› (“in-them/their until one”)
# "[EN-AID] And the waters returned, and covered the chariots and the
# horsemen, of all the host of Pharaoh coming after them into the sea; there
# remained not among them so much as one."
m.step("Exod.14.28")
# ‹לֹא־נִשְׁאַר בָּהֶם עַד־אֶחָד› (“not swell-up in-them/their until one”)
# — fact holds: is-it-not-swell-up-bahem-until-one
m.fact("lo_nishar_bahem_ad_echad")

# -------------------------- Exod.14.29 · THE_WALKED_ON_DRY -----------------
# ‹וּבְנֵי יִשְׂרָאֵל הָלְכוּ› (“and-son Israel walk/go”)
# ‹בַיַּבָּשָׁה בְּתוֹךְ הַיָּם› (“in-dry-land in-midst the-seas”)
# ‹וְהַמַּיִם לָהֶם חֹמָה› (“and-the-waters to-them/their wall-of-
# protection”)
# ‹מִימִינָם וּמִשְּׂמֹאלָם› (“from-right-hand-them/their and-from-dark-
# them/their”)
# "[EN-AID] And the sons of Israel walked on the dry ground in the midst of
# the sea, and the waters were for them a wall on their right and on their
# left."
m.step("Exod.14.29")
# ‹הַיָּם וְהַמַּיִם לָהֶם› (“the-seas and-the-waters to-them/their”)
# ‹חֹמָה מִימִינָם וּמִשְּׂמֹאלָם› (“wall-of-protection from-right-hand-
# them/their and-from-dark-them/their”)
# — fact holds: walk/go-and-dry-land
m.fact("halkhu_va_yabasha")

# -------------------------- Exod.14.30 · THE_SALVATION ---------------------
# ‹וַיּוֹשַׁע יְהוָה בַּיּוֹם› (“and-be-open YHWH in-day”)
# ‹הַהוּא אֶת־יִשְׂרָאֵל מִיַּד› (“that obj-marker Israel from-hand”)
# ‹מִצְרָיִם וַיַּרְא יִשְׂרָאֵל› (“Egypt and-see Israel”)
# ‹אֶת־מִצְרַיִם מֵת עַל־שְׂפַת› (“obj-marker Egypt die over lip”)
# ‹הַיָּם› (“the-seas”)
# "[EN-AID] And the LORD saved Israel in that day from the hand of Egypt;
# and Israel saw Egypt dead on the shore of the sea."
m.step("Exod.14.30")
# ‹וַיּוֹשַׁע יְהוָה בַּיּוֹם› (“and-be-open YHWH in-day”)
# ‹הַהוּא אֶת־יִשְׂרָאֵל› (“that obj-marker Israel”)
# — event: something-saved-the-LORD — agent the-LORD
m.event("yeshuat_YHWH", agent="YHWH")

# -------------------------- Exod.14.31 · AND_THEY_BELIEVED -----------------
# ‹וַיַּרְא יִשְׂרָאֵל אֶת־הַיָּד› (“and-see Israel obj-marker the-hand”)
# ‹הַגְּדֹלָה אֲשֶׁר עָשָׂה› (“the-great which make”)
# ‹יְהוָה בְּמִצְרַיִם וַיִּירְאוּ› (“YHWH in-Egypt and-fear”)
# ‹הָעָם אֶת־יְהוָה וַיַּאֲמִינוּ› (“the-people obj-marker YHWH and-build-
# up”)
# ‹בַּיהוָה וּבְמֹשֶׁה עַבְדּוֹ› (“in-YHWH and-in-Moses servant-him/its”)
# "[EN-AID] And Israel saw the great hand which the LORD had done against
# Egypt, and the people feared the LORD; and they believed in the LORD and
# in Moses His servant."
m.step("Exod.14.31")
# ‹יְהוָה וַיַּאֲמִינוּ בַּיהוָה› (“YHWH and-build-up in-YHWH”)
# — fact holds: and-build-up-in-the-the-LORD-and-and-Moses
m.fact("va_yaaminu_ba_YHWH_u_ve_moshe")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yedaber_14', 'nevukhim_hem_ba_aretz', 'va_yehafekh_levav_paro', 'va_yesor_et_rikhbo', 'shesh_meot_rekhev_bachur', 'yotzim_be_yad_rama', 'va_yasigu_otam_chonim', 'va_yitzaqu_el_YHWH', 'ha_mibli_en_qevarim', 'chadal_mimenu_ve_naavda', 'reu_et_yeshuat_YHWH', 'YHWH_yilachem_lakhem', 'daber_ve_yisau', 'va_ani_hineni_mechazeq', 've_yadu_mitzrayim_2', 'va_yaamod_me_acharehem', 've_lo_qarav_ze_el_ze', 've_ha_mayim_lahem_choma', 'va_yavou_acharehem_el_tokh_ha_yam', 'va_yahom_et_machane_mitzrayim', 'anusa_mipne_yisrael', 'lo_nishar_bahem_ad_echad', 'halkhu_va_yabasha', 'va_yaaminu_ba_YHWH_u_ve_moshe'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 8
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
