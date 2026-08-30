#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹בֹּא־אַתָּה וְכָל־בֵּיתְךָ אֶל־הַתֵּבָה› (“come you and-all house-
# you/your to the-ark”) — the-LORD speaks a demand — LET: come(Noach, to-
# the-ark)
m.declare("YHWH", "LET",
          "bo(noach, el_ha_tevah)")
# ‹כִּי־אֹתְךָ רָאִיתִי צַדִּיק לְפָנַי› (“that YOU have-I-seen righteous
# before-Me”) — test PASS — oracle-word righteous, on Noach
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
# ‹הַטְּהוֹרָה … שִׁבְעָה שִׁבְעָה … לֹא טְהֹרָה הִוא שְׁנַיִם› (“the-clean
# … seven seven … not clean she two”) — fact holds: seven-seven-the-
# livestock-the-clean; two-which-not-clean
m.fact("shivah_shivah_ha_behemah_ha_tehorah",
       "shnayim_asher_lo_tehorah")
# witness-tier presupposed read: coarse_word_avoided_in_the_ink on
# clean_speech_circumlocution — read, not installed
m.witness_read("clean_speech_circumlocution", "coarse_word_avoided_in_the_ink",
                cites=["Bereshit Rabbah 32:4", "Pesachim 3a:10", "Bava Batra 123a:14", "Vayikra Rabbah 26:1"])

# -------------------------- Gen.7.3 · BIRDS_AND_THE_SEED_PURPOSE -----------
# גַּם מֵעוֹף הַשָּׁמַיִם שִׁבְעָה שִׁבְעָה זָכָר וּנְקֵבָה לְחַיּוֹת זֶרַע
# עַל־פְּנֵי כָל־הָאָרֶץ
# "of the fowl also of the air, seven and seven, male and female; to keep
# seed alive upon the face of all the earth."
m.step("Gen.7.3")
# ‹לְחַיּוֹת זֶרַע עַל־פְּנֵי כָל־הָאָרֶץ› (“to-keep-alive seed over face
# all the-earth”) — fact holds: to-keep-alive-seed-over-face-of-all-the-
# earth
m.fact("le_chayot_zera_al_pnei_khol_ha_aretz")

# -------------------------- Gen.7.4 · COUNTDOWN_STACK_WIPE_SCHEDULED -------
# כִּי לְיָמִים עוֹד שִׁבְעָה אָנֹכִי מַמְטִיר עַל־הָאָרֶץ אַרְבָּעִים יוֹם
# וְאַרְבָּעִים לָיְלָה וּמָחִיתִי אֶת־כָּל־הַיְקוּם אֲשֶׁר עָשִׂיתִי מֵעַל
# פְּנֵי הָאֲדָמָה
# "For yet seven days, and I will cause it to rain upon the earth forty days
# and forty nights; and every living substance that I have made will I blot
# out from off the face of the earth.'"
m.step("Gen.7.4")
# ‹עוֹד שִׁבְעָה אָנֹכִי מַמְטִיר … וּמָחִיתִי אֶת־כָּל־הַיְקוּם› (“still
# seven I raining … and-I-will-wipe obj-marker all the-standing-substance”)
# — fact holds: still-seven-day-I-raining; and-I-will-wipe-obj-marker·et-
# all-the-standing-substance
m.fact("od_shivat_yamim_anokhi_mamtir",
       "u_machiti_et_kol_ha_yequm")

# -------------------------- Gen.7.5 · REFRAIN_TWO --------------------------
# וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר־צִוָּהוּ יְהוָה
# "And Noah did according unto all that the LORD commanded him."
m.step("Gen.7.5")
# ‹וַיַּעַשׂ נֹחַ כְּכֹל אֲשֶׁר־צִוָּהוּ יְהוָה› (“and-make Noah like-all
# which commanded-him YHWH”) — fact holds: like-all-which-commanded-him-the-
# LORD
m.fact("ke_khol_asher_tzivahu_YHWH")

# -------------------------- Gen.7.6 · AGE_AT_THE_FLOOD ---------------------
# וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת שָׁנָה וְהַמַּבּוּל הָיָה מַיִם עַל־הָאָרֶץ
# "And Noah was six hundred years old when the flood of waters was upon the
# earth."
m.step("Gen.7.6")
# ‹וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת שָׁנָה› (“and-Noah son six hundred years”) —
# fact holds: Noach-son-six-hundred-year
m.fact("noach_ben_shesh_meot_shanah")

