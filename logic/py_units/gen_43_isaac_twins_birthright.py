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

# -------------------------- Gen.25.19 · THE_TOLEDOT_OF_ISAAC ---------------
# ‹וְאֵ֛לֶּה תּוֹלְדֹ֥ת יִצְחָ֖ק› (“and-these generations Isaac”)
# ‹בֶּן־אַבְרָהָ֑ם אַבְרָהָ֖ם הוֹלִ֥יד› (“son Abraham Abraham bear-young”)
# ‹אֶת־יִצְחָֽק› (“obj-marker Isaac”)
# "[EN-AID] And these are the generations of Isaac, Abraham's son: Abraham
# begot Isaac."
m.step("Gen.25.19")
# ‹תּוֹלְדֹת יִצְחָק› (“generations Isaac”)
# — fact holds: generations-Isaac-section-header
m.fact("toledot_yitzchaq_section_header")

# -------------------------- Gen.25.20 · THE_MARRIAGE_AGE_AND_ORIGIN --------
# ‹וַיְהִ֤י יִצְחָק֙ בֶּן־אַרְבָּעִ֣ים› (“and-be Isaac son forty”)
# ‹שָׁנָ֔ה בְּקַחְתּ֣וֹ אֶת־רִבְקָ֗ה› (“years in-take-him/its obj-marker
# Rebekah”)
# ‹בַּת־בְּתוּאֵל֙ הָֽאֲרַמִּ֔י מִפַּדַּ֖ן› (“daughter Bethuel the-Aramite
# from”)
# ‹אֲרָ֑ם אֲח֛וֹת לָבָ֥ן› (“Padan sister Laban”)
# ‹הָאֲרַמִּ֖י ל֥וֹ לְאִשָּֽׁה› (“the-Aramite to-him/its to-woman”)
# "[EN-AID] And Isaac was forty years old when he took Rivqah, daughter of
# Betuel the Aramean of Padan-aram, sister of Laban the Aramean, as wife for
# himself."
m.step("Gen.25.20")
# ‹בֶּן־אַרְבָּעִים שָׁנָה … רִבְקָה› (“son forty years … Rebekah”)
# ‹… מִפַּדַּן אֲרָם› (“from Padan”)
# — fact holds: Isaac-forty-takes-Rebekah-from-from-Padan
m.fact("yitzchaq_forty_takes_rivqa_from_padan_aram")

# -------------------------- Gen.25.21 · THE_ENTREAT_PAIR -------------------
# ‹וַיֶּעְתַּ֨ר יִצְחָ֤ק לַֽיהוָה֙› (“and-burn-incense-in-worship Isaac to-
# YHWH”)
# ‹לְנֹ֣כַח אִשְׁתּ֔וֹ כִּ֥י› (“to-front-part woman-him/its that”)
# ‹עֲקָרָ֖ה הִ֑וא וַיֵּעָ֤תֶר› (“sterile he/it and-burn-incense-in-worship”)
# ‹לוֹ֙ יְהוָ֔ה וַתַּ֖הַר› (“to-him/its YHWH and-be-pregnant”)
# ‹רִבְקָ֥ה אִשְׁתּֽוֹ› (“Rebekah woman-him/its”)
# "[EN-AID] And Isaac entreated YHWH opposite his wife, for she was barren;
# and YHWH was entreated of him, and Rivqah his wife conceived."
m.step("Gen.25.21")
# ‹וַיֶּעְתַּר … וַיֵּעָתֶר … וַתַּהַר› (“and-burn-incense-in-worship … and-
# burn-incense-in-worship … and-be-pregnant”)
# — event: entreat-and-in-entreated — theme woman-him/its
m.event("entreat_and_be_entreated", themes=["isht-o"])
# witness-tier presupposed read: poured_out_or_decree_overturned on
# entreaty_verb — read, not installed
m.witness_read("entreaty_verb", "poured_out_or_decree_overturned",
                cites=["Bereshit Rabbah 63:5", "Onkelos Genesis 25:21"])
# witness-tier presupposed read: wire_closed_from_gen_41 on
# conception_held_for_this_prayer — read, not installed
m.witness_read("conception_held_for_this_prayer", "wire_closed_from_gen_41",
                cites=["Bereshit Rabbah 60:13"])

