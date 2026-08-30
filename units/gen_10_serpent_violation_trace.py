#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וְהַנָּחָשׁ הָיָה עָרוּם … אֲשֶׁר עָשָׂה יְהוָה אֱלֹהִים› (“and-the-
# serpent was cunning … which he-made YHWH God”) — fact holds:
# cunning(serpent); make-the-LORD-God(serpent)
m.fact("arum(nachash)",
       "asah_YHWH_Elohim(nachash)")
# reads without prior install (flag, not fix): serpent, woman, garden
m.presupposed("nachash", "ishah", "gan")
# ‹וַיֹּאמֶר אֶל־הָאִשָּׁה אַף כִּי־אָמַר אֱלֹהִים› (“and-he-said to the-
# woman really that he-said God”) — event: say — agent serpent; theme woman
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
# witness-grounded state (its own tier): erect_legged_intended_king_baseline
# on nachash_pre_curse_form
m.witness_state("nachash_pre_curse_form", "erect_legged_intended_king_baseline",
                cites=["Bereshit Rabbah 19:1", "Sotah 9b:1", "Tosefta Sotah 4:5"])

# -------------------------- Gen.3.2 · WOMAN_PERMISSION_REDUCED -------------
# וַתֹּאמֶר הָאִשָּׁה אֶל־הַנָּחָשׁ מִפְּרִי עֵץ־הַגָּן נֹאכֵל
# "And the woman said unto the serpent: 'Of the fruit of the trees of the
# garden we may eat.'"
m.step("Gen.3.2")
# ‹וַתֹּאמֶר הָאִשָּׁה אֶל־הַנָּחָשׁ› (“and-she-said the-woman to the-
# serpent”) — event: say — agent woman; theme serpent
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
# ‹וְלֹא תִגְּעוּ בּוֹ› (“and-not you-shall-touch in-it”) — spec-delta —
# spec said not she-ate from-it (gen-08 2:17: eating prohibited — nothing
# else), delivery says not you-shall-eat(pl) from-it VE-LO TIGU BO (eating
# AND TOUCHING prohibited — a fence added to the rule)
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
# ‹וַיֹּאמֶר הַנָּחָשׁ אֶל־הָאִשָּׁה› (“and-he-said the-serpent to the-
# woman”) — event: say — agent serpent; theme woman
m.event("say", agent="nachash", themes=["ishah"])
# ‹לֹא־מוֹת תְּמֻתוּן› (“not dying you-shall-die(pl)”) — spec-delta — spec
# said dying you-shall-die (gen-08 2:17: the penalty, doubled — the emphatic
# device the woman had dropped), delivery says LO-dying you-shall-die (the
# serpent: the doubling RESTORED in order to in NEGATED — the corpus first
# direct contradiction fowl a divine word)
m.spec_delta("mot tamut (gen_08 2:17: the penalty, doubled — the emphatic device the woman had dropped)",
             "LO-mot temutun (the serpent: the doubling RESTORED in order to be NEGATED — the corpus first direct contradiction of a divine word)")

# -------------------------- Gen.3.5 · SERPENT_COUNTER_THEORY ---------------
# כִּי יֹדֵעַ אֱלֹהִים כִּי בְּיוֹם אֲכָלְכֶם מִמֶּנּוּ וְנִפְקְחוּ
# עֵינֵיכֶם וִהְיִיתֶם כֵּאלֹהִים יֹדְעֵי טוֹב וָרָע
# "'For God doth know that in the day ye eat thereof, then your eyes shall
# be opened, and ye shall be as God, knowing good and evil.'"
m.step("Gen.3.5")
# ‹כִּי יֹדֵעַ אֱלֹהִים … וְנִפְקְחוּ … וִהְיִיתֶם כֵּאלֹהִים› (“that knows
# God … and-shall-be-opened … and-you-shall-be like-God”) — event: claim —
# agent serpent; theme were-opened-your-eyes, like-God
m.event("claim", agent="nachash", themes=["nifqechu_eineikhem", "ke_Elohim"])
# witness-tier presupposed read: first_slander_and_grammar_defence on
# serpent_speech — read, not installed
m.witness_read("serpent_speech", "first_slander_and_grammar_defence",
                cites=["Bereshit Rabbah 19:4", "Vayikra Rabbah 26:2"])

