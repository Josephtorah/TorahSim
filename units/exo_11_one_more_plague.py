#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_11_one_more_plague — 11:1-10
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_11_one_more_plague.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""One plague more (11:1-10)"""
from machine import Machine

m = Machine("exo_11_one_more_plague")

# -------------------------- Exod.11.1 · ONE_PLAGUE_MORE --------------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה עוֹד נֶגַע אֶחָד אָבִיא עַל־פַּרְעֹה
# וְעַל־מִצְרַיִם אַחֲרֵי־כֵן יְשַׁלַּח אֶתְכֶם מִזֶּה כְּשַׁלְּחוֹ כָּלָה
# גָּרֵשׁ יְגָרֵשׁ אֶתְכֶם מִזֶּה
# "[EN-AID] And the LORD said to Moses: One plague more I bring upon Pharaoh
# and upon Egypt; afterwards he will send you from here — when he sends,
# completely, driving he shall drive you out from here."
m.step("Exod.11.1")
# ‹עוֹד נֶגַע אֶחָד אָבִיא עַל־פַּרְעֹה וְעַל־מִצְרַיִם› (“still/again blow
# one come/bring over Pharaoh and-over Egypt”) — fact holds: still/again-
# blow-one-come/bring
m.fact("od_nega_echad_avi")

# -------------------------- Exod.11.2 · ASK_OF_YOUR_NEIGHBOR ---------------
# דַּבֶּר־נָא בְּאָזְנֵי הָעָם וְיִשְׁאֲלוּ אִישׁ מֵאֵת רֵעֵהוּ וְאִשָּׁה
# מֵאֵת רְעוּתָהּ כְּלֵי־כֶסֶף וּכְלֵי זָהָב
# "[EN-AID] Speak, pray, in the ears of the people: let them ask, each man
# of his neighbor and each woman of her neighbor, vessels of silver and
# vessels of gold."
m.step("Exod.11.2")
# ‹דַּבֶּר־נָא בְּאָזְנֵי הָעָם› (“speak please in-broadness.-i.e.-the-ear
# the-people”) — the-LORD speaks a demand — LET: and-inquire-man-vessel-
# silver
m.declare("YHWH", "LET",
          "ve_yishalu_ish_kele_khesef")

# -------------------------- Exod.11.3 · THE_MAN_MOSES ----------------------
# וַיִּתֵּן יְהוָה אֶת־חֵן הָעָם בְּעֵינֵי מִצְרָיִם גַּם הָאִישׁ מֹשֶׁה
# גָּדוֹל מְאֹד בְּאֶרֶץ מִצְרַיִם בְּעֵינֵי עַבְדֵי־פַרְעֹה וּבְעֵינֵי
# הָעָם
# "[EN-AID] And the LORD gave the people favor in the eyes of Egypt; also
# the man Moses was very great in the land of Egypt, in the eyes of
# Pharaoh's servants and in the eyes of the people."
m.step("Exod.11.3")
# ‹וַיִּתֵּן יְהוָה אֶת־חֵן הָעָם בְּעֵינֵי מִצְרָיִם› (“and-set YHWH obj-
# marker graciousness the-people in-eye Egyptian”) — fact holds: and-set-
# graciousness-the-people
m.fact("va_yiten_chen_ha_am")

# -------------------------- Exod.11.4 · ABOUT_MIDNIGHT ---------------------
# וַיֹּאמֶר מֹשֶׁה כֹּה אָמַר יְהוָה כַּחֲצֹת הַלַּיְלָה אֲנִי יוֹצֵא
# בְּתוֹךְ מִצְרָיִם
# "[EN-AID] And Moses said: Thus says the LORD: About midnight I go out in
# the midst of Egypt."
m.step("Exod.11.4")
# ‹כַּחֲצֹת הַלַּיְלָה אֲנִי יוֹצֵא בְּתוֹךְ מִצְרָיִם› (“like-middle the-
# night bring-forth in-midst Egypt”) — fact holds: like-chatzot-ani-bring-
# forth
m.fact("ka_chatzot_ani_yotze")

# -------------------------- Exod.11.5 · EVERY_FIRSTBORN_DIES ---------------
# וּמֵת כָּל־בְּכוֹר בְּאֶרֶץ מִצְרַיִם מִבְּכוֹר פַּרְעֹה הַיֹּשֵׁב
# עַל־כִּסְאוֹ עַד בְּכוֹר הַשִּׁפְחָה אֲשֶׁר אַחַר הָרֵחָיִם וְכֹל בְּכוֹר
# בְּהֵמָה
# "[EN-AID] And every firstborn in the land of Egypt shall die, from the
# firstborn of Pharaoh who sits on his throne to the firstborn of the slave-
# girl who is behind the millstones, and every firstborn of beast."
m.step("Exod.11.5")
# ‹וּמֵת כָּל־בְּכוֹר בְּאֶרֶץ מִצְרַיִם› (“and-die all firstborn in-earth
# Egypt”) — fact holds: and-die-all-firstborn
m.fact("u_met_kol_bekhor")

# -------------------------- Exod.11.6 · A_CRY_LIKE_NO_OTHER ----------------
# וְהָיְתָה צְעָקָה גְדֹלָה בְּכָל־אֶרֶץ מִצְרָיִם אֲשֶׁר כָּמֹהוּ לֹא
# נִהְיָתָה וְכָמֹהוּ לֹא תֹסִף
# "[EN-AID] And there shall be a great cry in all the land of Egypt, such as
# like it never was and like it shall never be again."
m.step("Exod.11.6")
# ‹וְהָיְתָה צְעָקָה גְדֹלָה בְּכָל־אֶרֶץ מִצְרָיִם› (“and-be shriek great
# in-all earth Egypt”) — fact holds: shriek-great-kamohu-not-be
m.fact("tzeaqa_gedola_kamohu_lo_nihyata")

# -------------------------- Exod.11.7 · NOT_A_DOG_SHALL_SHARPEN ------------
# וּלְכֹל בְּנֵי יִשְׂרָאֵל לֹא יֶחֱרַץ־כֶּלֶב לְשֹׁנוֹ לְמֵאִישׁ
# וְעַד־בְּהֵמָה לְמַעַן תֵּדְעוּן אֲשֶׁר יַפְלֶה יְהוָה בֵּין מִצְרַיִם
# וּבֵין יִשְׂרָאֵל
# "[EN-AID] And against all the sons of Israel not a dog shall sharpen its
# tongue, against man or beast — in order that you may know that the LORD
# distinguishes between Egypt and Israel."
m.step("Exod.11.7")
# ‹וּלְכֹל בְּנֵי יִשְׂרָאֵל לֹא יֶחֱרַץ־כֶּלֶב לְשֹׁנוֹ› (“and-to-all son
# Israel not point-sharply dog tongue-him/its”) — fact holds: not-point-
# sharply-dog-leshono
m.fact("lo_yecheratz_kelev_leshono")

# -------------------------- Exod.11.8 · YOUR_SERVANTS_WILL_BOW -------------
# וְיָרְדוּ כָל־עֲבָדֶיךָ אֵלֶּה אֵלַי וְהִשְׁתַּחֲוּוּ־לִי לֵאמֹר צֵא
# אַתָּה וְכָל־הָעָם אֲשֶׁר־בְּרַגְלֶיךָ וְאַחֲרֵי־כֵן אֵצֵא וַיֵּצֵא
# מֵעִם־פַּרְעֹה בָּחֳרִי־אָף
# "[EN-AID] And all these your servants shall come down to me and bow to me,
# saying: Go out, you and all the people at your feet — and after that I
# will go out. And he went out from Pharaoh in hot anger."
m.step("Exod.11.8")
# ‹וְיָרְדוּ כָל־עֲבָדֶיךָ אֵלֶּה אֵלַי וְהִשְׁתַּחֲוּוּ־לִי לֵאמֹר› (“and-
# go-down all servant-you/your these to-me/my and-afflict to-me/my to-say”)
# — fact holds: and-go-down-avadekha-these
m.fact("ve_yardu_avadekha_ele")

# -------------------------- Exod.11.9 · HE_WILL_NOT_LISTEN -----------------
# וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה לֹא־יִשְׁמַע אֲלֵיכֶם פַּרְעֹה לְמַעַן רְבוֹת
# מוֹפְתַי בְּאֶרֶץ מִצְרָיִם
# "[EN-AID] And the LORD said to Moses: Pharaoh will not listen to you — in
# order that My wonders may be multiplied in the land of Egypt."
m.step("Exod.11.9")
# ‹לֹא־יִשְׁמַע אֲלֵיכֶם פַּרְעֹה› (“not hear to-you/your(pl) Pharaoh”) —
# fact holds: not-hear-alekhem-Pharaoh-2
m.fact("lo_yishma_alekhem_paro_2")

# -------------------------- Exod.11.10 · THE_CYCLE_COLOPHON ----------------
# וּמֹשֶׁה וְאַהֲרֹן עָשׂוּ אֶת־כָּל־הַמֹּפְתִים הָאֵלֶּה לִפְנֵי פַרְעֹה
# וַיְחַזֵּק יְהוָה אֶת־לֵב פַּרְעֹה וְלֹא־שִׁלַּח אֶת־בְּנֵי־יִשְׂרָאֵל
# מֵאַרְצוֹ
# "[EN-AID] And Moses and Aaron did all these wonders before Pharaoh; and
# the LORD strengthened Pharaoh's heart, and he did not send the sons of
# Israel out of his land."
m.step("Exod.11.10")
# ‹וּמֹשֶׁה וְאַהֲרֹן עָשׂוּ אֶת־כָּל־הַמֹּפְתִים הָאֵלֶּה› (“and-Moses and-
# Aaron make obj-marker all the-miracle the-these”) — fact holds: and-Moses-
# and-Aaron-make
m.fact("u_moshe_ve_aharon_asu")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['ve_yishalu_ish_kele_khesef']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['od_nega_echad_avi', 'va_yiten_chen_ha_am', 'ka_chatzot_ani_yotze', 'u_met_kol_bekhor', 'tzeaqa_gedola_kamohu_lo_nihyata', 'lo_yecheratz_kelev_leshono', 've_yardu_avadekha_ele', 'lo_yishma_alekhem_paro_2', 'u_moshe_ve_aharon_asu'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 1
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
