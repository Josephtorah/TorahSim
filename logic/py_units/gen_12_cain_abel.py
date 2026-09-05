#!/usr/bin/env python3
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
# ‹וְהָאָדָם יָדַע אֶת־חַוָּה› (“and-the-human knew obj-marker Chavah”)
# ‹אִשְׁתּוֹ וַתַּהַר וַתֵּלֶד› (“his-wife and-she-conceived and-she-bore”)
# ‹אֶת־קַיִן וַתֹּאמֶר קָנִיתִי› (“obj-marker Cain and-she-said I-have-
# acquired”)
# ‹אִישׁ אֶת־יְהוָה› (“man obj-marker YHWH”)
# "And the man knew Eve his wife; and she conceived and bore Cain, and said:
# 'I have gotten a man with the help of the LORD.'"
m.step("Gen.4.1")
# ‹וְהָאָדָם יָדַע אֶת־חַוָּה› (“and-the-human knew obj-marker Chavah”)
# ‹אִשְׁתּוֹ› (“his-wife”)
# — event: know — agent human; theme Chavah-Eve
m.event("know", agent="adam", themes=["chavah"])
# ‹וַתַּהַר וַתֵּלֶד אֶת־קַיִן› (“and-she-conceived and-she-bore obj-marker
# Cain”)
# — event: bear — agent Chavah-Eve; theme Cain
m.event("bear", agent="chavah", themes=["kayin"])
# ‹וַתֹּאמֶר קָנִיתִי אִישׁ› (“and-she-said I-have-acquired man”)
# ‹אֶת־יְהוָה› (“obj-marker YHWH”)
# — named: Cain := Kayin
m.name("kayin", "Kayin")
# reads without prior install (flag, not fix): human, Chavah-Eve
m.presupposed("adam", "chavah")

# -------------------------- Gen.4.2 · SECOND_BIRTH_PROFESSIONS -------------
# ‹וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו› (“and-she-added to-bear obj-marker his-
# brother”)
# ‹אֶת־הָבֶל וַיְהִי־הֶבֶל רֹעֵה› (“obj-marker Abel and-was Abel shepherd-
# of”)
# ‹צֹאן וְקַיִן הָיָה› (“flock and-Cain was”)
# ‹עֹבֵד אֲדָמָה› (“worker-of ground”)
# "And again she bore his brother Abel. And Abel was a keeper of sheep, but
# Cain was a tiller of the ground."
m.step("Gen.4.2")
# ‹וַתֹּסֶף לָלֶדֶת אֶת־אָחִיו› (“and-she-added to-bear obj-marker his-
# brother”)
# ‹אֶת־הָבֶל› (“obj-marker Abel”)
# — event: bear — agent Chavah-Eve; theme Abel
m.event("bear", agent="chavah", themes=["hevel"])
# ‹רֹעֵה צֹאן … עֹבֵד› (“shepherd-of flock … worker-of”)
# ‹אֲדָמָה› (“ground”)
# — fact holds: shepherd-flock(Abel); worker-of-ground(Cain)
m.fact("roeh_tzon(hevel)",
       "oved_adamah(kayin)")
# reads without prior install (flag, not fix): ground
m.presupposed("adamah")
# witness-tier presupposed read: twin_sisters_and_procreation_measure on
# double_et — read, not installed
m.witness_read("double_et", "twin_sisters_and_procreation_measure",
                cites=["Yevamot 62a:7", "Bereshit Rabbah 22:3", "Bereshit Rabbah 61:4"])

# -------------------------- Gen.4.3 · FIRST_OFFERING -----------------------
# ‹וַיְהִי מִקֵּץ יָמִים› (“and-it-was at-end-of days”)
# ‹וַיָּבֵא קַיִן מִפְּרִי› (“and-he-brought Cain from-fruit-of”)
# ‹הָאֲדָמָה מִנְחָה לַיהוָה› (“the-ground offering to-YHWH”)
# "And in process of time it came to pass, that Cain brought of the fruit of
# the ground an offering unto the LORD."
m.step("Gen.4.3")
# ‹וַיָּבֵא קַיִן מִפְּרִי› (“and-he-brought Cain from-fruit-of”)
# ‹הָאֲדָמָה מִנְחָה לַיהוָה› (“the-ground offering to-YHWH”)
# — event: bring — agent Cain; theme offering
m.event("bring", agent="kayin", themes=["minchah"])

