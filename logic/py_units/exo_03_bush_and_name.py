#!/usr/bin/env python3
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
# ‹וּמֹשֶׁה הָיָה רֹעֶה› (“and-Moses be graze”)
# ‹אֶת־צֹאן יִתְרוֹ חֹתְנוֹ› (“obj-marker flock Jethro give-away-in-
# marriage-him/its”)
# ‹כֹּהֵן מִדְיָן וַיִּנְהַג› (“priest Midian and-drive-forth”)
# ‹אֶת־הַצֹּאן אַחַר הַמִּדְבָּר› (“obj-marker the-flock after the-pasture”)
# ‹וַיָּבֹא אֶל־הַר הָאֱלֹהִים› (“and-come/bring to mountain the-God”)
# ‹חֹרֵבָה› (“Horeb-ward”)
# "[EN-AID] And Moses was shepherding the flock of Jethro his father-in-law,
# priest of Midian; and he led the flock behind the wilderness, and came to
# the mountain of God, to Horeb."
m.step("Exod.3.1")
# ‹וַיָּבֹא אֶל־הַר הָאֱלֹהִים› (“and-come/bring to mountain the-God”)
# ‹חֹרֵבָה› (“Horeb-ward”)
# — fact holds: come/bring-come/bring-to-mountain-the-God-chorevah
m.fact("va_yavo_el_har_ha_elohim_chorevah")

# -------------------------- Exod.3.2 · THE_BUSH_UNCONSUMED -----------------
# ‹וַיֵּרָא מַלְאַךְ יְהֹוָה› (“and-see messenger YHWH”)
# ‹אֵלָיו בְּלַבַּת־אֵשׁ מִתּוֹךְ› (“to-him/its in-flame fire from-midst”)
# ‹הַסְּנֶה וַיַּרְא וְהִנֵּה› (“the-bramble and-see and-behold”)
# ‹הַסְּנֶה בֹּעֵר בָּאֵשׁ› (“the-bramble kindle in-fire”)
# ‹וְהַסְּנֶה אֵינֶנּוּ אֻכָּל› (“and-the-bramble there-is-not-him/its eat”)
# "[EN-AID] And the angel of the LORD appeared to him in a flame of fire
# from the midst of the bush; and he saw, and behold, the bush burning with
# fire, and the bush was not consumed."
m.step("Exod.3.2")
# ‹וַיֵּרָא מַלְאַךְ יְהֹוָה› (“and-see messenger YHWH”)
# ‹אֵלָיו בְּלַבַּת־אֵשׁ מִתּוֹךְ› (“to-him/its in-flame fire from-midst”)
# ‹הַסְּנֶה› (“the-bramble”)
# — event: see — agent messenger-the-LORD
m.event("nira", agent="malakh_YHWH")

# -------------------------- Exod.3.3 · LET_ME_TURN_ASIDE -------------------
# ‹וַיֹּאמֶר מֹשֶׁה אָסֻרָה־נָּא› (“and-say Moses turn-aside please”)
# ‹וְאֶרְאֶה אֶת־הַמַּרְאֶה הַגָּדֹל› (“and-see obj-marker the-appearance
# the-great”)
# ‹הַזֶּה מַדּוּעַ לֹא־יִבְעַר› (“the-this what-known? not kindle”)
# ‹הַסְּנֶה› (“the-bramble”)
# "[EN-AID] And Moses said: Let me turn aside, pray, and see this great
# sight — why the bush does not burn up."
m.step("Exod.3.3")
# ‹אָסֻרָה־נָּא וְאֶרְאֶה› (“turn-aside please and-see”)
# — fact holds: turn-aside-please-and-see
m.fact("asura_na_ve_ere")

