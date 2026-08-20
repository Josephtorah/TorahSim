#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיֻּגַּד לְלָבָן בַּיּוֹם הַשְּׁלִישִׁי כִּי בָרַח יַעֲקֹב
# "[EN-AID] And it was told to Laban on the third day that Jacob had fled."
m.step("Gen.31.22")
# ‹וַיֻּגַּד לְלָבָן בַּיּוֹם הַשְּׁלִישִׁי כִּי בָרַח יַעֲקֹב› (“and-tell
# to-Laban in-day the-third that bolt Jacob”) — fact holds: hugad-to-Laban-
# that-bolt-Jacob(day-third)
m.fact("hugad_le_lavan_ki_varach_yaaqov(yom_shelishi)")

# -------------------------- Gen.31.23 · THE_SEVEN_DAY_PURSUIT --------------
# וַיִּקַּח אֶת־אֶחָיו עִמּוֹ וַיִּרְדֹּף אַחֲרָיו דֶּרֶךְ שִׁבְעַת יָמִים
# וַיַּדְבֵּק אֹתוֹ בְּהַר הַגִּלְעָד
# "[EN-AID] And he took his kinsmen with him and pursued after him a seven
# days' journey, and overtook him in the hill-country of Gilead."
m.step("Gen.31.23")
# ‹וַיִּרְדֹּף אַחֲרָיו דֶּרֶךְ שִׁבְעַת יָמִים› (“and-run-after-gone-by)
# after-him/its way/road seven day”) — fact holds: radaf-and-impinge(Laban,
# echav, seven-day, mountain-the-Gilead)
m.fact("radaf_va_yadbeq(lavan, echav, shivat_yamim, har_ha_gilad)")

# -------------------------- Gen.31.24 · THE_DREAM_GUARD --------------------
# וַיָּבֹא אֱלֹהִים אֶל־לָבָן הָאֲרַמִּי בַּחֲלֹם הַלָּיְלָה וַיֹּאמֶר לוֹ
# הִשָּׁמֶר לְךָ פֶּן־תְּדַבֵּר עִם־יַעֲקֹב מִטּוֹב עַד־רָע
# "[EN-AID] And God came to Laban the Aramean in a dream of the night and
# said to him: Guard yourself, lest you speak with Jacob from good to bad."
m.step("Gen.31.24")
# ‹הִשָּׁמֶר לְךָ פֶּן־תְּדַבֵּר עִם־יַעֲקֹב מִטּוֹב עַד־רָע› (“keep/guard
# to-you/your lest speak with Jacob from-good until bad”) — God speaks a
# demand — LET: keep/guard(Laban, lest-speak-with-Jacob-from-good-until-bad)
m.declare("Elohim", "LET",
          "hishamer(lavan, pen_tedaber_im_yaaqov_mi_tov_ad_ra)")

# -------------------------- Gen.31.25 · THE_TWO_CAMPS ----------------------
# וַיַּשֵּׂג לָבָן אֶת־יַעֲקֹב וְיַעֲקֹב תָּקַע אֶת־אָהֳלוֹ בָּהָר וְלָבָן
# תָּקַע אֶת־אֶחָיו בְּהַר הַגִּלְעָד
# "[EN-AID] And Laban caught up with Jacob; and Jacob had pitched his tent
# in the mountain, and Laban with his kinsmen pitched in the hill-country of
# Gilead."
m.step("Gen.31.25")
# ‹וַיַּשֵּׂג לָבָן אֶת־יַעֲקֹב› (“and-reach Laban obj-marker Jacob”) — fact
# holds: clatter-tent-mul-tent(Jacob, Laban, mountain-the-Gilead)
m.fact("taqa_ohel_mul_ohel(yaaqov, lavan, har_ha_gilad)")

