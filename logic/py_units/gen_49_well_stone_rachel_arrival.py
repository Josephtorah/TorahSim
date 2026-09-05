#!/usr/bin/env python3
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
# ‹וַיִּשָּׂא יַעֲקֹב רַגְלָיו› (“and-lift/carry Jacob foot-him/its”)
# ‹וַיֵּלֶךְ אַרְצָה בְנֵי־קֶדֶם› (“and-go earth-ward son front”)
# "[EN-AID] And Jacob lifted his feet and went to the land of the children
# of the east."
m.step("Gen.29.1")
# ‹וַיִּשָּׂא … רַגְלָיו … קֶדֶם› (“and-lift/carry … foot-him/its … front”)
# — fact holds: Jacob-lifted-feet-walked-east
m.fact("yaaqov_lifted_feet_walked_east")

# -------------------------- Gen.29.2 · THE_WELL_THREE_FLOCKS_GREAT_STONE ---
# ‹וַיַּרְא וְהִנֵּה בְאֵר› (“and-see and-behold pit”)
# ‹בַּשָּׂדֶה וְהִנֵּה־שָׁם שְׁלֹשָׁה› (“in-field and-behold there three”)
# ‹עֶדְרֵי־צֹאן רֹבְצִים עָלֶיהָ› (“arrangement flock crouch over-her/its”)
# ‹כִּי מִן־הַבְּאֵר הַהִוא› (“that from the-pit that”)
# ‹יַשְׁקוּ הָעֲדָרִים וְהָאֶבֶן› (“give-drink the-arrangement and-the-
# stone”)
# ‹גְּדֹלָה עַל־פִּי הַבְּאֵר› (“great over mouth the-pit”)
# "[EN-AID] And he saw — behold a well in the field, and behold three flocks
# of sheep crouching by it, for from that well the flocks were watered; and
# the stone was great on the mouth of the well."
m.step("Gen.29.2")
# ‹רֹבְצִים … וְהָאֶבֶן גְּדֹלָה› (“crouch … and-the-stone great”)
# — fact holds: well-three-flocks-great-stone-on-mouth
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
# ‹וְנֶאֶסְפוּ־שָׁמָּה כָל־הָעֲדָרִים וְגָלֲלוּ› (“and-gather-for-any-
# purpose there-ward all the-arrangement and-roll”)
# ‹אֶת־הָאֶבֶן מֵעַל פִּי› (“obj-marker the-stone from-over mouth”)
# ‹הַבְּאֵר וְהִשְׁקוּ אֶת־הַצֹּאן› (“the-pit and-give-drink obj-marker the-
# flock”)
# ‹וְהֵשִׁיבוּ אֶת־הָאֶבֶן עַל־פִּי› (“and-return obj-marker the-stone over
# mouth”)
# ‹הַבְּאֵר לִמְקֹמָהּ› (“the-pit to-place-her/its”)
# "[EN-AID] And all the flocks would gather there, and they would roll the
# stone from the mouth of the well and water the sheep, and return the stone
# to its place on the mouth of the well."
m.step("Gen.29.3")
# ‹וְגָלֲלוּ … וְהִשְׁקוּ … וְהֵשִׁיבוּ› (“and-roll … and-give-drink … and-
# return”)
# — fact holds: stone-protocol-gather-roll-water-return
m.fact("stone_protocol_gather_roll_water_return")

# -------------------------- Gen.29.4 · THE_MY_BROTHERS_FROM_HARAN ----------
# ‹וַיֹּאמֶר לָהֶם יַעֲקֹב› (“and-say to-them/their Jacob”)
# ‹אַחַי מֵאַיִן אַתֶּם› (“brother-me/my from-where? you”)
# ‹וַיֹּאמְרוּ מֵחָרָן אֲנָחְנוּ› (“and-say from-Haran we”)
# "[EN-AID] And Jacob said to them: My brothers, from where are you? And
# they said: From Haran are we."
m.step("Gen.29.4")
# ‹אַחַי מֵאַיִן אַתֶּם› (“brother-me/my from-where? you”)
# ‹… מֵחָרָן› (“from-Haran”)
# — fact holds: shepherds-are-from-Haran
m.fact("shepherds_are_from_charan")
# witness-tier presupposed read: re_keyed_clause_by_clause_to_the_exile on
# the_greeting — read, not installed
m.witness_read("the_greeting", "re_keyed_clause_by_clause_to_the_exile",
                cites=["Bereshit Rabbah 70:10"])