# -------------------------- Gen.25.22 · THE_STRUGGLE_AND_INQUIRE -----------
# ‹וַיִּתְרֹֽצֲצ֤וּ הַבָּנִים֙ בְּקִרְבָּ֔הּ› (“and-crack-in-pieces the-son
# in-nearest-part-her/its”)
# ‹וַתֹּ֣אמֶר אִם־כֵּ֔ן לָ֥מָּה› (“and-say if so to-what”)
# ‹זֶּ֖ה אָנֹ֑כִי וַתֵּ֖לֶךְ› (“this and-go”)
# ‹לִדְרֹ֥שׁ אֶת־יְהוָֽה› (“to-tread obj-marker YHWH”)
# "[EN-AID] And the children struggled together within her; and she said: If
# it be so, why am I thus? And she went to inquire of YHWH."
m.step("Gen.25.22")
# ‹וַיִּתְרֹצֲצוּ … לִדְרֹשׁ אֶת־יְהוָה› (“and-crack-in-pieces … to-tread
# obj-marker YHWH”)
# — event: struggle-and-inquire
m.event("struggle_and_inquire")
# witness-tier presupposed read: read_as_conflict_of_law_systems on
# struggle_in_the_womb — read, not installed
m.witness_read("struggle_in_the_womb", "read_as_conflict_of_law_systems",
                cites=["Bereshit Rabbah 63:6"])
# witness-tier presupposed read: both_members_send_her_to_a_school on
# went_to_inquire — read, not installed
m.witness_read("went_to_inquire", "both_members_send_her_to_a_school",
                cites=["Bereshit Rabbah 63:6", "Onkelos Genesis 25:22"])

# -------------------------- Gen.25.23 · THE_ORACLE_DECREE_FACTS ------------
# ‹וַיֹּ֨אמֶר יְהוָ֜ה לָ֗הּ› (“and-say YHWH to-her/its”)
# ‹שְׁנֵ֤י גיים גוֹיִם֙› (“two nation nation”)
# ‹בְּבִטְנֵ֔ךְ וּשְׁנֵ֣י לְאֻמִּ֔ים› (“in-belly-you/your and-two
# community”)
# ‹מִמֵּעַ֖יִךְ יִפָּרֵ֑דוּ וּלְאֹם֙› (“from-used-only-in-plural-the-inte-
# you/your break-through and-community”)
# ‹מִלְאֹ֣ם יֶֽאֱמָ֔ץ וְרַ֖ב› (“from-community be-alert and-many/great”)
# ‹יַעֲבֹ֥ד צָעִֽיר› (“work/serve little”)
# "[EN-AID] And YHWH said to her: Two nations are in your womb, and two
# peoples shall be separated from your bowels; and one people shall be
# stronger than the other people; and the elder shall serve the younger."
m.step("Gen.25.23")
# ‹שְׁנֵי גוֹיִם … וְרַב› (“two nation … and-many/great”)
# ‹יַעֲבֹד צָעִיר› (“work/serve little”)
# — fact holds: oracle-two-nations-elder-serves-younger
m.fact("oracle_two_nations_elder_serves_younger")
# witness-tier presupposed read: ambiguity_closed_by_the_translation on
# elder_serve_younger — read, not installed
m.witness_read("elder_serve_younger", "ambiguity_closed_by_the_translation",
                cites=["Onkelos Genesis 25:23"])
# witness-tier presupposed read: counted_twice_to_twelve on the_oracle_terms
# — read, not installed
m.witness_read("the_oracle_terms", "counted_twice_to_twelve",
                cites=["Bereshit Rabbah 63:6"])

# -------------------------- Gen.25.24 · THE_TWINS_IN_THE_WOMB --------------
# ‹וַיִּמְלְא֥וּ יָמֶ֖יהָ לָלֶ֑דֶת› (“and-fill day-her/its to-bear-young”)
# ‹וְהִנֵּ֥ה תוֹמִ֖ם בְּבִטְנָֽהּ› (“and-behold twin in-belly-her/its”)
# "[EN-AID] And her days to give birth were filled; and behold, twins were
# in her womb."
m.step("Gen.25.24")
# ‹תוֹמִם בְּבִטְנָהּ› (“twin in-belly-her/its”)
# — event: birth-due — theme twin
m.event("birth_due", themes=["tomim"])
# witness-tier presupposed read: verdict_on_the_pair_carried_by_one_letter
# on twins_written_short — read, not installed
m.witness_read("twins_written_short", "verdict_on_the_pair_carried_by_one_letter",
                cites=["Bereshit Rabbah 63:8", "Bereshit Rabbah 85:13"])