# -------------------------- Exod.3.4 · MOSES_MOSES_UNBROKEN ----------------
# ‹וַיַּרְא יְהוָה כִּי› (“and-see YHWH that”)
# ‹סָר לִרְאוֹת וַיִּקְרָא› (“turn-aside to-see and-call”)
# ‹אֵלָיו אֱלֹהִים מִתּוֹךְ› (“to-him/its God from-midst”)
# ‹הַסְּנֶה וַיֹּאמֶר מֹשֶׁה› (“the-bramble and-say Moses”)
# ‹מֹשֶׁה וַיֹּאמֶר הִנֵּנִי› (“Moses and-say behold-me/my”)
# "[EN-AID] And the LORD saw that he turned aside to see; and God called to
# him from the midst of the bush, and said: Moses, Moses. And he said: Here
# I am."
m.step("Exod.3.4")
# ‹וַיֹּאמֶר מֹשֶׁה מֹשֶׁה› (“and-say Moses Moses”)
# ‹וַיֹּאמֶר הִנֵּנִי› (“and-say behold-me/my”)
# — fact holds: come/bring-say-Moses-Moses-behold-I
m.fact("va_yomer_moshe_moshe_hineni")

# -------------------------- Exod.3.5 · REMOVE_YOUR_SANDALS -----------------
# ‹וַיֹּאמֶר אַל־תִּקְרַב הֲלֹם› (“and-say do-not bring-near hither”)
# ‹שַׁל־נְעָלֶיךָ מֵעַל רַגְלֶיךָ› (“pluck-off sandal-tongue-you/your from-
# over foot-you/your”)
# ‹כִּי הַמָּקוֹם אֲשֶׁר› (“that the-place which”)
# ‹אַתָּה עוֹמֵד עָלָיו› (“you stand over-him/its”)
# ‹אַדְמַת־קֹדֶשׁ הוּא› (“ground holiness he/it”)
# "[EN-AID] And He said: Do not come near here; remove your sandals from
# your feet, for the place on which you are standing is holy ground."
m.step("Exod.3.5")
# ‹שַׁל־נְעָלֶיךָ מֵעַל רַגְלֶיךָ› (“pluck-off sandal-tongue-you/your from-
# over foot-you/your”)
# — the-God speaks a demand — LET: pluck-off-nealekha-from-over-raglekha
m.declare("ha_elohim", "LET",
          "shal_nealekha_me_al_raglekha")

# -------------------------- Exod.3.6 · THE_GOD_OF_YOUR_FATHER --------------
# ‹וַיֹּאמֶר אָנֹכִי אֱלֹהֵי› (“and-say God”)
# ‹אָבִיךָ אֱלֹהֵי אַבְרָהָם› (“father-you/your God Abraham”)
# ‹אֱלֹהֵי יִצְחָק וֵאלֹהֵי› (“God Isaac and-God”)
# ‹יַעֲקֹב וַיַּסְתֵּר מֹשֶׁה› (“Jacob and-hide Moses”)
# ‹פָּנָיו כִּי יָרֵא› (“face-him/its that fear”)
# ‹מֵהַבִּיט אֶל־הָאֱלֹהִים› (“from-scan to the-God”)
# "[EN-AID] And He said: I am the God of your father — the God of Abraham,
# the God of Isaac, and the God of Jacob. And Moses hid his face, for he
# feared to look upon God."
m.step("Exod.3.6")
# ‹וַיַּסְתֵּר מֹשֶׁה פָּנָיו› (“and-hide Moses face-him/its”)
# — fact holds: come/bring-hide-Moses-panav
m.fact("va_yaster_moshe_panav")

# -------------------------- Exod.3.7 · I_HAVE_SURELY_SEEN ------------------
# ‹וַיֹּאמֶר יְהוָה רָאֹה› (“and-say YHWH see”)
# ‹רָאִיתִי אֶת־עֳנִי עַמִּי› (“see obj-marker affliction people-me/my”)
# ‹אֲשֶׁר בְּמִצְרָיִם וְאֶת־צַעֲקָתָם› (“which in-Egypt and-obj-marker
# shriek-them/their”)
# ‹שָׁמַעְתִּי מִפְּנֵי נֹגְשָׂיו› (“hear from-face drive-him/its”)
# ‹כִּי יָדַעְתִּי אֶת־מַכְאֹבָיו› (“that know obj-marker anguish-him/its”)
# "[EN-AID] And the LORD said: I have surely seen the affliction of My
# people who are in Egypt, and their cry I have heard from before their
# taskmasters; for I know their pains."
m.step("Exod.3.7")
# ‹רָאֹה רָאִיתִי אֶת־עֳנִי› (“see see obj-marker affliction”)
# ‹עַמִּי› (“people-me/my”)
# — fact holds: see-see-obj-marker-affliction-ami
m.fact("rao_raiti_et_oni_ami")

