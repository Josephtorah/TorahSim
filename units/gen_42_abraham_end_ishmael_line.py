#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_42_abraham_end_ishmael_line — 25:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_42_abraham_end_ishmael_line.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Abraham's end and Ishmael's line (25:1-18)"""
from machine import Machine

m = Machine("gen_42_abraham_end_ishmael_line")

# -------------------------- Gen.25.1 · THE_KETURAH_REPORT_NAME -------------
# וַיֹּ֧סֶף אַבְרָהָ֛ם וַיִּקַּ֥ח אִשָּׁ֖ה וּשְׁמָ֥הּ קְטוּרָֽה
# "[EN-AID] And Abraham again took a wife, and her name was Keturah."
m.step("Gen.25.1")
# ‹וַיֹּסֶף … וַיִּקַּח אִשָּׁה› (“and-add … and-take woman”) — event: take-
# wife — agent Abraham; theme Keturah
m.event("take_wife", agent="avraham", themes=["qetura"])
# ‹וּשְׁמָהּ קְטוּרָה› (“and-name-her/its Keturah”) — fact holds: report-
# name-Keturah
m.fact("report_name_qetura")
# witness-tier presupposed read: evening_sowing_of_a_four_way_proverb on
# remarriage_in_old_age — read, not installed
m.witness_read("remarriage_in_old_age", "evening_sowing_of_a_four_way_proverb",
                cites=["Bereshit Rabbah 61:3"])
# witness-tier presupposed read: ink_leg_recorded_but_not_applied on
# ketura_identified_as_hagar — read, not installed
m.witness_read("ketura_identified_as_hagar", "ink_leg_recorded_but_not_applied",
                cites=["Bereshit Rabbah 61:4", "Bereshit Rabbah 47:2"])

# -------------------------- Gen.25.2 · THE_KETURAH_SIX_SONS ----------------
# וַתֵּ֣לֶד ל֗וֹ אֶת־זִמְרָן֙ וְאֶת־יָקְשָׁ֔ן וְאֶת־מְדָ֖ן וְאֶת־מִדְיָ֑ן
# וְאֶת־יִשְׁבָּ֖ק וְאֶת־שֽׁוּחַ
# "[EN-AID] And she bore him Zimran and Jokshan and Medan and Midian and
# Ishbak and Shuah."
m.step("Gen.25.2")
# ‹וַתֵּלֶד לוֹ› (“and-bear-young to-him/its”) — event: bear-sons — agent
# Keturah
m.event("bear_sons", agent="qetura")
# ‹זִמְרָן … יָקְשָׁן … מְדָן … מִדְיָן … יִשְׁבָּק … שׁוּחַ› (“Zimran …
# Jokshan … Medan … Midian … Ishbak … Shuah”) — fact holds: named-only-
# roster-Zimran-Jokshan-Medan-Midian-Ishbak-Shuah
m.fact("named_only_roster_zimran_yaqshan_medan_midyan_yishbaq_shucha")

# -------------------------- Gen.25.3 · THE_JOKSHAN_LINE --------------------
# וְיָקְשָׁ֣ן יָלַ֔ד אֶת־שְׁבָ֖א וְאֶת־דְּדָ֑ן וּבְנֵ֣י דְדָ֔ן הָי֛וּ
# אַשּׁוּרִ֥ם וּלְטוּשִׁ֖ים וּלְאֻמִּֽים
# "[EN-AID] And Jokshan begot Sheba and Dedan; and the sons of Dedan were
# Asshurim and Letushim and Leummim."
m.step("Gen.25.3")
# ‹שְׁבָא … דְּדָן … אַשּׁוּרִם וּלְטוּשִׁים וּלְאֻמִּים› (“Sheba … Dedan …
# Asshurim and-Letushim and-Leummim”) — fact holds: named-only-roster-
# Jokshan-line
m.fact("named_only_roster_yaqshan_line")
# witness-tier presupposed read: declared_shelf_splitting_three_ways_by_name
# on three_names — read, not installed
m.witness_read("three_names", "declared_shelf_splitting_three_ways_by_name",
                cites=["Bereshit Rabbah 61:5", "Onkelos Genesis 25:3"])

