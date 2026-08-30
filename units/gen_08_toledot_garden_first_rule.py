#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹אֵלֶּה תוֹלְדוֹת הַשָּׁמַיִם וְהָאָרֶץ› (“these generations the-heavens
# and-the-earth”) — section generations: heavens, earth
m.section("toledot", "shamayim", "aretz")
# ‹בְּיוֹם עֲשׂוֹת יְהוָה אֱלֹהִים אֶרֶץ וְשָׁמָיִם› (“in-day making YHWH
# God earth and-heavens”) — clock anchored: t0 := in-the-day-of-[His]-making
m.time_anchor("be_yom_asot")
# reads without prior install (flag, not fix): heavens, earth
m.presupposed("shamayim", "aretz")
# ‹יְהוָה אֱלֹהִים› (“YHWH God”) — spec-delta — spec said God (the week's
# sole agent name, gen-01-07), delivery says the-LORD-God (compound:
# personal name + generic)
m.spec_delta("Elohim (the week's sole agent name, gen_01-07)",
             "YHWH_Elohim (compound: personal name + generic)")
# witness-tier presupposed read: complete_name_over_completed_world on
# yhwh_elohim_debut — read, not installed
m.witness_read("yhwh_elohim_debut", "complete_name_over_completed_world",
                cites=["Bereshit Rabbah 13:3", "Bereshit Rabbah 12:15"])
# witness-tier presupposed read: mortality_class_marker on toledot_header —
# read, not installed
m.witness_read("toledot_header", "mortality_class_marker",
                cites=["Bereshit Rabbah 12:7"])
# witness-grounded state (its own tier): equal_creation_recorded_dispute on
# chiasm_flip_earth_heaven
m.witness_state("chiasm_flip_earth_heaven", "equal_creation_recorded_dispute",
                cites=["Tosefta Keritot 4:7", "Bereshit Rabbah 12:12"])

# -------------------------- Gen.2.5 · PRECONDITIONS_LACKS ------------------
# וְכֹל שִׂיחַ הַשָּׂדֶה טֶרֶם יִהְיֶה בָאָרֶץ וְכָל־עֵשֶׂב הַשָּׂדֶה טֶרֶם
# יִצְמָח כִּי לֹא הִמְטִיר יְהוָה אֱלֹהִים עַל־הָאָרֶץ וְאָדָם אַיִן
# לַעֲבֹד אֶת־הָאֲדָמָה
# "No shrub of the field was yet in the earth, and no herb of the field had
# yet sprung up; for the LORD God had not caused it to rain upon the earth,
# and there was not a man to till the ground."
m.step("Gen.2.5")
# ‹טֶרֶם … טֶרֶם … לֹא הִמְטִיר … וְאָדָם אַיִן› (“not-yet … not-yet … not
# caused-rain … and-human there-is-not”) — fact holds: not-yet(all-shrub-
# the-field); not-yet(all-herb-the-field); had-not-caused-rain(the-LORD-God,
# over-the-earth); no-human-existed(to-work-obj-marker·et-the-ground)
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
# ‹וְאֵד יַעֲלֶה … וְהִשְׁקָה› (“and-mist would-rise … and-would-water”) —
# fact holds: mist-went-up-and-watered(all-face-of-the-ground)
m.fact("ed_yaaleh_ve_hishqah(kol_pnei_ha_adamah)")
# witness-tier presupposed read: superseded_irrigation_regime on ed_mist —
# read, not installed
m.witness_read("ed_mist", "superseded_irrigation_regime",
                cites=["Bereshit Rabbah 13:9", "Mekhilta DeRabbi Yishmael, Tractate Shirah 2:4"])
# witness-tier presupposed read: sukkah_roof_and_niddah_law_source on
# ed_mist — read, not installed
m.witness_read("ed_mist", "sukkah_roof_and_niddah_law_source",
                cites=["Sukkah 11b:14", "Jerusalem Talmud Sukkah 1:5:4", "Jerusalem Talmud Shabbat 2:6:10"])

