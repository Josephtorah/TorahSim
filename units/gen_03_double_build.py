#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיֹּאמֶר אֱלֹהִים יִקָּווּ הַמַּיִם מִתַּחַת הַשָּׁמַיִם אֶל־מָקוֹם אֶחָד
# וְתֵרָאֶה הַיַּבָּשָׁה וַיְהִי־כֵן
# "And God said: 'Let the waters under the heaven be gathered together unto
# one place, and let the dry land appear.' And it was so."
m.step("Gen.1.9")
# ‹יִקָּווּ הַמַּיִם› (“be-gathered the-waters”) — God speaks a demand —
# LET: gathered(waters, to=place-one)
m.declare("Elohim", "LET",
          "gathered(mayim, to=maqom-echad)")
# ‹וְתֵרָאֶה הַיַּבָּשָׁה› (“and-let-appear the-dry-land”) — God speaks a
# demand — LET?: exists(dry-land)
m.declare("Elohim", "LET?",
          "exists(yabasha)")
# reads without prior install (flag, not fix): waters, heavens
m.presupposed("mayim", "shamayim")
# ‹וַיְהִי־כֵן› (“and-there-was so”) — demand settled (popped from the
# queue): gathered(waters, to=place-one)
m.result("gathered(mayim, to=maqom-echad)", tmark="t1")
# ‹הַיַּבָּשָׁה› (“the-dry-land”) — demand settled (popped from the queue):
# exists(dry-land)
m.result("exists(yabasha)", tmark="t1")

# -------------------------- Gen.1.10 · NAME_NAME_TEST ----------------------
# וַיִּקְרָא אֱלֹהִים לַיַּבָּשָׁה אֶרֶץ וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים
# וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And God called the dry land Earth, and the gathering together of the
# waters called He Seas; and God saw that it was good."
m.step("Gen.1.10")
# ‹לַיַּבָּשָׁה אֶרֶץ … קָרָא יַמִּים› (“to-the-dry-land Earth … called
# Seas”) — named: dry-land := Earth; miqveh-ha-mayim := Seas
m.name("yabasha", "eretz")
m.name("miqveh-ha-mayim", "yamim")
# ‹כִּי־טוֹב› (“that good”) — test PASS — oracle-word good, on gathering
m.test("PASS", "tov", "gathering")

# -------------------------- Gen.1.11 · DECLARE_DELEGATED_SPEC --------------
# וַיֹּאמֶר אֱלֹהִים תַּדְשֵׁא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע עֵץ
# פְּרִי עֹשֶׂה פְּרִי לְמִינוֹ אֲשֶׁר זַרְעוֹ־בוֹ עַל־הָאָרֶץ וַיְהִי־כֵן
# "And God said: 'Let the earth put forth grass, herb yielding seed, and
# fruit-tree bearing fruit after its kind, wherein is the seed thereof, upon
# the earth.' And it was so."
m.step("Gen.1.11")
# ‹תַּדְשֵׁא הָאָרֶץ› (“let-sprout the-earth”) — God speaks a demand — LET:
# sprout(earth, vegetation)
m.declare("Elohim", "LET",
          "sprout(aretz, vegetation)")
# ‹מַזְרִיעַ זֶרַע … עֹשֶׂה פְּרִי לְמִינוֹ› (“yielding-seed seed … making
# fruit by-its-kind”) — standing constraint: yielding-seed(herb, seed) ∧
# making(tree, fruit) ∧ to-by-its-kind(reproduction)
m.invariant("mazria(esev, zera) ∧ oseh(etz, peri) ∧ le-mino(reproduction)")
# ‹וַיְהִי־כֵן› (“and-there-was so”) — demand settled (popped from the
# queue): sprout(earth, vegetation)
m.result("sprout(aretz, vegetation)", tmark="t2")

# -------------------------- Gen.1.12 · DELEGATED_BUILD_DELTA_TEST ----------
# וַתּוֹצֵא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע לְמִינֵהוּ וְעֵץ
# עֹשֶׂה־פְּרִי אֲשֶׁר זַרְעוֹ־בוֹ לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And the earth brought forth grass, herb yielding seed after its kind, and
# tree bearing fruit, wherein is the seed thereof, after its kind; and God
# saw that it was good."
m.step("Gen.1.12")
# ‹וַתּוֹצֵא הָאָרֶץ› (“and-brought-forth the-earth”) — event: ? — agent
# earth; theme grass
m.event("?", agent="aretz", themes=["deshe"])
# the world gains: grass
m.install("deshe")
# ‹עֵץ פְּרִי עֹשֶׂה פְּרִי ← וְעֵץ עֹשֶׂה־פְּרִי› (“tree fruit making fruit
# and-tree making fruit”) — spec-delta — spec said tree fruit making fruit,
# delivery says tree making fruit
m.spec_delta("etz peri oseh peri",
             "etz oseh peri")
# ‹עֵשֶׂב מַזְרִיעַ זֶרַע ← עֵשֶׂב מַזְרִיעַ זֶרַע לְמִינֵהוּ› (“herb
# yielding-seed seed herb yielding-seed seed by-its-kind”) — spec-delta —
# spec said herb yielding-seed seed, delivery says herb yielding-seed seed
# to-by-its-kind
m.spec_delta("esev mazria zera",
             "esev mazria zera le-minehu")
# ‹כִּי־טוֹב› (“that good”) — test PASS — oracle-word good, on vegetation
m.test("PASS", "tov", "vegetation")

# -------------------------- Gen.1.13 · COMMIT_DOUBLE_DAY -------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם שְׁלִישִׁי
# "And there was evening and there was morning, a third day."
m.step("Gen.1.13")
# ‹יוֹם שְׁלִישִׁי› (“day third”) — ledger: day 3 committed
m.commit(3, label_form="ordinal", label_translit="yom shelishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'deshe', 'yabasha'}
    assert m.presupposed_set() == {'mayim', 'shamayim'}
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
