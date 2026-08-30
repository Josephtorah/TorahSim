#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וַיֵּרֶד אַבְרָם מִצְרַיְמָה לָגוּר שָׁם› (“and-go-down Abram Egypt-ward
# to-turn-aside-from-the-road there”) — event: go-down — agent Abram
m.event("go_down", agent="avram")
# ‹כִּי־כָבֵד הָרָעָב בָּאָרֶץ› (“that heavy the-hunger in-earth”) — fact
# holds: that-heavy-the-hunger-in-the-earth
m.fact("ki_khaved_ha_raav_ba_aretz")
# reads without prior install (flag, not fix): mitzrayim
m.presupposed("mitzrayim")
# witness-tier presupposed read: paved_way_template_of_eleven_ink_pairs on
# descent_episode — read, not installed
m.witness_read("descent_episode", "paved_way_template_of_eleven_ink_pairs",
                cites=["Bereshit Rabbah 40:6", "Yevamot 13b:6"])

# -------------------------- Gen.12.11 · THE_FIRST_SPEECH_IS_FEAR_AND_BEAUTY -
# וַיְהִי כַּאֲשֶׁר הִקְרִיב לָבוֹא מִצְרָיְמָה וַיֹּאמֶר אֶל־שָׂרַי
# אִשְׁתּוֹ הִנֵּה־נָא יָדַעְתִּי כִּי אִשָּׁה יְפַת־מַרְאֶה אָתְּ
# "And it came to pass, when he was come near to enter into Egypt, that he
# said unto Sarai his wife: 'Behold now, I know that thou art a fair woman
# to look upon.'"
m.step("Gen.12.11")
# ‹וַיֹּאמֶר אֶל־שָׂרַי אִשְׁתּוֹ› (“and-say to Sarai woman-him/its”) —
# event: say — agent Abram
m.event("say", agent="avram")
# ‹הִנֵּה־נָא יָדַעְתִּי כִּי אִשָּׁה יְפַת־מַרְאֶה אָתְּ› (“behold please
# know that woman beautiful appearance thou-and-thee”) — fact holds: behold-
# please-know-that-woman-beautiful-appearance-at
m.fact("hinneh_na_yadati_ki_ishah_yefat_mareh_at")

# -------------------------- Gen.12.12 · THE_FEAR_FORECAST ------------------
# וְהָיָה כִּי־יִרְאוּ אֹתָךְ הַמִּצְרִים וְאָמְרוּ אִשְׁתּוֹ זֹאת וְהָרְגוּ
# אֹתִי וְאֹתָךְ יְחַיּוּ
# "And it will come to pass, when the Egyptians shall see thee, that they
# will say: This is his wife; and they will kill me, but thee they will keep
# alive."
m.step("Gen.12.12")
# ‹וְהָרְגוּ אֹתִי וְאֹתָךְ יְחַיּוּ› (“and-smite-with-deadly-intent obj-
# marker-me/my and-obj-marker-you/your live”) — fact holds: and-smite-with-
# deadly-intent-me-and-otakh-live
m.fact("ve_hargu_oti_ve_otakh_yechayu")

# -------------------------- Gen.12.13 · THE_REQUEST_WITH_NO_REPLY ----------
# אִמְרִי־נָא אֲחֹתִי אָתְּ לְמַעַן יִיטַב־לִי בַעֲבוּרֵךְ וְחָיְתָה
# נַפְשִׁי בִּגְלָלֵךְ
# "Say, I pray thee, thou art my sister; that it may be well with me for thy
# sake, and that my soul may live because of thee.'"
m.step("Gen.12.13")
# ‹אִמְרִי־נָא אֲחֹתִי אָתְּ› (“say please sister-me/my thou-and-thee”) —
# Abram speaks a demand — LET: say(Sarai, achoti-hi)
m.declare("avram", "LET",
          "imri(saray, achoti_hi)")
# ‹לְמַעַן יִיטַב־לִי בַעֲבוּרֵךְ וְחָיְתָה נַפְשִׁי בִּגְלָלֵךְ› (“so-that
# do-well to-me/my in-crossed-you/your and-live living-being-me/my in-
# circumstance-you/your”) — fact holds: so-that-do-well-to-me-vaavurekh-and-
# chaytah-nafshi
m.fact("lemaan_yitav_li_vaavurekh_ve_chaytah_nafshi")
# witness-tier presupposed read: consent_established_by_one_word on
# request_particle — read, not installed
m.witness_read("request_particle", "consent_established_by_one_word",
                cites=["Bereshit Rabbah 52:4", "Sanhedrin 39b:21"])

