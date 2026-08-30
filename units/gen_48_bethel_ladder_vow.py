#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_48_bethel_ladder_vow — 28:10-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_48_bethel_ladder_vow.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The Bethel ladder, the name write, and the first vow (28:10-22)"""
from machine import Machine

m = Machine("gen_48_bethel_ladder_vow")

# -------------------------- Gen.28.10 · THE_DEPARTURE_BEER_SHEVA_TO_HARAN --
# וַיֵּצֵא יַעֲקֹב מִבְּאֵר שָׁבַע וַיֵּלֶךְ חָרָנָה
# "[EN-AID] And Jacob went out from Beer-sheva and went toward Haran."
m.step("Gen.28.10")
# ‹וַיֵּצֵא … וַיֵּלֶךְ חָרָנָה› (“and-bring-forth … and-go Haran-ward”) —
# fact holds: Jacob-departed-from-seven-toward-charan
m.fact("yaaqov_departed_beer_sheva_toward_charan")
# witness-tier presupposed read:
# the_traditions_own_grammar_rule_at_this_word on directional_ending — read,
# not installed
m.witness_read("directional_ending", "the_traditions_own_grammar_rule_at_this_word",
                cites=["Bereshit Rabbah 68:8"])
# witness-tier presupposed read: radiance_rule_made_comparative_to_survive
# on the_departure — read, not installed
m.witness_read("the_departure", "radiance_rule_made_comparative_to_survive",
                cites=["Bereshit Rabbah 68:6"])

# -------------------------- Gen.28.11 · THE_PLACE_SUNSET_AND_STONE_PILLOW --
# וַיִּפְגַּע בַּמָּקוֹם וַיָּלֶן שָׁם כִּי־בָא הַשֶּׁמֶשׁ וַיִּקַּח
# מֵאַבְנֵי הַמָּקוֹם וַיָּשֶׂם מְרַאֲשֹׁתָיו וַיִּשְׁכַּב בַּמָּקוֹם הַהוּא
# "[EN-AID] And he lit upon the place and lodged there, for the sun had set;
# and he took of the stones of the place and set them at his head, and lay
# down in that place."
m.step("Gen.28.11")
# ‹כִּי־בָא הַשֶּׁמֶשׁ … מֵאַבְנֵי הַמָּקוֹם› (“that come/bring the-sun …
# from-stone the-place”) — fact holds: sun-set-stone-pillow-at-the-place
m.fact("sun_set_stone_pillow_at_ha_maqom")
# witness-tier presupposed read: three_counts_each_framed_as_a_test on
# the_stones — read, not installed
m.witness_read("the_stones", "three_counts_each_framed_as_a_test",
                cites=["Bereshit Rabbah 68:11"])
# witness-tier presupposed read: borrowed_time_booked_for_repayment on
# sunset_two_hours_early — read, not installed
m.witness_read("sunset_two_hours_early", "borrowed_time_booked_for_repayment",
                cites=["Bereshit Rabbah 68:10"])

# -------------------------- Gen.28.12 · THE_DREAM_DEBUT_AND_LADDER_HAPAX ---
# וַיַּחֲלֹם וְהִנֵּה סֻלָּם מֻצָּב אַרְצָה וְרֹאשׁוֹ מַגִּיעַ הַשָּׁמָיְמָה
# וְהִנֵּה מַלְאֲכֵי אֱלֹהִים עֹלִים וְיֹרְדִים בּוֹ
# "[EN-AID] And he dreamed — and behold a ladder set earthward, its head
# reaching heavenward; and behold, angels of God ascending and descending on
# it."
m.step("Gen.28.12")
# ‹וַיַּחֲלֹם› (“and-bind-firmly”) — event: ?
m.event("?")
# ‹סֻלָּם מֻצָּב אַרְצָה› (“stair-case stand earth-ward”) — fact holds:
# stair-case-earthward-head-heavenward-angels
m.fact("sulam_earthward_head_heavenward_angels")
# witness-tier presupposed read: dreams_follow_the_interpretation on
# the_dream — read, not installed
m.witness_read("the_dream", "dreams_follow_the_interpretation",
                cites=["Bereshit Rabbah 68:12"])
# witness-tier presupposed read: kingdom_sequence_read_off_the_word_order on
# ascending_and_descending — read, not installed
m.witness_read("ascending_and_descending", "kingdom_sequence_read_off_the_word_order",
                cites=["Bereshit Rabbah 68:14"])

