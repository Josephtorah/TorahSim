#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_49_well_stone_rachel_arrival — 29:1-14
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_49_well_stone_rachel_arrival.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The well, the great stone, and Rachel — arrival at Haran (29:1-14)"""
from machine import Machine

m = Machine("gen_49_well_stone_rachel_arrival")

# -------------------------- Gen.29.1 · THE_LIFTED_FEET_TO_THE_EAST ---------
# וַיִּשָּׂא יַעֲקֹב רַגְלָיו וַיֵּלֶךְ אַרְצָה בְנֵי־קֶדֶם
# "[EN-AID] And Jacob lifted his feet and went to the land of the children
# of the east."
m.step("Gen.29.1")
# ‹וַיִּשָּׂא … רַגְלָיו … קֶדֶם› (“and-lift/carry … foot-him/its … front”)
# — fact holds: Jacob-lifted-feet-walked-east
m.fact("yaaqov_lifted_feet_walked_east")

# -------------------------- Gen.29.2 · THE_WELL_THREE_FLOCKS_GREAT_STONE ---
# וַיַּרְא וְהִנֵּה בְאֵר בַּשָּׂדֶה וְהִנֵּה־שָׁם שְׁלֹשָׁה עֶדְרֵי־צֹאן
# רֹבְצִים עָלֶיהָ כִּי מִן־הַבְּאֵר הַהִוא יַשְׁקוּ הָעֲדָרִים וְהָאֶבֶן
# גְּדֹלָה עַל־פִּי הַבְּאֵר
# "[EN-AID] And he saw — behold a well in the field, and behold three flocks
# of sheep crouching by it, for from that well the flocks were watered; and
# the stone was great on the mouth of the well."
m.step("Gen.29.2")
# ‹רֹבְצִים … וְהָאֶבֶן גְּדֹלָה› (“crouch … and-the-stone great”) — fact
# holds: well-three-flocks-great-stone-on-mouth
m.fact("well_three_flocks_great_stone_on_mouth")
# witness-grounded state (its own tier):
# one_machine_bound_to_six_institutions on the_well_frame
m.witness_state("the_well_frame", "one_machine_bound_to_six_institutions",
                cites=["Bereshit Rabbah 70:8"])
# witness-tier presupposed read: sinai_with_an_all_or_nothing_gate on
# the_seventh_binding — read, not installed
m.witness_read("the_seventh_binding", "sinai_with_an_all_or_nothing_gate",
                cites=["Bereshit Rabbah 70:9"])

# -------------------------- Gen.29.3 · THE_STONE_PROTOCOL_HABITUAL ---------
# וְנֶאֶסְפוּ־שָׁמָּה כָל־הָעֲדָרִים וְגָלֲלוּ אֶת־הָאֶבֶן מֵעַל פִּי
# הַבְּאֵר וְהִשְׁקוּ אֶת־הַצֹּאן וְהֵשִׁיבוּ אֶת־הָאֶבֶן עַל־פִּי הַבְּאֵר
# לִמְקֹמָהּ
# "[EN-AID] And all the flocks would gather there, and they would roll the
# stone from the mouth of the well and water the sheep, and return the stone
# to its place on the mouth of the well."
m.step("Gen.29.3")
# ‹וְגָלֲלוּ … וְהִשְׁקוּ … וְהֵשִׁיבוּ› (“and-roll … and-give-drink … and-
# return”) — fact holds: stone-protocol-gather-roll-water-return
m.fact("stone_protocol_gather_roll_water_return")

# -------------------------- Gen.29.4 · THE_MY_BROTHERS_FROM_HARAN ----------
# וַיֹּאמֶר לָהֶם יַעֲקֹב אַחַי מֵאַיִן אַתֶּם וַיֹּאמְרוּ מֵחָרָן אֲנָחְנוּ
# "[EN-AID] And Jacob said to them: My brothers, from where are you? And
# they said: From Haran are we."
m.step("Gen.29.4")
# ‹אַחַי מֵאַיִן אַתֶּם … מֵחָרָן› (“brother-me/my from-where? you … from-
# Haran”) — fact holds: shepherds-are-from-Haran
m.fact("shepherds_are_from_charan")
# witness-tier presupposed read: re_keyed_clause_by_clause_to_the_exile on
# the_greeting — read, not installed
m.witness_read("the_greeting", "re_keyed_clause_by_clause_to_the_exile",
                cites=["Bereshit Rabbah 70:10"])

# -------------------------- Gen.29.5 · THE_KNOW_CHAIN_AND_GRANDFATHER_SKIP -
# וַיֹּאמֶר לָהֶם הַיְדַעְתֶּם אֶת־לָבָן בֶּן־נָחוֹר וַיֹּאמְרוּ יָדָעְנוּ
# "[EN-AID] And he said to them: Do you know Laban son of Nachor? And they
# said: We know."
m.step("Gen.29.5")
# ‹הַיְדַעְתֶּם … בֶּן־נָחוֹר … יָדָעְנוּ› (“the-know … son Nahor … know”) —
# fact holds: shepherds-know-Laban-son-Nahor
m.fact("shepherds_know_lavan_ben_nachor")

# -------------------------- Gen.29.6 · THE_SHALOM_AND_RACHEL_DEBUT ---------
# וַיֹּאמֶר לָהֶם הֲשָׁלוֹם לוֹ וַיֹּאמְרוּ שָׁלוֹם וְהִנֵּה רָחֵל בִּתּוֹ
# בָּאָה עִם־הַצֹּאן
# "[EN-AID] And he said to them: Is there peace to him? And they said: Peace
# — and behold Rachel his daughter comes with the sheep."
m.step("Gen.29.6")
# ‹הֲשָׁלוֹם לוֹ … וְהִנֵּה רָחֵל› (“the-safe to-him/its … and-behold
# Rachel”) — fact holds: safe-confirmed-Rachel-approaching
m.fact("shalom_confirmed_rachel_approaching")

# -------------------------- Gen.29.7 · THE_COMPOUND_PUSH_ON_THE_SHEPHERDS --
# וַיֹּאמֶר הֵן עוֹד הַיּוֹם גָּדוֹל לֹא־עֵת הֵאָסֵף הַמִּקְנֶה הַשְׁקוּ
# הַצֹּאן וּלְכוּ רְעוּ
# "[EN-AID] And he said: Behold, the day is still great; it is not time for
# the livestock to be gathered — water the sheep and go, pasture."
m.step("Gen.29.7")
# ‹הַשְׁקוּ הַצֹּאן וּלְכוּ רְעוּ› (“give-drink the-flock and-go graze”) —
# Jacob speaks a demand — LET: give-drink-go-graze(the-roim)
m.declare("yaaqov", "LET",
          "hashqu_lekhu_reu(ha_roim)")
# witness-tier presupposed read: labour_duty_from_an_exhaustive_disjunction
# on the_shepherds_rebuke — read, not installed
m.witness_read("the_shepherds_rebuke", "labour_duty_from_an_exhaustive_disjunction",
                cites=["Bereshit Rabbah 70:11"])

# -------------------------- Gen.29.8 · THE_REFUSAL_WITH_STONE_GROUNDS ------
# וַיֹּאמְרוּ לֹא נוּכַל עַד אֲשֶׁר יֵאָסְפוּ כָּל־הָעֲדָרִים וְגָלֲלוּ
# אֶת־הָאֶבֶן מֵעַל פִּי הַבְּאֵר וְהִשְׁקִינוּ הַצֹּאן
# "[EN-AID] And they said: We cannot, until all the flocks are gathered and
# they roll the stone from the mouth of the well — then we water the sheep."
m.step("Gen.29.8")
# ‹לֹא נוּכַל עַד אֲשֶׁר …› (“not be-able until which”) — fact holds:
# refusal-not-be-able-stone-grounds
m.fact("refusal_lo_nukhal_stone_grounds")

# -------------------------- Gen.29.9 · THE_STILL_SPEAKING_SHEPHERDESS ------
# עוֹדֶנּוּ מְדַבֵּר עִמָּם וְרָחֵל בָּאָה עִם־הַצֹּאן אֲשֶׁר לְאָבִיהָ כִּי
# רֹעָה הִוא
# "[EN-AID] While he was still speaking with them, Rachel came with the
# sheep that were her father's, for she was a shepherdess."
m.step("Gen.29.9")
# ‹עוֹדֶנּוּ מְדַבֵּר … כִּי רֹעָה הִוא› (“still/again-him/its speak … that
# graze he/it”) — fact holds: Rachel-arrived-shepherdess-while-speaking
m.fact("rachel_arrived_shepherdess_while_speaking")

# -------------------------- Gen.29.10 · THE_DEMANDER_PERFORMS_ROLL_AND_WATER -
# וַיְהִי כַּאֲשֶׁר רָאָה יַעֲקֹב אֶת־רָחֵל בַּת־לָבָן אֲחִי אִמּוֹ
# וְאֶת־צֹאן לָבָן אֲחִי אִמּוֹ וַיִּגַּשׁ יַעֲקֹב וַיָּגֶל אֶת־הָאֶבֶן
# מֵעַל פִּי הַבְּאֵר וַיַּשְׁקְ אֶת־צֹאן לָבָן אֲחִי אִמּוֹ
# "[EN-AID] And it was, when Jacob saw Rachel daughter of Laban his mother's
# brother, and the sheep of Laban his mother's brother, that Jacob drew near
# and rolled the stone from the mouth of the well, and watered the sheep of
# Laban his mother's brother."
m.step("Gen.29.10")
# ‹וַיִּגַּשׁ … וַיָּגֶל … וַיַּשְׁקְ› (“and-be … and-roll … and-give-
# drink”) — fact holds: demander-performed-roll-and-water
m.fact("demander_performed_roll_and_water")
# witness-tier presupposed read: strength_exhibit_recorded_at_its_verse on
# the_stone_rolled — read, not installed
m.witness_read("the_stone_rolled", "strength_exhibit_recorded_at_its_verse",
                cites=["Bereshit Rabbah 70:12"])

# -------------------------- Gen.29.11 · THE_KISS_VOICE_AND_WEEPING ---------
# וַיִּשַּׁק יַעֲקֹב לְרָחֵל וַיִּשָּׂא אֶת־קֹלוֹ וַיֵּבְךְּ
# "[EN-AID] And Jacob kissed Rachel, and lifted his voice, and wept."
m.step("Gen.29.11")
# ‹וַיִּשַּׁק … וַיִּשָּׂא אֶת־קֹלוֹ וַיֵּבְךְּ› (“and-kiss … and-lift/carry
# obj-marker voice/sound-him/its and-weep”) — fact holds: kiss-lifted-voice-
# weeping
m.fact("kiss_lifted_voice_weeping")
# witness-tier presupposed read: classified_against_an_exhaustive_table on
# the_kiss — read, not installed
m.witness_read("the_kiss", "classified_against_an_exhaustive_table",
                cites=["Bereshit Rabbah 70:12"])

# -------------------------- Gen.29.12 · THE_TELL_CHAIN_AND_HER_RUN ---------
# וַיַּגֵּד יַעֲקֹב לְרָחֵל כִּי אֲחִי אָבִיהָ הוּא וְכִי בֶן־רִבְקָה הוּא
# וַתָּרָץ וַתַּגֵּד לְאָבִיהָ
# "[EN-AID] And Jacob told Rachel that he was her father's kinsman and that
# he was Rivqah's son; and she ran and told her father."
m.step("Gen.29.12")
# ‹וַיַּגֵּד … וַתָּרָץ וַתַּגֵּד› (“and-tell … and-run and-tell”) — fact
# holds: identity-told-Rachel-ran-told-father
m.fact("identity_told_rachel_ran_told_father")
# witness-tier presupposed read:
# ambiguity_kept_by_one_member_removed_by_the_other on her_fathers_brother —
# read, not installed
m.witness_read("her_fathers_brother", "ambiguity_kept_by_one_member_removed_by_the_other",
                cites=["Bereshit Rabbah 70:13", "Onkelos Genesis 29:12"])

# -------------------------- Gen.29.13 · THE_SECOND_RUN_EMBRACE_KISS_RECOUNT -
# וַיְהִי כִשְׁמֹעַ לָבָן אֶת־שֵׁמַע יַעֲקֹב בֶּן־אֲחֹתוֹ וַיָּרָץ
# לִקְרָאתוֹ וַיְחַבֶּק־לוֹ וַיְנַשֶּׁק־לוֹ וַיְבִיאֵהוּ אֶל־בֵּיתוֹ
# וַיְסַפֵּר לְלָבָן אֵת כָּל־הַדְּבָרִים הָאֵלֶּה
# "[EN-AID] And it was, when Laban heard the report of Jacob his sister's
# son, that he ran to meet him, and embraced him, and kissed him, and
# brought him to his house; and he recounted to Laban all these things."
m.step("Gen.29.13")
# ‹כִשְׁמֹעַ … וַיָּרָץ … וַיְחַבֶּק … וַיְסַפֵּר› (“like-hear … and-run …
# and-clasp … and-count”) — fact holds: Laban-heard-ran-embraced-kissed-
# housed-recounted
m.fact("lavan_heard_ran_embraced_kissed_housed_recounted")

# -------------------------- Gen.29.14 · THE_BONE_FLESH_AND_MONTH_DWELL -----
# וַיֹּאמֶר לוֹ לָבָן אַךְ עַצְמִי וּבְשָׂרִי אָתָּה וַיֵּשֶׁב עִמּוֹ חֹדֶשׁ
# יָמִים
# "[EN-AID] And Laban said to him: Surely you are my bone and my flesh. And
# he dwelt with him a month of days."
m.step("Gen.29.14")
# ‹עַצְמִי וּבְשָׂרִי … וַיֵּשֶׁב עִמּוֹ› (“bone-me/my and-flesh-me/my …
# and-dwell/sit with-him/its”) — fact holds: bone-flesh-kinship-month-dwell
m.fact("bone_flesh_kinship_month_dwell")
# witness-tier presupposed read: welcome_decoded_as_a_stripping_threat on
# my_bone_and_my_flesh — read, not installed
m.witness_read("my_bone_and_my_flesh", "welcome_decoded_as_a_stripping_threat",
                cites=["Bereshit Rabbah 70:14", "Onkelos Genesis 29:14"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hashqu_lekhu_reu(ha_roim)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['yaaqov_lifted_feet_walked_east', 'well_three_flocks_great_stone_on_mouth', 'stone_protocol_gather_roll_water_return', 'shepherds_are_from_charan', 'shepherds_know_lavan_ben_nachor', 'shalom_confirmed_rachel_approaching', 'refusal_lo_nukhal_stone_grounds', 'rachel_arrived_shepherdess_while_speaking', 'demander_performed_roll_and_water', 'kiss_lifted_voice_weeping', 'identity_told_rachel_ran_told_father', 'lavan_heard_ran_embraced_kissed_housed_recounted', 'bone_flesh_kinship_month_dwell'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 1
    assert sorted(m.WORLD["witnessed"]) == ['the_well_frame']
    assert m.WORLD["witnessed"]['the_well_frame']["cites"] == ['Bereshit Rabbah 70:8']
    assert all('one_machine_bound_to_six_institutions' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_seventh_binding', 'sinai_with_an_all_or_nothing_gate'), ('the_greeting', 're_keyed_clause_by_clause_to_the_exile'), ('the_shepherds_rebuke', 'labour_duty_from_an_exhaustive_disjunction'), ('the_stone_rolled', 'strength_exhibit_recorded_at_its_verse'), ('the_kiss', 'classified_against_an_exhaustive_table'), ('her_fathers_brother', 'ambiguity_kept_by_one_member_removed_by_the_other'), ('my_bone_and_my_flesh', 'welcome_decoded_as_a_stripping_threat')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 70:9']
    assert all('sinai_with_an_all_or_nothing_gate' not in f for f in m.WORLD["facts"])
    assert 'the_seventh_binding' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 70:10']
    assert all('re_keyed_clause_by_clause_to_the_exile' not in f for f in m.WORLD["facts"])
    assert 'the_greeting' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 70:11']
    assert all('labour_duty_from_an_exhaustive_disjunction' not in f for f in m.WORLD["facts"])
    assert 'the_shepherds_rebuke' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 70:12']
    assert all('strength_exhibit_recorded_at_its_verse' not in f for f in m.WORLD["facts"])
    assert 'the_stone_rolled' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 70:12']
    assert all('classified_against_an_exhaustive_table' not in f for f in m.WORLD["facts"])
    assert 'the_kiss' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 70:13', 'Onkelos Genesis 29:12']
    assert all('ambiguity_kept_by_one_member_removed_by_the_other' not in f for f in m.WORLD["facts"])
    assert 'her_fathers_brother' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 70:14', 'Onkelos Genesis 29:14']
    assert all('welcome_decoded_as_a_stripping_threat' not in f for f in m.WORLD["facts"])
    assert 'my_bone_and_my_flesh' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
