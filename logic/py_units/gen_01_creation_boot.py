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
# ‹בְּרֵאשִׁית בָּרָא אֱלֹהִים› (“in-beginning created God”)
# ‹אֵת הַשָּׁמַיִם וְאֵת› (“obj-marker the-heavens and-obj-marker”)
# ‹הָאָרֶץ› (“the-earth”)
# "[EN-AID] In the beginning God created the heavens and the earth."
m.step("Gen.1.1")
# clock anchored: t0 := beginning
m.time_anchor("reshit")
# ‹אֵת הַשָּׁמַיִם וְאֵת› (“obj-marker the-heavens and-obj-marker”)
# ‹הָאָרֶץ› (“the-earth”)
# — event: create — agent God; theme heavens, earth
m.event("create", agent="Elohim", themes=["shamayim", "aretz"])
# the world gains: heavens, earth
m.install("shamayim", "aretz")
# utterance #1 of the ten (ma'amar census)
m.utterance(1, "bulk-create")

# -------------------------- Gen.1.2 · STATE_BLOCK --------------------------
# ‹וְהָאָרֶץ הָיְתָה תֹהוּ› (“and-the-earth was formless”)
# ‹וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי› (“and-void and-darkness over face-of”)
# ‹תְהוֹם וְרוּחַ אֱלֹהִים› (“deep and-spirit God”)
# ‹מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם› (“hovering over face-of the-waters”)
# "[EN-AID] The earth was formless and void, darkness over the deep, God's
# spirit hovering over the waters."
m.step("Gen.1.2")
# fact holds: formless(earth) ∧ void(earth); over(darkness, face(deep))
m.fact("tohu(aretz) ∧ vohu(aretz)",
       "over(choshekh, face(tehom))")
# ‹מְרַחֶפֶת› (“hovering”)
# — standing constraint: hover(spirit-God, face(waters))
m.invariant("hover(ruach-Elohim, face(mayim))")
# note: zero events in this verse
m.note_zero_events()
# reads without prior install (flag, not fix): darkness, deep, waters,
# spirit
m.presupposed("choshekh", "tehom", "mayim", "ruach")
# disputed utterance — machloket carried, not decided
m.utterance_disputed("is ruach ('wind/spirit') the tenth utterance? R. Yaakov ben Kurshai: counts; Menachem bar Yosei: Gen 2:18 instead — machloket ('recorded dispute') carried, never decided (amendment 2026-08-20)")

# -------------------------- Gen.1.3 · DECLARE_LET_RESULT -------------------
# ‹וַיֹּאמֶר אֱלֹהִים יְהִי› (“and-said God let-there-be”)
# ‹אוֹר וַיְהִי־אוֹר› (“light and-there-was light”)
# "[EN-AID] God said: let there be light — and there was light."
m.step("Gen.1.3")
# utterance #2 of the ten (ma'amar census)
m.utterance(2, "fiat")
# ‹יְהִי אוֹר› (“let-there-be light”)
# — God speaks a demand — LET: exists(light)
m.declare("Elohim", "LET",
          "exists(or)")
# open question logged: exists(light)
m.triple("exists(or)")
# ‹וַיְהִי־אוֹר› (“and-there-was light”)
# — demand settled (popped from the queue): exists(light)
m.result("exists(or)", tmark="t1")

# -------------------------- Gen.1.4 · TEST_AND_PARTITION -------------------
# ‹וַיַּרְא אֱלֹהִים אֶת־הָאוֹר› (“and-saw God obj-marker the-light”)
# ‹כִּי־טוֹב וַיַּבְדֵּל אֱלֹהִים› (“that good and-divided God”)
# ‹בֵּין הָאוֹר וּבֵין› (“between the-light and-between”)
# ‹הַחֹשֶׁךְ› (“the-darkness”)
# "[EN-AID] God saw the light, that it was good; and God divided the light
# from the darkness."
m.step("Gen.1.4")
# ‹כִּי־טוֹב› (“that good”)
# — test PASS — oracle-word good, on light
m.test("PASS", "tov", "or")
# ‹בֵּין הָאוֹר וּבֵין› (“between the-light and-between”)
# ‹הַחֹשֶׁךְ› (“the-darkness”)
# — partition between light and darkness
m.partition("or", "choshekh")
# witness-grounded state (its own tier): or_ha_ganuz on or
m.witness_state("or", "or_ha_ganuz",
                cites=["Bereshit Rabbah 3:6", "Chagigah 12a:10"])

# -------------------------- Gen.1.5 · NAME_AND_COMMIT ----------------------
# ‹וַיִּקְרָא אֱלֹהִים לָאוֹר› (“and-called God to-the-light”)
# ‹יוֹם וְלַחֹשֶׁךְ קָרָא› (“Day and-to-the-darkness called”)
# ‹לָיְלָה וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר› (“Night and-there-was evening and-
# there-was morning”)
# ‹יוֹם אֶחָד› (“Day one”)
# "[EN-AID] God called the light Day and the darkness Night; evening,
# morning — day one."
m.step("Gen.1.5")
# ‹לָאוֹר יוֹם … וְלַחֹשֶׁךְ› (“to-the-light Day … and-to-the-darkness”)
# ‹… לָיְלָה› (“Night”)
# — named: light := Day; darkness := Night
m.name("or", "yom")
m.name("choshekh", "layla")
# ‹יוֹם אֶחָד› (“Day one”)
# — ledger: day 1 committed
m.commit(1, label_form="cardinal", label_translit="yom echad")
# witness-tier presupposed read: day_boundary_liturgy_jobs on
# va_yehi_erev_va_yehi_voqer — read, not installed
m.witness_read("va_yehi_erev_va_yehi_voqer", "day_boundary_liturgy_jobs",
                cites=["Berakhot 2a:8", "Berakhot 2a:9", "Berakhot 2a:10", "Berakhot 26a:16", "Berakhot 26a:17", "Berakhot 26a:18"])
