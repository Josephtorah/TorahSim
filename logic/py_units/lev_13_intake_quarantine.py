#!/usr/bin/env python3
# =============================================================================
# lev_13_intake_quarantine — 13:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_intake_quarantine.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The skin-mark intake: case, handlers, quarantine loop (Lev 13:1-8) — first law unit"""
from machine import Machine

m = Machine("lev_13_intake_quarantine")

# -------------------------- Lev.13.1 · FRAME_SPEECH ------------------------
# va-yedabber YHWH el-Moshe ve-el-Aharon le-mor
# "And the LORD spoke unto Moses and unto Aaron, saying:"
m.step("Lev.13.1")
m.event("speak", agent="YHWH")
m.presupposed("moshe", "aharon")

# -------------------------- Lev.13.2 · CASE_INTAKE -------------------------
# adam ki-yihyeh ve-or-besaro se'et o-sapachat o vaheret ve-hayah ve-or-
# besaro le-nega tzara'at ve-huva el-Aharon ha-kohen o el-achad mi-banav ha-
# kohanim
# "When a man shall have in the skin of his flesh a rising, or a scab, or a
# bright spot, and it become in the skin of his flesh the plague of leprosy,
# then he shall be brought unto Aaron the priest, or unto one of his sons
# the priests."
m.step("Lev.13.2")
m.case("adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat", "hova_el_ha_kohen")
m.presupposed("adam", "or_basar", "ha_kohen")

# -------------------------- Lev.13.3 · HANDLER_VERDICT_TAMEI ---------------
# ve-ra'ah ha-kohen et-ha-nega be-or ha-basar ve-se'ar ba-nega hafakh lavan
# u-mar'eh ha-nega amok me-or besaro nega tzara'at hu ve-ra'ahu ha-kohen ve-
# timme oto
# "And the priest shall look upon the plague in the skin of the flesh; and
# if the hair in the plague be turned white, and the appearance of the
# plague be deeper than the skin of his flesh, it is the plague of leprosy;
# and the priest shall look on him, and pronounce him unclean."
m.step("Lev.13.3")
m.handler("sear_hafakh_lavan ∧ mareh_amok_me_or",
          "classify(nega_tzaraat_hu) ∧ timme(status_tamei)")

# -------------------------- Lev.13.4 · HANDLER_CONFINE_FIRST ---------------
# ve-im-baheret levanah hi ve-or besaro ve-amok ein-mar'eha min-ha-or
# u-se'arah lo-hafakh lavan ve-hisgir ha-kohen et-ha-nega shivat yamim
# "And if the bright spot be white in the skin of his flesh, and the
# appearance thereof be not deeper than the skin, and the hair thereof be
# not turned white, then the priest shall shut up him that hath the plague
# seven days."
m.step("Lev.13.4")
m.handler("baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan",
          "hisgir(et_ha_nega, shivat_yamim)")

# -------------------------- Lev.13.5 · HANDLER_RECHECK_CONFINE_SECOND ------
# ve-ra'ahu ha-kohen ba-yom ha-shevi'i ve-hineh ha-nega amad be-einav lo-
# fasah ha-nega ba-or ve-hisgiro ha-kohen shivat yamim shenit
# "And the priest shall look on him the seventh day; and, behold, if the
# plague stay in its appearance, and the plague be not spread in the skin,
# then the priest shall shut him up seven days more."
m.step("Lev.13.5")
m.handler("ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah",
          "hisgiro(shivat_yamim_shenit)")

# -------------------------- Lev.13.6 · HANDLER_RELEASE ---------------------
# ve-ra'ah ha-kohen oto ba-yom ha-shevi'i shenit ve-hineh kehah ha-nega ve-
# lo-fasah ha-nega ba-or ve-tiharo ha-kohen mispachat hi ve-khibbes begadav
# ve-taher
# "And the priest shall look on him again the seventh day; and, behold, if
# the plague be dim, and the plague be not spread in the skin, then the
# priest shall pronounce him clean: it is a scab; and he shall wash his
# clothes, and be clean."
m.step("Lev.13.6")
m.handler("ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah",
          "tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher")

# -------------------------- Lev.13.7 · HANDLER_REOPEN_TRIGGER --------------
# ve-im-pasoh tifseh ha-mispachat ba-or acharei hera'oto el-ha-kohen le-
# tohorato ve-nir'ah shenit el-ha-kohen
# "But if the scab spread abroad in the skin, after that he hath shown
# himself to the priest for his cleansing, he shall show himself to the
# priest again."
m.step("Lev.13.7")
m.handler("pasoh_tifseh(acharei_heraoto_le_tohorato)",
          "nirah_shenit_el_ha_kohen")

# -------------------------- Lev.13.8 · HANDLER_REOPEN_VERDICT --------------
# ve-ra'ah ha-kohen ve-hineh pastah ha-mispachat ba-or ve-timme'o ha-kohen
# tzara'at hi
# "And the priest shall look, and, behold, the scab is spread in the skin;
# then the priest shall pronounce him unclean: it is leprosy."
m.step("Lev.13.8")
m.handler("hineh_pastah_ha_mispachat",
          "timmeo(status_tamei) ∧ classify(tzaraat_hi)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'or_basar', 'moshe', 'adam', 'aharon', 'ha_kohen'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['case: adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat -> hova_el_ha_kohen', 'handler: IF(sear_hafakh_lavan ∧ mareh_amok_me_or) THEN(classify(nega_tzaraat_hu) ∧ timme(status_tamei))', 'handler: IF(baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan) THEN(hisgir(et_ha_nega, shivat_yamim))', 'handler: IF(ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah) THEN(hisgiro(shivat_yamim_shenit))', 'handler: IF(ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah) THEN(tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher)', 'handler: IF(pasoh_tifseh(acharei_heraoto_le_tohorato)) THEN(nirah_shenit_el_ha_kohen)', 'handler: IF(hineh_pastah_ha_mispachat) THEN(timmeo(status_tamei) ∧ classify(tzaraat_hi))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 8
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
