#!/usr/bin/env python3
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
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹עוֹד נֶגַע אֶחָד› (“still/again blow one”)
# ‹אָבִיא עַל־פַּרְעֹה וְעַל־מִצְרַיִם› (“come/bring over Pharaoh and-over
# Egypt”)
# ‹אַחֲרֵי־כֵן יְשַׁלַּח אֶתְכֶם› (“after so send obj-marker-you/your(pl)”)
# ‹מִזֶּה כְּשַׁלְּחוֹ כָּלָה› (“from-this like-send-him/its completion”)
# ‹גָּרֵשׁ יְגָרֵשׁ אֶתְכֶם› (“drive-out-from-a-possession drive-out-from-a-
# possession obj-marker-you/your(pl)”)
# ‹מִזֶּה› (“from-this”)
# "[EN-AID] And the LORD said to Moses: One plague more I bring upon Pharaoh
# and upon Egypt; afterwards he will send you from here — when he sends,
# completely, driving he shall drive you out from here."
m.step("Exod.11.1")
# ‹עוֹד נֶגַע אֶחָד› (“still/again blow one”)
# ‹אָבִיא עַל־פַּרְעֹה וְעַל־מִצְרַיִם› (“come/bring over Pharaoh and-over
# Egypt”)
# — fact holds: still/again-blow-one-come/bring
m.fact("od_nega_echad_avi")
# witness-tier presupposed read: plague_census on one_more_plague — read,
# not installed
m.witness_read("one_more_plague", "plague_census",
                cites=["Pirkei Avot 5:4"])

# -------------------------- Exod.11.2 · ASK_OF_YOUR_NEIGHBOR ---------------
# ‹דַּבֶּר־נָא בְּאָזְנֵי הָעָם› (“speak please in-broadness.-i.e.-the-ear
# the-people”)
# ‹וְיִשְׁאֲלוּ אִישׁ מֵאֵת› (“and-inquire man from-with”)
# ‹רֵעֵהוּ וְאִשָּׁה מֵאֵת› (“associate-him/its and-woman from-with”)
# ‹רְעוּתָהּ כְּלֵי־כֶסֶף וּכְלֵי› (“female-associate-her/its vessel silver
# and-vessel”)
# ‹זָהָב› (“gold”)
# "[EN-AID] Speak, pray, in the ears of the people: let them ask, each man
# of his neighbor and each woman of her neighbor, vessels of silver and
# vessels of gold."
m.step("Exod.11.2")
# ‹דַּבֶּר־נָא בְּאָזְנֵי הָעָם› (“speak please in-broadness.-i.e.-the-ear
# the-people”)
# — the-LORD speaks a demand — LET: and-inquire-man-vessel-silver
m.declare("YHWH", "LET",
          "ve_yishalu_ish_kele_khesef")

# -------------------------- Exod.11.3 · THE_MAN_MOSES ----------------------
# ‹וַיִּתֵּן יְהוָה אֶת־חֵן› (“and-set YHWH obj-marker graciousness”)
# ‹הָעָם בְּעֵינֵי מִצְרָיִם› (“the-people in-eye Egyptian”)
# ‹גַּם הָאִישׁ מֹשֶׁה› (“also the-man Moses”)
# ‹גָּדוֹל מְאֹד בְּאֶרֶץ› (“great very in-earth”)
# ‹מִצְרַיִם בְּעֵינֵי עַבְדֵי־פַרְעֹה› (“Egypt in-eye servant Pharaoh”)
# ‹וּבְעֵינֵי הָעָם› (“and-in-eye the-people”)
# "[EN-AID] And the LORD gave the people favor in the eyes of Egypt; also
# the man Moses was very great in the land of Egypt, in the eyes of
# Pharaoh's servants and in the eyes of the people."
m.step("Exod.11.3")
# ‹וַיִּתֵּן יְהוָה אֶת־חֵן› (“and-set YHWH obj-marker graciousness”)
# ‹הָעָם בְּעֵינֵי מִצְרָיִם› (“the-people in-eye Egyptian”)
# — fact holds: and-set-graciousness-the-people
m.fact("va_yiten_chen_ha_am")

