#!/usr/bin/env python3
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

# -------------------------- Gen.25.1 · V_25_1 ------------------------------
# וַ/יֹּ֧סֶף אַבְרָהָ֛ם וַ/יִּקַּ֥ח אִשָּׁ֖ה וּ/שְׁמָ֥/הּ קְטוּרָֽה
# "[EN-AID] And Abraham took another wife, and her name was Keturah."
m.step("Gen.25.1")
# ‹וַיִּקַּח› event: take-wife — agent avraham; theme qetura
m.event("take_wife", agent="avraham", themes=["qetura"])
# ‹קְטוּרָה› the world gains: qetura
m.install("qetura")
# ‹אַבְרָהָם› reads without prior install (flag, not fix): avraham
m.presupposed("avraham")

# -------------------------- Gen.25.2 · V_25_2 ------------------------------
# וַ/תֵּ֣לֶד ל֗/וֹ אֶת זִמְרָן֙ וְ/אֶת יָקְשָׁ֔ן וְ/אֶת מְדָ֖ן וְ/אֶת
# מִדְיָ֑ן וְ/אֶת יִשְׁבָּ֖ק וְ/אֶת שֽׁוּחַ
# "[EN-AID] And she bore him Zimran and Jokshan and Medan and Midian and
# Ishbak and Shuah."
m.step("Gen.25.2")
# ‹וַ/תֵּ֣לֶד ל֗/וֹ אֶת זִמְרָן֙ וְ/אֶת יָק› fact holds: name-list-25-2
m.fact("name_list_25_2")

# -------------------------- Gen.25.3 · V_25_3 ------------------------------
# וְ/יָקְשָׁ֣ן יָלַ֔ד אֶת שְׁבָ֖א וְ/אֶת דְּדָ֑ן וּ/בְנֵ֣י דְדָ֔ן הָי֛וּ
# אַשּׁוּרִ֥ם וּ/לְטוּשִׁ֖ים וּ/לְאֻמִּֽים
# "[EN-AID] And Jokshan begot Sheba and Dedan. And the sons of Dedan were
# Asshurim and Letushim and Leummim."
m.step("Gen.25.3")
# ‹וְ/יָקְשָׁ֣ן יָלַ֔ד אֶת שְׁבָ֖א וְ/אֶת ד› fact holds: name-list-25-3
m.fact("name_list_25_3")

# -------------------------- Gen.25.4 · V_25_4 ------------------------------
# וּ/בְנֵ֣י מִדְיָ֗ן עֵיפָ֤ה וָ/עֵ֨פֶר֙ וַ/חֲנֹ֔ךְ וַ/אֲבִידָ֖ע
# וְ/אֶלְדָּעָ֑ה כָּל אֵ֖לֶּה בְּנֵ֥י קְטוּרָֽה
# "[EN-AID] And the sons of Midian: Ephah and Epher and Hanoch and Abida and
# Eldaah. All these were the sons of Keturah."
m.step("Gen.25.4")
# ‹וּ/בְנֵ֣י מִדְיָ֗ן עֵיפָ֤ה וָ/עֵ֨פֶר֙ וַ› fact holds: name-list-25-4
m.fact("name_list_25_4")

# -------------------------- Gen.25.5 · V_25_5 ------------------------------
# וַ/יִּתֵּ֧ן אַבְרָהָ֛ם אֶת כָּל אֲשֶׁר ל֖/וֹ לְ/יִצְחָֽק
# "[EN-AID] And Abraham gave all that he had to Isaac."
m.step("Gen.25.5")
# ‹וַיִּתֵּן› event: give-all — agent avraham
m.event("give_all", agent="avraham")
# ‹יִצְחָק› reads without prior install (flag, not fix): yitzchaq
m.presupposed("yitzchaq")

