#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
# "[EN-AID] In the beginning God created the heavens and the earth."
m.step("Gen.1.1")
# clock anchored: t0 := beginning
m.time_anchor("reshit")
# ‹אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ› (“obj-marker the-heavens and-obj-marker
# the-earth”) — event: create — agent God; theme heavens, earth
m.event("create", agent="Elohim", themes=["shamayim", "aretz"])
# the world gains: heavens, earth
m.install("shamayim", "aretz")
# utterance #1 of the ten (ma'amar census)
m.utterance(1, "bulk-create")

# -------------------------- Gen.1.2 · STATE_BLOCK --------------------------
# וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ
# אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם
# "[EN-AID] The earth was formless and void, darkness over the deep, God's
# spirit hovering over the waters."
m.step("Gen.1.2")
# fact holds: formless(earth) ∧ void(earth); over(darkness, face(deep))
m.fact("tohu(aretz) ∧ vohu(aretz)",
       "over(choshekh, face(tehom))")
# ‹מְרַחֶפֶת› (“hovering”) — standing constraint: hover(spirit-God,
# face(waters))
m.invariant("hover(ruach-Elohim, face(mayim))")
# note: zero events in this verse
m.note_zero_events()
# reads without prior install (flag, not fix): darkness, deep, waters,
# spirit
m.presupposed("choshekh", "tehom", "mayim", "ruach")
# disputed utterance — machloket carried, not decided
m.utterance_disputed("is ruach ('wind/spirit') the tenth utterance? R. Yaakov ben Kurshai: counts; Menachem bar Yosei: Gen 2:18 instead — machloket ('recorded dispute') carried, never decided (amendment 2026-08-20)")

# -------------------------- Gen.1.3 · DECLARE_LET_RESULT -------------------
# וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי־אוֹר
# "[EN-AID] God said: let there be light — and there was light."
m.step("Gen.1.3")
# utterance #2 of the ten (ma'amar census)
m.utterance(2, "fiat")
# ‹יְהִי אוֹר› (“let-there-be light”) — God speaks a demand — LET:
# exists(light)
m.declare("Elohim", "LET",
          "exists(or)")
# open question logged: exists(light)
m.triple("exists(or)")
# ‹וַיְהִי־אוֹר› (“and-there-was light”) — demand settled (popped from the
# queue): exists(light)
m.result("exists(or)", tmark="t1")

# -------------------------- Gen.1.4 · TEST_AND_PARTITION -------------------
# וַיַּרְא אֱלֹהִים אֶת־הָאוֹר כִּי־טוֹב וַיַּבְדֵּל אֱלֹהִים בֵּין הָאוֹר
# וּבֵין הַחֹשֶׁךְ
# "[EN-AID] God saw the light, that it was good; and God divided the light
# from the darkness."
m.step("Gen.1.4")
# ‹כִּי־טוֹב› (“that good”) — test PASS — oracle-word good, on light
m.test("PASS", "tov", "or")
# ‹בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ› (“between the-light and-between the-
# darkness”) — partition between light and darkness
m.partition("or", "choshekh")
# witness-grounded state (its own tier): or_ha_ganuz on or
m.witness_state("or", "or_ha_ganuz",
                cites=["Bereshit Rabbah 3:6", "Chagigah 12a:10"])

# -------------------------- Gen.1.5 · NAME_AND_COMMIT ----------------------
# וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי־עֶרֶב
# וַיְהִי־בֹקֶר יוֹם אֶחָד
# "[EN-AID] God called the light Day and the darkness Night; evening,
# morning — day one."
m.step("Gen.1.5")
# ‹לָאוֹר יוֹם … וְלַחֹשֶׁךְ … לָיְלָה› (“to-the-light Day … and-to-the-
# darkness … Night”) — named: light := Day; darkness := Night
m.name("or", "yom")
m.name("choshekh", "layla")
# ‹יוֹם אֶחָד› (“Day one”) — ledger: day 1 committed
m.commit(1, label_form="cardinal", label_translit="yom echad")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'aretz', 'or', 'shamayim'}
    assert m.presupposed_set() == {'choshekh', 'mayim', 'ruach', 'tehom'}
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
    assert [(u["n"], u["mode"]) for u in m.UTTERANCES] == [(1, 'bulk-create'), (2, 'fiat')]
    assert len(m.UTTERANCES_DISPUTED) == 1
    assert sorted(m.WORLD["witnessed"]) == ['or']
    assert m.WORLD["witnessed"]['or']["cites"] == ['Bereshit Rabbah 3:6', 'Chagigah 12a:10']
    assert all('or_ha_ganuz' not in f for f in m.WORLD["facts"])
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
