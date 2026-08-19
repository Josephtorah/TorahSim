#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל־צְבָאָם
# "And the heaven and the earth were finished, and all the host of them."
m.step("Gen.2.1")
# ‹וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל־צְבָאָם› (“and-they-were-finished
# the-heavens and-the-earth and-all their-host”) — event: complete — theme
# heavens, earth, their-host
m.event("complete", themes=["shamayim", "aretz", "tzevaam"])
# reads without prior install (flag, not fix): heavens, earth
m.presupposed("shamayim", "aretz")

# -------------------------- Gen.2.2 · COMPLETE_CEASE -----------------------
# וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי מְלַאכְתּוֹ אֲשֶׁר עָשָׂה
# וַיִּשְׁבֹּת בַּיּוֹם הַשְּׁבִיעִי מִכָּל־מְלַאכְתּוֹ אֲשֶׁר עָשָׂה
# "And on the seventh day God finished His work which He had made; and He
# rested on the seventh day from all His work which He had made."
m.step("Gen.2.2")
# ‹וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי מְלַאכְתּוֹ› (“and-he-finished God
# on-the-day the-seventh his-work”) — event: finish — agent God
m.event("finish", agent="Elohim")
# ‹וַיִּשְׁבֹּת בַּיּוֹם הַשְּׁבִיעִי מִכָּל־מְלַאכְתּוֹ› (“and-he-ceased
# on-the-day the-seventh from-all his-work”) — event: cease — agent God
m.event("cease", agent="Elohim")

# -------------------------- Gen.2.3 · BLESS_SANCTIFY -----------------------
# וַיְבָרֶךְ אֱלֹהִים אֶת־יוֹם הַשְּׁבִיעִי וַיְקַדֵּשׁ אֹתוֹ כִּי בוֹ
# שָׁבַת מִכָּל־מְלַאכְתּוֹ אֲשֶׁר־בָּרָא אֱלֹהִים לַעֲשׂוֹת
# "And God blessed the seventh day, and hallowed it; because that in it He
# rested from all His work which God in creating had made."
m.step("Gen.2.3")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־יוֹם הַשְּׁבִיעִי› (“and-blessed God obj-marker
# day the-seventh”) — blessing: God blesses the-seventh-day
m.bless("Elohim", "yom_ha_shevii")
# ‹וַיְקַדֵּשׁ אֹתוֹ› (“and-sanctified it”) — role assigned: the-seventh-day
# -> holy
m.assign("yom_ha_shevii", "kadosh")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'aretz', 'shamayim'}
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
