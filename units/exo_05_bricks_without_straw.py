#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_05_bricks_without_straw — 5:1-23
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_05_bricks_without_straw.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Bricks without straw (5:1-23)"""
from machine import Machine

m = Machine("exo_05_bricks_without_straw")

# -------------------------- Exod.5.1 · SEND_MY_PEOPLE ----------------------
# וְאַחַר בָּאוּ מֹשֶׁה וְאַהֲרֹן וַיֹּאמְרוּ אֶל־פַּרְעֹה כֹּה־אָמַר יְהוָה
# אֱלֹהֵי יִשְׂרָאֵל שַׁלַּח אֶת־עַמִּי וְיָחֹגּוּ לִי בַּמִּדְבָּר
# "[EN-AID] And afterward Moses and Aaron came, and said to Pharaoh: Thus
# says the LORD, the God of Israel: Send My people, that they may feast to
# Me in the wilderness."
m.step("Exod.5.1")
# ‹שַׁלַּח אֶת־עַמִּי וְיָחֹגּוּ לִי בַּמִּדְבָּר› (“send obj-marker people-
# me/my and-move-in-acircle to-me/my in-pasture”) — Moses-and-Aaron speaks a
# demand — LET: send-obj-marker-ami-and-move-in-acircle-to-me
m.declare("moshe_ve_aharon", "LET",
          "shalach_et_ami_ve_yachogu_li")

# -------------------------- Exod.5.2 · WHO_IS_YHWH -------------------------
# וַיֹּאמֶר פַּרְעֹה מִי יְהוָה אֲשֶׁר אֶשְׁמַע בְּקֹלוֹ לְשַׁלַּח
# אֶת־יִשְׂרָאֵל לֹא יָדַעְתִּי אֶת־יְהוָה וְגַם אֶת־יִשְׂרָאֵל לֹא
# אֲשַׁלֵּחַ
# "[EN-AID] And Pharaoh said: Who is the LORD, that I should hear His voice
# to send Israel? I know not the LORD, and Israel also I will not send."
m.step("Exod.5.2")
# ‹לֹא יָדַעְתִּי אֶת־יְהוָה› (“not know obj-marker YHWH”) — fact holds:
# not-know-obj-marker-the-LORD
m.fact("lo_yadati_et_YHWH")

# -------------------------- Exod.5.3 · THE_SCRIPT_PERFORMED ----------------
# וַיֹּאמְרוּ אֱלֹהֵי הָעִבְרִים נִקְרָא עָלֵינוּ נֵלֲכָה נָּא דֶּרֶךְ
# שְׁלֹשֶׁת יָמִים בַּמִּדְבָּר וְנִזְבְּחָה לַיהוָה אֱלֹהֵינוּ
# פֶּן־יִפְגָּעֵנוּ בַּדֶּבֶר אוֹ בֶחָרֶב
# "[EN-AID] And they said: The God of the Hebrews has happened upon us; let
# us go, pray, a journey of three days into the wilderness, and sacrifice to
# the LORD our God — lest He strike us with the pestilence, or with the
# sword."
m.step("Exod.5.3")
# ‹נֵלֲכָה נָּא דֶּרֶךְ שְׁלֹשֶׁת יָמִים בַּמִּדְבָּר וְנִזְבְּחָה לַיהוָה
# אֱלֹהֵינוּ› (“go please way/road three day in-pasture and-slaughter-an-
# animal to-YHWH God-us/our”) — fact holds: God-the-Hebrew-encounter-alenu
m.fact("elohe_ha_ivrim_niqra_alenu")

# -------------------------- Exod.5.4 · TO_YOUR_BURDENS ---------------------
# וַיֹּאמֶר אֲלֵהֶם מֶלֶךְ מִצְרַיִם לָמָּה מֹשֶׁה וְאַהֲרֹן תַּפְרִיעוּ
# אֶת־הָעָם מִמַּעֲשָׂיו לְכוּ לְסִבְלֹתֵיכֶם
# "[EN-AID] And the king of Egypt said to them: Why, Moses and Aaron, do you
# disturb the people from its works? Go to your burdens."
m.step("Exod.5.4")
# ‹לְכוּ לְסִבְלֹתֵיכֶם› (“go to-porterage-you/your(pl)”) — fact holds: go-
# to-sivlotekhem
m.fact("lekhu_le_sivlotekhem")

# -------------------------- Exod.5.5 · MANY_NOW ----------------------------
# וַיֹּאמֶר פַּרְעֹה הֵן־רַבִּים עַתָּה עַם הָאָרֶץ וְהִשְׁבַּתֶּם אֹתָם
# מִסִּבְלֹתָם
# "[EN-AID] And Pharaoh said: Behold, the people of the land are now many,
# and you would make them rest from their burdens."
m.step("Exod.5.5")
# ‹וְהִשְׁבַּתֶּם אֹתָם מִסִּבְלֹתָם› (“and-cease obj-marker-them/their
# from-porterage-them/their”) — fact holds: and-cease-otam-who?-sivlotam
m.fact("ve_hishbatem_otam_mi_sivlotam")

# -------------------------- Exod.5.6 · PHARAOH_COMMANDS_THE_TASKMASTERS ----
# וַיְצַו פַּרְעֹה בַּיּוֹם הַהוּא אֶת־הַנֹּגְשִׂים בָּעָם וְאֶת־שֹׁטְרָיו
# לֵאמֹר
# "[EN-AID] And Pharaoh commanded, on that day, the taskmasters over the
# people and its officers, saying:"
m.step("Exod.5.6")
# ‹וַיְצַו פַּרְעֹה בַּיּוֹם הַהוּא› (“and-command Pharaoh in-day that”) —
# fact holds: and-command-Pharaoh-in-the-day-the-that
m.fact("va_yetzav_paro_ba_yom_ha_hu")

# -------------------------- Exod.5.7 · NO_MORE_STRAW -----------------------
# לֹא תֹאסִפוּן לָתֵת תֶּבֶן לָעָם לִלְבֹּן הַלְּבֵנִים כִּתְמוֹל שִׁלְשֹׁם
# הֵם יֵלְכוּ וְקֹשְׁשׁוּ לָהֶם תֶּבֶן
# "[EN-AID] You shall not continue to give straw to the people to brick the
# bricks, as yesterday and the day before; they shall go and gather straw
# for themselves."
m.step("Exod.5.7")
# ‹לֹא תֹאסִפוּן לָתֵת תֶּבֶן לָעָם לִלְבֹּן הַלְּבֵנִים› (“not add-ward to-
# set material to-people to-be-white the-brick”) — Pharaoh speaks a demand —
# LET: not-tosifun-latet-material
m.declare("paro", "LET",
          "lo_tosifun_latet_teven")

# -------------------------- Exod.5.8 · THE_QUOTA_STANDS --------------------
# וְאֶת־מַתְכֹּנֶת הַלְּבֵנִים אֲשֶׁר הֵם עֹשִׂים תְּמוֹל שִׁלְשֹׁם
# תָּשִׂימוּ עֲלֵיהֶם לֹא תִגְרְעוּ מִמֶּנּוּ כִּי־נִרְפִּים הֵם עַל־כֵּן
# הֵם צֹעֲקִים לֵאמֹר נֵלְכָה נִזְבְּחָה לֵאלֹהֵינוּ
# "[EN-AID] And the count of the bricks which they made yesterday and the
# day before you shall set upon them — you shall not diminish from it; for
# they are idle — therefore they cry, saying: Let us go, sacrifice to our
# God."
m.step("Exod.5.8")
# ‹לֹא תִגְרְעוּ מִמֶּנּוּ› (“not scrape-off from-us/our”) — fact holds:
# not-tigreu-from-it
m.fact("lo_tigreu_mimenu")

# -------------------------- Exod.5.9 · HEAVY_ON_THE_MEN --------------------
# תִּכְבַּד הָעֲבֹדָה עַל־הָאֲנָשִׁים וְיַעֲשׂוּ־בָהּ וְאַל־יִשְׁעוּ
# בְּדִבְרֵי־שָׁקֶר
# "[EN-AID] Let the service be heavy on the men, and let them do it; and let
# them not turn to false words."
m.step("Exod.5.9")
# ‹תִּכְבַּד הָעֲבֹדָה עַל־הָאֲנָשִׁים› (“be-heavy the-service/work over
# the-man”) — fact holds: be-heavy-the-service/work-over-the-man
m.fact("tikhbad_ha_avoda_al_ha_anashim")

# -------------------------- Exod.5.10 · THE_DECREE_RELAYED -----------------
# וַיֵּצְאוּ נֹגְשֵׂי הָעָם וְשֹׁטְרָיו וַיֹּאמְרוּ אֶל־הָעָם לֵאמֹר כֹּה
# אָמַר פַּרְעֹה אֵינֶנִּי נֹתֵן לָכֶם תֶּבֶן
# "[EN-AID] And the taskmasters of the people went out, and its officers,
# and said to the people, saying: Thus says Pharaoh: I do not give you
# straw."
m.step("Exod.5.10")
# ‹כֹּה אָמַר פַּרְעֹה אֵינֶנִּי נֹתֵן לָכֶם תֶּבֶן› (“like-this say Pharaoh
# there-is-not-me/my set to-you/your(pl) material”) — demand settled (popped
# from the queue): not-tosifun-latet-material
m.result("lo_tosifun_latet_teven", tmark="t1")

# -------------------------- Exod.5.11 · GO_GET_STRAW -----------------------
# אַתֶּם לְכוּ קְחוּ לָכֶם תֶּבֶן מֵאֲשֶׁר תִּמְצָאוּ כִּי אֵין נִגְרָע
# מֵעֲבֹדַתְכֶם דָּבָר
# "[EN-AID] You — go, take straw for yourselves from wherever you find it;
# for nothing is diminished from your service."
m.step("Exod.5.11")
# ‹כִּי אֵין נִגְרָע מֵעֲבֹדַתְכֶם דָּבָר› (“that there-is-not scrape-off
# from-service/work-you/your(pl) word/thing”) — fact holds: that-there-is-
# not-scrape-off-from-avodatkhem-word/thing
m.fact("ki_en_nigra_me_avodatkhem_davar")

# -------------------------- Exod.5.12 · THE_SCATTERING ---------------------
# וַיָּפֶץ הָעָם בְּכָל־אֶרֶץ מִצְרָיִם לְקֹשֵׁשׁ קַשׁ לַתֶּבֶן
# "[EN-AID] And the people scattered in all the land of Egypt, to gather
# stubble for the straw."
m.step("Exod.5.12")
# ‹וַיָּפֶץ הָעָם בְּכָל־אֶרֶץ מִצְרָיִם› (“and-dash-in-pieces the-people
# in-all earth Egypt”) — fact holds: and-dash-in-pieces-the-people-in-all-
# earth-Egypt
m.fact("va_yafetz_ha_am_be_khol_eretz_mitzrayim")

# -------------------------- Exod.5.13 · THE_PRESSING -----------------------
# וְהַנֹּגְשִׂים אָצִים לֵאמֹר כַּלּוּ מַעֲשֵׂיכֶם דְּבַר־יוֹם בְּיוֹמוֹ
# כַּאֲשֶׁר בִּהְיוֹת הַתֶּבֶן
# "[EN-AID] And the taskmasters were pressing, saying: Complete your works,
# the matter of a day in its day, as when the straw was."
m.step("Exod.5.13")
# ‹דְּבַר־יוֹם בְּיוֹמוֹ› (“word/thing day in-day-him/its”) — fact holds:
# word/thing-day-in-yomo
m.fact("devar_yom_be_yomo")

# -------------------------- Exod.5.14 · THE_OFFICERS_BEATEN ----------------
# וַיֻּכּוּ שֹׁטְרֵי בְּנֵי יִשְׂרָאֵל אֲשֶׁר־שָׂמוּ עֲלֵהֶם נֹגְשֵׂי
# פַרְעֹה לֵאמֹר מַדּוּעַ לֹא כִלִּיתֶם חָקְכֶם לִלְבֹּן כִּתְמוֹל שִׁלְשֹׁם
# גַּם־תְּמוֹל גַּם־הַיּוֹם
# "[EN-AID] And the officers of the sons of Israel were beaten, whom
# Pharaoh's taskmasters had set over them, saying: Why have you not
# completed your portion to brick, as yesterday and the day before — both
# yesterday and today?"
m.step("Exod.5.14")
# ‹וַיֻּכּוּ שֹׁטְרֵי בְּנֵי יִשְׂרָאֵל› (“and-strike scribe son Israel”) —
# event: huku — agent drive-Pharaoh
m.event("huku", agent="nogse_faro")

# -------------------------- Exod.5.15 · THE_CRY_TO_PHARAOH -----------------
# וַיָּבֹאוּ שֹׁטְרֵי בְּנֵי יִשְׂרָאֵל וַיִּצְעֲקוּ אֶל־פַּרְעֹה לֵאמֹר
# לָמָּה תַעֲשֶׂה כֹה לַעֲבָדֶיךָ
# "[EN-AID] And the officers of the sons of Israel came and cried to
# Pharaoh, saying: Why do you deal thus with your servants?"
m.step("Exod.5.15")
# ‹וַיִּצְעֲקוּ אֶל־פַּרְעֹה לֵאמֹר› (“and-shriek to Pharaoh to-say”) — fact
# holds: and-shriek-to-Pharaoh
m.fact("va_yitzaqu_el_paro")

# -------------------------- Exod.5.16 · YOUR_OWN_PEOPLE_SIN ----------------
# תֶּבֶן אֵין נִתָּן לַעֲבָדֶיךָ וּלְבֵנִים אֹמְרִים לָנוּ עֲשׂוּ וְהִנֵּה
# עֲבָדֶיךָ מֻכִּים וְחָטָאת עַמֶּךָ
# "[EN-AID] Straw is not given to your servants, and bricks — they say to
# us: Make! And behold, your servants are beaten; and the sin is your
# people's."
m.step("Exod.5.16")
# ‹וְהִנֵּה עֲבָדֶיךָ מֻכִּים› (“and-behold servant-you/your strike”) — fact
# holds: and-behold-avadekha-strike
m.fact("ve_hine_avadekha_mukim")

# -------------------------- Exod.5.17 · IDLE_IDLE --------------------------
# וַיֹּאמֶר נִרְפִּים אַתֶּם נִרְפִּים עַל־כֵּן אַתֶּם אֹמְרִים נֵלְכָה
# נִזְבְּחָה לַיהוָה
# "[EN-AID] And he said: Idle — you are idle! Therefore you say: Let us go,
# sacrifice to the LORD."
m.step("Exod.5.17")
# ‹נִרְפִּים אַתֶּם נִרְפִּים› (“slacken you slacken”) — fact holds:
# slacken-you-slacken
m.fact("nirpim_atem_nirpim")

# -------------------------- Exod.5.18 · GO_SERVE_NO_STRAW ------------------
# וְעַתָּה לְכוּ עִבְדוּ וְתֶבֶן לֹא־יִנָּתֵן לָכֶם וְתֹכֶן לְבֵנִים
# תִּתֵּנּוּ
# "[EN-AID] And now — go, serve; and straw shall not be given you, and the
# count of bricks you shall give."
m.step("Exod.5.18")
# ‹וְתֹכֶן לְבֵנִים תִּתֵּנּוּ› (“and-fixed-quantity brick set”) — fact
# holds: and-fixed-quantity-brick-set
m.fact("ve_tokhen_levenim_titenu")

# -------------------------- Exod.5.19 · THEY_SAW_THEMSELVES_IN_EVIL --------
# וַיִּרְאוּ שֹׁטְרֵי בְנֵי־יִשְׂרָאֵל אֹתָם בְּרָע לֵאמֹר לֹא־תִגְרְעוּ
# מִלִּבְנֵיכֶם דְּבַר־יוֹם בְּיוֹמוֹ
# "[EN-AID] And the officers of the sons of Israel saw themselves in evil,
# saying: You shall not diminish from your bricks, the day's matter in its
# day."
m.step("Exod.5.19")
# ‹וַיִּרְאוּ שֹׁטְרֵי בְנֵי־יִשְׂרָאֵל אֹתָם בְּרָע› (“and-see scribe son
# Israel obj-marker-them/their in-bad”) — fact holds: and-see-otam-in-bad
m.fact("va_yiru_otam_be_ra")

# -------------------------- Exod.5.20 · THE_CORRIDOR_MEETING ---------------
# וַיִּפְגְּעוּ אֶת־מֹשֶׁה וְאֶת־אַהֲרֹן נִצָּבִים לִקְרָאתָם בְּצֵאתָם
# מֵאֵת פַּרְעֹה
# "[EN-AID] And they met Moses and Aaron, stationed to meet them, as they
# came out from Pharaoh."
m.step("Exod.5.20")
# ‹נִצָּבִים לִקְרָאתָם› (“stand to-encountering-them/their”) — fact holds:
# stand-liqratam
m.fact("nitzavim_liqratam")

# -------------------------- Exod.5.21 · MAY_HE_SEE_AND_JUDGE ---------------
# וַיֹּאמְרוּ אֲלֵהֶם יֵרֶא יְהוָה עֲלֵיכֶם וְיִשְׁפֹּט אֲשֶׁר הִבְאַשְׁתֶּם
# אֶת־רֵיחֵנוּ בְּעֵינֵי פַרְעֹה וּבְעֵינֵי עֲבָדָיו לָתֶת־חֶרֶב בְּיָדָם
# לְהָרְגֵנוּ
# "[EN-AID] And they said to them: May the LORD see upon you, and judge —
# for you have made our savor stink in the eyes of Pharaoh, and in the eyes
# of his servants, to put a sword in their hand to kill us."
m.step("Exod.5.21")
# ‹יֵרֶא יְהוָה עֲלֵיכֶם וְיִשְׁפֹּט› (“see YHWH over-you/your(pl) and-
# judge”) — scribe-son-Israel speaks a demand — LET: see-the-LORD-alekhem-
# and-judge
m.declare("shotre_bene_yisrael", "LET",
          "yere_YHWH_alekhem_ve_yishpot")

# -------------------------- Exod.5.22 · WHY_HAVE_YOU_DEALT_ILL -------------
# וַיָּשָׁב מֹשֶׁה אֶל־יְהוָה וַיֹּאמַר אֲדֹנָי לָמָה הֲרֵעֹתָה לָעָם הַזֶּה
# לָמָּה זֶּה שְׁלַחְתָּנִי
# "[EN-AID] And Moses returned to the LORD, and said: My Lord, why have You
# dealt ill with this people? Why is this that You have sent me?"
m.step("Exod.5.22")
# ‹אֲדֹנָי לָמָה הֲרֵעֹתָה לָעָם הַזֶּה› (“Lord-me/my to-what spoil to-
# people the-this”) — fact holds: lama-spoil-to-people-the-this
m.fact("lama_hareota_la_am_ha_ze")

# -------------------------- Exod.5.23 · YOU_HAVE_NOT_DELIVERED -------------
# וּמֵאָז בָּאתִי אֶל־פַּרְעֹה לְדַבֵּר בִּשְׁמֶךָ הֵרַע לָעָם הַזֶּה
# וְהַצֵּל לֹא־הִצַּלְתָּ אֶת־עַמֶּךָ
# "[EN-AID] And since I came to Pharaoh to speak in Your name, he has dealt
# ill with this people; and deliver — You have not delivered Your people."
m.step("Exod.5.23")
# ‹וְהַצֵּל לֹא־הִצַּלְתָּ אֶת־עַמֶּךָ› (“and-snatch-away not snatch-away
# obj-marker people-you/your”) — fact holds: and-snatch-away-not-snatch-
# away-obj-marker-amekha
m.fact("ve_hatzel_lo_hitzalta_et_amekha")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shalach_et_ami_ve_yachogu_li', 'yere_YHWH_alekhem_ve_yishpot']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_yadati_et_YHWH', 'elohe_ha_ivrim_niqra_alenu', 'lekhu_le_sivlotekhem', 've_hishbatem_otam_mi_sivlotam', 'va_yetzav_paro_ba_yom_ha_hu', 'lo_tigreu_mimenu', 'tikhbad_ha_avoda_al_ha_anashim', 'ki_en_nigra_me_avodatkhem_davar', 'va_yafetz_ha_am_be_khol_eretz_mitzrayim', 'devar_yom_be_yomo', 'va_yitzaqu_el_paro', 've_hine_avadekha_mukim', 'nirpim_atem_nirpim', 've_tokhen_levenim_titenu', 'va_yiru_otam_be_ra', 'nitzavim_liqratam', 'lama_hareota_la_am_ha_ze', 've_hatzel_lo_hitzalta_et_amekha'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