# -------------------------- Gen.25.6 · V_25_6 ------------------------------
# וְ/לִ/בְנֵ֤י הַ/פִּֽילַגְשִׁים֙ אֲשֶׁ֣ר לְ/אַבְרָהָ֔ם נָתַ֥ן אַבְרָהָ֖ם
# מַתָּנֹ֑ת וַֽ/יְשַׁלְּחֵ֞/ם מֵ/עַ֨ל יִצְחָ֤ק בְּנ/וֹ֙ בְּ/עוֹדֶ֣/נּוּ חַ֔י
# קֵ֖דְמָ/ה אֶל אֶ֥רֶץ קֶֽדֶם
# "[EN-AID] And to the sons of the concubines that Abraham had, Abraham gave
# gifts, and he sent them away from Isaac his son, while he was still
# living, eastward to the land of the east."
m.step("Gen.25.6")
# ‹נָתַן … וַיְשַׁלְּחֵם› event: gifts-send-east — agent avraham
m.event("gifts_send_east", agent="avraham")

# -------------------------- Gen.25.7 · V_25_7 ------------------------------
# וְ/אֵ֗לֶּה יְמֵ֛י שְׁנֵֽי חַיֵּ֥י אַבְרָהָ֖ם אֲשֶׁר חָ֑י מְאַ֥ת שָׁנָ֛ה
# וְ/שִׁבְעִ֥ים שָׁנָ֖ה וְ/חָמֵ֥שׁ שָׁנִֽים
# "[EN-AID] And these are the days of the years of Abraham's life that he
# lived: a hundred seventy-five years."
m.step("Gen.25.7")
# ‹מְאַת שָׁנָה וְשִׁבְעִים שָׁנָה וְחָמֵשׁ שָׁנִים› fact holds: avraham-
# age-175
m.fact("avraham_age_175")

# -------------------------- Gen.25.8 · V_25_8 ------------------------------
# וַ/יִּגְוַ֨ע וַ/יָּ֧מָת אַבְרָהָ֛ם בְּ/שֵׂיבָ֥ה טוֹבָ֖ה זָקֵ֣ן וְ/שָׂבֵ֑עַ
# וַ/יֵּאָ֖סֶף אֶל עַמָּֽי/ו
# "[EN-AID] And Abraham expired and died in a good old age, old and full,
# and he was gathered to his people."
m.step("Gen.25.8")
# ‹וַיִּגְוַע וַיָּמָת … וַיֵּאָסֶף› event: expire-die-gather — theme
# avraham
m.event("expire_die_gather", themes=["avraham"])
# ‹בְּשֵׂיבָה טוֹבָה› fact holds: seva-tova-no-test
m.fact("seva_tova_no_test")

# -------------------------- Gen.25.9 · V_25_9 ------------------------------
# וַ/יִּקְבְּר֨וּ אֹת֜/וֹ יִצְחָ֤ק וְ/יִשְׁמָעֵאל֙ בָּנָ֔י/ו אֶל מְעָרַ֖ת
# הַ/מַּכְפֵּלָ֑ה אֶל שְׂדֵ֞ה עֶפְרֹ֤ן בֶּן צֹ֨חַר֙ הַֽ/חִתִּ֔י אֲשֶׁ֖ר עַל
# פְּנֵ֥י מַמְרֵֽא
# "[EN-AID] And Isaac and Ishmael his sons buried him in the cave of
# Machpelah, in the field of Ephron son of Zohar the Hittite, which is
# before Mamre,"
m.step("Gen.25.9")
# ‹וַיִּקְבְּרוּ› event: bury — agent yitzchaq-yishmael; theme avraham
m.event("bury", agent="yitzchaq_yishmael", themes=["avraham"])
# ‹הַמַּכְפֵּלָה› reads without prior install (flag, not fix): makhpela,
# mamre, yishmael
m.presupposed("makhpela", "mamre", "yishmael")

