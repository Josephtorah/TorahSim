#!/usr/bin/env python3
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
# ‹וַיֹּאמֶר יְהוָה לְנֹחַ› (“and-say YHWH to-Noah”)
# ‹בֹּא־אַתָּה וְכָל־בֵּיתְךָ אֶל־הַתֵּבָה› (“come you and-all house-
# you/your to the-ark”)
# ‹כִּי־אֹתְךָ רָאִיתִי צַדִּיק› (“that YOU have-I-seen righteous”)
# ‹לְפָנַי בַּדּוֹר הַזֶּה› (“before-Me in-generation this”)
# "And the LORD said unto Noah: 'Come thou and all thy house into the ark;
# for thee have I seen righteous before Me in this generation.'"
m.step("Gen.7.1")
# ‹בֹּא־אַתָּה וְכָל־בֵּיתְךָ אֶל־הַתֵּבָה› (“come you and-all house-
# you/your to the-ark”)
# — the-LORD speaks a demand — LET: come(Noach, to-the-ark)
m.declare("YHWH", "LET",
          "bo(noach, el_ha_tevah)")
# ‹כִּי־אֹתְךָ רָאִיתִי צַדִּיק› (“that YOU have-I-seen righteous”)
# ‹לְפָנַי› (“before-Me”)
# — test PASS — oracle-word righteous, on Noach
m.test("PASS", "tzaddik", "noach")
# reads without prior install (flag, not fix): Noach, ark
m.presupposed("noach", "tevah")
# witness-tier presupposed read: praise_presence on otekha_raiti_tzadik —
# read, not installed
m.witness_read("otekha_raiti_tzadik", "praise_presence",
                cites=["Eruvin 18b:12", "Eruvin 18b:13", "Eruvin 18b:14"])

# -------------------------- Gen.7.2 · CLEAN_SEVENS_AMENDMENT ---------------
# ‹מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה› (“from-all the-livestock the-clean”)
# ‹תִּקַּח־לְךָ שִׁבְעָה שִׁבְעָה› (“you-shall-take to-you/your seven
# seven”)
# ‹אִישׁ וְאִשְׁתּוֹ וּמִן־הַבְּהֵמָה› (“a-man and-his-wife and-from the-
# livestock”)
# ‹אֲשֶׁר לֹא טְהֹרָה› (“which not clean”)
# ‹הִוא שְׁנַיִם אִישׁ› (“she two a-man”)
# ‹וְאִשְׁתּוֹ› (“and-his-wife”)
# "Of every clean beast thou shalt take to thee seven and seven, each with
# his mate; and of the beasts that are not clean two and two, each with his
# mate;"
m.step("Gen.7.2")
# ‹הַטְּהוֹרָה … שִׁבְעָה שִׁבְעָה› (“the-clean … seven seven”)
# ‹… לֹא טְהֹרָה הִוא› (“not clean she”)
# ‹שְׁנַיִם› (“two”)
# — fact holds: seven-seven-the-livestock-the-clean; two-which-not-clean
m.fact("shivah_shivah_ha_behemah_ha_tehorah",
       "shnayim_asher_lo_tehorah")
# witness-tier presupposed read: coarse_word_avoided_in_the_ink on
# clean_speech_circumlocution — read, not installed
m.witness_read("clean_speech_circumlocution", "coarse_word_avoided_in_the_ink",
                cites=["Bereshit Rabbah 32:4", "Pesachim 3a:10", "Bava Batra 123a:14", "Vayikra Rabbah 26:1"])

# -------------------------- Gen.7.3 · BIRDS_AND_THE_SEED_PURPOSE -----------
# ‹גַּם מֵעוֹף הַשָּׁמַיִם› (“also from-flying-creature the-heavens”)
# ‹שִׁבְעָה שִׁבְעָה זָכָר› (“seven seven male”)
# ‹וּנְקֵבָה לְחַיּוֹת זֶרַע› (“and-female to-keep-alive seed”)
# ‹עַל־פְּנֵי כָל־הָאָרֶץ› (“over face all the-earth”)
# "of the fowl also of the air, seven and seven, male and female; to keep
# seed alive upon the face of all the earth."
m.step("Gen.7.3")
# ‹לְחַיּוֹת זֶרַע עַל־פְּנֵי› (“to-keep-alive seed over face”)
# ‹כָל־הָאָרֶץ› (“all the-earth”)
# — fact holds: to-keep-alive-seed-over-face-of-all-the-earth
m.fact("le_chayot_zera_al_pnei_khol_ha_aretz")

