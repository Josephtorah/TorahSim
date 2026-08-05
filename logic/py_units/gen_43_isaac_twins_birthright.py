#!/usr/bin/env python3
# =============================================================================
# gen_43_isaac_twins_birthright — 25:19-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_43_isaac_twins_birthright.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Isaac's toledot: twins and the birthright (25:19-34)"""
from machine import Machine

m = Machine("gen_43_isaac_twins_birthright")

# -------------------------- Gen.25.19 · V_25_19 ----------------------------
# וְ/אֵ֛לֶּה תּוֹלְדֹ֥ת יִצְחָ֖ק בֶּן אַבְרָהָ֑ם אַבְרָהָ֖ם הוֹלִ֥יד אֶת
# יִצְחָֽק
# "[EN-AID] And these are the generations of Isaac, Abraham's son: Abraham
# begot Isaac."
m.step("Gen.25.19")
# ‹וְאֵלֶּה תּוֹלְדֹת יִצְחָק› section toldot-yitzchaq: yitzchaq
m.section("toldot_yitzchaq", "yitzchaq")
# ‹אַבְרָהָם› reads without prior install (flag, not fix): avraham, yitzchaq
m.presupposed("avraham", "yitzchaq")

# -------------------------- Gen.25.20 · V_25_20 ----------------------------
# וַ/יְהִ֤י יִצְחָק֙ בֶּן אַרְבָּעִ֣ים שָׁנָ֔ה בְּ/קַחְתּ֣/וֹ אֶת רִבְקָ֗ה
# בַּת בְּתוּאֵל֙ הָֽ/אֲרַמִּ֔י מִ/פַּדַּ֖ן אֲרָ֑ם אֲח֛וֹת לָבָ֥ן
# הָ/אֲרַמִּ֖י ל֥/וֹ לְ/אִשָּֽׁה
# "[EN-AID] And Isaac was forty years old when he took Rivqah, daughter of
# Betuel the Aramean of Paddan-aram, sister of Laban the Aramean, as wife."
m.step("Gen.25.20")
# ‹בְּקַחְתּוֹ אֶת־רִבְקָה› event: take-wife — agent yitzchaq; theme rivqah
m.event("take_wife", agent="yitzchaq", themes=["rivqah"])
# ‹רִבְקָה› reads without prior install (flag, not fix): rivqah, lavan,
# betuel, padan-aram
m.presupposed("rivqah", "lavan", "betuel", "padan_aram")

# -------------------------- Gen.25.21 · V_25_21 ----------------------------
# וַ/יֶּעְתַּ֨ר יִצְחָ֤ק לַֽ/יהוָה֙ לְ/נֹ֣כַח אִשְׁתּ֔/וֹ כִּ֥י עֲקָרָ֖ה
# הִ֑וא וַ/יֵּעָ֤תֶר ל/וֹ֙ יְהוָ֔ה וַ/תַּ֖הַר רִבְקָ֥ה אִשְׁתּֽ/וֹ
# "[EN-AID] And Isaac prayed to YHWH facing his wife, for she was barren;
# and YHWH was entreated of him, and Rivqah his wife conceived."
m.step("Gen.25.21")
# ‹וַיֶּעְתַּר … וַתַּהַר› event: pray-conceive — agent yitzchaq
m.event("pray_conceive", agent="yitzchaq")

# -------------------------- Gen.25.22 · V_25_22 ----------------------------
# וַ/יִּתְרֹֽצֲצ֤וּ הַ/בָּנִים֙ בְּ/קִרְבָּ֔/הּ וַ/תֹּ֣אמֶר אִם כֵּ֔ן
# לָ֥/מָּה זֶּ֖ה אָנֹ֑כִי וַ/תֵּ֖לֶךְ לִ/דְרֹ֥שׁ אֶת יְהוָֽה
# "[EN-AID] And the children struggled together within her; and she said: If
# so, why am I thus? And she went to inquire of YHWH."
m.step("Gen.25.22")
# ‹וַיִּתְרֹצְצוּ … וַתֵּלֶךְ לִדְרֹשׁ› event: struggle-inquire — agent
# rivqah
m.event("struggle_inquire", agent="rivqah")

# -------------------------- Gen.25.23 · V_25_23 ----------------------------
# וַ/יֹּ֨אמֶר יְהוָ֜ה לָ֗/הּ שְׁנֵ֤י גיים גוֹיִם֙ בְּ/בִטְנֵ֔/ךְ וּ/שְׁנֵ֣י
# לְאֻמִּ֔ים מִ/מֵּעַ֖יִ/ךְ יִפָּרֵ֑דוּ וּ/לְאֹם֙ מִ/לְאֹ֣ם יֶֽאֱמָ֔ץ
# וְ/רַ֖ב יַעֲבֹ֥ד צָעִֽיר
# "[EN-AID] And YHWH said to her: Two nations are in your womb, and two
# peoples shall be separated from your belly; and people shall be stronger
# than people, and the elder shall serve the younger."
m.step("Gen.25.23")
# ‹וַיֹּאמֶר יְהוָה› event: say-oracle — agent the-LORD
m.event("say_oracle", agent="YHWH")
# ‹שְׁנֵי גוֹיִם› fact holds: two-nations-oracle
m.fact("two_nations_oracle")

