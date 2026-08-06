#!/usr/bin/env python3
# =============================================================================
# gen_45_wells_covenant_esau_wives — 26:17-35
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_45_wells_covenant_esau_wives.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Wells, namings, covenant swear, Shibah, Esau's wives (26:17-35)"""
from machine import Machine

m = Machine("gen_45_wells_covenant_esau_wives")

# -------------------------- Gen.26.17 · THE_LEKH_DEED_ACROSS_THE_WALL ------
# וַיֵּ֥לֶךְ מִשָּׁ֖ם יִצְחָ֑ק וַיִּ֥חַן בְּֽנַחַל־גְּרָ֖ר וַיֵּ֥שֶׁב שָֽׁם
# "[EN-AID] And Isaac went from there and encamped in the wadi of Gerar, and
# dwelt there."
m.step("Gen.26.17")
# ‹וַיֵּלֶךְ מִשָּׁם יִצְחָק› event: ?
m.event("?")
# ‹וַיִּחַן בְּנַחַל־גְּרָר וַיֵּשֶׁב שָׁם› event: ?
m.event("?")
# ‹יִצְחָק … גְּרָר› reads without prior install (flag, not fix): yitzchaq,
# gerar
m.presupposed("yitzchaq", "gerar")

# -------------------------- Gen.26.18 · THE_REDIG_AND_THE_RESTORED_NAMES ---
# וַיָּ֨שָׁב יִצְחָ֜ק וַיַּחְפֹּ֣ר אֶת־בְּאֵרֹ֣ת הַמַּ֗יִם אֲשֶׁ֤ר חָֽפְרוּ֙
# בִּימֵי֙ אַבְרָהָ֣ם אָבִ֔יו וַיְסַתְּמ֣וּם פְּלִשְׁתִּ֔ים אַחֲרֵ֖י מ֣וֹת
# אַבְרָהָ֑ם וַיִּקְרָ֤א לָהֶן֙ שֵׁמ֔וֹת כַּשֵּׁמֹ֕ת אֲשֶׁר־קָרָ֥א לָהֶ֖ן
# אָבִֽיו
# "[EN-AID] And Isaac dug again the wells of water that they had dug in the
# days of Abraham his father, which the Philistines had stopped up after
# Abraham's death; and he called them names like the names his father had
# called them."
m.step("Gen.26.18")
# ‹וַיָּשָׁב … וַיַּחְפֹּר אֶת־בְּאֵרֹת הַמַּיִם› event: redig-wells — agent
# yitzchaq; theme beerot-avraham
m.event("redig_wells", agent="yitzchaq", themes=["beerot_avraham"])
# ‹וַיִּקְרָא לָהֶן שֵׁמוֹת כַּשֵּׁמוֹת אֲשֶׁר־קָרָא לָהֶן אָבִיו› event: ?
m.event("?")

# -------------------------- Gen.26.19 · THE_WELL_OF_LIVING_WATER -----------
# וַיַּחְפְּר֥וּ עַבְדֵֽי־יִצְחָ֖ק בַּנָּ֑חַל וַיִּ֨מְצְאוּ־שָׁ֔ם בְּאֵ֖ר
# מַ֥יִם חַיִּֽים
# "[EN-AID] And Isaac's servants dug in the wadi and found there a well of
# living water."
m.step("Gen.26.19")
# ‹וַיַּחְפְּרוּ … וַיִּמְצְאוּ … בְּאֵר מַיִם חַיִּים› event: dig-and-find
# — agent avde-yitzchaq; theme beer-waters-chayim
m.event("dig_and_find", agent="avde_yitzchaq", themes=["beer_mayim_chayim"])

# -------------------------- Gen.26.20 · THE_QUARREL_AND_THE_NAME_ESEK ------
# וַיָּרִ֜יבוּ רֹעֵ֣י גְרָ֗ר עִם־רֹעֵ֥י יִצְחָ֛ק לֵאמֹ֖ר לָ֣נוּ הַמָּ֑יִם
# וַיִּקְרָ֤א שֵֽׁם־הַבְּאֵר֙ עֵ֔שֶׂק כִּ֥י הִֽתְעַשְּׂק֖וּ עִמּֽוֹ
# "[EN-AID] And the herdsmen of Gerar quarreled with Isaac's herdsmen,
# saying: The water is ours. And he called the name of the well Esek,
# because they contended with him."
m.step("Gen.26.20")
# ‹וַיָּרִיבוּ רֹעֵי גְרָר עִם־רֹעֵי יִצְחָק› event: quarrel — agent roe-
# gerar
m.event("quarrel", agent="roe_gerar")
# ‹וַיִּקְרָא שֵׁם־הַבְּאֵר עֵשֶׂק› named: beer-eseq := eseq
m.name("beer_eseq", "eseq")

