#!/usr/bin/env python3
# =============================================================================
# lev_25_redeem_poor — 25:23-38
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_25_redeem_poor.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Land not sold forever; redeem; poor brother interest ban (25:23–38)"""
from machine import Machine

m = Machine("lev_25_redeem_poor")

# -------------------------- Lev.25.23 · ETNACHTA_SPLIT ---------------------
# והארץ לא תמכר לצמתת כי לי הארץ … כי גרים ותושבים אתם עמדי
# "[EN-AID] From top split: LEFT «והארץ לא תמכר לצמתת כי לי הארץ» / RIGHT
# «כי גרים ותושבים אתם עמדי». Derive claim from Hebrew arms. Lev 25:23."
m.step("Lev.25.23")
# witness-tier presupposed read: irrevocably_and_the_strangers_clause on
# vehaaretz_lo_timacher_litzmitut — read, not installed
m.witness_read("vehaaretz_lo_timacher_litzmitut", "irrevocably_and_the_strangers_clause",
                cites=["Sifra, Behar, Chapter 4 8", "Onkelos Lev 25:23"])

# -------------------------- Lev.25.24 · ETNACHTA_SPLIT ---------------------
# ובכל ארץ אחזתכם … גאלה תתנו לארץ
# "[EN-AID] From top split: LEFT «ובכל ארץ אחזתכם» / RIGHT «גאלה תתנו לארץ».
# Derive claim from Hebrew arms. Lev 25:24."
m.step("Lev.25.24")
# witness-tier presupposed read: the_redemption_domain on
# geulah_titnu_laaretz — read, not installed
m.witness_read("geulah_titnu_laaretz", "the_redemption_domain",
                cites=["Sifra, Behar, Chapter 4 9", "Onkelos Lev 25:24"])

# -------------------------- Lev.25.25 · COND_כי ----------------------------
# כי ימוך אחיך ומכר מאחזתו … ובא גאלו הקרב אליו וגאל את ממכר אחיו
# "[EN-AID] From top split: LEFT «כי ימוך אחיך ומכר מאחזתו» / RIGHT «ובא
# גאלו הקרב אליו וגאל את ממכר אחיו». Derive claim from Hebrew arms. Lev
# 25:25."
m.step("Lev.25.25")
# witness-tier presupposed read: the_sale_gate_and_nearest_first on
# ki_yamuch_achicha_umachar — read, not installed
m.witness_read("ki_yamuch_achicha_umachar", "the_sale_gate_and_nearest_first",
                cites=["Sifra, Behar, Chapter 5 1", "Onkelos Lev 25:25"])

# -------------------------- Lev.25.26 · COND_כי ----------------------------
# ואיש כי לא יהיה לו גאל … והשיגה ידו ומצא כדי גאלתו
# "[EN-AID] From top split: LEFT «ואיש כי לא יהיה לו גאל» / RIGHT «והשיגה
# ידו ומצא כדי גאלתו». Derive claim from Hebrew arms. Lev 25:26."
m.step("Lev.25.26")
# witness-tier presupposed read: the_four_constraints on
# vehisigah_yado_umatza — read, not installed
m.witness_read("vehisigah_yado_umatza", "the_four_constraints",
                cites=["Sifra, Behar, Chapter 5 2", "Onkelos Lev 25:26"])

# -------------------------- Lev.25.27 · ETNACHTA_SPLIT ---------------------
# וחשב את שני ממכרו והשיב את העדף לאיש אשר מכר לו … ושב לאחזתו
# "[EN-AID] From top split: LEFT «וחשב את שני ממכרו והשיב את העדף לאיש אשר
# מכר לו» / RIGHT «ושב לאחזתו». Derive claim from Hebrew arms. Lev 25:27."
m.step("Lev.25.27")
# witness-tier presupposed read:
# the_reckoning_counterpart_and_the_lesser_figure on
# vechishav_et_shnei_mimkaro — read, not installed
m.witness_read("vechishav_et_shnei_mimkaro", "the_reckoning_counterpart_and_the_lesser_figure",
                cites=["Sifra, Behar, Chapter 5 3", "Sifra, Behar, Chapter 5 4", "Onkelos Lev 25:27"])

# -------------------------- Lev.25.28 · COND_ואם ---------------------------
# ואם לא מצאה ידו די השיב לו והיה ממכרו ביד הקנה אתו עד שנת הי … ויצא ביבל
# ושב לאחזתו
# "[EN-AID] From top split: LEFT «ואם לא מצאה ידו די השיב לו והיה ממכרו ביד
# הקנה אתו עד שנת היובל» / RIGHT «ויצא ביבל ושב לאחזתו». Derive claim from
# Hebrew arms. Lev 25:28."
m.step("Lev.25.28")
# witness-tier presupposed read:
# the_sanctuarys_inversion_and_fields_with_money on
# vehayah_mimkaro_beyad_hakoneh — read, not installed
m.witness_read("vehayah_mimkaro_beyad_hakoneh", "the_sanctuarys_inversion_and_fields_with_money",
                cites=["Sifra, Behar, Chapter 5 5", "Sifra, Behar, Chapter 5 6", "Sifra, Behar, Chapter 5 7", "Onkelos Lev 25:28"])

# -------------------------- Lev.25.29 · COND_כי ----------------------------
# ואיש כי ימכר בית מושב עיר חומה והיתה גאלתו עד תם שנת ממכרו … ימים תהיה
# גאלתו
# "[EN-AID] From top split: LEFT «ואיש כי ימכר בית מושב עיר חומה והיתה גאלתו
# עד תם שנת ממכרו» / RIGHT «ימים תהיה גאלתו». Derive claim from Hebrew arms.
# Lev 25:29."
m.step("Lev.25.29")
# witness-tier presupposed read: the_walled_city_roster on
# beit_moshav_ir_chomah — read, not installed
m.witness_read("beit_moshav_ir_chomah", "the_walled_city_roster",
                cites=["Sifra, Behar, Section 4 1", "Sifra, Behar, Section 4 2", "Sifra, Behar, Section 4 3", "Onkelos Lev 25:29"])

# -------------------------- Lev.25.30 · COND_ואם ---------------------------
# ואם לא יגאל עד מלאת לו שנה תמימה וקם הבית אשר בעיר אשר לא לו … לא יצא ביבל
# "[EN-AID] From top split: LEFT «ואם לא יגאל עד מלאת לו שנה תמימה וקם הבית
# אשר בעיר אשר לא לו חמה לצמיתת לקנה אתו» / RIGHT «לא יצא ביבל». Derive
# claim from Hebrew arms. Lev 25:30."
m.step("Lev.25.30")
# witness-tier presupposed read: the_full_year_and_hillels_ordinance on
# shanah_temimah_vekam_habayit — read, not installed
m.witness_read("shanah_temimah_vekam_habayit", "the_full_year_and_hillels_ordinance",
                cites=["Sifra, Behar, Section 4 4", "Sifra, Behar, Section 4 5", "Sifra, Behar, Section 4 6", "Sifra, Behar, Section 4 7", "Sifra, Behar, Section 4 8", "Sifra, Behar, Section 4 9", "Sifra, Behar, Section 4 10", "Onkelos Lev 25:30"])

# -------------------------- Lev.25.31 · ETNACHTA_SPLIT ---------------------
# ובתי החצרים אשר אין להם חמה סביב על שדה הארץ יחשב … גאלה תהיה לו וביבל יצא
# "[EN-AID] From top split: LEFT «ובתי החצרים אשר אין להם חמה סביב על שדה
# הארץ יחשב» / RIGHT «גאלה תהיה לו וביבל יצא». Derive claim from Hebrew
# arms. Lev 25:31."
m.step("Lev.25.31")
# witness-tier presupposed read: the_village_threshold_and_best_of_both on
# batei_hachatzerim — read, not installed
m.witness_read("batei_hachatzerim", "the_village_threshold_and_best_of_both",
                cites=["Sifra, Behar, Chapter 6 1", "Sifra, Behar, Chapter 6 2", "Sifra, Behar, Chapter 6 3", "Onkelos Lev 25:31"])

# -------------------------- Lev.25.32 · ETNACHTA_SPLIT ---------------------
# וערי הלוים בתי ערי אחזתם … גאלת עולם תהיה ללוים
# "[EN-AID] From top split: LEFT «וערי הלוים בתי ערי אחזתם» / RIGHT «גאלת
# עולם תהיה ללוים». Derive claim from Hebrew arms. Lev 25:32."
m.step("Lev.25.32")
# witness-tier presupposed read: the_levites_three_exemptions on
# geulat_olam_laleviim — read, not installed
m.witness_read("geulat_olam_laleviim", "the_levites_three_exemptions",
                cites=["Sifra, Behar, Chapter 6 4", "Sifra, Behar, Chapter 6 5", "Onkelos Lev 25:32"])

# -------------------------- Lev.25.33 · ETNACHTA_SPLIT ---------------------
# ואשר יגאל מן הלוים ויצא ממכר בית ועיר אחזתו ביבל … כי בתי ערי הלוים הוא
# אחזתם בתוך בני ישראל
# "[EN-AID] From top split: LEFT «ואשר יגאל מן הלוים ויצא ממכר בית ועיר
# אחזתו ביבל» / RIGHT «כי בתי ערי הלוים הוא אחזתם בתוך בני ישראל». Derive
# claim from Hebrew arms. Lev 25:33."
m.step("Lev.25.33")
# witness-tier presupposed read: levite_from_levite_and_the_exclusions on
# vaasher_yigal_min_haleviim — read, not installed
m.witness_read("vaasher_yigal_min_haleviim", "levite_from_levite_and_the_exclusions",
                cites=["Sifra, Behar, Chapter 6 6", "Sifra, Behar, Chapter 6 7", "Sifra, Behar, Chapter 6 8", "Onkelos Lev 25:33"])

# -------------------------- Lev.25.34 · ETNACHTA_SPLIT ---------------------
# ושדה מגרש עריהם לא ימכר … כי אחזת עולם הוא להם
# "[EN-AID] From top split: LEFT «ושדה מגרש עריהם לא ימכר» / RIGHT «כי אחזת
# עולם הוא להם». Derive claim from Hebrew arms. Lev 25:34."
m.step("Lev.25.34")
# witness-tier presupposed read: the_zoning_rule on usdeh_migrash_areihem —
# read, not installed
m.witness_read("usdeh_migrash_areihem", "the_zoning_rule",
                cites=["Sifra, Behar, Chapter 6 9", "Onkelos Lev 25:34"])

# -------------------------- Lev.25.35 · COND_וכי ---------------------------
# וכי ימוך אחיך ומטה ידו עמך … והחזקת בו גר ותושב וחי עמך
# "[EN-AID] From top split: LEFT «וכי ימוך אחיך ומטה ידו עמך» / RIGHT
# «והחזקת בו גר ותושב וחי עמך». Derive claim from Hebrew arms. Lev 25:35."
m.step("Lev.25.35")
# witness-tier presupposed read: the_falling_load on vehechezakta_bo — read,
# not installed
m.witness_read("vehechezakta_bo", "the_falling_load",
                cites=["Sifra, Behar, Section 5 1", "Onkelos Lev 25:35"])

# -------------------------- Lev.25.36 · ETNACHTA_SPLIT ---------------------
# אל תקח מאתו נשך ותרבית ויראת מאלהיך … וחי אחיך עמך
# "[EN-AID] From top split: LEFT «אל תקח מאתו נשך ותרבית ויראת מאלהיך» /
# RIGHT «וחי אחיך עמך». Derive claim from Hebrew arms. Lev 25:36."
m.step("Lev.25.36")
# witness-tier presupposed read: the_interest_definitions_and_the_one_flask
# on neshech_vetarbit — read, not installed
m.witness_read("neshech_vetarbit", "the_interest_definitions_and_the_one_flask",
                cites=["Sifra, Behar, Section 5 2", "Sifra, Behar, Section 5 3", "Onkelos Lev 25:36", "Onkelos Lev 25:37"])

# -------------------------- Lev.25.37 · ETNACHTA_SPLIT ---------------------
# את כספך לא תתן לו בנשך … ובמרבית לא תתן אכלך
# "[EN-AID] From top split: LEFT «את כספך לא תתן לו בנשך» / RIGHT «ובמרבית
# לא תתן אכלך». Derive claim from Hebrew arms. Lev 25:37."
m.step("Lev.25.37")

# -------------------------- Lev.25.38 · ETNACHTA_SPLIT ---------------------
# אני יהוה אלהיכם אשר הוצאתי אתכם מארץ מצרים … לתת לכם את ארץ כנען להיות לכם
# לאלהים
# "[EN-AID] From top split: LEFT «אני יהוה אלהיכם אשר הוצאתי אתכם מארץ
# מצרים» / RIGHT «לתת לכם את ארץ כנען להיות לכם לאלהים». Derive claim from
# Hebrew arms. Lev 25:38."
m.step("Lev.25.38")
# witness-tier presupposed read: the_land_clause_as_status on
# latet_lachem_et_eretz_kenaan — read, not installed
m.witness_read("latet_lachem_et_eretz_kenaan", "the_land_clause_as_status",
                cites=["Sifra, Behar, Section 5 4", "Onkelos Lev 25:38"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('vehaaretz_lo_timacher_litzmitut', 'irrevocably_and_the_strangers_clause'), ('geulah_titnu_laaretz', 'the_redemption_domain'), ('ki_yamuch_achicha_umachar', 'the_sale_gate_and_nearest_first'), ('vehisigah_yado_umatza', 'the_four_constraints'), ('vechishav_et_shnei_mimkaro', 'the_reckoning_counterpart_and_the_lesser_figure'), ('vehayah_mimkaro_beyad_hakoneh', 'the_sanctuarys_inversion_and_fields_with_money'), ('beit_moshav_ir_chomah', 'the_walled_city_roster'), ('shanah_temimah_vekam_habayit', 'the_full_year_and_hillels_ordinance'), ('batei_hachatzerim', 'the_village_threshold_and_best_of_both'), ('geulat_olam_laleviim', 'the_levites_three_exemptions'), ('vaasher_yigal_min_haleviim', 'levite_from_levite_and_the_exclusions'), ('usdeh_migrash_areihem', 'the_zoning_rule'), ('vehechezakta_bo', 'the_falling_load'), ('neshech_vetarbit', 'the_interest_definitions_and_the_one_flask'), ('latet_lachem_et_eretz_kenaan', 'the_land_clause_as_status')]
    assert m.WITNESS_READS[0]["cites"] == ['Sifra, Behar, Chapter 4 8', 'Onkelos Lev 25:23']
    assert all('irrevocably_and_the_strangers_clause' not in f for f in m.WORLD["facts"])
    assert 'vehaaretz_lo_timacher_litzmitut' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Sifra, Behar, Chapter 4 9', 'Onkelos Lev 25:24']
    assert all('the_redemption_domain' not in f for f in m.WORLD["facts"])
    assert 'geulah_titnu_laaretz' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sifra, Behar, Chapter 5 1', 'Onkelos Lev 25:25']
    assert all('the_sale_gate_and_nearest_first' not in f for f in m.WORLD["facts"])
    assert 'ki_yamuch_achicha_umachar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sifra, Behar, Chapter 5 2', 'Onkelos Lev 25:26']
    assert all('the_four_constraints' not in f for f in m.WORLD["facts"])
    assert 'vehisigah_yado_umatza' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Sifra, Behar, Chapter 5 3', 'Sifra, Behar, Chapter 5 4', 'Onkelos Lev 25:27']
    assert all('the_reckoning_counterpart_and_the_lesser_figure' not in f for f in m.WORLD["facts"])
    assert 'vechishav_et_shnei_mimkaro' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Sifra, Behar, Chapter 5 5', 'Sifra, Behar, Chapter 5 6', 'Sifra, Behar, Chapter 5 7', 'Onkelos Lev 25:28']
    assert all('the_sanctuarys_inversion_and_fields_with_money' not in f for f in m.WORLD["facts"])
    assert 'vehayah_mimkaro_beyad_hakoneh' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Sifra, Behar, Section 4 1', 'Sifra, Behar, Section 4 2', 'Sifra, Behar, Section 4 3', 'Onkelos Lev 25:29']
    assert all('the_walled_city_roster' not in f for f in m.WORLD["facts"])
    assert 'beit_moshav_ir_chomah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Sifra, Behar, Section 4 4', 'Sifra, Behar, Section 4 5', 'Sifra, Behar, Section 4 6', 'Sifra, Behar, Section 4 7', 'Sifra, Behar, Section 4 8', 'Sifra, Behar, Section 4 9', 'Sifra, Behar, Section 4 10', 'Onkelos Lev 25:30']
    assert all('the_full_year_and_hillels_ordinance' not in f for f in m.WORLD["facts"])
    assert 'shanah_temimah_vekam_habayit' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sifra, Behar, Chapter 6 1', 'Sifra, Behar, Chapter 6 2', 'Sifra, Behar, Chapter 6 3', 'Onkelos Lev 25:31']
    assert all('the_village_threshold_and_best_of_both' not in f for f in m.WORLD["facts"])
    assert 'batei_hachatzerim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Sifra, Behar, Chapter 6 4', 'Sifra, Behar, Chapter 6 5', 'Onkelos Lev 25:32']
    assert all('the_levites_three_exemptions' not in f for f in m.WORLD["facts"])
    assert 'geulat_olam_laleviim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Sifra, Behar, Chapter 6 6', 'Sifra, Behar, Chapter 6 7', 'Sifra, Behar, Chapter 6 8', 'Onkelos Lev 25:33']
    assert all('levite_from_levite_and_the_exclusions' not in f for f in m.WORLD["facts"])
    assert 'vaasher_yigal_min_haleviim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Sifra, Behar, Chapter 6 9', 'Onkelos Lev 25:34']
    assert all('the_zoning_rule' not in f for f in m.WORLD["facts"])
    assert 'usdeh_migrash_areihem' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Sifra, Behar, Section 5 1', 'Onkelos Lev 25:35']
    assert all('the_falling_load' not in f for f in m.WORLD["facts"])
    assert 'vehechezakta_bo' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[13]["cites"] == ['Sifra, Behar, Section 5 2', 'Sifra, Behar, Section 5 3', 'Onkelos Lev 25:36', 'Onkelos Lev 25:37']
    assert all('the_interest_definitions_and_the_one_flask' not in f for f in m.WORLD["facts"])
    assert 'neshech_vetarbit' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[14]["cites"] == ['Sifra, Behar, Section 5 4', 'Onkelos Lev 25:38']
    assert all('the_land_clause_as_status' not in f for f in m.WORLD["facts"])
    assert 'latet_lachem_et_eretz_kenaan' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
