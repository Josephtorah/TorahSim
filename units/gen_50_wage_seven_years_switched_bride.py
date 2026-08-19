#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_50_wage_seven_years_switched_bride — 29:15-30
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_50_wage_seven_years_switched_bride.yaml) is
# CANONICAL (Pre-Code); this file is a derived, runnable rendering. Do not
# edit — regenerate. The assertion block at the bottom is baked from the
# Stage D interpreter's actual final state: running this file re-proves the
# unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The wage, the seven years, and the switched bride (29:15-30)"""
from machine import Machine

m = Machine("gen_50_wage_seven_years_switched_bride")

# -------------------------- Gen.29.15 · THE_WAGE_QUESTION_PUSH -------------
# וַיֹּאמֶר לָבָן לְיַעֲקֹב הֲכִי־אָחִי אַתָּה וַעֲבַדְתַּנִי חִנָּם
# הַגִּידָה לִּי מַה־מַּשְׂכֻּרְתֶּךָ
# "[EN-AID] And Laban said to Jacob: Because you are my brother, should you
# serve me for nothing? Tell me, what is your wage?"
m.step("Gen.29.15")
# ‹הַגִּידָה לִּי מַה־מַּשְׂכֻּרְתֶּךָ› (“tell-ward to-me/my what wages-
# you/your”) — Laban speaks a demand — LET: hagida-maskoret(Jacob)
m.declare("lavan", "LET",
          "hagida_maskoret(yaaqov)")

# -------------------------- Gen.29.16 · THE_TWO_DAUGHTERS ------------------
# וּלְלָבָן שְׁתֵּי בָנוֹת שֵׁם הַגְּדֹלָה לֵאָה וְשֵׁם הַקְּטַנָּה רָחֵל
# "[EN-AID] And Laban had two daughters: the name of the elder was Leah, and
# the name of the younger was Rachel."
m.step("Gen.29.16")
# ‹שֵׁם הַגְּדֹלָה לֵאָה וְשֵׁם הַקְּטַנָּה רָחֵל› (“name the-great Leah
# and-name the-abbreviated Rachel”) — fact holds: two-daughters-great-leah-
# abbreviated-Rachel
m.fact("two_daughters_gedola_leah_qetana_rachel")

# -------------------------- Gen.29.17 · THE_EYES_AND_THE_FORM --------------
# וְעֵינֵי לֵאָה רַכּוֹת וְרָחֵל הָיְתָה יְפַת־תֹּאַר וִיפַת מַרְאֶה
# "[EN-AID] And Leah's eyes were tender; but Rachel was beautiful of form
# and beautiful of appearance."
m.step("Gen.29.17")
# ‹וְעֵינֵי לֵאָה רַכּוֹת … יְפַת־תֹּאַר› (“and-eye Leah tender … beautiful
# outline”) — fact holds: leah-eyes-tender-Rachel-beautiful
m.fact("leah_eyes_tender_rachel_beautiful")

# -------------------------- Gen.29.18 · THE_WAGE_TOLD_POP ------------------
# וַיֶּאֱהַב יַעֲקֹב אֶת־רָחֵל וַיֹּאמֶר אֶעֱבָדְךָ שֶׁבַע שָׁנִים בְּרָחֵל
# בִּתְּךָ הַקְּטַנָּה
# "[EN-AID] And Jacob loved Rachel; and he said: I will serve you seven
# years for Rachel your younger daughter."
m.step("Gen.29.18")
# ‹אֶעֱבָדְךָ שֶׁבַע שָׁנִים בְּרָחֵל› (“work/serve-you/your seven years in-
# Rachel”) — demand settled (popped from the queue): hagida-maskoret(Jacob)
m.result("hagida_maskoret(yaaqov)", tmark="t1")
# ‹וַיֶּאֱהַב יַעֲקֹב אֶת־רָחֵל› (“and-have-affection-for Jacob obj-marker
# Rachel”) — fact holds: Jacob-loves-Rachel-contract-names-her
m.fact("yaaqov_loves_rachel_contract_names_her")

# -------------------------- Gen.29.19 · THE_FENCED_TOV_AND_DWELL_PUSH ------
# וַיֹּאמֶר לָבָן טוֹב תִּתִּי אֹתָהּ לָךְ מִתִּתִּי אֹתָהּ לְאִישׁ אַחֵר
# שְׁבָה עִמָּדִי
# "[EN-AID] And Laban said: Better that I give her to you than that I give
# her to another man — dwell with me."
m.step("Gen.29.19")
# ‹שְׁבָה עִמָּדִי› (“dwell/sit-ward along-with-me/my”) — Laban speaks a
# demand — LET: seven-with-me(Jacob)
m.declare("lavan", "LET",
          "sheva_imadi(yaaqov)")
