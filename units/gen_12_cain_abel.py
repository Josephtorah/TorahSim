#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וְהָאָדָם יָדַע אֶת־חַוָּה אִשְׁתּוֹ› (“and-the-human knew obj-marker
# Chavah his-wife”) — event: know — agent human; theme Chavah-Eve
m.event("know", agent="adam", themes=["chavah"])
# ‹וַתַּהַר וַתֵּלֶד אֶת־קַיִן› (“and-she-conceived and-she-bore obj-marker
# Cain”) — event: bear — agent Chavah-Eve; theme Cain
m.event("bear", agent="chavah", themes=["kayin"])
# ‹וַתֹּאמֶר קָנִיתִי אִישׁ אֶת־יְהוָה› (“and-she-said I-have-acquired man
# obj-marker YHWH”) — named: Cain := Kayin
m.name("kayin", "Kayin")
# reads without prior install (flag, not fix): human, Chavah-Eve
m.presupposed("adam", "chavah")

# -------------------------- Gen.4.2 · SECOND_BIRTH_PROFESSIONS -------------
# וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו אֶת־הָבֶל וַיְהִי־הֶבֶל רֹעֵה צֹאן וְקַיִן
# הָיָה עֹבֵד אֲדָמָה
# "And again she bore his brother Abel. And Abel was a keeper of sheep, but
# Cain was a tiller of the ground."
m.step("Gen.4.2")
# ‹וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו אֶת־הָבֶל› (“and-she-added to-bear obj-marker
# his-brother obj-marker Abel”) — event: bear — agent Chavah-Eve; theme Abel
m.event("bear", agent="chavah", themes=["hevel"])
# ‹רֹעֵה צֹאן … עֹבֵד אֲדָמָה› (“shepherd-of flock … worker-of ground”) —
# fact holds: shepherd-flock(Abel); worker-of-ground(Cain)
m.fact("roeh_tzon(hevel)",
       "oved_adamah(kayin)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")

# -------------------------- Gen.4.3 · FIRST_OFFERING -----------------------
# וַיְהִי מִקֵּץ יָמִים וַיָּבֵא קַיִן מִפְּרִי הָאֲדָמָה מִנְחָה לַיהוָה
# "And in process of time it came to pass, that Cain brought of the fruit of
# the ground an offering unto the LORD."
m.step("Gen.4.3")
# ‹וַיָּבֵא קַיִן מִפְּרִי הָאֲדָמָה מִנְחָה לַיהוָה› (“and-he-brought Cain
# from-fruit-of the-ground offering to-YHWH”) — event: bring — agent Cain;
# theme offering
m.event("bring", agent="kayin", themes=["minchah"])

# -------------------------- Gen.4.4 · SECOND_OFFERING_FAVOR ----------------
# וְהֶבֶל הֵבִיא גַם־הוּא מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן וַיִּשַׁע יְהוָה
# אֶל־הֶבֶל וְאֶל־מִנְחָתוֹ
# "And Abel, he also brought of the firstlings of his flock and of the fat
# thereof. And the LORD had respect unto Abel and to his offering."
m.step("Gen.4.4")
# ‹וְהֶבֶל הֵבִיא גַם־הוּא מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן› (“and-Abel
# brought also he from-firstlings-of his-flock and-from-their-fat”) — event:
# bring — agent Abel; theme firstlings-of
m.event("bring", agent="hevel", themes=["bekhorot"])
# ‹וַיִּשַׁע יְהוָה אֶל־הֶבֶל וְאֶל־מִנְחָתוֹ› (“and-he-regarded YHWH to
# Abel and-to his-offering”) — test PASS — oracle-word gaze, on Abel-and-
# his-offering
m.test("PASS", "shaah", "hevel_u_minchato")