# -------------------------- Gen.7.4 · COUNTDOWN_STACK_WIPE_SCHEDULED -------
# ‹כִּי לְיָמִים עוֹד› (“that to-day still”)
# ‹שִׁבְעָה אָנֹכִי מַמְטִיר› (“seven I raining”)
# ‹עַל־הָאָרֶץ אַרְבָּעִים יוֹם› (“over the-earth forty day”)
# ‹וְאַרְבָּעִים לָיְלָה וּמָחִיתִי› (“and-forty night and-I-will-wipe”)
# ‹אֶת־כָּל־הַיְקוּם אֲשֶׁר עָשִׂיתִי› (“obj-marker all the-standing-
# substance which I-made”)
# ‹מֵעַל פְּנֵי הָאֲדָמָה› (“from-over face the-ground”)
# "For yet seven days, and I will cause it to rain upon the earth forty days
# and forty nights; and every living substance that I have made will I blot
# out from off the face of the earth.'"
m.step("Gen.7.4")
# ‹עוֹד שִׁבְעָה אָנֹכִי› (“still seven I”)
# ‹מַמְטִיר … וּמָחִיתִי אֶת־כָּל־הַיְקוּם› (“raining … and-I-will-wipe obj-
# marker all the-standing-substance”)
# — fact holds: still-seven-day-I-raining; and-I-will-wipe-obj-marker·et-
# all-the-standing-substance
m.fact("od_shivat_yamim_anokhi_mamtir",
       "u_machiti_et_kol_ha_yequm")

# -------------------------- Gen.7.5 · REFRAIN_TWO --------------------------
# ‹וַיַּעַשׂ נֹחַ כְּכֹל› (“and-make Noah like-all”)
# ‹אֲשֶׁר־צִוָּהוּ יְהוָה› (“which commanded-him YHWH”)
# "And Noah did according unto all that the LORD commanded him."
m.step("Gen.7.5")
# ‹וַיַּעַשׂ נֹחַ כְּכֹל› (“and-make Noah like-all”)
# ‹אֲשֶׁר־צִוָּהוּ יְהוָה› (“which commanded-him YHWH”)
# — fact holds: like-all-which-commanded-him-the-LORD
m.fact("ke_khol_asher_tzivahu_YHWH")

# -------------------------- Gen.7.6 · AGE_AT_THE_FLOOD ---------------------
# ‹וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת› (“and-Noah son six hundred”)
# ‹שָׁנָה וְהַמַּבּוּל הָיָה› (“years and-the-deluge be”)
# ‹מַיִם עַל־הָאָרֶץ› (“waters over the-earth”)
# "And Noah was six hundred years old when the flood of waters was upon the
# earth."
m.step("Gen.7.6")
# ‹וְנֹחַ בֶּן־שֵׁשׁ מֵאוֹת› (“and-Noah son six hundred”)
# ‹שָׁנָה› (“years”)
# — fact holds: Noach-son-six-hundred-year
m.fact("noach_ben_shesh_meot_shanah")