# -------------------------- Gen.12.14 · THE_SEEING -------------------------
# וַיְהִי כְּבוֹא אַבְרָם מִצְרָיְמָה וַיִּרְאוּ הַמִּצְרִים אֶת־הָאִשָּׁה
# כִּי־יָפָה הִוא מְאֹד
# "And it came to pass, that, when Abram was come into Egypt, the Egyptians
# beheld the woman that she was very fair."
m.step("Gen.12.14")
# ‹וַיִּרְאוּ הַמִּצְרִים אֶת־הָאִשָּׁה› (“and-see the-Egyptian obj-marker
# the-woman”) — event: see — agent the-Egyptian; theme the-woman
m.event("see", agent="ha_mitzrim", themes=["ha_ishah"])
# ‹כִּי־יָפָה הִוא מְאֹד› (“that beautiful he/it very”) — fact holds: that-
# yafah-hi-very
m.fact("ki_yafah_hi_meod")

# -------------------------- Gen.12.15 · THE_PRAISE_AND_THE_PASSIVE_TAKING --
# וַיִּרְאוּ אֹתָהּ שָׂרֵי פַרְעֹה וַיְהַלְלוּ אֹתָהּ אֶל־פַּרְעֹה וַתֻּקַּח
# הָאִשָּׁה בֵּית פַּרְעֹה
# "And the princes of Pharaoh saw her, and praised her to Pharaoh; and the
# woman was taken into Pharaoh's house."
m.step("Gen.12.15")
# ‹וַיִּרְאוּ אֹתָהּ שָׂרֵי פַרְעֹה› (“and-see obj-marker-her/its officer
# Pharaoh”) — event: see — agent sarei-Pharaoh; theme the-woman
m.event("see", agent="sarei_faro", themes=["ha_ishah"])
# ‹וַיְהַלְלוּ אֹתָהּ אֶל־פַּרְעֹה› (“and-be-clear obj-marker-her/its to
# Pharaoh”) — event: praise — agent sarei-Pharaoh
m.event("praise", agent="sarei_faro")
# ‹וַתֻּקַּח הָאִשָּׁה בֵּית פַּרְעֹה› (“and-take the-woman house Pharaoh”)
# — event: take — theme the-woman
m.event("take", themes=["ha_ishah"])

# -------------------------- Gen.12.16 · THE_PAYMENT_FOR_HER_SAKE -----------
# וּלְאַבְרָם הֵיטִיב בַּעֲבוּרָהּ וַיְהִי־לוֹ צֹאן־וּבָקָר וַחֲמֹרִים
# וַעֲבָדִים וּשְׁפָחֹת וַאֲתֹנֹת וּגְמַלִּים
# "And he dealt well with Abram for her sake; and he had sheep, and oxen,
# and he-asses, and men-servants, and maid-servants, and she-asses, and
# camels."
m.step("Gen.12.16")
# ‹וּלְאַבְרָם הֵיטִיב בַּעֲבוּרָהּ› (“and-to-Abram do-well in-crossed-
# her/its”) — event: do-good — agent Pharaoh
m.event("do_good", agent="paro")
# ‹וַיְהִי־לוֹ צֹאן־וּבָקָר וַחֲמֹרִים וַעֲבָדִים וּשְׁפָחֹת וַאֲתֹנֹת
# וּגְמַלִּים› (“and-be to-him/its flock and-herd and-male-ass and-servant
# and-female-slave and-female-donkey and-camel”) — fact holds: and-be-not-
# flock-and-herd-and-male-ass-and-servant-and-shfachot-and-female-donkey-
# and-camel
m.fact("va_yehi_lo_tzon_u_vaqar_va_chamorim_va_avadim_u_shfachot_va_atonot_u_gemalim")

# -------------------------- Gen.12.17 · THE_PLAGUE_WITHOUT_A_WORD ----------
# וַיְנַגַּע יְהוָה אֶת־פַּרְעֹה נְגָעִים גְּדֹלִים וְאֶת־בֵּיתוֹ עַל־דְּבַר
# שָׂרַי אֵשֶׁת אַבְרָם
# "And the LORD plagued Pharaoh and his house with great plagues because of
# Sarai Abram's wife."
m.step("Gen.12.17")
# ‹וַיְנַגַּע יְהוָה אֶת־פַּרְעֹה נְגָעִים גְּדֹלִים וְאֶת־בֵּיתוֹ› (“and-
# touch YHWH obj-marker Pharaoh blow great and-obj-marker house-him/its”) —
# event: plague — agent the-LORD; theme Pharaoh-and-veito
m.event("plague", agent="YHWH", themes=["paro_u_veito"])
# ‹עַל־דְּבַר שָׂרַי אֵשֶׁת אַבְרָם› (“over word/thing Sarai woman Abram”) —
# fact holds: over-word/thing-Sarai-woman-Abram
m.fact("al_devar_saray_eshet_avram")
# witness-tier presupposed read: named_disease_carried_into_divorce_law on
# affliction_op — read, not installed
m.witness_read("affliction_op", "named_disease_carried_into_divorce_law",
                cites=["Bereshit Rabbah 41:2", "Jerusalem Talmud Ketubot 7:9:3", "Vayikra Rabbah 16:1", "Arakhin 16a:9"])

