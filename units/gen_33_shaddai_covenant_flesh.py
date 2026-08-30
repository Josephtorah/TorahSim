#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# ‹וַיֵּרָא יְהוָה אֶל־אַבְרָם› (“and-see YHWH to Abram”) — event: appear —
# agent the-LORD
m.event("appear", agent="YHWH")
# ‹אֲנִי־אֵל שַׁדַּי› (“strength Almighty”) — fact holds: ani-to-shaddai
m.fact("ani_el_shaddai")
# ‹הִתְהַלֵּךְ לְפָנַי וֶהְיֵה תָמִים› (“walk/go to-face-me/my and-be
# entire”) — the-LORD speaks a demand — LET: walk/go-and-heyeh-entire(Abram,
# before-Me)
m.declare("YHWH", "LET",
          "hithalekh_ve_heyeh_tamim(avram, lefanai)")
# witness-tier presupposed read: wholeness_pending_the_act on
# tamim_condition — read, not installed
m.witness_read("tamim_condition", "wholeness_pending_the_act",
                cites=["Mishnah Nedarim 3:11", "Bereshit Rabbah 46:1"])

# -------------------------- Gen.17.2 · THE_COHORTATIVE_COVENANT ------------
# וְאֶתְּנָה בְרִיתִי בֵּינִי וּבֵינֶךָ וְאַרְבֶּה אוֹתְךָ בִּמְאֹד מְאֹד
# "And I will make My covenant between Me and thee, and will multiply thee
# exceedingly.'"
m.step("Gen.17.2")
# ‹וְאֶתְּנָה בְרִיתִי בֵּינִי וּבֵינֶךָ וְאַרְבֶּה אוֹתְךָ בִּמְאֹד מְאֹד›
# (“and-set covenant-me/my between-me/my and-between-you/your and-multiply
# obj-marker-you/your in-very very”) — fact holds: and-etnah-vriti-beini-
# and-veinekha; and-I-will-multiply-otkha-bi-very-very
m.fact("ve_etnah_vriti_beini_u_veinekha",
       "ve_arbeh_otkha_bi_meod_meod")

# -------------------------- Gen.17.3 · THE_FIRST_FALL_AND_THE_SPEAK_FRAME --
# וַיִּפֹּל אַבְרָם עַל־פָּנָיו וַיְדַבֵּר אִתּוֹ אֱלֹהִים לֵאמֹר
# "And Abram fell on his face; and God talked with him, saying:"
m.step("Gen.17.3")
# ‹וַיִּפֹּל אַבְרָם עַל־פָּנָיו› (“and-fall Abram over face-him/its”) —
# event: fall — agent Abram
m.event("fall", agent="avram")
# ‹וַיְדַבֵּר אִתּוֹ אֱלֹהִים לֵאמֹר› (“and-speak with-him/its God to-say”)
# — event: speak — agent God
m.event("speak", agent="elohim")

# -------------------------- Gen.17.4 · THE_FATHER_OF_MULTITUDE_CHARTER -----
# אֲנִי הִנֵּה בְרִיתִי אִתָּךְ וְהָיִיתָ לְאַב הֲמוֹן גּוֹיִם
# "'As for Me, behold, My covenant is with thee, and thou shalt be the
# father of a multitude of nations."
m.step("Gen.17.4")
# ‹אֲנִי הִנֵּה בְרִיתִי אִתָּךְ וְהָיִיתָ לְאַב הֲמוֹן גּוֹיִם› (“behold
# covenant-me/my with-you/your and-be to-father noise nation”) — fact holds:
# ani-hineh-vriti-with-you; and-be-to-father-noise-nation
m.fact("ani_hineh_vriti_itakh",
       "ve_hayita_le_av_hamon_goyim")

