#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_47_grudge_flight_paddan_send — 27:41-28:9
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_47_grudge_flight_paddan_send.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Esau's grudge, Jacob's flight order, Rivqah's pressure — Paddan send (27:41-28:9)"""
from machine import Machine

m = Machine("gen_47_grudge_flight_paddan_send")

# -------------------------- Gen.27.41 · THE_GRUDGE_AND_HEART_SPEECH_KILL_INTENT -
# וַיִּשְׂטֹם עֵשָׂו אֶת־יַעֲקֹב עַל־הַבְּרָכָה אֲשֶׁר בֵּרֲכוֹ אָבִיו
# וַיֹּאמֶר עֵשָׂו בְּלִבּוֹ יִקְרְבוּ יְמֵי אֵבֶל אָבִי וְאַהַרְגָה
# אֶת־יַעֲקֹב אָחִי
# "[EN-AID] And Esau bore a grudge against Jacob over the blessing with
# which his father had blessed him; and Esau said in his heart, Let the days
# of mourning for my father draw near, and I will kill Jacob my brother."
m.step("Gen.27.41")
# ‹וַיִּשְׂטֹם … בְּלִבּוֹ … וְאַהַרְגָה› (“and-lurk-for … in-heart-him/its
# … and-smite-with-deadly-intent”) — fact holds: Esau-grudge; heart-kill-
# intent
m.fact("esav_grudge",
       "heart_kill_intent")

# -------------------------- Gen.27.42 · THE_LEAK_RETELLING_DELTA_AND_CALL_YOUNGER -
# וַיֻּגַּד לְרִבְקָה אֶת־דִּבְרֵי עֵשָׂו בְּנָהּ הַגָּדֹל וַתִּשְׁלַח
# וַתִּקְרָא לְיַעֲקֹב בְּנָהּ הַקָּטָן וַתֹּאמֶר אֵלָיו הִנֵּה עֵשָׂו
# אָחִיךָ מִתְנַחֵם לְךָ לְהָרְגֶךָ
# "[EN-AID] And the words of Esau her great son were told to Rivqah; and she
# sent and called Jacob her small son and said to him, Behold Esau your
# brother is consoling himself concerning you to kill you."
m.step("Gen.27.42")
# ‹וַיֻּגַּד … מִתְנַחֵם … לְהָרְגֶךָ› (“and-tell … sigh … to-smite-with-
# deadly-intent-you/your”) — fact holds: leak-and-delta
m.fact("leak_and_delta")

# -------------------------- Gen.27.43 · THE_SHEMA_BE_QOLI_AND_FLIGHT_COMPOUND -
# וְעַתָּה בְנִי שְׁמַע בְּקֹלִי וְקוּם בְּרַח־לְךָ אֶל־לָבָן אָחִי חָרָנָה
# "[EN-AID] And now my son hear my voice; and arise, flee for yourself to
# Laban my brother, to Haran."
m.step("Gen.27.43")
# ‹שְׁמַע בְּקֹלִי› (“hear in-voice/sound-me/my”) — rivqah speaks a demand —
# LET: hear-in-qoli-2(Jacob)
m.declare("rivqah", "LET",
          "shema_be_qoli_2(yaaqov)")
# ‹וְקוּם בְּרַח› (“and-arise bolt”) — rivqah speaks a demand — LET: arise-
# bolt-dwell/sit(Jacob)
m.declare("rivqah", "LET",
          "qum_berach_yashavta(yaaqov)")

# -------------------------- Gen.27.44 · THE_DWELL_DUTY_AND_WRATH_RETURN_WAIT -
# וְיָשַׁבְתָּ עִמּוֹ יָמִים אֲחָדִים עַד אֲשֶׁר־תָּשׁוּב חֲמַת אָחִיךָ
# "[EN-AID] And you shall dwell with him a few days, until your brother's
# wrath turns back."
m.step("Gen.27.44")
# ‹וְיָשַׁבְתָּ … חֲמַת אָחִיךָ› (“and-dwell/sit … heat brother-you/your”) —
# fact holds: dwell/sit-third-member-attached
m.fact("yashavta_third_member_attached")

# -------------------------- Gen.27.45 · THE_FORGET_SEND_TAKE_AND_BEREAVE_ARITHMETIC -
# עַד־שׁוּב אַף־אָחִיךָ מִמְּךָ וְשָׁכַח אֵת אֲשֶׁר־עָשִׂיתָ לּוֹ
# וְשָׁלַחְתִּי וּלְקַחְתִּיךָ מִשָּׁם לָמָה אֶשְׁכַּל גַּם־שְׁנֵיכֶם יוֹם
# אֶחָד
# "[EN-AID] Until your brother's anger turns back from you and he forgets
# what you did to him; then I will send and take you from there. Why should
# I be bereaved of both of you in one day?"
m.step("Gen.27.45")
# ‹וְשָׁכַח … וְשָׁלַחְתִּי … אֶשְׁכַּל› (“and-forget … and-send …
# miscarry”) — fact holds: Rebekah-plan-forget-send-take
m.fact("rivqa_plan_forget_send_take")