# -------------------------- Gen.4.4 · SECOND_OFFERING_FAVOR ----------------
# ‹וְהֶבֶל הֵבִיא גַם־הוּא› (“and-Abel brought also he”)
# ‹מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן› (“from-firstlings-of his-flock and-
# from-their-fat”)
# ‹וַיִּשַׁע יְהוָה אֶל־הֶבֶל› (“and-he-regarded YHWH to Abel”)
# ‹וְאֶל־מִנְחָתוֹ› (“and-to his-offering”)
# "And Abel, he also brought of the firstlings of his flock and of the fat
# thereof. And the LORD had respect unto Abel and to his offering."
m.step("Gen.4.4")
# ‹וְהֶבֶל הֵבִיא גַם־הוּא› (“and-Abel brought also he”)
# ‹מִבְּכֹרוֹת צֹאנוֹ וּמֵחֶלְבֵהֶן› (“from-firstlings-of his-flock and-
# from-their-fat”)
# — event: bring — agent Abel; theme firstlings-of
m.event("bring", agent="hevel", themes=["bekhorot"])
# ‹וַיִּשַׁע יְהוָה אֶל־הֶבֶל› (“and-he-regarded YHWH to Abel”)
# ‹וְאֶל־מִנְחָתוֹ› (“and-to his-offering”)
# — test PASS — oracle-word gaze, on Abel-and-his-offering
m.test("PASS", "shaah", "hevel_u_minchato")
# witness-tier presupposed read: pursued_census_and_offering_species_law on
# minchah_accepted — read, not installed
m.witness_read("minchah_accepted", "pursued_census_and_offering_species_law",
                cites=["Pesikta DeRav Kahana 9:4", "Sifra, Shemini, Mekhilta DeMiluim II 31"])
# witness-tier presupposed read: peace_offering_arm on u_me_chelvehen —
# read, not installed
m.witness_read("u_me_chelvehen", "peace_offering_arm",
                cites=["Zevachim 116a:12", "Zevachim 116a:13", "Zevachim 116a:14", "Zevachim 116a:15"])

# -------------------------- Gen.4.5 · NON_REGARD_FIRST_ANGER ---------------
# ‹וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא› (“and-to Cain and-to his-offering not”)
# ‹שָׁעָה וַיִּחַר לְקַיִן› (“he-regarded and-he-burned to-Cain”)
# ‹מְאֹד וַיִּפְּלוּ פָּנָיו› (“very and-fell his-face”)
# "But unto Cain and to his offering He had not respect. And Cain was very
# wroth, and his countenance fell."
m.step("Gen.4.5")
# ‹וְאֶל־קַיִן וְאֶל־מִנְחָתוֹ לֹא› (“and-to Cain and-to his-offering not”)
# ‹שָׁעָה› (“he-regarded”)
# — fact holds: not-gaze-to-Cain-and-to-his-offering
m.fact("lo_shaah_el_kayin_ve_el_minchato")
# ‹וַיִּחַר לְקַיִן מְאֹד› (“and-he-burned to-Cain very”)
# ‹וַיִּפְּלוּ פָּנָיו› (“and-fell his-face”)
# — event: burn — agent Cain
m.event("burn", agent="kayin")

# -------------------------- Gen.4.6 · ANGER_DIAGNOSTIC ---------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־קָיִן› (“and-say YHWH to Cain”)
# ‹לָמָּה חָרָה לָךְ› (“why burned to-you”)
# ‹וְלָמָּה נָפְלוּ פָנֶיךָ› (“and-why fell your-face”)
# "And the LORD said unto Cain: 'Why art thou wroth? and why is thy
# countenance fallen?'"
m.step("Gen.4.6")
# ‹לָמָּה חָרָה לָךְ› (“why burned to-you”)
# ‹וְלָמָּה נָפְלוּ פָנֶיךָ› (“and-why fell your-face”)
# — event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])

# -------------------------- Gen.4.7 · COUNSEL_FIRST_IF ---------------------
# ‹הֲלוֹא אִם־תֵּיטִיב שְׂאֵת› (“is-it-not IF you-do-well uplift”)
# ‹וְאִם לֹא תֵיטִיב› (“and-if not you-do-well”)
# ‹לַפֶּתַח חַטָּאת רֹבֵץ› (“at-the-door sin crouching”)
# ‹וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה› (“and-to-you its-longing and-you”)
# ‹תִּמְשָׁל־בּוֹ› (“shall-rule in-it”)
# "'If thou doest well, shall it not be lifted up? and if thou doest not
# well, sin coucheth at the door; and unto thee is its desire, but thou
# mayest rule over it.'"
m.step("Gen.4.7")
# ‹אִם־תֵּיטִיב שְׂאֵת› (“IF you-do-well uplift”)
# — standing handler — if you-do-well(Cain) then uplift
m.handler("teitiv(kayin)",
          "seet")
