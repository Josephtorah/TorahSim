#!/usr/bin/env python3
# =============================================================================
# gen_07_completion_sanctity — 2:1-3
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_07_completion_sanctity.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day seven: completion and sanctity — the open transaction (2:1-3)"""
from machine import Machine

m = Machine("gen_07_completion_sanctity")

# -------------------------- Gen.2.1 · COMPLETION_PASSIVE -------------------
# va-yekhulu ha-shamayim ve-ha-aretz ve-khol-tzeva'am
# "And the heaven and the earth were finished, and all the host of them."
m.step("Gen.2.1")
m.event("complete", themes=["shamayim", "aretz", "tzevaam"])
m.presupposed("shamayim", "aretz")

# -------------------------- Gen.2.2 · COMPLETE_CEASE -----------------------
# va-yekhal Elohim ba-yom ha-shevi'i melakhto asher asah va-yishbot ba-yom
# ha-shevi'i mi-kol-melakhto asher asah
# "And on the seventh day God finished His work which He had made; and He
# rested on the seventh day from all His work which He had made."
m.step("Gen.2.2")
m.event("finish", agent="Elohim")
m.event("cease", agent="Elohim")

# -------------------------- Gen.2.3 · BLESS_SANCTIFY -----------------------
# va-yevarekh Elohim et-yom ha-shevi'i va-yekadesh oto ki vo shavat mi-kol-
# melakhto asher-bara Elohim la'asot
# "And God blessed the seventh day, and hallowed it; because that in it He
# rested from all His work which God in creating had made."
m.step("Gen.2.3")
m.bless("Elohim", "yom_ha_shevii")
m.assign("yom_ha_shevii", "kadosh")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'shamayim', 'aretz'}
    assert m.REGISTRY["names"] == {'yom_ha_shevii': 'kadosh'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2, 'assigned_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