# -------------------------- Gen.7.7 · THE_ENTRY_DEMAND_POPPED --------------
# וַיָּבֹא נֹחַ וּבָנָיו וְאִשְׁתּוֹ וּנְשֵׁי־בָנָיו אִתּוֹ אֶל־הַתֵּבָה
# מִפְּנֵי מֵי הַמַּבּוּל
# "And Noah went in, and his sons, and his wife, and his sons' wives with
# him, into the ark, because of the waters of the flood."
m.step("Gen.7.7")
# ‹וַיָּבֹא נֹחַ … אֶל־הַתֵּבָה› (“and-he-came Noah … to the-ark”) — event:
# come — agent Noach; theme to-the-ark
m.event("come", agent="noach", themes=["el_ha_tevah"])
# ‹וַיָּבֹא … אֶל־הַתֵּבָה› (“and-he-came … to the-ark”) — demand settled
# (popped from the queue): come(Noach, to-the-ark)
m.result("bo(noach, el_ha_tevah)", tmark="t1")

# -------------------------- Gen.7.8 · THE_CARGO_CLASSES --------------------
# מִן־הַבְּהֵמָה הַטְּהוֹרָה וּמִן־הַבְּהֵמָה אֲשֶׁר אֵינֶנָּה טְהֹרָה
# וּמִן־הָעוֹף וְכֹל אֲשֶׁר־רֹמֵשׂ עַל־הָאֲדָמָה
# "Of clean beasts, and of beasts that are not clean, and of fowls, and of
# every thing that creepeth upon the ground,"
m.step("Gen.7.8")
# ‹הַטְּהוֹרָה … אֵינֶנָּה טְהֹרָה … הָעוֹף … רֹמֵשׂ› (“the-clean … is-not
# clean … the-flying-creature … creep”) — fact holds: the-clean-and-is-not-
# clean-and-the-flying-creature-and-the-creep
m.fact("ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes")

# -------------------------- Gen.7.9 · SELF_LOADING_REFRAIN_THREE -----------
# שְׁנַיִם שְׁנַיִם בָּאוּ אֶל־נֹחַ אֶל־הַתֵּבָה זָכָר וּנְקֵבָה כַּאֲשֶׁר
# צִוָּה אֱלֹהִים אֶת־נֹחַ
# "there went in two and two unto Noah into the ark, male and female, as God
# commanded Noah."
m.step("Gen.7.9")
# ‹שְׁנַיִם שְׁנַיִם בָּאוּ … כַּאֲשֶׁר צִוָּה אֱלֹהִים› (“two two they-came
# … like-as/which commanded God”) — fact holds: two-two-they-came-to-Noach;
# like-which-commanded-God-obj-marker·et-Noach
m.fact("shnayim_shnayim_bau_el_noach",
       "ka_asher_tzivah_elohim_et_noach")

# -------------------------- Gen.7.10 · SEVEN_DAYS_ELAPSE -------------------
# וַיְהִי לְשִׁבְעַת הַיָּמִים וּמֵי הַמַּבּוּל הָיוּ עַל־הָאָרֶץ
# "And it came to pass after the seven days, that the waters of the flood
# were upon the earth."
m.step("Gen.7.10")
# ‹וַיְהִי לְשִׁבְעַת הַיָּמִים וּמֵי הַמַּבּוּל הָיוּ› (“and-be to-seven
# the-day and-waters the-deluge be”) — fact holds: to-seven-the-day-waters-
# of-the-deluge
m.fact("le_shivat_ha_yamim_mei_ha_mabul")
# witness-tier presupposed read: mourning_period_and_its_rule on
# seven_days_delay — read, not installed
m.witness_read("seven_days_delay", "mourning_period_and_its_rule",
                cites=["Jerusalem Talmud Moed Katan 3:5:14", "Sanhedrin 108b:4", "Tosefta Sotah (Lieberman) 10:3"])