# -------------------------- Gen.25.4 · THE_MIDIAN_LINE_AND_CLOSE -----------
# וּבְנֵ֣י מִדְיָ֗ן עֵיפָ֤ה וָעֵ֨פֶר֙ וַחֲנֹ֔ךְ וַאֲבִידָ֖ע וְאֶלְדָּעָ֑ה
# כָּל־אֵ֖לֶּה בְּנֵ֥י קְטוּרָֽה
# "[EN-AID] And the sons of Midian: Ephah and Epher and Hanoch and Abida and
# Eldaah. All these were the sons of Keturah."
m.step("Gen.25.4")
# ‹עֵיפָה … עֵפֶר … חֲנֹךְ … אֲבִידָע … אֶלְדָּעָה … בְּנֵי קְטוּרָה›
# (“Ephah … dust … חנך … Abida … Eldaah … son Keturah”) — fact holds: named-
# only-roster-Midian-line-and-close
m.fact("named_only_roster_midyan_line_and_close")

# -------------------------- Gen.25.5 · THE_HEIR_GIFT_TO_ISAAC --------------
# וַיִּתֵּ֧ן אַבְרָהָ֛ם אֶת־כָּל־אֲשֶׁר־ל֖וֹ לְיִצְחָֽק
# "[EN-AID] And Abraham gave all that he had to Isaac."
m.step("Gen.25.5")
# ‹וַיִּתֵּן אַבְרָהָם אֶת־כָּל־אֲשֶׁר־לוֹ לְיִצְחָק› (“and-set Abraham obj-
# marker all which to-him/its to-Isaac”) — event: give-all — agent Abraham
m.event("give_all", agent="avraham")
# witness-tier presupposed read: four_way_dispute_resolved_by_deferral on
# all_that_he_had — read, not installed
m.witness_read("all_that_he_had", "four_way_dispute_resolved_by_deferral",
                cites=["Bereshit Rabbah 61:6"])
# witness-tier presupposed read: argued_as_property_law_in_a_tribunal on
# gift_plus_severance — read, not installed
m.witness_read("gift_plus_severance", "argued_as_property_law_in_a_tribunal",
                cites=["Bereshit Rabbah 61:7"])

# -------------------------- Gen.25.6 · THE_PILEGESH_GIFTS_AND_SEND_EAST ----
# וְלִבְנֵ֤י הַפִּֽילַגְשִׁים֙ אֲשֶׁ֣ר לְאַבְרָהָ֔ם נָתַ֥ן אַבְרָהָ֖ם
# מַתָּנֹ֑ת וַֽיְשַׁלְּחֵ֞ם מֵעַ֨ל יִצְחָ֤ק בְּנוֹ֙ בְּעוֹדֶ֣נּוּ חַ֔י
# קֵ֖דְמָה אֶל־אֶ֥רֶץ קֶֽדֶם
# "[EN-AID] And to the sons of the concubines that Abraham had, Abraham gave
# gifts; and he sent them away from Isaac his son, while he yet lived,
# eastward, to the land of the East."
m.step("Gen.25.6")
# ‹נָתַן … מַתָּנֹת וַיְשַׁלְּחֵם … קֵדְמָה› (“set … present and-send-
# them/their … front-ward”) — event: gift-and-send-east — agent Abraham;
# theme son-the-concubine
m.event("gift_and_send_east", agent="avraham", themes=["bene_ha_pilagshim"])

# -------------------------- Gen.25.7 · THE_YEARS_OF_ABRAHAM ----------------
# וְאֵ֗לֶּה יְמֵ֛י שְׁנֵֽי־חַיֵּ֥י אַבְרָהָ֖ם אֲשֶׁר־חָ֑י מְאַ֥ת שָׁנָ֛ה
# וְשִׁבְעִ֥ים שָׁנָ֖ה וְחָמֵ֥שׁ שָׁנִֽים
# "[EN-AID] And these are the days of the years of Abraham's life which he
# lived: a hundred years and seventy years and five years."
m.step("Gen.25.7")
# ‹מְאַת שָׁנָה וְשִׁבְעִים שָׁנָה וְחָמֵשׁ שָׁנִים› (“hundred years and-
# seventy years and-five years”) — fact holds: Abraham-lived-175-years
m.fact("avraham_lived_175_years")