# -------------------------- Gen.26.21 · THE_SECOND_WELL_SITNAH -------------
# וַֽיַּחְפְּרוּ֙ בְּאֵ֣ר אַחֶ֔רֶת וַיָּרִ֖יבוּ גַּם־עָלֶ֑יהָ וַיִּקְרָ֥א
# שְׁמָ֖הּ שִׂטְנָֽה
# "[EN-AID] And they dug another well, and they quarreled over it too; and
# he called its name Sitnah."
m.step("Gen.26.21")
# ‹וַיַּחְפְּרוּ בְּאֵר אַחֶרֶת וַיָּרִיבוּ גַּם־עָלֶיהָ› event: dig-and-
# quarrel — theme beer-acheret
m.event("dig_and_quarrel", themes=["beer_acheret"])
# ‹וַיִּקְרָא שְׁמָהּ שִׂטְנָה› named: beer-sitna := sitna
m.name("beer_sitna", "sitna")

# -------------------------- Gen.26.22 · THE_THIRD_WELL_REHOBOTH ------------
# וַיַּעְתֵּ֣ק מִשָּׁ֗ם וַיַּחְפֹּר֙ בְּאֵ֣ר אַחֶ֔רֶת וְלֹ֥א רָב֖וּ עָלֶ֑יהָ
# וַיִּקְרָ֤א שְׁמָהּ֙ רְחֹב֔וֹת וַיֹּ֗אמֶר כִּֽי־עַתָּ֞ה הִרְחִ֧יב יְהוָ֛ה
# לָ֖נוּ וּפָרִ֥ינוּ בָאָֽרֶץ
# "[EN-AID] And he moved from there and dug another well, and they did not
# quarrel over it; and he called its name Rehoboth, and he said: For now
# YHWH has made room for us, and we shall be fruitful in the land."
m.step("Gen.26.22")
# ‹וַיַּעְתֵּק … וַיַּחְפֹּר … וְלֹא רָבוּ› event: move-dig-no-quarrel —
# agent yitzchaq
m.event("move_dig_no_quarrel", agent="yitzchaq")
# ‹וַיִּקְרָא שְׁמָהּ רְחֹבוֹת› named: beer-rechovot := rechovot
m.name("beer_rechovot", "rechovot")
# ‹כִּי־עַתָּה הִרְחִיב יְהוָה לָנוּ וּפָרִינוּ בָאָרֶץ› fact holds:
# hirchiv-the-LORD-to-nu-and-farinu
m.fact("hirchiv_YHWH_la_nu_u_farinu")

# -------------------------- Gen.26.23 · THE_ASCENT_TO_BEER_SHEBA -----------
# וַיַּ֥עַל מִשָּׁ֖ם בְּאֵ֥ר שָֽׁבַע
# "[EN-AID] And he went up from there to Beer-sheba."
m.step("Gen.26.23")
# ‹וַיַּעַל מִשָּׁם בְּאֵר שָׁבַע› event: go-up — agent yitzchaq
m.event("go_up", agent="yitzchaq")

# -------------------------- Gen.26.24 · THE_NIGHT_WORD_AND_AL_TIRA ---------
# וַיֵּרָ֨א אֵלָ֤יו יְהוָה֙ בַּלַּ֣יְלָה הַה֔וּא וַיֹּ֕אמֶר אָנֹכִ֕י
# אֱלֹהֵ֖י אַבְרָהָ֣ם אָבִ֑יךָ אַל־תִּירָא֙ כִּֽי־אִתְּךָ֣ אָנֹ֔כִי
# וּבֵֽרַכְתִּ֨יךָ֙ וְהִרְבֵּיתִ֣י אֶֽת־זַרְעֲךָ֔ בַּעֲב֖וּר אַבְרָהָ֥ם
# עַבְדִּֽי
# "[EN-AID] And YHWH appeared to him that night and said: I am the God of
# Abraham your father; do not fear, for I am with you, and I will bless you
# and multiply your seed for the sake of Abraham My servant."
m.step("Gen.26.24")
# ‹וַיֵּרָא אֵלָיו יְהוָה בַּלַּיְלָה הַהוּא וַיֹּאמֶר› event: appear-night
# — agent the-LORD
m.event("appear_night", agent="YHWH")
# ‹אָנֹכִי אֱלֹהֵי אַבְרָהָם אָבִיךָ› fact holds: anokhi-elohe-avraham-avi-
# kha
m.fact("anokhi_elohe_avraham_avi_kha")
# ‹אַל־תִּירָא› the-LORD speaks a demand — LET-NOT: tira(yitzchaq)
m.declare("YHWH", "LET-NOT",
          "tira(yitzchaq)")
