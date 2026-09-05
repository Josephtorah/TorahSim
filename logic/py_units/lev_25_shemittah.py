#!/usr/bin/env python3
# =============================================================================
# lev_25_shemittah — 25:1-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_25_shemittah.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Shemittah land rest; six years sow; seventh Sabbath (25:1–22)"""
from machine import Machine

m = Machine("lev_25_shemittah")

# -------------------------- Lev.25.1 · TREE_CLAIM --------------------------
# וידבר יהוה אל משה … בהר סיני לאמר
# "[EN-AID] From top split: LEFT «וידבר יהוה אל משה» / RIGHT «בהר סיני
# לאמר». Derive claim from Hebrew arms. Lev 25:1."
m.step("Lev.25.1")
# witness-tier presupposed read: the_sinai_detail_rule on behar_sinai —
# read, not installed
m.witness_read("behar_sinai", "the_sinai_detail_rule",
                cites=["Sifra, Behar, Section 1 1", "Onkelos Lev 25:1"])

# -------------------------- Lev.25.2 · ETNACHTA_SPLIT ----------------------
# דבר אל בני ישראל ואמרת אלהם כי תבאו אל הארץ אשר אני נתן לכם … ושבתה הארץ
# שבת ליהוה
# "[EN-AID] From top split: LEFT «דבר אל בני ישראל ואמרת אלהם כי תבאו אל
# הארץ אשר אני נתן לכם» / RIGHT «ושבתה הארץ שבת ליהוה». Derive claim from
# Hebrew arms. Lev 25:2."
m.step("Lev.25.2")
# witness-tier presupposed read: onset_conditions_and_timeline on
# ki_tavou_el_haaretz — read, not installed
m.witness_read("ki_tavou_el_haaretz", "onset_conditions_and_timeline",
                cites=["Sifra, Behar, Section 1 2", "Sifra, Behar, Section 1 3", "Onkelos Lev 25:2"])

# -------------------------- Lev.25.3 · ETNACHTA_SPLIT ----------------------
# שש שנים תזרע שדך ושש שנים תזמר כרמך … ואספת את תבואתה
# "[EN-AID] From top split: LEFT «שש שנים תזרע שדך ושש שנים תזמר כרמך» /
# RIGHT «ואספת את תבואתה». Derive claim from Hebrew arms. Lev 25:3."
m.step("Lev.25.3")
# witness-tier presupposed read: six_and_six_with_the_rooting_threshold on
# shesh_shanim_tizra — read, not installed
m.witness_read("shesh_shanim_tizra", "six_and_six_with_the_rooting_threshold",
                cites=["Sifra, Behar, Section 1 7", "Sifra, Behar, Section 1 8", "Sifra, Behar, Section 1 9", "Onkelos Lev 25:3"])

# -------------------------- Lev.25.4 · ETNACHTA_SPLIT ----------------------
# ובשנה השביעת שבת שבתון יהיה לארץ שבת ליהוה … שדך לא תזרע וכרמך לא תזמר
# "[EN-AID] From top split: LEFT «ובשנה השביעת שבת שבתון יהיה לארץ שבת
# ליהוה» / RIGHT «שדך לא תזרע וכרמך לא תזמר». Derive claim from Hebrew arms.
# Lev 25:4."
m.step("Lev.25.4")
# witness-tier presupposed read: labor_census_and_the_class_rule on
# shabbat_shabbaton_laaretz — read, not installed
m.witness_read("shabbat_shabbaton_laaretz", "labor_census_and_the_class_rule",
                cites=["Sifra, Behar, Section 1 4", "Sifra, Behar, Section 1 5", "Sifra, Behar, Section 1 6", "Sifra, Behar, Chapter 1 1", "Sifra, Behar, Chapter 1 2", "Onkelos Lev 25:4"])
