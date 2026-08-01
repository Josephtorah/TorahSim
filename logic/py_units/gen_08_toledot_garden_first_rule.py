#!/usr/bin/env python3
# =============================================================================
# gen_08_toledot_garden_first_rule — 2:4-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_08_toledot_garden_first_rule.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden I: toledot header, garden, first job, FIRST RULE (2:4-17)"""
from machine import Machine

m = Machine("gen_08_toledot_garden_first_rule")

# -------------------------- Gen.2.4 · SECTION_HEADER -----------------------
# ele toledot ha-shamayim ve-ha-aretz be-hibaram be-yom asot YHWH Elohim
# eretz ve-shamayim
# "These are the generations of the heaven and of the earth when they were
# created, in the day that the LORD God made earth and heaven."
m.step("Gen.2.4")
m.section("toledot", "shamayim", "aretz")
m.time_anchor("be_yom_asot")
m.presupposed("shamayim", "aretz")
m.spec_delta("Elohim (the week's sole agent name, gen_01-07)",
             "YHWH_Elohim (compound: personal name + generic)")

# -------------------------- Gen.2.5 · PRECONDITIONS_LACKS ------------------
# ve-khol siach ha-sadeh terem yihyeh va-aretz ve-khal-esev ha-sadeh terem
# yitzmach ki lo himtir YHWH Elohim al-ha-aretz ve-adam ayin la-avod et-ha-
# adamah
# "No shrub of the field was yet in the earth, and no herb of the field had
# yet sprung up; for the LORD God had not caused it to rain upon the earth,
# and there was not a man to till the ground."
m.step("Gen.2.5")
m.fact("terem(kol_siach_ha_sadeh)",
       "terem(kol_esev_ha_sadeh)",
       "lo_himtir(YHWH_Elohim, al_ha_aretz)",
       "adam_ayin(la_avod_et_ha_adamah)")
m.presupposed("adamah")

# -------------------------- Gen.2.6 · PRECONDITION_IRRIGATION --------------
# ve-ed yaaleh min-ha-aretz ve-hishqah et-kal-pnei-ha-adamah
# "But there went up a mist from the earth, and watered the whole face of
# the ground."
m.step("Gen.2.6")
m.fact("ed_yaaleh_ve_hishqah(kol_pnei_ha_adamah)")

# -------------------------- Gen.2.7 · FORM_BREATHE_BECOME ------------------
# va-yitzer YHWH Elohim et-ha-adam afar min-ha-adamah va-yipach be-apav
# nishmat chayim va-yehi ha-adam le-nefesh chayah
# "Then the LORD God formed man of the dust of the ground, and breathed into
# his nostrils the breath of life; and man became a living soul."
m.step("Gen.2.7")
m.event("form", agent="YHWH_Elohim", themes=["adam"])
m.event("breathe", agent="YHWH_Elohim", themes=["nishmat_chayim"])
m.event("become", themes=["adam", "nefesh_chaya"])
m.install("adam")
m.spec_delta("bara/asah (create/make — the week's build verbs)",
             "yatzar (form — the potter verb, double-yod ktiv)")

# -------------------------- Gen.2.8 · PLANT_PLACE --------------------------
# va-yita YHWH Elohim gan-be-eden mi-qedem va-yasem sham et-ha-adam asher
# yatzar
# "And the LORD God planted a garden eastward, in Eden; and there He put the
# man whom He had formed."
m.step("Gen.2.8")
m.event("plant", agent="YHWH_Elohim", themes=["gan"])
m.event("place", agent="YHWH_Elohim", themes=["adam"])
m.install("gan")
m.presupposed("eden")

# -------------------------- Gen.2.9 · SPROUT_TWO_TREES ---------------------
# va-yatzmach YHWH Elohim min-ha-adamah kol-etz nechmad le-mareh ve-tov le-
# maakhal ve-etz ha-chayim be-tokh ha-gan ve-etz ha-daat tov va-ra
# "And out of the ground made the LORD God to grow every tree that is
# pleasant to the sight, and good for food; the tree of life also in the
# midst of the garden, and the tree of the knowledge of good and evil."
m.step("Gen.2.9")
m.event("sprout", agent="YHWH_Elohim", themes=["kol_etz"])
m.install("etz_ha_chayim", "etz_ha_daat_tov_va_ra")
m.spec_delta("tov as TEST verdict (the week's instrument, days 1-6)",
             "tov as attribute (tov le-maakhal; zahav tov 2:12; daat tov va-ra)")

# -------------------------- Gen.2.10 · RIVER_SYSTEM ------------------------
# ve-nahar yotze me-eden le-hashqot et-ha-gan u-mi-sham yipared ve-hayah le-
# arbaah rashim
# "And a river went out of Eden to water the garden; and from thence it was
# parted, and became four heads."
m.step("Gen.2.10")
m.fact("nahar_yotze_me_eden(le_hashqot_et_ha_gan)",
       "yipared_le_arbaah_rashim(nahar)")
m.install("nahar", "nahar_1", "nahar_2", "nahar_3", "nahar_4")

# -------------------------- Gen.2.11 · REGISTRY_ROW_1 ----------------------
# shem ha-echad pishon hu ha-sovev et kol-eretz ha-chavilah asher-sham ha-
# zahav
# "The name of the first is Pishon; that is it which compasseth the whole
# land of Havilah, where there is gold."
m.step("Gen.2.11")
m.name("nahar_1", "Pishon")
m.fact("sovev_kol_eretz_ha_chavilah(nahar_1)",
       "sham_ha_zahav(chavilah)")