# -------------------------- Gen.25.10 · V_25_10 ----------------------------
# הַ/שָּׂדֶ֛ה אֲשֶׁר קָנָ֥ה אַבְרָהָ֖ם מֵ/אֵ֣ת בְּנֵי חֵ֑ת שָׁ֛מָּ/ה קֻבַּ֥ר
# אַבְרָהָ֖ם וְ/שָׂרָ֥ה אִשְׁתּֽ/וֹ
# "[EN-AID] the field that Abraham bought from the sons of Heth; there
# Abraham was buried, and Sarah his wife."
m.step("Gen.25.10")
# ‹הַשָּׂדֶה … שָׁמָּה קֻבַּר› fact holds: field-bought-burial-there
m.fact("field_bought_burial_there")

# -------------------------- Gen.25.11 · V_25_11 ----------------------------
# וַ/יְהִ֗י אַחֲרֵי֙ מ֣וֹת אַבְרָהָ֔ם וַ/יְבָ֥רֶךְ אֱלֹהִ֖ים אֶת יִצְחָ֣ק
# בְּנ֑/וֹ וַ/יֵּ֣שֶׁב יִצְחָ֔ק עִם בְּאֵ֥ר לַחַ֖י רֹאִֽי
# "[EN-AID] And it was after Abraham's death that God blessed Isaac his son;
# and Isaac dwelt by Beer-lahai-roi."
m.step("Gen.25.11")
# ‹וַיְבָרֶךְ אֱלֹהִים› event: bless — agent God
m.event("bless", agent="Elohim")
# ‹בְּאֵר לַחַי רֹאִי› reads without prior install (flag, not fix): beer-
# lachai-roi
m.presupposed("beer_lachai_roi")

# -------------------------- Gen.25.12 · V_25_12 ----------------------------
# וְ/אֵ֛לֶּה תֹּלְדֹ֥ת יִשְׁמָעֵ֖אל בֶּן אַבְרָהָ֑ם אֲשֶׁ֨ר יָלְדָ֜ה הָגָ֧ר
# הַ/מִּצְרִ֛ית שִׁפְחַ֥ת שָׂרָ֖ה לְ/אַבְרָהָֽם
# "[EN-AID] And these are the generations of Ishmael, Abraham's son, whom
# Hagar the Egyptian, Sarah's maidservant, bore to Abraham."
m.step("Gen.25.12")
# ‹וְאֵלֶּה תֹּלְדֹת יִשְׁמָעֵאל› section toldot-yishmael: yishmael
m.section("toldot_yishmael", "yishmael")
# ‹הָגָר› reads without prior install (flag, not fix): hagar
m.presupposed("hagar")

# -------------------------- Gen.25.13 · V_25_13 ----------------------------
# וְ/אֵ֗לֶּה שְׁמוֹת֙ בְּנֵ֣י יִשְׁמָעֵ֔אל בִּ/שְׁמֹתָ֖/ם לְ/תוֹלְדֹתָ֑/ם
# בְּכֹ֤ר יִשְׁמָעֵאל֙ נְבָיֹ֔ת וְ/קֵדָ֥ר וְ/אַדְבְּאֵ֖ל וּ/מִבְשָֽׂם
# "[EN-AID] And these are the names of the sons of Ishmael, by their names,
# according to their generations: Nebaioth firstborn of Ishmael, and Kedar
# and Adbeel and Mibsam,"
m.step("Gen.25.13")
# ‹וְ/אֵ֗לֶּה שְׁמוֹת֙ בְּנֵ֣י יִשְׁמָעֵ֔אל› fact holds: name-list-25-13
m.fact("name_list_25_13")

# -------------------------- Gen.25.14 · V_25_14 ----------------------------
# וּ/מִשְׁמָ֥ע וְ/דוּמָ֖ה וּ/מַשָּֽׂא
# "[EN-AID] and Mishma and Dumah and Massa,"
m.step("Gen.25.14")
# ‹וּ/מִשְׁמָ֥ע וְ/דוּמָ֖ה וּ/מַשָּֽׂא› fact holds: name-list-25-14
m.fact("name_list_25_14")

