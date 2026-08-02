#!/usr/bin/env python3
# =============================================================================
# gen_20_exit_altar — 8:15-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_20_exit_altar.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The exit and the altar: go out, the families, the pleasing smell, never again (8:15-22)"""
from machine import Machine

m = Machine("gen_20_exit_altar")

# -------------------------- Gen.8.15 · THE_SPEAK_VERB_DEBUTS ---------------
# va-yedaber Elohim el-Noach lemor
# "And God spoke unto Noah, saying:"
m.step("Gen.8.15")
m.event("speak", agent="elohim", themes=["el_noach"])
m.presupposed("noach", "tevah")

# -------------------------- Gen.8.16 · THE_EXIT_COMMAND --------------------
# tze min-ha-tevah atah ve-ishtekha u-vanekha u-neshei-vanekha itakh
# "'Go forth from the ark, thou, and thy wife, and thy sons, and thy sons'
# wives with thee."
m.step("Gen.8.16")
m.declare("elohim", "LET",
          "tze(noach, min_ha_tevah)")

# -------------------------- Gen.8.17 · THE_BRING_OUT_AND_THE_CHARGE --------
# kol-ha-chayah asher-itekha mi-kol-basar ba-of u-va-behemah u-ve-khol-ha-
# remes ha-romes al-ha-aretz hotze [ktiv] haytze [qere] itakh ve-shartzu va-
# aretz u-faru ve-ravu al-ha-aretz
# "Bring forth with thee every living thing that is with thee, of all flesh,
# both fowl, and cattle, and every creeping thing that creepeth upon the
# earth; that they may swarm in the earth, and be fruitful, and multiply
# upon the earth.'"
m.step("Gen.8.17")
m.declare("elohim", "LET",
          "hotze(kol_ha_chayah, itakh)")
m.fact("ve_shartzu_u_faru_ve_ravu_al_ha_aretz")

# -------------------------- Gen.8.18 · THE_EXIT_RECEIPT --------------------
# va-yetze-Noach u-vanav ve-ishto u-neshei-vanav ito
# "And Noah went forth, and his sons, and his wife, and his sons' wives with
# him;"
m.step("Gen.8.18")
m.event("go_out", agent="noach")
m.result("tze(noach, min_ha_tevah)", tmark="t1")

# -------------------------- Gen.8.19 · OUT_BY_FAMILIES ---------------------
# kol-ha-chayah kol-ha-remes ve-khol-ha-of kol romes al-ha-aretz le-
# mishpechoteihem yatzu min-ha-tevah
# "every beast, every creeping thing, and every fowl, whatsoever moveth upon
# the earth, after their families, went forth out of the ark."
m.step("Gen.8.19")
m.fact("le_mishpechoteihem_yatzu_min_ha_tevah")
m.result("hotze(kol_ha_chayah, itakh)", tmark="t1")

# -------------------------- Gen.8.20 · THE_FIRST_ALTAR ---------------------
# va-yiven Noach mizbeach la-YHWH va-yikkach mi-kol ha-behemah ha-tehorah
# u-mi-kol ha-of ha-tahor va-yaal olot ba-mizbeach
# "And Noah builded an altar unto the LORD; and took of every clean beast,
# and of every clean fowl, and offered burnt-offerings on the altar."
m.step("Gen.8.20")
m.event("build", agent="noach", themes=["mizbeach"])
m.install("mizbeach")
m.event("take", agent="noach", themes=["min_ha_behemah_ha_tehorah_u_min_ha_of_ha_tahor"])
m.event("offer_up", agent="noach", themes=["olot_ba_mizbeach"])

# -------------------------- Gen.8.21 · THE_SMELL_THE_HEART_THE_NEVER_AGAINS -
# va-yarach YHWH et-reiach ha-nichoach va-yomer YHWH el-libo lo-osif le-
# qalel od et-ha-adamah baavur ha-adam ki yetzer lev ha-adam ra mi-neurav
# ve-lo-osif od le-hakot et-kol-chai ka-asher asiti
# "And the LORD smelled the sweet savour; and the LORD said in His heart: 'I
# will not again curse the ground any more for man's sake; for the
# imagination of man's heart is evil from his youth; neither will I again
# smite any more every thing living, as I have done."
m.step("Gen.8.21")
m.event("smell", agent="YHWH", themes=["reiach_ha_nichoach"])
m.test("PASS", "nichoach", "ha_olah")
m.event("say", agent="YHWH", themes=["el_libo"])
m.invariant("lo_osif_le_qalel_od_et_ha_adamah")
m.invariant("lo_osif_od_le_hakot_et_kol_chai")

# -------------------------- Gen.8.22 · THE_SEASONS_PLEDGE ------------------
# od kol-yemei ha-aretz zera ve-qatzir ve-qor va-chom ve-qayitz va-choref
# ve-yom va-laylah lo yishbotu
# "While the earth remaineth, seedtime and harvest, and cold and heat, and
# summer and winter, and day and night shall not cease.'"
m.step("Gen.8.22")
m.invariant("zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach'}
    assert m.presupposed_set() == {'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'nichoach', 'ha_olah')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_shartzu_u_faru_ve_ravu_al_ha_aretz', 'le_mishpechoteihem_yatzu_min_ha_tevah'])
    assert m.WORLD["invariants"] == ['lo_osif_le_qalel_od_et_ha_adamah', 'lo_osif_od_le_hakot_et_kol_chai', 'zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
