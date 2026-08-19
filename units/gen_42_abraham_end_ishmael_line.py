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

# -------------------------- Gen.25.4 · THE_MIDIAN_LINE_AND_CLOSE -----------
# וּבְנֵ֣י מִדְיָ֗ן עֵיפָ֤ה וָעֵ֨פֶר֙ וַחֲנֹ֔ךְ וַאֲבִידָ֖ע וְאֶלְדָּעָ֑ה
# כָּל־אֵ֖לֶּה בְּנֵ֥י קְטוּרָֽה
# "[EN-AID] And the sons of Midian: Ephah and Epher and Hanoch and Abida and
# Eldaah. All these were the sons of Keturah."
m.step("Gen.25.4")
# ‹עֵיפָה … עֵפֶר … חֲנוֹךְ … אֲבִידָע … אֶלְדָּעָה … בְּנֵי קְטוּרָה›
# (“Ephah … dust … Enoch … Abida … Eldaah … son Keturah”) — fact holds:
# named-only-roster-Midian-line-and-close
m.fact("named_only_roster_midyan_line_and_close")

# -------------------------- Gen.25.5 · THE_HEIR_GIFT_TO_ISAAC --------------
# וַיִּתֵּ֧ן אַבְרָהָ֛ם אֶת־כָּל־אֲשֶׁר־ל֖וֹ לְיִצְחָֽק
# "[EN-AID] And Abraham gave all that he had to Isaac."
m.step("Gen.25.5")
# ‹וַיִּתֵּן אַבְרָהָם אֶת־כָּל־אֲשֶׁר־לוֹ לְיִצְחָק› (“and-set Abraham obj-
# marker all which to-him/its to-Isaac”) — event: give-all — agent Abraham
m.event("give_all", agent="avraham")

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
# ‹נְבָיוֹת וְקֵדָר וְאַדְבְּאֵל וּמִבְשָׂם› (“Nebaioth and-Kedar and-Adbeel
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
# ‹שְׁנֵים־עָשָׂר נְשִׂיאִים› (“two -teen chieftains”) — fact holds: shneim
# --teen-prince-promise-landing-from-17-20
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