# -------------------------- Gen.4.5 · NON_REGARD_FIRST_ANGER ---------------
# וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא שָׁעָה וַיִּחַר לְקַיִן מְאֹד וַיִּפְּלוּ
# פָּנָיו
# "But unto Cain and to his offering He had not respect. And Cain was very
# wroth, and his countenance fell."
m.step("Gen.4.5")
# ‹וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא שָׁעָה› (“and-to Cain and-to his-offering
# not he-regarded”) — fact holds: not-gaze-to-Cain-and-to-his-offering
m.fact("lo_shaah_el_kayin_ve_el_minchato")
# ‹וַיִּחַר לְקַיִן מְאֹד וַיִּפְּלוּ פָּנָיו› (“and-he-burned to-Cain very
# and-fell his-face”) — event: burn — agent Cain
m.event("burn", agent="kayin")

# -------------------------- Gen.4.6 · ANGER_DIAGNOSTIC ---------------------
# וַיֹּאמֶר יְהוָה אֶל־קָיִן לָמָּה חָרָה לָךְ וְלָמָּה נָפְלוּ פָנֶיךָ
# "And the LORD said unto Cain: 'Why art thou wroth? and why is thy
# countenance fallen?'"
m.step("Gen.4.6")
# ‹לָמָּה חָרָה לָךְ וְלָמָּה נָפְלוּ פָנֶיךָ› (“why burned to-you and-why
# fell your-face”) — event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])

# -------------------------- Gen.4.7 · COUNSEL_FIRST_IF ---------------------
# הֲלוֹא אִם־תֵּיטִיב שְׂאֵת וְאִם לֹא תֵיטִיב לַפֶּתַח חַטָּאת רֹבֵץ
# וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ
# "'If thou doest well, shall it not be lifted up? and if thou doest not
# well, sin coucheth at the door; and unto thee is its desire, but thou
# mayest rule over it.'"
m.step("Gen.4.7")
# ‹אִם־תֵּיטִיב שְׂאֵת› (“IF you-do-well uplift”) — standing handler — if
# you-do-well(Cain) then uplift
m.handler("teitiv(kayin)",
          "seet")
# ‹וְאִם לֹא תֵיטִיב לַפֶּתַח חַטָּאת רֹבֵץ› (“and-if not you-do-well at-
# the-door sin crouching”) — standing handler — if not-you-do-well(Cain)
# then to-at-the-door-sin-crouching
m.handler("lo_teitiv(kayin)",
          "la_petach_chattat_rovetz")
# ‹וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה תִּמְשָׁל־בּוֹ› (“and-to-you its-longing
# and-you shall-rule in-it”) — the-LORD speaks a demand — LET?: you-shall-
# rule(Cain, in-the-sin)
m.declare("YHWH", "LET?",
          "timshol(kayin, ba_chattat)")

# -------------------------- Gen.4.8 · EMPTY_QUOTE_FIRST_MURDER -------------
# וַיֹּאמֶר קַיִן אֶל־הֶבֶל אָחִיו וַיְהִי בִּהְיוֹתָם בַּשָּׂדֶה וַיָּקָם
# קַיִן אֶל־הֶבֶל אָחִיו וַיַּהַרְגֵהוּ
# "And Cain spoke unto Abel his brother. And it came to pass, when they were
# in the field, that Cain rose up against Abel his brother, and slew him."
m.step("Gen.4.8")
# ‹וַיֹּאמֶר קַיִן אֶל־הֶבֶל אָחִיו› (“and-he-said Cain to Abel his-
# brother”) — event: say — agent Cain; theme Abel
m.event("say", agent="kayin", themes=["hevel"])
# ‹וַיָּקָם קַיִן אֶל־הֶבֶל אָחִיו וַיַּהַרְגֵהוּ› (“and-he-rose Cain to
# Abel his-brother and-killed-him”) — event: kill — agent Cain; theme Abel
m.event("kill", agent="kayin", themes=["hevel"])