# -------------------------- Gen.25.8 · THE_SEVAH_TOVAH_LANDING -------------
# וַיִּגְוַ֨ע וַיָּ֧מָת אַבְרָהָ֛ם בְּשֵׂיבָ֥ה טוֹבָ֖ה זָקֵ֣ן וְשָׂבֵ֑עַ
# וַיֵּאָ֖סֶף אֶל־עַמָּֽיו
# "[EN-AID] And Abraham expired and died in a good old age, old and full,
# and was gathered to his peoples."
m.step("Gen.25.8")
# ‹וַיִּגְוַע וַיָּמָת … וַיֵּאָסֶף אֶל־עַמָּיו› (“and-breathe-out and-die …
# and-gather-for-any-purpose to people-him/its”) — event: expire-die-gather
m.event("expire_die_gather")
# ‹בְּשֵׂיבָה טוֹבָה› (“in-old-age good”) — fact holds: sevah-tovah-promise-
# landing-from-15-15
m.fact("sevah_tovah_promise_landing_from_15_15")

# -------------------------- Gen.25.9 · THE_SONS_BURY_AT_MACHPELAH ----------
# וַיִּקְבְּר֨וּ אֹת֜וֹ יִצְחָ֤ק וְיִשְׁמָעֵאל֙ בָּנָ֔יו אֶל־מְעָרַ֖ת
# הַמַּכְפֵּלָ֑ה אֶל־שְׂדֵ֞ה עֶפְרֹ֤ן בֶּן־צֹ֨חַר֙ הַֽחִתִּ֔י אֲשֶׁ֖ר
# עַל־פְּנֵ֥י מַמְרֵֽא
# "[EN-AID] And Isaac and Ishmael his sons buried him in the cave of
# Machpelah, in the field of Efron son of Zohar the Hittite, which is before
# Mamre."
m.step("Gen.25.9")
# ‹וַיִּקְבְּרוּ אֹתוֹ יִצְחָק וְיִשְׁמָעֵאל … מְעָרַת הַמַּכְפֵּלָה› (“and-
# bury obj-marker-him/its Isaac and-Ishmael … cavern the-Machpelah”) —
# event: bury — theme Abraham
m.event("bury", themes=["avraham"])
# witness-tier presupposed read: order_read_as_repentance_evidence on
# isaac_named_before_ishmael — read, not installed
m.witness_read("isaac_named_before_ishmael", "order_read_as_repentance_evidence",
                cites=["Bereshit Rabbah 62:2"])

# -------------------------- Gen.25.10 · THE_FIELD_PURCHASE_RECAP -----------
# הַשָּׂדֶ֛ה אֲשֶׁר־קָנָ֥ה אַבְרָהָ֖ם מֵאֵ֣ת בְּנֵי־חֵ֑ת שָׁ֛מָּה קֻבַּ֥ר
# אַבְרָהָ֖ם וְשָׂרָ֥ה אִשְׁתּֽוֹ
# "[EN-AID] The field that Abraham bought from the sons of Chet — there
# Abraham was buried, and Sarah his wife."
m.step("Gen.25.10")
# ‹הַשָּׂדֶה אֲשֶׁר־קָנָה אַבְרָהָם מֵאֵת בְּנֵי־חֵת› (“the-field which
# possessor Abraham from-with son Heth”) — fact holds: field-bought-from-
# son-Heth-burial-place
m.fact("field_bought_from_bene_chet_burial_place")
# witness-tier presupposed read: kindness_receipted_after_thirty_eight_years
# on and_sarah_his_wife — read, not installed
m.witness_read("and_sarah_his_wife", "kindness_receipted_after_thirty_eight_years",
                cites=["Bereshit Rabbah 62:2", "Bereshit Rabbah 58:4"])
# witness-tier presupposed read: one_conveyance_counted_across_three_blocks
# on ninth_sons_of_chet_mention — read, not installed
m.witness_read("ninth_sons_of_chet_mention", "one_conveyance_counted_across_three_blocks",
                cites=["Bereshit Rabbah 58:8"])