# -------------------------- Gen.17.5 · AVRAM_RETIRED_AVRAHAM_DECREED -------
# וְלֹא־יִקָּרֵא עוֹד אֶת־שִׁמְךָ אַבְרָם וְהָיָה שִׁמְךָ אַבְרָהָם כִּי
# אַב־הֲמוֹן גּוֹיִם נְתַתִּיךָ
# "Neither shall thy name any more be called Abram, but thy name shall be
# Abraham; for the father of a multitude of nations have I made thee."
m.step("Gen.17.5")
# ‹וְלֹא־יִקָּרֵא עוֹד אֶת־שִׁמְךָ אַבְרָם וְהָיָה שִׁמְךָ אַבְרָהָם› (“and-
# not call still/again obj-marker name-you/your Abram and-be name-you/your
# Abraham”) — fact holds: not-call-still/again-shimkha-Abram; and-was-
# shimkha-Abraham
m.fact("lo_yiqare_od_shimkha_avram",
       "ve_hayah_shimkha_avraham")
# witness-tier presupposed read: charter_of_the_acronym_rule on av_hamon —
# read, not installed
m.witness_read("av_hamon", "charter_of_the_acronym_rule",
                cites=["Bereshit Rabbah 46:7", "Shabbat 105a:2"])
# witness-grounded state (its own tier):
# enforced_naming_law_and_counter_rule on rename_operator
m.witness_state("rename_operator", "enforced_naming_law_and_counter_rule",
                cites=["Berakhot 13a:8", "Bereshit Rabbah 46:8", "Tosefta Berakhot 1:15", "Berakhot 13a:10"])

# -------------------------- Gen.17.6 · FRUITFULNESS_AND_KINGS --------------
# וְהִפְרֵתִי אֹתְךָ בִּמְאֹד מְאֹד וּנְתַתִּיךָ לְגוֹיִם וּמְלָכִים מִמְּךָ
# יֵצֵאוּ
# "And I will make thee exceeding fruitful, and I will make nations of thee,
# and kings shall come out of thee."
m.step("Gen.17.6")
# ‹וְהִפְרֵתִי אֹתְךָ בִּמְאֹד מְאֹד … וּמְלָכִים מִמְּךָ יֵצֵאוּ› (“and-be-
# fruitful obj-marker-you/your in-very very … and-king from-you/your bring-
# forth”) — fact holds: and-be-fruitful-otkha-bi-very-very; and-king-mimkha-
# bring-forth
m.fact("ve_hifreti_otkha_bi_meod_meod",
       "u_melakhim_mimkha_yetzeu")

# -------------------------- Gen.17.7 · THE_EVERLASTING_COVENANT ------------
# וַהֲקִמֹתִי אֶת־בְּרִיתִי בֵּינִי וּבֵינֶךָ וּבֵין זַרְעֲךָ אַחֲרֶיךָ
# לְדֹרֹתָם לִבְרִית עוֹלָם לִהְיוֹת לְךָ לֵאלֹהִים וּלְזַרְעֲךָ אַחֲרֶיךָ
# "And I will establish My covenant between Me and thee and thy seed after
# thee throughout their generations for an everlasting covenant, to be a God
# unto thee and to thy seed after thee."
m.step("Gen.17.7")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי … לִבְרִית עוֹלָם לִהְיוֹת לְךָ לֵאלֹהִים›
# (“and-arise obj-marker covenant-me/my … to-covenant forever to-be to-
# you/your to-God”) — fact holds: and-arise-obj-marker-My-covenant-to-me-
# vrit-forever; to-me-being-to-you-to-lohim
m.fact("va_haqimoti_et_briti_li_vrit_olam",
       "li_heyot_lekha_le_lohim")
# witness-tier presupposed read: three_family_laws on covenant_clause —
# read, not installed
m.witness_read("covenant_clause", "three_family_laws",
                cites=["Yevamot 42a:6", "Yevamot 100b:9", "Yevamot 64a:2"])
# witness-tier presupposed read: surviving_analogy_of_three_weighed on
# dorot_token — read, not installed
m.witness_read("dorot_token", "surviving_analogy_of_three_weighed",
                cites=["Shabbat 132a:6", "Shabbat 132a:8", "Shabbat 132a:10"])