# -------------------------- Gen.31.26 · THE_HEART_THEFT_CHARGE -------------
# וַיֹּאמֶר לָבָן לְיַעֲקֹב מֶה עָשִׂיתָ וַתִּגְנֹב אֶת־לְבָבִי וַתְּנַהֵג
# אֶת־בְּנֹתַי כִּשְׁבֻיוֹת חָרֶב
# "[EN-AID] And Laban said to Jacob: What have you done, that you stole my
# heart and led away my daughters like captives of the sword?"
m.step("Gen.31.26")
# ‹מֶה עָשִׂיתָ וַתִּגְנֹב אֶת־לְבָבִי› (“what make and-steal obj-marker
# heart-me/my”) — fact holds: what-make-steal-levavi(Laban, divre-riv)
m.fact("me_asita_ganavta_levavi(lavan, divre_riv)")

# -------------------------- Gen.31.27 · THE_UNPLAYED_BAND ------------------
# לָמָּה נַחְבֵּאתָ לִבְרֹחַ וַתִּגְנֹב אֹתִי וְלֹא־הִגַּדְתָּ לִּי
# וָאֲשַׁלֵּחֲךָ בְּשִׂמְחָה וּבְשִׁרִים בְּתֹף וּבְכִנּוֹר
# "[EN-AID] Why did you hide yourself to flee, and steal me, and did not
# tell me — I would have sent you away with joy and with songs, with timbrel
# and with lyre —"
m.step("Gen.31.27")
# ‹לָמָּה נַחְבֵּאתָ לִבְרֹחַ וַתִּגְנֹב אֹתִי› (“to-what secrete to-bolt
# and-steal obj-marker-me/my”) — fact holds: secrete-and-ashalechakha-in-
# blithesomeness(Laban, irrealis)
m.fact("nachbeta_va_ashalechakha_be_simcha(lavan, irrealis)")

# -------------------------- Gen.31.28 · THE_DENIED_KISS --------------------
# וְלֹא נְטַשְׁתַּנִי לְנַשֵּׁק לְבָנַי וְלִבְנֹתָי עַתָּה הִסְכַּלְתָּ
# עֲשׂוֹ
# "[EN-AID] And did not allow me to kiss my sons and my daughters? Now you
# have done foolishly."
m.step("Gen.31.28")
# ‹וְלֹא נְטַשְׁתַּנִי לְנַשֵּׁק לְבָנַי וְלִבְנֹתָי› (“and-not pound-me/my
# to-kiss to-son-me/my and-to-daughter-me/my”) — fact holds: not-netashtani-
# to-kiss(Laban, be-silly-make)
m.fact("lo_netashtani_le_nasheq(lavan, hiskalta_aso)")

# -------------------------- Gen.31.29 · THE_POWER_AND_THE_RETELL -----------
# יֶשׁ־לְאֵל יָדִי לַעֲשׂוֹת עִמָּכֶם רָע וֵאלֹהֵי אֲבִיכֶם אֶמֶשׁ אָמַר
# אֵלַי לֵאמֹר הִשָּׁמֶר לְךָ מִדַּבֵּר עִם־יַעֲקֹב מִטּוֹב עַד־רָע
# "[EN-AID] It is in the power of my hand to do you all harm; but the God of
# your father last night said to me: Guard yourself from speaking with Jacob
# from good to bad."
m.step("Gen.31.29")
# ‹הִשָּׁמֶר לְךָ מִדַּבֵּר עִם־יַעֲקֹב מִטּוֹב עַד־רָע› (“keep/guard to-
# you/your from-speak with Jacob from-good until bad”) — fact holds: retell-
# keep/guard-yesterday(Laban, letter-delta-from-speak)
m.fact("retell_hishamer_emesh(lavan, letter_delta_mi_daber)")

# -------------------------- Gen.31.30 · THE_LONGING_AND_THE_GODS -----------
# וְעַתָּה הָלֹךְ הָלַכְתָּ כִּי־נִכְסֹף נִכְסַפְתָּה לְבֵית אָבִיךָ לָמָּה
# גָנַבְתָּ אֶת־אֱלֹהָי
# "[EN-AID] And now, going you went because longing you longed for your
# father's house — why did you steal my gods?"
m.step("Gen.31.30")
# ‹לָמָּה גָנַבְתָּ אֶת־אֱלֹהָי› (“to-what steal obj-marker God-me/my”) —
# fact holds: lama-steal-obj-marker-elohay(Laban)
m.fact("lama_ganavta_et_elohay(lavan)")