# -------------------------- Gen.4.9 · DOCKET_FIRST_LIE ---------------------
# וַיֹּאמֶר יְהוָה אֶל־קַיִן אֵי הֶבֶל אָחִיךָ וַיֹּאמֶר לֹא יָדַעְתִּי
# הֲשֹׁמֵר אָחִי אָנֹכִי
# "And the LORD said unto Cain: 'Where is Abel thy brother?' And he said: 'I
# know not; am I my brother's keeper?'"
m.step("Gen.4.9")
# ‹אֵי הֶבֶל אָחִיךָ› (“where Abel your-brother”) — event: ask — agent the-
# LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹לֹא יָדַעְתִּי הֲשֹׁמֵר אָחִי אָנֹכִי› (“not I-know the-keeper-of my-
# brother I”) — fact holds: not-I-know-the-keeper-of-my-brother-I(Cain)
m.fact("lo_yadati_ha_shomer_achi_anokhi(kayin)")

# -------------------------- Gen.4.10 · BLOODS_CRY --------------------------
# וַיֹּאמֶר מֶה עָשִׂיתָ קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן־הָאֲדָמָה
# "And He said: 'What hast thou done? the voice of thy brother's blood
# crieth unto Me from the ground.'"
m.step("Gen.4.10")
# ‹מֶה עָשִׂיתָ› (“what you-have-done”) — event: ask — agent the-LORD; theme
# Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹קוֹל דְּמֵי אָחִיךָ צֹעֲקִים אֵלַי מִן־הָאֲדָמָה› (“voice-of bloods-of
# your-brother crying to-me from the-ground”) — fact holds: all-bloods-of-
# your-brother-crying-out-from-the-ground
m.fact("kol_demei_achikha_tzoakim_min_ha_adamah")

# -------------------------- Gen.4.11 · CURSE_REACHES_HUMAN -----------------
# וְעַתָּה אָרוּר אָתָּה מִן־הָאֲדָמָה אֲשֶׁר פָּצְתָה אֶת־פִּיהָ לָקַחַת
# אֶת־דְּמֵי אָחִיךָ מִיָּדֶךָ
# "'And now cursed art thou from the ground, which hath opened her mouth to
# receive thy brother's blood from thy hand.'"
m.step("Gen.4.11")
# ‹אָרוּר אָתָּה מִן־הָאֲדָמָה› (“CURSED you from the-ground”) — role
# assigned: Cain -> CURSED-from-the-ground
m.assign("kayin", "arur_min_ha_adamah")
# ‹אֲשֶׁר פָּצְתָה אֶת־פִּיהָ› (“which opened obj-marker her-mouth”) — fact
# holds: the-ground-opened-wide-her-mouth-taken-bloods-of(Cain)
m.fact("ha_adamah_patztah_piha_lakachat_demei(kayin)")

# -------------------------- Gen.4.12 · GROUND_STRIKE_WANDERER --------------
# כִּי תַעֲבֹד אֶת־הָאֲדָמָה לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ נָע וָנָד תִּהְיֶה
# בָאָרֶץ
# "'When thou tillest the ground, it shall not henceforth yield unto thee
# her strength; a fugitive and a wanderer shalt thou be in the earth.'"
m.step("Gen.4.12")
# ‹לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ … נָע וָנָד תִּהְיֶה› (“not it-will-add to-
# give her-strength to-you … fugitive and-wanderer you-shall-be”) — fact
# holds: when-you-work-not-she-added-give-its-strength(ground, Cain);
# fugitive-and-wanderer-shall-be(Cain)
m.fact("ki_taavod_lo_tosef_tet_kochah(adamah, kayin)",
       "na_va_nad_tihyeh(kayin)")