# witness-tier presupposed read: labor_census_layer_label on
# sadekha_lo_tizra — read, not installed
m.witness_read("sadekha_lo_tizra", "labor_census_layer_label",
                cites=["Babylonian Talmud Moed Katan 3a:2", "Babylonian Talmud Moed Katan 3a:3", "Babylonian Talmud Moed Katan 3a:9", "Babylonian Talmud Moed Katan 3a:11", "Babylonian Talmud Moed Katan 3a:12", "Babylonian Talmud Moed Katan 3a:16", "Babylonian Talmud Moed Katan 3a:22", "Babylonian Talmud Moed Katan 3b:5", "Babylonian Talmud Moed Katan 3b:8", "Babylonian Talmud Moed Katan 3b:10", "Babylonian Talmud Moed Katan 3b:11", "Babylonian Talmud Moed Katan 3b:12", "Babylonian Talmud Moed Katan 3b:13", "Babylonian Talmud Moed Katan 4a:1", "Babylonian Talmud Moed Katan 4a:2", "Babylonian Talmud Moed Katan 4a:7", "Babylonian Talmud Moed Katan 4a:9", "Mishnah Sheviit 1:1", "Mishnah Sheviit 1:6", "Mishnah Sheviit 2:1", "Mishnah Sheviit 2:6"])

# -------------------------- Lev.25.5 · ETNACHTA_SPLIT ----------------------
# את ספיח קצירך לא תקצור ואת ענבי נזירך לא תבצר … שנת שבתון יהיה לארץ
# "[EN-AID] From top split: LEFT «את ספיח קצירך לא תקצור ואת ענבי נזירך לא
# תבצר» / RIGHT «שנת שבתון יהיה לארץ». Derive claim from Hebrew arms. Lev
# 25:5."
m.step("Lev.25.5")
# witness-tier presupposed read: changed_manner_rule_and_two_clocks on
# sefiach_ketzircha — read, not installed
m.witness_read("sefiach_ketzircha", "changed_manner_rule_and_two_clocks",
                cites=["Sifra, Behar, Chapter 1 3", "Sifra, Behar, Chapter 1 4", "Onkelos Lev 25:5"])

# -------------------------- Lev.25.6 · ETNACHTA_SPLIT ----------------------
# והיתה שבת הארץ לכם לאכלה לך ולעבדך ולאמתך … ולשכירך ולתושבך הגרים עמך
# "[EN-AID] From top split: LEFT «והיתה שבת הארץ לכם לאכלה לך ולעבדך ולאמתך»
# / RIGHT «ולשכירך ולתושבך הגרים עמך». Derive claim from Hebrew arms. Lev
# 25:6."
m.step("Lev.25.6")
# witness-tier presupposed read: the_eaters_and_the_removal_dispute on
# vehaytah_shabbat_haaretz_lachem — read, not installed
m.witness_read("vehaytah_shabbat_haaretz_lachem", "the_eaters_and_the_removal_dispute",
                cites=["Sifra, Behar, Chapter 1 5", "Sifra, Behar, Chapter 1 6", "Sifra, Behar, Chapter 1 7", "Onkelos Lev 25:6"])

# -------------------------- Lev.25.7 · ETNACHTA_SPLIT ----------------------
# ולבהמתך ולחיה אשר בארצך … תהיה כל תבואתה לאכל
# "[EN-AID] From top split: LEFT «ולבהמתך ולחיה אשר בארצך» / RIGHT «תהיה כל
# תבואתה לאכל». Derive claim from Hebrew arms. Lev 25:7."
m.step("Lev.25.7")
# witness-tier presupposed read: the_field_clock_and_the_season_table on
# velivhemtecha_velachayah — read, not installed
m.witness_read("velivhemtecha_velachayah", "the_field_clock_and_the_season_table",
                cites=["Sifra, Behar, Chapter 1 8", "Sifra, Behar, Chapter 1 9", "Sifra, Behar, Chapter 1 10", "Sifra, Behar, Chapter 1 11", "Onkelos Lev 25:7"])

# -------------------------- Lev.25.8 · ETNACHTA_SPLIT ----------------------
# וספרת לך שבע שבתת שנים שבע שנים שבע פעמים … והיו לך ימי שבע שבתת השנים תשע
# וארבעים שנה
# "[EN-AID] From top split: LEFT «וספרת לך שבע שבתת שנים שבע שנים שבע פעמים»
# / RIGHT «והיו לך ימי שבע שבתת השנים תשע וארבעים שנה». Derive claim from
# Hebrew arms. Lev 25:8."
m.step("Lev.25.8")
# witness-tier presupposed read:
# the_count_in_the_court_and_the_dependency_dispute on vesafarta_lecha —
# read, not installed
m.witness_read("vesafarta_lecha", "the_count_in_the_court_and_the_dependency_dispute",
                cites=["Sifra, Behar, Section 2 1", "Sifra, Behar, Section 2 2", "Onkelos Lev 25:8"])