# -------------------------- Gen.25.24 · V_25_24 ----------------------------
# וַ/יִּמְלְא֥וּ יָמֶ֖י/הָ לָ/לֶ֑דֶת וְ/הִנֵּ֥ה תוֹמִ֖ם בְּ/בִטְנָֽ/הּ
# "[EN-AID] And when her days to bear were fulfilled, behold twins were in
# her womb."
m.step("Gen.25.24")
# ‹וַ/יִּמְלְא֥וּ› event: ?
m.event("?")

# -------------------------- Gen.25.25 · V_25_25 ----------------------------
# וַ/יֵּצֵ֤א הָ/רִאשׁוֹן֙ אַדְמוֹנִ֔י כֻּלּ֖/וֹ כְּ/אַדֶּ֣רֶת שֵׂעָ֑ר
# וַ/יִּקְרְא֥וּ שְׁמ֖/וֹ עֵשָֽׂו
# "[EN-AID] And the first came out red, all of him like a hairy mantle; and
# they called his name Esau."
m.step("Gen.25.25")
# ‹וַיֵּצֵא הָרִאשׁוֹן› event: birth-first
m.event("birth_first")
# ‹עֵשָׂו› the world gains: esav
m.install("esav")

# -------------------------- Gen.25.26 · V_25_26 ----------------------------
# וְ/אַֽחֲרֵי כֵ֞ן יָצָ֣א אָחִ֗י/ו וְ/יָד֤/וֹ אֹחֶ֨זֶת֙ בַּ/עֲקֵ֣ב עֵשָׂ֔ו
# וַ/יִּקְרָ֥א שְׁמ֖/וֹ יַעֲקֹ֑ב וְ/יִצְחָ֛ק בֶּן שִׁשִּׁ֥ים שָׁנָ֖ה
# בְּ/לֶ֥דֶת אֹתָֽ/ם
# "[EN-AID] And afterward his brother came out, and his hand holding Esau's
# heel; and his name was called Jacob. And Isaac was sixty years old when
# she bore them."
m.step("Gen.25.26")
# ‹וְאַחֲרֵי־כֵן יָצָא אָחִיו› event: birth-second
m.event("birth_second")
# ‹יַעֲקֹב› the world gains: yaaqov
m.install("yaaqov")

# -------------------------- Gen.25.27 · V_25_27 ----------------------------
# וַֽ/יִּגְדְּלוּ֙ הַ/נְּעָרִ֔ים וַ/יְהִ֣י עֵשָׂ֗ו אִ֛ישׁ יֹדֵ֥עַ צַ֖יִד
# אִ֣ישׁ שָׂדֶ֑ה וְ/יַעֲקֹב֙ אִ֣ישׁ תָּ֔ם יֹשֵׁ֖ב אֹהָלִֽים
# "[EN-AID] And the boys grew; and Esau was a man knowing hunting, a man of
# the field, and Jacob was a quiet man, dwelling in tents."
m.step("Gen.25.27")
# ‹וַֽ/יִּגְדְּלוּ֙› event: ?
m.event("?")

# -------------------------- Gen.25.28 · V_25_28 ----------------------------
# וַ/יֶּאֱהַ֥ב יִצְחָ֛ק אֶת עֵשָׂ֖ו כִּי צַ֣יִד בְּ/פִ֑י/ו וְ/רִבְקָ֖ה
# אֹהֶ֥בֶת אֶֽת יַעֲקֹֽב
# "[EN-AID] And Isaac loved Esau because game was in his mouth, and Rivqah
# loved Jacob."
m.step("Gen.25.28")
# ‹וַ/יֶּאֱהַ֥ב› event: ?
m.event("?")

# -------------------------- Gen.25.29 · V_25_29 ----------------------------
# וַ/יָּ֥זֶד יַעֲקֹ֖ב נָזִ֑יד וַ/יָּבֹ֥א עֵשָׂ֛ו מִן הַ/שָּׂדֶ֖ה וְ/ה֥וּא
# עָיֵֽף
# "[EN-AID] And Jacob boiled stew; and Esau came in from the field, and he
# was faint."
m.step("Gen.25.29")
# ‹וַ/יָּ֥זֶד› event: ?
m.event("?")