# -------------------------- Exod.11.4 · ABOUT_MIDNIGHT ---------------------
# ‹וַיֹּאמֶר מֹשֶׁה כֹּה› (“and-say Moses like-this”)
# ‹אָמַר יְהוָה כַּחֲצֹת› (“say YHWH like-middle”)
# ‹הַלַּיְלָה אֲנִי יוֹצֵא› (“the-night bring-forth”)
# ‹בְּתוֹךְ מִצְרָיִם› (“in-midst Egypt”)
# "[EN-AID] And Moses said: Thus says the LORD: About midnight I go out in
# the midst of Egypt."
m.step("Exod.11.4")
# ‹כַּחֲצֹת הַלַּיְלָה אֲנִי› (“like-middle the-night”)
# ‹יוֹצֵא בְּתוֹךְ מִצְרָיִם› (“bring-forth in-midst Egypt”)
# — fact holds: like-chatzot-ani-bring-forth
m.fact("ka_chatzot_ani_yotze")

# -------------------------- Exod.11.5 · EVERY_FIRSTBORN_DIES ---------------
# ‹וּמֵת כָּל־בְּכוֹר בְּאֶרֶץ› (“and-die all firstborn in-earth”)
# ‹מִצְרַיִם מִבְּכוֹר פַּרְעֹה› (“Egypt from-firstborn Pharaoh”)
# ‹הַיֹּשֵׁב עַל־כִּסְאוֹ עַד› (“the-dwell/sit over covered-him/its until”)
# ‹בְּכוֹר הַשִּׁפְחָה אֲשֶׁר› (“firstborn the-female-slave which”)
# ‹אַחַר הָרֵחָיִם וְכֹל› (“after the-mill-stone and-all”)
# ‹בְּכוֹר בְּהֵמָה› (“firstborn livestock”)
# "[EN-AID] And every firstborn in the land of Egypt shall die, from the
# firstborn of Pharaoh who sits on his throne to the firstborn of the slave-
# girl who is behind the millstones, and every firstborn of beast."
m.step("Exod.11.5")
# ‹וּמֵת כָּל־בְּכוֹר בְּאֶרֶץ› (“and-die all firstborn in-earth”)
# ‹מִצְרַיִם› (“Egypt”)
# — fact holds: and-die-all-firstborn
m.fact("u_met_kol_bekhor")

# -------------------------- Exod.11.6 · A_CRY_LIKE_NO_OTHER ----------------
# ‹וְהָיְתָה צְעָקָה גְדֹלָה› (“and-be shriek great”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם אֲשֶׁר› (“in-all earth Egypt which”)
# ‹כָּמֹהוּ לֹא נִהְיָתָה› (“form-of-the-prefix-'k-'-him/its not be”)
# ‹וְכָמֹהוּ לֹא תֹסִף› (“and-form-of-the-prefix-'k-'-him/its not add”)
# "[EN-AID] And there shall be a great cry in all the land of Egypt, such as
# like it never was and like it shall never be again."
m.step("Exod.11.6")
# ‹וְהָיְתָה צְעָקָה גְדֹלָה› (“and-be shriek great”)
# ‹בְּכָל־אֶרֶץ מִצְרָיִם› (“in-all earth Egypt”)
# — fact holds: shriek-great-kamohu-not-be
m.fact("tzeaqa_gedola_kamohu_lo_nihyata")

# -------------------------- Exod.11.7 · NOT_A_DOG_SHALL_SHARPEN ------------
# ‹וּלְכֹל בְּנֵי יִשְׂרָאֵל› (“and-to-all son Israel”)
# ‹לֹא יֶחֱרַץ־כֶּלֶב לְשֹׁנוֹ› (“not point-sharply dog tongue-him/its”)
# ‹לְמֵאִישׁ וְעַד־בְּהֵמָה לְמַעַן› (“to-from-man and-until livestock so-
# that”)
# ‹תֵּדְעוּן אֲשֶׁר יַפְלֶה› (“know-ward which distinguish”)
# ‹יְהוָה בֵּין מִצְרַיִם› (“YHWH between Egypt”)
# ‹וּבֵין יִשְׂרָאֵל› (“and-between Israel”)
# "[EN-AID] And against all the sons of Israel not a dog shall sharpen its
# tongue, against man or beast — in order that you may know that the LORD
# distinguishes between Egypt and Israel."
m.step("Exod.11.7")
# ‹וּלְכֹל בְּנֵי יִשְׂרָאֵל› (“and-to-all son Israel”)
# ‹לֹא יֶחֱרַץ־כֶּלֶב לְשֹׁנוֹ› (“not point-sharply dog tongue-him/its”)
# — fact holds: not-point-sharply-dog-leshono
m.fact("lo_yecheratz_kelev_leshono")