# witness-tier presupposed read: seventeen_jubilees_cycle_year on
# sheva_shabtot_shanim — read, not installed
m.witness_read("sheva_shabtot_shanim", "seventeen_jubilees_cycle_year",
                cites=["Babylonian Talmud Arakhin 12b:3", "Babylonian Talmud Arakhin 12b:4", "Babylonian Talmud Arakhin 12b:5", "Babylonian Talmud Arakhin 12b:6", "Babylonian Talmud Arakhin 12b:7", "Babylonian Talmud Arakhin 12b:8", "Babylonian Talmud Arakhin 13a:2", "Babylonian Talmud Arakhin 13a:3", "Babylonian Talmud Arakhin 13a:4", "Babylonian Talmud Arakhin 13a:5", "Babylonian Talmud Arakhin 13a:6", "Babylonian Talmud Arakhin 13a:7", "Babylonian Talmud Arakhin 13a:8"])

# -------------------------- Lev.25.9 · ETNACHTA_SPLIT ----------------------
# והעברת שופר תרועה בחדש השבעי בעשור לחדש … ביום הכפרים תעבירו שופר בכל
# ארצכם
# "[EN-AID] From top split: LEFT «והעברת שופר תרועה בחדש השבעי בעשור לחדש» /
# RIGHT «ביום הכפרים תעבירו שופר בכל ארצכם». Derive claim from Hebrew arms.
# Lev 25:9."
m.step("Lev.25.9")
# witness-tier presupposed read: the_shofar_export on
# vehaavarta_shofar_teruah — read, not installed
m.witness_read("vehaavarta_shofar_teruah", "the_shofar_export",
                cites=["Sifra, Behar, Section 2 3", "Sifra, Behar, Section 2 4", "Sifra, Behar, Section 2 5", "Onkelos Lev 25:9"])

# -------------------------- Lev.25.10 · ETNACHTA_SPLIT ---------------------
# וקדשתם את שנת החמשים שנה וקראתם דרור בארץ לכל ישביה … יובל הוא תהיה לכם
# ושבתם איש אל אחזתו ואיש אל משפחתו תשבו
# "[EN-AID] From top split: LEFT «וקדשתם את שנת החמשים שנה וקראתם דרור בארץ
# לכל ישביה» / RIGHT «יובל הוא תהיה לכם ושבתם איש אל אחזתו ואיש אל משפחתו
# תשבו». Derive claim from Hebrew arms. Lev 25:10."
m.step("Lev.25.10")
# witness-tier presupposed read: the_ten_day_window_and_the_jubilees_gates
# on vekidashtem_ukratem_deror — read, not installed
m.witness_read("vekidashtem_ukratem_deror", "the_ten_day_window_and_the_jubilees_gates",
                cites=["Sifra, Behar, Chapter 2 1", "Sifra, Behar, Chapter 2 2", "Sifra, Behar, Chapter 2 3", "Sifra, Behar, Chapter 2 4", "Sifra, Behar, Chapter 2 5", "Onkelos Lev 25:10"])

# -------------------------- Lev.25.11 · ETNACHTA_SPLIT ---------------------
# יובל הוא שנת החמשים שנה תהיה לכם … לא תזרעו ולא תקצרו את ספיחיה ולא תבצרו
# את נזריה
# "[EN-AID] From top split: LEFT «יובל הוא שנת החמשים שנה תהיה לכם» / RIGHT
# «לא תזרעו ולא תקצרו את ספיחיה ולא תבצרו את נזריה». Derive claim from
# Hebrew arms. Lev 25:11."
m.step("Lev.25.11")
# witness-tier presupposed read: the_timers_end_and_the_imported_ban on
# yovel_hi_shnat_hachamishim — read, not installed
m.witness_read("yovel_hi_shnat_hachamishim", "the_timers_end_and_the_imported_ban",
                cites=["Sifra, Behar, Chapter 3 1", "Sifra, Behar, Chapter 3 2", "Onkelos Lev 25:11"])