# -------------------------- Gen.25.25 · THE_ESAV_NAMING --------------------
# ‹וַיֵּצֵ֤א הָרִאשׁוֹן֙ אַדְמוֹנִ֔י› (“and-bring-forth the-first reddish”)
# ‹כֻּלּ֖וֹ כְּאַדֶּ֣רֶת שֵׂעָ֑ר› (“all-him/its like-something-ample hair”)
# ‹וַיִּקְרְא֥וּ שְׁמ֖וֹ עֵשָֽׂו› (“and-call name-him/its Esau”)
# "[EN-AID] And the first came out reddish, all of him like a hairy mantle;
# and they called his name Esau."
m.step("Gen.25.25")
# ‹וַיֵּצֵא הָרִאשׁוֹן אַדְמוֹנִי› (“and-bring-forth the-first reddish”)
# ‹… כְּאַדֶּרֶת שֵׂעָר› (“like-something-ample hair”)
# — event: birth-first — theme the-first
m.event("birth_first", themes=["ha_rishon"])
# ‹וַיִּקְרְאוּ שְׁמוֹ עֵשָׂו› (“and-call name-him/its Esau”)
# — named: Esau := Esau
m.name("esav", "esav")

# -------------------------- Gen.25.26 · THE_YAAQOV_NAMING ------------------
# ‹וְאַֽחֲרֵי־כֵ֞ן יָצָ֣א אָחִ֗יו› (“and-after so bring-forth brother-
# him/its”)
# ‹וְיָד֤וֹ אֹחֶ֨זֶת֙ בַּעֲקֵ֣ב› (“and-hand-him/its seize in-heel”)
# ‹עֵשָׂ֔ו וַיִּקְרָ֥א שְׁמ֖וֹ› (“Esau and-call name-him/its”)
# ‹יַעֲקֹ֑ב וְיִצְחָ֛ק בֶּן־שִׁשִּׁ֥ים› (“Jacob and-Isaac son sixty”)
# ‹שָׁנָ֖ה בְּלֶ֥דֶת אֹתָֽם› (“years in-bear-young obj-marker-them/their”)
# "[EN-AID] And after that his brother came out, and his hand was holding
# Esau's heel; and he called his name Jacob; and Isaac was sixty years old
# when she bore them."
m.step("Gen.25.26")
# ‹יָדוֹ אֹחֶזֶת בַּעֲקֵב› (“hand-him/its seize in-heel”)
# ‹עֵשָׂו› (“Esau”)
# — event: birth-second-heel — theme brother-him/its
m.event("birth_second_heel", themes=["achi_v"])
# ‹וַיִּקְרָא שְׁמוֹ יַעֲקֹב› (“and-call name-him/its Jacob”)
# — named: Jacob := Jacob
m.name("yaaqov", "yaaqov")

# -------------------------- Gen.25.27 · THE_TWO_MEN_GROW -------------------
# ‹וַֽיִּגְדְּלוּ֙ הַנְּעָרִ֔ים וַיְהִ֣י› (“and-be-large the-boy and-be”)
# ‹עֵשָׂ֗ו אִ֛ישׁ יֹדֵ֥עַ› (“Esau man know”)
# ‹צַ֖יִד אִ֣ישׁ שָׂדֶ֑ה› (“chase man field”)
# ‹וְיַעֲקֹב֙ אִ֣ישׁ תָּ֔ם› (“and-Jacob man complete”)
# ‹יֹשֵׁ֖ב אֹהָלִֽים› (“dwell/sit tent”)
# "[EN-AID] And the boys grew; and Esau was a man knowing hunting, a man of
# the field; and Jacob was a complete man, dwelling in tents."
m.step("Gen.25.27")
# ‹עֵשָׂו אִישׁ יֹדֵעַ› (“Esau man know”)
# ‹צַיִד … יַעֲקֹב אִישׁ› (“chase … Jacob man”)
# ‹תָּם› (“complete”)
# — fact holds: Esau-hunter-Jacob-man-complete
m.fact("esav_hunter_yaaqov_ish_tam")
# witness-tier presupposed read: study_house_written_into_the_verse on
# dweller_in_tents — read, not installed
m.witness_read("dweller_in_tents", "study_house_written_into_the_verse",
                cites=["Onkelos Genesis 25:27", "Bereshit Rabbah 63:10"])
# witness-tier presupposed read:
# thirteen_years_charter_for_a_standing_blessing on the_lads_grew — read,
# not installed
m.witness_read("the_lads_grew", "thirteen_years_charter_for_a_standing_blessing",
                cites=["Bereshit Rabbah 63:10"])

