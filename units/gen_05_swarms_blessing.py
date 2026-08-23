#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_05_swarms_blessing — 1:20-23
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_05_swarms_blessing.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day five: swarms and the blessing — LET? demands, missing receipt, bara returns, first life, first blessing (1:20-23)"""
from machine import Machine

m = Machine("gen_05_swarms_blessing")

# -------------------------- Gen.1.20 · DECLARE_SPEC_SWARM_FLIGHT -----------
# וַיֹּאמֶר אֱלֹהִים יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ נֶפֶשׁ חַיָּה וְעוֹף
# יְעוֹפֵף עַל־הָאָרֶץ עַל־פְּנֵי רְקִיעַ הַשָּׁמָיִם
# "And God said: 'Let the waters swarm with swarms of living creatures, and
# let fowl fly above the earth in the open firmament of heaven.'"
m.step("Gen.1.20")
# utterance #7 of the ten (ma'amar census)
m.utterance(7, "fiat")
# ‹יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ נֶפֶשׁ חַיָּה› (“let-swarm the-waters swarm-of
# living-being living”) — God speaks a demand — LET?: swarm(waters),
# product=swarm-of-living-being-living
m.declare("Elohim", "LET?",
          "swarm(mayim), product=sheretz_nefesh_chaya")
# ‹וְעוֹף יְעוֹפֵף עַל־הָאָרֶץ עַל־פְּנֵי רְקִיעַ הַשָּׁמָיִם› (“and-flier
# let-fly over the-earth over face-of firmament-of the-heavens”) — God
# speaks a demand — LET?: fly(flier), loc=face-of-expanse-the-heavens
m.declare("Elohim", "LET?",
          "fly(of), loc=pnei_raqia_ha_shamayim")
# ‹יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ› (“let-swarm the-waters swarm-of”) — open
# question logged: swarm(waters), product=swarm-of-living-being-living
m.triple("swarm(mayim), product=sheretz_nefesh_chaya")
# reads without prior install (flag, not fix): waters, earth, expanse,
# heavens
m.presupposed("mayim", "aretz", "raqia", "shamayim")

# -------------------------- Gen.1.21 · BUILD_CREATE_CREDIT_DELTA_TEST ------
# וַיִּבְרָא אֱלֹהִים אֶת־הַתַּנִּינִם הַגְּדֹלִים וְאֵת כָּל־נֶפֶשׁ
# הַחַיָּה הָרֹמֶשֶׂת אֲשֶׁר שָׁרְצוּ הַמַּיִם לְמִינֵהֶם וְאֵת כָּל־עוֹף
# כָּנָף לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And God created the great sea-monsters, and every living creature that
# creepeth, wherewith the waters swarmed, after its kind, and every winged
# fowl after its kind; and God saw that it was good."
m.step("Gen.1.21")
# ‹וַיִּבְרָא אֱלֹהִים אֶת … וְאֵת … וְאֵת› (“and-created God obj-marker …
# and-obj-marker … and-obj-marker”) — event: create — agent God; theme sea-
# monsters, living-being-living-creeping, flier-wing
m.event("create", agent="Elohim", themes=["taninim", "nefesh_chaya_romeset", "of_kanaf"])
# disputed utterance — machloket carried, not decided
m.utterance_disputed("does 1:21's bara count among the ten? R. Yirmiyah: sustains it (removing Gen 2:18) — machloket ('recorded dispute') carried, never decided (amendment 2026-08-23; full dossier at ORAL_census_taninim, incl. the plene-vs-defective quote twist)")
# the world gains: sea-monsters, living-being-living-creeping, flier-wing
m.install("taninim", "nefesh_chaya_romeset", "of_kanaf")
# ‹אֲשֶׁר שָׁרְצוּ הַמַּיִם› (“which swarmed the-waters”) — demand settled
# (popped from the queue): swarm(waters), product=swarm-of-living-being-
# living
m.result("swarm(mayim), product=sheretz_nefesh_chaya", tmark="t1")
# ‹וְאֵת כָּל־עוֹף כָּנָף› (“and-obj-marker every flier wing”) — demand
# settled (popped from the queue): fly(flier), loc=face-of-expanse-the-
# heavens
m.result("fly(of), loc=pnei_raqia_ha_shamayim", tmark="t1")
# ‹יִשְׁרְצוּ הַמַּיִם ← וַיִּבְרָא אֱלֹהִים› (“swarm the-waters and-created
# God”) — spec-delta — spec said let-swarm HA-MAYIM (the waters as delegated
# producer), delivery says and-created ELOHIM (create — God executes; the
# waters credited only in the relative clause)
m.spec_delta("yishretzu HA-MAYIM (the waters as delegated producer)",
             "va-yivra ELOHIM (bara — God executes; the waters credited only in the relative clause)")
# ‹אֶת־הַתַּנִּינִם הַגְּדֹלִים› (“obj-marker the-sea-monsters the-great-
# ones”) — spec-delta — spec said no sea-monsters in the order, delivery
# says obj-marker-the-sea-monsters the-great-ones leading the inventory,
# with the week
m.spec_delta("no taninim in the order",
             "et-ha-taninim ha-gedolim leading the inventory, with the week")
# witness-grounded state (its own tier): no_propagating_pair on taninim
m.witness_state("taninim", "no_propagating_pair",
                cites=["Bereshit Rabbah 7:4", "Bava Batra 74b:5", "Bava Batra 74b:6"])
# ‹כָּל … לְמִינֵהֶם … כָּל־עוֹף כָּנָף לְמִינֵהוּ› (“every … by-their-kinds
# … every flier wing by-its-kind”) — spec-delta — spec said swarm-of living-
# being living; flier (bare classes), delivery says every- totality x2,
# kind-keys to-by-their-kinds / to-by-its-kind, flier differentiated as
# flier KANAF
m.spec_delta("sheretz nefesh chaya; of (bare classes)",
             "kol- totality x2, kind-keys le-minehem / le-minehu, of differentiated as of KANAF")
# ‹כִּי־טוֹב› (“that good”) — test PASS — oracle-word good, on living-being
m.test("PASS", "tov", "nefesh_chaya")

# -------------------------- Gen.1.22 · BLESS_MANDATE -----------------------
# וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הַמַּיִם
# בַּיַּמִּים וְהָעוֹף יִרֶב בָּאָרֶץ
# "And God blessed them, saying: 'Be fruitful, and multiply, and fill the
# waters in the seas, and let fowl multiply in the earth.'"
m.step("Gen.1.22")
# ‹וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ› (“and-blessed
# them God saying be-fruitful and-multiply and-fill”) — blessing: God
# blesses them — mandate: CMD!(peru), CMD!(revu), CMD!(milu(et-the-waters-
# in-the-yamim)), LET(yirev(ha-flier-in-the-aretz))
m.bless("Elohim", "otam", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_mayim_ba_yamim))", "LET(yirev(ha_of_ba_aretz))"])
# reads without prior install (flag, not fix): seas
m.presupposed("yamim")

# -------------------------- Gen.1.23 · COMMIT_DAY --------------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם חֲמִישִׁי
# "And there was evening and there was morning, a fifth day."
m.step("Gen.1.23")
# ‹יוֹם חֲמִישִׁי› (“day fifth”) — ledger: day 5 committed
m.commit(5, label_form="ordinal", label_translit="yom chamishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'nefesh_chaya_romeset', 'of_kanaf', 'taninim'}
    assert m.presupposed_set() == {'aretz', 'mayim', 'raqia', 'shamayim', 'yamim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tov', 'nefesh_chaya')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == [5]
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_mayim_ba_yamim))', 'mandate: LET(yirev(ha_of_ba_aretz))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    assert [(u["n"], u["mode"]) for u in m.UTTERANCES] == [(7, 'fiat')]
    assert len(m.UTTERANCES_DISPUTED) == 1
    assert sorted(m.WORLD["witnessed"]) == ['taninim']
    assert m.WORLD["witnessed"]['taninim']["cites"] == ['Bereshit Rabbah 7:4', 'Bava Batra 74b:5', 'Bava Batra 74b:6']
    assert all('no_propagating_pair' not in f for f in m.WORLD["facts"])
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