# -------------------------- Gen.17.8 · THE_EVERLASTING_POSSESSION ----------
# וְנָתַתִּי לְךָ וּלְזַרְעֲךָ אַחֲרֶיךָ אֵת אֶרֶץ מְגֻרֶיךָ אֵת כָּל־אֶרֶץ
# כְּנַעַן לַאֲחֻזַּת עוֹלָם וְהָיִיתִי לָהֶם לֵאלֹהִים
# "And I will give unto thee, and to thy seed after thee, the land of thy
# sojournings, all the land of Canaan, for an everlasting possession; and I
# will be their God.'"
m.step("Gen.17.8")
# ‹וְנָתַתִּי … אֵת אֶרֶץ מְגֻרֶיךָ … לַאֲחֻזַּת עוֹלָם וְהָיִיתִי לָהֶם
# לֵאלֹהִים› (“and-set … obj-marker earth sojourning-you/your … to-
# something-seized forever and-be to-them/their to-God”) — fact holds: and-
# set-obj-marker-earth-megurekha-to-something-seized-forever; and-be-to-
# them-to-lohim
m.fact("ve_natati_et_eretz_megurekha_la_achuzat_olam",
       "ve_hayiti_lahem_le_lohim")
# witness-tier presupposed read: conditioned_on_the_next_verse on land_grant
# — read, not installed
m.witness_read("land_grant", "conditioned_on_the_next_verse",
                cites=["Bereshit Rabbah 46:9"])

# -------------------------- Gen.17.9 · THE_GUARDED_KEEP_COMMAND ------------
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם וְאַתָּה אֶת־בְּרִיתִי תִשְׁמֹר אַתָּה
# וְזַרְעֲךָ אַחֲרֶיךָ לְדֹרֹתָם
# "And God said unto Abraham: 'And as for thee, thou shalt keep My covenant,
# thou, and thy seed after thee throughout their generations."
m.step("Gen.17.9")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם› (“and-say God to Abraham”) — event: say
# — agent God
m.event("say", agent="elohim")
# ‹וְאַתָּה אֶת־בְּרִיתִי תִשְׁמֹר› (“and-you obj-marker covenant-me/my
# keep/guard”) — God speaks a demand — LET?: keep/guard(Abraham, obj-marker-
# My-covenant)
m.declare("elohim", "LET?",
          "tishmor(avraham, et_briti)")

# -------------------------- Gen.17.10 · THE_LAW_ANNOUNCED ------------------
# זֹאת בְּרִיתִי אֲשֶׁר תִּשְׁמְרוּ בֵּינִי וּבֵינֵיכֶם וּבֵין זַרְעֲךָ
# אַחֲרֶיךָ הִמּוֹל לָכֶם כָּל־זָכָר
# "This is My covenant, which ye shall keep, between Me and you and thy seed
# after thee: every male among you shall be circumcised."
m.step("Gen.17.10")
# ‹זֹאת בְּרִיתִי אֲשֶׁר תִּשְׁמְרוּ … הִמּוֹל לָכֶם כָּל־זָכָר› (“this
# covenant-me/my which keep/guard … circumcise to-you/your(pl) all male”) —
# fact holds: this-My-covenant-which-tishmeru; circumcise-lakhem-all-male
m.fact("zot_briti_asher_tishmeru",
       "himol_lakhem_kol_zakhar")
# witness-tier presupposed read: three_tier_enforcement_cascade on
# circumcision_command — read, not installed
m.witness_read("circumcision_command", "three_tier_enforcement_cascade",
                cites=["Kiddushin 29a:11", "Avodah Zarah 26b:12", "Jerusalem Talmud Kiddushin 1:7:2"])

# -------------------------- Gen.17.11 · THE_SIGN_IN_THE_FLESH --------------
# וּנְמַלְתֶּם אֵת בְּשַׂר עָרְלַתְכֶם וְהָיָה לְאוֹת בְּרִית בֵּינִי
# וּבֵינֵיכֶם
# "And ye shall be circumcised in the flesh of your foreskin; and it shall
# be a token of a covenant betwixt Me and you."
m.step("Gen.17.11")
# ‹וּנְמַלְתֶּם אֵת בְּשַׂר עָרְלַתְכֶם וְהָיָה לְאוֹת בְּרִית› (“and-be-
# circumcised obj-marker flesh foreskin-you/your(pl) and-be to-signs
# covenant”) — fact holds: and-be-circumcised-obj-marker-flesh-arlatkhem;
# and-was-to-signs-brit
m.fact("u_nemaltem_et_besar_arlatkhem",
       "ve_hayah_le_ot_brit")
