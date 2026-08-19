#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# exo_03_bush_and_name — 3:1-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/exo_03_bush_and_name.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The bush and the Name (3:1-22)"""
from machine import Machine

m = Machine("exo_03_bush_and_name")

# -------------------------- Exod.3.1 · BEHIND_THE_WILDERNESS ---------------
# וּמֹשֶׁה הָיָה רֹעֶה אֶת־צֹאן יִתְרוֹ חֹתְנוֹ כֹּהֵן מִדְיָן וַיִּנְהַג
# אֶת־הַצֹּאן אַחַר הַמִּדְבָּר וַיָּבֹא אֶל־הַר הָאֱלֹהִים חֹרֵבָה
# "[EN-AID] And Moses was shepherding the flock of Jethro his father-in-law,
# priest of Midian; and he led the flock behind the wilderness, and came to
# the mountain of God, to Horeb."
m.step("Exod.3.1")
# ‹וַיָּבֹא אֶל־הַר הָאֱלֹהִים חֹרֵבָה› (“and-come/bring to mountain the-God
# Horeb-ward”) — fact holds: come/bring-come/bring-to-mountain-the-God-
# chorevah
m.fact("va_yavo_el_har_ha_elohim_chorevah")

# -------------------------- Exod.3.2 · THE_BUSH_UNCONSUMED -----------------
# וַיֵּרָא מַלְאַךְ יְהֹוָה אֵלָיו בְּלַבַּת־אֵשׁ מִתּוֹךְ הַסְּנֶה וַיַּרְא
# וְהִנֵּה הַסְּנֶה בֹּעֵר בָּאֵשׁ וְהַסְּנֶה אֵינֶנּוּ אֻכָּל
# "[EN-AID] And the angel of the LORD appeared to him in a flame of fire
# from the midst of the bush; and he saw, and behold, the bush burning with
# fire, and the bush was not consumed."
m.step("Exod.3.2")
# ‹וַיֵּרָא מַלְאַךְ יְהֹוָה אֵלָיו בְּלַבַּת־אֵשׁ מִתּוֹךְ הַסְּנֶה› (“and-
# see messenger YHWH to-him/its in-flame fire from-midst the-bramble”) —
# event: see — agent messenger-the-LORD
m.event("nira", agent="malakh_YHWH")

# -------------------------- Exod.3.3 · LET_ME_TURN_ASIDE -------------------
# וַיֹּאמֶר מֹשֶׁה אָסֻרָה־נָּא וְאֶרְאֶה אֶת־הַמַּרְאֶה הַגָּדֹל הַזֶּה
# מַדּוּעַ לֹא־יִבְעַר הַסְּנֶה
# "[EN-AID] And Moses said: Let me turn aside, pray, and see this great
# sight — why the bush does not burn up."
m.step("Exod.3.3")
# ‹אָסֻרָה־נָּא וְאֶרְאֶה› (“turn-aside please and-see”) — fact holds: turn-
# aside-please-and-see
m.fact("asura_na_ve_ere")

# -------------------------- Exod.3.4 · MOSES_MOSES_UNBROKEN ----------------
# וַיַּרְא יְהוָה כִּי סָר לִרְאוֹת וַיִּקְרָא אֵלָיו אֱלֹהִים מִתּוֹךְ
# הַסְּנֶה וַיֹּאמֶר מֹשֶׁה מֹשֶׁה וַיֹּאמֶר הִנֵּנִי
# "[EN-AID] And the LORD saw that he turned aside to see; and God called to
# him from the midst of the bush, and said: Moses, Moses. And he said: Here
# I am."
m.step("Exod.3.4")
# ‹וַיֹּאמֶר מֹשֶׁה מֹשֶׁה וַיֹּאמֶר הִנֵּנִי› (“and-say Moses Moses and-say
# behold-me/my”) — fact holds: come/bring-say-Moses-Moses-behold-I
m.fact("va_yomer_moshe_moshe_hineni")

# -------------------------- Exod.3.5 · REMOVE_YOUR_SANDALS -----------------
# וַיֹּאמֶר אַל־תִּקְרַב הֲלֹם שַׁל־נְעָלֶיךָ מֵעַל רַגְלֶיךָ כִּי הַמָּקוֹם
# אֲשֶׁר אַתָּה עוֹמֵד עָלָיו אַדְמַת־קֹדֶשׁ הוּא
# "[EN-AID] And He said: Do not come near here; remove your sandals from
# your feet, for the place on which you are standing is holy ground."
m.step("Exod.3.5")
# ‹שַׁל־נְעָלֶיךָ מֵעַל רַגְלֶיךָ› (“pluck-off sandal-tongue-you/your from-
# over foot-you/your”) — the-God speaks a demand — LET: pluck-off-nealekha-
# from-over-raglekha
m.declare("ha_elohim", "LET",
          "shal_nealekha_me_al_raglekha")

