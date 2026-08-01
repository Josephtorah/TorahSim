#!/usr/bin/env python3
# =============================================================================
# gen_01_creation_boot — 1:1-5
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_01_creation_boot.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Genesis boot: create world, light, separate, name, day one (1:1-5)"""
from machine import Machine

m = Machine("gen_01_creation_boot")

# -------------------------- Gen.1.1 · EVENT_CREATE -------------------------
# be-reshit bara Elohim et ha-shamayim ve-et ha-aretz
# "[EN-AID] In the beginning God created the heavens and the earth."
m.step("Gen.1.1")
m.time_anchor("reshit")
m.event("create", agent="Elohim", themes=["shamayim", "aretz"])
m.install("shamayim", "aretz")

# -------------------------- Gen.1.2 · STATE_BLOCK --------------------------
# ve-ha-aretz hayta tohu va-vohu ve-choshekh al-penei tehom ve-ruach Elohim
# merachefet al-penei ha-mayim
# "[EN-AID] The earth was formless and void, darkness over the deep, God's
# spirit hovering over the waters."
m.step("Gen.1.2")
m.fact("tohu(aretz) ∧ vohu(aretz)",
       "over(choshekh, face(tehom))")
m.invariant("hover(ruach-Elohim, face(mayim))")
m.note_zero_events()
m.presupposed("choshekh", "tehom", "mayim", "ruach")

# -------------------------- Gen.1.3 · DECLARE_LET_RESULT -------------------
# va-yomer Elohim yehi or va-yehi or
# "[EN-AID] God said: let there be light — and there was light."
m.step("Gen.1.3")
m.declare("Elohim", "LET",
          "exists(or)")
m.triple("exists(or)")
m.result("exists(or)", tmark="t1")

# -------------------------- Gen.1.4 · TEST_AND_PARTITION -------------------
# va-yar Elohim et-ha-or ki-tov va-yavdel Elohim bein ha-or u-vein ha-
# choshekh
# "[EN-AID] God saw the light, that it was good; and God divided the light
# from the darkness."
m.step("Gen.1.4")
m.test("PASS", "tov", "or")
m.partition("or", "choshekh")

# -------------------------- Gen.1.5 · NAME_AND_COMMIT ----------------------
# va-yiqra Elohim la-or yom ve-la-choshekh qara layla va-yehi erev va-yehi
# voqer yom echad
# "[EN-AID] God called the light Day and the darkness Night; evening,
# morning — day one."
m.step("Gen.1.5")
m.name("or", "yom")
m.name("choshekh", "layla")
m.commit(1, label_form="cardinal", label_translit="yom echad")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shamayim', 'aretz', 'or'}
    assert m.presupposed_set() == {'mayim', 'tehom', 'ruach', 'choshekh'}
    assert m.REGISTRY["names"] == {'or': 'yom', 'choshekh': 'layla'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'tov', 'or')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == [1]
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['tohu(aretz) ∧ vohu(aretz)', 'over(choshekh, face(tehom))'])
    assert m.WORLD["invariants"] == ['hover(ruach-Elohim, face(mayim))']
    assert m.WORLD["partitions"] == [('or', 'choshekh')]
    assert len(m.EVENTS) == 6
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