# -------------------------- Gen.7.7 · THE_ENTRY_DEMAND_POPPED --------------
# ‹וַיָּבֹא נֹחַ וּבָנָיו› (“and-he-came Noah and-son-him/its”)
# ‹וְאִשְׁתּוֹ וּנְשֵׁי־בָנָיו אִתּוֹ› (“and-his-wife and-woman son-him/its
# with-him/its”)
# ‹אֶל־הַתֵּבָה מִפְּנֵי מֵי› (“to the-ark from-before waters-of”)
# ‹הַמַּבּוּל› (“the-deluge”)
# "And Noah went in, and his sons, and his wife, and his sons' wives with
# him, into the ark, because of the waters of the flood."
m.step("Gen.7.7")
# ‹וַיָּבֹא נֹחַ … אֶל־הַתֵּבָה› (“and-he-came Noah … to the-ark”)
# — event: come — agent Noach; theme to-the-ark
m.event("come", agent="noach", themes=["el_ha_tevah"])
# ‹וַיָּבֹא … אֶל־הַתֵּבָה› (“and-he-came … to the-ark”)
# — demand settled (popped from the queue): come(Noach, to-the-ark)
m.result("bo(noach, el_ha_tevah)", tmark="t1")

# -------------------------- Gen.7.8 · THE_CARGO_CLASSES --------------------
# ‹מִן־הַבְּהֵמָה הַטְּהוֹרָה וּמִן־הַבְּהֵמָה› (“from the-livestock the-
# clean and-from the-livestock”)
# ‹אֲשֶׁר אֵינֶנָּה טְהֹרָה› (“which is-not clean”)
# ‹וּמִן־הָעוֹף וְכֹל אֲשֶׁר־רֹמֵשׂ› (“and-from the-flying-creature and-all
# which creep”)
# ‹עַל־הָאֲדָמָה› (“over the-ground”)
# "Of clean beasts, and of beasts that are not clean, and of fowls, and of
# every thing that creepeth upon the ground,"
m.step("Gen.7.8")
# ‹הַטְּהוֹרָה … אֵינֶנָּה טְהֹרָה› (“the-clean … is-not clean”)
# ‹… הָעוֹף … רֹמֵשׂ› (“the-flying-creature … creep”)
# — fact holds: the-clean-and-is-not-clean-and-the-flying-creature-and-the-
# creep
m.fact("ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes")

# -------------------------- Gen.7.9 · SELF_LOADING_REFRAIN_THREE -----------
# ‹שְׁנַיִם שְׁנַיִם בָּאוּ› (“two two they-came”)
# ‹אֶל־נֹחַ אֶל־הַתֵּבָה זָכָר› (“to Noah to the-ark male”)
# ‹וּנְקֵבָה כַּאֲשֶׁר צִוָּה› (“and-female like-as/which commanded”)
# ‹אֱלֹהִים אֶת־נֹחַ› (“God obj-marker Noah”)
# "there went in two and two unto Noah into the ark, male and female, as God
# commanded Noah."
m.step("Gen.7.9")
# ‹שְׁנַיִם שְׁנַיִם בָּאוּ› (“two two they-came”)
# ‹… כַּאֲשֶׁר צִוָּה אֱלֹהִים› (“like-as/which commanded God”)
# — fact holds: two-two-they-came-to-Noach; like-which-commanded-God-obj-
# marker·et-Noach
m.fact("shnayim_shnayim_bau_el_noach",
       "ka_asher_tzivah_elohim_et_noach")

# -------------------------- Gen.7.10 · SEVEN_DAYS_ELAPSE -------------------
# ‹וַיְהִי לְשִׁבְעַת הַיָּמִים› (“and-be to-seven the-day”)
# ‹וּמֵי הַמַּבּוּל הָיוּ› (“and-waters the-deluge be”)
# ‹עַל־הָאָרֶץ› (“over the-earth”)
# "And it came to pass after the seven days, that the waters of the flood
# were upon the earth."
m.step("Gen.7.10")
# ‹וַיְהִי לְשִׁבְעַת הַיָּמִים› (“and-be to-seven the-day”)
# ‹וּמֵי הַמַּבּוּל הָיוּ› (“and-waters the-deluge be”)
# — fact holds: to-seven-the-day-waters-of-the-deluge
m.fact("le_shivat_ha_yamim_mei_ha_mabul")
# witness-tier presupposed read: mourning_period_and_its_rule on
# seven_days_delay — read, not installed
m.witness_read("seven_days_delay", "mourning_period_and_its_rule",
                cites=["Jerusalem Talmud Moed Katan 3:5:14", "Sanhedrin 108b:4", "Tosefta Sotah (Lieberman) 10:3"])