# witness-tier presupposed read: objected_to_and_answered on
# abraham_own_analogy — read, not installed
m.witness_read("abraham_own_analogy", "objected_to_and_answered",
                cites=["Bereshit Rabbah 46:4"])

# -------------------------- Gen.17.12 · THE_EIGHTH_DAY_HANDLER -------------
# וּבֶן־שְׁמֹנַת יָמִים יִמּוֹל לָכֶם כָּל־זָכָר לְדֹרֹתֵיכֶם יְלִיד בָּיִת
# וּמִקְנַת־כֶּסֶף מִכֹּל בֶּן־נֵכָר אֲשֶׁר לֹא מִזַּרְעֲךָ הוּא
# "And he that is eight days old shall be circumcised among you, every male
# throughout your generations, he that is born in the house, or bought with
# money of any foreigner, that is not of thy seed."
m.step("Gen.17.12")
# ‹וּבֶן־שְׁמֹנַת יָמִים יִמּוֹל לָכֶם כָּל־זָכָר› (“and-son number day
# circumcise to-you/your(pl) all male”) — standing handler — if son-number-
# day ∧ all-male-to-doroteikhem then circumcise ∧ born-house-and-buying-
# silver-bi-khlal
m.handler("ben_shemonat_yamim ∧ kol_zakhar_le_doroteikhem",
          "yimol ∧ yelid_bayit_u_miqnat_kesef_bi_khlal")
# witness-tier presupposed read: three_determinations_from_one_number on
# eighth_day_clause — read, not installed
m.witness_read("eighth_day_clause", "three_determinations_from_one_number",
                cites=["Shabbat 132a:15", "Shabbat 132a:20", "Sifra, Tazria Parashat Yoledet, Chapter 1 2"])

# -------------------------- Gen.17.13 · THE_DOUBLED_MUST_AND_THE_FLESH_COVENANT -
# הִמּוֹל יִמּוֹל יְלִיד בֵּיתְךָ וּמִקְנַת כַּסְפֶּךָ וְהָיְתָה בְרִיתִי
# בִּבְשַׂרְכֶם לִבְרִית עוֹלָם
# "He that is born in thy house, and he that is bought with thy money, must
# needs be circumcised; and My covenant shall be in your flesh for an
# everlasting covenant."
m.step("Gen.17.13")
# ‹הִמּוֹל יִמּוֹל … וְהָיְתָה בְרִיתִי בִּבְשַׂרְכֶם לִבְרִית עוֹלָם›
# (“circumcise circumcise … and-be covenant-me/my in-flesh-you/your(pl) to-
# covenant forever”) — fact holds: circumcise-circumcise-born-beitkha;
# vriti-bi-vesarkhem-to-me-vrit-forever
m.fact("himol_yimol_yelid_beitkha",
       "vriti_bi_vesarkhem_li_vrit_olam")
# witness-grounded state (its own tier): the_two_grammar_schools on
# himol_yimol
m.witness_state("himol_yimol", "the_two_grammar_schools",
                cites=["Jerusalem Talmud Shabbat 19:2:2", "Avodah Zarah 27a:6", "Bereshit Rabbah 46:12"])

