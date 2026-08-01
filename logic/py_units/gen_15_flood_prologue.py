#!/usr/bin/env python3
# =============================================================================
# gen_15_flood_prologue — 6:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_15_flood_prologue.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The flood prologue: the stolen verdict, the 120 years, the regret, the favor (6:1-8)"""
from machine import Machine

m = Machine("gen_15_flood_prologue")

# -------------------------- Gen.6.1 · MULTIPLYING_AND_DAUGHTERS ------------
# va-yehi ki-hechel ha-adam la-rov al-pnei ha-adamah u-vanot yuldu lahem
# "And it came to pass, when men began to multiply on the face of the earth,
# and daughters were born unto them,"
m.step("Gen.6.1")
m.event("multiply", agent="ha_adam")
m.event("born", themes=["banot"])
m.presupposed("adam")

# -------------------------- Gen.6.2 · STOLEN_FORMULA_THE_TAKING ------------
# va-yiru vnei-ha-Elohim et-bnot ha-adam ki tovot henah va-yiqchu lahem
# nashim mi-kol asher bacharu
# "that the sons of God saw the daughters of men that they were fair; and
# they took them wives, whomsoever they chose."
m.step("Gen.6.2")
m.event("see", agent="bnei_ha_elohim", themes=["benot_ha_adam"])
m.test("PASS", "tovot", "benot_ha_adam")
m.spec_delta("va-yar Elohim ki-tov — the Maker inspects His work and verdicts it good (the frozen week units)",
             "va-yiru bnei-ha-elohim et-bnot ha-adam ki tovot — creature subjects, human daughters as object, and a TAKING as the consequence (6:2)")
m.event("take", agent="bnei_ha_elohim", themes=["nashim_mi_kol_asher_bacharu"])

# -------------------------- Gen.6.3 · DECREE_120_YEARS ---------------------
# va-yomer YHWH lo-yadon ruchi va-adam le-olam be-shagam hu vasar ve-hayu
# yamav meah ve-esrim shanah
# "And the LORD said: 'My spirit shall not abide in man for ever, for that
# he also is flesh; therefore shall his days be a hundred and twenty
# years.'"
m.step("Gen.6.3")
m.event("say", agent="YHWH")
m.fact("lo_yadon_ruchi_va_adam_le_olam",
       "ve_hayu_yamav_meah_ve_esrim_shanah")

# -------------------------- Gen.6.4 · NEPHILIM_PARENTHESIS -----------------
# ha-nefilim hayu va-aretz ba-yamim ha-hem ve-gam acharei-khen asher yavou
# bnei ha-Elohim el-bnot ha-adam ve-yaldu lahem hemah ha-giborim asher me-
# olam anshei ha-shem
# "The Nephilim were in the earth in those days, and also after that, when
# the sons of God came in unto the daughters of men, and they bore children
# to them; the same were the mighty men that were of old, the men of
# renown."
m.step("Gen.6.4")
m.fact("ha_nefilim_hayu_va_aretz",
       "anshei_ha_shem_me_olam")

# -------------------------- Gen.6.5 · INVERTED_INSPECTION_TOTAL_DIAGNOSIS --
# va-yar YHWH ki rabbah raat ha-adam ba-aretz ve-khol-yetzer machshevot libo
# raq ra kol-ha-yom
# "And the LORD saw that the wickedness of man was great in the earth, and
# that every imagination of the thoughts of his heart was only evil
# continually."
m.step("Gen.6.5")
m.event("see", agent="YHWH", themes=["raat_ha_adam"])
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — He saw all He had made: very good (1:31, frozen day 6)",
             "va-yar YHWH ki rabbah raat ha-adam — He saw: GREAT was the EVIL of man (6:5)")
m.fact("kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom")

# -------------------------- Gen.6.6 · REGRET_AND_GRIEF ---------------------
# va-yinachem YHWH ki-asah et-ha-adam ba-aretz va-yitatzev el-libo
# "And it repented the LORD that He had made man on the earth, and it
# grieved Him at His heart."
m.step("Gen.6.6")
m.event("regret", agent="YHWH")
m.event("grieve", agent="YHWH", themes=["libo"])

# -------------------------- Gen.6.7 · WIPE_RESOLVE_PUSHED ------------------
# va-yomer YHWH emcheh et-ha-adam asher-barati me-al pnei ha-adamah me-adam
# ad-behemah ad-remes ve-ad-of ha-shamayim ki nichamti ki asitim
# "And the LORD said: 'I will blot out man whom I have created from the face
# of the earth; both man, and beast, and creeping thing, and fowl of the
# air; for it repenteth Me that I have made them.'"
m.step("Gen.6.7")
m.event("say", agent="YHWH")
m.declare("YHWH", "CMD-US?",
          "machah(ha_adam, me_al_pnei_ha_adamah)")
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim")

# -------------------------- Gen.6.8 · FIVE_WORDS_FAVOR ---------------------
# ve-Noach matza chen be-einei YHWH
# "But Noah found grace in the eyes of the LORD."
m.step("Gen.6.8")
m.fact("noach_matza_chen_be_einei_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tovot', 'benot_ha_adam')]
    assert m.open_demands() == ['machah(ha_adam, me_al_pnei_ha_adamah)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_yadon_ruchi_va_adam_le_olam', 've_hayu_yamav_meah_ve_esrim_shanah', 'ha_nefilim_hayu_va_aretz', 'anshei_ha_shem_me_olam', 'kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom', 'me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim', 'noach_matza_chen_be_einei_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