# ‹כִּי־אִתְּךָ אָנֹכִי וּבֵרַכְתִּיךָ וְהִרְבֵּיתִי אֶת־זַרְעֲךָ› fact
# holds: kha-anokhi-and-verakhti-and-hirbeti
m.fact("et_kha_anokhi_u_verakhti_ve_hirbeti")

# -------------------------- Gen.26.25 · THE_ALTAR_INVOCATION_AND_KARAH_DIG -
# וַיִּ֧בֶן שָׁ֣ם מִזְבֵּ֗חַ וַיִּקְרָא֙ בְּשֵׁ֣ם יְהוָ֔ה וַיֶּט־שָׁ֖ם
# אָהֳל֑וֹ וַיִּכְרוּ־שָׁ֥ם עַבְדֵי־יִצְחָ֖ק בְּאֵֽר
# "[EN-AID] And he built an altar there and called on the name of YHWH, and
# pitched his tent there; and Isaac's servants dug a well there."
m.step("Gen.26.25")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ … וַיֶּט שָׁם אָהֳלוֹ› event: ?
m.event("?")
# ‹וַיִּקְרָא בְּשֵׁם יְהוָה› event: ?
m.event("?")
# ‹וַיִּכְרוּ שָׁם עַבְדֵי יִצְחָק בְּאֵר› event: ?
m.event("?")

# -------------------------- Gen.26.26 · THE_VISITORS_FROM_GERAR ------------
# וַאֲבִימֶ֕לֶךְ הָלַ֥ךְ אֵלָ֖יו מִגְּרָ֑ר וַאֲחֻזַּת֙ מֵרֵעֵ֔הוּ וּפִיכֹ֖ל
# שַׂר־צְבָאֽוֹ
# "[EN-AID] And Abimelech went to him from Gerar, with Achuzzath his friend
# and Phichol the commander of his army."
m.step("Gen.26.26")
# ‹וַאֲבִימֶלֶךְ הָלַךְ אֵלָיו מִגְּרָר› event: visit — agent avimelekh
m.event("visit", agent="avimelekh")
# ‹אֲחֻזַּת … פִיכֹל› reads without prior install (flag, not fix): achuzat,
# fikhol, merea
m.presupposed("achuzat", "fikhol", "merea")

# -------------------------- Gen.26.27 · THE_WHY_HAVE_YOU_COME --------------
# וַיֹּ֤אמֶר אֲלֵהֶם֙ יִצְחָ֔ק מַדּ֖וּעַ בָּאתֶ֣ם אֵלָ֑י וְאַתֶּם֙
# שְׂנֵאתֶ֣ם אֹתִ֔י וַתְּשַׁלְּח֖וּנִי מֵאִתְּכֶֽם
# "[EN-AID] And Isaac said to them: Why have you come to me, seeing you hate
# me and have sent me away from you?"
m.step("Gen.26.27")
# ‹וַיֹּאמֶר … מַדּוּעַ בָּאתֶם› event: say — agent yitzchaq
m.event("say", agent="yitzchaq")

# -------------------------- Gen.26.28 · THE_COVENANT_VOLITIVES -------------
# וַיֹּאמְר֗וּ רָא֣וֹ רָאִינוּ֮ כִּֽי־הָיָ֣ה יְהוָ֣ה ׀ עִמָּךְ֒ וַנֹּ֗אמֶר
# תְּהִ֨י נָ֥א אָלָ֛ה בֵּינוֹתֵ֖ינוּ בֵּינֵ֣ינוּ וּבֵינֶ֑ךָ וְנִכְרְתָ֥ה
# בְרִ֖ית עִמָּֽךְ
# "[EN-AID] And they said: We have surely seen that YHWH is with you; and we
# said: Let there be an oath between us, between us and you, and let us cut
# a covenant with you."
m.step("Gen.26.28")
# ‹רָאוֹ רָאִינוּ כִּי־הָיָה יְהוָה עִמָּךְ› fact holds: rao-rainu-the-LORD-
# ima-kha
m.fact("rao_rainu_YHWH_ima_kha")
# ‹תְּהִי נָא אָלָה בֵּינוֹתֵינוּ› avimelekh-party speaks a demand — LET:
# tehi(ala-between-us)
m.declare("avimelekh_party", "LET",
          "tehi(ala_between_us)")