# -------------------------- Lev.25.12 · COND_כי ----------------------------
# כי יובל הוא קדש תהיה לכם … מן השדה תאכלו את תבואתה
# "[EN-AID] From top split: LEFT «כי יובל הוא קדש תהיה לכם» / RIGHT «מן השדה
# תאכלו את תבואתה». Derive claim from Hebrew arms. Lev 25:12."
m.step("Lev.25.12")
# witness-tier presupposed read: the_substitution_chain_and_the_jar_dispute
# on ki_yovel_hi_kodesh — read, not installed
m.witness_read("ki_yovel_hi_kodesh", "the_substitution_chain_and_the_jar_dispute",
                cites=["Sifra, Behar, Chapter 3 3", "Sifra, Behar, Chapter 3 4", "Sifra, Behar, Chapter 3 5", "Onkelos Lev 25:12"])

# -------------------------- Lev.25.13 · ETNACHTA_SPLIT ---------------------
# בשנת היובל הזאת … תשבו איש אל אחזתו
# "[EN-AID] From top split: LEFT «בשנת היובל הזאת» / RIGHT «תשבו איש אל
# אחזתו». Derive claim from Hebrew arms. Lev 25:13."
m.step("Lev.25.13")
# witness-tier presupposed read: the_two_releases_matrix on
# bishnat_hayovel_hazot — read, not installed
m.witness_read("bishnat_hayovel_hazot", "the_two_releases_matrix",
                cites=["Sifra, Behar, Chapter 3 6", "Onkelos Lev 25:13"])

# -------------------------- Lev.25.14 · COND_וכי ---------------------------
# וכי תמכרו ממכר לעמיתך או קנה מיד עמיתך … אל תונו איש את אחיו
# "[EN-AID] From top split: LEFT «וכי תמכרו ממכר לעמיתך או קנה מיד עמיתך» /
# RIGHT «אל תונו איש את אחיו». Derive claim from Hebrew arms. Lev 25:14."
m.step("Lev.25.14")
# witness-tier presupposed read: the_overreaching_file on
# al_tonu_ish_et_achiv — read, not installed
m.witness_read("al_tonu_ish_et_achiv", "the_overreaching_file",
                cites=["Sifra, Behar, Section 3 1", "Sifra, Behar, Section 3 2", "Sifra, Behar, Section 3 3", "Sifra, Behar, Section 3 4", "Sifra, Behar, Section 3 5", "Sifra, Behar, Section 3 6", "Sifra, Behar, Section 3 7", "Sifra, Behar, Section 3 8", "Sifra, Behar, Section 3 9", "Onkelos Lev 25:14"])

# -------------------------- Lev.25.15 · ETNACHTA_SPLIT ---------------------
# במספר שנים אחר היובל תקנה מאת עמיתך … במספר שני תבואת ימכר לך
# "[EN-AID] From top split: LEFT «במספר שנים אחר היובל תקנה מאת עמיתך» /
# RIGHT «במספר שני תבואת ימכר לך». Derive claim from Hebrew arms. Lev
# 25:15."
m.step("Lev.25.15")
# witness-tier presupposed read: the_two_year_floor on
# bemispar_shanim_achar_hayovel — read, not installed
m.witness_read("bemispar_shanim_achar_hayovel", "the_two_year_floor",
                cites=["Sifra, Behar, Section 3 10", "Onkelos Lev 25:15"])

# -------------------------- Lev.25.16 · ETNACHTA_SPLIT ---------------------
# לפי רב השנים תרבה מקנתו ולפי מעט השנים תמעיט מקנתו … כי מספר תבואת הוא מכר
# לך
# "[EN-AID] From top split: LEFT «לפי רב השנים תרבה מקנתו ולפי מעט השנים
# תמעיט מקנתו» / RIGHT «כי מספר תבואת הוא מכר לך». Derive claim from Hebrew
# arms. Lev 25:16."
m.step("Lev.25.16")

# -------------------------- Lev.25.17 · ETNACHTA_SPLIT ---------------------
# ולא תונו איש את עמיתו ויראת מאלהיך … כי אני יהוה אלהיכם
# "[EN-AID] From top split: LEFT «ולא תונו איש את עמיתו ויראת מאלהיך» /
# RIGHT «כי אני יהוה אלהיכם». Derive claim from Hebrew arms. Lev 25:17."
m.step("Lev.25.17")
# witness-tier presupposed read: verbal_wronging_and_the_heart_clause_rule
# on velo_tonu_ish_et_amito — read, not installed
m.witness_read("velo_tonu_ish_et_amito", "verbal_wronging_and_the_heart_clause_rule",
                cites=["Sifra, Behar, Chapter 4 1", "Sifra, Behar, Chapter 4 2", "Onkelos Lev 25:17"])