# -------------------------- Gen.2.12 · REGISTRY_ROW_1_RESOURCES ------------
# u-zahav ha-aretz ha-hiv tov sham ha-bedolach ve-even ha-shoham
# "And the gold of that land is good; there is bdellium and the onyx stone."
m.step("Gen.2.12")
m.fact("zahav_tov(ha_aretz_ha_hiv)",
       "sham_ha_bedolach_ve_even_ha_shoham(chavilah)")

# -------------------------- Gen.2.13 · REGISTRY_ROW_2 ----------------------
# ve-shem-ha-nahar ha-sheni gichon hu ha-sovev et kol-eretz kush
# "And the name of the second river is Gihon; the same is it that compasseth
# the whole land of Cush."
m.step("Gen.2.13")
m.name("nahar_2", "Gichon")
m.fact("sovev_kol_eretz_kush(nahar_2)")

# -------------------------- Gen.2.14 · REGISTRY_ROWS_3_4 -------------------
# ve-shem ha-nahar ha-shelishi chidekel hu ha-holekh qidmat ashur ve-ha-
# nahar ha-revii hu ferat
# "And the name of the third river is Hiddekel; that is it which goeth
# toward the east of Asshur. And the fourth river is the Euphrates."
m.step("Gen.2.14")
m.name("nahar_3", "Chidekel")
m.name("nahar_4", "Perat")
m.fact("holekh_qidmat_ashur(nahar_3)")

# -------------------------- Gen.2.15 · TAKE_SETTLE_ASSIGN_JOB --------------
# va-yiqach YHWH Elohim et-ha-adam va-yanichehu ve-gan-eden le-avdah u-le-
# shamrah
# "And the LORD God took the man, and put him into the garden of Eden to
# dress it and to keep it."
m.step("Gen.2.15")
m.event("take", agent="YHWH_Elohim", themes=["adam"])
m.event("settle", agent="YHWH_Elohim", themes=["adam"])
m.assign("adam", "oved_ve_shomer")

# -------------------------- Gen.2.16 · COMMAND_PERMISSION ------------------
# va-yetzav YHWH Elohim al-ha-adam le-mor mi-kol etz-ha-gan akhol tokhel
# "And the LORD God commanded the man, saying: 'Of every tree of the garden
# thou mayest freely eat.'"
m.step("Gen.2.16")
m.event("command", agent="YHWH_Elohim", themes=["adam"])
m.declare("YHWH_Elohim", "LET?",
          "akhal(adam, mi_kol_etz_ha_gan)")
m.spec_delta("kol esev + kol etz le-okhlah (1:29 universal food grant)",
             "mi-kol etz ha-gan + one exclusion pending (the grant narrows to a bounded domain)")

# -------------------------- Gen.2.17 · PROHIBITION_PENALTY -----------------
# u-me-etz ha-daat tov va-ra lo tokhal mimenu ki be-yom akholkha mimenu mot
# tamut
# "'But of the tree of the knowledge of good and evil, thou shalt not eat of
# it; for in the day that thou eatest thereof thou shalt surely die.'"
m.step("Gen.2.17")
m.declare("YHWH_Elohim", "LET-NOT",
          "akhal(adam, me_etz_ha_daat_tov_va_ra)")
m.handler("be_yom_akhal(adam, me_etz_ha_daat_tov_va_ra)",
          "mot_tamut(adam)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'nahar_4', 'nahar', 'nahar_1', 'adam', 'gan', 'etz_ha_chayim', 'nahar_2', 'etz_ha_daat_tov_va_ra', 'nahar_3'}
    assert m.presupposed_set() == {'shamayim', 'aretz', 'adamah', 'eden'}
    assert m.REGISTRY["names"] == {'nahar_1': 'Pishon', 'nahar_2': 'Gichon', 'nahar_3': 'Chidekel', 'nahar_4': 'Perat', 'adam': 'oved_ve_shomer'}
    assert m.REGISTRY["writes"] == 5
    assert m.tests_list() == []
    assert m.open_demands() == ['akhal(adam, mi_kol_etz_ha_gan)', 'akhal(adam, me_etz_ha_daat_tov_va_ra)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4, 'spec_delta': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['terem(kol_siach_ha_sadeh)', 'terem(kol_esev_ha_sadeh)', 'lo_himtir(YHWH_Elohim, al_ha_aretz)', 'adam_ayin(la_avod_et_ha_adamah)', 'ed_yaaleh_ve_hishqah(kol_pnei_ha_adamah)', 'nahar_yotze_me_eden(le_hashqot_et_ha_gan)', 'yipared_le_arbaah_rashim(nahar)', 'sovev_kol_eretz_ha_chavilah(nahar_1)', 'sham_ha_zahav(chavilah)', 'zahav_tov(ha_aretz_ha_hiv)', 'sham_ha_bedolach_ve_even_ha_shoham(chavilah)', 'sovev_kol_eretz_kush(nahar_2)', 'holekh_qidmat_ashur(nahar_3)', 'handler: IF(be_yom_akhal(adam, me_etz_ha_daat_tov_va_ra)) THEN(mot_tamut(adam))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 18
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
