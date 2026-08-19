#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיֹּאמֶר אֱלֹהִים יְהִי רָקִיעַ בְּתוֹךְ הַמָּיִם וִיהִי מַבְדִּיל בֵּין
# מַיִם לָמָיִם
# "And God said: 'Let there be a firmament in the midst of the waters, and
# let it divide the waters from the waters.'"
m.step("Gen.1.6")
# ‹יְהִי רָקִיעַ› (“let-there-be firmament”) — God speaks a demand — LET:
# exists(firmament)
m.declare("Elohim", "LET",
          "exists(raqia)")
# ‹וִיהִי מַבְדִּיל› (“and-let-it-be dividing”) — God speaks a demand —
# LET?: dividing(firmament, waters|waters)
m.declare("Elohim", "LET?",
          "mavdil(raqia, mayim|mayim)")
# ‹מַבְדִּיל› (“dividing”) — standing constraint: dividing(firmament,
# waters|waters)
m.invariant("mavdil(raqia, mayim|mayim)")
# reads without prior install (flag, not fix): waters
m.presupposed("mayim")

# -------------------------- Gen.1.7 · BUILD_DIVIDE_RESULT ------------------
# וַיַּעַשׂ אֱלֹהִים אֶת־הָרָקִיעַ וַיַּבְדֵּל בֵּין הַמַּיִם אֲשֶׁר
# מִתַּחַת לָרָקִיעַ וּבֵין הַמַּיִם אֲשֶׁר מֵעַל לָרָקִיעַ וַיְהִי־כֵן
# "And God made the firmament, and divided the waters which were under the
# firmament from the waters which were above the firmament; and it was so."
m.step("Gen.1.7")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת־הָרָקִיעַ› (“and-made God obj-marker the-
# firmament”) — event: make — agent God; theme firmament
m.event("make", agent="Elohim", themes=["raqia"])
# ‹בֵּין הַמַּיִם … וּבֵין הַמַּיִם› (“between the-waters … and-between the-
# waters”) — partition between mayim-under and mayim-over
m.partition("mayim-under", "mayim-over")
# ‹וַיְהִי־כֵן› (“and-there-was so”) — demand settled (popped from the
# queue): exists(firmament)
m.result("exists(raqia)", tmark="t2")
# ‹וַיַּבְדֵּל› (“and-divided”) — demand settled (popped from the queue):
# dividing(firmament, waters|waters)
m.result("mavdil(raqia, mayim|mayim)", tmark="t2")

# -------------------------- Gen.1.8 · NAME_AND_COMMIT_NO_TEST --------------
# וַיִּקְרָא אֱלֹהִים לָרָקִיעַ שָׁמָיִם וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם
# שֵׁנִי
# "And God called the firmament Heaven. And there was evening and there was
# morning, a second day."
m.step("Gen.1.8")
# ‹לָרָקִיעַ שָׁמָיִם› (“to-the-firmament Heavens”) — named: firmament :=
# Heavens
m.name("raqia", "shamayim")
# ‹יוֹם שֵׁנִי› (“day second”) — ledger: day 2 committed
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
