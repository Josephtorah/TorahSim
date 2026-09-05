#!/usr/bin/env python3
# =============================================================================
# gen_54_pursuit_heap_two_tongues — 31:22-54
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_54_pursuit_heap_two_tongues.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The pursuit, the search, and the heap of witness in two tongues (31:22-54)"""
from machine import Machine

m = Machine("gen_54_pursuit_heap_two_tongues")

# -------------------------- Gen.31.22 · THE_TOLD_FLIGHT --------------------
# ‹וַיֻּגַּד לְלָבָן בַּיּוֹם› (“and-tell to-Laban in-day”)
# ‹הַשְּׁלִישִׁי כִּי בָרַח› (“the-third that bolt”)
# ‹יַעֲקֹב› (“Jacob”)
# "[EN-AID] And it was told to Laban on the third day that Jacob had fled."
m.step("Gen.31.22")
# ‹וַיֻּגַּד לְלָבָן בַּיּוֹם› (“and-tell to-Laban in-day”)
# ‹הַשְּׁלִישִׁי כִּי בָרַח› (“the-third that bolt”)
# ‹יַעֲקֹב› (“Jacob”)
# — fact holds: hugad-to-Laban-that-bolt-Jacob(day-third)
m.fact("hugad_le_lavan_ki_varach_yaaqov(yom_shelishi)")

# -------------------------- Gen.31.23 · THE_SEVEN_DAY_PURSUIT --------------
# ‹וַיִּקַּח אֶת־אֶחָיו עִמּוֹ› (“and-take obj-marker brother-him/its with-
# him/its”)
# ‹וַיִּרְדֹּף אַחֲרָיו דֶּרֶךְ› (“and-run-after-gone-by) after-him/its
# way/road”)
# ‹שִׁבְעַת יָמִים וַיַּדְבֵּק› (“seven day and-impinge”)
# ‹אֹתוֹ בְּהַר הַגִּלְעָד› (“obj-marker-him/its in-mountain the-Gilead”)
# "[EN-AID] And he took his kinsmen with him and pursued after him a seven
# days' journey, and overtook him in the hill-country of Gilead."
m.step("Gen.31.23")
# ‹וַיִּרְדֹּף אַחֲרָיו דֶּרֶךְ› (“and-run-after-gone-by) after-him/its
# way/road”)
# ‹שִׁבְעַת יָמִים› (“seven day”)
# — fact holds: radaf-and-impinge(Laban, echav, seven-day, mountain-the-
# Gilead)
m.fact("radaf_va_yadbeq(lavan, echav, shivat_yamim, har_ha_gilad)")

# -------------------------- Gen.31.24 · THE_DREAM_GUARD --------------------
# ‹וַיָּבֹא אֱלֹהִים אֶל־לָבָן› (“and-come/bring God to Laban”)
# ‹הָאֲרַמִּי בַּחֲלֹם הַלָּיְלָה› (“the-Aramite in-dream the-night”)
# ‹וַיֹּאמֶר לוֹ הִשָּׁמֶר› (“and-say to-him/its keep/guard”)
# ‹לְךָ פֶּן־תְּדַבֵּר עִם־יַעֲקֹב› (“to-you/your lest speak with Jacob”)
# ‹מִטּוֹב עַד־רָע› (“from-good until bad”)
# "[EN-AID] And God came to Laban the Aramean in a dream of the night and
# said to him: Guard yourself, lest you speak with Jacob from good to bad."
m.step("Gen.31.24")
# ‹הִשָּׁמֶר לְךָ פֶּן־תְּדַבֵּר› (“keep/guard to-you/your lest speak”)
# ‹עִם־יַעֲקֹב מִטּוֹב עַד־רָע› (“with Jacob from-good until bad”)
# — God speaks a demand — LET: keep/guard(Laban, lest-speak-with-Jacob-from-
# good-until-bad)
m.declare("Elohim", "LET",
          "hishamer(lavan, pen_tedaber_im_yaaqov_mi_tov_ad_ra)")
# witness-tier presupposed read:
# prophecy_guard_stated_and_rendered_at_one_verse on a_word_came_by_night —
# read, not installed
m.witness_read("a_word_came_by_night", "prophecy_guard_stated_and_rendered_at_one_verse",
                cites=["Bereshit Rabbah 74:7", "Onkelos Genesis 31:24"])

# -------------------------- Gen.31.25 · THE_TWO_CAMPS ----------------------
# ‹וַיַּשֵּׂג לָבָן אֶת־יַעֲקֹב› (“and-reach Laban obj-marker Jacob”)
# ‹וְיַעֲקֹב תָּקַע אֶת־אָהֳלוֹ› (“and-Jacob clatter obj-marker tent-
# him/its”)
# ‹בָּהָר וְלָבָן תָּקַע› (“in-mountain and-Laban clatter”)
# ‹אֶת־אֶחָיו בְּהַר הַגִּלְעָד› (“with brother-him/its in-mountain the-
# Gilead”)
# "[EN-AID] And Laban caught up with Jacob; and Jacob had pitched his tent
# in the mountain, and Laban with his kinsmen pitched in the hill-country of
# Gilead."
m.step("Gen.31.25")
# ‹וַיַּשֵּׂג לָבָן אֶת־יַעֲקֹב› (“and-reach Laban obj-marker Jacob”)
# — fact holds: clatter-tent-mul-tent(Jacob, Laban, mountain-the-Gilead)
m.fact("taqa_ohel_mul_ohel(yaaqov, lavan, har_ha_gilad)")

# -------------------------- Gen.31.26 · THE_HEART_THEFT_CHARGE -------------
# ‹וַיֹּאמֶר לָבָן לְיַעֲקֹב› (“and-say Laban to-Jacob”)
# ‹מֶה עָשִׂיתָ וַתִּגְנֹב› (“what make and-steal”)
# ‹אֶת־לְבָבִי וַתְּנַהֵג אֶת־בְּנֹתַי› (“obj-marker heart-me/my and-drive-
# forth obj-marker daughter-me/my”)
# ‹כִּשְׁבֻיוֹת חָרֶב› (“like-transport-into-captivity drought”)
# "[EN-AID] And Laban said to Jacob: What have you done, that you stole my
# heart and led away my daughters like captives of the sword?"
m.step("Gen.31.26")
# ‹מֶה עָשִׂיתָ וַתִּגְנֹב› (“what make and-steal”)
# ‹אֶת־לְבָבִי› (“obj-marker heart-me/my”)
# — fact holds: what-make-steal-levavi(Laban, divre-riv)
m.fact("me_asita_ganavta_levavi(lavan, divre_riv)")

# -------------------------- Gen.31.27 · THE_UNPLAYED_BAND ------------------
# ‹לָמָּה נַחְבֵּאתָ לִבְרֹחַ› (“to-what secrete to-bolt”)
# ‹וַתִּגְנֹב אֹתִי וְלֹא־הִגַּדְתָּ› (“and-steal obj-marker-me/my and-not
# tell”)
# ‹לִּי וָאֲשַׁלֵּחֲךָ בְּשִׂמְחָה› (“to-me/my and-send-you/your in-
# blithesomeness”)
# ‹וּבְשִׁרִים בְּתֹף וּבְכִנּוֹר› (“and-in-song in-tambourine and-in-harp”)
# "[EN-AID] Why did you hide yourself to flee, and steal me, and did not
# tell me — I would have sent you away with joy and with songs, with timbrel
# and with lyre —"
m.step("Gen.31.27")
# ‹לָמָּה נַחְבֵּאתָ לִבְרֹחַ› (“to-what secrete to-bolt”)
# ‹וַתִּגְנֹב אֹתִי› (“and-steal obj-marker-me/my”)
# — fact holds: secrete-and-ashalechakha-in-blithesomeness(Laban, irrealis)
m.fact("nachbeta_va_ashalechakha_be_simcha(lavan, irrealis)")

# -------------------------- Gen.31.28 · THE_DENIED_KISS --------------------
# ‹וְלֹא נְטַשְׁתַּנִי לְנַשֵּׁק› (“and-not pound-me/my to-kiss”)
# ‹לְבָנַי וְלִבְנֹתָי עַתָּה› (“to-son-me/my and-to-daughter-me/my now”)
# ‹הִסְכַּלְתָּ עֲשׂוֹ› (“be-silly make”)
# "[EN-AID] And did not allow me to kiss my sons and my daughters? Now you
# have done foolishly."
m.step("Gen.31.28")
# ‹וְלֹא נְטַשְׁתַּנִי לְנַשֵּׁק› (“and-not pound-me/my to-kiss”)
# ‹לְבָנַי וְלִבְנֹתָי› (“to-son-me/my and-to-daughter-me/my”)
# — fact holds: not-netashtani-to-kiss(Laban, be-silly-make)
m.fact("lo_netashtani_le_nasheq(lavan, hiskalta_aso)")

# -------------------------- Gen.31.29 · THE_POWER_AND_THE_RETELL -----------
# ‹יֶשׁ־לְאֵל יָדִי לַעֲשׂוֹת› (“there-is to-God hand-me/my to-make”)
# ‹עִמָּכֶם רָע וֵאלֹהֵי› (“with-you/your(pl) bad and-God”)
# ‹אֲבִיכֶם אֶמֶשׁ אָמַר› (“father-you/your(pl) yesterday say”)
# ‹אֵלַי לֵאמֹר הִשָּׁמֶר› (“to-me/my to-say keep/guard”)
# ‹לְךָ מִדַּבֵּר עִם־יַעֲקֹב› (“to-you/your from-speak with Jacob”)
# ‹מִטּוֹב עַד־רָע› (“from-good until bad”)
# "[EN-AID] It is in the power of my hand to do you all harm; but the God of
# your father last night said to me: Guard yourself from speaking with Jacob
# from good to bad."
m.step("Gen.31.29")
# ‹הִשָּׁמֶר לְךָ מִדַּבֵּר› (“keep/guard to-you/your from-speak”)
# ‹עִם־יַעֲקֹב מִטּוֹב עַד־רָע› (“with Jacob from-good until bad”)
# — fact holds: retell-keep/guard-yesterday(Laban, letter-delta-from-speak)
m.fact("retell_hishamer_emesh(lavan, letter_delta_mi_daber)")

# -------------------------- Gen.31.30 · THE_LONGING_AND_THE_GODS -----------
# ‹וְעַתָּה הָלֹךְ הָלַכְתָּ› (“and-now walk/go walk/go”)
# ‹כִּי־נִכְסֹף נִכְסַפְתָּה לְבֵית› (“that become-pale become-pale to-
# house”)
# ‹אָבִיךָ לָמָּה גָנַבְתָּ› (“father-you/your to-what steal”)
# ‹אֶת־אֱלֹהָי› (“obj-marker God-me/my”)
# "[EN-AID] And now, going you went because longing you longed for your
# father's house — why did you steal my gods?"
m.step("Gen.31.30")
# ‹לָמָּה גָנַבְתָּ אֶת־אֱלֹהָי› (“to-what steal obj-marker God-me/my”)
# — fact holds: lama-steal-obj-marker-elohay(Laban)
m.fact("lama_ganavta_et_elohay(lavan)")

# -------------------------- Gen.31.31 · THE_FEAR_ANSWER --------------------
# ‹וַיַּעַן יַעֲקֹב וַיֹּאמֶר› (“and-eye Jacob and-say”)
# ‹לְלָבָן כִּי יָרֵאתִי› (“to-Laban that fear”)
# ‹כִּי אָמַרְתִּי פֶּן־תִּגְזֹל› (“that say lest pluck-off”)
# ‹אֶת־בְּנוֹתֶיךָ מֵעִמִּי› (“obj-marker daughter-you/your from-with-
# me/my”)
# "[EN-AID] And Jacob answered and said to Laban: Because I was afraid, for
# I said: Lest you tear your daughters away from me."
m.step("Gen.31.31")
# ‹כִּי יָרֵאתִי כִּי› (“that fear that”)
# ‹אָמַרְתִּי› (“say”)
# — fact holds: fear-lest-pluck-off(Jacob)
m.fact("yareti_pen_tigzol(yaaqov)")

# -------------------------- Gen.31.32 · THE_DEATH_OATH_AND_THE_WARRANT -----
# ‹עִם אֲשֶׁר תִּמְצָא› (“with which find”)
# ‹אֶת־אֱלֹהֶיךָ לֹא יִחְיֶה› (“obj-marker God-you/your not live”)
# ‹נֶגֶד אַחֵינוּ הַכֶּר־לְךָ› (“front brother-us/our scrutinize to-
# you/your”)
# ‹מָה עִמָּדִי וְקַח־לָךְ› (“what along-with-me/my and-take to-you/your”)
# ‹וְלֹא־יָדַע יַעֲקֹב כִּי› (“and-not know Jacob that”)
# ‹רָחֵל גְּנָבָתַם› (“Rachel steal-them/their”)
# "[EN-AID] With whomever you find your gods — he shall not live. Before our
# kinsmen, identify what of yours is with me and take it. And Jacob did not
# know that Rachel had stolen them."
m.step("Gen.31.32")
# ‹עִם אֲשֶׁר תִּמְצָא› (“with which find”)
# ‹אֶת־אֱלֹהֶיךָ לֹא יִחְיֶה› (“obj-marker God-you/your not live”)
# — fact holds: with-find-not-live(oath-content)
m.fact("im_timtza_lo_yichye(oath_content)")
# ‹הַכֶּר־לְךָ מָה עִמָּדִי› (“scrutinize to-you/your what along-with-
# me/my”)
# ‹וְקַח־לָךְ› (“and-take to-you/your”)
# — Jacob speaks a demand — LET: scrutinize-and-take(Laban, what-with-me)
m.declare("yaaqov", "LET",
          "haker_ve_qach(lavan, ma_imadi)")
# ‹וְלֹא־יָדַע יַעֲקֹב כִּי› (“and-not know Jacob that”)
# ‹רָחֵל גְּנָבָתַם› (“Rachel steal-them/their”)
# — fact holds: velo-know-Jacob-that-Rachel-genavatam(narrator)
m.fact("velo_yada_yaaqov_ki_rachel_genavatam(narrator)")

# -------------------------- Gen.31.33 · THE_FOUR_TENTS ---------------------
# ‹וַיָּבֹא לָבָן בְּאֹהֶל› (“and-come/bring Laban in-tent”)
# ‹יַעֲקֹב וּבְאֹהֶל לֵאָה› (“Jacob and-in-tent Leah”)
# ‹וּבְאֹהֶל שְׁתֵּי הָאֲמָהֹת› (“and-in-tent two the-maidservant”)
# ‹וְלֹא מָצָא וַיֵּצֵא› (“and-not find and-bring-forth”)
# ‹מֵאֹהֶל לֵאָה וַיָּבֹא› (“from-tent Leah and-come/bring”)
# ‹בְּאֹהֶל רָחֵל› (“in-tent Rachel”)
# "[EN-AID] And Laban came into Jacob's tent and into Leah's tent and into
# the tent of the two maidservants, and did not find; and he went out of
# Leah's tent and came into Rachel's tent."
m.step("Gen.31.33")
# ‹וַיָּבֹא בְּאֹהֶל רָחֵל› (“and-come/bring in-tent Rachel”)
# — fact holds: not-find-rishon(Laban, four-ohalim)
m.fact("lo_matza_rishon(lavan, arba_ohalim)")

# -------------------------- Gen.31.34 · THE_SITTING_ON_THE_GODS ------------
# ‹וְרָחֵל לָקְחָה אֶת־הַתְּרָפִים› (“and-Rachel take obj-marker the-
# Teraphim-a-family-idol”)
# ‹וַתְּשִׂמֵם בְּכַר הַגָּמָל› (“and-put/set-them/their in-ram the-camel”)
# ‹וַתֵּשֶׁב עֲלֵיהֶם וַיְמַשֵּׁשׁ› (“and-dwell/sit over-them/their and-
# feel-of”)
# ‹לָבָן אֶת־כָּל־הָאֹהֶל וְלֹא› (“Laban obj-marker all the-tent and-not”)
# ‹מָצָא› (“find”)
# "[EN-AID] And Rachel had taken the terafim and put them in the camel's
# saddle-cushion and sat upon them. And Laban felt through all the tent and
# did not find."
m.step("Gen.31.34")
# ‹וְרָחֵל לָקְחָה אֶת־הַתְּרָפִים› (“and-Rachel take obj-marker the-
# Teraphim-a-family-idol”)
# — fact holds: and-tesimem-and-dwell/sit-aleihem(Rachel, the-Teraphim-a-
# family-idol)
m.fact("va_tesimem_va_teshev_aleihem(rachel, ha_terafim)")

# -------------------------- Gen.31.35 · THE_WAY_OF_WOMEN_AND_THE_JUSSIVE ---
# ‹וַתֹּאמֶר אֶל־אָבִיהָ אַל־יִחַר› (“and-say to father-her/its do-not
# glow”)
# ‹בְּעֵינֵי אֲדֹנִי כִּי› (“in-eye lord-me/my that”)
# ‹לוֹא אוּכַל לָקוּם› (“not be-able to-arise”)
# ‹מִפָּנֶיךָ כִּי־דֶרֶךְ נָשִׁים› (“from-face-you/your that way/road
# woman”)
# ‹לִי וַיְחַפֵּשׂ וְלֹא› (“to-me/my and-seek and-not”)
# ‹מָצָא אֶת־הַתְּרָפִים› (“find obj-marker the-Teraphim-a-family-idol”)
# "[EN-AID] And she said to her father: Let it not burn in the eyes of my
# lord that I cannot rise before you, for the way of women is upon me. And
# he searched and did not find the terafim."
m.step("Gen.31.35")
# ‹יִחַר בְּעֵינֵי אֲדֹנִי› (“glow in-eye lord-me/my”)
# — Rachel speaks a demand — LET-NOT: glow(in-eye-adoni)
m.declare("rachel", "LET-NOT",
          "yichar(be_ene_adoni)")
# ‹וַיְחַפֵּשׂ וְלֹא מָצָא› (“and-seek and-not find”)
# ‹אֶת› (“obj-marker”)
# — fact holds: not-find-obj-marker-the-Teraphim-a-family-idol(Laban, sof-
# chipus)
m.fact("lo_matza_et_ha_terafim(lavan, sof_chipus)")

# -------------------------- Gen.31.36 · THE_BURN_LANDS_WRONG ---------------
# ‹וַיִּחַר לְיַעֲקֹב וַיָּרֶב› (“and-glow to-Jacob and-toss”)
# ‹בְּלָבָן וַיַּעַן יַעֲקֹב› (“in-Laban and-eye Jacob”)
# ‹וַיֹּאמֶר לְלָבָן מַה־פִּשְׁעִי› (“and-say to-Laban what revolt-me/my”)
# ‹מַה חַטָּאתִי כִּי› (“what sin-offering-me/my that”)
# ‹דָלַקְתָּ אַחֲרָי› (“flame after-me/my”)
# "[EN-AID] And it burned for Jacob, and he quarreled with Laban; and Jacob
# answered and said to Laban: What is my transgression, what is my sin, that
# you have hotly pursued after me?"
m.step("Gen.31.36")
# ‹וַיִּחַר לְיַעֲקֹב וַיָּרֶב› (“and-glow to-Jacob and-toss”)
# ‹בְּלָבָן› (“in-Laban”)
# — fact holds: and-glow-to-Jacob(the-charon-in-the-enayim-acherot)
m.fact("va_yichar_le_yaaqov(ha_charon_ba_enayim_acherot)")
# witness-tier presupposed read: audited_and_found_to_contain_appeasement on
# the_quarrel — read, not installed
m.witness_read("the_quarrel", "audited_and_found_to_contain_appeasement",
                cites=["Bereshit Rabbah 74:10"])

# -------------------------- Gen.31.37 · THE_TRIBUNAL_DEMAND ----------------
# ‹כִּי־מִשַּׁשְׁתָּ אֶת־כָּל־כֵּלַי מַה־מָּצָאתָ› (“that feel-of obj-marker
# all vessel-me/my what find”)
# ‹מִכֹּל כְּלֵי־בֵיתֶךָ שִׂים› (“from-all vessel house-you/your put/set”)
# ‹כֹּה נֶגֶד אַחַי› (“like-this front brother-me/my”)
# ‹וְאַחֶיךָ וְיוֹכִיחוּ בֵּין› (“and-brother-you/your and-be-right
# between”)
# ‹שְׁנֵינוּ› (“two-us/our”)
# "[EN-AID] For you have felt through all my vessels — what have you found
# of all your house's vessels? Set it here before my kinsmen and your
# kinsmen, and let them decide between the two of us."
m.step("Gen.31.37")
# ‹שִׂים כֹּה נֶגֶד› (“put/set like-this front”)
# ‹אַחַי וְאַחֶיךָ› (“brother-me/my and-brother-you/your”)
# — Jacob speaks a demand — LET: put/set(Laban, this-front-achai-and-
# achekha)
m.declare("yaaqov", "LET",
          "sim(lavan, ko_neged_achai_ve_achekha)")

# -------------------------- Gen.31.38 · THE_AUDIT_OPENS --------------------
# ‹זֶה עֶשְׂרִים שָׁנָה› (“this twenty years”)
# ‹אָנֹכִי עִמָּךְ רְחֵלֶיךָ› (“with-you/your ewe-you/your”)
# ‹וְעִזֶּיךָ לֹא שִׁכֵּלוּ› (“and-she-goat-you/your not miscarry”)
# ‹וְאֵילֵי צֹאנְךָ לֹא› (“and-ram flock-you/your not”)
# ‹אָכָלְתִּי› (“eat”)
# "[EN-AID] These twenty years I have been with you: your ewes and your she-
# goats have not miscarried, and the rams of your flock I have not eaten."
m.step("Gen.31.38")
# ‹זֶה עֶשְׂרִים שָׁנָה› (“this twenty years”)
# ‹אָנֹכִי עִמָּךְ› (“with-you/your”)
# — fact holds: twenty-years-not-miscarry(Jacob, cheshbon)
m.fact("esrim_shana_lo_shikelu(yaaqov, cheshbon)")
# witness-tier presupposed read: day_old_ram on ve_eilei_tzonkha — read, not
# installed
m.witness_read("ve_eilei_tzonkha", "day_old_ram",
                cites=["Bava Kamma 65b:17", "Bava Kamma 65b:18", "Bava Kamma 65b:19"])

# -------------------------- Gen.31.39 · THE_SHEPHERD_LAW_SEED --------------
# ‹טְרֵפָה לֹא־הֵבֵאתִי אֵלֶיךָ› (“prey not come/bring to-you/your”)
# ‹אָנֹכִי אֲחַטֶּנָּה מִיָּדִי› (“sin-her/its from-hand-me/my”)
# ‹תְּבַקְשֶׁנָּה גְּנֻבְתִי יוֹם› (“search-out-her/its steal day”)
# ‹וּגְנֻבְתִי לָיְלָה› (“and-steal night”)
# "[EN-AID] A torn animal I did not bring you — I bore its loss; from my
# hand you would seek it, stolen by day or stolen by night."
m.step("Gen.31.39")
# ‹טְרֵפָה לֹא־הֵבֵאתִי אֵלֶיךָ› (“prey not come/bring to-you/your”)
# — fact holds: prey-anokhi-achatena(Jacob, cheshbon)
m.fact("terefa_anokhi_achatena(yaaqov, cheshbon)")
# witness-tier presupposed read: refiled_under_the_bailment_statutes on
# the_shepherds_defence — read, not installed
m.witness_read("the_shepherds_defence", "refiled_under_the_bailment_statutes",
                cites=["Onkelos Genesis 31:39"])

# -------------------------- Gen.31.40 · THE_HEAT_AND_THE_FROST -------------
# ‹הָיִיתִי בַיּוֹם אֲכָלַנִי› (“be in-day eat-me/my”)
# ‹חֹרֶב וְקֶרַח בַּלָּיְלָה› (“drought and-ice in-night”)
# ‹וַתִּדַּד שְׁנָתִי מֵעֵינָי› (“and-wave-to-and-fro sleep-me/my from-eye-
# me/my”)
# "[EN-AID] I was: by day heat consumed me, and frost by night; and my sleep
# fled from my eyes."
m.step("Gen.31.40")
# ‹הָיִיתִי בַיּוֹם אֲכָלַנִי› (“be in-day eat-me/my”)
# ‹חֹרֶב וְקֶרַח בַּלָּיְלָה› (“drought and-ice in-night”)
# — fact holds: drought-ice-nadad-shena(Jacob, cheshbon)
m.fact("chorev_qerach_nadad_shena(yaaqov, cheshbon)")
# witness-tier presupposed read: keeper_ceiling on akhalani_chorev_va_kerach
# — read, not installed
m.witness_read("akhalani_chorev_va_kerach", "keeper_ceiling",
                cites=["Bava Metzia 93b:2", "Bava Metzia 93b:3", "Bava Metzia 93b:4"])

# -------------------------- Gen.31.41 · THE_TWENTY_YEARS_LEDGER ------------
# ‹זֶה־לִּי עֶשְׂרִים שָׁנָה› (“this to-me/my twenty years”)
# ‹בְּבֵיתֶךָ עֲבַדְתִּיךָ אַרְבַּע־עֶשְׂרֵה› (“in-house-you/your
# work/serve-you/your four -teen”)
# ‹שָׁנָה בִּשְׁתֵּי בְנֹתֶיךָ› (“years in-two daughter-you/your”)
# ‹וְשֵׁשׁ שָׁנִים בְּצֹאנֶךָ› (“and-six years in-flock-you/your”)
# ‹וַתַּחֲלֵף אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת› (“and-slide-by obj-marker wages-
# me/my ten”)
# ‹מֹנִים› (“something-weighed-out”)
# "[EN-AID] These twenty years I have been in your house: I served you
# fourteen years for your two daughters and six years for your flock, and
# you changed my wages ten countings."
m.step("Gen.31.41")
# ‹וַתַּחֲלֵף אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת› (“and-slide-by obj-marker wages-
# me/my ten”)
# ‹מֹנִים› (“something-weighed-out”)
# — fact holds: four--teen-and-six-ten-something-weighed-out(Jacob,
# cheshbon)
m.fact("arba_esre_ve_shesh_aseret_monim(yaaqov, cheshbon)")

# -------------------------- Gen.31.42 · THE_ADJUDICATION_ALREADY_HELD ------
# ‹לוּלֵי אֱלֹהֵי אָבִי› (“if-not God father-me/my”)
# ‹אֱלֹהֵי אַבְרָהָם וּפַחַד› (“God Abraham and-alarm”)
# ‹יִצְחָק הָיָה לִי› (“Isaac be to-me/my”)
# ‹כִּי עַתָּה רֵיקָם› (“that now emptily”)
# ‹שִׁלַּחְתָּנִי אֶת־עָנְיִי וְאֶת־יְגִיעַ› (“send-me/my obj-marker
# affliction-me/my and-obj-marker toil”)
# ‹כַּפַּי רָאָה אֱלֹהִים› (“palm-of-hand-us/our see God”)
# ‹וַיּוֹכַח אָמֶשׁ› (“and-be-right yesterday”)
# "[EN-AID] Were it not that the God of my father — the God of Abraham and
# the Fear of Isaac — was for me, now you would have sent me away empty. My
# affliction and the toil of my palms God has seen — and he adjudicated last
# night."
m.step("Gen.31.42")
# ‹לוּלֵי אֱלֹהֵי אָבִי› (“if-not God father-me/my”)
# ‹אֱלֹהֵי אַבְרָהָם וּפַחַד› (“God Abraham and-alarm”)
# ‹יִצְחָק› (“Isaac”)
# — fact holds: if-not-God-avi-and-alarm-Isaac(Jacob)
m.fact("lule_elohe_avi_u_fachad_yitzchaq(yaaqov)")
# ‹וַיּוֹכַח אָמֶשׁ› (“and-be-right yesterday”)
# — fact holds: see-God-and-be-right-yesterday(landing-put/set-tribunal)
m.fact("raa_Elohim_va_yokhach_amesh(landing_sim_tribunal)")
# witness-grounded state (its own tier):
# ranked_above_the_merit_of_the_fathers on labour
m.witness_state("labour", "ranked_above_the_merit_of_the_fathers",
                cites=["Bereshit Rabbah 74:12"])
# witness-tier presupposed read: flagged_uncertain_by_the_transmitter on
# the_attribution — read, not installed
m.witness_read("the_attribution", "flagged_uncertain_by_the_transmitter",
                cites=["Bereshit Rabbah 74:12"])

# -------------------------- Gen.31.43 · THE_EVERYTHING_IS_MINE -------------
# ‹וַיַּעַן לָבָן וַיֹּאמֶר› (“and-eye Laban and-say”)
# ‹אֶל־יַעֲקֹב הַבָּנוֹת בְּנֹתַי› (“to Jacob the-daughter daughter-me/my”)
# ‹וְהַבָּנִים בָּנַי וְהַצֹּאן› (“and-the-son son-me/my and-the-flock”)
# ‹צֹאנִי וְכֹל אֲשֶׁר־אַתָּה› (“flock-me/my and-all which you”)
# ‹רֹאֶה לִי־הוּא וְלִבְנֹתַי› (“see to-me/my he/it and-to-daughter-me/my”)
# ‹מָה־אֶעֱשֶׂה לָאֵלֶּה הַיּוֹם› (“what make to-these the-day”)
# ‹אוֹ לִבְנֵיהֶן אֲשֶׁר› (“or to-son-them/their which”)
# ‹יָלָדוּ› (“bear-young”)
# "[EN-AID] And Laban answered and said to Jacob: The daughters are my
# daughters and the sons are my sons and the flock is my flock, and all that
# you see — it is mine. And for my daughters, what can I do for these today,
# or for their sons whom they have borne?"
m.step("Gen.31.43")
# ‹וְכֹל אֲשֶׁר־אַתָּה רֹאֶה› (“and-all which you see”)
# ‹לִי־הוּא› (“to-me/my he/it”)
# — fact holds: the-all-to-me-he/it-and-what-make(Laban)
m.fact("ha_kol_li_hu_u_ma_eese(lavan)")
# witness-tier presupposed read: all_four_mothers_one_house on
# my_daughters_doubled — read, not installed
m.witness_read("my_daughters_doubled", "all_four_mothers_one_house",
                cites=["Bereshit Rabbah 74:13"])

# -------------------------- Gen.31.44 · THE_COVENANT_COHORTATIVE -----------
# ‹וְעַתָּה לְכָה נִכְרְתָה› (“and-now go-ward cut”)
# ‹בְרִית אֲנִי וָאָתָּה› (“covenant and-you”)
# ‹וְהָיָה לְעֵד בֵּינִי› (“and-be to-concretely between-me/my”)
# ‹וּבֵינֶךָ› (“and-between-you/your”)
# "[EN-AID] And now, come, let us cut a covenant, I and you; and let it be
# for a witness between me and you."
m.step("Gen.31.44")
# ‹וְעַתָּה לְכָה נִכְרְתָה› (“and-now go-ward cut”)
# ‹בְרִית אֲנִי וָאָתָּה› (“covenant and-you”)
# — Laban speaks a demand — CMD-US?: nikhreta(covenant-ani-and-now)
m.declare("lavan", "CMD-US?",
          "nikhreta(verit_ani_va_ata)")

# -------------------------- Gen.31.45 · THE_STONE_RAISED -------------------
# ‹וַיִּקַּח יַעֲקֹב אָבֶן› (“and-take Jacob stone”)
# ‹וַיְרִימֶהָ מַצֵּבָה› (“and-rise-high-her/its pillar”)
# "[EN-AID] And Jacob took a stone and raised it up as a pillar."
m.step("Gen.31.45")
# ‹וַיִּקַּח יַעֲקֹב אָבֶן› (“and-take Jacob stone”)
# ‹וַיְרִימֶהָ מַצֵּבָה› (“and-rise-high-her/its pillar”)
# — the world gains: the-pillar
m.install("ha_matzeva")

# -------------------------- Gen.31.46 · THE_HEAP_AND_THE_WRONG_VERB --------
# ‹וַיֹּאמֶר יַעֲקֹב לְאֶחָיו› (“and-say Jacob to-brother-him/its”)
# ‹לִקְטוּ אֲבָנִים וַיִּקְחוּ› (“pick-up stone and-take”)
# ‹אֲבָנִים וַיַּעֲשׂוּ־גָל וַיֹּאכְלוּ› (“stone and-make something-rolled
# and-eat”)
# ‹שָׁם עַל־הַגָּל› (“there over the-something-rolled”)
# "[EN-AID] And Jacob said to his kinsmen: Gather stones! And they took
# stones and made a heap, and they ate there upon the heap."
m.step("Gen.31.46")
# ‹לִקְטוּ אֲבָנִים› (“pick-up stone”)
# — Jacob speaks a demand — LET: pick-up(echav, stone)
m.declare("yaaqov", "LET",
          "liqtu(echav, avanim)")
# ‹וַיִּקְחוּ אֲבָנִים וַיַּעֲשׂוּ־גָל› (“and-take stone and-make something-
# rolled”)
# — the world gains: the-something-rolled
m.install("ha_gal")

# -------------------------- Gen.31.47 · THE_TWO_TONGUES --------------------
# ‹וַיִּקְרָא־לוֹ לָבָן יְגַר› (“and-call to-him/its Laban Jegar-Sahadutha”)
# ‹שָׂהֲדוּתָא וְיַעֲקֹב קָרָא› (“Jegar-Sahadutha and-Jacob call”)
# ‹לוֹ גַּלְעֵד› (“to-him/its Galeed”)
# "[EN-AID] And Laban called it Yegar-Sahaduta [heap of witness, in
# Aramaic], and Jacob called it Galed [heap of witness, in Hebrew]."
m.step("Gen.31.47")
# ‹וַיִּקְרָא־לוֹ לָבָן יְגַר› (“and-call to-him/its Laban Jegar-Sahadutha”)
# ‹שָׂהֲדוּתָא› (“Jegar-Sahadutha”)
# — named: the-something-rolled := Jegar-Sahadutha-Jegar-Sahadutha
m.name("ha_gal", "yegar_sahaduta")
# ‹וְיַעֲקֹב קָרָא לוֹ› (“and-Jacob call to-him/its”)
# ‹גַּלְעֵד› (“Galeed”)
# — named: the-something-rolled := Galeed
m.name("ha_gal", "galed")
# witness-tier presupposed read: one_member_honouring_the_others_language on
# the_two_names — read, not installed
m.witness_read("the_two_names", "one_member_honouring_the_others_language",
                cites=["Bereshit Rabbah 74:14"])

# -------------------------- Gen.31.48 · THE_ETIOLOGY_REPORT ----------------
# ‹וַיֹּאמֶר לָבָן הַגַּל› (“and-say Laban the-something-rolled”)
# ‹הַזֶּה עֵד בֵּינִי› (“the-this concretely between-me/my”)
# ‹וּבֵינְךָ הַיּוֹם עַל־כֵּן› (“and-between-you/your the-day over so”)
# ‹קָרָא־שְׁמוֹ גַּלְעֵד› (“call name-him/its Galeed”)
# "[EN-AID] And Laban said: This heap is witness between me and you today.
# Therefore its name was called Galed,"
m.step("Gen.31.48")
# ‹עַל־כֵּן קָרָא־שְׁמוֹ גַּלְעֵד› (“over so call name-him/its Galeed”)
# — fact holds: the-something-rolled-concretely-over-so-Galeed(report-only)
m.fact("ha_gal_ed_al_ken_galed(report_only)")

# -------------------------- Gen.31.49 · THE_WATCHPOST_PRAYER ---------------
# ‹וְהַמִּצְפָּה אֲשֶׁר אָמַר› (“and-the-Mitspah which say”)
# ‹יִצֶף יְהוָה בֵּינִי› (“lean-forward YHWH between-me/my”)
# ‹וּבֵינֶךָ כִּי נִסָּתֵר› (“and-between-you/your that hide”)
# ‹אִישׁ מֵרֵעֵהוּ› (“man from-associate-him/its”)
# "[EN-AID] And the Mitzpah [watchpost], because he said: May YHWH watch
# between me and you when we are hidden each from his fellow."
m.step("Gen.31.49")
# ‹יִצֶף יְהוָה בֵּינִי› (“lean-forward YHWH between-me/my”)
# ‹וּבֵינֶךָ› (“and-between-you/your”)
# — Laban speaks a demand — LET: lean-forward(the-LORD, beni-and-venekha)
m.declare("lavan", "LET",
          "yitzef(YHWH, beni_u_venekha)")
# witness-tier presupposed read: both_routed_through_the_word on
# the_watch_and_the_witness — read, not installed
m.witness_read("the_watch_and_the_witness", "both_routed_through_the_word",
                cites=["Onkelos Genesis 31:49", "Onkelos Genesis 31:50"])

# -------------------------- Gen.31.50 · THE_TERMS_AND_THE_SEE --------------
# ‹אִם־תְּעַנֶּה אֶת־בְּנֹתַי וְאִם־תִּקַּח› (“if afflict-literally obj-
# marker daughter-me/my and-if take”)
# ‹נָשִׁים עַל־בְּנֹתַי אֵין› (“woman over daughter-me/my there-is-not”)
# ‹אִישׁ עִמָּנוּ רְאֵה› (“man with-us/our see”)
# ‹אֱלֹהִים עֵד בֵּינִי› (“God concretely between-me/my”)
# ‹וּבֵינֶךָ› (“and-between-you/your”)
# "[EN-AID] If you afflict my daughters, and if you take wives over my
# daughters — no man is with us; see, God is witness between me and you."
m.step("Gen.31.50")
# ‹רְאֵה אֱלֹהִים עֵד› (“see God concretely”)
# ‹בֵּינִי וּבֵינֶךָ› (“between-me/my and-between-you/your”)
# — fact holds: with-afflict-literally-with-take-oath-content(Laban)
m.fact("im_teane_im_tiqach_oath_content(lavan)")
# witness-tier presupposed read: family_law_partitioning_time on
# the_two_clauses — read, not installed
m.witness_read("the_two_clauses", "family_law_partitioning_time",
                cites=["Bereshit Rabbah 74:14"])
# witness-tier presupposed read: affliction_token on im_teane_et_benotai —
# read, not installed
m.witness_read("im_teane_et_benotai", "affliction_token",
                cites=["Yoma 77a:13", "Yoma 77a:14"])

# -------------------------- Gen.31.51 · THE_CLAIMED_CASTER -----------------
# ‹וַיֹּאמֶר לָבָן לְיַעֲקֹב› (“and-say Laban to-Jacob”)
# ‹הִנֵּה הַגַּל הַזֶּה› (“behold the-something-rolled the-this”)
# ‹וְהִנֵּה הַמַצֵּבָה אֲשֶׁר› (“and-behold the-pillar which”)
# ‹יָרִיתִי בֵּינִי וּבֵינֶךָ› (“flow-as-water between-me/my and-between-
# you/your”)
# "[EN-AID] And Laban said to Jacob: Behold this heap and behold the pillar
# which I have cast between me and you."
m.step("Gen.31.51")
# ‹הִנֵּה הַגַּל הַזֶּה› (“behold the-something-rolled the-this”)
# ‹וְהִנֵּה הַמַצֵּבָה› (“and-behold the-pillar”)
# — fact holds: behold-the-something-rolled-and-the-pillar-flow-as-
# water(Laban)
m.fact("hine_ha_gal_ve_ha_matzeva_yariti(lavan)")

# -------------------------- Gen.31.52 · THE_BOUNDARY_OATH ------------------
# ‹עֵד הַגַּל הַזֶּה› (“concretely the-something-rolled the-this”)
# ‹וְעֵדָה הַמַּצֵּבָה אִם־אָנִי› (“and-testimony the-pillar if”)
# ‹לֹא־אֶעֱבֹר אֵלֶיךָ אֶת־הַגַּל› (“not pass-over to-you/your obj-marker
# the-something-rolled”)
# ‹הַזֶּה וְאִם־אַתָּה לֹא־תַעֲבֹר› (“the-this and-if you not pass-over”)
# ‹אֵלַי אֶת־הַגַּל הַזֶּה› (“to-me/my obj-marker the-something-rolled the-
# this”)
# ‹וְאֶת־הַמַּצֵּבָה הַזֹּאת לְרָעָה› (“and-obj-marker the-pillar the-this
# to-bad”)
# "[EN-AID] Witness is this heap and witness the pillar: that I will not
# pass beyond this heap to you, and that you will not pass beyond this heap
# and this pillar to me, for harm."
m.step("Gen.31.52")
# ‹עֵד הַגַּל הַזֶּה› (“concretely the-something-rolled the-this”)
# ‹וְעֵדָה הַמַּצֵּבָה› (“and-testimony the-pillar”)
# — fact holds: concretely-the-something-rolled-and-testimony-the-pillar-
# not-naavor(oath-content)
m.fact("ed_ha_gal_ve_eda_ha_matzeva_lo_naavor(oath_content)")
# witness-tier presupposed read: carve_out_and_a_legal_afterlife_in_court on
# the_boundary — read, not installed
m.witness_read("the_boundary", "carve_out_and_a_legal_afterlife_in_court",
                cites=["Bereshit Rabbah 74:15"])

# -------------------------- Gen.31.53 · THE_OATH_BY_THE_FEAR ---------------
# ‹אֱלֹהֵי אַבְרָהָם וֵאלֹהֵי› (“God Abraham and-God”)
# ‹נָחוֹר יִשְׁפְּטוּ בֵינֵינוּ› (“Nahor judge between-us/our”)
# ‹אֱלֹהֵי אֲבִיהֶם וַיִּשָּׁבַע› (“God father-them/their and-swear”)
# ‹יַעֲקֹב בְּפַחַד אָבִיו› (“Jacob in-alarm father-him/its”)
# ‹יִצְחָק› (“Isaac”)
# "[EN-AID] The God of Abraham and the god of Nahor judge between us — the
# god of their father. And Jacob swore by the Fear of his father Isaac."
m.step("Gen.31.53")
# ‹אֱלֹהֵי אַבְרָהָם וֵאלֹהֵי› (“God Abraham and-God”)
# ‹נָחוֹר יִשְׁפְּטוּ› (“Nahor judge”)
# — fact holds: judge-imperfect-fenced(God-Abraham-and-God-Nahor)
m.fact("yishptu_imperfect_fenced(elohe_avraham_ve_lohe_nachor)")
# ‹וַיִּשָּׁבַע יַעֲקֹב בְּפַחַד› (“and-swear Jacob in-alarm”)
# ‹אָבִיו יִצְחָק› (“father-him/its Isaac”)
# — fact holds: and-swear-Jacob-in-alarm-aviv(other-root-performance)
m.fact("va_yishava_yaaqov_be_fachad_aviv(other_root_performance)")
# witness-tier presupposed read: graded_sacred_profane_and_both on
# the_oath_formula — read, not installed
m.witness_read("the_oath_formula", "graded_sacred_profane_and_both",
                cites=["Bereshit Rabbah 74:16", "Onkelos Genesis 31:53"])

# -------------------------- Gen.31.54 · THE_FIRST_SACRIFICE ----------------
# ‹וַיִּזְבַּח יַעֲקֹב זֶבַח› (“and-slaughter-an-animal Jacob sacrifice”)
# ‹בָּהָר וַיִּקְרָא לְאֶחָיו› (“in-mountain and-call to-brother-him/its”)
# ‹לֶאֱכָל־לָחֶם וַיֹּאכְלוּ לֶחֶם› (“to-eat food and-eat food”)
# ‹וַיָּלִינוּ בָּהָר› (“and-stop in-mountain”)
# "[EN-AID] And Jacob sacrificed a sacrifice on the mountain and called his
# kinsmen to eat bread; and they ate bread and lodged on the mountain."
m.step("Gen.31.54")
# ‹וַיִּזְבַּח יַעֲקֹב זֶבַח› (“and-slaughter-an-animal Jacob sacrifice”)
# ‹בָּהָר› (“in-mountain”)
# — fact holds: and-slaughter-an-animal-sacrifice-and-eat-and-stop(Jacob,
# echav, mountain)
m.fact("va_yizbach_zevach_va_yokhlu_va_yalinu(yaaqov, echav, ba_har)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ha_gal', 'ha_matzeva'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha_gal': 'galed'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['hishamer(lavan, pen_tedaber_im_yaaqov_mi_tov_ad_ra)', 'haker_ve_qach(lavan, ma_imadi)', 'yichar(be_ene_adoni)', 'sim(lavan, ko_neged_achai_ve_achekha)', 'nikhreta(verit_ani_va_ata)', 'liqtu(echav, avanim)', 'yitzef(YHWH, beni_u_venekha)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['hugad_le_lavan_ki_varach_yaaqov(yom_shelishi)', 'radaf_va_yadbeq(lavan, echav, shivat_yamim, har_ha_gilad)', 'taqa_ohel_mul_ohel(yaaqov, lavan, har_ha_gilad)', 'me_asita_ganavta_levavi(lavan, divre_riv)', 'nachbeta_va_ashalechakha_be_simcha(lavan, irrealis)', 'lo_netashtani_le_nasheq(lavan, hiskalta_aso)', 'retell_hishamer_emesh(lavan, letter_delta_mi_daber)', 'lama_ganavta_et_elohay(lavan)', 'yareti_pen_tigzol(yaaqov)', 'im_timtza_lo_yichye(oath_content)', 'velo_yada_yaaqov_ki_rachel_genavatam(narrator)', 'lo_matza_rishon(lavan, arba_ohalim)', 'va_tesimem_va_teshev_aleihem(rachel, ha_terafim)', 'lo_matza_et_ha_terafim(lavan, sof_chipus)', 'va_yichar_le_yaaqov(ha_charon_ba_enayim_acherot)', 'esrim_shana_lo_shikelu(yaaqov, cheshbon)', 'terefa_anokhi_achatena(yaaqov, cheshbon)', 'chorev_qerach_nadad_shena(yaaqov, cheshbon)', 'arba_esre_ve_shesh_aseret_monim(yaaqov, cheshbon)', 'lule_elohe_avi_u_fachad_yitzchaq(yaaqov)', 'raa_Elohim_va_yokhach_amesh(landing_sim_tribunal)', 'ha_kol_li_hu_u_ma_eese(lavan)', 'ha_gal_ed_al_ken_galed(report_only)', 'im_teane_im_tiqach_oath_content(lavan)', 'hine_ha_gal_ve_ha_matzeva_yariti(lavan)', 'ed_ha_gal_ve_eda_ha_matzeva_lo_naavor(oath_content)', 'yishptu_imperfect_fenced(elohe_avraham_ve_lohe_nachor)', 'va_yishava_yaaqov_be_fachad_aviv(other_root_performance)', 'va_yizbach_zevach_va_yokhlu_va_yalinu(yaaqov, echav, ba_har)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    assert sorted(m.WORLD["witnessed"]) == ['labour']
    assert m.WORLD["witnessed"]['labour']["cites"] == ['Bereshit Rabbah 74:12']
    assert all('ranked_above_the_merit_of_the_fathers' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('a_word_came_by_night', 'prophecy_guard_stated_and_rendered_at_one_verse'), ('the_quarrel', 'audited_and_found_to_contain_appeasement'), ('ve_eilei_tzonkha', 'day_old_ram'), ('the_shepherds_defence', 'refiled_under_the_bailment_statutes'), ('akhalani_chorev_va_kerach', 'keeper_ceiling'), ('the_attribution', 'flagged_uncertain_by_the_transmitter'), ('my_daughters_doubled', 'all_four_mothers_one_house'), ('the_two_names', 'one_member_honouring_the_others_language'), ('the_watch_and_the_witness', 'both_routed_through_the_word'), ('the_two_clauses', 'family_law_partitioning_time'), ('im_teane_et_benotai', 'affliction_token'), ('the_boundary', 'carve_out_and_a_legal_afterlife_in_court'), ('the_oath_formula', 'graded_sacred_profane_and_both')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 74:7', 'Onkelos Genesis 31:24']
    assert all('prophecy_guard_stated_and_rendered_at_one_verse' not in f for f in m.WORLD["facts"])
    assert 'a_word_came_by_night' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 74:10']
    assert all('audited_and_found_to_contain_appeasement' not in f for f in m.WORLD["facts"])
    assert 'the_quarrel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bava Kamma 65b:17', 'Bava Kamma 65b:18', 'Bava Kamma 65b:19']
    assert all('day_old_ram' not in f for f in m.WORLD["facts"])
    assert 've_eilei_tzonkha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Onkelos Genesis 31:39']
    assert all('refiled_under_the_bailment_statutes' not in f for f in m.WORLD["facts"])
    assert 'the_shepherds_defence' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bava Metzia 93b:2', 'Bava Metzia 93b:3', 'Bava Metzia 93b:4']
    assert all('keeper_ceiling' not in f for f in m.WORLD["facts"])
    assert 'akhalani_chorev_va_kerach' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 74:12']
    assert all('flagged_uncertain_by_the_transmitter' not in f for f in m.WORLD["facts"])
    assert 'the_attribution' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 74:13']
    assert all('all_four_mothers_one_house' not in f for f in m.WORLD["facts"])
    assert 'my_daughters_doubled' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 74:14']
    assert all('one_member_honouring_the_others_language' not in f for f in m.WORLD["facts"])
    assert 'the_two_names' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Onkelos Genesis 31:49', 'Onkelos Genesis 31:50']
    assert all('both_routed_through_the_word' not in f for f in m.WORLD["facts"])
    assert 'the_watch_and_the_witness' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 74:14']
    assert all('family_law_partitioning_time' not in f for f in m.WORLD["facts"])
    assert 'the_two_clauses' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Yoma 77a:13', 'Yoma 77a:14']
    assert all('affliction_token' not in f for f in m.WORLD["facts"])
    assert 'im_teane_et_benotai' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 74:15']
    assert all('carve_out_and_a_legal_afterlife_in_court' not in f for f in m.WORLD["facts"])
    assert 'the_boundary' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 74:16', 'Onkelos Genesis 31:53']
    assert all('graded_sacred_profane_and_both' not in f for f in m.WORLD["facts"])
    assert 'the_oath_formula' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