# -------------------------- Gen.31.31 · THE_FEAR_ANSWER --------------------
# וַיַּעַן יַעֲקֹב וַיֹּאמֶר לְלָבָן כִּי יָרֵאתִי כִּי אָמַרְתִּי
# פֶּן־תִּגְזֹל אֶת־בְּנוֹתֶיךָ מֵעִמִּי
# "[EN-AID] And Jacob answered and said to Laban: Because I was afraid, for
# I said: Lest you tear your daughters away from me."
m.step("Gen.31.31")
# ‹כִּי יָרֵאתִי כִּי אָמַרְתִּי› (“that fear that say”) — fact holds: fear-
# lest-pluck-off(Jacob)
m.fact("yareti_pen_tigzol(yaaqov)")

# -------------------------- Gen.31.32 · THE_DEATH_OATH_AND_THE_WARRANT -----
# עִם אֲשֶׁר תִּמְצָא אֶת־אֱלֹהֶיךָ לֹא יִחְיֶה נֶגֶד אַחֵינוּ הַכֶּר־לְךָ
# מָה עִמָּדִי וְקַח־לָךְ וְלֹא־יָדַע יַעֲקֹב כִּי רָחֵל גְּנָבָתַם
# "[EN-AID] With whomever you find your gods — he shall not live. Before our
# kinsmen, identify what of yours is with me and take it. And Jacob did not
# know that Rachel had stolen them."
m.step("Gen.31.32")
# ‹עִם אֲשֶׁר תִּמְצָא אֶת־אֱלֹהֶיךָ לֹא יִחְיֶה› (“with which find obj-
# marker God-you/your not live”) — fact holds: with-find-not-live(oath-
# content)
m.fact("im_timtza_lo_yichye(oath_content)")
# ‹הַכֶּר־לְךָ מָה עִמָּדִי וְקַח־לָךְ› (“scrutinize to-you/your what along-
# with-me/my and-take to-you/your”) — Jacob speaks a demand — LET:
# scrutinize-and-take(Laban, what-with-me)
m.declare("yaaqov", "LET",
          "haker_ve_qach(lavan, ma_imadi)")
# ‹וְלֹא־יָדַע יַעֲקֹב כִּי רָחֵל גְּנָבָתַם› (“and-not know Jacob that
# Rachel steal-them/their”) — fact holds: velo-know-Jacob-that-Rachel-
# genavatam(narrator)
m.fact("velo_yada_yaaqov_ki_rachel_genavatam(narrator)")

# -------------------------- Gen.31.33 · THE_FOUR_TENTS ---------------------
# וַיָּבֹא לָבָן בְּאֹהֶל יַעֲקֹב וּבְאֹהֶל לֵאָה וּבְאֹהֶל שְׁתֵּי
# הָאֲמָהֹת וְלֹא מָצָא וַיֵּצֵא מֵאֹהֶל לֵאָה וַיָּבֹא בְּאֹהֶל רָחֵל
# "[EN-AID] And Laban came into Jacob's tent and into Leah's tent and into
# the tent of the two maidservants, and did not find; and he went out of
# Leah's tent and came into Rachel's tent."
m.step("Gen.31.33")
# ‹וַיָּבֹא בְּאֹהֶל רָחֵל› (“and-come/bring in-tent Rachel”) — fact holds:
# not-find-rishon(Laban, four-ohalim)
m.fact("lo_matza_rishon(lavan, arba_ohalim)")