# -------------------------- Gen.28.13 · THE_STATIONED_LORD_AND_LAND_COMMITMENT -
# וְהִנֵּה יְהוָה נִצָּב עָלָיו וַיֹּאמַר אֲנִי יְהוָה אֱלֹהֵי אַבְרָהָם
# אָבִיךָ וֵאלֹהֵי יִצְחָק הָאָרֶץ אֲשֶׁר אַתָּה שֹׁכֵב עָלֶיהָ לְךָ
# אֶתְּנֶנָּה וּלְזַרְעֶךָ
# "[EN-AID] And behold, YHWH stood over him and said: I am YHWH, God of
# Abraham your father and God of Isaac; the land on which you lie, to you I
# will give it and to your seed."
m.step("Gen.28.13")
# ‹נִצָּב עָלָיו … לְךָ אֶתְּנֶנָּה› (“stand over-him/its … to-you/your set-
# her/its”) — fact holds: the-LORD-stand-self-identification-land-commitment
m.fact("YHWH_nitzav_self_identification_land_commitment")
# witness-tier presupposed read: opened_frame_stated_leg_left_open on
# the_eighteen_count — read, not installed
m.witness_read("the_eighteen_count", "opened_frame_stated_leg_left_open",
                cites=["Bereshit Rabbah 69:4"])
# witness-tier presupposed read: glory_buffer_at_both_theophany_verses on
# the_LORD_stood_over_him — read, not installed
m.witness_read("the_LORD_stood_over_him", "glory_buffer_at_both_theophany_verses",
                cites=["Onkelos Genesis 28:13", "Onkelos Genesis 28:16"])

# -------------------------- Gen.28.14 · THE_DUST_FORMULA_ALL_FAMILIES_NIPHAL -
# וְהָיָה זַרְעֲךָ כַּעֲפַר הָאָרֶץ וּפָרַצְתָּ יָמָּה וָקֵדְמָה וְצָפֹנָה
# וָנֶגְבָּה וְנִבְרֲכוּ בְךָ כָּל־מִשְׁפְּחֹת הָאֲדָמָה וּבְזַרְעֶךָ
# "[EN-AID] And your seed shall be as the dust of the earth, and you shall
# spread west and east and north and south; and all the families of the
# ground shall be blessed in you and in your seed."
m.step("Gen.28.14")
# ‹כַּעֲפַר הָאָרֶץ … וְנִבְרֲכוּ בְךָ› (“like-dust the-earth … and-bless
# in-you/your”) — fact holds: dust-seed-spread-all-families-blessed
m.fact("dust_seed_spread_all_families_blessed")

# -------------------------- Gen.28.15 · THE_FIVE_FOLD_PROMISE_NOT_LEAVE ----
# וְהִנֵּה אָנֹכִי עִמָּךְ וּשְׁמַרְתִּיךָ בְּכֹל אֲשֶׁר־תֵּלֵךְ
# וַהֲשִׁבֹתִיךָ אֶל־הָאֲדָמָה הַזֹּאת כִּי לֹא אֶעֱזָבְךָ עַד אֲשֶׁר
# אִם־עָשִׂיתִי אֵת אֲשֶׁר־דִּבַּרְתִּי לָךְ
# "[EN-AID] And behold, I am with you, and I will keep you wherever you go,
# and I will bring you back to this ground; for I will not leave you until I
# have done what I have spoken to you."
m.step("Gen.28.15")
# ‹וּשְׁמַרְתִּיךָ … וַהֲשִׁבֹתִיךָ … לֹא אֶעֱזָבְךָ› (“and-keep/guard-
# you/your … and-return-you/your … not loosen-you/your”) — fact holds: five-
# fold-promise-with-keep-return-not-leave-until-done
m.fact("five_fold_promise_with_keep_return_not_leave_until_done")
# witness-tier presupposed read:
# clause_map_against_the_vow_with_one_field_uncovered on the_promise — read,
# not installed
m.witness_read("the_promise", "clause_map_against_the_vow_with_one_field_uncovered",
                cites=["Bereshit Rabbah 69:6"])
# witness-tier presupposed read: condition_made_to_quote_the_promise on
# my_word_is_your_support — read, not installed
m.witness_read("my_word_is_your_support", "condition_made_to_quote_the_promise",
                cites=["Onkelos Genesis 28:15", "Onkelos Genesis 28:20"])