# ‹וְאִם לֹא תֵיטִיב› (“and-if not you-do-well”)
# ‹לַפֶּתַח חַטָּאת רֹבֵץ› (“at-the-door sin crouching”)
# — standing handler — if not-you-do-well(Cain) then to-at-the-door-sin-
# crouching
m.handler("lo_teitiv(kayin)",
          "la_petach_chattat_rovetz")
# ‹וְאֵלֶיךָ תְּשׁוּקָתוֹ וְאַתָּה› (“and-to-you its-longing and-you”)
# ‹תִּמְשָׁל־בּוֹ› (“shall-rule in-it”)
# — the-LORD speaks a demand — LET?: you-shall-rule(Cain, in-the-sin)
m.declare("YHWH", "LET?",
          "timshol(kayin, ba_chattat)")
# witness-tier presupposed read: gender_mismatch_as_growth_curve on
# chatat_rovetz — read, not installed
m.witness_read("chatat_rovetz", "gender_mismatch_as_growth_curve",
                cites=["Bereshit Rabbah 22:6", "Berakhot 61a:27"])
# witness-tier presupposed read: torah_antidote_and_condition_syntax_law on
# conditional_op — read, not installed
m.witness_read("conditional_op", "torah_antidote_and_condition_syntax_law",
                cites=["Kiddushin 30b:4", "Kiddushin 30b:5", "Kiddushin 61b:9", "Sanhedrin 91b:7", "Niddah 30b:23"])
# witness-grounded state (its own tier): undecidable_parse_on_record on
# seet_cut_point
m.witness_state("seet_cut_point", "undecidable_parse_on_record",
                cites=["Bereshit Rabbah 80:6", "Sifrei Devarim 54:1"])

# -------------------------- Gen.4.8 · EMPTY_QUOTE_FIRST_MURDER -------------
# ‹וַיֹּאמֶר קַיִן אֶל־הֶבֶל› (“and-he-said Cain to Abel”)
# ‹אָחִיו וַיְהִי בִּהְיוֹתָם› (“his-brother and-it-was in-their-being”)
# ‹בַּשָּׂדֶה וַיָּקָם קַיִן› (“in-the-field and-he-rose Cain”)
# ‹אֶל־הֶבֶל אָחִיו וַיַּהַרְגֵהוּ› (“to Abel his-brother and-killed-him”)
# "And Cain spoke unto Abel his brother. And it came to pass, when they were
# in the field, that Cain rose up against Abel his brother, and slew him."
m.step("Gen.4.8")
# ‹וַיֹּאמֶר קַיִן אֶל־הֶבֶל› (“and-he-said Cain to Abel”)
# ‹אָחִיו› (“his-brother”)
# — event: say — agent Cain; theme Abel
m.event("say", agent="kayin", themes=["hevel"])
# ‹וַיָּקָם קַיִן אֶל־הֶבֶל› (“and-he-rose Cain to Abel”)
# ‹אָחִיו וַיַּהַרְגֵהוּ› (“his-brother and-killed-him”)
# — event: kill — agent Cain; theme Abel
m.event("kill", agent="kayin", themes=["hevel"])
# witness-tier presupposed read: filled_three_ways on empty_quote — read,
# not installed
m.witness_read("empty_quote", "filled_three_ways",
                cites=["Bereshit Rabbah 22:7", "Bereshit Rabbah 22:8"])

# -------------------------- Gen.4.9 · DOCKET_FIRST_LIE ---------------------
# ‹וַיֹּאמֶר יְהוָה אֶל־קַיִן› (“and-say YHWH to Cain”)
# ‹אֵי הֶבֶל אָחִיךָ› (“where Abel your-brother”)
# ‹וַיֹּאמֶר לֹא יָדַעְתִּי› (“and-say not I-know”)
# ‹הֲשֹׁמֵר אָחִי אָנֹכִי› (“the-keeper-of my-brother I”)
# "And the LORD said unto Cain: 'Where is Abel thy brother?' And he said: 'I
# know not; am I my brother's keeper?'"
m.step("Gen.4.9")
# ‹אֵי הֶבֶל אָחִיךָ› (“where Abel your-brother”)
# — event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹לֹא יָדַעְתִּי הֲשֹׁמֵר› (“not I-know the-keeper-of”)
# ‹אָחִי אָנֹכִי› (“my-brother I”)
# — fact holds: not-I-know-the-keeper-of-my-brother-I(Cain)
m.fact("lo_yadati_ha_shomer_achi_anokhi(kayin)")