# -------------------------- Gen.2.7 · FORM_BREATHE_BECOME ------------------
# וַיִּיצֶר יְהוָה אֱלֹהִים אֶת־הָאָדָם עָפָר מִן־הָאֲדָמָה וַיִּפַּח
# בְּאַפָּיו נִשְׁמַת חַיִּים וַיְהִי הָאָדָם לְנֶפֶשׁ חַיָּה
# "Then the LORD God formed man of the dust of the ground, and breathed into
# his nostrils the breath of life; and man became a living soul."
m.step("Gen.2.7")
# ‹וַיִּיצֶר יְהוָה אֱלֹהִים אֶת־הָאָדָם עָפָר מִן־הָאֲדָמָה› (“and-he-
# formed YHWH God obj-marker the-human dust from the-ground”) — event: form
# — agent the-LORD-God; theme human
m.event("form", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיִּפַּח בְּאַפָּיו נִשְׁמַת חַיִּים› (“and-he-breathed in-his-nostrils
# breath-of life”) — event: breathe — agent the-LORD-God; theme breath-of-
# life
m.event("breathe", agent="YHWH_Elohim", themes=["nishmat_chayim"])
# ‹וַיְהִי הָאָדָם לְנֶפֶשׁ חַיָּה› (“and-he-became the-human to-living-
# being living”) — event: become — theme human, living-being
m.event("become", themes=["adam", "nefesh_chaya"])
# ‹הָאָדָם› (“the-human”) — the world gains: human
m.install("adam")
# spec-delta — spec said create/make (create/make — the week's build verbs),
# delivery says he-formed (form — the potter verb, double-yod written-form)
m.spec_delta("bara/asah (create/make — the week's build verbs)",
             "yatzar (form — the potter verb, double-yod ktiv)")
# witness-tier presupposed read: flood_breath_verbal_analogy on
# nishmat_chayim — read, not installed
m.witness_read("nishmat_chayim", "flood_breath_verbal_analogy",
                cites=["Bereshit Rabbah 14:10"])
# witness-grounded state (its own tier): four_recorded_readings on
# vayyitzer_double_yod
m.witness_state("vayyitzer_double_yod", "four_recorded_readings",
                cites=["Berakhot 61a:3", "Bereshit Rabbah 14:2", "Bereshit Rabbah 14:3", "Eruvin 18a:20"])
# witness-tier presupposed read: self_preservation_command on nefesh_chayah
# — read, not installed
m.witness_read("nefesh_chayah", "self_preservation_command",
                cites=["Taanit 22b:11", "Bereshit Rabbah 14:9"])
# witness-tier presupposed read: shaped_fetus_purity_law on
# vayyitzer_man_and_beast — read, not installed
m.witness_read("vayyitzer_man_and_beast", "shaped_fetus_purity_law",
                cites=["Niddah 22b:13", "Chullin 71a:12"])

# -------------------------- Gen.2.8 · PLANT_PLACE --------------------------
# וַיִּטַּע יְהוָה אֱלֹהִים גַּן־בְּעֵדֶן מִקֶּדֶם וַיָּשֶׂם שָׁם
# אֶת־הָאָדָם אֲשֶׁר יָצָר
# "And the LORD God planted a garden eastward, in Eden; and there He put the
# man whom He had formed."
m.step("Gen.2.8")
# ‹וַיִּטַּע יְהוָה אֱלֹהִים גַּן־בְּעֵדֶן מִקֶּדֶם› (“and-he-planted YHWH
# God garden in-Eden from-east-or-of-old”) — event: plant — agent the-LORD-
# God; theme garden
m.event("plant", agent="YHWH_Elohim", themes=["gan"])
# ‹וַיָּשֶׂם שָׁם אֶת־הָאָדָם אֲשֶׁר יָצָר› (“and-he-set there obj-marker
# the-human whom he-formed”) — event: place — agent the-LORD-God; theme
# human
m.event("place", agent="YHWH_Elohim", themes=["adam"])
# ‹גַּן› (“garden”) — the world gains: garden
m.install("gan")
# reads without prior install (flag, not fix): Eden
m.presupposed("eden")
# witness-grounded state (its own tier):
# recorded_dispute_time_and_containment on gan_planting
m.witness_state("gan_planting", "recorded_dispute_time_and_containment",
                cites=["Bereshit Rabbah 15:3", "Pesachim 54a:10", "Bereshit Rabbah 15:2"])

# -------------------------- Gen.2.9 · SPROUT_TWO_TREES ---------------------
# וַיַּצְמַח יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־עֵץ נֶחְמָד לְמַרְאֶה וְטוֹב
# לְמַאֲכָל וְעֵץ הַחַיִּים בְּתוֹךְ הַגָּן וְעֵץ הַדַּעַת טוֹב וָרָע
# "And out of the ground made the LORD God to grow every tree that is
# pleasant to the sight, and good for food; the tree of life also in the
# midst of the garden, and the tree of the knowledge of good and evil."
m.step("Gen.2.9")
# ‹וַיַּצְמַח יְהוָה אֱלֹהִים מִן־הָאֲדָמָה כָּל־עֵץ› (“and-he-caused-sprout
# YHWH God from the-ground all tree”) — event: sprout — agent the-LORD-God;
# theme all-tree
m.event("sprout", agent="YHWH_Elohim", themes=["kol_etz"])
# ‹וְעֵץ הַחַיִּים בְּתוֹךְ הַגָּן וְעֵץ הַדַּעַת טוֹב וָרָע› (“and-tree-of
# the-life in-midst the-garden and-tree-of the-knowledge good and-evil”) —
# the world gains: tree-of-life, tree-of-knowledge-of-good-and-evil
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
# ‹וְנָהָר יֹצֵא … יִפָּרֵד וְהָיָה› (“and-river goes-out … divides and-
# becomes”) — fact holds: river-goes-out-from-Eden(to-water-obj-marker·et-
# the-garden); divides-to-four-heads(river)
m.fact("nahar_yotze_me_eden(le_hashqot_et_ha_gan)",
       "yipared_le_arbaah_rashim(nahar)")
# ‹וְהָיָה לְאַרְבָּעָה רָאשִׁים› (“and-becomes to-four heads”) — the world
# gains: river, river-1, river-2, river-3, river-4
m.install("nahar", "nahar_1", "nahar_2", "nahar_3", "nahar_4")

# -------------------------- Gen.2.11 · REGISTRY_ROW_1 ----------------------
# שֵׁם הָאֶחָד פִּישׁוֹן הוּא הַסֹּבֵב אֵת כָּל־אֶרֶץ הַחֲוִילָה אֲשֶׁר־שָׁם
# הַזָּהָב
# "The name of the first is Pishon; that is it which compasseth the whole
# land of Havilah, where there is gold."
m.step("Gen.2.11")
# ‹שֵׁם הָאֶחָד פִּישׁוֹן› (“name-of the-first Pison”) — named: river-1 :=
# Pishon
m.name("nahar_1", "Pishon")
# ‹הוּא הַסֹּבֵב … אֲשֶׁר־שָׁם הַזָּהָב› (“he/it the-circling … which name-
# of the-gold”) — fact holds: circling-all-earth-the-Havilah(river-1);
# there-the-gold(Havilah)
m.fact("sovev_kol_eretz_ha_chavilah(nahar_1)",
       "sham_ha_zahav(chavilah)")

# -------------------------- Gen.2.12 · REGISTRY_ROW_1_RESOURCES ------------
# וּזְהַב הָאָרֶץ הַהִוא טוֹב שָׁם הַבְּדֹלַח וְאֶבֶן הַשֹּׁהַם
# "And the gold of that land is good; there is bdellium and the onyx stone."
m.step("Gen.2.12")
# ‹וּזְהַב הָאָרֶץ הַהִוא טוֹב שָׁם הַבְּדֹלַח וְאֶבֶן הַשֹּׁהַם› (“and-
# gold-of the-earth that-one-ktiv-hu-qere-hi good there the-bdellium and-
# stone-of the-shoham”) — fact holds: gold-good(the-earth-the-that-one-ktiv-
# hu-qere-hi); there-the-bdellium-and-stone-of-the-shoham(Havilah)
m.fact("zahav_tov(ha_aretz_ha_hiv)",
       "sham_ha_bedolach_ve_even_ha_shoham(chavilah)")

# -------------------------- Gen.2.13 · REGISTRY_ROW_2 ----------------------
# וְשֵׁם־הַנָּהָר הַשֵּׁנִי גִּיחוֹן הוּא הַסּוֹבֵב אֵת כָּל־אֶרֶץ כּוּשׁ
# "And the name of the second river is Gihon; the same is it that compasseth
# the whole land of Cush."
m.step("Gen.2.13")
# ‹וְשֵׁם־הַנָּהָר הַשֵּׁנִי גִּיחוֹן› (“and-name the-river the-second
# Gihon”) — named: river-2 := Gichon
m.name("nahar_2", "Gichon")
# ‹הוּא הַסּוֹבֵב אֵת כָּל־אֶרֶץ כּוּשׁ› (“he/it the-circling obj-marker all
# earth Chush”) — fact holds: circling-all-earth-Chush(river-2)
m.fact("sovev_kol_eretz_kush(nahar_2)")

# -------------------------- Gen.2.14 · REGISTRY_ROWS_3_4 -------------------
# וְשֵׁם הַנָּהָר הַשְּׁלִישִׁי חִדֶּקֶל הוּא הַהֹלֵךְ קִדְמַת אַשּׁוּר
# וְהַנָּהָר הָרְבִיעִי הוּא פְרָת
# "And the name of the third river is Hiddekel; that is it which goeth
# toward the east of Asshur. And the fourth river is the Euphrates."
m.step("Gen.2.14")
# ‹חִדֶּקֶל … וְהַנָּהָר הָרְבִיעִי הוּא פְרָת› (“Hiddekel … and-the-river
# the-fourth he/it Perat”) — named: river-3 := Chidekel; river-4 := Perat
m.name("nahar_3", "Chidekel")
m.name("nahar_4", "Perat")
# ‹הוּא הַהֹלֵךְ קִדְמַת אַשּׁוּר› (“he/it the-going east-of Asshur”) — fact
# holds: going-east-of-Asshur(river-3)
m.fact("holekh_qidmat_ashur(nahar_3)")
# witness-tier presupposed read: proleptic_name_rule on
# known_geography_flags — read, not installed
m.witness_read("known_geography_flags", "proleptic_name_rule",
                cites=["Ketubot 10b:10", "Bereshit Rabbah 16:2"])

# -------------------------- Gen.2.15 · TAKE_SETTLE_ASSIGN_JOB --------------
# וַיִּקַּח יְהוָה אֱלֹהִים אֶת־הָאָדָם וַיַּנִּחֵהוּ בְגַן־עֵדֶן לְעָבְדָהּ
# וּלְשָׁמְרָהּ
# "And the LORD God took the man, and put him into the garden of Eden to
# dress it and to keep it."
m.step("Gen.2.15")
# ‹וַיִּקַּח יְהוָה אֱלֹהִים אֶת־הָאָדָם› (“and-he-took YHWH God obj-marker
# the-human”) — event: take — agent the-LORD-God; theme human
m.event("take", agent="YHWH_Elohim", themes=["adam"])
# ‹וַיַּנִּחֵהוּ בְגַן־עֵדֶן› (“and-settled-him in-garden-of Eden”) — event:
# settle — agent the-LORD-God; theme human
m.event("settle", agent="YHWH_Elohim", themes=["adam"])
# ‹לְעָבְדָהּ וּלְשָׁמְרָהּ› (“to-work-her and-to-keep-her”) — role
# assigned: human -> worker-and-keeper
m.assign("adam", "oved_ve_shomer")

# -------------------------- Gen.2.16 · COMMAND_PERMISSION ------------------
# וַיְצַו יְהוָה אֱלֹהִים עַל־הָאָדָם לֵאמֹר מִכֹּל עֵץ־הַגָּן אָכֹל תֹּאכֵל
# "And the LORD God commanded the man, saying: 'Of every tree of the garden
# thou mayest freely eat.'"
m.step("Gen.2.16")
# ‹וַיְצַו יְהוָה אֱלֹהִים עַל־הָאָדָם לֵאמֹר› (“and-he-commanded YHWH God
# upon the-human saying”) — event: command — agent the-LORD-God; theme human
m.event("command", agent="YHWH_Elohim", themes=["adam"])
# ‹מִכֹּל עֵץ־הַגָּן אָכֹל תֹּאכֵל› (“from-all tree-of the-garden eating
# you-may-eat”) — the-LORD-God speaks a demand — LET?: eat(human, from-
# every-tree-of-the-garden)
m.declare("YHWH_Elohim", "LET?",
          "akhal(adam, mi_kol_etz_ha_gan)")
# spec-delta — spec said all herb + all tree to-food (1:29 universal food
# grant), delivery says from-all tree the-garden + one exclusion pending
# (the grant narrows to a bounded domain)
m.spec_delta("kol esev + kol etz le-okhlah (1:29 universal food grant)",
             "mi-kol etz ha-gan + one exclusion pending (the grant narrows to a bounded domain)")
# witness-tier presupposed read: six_noachide_commandments on
# declare_payload — read, not installed
m.witness_read("declare_payload", "six_noachide_commandments",
                cites=["Sanhedrin 56b:4", "Bereshit Rabbah 16:6", "Pesikta DeRav Kahana 12:1", "Sanhedrin 56b:23"])

# -------------------------- Gen.2.17 · PROHIBITION_PENALTY -----------------
# וּמֵעֵץ הַדַּעַת טוֹב וָרָע לֹא תֹאכַל מִמֶּנּוּ כִּי בְּיוֹם אֲכָלְךָ
# מִמֶּנּוּ מוֹת תָּמוּת
# "'But of the tree of the knowledge of good and evil, thou shalt not eat of
# it; for in the day that thou eatest thereof thou shalt surely die.'"
m.step("Gen.2.17")
# ‹וּמֵעֵץ הַדַּעַת טוֹב וָרָע לֹא תֹאכַל מִמֶּנּוּ› (“and-from-tree-of the-
# knowledge good and-evil not you-shall-eat from-it”) — the-LORD-God speaks
# a demand — LET-NOT: eat(human, from-the-tree-of-knowledge-of-good-and-
# evil)
m.declare("YHWH_Elohim", "LET-NOT",
          "akhal(adam, me_etz_ha_daat_tov_va_ra)")
# ‹כִּי בְּיוֹם אֲכָלְךָ מִמֶּנּוּ מוֹת תָּמוּת› (“for in-day-of your-eating
# from-it dying you-shall-die”) — standing handler — if in-day-eat(human,
# from-the-tree-of-knowledge-of-good-and-evil) then dying-you-shall-
# die(human)
m.handler("be_yom_akhal(adam, me_etz_ha_daat_tov_va_ra)",
          "mot_tamut(adam)")
# witness-tier presupposed read: divine_day_scope_and_exact_payload on
# death_handler — read, not installed
m.witness_read("death_handler", "divine_day_scope_and_exact_payload",
                cites=["Bereshit Rabbah 19:8", "Bereshit Rabbah 19:3", "Sanhedrin 29a:34", "Jerusalem Talmud Kiddushin 4:1:9"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'adam', 'etz_ha_chayim', 'etz_ha_daat_tov_va_ra', 'gan', 'nahar', 'nahar_1', 'nahar_2', 'nahar_3', 'nahar_4'}
    assert m.presupposed_set() == {'adamah', 'aretz', 'eden', 'shamayim'}
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
    assert sorted(m.WORLD["witnessed"]) == ['chiasm_flip_earth_heaven', 'gan_planting', 'vayyitzer_double_yod']
    assert m.WORLD["witnessed"]['chiasm_flip_earth_heaven']["cites"] == ['Tosefta Keritot 4:7', 'Bereshit Rabbah 12:12']
    assert all('equal_creation_recorded_dispute' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['gan_planting']["cites"] == ['Bereshit Rabbah 15:3', 'Pesachim 54a:10', 'Bereshit Rabbah 15:2']
    assert all('recorded_dispute_time_and_containment' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['vayyitzer_double_yod']["cites"] == ['Berakhot 61a:3', 'Bereshit Rabbah 14:2', 'Bereshit Rabbah 14:3', 'Eruvin 18a:20']
    assert all('four_recorded_readings' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('yhwh_elohim_debut', 'complete_name_over_completed_world'), ('toledot_header', 'mortality_class_marker'), ('ed_mist', 'superseded_irrigation_regime'), ('ed_mist', 'sukkah_roof_and_niddah_law_source'), ('nishmat_chayim', 'flood_breath_verbal_analogy'), ('nefesh_chayah', 'self_preservation_command'), ('vayyitzer_man_and_beast', 'shaped_fetus_purity_law'), ('known_geography_flags', 'proleptic_name_rule'), ('declare_payload', 'six_noachide_commandments'), ('death_handler', 'divine_day_scope_and_exact_payload')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 13:3', 'Bereshit Rabbah 12:15']
    assert all('complete_name_over_completed_world' not in f for f in m.WORLD["facts"])
    assert 'yhwh_elohim_debut' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 12:7']
    assert all('mortality_class_marker' not in f for f in m.WORLD["facts"])
    assert 'toledot_header' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 13:9', 'Mekhilta DeRabbi Yishmael, Tractate Shirah 2:4']
    assert all('superseded_irrigation_regime' not in f for f in m.WORLD["facts"])
    assert 'ed_mist' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sukkah 11b:14', 'Jerusalem Talmud Sukkah 1:5:4', 'Jerusalem Talmud Shabbat 2:6:10']
    assert all('sukkah_roof_and_niddah_law_source' not in f for f in m.WORLD["facts"])
    assert 'ed_mist' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 14:10']
    assert all('flood_breath_verbal_analogy' not in f for f in m.WORLD["facts"])
    assert 'nishmat_chayim' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Taanit 22b:11', 'Bereshit Rabbah 14:9']
    assert all('self_preservation_command' not in f for f in m.WORLD["facts"])
    assert 'nefesh_chayah' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Niddah 22b:13', 'Chullin 71a:12']
    assert all('shaped_fetus_purity_law' not in f for f in m.WORLD["facts"])
    assert 'vayyitzer_man_and_beast' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Ketubot 10b:10', 'Bereshit Rabbah 16:2']
    assert all('proleptic_name_rule' not in f for f in m.WORLD["facts"])
    assert 'known_geography_flags' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Sanhedrin 56b:4', 'Bereshit Rabbah 16:6', 'Pesikta DeRav Kahana 12:1', 'Sanhedrin 56b:23']
    assert all('six_noachide_commandments' not in f for f in m.WORLD["facts"])
    assert 'declare_payload' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 19:8', 'Bereshit Rabbah 19:3', 'Sanhedrin 29a:34', 'Jerusalem Talmud Kiddushin 4:1:9']
    assert all('divine_day_scope_and_exact_payload' not in f for f in m.WORLD["facts"])
    assert 'death_handler' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