# -------------------------- Gen.25.30 · V_25_30 ----------------------------
# וַ/יֹּ֨אמֶר עֵשָׂ֜ו אֶֽל יַעֲקֹ֗ב הַלְעִיטֵ֤/נִי נָא֙ מִן הָ/אָדֹ֤ם
# הָ/אָדֹם֙ הַ/זֶּ֔ה כִּ֥י עָיֵ֖ף אָנֹ֑כִי עַל כֵּ֥ן קָרָֽא שְׁמ֖/וֹ אֱדֽוֹם
# "[EN-AID] And Esau said to Jacob: Let me gulp, please, from this red red,
# for I am faint. Therefore his name was called Edom."
m.step("Gen.25.30")
# ‹וַיֹּאמֶר עֵשָׂו› event: say — agent esav
m.event("say", agent="esav")
# ‹הַלְעִיטֵנִי נָא› esav speaks a demand — LET: halite-ni(yaaqov, from-the-
# adom)
m.declare("esav", "LET",
          "halite_ni(yaaqov, min_ha_adom)")
# ‹עַל־כֵּן קָרָא־שְׁמוֹ אֱדוֹם› fact holds: name-edom-etiology
m.fact("name_edom_etiology")

# -------------------------- Gen.25.31 · V_25_31 ----------------------------
# וַ/יֹּ֖אמֶר יַעֲקֹ֑ב מִכְרָ֥/ה כַ/יּ֛וֹם אֶת בְּכֹֽרָתְ/ךָ֖ לִֽ/י
# "[EN-AID] And Jacob said: Sell me as of today your birthright."
m.step("Gen.25.31")
# ‹מִכְרָה כַיּוֹם אֶת־בְּכֹרָתְךָ› yaaqov speaks a demand — LET:
# mikhra(esav, bekhorat-kha)
m.declare("yaaqov", "LET",
          "mikhra(esav, bekhorat_kha)")

# -------------------------- Gen.25.32 · V_25_32 ----------------------------
# וַ/יֹּ֣אמֶר עֵשָׂ֔ו הִנֵּ֛ה אָנֹכִ֥י הוֹלֵ֖ךְ לָ/מ֑וּת וְ/לָ/מָּה זֶּ֥ה
# לִ֖/י בְּכֹרָֽה
# "[EN-AID] And Esau said: Behold I am going to die; and what is this
# birthright to me?"
m.step("Gen.25.32")
# ‹הִנֵּה אָנֹכִי הוֹלֵךְ לָמוּת› fact holds: esav-die-speech-fact
m.fact("esav_die_speech_fact")

# -------------------------- Gen.25.33 · V_25_33 ----------------------------
# וַ/יֹּ֣אמֶר יַעֲקֹ֗ב הִשָּׁ֤בְעָ/ה לִּ/י֙ כַּ/יּ֔וֹם וַ/יִּשָּׁבַ֖ע ל֑/וֹ
# וַ/יִּמְכֹּ֥ר אֶת בְּכֹרָת֖/וֹ לְ/יַעֲקֹֽב
# "[EN-AID] And Jacob said: Swear to me as of today. And he swore to him,
# and he sold his birthright to Jacob."
m.step("Gen.25.33")
# ‹הִשָּׁבְעָה לִּי› yaaqov speaks a demand — LET: hishava(esav)
m.declare("yaaqov", "LET",
          "hishava(esav)")
# ‹וַיִּשָּׁבַע לוֹ› demand settled (popped from the queue): hishava(esav)
m.result("hishava(esav)", tmark="t1")
# ‹וַיִּמְכֹּר אֶת־בְּכֹרָתוֹ› demand settled (popped from the queue):
# mikhra(esav, bekhorat-kha)
m.result("mikhra(esav, bekhorat_kha)", tmark="t2")

# -------------------------- Gen.25.34 · V_25_34 ----------------------------
# וְ/יַעֲקֹ֞ב נָתַ֣ן לְ/עֵשָׂ֗ו לֶ֚חֶם וּ/נְזִ֣יד עֲדָשִׁ֔ים וַ/יֹּ֣אכַל
# וַ/יֵּ֔שְׁתְּ וַ/יָּ֖קָם וַ/יֵּלַ֑ךְ וַ/יִּ֥בֶז עֵשָׂ֖ו אֶת הַ/בְּכֹרָֽה
# "[EN-AID] And Jacob gave Esau bread and lentil stew, and he ate and drank
# and rose and went; and Esau despised the birthright."
m.step("Gen.25.34")
# ‹נָתַן … וַיֹּאכַל וַיֵּשְׁתְּ› event: feed-eat-drink-go — agent yaaqov-
# esav
m.event("feed_eat_drink_go", agent="yaaqov_esav")
# ‹וַיִּבֶז עֵשָׂו אֶת־הַבְּכֹרָה› fact holds: esav-despised-birthright
m.fact("esav_despised_birthright")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'yaaqov', 'esav'}
    assert m.presupposed_set() == {'rivqah', 'yitzchaq', 'avraham', 'padan_aram', 'lavan', 'betuel'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['halite_ni(yaaqov, min_ha_adom)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6}
    assert sorted(m.WORLD["facts"]) == sorted(['two_nations_oracle', 'name_edom_etiology', 'esav_die_speech_fact', 'esav_despised_birthright'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 18
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