# -------------------------- Lev.25.18 · ETNACHTA_SPLIT ---------------------
# ועשיתם את חקתי ואת משפטי תשמרו ועשיתם אתם … וישבתם על הארץ לבטח
# "[EN-AID] From top split: LEFT «ועשיתם את חקתי ואת משפטי תשמרו ועשיתם אתם»
# / RIGHT «וישבתם על הארץ לבטח». Derive claim from Hebrew arms. Lev 25:18."
m.step("Lev.25.18")

# -------------------------- Lev.25.19 · ETNACHTA_SPLIT ---------------------
# ונתנה הארץ פריה ואכלתם לשבע … וישבתם לבטח עליה
# "[EN-AID] From top split: LEFT «ונתנה הארץ פריה ואכלתם לשבע» / RIGHT
# «וישבתם לבטח עליה». Derive claim from Hebrew arms. Lev 25:19."
m.step("Lev.25.19")

# -------------------------- Lev.25.20 · COND_וכי ---------------------------
# וכי תאמרו מה נאכל בשנה השביעת … הן לא נזרע ולא נאסף את תבואתנו
# "[EN-AID] From top split: LEFT «וכי תאמרו מה נאכל בשנה השביעת» / RIGHT «הן
# לא נזרע ולא נאסף את תבואתנו». Derive claim from Hebrew arms. Lev 25:20."
m.step("Lev.25.20")
# witness-tier presupposed read: the_aftergrowth_bans_provenance on
# mah_nochal_bashanah_hasheviit — read, not installed
m.witness_read("mah_nochal_bashanah_hasheviit", "the_aftergrowth_bans_provenance",
                cites=["Sifra, Behar, Chapter 4 5", "Onkelos Lev 25:20"])

# -------------------------- Lev.25.21 · ETNACHTA_SPLIT ---------------------
# וצויתי את ברכתי לכם בשנה הששית … ועשת את התבואה לשלש השנים
# "[EN-AID] From top split: LEFT «וצויתי את ברכתי לכם בשנה הששית» / RIGHT
# «ועשת את התבואה לשלש השנים». Derive claim from Hebrew arms. Lev 25:21."
m.step("Lev.25.21")
# witness-tier presupposed read:
# the_blessings_arithmetic_and_the_year_ladder on vetzivviti_et_birchati —
# read, not installed
m.witness_read("vetzivviti_et_birchati", "the_blessings_arithmetic_and_the_year_ladder",
                cites=["Sifra, Behar, Chapter 4 6", "Sifra, Behar, Chapter 4 7", "Onkelos Lev 25:21", "Onkelos Lev 25:22"])

