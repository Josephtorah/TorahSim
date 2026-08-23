#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיֹּאמֶר אֱלֹהִים יְהִי מְאֹרֹת בִּרְקִיעַ הַשָּׁמַיִם לְהַבְדִּיל בֵּין
# הַיּוֹם וּבֵין הַלָּיְלָה וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים
# וְשָׁנִים
# "And God said: 'Let there be lights in the firmament of the heaven to
# divide the day from the night; and let them be for signs, and for seasons,
# and for days and years.'"
m.step("Gen.1.14")
# utterance #6 of the ten (ma'amar census)
m.utterance(6, "fiat")
# ‹יְהִי מְאֹרֹת› (“let-be lights”) — God speaks a demand — LET:
# exists(lights), loc=expanse-the-heavens
m.declare("Elohim", "LET",
          "exists(meorot), loc=raqia_ha_shamayim")
# ‹לְהַבְדִּיל … וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים› (“to-
# divide … and-they-shall-be for-signs and-for-seasons and-for-days and-
# years”) — open question logged: exists(lights), loc=expanse-the-heavens
m.triple("exists(meorot), loc=raqia_ha_shamayim")
# reads without prior install (flag, not fix): expanse, heavens
m.presupposed("raqia", "shamayim")

# -------------------------- Gen.1.15 · SPEC_CROSS_REGISTRY_RESULT ----------
# וְהָיוּ לִמְאוֹרֹת בִּרְקִיעַ הַשָּׁמַיִם לְהָאִיר עַל־הָאָרֶץ וַיְהִי־כֵן
# "'And let them be for lights in the firmament of the heaven to give light
# upon the earth.' And it was so."
m.step("Gen.1.15")
# reads without prior install (flag, not fix): earth
m.presupposed("aretz")
# ‹וַיְהִי־כֵן› (“and-there-was so”) — demand settled (popped from the
# queue): exists(lights), loc=expanse-the-heavens
m.result("exists(meorot), loc=raqia_ha_shamayim", tmark="t1")