# -------------------------- Gen.31.34 · THE_SITTING_ON_THE_GODS ------------
# וְרָחֵל לָקְחָה אֶת־הַתְּרָפִים וַתְּשִׂמֵם בְּכַר הַגָּמָל וַתֵּשֶׁב
# עֲלֵיהֶם וַיְמַשֵּׁשׁ לָבָן אֶת־כָּל־הָאֹהֶל וְלֹא מָצָא
# "[EN-AID] And Rachel had taken the terafim and put them in the camel's
# saddle-cushion and sat upon them. And Laban felt through all the tent and
# did not find."
m.step("Gen.31.34")
# ‹וְרָחֵל לָקְחָה אֶת־הַתְּרָפִים› (“and-Rachel take obj-marker the-
# Teraphim-a-family-idol”) — fact holds: and-tesimem-and-dwell/sit-
# aleihem(Rachel, the-Teraphim-a-family-idol)
m.fact("va_tesimem_va_teshev_aleihem(rachel, ha_terafim)")

# -------------------------- Gen.31.35 · THE_WAY_OF_WOMEN_AND_THE_JUSSIVE ---
# וַתֹּאמֶר אֶל־אָבִיהָ אַל־יִחַר בְּעֵינֵי אֲדֹנִי כִּי לוֹא אוּכַל לָקוּם
# מִפָּנֶיךָ כִּי־דֶרֶךְ נָשִׁים לִי וַיְחַפֵּשׂ וְלֹא מָצָא אֶת־הַתְּרָפִים
# "[EN-AID] And she said to her father: Let it not burn in the eyes of my
# lord that I cannot rise before you, for the way of women is upon me. And
# he searched and did not find the terafim."
m.step("Gen.31.35")
# ‹יִחַר בְּעֵינֵי אֲדֹנִי› (“glow in-eye lord-me/my”) — Rachel speaks a
# demand — LET-NOT: glow(in-eye-adoni)
m.declare("rachel", "LET-NOT",
          "yichar(be_ene_adoni)")
# ‹וַיְחַפֵּשׂ וְלֹא מָצָא אֶת› (“and-seek and-not find obj-marker”) — fact
# holds: not-find-obj-marker-the-Teraphim-a-family-idol(Laban, sof-chipus)
m.fact("lo_matza_et_ha_terafim(lavan, sof_chipus)")

# -------------------------- Gen.31.36 · THE_BURN_LANDS_WRONG ---------------
# וַיִּחַר לְיַעֲקֹב וַיָּרֶב בְּלָבָן וַיַּעַן יַעֲקֹב וַיֹּאמֶר לְלָבָן
# מַה־פִּשְׁעִי מַה חַטָּאתִי כִּי דָלַקְתָּ אַחֲרָי
# "[EN-AID] And it burned for Jacob, and he quarreled with Laban; and Jacob
# answered and said to Laban: What is my transgression, what is my sin, that
# you have hotly pursued after me?"
m.step("Gen.31.36")
# ‹וַיִּחַר לְיַעֲקֹב וַיָּרֶב בְּלָבָן› (“and-glow to-Jacob and-toss in-
# Laban”) — fact holds: and-glow-to-Jacob(the-charon-in-the-enayim-acherot)
m.fact("va_yichar_le_yaaqov(ha_charon_ba_enayim_acherot)")

# -------------------------- Gen.31.37 · THE_TRIBUNAL_DEMAND ----------------
# כִּי־מִשַּׁשְׁתָּ אֶת־כָּל־כֵּלַי מַה־מָּצָאתָ מִכֹּל כְּלֵי־בֵיתֶךָ שִׂים
# כֹּה נֶגֶד אַחַי וְאַחֶיךָ וְיוֹכִיחוּ בֵּין שְׁנֵינוּ
# "[EN-AID] For you have felt through all my vessels — what have you found
# of all your house's vessels? Set it here before my kinsmen and your
# kinsmen, and let them decide between the two of us."
m.step("Gen.31.37")
# ‹שִׂים כֹּה נֶגֶד אַחַי וְאַחֶיךָ› (“put/set like-this front brother-me/my
# and-brother-you/your”) — Jacob speaks a demand — LET: put/set(Laban, this-
# front-achai-and-achekha)
m.declare("yaaqov", "LET",
          "sim(lavan, ko_neged_achai_ve_achekha)")