# -------------------------- Exod.11.8 · YOUR_SERVANTS_WILL_BOW -------------
# ‹וְיָרְדוּ כָל־עֲבָדֶיךָ אֵלֶּה› (“and-go-down all servant-you/your
# these”)
# ‹אֵלַי וְהִשְׁתַּחֲוּוּ־לִי לֵאמֹר› (“to-me/my and-afflict to-me/my to-
# say”)
# ‹צֵא אַתָּה וְכָל־הָעָם› (“bring-forth you and-all the-people”)
# ‹אֲשֶׁר־בְּרַגְלֶיךָ וְאַחֲרֵי־כֵן אֵצֵא› (“which in-foot-you/your and-
# after so bring-forth”)
# ‹וַיֵּצֵא מֵעִם־פַּרְעֹה בָּחֳרִי־אָף› (“and-bring-forth from-with Pharaoh
# in-burning-anger nose”)
# "[EN-AID] And all these your servants shall come down to me and bow to me,
# saying: Go out, you and all the people at your feet — and after that I
# will go out. And he went out from Pharaoh in hot anger."
m.step("Exod.11.8")
# ‹וְיָרְדוּ כָל־עֲבָדֶיךָ אֵלֶּה› (“and-go-down all servant-you/your
# these”)
# ‹אֵלַי וְהִשְׁתַּחֲוּוּ־לִי לֵאמֹר› (“to-me/my and-afflict to-me/my to-
# say”)
# — fact holds: and-go-down-avadekha-these
m.fact("ve_yardu_avadekha_ele")

# -------------------------- Exod.11.9 · HE_WILL_NOT_LISTEN -----------------
# ‹וַיֹּאמֶר יְהוָה אֶל־מֹשֶׁה› (“and-say YHWH to Moses”)
# ‹לֹא־יִשְׁמַע אֲלֵיכֶם פַּרְעֹה› (“not hear to-you/your(pl) Pharaoh”)
# ‹לְמַעַן רְבוֹת מוֹפְתַי› (“so-that multiply miracle-me/my”)
# ‹בְּאֶרֶץ מִצְרָיִם› (“in-earth Egypt”)
# "[EN-AID] And the LORD said to Moses: Pharaoh will not listen to you — in
# order that My wonders may be multiplied in the land of Egypt."
m.step("Exod.11.9")
# ‹לֹא־יִשְׁמַע אֲלֵיכֶם פַּרְעֹה› (“not hear to-you/your(pl) Pharaoh”)
# — fact holds: not-hear-alekhem-Pharaoh-2
m.fact("lo_yishma_alekhem_paro_2")

# -------------------------- Exod.11.10 · THE_CYCLE_COLOPHON ----------------
# ‹וּמֹשֶׁה וְאַהֲרֹן עָשׂוּ› (“and-Moses and-Aaron make”)
# ‹אֶת־כָּל־הַמֹּפְתִים הָאֵלֶּה לִפְנֵי› (“obj-marker all the-miracle the-
# these to-face”)
# ‹פַרְעֹה וַיְחַזֵּק יְהוָה› (“Pharaoh and-fasten-upon YHWH”)
# ‹אֶת־לֵב פַּרְעֹה וְלֹא־שִׁלַּח› (“obj-marker heart Pharaoh and-not send”)
# ‹אֶת־בְּנֵי־יִשְׂרָאֵל מֵאַרְצוֹ› (“obj-marker son Israel from-earth-
# him/its”)
# "[EN-AID] And Moses and Aaron did all these wonders before Pharaoh; and
# the LORD strengthened Pharaoh's heart, and he did not send the sons of
# Israel out of his land."
m.step("Exod.11.10")
# ‹וּמֹשֶׁה וְאַהֲרֹן עָשׂוּ› (“and-Moses and-Aaron make”)
# ‹אֶת־כָּל־הַמֹּפְתִים הָאֵלֶּה› (“obj-marker all the-miracle the-these”)
# — fact holds: and-Moses-and-Aaron-make
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('one_more_plague', 'plague_census')]
    assert m.WITNESS_READS[0]["cites"] == ['Pirkei Avot 5:4']
    assert all('plague_census' not in f for f in m.WORLD["facts"])
    assert 'one_more_plague' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
