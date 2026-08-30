#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_16_ark_spec — 6:9-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_16_ark_spec.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The ark spec: the blueprint, the covenant word, the first obeyed command (6:9-22)"""
from machine import Machine

m = Machine("gen_16_ark_spec")

# -------------------------- Gen.6.9 · TOLEDOT_NOACH_THE_WALKER -------------
# אֵלֶּה תּוֹלְדֹת נֹחַ נֹחַ אִישׁ צַדִּיק תָּמִים הָיָה בְּדֹרֹתָיו
# אֶת־הָאֱלֹהִים הִתְהַלֶּךְ־נֹחַ
# "These are the generations of Noah. Noah was in his generations a man
# righteous and whole-hearted; Noah walked with God."
m.step("Gen.6.9")
# ‹אֵלֶּה תּוֹלְדֹת נֹחַ› (“these generations-of Noach”) — section
# generations-Noach: eleh toledot noach — the third generations header
m.section("toledot_noach", "eleh toledot noach — the third generations header")
# ‹אִישׁ צַדִּיק תָּמִים הָיָה בְּדֹרֹתָיו אֶת־הָאֱלֹהִים הִתְהַלֶּךְ־נֹחַ›
# (“man righteous whole was in-his-generations with the-God walked Noach”) —
# fact holds: man-righteous-whole-in-his-generations; with-the-God-walked-
# Noach
m.fact("ish_tzaddik_tamim_be_dorotav",
       "et_ha_elohim_hithalekh_noach")
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")
# witness-grounded state (its own tier): two_domains_and_disputed_qualifier
# on noach_epithets
m.witness_state("noach_epithets", "two_domains_and_disputed_qualifier",
                cites=["Bereshit Rabbah 30:9", "Avodah Zarah 6a:2", "Bereshit Rabbah 30:10"])
# witness-tier presupposed read: exclusion_particle on eleh_header — read,
# not installed
m.witness_read("eleh_header", "exclusion_particle",
                cites=["Bereshit Rabbah 30:3"])

# -------------------------- Gen.6.10 · THREE_SONS_RESTATED -----------------
# וַיּוֹלֶד נֹחַ שְׁלֹשָׁה בָנִים אֶת־שֵׁם אֶת־חָם וְאֶת־יָפֶת
# "And Noah begot three sons, Shem, Ham, and Japheth."
m.step("Gen.6.10")
# ‹וַיּוֹלֶד נֹחַ שְׁלֹשָׁה בָנִים אֶת־שֵׁם אֶת־חָם וְאֶת־יָפֶת› (“and-he-
# begot Noach three sons obj-marker Shem obj-marker Cham and-obj-marker
# Yafet”) — event: beget — agent Noach; theme Shem, Cham, Yafet
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- Gen.6.11 · EARTH_CORRUPTED_FILLED --------------
# וַתִּשָּׁחֵת הָאָרֶץ לִפְנֵי הָאֱלֹהִים וַתִּמָּלֵא הָאָרֶץ חָמָס
# "And the earth was corrupt before God, and the earth was filled with
# violence."
m.step("Gen.6.11")
# ‹וַתִּשָּׁחֵת הָאָרֶץ לִפְנֵי הָאֱלֹהִים› (“and-was-corrupted the-earth
# before the-God”) — event: corrupt — theme the-earth
m.event("corrupt", themes=["ha_aretz"])
# ‹וַתִּמָּלֵא הָאָרֶץ חָמָס› (“and-was-filled the-earth violence”) — fact
# holds: and-was-filled-the-earth-violence
m.fact("va_timale_ha_aretz_chamas")
# witness-tier presupposed read: threshold_definition_and_capital_list on
# chamas_vocabulary — read, not installed
m.witness_read("chamas_vocabulary", "threshold_definition_and_capital_list",
                cites=["Bereshit Rabbah 31:5", "Bereshit Rabbah 31:6", "Sanhedrin 57a:1"])