# -------------------------- Gen.31.38 · THE_AUDIT_OPENS --------------------
# זֶה עֶשְׂרִים שָׁנָה אָנֹכִי עִמָּךְ רְחֵלֶיךָ וְעִזֶּיךָ לֹא שִׁכֵּלוּ
# וְאֵילֵי צֹאנְךָ לֹא אָכָלְתִּי
# "[EN-AID] These twenty years I have been with you: your ewes and your she-
# goats have not miscarried, and the rams of your flock I have not eaten."
m.step("Gen.31.38")
# ‹זֶה עֶשְׂרִים שָׁנָה אָנֹכִי עִמָּךְ› (“this twenty years with-you/your”)
# — fact holds: twenty-years-not-miscarry(Jacob, cheshbon)
m.fact("esrim_shana_lo_shikelu(yaaqov, cheshbon)")

# -------------------------- Gen.31.39 · THE_SHEPHERD_LAW_SEED --------------
# טְרֵפָה לֹא־הֵבֵאתִי אֵלֶיךָ אָנֹכִי אֲחַטֶּנָּה מִיָּדִי תְּבַקְשֶׁנָּה
# גְּנֻבְתִי יוֹם וּגְנֻבְתִי לָיְלָה
# "[EN-AID] A torn animal I did not bring you — I bore its loss; from my
# hand you would seek it, stolen by day or stolen by night."
m.step("Gen.31.39")
# ‹טְרֵפָה לֹא־הֵבֵאתִי אֵלֶיךָ› (“prey not come/bring to-you/your”) — fact
# holds: prey-anokhi-achatena(Jacob, cheshbon)
m.fact("terefa_anokhi_achatena(yaaqov, cheshbon)")

# -------------------------- Gen.31.40 · THE_HEAT_AND_THE_FROST -------------
# הָיִיתִי בַיּוֹם אֲכָלַנִי חֹרֶב וְקֶרַח בַּלָּיְלָה וַתִּדַּד שְׁנָתִי
# מֵעֵינָי
# "[EN-AID] I was: by day heat consumed me, and frost by night; and my sleep
# fled from my eyes."
m.step("Gen.31.40")
# ‹הָיִיתִי בַיּוֹם אֲכָלַנִי חֹרֶב וְקֶרַח בַּלָּיְלָה› (“be in-day eat-
# me/my drought and-ice in-night”) — fact holds: drought-ice-nadad-
# shena(Jacob, cheshbon)
m.fact("chorev_qerach_nadad_shena(yaaqov, cheshbon)")

# -------------------------- Gen.31.41 · THE_TWENTY_YEARS_LEDGER ------------
# זֶה־לִּי עֶשְׂרִים שָׁנָה בְּבֵיתֶךָ עֲבַדְתִּיךָ אַרְבַּע־עֶשְׂרֵה שָׁנָה
# בִּשְׁתֵּי בְנֹתֶיךָ וְשֵׁשׁ שָׁנִים בְּצֹאנֶךָ וַתַּחֲלֵף
# אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת מֹנִים
# "[EN-AID] These twenty years I have been in your house: I served you
# fourteen years for your two daughters and six years for your flock, and
# you changed my wages ten countings."
m.step("Gen.31.41")
# ‹וַתַּחֲלֵף אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת מֹנִים› (“and-slide-by obj-marker
# wages-me/my ten something-weighed-out”) — fact holds: four--teen-and-six-
# ten-something-weighed-out(Jacob, cheshbon)
m.fact("arba_esre_ve_shesh_aseret_monim(yaaqov, cheshbon)")

