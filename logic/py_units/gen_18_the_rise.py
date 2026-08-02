#!/usr/bin/env python3
# =============================================================================
# gen_18_the_rise — 7:17-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_18_the_rise.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The rise: the waters lift the ark, all flesh dies, only Noach is left (7:17-24)"""
from machine import Machine

m = Machine("gen_18_the_rise")

# -------------------------- Gen.7.17 · THE_LIFT_AND_THE_RISE ---------------
# va-yehi ha-mabul arbaim yom al-ha-aretz va-yirbu ha-mayim va-yisu et-ha-
# tevah va-taram me-al ha-aretz
# "And the flood was forty days upon the earth; and the waters increased,
# and bore up the ark, and it was lifted up above the earth."
m.step("Gen.7.17")
m.fact("ha_mabul_arbaim_yom_al_ha_aretz")
m.event("lift", agent="ha_mayim", themes=["ha_tevah"])
m.event("rise", themes=["ha_tevah"])
m.presupposed("tevah", "mayim")

# -------------------------- Gen.7.18 · THE_PREVAIL_DEBUT_THE_ARK_WALKS -----
# va-yigberu ha-mayim va-yirbu meod al-ha-aretz va-telekh ha-tevah al-pnei
# ha-mayim
# "And the waters prevailed, and increased greatly upon the earth; and the
# ark went upon the face of the waters."
m.step("Gen.7.18")
m.event("prevail", agent="ha_mayim")
m.fact("va_yirbu_meod_al_ha_aretz")
m.event("walk", agent="ha_tevah", themes=["al_pnei_ha_mayim"])

# -------------------------- Gen.7.19 · THE_MOUNTAINS_GO_UNDER --------------
# ve-ha-mayim gavru meod meod al-ha-aretz va-yekhusu kol-he-harim ha-gevohim
# asher-tachat kol-ha-shamayim
# "And the waters prevailed exceedingly upon the earth; and all the high
# mountains that were under the whole heaven were covered."
m.step("Gen.7.19")
m.fact("gavru_meod_meod_al_ha_aretz",
       "kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim")
m.event("cover", themes=["kol_he_harim_ha_gevohim"])

# -------------------------- Gen.7.20 · FIFTEEN_CUBITS_UPWARD ---------------
# chamesh esreh amah mi-lemalah gavru ha-mayim va-yekhusu he-harim
# "Fifteen cubits upward did the waters prevail; and the mountains were
# covered."
m.step("Gen.7.20")
m.fact("chamesh_esreh_amah_mi_lemalah_gavru")
m.event("cover", themes=["he_harim"])

# -------------------------- Gen.7.21 · ALL_FLESH_EXPIRES -------------------
# va-yigva kol-basar ha-romes al-ha-aretz ba-of u-va-behemah u-va-chayah
# u-ve-khol-ha-sheretz ha-shoretz al-ha-aretz ve-khol ha-adam
# "And all flesh perished that moved upon the earth, both fowl, and cattle,
# and beast, and every swarming thing that swarmeth upon the earth, and
# every man;"
m.step("Gen.7.21")
m.event("expire", themes=["kol_basar"])
m.fact("ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam")

# -------------------------- Gen.7.22 · THE_COMPOUNDED_BREATH_CRITERION -----
# kol asher nishmat-ruach chayim be-apav mi-kol asher be-charavah metu
# "all in whose nostrils was the breath of the spirit of life, whatsoever
# was in the dry land, died."
m.step("Gen.7.22")
m.fact("nishmat_ruach_chayim_be_apav",
       "mi_kol_asher_be_charavah_metu")

# -------------------------- Gen.7.23 · THE_WIPE_EXECUTED_ONLY_NOACH_LEFT ---
# va-yimach et-kol-ha-yequm asher al-pnei ha-adamah me-adam ad-behemah ad-
# remes ve-ad-of ha-shamayim va-yimachu min-ha-aretz va-yishaer akh-Noach
# va-asher ito ba-tevah
# "And He blotted out every living substance which was upon the face of the
# ground, both man, and cattle, and creeping thing, and fowl of the heaven;
# and they were blotted out from the earth; and Noah only was left, and they
# that were with him in the ark."
m.step("Gen.7.23")
m.event("wipe", themes=["kol_ha_yequm"])
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of")
m.event("wiped", themes=["kol_ha_yequm"])
m.event("remain", themes=["akh_noach_va_asher_ito"])
m.presupposed("noach")

# -------------------------- Gen.7.24 · THE_HUNDRED_AND_FIFTY_DAYS ----------
# va-yigberu ha-mayim al-ha-aretz chamishim u-meat yom
# "And the waters prevailed upon the earth a hundred and fifty days."
m.step("Gen.7.24")
m.event("prevail", agent="ha_mayim")
m.fact("chamishim_u_meat_yom_al_ha_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'noach', 'mayim', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['ha_mabul_arbaim_yom_al_ha_aretz', 'va_yirbu_meod_al_ha_aretz', 'gavru_meod_meod_al_ha_aretz', 'kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim', 'chamesh_esreh_amah_mi_lemalah_gavru', 'ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam', 'nishmat_ruach_chayim_be_apav', 'mi_kol_asher_be_charavah_metu', 'me_adam_ad_behemah_ad_remes_ve_ad_of', 'chamishim_u_meat_yom_al_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