# -------------------------- Gen.4.10 · BLOODS_CRY --------------------------
# ‹וַיֹּאמֶר מֶה עָשִׂיתָ› (“and-say what you-have-done”)
# ‹קוֹל דְּמֵי אָחִיךָ› (“voice-of bloods-of your-brother”)
# ‹צֹעֲקִים אֵלַי מִן־הָאֲדָמָה› (“crying to-me from the-ground”)
# "And He said: 'What hast thou done? the voice of thy brother's blood
# crieth unto Me from the ground.'"
m.step("Gen.4.10")
# ‹מֶה עָשִׂיתָ› (“what you-have-done”)
# — event: ask — agent the-LORD; theme Cain
m.event("ask", agent="YHWH", themes=["kayin"])
# ‹קוֹל דְּמֵי אָחִיךָ› (“voice-of bloods-of your-brother”)
# ‹צֹעֲקִים אֵלַי מִן־הָאֲדָמָה› (“crying to-me from the-ground”)
# — fact holds: all-bloods-of-your-brother-crying-out-from-the-ground
m.fact("kol_demei_achikha_tzoakim_min_ha_adamah")
# witness-tier presupposed read: capital_court_witness_warning on
# demei_plural — read, not installed
m.witness_read("demei_plural", "capital_court_witness_warning",
                cites=["Mishnah Sanhedrin 4:5", "Bereshit Rabbah 22:9", "Sanhedrin 37b:10", "Jerusalem Talmud Sanhedrin 4:9:1"])

# -------------------------- Gen.4.11 · CURSE_REACHES_HUMAN -----------------
# ‹וְעַתָּה אָרוּר אָתָּה› (“and-now CURSED you”)
# ‹מִן־הָאֲדָמָה אֲשֶׁר פָּצְתָה› (“from the-ground which opened”)
# ‹אֶת־פִּיהָ לָקַחַת אֶת־דְּמֵי› (“obj-marker her-mouth to-take obj-marker
# bloods-of”)
# ‹אָחִיךָ מִיָּדֶךָ› (“your-brother from-your-hand”)
# "'And now cursed art thou from the ground, which hath opened her mouth to
# receive thy brother's blood from thy hand.'"
m.step("Gen.4.11")
# ‹אָרוּר אָתָּה מִן־הָאֲדָמָה› (“CURSED you from the-ground”)
# — role assigned: Cain -> CURSED-from-the-ground
m.assign("kayin", "arur_min_ha_adamah")
# ‹אֲשֶׁר פָּצְתָה אֶת־פִּיהָ› (“which opened obj-marker her-mouth”)
# — fact holds: the-ground-opened-wide-her-mouth-taken-bloods-of(Cain)
m.fact("ha_adamah_patztah_piha_lakachat_demei(kayin)")

# -------------------------- Gen.4.12 · GROUND_STRIKE_WANDERER --------------
# ‹כִּי תַעֲבֹד אֶת־הָאֲדָמָה› (“when you-work obj-marker the-ground”)
# ‹לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ› (“not it-will-add to-give her-strength to-
# you”)
# ‹נָע וָנָד תִּהְיֶה› (“fugitive and-wanderer you-shall-be”)
# ‹בָאָרֶץ› (“in-the-earth”)
# "'When thou tillest the ground, it shall not henceforth yield unto thee
# her strength; a fugitive and a wanderer shalt thou be in the earth.'"
m.step("Gen.4.12")
# ‹לֹא־תֹסֵף תֵּת־כֹּחָהּ לָךְ› (“not it-will-add to-give her-strength to-
# you”)
# ‹… נָע וָנָד תִּהְיֶה› (“fugitive and-wanderer you-shall-be”)
# — fact holds: when-you-work-not-she-added-give-its-strength(ground, Cain);
# fugitive-and-wanderer-shall-be(Cain)
m.fact("ki_taavod_lo_tosef_tet_kochah(adamah, kayin)",
       "na_va_nad_tihyeh(kayin)")
# witness-tier presupposed read: half_remitted_visible_in_the_ink on
# na_va_nad_decree — read, not installed
m.witness_read("na_va_nad_decree", "half_remitted_visible_in_the_ink",
                cites=["Pesikta DeRav Kahana 24:11", "Sanhedrin 37b:12", "Vayikra Rabbah 10:5"])