# ‹וְנִכְרְתָה בְרִית עִמָּךְ› avimelekh-party speaks a demand — CMD-US?:
# nikhreta(berit-if-kha)
m.declare("avimelekh_party", "CMD-US?",
          "nikhreta(berit_im_kha)")

# -------------------------- Gen.26.29 · THE_OATH_CONTENT_TERMS -------------
# אִם־תַּעֲשֵׂ֨ה עִמָּ֜נוּ רָעָ֗ה כַּאֲשֶׁר֙ לֹ֣א נְגַֽעֲנ֔וּךָ וְכַאֲשֶׁ֨ר
# עָשִׂ֤ינוּ עִמְּךָ֙ רַק־ט֔וֹב וַנְּשַׁלֵּֽחֲךָ֖ בְּשָׁל֑וֹם אַתָּ֥ה
# עַתָּ֖ה בְּר֥וּךְ יְהוָֽה
# "[EN-AID] that you will do us no harm, as we have not touched you and as
# we have done with you only good and have sent you away in peace; you are
# now the blessed of YHWH."
m.step("Gen.26.29")
# ‹אִם־תַּעֲשֵׂה עִמָּנוּ רָעָה …› fact holds: if-taase-ima-nu-raa-oath-
# content
m.fact("im_taase_ima_nu_raa_oath_content")
# ‹אַתָּה עַתָּה בְּרוּךְ יְהוָה› fact holds: ata-ata-berukh-the-LORD
m.fact("ata_ata_berukh_YHWH")

# -------------------------- Gen.26.30 · THE_FEAST --------------------------
# וַיַּ֤עַשׂ לָהֶם֙ מִשְׁתֶּ֔ה וַיֹּאכְל֖וּ וַיִּשְׁתּֽוּ
# "[EN-AID] And he made them a feast, and they ate and drank."
m.step("Gen.26.30")
# ‹וַיַּעַשׂ … מִשְׁתֶּה וַיֹּאכְלוּ וַיִּשְׁתּוּ› event: feast-eat-drink —
# agent yitzchaq-and-guests
m.event("feast_eat_drink", agent="yitzchaq_and_guests")

# -------------------------- Gen.26.31 · THE_SWEAR_OTHER_VERB_CENTERPIECE ---
# וַיַּשְׁכִּ֣ימוּ בַבֹּ֔קֶר וַיִּשָּׁבְע֖וּ אִ֣ישׁ לְאָחִ֑יו וַיְשַׁלְּחֵ֣ם
# יִצְחָ֔ק וַיֵּלְכ֥וּ מֵאִתּ֖וֹ בְּשָׁלֽוֹם
# "[EN-AID] And they rose early in the morning and swore each to his
# brother; and Isaac sent them away, and they went from him in peace."
m.step("Gen.26.31")
# ‹וַיַּשְׁכִּימוּ … וַיִּשָּׁבְעוּ אִישׁ לְאָחִיו› event: ?
m.event("?")
# ‹וַיִּשָּׁבְעוּ ≠ תְּהִי / נִכְרְתָה› fact holds: other-verb-non-pop-tehi-
# and-nikhreta
m.fact("other_verb_non_pop_tehi_and_nikhreta")
# ‹וַיְשַׁלְּחֵם יִצְחָק וַיֵּלְכוּ … בְּשָׁלוֹם› event: ?
m.event("?")

# -------------------------- Gen.26.32 · THE_WELL_FOUND_REPORT --------------
# וַיְהִ֣י ׀ בַּיּ֣וֹם הַה֗וּא וַיָּבֹ֨אוּ֙ עַבְדֵ֣י יִצְחָ֔ק וַיַּגִּ֣דוּ
# לוֹ֔ עַל־אֹד֥וֹת הַבְּאֵ֖ר אֲשֶׁ֣ר חָפָ֑רוּ וַיֹּ֥אמְרוּ ל֖וֹ מָצָ֥אנוּ
# מָֽיִם
# "[EN-AID] And it came to pass the same day that Isaac's servants came and
# told him about the well that they had dug, and said to him: We have found
# water."
m.step("Gen.26.32")
# ‹וַיַּגִּדוּ … מָצָאנוּ מָיִם› event: report-well-found — agent avde-
# yitzchaq
m.event("report_well_found", agent="avde_yitzchaq")