# -------------------------- Gen.7.11 · THE_DATE_DOUBLE_BREACH --------------
# ‹בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה› (“in-years six hundred years”)
# ‹לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי› (“to-alive Noah in-month the-second”)
# ‹בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ› (“in-seven teen day of-month”)
# ‹בַּיּוֹם הַזֶּה נִבְקְעוּ› (“in-day the-this were-split”)
# ‹כָּל־מַעְיְנֹת תְּהוֹם רַבָּה› (“all fountains-of the-deep many/great”)
# ‹וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ› (“and-windows-of the-heavens were-
# opened”)
# "In the six hundredth year of Noah's life, in the second month, on the
# seventeenth day of the month, on the same day were all the fountains of
# the great deep broken up, and the windows of heaven were opened."
m.step("Gen.7.11")
# ‹בִּשְׁנַת שֵׁשׁ־מֵאוֹת שָׁנָה› (“in-years six hundred years”)
# ‹לְחַיֵּי־נֹחַ בַּחֹדֶשׁ הַשֵּׁנִי› (“to-alive Noah in-month the-second”)
# ‹בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ› (“in-seven teen day of-month”)
# — clock anchored: t0 := year-of-600-of-month-2-day-17
m.time_anchor("shnat_600_chodesh_2_yom_17")
# ‹נִבְקְעוּ כָּל־מַעְיְנֹת תְּהוֹם› (“were-split all fountains-of the-
# deep”)
# ‹רַבָּה› (“many/great”)
# — event: split — theme fountains-of-deep-great
m.event("split", themes=["mayenot_tehom_rabbah"])
# ‹וַאֲרֻבֹּת הַשָּׁמַיִם נִפְתָּחוּ› (“and-windows-of the-heavens were-
# opened”)
# — event: open — theme windows-of-the-heavens
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
# witness-tier presupposed read: hydraulic_model_then_manna_a_fortiori on
# flood_height_numbers — read, not installed
m.witness_read("flood_height_numbers", "hydraulic_model_then_manna_a_fortiori",
                cites=["Yoma 76a:6", "Yoma 76a:10", "Mekhilta DeRabbi Yishmael, Tractate Vayassa 4:17"])

# -------------------------- Gen.7.12 · THE_RAIN_FORTY ----------------------
# ‹וַיְהִי הַגֶּשֶׁם עַל־הָאָרֶץ› (“and-be the-rain over the-earth”)
# ‹אַרְבָּעִים יוֹם וְאַרְבָּעִים› (“forty day and-forty”)
# ‹לָיְלָה› (“night”)
# "And the rain was upon the earth forty days and forty nights."
m.step("Gen.7.12")
# ‹הַגֶּשֶׁם … אַרְבָּעִים יוֹם› (“the-rain … forty day”)
# ‹וְאַרְבָּעִים לָיְלָה› (“and-forty night”)
# — fact holds: the-rain-forty-day-and-forty-night
m.fact("ha_geshem_arbaim_yom_va_arbaim_laylah")
# witness-tier presupposed read: twelve_months_worked_to_the_day on
# flood_calendar — read, not installed
m.witness_read("flood_calendar", "twelve_months_worked_to_the_day",
                cites=["Bereshit Rabbah 33:7", "Mishnah Eduyot 2:10", "Bereshit Rabbah 32:6"])

# -------------------------- Gen.7.13 · THE_SOLEMN_DAY_STAMP ----------------
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה› (“in-the-very the-day the-this”)
# ‹בָּא נֹחַ וְשֵׁם־וְחָם› (“came Noah and-Sem and-Ham”)
# ‹וָיֶפֶת בְּנֵי־נֹחַ וְאֵשֶׁת› (“and-Japheth son Noah and-woman”)
# ‹נֹחַ וּשְׁלֹשֶׁת נְשֵׁי־בָנָיו› (“Noah and-three woman son-him/its”)
# ‹אִתָּם אֶל־הַתֵּבָה› (“with-them/their to the-ark”)
# "In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the
# sons of Noah, and Noah's wife, and the three wives of his sons with them,
# into the ark;"
m.step("Gen.7.13")
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה› (“in-the-very the-day the-this”)
# ‹בָּא נֹחַ› (“came Noah”)
# — fact holds: in-very-the-day-the-this-came-Noach
m.fact("be_etzem_ha_yom_ha_zeh_ba_noach")

