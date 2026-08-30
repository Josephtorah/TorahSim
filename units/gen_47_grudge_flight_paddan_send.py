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
# witness-tier presupposed read: full_plan_decoded_and_censused on
# said_in_his_heart — read, not installed
m.witness_read("said_in_his_heart", "full_plan_decoded_and_censused",
                cites=["Bereshit Rabbah 75:9", "Bereshit Rabbah 34:10"])
# witness-tier presupposed read: expanded_into_the_empires_own_title on
# the_grudge_verb — read, not installed
m.witness_read("the_grudge_verb", "expanded_into_the_empires_own_title",
                cites=["Bereshit Rabbah 67:8"])
# witness-tier presupposed read: the_same_clause_read_as_filial_honour on
# waiting_for_the_mourning_days — read, not installed
m.witness_read("waiting_for_the_mourning_days", "the_same_clause_read_as_filial_honour",
                cites=["Bereshit Rabbah 76:2"])

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
# witness-tier presupposed read: matriarch_prophecy_stated_at_its_source on
# it_was_told_to_rebecca — read, not installed
m.witness_read("it_was_told_to_rebecca", "matriarch_prophecy_stated_at_its_source",
                cites=["Bereshit Rabbah 67:9", "Onkelos Genesis 27:13"])
# witness-tier presupposed read: interior_resolution_or_external_ambush on
# consoles_himself — read, not installed
m.witness_read("consoles_himself", "interior_resolution_or_external_ambush",
                cites=["Bereshit Rabbah 67:9", "Onkelos Genesis 27:42"])

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
# witness-tier presupposed read: made_seven_years_by_verbal_analogy on
# a_few_days — read, not installed
m.witness_read("a_few_days", "made_seven_years_by_verbal_analogy",
                cites=["Bereshit Rabbah 67:10"])

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
# witness-tier presupposed read:
# fourteen_hidden_and_the_marriage_at_eighty_four on the_untold_years —
# read, not installed
m.witness_read("the_untold_years", "fourteen_hidden_and_the_marriage_at_eighty_four",
                cites=["Bereshit Rabbah 68:5"])

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
# witness-tier presupposed read:
# loathing_speech_counted_against_the_standing_wives on the_stated_pretext —
# read, not installed
m.witness_read("the_stated_pretext", "loathing_speech_counted_against_the_standing_wives",
                cites=["Bereshit Rabbah 67:11"])

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
# witness-tier presupposed read: ratification_maxim_at_its_home_seat on
# the_summons — read, not installed
m.witness_read("the_summons", "ratification_maxim_at_its_home_seat",
                cites=["Bereshit Rabbah 67:12"])

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
# witness-tier presupposed read: nationalized_into_tribes on
# assembly_of_peoples — read, not installed
m.witness_read("assembly_of_peoples", "nationalized_into_tribes",
                cites=["Onkelos Genesis 28:3"])

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
# witness-tier presupposed read: absorbed_into_the_acceptance_register on
# heeded_his_father_and_mother — read, not installed
m.witness_read("heeded_his_father_and_mother", "absorbed_into_the_acceptance_register",
                cites=["Onkelos Genesis 28:7"])

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
# witness-grounded state (its own tier):
# tribes_paired_against_kingdoms_with_named_agents on the_exile_table
m.witness_state("the_exile_table", "tribes_paired_against_kingdoms_with_named_agents",
                cites=["Bereshit Rabbah 99:2", "Bereshit Rabbah 100:12"])

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
    assert sorted(m.WORLD["witnessed"]) == ['the_exile_table']
    assert m.WORLD["witnessed"]['the_exile_table']["cites"] == ['Bereshit Rabbah 99:2', 'Bereshit Rabbah 100:12']
    assert all('tribes_paired_against_kingdoms_with_named_agents' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('said_in_his_heart', 'full_plan_decoded_and_censused'), ('the_grudge_verb', 'expanded_into_the_empires_own_title'), ('waiting_for_the_mourning_days', 'the_same_clause_read_as_filial_honour'), ('it_was_told_to_rebecca', 'matriarch_prophecy_stated_at_its_source'), ('consoles_himself', 'interior_resolution_or_external_ambush'), ('a_few_days', 'made_seven_years_by_verbal_analogy'), ('the_untold_years', 'fourteen_hidden_and_the_marriage_at_eighty_four'), ('the_stated_pretext', 'loathing_speech_counted_against_the_standing_wives'), ('the_summons', 'ratification_maxim_at_its_home_seat'), ('assembly_of_peoples', 'nationalized_into_tribes'), ('heeded_his_father_and_mother', 'absorbed_into_the_acceptance_register')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 75:9', 'Bereshit Rabbah 34:10']
    assert all('full_plan_decoded_and_censused' not in f for f in m.WORLD["facts"])
    assert 'said_in_his_heart' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 67:8']
    assert all('expanded_into_the_empires_own_title' not in f for f in m.WORLD["facts"])
    assert 'the_grudge_verb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 76:2']
    assert all('the_same_clause_read_as_filial_honour' not in f for f in m.WORLD["facts"])
    assert 'waiting_for_the_mourning_days' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 67:9', 'Onkelos Genesis 27:13']
    assert all('matriarch_prophecy_stated_at_its_source' not in f for f in m.WORLD["facts"])
    assert 'it_was_told_to_rebecca' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 67:9', 'Onkelos Genesis 27:42']
    assert all('interior_resolution_or_external_ambush' not in f for f in m.WORLD["facts"])
    assert 'consoles_himself' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 67:10']
    assert all('made_seven_years_by_verbal_analogy' not in f for f in m.WORLD["facts"])
    assert 'a_few_days' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 68:5']
    assert all('fourteen_hidden_and_the_marriage_at_eighty_four' not in f for f in m.WORLD["facts"])
    assert 'the_untold_years' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 67:11']
    assert all('loathing_speech_counted_against_the_standing_wives' not in f for f in m.WORLD["facts"])
    assert 'the_stated_pretext' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 67:12']
    assert all('ratification_maxim_at_its_home_seat' not in f for f in m.WORLD["facts"])
    assert 'the_summons' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 28:3']
    assert all('nationalized_into_tribes' not in f for f in m.WORLD["facts"])
    assert 'assembly_of_peoples' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Genesis 28:7']
    assert all('absorbed_into_the_acceptance_register' not in f for f in m.WORLD["facts"])
    assert 'heeded_his_father_and_mother' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