# -------------------------- Gen.25.15 · V_25_15 ----------------------------
# חֲדַ֣ד וְ/תֵימָ֔א יְט֥וּר נָפִ֖ישׁ וָ/קֵֽדְמָה
# "[EN-AID] Hadad and Tema, Jetur, Naphish, and Kedemah."
m.step("Gen.25.15")
# ‹חֲדַ֣ד וְ/תֵימָ֔א יְט֥וּר נָפִ֖ישׁ וָ/קֵ› fact holds: name-list-25-15
m.fact("name_list_25_15")

# -------------------------- Gen.25.16 · V_25_16 ----------------------------
# אֵ֣לֶּה הֵ֞ם בְּנֵ֤י יִשְׁמָעֵאל֙ וְ/אֵ֣לֶּה שְׁמֹתָ֔/ם בְּ/חַצְרֵי/הֶ֖ם
# וּ/בְ/טִֽירֹתָ֑/ם שְׁנֵים עָשָׂ֥ר נְשִׂיאִ֖ם לְ/אֻמֹּתָֽ/ם
# "[EN-AID] These are the sons of Ishmael and these are their names, by
# their villages and by their encampments, twelve princes according to their
# tribes."
m.step("Gen.25.16")
# ‹אֵ֣לֶּה הֵ֞ם בְּנֵ֤י יִשְׁמָעֵאל֙ וְ/אֵ֣› fact holds: name-list-25-16
m.fact("name_list_25_16")

# -------------------------- Gen.25.17 · V_25_17 ----------------------------
# וְ/אֵ֗לֶּה שְׁנֵי֙ חַיֵּ֣י יִשְׁמָעֵ֔אל מְאַ֥ת שָׁנָ֛ה וּ/שְׁלֹשִׁ֥ים
# שָׁנָ֖ה וְ/שֶׁ֣בַע שָׁנִ֑ים וַ/יִּגְוַ֣ע וַ/יָּ֔מָת וַ/יֵּאָ֖סֶף אֶל
# עַמָּֽי/ו
# "[EN-AID] And these are the years of the life of Ishmael: a hundred
# thirty-seven years; and he expired and died, and was gathered to his
# people."
m.step("Gen.25.17")
# ‹וַיִּגְוַע וַיָּמָת› event: expire-die-gather — theme yishmael
m.event("expire_die_gather", themes=["yishmael"])

# -------------------------- Gen.25.18 · V_25_18 ----------------------------
# וַ/יִּשְׁכְּנ֨וּ מֵֽ/חֲוִילָ֜ה עַד שׁ֗וּר אֲשֶׁר֙ עַל פְּנֵ֣י מִצְרַ֔יִם
# בֹּאֲ/כָ֖ה אַשּׁ֑וּרָ/ה עַל פְּנֵ֥י כָל אֶחָ֖י/ו נָפָֽל
# "[EN-AID] And they dwelt from Havilah to Shur, which is before Egypt as
# you go toward Assyria; he settled facing all his brothers."
m.step("Gen.25.18")
# ‹וַיִּשְׁכְּנוּ› event: dwell — theme yishmael-line
m.event("dwell", themes=["yishmael_line"])
# ‹מֵחֲוִילָה עַד־שׁוּר› reads without prior install (flag, not fix):
# havila, shur, mitzrayim
m.presupposed("havila", "shur", "mitzrayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'qetura'}
    assert m.presupposed_set() == {'shur', 'makhpela', 'beer_lachai_roi', 'mitzrayim', 'yitzchaq', 'havila', 'avraham', 'mamre', 'hagar', 'yishmael'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 10}
    assert sorted(m.WORLD["facts"]) == sorted(['name_list_25_2', 'name_list_25_3', 'name_list_25_4', 'avraham_age_175', 'seva_tova_no_test', 'field_bought_burial_there', 'name_list_25_13', 'name_list_25_14', 'name_list_25_15', 'name_list_25_16'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