# -------------------------- Gen.25.28 · THE_SPLIT_LOVES --------------------
# ‹וַיֶּאֱהַ֥ב יִצְחָ֛ק אֶת־עֵשָׂ֖ו› (“and-have-affection-for Isaac obj-
# marker Esau”)
# ‹כִּי־צַ֣יִד בְּפִ֑יו וְרִבְקָ֖ה› (“that chase in-mouth-him/its and-
# Rebekah”)
# ‹אֹהֶ֥בֶת אֶֽת־יַעֲקֹֽב› (“have-affection-for obj-marker Jacob”)
# "[EN-AID] And Isaac loved Esau because game was in his mouth; and Rivqah
# loved Jacob."
m.step("Gen.25.28")
# ‹וַיֶּאֱהַב יִצְחָק אֶת־עֵשָׂו› (“and-have-affection-for Isaac obj-marker
# Esau”)
# ‹… וְרִבְקָה אֹהֶבֶת אֶת־יַעֲקֹב› (“and-Rebekah have-affection-for obj-
# marker Jacob”)
# — event: love-split
m.event("love_split")

# -------------------------- Gen.25.29 · THE_STEW_AND_THE_WEARY -------------
# ‹וַיָּ֥זֶד יַעֲקֹ֖ב נָזִ֑יד› (“and-seethe Jacob something-boiled”)
# ‹וַיָּבֹ֥א עֵשָׂ֛ו מִן־הַשָּׂדֶ֖ה› (“and-come/bring Esau from the-field”)
# ‹וְה֥וּא עָיֵֽף› (“and-he/it languid”)
# "[EN-AID] And Jacob boiled stew; and Esau came in from the field, and he
# was weary."
m.step("Gen.25.29")
# ‹וַיָּזֶד … נָזִיד … עָיֵף› (“and-seethe … something-boiled … languid”)
# — event: stew-and-arrive
m.event("stew_and_arrive")

# -------------------------- Gen.25.30 · THE_HALITENI_AND_EDOM_REPORT -------
# ‹וַיֹּ֨אמֶר עֵשָׂ֜ו אֶֽל־יַעֲקֹ֗ב› (“and-say Esau to Jacob”)
# ‹הַלְעִיטֵ֤נִי נָא֙ מִן־הָאָדֹ֤ם› (“swallow-greedily-me/my please from
# the-rosy”)
# ‹הָאָדֹם֙ הַזֶּ֔ה כִּ֥י› (“the-rosy the-this that”)
# ‹עָיֵ֖ף אָנֹ֑כִי עַל־כֵּ֥ן› (“languid over so”)
# ‹קָרָֽא־שְׁמ֖וֹ אֱדֽוֹם› (“call name-him/its Edom”)
# "[EN-AID] And Esau said to Jacob: Let me gulp, please, from this red, this
# red, for I am weary; therefore his name was called Edom."
m.step("Gen.25.30")
# ‹הַלְעִיטֵנִי נָא› (“swallow-greedily-me/my please”)
# — Esau speaks a demand — LET: haliteni(from-the-rosy)
m.declare("esav", "LET",
          "haliteni(min_ha_adom)")
# ‹עַל־כֵּן קָרָא־שְׁמוֹ אֱדוֹם› (“over so call name-him/its Edom”)
# — fact holds: over-so-call-shemo-Edom-report-only
m.fact("al_ken_qara_shemo_edom_report_only")
# witness-tier presupposed read: elder_died_today_and_the_heresy_at_the_pot
# on the_stew_day — read, not installed
m.witness_read("the_stew_day", "elder_died_today_and_the_heresy_at_the_pot",
                cites=["Bereshit Rabbah 63:11", "Bereshit Rabbah 63:14"])

# -------------------------- Gen.25.31 · THE_MIKHRA_PUSH --------------------
# ‹וַיֹּ֖אמֶר יַעֲקֹ֑ב מִכְרָ֥ה› (“and-say Jacob sell-ward”)
# ‹כַיּ֛וֹם אֶת־בְּכֹֽרָתְךָ֖ לִֽי› (“like-day obj-marker firstling-of-man-
# you/your to-me/my”)
# "[EN-AID] And Jacob said: Sell me as of today your birthright."
m.step("Gen.25.31")
# ‹מִכְרָה כַיּוֹם אֶת־בְּכֹרָתְךָ› (“sell-ward like-day obj-marker
# firstling-of-man-you/your”)
# ‹לִי› (“to-me/my”)
# — Jacob speaks a demand — LET: mikhra(firstling-of-man-you/your, day)
m.declare("yaaqov", "LET",
          "mikhra(bekhorat_kha, ka_yom)")