# -------------------------- Gen.6.12 · THIRD_SEEING_BEHOLD_CORRUPTED -------
# וַיַּרְא אֱלֹהִים אֶת־הָאָרֶץ וְהִנֵּה נִשְׁחָתָה כִּי־הִשְׁחִית
# כָּל־בָּשָׂר אֶת־דַּרְכּוֹ עַל־הָאָרֶץ
# "And God saw the earth, and, behold, it was corrupt; for all flesh had
# corrupted their way upon the earth."
m.step("Gen.6.12")
# ‹וַיַּרְא אֱלֹהִים אֶת־הָאָרֶץ› (“and-He-saw God obj-marker the-earth”) —
# event: see — agent God; theme the-earth
m.event("see", agent="Elohim", themes=["ha_aretz"])
# ‹וְהִנֵּה נִשְׁחָתָה› (“and-behold corrupted”) — spec-delta — spec said
# and-He-saw God with-all-which make and-behold good very — and behold, very
# good (1:31, frozen day 6), delivery says and-He-saw God with-the-earth
# and-behold was-corrupted — and behold, CORRUPTED (6:12)
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — and behold, very good (1:31, frozen day 6)",
             "va-yar Elohim et-ha-aretz ve-hinneh nishchatah — and behold, CORRUPTED (6:12)")
# ‹כִּי־הִשְׁחִית כָּל־בָּשָׂר אֶת־דַּרְכּוֹ› (“for had-corrupted all flesh
# obj-marker its-way”) — fact holds: had-corrupted-all-flesh-with-its-way
m.fact("hishchit_kol_basar_et_darko")

# -------------------------- Gen.6.13 · END_DECREE_SPOKEN_TO_NOACH ----------
# וַיֹּאמֶר אֱלֹהִים לְנֹחַ קֵץ כָּל־בָּשָׂר בָּא לְפָנַי כִּי־מָלְאָה
# הָאָרֶץ חָמָס מִפְּנֵיהֶם וְהִנְנִי מַשְׁחִיתָם אֶת־הָאָרֶץ
# "And God said unto Noah: 'The end of all flesh is come before Me; for the
# earth is filled with violence through them; and, behold, I will destroy
# them with the earth.'"
m.step("Gen.6.13")
# ‹וַיֹּאמֶר אֱלֹהִים לְנֹחַ› (“and-He-said God to-Noach”) — event: say —
# agent God; theme Noach
m.event("say", agent="Elohim", themes=["noach"])
# ‹קֵץ כָּל־בָּשָׂר בָּא לְפָנַי … וְהִנְנִי מַשְׁחִיתָם אֶת־הָאָרֶץ› (“end-
# of all flesh has-come before-Me … and-behold-Me destroying-them with the-
# earth”) — fact holds: end-of-all-flesh-has-come-before-Me; behold-I-
# destroying-them-with-the-earth
m.fact("qetz_kol_basar_ba_lefanai",
       "hineni_mashchitam_et_ha_aretz")

# -------------------------- Gen.6.14 · COMMISSION_MAKE_THE_ARK -------------
# עֲשֵׂה לְךָ תֵּבַת עֲצֵי־גֹפֶר קִנִּים תַּעֲשֶׂה אֶת־הַתֵּבָה וְכָפַרְתָּ
# אֹתָהּ מִבַּיִת וּמִחוּץ בַּכֹּפֶר
# "Make thee an ark of gopher wood; with rooms shalt thou make the ark, and
# shalt pitch it within and without with pitch."
m.step("Gen.6.14")
# ‹עֲשֵׂה לְךָ תֵּבַת עֲצֵי־גֹפֶר› (“make for-yourself ark-of woods-of
# gofer”) — God speaks a demand — LET: make(Noach, ark)
m.declare("Elohim", "LET",
          "aseh(noach, tevah)")
# ‹קִנִּים תַּעֲשֶׂה אֶת־הַתֵּבָה וְכָפַרְתָּ אֹתָהּ … בַּכֹּפֶר› (“rooms
# you-shall-make with the-ark and-you-shall-pitch it … with-the-pitch”) —
# fact holds: ark-of-wood-of-gofer-rooms; and-you-shall-pitch-has-come-pitch
m.fact("tevat_atzei_gofer_qinim",
       "ve_khafarta_ba_kofer")
# witness-tier presupposed read: make_for_yourself_census on build_command —
# read, not installed
m.witness_read("build_command", "make_for_yourself_census",
                cites=["Jerusalem Talmud Rosh Hashanah 3:9:2"])