# -------------------------- Gen.4.13 · PLEA_UNBEARABLE ---------------------
# ‹וַיֹּאמֶר קַיִן אֶל־יְהוָה› (“and-say Cain to YHWH”)
# ‹גָּדוֹל עֲוֺנִי מִנְּשֹׂא› (“great my-iniquity than-bearing”)
# "And Cain said unto the LORD: 'My punishment is greater than I can bear.'"
m.step("Gen.4.13")
# ‹גָּדוֹל עֲוֺנִי מִנְּשֹׂא› (“great my-iniquity than-bearing”)
# — event: plead — agent Cain; theme the-LORD
m.event("plead", agent="kayin", themes=["YHWH"])
# witness-grounded state (its own tier): three_recorded_readings on
# cain_plea
m.witness_state("cain_plea", "three_recorded_readings",
                cites=["Bereshit Rabbah 22:11", "Sanhedrin 101b:3", "Bereshit Rabbah 22:13"])

# -------------------------- Gen.4.14 · FEAR_OF_FINDERS ---------------------
# ‹הֵן גֵּרַשְׁתָּ אֹתִי› (“behold you-have-driven-out me”)
# ‹הַיּוֹם מֵעַל פְּנֵי› (“this-day from-upon face-of”)
# ‹הָאֲדָמָה וּמִפָּנֶיךָ אֶסָּתֵר› (“the-ground and-from-your-face I-shall-
# be-hidden”)
# ‹וְהָיִיתִי נָע וָנָד› (“and-I-shall-be fugitive and-wanderer”)
# ‹בָּאָרֶץ וְהָיָה כָל־מֹצְאִי› (“in-the-earth and-it-will-be all finding-
# me”)
# ‹יַהַרְגֵנִי› (“will-kill-me”)
# "'Behold, Thou hast driven me out this day from the face of the land; and
# from Thy face shall I be hid; and I shall be a fugitive and a wanderer in
# the earth; and it will come to pass, that whosoever findeth me will slay
# me.'"
m.step("Gen.4.14")
# ‹גֵּרַשְׁתָּ אֹתִי … וּמִפָּנֶיךָ› (“you-have-driven-out me … and-from-
# your-face”)
# ‹אֶסָּתֵר … כָל־מֹצְאִי יַהַרְגֵנִי› (“I-shall-be-hidden … all finding-me
# will-kill-me”)
# — fact holds: you-have-driven-out-me-and-from-your-face-I-shall-be-
# hidden(Cain); all-finder-will-kill-me-fear(Cain)
m.fact("gerashta_oti_u_mi_panekha_esater(kayin)",
       "khol_motzi_yahargeni_fear(kayin)")

# -------------------------- Gen.4.15 · SEVENFOLD_HANDLER_MARK --------------
# ‹וַיֹּאמֶר לוֹ יְהוָה› (“and-he-said to-him YHWH”)
# ‹לָכֵן כָּל־הֹרֵג קַיִן› (“therefore all killer-of Cain”)
# ‹שִׁבְעָתַיִם יֻקָּם וַיָּשֶׂם› (“sevenfold shall-be-avenged and-he-set”)
# ‹יְהוָה לְקַיִן אוֹת› (“YHWH for-Cain sign”)
# ‹לְבִלְתִּי הַכּוֹת־אֹתוֹ כָּל־מֹצְאוֹ› (“not-to strike him all finding-
# him”)
# "And the LORD said unto him: 'Therefore whosoever slayeth Cain, vengeance
# shall be taken on him sevenfold.' And the LORD set a sign for Cain, lest
# any finding him should smite him."
m.step("Gen.4.15")
# ‹כָּל־הֹרֵג קַיִן שִׁבְעָתַיִם› (“all killer-of Cain sevenfold”)
# ‹יֻקָּם› (“shall-be-avenged”)
# — standing handler — if killer-of(Cain) then sevenfold-shall-be-avenged
m.handler("horeg(kayin)",
          "shivatayim_yukam")
# ‹וַיָּשֶׂם יְהוָה לְקַיִן› (“and-he-set YHWH for-Cain”)
# ‹אוֹת› (“sign”)
# — fact holds: sign-to-Cain-so-as-not-strike(Cain)
m.fact("ot_le_kayin_levilti_hakot(kayin)")
# witness-tier presupposed read: discharged_at_the_flood on
# seven_generations_clause — read, not installed
m.witness_read("seven_generations_clause", "discharged_at_the_flood",
                cites=["Bereshit Rabbah 32:5"])