# -------------------------- Gen.3.6 · CREATURE_TEST_AND_TRIGGER ------------
# וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ לְמַאֲכָל וְכִי תַאֲוָה־הוּא לָעֵינַיִם
# וְנֶחְמָד הָעֵץ לְהַשְׂכִּיל וַתִּקַּח מִפִּרְיוֹ וַתֹּאכַל וַתִּתֵּן
# גַּם־לְאִישָׁהּ עִמָּהּ וַיֹּאכַל
# "And when the woman saw that the tree was good for food, and that it was a
# delight to the eyes, and that the tree was to be desired to make one wise,
# she took of the fruit thereof, and did eat; and she gave also unto her
# husband with her, and he did eat."
m.step("Gen.3.6")
# ‹וַתֵּרֶא הָאִשָּׁה כִּי טוֹב הָעֵץ לְמַאֲכָל› (“and-she-saw the-woman
# that good the-tree for-food”) — test PASS — oracle-word good, on the-tree-
# of-to-food
m.test("PASS", "tov", "ha_etz_le_maakhal")
# ‹וַתִּקַּח מִפִּרְיוֹ› (“and-she-took from-its-fruit”) — event: take —
# agent woman; theme fruit
m.event("take", agent="ishah", themes=["pri"])
# ‹וַתֹּאכַל› (“and-she-ate”) — event: eat — agent woman; theme fruit
m.event("eat", agent="ishah", themes=["pri"])
# ‹וַתִּתֵּן גַּם־לְאִישָׁהּ עִמָּהּ› (“and-she-gave also to-her-man with-
# her”) — event: give — agent woman; theme human
m.event("give", agent="ishah", themes=["adam"])
# ‹וַיֹּאכַל› (“and-he-ate”) — event: eat — agent human; theme fruit
m.event("eat", agent="adam", themes=["pri"])
# reads without prior install (flag, not fix): human
m.presupposed("adam")
# witness-tier presupposed read: three_properties_and_inclusive_gam on
# test_op — read, not installed
m.witness_read("test_op", "three_properties_and_inclusive_gam",
                cites=["Bereshit Rabbah 19:5"])

# -------------------------- Gen.3.7 · EYES_OPEN_FIRST_MANUFACTURE ----------
# וַתִּפָּקַחְנָה עֵינֵי שְׁנֵיהֶם וַיֵּדְעוּ כִּי עֵירֻמִּם הֵם
# וַיִּתְפְּרוּ עֲלֵה תְאֵנָה וַיַּעֲשׂוּ לָהֶם חֲגֹרֹת
# "And the eyes of them both were opened, and they knew that they were
# naked; and they sewed fig-leaves together, and made themselves girdles."
m.step("Gen.3.7")
# ‹וַתִּפָּקַחְנָה עֵינֵי שְׁנֵיהֶם› (“and-were-opened eyes-of the-two-of-
# them”) — event: open-eyes — theme eyes-of-both-of-them
m.event("open_eyes", themes=["einei_shneihem"])
# ‹וַיֵּדְעוּ כִּי עֵירֻמִּם הֵם› (“and-they-knew that naked they”) — event:
# know — agent both-of-them; theme naked
m.event("know", agent="shneihem", themes=["eirummim"])
# ‹וַיִּתְפְּרוּ עֲלֵה תְאֵנָה וַיַּעֲשׂוּ לָהֶם חֲגֹרֹת› (“and-they-sewed
# leaf-of fig and-they-made for-them girdles”) — event: make — agent both-
# of-them; theme girdles
m.event("make", agent="shneihem", themes=["chagorot"])
# ‹חֲגֹרֹת› (“girdles”) — the world gains: girdles
m.install("chagorot")
# witness-tier presupposed read: stripped_of_one_commandment on eyes_open —
# read, not installed
m.witness_read("eyes_open", "stripped_of_one_commandment",
                cites=["Bereshit Rabbah 19:6"])