# -------------------------- Gen.6.15 · BLUEPRINT_DIMENSIONS ----------------
# וְזֶה אֲשֶׁר תַּעֲשֶׂה אֹתָהּ שְׁלֹשׁ מֵאוֹת אַמָּה אֹרֶךְ הַתֵּבָה
# חֲמִשִּׁים אַמָּה רָחְבָּהּ וּשְׁלֹשִׁים אַמָּה קוֹמָתָהּ
# "And this is how thou shalt make it: the length of the ark three hundred
# cubits, the breadth of it fifty cubits, and the height of it thirty
# cubits."
m.step("Gen.6.15")
# ‹שְׁלֹשׁ מֵאוֹת אַמָּה אֹרֶךְ … חֲמִשִּׁים אַמָּה רָחְבָּהּ וּשְׁלֹשִׁים
# אַמָּה קוֹמָתָהּ› (“three hundred cubit length-of … fifty cubit its-width
# and-thirty cubit its-height”) — fact holds: three-hundred-cubit-length-of;
# fifty-cubit-its-width; thirty-cubit-its-height
m.fact("shelosh_meot_amah_orekh",
       "chamishim_amah_rochbah",
       "sheloshim_amah_qomatah")
# witness-tier presupposed read: shipwright_ratios_and_disputed_compartments
# on ark_dimensions — read, not installed
m.witness_read("ark_dimensions", "shipwright_ratios_and_disputed_compartments",
                cites=["Bereshit Rabbah 31:10", "Sanhedrin 108b:10", "Bereshit Rabbah 31:11", "Sanhedrin 108b:11"])

# -------------------------- Gen.6.16 · BLUEPRINT_LIGHT_DOOR_DECKS ----------
# צֹהַר תַּעֲשֶׂה לַתֵּבָה וְאֶל־אַמָּה תְּכַלֶנָּה מִלְמַעְלָה וּפֶתַח
# הַתֵּבָה בְּצִדָּהּ תָּשִׂים תַּחְתִּיִּם שְׁנִיִּם וּשְׁלִשִׁים
# תַּעֲשֶׂהָ
# "A light shalt thou make to the ark, and to a cubit shalt thou finish it
# upward; and the door of the ark shalt thou set in the side thereof; with
# lower, second, and third stories shalt thou make it."
m.step("Gen.6.16")
# ‹צֹהַר … וּפֶתַח הַתֵּבָה בְּצִדָּהּ … תַּחְתִּיִּם שְׁנִיִּם
# וּשְׁלִשִׁים› (“a-light … and-door-of the-ark in-its-side … lower second
# and-third”) — fact holds: a-light-to-ark; door-opening-has-come-its-side;
# lower-second-decks-and-third-decks
m.fact("tzohar_la_tevah",
       "petach_ba_tzidah",
       "tachtiyim_shniyim_u_shlishim")
# witness-tier presupposed read: pitch_regime_compared_to_the_basket on
# vessel_spec_delta — read, not installed
m.witness_read("vessel_spec_delta", "pitch_regime_compared_to_the_basket",
                cites=["Bereshit Rabbah 31:9"])

# -------------------------- Gen.6.17 · FLOOD_ANNOUNCED ---------------------
# וַאֲנִי הִנְנִי מֵבִיא אֶת־הַמַּבּוּל מַיִם עַל־הָאָרֶץ לְשַׁחֵת
# כָּל־בָּשָׂר אֲשֶׁר־בּוֹ רוּחַ חַיִּים מִתַּחַת הַשָּׁמָיִם כֹּל
# אֲשֶׁר־בָּאָרֶץ יִגְוָע
# "And I, behold, I do bring the flood of waters upon the earth, to destroy
# all flesh, wherein is the breath of life, from under heaven; every thing
# that is in the earth shall perish."
m.step("Gen.6.17")
# ‹וַאֲנִי הִנְנִי מֵבִיא אֶת־הַמַּבּוּל … כֹּל אֲשֶׁר־בָּאָרֶץ יִגְוָע›
# (“and-I behold-Me bringing obj-marker the-flood … all which in-the-earth
# shall-expire”) — fact holds: behold-I-bringing-with-the-flood-waters; all-
# which-has-come-earth-shall-expire
m.fact("hineni_mevi_et_ha_mabul_mayim",
       "kol_asher_ba_aretz_yigva")

