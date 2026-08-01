#!/usr/bin/env python3
# =============================================================================
# gen_05_swarms_blessing — 1:20-23
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_05_swarms_blessing.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day five: swarms and the blessing — LET? demands, missing receipt, bara returns, first life, first blessing (1:20-23)"""
from machine import Machine

m = Machine("gen_05_swarms_blessing")

# -------------------------- Gen.1.20 · DECLARE_SPEC_SWARM_FLIGHT -----------
# va-yomer Elohim yishretzu ha-mayim sheretz nefesh chaya ve-of ye'ofef al-
# ha-aretz al-pnei reqia ha-shamayim
# "And God said: 'Let the waters swarm with swarms of living creatures, and
# let fowl fly above the earth in the open firmament of heaven.'"
m.step("Gen.1.20")
m.declare("Elohim", "LET?",
          "swarm(mayim), product=sheretz_nefesh_chaya")
m.declare("Elohim", "LET?",
          "fly(of), loc=pnei_raqia_ha_shamayim")
m.triple("swarm(mayim), product=sheretz_nefesh_chaya")
m.presupposed("mayim", "aretz", "raqia", "shamayim")

# -------------------------- Gen.1.21 · BUILD_CREATE_CREDIT_DELTA_TEST ------
# va-yivra Elohim et-ha-taninim ha-gedolim ve-et kol-nefesh ha-chaya ha-
# romeset asher shartzu ha-mayim le-minehem ve-et kol-of kanaf le-minehu va-
# yar Elohim ki-tov
# "And God created the great sea-monsters, and every living creature that
# creepeth, wherewith the waters swarmed, after its kind, and every winged
# fowl after its kind; and God saw that it was good."
m.step("Gen.1.21")
m.event("create", agent="Elohim", themes=["taninim", "nefesh_chaya_romeset", "of_kanaf"])
m.install("taninim", "nefesh_chaya_romeset", "of_kanaf")
m.result("swarm(mayim), product=sheretz_nefesh_chaya", tmark="t1")
m.result("fly(of), loc=pnei_raqia_ha_shamayim", tmark="t1")
m.spec_delta("yishretzu HA-MAYIM (the waters as delegated producer)",
             "va-yivra ELOHIM (bara — God executes; the waters credited only in the relative clause)")
m.spec_delta("no taninim in the order",
             "et-ha-taninim ha-gedolim leading the inventory, with the week")
m.spec_delta("sheretz nefesh chaya; of (bare classes)",
             "kol- totality x2, kind-keys le-minehem / le-minehu, of differentiated as of KANAF")
m.test("PASS", "tov", "nefesh_chaya")

# -------------------------- Gen.1.22 · BLESS_MANDATE -----------------------
# va-yevarekh otam Elohim le-mor peru u-revu u-milu et-ha-mayim ba-yamim ve-
# ha-of yirev ba-aretz
# "And God blessed them, saying: 'Be fruitful, and multiply, and fill the
# waters in the seas, and let fowl multiply in the earth.'"
m.step("Gen.1.22")
m.bless("Elohim", "otam", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_mayim_ba_yamim))", "LET(yirev(ha_of_ba_aretz))"])
m.presupposed("yamim")

# -------------------------- Gen.1.23 · COMMIT_DAY --------------------------
# va-yehi erev va-yehi voqer yom chamishi
# "And there was evening and there was morning, a fifth day."
m.step("Gen.1.23")
m.commit(5, label_form="ordinal", label_translit="yom chamishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'taninim', 'nefesh_chaya_romeset', 'of_kanaf'}
    assert m.presupposed_set() == {'mayim', 'shamayim', 'aretz', 'yamim', 'raqia'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tov', 'nefesh_chaya')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == [5]
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_mayim_ba_yamim))', 'mandate: LET(yirev(ha_of_ba_aretz))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