# -------------------------- Gen.3.8 · VOICE_AND_HIDING ---------------------
# וַיִּשְׁמְעוּ אֶת־קוֹל יְהוָה אֱלֹהִים מִתְהַלֵּךְ בַּגָּן לְרוּחַ הַיּוֹם
# וַיִּתְחַבֵּא הָאָדָם וְאִשְׁתּוֹ מִפְּנֵי יְהוָה אֱלֹהִים בְּתוֹךְ עֵץ
# הַגָּן
# "And they heard the voice of the LORD God walking in the garden toward the
# cool of the day; and the man and his wife hid themselves from the presence
# of the LORD God amongst the trees of the garden."
m.step("Gen.3.8")
# ‹וַיִּשְׁמְעוּ אֶת־קוֹל יְהוָה אֱלֹהִים מִתְהַלֵּךְ בַּגָּן› (“and-they-
# heard obj-marker voice-of YHWH God walking-about in-the-garden”) — event:
# hear — agent both-of-them; theme voice-of-the-LORD-God
m.event("hear", agent="shneihem", themes=["qol_YHWH_Elohim"])
# ‹וַיִּתְחַבֵּא הָאָדָם וְאִשְׁתּוֹ … בְּתוֹךְ עֵץ הַגָּן› (“and-he-hid
# the-human and-his-wife … in-midst-of tree-of the-garden”) — event: hide —
# agent both-of-them; theme in-midst-of-tree-of-the-garden
m.event("hide", agent="shneihem", themes=["be_tokh_etz_ha_gan"])
# witness-tier presupposed read: presence_altitude_first_withdrawal on
# voice_event — read, not installed
m.witness_read("voice_event", "presence_altitude_first_withdrawal",
                cites=["Bereshit Rabbah 19:7", "Pesikta DeRav Kahana 5:3"])

# -------------------------- Gen.3.9 · FIRST_QUESTION -----------------------
# וַיִּקְרָא יְהוָה אֱלֹהִים אֶל־הָאָדָם וַיֹּאמֶר לוֹ אַיֶּכָּה
# "And the LORD God called unto the man, and said unto him: 'Where art
# thou?'"
m.step("Gen.3.9")
# ‹וַיִּקְרָא יְהוָה אֱלֹהִים אֶל־הָאָדָם› (“and-he-called YHWH God to the-
# human”) — event: call — agent the-LORD-God; theme human
m.event("call", agent="YHWH_Elohim", themes=["adam"])
# ‹אַיֶּכָּה› (“where-are-you”) — event: ask — agent the-LORD-God; theme
# where-are-you
m.event("ask", agent="YHWH_Elohim", themes=["ayeka"])
# witness-tier presupposed read: opportunity_to_confess_class on
# first_question — read, not installed
m.witness_read("first_question", "opportunity_to_confess_class",
                cites=["Bereshit Rabbah 19:11", "Sanhedrin 38b:11"])

# -------------------------- Gen.3.10 · TESTIMONY_FEAR ----------------------
# וַיֹּאמֶר אֶת־קֹלְךָ שָׁמַעְתִּי בַּגָּן וָאִירָא כִּי־עֵירֹם אָנֹכִי
# וָאֵחָבֵא
# "And he said: 'I heard Thy voice in the garden, and I was afraid, because
# I was naked; and I hid myself.'"
m.step("Gen.3.10")
# ‹וַיֹּאמֶר אֶת־קֹלְךָ שָׁמַעְתִּי בַּגָּן› (“and-he-said obj-marker your-
# voice I-heard in-the-garden”) — event: say — agent human; theme the-LORD-
# God
m.event("say", agent="adam", themes=["YHWH_Elohim"])
# ‹וָאִירָא כִּי־עֵירֹם אָנֹכִי וָאֵחָבֵא› (“and-I-feared that naked I and-
# I-hid”) — fact holds: testimony-feared-naked-hid(human)
m.fact("testimony_feared_naked_hid(adam)")

# -------------------------- Gen.3.11 · RULE_QUOTED_BACK --------------------
# וַיֹּאמֶר מִי הִגִּיד לְךָ כִּי עֵירֹם אָתָּה הֲמִן־הָעֵץ אֲשֶׁר
# צִוִּיתִיךָ לְבִלְתִּי אֲכָל־מִמֶּנּוּ אָכָלְתָּ
# "And He said: 'Who told thee that thou wast naked? Hast thou eaten of the
# tree, whereof I commanded thee that thou shouldest not eat?'"
m.step("Gen.3.11")
# ‹מִי הִגִּיד לְךָ … הֲמִן־הָעֵץ אֲשֶׁר צִוִּיתִיךָ לְבִלְתִּי
# אֲכָל־מִמֶּנּוּ אָכָלְתָּ› (“who told to-you … is-it-from the-tree which
# I-commanded-you not-to eat from-it you-have-eaten”) — event: ask — agent
# the-LORD-God; theme who-told, you-have-eaten
m.event("ask", agent="YHWH_Elohim", themes=["mi_higid", "akhalta"])