# -------------------------- Exod.3.6 · THE_GOD_OF_YOUR_FATHER --------------
# וַיֹּאמֶר אָנֹכִי אֱלֹהֵי אָבִיךָ אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק
# וֵאלֹהֵי יַעֲקֹב וַיַּסְתֵּר מֹשֶׁה פָּנָיו כִּי יָרֵא מֵהַבִּיט
# אֶל־הָאֱלֹהִים
# "[EN-AID] And He said: I am the God of your father — the God of Abraham,
# the God of Isaac, and the God of Jacob. And Moses hid his face, for he
# feared to look upon God."
m.step("Exod.3.6")
# ‹וַיַּסְתֵּר מֹשֶׁה פָּנָיו› (“and-hide Moses face-him/its”) — fact holds:
# come/bring-hide-Moses-panav
m.fact("va_yaster_moshe_panav")

# -------------------------- Exod.3.7 · I_HAVE_SURELY_SEEN ------------------
# וַיֹּאמֶר יְהוָה רָאֹה רָאִיתִי אֶת־עֳנִי עַמִּי אֲשֶׁר בְּמִצְרָיִם
# וְאֶת־צַעֲקָתָם שָׁמַעְתִּי מִפְּנֵי נֹגְשָׂיו כִּי יָדַעְתִּי
# אֶת־מַכְאֹבָיו
# "[EN-AID] And the LORD said: I have surely seen the affliction of My
# people who are in Egypt, and their cry I have heard from before their
# taskmasters; for I know their pains."
m.step("Exod.3.7")
# ‹רָאֹה רָאִיתִי אֶת־עֳנִי עַמִּי› (“see see obj-marker affliction people-
# me/my”) — fact holds: see-see-obj-marker-affliction-ami
m.fact("rao_raiti_et_oni_ami")

# -------------------------- Exod.3.8 · I_HAVE_COME_DOWN --------------------
# וָאֵרֵד לְהַצִּילוֹ מִיַּד מִצְרַיִם וּלְהַעֲלֹתוֹ מִן־הָאָרֶץ הַהִוא
# אֶל־אֶרֶץ טוֹבָה וּרְחָבָה אֶל־אֶרֶץ זָבַת חָלָב וּדְבָשׁ אֶל־מְקוֹם
# הַכְּנַעֲנִי וְהַחִתִּי וְהָאֱמֹרִי וְהַפְּרִזִּי וְהַחִוִּי וְהַיְבוּסִי
# "[EN-AID] And I have come down to deliver him from the hand of Egypt, and
# to bring him up from that land to a good and broad land, to a land flowing
# with milk and honey — to the place of the Canaanite, the Hittite, the
# Amorite, the Perizzite, the Hivite, and the Jebusite."
m.step("Exod.3.8")
# ‹וָאֵרֵד לְהַצִּילוֹ מִיַּד מִצְרַיִם וּלְהַעֲלֹתוֹ› (“and-go-down to-
# snatch-away-him/its from-hand Egyptian and-to-go-up-him/its”) — fact
# holds: come/bring-go-down-to-hatzilo-and-to-haaloto
m.fact("va_ered_le_hatzilo_u_le_haaloto")

# -------------------------- Exod.3.9 · THE_CRY_HAS_COME --------------------
# וְעַתָּה הִנֵּה צַעֲקַת בְּנֵי־יִשְׂרָאֵל בָּאָה אֵלָי וְגַם־רָאִיתִי
# אֶת־הַלַּחַץ אֲשֶׁר מִצְרַיִם לֹחֲצִים אֹתָם
# "[EN-AID] And now, behold, the cry of the sons of Israel has come to Me;
# and I have also seen the oppression with which Egypt oppresses them."
m.step("Exod.3.9")
# ‹הִנֵּה צַעֲקַת בְּנֵי־יִשְׂרָאֵל בָּאָה אֵלָי› (“behold shriek son Israel
# come/bring to-me/my”) — fact holds: shriek-son-Israel-come/bring-elai
m.fact("tzaaqat_bene_yisrael_baa_elai")