# -------------------------- Gen.12.18 · THE_KINGS_QUESTIONS_IN_THE_GARDENS_FORM -
# וַיִּקְרָא פַרְעֹה לְאַבְרָם וַיֹּאמֶר מַה־זֹּאת עָשִׂיתָ לִּי לָמָּה
# לֹא־הִגַּדְתָּ לִּי כִּי אִשְׁתְּךָ הִוא
# "And Pharaoh called Abram, and said: 'What is this that thou hast done
# unto me? why didst thou not tell me that she was thy wife?'"
m.step("Gen.12.18")
# ‹וַיִּקְרָא פַרְעֹה לְאַבְרָם וַיֹּאמֶר מַה־זֹּאת עָשִׂיתָ לִּי› (“and-
# call Pharaoh to-Abram and-say what this make to-me/my”) — event: say —
# agent Pharaoh
m.event("say", agent="paro")

# -------------------------- Gen.12.19 · THE_CONFESSION_AND_THE_COUNTER_COMMANDS -
# לָמָה אָמַרְתָּ אֲחֹתִי הִוא וָאֶקַּח אֹתָהּ לִי לְאִשָּׁה וְעַתָּה הִנֵּה
# אִשְׁתְּךָ קַח וָלֵךְ
# "Why saidst thou: She is my sister? so that I took her to be my wife; now
# therefore behold thy wife, take her, and go thy way.'"
m.step("Gen.12.19")
# ‹אָמַרְתָּ אֲחֹתִי הִוא וָאֶקַּח אֹתָהּ לִי לְאִשָּׁה› (“say sister-me/my
# he/it and-take obj-marker-her/its to-me/my to-woman”) — fact holds: say-
# achoti-hi; and-take-her-to-me-to-woman
m.fact("amarta_achoti_hi",
       "va_eqach_otah_li_le_ishah")
# ‹הִנֵּה אִשְׁתְּךָ קַח› (“behold woman-you/your take”) — Pharaoh speaks a
# demand — LET: take(Abram, thou-and-thee-his-wife)
m.declare("paro", "LET",
          "qach(avram, et_ishto)")
# ‹וָלֵךְ› (“and-go”) — Pharaoh speaks a demand — LET: go(Abram)
m.declare("paro", "LET",
          "lekh(avram)")

# -------------------------- Gen.12.20 · THE_ESCORTED_EXPULSION -------------
# וַיְצַו עָלָיו פַּרְעֹה אֲנָשִׁים וַיְשַׁלְּחוּ אֹתוֹ וְאֶת־אִשְׁתּוֹ
# וְאֶת־כָּל־אֲשֶׁר־לוֹ
# "And Pharaoh gave men charge concerning him; and they brought him on the
# way, and his wife, and all that he had."
m.step("Gen.12.20")
# ‹וַיְצַו עָלָיו פַּרְעֹה אֲנָשִׁים› (“and-command over-him/its Pharaoh
# man”) — event: command — agent Pharaoh; theme man
m.event("command", agent="paro", themes=["anashim"])
# ‹וַיְשַׁלְּחוּ אֹתוֹ וְאֶת־אִשְׁתּוֹ וְאֶת־כָּל־אֲשֶׁר־לוֹ› (“and-send
# obj-marker-him/its and-obj-marker woman-him/its and-obj-marker all which
# to-him/its”) — event: send-away — agent man; theme Abram-and-his-wife-and-
# all-which-not
m.event("send_away", agent="anashim", themes=["avram_ve_ishto_ve_khol_asher_lo"])
# witness-tier presupposed read: four_steps_priced_at_four_hundred_years on
# escort_and_release — read, not installed
m.witness_read("escort_and_release", "four_steps_priced_at_four_hundred_years",
                cites=["Sotah 46b:14", "Mekhilta DeRabbi Shimon Ben Yochai 3:1"])

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
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('descent_episode', 'paved_way_template_of_eleven_ink_pairs'), ('request_particle', 'consent_established_by_one_word'), ('affliction_op', 'named_disease_carried_into_divorce_law'), ('escort_and_release', 'four_steps_priced_at_four_hundred_years')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 40:6', 'Yevamot 13b:6']
    assert all('paved_way_template_of_eleven_ink_pairs' not in f for f in m.WORLD["facts"])
    assert 'descent_episode' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 52:4', 'Sanhedrin 39b:21']
    assert all('consent_established_by_one_word' not in f for f in m.WORLD["facts"])
    assert 'request_particle' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 41:2', 'Jerusalem Talmud Ketubot 7:9:3', 'Vayikra Rabbah 16:1', 'Arakhin 16a:9']
    assert all('named_disease_carried_into_divorce_law' not in f for f in m.WORLD["facts"])
    assert 'affliction_op' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Sotah 46b:14', 'Mekhilta DeRabbi Shimon Ben Yochai 3:1']
    assert all('four_steps_priced_at_four_hundred_years' not in f for f in m.WORLD["facts"])
    assert 'escort_and_release' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