# -------------------------- Gen.4.13 · PLEA_UNBEARABLE ---------------------
# וַיֹּאמֶר קַיִן אֶל־יְהוָה גָּדוֹל עֲוֺנִי מִנְּשֹׂא
# "And Cain said unto the LORD: 'My punishment is greater than I can bear.'"
m.step("Gen.4.13")
# ‹גָּדוֹל עֲוֺנִי מִנְּשֹׂא› (“great my-iniquity than-bearing”) — event:
# plead — agent Cain; theme the-LORD
m.event("plead", agent="kayin", themes=["YHWH"])

# -------------------------- Gen.4.14 · FEAR_OF_FINDERS ---------------------
# הֵן גֵּרַשְׁתָּ אֹתִי הַיּוֹם מֵעַל פְּנֵי הָאֲדָמָה וּמִפָּנֶיךָ אֶסָּתֵר
# וְהָיִיתִי נָע וָנָד בָּאָרֶץ וְהָיָה כָל־מֹצְאִי יַהַרְגֵנִי
# "'Behold, Thou hast driven me out this day from the face of the land; and
# from Thy face shall I be hid; and I shall be a fugitive and a wanderer in
# the earth; and it will come to pass, that whosoever findeth me will slay
# me.'"
m.step("Gen.4.14")
# ‹גֵּרַשְׁתָּ אֹתִי … וּמִפָּנֶיךָ אֶסָּתֵר … כָל־מֹצְאִי יַהַרְגֵנִי›
# (“you-have-driven-out me … and-from-your-face I-shall-be-hidden … all
# finding-me will-kill-me”) — fact holds: you-have-driven-out-me-and-from-
# your-face-I-shall-be-hidden(Cain); all-finder-will-kill-me-fear(Cain)
m.fact("gerashta_oti_u_mi_panekha_esater(kayin)",
       "khol_motzi_yahargeni_fear(kayin)")

# -------------------------- Gen.4.15 · SEVENFOLD_HANDLER_MARK --------------
# וַיֹּאמֶר לוֹ יְהוָה לָכֵן כָּל־הֹרֵג קַיִן שִׁבְעָתַיִם יֻקָּם וַיָּשֶׂם
# יְהוָה לְקַיִן אוֹת לְבִלְתִּי הַכּוֹת־אֹתוֹ כָּל־מֹצְאוֹ
# "And the LORD said unto him: 'Therefore whosoever slayeth Cain, vengeance
# shall be taken on him sevenfold.' And the LORD set a sign for Cain, lest
# any finding him should smite him."
m.step("Gen.4.15")
# ‹כָּל־הֹרֵג קַיִן שִׁבְעָתַיִם יֻקָּם› (“all killer-of Cain sevenfold
# shall-be-avenged”) — standing handler — if killer-of(Cain) then sevenfold-
# shall-be-avenged
m.handler("horeg(kayin)",
          "shivatayim_yukam")
# ‹וַיָּשֶׂם יְהוָה לְקַיִן אוֹת› (“and-he-set YHWH for-Cain sign”) — fact
# holds: sign-to-Cain-so-as-not-strike(Cain)
m.fact("ot_le_kayin_levilti_hakot(kayin)")

# -------------------------- Gen.4.16 · EXIT_EAST_SETTLED_IN_WANDERING ------
# וַיֵּצֵא קַיִן מִלִּפְנֵי יְהוָה וַיֵּשֶׁב בְּאֶרֶץ־נוֹד קִדְמַת־עֵדֶן
# "And Cain went out from the presence of the LORD, and dwelt in the land of
# Nod, on the east of Eden."
m.step("Gen.4.16")
# ‹וַיֵּצֵא … וַיֵּשֶׁב בְּאֶרֶץ־נוֹד קִדְמַת־עֵדֶן› (“and-he-went-out …
# and-he-settled in-land-of Nod-Wandering east-of Eden”) — event: go-out —
# agent Cain; theme land-of-Nod-Wandering-east-of-Eden
m.event("go_out", agent="kayin", themes=["eretz_nod_kidmat_eden"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adamah', 'chavah', 'adam'}
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