# -------------------------- Gen.28.16 · THE_WAKING_AKHEN_AND_NOT_KNOWING ---
# וַיִּיקַץ יַעֲקֹב מִשְּׁנָתוֹ וַיֹּאמֶר אָכֵן יֵשׁ יְהוָה בַּמָּקוֹם
# הַזֶּה וְאָנֹכִי לֹא יָדָעְתִּי
# "[EN-AID] And Jacob awoke from his sleep and said: Surely YHWH is in this
# place, and I did not know."
m.step("Gen.28.16")
# ‹וַיִּיקַץ … אָכֵן … לֹא יָדָעְתִּי› (“and-awake … firmly … not know”) —
# fact holds: Jacob-woke-firmly-the-LORD-in-place-unknown
m.fact("yaaqov_woke_akhen_YHWH_in_place_unknown")

# -------------------------- Gen.28.17 · THE_FEAR_DOUBLET_GATE_OF_HEAVEN ----
# וַיִּירָא וַיֹּאמַר מַה־נּוֹרָא הַמָּקוֹם הַזֶּה אֵין זֶה כִּי אִם־בֵּית
# אֱלֹהִים וְזֶה שַׁעַר הַשָּׁמָיִם
# "[EN-AID] And he feared and said: How awesome is this place! This is none
# other than the house of God, and this is the gate of heaven."
m.step("Gen.28.17")
# ‹וַיִּירָא … מַה־נּוֹרָא … שַׁעַר הַשָּׁמָיִם› (“and-fear … what fear …
# gate the-heavens”) — fact holds: fear-doublet-house-God-gate-the-heavens
m.fact("fear_doublet_bet_elohim_shaar_ha_shamayim")
# witness-tier presupposed read: de_literalized_into_prayer_reception on
# house_of_God — read, not installed
m.witness_read("house_of_God", "de_literalized_into_prayer_reception",
                cites=["Onkelos Genesis 28:17", "Onkelos Genesis 28:22"])

# -------------------------- Gen.28.18 · THE_PILLAR_AND_THE_OIL_DEBUT -------
# וַיַּשְׁכֵּם יַעֲקֹב בַּבֹּקֶר וַיִּקַּח אֶת־הָאֶבֶן אֲשֶׁר־שָׂם
# מְרַאֲשֹׁתָיו וַיָּשֶׂם אֹתָהּ מַצֵּבָה וַיִּצֹק שֶׁמֶן עַל־רֹאשָׁהּ
# "[EN-AID] And Jacob rose early in the morning and took the stone he had
# set at his head, and set it as a pillar, and poured oil on its head."
m.step("Gen.28.18")
# ‹וַיָּשֶׂם אֹתָהּ מַצֵּבָה וַיִּצֹק שֶׁמֶן› (“and-put/set obj-marker-
# her/its pillar and-pour-out oil”) — event: ?
m.event("?")
# ‹וַיַּשְׁכֵּם … וַיִּקַּח אֶת־הָאֶבֶן› (“and-rise-early … and-take obj-
# marker the-stone”) — fact holds: early-rise-stone-taken-set-as-pillar
m.fact("early_rise_stone_taken_set_as_pillar")

# -------------------------- Gen.28.19 · THE_NAME_WRITE_BEIT_EL -------------
# וַיִּקְרָא אֶת־שֵׁם־הַמָּקוֹם הַהוּא בֵּית־אֵל וְאוּלָם לוּז שֵׁם־הָעִיר
# לָרִאשֹׁנָה
# "[EN-AID] And he called the name of that place Bethel; but Luz was the
# name of the city at first."
m.step("Gen.28.19")
# ‹וַיִּקְרָא אֶת־שֵׁם־הַמָּקוֹם הַהוּא בֵּית־אֵל› (“and-call obj-marker
# name the-place that Beth-el”) — named: the-place-Luz := beit-to
m.name("ha_maqom_luz", "beit_el")
# witness-grounded state (its own tier):
# permanent_properties_across_the_corpus on the_city
m.witness_state("the_city", "permanent_properties_across_the_corpus",
                cites=["Bereshit Rabbah 69:8"])