# ‹טוֹב תִּתִּי אֹתָהּ לָךְ› (“good set-me/my obj-marker-her/its to-
# you/your”) — fact holds: good-comparative-fenced-in-speech
m.fact("tov_comparative_fenced_in_speech")

# -------------------------- Gen.29.20 · THE_SEVEN_YEARS_AS_FEW_DAYS --------
# וַיַּעֲבֹד יַעֲקֹב בְּרָחֵל שֶׁבַע שָׁנִים וַיִּהְיוּ בְעֵינָיו כְּיָמִים
# אֲחָדִים בְּאַהֲבָתוֹ אֹתָהּ
# "[EN-AID] And Jacob served seven years for Rachel; and they were in his
# eyes as a few days, in his love for her."
m.step("Gen.29.20")
# ‹וַיַּעֲבֹד … כְּיָמִים אֲחָדִים› (“and-work/serve … like-day one”) — fact
# holds: seven-years-served-as-few-days
m.fact("seven_years_served_as_few_days")

# -------------------------- Gen.29.21 · THE_BABEL_IMPERATIVE_GIVE_MY_WIFE --
# וַיֹּאמֶר יַעֲקֹב אֶל־לָבָן הָבָה אֶת־אִשְׁתִּי כִּי מָלְאוּ יָמָי
# וְאָבוֹאָה אֵלֶיהָ
# "[EN-AID] And Jacob said to Laban: Give my wife, for my days are
# fulfilled, that I may go in to her."
m.step("Gen.29.21")
# ‹הָבָה אֶת־אִשְׁתִּי› (“give-ward obj-marker woman-me/my”) — Jacob speaks
# a demand — LET: hava-ishti(Laban)
m.declare("yaaqov", "LET",
          "hava_ishti(lavan)")

# -------------------------- Gen.29.22 · THE_FEAST_OF_THE_PLACE -------------
# וַיֶּאֱסֹף לָבָן אֶת־כָּל־אַנְשֵׁי הַמָּקוֹם וַיַּעַשׂ מִשְׁתֶּה
# "[EN-AID] And Laban gathered all the men of the place, and made a feast."
m.step("Gen.29.22")
# ‹וַיַּעַשׂ מִשְׁתֶּה› (“and-make drink”) — fact holds: feast-gathered-men-
# fowl-the-place
m.fact("feast_gathered_men_of_the_place")

# -------------------------- Gen.29.23 · THE_SWITCH_OBJECT_MISMATCH_NO_POP --
# וַיְהִי בָעֶרֶב וַיִּקַּח אֶת־לֵאָה בִתּוֹ וַיָּבֵא אֹתָהּ אֵלָיו וַיָּבֹא
# אֵלֶיהָ
# "[EN-AID] And it was in the evening: he took Leah his daughter and brought
# her to him; and he went in to her."
m.step("Gen.29.23")
# ‹וַיִּקַּח אֶת־לֵאָה … וַיָּבֹא אֵלֶיהָ› (“and-take obj-marker Leah … and-
# come/bring to-her/its”) — fact holds: leah-delivered-object-mismatch-no-
# pop
m.fact("leah_delivered_object_mismatch_no_pop")

# -------------------------- Gen.29.24 · THE_FIRST_MAID_ZILPAH --------------
# וַיִּתֵּן לָבָן לָהּ אֶת־זִלְפָּה שִׁפְחָתוֹ לְלֵאָה בִתּוֹ שִׁפְחָה
# "[EN-AID] And Laban gave her Zilpah his maid — to Leah his daughter as a
# maid."
m.step("Gen.29.24")
# ‹אֶת־זִלְפָּה שִׁפְחָתוֹ› (“obj-marker Zilpah female-slave-him/its”) —
# fact holds: zilpah-given-to-leah
m.fact("zilpah_given_to_leah")

# -------------------------- Gen.29.25 · THE_MORNING_BEHOLD_LEAH ------------
# וַיְהִי בַבֹּקֶר וְהִנֵּה־הִוא לֵאָה וַיֹּאמֶר אֶל־לָבָן מַה־זֹּאת
# עָשִׂיתָ לִּי הֲלֹא בְרָחֵל עָבַדְתִּי עִמָּךְ וְלָמָּה רִמִּיתָנִי
# "[EN-AID] And it was in the morning — behold, she was Leah. And he said to
# Laban: What is this you have done to me? Did I not serve with you for
# Rachel? Why have you deceived me?"
m.step("Gen.29.25")
# ‹וְהִנֵּה־הִוא לֵאָה … וְלָמָּה רִמִּיתָנִי› (“and-behold he/it Leah …
# and-to-what hurl-me/my”) — fact holds: morning-revelation-accusation-
# rimitani
m.fact("morning_revelation_accusation_rimitani")