# -------------------------- Gen.4.16 · EXIT_EAST_SETTLED_IN_WANDERING ------
# ‹וַיֵּצֵא קַיִן מִלִּפְנֵי› (“and-he-went-out Cain from-before”)
# ‹יְהוָה וַיֵּשֶׁב בְּאֶרֶץ־נוֹד› (“YHWH and-he-settled in-land-of Nod-
# Wandering”)
# ‹קִדְמַת־עֵדֶן› (“east-of Eden”)
# "And Cain went out from the presence of the LORD, and dwelt in the land of
# Nod, on the east of Eden."
m.step("Gen.4.16")
# ‹וַיֵּצֵא … וַיֵּשֶׁב בְּאֶרֶץ־נוֹד› (“and-he-went-out … and-he-settled
# in-land-of Nod-Wandering”)
# ‹קִדְמַת־עֵדֶן› (“east-of Eden”)
# — event: go-out — agent Cain; theme land-of-Nod-Wandering-east-of-Eden
m.event("go_out", agent="kayin", themes=["eretz_nod_kidmat_eden"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam', 'adamah', 'chavah'}
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
    assert sorted(m.WORLD["witnessed"]) == ['cain_plea', 'seet_cut_point']
    assert m.WORLD["witnessed"]['cain_plea']["cites"] == ['Bereshit Rabbah 22:11', 'Sanhedrin 101b:3', 'Bereshit Rabbah 22:13']
    assert all('three_recorded_readings' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['seet_cut_point']["cites"] == ['Bereshit Rabbah 80:6', 'Sifrei Devarim 54:1']
    assert all('undecidable_parse_on_record' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('double_et', 'twin_sisters_and_procreation_measure'), ('minchah_accepted', 'pursued_census_and_offering_species_law'), ('u_me_chelvehen', 'peace_offering_arm'), ('chatat_rovetz', 'gender_mismatch_as_growth_curve'), ('conditional_op', 'torah_antidote_and_condition_syntax_law'), ('empty_quote', 'filled_three_ways'), ('demei_plural', 'capital_court_witness_warning'), ('na_va_nad_decree', 'half_remitted_visible_in_the_ink'), ('seven_generations_clause', 'discharged_at_the_flood')]
    assert m.WITNESS_READS[0]["cites"] == ['Yevamot 62a:7', 'Bereshit Rabbah 22:3', 'Bereshit Rabbah 61:4']
    assert all('twin_sisters_and_procreation_measure' not in f for f in m.WORLD["facts"])
    assert 'double_et' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Pesikta DeRav Kahana 9:4', 'Sifra, Shemini, Mekhilta DeMiluim II 31']
    assert all('pursued_census_and_offering_species_law' not in f for f in m.WORLD["facts"])
    assert 'minchah_accepted' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Zevachim 116a:12', 'Zevachim 116a:13', 'Zevachim 116a:14', 'Zevachim 116a:15']
    assert all('peace_offering_arm' not in f for f in m.WORLD["facts"])
    assert 'u_me_chelvehen' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 22:6', 'Berakhot 61a:27']
    assert all('gender_mismatch_as_growth_curve' not in f for f in m.WORLD["facts"])
    assert 'chatat_rovetz' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Kiddushin 30b:4', 'Kiddushin 30b:5', 'Kiddushin 61b:9', 'Sanhedrin 91b:7', 'Niddah 30b:23']
    assert all('torah_antidote_and_condition_syntax_law' not in f for f in m.WORLD["facts"])
    assert 'conditional_op' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 22:7', 'Bereshit Rabbah 22:8']
    assert all('filled_three_ways' not in f for f in m.WORLD["facts"])
    assert 'empty_quote' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Mishnah Sanhedrin 4:5', 'Bereshit Rabbah 22:9', 'Sanhedrin 37b:10', 'Jerusalem Talmud Sanhedrin 4:9:1']
    assert all('capital_court_witness_warning' not in f for f in m.WORLD["facts"])
    assert 'demei_plural' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Pesikta DeRav Kahana 24:11', 'Sanhedrin 37b:12', 'Vayikra Rabbah 10:5']
    assert all('half_remitted_visible_in_the_ink' not in f for f in m.WORLD["facts"])
    assert 'na_va_nad_decree' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 32:5']
    assert all('discharged_at_the_flood' not in f for f in m.WORLD["facts"])
    assert 'seven_generations_clause' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