# -------------------------- Exod.3.10 · GO_I_SEND_YOU ----------------------
# וְעַתָּה לְכָה וְאֶשְׁלָחֲךָ אֶל־פַּרְעֹה וְהוֹצֵא אֶת־עַמִּי
# בְנֵי־יִשְׂרָאֵל מִמִּצְרָיִם
# "[EN-AID] And now, go — and I will send you to Pharaoh; and bring out My
# people, the sons of Israel, from Egypt."
m.step("Exod.3.10")
# ‹וְעַתָּה לְכָה וְאֶשְׁלָחֲךָ אֶל־פַּרְעֹה› (“and-now go-ward and-send-
# you/your to Pharaoh”) — the-LORD speaks a demand — LET: to-you-and-
# eshlachakha-to-Pharaoh
m.declare("YHWH", "LET",
          "lekha_ve_eshlachakha_el_paro")

# -------------------------- Exod.3.11 · WHO_AM_I ---------------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־הָאֱלֹהִים מִי אָנֹכִי כִּי אֵלֵךְ אֶל־פַּרְעֹה וְכִי
# אוֹצִיא אֶת־בְּנֵי יִשְׂרָאֵל מִמִּצְרָיִם
# "[EN-AID] And Moses said to God: Who am I, that I should go to Pharaoh,
# and that I should bring out the sons of Israel from Egypt?"
m.step("Exod.3.11")
# ‹מִי אָנֹכִי כִּי אֵלֵךְ› (“who? that go”) — fact holds: who?-anokhi-that-
# go
m.fact("mi_anokhi_ki_elekh")

# -------------------------- Exod.3.12 · I_WILL_BE_WITH_YOU -----------------
# וַיֹּאמֶר כִּי־אֶהְיֶה עִמָּךְ וְזֶה־לְּךָ הָאוֹת כִּי אָנֹכִי
# שְׁלַחְתִּיךָ בְּהוֹצִיאֲךָ אֶת־הָעָם מִמִּצְרַיִם תַּעַבְדוּן
# אֶת־הָאֱלֹהִים עַל הָהָר הַזֶּה
# "[EN-AID] And He said: For I will be with you; and this is the sign for
# you that I have sent you: when you bring out the people from Egypt, you
# shall serve God upon this mountain."
m.step("Exod.3.12")
# ‹תַּעַבְדוּן אֶת־הָאֱלֹהִים עַל הָהָר הַזֶּה› (“work/serve-ward obj-marker
# the-God over the-mountain the-this”) — fact holds: taavdun-over-the-
# mountain-the-this
m.fact("taavdun_al_ha_har_ha_ze")

# -------------------------- Exod.3.13 · WHAT_IS_HIS_NAME -------------------
# וַיֹּאמֶר מֹשֶׁה אֶל־הָאֱלֹהִים הִנֵּה אָנֹכִי בָא אֶל־בְּנֵי יִשְׂרָאֵל
# וְאָמַרְתִּי לָהֶם אֱלֹהֵי אֲבוֹתֵיכֶם שְׁלָחַנִי אֲלֵיכֶם וְאָמְרוּ־לִי
# מַה־שְּׁמוֹ מָה אֹמַר אֲלֵהֶם
# "[EN-AID] And Moses said to God: Behold, I come to the sons of Israel, and
# I say to them: The God of your fathers sent me to you. And they will say
# to me: What is His name? What shall I say to them?"
m.step("Exod.3.13")
# ‹וְאָמְרוּ־לִי מַה־שְּׁמוֹ מָה› (“and-say to-me/my what name-him/its
# what”) — fact holds: and-say-to-me-what-shemo
m.fact("ve_amru_li_ma_shemo")

# -------------------------- Exod.3.14 · I_WILL_BE_WHAT_I_WILL_BE -----------
# וַיֹּאמֶר אֱלֹהִים אֶל־מֹשֶׁה אֶהְיֶה אֲשֶׁר אֶהְיֶה וַיֹּאמֶר כֹּה תֹאמַר
# לִבְנֵי יִשְׂרָאֵל אֶהְיֶה שְׁלָחַנִי אֲלֵיכֶם
# "[EN-AID] And God said to Moses: I will be what I will be. And He said:
# Thus shall you say to the sons of Israel: I-Will-Be sent me to you."
m.step("Exod.3.14")
# ‹אֶהְיֶה אֲשֶׁר אֶהְיֶה› (“be which be”) — fact holds: be-which-be
m.fact("ehye_asher_ehye")