# -------------------------- Gen.17.14 · THE_KARET_HANDLER ------------------
# וְעָרֵל זָכָר אֲשֶׁר לֹא־יִמּוֹל אֶת־בְּשַׂר עָרְלָתוֹ וְנִכְרְתָה
# הַנֶּפֶשׁ הַהִוא מֵעַמֶּיהָ אֶת־בְּרִיתִי הֵפַר
# "And the uncircumcised male who is not circumcised in the flesh of his
# foreskin, that soul shall be cut off from his people; he hath broken My
# covenant.'"
m.step("Gen.17.14")
# ‹וְעָרֵל זָכָר אֲשֶׁר לֹא־יִמּוֹל … וְנִכְרְתָה הַנֶּפֶשׁ הַהִוא
# מֵעַמֶּיהָ› (“and-uncircumcised male which not circumcise … and-cut the-
# living-being that from-people-her/its”) — standing handler — if
# uncircumcised-male-which-not-circumcise then and-cut-the-living-being-the-
# hi-from-ameha ∧ obj-marker-My-covenant-break-up
m.handler("arel_zakhar_asher_lo_yimol",
          "ve_nikhrta_ha_nefesh_ha_hi_me_ameha ∧ et_briti_hefar")

# -------------------------- Gen.17.15 · SARAY_RETIRED_SARAH_DECREED --------
# וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם שָׂרַי אִשְׁתְּךָ לֹא־תִקְרָא אֶת־שְׁמָהּ
# שָׂרָי כִּי שָׂרָה שְׁמָהּ
# "And God said unto Abraham: 'As for Sarai thy wife, thou shalt not call
# her name Sarai, but Sarah shall her name be."
m.step("Gen.17.15")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־אַבְרָהָם› (“and-say God to Abraham”) — event: say
# — agent God
m.event("say", agent="elohim")
# ‹לֹא־תִקְרָא אֶת־שְׁמָהּ שָׂרָי כִּי שָׂרָה שְׁמָהּ› (“not call obj-marker
# name-her/its Sarai that Sarah name-her/its”) — fact holds: not-call-obj-
# marker-shemah-Sarai; that-sarah-shemah
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
# מִמֶּנָּה יִהְיוּ› (“and-bless obj-marker-her/its and-also set from-
# her/its to-you/your son … king people from-her/its be”) — fact holds: and-
# bless-her-and-set-mimenah-to-you-son; malkhei-people-mimenah-be
m.fact("u_verakhti_otah_ve_natati_mimenah_lekha_ben",
       "malkhei_amim_mimenah_yihyu")

# -------------------------- Gen.17.17 · THE_LAUGH_IN_THE_HEART -------------
# וַיִּפֹּל אַבְרָהָם עַל־פָּנָיו וַיִּצְחָק וַיֹּאמֶר בְּלִבּוֹ הַלְּבֶן
# מֵאָה־שָׁנָה יִוָּלֵד וְאִם־שָׂרָה הֲבַת־תִּשְׁעִים שָׁנָה תֵּלֵד
# "Then Abraham fell upon his face, and laughed, and said in his heart:
# 'Shall a child be born unto him that is a hundred years old? and shall
# Sarah, that is ninety years old, bear?'"
m.step("Gen.17.17")
# ‹וַיִּפֹּל אַבְרָהָם עַל־פָּנָיו› (“and-fall Abraham over face-him/its”) —
# event: fall — agent Abraham
m.event("fall", agent="avraham")
# ‹וַיִּצְחָק› (“and-laugh-outright”) — event: laugh — agent Abraham
m.event("laugh", agent="avraham")
# ‹וַיֹּאמֶר בְּלִבּוֹ› (“and-say in-heart-him/its”) — event: say — agent
# Abraham
m.event("say", agent="avraham")
# ‹הַלְּבֶן מֵאָה־שָׁנָה יִוָּלֵד וְאִם־שָׂרָה הֲבַת־תִּשְׁעִים שָׁנָה
# תֵּלֵד› (“the-to-son hundred years bear-young and-if Sarah the-daughter
# ninety years bear-young”) — fact holds: the-to-between-hundred-year-bear-
# young; the-daughter-ninety-year-bear-young
m.fact("ha_le_ven_meah_shanah_yivaled",
       "ha_vat_tishim_shanah_teled")
# witness-tier presupposed read: alteration_census_and_name_remedy on
# laughter_clause — read, not installed
m.witness_read("laughter_clause", "alteration_census_and_name_remedy",
                cites=["Bereshit Rabbah 48:17", "Rosh Hashanah 16b:6"])