# -------------------------- Gen.3.12 · BLAME_CHAIN_ADMISSION_1 -------------
# וַיֹּאמֶר הָאָדָם הָאִשָּׁה אֲשֶׁר נָתַתָּה עִמָּדִי הִוא נָתְנָה־לִּי
# מִן־הָעֵץ וָאֹכֵל
# "And the man said: 'The woman whom Thou gavest to be with me, she gave me
# of the tree, and I did eat.'"
m.step("Gen.3.12")
# ‹הָאִשָּׁה אֲשֶׁר נָתַתָּה עִמָּדִי הִוא נָתְנָה־לִּי› (“the-woman which
# you-gave with-me she-ktiv-hu-qere-hi she-gave to-me”) — event: say — agent
# human; theme woman
m.event("say", agent="adam", themes=["ishah"])
# ‹וָאֹכֵל› (“and-I-ate”) — fact holds: admission-and-I-ate(human)
m.fact("admission_va_okhel(adam)")

# -------------------------- Gen.3.13 · ADMISSION_2_HAPAX_DECEIT ------------
# וַיֹּאמֶר יְהוָה אֱלֹהִים לָאִשָּׁה מַה־זֹּאת עָשִׂית וַתֹּאמֶר הָאִשָּׁה
# הַנָּחָשׁ הִשִּׁיאַנִי וָאֹכֵל
# "And the LORD God said unto the woman: 'What is this thou hast done?' And
# the woman said: 'The serpent beguiled me, and I did eat.'"
m.step("Gen.3.13")
# ‹מַה־זֹּאת עָשִׂית› (“what this you-have-done”) — event: ask — agent the-
# LORD-God; theme woman
m.event("ask", agent="YHWH_Elohim", themes=["ishah"])
# ‹הַנָּחָשׁ הִשִּׁיאַנִי› (“the-serpent deceived-me”) — event: say — agent
# woman; theme serpent
m.event("say", agent="ishah", themes=["nachash"])
# ‹וָאֹכֵל› (“and-I-ate”) — fact holds: admission-and-I-ate(woman)
m.fact("admission_va_okhel(ishah)")
# witness-grounded state (its own tier): absent_by_procedure on
# third_interrogation
m.witness_state("third_interrogation", "absent_by_procedure",
                cites=["Bereshit Rabbah 20:2"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'chagorot'}
    assert m.presupposed_set() == {'adam', 'gan', 'ha_etz', 'ishah', 'nachash'}
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
    assert sorted(m.WORLD["witnessed"]) == ['nachash_pre_curse_form', 'third_interrogation']
    assert m.WORLD["witnessed"]['nachash_pre_curse_form']["cites"] == ['Bereshit Rabbah 19:1', 'Sotah 9b:1', 'Tosefta Sotah 4:5']
    assert all('erect_legged_intended_king_baseline' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['third_interrogation']["cites"] == ['Bereshit Rabbah 20:2']
    assert all('absent_by_procedure' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('serpent_speech', 'first_slander_and_grammar_defence'), ('test_op', 'three_properties_and_inclusive_gam'), ('eyes_open', 'stripped_of_one_commandment'), ('voice_event', 'presence_altitude_first_withdrawal'), ('first_question', 'opportunity_to_confess_class')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 19:4', 'Vayikra Rabbah 26:2']
    assert all('first_slander_and_grammar_defence' not in f for f in m.WORLD["facts"])
    assert 'serpent_speech' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 19:5']
    assert all('three_properties_and_inclusive_gam' not in f for f in m.WORLD["facts"])
    assert 'test_op' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 19:6']
    assert all('stripped_of_one_commandment' not in f for f in m.WORLD["facts"])
    assert 'eyes_open' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 19:7', 'Pesikta DeRav Kahana 5:3']
    assert all('presence_altitude_first_withdrawal' not in f for f in m.WORLD["facts"])
    assert 'voice_event' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 19:11', 'Sanhedrin 38b:11']
    assert all('opportunity_to_confess_class' not in f for f in m.WORLD["facts"])
    assert 'first_question' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