# -------------------------- Gen.29.26 · THE_CUSTOM_YOUNGER_NOT_BEFORE_FIRSTBORN -
# וַיֹּאמֶר לָבָן לֹא־יֵעָשֶׂה כֵן בִּמְקוֹמֵנוּ לָתֵת הַצְּעִירָה לִפְנֵי
# הַבְּכִירָה
# "[EN-AID] And Laban said: It is not done so in our place, to give the
# younger before the firstborn."
m.step("Gen.29.26")
# ‹הַצְּעִירָה לִפְנֵי הַבְּכִירָה› (“the-little to-face the-eldest-
# daughter”) — fact holds: custom-little-not-before-eldest-daughter
m.fact("custom_tzeira_not_before_bekhira")

# -------------------------- Gen.29.27 · THE_FULFILL_WEEK_PUSH --------------
# מַלֵּא שְׁבֻעַ זֹאת וְנִתְּנָה לְךָ גַּם־אֶת־זֹאת בַּעֲבֹדָה אֲשֶׁר
# תַּעֲבֹד עִמָּדִי עוֹד שֶׁבַע־שָׁנִים אֲחֵרוֹת
# "[EN-AID] Fulfill the week of this one, and we will give you also the
# other, for the service that you shall serve with me — seven more years."
m.step("Gen.29.27")
# ‹מַלֵּא שְׁבֻעַ זֹאת› (“fill sevened this”) — Laban speaks a demand — LET:
# fill-sevened(Jacob)
m.declare("lavan", "LET",
          "male_shevua(yaaqov)")

# -------------------------- Gen.29.28 · THE_DOUBLE_POP_RACHEL_GIVEN --------
# וַיַּעַשׂ יַעֲקֹב כֵּן וַיְמַלֵּא שְׁבֻעַ זֹאת וַיִּתֶּן־לוֹ אֶת־רָחֵל
# בִּתּוֹ לוֹ לְאִשָּׁה
# "[EN-AID] And Jacob did so, and fulfilled her week; and he gave him Rachel
# his daughter as his wife."
m.step("Gen.29.28")
# ‹וַיְמַלֵּא שְׁבֻעַ זֹאת› (“and-fill sevened this”) — demand settled
# (popped from the queue): fill-sevened(Jacob)
m.result("male_shevua(yaaqov)", tmark="t1")
# ‹וַיִּתֶּן־לוֹ אֶת־רָחֵל בִּתּוֹ› (“and-set to-him/its obj-marker Rachel
# daughter-him/its”) — demand settled (popped from the queue): hava-
# ishti(Laban)
m.result("hava_ishti(lavan)", tmark="t1")

# -------------------------- Gen.29.29 · THE_SECOND_MAID_BILHAH -------------
# וַיִּתֵּן לָבָן לְרָחֵל בִּתּוֹ אֶת־בִּלְהָה שִׁפְחָתוֹ לָהּ לְשִׁפְחָה
# "[EN-AID] And Laban gave to Rachel his daughter Bilhah his maid, as her
# maid."
m.step("Gen.29.29")
# ‹אֶת־בִּלְהָה שִׁפְחָתוֹ› (“obj-marker Bilhah female-slave-him/its”) —
# fact holds: bilhah-given-to-Rachel
m.fact("bilhah_given_to_rachel")

# -------------------------- Gen.29.30 · THE_PREFERENCE_AND_SEVEN_MORE ------
# וַיָּבֹא גַּם אֶל־רָחֵל וַיֶּאֱהַב גַּם־אֶת־רָחֵל מִלֵּאָה וַיַּעֲבֹד
# עִמּוֹ עוֹד שֶׁבַע־שָׁנִים אֲחֵרוֹת
# "[EN-AID] And he went in also to Rachel, and loved also Rachel more than
# Leah; and he served with him seven more years."
m.step("Gen.29.30")
# ‹וַיֶּאֱהַב גַּם־אֶת־רָחֵל מִלֵּאָה … עוֹד שֶׁבַע־שָׁנִים› (“and-have-
# affection-for also obj-marker Rachel from-Leah … still/again seven years”)
# — fact holds: Rachel-loved-more-seven-more-years
m.fact("rachel_loved_more_seven_more_years")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['sheva_imadi(yaaqov)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['two_daughters_gedola_leah_qetana_rachel', 'leah_eyes_tender_rachel_beautiful', 'yaaqov_loves_rachel_contract_names_her', 'tov_comparative_fenced_in_speech', 'seven_years_served_as_few_days', 'feast_gathered_men_of_the_place', 'leah_delivered_object_mismatch_no_pop', 'zilpah_given_to_leah', 'morning_revelation_accusation_rimitani', 'custom_tzeira_not_before_bekhira', 'bilhah_given_to_rachel', 'rachel_loved_more_seven_more_years'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