# -------------------------- Exod.3.15 · MY_NAME_FOREVER_CONCEALED ----------
# וַיֹּאמֶר עוֹד אֱלֹהִים אֶל־מֹשֶׁה כֹּה־תֹאמַר אֶל־בְּנֵי יִשְׂרָאֵל
# יְהוָה אֱלֹהֵי אֲבֹתֵיכֶם אֱלֹהֵי אַבְרָהָם אֱלֹהֵי יִצְחָק וֵאלֹהֵי
# יַעֲקֹב שְׁלָחַנִי אֲלֵיכֶם זֶה־שְּׁמִי לְעֹלָם וְזֶה זִכְרִי לְדֹר דֹּר
# "[EN-AID] And God said further to Moses: Thus shall you say to the sons of
# Israel: The LORD, the God of your fathers — the God of Abraham, the God of
# Isaac, and the God of Jacob — sent me to you. This is My name forever, and
# this is My memorial to generation after generation."
m.step("Exod.3.15")
# ‹זֶה־שְּׁמִי לְעֹלָם› (“this name-me/my to-forever”) — fact holds: this-
# shemi-to-forever
m.fact("ze_shemi_le_olam")

# -------------------------- Exod.3.16 · GATHER_THE_ELDERS ------------------
# לֵךְ וְאָסַפְתָּ אֶת־זִקְנֵי יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם יְהוָה אֱלֹהֵי
# אֲבֹתֵיכֶם נִרְאָה אֵלַי אֱלֹהֵי אַבְרָהָם יִצְחָק וְיַעֲקֹב לֵאמֹר פָּקֹד
# פָּקַדְתִּי אֶתְכֶם וְאֶת־הֶעָשׂוּי לָכֶם בְּמִצְרָיִם
# "[EN-AID] Go, and gather the elders of Israel, and say to them: The LORD,
# the God of your fathers, appeared to me — the God of Abraham, Isaac, and
# Jacob — saying: I have surely visited you, and that which is done to you
# in Egypt."
m.step("Exod.3.16")
# ‹פָּקֹד פָּקַדְתִּי אֶתְכֶם› (“count/visit count/visit obj-marker-
# you/your(pl)”) — the-LORD speaks a demand — LET: go-and-gather-for-any-
# purpose-obj-marker-old-Israel
m.declare("YHWH", "LET",
          "lekh_ve_asafta_et_ziqne_yisrael")

# -------------------------- Exod.3.17 · UP_FROM_THE_AFFLICTION -------------
# וָאֹמַר אַעֲלֶה אֶתְכֶם מֵעֳנִי מִצְרַיִם אֶל־אֶרֶץ הַכְּנַעֲנִי
# וְהַחִתִּי וְהָאֱמֹרִי וְהַפְּרִזִּי וְהַחִוִּי וְהַיְבוּסִי אֶל־אֶרֶץ
# זָבַת חָלָב וּדְבָשׁ
# "[EN-AID] And I have said: I will bring you up from the affliction of
# Egypt to the land of the Canaanite, the Hittite, the Amorite, the
# Perizzite, the Hivite, and the Jebusite — to a land flowing with milk and
# honey."
m.step("Exod.3.17")
# ‹וָאֹמַר אַעֲלֶה אֶתְכֶם מֵעֳנִי מִצְרַיִם› (“and-say go-up obj-marker-
# you/your(pl) from-affliction Egypt”) — fact holds: go-up-etkhem-from-
# affliction-Egypt
m.fact("aale_etkhem_me_oni_mitzrayim")

# -------------------------- Exod.3.18 · THE_COURT_SCRIPT -------------------
# וְשָׁמְעוּ לְקֹלֶךָ וּבָאתָ אַתָּה וְזִקְנֵי יִשְׂרָאֵל אֶל־מֶלֶךְ
# מִצְרַיִם וַאֲמַרְתֶּם אֵלָיו יְהוָה אֱלֹהֵי הָעִבְרִיִּים נִקְרָה
# עָלֵינוּ וְעַתָּה נֵלֲכָה־נָּא דֶּרֶךְ שְׁלֹשֶׁת יָמִים בַּמִּדְבָּר
# וְנִזְבְּחָה לַיהוָה אֱלֹהֵינוּ
# "[EN-AID] And they will hear your voice; and you shall come — you and the
# elders of Israel — to the king of Egypt, and you shall say to him: The
# LORD, the God of the Hebrews, happened upon us; and now, let us go, pray,
# a journey of three days into the wilderness, that we may sacrifice to the
# LORD our God."
m.step("Exod.3.18")
# ‹וַאֲמַרְתֶּם אֵלָיו יְהוָה אֱלֹהֵי הָעִבְרִיִּים נִקְרָה עָלֵינוּ› (“and-
# say to-him/its YHWH God the-Hebrew light-upon over-us/our”) — the-LORD
# speaks a demand — LET: come/bring-say-to-king-Egypt
m.declare("YHWH", "LET",
          "va_amartem_el_melekh_mitzrayim")