# -------------------------- Gen.25.11 · THE_BLESSING_AND_BEER_LACHAI_ROI_CLOSE -
# וַיְהִ֗י אַחֲרֵי֙ מ֣וֹת אַבְרָהָ֔ם וַיְבָ֥רֶךְ אֱלֹהִ֖ים אֶת־יִצְחָ֣ק
# בְּנ֑וֹ וַיֵּ֣שֶׁב יִצְחָ֔ק עִם־בְּאֵ֥ר לַחַ֖י רֹאִֽי
# "[EN-AID] And after the death of Abraham, God blessed Isaac his son; and
# Isaac dwelt with Beer-lachai-roi."
m.step("Gen.25.11")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־יִצְחָק בְּנוֹ› (“and-bless God obj-marker Isaac
# son-him/its”) — event: ?
m.event("?")
# ‹בְּאֵר לַחַי רֹאִי› (“Beer-lahai-roi”) — fact holds: Isaac-dwells-beer-
# lachai-Beer-lahai-roi-career-close
m.fact("yitzchaq_dwells_beer_lachai_roi_career_close")
# witness-tier presupposed read: deferred_blessing_discharged_in_this_block
# on God_blessed_isaac — read, not installed
m.witness_read("God_blessed_isaac", "deferred_blessing_discharged_in_this_block",
                cites=["Bereshit Rabbah 61:6"])
# witness-grounded state (its own tier): regression_rule_with_an_ink_guard
# on after_the_death_formula
m.witness_state("after_the_death_formula", "regression_rule_with_an_ink_guard",
                cites=["Bereshit Rabbah 62:3"])

# -------------------------- Gen.25.12 · THE_TOLEDOT_OF_ISHMAEL -------------
# וְאֵ֛לֶּה תֹּלְדֹ֥ת יִשְׁמָעֵ֖אל בֶּן־אַבְרָהָ֑ם אֲשֶׁ֨ר יָלְדָ֜ה הָגָ֧ר
# הַמִּצְרִ֛ית שִׁפְחַ֥ת שָׂרָ֖ה לְאַבְרָהָֽם
# "[EN-AID] And these are the generations of Ishmael, Abraham's son, whom
# Hagar the Egyptian, Sarah's maid, bore to Abraham."
m.step("Gen.25.12")
# ‹תֹּלְדֹת יִשְׁמָעֵאל› (“generations Ishmael”) — fact holds: generations-
# Ishmael-section-header
m.fact("toledot_yishmael_section_header")

# -------------------------- Gen.25.13 · THE_ISHMAEL_NAMES_A ----------------
# וְאֵ֗לֶּה שְׁמוֹת֙ בְּנֵ֣י יִשְׁמָעֵ֔אל בִּשְׁמֹתָ֖ם לְתוֹלְדֹתָ֑ם בְּכֹ֤ר
# יִשְׁמָעֵאל֙ נְבָיֹ֔ת וְקֵדָ֥ר וְאַדְבְּאֵ֖ל וּמִבְשָֽׂם
# "[EN-AID] And these are the names of the sons of Ishmael, by their names,
# according to their generations: the firstborn of Ishmael, Nevayot; and
# Qedar and Adbeel and Mibsam."
m.step("Gen.25.13")
# ‹נְבָיֹת וְקֵדָר וְאַדְבְּאֵל וּמִבְשָׂם› (“Nebaioth and-Kedar and-Adbeel
# and-Mibsam”) — fact holds: named-only-roster-ishmael-sons-a
m.fact("named_only_roster_ishmael_sons_a")

# -------------------------- Gen.25.14 · THE_ISHMAEL_NAMES_B ----------------
# וּמִשְׁמָ֥ע וְדוּמָ֖ה וּמַשָּֽׂא
# "[EN-AID] and Mishma and Duma and Masa."
m.step("Gen.25.14")
# ‹מִשְׁמָע וְדוּמָה וּמַשָּׂא› (“Mishma and-Dumah and-Massa”) — fact holds:
# named-only-roster-ishmael-sons-b
m.fact("named_only_roster_ishmael_sons_b")

# -------------------------- Gen.25.15 · THE_ISHMAEL_NAMES_C ----------------
# חֲדַ֣ד וְתֵימָ֔א יְט֥וּר נָפִ֖ישׁ וָקֵֽדְמָה
# "[EN-AID] Chadad and Tema, Yetur, Nafish, and Qedma."
m.step("Gen.25.15")
# ‹חֲדַד וְתֵימָא יְטוּר נָפִישׁ וָקֵדְמָה› (“Hadad and-Tema Jetur Naphish
# and-Kedemah”) — fact holds: named-only-roster-ishmael-sons-c
m.fact("named_only_roster_ishmael_sons_c")

# -------------------------- Gen.25.16 · THE_TWELVE_PRINCES_PAY -------------
# אֵ֣לֶּה הֵ֞ם בְּנֵ֤י יִשְׁמָעֵאל֙ וְאֵ֣לֶּה שְׁמֹתָ֔ם בְּחַצְרֵיהֶ֖ם
# וּבְטִֽירֹתָ֑ם שְׁנֵים־עָשָׂ֥ר נְשִׂיאִ֖ם לְאֻמֹּתָֽם
# "[EN-AID] These are the sons of Ishmael and these are their names, by
# their villages and by their encampments: twelve princes according to their
# nations."
m.step("Gen.25.16")
# ‹שְׁנֵים־עָשָׂר נְשִׂיאִם› (“two -teen prince”) — fact holds: shneim--
# teen-prince-promise-landing-from-17-20
m.fact("shneim_asar_nesiim_promise_landing_from_17_20")

# -------------------------- Gen.25.17 · THE_ISHMAEL_DEATH_TRIAD ------------
# וְאֵ֗לֶּה שְׁנֵי֙ חַיֵּ֣י יִשְׁמָעֵ֔אל מְאַ֥ת שָׁנָ֛ה וּשְׁלֹשִׁ֥ים
# שָׁנָ֖ה וְשֶׁ֣בַע שָׁנִ֑ים וַיִּגְוַ֣ע וַיָּ֔מָת וַיֵּאָ֖סֶף אֶל־עַמָּֽיו
# "[EN-AID] And these are the years of the life of Ishmael: a hundred years
# and thirty years and seven years; and he expired and died and was gathered
# to his peoples."
m.step("Gen.25.17")
# ‹וַיִּגְוַע וַיָּמָת וַיֵּאָסֶף אֶל־עַמָּיו› (“and-breathe-out and-die
# and-gather-for-any-purpose to people-him/its”) — event: expire-die-gather
m.event("expire_die_gather")
# witness-tier presupposed read: genealogy_number_used_to_date_another_block
# on one_hundred_thirty_seven — read, not installed
m.witness_read("one_hundred_thirty_seven", "genealogy_number_used_to_date_another_block",
                cites=["Bereshit Rabbah 62:4", "Megillah 17a"])

# -------------------------- Gen.25.18 · THE_NAFAL_YISHKON_ECHO_AND_SEAM ----
# וַיִּשְׁכְּנ֨וּ מֵֽחֲוִילָ֜ה עַד־שׁ֗וּר אֲשֶׁר֙ עַל־פְּנֵ֣י מִצְרַ֔יִם
# בֹּאֲכָ֖ה אַשּׁ֑וּרָה עַל־פְּנֵ֥י כָל־אֶחָ֖יו נָפָֽל
# "[EN-AID] And they dwelt from Chavila to Shur, which is before Egypt as
# you go toward Ashur; before all his brothers he fell."
m.step("Gen.25.18")
# ‹וַיִּשְׁכְּנוּ מֵחֲוִילָה עַד־שׁוּר› (“and-reside from-Havilah until
# Shur”) — event: ?
m.event("?")
# ‹עַל־פְּנֵי כָל־אֶחָיו נָפָל› (“over face all brother-him/its fall”) —
# fact holds: fall-before-brothers-echo-fowl-16-12-yishkon
m.fact("nafal_before_brothers_echo_of_16_12_yishkon")
# witness-tier presupposed read: polarity_completed_and_then_flattened on
# he_fell_before_his_brethren — read, not installed
m.witness_read("he_fell_before_his_brethren", "polarity_completed_and_then_flattened",
                cites=["Bereshit Rabbah 45:9", "Onkelos Genesis 25:18"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['report_name_qetura', 'named_only_roster_zimran_yaqshan_medan_midyan_yishbaq_shucha', 'named_only_roster_yaqshan_line', 'named_only_roster_midyan_line_and_close', 'avraham_lived_175_years', 'sevah_tovah_promise_landing_from_15_15', 'field_bought_from_bene_chet_burial_place', 'yitzchaq_dwells_beer_lachai_roi_career_close', 'toledot_yishmael_section_header', 'named_only_roster_ishmael_sons_a', 'named_only_roster_ishmael_sons_b', 'named_only_roster_ishmael_sons_c', 'shneim_asar_nesiim_promise_landing_from_17_20', 'nafal_before_brothers_echo_of_16_12_yishkon'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    assert sorted(m.WORLD["witnessed"]) == ['after_the_death_formula']
    assert m.WORLD["witnessed"]['after_the_death_formula']["cites"] == ['Bereshit Rabbah 62:3']
    assert all('regression_rule_with_an_ink_guard' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('remarriage_in_old_age', 'evening_sowing_of_a_four_way_proverb'), ('ketura_identified_as_hagar', 'ink_leg_recorded_but_not_applied'), ('three_names', 'declared_shelf_splitting_three_ways_by_name'), ('all_that_he_had', 'four_way_dispute_resolved_by_deferral'), ('gift_plus_severance', 'argued_as_property_law_in_a_tribunal'), ('isaac_named_before_ishmael', 'order_read_as_repentance_evidence'), ('and_sarah_his_wife', 'kindness_receipted_after_thirty_eight_years'), ('ninth_sons_of_chet_mention', 'one_conveyance_counted_across_three_blocks'), ('God_blessed_isaac', 'deferred_blessing_discharged_in_this_block'), ('one_hundred_thirty_seven', 'genealogy_number_used_to_date_another_block'), ('he_fell_before_his_brethren', 'polarity_completed_and_then_flattened')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 61:3']
    assert all('evening_sowing_of_a_four_way_proverb' not in f for f in m.WORLD["facts"])
    assert 'remarriage_in_old_age' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 61:4', 'Bereshit Rabbah 47:2']
    assert all('ink_leg_recorded_but_not_applied' not in f for f in m.WORLD["facts"])
    assert 'ketura_identified_as_hagar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 61:5', 'Onkelos Genesis 25:3']
    assert all('declared_shelf_splitting_three_ways_by_name' not in f for f in m.WORLD["facts"])
    assert 'three_names' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 61:6']
    assert all('four_way_dispute_resolved_by_deferral' not in f for f in m.WORLD["facts"])
    assert 'all_that_he_had' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 61:7']
    assert all('argued_as_property_law_in_a_tribunal' not in f for f in m.WORLD["facts"])
    assert 'gift_plus_severance' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 62:2']
    assert all('order_read_as_repentance_evidence' not in f for f in m.WORLD["facts"])
    assert 'isaac_named_before_ishmael' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 62:2', 'Bereshit Rabbah 58:4']
    assert all('kindness_receipted_after_thirty_eight_years' not in f for f in m.WORLD["facts"])
    assert 'and_sarah_his_wife' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 58:8']
    assert all('one_conveyance_counted_across_three_blocks' not in f for f in m.WORLD["facts"])
    assert 'ninth_sons_of_chet_mention' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 61:6']
    assert all('deferred_blessing_discharged_in_this_block' not in f for f in m.WORLD["facts"])
    assert 'God_blessed_isaac' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 62:4', 'Megillah 17a']
    assert all('genealogy_number_used_to_date_another_block' not in f for f in m.WORLD["facts"])
    assert 'one_hundred_thirty_seven' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 45:9', 'Onkelos Genesis 25:18']
    assert all('polarity_completed_and_then_flattened' not in f for f in m.WORLD["facts"])
    assert 'he_fell_before_his_brethren' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
