#!/usr/bin/env python3
# =============================================================================
# gen_09_helper_woman_first_speech — 2:18-25
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_09_helper_woman_first_speech.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden II: not-good, the helper, the woman, first human speech (2:18-25)"""
from machine import Machine

m = Machine("gen_09_helper_woman_first_speech")

# -------------------------- Gen.2.18 · VERDICT_FAIL_AND_PLAN ---------------
# va-yomer YHWH Elohim lo-tov heyot ha-adam levado e'eseh-lo ezer kenegdo
# "And the LORD God said: 'It is not good that the man should be alone; I
# will make him a help meet for him.'"
m.step("Gen.2.18")
m.test("FAIL", "tov", "heyot_ha_adam_levado")
m.declare("YHWH_Elohim", "CMD-US?",
          "make(ezer_kenegdo, le_adam)")
m.presupposed("adam")

# -------------------------- Gen.2.19 · FORM_BRING_DELEGATE -----------------
# va-yitzer YHWH Elohim min-ha-adamah kol-chayat ha-sadeh ve-et kol-of ha-
# shamayim va-yave el-ha-adam li-reot mah-yiqra-lo ve-khol asher yiqra-lo
# ha-adam nefesh chayah hu shemo
# "And out of the ground the LORD God formed every beast of the field, and
# every fowl of the air; and brought them unto the man to see what he would
# call them; and whatsoever the man would call every living creature, that
# was to be the name thereof."
m.step("Gen.2.19")
m.event("form", agent="YHWH_Elohim", themes=["chayat_ha_sadeh", "of_ha_shamayim"])
m.install("chayat_ha_sadeh", "of_ha_shamayim")
m.event("bring", agent="YHWH_Elohim", themes=["chayat_ha_sadeh"])
m.fact("hu_shemo(kol_asher_yiqra_lo_ha_adam)")
m.presupposed("adamah")

# -------------------------- Gen.2.20 · BULK_NAMING_FAILED_SEARCH -----------
# va-yiqra ha-adam shemot le-khol-ha-behemah u-le-of ha-shamayim u-le-khol
# chayat ha-sadeh u-le-adam lo-matza ezer kenegdo
# "And the man gave names to all cattle, and to the fowl of the air, and to
# every beast of the field; but for Adam there was not found a help meet for
# him."
m.step("Gen.2.20")
m.event("call", agent="adam", themes=["shemot"])
m.fact("lo_matza(ezer_kenegdo, le_adam)")
m.presupposed("behemah")

# -------------------------- Gen.2.21 · SLEEP_AND_SURGERY -------------------
# va-yapel YHWH Elohim tardemah al-ha-adam va-yishan va-yiqach achat mi-
# tzalotav va-yisgor basar tachtenah
# "And the LORD God caused a deep sleep to fall upon the man, and he slept;
# and He took one of his ribs, and closed up the place with flesh instead
# thereof."
m.step("Gen.2.21")
m.event("cast_sleep", agent="YHWH_Elohim", themes=["tardemah"])
m.event("take", agent="YHWH_Elohim", themes=["tzela"])
m.event("close", agent="YHWH_Elohim", themes=["basar"])

# -------------------------- Gen.2.22 · BUILD_WOMAN_RECEIPT -----------------
# va-yiven YHWH Elohim et-ha-tzela asher-laqach min-ha-adam le-ishah va-
# yevieha el-ha-adam
# "And the rib, which the LORD God had taken from the man, made He a woman,
# and brought her unto the man."
m.step("Gen.2.22")
m.event("build", agent="YHWH_Elohim", themes=["ishah"])
m.install("ishah")
m.result("make(ezer_kenegdo, le_adam)", tmark="t1")
m.spec_delta("e'eseh (I will MAKE — asah, the week's build verb)",
             "va-yiven (He BUILT — banah, first token)")

# -------------------------- Gen.2.23 · FIRST_HUMAN_SPEECH_NAME -------------
# va-yomer ha-adam zot ha-paam etzem me-atzamai u-vasar mi-besari le-zot
# yiqare ishah ki me-ish lukocha-zot
# "And the man said: 'This is now bone of my bones, and flesh of my flesh;
# she shall be called Woman, because she was taken out of Man.'"
m.step("Gen.2.23")
m.event("say", agent="adam")
m.name("ishah", "ishah")

# -------------------------- Gen.2.24 · ETIOLOGY_PATTERN --------------------
# al-ken yaazov-ish et-aviv ve-et-imo ve-davak be-ishto ve-hayu le-vasar
# echad
# "Therefore shall a man leave his father and his mother, and shall cleave
# unto his wife, and they shall be one flesh."
m.step("Gen.2.24")
m.pattern("azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)")

# -------------------------- Gen.2.25 · CLOSING_STATE_BRIDGE ----------------
# va-yihyu shneihem arumim ha-adam ve-ishto ve-lo yitboshashu
# "And they were both naked, the man and his wife, and were not ashamed."
m.step("Gen.2.25")
m.fact("arumim(ha_adam_ve_ishto)",
       "lo_yitboshashu(shneihem)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ishah', 'chayat_ha_sadeh', 'of_ha_shamayim'}
    assert m.presupposed_set() == {'adam', 'adamah', 'behemah'}
    assert m.REGISTRY["names"] == {'ishah': 'ishah'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == [('FAIL', 'tov', 'heyot_ha_adam_levado')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['hu_shemo(kol_asher_yiqra_lo_ha_adam)', 'lo_matza(ezer_kenegdo, le_adam)', 'pattern: azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)', 'arumim(ha_adam_ve_ishto)', 'lo_yitboshashu(shneihem)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