# -------------------------- Exod.3.19 · I_KNOW_HE_WILL_NOT_GIVE ------------
# וַאֲנִי יָדַעְתִּי כִּי לֹא־יִתֵּן אֶתְכֶם מֶלֶךְ מִצְרַיִם לַהֲלֹךְ וְלֹא
# בְּיָד חֲזָקָה
# "[EN-AID] And I — I know that the king of Egypt will not give you to go,
# and not by a strong hand."
m.step("Exod.3.19")
# ‹כִּי לֹא־יִתֵּן אֶתְכֶם מֶלֶךְ מִצְרַיִם לַהֲלֹךְ› (“that not set obj-
# marker-you/your(pl) king Egypt to-walk/go”) — fact holds: not-set-etkhem-
# to-walk/go
m.fact("lo_yiten_etkhem_la_halokh")

# -------------------------- Exod.3.20 · I_WILL_STRIKE ----------------------
# וְשָׁלַחְתִּי אֶת־יָדִי וְהִכֵּיתִי אֶת־מִצְרַיִם בְּכֹל נִפְלְאֹתַי
# אֲשֶׁר אֶעֱשֶׂה בְּקִרְבּוֹ וְאַחֲרֵי־כֵן יְשַׁלַּח אֶתְכֶם
# "[EN-AID] And I will send My hand, and strike Egypt with all My wonders
# which I will do in its midst; and after that he will send you out."
m.step("Exod.3.20")
# ‹וְהִכֵּיתִי אֶת־מִצְרַיִם› (“and-strike obj-marker Egyptian”) — fact
# holds: and-strike-obj-marker-Egypt
m.fact("ve_hiketi_et_mitzrayim")

# -------------------------- Exod.3.21 · NOT_EMPTY --------------------------
# וְנָתַתִּי אֶת־חֵן הָעָם־הַזֶּה בְּעֵינֵי מִצְרָיִם וְהָיָה כִּי תֵלֵכוּן
# לֹא תֵלְכוּ רֵיקָם
# "[EN-AID] And I will give this people favor in the eyes of Egypt; and it
# shall be, when you go, you shall not go empty."
m.step("Exod.3.21")
# ‹לֹא תֵלְכוּ רֵיקָם› (“not go emptily”) — fact holds: not-go-emptily
m.fact("lo_telkhu_reqam")

# -------------------------- Exod.3.22 · YOU_SHALL_EMPTY_EGYPT --------------
# וְשָׁאֲלָה אִשָּׁה מִשְּׁכֶנְתָּהּ וּמִגָּרַת בֵּיתָהּ כְּלֵי־כֶסֶף
# וּכְלֵי זָהָב וּשְׂמָלֹת וְשַׂמְתֶּם עַל־בְּנֵיכֶם וְעַל־בְּנֹתֵיכֶם
# וְנִצַּלְתֶּם אֶת־מִצְרָיִם
# "[EN-AID] And each woman shall ask of her neighbor, and of the sojourner
# of her house, vessels of silver and vessels of gold, and garments; and you
# shall put them on your sons and on your daughters — and you shall empty
# Egypt."
m.step("Exod.3.22")
# ‹וְנִצַּלְתֶּם אֶת־מִצְרָיִם› (“and-snatch-away obj-marker Egyptian”) —
# fact holds: and-snatch-away-obj-marker-Egypt
m.fact("ve_nitzaltem_et_mitzrayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shal_nealekha_me_al_raglekha', 'lekha_ve_eshlachakha_el_paro', 'lekh_ve_asafta_et_ziqne_yisrael', 'va_amartem_el_melekh_mitzrayim']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yavo_el_har_ha_elohim_chorevah', 'asura_na_ve_ere', 'va_yomer_moshe_moshe_hineni', 'va_yaster_moshe_panav', 'rao_raiti_et_oni_ami', 'va_ered_le_hatzilo_u_le_haaloto', 'tzaaqat_bene_yisrael_baa_elai', 'mi_anokhi_ki_elekh', 'taavdun_al_ha_har_ha_ze', 've_amru_li_ma_shemo', 'ehye_asher_ehye', 'ze_shemi_le_olam', 'aale_etkhem_me_oni_mitzrayim', 'lo_yiten_etkhem_la_halokh', 've_hiketi_et_mitzrayim', 'lo_telkhu_reqam', 've_nitzaltem_et_mitzrayim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