# -------------------------- Gen.27.46 · THE_PRESSURE_SPEECH_TO_ISAAC_HITTITE_LOATHE -
# וַתֹּאמֶר רִבְקָה אֶל־יִצְחָק קַצְתִּי בְחַיַּי מִפְּנֵי בְּנוֹת חֵת
# אִם־לֹקֵחַ יַעֲקֹב אִשָּׁה מִבְּנוֹת־חֵת כָּאֵלֶּה מִבְּנוֹת הָאָרֶץ
# לָמָּה לִּי חַיִּים
# "[EN-AID] And Rivqah said to Isaac, I loathe my life because of the
# daughters of Heth; if Jacob takes a wife from the daughters of Heth like
# these, from the daughters of the land, why is life mine?"
m.step("Gen.27.46")
# ‹קַצְתִּי … לָמָּה לִּי חַיִּים› (“be-disgusted … to-what to-me/my alive”)
# — fact holds: Rebekah-pressure-speech-to-Isaac
m.fact("rivqa_pressure_speech_to_yitzchaq")

# -------------------------- Gen.28.1 · THE_BLESS_EVENT_AND_CANAANITE_PROHIBITION -
# וַיִּקְרָא יִצְחָק אֶל־יַעֲקֹב וַיְבָרֶךְ אֹתוֹ וַיְצַוֵּהוּ וַיֹּאמֶר לוֹ
# לֹא־תִקַּח אִשָּׁה מִבְּנוֹת כְּנָעַן
# "[EN-AID] And Isaac called Jacob and blessed him, and commanded him and
# said to him, You shall not take a wife from the daughters of Canaan."
m.step("Gen.28.1")
# ‹וַיְבָרֶךְ אֹתוֹ› (“and-bless obj-marker-him/its”) — event: ?
m.event("?")
# ‹לֹא תִקַּח› (“not take”) — fact holds: prohibition-not-take-kenaanit
m.fact("prohibition_lo_tiqach_kenaanit")

# -------------------------- Gen.28.2 · THE_QUM_LEKH_QACH_WIFE_COMPOUND -----
# קוּם לֵךְ פַּדֶּנָה אֲרָם בֵּיתָה בְתוּאֵל אֲבִי אִמֶּךָ וְקַח־לְךָ
# מִשָּׁם אִשָּׁה מִבְּנוֹת לָבָן אֲחִי אִמֶּךָ
# "[EN-AID] Arise, go to Paddan-aram, to the house of Bethuel your mother's
# father, and take for yourself from there a wife from the daughters of
# Laban your mother's brother."
m.step("Gen.28.2")
# ‹קוּם לֵךְ … וְקַח› (“arise go … and-take”) — Isaac speaks a demand — LET:
# arise-go-take(Jacob)
m.declare("yitzchaq", "LET",
          "qum_lekh_qach(yaaqov)")

# -------------------------- Gen.28.3 · THE_EL_SHADDAI_JUSSIVE_PACKAGE_OPEN -
# וְאֵל שַׁדַּי יְבָרֵךְ אֹתְךָ וְיַפְרְךָ וְיַרְבֶּךָ וְהָיִיתָ לִקְהַל
# עַמִּים
# "[EN-AID] And may El Shaddai bless you and make you fruitful and multiply
# you, and may you become an assembly of peoples."
m.step("Gen.28.3")
# ‹וְאֵל שַׁדַּי יְבָרֵךְ … וְיַרְבֶּךָ› (“and-strength Almighty bless …
# and-multiply-you/your”) — fact holds: to-shaddai-limbs-staged
m.fact("el_shaddai_limbs_staged")

# -------------------------- Gen.28.4 · THE_ABRAHAM_BLESSING_GRANT_PACKAGE_PUSH -
# וְיִתֶּן־לְךָ אֶת־בִּרְכַּת אַבְרָהָם לְךָ וּלְזַרְעֲךָ אִתָּךְ
# לְרִשְׁתְּךָ אֶת־אֶרֶץ מְגֻרֶיךָ אֲשֶׁר־נָתַן אֱלֹהִים לְאַבְרָהָם
# "[EN-AID] And may He give you the blessing of Abraham, to you and to your
# seed with you, to possess the land of your sojournings which God gave to
# Abraham."
m.step("Gen.28.4")
# ‹וְיִתֶּן … בִּרְכַּת אַבְרָהָם› (“and-set … blessing Abraham”) — Isaac
# speaks a demand — LET: to-shaddai-package(Jacob)
m.declare("yitzchaq", "LET",
          "el_shaddai_package(yaaqov)")