# -------------------------- Exod.3.8 · I_HAVE_COME_DOWN --------------------
# ‹וָאֵרֵד לְהַצִּילוֹ מִיַּד› (“and-go-down to-snatch-away-him/its from-
# hand”)
# ‹מִצְרַיִם וּלְהַעֲלֹתוֹ מִן־הָאָרֶץ› (“Egyptian and-to-go-up-him/its from
# the-earth”)
# ‹הַהִוא אֶל־אֶרֶץ טוֹבָה› (“that to earth good”)
# ‹וּרְחָבָה אֶל־אֶרֶץ זָבַת› (“and-roomy to earth flow-freely”)
# ‹חָלָב וּדְבָשׁ אֶל־מְקוֹם› (“milk and-honey to place”)
# ‹הַכְּנַעֲנִי וְהַחִתִּי וְהָאֱמֹרִי› (“the-Kenaanite and-the-Chittite
# and-the-Emorite”)
# ‹וְהַפְּרִזִּי וְהַחִוִּי וְהַיְבוּסִי› (“and-the-Perizzite and-the-
# Chivvite and-the-Jebusite”)
# "[EN-AID] And I have come down to deliver him from the hand of Egypt, and
# to bring him up from that land to a good and broad land, to a land flowing
# with milk and honey — to the place of the Canaanite, the Hittite, the
# Amorite, the Perizzite, the Hivite, and the Jebusite."
m.step("Exod.3.8")
# ‹וָאֵרֵד לְהַצִּילוֹ מִיַּד› (“and-go-down to-snatch-away-him/its from-
# hand”)
# ‹מִצְרַיִם וּלְהַעֲלֹתוֹ› (“Egyptian and-to-go-up-him/its”)
# — fact holds: come/bring-go-down-to-hatzilo-and-to-haaloto
m.fact("va_ered_le_hatzilo_u_le_haaloto")

# -------------------------- Exod.3.9 · THE_CRY_HAS_COME --------------------
# ‹וְעַתָּה הִנֵּה צַעֲקַת› (“and-now behold shriek”)
# ‹בְּנֵי־יִשְׂרָאֵל בָּאָה אֵלָי› (“son Israel come/bring to-me/my”)
# ‹וְגַם־רָאִיתִי אֶת־הַלַּחַץ אֲשֶׁר› (“and-also see obj-marker the-
# distress which”)
# ‹מִצְרַיִם לֹחֲצִים אֹתָם› (“Egyptian press obj-marker-them/their”)
# "[EN-AID] And now, behold, the cry of the sons of Israel has come to Me;
# and I have also seen the oppression with which Egypt oppresses them."
m.step("Exod.3.9")
# ‹הִנֵּה צַעֲקַת בְּנֵי־יִשְׂרָאֵל› (“behold shriek son Israel”)
# ‹בָּאָה אֵלָי› (“come/bring to-me/my”)
# — fact holds: shriek-son-Israel-come/bring-elai
m.fact("tzaaqat_bene_yisrael_baa_elai")

# -------------------------- Exod.3.10 · GO_I_SEND_YOU ----------------------
# ‹וְעַתָּה לְכָה וְאֶשְׁלָחֲךָ› (“and-now go-ward and-send-you/your”)
# ‹אֶל־פַּרְעֹה וְהוֹצֵא אֶת־עַמִּי› (“to Pharaoh and-bring-forth obj-marker
# people-me/my”)
# ‹בְנֵי־יִשְׂרָאֵל מִמִּצְרָיִם› (“son Israel from-Egypt”)
# "[EN-AID] And now, go — and I will send you to Pharaoh; and bring out My
# people, the sons of Israel, from Egypt."
m.step("Exod.3.10")
# ‹וְעַתָּה לְכָה וְאֶשְׁלָחֲךָ› (“and-now go-ward and-send-you/your”)
# ‹אֶל־פַּרְעֹה› (“to Pharaoh”)
# — the-LORD speaks a demand — LET: to-you-and-eshlachakha-to-Pharaoh
m.declare("YHWH", "LET",
          "lekha_ve_eshlachakha_el_paro")