# -------------------------- Gen.29.5 · THE_KNOW_CHAIN_AND_GRANDFATHER_SKIP -
# ‹וַיֹּאמֶר לָהֶם הַיְדַעְתֶּם› (“and-say to-them/their the-know”)
# ‹אֶת־לָבָן בֶּן־נָחוֹר וַיֹּאמְרוּ› (“obj-marker Laban son Nahor and-say”)
# ‹יָדָעְנוּ› (“know”)
# "[EN-AID] And he said to them: Do you know Laban son of Nachor? And they
# said: We know."
m.step("Gen.29.5")
# ‹הַיְדַעְתֶּם … בֶּן־נָחוֹר … יָדָעְנוּ› (“the-know … son Nahor … know”)
# — fact holds: shepherds-know-Laban-son-Nahor
m.fact("shepherds_know_lavan_ben_nachor")

# -------------------------- Gen.29.6 · THE_SHALOM_AND_RACHEL_DEBUT ---------
# ‹וַיֹּאמֶר לָהֶם הֲשָׁלוֹם› (“and-say to-them/their the-safe”)
# ‹לוֹ וַיֹּאמְרוּ שָׁלוֹם› (“to-him/its and-say safe”)
# ‹וְהִנֵּה רָחֵל בִּתּוֹ› (“and-behold Rachel daughter-him/its”)
# ‹בָּאָה עִם־הַצֹּאן› (“come/bring with the-flock”)
# "[EN-AID] And he said to them: Is there peace to him? And they said: Peace
# — and behold Rachel his daughter comes with the sheep."
m.step("Gen.29.6")
# ‹הֲשָׁלוֹם לוֹ … וְהִנֵּה› (“the-safe to-him/its … and-behold”)
# ‹רָחֵל› (“Rachel”)
# — fact holds: safe-confirmed-Rachel-approaching
m.fact("shalom_confirmed_rachel_approaching")

# -------------------------- Gen.29.7 · THE_COMPOUND_PUSH_ON_THE_SHEPHERDS --
# ‹וַיֹּאמֶר הֵן עוֹד› (“and-say lo! still/again”)
# ‹הַיּוֹם גָּדוֹל לֹא־עֵת› (“the-day great not time”)
# ‹הֵאָסֵף הַמִּקְנֶה הַשְׁקוּ› (“gather-for-any-purpose the-something-
# bought give-drink”)
# ‹הַצֹּאן וּלְכוּ רְעוּ› (“the-flock and-go graze”)
# "[EN-AID] And he said: Behold, the day is still great; it is not time for
# the livestock to be gathered — water the sheep and go, pasture."
m.step("Gen.29.7")
# ‹הַשְׁקוּ הַצֹּאן וּלְכוּ› (“give-drink the-flock and-go”)
# ‹רְעוּ› (“graze”)
# — Jacob speaks a demand — LET: give-drink-go-graze(the-roim)
m.declare("yaaqov", "LET",
          "hashqu_lekhu_reu(ha_roim)")
# witness-tier presupposed read: labour_duty_from_an_exhaustive_disjunction
# on the_shepherds_rebuke — read, not installed
m.witness_read("the_shepherds_rebuke", "labour_duty_from_an_exhaustive_disjunction",
                cites=["Bereshit Rabbah 70:11"])

# -------------------------- Gen.29.8 · THE_REFUSAL_WITH_STONE_GROUNDS ------
# ‹וַיֹּאמְרוּ לֹא נוּכַל› (“and-say not be-able”)
# ‹עַד אֲשֶׁר יֵאָסְפוּ› (“until which gather-for-any-purpose”)
# ‹כָּל־הָעֲדָרִים וְגָלֲלוּ אֶת־הָאֶבֶן› (“all the-arrangement and-roll
# obj-marker the-stone”)
# ‹מֵעַל פִּי הַבְּאֵר› (“from-over mouth the-pit”)
# ‹וְהִשְׁקִינוּ הַצֹּאן› (“and-give-drink the-flock”)
# "[EN-AID] And they said: We cannot, until all the flocks are gathered and
# they roll the stone from the mouth of the well — then we water the sheep."
m.step("Gen.29.8")
# ‹לֹא נוּכַל עַד› (“not be-able until”)
# ‹אֲשֶׁר …› (“which”)
# — fact holds: refusal-not-be-able-stone-grounds
m.fact("refusal_lo_nukhal_stone_grounds")

