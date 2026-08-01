#!/usr/bin/env python3
# =============================================================================
# gen_04_lights_calendar — 1:14-19
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_04_lights_calendar.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day four: luminaries — jobs, calendar, dominion; three spec deltas (1:14-19)"""
from machine import Machine

m = Machine("gen_04_lights_calendar")

# -------------------------- Gen.1.14 · DECLARE_SPEC_CALENDAR ---------------
# va-yomer Elohim yehi me'orot bi-rkia ha-shamayim le-havdil bein ha-yom
# u-vein ha-lailah ve-hayu le-otot u-le-mo'adim u-le-yamim ve-shanim
# "And God said: 'Let there be lights in the firmament of the heaven to
# divide the day from the night; and let them be for signs, and for seasons,
# and for days and years.'"
m.step("Gen.1.14")
m.declare("Elohim", "LET",
          "exists(meorot), loc=raqia_ha_shamayim")
m.triple("exists(meorot), loc=raqia_ha_shamayim")
m.presupposed("raqia", "shamayim")

# -------------------------- Gen.1.15 · SPEC_CROSS_REGISTRY_RESULT ----------
# ve-hayu li-me'orot bi-rkia ha-shamayim le-ha'ir al-ha-aretz va-yehi khen
# "'And let them be for lights in the firmament of the heaven to give light
# upon the earth.' And it was so."
m.step("Gen.1.15")
m.presupposed("aretz")
m.result("exists(meorot), loc=raqia_ha_shamayim", tmark="t1")

# -------------------------- Gen.1.16 · BUILD_DIFFERENTIATE_DELTA -----------
# va-ya'as Elohim et-shnei ha-me'orot ha-gedolim et-ha-maor ha-gadol le-
# memshelet ha-yom ve-et-ha-maor ha-qaton le-memshelet ha-lailah ve-et ha-
# kokhavim
# "And God made the two great lights: the greater light to rule the day, and
# the lesser light to rule the night; and the stars."
m.step("Gen.1.16")
m.event("make", agent="Elohim", themes=["maor_gadol", "maor_qaton", "kokhavim"])
m.install("maor_gadol", "maor_qaton", "kokhavim")
m.assign("maor_gadol", "memshelet_yom")
m.assign("maor_qaton", "memshelet_lailah")
m.spec_delta("me'orot (one undifferentiated plural)",
             "shnei ha-me")
m.spec_delta("no stars in the job order",
             "ve-et ha-kokhavim")
m.spec_delta("jobs: divide, signs, festivals, days+years, shine",
             "le-memshelet (dominion) added")

# -------------------------- Gen.1.17 · INSTALL_MOUNT -----------------------
# va-yiten otam Elohim bi-rkia ha-shamayim le-ha'ir al-ha-aretz
# "And God set them in the firmament of the heaven to give light upon the
# earth."
m.step("Gen.1.17")
m.event("place", agent="Elohim", themes=["otam_ha_meorot"])

# -------------------------- Gen.1.18 · PURPOSE_RECAP_DELTA_TEST ------------
# ve-limshol ba-yom u-va-lailah u-le-havdil bein ha-or u-vein ha-choshekh
# va-yar Elohim ki-tov
# "And to rule over the day and over the night, and to divide the light from
# the darkness; and God saw that it was good."
m.step("Gen.1.18")
m.spec_delta("le-havdil bein ha-YOM u-vein ha-LAILAH (registry labels, 1:14)",
             "u-le-havdil bein ha-OR u-vein ha-CHOSHEKH (the entities, 1:18)")
m.test("PASS", "tov", "meorot")

# -------------------------- Gen.1.19 · COMMIT_DAY --------------------------
# va-yehi erev va-yehi voqer yom revi'i
# "And there was evening and there was morning, a fourth day."
m.step("Gen.1.19")
m.commit(4, label_form="ordinal", label_translit="yom revii")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'meorot', 'kokhavim', 'maor_qaton', 'maor_gadol'}
    assert m.presupposed_set() == {'shamayim', 'aretz', 'raqia'}
    assert m.REGISTRY["names"] == {'maor_gadol': 'memshelet_yom', 'maor_qaton': 'memshelet_lailah'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'tov', 'meorot')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == [4]
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 4}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