# -------------------------- Lev.25.22 · ETNACHTA_SPLIT ---------------------
# וזרעתם את השנה השמינת ואכלתם מן התבואה ישן … עד השנה התשיעת עד בוא תבואתה
# תאכלו ישן
# "[EN-AID] From top split: LEFT «וזרעתם את השנה השמינת ואכלתם מן התבואה
# ישן» / RIGHT «עד השנה התשיעת עד בוא תבואתה תאכלו ישן». Derive claim from
# Hebrew arms. Lev 25:22."
m.step("Lev.25.22")

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
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 0
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('behar_sinai', 'the_sinai_detail_rule'), ('ki_tavou_el_haaretz', 'onset_conditions_and_timeline'), ('shesh_shanim_tizra', 'six_and_six_with_the_rooting_threshold'), ('shabbat_shabbaton_laaretz', 'labor_census_and_the_class_rule'), ('sadekha_lo_tizra', 'labor_census_layer_label'), ('sefiach_ketzircha', 'changed_manner_rule_and_two_clocks'), ('vehaytah_shabbat_haaretz_lachem', 'the_eaters_and_the_removal_dispute'), ('velivhemtecha_velachayah', 'the_field_clock_and_the_season_table'), ('vesafarta_lecha', 'the_count_in_the_court_and_the_dependency_dispute'), ('sheva_shabtot_shanim', 'seventeen_jubilees_cycle_year'), ('vehaavarta_shofar_teruah', 'the_shofar_export'), ('vekidashtem_ukratem_deror', 'the_ten_day_window_and_the_jubilees_gates'), ('yovel_hi_shnat_hachamishim', 'the_timers_end_and_the_imported_ban'), ('ki_yovel_hi_kodesh', 'the_substitution_chain_and_the_jar_dispute'), ('bishnat_hayovel_hazot', 'the_two_releases_matrix'), ('al_tonu_ish_et_achiv', 'the_overreaching_file'), ('bemispar_shanim_achar_hayovel', 'the_two_year_floor'), ('velo_tonu_ish_et_amito', 'verbal_wronging_and_the_heart_clause_rule'), ('mah_nochal_bashanah_hasheviit', 'the_aftergrowth_bans_provenance'), ('vetzivviti_et_birchati', 'the_blessings_arithmetic_and_the_year_ladder')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Behar, Section 1 1', 'Onkelos Lev 25:1']
    assert all('the_sinai_detail_rule' not in f for f in m.WORLD["facts"])
    assert 'behar_sinai' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Behar, Section 1 2', 'Sifra, Behar, Section 1 3', 'Onkelos Lev 25:2']
    assert all('onset_conditions_and_timeline' not in f for f in m.WORLD["facts"])
    assert 'ki_tavou_el_haaretz' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Behar, Section 1 7', 'Sifra, Behar, Section 1 8', 'Sifra, Behar, Section 1 9', 'Onkelos Lev 25:3']
    assert all('six_and_six_with_the_rooting_threshold' not in f for f in m.WORLD["facts"])
    assert 'shesh_shanim_tizra' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Behar, Section 1 4', 'Sifra, Behar, Section 1 5', 'Sifra, Behar, Section 1 6', 'Sifra, Behar, Chapter 1 1', 'Sifra, Behar, Chapter 1 2', 'Onkelos Lev 25:4']
    assert all('labor_census_and_the_class_rule' not in f for f in m.WORLD["facts"])
    assert 'shabbat_shabbaton_laaretz' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Babylonian Talmud Moed Katan 3a:2', 'Babylonian Talmud Moed Katan 3a:3', 'Babylonian Talmud Moed Katan 3a:9', 'Babylonian Talmud Moed Katan 3a:11', 'Babylonian Talmud Moed Katan 3a:12', 'Babylonian Talmud Moed Katan 3a:16', 'Babylonian Talmud Moed Katan 3a:22', 'Babylonian Talmud Moed Katan 3b:5', 'Babylonian Talmud Moed Katan 3b:8', 'Babylonian Talmud Moed Katan 3b:10', 'Babylonian Talmud Moed Katan 3b:11', 'Babylonian Talmud Moed Katan 3b:12', 'Babylonian Talmud Moed Katan 3b:13', 'Babylonian Talmud Moed Katan 4a:1', 'Babylonian Talmud Moed Katan 4a:2', 'Babylonian Talmud Moed Katan 4a:7', 'Babylonian Talmud Moed Katan 4a:9', 'Mishnah Sheviit 1:1', 'Mishnah Sheviit 1:6', 'Mishnah Sheviit 2:1', 'Mishnah Sheviit 2:6']
    assert all('labor_census_layer_label' not in f for f in m.WORLD["facts"])
    assert 'sadekha_lo_tizra' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Behar, Chapter 1 3', 'Sifra, Behar, Chapter 1 4', 'Onkelos Lev 25:5']
    assert all('changed_manner_rule_and_two_clocks' not in f for f in m.WORLD["facts"])
    assert 'sefiach_ketzircha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Behar, Chapter 1 5', 'Sifra, Behar, Chapter 1 6', 'Sifra, Behar, Chapter 1 7', 'Onkelos Lev 25:6']
    assert all('the_eaters_and_the_removal_dispute' not in f for f in m.WORLD["facts"])
    assert 'vehaytah_shabbat_haaretz_lachem' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Behar, Chapter 1 8', 'Sifra, Behar, Chapter 1 9', 'Sifra, Behar, Chapter 1 10', 'Sifra, Behar, Chapter 1 11', 'Onkelos Lev 25:7']
    assert all('the_field_clock_and_the_season_table' not in f for f in m.WORLD["facts"])
    assert 'velivhemtecha_velachayah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Behar, Section 2 1', 'Sifra, Behar, Section 2 2', 'Onkelos Lev 25:8']
    assert all('the_count_in_the_court_and_the_dependency_dispute' not in f for f in m.WORLD["facts"])
    assert 'vesafarta_lecha' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Babylonian Talmud Arakhin 12b:3', 'Babylonian Talmud Arakhin 12b:4', 'Babylonian Talmud Arakhin 12b:5', 'Babylonian Talmud Arakhin 12b:6', 'Babylonian Talmud Arakhin 12b:7', 'Babylonian Talmud Arakhin 12b:8', 'Babylonian Talmud Arakhin 13a:2', 'Babylonian Talmud Arakhin 13a:3', 'Babylonian Talmud Arakhin 13a:4', 'Babylonian Talmud Arakhin 13a:5', 'Babylonian Talmud Arakhin 13a:6', 'Babylonian Talmud Arakhin 13a:7', 'Babylonian Talmud Arakhin 13a:8']
    assert all('seventeen_jubilees_cycle_year' not in f for f in m.WORLD["facts"])
    assert 'sheva_shabtot_shanim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Sifra, Behar, Section 2 3', 'Sifra, Behar, Section 2 4', 'Sifra, Behar, Section 2 5', 'Onkelos Lev 25:9']
    assert all('the_shofar_export' not in f for f in m.WORLD["facts"])
    assert 'vehaavarta_shofar_teruah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Sifra, Behar, Chapter 2 1', 'Sifra, Behar, Chapter 2 2', 'Sifra, Behar, Chapter 2 3', 'Sifra, Behar, Chapter 2 4', 'Sifra, Behar, Chapter 2 5', 'Onkelos Lev 25:10']
    assert all('the_ten_day_window_and_the_jubilees_gates' not in f for f in m.WORLD["facts"])
    assert 'vekidashtem_ukratem_deror' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Sifra, Behar, Chapter 3 1', 'Sifra, Behar, Chapter 3 2', 'Onkelos Lev 25:11']
    assert all('the_timers_end_and_the_imported_ban' not in f for f in m.WORLD["facts"])
    assert 'yovel_hi_shnat_hachamishim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Sifra, Behar, Chapter 3 3', 'Sifra, Behar, Chapter 3 4', 'Sifra, Behar, Chapter 3 5', 'Onkelos Lev 25:12']
    assert all('the_substitution_chain_and_the_jar_dispute' not in f for f in m.WORLD["facts"])
    assert 'ki_yovel_hi_kodesh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Sifra, Behar, Chapter 3 6', 'Onkelos Lev 25:13']
    assert all('the_two_releases_matrix' not in f for f in m.WORLD["facts"])
    assert 'bishnat_hayovel_hazot' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[15]["cites"] == ['Sifra, Behar, Section 3 1', 'Sifra, Behar, Section 3 2', 'Sifra, Behar, Section 3 3', 'Sifra, Behar, Section 3 4', 'Sifra, Behar, Section 3 5', 'Sifra, Behar, Section 3 6', 'Sifra, Behar, Section 3 7', 'Sifra, Behar, Section 3 8', 'Sifra, Behar, Section 3 9', 'Onkelos Lev 25:14']
    assert all('the_overreaching_file' not in f for f in m.WORLD["facts"])
    assert 'al_tonu_ish_et_achiv' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[16]["cites"] == ['Sifra, Behar, Section 3 10', 'Onkelos Lev 25:15']
    assert all('the_two_year_floor' not in f for f in m.WORLD["facts"])
    assert 'bemispar_shanim_achar_hayovel' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[17]["cites"] == ['Sifra, Behar, Chapter 4 1', 'Sifra, Behar, Chapter 4 2', 'Onkelos Lev 25:17']
    assert all('verbal_wronging_and_the_heart_clause_rule' not in f for f in m.WORLD["facts"])
    assert 'velo_tonu_ish_et_amito' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[18]["cites"] == ['Sifra, Behar, Chapter 4 5', 'Onkelos Lev 25:20']
    assert all('the_aftergrowth_bans_provenance' not in f for f in m.WORLD["facts"])
    assert 'mah_nochal_bashanah_hasheviit' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[19]["cites"] == ['Sifra, Behar, Chapter 4 6', 'Sifra, Behar, Chapter 4 7', 'Onkelos Lev 25:21', 'Onkelos Lev 25:22']
    assert all('the_blessings_arithmetic_and_the_year_ladder' not in f for f in m.WORLD["facts"])
    assert 'vetzivviti_et_birchati' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