# -------------------------- Exod.3.11 · WHO_AM_I ---------------------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־הָאֱלֹהִים› (“and-say Moses to the-God”)
# ‹מִי אָנֹכִי כִּי› (“who? that”)
# ‹אֵלֵךְ אֶל־פַּרְעֹה וְכִי› (“go to Pharaoh and-that”)
# ‹אוֹצִיא אֶת־בְּנֵי יִשְׂרָאֵל› (“bring-forth obj-marker son Israel”)
# ‹מִמִּצְרָיִם› (“from-Egypt”)
# "[EN-AID] And Moses said to God: Who am I, that I should go to Pharaoh,
# and that I should bring out the sons of Israel from Egypt?"
m.step("Exod.3.11")
# ‹מִי אָנֹכִי כִּי› (“who? that”)
# ‹אֵלֵךְ› (“go”)
# — fact holds: who?-anokhi-that-go
m.fact("mi_anokhi_ki_elekh")

# -------------------------- Exod.3.12 · I_WILL_BE_WITH_YOU -----------------
# ‹וַיֹּאמֶר כִּי־אֶהְיֶה עִמָּךְ› (“and-say that be with-you/your”)
# ‹וְזֶה־לְּךָ הָאוֹת כִּי› (“and-this to-you/your the-signs that”)
# ‹אָנֹכִי שְׁלַחְתִּיךָ בְּהוֹצִיאֲךָ› (“send-you/your in-bring-forth-
# you/your”)
# ‹אֶת־הָעָם מִמִּצְרַיִם תַּעַבְדוּן› (“obj-marker the-people from-Egypt
# work/serve-ward”)
# ‹אֶת־הָאֱלֹהִים עַל הָהָר› (“obj-marker the-God over the-mountain”)
# ‹הַזֶּה› (“the-this”)
# "[EN-AID] And He said: For I will be with you; and this is the sign for
# you that I have sent you: when you bring out the people from Egypt, you
# shall serve God upon this mountain."
m.step("Exod.3.12")
# ‹תַּעַבְדוּן אֶת־הָאֱלֹהִים עַל› (“work/serve-ward obj-marker the-God
# over”)
# ‹הָהָר הַזֶּה› (“the-mountain the-this”)
# — fact holds: taavdun-over-the-mountain-the-this
m.fact("taavdun_al_ha_har_ha_ze")

# -------------------------- Exod.3.13 · WHAT_IS_HIS_NAME -------------------
# ‹וַיֹּאמֶר מֹשֶׁה אֶל־הָאֱלֹהִים› (“and-say Moses to the-God”)
# ‹הִנֵּה אָנֹכִי בָא› (“behold come/bring”)
# ‹אֶל־בְּנֵי יִשְׂרָאֵל וְאָמַרְתִּי› (“to son Israel and-say”)
# ‹לָהֶם אֱלֹהֵי אֲבוֹתֵיכֶם› (“to-them/their God father-you/your(pl)”)
# ‹שְׁלָחַנִי אֲלֵיכֶם וְאָמְרוּ־לִי› (“send-me/my to-you/your(pl) and-say
# to-me/my”)
# ‹מַה־שְּׁמוֹ מָה אֹמַר› (“what name-him/its what say”)
# ‹אֲלֵהֶם› (“to-them/their”)
# "[EN-AID] And Moses said to God: Behold, I come to the sons of Israel, and
# I say to them: The God of your fathers sent me to you. And they will say
# to me: What is His name? What shall I say to them?"
m.step("Exod.3.13")
# ‹וְאָמְרוּ־לִי מַה־שְּׁמוֹ מָה› (“and-say to-me/my what name-him/its
# what”)
# — fact holds: and-say-to-me-what-shemo
m.fact("ve_amru_li_ma_shemo")

# -------------------------- Exod.3.14 · I_WILL_BE_WHAT_I_WILL_BE -----------
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־מֹשֶׁה› (“and-say God to Moses”)
# ‹אֶהְיֶה אֲשֶׁר אֶהְיֶה› (“be which be”)
# ‹וַיֹּאמֶר כֹּה תֹאמַר› (“and-say like-this say”)
# ‹לִבְנֵי יִשְׂרָאֵל אֶהְיֶה› (“to-son Israel be”)
# ‹שְׁלָחַנִי אֲלֵיכֶם› (“send-me/my to-you/your(pl)”)
# "[EN-AID] And God said to Moses: I will be what I will be. And He said:
# Thus shall you say to the sons of Israel: I-Will-Be sent me to you."
m.step("Exod.3.14")
# ‹אֶהְיֶה אֲשֶׁר אֶהְיֶה› (“be which be”)
# — fact holds: be-which-be
m.fact("ehye_asher_ehye")