# -------------------------- Gen.28.20 · THE_FIRST_VOW_CONDITIONS_OPEN ------
# וַיִּדַּר יַעֲקֹב נֶדֶר לֵאמֹר אִם־יִהְיֶה אֱלֹהִים עִמָּדִי וּשְׁמָרַנִי
# בַּדֶּרֶךְ הַזֶּה אֲשֶׁר אָנֹכִי הוֹלֵךְ וְנָתַן־לִי לֶחֶם לֶאֱכֹל וּבֶגֶד
# לִלְבֹּשׁ
# "[EN-AID] And Jacob vowed a vow, saying: If God will be with me and keep
# me on this way that I go, and give me bread to eat and a garment to wear
# —"
m.step("Gen.28.20")
# ‹וַיִּדַּר יַעֲקֹב נֶדֶר … לֶחֶם … וּבֶגֶד› (“and-promise Jacob promise …
# food … and-garment”) — fact holds: promise-opened-conditions-with-keep-
# bread-garment
m.fact("neder_opened_conditions_with_keep_bread_garment")
# witness-tier presupposed read:
# first_instance_chain_of_title_and_a_register on the_vow — read, not
# installed
m.witness_read("the_vow", "first_instance_chain_of_title_and_a_register",
                cites=["Bereshit Rabbah 70:1", "Bereshit Rabbah 70:3"])
# witness-tier presupposed read: audit_penalty_that_explains_the_loss on
# delay_in_discharge — read, not installed
m.witness_read("delay_in_discharge", "audit_penalty_that_explains_the_loss",
                cites=["Bereshit Rabbah 81:1"])

# -------------------------- Gen.28.21 · THE_RETURN_IN_PEACE_AND_THEN_CLAUSE -
# וְשַׁבְתִּי בְשָׁלוֹם אֶל־בֵּית אָבִי וְהָיָה יְהוָה לִי לֵאלֹהִים
# "[EN-AID] And I return in peace to my father's house — then YHWH will be
# my God."
m.step("Gen.28.21")
# ‹וְשַׁבְתִּי בְשָׁלוֹם … וְהָיָה יְהוָה לִי לֵאלֹהִים› (“and-return in-
# safe … and-be YHWH to-me/my to-God”) — fact holds: return-in-peace-
# condition-then-the-LORD-my-God
m.fact("return_in_peace_condition_then_YHWH_my_God")

# -------------------------- Gen.28.22 · THE_VOW_HANDLER_STONE_HOUSE_TITHE --
# וְהָאֶבֶן הַזֹּאת אֲשֶׁר־שַׂמְתִּי מַצֵּבָה יִהְיֶה בֵּית אֱלֹהִים וְכֹל
# אֲשֶׁר תִּתֶּן־לִי עַשֵּׂר אֲעַשְּׂרֶנּוּ לָךְ
# "[EN-AID] And this stone which I have set as a pillar shall be the house
# of God; and all that You give me I will surely tithe to You."
m.step("Gen.28.22")
# ‹אִם־יִהְיֶה אֱלֹהִים עִמָּדִי … עַשֵּׂר אֲעַשְּׂרֶנּוּ לָךְ› (“if be God
# along-with-me/my … tithe tithe-him/its to-you/your”) — standing handler —
# if God-with-me ∧ shemarani-in-the-derekh ∧ set-food-and-garment ∧ return-
# and-safe then the-LORD-to-me-to-God ∧ the-stone-house-God ∧ tithe-aasrenu
m.handler("elohim_imadi ∧ shemarani_ba_derekh ∧ natan_lechem_u_veged ∧ shavti_ve_shalom",
          "YHWH_li_le_Elohim ∧ ha_even_bet_Elohim ∧ aser_aasrenu")