# -------------------------- Gen.7.11 · THE_DATE_DOUBLE_BREACH --------------
# בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי
# בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ בַּיּוֹם הַזֶּה נִבְקְעוּ כָּל־מַעְיְנֹת
# תְּהוֹם רַבָּה וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ
# "In the six hundredth year of Noah's life, in the second month, on the
# seventeenth day of the month, on the same day were all the fountains of
# the great deep broken up, and the windows of heaven were opened."
m.step("Gen.7.11")
# ‹בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי
# בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ› (“in-years six hundred years to-alive
# Noah in-month the-second in-seven teen day of-month”) — clock anchored: t0
# := year-of-600-of-month-2-day-17
m.time_anchor("shnat_600_chodesh_2_yom_17")
# ‹נִבְקְעוּ כָּל־מַעְיְנֹת תְּהוֹם רַבָּה› (“were-split all fountains-of
# the-deep many/great”) — event: split — theme fountains-of-deep-great
m.event("split", themes=["mayenot_tehom_rabbah"])
# ‹וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ› (“and-windows-of the-heavens were-
# opened”) — event: open — theme windows-of-the-heavens
m.event("open", themes=["arubot_ha_shamayim"])
# witness-tier presupposed read: measure_for_measure_on_a_shared_root on
# breach_event — read, not installed
m.witness_read("breach_event", "measure_for_measure_on_a_shared_root",
                cites=["Mekhilta DeRabbi Yishmael, Tractate Shirah 2:5"])
# witness-grounded state (its own tier): disputed_by_the_years_own_start on
# second_month_date
m.witness_state("second_month_date", "disputed_by_the_years_own_start",
                cites=["Rosh Hashanah 11b:6", "Jerusalem Talmud Taanit 1:3:2"])
# witness-tier presupposed read: exception_class_left_standing on
# all_wellsprings_quantifier — read, not installed
m.witness_read("all_wellsprings_quantifier", "exception_class_left_standing",
                cites=["Bereshit Rabbah 33:4"])

# -------------------------- Gen.7.12 · THE_RAIN_FORTY ----------------------
# וַיְהִי הַגֶּשֶׁם עַל־הָאָרֶץ אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה
# "And the rain was upon the earth forty days and forty nights."
m.step("Gen.7.12")
# ‹הַגֶּשֶׁם … אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה› (“the-rain … forty
# day and-forty night”) — fact holds: the-rain-forty-day-and-forty-night
m.fact("ha_geshem_arbaim_yom_va_arbaim_laylah")
# witness-tier presupposed read: twelve_months_worked_to_the_day on
# flood_calendar — read, not installed
m.witness_read("flood_calendar", "twelve_months_worked_to_the_day",
                cites=["Bereshit Rabbah 33:7", "Mishnah Eduyot 2:10", "Bereshit Rabbah 32:6"])