# -------------------------- Exod.3.15 · MY_NAME_FOREVER_CONCEALED ----------
# ‹וַיֹּאמֶר עוֹד אֱלֹהִים› (“and-say still/again God”)
# ‹אֶל־מֹשֶׁה כֹּה־תֹאמַר אֶל־בְּנֵי› (“to Moses like-this say to son”)
# ‹יִשְׂרָאֵל יְהוָה אֱלֹהֵי› (“Israel YHWH God”)
# ‹אֲבֹתֵיכֶם אֱלֹהֵי אַבְרָהָם› (“father-you/your(pl) God Abraham”)
# ‹אֱלֹהֵי יִצְחָק וֵאלֹהֵי› (“God Isaac and-God”)
# ‹יַעֲקֹב שְׁלָחַנִי אֲלֵיכֶם› (“Jacob send-me/my to-you/your(pl)”)
# ‹זֶה־שְּׁמִי לְעֹלָם וְזֶה› (“this name-me/my to-forever and-this”)
# ‹זִכְרִי לְדֹר דֹּר› (“memento-me/my to-generation generation”)
# "[EN-AID] And God said further to Moses: Thus shall you say to the sons of
# Israel: The LORD, the God of your fathers — the God of Abraham, the God of
# Isaac, and the God of Jacob — sent me to you. This is My name forever, and
# this is My memorial to generation after generation."
m.step("Exod.3.15")
# ‹זֶה־שְּׁמִי לְעֹלָם› (“this name-me/my to-forever”)
# — fact holds: this-shemi-to-forever
m.fact("ze_shemi_le_olam")
# witness-tier presupposed read: name_ink_protection_file on
# ze_shemi_le_olam — read, not installed
m.witness_read("ze_shemi_le_olam", "name_ink_protection_file",
                cites=["Shevuot 35a:27", "Shevuot 35a:28", "Shevuot 35b:4", "Shevuot 35b:5", "Shevuot 35b:6", "Shevuot 35b:7", "Pesachim 50a:19", "Pesachim 50a:20", "Pesachim 50a:21", "Pesachim 117a:1", "Pesachim 117a:2", "Pesachim 117a:3"])

# -------------------------- Exod.3.16 · GATHER_THE_ELDERS ------------------
# ‹לֵךְ וְאָסַפְתָּ אֶת־זִקְנֵי› (“go and-gather-for-any-purpose obj-marker
# old”)
# ‹יִשְׂרָאֵל וְאָמַרְתָּ אֲלֵהֶם› (“Israel and-say to-them/their”)
# ‹יְהוָה אֱלֹהֵי אֲבֹתֵיכֶם› (“YHWH God father-you/your(pl)”)
# ‹נִרְאָה אֵלַי אֱלֹהֵי› (“see to-me/my God”)
# ‹אַבְרָהָם יִצְחָק וְיַעֲקֹב› (“Abraham Isaac and-Jacob”)
# ‹לֵאמֹר פָּקֹד פָּקַדְתִּי› (“to-say count/visit count/visit”)
# ‹אֶתְכֶם וְאֶת־הֶעָשׂוּי לָכֶם› (“obj-marker-you/your(pl) and-obj-marker
# the-make to-you/your(pl)”)
# ‹בְּמִצְרָיִם› (“in-Egypt”)
# "[EN-AID] Go, and gather the elders of Israel, and say to them: The LORD,
# the God of your fathers, appeared to me — the God of Abraham, Isaac, and
# Jacob — saying: I have surely visited you, and that which is done to you
# in Egypt."
m.step("Exod.3.16")
# ‹פָּקֹד פָּקַדְתִּי אֶתְכֶם› (“count/visit count/visit obj-marker-
# you/your(pl)”)
# — the-LORD speaks a demand — LET: go-and-gather-for-any-purpose-obj-
# marker-old-Israel
m.declare("YHWH", "LET",
          "lekh_ve_asafta_et_ziqne_yisrael")

