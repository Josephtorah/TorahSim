#!/usr/bin/env python3
"""ALL_UNITS.py — frozen only (gen_43 re-frozen 2026-08-06; amendment wave complete; 46 frozen)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))


###############################################################################
# UNIT: gen_01_creation_boot
###############################################################################
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
# ‹אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ› event: create — agent God; theme heavens,
# earth
m.event("create", agent="Elohim", themes=["shamayim", "aretz"])
# the world gains: heavens, earth
m.install("shamayim", "aretz")

# -------------------------- Gen.1.2 · STATE_BLOCK --------------------------
# וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ
# אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם
# "[EN-AID] The earth was formless and void, darkness over the deep, God's
# spirit hovering over the waters."
m.step("Gen.1.2")
# fact holds: formless(earth) ∧ void(earth); over(darkness, face(deep))
m.fact("tohu(aretz) ∧ vohu(aretz)",
       "over(choshekh, face(tehom))")
# ‹מְרַחֶפֶת› standing constraint: hover(spirit-God, face(waters))
m.invariant("hover(ruach-Elohim, face(mayim))")
# note: zero events in this verse
m.note_zero_events()
# reads without prior install (flag, not fix): darkness, deep, waters,
# spirit
m.presupposed("choshekh", "tehom", "mayim", "ruach")

# -------------------------- Gen.1.3 · DECLARE_LET_RESULT -------------------
# וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי־אוֹר
# "[EN-AID] God said: let there be light — and there was light."
m.step("Gen.1.3")
# ‹יְהִי אוֹר› God speaks a demand — LET: exists(light)
m.declare("Elohim", "LET",
          "exists(or)")
# open question logged: exists(light)
m.triple("exists(or)")
# ‹וַיְהִי־אוֹר› demand settled (popped from the queue): exists(light)
m.result("exists(or)", tmark="t1")

# -------------------------- Gen.1.4 · TEST_AND_PARTITION -------------------
# וַיַּרְא אֱלֹהִים אֶת־הָאוֹר כִּי־טוֹב וַיַּבְדֵּל אֱלֹהִים בֵּין הָאוֹר
# וּבֵין הַחֹשֶׁךְ
# "[EN-AID] God saw the light, that it was good; and God divided the light
# from the darkness."
m.step("Gen.1.4")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on light
m.test("PASS", "tov", "or")
# ‹בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ› partition between light and darkness
m.partition("or", "choshekh")

# -------------------------- Gen.1.5 · NAME_AND_COMMIT ----------------------
# וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי־עֶרֶב
# וַיְהִי־בֹקֶר יוֹם אֶחָד
# "[EN-AID] God called the light Day and the darkness Night; evening,
# morning — day one."
m.step("Gen.1.5")
# ‹לָאוֹר יוֹם … וְלַחֹשֶׁךְ … לָיְלָה› named: light := Day; darkness :=
# Night
m.name("or", "yom")
m.name("choshekh", "layla")
# ‹יוֹם אֶחָד› ledger: day 1 committed
m.commit(1, label_form="cardinal", label_translit="yom echad")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'aretz', 'or', 'shamayim'}
    assert m.presupposed_set() == {'mayim', 'ruach', 'tehom', 'choshekh'}
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_02_raqia_day
###############################################################################
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
# ‹יְהִי רָקִיעַ› God speaks a demand — LET: exists(firmament)
m.declare("Elohim", "LET",
          "exists(raqia)")
# ‹וִיהִי מַבְדִּיל› God speaks a demand — LET?: dividing(firmament,
# waters|waters)
m.declare("Elohim", "LET?",
          "mavdil(raqia, mayim|mayim)")
# ‹מַבְדִּיל› standing constraint: dividing(firmament, waters|waters)
m.invariant("mavdil(raqia, mayim|mayim)")
# reads without prior install (flag, not fix): waters
m.presupposed("mayim")

# -------------------------- Gen.1.7 · BUILD_DIVIDE_RESULT ------------------
# וַיַּעַשׂ אֱלֹהִים אֶת־הָרָקִיעַ וַיַּבְדֵּל בֵּין הַמַּיִם אֲשֶׁר
# מִתַּחַת לָרָקִיעַ וּבֵין הַמַּיִם אֲשֶׁר מֵעַל לָרָקִיעַ וַיְהִי־כֵן
# "And God made the firmament, and divided the waters which were under the
# firmament from the waters which were above the firmament; and it was so."
m.step("Gen.1.7")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת־הָרָקִיעַ› event: make — agent God; theme
# firmament
m.event("make", agent="Elohim", themes=["raqia"])
# ‹בֵּין הַמַּיִם … וּבֵין הַמַּיִם› partition between mayim-under and
# mayim-over
m.partition("mayim-under", "mayim-over")
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): exists(firmament)
m.result("exists(raqia)", tmark="t2")
# ‹וַיַּבְדֵּל› demand settled (popped from the queue): dividing(firmament,
# waters|waters)
m.result("mavdil(raqia, mayim|mayim)", tmark="t2")

# -------------------------- Gen.1.8 · NAME_AND_COMMIT_NO_TEST --------------
# וַיִּקְרָא אֱלֹהִים לָרָקִיעַ שָׁמָיִם וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם
# שֵׁנִי
# "And God called the firmament Heaven. And there was evening and there was
# morning, a second day."
m.step("Gen.1.8")
# ‹לָרָקִיעַ שָׁמָיִם› named: firmament := Heavens
m.name("raqia", "shamayim")
# ‹יוֹם שֵׁנִי› ledger: day 2 committed
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

###############################################################################
# UNIT: gen_03_double_build
###############################################################################
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
# ‹יִקָּווּ הַמַּיִם› God speaks a demand — LET: gathered(waters, to=place-
# one)
m.declare("Elohim", "LET",
          "gathered(mayim, to=maqom-echad)")
# ‹וְתֵרָאֶה הַיַּבָּשָׁה› God speaks a demand — LET?: exists(dry-land)
m.declare("Elohim", "LET?",
          "exists(yabasha)")
# reads without prior install (flag, not fix): waters, heavens
m.presupposed("mayim", "shamayim")
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): gathered(waters,
# to=place-one)
m.result("gathered(mayim, to=maqom-echad)", tmark="t1")
# ‹הַיַּבָּשָׁה› demand settled (popped from the queue): exists(dry-land)
m.result("exists(yabasha)", tmark="t1")

# -------------------------- Gen.1.10 · NAME_NAME_TEST ----------------------
# וַיִּקְרָא אֱלֹהִים לַיַּבָּשָׁה אֶרֶץ וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים
# וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And God called the dry land Earth, and the gathering together of the
# waters called He Seas; and God saw that it was good."
m.step("Gen.1.10")
# ‹לַיַּבָּשָׁה אֶרֶץ … קָרָא יַמִּים› named: dry-land := Earth; miqveh-ha-
# mayim := Seas
m.name("yabasha", "eretz")
m.name("miqveh-ha-mayim", "yamim")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on gathering
m.test("PASS", "tov", "gathering")

# -------------------------- Gen.1.11 · DECLARE_DELEGATED_SPEC --------------
# וַיֹּאמֶר אֱלֹהִים תַּדְשֵׁא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע עֵץ
# פְּרִי עֹשֶׂה פְּרִי לְמִינוֹ אֲשֶׁר זַרְעוֹ־בוֹ עַל־הָאָרֶץ וַיְהִי־כֵן
# "And God said: 'Let the earth put forth grass, herb yielding seed, and
# fruit-tree bearing fruit after its kind, wherein is the seed thereof, upon
# the earth.' And it was so."
m.step("Gen.1.11")
# ‹תַּדְשֵׁא הָאָרֶץ› God speaks a demand — LET: sprout(earth, vegetation)
m.declare("Elohim", "LET",
          "sprout(aretz, vegetation)")
# ‹מַזְרִיעַ זֶרַע … עֹשֶׂה פְּרִי לְמִינוֹ› standing constraint: yielding-
# seed(herb, seed) ∧ making(tree, fruit) ∧ to-by-its-kind(reproduction)
m.invariant("mazria(esev, zera) ∧ oseh(etz, peri) ∧ le-mino(reproduction)")
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): sprout(earth,
# vegetation)
m.result("sprout(aretz, vegetation)", tmark="t2")

# -------------------------- Gen.1.12 · DELEGATED_BUILD_DELTA_TEST ----------
# וַתּוֹצֵא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע לְמִינֵהוּ וְעֵץ
# עֹשֶׂה־פְּרִי אֲשֶׁר זַרְעוֹ־בוֹ לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And the earth brought forth grass, herb yielding seed after its kind, and
# tree bearing fruit, wherein is the seed thereof, after its kind; and God
# saw that it was good."
m.step("Gen.1.12")
# ‹וַתּוֹצֵא הָאָרֶץ› event: ? — agent earth; theme grass
m.event("?", agent="aretz", themes=["deshe"])
# the world gains: grass
m.install("deshe")
# ‹עֵץ פְּרִי עֹשֶׂה פְּרִי ← וְעֵץ עֹשֶׂה־פְּרִי› spec-delta — spec said
# tree fruit making fruit, delivery says tree making fruit
m.spec_delta("etz peri oseh peri",
             "etz oseh peri")
# ‹עֵשֶׂב מַזְרִיעַ זֶרַע ← עֵשֶׂב מַזְרִיעַ זֶרַע לְמִינֵהוּ› spec-delta —
# spec said herb yielding-seed seed, delivery says herb yielding-seed seed
# to-by-its-kind
m.spec_delta("esev mazria zera",
             "esev mazria zera le-minehu")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on vegetation
m.test("PASS", "tov", "vegetation")

# -------------------------- Gen.1.13 · COMMIT_DOUBLE_DAY -------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם שְׁלִישִׁי
# "And there was evening and there was morning, a third day."
m.step("Gen.1.13")
# ‹יוֹם שְׁלִישִׁי› ledger: day 3 committed
m.commit(3, label_form="ordinal", label_translit="yom shelishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'yabasha', 'deshe'}
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

###############################################################################
# UNIT: gen_04_lights_calendar
###############################################################################
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
# ‹יְהִי מְאֹרֹת› God speaks a demand — LET: exists(lights), loc=expanse-
# the-heavens
m.declare("Elohim", "LET",
          "exists(meorot), loc=raqia_ha_shamayim")
# ‹לְהַבְדִּיל … וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים› open
# question logged: exists(lights), loc=expanse-the-heavens
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
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): exists(lights),
# loc=expanse-the-heavens
m.result("exists(meorot), loc=raqia_ha_shamayim", tmark="t1")

# -------------------------- Gen.1.16 · BUILD_DIFFERENTIATE_DELTA -----------
# וַיַּעַשׂ אֱלֹהִים אֶת־שְׁנֵי הַמְּאֹרֹת הַגְּדֹלִים אֶת־הַמָּאוֹר
# הַגָּדֹל לְמֶמְשֶׁלֶת הַיּוֹם וְאֶת־הַמָּאוֹר הַקָּטֹן לְמֶמְשֶׁלֶת
# הַלַּיְלָה וְאֵת הַכּוֹכָבִים
# "And God made the two great lights: the greater light to rule the day, and
# the lesser light to rule the night; and the stars."
m.step("Gen.1.16")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת … אֶת … וְאֶת … וְאֵת› event: make — agent God;
# theme light-great, light-small, stars
m.event("make", agent="Elohim", themes=["maor_gadol", "maor_qaton", "kokhavim"])
# the world gains: light-great, light-small, stars
m.install("maor_gadol", "maor_qaton", "kokhavim")
# ‹לְמֶמְשֶׁלֶת הַיּוֹם … לְמֶמְשֶׁלֶת הַלַּיְלָה› role assigned: light-
# great -> dominion-of-day; light-small -> dominion-of-night
m.assign("maor_gadol", "memshelet_yom")
m.assign("maor_qaton", "memshelet_lailah")
# ‹הַמְּאֹרֹת הַגְּדֹלִים ← הַגָּדֹל / הַקָּטֹן› spec-delta — spec said
# from'lights (one undifferentiated plural), delivery says two-of the-from
m.spec_delta("me'orot (one undifferentiated plural)",
             "shnei ha-me")
# ‹וְאֵת הַכּוֹכָבִים› spec-delta — spec said no stars in the job order,
# delivery says and-obj-marker the-stars
m.spec_delta("no stars in the job order",
             "ve-et ha-kokhavim")
# ‹לְמֶמְשֶׁלֶת› spec-delta — spec said jobs: divide, signs, festivals,
# days+years, shine, delivery says to-dominion-of (dominion) added
m.spec_delta("jobs: divide, signs, festivals, days+years, shine",
             "le-memshelet (dominion) added")

# -------------------------- Gen.1.17 · INSTALL_MOUNT -----------------------
# וַיִּתֵּן אֹתָם אֱלֹהִים בִּרְקִיעַ הַשָּׁמָיִם לְהָאִיר עַל־הָאָרֶץ
# "And God set them in the firmament of the heaven to give light upon the
# earth."
m.step("Gen.1.17")
# ‹וַיִּתֵּן אֹתָם› event: place — agent God; theme them-the-lights
m.event("place", agent="Elohim", themes=["otam_ha_meorot"])

# -------------------------- Gen.1.18 · PURPOSE_RECAP_DELTA_TEST ------------
# וְלִמְשֹׁל בַּיּוֹם וּבַלַּיְלָה וּלְהַבְדִּיל בֵּין הָאוֹר וּבֵין
# הַחֹשֶׁךְ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And to rule over the day and over the night, and to divide the light from
# the darkness; and God saw that it was good."
m.step("Gen.1.18")
# ‹בֵּין הַיּוֹם וּבֵין הַלָּיְלָה ← בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ› spec-
# delta — spec said to-divide between the-YOM u-between the-LAILAH (registry
# labels, 1:14), delivery says u-to-divide between the-OR u-between the-
# CHOSHEKH (the entities, 1:18)
m.spec_delta("le-havdil bein ha-YOM u-vein ha-LAILAH (registry labels, 1:14)",
             "u-le-havdil bein ha-OR u-vein ha-CHOSHEKH (the entities, 1:18)")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on lights
m.test("PASS", "tov", "meorot")

# -------------------------- Gen.1.19 · COMMIT_DAY --------------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם רְבִיעִי
# "And there was evening and there was morning, a fourth day."
m.step("Gen.1.19")
# ‹יוֹם רְבִיעִי› ledger: day 4 committed
m.commit(4, label_form="ordinal", label_translit="yom revii")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'maor_gadol', 'maor_qaton', 'kokhavim', 'meorot'}
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_05_swarms_blessing
###############################################################################
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
# ‹יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ נֶפֶשׁ חַיָּה› God speaks a demand — LET?:
# swarm(waters), product=swarm-of-living-being-living
m.declare("Elohim", "LET?",
          "swarm(mayim), product=sheretz_nefesh_chaya")
# ‹וְעוֹף יְעוֹפֵף עַל־הָאָרֶץ עַל־פְּנֵי רְקִיעַ הַשָּׁמָיִם› God speaks a
# demand — LET?: fly(flier), loc=face-of-expanse-the-heavens
m.declare("Elohim", "LET?",
          "fly(of), loc=pnei_raqia_ha_shamayim")
# ‹יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ› open question logged: swarm(waters),
# product=swarm-of-living-being-living
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
# ‹וַיִּבְרָא אֱלֹהִים אֶת … וְאֵת … וְאֵת› event: create — agent God; theme
# sea-monsters, living-being-living-creeping, flier-wing
m.event("create", agent="Elohim", themes=["taninim", "nefesh_chaya_romeset", "of_kanaf"])
# the world gains: sea-monsters, living-being-living-creeping, flier-wing
m.install("taninim", "nefesh_chaya_romeset", "of_kanaf")
# ‹אֲשֶׁר שָׁרְצוּ הַמַּיִם› demand settled (popped from the queue):
# swarm(waters), product=swarm-of-living-being-living
m.result("swarm(mayim), product=sheretz_nefesh_chaya", tmark="t1")
# ‹וְאֵת כָּל־עוֹף כָּנָף› demand settled (popped from the queue):
# fly(flier), loc=face-of-expanse-the-heavens
m.result("fly(of), loc=pnei_raqia_ha_shamayim", tmark="t1")
# ‹יִשְׁרְצוּ הַמַּיִם ← וַיִּבְרָא אֱלֹהִים› spec-delta — spec said let-
# swarm HA-MAYIM (the waters as delegated producer), delivery says and-
# created ELOHIM (create — God executes; the waters credited only in the
# relative clause)
m.spec_delta("yishretzu HA-MAYIM (the waters as delegated producer)",
             "va-yivra ELOHIM (bara — God executes; the waters credited only in the relative clause)")
# ‹אֶת־הַתַּנִּינִם הַגְּדֹלִים› spec-delta — spec said no sea-monsters in
# the order, delivery says obj-marker-the-sea-monsters the-great-ones
# leading the inventory, with the week
m.spec_delta("no taninim in the order",
             "et-ha-taninim ha-gedolim leading the inventory, with the week")
# ‹כָּל … לְמִינֵהֶם … כָּל־עוֹף כָּנָף לְמִינֵהוּ› spec-delta — spec said
# swarm-of living-being living; flier (bare classes), delivery says every-
# totality x2, kind-keys to-by-their-kinds / to-by-its-kind, flier
# differentiated as flier KANAF
m.spec_delta("sheretz nefesh chaya; of (bare classes)",
             "kol- totality x2, kind-keys le-minehem / le-minehu, of differentiated as of KANAF")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on living-being
m.test("PASS", "tov", "nefesh_chaya")

# -------------------------- Gen.1.22 · BLESS_MANDATE -----------------------
# וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הַמַּיִם
# בַּיַּמִּים וְהָעוֹף יִרֶב בָּאָרֶץ
# "And God blessed them, saying: 'Be fruitful, and multiply, and fill the
# waters in the seas, and let fowl multiply in the earth.'"
m.step("Gen.1.22")
# ‹וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ› blessing: God
# blesses them — mandate: CMD!(peru), CMD!(revu), CMD!(milu(et-the-waters-
# in-the-yamim)), LET(yirev(ha-flier-in-the-aretz))
m.bless("Elohim", "otam", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_mayim_ba_yamim))", "LET(yirev(ha_of_ba_aretz))"])
# reads without prior install (flag, not fix): seas
m.presupposed("yamim")

# -------------------------- Gen.1.23 · COMMIT_DAY --------------------------
# וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם חֲמִישִׁי
# "And there was evening and there was morning, a fifth day."
m.step("Gen.1.23")
# ‹יוֹם חֲמִישִׁי› ledger: day 5 committed
m.commit(5, label_form="ordinal", label_translit="yom chamishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'of_kanaf', 'nefesh_chaya_romeset', 'taninim'}
    assert m.presupposed_set() == {'aretz', 'shamayim', 'mayim', 'raqia', 'yamim'}
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_06_land_adam_dominion
###############################################################################
# =============================================================================
# gen_06_land_adam_dominion — 1:24-31
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_06_land_adam_dominion.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Day six: land classes, the adam, dominion — receipts return, the council plural, bara tripled, the five-imperative blessing, the food grants, THE sixth day (1:24-31)"""
from machine import Machine

m = Machine("gen_06_land_adam_dominion")

# -------------------------- Gen.1.24 · DECLARE_SPEC_LAND_CLASSES_RECEIPT ---
# וַיֹּאמֶר אֱלֹהִים תּוֹצֵא הָאָרֶץ נֶפֶשׁ חַיָּה לְמִינָהּ בְּהֵמָה
# וָרֶמֶשׂ וְחַיְתוֹ־אֶרֶץ לְמִינָהּ וַיְהִי־כֵן
# "And God said: 'Let the earth bring forth the living creature after its
# kind, cattle, and creeping thing, and beast of the earth after its kind.'
# And it was so."
m.step("Gen.1.24")
# ‹תּוֹצֵא הָאָרֶץ נֶפֶשׁ חַיָּה לְמִינָהּ› God speaks a demand — LET: let-
# bring-forth(earth), product=living-being-living-to-by-its-kind
m.declare("Elohim", "LET",
          "totze(aretz), product=nefesh_chaya_le_minah")
# ‹תּוֹצֵא הָאָרֶץ› open question logged: let-bring-forth(earth),
# product=living-being-living-to-by-its-kind
m.triple("totze(aretz), product=nefesh_chaya_le_minah")
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): let-bring-
# forth(earth), product=living-being-living-to-by-its-kind
m.result("totze(aretz), product=nefesh_chaya_le_minah", tmark="t1")
# reads without prior install (flag, not fix): earth
m.presupposed("aretz")

# -------------------------- Gen.1.25 · BUILD_DELTA_TEST --------------------
# וַיַּעַשׂ אֱלֹהִים אֶת־חַיַּת הָאָרֶץ לְמִינָהּ וְאֶת־הַבְּהֵמָה לְמִינָהּ
# וְאֵת כָּל־רֶמֶשׂ הָאֲדָמָה לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
# "And God made the beast of the earth after its kind, and the cattle after
# their kind, and every thing that creepeth upon the ground after its kind;
# and God saw that it was good."
m.step("Gen.1.25")
# ‹וַיַּעַשׂ אֱלֹהִים אֶת … וְאֶת … וְאֵת› event: make — agent God; theme
# wild-beast-of-the-earth, cattle, creeper-the-ground
m.event("make", agent="Elohim", themes=["chayat_ha_aretz", "behemah", "remes_ha_adamah"])
# the world gains: wild-beast-of-the-earth, cattle, creeper-the-ground
m.install("chayat_ha_aretz", "behemah", "remes_ha_adamah")
# ‹תּוֹצֵא הָאָרֶץ ← וַיַּעַשׂ אֱלֹהִים› spec-delta — spec said let-bring-
# forth HA-ARETZ (the earth as delegated producer), delivery says and-ya
m.spec_delta("totze HA-ARETZ (the earth as delegated producer)",
             "va-ya")
# ‹וְחַיְתוֹ־אֶרֶץ ← חַיַּת הָאָרֶץ› spec-delta — spec said cattle, creeper,
# wild-beast-of-earth (archaic construct, bare earth), delivery says CHAYAT
# HA-ARETZ first (normalized construct + definite article), the-cattle,
# creeper
m.spec_delta("behemah, remes, chayto-eretz (archaic construct, bare eretz)",
             "CHAYAT HA-ARETZ first (normalized construct + definite article), ha-behemah, remes")
# ‹וָרֶמֶשׂ ← כָּל־רֶמֶשׂ הָאֲדָמָה› spec-delta — spec said creeper (bare),
# delivery says KOL-creeper HA-ADAMAH (totality quantifier + substrate shift
# to the ground)
m.spec_delta("remes (bare)",
             "KOL-remes HA-ADAMAH (totality quantifier + substrate shift to the ground)")
# ‹כִּי־טוֹב› test PASS — oracle-word good, on living-being
m.test("PASS", "tov", "nefesh_chaya")

# -------------------------- Gen.1.26 · DECLARE_SPEC_ADAM_COUNCIL -----------
# וַיֹּאמֶר אֱלֹהִים נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ וְיִרְדּוּ
# בִדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבַבְּהֵמָה וּבְכָל־הָאָרֶץ
# וּבְכָל־הָרֶמֶשׂ הָרֹמֵשׂ עַל־הָאָרֶץ
# "And God said: 'Let us make man in our image, after our likeness; and let
# them have dominion over the fish of the sea, and over the fowl of the air,
# and over the cattle, and over all the earth, and over every creeping thing
# that creepeth upon the earth.'"
m.step("Gen.1.26")
# ‹נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ› God speaks a demand — CMD-US?:
# make(man), spec=in-image-after-likeness
m.declare("Elohim", "CMD-US?",
          "make(adam), spec=b_tzelem_k_demut")
# ‹וְיִרְדּוּ בִדְגַת הַיָּם …› open question logged: rule(man, fish-over-
# flier-of-cattle-earth-creeper)
m.triple("rule(adam, dagah_of_behemah_aretz_remes)")
# reads without prior install (flag, not fix): fish-of-the-sea, fowl-of-the-
# sky
m.presupposed("dagat_ha_yam", "of_ha_shamayim")

# -------------------------- Gen.1.27 · BUILD_BARA_TRIPLED ------------------
# וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ
# זָכָר וּנְקֵבָה בָּרָא אֹתָם
# "And God created man in His own image, in the image of God created He him;
# male and female created He them."
m.step("Gen.1.27")
# ‹וַיִּבְרָא … בָּרָא … בָּרָא› event: create — agent God; theme the-man
m.event("create", agent="Elohim", themes=["ha_adam"])
# the world gains: the-man
m.install("ha_adam")
# ‹וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם› demand settled (popped from the queue):
# make(man), spec=in-image-after-likeness
m.result("make(adam), spec=b_tzelem_k_demut", tmark="t2")
# ‹נַעֲשֶׂה ← וַיִּבְרָא … בָּרָא … בָּרָא› spec-delta — spec said na'make
# (he-made — the making verb, 1cp), delivery says created x3 (creation
m.spec_delta("na'aseh (asah — the making verb, 1cp)",
             "bara x3 (creation")
# ‹בְּצַלְמֵנוּ ← בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים› spec-delta — spec said in-
# tzalmeNU that-our-likeness (OUR image, OUR likeness — plural possessor),
# delivery says in-His-image (HIS image) + in-image-of ELOHIM (the image
# over-flier-of God, named singular)
m.spec_delta("be-tzalmeNU ki-dmuteNU (OUR image, OUR likeness — plural possessor)",
             "be-tzalmO (HIS image) + be-tzelem ELOHIM (the image of God, named singular)")
# ‹כִּדְמוּתֵנוּ ← (אבד)› spec-delta — spec said image-of AND likeness
# (image and likeness, two nouns), delivery says image-of only, x3 —
# likeness DROPPED
m.spec_delta("tzelem AND demut (image and likeness, two nouns)",
             "tzelem only, x3 — demut DROPPED")
# ‹אֹתוֹ ← אֹתָם› spec-delta — spec said man (unsexed species noun),
# delivery says male u-female (male and female) + him -> them (created HIM
# -> created THEM)
m.spec_delta("adam (unsexed species noun)",
             "zakhar u-nekevah (male and female) + oto -> otam (created HIM -> created THEM)")

# -------------------------- Gen.1.28 · BLESS_MANDATE_DOMINION --------------
# וַיְבָרֶךְ אֹתָם אֱלֹהִים וַיֹּאמֶר לָהֶם אֱלֹהִים פְּרוּ וּרְבוּ
# וּמִלְאוּ אֶת־הָאָרֶץ וְכִבְשֻׁהָ וּרְדוּ בִּדְגַת הַיָּם וּבְעוֹף
# הַשָּׁמַיִם וּבְכָל־חַיָּה הָרֹמֶשֶׂת עַל־הָאָרֶץ
# "And God blessed them; and God said unto them: 'Be fruitful, and multiply,
# and replenish the earth, and subdue it; and have dominion over the fish of
# the sea, and over the fowl of the air, and over every living thing that
# creepeth upon the earth.'"
m.step("Gen.1.28")
# ‹וַיְבָרֶךְ אֹתָם אֱלֹהִים וַיֹּאמֶר לָהֶם אֱלֹהִים פְּרוּ וּרְבוּ
# וּמִלְאוּ … וְכִבְשֻׁהָ וּרְדוּ› blessing: God blesses them — mandate:
# CMD!(peru), CMD!(revu), CMD!(milu(et-the-aretz)), CMD!(kivshuha),
# CMD!(redu(ba-fish-and-and-over-flier-of-and-and-over-all-living-romeset))
m.bless("Elohim", "otam", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_aretz))", "CMD!(kivshuha)", "CMD!(redu(ba_dagah_u_va_of_u_ve_khol_chaya_romeset))"])
# ‹וּבְכָל־הָאָרֶץ ← וּמִלְאוּ אֶת־הָאָרֶץ וְכִבְשֻׁהָ› spec-delta — spec
# said design: let-them-rule over 5 domains (incl. cattle + KOL HA-ARETZ as
# dominion domains), delivery says mandate: rule over 3 domains — cattle
# dropped, creeper -> KOL CHAYAH creeping, and the earth MOVED from
# dominion-domain to fill-and-subdue OBJECT
m.spec_delta("design: yirdu over 5 domains (incl. behemah + KOL HA-ARETZ as dominion domains)",
             "mandate: redu over 3 domains — behemah dropped, remes -> KOL CHAYAH romeset, and the earth MOVED from dominion-domain to fill-and-subdue OBJECT")
# ‹וְכִבְשֻׁהָ› spec-delta — spec said design verbs: rule only (rule),
# delivery says subdue ADDED (subdue) — a verb absent from every spec clause
# over-flier-of the week
m.spec_delta("design verbs: radah only (rule)",
             "kavash ADDED (subdue) — a verb absent from every spec clause of the week")

# -------------------------- Gen.1.29 · GRANT_FOOD_ADAM ---------------------
# וַיֹּאמֶר אֱלֹהִים הִנֵּה נָתַתִּי לָכֶם אֶת־כָּל־עֵשֶׂב זֹרֵעַ זֶרַע
# אֲשֶׁר עַל־פְּנֵי כָל־הָאָרֶץ וְאֶת־כָּל־הָעֵץ אֲשֶׁר־בּוֹ פְרִי־עֵץ
# זֹרֵעַ זָרַע לָכֶם יִהְיֶה לְאָכְלָה
# "And God said: 'Behold, I have given you every herb yielding seed, which
# is upon the face of all the earth, and every tree, in which is the fruit
# of a tree yielding seed — to you it shall be for food;'"
m.step("Gen.1.29")
# ‹הִנֵּה נָתַתִּי לָכֶם› event: grant — agent God; theme every-seed-
# bearing-plant
m.event("grant", agent="Elohim", themes=["kol_zorea_zera"])
# reads without prior install (flag, not fix): every-seed-bearing-plant
m.presupposed("kol_zorea_zera")
# ‹כָּל־עֵשֶׂב זֹרֵעַ זֶרַע … כָּל־הָעֵץ … לְאָכְלָה› role assigned: every-
# seed-bearing-plant -> food-to-man
m.assign("kol_zorea_zera", "okhlah_la_adam")
# ‹לָכֶם יִהְיֶה לְאָכְלָה› God speaks a demand — LET?: it-shall-be(every-
# seed-bearing-plant, for-food)
m.declare("Elohim", "LET?",
          "yihyeh(kol_zorea_zera, le_okhlah)")

# -------------------------- Gen.1.30 · GRANT_FOOD_ANIMALS_RECEIPT ----------
# וּלְכָל־חַיַּת הָאָרֶץ וּלְכָל־עוֹף הַשָּׁמַיִם וּלְכֹל רוֹמֵשׂ
# עַל־הָאָרֶץ אֲשֶׁר־בּוֹ נֶפֶשׁ חַיָּה אֶת־כָּל־יֶרֶק עֵשֶׂב לְאָכְלָה
# וַיְהִי־כֵן
# "'and to every beast of the earth, and to every fowl of the air, and to
# every thing that creepeth upon the earth, wherein there is a living soul,
# [I have given] every green herb for food.' And it was so."
m.step("Gen.1.30")
# reads without prior install (flag, not fix): every-green-of-herb
m.presupposed("kol_yerek_esev")
# ‹אֶת־כָּל־יֶרֶק עֵשֶׂב לְאָכְלָה› role assigned: every-green-of-herb ->
# food-to-chol-living-being-living
m.assign("kol_yerek_esev", "okhlah_le_chol_nefesh_chaya")
# ‹וַיְהִי־כֵן› demand settled (popped from the queue): it-shall-be(every-
# seed-bearing-plant, for-food)
m.result("yihyeh(kol_zorea_zera, le_okhlah)", tmark="t3")

# -------------------------- Gen.1.31 · TEST_GLOBAL_COMMIT ------------------
# וַיַּרְא אֱלֹהִים אֶת־כָּל־אֲשֶׁר עָשָׂה וְהִנֵּה־טוֹב מְאֹד וַיְהִי־עֶרֶב
# וַיְהִי־בֹקֶר יוֹם הַשִּׁשִּׁי
# "And God saw every thing that He had made, and, behold, it was very good.
# And there was evening and there was morning, the sixth day."
m.step("Gen.1.31")
# ‹וְהִנֵּה־טוֹב מְאֹד› test PASS — oracle-word very-good, on all-that-He-
# made
m.test("PASS", "tov_meod", "kol_asher_asah")
# ‹יוֹם הַשִּׁשִּׁי› ledger: day 6 committed
m.commit(6, label_form="ordinal", label_translit="yom ha-shishi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ha_adam', 'remes_ha_adamah', 'chayat_ha_aretz', 'behemah'}
    assert m.presupposed_set() == {'of_ha_shamayim', 'kol_zorea_zera', 'kol_yerek_esev', 'aretz', 'dagat_ha_yam'}
    assert m.REGISTRY["names"] == {'kol_zorea_zera': 'okhlah_la_adam', 'kol_yerek_esev': 'okhlah_le_chol_nefesh_chaya'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'tov', 'nefesh_chaya'), ('PASS', 'tov_meod', 'kol_asher_asah')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == [6]
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 9}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_aretz))', 'mandate: CMD!(kivshuha)', 'mandate: CMD!(redu(ba_dagah_u_va_of_u_ve_khol_chaya_romeset))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_07_completion_sanctity
###############################################################################
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
# ‹וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל־צְבָאָם› event: complete — theme
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
# ‹וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי מְלַאכְתּוֹ› event: finish — agent
# God
m.event("finish", agent="Elohim")
# ‹וַיִּשְׁבֹּת בַּיּוֹם הַשְּׁבִיעִי מִכָּל־מְלַאכְתּוֹ› event: cease —
# agent God
m.event("cease", agent="Elohim")

# -------------------------- Gen.2.3 · BLESS_SANCTIFY -----------------------
# וַיְבָרֶךְ אֱלֹהִים אֶת־יוֹם הַשְּׁבִיעִי וַיְקַדֵּשׁ אֹתוֹ כִּי בוֹ
# שָׁבַת מִכָּל־מְלַאכְתּוֹ אֲשֶׁר־בָּרָא אֱלֹהִים לַעֲשׂוֹת
# "And God blessed the seventh day, and hallowed it; because that in it He
# rested from all His work which God in creating had made."
m.step("Gen.2.3")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־יוֹם הַשְּׁבִיעִי› blessing: God blesses the-
# seventh-day
m.bless("Elohim", "yom_ha_shevii")
# ‹וַיְקַדֵּשׁ אֹתוֹ› role assigned: the-seventh-day -> holy
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

###############################################################################
# UNIT: gen_08_toledot_garden_first_rule
###############################################################################
# =============================================================================
# gen_08_toledot_garden_first_rule — 2:4-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_08_toledot_garden_first_rule.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden I: toledot header, garden, first job, FIRST RULE (2:4-17)"""
from machine import Machine

m = Machine("gen_08_toledot_garden_first_rule")

# -------------------------- Gen.2.4 · SECTION_HEADER -----------------------
# אֵלֶּה תוֹלְדוֹת הַשָּׁמַיִם וְהָאָרֶץ בְּהִבָּרְאָם בְּיוֹם עֲשׂוֹת
# יְהוָה אֱלֹהִים אֶרֶץ וְשָׁמָיִם
# "These are the generations of the heaven and of the earth when they were
# created, in the day that the LORD God made earth and heaven."
m.step("Gen.2.4")
# ‹אֵלֶּה תוֹלְדוֹת הַשָּׁמַיִם וְהָאָרֶץ› section generations: heavens,
# earth
m.section("toledot", "shamayim", "aretz")
# ‹בְּיוֹם עֲשׂוֹת יְהוָה אֱלֹהִים אֶרֶץ וְשָׁמָיִם› clock anchored: t0 :=
# in-the-day-of-[His]-making
m.time_anchor("be_yom_asot")
# reads without prior install (flag, not fix): heavens, earth
m.presupposed("shamayim", "aretz")
# ‹יְהוָה אֱלֹהִים› spec-delta — spec said God (the week's sole agent name,
# gen-01-07), delivery says the-LORD-God (compound: personal name + generic)
m.spec_delta("Elohim (the week's sole agent name, gen_01-07)",
             "YHWH_Elohim (compound: personal name + generic)")

# -------------------------- Gen.2.5 · PRECONDITIONS_LACKS ------------------
# וְכֹל שִׂיחַ הַשָּׂדֶה טֶרֶם יִהְיֶה בָאָרֶץ וְכָל־עֵשֶׂב הַשָּׂדֶה טֶרֶם
# יִצְמָח כִּי לֹא הִמְטִיר יְהוָה אֱלֹהִים עַל־הָאָרֶץ וְאָדָם אַיִן
# לַעֲבֹד אֶת־הָאֲדָמָה
# "No shrub of the field was yet in the earth, and no herb of the field had
# yet sprung up; for the LORD God had not caused it to rain upon the earth,
# and there was not a man to till the ground."
m.step("Gen.2.5")
# ‹טֶרֶם … טֶרֶם … לֹא הִמְטִיר … וְאָדָם אַיִן› fact holds: not-yet(all-
# shrub-the-field); not-yet(all-herb-the-field); had-not-caused-rain(the-
# LORD-God, over-the-earth); no-human-existed(to-work-obj-marker·et-the-
# ground)
m.fact("terem(kol_siach_ha_sadeh)",
       "terem(kol_esev_ha_sadeh)",
       "lo_himtir(YHWH_Elohim, al_ha_aretz)",
       "adam_ayin(la_avod_et_ha_adamah)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")

# -------------------------- Gen.2.6 · PRECONDITION_IRRIGATION --------------
# וְאֵד יַעֲלֶה מִן־הָאָרֶץ וְהִשְׁקָה אֶת־כָּל־פְּנֵי־הָאֲדָמָה
# "But there went up a mist from the earth, and watered the whole face of
# the ground."
m.step("Gen.2.6")
# ‹וְאֵד יַעֲלֶה … וְהִשְׁקָה› fact holds: mist-went-up-and-watered(all-
# face-of-the-ground)
m.fact("ed_yaaleh_ve_hishqah(kol_pnei_ha_adamah)")

# -------------------------- Gen.2.7 · FORM_BREATHE_BECOME ------------------
# וַיִּיצֶר יְהוָה אֱלֹהִים אֶת־הָאָדָם עָפָר מִן־הָאֲדָמָה וַיִּפַּח
# בְּאַפָּיו נִשְׁמַת חַיִּים וַיְהִי הָאָדָם לְנֶפֶשׁ חַיָּה
# "Then the LORD God formed man of the dust of the ground, and breathed into
# his nostrils the breath of life; and man became a living soul."
m.step("Gen.2.7")
# ‹וַיִּיצֶר יְהוָה אֱלֹהִים אֶת־הָאָדָם עָפָר מִן־הָאֲדָמָה› event: form —
# agent the-LORD-God; theme human
m.event("form", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיִּפַּח בְּאַפָּיו נִשְׁמַת חַיִּים› event: breathe — agent the-LORD-
# God; theme breath-of-life
m.event("breathe", agent="YHWH_Elohim", themes=["nishmat_chayim"])
# ‹וַיְהִי הָאָדָם לְנֶפֶשׁ חַיָּה› event: become — theme human, living-
# being
m.event("become", themes=["adam", "nefesh_chaya"])
# ‹הָאָדָם› the world gains: human
m.install("adam")
# spec-delta — spec said create/make (create/make — the week's build verbs),
# delivery says he-formed (form — the potter verb, double-yod written-form)
m.spec_delta("bara/asah (create/make — the week's build verbs)",
             "yatzar (form — the potter verb, double-yod ktiv)")

# -------------------------- Gen.2.8 · PLANT_PLACE --------------------------
# וַיִּטַּע יְהוָה אֱלֹהִים גַּן־בְּעֵדֶן מִקֶּדֶם וַיָּשֶׂם שָׁם
# אֶת־הָאָדָם אֲשֶׁר יָצָר
# "And the LORD God planted a garden eastward, in Eden; and there He put the
# man whom He had formed."
m.step("Gen.2.8")
# ‹וַיִּטַּע יְהוָה אֱלֹהִים גַּן־בְּעֵדֶן מִקֶּדֶם› event: plant — agent
# the-LORD-God; theme garden
m.event("plant", agent="YHWH_Elohim", themes=["gan"])
# ‹וַיָּשֶׂם שָׁם אֶת־הָאָדָם אֲשֶׁר יָצָר› event: place — agent the-LORD-
# God; theme human
m.event("place", agent="YHWH_Elohim", themes=["adam"])
# ‹גַּן› the world gains: garden
m.install("gan")
# reads without prior install (flag, not fix): Eden
m.presupposed("eden")

# -------------------------- Gen.2.9 · SPROUT_TWO_TREES ---------------------
# וַיַּצְמַח יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־עֵץ נֶחְמָד לְמַרְאֶה וְטוֹב
# לְמַאֲכָל וְעֵץ הַחַיִּים בְּתוֹךְ הַגָּן וְעֵץ הַדַּעַת טוֹב וָרָע
# "And out of the ground made the LORD God to grow every tree that is
# pleasant to the sight, and good for food; the tree of life also in the
# midst of the garden, and the tree of the knowledge of good and evil."
m.step("Gen.2.9")
# ‹וַיַּצְמַח יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־עֵץ› event: sprout — agent
# the-LORD-God; theme all-tree
m.event("sprout", agent="YHWH_Elohim", themes=["kol_etz"])
# ‹וְעֵץ הַחַיִּים בְּתוֹךְ הַגָּן וְעֵץ הַדַּעַת טוֹב וָרָע› the world
# gains: tree-of-life, tree-of-knowledge-of-good-and-evil
m.install("etz_ha_chayim", "etz_ha_daat_tov_va_ra")
# spec-delta — spec said good as TEST verdict (the week's instrument, days
# 1-6), delivery says good as attribute (good to-food; gold good 2:12;
# knowledge good and-evil)
m.spec_delta("tov as TEST verdict (the week's instrument, days 1-6)",
             "tov as attribute (tov le-maakhal; zahav tov 2:12; daat tov va-ra)")

# -------------------------- Gen.2.10 · RIVER_SYSTEM ------------------------
# וְנָהָר יֹצֵא מֵעֵדֶן לְהַשְׁקוֹת אֶת־הַגָּן וּמִשָּׁם יִפָּרֵד וְהָיָה
# לְאַרְבָּעָה רָאשִׁים
# "And a river went out of Eden to water the garden; and from thence it was
# parted, and became four heads."
m.step("Gen.2.10")
# ‹וְנָהָר יֹצֵא … יִפָּרֵד וְהָיָה› fact holds: river-goes-out-from-
# Eden(to-water-obj-marker·et-the-garden); divides-to-four-heads(river)
m.fact("nahar_yotze_me_eden(le_hashqot_et_ha_gan)",
       "yipared_le_arbaah_rashim(nahar)")
# ‹וְהָיָה לְאַרְבָּעָה רָאשִׁים› the world gains: river, river-1, river-2,
# river-3, river-4
m.install("nahar", "nahar_1", "nahar_2", "nahar_3", "nahar_4")

# -------------------------- Gen.2.11 · REGISTRY_ROW_1 ----------------------
# שֵׁם הָאֶחָד פִּישׁוֹן הוּא הַסֹּבֵב אֵת כָּל־אֶרֶץ הַחֲוִילָה אֲשֶׁר־שָׁם
# הַזָּהָב
# "The name of the first is Pishon; that is it which compasseth the whole
# land of Havilah, where there is gold."
m.step("Gen.2.11")
# ‹שֵׁם הָאֶחָד פִּישׁוֹן› named: river-1 := Pishon
m.name("nahar_1", "Pishon")
# ‹הוּא הַסֹּבֵב … אֲשֶׁר־שָׁם הַזָּהָב› fact holds: circling-all-earth-the-
# Havilah(river-1); there-the-gold(Havilah)
m.fact("sovev_kol_eretz_ha_chavilah(nahar_1)",
       "sham_ha_zahav(chavilah)")

# -------------------------- Gen.2.12 · REGISTRY_ROW_1_RESOURCES ------------
# וּזְהַב הָאָרֶץ הַהִוא טוֹב שָׁם הַבְּדֹלַח וְאֶבֶן הַשֹּׁהַם
# "And the gold of that land is good; there is bdellium and the onyx stone."
m.step("Gen.2.12")
# ‹וּזְהַב הָאָרֶץ הַהִוא טוֹב שָׁם הַבְּדֹלַח וְאֶבֶן הַשֹּׁהַם› fact
# holds: gold-good(the-earth-the-that-one-ktiv-hu-qere-hi); there-the-
# bdellium-and-stone-of-the-shoham(Havilah)
m.fact("zahav_tov(ha_aretz_ha_hiv)",
       "sham_ha_bedolach_ve_even_ha_shoham(chavilah)")

# -------------------------- Gen.2.13 · REGISTRY_ROW_2 ----------------------
# וְשֵׁם־הַנָּהָר הַשֵּׁנִי גִּיחוֹן הוּא הַסּוֹבֵב אֵת כָּל־אֶרֶץ כּוּשׁ
# "And the name of the second river is Gihon; the same is it that compasseth
# the whole land of Cush."
m.step("Gen.2.13")
# ‹וְשֵׁם־הַנָּהָר הַשֵּׁנִי גִּיחוֹן› named: river-2 := Gichon
m.name("nahar_2", "Gichon")
# ‹הוּא הַסּוֹבֵב אֵת כָּל־אֶרֶץ כּוּשׁ› fact holds: circling-all-earth-
# Chush(river-2)
m.fact("sovev_kol_eretz_kush(nahar_2)")

# -------------------------- Gen.2.14 · REGISTRY_ROWS_3_4 -------------------
# וְשֵׁם הַנָּהָר הַשְּׁלִישִׁי חִדֶּקֶל הוּא הַהֹלֵךְ קִדְמַת אַשּׁוּר
# וְהַנָּהָר הָרְבִיעִי הוּא פְרָת
# "And the name of the third river is Hiddekel; that is it which goeth
# toward the east of Asshur. And the fourth river is the Euphrates."
m.step("Gen.2.14")
# ‹חִדֶּקֶל … וְהַנָּהָר הָרְבִיעִי הוּא פְרָת› named: river-3 := Chidekel;
# river-4 := Perat
m.name("nahar_3", "Chidekel")
m.name("nahar_4", "Perat")
# ‹הוּא הַהֹלֵךְ קִדְמַת אַשּׁוּר› fact holds: going-east-of-Asshur(river-3)
m.fact("holekh_qidmat_ashur(nahar_3)")

# -------------------------- Gen.2.15 · TAKE_SETTLE_ASSIGN_JOB --------------
# וַיִּקַּח יְהוָה אֱלֹהִים אֶת־הָאָדָם וַיַּנִּחֵהוּ בְגַן־עֵדֶן לְעָבְדָהּ
# וּלְשָׁמְרָהּ
# "And the LORD God took the man, and put him into the garden of Eden to
# dress it and to keep it."
m.step("Gen.2.15")
# ‹וַיִּקַּח יְהוָה אֱלֹהִים אֶת־הָאָדָם› event: take — agent the-LORD-God;
# theme human
m.event("take", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיַּנִּחֵהוּ בְגַן־עֵדֶן› event: settle — agent the-LORD-God; theme
# human
m.event("settle", agent="YHWH_Elohim", themes=["adam"])
# ‹לְעָבְדָהּ וּלְשָׁמְרָהּ› role assigned: human -> worker-and-keeper
m.assign("adam", "oved_ve_shomer")

# -------------------------- Gen.2.16 · COMMAND_PERMISSION ------------------
# וַיְצַו יְהוָה אֱלֹהִים עַל־הָאָדָם לֵאמֹר מִכֹּל עֵץ־הַגָּן אָכֹל תֹּאכֵל
# "And the LORD God commanded the man, saying: 'Of every tree of the garden
# thou mayest freely eat.'"
m.step("Gen.2.16")
# ‹וַיְצַו יְהוָה אֱלֹהִים עַל־הָאָדָם לֵאמֹר› event: command — agent the-
# LORD-God; theme human
m.event("command", agent="YHWH_Elohim", themes=["adam"])
# ‹מִכֹּל עֵץ־הַגָּן אָכֹל תֹּאכֵל› the-LORD-God speaks a demand — LET?:
# eat(human, from-every-tree-of-the-garden)
m.declare("YHWH_Elohim", "LET?",
          "akhal(adam, mi_kol_etz_ha_gan)")
# spec-delta — spec said all herb + all tree to-food (1:29 universal food
# grant), delivery says from-all tree the-garden + one exclusion pending
# (the grant narrows to a bounded domain)
m.spec_delta("kol esev + kol etz le-okhlah (1:29 universal food grant)",
             "mi-kol etz ha-gan + one exclusion pending (the grant narrows to a bounded domain)")

# -------------------------- Gen.2.17 · PROHIBITION_PENALTY -----------------
# וּמֵעֵץ הַדַּעַת טוֹב וָרָע לֹא תֹאכַל מִמֶּנּוּ כִּי בְּיוֹם אֲכָלְךָ
# מִמֶּנּוּ מוֹת תָּמוּת
# "'But of the tree of the knowledge of good and evil, thou shalt not eat of
# it; for in the day that thou eatest thereof thou shalt surely die.'"
m.step("Gen.2.17")
# ‹וּמֵעֵץ הַדַּעַת טוֹב וָרָע לֹא תֹאכַל מִמֶּנּוּ› the-LORD-God speaks a
# demand — LET-NOT: eat(human, from-the-tree-of-knowledge-of-good-and-evil)
m.declare("YHWH_Elohim", "LET-NOT",
          "akhal(adam, me_etz_ha_daat_tov_va_ra)")
# ‹כִּי בְּיוֹם אֲכָלְךָ מִמֶּנּוּ מוֹת תָּמוּת› standing handler — if in-
# day-eat(human, from-the-tree-of-knowledge-of-good-and-evil) then dying-
# you-shall-die(human)
m.handler("be_yom_akhal(adam, me_etz_ha_daat_tov_va_ra)",
          "mot_tamut(adam)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'gan', 'etz_ha_daat_tov_va_ra', 'nahar', 'nahar_1', 'etz_ha_chayim', 'adam', 'nahar_3', 'nahar_2', 'nahar_4'}
    assert m.presupposed_set() == {'aretz', 'adamah', 'eden', 'shamayim'}
    assert m.REGISTRY["names"] == {'nahar_1': 'Pishon', 'nahar_2': 'Gichon', 'nahar_3': 'Chidekel', 'nahar_4': 'Perat', 'adam': 'oved_ve_shomer'}
    assert m.REGISTRY["writes"] == 5
    assert m.tests_list() == []
    assert m.open_demands() == ['akhal(adam, mi_kol_etz_ha_gan)', 'akhal(adam, me_etz_ha_daat_tov_va_ra)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4, 'spec_delta': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['terem(kol_siach_ha_sadeh)', 'terem(kol_esev_ha_sadeh)', 'lo_himtir(YHWH_Elohim, al_ha_aretz)', 'adam_ayin(la_avod_et_ha_adamah)', 'ed_yaaleh_ve_hishqah(kol_pnei_ha_adamah)', 'nahar_yotze_me_eden(le_hashqot_et_ha_gan)', 'yipared_le_arbaah_rashim(nahar)', 'sovev_kol_eretz_ha_chavilah(nahar_1)', 'sham_ha_zahav(chavilah)', 'zahav_tov(ha_aretz_ha_hiv)', 'sham_ha_bedolach_ve_even_ha_shoham(chavilah)', 'sovev_kol_eretz_kush(nahar_2)', 'holekh_qidmat_ashur(nahar_3)', 'handler: IF(be_yom_akhal(adam, me_etz_ha_daat_tov_va_ra)) THEN(mot_tamut(adam))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 18
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_09_helper_woman_first_speech
###############################################################################
# =============================================================================
# gen_09_helper_woman_first_speech — 2:18-25
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_09_helper_woman_first_speech.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden II: not-good, the helper, the woman, first human speech (2:18-25)"""
from machine import Machine

m = Machine("gen_09_helper_woman_first_speech")

# -------------------------- Gen.2.18 · VERDICT_FAIL_AND_PLAN ---------------
# וַיֹּאמֶר יְהוָה אֱלֹהִים לֹא־טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ אֶעֱשֶׂה־לּוֹ
# עֵזֶר כְּנֶגְדּוֹ
# "And the LORD God said: 'It is not good that the man should be alone; I
# will make him a help meet for him.'"
m.step("Gen.2.18")
# ‹לֹא־טוֹב הֱיוֹת הָאָדָם לְבַדּוֹ› test FAIL — oracle-word good, on the-
# human-being-alone
m.test("FAIL", "tov", "heyot_ha_adam_levado")
# ‹אֶעֱשֶׂה־לּוֹ עֵזֶר כְּנֶגְדּוֹ› the-LORD-God speaks a demand — CMD-US?:
# make(helper-corresponding-to-him, to-human)
m.declare("YHWH_Elohim", "CMD-US?",
          "make(ezer_kenegdo, le_adam)")
# reads without prior install (flag, not fix): human
m.presupposed("adam")

# -------------------------- Gen.2.19 · FORM_BRING_DELEGATE -----------------
# וַיִּצֶר יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־חַיַּת הַשָּׂדֶה וְאֵת
# כָּל־עוֹף הַשָּׁמַיִם וַיָּבֵא אֶל־הָאָדָם לִרְאוֹת מַה־יִּקְרָא־לוֹ וְכֹל
# אֲשֶׁר יִקְרָא־לוֹ הָאָדָם נֶפֶשׁ חַיָּה הוּא שְׁמוֹ
# "And out of the ground the LORD God formed every beast of the field, and
# every fowl of the air; and brought them unto the man to see what he would
# call them; and whatsoever the man would call every living creature, that
# was to be the name thereof."
m.step("Gen.2.19")
# ‹וַיִּצֶר … מִן־הָאֲדָמָה› event: form — agent the-LORD-God; theme beast-
# of-the-field, fowl-of-the-sky
m.event("form", agent="YHWH_Elohim", themes=["chayat_ha_sadeh", "of_ha_shamayim"])
# ‹כָּל־חַיַּת הַשָּׂדֶה וְאֵת כָּל־עוֹף הַשָּׁמַיִם› the world gains:
# beast-of-the-field, fowl-of-the-sky
m.install("chayat_ha_sadeh", "of_ha_shamayim")
# ‹וַיָּבֵא אֶל־הָאָדָם לִרְאוֹת מַה־יִּקְרָא־לוֹ› event: bring — agent the-
# LORD-God; theme beast-of-the-field
m.event("bring", agent="YHWH_Elohim", themes=["chayat_ha_sadeh"])
# ‹וְכֹל אֲשֶׁר יִקְרָא־לוֹ הָאָדָם נֶפֶשׁ חַיָּה הוּא שְׁמוֹ› fact holds:
# that-is-its-name(all-which-he-will-call-not-the-human)
m.fact("hu_shemo(kol_asher_yiqra_lo_ha_adam)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")

# -------------------------- Gen.2.20 · BULK_NAMING_FAILED_SEARCH -----------
# וַיִּקְרָא הָאָדָם שֵׁמוֹת לְכָל־הַבְּהֵמָה וּלְעוֹף הַשָּׁמַיִם וּלְכֹל
# חַיַּת הַשָּׂדֶה וּלְאָדָם לֹא־מָצָא עֵזֶר כְּנֶגְדּוֹ
# "And the man gave names to all cattle, and to the fowl of the air, and to
# every beast of the field; but for Adam there was not found a help meet for
# him."
m.step("Gen.2.20")
# ‹וַיִּקְרָא הָאָדָם שֵׁמוֹת› event: call — agent human; theme names
m.event("call", agent="adam", themes=["shemot"])
# ‹וּלְאָדָם לֹא־מָצָא עֵזֶר כְּנֶגְדּוֹ› fact holds: did-not-find(helper-
# corresponding-to-him, to-human)
m.fact("lo_matza(ezer_kenegdo, le_adam)")
# reads without prior install (flag, not fix): livestock
m.presupposed("behemah")

# -------------------------- Gen.2.21 · SLEEP_AND_SURGERY -------------------
# וַיַּפֵּל יְהוָה אֱלֹהִים תַּרְדֵּמָה עַל־הָאָדָם וַיִּישָׁן וַיִּקַּח
# אַחַת מִצַּלְעֹתָיו וַיִּסְגֹּר בָּשָׂר תַּחְתֶּנָּה
# "And the LORD God caused a deep sleep to fall upon the man, and he slept;
# and He took one of his ribs, and closed up the place with flesh instead
# thereof."
m.step("Gen.2.21")
# ‹וַיַּפֵּל … תַּרְדֵּמָה עַל־הָאָדָם וַיִּישָׁן› event: cast-sleep — agent
# the-LORD-God; theme deep-sleep
m.event("cast_sleep", agent="YHWH_Elohim", themes=["tardemah"])
# ‹וַיִּקַּח אַחַת מִצַּלְעֹתָיו› event: take — agent the-LORD-God; theme
# side
m.event("take", agent="YHWH_Elohim", themes=["tzela"])
# ‹וַיִּסְגֹּר בָּשָׂר תַּחְתֶּנָּה› event: close — agent the-LORD-God;
# theme flesh
m.event("close", agent="YHWH_Elohim", themes=["basar"])

# -------------------------- Gen.2.22 · BUILD_WOMAN_RECEIPT -----------------
# וַיִּבֶן יְהוָה אֱלֹהִים אֶת־הַצֵּלָע אֲשֶׁר־לָקַח מִן־הָאָדָם לְאִשָּׁה
# וַיְבִאֶהָ אֶל־הָאָדָם
# "And the rib, which the LORD God had taken from the man, made He a woman,
# and brought her unto the man."
m.step("Gen.2.22")
# ‹וַיִּבֶן … אֶת־הַצֵּלָע … לְאִשָּׁה› event: build — agent the-LORD-God;
# theme woman
m.event("build", agent="YHWH_Elohim", themes=["ishah"])
# ‹לְאִשָּׁה› the world gains: woman
m.install("ishah")
# ‹וַיִּבֶן … וַיְבִאֶהָ אֶל־הָאָדָם› demand settled (popped from the
# queue): make(helper-corresponding-to-him, to-human)
m.result("make(ezer_kenegdo, le_adam)", tmark="t1")
# spec-delta — spec said e'I-will-make (I will MAKE — make, the week's build
# verb), delivery says and-he-built (He BUILT — build, first token)
m.spec_delta("e'eseh (I will MAKE — asah, the week's build verb)",
             "va-yiven (He BUILT — banah, first token)")

# -------------------------- Gen.2.23 · FIRST_HUMAN_SPEECH_NAME -------------
# וַיֹּאמֶר הָאָדָם זֹאת הַפַּעַם עֶצֶם מֵעֲצָמַי וּבָשָׂר מִבְּשָׂרִי
# לְזֹאת יִקָּרֵא אִשָּׁה כִּי מֵאִישׁ לֻקֳחָה־זֹּאת
# "And the man said: 'This is now bone of my bones, and flesh of my flesh;
# she shall be called Woman, because she was taken out of Man.'"
m.step("Gen.2.23")
# ‹וַיֹּאמֶר הָאָדָם› event: say — agent human
m.event("say", agent="adam")
# ‹לְזֹאת יִקָּרֵא אִשָּׁה כִּי מֵאִישׁ לֻקֳחָה־זֹּאת› named: woman := woman
m.name("ishah", "ishah")

# -------------------------- Gen.2.24 · ETIOLOGY_PATTERN --------------------
# עַל־כֵּן יַעֲזָב־אִישׁ אֶת־אָבִיו וְאֶת־אִמּוֹ וְדָבַק בְּאִשְׁתּוֹ
# וְהָיוּ לְבָשָׂר אֶחָד
# "Therefore shall a man leave his father and his mother, and shall cleave
# unto his wife, and they shall be one flesh."
m.step("Gen.2.24")
# ‹עַל־כֵּן יַעֲזָב־אִישׁ … וְדָבַק … וְהָיוּ לְבָשָׂר אֶחָד› pattern
# recorded: leave(man, father-and-mother) ∧ cleave(man, in-his-wife) ∧ they-
# become(one-flesh)
m.pattern("azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)")

# -------------------------- Gen.2.25 · CLOSING_STATE_BRIDGE ----------------
# וַיִּהְיוּ שְׁנֵיהֶם עֲרוּמִּים הָאָדָם וְאִשְׁתּוֹ וְלֹא יִתְבֹּשָׁשׁוּ
# "And they were both naked, the man and his wife, and were not ashamed."
m.step("Gen.2.25")
# ‹עֲרוּמִּים … וְלֹא יִתְבֹּשָׁשׁוּ› fact holds: naked(the-human-and-his-
# wife); were-not-ashamed(both-of-them)
m.fact("arumim(ha_adam_ve_ishto)",
       "lo_yitboshashu(shneihem)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ishah', 'of_ha_shamayim', 'chayat_ha_sadeh'}
    assert m.presupposed_set() == {'adamah', 'behemah', 'adam'}
    assert m.REGISTRY["names"] == {'ishah': 'ishah'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == [('FAIL', 'tov', 'heyot_ha_adam_levado')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['hu_shemo(kol_asher_yiqra_lo_ha_adam)', 'lo_matza(ezer_kenegdo, le_adam)', 'pattern: azav(ish, av_ve_em) ∧ davak(ish, be_ishto) ∧ hayu(basar_echad)', 'arumim(ha_adam_ve_ishto)', 'lo_yitboshashu(shneihem)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_10_serpent_violation_trace
###############################################################################
# =============================================================================
# gen_10_serpent_violation_trace — 3:1-13
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_10_serpent_violation_trace.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden III: the serpent, the misquoted rule, the eating, the interrogation (3:1-13)"""
from machine import Machine

m = Machine("gen_10_serpent_violation_trace")

# -------------------------- Gen.3.1 · SERPENT_ONSET_INVERTED_QUOTE ---------
# וְהַנָּחָשׁ הָיָה עָרוּם מִכֹּל חַיַּת הַשָּׂדֶה אֲשֶׁר עָשָׂה יְהוָה
# אֱלֹהִים וַיֹּאמֶר אֶל־הָאִשָּׁה אַף כִּי־אָמַר אֱלֹהִים לֹא תֹאכְלוּ
# מִכֹּל עֵץ הַגָּן
# "Now the serpent was more subtle than any beast of the field which the
# LORD God had made. And he said unto the woman: 'Yea, hath God said: Ye
# shall not eat of any tree of the garden?'"
m.step("Gen.3.1")
# ‹וְהַנָּחָשׁ הָיָה עָרוּם … אֲשֶׁר עָשָׂה יְהוָה אֱלֹהִים› fact holds:
# cunning(serpent); make-the-LORD-God(serpent)
m.fact("arum(nachash)",
       "asah_YHWH_Elohim(nachash)")
# reads without prior install (flag, not fix): serpent, woman, garden
m.presupposed("nachash", "ishah", "gan")
# ‹וַיֹּאמֶר אֶל־הָאִשָּׁה אַף כִּי־אָמַר אֱלֹהִים› event: say — agent
# serpent; theme woman
m.event("say", agent="nachash", themes=["ishah"])
# spec-delta — spec said eating eat who-all tree-of the-garden + one
# exclusion (gen-08 2:16-17: permission over ALL, prohibition on ONE),
# delivery says not you-shall-eat(pl) who-all tree-of the-garden (the
# serpent: negation over ALL — the scope INVERTED, and the addressee
# pluralized 2ms->2mp)
m.spec_delta("akhol tokhel mi-kol etz ha-gan + one exclusion (gen_08 2:16-17: permission over ALL, prohibition on ONE)",
             "lo tokhlu mi-kol etz ha-gan (the serpent: negation over ALL — the scope INVERTED, and the addressee pluralized 2ms->2mp)")
# spec-delta — spec said the-LORD-God (the rule's issuer, gen-08 2:16 — the
# Eden-exclusive compound), delivery says God (the serpent
m.spec_delta("YHWH_Elohim (the rule's issuer, gen_08 2:16 — the Eden-exclusive compound)",
             "Elohim (the serpent")

# -------------------------- Gen.3.2 · WOMAN_PERMISSION_REDUCED -------------
# וַתֹּאמֶר הָאִשָּׁה אֶל־הַנָּחָשׁ מִפְּרִי עֵץ־הַגָּן נֹאכֵל
# "And the woman said unto the serpent: 'Of the fruit of the trees of the
# garden we may eat.'"
m.step("Gen.3.2")
# ‹וַתֹּאמֶר הָאִשָּׁה אֶל־הַנָּחָשׁ› event: say — agent woman; theme
# serpent
m.event("say", agent="ishah", themes=["nachash"])
# spec-delta — spec said who-KOL tree-of the-garden AKHOL TOKHEL (gen-08
# 2:16: from ALL, with the emphatic doubling — the corpus first doubling),
# delivery says who-fruit-of tree-of-the-garden we-may-eat (the woman: no
# who-all, no doubling — from the fruit fowl the garden trees we may eat)
m.spec_delta("mi-KOL etz ha-gan AKHOL TOKHEL (gen_08 2:16: from ALL, with the emphatic doubling — the corpus first doubling)",
             "mi-peri etz-ha-gan nokhel (the woman: no mi-kol, no doubling — from the fruit of the garden trees we may eat)")

# -------------------------- Gen.3.3 · WOMAN_FENCE_AND_SOFTENED_PENALTY -----
# וּמִפְּרִי הָעֵץ אֲשֶׁר בְּתוֹךְ־הַגָּן אָמַר אֱלֹהִים לֹא תֹאכְלוּ
# מִמֶּנּוּ וְלֹא תִגְּעוּ בּוֹ פֶּן־תְּמֻתוּן
# "'But of the fruit of the tree which is in the midst of the garden, God
# hath said: Ye shall not eat of it, neither shall ye touch it, lest ye
# die.'"
m.step("Gen.3.3")
# reads without prior install (flag, not fix): the-tree-of
m.presupposed("ha_etz")
# spec-delta — spec said from-tree-of the-knowledge good and-evil (gen-08
# 2:17: the tree named by its knowledge; located nowhere), delivery says
# the-tree-of which in-midst-of the-garden (the woman: the tree IN THE MIDST
# — the address 2:9 states for the tree fowl LIFE)
m.spec_delta("me-etz ha-daat tov va-ra (gen_08 2:17: the tree named by its knowledge; located nowhere)",
             "ha-etz asher be-tokh ha-gan (the woman: the tree IN THE MIDST — the address 2:9 states for the tree of LIFE)")
# ‹וְלֹא תִגְּעוּ בּוֹ› spec-delta — spec said not she-ate from-it (gen-08
# 2:17: eating prohibited — nothing else), delivery says not you-shall-
# eat(pl) from-it VE-LO TIGU BO (eating AND TOUCHING prohibited — a fence
# added to the rule)
m.spec_delta("lo tokhal mimenu (gen_08 2:17: eating prohibited — nothing else)",
             "lo tokhlu mimenu VE-LO TIGU BO (eating AND TOUCHING prohibited — a fence added to the rule)")
# spec-delta — spec said that in-day-of your-eating from-it dying you-shall-
# die (gen-08 2:17: certainty ON THE DAY, with the death-doubling), delivery
# says lest-you-shall-die (the woman: LEST you die — risk for certainty, no
# doubling, no day-clock)
m.spec_delta("ki be-yom akholkha mimenu mot tamut (gen_08 2:17: certainty ON THE DAY, with the death-doubling)",
             "pen-temutun (the woman: LEST you die — risk for certainty, no doubling, no day-clock)")

# -------------------------- Gen.3.4 · SERPENT_CONTRADICTION ----------------
# וַיֹּאמֶר הַנָּחָשׁ אֶל־הָאִשָּׁה לֹא־מוֹת תְּמֻתוּן
# "And the serpent said unto the woman: 'Ye shall not surely die.'"
m.step("Gen.3.4")
# ‹וַיֹּאמֶר הַנָּחָשׁ אֶל־הָאִשָּׁה› event: say — agent serpent; theme
# woman
m.event("say", agent="nachash", themes=["ishah"])
# ‹לֹא־מוֹת תְּמֻתוּן› spec-delta — spec said dying you-shall-die (gen-08
# 2:17: the penalty, doubled — the emphatic device the woman had dropped),
# delivery says LO-dying you-shall-die (the serpent: the doubling RESTORED
# in order to in NEGATED — the corpus first direct contradiction fowl a
# divine word)
m.spec_delta("mot tamut (gen_08 2:17: the penalty, doubled — the emphatic device the woman had dropped)",
             "LO-mot temutun (the serpent: the doubling RESTORED in order to be NEGATED — the corpus first direct contradiction of a divine word)")

# -------------------------- Gen.3.5 · SERPENT_COUNTER_THEORY ---------------
# כִּי יֹדֵעַ אֱלֹהִים כִּי בְּיוֹם אֲכָלְכֶם מִמֶּנּוּ וְנִפְקְחוּ
# עֵינֵיכֶם וִהְיִיתֶם כֵּאלֹהִים יֹדְעֵי טוֹב וָרָע
# "'For God doth know that in the day ye eat thereof, then your eyes shall
# be opened, and ye shall be as God, knowing good and evil.'"
m.step("Gen.3.5")
# ‹כִּי יֹדֵעַ אֱלֹהִים … וְנִפְקְחוּ … וִהְיִיתֶם כֵּאלֹהִים› event: claim
# — agent serpent; theme were-opened-your-eyes, like-God
m.event("claim", agent="nachash", themes=["nifqechu_eineikhem", "ke_Elohim"])

# -------------------------- Gen.3.6 · CREATURE_TEST_AND_TRIGGER ------------
# וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ לְמַאֲכָל וְכִי תַאֲוָה־הוּא לָעֵינַיִם
# וְנֶחְמָד הָעֵץ לְהַשְׂכִּיל וַתִּקַּח מִפִּרְיוֹ וַתֹּאכַל וַתִּתֵּן
# גַּם־לְאִישָׁהּ עִמָּהּ וַיֹּאכַל
# "And when the woman saw that the tree was good for food, and that it was a
# delight to the eyes, and that the tree was to be desired to make one wise,
# she took of the fruit thereof, and did eat; and she gave also unto her
# husband with her, and he did eat."
m.step("Gen.3.6")
# ‹וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ לְמַאֲכָל› test PASS — oracle-word
# good, on the-tree-of-to-food
m.test("PASS", "tov", "ha_etz_le_maakhal")
# ‹וַתִּקַּח מִפִּרְיוֹ› event: take — agent woman; theme fruit
m.event("take", agent="ishah", themes=["pri"])
# ‹וַתֹּאכַל› event: eat — agent woman; theme fruit
m.event("eat", agent="ishah", themes=["pri"])
# ‹וַתִּתֵּן גַּם־לְאִישָׁהּ עִמָּהּ› event: give — agent woman; theme human
m.event("give", agent="ishah", themes=["adam"])
# ‹וַיֹּאכַל› event: eat — agent human; theme fruit
m.event("eat", agent="adam", themes=["pri"])
# reads without prior install (flag, not fix): human
m.presupposed("adam")

# -------------------------- Gen.3.7 · EYES_OPEN_FIRST_MANUFACTURE ----------
# וַתִּפָּקַחְנָה עֵינֵי שְׁנֵיהֶם וַיֵּדְעוּ כִּי עֵירֻמִּם הֵם
# וַיִּתְפְּרוּ עֲלֵה תְאֵנָה וַיַּעֲשׂוּ לָהֶם חֲגֹרֹת
# "And the eyes of them both were opened, and they knew that they were
# naked; and they sewed fig-leaves together, and made themselves girdles."
m.step("Gen.3.7")
# ‹וַתִּפָּקַחְנָה עֵינֵי שְׁנֵיהֶם› event: open-eyes — theme eyes-of-both-
# of-them
m.event("open_eyes", themes=["einei_shneihem"])
# ‹וַיֵּדְעוּ כִּי עֵירֻמִּם הֵם› event: know — agent both-of-them; theme
# naked
m.event("know", agent="shneihem", themes=["eirummim"])
# ‹וַיִּתְפְּרוּ עֲלֵה תְאֵנָה וַיַּעֲשׂוּ לָהֶם חֲגֹרֹת› event: make —
# agent both-of-them; theme girdles
m.event("make", agent="shneihem", themes=["chagorot"])
# ‹חֲגֹרֹת› the world gains: girdles
m.install("chagorot")

# -------------------------- Gen.3.8 · VOICE_AND_HIDING ---------------------
# וַיִּשְׁמְעוּ אֶת־קוֹל יְהוָה אֱלֹהִים מִתְהַלֵּךְ בַּגָּן לְרוּחַ הַיּוֹם
# וַיִּתְחַבֵּא הָאָדָם וְאִשְׁתּוֹ מִפְּנֵי יְהוָה אֱלֹהִים בְּתוֹךְ עֵץ
# הַגָּן
# "And they heard the voice of the LORD God walking in the garden toward the
# cool of the day; and the man and his wife hid themselves from the presence
# of the LORD God amongst the trees of the garden."
m.step("Gen.3.8")
# ‹וַיִּשְׁמְעוּ אֶת־קוֹל יְהוָה אֱלֹהִים מִתְהַלֵּךְ בַּגָּן› event: hear —
# agent both-of-them; theme voice-of-the-LORD-God
m.event("hear", agent="shneihem", themes=["qol_YHWH_Elohim"])
# ‹וַיִּתְחַבֵּא הָאָדָם וְאִשְׁתּוֹ … בְּתוֹךְ עֵץ הַגָּן› event: hide —
# agent both-of-them; theme in-midst-of-tree-of-the-garden
m.event("hide", agent="shneihem", themes=["be_tokh_etz_ha_gan"])

# -------------------------- Gen.3.9 · FIRST_QUESTION -----------------------
# וַיִּקְרָא יְהוָה אֱלֹהִים אֶל־הָאָדָם וַיֹּאמֶר לוֹ אַיֶּכָּה
# "And the LORD God called unto the man, and said unto him: 'Where art
# thou?'"
m.step("Gen.3.9")
# ‹וַיִּקְרָא יְהוָה אֱלֹהִים אֶל־הָאָדָם› event: call — agent the-LORD-God;
# theme human
m.event("call", agent="YHWH_Elohim", themes=["adam"])
# ‹אַיֶּכָּה› event: ask — agent the-LORD-God; theme where-are-you
m.event("ask", agent="YHWH_Elohim", themes=["ayeka"])

# -------------------------- Gen.3.10 · TESTIMONY_FEAR ----------------------
# וַיֹּאמֶר אֶת־קֹלְךָ שָׁמַעְתִּי בַּגָּן וָאִירָא כִּי־עֵירֹם אָנֹכִי
# וָאֵחָבֵא
# "And he said: 'I heard Thy voice in the garden, and I was afraid, because
# I was naked; and I hid myself.'"
m.step("Gen.3.10")
# ‹וַיֹּאמֶר אֶת־קֹלְךָ שָׁמַעְתִּי בַּגָּן› event: say — agent human; theme
# the-LORD-God
m.event("say", agent="adam", themes=["YHWH_Elohim"])
# ‹וָאִירָא כִּי־עֵירֹם אָנֹכִי וָאֵחָבֵא› fact holds: testimony-feared-
# naked-hid(human)
m.fact("testimony_feared_naked_hid(adam)")

# -------------------------- Gen.3.11 · RULE_QUOTED_BACK --------------------
# וַיֹּאמֶר מִי הִגִּיד לְךָ כִּי עֵירֹם אָתָּה הֲמִן־הָעֵץ אֲשֶׁר
# צִוִּיתִיךָ לְבִלְתִּי אֲכָל־מִמֶּנּוּ אָכָלְתָּ
# "And He said: 'Who told thee that thou wast naked? Hast thou eaten of the
# tree, whereof I commanded thee that thou shouldest not eat?'"
m.step("Gen.3.11")
# ‹מִי הִגִּיד לְךָ … הֲמִן־הָעֵץ אֲשֶׁר צִוִּיתִיךָ לְבִלְתִּי
# אֲכָל־מִמֶּנּוּ אָכָלְתָּ› event: ask — agent the-LORD-God; theme who-
# told, you-have-eaten
m.event("ask", agent="YHWH_Elohim", themes=["mi_higid", "akhalta"])

# -------------------------- Gen.3.12 · BLAME_CHAIN_ADMISSION_1 -------------
# וַיֹּאמֶר הָאָדָם הָאִשָּׁה אֲשֶׁר נָתַתָּה עִמָּדִי הִוא נָתְנָה־לִּי
# מִן־הָעֵץ וָאֹכֵל
# "And the man said: 'The woman whom Thou gavest to be with me, she gave me
# of the tree, and I did eat.'"
m.step("Gen.3.12")
# ‹הָאִשָּׁה אֲשֶׁר נָתַתָּה עִמָּדִי הִוא נָתְנָה־לִּי› event: say — agent
# human; theme woman
m.event("say", agent="adam", themes=["ishah"])
# ‹וָאֹכֵל› fact holds: admission-and-I-ate(human)
m.fact("admission_va_okhel(adam)")

# -------------------------- Gen.3.13 · ADMISSION_2_HAPAX_DECEIT ------------
# וַיֹּאמֶר יְהוָה אֱלֹהִים לָאִשָּׁה מַה־זֹּאת עָשִׂית וַתֹּאמֶר הָאִשָּׁה
# הַנָּחָשׁ הִשִּׁיאַנִי וָאֹכֵל
# "And the LORD God said unto the woman: 'What is this thou hast done?' And
# the woman said: 'The serpent beguiled me, and I did eat.'"
m.step("Gen.3.13")
# ‹מַה־זֹּאת עָשִׂית› event: ask — agent the-LORD-God; theme woman
m.event("ask", agent="YHWH_Elohim", themes=["ishah"])
# ‹הַנָּחָשׁ הִשִּׁיאַנִי› event: say — agent woman; theme serpent
m.event("say", agent="ishah", themes=["nachash"])
# ‹וָאֹכֵל› fact holds: admission-and-I-ate(woman)
m.fact("admission_va_okhel(ishah)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'chagorot'}
    assert m.presupposed_set() == {'gan', 'adam', 'ishah', 'ha_etz', 'nachash'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tov', 'ha_etz_le_maakhal')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 7}
    assert sorted(m.WORLD["facts"]) == sorted(['arum(nachash)', 'asah_YHWH_Elohim(nachash)', 'testimony_feared_naked_hid(adam)', 'admission_va_okhel(adam)', 'admission_va_okhel(ishah)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 20
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_11_sentences_exile
###############################################################################
# =============================================================================
# gen_11_sentences_exile — 3:14-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_11_sentences_exile.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden IV: the sentences, the skin garments, the exile (3:14-24)"""
from machine import Machine

m = Machine("gen_11_sentences_exile")

# -------------------------- Gen.3.14 · SENTENCE_SERPENT_FIRST_CURSE --------
# וַיֹּאמֶר יְהוָה אֱלֹהִים אֶל־הַנָּחָשׁ כִּי עָשִׂיתָ זֹּאת אָרוּר אַתָּה
# מִכָּל־הַבְּהֵמָה וּמִכֹּל חַיַּת הַשָּׂדֶה עַל־גְּחֹנְךָ תֵלֵךְ וְעָפָר
# תֹּאכַל כָּל־יְמֵי חַיֶּיךָ
# "And the LORD God said unto the serpent: 'Because thou hast done this,
# cursed art thou from among all cattle, and from among all beasts of the
# field; upon thy belly shalt thou go, and dust shalt thou eat all the days
# of thy life.'"
m.step("Gen.3.14")
# ‹וַיֹּאמֶר … אֶל־הַנָּחָשׁ כִּי עָשִׂיתָ זֹּאת› event: sentence — agent
# the-LORD-God; theme serpent
m.event("sentence", agent="YHWH_Elohim", themes=["nachash"])
# reads without prior install (flag, not fix): serpent
m.presupposed("nachash")
# ‹אָרוּר אַתָּה מִכָּל־הַבְּהֵמָה› role assigned: serpent -> CURSED-from-
# all-the-livestock
m.assign("nachash", "arur_mi_kol_ha_behemah")
# ‹עַל־גְּחֹנְךָ תֵלֵךְ וְעָפָר תֹּאכַל› fact holds: upon-your-belly-you-
# shall-go(serpent); dust-you-shall-eat-all-days-of-your-life(serpent)
m.fact("al_gechonkha_telekh(nachash)",
       "afar_tokhal_kol_yemei_chayekha(nachash)")

# -------------------------- Gen.3.15 · ENMITY_PROGRAM ----------------------
# וְאֵיבָה אָשִׁית בֵּינְךָ וּבֵין הָאִשָּׁה וּבֵין זַרְעֲךָ וּבֵין זַרְעָהּ
# הוּא יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב
# "'And I will put enmity between thee and the woman, and between thy seed
# and her seed; they shall bruise thy head, and thou shalt bruise their
# heel.'"
m.step("Gen.3.15")
# ‹וְאֵיבָה אָשִׁית … הוּא יְשׁוּפְךָ רֹאשׁ וְאַתָּה תְּשׁוּפֶנּוּ עָקֵב›
# pattern recorded: enmity(between-seed-the-woman, between-seed-the-serpent)
# ∧ he-shall-bruise-you-head ∧ you-shall-bruise-him-heel
m.pattern("eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev")

# -------------------------- Gen.3.16 · SENTENCE_WOMAN ----------------------
# אֶל־הָאִשָּׁה אָמַר הַרְבָּה אַרְבֶּה עִצְּבוֹנֵךְ וְהֵרֹנֵךְ בְּעֶצֶב
# תֵּלְדִי בָנִים וְאֶל־אִישֵׁךְ תְּשׁוּקָתֵךְ וְהוּא יִמְשָׁל־בָּךְ
# "Unto the woman He said: 'I will greatly multiply thy pain and thy
# travail; in pain thou shalt bring forth children; and thy desire shall be
# to thy husband, and he shall rule over thee.'"
m.step("Gen.3.16")
# reads without prior install (flag, not fix): woman
m.presupposed("ishah")
# ‹הַרְבָּה אַרְבֶּה עִצְּבוֹנֵךְ … בְּעֶצֶב תֵּלְדִי בָנִים … וְהוּא
# יִמְשָׁל־בָּךְ› fact holds: greatly-I-will-multiply-your-toil-and-your-
# pregnancy(woman); in-pain-you-shall-bear-sons(woman); to-your-husband-
# your-desire-and-he-shall-rule-in-you(woman)
m.fact("harbah_arbeh_itzvonekh_ve_heronekh(ishah)",
       "be_etzev_teldi_vanim(ishah)",
       "el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)")

# -------------------------- Gen.3.17 · SENTENCE_MAN_GROUND_CURSED ----------
# וּלְאָדָם אָמַר כִּי־שָׁמַעְתָּ לְקוֹל אִשְׁתֶּךָ וַתֹּאכַל מִן־הָעֵץ
# אֲשֶׁר צִוִּיתִיךָ לֵאמֹר לֹא תֹאכַל מִמֶּנּוּ אֲרוּרָה הָאֲדָמָה
# בַּעֲבוּרֶךָ בְּעִצָּבוֹן תֹּאכֲלֶנָּה כֹּל יְמֵי חַיֶּיךָ
# "And unto Adam He said: 'Because thou hast hearkened unto the voice of thy
# wife, and hast eaten of the tree, of which I commanded thee, saying: Thou
# shalt not eat of it; cursed is the ground for thy sake; in toil shalt thou
# eat of it all the days of thy life.'"
m.step("Gen.3.17")
# ‹וּלְאָדָם אָמַר כִּי־שָׁמַעְתָּ לְקוֹל אִשְׁתֶּךָ … אֲשֶׁר צִוִּיתִיךָ
# לֵאמֹר לֹא תֹאכַל מִמֶּנּוּ› event: sentence — agent the-LORD-God; theme
# Adam
m.event("sentence", agent="YHWH_Elohim", themes=["adam"])
# reads without prior install (flag, not fix): Adam, ground
m.presupposed("adam", "adamah")
# ‹אֲרוּרָה הָאֲדָמָה בַּעֲבוּרֶךָ› role assigned: ground -> cursed-for-
# your-sake
m.assign("adamah", "arurah_baavurekha")
# ‹בְּעִצָּבוֹן תֹּאכֲלֶנָּה כֹּל יְמֵי חַיֶּיךָ› fact holds: in-toil-you-
# shall-eat-all-days-of-your-life(Adam)
m.fact("be_itzavon_tokhalenah_kol_yemei_chayekha(adam)")

# -------------------------- Gen.3.18 · THORN_DIET --------------------------
# וְקוֹץ וְדַרְדַּר תַּצְמִיחַ לָךְ וְאָכַלְתָּ אֶת־עֵשֶׂב הַשָּׂדֶה
# "'Thorns also and thistles shall it bring forth to thee; and thou shalt
# eat the herb of the field.'"
m.step("Gen.3.18")
# ‹וְקוֹץ וְדַרְדַּר תַּצְמִיחַ … וְאָכַלְתָּ אֶת־עֵשֶׂב הַשָּׂדֶה› fact
# holds: thorn-and-thistle-tatzmiach-to-you(ground); and-you-shall-eat-obj-
# marker·et-herb-of-the-field(Adam)
m.fact("kotz_ve_dardar_tatzmiach_lakh(adamah)",
       "ve_akhalta_et_esev_ha_sadeh(adam)")

# -------------------------- Gen.3.19 · MORTALITY_BOUNDARY ------------------
# בְּזֵעַת אַפֶּיךָ תֹּאכַל לֶחֶם עַד שׁוּבְךָ אֶל־הָאֲדָמָה כִּי מִמֶּנָּה
# לֻקָּחְתָּ כִּי־עָפָר אַתָּה וְאֶל־עָפָר תָּשׁוּב
# "'In the sweat of thy face shalt thou eat bread, till thou return unto the
# ground; for out of it wast thou taken; for dust thou art, and unto dust
# shalt thou return.'"
m.step("Gen.3.19")
# ‹בְּזֵעַת אַפֶּיךָ … עַד שׁוּבְךָ … וְאֶל־עָפָר תָּשׁוּב› fact holds: in-
# sweat-of-your-nostrils-you-shall-eat-bread(Adam); until-your-return-to-
# the-ground(Adam); dust-you-and-to-dust-you-shall-return(Adam)
m.fact("be_zeat_apekha_tokhal_lechem(adam)",
       "ad_shuvkha_el_ha_adamah(adam)",
       "afar_atah_ve_el_afar_tashuv(adam)")
# ‹מוֹת תָּמוּת … עַד שׁוּבְךָ› spec-delta — spec said because in-day your-
# eating from-it dying you-shall-die (gen-08 2:17 — the armed HANDLER:
# dying-you-shall-die, IN THE DAY), delivery says until your-return to-the-
# ground … and-to-dust you-shall-return (the sentence: toil-terms +
# mortality as BOUNDARY — the return to dust as horizon; same-day death not
# executed)
m.spec_delta("ki be-yom akholkha mimenu mot tamut (gen_08 2:17 — the armed HANDLER: dying-you-shall-die, IN THE DAY)",
             "ad shuvkha el-ha-adamah … ve-el-afar tashuv (the sentence: toil-terms + mortality as BOUNDARY — the return to dust as horizon; same-day death not executed)")

# -------------------------- Gen.3.20 · NAME_CHAVAH -------------------------
# וַיִּקְרָא הָאָדָם שֵׁם אִשְׁתּוֹ חַוָּה כִּי הִוא הָיְתָה אֵם כָּל־חָי
# "And the man called his wife's name Eve; because she was the mother of all
# living."
m.step("Gen.3.20")
# ‹וַיִּקְרָא הָאָדָם שֵׁם אִשְׁתּוֹ חַוָּה כִּי הִוא הָיְתָה אֵם כָּל־חָי›
# named: woman := Chavah
m.name("ishah", "Chavah")

# -------------------------- Gen.3.21 · SKIN_GARMENTS -----------------------
# וַיַּעַשׂ יְהוָה אֱלֹהִים לְאָדָם וּלְאִשְׁתּוֹ כָּתְנוֹת עוֹר
# וַיַּלְבִּשֵׁם
# "And the LORD God made for Adam and for his wife garments of skins, and
# clothed them."
m.step("Gen.3.21")
# ‹וַיַּעַשׂ … כָּתְנוֹת עוֹר› event: make — agent the-LORD-God; theme
# garments-of-skin
m.event("make", agent="YHWH_Elohim", themes=["kotnot_or"])
# ‹וַיַּלְבִּשֵׁם› event: clothe — agent the-LORD-God; theme Adam
m.event("clothe", agent="YHWH_Elohim", themes=["adam"])
# ‹כָּתְנוֹת עוֹר› the world gains: garments-of-skin
m.install("kotnot_or")

# -------------------------- Gen.3.22 · COUNCIL_CONCERN_SECOND_TREE ---------
# וַיֹּאמֶר יְהוָה אֱלֹהִים הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ לָדַעַת
# טוֹב וָרָע וְעַתָּה פֶּן־יִשְׁלַח יָדוֹ וְלָקַח גַּם מֵעֵץ הַחַיִּים
# וְאָכַל וָחַי לְעֹלָם
# "And the LORD God said: 'Behold, the man is become as one of us, to know
# good and evil; and now, lest he put forth his hand, and take also of the
# tree of life, and eat, and live for ever.'"
m.step("Gen.3.22")
# ‹הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ› event: deliberate — agent the-LORD-
# God; theme Adam
m.event("deliberate", agent="YHWH_Elohim", themes=["adam"])
# ‹וְעַתָּה פֶּן־יִשְׁלַח יָדוֹ וְלָקַח גַּם מֵעֵץ הַחַיִּים וְאָכַל וָחַי
# לְעֹלָם› fact holds: like-one-from-it-to-know-good-and-evil(Adam); lest-
# he-send-his-hand-and-take-from-tree-the-life-and-living-to-forever
m.fact("ke_achad_mimenu_la_daat_tov_va_ra(adam)",
       "pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam")
# reads without prior install (flag, not fix): tree-of-life, garden-of
m.presupposed("etz_ha_chayim", "gan")

# -------------------------- Gen.3.23 · EXPULSION_WORK_HALF -----------------
# וַיְשַׁלְּחֵהוּ יְהוָה אֱלֹהִים מִגַּן־עֵדֶן לַעֲבֹד אֶת־הָאֲדָמָה אֲשֶׁר
# לֻקַּח מִשָּׁם
# "Therefore the LORD God sent him forth from the garden of Eden, to till
# the ground from whence he was taken."
m.step("Gen.3.23")
# ‹וַיְשַׁלְּחֵהוּ … מִגַּן־עֵדֶן לַעֲבֹד אֶת־הָאֲדָמָה אֲשֶׁר לֻקַּח
# מִשָּׁם› event: send-out — agent the-LORD-God; theme Adam
m.event("send_out", agent="YHWH_Elohim", themes=["adam"])

# -------------------------- Gen.3.24 · GUARDS_INSTALLED_WAY_KEPT -----------
# וַיְגָרֶשׁ אֶת־הָאָדָם וַיַּשְׁכֵּן מִקֶּדֶם לְגַן־עֵדֶן אֶת־הַכְּרֻבִים
# וְאֵת לַהַט הַחֶרֶב הַמִּתְהַפֶּכֶת לִשְׁמֹר אֶת־דֶּרֶךְ עֵץ הַחַיִּים
# "So He drove out the man; and He placed at the east of the garden of Eden
# the cherubim, and the flaming sword which turned every way, to keep the
# way to the tree of life."
m.step("Gen.3.24")
# ‹וַיְגָרֶשׁ אֶת־הָאָדָם› event: drive-out — agent the-LORD-God; theme Adam
m.event("drive_out", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיַּשְׁכֵּן מִקֶּדֶם לְגַן־עֵדֶן› event: station — agent the-LORD-God;
# theme cherubim
m.event("station", agent="YHWH_Elohim", themes=["keruvim"])
# ‹אֶת־הַכְּרֻבִים וְאֵת לַהַט הַחֶרֶב הַמִּתְהַפֶּכֶת› the world gains:
# cherubim, flame-of-the-sword
m.install("keruvim", "lahat_ha_cherev")
# ‹לִשְׁמֹר אֶת־דֶּרֶךְ עֵץ הַחַיִּים› role assigned: cherubim -> keeper-
# way-of-tree-the-life
m.assign("keruvim", "shomer_derekh_etz_ha_chayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'lahat_ha_cherev', 'kotnot_or', 'keruvim'}
    assert m.presupposed_set() == {'gan', 'adamah', 'etz_ha_chayim', 'adam', 'ishah', 'nachash'}
    assert m.REGISTRY["names"] == {'nachash': 'arur_mi_kol_ha_behemah', 'adamah': 'arurah_baavurekha', 'ishah': 'Chavah', 'keruvim': 'shomer_derekh_etz_ha_chayim'}
    assert m.REGISTRY["writes"] == 4
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['al_gechonkha_telekh(nachash)', 'afar_tokhal_kol_yemei_chayekha(nachash)', 'pattern: eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev', 'harbah_arbeh_itzvonekh_ve_heronekh(ishah)', 'be_etzev_teldi_vanim(ishah)', 'el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)', 'be_itzavon_tokhalenah_kol_yemei_chayekha(adam)', 'kotz_ve_dardar_tatzmiach_lakh(adamah)', 've_akhalta_et_esev_ha_sadeh(adam)', 'be_zeat_apekha_tokhal_lechem(adam)', 'ad_shuvkha_el_ha_adamah(adam)', 'afar_atah_ve_el_afar_tashuv(adam)', 'ke_achad_mimenu_la_daat_tov_va_ra(adam)', 'pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 13
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_12_cain_abel
###############################################################################
# =============================================================================
# gen_12_cain_abel — 4:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_12_cain_abel.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Cain and Abel: first offerings, sin at the door, first murder, the mark (4:1-16)"""
from machine import Machine

m = Machine("gen_12_cain_abel")

# -------------------------- Gen.4.1 · FIRST_BIRTH_NAME_SPEECH --------------
# וְהָאָדָם יָדַע אֶת־חַוָּה אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת־קַיִן וַתֹּאמֶר
# קָנִיתִי אִישׁ אֶת־יְהוָה
# "And the man knew Eve his wife; and she conceived and bore Cain, and said:
# 'I have gotten a man with the help of the LORD.'"
m.step("Gen.4.1")
# ‹וְהָאָדָם יָדַע אֶת־חַוָּה אִשְׁתּוֹ› event: know — agent human; theme
# Chavah-Eve
m.event("know", agent="adam", themes=["chavah"])
# ‹וַתַּהַר וַתֵּלֶד אֶת־קַיִן› event: bear — agent Chavah-Eve; theme Cain
m.event("bear", agent="chavah", themes=["kayin"])
# ‹וַתֹּאמֶר קָנִיתִי אִישׁ אֶת־יְהוָה› named: Cain := Kayin
m.name("kayin", "Kayin")
# reads without prior install (flag, not fix): human, Chavah-Eve
m.presupposed("adam", "chavah")

# -------------------------- Gen.4.2 · SECOND_BIRTH_PROFESSIONS -------------
# וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו אֶת־הָבֶל וַיְהִי־הֶבֶל רֹעֵה צֹאן וְקַיִן
# הָיָה עֹבֵד אֲדָמָה
# "And again she bore his brother Abel. And Abel was a keeper of sheep, but
# Cain was a tiller of the ground."
m.step("Gen.4.2")
# ‹וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו אֶת־הָבֶל› event: bear — agent Chavah-Eve;
# theme Abel
m.event("bear", agent="chavah", themes=["hevel"])
# ‹רֹעֵה צֹאן … עֹבֵד אֲדָמָה› fact holds: shepherd-flock(Abel); worker-of-
# ground(Cain)
m.fact("roeh_tzon(hevel)",
       "oved_adamah(kayin)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")

# -------------------------- Gen.4.3 · FIRST_OFFERING -----------------------
# וַיְהִי מִקֵּץ יָמִים וַיָּבֵא קַיִן מִפְּרִי הָאֲדָמָה מִנְחָה לַיהוָה
# "And in process of time it came to pass, that Cain brought of the fruit of
# the ground an offering unto the LORD."
m.step("Gen.4.3")
# ‹וַיָּבֵא קַיִן מִפְּרִי הָאֲדָמָה מִנְחָה לַיהוָה› event: bring — agent
# Cain; theme offering
m.event("bring", agent="kayin", themes=["minchah"])

# -------------------------- Gen.4.4 · SECOND_OFFERING_FAVOR ----------------
# וְהֶבֶל הֵבִיא גַם־הוּא מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן וַיִּשַׁע יְהוָה
# אֶל־הֶבֶל וְאֶל־מִנְחָתוֹ
# "And Abel, he also brought of the firstlings of his flock and of the fat
# thereof. And the LORD had respect unto Abel and to his offering."
m.step("Gen.4.4")
# ‹וְהֶבֶל הֵבִיא גַם־הוּא מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן› event: bring —
# agent Abel; theme firstlings-of
m.event("bring", agent="hevel", themes=["bekhorot"])
# ‹וַיִּשַׁע יְהוָה אֶל־הֶבֶל וְאֶל־מִנְחָתוֹ› test PASS — oracle-word gaze,
# on Abel-and-his-offering
m.test("PASS", "shaah", "hevel_u_minchato")

# -------------------------- Gen.4.5 · NON_REGARD_FIRST_ANGER ---------------
# וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא שָׁעָה וַיִּחַר לְקַיִן מְאֹד וַיִּפְּלוּ
# פָּנָיו
# "But unto Cain and to his offering He had not respect. And Cain was very
# wroth, and his countenance fell."
m.step("Gen.4.5")
# ‹וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא שָׁעָה› fact holds: not-gaze-to-Cain-and-
# to-his-offering
m.fact("lo_shaah_el_kayin_ve_el_minchato")
# ‹וַיִּחַר לְקַיִן מְאֹד וַיִּפְּלוּ פָּנָיו› event: burn — agent Cain
m.event("burn", agent="kayin")

# -------------------------- Gen.4.6 · ANGER_DIAGNOSTIC ---------------------
# וַיֹּאמֶר יְהוָה אֶל־קָיִן לָמָּה חָרָה לָךְ וְלָמָּה נָפְלוּ פָנֶיךָ
# "And the LORD said unto Cain: 'Why art thou wroth? and why is thy
# countenance fallen?'"
m.step("Gen.4.6")
# ‹לָמָּה חָרָה לָךְ וְלָמָּה נָפְלוּ פָנֶיךָ› event: ask — agent the-LORD;
# theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])

# -------------------------- Gen.4.7 · COUNSEL_FIRST_IF ---------------------
# הֲלוֹא אִם־תֵּיטִיב שְׂאֵת וְאִם לֹא תֵיטִיב לַפֶּתַח חַטָּאת רֹבֵץ
# וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ
# "'If thou doest well, shall it not be lifted up? and if thou doest not
# well, sin coucheth at the door; and unto thee is its desire, but thou
# mayest rule over it.'"
m.step("Gen.4.7")
# ‹אִם־תֵּיטִיב שְׂאֵת› standing handler — if you-do-well(Cain) then uplift
m.handler("teitiv(kayin)",
          "seet")
# ‹וְאִם לֹא תֵיטִיב לַפֶּתַח חַטָּאת רֹבֵץ› standing handler — if not-you-
# do-well(Cain) then to-at-the-door-sin-crouching
m.handler("lo_teitiv(kayin)",
          "la_petach_chattat_rovetz")
# ‹וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ› the-LORD speaks a demand
# — LET?: you-shall-rule(Cain, in-the-sin)
m.declare("YHWH", "LET?",
          "timshol(kayin, ba_chattat)")

# -------------------------- Gen.4.8 · EMPTY_QUOTE_FIRST_MURDER -------------
# וַיֹּאמֶר קַיִן אֶל־הֶבֶל אָחִיו וַיְהִי בִּהְיוֹתָם בַּשָּׂדֶה וַיָּקָם
# קַיִן אֶל־הֶבֶל אָחִיו וַיַּהַרְגֵהוּ
# "And Cain spoke unto Abel his brother. And it came to pass, when they were
# in the field, that Cain rose up against Abel his brother, and slew him."
m.step("Gen.4.8")
# ‹וַיֹּאמֶר קַיִן אֶל־הֶבֶל אָחִיו› event: say — agent Cain; theme Abel
m.event("say", agent="kayin", themes=["hevel"])
# ‹וַיָּקָם קַיִן אֶל־הֶבֶל אָחִיו וַיַּהַרְגֵהוּ› event: kill — agent Cain;
# theme Abel
m.event("kill", agent="kayin", themes=["hevel"])

# -------------------------- Gen.4.9 · DOCKET_FIRST_LIE ---------------------
# וַיֹּאמֶר יְהוָה אֶל־קַיִן אֵי הֶבֶל אָחִיךָ וַיֹּאמֶר לֹא יָדַעְתִּי
# הֲשֹׁמֵר אָחִי אָנֹכִי
# "And the LORD said unto Cain: 'Where is Abel thy brother?' And he said: 'I
# know not; am I my brother's keeper?'"
m.step("Gen.4.9")
# ‹אֵי הֶבֶל אָחִיךָ› event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹לֹא יָדַעְתִּי הֲשֹׁמֵר אָחִי אָנֹכִי› fact holds: not-I-know-the-keeper-
# of-my-brother-I(Cain)
m.fact("lo_yadati_ha_shomer_achi_anokhi(kayin)")

# -------------------------- Gen.4.10 · BLOODS_CRY --------------------------
# וַיֹּאמֶר מֶה עָשִׂיתָ קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן־הָאֲדָמָה
# "And He said: 'What hast thou done? the voice of thy brother's blood
# crieth unto Me from the ground.'"
m.step("Gen.4.10")
# ‹מֶה עָשִׂיתָ› event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן־הָאֲדָמָה› fact holds: all-bloods-
# of-your-brother-crying-out-from-the-ground
m.fact("kol_demei_achikha_tzoakim_min_ha_adamah")

# -------------------------- Gen.4.11 · CURSE_REACHES_HUMAN -----------------
# וְעַתָּה אָרוּר אָתָּה מִן־הָאֲדָמָה אֲשֶׁר פָּצְתָה אֶת־פִּיהָ לָקַחַת
# אֶת־דְּמֵי אָחִיךָ מִיָּדֶךָ
# "'And now cursed art thou from the ground, which hath opened her mouth to
# receive thy brother's blood from thy hand.'"
m.step("Gen.4.11")
# ‹אָרוּר אָתָּה מִן־הָאֲדָמָה› role assigned: Cain -> CURSED-from-the-
# ground
m.assign("kayin", "arur_min_ha_adamah")
# ‹אֲשֶׁר פָּצְתָה אֶת־פִּיהָ› fact holds: the-ground-opened-wide-her-mouth-
# taken-bloods-of(Cain)
m.fact("ha_adamah_patztah_piha_lakachat_demei(kayin)")

# -------------------------- Gen.4.12 · GROUND_STRIKE_WANDERER --------------
# כִּי תַעֲבֹד אֶת־הָאֲדָמָה לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ נָע וָנָד תִּהְיֶה
# בָאָרֶץ
# "'When thou tillest the ground, it shall not henceforth yield unto thee
# her strength; a fugitive and a wanderer shalt thou be in the earth.'"
m.step("Gen.4.12")
# ‹לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ … נָע וָנָד תִּהְיֶה› fact holds: when-you-
# work-not-she-added-give-its-strength(ground, Cain); fugitive-and-wanderer-
# shall-be(Cain)
m.fact("ki_taavod_lo_tosef_tet_kochah(adamah, kayin)",
       "na_va_nad_tihyeh(kayin)")

# -------------------------- Gen.4.13 · PLEA_UNBEARABLE ---------------------
# וַיֹּאמֶר קַיִן אֶל־יְהוָה גָּדוֹל עֲוֺנִי מִנְּשֹׂא
# "And Cain said unto the LORD: 'My punishment is greater than I can bear.'"
m.step("Gen.4.13")
# ‹גָּדוֹל עֲוֺנִי מִנְּשֹׂא› event: plead — agent Cain; theme the-LORD
m.event("plead", agent="kayin", themes=["YHWH"])

# -------------------------- Gen.4.14 · FEAR_OF_FINDERS ---------------------
# הֵן גֵּרַשְׁתָּ אֹתִי הַיּוֹם מֵעַל פְּנֵי הָאֲדָמָה וּמִפָּנֶיךָ אֶסָּתֵר
# וְהָיִיתִי נָע וָנָד בָּאָרֶץ וְהָיָה כָל־מֹצְאִי יַהַרְגֵנִי
# "'Behold, Thou hast driven me out this day from the face of the land; and
# from Thy face shall I be hid; and I shall be a fugitive and a wanderer in
# the earth; and it will come to pass, that whosoever findeth me will slay
# me.'"
m.step("Gen.4.14")
# ‹גֵּרַשְׁתָּ אֹתִי … וּמִפָּנֶיךָ אֶסָּתֵר … כָל־מֹצְאִי יַהַרְגֵנִי› fact
# holds: you-have-driven-out-me-and-from-your-face-I-shall-be-hidden(Cain);
# all-finder-will-kill-me-fear(Cain)
m.fact("gerashta_oti_u_mi_panekha_esater(kayin)",
       "khol_motzi_yahargeni_fear(kayin)")

# -------------------------- Gen.4.15 · SEVENFOLD_HANDLER_MARK --------------
# וַיֹּאמֶר לוֹ יְהוָה לָכֵן כָּל־הֹרֵג קַיִן שִׁבְעָתַיִם יֻקָּם וַיָּשֶׂם
# יְהוָה לְקַיִן אוֹת לְבִלְתִּי הַכּוֹת־אֹתוֹ כָּל־מֹצְאוֹ
# "And the LORD said unto him: 'Therefore whosoever slayeth Cain, vengeance
# shall be taken on him sevenfold.' And the LORD set a sign for Cain, lest
# any finding him should smite him."
m.step("Gen.4.15")
# ‹כָּל־הֹרֵג קַיִן שִׁבְעָתַיִם יֻקָּם› standing handler — if killer-
# of(Cain) then sevenfold-shall-be-avenged
m.handler("horeg(kayin)",
          "shivatayim_yukam")
# ‹וַיָּשֶׂם יְהוָה לְקַיִן אוֹת› fact holds: sign-to-Cain-so-as-not-
# strike(Cain)
m.fact("ot_le_kayin_levilti_hakot(kayin)")

# -------------------------- Gen.4.16 · EXIT_EAST_SETTLED_IN_WANDERING ------
# וַיֵּצֵא קַיִן מִלִּפְנֵי יְהוָה וַיֵּשֶׁב בְּאֶרֶץ־נוֹד קִדְמַת־עֵדֶן
# "And Cain went out from the presence of the LORD, and dwelt in the land of
# Nod, on the east of Eden."
m.step("Gen.4.16")
# ‹וַיֵּצֵא … וַיֵּשֶׁב בְּאֶרֶץ־נוֹד קִדְמַת־עֵדֶן› event: go-out — agent
# Cain; theme land-of-Nod-Wandering-east-of-Eden
m.event("go_out", agent="kayin", themes=["eretz_nod_kidmat_eden"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'chavah', 'adamah', 'adam'}
    assert m.REGISTRY["names"] == {'kayin': 'arur_min_ha_adamah'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'shaah', 'hevel_u_minchato')]
    assert m.open_demands() == ['timshol(kayin, ba_chattat)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1, 'read_before_install': 3, 'assigned_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['roeh_tzon(hevel)', 'oved_adamah(kayin)', 'lo_shaah_el_kayin_ve_el_minchato', 'handler: IF(teitiv(kayin)) THEN(seet)', 'handler: IF(lo_teitiv(kayin)) THEN(la_petach_chattat_rovetz)', 'lo_yadati_ha_shomer_achi_anokhi(kayin)', 'kol_demei_achikha_tzoakim_min_ha_adamah', 'ha_adamah_patztah_piha_lakachat_demei(kayin)', 'ki_taavod_lo_tosef_tet_kochah(adamah, kayin)', 'na_va_nad_tihyeh(kayin)', 'gerashta_oti_u_mi_panekha_esater(kayin)', 'khol_motzi_yahargeni_fear(kayin)', 'handler: IF(horeg(kayin)) THEN(shivatayim_yukam)', 'ot_le_kayin_levilti_hakot(kayin)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_13_cain_line_seth
###############################################################################
# =============================================================================
# gen_13_cain_line_seth — 4:17-26
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_13_cain_line_seth.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Cain's line and Seth: the first city, the crafts, seventy-seven, calling on the Name (4:17-26)"""
from machine import Machine

m = Machine("gen_13_cain_line_seth")

# -------------------------- Gen.4.17 · FIRST_CITY_BUILT_NAMED --------------
# וַיֵּדַע קַיִן אֶת־אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת־חֲנוֹךְ וַיְהִי בֹּנֶה
# עִיר וַיִּקְרָא שֵׁם הָעִיר כְּשֵׁם בְּנוֹ חֲנוֹךְ
# "And Cain knew his wife; and she conceived, and bore Enoch; and he builded
# a city, and called the name of the city after the name of his son Enoch."
m.step("Gen.4.17")
# ‹וַיֵּדַע קַיִן אֶת־אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד אֶת־חֲנוֹךְ› event: bear —
# agent wife-of-Cain; theme Enoch
m.event("bear", agent="eshet_kayin", themes=["chanokh"])
# ‹וַיְהִי בֹּנֶה עִיר› the world gains: city
m.install("ir")
# ‹וַיִּקְרָא שֵׁם הָעִיר כְּשֵׁם בְּנוֹ חֲנוֹךְ› named: city := Chanokh
m.name("ir", "Chanokh")
# reads without prior install (flag, not fix): Cain, wife-of-Cain
m.presupposed("kayin", "eshet_kayin")

# -------------------------- Gen.4.18 · BEGETTING_CHAIN_FOUR_LINKS ----------
# וַיִּוָּלֵד לַחֲנוֹךְ אֶת־עִירָד וְעִירָד יָלַד אֶת־מְחוּיָאֵל
# וּמְחִיּיָאֵל יָלַד אֶת־מְתוּשָׁאֵל וּמְתוּשָׁאֵל יָלַד אֶת־לָמֶךְ
# "And unto Enoch was born Irad; and Irad begot Mehujael; and Mehujael begot
# Methushael; and Methushael begot Lamech."
m.step("Gen.4.18")
# ‹וַיִּוָּלֵד לַחֲנוֹךְ אֶת־עִירָד› event: born — theme Irad
m.event("born", themes=["irad"])
# ‹וְעִירָד יָלַד אֶת־מְחוּיָאֵל› event: beget — agent Irad; theme Mehujael
m.event("beget", agent="irad", themes=["mechuyael"])
# ‹וּמְחִיּיָאֵל יָלַד אֶת־מְתוּשָׁאֵל› event: beget — agent Mehujael; theme
# Methusael
m.event("beget", agent="mechuyael", themes=["metushael"])
# ‹וּמְתוּשָׁאֵל יָלַד אֶת־לָמֶךְ› event: beget — agent Methusael; theme
# Lamech
m.event("beget", agent="metushael", themes=["lemekh"])

# -------------------------- Gen.4.19 · FIRST_POLYGAMY ----------------------
# וַיִּקַּח־לוֹ לֶמֶךְ שְׁתֵּי נָשִׁים שֵׁם הָאַחַת עָדָה וְשֵׁם הַשֵּׁנִית
# צִלָּה
# "And Lamech took unto him two wives; the name of the one was Adah, and the
# name of the other Zillah."
m.step("Gen.4.19")
# ‹וַיִּקַּח־לוֹ לֶמֶךְ שְׁתֵּי נָשִׁים› event: take — agent Lamech; theme
# two-of-wives
m.event("take", agent="lemekh", themes=["shte_nashim"])
# ‹שֵׁם הָאַחַת עָדָה וְשֵׁם הַשֵּׁנִית צִלָּה› fact holds: two-of-wives-to-
# Lamech; name-of-the-first-Adah; name-of-the-second-Tzillah
m.fact("shte_nashim_le_lemekh",
       "shem_ha_achat_adah",
       "shem_ha_shenit_tzilah")

# -------------------------- Gen.4.20 · OFFICE_TENT_AND_HERD ----------------
# וַתֵּלֶד עָדָה אֶת־יָבָל הוּא הָיָה אֲבִי יֹשֵׁב אֹהֶל וּמִקְנֶה
# "And Adah bore Jabal; he was the father of such as dwell in tents and have
# cattle."
m.step("Gen.4.20")
# ‹וַתֵּלֶד עָדָה אֶת־יָבָל› event: bear — agent Adah; theme Yaval
m.event("bear", agent="adah", themes=["yaval"])
# ‹הוּא הָיָה אֲבִי יֹשֵׁב אֹהֶל וּמִקְנֶה› fact holds: father-of-dweller-
# of-tent-and-livestock(Yaval)
m.fact("avi_yoshev_ohel_u_mikneh(yaval)")

# -------------------------- Gen.4.21 · OFFICE_HARP_AND_PIPE ----------------
# וְשֵׁם אָחִיו יוּבָל הוּא הָיָה אֲבִי כָּל־תֹּפֵשׂ כִּנּוֹר וְעוּגָב
# "And his brother's name was Jubal; he was the father of all such as handle
# the harp and pipe."
m.step("Gen.4.21")
# ‹וְשֵׁם אָחִיו יוּבָל הוּא הָיָה אֲבִי כָּל־תֹּפֵשׂ כִּנּוֹר וְעוּגָב›
# fact holds: name-of-his-brother-Yuval; father-of-all-handler-of-harp-and-
# pipe(Yuval)
m.fact("shem_achiv_yuval",
       "avi_kol_tofes_kinor_ve_ugav(yuval)")

# -------------------------- Gen.4.22 · OFFICE_BRONZE_IRON_SISTER -----------
# וְצִלָּה גַם־הִוא יָלְדָה אֶת־תּוּבַל קַיִן לֹטֵשׁ כָּל־חֹרֵשׁ נְחֹשֶׁת
# וּבַרְזֶל וַאֲחוֹת תּוּבַל־קַיִן נַעֲמָה
# "And Zillah, she also bore Tubal-cain, the forger of every cutting
# instrument of brass and iron; and the sister of Tubal-cain was Naamah."
m.step("Gen.4.22")
# ‹וְצִלָּה גַם־הִוא יָלְדָה אֶת־תּוּבַל קַיִן› event: bear — agent Tzillah;
# theme Tuval-Cain
m.event("bear", agent="tzilah", themes=["tuval_kayin"])
# ‹לֹטֵשׁ כָּל־חֹרֵשׁ נְחֹשֶׁת וּבַרְזֶל וַאֲחוֹת תּוּבַל־קַיִן נַעֲמָה›
# fact holds: hammerer-of-all-craftsman-of-bronze-and-iron(Tuval-Cain);
# sister-of-Tuval-Cain-Naamah
m.fact("lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)",
       "achot_tuval_kayin_naamah")

# -------------------------- Gen.4.23 · SWORD_SONG_FIRST_HUMAN_IMPERATIVES --
# וַיֹּאמֶר לֶמֶךְ לְנָשָׁיו עָדָה וְצִלָּה שְׁמַעַן קוֹלִי נְשֵׁי לֶמֶךְ
# הַאְזֵנָּה אִמְרָתִי כִּי אִישׁ הָרַגְתִּי לְפִצְעִי וְיֶלֶד לְחַבֻּרָתִי
# "And Lamech said unto his wives: Adah and Zillah, hear my voice; ye wives
# of Lamech, hearken unto my speech; for I have slain a man for wounding me,
# and a young man for bruising me."
m.step("Gen.4.23")
# ‹וַיֹּאמֶר לֶמֶךְ לְנָשָׁיו עָדָה וְצִלָּה› event: say — agent Lamech;
# theme wives-of-Lamech
m.event("say", agent="lemekh", themes=["neshei_lemekh"])
# ‹שְׁמַעַן קוֹלִי … הַאְזֵנָּה אִמְרָתִי› Lamech speaks a demand — LET:
# hear(wives-of-Lamech, voice-Lamech)
m.declare("lemekh", "LET",
          "shema(neshei_lemekh, qol_lemekh)")
# ‹כִּי אִישׁ הָרַגְתִּי לְפִצְעִי וְיֶלֶד לְחַבֻּרָתִי› fact holds: a-man-
# I-have-killed-to-fitzi-and-a-boy-to-my-wound
m.fact("ish_haragti_le_fitzi_ve_yeled_le_chaburati")

# -------------------------- Gen.4.24 · QUOTE_DIFF_SEVENTY_SEVEN ------------
# כִּי שִׁבְעָתַיִם יֻקַּם־קָיִן וְלֶמֶךְ שִׁבְעִים וְשִׁבְעָה
# "If Cain shall be avenged sevenfold, truly Lamech seventy and sevenfold."
m.step("Gen.4.24")
# ‹כִּי שִׁבְעָתַיִם יֻקַּם־קָיִן וְלֶמֶךְ שִׁבְעִים וְשִׁבְעָה› spec-delta
# — spec said all-slayer Kayin sevenfold shall-be-avenged — issuer the-LORD,
# decree with mark (4:15, frozen gen-12), delivery says for sevenfold shall-
# be-avenged-Kayin and-Lemekh seventy and-seven — issuer Lamech, boast,
# multiplier x11, target self, ratification NONE (4:24)
m.spec_delta("kol-horeg Kayin shivatayim yukam — issuer YHWH, decree with mark (4:15, frozen gen_12)",
             "ki shivatayim yukam-Kayin ve-Lemekh shivim ve-shivah — issuer lemekh, boast, multiplier x11, target self, ratification NONE (4:24)")

# -------------------------- Gen.4.25 · SETH_REPLACEMENT_SEED ---------------
# וַיֵּדַע אָדָם עוֹד אֶת־אִשְׁתּוֹ וַתֵּלֶד בֵּן וַתִּקְרָא אֶת־שְׁמוֹ שֵׁת
# כִּי שָׁת־לִי אֱלֹהִים זֶרַע אַחֵר תַּחַת הֶבֶל כִּי הֲרָגוֹ קָיִן
# "And Adam knew his wife again; and she bore a son, and called his name
# Seth: 'for God hath appointed me another seed instead of Abel; for Cain
# slew him.'"
m.step("Gen.4.25")
# ‹וַיֵּדַע אָדָם עוֹד אֶת־אִשְׁתּוֹ וַתֵּלֶד בֵּן› event: bear — agent
# wife-of-Adam; theme Shet
m.event("bear", agent="eshet_adam", themes=["shet"])
# ‹וַתִּקְרָא אֶת־שְׁמוֹ שֵׁת› named: Shet := Shet
m.name("shet", "Shet")
# ‹כִּי שָׁת־לִי אֱלֹהִים זֶרַע אַחֵר תַּחַת הֶבֶל כִּי הֲרָגוֹ קָיִן› fact
# holds: has-SET-to-me-God-seed-another-place-of-Abel; slew-him-Cain-named-
# in-speech
m.fact("shat_li_elohim_zera_acher_tachat_hevel",
       "harago_kayin_named_in_speech")
# reads without prior install (flag, not fix): Adam, wife-of-Adam
m.presupposed("adam", "eshet_adam")

# -------------------------- Gen.4.26 · ENOSH_CALLING_ON_THE_NAME -----------
# וּלְשֵׁת גַּם־הוּא יֻלַּד־בֵּן וַיִּקְרָא אֶת־שְׁמוֹ אֱנוֹשׁ אָז הוּחַל
# לִקְרֹא בְּשֵׁם יְהוָה
# "And to Seth, to him also there was born a son; and he called his name
# Enosh; then began men to call upon the name of the LORD."
m.step("Gen.4.26")
# ‹וּלְשֵׁת גַּם־הוּא יֻלַּד־בֵּן› event: born — theme Enosh
m.event("born", themes=["enosh"])
# ‹וַיִּקְרָא אֶת־שְׁמוֹ אֱנוֹשׁ› named: Enosh := Enosh
m.name("enosh", "Enosh")
# ‹אָז הוּחַל לִקְרֹא בְּשֵׁם יְהוָה› fact holds: was-begun-to-call-in-name-
# of-the-LORD
m.fact("huchal_likro_be_shem_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ir'}
    assert m.presupposed_set() == {'eshet_kayin', 'eshet_adam', 'adam', 'kayin'}
    assert m.REGISTRY["names"] == {'ir': 'Chanokh', 'shet': 'Shet', 'enosh': 'Enosh'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == ['shema(neshei_lemekh, qol_lemekh)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4, 'spec_delta': 1, 'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['shte_nashim_le_lemekh', 'shem_ha_achat_adah', 'shem_ha_shenit_tzilah', 'avi_yoshev_ohel_u_mikneh(yaval)', 'shem_achiv_yuval', 'avi_kol_tofes_kinor_ve_ugav(yuval)', 'lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)', 'achot_tuval_kayin_naamah', 'ish_haragti_le_fitzi_ve_yeled_le_chaburati', 'shat_li_elohim_zera_acher_tachat_hevel', 'harago_kayin_named_in_speech', 'huchal_likro_be_shem_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_14_adam_line_ledger
###############################################################################
# =============================================================================
# gen_14_adam_line_ledger — 5:1-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_14_adam_line_ledger.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The book of Adam's line: the death ledger and the man who walked (5:1-32)"""
from machine import Machine

m = Machine("gen_14_adam_line_ledger")

# -------------------------- Gen.5.1 · BOOK_HEADER_LIKENESS_ONLY ------------
# זה ספר תולדת אדם ביום ברא אלהים אדם בדמות אלהים עשׂה אתו
# "This is the book of the generations of Adam. In the day that God created
# man, in the likeness of God made He him;"
m.step("Gen.5.1")
# ‹זה ספר תולדת אדם› section book-generations-Adam: zeh sefer toledot adam —
# the book header labels; installs nothing
m.section("sefer_toledot_adam", "zeh sefer toledot adam — the book header labels; installs nothing")
# ‹ביום ברא אלהים אדם בדמות אלהים עשׂה אתו› fact holds: in-day-of-creating-
# God-Adam-in-likeness-of-God-make-it
m.fact("be_yom_bero_elohim_adam_bidmut_elohim_asah_oto")
# ‹בדמות אלהים עשׂה אתו› spec-delta — spec said in-our-image for-our-
# likeness — in-our-IMAGE after-our-LIKENESS (1:26, frozen day 6), delivery
# says in-likeness-of God make it — LIKENESS ONLY, the image-word dropped
# from the restatement (5:1)
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS (1:26, frozen day 6)",
             "bidmut elohim asah oto — LIKENESS ONLY, the image-word dropped from the restatement (5:1)")
# reads without prior install (flag, not fix): Adam
m.presupposed("adam")

# -------------------------- Gen.5.2 · SPECIES_BLESSED_AND_NAMED ------------
# זכר ונקבה בראם ויברך אתם ויקרא את־שׁמם אדם ביום הבראם
# "male and female created He them, and blessed them, and called their name
# Adam, in the day when they were created."
m.step("Gen.5.2")
# ‹זכר ונקבה בראם ויברך אתם› event: bless — agent God; theme male-and-female
m.event("bless", agent="Elohim", themes=["zakhar_u_nekevah"])
# ‹ויקרא את־שׁמם אדם› named: Adam-species := Adam
m.name("adam_species", "Adam")
# ‹זכר ונקבה בראם› fact holds: male-and-female-when-created; in-day-of-
# their-being-created
m.fact("zakhar_u_nekevah_beraam",
       "be_yom_hibaram")

# -------------------------- Gen.5.3 · SHET_IN_SWAPPED_IMAGE ----------------
# ויחי אדם שׁלשׁים ומאת שׁנה ויולד בדמותו כצלמו ויקרא את־שׁמו שׁת
# "And Adam lived a hundred and thirty years, and begot a son in his own
# likeness, after his image; and called his name Seth."
m.step("Gen.5.3")
# ‹ויחי אדם שׁלשׁים ומאת שׁנה ויולד בדמותו כצלמו› event: beget — agent Adam;
# theme Shet
m.event("beget", agent="adam", themes=["shet"])
# ‹בדמותו כצלמו› spec-delta — spec said in-our-image for-our-likeness — in-
# our-IMAGE after-our-LIKENESS, God to human (1:26, frozen day 6), delivery
# says bi-his-likeness like-his-image — in-his-LIKENESS after-his-IMAGE:
# order swapped, prepositions swapped, direction man-to-son (5:3)
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS, God to human (1:26, frozen day 6)",
             "bi-dmuto ke-tzalmo — in-his-LIKENESS after-his-IMAGE: order swapped, prepositions swapped, direction man-to-son (5:3)")
# ‹ויקרא את־שׁמו שׁת› named: Shet := Shet
m.name("shet", "Shet")

# -------------------------- Gen.5.4 · LEDGER_ADAM_AFTER --------------------
# ויהיו ימי־אדם אחרי הולידו את־שׁת שׁמנה מאת שׁנה ויולד בנים ובנות
# "And the days of Adam after he begot Seth were eight hundred years; and he
# begot sons and daughters."
m.step("Gen.5.4")
# ‹ויהיו ימי־אדם אחרי הולידו את־שׁת שׁמנה מאת שׁנה ויולד בנים ובנות› fact
# holds: sons-and-daughters(Adam)
m.fact("banim_u_vanot(adam)")

# -------------------------- Gen.5.5 · LEDGER_ADAM_TOTAL_DIES ---------------
# ויהיו כל־ימי אדם אשׁר־חי תשׁע מאות שׁנה ושׁלשׁים שׁנה וימת
# "And all the days that Adam lived were nine hundred and thirty years; and
# he died."
m.step("Gen.5.5")
# ‹ויהיו כל־ימי אדם אשׁר־חי תשׁע מאות שׁנה ושׁלשׁים שׁנה› fact holds: all-
# days-of-Adam-930-year
m.fact("kol_yemei_adam_930_shanah")
# ‹וימת› event: die — agent Adam
m.event("die", agent="adam")

# -------------------------- Gen.5.6 · LEDGER_SHET_BEGETS -------------------
# ויחי־שׁת חמשׁ שׁנים ומאת שׁנה ויולד את־אנושׁ
# "And Seth lived a hundred and five years, and begot Enosh."
m.step("Gen.5.6")
# ‹ויחי־שׁת חמשׁ שׁנים ומאת שׁנה ויולד את־אנושׁ› event: beget — agent Shet;
# theme Enos
m.event("beget", agent="shet", themes=["enosh"])

# -------------------------- Gen.5.7 · LEDGER_SHET_AFTER --------------------
# ויחי־שׁת אחרי הולידו את־אנושׁ שׁבע שׁנים ושׁמנה מאות שׁנה ויולד בנים ובנות
# "And Seth lived after he begot Enosh eight hundred and seven years, and
# begot sons and daughters."
m.step("Gen.5.7")
# ‹ויחי־שׁת אחרי הולידו את־אנושׁ שׁבע שׁנים ושׁמנה מאות שׁנה ויולד בנים
# ובנות› fact holds: sons-and-daughters(Shet)
m.fact("banim_u_vanot(shet)")

# -------------------------- Gen.5.8 · LEDGER_SHET_TOTAL_DIES ---------------
# ויהיו כל־ימי־שׁת שׁתים עשׂרה שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Seth were nine hundred and twelve years; and he
# died."
m.step("Gen.5.8")
# ‹ויהיו כל־ימי־שׁת שׁתים עשׂרה שׁנה ותשׁע מאות שׁנה› fact holds: all-days-
# of-Shet-912-year
m.fact("kol_yemei_shet_912_shanah")
# ‹וימת› event: die — agent Shet
m.event("die", agent="shet")

# -------------------------- Gen.5.9 · LEDGER_ENOSH_BEGETS ------------------
# ויחי אנושׁ תשׁעים שׁנה ויולד את־קינן
# "And Enosh lived ninety years, and begot Kenan."
m.step("Gen.5.9")
# ‹ויחי אנושׁ תשׁעים שׁנה ויולד את־קינן› event: beget — agent Enos; theme
# Cainan
m.event("beget", agent="enosh", themes=["qenan"])

# -------------------------- Gen.5.10 · LEDGER_ENOSH_AFTER ------------------
# ויחי אנושׁ אחרי הולידו את־קינן חמשׁ עשׂרה שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Enosh lived after he begot Kenan eight hundred and fifteen years, and
# begot sons and daughters."
m.step("Gen.5.10")
# ‹ויחי אנושׁ אחרי הולידו את־קינן חמשׁ עשׂרה שׁנה ושׁמנה מאות שׁנה ויולד
# בנים ובנות› fact holds: sons-and-daughters(Enos)
m.fact("banim_u_vanot(enosh)")

# -------------------------- Gen.5.11 · LEDGER_ENOSH_TOTAL_DIES -------------
# ויהיו כל־ימי אנושׁ חמשׁ שׁנים ותשׁע מאות שׁנה וימת
# "And all the days of Enosh were nine hundred and five years; and he died."
m.step("Gen.5.11")
# ‹ויהיו כל־ימי אנושׁ חמשׁ שׁנים ותשׁע מאות שׁנה› fact holds: all-days-of-
# Enos-905-year
m.fact("kol_yemei_enosh_905_shanah")
# ‹וימת› event: die — agent Enos
m.event("die", agent="enosh")

# -------------------------- Gen.5.12 · LEDGER_KENAN_BEGETS -----------------
# ויחי קינן שׁבעים שׁנה ויולד את־מהללאל
# "And Kenan lived seventy years, and begot Mahalalel."
m.step("Gen.5.12")
# ‹ויחי קינן שׁבעים שׁנה ויולד את־מהללאל› event: beget — agent Cainan; theme
# Mahalaleel
m.event("beget", agent="qenan", themes=["mahalalel"])

# -------------------------- Gen.5.13 · LEDGER_KENAN_AFTER ------------------
# ויחי קינן אחרי הולידו את־מהללאל ארבעים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Kenan lived after he begot Mahalalel eight hundred and forty years,
# and begot sons and daughters."
m.step("Gen.5.13")
# ‹ויחי קינן אחרי הולידו את־מהללאל ארבעים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות› fact holds: sons-and-daughters(Cainan)
m.fact("banim_u_vanot(qenan)")

# -------------------------- Gen.5.14 · LEDGER_KENAN_TOTAL_DIES -------------
# ויהיו כל־ימי קינן עשׂר שׁנים ותשׁע מאות שׁנה וימת
# "And all the days of Kenan were nine hundred and ten years; and he died."
m.step("Gen.5.14")
# ‹ויהיו כל־ימי קינן עשׂר שׁנים ותשׁע מאות שׁנה› fact holds: all-days-of-
# Cainan-910-year
m.fact("kol_yemei_qenan_910_shanah")
# ‹וימת› event: die — agent Cainan
m.event("die", agent="qenan")

# -------------------------- Gen.5.15 · LEDGER_MAHALALEL_BEGETS -------------
# ויחי מהללאל חמשׁ שׁנים ושׁשׁים שׁנה ויולד את־ירד
# "And Mahalalel lived sixty and five years, and begot Jared."
m.step("Gen.5.15")
# ‹ויחי מהללאל חמשׁ שׁנים ושׁשׁים שׁנה ויולד את־ירד› event: beget — agent
# Mahalaleel; theme Jared
m.event("beget", agent="mahalalel", themes=["yered"])

# -------------------------- Gen.5.16 · LEDGER_MAHALALEL_AFTER --------------
# ויחי מהללאל אחרי הולידו את־ירד שׁלשׁים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות
# "And Mahalalel lived after he begot Jared eight hundred and thirty years,
# and begot sons and daughters."
m.step("Gen.5.16")
# ‹ויחי מהללאל אחרי הולידו את־ירד שׁלשׁים שׁנה ושׁמנה מאות שׁנה ויולד בנים
# ובנות› fact holds: sons-and-daughters(Mahalaleel)
m.fact("banim_u_vanot(mahalalel)")

# -------------------------- Gen.5.17 · LEDGER_MAHALALEL_TOTAL_DIES ---------
# ויהיו כל־ימי מהללאל חמשׁ ותשׁעים שׁנה ושׁמנה מאות שׁנה וימת
# "And all the days of Mahalalel were eight hundred ninety and five years;
# and he died."
m.step("Gen.5.17")
# ‹ויהיו כל־ימי מהללאל חמשׁ ותשׁעים שׁנה ושׁמנה מאות שׁנה› fact holds: all-
# days-of-Mahalaleel-895-year
m.fact("kol_yemei_mahalalel_895_shanah")
# ‹וימת› event: die — agent Mahalaleel
m.event("die", agent="mahalalel")

# -------------------------- Gen.5.18 · LEDGER_YERED_BEGETS -----------------
# ויחי־ירד שׁתים ושׁשׁים שׁנה ומאת שׁנה ויולד את־חנוך
# "And Jared lived a hundred sixty and two years, and begot Enoch."
m.step("Gen.5.18")
# ‹ויחי־ירד שׁתים ושׁשׁים שׁנה ומאת שׁנה ויולד את־חנוך› event: beget — agent
# Jared; theme Enoch
m.event("beget", agent="yered", themes=["chanokh"])

# -------------------------- Gen.5.19 · LEDGER_YERED_AFTER ------------------
# ויחי־ירד אחרי הולידו את־חנוך שׁמנה מאות שׁנה ויולד בנים ובנות
# "And Jared lived after he begot Enoch eight hundred years, and begot sons
# and daughters."
m.step("Gen.5.19")
# ‹ויחי־ירד אחרי הולידו את־חנוך שׁמנה מאות שׁנה ויולד בנים ובנות› fact
# holds: sons-and-daughters(Jared)
m.fact("banim_u_vanot(yered)")

# -------------------------- Gen.5.20 · LEDGER_YERED_TOTAL_DIES -------------
# ויהיו כל־ימי־ירד שׁתים ושׁשׁים שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Jared were nine hundred sixty and two years; and he
# died."
m.step("Gen.5.20")
# ‹ויהיו כל־ימי־ירד שׁתים ושׁשׁים שׁנה ותשׁע מאות שׁנה› fact holds: all-
# days-of-Jared-962-year
m.fact("kol_yemei_yered_962_shanah")
# ‹וימת› event: die — agent Jared
m.event("die", agent="yered")

# -------------------------- Gen.5.21 · LEDGER_CHANOKH_BEGETS ---------------
# ויחי חנוך חמשׁ ושׁשׁים שׁנה ויולד את־מתושׁלח
# "And Enoch lived sixty and five years, and begot Methuselah."
m.step("Gen.5.21")
# ‹ויחי חנוך חמשׁ ושׁשׁים שׁנה ויולד את־מתושׁלח› event: beget — agent Enoch;
# theme Methuselah
m.event("beget", agent="chanokh", themes=["metushelach"])

# -------------------------- Gen.5.22 · WALK_REPLACES_LIVED -----------------
# ויתהלך חנוך את־האלהים אחרי הולידו את־מתושׁלח שׁלשׁ מאות שׁנה ויולד בנים
# ובנות
# "And Enoch walked with God after he begot Methuselah three hundred years,
# and begot sons and daughters."
m.step("Gen.5.22")
# ‹ויתהלך חנוך את־האלהים› fact holds: walked-about-Enoch-obj-marker·et-the-
# God; sons-and-daughters(Enoch)
m.fact("hithalekh_chanokh_et_ha_elohim",
       "banim_u_vanot(chanokh)")

# -------------------------- Gen.5.23 · TOTAL_365_NO_REFRAIN_YET ------------
# ויהי כל־ימי חנוך חמשׁ ושׁשׁים שׁנה ושׁלשׁ מאות שׁנה
# "And all the days of Enoch were three hundred sixty and five years."
m.step("Gen.5.23")
# ‹ויהי כל־ימי חנוך חמשׁ ושׁשׁים שׁנה ושׁלשׁ מאות שׁנה› fact holds: all-
# days-of-Enoch-365-year
m.fact("kol_yemei_chanokh_365_shanah")

# -------------------------- Gen.5.24 · TAKEN_NOT_DEAD ----------------------
# ויתהלך חנוך את־האלהים ואיננו כי־לקח אתו אלהים
# "And Enoch walked with God, and he was not; for God took him."
m.step("Gen.5.24")
# ‹ויתהלך חנוך את־האלהים ואיננו› fact holds: walked-about-Enoch-obj-
# marker·et-the-God; he-is-not-for-take-it-God
m.fact("hithalekh_chanokh_et_ha_elohim",
       "einenu_ki_lakach_oto_elohim")
# ‹כי־לקח אתו אלהים› event: take — agent God; theme Enoch
m.event("take", agent="Elohim", themes=["chanokh"])

# -------------------------- Gen.5.25 · LEDGER_METUSHELACH_BEGETS -----------
# ויחי מתושׁלח שׁבע ושׁמנים שׁנה ומאת שׁנה ויולד את־למך
# "And Methuselah lived a hundred eighty and seven years, and begot Lamech."
m.step("Gen.5.25")
# ‹ויחי מתושׁלח שׁבע ושׁמנים שׁנה ומאת שׁנה ויולד את־למך› event: beget —
# agent Methuselah; theme Lamech
m.event("beget", agent="metushelach", themes=["lemekh"])

# -------------------------- Gen.5.26 · LEDGER_METUSHELACH_AFTER ------------
# ויחי מתושׁלח אחרי הולידו את־למך שׁתים ושׁמונים שׁנה ושׁבע מאות שׁנה ויולד
# בנים ובנות
# "And Methuselah lived after he begot Lamech seven hundred eighty and two
# years, and begot sons and daughters."
m.step("Gen.5.26")
# ‹ויחי מתושׁלח אחרי הולידו את־למך שׁתים ושׁמונים שׁנה ושׁבע מאות שׁנה ויולד
# בנים ובנות› fact holds: sons-and-daughters(Methuselah)
m.fact("banim_u_vanot(metushelach)")

# -------------------------- Gen.5.27 · LEDGER_METUSHELACH_TOTAL_DIES -------
# ויהיו כל־ימי מתושׁלח תשׁע ושׁשׁים שׁנה ותשׁע מאות שׁנה וימת
# "And all the days of Methuselah were nine hundred sixty and nine years;
# and he died."
m.step("Gen.5.27")
# ‹ויהיו כל־ימי מתושׁלח תשׁע ושׁשׁים שׁנה ותשׁע מאות שׁנה› fact holds: all-
# days-of-Methuselah-969-year
m.fact("kol_yemei_metushelach_969_shanah")
# ‹וימת› event: die — agent Methuselah
m.event("die", agent="metushelach")

# -------------------------- Gen.5.28 · SON_BORN_NAMELESS -------------------
# ויחי־למך שׁתים ושׁמנים שׁנה ומאת שׁנה ויולד בן
# "And Lamech lived a hundred eighty and two years, and begot a son."
m.step("Gen.5.28")
# ‹ויחי־למך שׁתים ושׁמנים שׁנה ומאת שׁנה ויולד בן› event: beget — agent
# Lamech; theme son-unnamed
m.event("beget", agent="lemekh", themes=["ben_unnamed"])

# -------------------------- Gen.5.29 · NOACH_NAMED_CURSE_QUOTED ------------
# ויקרא את־שׁמו נח לאמר זה ינחמנו ממעשׂנו ומעצבון ידינו מן־האדמה אשׁר אררה
# יהוה
# "And he called his name Noah, saying: 'This same shall comfort us in our
# work and in the toil of our hands, which cometh from the ground which the
# LORD hath cursed.'"
m.step("Gen.5.29")
# ‹ויקרא את־שׁמו נח› named: Noach := Noach
m.name("noach", "Noach")
# ‹לאמר זה ינחמנו ממעשׂנו ומעצבון ידינו מן־האדמה אשׁר אררה יהוה› fact holds:
# this-will-comfort-us-from-our-work-and-from-toil-of-our-hands; from-the-
# ground-that-cursed-the-LORD
m.fact("zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu",
       "min_ha_adamah_asher_ererah_YHWH")
# ‹מן־האדמה אשׁר אררה יהוה› spec-delta — spec said cursed the-ground for-
# your-sake — the ground cursed, curser unnamed in the sentence text (3:17,
# frozen gen-11), delivery says the-ground that cursed the-LORD — the curse
# attributed to the-LORD by name, plus a comfort forecast no one ratifies
# (5:29)
m.spec_delta("arurah ha-adamah baavurekha — the ground cursed, curser unnamed in the sentence text (3:17, frozen gen_11)",
             "ha-adamah asher ererah YHWH — the curse attributed to YHWH by name, plus a comfort forecast no one ratifies (5:29)")

# -------------------------- Gen.5.30 · LEDGER_LEMEKH_AFTER -----------------
# ויחי־למך אחרי הולידו את־נח חמשׁ ותשׁעים שׁנה וחמשׁ מאת שׁנה ויולד בנים
# ובנות
# "And Lamech lived after he begot Noah five hundred ninety and five years,
# and begot sons and daughters."
m.step("Gen.5.30")
# ‹ויחי־למך אחרי הולידו את־נח חמשׁ ותשׁעים שׁנה וחמשׁ מאת שׁנה ויולד בנים
# ובנות› fact holds: sons-and-daughters(Lamech)
m.fact("banim_u_vanot(lemekh)")

# -------------------------- Gen.5.31 · LEDGER_LEMEKH_TOTAL_777 -------------
# ויהי כל־ימי־למך שׁבע ושׁבעים שׁנה ושׁבע מאות שׁנה וימת
# "And all the days of Lamech were seven hundred seventy and seven years;
# and he died."
m.step("Gen.5.31")
# ‹ויהי כל־ימי־למך שׁבע ושׁבעים שׁנה ושׁבע מאות שׁנה› fact holds: all-days-
# of-Lamech-777-year
m.fact("kol_yemei_lemekh_777_shanah")
# ‹וימת› event: die — agent Lamech
m.event("die", agent="lemekh")

# -------------------------- Gen.5.32 · NOACH_500_THREE_SONS ----------------
# ויהי־נח בן־חמשׁ מאות שׁנה ויולד נח את־שׁם את־חם ואת־יפת
# "And Noah was five hundred years old; and Noah begot Shem, Ham, and
# Japheth."
m.step("Gen.5.32")
# ‹ויהי־נח בן־חמשׁ מאות שׁנה› fact holds: Noach-son-five-hundred-year
m.fact("noach_ben_chamesh_meot_shanah")
# ‹ויולד נח את־שׁם את־חם ואת־יפת› event: beget — agent Noach; theme Shem,
# Cham, Yafet
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {'adam_species': 'Adam', 'shet': 'Shet', 'noach': 'Noach'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'spec_delta': 3, 'read_before_install': 1, 'named_before_any_presence': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['be_yom_bero_elohim_adam_bidmut_elohim_asah_oto', 'zakhar_u_nekevah_beraam', 'be_yom_hibaram', 'banim_u_vanot(adam)', 'kol_yemei_adam_930_shanah', 'banim_u_vanot(shet)', 'kol_yemei_shet_912_shanah', 'banim_u_vanot(enosh)', 'kol_yemei_enosh_905_shanah', 'banim_u_vanot(qenan)', 'kol_yemei_qenan_910_shanah', 'banim_u_vanot(mahalalel)', 'kol_yemei_mahalalel_895_shanah', 'banim_u_vanot(yered)', 'kol_yemei_yered_962_shanah', 'hithalekh_chanokh_et_ha_elohim', 'banim_u_vanot(chanokh)', 'kol_yemei_chanokh_365_shanah', 'hithalekh_chanokh_et_ha_elohim', 'einenu_ki_lakach_oto_elohim', 'banim_u_vanot(metushelach)', 'kol_yemei_metushelach_969_shanah', 'zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu', 'min_ha_adamah_asher_ererah_YHWH', 'banim_u_vanot(lemekh)', 'kol_yemei_lemekh_777_shanah', 'noach_ben_chamesh_meot_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 24
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_15_flood_prologue
###############################################################################
# =============================================================================
# gen_15_flood_prologue — 6:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_15_flood_prologue.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The flood prologue: the stolen verdict, the 120 years, the regret, the favor (6:1-8)"""
from machine import Machine

m = Machine("gen_15_flood_prologue")

# -------------------------- Gen.6.1 · MULTIPLYING_AND_DAUGHTERS ------------
# וַיְהִי כִּי־הֵחֵל הָאָדָם לָרֹב עַל־פְּנֵי הָאֲדָמָה וּבָנוֹת יֻלְּדוּ
# לָהֶם
# "And it came to pass, when men began to multiply on the face of the earth,
# and daughters were born unto them,"
m.step("Gen.6.1")
# ‹כִּי־הֵחֵל הָאָדָם לָרֹב עַל־פְּנֵי הָאֲדָמָה› event: multiply — agent
# the-human
m.event("multiply", agent="ha_adam")
# ‹וּבָנוֹת יֻלְּדוּ לָהֶם› event: born — theme daughters
m.event("born", themes=["banot"])
# reads without prior install (flag, not fix): human
m.presupposed("adam")

# -------------------------- Gen.6.2 · STOLEN_FORMULA_THE_TAKING ------------
# וַיִּרְאוּ בְנֵי־הָאֱלֹהִים אֶת־בְּנוֹת הָאָדָם כִּי טֹבֹת הֵנָּה
# וַיִּקְחוּ לָהֶם נָשִׁים מִכֹּל אֲשֶׁר בָּחָרוּ
# "that the sons of God saw the daughters of men that they were fair; and
# they took them wives, whomsoever they chose."
m.step("Gen.6.2")
# ‹וַיִּרְאוּ בְנֵי־הָאֱלֹהִים אֶת־בְּנוֹת הָאָדָם› event: see — agent sons-
# of-the-God; theme daughters-of-the-human
m.event("see", agent="bnei_ha_elohim", themes=["benot_ha_adam"])
# ‹כִּי טֹבֹת הֵנָּה› test PASS — oracle-word good, on daughters-of-the-
# human
m.test("PASS", "tovot", "benot_ha_adam")
# ‹וַיִּרְאוּ … כִּי טֹבֹת … וַיִּקְחוּ› spec-delta — spec said and-He-saw
# God when-good — the Maker inspects His work and verdicts it good (the
# frozen week units), delivery says and-they-saw sons-of-the-God obj-
# marker·et-daughters-of the-human when good — creature subjects, human
# daughters as object, and a TAKING as the consequence (6:2)
m.spec_delta("va-yar Elohim ki-tov — the Maker inspects His work and verdicts it good (the frozen week units)",
             "va-yiru bnei-ha-elohim et-bnot ha-adam ki tovot — creature subjects, human daughters as object, and a TAKING as the consequence (6:2)")
# ‹וַיִּקְחוּ לָהֶם נָשִׁים מִכֹּל אֲשֶׁר בָּחָרוּ› event: take — agent
# sons-of-the-God; theme wives-from-all-that-they-chose
m.event("take", agent="bnei_ha_elohim", themes=["nashim_mi_kol_asher_bacharu"])

# -------------------------- Gen.6.3 · DECREE_120_YEARS ---------------------
# וַיֹּאמֶר יְהוָה לֹא־יָדוֹן רוּחִי בָאָדָם לְעֹלָם בְּשַׁגַּם הוּא בָשָׂר
# וְהָיוּ יָמָיו מֵאָה וְעֶשְׂרִים שָׁנָה
# "And the LORD said: 'My spirit shall not abide in man for ever, for that
# he also is flesh; therefore shall his days be a hundred and twenty
# years.'"
m.step("Gen.6.3")
# ‹וַיֹּאמֶר יְהוָה› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹לֹא־יָדוֹן רוּחִי בָאָדָם לְעֹלָם … וְהָיוּ יָמָיו מֵאָה וְעֶשְׂרִים
# שָׁנָה› fact holds: not-shall-abide-judge-My-spirit-and-human-to-forever;
# and-shall-be-his-days-hundred-and-twenty-year
m.fact("lo_yadon_ruchi_va_adam_le_olam",
       "ve_hayu_yamav_meah_ve_esrim_shanah")

# -------------------------- Gen.6.4 · NEPHILIM_PARENTHESIS -----------------
# הַנְּפִלִים הָיוּ בָאָרֶץ בַּיָּמִים הָהֵם וְגַם אַחֲרֵי־כֵן אֲשֶׁר
# יָבֹאוּ בְּנֵי הָאֱלֹהִים אֶל־בְּנוֹת הָאָדָם וְיָלְדוּ לָהֶם הֵמָּה
# הַגִּבֹּרִים אֲשֶׁר מֵעוֹלָם אַנְשֵׁי הַשֵּׁם
# "The Nephilim were in the earth in those days, and also after that, when
# the sons of God came in unto the daughters of men, and they bore children
# to them; the same were the mighty men that were of old, the men of
# renown."
m.step("Gen.6.4")
# ‹הַנְּפִלִים הָיוּ בָאָרֶץ … הֵמָּה הַגִּבֹּרִים אֲשֶׁר מֵעוֹלָם אַנְשֵׁי
# הַשֵּׁם› fact holds: the-Nephilim-shall-be-and-earth; men-of-the-name-
# from-forever
m.fact("ha_nefilim_hayu_va_aretz",
       "anshei_ha_shem_me_olam")

# -------------------------- Gen.6.5 · INVERTED_INSPECTION_TOTAL_DIAGNOSIS --
# וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם בָּאָרֶץ וְכָל־יֵצֶר מַחְשְׁבֹת
# לִבּוֹ רַק רַע כָּל־הַיּוֹם
# "And the LORD saw that the wickedness of man was great in the earth, and
# that every imagination of the thoughts of his heart was only evil
# continually."
m.step("Gen.6.5")
# ‹וַיַּרְא יְהוָה כִּי רַבָּה רָעַת הָאָדָם› event: see — agent the-LORD;
# theme evil-of-the-human
m.event("see", agent="YHWH", themes=["raat_ha_adam"])
# ‹וַיַּרְא … כִּי רַבָּה רָעַת› spec-delta — spec said and-He-saw God obj-
# marker·et-all-that make and-behold good very — He saw all He had made:
# very good (1:31, frozen day 6), delivery says and-He-saw the-LORD when
# great evil-of the-human — He saw: GREAT was the EVIL bird-of man (6:5)
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — He saw all He had made: very good (1:31, frozen day 6)",
             "va-yar YHWH ki rabbah raat ha-adam — He saw: GREAT was the EVIL of man (6:5)")
# ‹וְכָל־יֵצֶר מַחְשְׁבֹת לִבּוֹ רַק רַע כָּל־הַיּוֹם› fact holds: all-
# devising-of-thoughts-His-heart-only-evil-all-the-day
m.fact("kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom")

# -------------------------- Gen.6.6 · REGRET_AND_GRIEF ---------------------
# וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם בָּאָרֶץ וַיִּתְעַצֵּב
# אֶל־לִבּוֹ
# "And it repented the LORD that He had made man on the earth, and it
# grieved Him at His heart."
m.step("Gen.6.6")
# ‹וַיִּנָּחֶם יְהוָה כִּי־עָשָׂה אֶת־הָאָדָם› event: regret — agent the-
# LORD
m.event("regret", agent="YHWH")
# ‹וַיִּתְעַצֵּב אֶל־לִבּוֹ› event: grieve — agent the-LORD; theme His-heart
m.event("grieve", agent="YHWH", themes=["libo"])

# -------------------------- Gen.6.7 · WIPE_RESOLVE_PUSHED ------------------
# וַיֹּאמֶר יְהוָה אֶמְחֶה אֶת־הָאָדָם אֲשֶׁר־בָּרָאתִי מֵעַל פְּנֵי
# הָאֲדָמָה מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמָיִם כִּי
# נִחַמְתִּי כִּי עֲשִׂיתִם
# "And the LORD said: 'I will blot out man whom I have created from the face
# of the earth; both man, and beast, and creeping thing, and fowl of the
# air; for it repenteth Me that I have made them.'"
m.step("Gen.6.7")
# ‹וַיֹּאמֶר יְהוָה› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹אֶמְחֶה אֶת־הָאָדָם אֲשֶׁר־בָּרָאתִי מֵעַל פְּנֵי הָאֲדָמָה› the-LORD
# speaks a demand — CMD-US?: wipe(the-human, from-upon-face-of-the-ground)
m.declare("YHWH", "CMD-US?",
          "machah(ha_adam, me_al_pnei_ha_adamah)")
# ‹מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמָיִם› fact holds: from-
# human-to-livestock-to-creeper-and-to-bird-of-the-heavens
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim")

# -------------------------- Gen.6.8 · FIVE_WORDS_FAVOR ---------------------
# וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה
# "But Noah found grace in the eyes of the LORD."
m.step("Gen.6.8")
# ‹וְנֹחַ מָצָא חֵן בְּעֵינֵי יְהוָה› fact holds: Noach-found-favor-in-eyes-
# of-the-LORD
m.fact("noach_matza_chen_be_einei_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tovot', 'benot_ha_adam')]
    assert m.open_demands() == ['machah(ha_adam, me_al_pnei_ha_adamah)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_yadon_ruchi_va_adam_le_olam', 've_hayu_yamav_meah_ve_esrim_shanah', 'ha_nefilim_hayu_va_aretz', 'anshei_ha_shem_me_olam', 'kol_yetzer_machshevot_libo_raq_ra_kol_ha_yom', 'me_adam_ad_behemah_ad_remes_ve_ad_of_ha_shamayim', 'noach_matza_chen_be_einei_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_16_ark_spec
###############################################################################
# =============================================================================
# gen_16_ark_spec — 6:9-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_16_ark_spec.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The ark spec: the blueprint, the covenant word, the first obeyed command (6:9-22)"""
from machine import Machine

m = Machine("gen_16_ark_spec")

# -------------------------- Gen.6.9 · TOLEDOT_NOACH_THE_WALKER -------------
# אֵלֶּה תּוֹלְדֹת נֹחַ נֹחַ אִישׁ צַדִּיק תָּמִים הָיָה בְּדֹרֹתָיו
# אֶת־הָאֱלֹהִים הִתְהַלֶּךְ־נֹחַ
# "These are the generations of Noah. Noah was in his generations a man
# righteous and whole-hearted; Noah walked with God."
m.step("Gen.6.9")
# ‹אֵלֶּה תּוֹלְדֹת נֹחַ› section generations-Noach: eleh toledot noach —
# the third generations header
m.section("toledot_noach", "eleh toledot noach — the third generations header")
# ‹אִישׁ צַדִּיק תָּמִים הָיָה בְּדֹרֹתָיו אֶת־הָאֱלֹהִים הִתְהַלֶּךְ־נֹחַ›
# fact holds: man-righteous-whole-in-his-generations; with-the-God-walked-
# Noach
m.fact("ish_tzaddik_tamim_be_dorotav",
       "et_ha_elohim_hithalekh_noach")
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")

# -------------------------- Gen.6.10 · THREE_SONS_RESTATED -----------------
# וַיּוֹלֶד נֹחַ שְׁלֹשָׁה בָנִים אֶת־שֵׁם אֶת־חָם וְאֶת־יָפֶת
# "And Noah begot three sons, Shem, Ham, and Japheth."
m.step("Gen.6.10")
# ‹וַיּוֹלֶד נֹחַ שְׁלֹשָׁה בָנִים אֶת־שֵׁם אֶת־חָם וְאֶת־יָפֶת› event:
# beget — agent Noach; theme Shem, Cham, Yafet
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- Gen.6.11 · EARTH_CORRUPTED_FILLED --------------
# וַתִּשָּׁחֵת הָאָרֶץ לִפְנֵי הָאֱלֹהִים וַתִּמָּלֵא הָאָרֶץ חָמָס
# "And the earth was corrupt before God, and the earth was filled with
# violence."
m.step("Gen.6.11")
# ‹וַתִּשָּׁחֵת הָאָרֶץ לִפְנֵי הָאֱלֹהִים› event: corrupt — theme the-earth
m.event("corrupt", themes=["ha_aretz"])
# ‹וַתִּמָּלֵא הָאָרֶץ חָמָס› fact holds: and-was-filled-the-earth-violence
m.fact("va_timale_ha_aretz_chamas")

# -------------------------- Gen.6.12 · THIRD_SEEING_BEHOLD_CORRUPTED -------
# וַיַּרְא אֱלֹהִים אֶת־הָאָרֶץ וְהִנֵּה נִשְׁחָתָה כִּי־הִשְׁחִית
# כָּל־בָּשָׂר אֶת־דַּרְכּוֹ עַל־הָאָרֶץ
# "And God saw the earth, and, behold, it was corrupt; for all flesh had
# corrupted their way upon the earth."
m.step("Gen.6.12")
# ‹וַיַּרְא אֱלֹהִים אֶת־הָאָרֶץ› event: see — agent God; theme the-earth
m.event("see", agent="Elohim", themes=["ha_aretz"])
# ‹וְהִנֵּה נִשְׁחָתָה› spec-delta — spec said and-He-saw God with-all-which
# make and-behold good very — and behold, very good (1:31, frozen day 6),
# delivery says and-He-saw God with-the-earth and-behold was-corrupted — and
# behold, CORRUPTED (6:12)
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — and behold, very good (1:31, frozen day 6)",
             "va-yar Elohim et-ha-aretz ve-hinneh nishchatah — and behold, CORRUPTED (6:12)")
# ‹כִּי־הִשְׁחִית כָּל־בָּשָׂר אֶת־דַּרְכּוֹ› fact holds: had-corrupted-all-
# flesh-with-its-way
m.fact("hishchit_kol_basar_et_darko")

# -------------------------- Gen.6.13 · END_DECREE_SPOKEN_TO_NOACH ----------
# וַיֹּאמֶר אֱלֹהִים לְנֹחַ קֵץ כָּל־בָּשָׂר בָּא לְפָנַי כִּי־מָלְאָה
# הָאָרֶץ חָמָס מִפְּנֵיהֶם וְהִנְנִי מַשְׁחִיתָם אֶת־הָאָרֶץ
# "And God said unto Noah: 'The end of all flesh is come before Me; for the
# earth is filled with violence through them; and, behold, I will destroy
# them with the earth.'"
m.step("Gen.6.13")
# ‹וַיֹּאמֶר אֱלֹהִים לְנֹחַ› event: say — agent God; theme Noach
m.event("say", agent="Elohim", themes=["noach"])
# ‹קֵץ כָּל־בָּשָׂר בָּא לְפָנַי … וְהִנְנִי מַשְׁחִיתָם אֶת־הָאָרֶץ› fact
# holds: end-of-all-flesh-has-come-before-Me; behold-I-destroying-them-with-
# the-earth
m.fact("qetz_kol_basar_ba_lefanai",
       "hineni_mashchitam_et_ha_aretz")

# -------------------------- Gen.6.14 · COMMISSION_MAKE_THE_ARK -------------
# עֲשֵׂה לְךָ תֵּבַת עֲצֵי־גֹפֶר קִנִּים תַּעֲשֶׂה אֶת־הַתֵּבָה וְכָפַרְתָּ
# אֹתָהּ מִבַּיִת וּמִחוּץ בַּכֹּפֶר
# "Make thee an ark of gopher wood; with rooms shalt thou make the ark, and
# shalt pitch it within and without with pitch."
m.step("Gen.6.14")
# ‹עֲשֵׂה לְךָ תֵּבַת עֲצֵי־גֹפֶר› God speaks a demand — LET: make(Noach,
# ark)
m.declare("Elohim", "LET",
          "aseh(noach, tevah)")
# ‹קִנִּים תַּעֲשֶׂה אֶת־הַתֵּבָה וְכָפַרְתָּ אֹתָהּ … בַּכֹּפֶר› fact
# holds: ark-of-wood-of-gofer-rooms; and-you-shall-pitch-has-come-pitch
m.fact("tevat_atzei_gofer_qinim",
       "ve_khafarta_ba_kofer")

# -------------------------- Gen.6.15 · BLUEPRINT_DIMENSIONS ----------------
# וְזֶה אֲשֶׁר תַּעֲשֶׂה אֹתָהּ שְׁלֹשׁ מֵאוֹת אַמָּה אֹרֶךְ הַתֵּבָה
# חֲמִשִּׁים אַמָּה רָחְבָּהּ וּשְׁלֹשִׁים אַמָּה קוֹמָתָהּ
# "And this is how thou shalt make it: the length of the ark three hundred
# cubits, the breadth of it fifty cubits, and the height of it thirty
# cubits."
m.step("Gen.6.15")
# ‹שְׁלֹשׁ מֵאוֹת אַמָּה אֹרֶךְ … חֲמִשִּׁים אַמָּה רָחְבָּהּ וּשְׁלֹשִׁים
# אַמָּה קוֹמָתָהּ› fact holds: three-hundred-cubit-length-of; fifty-cubit-
# its-width; thirty-cubit-its-height
m.fact("shelosh_meot_amah_orekh",
       "chamishim_amah_rochbah",
       "sheloshim_amah_qomatah")

# -------------------------- Gen.6.16 · BLUEPRINT_LIGHT_DOOR_DECKS ----------
# צֹהַר תַּעֲשֶׂה לַתֵּבָה וְאֶל־אַמָּה תְּכַלֶנָּה מִלְמַעְלָה וּפֶתַח
# הַתֵּבָה בְּצִדָּהּ תָּשִׂים תַּחְתִּיִּם שְׁנִיִּם וּשְׁלִשִׁים
# תַּעֲשֶׂהָ
# "A light shalt thou make to the ark, and to a cubit shalt thou finish it
# upward; and the door of the ark shalt thou set in the side thereof; with
# lower, second, and third stories shalt thou make it."
m.step("Gen.6.16")
# ‹צֹהַר … וּפֶתַח הַתֵּבָה בְּצִדָּהּ … תַּחְתִּיִּם שְׁנִיִּם
# וּשְׁלִשִׁים› fact holds: a-light-to-ark; door-opening-has-come-its-side;
# lower-second-decks-and-third-decks
m.fact("tzohar_la_tevah",
       "petach_ba_tzidah",
       "tachtiyim_shniyim_u_shlishim")

# -------------------------- Gen.6.17 · FLOOD_ANNOUNCED ---------------------
# וַאֲנִי הִנְנִי מֵבִיא אֶת־הַמַּבּוּל מַיִם עַל־הָאָרֶץ לְשַׁחֵת
# כָּל־בָּשָׂר אֲשֶׁר־בּוֹ רוּחַ חַיִּים מִתַּחַת הַשָּׁמָיִם כֹּל
# אֲשֶׁר־בָּאָרֶץ יִגְוָע
# "And I, behold, I do bring the flood of waters upon the earth, to destroy
# all flesh, wherein is the breath of life, from under heaven; every thing
# that is in the earth shall perish."
m.step("Gen.6.17")
# ‹וַאֲנִי הִנְנִי מֵבִיא אֶת־הַמַּבּוּל … כֹּל אֲשֶׁר־בָּאָרֶץ יִגְוָע›
# fact holds: behold-I-bringing-with-the-flood-waters; all-which-has-come-
# earth-shall-expire
m.fact("hineni_mevi_et_ha_mabul_mayim",
       "kol_asher_ba_aretz_yigva")

# -------------------------- Gen.6.18 · COVENANT_PROMISED_BOARDING_LIST -----
# וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתָּךְ וּבָאתָ אֶל־הַתֵּבָה אַתָּה וּבָנֶיךָ
# וְאִשְׁתְּךָ וּנְשֵׁי־בָנֶיךָ אִתָּךְ
# "But I will establish My covenant with thee; and thou shalt come into the
# ark, thou, and thy sons, and thy wife, and thy sons' wives with thee."
m.step("Gen.6.18")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתָּךְ וּבָאתָ אֶל־הַתֵּבָה› fact holds: and-
# I-will-establish-with-My-covenant-with-you; and-you-shall-come-to-the-ark-
# you-and-your-sons
m.fact("va_hakimoti_et_briti_itakh",
       "u_vata_el_ha_tevah_atah_u_vanekha")

# -------------------------- Gen.6.19 · MANIFEST_TWO_OF_ALL -----------------
# וּמִכָּל־הָחַי מִכָּל־בָּשָׂר שְׁנַיִם מִכֹּל תָּבִיא אֶל־הַתֵּבָה
# לְהַחֲיֹת אִתָּךְ זָכָר וּנְקֵבָה יִהְיוּ
# "And of every living thing of all flesh, two of every sort shalt thou
# bring into the ark, to keep them alive with thee; they shall be male and
# female."
m.step("Gen.6.19")
# ‹שְׁנַיִם מִכֹּל תָּבִיא … זָכָר וּנְקֵבָה יִהְיוּ› fact holds: two-from-
# all-you-shall-bring-to-the-ark; male-and-female-they-shall-be
m.fact("shnayim_mi_kol_tavi_el_ha_tevah",
       "zakhar_u_nekevah_yihyu")

# -------------------------- Gen.6.20 · MANIFEST_BY_KINDS_SELF_LOADING ------
# מֵהָעוֹף לְמִינֵהוּ וּמִן־הַבְּהֵמָה לְמִינָהּ מִכֹּל רֶמֶשׂ הָאֲדָמָה
# לְמִינֵהוּ שְׁנַיִם מִכֹּל יָבֹאוּ אֵלֶיךָ לְהַחֲיוֹת
# "Of the fowl after their kind, and of the cattle after their kind, of
# every creeping thing of the ground after its kind, two of every sort shall
# come unto thee, to keep them alive."
m.step("Gen.6.20")
# ‹מֵהָעוֹף לְמִינֵהוּ … שְׁנַיִם מִכֹּל יָבֹאוּ אֵלֶיךָ› fact holds: to-
# its-kind-manifest-bird-livestock-creeper-of
m.fact("le_minehu_manifest_of_behemah_remes")

# -------------------------- Gen.6.21 · SECOND_IMPERATIVE_PROVISIONS --------
# וְאַתָּה קַח־לְךָ מִכָּל־מַאֲכָל אֲשֶׁר יֵאָכֵל וְאָסַפְתָּ אֵלֶיךָ
# וְהָיָה לְךָ וְלָהֶם לְאָכְלָה
# "And take thou unto thee of all food that is eaten, and gather it to thee;
# and it shall be for food for thee, and for them.'"
m.step("Gen.6.21")
# ‹וְאַתָּה קַח־לְךָ מִכָּל־מַאֲכָל אֲשֶׁר יֵאָכֵל› God speaks a demand —
# LET: take(Noach, from-all-food)
m.declare("Elohim", "LET",
          "qach(noach, mi_kol_maakhal)")
# ‹וְהָיָה לְךָ וְלָהֶם לְאָכְלָה› fact holds: and-was-to-you-and-to-them-
# to-food
m.fact("ve_hayah_lekha_ve_lahem_le_akhlah")

# -------------------------- Gen.6.22 · THE_RECEIPT_BOTH_POPPED -------------
# וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים כֵּן עָשָׂה
# "Thus did Noah; according to all that God commanded him, so did he."
m.step("Gen.6.22")
# ‹וַיַּעַשׂ נֹחַ› event: make — agent Noach; theme ark
m.event("make", agent="noach", themes=["tevah"])
# ‹וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר צִוָּה› the world gains: ark
m.install("tevah")
# ‹כְּכֹל אֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› demand settled (popped from the
# queue): make(Noach, ark)
m.result("aseh(noach, tevah)", tmark="t2")
# ‹כֵּן עָשָׂה› demand settled (popped from the queue): take(Noach, from-
# all-food)
m.result("qach(noach, mi_kol_maakhal)", tmark="t2")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'tevah'}
    assert m.presupposed_set() == {'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['ish_tzaddik_tamim_be_dorotav', 'et_ha_elohim_hithalekh_noach', 'va_timale_ha_aretz_chamas', 'hishchit_kol_basar_et_darko', 'qetz_kol_basar_ba_lefanai', 'hineni_mashchitam_et_ha_aretz', 'tevat_atzei_gofer_qinim', 've_khafarta_ba_kofer', 'shelosh_meot_amah_orekh', 'chamishim_amah_rochbah', 'sheloshim_amah_qomatah', 'tzohar_la_tevah', 'petach_ba_tzidah', 'tachtiyim_shniyim_u_shlishim', 'hineni_mevi_et_ha_mabul_mayim', 'kol_asher_ba_aretz_yigva', 'va_hakimoti_et_briti_itakh', 'u_vata_el_ha_tevah_atah_u_vanekha', 'shnayim_mi_kol_tavi_el_ha_tevah', 'zakhar_u_nekevah_yihyu', 'le_minehu_manifest_of_behemah_remes', 've_hayah_lekha_ve_lahem_le_akhlah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_17_boarding
###############################################################################
# =============================================================================
# gen_17_boarding — 7:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_17_boarding.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The boarding: you have I seen righteous, the date, the shut door (7:1-16)"""
from machine import Machine

m = Machine("gen_17_boarding")

# -------------------------- Gen.7.1 · COME_COMMAND_SECOND_PERSON_VERDICT ---
# וַיֹּאמֶר יְהוָה לְנֹחַ בֹּא־אַתָּה וְכָל־בֵּיתְךָ אֶל־הַתֵּבָה
# כִּי־אֹתְךָ רָאִיתִי צַדִּיק לְפָנַי בַּדּוֹר הַזֶּה
# "And the LORD said unto Noah: 'Come thou and all thy house into the ark;
# for thee have I seen righteous before Me in this generation.'"
m.step("Gen.7.1")
# ‹בֹּא־אַתָּה וְכָל־בֵּיתְךָ אֶל־הַתֵּבָה› the-LORD speaks a demand — LET:
# come(Noach, to-the-ark)
m.declare("YHWH", "LET",
          "bo(noach, el_ha_tevah)")
# ‹כִּי־אֹתְךָ רָאִיתִי צַדִּיק לְפָנַי› test PASS — oracle-word righteous,
# on Noach
m.test("PASS", "tzaddik", "noach")
# reads without prior install (flag, not fix): Noach, ark
m.presupposed("noach", "tevah")

# -------------------------- Gen.7.2 · CLEAN_SEVENS_AMENDMENT ---------------
# מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה תִּקַּח־לְךָ שִׁבְעָה שִׁבְעָה אִישׁ
# וְאִשְׁתּוֹ וּמִן־הַבְּהֵמָה אֲשֶׁר לֹא טְהֹרָה הִוא שְׁנַיִם אִישׁ
# וְאִשְׁתּוֹ
# "Of every clean beast thou shalt take to thee seven and seven, each with
# his mate; and of the beasts that are not clean two and two, each with his
# mate;"
m.step("Gen.7.2")
# ‹הַטְּהוֹרָה … שִׁבְעָה שִׁבְעָה … לֹא טְהֹרָה הִוא שְׁנַיִם› fact holds:
# seven-seven-the-livestock-the-clean; two-which-not-clean
m.fact("shivah_shivah_ha_behemah_ha_tehorah",
       "shnayim_asher_lo_tehorah")

# -------------------------- Gen.7.3 · BIRDS_AND_THE_SEED_PURPOSE -----------
# גַּם מֵעוֹף הַשָּׁמַיִם שִׁבְעָה שִׁבְעָה זָכָר וּנְקֵבָה לְחַיּוֹת זֶרַע
# עַל־פְּנֵי כָל־הָאָרֶץ
# "of the fowl also of the air, seven and seven, male and female; to keep
# seed alive upon the face of all the earth."
m.step("Gen.7.3")
# ‹לְחַיּוֹת זֶרַע עַל־פְּנֵי כָל־הָאָרֶץ› fact holds: to-keep-alive-seed-
# over-face-of-all-the-earth
m.fact("le_chayot_zera_al_pnei_khol_ha_aretz")

# -------------------------- Gen.7.4 · COUNTDOWN_STACK_WIPE_SCHEDULED -------
# כִּי לְיָמִים עוֹד שִׁבְעָה אָנֹכִי מַמְטִיר עַל־הָאָרֶץ אַרְבָּעִים יוֹם
# וְאַרְבָּעִים לָיְלָה וּמָחִיתִי אֶת־כָּל־הַיְקוּם אֲשֶׁר עָשִׂיתִי מֵעַל
# פְּנֵי הָאֲדָמָה
# "For yet seven days, and I will cause it to rain upon the earth forty days
# and forty nights; and every living substance that I have made will I blot
# out from off the face of the earth.'"
m.step("Gen.7.4")
# ‹עוֹד שִׁבְעָה אָנֹכִי מַמְטִיר … וּמָחִיתִי אֶת־כָּל־הַיְקוּם› fact
# holds: still-seven-day-I-raining; and-I-will-wipe-obj-marker·et-all-the-
# standing-substance
m.fact("od_shivat_yamim_anokhi_mamtir",
       "u_machiti_et_kol_ha_yequm")

# -------------------------- Gen.7.5 · REFRAIN_TWO --------------------------
# וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר־צִוָּהוּ יְהוָה
# "And Noah did according unto all that the LORD commanded him."
m.step("Gen.7.5")
# ‹וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר־צִוָּהוּ יְהוָה› fact holds: like-all-which-
# commanded-him-the-LORD
m.fact("ke_khol_asher_tzivahu_YHWH")

# -------------------------- Gen.7.6 · AGE_AT_THE_FLOOD ---------------------
# וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת שָׁנָה וְהַמַּבּוּל הָיָה מַיִם עַל־הָאָרֶץ
# "And Noah was six hundred years old when the flood of waters was upon the
# earth."
m.step("Gen.7.6")
# ‹וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת שָׁנָה› fact holds: Noach-son-six-hundred-year
m.fact("noach_ben_shesh_meot_shanah")

# -------------------------- Gen.7.7 · THE_ENTRY_DEMAND_POPPED --------------
# וַיָּבֹא נֹחַ וּבָנָיו וְאִשְׁתּוֹ וּנְשֵׁי־בָנָיו אִתּוֹ אֶל־הַתֵּבָה
# מִפְּנֵי מֵי הַמַּבּוּל
# "And Noah went in, and his sons, and his wife, and his sons' wives with
# him, into the ark, because of the waters of the flood."
m.step("Gen.7.7")
# ‹וַיָּבֹא נֹחַ … אֶל־הַתֵּבָה› event: come — agent Noach; theme to-the-ark
m.event("come", agent="noach", themes=["el_ha_tevah"])
# ‹וַיָּבֹא … אֶל־הַתֵּבָה› demand settled (popped from the queue):
# come(Noach, to-the-ark)
m.result("bo(noach, el_ha_tevah)", tmark="t1")

# -------------------------- Gen.7.8 · THE_CARGO_CLASSES --------------------
# מִן־הַבְּהֵמָה הַטְּהוֹרָה וּמִן־הַבְּהֵמָה אֲשֶׁר אֵינֶנָּה טְהֹרָה
# וּמִן־הָעוֹף וְכֹל אֲשֶׁר־רֹמֵשׂ עַל־הָאֲדָמָה
# "Of clean beasts, and of beasts that are not clean, and of fowls, and of
# every thing that creepeth upon the ground,"
m.step("Gen.7.8")
# ‹הַטְּהוֹרָה … אֵינֶנָּה טְהֹרָה … הָעוֹף … רֹמֵשׂ› fact holds: the-clean-
# and-is-not-clean-and-the-flying-creature-and-the-creep
m.fact("ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes")

# -------------------------- Gen.7.9 · SELF_LOADING_REFRAIN_THREE -----------
# שְׁנַיִם שְׁנַיִם בָּאוּ אֶל־נֹחַ אֶל־הַתֵּבָה זָכָר וּנְקֵבָה כַּאֲשֶׁר
# צִוָּה אֱלֹהִים אֶת־נֹחַ
# "there went in two and two unto Noah into the ark, male and female, as God
# commanded Noah."
m.step("Gen.7.9")
# ‹שְׁנַיִם שְׁנַיִם בָּאוּ … כַּאֲשֶׁר צִוָּה אֱלֹהִים› fact holds: two-
# two-they-came-to-Noach; like-which-commanded-God-obj-marker·et-Noach
m.fact("shnayim_shnayim_bau_el_noach",
       "ka_asher_tzivah_elohim_et_noach")

# -------------------------- Gen.7.10 · SEVEN_DAYS_ELAPSE -------------------
# וַיְהִי לְשִׁבְעַת הַיָּמִים וּמֵי הַמַּבּוּל הָיוּ עַל־הָאָרֶץ
# "And it came to pass after the seven days, that the waters of the flood
# were upon the earth."
m.step("Gen.7.10")
# ‹וַיְהִי לְשִׁבְעַת הַיָּמִים וּמֵי הַמַּבּוּל הָיוּ› fact holds: to-
# seven-the-day-waters-of-the-deluge
m.fact("le_shivat_ha_yamim_mei_ha_mabul")

# -------------------------- Gen.7.11 · THE_DATE_DOUBLE_BREACH --------------
# בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי
# בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ בַּיּוֹם הַזֶּה נִבְקְעוּ כָּל־מַעְיְנֹת
# תְּהוֹם רַבָּה וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ
# "In the six hundredth year of Noah's life, in the second month, on the
# seventeenth day of the month, on the same day were all the fountains of
# the great deep broken up, and the windows of heaven were opened."
m.step("Gen.7.11")
# ‹בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי
# בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ› clock anchored: t0 := year-of-600-of-
# month-2-day-17
m.time_anchor("shnat_600_chodesh_2_yom_17")
# ‹נִבְקְעוּ כָּל־מַעְיְנֹת תְּהוֹם רַבָּה› event: split — theme fountains-
# of-deep-great
m.event("split", themes=["mayenot_tehom_rabbah"])
# ‹וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ› event: open — theme windows-of-the-
# heavens
m.event("open", themes=["arubot_ha_shamayim"])

# -------------------------- Gen.7.12 · THE_RAIN_FORTY ----------------------
# וַיְהִי הַגֶּשֶׁם עַל־הָאָרֶץ אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה
# "And the rain was upon the earth forty days and forty nights."
m.step("Gen.7.12")
# ‹הַגֶּשֶׁם … אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה› fact holds: the-rain-
# forty-day-and-forty-night
m.fact("ha_geshem_arbaim_yom_va_arbaim_laylah")

# -------------------------- Gen.7.13 · THE_SOLEMN_DAY_STAMP ----------------
# בְּעֶצֶם הַיּוֹם הַזֶּה בָּא נֹחַ וְשֵׁם־וְחָם וָיֶפֶת בְּנֵי־נֹחַ
# וְאֵשֶׁת נֹחַ וּשְׁלֹשֶׁת נְשֵׁי־בָנָיו אִתָּם אֶל־הַתֵּבָה
# "In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the
# sons of Noah, and Noah's wife, and the three wives of his sons with them,
# into the ark;"
m.step("Gen.7.13")
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה בָּא נֹחַ› fact holds: in-very-the-day-the-this-
# came-Noach
m.fact("be_etzem_ha_yom_ha_zeh_ba_noach")

# -------------------------- Gen.7.14 · FULL_TAXONOMY_EVERY_WING ------------
# הֵמָּה וְכָל־הַחַיָּה לְמִינָהּ וְכָל־הַבְּהֵמָה לְמִינָהּ וְכָל־הָרֶמֶשׂ
# הָרֹמֵשׂ עַל־הָאָרֶץ לְמִינֵהוּ וְכָל־הָעוֹף לְמִינֵהוּ כֹּל צִפּוֹר
# כָּל־כָּנָף
# "they, and every beast after its kind, and all the cattle after their
# kind, and every creeping thing that creepeth upon the earth after its
# kind, and every fowl after its kind, every bird of every sort."
m.step("Gen.7.14")
# ‹לְמִינָהּ … לְמִינֵהוּ … כֹּל צִפּוֹר כָּל־כָּנָף› fact holds: all-the-
# beast-to-its-kind-the-flying-creature-to-its-kind; all-bird-all-wing
m.fact("kol_ha_chayah_le_minah_ha_of_le_minehu",
       "kol_tzippor_kol_kanaf")

# -------------------------- Gen.7.15 · THE_PAIRS_AND_THE_BREATH ------------
# וַיָּבֹאוּ אֶל־נֹחַ אֶל־הַתֵּבָה שְׁנַיִם שְׁנַיִם מִכָּל־הַבָּשָׂר
# אֲשֶׁר־בּוֹ רוּחַ חַיִּים
# "And they went in unto Noah into the ark, two and two of all flesh wherein
# is the breath of life."
m.step("Gen.7.15")
# ‹וַיָּבֹאוּ אֶל־נֹחַ … שְׁנַיִם שְׁנַיִם› event: come — theme all-flesh-
# two-two
m.event("come", themes=["kol_basar_shnayim_shnayim"])

# -------------------------- Gen.7.16 · THE_SEAL_YHWH_SHUTS -----------------
# וְהַבָּאִים זָכָר וּנְקֵבָה מִכָּל־בָּשָׂר בָּאוּ כַּאֲשֶׁר צִוָּה אֹתוֹ
# אֱלֹהִים וַיִּסְגֹּר יְהוָה בַּעֲדוֹ
# "And they that went in, went in male and female of all flesh, as God
# commanded him; and the LORD shut him in."
m.step("Gen.7.16")
# ‹וְהַבָּאִים זָכָר וּנְקֵבָה … בָּאוּ כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים›
# fact holds: the-comers-male-and-female-they-came; like-which-commanded-it-
# God
m.fact("ha_baim_zakhar_u_nekevah_bau",
       "ka_asher_tzivah_oto_elohim")
# ‹וַיִּסְגֹּר יְהוָה בַּעֲדוֹ› event: shut — agent the-LORD; theme about-
# him
m.event("shut", agent="YHWH", themes=["baado"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tzaddik', 'noach')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['shivah_shivah_ha_behemah_ha_tehorah', 'shnayim_asher_lo_tehorah', 'le_chayot_zera_al_pnei_khol_ha_aretz', 'od_shivat_yamim_anokhi_mamtir', 'u_machiti_et_kol_ha_yequm', 'ke_khol_asher_tzivahu_YHWH', 'noach_ben_shesh_meot_shanah', 'ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes', 'shnayim_shnayim_bau_el_noach', 'ka_asher_tzivah_elohim_et_noach', 'le_shivat_ha_yamim_mei_ha_mabul', 'ha_geshem_arbaim_yom_va_arbaim_laylah', 'be_etzem_ha_yom_ha_zeh_ba_noach', 'kol_ha_chayah_le_minah_ha_of_le_minehu', 'kol_tzippor_kol_kanaf', 'ha_baim_zakhar_u_nekevah_bau', 'ka_asher_tzivah_oto_elohim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_18_the_rise
###############################################################################
# =============================================================================
# gen_18_the_rise — 7:17-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_18_the_rise.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The rise: the waters lift the ark, all flesh dies, only Noach is left (7:17-24)"""
from machine import Machine

m = Machine("gen_18_the_rise")

# -------------------------- Gen.7.17 · THE_LIFT_AND_THE_RISE ---------------
# וַיְהִי הַמַּבּוּל אַרְבָּעִים יוֹם עַל־הָאָרֶץ וַיִּרְבּוּ הַמַּיִם
# וַיִּשְׂאוּ אֶת־הַתֵּבָה וַתָּרָם מֵעַל הָאָרֶץ
# "And the flood was forty days upon the earth; and the waters increased,
# and bore up the ark, and it was lifted up above the earth."
m.step("Gen.7.17")
# ‹וַיְהִי הַמַּבּוּל אַרְבָּעִים יוֹם עַל־הָאָרֶץ› fact holds: the-deluge-
# forty-day-over-the-earth
m.fact("ha_mabul_arbaim_yom_al_ha_aretz")
# ‹וַיִּרְבּוּ הַמַּיִם וַיִּשְׂאוּ אֶת־הַתֵּבָה› event: lift — agent the-
# waters; theme the-ark
m.event("lift", agent="ha_mayim", themes=["ha_tevah"])
# ‹וַתָּרָם מֵעַל הָאָרֶץ› event: rise — theme the-ark
m.event("rise", themes=["ha_tevah"])
# reads without prior install (flag, not fix): ark, waters
m.presupposed("tevah", "mayim")

# -------------------------- Gen.7.18 · THE_PREVAIL_DEBUT_THE_ARK_WALKS -----
# וַיִּגְבְּרוּ הַמַּיִם וַיִּרְבּוּ מְאֹד עַל־הָאָרֶץ וַתֵּלֶךְ הַתֵּבָה
# עַל־פְּנֵי הַמָּיִם
# "And the waters prevailed, and increased greatly upon the earth; and the
# ark went upon the face of the waters."
m.step("Gen.7.18")
# ‹וַיִּגְבְּרוּ הַמַּיִם› event: prevail — agent the-waters
m.event("prevail", agent="ha_mayim")
# ‹וַיִּרְבּוּ מְאֹד עַל־הָאָרֶץ› fact holds: and-increased-very-over-the-
# earth
m.fact("va_yirbu_meod_al_ha_aretz")
# ‹וַתֵּלֶךְ הַתֵּבָה עַל־פְּנֵי הַמָּיִם› event: walk — agent the-ark;
# theme over-face-of-the-waters
m.event("walk", agent="ha_tevah", themes=["al_pnei_ha_mayim"])

# -------------------------- Gen.7.19 · THE_MOUNTAINS_GO_UNDER --------------
# וְהַמַּיִם גָּבְרוּ מְאֹד מְאֹד עַל־הָאָרֶץ וַיְכֻסּוּ כָּל־הֶהָרִים
# הַגְּבֹהִים אֲשֶׁר־תַּחַת כָּל־הַשָּׁמָיִם
# "And the waters prevailed exceedingly upon the earth; and all the high
# mountains that were under the whole heaven were covered."
m.step("Gen.7.19")
# ‹גָּבְרוּ מְאֹד מְאֹד … כָּל־הֶהָרִים הַגְּבֹהִים אֲשֶׁר־תַּחַת
# כָּל־הַשָּׁמָיִם› fact holds: prevailed-very-very-over-the-earth; all-he-
# mountains-the-high-under-all-the-heavens
m.fact("gavru_meod_meod_al_ha_aretz",
       "kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim")
# ‹וַיְכֻסּוּ כָּל־הֶהָרִים הַגְּבֹהִים› event: cover — theme all-he-
# mountains-the-high
m.event("cover", themes=["kol_he_harim_ha_gevohim"])

# -------------------------- Gen.7.20 · FIFTEEN_CUBITS_UPWARD ---------------
# חֲמֵשׁ עֶשְׂרֵה אַמָּה מִלְמַעְלָה גָּבְרוּ הַמָּיִם וַיְכֻסּוּ הֶהָרִים
# "Fifteen cubits upward did the waters prevail; and the mountains were
# covered."
m.step("Gen.7.20")
# ‹חֲמֵשׁ עֶשְׂרֵה אַמָּה מִלְמַעְלָה גָּבְרוּ הַמָּיִם› fact holds: five--
# teen-cubit-from-upward-prevailed
m.fact("chamesh_esreh_amah_mi_lemalah_gavru")
# ‹וַיְכֻסּוּ הֶהָרִים› event: cover — theme mountains
m.event("cover", themes=["he_harim"])

# -------------------------- Gen.7.21 · ALL_FLESH_EXPIRES -------------------
# וַיִּגְוַע כָּל־בָּשָׂר הָרֹמֵשׂ עַל־הָאָרֶץ בָּעוֹף וּבַבְּהֵמָה
# וּבַחַיָּה וּבְכָל־הַשֶּׁרֶץ הַשֹּׁרֵץ עַל־הָאָרֶץ וְכֹל הָאָדָם
# "And all flesh perished that moved upon the earth, both fowl, and cattle,
# and beast, and every swarming thing that swarmeth upon the earth, and
# every man;"
m.step("Gen.7.21")
# ‹וַיִּגְוַע כָּל־בָּשָׂר› event: expire — theme all-flesh
m.event("expire", themes=["kol_basar"])
# ‹בָּעוֹף וּבַבְּהֵמָה וּבַחַיָּה וּבְכָל־הַשֶּׁרֶץ … וְכֹל הָאָדָם› fact
# holds: in-the-flying-creature-and-and-livestock-and-and-beast-and-and-
# swarming-creature-and-all-the-human
m.fact("ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam")

# -------------------------- Gen.7.22 · THE_COMPOUNDED_BREATH_CRITERION -----
# כֹּל אֲשֶׁר נִשְׁמַת־רוּחַ חַיִּים בְּאַפָּיו מִכֹּל אֲשֶׁר בֶּחָרָבָה
# מֵתוּ
# "all in whose nostrils was the breath of the spirit of life, whatsoever
# was in the dry land, died."
m.step("Gen.7.22")
# ‹נִשְׁמַת־רוּחַ חַיִּים בְּאַפָּיו … מִכֹּל אֲשֶׁר בֶּחָרָבָה מֵתוּ› fact
# holds: breath-of-spirit-wind-life-in-his-nostrils; from-all-which-in-dry-
# land-died
m.fact("nishmat_ruach_chayim_be_apav",
       "mi_kol_asher_be_charavah_metu")

# -------------------------- Gen.7.23 · THE_WIPE_EXECUTED_ONLY_NOACH_LEFT ---
# וַיִּמַח אֶת־כָּל־הַיְקוּם אֲשֶׁר עַל־פְּנֵי הָאֲדָמָה מֵאָדָם
# עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמַיִם וַיִּמָּחוּ מִן־הָאָרֶץ
# וַיִשָּׁאֶר אַךְ־נֹחַ וַאֲשֶׁר אִתּוֹ בַּתֵּבָה
# "And He blotted out every living substance which was upon the face of the
# ground, both man, and cattle, and creeping thing, and fowl of the heaven;
# and they were blotted out from the earth; and Noah only was left, and they
# that were with him in the ark."
m.step("Gen.7.23")
# ‹וַיִּמַח אֶת־כָּל־הַיְקוּם› event: wipe — theme all-the-standing-
# substance
m.event("wipe", themes=["kol_ha_yequm"])
# ‹מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמַיִם› fact holds: from-
# human-until-livestock-until-creeper-and-until-flying-creature
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of")
# ‹וַיִּמָּחוּ מִן־הָאָרֶץ› event: wiped — theme all-the-standing-substance
m.event("wiped", themes=["kol_ha_yequm"])
# ‹וַיִשָּׁאֶר אַךְ־נֹחַ וַאֲשֶׁר אִתּוֹ בַּתֵּבָה› event: remain — theme
# only-Noach-and-which-with-him
m.event("remain", themes=["akh_noach_va_asher_ito"])
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")

# -------------------------- Gen.7.24 · THE_HUNDRED_AND_FIFTY_DAYS ----------
# וַיִּגְבְּרוּ הַמַּיִם עַל־הָאָרֶץ חֲמִשִּׁים וּמְאַת יוֹם
# "And the waters prevailed upon the earth a hundred and fifty days."
m.step("Gen.7.24")
# ‹וַיִּגְבְּרוּ הַמַּיִם עַל־הָאָרֶץ› event: prevail — agent the-waters
m.event("prevail", agent="ha_mayim")
# ‹חֲמִשִּׁים וּמְאַת יוֹם› fact holds: fifty-and-hundred-day-over-the-earth
m.fact("chamishim_u_meat_yom_al_ha_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'mayim', 'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['ha_mabul_arbaim_yom_al_ha_aretz', 'va_yirbu_meod_al_ha_aretz', 'gavru_meod_meod_al_ha_aretz', 'kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim', 'chamesh_esreh_amah_mi_lemalah_gavru', 'ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam', 'nishmat_ruach_chayim_be_apav', 'mi_kol_asher_be_charavah_metu', 'me_adam_ad_behemah_ad_remes_ve_ad_of', 'chamishim_u_meat_yom_al_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_19_the_remembering
###############################################################################
# =============================================================================
# gen_19_the_remembering — 8:1-14
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_19_the_remembering.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The remembering: God remembers Noach, the waters go home, the earth dries (8:1-14)"""
from machine import Machine

m = Machine("gen_19_the_remembering")

# -------------------------- Gen.8.1 · THE_REMEMBERING_THE_WIND -------------
# וַיִּזְכֹּר אֱלֹהִים אֶת־נֹחַ וְאֵת כָּל־הַחַיָּה וְאֶת־כָּל־הַבְּהֵמָה
# אֲשֶׁר אִתּוֹ בַּתֵּבָה וַיַּעֲבֵר אֱלֹהִים רוּחַ עַל־הָאָרֶץ וַיָּשֹׁכּוּ
# הַמָּיִם
# "And God remembered Noah, and every living thing, and all the cattle that
# were with him in the ark; and God made a wind to pass over the earth, and
# the waters assuaged;"
m.step("Gen.8.1")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־נֹחַ וְאֵת כָּל־הַחַיָּה וְאֶת־כָּל־הַבְּהֵמָה›
# event: remember — agent God; theme Noach, all-the-beast-and-the-livestock
m.event("remember", agent="elohim", themes=["noach", "kol_ha_chayah_ve_ha_behemah"])
# ‹וַיַּעֲבֵר אֱלֹהִים רוּחַ עַל־הָאָרֶץ› event: pass — agent God; theme
# spirit-wind-over-the-earth
m.event("pass", agent="elohim", themes=["ruach_al_ha_aretz"])
# ‹וַיָּשֹׁכּוּ הַמָּיִם› event: subside — theme the-waters
m.event("subside", themes=["ha_mayim"])
# reads without prior install (flag, not fix): Noach, ark, waters
m.presupposed("noach", "tevah", "mayim")

# -------------------------- Gen.8.2 · THE_SHUT_MIRROR ----------------------
# וַיִּסָּכְרוּ מַעְיְנֹת תְּהוֹם וַאֲרֻבֹּת הַשָּׁמָיִם וַיִּכָּלֵא
# הַגֶּשֶׁם מִן־הַשָּׁמָיִם
# "the fountains also of the deep and the windows of heaven were stopped,
# and the rain from heaven was restrained."
m.step("Gen.8.2")
# ‹וַיִּסָּכְרוּ מַעְיְנֹת תְּהוֹם וַאֲרֻבֹּת הַשָּׁמָיִם› event: stop-up —
# theme fountains-of-deep-and-windows-of-the-heavens
m.event("stop_up", themes=["mayenot_tehom_va_arubot_ha_shamayim"])
# ‹וַיִּכָּלֵא הַגֶּשֶׁם מִן־הַשָּׁמָיִם› event: restrain — theme the-rain
m.event("restrain", themes=["ha_geshem"])

# -------------------------- Gen.8.3 · THE_WATERS_COMMUTE_BRACKET_CLOSED ----
# וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ הָלוֹךְ וָשׁוֹב וַיַּחְסְרוּ הַמַּיִם
# מִקְצֵה חֲמִשִּׁים וּמְאַת יוֹם
# "And the waters returned from off the earth continually; and after the end
# of a hundred and fifty days the waters decreased."
m.step("Gen.8.3")
# ‹וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ› event: return — agent the-waters
m.event("return", agent="ha_mayim")
# ‹הָלוֹךְ וָשׁוֹב … מִקְצֵה חֲמִשִּׁים וּמְאַת יוֹם› fact holds: going-and-
# returning; from-at-the-end-of-fifty-and-hundred-day
m.fact("halokh_va_shov",
       "mi_qetze_chamishim_u_meat_yom")
# ‹וַיַּחְסְרוּ הַמַּיִם› event: diminish — theme the-waters
m.event("diminish", themes=["ha_mayim"])

# -------------------------- Gen.8.4 · THE_ARK_RESTS ------------------------
# וַתָּנַח הַתֵּבָה בַּחֹדֶשׁ הַשְּׁבִיעִי בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ
# עַל הָרֵי אֲרָרָט
# "And the ark rested in the seventh month, on the seventeenth day of the
# month, upon the mountains of Ararat."
m.step("Gen.8.4")
# ‹וַתָּנַח הַתֵּבָה› event: rest — theme the-ark
m.event("rest", themes=["ha_tevah"])
# ‹בַּחֹדֶשׁ הַשְּׁבִיעִי בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ עַל הָרֵי
# אֲרָרָט› fact holds: in-the-of-month-the-seventh-in-seven-teen-day; over-
# mountains-of-Ararat
m.fact("ba_chodesh_ha_shevii_be_shivah_asar_yom",
       "al_harei_ararat")

# -------------------------- Gen.8.5 · THE_TOPS_APPEAR ----------------------
# וְהַמַּיִם הָיוּ הָלוֹךְ וְחָסוֹר עַד הַחֹדֶשׁ הָעֲשִׂירִי בָּעֲשִׂירִי
# בְּאֶחָד לַחֹדֶשׁ נִרְאוּ רָאשֵׁי הֶהָרִים
# "And the waters decreased continually until the tenth month; in the tenth
# month, on the first day of the month, were the tops of the mountains
# seen."
m.step("Gen.8.5")
# ‹הָלוֹךְ וְחָסוֹר … נִרְאוּ רָאשֵׁי הֶהָרִים› fact holds: going-and-
# diminishing-until-the-of-month-the-tenth; in-the-tenth-in-one-were-seen-
# tops-of-he-mountains
m.fact("halokh_ve_chasor_ad_ha_chodesh_ha_asiri",
       "ba_asiri_be_echad_niru_rashei_he_harim")

# -------------------------- Gen.8.6 · THE_WINDOW_HE_MADE -------------------
# וַיְהִי מִקֵּץ אַרְבָּעִים יוֹם וַיִּפְתַּח נֹחַ אֶת־חַלּוֹן הַתֵּבָה
# אֲשֶׁר עָשָׂה
# "And it came to pass at the end of forty days, that Noah opened the window
# of the ark which he had made."
m.step("Gen.8.6")
# ‹מִקֵּץ אַרְבָּעִים יוֹם› fact holds: from-at-the-end-of-forty-day
m.fact("mi_qetz_arbaim_yom")
# ‹וַיִּפְתַּח נֹחַ אֶת־חַלּוֹן הַתֵּבָה אֲשֶׁר עָשָׂה› event: open — agent
# Noach; theme window-the-ark
m.event("open", agent="noach", themes=["chalon_ha_tevah"])

# -------------------------- Gen.8.7 · THE_RAVEN ----------------------------
# וַיְשַׁלַּח אֶת־הָעֹרֵב וַיֵּצֵא יָצוֹא וָשׁוֹב עַד־יְבֹשֶׁת הַמַּיִם
# מֵעַל הָאָרֶץ
# "And he sent forth a raven, and it went forth to and fro, until the waters
# were dried up from off the earth."
m.step("Gen.8.7")
# ‹וַיְשַׁלַּח אֶת־הָעֹרֵב› event: send — agent Noach; theme the-raven
m.event("send", agent="noach", themes=["ha_orev"])
# ‹יָצוֹא וָשׁוֹב עַד־יְבֹשֶׁת הַמַּיִם› fact holds: going-out-and-
# returning-until-drying-of-the-waters
m.fact("yatzo_va_shov_ad_yevoshet_ha_mayim")

# -------------------------- Gen.8.8 · THE_DOVE_THE_QUESTION ----------------
# וַיְשַׁלַּח אֶת־הַיּוֹנָה מֵאִתּוֹ לִרְאוֹת הֲקַלּוּ הַמַּיִם מֵעַל פְּנֵי
# הָאֲדָמָה
# "And he sent forth a dove from him, to see if the waters were abated from
# off the face of the ground."
m.step("Gen.8.8")
# ‹וַיְשַׁלַּח אֶת־הַיּוֹנָה מֵאִתּוֹ› event: send — agent Noach; theme the-
# dove
m.event("send", agent="noach", themes=["ha_yonah"])
# ‹לִרְאוֹת הֲקַלּוּ הַמַּיִם› fact holds: to-me-see-the-whether-they-
# abated-the-waters
m.fact("li_reot_ha_qalu_ha_mayim")

# -------------------------- Gen.8.9 · NO_RESTING_PLACE_THE_HAND ------------
# וְלֹא־מָצְאָה הַיּוֹנָה מָנוֹחַ לְכַף־רַגְלָהּ וַתָּשָׁב אֵלָיו
# אֶל־הַתֵּבָה כִּי־מַיִם עַל־פְּנֵי כָל־הָאָרֶץ וַיִּשְׁלַח יָדוֹ
# וַיִּקָּחֶהָ וַיָּבֵא אֹתָהּ אֵלָיו אֶל־הַתֵּבָה
# "But the dove found no rest for the sole of her foot, and she returned
# unto him to the ark, for the waters were on the face of the whole earth;
# and he put forth his hand, and took her, and brought her in unto him into
# the ark."
m.step("Gen.8.9")
# ‹וְלֹא־מָצְאָה הַיּוֹנָה מָנוֹחַ לְכַף־רַגְלָהּ כִּי־מַיִם עַל־פְּנֵי
# כָל־הָאָרֶץ› fact holds: not-found-the-dove-resting-place-to-sole-of-her-
# foot; that-waters-over-face-of-all-the-earth
m.fact("lo_matzah_ha_yonah_manoach_le_khaf_raglah",
       "ki_mayim_al_pnei_khol_ha_aretz")
# ‹וַתָּשָׁב אֵלָיו אֶל־הַתֵּבָה› event: return — agent the-dove
m.event("return", agent="ha_yonah")
# ‹וַיִּשְׁלַח יָדוֹ› event: send — agent Noach; theme his-hand
m.event("send", agent="noach", themes=["yado"])
# ‹וַיִּקָּחֶהָ› event: take — agent Noach; theme the-dove
m.event("take", agent="noach", themes=["ha_yonah"])
# ‹וַיָּבֵא אֹתָהּ אֵלָיו אֶל־הַתֵּבָה› event: bring — agent Noach; theme
# the-dove
m.event("bring", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.10 · THE_FIRST_WAIT ----------------------
# וַיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים וַיֹּסֶף שַׁלַּח אֶת־הַיּוֹנָה
# מִן־הַתֵּבָה
# "And he stayed yet other seven days; and again he sent forth the dove out
# of the ark."
m.step("Gen.8.10")
# ‹וַיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים› event: wait — agent Noach
m.event("wait", agent="noach")
# ‹עוֹד שִׁבְעַת יָמִים אֲחֵרִים› fact holds: again-seven-day-other
m.fact("od_shivat_yamim_acherim")
# ‹וַיֹּסֶף שַׁלַּח אֶת־הַיּוֹנָה› event: send — agent Noach; theme the-dove
m.event("send", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.11 · THE_LEAF_AT_EVENING -----------------
# וַתָּבֹא אֵלָיו הַיּוֹנָה לְעֵת עֶרֶב וְהִנֵּה עֲלֵה־זַיִת טָרָף בְּפִיהָ
# וַיֵּדַע נֹחַ כִּי־קַלּוּ הַמַּיִם מֵעַל הָאָרֶץ
# "And the dove came in to him at eventide; and lo in her mouth an olive-
# leaf freshly plucked; so Noah knew that the waters were abated from off
# the earth."
m.step("Gen.8.11")
# ‹וַתָּבֹא אֵלָיו הַיּוֹנָה לְעֵת עֶרֶב› event: come — agent the-dove;
# theme to-obj-marker·et-evening
m.event("come", agent="ha_yonah", themes=["le_et_erev"])
# ‹וְהִנֵּה עֲלֵה־זַיִת טָרָף בְּפִיהָ› fact holds: leaf-olive-freshly-
# plucked-in-her-mouth
m.fact("aleh_zayit_taraf_be_fiha")
# ‹וַיֵּדַע נֹחַ כִּי־קַלּוּ הַמַּיִם› event: know — agent Noach; theme
# that-whether-they-abated-the-waters
m.event("know", agent="noach", themes=["ki_qalu_ha_mayim"])

# -------------------------- Gen.8.12 · THE_SECOND_WAIT_THE_LAST_OD ---------
# וַיִּיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים וַיְשַׁלַּח אֶת־הַיּוֹנָה
# וְלֹא־יָסְפָה שׁוּב־אֵלָיו עוֹד
# "And he stayed yet other seven days; and sent forth the dove; and she
# returned not again unto him any more."
m.step("Gen.8.12")
# ‹וַיִּיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים› event: wait — agent Noach
m.event("wait", agent="noach")
# ‹וַיְשַׁלַּח אֶת־הַיּוֹנָה› event: send — agent Noach; theme the-dove
m.event("send", agent="noach", themes=["ha_yonah"])
# ‹וְלֹא־יָסְפָה שׁוּב־אֵלָיו עוֹד› fact holds: and-not-did-again-return-to-
# him-again
m.fact("ve_lo_yasfah_shuv_elav_od")

# -------------------------- Gen.8.13 · NEW_YEARS_DAY_THE_COVER_OFF ---------
# וַיְהִי בְּאַחַת וְשֵׁשׁ־מֵאוֹת שָׁנָה בָּרִאשׁוֹן בְּאֶחָד לַחֹדֶשׁ
# חָרְבוּ הַמַּיִם מֵעַל הָאָרֶץ וַיָּסַר נֹחַ אֶת־מִכְסֵה הַתֵּבָה וַיַּרְא
# וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה
# "And it came to pass in the six hundred and first year, in the first
# month, the first day of the month, the waters were dried up from off the
# earth; and Noah removed the covering of the ark, and looked, and behold,
# the face of the ground was dried."
m.step("Gen.8.13")
# ‹בְּאַחַת וְשֵׁשׁ־מֵאוֹת שָׁנָה בָּרִאשׁוֹן בְּאֶחָד לַחֹדֶשׁ› clock
# anchored: t0 := year-of-601-of-month-1-day-1
m.time_anchor("shnat_601_chodesh_1_yom_1")
# ‹חָרְבוּ הַמַּיִם מֵעַל הָאָרֶץ› fact holds: were-parched-the-waters-from-
# over-the-earth
m.fact("charvu_ha_mayim_me_al_ha_aretz")
# ‹וַיָּסַר נֹחַ אֶת־מִכְסֵה הַתֵּבָה› event: remove — agent Noach; theme
# covering-the-ark
m.event("remove", agent="noach", themes=["mikhseh_ha_tevah"])
# ‹וַיַּרְא וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה› event: see — agent Noach;
# theme face-of-the-ground
m.event("see", agent="noach", themes=["pnei_ha_adamah"])
# ‹וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה› fact holds: and-behold-were-parched-
# face-of-the-ground
m.fact("ve_hinneh_charvu_pnei_ha_adamah")

# -------------------------- Gen.8.14 · THE_EARTH_DRY -----------------------
# וּבַחֹדֶשׁ הַשֵּׁנִי בְּשִׁבְעָה וְעֶשְׂרִים יוֹם לַחֹדֶשׁ יָבְשָׁה
# הָאָרֶץ
# "And in the second month, on the seven and twentieth day of the month, was
# the earth dry."
m.step("Gen.8.14")
# ‹בְּשִׁבְעָה וְעֶשְׂרִים יוֹם לַחֹדֶשׁ יָבְשָׁה הָאָרֶץ› fact holds: in-
# the-of-month-the-second-in-seven-and-twenty-day; was-dry-the-earth
m.fact("ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom",
       "yavshah_ha_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'noach', 'mayim', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['halokh_va_shov', 'mi_qetze_chamishim_u_meat_yom', 'ba_chodesh_ha_shevii_be_shivah_asar_yom', 'al_harei_ararat', 'halokh_ve_chasor_ad_ha_chodesh_ha_asiri', 'ba_asiri_be_echad_niru_rashei_he_harim', 'mi_qetz_arbaim_yom', 'yatzo_va_shov_ad_yevoshet_ha_mayim', 'li_reot_ha_qalu_ha_mayim', 'lo_matzah_ha_yonah_manoach_le_khaf_raglah', 'ki_mayim_al_pnei_khol_ha_aretz', 'od_shivat_yamim_acherim', 'aleh_zayit_taraf_be_fiha', 've_lo_yasfah_shuv_elav_od', 'charvu_ha_mayim_me_al_ha_aretz', 've_hinneh_charvu_pnei_ha_adamah', 'ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom', 'yavshah_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_20_exit_altar
###############################################################################
# =============================================================================
# gen_20_exit_altar — 8:15-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_20_exit_altar.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The exit and the altar: go out, the families, the pleasing smell, never again (8:15-22)"""
from machine import Machine

m = Machine("gen_20_exit_altar")

# -------------------------- Gen.8.15 · THE_SPEAK_VERB_DEBUTS ---------------
# וַיְדַבֵּר אֱלֹהִים אֶל־נֹחַ לֵאמֹר
# "And God spoke unto Noah, saying:"
m.step("Gen.8.15")
# ‹וַיְדַבֵּר אֱלֹהִים אֶל־נֹחַ לֵאמֹר› event: speak — agent God; theme to-
# Noach
m.event("speak", agent="elohim", themes=["el_noach"])
# reads without prior install (flag, not fix): Noach, ark
m.presupposed("noach", "tevah")

# -------------------------- Gen.8.16 · THE_EXIT_COMMAND --------------------
# צֵא מִן־הַתֵּבָה אַתָּה וְאִשְׁתְּךָ וּבָנֶיךָ וּנְשֵׁי־בָנֶיךָ אִתָּךְ
# "'Go forth from the ark, thou, and thy wife, and thy sons, and thy sons'
# wives with thee."
m.step("Gen.8.16")
# ‹צֵא מִן־הַתֵּבָה› God speaks a demand — LET: go-out(Noach, from-the-ark)
m.declare("elohim", "LET",
          "tze(noach, min_ha_tevah)")

# -------------------------- Gen.8.17 · THE_BRING_OUT_AND_THE_CHARGE --------
# כָּל־הַחַיָּה אֲשֶׁר־אִתְּךָ מִכָּל־בָּשָׂר בָּעוֹף וּבַבְּהֵמָה
# וּבְכָל־הָרֶמֶשׂ הָרֹמֵשׂ עַל־הָאָרֶץ הוצא הַיְצֵא אִתָּךְ וְשָׁרְצוּ
# בָאָרֶץ וּפָרוּ וְרָבוּ עַל־הָאָרֶץ
# "Bring forth with thee every living thing that is with thee, of all flesh,
# both fowl, and cattle, and every creeping thing that creepeth upon the
# earth; that they may swarm in the earth, and be fruitful, and multiply
# upon the earth.'"
m.step("Gen.8.17")
# ‹הוצא הַיְצֵא אִתָּךְ› God speaks a demand — LET: bring-out(all-the-beast,
# with-you)
m.declare("elohim", "LET",
          "hotze(kol_ha_chayah, itakh)")
# ‹וְשָׁרְצוּ בָאָרֶץ וּפָרוּ וְרָבוּ עַל־הָאָרֶץ› fact holds: and-they-
# shall-swarm-and-be-fruitful-and-multiply-over-the-earth
m.fact("ve_shartzu_u_faru_ve_ravu_al_ha_aretz")

# -------------------------- Gen.8.18 · THE_EXIT_RECEIPT --------------------
# וַיֵּצֵא־נֹחַ וּבָנָיו וְאִשְׁתּוֹ וּנְשֵׁי־בָנָיו אִתּוֹ
# "And Noah went forth, and his sons, and his wife, and his sons' wives with
# him;"
m.step("Gen.8.18")
# ‹וַיֵּצֵא־נֹחַ› event: go-out — agent Noach
m.event("go_out", agent="noach")
# ‹וַיֵּצֵא־נֹחַ … אִתּוֹ› demand settled (popped from the queue): go-
# out(Noach, from-the-ark)
m.result("tze(noach, min_ha_tevah)", tmark="t1")

# -------------------------- Gen.8.19 · OUT_BY_FAMILIES ---------------------
# כָּל־הַחַיָּה כָּל־הָרֶמֶשׂ וְכָל־הָעוֹף כֹּל רוֹמֵשׂ עַל־הָאָרֶץ
# לְמִשְׁפְּחֹתֵיהֶם יָצְאוּ מִן־הַתֵּבָה
# "every beast, every creeping thing, and every fowl, whatsoever moveth upon
# the earth, after their families, went forth out of the ark."
m.step("Gen.8.19")
# ‹לְמִשְׁפְּחֹתֵיהֶם יָצְאוּ מִן־הַתֵּבָה› fact holds: to-mishpechoteihem-
# they-went-out-from-the-ark
m.fact("le_mishpechoteihem_yatzu_min_ha_tevah")
# ‹יָצְאוּ מִן־הַתֵּבָה› demand settled (popped from the queue): bring-
# out(all-the-beast, with-you)
m.result("hotze(kol_ha_chayah, itakh)", tmark="t1")

# -------------------------- Gen.8.20 · THE_FIRST_ALTAR ---------------------
# וַיִּבֶן נֹחַ מִזְבֵּחַ לַיהוָה וַיִּקַּח מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה
# וּמִכֹּל הָעוֹף הַטָּהֹר וַיַּעַל עֹלֹת בַּמִּזְבֵּחַ
# "And Noah builded an altar unto the LORD; and took of every clean beast,
# and of every clean fowl, and offered burnt-offerings on the altar."
m.step("Gen.8.20")
# ‹וַיִּבֶן נֹחַ מִזְבֵּחַ לַיהוָה› event: build — agent Noach; theme altar
m.event("build", agent="noach", themes=["mizbeach"])
# ‹מִזְבֵּחַ› the world gains: altar
m.install("mizbeach")
# ‹וַיִּקַּח מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה וּמִכֹּל הָעוֹף הַטָּהֹר› event:
# take — agent Noach; theme from-the-livestock-the-clean-and-from-the-
# flying-creature-the-clean
m.event("take", agent="noach", themes=["min_ha_behemah_ha_tehorah_u_min_ha_of_ha_tahor"])
# ‹וַיַּעַל עֹלֹת בַּמִּזְבֵּחַ› event: offer-up — agent Noach; theme burnt-
# offerings-in-the-altar
m.event("offer_up", agent="noach", themes=["olot_ba_mizbeach"])

# -------------------------- Gen.8.21 · THE_SMELL_THE_HEART_THE_NEVER_AGAINS -
# וַיָּרַח יְהוָה אֶת־רֵיחַ הַנִּיחֹחַ וַיֹּאמֶר יְהוָה אֶל־לִבּוֹ לֹא־אֹסִף
# לְקַלֵּל עוֹד אֶת־הָאֲדָמָה בַּעֲבוּר הָאָדָם כִּי יֵצֶר לֵב הָאָדָם רַע
# מִנְּעֻרָיו וְלֹא־אֹסִף עוֹד לְהַכּוֹת אֶת־כָּל־חַי כַּאֲשֶׁר עָשִׂיתִי
# "And the LORD smelled the sweet savour; and the LORD said in His heart: 'I
# will not again curse the ground any more for man's sake; for the
# imagination of man's heart is evil from his youth; neither will I again
# smite any more every thing living, as I have done."
m.step("Gen.8.21")
# ‹וַיָּרַח יְהוָה אֶת־רֵיחַ הַנִּיחֹחַ› event: smell — agent the-LORD;
# theme odor-the-pleasing-savor
m.event("smell", agent="YHWH", themes=["reiach_ha_nichoach"])
# ‹רֵיחַ הַנִּיחֹחַ› test PASS — oracle-word pleasing-savor, on the-burnt-
# offering
m.test("PASS", "nichoach", "ha_olah")
# ‹וַיֹּאמֶר יְהוָה אֶל־לִבּוֹ› event: say — agent the-LORD; theme to-His-
# heart
m.event("say", agent="YHWH", themes=["el_libo"])
# ‹לֹא־אֹסִף לְקַלֵּל עוֹד אֶת־הָאֲדָמָה בַּעֲבוּר הָאָדָם כִּי יֵצֶר לֵב
# הָאָדָם רַע מִנְּעֻרָיו› standing constraint: not-will-I-again-to-curse-
# again-obj-marker·et-the-ground
m.invariant("lo_osif_le_qalel_od_et_ha_adamah")
# ‹וְלֹא־אֹסִף עוֹד לְהַכּוֹת אֶת־כָּל־חַי כַּאֲשֶׁר עָשִׂיתִי› standing
# constraint: not-will-I-again-again-to-strike-obj-marker·et-all-living
m.invariant("lo_osif_od_le_hakot_et_kol_chai")

# -------------------------- Gen.8.22 · THE_SEASONS_PLEDGE ------------------
# עֹד כָּל־יְמֵי הָאָרֶץ זֶרַע וְקָצִיר וְקֹר וָחֹם וְקַיִץ וָחֹרֶף וְיוֹם
# וָלַיְלָה לֹא יִשְׁבֹּתוּ
# "While the earth remaineth, seedtime and harvest, and cold and heat, and
# summer and winter, and day and night shall not cease.'"
m.step("Gen.8.22")
# ‹זֶרַע וְקָצִיר וְקֹר וָחֹם וְקַיִץ וָחֹרֶף וְיוֹם וָלַיְלָה לֹא
# יִשְׁבֹּתוּ› standing constraint: seedtime-and-harvest-and-cold-and-heat-
# and-summer-and-winter-and-day-and-night-not-shall-cease
m.invariant("zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach'}
    assert m.presupposed_set() == {'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'nichoach', 'ha_olah')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_shartzu_u_faru_ve_ravu_al_ha_aretz', 'le_mishpechoteihem_yatzu_min_ha_tevah'])
    assert m.WORLD["invariants"] == ['lo_osif_le_qalel_od_et_ha_adamah', 'lo_osif_od_le_hakot_et_kol_chai', 'zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_21_blessing_blood_law
###############################################################################
# =============================================================================
# gen_21_blessing_blood_law — 9:1-7
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_21_blessing_blood_law.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The blessing and the blood-law: be fruitful again, but the blood is Mine (9:1-7)"""
from machine import Machine

m = Machine("gen_21_blessing_blood_law")

# -------------------------- Gen.9.1 · THE_BLESSING_REISSUED_SHORTER --------
# וַיְבָרֶךְ אֱלֹהִים אֶת־נֹחַ וְאֶת־בָּנָיו וַיֹּאמֶר לָהֶם פְּרוּ וּרְבוּ
# וּמִלְאוּ אֶת־הָאָרֶץ
# "And God blessed Noah and his sons, and said unto them: 'Be fruitful and
# multiply, and replenish the earth."
m.step("Gen.9.1")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־נֹחַ וְאֶת־בָּנָיו … פְּרוּ וּרְבוּ וּמִלְאוּ
# אֶת־הָאָרֶץ› blessing: God blesses Noach-and-vanav — mandate: CMD!(peru),
# CMD!(revu), CMD!(milu(et-the-aretz))
m.bless("elohim", "noach_u_vanav", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_aretz))"])
# reads without prior install (flag, not fix): Noach, banav
m.presupposed("noach", "banav")

# -------------------------- Gen.9.2 · FEAR_AND_DREAD_IN_DOMINIONS_PLACE ----
# וּמוֹרַאֲכֶם וְחִתְּכֶם יִהְיֶה עַל כָּל־חַיַּת הָאָרֶץ וְעַל כָּל־עוֹף
# הַשָּׁמָיִם בְּכֹל אֲשֶׁר תִּרְמֹשׂ הָאֲדָמָה וּבְכָל־דְּגֵי הַיָּם
# בְּיֶדְכֶם נִתָּנוּ
# "And the fear of you and the dread of you shall be upon every beast of the
# earth, and upon every fowl of the air, and upon all wherewith the ground
# teemeth, and upon all the fishes of the sea: into your hand are they
# delivered."
m.step("Gen.9.2")
# ‹וּמוֹרַאֲכֶם וְחִתְּכֶם … בְּיֶדְכֶם נִתָּנוּ› fact holds: moraakhem-and-
# chitkhem-over-all-living-the-earth; in-yedkhem-nittanu
m.fact("moraakhem_ve_chitkhem_al_kol_chayat_ha_aretz",
       "be_yedkhem_nittanu")

# -------------------------- Gen.9.3 · THE_MEAT_GRANT_CITES_THE_OLD ---------
# כָּל־רֶמֶשׂ אֲשֶׁר הוּא־חַי לָכֶם יִהְיֶה לְאָכְלָה כְּיֶרֶק עֵשֶׂב
# נָתַתִּי לָכֶם אֶת־כֹּל
# "Every moving thing that liveth shall be for food for you; as the green
# herb have I given you all."
m.step("Gen.9.3")
# ‹כָּל־רֶמֶשׂ אֲשֶׁר הוּא־חַי … לְאָכְלָה› role assigned: all-moving-thing-
# which-it-living -> food-to-you
m.assign("kol_remes_asher_hu_chai", "okhlah_la_khem")
# ‹לָכֶם יִהְיֶה לְאָכְלָה› God speaks a demand — LET?: yihyeh(all-moving-
# thing-living, for-food)
m.declare("elohim", "LET?",
          "yihyeh(kol_remes_chai, le_okhlah)")
# ‹כְּיֶרֶק עֵשֶׂב נָתַתִּי לָכֶם אֶת־כֹּל› fact holds: like-as-the-green-
# of-herb-I-have-given-to-you-obj-marker·et-all
m.fact("ke_yereq_esev_natati_la_khem_et_kol")

# -------------------------- Gen.9.4 · THE_FIRST_PROHIBITION_SINCE_EDEN -----
# אַךְ־בָּשָׂר בְּנַפְשׁוֹ דָמוֹ לֹא תֹאכֵלוּ
# "Only flesh with the life thereof, which is the blood thereof, shall ye
# not eat."
m.step("Gen.9.4")
# ‹אַךְ־בָּשָׂר בְּנַפְשׁוֹ דָמוֹ לֹא תֹאכֵלוּ› God speaks a demand — LET-
# NOT: eat(flesh-in-nafsho-damo)
m.declare("elohim", "LET-NOT",
          "akhal(basar_be_nafsho_damo)")

# -------------------------- Gen.9.5 · THE_RECKONING_LADDER -----------------
# וְאַךְ אֶת־דִּמְכֶם לְנַפְשֹׁתֵיכֶם אֶדְרֹשׁ מִיַּד כָּל־חַיָּה
# אֶדְרְשֶׁנּוּ וּמִיַּד הָאָדָם מִיַּד אִישׁ אָחִיו אֶדְרֹשׁ אֶת־נֶפֶשׁ
# הָאָדָם
# "And surely your blood of your lives will I require; at the hand of every
# beast will I require it; and at the hand of man, even at the hand of every
# man's brother, will I require the life of man."
m.step("Gen.9.5")
# ‹וְאַךְ אֶת־דִּמְכֶם לְנַפְשֹׁתֵיכֶם אֶדְרֹשׁ … אֶדְרְשֶׁנּוּ … אֶדְרֹשׁ›
# standing constraint: obj-marker·et-dimkhem-to-nafshoteikhem-I-will-require
m.invariant("et_dimkhem_le_nafshoteikhem_edrosh")
# ‹מִיַּד כָּל־חַיָּה … וּמִיַּד הָאָדָם מִיַּד אִישׁ אָחִיו› fact holds:
# from-hand-of-all-beast-and-from-hand-of-the-human-a-man-his-brother
m.fact("mi_yad_kol_chayah_u_mi_yad_ha_adam_ish_achiv")

# -------------------------- Gen.9.6 · THE_TALION_ON_THE_IMAGE_GROUND -------
# שֹׁפֵךְ דַּם הָאָדָם בָּאָדָם דָּמוֹ יִשָּׁפֵךְ כִּי בְּצֶלֶם אֱלֹהִים
# עָשָׂה אֶת־הָאָדָם
# "Whoso sheddeth man's blood, by man shall his blood be shed; for in the
# image of God made He man."
m.step("Gen.9.6")
# ‹שֹׁפֵךְ דַּם הָאָדָם בָּאָדָם דָּמוֹ יִשָּׁפֵךְ› standing handler — if
# shedder-of(blood-of-the-human) then in-the-human-damo-shall-be-shed
m.handler("shofekh(dam_ha_adam)",
          "ba_adam_damo_yishafekh")
# ‹כִּי בְּצֶלֶם אֱלֹהִים עָשָׂה אֶת־הָאָדָם› fact holds: that-in-image-of-
# God-make-obj-marker·et-the-human
m.fact("ki_be_tzelem_elohim_asah_et_ha_adam")

# -------------------------- Gen.9.7 · THE_FRAME_REDOUBLED ------------------
# וְאַתֶּם פְּרוּ וּרְבוּ שִׁרְצוּ בָאָרֶץ וּרְבוּ־בָהּ
# "And you, be ye fruitful, and multiply; swarm in the earth, and multiply
# therein.'"
m.step("Gen.9.7")
# ‹וְאַתֶּם פְּרוּ וּרְבוּ שִׁרְצוּ בָאָרֶץ וּרְבוּ־בָהּ› fact holds: and-
# you-be-fruitful-and-multiply-swarm-and-earth
m.fact("ve_atem_peru_u_revu_shirtzu_va_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'noach', 'banav'}
    assert m.REGISTRY["names"] == {'kol_remes_asher_hu_chai': 'okhlah_la_khem'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['yihyeh(kol_remes_chai, le_okhlah)', 'akhal(basar_be_nafsho_damo)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2, 'assigned_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_aretz))', 'moraakhem_ve_chitkhem_al_kol_chayat_ha_aretz', 'be_yedkhem_nittanu', 'ke_yereq_esev_natati_la_khem_et_kol', 'mi_yad_kol_chayah_u_mi_yad_ha_adam_ish_achiv', 'handler: IF(shofekh(dam_ha_adam)) THEN(ba_adam_damo_yishafekh)', 'ki_be_tzelem_elohim_asah_et_ha_adam', 've_atem_peru_u_revu_shirtzu_va_aretz'])
    assert m.WORLD["invariants"] == ['et_dimkhem_le_nafshoteikhem_edrosh']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_22_covenant_bow
###############################################################################
# =============================================================================
# gen_22_covenant_bow — 9:8-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_22_covenant_bow.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The covenant and the bow: My bow I have set in the cloud (9:8-17)"""
from machine import Machine

m = Machine("gen_22_covenant_bow")

# -------------------------- Gen.9.8 · THE_TRIPLE_FRAME_OPENS ---------------
# וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ וְאֶל־בָּנָיו אִתּוֹ לֵאמֹר
# "And God spoke unto Noah, and to his sons with him, saying:"
m.step("Gen.9.8")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ וְאֶל־בָּנָיו אִתּוֹ› event: speak — agent
# God; theme to-Noach-and-to-banav
m.event("speak", agent="elohim", themes=["el_noach_ve_el_banav"])
# reads without prior install (flag, not fix): Noach, banav, ark
m.presupposed("noach", "banav", "tevah")

# -------------------------- Gen.9.9 · I_AM_ESTABLISHING --------------------
# וַאֲנִי הִנְנִי מֵקִים אֶת־בְּרִיתִי אִתְּכֶם וְאֶת־זַרְעֲכֶם אַחֲרֵיכֶם
# "'As for Me, behold, I establish My covenant with you, and with your seed
# after you;"
m.step("Gen.9.9")
# ‹הִנְנִי מֵקִים אֶת־בְּרִיתִי אִתְּכֶם וְאֶת־זַרְעֲכֶם› fact holds: hinni-
# mekim-obj-marker·et-My-covenant-itkhem
m.fact("hinni_mekim_et_briti_itkhem")

# -------------------------- Gen.9.10 · EVERY_LIVING_SOUL_A_PARTY -----------
# וְאֵת כָּל־נֶפֶשׁ הַחַיָּה אֲשֶׁר אִתְּכֶם בָּעוֹף בַּבְּהֵמָה
# וּבְכָל־חַיַּת הָאָרֶץ אִתְּכֶם מִכֹּל יֹצְאֵי הַתֵּבָה לְכֹל חַיַּת
# הָאָרֶץ
# "and with every living creature that is with you, the fowl, the cattle,
# and every beast of the earth with you; of all that go out of the ark, even
# every beast of the earth."
m.step("Gen.9.10")
# ‹וְאֵת כָּל־נֶפֶשׁ הַחַיָּה אֲשֶׁר אִתְּכֶם … מִכֹּל יֹצְאֵי הַתֵּבָה›
# fact holds: and-obj-marker·et-all-soul-of-the-beast-which-itkhem
m.fact("ve_et_kol_nefesh_ha_chayah_asher_itkhem")

# -------------------------- Gen.9.11 · THE_CUT_VERB_BORN_REFUSING ----------
# וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתְּכֶם וְלֹא־יִכָּרֵת כָּל־בָּשָׂר עוֹד מִמֵּי
# הַמַּבּוּל וְלֹא־יִהְיֶה עוֹד מַבּוּל לְשַׁחֵת הָאָרֶץ
# "And I will establish My covenant with you; neither shall all flesh be cut
# off any more by the waters of the flood; neither shall there any more be a
# flood to destroy the earth.'"
m.step("Gen.9.11")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתְּכֶם› fact holds: and-I-will-establish-obj-
# marker·et-My-covenant-itkhem
m.fact("va_hakimoti_et_briti_itkhem")
# ‹וְלֹא־יִכָּרֵת כָּל־בָּשָׂר עוֹד מִמֵּי הַמַּבּוּל› standing constraint:
# and-not-yikkaret-all-flesh-still/again-from-waters-of-the-deluge
m.invariant("ve_lo_yikkaret_kol_basar_od_mi_mei_ha_mabul")
# ‹וְלֹא־יִהְיֶה עוֹד מַבּוּל לְשַׁחֵת הָאָרֶץ› standing constraint: and-
# not-yihyeh-still/again-deluge-to-destroy-the-earth
m.invariant("ve_lo_yihyeh_od_mabul_le_shachet_ha_aretz")

# -------------------------- Gen.9.12 · THE_FRAME_REOPENS_ON_THE_SIGN -------
# וַיֹּאמֶר אֱלֹהִים זֹאת אוֹת־הַבְּרִית אֲשֶׁר־אֲנִי נֹתֵן בֵּינִי
# וּבֵינֵיכֶם וּבֵין כָּל־נֶפֶשׁ חַיָּה אֲשֶׁר אִתְּכֶם לְדֹרֹת עוֹלָם
# "And God said: 'This is the token of the covenant which I make between Me
# and you and every living creature that is with you, for perpetual
# generations:"
m.step("Gen.9.12")
# ‹וַיֹּאמֶר אֱלֹהִים זֹאת אוֹת־הַבְּרִית› event: speak — agent God; theme
# this-sign-of-the-brit
m.event("speak", agent="elohim", themes=["zot_ot_ha_brit"])
# ‹אֲשֶׁר־אֲנִי נֹתֵן בֵּינִי וּבֵינֵיכֶם … לְדֹרֹת עוֹלָם› fact holds:
# I-giving-beini-and-veineikhem-to-generations-of-everlasting
m.fact("ani_noten_beini_u_veineikhem_le_dorot_olam")

# -------------------------- Gen.9.13 · MY_BOW_IN_THE_CLOUD -----------------
# אֶת־קַשְׁתִּי נָתַתִּי בֶּעָנָן וְהָיְתָה לְאוֹת בְּרִית בֵּינִי וּבֵין
# הָאָרֶץ
# "I have set My bow in the cloud, and it shall be for a token of a covenant
# between Me and the earth."
m.step("Gen.9.13")
# ‹אֶת־קַשְׁתִּי נָתַתִּי בֶּעָנָן וְהָיְתָה לְאוֹת בְּרִית› fact holds:
# obj-marker·et-qashti-I-have-set-in-cloud; and-haytah-to-sign-of-brit-
# beini-and-vein-the-earth
m.fact("et_qashti_natati_be_anan",
       "ve_haytah_le_ot_brit_beini_u_vein_ha_aretz")

# -------------------------- Gen.9.14 · THE_WEATHER_WIRED_HANDLER -----------
# וְהָיָה בְּעַנְנִי עָנָן עַל־הָאָרֶץ וְנִרְאֲתָה הַקֶּשֶׁת בֶּעָנָן
# "And it shall come to pass, when I bring clouds over the earth, and the
# bow is seen in the cloud,"
m.step("Gen.9.14")
# ‹וְהָיָה בְּעַנְנִי עָנָן … וְנִרְאֲתָה הַקֶּשֶׁת … וְזָכַרְתִּי› standing
# handler — if in-anni-cloud-and-nireatah-the-bow then and-I-will-remember-
# obj-marker·et-My-covenant
m.handler("be_anni_anan_ve_nireatah_ha_qeshet",
          "ve_zakharti_et_briti")

# -------------------------- Gen.9.15 · THE_REMEMBERING_PLEDGED -------------
# וְזָכַרְתִּי אֶת־בְּרִיתִי אֲשֶׁר בֵּינִי וּבֵינֵיכֶם וּבֵין כָּל־נֶפֶשׁ
# חַיָּה בְּכָל־בָּשָׂר וְלֹא־יִהְיֶה עוֹד הַמַּיִם לְמַבּוּל לְשַׁחֵת
# כָּל־בָּשָׂר
# "that I will remember My covenant, which is between Me and you and every
# living creature of all flesh; and the waters shall no more become a flood
# to destroy all flesh."
m.step("Gen.9.15")
# ‹וְזָכַרְתִּי אֶת־בְּרִיתִי … וְלֹא־יִהְיֶה עוֹד הַמַּיִם לְמַבּוּל› fact
# holds: and-I-will-remember-obj-marker·et-My-covenant-beini-and-veineikhem;
# and-not-yihyeh-still/again-the-waters-to-deluge
m.fact("ve_zakharti_et_briti_beini_u_veineikhem",
       "ve_lo_yihyeh_od_ha_mayim_le_mabul")

# -------------------------- Gen.9.16 · TO_REMEMBER_THE_EVERLASTING ---------
# וְהָיְתָה הַקֶּשֶׁת בֶּעָנָן וּרְאִיתִיהָ לִזְכֹּר בְּרִית עוֹלָם בֵּין
# אֱלֹהִים וּבֵין כָּל־נֶפֶשׁ חַיָּה בְּכָל־בָּשָׂר אֲשֶׁר עַל־הָאָרֶץ
# "And the bow shall be in the cloud; and I will look upon it, that I may
# remember the everlasting covenant between God and every living creature of
# all flesh that is upon the earth.'"
m.step("Gen.9.16")
# ‹וּרְאִיתִיהָ לִזְכֹּר בְּרִית עוֹלָם בֵּין אֱלֹהִים וּבֵין כָּל־נֶפֶשׁ
# חַיָּה› fact holds: and-reitiha-to-me-zekor-brit-everlasting
m.fact("u_reitiha_li_zekor_brit_olam")

# -------------------------- Gen.9.17 · THE_SEAL_I_HAVE_ESTABLISHED ---------
# וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ זֹאת אוֹת־הַבְּרִית אֲשֶׁר הֲקִמֹתִי בֵּינִי
# וּבֵין כָּל־בָּשָׂר אֲשֶׁר עַל־הָאָרֶץ
# "And God said unto Noah: 'This is the token of the covenant which I have
# established between Me and all flesh that is upon the earth.'"
m.step("Gen.9.17")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ› event: speak — agent God; theme to-Noach
m.event("speak", agent="elohim", themes=["el_noach"])
# ‹זֹאת אוֹת־הַבְּרִית אֲשֶׁר הֲקִמֹתִי› fact holds: this-sign-of-the-brit-
# which-I-will-establish
m.fact("zot_ot_ha_brit_asher_hakimoti")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'tevah', 'banav', 'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['hinni_mekim_et_briti_itkhem', 've_et_kol_nefesh_ha_chayah_asher_itkhem', 'va_hakimoti_et_briti_itkhem', 'ani_noten_beini_u_veineikhem_le_dorot_olam', 'et_qashti_natati_be_anan', 've_haytah_le_ot_brit_beini_u_vein_ha_aretz', 'handler: IF(be_anni_anan_ve_nireatah_ha_qeshet) THEN(ve_zakharti_et_briti)', 've_zakharti_et_briti_beini_u_veineikhem', 've_lo_yihyeh_od_ha_mayim_le_mabul', 'u_reitiha_li_zekor_brit_olam', 'zot_ot_ha_brit_asher_hakimoti'])
    assert m.WORLD["invariants"] == ['ve_lo_yikkaret_kol_basar_od_mi_mei_ha_mabul', 've_lo_yihyeh_od_mabul_le_shachet_ha_aretz']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_23_vineyard_curse
###############################################################################
# =============================================================================
# gen_23_vineyard_curse — 9:18-29
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_23_vineyard_curse.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The vineyard and the curse: cursed be Canaan, blessed be the LORD (9:18-29)"""
from machine import Machine

m = Machine("gen_23_vineyard_curse")

# -------------------------- Gen.9.18 · THE_ROSTER_OUT_OF_THE_ARK -----------
# וַיִּהְיוּ בְנֵי־נֹחַ הַיֹּצְאִים מִן־הַתֵּבָה שֵׁם וְחָם וָיָפֶת וְחָם
# הוּא אֲבִי כְנָעַן
# "And the sons of Noah, that went forth from the ark, were Shem, and Ham,
# and Japheth; and Ham is the father of Canaan."
m.step("Gen.9.18")
# ‹וַיִּהְיוּ בְנֵי־נֹחַ הַיֹּצְאִים מִן־הַתֵּבָה … וְחָם הוּא אֲבִי
# כְנָעַן› fact holds: sons-of-Noach-the-going-out-of-from-the-ark-Shem-Ham-
# and-Yefet; Ham-he-father-of-Canaan
m.fact("bnei_noach_ha_yotzim_min_ha_tevah_shem_cham_va_yefet",
       "cham_hu_avi_khenaan")
# reads without prior install (flag, not fix): Noach, ark, Canaan
m.presupposed("noach", "tevah", "kenaan")

# -------------------------- Gen.9.19 · THREE_AND_THE_SCATTERED_EARTH -------
# שְׁלֹשָׁה אֵלֶּה בְּנֵי־נֹחַ וּמֵאֵלֶּה נָפְצָה כָל־הָאָרֶץ
# "These three were the sons of Noah, and of these was the whole earth
# overspread."
m.step("Gen.9.19")
# ‹שְׁלֹשָׁה אֵלֶּה … וּמֵאֵלֶּה נָפְצָה כָל־הָאָרֶץ› fact holds: three-
# these-sons-of-Noach; and-from-these-naftzah-all-the-earth
m.fact("shelosha_eleh_bnei_noach",
       "u_me_eleh_naftzah_khol_ha_aretz")

# -------------------------- Gen.9.20 · THE_GROUND_MAN_PLANTS_A_VINEYARD ----
# וַיָּחֶל נֹחַ אִישׁ הָאֲדָמָה וַיִּטַּע כָּרֶם
# "And Noah the husbandman began, and planted a vineyard."
m.step("Gen.9.20")
# ‹וַיָּחֶל נֹחַ› event: begin — agent Noach
m.event("begin", agent="noach")
# ‹אִישׁ הָאֲדָמָה› fact holds: Noach-man-of-the-ground
m.fact("noach_ish_ha_adamah")
# ‹וַיִּטַּע כָּרֶם› event: plant — agent Noach; theme kerem
m.event("plant", agent="noach", themes=["kerem"])
# ‹כָּרֶם› the world gains: kerem
m.install("kerem")

# -------------------------- Gen.9.21 · THE_WINE_AND_THE_SELF_UNCOVERING ----
# וַיֵּשְׁתְּ מִן־הַיַּיִן וַיִּשְׁכָּר וַיִּתְגַּל בְּתוֹךְ אָהֳלֹה
# "And he drank of the wine, and was drunken; and he was uncovered within
# his tent."
m.step("Gen.9.21")
# ‹וַיֵּשְׁתְּ מִן־הַיַּיִן› event: drink — agent Noach; theme from-the-wine
m.event("drink", agent="noach", themes=["min_ha_yayin"])
# ‹וַיִּשְׁכָּר› event: become-drunk — agent Noach
m.event("become_drunk", agent="noach")
# ‹וַיִּתְגַּל בְּתוֹךְ אָהֳלֹה› event: uncover-self — agent Noach; theme
# in-inside-aholoh
m.event("uncover_self", agent="noach", themes=["be_tokh_aholoh"])

# -------------------------- Gen.9.22 · THE_SEEING_AND_THE_TELLING ----------
# וַיַּרְא חָם אֲבִי כְנַעַן אֵת עֶרְוַת אָבִיו וַיַּגֵּד לִשְׁנֵי־אֶחָיו
# בַּחוּץ
# "And Ham, the father of Canaan, saw the nakedness of his father, and told
# his two brethren without."
m.step("Gen.9.22")
# ‹וַיַּרְא חָם אֲבִי כְנַעַן אֵת עֶרְוַת אָבִיו› event: see — agent Ham;
# theme nakedness-of-aviv
m.event("see", agent="cham", themes=["ervat_aviv"])
# ‹וַיַּגֵּד לִשְׁנֵי־אֶחָיו בַּחוּץ› event: tell — agent Ham; theme to-me-
# shnei-echav
m.event("tell", agent="cham", themes=["li_shnei_echav"])

# -------------------------- Gen.9.23 · THE_BACKWARD_COVERING ---------------
# וַיִּקַּח שֵׁם וָיֶפֶת אֶת־הַשִּׂמְלָה וַיָּשִׂימוּ עַל־שְׁכֶם שְׁנֵיהֶם
# וַיֵּלְכוּ אֲחֹרַנִּית וַיְכַסּוּ אֵת עֶרְוַת אֲבִיהֶם וּפְנֵיהֶם
# אֲחֹרַנִּית וְעֶרְוַת אֲבִיהֶם לֹא רָאוּ
# "And Shem and Japheth took a garment, and laid it upon both their
# shoulders, and went backward, and covered the nakedness of their father;
# and their faces were backward, and they saw not their father's nakedness."
m.step("Gen.9.23")
# ‹וַיִּקַּח שֵׁם וָיֶפֶת אֶת־הַשִּׂמְלָה› event: take — agent Shem-and-
# Yefet; theme the-simlah
m.event("take", agent="shem_va_yefet", themes=["ha_simlah"])
# ‹וַיָּשִׂימוּ עַל־שְׁכֶם שְׁנֵיהֶם› event: set — agent Shem-and-Yefet;
# theme over-shoulder-of-both-of-them
m.event("set", agent="shem_va_yefet", themes=["al_shekhem_shneihem"])
# ‹וַיֵּלְכוּ אֲחֹרַנִּית› event: walk-backward — agent Shem-and-Yefet
m.event("walk_backward", agent="shem_va_yefet")
# ‹וַיְכַסּוּ אֵת עֶרְוַת אֲבִיהֶם› event: cover — agent Shem-and-Yefet;
# theme nakedness-of-avihem
m.event("cover", agent="shem_va_yefet", themes=["ervat_avihem"])
# ‹וּפְנֵיהֶם אֲחֹרַנִּית וְעֶרְוַת אֲבִיהֶם לֹא רָאוּ› fact holds: and-
# nakedness-of-avihem-not-they-saw
m.fact("ve_ervat_avihem_lo_rau")

# -------------------------- Gen.9.24 · THE_AWAKENING_AND_THE_KNOWING -------
# וַיִּיקֶץ נֹחַ מִיֵּינוֹ וַיֵּדַע אֵת אֲשֶׁר־עָשָׂה־לוֹ בְּנוֹ הַקָּטָן
# "And Noah awoke from his wine, and knew what his youngest son had done
# unto him."
m.step("Gen.9.24")
# ‹וַיִּיקֶץ נֹחַ מִיֵּינוֹ› event: awake — agent Noach
m.event("awake", agent="noach")
# ‹וַיֵּדַע אֵת אֲשֶׁר־עָשָׂה־לוֹ בְּנוֹ הַקָּטָן› event: know — agent
# Noach; theme that-which-make-not-beno-the-small
m.event("know", agent="noach", themes=["asher_asah_lo_beno_ha_qatan"])

# -------------------------- Gen.9.25 · THE_FIRST_HUMAN_CURSE ---------------
# וַיֹּאמֶר אָרוּר כְּנָעַן עֶבֶד עֲבָדִים יִהְיֶה לְאֶחָיו
# "And he said: 'Cursed be Canaan; a servant of servants shall he be unto
# his brethren.'"
m.step("Gen.9.25")
# ‹וַיֹּאמֶר אָרוּר כְּנָעַן› event: speak — agent Noach; theme cursed-
# Canaan
m.event("speak", agent="noach", themes=["arur_kenaan"])
# ‹אָרוּר כְּנָעַן› role assigned: Canaan -> cursed
m.assign("kenaan", "arur")
# ‹עֶבֶד עֲבָדִים יִהְיֶה לְאֶחָיו› fact holds: slave-of-slaves-yihyeh-to-
# echav(Canaan)
m.fact("eved_avadim_yihyeh_le_echav(kenaan)")

# -------------------------- Gen.9.26 · THE_FIRST_HUMAN_BLESSING ------------
# וַיֹּאמֶר בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם וִיהִי כְנַעַן עֶבֶד לָמוֹ
# "And he said: 'Blessed be the LORD, the God of Shem; and let Canaan be
# their servant.'"
m.step("Gen.9.26")
# ‹וַיֹּאמֶר בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם› event: speak — agent Noach;
# theme blessed-yhwh-elohei-Shem
m.event("speak", agent="noach", themes=["barukh_yhwh_elohei_shem"])
# ‹בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם› blessing: Noach blesses yhwh-elohei-Shem
m.bless("noach", "yhwh_elohei_shem")
# ‹וִיהִי כְנַעַן עֶבֶד לָמוֹ› Noach speaks a demand — LET: yehi(Canaan,
# slave-of-lamo)
m.declare("noach", "LET",
          "yehi(kenaan, eved_lamo)")

# -------------------------- Gen.9.27 · THE_ENLARGEMENT_AND_THE_DWELLING ----
# יַפְתְּ אֱלֹהִים לְיֶפֶת וְיִשְׁכֹּן בְּאָהֳלֵי־שֵׁם וִיהִי כְנַעַן עֶבֶד
# לָמוֹ
# "God enlarge Japheth, and he shall dwell in the tents of Shem; and let
# Canaan be their servant."
m.step("Gen.9.27")
# ‹יַפְתְּ אֱלֹהִים לְיֶפֶת› Noach speaks a demand — LET: may-He-
# enlarge(God, to-Yefet)
m.declare("noach", "LET",
          "yaft(elohim, le_yefet)")
# ‹וְיִשְׁכֹּן בְּאָהֳלֵי־שֵׁם› Noach speaks a demand — LET: may-he-
# dwell(in-aholei-Shem)
m.declare("noach", "LET",
          "yishkon(be_aholei_shem)")
# ‹וִיהִי כְנַעַן עֶבֶד לָמוֹ› Noach speaks a demand — LET: yehi(Canaan,
# slave-of-lamo)
m.declare("noach", "LET",
          "yehi(kenaan, eved_lamo)")

# -------------------------- Gen.9.28 · THE_YEARS_AFTER_THE_DELUGE ----------
# וַיְחִי־נֹחַ אַחַר הַמַּבּוּל שְׁלֹשׁ מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה
# "And Noah lived after the flood three hundred and fifty years."
m.step("Gen.9.28")
# ‹וַיְחִי־נֹחַ אַחַר הַמַּבּוּל שְׁלֹשׁ מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה›
# fact holds: and-he-lived-Noach-after-the-deluge-350-year
m.fact("va_yechi_noach_achar_ha_mabul_350_shanah")

# -------------------------- Gen.9.29 · THE_LEDGER_ROW_CLOSES ---------------
# וַיִּהְיוּ כָּל־יְמֵי־נֹחַ תְּשַׁע מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה
# וַיָּמֹת
# "And all the days of Noah were nine hundred and fifty years; and he died."
m.step("Gen.9.29")
# ‹וַיִּהְיוּ כָּל־יְמֵי־נֹחַ תְּשַׁע מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה›
# fact holds: all-days-of-Noach-950-year
m.fact("kol_yemei_noach_950_shanah")
# ‹וַיָּמֹת› event: die — agent Noach
m.event("die", agent="noach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'kerem'}
    assert m.presupposed_set() == {'tevah', 'noach', 'kenaan'}
    assert m.REGISTRY["names"] == {'kenaan': 'arur'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['yehi(kenaan, eved_lamo)', 'yaft(elohim, le_yefet)', 'yishkon(be_aholei_shem)', 'yehi(kenaan, eved_lamo)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['bnei_noach_ha_yotzim_min_ha_tevah_shem_cham_va_yefet', 'cham_hu_avi_khenaan', 'shelosha_eleh_bnei_noach', 'u_me_eleh_naftzah_khol_ha_aretz', 'noach_ish_ha_adamah', 've_ervat_avihem_lo_rau', 'eved_avadim_yihyeh_le_echav(kenaan)', 'va_yechi_noach_achar_ha_mabul_350_shanah', 'kol_yemei_noach_950_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 22
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_24_nations_table
###############################################################################
# =============================================================================
# gen_24_nations_table — 10:1-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_24_nations_table.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The nations table: of these the nations divided after the flood (10:1-32)"""
from machine import Machine

m = Machine("gen_24_nations_table")

# -------------------------- Gen.10.1 · THE_FOURTH_TOLEDOT_HEADING ----------
# וְאֵלֶּה תּוֹלְדֹת בְּנֵי־נֹחַ שֵׁם חָם וָיָפֶת וַיִּוָּלְדוּ לָהֶם
# בָּנִים אַחַר הַמַּבּוּל
# "Now these are the generations of the sons of Noah: Shem, Ham, and
# Japheth; and unto them were sons born after the flood."
m.step("Gen.10.1")
# ‹וְאֵלֶּה תּוֹלְדֹת בְּנֵי־נֹחַ שֵׁם חָם וָיָפֶת› section generations-
# sons-of-Noach: Sem, Ham, Japheth
m.section("toledot_bnei_noach", "shem", "cham", "yefet")
# ‹וַיִּוָּלְדוּ לָהֶם בָּנִים אַחַר הַמַּבּוּל› event: in-born — theme
# sons-of-after-the-deluge
m.event("be_born", themes=["banim_achar_ha_mabul"])
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")

# -------------------------- Gen.10.2-5 · YEFET_ROWS_AND_THE_ANOMALOUS_CLOSE -
# בְּנֵי יֶפֶת גֹּמֶר וּמָגוֹג וּמָדַי וְיָוָן וְתֻבָל וּמֶשֶׁךְ וְתִירָס …
# מֵאֵלֶּה נִפְרְדוּ אִיֵּי הַגּוֹיִם בְּאַרְצֹתָם אִישׁ לִלְשֹׁנוֹ
# לְמִשְׁפְּחֹתָם בְּגוֹיֵהֶם
# "The sons of Japheth: Gomer, Magog, Madai, Javan, Tubal, Meshech, Tiras —
# and the sons of Gomer and of Javan — of these were the isles of the
# nations divided in their lands, every one after his tongue, after their
# families, in their nations."
m.step("Gen.10.2-5")
# ‹בְּנֵי יֶפֶת גֹּמֶר וּמָגוֹג וּמָדַי וְיָוָן וְתֻבָל וּמֶשֶׁךְ וְתִירָס›
# fact holds: sons-of-Japheth-Gomer-and-Magog-and-Madai-and-Javan
m.fact("bnei_yefet_gomer_u_magog_u_maday_ve_yavan")
# ‹מֵאֵלֶּה נִפְרְדוּ אִיֵּי הַגּוֹיִם … אִישׁ לִלְשֹׁנוֹ› fact holds: and-
# from-these-nifredu-iyei-the-nations-in-artzotam; each-to-me-leshono-to-
# mishpechotam-in-goyehem
m.fact("u_me_eleh_nifredu_iyei_ha_goyim_be_artzotam",
       "ish_li_leshono_le_mishpechotam_be_goyehem")

# -------------------------- Gen.10.6-7 · HAM_ROWS_KUSH_TO_DEDAN ------------
# וּבְנֵי חָם כּוּשׁ וּמִצְרַיִם וּפוּט וּכְנָעַן וּבְנֵי כוּשׁ סְבָא
# וַחֲוִילָה וְסַבְתָּה וְרַעְמָה וְסַבְתְּכָא וּבְנֵי רַעְמָה שְׁבָא
# וּדְדָן
# "And the sons of Ham: Cush, and Mizraim, and Put, and Canaan. And the sons
# of Cush: Seba, and Havilah, and Sabtah, and Raamah, and Sabteca; and the
# sons of Raamah: Sheba, and Dedan."
m.step("Gen.10.6-7")
# ‹וּבְנֵי חָם כּוּשׁ וּמִצְרַיִם וּפוּט וּכְנָעַן …› fact holds: sons-of-
# Ham-Chush-and-Egypt-and-Phut-and-Canaan; sons-of-Chush-Seba-and-Havilah-
# and-vnei-ramah
m.fact("bnei_cham_kush_u_mitzrayim_u_fut_u_khenaan",
       "bnei_khush_seva_va_chavilah_u_vnei_ramah")

# -------------------------- Gen.10.8-9 · NIMROD_AND_THE_PROVERB ------------
# וְכוּשׁ יָלַד אֶת־נִמְרֹד הוּא הֵחֵל לִהְיוֹת גִּבֹּר בָּאָרֶץ הוּא־הָיָה
# גִבֹּר־צַיִד לִפְנֵי יְהוָה עַל־כֵּן יֵאָמַר כְּנִמְרֹד גִּבּוֹר צַיִד
# לִפְנֵי יְהוָה
# "And Cush begot Nimrod; he began to be a mighty one in the earth. He was a
# mighty hunter before the LORD; wherefore it is said: 'Like Nimrod a mighty
# hunter before the LORD.'"
m.step("Gen.10.8-9")
# ‹וְכוּשׁ יָלַד אֶת־נִמְרֹד› event: beget — agent Chush; theme Nimrod
m.event("beget", agent="kush", themes=["nimrod"])
# ‹הוּא הֵחֵל לִהְיוֹת גִּבֹּר בָּאָרֶץ … גִבֹּר־צַיִד לִפְנֵי יְהוָה› fact
# holds: he-began-lihyot-gibbor-in-the-earth; gibbor-hunter-lifnei-yhwh
m.fact("hu_hechel_lihyot_gibbor_ba_aretz",
       "gibbor_tzayid_lifnei_yhwh")
# ‹עַל־כֵּן יֵאָמַר כְּנִמְרֹד גִּבּוֹר צַיִד לִפְנֵי יְהוָה› pattern
# recorded: like-Nimrod-gibbor-hunter-lifnei-yhwh
m.pattern("ke_nimrod_gibbor_tzayid_lifnei_yhwh")

# -------------------------- Gen.10.10-12 · THE_KINGDOM_AND_THE_FOUR_CITIES -
# וַתְּהִי רֵאשִׁית מַמְלַכְתּוֹ בָּבֶל וְאֶרֶךְ וְאַכַּד וְכַלְנֵה בְּאֶרֶץ
# שִׁנְעָר מִן־הָאָרֶץ הַהִוא יָצָא אַשּׁוּר וַיִּבֶן אֶת־נִינְוֵה
# וְאֶת־רְחֹבֹת עִיר וְאֶת־כָּלַח וְאֶת־רֶסֶן בֵּין נִינְוֵה וּבֵין כָּלַח
# הִוא הָעִיר הַגְּדֹלָה
# "And the beginning of his kingdom was Babel, and Erech, and Accad, and
# Calneh, in the land of Shinar. Out of that land went forth Asshur, and
# builded Nineveh, and Rehoboth-ir, and Calah, and Resen between Nineveh and
# Calah — the same is the great city."
m.step("Gen.10.10-12")
# ‹וַתְּהִי רֵאשִׁית מַמְלַכְתּוֹ בָּבֶל … בְּאֶרֶץ שִׁנְעָר› fact holds:
# beginning-of-mamlakhto-Babel-in-land-Shinar; from-the-earth-the-hi-went-
# out-Ashur
m.fact("reshit_mamlakhto_bavel_be_eretz_shinar",
       "min_ha_aretz_ha_hi_yatza_ashur")
# ‹וַיִּבֶן אֶת־נִינְוֵה וְאֶת־רְחֹבֹת עִיר וְאֶת־כָּלַח וְאֶת־רֶסֶן› event:
# build — theme ninveh, Rehoboth-city, Calah, Resen
m.event("build", themes=["ninveh", "rechovot_ir", "kalach", "resen"])
# ‹נִינְוֵה וְרְחֹבֹת עִיר וְכָלַח וְרֶסֶן› the world gains: ninveh,
# Rehoboth-city, Calah, Resen
m.install("ninveh", "rechovot_ir", "kalach", "resen")
# ‹הִוא הָעִיר הַגְּדֹלָה› fact holds: hi-the-city-the-gedolah
m.fact("hi_ha_ir_ha_gedolah")

# -------------------------- Gen.10.13-14 · MITZRAYIM_ROWS_AND_THE_PHILISTINE_NOTE -
# וּמִצְרַיִם יָלַד אֶת־לוּדִים וְאֶת־עֲנָמִים וְאֶת־לְהָבִים
# וְאֶת־נַפְתֻּחִים וְאֶת־פַּתְרֻסִים וְאֶת־כַּסְלֻחִים אֲשֶׁר יָצְאוּ
# מִשָּׁם פְּלִשְׁתִּים וְאֶת־כַּפְתֹּרִים
# "And Mizraim begot Ludim, and Anamim, and Lehabim, and Naphtuhim, and
# Pathrusim, and Casluhim — whence went forth the Philistines — and
# Caphtorim."
m.step("Gen.10.13-14")
# ‹וּמִצְרַיִם יָלַד אֶת־לוּדִים …› event: beget — agent Egypt; theme seven-
# amamim
m.event("beget", agent="mitzrayim", themes=["shivat_amamim"])
# ‹אֲשֶׁר יָצְאוּ מִשָּׁם פְּלִשְׁתִּים› fact holds: who-bring-forth-from-
# there-Philistines
m.fact("asher_yatzu_mi_sham_pelishtim")

# -------------------------- Gen.10.15-19 · CANAAN_ROWS_SPREAD_AND_BORDER ---
# וּכְנַעַן יָלַד אֶת־צִידֹן בְּכֹרוֹ וְאֶת־חֵת … וְאַחַר נָפֹצוּ
# מִשְׁפְּחוֹת הַכְּנַעֲנִי וַיְהִי גְּבוּל הַכְּנַעֲנִי מִצִּידֹן …
# עַד־לָשַׁע
# "And Canaan begot Zidon his firstborn, and Heth; and the Jebusite, and the
# Amorite, and the Girgashite; and the Hivite, and the Arkite, and the
# Sinite; and the Arvadite, and the Zemarite, and the Hamathite; and
# afterward were the families of the Canaanite spread abroad. And the border
# of the Canaanite was from Zidon, as thou goest toward Gerar, unto Gaza; as
# thou goest toward Sodom and Gomorrah and Admah and Zeboiim, unto Lasha."
m.step("Gen.10.15-19")
# ‹וּכְנַעַן יָלַד אֶת־צִידֹן בְּכֹרוֹ וְאֶת־חֵת› event: beget — agent
# kenaan; theme Sidon-bekhoro, Heth
m.event("beget", agent="kenaan", themes=["tzidon_bekhoro", "chet"])
# ‹וְאֶת־הַיְבוּסִי וְאֶת־הָאֱמֹרִי … וְאַחַר נָפֹצוּ מִשְׁפְּחוֹת
# הַכְּנַעֲנִי› fact holds: these-the-Canaanite-asarah-amamim; and-after-
# were-spread-mishpechot-the-Canaanite
m.fact("eleh_ha_kenaani_asarah_amamim",
       "ve_achar_nafotzu_mishpechot_ha_kenaani")
# ‹וַיְהִי גְּבוּל הַכְּנַעֲנִי מִצִּידֹן … עַד־לָשַׁע› fact holds: border-
# of-the-Canaanite-from-Sidon-until-azah-until-Lasha
m.fact("gevul_ha_kenaani_mi_tzidon_ad_azah_ad_lasha")

# -------------------------- Gen.10.20 · HAM_CLOSE --------------------------
# אֵלֶּה בְנֵי־חָם לְמִשְׁפְּחֹתָם לִלְשֹׁנֹתָם בְּאַרְצֹתָם בְּגוֹיֵהֶם
# "These are the sons of Ham, after their families, after their tongues, in
# their lands, in their nations."
m.step("Gen.10.20")
# ‹אֵלֶּה בְנֵי־חָם … בְּגוֹיֵהֶם› fact holds: these-vnei-Ham-to-
# mishpechotam-to-me-leshonotam-in-artzotam-in-goyehem
m.fact("eleh_vnei_cham_le_mishpechotam_li_leshonotam_be_artzotam_be_goyehem")

# -------------------------- Gen.10.21-24 · SHEM_OPENER_AND_ROWS ------------
# וּלְשֵׁם יֻלַּד גַּם־הוּא אֲבִי כָּל־בְּנֵי־עֵבֶר אֲחִי יֶפֶת הַגָּדוֹל
# בְּנֵי שֵׁם עֵילָם וְאַשּׁוּר וְאַרְפַּכְשַׁד וְלוּד וַאֲרָם …
# וְאַרְפַּכְשַׁד יָלַד אֶת־שָׁלַח וְשֶׁלַח יָלַד אֶת־עֵבֶר
# "And unto Shem, the father of all the children of Eber, the elder brother
# of Japheth, to him also were children born. The sons of Shem: Elam, and
# Asshur, and Arpachshad, and Lud, and Aram. And the sons of Aram: Uz, and
# Hul, and Gether, and Mash. And Arpachshad begot Shelah; and Shelah begot
# Eber."
m.step("Gen.10.21-24")
# ‹וּלְשֵׁם יֻלַּד גַּם־הוּא› event: in-born — theme to-Sem-also-he
m.event("be_born", themes=["le_shem_gam_hu"])
# ‹אֲבִי כָּל־בְּנֵי־עֵבֶר אֲחִי יֶפֶת הַגָּדוֹל … בְּנֵי שֵׁם עֵילָם
# וְאַשּׁוּר› fact holds: father-of-all-sons-of-Ever-brother-Japheth-the-
# elder; sons-of-Sem-eilam-and-Ashur-and-Arphaxad
m.fact("avi_kol_bnei_ever_achi_yefet_ha_gadol",
       "bnei_shem_eilam_ve_ashur_ve_arpakhshad")
# ‹וְאַרְפַּכְשַׁד יָלַד אֶת־שָׁלַח› event: beget — agent Arphaxad; theme
# Salah
m.event("beget", agent="arpakhshad", themes=["shelach"])
# ‹וְשֶׁלַח יָלַד אֶת־עֵבֶר› event: beget — agent Salah; theme Ever
m.event("beget", agent="shelach", themes=["ever"])

# -------------------------- Gen.10.25-29 · PELEG_AND_THE_YOKTAN_ROWS -------
# וּלְעֵבֶר יֻלַּד שְׁנֵי בָנִים שֵׁם הָאֶחָד פֶּלֶג כִּי בְיָמָיו נִפְלְגָה
# הָאָרֶץ וְשֵׁם אָחִיו יָקְטָן וְיָקְטָן יָלַד … כָּל־אֵלֶּה בְּנֵי יָקְטָן
# "And unto Eber were born two sons; the name of the one was Peleg; for in
# his days was the earth divided; and his brother's name was Joktan. And
# Joktan begot Almodad, and Sheleph, and Hazarmaveth, and Jerah; and
# Hadoram, and Uzal, and Diklah; and Obal, and Abimael, and Sheba; and
# Ophir, and Havilah, and Jobab; all these were the sons of Joktan."
m.step("Gen.10.25-29")
# ‹וּלְעֵבֶר יֻלַּד שְׁנֵי בָנִים› event: in-born — theme to-Ever-shnei-
# sons-of
m.event("be_born", themes=["le_ever_shnei_vanim"])
# ‹שֵׁם הָאֶחָד פֶּלֶג כִּי בְיָמָיו נִפְלְגָה הָאָרֶץ› fact holds: Sem-the-
# one-Peleg-that-and-his-days-niflegah-the-earth; and-Sem-his-brother-yoktan
m.fact("shem_ha_echad_peleg_ki_ve_yamav_niflegah_ha_aretz",
       "ve_shem_achiv_yoktan")
# ‹וְיָקְטָן יָלַד אֶת־אַלְמוֹדָד … וְאֶת־יוֹבָב› event: beget — agent
# yoktan; theme shloshah-asar-sons-of
m.event("beget", agent="yoktan", themes=["shloshah_asar_banim"])
# ‹כָּל־אֵלֶּה בְּנֵי יָקְטָן› fact holds: all-these-sons-of-yoktan
m.fact("kol_eleh_bnei_yoktan")

# -------------------------- Gen.10.30-31 · THE_DWELLING_AND_SHEM_CLOSE -----
# וַיְהִי מוֹשָׁבָם מִמֵּשָׁא בֹּאֲכָה סְפָרָה הַר הַקֶּדֶם אֵלֶּה
# בְנֵי־שֵׁם לְמִשְׁפְּחֹתָם לִלְשֹׁנֹתָם בְּאַרְצֹתָם לְגוֹיֵהֶם
# "And their dwelling was from Mesha, as thou goest toward Sephar, unto the
# mountain of the east. These are the sons of Shem, after their families,
# after their tongues, in their lands, after their nations."
m.step("Gen.10.30-31")
# ‹וַיְהִי מוֹשָׁבָם מִמֵּשָׁא בֹּאֲכָה סְפָרָה הַר הַקֶּדֶם› fact holds:
# moshavam-from-Mesha-mountain-the-east
m.fact("moshavam_mi_mesha_har_ha_qedem")
# ‹אֵלֶּה בְנֵי־שֵׁם … לְגוֹיֵהֶם› fact holds: these-vnei-Sem-to-
# mishpechotam-to-me-leshonotam-in-artzotam-to-goyehem
m.fact("eleh_vnei_shem_le_mishpechotam_li_leshonotam_be_artzotam_le_goyehem")

# -------------------------- Gen.10.32 · THE_GRAND_CLOSE_SEALS_THE_INCLUSIO -
# אֵלֶּה מִשְׁפְּחֹת בְּנֵי־נֹחַ לְתוֹלְדֹתָם בְּגוֹיֵהֶם וּמֵאֵלֶּה
# נִפְרְדוּ הַגּוֹיִם בָּאָרֶץ אַחַר הַמַּבּוּל
# "These are the families of the sons of Noah, after their generations, in
# their nations; and of these were the nations divided in the earth after
# the flood."
m.step("Gen.10.32")
# ‹אֵלֶּה מִשְׁפְּחֹת בְּנֵי־נֹחַ … וּמֵאֵלֶּה נִפְרְדוּ הַגּוֹיִם בָּאָרֶץ
# אַחַר הַמַּבּוּל› fact holds: these-mishpechot-sons-of-Noach-to-toledotam;
# and-from-these-nifredu-the-nations-in-the-earth-after-the-deluge
m.fact("eleh_mishpechot_bnei_noach_le_toledotam",
       "u_me_eleh_nifredu_ha_goyim_ba_aretz_achar_ha_mabul")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'resen', 'rechovot_ir', 'kalach', 'ninveh'}
    assert m.presupposed_set() == {'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['bnei_yefet_gomer_u_magog_u_maday_ve_yavan', 'u_me_eleh_nifredu_iyei_ha_goyim_be_artzotam', 'ish_li_leshono_le_mishpechotam_be_goyehem', 'bnei_cham_kush_u_mitzrayim_u_fut_u_khenaan', 'bnei_khush_seva_va_chavilah_u_vnei_ramah', 'hu_hechel_lihyot_gibbor_ba_aretz', 'gibbor_tzayid_lifnei_yhwh', 'pattern: ke_nimrod_gibbor_tzayid_lifnei_yhwh', 'reshit_mamlakhto_bavel_be_eretz_shinar', 'min_ha_aretz_ha_hi_yatza_ashur', 'hi_ha_ir_ha_gedolah', 'asher_yatzu_mi_sham_pelishtim', 'eleh_ha_kenaani_asarah_amamim', 've_achar_nafotzu_mishpechot_ha_kenaani', 'gevul_ha_kenaani_mi_tzidon_ad_azah_ad_lasha', 'eleh_vnei_cham_le_mishpechotam_li_leshonotam_be_artzotam_be_goyehem', 'avi_kol_bnei_ever_achi_yefet_ha_gadol', 'bnei_shem_eilam_ve_ashur_ve_arpakhshad', 'shem_ha_echad_peleg_ki_ve_yamav_niflegah_ha_aretz', 've_shem_achiv_yoktan', 'kol_eleh_bnei_yoktan', 'moshavam_mi_mesha_har_ha_qedem', 'eleh_vnei_shem_le_mishpechotam_li_leshonotam_be_artzotam_le_goyehem', 'eleh_mishpechot_bnei_noach_le_toledotam', 'u_me_eleh_nifredu_ha_goyim_ba_aretz_achar_ha_mabul'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 12
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_25_babel
###############################################################################
# =============================================================================
# gen_25_babel — 11:1-9
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_25_babel.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Babel: come, let us build — come, let Us go down (11:1-9)"""
from machine import Machine

m = Machine("gen_25_babel")

# -------------------------- Gen.11.1 · ONE_LIP_ONE_WORDS -------------------
# וַיְהִי כָל־הָאָרֶץ שָׂפָה אֶחָת וּדְבָרִים אֲחָדִים
# "And the whole earth was of one language and of one speech."
m.step("Gen.11.1")
# ‹כָל־הָאָרֶץ שָׂפָה אֶחָת וּדְבָרִים אֲחָדִים› fact holds: all-the-earth-
# safah-one-and-words-one
m.fact("kol_ha_aretz_safah_echat_u_devarim_achadim")

# -------------------------- Gen.11.2 · THE_JOURNEY_EAST_TO_SHINAR ----------
# וַיְהִי בְּנָסְעָם מִקֶּדֶם וַיִּמְצְאוּ בִקְעָה בְּאֶרֶץ שִׁנְעָר
# וַיֵּשְׁבוּ שָׁם
# "And it came to pass, as they journeyed east, that they found a plain in
# the land of Shinar; and they dwelt there."
m.step("Gen.11.2")
# ‹בְּנָסְעָם מִקֶּדֶם› fact holds: in-nasam-from-east
m.fact("be_nasam_mi_qedem")
# ‹וַיִּמְצְאוּ בִקְעָה בְּאֶרֶץ שִׁנְעָר› event: find — theme viqah-in-
# earth-Shinar
m.event("find", themes=["viqah_be_eretz_shinar"])
# ‹וַיֵּשְׁבוּ שָׁם› event: settle — theme there
m.event("settle", themes=["sham"])
# reads without prior install (flag, not fix): Shinar
m.presupposed("shinar")

# -------------------------- Gen.11.3 · COME_LET_US_BRICK -------------------
# וַיֹּאמְרוּ אִישׁ אֶל־רֵעֵהוּ הָבָה נִלְבְּנָה לְבֵנִים וְנִשְׂרְפָה
# לִשְׂרֵפָה וַתְּהִי לָהֶם הַלְּבֵנָה לְאָבֶן וְהַחֵמָר הָיָה לָהֶם לַחֹמֶר
# "And they said one to another: 'Come, let us make brick, and burn them
# thoroughly.' And they had brick for stone, and slime had they for mortar."
m.step("Gen.11.3")
# ‹וַיֹּאמְרוּ אִישׁ אֶל־רֵעֵהוּ הָבָה› event: speak — agent man-to-reehu
m.event("speak", agent="ish_el_reehu")
# ‹נִלְבְּנָה לְבֵנִים› man-to-reehu speaks a demand — CMD-US:
# nilbenah(bricks)
m.declare("ish_el_reehu", "CMD-US",
          "nilbenah(levenim)")
# ‹וְנִשְׂרְפָה לִשְׂרֵפָה› man-to-reehu speaks a demand — CMD-US:
# nisrefah(to-me-serefah)
m.declare("ish_el_reehu", "CMD-US",
          "nisrefah(li_serefah)")
# ‹וַתְּהִי לָהֶם הַלְּבֵנָה לְאָבֶן וְהַחֵמָר הָיָה לָהֶם לַחֹמֶר› fact
# holds: and-be-to-them-the-levenah-to-stone; and-the-bitumen-was-to-them-
# to-mortar
m.fact("va_tehi_lahem_ha_levenah_le_aven",
       "ve_ha_chemar_hayah_lahem_la_chomer")

# -------------------------- Gen.11.4 · CITY_TOWER_NAME_AND_FEAR ------------
# וַיֹּאמְרוּ הָבָה נִבְנֶה־לָּנוּ עִיר וּמִגְדָּל וְרֹאשׁוֹ בַשָּׁמַיִם
# וְנַעֲשֶׂה־לָּנוּ שֵׁם פֶּן־נָפוּץ עַל־פְּנֵי כָל־הָאָרֶץ
# "And they said: 'Come, let us build us a city, and a tower, with its top
# in heaven, and let us make us a name; lest we be scattered abroad upon the
# face of the whole earth.'"
m.step("Gen.11.4")
# ‹וַיֹּאמְרוּ הָבָה› event: speak — agent man-to-reehu
m.event("speak", agent="ish_el_reehu")
# ‹נִבְנֶה־לָּנוּ עִיר וּמִגְדָּל וְרֹאשׁוֹ בַשָּׁמַיִם› man-to-reehu speaks
# a demand — CMD-US?: nivneh(a-city-and-a-tower)
m.declare("ish_el_reehu", "CMD-US?",
          "nivneh(ir_u_migdal)")
# ‹וְנַעֲשֶׂה־לָּנוּ שֵׁם› man-to-reehu speaks a demand — CMD-US?:
# naaseh(lanu-a-name)
m.declare("ish_el_reehu", "CMD-US?",
          "naaseh(lanu_shem)")
# ‹וְרֹאשׁוֹ בַשָּׁמַיִם … פֶּן־נָפוּץ עַל־פְּנֵי כָל־הָאָרֶץ› fact holds:
# and-rosho-and-heavens; lest-we-be-scattered-over-face-of-all-the-earth
m.fact("ve_rosho_va_shamayim",
       "pen_nafutz_al_pnei_khol_ha_aretz")

# -------------------------- Gen.11.5 · THE_DESCENT_TO_SEE ------------------
# וַיֵּרֶד יְהוָה לִרְאֹת אֶת־הָעִיר וְאֶת־הַמִּגְדָּל אֲשֶׁר בָּנוּ בְּנֵי
# הָאָדָם
# "And the LORD came down to see the city and the tower, which the children
# of men builded."
m.step("Gen.11.5")
# ‹וַיֵּרֶד יְהוָה לִרְאֹת› event: descend — agent the-LORD; theme lirot-
# obj-marker·et-the-a-city-and-obj-marker·et-the-a-tower
m.event("descend", agent="YHWH", themes=["lirot_et_ha_ir_ve_et_ha_migdal"])
# ‹אֲשֶׁר בָּנוּ בְּנֵי הָאָדָם› fact holds: which-they-built-sons-of-the-
# humankind
m.fact("asher_banu_bnei_ha_adam")

# -------------------------- Gen.11.6 · ONE_PEOPLE_THE_ASSESSMENT -----------
# וַיֹּאמֶר יְהוָה הֵן עַם אֶחָד וְשָׂפָה אַחַת לְכֻלָּם וְזֶה הַחִלָּם
# לַעֲשׂוֹת וְעַתָּה לֹא־יִבָּצֵר מֵהֶם כֹּל אֲשֶׁר יָזְמוּ לַעֲשׂוֹת
# "And the LORD said: 'Behold, they are one people, and they have all one
# language; and this is what they begin to do; and now nothing will be
# withholden from them, which they purpose to do.'"
m.step("Gen.11.6")
# ‹וַיֹּאמֶר יְהוָה הֵן עַם אֶחָד› event: speak — agent the-LORD; theme
# behold-people-one
m.event("speak", agent="YHWH", themes=["hen_am_echad"])
# ‹הֵן עַם אֶחָד … וְזֶה הַחִלָּם לַעֲשׂוֹת … לֹא־יִבָּצֵר מֵהֶם› fact
# holds: behold-people-one-and-safah-one-to-khulam; and-this-hachillam-to-
# do; not-will-be-withheld-mehem-all-which-they-plan
m.fact("hen_am_echad_ve_safah_achat_le_khulam",
       "ve_zeh_hachillam_la_asot",
       "lo_yibatzer_mehem_kol_asher_yazmu")

# -------------------------- Gen.11.7 · THE_MIRRORED_COUNTER_COUNCIL --------
# הָבָה נֵרְדָה וְנָבְלָה שָׁם שְׂפָתָם אֲשֶׁר לֹא יִשְׁמְעוּ אִישׁ שְׂפַת
# רֵעֵהוּ
# "'Come, let us go down, and there confound their language, that they may
# not understand one another's speech.'"
m.step("Gen.11.7")
# ‹הָבָה נֵרְדָה› the-LORD speaks a demand — CMD-US: nerdah(there)
m.declare("YHWH", "CMD-US",
          "nerdah(sham)")
# ‹וְנָבְלָה שָׁם שְׂפָתָם› the-LORD speaks a demand — CMD-US: navlah(there-
# sefatam)
m.declare("YHWH", "CMD-US",
          "navlah(sham_sefatam)")

# -------------------------- Gen.11.8 · THE_SCATTER_AND_THE_CEASING ---------
# וַיָּפֶץ יְהוָה אֹתָם מִשָּׁם עַל־פְּנֵי כָל־הָאָרֶץ וַיַּחְדְּלוּ לִבְנֹת
# הָעִיר
# "So the LORD scattered them abroad from thence upon the face of all the
# earth; and they left off to build the city."
m.step("Gen.11.8")
# ‹וַיָּפֶץ יְהוָה אֹתָם מִשָּׁם› event: scatter — agent the-LORD; theme
# from-there-over-face-of-all-the-earth
m.event("scatter", agent="YHWH", themes=["mi_sham_al_pnei_khol_ha_aretz"])
# ‹וַיַּחְדְּלוּ לִבְנֹת הָעִיר› fact holds: and-yachdelu-livnot-the-a-city
m.fact("va_yachdelu_livnot_ha_ir")

# -------------------------- Gen.11.9 · THE_NAME_ETIOLOGY_AND_THE_ECHO ------
# עַל־כֵּן קָרָא שְׁמָהּ בָּבֶל כִּי־שָׁם בָּלַל יְהוָה שְׂפַת כָּל־הָאָרֶץ
# וּמִשָּׁם הֱפִיצָם יְהוָה עַל־פְּנֵי כָּל־הָאָרֶץ
# "Therefore was the name of it called Babel; because the LORD did there
# confound the language of all the earth; and from thence did the LORD
# scatter them abroad upon the face of all the earth."
m.step("Gen.11.9")
# ‹כִּי־שָׁם בָּלַל יְהוָה שְׂפַת כָּל־הָאָרֶץ› demand settled (popped from
# the queue): navlah(there-sefatam)
m.result("navlah(sham_sefatam)", tmark="t2")
# ‹עַל־כֵּן קָרָא שְׁמָהּ בָּבֶל› pattern recorded: over-so-kara-shemah-
# Babel
m.pattern("al_ken_kara_shemah_bavel")
# ‹כִּי־שָׁם בָּלַל … וּמִשָּׁם הֱפִיצָם› fact holds: for-there-He-confused-
# yhwh-lip-of-all-the-earth; and-from-there-hefitzam-yhwh
m.fact("ki_sham_balal_yhwh_sefat_kol_ha_aretz",
       "u_mi_sham_hefitzam_yhwh")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'shinar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['nilbenah(levenim)', 'nisrefah(li_serefah)', 'nivneh(ir_u_migdal)', 'naaseh(lanu_shem)', 'nerdah(sham)']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['kol_ha_aretz_safah_echat_u_devarim_achadim', 'be_nasam_mi_qedem', 'va_tehi_lahem_ha_levenah_le_aven', 've_ha_chemar_hayah_lahem_la_chomer', 've_rosho_va_shamayim', 'pen_nafutz_al_pnei_khol_ha_aretz', 'asher_banu_bnei_ha_adam', 'hen_am_echad_ve_safah_achat_le_khulam', 've_zeh_hachillam_la_asot', 'lo_yibatzer_mehem_kol_asher_yazmu', 'va_yachdelu_livnot_ha_ir', 'pattern: al_ken_kara_shemah_bavel', 'ki_sham_balal_yhwh_sefat_kol_ha_aretz', 'u_mi_sham_hefitzam_yhwh'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_26_shem_ledger
###############################################################################
# =============================================================================
# gen_26_shem_ledger — 11:10-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_26_shem_ledger.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The deathless ledger: Shem to Terach, and the two deaths that land (11:10-32)"""
from machine import Machine

m = Machine("gen_26_shem_ledger")

# -------------------------- Gen.11.10-11 · SHEM_HEADER_AND_THE_FIRST_DEATHLESS_ROW -
# אֵלֶּה תּוֹלְדֹת שֵׁם שֵׁם בֶּן־מְאַת שָׁנָה וַיּוֹלֶד אֶת־אַרְפַּכְשָׁד
# שְׁנָתַיִם אַחַר הַמַּבּוּל … וַיּוֹלֶד בָּנִים וּבָנוֹת
# "These are the generations of Shem. Shem was a hundred years old, and
# begot Arpachshad two years after the flood. And Shem lived after he begot
# Arpachshad five hundred years, and begot sons and daughters."
m.step("Gen.11.10-11")
# ‹אֵלֶּה תּוֹלְדֹת שֵׁם› section generations-shem: eleh toldot shem — the
# sixth toledot header labels; installs nothing
m.section("toledot_shem", "eleh toldot shem — the sixth toledot header labels; installs nothing")
# ‹שֵׁם בֶּן־מְאַת שָׁנָה … שְׁנָתַיִם אַחַר הַמַּבּוּל› fact holds: shem-
# ben-meat-year; shenatayim-achar-the-mabul
m.fact("shem_ben_meat_shanah",
       "shenatayim_achar_ha_mabul")
# ‹וַיּוֹלֶד אֶת־אַרְפַּכְשָׁד› event: beget — agent shem; theme arpakhshad
m.event("beget", agent="shem", themes=["arpakhshad"])
# ‹וַיְחִי־שֵׁם אַחֲרֵי הוֹלִידוֹ אֶת־אַרְפַּכְשָׁד חֲמֵשׁ מֵאוֹת שָׁנָה
# וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(shem)
m.fact("banim_u_vanot(shem)")

# -------------------------- Gen.11.12-13 · ARPACHSHAD_ROW_FRONTED_PERFECT --
# וְאַרְפַּכְשַׁד חַי חָמֵשׁ וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שָׁלַח …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Arpachshad lived five and thirty years, and begot Shelah. And
# Arpachshad lived after he begot Shelah four hundred and three years, and
# begot sons and daughters."
m.step("Gen.11.12-13")
# ‹וְאַרְפַּכְשַׁד חַי חָמֵשׁ וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שָׁלַח›
# event: beget — agent arpakhshad; theme shelach
m.event("beget", agent="arpakhshad", themes=["shelach"])
# ‹וַיְחִי אַרְפַּכְשַׁד … שָׁלֹשׁ שָׁנִים וְאַרְבַּע מֵאוֹת שָׁנָה
# וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(arpakhshad)
m.fact("banim_u_vanot(arpakhshad)")

# -------------------------- Gen.11.14-15 · SHELACH_ROW_FRONTED_PERFECT -----
# וְשֶׁלַח חַי שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־עֵבֶר … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Shelah lived thirty years, and begot Eber. And Shelah lived after he
# begot Eber four hundred and three years, and begot sons and daughters."
m.step("Gen.11.14-15")
# ‹וְשֶׁלַח חַי שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־עֵבֶר› event: beget — agent
# shelach; theme ever
m.event("beget", agent="shelach", themes=["ever"])
# ‹וַיְחִי־שֶׁלַח … שָׁלֹשׁ שָׁנִים וְאַרְבַּע מֵאוֹת שָׁנָה וַיּוֹלֶד
# בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(shelach)
m.fact("banim_u_vanot(shelach)")

# -------------------------- Gen.11.16-17 · EVER_ROW_WAYYIQTOL_RESUMES ------
# וַיְחִי־עֵבֶר אַרְבַּע וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־פָּלֶג …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Eber lived four and thirty years, and begot Peleg. And Eber lived
# after he begot Peleg four hundred and thirty years, and begot sons and
# daughters."
m.step("Gen.11.16-17")
# ‹וַיְחִי־עֵבֶר אַרְבַּע וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־פָּלֶג› event:
# beget — agent ever; theme peleg
m.event("beget", agent="ever", themes=["peleg"])
# ‹וַיְחִי־עֵבֶר אַחֲרֵי הוֹלִידוֹ אֶת־פֶּלֶג שְׁלֹשִׁים שָׁנָה וְאַרְבַּע
# מֵאוֹת שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-
# vanot(ever)
m.fact("banim_u_vanot(ever)")

# -------------------------- Gen.11.18-19 · PELEG_ROW_CAREER_CLOSES ---------
# וַיְחִי־פֶלֶג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־רְעוּ … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Peleg lived thirty years, and begot Reu. And Peleg lived after he
# begot Reu two hundred and nine years, and begot sons and daughters."
m.step("Gen.11.18-19")
# ‹וַיְחִי־פֶלֶג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־רְעוּ› event: beget — agent
# peleg; theme reu
m.event("beget", agent="peleg", themes=["reu"])
# ‹וַיְחִי־פֶלֶג אַחֲרֵי הוֹלִידוֹ אֶת־רְעוּ תֵּשַׁע שָׁנִים וּמָאתַיִם
# שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(peleg)
m.fact("banim_u_vanot(peleg)")

# -------------------------- Gen.11.20-21 · REU_ROW_WHOLE_CAREER_IN_SPAN ----
# וַיְחִי רְעוּ שְׁתַּיִם וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שְׂרוּג …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Reu lived two and thirty years, and begot Serug. And Reu lived after
# he begot Serug two hundred and seven years, and begot sons and daughters."
m.step("Gen.11.20-21")
# ‹וַיְחִי רְעוּ שְׁתַּיִם וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שְׂרוּג› event:
# beget — agent reu; theme serug
m.event("beget", agent="reu", themes=["serug"])
# ‹וַיְחִי רְעוּ אַחֲרֵי הוֹלִידוֹ אֶת־שְׂרוּג שֶׁבַע שָׁנִים וּמָאתַיִם
# שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(reu)
m.fact("banim_u_vanot(reu)")

# -------------------------- Gen.11.22-23 · SERUG_ROW_BEGETS_THE_FIRST_NACHOR -
# וַיְחִי שְׂרוּג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־נָחוֹר … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Serug lived thirty years, and begot Nahor. And Serug lived after he
# begot Nahor two hundred years, and begot sons and daughters."
m.step("Gen.11.22-23")
# ‹וַיְחִי שְׂרוּג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־נָחוֹר› event: beget —
# agent serug; theme nachor-ben-serug
m.event("beget", agent="serug", themes=["nachor_ben_serug"])
# ‹וַיְחִי שְׂרוּג אַחֲרֵי הוֹלִידוֹ אֶת־נָחוֹר מָאתַיִם שָׁנָה וַיּוֹלֶד
# בָּנִים וּבָנוֹת› fact holds: banim-and-vanot(serug)
m.fact("banim_u_vanot(serug)")

# -------------------------- Gen.11.24-25 · NACHOR_ROW_BEGETS_TERACH --------
# וַיְחִי נָחוֹר תֵּשַׁע וְעֶשְׂרִים שָׁנָה וַיּוֹלֶד אֶת־תָּרַח … וַיּוֹלֶד
# בָּנִים וּבָנוֹת
# "And Nahor lived nine and twenty years, and begot Terah. And Nahor lived
# after he begot Terah a hundred and nineteen years, and begot sons and
# daughters."
m.step("Gen.11.24-25")
# ‹וַיְחִי נָחוֹר תֵּשַׁע וְעֶשְׂרִים שָׁנָה וַיּוֹלֶד אֶת־תָּרַח› event:
# beget — agent nachor-ben-serug; theme terach
m.event("beget", agent="nachor_ben_serug", themes=["terach"])
# ‹וַיְחִי נָחוֹר אַחֲרֵי הוֹלִידוֹ אֶת־תֶּרַח תְּשַׁע־עֶשְׂרֵה שָׁנָה
# וּמְאַת שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› fact holds: banim-and-
# vanot(nachor-ben-serug)
m.fact("banim_u_vanot(nachor_ben_serug)")

# -------------------------- Gen.11.26 · TERACH_ROW_OPENS_THREE_SONS --------
# וַיְחִי־תֶרַח שִׁבְעִים שָׁנָה וַיּוֹלֶד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן
# "And Terah lived seventy years, and begot Abram, Nahor, and Haran."
m.step("Gen.11.26")
# ‹וַיְחִי־תֶרַח שִׁבְעִים שָׁנָה וַיּוֹלֶד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן› event: beget — agent terach; theme avram, nachor-ben-terach,
# haran
m.event("beget", agent="terach", themes=["avram", "nachor_ben_terach", "haran"])

# -------------------------- Gen.11.27 · TERACH_HEADER_INSIDE_THE_OPEN_ROW --
# וְאֵלֶּה תּוֹלְדֹת תֶּרַח תֶּרַח הוֹלִיד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן וְהָרָן הוֹלִיד אֶת־לוֹט
# "Now these are the generations of Terah. Terah begot Abram, Nahor, and
# Haran; and Haran begot Lot."
m.step("Gen.11.27")
# ‹וְאֵלֶּה תּוֹלְדֹת תֶּרַח› section generations-terach: ve-eleh toldot
# terach — the seventh toledot header labels; installs nothing
m.section("toledot_terach", "ve-eleh toldot terach — the seventh toledot header labels; installs nothing")
# ‹וְהָרָן הוֹלִיד אֶת־לוֹט› event: beget — agent haran; theme lot
m.event("beget", agent="haran", themes=["lot"])

# -------------------------- Gen.11.28 · HARAN_DIES_BEFORE_HIS_FATHER -------
# וַיָּמָת הָרָן עַל־פְּנֵי תֶּרַח אָבִיו בְּאֶרֶץ מוֹלַדְתּוֹ בְּאוּר
# כַּשְׂדִּים
# "And Haran died in the presence of his father Terah in the land of his
# nativity, in Ur of the Chaldees."
m.step("Gen.11.28")
# ‹וַיָּמָת הָרָן עַל־פְּנֵי תֶּרַח אָבִיו› event: die — agent haran
m.event("die", agent="haran")
# ‹בְּאֶרֶץ מוֹלַדְתּוֹ בְּאוּר כַּשְׂדִּים› fact holds: in-earth-moladto-
# in-ur-kasdim(haran)
m.fact("be_eretz_moladto_be_ur_kasdim(haran)")
# reads without prior install (flag, not fix): ur-kasdim
m.presupposed("ur_kasdim")

# -------------------------- Gen.11.29 · THE_WIVES_TAKEN_ONE_GENEALOGY_WITHHELD -
# וַיִּקַּח אַבְרָם וְנָחוֹר לָהֶם נָשִׁים שֵׁם אֵשֶׁת־אַבְרָם שָׂרָי וְשֵׁם
# אֵשֶׁת־נָחוֹר מִלְכָּה בַּת־הָרָן אֲבִי־מִלְכָּה וַאֲבִי יִסְכָּה
# "And Abram and Nahor took them wives: the name of Abram's wife was Sarai;
# and the name of Nahor's wife, Milcah, the daughter of Haran, the father of
# Milcah, and the father of Iscah."
m.step("Gen.11.29")
# ‹וַיִּקַּח אַבְרָם וְנָחוֹר לָהֶם נָשִׁים› event: take — agent avram;
# theme nashim
m.event("take", agent="avram", themes=["nashim"])
# ‹שֵׁם אֵשֶׁת־אַבְרָם שָׂרָי וְשֵׁם אֵשֶׁת־נָחוֹר מִלְכָּה› fact holds:
# shem-wife-of-avram-saray; shem-wife-of-nachor-milkah
m.fact("shem_eshet_avram_saray",
       "shem_eshet_nachor_milkah")
# ‹מִלְכָּה בַּת־הָרָן אֲבִי־מִלְכָּה וַאֲבִי יִסְכָּה› fact holds: milkah-
# bat-haran; haran-avi-milkah-and-avi-yiskah
m.fact("milkah_bat_haran",
       "haran_avi_milkah_va_avi_yiskah")

# -------------------------- Gen.11.30 · SARAI_BARREN_THE_DOUBLED_ABSENCE ---
# וַתְּהִי שָׂרַי עֲקָרָה אֵין לָהּ וָלָד
# "And Sarai was barren; she had no child."
m.step("Gen.11.30")
# ‹וַתְּהִי שָׂרַי עֲקָרָה› fact holds: saray-akarah
m.fact("saray_akarah")
# ‹אֵין לָהּ וָלָד› fact holds: ein-lah-valad
m.fact("ein_lah_valad")

# -------------------------- Gen.11.31 · THE_JOURNEY_STATED_STOPPED_SETTLED -
# וַיִּקַּח תֶּרַח אֶת־אַבְרָם בְּנוֹ וְאֶת־לוֹט בֶּן־הָרָן בֶּן־בְּנוֹ
# וְאֵת שָׂרַי כַּלָּתוֹ אֵשֶׁת אַבְרָם בְּנוֹ וַיֵּצְאוּ אִתָּם מֵאוּר
# כַּשְׂדִּים לָלֶכֶת אַרְצָה כְּנַעַן וַיָּבֹאוּ עַד־חָרָן וַיֵּשְׁבוּ שָׁם
# "And Terah took Abram his son, and Lot the son of Haran, his son's son,
# and Sarai his daughter-in-law, his son Abram's wife; and they went forth
# with them from Ur of the Chaldees, to go into the land of Canaan; and they
# came unto Haran, and dwelt there."
m.step("Gen.11.31")
# ‹וַיִּקַּח תֶּרַח אֶת־אַבְרָם בְּנוֹ וְאֶת־לוֹט בֶּן־הָרָן בֶּן־בְּנוֹ
# וְאֵת שָׂרַי כַּלָּתוֹ אֵשֶׁת אַבְרָם בְּנוֹ› event: take — agent terach;
# theme avram, lot, saray
m.event("take", agent="terach", themes=["avram", "lot", "saray"])
# ‹וַיֵּצְאוּ אִתָּם מֵאוּר כַּשְׂדִּים› event: go-out — agent terach
m.event("go_out", agent="terach")
# ‹לָלֶכֶת אַרְצָה כְּנַעַן› fact holds: to-lekhet-artzah-kenaan
m.fact("la_lekhet_artzah_kenaan")
# ‹וַיָּבֹאוּ עַד־חָרָן› event: come — agent terach
m.event("come", agent="terach")
# ‹וַיֵּשְׁבוּ שָׁם› event: settle — agent terach
m.event("settle", agent="terach")
# reads without prior install (flag, not fix): charan, earth-kenaan
m.presupposed("charan", "eretz_kenaan")

# -------------------------- Gen.11.32 · TERACH_ROW_CLOSES_WITHOUT_ALL ------
# וַיִּהְיוּ יְמֵי־תֶרַח חָמֵשׁ שָׁנִים וּמָאתַיִם שָׁנָה וַיָּמָת תֶּרַח
# בְּחָרָן
# "And the days of Terah were two hundred and five years; and Terah died in
# Haran."
m.step("Gen.11.32")
# ‹וַיִּהְיוּ יְמֵי־תֶרַח חָמֵשׁ שָׁנִים וּמָאתַיִם שָׁנָה› fact holds:
# days-of-terach-205-year
m.fact("yemei_terach_205_shanah")
# ‹וַיָּמָת תֶּרַח בְּחָרָן› event: die — agent terach
m.event("die", agent="terach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'ur_kasdim', 'eretz_kenaan', 'charan'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['shem_ben_meat_shanah', 'shenatayim_achar_ha_mabul', 'banim_u_vanot(shem)', 'banim_u_vanot(arpakhshad)', 'banim_u_vanot(shelach)', 'banim_u_vanot(ever)', 'banim_u_vanot(peleg)', 'banim_u_vanot(reu)', 'banim_u_vanot(serug)', 'banim_u_vanot(nachor_ben_serug)', 'be_eretz_moladto_be_ur_kasdim(haran)', 'shem_eshet_avram_saray', 'shem_eshet_nachor_milkah', 'milkah_bat_haran', 'haran_avi_milkah_va_avi_yiskah', 'saray_akarah', 'ein_lah_valad', 'la_lekhet_artzah_kenaan', 'yemei_terach_205_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_27_the_call
###############################################################################
# =============================================================================
# gen_27_the_call — 12:1-9
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_27_the_call.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The call: go to the land I will show you (12:1-9)"""
from machine import Machine

m = Machine("gen_27_the_call")

# -------------------------- Gen.12.1 · THE_CALL_WITH_THE_OBJECT_WITHHELD ---
# וַיֹּאמֶר יְהוָה אֶל־אַבְרָם לֶךְ־לְךָ מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ
# וּמִבֵּית אָבִיךָ אֶל־הָאָרֶץ אֲשֶׁר אַרְאֶךָּ
# "Now the LORD said unto Abram: 'Get thee out of thy country, and from thy
# kindred, and from thy father's house, unto the land that I will show
# thee.'"
m.step("Gen.12.1")
# ‹לֶךְ־לְךָ … אֶל־הָאָרֶץ אֲשֶׁר אַרְאֶךָּ› the-LORD speaks a demand — LET:
# lekh(avram, to-the-earth-which-areka)
m.declare("YHWH", "LET",
          "lekh(avram, el_ha_aretz_asher_areka)")
# ‹מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ וּמִבֵּית אָבִיךָ› fact holds: lekh-to-you-
# from-artzekha-and-from-moladtekha-and-from-beit-avikha
m.fact("lekh_lekha_me_artzekha_u_mi_moladtekha_u_mi_beit_avikha")

# -------------------------- Gen.12.2 · THE_PROMISE_LADDER_AND_THE_SECOND_IMPERATIVE -
# וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ וֶהְיֵה
# בְּרָכָה
# "And I will make of thee a great nation, and I will bless thee, and make
# thy name great; and be thou a blessing."
m.step("Gen.12.2")
# ‹וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ› fact holds:
# e-eskha-to-goy-gadol; and-avarekhkha-and-agadlah-shmekha
m.fact("e_eskha_le_goy_gadol",
       "va_avarekhkha_va_agadlah_shmekha")
# ‹וֶהְיֵה בְּרָכָה› the-LORD speaks a demand — LET: heyeh(avram, berakhah)
m.declare("YHWH", "LET",
          "heyeh(avram, berakhah)")

# -------------------------- Gen.12.3 · THE_ASYMMETRY_AND_THE_FAMILIES ------
# וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר וְנִבְרְכוּ בְךָ כֹּל
# מִשְׁפְּחֹת הָאֲדָמָה
# "And I will bless them that bless thee, and him that curseth thee will I
# curse; and in thee shall all the families of the earth be blessed.'"
m.step("Gen.12.3")
# ‹וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר› fact holds: and-avarakhah-
# mevarakhekha; and-meqallelkha-aor
m.fact("va_avarakhah_mevarakhekha",
       "u_meqallelkha_aor")
# ‹וְנִבְרְכוּ בְךָ כֹּל מִשְׁפְּחֹת הָאֲדָמָה› fact holds: and-nivrekhu-
# vekha-all-mishpechot-the-ground
m.fact("ve_nivrekhu_vekha_kol_mishpechot_ha_adamah")

# -------------------------- Gen.12.4 · THE_RECEIPT_IN_THE_LETTERS_OWN_GRAMMAR -
# וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה וַיֵּלֶךְ אִתּוֹ לוֹט
# וְאַבְרָם בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה בְּצֵאתוֹ מֵחָרָן
# "So Abram went, as the LORD had spoken unto him; and Lot went with him;
# and Abram was seventy and five years old when he departed out of Haran."
m.step("Gen.12.4")
# ‹וַיֵּלֶךְ אַבְרָם … וַיֵּלֶךְ אִתּוֹ לוֹט› event: go — agent avram
m.event("go", agent="avram")
# ‹וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה› demand settled (popped
# from the queue): lekh(avram, to-the-earth-which-areka)
m.result("lekh(avram, el_ha_aretz_asher_areka)", tmark="t1")
# ‹כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה … בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה›
# fact holds: like-which-dibber-to-him-the-LORD; avram-ben-75-year-in-tzeto-
# from-charan
m.fact("ka_asher_dibber_elav_YHWH",
       "avram_ben_75_shanah_be_tzeto_me_charan")
# reads without prior install (flag, not fix): charan
m.presupposed("charan")

# -------------------------- Gen.12.5 · THE_ARRIVAL_THE_FROZEN_WALL_WAITED_FOR -
# וַיִּקַּח אַבְרָם אֶת־שָׂרַי אִשְׁתּוֹ וְאֶת־לוֹט בֶּן־אָחִיו
# וְאֶת־כָּל־רְכוּשָׁם אֲשֶׁר רָכָשׁוּ וְאֶת־הַנֶּפֶשׁ אֲשֶׁר־עָשׂוּ בְחָרָן
# וַיֵּצְאוּ לָלֶכֶת אַרְצָה כְּנַעַן וַיָּבֹאוּ אַרְצָה כְּנָעַן
# "And Abram took Sarai his wife, and Lot his brother's son, and all their
# substance that they had gathered, and the souls that they had gotten in
# Haran; and they went forth to go into the land of Canaan; and into the
# land of Canaan they came."
m.step("Gen.12.5")
# ‹וַיִּקַּח אַבְרָם אֶת־שָׂרַי אִשְׁתּוֹ וְאֶת־לוֹט בֶּן־אָחִיו …› event:
# take — agent avram; theme saray, lot, all-rekhusham, the-nefesh-which-asu
m.event("take", agent="avram", themes=["saray", "lot", "kol_rekhusham", "ha_nefesh_asher_asu"])
# ‹וַיֵּצְאוּ לָלֶכֶת אַרְצָה כְּנַעַן› event: go-out — agent avram
m.event("go_out", agent="avram")
# ‹וַיָּבֹאוּ אַרְצָה כְּנָעַן› event: come — agent avram
m.event("come", agent="avram")
# ‹וְאֶת־כָּל־רְכוּשָׁם אֲשֶׁר רָכָשׁוּ וְאֶת־הַנֶּפֶשׁ אֲשֶׁר־עָשׂוּ
# בְחָרָן› fact holds: all-rekhusham-which-rakhashu; and-the-nefesh-which-
# asu-and-charan
m.fact("kol_rekhusham_asher_rakhashu",
       "ve_et_ha_nefesh_asher_asu_ve_charan")
# reads without prior install (flag, not fix): earth-kenaan
m.presupposed("eretz_kenaan")

# -------------------------- Gen.12.6 · THE_PASS_AND_THE_THEN ---------------
# וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה
# וְהַכְּנַעֲנִי אָז בָּאָרֶץ
# "And Abram passed through the land unto the place of Shechem, unto the
# terebinth of Moreh. And the Canaanite was then in the land."
m.step("Gen.12.6")
# ‹וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה› event:
# pass — agent avram; theme until-meqom-shekhem-until-elon-moreh
m.event("pass", agent="avram", themes=["ad_meqom_shekhem_ad_elon_moreh"])
# ‹וְהַכְּנַעֲנִי אָז בָּאָרֶץ› fact holds: and-the-kenaani-az-in-the-earth
m.fact("ve_ha_kenaani_az_ba_aretz")
# reads without prior install (flag, not fix): shekhem
m.presupposed("shekhem")

# -------------------------- Gen.12.7 · THE_APPEARANCE_THE_PLEDGE_THE_FIRST_ALTAR -
# וַיֵּרָא יְהוָה אֶל־אַבְרָם וַיֹּאמֶר לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ
# הַזֹּאת וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו
# "And the LORD appeared unto Abram, and said: 'Unto thy seed will I give
# this land'; and he builded there an altar unto the LORD, who appeared unto
# him."
m.step("Gen.12.7")
# ‹וַיֵּרָא יְהוָה אֶל־אַבְרָם› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹וַיֹּאמֶר› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ הַזֹּאת› fact holds: to-zarakha-etten-the-
# earth-the-this
m.fact("le_zarakha_etten_et_ha_aretz_ha_zot")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו› event: build — agent
# avram; theme altar-shekhem
m.event("build", agent="avram", themes=["mizbeach_shekhem"])
# ‹מִזְבֵּחַ› the world gains: altar-shekhem
m.install("mizbeach_shekhem")

# -------------------------- Gen.12.8 · THE_TENT_THE_SECOND_ALTAR_THE_NAME_CALLED -
# וַיַּעְתֵּק מִשָּׁם הָהָרָה מִקֶּדֶם לְבֵית־אֵל וַיֵּט אָהֳלֹה בֵּית־אֵל
# מִיָּם וְהָעַי מִקֶּדֶם וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה וַיִּקְרָא בְּשֵׁם
# יְהוָה
# "And he removed from thence unto the mountain on the east of Beth-el, and
# pitched his tent, having Beth-el on the west, and Ai on the east; and he
# builded there an altar unto the LORD, and called upon the name of the
# LORD."
m.step("Gen.12.8")
# ‹וַיַּעְתֵּק מִשָּׁם הָהָרָה מִקֶּדֶם לְבֵית־אֵל› event: move-on — agent
# avram
m.event("move_on", agent="avram")
# ‹וַיֵּט אָהֳלֹה בֵּית־אֵל מִיָּם וְהָעַי מִקֶּדֶם› event: pitch — agent
# avram; theme ohel
m.event("pitch", agent="avram", themes=["ohel"])
# ‹וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה› event: build — agent avram; theme altar-
# beit-to
m.event("build", agent="avram", themes=["mizbeach_beit_el"])
# ‹מִזְבֵּחַ› the world gains: altar-beit-to
m.install("mizbeach_beit_el")
# ‹וַיִּקְרָא בְּשֵׁם יְהוָה› event: call — agent avram; theme in-shem-the-
# LORD
m.event("call", agent="avram", themes=["be_shem_YHWH"])
# reads without prior install (flag, not fix): beit-to, the-ai
m.presupposed("beit_el", "ha_ai")

# -------------------------- Gen.12.9 · THE_ROAD_SOUTH_STAYS_OPEN -----------
# וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה
# "And Abram journeyed, going on still toward the South."
m.step("Gen.12.9")
# ‹וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה› event: journey — agent
# avram
m.event("journey", agent="avram")
# reads without prior install (flag, not fix): the-negev
m.presupposed("ha_negev")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach_shekhem', 'mizbeach_beit_el'}
    assert m.presupposed_set() == {'ha_ai', 'shekhem', 'beit_el', 'charan', 'eretz_kenaan', 'ha_negev'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['heyeh(avram, berakhah)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6}
    assert sorted(m.WORLD["facts"]) == sorted(['lekh_lekha_me_artzekha_u_mi_moladtekha_u_mi_beit_avikha', 'e_eskha_le_goy_gadol', 'va_avarekhkha_va_agadlah_shmekha', 'va_avarakhah_mevarakhekha', 'u_meqallelkha_aor', 've_nivrekhu_vekha_kol_mishpechot_ha_adamah', 'ka_asher_dibber_elav_YHWH', 'avram_ben_75_shanah_be_tzeto_me_charan', 'kol_rekhusham_asher_rakhashu', 've_et_ha_nefesh_asher_asu_ve_charan', 've_ha_kenaani_az_ba_aretz', 'le_zarakha_etten_et_ha_aretz_ha_zot'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 16
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_28_egypt_descent
###############################################################################
# =============================================================================
# gen_28_egypt_descent — 12:10-20
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_28_egypt_descent.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The descent to Egypt: the famine, the sister-word, the plagued house (12:10-20)"""
from machine import Machine

m = Machine("gen_28_egypt_descent")

# -------------------------- Gen.12.10 · THE_DESCENT_FOR_FAMINE -------------
# וַיְהִי רָעָב בָּאָרֶץ וַיֵּרֶד אַבְרָם מִצְרַיְמָה לָגוּר שָׁם כִּי־כָבֵד
# הָרָעָב בָּאָרֶץ
# "And there was a famine in the land; and Abram went down into Egypt to
# sojourn there; for the famine was sore in the land."
m.step("Gen.12.10")
# ‹וַיֵּרֶד אַבְרָם מִצְרַיְמָה לָגוּר שָׁם› event: go-down — agent avram
m.event("go_down", agent="avram")
# ‹כִּי־כָבֵד הָרָעָב בָּאָרֶץ› fact holds: when-khaved-the-raav-in-the-
# earth
m.fact("ki_khaved_ha_raav_ba_aretz")
# reads without prior install (flag, not fix): mitzrayim
m.presupposed("mitzrayim")

# -------------------------- Gen.12.11 · THE_FIRST_SPEECH_IS_FEAR_AND_BEAUTY -
# וַיְהִי כַּאֲשֶׁר הִקְרִיב לָבוֹא מִצְרָיְמָה וַיֹּאמֶר אֶל־שָׂרַי
# אִשְׁתּוֹ הִנֵּה־נָא יָדַעְתִּי כִּי אִשָּׁה יְפַת־מַרְאֶה אָתְּ
# "And it came to pass, when he was come near to enter into Egypt, that he
# said unto Sarai his wife: 'Behold now, I know that thou art a fair woman
# to look upon.'"
m.step("Gen.12.11")
# ‹וַיֹּאמֶר אֶל־שָׂרַי אִשְׁתּוֹ› event: say — agent avram
m.event("say", agent="avram")
# ‹הִנֵּה־נָא יָדַעְתִּי כִּי אִשָּׁה יְפַת־מַרְאֶה אָתְּ› fact holds:
# behold-na-yadati-when-woman-yefat-appearance-at
m.fact("hinneh_na_yadati_ki_ishah_yefat_mareh_at")

# -------------------------- Gen.12.12 · THE_FEAR_FORECAST ------------------
# וְהָיָה כִּי־יִרְאוּ אֹתָךְ הַמִּצְרִים וְאָמְרוּ אִשְׁתּוֹ זֹאת וְהָרְגוּ
# אֹתִי וְאֹתָךְ יְחַיּוּ
# "And it will come to pass, when the Egyptians shall see thee, that they
# will say: This is his wife; and they will kill me, but thee they will keep
# alive."
m.step("Gen.12.12")
# ‹וְהָרְגוּ אֹתִי וְאֹתָךְ יְחַיּוּ› fact holds: and-hargu-me-and-otakh-
# yechayu
m.fact("ve_hargu_oti_ve_otakh_yechayu")

# -------------------------- Gen.12.13 · THE_REQUEST_WITH_NO_REPLY ----------
# אִמְרִי־נָא אֲחֹתִי אָתְּ לְמַעַן יִיטַב־לִי בַעֲבוּרֵךְ וְחָיְתָה
# נַפְשִׁי בִּגְלָלֵךְ
# "Say, I pray thee, thou art my sister; that it may be well with me for thy
# sake, and that my soul may live because of thee.'"
m.step("Gen.12.13")
# ‹אִמְרִי־נָא אֲחֹתִי אָתְּ› avram speaks a demand — LET: imri(saray,
# achoti-hi)
m.declare("avram", "LET",
          "imri(saray, achoti_hi)")
# ‹לְמַעַן יִיטַב־לִי בַעֲבוּרֵךְ וְחָיְתָה נַפְשִׁי בִּגְלָלֵךְ› fact
# holds: lemaan-yitav-to-me-vaavurekh-and-chaytah-nafshi
m.fact("lemaan_yitav_li_vaavurekh_ve_chaytah_nafshi")

# -------------------------- Gen.12.14 · THE_SEEING -------------------------
# וַיְהִי כְּבוֹא אַבְרָם מִצְרָיְמָה וַיִּרְאוּ הַמִּצְרִים אֶת־הָאִשָּׁה
# כִּי־יָפָה הִוא מְאֹד
# "And it came to pass, that, when Abram was come into Egypt, the Egyptians
# beheld the woman that she was very fair."
m.step("Gen.12.14")
# ‹וַיִּרְאוּ הַמִּצְרִים אֶת־הָאִשָּׁה› event: see — agent the-mitzrim;
# theme the-woman
m.event("see", agent="ha_mitzrim", themes=["ha_ishah"])
# ‹כִּי־יָפָה הִוא מְאֹד› fact holds: when-yafah-hi-very
m.fact("ki_yafah_hi_meod")

# -------------------------- Gen.12.15 · THE_PRAISE_AND_THE_PASSIVE_TAKING --
# וַיִּרְאוּ אֹתָהּ שָׂרֵי פַרְעֹה וַיְהַלְלוּ אֹתָהּ אֶל־פַּרְעֹה וַתֻּקַּח
# הָאִשָּׁה בֵּית פַּרְעֹה
# "And the princes of Pharaoh saw her, and praised her to Pharaoh; and the
# woman was taken into Pharaoh's house."
m.step("Gen.12.15")
# ‹וַיִּרְאוּ אֹתָהּ שָׂרֵי פַרְעֹה› event: see — agent sarei-faro; theme
# the-woman
m.event("see", agent="sarei_faro", themes=["ha_ishah"])
# ‹וַיְהַלְלוּ אֹתָהּ אֶל־פַּרְעֹה› event: praise — agent sarei-faro
m.event("praise", agent="sarei_faro")
# ‹וַתֻּקַּח הָאִשָּׁה בֵּית פַּרְעֹה› event: take — theme the-woman
m.event("take", themes=["ha_ishah"])

# -------------------------- Gen.12.16 · THE_PAYMENT_FOR_HER_SAKE -----------
# וּלְאַבְרָם הֵיטִיב בַּעֲבוּרָהּ וַיְהִי־לוֹ צֹאן־וּבָקָר וַחֲמֹרִים
# וַעֲבָדִים וּשְׁפָחֹת וַאֲתֹנֹת וּגְמַלִּים
# "And he dealt well with Abram for her sake; and he had sheep, and oxen,
# and he-asses, and men-servants, and maid-servants, and she-asses, and
# camels."
m.step("Gen.12.16")
# ‹וּלְאַבְרָם הֵיטִיב בַּעֲבוּרָהּ› event: do-good — agent paro
m.event("do_good", agent="paro")
# ‹וַיְהִי־לוֹ צֹאן־וּבָקָר וַחֲמֹרִים וַעֲבָדִים וּשְׁפָחֹת וַאֲתֹנֹת
# וּגְמַלִּים› fact holds: and-yehi-not-tzon-and-vaqar-and-chamorim-and-
# avadim-and-shfachot-and-atonot-and-gemalim
m.fact("va_yehi_lo_tzon_u_vaqar_va_chamorim_va_avadim_u_shfachot_va_atonot_u_gemalim")

# -------------------------- Gen.12.17 · THE_PLAGUE_WITHOUT_A_WORD ----------
# וַיְנַגַּע יְהוָה אֶת־פַּרְעֹה נְגָעִים גְּדֹלִים וְאֶת־בֵּיתוֹ עַל־דְּבַר
# שָׂרַי אֵשֶׁת אַבְרָם
# "And the LORD plagued Pharaoh and his house with great plagues because of
# Sarai Abram's wife."
m.step("Gen.12.17")
# ‹וַיְנַגַּע יְהוָה אֶת־פַּרְעֹה נְגָעִים גְּדֹלִים וְאֶת־בֵּיתוֹ› event:
# plague — agent the-LORD; theme paro-and-veito
m.event("plague", agent="YHWH", themes=["paro_u_veito"])
# ‹עַל־דְּבַר שָׂרַי אֵשֶׁת אַבְרָם› fact holds: upon-devar-saray-wife-of-
# avram
m.fact("al_devar_saray_eshet_avram")

# -------------------------- Gen.12.18 · THE_KINGS_QUESTIONS_IN_THE_GARDENS_FORM -
# וַיִּקְרָא פַרְעֹה לְאַבְרָם וַיֹּאמֶר מַה־זֹּאת עָשִׂיתָ לִּי לָמָּה
# לֹא־הִגַּדְתָּ לִּי כִּי אִשְׁתְּךָ הִוא
# "And Pharaoh called Abram, and said: 'What is this that thou hast done
# unto me? why didst thou not tell me that she was thy wife?'"
m.step("Gen.12.18")
# ‹וַיִּקְרָא פַרְעֹה לְאַבְרָם וַיֹּאמֶר מַה־זֹּאת עָשִׂיתָ לִּי› event:
# say — agent paro
m.event("say", agent="paro")

# -------------------------- Gen.12.19 · THE_CONFESSION_AND_THE_COUNTER_COMMANDS -
# לָמָה אָמַרְתָּ אֲחֹתִי הִוא וָאֶקַּח אֹתָהּ לִי לְאִשָּׁה וְעַתָּה הִנֵּה
# אִשְׁתְּךָ קַח וָלֵךְ
# "Why saidst thou: She is my sister? so that I took her to be my wife; now
# therefore behold thy wife, take her, and go thy way.'"
m.step("Gen.12.19")
# ‹אָמַרְתָּ אֲחֹתִי הִוא וָאֶקַּח אֹתָהּ לִי לְאִשָּׁה› fact holds: amarta-
# achoti-hi; and-eqach-her-to-me-to-woman
m.fact("amarta_achoti_hi",
       "va_eqach_otah_li_le_ishah")
# ‹הִנֵּה אִשְׁתְּךָ קַח› paro speaks a demand — LET: qach(avram, his-wife)
m.declare("paro", "LET",
          "qach(avram, et_ishto)")
# ‹וָלֵךְ› paro speaks a demand — LET: lekh(avram)
m.declare("paro", "LET",
          "lekh(avram)")

# -------------------------- Gen.12.20 · THE_ESCORTED_EXPULSION -------------
# וַיְצַו עָלָיו פַּרְעֹה אֲנָשִׁים וַיְשַׁלְּחוּ אֹתוֹ וְאֶת־אִשְׁתּוֹ
# וְאֶת־כָּל־אֲשֶׁר־לוֹ
# "And Pharaoh gave men charge concerning him; and they brought him on the
# way, and his wife, and all that he had."
m.step("Gen.12.20")
# ‹וַיְצַו עָלָיו פַּרְעֹה אֲנָשִׁים› event: command — agent paro; theme
# anashim
m.event("command", agent="paro", themes=["anashim"])
# ‹וַיְשַׁלְּחוּ אֹתוֹ וְאֶת־אִשְׁתּוֹ וְאֶת־כָּל־אֲשֶׁר־לוֹ› event: send-
# away — agent anashim; theme avram-and-his-wife-and-all-which-not
m.event("send_away", agent="anashim", themes=["avram_ve_ishto_ve_khol_asher_lo"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'mitzrayim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['imri(saray, achoti_hi)', 'qach(avram, et_ishto)', 'lekh(avram)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['ki_khaved_ha_raav_ba_aretz', 'hinneh_na_yadati_ki_ishah_yefat_mareh_at', 've_hargu_oti_ve_otakh_yechayu', 'lemaan_yitav_li_vaavurekh_ve_chaytah_nafshi', 'ki_yafah_hi_meod', 'va_yehi_lo_tzon_u_vaqar_va_chamorim_va_avadim_u_shfachot_va_atonot_u_gemalim', 'al_devar_saray_eshet_avram', 'amarta_achoti_hi', 'va_eqach_otah_li_le_ishah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_29_separation_promise
###############################################################################
# =============================================================================
# gen_29_separation_promise — 13:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_29_separation_promise.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The separation and the promise: the return, the strife, the plain, the land forever (13:1-18)"""
from machine import Machine

m = Machine("gen_29_separation_promise")

# -------------------------- Gen.13.1 · THE_ASCENT_WITH_ALL -----------------
# וַיַּעַל אַבְרָם מִמִּצְרַיִם הוּא וְאִשְׁתּוֹ וְכָל־אֲשֶׁר־לוֹ וְלוֹט
# עִמּוֹ הַנֶּגְבָּה
# "And Abram went up out of Egypt, he, and his wife, and all that he had,
# and Lot with him, into the South."
m.step("Gen.13.1")
# ‹וַיַּעַל אַבְרָם מִמִּצְרַיִם› event: go-up — agent avram
m.event("go_up", agent="avram")
# ‹הוּא וְאִשְׁתּוֹ וְכָל־אֲשֶׁר־לוֹ וְלוֹט עִמּוֹ› fact holds: that-and-
# his-wife-and-all-which-not-and-lot-imo
m.fact("hu_ve_ishto_ve_khol_asher_lo_ve_lot_imo")
# reads without prior install (flag, not fix): mitzrayim, the-negev
m.presupposed("mitzrayim", "ha_negev")

# -------------------------- Gen.13.2 · THE_HEAVY_WEALTH --------------------
# וְאַבְרָם כָּבֵד מְאֹד בַּמִּקְנֶה בַּכֶּסֶף וּבַזָּהָב
# "And Abram was very rich in cattle, in silver, and in gold."
m.step("Gen.13.2")
# ‹כָּבֵד מְאֹד בַּמִּקְנֶה בַּכֶּסֶף וּבַזָּהָב› fact holds: kaved-very-in-
# the-miqneh-in-the-kesef-and-and-gold
m.fact("kaved_meod_ba_miqneh_ba_kesef_u_va_zahav")

# -------------------------- Gen.13.3 · THE_RETRACED_STAGES -----------------
# וַיֵּלֶךְ לְמַסָּעָיו מִנֶּגֶב וְעַד־בֵּית־אֵל עַד־הַמָּקוֹם אֲשֶׁר־הָיָה
# שָׁם אהלה אָהֳלוֹ בַּתְּחִלָּה בֵּין בֵּית־אֵל וּבֵין הָעָי
# "And he went on his journeys from the South even to Beth-el, unto the
# place where his tent had been at the beginning, between Beth-el and Ai;"
m.step("Gen.13.3")
# ‹וַיֵּלֶךְ לְמַסָּעָיו› event: go — agent avram
m.event("go", agent="avram")
# ‹אֲשֶׁר־הָיָה שָׁם אהלה אָהֳלוֹ בַּתְּחִלָּה› fact holds: which-was-there-
# aholo-in-the-techillah
m.fact("asher_hayah_sham_aholo_ba_techillah")
# reads without prior install (flag, not fix): beit-to, the-ai
m.presupposed("beit_el", "ha_ai")

# -------------------------- Gen.13.4 · THE_RETURN_CALL_AT_THE_FIRST_ALTAR --
# אֶל־מְקוֹם הַמִּזְבֵּחַ אֲשֶׁר־עָשָׂה שָׁם בָּרִאשֹׁנָה וַיִּקְרָא שָׁם
# אַבְרָם בְּשֵׁם יְהוָה
# "unto the place of the altar, which he had made there at the first; and
# Abram called there on the name of the LORD."
m.step("Gen.13.4")
# ‹מְקוֹם הַמִּזְבֵּחַ אֲשֶׁר־עָשָׂה שָׁם› reads without prior install
# (flag, not fix): altar-beit-to
m.presupposed("mizbeach_beit_el")
# ‹וַיִּקְרָא שָׁם אַבְרָם בְּשֵׁם יְהוָה› event: call — agent avram; theme
# shem-the-LORD
m.event("call", agent="avram", themes=["shem_YHWH"])

# -------------------------- Gen.13.5 · LOTS_HOLDINGS -----------------------
# וְגַם־לְלוֹט הַהֹלֵךְ אֶת־אַבְרָם הָיָה צֹאן־וּבָקָר וְאֹהָלִים
# "And Lot also, who went with Abram, had flocks, and herds, and tents."
m.step("Gen.13.5")
# ‹וְגַם־לְלוֹט ... הָיָה צֹאן־וּבָקָר וְאֹהָלִים› fact holds: and-also-to-
# lot-tzon-and-vaqar-and-ohalim
m.fact("ve_gam_le_lot_tzon_u_vaqar_ve_ohalim")

# -------------------------- Gen.13.6 · THE_LAND_THAT_COULD_NOT_BEAR --------
# וְלֹא־נָשָׂא אֹתָם הָאָרֶץ לָשֶׁבֶת יַחְדָּו כִּי־הָיָה רְכוּשָׁם רָב
# וְלֹא יָכְלוּ לָשֶׁבֶת יַחְדָּו
# "And the land was not able to bear them, that they might dwell together;
# for their substance was great, so that they could not dwell together."
m.step("Gen.13.6")
# ‹וְלֹא־נָשָׂא אֹתָם הָאָרֶץ ... כִּי־הָיָה רְכוּשָׁם רָב› fact holds: not-
# nasa-otam-the-earth-to-shevet-yachdav; when-was-rekhusham-rav
m.fact("lo_nasa_otam_ha_aretz_la_shevet_yachdav",
       "ki_hayah_rekhusham_rav")

# -------------------------- Gen.13.7 · THE_STRIFE_AND_THE_WATCHING_LAND ----
# וַיְהִי־רִיב בֵּין רֹעֵי מִקְנֵה־אַבְרָם וּבֵין רֹעֵי מִקְנֵה־לוֹט
# וְהַכְּנַעֲנִי וְהַפְּרִזִּי אָז יֹשֵׁב בָּאָרֶץ
# "And there was a strife between the herdmen of Abram's cattle and the
# herdmen of Lot's cattle. And the Canaanite and the Perizzite dwelt then in
# the land."
m.step("Gen.13.7")
# ‹וַיְהִי־רִיב ... וְהַכְּנַעֲנִי וְהַפְּרִזִּי אָז יֹשֵׁב בָּאָרֶץ› fact
# holds: and-yehi-riv-between-roei-miqneh-avram-and-vein-roei-miqneh-lot;
# and-the-kenaani-and-the-perizi-az-yoshev-in-the-earth
m.fact("va_yehi_riv_bein_roei_miqneh_avram_u_vein_roei_miqneh_lot",
       "ve_ha_kenaani_ve_ha_perizi_az_yoshev_ba_aretz")

# -------------------------- Gen.13.8 · THE_PEACE_PLEA_WE_ARE_BROTHERS ------
# וַיֹּאמֶר אַבְרָם אֶל־לוֹט אַל־נָא תְהִי מְרִיבָה בֵּינִי וּבֵינֶיךָ
# וּבֵין רֹעַי וּבֵין רֹעֶיךָ כִּי־אֲנָשִׁים אַחִים אֲנָחְנוּ
# "And Abram said unto Lot: 'Let there be no strife, I pray thee, between me
# and thee, and between my herdmen and thy herdmen; for we are brethren."
m.step("Gen.13.8")
# ‹וַיֹּאמֶר אַבְרָם אֶל־לוֹט› event: say — agent avram
m.event("say", agent="avram")
# ‹אַל־נָא תְהִי מְרִיבָה בֵּינִי וּבֵינֶיךָ› avram speaks a demand — LET-
# NOT: tehi(merivah, between-avram-and-ven-lot)
m.declare("avram", "LET-NOT",
          "tehi(merivah, bein_avram_u_ven_lot)")
# ‹כִּי־אֲנָשִׁים אַחִים אֲנָחְנוּ› fact holds: when-anashim-achim-anachnu
m.fact("ki_anashim_achim_anachnu")

# -------------------------- Gen.13.9 · THE_OFFER_OF_THE_WHOLE_LAND ---------
# הֲלֹא כָל־הָאָרֶץ לְפָנֶיךָ הִפָּרֶד נָא מֵעָלָי אִם־הַשְּׂמֹאל וְאֵימִנָה
# וְאִם־הַיָּמִין וְאַשְׂמְאִילָה
# "Is not the whole land before thee? separate thyself, I pray thee, from
# me; if thou wilt take the left hand, then I will go to the right; or if
# thou take the right hand, then I will go to the left.'"
m.step("Gen.13.9")
# ‹הֲלֹא כָל־הָאָרֶץ לְפָנֶיךָ› fact holds: the-not-all-the-earth-lefanekha
m.fact("ha_lo_khol_ha_aretz_lefanekha")
# ‹הִפָּרֶד נָא מֵעָלָי› avram speaks a demand — LET: hipared(lot, from-
# upon-avram)
m.declare("avram", "LET",
          "hipared(lot, me_al_avram)")
# ‹אִם־הַשְּׂמֹאל וְאֵימִנָה וְאִם־הַיָּמִין וְאַשְׂמְאִילָה› fact holds:
# if-the-semol-and-eminah-and-if-the-yamin-and-asmilah
m.fact("im_ha_semol_ve_eminah_ve_im_ha_yamin_ve_asmilah")

# -------------------------- Gen.13.10 · THE_EYES_LIFT_TOWARD_EDEN_GROUND ---
# וַיִּשָּׂא־לוֹט אֶת־עֵינָיו וַיַּרְא אֶת־כָּל־כִּכַּר הַיַּרְדֵּן כִּי
# כֻלָּהּ מַשְׁקֶה לִפְנֵי שַׁחֵת יְהוָה אֶת־סְדֹם וְאֶת־עֲמֹרָה
# כְּגַן־יְהוָה כְּאֶרֶץ מִצְרַיִם בֹּאֲכָה צֹעַר
# "And Lot lifted up his eyes, and beheld all the plain of the Jordan, that
# it was well watered every where, before the LORD destroyed Sodom and
# Gomorrah, like the garden of the LORD, like the land of Egypt, as thou
# goest unto Zoar."
m.step("Gen.13.10")
# ‹וַיִּשָּׂא־לוֹט אֶת־עֵינָיו› event: lift-eyes — agent lot; theme einav
m.event("lift_eyes", agent="lot", themes=["einav"])
# ‹וַיַּרְא אֶת־כָּל־כִּכַּר הַיַּרְדֵּן› event: see — agent lot; theme all-
# kikar-the-yarden
m.event("see", agent="lot", themes=["kol_kikar_ha_yarden"])
# ‹כִּי כֻלָּהּ מַשְׁקֶה לִפְנֵי שַׁחֵת יְהוָה אֶת־סְדֹם וְאֶת־עֲמֹרָה
# כְּגַן־יְהוָה כְּאֶרֶץ מִצְרַיִם› fact holds: when-khulah-mashqeh-lifnei-
# shachet-the-LORD-sedom-and-amorah
m.fact("ki_khulah_mashqeh_lifnei_shachet_YHWH_et_sedom_ve_et_amorah")
# reads without prior install (flag, not fix): the-yarden, sedom, amora,
# tzoar
m.presupposed("ha_yarden", "sedom", "amora", "tzoar")

# -------------------------- Gen.13.11 · THE_CHOICE_AND_THE_SEPARATION ------
# וַיִּבְחַר־לוֹ לוֹט אֵת כָּל־כִּכַּר הַיַּרְדֵּן וַיִּסַּע לוֹט מִקֶּדֶם
# וַיִּפָּרְדוּ אִישׁ מֵעַל אָחִיו
# "So Lot chose him all the plain of the Jordan; and Lot journeyed east; and
# they separated themselves the one from the other."
m.step("Gen.13.11")
# ‹וַיִּבְחַר־לוֹ לוֹט אֵת כָּל־כִּכַּר הַיַּרְדֵּן› event: choose — agent
# lot; theme all-kikar-the-yarden
m.event("choose", agent="lot", themes=["kol_kikar_ha_yarden"])
# ‹וַיִּסַּע לוֹט מִקֶּדֶם› event: journey — agent lot
m.event("journey", agent="lot")
# ‹וַיִּפָּרְדוּ אִישׁ מֵעַל אָחִיו› demand settled (popped from the queue):
# hipared(lot, from-upon-avram)
m.result("hipared(lot, me_al_avram)", tmark="t1")

# -------------------------- Gen.13.12 · THE_TWO_SETTLINGS ------------------
# אַבְרָם יָשַׁב בְּאֶרֶץ־כְּנָעַן וְלוֹט יָשַׁב בְּעָרֵי הַכִּכָּר
# וַיֶּאֱהַל עַד־סְדֹם
# "Abram dwelt in the land of Canaan, and Lot dwelt in the cities of the
# Plain, and moved his tent as far as Sodom."
m.step("Gen.13.12")
# ‹אַבְרָם יָשַׁב בְּאֶרֶץ־כְּנָעַן› event: dwell — agent avram
m.event("dwell", agent="avram")
# ‹וְלוֹט יָשַׁב בְּעָרֵי הַכִּכָּר› event: dwell — agent lot
m.event("dwell", agent="lot")
# ‹וַיֶּאֱהַל עַד־סְדֹם› event: tent — agent lot
m.event("tent", agent="lot")
# reads without prior install (flag, not fix): earth-kenaan
m.presupposed("eretz_kenaan")

# -------------------------- Gen.13.13 · THE_SODOM_VERDICT ------------------
# וְאַנְשֵׁי סְדֹם רָעִים וְחַטָּאִים לַיהוָה מְאֹד
# "Now the men of Sodom were wicked and sinners against the LORD
# exceedingly."
m.step("Gen.13.13")
# ‹וְאַנְשֵׁי סְדֹם רָעִים וְחַטָּאִים לַיהוָה מְאֹד› fact holds: and-men-
# of-sedom-raim-and-chataim-to-the-LORD-very
m.fact("ve_anshei_sedom_raim_ve_chataim_la_YHWH_meod")

# -------------------------- Gen.13.14 · THE_SPEECH_AFTER_THE_SEPARATING ----
# וַיהוָה אָמַר אֶל־אַבְרָם אַחֲרֵי הִפָּרֶד־לוֹט מֵעִמּוֹ שָׂא נָא עֵינֶיךָ
# וּרְאֵה מִן־הַמָּקוֹם אֲשֶׁר־אַתָּה שָׁם צָפֹנָה וָנֶגְבָּה וָקֵדְמָה
# וָיָמָּה
# "And the LORD said unto Abram, after that Lot was separated from him:
# 'Lift up now thine eyes, and look from the place where thou art, northward
# and southward and eastward and westward;"
m.step("Gen.13.14")
# ‹וַיהוָה אָמַר אֶל־אַבְרָם אַחֲרֵי הִפָּרֶד־לוֹט מֵעִמּוֹ› event: say —
# agent the-LORD
m.event("say", agent="YHWH")
# ‹שָׂא נָא עֵינֶיךָ וּרְאֵה ... צָפֹנָה וָנֶגְבָּה וָקֵדְמָה וָיָמָּה› the-
# LORD speaks a demand — LET: sa-and-ree(avram, tzafonah-and-negbah-and-
# qedmah-and-yamah)
m.declare("YHWH", "LET",
          "sa_u_ree(avram, tzafonah_va_negbah_va_qedmah_va_yamah)")

# -------------------------- Gen.13.15 · THE_GIFT_FOREVER -------------------
# כִּי אֶת־כָּל־הָאָרֶץ אֲשֶׁר־אַתָּה רֹאֶה לְךָ אֶתְּנֶנָּה וּלְזַרְעֲךָ
# עַד־עוֹלָם
# "for all the land which thou seest, to thee will I give it, and to thy
# seed for ever."
m.step("Gen.13.15")
# ‹כִּי אֶת־כָּל־הָאָרֶץ אֲשֶׁר־אַתָּה רֹאֶה לְךָ אֶתְּנֶנָּה וּלְזַרְעֲךָ
# עַד־עוֹלָם› fact holds: all-the-earth-which-ata-shepherd-to-you-etnenah;
# and-to-zarakha-until-olam
m.fact("et_kol_ha_aretz_asher_ata_roeh_lekha_etnenah",
       "u_le_zarakha_ad_olam")

# -------------------------- Gen.13.16 · THE_DUST_MEASURE -------------------
# וְשַׂמְתִּי אֶת־זַרְעֲךָ כַּעֲפַר הָאָרֶץ אֲשֶׁר אִם־יוּכַל אִישׁ לִמְנוֹת
# אֶת־עֲפַר הָאָרֶץ גַּם־זַרְעֲךָ יִמָּנֶה
# "And I will make thy seed as the dust of the earth; so that if a man can
# number the dust of the earth, then shall thy seed also be numbered."
m.step("Gen.13.16")
# ‹וְשַׂמְתִּי אֶת־זַרְעֲךָ כַּעֲפַר הָאָרֶץ ... גַּם־זַרְעֲךָ יִמָּנֶה›
# fact holds: and-samti-zarakha-like-afar-the-earth; if-yukhal-man-limnot-
# also-zarakha-yimaneh
m.fact("ve_samti_et_zarakha_ka_afar_ha_aretz",
       "im_yukhal_ish_limnot_gam_zarakha_yimaneh")

# -------------------------- Gen.13.17 · THE_WALK_COMMAND -------------------
# קוּם הִתְהַלֵּךְ בָּאָרֶץ לְאָרְכָּהּ וּלְרָחְבָּהּ כִּי לְךָ אֶתְּנֶנָּה
# "Arise, walk through the land in the length of it and in the breadth of
# it; for unto thee will I give it.'"
m.step("Gen.13.17")
# ‹קוּם הִתְהַלֵּךְ בָּאָרֶץ לְאָרְכָּהּ וּלְרָחְבָּהּ› the-LORD speaks a
# demand — LET: qum-walked-about(avram, in-the-earth-to-arkah-and-to-
# rachbah)
m.declare("YHWH", "LET",
          "qum_hithalekh(avram, ba_aretz_le_arkah_u_le_rachbah)")
# ‹כִּי לְךָ אֶתְּנֶנָּה› fact holds: when-to-you-etnenah
m.fact("ki_lekha_etnenah")

# -------------------------- Gen.13.18 · THE_HEBRON_ALTAR -------------------
# וַיֶּאֱהַל אַבְרָם וַיָּבֹא וַיֵּשֶׁב בְּאֵלֹנֵי מַמְרֵא אֲשֶׁר
# בְּחֶבְרוֹן וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה
# "And Abram moved his tent, and came and dwelt by the terebinths of Mamre,
# which are in Hebron, and built there an altar unto the LORD."
m.step("Gen.13.18")
# ‹וַיֶּאֱהַל אַבְרָם› event: tent — agent avram
m.event("tent", agent="avram")
# ‹וַיָּבֹא› event: come — agent avram
m.event("come", agent="avram")
# ‹וַיֵּשֶׁב בְּאֵלֹנֵי מַמְרֵא› event: dwell — agent avram
m.event("dwell", agent="avram")
# ‹וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה› event: build — agent avram; theme altar
m.event("build", agent="avram", themes=["mizbeach"])
# ‹מִזְבֵּחַ› the world gains: altar-chevron
m.install("mizbeach_chevron")
# reads without prior install (flag, not fix): mamre, chevron
m.presupposed("mamre", "chevron")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach_chevron'}
    assert m.presupposed_set() == {'tzoar', 'beit_el', 'sedom', 'mitzrayim', 'chevron', 'ha_yarden', 'mizbeach_beit_el', 'ha_negev', 'eretz_kenaan', 'mamre', 'amora', 'ha_ai'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tehi(merivah, bein_avram_u_ven_lot)', 'sa_u_ree(avram, tzafonah_va_negbah_va_qedmah_va_yamah)', 'qum_hithalekh(avram, ba_aretz_le_arkah_u_le_rachbah)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 12}
    assert sorted(m.WORLD["facts"]) == sorted(['hu_ve_ishto_ve_khol_asher_lo_ve_lot_imo', 'kaved_meod_ba_miqneh_ba_kesef_u_va_zahav', 'asher_hayah_sham_aholo_ba_techillah', 've_gam_le_lot_tzon_u_vaqar_ve_ohalim', 'lo_nasa_otam_ha_aretz_la_shevet_yachdav', 'ki_hayah_rekhusham_rav', 'va_yehi_riv_bein_roei_miqneh_avram_u_vein_roei_miqneh_lot', 've_ha_kenaani_ve_ha_perizi_az_yoshev_ba_aretz', 'ki_anashim_achim_anachnu', 'ha_lo_khol_ha_aretz_lefanekha', 'im_ha_semol_ve_eminah_ve_im_ha_yamin_ve_asmilah', 'ki_khulah_mashqeh_lifnei_shachet_YHWH_et_sedom_ve_et_amorah', 've_anshei_sedom_raim_ve_chataim_la_YHWH_meod', 'et_kol_ha_aretz_asher_ata_roeh_lekha_etnenah', 'u_le_zarakha_ad_olam', 've_samti_et_zarakha_ka_afar_ha_aretz', 'im_yukhal_ish_limnot_gam_zarakha_yimaneh', 'ki_lekha_etnenah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 21
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_30_war_of_kings
###############################################################################
# =============================================================================
# gen_30_war_of_kings — 14:1-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_30_war_of_kings.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The war of the kings: the annal, the rescue, the priest, the refused spoils (14:1-24)"""
from machine import Machine

m = Machine("gen_30_war_of_kings")

# -------------------------- Gen.14.1 · THE_COALITION_AND_THE_VALE ----------
# וַיְהִי בִּימֵי אַמְרָפֶל מֶלֶךְ־שִׁנְעָר אַרְיוֹךְ מֶלֶךְ אֶלָּסָר
# כְּדָרְלָעֹמֶר מֶלֶךְ עֵילָם וְתִדְעָל מֶלֶךְ גּוֹיִם … כָּל־אֵלֶּה
# חָבְרוּ אֶל־עֵמֶק הַשִּׂדִּים הוּא יָם הַמֶּלַח
# "[EN-AID/JPS 14:1-3] And it came to pass in the days of Amraphel king of
# Shinar, Arioch king of Ellasar, Chedorlaomer king of Elam, and Tidal king
# of Goiim, that they made war with Bera king of Sodom, and with Birsha king
# of Gomorrah, Shinab king of Admah, and Shemeber king of Zeboiim, and the
# king of Bela — the same is Zoar. All these came as allies unto the vale of
# Siddim — the same is the Salt Sea."
m.step("Gen.14.1")
# ‹עָשׂוּ מִלְחָמָה אֶת־בֶּרַע מֶלֶךְ סְדֹם› event: make-war — agent arbaat-
# the-melakhim
m.event("make_war", agent="arbaat_ha_melakhim")
# ‹כָּל־אֵלֶּה חָבְרוּ אֶל־עֵמֶק הַשִּׂדִּים הוּא יָם הַמֶּלַח› fact holds:
# all-these-chavru-to-emeq-the-sidim-that-yam-the-melach
m.fact("kol_eleh_chavru_el_emeq_ha_sidim_hu_yam_ha_melach")
# reads without prior install (flag, not fix): shinar, elasar, elam, sedom,
# amora, admah, tzevoyim, tzoar, emeq-the-sidim, yam-the-melach
m.presupposed("shinar", "elasar", "elam", "sedom", "amora", "admah", "tzevoyim", "tzoar", "emeq_ha_sidim", "yam_ha_melach")

# -------------------------- Gen.14.4 · THE_CLOCK_AND_THE_SWEEP -------------
# שְׁתֵּים עֶשְׂרֵה שָׁנָה עָבְדוּ אֶת־כְּדָרְלָעֹמֶר וּשְׁלֹשׁ־עֶשְׂרֵה
# שָׁנָה מָרָדוּ … וַיַּכּוּ אֶת־כָּל־שְׂדֵה הָעֲמָלֵקִי וְגַם אֶת־הָאֱמֹרִי
# הַיֹּשֵׁב בְּחַצְצֹן תָּמָר
# "[EN-AID/JPS 14:4-7] Twelve years they served Chedorlaomer, and in the
# thirteenth year they rebelled. And in the fourteenth year came
# Chedorlaomer and the kings that were with him, and smote the Rephaim in
# Ashteroth-karnaim, and the Zuzim in Ham, and the Emim in Shaveh-
# kiriathaim, and the Horites in their mount Seir, unto El-paran, which is
# by the wilderness. And they turned back, and came to En-mishpat — the same
# is Kadesh — and smote all the country of the Amalekites, and also the
# Amorites, that dwelt in Hazazon-tamar."
m.step("Gen.14.4")
# ‹שְׁתֵּים עֶשְׂרֵה שָׁנָה עָבְדוּ … וּשְׁלֹשׁ־עֶשְׂרֵה שָׁנָה מָרָדוּ›
# fact holds: shtem--teen-year-avdu-kedarlaomer-and-shelosh--teen-maradu
m.fact("shtem_esreh_shanah_avdu_et_kedarlaomer_u_shelosh_esreh_maradu")
# ‹וַיַּכּוּ אֶת־רְפָאִים … וְאֶת־הַזּוּזִים … וְאֵת הָאֵימִים …
# וְאֶת־הַחֹרִי … אֶת־כָּל־שְׂדֵה הָעֲמָלֵקִי וְגַם אֶת־הָאֱמֹרִי› event:
# strike — agent kedarlaomer-and-the-melakhim; theme refaim-zuzim-emim-
# chori-amaleqi-emori
m.event("strike", agent="kedarlaomer_ve_ha_melakhim", themes=["refaim_zuzim_emim_chori_amaleqi_emori"])
# reads without prior install (flag, not fix): ashterot-qarnayim, ham,
# shaveh-qiryatayim, har-seir, to-paran, en-mishpat-qadesh, chatzetzon-tamar
m.presupposed("ashterot_qarnayim", "ham", "shaveh_qiryatayim", "har_seir", "el_paran", "en_mishpat_qadesh", "chatzetzon_tamar")

# -------------------------- Gen.14.8 · THE_BATTLE_THE_PITS_THE_PLUNDER -----
# וַיֵּצֵא מֶלֶךְ־סְדֹם … וַיַּעַרְכוּ אִתָּם מִלְחָמָה בְּעֵמֶק הַשִּׂדִּים
# … אַרְבָּעָה מְלָכִים אֶת־הַחֲמִשָּׁה … וַיִּקְחוּ אֶת־כָּל־רְכֻשׁ סְדֹם
# וַעֲמֹרָה וְאֶת־כָּל־אָכְלָם וַיֵּלֵכוּ
# "[EN-AID/JPS 14:8-11] And there went out the king of Sodom... and they set
# the battle in array against them in the vale of Siddim; against
# Chedorlaomer... four kings against the five. Now the vale of Siddim was
# full of slime pits; and the kings of Sodom and Gomorrah fled, and they
# fell there, and they that remained fled to the mountain. And they took all
# the goods of Sodom and Gomorrah, and all their victuals, and went their
# way."
m.step("Gen.14.8")
# ‹וַיַּעַרְכוּ אִתָּם מִלְחָמָה› event: array-battle — agent chameshet-the-
# melakhim
m.event("array_battle", agent="chameshet_ha_melakhim")
# ‹אַרְבָּעָה מְלָכִים אֶת־הַחֲמִשָּׁה … וְעֵמֶק הַשִׂדִּים בֶּאֱרֹת
# בֶּאֱרֹת חֵמָר› fact holds: four-melakhim-the-chamishah; emeq-the-sidim-
# beerot-beerot-chemar
m.fact("arbaah_melakhim_et_ha_chamishah",
       "emeq_ha_sidim_beerot_beerot_chemar")
# ‹וַיָּנֻסוּ מֶלֶךְ־סְדֹם וַעֲמֹרָה וַיִּפְּלוּ־שָׁמָּה› event: flee —
# agent melekh-sedom-and-amorah
m.event("flee", agent="melekh_sedom_va_amorah")
# ‹וַיִּקְחוּ אֶת־כָּל־רְכֻשׁ סְדֹם וַעֲמֹרָה וְאֶת־כָּל־אָכְלָם וַיֵּלֵכוּ›
# event: take — agent arbaat-the-melakhim; theme all-rekhush-sedom-and-
# amorah
m.event("take", agent="arbaat_ha_melakhim", themes=["kol_rekhush_sedom_va_amorah"])
# reads without prior install (flag, not fix): goyim-land
m.presupposed("goyim_land")

# -------------------------- Gen.14.12 · THE_TAKING_OF_LOT ------------------
# וַיִּקְחוּ אֶת־לוֹט וְאֶת־רְכֻשׁוֹ בֶּן־אֲחִי אַבְרָם וַיֵּלֵכוּ וְהוּא
# יֹשֵׁב בִּסְדֹם
# "And they took Lot, Abram's brother's son, who dwelt in Sodom, and his
# goods, and departed."
m.step("Gen.14.12")
# ‹וַיִּקְחוּ אֶת־לוֹט וְאֶת־רְכֻשׁוֹ› event: take — agent arbaat-the-
# melakhim; theme lot
m.event("take", agent="arbaat_ha_melakhim", themes=["lot"])
# ‹וְהוּא יֹשֵׁב בִּסְדֹם› fact holds: and-that-yoshev-bi-sedom
m.fact("ve_hu_yoshev_bi_sedom")

# -------------------------- Gen.14.13 · THE_REFUGEE_AND_THE_HEBREW ---------
# וַיָּבֹא הַפָּלִיט וַיַּגֵּד לְאַבְרָם הָעִבְרִי וְהוּא שֹׁכֵן בְּאֵלֹנֵי
# מַמְרֵא הָאֱמֹרִי אֲחִי אֶשְׁכֹּל וַאֲחִי עָנֵר וְהֵם בַּעֲלֵי
# בְרִית־אַבְרָם
# "And there came one that had escaped, and told Abram the Hebrew — now he
# dwelt by the terebinths of Mamre the Amorite, brother of Eshcol, and
# brother of Aner; and these were confederate with Abram."
m.step("Gen.14.13")
# ‹וַיָּבֹא הַפָּלִיט› event: come — agent the-palit
m.event("come", agent="ha_palit")
# ‹וַיַּגֵּד לְאַבְרָם הָעִבְרִי› event: tell — agent the-palit
m.event("tell", agent="ha_palit")
# ‹וְהֵם בַּעֲלֵי בְרִית־אַבְרָם› fact holds: and-hem-baalei-verit-avram
m.fact("ve_hem_baalei_verit_avram")

# -------------------------- Gen.14.14 · THE_MUSTER_OF_THE_318 --------------
# וַיִּשְׁמַע אַבְרָם כִּי נִשְׁבָּה אָחִיו וַיָּרֶק אֶת־חֲנִיכָיו יְלִידֵי
# בֵיתוֹ שְׁמֹנָה עָשָׂר וּשְׁלֹשׁ מֵאוֹת וַיִּרְדֹּף עַד־דָּן
# "And when Abram heard that his brother was taken captive, he led forth his
# trained men, born in his house, three hundred and eighteen, and pursued as
# far as Dan."
m.step("Gen.14.14")
# ‹וַיִּשְׁמַע אַבְרָם כִּי נִשְׁבָּה אָחִיו› event: hear — agent avram
m.event("hear", agent="avram")
# ‹וַיָּרֶק אֶת־חֲנִיכָיו יְלִידֵי בֵיתוֹ› event: muster — agent avram;
# theme chanikhav
m.event("muster", agent="avram", themes=["chanikhav"])
# ‹שְׁמֹנָה עָשָׂר וּשְׁלֹשׁ מֵאוֹת› fact holds: chanikhav-yelidei-veito-
# shmonah-asar-and-shelosh-meot
m.fact("chanikhav_yelidei_veito_shmonah_asar_u_shelosh_meot")
# ‹וַיִּרְדֹּף עַד־דָּן› event: pursue — agent avram
m.event("pursue", agent="avram")
# reads without prior install (flag, not fix): dan
m.presupposed("dan")

# -------------------------- Gen.14.15 · THE_NIGHT_SPLIT --------------------
# וַיֵּחָלֵק עֲלֵיהֶם לַיְלָה הוּא וַעֲבָדָיו וַיַּכֵּם וַיִּרְדְּפֵם
# עַד־חוֹבָה אֲשֶׁר מִשְּׂמֹאל לְדַמָּשֶׂק
# "And he divided himself against them by night, he and his servants, and
# smote them, and pursued them unto Hobah, which is on the left hand of
# Damascus."
m.step("Gen.14.15")
# ‹וַיֵּחָלֵק עֲלֵיהֶם לַיְלָה› event: split — agent avram-and-avadav
m.event("split", agent="avram_va_avadav")
# ‹וַיַּכֵּם› event: strike — agent avram-and-avadav
m.event("strike", agent="avram_va_avadav")
# ‹וַיִּרְדְּפֵם עַד־חוֹבָה אֲשֶׁר מִשְּׂמֹאל לְדַמָּשֶׂק› event: pursue —
# agent avram-and-avadav
m.event("pursue", agent="avram_va_avadav")
# reads without prior install (flag, not fix): chovah, damaseq
m.presupposed("chovah", "damaseq")

# -------------------------- Gen.14.16 · THE_BRINGING_BACK ------------------
# וַיָּשֶׁב אֵת כָּל־הָרְכֻשׁ וְגַם אֶת־לוֹט אָחִיו וּרְכֻשׁוֹ הֵשִׁיב וְגַם
# אֶת־הַנָּשִׁים וְאֶת־הָעָם
# "And he brought back all the goods, and also brought back his brother Lot,
# and his goods, and the women also, and the people."
m.step("Gen.14.16")
# ‹וַיָּשֶׁב אֵת כָּל־הָרְכֻשׁ … הֵשִׁיב› event: bring-back — agent avram;
# theme all-the-rekhush-and-lot-and-the-nashim-and-the-am
m.event("bring_back", agent="avram", themes=["kol_ha_rekhush_ve_lot_ve_ha_nashim_ve_ha_am"])

# -------------------------- Gen.14.17 · THE_KINGS_MEETING ------------------
# וַיֵּצֵא מֶלֶךְ־סְדֹם לִקְרָאתוֹ אַחֲרֵי שׁוּבוֹ מֵהַכּוֹת
# אֶת־כְּדָרלָעֹמֶר וְאֶת־הַמְּלָכִים אֲשֶׁר אִתּוֹ אֶל־עֵמֶק שָׁוֵה הוּא
# עֵמֶק הַמֶּלֶךְ
# "And the king of Sodom went out to meet him, after his return from the
# slaughter of Chedorlaomer and the kings that were with him, at the vale of
# Shaveh — the same is the King's Vale."
m.step("Gen.14.17")
# ‹וַיֵּצֵא מֶלֶךְ־סְדֹם לִקְרָאתוֹ› event: go-out — agent melekh-sedom
m.event("go_out", agent="melekh_sedom")
# reads without prior install (flag, not fix): emeq-shaveh
m.presupposed("emeq_shaveh")

# -------------------------- Gen.14.18 · BREAD_WINE_AND_A_PRIEST ------------
# וּמַלְכִּי־צֶדֶק מֶלֶךְ שָׁלֵם הוֹצִיא לֶחֶם וָיָיִן וְהוּא כֹהֵן לְאֵל
# עֶלְיוֹן
# "And Melchizedek king of Salem brought forth bread and wine; and he was
# priest of God the Most High."
m.step("Gen.14.18")
# ‹הוֹצִיא לֶחֶם וָיָיִן› event: bring-out — agent malki-tzedeq; theme
# lechem-and-yayin
m.event("bring_out", agent="malki_tzedeq", themes=["lechem_va_yayin"])
# ‹וְהוּא כֹהֵן לְאֵל עֶלְיוֹן› fact holds: and-that-khohen-to-to-elyon
m.fact("ve_hu_khohen_le_el_elyon")
# reads without prior install (flag, not fix): shalem
m.presupposed("shalem")

# -------------------------- Gen.14.19 · THE_BLESSING_OF_ABRAM --------------
# וַיְבָרְכֵהוּ וַיֹּאמַר בָּרוּךְ אַבְרָם לְאֵל עֶלְיוֹן קֹנֵה שָׁמַיִם
# וָאָרֶץ
# "And he blessed him, and said: 'Blessed be Abram of God Most High, Maker
# of heaven and earth;"
m.step("Gen.14.19")
# ‹וַיְבָרְכֵהוּ› blessing: malki-tzedeq blesses avram
m.bless("malki_tzedeq", "avram")
# ‹בָּרוּךְ אַבְרָם לְאֵל עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ› fact holds:
# barukh-avram-to-to-elyon-qoneh-heavens-and-earth
m.fact("barukh_avram_le_el_elyon_qoneh_shamayim_va_aretz")

# -------------------------- Gen.14.20 · THE_BLESSING_OF_EL_ELYON_AND_THE_TENTH -
# וּבָרוּךְ אֵל עֶלְיוֹן אֲשֶׁר־מִגֵּן צָרֶיךָ בְּיָדֶךָ וַיִּתֶּן־לוֹ
# מַעֲשֵׂר מִכֹּל
# "and blessed be God the Most High, who hath delivered thine enemies into
# thy hand.' And he gave him a tenth of all."
m.step("Gen.14.20")
# ‹וּבָרוּךְ אֵל עֶלְיוֹן› blessing: malki-tzedeq blesses to-elyon
m.bless("malki_tzedeq", "el_elyon")
# ‹אֲשֶׁר־מִגֵּן צָרֶיךָ בְּיָדֶךָ› fact holds: which-miggen-tzarekha-in-
# yadekha
m.fact("asher_miggen_tzarekha_be_yadekha")
# ‹וַיִּתֶּן־לוֹ מַעֲשֵׂר מִכֹּל› event: give — theme maaser-from-all
m.event("give", themes=["maaser_mi_kol"])

# -------------------------- Gen.14.21 · THE_KINGS_DEMANDS ------------------
# וַיֹּאמֶר מֶלֶךְ־סְדֹם אֶל־אַבְרָם תֶּן־לִי הַנֶּפֶשׁ וְהָרְכֻשׁ קַח־לָךְ
# "And the king of Sodom said unto Abram: 'Give me the persons, and take the
# goods to thyself.'"
m.step("Gen.14.21")
# ‹וַיֹּאמֶר מֶלֶךְ־סְדֹם אֶל־אַבְרָם› event: say — agent melekh-sedom
m.event("say", agent="melekh_sedom")
# ‹תֶּן־לִי הַנֶּפֶשׁ› melekh-sedom speaks a demand — LET: ten(avram, the-
# nefesh)
m.declare("melekh_sedom", "LET",
          "ten(avram, ha_nefesh)")
# ‹וְהָרְכֻשׁ קַח־לָךְ› melekh-sedom speaks a demand — LET: qach(avram, the-
# rekhush)
m.declare("melekh_sedom", "LET",
          "qach(avram, ha_rekhush)")

# -------------------------- Gen.14.22 · THE_RAISED_HAND --------------------
# וַיֹּאמֶר אַבְרָם אֶל־מֶלֶךְ סְדֹם הֲרִימֹתִי יָדִי אֶל־יְהוָה אֵל
# עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ
# "And Abram said to the king of Sodom: 'I have lifted up my hand unto the
# LORD, God Most High, Maker of heaven and earth,"
m.step("Gen.14.22")
# ‹וַיֹּאמֶר אַבְרָם אֶל־מֶלֶךְ סְדֹם› event: say — agent avram
m.event("say", agent="avram")
# ‹הֲרִימֹתִי יָדִי אֶל־יְהוָה אֵל עֶלְיוֹן קֹנֵה שָׁמַיִם וָאָרֶץ› fact
# holds: harimoti-yadi-to-the-LORD-to-elyon-qoneh-heavens-and-earth
m.fact("harimoti_yadi_el_YHWH_el_elyon_qoneh_shamayim_va_aretz")

# -------------------------- Gen.14.23 · THE_THREAD_AND_THE_THONG -----------
# אִם־מִחוּט וְעַד שְׂרוֹךְ־נַעַל וְאִם־אֶקַּח מִכָּל־אֲשֶׁר־לָךְ וְלֹא
# תֹאמַר אֲנִי הֶעֱשַׁרְתִּי אֶת־אַבְרָם
# "that I will not take a thread nor a shoe-latchet nor aught that is thine,
# lest thou shouldest say: I have made Abram rich;"
m.step("Gen.14.23")
# ‹אִם־מִחוּט וְעַד שְׂרוֹךְ־נַעַל וְאִם־אֶקַּח … וְלֹא תֹאמַר אֲנִי
# הֶעֱשַׁרְתִּי אֶת־אַבְרָם› fact holds: if-from-chut-and-until-serokh-naal-
# and-if-eqach-from-all-which-to-you; and-not-tomar-ani-heesharti-avram
m.fact("im_mi_chut_ve_ad_serokh_naal_ve_im_eqach_mi_kol_asher_lakh",
       "ve_lo_tomar_ani_heesharti_et_avram")

# -------------------------- Gen.14.24 · THE_EXCEPTION_AND_THE_PORTION ------
# בִּלְעָדַי רַק אֲשֶׁר אָכְלוּ הַנְּעָרִים וְחֵלֶק הָאֲנָשִׁים אֲשֶׁר
# הָלְכוּ אִתִּי עָנֵר אֶשְׁכֹּל וּמַמְרֵא הֵם יִקְחוּ חֶלְקָם
# "save only that which the young men have eaten, and the portion of the men
# which went with me, Aner, Eshcol, and Mamre, let them take their
# portion.'"
m.step("Gen.14.24")
# ‹בִּלְעָדַי רַק אֲשֶׁר אָכְלוּ הַנְּעָרִים› fact holds: biladai-raq-which-
# akhlu-the-nearim
m.fact("biladai_raq_asher_akhlu_ha_nearim")
# ‹עָנֵר אֶשְׁכֹּל וּמַמְרֵא הֵם יִקְחוּ חֶלְקָם› avram speaks a demand —
# LET: yiqchu(aner-eshkol-mamre, chelqam)
m.declare("avram", "LET",
          "yiqchu(aner_eshkol_mamre, chelqam)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'shinar', 'elam', 'en_mishpat_qadesh', 'ashterot_qarnayim', 'admah', 'chovah', 'chatzetzon_tamar', 'dan', 'ham', 'har_seir', 'goyim_land', 'shaveh_qiryatayim', 'yam_ha_melach', 'shalem', 'emeq_shaveh', 'elasar', 'tzevoyim', 'el_paran', 'amora', 'sedom', 'tzoar', 'damaseq', 'emeq_ha_sidim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['ten(avram, ha_nefesh)', 'qach(avram, ha_rekhush)', 'yiqchu(aner_eshkol_mamre, chelqam)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 23}
    assert sorted(m.WORLD["facts"]) == sorted(['kol_eleh_chavru_el_emeq_ha_sidim_hu_yam_ha_melach', 'shtem_esreh_shanah_avdu_et_kedarlaomer_u_shelosh_esreh_maradu', 'arbaah_melakhim_et_ha_chamishah', 'emeq_ha_sidim_beerot_beerot_chemar', 've_hu_yoshev_bi_sedom', 've_hem_baalei_verit_avram', 'chanikhav_yelidei_veito_shmonah_asar_u_shelosh_meot', 've_hu_khohen_le_el_elyon', 'barukh_avram_le_el_elyon_qoneh_shamayim_va_aretz', 'asher_miggen_tzarekha_be_yadekha', 'harimoti_yadi_el_YHWH_el_elyon_qoneh_shamayim_va_aretz', 'im_mi_chut_ve_ad_serokh_naal_ve_im_eqach_mi_kol_asher_lakh', 've_lo_tomar_ani_heesharti_et_avram', 'biladai_raq_asher_akhlu_ha_nearim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 25
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_31_covenant_pieces
###############################################################################
# =============================================================================
# gen_31_covenant_pieces — 15:1-21
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_31_covenant_pieces.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The covenant of the pieces: the vision, the stars, the rite, the decree, the grant (15:1-21)"""
from machine import Machine

m = Machine("gen_31_covenant_pieces")

# -------------------------- Gen.15.1 · THE_WORD_THE_SHIELD_AND_THE_FEAR_NOT -
# אַחַר הַדְּבָרִים הָאֵלֶּה הָיָה דְבַר־יְהוָה אֶל־אַבְרָם בַּמַּחֲזֶה
# לֵאמֹר אַל־תִּירָא אַבְרָם אָנֹכִי מָגֵן לָךְ שְׂכָרְךָ הַרְבֵּה מְאֹד
# "After these things the word of the LORD came unto Abram in a vision,
# saying: 'Fear not, Abram, I am thy shield, thy reward shall be exceeding
# great.'"
m.step("Gen.15.1")
# ‹הָיָה דְבַר־יְהוָה אֶל־אַבְרָם בַּמַּחֲזֶה› event: come — theme devar-
# the-LORD
m.event("come", themes=["devar_YHWH"])
# ‹אַל־תִּירָא אַבְרָם› the-LORD speaks a demand — LET-NOT: tira(avram)
m.declare("YHWH", "LET-NOT",
          "tira(avram)")
# ‹אָנֹכִי מָגֵן לָךְ שְׂכָרְךָ הַרְבֵּה מְאֹד› fact holds: anokhi-magen-to-
# you; sekharkha-harbeh-very
m.fact("anokhi_magen_lakh",
       "sekharkha_harbeh_meod")

# -------------------------- Gen.15.2 · THE_FIRST_SPEECH_TO_GOD -------------
# וַיֹּאמֶר אַבְרָם אֲדֹנָי יֱהוִה מַה־תִּתֶּן־לִי וְאָנֹכִי הוֹלֵךְ
# עֲרִירִי וּבֶן־מֶשֶׁק בֵּיתִי הוּא דַּמֶּשֶׂק אֱלִיעֶזֶר
# "And Abram said: 'O Lord GOD, what wilt Thou give me, seeing I go hence
# childless, and he that shall be possessor of my house is Eliezer of
# Damascus?'"
m.step("Gen.15.2")
# ‹וַיֹּאמֶר אַבְרָם אֲדֹנָי יֱהוִה› event: say — agent avram
m.event("say", agent="avram")
# ‹מַה־תִּתֶּן־לִי וְאָנֹכִי הוֹלֵךְ עֲרִירִי וּבֶן־מֶשֶׁק בֵּיתִי הוּא
# דַּמֶּשֶׂק אֱלִיעֶזֶר› fact holds: mah-titen-to-me-and-anokhi-holekh-
# ariri; ben-mesheq-beti-that-dameseq-eliezer
m.fact("mah_titen_li_ve_anokhi_holekh_ariri",
       "ben_mesheq_beti_hu_dameseq_eliezer")
# reads without prior install (flag, not fix): dameseq
m.presupposed("dameseq")

# -------------------------- Gen.15.3 · THE_COMPLAINT_RELAUNCHED ------------
# וַיֹּאמֶר אַבְרָם הֵן לִי לֹא נָתַתָּה זָרַע וְהִנֵּה בֶן־בֵּיתִי יוֹרֵשׁ
# אֹתִי
# "And Abram said: 'Behold, to me Thou hast given no seed, and, lo, one born
# in my house is to be mine heir.'"
m.step("Gen.15.3")
# ‹וַיֹּאמֶר אַבְרָם› event: say — agent avram
m.event("say", agent="avram")
# ‹הֵן לִי לֹא נָתַתָּה זָרַע וְהִנֵּה בֶן־בֵּיתִי יוֹרֵשׁ אֹתִי› fact
# holds: hen-to-me-not-natata-zara; ben-beti-yoresh-me
m.fact("hen_li_lo_natata_zara",
       "ben_beti_yoresh_oti")

# -------------------------- Gen.15.4 · THE_HEIR_CORRECTION -----------------
# וְהִנֵּה דְבַר־יְהוָה אֵלָיו לֵאמֹר לֹא יִירָשְׁךָ זֶה כִּי־אִם אֲשֶׁר
# יֵצֵא מִמֵּעֶיךָ הוּא יִירָשֶׁךָ
# "And, behold, the word of the LORD came unto him, saying: 'This man shall
# not be thine heir; but he that shall come forth out of thine own bowels
# shall be thine heir.'"
m.step("Gen.15.4")
# ‹וְהִנֵּה דְבַר־יְהוָה אֵלָיו לֵאמֹר› event: come — theme devar-the-LORD
m.event("come", themes=["devar_YHWH"])
# ‹לֹא יִירָשְׁךָ זֶה כִּי־אִם אֲשֶׁר יֵצֵא מִמֵּעֶיךָ הוּא יִירָשֶׁךָ› fact
# holds: not-yirashkha-this; which-yetze-from-meekha-that-yirashekha
m.fact("lo_yirashkha_zeh",
       "asher_yetze_mi_meekha_hu_yirashekha")

# -------------------------- Gen.15.5 · THE_STARS_AND_THE_COUNT_COMMAND -----
# וַיּוֹצֵא אֹתוֹ הַחוּצָה וַיֹּאמֶר הַבֶּט־נָא הַשָּׁמַיְמָה וּסְפֹר
# הַכּוֹכָבִים אִם־תּוּכַל לִסְפֹּר אֹתָם וַיֹּאמֶר לוֹ כֹּה יִהְיֶה
# זַרְעֶךָ
# "And He brought him forth abroad, and said: 'Look now toward heaven, and
# count the stars, if thou be able to count them'; and He said unto him: 'So
# shall thy seed be.'"
m.step("Gen.15.5")
# ‹וַיּוֹצֵא אֹתוֹ הַחוּצָה› event: bring-out — agent the-LORD; theme avram
m.event("bring_out", agent="YHWH", themes=["avram"])
# ‹וַיֹּאמֶר› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹הַבֶּט־נָא הַשָּׁמַיְמָה וּסְפֹר הַכּוֹכָבִים› the-LORD speaks a demand —
# LET: habet-and-sefor(avram, the-shamaymah-and-the-stars)
m.declare("YHWH", "LET",
          "habet_u_sefor(avram, ha_shamaymah_ve_ha_kokhavim)")
# ‹וַיֹּאמֶר לוֹ› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹כֹּה יִהְיֶה זַרְעֶךָ› fact holds: koh-yihyeh-zarekha
m.fact("koh_yihyeh_zarekha")

# -------------------------- Gen.15.6 · THE_BELIEF_AND_THE_RECKONING --------
# וְהֶאֱמִן בַּיהוָה וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה
# "And he believed in the LORD; and He counted it to him for righteousness."
m.step("Gen.15.6")
# ‹וְהֶאֱמִן בַּיהוָה וַיַּחְשְׁבֶהָ לּוֹ צְדָקָה› fact holds: and-heemin-
# in-the-the-LORD; and-yachsheveha-not-tzedaqah
m.fact("ve_heemin_ba_YHWH",
       "va_yachsheveha_lo_tzedaqah")

# -------------------------- Gen.15.7 · ANI_YHWH_THE_SELF_NAMING ------------
# וַיֹּאמֶר אֵלָיו אֲנִי יְהוָה אֲשֶׁר הוֹצֵאתִיךָ מֵאוּר כַּשְׂדִּים לָתֶת
# לְךָ אֶת־הָאָרֶץ הַזֹּאת לְרִשְׁתָּהּ
# "And He said unto him: 'I am the LORD that brought thee out of Ur of the
# Chaldees, to give thee this land to inherit it.'"
m.step("Gen.15.7")
# ‹וַיֹּאמֶר אֵלָיו› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹אֲנִי יְהוָה אֲשֶׁר הוֹצֵאתִיךָ מֵאוּר כַּשְׂדִּים לָתֶת לְךָ אֶת־הָאָרֶץ
# הַזֹּאת לְרִשְׁתָּהּ› fact holds: ani-the-LORD-which-hotzetikha-from-ur-
# kasdim; to-tet-to-you-the-earth-the-this-to-rishtah
m.fact("ani_YHWH_asher_hotzetikha_me_ur_kasdim",
       "la_tet_lekha_et_ha_aretz_ha_zot_le_rishtah")
# reads without prior install (flag, not fix): ur-kasdim
m.presupposed("ur_kasdim")

# -------------------------- Gen.15.8 · THE_SECOND_QUESTION -----------------
# וַיֹּאמַר אֲדֹנָי יֱהוִה בַּמָּה אֵדַע כִּי אִירָשֶׁנָּה
# "And he said: 'O Lord GOD, whereby shall I know that I shall inherit it?'"
m.step("Gen.15.8")
# ‹וַיֹּאמַר› event: say — agent avram
m.event("say", agent="avram")
# ‹אֲדֹנָי יֱהוִה בַּמָּה אֵדַע כִּי אִירָשֶׁנָּה› fact holds: in-the-mah-
# eda-when-irashena
m.fact("ba_mah_eda_ki_irashena")

# -------------------------- Gen.15.9 · THE_TAKE_COMMAND --------------------
# וַיֹּאמֶר אֵלָיו קְחָה לִי עֶגְלָה מְשֻׁלֶּשֶׁת וְעֵז מְשֻׁלֶּשֶׁת וְאַיִל
# מְשֻׁלָּשׁ וְתֹר וְגוֹזָל
# "And He said unto him: 'Take Me a heifer of three years old, and a she-
# goat of three years old, and a ram of three years old, and a turtle-dove,
# and a young pigeon.'"
m.step("Gen.15.9")
# ‹וַיֹּאמֶר אֵלָיו› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹קְחָה לִי עֶגְלָה מְשֻׁלֶּשֶׁת וְעֵז מְשֻׁלֶּשֶׁת וְאַיִל מְשֻׁלָּשׁ
# וְתֹר וְגוֹזָל› the-LORD speaks a demand — LET: qechah(avram, eglah-ez-
# ayil-tor-and-gozal)
m.declare("YHWH", "LET",
          "qechah(avram, eglah_ez_ayil_tor_ve_gozal)")

# -------------------------- Gen.15.10 · THE_COMPLIANCE_AND_THE_CUTTING -----
# וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה וַיְבַתֵּר אֹתָם בַּתָּוֶךְ וַיִּתֵּן
# אִישׁ־בִּתְרוֹ לִקְרַאת רֵעֵהוּ וְאֶת־הַצִפֹּר לֹא בָתָר
# "And he took him all these, and divided them in the midst, and laid each
# half over against the other; but the birds divided he not."
m.step("Gen.15.10")
# ‹וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה› event: take — agent avram; theme all-these
m.event("take", agent="avram", themes=["kol_eleh"])
# ‹וַיִּקַּח־לוֹ אֶת־כָּל־אֵלֶּה› demand settled (popped from the queue):
# qechah(avram, eglah-ez-ayil-tor-and-gozal)
m.result("qechah(avram, eglah_ez_ayil_tor_ve_gozal)", tmark="t1")
# ‹וַיְבַתֵּר אֹתָם בַּתָּוֶךְ› event: cut — agent avram; theme the-behemot
m.event("cut", agent="avram", themes=["ha_behemot"])
# ‹וַיִּתֵּן אִישׁ־בִּתְרוֹ לִקְרַאת רֵעֵהוּ› event: give — agent avram;
# theme man-bitro
m.event("give", agent="avram", themes=["ish_bitro"])
# ‹וְאֶת־הַצִפֹּר לֹא בָתָר› fact holds: and-the-tzipor-not-vatar
m.fact("ve_et_ha_tzipor_lo_vatar")

# -------------------------- Gen.15.11 · THE_VULTURES_DRIVEN_OFF ------------
# וַיֵּרֶד הָעַיִט עַל־הַפְּגָרִים וַיַּשֵּׁב אֹתָם אַבְרָם
# "And the birds of prey came down upon the carcasses, and Abram drove them
# away."
m.step("Gen.15.11")
# ‹וַיֵּרֶד הָעַיִט עַל־הַפְּגָרִים› event: descend — agent the-ayit
m.event("descend", agent="ha_ayit")
# ‹וַיַּשֵּׁב אֹתָם אַבְרָם› event: drive-off — agent avram; theme the-ayit
m.event("drive_off", agent="avram", themes=["ha_ayit"])

# -------------------------- Gen.15.12 · THE_SLEEP_AND_THE_DREAD ------------
# וַיְהִי הַשֶּׁמֶשׁ לָבוֹא וְתַרְדֵּמָה נָפְלָה עַל־אַבְרָם וְהִנֵּה אֵימָה
# חֲשֵׁכָה גְדֹלָה נֹפֶלֶת עָלָיו
# "And it came to pass, that, when the sun was going down, a deep sleep fell
# upon Abram; and, lo, a dread, even a great darkness, fell upon him."
m.step("Gen.15.12")
# ‹וְתַרְדֵּמָה נָפְלָה עַל־אַבְרָם› event: fall — theme deep-sleep
m.event("fall", themes=["tardemah"])
# ‹וְהִנֵּה אֵימָה חֲשֵׁכָה גְדֹלָה נֹפֶלֶת עָלָיו› fact holds: emah-
# chashekhah-gedolah-nofelet-alav
m.fact("emah_chashekhah_gedolah_nofelet_alav")

# -------------------------- Gen.15.13 · THE_DECREE_SOJOURN_SERVE_AFFLICT ---
# וַיֹּאמֶר לְאַבְרָם יָדֹעַ תֵּדַע כִּי־גֵר יִהְיֶה זַרְעֲךָ בְּאֶרֶץ לֹא
# לָהֶם וַעֲבָדוּם וְעִנּוּ אֹתָם אַרְבַּע מֵאוֹת שָׁנָה
# "And He said unto Abram: 'Know of a surety that thy seed shall be a
# stranger in a land that is not theirs, and shall serve them; and they
# shall afflict them four hundred years;"
m.step("Gen.15.13")
# ‹וַיֹּאמֶר לְאַבְרָם יָדֹעַ תֵּדַע› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹כִּי־גֵר יִהְיֶה זַרְעֲךָ בְּאֶרֶץ לֹא לָהֶם וַעֲבָדוּם וְעִנּוּ אֹתָם
# אַרְבַּע מֵאוֹת שָׁנָה› fact holds: ger-yihyeh-zarakha-in-earth-not-to-
# them; and-avadum-and-inu-otam-arba-meot-year
m.fact("ger_yihyeh_zarakha_be_eretz_lo_lahem",
       "va_avadum_ve_inu_otam_arba_meot_shanah")

# -------------------------- Gen.15.14 · THE_JUDGMENT_AND_THE_EXODUS_WEALTH -
# וְגַם אֶת־הַגּוֹי אֲשֶׁר יַעֲבֹדוּ דָּן אָנֹכִי וְאַחֲרֵי־כֵן יֵצְאוּ
# בִּרְכֻשׁ גָּדוֹל
# "and also that nation, whom they shall serve, will I judge; and afterward
# shall they come out with great substance."
m.step("Gen.15.14")
# ‹וְגַם אֶת־הַגּוֹי אֲשֶׁר יַעֲבֹדוּ דָּן אָנֹכִי וְאַחֲרֵי־כֵן יֵצְאוּ
# בִּרְכֻשׁ גָּדוֹל› fact holds: dan-anokhi-the-goy-which-yaavodu; and-
# acharei-so-yetzu-bi-rekhush-gadol
m.fact("dan_anokhi_et_ha_goy_asher_yaavodu",
       "ve_acharei_khen_yetzu_bi_rekhush_gadol")

# -------------------------- Gen.15.15 · THE_PEACE_AND_THE_BURIAL -----------
# וְאַתָּה תָּבוֹא אֶל־אֲבֹתֶיךָ בְּשָׁלוֹם תִּקָּבֵר בְּשֵׂיבָה טוֹבָה
# "But thou shalt go to thy fathers in peace; thou shalt be buried in a good
# old age."
m.step("Gen.15.15")
# ‹וְאַתָּה תָּבוֹא אֶל־אֲבֹתֶיךָ בְּשָׁלוֹם תִּקָּבֵר בְּשֵׂיבָה טוֹבָה›
# fact holds: tavo-to-avotekha-in-shalom; tiqaver-in-sevah-tovah
m.fact("tavo_el_avotekha_be_shalom",
       "tiqaver_be_sevah_tovah")

# -------------------------- Gen.15.16 · THE_FOURTH_GENERATION_AND_THE_UNFULL_INIQUITY -
# וְדוֹר רְבִיעִי יָשׁוּבוּ הֵנָּה כִּי לֹא־שָׁלֵם עֲוֺן הָאֱמֹרִי
# עַד־הֵנָּה
# "And in the fourth generation they shall come back hither; for the
# iniquity of the Amorite is not yet full.'"
m.step("Gen.15.16")
# ‹וְדוֹר רְבִיעִי יָשׁוּבוּ הֵנָּה כִּי לֹא־שָׁלֵם עֲוֺן הָאֱמֹרִי
# עַד־הֵנָּה› fact holds: and-dor-revii-yashuvu-henah; not-shalem-avon-the-
# emori-until-henah
m.fact("ve_dor_revii_yashuvu_henah",
       "lo_shalem_avon_ha_emori_ad_henah")

# -------------------------- Gen.15.17 · THE_FIRE_BETWEEN_THE_PIECES --------
# וַיְהִי הַשֶּׁמֶשׁ בָּאָה וַעֲלָטָה הָיָה וְהִנֵּה תַנּוּר עָשָׁן
# וְלַפִּיד אֵשׁ אֲשֶׁר עָבַר בֵּין הַגְּזָרִים הָאֵלֶּה
# "And it came to pass, that, when the sun went down, and there was thick
# darkness, behold a smoking furnace, and a flaming torch that passed
# between these pieces."
m.step("Gen.15.17")
# ‹וַיְהִי הַשֶּׁמֶשׁ בָּאָה וַעֲלָטָה הָיָה› fact holds: and-alatah-was
m.fact("va_alatah_hayah")
# ‹וְהִנֵּה תַנּוּר עָשָׁן וְלַפִּיד אֵשׁ אֲשֶׁר עָבַר בֵּין הַגְּזָרִים
# הָאֵלֶּה› event: pass — agent tanur-ashan-and-lapid-esh; theme between-
# the-gezarim
m.event("pass", agent="tanur_ashan_ve_lapid_esh", themes=["bein_ha_gezarim"])

# -------------------------- Gen.15.18 · THE_COVENANT_CUT_AND_THE_RECEIPT ---
# בַּיּוֹם הַהוּא כָּרַת יְהוָה אֶת־אַבְרָם בְּרִית לֵאמֹר לְזַרְעֲךָ
# נָתַתִּי אֶת־הָאָרֶץ הַזֹּאת מִנְּהַר מִצְרַיִם עַד־הַנָּהָר הַגָּדֹל
# נְהַר־פְּרָת
# "In that day the LORD made a covenant with Abram, saying: 'Unto thy seed
# have I given this land, from the river of Egypt unto the great river, the
# river Euphrates;"
m.step("Gen.15.18")
# ‹כָּרַת יְהוָה אֶת־אַבְרָם בְּרִית› event: cut-covenant — agent the-LORD;
# theme brit
m.event("cut_covenant", agent="YHWH", themes=["brit"])
# ‹לְזַרְעֲךָ נָתַתִּי אֶת־הָאָרֶץ הַזֹּאת› fact holds: to-zarakha-natati-
# the-earth-the-this
m.fact("le_zarakha_natati_et_ha_aretz_ha_zot")
# ‹מִנְּהַר מִצְרַיִם עַד־הַנָּהָר הַגָּדֹל נְהַר־פְּרָת› fact holds: from-
# nehar-mitzrayim-until-the-river-the-gadol-nehar-Euphrates
m.fact("mi_nehar_mitzrayim_ad_ha_nahar_ha_gadol_nehar_perat")
# reads without prior install (flag, not fix): river-mitzrayim, nehar-
# Euphrates
m.presupposed("nahar_mitzrayim", "nehar_perat")

# -------------------------- Gen.15.19 · THE_GRANT_ROSTER_ROW_ONE -----------
# אֶת־הַקֵּינִי וְאֶת־הַקְּנִזִּי וְאֵת הַקַּדְמֹנִי
# "the Kenite, and the Kenizzite, and the Kadmonite,"
m.step("Gen.15.19")
# ‹אֶת־הַקֵּינִי וְאֶת־הַקְּנִזִּי וְאֵת הַקַּדְמֹנִי› fact holds: the-qeni-
# and-the-qenizi-and-the-qadmoni
m.fact("et_ha_qeni_ve_et_ha_qenizi_ve_et_ha_qadmoni")

# -------------------------- Gen.15.20 · THE_GRANT_ROSTER_ROW_TWO -----------
# וְאֶת־הַחִתִּי וְאֶת־הַפְּרִזִּי וְאֶת־הָרְפָאִים
# "and the Hittite, and the Perizzite, and the Rephaim,"
m.step("Gen.15.20")
# ‹וְאֶת־הַחִתִּי וְאֶת־הַפְּרִזִּי וְאֶת־הָרְפָאִים› fact holds: and-the-
# chiti-and-the-perizi-and-the-refaim
m.fact("ve_et_ha_chiti_ve_et_ha_perizi_ve_et_ha_refaim")

# -------------------------- Gen.15.21 · THE_GRANT_ROSTER_ROW_THREE ---------
# וְאֶת־הָאֱמֹרִי וְאֶת־הַכְּנַעֲנִי וְאֶת־הַגִּרְגָּשִׁי וְאֶת־הַיְבוּסִי
# "and the Amorite, and the Canaanite, and the Girgashite, and the
# Jebusite.'"
m.step("Gen.15.21")
# ‹וְאֶת־הָאֱמֹרִי וְאֶת־הַכְּנַעֲנִי וְאֶת־הַגִּרְגָּשִׁי וְאֶת־הַיְבוּסִי›
# fact holds: and-the-emori-and-the-kenaani-and-the-girgashi-and-the-yevusi
m.fact("ve_et_ha_emori_ve_et_ha_kenaani_ve_et_ha_girgashi_ve_et_ha_yevusi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'ur_kasdim', 'nehar_perat', 'dameseq', 'nahar_mitzrayim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tira(avram)', 'habet_u_sefor(avram, ha_shamaymah_ve_ha_kokhavim)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['anokhi_magen_lakh', 'sekharkha_harbeh_meod', 'mah_titen_li_ve_anokhi_holekh_ariri', 'ben_mesheq_beti_hu_dameseq_eliezer', 'hen_li_lo_natata_zara', 'ben_beti_yoresh_oti', 'lo_yirashkha_zeh', 'asher_yetze_mi_meekha_hu_yirashekha', 'koh_yihyeh_zarekha', 've_heemin_ba_YHWH', 'va_yachsheveha_lo_tzedaqah', 'ani_YHWH_asher_hotzetikha_me_ur_kasdim', 'la_tet_lekha_et_ha_aretz_ha_zot_le_rishtah', 'ba_mah_eda_ki_irashena', 've_et_ha_tzipor_lo_vatar', 'emah_chashekhah_gedolah_nofelet_alav', 'ger_yihyeh_zarakha_be_eretz_lo_lahem', 'va_avadum_ve_inu_otam_arba_meot_shanah', 'dan_anokhi_et_ha_goy_asher_yaavodu', 've_acharei_khen_yetzu_bi_rekhush_gadol', 'tavo_el_avotekha_be_shalom', 'tiqaver_be_sevah_tovah', 've_dor_revii_yashuvu_henah', 'lo_shalem_avon_ha_emori_ad_henah', 'va_alatah_hayah', 'le_zarakha_natati_et_ha_aretz_ha_zot', 'mi_nehar_mitzrayim_ad_ha_nahar_ha_gadol_nehar_perat', 'et_ha_qeni_ve_et_ha_qenizi_ve_et_ha_qadmoni', 've_et_ha_chiti_ve_et_ha_perizi_ve_et_ha_refaim', 've_et_ha_emori_ve_et_ha_kenaani_ve_et_ha_girgashi_ve_et_ha_yevusi'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_32_hagar_angel
###############################################################################
# =============================================================================
# gen_32_hagar_angel — 16:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_32_hagar_angel.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Hagar: the maid given, the flight, the angel, the names (16:1-16)"""
from machine import Machine

m = Machine("gen_32_hagar_angel")

# -------------------------- Gen.16.1 · THE_BARREN_WIFE_AND_THE_MAID --------
# וְשָׂרַי אֵשֶׁת אַבְרָם לֹא יָלְדָה לוֹ וְלָהּ שִׁפְחָה מִצְרִית וּשְׁמָהּ
# הָגָר
# "Now Sarai Abram's wife bore him no children; and she had a handmaid, an
# Egyptian, whose name was Hagar."
m.step("Gen.16.1")
# ‹לֹא יָלְדָה לוֹ וְלָהּ שִׁפְחָה מִצְרִית וּשְׁמָהּ הָגָר› fact holds:
# saray-not-yaldah-not; and-lah-shifchah-mitzrit-and-shemah-hagar
m.fact("saray_lo_yaldah_lo",
       "ve_lah_shifchah_mitzrit_u_shemah_hagar")

# -------------------------- Gen.16.2 · THE_INITIATIVE_AND_THE_LISTENING ----
# וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם הִנֵּה־נָא עֲצָרַנִי יְהוָה מִלֶּדֶת בֹּא־נָא
# אֶל־שִׁפְחָתִי אוּלַי אִבָּנֶה מִמֶּנָּה וַיִּשְׁמַע אַבְרָם לְקוֹל שָׂרָי
# "And Sarai said unto Abram: 'Behold now, the LORD hath restrained me from
# bearing; go in, I pray thee, unto my handmaid; it may be that I shall be
# builded up through her.' And Abram hearkened to the voice of Sarai."
m.step("Gen.16.2")
# ‹וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם› event: say — agent saray
m.event("say", agent="saray")
# ‹בֹּא־נָא אֶל־שִׁפְחָתִי› saray speaks a demand — LET: in-it(avram, to-
# shifchati)
m.declare("saray", "LET",
          "bo(avram, el_shifchati)")
# ‹עֲצָרַנִי יְהוָה מִלֶּדֶת … אוּלַי אִבָּנֶה מִמֶּנָּה› fact holds:
# atzarani-the-LORD-from-ledet; ulay-ibaneh-mimenah
m.fact("atzarani_YHWH_mi_ledet",
       "ulay_ibaneh_mimenah")
# ‹וַיִּשְׁמַע אַבְרָם לְקוֹל שָׂרָי› event: hear — agent avram; theme
# voice-saray
m.event("hear", agent="avram", themes=["qol_saray"])

# -------------------------- Gen.16.3 · THE_TAKE_AND_THE_GIVE ---------------
# וַתִּקַּח שָׂרַי אֵשֶׁת־אַבְרָם אֶת־הָגָר הַמִּצְרִית שִׁפְחָתָהּ מִקֵּץ
# עֶשֶׂר שָׁנִים לְשֶׁבֶת אַבְרָם בְּאֶרֶץ כְּנָעַן וַתִּתֵּן אֹתָהּ
# לְאַבְרָם אִישָׁהּ לוֹ לְאִשָּׁה
# "And Sarai Abram's wife took Hagar the Egyptian, her handmaid, after Abram
# had dwelt ten years in the land of Canaan, and gave her to Abram her
# husband to be his wife."
m.step("Gen.16.3")
# ‹וַתִּקַּח שָׂרַי … אֶת־הָגָר› event: take — agent saray; theme hagar
m.event("take", agent="saray", themes=["hagar"])
# ‹וַתִּתֵּן אֹתָהּ לְאַבְרָם אִישָׁהּ לוֹ לְאִשָּׁה› event: give — agent
# saray; theme hagar
m.event("give", agent="saray", themes=["hagar"])
# ‹מִקֵּץ עֶשֶׂר שָׁנִים לְשֶׁבֶת אַבְרָם בְּאֶרֶץ כְּנָעַן› fact holds:
# from-qetz-eser-shanim-to-shevet-avram-in-earth-kenaan
m.fact("mi_qetz_eser_shanim_le_shevet_avram_be_eretz_kenaan")

# -------------------------- Gen.16.4 · THE_COMPLIANCE_AND_THE_CONTEMPT -----
# וַיָּבֹא אֶל־הָגָר וַתַּהַר וַתֵּרֶא כִּי הָרָתָה וַתֵּקַל גְּבִרְתָּהּ
# בְּעֵינֶיהָ
# "And he went in unto Hagar, and she conceived; and when she saw that she
# had conceived, her mistress was despised in her eyes."
m.step("Gen.16.4")
# ‹וַיָּבֹא אֶל־הָגָר› event: come — agent avram
m.event("come", agent="avram")
# ‹וַיָּבֹא אֶל־הָגָר› demand settled (popped from the queue): in-it(avram,
# to-shifchati)
m.result("bo(avram, el_shifchati)", tmark="t1")
# ‹וַתַּהַר› event: conceive — agent hagar
m.event("conceive", agent="hagar")
# ‹וַתֵּקַל גְּבִרְתָּהּ בְּעֵינֶיהָ› fact holds: and-teqal-gevirtah-in-
# eineha
m.fact("va_teqal_gevirtah_be_eineha")

# -------------------------- Gen.16.5 · THE_GRIEVANCE_AND_THE_DEMAND_ON_GOD -
# וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם חֲמָסִי עָלֶיךָ אָנֹכִי נָתַתִּי שִׁפְחָתִי
# בְּחֵיקֶךָ וַתֵּרֶא כִּי הָרָתָה וָאֵקַל בְּעֵינֶיהָ יִשְׁפֹּט יְהוָה
# בֵּינִי וּבֵינֶיךָ
# "And Sarai said unto Abram: 'My wrong be upon thee: I gave my handmaid
# into thy bosom; and when she saw that she had conceived, I was despised in
# her eyes: the LORD judge between me and thee.'"
m.step("Gen.16.5")
# ‹וַתֹּאמֶר שָׂרַי אֶל־אַבְרָם› event: say — agent saray
m.event("say", agent="saray")
# ‹חֲמָסִי עָלֶיךָ אָנֹכִי נָתַתִּי שִׁפְחָתִי בְּחֵיקֶךָ› fact holds:
# chamasi-alekha; anokhi-natati-shifchati-in-cheqekha
m.fact("chamasi_alekha",
       "anokhi_natati_shifchati_be_cheqekha")
# ‹יִשְׁפֹּט יְהוָה בֵּינִי וּבֵינֶיךָ› saray speaks a demand — LET:
# yishpot(the-LORD, beini-and-veinekha)
m.declare("saray", "LET",
          "yishpot(YHWH, beini_u_veinekha)")

# -------------------------- Gen.16.6 · THE_PERMISSION_THE_AFFLICTION_THE_FLIGHT -
# וַיֹּאמֶר אַבְרָם אֶל־שָׂרַי הִנֵּה שִׁפְחָתֵךְ בְּיָדֵךְ עֲשִׂי־לָהּ
# הַטּוֹב בְּעֵינָיִךְ וַתְּעַנֶּהָ שָׂרַי וַתִּבְרַח מִפָּנֶיהָ
# "But Abram said unto Sarai: 'Behold, thy maid is in thy hand; do to her
# that which is good in thine eyes.' And Sarai dealt harshly with her, and
# she fled from her face."
m.step("Gen.16.6")
# ‹וַיֹּאמֶר אַבְרָם אֶל־שָׂרַי› event: say — agent avram
m.event("say", agent="avram")
# ‹עֲשִׂי־לָהּ הַטּוֹב בְּעֵינָיִךְ› avram speaks a demand — LET: asi(saray,
# to-hagar-the-good-in-einayikh)
m.declare("avram", "LET",
          "asi(saray, la_hagar_ha_tov_be_einayikh)")
# ‹וַתְּעַנֶּהָ שָׂרַי› event: afflict — agent saray; theme hagar
m.event("afflict", agent="saray", themes=["hagar"])
# ‹וַתִּבְרַח מִפָּנֶיהָ› event: flee — agent hagar
m.event("flee", agent="hagar")

# -------------------------- Gen.16.7 · THE_ANGEL_FINDS_HER -----------------
# וַיִּמְצָאָהּ מַלְאַךְ יְהוָה עַל־עֵין הַמַּיִם בַּמִּדְבָּר עַל־הָעַיִן
# בְּדֶרֶךְ שׁוּר
# "And the angel of the LORD found her by a fountain of water in the
# wilderness, by the fountain in the way to Shur."
m.step("Gen.16.7")
# ‹וַיִּמְצָאָהּ מַלְאַךְ יְהוָה› event: find — agent malakh-the-LORD; theme
# hagar
m.event("find", agent="malakh_YHWH", themes=["hagar"])
# reads without prior install (flag, not fix): shur
m.presupposed("shur")

# -------------------------- Gen.16.8 · THE_WHERE_QUESTIONS_AND_THE_RUNAWAY_ANSWER -
# וַיֹּאמַר הָגָר שִׁפְחַת שָׂרַי אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי וַתֹּאמֶר
# מִפְּנֵי שָׂרַי גְּבִרְתִּי אָנֹכִי בֹּרַחַת
# "And he said: 'Hagar, Sarai's handmaid, whence camest thou? and whither
# goest thou?' And she said: 'I flee from the face of my mistress Sarai.'"
m.step("Gen.16.8")
# ‹וַיֹּאמַר הָגָר שִׁפְחַת שָׂרַי אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי› event:
# say — agent malakh-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹אֵי־מִזֶּה בָאת וְאָנָה תֵלֵכִי› fact holds: ei-mizeh-vat-and-anah-
# telekhi
m.fact("ei_mizeh_vat_ve_anah_telekhi")
# ‹וַתֹּאמֶר› event: say — agent hagar
m.event("say", agent="hagar")
# ‹מִפְּנֵי שָׂרַי גְּבִרְתִּי אָנֹכִי בֹּרַחַת› fact holds: from-face-of-
# saray-gevirti-anokhi-borachat
m.fact("mi_pnei_saray_gevirti_anokhi_borachat")

# -------------------------- Gen.16.9 · THE_RETURN_AND_SUBMIT_COMMAND -------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה שׁוּבִי אֶל־גְּבִרְתֵּךְ וְהִתְעַנִּי
# תַּחַת יָדֶיהָ
# "And the angel of the LORD said unto her: 'Return to thy mistress, and
# submit thyself under her hands.'"
m.step("Gen.16.9")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› event: say — agent malakh-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹שׁוּבִי אֶל־גְּבִרְתֵּךְ וְהִתְעַנִּי תַּחַת יָדֶיהָ› malakh-the-LORD
# speaks a demand — LET: shuvi-and-hitani(hagar, to-gevirtekh-tachat-yadeha)
m.declare("malakh_YHWH", "LET",
          "shuvi_ve_hitani(hagar, el_gevirtekh_tachat_yadeha)")

# -------------------------- Gen.16.10 · THE_UNCOUNTABLE_SEED ---------------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה הַרְבָּה אַרְבֶּה אֶת־זַרְעֵךְ וְלֹא
# יִסָּפֵר מֵרֹב
# "And the angel of the LORD said unto her: 'I will greatly multiply thy
# seed, that it shall not be numbered for multitude.'"
m.step("Gen.16.10")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› event: say — agent malakh-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹הַרְבָּה אַרְבֶּה אֶת־זַרְעֵךְ וְלֹא יִסָּפֵר מֵרֹב› fact holds: greatly-
# I-will-multiply-zarekh; and-not-yisafer-from-rov
m.fact("harbah_arbeh_et_zarekh",
       "ve_lo_yisafer_me_rov")

# -------------------------- Gen.16.11 · THE_ANNUNCIATION -------------------
# וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה הִנָּךְ הָרָה וְיֹלַדְתְּ בֵּן וְקָרָאת
# שְׁמוֹ יִשְׁמָעֵאל כִּי־שָׁמַע יְהוָה אֶל־עָנְיֵךְ
# "And the angel of the LORD said unto her: 'Behold, thou art with child,
# and shalt bear a son; and thou shalt call his name Ishmael, because the
# LORD hath heard thy affliction.'"
m.step("Gen.16.11")
# ‹וַיֹּאמֶר לָהּ מַלְאַךְ יְהוָה› event: say — agent malakh-the-LORD
m.event("say", agent="malakh_YHWH")
# ‹הִנָּךְ הָרָה וְיֹלַדְתְּ בֵּן וְקָרָאת שְׁמוֹ יִשְׁמָעֵאל כִּי־שָׁמַע
# יְהוָה אֶל־עָנְיֵךְ› fact holds: hinakh-harah-and-yoladt-ben; and-qarat-
# shemo-yishmael; when-shama-the-LORD-to-onyekh
m.fact("hinakh_harah_ve_yoladt_ben",
       "ve_qarat_shemo_yishmael",
       "ki_shama_YHWH_el_onyekh")

# -------------------------- Gen.16.12 · THE_WILD_ASS_ORACLE ----------------
# וְהוּא יִהְיֶה פֶּרֶא אָדָם יָדוֹ בַכֹּל וְיַד כֹּל בּוֹ וְעַל־פְּנֵי
# כָל־אֶחָיו יִשְׁכֹּן
# "And he shall be a wild ass of a man: his hand shall be against every man,
# and every man's hand against him; and he shall dwell in the face of all
# his brethren.'"
m.step("Gen.16.12")
# ‹פֶּרֶא אָדָם יָדוֹ בַכֹּל וְיַד כֹּל בּוֹ וְעַל־פְּנֵי כָל־אֶחָיו
# יִשְׁכֹּן› fact holds: pere-human-his-hand-and-all-and-yad-all-in-it;
# upon-face-of-all-echav-yishkon
m.fact("pere_adam_yado_va_khol_ve_yad_kol_bo",
       "al_pnei_khol_echav_yishkon")

# -------------------------- Gen.16.13 · SHE_NAMES_YHWH ---------------------
# וַתִּקְרָא שֵׁם־יְהוָה הַדֹּבֵר אֵלֶיהָ אַתָּה אֵל רֳאִי כִּי אָמְרָה
# הֲגַם הֲלֹם רָאִיתִי אַחֲרֵי רֹאִי
# "And she called the name of the LORD that spoke unto her, Thou art a God
# of seeing; for she said: 'Have I even here seen Him that seeth Me?'"
m.step("Gen.16.13")
# ‹וַתִּקְרָא שֵׁם־יְהוָה הַדֹּבֵר אֵלֶיהָ אַתָּה אֵל רֳאִי› named: the-LORD
# := El-Roi
m.name("YHWH", "El_Roi")
# ‹כִּי אָמְרָה הֲגַם הֲלֹם רָאִיתִי אַחֲרֵי רֹאִי› fact holds: hagam-halom-
# raiti-acharei-roi
m.fact("hagam_halom_raiti_acharei_roi")

# -------------------------- Gen.16.14 · THE_WELL_OF_THE_LIVING_ONE_WHO_SEES -
# עַל־כֵּן קָרָא לַבְּאֵר בְּאֵר לַחַי רֹאִי הִנֵּה בֵין־קָדֵשׁ וּבֵין
# בָּרֶד
# "Wherefore the well was called 'Beer-lahai-roi; behold, it is between
# Kadesh and Bered."
m.step("Gen.16.14")
# ‹עַל־כֵּן קָרָא לַבְּאֵר בְּאֵר לַחַי רֹאִי› pattern recorded: upon-ken-
# qara-to-beer-beer-lachai-roi
m.pattern("al_ken_qara_la_beer_beer_lachai_roi")
# ‹הִנֵּה בֵין־קָדֵשׁ וּבֵין בָּרֶד› fact holds: hineh-vein-qadesh-and-vein-
# bared
m.fact("hineh_vein_qadesh_u_vein_bared")
# reads without prior install (flag, not fix): qadesh, bered
m.presupposed("qadesh", "bered")

# -------------------------- Gen.16.15 · THE_BIRTH_AND_THE_FATHERS_NAMING ---
# וַתֵּלֶד הָגָר לְאַבְרָם בֵּן וַיִּקְרָא אַבְרָם שֶׁם־בְּנוֹ
# אֲשֶׁר־יָלְדָה הָגָר יִשְׁמָעֵאל
# "And Hagar bore Abram a son; and Abram called the name of his son, whom
# Hagar bore, Ishmael."
m.step("Gen.16.15")
# ‹וַתֵּלֶד הָגָר לְאַבְרָם בֵּן› event: bear — agent hagar; theme yishmael
m.event("bear", agent="hagar", themes=["yishmael"])
# ‹וַיִּקְרָא אַבְרָם שֶׁם־בְּנוֹ … יִשְׁמָעֵאל› named: yishmael := Yishmael
m.name("yishmael", "Yishmael")

# -------------------------- Gen.16.16 · THE_AGE_FRAME ----------------------
# וְאַבְרָם בֶּן־שְׁמֹנִים שָׁנָה וְשֵׁשׁ שָׁנִים בְּלֶדֶת־הָגָר
# אֶת־יִשְׁמָעֵאל לְאַבְרָם
# "And Abram was fourscore and six years old, when Hagar bore Ishmael to
# Abram."
m.step("Gen.16.16")
# ‹וְאַבְרָם בֶּן־שְׁמֹנִים שָׁנָה וְשֵׁשׁ שָׁנִים› fact holds: avram-ben-
# shemonim-year-and-shesh-shanim
m.fact("avram_ben_shemonim_shanah_ve_shesh_shanim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'bered', 'shur', 'qadesh'}
    assert m.REGISTRY["names"] == {'YHWH': 'El_Roi', 'yishmael': 'Yishmael'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['yishpot(YHWH, beini_u_veinekha)', 'asi(saray, la_hagar_ha_tov_be_einayikh)', 'shuvi_ve_hitani(hagar, el_gevirtekh_tachat_yadeha)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['saray_lo_yaldah_lo', 've_lah_shifchah_mitzrit_u_shemah_hagar', 'atzarani_YHWH_mi_ledet', 'ulay_ibaneh_mimenah', 'mi_qetz_eser_shanim_le_shevet_avram_be_eretz_kenaan', 'va_teqal_gevirtah_be_eineha', 'chamasi_alekha', 'anokhi_natati_shifchati_be_cheqekha', 'ei_mizeh_vat_ve_anah_telekhi', 'mi_pnei_saray_gevirti_anokhi_borachat', 'harbah_arbeh_et_zarekh', 've_lo_yisafer_me_rov', 'hinakh_harah_ve_yoladt_ben', 've_qarat_shemo_yishmael', 'ki_shama_YHWH_el_onyekh', 'pere_adam_yado_va_khol_ve_yad_kol_bo', 'al_pnei_khol_echav_yishkon', 'hagam_halom_raiti_acharei_roi', 'pattern: al_ken_qara_la_beer_beer_lachai_roi', 'hineh_vein_qadesh_u_vein_bared', 'avram_ben_shemonim_shanah_ve_shesh_shanim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 25
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_33_shaddai_covenant_flesh
###############################################################################
# =============================================================================
# gen_33_shaddai_covenant_flesh — 17:1-27
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_33_shaddai_covenant_flesh.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""El Shaddai: the renamings, the law of the flesh, the laugh, the selfsame day (17:1-27)"""
from machine import Machine

m = Machine("gen_33_shaddai_covenant_flesh")

# -------------------------- Gen.17.1 · EL_SHADDAI_AND_THE_WALK_COMMAND -----
# וַיְהִי אַבְרָם בֶּן־תִּשְׁעִים שָׁנָה וְתֵשַׁע שָׁנִים וַיֵּרָא יְהוָה
# אֶל־אַבְרָם וַיֹּאמֶר אֵלָיו אֲנִי־אֵל שַׁדַּי הִתְהַלֵּךְ לְפָנַי וֶהְיֵה
# תָמִים
# "And when Abram was ninety years old and nine, the LORD appeared to Abram,
# and said unto him: 'I am God Almighty; walk before Me, and be thou
# wholehearted."
m.step("Gen.17.1")
# ‹וַיֵּרָא יְהוָה אֶל־אַבְרָם› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹אֲנִי־אֵל שַׁדַּי› fact holds: ani-to-shaddai
m.fact("ani_el_shaddai")
# ‹הִתְהַלֵּךְ לְפָנַי וֶהְיֵה תָמִים› the-LORD speaks a demand — LET:
# walked-about-and-heyeh-tamim(avram, before-Me)
m.declare("YHWH", "LET",
          "hithalekh_ve_heyeh_tamim(avram, lefanai)")

# -------------------------- Gen.17.2 · THE_COHORTATIVE_COVENANT ------------
# וְאֶתְּנָה בְרִיתִי בֵּינִי וּבֵינֶךָ וְאַרְבֶּה אוֹתְךָ בִּמְאֹד מְאֹד
# "And I will make My covenant between Me and thee, and will multiply thee
# exceedingly.'"
m.step("Gen.17.2")
# ‹וְאֶתְּנָה בְרִיתִי בֵּינִי וּבֵינֶךָ וְאַרְבֶּה אוֹתְךָ בִּמְאֹד מְאֹד›
# fact holds: and-etnah-vriti-beini-and-veinekha; and-I-will-multiply-otkha-
# bi-very-very
m.fact("ve_etnah_vriti_beini_u_veinekha",
       "ve_arbeh_otkha_bi_meod_meod")

# -------------------------- Gen.17.3 · THE_FIRST_FALL_AND_THE_SPEAK_FRAME --
# וַיִּפֹּל אַבְרָם עַל־פָּנָיו וַיְדַבֵּר אִתּוֹ אֱלֹהִים לֵאמֹר
# "And Abram fell on his face; and God talked with him, saying:"
m.step("Gen.17.3")
# ‹וַיִּפֹּל אַבְרָם עַל־פָּנָיו› event: fall — agent avram
m.event("fall", agent="avram")
# ‹וַיְדַבֵּר אִתּוֹ אֱלֹהִים לֵאמֹר› event: speak — agent God
m.event("speak", agent="elohim")

# -------------------------- Gen.17.4 · THE_FATHER_OF_MULTITUDE_CHARTER -----
# אֲנִי הִנֵּה בְרִיתִי אִתָּךְ וְהָיִיתָ לְאַב הֲמוֹן גּוֹיִם
# "'As for Me, behold, My covenant is with thee, and thou shalt be the
# father of a multitude of nations."
m.step("Gen.17.4")
# ‹אֲנִי הִנֵּה בְרִיתִי אִתָּךְ וְהָיִיתָ לְאַב הֲמוֹן גּוֹיִם› fact holds:
# ani-hineh-vriti-with-you; and-hayita-to-father-hamon-goyim
m.fact("ani_hineh_vriti_itakh",
       "ve_hayita_le_av_hamon_goyim")

# -------------------------- Gen.17.5 · AVRAM_RETIRED_AVRAHAM_DECREED -------
# וְלֹא־יִקָּרֵא עוֹד אֶת־שִׁמְךָ אַבְרָם וְהָיָה שִׁמְךָ אַבְרָהָם כִּי
# אַב־הֲמוֹן גּוֹיִם נְתַתִּיךָ
# "Neither shall thy name any more be called Abram, but thy name shall be
# Abraham; for the father of a multitude of nations have I made thee."
m.step("Gen.17.5")
# ‹וְלֹא־יִקָּרֵא עוֹד אֶת־שִׁמְךָ אַבְרָם וְהָיָה שִׁמְךָ אַבְרָהָם› fact
# holds: not-yiqare-od-shimkha-avram; and-was-shimkha-avraham
m.fact("lo_yiqare_od_shimkha_avram",
       "ve_hayah_shimkha_avraham")

# -------------------------- Gen.17.6 · FRUITFULNESS_AND_KINGS --------------
# וְהִפְרֵתִי אֹתְךָ בִּמְאֹד מְאֹד וּנְתַתִּיךָ לְגוֹיִם וּמְלָכִים מִמְּךָ
# יֵצֵאוּ
# "And I will make thee exceeding fruitful, and I will make nations of thee,
# and kings shall come out of thee."
m.step("Gen.17.6")
# ‹וְהִפְרֵתִי אֹתְךָ בִּמְאֹד מְאֹד וּמְלָכִים מִמְּךָ יֵצֵאוּ› fact holds:
# and-hifreti-otkha-bi-very-very; and-melakhim-mimkha-yetzeu
m.fact("ve_hifreti_otkha_bi_meod_meod",
       "u_melakhim_mimkha_yetzeu")

# -------------------------- Gen.17.7 · THE_EVERLASTING_COVENANT ------------
# וַהֲקִמֹתִי אֶת־בְּרִיתִי בֵּינִי וּבֵינֶךָ וּבֵין זַרְעֲךָ אַחֲרֶיךָ
# לְדֹרֹתָם לִבְרִית עוֹלָם לִהְיוֹת לְךָ לֵאלֹהִים וּלְזַרְעֲךָ אַחֲרֶיךָ
# "And I will establish My covenant between Me and thee and thy seed after
# thee throughout their generations for an everlasting covenant, to be a God
# unto thee and to thy seed after thee."
m.step("Gen.17.7")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי … לִבְרִית עוֹלָם לִהְיוֹת לְךָ לֵאלֹהִים› fact
# holds: and-haqimoti-My-covenant-to-me-vrit-olam; to-me-being-to-you-to-
# lohim
m.fact("va_haqimoti_et_briti_li_vrit_olam",
       "li_heyot_lekha_le_lohim")

# -------------------------- Gen.17.8 · THE_EVERLASTING_POSSESSION ----------
# וְנָתַתִּי לְךָ וּלְזַרְעֲךָ אַחֲרֶיךָ אֵת אֶרֶץ מְגֻרֶיךָ אֵת כָּל־אֶרֶץ
# כְּנַעַן לַאֲחֻזַּת עוֹלָם וְהָיִיתִי לָהֶם לֵאלֹהִים
# "And I will give unto thee, and to thy seed after thee, the land of thy
# sojournings, all the land of Canaan, for an everlasting possession; and I
# will be their God.'"
m.step("Gen.17.8")
# ‹וְנָתַתִּי … אֵת אֶרֶץ מְגֻרֶיךָ … לַאֲחֻזַּת עוֹלָם וְהָיִיתִי לָהֶם
# לֵאלֹהִים› fact holds: and-natati-earth-megurekha-to-achuzat-olam; and-
# hayiti-to-them-to-lohim
m.fact("ve_natati_et_eretz_megurekha_la_achuzat_olam",
       "ve_hayiti_lahem_le_lohim")

# -------------------------- Gen.17.9 · THE_GUARDED_KEEP_COMMAND ------------
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם וְאַתָּה אֶת־בְּרִיתִי תִשְׁמֹר אַתָּה
# וְזַרְעֲךָ אַחֲרֶיךָ לְדֹרֹתָם
# "And God said unto Abraham: 'And as for thee, thou shalt keep My covenant,
# thou, and thy seed after thee throughout their generations."
m.step("Gen.17.9")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם› event: say — agent God
m.event("say", agent="elohim")
# ‹וְאַתָּה אֶת־בְּרִיתִי תִשְׁמֹר› God speaks a demand — LET?:
# tishmor(avraham, My-covenant)
m.declare("elohim", "LET?",
          "tishmor(avraham, et_briti)")

# -------------------------- Gen.17.10 · THE_LAW_ANNOUNCED ------------------
# זֹאת בְּרִיתִי אֲשֶׁר תִּשְׁמְרוּ בֵּינִי וּבֵינֵיכֶם וּבֵין זַרְעֲךָ
# אַחֲרֶיךָ הִמּוֹל לָכֶם כָּל־זָכָר
# "This is My covenant, which ye shall keep, between Me and you and thy seed
# after thee: every male among you shall be circumcised."
m.step("Gen.17.10")
# ‹זֹאת בְּרִיתִי אֲשֶׁר תִּשְׁמְרוּ … הִמּוֹל לָכֶם כָּל־זָכָר› fact holds:
# this-My-covenant-which-tishmeru; himol-lakhem-all-male
m.fact("zot_briti_asher_tishmeru",
       "himol_lakhem_kol_zakhar")

# -------------------------- Gen.17.11 · THE_SIGN_IN_THE_FLESH --------------
# וּנְמַלְתֶּם אֵת בְּשַׂר עָרְלַתְכֶם וְהָיָה לְאוֹת בְּרִית בֵּינִי
# וּבֵינֵיכֶם
# "And ye shall be circumcised in the flesh of your foreskin; and it shall
# be a token of a covenant betwixt Me and you."
m.step("Gen.17.11")
# ‹וּנְמַלְתֶּם אֵת בְּשַׂר עָרְלַתְכֶם וְהָיָה לְאוֹת בְּרִית› fact holds:
# and-nemaltem-besar-arlatkhem; and-was-to-ot-brit
m.fact("u_nemaltem_et_besar_arlatkhem",
       "ve_hayah_le_ot_brit")

# -------------------------- Gen.17.12 · THE_EIGHTH_DAY_HANDLER -------------
# וּבֶן־שְׁמֹנַת יָמִים יִמּוֹל לָכֶם כָּל־זָכָר לְדֹרֹתֵיכֶם יְלִיד בָּיִת
# וּמִקְנַת־כֶּסֶף מִכֹּל בֶּן־נֵכָר אֲשֶׁר לֹא מִזַּרְעֲךָ הוּא
# "And he that is eight days old shall be circumcised among you, every male
# throughout your generations, he that is born in the house, or bought with
# money of any foreigner, that is not of thy seed."
m.step("Gen.17.12")
# ‹וּבֶן־שְׁמֹנַת יָמִים יִמּוֹל לָכֶם כָּל־זָכָר› standing handler — if
# ben-shemonat-seas ∧ all-male-to-doroteikhem then yimol ∧ yelid-bayit-and-
# miqnat-kesef-bi-khlal
m.handler("ben_shemonat_yamim ∧ kol_zakhar_le_doroteikhem",
          "yimol ∧ yelid_bayit_u_miqnat_kesef_bi_khlal")

# -------------------------- Gen.17.13 · THE_DOUBLED_MUST_AND_THE_FLESH_COVENANT -
# הִמּוֹל יִמּוֹל יְלִיד בֵּיתְךָ וּמִקְנַת כַּסְפֶּךָ וְהָיְתָה בְרִיתִי
# בִּבְשַׂרְכֶם לִבְרִית עוֹלָם
# "He that is born in thy house, and he that is bought with thy money, must
# needs be circumcised; and My covenant shall be in your flesh for an
# everlasting covenant."
m.step("Gen.17.13")
# ‹הִמּוֹל יִמּוֹל … וְהָיְתָה בְרִיתִי בִּבְשַׂרְכֶם לִבְרִית עוֹלָם› fact
# holds: himol-yimol-yelid-beitkha; vriti-bi-vesarkhem-to-me-vrit-olam
m.fact("himol_yimol_yelid_beitkha",
       "vriti_bi_vesarkhem_li_vrit_olam")

# -------------------------- Gen.17.14 · THE_KARET_HANDLER ------------------
# וְעָרֵל זָכָר אֲשֶׁר לֹא־יִמּוֹל אֶת־בְּשַׂר עָרְלָתוֹ וְנִכְרְתָה
# הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ אֶת־בְּרִיתִי הֵפַר
# "And the uncircumcised male who is not circumcised in the flesh of his
# foreskin, that soul shall be cut off from his people; he hath broken My
# covenant.'"
m.step("Gen.17.14")
# ‹וְעָרֵל זָכָר אֲשֶׁר לֹא־יִמּוֹל … וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא
# מֵעַמֶּיהָ› standing handler — if arel-male-which-not-yimol then and-
# nikhrta-the-nefesh-the-hi-from-ameha ∧ My-covenant-hefar
m.handler("arel_zakhar_asher_lo_yimol",
          "ve_nikhrta_ha_nefesh_ha_hi_me_ameha ∧ et_briti_hefar")

# -------------------------- Gen.17.15 · SARAY_RETIRED_SARAH_DECREED --------
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם שָׂרַי אִשְׁתְּךָ לֹא־תִקְרָא אֶת־שְׁמָהּ
# שָׂרָי כִּי שָׂרָה שְׁמָהּ
# "And God said unto Abraham: 'As for Sarai thy wife, thou shalt not call
# her name Sarai, but Sarah shall her name be."
m.step("Gen.17.15")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם› event: say — agent God
m.event("say", agent="elohim")
# ‹לֹא־תִקְרָא אֶת־שְׁמָהּ שָׂרָי כִּי שָׂרָה שְׁמָהּ› fact holds: not-
# tiqra-shemah-saray; when-sarah-shemah
m.fact("lo_tiqra_et_shemah_saray",
       "ki_sarah_shemah")

# -------------------------- Gen.17.16 · SARAHS_BLESSING_AND_HER_KINGS ------
# וּבֵרַכְתִּי אֹתָהּ וְגַם נָתַתִּי מִמֶּנָּה לְךָ בֵּן וּבֵרַכְתִּיהָ
# וְהָיְתָה לְגוֹיִם מַלְכֵי עַמִּים מִמֶּנָּה יִהְיוּ
# "And I will bless her, and moreover I will give thee a son of her; yea, I
# will bless her, and she shall be a mother of nations; kings of peoples
# shall be of her.'"
m.step("Gen.17.16")
# ‹וּבֵרַכְתִּי אֹתָהּ וְגַם נָתַתִּי מִמֶּנָּה לְךָ בֵּן … מַלְכֵי עַמִּים
# מִמֶּנָּה יִהְיוּ› fact holds: and-verakhti-her-and-natati-mimenah-to-you-
# ben; malkhei-amim-mimenah-yihyu
m.fact("u_verakhti_otah_ve_natati_mimenah_lekha_ben",
       "malkhei_amim_mimenah_yihyu")

# -------------------------- Gen.17.17 · THE_LAUGH_IN_THE_HEART -------------
# וַיִּפֹּל אַבְרָהָם עַל־פָּנָיו וַיִּצְחָק וַיֹּאמֶר בְּלִבּוֹ הַלְּבֶן
# מֵאָה־שָׁנָה יִוָּלֵד וְאִם־שָׂרָה הֲבַת־תִּשְׁעִים שָׁנָה תֵּלֵד
# "Then Abraham fell upon his face, and laughed, and said in his heart:
# 'Shall a child be born unto him that is a hundred years old? and shall
# Sarah, that is ninety years old, bear?'"
m.step("Gen.17.17")
# ‹וַיִּפֹּל אַבְרָהָם עַל־פָּנָיו› event: fall — agent avraham
m.event("fall", agent="avraham")
# ‹וַיִּצְחָק› event: laugh — agent avraham
m.event("laugh", agent="avraham")
# ‹וַיֹּאמֶר בְּלִבּוֹ› event: say — agent avraham
m.event("say", agent="avraham")
# ‹הַלְּבֶן מֵאָה־שָׁנָה יִוָּלֵד וְאִם־שָׂרָה הֲבַת־תִּשְׁעִים שָׁנָה
# תֵּלֵד› fact holds: the-to-ven-hundred-year-yivaled; the-vat-tishim-year-
# teled
m.fact("ha_le_ven_meah_shanah_yivaled",
       "ha_vat_tishim_shanah_teled")

# -------------------------- Gen.17.18 · THE_LU_PLEA ------------------------
# וַיֹּאמֶר אַבְרָהָם אֶל־הָאֱלֹהִים לוּ יִשְׁמָעֵאל יִחְיֶה לְפָנֶיךָ
# "And Abraham said unto God: 'Oh that Ishmael might live before Thee!'"
m.step("Gen.17.18")
# ‹וַיֹּאמֶר אַבְרָהָם אֶל־הָאֱלֹהִים› event: say — agent avraham
m.event("say", agent="avraham")
# ‹לוּ יִשְׁמָעֵאל יִחְיֶה לְפָנֶיךָ› fact holds: lu-yishmael-yichyeh-
# lefanekha
m.fact("lu_yishmael_yichyeh_lefanekha")

# -------------------------- Gen.17.19 · YITZCHAQ_NAMED_BEFORE_BIRTH --------
# וַיֹּאמֶר אֱלֹהִים אֲבָל שָׂרָה אִשְׁתְּךָ יֹלֶדֶת לְךָ בֵּן וְקָרָאתָ
# אֶת־שְׁמוֹ יִצְחָק וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתּוֹ לִבְרִית עוֹלָם
# לְזַרְעוֹ אַחֲרָיו
# "And God said: 'Nay, but Sarah thy wife shall bear thee a son; and thou
# shalt call his name Isaac; and I will establish My covenant with him for
# an everlasting covenant for his seed after him."
m.step("Gen.17.19")
# ‹וַיֹּאמֶר אֱלֹהִים אֲבָל› event: say — agent God
m.event("say", agent="elohim")
# ‹שָׂרָה … יֹלֶדֶת לְךָ בֵּן וְקָרָאתָ אֶת־שְׁמוֹ יִצְחָק וַהֲקִמֹתִי
# אֶת־בְּרִיתִי אִתּוֹ› fact holds: sarah-yoledet-to-you-ben; and-qarata-
# shemo-yitzchaq; and-haqimoti-My-covenant-with-him-to-me-vrit-olam
m.fact("sarah_yoledet_lekha_ben",
       "ve_qarata_et_shemo_yitzchaq",
       "va_haqimoti_et_briti_ito_li_vrit_olam")

# -------------------------- Gen.17.20 · YISHMAEL_HEARD ---------------------
# וּלְיִשְׁמָעֵאל שְׁמַעְתִּיךָ הִנֵּה בֵּרַכְתִּי אֹתוֹ וְהִפְרֵיתִי אֹתוֹ
# וְהִרְבֵּיתִי אֹתוֹ בִּמְאֹד מְאֹד שְׁנֵים־עָשָׂר נְשִׂיאִם יוֹלִיד
# וּנְתַתִּיו לְגוֹי גָּדוֹל
# "And as for Ishmael, I have heard thee; behold, I have blessed him, and
# will make him fruitful, and will multiply him exceedingly; twelve princes
# shall he beget, and I will make him a great nation."
m.step("Gen.17.20")
# ‹וּלְיִשְׁמָעֵאל שְׁמַעְתִּיךָ הִנֵּה בֵּרַכְתִּי אֹתוֹ … שְׁנֵים־עָשָׂר
# נְשִׂיאִם יוֹלִיד› fact holds: and-to-yishmael-shematikha; hineh-berakhti-
# it-bi-very-very; shneim-asar-nesiim-yolid
m.fact("u_le_yishmael_shematikha",
       "hineh_berakhti_oto_bi_meod_meod",
       "shneim_asar_nesiim_yolid")

# -------------------------- Gen.17.21 · THE_COVENANT_GETS_A_CALENDAR -------
# וְאֶת־בְּרִיתִי אָקִים אֶת־יִצְחָק אֲשֶׁר תֵּלֵד לְךָ שָׂרָה לַמּוֹעֵד
# הַזֶּה בַּשָּׁנָה הָאַחֶרֶת
# "But My covenant will I establish with Isaac, whom Sarah shall bear unto
# thee at this set time in the next year.'"
m.step("Gen.17.21")
# ‹וְאֶת־בְּרִיתִי אָקִים אֶת־יִצְחָק … לַמּוֹעֵד הַזֶּה בַּשָּׁנָה
# הָאַחֶרֶת› fact holds: and-My-covenant-aqim-yitzchaq; to-moed-the-this-in-
# the-year-the-acheret
m.fact("ve_et_briti_aqim_et_yitzchaq",
       "la_moed_ha_zeh_ba_shanah_ha_acheret")

# -------------------------- Gen.17.22 · THE_FINISH_AND_THE_ASCENT ----------
# וַיְכַל לְדַבֵּר אִתּוֹ וַיַּעַל אֱלֹהִים מֵעַל אַבְרָהָם
# "And He left off talking with him, and God went up from Abraham."
m.step("Gen.17.22")
# ‹וַיְכַל לְדַבֵּר אִתּוֹ› event: finish-speaking — agent God
m.event("finish_speaking", agent="elohim")
# ‹וַיַּעַל אֱלֹהִים מֵעַל אַבְרָהָם› event: ascend — agent God
m.event("ascend", agent="elohim")

# -------------------------- Gen.17.23 · THE_SELFSAME_DAY_COMPLIANCE --------
# וַיִּקַּח אַבְרָהָם אֶת־יִשְׁמָעֵאל בְּנוֹ וְאֵת כָּל־יְלִידֵי בֵיתוֹ …
# וַיָּמָל אֶת־בְּשַׂר עָרְלָתָם בְּעֶצֶם הַיּוֹם הַזֶּה כַּאֲשֶׁר דִּבֶּר
# אִתּוֹ אֱלֹהִים … בְּעֶצֶם הַיּוֹם הַזֶּה נִמּוֹל אַבְרָהָם וְיִשְׁמָעֵאל
# בְּנוֹ … נִמֹּלוּ אִתּוֹ
# "[EN-AID/JPS 17:23-27] And Abraham took Ishmael his son, and all that were
# born in his house, and all that were bought with his money... and
# circumcised the flesh of their foreskin in the selfsame day, as God had
# said unto him. And Abraham was ninety years old and nine... And Ishmael
# his son was thirteen years old... In the selfsame day was Abraham
# circumcised, and Ishmael his son. And all the men of his house... were
# circumcised with him."
m.step("Gen.17.23")
# ‹וַיִּקַּח אַבְרָהָם אֶת־יִשְׁמָעֵאל בְּנוֹ› event: take — agent avraham;
# theme yishmael-and-all-men-of-beito
m.event("take", agent="avraham", themes=["yishmael_ve_khol_anshei_beito"])
# ‹וַיָּמָל אֶת־בְּשַׂר עָרְלָתָם … נִמּוֹל אַבְרָהָם וְיִשְׁמָעֵאל בְּנוֹ …
# נִמֹּלוּ אִתּוֹ› event: circumcise — agent avraham; theme all-male-in-men-
# of-beito
m.event("circumcise", agent="avraham", themes=["kol_zakhar_be_anshei_beito"])
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה … כַּאֲשֶׁר דִּבֶּר אִתּוֹ אֱלֹהִים› fact holds:
# in-etzem-the-day-the-this; like-which-diber-with-him-God;
# avraham-99-yishmael-13-in-himolam
m.fact("be_etzem_ha_yom_ha_zeh",
       "ka_asher_diber_ito_elohim",
       "avraham_99_yishmael_13_be_himolam")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hithalekh_ve_heyeh_tamim(avram, lefanai)', 'tishmor(avraham, et_briti)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['ani_el_shaddai', 've_etnah_vriti_beini_u_veinekha', 've_arbeh_otkha_bi_meod_meod', 'ani_hineh_vriti_itakh', 've_hayita_le_av_hamon_goyim', 'lo_yiqare_od_shimkha_avram', 've_hayah_shimkha_avraham', 've_hifreti_otkha_bi_meod_meod', 'u_melakhim_mimkha_yetzeu', 'va_haqimoti_et_briti_li_vrit_olam', 'li_heyot_lekha_le_lohim', 've_natati_et_eretz_megurekha_la_achuzat_olam', 've_hayiti_lahem_le_lohim', 'zot_briti_asher_tishmeru', 'himol_lakhem_kol_zakhar', 'u_nemaltem_et_besar_arlatkhem', 've_hayah_le_ot_brit', 'handler: IF(ben_shemonat_yamim ∧ kol_zakhar_le_doroteikhem) THEN(yimol ∧ yelid_bayit_u_miqnat_kesef_bi_khlal)', 'himol_yimol_yelid_beitkha', 'vriti_bi_vesarkhem_li_vrit_olam', 'handler: IF(arel_zakhar_asher_lo_yimol) THEN(ve_nikhrta_ha_nefesh_ha_hi_me_ameha ∧ et_briti_hefar)', 'lo_tiqra_et_shemah_saray', 'ki_sarah_shemah', 'u_verakhti_otah_ve_natati_mimenah_lekha_ben', 'malkhei_amim_mimenah_yihyu', 'ha_le_ven_meah_shanah_yivaled', 'ha_vat_tishim_shanah_teled', 'lu_yishmael_yichyeh_lefanekha', 'sarah_yoledet_lekha_ben', 've_qarata_et_shemo_yitzchaq', 'va_haqimoti_et_briti_ito_li_vrit_olam', 'u_le_yishmael_shematikha', 'hineh_berakhti_oto_bi_meod_meod', 'shneim_asar_nesiim_yolid', 've_et_briti_aqim_et_yitzchaq', 'la_moed_ha_zeh_ba_shanah_ha_acheret', 'be_etzem_ha_yom_ha_zeh', 'ka_asher_diber_ito_elohim', 'avraham_99_yishmael_13_be_himolam'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 18
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_34_mamre_laugh_plea
###############################################################################
# =============================================================================
# gen_34_mamre_laugh_plea — 18:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_34_mamre_laugh_plea.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The visitors at Mamre, the laugh within, the plea for Sodom (18:1-33)"""
from machine import Machine

m = Machine("gen_34_mamre_laugh_plea")

# -------------------------- Gen.18.1 · THE_THIRD_APPEARANCE ----------------
# וַיֵּרָא אֵלָיו יְהוָה בְּאֵלֹנֵי מַמְרֵא וְהוּא יֹשֵׁב פֶּתַח־הָאֹהֶל
# כְּחֹם הַיּוֹם
# "And the LORD appeared unto him by the terebinths of Mamre, as he sat in
# the tent door in the heat of the day;"
m.step("Gen.18.1")
# ‹וַיֵּרָא אֵלָיו יְהוָה› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹בְּאֵלֹנֵי מַמְרֵא› reads without prior install (flag, not fix): mamre
m.presupposed("mamre")
# ‹וְהוּא יֹשֵׁב פֶּתַח־הָאֹהֶל כְּחֹם הַיּוֹם› fact holds: yoshev-door-
# opening-the-ohel-like-chom-the-day
m.fact("yoshev_petach_ha_ohel_ke_chom_ha_yom")

# -------------------------- Gen.18.2 · THREE_MEN_AND_THE_BOW ---------------
# וַיִּשָּׂא עֵינָיו וַיַּרְא וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים נִצָּבִים עָלָיו
# וַיַּרְא וַיָּרָץ לִקְרָאתָם מִפֶּתַח הָאֹהֶל וַיִּשְׁתַּחוּ אָרְצָה
# "and he lifted up his eyes and looked, and, lo, three men stood over
# against him; and when he saw them, he ran to meet them from the tent door,
# and bowed down to the earth,"
m.step("Gen.18.2")
# ‹וְהִנֵּה שְׁלֹשָׁה אֲנָשִׁים נִצָּבִים עָלָיו› the world gains: shelosha-
# anashim
m.install("shelosha_anashim")
# ‹וַיָּרָץ לִקְרָאתָם› event: run — agent avraham
m.event("run", agent="avraham")
# ‹וַיִּשְׁתַּחוּ אָרְצָה› event: bow — agent avraham
m.event("bow", agent="avraham")

# -------------------------- Gen.18.3 · THE_DOOR_PETITION -------------------
# וַיֹּאמַר אֲדֹנָי אִם־נָא מָצָאתִי חֵן בְּעֵינֶיךָ אַל־נָא תַעֲבֹר מֵעַל
# עַבְדֶּךָ
# "and said: 'My lord, if now I have found favour in thy sight, pass not
# away, I pray thee, from thy servant."
m.step("Gen.18.3")
# ‹אַל־נָא תַעֲבֹר מֵעַל עַבְדֶּךָ› avraham speaks a demand — LET-NOT:
# taavor(from-upon-avdekha)
m.declare("avraham", "LET-NOT",
          "taavor(me_al_avdekha)")

# -------------------------- Gen.18.4 · WATER_AND_THE_RARE_PASSIVE ----------
# יֻקַּח־נָא מְעַט־מַיִם וְרַחֲצוּ רַגְלֵיכֶם וְהִשָּׁעֲנוּ תַּחַת הָעֵץ
# "Let now a little water be fetched, and wash your feet, and recline
# yourselves under the tree."
m.step("Gen.18.4")
# ‹יֻקַּח־נָא מְעַט־מַיִם› avraham speaks a demand — LET: yuqach(meat-
# waters)
m.declare("avraham", "LET",
          "yuqach(meat_mayim)")
# ‹וְרַחֲצוּ רַגְלֵיכֶם וְהִשָּׁעֲנוּ תַּחַת הָעֵץ› avraham speaks a demand
# — LET: rachatzu-and-hishaanu(raglekhem)
m.declare("avraham", "LET",
          "rachatzu_ve_hishaanu(raglekhem)")

# -------------------------- Gen.18.5 · BREAD_PROMISED_ASSENT_GIVEN ---------
# וְאֶקְחָה פַת־לֶחֶם וְסַעֲדוּ לִבְּכֶם אַחַר תַּעֲבֹרוּ כִּי־עַל־כֵּן
# עֲבַרְתֶּם עַל־עַבְדְּכֶם וַיֹּאמְרוּ כֵּן תַּעֲשֶׂה כַּאֲשֶׁר דִּבַּרְתָּ
# "And I will fetch a morsel of bread, and stay ye your heart; after that ye
# shall pass on; forasmuch as ye are come to your servant.' And they said:
# 'So do, as thou hast said.'"
m.step("Gen.18.5")
# ‹וְאֶקְחָה פַת־לֶחֶם› fact holds: and-eqchah-fat-lechem
m.fact("ve_eqchah_fat_lechem")
# ‹וְסַעֲדוּ לִבְּכֶם› avraham speaks a demand — LET: saadu(libkhem)
m.declare("avraham", "LET",
          "saadu(libkhem)")
# ‹כֵּן תַּעֲשֶׂה כַּאֲשֶׁר דִּבַּרְתָּ› fact holds: ken-taaseh-like-which-
# dibarta
m.fact("ken_taaseh_ka_asher_dibarta")

# -------------------------- Gen.18.6 · THE_TRIPLE_TO_SARAH -----------------
# וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה אֶל־שָׂרָה וַיֹּאמֶר מַהֲרִי שְׁלֹשׁ סְאִים
# קֶמַח סֹלֶת לוּשִׁי וַעֲשִׂי עֻגוֹת
# "And Abraham hastened into the tent unto Sarah, and said: 'Make ready
# quickly three measures of fine meal, knead it, and make cakes.'"
m.step("Gen.18.6")
# ‹וַיְמַהֵר אַבְרָהָם הָאֹהֱלָה אֶל־שָׂרָה› event: hurry — agent avraham
m.event("hurry", agent="avraham")
# ‹מַהֲרִי שְׁלֹשׁ סְאִים קֶמַח סֹלֶת לוּשִׁי וַעֲשִׂי עֻגוֹת› avraham
# speaks a demand — LET: mahari-lushi-and-asi(ugot)
m.declare("avraham", "LET",
          "mahari_lushi_va_asi(ugot)")

# -------------------------- Gen.18.7 · THE_RUN_TO_THE_HERD -----------------
# וְאֶל־הַבָּקָר רָץ אַבְרָהָם וַיִּקַּח בֶּן־בָּקָר רַךְ וָטוֹב וַיִּתֵּן
# אֶל־הַנַּעַר וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ
# "And Abraham ran unto the herd, and fetched a calf tender and good, and
# gave it unto the servant; and he hastened to dress it."
m.step("Gen.18.7")
# ‹וַיִּקַּח בֶּן־בָּקָר רַךְ וָטוֹב› event: take — agent avraham; theme
# ben-baqar
m.event("take", agent="avraham", themes=["ben_baqar"])
# ‹וַיְמַהֵר לַעֲשׂוֹת אֹתוֹ› event: hurry-prepare — agent the-naar; theme
# ben-baqar
m.event("hurry_prepare", agent="ha_naar", themes=["ben_baqar"])

# -------------------------- Gen.18.8 · THE_DELIVERED_FEAST -----------------
# וַיִּקַּח חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה וַיִּתֵּן
# לִפְנֵיהֶם וְהוּא־עֹמֵד עֲלֵיהֶם תַּחַת הָעֵץ וַיֹּאכֵלוּ
# "And he took curd, and milk, and the calf which he had dressed, and set it
# before them; and he stood by them under the tree, and they did eat."
m.step("Gen.18.8")
# ‹וַיִּקַּח חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר אֲשֶׁר עָשָׂה וַיִּתֵּן
# לִפְנֵיהֶם› event: serve — agent avraham; theme chemah-chalav-and-ven-the-
# baqar
m.event("serve", agent="avraham", themes=["chemah_chalav_u_ven_ha_baqar"])
# ‹פַת־לֶחֶם … חֶמְאָה וְחָלָב וּבֶן־הַבָּקָר› spec-delta — spec said fat-
# lechem (a morsel fowl bread), delivery says chemah-chalav-and-ven-the-
# baqar (curds, milk, the dressed calf)
m.spec_delta("fat_lechem (a morsel of bread)",
             "chemah_chalav_u_ven_ha_baqar (curds, milk, the dressed calf)")
# ‹וְהוּא־עֹמֵד עֲלֵיהֶם תַּחַת הָעֵץ וַיֹּאכֵלוּ› fact holds: and-that-
# omed-aleihem-tachat-the-tree
m.fact("ve_hu_omed_aleihem_tachat_ha_etz")

# -------------------------- Gen.18.9 · THE_FOURTH_WHERE --------------------
# וַיֹּאמְרוּ אֵלָיו אַיֵּה שָׂרָה אִשְׁתֶּךָ וַיֹּאמֶר הִנֵּה בָאֹהֶל
# "And they said unto him: 'Where is Sarah thy wife?' And he said: 'Behold,
# in the tent.'"
m.step("Gen.18.9")
# ‹וַיֹּאמְרוּ אֵלָיו אַיֵּה שָׂרָה אִשְׁתֶּךָ› event: say — agent shelosha-
# anashim
m.event("say", agent="shelosha_anashim")

# -------------------------- Gen.18.10 · THE_RETURN_PROMISE -----------------
# וַיֹּאמֶר שׁוֹב אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וְהִנֵּה־בֵן לְשָׂרָה
# אִשְׁתֶּךָ וְשָׂרָה שֹׁמַעַת פֶּתַח הָאֹהֶל וְהוּא אַחֲרָיו
# "And He said: 'I will certainly return unto thee when the season cometh
# round; and, lo, Sarah thy wife shall have a son.' And Sarah heard in the
# tent door, which was behind him.—"
m.step("Gen.18.10")
# ‹שׁוֹב אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וְהִנֵּה־בֵן לְשָׂרָה› fact holds:
# shov-ashuv-to-you-like-beast; behold-ven-to-sarah
m.fact("shov_ashuv_elekha_ka_et_chayah",
       "hinneh_ven_le_sarah")
# ‹וְשָׂרָה שֹׁמַעַת פֶּתַח הָאֹהֶל› event: hear — agent sarah
m.event("hear", agent="sarah")

# -------------------------- Gen.18.11 · THE_AGE_PARENTHESIS ----------------
# וְאַבְרָהָם וְשָׂרָה זְקֵנִים בָּאִים בַּיָּמִים חָדַל לִהְיוֹת לְשָׂרָה
# אֹרַח כַּנָּשִׁים
# "Now Abraham and Sarah were old, and well stricken in age; it had ceased
# to be with Sarah after the manner of women.—"
m.step("Gen.18.11")
# ‹זְקֵנִים בָּאִים בַּיָּמִים … חָדַל לִהְיוֹת לְשָׂרָה אֹרַח כַּנָּשִׁים›
# fact holds: zeqenim-baim-in-the-seas; chadal-orach-like-nashim
m.fact("zeqenim_baim_ba_yamim",
       "chadal_orach_ka_nashim")
# ‹וְאַבְרָהָם וְשָׂרָה זְקֵנִים› note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.18.12 · THE_INTERIOR_LAUGH -----------------
# וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ לֵאמֹר אַחֲרֵי בְלֹתִי הָיְתָה־לִּי עֶדְנָה
# וַאדֹנִי זָקֵן
# "And Sarah laughed within herself, saying: 'After I am waxed old shall I
# have pleasure, my lord being old also?'"
m.step("Gen.18.12")
# ‹וַתִּצְחַק שָׂרָה בְּקִרְבָּהּ לֵאמֹר› event: say — agent sarah
m.event("say", agent="sarah")
# ‹אַחֲרֵי בְלֹתִי הָיְתָה־לִּי עֶדְנָה וַאדֹנִי זָקֵן› fact holds: acharei-
# veloti-haytah-to-me-ednah-and-adoni-zaqen
m.fact("acharei_veloti_haytah_li_ednah_va_adoni_zaqen")

# -------------------------- Gen.18.13 · THE_QUOTED_LAUGH -------------------
# וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם לָמָּה זֶּה צָחֲקָה שָׂרָה לֵאמֹר הַאַף
# אֻמְנָם אֵלֵד וַאֲנִי זָקַנְתִּי
# "And the LORD said unto Abraham: 'Wherefore did Sarah laugh, saying: Shall
# I of a surety bear a child, who am old?"
m.step("Gen.18.13")
# ‹וַיֹּאמֶר יְהוָה אֶל־אַבְרָהָם לָמָּה זֶּה צָחֲקָה שָׂרָה› event: say —
# agent the-LORD
m.event("say", agent="YHWH")

# -------------------------- Gen.18.14 · TOO_WONDROUS -----------------------
# הֲיִפָּלֵא מֵיְהוָה דָּבָר לַמּוֹעֵד אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה
# וּלְשָׂרָה בֵן
# "Is any thing too hard for the LORD. At the set time I will return unto
# thee, when the season cometh round, and Sarah shall have a son.'"
m.step("Gen.18.14")
# ‹הֲיִפָּלֵא מֵיְהוָה דָּבָר› fact holds: the-yipale-from-the-LORD-davar
m.fact("ha_yipale_me_YHWH_davar")
# ‹לַמּוֹעֵד אָשׁוּב אֵלֶיךָ כָּעֵת חַיָּה וּלְשָׂרָה בֵן› fact holds: to-
# moed-ashuv-to-you-and-to-sarah-ven
m.fact("la_moed_ashuv_elekha_u_le_sarah_ven")

# -------------------------- Gen.18.15 · THE_DENIAL_AND_THE_CORRECTION ------
# וַתְּכַחֵשׁ שָׂרָה לֵאמֹר לֹא צָחַקְתִּי כִּי יָרֵאָה וַיֹּאמֶר לֹא כִּי
# צָחָקְתְּ
# "Then Sarah denied, saying: 'I laughed not'; for she was afraid. And He
# said: 'Nay; but thou didst laugh.'"
m.step("Gen.18.15")
# ‹וַתְּכַחֵשׁ שָׂרָה לֵאמֹר לֹא צָחַקְתִּי› event: deny — agent sarah
m.event("deny", agent="sarah")
# ‹וַיֹּאמֶר לֹא כִּי צָחָקְתְּ› event: correct — agent the-LORD
m.event("correct", agent="YHWH")

# -------------------------- Gen.18.16 · THE_TURN_TOWARD_SODOM --------------
# וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם וְאַבְרָהָם
# הֹלֵךְ עִמָּם לְשַׁלְּחָם
# "And the men rose up from thence, and looked out toward Sodom; and Abraham
# went with them to bring them on the way."
m.step("Gen.18.16")
# ‹וַיָּקֻמוּ מִשָּׁם הָאֲנָשִׁים וַיַּשְׁקִפוּ עַל־פְּנֵי סְדֹם› event:
# rise-look — agent shelosha-anashim
m.event("rise_look", agent="shelosha_anashim")
# ‹סְדֹם› reads without prior install (flag, not fix): sedom
m.presupposed("sedom")
# ‹וְאַבְרָהָם הֹלֵךְ עִמָּם לְשַׁלְּחָם› event: escort — agent avraham
m.event("escort", agent="avraham")

# -------------------------- Gen.18.17 · THE_SOLILOQUY_OPENS ----------------
# וַיהֹוָה אָמָר הַמְכַסֶּה אֲנִי מֵאַבְרָהָם אֲשֶׁר אֲנִי עֹשֶׂה
# "And the LORD said: 'Shall I hide from Abraham that which I am doing;"
m.step("Gen.18.17")
# ‹וַיהֹוָה אָמָר הַמְכַסֶּה אֲנִי מֵאַבְרָהָם› event: say — agent the-LORD
m.event("say", agent="YHWH")

# -------------------------- Gen.18.18 · THE_GUARD_FORMULA_RESOUNDED --------
# וְאַבְרָהָם הָיוֹ יִהְיֶה לְגוֹי גָּדוֹל וְעָצוּם וְנִבְרְכוּ בוֹ כֹּל
# גּוֹיֵי הָאָרֶץ
# "seeing that Abraham shall surely become a great and mighty nation, and
# all the nations of the earth shall be blessed in him?"
m.step("Gen.18.18")
# ‹הָיוֹ יִהְיֶה לְגוֹי גָּדוֹל וְעָצוּם וְנִבְרְכוּ בוֹ כֹּל גּוֹיֵי
# הָאָרֶץ› fact holds: hayo-yihyeh-to-goy-gadol-and-atzum; and-nivrekhu-vo-
# all-goyei-the-earth
m.fact("hayo_yihyeh_le_goy_gadol_ve_atzum",
       "ve_nivrekhu_vo_kol_goyei_ha_aretz")

# -------------------------- Gen.18.19 · THE_HOUSE_CHARGE -------------------
# כִּי יְדַעְתִּיו לְמַעַן אֲשֶׁר יְצַוֶּה אֶת־בָּנָיו וְאֶת־בֵּיתוֹ
# אַחֲרָיו וְשָׁמְרוּ דֶּרֶךְ יְהוָה לַעֲשׂוֹת צְדָקָה וּמִשְׁפָּט לְמַעַן
# הָבִיא יְהוָה עַל־אַבְרָהָם אֵת אֲשֶׁר־דִּבֶּר עָלָיו
# "For I have known him, to the end that he may command his children and his
# household after him, that they may keep the way of the LORD, to do
# righteousness and justice; to the end that the LORD may bring upon Abraham
# that which He hath spoken of him.'"
m.step("Gen.18.19")
# ‹כִּי יְדַעְתִּיו› fact holds: when-yedativ
m.fact("ki_yedativ")
# ‹וְשָׁמְרוּ דֶּרֶךְ יְהוָה לַעֲשׂוֹת צְדָקָה וּמִשְׁפָּט› fact holds: and-
# shamru-derekh-the-LORD-to-making-tzedaqah-and-mishpat
m.fact("ve_shamru_derekh_YHWH_la_asot_tzedaqah_u_mishpat")
# ‹לְמַעַן הָבִיא יְהוָה עַל־אַבְרָהָם אֵת אֲשֶׁר־דִּבֶּר עָלָיו› fact
# holds: lemaan-havi-the-LORD-upon-avraham-which-diber
m.fact("lemaan_havi_YHWH_al_avraham_et_asher_diber")

# -------------------------- Gen.18.20 · THE_OUTCRY_DOUBLED -----------------
# וַיֹּאמֶר יְהוָה זַעֲקַת סְדֹם וַעֲמֹרָה כִּי־רָבָּה וְחַטָּאתָם כִּי
# כָבְדָה מְאֹד
# "And the LORD said: 'Verily, the cry of Sodom and Gomorrah is great, and,
# verily, their sin is exceeding grievous."
m.step("Gen.18.20")
# ‹וַיֹּאמֶר יְהוָה› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹זַעֲקַת סְדֹם וַעֲמֹרָה כִּי־רָבָּה וְחַטָּאתָם כִּי כָבְדָה מְאֹד› fact
# holds: zaaqat-sedom-and-amorah-when-rabah; chatatam-when-khavdah-very
m.fact("zaaqat_sedom_va_amorah_ki_rabah",
       "chatatam_ki_khavdah_meod")
# ‹וַעֲמֹרָה› reads without prior install (flag, not fix): amora
m.presupposed("amora")

# -------------------------- Gen.18.21 · THE_DESCEND_COHORTATIVE_RETURNS ----
# אֵרֲדָה־נָּא וְאֶרְאֶה הַכְּצַעֲקָתָהּ הַבָּאָה אֵלַי עָשׂוּ כָּלָה
# וְאִם־לֹא אֵדָעָה
# "I will go down now, and see whether they have done altogether according
# to the cry of it, which is come unto Me; and if not, I will know.'"
m.step("Gen.18.21")
# ‹אֵרֲדָה־נָּא וְאֶרְאֶה› fact holds: eradah-na-and-ereh
m.fact("eradah_na_ve_ereh")
# ‹הַכְּצַעֲקָתָהּ הַבָּאָה אֵלַי עָשׂוּ כָּלָה וְאִם־לֹא אֵדָעָה› fact
# holds: the-like-tzaaqatah-asu-kalah; and-if-not-edaah
m.fact("ha_ke_tzaaqatah_asu_kalah",
       "ve_im_lo_edaah")

# -------------------------- Gen.18.22 · STILL_STANDING_BEFORE_YHWH ---------
# וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים וַיֵּלְכוּ סְדֹמָה וְאַבְרָהָם עוֹדֶנּוּ
# עֹמֵד לִפְנֵי יְהוָה
# "And the men turned from thence, and went toward Sodom; but Abraham stood
# yet before the LORD."
m.step("Gen.18.22")
# ‹וַיִּפְנוּ מִשָּׁם הָאֲנָשִׁים וַיֵּלְכוּ סְדֹמָה› event: turn-go — agent
# shelosha-anashim
m.event("turn_go", agent="shelosha_anashim")
# ‹וְאַבְרָהָם עוֹדֶנּוּ עֹמֵד לִפְנֵי יְהוָה› fact holds: and-avraham-
# odenu-omed-lifnei-the-LORD
m.fact("ve_avraham_odenu_omed_lifnei_YHWH")

# -------------------------- Gen.18.23 · THE_APPROACH_AND_THE_FIFTY ---------
# וַיִּגַּשׁ אַבְרָהָם וַיֹּאמַר הַאַף תִּסְפֶּה צַדִּיק עִם־רָשָׁע … אוּלַי
# יֵשׁ חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר … חָלִלָה לְּךָ מֵעֲשֹׂת
# כַּדָּבָר הַזֶּה … הֲשֹׁפֵט כָּל־הָאָרֶץ לֹא יַעֲשֶׂה מִשְׁפָּט …
# וַיֹּאמֶר יְהוָה אִם־אֶמְצָא בִסְדֹם חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר
# וְנָשָׂאתִי לְכָל־הַמָּקוֹם בַּעֲבוּרָם
# "[EN-AID/JPS 18:23-26] And Abraham drew near, and said: 'Will You indeed
# sweep away the righteous with the wicked? Peradventure there are fifty
# righteous within the city... That be far from Thee... shall not the judge
# of all the earth do justly?' And the LORD said: 'If I find in Sodom fifty
# righteous within the city, then I will forgive all the place for their
# sake.'"
m.step("Gen.18.23")
# ‹וַיִּגַּשׁ אַבְרָהָם› event: approach — agent avraham
m.event("approach", agent="avraham")
# ‹הַאַף תִּסְפֶּה צַדִּיק עִם־רָשָׁע אוּלַי יֵשׁ חֲמִשִּׁים צַדִּיקִם
# בְּתוֹךְ הָעִיר› fact holds: the-af-tispeh-tzaddiq-if-rasha; ulay-yesh-
# chamishim-tzaddiqim
m.fact("ha_af_tispeh_tzaddiq_im_rasha",
       "ulay_yesh_chamishim_tzaddiqim")
# ‹חָלִלָה לְּךָ … הֲשֹׁפֵט כָּל־הָאָרֶץ לֹא יַעֲשֶׂה מִשְׁפָּט› fact holds:
# chalilah-to-you-the-shofet-all-the-earth-not-yaaseh-mishpat
m.fact("chalilah_lekha_ha_shofet_kol_ha_aretz_lo_yaaseh_mishpat")
# ‹אִם־אֶמְצָא בִסְדֹם חֲמִשִּׁים צַדִּיקִם בְּתוֹךְ הָעִיר וְנָשָׂאתִי
# לְכָל־הַמָּקוֹם בַּעֲבוּרָם› fact holds: if-emtza-chamishim-and-nasati-to-
# all-the-maqom
m.fact("im_emtza_chamishim_ve_nasati_le_khol_ha_maqom")

# -------------------------- Gen.18.27 · THE_DESCENDING_LADDER --------------
# וַיַּעַן אַבְרָהָם וַיֹּאמַר הִנֵּה־נָא הוֹאַלְתִּי לְדַבֵּר אֶל־אֲדֹנָי
# וְאָנֹכִי עָפָר וָאֵפֶר … אוּלַי יַחְסְרוּן חֲמִשִּׁים הַצַּדִּיקִם
# חֲמִשָּׁה … לֹא אַשְׁחִית אִם־אֶמְצָא שָׁם אַרְבָּעִים וַחֲמִשָּׁה …
# אַל־נָא יִחַר לַאדֹנָי וַאֲדַבֵּרָה … אַךְ־הַפַּעַם אוּלַי יִמָּצְאוּן
# שָׁם עֲשָׂרָה וַיֹּאמֶר לֹא אַשְׁחִית בַּעֲבוּר הָעֲשָׂרָה
# "[EN-AID/JPS 18:27-32] And Abraham answered and said: 'Behold now, I have
# taken upon me to speak unto the Lord, who am but dust and ashes.
# Peradventure there shall lack five of the fifty righteous...' ...'Oh, let
# not the Lord be angry, and I will speak yet but this once. Peradventure
# ten shall be found there.' And He said: 'I will not destroy it for the
# ten's sake.'"
m.step("Gen.18.27")
# ‹וַיַּעַן אַבְרָהָם וַיֹּאמַר› event: answer — agent avraham
m.event("answer", agent="avraham")
# ‹אַל־נָא יִחַר לַאדֹנָי וַאֲדַבֵּרָה› avraham speaks a demand — LET-NOT:
# yichar(to-adonai)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai)")
# ‹אַל־נָא יִחַר לַאדֹנָי וַאֲדַבְּרָה אַךְ־הַפַּעַם› avraham speaks a
# demand — LET-NOT: yichar(to-adonai, akh-the-paam)
m.declare("avraham", "LET-NOT",
          "yichar(le_adonai, akh_ha_paam)")
# ‹לֹא אַשְׁחִית … לֹא אֶעֱשֶׂה … לֹא אַשְׁחִית בַּעֲבוּר הָעֲשָׂרָה› fact
# holds: not-ashchit-in-the-avur-the-asarah
m.fact("lo_ashchit_ba_avur_ha_asarah")

# -------------------------- Gen.18.33 · THE_EXIT_FORMULA -------------------
# וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר כִּלָּה לְדַבֵּר אֶל־אַבְרָהָם וְאַבְרָהָם שָׁב
# לִמְקֹמוֹ
# "And the LORD went His way, as soon as He had left off speaking to
# Abraham; and Abraham returned unto his place."
m.step("Gen.18.33")
# ‹וַיֵּלֶךְ יְהוָה כַּאֲשֶׁר כִּלָּה לְדַבֵּר› event: depart — agent the-
# LORD
m.event("depart", agent="YHWH")
# ‹וְאַבְרָהָם שָׁב לִמְקֹמוֹ› event: return — agent avraham
m.event("return", agent="avraham")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shelosha_anashim'}
    assert m.presupposed_set() == {'amora', 'mamre', 'sedom'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['taavor(me_al_avdekha)', 'yuqach(meat_mayim)', 'rachatzu_ve_hishaanu(raglekhem)', 'saadu(libkhem)', 'mahari_lushi_va_asi(ugot)', 'yichar(le_adonai)', 'yichar(le_adonai, akh_ha_paam)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['yoshev_petach_ha_ohel_ke_chom_ha_yom', 've_eqchah_fat_lechem', 'ken_taaseh_ka_asher_dibarta', 've_hu_omed_aleihem_tachat_ha_etz', 'shov_ashuv_elekha_ka_et_chayah', 'hinneh_ven_le_sarah', 'zeqenim_baim_ba_yamim', 'chadal_orach_ka_nashim', 'acharei_veloti_haytah_li_ednah_va_adoni_zaqen', 'ha_yipale_me_YHWH_davar', 'la_moed_ashuv_elekha_u_le_sarah_ven', 'hayo_yihyeh_le_goy_gadol_ve_atzum', 've_nivrekhu_vo_kol_goyei_ha_aretz', 'ki_yedativ', 've_shamru_derekh_YHWH_la_asot_tzedaqah_u_mishpat', 'lemaan_havi_YHWH_al_avraham_et_asher_diber', 'zaaqat_sedom_va_amorah_ki_rabah', 'chatatam_ki_khavdah_meod', 'eradah_na_ve_ereh', 'ha_ke_tzaaqatah_asu_kalah', 've_im_lo_edaah', 've_avraham_odenu_omed_lifnei_YHWH', 'ha_af_tispeh_tzaddiq_im_rasha', 'ulay_yesh_chamishim_tzaddiqim', 'chalilah_lekha_ha_shofet_kol_ha_aretz_lo_yaaseh_mishpat', 'im_emtza_chamishim_ve_nasati_le_khol_ha_maqom', 'lo_ashchit_ba_avur_ha_asarah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 29
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_35_sodom_overthrow_cave
###############################################################################
# =============================================================================
# gen_35_sodom_overthrow_cave — 19:1-38
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_35_sodom_overthrow_cave.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The two angels, the overthrow of Sodom, the pillar, the cave (19:1-38)"""
from machine import Machine

m = Machine("gen_35_sodom_overthrow_cave")

# -------------------------- Gen.19.1 · TWO_ANGELS_AT_THE_GATE --------------
# וַיָּבֹאוּ שְׁנֵי הַמַּלְאָכִים סְדֹמָה בָּעֶרֶב וְלוֹט יֹשֵׁב
# בְּשַׁעַר־סְדֹם וַיַּרְא־לוֹט וַיָּקָם לִקְרָאתָם וַיִּשְׁתַּחוּ אַפַּיִם
# אָרְצָה
# "And the two angels came to Sodom at even; and Lot sat in the gate of
# Sodom; and Lot saw them, and rose up to meet them; and he fell down on his
# face to the earth;"
m.step("Gen.19.1")
# ‹שְׁנֵי הַמַּלְאָכִים› the world gains: shnei-the-malakhim
m.install("shnei_ha_malakhim")
# ‹סְדֹמָה … בְּשַׁעַר־סְדֹם› reads without prior install (flag, not fix):
# sedom
m.presupposed("sedom")
# ‹וַיָּקָם לִקְרָאתָם וַיִּשְׁתַּחוּ אַפַּיִם אָרְצָה› event: bow — agent
# lot
m.event("bow", agent="lot")

# -------------------------- Gen.19.2 · THE_COPIED_TRIPLE_AND_THE_REFUSAL ---
# וַיֹּאמֶר הִנֶּה נָּא־אֲדֹנַי סוּרוּ נָא אֶל־בֵּית עַבְדְּכֶם וְלִינוּ
# וְרַחֲצוּ רַגְלֵיכֶם וְהִשְׁכַּמְתֶּם וַהֲלַכְתֶּם לְדַרְכְּכֶם
# וַיֹּאמְרוּ לֹּא כִּי בָרְחוֹב נָלִין
# "and he said: 'Behold now, my lords, turn aside, I pray you, into your
# servant's house, and tarry all night, and wash your feet, and ye shall
# rise up early, and go on your way.' And they said: 'Nay; but we will abide
# in the broad place all night.'"
m.step("Gen.19.2")
# ‹סוּרוּ נָא … וְלִינוּ וְרַחֲצוּ רַגְלֵיכֶם› lot speaks a demand — LET:
# suru-linu-and-rachatzu(raglekhem)
m.declare("lot", "LET",
          "suru_linu_ve_rachatzu(raglekhem)")
# ‹וַיֹּאמְרוּ לֹּא כִּי בָרְחוֹב נָלִין› fact holds: not-when-and-rechov-
# nalin
m.fact("lo_ki_va_rechov_nalin")

# -------------------------- Gen.19.3 · THE_URGING_AND_THE_UNLEAVENED_FEAST -
# וַיִּפְצַר־בָּם מְאֹד וַיָּסֻרוּ אֵלָיו וַיָּבֹאוּ אֶל־בֵּיתוֹ וַיַּעַשׂ
# לָהֶם מִשְׁתֶּה וּמַצּוֹת אָפָה וַיֹּאכֵלוּ
# "And he urged them greatly; and they turned in unto him, and entered into
# his house; and he made them a feast, and did bake unleavened bread, and
# they did eat."
m.step("Gen.19.3")
# ‹וַיִּפְצַר־בָּם מְאֹד› event: urge — agent lot
m.event("urge", agent="lot")
# ‹וַיָּסֻרוּ אֵלָיו וַיָּבֹאוּ אֶל־בֵּיתוֹ› fact holds: and-yasuru-to-him-
# and-yavou
m.fact("va_yasuru_elav_va_yavou")
# ‹וַיַּעַשׂ לָהֶם מִשְׁתֶּה וּמַצּוֹת אָפָה וַיֹּאכֵלוּ› event: feast —
# agent lot; theme mishteh-and-matzot
m.event("feast", agent="lot", themes=["mishteh_u_matzot"])

# -------------------------- Gen.19.4 · THE_SIEGE_RING ----------------------
# טֶרֶם יִשְׁכָּבוּ וְאַנְשֵׁי הָעִיר אַנְשֵׁי סְדֹם נָסַבּוּ עַל־הַבַּיִת
# מִנַּעַר וְעַד־זָקֵן כָּל־הָעָם מִקָּצֶה
# "But before they lay down, the men of the city, even the men of Sodom,
# compassed the house round, both young and old, all the people from every
# quarter."
m.step("Gen.19.4")
# ‹אַנְשֵׁי הָעִיר אַנְשֵׁי סְדֹם› the world gains: men-of-sedom
m.install("anshei_sedom")
# ‹טֶרֶם יִשְׁכָּבוּ … נָסַבּוּ› note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.19.5 · THE_WHERE_WEAPONIZED ----------------
# וַיִּקְרְאוּ אֶל־לוֹט וַיֹּאמְרוּ לוֹ אַיֵּה הָאֲנָשִׁים אֲשֶׁר־בָּאוּ
# אֵלֶיךָ הַלָּיְלָה הוֹצִיאֵם אֵלֵינוּ וְנֵדְעָה אֹתָם
# "And they called unto Lot, and said unto him: 'Where are the men that came
# in to thee this night? bring them out unto us, that we may know them.'"
m.step("Gen.19.5")
# ‹אַיֵּה הָאֲנָשִׁים אֲשֶׁר־בָּאוּ אֵלֶיךָ הַלָּיְלָה› fact holds: ayeh-
# the-anashim-which-bau
m.fact("ayeh_ha_anashim_asher_bau")
# ‹הוֹצִיאֵם אֵלֵינוּ› men-of-sedom speaks a demand — LET: hotziem(to-the-
# anashim)
m.declare("anshei_sedom", "LET",
          "hotziem(el_ha_anashim)")
# ‹וְנֵדְעָה אֹתָם› men-of-sedom speaks a demand — CMD-US: nedah(otam)
m.declare("anshei_sedom", "CMD-US",
          "nedah(otam)")

# -------------------------- Gen.19.6 · THE_DOOR_SHUT_BEHIND ----------------
# וַיֵּצֵא אֲלֵהֶם לוֹט הַפֶּתְחָה וְהַדֶּלֶת סָגַר אַחֲרָיו
# "And Lot went out unto them to the door, and shut the door after him."
m.step("Gen.19.6")
# ‹וַיֵּצֵא … וְהַדֶּלֶת סָגַר אַחֲרָיו› event: exit-shut — agent lot
m.event("exit_shut", agent="lot")

# -------------------------- Gen.19.7 · THE_BROTHERS_PLEA -------------------
# וַיֹּאמַר אַל־נָא אַחַי תָּרֵעוּ
# "And he said: 'I pray you, my brethren, do not so wickedly."
m.step("Gen.19.7")
# ‹אַל־נָא אַחַי תָּרֵעוּ› fact holds: upon-na-achai-tareu
m.fact("al_na_achai_tareu")

# -------------------------- Gen.19.8 · THE_VILE_OFFER_AND_THE_ROOF_LAW -----
# הִנֵּה־נָא לִי שְׁתֵּי בָנוֹת אֲשֶׁר לֹא־יָדְעוּ אִישׁ אוֹצִיאָה־נָּא
# אֶתְהֶן אֲלֵיכֶם וַעֲשׂוּ לָהֶן כַּטּוֹב בְּעֵינֵיכֶם רַק לָאֲנָשִׁים
# הָאֵל אַל־תַּעֲשׂוּ דָבָר כִּי־עַל־כֵּן בָּאוּ בְּצֵל קֹרָתִי
# "Behold now, I have two daughters that have not known man; let me, I pray
# you, bring them out unto you, and do ye to them as is good in your eyes;
# only unto these men do nothing; forasmuch as they are come under the
# shadow of my roof.'"
m.step("Gen.19.8")
# ‹שְׁתֵּי בָנוֹת אֲשֶׁר לֹא־יָדְעוּ אִישׁ› the world gains: shtei-the-
# daughters
m.install("shtei_ha_banot")
# ‹וַעֲשׂוּ לָהֶן כַּטּוֹב בְּעֵינֵיכֶם› lot speaks a demand — LET:
# asu(lahen-like-good-in-your-eyes)
m.declare("lot", "LET",
          "asu(lahen_ka_tov_be_eineikhem)")
# ‹רַק לָאֲנָשִׁים הָאֵל אַל־תַּעֲשׂוּ דָבָר› lot speaks a demand — LET-NOT:
# taasu(to-anashim-the-to-davar)
m.declare("lot", "LET-NOT",
          "taasu(la_anashim_ha_el_davar)")

# -------------------------- Gen.19.9 · THE_JUDGE_TAUNT_AND_THE_DOOR_RUSH ---
# וַיֹּאמְרוּ גֶּשׁ־הָלְאָה וַיֹּאמְרוּ הָאֶחָד בָּא־לָגוּר וַיִּשְׁפֹּט
# שָׁפוֹט עַתָּה נָרַע לְךָ מֵהֶם וַיִּפְצְרוּ בָאִישׁ בְּלוֹט מְאֹד
# וַיִּגְּשׁוּ לִשְׁבֹּר הַדָּלֶת
# "And they said: 'Stand back.' And they said: 'This one fellow came in to
# sojourn, and he will needs play the judge; now will we deal worse with
# thee, than with them.' And they pressed sore upon the man, even Lot, and
# drew near to break the door."
m.step("Gen.19.9")
# ‹גֶּשׁ־הָלְאָה› men-of-sedom speaks a demand — LET: gesh-halah(lot)
m.declare("anshei_sedom", "LET",
          "gesh_halah(lot)")
# ‹הָאֶחָד בָּא־לָגוּר וַיִּשְׁפֹּט שָׁפוֹט עַתָּה נָרַע לְךָ מֵהֶם› fact
# holds: and-yishpot-shafot; nara-to-you-mehem
m.fact("va_yishpot_shafot",
       "nara_lekha_mehem")

# -------------------------- Gen.19.10 · THE_INVERTED_RESCUE ----------------
# וַיִּשְׁלְחוּ הָאֲנָשִׁים אֶת־יָדָם וַיָּבִיאוּ אֶת־לוֹט אֲלֵיהֶם
# הַבָּיְתָה וְאֶת־הַדֶּלֶת סָגָרוּ
# "But the men put forth their hand, and brought Lot into the house to them,
# and the door they shut."
m.step("Gen.19.10")
# ‹וַיָּבִיאוּ אֶת־לוֹט אֲלֵיהֶם הַבָּיְתָה וְאֶת־הַדֶּלֶת סָגָרוּ› event:
# pull-in — agent shnei-the-malakhim; theme lot
m.event("pull_in", agent="shnei_ha_malakhim", themes=["lot"])

# -------------------------- Gen.19.11 · THE_BLINDNESS ----------------------
# וְאֶת־הָאֲנָשִׁים אֲשֶׁר־פֶּתַח הַבַּיִת הִכּוּ בַּסַּנְוֵרִים מִקָּטֹן
# וְעַד־גָּדוֹל וַיִּלְאוּ לִמְצֹא הַפָּתַח
# "And they smote the men that were at the door of the house with blindness,
# both small and great; so that they wearied themselves to find the door."
m.step("Gen.19.11")
# ‹הִכּוּ בַּסַּנְוֵרִים› event: smite-blind — agent shnei-the-malakhim;
# theme men-of-sedom
m.event("smite_blind", agent="shnei_ha_malakhim", themes=["anshei_sedom"])

# -------------------------- Gen.19.12 · THE_EVACUATION_COMMAND -------------
# וַיֹּאמְרוּ הָאֲנָשִׁים אֶל־לוֹט עֹד מִי־לְךָ פֹה חָתָן וּבָנֶיךָ
# וּבְנֹתֶיךָ וְכֹל אֲשֶׁר־לְךָ בָּעִיר הוֹצֵא מִן־הַמָּקוֹם
# "And the men said unto Lot: 'Hast thou here any besides? son-in-law, and
# thy sons, and thy daughters, and whomsoever thou hast in the city; bring
# them out of the place;"
m.step("Gen.19.12")
# ‹הוֹצֵא מִן־הַמָּקוֹם› the-malakhim speaks a demand — LET: bring-out(all-
# which-to-you-from-the-maqom)
m.declare("ha_malakhim", "LET",
          "hotze(kol_asher_lekha_min_ha_maqom)")

# -------------------------- Gen.19.13 · THE_MISSION_STATEMENT --------------
# כִּי־מַשְׁחִתִים אֲנַחְנוּ אֶת־הַמָּקוֹם הַזֶּה כִּי־גָדְלָה צַעֲקָתָם
# אֶת־פְּנֵי יְהוָה וַיְשַׁלְּחֵנוּ יְהוָה לְשַׁחֲתָהּ
# "for we will destroy this place, because the cry of them is waxed great
# before the LORD; and the LORD hath sent us to destroy it.'"
m.step("Gen.19.13")
# ‹כִּי־מַשְׁחִתִים אֲנַחְנוּ … כִּי־גָדְלָה צַעֲקָתָם … וַיְשַׁלְּחֵנוּ
# יְהוָה› fact holds: mashchitim-anachnu-the-maqom; gadlah-tzaaqatam-and-
# yeshalchenu-the-LORD
m.fact("mashchitim_anachnu_et_ha_maqom",
       "gadlah_tzaaqatam_va_yeshalchenu_YHWH")

# -------------------------- Gen.19.14 · THE_MOCKED_DEMAND ------------------
# וַיֵּצֵא לוֹט וַיְדַבֵּר אֶל־חֲתָנָיו לֹקְחֵי בְנֹתָיו וַיֹּאמֶר קוּמוּ
# צְּאוּ מִן־הַמָּקוֹם הַזֶּה כִּי־מַשְׁחִית יְהוָה אֶת־הָעִיר וַיְהִי
# כִמְצַחֵק בְּעֵינֵי חֲתָנָיו
# "And Lot went out, and spoke unto his sons-in-law, who married his
# daughters, and said: 'Up, get you out of this place; for the LORD will
# destroy the city.' But he seemed unto his sons-in-law as one that jested."
m.step("Gen.19.14")
# ‹קוּמוּ צְּאוּ מִן־הַמָּקוֹם הַזֶּה› lot speaks a demand — LET: qumu-
# tzeu(from-the-maqom)
m.declare("lot", "LET",
          "qumu_tzeu(min_ha_maqom)")
# ‹וַיְהִי כִמְצַחֵק בְּעֵינֵי חֲתָנָיו› fact holds: and-yehi-khi-metzacheq-
# in-eyes-of-chatanav
m.fact("va_yehi_khi_metzacheq_be_einei_chatanav")

# -------------------------- Gen.19.15 · DAWN_AND_THE_PAIR_TO_LOT -----------
# וּכְמוֹ הַשַּׁחַר עָלָה וַיָּאִיצוּ הַמַּלְאָכִים בְּלוֹט לֵאמֹר קוּם קַח
# אֶת־אִשְׁתְּךָ וְאֶת־שְׁתֵּי בְנֹתֶיךָ הַנִּמְצָאֹת פֶּן־תִּסָּפֶה
# בַּעֲוֺן הָעִיר
# "And when the morning arose, then the angels hastened Lot, saying: 'Arise,
# take thy wife, and thy two daughters that are here; lest thou be swept
# away in the iniquity of the city.'"
m.step("Gen.19.15")
# ‹קוּם קַח אֶת־אִשְׁתְּךָ וְאֶת־שְׁתֵּי בְנֹתֶיךָ› the-malakhim speaks a
# demand — LET: qum-qach(ishtekha-and-shtei-venotekha)
m.declare("ha_malakhim", "LET",
          "qum_qach(ishtekha_u_shtei_venotekha)")

# -------------------------- Gen.19.16 · THE_LINGERING_AND_THE_SEIZURE ------
# וַיִּתְמַהְמָהּ וַיַּחֲזִיקוּ הָאֲנָשִׁים בְּיָדוֹ וּבְיַד־אִשְׁתּוֹ
# וּבְיַד שְׁתֵּי בְנֹתָיו בְּחֶמְלַת יְהוָה עָלָיו וַיֹּצִאֻהוּ
# וַיַּנִּחֻהוּ מִחוּץ לָעִיר
# "But he lingered; and the men laid hold upon his hand, and upon the hand
# of his wife, and upon the hand of his two daughters; the LORD being
# merciful unto him. And they brought him forth, and set him without the
# city."
m.step("Gen.19.16")
# ‹וַיִּתְמַהְמָהּ וַיַּחֲזִיקוּ הָאֲנָשִׁים בְּיָדוֹ … וַיֹּצִאֻהוּ› event:
# seize-carry — agent shnei-the-malakhim; theme lot-and-veito
m.event("seize_carry", agent="shnei_ha_malakhim", themes=["lot_u_veito"])

# -------------------------- Gen.19.17 · THE_ESCAPE_SPEECH ------------------
# וַיְהִי כְהוֹצִיאָם אֹתָם הַחוּצָה וַיֹּאמֶר הִמָּלֵט עַל־נַפְשֶׁךָ
# אַל־תַּבִּיט אַחֲרֶיךָ וְאַל־תַּעֲמֹד בְּכָל־הַכִּכָּר הָהָרָה הִמָּלֵט
# פֶּן־תִּסָּפֶה
# "And it came to pass, when they had brought them forth abroad, that he
# said: 'Escape for thy life; look not behind thee, neither stay thou in all
# the Plain; escape to the mountain, lest thou be swept away.'"
m.step("Gen.19.17")
# ‹הִמָּלֵט עַל־נַפְשֶׁךָ … הָהָרָה הִמָּלֵט› the-malakhim speaks a demand —
# LET: himalet(upon-nafshekha)
m.declare("ha_malakhim", "LET",
          "himalet(al_nafshekha)")
# ‹אַל־תַּבִּיט אַחֲרֶיךָ› the-malakhim speaks a demand — LET-NOT:
# tabit(acharekha)
m.declare("ha_malakhim", "LET-NOT",
          "tabit(acharekha)")
# ‹וְאַל־תַּעֲמֹד בְּכָל־הַכִּכָּר› the-malakhim speaks a demand — LET-NOT:
# taamod(in-all-the-kikar)
m.declare("ha_malakhim", "LET-NOT",
          "taamod(be_khol_ha_kikar)")

# -------------------------- Gen.19.18 · THE_VERBLESS_NO --------------------
# וַיֹּאמֶר לוֹט אֲלֵהֶם אַל־נָא אֲדֹנָי
# "And Lot said unto them: 'Oh, not so, my lord;"
m.step("Gen.19.18")
# ‹אַל־נָא אֲדֹנָי› fact holds: upon-na-adonai
m.fact("al_na_adonai")

# -------------------------- Gen.19.19 · THE_INABILITY_CLAIM ----------------
# הִנֵּה־נָא מָצָא עַבְדְּךָ חֵן בְּעֵינֶיךָ וַתַּגְדֵּל חַסְדְּךָ אֲשֶׁר
# עָשִׂיתָ עִמָּדִי לְהַחֲיוֹת אֶת־נַפְשִׁי וְאָנֹכִי לֹא אוּכַל לְהִמָּלֵט
# הָהָרָה פֶּן־תִּדְבָּקַנִי הָרָעָה וָמַתִּי
# "behold now, thy servant hath found grace in thy sight, and thou hast
# magnified thy mercy, which thou hast shown unto me in saving my life; and
# I cannot escape to the mountain, lest the evil overtake me, and I die."
m.step("Gen.19.19")
# ‹מָצָא עַבְדְּךָ חֵן … וְאָנֹכִי לֹא אוּכַל לְהִמָּלֵט› fact holds: matza-
# chen-and-tagdel-chasdekha; not-ukhal-to-himalet
m.fact("matza_chen_va_tagdel_chasdekha",
       "lo_ukhal_le_himalet")

# -------------------------- Gen.19.20 · THE_LITTLE_CITY_PLEA ---------------
# הִנֵּה־נָא הָעִיר הַזֹּאת קְרֹבָה לָנוּס שָׁמָּה וְהִוא מִצְעָר אִמָּלְטָה
# נָּא שָׁמָּה הֲלֹא מִצְעָר הִוא וּתְחִי נַפְשִׁי
# "Behold now, this city is near to flee unto, and it is a little one; oh,
# let me escape thither—is it not a little one?—and my soul shall live.'"
m.step("Gen.19.20")
# ‹אִמָּלְטָה נָּא שָׁמָּה הֲלֹא מִצְעָר הִוא› fact holds: imaltah-na-
# shamah-the-not-mitzar-hi
m.fact("imaltah_na_shamah_ha_lo_mitzar_hi")

# -------------------------- Gen.19.21 · THE_GRANT --------------------------
# וַיֹּאמֶר אֵלָיו הִנֵּה נָשָׂאתִי פָנֶיךָ גַּם לַדָּבָר הַזֶּה לְבִלְתִּי
# הָפְכִּי אֶת־הָעִיר אֲשֶׁר דִּבַּרְתָּ
# "And he said unto him: 'See, I have accepted thee concerning this thing
# also, that I will not overthrow the city of which thou hast spoken."
m.step("Gen.19.21")
# ‹נָשָׂאתִי פָנֶיךָ … לְבִלְתִּי הָפְכִּי אֶת־הָעִיר› fact holds: nasati-
# fanekha-to-vilti-hofki-the-ir
m.fact("nasati_fanekha_le_vilti_hofki_et_ha_ir")

# -------------------------- Gen.19.22 · HURRY_AND_THE_REPORT_NAMING --------
# מַהֵר הִמָּלֵט שָׁמָּה כִּי לֹא אוּכַל לַעֲשׂוֹת דָּבָר עַד־בֹּאֲךָ
# שָׁמָּה עַל־כֵּן קָרָא שֵׁם־הָעִיר צוֹעַר
# "Hasten thou, escape thither; for I cannot do any thing till thou be come
# thither.'—Therefore the name of the city was called Zoar.—"
m.step("Gen.19.22")
# ‹מַהֵר הִמָּלֵט שָׁמָּה› the-malakhim speaks a demand — LET: maher-
# himalet(shamah)
m.declare("ha_malakhim", "LET",
          "maher_himalet(shamah)")
# ‹עַל־כֵּן קָרָא שֵׁם־הָעִיר צוֹעַר› pattern recorded: upon-ken-qara-shem-
# the-ir-tzoar
m.pattern("al_ken_qara_shem_ha_ir_tzoar")
# ‹צוֹעַר› reads without prior install (flag, not fix): tzoar
m.presupposed("tzoar")

# -------------------------- Gen.19.23 · SUNRISE_AT_TZOAR -------------------
# הַשֶּׁמֶשׁ יָצָא עַל־הָאָרֶץ וְלוֹט בָּא צֹעֲרָה
# "The sun was risen upon the earth when Lot came unto Zoar."
m.step("Gen.19.23")
# ‹הַשֶּׁמֶשׁ יָצָא … וְלוֹט בָּא› fact holds: the-shemesh-yatza-and-lot-in-
# the-tzoarah
m.fact("ha_shemesh_yatza_ve_lot_ba_tzoarah")
# ‹הַשֶּׁמֶשׁ יָצָא עַל־הָאָרֶץ› note: zero events in this verse
m.note_zero_events()

# -------------------------- Gen.19.24 · THE_FIRE_RAIN ----------------------
# וַיהוָה הִמְטִיר עַל־סְדֹם וְעַל־עֲמֹרָה גָּפְרִית וָאֵשׁ מֵאֵת יְהוָה
# מִן־הַשָּׁמָיִם
# "Then the LORD caused to rain upon Sodom and upon Gomorrah brimstone and
# fire from the LORD out of heaven;"
m.step("Gen.19.24")
# ‹וַיהוָה הִמְטִיר … גָּפְרִית וָאֵשׁ› event: rain-fire — agent the-LORD;
# theme sedom-and-amorah
m.event("rain_fire", agent="YHWH", themes=["sedom_va_amorah"])
# ‹וְעַל־עֲמֹרָה› reads without prior install (flag, not fix): amora
m.presupposed("amora")

# -------------------------- Gen.19.25 · THE_OVERTHROW ----------------------
# וַיַּהֲפֹךְ אֶת־הֶעָרִים הָאֵל וְאֵת כָּל־הַכִּכָּר וְאֵת כָּל־יֹשְׁבֵי
# הֶעָרִים וְצֶמַח הָאֲדָמָה
# "and He overthrow those cities, and all the Plain, and all the inhabitants
# of the cities, and that which grew upon the ground."
m.step("Gen.19.25")
# ‹וַיַּהֲפֹךְ אֶת־הֶעָרִים הָאֵל› event: overturn — agent the-LORD; theme
# he-arim-and-the-kikar
m.event("overturn", agent="YHWH", themes=["he_arim_ve_ha_kikar"])

# -------------------------- Gen.19.26 · THE_BREACH_AND_THE_PILLAR ----------
# וַתַּבֵּט אִשְׁתּוֹ מֵאַחֲרָיו וַתְּהִי נְצִיב מֶלַח
# "But his wife looked back from behind him, and she became a pillar of
# salt."
m.step("Gen.19.26")
# ‹וַתַּבֵּט אִשְׁתּוֹ מֵאַחֲרָיו› event: look-back — agent wife-of-lot
m.event("look_back", agent="eshet_lot")
# ‹וַתְּהִי נְצִיב מֶלַח› fact holds: and-tehi-netziv-melach
m.fact("va_tehi_netziv_melach")

# -------------------------- Gen.19.27 · THE_DAWN_RETURN_TO_THE_STANDING_PLACE -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר אֶל־הַמָּקוֹם אֲשֶׁר־עָמַד שָׁם
# אֶת־פְּנֵי יְהוָה
# "And Abraham got up early in the morning to the place where he had stood
# before the LORD."
m.step("Gen.19.27")
# ‹וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר אֶל־הַמָּקוֹם אֲשֶׁר־עָמַד שָׁם› event:
# dawn-return — agent avraham
m.event("dawn_return", agent="avraham")

# -------------------------- Gen.19.28 · THE_KILN_SMOKE ---------------------
# וַיַּשְׁקֵף עַל־פְּנֵי סְדֹם וַעֲמֹרָה וְעַל־כָּל־פְּנֵי אֶרֶץ הַכִּכָּר
# וַיַּרְא וְהִנֵּה עָלָה קִיטֹר הָאָרֶץ כְּקִיטֹר הַכִּבְשָׁן
# "And he looked out toward Sodom and Gomorrah, and toward all the land of
# the Plain, and beheld, and, lo, the smoke of the land went up as the smoke
# of a furnace."
m.step("Gen.19.28")
# ‹וַיַּשְׁקֵף … וַיַּרְא וְהִנֵּה עָלָה קִיטֹר הָאָרֶץ› event: look-down —
# agent avraham
m.event("look_down", agent="avraham")

# -------------------------- Gen.19.29 · THE_REMEMBER_HINGE -----------------
# וַיְהִי בְּשַׁחֵת אֱלֹהִים אֶת־עָרֵי הַכִּכָּר וַיִּזְכֹּר אֱלֹהִים
# אֶת־אַבְרָהָם וַיְשַׁלַּח אֶת־לוֹט מִתּוֹךְ הַהֲפֵכָה בַּהֲפֹךְ
# אֶת־הֶעָרִים אֲשֶׁר־יָשַׁב בָּהֵן לוֹט
# "And it came to pass, when God destroyed the cities of the Plain, that God
# remembered Abraham, and sent Lot out of the midst of the overthrow, when
# He overthrew the cities in which Lot dwelt."
m.step("Gen.19.29")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־אַבְרָהָם› event: remember — agent God; theme
# avraham
m.event("remember", agent="elohim", themes=["avraham"])

# -------------------------- Gen.19.30 · THE_ASCENT_TO_THE_CAVE -------------
# וַיַּעַל לוֹט מִצּוֹעַר וַיֵּשֶׁב בָּהָר וּשְׁתֵּי בְנֹתָיו עִמּוֹ כִּי
# יָרֵא לָשֶׁבֶת בְּצוֹעַר וַיֵּשֶׁב בַּמְּעָרָה הוּא וּשְׁתֵּי בְנֹתָיו
# "And Lot went up out of Zoar, and dwelt in the mountain, and his two
# daughters with him; for he feared to dwell in Zoar; and he dwelt in a
# cave, he and his two daughters."
m.step("Gen.19.30")
# ‹וַיַּעַל לוֹט מִצּוֹעַר … וַיֵּשֶׁב בַּמְּעָרָה› event: ascend-dwell —
# agent lot
m.event("ascend_dwell", agent="lot")

# -------------------------- Gen.19.31 · THE_CAVE_COUNCILS_AND_THE_TWIN_NIGHTS -
# וַתֹּאמֶר הַבְּכִירָה אֶל־הַצְּעִירָה אָבִינוּ זָקֵן … לְכָה נַשְׁקֶה
# אֶת־אָבִינוּ יַיִן וְנִשְׁכְּבָה עִמּוֹ וּנְחַיֶּה מֵאָבִינוּ זָרַע …
# וַתַּשְׁקֶיןָ אֶת־אֲבִיהֶן יַיִן בַּלַּיְלָה הוּא וַתָּבֹא הַבְּכִירָה
# וַתִּשְׁכַּב אֶת־אָבִיהָ … נַשְׁקֶנּוּ יַיִן גַּם־הַלַּיְלָה וּבֹאִי
# שִׁכְבִי עִמּוֹ … וַתַּשְׁקֶיןָ גַּם בַּלַּיְלָה הַהוּא … וַתָּקָם
# הַצְּעִירָה וַתִּשְׁכַּב עִמּוֹ … וַתַּהֲרֶיןָ שְׁתֵּי בְנוֹת־לוֹט
# מֵאֲבִיהֶן
# "[EN-AID/JPS 19:31-36] And the first-born said unto the younger: 'Our
# father is old, and there is not a man in the earth... Come, let us make
# our father drink wine, and we will lie with him, that we may preserve seed
# of our father.' And they made their father drink wine that night. And the
# first-born went in, and lay with her father... 'Let us make him drink wine
# this night also; and go thou in, and lie with him'... And they made their
# father drink wine that night also. And the younger arose, and lay with
# him... Thus were both the daughters of Lot with child by their father."
m.step("Gen.19.31")
# ‹אָבִינוּ זָקֵן וְאִישׁ אֵין בָּאָרֶץ לָבוֹא עָלֵינוּ› fact holds: avinu-
# zaqen-and-man-ein-in-the-earth
m.fact("avinu_zaqen_ve_ish_ein_ba_aretz")
# ‹לְכָה נַשְׁקֶה אֶת־אָבִינוּ יַיִן› the-bekhirah speaks a demand — CMD-
# US?: nashqeh(avinu-yayin)
m.declare("ha_bekhirah", "CMD-US?",
          "nashqeh(et_avinu_yayin)")
# ‹וְנִשְׁכְּבָה עִמּוֹ› the-bekhirah speaks a demand — CMD-US:
# nishkevah(imo)
m.declare("ha_bekhirah", "CMD-US",
          "nishkevah(imo)")
# ‹וַתַּשְׁקֶיןָ אֶת־אֲבִיהֶן יַיִן בַּלַּיְלָה הוּא› demand settled (popped
# from the queue): nashqeh(avinu-yayin)
m.result("nashqeh(et_avinu_yayin)", tmark="t1")
# ‹וַתָּבֹא הַבְּכִירָה וַתִּשְׁכַּב אֶת־אָבִיהָ› demand settled (popped
# from the queue): nishkevah(imo)
m.result("nishkevah(imo)", tmark="t1")
# ‹נַשְׁקֶנּוּ יַיִן גַּם־הַלַּיְלָה› the-bekhirah speaks a demand — CMD-US:
# nashqenu(also-the-lailah)
m.declare("ha_bekhirah", "CMD-US",
          "nashqenu(gam_ha_lailah)")
# ‹וּבֹאִי שִׁכְבִי עִמּוֹ› the-bekhirah speaks a demand — LET: and-voi-
# shikhvi(imo)
m.declare("ha_bekhirah", "LET",
          "u_voi_shikhvi(imo)")
# ‹וַתַּשְׁקֶיןָ גַּם בַּלַּיְלָה הַהוּא אֶת־אֲבִיהֶן יָיִן› demand settled
# (popped from the queue): nashqenu(also-the-lailah)
m.result("nashqenu(gam_ha_lailah)", tmark="t1")
# ‹וַתַּשְׁקֶיןָ … וַתִּשְׁכַּב … וַתַּהֲרֶיןָ› fact holds: and-tashqena-
# avihen-yayin; and-tishkav-and-taharena
m.fact("va_tashqena_et_avihen_yayin",
       "va_tishkav_va_taharena")

# -------------------------- Gen.19.37 · THE_TWO_NAMINGS --------------------
# וַתֵּלֶד הַבְּכִירָה בֵּן וַתִּקְרָא שְׁמוֹ מוֹאָב הוּא אֲבִי־מוֹאָב
# עַד־הַיּוֹם וְהַצְּעִירָה גַם־הִוא יָלְדָה בֵּן וַתִּקְרָא שְׁמוֹ
# בֶּן־עַמִּי הוּא אֲבִי בְנֵי־עַמּוֹן עַד־הַיּוֹם
# "[EN-AID/JPS 19:37-38] And the first-born bore a son, and called his name
# Moab—the same is the father of the Moabites unto this day. And the
# younger, she also bore a son, and called his name Ben-ammi—the same is the
# father of the children of Ammon unto this day."
m.step("Gen.19.37")
# ‹וַתֵּלֶד הַבְּכִירָה בֵּן … וְהַצְּעִירָה גַם־הִוא יָלְדָה בֵּן› the
# world gains: moav, ben-ammi
m.install("moav", "ben_ammi")
# ‹וַתִּקְרָא שְׁמוֹ מוֹאָב … וַתִּקְרָא שְׁמוֹ בֶּן־עַמִּי› named: moav :=
# Moav; ben-ammi := Ben-Ammi
m.name("moav", "Moav")
m.name("ben_ammi", "Ben_Ammi")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'moav', 'ben_ammi', 'anshei_sedom', 'shtei_ha_banot', 'shnei_ha_malakhim'}
    assert m.presupposed_set() == {'sedom', 'amora', 'tzoar'}
    assert m.REGISTRY["names"] == {'moav': 'Moav', 'ben_ammi': 'Ben_Ammi'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['suru_linu_ve_rachatzu(raglekhem)', 'hotziem(el_ha_anashim)', 'nedah(otam)', 'asu(lahen_ka_tov_be_eineikhem)', 'taasu(la_anashim_ha_el_davar)', 'gesh_halah(lot)', 'hotze(kol_asher_lekha_min_ha_maqom)', 'qumu_tzeu(min_ha_maqom)', 'qum_qach(ishtekha_u_shtei_venotekha)', 'himalet(al_nafshekha)', 'tabit(acharekha)', 'taamod(be_khol_ha_kikar)', 'maher_himalet(shamah)', 'u_voi_shikhvi(imo)']
    assert len(m.SPECS["log"]) == 17
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['lo_ki_va_rechov_nalin', 'va_yasuru_elav_va_yavou', 'ayeh_ha_anashim_asher_bau', 'al_na_achai_tareu', 'va_yishpot_shafot', 'nara_lekha_mehem', 'mashchitim_anachnu_et_ha_maqom', 'gadlah_tzaaqatam_va_yeshalchenu_YHWH', 'va_yehi_khi_metzacheq_be_einei_chatanav', 'al_na_adonai', 'matza_chen_va_tagdel_chasdekha', 'lo_ukhal_le_himalet', 'imaltah_na_shamah_ha_lo_mitzar_hi', 'nasati_fanekha_le_vilti_hofki_et_ha_ir', 'pattern: al_ken_qara_shem_ha_ir_tzoar', 'ha_shemesh_yatza_ve_lot_ba_tzoarah', 'va_tehi_netziv_melach', 'avinu_zaqen_ve_ish_ein_ba_aretz', 'va_tashqena_et_avihen_yayin', 'va_tishkav_va_taharena'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 37
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_36_gerar_dream_prophet
###############################################################################
# =============================================================================
# gen_36_gerar_dream_prophet — 20:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_36_gerar_dream_prophet.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Gerar: the dream-court, the prophet's prayer, the shut wombs (20:1-18)"""
from machine import Machine

m = Machine("gen_36_gerar_dream_prophet")

# -------------------------- Gen.20.1 · THE_JOURNEY_TO_GERAR ----------------
# וַיִּסַּע מִשָּׁם אַבְרָהָם אַרְצָה הַנֶּגֶב וַיֵּשֶׁב בֵּין־קָדֵשׁ וּבֵין
# שׁוּר וַיָּגָר בִּגְרָר
# "And Abraham journeyed from thence toward the land of the South, and dwelt
# between Kadesh and Shur; and he sojourned in Gerar."
m.step("Gen.20.1")
# ‹וַיִּסַּע מִשָּׁם אַבְרָהָם … וַיָּגָר בִּגְרָר› event: journey-sojourn —
# agent avraham
m.event("journey_sojourn", agent="avraham")
# ‹בֵּין־קָדֵשׁ וּבֵין שׁוּר … בִּגְרָר› reads without prior install (flag,
# not fix): gerar, qadesh, shur
m.presupposed("gerar", "qadesh", "shur")

# -------------------------- Gen.20.2 · THE_SECOND_CLAIM_AND_THE_TAKING -----
# וַיֹּאמֶר אַבְרָהָם אֶל־שָׂרָה אִשְׁתּוֹ אֲחֹתִי הִוא וַיִּשְׁלַח
# אֲבִימֶלֶךְ מֶלֶךְ גְּרָר וַיִּקַּח אֶת־שָׂרָה
# "And Abraham said of Sarah his wife: 'She is my sister.' And Abimelech
# king of Gerar sent, and took Sarah."
m.step("Gen.20.2")
# ‹אֲחֹתִי הִוא› fact holds: achoti-hi
m.fact("achoti_hi")
# ‹אֲבִימֶלֶךְ מֶלֶךְ גְּרָר› the world gains: avimelekh
m.install("avimelekh")
# ‹וַיִּשְׁלַח … וַיִּקַּח אֶת־שָׂרָה› event: take — agent avimelekh; theme
# sarah
m.event("take", agent="avimelekh", themes=["sarah"])

# -------------------------- Gen.20.3 · THE_DREAM_VERDICT -------------------
# וַיָּבֹא אֱלֹהִים אֶל־אֲבִימֶלֶךְ בַּחֲלוֹם הַלָּיְלָה וַיֹּאמֶר לוֹ
# הִנְּךָ מֵת עַל־הָאִשָּׁה אֲשֶׁר־לָקַחְתָּ וְהִוא בְּעֻלַת בָּעַל
# "But God came to Abimelech in a dream of the night, and said to him:
# 'Behold, thou shalt die, because of the woman whom thou hast taken; for
# she is a man's wife.'"
m.step("Gen.20.3")
# ‹וַיָּבֹא אֱלֹהִים אֶל־אֲבִימֶלֶךְ בַּחֲלוֹם הַלָּיְלָה› event: dream-say
# — agent God
m.event("dream_say", agent="elohim")
# ‹הִנְּךָ מֵת עַל־הָאִשָּׁה אֲשֶׁר־לָקַחְתָּ וְהִוא בְּעֻלַת בָּעַל› fact
# holds: hinkha-met-upon-the-woman; and-hi-beulat-baal
m.fact("hinkha_met_al_ha_ishah",
       "ve_hi_beulat_baal")

# -------------------------- Gen.20.4 · THE_KINGS_COUNT_QUESTION ------------
# וַאֲבִימֶלֶךְ לֹא קָרַב אֵלֶיהָ וַיֹּאמַר אֲדֹנָי הֲגוֹי גַּם־צַדִּיק
# תַּהֲרֹג
# "Now Abimelech had not come near her; and he said: 'Lord, wilt Thou slay
# even a righteous nation?"
m.step("Gen.20.4")
# ‹לֹא קָרַב אֵלֶיהָ … הֲגוֹי גַּם־צַדִּיק תַּהֲרֹג› fact holds: not-qarav-
# eleha; the-goy-also-tzaddiq-taharog
m.fact("lo_qarav_eleha",
       "ha_goy_gam_tzaddiq_taharog")

# -------------------------- Gen.20.5 · THE_INTEGRITY_DEFENSE ---------------
# הֲלֹא הוּא אָמַר־לִי אֲחֹתִי הִוא וְהִיא־גַם־הִוא אָמְרָה אָחִי הוּא
# בְּתָם־לְבָבִי וּבְנִקְיֹן כַּפַּי עָשִׂיתִי זֹאת
# "Said he not himself unto me: She is my sister? and she, even she herself
# said: He is my brother. In the simplicity of my heart and the innocency of
# my hands have I done this.'"
m.step("Gen.20.5")
# ‹הֲלֹא הוּא אָמַר־לִי … בְּתָם־לְבָבִי וּבְנִקְיֹן כַּפַּי› fact holds:
# that-amar-to-me-and-hi-also-hi-amrah; in-tom-levavi-and-and-niqyon-kapai
m.fact("hu_amar_li_ve_hi_gam_hi_amrah",
       "be_tom_levavi_u_ve_niqyon_kapai")

# -------------------------- Gen.20.6 · THE_CONCESSION_AND_THE_WITHHOLDING --
# וַיֹּאמֶר אֵלָיו הָאֱלֹהִים בַּחֲלֹם גַּם אָנֹכִי יָדַעְתִּי כִּי
# בְתָם־לְבָבְךָ עָשִׂיתָ זֹּאת וָאֶחְשֹׂךְ גַּם־אָנֹכִי אוֹתְךָ מֵחֲטוֹ־לִי
# עַל־כֵּן לֹא־נְתַתִּיךָ לִנְגֹּעַ אֵלֶיהָ
# "And God said unto him in the dream: 'Yea, I know that in the simplicity
# of thy heart thou hast done this, and I also withheld thee from sinning
# against Me. Therefore suffered I thee not to touch her."
m.step("Gen.20.6")
# ‹יָדַעְתִּי … וָאֶחְשֹׂךְ … מֵחֲטוֹ־לִי … לֹא־נְתַתִּיךָ לִנְגֹּעַ› fact
# holds: also-anokhi-yadati-and-tom-levavkha; and-echsokh-otkha-from-chato-
# to-me; not-netatikha-lingoa
m.fact("gam_anokhi_yadati_ve_tom_levavkha",
       "va_echsokh_otkha_me_chato_li",
       "lo_netatikha_lingoa")

# -------------------------- Gen.20.7 · THE_PROPHET_AND_THE_RETURN_COMMAND --
# וְעַתָּה הָשֵׁב אֵשֶׁת־הָאִישׁ כִּי־נָבִיא הוּא וְיִתְפַּלֵּל בַּעַדְךָ
# וֶחְיֵה וְאִם־אֵינְךָ מֵשִׁיב דַּע כִּי־מוֹת תָּמוּת אַתָּה
# וְכָל־אֲשֶׁר־לָךְ
# "Now therefore restore the man's wife; for he is a prophet, and he shall
# pray for thee, and thou shalt live; and if thou restore her not, know thou
# that thou shalt surely die, thou, and all that are thine.'"
m.step("Gen.20.7")
# ‹וְעַתָּה הָשֵׁב אֵשֶׁת־הָאִישׁ› God speaks a demand — LET: hashev(wife-
# of-the-man)
m.declare("elohim", "LET",
          "hashev(eshet_ha_ish)")
# ‹וְיִתְפַּלֵּל בַּעַדְךָ וֶחְיֵה› fact holds: and-yitpalel-baadkha-and-
# cheyeh
m.fact("ve_yitpalel_baadkha_ve_cheyeh")
# ‹וְאִם־אֵינְךָ מֵשִׁיב דַּע כִּי־מוֹת תָּמוּת› fact holds: if-einkha-
# meshiv-da-when-dying-you-shall-die
m.fact("im_einkha_meshiv_da_ki_mot_tamut")

# -------------------------- Gen.20.8 · THE_COURT_FEARS ---------------------
# וַיַּשְׁכֵּם אֲבִימֶלֶךְ בַּבֹּקֶר וַיִּקְרָא לְכָל־עֲבָדָיו וַיְדַבֵּר
# אֶת־כָּל־הַדְּבָרִים הָאֵלֶּה בְּאָזְנֵיהֶם וַיִּירְאוּ הָאֲנָשִׁים מְאֹד
# "And Abimelech rose early in the morning, and called all his servants, and
# told all these things in their ears; and the men were sore afraid."
m.step("Gen.20.8")
# ‹וַיַּשְׁכֵּם … וַיְדַבֵּר … וַיִּירְאוּ הָאֲנָשִׁים מְאֹד› event: report-
# fear — agent avimelekh
m.event("report_fear", agent="avimelekh")

# -------------------------- Gen.20.9 · THE_GREAT_SIN_REBUKE ----------------
# וַיִּקְרָא אֲבִימֶלֶךְ לְאַבְרָהָם וַיֹּאמֶר לוֹ מֶה־עָשִׂיתָ לָּנוּ
# וּמֶה־חָטָאתִי לָךְ כִּי־הֵבֵאתָ עָלַי וְעַל־מַמְלַכְתִּי חֲטָאָה גְדֹלָה
# מַעֲשִׂים אֲשֶׁר לֹא־יֵעָשׂוּ עָשִׂיתָ עִמָּדִי
# "Then Abimelech called Abraham, and said unto him: 'What hast thou done
# unto us? and wherein have I sinned against thee, that thou hast brought on
# me and on my kingdom a great sin? thou hast done deeds unto me that ought
# not to be done.'"
m.step("Gen.20.9")
# ‹מֶה־עָשִׂיתָ לָּנוּ … חֲטָאָה גְדֹלָה … מַעֲשִׂים אֲשֶׁר לֹא־יֵעָשׂוּ›
# fact holds: meh-asita-lanu-and-meh-chatati; chataah-gedolah-upon-mamlakhti
m.fact("meh_asita_lanu_u_meh_chatati",
       "chataah_gedolah_al_mamlakhti")

# -------------------------- Gen.20.10 · THE_SECOND_QUESTION ----------------
# וַיֹּאמֶר אֲבִימֶלֶךְ אֶל־אַבְרָהָם מָה רָאִיתָ כִּי עָשִׂיתָ אֶת־הַדָּבָר
# הַזֶּה
# "And Abimelech said unto Abraham: 'What sawest thou, that thou hast done
# this thing?'"
m.step("Gen.20.10")
# ‹מָה רָאִיתָ כִּי עָשִׂיתָ› fact holds: mah-raita-when-asita
m.fact("mah_raita_ki_asita")

# -------------------------- Gen.20.11 · THE_FEAR_OF_GOD_GUESS --------------
# וַיֹּאמֶר אַבְרָהָם כִּי אָמַרְתִּי רַק אֵין־יִרְאַת אֱלֹהִים בַּמָּקוֹם
# הַזֶּה וַהֲרָגוּנִי עַל־דְּבַר אִשְׁתִּי
# "And Abraham said: 'Because I thought: Surely the fear of God is not in
# this place; and they will slay me for my wife's sake."
m.step("Gen.20.11")
# ‹אֵין־יִרְאַת אֱלֹהִים בַּמָּקוֹם הַזֶּה וַהֲרָגוּנִי› fact holds: amarti-
# ein-yirat-God; and-haraguni-upon-devar-ishti
m.fact("amarti_ein_yirat_elohim",
       "va_haraguni_al_devar_ishti")

# -------------------------- Gen.20.12 · THE_HALF_TRUTH ---------------------
# וְגַם־אָמְנָה אֲחֹתִי בַת־אָבִי הִוא אַךְ לֹא בַת־אִמִּי וַתְּהִי־לִי
# לְאִשָּׁה
# "And moreover she is indeed my sister, the daughter of my father, but not
# the daughter of my mother; and so she became my wife."
m.step("Gen.20.12")
# ‹אֲחֹתִי בַת־אָבִי הִוא אַךְ לֹא בַת־אִמִּי› fact holds: achoti-vat-avi-
# akh-not-vat-imi
m.fact("achoti_vat_avi_akh_lo_vat_imi")

# -------------------------- Gen.20.13 · THE_WANDERING_AND_THE_QUOTED_DEMAND -
# וַיְהִי כַּאֲשֶׁר הִתְעוּ אֹתִי אֱלֹהִים מִבֵּית אָבִי וָאֹמַר לָהּ זֶה
# חַסְדֵּךְ אֲשֶׁר תַּעֲשִׂי עִמָּדִי אֶל כָּל־הַמָּקוֹם אֲשֶׁר נָבוֹא
# שָׁמָּה אִמְרִי־לִי אָחִי הוּא
# "And it came to pass, when God caused me to wander from my father's house,
# that I said unto her: This is thy kindness which thou shalt show unto me;
# at every place whither we shall come, say of me: He is my brother.'"
m.step("Gen.20.13")
# ‹הִתְעוּ אֹתִי אֱלֹהִים … אִמְרִי־לִי אָחִי הוּא› fact holds: hitu-me-God-
# from-beit-avi; imri-to-me-my-brother-that
m.fact("hitu_oti_elohim_mi_beit_avi",
       "imri_li_achi_hu")

# -------------------------- Gen.20.14 · THE_RETURN_CYCLE_CLOSES ------------
# וַיִּקַּח אֲבִימֶלֶךְ צֹאן וּבָקָר וַעֲבָדִים וּשְׁפָחֹת וַיִּתֵּן
# לְאַבְרָהָם וַיָּשֶׁב לוֹ אֵת שָׂרָה אִשְׁתּוֹ
# "And Abimelech took sheep and oxen, and men-servants and women-servants,
# and gave them unto Abraham, and restored him Sarah his wife."
m.step("Gen.20.14")
# ‹וַיָּשֶׁב לוֹ אֵת שָׂרָה אִשְׁתּוֹ› demand settled (popped from the
# queue): hashev(wife-of-the-man)
m.result("hashev(eshet_ha_ish)", tmark="t1")

# -------------------------- Gen.20.15 · THE_DWELL_GRANT --------------------
# וַיֹּאמֶר אֲבִימֶלֶךְ הִנֵּה אַרְצִי לְפָנֶיךָ בַּטּוֹב בְּעֵינֶיךָ שֵׁב
# "And Abimelech said: 'Behold, my land is before thee: dwell where it
# pleaseth thee.'"
m.step("Gen.20.15")
# ‹בַּטּוֹב בְּעֵינֶיךָ שֵׁב› avimelekh speaks a demand — LET: shev(in-the-
# good-in-einekha)
m.declare("avimelekh", "LET",
          "shev(ba_tov_be_einekha)")

# -------------------------- Gen.20.16 · THE_COVERING_AND_THE_VINDICATION ---
# וּלְשָׂרָה אָמַר הִנֵּה נָתַתִּי אֶלֶף כֶּסֶף לְאָחִיךְ הִנֵּה הוּא־לָךְ
# כְּסוּת עֵינַיִם לְכֹל אֲשֶׁר אִתָּךְ וְאֵת כֹּל וְנֹכָחַת
# "And unto Sarah he said: 'Behold, I have given thy brother a thousand
# pieces of silver; behold, it is for thee a covering of the eyes to all
# that are with thee; and before all men thou art righted.'"
m.step("Gen.20.16")
# ‹אֶלֶף כֶּסֶף … כְּסוּת עֵינַיִם … וְנֹכָחַת› fact holds: elef-kesef-
# kesut-einayim; and-nokhachat
m.fact("elef_kesef_kesut_einayim",
       "ve_nokhachat")

# -------------------------- Gen.20.17 · THE_PRAYER_AND_THE_HEALING ---------
# וַיִּתְפַּלֵּל אַבְרָהָם אֶל־הָאֱלֹהִים וַיִּרְפָּא אֱלֹהִים
# אֶת־אֲבִימֶלֶךְ וְאֶת־אִשְׁתּוֹ וְאַמְהֹתָיו וַיֵּלֵדוּ
# "And Abraham prayed unto God; and God healed Abimelech, and his wife, and
# his maid-servants; and they bore children."
m.step("Gen.20.17")
# ‹וַיִּתְפַּלֵּל אַבְרָהָם אֶל־הָאֱלֹהִים› event: pray — agent avraham
m.event("pray", agent="avraham")
# ‹וַיִּרְפָּא אֱלֹהִים … וַיֵּלֵדוּ› event: heal — agent God; theme beit-
# avimelekh
m.event("heal", agent="elohim", themes=["beit_avimelekh"])

# -------------------------- Gen.20.18 · THE_SHUT_WOMB_CLOSER ---------------
# כִּי־עָצֹר עָצַר יְהוָה בְּעַד כָּל־רֶחֶם לְבֵית אֲבִימֶלֶךְ עַל־דְּבַר
# שָׂרָה אֵשֶׁת אַבְרָהָם
# "For the LORD had fast closed up all the wombs of the house of Abimelech,
# because of Sarah Abraham's wife."
m.step("Gen.20.18")
# ‹כִּי־עָצֹר עָצַר יְהוָה בְּעַד כָּל־רֶחֶם› fact holds: atzor-atzar-the-
# LORD-bead-all-rechem
m.fact("atzor_atzar_YHWH_bead_kol_rechem")
# ‹כִּי־עָצֹר עָצַר יְהוָה› note: zero events in this verse
m.note_zero_events()

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'avimelekh'}
    assert m.presupposed_set() == {'shur', 'qadesh', 'gerar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shev(ba_tov_be_einekha)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['achoti_hi', 'hinkha_met_al_ha_ishah', 've_hi_beulat_baal', 'lo_qarav_eleha', 'ha_goy_gam_tzaddiq_taharog', 'hu_amar_li_ve_hi_gam_hi_amrah', 'be_tom_levavi_u_ve_niqyon_kapai', 'gam_anokhi_yadati_ve_tom_levavkha', 'va_echsokh_otkha_me_chato_li', 'lo_netatikha_lingoa', 've_yitpalel_baadkha_ve_cheyeh', 'im_einkha_meshiv_da_ki_mot_tamut', 'meh_asita_lanu_u_meh_chatati', 'chataah_gedolah_al_mamlakhti', 'mah_raita_ki_asita', 'amarti_ein_yirat_elohim', 'va_haraguni_al_devar_ishti', 'achoti_vat_avi_akh_lo_vat_imi', 'hitu_oti_elohim_mi_beit_avi', 'imri_li_achi_hu', 'elef_kesef_kesut_einayim', 've_nokhachat', 'atzor_atzar_YHWH_bead_kol_rechem'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_37_laughter_wilderness_oath
###############################################################################
# =============================================================================
# gen_37_laughter_wilderness_oath — 21:1-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_37_laughter_wilderness_oath.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The visitation, the expulsion, the well-oath (21:1-34)"""
from machine import Machine

m = Machine("gen_37_laughter_wilderness_oath")

# -------------------------- Gen.21.1 · THE_VISITATION_PAYS_TWICE -----------
# וַיהוָה פָּקַד אֶת־שָׂרָה כַּאֲשֶׁר אָמָר וַיַּעַשׂ יְהוָה לְשָׂרָה
# כַּאֲשֶׁר דִּבֵּר
# "And the LORD remembered Sarah as He had said, and the LORD did unto Sarah
# as He had spoken."
m.step("Gen.21.1")
# ‹פָּקַד … כַּאֲשֶׁר אָמָר … כַּאֲשֶׁר דִּבֵּר› fact holds: paqad-like-
# which-amar-and-yaas-like-which-diber
m.fact("paqad_ka_asher_amar_va_yaas_ka_asher_diber")

# -------------------------- Gen.21.2 · THE_BIRTH_AT_THE_APPOINTED_TIME -----
# וַתַּהַר וַתֵּלֶד שָׂרָה לְאַבְרָהָם בֵּן לִזְקֻנָיו לַמּוֹעֵד
# אֲשֶׁר־דִּבֶּר אֹתוֹ אֱלֹהִים
# "And Sarah conceived, and bore Abraham a son in his old age, at the set
# time of which God had spoken to him."
m.step("Gen.21.2")
# ‹וַתֵּלֶד שָׂרָה לְאַבְרָהָם בֵּן› the world gains: yitzchaq
m.install("yitzchaq")
# ‹בֵּן לִזְקֻנָיו לַמּוֹעֵד אֲשֶׁר־דִּבֶּר› fact holds: ben-to-me-zequnayv;
# to-moed-which-diber-God
m.fact("ben_li_zequnayv",
       "la_moed_asher_diber_elohim")

# -------------------------- Gen.21.3 · THE_DECREE_EXECUTED_IN_FORMULA ------
# וַיִּקְרָא אַבְרָהָם אֶת־שֶׁם־בְּנוֹ הַנּוֹלַד־לוֹ אֲשֶׁר־יָלְדָה־לּוֹ
# שָׂרָה יִצְחָק
# "And Abraham called the name of his son that was born unto him, whom Sarah
# bore to him, Isaac."
m.step("Gen.21.3")
# ‹וַיִּקְרָא אַבְרָהָם אֶת־שֶׁם־בְּנוֹ … יִצְחָק› named: yitzchaq :=
# Yitzchaq
m.name("yitzchaq", "Yitzchaq")

# -------------------------- Gen.21.4 · THE_LAWS_SECOND_CASE_EXECUTES -------
# וַיָּמָל אַבְרָהָם אֶת־יִצְחָק בְּנוֹ בֶּן־שְׁמֹנַת יָמִים כַּאֲשֶׁר
# צִוָּה אֹתוֹ אֱלֹהִים
# "And Abraham circumcised his son Isaac when he was eight days old, as God
# had commanded him."
m.step("Gen.21.4")
# ‹וַיָּמָל אַבְרָהָם אֶת־יִצְחָק … כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› event:
# circumcise — agent avraham; theme yitzchaq
m.event("circumcise", agent="avraham", themes=["yitzchaq"])
# ‹כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים› fact holds: like-which-tziva-it-God
m.fact("ka_asher_tziva_oto_elohim")

# -------------------------- Gen.21.5 · THE_HUNDRED_YEAR_FRAME --------------
# וְאַבְרָהָם בֶּן־מְאַת שָׁנָה בְּהִוָּלֶד לוֹ אֵת יִצְחָק בְּנוֹ
# "And Abraham was a hundred years old, when his son Isaac was born unto
# him."
m.step("Gen.21.5")
# ‹בֶּן־מְאַת שָׁנָה› fact holds: ben-meat-year
m.fact("ben_meat_shanah")

# -------------------------- Gen.21.6 · THE_LAUGHTER_MADE_AND_CONJUGATED ----
# וַתֹּאמֶר שָׂרָה צְחֹק עָשָׂה לִי אֱלֹהִים כָּל־הַשֹּׁמֵעַ יִצְחַק־לִי
# "And Sarah said: 'God hath made laughter for me; every one that heareth
# will laugh on account of me.'"
m.step("Gen.21.6")
# ‹צְחֹק עָשָׂה לִי אֱלֹהִים כָּל־הַשֹּׁמֵעַ יִצְחַק־לִי› fact holds:
# tzechoq-make-to-me-God-all-the-shomea-yitzchaq-to-me
m.fact("tzechoq_asah_li_elohim_kol_ha_shomea_yitzchaq_li")

# -------------------------- Gen.21.7 · THE_WHO_WOULD_HAVE_SAID -------------
# וַתֹּאמֶר מִי מִלֵּל לְאַבְרָהָם הֵינִיקָה בָנִים שָׂרָה כִּי־יָלַדְתִּי
# בֵן לִזְקֻנָיו
# "And she said: 'Who would have said unto Abraham, that Sarah should give
# children suck? for I have borne him a son in his old age.'"
m.step("Gen.21.7")
# ‹מִי מִלֵּל לְאַבְרָהָם› fact holds: from-milel-to-avraham-heniqah-vanim-
# sarah
m.fact("mi_milel_le_avraham_heniqah_vanim_sarah")

# -------------------------- Gen.21.8 · THE_WEANING_FEAST -------------------
# וַיִּגְדַּל הַיֶּלֶד וַיִּגָּמַל וַיַּעַשׂ אַבְרָהָם מִשְׁתֶּה גָדוֹל
# בְּיוֹם הִגָּמֵל אֶת־יִצְחָק
# "And the child grew, and was weaned. And Abraham made a great feast on the
# day that Isaac was weaned."
m.step("Gen.21.8")
# ‹וַיַּעַשׂ אַבְרָהָם מִשְׁתֶּה גָדוֹל› event: feast — agent avraham; theme
# yitzchaq
m.event("feast", agent="avraham", themes=["yitzchaq"])

# -------------------------- Gen.21.9 · THE_MOCKING_SEEN --------------------
# וַתֵּרֶא שָׂרָה אֶת־בֶּן־הָגָר הַמִּצְרִית אֲשֶׁר־יָלְדָה לְאַבְרָהָם
# מְצַחֵק
# "And Sarah saw the son of Hagar the Egyptian, whom she had borne unto
# Abraham, making sport."
m.step("Gen.21.9")
# ‹הָגָר הַמִּצְרִית› the world gains: hagar
m.install("hagar")
# ‹בֶּן־הָגָר› the world gains: the-naar
m.install("ha_naar")
# ‹וַתֵּרֶא שָׂרָה … מְצַחֵק› event: see — agent sarah; theme the-naar
m.event("see", agent="sarah", themes=["ha_naar"])

# -------------------------- Gen.21.10 · THE_EXPULSION_DEMAND ---------------
# וַתֹּאמֶר לְאַבְרָהָם גָּרֵשׁ הָאָמָה הַזֹּאת וְאֶת־בְּנָהּ כִּי לֹא
# יִירַשׁ בֶּן־הָאָמָה הַזֹּאת עִם־בְּנִי עִם־יִצְחָק
# "Wherefore she said unto Abraham: 'Cast out this bondwoman and her son;
# for the son of this bondwoman shall not be heir with my son, even with
# Isaac.'"
m.step("Gen.21.10")
# ‹גָּרֵשׁ הָאָמָה הַזֹּאת וְאֶת־בְּנָהּ› sarah speaks a demand — LET:
# garesh(the-cubit-and-benah)
m.declare("sarah", "LET",
          "garesh(ha_amah_ve_et_benah)")
# ‹כִּי לֹא יִירַשׁ בֶּן־הָאָמָה הַזֹּאת עִם־בְּנִי עִם־יִצְחָק› fact holds:
# not-yirash-ben-the-cubit-if-beni-if-yitzchaq
m.fact("lo_yirash_ben_ha_amah_im_beni_im_yitzchaq")

# -------------------------- Gen.21.11 · THE_EVIL_IN_THE_FATHERS_EYES -------
# וַיֵּרַע הַדָּבָר מְאֹד בְּעֵינֵי אַבְרָהָם עַל אוֹדֹת בְּנוֹ
# "And the thing was very grievous in Abraham's sight on account of his
# son."
m.step("Gen.21.11")
# ‹וַיֵּרַע הַדָּבָר מְאֹד בְּעֵינֵי אַבְרָהָם› fact holds: and-yera-the-
# davar-very-in-eyes-of-avraham
m.fact("va_yera_ha_davar_meod_be_einei_avraham")

# -------------------------- Gen.21.12 · THE_ARBITRATION_IN_THREE_MOODS -----
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם אַל־יֵרַע בְּעֵינֶיךָ עַל־הַנַּעַר
# וְעַל־אֲמָתֶךָ כֹּל אֲשֶׁר תֹּאמַר אֵלֶיךָ שָׂרָה שְׁמַע בְּקֹלָהּ כִּי
# בְיִצְחָק יִקָּרֵא לְךָ זָרַע
# "And God said unto Abraham: 'Let it not be grievous in thy sight because
# of the lad, and because of thy bondwoman; in all that Sarah saith unto
# thee, hearken unto her voice; for in Isaac shall seed be called to thee."
m.step("Gen.21.12")
# ‹אַל־יֵרַע בְּעֵינֶיךָ› God speaks a demand — LET-NOT: yera(in-einekha)
m.declare("elohim", "LET-NOT",
          "yera(be_einekha)")
# ‹כֹּל אֲשֶׁר תֹּאמַר אֵלֶיךָ שָׂרָה שְׁמַע בְּקֹלָהּ› God speaks a demand
# — LET: hear(in-voice-sarah)
m.declare("elohim", "LET",
          "shema(be_qol_sarah)")
# ‹כִּי בְיִצְחָק יִקָּרֵא לְךָ זָרַע› fact holds: when-and-yitzchaq-yiqare-
# to-you-zara
m.fact("ki_ve_yitzchaq_yiqare_lekha_zara")

# -------------------------- Gen.21.13 · THE_OTHER_NATION_PROMISE -----------
# וְגַם אֶת־בֶּן־הָאָמָה לְגוֹי אֲשִׂימֶנּוּ כִּי זַרְעֲךָ הוּא
# "And also of the son of the bondwoman will I make a nation, because he is
# thy seed.'"
m.step("Gen.21.13")
# ‹לְגוֹי אֲשִׂימֶנּוּ כִּי זַרְעֲךָ הוּא› fact holds: to-goy-asimenu-when-
# zarakha-that
m.fact("le_goy_asimenu_ki_zarakha_hu")

# -------------------------- Gen.21.14 · THE_DAWN_COMPLIANCE_IN_OTHER_VERBS -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיִּקַּח־לֶחֶם וְחֵמַת מַיִם וַיִּתֵּן
# אֶל־הָגָר שָׂם עַל־שִׁכְמָהּ וְאֶת־הַיֶּלֶד וַיְשַׁלְּחֶהָ וַתֵּלֶךְ
# וַתֵּתַע בְּמִדְבַּר בְּאֵר שָׁבַע
# "And Abraham arose up early in the morning, and took bread and a bottle of
# water, and gave it unto Hagar, putting it on her shoulder, and the child,
# and sent her away; and she departed, and strayed in the wilderness of
# Beer-sheba."
m.step("Gen.21.14")
# ‹וַיַּשְׁכֵּם … וַיִּקַּח … וַיִּתֵּן … וַיְשַׁלְּחֶהָ› event: send-away —
# agent avraham; theme hagar
m.event("send_away", agent="avraham", themes=["hagar"])
# ‹וַיְשַׁלְּחֶהָ … וַתֵּתַע› fact holds: and-yashkem-and-yeshalcheha-and-
# teta
m.fact("va_yashkem_va_yeshalcheha_va_teta")
# ‹בְּמִדְבַּר בְּאֵר שָׁבַע› reads without prior install (flag, not fix):
# beer-seven
m.presupposed("beer_sheva")

# -------------------------- Gen.21.15 · THE_SPENT_SKIN_AND_THE_CAST_CHILD --
# וַיִּכְלוּ הַמַּיִם מִן־הַחֵמֶת וַתַּשְׁלֵךְ אֶת־הַיֶּלֶד תַּחַת אַחַד
# הַשִּׂיחִם
# "And the water in the bottle was spent, and she cast the child under one
# of the shrubs."
m.step("Gen.21.15")
# ‹וַתַּשְׁלֵךְ אֶת־הַיֶּלֶד› event: cast — agent hagar; theme the-naar
m.event("cast", agent="hagar", themes=["ha_naar"])

# -------------------------- Gen.21.16 · THE_BOWSHOT_AND_THE_WEEPING --------
# וַתֵּלֶךְ וַתֵּשֶׁב לָהּ מִנֶּגֶד הַרְחֵק כִּמְטַחֲוֵי קֶשֶׁת כִּי אָמְרָה
# אַל־אֶרְאֶה בְּמוֹת הַיָּלֶד וַתֵּשֶׁב מִנֶּגֶד וַתִּשָּׂא אֶת־קֹלָהּ
# וַתֵּבְךְּ
# "And she went, and sat her down over against him a good way off, as it
# were a bow-shot; for she said: 'Let me not look upon the death of the
# child.' And she sat over against him, and lifted up her voice, and wept."
m.step("Gen.21.16")
# ‹אַל־אֶרְאֶה בְּמוֹת הַיָּלֶד› fact holds: upon-ereh-in-dying-the-yaled
m.fact("al_ereh_be_mot_ha_yaled")
# ‹וַתִּשָּׂא אֶת־קֹלָהּ וַתֵּבְךְּ› event: weep — agent hagar
m.event("weep", agent="hagar")

# -------------------------- Gen.21.17 · THE_SKY_CALL_AND_THE_HEARD_NAME ----
# וַיִּשְׁמַע אֱלֹהִים אֶת־קוֹל הַנַּעַר וַיִּקְרָא מַלְאַךְ אֱלֹהִים
# אֶל־הָגָר מִן־הַשָּׁמַיִם וַיֹּאמֶר לָהּ מַה־לָּךְ הָגָר אַל־תִּירְאִי
# כִּי־שָׁמַע אֱלֹהִים אֶל־קוֹל הַנַּעַר בַּאֲשֶׁר הוּא־שָׁם
# "And God heard the voice of the lad; and the angel of God called to Hagar
# out of heaven, and said unto her: 'What aileth thee, Hagar? fear not; for
# God hath heard the voice of the lad where he is."
m.step("Gen.21.17")
# ‹מַלְאַךְ אֱלֹהִים … מִן־הַשָּׁמַיִם› the world gains: malakh-God
m.install("malakh_elohim")
# ‹אַל־תִּירְאִי› malakh-God speaks a demand — LET-NOT: tiri(hagar)
m.declare("malakh_elohim", "LET-NOT",
          "tiri(hagar)")
# ‹כִּי־שָׁמַע אֱלֹהִים אֶל־קוֹל הַנַּעַר בַּאֲשֶׁר הוּא־שָׁם› fact holds:
# shama-God-to-voice-the-naar-in-the-which-that-there
m.fact("shama_elohim_el_qol_ha_naar_ba_asher_hu_sham")

# -------------------------- Gen.21.18 · THE_COMPOUND_TRIPLE_THIRD_TOKEN ----
# קוּמִי שְׂאִי אֶת־הַנַּעַר וְהַחֲזִיקִי אֶת־יָדֵךְ בּוֹ כִּי־לְגוֹי
# גָּדוֹל אֲשִׂימֶנּוּ
# "Arise, lift up the lad, and hold him fast by thy hand; for I will make
# him a great nation.'"
m.step("Gen.21.18")
# ‹קוּמִי שְׂאִי אֶת־הַנַּעַר וְהַחֲזִיקִי אֶת־יָדֵךְ בּוֹ› malakh-God
# speaks a demand — LET: qumi-sei-and-hachaziqi(the-naar)
m.declare("malakh_elohim", "LET",
          "qumi_sei_ve_hachaziqi(et_ha_naar)")
# ‹כִּי־לְגוֹי גָּדוֹל אֲשִׂימֶנּוּ› fact holds: when-to-goy-gadol-asimenu
m.fact("ki_le_goy_gadol_asimenu")

# -------------------------- Gen.21.19 · THE_EYES_OPENED_AT_THE_WELL --------
# וַיִּפְקַח אֱלֹהִים אֶת־עֵינֶיהָ וַתֵּרֶא בְּאֵר מָיִם וַתֵּלֶךְ
# וַתְּמַלֵּא אֶת־הַחֵמֶת מַיִם וַתַּשְׁקְ אֶת־הַנָּעַר
# "And God opened her eyes, and she saw a well of water; and she went, and
# filled the bottle with water, and gave the lad drink."
m.step("Gen.21.19")
# ‹וַיִּפְקַח אֱלֹהִים אֶת־עֵינֶיהָ› event: open-eyes — agent God
m.event("open_eyes", agent="elohim")
# ‹וַתְּמַלֵּא אֶת־הַחֵמֶת מַיִם וַתַּשְׁקְ אֶת־הַנָּעַר› event: water —
# agent hagar
m.event("water", agent="hagar")

# -------------------------- Gen.21.20 · GOD_WITH_THE_LAD -------------------
# וַיְהִי אֱלֹהִים אֶת־הַנַּעַר וַיִּגְדָּל וַיֵּשֶׁב בַּמִּדְבָּר וַיְהִי
# רֹבֶה קַשָּׁת
# "And God was with the lad, and he grew; and he dwelt in the wilderness,
# and became an archer."
m.step("Gen.21.20")
# ‹וַיְהִי אֱלֹהִים אֶת־הַנַּעַר וַיִּגְדָּל› fact holds: God-the-naar-and-
# yigdal
m.fact("elohim_et_ha_naar_va_yigdal")

# -------------------------- Gen.21.21 · PARAN_AND_THE_EGYPTIAN_WIFE --------
# וַיֵּשֶׁב בְּמִדְבַּר פָּארָן וַתִּקַּח־לוֹ אִמּוֹ אִשָּׁה מֵאֶרֶץ
# מִצְרָיִם
# "And he dwelt in the wilderness of Paran; and his mother took him a wife
# out of the land of Egypt."
m.step("Gen.21.21")
# ‹וַתִּקַּח־לוֹ אִמּוֹ אִשָּׁה› event: take-wife — agent hagar
m.event("take_wife", agent="hagar")
# ‹בְּמִדְבַּר פָּארָן … מֵאֶרֶץ מִצְרָיִם› reads without prior install
# (flag, not fix): paran, mitzrayim
m.presupposed("paran", "mitzrayim")

# -------------------------- Gen.21.22-24 · THE_PACT_OPENING_DEMAND_AND_COMMITMENT -
# וַיְהִי בָּעֵת הַהִוא וַיֹּאמֶר אֲבִימֶלֶךְ וּפִיכֹל שַׂר־צְבָאוֹ
# אֶל־אַבְרָהָם לֵאמֹר אֱלֹהִים עִמְּךָ בְּכֹל אֲשֶׁר־אַתָּה עֹשֶׂה …
# וְעַתָּה הִשָּׁבְעָה לִּי בֵאלֹהִים הֵנָּה … וַיֹּאמֶר אַבְרָהָם אָנֹכִי
# אִשָּׁבֵעַ
# "And it came to pass at that time, that Abimelech and Phicol the captain
# of his host spoke unto Abraham, saying: 'God is with thee in all that thou
# doest. Now therefore swear unto me here by God that thou wilt not deal
# falsely with me, nor with my son, nor with my son's son; but according to
# the kindness that I have done unto thee, thou shalt do unto me, and to the
# land wherein thou hast sojourned.' And Abraham said: 'I will swear.'"
m.step("Gen.21.22-24")
# ‹אֲבִימֶלֶךְ› the world gains: avimelekh
m.install("avimelekh")
# ‹וּפִיכֹל שַׂר־צְבָאוֹ› the world gains: fikhol
m.install("fikhol")
# ‹אֱלֹהִים עִמְּךָ בְּכֹל אֲשֶׁר־אַתָּה עֹשֶׂה … כַּחֶסֶד אֲשֶׁר־עָשִׂיתִי
# עִמְּךָ› fact holds: God-imkha-in-all-which-you-oseh; like-chesed-which-
# asiti-imkha
m.fact("elohim_imkha_be_khol_asher_atah_oseh",
       "ka_chesed_asher_asiti_imkha")
# ‹וְעַתָּה הִשָּׁבְעָה לִּי בֵאלֹהִים הֵנָּה› avimelekh speaks a demand —
# LET: hishava(to-me-and-God)
m.declare("avimelekh", "LET",
          "hishava(li_ve_elohim)")
# ‹אָנֹכִי אִשָּׁבֵעַ› fact holds: anokhi-ishavea
m.fact("anokhi_ishavea")

# -------------------------- Gen.21.25 · THE_REPROOF_OVER_THE_STOLEN_WELL ---
# וְהוֹכִחַ אַבְרָהָם אֶת־אֲבִימֶלֶךְ עַל־אֹדוֹת בְּאֵר הַמַּיִם אֲשֶׁר
# גָּזְלוּ עַבְדֵי אֲבִימֶלֶךְ
# "And Abraham reproved Abimelech because of the well of water, which
# Abimelech's servants had violently taken away."
m.step("Gen.21.25")
# ‹וְהוֹכִחַ אַבְרָהָם אֶת־אֲבִימֶלֶךְ› event: reprove — agent avraham;
# theme avimelekh
m.event("reprove", agent="avraham", themes=["avimelekh"])

# -------------------------- Gen.21.26 · THE_TRIPLE_DENIAL ------------------
# וַיֹּאמֶר אֲבִימֶלֶךְ לֹא יָדַעְתִּי מִי עָשָׂה אֶת־הַדָּבָר הַזֶּה
# וְגַם־אַתָּה לֹא־הִגַּדְתָּ לִּי וְגַם אָנֹכִי לֹא שָׁמַעְתִּי בִּלְתִּי
# הַיּוֹם
# "And Abimelech said: 'I know not who hath done this thing; neither didst
# thou tell me, neither yet heard I of it, but to-day.'"
m.step("Gen.21.26")
# ‹לֹא יָדַעְתִּי … לֹא־הִגַּדְתָּ … לֹא שָׁמַעְתִּי› fact holds: not-
# yadati-not-higadta-not-shamati-bilti-the-day
m.fact("lo_yadati_lo_higadta_lo_shamati_bilti_ha_yom")

# -------------------------- Gen.21.27 · THE_FIRST_HUMAN_HUMAN_CUT ----------
# וַיִּקַּח אַבְרָהָם צֹאן וּבָקָר וַיִּתֵּן לַאֲבִימֶלֶךְ וַיִּכְרְתוּ
# שְׁנֵיהֶם בְּרִית
# "And Abraham took sheep and oxen, and gave them unto Abimelech; and they
# two made a covenant."
m.step("Gen.21.27")
# ‹וַיִּכְרְתוּ שְׁנֵיהֶם בְּרִית› event: cut-covenant — agent avraham
m.event("cut_covenant", agent="avraham")

# -------------------------- Gen.21.28-31 · THE_SEVEN_EWES_AND_THE_NAMING_REPORT -
# וַיַּצֵּב אַבְרָהָם אֶת־שֶׁבַע כִּבְשֹׂת הַצֹּאן לְבַדְּהֶן … מָה הֵנָּה
# שֶׁבַע כְּבָשֹׂת … כִּי אֶת־שֶׁבַע כְּבָשֹׂת תִּקַּח מִיָּדִי בַּעֲבוּר
# תִּהְיֶה־לִּי לְעֵדָה כִּי חָפַרְתִּי אֶת־הַבְּאֵר הַזֹּאת עַל־כֵּן קָרָא
# לַמָּקוֹם הַהוּא בְּאֵר שָׁבַע כִּי שָׁם נִשְׁבְּעוּ שְׁנֵיהֶם
# "And Abraham set seven ewe-lambs of the flock by themselves. And Abimelech
# said unto Abraham: 'What mean these seven ewe-lambs which thou hast set by
# themselves?' And he said: 'Verily, these seven ewe-lambs shalt thou take
# of my hand, that it may be a witness unto me, that I have digged this
# well.' Wherefore that place was called Beer-sheba; because there they
# swore both of them."
m.step("Gen.21.28-31")
# ‹וַיַּצֵּב אַבְרָהָם אֶת־שֶׁבַע כִּבְשֹׂת הַצֹּאן לְבַדְּהֶן› event:
# station — agent avraham; theme seven-kivsot
m.event("station", agent="avraham", themes=["sheva_kivsot"])
# ‹תִּקַּח מִיָּדִי בַּעֲבוּר תִּהְיֶה־לִּי לְעֵדָה כִּי חָפַרְתִּי
# אֶת־הַבְּאֵר› fact holds: seven-khevasot-tiqach-from-yadi-to-edah; when-
# chafarti-the-beer
m.fact("sheva_khevasot_tiqach_mi_yadi_le_edah",
       "ki_chafarti_et_ha_beer")
# ‹כִּי שָׁם נִשְׁבְּעוּ שְׁנֵיהֶם› demand settled (popped from the queue):
# hishava(to-me-and-God)
m.result("hishava(li_ve_elohim)", tmark="t1")
# ‹עַל־כֵּן קָרָא לַמָּקוֹם הַהוּא בְּאֵר שָׁבַע› pattern recorded: upon-
# ken-qara-to-maqom-beer-shava
m.pattern("al_ken_qara_la_maqom_beer_shava")

# -------------------------- Gen.21.32 · THE_SECOND_CUT_AND_THE_RETURN ------
# וַיִּכְרְתוּ בְרִית בִּבְאֵר שָׁבַע וַיָּקָם אֲבִימֶלֶךְ וּפִיכֹל
# שַׂר־צְבָאוֹ וַיָּשֻׁבוּ אֶל־אֶרֶץ פְּלִשְׁתִּים
# "So they made a covenant at Beer-sheba; and Abimelech rose up, and Phicol
# the captain of his host, and they returned into the land of the
# Philistines."
m.step("Gen.21.32")
# ‹וַיִּכְרְתוּ בְרִית בִּבְאֵר שָׁבַע› event: cut-covenant — agent
# avimelekh
m.event("cut_covenant", agent="avimelekh")
# ‹אֶל־אֶרֶץ פְּלִשְׁתִּים› reads without prior install (flag, not fix):
# earth-pelishtim
m.presupposed("eretz_pelishtim")

# -------------------------- Gen.21.33 · THE_TAMARISK_AND_THE_EVERLASTING_NAME -
# וַיִּטַּע אֶשֶׁל בִּבְאֵר שָׁבַע וַיִּקְרָא־שָׁם בְּשֵׁם יְהוָה אֵל עוֹלָם
# "And Abraham planted a tamarisk-tree in Beer-sheba, and called there on
# the name of the LORD, the Everlasting God."
m.step("Gen.21.33")
# ‹וַיִּטַּע אֶשֶׁל … וַיִּקְרָא־שָׁם בְּשֵׁם יְהוָה› event: plant-and-call
# — agent avraham
m.event("plant_and_call", agent="avraham")
# ‹אֵל עוֹלָם› fact holds: and-yiqra-in-shem-the-LORD-to-olam
m.fact("va_yiqra_be_shem_YHWH_el_olam")

# -------------------------- Gen.21.34 · THE_LONG_SOJOURN_CODA --------------
# וַיָּגָר אַבְרָהָם בְּאֶרֶץ פְּלִשְׁתִּים יָמִים רַבִּים
# "And Abraham sojourned in the land of the Philistines many days."
m.step("Gen.21.34")
# ‹וַיָּגָר אַבְרָהָם בְּאֶרֶץ פְּלִשְׁתִּים יָמִים רַבִּים› fact holds:
# and-yagar-in-earth-pelishtim-seas-rabim
m.fact("va_yagar_be_eretz_pelishtim_yamim_rabim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'malakh_elohim', 'yitzchaq', 'hagar', 'avimelekh', 'ha_naar', 'fikhol'}
    assert m.presupposed_set() == {'paran', 'mitzrayim', 'eretz_pelishtim', 'beer_sheva'}
    assert m.REGISTRY["names"] == {'yitzchaq': 'Yitzchaq'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['garesh(ha_amah_ve_et_benah)', 'yera(be_einekha)', 'shema(be_qol_sarah)', 'tiri(hagar)', 'qumi_sei_ve_hachaziqi(et_ha_naar)']
    assert len(m.SPECS["log"]) == 6
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['paqad_ka_asher_amar_va_yaas_ka_asher_diber', 'ben_li_zequnayv', 'la_moed_asher_diber_elohim', 'ka_asher_tziva_oto_elohim', 'ben_meat_shanah', 'tzechoq_asah_li_elohim_kol_ha_shomea_yitzchaq_li', 'mi_milel_le_avraham_heniqah_vanim_sarah', 'lo_yirash_ben_ha_amah_im_beni_im_yitzchaq', 'va_yera_ha_davar_meod_be_einei_avraham', 'ki_ve_yitzchaq_yiqare_lekha_zara', 'le_goy_asimenu_ki_zarakha_hu', 'va_yashkem_va_yeshalcheha_va_teta', 'al_ereh_be_mot_ha_yaled', 'shama_elohim_el_qol_ha_naar_ba_asher_hu_sham', 'ki_le_goy_gadol_asimenu', 'elohim_et_ha_naar_va_yigdal', 'elohim_imkha_be_khol_asher_atah_oseh', 'ka_chesed_asher_asiti_imkha', 'anokhi_ishavea', 'lo_yadati_lo_higadta_lo_shamati_bilti_ha_yom', 'sheva_khevasot_tiqach_mi_yadi_le_edah', 'ki_chafarti_et_ha_beer', 'pattern: al_ken_qara_la_maqom_beer_shava', 'va_yiqra_be_shem_YHWH_el_olam', 'va_yagar_be_eretz_pelishtim_yamim_rabim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_38_moriah_binding_oath
###############################################################################
# =============================================================================
# gen_38_moriah_binding_oath — 22:1-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_38_moriah_binding_oath.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The test, the binding, the oath (22:1-24)"""
from machine import Machine

m = Machine("gen_38_moriah_binding_oath")

# -------------------------- Gen.22.1 · THE_FRAME_AND_THE_TEST --------------
# וַיְהִי אַחַר הַדְּבָרִים הָאֵלֶּה וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם
# וַיֹּאמֶר אֵלָיו אַבְרָהָם וַיֹּאמֶר הִנֵּנִי
# "And it came to pass after these things, that God did prove Abraham, and
# said unto him: 'Abraham'; and he said: 'Here am I.'"
m.step("Gen.22.1")
# ‹וְהָאֱלֹהִים נִסָּה אֶת־אַבְרָהָם … הִנֵּנִי› fact holds: achar-the-
# devarim-and-the-God-nisah-avraham; and-yomer-behold-I
m.fact("achar_ha_devarim_ve_ha_elohim_nisah_et_avraham",
       "va_yomer_hineni")

# -------------------------- Gen.22.2 · THE_CROWN_COMMAND -------------------
# וַיֹּאמֶר קַח־נָא אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק
# וְלֶךְ־לְךָ אֶל־אֶרֶץ הַמֹּרִיָּה וְהַעֲלֵהוּ שָׁם לְעֹלָה עַל אַחַד
# הֶהָרִים אֲשֶׁר אֹמַר אֵלֶיךָ
# "And He said: 'Take now thy son, thine only son, whom thou lovest, even
# Isaac, and get thee into the land of Moriah; and offer him there for a
# burnt-offering upon one of the mountains which I will tell thee of.'"
m.step("Gen.22.2")
# ‹קַח־נָא … וְלֶךְ־לְךָ … וְהַעֲלֵהוּ שָׁם לְעֹלָה› God speaks a demand —
# LET: qach-lekh-and-haalehu(binkha, to-burnt-offering)
m.declare("elohim", "LET",
          "qach_lekh_ve_haalehu(et_binkha, le_olah)")
# ‹אֶת־בִּנְךָ אֶת־יְחִידְךָ אֲשֶׁר־אָהַבְתָּ אֶת־יִצְחָק› fact holds:
# binkha-yechidkha-which-ahavta-yitzchaq; to-earth-the-moriyah-which-omar-
# to-you
m.fact("et_binkha_et_yechidkha_asher_ahavta_et_yitzchaq",
       "el_eretz_ha_moriyah_asher_omar_elekha")

# -------------------------- Gen.22.3 · THE_DAWN_OBEDIENCE_TWO_ROOTS_RETURN -
# וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת־חֲמֹרוֹ וַיִּקַּח
# אֶת־שְׁנֵי נְעָרָיו אִתּוֹ וְאֵת יִצְחָק בְּנוֹ וַיְבַקַּע עֲצֵי עֹלָה
# וַיָּקָם וַיֵּלֶךְ אֶל־הַמָּקוֹם אֲשֶׁר־אָמַר־לוֹ הָאֱלֹהִים
# "And Abraham rose early in the morning, and saddled his ass, and took two
# of his young men with him, and Isaac his son; and he cleaved the wood for
# the burnt-offering, and rose up, and went unto the place of which God had
# told him."
m.step("Gen.22.3")
# ‹וְאֵת יִצְחָק בְּנוֹ› the world gains: yitzchaq
m.install("yitzchaq")
# ‹אֶת־שְׁנֵי נְעָרָיו› the world gains: shnei-nearav
m.install("shnei_nearav")
# ‹וַיַּשְׁכֵּם … וַיַּחֲבֹשׁ … וַיִּקַּח … וַיְבַקַּע … וַיָּקָם וַיֵּלֶךְ›
# event: dawn-journey — agent avraham
m.event("dawn_journey", agent="avraham")
# ‹וַיַּשְׁכֵּם אַבְרָהָם בַּבֹּקֶר וַיַּחֲבֹשׁ אֶת־חֲמֹרוֹ› fact holds:
# and-yashkem-in-the-morning-and-yachavosh-chamoro
m.fact("va_yashkem_ba_boqer_va_yachavosh_et_chamoro")

# -------------------------- Gen.22.4 · THE_THIRD_DAY_SIGHTING --------------
# בַּיּוֹם הַשְּׁלִישִׁי וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו וַיַּרְא
# אֶת־הַמָּקוֹם מֵרָחֹק
# "On the third day Abraham lifted up his eyes, and saw the place afar off."
m.step("Gen.22.4")
# ‹בַּיּוֹם הַשְּׁלִישִׁי … מֵרָחֹק› fact holds: in-the-day-the-shelishi-
# and-yar-the-maqom-from-rachoq
m.fact("ba_yom_ha_shelishi_va_yar_et_ha_maqom_me_rachoq")

# -------------------------- Gen.22.5 · THE_STAY_DEMAND_AND_THE_EXCLUSIVE_WE -
# וַיֹּאמֶר אַבְרָהָם אֶל־נְעָרָיו שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר וַאֲנִי
# וְהַנַּעַר נֵלְכָה עַד־כֹּה וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם
# "And Abraham said unto his young men: 'Abide ye here with the ass, and I
# and the lad will go yonder; and we will worship, and come back to you.'"
m.step("Gen.22.5")
# ‹שְׁבוּ־לָכֶם פֹּה עִם־הַחֲמוֹר› avraham speaks a demand — LET: shevu(po-
# if-the-chamor)
m.declare("avraham", "LET",
          "shevu(po_im_ha_chamor)")
# ‹נֵלְכָה … וְנִשְׁתַּחֲוֶה וְנָשׁוּבָה אֲלֵיכֶם› fact holds: nelkha-and-
# nishtachaveh-and-nashuvah-aleikhem
m.fact("nelkha_ve_nishtachaveh_ve_nashuvah_aleikhem")

# -------------------------- Gen.22.6 · THE_LOADED_WALK_TOGETHER ------------
# וַיִּקַּח אַבְרָהָם אֶת־עֲצֵי הָעֹלָה וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ
# וַיִּקַּח בְּיָדוֹ אֶת־הָאֵשׁ וְאֶת־הַמַּאֲכֶלֶת וַיֵּלְכוּ שְׁנֵיהֶם
# יַחְדָּו
# "And Abraham took the wood of the burnt-offering, and laid it upon Isaac
# his son; and he took in his hand the fire and the knife; and they went
# both of them together."
m.step("Gen.22.6")
# ‹וַיָּשֶׂם עַל־יִצְחָק בְּנוֹ … וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו› event:
# load-and-walk — agent avraham
m.event("load_and_walk", agent="avraham")

# -------------------------- Gen.22.7 · THE_WHERE_IS_THE_LAMB ---------------
# וַיֹּאמֶר יִצְחָק אֶל־אַבְרָהָם אָבִיו וַיֹּאמֶר אָבִי וַיֹּאמֶר הִנֶּנִּי
# בְנִי וַיֹּאמֶר הִנֵּה הָאֵשׁ וְהָעֵצִים וְאַיֵּה הַשֶּׂה לְעֹלָה
# "And Isaac spoke unto Abraham his father, and said: 'My father.' And he
# said: 'Here am I, my son.' And he said: 'Behold the fire and the wood; but
# where is the lamb for a burnt-offering?'"
m.step("Gen.22.7")
# ‹אָבִי … הִנֶּנִּי בְנִי … וְאַיֵּה הַשֶּׂה לְעֹלָה› fact holds: avi-and-
# yomer-behold-I-veni; and-ayeh-the-seh-to-burnt-offering
m.fact("avi_va_yomer_hineni_veni",
       "ve_ayeh_ha_seh_le_olah")

# -------------------------- Gen.22.8 · THE_PROVIDE_ANSWER ------------------
# וַיֹּאמֶר אַבְרָהָם אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי
# וַיֵּלְכוּ שְׁנֵיהֶם יַחְדָּו
# "And Abraham said: 'God will provide Himself the lamb for a burnt-
# offering, my son.' So they went both of them together."
m.step("Gen.22.8")
# ‹אֱלֹהִים יִרְאֶה־לּוֹ הַשֶּׂה לְעֹלָה בְּנִי› fact holds: God-yireh-not-
# the-seh-to-burnt-offering-beni
m.fact("elohim_yireh_lo_ha_seh_le_olah_beni")

# -------------------------- Gen.22.9 · THE_BINDING -------------------------
# וַיָּבֹאוּ אֶל־הַמָּקוֹם אֲשֶׁר אָמַר־לוֹ הָאֱלֹהִים וַיִּבֶן שָׁם
# אַבְרָהָם אֶת־הַמִּזְבֵּחַ וַיַּעֲרֹךְ אֶת־הָעֵצִים וַיַּעֲקֹד אֶת־יִצְחָק
# בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ מִמַּעַל לָעֵצִים
# "And they came to the place which God had told him of; and Abraham built
# the altar there, and laid the wood in order, and bound Isaac his son, and
# laid him on the altar, upon the wood."
m.step("Gen.22.9")
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› event:
# bind — agent avraham; theme yitzchaq
m.event("bind", agent="avraham", themes=["yitzchaq"])
# ‹וַיַּעֲקֹד אֶת־יִצְחָק בְּנוֹ וַיָּשֶׂם אֹתוֹ עַל־הַמִּזְבֵּחַ› fact
# holds: and-yaaqod-yitzchaq-and-yasem-upon-the-altar
m.fact("va_yaaqod_et_yitzchaq_va_yasem_al_ha_mizbeach")

# -------------------------- Gen.22.10 · THE_HAND_AND_THE_KNIFE -------------
# וַיִּשְׁלַח אַבְרָהָם אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט
# אֶת־בְּנוֹ
# "And Abraham stretched forth his hand, and took the knife to slay his
# son."
m.step("Gen.22.10")
# ‹וַיִּשְׁלַח … אֶת־יָדוֹ וַיִּקַּח אֶת־הַמַּאֲכֶלֶת לִשְׁחֹט› event:
# reach-knife — agent avraham
m.event("reach_knife", agent="avraham")

# -------------------------- Gen.22.11 · THE_FIRST_DOUBLED_NAME_CALL --------
# וַיִּקְרָא אֵלָיו מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם וַיֹּאמֶר אַבְרָהָם
# אַבְרָהָם וַיֹּאמֶר הִנֵּנִי
# "And the angel of the LORD called unto him out of heaven, and said:
# 'Abraham, Abraham.' And he said: 'Here am I.'"
m.step("Gen.22.11")
# ‹מַלְאַךְ יְהוָה מִן־הַשָּׁמַיִם› the world gains: malakh-the-LORD
m.install("malakh_YHWH")
# ‹אַבְרָהָם אַבְרָהָם … הִנֵּנִי› fact holds: avraham-avraham-and-yomer-
# behold-I
m.fact("avraham_avraham_va_yomer_hineni")

# -------------------------- Gen.22.12 · THE_COUNTERMAND_AND_THE_CONFERRED_TITLE -
# וַיֹּאמֶר אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר וְאַל־תַּעַשׂ לוֹ מְאוּמָה
# כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ
# אֶת־בִּנְךָ אֶת־יְחִידְךָ מִמֶּנִּי
# "And he said: 'Lay not thy hand upon the lad, neither do thou any thing
# unto him; for now I know that thou art a God-fearing man, seeing thou hast
# not withheld thy son, thine only son, from Me.'"
m.step("Gen.22.12")
# ‹אַל־תִּשְׁלַח יָדְךָ אֶל־הַנַּעַר› malakh-the-LORD speaks a demand — LET-
# NOT: tishlach(yadkha-to-the-naar)
m.declare("malakh_YHWH", "LET-NOT",
          "tishlach(yadkha_el_ha_naar)")
# ‹וְאַל־תַּעַשׂ לוֹ מְאוּמָה› malakh-the-LORD speaks a demand — LET-NOT:
# taas(not-meumah)
m.declare("malakh_YHWH", "LET-NOT",
          "taas(lo_meumah)")
# ‹כִּי עַתָּה יָדַעְתִּי כִּי־יְרֵא אֱלֹהִים אַתָּה וְלֹא חָשַׂכְתָּ› fact
# holds: you-yadati-when-yere-God-you; and-not-chasakhta-binkha-yechidkha
m.fact("atah_yadati_ki_yere_elohim_atah",
       "ve_lo_chasakhta_et_binkha_et_yechidkha")

# -------------------------- Gen.22.13 · THE_RAM_AND_THE_CROWN_FORK ---------
# וַיִּשָּׂא אַבְרָהָם אֶת־עֵינָיו וַיַּרְא וְהִנֵּה־אַיִל אַחַר נֶאֱחַז
# בַּסְּבַךְ בְּקַרְנָיו וַיֵּלֶךְ אַבְרָהָם וַיִּקַּח אֶת־הָאַיִל
# וַיַּעֲלֵהוּ לְעֹלָה תַּחַת בְּנוֹ
# "And Abraham lifted up his eyes, and looked, and behold behind him a ram
# caught in the thicket by his horns. And Abraham went and took the ram, and
# offered him up for a burnt-offering in the stead of his son."
m.step("Gen.22.13")
# ‹וְהִנֵּה־אַיִל אַחַר נֶאֱחַז בַּסְּבַךְ בְּקַרְנָיו› event: see-ram —
# agent avraham
m.event("see_ram", agent="avraham")
# ‹וַיֵּלֶךְ אַבְרָהָם וַיִּקַּח אֶת־הָאַיִל וַיַּעֲלֵהוּ לְעֹלָה תַּחַת
# בְּנוֹ› event: offer-substitute — agent avraham; theme the-ayil
m.event("offer_substitute", agent="avraham", themes=["ha_ayil"])
# ‹אַיִל … נֶאֱחַז בַּסְּבַךְ … וַיַּעֲלֵהוּ לְעֹלָה תַּחַת בְּנוֹ› fact
# holds: ayil-neechaz-in-the-sevakh-in-qarnav; and-yaalehu-to-burnt-
# offering-tachat-beno
m.fact("ayil_neechaz_ba_sevakh_be_qarnav",
       "va_yaalehu_le_olah_tachat_beno")

# -------------------------- Gen.22.14 · THE_SENTENCE_NAME_AND_THE_SAYING ---
# וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה אֲשֶׁר יֵאָמֵר
# הַיּוֹם בְּהַר יְהוָה יֵרָאֶה
# "And Abraham called the name of that place Adonai-jireh; as it is said to
# this day: 'In the mount where the LORD is seen.'"
m.step("Gen.22.14")
# ‹וַיִּקְרָא אַבְרָהָם שֵׁם־הַמָּקוֹם הַהוּא יְהוָה יִרְאֶה› named: the-
# maqom := the-LORD-Yireh
m.name("ha_maqom", "YHWH_Yireh")
# ‹אֲשֶׁר יֵאָמֵר הַיּוֹם בְּהַר יְהוָה יֵרָאֶה› pattern recorded: which-
# yeamer-the-day-in-har-the-LORD-yeraeh
m.pattern("asher_yeamer_ha_yom_be_har_YHWH_yeraeh")

# -------------------------- Gen.22.15 · THE_SECOND_SKY_CALL ----------------
# וַיִּקְרָא מַלְאַךְ יְהוָה אֶל־אַבְרָהָם שֵׁנִית מִן־הַשָּׁמָיִם
# "And the angel of the LORD called unto Abraham a second time out of
# heaven,"
m.step("Gen.22.15")
# ‹וַיִּקְרָא … שֵׁנִית מִן־הַשָּׁמָיִם› event: sky-call — agent malakh-the-
# LORD
m.event("sky_call", agent="malakh_YHWH")

# -------------------------- Gen.22.16 · THE_DIVINE_SELF_OATH ---------------
# וַיֹּאמֶר בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה כִּי יַעַן אֲשֶׁר עָשִׂיתָ
# אֶת־הַדָּבָר הַזֶּה וְלֹא חָשַׂכְתָּ אֶת־בִּנְךָ אֶת־יְחִידֶךָ
# "and said: 'By Myself have I sworn, saith the LORD, because thou hast done
# this thing, and hast not withheld thy son, thine only son,"
m.step("Gen.22.16")
# ‹בִּי נִשְׁבַּעְתִּי נְאֻם־יְהוָה … יַעַן אֲשֶׁר עָשִׂיתָ› fact holds: bi-
# nishbati-neum-the-LORD; yaan-which-asita-and-not-chasakhta
m.fact("bi_nishbati_neum_YHWH",
       "yaan_asher_asita_ve_lo_chasakhta")

# -------------------------- Gen.22.17 · THE_DOUBLED_BLESSINGS --------------
# כִּי־בָרֵךְ אֲבָרֶכְךָ וְהַרְבָּה אַרְבֶּה אֶת־זַרְעֲךָ כְּכוֹכְבֵי
# הַשָּׁמַיִם וְכַחוֹל אֲשֶׁר עַל־שְׂפַת הַיָּם וְיִרַשׁ זַרְעֲךָ אֵת שַׁעַר
# אֹיְבָיו
# "that in blessing I will bless thee, and in multiplying I will multiply
# thy seed as the stars of the heaven, and as the sand which is upon the
# seashore; and thy seed shall possess the gate of his enemies;"
m.step("Gen.22.17")
# ‹בָרֵךְ אֲבָרֶכְךָ וְהַרְבָּה אַרְבֶּה … כְּכוֹכְבֵי … וְכַחוֹל› fact
# holds: varekh-avarekhkha-and-greatly-I-will-multiply; like-khokhvei-and-
# kha-chol-and-yirash-shaar-oyvav
m.fact("varekh_avarekhkha_ve_harbah_arbeh",
       "ke_khokhvei_ve_kha_chol_ve_yirash_shaar_oyvav")

# -------------------------- Gen.22.18 · THE_LISTENED_VOICE_GROUND ----------
# וְהִתְבָּרְכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ עֵקֶב אֲשֶׁר שָׁמַעְתָּ
# בְּקֹלִי
# "and in thy seed shall all the nations of the earth be blessed; because
# thou hast hearkened to My voice.'"
m.step("Gen.22.18")
# ‹וְהִתְבָּרְכוּ … עֵקֶב אֲשֶׁר שָׁמַעְתָּ בְּקֹלִי› fact holds: and-
# hitbarakhu-and-zarakha-all-goyei-the-earth; ekev-which-shamata-in-qoli
m.fact("ve_hitbarakhu_ve_zarakha_kol_goyei_ha_aretz",
       "ekev_asher_shamata_be_qoli")

# -------------------------- Gen.22.19 · THE_RETURN_AND_THE_DWELL -----------
# וַיָּשָׁב אַבְרָהָם אֶל־נְעָרָיו וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו אֶל־בְּאֵר
# שָׁבַע וַיֵּשֶׁב אַבְרָהָם בִּבְאֵר שָׁבַע
# "So Abraham returned unto his young men, and they rose up and went
# together to Beer-sheba; and Abraham dwelt at Beer-sheba."
m.step("Gen.22.19")
# ‹וַיָּשָׁב … וַיָּקֻמוּ וַיֵּלְכוּ יַחְדָּו … וַיֵּשֶׁב› event: return-
# dwell — agent avraham
m.event("return_dwell", agent="avraham")
# ‹אֶל־בְּאֵר שָׁבַע … בִּבְאֵר שָׁבַע› reads without prior install (flag,
# not fix): beer-seven
m.presupposed("beer_sheva")

# -------------------------- Gen.22.20-24 · THE_CODA_REPORT_THE_BRIDE_MINTED -
# וַיְהִי אַחֲרֵי הַדְּבָרִים הָאֵלֶּה וַיֻּגַּד לְאַבְרָהָם לֵאמֹר הִנֵּה
# יָלְדָה מִלְכָּה גַם־הִוא בָּנִים לְנָחוֹר אָחִיךָ … וּבְתוּאֵל יָלַד
# אֶת־רִבְקָה … וּפִילַגְשׁוֹ וּשְׁמָהּ רְאוּמָה וַתֵּלֶד גַּם־הִוא
# "And it came to pass after these things, that it was told Abraham, saying:
# 'Behold, Milcah, she also hath borne children unto thy brother Nahor: Uz
# his first-born, and Buz his brother, and Kemuel the father of Aram; and
# Chesed, and Hazo, and Pildash, and Jidlaph, and Bethuel.' And Bethuel
# begot Rebekah; these eight Milcah bore to Nahor, Abraham's brother. And
# his concubine, whose name was Reumah, she also bore Tebah, and Gaham, and
# Tahash, and Maacah."
m.step("Gen.22.20-24")
# ‹וַיֻּגַּד לְאַבְרָהָם … הִנֵּה יָלְדָה מִלְכָּה גַם־הִוא … וּבְתוּאֵל
# יָלַד אֶת־רִבְקָה› fact holds: and-yugad-to-avraham-behold-yaldah-milkah-
# also-hi; and-vetuel-yalad-rivqah
m.fact("va_yugad_le_avraham_hinneh_yaldah_milkah_gam_hi",
       "u_vetuel_yalad_et_rivqah")
# ‹שְׁמֹנָה אֵלֶּה יָלְדָה מִלְכָּה … וּפִילַגְשׁוֹ … וַתֵּלֶד גַּם־הִוא›
# fact holds: shmonah-ele-yaldah-milkah-and-filagsho-reumah-four
m.fact("shmonah_ele_yaldah_milkah_u_filagsho_reumah_arbaah")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'shnei_nearav', 'malakh_YHWH', 'yitzchaq'}
    assert m.presupposed_set() == {'beer_sheva'}
    assert m.REGISTRY["names"] == {'ha_maqom': 'YHWH_Yireh'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['qach_lekh_ve_haalehu(et_binkha, le_olah)', 'shevu(po_im_ha_chamor)', 'tishlach(yadkha_el_ha_naar)', 'taas(lo_meumah)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1, 'read_before_install': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['achar_ha_devarim_ve_ha_elohim_nisah_et_avraham', 'va_yomer_hineni', 'et_binkha_et_yechidkha_asher_ahavta_et_yitzchaq', 'el_eretz_ha_moriyah_asher_omar_elekha', 'va_yashkem_ba_boqer_va_yachavosh_et_chamoro', 'ba_yom_ha_shelishi_va_yar_et_ha_maqom_me_rachoq', 'nelkha_ve_nishtachaveh_ve_nashuvah_aleikhem', 'avi_va_yomer_hineni_veni', 've_ayeh_ha_seh_le_olah', 'elohim_yireh_lo_ha_seh_le_olah_beni', 'va_yaaqod_et_yitzchaq_va_yasem_al_ha_mizbeach', 'avraham_avraham_va_yomer_hineni', 'atah_yadati_ki_yere_elohim_atah', 've_lo_chasakhta_et_binkha_et_yechidkha', 'ayil_neechaz_ba_sevakh_be_qarnav', 'va_yaalehu_le_olah_tachat_beno', 'pattern: asher_yeamer_ha_yom_be_har_YHWH_yeraeh', 'bi_nishbati_neum_YHWH', 'yaan_asher_asita_ve_lo_chasakhta', 'varekh_avarekhkha_ve_harbah_arbeh', 'ke_khokhvei_ve_kha_chol_ve_yirash_shaar_oyvav', 've_hitbarakhu_ve_zarakha_kol_goyei_ha_aretz', 'ekev_asher_shamata_be_qoli', 'va_yugad_le_avraham_hinneh_yaldah_milkah_gam_hi', 'u_vetuel_yalad_et_rivqah', 'shmonah_ele_yaldah_milkah_u_filagsho_reumah_arbaah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 14
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_39_machpelah_purchase
###############################################################################
# =============================================================================
# gen_39_machpelah_purchase — 23:1-20
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_39_machpelah_purchase.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Sarah's death and the Machpelah purchase (23:1-20)"""
from machine import Machine

m = Machine("gen_39_machpelah_purchase")

# -------------------------- Gen.23.1 · THE_LIFE_COUNT ----------------------
# וַיִּהְיוּ חַיֵּי שָׂרָה מֵאָה שָׁנָה וְעֶשְׂרִים שָׁנָה וְשֶׁבַע שָׁנִים
# שְׁנֵי חַיֵּי שָׂרָה
# "And the life of Sarah was a hundred and seven and twenty years; these
# were the years of the life of Sarah."
m.step("Gen.23.1")
# ‹חַיֵּי שָׂרָה› the world gains: sarah
m.install("sarah")
# ‹מֵאָה שָׁנָה וְעֶשְׂרִים שָׁנָה וְשֶׁבַע שָׁנִים› fact holds: chayei-
# sarah-hundred-and-esrim-and-seven-shanim
m.fact("chayei_sarah_meah_ve_esrim_ve_sheva_shanim")

# -------------------------- Gen.23.2 · THE_DEATH_AND_THE_MOURNING ----------
# וַתָּמָת שָׂרָה בְּקִרְיַת אַרְבַּע הִוא חֶבְרוֹן בְּאֶרֶץ כְּנָעַן
# וַיָּבֹא אַבְרָהָם לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ
# "And Sarah died in Kiriatharba—the same is Hebron—in the land of Canaan;
# and Abraham came to mourn for Sarah, and to weep for her."
m.step("Gen.23.2")
# ‹וַתָּמָת שָׂרָה› event: die — theme sarah
m.event("die", themes=["sarah"])
# ‹לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ› event: mourn-weep — agent avraham; theme
# sarah
m.event("mourn_weep", agent="avraham", themes=["sarah"])
# ‹וַתָּמָת שָׂרָה … לִסְפֹּד לְשָׂרָה וְלִבְכֹּתָהּ› fact holds: and-tamat-
# sarah-in-qiryat-arba-hi-chevron; to-me-sepod-to-sarah-and-livkotah
m.fact("va_tamat_sarah_be_qiryat_arba_hi_chevron",
       "li_sepod_le_sarah_ve_livkotah")
# ‹הִוא חֶבְרוֹן› reads without prior install (flag, not fix): chevron
m.presupposed("chevron")

# -------------------------- Gen.23.3 · THE_RISING_FROM_THE_DEAD_FACE -------
# וַיָּקָם אַבְרָהָם מֵעַל פְּנֵי מֵתוֹ וַיְדַבֵּר אֶל־בְּנֵי־חֵת לֵאמֹר
# "And Abraham rose up from before his dead, and spoke unto the children of
# Heth, saying:"
m.step("Gen.23.3")
# ‹וַיָּקָם … מֵעַל פְּנֵי מֵתוֹ וַיְדַבֵּר› event: rise-speak — agent
# avraham
m.event("rise_speak", agent="avraham")

# -------------------------- Gen.23.4 · THE_SOJOURNER_ASKS_FOR_A_GRAVE ------
# גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם תְּנוּ לִי אֲחֻזַּת־קֶבֶר עִמָּכֶם
# וְאֶקְבְּרָה מֵתִי מִלְּפָנָי
# "'I am a stranger and a sojourner with you: give me a possession of a
# burying-place with you, that I may bury my dead out of my sight.'"
m.step("Gen.23.4")
# ‹גֵּר־וְתוֹשָׁב אָנֹכִי עִמָּכֶם› fact holds: ger-and-toshav-anokhi-
# imakhem
m.fact("ger_ve_toshav_anokhi_imakhem")
# ‹תְּנוּ לִי אֲחֻזַּת־קֶבֶר עִמָּכֶם› avraham speaks a demand — LET:
# tenu(achuzat-qever)
m.declare("avraham", "LET",
          "tenu(achuzat_qever)")

# -------------------------- Gen.23.5 · THE_ANSWER_FRAME --------------------
# וַיַּעֲנוּ בְנֵי־חֵת אֶת־אַבְרָהָם לֵאמֹר לוֹ
# "And the children of Heth answered Abraham, saying unto him:"
m.step("Gen.23.5")
# ‹בְנֵי־חֵת› the world gains: sons-of-chet
m.install("bnei_chet")

# -------------------------- Gen.23.6 · THE_PRINCE_AND_THE_CHOICE_GRAVES ----
# שְׁמָעֵנוּ אֲדֹנִי נְשִׂיא אֱלֹהִים אַתָּה בְּתוֹכֵנוּ בְּמִבְחַר
# קְבָרֵינוּ קְבֹר אֶת־מֵתֶךָ אִישׁ מִמֶּנּוּ אֶת־קִבְרוֹ לֹא־יִכְלֶה
# מִמְּךָ מִקְּבֹר מֵתֶךָ
# "'Hear us, my lord: thou art a mighty prince among us; in the choice of
# our sepulchres bury thy dead; none of us shall withhold from thee his
# sepulchre, but that thou mayest bury thy dead.'"
m.step("Gen.23.6")
# ‹שְׁמָעֵנוּ אֲדֹנִי› sons-of-chet speaks a demand — LET: shemaenu(adoni)
m.declare("bnei_chet", "LET",
          "shemaenu(adoni)")
# ‹בְּמִבְחַר קְבָרֵינוּ קְבֹר אֶת־מֵתֶךָ› sons-of-chet speaks a demand —
# LET: qevor(in-mivchar-qevareinu)
m.declare("bnei_chet", "LET",
          "qevor(be_mivchar_qevareinu)")
# ‹נְשִׂיא אֱלֹהִים אַתָּה בְּתוֹכֵנוּ› fact holds: nesi-God-you-in-tokhenu
m.fact("nesi_elohim_atah_be_tokhenu")

# -------------------------- Gen.23.7 · THE_FIRST_BOW -----------------------
# וַיָּקָם אַבְרָהָם וַיִּשְׁתַּחוּ לְעַם־הָאָרֶץ לִבְנֵי־חֵת
# "And Abraham rose up, and bowed down to the people of the land, even to
# the children of Heth."
m.step("Gen.23.7")
# ‹וַיִּשְׁתַּחוּ לְעַם־הָאָרֶץ› event: bow — agent avraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.8 · THE_ENTREATY_COMPOUND ---------------
# וַיְדַבֵּר אִתָּם לֵאמֹר אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר אֶת־מֵתִי
# מִלְּפָנַי שְׁמָעוּנִי וּפִגְעוּ־לִי בְּעֶפְרוֹן בֶּן־צֹחַר
# "And he spoke with them, saying: 'If it be your mind that I should bury my
# dead out of my sight, hear me, and entreat for me to Ephron the son of
# Zohar,"
m.step("Gen.23.8")
# ‹שְׁמָעוּנִי וּפִגְעוּ־לִי בְּעֶפְרוֹן› avraham speaks a demand — LET:
# shimuni-and-figu(in-efron)
m.declare("avraham", "LET",
          "shimuni_u_figu(be_efron)")
# ‹אִם־יֵשׁ אֶת־נַפְשְׁכֶם לִקְבֹּר אֶת־מֵתִי› fact holds: if-yesh-
# nafshekhem-liqbor-meti
m.fact("im_yesh_et_nafshekhem_liqbor_et_meti")

# -------------------------- Gen.23.9 · THE_FULL_PRICE_CLAUSE ---------------
# וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה אֲשֶׁר־לוֹ אֲשֶׁר בִּקְצֵה שָׂדֵהוּ
# בְּכֶסֶף מָלֵא יִתְּנֶנָּה לִי בְּתוֹכְכֶם לַאֲחֻזַּת־קָבֶר
# "that he may give me the cave of Machpelah, which he hath, which is in the
# end of his field; for the full price let him give it to me in the midst of
# you for a possession of a burying-place.'"
m.step("Gen.23.9")
# ‹וְיִתֶּן־לִי אֶת־מְעָרַת הַמַּכְפֵּלָה … בְּכֶסֶף מָלֵא› fact holds: and-
# yiten-to-me-mearat-the-makhpelah; in-khesef-male-yitnenah-to-me
m.fact("ve_yiten_li_et_mearat_ha_makhpelah",
       "be_khesef_male_yitnenah_li")

# -------------------------- Gen.23.10 · THE_ANSWER_FROM_INSIDE_THE_ROOM ----
# וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ בְּנֵי־חֵת וַיַּעַן עֶפְרוֹן הַחִתִּי
# אֶת־אַבְרָהָם בְּאָזְנֵי בְנֵי־חֵת לְכֹל בָּאֵי שַׁעַר־עִירוֹ לֵאמֹר
# "Now Ephron was sitting in the midst of the children of Heth; and Ephron
# the Hittite answered Abraham in the hearing of the children of Heth, even
# of all that went in at the gate of his city, saying:"
m.step("Gen.23.10")
# ‹וְעֶפְרוֹן יֹשֵׁב בְּתוֹךְ בְּנֵי־חֵת› the world gains: efron
m.install("efron")
# ‹בְּאָזְנֵי בְנֵי־חֵת לְכֹל בָּאֵי שַׁעַר־עִירוֹ› fact holds: in-oznei-
# vnei-chet-to-all-baei-shaar-iro
m.fact("be_oznei_vnei_chet_le_khol_baei_shaar_iro")

# -------------------------- Gen.23.11 · THE_GIFT_ROUND ---------------------
# לֹא־אֲדֹנִי שְׁמָעֵנִי הַשָּׂדֶה נָתַתִּי לָךְ וְהַמְּעָרָה אֲשֶׁר־בּוֹ
# לְךָ נְתַתִּיהָ לְעֵינֵי בְנֵי־עַמִּי נְתַתִּיהָ לָּךְ קְבֹר מֵתֶךָ
# "'Nay, my lord, hear me: the field give I thee, and the cave that is
# therein, I give it thee; in the presence of the sons of my people give I
# it thee; bury thy dead.'"
m.step("Gen.23.11")
# ‹לֹא־אֲדֹנִי שְׁמָעֵנִי› efron speaks a demand — LET: shemaeni(not-adoni)
m.declare("efron", "LET",
          "shemaeni(lo_adoni)")
# ‹קְבֹר מֵתֶךָ› efron speaks a demand — LET: qevor(metekha)
m.declare("efron", "LET",
          "qevor(et_metekha)")
# ‹הַשָּׂדֶה נָתַתִּי לָךְ … נְתַתִּיהָ› fact holds: the-field-natati-to-
# you-netatiha
m.fact("ha_sadeh_natati_lakh_netatiha")

# -------------------------- Gen.23.12 · THE_SECOND_BOW ---------------------
# וַיִּשְׁתַּחוּ אַבְרָהָם לִפְנֵי עַם הָאָרֶץ
# "And Abraham bowed down before the people of the land."
m.step("Gen.23.12")
# ‹וַיִּשְׁתַּחוּ … לִפְנֵי עַם הָאָרֶץ› event: bow — agent avraham
m.event("bow", agent="avraham")

# -------------------------- Gen.23.13 · THE_WISH_AND_THE_TAKE_DEMAND -------
# וַיְדַבֵּר אֶל־עֶפְרוֹן בְּאָזְנֵי עַם־הָאָרֶץ לֵאמֹר אַךְ אִם־אַתָּה לוּ
# שְׁמָעֵנִי נָתַתִּי כֶּסֶף הַשָּׂדֶה קַח מִמֶּנִּי וְאֶקְבְּרָה אֶת־מֵתִי
# שָׁמָּה
# "And he spoke unto Ephron in the hearing of the people of the land,
# saying: 'But if thou wilt, I pray thee, hear me: I will give the price of
# the field; take it of me, and I will bury my dead there.'"
m.step("Gen.23.13")
# ‹אַךְ אִם־אַתָּה לוּ שְׁמָעֵנִי נָתַתִּי כֶּסֶף הַשָּׂדֶה› fact holds:
# akh-if-you-lu-shemaeni; natati-kesef-the-field
m.fact("akh_im_atah_lu_shemaeni",
       "natati_kesef_ha_sadeh")
# ‹קַח מִמֶּנִּי› avraham speaks a demand — LET: qach(kesef-the-field)
m.declare("avraham", "LET",
          "qach(kesef_ha_sadeh)")

# -------------------------- Gen.23.14 · THE_SECOND_ANSWER_FRAME ------------
# וַיַּעַן עֶפְרוֹן אֶת־אַבְרָהָם לֵאמֹר לוֹ
# "And Ephron answered Abraham, saying unto him:"
m.step("Gen.23.14")
# ‹וַיַּעַן עֶפְרוֹן› event: answer — agent efron
m.event("answer", agent="efron")

# -------------------------- Gen.23.15 · THE_PRICE_ROUND --------------------
# אֲדֹנִי שְׁמָעֵנִי אֶרֶץ אַרְבַּע מֵאֹת שֶׁקֶל־כֶּסֶף בֵּינִי וּבֵינְךָ
# מַה־הִוא וְאֶת־מֵתְךָ קְבֹר
# "'My lord, hearken unto me: a piece of land worth four hundred shekels of
# silver, what is that betwixt me and thee? bury therefore thy dead.'"
m.step("Gen.23.15")
# ‹אֲדֹנִי שְׁמָעֵנִי› efron speaks a demand — LET: shemaeni(adoni)
m.declare("efron", "LET",
          "shemaeni(adoni)")
# ‹אֶרֶץ אַרְבַּע מֵאֹת שֶׁקֶל־כֶּסֶף … וְאֶת־מֵתְךָ קְבֹר› fact holds:
# earth-arba-meot-sheqel-kesef-beini-and-veinkha; and-metkha-qevor-resound
m.fact("eretz_arba_meot_sheqel_kesef_beini_u_veinkha",
       "ve_et_metkha_qevor_resound")

# -------------------------- Gen.23.16 · CYCLE_A_THE_HEARING_AND_THE_WEIGHING -
# וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן
# אֶת־הַכֶּסֶף אֲשֶׁר דִּבֶּר בְּאָזְנֵי בְנֵי־חֵת אַרְבַּע מֵאוֹת שֶׁקֶל
# כֶּסֶף עֹבֵר לַסֹּחֵר
# "And Abraham hearkened unto Ephron; and Abraham weighed to Ephron the
# silver, which he had named in the hearing of the children of Heth, four
# hundred shekels of silver, current money with the merchant."
m.step("Gen.23.16")
# ‹וַיִּשְׁמַע אַבְרָהָם אֶל־עֶפְרוֹן› demand settled (popped from the
# queue): shemaeni(adoni)
m.result("shemaeni(adoni)", tmark="t1")
# ‹וַיִּשְׁקֹל אַבְרָהָם לְעֶפְרֹן אֶת־הַכֶּסֶף› event: weigh-silver — agent
# avraham
m.event("weigh_silver", agent="avraham")
# ‹אַרְבַּע מֵאוֹת שֶׁקֶל כֶּסֶף עֹבֵר לַסֹּחֵר› fact holds: and-yishqol-
# arba-meot-sheqel-over-to-socher
m.fact("va_yishqol_arba_meot_sheqel_over_la_socher")

# -------------------------- Gen.23.17 · THE_FIELD_ARISES -------------------
# וַיָּקָם שְׂדֵה עֶפְרוֹן אֲשֶׁר בַּמַּכְפֵּלָה אֲשֶׁר לִפְנֵי מַמְרֵא
# הַשָּׂדֶה וְהַמְּעָרָה אֲשֶׁר־בּוֹ וְכָל־הָעֵץ אֲשֶׁר בַּשָּׂדֶה אֲשֶׁר
# בְּכָל־גְּבֻלוֹ סָבִיב
# "So the field of Ephron, which was in Machpelah, which was before Mamre,
# the field, and the cave which was therein, and all the trees that were in
# the field, that were in all the border thereof round about, were made
# sure"
m.step("Gen.23.17")
# ‹וַיָּקָם שְׂדֵה עֶפְרוֹן … וְכָל־הָעֵץ … סָבִיב› fact holds: and-yaqam-
# sdeh-efron-in-the-makhpelah; the-field-and-the-mearah-and-all-the-tree-
# saviv
m.fact("va_yaqam_sdeh_efron_ba_makhpelah",
       "ha_sadeh_ve_ha_mearah_ve_khol_ha_etz_saviv")

# -------------------------- Gen.23.18 · THE_PURCHASE_BEFORE_THE_GATE -------
# לְאַבְרָהָם לְמִקְנָה לְעֵינֵי בְנֵי־חֵת בְּכֹל בָּאֵי שַׁעַר־עִירוֹ
# "unto Abraham for a possession in the presence of the children of Heth,
# before all that went in at the gate of his city."
m.step("Gen.23.18")
# ‹לְאַבְרָהָם לְמִקְנָה› fact holds: to-avraham-to-miqnah-to-eyes-of-vnei-
# chet
m.fact("le_avraham_le_miqnah_le_einei_vnei_chet")

# -------------------------- Gen.23.19 · CYCLE_B_THE_BURIAL -----------------
# וְאַחֲרֵי־כֵן קָבַר אַבְרָהָם אֶת־שָׂרָה אִשְׁתּוֹ אֶל־מְעָרַת שְׂדֵה
# הַמַּכְפֵּלָה עַל־פְּנֵי מַמְרֵא הִוא חֶבְרוֹן בְּאֶרֶץ כְּנָעַן
# "And after this, Abraham buried Sarah his wife in the cave of the field of
# Machpelah before Mamre—the same is Hebron—in the land of Canaan."
m.step("Gen.23.19")
# ‹קָבַר אַבְרָהָם אֶת־שָׂרָה אִשְׁתּוֹ› demand settled (popped from the
# queue): qevor(metekha)
m.result("qevor(et_metekha)", tmark="t2")
# ‹עַל־פְּנֵי מַמְרֵא הִוא חֶבְרוֹן› reads without prior install (flag, not
# fix): mamre
m.presupposed("mamre")

# -------------------------- Gen.23.20 · THE_CONVEYANCE_CODA ----------------
# וַיָּקָם הַשָּׂדֶה וְהַמְּעָרָה אֲשֶׁר־בּוֹ לְאַבְרָהָם לַאֲחֻזַּת־קָבֶר
# מֵאֵת בְּנֵי־חֵת
# "And the field, and the cave that is therein, were made sure unto Abraham
# for a possession of a burying-place by the children of Heth."
m.step("Gen.23.20")
# ‹וַיָּקָם הַשָּׂדֶה … לַאֲחֻזַּת־קָבֶר› fact holds: and-yaqam-the-field-
# to-achuzat-qaver-from-sons-of-chet
m.fact("va_yaqam_ha_sadeh_la_achuzat_qaver_me_et_bnei_chet")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'efron', 'bnei_chet', 'sarah'}
    assert m.presupposed_set() == {'mamre', 'chevron'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['tenu(achuzat_qever)', 'shemaenu(adoni)', 'qevor(be_mivchar_qevareinu)', 'shimuni_u_figu(be_efron)', 'shemaeni(lo_adoni)', 'qach(kesef_ha_sadeh)']
    assert len(m.SPECS["log"]) == 8
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['chayei_sarah_meah_ve_esrim_ve_sheva_shanim', 'va_tamat_sarah_be_qiryat_arba_hi_chevron', 'li_sepod_le_sarah_ve_livkotah', 'ger_ve_toshav_anokhi_imakhem', 'nesi_elohim_atah_be_tokhenu', 'im_yesh_et_nafshekhem_liqbor_et_meti', 've_yiten_li_et_mearat_ha_makhpelah', 'be_khesef_male_yitnenah_li', 'be_oznei_vnei_chet_le_khol_baei_shaar_iro', 'ha_sadeh_natati_lakh_netatiha', 'akh_im_atah_lu_shemaeni', 'natati_kesef_ha_sadeh', 'eretz_arba_meot_sheqel_kesef_beini_u_veinkha', 've_et_metkha_qevor_resound', 'va_yishqol_arba_meot_sheqel_over_la_socher', 'va_yaqam_sdeh_efron_ba_makhpelah', 'ha_sadeh_ve_ha_mearah_ve_khol_ha_etz_saviv', 'le_avraham_le_miqnah_le_einei_vnei_chet', 'va_yaqam_ha_sadeh_la_achuzat_qaver_me_et_bnei_chet'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 17
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_40_servant_oath_well
###############################################################################
# =============================================================================
# gen_40_servant_oath_well — 24:1-33
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_40_servant_oath_well.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The servant's oath and the well (24:1-33)"""
from machine import Machine

m = Machine("gen_40_servant_oath_well")

# -------------------------- Gen.24.1 · THE_OLD_AND_THE_BLESSED -------------
# וְאַבְרָהָ֣ם זָקֵ֔ן בָּ֖א בַּיָּמִ֑ים וַֽיהוָ֛ה בֵּרַ֥ךְ אֶת־אַבְרָהָ֖ם
# בַּכֹּֽל
# "[EN-AID] And Abraham was old, advanced in days; and YHWH had blessed
# Abraham in all."
m.step("Gen.24.1")
# ‹אַבְרָהָם … יְהוָה› reads without prior install (flag, not fix): avraham,
# the-LORD
m.presupposed("avraham", "YHWH")
# ‹זָקֵן בָּא בַּיָּמִים … בֵּרַךְ אֶת־אַבְרָהָם בַּכֹּל› fact holds:
# avraham-zaqen-in-the-in-the-seas; the-LORD-berakh-avraham-in-the-all
m.fact("avraham_zaqen_ba_ba_yamim",
       "YHWH_berakh_et_avraham_ba_kol")

# -------------------------- Gen.24.2 · THE_THIGH_GESTURE_DEMAND ------------
# וַיֹּ֣אמֶר אַבְרָהָ֗ם אֶל־עַבְדּוֹ֙ זְקַ֣ן בֵּית֔וֹ הַמֹּשֵׁ֖ל
# בְּכָל־אֲשֶׁר־ל֑וֹ שִֽׂים־נָ֥א יָדְךָ֖ תַּ֥חַת יְרֵכִֽי
# "[EN-AID] And Abraham said to his servant, the elder of his house, who
# ruled over all that was his: Place, please, your hand under my thigh."
m.step("Gen.24.2")
# ‹וַיֹּאמֶר אַבְרָהָם אֶל־עַבְדּוֹ› event: say — agent avraham
m.event("say", agent="avraham")
# ‹עַבְדּוֹ … הַמֹּשֵׁל בְּכָל־אֲשֶׁר־לוֹ› the world gains: the-eved
m.install("ha_eved")
# ‹שִׂים־נָא יָדְךָ תַּחַת יְרֵכִי› avraham speaks a demand — LET: sim(the-
# eved, yad-tachat-yerekh)
m.declare("avraham", "LET",
          "sim(ha_eved, yad_tachat_yerekh)")

# -------------------------- Gen.24.3 · THE_OATH_FRAME_AND_THE_NOT_TAKE -----
# וְאַשְׁבִּ֣יעֲךָ֔ בַּֽיהוָה֙ אֱלֹהֵ֣י הַשָּׁמַ֔יִם וֵֽאלֹהֵ֖י הָאָ֑רֶץ
# אֲשֶׁ֨ר לֹֽא־תִקַּ֤ח אִשָּׁה֙ לִבְנִ֔י מִבְּנוֹת֙ הַֽכְּנַעֲנִ֔י אֲשֶׁ֥ר
# אָנֹכִ֖י יוֹשֵׁ֥ב בְּקִרְבּֽוֹ
# "[EN-AID] And I will make you swear by YHWH, God of the heavens and God of
# the earth, that you shall not take a wife for my son from the daughters of
# the Canaanite among whom I dwell."
m.step("Gen.24.3")
# ‹וְאַשְׁבִּיעֲךָ בַּיהוָה› fact holds: and-ashbia-kha-in-the-the-LORD
m.fact("ve_ashbia_kha_ba_YHWH")
# ‹לֹא־תִקַּח אִשָּׁה לִבְנִי מִבְּנוֹת הַכְּנַעֲנִי› fact holds: not-
# tiqach-isha-to-me-veni-from-benot-the-kenaani
m.fact("lo_tiqach_isha_li_veni_mi_benot_ha_kenaani")

# -------------------------- Gen.24.4 · THE_GO_AND_THE_TAKE_DUTY ------------
# כִּ֧י אֶל־אַרְצִ֛י וְאֶל־מוֹלַדְתִּ֖י תֵּלֵ֑ךְ וְלָקַחְתָּ֥ אִשָּׁ֖ה
# לִבְנִ֥י לְיִצְחָֽק
# "[EN-AID] But to my land and to my kindred you shall go, and you shall
# take a wife for my son, for Isaac."
m.step("Gen.24.4")
# ‹אֶל־אַרְצִי וְאֶל־מוֹלַדְתִּי תֵּלֵךְ› fact holds: telekh-to-artzi-and-
# to-moladti
m.fact("telekh_el_artzi_ve_el_moladti")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי לְיִצְחָק› fact holds: laqachta(the-eved,
# isha-to-me-yitzchaq)
m.fact("laqachta(ha_eved, isha_li_yitzchaq)")

# -------------------------- Gen.24.5 · THE_SERVANT_ASKS_THE_RETURN_CASE ----
# וַיֹּ֤אמֶר אֵלָיו֙ הָעֶ֔בֶד אוּלַי֙ לֹא־תֹאבֶ֣ה הָֽאִשָּׁ֔ה לָלֶ֥כֶת
# אַחֲרַ֖י אֶל־הָאָ֣רֶץ הַזֹּ֑את הֶֽהָשֵׁ֤ב אָשִׁיב֙ אֶת־בִּנְךָ֔
# אֶל־הָאָ֖רֶץ אֲשֶׁר־יָצָ֥אתָ מִשָּֽׁם
# "[EN-AID] And the servant said to him: Perhaps the woman will not be
# willing to follow me to this land; shall I indeed bring your son back to
# the land from which you came?"
m.step("Gen.24.5")
# ‹וַיֹּאמֶר אֵלָיו הָעֶבֶד› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹אוּלַי לֹא־תֹאבֶה … הֶהָשֵׁב אָשִׁיב› fact holds: ulay-not-tove-the-isha-
# to-lekhet; question-he-hashev-ashiv
m.fact("ulay_lo_tove_ha_isha_la_lekhet",
       "question_he_hashev_ashiv")

# -------------------------- Gen.24.6 · THE_GUARD_LEST_YOU_RETURN -----------
# וַיֹּ֥אמֶר אֵלָ֖יו אַבְרָהָ֑ם הִשָּׁ֣מֶר לְךָ֔ פֶּן־תָּשִׁ֥יב אֶת־בְּנִ֖י
# שָֽׁמָּה
# "[EN-AID] And Abraham said to him: Guard yourself, lest you return my son
# there."
m.step("Gen.24.6")
# ‹וַיֹּאמֶר אֵלָיו אַבְרָהָם› event: say — agent avraham
m.event("say", agent="avraham")
# ‹הִשָּׁמֶר לְךָ פֶּן־תָּשִׁיב אֶת־בְּנִי שָׁמָּה› avraham speaks a demand
# — LET: hishamer(the-eved, lest-tashiv-beni-shama)
m.declare("avraham", "LET",
          "hishamer(ha_eved, pen_tashiv_et_beni_shama)")

# -------------------------- Gen.24.7 · THE_PAST_OATH_AND_THE_ANGEL_PROMISE -
# יְהוָ֣ה אֱלֹהֵ֣י הַשָּׁמַ֗יִם אֲשֶׁ֨ר לְקָחַ֜נִי מִבֵּ֣ית אָבִי֮
# וּמֵאֶ֣רֶץ מֽוֹלַדְתִּי֒ וַאֲשֶׁ֨ר דִּבֶּר־לִ֜י וַאֲשֶׁ֤ר נִֽשְׁבַּֽע־לִי֙
# לֵאמֹ֔ר לְזַ֨רְעֲךָ֔ אֶתֵּ֖ן אֶת־הָאָ֣רֶץ הַזֹּ֑את ה֗וּא יִשְׁלַ֤ח
# מַלְאָכוֹ֙ לְפָנֶ֔יךָ וְלָקַחְתָּ֥ אִשָּׁ֛ה לִבְנִ֖י מִשָּֽׁם
# "[EN-AID] YHWH, God of the heavens, who took me from my father's house and
# from the land of my kindred, and who spoke to me and who swore to me,
# saying, To your seed I will give this land — He will send His angel before
# you, and you shall take a wife for my son from there."
m.step("Gen.24.7")
# ‹נִשְׁבַּע־לִי … אֶתֵּן אֶת־הָאָרֶץ הַזֹּאת› fact holds: past-oath-nishba-
# to-me; quoted-eten-to-zara-kha
m.fact("past_oath_nishba_li",
       "quoted_eten_le_zara_kha")
# ‹הוּא יִשְׁלַח מַלְאָכוֹ לְפָנֶיךָ› fact holds: yishlach-malakh-o-to-fane-
# kha
m.fact("yishlach_malakh_o_le_fane_kha")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי מִשָּׁם› fact holds: laqachta(the-eved, isha-
# to-me-veni-from-there)
m.fact("laqachta(ha_eved, isha_li_veni_mi_sham)")

# -------------------------- Gen.24.8 · THE_RELEASE_CONDITION ---------------
# וְאִם־לֹ֨א תֹאבֶ֤ה הָֽאִשָּׁה֙ לָלֶ֣כֶת אַחֲרֶ֔יךָ וְנִקִּ֕יתָ
# מִשְּׁבֻעָתִ֖י זֹ֑את רַ֣ק אֶת־בְּנִ֔י לֹ֥א תָשֵׁ֖ב שָֽׁמָּה
# "[EN-AID] And if the woman is not willing to follow you, then you shall be
# free from this my oath; only my son you shall not return there."
m.step("Gen.24.8")
# ‹וְאִם־לֹא תֹאבֶה … וְנִקִּיתָ מִשְּׁבֻעָתִי זֹאת› fact holds: release-if-
# not-tove-then-niqita-from-shevuah
m.fact("release_if_lo_tove_then_niqita_mi_shevuah")
# ‹רַק אֶת־בְּנִי לֹא תָשֵׁב שָׁמָּה› fact holds: raq-beni-not-tashev-shama
m.fact("raq_et_beni_lo_tashev_shama")

# -------------------------- Gen.24.9 · THE_THIGH_POP_AND_THE_SWEAR ---------
# וַיָּ֤שֶׂם הָעֶ֨בֶד֙ אֶת־יָד֔וֹ תַּ֛חַת יֶ֥רֶךְ אַבְרָהָ֖ם אֲדֹנָ֑יו
# וַיִּשָּׁ֣בַֽע ל֔וֹ עַל־הַדָּבָ֖ר הַזֶּֽה
# "[EN-AID] And the servant placed his hand under the thigh of Abraham his
# master, and swore to him concerning this matter."
m.step("Gen.24.9")
# ‹וַיָּשֶׂם הָעֶבֶד אֶת־יָדוֹ תַּחַת יֶרֶךְ אַבְרָהָם› demand settled
# (popped from the queue): sim(the-eved, yad-tachat-yerekh)
m.result("sim(ha_eved, yad_tachat_yerekh)", tmark="t1")
# ‹וַיִּשָּׁבַע לוֹ עַל־הַדָּבָר הַזֶּה› event: swear — agent the-eved;
# theme the-davar-the-ze
m.event("swear", agent="ha_eved", themes=["ha_davar_ha_ze"])

# -------------------------- Gen.24.10 · THE_JOURNEY_TO_ARAM_NAHARAYIM ------
# וַיִּקַּ֣ח הָ֠עֶבֶד עֲשָׂרָ֨ה גְמַלִּ֜ים מִגְּמַלֵּ֤י אֲדֹנָיו֙ וַיֵּ֔לֶךְ
# וְכָל־ט֥וּב אֲדֹנָ֖יו בְּיָד֑וֹ וַיָּ֗קָם וַיֵּ֛לֶךְ אֶל־אֲרַ֥ם
# נַֽהֲרַ֖יִם אֶל־עִ֥יר נָחֽוֹר
# "[EN-AID] And the servant took ten camels from his master's camels and
# went, with all his master's goods in his hand; and he rose and went to
# Aram-naharayim, to the city of Nahor."
m.step("Gen.24.10")
# ‹וַיִּקַּח … וַיֵּלֶךְ … וַיָּקָם וַיֵּלֶךְ› event: take-go-rise-go —
# agent the-eved; theme gemalim-tuv
m.event("take_go_rise_go", agent="ha_eved", themes=["gemalim_tuv"])
# ‹אֲרַם נַהֲרַיִם … עִיר נָחוֹר› reads without prior install (flag, not
# fix): aram-naharayim, ir-nachor
m.presupposed("aram_naharayim", "ir_nachor")

# -------------------------- Gen.24.11 · THE_CAMELS_AT_THE_WELL -------------
# וַיַּבְרֵ֧ךְ הַגְּמַלִּ֛ים מִח֥וּץ לָעִ֖יר אֶל־בְּאֵ֣ר הַמָּ֑יִם לְעֵ֣ת
# עֶ֔רֶב לְעֵ֖ת צֵ֥את הַשֹּׁאֲבֹֽת
# "[EN-AID] And he made the camels kneel outside the city by the well of
# water, at evening time, the time the water-drawers go out."
m.step("Gen.24.11")
# ‹וַיַּבְרֵךְ הַגְּמַלִּים … אֶל־בְּאֵר הַמָּיִם› event: kneel-camels —
# agent the-eved; theme the-gemalim
m.event("kneel_camels", agent="ha_eved", themes=["ha_gemalim"])

# -------------------------- Gen.24.12 · THE_PRAYER_IMPERATIVES_AT_YHWH -----
# וַיֹּאמַ֓ר יְהוָ֗ה אֱלֹהֵי֙ אֲדֹנִ֣י אַבְרָהָ֔ם הַקְרֵה־נָ֥א לְפָנַ֖י
# הַיּ֑וֹם וַעֲשֵׂה־חֶ֕סֶד עִ֖ם אֲדֹנִ֥י אַבְרָהָֽם
# "[EN-AID] And he said: YHWH, God of my master Abraham, cause it to happen
# before me today, and do kindness with my master Abraham."
m.step("Gen.24.12")
# ‹וַיֹּאמַר› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹הַקְרֵה־נָא לְפָנַי הַיּוֹם› the-eved speaks a demand — LET: haqreh(the-
# LORD, before-Me-hayom)
m.declare("ha_eved", "LET",
          "haqreh(YHWH, lefanai_hayom)")
# ‹וַעֲשֵׂה־חֶסֶד עִם אֲדֹנִי אַבְרָהָם› the-eved speaks a demand — LET:
# make-chesed(the-LORD, if-adoni-avraham)
m.declare("ha_eved", "LET",
          "aseh_chesed(YHWH, im_adoni_avraham)")

# -------------------------- Gen.24.13 · THE_STANDING_AT_THE_SPRING ---------
# הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב עַל־עֵ֣ין הַמָּ֑יִם וּבְנוֹת֙ אַנְשֵׁ֣י הָעִ֔יר
# יֹצְאֹ֖ת לִשְׁאֹ֥ב מָֽיִם
# "[EN-AID] Behold, I am standing by the spring of water, and the daughters
# of the men of the city are coming out to draw water."
m.step("Gen.24.13")
# ‹אָנֹכִי נִצָּב … יֹצְאֹת לִשְׁאֹב› fact holds: anokhi-nitzav-upon-en-the-
# waters; daughters-yotzot-to-me-sheov
m.fact("anokhi_nitzav_al_en_ha_mayim",
       "banot_yotzot_li_sheov")

# -------------------------- Gen.24.14 · THE_DESIGNED_SIGN ------------------
# וְהָיָ֣ה הַֽנַּעֲרָ֗ אֲשֶׁ֨ר אֹמַ֤ר אֵלֶ֨יהָ֙ הַטִּי־נָ֤א כַדֵּךְ֙
# וְאֶשְׁתֶּ֔ה וְאָמְרָ֣ה שְׁתֵ֔ה וְגַם־גְּמַלֶּ֖יךָ אַשְׁקֶ֑ה אֹתָ֤הּ
# הֹכַ֨חְתָּ֙ לְעַבְדְּךָ֣ לְיִצְחָ֔ק וּבָ֣הּ אֵדַ֔ע כִּי־עָשִׂ֥יתָ חֶ֖סֶד
# עִם־אֲדֹנִֽי
# "[EN-AID] And let it be the girl to whom I say, Tip your pitcher please
# that I may drink, and she says, Drink, and I will also water your camels —
# her You have appointed for Your servant, for Isaac; and by her I shall
# know that You have done kindness with my master."
m.step("Gen.24.14")
# ‹הַטִּי־נָא … שְׁתֵה … אַשְׁקֶה› fact holds: designed-sign-oracle
m.fact("designed_sign_oracle")
# ‹אֹתָהּ הֹכַחְתָּ לְעַבְדְּךָ לְיִצְחָק› fact holds: hokhachta-
# appointment-criterion
m.fact("hokhachta_appointment_criterion")

# -------------------------- Gen.24.15 · RIVQAH_APPEARS ---------------------
# וַֽיְהִי־ה֗וּא טֶרֶם֮ כִּלָּ֣ה לְדַבֵּר֒ וְהִנֵּ֧ה רִבְקָ֣ה יֹצֵ֗את
# אֲשֶׁ֤ר יֻלְּדָה֙ לִבְתוּאֵ֣ל בֶּן־מִלְכָּ֔ה אֵ֥שֶׁת נָח֖וֹר אֲחִ֣י
# אַבְרָהָ֑ם וְכַדָּ֖הּ עַל־שִׁכְמָֽהּ
# "[EN-AID] And it was, before he had finished speaking, that behold Rivqah
# was coming out — who was born to Betuel son of Milcah, wife of Nahor
# brother of Abraham — and her pitcher on her shoulder."
m.step("Gen.24.15")
# ‹וַיְהִי … טֶרֶם כִּלָּה לְדַבֵּר וְהִנֵּה רִבְקָה יֹצֵאת› event: appear —
# theme rivqah
m.event("appear", themes=["rivqah"])
# ‹רִבְקָה› the world gains: rivqah
m.install("rivqah")

# -------------------------- Gen.24.16 · THE_GIRL_ATTRIBUTE_AND_THE_WELL_ACT -
# וְהַֽנַּעֲרָ֗ טֹבַ֤ת מַרְאֶה֙ מְאֹ֔ד בְּתוּלָ֕ה וְאִ֖ישׁ לֹ֣א יְדָעָ֑הּ
# וַתֵּ֣רֶד הָעַ֔יְנָה וַתְּמַלֵּ֥א כַדָּ֖הּ וַתָּֽעַל
# "[EN-AID] And the girl was very fair of appearance, a virgin, and no man
# had known her; and she went down to the spring and filled her pitcher and
# came up."
m.step("Gen.24.16")
# ‹טֹבַת מַרְאֶה› fact holds: tovat-appearance-attribute
m.fact("tovat_mareh_attribute")
# ‹וַתֵּרֶד … וַתְּמַלֵּא … וַתָּעַל› event: descend-fill-ascend — agent
# rivqah
m.event("descend_fill_ascend", agent="rivqah")

# -------------------------- Gen.24.17 · THE_LIVE_SIP_DEMAND ----------------
# וַיָּ֥רָץ הָעֶ֖בֶד לִקְרָאתָ֑הּ וַיֹּ֕אמֶר הַגְמִיאִ֥ינִי נָ֛א
# מְעַט־מַ֖יִם מִכַּדֵּֽךְ
# "[EN-AID] And the servant ran to meet her and said: Let me sip, please, a
# little water from your pitcher."
m.step("Gen.24.17")
# ‹וַיָּרָץ … וַיֹּאמֶר› event: run-say — agent the-eved
m.event("run_say", agent="ha_eved")
# ‹הַגְמִיאִינִי נָא› the-eved speaks a demand — LET: hagmiini(rivqah, meat-
# waters)
m.declare("ha_eved", "LET",
          "hagmiini(rivqah, meat_mayim)")

# -------------------------- Gen.24.18 · DRINK_MY_LORD_AND_THE_WATERING -----
# וַתֹּ֖אמֶר שְׁתֵ֣ה אֲדֹנִ֑י וַתְּמַהֵ֗ר וַתֹּ֧רֶד כַּדָּ֛הּ עַל־יָדָ֖הּ
# וַתַּשְׁקֵֽהוּ
# "[EN-AID] And she said: Drink, my lord; and she hurried and lowered her
# pitcher on her hand and gave him drink."
m.step("Gen.24.18")
# ‹שְׁתֵה אֲדֹנִי› rivqah speaks a demand — LET: shete(the-eved)
m.declare("rivqah", "LET",
          "shete(ha_eved)")
# ‹וַתְּמַהֵר … וַתַּשְׁקֵהוּ› event: water — agent rivqah
m.event("water", agent="rivqah")

# -------------------------- Gen.24.19 · THE_OVERPERFORMANCE_PROMISE --------
# וַתְּכַ֖ל לְהַשְׁקֹת֑וֹ וַתֹּ֗אמֶר גַּ֤ם לִגְמַלֶּ֨יךָ֙ אֶשְׁאָ֔ב עַ֥ד
# אִם־כִּלּ֖וּ לִשְׁתֹּֽת
# "[EN-AID] And she finished giving him drink, and said: Also for your
# camels I will draw until they have finished drinking."
m.step("Gen.24.19")
# ‹וַתְּכַל לְהַשְׁקֹתוֹ› event: finish-watering — agent rivqah
m.event("finish_watering", agent="rivqah")
# ‹גַּם לִגְמַלֶּיךָ אֶשְׁאָב› fact holds: promise-eshav-to-me-gemale-kha
m.fact("promise_eshav_li_gemale_kha")

# -------------------------- Gen.24.20 · THE_CAMELS_WATERED -----------------
# וַתְּמַהֵ֗ר וַתְּעַ֤ר כַּדָּהּ֙ אֶל־הַשֹּׁ֔קֶת וַתָּ֥רָץ ע֛וֹד
# אֶֽל־הַבְּאֵ֖ר לִשְׁאֹ֑ב וַתִּשְׁאַ֖ב לְכָל־גְּמַלָּֽיו
# "[EN-AID] And she hurried and emptied her pitcher into the trough and ran
# again to the well to draw, and she drew for all his camels."
m.step("Gen.24.20")
# ‹וַתְּמַהֵר וַתְּעַר … וַתָּרָץ … וַתִּשְׁאַב› event: empty-run-draw —
# agent rivqah; theme all-camels
m.event("empty_run_draw", agent="rivqah", themes=["all_camels"])

# -------------------------- Gen.24.21 · THE_SILENT_GAZE --------------------
# וְהָאִ֥ישׁ מִשְׁתָּאֵ֖ה לָ֑הּ מַחֲרִ֕ישׁ לָדַ֗עַת הַֽהִצְלִ֧יחַ יְהוָ֛ה
# דַּרְכּ֖וֹ אִם־לֹֽא
# "[EN-AID] And the man was gazing at her, keeping silent, to know whether
# YHWH had prospered his way or not."
m.step("Gen.24.21")
# ‹מִשְׁתָּאֵה … מַחֲרִישׁ … הֲהִצְלִיחַ› fact holds: gazing-silent-wonder
m.fact("gazing_silent_wonder")

# -------------------------- Gen.24.22 · THE_GIFTS_OF_GOLD ------------------
# וַיְהִ֗י כַּאֲשֶׁ֨ר כִּלּ֤וּ הַגְּמַלִּים֙ לִשְׁתּ֔וֹת וַיִּקַּ֤ח הָאִישׁ֙
# נֶ֣זֶם זָהָ֔ב בֶּ֖קַע מִשְׁקָל֑וֹ וּשְׁנֵ֤י צְמִידִים֙ עַל־יָדֶ֔יהָ
# עֲשָׂרָ֥ה זָהָ֖ב מִשְׁקָלָֽם
# "[EN-AID] And when the camels had finished drinking, the man took a gold
# nose-ring, a beqa its weight, and two bracelets on her hands, ten of gold
# their weight."
m.step("Gen.24.22")
# ‹וַיִּקַּח … נֶזֶם … צְמִידִים› event: take-gifts — agent the-eved; theme
# nezem-tzamid
m.event("take_gifts", agent="ha_eved", themes=["nezem_tzamid"])

# -------------------------- Gen.24.23 · TELL_ME_WHOSE_DAUGHTER -------------
# וַיֹּ֨אמֶר֙ בַּת־מִ֣י אַ֔תְּ הַגִּ֥ידִי נָ֖א לִ֑י הֲיֵ֧שׁ בֵּית־אָבִ֛יךְ
# מָק֥וֹם לָ֖נוּ לָלִֽין
# "[EN-AID] And he said: Whose daughter are you? Tell me, please. Is there
# in your father's house a place for us to lodge?"
m.step("Gen.24.23")
# ‹וַיֹּאמֶר› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹הַגִּידִי נָא לִי› the-eved speaks a demand — LET: hagidi(rivqah, bat-
# from)
m.declare("ha_eved", "LET",
          "hagidi(rivqah, bat_mi)")

# -------------------------- Gen.24.24 · THE_LINEAGE_ANSWER -----------------
# וַתֹּ֣אמֶר אֵלָ֔יו בַּת־בְּתוּאֵ֖ל אָנֹ֑כִי בֶּן־מִלְכָּ֕ה אֲשֶׁ֥ר
# יָלְדָ֖ה לְנָחֽוֹר
# "[EN-AID] And she said to him: I am the daughter of Betuel, son of Milcah,
# whom she bore to Nahor."
m.step("Gen.24.24")
# ‹וַתֹּאמֶר› event: say — agent rivqah
m.event("say", agent="rivqah")
# ‹בַּת־בְּתוּאֵל … לְנָחוֹר› fact holds: rivqah-bat-betuel-line
m.fact("rivqah_bat_betuel_line")

# -------------------------- Gen.24.25 · STRAW_AND_FODDER_AND_ROOM ----------
# וַתֹּ֣אמֶר אֵלָ֔יו גַּם־תֶּ֥בֶן גַּם־מִסְפּ֖וֹא רַ֣ב עִמָּ֑נוּ
# גַּם־מָק֖וֹם לָלֽוּן
# "[EN-AID] And she said to him: Also straw, also fodder, much with us; also
# a place to lodge."
m.step("Gen.24.25")
# ‹וַתֹּאמֶר› event: say — agent rivqah
m.event("say", agent="rivqah")

# -------------------------- Gen.24.26 · THE_BOW_TO_YHWH --------------------
# וַיִּקֹּ֣ד הָאִ֔ישׁ וַיִּשְׁתַּ֖חוּ לַֽיהוָֽה
# "[EN-AID] And the man bowed the head and prostrated himself to YHWH."
m.step("Gen.24.26")
# ‹וַיִּקֹּד … וַיִּשְׁתַּחוּ לַיהוָה› event: bow-prostrate — agent the-eved
m.event("bow_prostrate", agent="ha_eved")

# -------------------------- Gen.24.27 · BLESSED_BE_YHWH_KINDNESS_AND_TRUTH -
# וַיֹּ֗אמֶר בָּר֤וּךְ יְהוָה֙ אֱלֹהֵי֙ אֲדֹנִ֣י אַבְרָהָ֔ם אֲ֠שֶׁר
# לֹֽא־עָזַ֥ב חַסְדּ֛וֹ וַאֲמִתּ֖וֹ מֵעִ֣ם אֲדֹנִ֑י אָנֹכִ֗י בַּדֶּ֨רֶךְ֙
# נָחַ֣נִי יְהוָ֔ה בֵּ֖ית אֲחֵ֥י אֲדֹנִֽי
# "[EN-AID] And he said: Blessed be YHWH, God of my master Abraham, who has
# not forsaken His kindness and His truth from with my master; I being on
# the way, YHWH led me to the house of my master's brothers."
m.step("Gen.24.27")
# ‹וַיֹּאמֶר› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹בָּרוּךְ יְהוָה … חַסְדּוֹ וַאֲמִתּוֹ› fact holds: barukh-the-LORD-
# chesed-and-emet
m.fact("barukh_YHWH_chesed_ve_emet")

# -------------------------- Gen.24.28 · SHE_RUNS_AND_TELLS -----------------
# וַתָּ֨רָץ֙ הַֽנַּעֲרָ֔ וַתַּגֵּ֖ד לְבֵ֣ית אִמָּ֑הּ כַּדְּבָרִ֖ים הָאֵֽלֶּה
# "[EN-AID] And the girl ran and told her mother's household these things."
m.step("Gen.24.28")
# ‹וַתָּרָץ … וַתַּגֵּד› event: run-tell — agent rivqah
m.event("run_tell", agent="rivqah")

# -------------------------- Gen.24.29 · LABAN_RUNS -------------------------
# וּלְרִבְקָ֥ה אָ֖ח וּשְׁמ֣וֹ לָבָ֑ן וַיָּ֨רָץ לָבָ֧ן אֶל־הָאִ֛ישׁ הַח֖וּצָה
# אֶל־הָעָֽיִן
# "[EN-AID] And Rivqah had a brother, and his name was Laban; and Laban ran
# to the man outside, to the spring."
m.step("Gen.24.29")
# ‹וּשְׁמוֹ לָבָן› the world gains: lavan
m.install("lavan")

# -------------------------- Gen.24.30 · HE_SEES_THE_GIFTS_AND_COMES --------
# וַיְהִ֣י כִּרְאֹ֣ת אֶת־הַנֶּ֗זֶם וְֽאֶת־הַצְּמִדִים֮ עַל־יְדֵ֣י אֲחֹתוֹ֒
# וּכְשָׁמְע֗וֹ אֶת־דִּבְרֵ֞י רִבְקָ֤ה אֲחֹתוֹ֙ לֵאמֹ֔ר כֹּֽה־דִבֶּ֥ר אֵלַ֖י
# הָאִ֑ישׁ וַיָּבֹא֙ אֶל־הָאִ֔ישׁ וְהִנֵּ֛ה עֹמֵ֥ד עַל־הַגְּמַלִּ֖ים
# עַל־הָעָֽיִן
# "[EN-AID] And when he saw the nose-ring and the bracelets on his sister's
# hands, and when he heard the words of Rivqah his sister saying, Thus the
# man spoke to me, he came to the man; and behold, standing by the camels at
# the spring."
m.step("Gen.24.30")
# ‹כִּרְאֹת … וּכְשָׁמְעוֹ … וַיָּבֹא› event: see-hear-come — agent lavan
m.event("see_hear_come", agent="lavan")

# -------------------------- Gen.24.31 · COME_IN_O_BLESSED_OF_YHWH ----------
# וַיֹּ֕אמֶר בּ֖וֹא בְּר֣וּךְ יְהוָ֑ה לָ֤מָּה תַעֲמֹד֙ בַּח֔וּץ וְאָנֹכִי֙
# פִּנִּ֣יתִי הַבַּ֔יִת וּמָק֖וֹם לַגְּמַלִּֽים
# "[EN-AID] And he said: Come in, O blessed of YHWH; why do you stand
# outside? And I have cleared the house, and a place for the camels."
m.step("Gen.24.31")
# ‹בּוֹא› lavan speaks a demand — LET: in-it(the-eved)
m.declare("lavan", "LET",
          "bo(ha_eved)")

# -------------------------- Gen.24.32 · HE_ENTERS_AND_IS_SERVED ------------
# וַיָּבֹ֤א הָאִישׁ֙ הַבַּ֔יְתָה וַיְפַתַּ֖ח הַגְּמַלִּ֑ים וַיִּתֵּ֨ן
# תֶּ֤בֶן וּמִסְפּוֹא֙ לַגְּמַלִּ֔ים וּמַ֨יִם֙ לִרְחֹ֣ץ רַגְלָ֔יו וְרַגְלֵ֥י
# הָאֲנָשִׁ֖ים אֲשֶׁ֥ר אִתּֽוֹ
# "[EN-AID] And the man came to the house and unmuzzled the camels; and he
# gave straw and fodder to the camels, and water to wash his feet and the
# feet of the men who were with him."
m.step("Gen.24.32")
# ‹וַיָּבֹא הָאִישׁ הַבַּיְתָה› demand settled (popped from the queue): in-
# it(the-eved)
m.result("bo(ha_eved)", tmark="t2")
# ‹וַיְפַתַּח … וַיִּתֵּן … לִרְחֹץ› event: serve-camels-and-feet
m.event("serve_camels_and_feet")

# -------------------------- Gen.24.33 · THE_SEAM_SPEAK_DEMAND --------------
# ויישם וַיּוּשַׂ֤ם לְפָנָיו֙ לֶאֱכֹ֔ל וַיֹּ֨אמֶר֙ לֹ֣א אֹכַ֔ל עַ֥ד
# אִם־דִּבַּ֖רְתִּי דְּבָרָ֑י וַיֹּ֖אמֶר דַּבֵּֽר
# "[EN-AID] And food was set before him to eat; and he said: I will not eat
# until I have spoken my words. And he said: Speak."
m.step("Gen.24.33")
# ‹וַיּוּשַׂם … וַיֹּאמֶר לֹא אֹכַל … וַיֹּאמֶר דַּבֵּר› event: food-set
m.event("food_set")
# ‹דַּבֵּר› house-voice speaks a demand — LET: daber(the-eved)
m.declare("house_voice", "LET",
          "daber(ha_eved)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'lavan', 'ha_eved', 'rivqah'}
    assert m.presupposed_set() == {'ir_nachor', 'avraham', 'aram_naharayim', 'YHWH'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hishamer(ha_eved, pen_tashiv_et_beni_shama)', 'haqreh(YHWH, lefanai_hayom)', 'aseh_chesed(YHWH, im_adoni_avraham)', 'hagmiini(rivqah, meat_mayim)', 'shete(ha_eved)', 'hagidi(rivqah, bat_mi)', 'daber(ha_eved)']
    assert len(m.SPECS["log"]) == 9
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['avraham_zaqen_ba_ba_yamim', 'YHWH_berakh_et_avraham_ba_kol', 've_ashbia_kha_ba_YHWH', 'lo_tiqach_isha_li_veni_mi_benot_ha_kenaani', 'telekh_el_artzi_ve_el_moladti', 'laqachta(ha_eved, isha_li_yitzchaq)', 'ulay_lo_tove_ha_isha_la_lekhet', 'question_he_hashev_ashiv', 'past_oath_nishba_li', 'quoted_eten_le_zara_kha', 'yishlach_malakh_o_le_fane_kha', 'laqachta(ha_eved, isha_li_veni_mi_sham)', 'release_if_lo_tove_then_niqita_mi_shevuah', 'raq_et_beni_lo_tashev_shama', 'anokhi_nitzav_al_en_ha_mayim', 'banot_yotzot_li_sheov', 'designed_sign_oracle', 'hokhachta_appointment_criterion', 'tovat_mareh_attribute', 'promise_eshav_li_gemale_kha', 'gazing_silent_wonder', 'rivqah_bat_betuel_line', 'barukh_YHWH_chesed_ve_emet'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 34
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_41_retelling_release_meeting
###############################################################################
# =============================================================================
# gen_41_retelling_release_meeting — 24:34-67
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_41_retelling_release_meeting.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The retelling, the release, and the meeting (24:34-67)"""
from machine import Machine

m = Machine("gen_41_retelling_release_meeting")

# -------------------------- Gen.24.34 · THE_SERVANT_IDENTIFIES -------------
# וַיֹּאמַ֑ר עֶ֥בֶד אַבְרָהָ֖ם אָנֹֽכִי
# "[EN-AID] And he said: I am Abraham's servant."
m.step("Gen.24.34")
# ‹וַיֹּאמַר› event: say — agent the-eved
m.event("say", agent="ha_eved")
# ‹עֶבֶד אַבְרָהָם אָנֹכִי› fact holds: eved-avraham-anokhi
m.fact("eved_avraham_anokhi")
# ‹עֶבֶד אַבְרָהָם› reads without prior install (flag, not fix): the-eved,
# avraham
m.presupposed("ha_eved", "avraham")

# -------------------------- Gen.24.35 · THE_RETELLING_OF_THE_BLESSING ------
# וַיהוָ֞ה בֵּרַ֧ךְ אֶת־אֲדֹנִ֛י מְאֹ֖ד וַיִּגְדָּ֑ל וַיִּתֶּן־ל֞וֹ צֹ֤אן
# וּבָקָר֙ וְכֶ֣סֶף וְזָהָ֔ב וַעֲבָדִם֙ וּשְׁפָחֹ֔ת וּגְמַלִּ֖ים וַחֲמֹרִֽים
# "[EN-AID] And YHWH has blessed my master greatly, and he has become great;
# and He gave him flocks and herds, silver and gold, male and female
# servants, camels and donkeys."
m.step("Gen.24.35")
# ‹יְהוָה בֵּרַךְ אֶת־אֲדֹנִי … וַיִּתֶּן לוֹ› fact holds: the-LORD-berakh-
# adoni-very-and-yigdal-and-yiten-wealth
m.fact("YHWH_berakh_et_adoni_meod_va_yigdal_va_yiten_wealth")

# -------------------------- Gen.24.36 · THE_RETELLING_OF_THE_HEIR ----------
# וַתֵּ֡לֶד שָׂרָה֩ אֵ֨שֶׁת אֲדֹנִ֥י בֵן֙ לַֽאדֹנִ֔י אַחֲרֵ֖י זִקְנָתָ֑הּ
# וַיִּתֶּן־לּ֖וֹ אֶת־כָּל־אֲשֶׁר־לֽוֹ
# "[EN-AID] And Sarah my master's wife bore a son to my master after her old
# age; and he has given him all that he has."
m.step("Gen.24.36")
# ‹וַתֵּלֶד שָׂרָה … בֵן … אַחֲרֵי זִקְנָתָהּ וַיִּתֶּן לוֹ
# אֶת־כָּל־אֲשֶׁר־לוֹ› fact holds: sara-teled-ben-achare-ziqnah-and-gave-all
m.fact("sara_teled_ben_achare_ziqnah_and_gave_all")

# -------------------------- Gen.24.37 · THE_RETELLING_OF_THE_NOT_TAKE ------
# וַיַּשְׁבִּעֵ֥נִי אֲדֹנִ֖י לֵאמֹ֑ר לֹא־תִקַּ֤ח אִשָּׁה֙ לִבְנִ֔י
# מִבְּנוֹת֙ הַֽכְּנַעֲנִ֔י אֲשֶׁ֥ר אָנֹכִ֖י יֹשֵׁ֥ב בְּאַרְצֽוֹ
# "[EN-AID] And my master made me swear, saying: You shall not take a wife
# for my son from the daughters of the Canaanite among whom I dwell."
m.step("Gen.24.37")
# ‹וַיַּשְׁבִּעֵנִי אֲדֹנִי לֵאמֹר› fact holds: and-yashbie-ni-adoni-to-mor
m.fact("va_yashbie_ni_adoni_le_mor")
# ‹לֹא־תִקַּח אִשָּׁה לִבְנִי מִבְּנוֹת הַכְּנַעֲנִי› fact holds: not-
# tiqach-isha-to-me-veni-from-benot-the-kenaani
m.fact("lo_tiqach_isha_li_veni_mi_benot_ha_kenaani")

# -------------------------- Gen.24.38 · THE_RETELLING_OF_THE_GO_AND_TAKE ---
# אִם־לֹ֧א אֶל־בֵּית־אָבִ֛י תֵּלֵ֖ךְ וְאֶל־מִשְׁפַּחְתִּ֑י וְלָקַחְתָּ֥
# אִשָּׁ֖ה לִבְנִֽי
# "[EN-AID] But you shall go to my father's house and to my family, and take
# a wife for my son."
m.step("Gen.24.38")
# ‹אֶל־בֵּית־אָבִי תֵּלֵךְ וְאֶל־מִשְׁפַּחְתִּי› fact holds: telekh-to-bet-
# avi-and-to-mishpachti
m.fact("telekh_el_bet_avi_ve_el_mishpachti")
# ‹וְלָקַחְתָּ אִשָּׁה לִבְנִי› fact holds: and-laqachta-isha-to-me-veni
m.fact("ve_laqachta_isha_li_veni")

# -------------------------- Gen.24.39 · THE_RETELLING_OF_ULAI --------------
# וָאֹמַ֖ר אֶל־אֲדֹנִ֑י אֻלַ֛י לֹא־תֵלֵ֥ךְ הָאִשָּׁ֖ה אַחֲרָֽי
# "[EN-AID] And I said to my master: Perhaps the woman will not follow me."
m.step("Gen.24.39")
# ‹אֻלַי לֹא־תֵלֵךְ הָאִשָּׁה אַחֲרָי› fact holds: ulay-not-telekh-the-isha-
# achara-y-retell
m.fact("ulay_lo_telekh_ha_isha_achara_y_retell")

# -------------------------- Gen.24.40 · THE_RETELLING_OF_THE_ANGEL_PROMISE -
# וַיֹּ֖אמֶר אֵלָ֑י יְהוָ֞ה אֲשֶׁר־הִתְהַלַּ֣כְתִּי לְפָנָ֗יו יִשְׁלַ֨ח
# מַלְאָכ֤וֹ אִתָּךְ֙ וְהִצְלִ֣יחַ דַּרְכֶּ֔ךָ וְלָקַחְתָּ֤ אִשָּׁה֙
# לִבְנִ֔י מִמִּשְׁפַּחְתִּ֖י וּמִבֵּ֥ית אָבִֽי
# "[EN-AID] And he said to me: YHWH, before whom I walk, will send His angel
# with you and prosper your way; and you shall take a wife for my son from
# my family and from my father's house."
m.step("Gen.24.40")
# ‹יְהוָה … יִשְׁלַח מַלְאָכוֹ … וְלָקַחְתָּ אִשָּׁה› fact holds: retold-
# angel-promise-and-take-from-family
m.fact("retold_angel_promise_and_take_from_family")

# -------------------------- Gen.24.41 · THE_ALAH_DELTA_RELEASE -------------
# אָ֤ז תִּנָּקֶה֙ מֵאָ֣לָתִ֔י כִּ֥י תָב֖וֹא אֶל־מִשְׁפַּחְתִּ֑י וְאִם־לֹ֤א
# יִתְּנוּ֙ לָ֔ךְ וְהָיִ֥יתָ נָקִ֖י מֵאָלָתִֽי
# "[EN-AID] Then you shall be free from my imprecation when you come to my
# family; and if they will not give her to you, you shall be free from my
# imprecation."
m.step("Gen.24.41")
# ‹תִּנָּקֶה מֵאָלָתִי … נָקִי מֵאָלָתִי› fact holds: alah-delta-release-
# content
m.fact("alah_delta_release_content")

# -------------------------- Gen.24.42 · THE_RETELLING_OF_ARRIVAL_AND_PRAYER -
# וָאָבֹ֥א הַיּ֖וֹם אֶל־הָעָ֑יִן וָאֹמַ֗ר יְהוָה֙ אֱלֹהֵי֙ אֲדֹנִ֣י
# אַבְרָהָ֔ם אִם־יֶשְׁךָ־נָּא֙ מַצְלִ֣יחַ דַּרְכִּ֔י אֲשֶׁ֥ר אָנֹכִ֖י
# הֹלֵ֥ךְ עָלֶֽיהָ
# "[EN-AID] And I came today to the spring and said: YHWH, God of my master
# Abraham, if You are prospering my way on which I go—"
m.step("Gen.24.42")
# ‹וָאָבֹא … וָאֹמַר … אִם־יֶשְׁךָ נָא מַצְלִיחַ דַּרְכִּי› fact holds:
# retold-arrival-and-prosper-prayer
m.fact("retold_arrival_and_prosper_prayer")

# -------------------------- Gen.24.43 · THE_ALMAH_DELTA_IN_RETELLING -------
# הִנֵּ֛ה אָנֹכִ֥י נִצָּ֖ב עַל־עֵ֣ין הַמָּ֑יִם וְהָיָ֤ה הָֽעַלְמָה֙
# הַיֹּצֵ֣את לִשְׁאֹ֔ב וְאָמַרְתִּ֣י אֵלֶ֔יהָ הַשְׁקִֽינִי־נָ֥א מְעַט־מַ֖יִם
# מִכַּדֵּֽךְ
# "[EN-AID] Behold, I stand by the spring of water; and let it be that the
# maiden who comes out to draw, to whom I say, Please let me drink a little
# water from your jar—"
m.step("Gen.24.43")
# ‹הָעַלְמָה› fact holds: almah-debut-and-naarah-delta
m.fact("almah_debut_and_naarah_delta")
# ‹הַשְׁקִינִי נָא מְעַט מַיִם מִכַּדֵּךְ› fact holds: retold-design-hashqi-
# ni-sign
m.fact("retold_design_hashqi_ni_sign")

# -------------------------- Gen.24.44 · THE_RETELLING_OF_THE_SIGN_ANSWER ---
# וְאָמְרָ֤ה אֵלַי֙ גַּם־אַתָּ֣ה שְׁתֵ֔ה וְגַ֥ם לִגְמַלֶּ֖יךָ אֶשְׁאָ֑ב
# הִ֣וא הָֽאִשָּׁ֔ה אֲשֶׁר־הֹכִ֥יחַ יְהוָ֖ה לְבֶן־אֲדֹנִֽי
# "[EN-AID] and she says to me, Drink, and I will also draw for your camels
# — she is the woman whom YHWH has appointed for my master's son."
m.step("Gen.24.44")
# ‹גַּם־אַתָּה שְׁתֵה … אֶשְׁאָב … הִיא הָאִשָּׁה אֲשֶׁר־הֹכִיחַ יְהוָה›
# fact holds: retold-sign-shete-eshav-and-appoint
m.fact("retold_sign_shete_eshav_and_appoint")

# -------------------------- Gen.24.45 · THE_RETELLING_BEFORE_I_FINISHED ----
# אֲנִי֩ טֶ֨רֶם אֲכַלֶּ֜ה לְדַבֵּ֣ר אֶל־לִבִּ֗י וְהִנֵּ֨ה רִבְקָ֤ה יֹצֵאת֙
# וְכַדָּ֣הּ עַל־שִׁכְמָ֔הּ וַתֵּ֥רֶד הָעַ֖יְנָה וַתִּשְׁאָ֑ב וָאֹמַ֥ר
# אֵלֶ֖יהָ הַשְׁקִ֥ינִי נָֽא
# "[EN-AID] I had not yet finished speaking to my heart, and behold Rivqah
# came out with her jar on her shoulder, went down to the spring and drew;
# and I said to her: Please let me drink."
m.step("Gen.24.45")
# ‹רִבְקָה יֹצֵאת … הַשְׁקִינִי נָא› fact holds: retold-rivqah-arrival-and-
# hashqi-ni
m.fact("retold_rivqah_arrival_and_hashqi_ni")

# -------------------------- Gen.24.46 · THE_RETELLING_OF_THE_DRINK_OFFER ---
# וַתְּמַהֵ֗ר וַתּ֤וֹרֶד כַּדָּהּ֙ מֵֽעָלֶ֔יהָ וַתֹּ֣אמֶר שְׁתֵ֔ה
# וְגַם־גְּמַלֶּ֖יךָ אַשְׁקֶ֑ה וָאֵ֕שְׁתְּ וְגַ֥ם הַגְּמַלִּ֖ים הִשְׁקָֽתָה
# "[EN-AID] And she hurried and lowered her jar and said: Drink, and I will
# also water your camels; and I drank, and she also watered the camels."
m.step("Gen.24.46")
# ‹שְׁתֵה … אַשְׁקֶה … הִשְׁקָתָה› fact holds: retold-shete-and-watering
m.fact("retold_shete_and_watering")

# -------------------------- Gen.24.47 · THE_RETELLING_OF_IDENTITY_AND_GIFTS -
# וָאֶשְׁאַ֣ל אֹתָ֗הּ וָאֹמַר֮ בַּת־מִ֣י אַתְּ֒ וַתֹּ֗אמֶר בַּת־בְּתוּאֵל֙
# בֶּן־נָח֔וֹר אֲשֶׁ֥ר יָֽלְדָה־לּ֖וֹ מִלְכָּ֑ה וָאָשִׂ֤ם הַנֶּ֨זֶם֙
# עַל־אַפָּ֔הּ וְהַצְּמִידִ֖ים עַל־יָדֶֽיהָ
# "[EN-AID] And I asked her: Whose daughter are you? And she said: Daughter
# of Betuel son of Nahor, whom Milcah bore him. And I put the ring on her
# nose and the bracelets on her hands."
m.step("Gen.24.47")
# ‹בַּת־בְּתוּאֵל … וָאָשִׂם הַנֶּזֶם› fact holds: retold-identity-and-gifts
m.fact("retold_identity_and_gifts")

# -------------------------- Gen.24.48 · THE_RETELLING_OF_THE_BOW_AND_CHOICE -
# וָאֶקֹּ֥ד וָֽאֶשְׁתַּחֲוֶ֖ה לַיהוָ֑ה וָאֲבָרֵךְ֙ אֶת־יְהוָ֔ה אֱלֹהֵי֙
# אֲדֹנִ֣י אַבְרָהָ֔ם אֲשֶׁ֤ר הִנְחַ֙נִי֙ בְּדֶ֣רֶךְ אֱמֶ֔ת לָקַ֛חַת
# אֶת־בַּת־אֲחִ֥י אֲדֹנִ֖י לִבְנֽוֹ
# "[EN-AID] And I bowed and prostrated to YHWH and blessed YHWH, God of my
# master Abraham, who led me in the true way to take my master's brother's
# daughter for his son."
m.step("Gen.24.48")
# ‹וָאֶקֹּד וָאֶשְׁתַּחֲוֶה … וָאֲבָרֵךְ … בְּדֶרֶךְ אֱמֶת› fact holds:
# retold-bow-bless-and-true-way
m.fact("retold_bow_bless_and_true_way")

# -------------------------- Gen.24.49 · THE_LIVE_HAGIDU_FENCE_ENDS ---------
# וְעַתָּ֗ה אִם־יֶשְׁכֶ֨ם עֹשִׂ֜ים חֶ֧סֶד וֶֽאֱמֶ֛ת אֶת־אֲדֹנִ֖י הַגִּ֣ידוּ
# לִ֑י וְאִם־לֹ֕א הַגִּ֣ידוּ לִ֔י וְאֶפְנֶ֥ה עַל־יָמִ֖ין א֥וֹ עַל־שְׂמֹֽאל
# "[EN-AID] And now, if you will deal kindly and truly with my master, tell
# me; and if not, tell me, that I may turn to the right or to the left."
m.step("Gen.24.49")
# ‹הַגִּידוּ לִי› the-eved speaks a demand — LET: hagidu(to-me, the-bayit)
m.declare("ha_eved", "LET",
          "hagidu(li, ha_bayit)")
# ‹אִם־יֶשְׁכֶם עֹשִׂים חֶסֶד וֶאֱמֶת› fact holds: if-chesed-and-emet-branch
m.fact("im_chesed_ve_emet_branch")

# -------------------------- Gen.24.50 · THE_FROM_YHWH_VERDICT --------------
# וַיַּ֨עַן לָבָ֤ן וּבְתוּאֵל֙ וַיֹּ֣אמְר֔וּ מֵיְהוָ֖ה יָצָ֣א הַדָּבָ֑ר לֹ֥א
# נוּכַ֛ל דַּבֵּ֥ר אֵלֶ֖יךָ רַ֥ע אוֹ־טֽוֹב
# "[EN-AID] And Laban and Betuel answered and said: The matter has come out
# from YHWH; we cannot speak to you bad or good."
m.step("Gen.24.50")
# ‹וַיַּעַן לָבָן וּבְתוּאֵל וַיֹּאמְרוּ› event: answer
m.event("answer")
# ‹מֵיְהוָה יָצָא הַדָּבָר› fact holds: from-the-LORD-yatza-the-davar
m.fact("me_YHWH_yatza_ha_davar")

# -------------------------- Gen.24.51 · THE_COMPOUND_QACH_VA_LEKH ----------
# הִנֵּֽה־רִבְקָ֥ה לְפָנֶ֖יךָ קַ֣ח וָלֵ֑ךְ וּתְהִ֤י אִשָּׁה֙
# לְבֶן־אֲדֹנֶ֔יךָ כַּאֲשֶׁ֖ר דִּבֶּ֥ר יְהוָֽה
# "[EN-AID] Behold, Rivqah is before you; take and go, and let her be a wife
# to your master's son, as YHWH has spoken."
m.step("Gen.24.51")
# ‹קַח וָלֵךְ› lavan-betuel speaks a demand — LET: qach-and-lekh(rivqah)
m.declare("lavan_betuel", "LET",
          "qach_va_lekh(rivqah)")
# ‹וּתְהִי אִשָּׁה לְבֶן־אֲדֹנֶיךָ› lavan-betuel speaks a demand — LET:
# tehi(rivqah, isha-to-ven-adonekha)
m.declare("lavan_betuel", "LET",
          "tehi(rivqah, isha_le_ven_adonekha)")

# -------------------------- Gen.24.52 · THE_BOW_TO_YHWH --------------------
# וַיְהִ֕י כַּאֲשֶׁ֥ר שָׁמַ֛ע עֶ֥בֶד אַבְרָהָ֖ם אֶת־דִּבְרֵיהֶ֑ם
# וַיִּשְׁתַּ֥חוּ אַ֖רְצָה לַֽיהוָֽה
# "[EN-AID] And when Abraham's servant heard their words, he bowed to the
# ground to YHWH."
m.step("Gen.24.52")
# ‹שָׁמַע … וַיִּשְׁתַּחוּ אַרְצָה לַיהוָה› event: hear-and-bow — agent the-
# eved
m.event("hear_and_bow", agent="ha_eved")

# -------------------------- Gen.24.53 · THE_GIFTS --------------------------
# וַיּוֹצֵ֨א הָעֶ֜בֶד כְּלֵי־כֶ֨סֶף וּכְלֵ֤י זָהָב֙ וּבְגָדִ֔ים וַיִּתֵּ֖ן
# לְרִבְקָ֑ה וּמִ֨גְדָּנֹ֔ת נָתַ֥ן לְאָחִ֖יהָ וּלְאִמָּֽהּ
# "[EN-AID] And the servant brought out vessels of silver and vessels of
# gold and garments and gave to Rivqah; and precious gifts he gave to her
# brother and to her mother."
m.step("Gen.24.53")
# ‹וַיּוֹצֵא … וַיִּתֵּן לְרִבְקָה … מִגְדָּנֹת נָתַן› event: give-gifts —
# agent the-eved; theme kele-and-begadim-and-migdanot
m.event("give_gifts", agent="ha_eved", themes=["kele_u_begadim_u_migdanot"])

# -------------------------- Gen.24.54 · THE_HOSPITALITY_AND_SHALCHUNI ------
# וַיֹּאכְל֣וּ וַיִּשְׁתּ֗וּ ה֛וּא וְהָאֲנָשִׁ֥ים אֲשֶׁר־עִמּ֖וֹ
# וַיָּלִ֑ינוּ וַיָּק֣וּמוּ בַבֹּ֔קֶר וַיֹּ֖אמֶר שַׁלְּחֻ֥נִי לַֽאדֹנִֽי
# "[EN-AID] And they ate and drank, he and the men who were with him, and
# lodged; and they rose in the morning and he said: Send me to my master."
m.step("Gen.24.54")
# ‹וַיֹּאכְלוּ וַיִּשְׁתּוּ … וַיָּלִינוּ› event: eat-drink-lodge — agent
# the-eved-and-anashim
m.event("eat_drink_lodge", agent="ha_eved_u_anashim")
# ‹שַׁלְּחֻנִי לַאדֹנִי› the-eved speaks a demand — LET: shalchuni(the-eved,
# to-adoni)
m.declare("ha_eved", "LET",
          "shalchuni(ha_eved, la_adoni)")

# -------------------------- Gen.24.55 · THE_FAMILY_COUNTER_PROPOSAL --------
# וַיֹּ֤אמֶר אָחִ֨יהָ֙ וְאִמָּ֔הּ תֵּשֵׁ֨ב הַנַּעֲרָ֥ אִתָּ֛נוּ יָמִ֖ים א֣וֹ
# עָשׂ֑וֹר אַחַ֖ר תֵּלֵֽךְ
# "[EN-AID] And her brother and her mother said: Let the young woman stay
# with us days or ten; afterward you may go."
m.step("Gen.24.55")
# ‹תֵּשֵׁב הַנַּעֲרָ אִתָּנוּ יָמִים אוֹ עָשׂוֹר› fact holds: family-
# counter-teshev-seas-o-asor
m.fact("family_counter_teshev_yamim_o_asor")

# -------------------------- Gen.24.56 · THE_AL_TEACHARU_AND_SHALCHUNI_REPEAT -
# וַיֹּ֤אמֶר אֲלֵהֶם֙ אַל־תְּאַחֲר֣וּ אֹתִ֔י וַֽיהוָ֖ה הִצְלִ֣יחַ דַּרְכִּ֑י
# שַׁלְּח֕וּנִי וְאֵלְכָ֖ה לַֽאדֹנִֽי
# "[EN-AID] And he said to them: Do not delay me, since YHWH has made my way
# prosper; send me and I will go to my master."
m.step("Gen.24.56")
# ‹אַל־תְּאַחֲרוּ אֹתִי› the-eved speaks a demand — LET-NOT: upon-
# teacharu(me)
m.declare("ha_eved", "LET-NOT",
          "al_teacharu(oti)")
# ‹שַׁלְּחוּנִי וְאֵלְכָה לַאדֹנִי› fact holds: shalchuni-resound-and-and-
# elkha-purpose
m.fact("shalchuni_resound_and_ve_elkha_purpose")

# -------------------------- Gen.24.57 · THE_CONSENT_QUESTION_NISHALA -------
# וַיֹּאמְר֖וּ נִקְרָ֣א לַֽנַּעֲרָ֑ וְנִשְׁאֲלָ֖ה אֶת־פִּֽיהָ
# "[EN-AID] And they said: Let us call the young woman and ask her mouth."
m.step("Gen.24.57")
# ‹נִקְרָא … וְנִשְׁאֲלָה אֶת־פִּיהָ› the-bayit speaks a demand — CMD-US?:
# nishala(pi-the)
m.declare("ha_bayit", "CMD-US?",
          "nishala(et_pi_ha)")

# -------------------------- Gen.24.58 · THE_ELEKH_CONSENT ------------------
# וַיִּקְרְא֤וּ לְרִבְקָה֙ וַיֹּאמְר֣וּ אֵלֶ֔יהָ הֲתֵלְכִ֖י עִם־הָאִ֣ישׁ
# הַזֶּ֑ה וַתֹּ֖אמֶר אֵלֵֽךְ
# "[EN-AID] And they called Rivqah and said to her: Will you go with this
# man? And she said: I will go."
m.step("Gen.24.58")
# ‹הֲתֵלְכִי … אֵלֵךְ› event: ask-and-consent
m.event("ask_and_consent")

# -------------------------- Gen.24.59 · THE_SEND_POP -----------------------
# וַֽיְשַׁלְּח֛וּ אֶת־רִבְקָ֥ה אֲחֹתָ֖ם וְאֶת־מֵנִקְתָּ֑הּ וְאֶת־עֶ֥בֶד
# אַבְרָהָ֖ם וְאֶת־אֲנָשָֽׁיו
# "[EN-AID] And they sent Rivqah their sister and her nurse and Abraham's
# servant and his men."
m.step("Gen.24.59")
# ‹וַיְשַׁלְּחוּ … עֶבֶד אַבְרָהָם› demand settled (popped from the queue):
# shalchuni(the-eved, to-adoni)
m.result("shalchuni(ha_eved, la_adoni)", tmark="t1")

# -------------------------- Gen.24.60 · THE_HAYI_BLESSING ------------------
# וַיְבָרֲכ֤וּ אֶת־רִבְקָה֙ וַיֹּ֣אמְרוּ לָ֔הּ אֲחֹתֵ֕נוּ אַ֥תְּ הֲיִ֖י
# לְאַלְפֵ֣י רְבָבָ֑ה וְיִירַ֣שׁ זַרְעֵ֔ךְ אֵ֖ת שַׁ֥עַר שֹׂנְאָֽיו
# "[EN-AID] And they blessed Rivqah and said to her: Our sister, be you
# thousands of myriads, and may your seed possess the gate of its haters."
m.step("Gen.24.60")
# ‹הֲיִי לְאַלְפֵי רְבָבָה› the-bayit speaks a demand — LET: hayi(rivqah,
# to-alfe-revava)
m.declare("ha_bayit", "LET",
          "hayi(rivqah, le_alfe_revava)")
# ‹וְיִירַשׁ זַרְעֵךְ אֵת שַׁעַר שֹׂנְאָיו› fact holds: gate-fowl-haters-
# blessing-content
m.fact("gate_of_haters_blessing_content")

# -------------------------- Gen.24.61 · THE_COMPOUND_POP_AND_DEPARTURE -----
# וַתָּ֨קָם רִבְקָ֜ה וְנַעֲרֹתֶ֗יהָ וַתִּרְכַּ֨בְנָה֙ עַל־הַגְּמַלִּ֔ים
# וַתֵּלַ֖כְנָה אַחֲרֵ֣י הָאִ֑ישׁ וַיִּקַּ֥ח הָעֶ֛בֶד אֶת־רִבְקָ֖ה
# וַיֵּלַֽךְ
# "[EN-AID] And Rivqah and her young women rose and rode on the camels and
# went after the man; and the servant took Rivqah and went."
m.step("Gen.24.61")
# ‹וַתָּקָם … וַתֵּלַכְנָה אַחֲרֵי הָאִישׁ› event: ?
m.event("?")
# ‹וַיִּקַּח הָעֶבֶד אֶת־רִבְקָה וַיֵּלַךְ› demand settled (popped from the
# queue): qach-and-lekh(rivqah)
m.result("qach_va_lekh(rivqah)", tmark="t2")

# -------------------------- Gen.24.62 · THE_BEER_LACHAI_ROI_ADDRESS --------
# וְיִצְחָק֙ בָּ֣א מִבּ֔וֹא בְּאֵ֥ר לַחַ֖י רֹאִ֑י וְה֥וּא יוֹשֵׁ֖ב בְּאֶ֥רֶץ
# הַנֶּֽגֶב
# "[EN-AID] And Isaac came from coming to Beer-lachai-roi; and he was
# dwelling in the land of the Negev."
m.step("Gen.24.62")
# ‹בְּאֵר לַחַי רֹאִי› fact holds: yitzchaq-address-beer-lachai-roi
m.fact("yitzchaq_address_beer_lachai_roi")

# -------------------------- Gen.24.63 · THE_SUACH_HAPAX_AND_CAMELS ---------
# וַיֵּצֵ֥א יִצְחָ֛ק לָשׂ֥וּחַ בַּשָּׂדֶ֖ה לִפְנ֣וֹת עָ֑רֶב וַיִּשָּׂ֤א
# עֵינָיו֙ וַיַּ֔רְא וְהִנֵּ֥ה גְמַלִּ֖ים בָּאִֽים
# "[EN-AID] And Isaac went out to meditate in the field toward evening; and
# he lifted his eyes and saw, and behold, camels were coming."
m.step("Gen.24.63")
# ‹לָשׂוּחַ … וְהִנֵּה גְמַלִּים בָּאִים› event: meditate-and-see-camels —
# agent yitzchaq
m.event("meditate_and_see_camels", agent="yitzchaq")

# -------------------------- Gen.24.64 · THE_RIVQAH_SEES_ISAAC --------------
# וַתִּשָּׂ֤א רִבְקָה֙ אֶת־עֵינֶ֔יהָ וַתֵּ֖רֶא אֶת־יִצְחָ֑ק וַתִּפֹּ֖ל
# מֵעַ֥ל הַגָּמָֽל
# "[EN-AID] And Rivqah lifted her eyes and saw Isaac, and she fell from upon
# the camel."
m.step("Gen.24.64")
# ‹וַתֵּרֶא אֶת־יִצְחָק וַתִּפֹּל מֵעַל הַגָּמָל› event: see-and-dismount —
# agent rivqah; theme yitzchaq
m.event("see_and_dismount", agent="rivqah", themes=["yitzchaq"])

# -------------------------- Gen.24.65 · THE_TZAIF_VEIL ---------------------
# וַתֹּ֣אמֶר אֶל־הָעֶ֗בֶד מִֽי־הָאִ֤ישׁ הַלָּזֶה֙ הַהֹלֵ֤ךְ בַּשָּׂדֶה֙
# לִקְרָאתֵ֔נוּ וַיֹּ֥אמֶר הָעֶ֖בֶד ה֣וּא אֲדֹנִ֑י וַתִּקַּ֥ח הַצָּעִ֖יף
# וַתִּתְכָּֽס
# "[EN-AID] And she said to the servant: Who is that man walking in the
# field to meet us? And the servant said: He is my master. And she took the
# veil and covered herself."
m.step("Gen.24.65")
# ‹ה֣וּא אֲדֹנִי … הַצָּעִיף וַתִּתְכָּס› event: identify-and-veil
m.event("identify_and_veil")

# -------------------------- Gen.24.66 · THE_SERVANT_RECOUNTS ---------------
# וַיְסַפֵּ֥ר הָעֶ֖בֶד לְיִצְחָ֑ק אֵ֥ת כָּל־הַדְּבָרִ֖ים אֲשֶׁ֥ר עָשָֽׂה
# "[EN-AID] And the servant recounted to Isaac all the things that he had
# done."
m.step("Gen.24.66")
# ‹וַיְסַפֵּר … כָּל־הַדְּבָרִים אֲשֶׁר עָשָׂה› event: recount — agent the-
# eved
m.event("recount", agent="ha_eved")

# -------------------------- Gen.24.67 · THE_WIFE_LOVE_AND_COMFORT ----------
# וַיְבִאֶ֣הָ יִצְחָ֗ק הָאֹ֨הֱלָה֙ שָׂרָ֣ה אִמּ֔וֹ וַיִּקַּ֧ח אֶת־רִבְקָ֛ה
# וַתְּהִי־ל֥וֹ לְאִשָּׁ֖ה וַיֶּאֱהָבֶ֑הָ וַיִּנָּחֵ֥ם יִצְחָ֖ק אַחֲרֵ֥י
# אִמּֽוֹ
# "[EN-AID] And Isaac brought her into the tent of Sarah his mother; and he
# took Rivqah and she became his wife, and he loved her; and Isaac was
# comforted after his mother."
m.step("Gen.24.67")
# ‹וַיְבִאֶהָ יִצְחָק הָאֹהֱלָה שָׂרָה אִמּוֹ› event: ?
m.event("?")
# ‹וַיִּקַּח אֶת־רִבְקָה וַתְּהִי־לוֹ לְאִשָּׁה› demand settled (popped from
# the queue): tehi(rivqah, isha-to-ven-adonekha)
m.result("tehi(rivqah, isha_le_ven_adonekha)", tmark="t3")
# ‹וַיֶּאֱהָבֶהָ … וַיִּנָּחֵם יִצְחָק אַחֲרֵי אִמּוֹ› event: ?
m.event("?")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'ha_eved', 'avraham'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['hagidu(li, ha_bayit)', 'al_teacharu(oti)', 'nishala(et_pi_ha)', 'hayi(rivqah, le_alfe_revava)']
    assert len(m.SPECS["log"]) == 7
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['eved_avraham_anokhi', 'YHWH_berakh_et_adoni_meod_va_yigdal_va_yiten_wealth', 'sara_teled_ben_achare_ziqnah_and_gave_all', 'va_yashbie_ni_adoni_le_mor', 'lo_tiqach_isha_li_veni_mi_benot_ha_kenaani', 'telekh_el_bet_avi_ve_el_mishpachti', 've_laqachta_isha_li_veni', 'ulay_lo_telekh_ha_isha_achara_y_retell', 'retold_angel_promise_and_take_from_family', 'alah_delta_release_content', 'retold_arrival_and_prosper_prayer', 'almah_debut_and_naarah_delta', 'retold_design_hashqi_ni_sign', 'retold_sign_shete_eshav_and_appoint', 'retold_rivqah_arrival_and_hashqi_ni', 'retold_shete_and_watering', 'retold_identity_and_gifts', 'retold_bow_bless_and_true_way', 'im_chesed_ve_emet_branch', 'me_YHWH_yatza_ha_davar', 'family_counter_teshev_yamim_o_asor', 'shalchuni_resound_and_ve_elkha_purpose', 'gate_of_haters_blessing_content', 'yitzchaq_address_beer_lachai_roi'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_42_abraham_end_ishmael_line
###############################################################################
# =============================================================================
# gen_42_abraham_end_ishmael_line — 25:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_42_abraham_end_ishmael_line.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Abraham's end and Ishmael's line (25:1-18)"""
from machine import Machine

m = Machine("gen_42_abraham_end_ishmael_line")

# -------------------------- Gen.25.1 · THE_KETURAH_REPORT_NAME -------------
# וַיֹּ֧סֶף אַבְרָהָ֛ם וַיִּקַּ֥ח אִשָּׁ֖ה וּשְׁמָ֥הּ קְטוּרָֽה
# "[EN-AID] And Abraham again took a wife, and her name was Keturah."
m.step("Gen.25.1")
# ‹וַיֹּסֶף … וַיִּקַּח אִשָּׁה› event: take-wife — agent avraham; theme
# qetura
m.event("take_wife", agent="avraham", themes=["qetura"])
# ‹וּשְׁמָהּ קְטוּרָה› fact holds: report-name-qetura
m.fact("report_name_qetura")

# -------------------------- Gen.25.2 · THE_KETURAH_SIX_SONS ----------------
# וַתֵּ֣לֶד ל֗וֹ אֶת־זִמְרָן֙ וְאֶת־יָקְשָׁ֔ן וְאֶת־מְדָ֖ן וְאֶת־מִדְיָ֑ן
# וְאֶת־יִשְׁבָּ֖ק וְאֶת־שֽׁוּחַ
# "[EN-AID] And she bore him Zimran and Jokshan and Medan and Midian and
# Ishbak and Shuah."
m.step("Gen.25.2")
# ‹וַתֵּלֶד לוֹ› event: bear-sons — agent qetura
m.event("bear_sons", agent="qetura")
# ‹זִמְרָן … יָקְשָׁן … מְדָן … מִדְיָן … יִשְׁבָּק … שׁוּחַ› fact holds:
# named-only-roster-zimran-yaqshan-medan-midyan-yishbaq-shucha
m.fact("named_only_roster_zimran_yaqshan_medan_midyan_yishbaq_shucha")

# -------------------------- Gen.25.3 · THE_JOKSHAN_LINE --------------------
# וְיָקְשָׁ֣ן יָלַ֔ד אֶת־שְׁבָ֖א וְאֶת־דְּדָ֑ן וּבְנֵ֣י דְדָ֔ן הָי֛וּ
# אַשּׁוּרִ֥ם וּלְטוּשִׁ֖ים וּלְאֻמִּֽים
# "[EN-AID] And Jokshan begot Sheba and Dedan; and the sons of Dedan were
# Asshurim and Letushim and Leummim."
m.step("Gen.25.3")
# ‹שְׁבָא … דְּדָן … אַשּׁוּרִם וּלְטוּשִׁים וּלְאֻמִּים› fact holds: named-
# only-roster-yaqshan-line
m.fact("named_only_roster_yaqshan_line")

# -------------------------- Gen.25.4 · THE_MIDIAN_LINE_AND_CLOSE -----------
# וּבְנֵ֣י מִדְיָ֗ן עֵיפָ֤ה וָעֵ֨פֶר֙ וַחֲנֹ֔ךְ וַאֲבִידָ֖ע וְאֶלְדָּעָ֑ה
# כָּל־אֵ֖לֶּה בְּנֵ֥י קְטוּרָֽה
# "[EN-AID] And the sons of Midian: Ephah and Epher and Hanoch and Abida and
# Eldaah. All these were the sons of Keturah."
m.step("Gen.25.4")
# ‹עֵיפָה … עֵפֶר … חֲנוֹךְ … אֲבִידָע … אֶלְדָּעָה … בְּנֵי קְטוּרָה› fact
# holds: named-only-roster-midyan-line-and-close
m.fact("named_only_roster_midyan_line_and_close")

# -------------------------- Gen.25.5 · THE_HEIR_GIFT_TO_ISAAC --------------
# וַיִּתֵּ֧ן אַבְרָהָ֛ם אֶת־כָּל־אֲשֶׁר־ל֖וֹ לְיִצְחָֽק
# "[EN-AID] And Abraham gave all that he had to Isaac."
m.step("Gen.25.5")
# ‹וַיִּתֵּן אַבְרָהָם אֶת־כָּל־אֲשֶׁר־לוֹ לְיִצְחָק› event: give-all —
# agent avraham
m.event("give_all", agent="avraham")

# -------------------------- Gen.25.6 · THE_PILEGESH_GIFTS_AND_SEND_EAST ----
# וְלִבְנֵ֤י הַפִּֽילַגְשִׁים֙ אֲשֶׁ֣ר לְאַבְרָהָ֔ם נָתַ֥ן אַבְרָהָ֖ם
# מַתָּנֹ֑ת וַֽיְשַׁלְּחֵ֞ם מֵעַ֨ל יִצְחָ֤ק בְּנוֹ֙ בְּעוֹדֶ֣נּוּ חַ֔י
# קֵ֖דְמָה אֶל־אֶ֥רֶץ קֶֽדֶם
# "[EN-AID] And to the sons of the concubines that Abraham had, Abraham gave
# gifts; and he sent them away from Isaac his son, while he yet lived,
# eastward, to the land of the East."
m.step("Gen.25.6")
# ‹נָתַן … מַתָּנֹת וַיְשַׁלְּחֵם … קֵדְמָה› event: gift-and-send-east —
# agent avraham; theme bene-the-pilagshim
m.event("gift_and_send_east", agent="avraham", themes=["bene_ha_pilagshim"])

# -------------------------- Gen.25.7 · THE_YEARS_OF_ABRAHAM ----------------
# וְאֵ֗לֶּה יְמֵ֛י שְׁנֵֽי־חַיֵּ֥י אַבְרָהָ֖ם אֲשֶׁר־חָ֑י מְאַ֥ת שָׁנָ֛ה
# וְשִׁבְעִ֥ים שָׁנָ֖ה וְחָמֵ֥שׁ שָׁנִֽים
# "[EN-AID] And these are the days of the years of Abraham's life which he
# lived: a hundred years and seventy years and five years."
m.step("Gen.25.7")
# ‹מְאַת שָׁנָה וְשִׁבְעִים שָׁנָה וְחָמֵשׁ שָׁנִים› fact holds: avraham-
# lived-175-years
m.fact("avraham_lived_175_years")

# -------------------------- Gen.25.8 · THE_SEVAH_TOVAH_LANDING -------------
# וַיִּגְוַ֨ע וַיָּ֧מָת אַבְרָהָ֛ם בְּשֵׂיבָ֥ה טוֹבָ֖ה זָקֵ֣ן וְשָׂבֵ֑עַ
# וַיֵּאָ֖סֶף אֶל־עַמָּֽיו
# "[EN-AID] And Abraham expired and died in a good old age, old and full,
# and was gathered to his peoples."
m.step("Gen.25.8")
# ‹וַיִּגְוַע וַיָּמָת … וַיֵּאָסֶף אֶל־עַמָּיו› event: expire-die-gather
m.event("expire_die_gather")
# ‹בְּשֵׂיבָה טוֹבָה› fact holds: sevah-tovah-promise-landing-from-15-15
m.fact("sevah_tovah_promise_landing_from_15_15")

# -------------------------- Gen.25.9 · THE_SONS_BURY_AT_MACHPELAH ----------
# וַיִּקְבְּר֨וּ אֹת֜וֹ יִצְחָ֤ק וְיִשְׁמָעֵאל֙ בָּנָ֔יו אֶל־מְעָרַ֖ת
# הַמַּכְפֵּלָ֑ה אֶל־שְׂדֵ֞ה עֶפְרֹ֤ן בֶּן־צֹ֨חַר֙ הַֽחִתִּ֔י אֲשֶׁ֖ר
# עַל־פְּנֵ֥י מַמְרֵֽא
# "[EN-AID] And Isaac and Ishmael his sons buried him in the cave of
# Machpelah, in the field of Efron son of Zohar the Hittite, which is before
# Mamre."
m.step("Gen.25.9")
# ‹וַיִּקְבְּרוּ אֹתוֹ יִצְחָק וְיִשְׁמָעֵאל … מְעָרַת הַמַּכְפֵּלָה› event:
# bury — theme avraham
m.event("bury", themes=["avraham"])

# -------------------------- Gen.25.10 · THE_FIELD_PURCHASE_RECAP -----------
# הַשָּׂדֶ֛ה אֲשֶׁר־קָנָ֥ה אַבְרָהָ֖ם מֵאֵ֣ת בְּנֵי־חֵ֑ת שָׁ֛מָּה קֻבַּ֥ר
# אַבְרָהָ֖ם וְשָׂרָ֥ה אִשְׁתּֽוֹ
# "[EN-AID] The field that Abraham bought from the sons of Chet — there
# Abraham was buried, and Sarah his wife."
m.step("Gen.25.10")
# ‹הַשָּׂדֶה אֲשֶׁר־קָנָה אַבְרָהָם מֵאֵת בְּנֵי־חֵת› fact holds: field-
# bought-from-bene-chet-burial-place
m.fact("field_bought_from_bene_chet_burial_place")

# -------------------------- Gen.25.11 · THE_BLESSING_AND_BEER_LACHAI_ROI_CLOSE -
# וַיְהִ֗י אַחֲרֵי֙ מ֣וֹת אַבְרָהָ֔ם וַיְבָ֥רֶךְ אֱלֹהִ֖ים אֶת־יִצְחָ֣ק
# בְּנ֑וֹ וַיֵּ֣שֶׁב יִצְחָ֔ק עִם־בְּאֵ֥ר לַחַ֖י רֹאִֽי
# "[EN-AID] And after the death of Abraham, God blessed Isaac his son; and
# Isaac dwelt with Beer-lachai-roi."
m.step("Gen.25.11")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־יִצְחָק בְּנוֹ› event: ?
m.event("?")
# ‹בְּאֵר לַחַי רֹאִי› fact holds: yitzchaq-dwells-beer-lachai-roi-career-
# close
m.fact("yitzchaq_dwells_beer_lachai_roi_career_close")

# -------------------------- Gen.25.12 · THE_TOLEDOT_OF_ISHMAEL -------------
# וְאֵ֛לֶּה תֹּלְדֹ֥ת יִשְׁמָעֵ֖אל בֶּן־אַבְרָהָ֑ם אֲשֶׁ֨ר יָלְדָ֜ה הָגָ֧ר
# הַמִּצְרִ֛ית שִׁפְחַ֥ת שָׂרָ֖ה לְאַבְרָהָֽם
# "[EN-AID] And these are the generations of Ishmael, Abraham's son, whom
# Hagar the Egyptian, Sarah's maid, bore to Abraham."
m.step("Gen.25.12")
# ‹תֹּלְדֹת יִשְׁמָעֵאל› fact holds: generations-yishmael-section-header
m.fact("toledot_yishmael_section_header")

# -------------------------- Gen.25.13 · THE_ISHMAEL_NAMES_A ----------------
# וְאֵ֗לֶּה שְׁמוֹת֙ בְּנֵ֣י יִשְׁמָעֵ֔אל בִּשְׁמֹתָ֖ם לְתוֹלְדֹתָ֑ם בְּכֹ֤ר
# יִשְׁמָעֵאל֙ נְבָיֹ֔ת וְקֵדָ֥ר וְאַדְבְּאֵ֖ל וּמִבְשָֽׂם
# "[EN-AID] And these are the names of the sons of Ishmael, by their names,
# according to their generations: the firstborn of Ishmael, Nevayot; and
# Qedar and Adbeel and Mibsam."
m.step("Gen.25.13")
# ‹נְבָיוֹת וְקֵדָר וְאַדְבְּאֵל וּמִבְשָׂם› fact holds: named-only-roster-
# ishmael-sons-a
m.fact("named_only_roster_ishmael_sons_a")

# -------------------------- Gen.25.14 · THE_ISHMAEL_NAMES_B ----------------
# וּמִשְׁמָ֥ע וְדוּמָ֖ה וּמַשָּֽׂא
# "[EN-AID] and Mishma and Duma and Masa."
m.step("Gen.25.14")
# ‹מִשְׁמָע וְדוּמָה וּמַשָּׂא› fact holds: named-only-roster-ishmael-sons-b
m.fact("named_only_roster_ishmael_sons_b")

# -------------------------- Gen.25.15 · THE_ISHMAEL_NAMES_C ----------------
# חֲדַ֣ד וְתֵימָ֔א יְט֥וּר נָפִ֖ישׁ וָקֵֽדְמָה
# "[EN-AID] Chadad and Tema, Yetur, Nafish, and Qedma."
m.step("Gen.25.15")
# ‹חֲדַד וְתֵימָא יְטוּר נָפִישׁ וָקֵדְמָה› fact holds: named-only-roster-
# ishmael-sons-c
m.fact("named_only_roster_ishmael_sons_c")

# -------------------------- Gen.25.16 · THE_TWELVE_PRINCES_PAY -------------
# אֵ֣לֶּה הֵ֞ם בְּנֵ֤י יִשְׁמָעֵאל֙ וְאֵ֣לֶּה שְׁמֹתָ֔ם בְּחַצְרֵיהֶ֖ם
# וּבְטִֽירֹתָ֑ם שְׁנֵים־עָשָׂ֥ר נְשִׂיאִ֖ם לְאֻמֹּתָֽם
# "[EN-AID] These are the sons of Ishmael and these are their names, by
# their villages and by their encampments: twelve princes according to their
# nations."
m.step("Gen.25.16")
# ‹שְׁנֵים־עָשָׂר נְשִׂיאִים› fact holds: shneim-asar-nesiim-promise-
# landing-from-17-20
m.fact("shneim_asar_nesiim_promise_landing_from_17_20")

# -------------------------- Gen.25.17 · THE_ISHMAEL_DEATH_TRIAD ------------
# וְאֵ֗לֶּה שְׁנֵי֙ חַיֵּ֣י יִשְׁמָעֵ֔אל מְאַ֥ת שָׁנָ֛ה וּשְׁלֹשִׁ֥ים
# שָׁנָ֖ה וְשֶׁ֣בַע שָׁנִ֑ים וַיִּגְוַ֣ע וַיָּ֔מָת וַיֵּאָ֖סֶף אֶל־עַמָּֽיו
# "[EN-AID] And these are the years of the life of Ishmael: a hundred years
# and thirty years and seven years; and he expired and died and was gathered
# to his peoples."
m.step("Gen.25.17")
# ‹וַיִּגְוַע וַיָּמָת וַיֵּאָסֶף אֶל־עַמָּיו› event: expire-die-gather
m.event("expire_die_gather")

# -------------------------- Gen.25.18 · THE_NAFAL_YISHKON_ECHO_AND_SEAM ----
# וַיִּשְׁכְּנ֨וּ מֵֽחֲוִילָ֜ה עַד־שׁ֗וּר אֲשֶׁר֙ עַל־פְּנֵ֣י מִצְרַ֔יִם
# בֹּאֲכָ֖ה אַשּׁ֑וּרָה עַל־פְּנֵ֥י כָל־אֶחָ֖יו נָפָֽל
# "[EN-AID] And they dwelt from Chavila to Shur, which is before Egypt as
# you go toward Ashur; before all his brothers he fell."
m.step("Gen.25.18")
# ‹וַיִּשְׁכְּנוּ מֵחֲוִילָה עַד־שׁוּר› event: ?
m.event("?")
# ‹עַל־פְּנֵי כָל־אֶחָיו נָפָל› fact holds: nafal-before-brothers-echo-
# fowl-16-12-yishkon
m.fact("nafal_before_brothers_echo_of_16_12_yishkon")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['report_name_qetura', 'named_only_roster_zimran_yaqshan_medan_midyan_yishbaq_shucha', 'named_only_roster_yaqshan_line', 'named_only_roster_midyan_line_and_close', 'avraham_lived_175_years', 'sevah_tovah_promise_landing_from_15_15', 'field_bought_from_bene_chet_burial_place', 'yitzchaq_dwells_beer_lachai_roi_career_close', 'toledot_yishmael_section_header', 'named_only_roster_ishmael_sons_a', 'named_only_roster_ishmael_sons_b', 'named_only_roster_ishmael_sons_c', 'shneim_asar_nesiim_promise_landing_from_17_20', 'nafal_before_brothers_echo_of_16_12_yishkon'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_43_isaac_twins_birthright
###############################################################################
# =============================================================================
# gen_43_isaac_twins_birthright — 25:19-34
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_43_isaac_twins_birthright.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Isaac's toledot: twins and the birthright (25:19-34)"""
from machine import Machine

m = Machine("gen_43_isaac_twins_birthright")

# -------------------------- Gen.25.19 · THE_TOLEDOT_OF_ISAAC ---------------
# וְאֵ֛לֶּה תּוֹלְדֹ֥ת יִצְחָ֖ק בֶּן־אַבְרָהָ֑ם אַבְרָהָ֖ם הוֹלִ֥יד
# אֶת־יִצְחָֽק
# "[EN-AID] And these are the generations of Isaac, Abraham's son: Abraham
# begot Isaac."
m.step("Gen.25.19")
# ‹תּוֹלְדֹת יִצְחָק› fact holds: generations-yitzchaq-section-header
m.fact("toledot_yitzchaq_section_header")

# -------------------------- Gen.25.20 · THE_MARRIAGE_AGE_AND_ORIGIN --------
# וַיְהִ֤י יִצְחָק֙ בֶּן־אַרְבָּעִ֣ים שָׁנָ֔ה בְּקַחְתּ֣וֹ אֶת־רִבְקָ֗ה
# בַּת־בְּתוּאֵל֙ הָֽאֲרַמִּ֔י מִפַּדַּ֖ן אֲרָ֑ם אֲח֛וֹת לָבָ֥ן הָאֲרַמִּ֖י
# ל֥וֹ לְאִשָּֽׁה
# "[EN-AID] And Isaac was forty years old when he took Rivqah, daughter of
# Betuel the Aramean of Padan-aram, sister of Laban the Aramean, as wife for
# himself."
m.step("Gen.25.20")
# ‹בֶּן־אַרְבָּעִים שָׁנָה … רִבְקָה … מִפַּדַּן אֲרָם› fact holds:
# yitzchaq-forty-takes-rivqa-from-padan-aram
m.fact("yitzchaq_forty_takes_rivqa_from_padan_aram")

# -------------------------- Gen.25.21 · THE_ENTREAT_PAIR -------------------
# וַיֶּעְתַּ֨ר יִצְחָ֤ק לַֽיהוָה֙ לְנֹ֣כַח אִשְׁתּ֔וֹ כִּ֥י עֲקָרָ֖ה הִ֑וא
# וַיֵּעָ֤תֶר לוֹ֙ יְהוָ֔ה וַתַּ֖הַר רִבְקָ֥ה אִשְׁתּֽוֹ
# "[EN-AID] And Isaac entreated YHWH opposite his wife, for she was barren;
# and YHWH was entreated of him, and Rivqah his wife conceived."
m.step("Gen.25.21")
# ‹וַיֶּעְתַּר … וַיֵּעָתֶר … וַתַּהַר› event: entreat-and-in-entreated —
# theme isht-o
m.event("entreat_and_be_entreated", themes=["isht-o"])

# -------------------------- Gen.25.22 · THE_STRUGGLE_AND_INQUIRE -----------
# וַיִּתְרֹֽצֲצ֤וּ הַבָּנִים֙ בְּקִרְבָּ֔הּ וַתֹּ֣אמֶר אִם־כֵּ֔ן לָ֥מָּה
# זֶּ֖ה אָנֹ֑כִי וַתֵּ֖לֶךְ לִדְרֹ֥שׁ אֶת־יְהוָֽה
# "[EN-AID] And the children struggled together within her; and she said: If
# it be so, why am I thus? And she went to inquire of YHWH."
m.step("Gen.25.22")
# ‹וַיִּתְרֹצֲצוּ … לִדְרֹשׁ אֶת־יְהוָה› event: struggle-and-inquire
m.event("struggle_and_inquire")

# -------------------------- Gen.25.23 · THE_ORACLE_DECREE_FACTS ------------
# וַיֹּ֨אמֶר יְהוָ֜ה לָ֗הּ שְׁנֵ֤י גיים גוֹיִם֙ בְּבִטְנֵ֔ךְ וּשְׁנֵ֣י
# לְאֻמִּ֔ים מִמֵּעַ֖יִךְ יִפָּרֵ֑דוּ וּלְאֹם֙ מִלְאֹ֣ם יֶֽאֱמָ֔ץ וְרַ֖ב
# יַעֲבֹ֥ד צָעִֽיר
# "[EN-AID] And YHWH said to her: Two nations are in your womb, and two
# peoples shall be separated from your bowels; and one people shall be
# stronger than the other people; and the elder shall serve the younger."
m.step("Gen.25.23")
# ‹שְׁנֵי גוֹיִם … וְרַב יַעֲבֹד צָעִיר› fact holds: oracle-two-nations-
# elder-serves-younger
m.fact("oracle_two_nations_elder_serves_younger")

# -------------------------- Gen.25.24 · THE_TWINS_IN_THE_WOMB --------------
# וַיִּמְלְא֥וּ יָמֶ֖יהָ לָלֶ֑דֶת וְהִנֵּ֥ה תוֹמִ֖ם בְּבִטְנָֽהּ
# "[EN-AID] And her days to give birth were filled; and behold, twins were
# in her womb."
m.step("Gen.25.24")
# ‹תוֹמִם בְּבִטְנָהּ› event: birth-due — theme tomim
m.event("birth_due", themes=["tomim"])

# -------------------------- Gen.25.25 · THE_ESAV_NAMING --------------------
# וַיֵּצֵ֤א הָרִאשׁוֹן֙ אַדְמוֹנִ֔י כֻּלּ֖וֹ כְּאַדֶּ֣רֶת שֵׂעָ֑ר
# וַיִּקְרְא֥וּ שְׁמ֖וֹ עֵשָֽׂו
# "[EN-AID] And the first came out reddish, all of him like a hairy mantle;
# and they called his name Esau."
m.step("Gen.25.25")
# ‹וַיֵּצֵא הָרִאשׁוֹן אַדְמוֹנִי … כְּאַדֶּרֶת שֵׂעָר› event: birth-first —
# theme the-rishon
m.event("birth_first", themes=["ha_rishon"])
# ‹וַיִּקְרְאוּ שְׁמוֹ עֵשָׂו› named: esav := esav
m.name("esav", "esav")

# -------------------------- Gen.25.26 · THE_YAAQOV_NAMING ------------------
# וְאַֽחֲרֵי־כֵ֞ן יָצָ֣א אָחִ֗יו וְיָד֤וֹ אֹחֶ֨זֶת֙ בַּעֲקֵ֣ב עֵשָׂ֔ו
# וַיִּקְרָ֥א שְׁמ֖וֹ יַעֲקֹ֑ב וְיִצְחָ֛ק בֶּן־שִׁשִּׁ֥ים שָׁנָ֖ה בְּלֶ֥דֶת
# אֹתָֽם
# "[EN-AID] And after that his brother came out, and his hand was holding
# Esau's heel; and he called his name Jacob; and Isaac was sixty years old
# when she bore them."
m.step("Gen.25.26")
# ‹יָדוֹ אֹחֶזֶת בַּעֲקֵב עֵשָׂו› event: birth-second-heel — theme my-
# brother-v
m.event("birth_second_heel", themes=["achi_v"])
# ‹וַיִּקְרָא שְׁמוֹ יַעֲקֹב› named: yaaqov := yaaqov
m.name("yaaqov", "yaaqov")

# -------------------------- Gen.25.27 · THE_TWO_MEN_GROW -------------------
# וַֽיִּגְדְּלוּ֙ הַנְּעָרִ֔ים וַיְהִ֣י עֵשָׂ֗ו אִ֛ישׁ יֹדֵ֥עַ צַ֖יִד אִ֣ישׁ
# שָׂדֶ֑ה וְיַעֲקֹב֙ אִ֣ישׁ תָּ֔ם יֹשֵׁ֖ב אֹהָלִֽים
# "[EN-AID] And the boys grew; and Esau was a man knowing hunting, a man of
# the field; and Jacob was a complete man, dwelling in tents."
m.step("Gen.25.27")
# ‹עֵשָׂו אִישׁ יֹדֵעַ צַיִד … יַעֲקֹב אִישׁ תָּם› fact holds: esav-hunter-
# yaaqov-man-tam
m.fact("esav_hunter_yaaqov_ish_tam")

# -------------------------- Gen.25.28 · THE_SPLIT_LOVES --------------------
# וַיֶּאֱהַ֥ב יִצְחָ֛ק אֶת־עֵשָׂ֖ו כִּי־צַ֣יִד בְּפִ֑יו וְרִבְקָ֖ה אֹהֶ֥בֶת
# אֶֽת־יַעֲקֹֽב
# "[EN-AID] And Isaac loved Esau because game was in his mouth; and Rivqah
# loved Jacob."
m.step("Gen.25.28")
# ‹וַיֶּאֱהַב יִצְחָק אֶת־עֵשָׂו … וְרִבְקָה אֹהֶבֶת אֶת־יַעֲקֹב› event:
# love-split
m.event("love_split")

# -------------------------- Gen.25.29 · THE_STEW_AND_THE_WEARY -------------
# וַיָּ֥זֶד יַעֲקֹ֖ב נָזִ֑יד וַיָּבֹ֥א עֵשָׂ֛ו מִן־הַשָּׂדֶ֖ה וְה֥וּא עָיֵֽף
# "[EN-AID] And Jacob boiled stew; and Esau came in from the field, and he
# was weary."
m.step("Gen.25.29")
# ‹וַיָּזֶד … נָזִיד … עָיֵף› event: stew-and-arrive
m.event("stew_and_arrive")

# -------------------------- Gen.25.30 · THE_HALITENI_AND_EDOM_REPORT -------
# וַיֹּ֨אמֶר עֵשָׂ֜ו אֶֽל־יַעֲקֹ֗ב הַלְעִיטֵ֤נִי נָא֙ מִן־הָאָדֹ֤ם הָאָדֹם֙
# הַזֶּ֔ה כִּ֥י עָיֵ֖ף אָנֹ֑כִי עַל־כֵּ֥ן קָרָֽא־שְׁמ֖וֹ אֱדֽוֹם
# "[EN-AID] And Esau said to Jacob: Let me gulp, please, from this red, this
# red, for I am weary; therefore his name was called Edom."
m.step("Gen.25.30")
# ‹הַלְעִיטֵנִי נָא› esav speaks a demand — LET: haliteni(from-the-adom)
m.declare("esav", "LET",
          "haliteni(min_ha_adom)")
# ‹עַל־כֵּן קָרָא־שְׁמוֹ אֱדוֹם› fact holds: upon-ken-qara-shemo-edom-
# report-only
m.fact("al_ken_qara_shemo_edom_report_only")

# -------------------------- Gen.25.31 · THE_MIKHRA_PUSH --------------------
# וַיֹּ֖אמֶר יַעֲקֹ֑ב מִכְרָ֥ה כַיּ֛וֹם אֶת־בְּכֹֽרָתְךָ֖ לִֽי
# "[EN-AID] And Jacob said: Sell me as of today your birthright."
m.step("Gen.25.31")
# ‹מִכְרָה כַיּוֹם אֶת־בְּכֹרָתְךָ לִי› yaaqov speaks a demand — LET:
# mikhra(bekhorat-kha, like-day)
m.declare("yaaqov", "LET",
          "mikhra(bekhorat_kha, ka_yom)")

# -------------------------- Gen.25.32 · THE_DISMISS_SPEECH -----------------
# וַיֹּ֣אמֶר עֵשָׂ֔ו הִנֵּ֛ה אָנֹכִ֥י הוֹלֵ֖ךְ לָמ֑וּת וְלָמָּה־זֶּ֥ה לִ֖י
# בְּכֹרָֽה
# "[EN-AID] And Esau said: Behold, I am going to die; and what is this
# birthright to me?"
m.step("Gen.25.32")
# ‹וְלָמָּה־זֶּה לִי בְּכֹרָה› fact holds: esav-dismisses-bekhora-speech
m.fact("esav_dismisses_bekhora_speech")

# -------------------------- Gen.25.33 · THE_DOUBLE_POP_SWEAR_AND_SELL ------
# וַיֹּ֣אמֶר יַעֲקֹ֗ב הִשָּׁ֤בְעָה לִּי֙ כַּיּ֔וֹם וַיִּשָּׁבַ֖ע ל֑וֹ
# וַיִּמְכֹּ֥ר אֶת־בְּכֹרָת֖וֹ לְיַעֲקֹֽב
# "[EN-AID] And Jacob said: Swear to me as of today; and he swore to him;
# and he sold his birthright to Jacob."
m.step("Gen.25.33")
# ‹הִשָּׁבְעָה לִי כַּיּוֹם› yaaqov speaks a demand — LET: hishava(to-me,
# like-day)
m.declare("yaaqov", "LET",
          "hishava(li, ka_yom)")
# ‹וַיִּשָּׁבַע לוֹ› demand settled (popped from the queue): hishava(to-me,
# like-day)
m.result("hishava(li, ka_yom)", tmark="t1")
# ‹וַיִּמְכֹּר אֶת־בְּכֹרָתוֹ לְיַעֲקֹב› demand settled (popped from the
# queue): mikhra(bekhorat-kha, like-day)
m.result("mikhra(bekhorat_kha, ka_yom)", tmark="t2")

# -------------------------- Gen.25.34 · THE_MEAL_AND_THE_DESPISE -----------
# וְיַעֲקֹ֞ב נָתַ֣ן לְעֵשָׂ֗ו לֶ֚חֶם וּנְזִ֣יד עֲדָשִׁ֔ים וַיֹּ֣אכַל
# וַיֵּ֔שְׁתְּ וַיָּ֖קָם וַיֵּלַ֑ךְ וַיִּ֥בֶז עֵשָׂ֖ו אֶת־הַבְּכֹרָֽה
# "[EN-AID] And Jacob gave Esau bread and lentil stew; and he ate and drank
# and rose and went; and Esau despised the birthright."
m.step("Gen.25.34")
# ‹וַיֹּאכַל וַיֵּשְׁתְּ וַיָּקָם וַיֵּלַךְ› event: ?
m.event("?")
# ‹וַיִּבֶז עֵשָׂו אֶת־הַבְּכֹרָה› event: ?
m.event("?")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'esav': 'esav', 'yaaqov': 'yaaqov'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == []
    assert m.open_demands() == ['haliteni(min_ha_adom)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['toledot_yitzchaq_section_header', 'yitzchaq_forty_takes_rivqa_from_padan_aram', 'oracle_two_nations_elder_serves_younger', 'esav_hunter_yaaqov_ish_tam', 'al_ken_qara_shemo_edom_report_only', 'esav_dismisses_bekhora_speech'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 16
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_44_isaac_gerar_sister_expel
###############################################################################
# =============================================================================
# gen_44_isaac_gerar_sister_expel — 26:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_44_isaac_gerar_sister_expel.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Isaac in Gerar — sister-claim, decree, hundredfold, expulsion seam (26:1-16)"""
from machine import Machine

m = Machine("gen_44_isaac_gerar_sister_expel")

# -------------------------- Gen.26.1 · THE_FAMINE_ECHO_AND_THE_PATH_TO_GERAR -
# וַיְהִ֤י רָעָב֙ בָּאָ֔רֶץ מִלְּבַד֙ הָרָעָ֣ב הָרִאשׁ֔וֹן אֲשֶׁ֥ר הָיָ֖ה
# בִּימֵ֣י אַבְרָהָ֑ם וַיֵּ֧לֶךְ יִצְחָ֛ק אֶל־אֲבִימֶּ֥לֶךְ
# מֶֽלֶךְ־פְּלִשְׁתִּ֖ים גְּרָֽרָה
# "[EN-AID] And there was a famine in the land, besides the first famine
# that was in the days of Abraham; and Isaac went to Abimelech king of the
# Philistines, to Gerar."
m.step("Gen.26.1")
# ‹וַיְהִי רָעָב בָּאָרֶץ› event: famine
m.event("famine")
# ‹מִלְּבַד הָרָעָב הָרִאשׁוֹן אֲשֶׁר הָיָה בִּימֵי אַבְרָהָם› fact holds:
# echo-first-famine-days-fowl-avraham
m.fact("echo_first_famine_days_of_avraham")
# ‹וַיֵּלֶךְ יִצְחָק אֶל־אֲבִימֶּלֶךְ … גְּרָרָה› event: go — agent yitzchaq
m.event("go", agent="yitzchaq")
# ‹יִצְחָק … אַבְרָהָם … אֲבִימֶּלֶךְ … גְּרָרָה› reads without prior
# install (flag, not fix): yitzchaq, avraham, avimelekh, gerar, pelishtim
m.presupposed("yitzchaq", "avraham", "avimelekh", "gerar", "pelishtim")

# -------------------------- Gen.26.2 · THE_APPEARANCE_THE_LET_NOT_AND_THE_DWELL -
# וַיֵּרָ֤א אֵלָי֙ו יְהוָ֔ה וַיֹּ֖אמֶר אַל־תֵּרֵ֣ד מִצְרָ֑יְמָה שְׁכֹ֣ן
# בָּאָ֔רֶץ אֲשֶׁ֖ר אֹמַ֥ר אֵלֶֽיךָ
# "[EN-AID] And YHWH appeared to him and said: Do not go down to Egypt;
# dwell in the land that I say to you."
m.step("Gen.26.2")
# ‹וַיֵּרָא אֵלָיו יְהוָה וַיֹּאמֶר› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹אַל־תֵּרֵד מִצְרָיְמָה› the-LORD speaks a demand — LET-NOT: upon-
# tered(yitzchaq, mitzrayim)
m.declare("YHWH", "LET-NOT",
          "al_tered(yitzchaq, mitzrayim)")
# ‹שְׁכֹן בָּאָרֶץ אֲשֶׁר אֹמַר אֵלֶיךָ› the-LORD speaks a demand — LET:
# shekhon(yitzchaq, in-the-earth-which-omar-to-you)
m.declare("YHWH", "LET",
          "shekhon(yitzchaq, ba_aretz_asher_omar_elekha)")

# -------------------------- Gen.26.3 · THE_SOJOURN_THE_PROMISE_AND_THE_PAST_OATH -
# גּ֚וּר בָּאָ֣רֶץ הַזֹּ֔את וְאֶֽהְיֶ֥ה עִמְּךָ֖ וַאֲבָרְכֶ֑ךָּ כִּֽי־לְךָ֣
# וּֽלְזַרְעֲךָ֗ אֶתֵּן֙ אֶת־כָּל־הָֽאֲרָצֹ֣ת הָאֵ֔ל וַהֲקִֽמֹתִי֙
# אֶת־הַשְּׁבֻעָ֔ה אֲשֶׁ֥ר נִשְׁבַּ֖עְתִּי לְאַבְרָהָ֥ם אָבִֽיךָ
# "[EN-AID] Sojourn in this land, and I will be with you and will bless you;
# for to you and to your seed I will give all these lands, and I will
# establish the oath that I swore to Abraham your father."
m.step("Gen.26.3")
# ‹גּוּר בָּאָרֶץ הַזֹּאת› the-LORD speaks a demand — LET: gur(yitzchaq, in-
# the-earth-the-this)
m.declare("YHWH", "LET",
          "gur(yitzchaq, ba_aretz_ha_zot)")
# ‹וְאֶהְיֶה עִמְּךָ וַאֲבָרְכֶךָּ› fact holds: and-ehye-if-kha; and-
# avarkhe-like
m.fact("ve_ehye_im_kha",
       "va_avarkhe_ka")
# ‹כִּי־לְךָ וּלְזַרְעֲךָ אֶתֵּן אֶת־כָּל־הָאֲרָצֹת הָאֵל› fact holds: eten-
# to-kha-and-to-zara-kha-kal-the-aratzot-the-to
m.fact("eten_le_kha_u_le_zara_kha_et_kal_ha_aratzot_ha_el")
# ‹וַהֲקִמֹתִי אֶת־הַשְּׁבֻעָה אֲשֶׁר נִשְׁבַּעְתִּי לְאַבְרָהָם אָבִיךָ›
# fact holds: and-haqimoti-the-shevua; past-oath-nishbati-to-avraham
m.fact("va_haqimoti_et_ha_shevua",
       "past_oath_nishbati_le_avraham")

# -------------------------- Gen.26.4 · THE_SEED_STARS_AND_THE_NATIONS_BLESSING -
# וְהִרְבֵּיתִ֤י אֶֽת־זַרְעֲךָ֙ כְּכוֹכְבֵ֣י הַשָּׁמַ֔יִם וְנָתַתִּ֣י
# לְזַרְעֲךָ֔ אֵ֥ת כָּל־הָאֲרָצֹ֖ת הָאֵ֑ל וְהִתְבָּרֲכ֣וּ בְזַרְעֲךָ֔ כֹּ֖ל
# גּוֹיֵ֥י הָאָֽרֶץ
# "[EN-AID] And I will multiply your seed as the stars of the heavens, and I
# will give to your seed all these lands; and in your seed all nations of
# the earth shall bless themselves."
m.step("Gen.26.4")
# ‹וְהִרְבֵּיתִי … וְנָתַתִּי לְזַרְעֲךָ אֵת כָּל־הָאֲרָצֹת הָאֵל› fact
# holds: and-hirbeti-zara-kha-like-khokhve-the-heavens; and-natati-to-zara-
# kha-the-aratzot
m.fact("ve_hirbeti_zara_kha_ke_khokhve_ha_shamayim",
       "ve_natati_le_zara_kha_ha_aratzot")
# ‹וְהִתְבָּרֲכוּ בְזַרְעֲךָ כֹּל גּוֹיֵי הָאָרֶץ› fact holds: and-
# hitbarakhu-and-zara-kha-all-goye-the-earth
m.fact("ve_hitbarakhu_ve_zara_kha_kol_goye_ha_aretz")

# -------------------------- Gen.26.5 · THE_GROUNDS_BECAUSE_ABRAHAM_LISTENED -
# עֵ֕קֶב אֲשֶׁר־שָׁמַ֥ע אַבְרָהָ֖ם בְּקֹלִ֑י וַיִּשְׁמֹר֙ מִשְׁמַרְתִּ֔י
# מִצְוֺתַ֖י חֻקּוֹתַ֥י וְתוֹרֹתָֽי
# "[EN-AID] because Abraham listened to My voice and kept My charge, My
# commandments, My statutes, and My teachings."
m.step("Gen.26.5")
# ‹עֵקֶב אֲשֶׁר־שָׁמַע אַבְרָהָם בְּקֹלִי› fact holds: eqev-which-shama-
# avraham-in-qoli
m.fact("eqev_asher_shama_avraham_be_qoli")
# ‹וַיִּשְׁמֹר מִשְׁמַרְתִּי מִצְוֺתַי חֻקּוֹתַי וְתוֹרֹתָי› fact holds:
# and-yishmor-mishmarti-mitzvotai-chuqqotai-and-torotai
m.fact("va_yishmor_mishmarti_mitzvotai_chuqqotai_ve_torotai")

# -------------------------- Gen.26.6 · THE_DWELL_OTHER_VERB_CENTERPIECE ----
# וַיֵּ֥שֶׁב יִצְחָ֖ק בִּגְרָֽר
# "[EN-AID] And Isaac dwelt in Gerar."
m.step("Gen.26.6")
# ‹וַיֵּשֶׁב יִצְחָק בִּגְרָר› event: dwell — agent yitzchaq
m.event("dwell", agent="yitzchaq")
# ‹וַיֵּשֶׁב ≠ שְׁכֹן / גּוּר› fact holds: other-verb-non-pop-shekhon-and-
# gur
m.fact("other_verb_non_pop_shekhon_and_gur")

# -------------------------- Gen.26.7 · THE_SISTER_CLAIM_ISAAC_LIVE ---------
# וַֽיִּשְׁאֲל֞וּ אַנְשֵׁ֤י הַמָּקוֹם֙ לְאִשְׁתּ֔וֹ וַיֹּ֖אמֶר אֲחֹ֣תִי
# הִ֑וא כִּ֤י יָרֵא֙ לֵאמֹ֣ר אִשְׁתִּ֔י פֶּן־יַֽהַרְגֻ֜נִי אַנְשֵׁ֤י
# הַמָּקוֹם֙ עַל־רִבְקָ֔ה כִּֽי־טוֹבַ֥ת מַרְאֶ֖ה הִֽיא
# "[EN-AID] And the men of the place asked about his wife; and he said: She
# is my sister — for he feared to say, My wife, lest the men of the place
# kill me on account of Rivqah, for she is good of appearance."
m.step("Gen.26.7")
# ‹וַיִּשְׁאֲלוּ … וַיֹּאמֶר› event: ?
m.event("?")
# ‹אֲחֹתִי הִוא› fact holds: achoti-hi-claim-by-yitzchaq
m.fact("achoti_hi_claim_by_yitzchaq")
# ‹כִּי יָרֵא … כִּי־טוֹבַת מַרְאֶה הִיא› fact holds: yare-to-mor-ishti-
# lest-yahargu; tovat-appearance-hi
m.fact("yare_le_mor_ishti_pen_yahargu",
       "tovat_mareh_hi")

# -------------------------- Gen.26.8 · THE_WINDOW_AND_THE_NAME_ROOT_LAUGH --
# וַיְהִ֗י כִּ֣י אָֽרְכוּ־ל֥וֹ שָׁם֙ הַיָּמִ֔ים וַיַּשְׁקֵ֗ף אֲבִימֶ֨לֶךְ֙
# מֶ֣לֶךְ פְּלִשְׁתִּ֔ים בְּעַ֖ד הַֽחַלּ֑וֹן וַיַּ֗רְא וְהִנֵּ֤ה יִצְחָק֙
# מְצַחֵ֔ק אֵ֖ת רִבְקָ֥ה אִשְׁתּֽוֹ
# "[EN-AID] And it came to pass, when he had been there a long time, that
# Abimelech king of the Philistines looked out through the window and saw,
# and behold, Isaac was laughing/playing with Rivqah his wife."
m.step("Gen.26.8")
# ‹אָרְכוּ … וַיַּשְׁקֵף … וַיַּרְא› event: ?
m.event("?")
# ‹יִצְחָק מְצַחֵק אֵת רִבְקָה אִשְׁתּוֹ› fact holds: yitzchaq-metzacheq-
# rivqah-his-wife
m.fact("yitzchaq_metzacheq_et_rivqah_ishto")

# -------------------------- Gen.26.9 · THE_SUMMONS_AND_THE_RE_QUOTE --------
# וַיִּקְרָ֨א אֲבִימֶ֜לֶךְ לְיִצְחָ֗ק וַיֹּ֨אמֶר֙ אַ֣ךְ הִנֵּ֤ה אִשְׁתְּךָ֙
# הִ֔וא וְאֵ֥יךְ אָמַ֖רְתָּ אֲחֹ֣תִי הִ֑וא וַיֹּ֤אמֶר אֵלָי֙ו יִצְחָ֔ק כִּ֣י
# אָמַ֔רְתִּי פֶּן־אָמ֖וּת עָלֶֽיהָ
# "[EN-AID] And Abimelech called Isaac and said: Behold, of a surety she is
# your wife; and how did you say, She is my sister? And Isaac said to him:
# Because I said, Lest I die because of her."
m.step("Gen.26.9")
# ‹וַיִּקְרָא אֲבִימֶלֶךְ לְיִצְחָק וַיֹּאמֶר … וַיֹּאמֶר אֵלָיו יִצְחָק›
# event: ?
m.event("?")
# ‹הִנֵּה אִשְׁתְּךָ הִוא … אָמַרְתָּ אֲחֹתִי הִוא› fact holds: isht-kha-
# hiv; amarta-achoti-hi-requote
m.fact("isht_kha_hiv",
       "amarta_achoti_hi_requote")

# -------------------------- Gen.26.10 · THE_WHAT_HAVE_YOU_DONE_AND_THE_GUILT_DEBUT -
# וַיֹּ֣אמֶר אֲבִימֶ֔לֶךְ מַה־זֹּ֖את עָשִׂ֣יתָ לָּ֑נוּ כִּ֠מְעַט שָׁכַ֞ב
# אַחַ֤ד הָעָם֙ אֶת־אִשְׁתֶּ֔ךָ וְהֵבֵאתָ֥ עָלֵ֖ינוּ אָשָֽׁם
# "[EN-AID] And Abimelech said: What is this you have done to us? One of the
# people might easily have lain with your wife, and you would have brought
# guilt upon us."
m.step("Gen.26.10")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ› event: say — agent avimelekh
m.event("say", agent="avimelekh")
# ‹מַה־זֹּאת עָשִׂיתָ לָּנוּ› fact holds: ma-this-asita-to-nu
m.fact("ma_zot_asita_la_nu")
# ‹כִּמְעַט שָׁכַב … וְהֵבֵאתָ עָלֵינוּ אָשָׁם› fact holds: near-miss-
# shakhav-and-asham-brought
m.fact("near_miss_shakhav_and_asham_brought")

# -------------------------- Gen.26.11 · THE_ROYAL_DECREE_MOT_YUMAT ---------
# וַיְצַ֣ו אֲבִימֶ֔לֶךְ אֶת־כָּל־הָעָ֖ם לֵאמֹ֑ר הַנֹּגֵ֜עַ בָּאִ֥ישׁ הַזֶּ֛ה
# וּבְאִשְׁתּ֖וֹ מ֥וֹת יוּמָֽת
# "[EN-AID] And Abimelech commanded all the people, saying: He who touches
# this man or his wife shall surely be put to death."
m.step("Gen.26.11")
# ‹וַיְצַו אֲבִימֶלֶךְ אֶת־כָּל־הָעָם› event: command — agent avimelekh
m.event("command", agent="avimelekh")
# ‹הַנֹּגֵעַ בָּאִישׁ הַזֶּה וּבְאִשְׁתּוֹ מוֹת יוּמָת› fact holds: royal-
# decree-no-touch-dying-yumat
m.fact("royal_decree_no_touch_mot_yumat")

# -------------------------- Gen.26.12 · THE_HUNDREDFOLD_AND_THE_BLESSING ---
# וַיִּזְרַ֤ע יִצְחָק֙ בָּאָ֣רֶץ הַהִ֔וא וַיִּמְצָ֛א בַּשָּׁנָ֥ה הַהִ֖וא
# מֵאָ֣ה שְׁעָרִ֑ים וַֽיְבָרֲכֵ֖הוּ יְהוָֽה
# "[EN-AID] And Isaac sowed in that land and found in that year a hundred
# measures; and YHWH blessed him."
m.step("Gen.26.12")
# ‹וַיִּזְרַע … וַיִּמְצָא … מֵאָה שְׁעָרִים› event: sow-and-find — agent
# yitzchaq; theme mea-shearim
m.event("sow_and_find", agent="yitzchaq", themes=["mea_shearim"])
# ‹וַיְבָרֲכֵהוּ יְהוָה› event: ?
m.event("?")

# -------------------------- Gen.26.13 · THE_MAN_GREW_VERY_GREAT ------------
# וַיִּגְדַּ֖ל הָאִ֑ישׁ וַיֵּ֤לֶךְ הָלוֹךְ֙ וְגָדֵ֔ל עַ֥ד כִּֽי־גָדַ֖ל
# מְאֹֽד
# "[EN-AID] And the man became great, and grew more and more until he became
# very great."
m.step("Gen.26.13")
# ‹וַיִּגְדַּל … הָלוֹךְ וְגָדֵל … גָדַל מְאֹד› event: grow-great
m.event("grow_great")

# -------------------------- Gen.26.14 · THE_FLOCKS_AND_THE_ENVY_DEBUT ------
# וַֽיְהִי־ל֤וֹ מִקְנֵה־צֹאן֙ וּמִקְנֵ֣ה בָקָ֔ר וַעֲבֻדָּ֖ה רַבָּ֑ה
# וַיְקַנְא֥וּ אֹת֖וֹ פְּלִשְׁתִּֽים
# "[EN-AID] And he had possessions of flocks and possessions of herds and a
# great household; and the Philistines envied him."
m.step("Gen.26.14")
# ‹מִקְנֵה־צֹאן וּמִקְנֵה בָקָר וַעֲבֻדָּה רַבָּה› fact holds: miqne-tzon-
# vaqar-and-avuda-raba
m.fact("miqne_tzon_vaqar_va_avuda_raba")
# ‹וַיְקַנְאוּ אֹתוֹ פְּלִשְׁתִּים› event: envy — agent pelishtim
m.event("envy", agent="pelishtim")

# -------------------------- Gen.26.15 · THE_STOPPED_WELLS_OF_ABRAHAMS_DAYS -
# וְכָל־הַבְּאֵרֹ֗ת אֲשֶׁ֤ר חָֽפְרוּ֙ עַבְדֵ֣י אָבִ֔יו בִּימֵ֖י אַבְרָהָ֣ם
# אָבִ֑יו סִתְּמ֣וּם פְּלִשְׁתִּ֔ים וַיְמַלְא֖וּם עָפָֽר
# "[EN-AID] And all the wells that his father's servants had dug in the days
# of Abraham his father, the Philistines stopped them up and filled them
# with earth."
m.step("Gen.26.15")
# ‹הַבְּאֵרֹת אֲשֶׁר חָפְרוּ עַבְדֵי אָבִיו בִּימֵי אַבְרָהָם אָבִיו› fact
# holds: wells-dug-by-avde-avraham-bi-yme-avraham
m.fact("wells_dug_by_avde_avraham_bi_yme_avraham")
# ‹סִתְּמוּם פְּלִשְׁתִּים וַיְמַלְאוּם עָפָר› event: stop-up-and-fill —
# agent pelishtim; theme the-beerot
m.event("stop_up_and_fill", agent="pelishtim", themes=["ha_beerot"])

# -------------------------- Gen.26.16 · THE_EXPULSION_SEAM_LEKH ------------
# וַיֹּ֥אמֶר אֲבִימֶ֖לֶךְ אֶל־יִצְחָ֑ק לֵ֚ךְ מֵֽעִמָּ֔נוּ כִּֽי־עָצַֽמְתָּ
# מִמֶּ֖נּוּ מְאֹֽד
# "[EN-AID] And Abimelech said to Isaac: Go from us, for you have become
# much mightier than we."
m.step("Gen.26.16")
# ‹וַיֹּאמֶר אֲבִימֶלֶךְ אֶל־יִצְחָק› event: say — agent avimelekh
m.event("say", agent="avimelekh")
# ‹לֵךְ מֵעִמָּנוּ› avimelekh speaks a demand — LET: lekh(yitzchaq, from-
# imanu)
m.declare("avimelekh", "LET",
          "lekh(yitzchaq, me_imanu)")
# ‹כִּי־עָצַמְתָּ מִמֶּנּוּ מְאֹד› fact holds: atzamta-mime-nu-very
m.fact("atzamta_mime_nu_meod")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'avimelekh', 'pelishtim', 'yitzchaq', 'avraham', 'gerar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['al_tered(yitzchaq, mitzrayim)', 'shekhon(yitzchaq, ba_aretz_asher_omar_elekha)', 'gur(yitzchaq, ba_aretz_ha_zot)', 'lekh(yitzchaq, me_imanu)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['echo_first_famine_days_of_avraham', 've_ehye_im_kha', 'va_avarkhe_ka', 'eten_le_kha_u_le_zara_kha_et_kal_ha_aratzot_ha_el', 'va_haqimoti_et_ha_shevua', 'past_oath_nishbati_le_avraham', 've_hirbeti_zara_kha_ke_khokhve_ha_shamayim', 've_natati_le_zara_kha_ha_aratzot', 've_hitbarakhu_ve_zara_kha_kol_goye_ha_aretz', 'eqev_asher_shama_avraham_be_qoli', 'va_yishmor_mishmarti_mitzvotai_chuqqotai_ve_torotai', 'other_verb_non_pop_shekhon_and_gur', 'achoti_hi_claim_by_yitzchaq', 'yare_le_mor_ishti_pen_yahargu', 'tovat_mareh_hi', 'yitzchaq_metzacheq_et_rivqah_ishto', 'isht_kha_hiv', 'amarta_achoti_hi_requote', 'ma_zot_asita_la_nu', 'near_miss_shakhav_and_asham_brought', 'royal_decree_no_touch_mot_yumat', 'miqne_tzon_vaqar_va_avuda_raba', 'wells_dug_by_avde_avraham_bi_yme_avraham', 'atzamta_mime_nu_meod'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: gen_45_wells_covenant_esau_wives
###############################################################################
# =============================================================================
# gen_45_wells_covenant_esau_wives — 26:17-35
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_45_wells_covenant_esau_wives.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Wells, namings, covenant swear, Shibah, Esau's wives (26:17-35)"""
from machine import Machine

m = Machine("gen_45_wells_covenant_esau_wives")

# -------------------------- Gen.26.17 · THE_LEKH_DEED_ACROSS_THE_WALL ------
# וַיֵּ֥לֶךְ מִשָּׁ֖ם יִצְחָ֑ק וַיִּ֥חַן בְּֽנַחַל־גְּרָ֖ר וַיֵּ֥שֶׁב שָֽׁם
# "[EN-AID] And Isaac went from there and encamped in the wadi of Gerar, and
# dwelt there."
m.step("Gen.26.17")
# ‹וַיֵּלֶךְ מִשָּׁם יִצְחָק› event: ?
m.event("?")
# ‹וַיִּחַן בְּנַחַל־גְּרָר וַיֵּשֶׁב שָׁם› event: ?
m.event("?")
# ‹יִצְחָק … גְּרָר› reads without prior install (flag, not fix): yitzchaq,
# gerar
m.presupposed("yitzchaq", "gerar")

# -------------------------- Gen.26.18 · THE_REDIG_AND_THE_RESTORED_NAMES ---
# וַיָּ֨שָׁב יִצְחָ֜ק וַיַּחְפֹּ֣ר אֶת־בְּאֵרֹ֣ת הַמַּ֗יִם אֲשֶׁ֤ר חָֽפְרוּ֙
# בִּימֵי֙ אַבְרָהָ֣ם אָבִ֔יו וַיְסַתְּמ֣וּם פְּלִשְׁתִּ֔ים אַחֲרֵ֖י מ֣וֹת
# אַבְרָהָ֑ם וַיִּקְרָ֤א לָהֶן֙ שֵׁמ֔וֹת כַּשֵּׁמֹ֕ת אֲשֶׁר־קָרָ֥א לָהֶ֖ן
# אָבִֽיו
# "[EN-AID] And Isaac dug again the wells of water that they had dug in the
# days of Abraham his father, which the Philistines had stopped up after
# Abraham's death; and he called them names like the names his father had
# called them."
m.step("Gen.26.18")
# ‹וַיָּשָׁב … וַיַּחְפֹּר אֶת־בְּאֵרֹת הַמַּיִם› event: redig-wells — agent
# yitzchaq; theme beerot-avraham
m.event("redig_wells", agent="yitzchaq", themes=["beerot_avraham"])
# ‹וַיִּקְרָא לָהֶן שֵׁמוֹת כַּשֵּׁמוֹת אֲשֶׁר־קָרָא לָהֶן אָבִיו› event: ?
m.event("?")

# -------------------------- Gen.26.19 · THE_WELL_OF_LIVING_WATER -----------
# וַיַּחְפְּר֥וּ עַבְדֵֽי־יִצְחָ֖ק בַּנָּ֑חַל וַיִּ֨מְצְאוּ־שָׁ֔ם בְּאֵ֖ר
# מַ֥יִם חַיִּֽים
# "[EN-AID] And Isaac's servants dug in the wadi and found there a well of
# living water."
m.step("Gen.26.19")
# ‹וַיַּחְפְּרוּ … וַיִּמְצְאוּ … בְּאֵר מַיִם חַיִּים› event: dig-and-find
# — agent avde-yitzchaq; theme beer-waters-chayim
m.event("dig_and_find", agent="avde_yitzchaq", themes=["beer_mayim_chayim"])

# -------------------------- Gen.26.20 · THE_QUARREL_AND_THE_NAME_ESEK ------
# וַיָּרִ֜יבוּ רֹעֵ֣י גְרָ֗ר עִם־רֹעֵ֥י יִצְחָ֛ק לֵאמֹ֖ר לָ֣נוּ הַמָּ֑יִם
# וַיִּקְרָ֤א שֵֽׁם־הַבְּאֵר֙ עֵ֔שֶׂק כִּ֥י הִֽתְעַשְּׂק֖וּ עִמּֽוֹ
# "[EN-AID] And the herdsmen of Gerar quarreled with Isaac's herdsmen,
# saying: The water is ours. And he called the name of the well Esek,
# because they contended with him."
m.step("Gen.26.20")
# ‹וַיָּרִיבוּ רֹעֵי גְרָר עִם־רֹעֵי יִצְחָק› event: quarrel — agent roe-
# gerar
m.event("quarrel", agent="roe_gerar")
# ‹וַיִּקְרָא שֵׁם־הַבְּאֵר עֵשֶׂק› named: beer-eseq := eseq
m.name("beer_eseq", "eseq")

# -------------------------- Gen.26.21 · THE_SECOND_WELL_SITNAH -------------
# וַֽיַּחְפְּרוּ֙ בְּאֵ֣ר אַחֶ֔רֶת וַיָּרִ֖יבוּ גַּם־עָלֶ֑יהָ וַיִּקְרָ֥א
# שְׁמָ֖הּ שִׂטְנָֽה
# "[EN-AID] And they dug another well, and they quarreled over it too; and
# he called its name Sitnah."
m.step("Gen.26.21")
# ‹וַיַּחְפְּרוּ בְּאֵר אַחֶרֶת וַיָּרִיבוּ גַּם־עָלֶיהָ› event: dig-and-
# quarrel — theme beer-acheret
m.event("dig_and_quarrel", themes=["beer_acheret"])
# ‹וַיִּקְרָא שְׁמָהּ שִׂטְנָה› named: beer-sitna := sitna
m.name("beer_sitna", "sitna")

# -------------------------- Gen.26.22 · THE_THIRD_WELL_REHOBOTH ------------
# וַיַּעְתֵּ֣ק מִשָּׁ֗ם וַיַּחְפֹּר֙ בְּאֵ֣ר אַחֶ֔רֶת וְלֹ֥א רָב֖וּ עָלֶ֑יהָ
# וַיִּקְרָ֤א שְׁמָהּ֙ רְחֹב֔וֹת וַיֹּ֗אמֶר כִּֽי־עַתָּ֞ה הִרְחִ֧יב יְהוָ֛ה
# לָ֖נוּ וּפָרִ֥ינוּ בָאָֽרֶץ
# "[EN-AID] And he moved from there and dug another well, and they did not
# quarrel over it; and he called its name Rehoboth, and he said: For now
# YHWH has made room for us, and we shall be fruitful in the land."
m.step("Gen.26.22")
# ‹וַיַּעְתֵּק … וַיַּחְפֹּר … וְלֹא רָבוּ› event: move-dig-no-quarrel —
# agent yitzchaq
m.event("move_dig_no_quarrel", agent="yitzchaq")
# ‹וַיִּקְרָא שְׁמָהּ רְחֹבוֹת› named: beer-rechovot := rechovot
m.name("beer_rechovot", "rechovot")
# ‹כִּי־עַתָּה הִרְחִיב יְהוָה לָנוּ וּפָרִינוּ בָאָרֶץ› fact holds:
# hirchiv-the-LORD-to-nu-and-farinu
m.fact("hirchiv_YHWH_la_nu_u_farinu")

# -------------------------- Gen.26.23 · THE_ASCENT_TO_BEER_SHEBA -----------
# וַיַּ֥עַל מִשָּׁ֖ם בְּאֵ֥ר שָֽׁבַע
# "[EN-AID] And he went up from there to Beer-sheba."
m.step("Gen.26.23")
# ‹וַיַּעַל מִשָּׁם בְּאֵר שָׁבַע› event: go-up — agent yitzchaq
m.event("go_up", agent="yitzchaq")

# -------------------------- Gen.26.24 · THE_NIGHT_WORD_AND_AL_TIRA ---------
# וַיֵּרָ֨א אֵלָ֤יו יְהוָה֙ בַּלַּ֣יְלָה הַה֔וּא וַיֹּ֕אמֶר אָנֹכִ֕י
# אֱלֹהֵ֖י אַבְרָהָ֣ם אָבִ֑יךָ אַל־תִּירָא֙ כִּֽי־אִתְּךָ֣ אָנֹ֔כִי
# וּבֵֽרַכְתִּ֨יךָ֙ וְהִרְבֵּיתִ֣י אֶֽת־זַרְעֲךָ֔ בַּעֲב֖וּר אַבְרָהָ֥ם
# עַבְדִּֽי
# "[EN-AID] And YHWH appeared to him that night and said: I am the God of
# Abraham your father; do not fear, for I am with you, and I will bless you
# and multiply your seed for the sake of Abraham My servant."
m.step("Gen.26.24")
# ‹וַיֵּרָא אֵלָיו יְהוָה בַּלַּיְלָה הַהוּא וַיֹּאמֶר› event: appear-night
# — agent the-LORD
m.event("appear_night", agent="YHWH")
# ‹אָנֹכִי אֱלֹהֵי אַבְרָהָם אָבִיךָ› fact holds: anokhi-elohe-avraham-avi-
# kha
m.fact("anokhi_elohe_avraham_avi_kha")
# ‹אַל־תִּירָא› the-LORD speaks a demand — LET-NOT: tira(yitzchaq)
m.declare("YHWH", "LET-NOT",
          "tira(yitzchaq)")
# ‹כִּי־אִתְּךָ אָנֹכִי וּבֵרַכְתִּיךָ וְהִרְבֵּיתִי אֶת־זַרְעֲךָ› fact
# holds: kha-anokhi-and-verakhti-and-hirbeti
m.fact("et_kha_anokhi_u_verakhti_ve_hirbeti")

# -------------------------- Gen.26.25 · THE_ALTAR_INVOCATION_AND_KARAH_DIG -
# וַיִּ֧בֶן שָׁ֣ם מִזְבֵּ֗חַ וַיִּקְרָא֙ בְּשֵׁ֣ם יְהוָ֔ה וַיֶּט־שָׁ֖ם
# אָהֳל֑וֹ וַיִּכְרוּ־שָׁ֥ם עַבְדֵי־יִצְחָ֖ק בְּאֵֽר
# "[EN-AID] And he built an altar there and called on the name of YHWH, and
# pitched his tent there; and Isaac's servants dug a well there."
m.step("Gen.26.25")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ … וַיֶּט שָׁם אָהֳלוֹ› event: ?
m.event("?")
# ‹וַיִּקְרָא בְּשֵׁם יְהוָה› event: ?
m.event("?")
# ‹וַיִּכְרוּ שָׁם עַבְדֵי יִצְחָק בְּאֵר› event: ?
m.event("?")

# -------------------------- Gen.26.26 · THE_VISITORS_FROM_GERAR ------------
# וַאֲבִימֶ֕לֶךְ הָלַ֥ךְ אֵלָ֖יו מִגְּרָ֑ר וַאֲחֻזַּת֙ מֵרֵעֵ֔הוּ וּפִיכֹ֖ל
# שַׂר־צְבָאֽוֹ
# "[EN-AID] And Abimelech went to him from Gerar, with Achuzzath his friend
# and Phichol the commander of his army."
m.step("Gen.26.26")
# ‹וַאֲבִימֶלֶךְ הָלַךְ אֵלָיו מִגְּרָר› event: visit — agent avimelekh
m.event("visit", agent="avimelekh")
# ‹אֲחֻזַּת … פִיכֹל› reads without prior install (flag, not fix): achuzat,
# fikhol, merea
m.presupposed("achuzat", "fikhol", "merea")

# -------------------------- Gen.26.27 · THE_WHY_HAVE_YOU_COME --------------
# וַיֹּ֤אמֶר אֲלֵהֶם֙ יִצְחָ֔ק מַדּ֖וּעַ בָּאתֶ֣ם אֵלָ֑י וְאַתֶּם֙
# שְׂנֵאתֶ֣ם אֹתִ֔י וַתְּשַׁלְּח֖וּנִי מֵאִתְּכֶֽם
# "[EN-AID] And Isaac said to them: Why have you come to me, seeing you hate
# me and have sent me away from you?"
m.step("Gen.26.27")
# ‹וַיֹּאמֶר … מַדּוּעַ בָּאתֶם› event: say — agent yitzchaq
m.event("say", agent="yitzchaq")

# -------------------------- Gen.26.28 · THE_COVENANT_VOLITIVES -------------
# וַיֹּאמְר֗וּ רָא֣וֹ רָאִינוּ֮ כִּֽי־הָיָ֣ה יְהוָ֣ה ׀ עִמָּךְ֒ וַנֹּ֗אמֶר
# תְּהִ֨י נָ֥א אָלָ֛ה בֵּינוֹתֵ֖ינוּ בֵּינֵ֣ינוּ וּבֵינֶ֑ךָ וְנִכְרְתָ֥ה
# בְרִ֖ית עִמָּֽךְ
# "[EN-AID] And they said: We have surely seen that YHWH is with you; and we
# said: Let there be an oath between us, between us and you, and let us cut
# a covenant with you."
m.step("Gen.26.28")
# ‹רָאוֹ רָאִינוּ כִּי־הָיָה יְהוָה עִמָּךְ› fact holds: rao-rainu-the-LORD-
# ima-kha
m.fact("rao_rainu_YHWH_ima_kha")
# ‹תְּהִי נָא אָלָה בֵּינוֹתֵינוּ› avimelekh-party speaks a demand — LET:
# tehi(ala-between-us)
m.declare("avimelekh_party", "LET",
          "tehi(ala_between_us)")
# ‹וְנִכְרְתָה בְרִית עִמָּךְ› avimelekh-party speaks a demand — CMD-US?:
# nikhreta(berit-if-kha)
m.declare("avimelekh_party", "CMD-US?",
          "nikhreta(berit_im_kha)")

# -------------------------- Gen.26.29 · THE_OATH_CONTENT_TERMS -------------
# אִם־תַּעֲשֵׂ֨ה עִמָּ֜נוּ רָעָ֗ה כַּאֲשֶׁר֙ לֹ֣א נְגַֽעֲנ֔וּךָ וְכַאֲשֶׁ֨ר
# עָשִׂ֤ינוּ עִמְּךָ֙ רַק־ט֔וֹב וַנְּשַׁלֵּֽחֲךָ֖ בְּשָׁל֑וֹם אַתָּ֥ה
# עַתָּ֖ה בְּר֥וּךְ יְהוָֽה
# "[EN-AID] that you will do us no harm, as we have not touched you and as
# we have done with you only good and have sent you away in peace; you are
# now the blessed of YHWH."
m.step("Gen.26.29")
# ‹אִם־תַּעֲשֵׂה עִמָּנוּ רָעָה …› fact holds: if-taase-ima-nu-raa-oath-
# content
m.fact("im_taase_ima_nu_raa_oath_content")
# ‹אַתָּה עַתָּה בְּרוּךְ יְהוָה› fact holds: ata-ata-berukh-the-LORD
m.fact("ata_ata_berukh_YHWH")

# -------------------------- Gen.26.30 · THE_FEAST --------------------------
# וַיַּ֤עַשׂ לָהֶם֙ מִשְׁתֶּ֔ה וַיֹּאכְל֖וּ וַיִּשְׁתּֽוּ
# "[EN-AID] And he made them a feast, and they ate and drank."
m.step("Gen.26.30")
# ‹וַיַּעַשׂ … מִשְׁתֶּה וַיֹּאכְלוּ וַיִּשְׁתּוּ› event: feast-eat-drink —
# agent yitzchaq-and-guests
m.event("feast_eat_drink", agent="yitzchaq_and_guests")

# -------------------------- Gen.26.31 · THE_SWEAR_OTHER_VERB_CENTERPIECE ---
# וַיַּשְׁכִּ֣ימוּ בַבֹּ֔קֶר וַיִּשָּׁבְע֖וּ אִ֣ישׁ לְאָחִ֑יו וַיְשַׁלְּחֵ֣ם
# יִצְחָ֔ק וַיֵּלְכ֥וּ מֵאִתּ֖וֹ בְּשָׁלֽוֹם
# "[EN-AID] And they rose early in the morning and swore each to his
# brother; and Isaac sent them away, and they went from him in peace."
m.step("Gen.26.31")
# ‹וַיַּשְׁכִּימוּ … וַיִּשָּׁבְעוּ אִישׁ לְאָחִיו› event: ?
m.event("?")
# ‹וַיִּשָּׁבְעוּ ≠ תְּהִי / נִכְרְתָה› fact holds: other-verb-non-pop-tehi-
# and-nikhreta
m.fact("other_verb_non_pop_tehi_and_nikhreta")
# ‹וַיְשַׁלְּחֵם יִצְחָק וַיֵּלְכוּ … בְּשָׁלוֹם› event: ?
m.event("?")

# -------------------------- Gen.26.32 · THE_WELL_FOUND_REPORT --------------
# וַיְהִ֣י ׀ בַּיּ֣וֹם הַה֗וּא וַיָּבֹ֨אוּ֙ עַבְדֵ֣י יִצְחָ֔ק וַיַּגִּ֣דוּ
# לוֹ֔ עַל־אֹד֥וֹת הַבְּאֵ֖ר אֲשֶׁ֣ר חָפָ֑רוּ וַיֹּ֥אמְרוּ ל֖וֹ מָצָ֥אנוּ
# מָֽיִם
# "[EN-AID] And it came to pass the same day that Isaac's servants came and
# told him about the well that they had dug, and said to him: We have found
# water."
m.step("Gen.26.32")
# ‹וַיַּגִּדוּ … מָצָאנוּ מָיִם› event: report-well-found — agent avde-
# yitzchaq
m.event("report_well_found", agent="avde_yitzchaq")

# -------------------------- Gen.26.33 · THE_NAME_SHIBAH_AND_THE_CITY_ETIOLOGY -
# וַיִּקְרָ֥א אֹתָ֖הּ שִׁבְעָ֑ה עַל־כֵּ֤ן שֵׁם־הָעִיר֙ בְּאֵ֣ר שֶׁ֔בַע עַ֖ד
# הַיּ֥וֹם הַזֶּֽה
# "[EN-AID] And he called it Shibah; therefore the name of the city is Beer-
# sheba to this day."
m.step("Gen.26.33")
# ‹וַיִּקְרָא אֹתָהּ שִׁבְעָה› named: beer-shiva := shiva
m.name("beer_shiva", "shiva")
# ‹עַל־כֵּן שֵׁם הָעִיר בְּאֵר שֶׁבַע עַד הַיּוֹם הַזֶּה› fact holds: upon-
# ken-shem-the-ir-beer-seven
m.fact("al_ken_shem_ha_ir_beer_sheva")

# -------------------------- Gen.26.34 · ESAU_TAKES_TWO_HITTITE_WIVES -------
# וַיְהִ֤י עֵשָׂו֙ בֶּן־אַרְבָּעִ֣ים שָׁנָ֔ה וַיִּקַּ֤ח אִשָּׁה֙
# אֶת־יְהוּדִ֔ית בַּת־בְּאֵרִ֖י הַֽחִתִּ֑י וְאֶת־בָּ֣שְׂמַ֔ת בַּת־אֵילֹ֖ן
# הַֽחִתִּֽי
# "[EN-AID] And when Esau was forty years old he took as wife Judith
# daughter of Beeri the Hittite, and Basemath daughter of Elon the Hittite."
m.step("Gen.26.34")
# ‹עֵשָׂו בֶּן־אַרְבָּעִים שָׁנָה› fact holds: esav-ben-arbaim-shana
m.fact("esav_ben_arbaim_shana")
# ‹וַיִּקַּח אִשָּׁה אֶת־יְהוּדִית … וְאֶת־בָּשְׂמַת› event: take-wives —
# agent esav
m.event("take_wives", agent="esav")
# ‹יְהוּדִית … בָּשְׂמַת … בְּאֵרִי … אֵילוֹן› the world gains: yehudit,
# basmat, beeri, elon
m.install("yehudit", "basmat", "beeri", "elon")

# -------------------------- Gen.26.35 · BITTERNESS_OF_SPIRIT ---------------
# וַתִּהְיֶ֖יןָ מֹ֣רַת ר֑וּחַ לְיִצְחָ֖ק וּלְרִבְקָֽה
# "[EN-AID] And they were a bitterness of spirit to Isaac and to Rivqah."
m.step("Gen.26.35")
# ‹מֹרַת רוּחַ לְיִצְחָק וּלְרִבְקָה› fact holds: morat-spirit-wind-to-
# yitzchaq-and-to-rivqah
m.fact("morat_ruach_le_yitzchaq_u_le_rivqah")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'yehudit', 'elon', 'basmat', 'beeri'}
    assert m.presupposed_set() == {'achuzat', 'gerar', 'merea', 'fikhol', 'yitzchaq'}
    assert m.REGISTRY["names"] == {'beer_eseq': 'eseq', 'beer_sitna': 'sitna', 'beer_rechovot': 'rechovot', 'beer_shiva': 'shiva'}
    assert m.REGISTRY["writes"] == 4
    assert m.tests_list() == []
    assert m.open_demands() == ['tira(yitzchaq)', 'tehi(ala_between_us)', 'nikhreta(berit_im_kha)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5, 'named_before_any_presence': 4}
    assert sorted(m.WORLD["facts"]) == sorted(['hirchiv_YHWH_la_nu_u_farinu', 'anokhi_elohe_avraham_avi_kha', 'et_kha_anokhi_u_verakhti_ve_hirbeti', 'rao_rainu_YHWH_ima_kha', 'im_taase_ima_nu_raa_oath_content', 'ata_ata_berukh_YHWH', 'other_verb_non_pop_tehi_and_nikhreta', 'al_ken_shem_ha_ir_beer_sheva', 'esav_ben_arbaim_shana', 'morat_ruach_le_yitzchaq_u_le_rivqah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 27
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")

###############################################################################
# UNIT: lev_13_intake_quarantine
###############################################################################
# =============================================================================
# lev_13_intake_quarantine — 13:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_intake_quarantine.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The skin-mark intake: case, handlers, quarantine loop (Lev 13:1-8) — first law unit"""
from machine import Machine

m = Machine("lev_13_intake_quarantine")

# -------------------------- Lev.13.1 · FRAME_SPEECH ------------------------
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן לֵאמֹר
# "And the LORD spoke unto Moses and unto Aaron, saying:"
m.step("Lev.13.1")
# ‹וַיְדַבֵּר יְהוָה› event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# reads without prior install (flag, not fix): Moses, Aaron
m.presupposed("moshe", "aharon")

# -------------------------- Lev.13.2 · CASE_INTAKE -------------------------
# אָדָם כִּי־יִהְיֶה בְעוֹר־בְּשָׂרוֹ שְׂאֵת אוֹ־סַפַּחַת אוֹ בַהֶרֶת
# וְהָיָה בְעוֹר־בְּשָׂרוֹ לְנֶגַע צָרָעַת וְהוּבָא אֶל־אַהֲרֹן הַכֹּהֵן אוֹ
# אֶל־אַחַד מִבָּנָיו הַכֹּהֲנִים
# "When a man shall have in the skin of his flesh a rising, or a scab, or a
# bright spot, and it become in the skin of his flesh the plague of leprosy,
# then he shall be brought unto Aaron the priest, or unto one of his sons
# the priests."
m.step("Lev.13.2")
# ‹אָדָם כִּי־יִהְיֶה … וְהוּבָא אֶל־אַהֲרֹן הַכֹּהֵן› case human, mark-in-
# skin-of-flesh(swelling-or-scab-or-bright-spot) -> the-disease-mark routes
# to hova-to-the-priest
m.case("adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat", "hova_el_ha_kohen")
# reads without prior install (flag, not fix): human, skin-of-flesh, the-
# priest
m.presupposed("adam", "or_basar", "ha_kohen")

# -------------------------- Lev.13.3 · HANDLER_VERDICT_TAMEI ---------------
# וְרָאָה הַכֹּהֵן אֶת־הַנֶּגַע בְּעוֹר־הַבָּשָׂר וְשֵׂעָר בַּנֶּגַע הָפַךְ
# לָבָן וּמַרְאֵה הַנֶּגַע עָמֹק מֵעוֹר בְּשָׂרוֹ נֶגַע צָרַעַת הוּא
# וְרָאָהוּ הַכֹּהֵן וְטִמֵּא אֹתוֹ
# "And the priest shall look upon the plague in the skin of the flesh; and
# if the hair in the plague be turned white, and the appearance of the
# plague be deeper than the skin of his flesh, it is the plague of leprosy;
# and the priest shall look on him, and pronounce him unclean."
m.step("Lev.13.3")
# ‹וְשֵׂעָר … הָפַךְ לָבָן וּמַרְאֵה … עָמֹק … וְטִמֵּא אֹתוֹ› standing
# handler — if hair-has-turned-white ∧ appearance-deeper-from-skin-of then
# classify(into-a-mark-of-the-disease-it-is) ∧ he-shall-declare-
# impure(status-impure)
m.handler("sear_hafakh_lavan ∧ mareh_amok_me_or",
          "classify(nega_tzaraat_hu) ∧ timme(status_tamei)")

# -------------------------- Lev.13.4 · HANDLER_CONFINE_FIRST ---------------
# וְאִם־בַּהֶרֶת לְבָנָה הִוא בְּעוֹר בְּשָׂרוֹ וְעָמֹק אֵין־מַרְאֶהָ
# מִן־הָעוֹר וּשְׂעָרָה לֹא־הָפַךְ לָבָן וְהִסְגִּיר הַכֹּהֵן אֶת־הַנֶּגַע
# שִׁבְעַת יָמִים
# "And if the bright spot be white in the skin of his flesh, and the
# appearance thereof be not deeper than the skin, and the hair thereof be
# not turned white, then the priest shall shut up him that hath the plague
# seven days."
m.step("Lev.13.4")
# ‹וְאִם … אֵין … לֹא … וְהִסְגִּיר … שִׁבְעַת יָמִים› standing handler — if
# bright-spot-white ∧ is-not-deeper-its-appearance ∧ not-has-turned-white
# then he-shall-confine(obj-marker-the-into-a-mark-of, seven-of-days)
m.handler("baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan",
          "hisgir(et_ha_nega, shivat_yamim)")

# -------------------------- Lev.13.5 · HANDLER_RECHECK_CONFINE_SECOND ------
# וְרָאָהוּ הַכֹּהֵן בַּיּוֹם הַשְּׁבִיעִי וְהִנֵּה הַנֶּגַע עָמַד
# בְּעֵינָיו לֹא־פָשָׂה הַנֶּגַע בָּעוֹר וְהִסְגִּירוֹ הַכֹּהֵן שִׁבְעַת
# יָמִים שֵׁנִית
# "And the priest shall look on him the seventh day; and, behold, if the
# plague stay in its appearance, and the plague be not spread in the skin,
# then the priest shall shut him up seven days more."
m.step("Lev.13.5")
# ‹בַּיּוֹם הַשְּׁבִיעִי וְהִנֵּה … עָמַד … לֹא־פָשָׂה … שֵׁנִית› standing
# handler — if in-the-day-the-seventh ∧ has-stood-in-its-appearance ∧ not-
# has-spread then he-shall-confine-him(seven-of-days-a-second-time)
m.handler("ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah",
          "hisgiro(shivat_yamim_shenit)")

# -------------------------- Lev.13.6 · HANDLER_RELEASE ---------------------
# וְרָאָה הַכֹּהֵן אֹתוֹ בַּיּוֹם הַשְּׁבִיעִי שֵׁנִית וְהִנֵּה כֵּהָה
# הַנֶּגַע וְלֹא־פָשָׂה הַנֶּגַע בָּעוֹר וְטִהֲרוֹ הַכֹּהֵן מִסְפַּחַת הִיא
# וְכִבֶּס בְּגָדָיו וְטָהֵר
# "And the priest shall look on him again the seventh day; and, behold, if
# the plague be dim, and the plague be not spread in the skin, then the
# priest shall pronounce him clean: it is a scab; and he shall wash his
# clothes, and be clean."
m.step("Lev.13.6")
# ‹כֵּהָה … וְטִהֲרוֹ … מִסְפַּחַת הִיא וְכִבֶּס בְּגָדָיו וְטָהֵר› standing
# handler — if in-the-day-the-seventh-a-second-time ∧ has-dimmed ∧ not-has-
# spread then he-shall-declare-him-pure(status-pure) ∧ classify(scab-it-is)
# ∧ wash-his-garments ∧ he-is-pure
m.handler("ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah",
          "tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher")

# -------------------------- Lev.13.7 · HANDLER_REOPEN_TRIGGER --------------
# וְאִם־פָּשֹׂה תִפְשֶׂה הַמִּסְפַּחַת בָּעוֹר אַחֲרֵי הֵרָאֹתוֹ
# אֶל־הַכֹּהֵן לְטָהֳרָתוֹ וְנִרְאָה שֵׁנִית אֶל־הַכֹּהֵן
# "But if the scab spread abroad in the skin, after that he hath shown
# himself to the priest for his cleansing, he shall show himself to the
# priest again."
m.step("Lev.13.7")
# ‹פָּשֹׂה תִפְשֶׂה … אַחֲרֵי הֵרָאֹתוֹ … וְנִרְאָה שֵׁנִית› standing
# handler — if spread-it-spreads(after-its-appearing-to-his-purification)
# then seen-a-second-time-to-the-priest
m.handler("pasoh_tifseh(acharei_heraoto_le_tohorato)",
          "nirah_shenit_el_ha_kohen")

# -------------------------- Lev.13.8 · HANDLER_REOPEN_VERDICT --------------
# וְרָאָה הַכֹּהֵן וְהִנֵּה פָּשְׂתָה הַמִּסְפַּחַת בָּעוֹר וְטִמְּאוֹ
# הַכֹּהֵן צָרַעַת הִוא
# "And the priest shall look, and, behold, the scab is spread in the skin;
# then the priest shall pronounce him unclean: it is leprosy."
m.step("Lev.13.8")
# ‹וְהִנֵּה פָּשְׂתָה … וְטִמְּאוֹ … צָרַעַת הִוא› standing handler — if
# behold-has-spread-the-scab then pronounce-impure(status-impure) ∧
# classify(the-disease-it-is)
m.handler("hineh_pastah_ha_mispachat",
          "timmeo(status_tamei) ∧ classify(tzaraat_hi)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'or_basar', 'moshe', 'adam', 'aharon', 'ha_kohen'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['case: adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat -> hova_el_ha_kohen', 'handler: IF(sear_hafakh_lavan ∧ mareh_amok_me_or) THEN(classify(nega_tzaraat_hu) ∧ timme(status_tamei))', 'handler: IF(baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan) THEN(hisgir(et_ha_nega, shivat_yamim))', 'handler: IF(ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah) THEN(hisgiro(shivat_yamim_shenit))', 'handler: IF(ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah) THEN(tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher)', 'handler: IF(pasoh_tifseh(acharei_heraoto_le_tohorato)) THEN(nirah_shenit_el_ha_kohen)', 'handler: IF(hineh_pastah_ha_mispachat) THEN(timmeo(status_tamei) ∧ classify(tzaraat_hi))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 8
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