# witness-tier presupposed read: case_shelf_law_supplied_as_the_motive on
# the_sale_push — read, not installed
m.witness_read("the_sale_push", "case_shelf_law_supplied_as_the_motive",
                cites=["Bereshit Rabbah 63:13"])

# -------------------------- Gen.25.32 · THE_DISMISS_SPEECH -----------------
# ‹וַיֹּ֣אמֶר עֵשָׂ֔ו הִנֵּ֛ה› (“and-say Esau behold”)
# ‹אָנֹכִ֥י הוֹלֵ֖ךְ לָמ֑וּת› (“walk/go to-die”)
# ‹וְלָמָּה־זֶּ֥ה לִ֖י בְּכֹרָֽה› (“and-to-what this to-me/my firstling-of-
# man”)
# "[EN-AID] And Esau said: Behold, I am going to die; and what is this
# birthright to me?"
m.step("Gen.25.32")
# ‹וְלָמָּה־זֶּה לִי בְּכֹרָה› (“and-to-what this to-me/my firstling-of-
# man”)
# — fact holds: Esau-dismisses-firstling-of-man-speech
m.fact("esav_dismisses_bekhora_speech")

# -------------------------- Gen.25.33 · THE_DOUBLE_POP_SWEAR_AND_SELL ------
# ‹וַיֹּ֣אמֶר יַעֲקֹ֗ב הִשָּׁ֤בְעָה› (“and-say Jacob swear-ward”)
# ‹לִּי֙ כַּיּ֔וֹם וַיִּשָּׁבַ֖ע› (“to-me/my like-day and-swear”)
# ‹ל֑וֹ וַיִּמְכֹּ֥ר אֶת־בְּכֹרָת֖וֹ› (“to-him/its and-sell obj-marker
# firstling-of-man-him/its”)
# ‹לְיַעֲקֹֽב› (“to-Jacob”)
# "[EN-AID] And Jacob said: Swear to me as of today; and he swore to him;
# and he sold his birthright to Jacob."
m.step("Gen.25.33")
# ‹הִשָּׁבְעָה לִי כַּיּוֹם› (“swear-ward to-me/my like-day”)
# — Jacob speaks a demand — LET: hishava(to-me, day)
m.declare("yaaqov", "LET",
          "hishava(li, ka_yom)")
# ‹וַיִּשָּׁבַע לוֹ› (“and-swear to-him/its”)
# — demand settled (popped from the queue): hishava(to-me, day)
m.result("hishava(li, ka_yom)", tmark="t1")
# ‹וַיִּמְכֹּר אֶת־בְּכֹרָתוֹ לְיַעֲקֹב› (“and-sell obj-marker firstling-of-
# man-him/its to-Jacob”)
# — demand settled (popped from the queue): mikhra(firstling-of-man-
# you/your, day)
m.result("mikhra(bekhorat_kha, ka_yom)", tmark="t2")
# witness-tier presupposed read: standing_instrument_still_feared_lost on
# the_oath_on_the_sale — read, not installed
m.witness_read("the_oath_on_the_sale", "standing_instrument_still_feared_lost",
                cites=["Bereshit Rabbah 68:7"])
# witness-tier presupposed read: written_deed_and_a_countersignature on
# the_sale — read, not installed
m.witness_read("the_sale", "written_deed_and_a_countersignature",
                cites=["Bereshit Rabbah 63:14"])