# -------------------------- Exod.3.17 · UP_FROM_THE_AFFLICTION -------------
# ‹וָאֹמַר אַעֲלֶה אֶתְכֶם› (“and-say go-up obj-marker-you/your(pl)”)
# ‹מֵעֳנִי מִצְרַיִם אֶל־אֶרֶץ› (“from-affliction Egypt to earth”)
# ‹הַכְּנַעֲנִי וְהַחִתִּי וְהָאֱמֹרִי› (“the-Kenaanite and-the-Chittite
# and-the-Emorite”)
# ‹וְהַפְּרִזִּי וְהַחִוִּי וְהַיְבוּסִי› (“and-the-Perizzite and-the-
# Chivvite and-the-Jebusite”)
# ‹אֶל־אֶרֶץ זָבַת חָלָב› (“to earth flow-freely milk”)
# ‹וּדְבָשׁ› (“and-honey”)
# "[EN-AID] And I have said: I will bring you up from the affliction of
# Egypt to the land of the Canaanite, the Hittite, the Amorite, the
# Perizzite, the Hivite, and the Jebusite — to a land flowing with milk and
# honey."
m.step("Exod.3.17")
# ‹וָאֹמַר אַעֲלֶה אֶתְכֶם› (“and-say go-up obj-marker-you/your(pl)”)
# ‹מֵעֳנִי מִצְרַיִם› (“from-affliction Egypt”)
# — fact holds: go-up-etkhem-from-affliction-Egypt
m.fact("aale_etkhem_me_oni_mitzrayim")

# -------------------------- Exod.3.18 · THE_COURT_SCRIPT -------------------
# ‹וְשָׁמְעוּ לְקֹלֶךָ וּבָאתָ› (“and-hear to-voice/sound-you/your and-
# come/bring”)
# ‹אַתָּה וְזִקְנֵי יִשְׂרָאֵל› (“you and-old Israel”)
# ‹אֶל־מֶלֶךְ מִצְרַיִם וַאֲמַרְתֶּם› (“to king Egypt and-say”)
# ‹אֵלָיו יְהוָה אֱלֹהֵי› (“to-him/its YHWH God”)
# ‹הָעִבְרִיִּים נִקְרָה עָלֵינוּ› (“the-Hebrew light-upon over-us/our”)
# ‹וְעַתָּה נֵלֲכָה־נָּא דֶּרֶךְ› (“and-now go please way/road”)
# ‹שְׁלֹשֶׁת יָמִים בַּמִּדְבָּר› (“three day in-pasture”)
# ‹וְנִזְבְּחָה לַיהוָה אֱלֹהֵינוּ› (“and-slaughter-an-animal to-YHWH God-
# us/our”)
# "[EN-AID] And they will hear your voice; and you shall come — you and the
# elders of Israel — to the king of Egypt, and you shall say to him: The
# LORD, the God of the Hebrews, happened upon us; and now, let us go, pray,
# a journey of three days into the wilderness, that we may sacrifice to the
# LORD our God."
m.step("Exod.3.18")
# ‹וַאֲמַרְתֶּם אֵלָיו יְהוָה› (“and-say to-him/its YHWH”)
# ‹אֱלֹהֵי הָעִבְרִיִּים נִקְרָה› (“God the-Hebrew light-upon”)
# ‹עָלֵינוּ› (“over-us/our”)
# — the-LORD speaks a demand — LET: come/bring-say-to-king-Egypt
m.declare("YHWH", "LET",
          "va_amartem_el_melekh_mitzrayim")

# -------------------------- Exod.3.19 · I_KNOW_HE_WILL_NOT_GIVE ------------
# ‹וַאֲנִי יָדַעְתִּי כִּי› (“and-I know that”)
# ‹לֹא־יִתֵּן אֶתְכֶם מֶלֶךְ› (“not set obj-marker-you/your(pl) king”)
# ‹מִצְרַיִם לַהֲלֹךְ וְלֹא› (“Egypt to-walk/go and-not”)
# ‹בְּיָד חֲזָקָה› (“in-hand strong”)
# "[EN-AID] And I — I know that the king of Egypt will not give you to go,
# and not by a strong hand."
m.step("Exod.3.19")
# ‹כִּי לֹא־יִתֵּן אֶתְכֶם› (“that not set obj-marker-you/your(pl)”)
# ‹מֶלֶךְ מִצְרַיִם לַהֲלֹךְ› (“king Egypt to-walk/go”)
# — fact holds: not-set-etkhem-to-walk/go
m.fact("lo_yiten_etkhem_la_halokh")

