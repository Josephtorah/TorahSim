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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