# ‹וְהָאֶבֶן הַזֹּאת … עַשֵּׂר אֲעַשְּׂרֶנּוּ› (“and-the-stone the-this …
# tithe tithe-him/its”) — fact holds: stone-house-tithe-vow-content
m.fact("stone_house_tithe_vow_content")
# witness-tier presupposed read:
# challenged_by_arithmetic_and_rescued_by_exclusion on the_tithe_promise —
# read, not installed
m.witness_read("the_tithe_promise", "challenged_by_arithmetic_and_rescued_by_exclusion",
                cites=["Bereshit Rabbah 70:7"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha_maqom_luz': 'beit_el'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['yaaqov_departed_beer_sheva_toward_charan', 'sun_set_stone_pillow_at_ha_maqom', 'sulam_earthward_head_heavenward_angels', 'YHWH_nitzav_self_identification_land_commitment', 'dust_seed_spread_all_families_blessed', 'five_fold_promise_with_keep_return_not_leave_until_done', 'yaaqov_woke_akhen_YHWH_in_place_unknown', 'fear_doublet_bet_elohim_shaar_ha_shamayim', 'early_rise_stone_taken_set_as_pillar', 'neder_opened_conditions_with_keep_bread_garment', 'return_in_peace_condition_then_YHWH_my_God', 'handler: IF(elohim_imadi ∧ shemarani_ba_derekh ∧ natan_lechem_u_veged ∧ shavti_ve_shalom) THEN(YHWH_li_le_Elohim ∧ ha_even_bet_Elohim ∧ aser_aasrenu)', 'stone_house_tithe_vow_content'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    assert sorted(m.WORLD["witnessed"]) == ['the_city']
    assert m.WORLD["witnessed"]['the_city']["cites"] == ['Bereshit Rabbah 69:8']
    assert all('permanent_properties_across_the_corpus' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('directional_ending', 'the_traditions_own_grammar_rule_at_this_word'), ('the_departure', 'radiance_rule_made_comparative_to_survive'), ('the_stones', 'three_counts_each_framed_as_a_test'), ('sunset_two_hours_early', 'borrowed_time_booked_for_repayment'), ('the_dream', 'dreams_follow_the_interpretation'), ('ascending_and_descending', 'kingdom_sequence_read_off_the_word_order'), ('the_eighteen_count', 'opened_frame_stated_leg_left_open'), ('the_LORD_stood_over_him', 'glory_buffer_at_both_theophany_verses'), ('the_promise', 'clause_map_against_the_vow_with_one_field_uncovered'), ('my_word_is_your_support', 'condition_made_to_quote_the_promise'), ('house_of_God', 'de_literalized_into_prayer_reception'), ('the_vow', 'first_instance_chain_of_title_and_a_register'), ('delay_in_discharge', 'audit_penalty_that_explains_the_loss'), ('the_tithe_promise', 'challenged_by_arithmetic_and_rescued_by_exclusion')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 68:8']
    assert all('the_traditions_own_grammar_rule_at_this_word' not in f for f in m.WORLD["facts"])
    assert 'directional_ending' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 68:6']
    assert all('radiance_rule_made_comparative_to_survive' not in f for f in m.WORLD["facts"])
    assert 'the_departure' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 68:11']
    assert all('three_counts_each_framed_as_a_test' not in f for f in m.WORLD["facts"])
    assert 'the_stones' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 68:10']
    assert all('borrowed_time_booked_for_repayment' not in f for f in m.WORLD["facts"])
    assert 'sunset_two_hours_early' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 68:12']
    assert all('dreams_follow_the_interpretation' not in f for f in m.WORLD["facts"])
    assert 'the_dream' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 68:14']
    assert all('kingdom_sequence_read_off_the_word_order' not in f for f in m.WORLD["facts"])
    assert 'ascending_and_descending' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 69:4']
    assert all('opened_frame_stated_leg_left_open' not in f for f in m.WORLD["facts"])
    assert 'the_eighteen_count' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Genesis 28:13', 'Onkelos Genesis 28:16']
    assert all('glory_buffer_at_both_theophany_verses' not in f for f in m.WORLD["facts"])
    assert 'the_LORD_stood_over_him' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 69:6']
    assert all('clause_map_against_the_vow_with_one_field_uncovered' not in f for f in m.WORLD["facts"])
    assert 'the_promise' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Onkelos Genesis 28:15', 'Onkelos Genesis 28:20']
    assert all('condition_made_to_quote_the_promise' not in f for f in m.WORLD["facts"])
    assert 'my_word_is_your_support' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Genesis 28:17', 'Onkelos Genesis 28:22']
    assert all('de_literalized_into_prayer_reception' not in f for f in m.WORLD["facts"])
    assert 'house_of_God' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 70:1', 'Bereshit Rabbah 70:3']
    assert all('first_instance_chain_of_title_and_a_register' not in f for f in m.WORLD["facts"])
    assert 'the_vow' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 81:1']
    assert all('audit_penalty_that_explains_the_loss' not in f for f in m.WORLD["facts"])
    assert 'delay_in_discharge' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Bereshit Rabbah 70:7']
    assert all('challenged_by_arithmetic_and_rescued_by_exclusion' not in f for f in m.WORLD["facts"])
    assert 'the_tithe_promise' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