# -------------------------- Gen.29.9 · THE_STILL_SPEAKING_SHEPHERDESS ------
# ‹עוֹדֶנּוּ מְדַבֵּר עִמָּם› (“still/again-him/its speak with-them/their”)
# ‹וְרָחֵל בָּאָה עִם־הַצֹּאן› (“and-Rachel come/bring with the-flock”)
# ‹אֲשֶׁר לְאָבִיהָ כִּי› (“which to-father-her/its that”)
# ‹רֹעָה הִוא› (“graze he/it”)
# "[EN-AID] While he was still speaking with them, Rachel came with the
# sheep that were her father's, for she was a shepherdess."
m.step("Gen.29.9")
# ‹עוֹדֶנּוּ מְדַבֵּר … כִּי› (“still/again-him/its speak … that”)
# ‹רֹעָה הִוא› (“graze he/it”)
# — fact holds: Rachel-arrived-shepherdess-while-speaking
m.fact("rachel_arrived_shepherdess_while_speaking")

# -------------------------- Gen.29.10 · THE_DEMANDER_PERFORMS_ROLL_AND_WATER -
# ‹וַיְהִי כַּאֲשֶׁר רָאָה› (“and-be like-as/which see”)
# ‹יַעֲקֹב אֶת־רָחֵל בַּת־לָבָן› (“Jacob obj-marker Rachel daughter Laban”)
# ‹אֲחִי אִמּוֹ וְאֶת־צֹאן› (“brother mother-him/its and-obj-marker flock”)
# ‹לָבָן אֲחִי אִמּוֹ› (“Laban brother mother-him/its”)
# ‹וַיִּגַּשׁ יַעֲקֹב וַיָּגֶל› (“and-be Jacob and-roll”)
# ‹אֶת־הָאֶבֶן מֵעַל פִּי› (“obj-marker the-stone from-over mouth”)
# ‹הַבְּאֵר וַיַּשְׁקְ אֶת־צֹאן› (“the-pit and-give-drink obj-marker flock”)
# ‹לָבָן אֲחִי אִמּוֹ› (“Laban brother mother-him/its”)
# "[EN-AID] And it was, when Jacob saw Rachel daughter of Laban his mother's
# brother, and the sheep of Laban his mother's brother, that Jacob drew near
# and rolled the stone from the mouth of the well, and watered the sheep of
# Laban his mother's brother."
m.step("Gen.29.10")
# ‹וַיִּגַּשׁ … וַיָּגֶל … וַיַּשְׁקְ› (“and-be … and-roll … and-give-
# drink”)
# — fact holds: demander-performed-roll-and-water
m.fact("demander_performed_roll_and_water")
# witness-tier presupposed read: strength_exhibit_recorded_at_its_verse on
# the_stone_rolled — read, not installed
m.witness_read("the_stone_rolled", "strength_exhibit_recorded_at_its_verse",
                cites=["Bereshit Rabbah 70:12"])

# -------------------------- Gen.29.11 · THE_KISS_VOICE_AND_WEEPING ---------
# ‹וַיִּשַּׁק יַעֲקֹב לְרָחֵל› (“and-kiss Jacob to-Rachel”)
# ‹וַיִּשָּׂא אֶת־קֹלוֹ וַיֵּבְךְּ› (“and-lift/carry obj-marker voice/sound-
# him/its and-weep”)
# "[EN-AID] And Jacob kissed Rachel, and lifted his voice, and wept."
m.step("Gen.29.11")
# ‹וַיִּשַּׁק … וַיִּשָּׂא אֶת־קֹלוֹ› (“and-kiss … and-lift/carry obj-marker
# voice/sound-him/its”)
# ‹וַיֵּבְךְּ› (“and-weep”)
# — fact holds: kiss-lifted-voice-weeping
m.fact("kiss_lifted_voice_weeping")
# witness-tier presupposed read: classified_against_an_exhaustive_table on
# the_kiss — read, not installed
m.witness_read("the_kiss", "classified_against_an_exhaustive_table",
                cites=["Bereshit Rabbah 70:12"])