# -------------------------- Exod.3.20 · I_WILL_STRIKE ----------------------
# ‹וְשָׁלַחְתִּי אֶת־יָדִי וְהִכֵּיתִי› (“and-send obj-marker hand-me/my
# and-strike”)
# ‹אֶת־מִצְרַיִם בְּכֹל נִפְלְאֹתַי› (“obj-marker Egyptian in-all perhaps-
# to-separate-me/my”)
# ‹אֲשֶׁר אֶעֱשֶׂה בְּקִרְבּוֹ› (“which make in-nearest-part-him/its”)
# ‹וְאַחֲרֵי־כֵן יְשַׁלַּח אֶתְכֶם› (“and-after so send obj-marker-
# you/your(pl)”)
# "[EN-AID] And I will send My hand, and strike Egypt with all My wonders
# which I will do in its midst; and after that he will send you out."
m.step("Exod.3.20")
# ‹וְהִכֵּיתִי אֶת־מִצְרַיִם› (“and-strike obj-marker Egyptian”)
# — fact holds: and-strike-obj-marker-Egypt
m.fact("ve_hiketi_et_mitzrayim")

# -------------------------- Exod.3.21 · NOT_EMPTY --------------------------
# ‹וְנָתַתִּי אֶת־חֵן הָעָם־הַזֶּה› (“and-set obj-marker graciousness the-
# people the-this”)
# ‹בְּעֵינֵי מִצְרָיִם וְהָיָה› (“in-eye Egyptian and-be”)
# ‹כִּי תֵלֵכוּן לֹא› (“that go-ward not”)
# ‹תֵלְכוּ רֵיקָם› (“go emptily”)
# "[EN-AID] And I will give this people favor in the eyes of Egypt; and it
# shall be, when you go, you shall not go empty."
m.step("Exod.3.21")
# ‹לֹא תֵלְכוּ רֵיקָם› (“not go emptily”)
# — fact holds: not-go-emptily
m.fact("lo_telkhu_reqam")

# -------------------------- Exod.3.22 · YOU_SHALL_EMPTY_EGYPT --------------
# ‹וְשָׁאֲלָה אִשָּׁה מִשְּׁכֶנְתָּהּ› (“and-inquire woman from-resident-
# her/its”)
# ‹וּמִגָּרַת בֵּיתָהּ כְּלֵי־כֶסֶף› (“and-from-turn-aside-from-the-road
# house-her/its vessel silver”)
# ‹וּכְלֵי זָהָב וּשְׂמָלֹת› (“and-vessel gold and-dress”)
# ‹וְשַׂמְתֶּם עַל־בְּנֵיכֶם וְעַל־בְּנֹתֵיכֶם› (“and-put/set over son-
# you/your(pl) and-over daughter-you/your(pl)”)
# ‹וְנִצַּלְתֶּם אֶת־מִצְרָיִם› (“and-snatch-away obj-marker Egyptian”)
# "[EN-AID] And each woman shall ask of her neighbor, and of the sojourner
# of her house, vessels of silver and vessels of gold, and garments; and you
# shall put them on your sons and on your daughters — and you shall empty
# Egypt."
m.step("Exod.3.22")
# ‹וְנִצַּלְתֶּם אֶת־מִצְרָיִם› (“and-snatch-away obj-marker Egyptian”)
# — fact holds: and-snatch-away-obj-marker-Egypt
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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('ze_shemi_le_olam', 'name_ink_protection_file')]
    assert m.WITNESS_READS[0]["cites"] == ['Shevuot 35a:27', 'Shevuot 35a:28', 'Shevuot 35b:4', 'Shevuot 35b:5', 'Shevuot 35b:6', 'Shevuot 35b:7', 'Pesachim 50a:19', 'Pesachim 50a:20', 'Pesachim 50a:21', 'Pesachim 117a:1', 'Pesachim 117a:2', 'Pesachim 117a:3']
    assert all('name_ink_protection_file' not in f for f in m.WORLD["facts"])
    assert 'ze_shemi_le_olam' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