# -------------------------- Gen.25.34 · THE_MEAL_AND_THE_DESPISE -----------
# ‹וְיַעֲקֹ֞ב נָתַ֣ן לְעֵשָׂ֗ו› (“and-Jacob set to-Esau”)
# ‹לֶ֚חֶם וּנְזִ֣יד עֲדָשִׁ֔ים› (“food and-something-boiled lentil”)
# ‹וַיֹּ֣אכַל וַיֵּ֔שְׁתְּ וַיָּ֖קָם› (“and-eat and-drink and-arise”)
# ‹וַיֵּלַ֑ךְ וַיִּ֥בֶז עֵשָׂ֖ו› (“and-go and-disesteem Esau”)
# ‹אֶת־הַבְּכֹרָֽה› (“obj-marker the-firstling-of-man”)
# "[EN-AID] And Jacob gave Esau bread and lentil stew; and he ate and drank
# and rose and went; and Esau despised the birthright."
m.step("Gen.25.34")
# ‹וַיֹּאכַל וַיֵּשְׁתְּ וַיָּקָם› (“and-eat and-drink and-arise”)
# ‹וַיֵּלַךְ› (“and-go”)
# — event: ?
m.event("?")
# ‹וַיִּבֶז עֵשָׂו אֶת־הַבְּכֹרָה› (“and-disesteem Esau obj-marker the-
# firstling-of-man”)
# — event: ?
m.event("?")
# witness-grounded state (its own tier): five_withheld_on_the_stew_day on
# the_elders_years
m.witness_state("the_elders_years", "five_withheld_on_the_stew_day",
                cites=["Bereshit Rabbah 63:12"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'esav': 'esav', 'yaaqov': 'yaaqov'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['haliteni(min_ha_adom)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['toledot_yitzchaq_section_header', 'yitzchaq_forty_takes_rivqa_from_padan_aram', 'oracle_two_nations_elder_serves_younger', 'esav_hunter_yaaqov_ish_tam', 'al_ken_qara_shemo_edom_report_only', 'esav_dismisses_bekhora_speech'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 16
    assert sorted(m.WORLD["witnessed"]) == ['the_elders_years']
    assert m.WORLD["witnessed"]['the_elders_years']["cites"] == ['Bereshit Rabbah 63:12']
    assert all('five_withheld_on_the_stew_day' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('entreaty_verb', 'poured_out_or_decree_overturned'), ('conception_held_for_this_prayer', 'wire_closed_from_gen_41'), ('struggle_in_the_womb', 'read_as_conflict_of_law_systems'), ('went_to_inquire', 'both_members_send_her_to_a_school'), ('elder_serve_younger', 'ambiguity_closed_by_the_translation'), ('the_oracle_terms', 'counted_twice_to_twelve'), ('twins_written_short', 'verdict_on_the_pair_carried_by_one_letter'), ('dweller_in_tents', 'study_house_written_into_the_verse'), ('the_lads_grew', 'thirteen_years_charter_for_a_standing_blessing'), ('the_stew_day', 'elder_died_today_and_the_heresy_at_the_pot'), ('the_sale_push', 'case_shelf_law_supplied_as_the_motive'), ('the_oath_on_the_sale', 'standing_instrument_still_feared_lost'), ('the_sale', 'written_deed_and_a_countersignature')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 63:5', 'Onkelos Genesis 25:21']
    assert all('poured_out_or_decree_overturned' not in f for f in m.WORLD["facts"])
    assert 'entreaty_verb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 60:13']
    assert all('wire_closed_from_gen_41' not in f for f in m.WORLD["facts"])
    assert 'conception_held_for_this_prayer' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 63:6']
    assert all('read_as_conflict_of_law_systems' not in f for f in m.WORLD["facts"])
    assert 'struggle_in_the_womb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 63:6', 'Onkelos Genesis 25:22']
    assert all('both_members_send_her_to_a_school' not in f for f in m.WORLD["facts"])
    assert 'went_to_inquire' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Onkelos Genesis 25:23']
    assert all('ambiguity_closed_by_the_translation' not in f for f in m.WORLD["facts"])
    assert 'elder_serve_younger' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 63:6']
    assert all('counted_twice_to_twelve' not in f for f in m.WORLD["facts"])
    assert 'the_oracle_terms' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 63:8', 'Bereshit Rabbah 85:13']
    assert all('verdict_on_the_pair_carried_by_one_letter' not in f for f in m.WORLD["facts"])
    assert 'twins_written_short' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Onkelos Genesis 25:27', 'Bereshit Rabbah 63:10']
    assert all('study_house_written_into_the_verse' not in f for f in m.WORLD["facts"])
    assert 'dweller_in_tents' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 63:10']
    assert all('thirteen_years_charter_for_a_standing_blessing' not in f for f in m.WORLD["facts"])
    assert 'the_lads_grew' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 63:11', 'Bereshit Rabbah 63:14']
    assert all('elder_died_today_and_the_heresy_at_the_pot' not in f for f in m.WORLD["facts"])
    assert 'the_stew_day' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 63:13']
    assert all('case_shelf_law_supplied_as_the_motive' not in f for f in m.WORLD["facts"])
    assert 'the_sale_push' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 68:7']
    assert all('standing_instrument_still_feared_lost' not in f for f in m.WORLD["facts"])
    assert 'the_oath_on_the_sale' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 63:14']
    assert all('written_deed_and_a_countersignature' not in f for f in m.WORLD["facts"])
    assert 'the_sale' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
