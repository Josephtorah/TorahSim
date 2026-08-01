#!/usr/bin/env python3
# =============================================================================
# gen_02_raqia_day — 1:6-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_02_raqia_day.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day two: firmament — build, divide, name; commit without test (1:6-8)"""
from machine import Machine

m = Machine("gen_02_raqia_day")

# -------------------------- Gen.1.6 · DECLARE_TWO_MOOD_SPEC ----------------
# va-yomer Elohim yehi raqia be-tokh ha-mayim vi-yhi mavdil bein mayim la-
# mayim
# "And God said: 'Let there be a firmament in the midst of the waters, and
# let it divide the waters from the waters.'"
m.step("Gen.1.6")
m.declare("Elohim", "LET",
          "exists(raqia)")
m.declare("Elohim", "LET?",
          "mavdil(raqia, mayim|mayim)")
m.invariant("mavdil(raqia, mayim|mayim)")
m.presupposed("mayim")

# -------------------------- Gen.1.7 · BUILD_DIVIDE_RESULT ------------------
# va-ya'as Elohim et-ha-raqia va-yavdel bein ha-mayim asher mi-tachat la-
# raqia u-vein ha-mayim asher me-al la-raqia va-yehi khen
# "And God made the firmament, and divided the waters which were under the
# firmament from the waters which were above the firmament; and it was so."
m.step("Gen.1.7")
m.event("make", agent="Elohim", themes=["raqia"])
m.partition("mayim-under", "mayim-over")
m.result("exists(raqia)", tmark="t2")
m.result("mavdil(raqia, mayim|mayim)", tmark="t2")

# -------------------------- Gen.1.8 · NAME_AND_COMMIT_NO_TEST --------------
# va-yiqra Elohim la-raqia shamayim va-yehi erev va-yehi voqer yom sheni
# "And God called the firmament Heaven. And there was evening and there was
# morning, a second day."
m.step("Gen.1.8")
m.name("raqia", "shamayim")
m.commit(2, label_form="ordinal", label_translit="yom sheni")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'raqia'}
    assert m.presupposed_set() == {'mayim'}
    assert m.REGISTRY["names"] == {'raqia': 'shamayim'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == [2]
    assert m.flag_counts() == {'read_before_install': 1, 'commit_without_test': 1}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == ['mavdil(raqia, mayim|mayim)']
    assert m.WORLD["partitions"] == [('mayim-under', 'mayim-over')]
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
