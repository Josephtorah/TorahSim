#!/usr/bin/env python3
# =============================================================================
# gen_03_double_build — 1:9-13
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_03_double_build.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day three: double build — gathering + vegetation; delegation; spec delta (1:9-13)"""
from machine import Machine

m = Machine("gen_03_double_build")

# -------------------------- Gen.1.9 · DECLARE_AGENTLESS_RESULT -------------
# va-yomer Elohim yiqqavu ha-mayim mi-tachat ha-shamayim el-maqom echad ve-
# tera'e ha-yabasha va-yehi khen
# "And God said: 'Let the waters under the heaven be gathered together unto
# one place, and let the dry land appear.' And it was so."
m.step("Gen.1.9")
m.declare("Elohim", "LET",
          "gathered(mayim, to=maqom-echad)")
m.declare("Elohim", "LET?",
          "exists(yabasha)")
m.presupposed("mayim", "shamayim")
m.result("gathered(mayim, to=maqom-echad)", tmark="t1")
m.result("exists(yabasha)", tmark="t1")

# -------------------------- Gen.1.10 · NAME_NAME_TEST ----------------------
# va-yiqra Elohim la-yabasha eretz u-le-miqveh ha-mayim qara yamim va-yar
# Elohim ki-tov
# "And God called the dry land Earth, and the gathering together of the
# waters called He Seas; and God saw that it was good."
m.step("Gen.1.10")
m.name("yabasha", "eretz")
m.name("miqveh-ha-mayim", "yamim")
m.test("PASS", "tov", "gathering")

# -------------------------- Gen.1.11 · DECLARE_DELEGATED_SPEC --------------
# va-yomer Elohim tadshe ha-aretz deshe esev mazria zera etz peri oseh peri
# le-mino asher zar'o-vo al-ha-aretz va-yehi khen
# "And God said: 'Let the earth put forth grass, herb yielding seed, and
# fruit-tree bearing fruit after its kind, wherein is the seed thereof, upon
# the earth.' And it was so."
m.step("Gen.1.11")
m.declare("Elohim", "LET",
          "sprout(aretz, vegetation)")
m.invariant("mazria(esev, zera) ∧ oseh(etz, peri) ∧ le-mino(reproduction)")
m.result("sprout(aretz, vegetation)", tmark="t2")

# -------------------------- Gen.1.12 · DELEGATED_BUILD_DELTA_TEST ----------
# va-totze ha-aretz deshe esev mazria zera le-minehu ve-etz oseh-peri asher
# zar'o-vo le-minehu va-yar Elohim ki-tov
# "And the earth brought forth grass, herb yielding seed after its kind, and
# tree bearing fruit, wherein is the seed thereof, after its kind; and God
# saw that it was good."
m.step("Gen.1.12")
m.event("?", agent="aretz", themes=["deshe"])
m.install("deshe")
m.spec_delta("etz peri oseh peri",
             "etz oseh peri")
m.spec_delta("esev mazria zera",
             "esev mazria zera le-minehu")
m.test("PASS", "tov", "vegetation")

# -------------------------- Gen.1.13 · COMMIT_DOUBLE_DAY -------------------
# va-yehi erev va-yehi voqer yom shelishi
# "And there was evening and there was morning, a third day."
m.step("Gen.1.13")
m.commit(3, label_form="ordinal", label_translit="yom shelishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'deshe', 'yabasha'}
    assert m.presupposed_set() == {'shamayim', 'mayim'}
    assert m.REGISTRY["names"] == {'yabasha': 'eretz', 'miqveh-ha-mayim': 'yamim'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'tov', 'gathering'), ('PASS', 'tov', 'vegetation')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == [3]
    assert m.flag_counts() == {'read_before_install': 2, 'named_before_any_presence': 1, 'spec_delta': 2}
    assert sorted(m.WORLD["facts"]) == sorted([])
    assert m.WORLD["invariants"] == ['mazria(esev, zera) ∧ oseh(etz, peri) ∧ le-mino(reproduction)']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