# witness-tier presupposed read:
# the_day_boundary_and_the_sabbaths_three_seats_compiled_cold on
# the_creation_chapter_as_the_first_spec_run_pair — read, not installed
m.witness_read("the_creation_chapter_as_the_first_spec_run_pair", "the_day_boundary_and_the_sabbaths_three_seats_compiled_cold",
                cites=["Mishnah Berakhot 1:1", "Mishnah Chullin 5:5", "Mishnah Taanit 4:2", "Mishnah Taanit 4:3", "Mishnah Tamid 7:4", "Mishnah Chagigah 2:1", "Mishnah Avot 5:1", "Mishnah Mikvaot 5:4", "Mishnah Nedarim 10:8", "Mishnah Shabbat 19:5", "Mishnah Nedarim 3:10", "Mishnah Megillah 3:6", "Megillah 21b:10", "Rosh Hashanah 32a:18", "Chagigah 12a:5", "Chagigah 12a:6", "Chagigah 12a:10", "Chagigah 12a:16", "Chagigah 12a:20", "Tamid 32a:3", "Megillah 9a:12", "Megillah 9a:13", "Shabbat 88a:6", "Avodah Zarah 5a:12", "Avodah Zarah 3a:6", "Chullin 60b:2", "Chullin 60b:3", "Chullin 60b:4", "Chullin 60a:9", "Chullin 60a:10", "Chullin 60a:11", "Chullin 60a:12", "Chullin 27b:11", "Rosh Hashanah 11a:3", "Rosh Hashanah 11a:4", "Rosh Hashanah 11a:5", "Rosh Hashanah 11a:6", "Pesachim 54a:13", "Sanhedrin 38b:14", "Ketubot 8a:9", "Eruvin 18a:23", "Berakhot 61a:14", "Megillah 22a:2", "Taanit 27b:10", "Taanit 26a:7", "Taanit 27b:3", "Megillah 20b:2", "Megillah 20b:3", "Megillah 10b:8", "Pesachim 2a:3", "Shabbat 119b:2", "Shabbat 10a:5", "Nazir 7a:10", "Pesachim 88a:5", "Yevamot 65b:4", "Kiddushin 35a:2", "Bava Kamma 55a:12", "Beitzah 16a:12", "Rosh Hashanah 31a:2", "Rosh Hashanah 31a:5", "Sukkah 49a:2", "Berakhot 2a:9", "Chullin 83a:15", "Shabbat 109a:9"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('va_yehi_erev_va_yehi_voqer', 'day_boundary_liturgy_jobs'), ('the_creation_chapter_as_the_first_spec_run_pair', 'the_day_boundary_and_the_sabbaths_three_seats_compiled_cold')]
    assert m.WITNESS_READS[0]["cites"] == ['Berakhot 2a:8', 'Berakhot 2a:9', 'Berakhot 2a:10', 'Berakhot 26a:16', 'Berakhot 26a:17', 'Berakhot 26a:18']
    assert all('day_boundary_liturgy_jobs' not in f for f in m.WORLD["facts"])
    assert 'va_yehi_erev_va_yehi_voqer' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Mishnah Berakhot 1:1', 'Mishnah Chullin 5:5', 'Mishnah Taanit 4:2', 'Mishnah Taanit 4:3', 'Mishnah Tamid 7:4', 'Mishnah Chagigah 2:1', 'Mishnah Avot 5:1', 'Mishnah Mikvaot 5:4', 'Mishnah Nedarim 10:8', 'Mishnah Shabbat 19:5', 'Mishnah Nedarim 3:10', 'Mishnah Megillah 3:6', 'Megillah 21b:10', 'Rosh Hashanah 32a:18', 'Chagigah 12a:5', 'Chagigah 12a:6', 'Chagigah 12a:10', 'Chagigah 12a:16', 'Chagigah 12a:20', 'Tamid 32a:3', 'Megillah 9a:12', 'Megillah 9a:13', 'Shabbat 88a:6', 'Avodah Zarah 5a:12', 'Avodah Zarah 3a:6', 'Chullin 60b:2', 'Chullin 60b:3', 'Chullin 60b:4', 'Chullin 60a:9', 'Chullin 60a:10', 'Chullin 60a:11', 'Chullin 60a:12', 'Chullin 27b:11', 'Rosh Hashanah 11a:3', 'Rosh Hashanah 11a:4', 'Rosh Hashanah 11a:5', 'Rosh Hashanah 11a:6', 'Pesachim 54a:13', 'Sanhedrin 38b:14', 'Ketubot 8a:9', 'Eruvin 18a:23', 'Berakhot 61a:14', 'Megillah 22a:2', 'Taanit 27b:10', 'Taanit 26a:7', 'Taanit 27b:3', 'Megillah 20b:2', 'Megillah 20b:3', 'Megillah 10b:8', 'Pesachim 2a:3', 'Shabbat 119b:2', 'Shabbat 10a:5', 'Nazir 7a:10', 'Pesachim 88a:5', 'Yevamot 65b:4', 'Kiddushin 35a:2', 'Bava Kamma 55a:12', 'Beitzah 16a:12', 'Rosh Hashanah 31a:2', 'Rosh Hashanah 31a:5', 'Sukkah 49a:2', 'Berakhot 2a:9', 'Chullin 83a:15', 'Shabbat 109a:9']
    assert all('the_day_boundary_and_the_sabbaths_three_seats_compiled_cold' not in f for f in m.WORLD["facts"])
    assert 'the_creation_chapter_as_the_first_spec_run_pair' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