# -------------------------- Gen.31.42 · THE_ADJUDICATION_ALREADY_HELD ------
# לוּלֵי אֱלֹהֵי אָבִי אֱלֹהֵי אַבְרָהָם וּפַחַד יִצְחָק הָיָה לִי כִּי
# עַתָּה רֵיקָם שִׁלַּחְתָּנִי אֶת־עָנְיִי וְאֶת־יְגִיעַ כַּפַּי רָאָה
# אֱלֹהִים וַיּוֹכַח אָמֶשׁ
# "[EN-AID] Were it not that the God of my father — the God of Abraham and
# the Fear of Isaac — was for me, now you would have sent me away empty. My
# affliction and the toil of my palms God has seen — and he adjudicated last
# night."
m.step("Gen.31.42")
# ‹לוּלֵי אֱלֹהֵי אָבִי אֱלֹהֵי אַבְרָהָם וּפַחַד יִצְחָק› (“if-not God
# father-me/my God Abraham and-alarm Isaac”) — fact holds: if-not-God-avi-
# and-alarm-Isaac(Jacob)
m.fact("lule_elohe_avi_u_fachad_yitzchaq(yaaqov)")
# ‹וַיּוֹכַח אָמֶשׁ› (“and-be-right yesterday”) — fact holds: see-God-and-
# be-right-yesterday(landing-put/set-tribunal)
m.fact("raa_Elohim_va_yokhach_amesh(landing_sim_tribunal)")

# -------------------------- Gen.31.43 · THE_EVERYTHING_IS_MINE -------------
# וַיַּעַן לָבָן וַיֹּאמֶר אֶל־יַעֲקֹב הַבָּנוֹת בְּנֹתַי וְהַבָּנִים בָּנַי
# וְהַצֹּאן צֹאנִי וְכֹל אֲשֶׁר־אַתָּה רֹאֶה לִי־הוּא וְלִבְנֹתַי
# מָה־אֶעֱשֶׂה לָאֵלֶּה הַיּוֹם אוֹ לִבְנֵיהֶן אֲשֶׁר יָלָדוּ
# "[EN-AID] And Laban answered and said to Jacob: The daughters are my
# daughters and the sons are my sons and the flock is my flock, and all that
# you see — it is mine. And for my daughters, what can I do for these today,
# or for their sons whom they have borne?"
m.step("Gen.31.43")
# ‹וְכֹל אֲשֶׁר־אַתָּה רֹאֶה לִי־הוּא› (“and-all which you see to-me/my
# he/it”) — fact holds: the-all-to-me-he/it-and-what-make(Laban)
m.fact("ha_kol_li_hu_u_ma_eese(lavan)")

# -------------------------- Gen.31.44 · THE_COVENANT_COHORTATIVE -----------
# וְעַתָּה לְכָה נִכְרְתָה בְרִית אֲנִי וָאָתָּה וְהָיָה לְעֵד בֵּינִי
# וּבֵינֶךָ
# "[EN-AID] And now, come, let us cut a covenant, I and you; and let it be
# for a witness between me and you."
m.step("Gen.31.44")
# ‹וְעַתָּה לְכָה נִכְרְתָה בְרִית אֲנִי וָאָתָּה› (“and-now go-ward cut
# covenant and-you”) — Laban speaks a demand — CMD-US?: nikhreta(covenant-
# ani-and-now)
m.declare("lavan", "CMD-US?",
          "nikhreta(verit_ani_va_ata)")

# -------------------------- Gen.31.45 · THE_STONE_RAISED -------------------
# וַיִּקַּח יַעֲקֹב אָבֶן וַיְרִימֶהָ מַצֵּבָה
# "[EN-AID] And Jacob took a stone and raised it up as a pillar."
m.step("Gen.31.45")
# ‹וַיִּקַּח יַעֲקֹב אָבֶן וַיְרִימֶהָ מַצֵּבָה› (“and-take Jacob stone and-
# rise-high-her/its pillar”) — the world gains: the-pillar
m.install("ha_matzeva")

# -------------------------- Gen.31.46 · THE_HEAP_AND_THE_WRONG_VERB --------
# וַיֹּאמֶר יַעֲקֹב לְאֶחָיו לִקְטוּ אֲבָנִים וַיִּקְחוּ אֲבָנִים
# וַיַּעֲשׂוּ־גָל וַיֹּאכְלוּ שָׁם עַל־הַגָּל
# "[EN-AID] And Jacob said to his kinsmen: Gather stones! And they took
# stones and made a heap, and they ate there upon the heap."
m.step("Gen.31.46")
# ‹לִקְטוּ אֲבָנִים› (“pick-up stone”) — Jacob speaks a demand — LET: pick-
# up(echav, stone)
m.declare("yaaqov", "LET",
          "liqtu(echav, avanim)")