# -------------------------- Gen.7.14 · FULL_TAXONOMY_EVERY_WING ------------
# ‹הֵמָּה וְכָל־הַחַיָּה לְמִינָהּ› (“they and-all the-living by-its-kind”)
# ‹וְכָל־הַבְּהֵמָה לְמִינָהּ וְכָל־הָרֶמֶשׂ› (“and-all the-livestock by-
# its-kind and-all the-creeper”)
# ‹הָרֹמֵשׂ עַל־הָאָרֶץ לְמִינֵהוּ› (“the-creeper over the-earth by-its-
# kind”)
# ‹וְכָל־הָעוֹף לְמִינֵהוּ כֹּל› (“and-all the-flying-creature by-its-kind
# all”)
# ‹צִפּוֹר כָּל־כָּנָף› (“bird all wing”)
# "they, and every beast after its kind, and all the cattle after their
# kind, and every creeping thing that creepeth upon the earth after its
# kind, and every fowl after its kind, every bird of every sort."
m.step("Gen.7.14")
# ‹לְמִינָהּ … לְמִינֵהוּ … כֹּל› (“by-its-kind … by-its-kind … all”)
# ‹צִפּוֹר כָּל־כָּנָף› (“bird all wing”)
# — fact holds: all-the-beast-to-its-kind-the-flying-creature-to-its-kind;
# all-bird-all-wing
m.fact("kol_ha_chayah_le_minah_ha_of_le_minehu",
       "kol_tzippor_kol_kanaf")
# witness-tier presupposed read: bird_tokens on kol_tzipor_kol_kanaf — read,
# not installed
m.witness_read("kol_tzipor_kol_kanaf", "bird_tokens",
                cites=["Chullin 139b:18", "Chullin 139b:19", "Chullin 139b:20"])

# -------------------------- Gen.7.15 · THE_PAIRS_AND_THE_BREATH ------------
# ‹וַיָּבֹאוּ אֶל־נֹחַ אֶל־הַתֵּבָה› (“and-came to Noah to the-ark”)
# ‹שְׁנַיִם שְׁנַיִם מִכָּל־הַבָּשָׂר› (“two two from-all the-flesh”)
# ‹אֲשֶׁר־בּוֹ רוּחַ חַיִּים› (“which in-him/its breath-of life”)
# "And they went in unto Noah into the ark, two and two of all flesh wherein
# is the breath of life."
m.step("Gen.7.15")
# ‹וַיָּבֹאוּ אֶל־נֹחַ … שְׁנַיִם› (“and-came to Noah … two”)
# ‹שְׁנַיִם› (“two”)
# — event: come — theme all-flesh-two-two
m.event("come", themes=["kol_basar_shnayim_shnayim"])

# -------------------------- Gen.7.16 · THE_SEAL_YHWH_SHUTS -----------------
# ‹וְהַבָּאִים זָכָר וּנְקֵבָה› (“and-the-comers male and-female”)
# ‹מִכָּל־בָּשָׂר בָּאוּ כַּאֲשֶׁר› (“from-all flesh come as”)
# ‹צִוָּה אֹתוֹ אֱלֹהִים› (“commanded obj-marker God”)
# ‹וַיִּסְגֹּר יְהוָה בַּעֲדוֹ› (“and-He-shut YHWH behind-him”)
# "And they that went in, went in male and female of all flesh, as God
# commanded him; and the LORD shut him in."
m.step("Gen.7.16")
# ‹וְהַבָּאִים זָכָר וּנְקֵבָה› (“and-the-comers male and-female”)
# ‹… בָּאוּ כַּאֲשֶׁר צִוָּה› (“come as commanded”)
# ‹אֹתוֹ אֱלֹהִים› (“obj-marker God”)
# — fact holds: the-comers-male-and-female-they-came; like-which-commanded-
# it-God
m.fact("ha_baim_zakhar_u_nekevah_bau",
       "ka_asher_tzivah_oto_elohim")
