#!/usr/bin/env python3
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