# ‹וַיִּקְחוּ אֲבָנִים וַיַּעֲשׂוּ־גָל› (“and-take stone and-make something-
# rolled”) — the world gains: the-something-rolled
m.install("ha_gal")

# -------------------------- Gen.31.47 · THE_TWO_TONGUES --------------------
# וַיִּקְרָא־לוֹ לָבָן יְגַר שָׂהֲדוּתָא וְיַעֲקֹב קָרָא לוֹ גַּלְעֵד
# "[EN-AID] And Laban called it Yegar-Sahaduta [heap of witness, in
# Aramaic], and Jacob called it Galed [heap of witness, in Hebrew]."
m.step("Gen.31.47")
# ‹וַיִּקְרָא־לוֹ לָבָן יְגַר שָׂהֲדוּתָא› (“and-call to-him/its Laban
# Jegar-Sahadutha Jegar-Sahadutha”) — named: the-something-rolled := Jegar-
# Sahadutha-Jegar-Sahadutha
m.name("ha_gal", "yegar_sahaduta")
# ‹וְיַעֲקֹב קָרָא לוֹ גַּלְעֵד› (“and-Jacob call to-him/its Galeed”) —
# named: the-something-rolled := Galeed
m.name("ha_gal", "galed")

# -------------------------- Gen.31.48 · THE_ETIOLOGY_REPORT ----------------
# וַיֹּאמֶר לָבָן הַגַּל הַזֶּה עֵד בֵּינִי וּבֵינְךָ הַיּוֹם עַל־כֵּן
# קָרָא־שְׁמוֹ גַּלְעֵד
# "[EN-AID] And Laban said: This heap is witness between me and you today.
# Therefore its name was called Galed,"
m.step("Gen.31.48")
# ‹עַל־כֵּן קָרָא־שְׁמוֹ גַּלְעֵד› (“over so call name-him/its Galeed”) —
# fact holds: the-something-rolled-concretely-over-so-Galeed(report-only)
m.fact("ha_gal_ed_al_ken_galed(report_only)")

# -------------------------- Gen.31.49 · THE_WATCHPOST_PRAYER ---------------
# וְהַמִּצְפָּה אֲשֶׁר אָמַר יִצֶף יְהוָה בֵּינִי וּבֵינֶךָ כִּי נִסָּתֵר
# אִישׁ מֵרֵעֵהוּ
# "[EN-AID] And the Mitzpah [watchpost], because he said: May YHWH watch
# between me and you when we are hidden each from his fellow."
m.step("Gen.31.49")
# ‹יִצֶף יְהוָה בֵּינִי וּבֵינֶךָ› (“lean-forward YHWH between-me/my and-
# between-you/your”) — Laban speaks a demand — LET: lean-forward(the-LORD,
# beni-and-venekha)
m.declare("lavan", "LET",
          "yitzef(YHWH, beni_u_venekha)")

# -------------------------- Gen.31.50 · THE_TERMS_AND_THE_SEE --------------
# אִם־תְּעַנֶּה אֶת־בְּנֹתַי וְאִם־תִּקַּח נָשִׁים עַל־בְּנֹתַי אֵין אִישׁ
# עִמָּנוּ רְאֵה אֱלֹהִים עֵד בֵּינִי וּבֵינֶךָ
# "[EN-AID] If you afflict my daughters, and if you take wives over my
# daughters — no man is with us; see, God is witness between me and you."
m.step("Gen.31.50")
# ‹רְאֵה אֱלֹהִים עֵד בֵּינִי וּבֵינֶךָ› (“see God concretely between-me/my
# and-between-you/your”) — fact holds: with-afflict-literally-with-take-
# oath-content(Laban)
m.fact("im_teane_im_tiqach_oath_content(lavan)")