# -------------------------- Gen.1.16 · BUILD_DIFFERENTIATE_DELTA -----------
# וַיַּעַשׂ אֱלֹהִים אֶת־שְׁנֵי הַמְּאֹרֹת הַגְּדֹלִים אֶת־הַמָּאוֹר
# הַגָּדֹל לְמֶמְשֶׁלֶת הַיּוֹם וְאֶת־הַמָּאוֹר הַקָּטֹן לְמֶמְשֶׁלֶת
# הַלַּיְלָה וְאֵת הַכּוֹכָבִים
# "And God made the two great lights: the greater light to rule the day, and
# the lesser light to rule the night; and the stars."
m.step("Gen.1.16")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת … אֶת … וְאֶת … וְאֵת› (“and-made God obj-marker …
# obj-marker … and-obj-marker … and-obj-marker”) — event: make — agent God;
# theme light-great, light-small, stars
m.event("make", agent="Elohim", themes=["maor_gadol", "maor_qaton", "kokhavim"])
# the world gains: light-great, light-small, stars
m.install("maor_gadol", "maor_qaton", "kokhavim")
# ‹לְמֶמְשֶׁלֶת הַיּוֹם … לְמֶמְשֶׁלֶת הַלַּיְלָה› (“for-dominion-of the-day
# … for-dominion-of the-night”) — role assigned: light-great -> dominion-of-
# day; light-small -> dominion-of-night
m.assign("maor_gadol", "memshelet_yom")
m.assign("maor_qaton", "memshelet_lailah")
# ‹הַמְּאֹרֹת הַגְּדֹלִים ← הַגָּדֹל / הַקָּטֹן› (“the-lights the-great-ones
# the-great the-small”) — spec-delta — spec said from'lights (one
# undifferentiated plural), delivery says two-of the-from
m.spec_delta("me'orot (one undifferentiated plural)",
             "shnei ha-me")
# witness-grounded state (its own tier): equal_then_diminished on maor_qaton
m.witness_state("maor_qaton", "equal_then_diminished",
                cites=["Chullin 60b:2", "Bereshit Rabbah 6:3", "Chullin 60b:3"])
# witness-grounded state (its own tier): standing_monthly on
# kapparah_chodesh
m.witness_state("kapparah_chodesh", "standing_monthly",
                cites=["Bereshit Rabbah 6:3"])
# ‹וְאֵת הַכּוֹכָבִים› (“and-obj-marker the-stars”) — spec-delta — spec said
# no stars in the job order, delivery says and-obj-marker the-stars
m.spec_delta("no stars in the job order",
             "ve-et ha-kokhavim")
# witness-grounded state (its own tier): retinue_of_maor_qaton on kokhavim
m.witness_state("kokhavim", "retinue_of_maor_qaton",
                cites=["Bereshit Rabbah 6:4"])
# ‹לְמֶמְשֶׁלֶת› (“for-dominion-of”) — spec-delta — spec said jobs: divide,
# signs, festivals, days+years, shine, delivery says to-dominion-of
# (dominion) added
m.spec_delta("jobs: divide, signs, festivals, days+years, shine",
             "le-memshelet (dominion) added")

# -------------------------- Gen.1.17 · INSTALL_MOUNT -----------------------
# וַיִּתֵּן אֹתָם אֱלֹהִים בִּרְקִיעַ הַשָּׁמָיִם לְהָאִיר עַל־הָאָרֶץ
# "And God set them in the firmament of the heaven to give light upon the
# earth."
m.step("Gen.1.17")
# ‹וַיִּתֵּן אֹתָם› (“and-set them”) — event: place — agent God; theme them-
# the-lights
m.event("place", agent="Elohim", themes=["otam_ha_meorot"])
# witness-tier presupposed read: or_ha_ganuz on or — read, not installed
m.witness_read("or", "or_ha_ganuz",
                cites=["Chagigah 12a:8"])

# -------------------------- Gen.1.18 · PURPOSE_RECAP_DELTA_TEST ------------
# וְלִמְשֹׁל בַּיּוֹם וּבַלַּיְלָה וּלְהַבְדִּיל בֵּין הָאוֹר וּבֵין
# הַחֹשֶׁךְ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And to rule over the day and over the night, and to divide the light from
# the darkness; and God saw that it was good."
m.step("Gen.1.18")
# ‹בֵּין הַיּוֹם וּבֵין הַלָּיְלָה ← בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ›
# (“between the-day and-between the-night between the-light and-between the-
# darkness”) — spec-delta — spec said to-divide between the-YOM u-between
# the-LAILAH (registry labels, 1:14), delivery says u-to-divide between the-
# OR u-between the-CHOSHEKH (the entities, 1:18)
m.spec_delta("le-havdil bein ha-YOM u-vein ha-LAILAH (registry labels, 1:14)",
             "u-le-havdil bein ha-OR u-vein ha-CHOSHEKH (the entities, 1:18)")
# ‹כִּי־טוֹב› (“that good”) — test PASS — oracle-word good, on lights
m.test("PASS", "tov", "meorot")

# -------------------------- Gen.1.19 · COMMIT_DAY --------------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם רְבִיעִי
# "And there was evening and there was morning, a fourth day."
m.step("Gen.1.19")
# ‹יוֹם רְבִיעִי› (“day fourth”) — ledger: day 4 committed
m.commit(4, label_form="ordinal", label_translit="yom revii")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'kokhavim', 'maor_gadol', 'maor_qaton', 'meorot'}
    assert m.presupposed_set() == {'aretz', 'raqia', 'shamayim'}
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
    assert [(u["n"], u["mode"]) for u in m.UTTERANCES] == [(6, 'fiat')]
    assert sorted(m.WORLD["witnessed"]) == ['kapparah_chodesh', 'kokhavim', 'maor_qaton']
    assert m.WORLD["witnessed"]['kapparah_chodesh']["cites"] == ['Bereshit Rabbah 6:3']
    assert all('standing_monthly' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['kokhavim']["cites"] == ['Bereshit Rabbah 6:4']
    assert all('retinue_of_maor_qaton' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['maor_qaton']["cites"] == ['Chullin 60b:2', 'Bereshit Rabbah 6:3', 'Chullin 60b:3']
    assert all('equal_then_diminished' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('or', 'or_ha_ganuz')]
    assert m.WITNESS_READS[0]["cites"] == ['Chagigah 12a:8']
    assert all('or_ha_ganuz' not in f for f in m.WORLD["facts"])
    assert 'or' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