# -------------------------- Gen.6.18 · COVENANT_PROMISED_BOARDING_LIST -----
# וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתָּךְ וּבָאתָ אֶל־הַתֵּבָה אַתָּה וּבָנֶיךָ
# וְאִשְׁתְּךָ וּנְשֵׁי־בָנֶיךָ אִתָּךְ
# "But I will establish My covenant with thee; and thou shalt come into the
# ark, thou, and thy sons, and thy wife, and thy sons' wives with thee."
m.step("Gen.6.18")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתָּךְ וּבָאתָ אֶל־הַתֵּבָה› (“and-I-will-
# establish obj-marker My-covenant with-you and-you-shall-come to the-ark”)
# — fact holds: and-I-will-establish-with-My-covenant-with-you; and-you-
# shall-come-to-the-ark-you-and-your-sons
m.fact("va_hakimoti_et_briti_itakh",
       "u_vata_el_ha_tevah_atah_u_vanekha")
# witness-tier presupposed read: ark_abstinence_from_the_order on
# covenant_entry_listing — read, not installed
m.witness_read("covenant_entry_listing", "ark_abstinence_from_the_order",
                cites=["Bereshit Rabbah 34:7", "Jerusalem Talmud Taanit 1:6:10"])

# -------------------------- Gen.6.19 · MANIFEST_TWO_OF_ALL -----------------
# וּמִכָּל־הָחַי מִכָּל־בָּשָׂר שְׁנַיִם מִכֹּל תָּבִיא אֶל־הַתֵּבָה
# לְהַחֲיֹת אִתָּךְ זָכָר וּנְקֵבָה יִהְיוּ
# "And of every living thing of all flesh, two of every sort shalt thou
# bring into the ark, to keep them alive with thee; they shall be male and
# female."
m.step("Gen.6.19")
# ‹שְׁנַיִם מִכֹּל תָּבִיא … זָכָר וּנְקֵבָה יִהְיוּ› (“two from-all you-
# shall-bring … male and-female they-shall-be”) — fact holds: two-from-all-
# you-shall-bring-to-the-ark; male-and-female-they-shall-be
m.fact("shnayim_mi_kol_tavi_el_ha_tevah",
       "zakhar_u_nekevah_yihyu")
# witness-tier presupposed read: offering_fitness_standard on intake_roster
# — read, not installed
m.witness_read("intake_roster", "offering_fitness_standard",
                cites=["Avodah Zarah 51a:15", "Avodah Zarah 51a:18", "Jerusalem Talmud Pesachim 9:5:2", "Sanhedrin 57a:7"])

# -------------------------- Gen.6.20 · MANIFEST_BY_KINDS_SELF_LOADING ------
# מֵהָעוֹף לְמִינֵהוּ וּמִן־הַבְּהֵמָה לְמִינָהּ מִכֹּל רֶמֶשׂ הָאֲדָמָה
# לְמִינֵהוּ שְׁנַיִם מִכֹּל יָבֹאוּ אֵלֶיךָ לְהַחֲיוֹת
# "Of the fowl after their kind, and of the cattle after their kind, of
# every creeping thing of the ground after its kind, two of every sort shall
# come unto thee, to keep them alive."
m.step("Gen.6.20")
# ‹מֵהָעוֹף לְמִינֵהוּ … שְׁנַיִם מִכֹּל יָבֹאוּ אֵלֶיךָ› (“from-the-bird
# by-its-kind … two from-all shall-come to-you”) — fact holds: to-its-kind-
# manifest-bird-livestock-creeper-of
m.fact("le_minehu_manifest_of_behemah_remes")

# -------------------------- Gen.6.21 · SECOND_IMPERATIVE_PROVISIONS --------
# וְאַתָּה קַח־לְךָ מִכָּל־מַאֲכָל אֲשֶׁר יֵאָכֵל וְאָסַפְתָּ אֵלֶיךָ
# וְהָיָה לְךָ וְלָהֶם לְאָכְלָה
# "And take thou unto thee of all food that is eaten, and gather it to thee;
# and it shall be for food for thee, and for them.'"
m.step("Gen.6.21")
# ‹וְאַתָּה קַח־לְךָ מִכָּל־מַאֲכָל אֲשֶׁר יֵאָכֵל› (“and-you take for-
# yourself from-all food which is-eaten”) — God speaks a demand — LET:
# take(Noach, from-all-food)
m.declare("Elohim", "LET",
          "qach(noach, mi_kol_maakhal)")
# ‹וְהָיָה לְךָ וְלָהֶם לְאָכְלָה› (“and-it-shall-be for-yourself and-for-
# them for-food”) — fact holds: and-was-to-you-and-to-them-to-food
m.fact("ve_hayah_lekha_ve_lahem_le_akhlah")

# -------------------------- Gen.6.22 · THE_RECEIPT_BOTH_POPPED -------------
# וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים כֵּן עָשָׂה
# "Thus did Noah; according to all that God commanded him, so did he."
m.step("Gen.6.22")
# ‹וַיַּעַשׂ נֹחַ› (“and-he-made Noach”) — event: make — agent Noach; theme
# ark
m.event("make", agent="noach", themes=["tevah"])
# ‹וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר צִוָּה› (“and-he-made Noach according-to-all
# which commanded”) — the world gains: ark
m.install("tevah")
# ‹כְּכֹל אֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› (“according-to-all which commanded
# him God”) — demand settled (popped from the queue): make(Noach, ark)
m.result("aseh(noach, tevah)", tmark="t2")
# ‹כֵּן עָשָׂה› (“so he-did”) — demand settled (popped from the queue):
# take(Noach, from-all-food)
m.result("qach(noach, mi_kol_maakhal)", tmark="t2")
# witness-tier presupposed read: praise_law_from_an_ink_diff on
# compliance_note — read, not installed
m.witness_read("compliance_note", "praise_law_from_an_ink_diff",
                cites=["Bereshit Rabbah 32:3"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'tevah'}
    assert m.presupposed_set() == {'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['ish_tzaddik_tamim_be_dorotav', 'et_ha_elohim_hithalekh_noach', 'va_timale_ha_aretz_chamas', 'hishchit_kol_basar_et_darko', 'qetz_kol_basar_ba_lefanai', 'hineni_mashchitam_et_ha_aretz', 'tevat_atzei_gofer_qinim', 've_khafarta_ba_kofer', 'shelosh_meot_amah_orekh', 'chamishim_amah_rochbah', 'sheloshim_amah_qomatah', 'tzohar_la_tevah', 'petach_ba_tzidah', 'tachtiyim_shniyim_u_shlishim', 'hineni_mevi_et_ha_mabul_mayim', 'kol_asher_ba_aretz_yigva', 'va_hakimoti_et_briti_itakh', 'u_vata_el_ha_tevah_atah_u_vanekha', 'shnayim_mi_kol_tavi_el_ha_tevah', 'zakhar_u_nekevah_yihyu', 'le_minehu_manifest_of_behemah_remes', 've_hayah_lekha_ve_lahem_le_akhlah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    assert sorted(m.WORLD["witnessed"]) == ['noach_epithets']
    assert m.WORLD["witnessed"]['noach_epithets']["cites"] == ['Bereshit Rabbah 30:9', 'Avodah Zarah 6a:2', 'Bereshit Rabbah 30:10']
    assert all('two_domains_and_disputed_qualifier' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('eleh_header', 'exclusion_particle'), ('chamas_vocabulary', 'threshold_definition_and_capital_list'), ('build_command', 'make_for_yourself_census'), ('ark_dimensions', 'shipwright_ratios_and_disputed_compartments'), ('vessel_spec_delta', 'pitch_regime_compared_to_the_basket'), ('covenant_entry_listing', 'ark_abstinence_from_the_order'), ('intake_roster', 'offering_fitness_standard'), ('compliance_note', 'praise_law_from_an_ink_diff')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 30:3']
    assert all('exclusion_particle' not in f for f in m.WORLD["facts"])
    assert 'eleh_header' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 31:5', 'Bereshit Rabbah 31:6', 'Sanhedrin 57a:1']
    assert all('threshold_definition_and_capital_list' not in f for f in m.WORLD["facts"])
    assert 'chamas_vocabulary' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Jerusalem Talmud Rosh Hashanah 3:9:2']
    assert all('make_for_yourself_census' not in f for f in m.WORLD["facts"])
    assert 'build_command' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 31:10', 'Sanhedrin 108b:10', 'Bereshit Rabbah 31:11', 'Sanhedrin 108b:11']
    assert all('shipwright_ratios_and_disputed_compartments' not in f for f in m.WORLD["facts"])
    assert 'ark_dimensions' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 31:9']
    assert all('pitch_regime_compared_to_the_basket' not in f for f in m.WORLD["facts"])
    assert 'vessel_spec_delta' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 34:7', 'Jerusalem Talmud Taanit 1:6:10']
    assert all('ark_abstinence_from_the_order' not in f for f in m.WORLD["facts"])
    assert 'covenant_entry_listing' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Avodah Zarah 51a:15', 'Avodah Zarah 51a:18', 'Jerusalem Talmud Pesachim 9:5:2', 'Sanhedrin 57a:7']
    assert all('offering_fitness_standard' not in f for f in m.WORLD["facts"])
    assert 'intake_roster' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 32:3']
    assert all('praise_law_from_an_ink_diff' not in f for f in m.WORLD["facts"])
    assert 'compliance_note' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