# -------------------------- Gen.31.51 · THE_CLAIMED_CASTER -----------------
# וַיֹּאמֶר לָבָן לְיַעֲקֹב הִנֵּה הַגַּל הַזֶּה וְהִנֵּה הַמַצֵּבָה אֲשֶׁר
# יָרִיתִי בֵּינִי וּבֵינֶךָ
# "[EN-AID] And Laban said to Jacob: Behold this heap and behold the pillar
# which I have cast between me and you."
m.step("Gen.31.51")
# ‹הִנֵּה הַגַּל הַזֶּה וְהִנֵּה הַמַצֵּבָה› (“behold the-something-rolled
# the-this and-behold the-pillar”) — fact holds: behold-the-something-
# rolled-and-the-pillar-flow-as-water(Laban)
m.fact("hine_ha_gal_ve_ha_matzeva_yariti(lavan)")

# -------------------------- Gen.31.52 · THE_BOUNDARY_OATH ------------------
# עֵד הַגַּל הַזֶּה וְעֵדָה הַמַּצֵּבָה אִם־אָנִי לֹא־אֶעֱבֹר אֵלֶיךָ
# אֶת־הַגַּל הַזֶּה וְאִם־אַתָּה לֹא־תַעֲבֹר אֵלַי אֶת־הַגַּל הַזֶּה
# וְאֶת־הַמַּצֵּבָה הַזֹּאת לְרָעָה
# "[EN-AID] Witness is this heap and witness the pillar: that I will not
# pass beyond this heap to you, and that you will not pass beyond this heap
# and this pillar to me, for harm."
m.step("Gen.31.52")
# ‹עֵד הַגַּל הַזֶּה וְעֵדָה הַמַּצֵּבָה› (“concretely the-something-rolled
# the-this and-testimony the-pillar”) — fact holds: concretely-the-
# something-rolled-and-testimony-the-pillar-not-naavor(oath-content)
m.fact("ed_ha_gal_ve_eda_ha_matzeva_lo_naavor(oath_content)")

# -------------------------- Gen.31.53 · THE_OATH_BY_THE_FEAR ---------------
# אֱלֹהֵי אַבְרָהָם וֵאלֹהֵי נָחוֹר יִשְׁפְּטוּ בֵינֵינוּ אֱלֹהֵי אֲבִיהֶם
# וַיִּשָּׁבַע יַעֲקֹב בְּפַחַד אָבִיו יִצְחָק
# "[EN-AID] The God of Abraham and the god of Nahor judge between us — the
# god of their father. And Jacob swore by the Fear of his father Isaac."
m.step("Gen.31.53")
# ‹אֱלֹהֵי אַבְרָהָם וֵאלֹהֵי נָחוֹר יִשְׁפְּטוּ› (“God Abraham and-God
# Nahor judge”) — fact holds: judge-imperfect-fenced(God-Abraham-and-God-
# Nahor)
m.fact("yishptu_imperfect_fenced(elohe_avraham_ve_lohe_nachor)")
# ‹וַיִּשָּׁבַע יַעֲקֹב בְּפַחַד אָבִיו יִצְחָק› (“and-swear Jacob in-alarm
# father-him/its Isaac”) — fact holds: and-swear-Jacob-in-alarm-aviv(other-
# root-performance)
m.fact("va_yishava_yaaqov_be_fachad_aviv(other_root_performance)")

# -------------------------- Gen.31.54 · THE_FIRST_SACRIFICE ----------------
# וַיִּזְבַּח יַעֲקֹב זֶבַח בָּהָר וַיִּקְרָא לְאֶחָיו לֶאֱכָל־לָחֶם
# וַיֹּאכְלוּ לֶחֶם וַיָּלִינוּ בָּהָר
# "[EN-AID] And Jacob sacrificed a sacrifice on the mountain and called his
# kinsmen to eat bread; and they ate bread and lodged on the mountain."
m.step("Gen.31.54")
# ‹וַיִּזְבַּח יַעֲקֹב זֶבַח בָּהָר› (“and-slaughter-an-animal Jacob
# sacrifice in-mountain”) — fact holds: and-slaughter-an-animal-sacrifice-
# and-eat-and-stop(Jacob, echav, mountain)
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