# -------------------------- Gen.26.33 · THE_NAME_SHIBAH_AND_THE_CITY_ETIOLOGY -
# וַיִּקְרָ֥א אֹתָ֖הּ שִׁבְעָ֑ה עַל־כֵּ֤ן שֵׁם־הָעִיר֙ בְּאֵ֣ר שֶׁ֔בַע עַ֖ד
# הַיּ֥וֹם הַזֶּֽה
# "[EN-AID] And he called it Shibah; therefore the name of the city is Beer-
# sheba to this day."
m.step("Gen.26.33")
# ‹וַיִּקְרָא אֹתָהּ שִׁבְעָה› named: beer-shiva := shiva
m.name("beer_shiva", "shiva")
# ‹עַל־כֵּן שֵׁם הָעִיר בְּאֵר שֶׁבַע עַד הַיּוֹם הַזֶּה› fact holds: upon-
# ken-shem-the-ir-beer-seven
m.fact("al_ken_shem_ha_ir_beer_sheva")

# -------------------------- Gen.26.34 · ESAU_TAKES_TWO_HITTITE_WIVES -------
# וַיְהִ֤י עֵשָׂו֙ בֶּן־אַרְבָּעִ֣ים שָׁנָ֔ה וַיִּקַּ֤ח אִשָּׁה֙
# אֶת־יְהוּדִ֔ית בַּת־בְּאֵרִ֖י הַֽחִתִּ֑י וְאֶת־בָּ֣שְׂמַ֔ת בַּת־אֵילֹ֖ן
# הַֽחִתִּֽי
# "[EN-AID] And when Esau was forty years old he took as wife Judith
# daughter of Beeri the Hittite, and Basemath daughter of Elon the Hittite."
m.step("Gen.26.34")
# ‹עֵשָׂו בֶּן־אַרְבָּעִים שָׁנָה› fact holds: esav-ben-arbaim-shana
m.fact("esav_ben_arbaim_shana")
# ‹וַיִּקַּח אִשָּׁה אֶת־יְהוּדִית … וְאֶת־בָּשְׂמַת› event: take-wives —
# agent esav
m.event("take_wives", agent="esav")
# ‹יְהוּדִית … בָּשְׂמַת … בְּאֵרִי … אֵילוֹן› the world gains: yehudit,
# basmat, beeri, elon
m.install("yehudit", "basmat", "beeri", "elon")

# -------------------------- Gen.26.35 · BITTERNESS_OF_SPIRIT ---------------
# וַתִּהְיֶ֖יןָ מֹ֣רַת ר֑וּחַ לְיִצְחָ֖ק וּלְרִבְקָֽה
# "[EN-AID] And they were a bitterness of spirit to Isaac and to Rivqah."
m.step("Gen.26.35")
# ‹מֹרַת רוּחַ לְיִצְחָק וּלְרִבְקָה› fact holds: morat-spirit-wind-to-
# yitzchaq-and-to-rivqah
m.fact("morat_ruach_le_yitzchaq_u_le_rivqah")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'yehudit', 'elon', 'basmat', 'beeri'}
    assert m.presupposed_set() == {'achuzat', 'gerar', 'merea', 'fikhol', 'yitzchaq'}
    assert m.REGISTRY["names"] == {'beer_eseq': 'eseq', 'beer_sitna': 'sitna', 'beer_rechovot': 'rechovot', 'beer_shiva': 'shiva'}
    assert m.REGISTRY["writes"] == 4
    assert m.tests_list() == []
    assert m.open_demands() == ['tira(yitzchaq)', 'tehi(ala_between_us)', 'nikhreta(berit_im_kha)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5, 'named_before_any_presence': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['hirchiv_YHWH_la_nu_u_farinu', 'anokhi_elohe_avraham_avi_kha', 'et_kha_anokhi_u_verakhti_ve_hirbeti', 'rao_rainu_YHWH_ima_kha', 'im_taase_ima_nu_raa_oath_content', 'ata_ata_berukh_YHWH', 'other_verb_non_pop_tehi_and_nikhreta', 'al_ken_shem_ha_ir_beer_sheva', 'esav_ben_arbaim_shana', 'morat_ruach_le_yitzchaq_u_le_rivqah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 27
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