# -------------------------- Gen.7.13 · THE_SOLEMN_DAY_STAMP ----------------
# בְּעֶצֶם הַיּוֹם הַזֶּה בָּא נֹחַ וְשֵׁם־וְחָם וָיֶפֶת בְּנֵי־נֹחַ
# וְאֵשֶׁת נֹחַ וּשְׁלֹשֶׁת נְשֵׁי־בָנָיו אִתָּם אֶל־הַתֵּבָה
# "In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the
# sons of Noah, and Noah's wife, and the three wives of his sons with them,
# into the ark;"
m.step("Gen.7.13")
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה בָּא נֹחַ› (“in-the-very the-day the-this came
# Noah”) — fact holds: in-very-the-day-the-this-came-Noach
m.fact("be_etzem_ha_yom_ha_zeh_ba_noach")

# -------------------------- Gen.7.14 · FULL_TAXONOMY_EVERY_WING ------------
# הֵמָּה וְכָל־הַחַיָּה לְמִינָהּ וְכָל־הַבְּהֵמָה לְמִינָהּ וְכָל־הָרֶמֶשׂ
# הָרֹמֵשׂ עַל־הָאָרֶץ לְמִינֵהוּ וְכָל־הָעוֹף לְמִינֵהוּ כֹּל צִפּוֹר
# כָּל־כָּנָף
# "they, and every beast after its kind, and all the cattle after their
# kind, and every creeping thing that creepeth upon the earth after its
# kind, and every fowl after its kind, every bird of every sort."
m.step("Gen.7.14")
# ‹לְמִינָהּ … לְמִינֵהוּ … כֹּל צִפּוֹר כָּל־כָּנָף› (“by-its-kind … by-
# its-kind … all bird all wing”) — fact holds: all-the-beast-to-its-kind-
# the-flying-creature-to-its-kind; all-bird-all-wing
m.fact("kol_ha_chayah_le_minah_ha_of_le_minehu",
       "kol_tzippor_kol_kanaf")

# -------------------------- Gen.7.15 · THE_PAIRS_AND_THE_BREATH ------------
# וַיָּבֹאוּ אֶל־נֹחַ אֶל־הַתֵּבָה שְׁנַיִם שְׁנַיִם מִכָּל־הַבָּשָׂר
# אֲשֶׁר־בּוֹ רוּחַ חַיִּים
# "And they went in unto Noah into the ark, two and two of all flesh wherein
# is the breath of life."
m.step("Gen.7.15")
# ‹וַיָּבֹאוּ אֶל־נֹחַ … שְׁנַיִם שְׁנַיִם› (“and-came to Noah … two two”) —
# event: come — theme all-flesh-two-two
m.event("come", themes=["kol_basar_shnayim_shnayim"])

# -------------------------- Gen.7.16 · THE_SEAL_YHWH_SHUTS -----------------
# וְהַבָּאִים זָכָר וּנְקֵבָה מִכָּל־בָּשָׂר בָּאוּ כַּאֲשֶׁר צִוָּה אֹתוֹ
# אֱלֹהִים וַיִּסְגֹּר יְהוָה בַּעֲדוֹ
# "And they that went in, went in male and female of all flesh, as God
# commanded him; and the LORD shut him in."
m.step("Gen.7.16")
# ‹וְהַבָּאִים זָכָר וּנְקֵבָה … בָּאוּ כַּאֲשֶׁר צִוָּה אֹתוֹ אֱלֹהִים›
# (“and-the-comers male and-female … come as commanded obj-marker God”) —
# fact holds: the-comers-male-and-female-they-came; like-which-commanded-it-
# God
m.fact("ha_baim_zakhar_u_nekevah_bau",
       "ka_asher_tzivah_oto_elohim")
# ‹וַיִּסְגֹּר יְהוָה בַּעֲדוֹ› (“and-He-shut YHWH behind-him”) — event:
# shut — agent the-LORD; theme about-him
m.event("shut", agent="YHWH", themes=["baado"])
# witness-tier presupposed read: permission_discipline_loop on shutting_in —
# read, not installed
m.witness_read("shutting_in", "permission_discipline_loop",
                cites=["Bereshit Rabbah 34:4", "Bereshit Rabbah 34:6", "Bereshit Rabbah 34:1"])

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
    assert sorted(m.WORLD["witnessed"]) == ['second_month_date']
    assert m.WORLD["witnessed"]['second_month_date']["cites"] == ['Rosh Hashanah 11b:6', 'Jerusalem Talmud Taanit 1:3:2']
    assert all('disputed_by_the_years_own_start' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('clean_speech_circumlocution', 'coarse_word_avoided_in_the_ink'), ('seven_days_delay', 'mourning_period_and_its_rule'), ('breach_event', 'measure_for_measure_on_a_shared_root'), ('all_wellsprings_quantifier', 'exception_class_left_standing'), ('flood_calendar', 'twelve_months_worked_to_the_day'), ('shutting_in', 'permission_discipline_loop')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 32:4', 'Pesachim 3a:10', 'Bava Batra 123a:14', 'Vayikra Rabbah 26:1']
    assert all('coarse_word_avoided_in_the_ink' not in f for f in m.WORLD["facts"])
    assert 'clean_speech_circumlocution' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Jerusalem Talmud Moed Katan 3:5:14', 'Sanhedrin 108b:4', 'Tosefta Sotah (Lieberman) 10:3']
    assert all('mourning_period_and_its_rule' not in f for f in m.WORLD["facts"])
    assert 'seven_days_delay' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Mekhilta DeRabbi Yishmael, Tractate Shirah 2:5']
    assert all('measure_for_measure_on_a_shared_root' not in f for f in m.WORLD["facts"])
    assert 'breach_event' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 33:4']
    assert all('exception_class_left_standing' not in f for f in m.WORLD["facts"])
    assert 'all_wellsprings_quantifier' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 33:7', 'Mishnah Eduyot 2:10', 'Bereshit Rabbah 32:6']
    assert all('twelve_months_worked_to_the_day' not in f for f in m.WORLD["facts"])
    assert 'flood_calendar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 34:4', 'Bereshit Rabbah 34:6', 'Bereshit Rabbah 34:1']
    assert all('permission_discipline_loop' not in f for f in m.WORLD["facts"])
    assert 'shutting_in' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