# -------------------------- Gen.17.18 · THE_LU_PLEA ------------------------
# וַיֹּאמֶר אַבְרָהָם אֶל־הָאֱלֹהִים לוּ יִשְׁמָעֵאל יִחְיֶה לְפָנֶיךָ
# "And Abraham said unto God: 'Oh that Ishmael might live before Thee!'"
m.step("Gen.17.18")
# ‹וַיֹּאמֶר אַבְרָהָם אֶל־הָאֱלֹהִים› (“and-say Abraham to the-God”) —
# event: say — agent Abraham
m.event("say", agent="avraham")
# ‹לוּ יִשְׁמָעֵאל יִחְיֶה לְפָנֶיךָ› (“conditional-particle Ishmael live
# to-face-you/your”) — fact holds: conditional-particle-Ishmael-yichyeh-
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
# ‹וַיֹּאמֶר אֱלֹהִים אֲבָל› (“and-say God nay”) — event: say — agent God
m.event("say", agent="elohim")
# ‹שָׂרָה … יֹלֶדֶת לְךָ בֵּן וְקָרָאתָ אֶת־שְׁמוֹ יִצְחָק וַהֲקִמֹתִי
# אֶת־בְּרִיתִי אִתּוֹ› (“Sarah … bear-young to-you/your son and-call obj-
# marker name-him/its Isaac and-arise obj-marker covenant-me/my with-
# him/its”) — fact holds: sarah-bear-young-to-you-son; and-call-obj-marker-
# shemo-laugh-outright; and-arise-obj-marker-My-covenant-with-him-to-me-
# vrit-forever
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
# נְשִׂיאִם יוֹלִיד› (“and-to-Ishmael hear-you/your behold bless obj-marker-
# him/its … two -teen prince bear-young”) — fact holds: and-to-Ishmael-
# shematikha; hineh-bless-it-bi-very-very; shneim--teen-prince-bear-young
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
# הָאַחֶרֶת› (“and-obj-marker covenant-me/my arise with Isaac … to-seasons
# the-this in-years the-hinder”) — fact holds: and-obj-marker-My-covenant-
# arise-obj-marker-laugh-outright; to-seasons-the-this-in-the-year-the-
# hinder
m.fact("ve_et_briti_aqim_et_yitzchaq",
       "la_moed_ha_zeh_ba_shanah_ha_acheret")