# -------------------------- Gen.29.12 · THE_TELL_CHAIN_AND_HER_RUN ---------
# ‹וַיַּגֵּד יַעֲקֹב לְרָחֵל› (“and-tell Jacob to-Rachel”)
# ‹כִּי אֲחִי אָבִיהָ› (“that brother father-her/its”)
# ‹הוּא וְכִי בֶן־רִבְקָה› (“he/it and-that son Rebekah”)
# ‹הוּא וַתָּרָץ וַתַּגֵּד› (“he/it and-run and-tell”)
# ‹לְאָבִיהָ› (“to-father-her/its”)
# "[EN-AID] And Jacob told Rachel that he was her father's kinsman and that
# he was Rivqah's son; and she ran and told her father."
m.step("Gen.29.12")
# ‹וַיַּגֵּד … וַתָּרָץ וַתַּגֵּד› (“and-tell … and-run and-tell”)
# — fact holds: identity-told-Rachel-ran-told-father
m.fact("identity_told_rachel_ran_told_father")
# witness-tier presupposed read:
# ambiguity_kept_by_one_member_removed_by_the_other on her_fathers_brother —
# read, not installed
m.witness_read("her_fathers_brother", "ambiguity_kept_by_one_member_removed_by_the_other",
                cites=["Bereshit Rabbah 70:13", "Onkelos Genesis 29:12"])

# -------------------------- Gen.29.13 · THE_SECOND_RUN_EMBRACE_KISS_RECOUNT -
# ‹וַיְהִי כִשְׁמֹעַ לָבָן› (“and-be like-hear Laban”)
# ‹אֶת־שֵׁמַע יַעֲקֹב בֶּן־אֲחֹתוֹ› (“obj-marker something-heard Jacob son
# sister-him/its”)
# ‹וַיָּרָץ לִקְרָאתוֹ וַיְחַבֶּק־לוֹ› (“and-run to-encountering-him/its
# and-clasp to-him/its”)
# ‹וַיְנַשֶּׁק־לוֹ וַיְבִיאֵהוּ אֶל־בֵּיתוֹ› (“and-kiss to-him/its and-
# come/bring-him/its to house-him/its”)
# ‹וַיְסַפֵּר לְלָבָן אֵת› (“and-count to-Laban obj-marker”)
# ‹כָּל־הַדְּבָרִים הָאֵלֶּה› (“all the-word/thing the-these”)
# "[EN-AID] And it was, when Laban heard the report of Jacob his sister's
# son, that he ran to meet him, and embraced him, and kissed him, and
# brought him to his house; and he recounted to Laban all these things."
m.step("Gen.29.13")
# ‹כִשְׁמֹעַ … וַיָּרָץ … וַיְחַבֶּק› (“like-hear … and-run … and-clasp”)
# ‹… וַיְסַפֵּר› (“and-count”)
# — fact holds: Laban-heard-ran-embraced-kissed-housed-recounted
m.fact("lavan_heard_ran_embraced_kissed_housed_recounted")

# -------------------------- Gen.29.14 · THE_BONE_FLESH_AND_MONTH_DWELL -----
# ‹וַיֹּאמֶר לוֹ לָבָן› (“and-say to-him/its Laban”)
# ‹אַךְ עַצְמִי וּבְשָׂרִי› (“indeed bone-me/my and-flesh-me/my”)
# ‹אָתָּה וַיֵּשֶׁב עִמּוֹ› (“you and-dwell/sit with-him/its”)
# ‹חֹדֶשׁ יָמִים› (“new-moon day”)
# "[EN-AID] And Laban said to him: Surely you are my bone and my flesh. And
# he dwelt with him a month of days."
m.step("Gen.29.14")
# ‹עַצְמִי וּבְשָׂרִי … וַיֵּשֶׁב› (“bone-me/my and-flesh-me/my … and-
# dwell/sit”)
# ‹עִמּוֹ› (“with-him/its”)
# — fact holds: bone-flesh-kinship-month-dwell
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