# -------------------------- Gen.28.5 · THE_FATHER_SEND_AND_LEKH_PARTIAL ----
# וַיִּשְׁלַח יִצְחָק אֶת־יַעֲקֹב וַיֵּלֶךְ פַּדֶּנָה אֲרָם אֶל־לָבָן
# בֶּן־בְּתוּאֵל הָאֲרַמִּי אֲחִי רִבְקָה אֵם יַעֲקֹב וְעֵשָׂו
# "[EN-AID] And Isaac sent Jacob, and he went to Paddan-aram, to Laban son
# of Bethuel the Aramean, brother of Rivqah mother of Jacob and Esau."
m.step("Gen.28.5")
# ‹וַיִּשְׁלַח … וַיֵּלֶךְ› (“and-send … and-go”) — fact holds: go-partial-
# return-no-pop
m.fact("lekh_partial_return_no_pop")

# -------------------------- Gen.28.6 · THE_ESAU_SEES_BLESS_SEND_AND_QUOTE_REPLAY -
# וַיַּרְא עֵשָׂו כִּי־בֵרַךְ יִצְחָק אֶת־יַעֲקֹב וְשִׁלַּח אֹתוֹ פַּדֶּנָה
# אֲרָם לָקַחַת־לוֹ מִשָּׁם אִשָּׁה בְּבָרֲכוֹ אֹתוֹ וַיְצַו עָלָיו לֵאמֹר
# לֹא־תִקַּח אִשָּׁה מִבְּנוֹת כְּנָעַן
# "[EN-AID] And Esau saw that Isaac had blessed Jacob and sent him to
# Paddan-aram to take for himself from there a wife — when he blessed him he
# commanded him, saying, You shall not take a wife from the daughters of
# Canaan."
m.step("Gen.28.6")
# ‹וַיַּרְא עֵשָׂו כִּי־בֵרַךְ› (“and-see Esau that bless”) — fact holds:
# Esau-sees-bless-and-send
m.fact("esav_sees_bless_and_send")

# -------------------------- Gen.28.7 · THE_VA_YISHMA_POP_AND_GO_NOT_FLEE ---
# וַיִּשְׁמַע יַעֲקֹב אֶל־אָבִיו וְאֶל־אִמּוֹ וַיֵּלֶךְ פַּדֶּנָה אֲרָם
# "[EN-AID] And Jacob heeded his father and his mother, and went to Paddan-
# aram."
m.step("Gen.28.7")
# ‹וַיִּשְׁמַע יַעֲקֹב› (“and-hear Jacob”) — demand settled (popped from the
# queue): hear-in-qoli-2(Jacob)
m.result("shema_be_qoli_2(yaaqov)", tmark="t1")
# ‹וַיֵּלֶךְ פַּדֶּנָה אֲרָם› (“and-go to-Padan Padan”) — fact holds: go-go-
# frame-not-flee-frame
m.fact("yelekh_go_frame_not_flee_frame")

# -------------------------- Gen.28.8 · THE_SECOND_SEEING_EVIL_IN_THE_FATHERS_EYES -
# וַיַּרְא עֵשָׂו כִּי רָעוֹת בְּנוֹת כְּנָעַן בְּעֵינֵי יִצְחָק אָבִיו
# "[EN-AID] And Esau saw that the daughters of Canaan were evil in the eyes
# of Isaac his father."
m.step("Gen.28.8")
# ‹רָעוֹת … בְּעֵינֵי יִצְחָק› (“bad … in-eye Isaac”) — fact holds: Esau-
# sees-canaanite-evil-in-isaacs-eyes
m.fact("esav_sees_canaanite_evil_in_isaacs_eyes")

# -------------------------- Gen.28.9 · THE_MIRROR_TAKE_MACHALAT_CODA -------
# וַיֵּלֶךְ עֵשָׂו אֶל־יִשְׁמָעֵאל וַיִּקַּח אֶת־מָחֲלַת בַּת־יִשְׁמָעֵאל
# בֶּן־אַבְרָהָם אֲחוֹת נְבָיוֹת עַל־נָשָׁיו לוֹ לְאִשָּׁה
# "[EN-AID] And Esau went to Ishmael and took Machalat, daughter of Ishmael
# son of Abraham, sister of Nebaioth, in addition to his wives, as his
# wife."
m.step("Gen.28.9")
# ‹וַיִּקַּח אֶת־מָחֲלַת› (“and-take obj-marker Mahalath”) — fact holds:
# Esau-mirror-take-Mahalath
m.fact("esav_mirror_take_machalat")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['qum_berach_yashavta(yaaqov)', 'qum_lekh_qach(yaaqov)', 'el_shaddai_package(yaaqov)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['esav_grudge', 'heart_kill_intent', 'leak_and_delta', 'yashavta_third_member_attached', 'rivqa_plan_forget_send_take', 'rivqa_pressure_speech_to_yitzchaq', 'prohibition_lo_tiqach_kenaanit', 'el_shaddai_limbs_staged', 'lekh_partial_return_no_pop', 'esav_sees_bless_and_send', 'yelekh_go_frame_not_flee_frame', 'esav_sees_canaanite_evil_in_isaacs_eyes', 'esav_mirror_take_machalat'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