# -------------------------- Gen.17.22 · THE_FINISH_AND_THE_ASCENT ----------
# וַיְכַל לְדַבֵּר אִתּוֹ וַיַּעַל אֱלֹהִים מֵעַל אַבְרָהָם
# "And He left off talking with him, and God went up from Abraham."
m.step("Gen.17.22")
# ‹וַיְכַל לְדַבֵּר אִתּוֹ› (“and-be-complete to-speak with-him/its”) —
# event: finish-speaking — agent God
m.event("finish_speaking", agent="elohim")
# ‹וַיַּעַל אֱלֹהִים מֵעַל אַבְרָהָם› (“and-go-up God from-over Abraham”) —
# event: ascend — agent God
m.event("ascend", agent="elohim")
# witness-tier presupposed read: leave_taking_rule_and_chariot_claim on
# ascent_from_abraham — read, not installed
m.witness_read("ascent_from_abraham", "leave_taking_rule_and_chariot_claim",
                cites=["Bereshit Rabbah 47:6", "Mekhilta DeRabbi Shimon Ben Yochai, Additions 6:2"])

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
# ‹וַיִּקַּח אַבְרָהָם אֶת־יִשְׁמָעֵאל בְּנוֹ› (“and-take Abraham obj-marker
# Ishmael son-him/its”) — event: take — agent Abraham; theme Ishmael-and-
# all-men-of-beito
m.event("take", agent="avraham", themes=["yishmael_ve_khol_anshei_beito"])
# ‹וַיָּמָל אֶת־בְּשַׂר עָרְלָתָם … נִמּוֹל אַבְרָהָם וְיִשְׁמָעֵאל בְּנוֹ …
# נִמֹּלוּ אִתּוֹ› (“and-circumcise obj-marker flesh foreskin-them/their …
# circumcise Abraham and-Ishmael son-him/its … circumcise with-him/its”) —
# event: circumcise — agent Abraham; theme all-male-in-men-of-beito
m.event("circumcise", agent="avraham", themes=["kol_zakhar_be_anshei_beito"])
# ‹בְּעֶצֶם הַיּוֹם הַזֶּה … כַּאֲשֶׁר דִּבֶּר אִתּוֹ אֱלֹהִים› (“in-bone
# the-day the-this … like-as/which speak with-him/its God”) — fact holds:
# in-bone-the-day-the-this; like-which-speak-with-him-God;
# Abraham-99-Ishmael-13-in-himolam
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
    assert sorted(m.WORLD["witnessed"]) == ['himol_yimol', 'rename_operator']
    assert m.WORLD["witnessed"]['himol_yimol']["cites"] == ['Jerusalem Talmud Shabbat 19:2:2', 'Avodah Zarah 27a:6', 'Bereshit Rabbah 46:12']
    assert all('the_two_grammar_schools' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['rename_operator']["cites"] == ['Berakhot 13a:8', 'Bereshit Rabbah 46:8', 'Tosefta Berakhot 1:15', 'Berakhot 13a:10']
    assert all('enforced_naming_law_and_counter_rule' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('tamim_condition', 'wholeness_pending_the_act'), ('av_hamon', 'charter_of_the_acronym_rule'), ('covenant_clause', 'three_family_laws'), ('dorot_token', 'surviving_analogy_of_three_weighed'), ('land_grant', 'conditioned_on_the_next_verse'), ('circumcision_command', 'three_tier_enforcement_cascade'), ('abraham_own_analogy', 'objected_to_and_answered'), ('eighth_day_clause', 'three_determinations_from_one_number'), ('laughter_clause', 'alteration_census_and_name_remedy'), ('ascent_from_abraham', 'leave_taking_rule_and_chariot_claim')]
    assert m.WITNESS_READS[0]["cites"] == ['Mishnah Nedarim 3:11', 'Bereshit Rabbah 46:1']
    assert all('wholeness_pending_the_act' not in f for f in m.WORLD["facts"])
    assert 'tamim_condition' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 46:7', 'Shabbat 105a:2']
    assert all('charter_of_the_acronym_rule' not in f for f in m.WORLD["facts"])
    assert 'av_hamon' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Yevamot 42a:6', 'Yevamot 100b:9', 'Yevamot 64a:2']
    assert all('three_family_laws' not in f for f in m.WORLD["facts"])
    assert 'covenant_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Shabbat 132a:6', 'Shabbat 132a:8', 'Shabbat 132a:10']
    assert all('surviving_analogy_of_three_weighed' not in f for f in m.WORLD["facts"])
    assert 'dorot_token' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 46:9']
    assert all('conditioned_on_the_next_verse' not in f for f in m.WORLD["facts"])
    assert 'land_grant' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Kiddushin 29a:11', 'Avodah Zarah 26b:12', 'Jerusalem Talmud Kiddushin 1:7:2']
    assert all('three_tier_enforcement_cascade' not in f for f in m.WORLD["facts"])
    assert 'circumcision_command' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 46:4']
    assert all('objected_to_and_answered' not in f for f in m.WORLD["facts"])
    assert 'abraham_own_analogy' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Shabbat 132a:15', 'Shabbat 132a:20', 'Sifra, Tazria Parashat Yoledet, Chapter 1 2']
    assert all('three_determinations_from_one_number' not in f for f in m.WORLD["facts"])
    assert 'eighth_day_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 48:17', 'Rosh Hashanah 16b:6']
    assert all('alteration_census_and_name_remedy' not in f for f in m.WORLD["facts"])
    assert 'laughter_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 47:6', 'Mekhilta DeRabbi Shimon Ben Yochai, Additions 6:2']
    assert all('leave_taking_rule_and_chariot_claim' not in f for f in m.WORLD["facts"])
    assert 'ascent_from_abraham' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