# ‹וַיִּסְגֹּר יְהוָה בַּעֲדוֹ› (“and-He-shut YHWH behind-him”)
# — event: shut — agent the-LORD; theme about-him
m.event("shut", agent="YHWH", themes=["baado"])
# witness-tier presupposed read: permission_discipline_loop on shutting_in —
# read, not installed
m.witness_read("shutting_in", "permission_discipline_loop",
                cites=["Bereshit Rabbah 34:4", "Bereshit Rabbah 34:6", "Bereshit Rabbah 34:1"])
# witness-tier presupposed read: self_presenting on
# ve_ha_baim_zakhar_u_nekevah — read, not installed
m.witness_read("ve_ha_baim_zakhar_u_nekevah", "self_presenting",
                cites=["Zevachim 116a:10", "Zevachim 116a:11"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('otekha_raiti_tzadik', 'praise_presence'), ('clean_speech_circumlocution', 'coarse_word_avoided_in_the_ink'), ('seven_days_delay', 'mourning_period_and_its_rule'), ('breach_event', 'measure_for_measure_on_a_shared_root'), ('all_wellsprings_quantifier', 'exception_class_left_standing'), ('flood_height_numbers', 'hydraulic_model_then_manna_a_fortiori'), ('flood_calendar', 'twelve_months_worked_to_the_day'), ('kol_tzipor_kol_kanaf', 'bird_tokens'), ('shutting_in', 'permission_discipline_loop'), ('ve_ha_baim_zakhar_u_nekevah', 'self_presenting')]
    assert m.WITNESS_READS[0]["cites"] == ['Eruvin 18b:12', 'Eruvin 18b:13', 'Eruvin 18b:14']
    assert all('praise_presence' not in f for f in m.WORLD["facts"])
    assert 'otekha_raiti_tzadik' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 32:4', 'Pesachim 3a:10', 'Bava Batra 123a:14', 'Vayikra Rabbah 26:1']
    assert all('coarse_word_avoided_in_the_ink' not in f for f in m.WORLD["facts"])
    assert 'clean_speech_circumlocution' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Jerusalem Talmud Moed Katan 3:5:14', 'Sanhedrin 108b:4', 'Tosefta Sotah (Lieberman) 10:3']
    assert all('mourning_period_and_its_rule' not in f for f in m.WORLD["facts"])
    assert 'seven_days_delay' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Mekhilta DeRabbi Yishmael, Tractate Shirah 2:5']
    assert all('measure_for_measure_on_a_shared_root' not in f for f in m.WORLD["facts"])
    assert 'breach_event' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 33:4']
    assert all('exception_class_left_standing' not in f for f in m.WORLD["facts"])
    assert 'all_wellsprings_quantifier' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Yoma 76a:6', 'Yoma 76a:10', 'Mekhilta DeRabbi Yishmael, Tractate Vayassa 4:17']
    assert all('hydraulic_model_then_manna_a_fortiori' not in f for f in m.WORLD["facts"])
    assert 'flood_height_numbers' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 33:7', 'Mishnah Eduyot 2:10', 'Bereshit Rabbah 32:6']
    assert all('twelve_months_worked_to_the_day' not in f for f in m.WORLD["facts"])
    assert 'flood_calendar' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Chullin 139b:18', 'Chullin 139b:19', 'Chullin 139b:20']
    assert all('bird_tokens' not in f for f in m.WORLD["facts"])
    assert 'kol_tzipor_kol_kanaf' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 34:4', 'Bereshit Rabbah 34:6', 'Bereshit Rabbah 34:1']
    assert all('permission_discipline_loop' not in f for f in m.WORLD["facts"])
    assert 'shutting_in' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Zevachim 116a:10', 'Zevachim 116a:11']
    assert all('self_presenting' not in f for f in m.WORLD["facts"])
    assert 've_ha_baim_zakhar_u_nekevah' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
