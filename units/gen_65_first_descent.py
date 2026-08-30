#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_65_first_descent — 42:1-38
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_65_first_descent.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The first descent: brothers before the governor (42:1-38)"""
from machine import Machine

m = Machine("gen_65_first_descent")

# -------------------------- Gen.42.1 · WHY_DO_YOU_LOOK_AT_ONE_ANOTHER ------
# וַיַּרְא יַעֲקֹב כִּי יֶשׁ־שֶׁבֶר בְּמִצְרָיִם וַיֹּאמֶר יַעֲקֹב לְבָנָיו
# לָמָּה תִּתְרָאוּ
# "[EN-AID] And Jacob saw that there was grain in Egypt; and Jacob said to
# his sons: Why do you look at one another?"
m.step("Gen.42.1")
# ‹כִּי יֶשׁ־שֶׁבֶר בְּמִצְרָיִם› (“that there-is grain in-Egypt”) — fact
# holds: there-is-grain-in-Egypt
m.fact("yesh_shever_be_mitzrayim")
# witness-tier presupposed read: a_pun_the_chain_builds_on on grain_in_egypt
# — read, not installed
m.witness_read("grain_in_egypt", "a_pun_the_chain_builds_on",
                cites=["Bereshit Rabbah 91:1", "Onkelos Genesis 42:1"])

# -------------------------- Gen.42.2 · GO_DOWN_AND_BUY ---------------------
# וַיֹּאמֶר הִנֵּה שָׁמַעְתִּי כִּי יֶשׁ־שֶׁבֶר בְּמִצְרָיִם רְדוּ־שָׁמָּה
# וְשִׁבְרוּ־לָנוּ מִשָּׁם וְנִחְיֶה וְלֹא נָמוּת
# "[EN-AID] And he said: Behold, I have heard that there is grain in Egypt;
# go down there and buy for us from there, that we may live and not die."
m.step("Gen.42.2")
# ‹רְדוּ־שָׁמָּה וְשִׁבְרוּ־לָנוּ› (“go-down there-ward and-deal-in-grain
# to-us/our”) — Jacob speaks a demand — LET: go-down-shamah-and-deal-in-
# grain-lanu
m.declare("yaaqov", "LET",
          "redu_shamah_ve_shivru_lanu")
# witness-grounded state (its own tier):
# the_imperative_carries_the_years_of_the_bondage on go_down
m.witness_state("go_down", "the_imperative_carries_the_years_of_the_bondage",
                cites=["Bereshit Rabbah 91:2", "Bereshit Rabbah 91:6"])

# -------------------------- Gen.42.3 · TEN_GO_DOWN -------------------------
# וַיֵּרְדוּ אֲחֵי־יוֹסֵף עֲשָׂרָה לִשְׁבֹּר בָּר מִמִּצְרָיִם
# "[EN-AID] And the ten brothers of Joseph went down to buy grain from
# Egypt."
m.step("Gen.42.3")
# ‹וַיֵּרְדוּ אֲחֵי־יוֹסֵף עֲשָׂרָה לִשְׁבֹּר בָּר מִמִּצְרָיִם› (“and-go-
# down brother Joseph ten to-deal-in-grain grain-of-any-kind from-Egypt”) —
# demand settled (popped from the queue): go-down-shamah-and-deal-in-grain-
# lanu
m.result("redu_shamah_ve_shivru_lanu", tmark="t1")
# witness-tier presupposed read: nine_parts_brotherhood_one_part_grain on
# ten_brothers_went_down — read, not installed
m.witness_read("ten_brothers_went_down", "nine_parts_brotherhood_one_part_grain",
                cites=["Bereshit Rabbah 91:2"])

# -------------------------- Gen.42.4 · BENJAMIN_WITHHELD -------------------
# וְאֶת־בִּנְיָמִין אֲחִי יוֹסֵף לֹא־שָׁלַח יַעֲקֹב אֶת־אֶחָיו כִּי אָמַר
# פֶּן־יִקְרָאֶנּוּ אָסוֹן
# "[EN-AID] But Benjamin, Joseph's brother, Jacob did not send with his
# brothers — for he said: Lest harm befall him."
m.step("Gen.42.4")
# ‹וְאֶת־בִּנְיָמִין› (“and-obj-marker Benjamin”) — fact holds: obj-marker-
# Benjamin-not-send-lest-hurt
m.fact("et_binyamin_lo_shalach_pen_ason")
# witness-grounded state (its own tier):
# the_word_lives_only_here_and_in_the_capital_law on lest_harm_befall_him
m.witness_state("lest_harm_befall_him", "the_word_lives_only_here_and_in_the_capital_law",
                cites=["Onkelos Genesis 42:4", "Onkelos Genesis 42:38"])

# -------------------------- Gen.42.5 · AMONG_THE_COMERS --------------------
# וַיָּבֹאוּ בְּנֵי יִשְׂרָאֵל לִשְׁבֹּר בְּתוֹךְ הַבָּאִים כִּי־הָיָה
# הָרָעָב בְּאֶרֶץ כְּנָעַן
# "[EN-AID] And the sons of Israel came to buy among those who came, for the
# famine was in the land of Canaan."
m.step("Gen.42.5")
# ‹וַיָּבֹאוּ בְּנֵי יִשְׂרָאֵל לִשְׁבֹּר בְּתוֹךְ הַבָּאִים› (“and-
# come/bring son Israel to-deal-in-grain in-midst the-come/bring”) — fact
# holds: in-midst-the-come/bring-that-the-hunger-in-earth-Canaan
m.fact("be_tokh_ha_baim_ki_ha_raav_be_eretz_kenaan")
# witness-tier presupposed read: the_quorum_of_ten_derived_here on
# among_those_who_came — read, not installed
m.witness_read("among_those_who_came", "the_quorum_of_ten_derived_here",
                cites=["Bereshit Rabbah 91:3"])

# -------------------------- Gen.42.6 · THE_SHEAVES_BOW ---------------------
# וְיוֹסֵף הוּא הַשַּׁלִּיט עַל־הָאָרֶץ הוּא הַמַּשְׁבִּיר לְכָל־עַם הָאָרֶץ
# וַיָּבֹאוּ אֲחֵי יוֹסֵף וַיִּשְׁתַּחֲווּ־לוֹ אַפַּיִם אָרְצָה
# "[EN-AID] And Joseph — he was the governor over the land, he the seller to
# all the people of the land; and Joseph's brothers came and bowed down to
# him, faces to the earth."
m.step("Gen.42.6")
# ‹וַיָּבֹאוּ אֲחֵי יוֹסֵף וַיִּשְׁתַּחֲווּ־לוֹ אַפַּיִם אָרְצָה› (“and-
# come/bring brother Joseph and-afflict to-him/its nose earth-ward”) —
# event: hishtachavu — agent achei-Joseph
m.event("hishtachavu", agent="achei_yosef")
# witness-tier presupposed read: three_edicts_that_make_the_finding_possible
# on the_governor_over_the_land — read, not installed
m.witness_read("the_governor_over_the_land", "three_edicts_that_make_the_finding_possible",
                cites=["Bereshit Rabbah 91:4"])

# -------------------------- Gen.42.7 · HE_KNEW_THEM_THEY_KNEW_HIM_NOT ------
# וַיַּרְא יוֹסֵף אֶת־אֶחָיו וַיַּכִּרֵם וַיִּתְנַכֵּר אֲלֵיהֶם וַיְדַבֵּר
# אִתָּם קָשׁוֹת וַיֹּאמֶר אֲלֵהֶם מֵאַיִן בָּאתֶם וַיֹּאמְרוּ מֵאֶרֶץ
# כְּנַעַן לִשְׁבָּר־אֹכֶל
# "[EN-AID] And Joseph saw his brothers and recognized them, and made
# himself strange to them, and spoke with them harshly; and he said to them:
# From where do you come? And they said: From the land of Canaan, to buy
# food."
m.step("Gen.42.7")
# ‹וַיַּכִּרֵם וַיִּתְנַכֵּר אֲלֵיהֶם› (“and-scrutinize-them/their and-
# scrutinize to-them/their”) — fact holds: and-yakirem-and-scrutinize-alehem
m.fact("va_yakirem_va_yitnaker_alehem")
# witness-grounded state (its own tier):
# disguise_against_deliberation_unresolved on he_made_himself_strange
m.witness_state("he_made_himself_strange", "disguise_against_deliberation_unresolved",
                cites=["Onkelos Genesis 42:7", "Bereshit Rabbah 91:7"])

# -------------------------- Gen.42.8 · THE_ONE_WAY_KNOWING -----------------
# וַיַּכֵּר יוֹסֵף אֶת־אֶחָיו וְהֵם לֹא הִכִּרֻהוּ
# "[EN-AID] And Joseph recognized his brothers, but they did not recognize
# him."
m.step("Gen.42.8")
# ‹וְהֵם לֹא הִכִּרֻהוּ› (“and-they not scrutinize-him/its”) — fact holds:
# and-they-not-hikiruhu
m.fact("ve_hem_lo_hikiruhu")
# witness-tier presupposed read: the_beard_as_the_recognition_variable on
# he_knew_them_they_knew_him_not — read, not installed
m.witness_read("he_knew_them_they_knew_him_not", "the_beard_as_the_recognition_variable",
                cites=["Bereshit Rabbah 91:7"])

# -------------------------- Gen.42.9 · THE_DREAMS_REMEMBERED ---------------
# וַיִּזְכֹּר יוֹסֵף אֵת הַחֲלֹמוֹת אֲשֶׁר חָלַם לָהֶם וַיֹּאמֶר אֲלֵהֶם
# מְרַגְּלִים אַתֶּם לִרְאוֹת אֶת־עֶרְוַת הָאָרֶץ בָּאתֶם
# "[EN-AID] And Joseph remembered the dreams which he dreamed of them; and
# he said to them: You are spies! To see the nakedness of the land you have
# come."
m.step("Gen.42.9")
# ‹וַיִּזְכֹּר יוֹסֵף אֵת הַחֲלֹמוֹת› (“and-mark Joseph obj-marker the-
# dream”) — event: male — agent Joseph; theme the-dream
m.event("zakhar", agent="yosef", themes=["ha_chalomot"])
# witness-tier presupposed read: rendered_as_the_breach_in_the_defenses on
# the_nakedness_of_the_land — read, not installed
m.witness_read("the_nakedness_of_the_land", "rendered_as_the_breach_in_the_defenses",
                cites=["Onkelos Genesis 42:9", "Onkelos Genesis 42:12"])

# -------------------------- Gen.42.10 · NO_MY_LORD -------------------------
# וַיֹּאמְרוּ אֵלָיו לֹא אֲדֹנִי וַעֲבָדֶיךָ בָּאוּ לִשְׁבָּר־אֹכֶל
# "[EN-AID] And they said to him: No, my lord; your servants have come to
# buy food."
m.step("Gen.42.10")
# ‹לֹא אֲדֹנִי וַעֲבָדֶיךָ בָּאוּ› (“not lord-me/my and-servant-you/your
# come/bring”) — fact holds: not-adoni-avadekha-come/bring-lishbor-food
m.fact("lo_adoni_avadekha_bau_lishbor_okhel")

# -------------------------- Gen.42.11 · WE_ARE_TWELVE_HONEST_MEN -----------
# כֻּלָּנוּ בְּנֵי אִישׁ־אֶחָד נָחְנוּ כֵּנִים אֲנַחְנוּ לֹא־הָיוּ עֲבָדֶיךָ
# מְרַגְּלִים
# "[EN-AID] We are all sons of one man; we are honest; your servants have
# never been spies."
m.step("Gen.42.11")
# ‹כֻּלָּנוּ בְּנֵי אִישׁ־אֶחָד נָחְנוּ› (“all-us/our son man one we”) —
# fact holds: kulanu-son-man-one-we
m.fact("kulanu_bene_ish_echad_nachnu")

# -------------------------- Gen.42.12 · THE_CHARGE_REPEATED ----------------
# וַיֹּאמֶר אֲלֵהֶם לֹא כִּי־עֶרְוַת הָאָרֶץ בָּאתֶם לִרְאוֹת
# "[EN-AID] And he said to them: No — for the nakedness of the land you have
# come to see."
m.step("Gen.42.12")
# ‹וַיֹּאמֶר אֲלֵהֶם לֹא כִּי־עֶרְוַת הָאָרֶץ בָּאתֶם לִרְאוֹת› (“and-say
# to-them/their not that nudity the-earth come/bring to-see”) — fact holds:
# nudity-the-earth-come/bring-lirot
m.fact("ervat_ha_aretz_batem_lirot")

# -------------------------- Gen.42.13 · TWELVE_MINUS_ONE_ACCOUNTING --------
# וַיֹּאמְרוּ שְׁנֵים עָשָׂר עֲבָדֶיךָ אַחִים אֲנַחְנוּ בְּנֵי אִישׁ־אֶחָד
# בְּאֶרֶץ כְּנָעַן וְהִנֵּה הַקָּטֹן אֶת־אָבִינוּ הַיּוֹם וְהָאֶחָד
# אֵינֶנּוּ
# "[EN-AID] And they said: Your servants are twelve brothers, sons of one
# man in the land of Canaan; and behold, the youngest is with our father
# today, and the one — he is not."
m.step("Gen.42.13")
# ‹וְהִנֵּה הַקָּטֹן אֶת־אָבִינוּ הַיּוֹם וְהָאֶחָד אֵינֶנּוּ› (“and-behold
# the-small with father-us/our the-day and-the-one there-is-not-him/its”) —
# fact holds: two--teen-and-the-one-enennu
m.fact("shenem_asar_ve_ha_echad_enennu")

# -------------------------- Gen.42.14 · IT_IS_WHAT_I_SAID ------------------
# וַיֹּאמֶר אֲלֵהֶם יוֹסֵף הוּא אֲשֶׁר דִּבַּרְתִּי אֲלֵכֶם לֵאמֹר
# מְרַגְּלִים אַתֶּם
# "[EN-AID] And Joseph said to them: It is what I spoke to you, saying: You
# are spies."
m.step("Gen.42.14")
# ‹וַיֹּאמֶר אֲלֵהֶם יוֹסֵף הוּא אֲשֶׁר דִּבַּרְתִּי אֲלֵכֶם לֵאמֹר
# מְרַגְּלִים אַתֶּם› (“and-say to-them/their Joseph he/it which speak to-
# you/your(pl) to-say walk-along you”) — fact holds: he/it-which-speak-walk-
# along-you
m.fact("hu_asher_dibarti_meraglim_atem")

# -------------------------- Gen.42.15 · BY_THIS_YOU_SHALL_BE_TESTED --------
# בְּזֹאת תִּבָּחֵנוּ חֵי פַרְעֹה אִם־תֵּצְאוּ מִזֶּה כִּי אִם־בְּבוֹא
# אֲחִיכֶם הַקָּטֹן הֵנָּה
# "[EN-AID] By this you shall be tested — by the life of Pharaoh! — you
# shall not go out from here except by the coming of your youngest brother
# here."
m.step("Gen.42.15")
# ‹בְּזֹאת תִּבָּחֵנוּ חֵי פַרְעֹה› (“in-this test living Pharaoh”) — fact
# holds: in-this-test-chei-Pharaoh
m.fact("be_zot_tibachenu_chei_faro")
# witness-tier presupposed read: identified_as_a_false_oath_formula on
# by_pharaohs_life — read, not installed
m.witness_read("by_pharaohs_life", "identified_as_a_false_oath_formula",
                cites=["Bereshit Rabbah 91:7"])

# -------------------------- Gen.42.16 · THE_FIRST_PLAN ---------------------
# שִׁלְחוּ מִכֶּם אֶחָד וְיִקַּח אֶת־אֲחִיכֶם וְאַתֶּם הֵאָסְרוּ
# וְיִבָּחֲנוּ דִּבְרֵיכֶם הַאֱמֶת אִתְּכֶם וְאִם־לֹא חֵי פַרְעֹה כִּי
# מְרַגְּלִים אַתֶּם
# "[EN-AID] Send one of you and let him take your brother, and you — be
# bound! — and your words will be tested, whether truth is with you; and if
# not — by the life of Pharaoh — you are spies."
m.step("Gen.42.16")
# ‹שִׁלְחוּ מִכֶּם אֶחָד› (“send from-you/your(pl) one”) — Joseph speaks a
# demand — LET: send-mikem-one
m.declare("yosef", "LET",
          "shilchu_mikem_echad")

# -------------------------- Gen.42.17 · THREE_DAYS_IN_CUSTODY --------------
# וַיֶּאֱסֹף אֹתָם אֶל־מִשְׁמָר שְׁלֹשֶׁת יָמִים
# "[EN-AID] And he gathered them into custody three days."
m.step("Gen.42.17")
# ‹וַיֶּאֱסֹף אֹתָם אֶל־מִשְׁמָר שְׁלֹשֶׁת יָמִים› (“and-gather-for-any-
# purpose obj-marker-them/their to guard three day”) — fact holds: to-guard-
# three-day
m.fact("el_mishmar_sheloshet_yamim")

# -------------------------- Gen.42.18 · THE_THIRD_DAY_REVISION -------------
# וַיֹּאמֶר אֲלֵהֶם יוֹסֵף בַּיּוֹם הַשְּׁלִישִׁי זֹאת עֲשׂוּ וִחְיוּ
# אֶת־הָאֱלֹהִים אֲנִי יָרֵא
# "[EN-AID] And Joseph said to them on the third day: This do, and live — I
# fear God."
m.step("Gen.42.18")
# ‹זֹאת עֲשׂוּ וִחְיוּ› (“this make and-live”) — Joseph speaks a demand —
# LET: this-make-vichyu
m.declare("yosef", "LET",
          "zot_asu_vichyu")
# witness-tier presupposed read: an_enumerated_member_of_the_canon_pattern
# on on_the_third_day — read, not installed
m.witness_read("on_the_third_day", "an_enumerated_member_of_the_canon_pattern",
                cites=["Bereshit Rabbah 56:1", "Onkelos Genesis 42:18"])

# -------------------------- Gen.42.19 · ONE_BOUND_NINE_CARRY ---------------
# אִם־כֵּנִים אַתֶּם אֲחִיכֶם אֶחָד יֵאָסֵר בְּבֵית מִשְׁמַרְכֶם וְאַתֶּם
# לְכוּ הָבִיאוּ שֶׁבֶר רַעֲבוֹן בָּתֵּיכֶם
# "[EN-AID] If you are honest, let one brother of yours be bound in the
# house of your custody; and you — go, carry grain for the famine of your
# households."
m.step("Gen.42.19")
# ‹אֲחִיכֶם אֶחָד יֵאָסֵר› (“brother-you/your(pl) one yoke”) — fact holds:
# achikhem-one-yoke-and-you-go
m.fact("achikhem_echad_yeaser_ve_atem_lekhu")

# -------------------------- Gen.42.20 · BRING_THE_YOUNGEST_AND_THE_RECEIPT -
# וְאֶת־אֲחִיכֶם הַקָּטֹן תָּבִיאוּ אֵלַי וְיֵאָמְנוּ דִבְרֵיכֶם וְלֹא
# תָמוּתוּ וַיַּעֲשׂוּ־כֵן
# "[EN-AID] And your youngest brother you shall bring to me, and your words
# will be confirmed, and you shall not die. And they did so."
m.step("Gen.42.20")
# ‹וְאֶת־אֲחִיכֶם הַקָּטֹן תָּבִיאוּ אֵלַי› (“and-obj-marker brother-
# you/your(pl) the-small come/bring to-me/my”) — Joseph speaks a demand —
# LET: obj-marker-achikhem-the-small-come/bring-elai
m.declare("yosef", "LET",
          "et_achikhem_ha_qaton_taviu_elai")
# ‹וַיַּעֲשׂוּ־כֵן› (“and-make so”) — demand settled (popped from the
# queue): this-make-vichyu
m.result("zot_asu_vichyu", tmark="t2")

# -------------------------- Gen.42.21 · THE_GUILT_SURFACES -----------------
# וַיֹּאמְרוּ אִישׁ אֶל־אָחִיו אֲבָל אֲשֵׁמִים אֲנַחְנוּ עַל־אָחִינוּ אֲשֶׁר
# רָאִינוּ צָרַת נַפְשׁוֹ בְּהִתְחַנְנוֹ אֵלֵינוּ וְלֹא שָׁמָעְנוּ עַל־כֵּן
# בָּאָה אֵלֵינוּ הַצָּרָה הַזֹּאת
# "[EN-AID] And they said, each to his brother: Truly we are guilty
# concerning our brother, whose soul's distress we saw when he pleaded to us
# and we did not hear — therefore this distress has come to us."
m.step("Gen.42.21")
# ‹אֲבָל אֲשֵׁמִים אֲנַחְנוּ עַל־אָחִינוּ› (“nay guilty we over brother-
# us/our”) — fact holds: nay-guilty-we-over-achinu
m.fact("aval_ashemim_anachnu_al_achinu")
# witness-tier presupposed read:
# the_pit_entered_as_evidence_and_hearing_read_as_obedience on
# the_confession — read, not installed
m.witness_read("the_confession", "the_pit_entered_as_evidence_and_hearing_read_as_obedience",
                cites=["Bereshit Rabbah 91:8", "Onkelos Genesis 42:21", "Onkelos Genesis 42:22"])

# -------------------------- Gen.42.22 · REUBEN_CITES_HIS_DEAD_DEMANDS ------
# וַיַּעַן רְאוּבֵן אֹתָם לֵאמֹר הֲלוֹא אָמַרְתִּי אֲלֵיכֶם לֵאמֹר
# אַל־תֶּחֶטְאוּ בַיֶּלֶד וְלֹא שְׁמַעְתֶּם וְגַם־דָּמוֹ הִנֵּה נִדְרָשׁ
# "[EN-AID] And Reuben answered them, saying: Did I not say to you, saying:
# Do not sin against the boy — and you did not hear; and also his blood —
# behold, it is required."
m.step("Gen.42.22")
# ‹הֲלוֹא אָמַרְתִּי› (“is-it-not say”) — fact holds: halo-say-over-sin-and-
# child
m.fact("halo_amarti_al_techetu_va_yeled")

# -------------------------- Gen.42.23 · THE_INTERPRETER_BETWEEN ------------
# וְהֵם לֹא יָדְעוּ כִּי שֹׁמֵעַ יוֹסֵף כִּי הַמֵּלִיץ בֵּינֹתָם
# "[EN-AID] And they did not know that Joseph heard — for the interpreter
# was between them."
m.step("Gen.42.23")
# ‹כִּי הַמֵּלִיץ בֵּינֹתָם› (“that the-make-mouths-at between-them/their”)
# — fact holds: that-the-make-mouths-at-benotam
m.fact("ki_ha_melitz_benotam")
# witness-grounded state (its own tier):
# identified_as_the_viceroys_elder_son on the_interpreter
m.witness_state("the_interpreter", "identified_as_the_viceroys_elder_son",
                cites=["Bereshit Rabbah 91:8"])

# -------------------------- Gen.42.24 · WEEPING_AND_THE_SOFT_BINDING -------
# וַיִּסֹּב מֵעֲלֵיהֶם וַיֵּבְךְּ וַיָּשָׁב אֲלֵהֶם וַיְדַבֵּר אֲלֵהֶם
# וַיִּקַּח מֵאִתָּם אֶת־שִׁמְעוֹן וַיֶּאֱסֹר אֹתוֹ לְעֵינֵיהֶם
# "[EN-AID] And he turned from them and wept; and he returned to them and
# spoke to them; and he took Simeon from them and bound him before their
# eyes."
m.step("Gen.42.24")
# ‹וַיִּסֹּב מֵעֲלֵיהֶם וַיֵּבְךְּ› (“and-revolve from-over-them/their and-
# weep”) — event: bakha — agent Joseph
m.event("bakha", agent="yosef")
# ‹וַיִּקַּח מֵאִתָּם אֶת־שִׁמְעוֹן וַיֶּאֱסֹר אֹתוֹ לְעֵינֵיהֶם› (“and-take
# from-with-them/their obj-marker Simeon and-yoke obj-marker-him/its to-eye-
# them/their”) — fact holds: and-yikach-obj-marker-Simeon-and-yoke
m.fact("va_yikach_et_shimon_va_yeesor")
# witness-tier presupposed read: the_promised_repayment_arrives on
# simeon_bound_before_their_eyes — read, not installed
m.witness_read("simeon_bound_before_their_eyes", "the_promised_repayment_arrives",
                cites=["Bereshit Rabbah 84:16", "Bereshit Rabbah 99:7"])

# -------------------------- Gen.42.25 · VESSELS_SILVER_PROVISIONS ----------
# וַיְצַו יוֹסֵף וַיְמַלְאוּ אֶת־כְּלֵיהֶם בָּר וּלְהָשִׁיב כַּסְפֵּיהֶם
# אִישׁ אֶל־שַׂקּוֹ וְלָתֵת לָהֶם צֵדָה לַדָּרֶךְ וַיַּעַשׂ לָהֶם כֵּן
# "[EN-AID] And Joseph commanded, and they filled their vessels with grain,
# and returned their silver each to his sack, and gave them provisions for
# the way; and he did for them so."
m.step("Gen.42.25")
# ‹וַיְצַו יוֹסֵף וַיְמַלְאוּ אֶת־כְּלֵיהֶם בָּר וּלְהָשִׁיב כַּסְפֵּיהֶם›
# (“and-command Joseph and-fill obj-marker vessel-them/their grain-of-any-
# kind and-to-return silver-them/their”) — fact holds: and-command-and-to-
# return-kaspehem
m.fact("va_yetzav_u_le_hashiv_kaspehem")

# -------------------------- Gen.42.26 · THEY_DEPART ------------------------
# וַיִּשְׂאוּ אֶת־שִׁבְרָם עַל־חֲמֹרֵיהֶם וַיֵּלְכוּ מִשָּׁם
# "[EN-AID] And they carried their grain on their donkeys, and went from
# there."
m.step("Gen.42.26")
# ‹וַיִּשְׂאוּ אֶת־שִׁבְרָם עַל־חֲמֹרֵיהֶם› (“and-lift/carry obj-marker
# grain-them/their over male-ass-them/their”) — fact holds: and-lift/carry-
# obj-marker-shivram-over-chamorehem
m.fact("va_yisu_et_shivram_al_chamorehem")

# -------------------------- Gen.42.27 · THE_FIRST_SACK_OPENS ---------------
# וַיִּפְתַּח הָאֶחָד אֶת־שַׂקּוֹ לָתֵת מִסְפּוֹא לַחֲמֹרוֹ בַּמָּלוֹן
# וַיַּרְא אֶת־כַּסְפּוֹ וְהִנֵּה־הוּא בְּפִי אַמְתַּחְתּוֹ
# "[EN-AID] And the one opened his sack to give fodder to his donkey at the
# lodging place, and he saw his silver — and behold, it was in the mouth of
# his bag."
m.step("Gen.42.27")
# ‹וַיַּרְא אֶת־כַּסְפּוֹ וְהִנֵּה־הוּא בְּפִי אַמְתַּחְתּוֹ› (“and-see obj-
# marker silver-him/its and-behold he/it in-mouth something-expansive-
# him/its”) — fact holds: and-see-obj-marker-kaspo-in-mouth-amtachto
m.fact("va_yar_et_kaspo_be_fi_amtachto")

# -------------------------- Gen.42.28 · WHAT_IS_THIS_GOD_HAS_DONE ----------
# וַיֹּאמֶר אֶל־אֶחָיו הוּשַׁב כַּסְפִּי וְגַם הִנֵּה בְאַמְתַּחְתִּי
# וַיֵּצֵא לִבָּם וַיֶּחֶרְדוּ אִישׁ אֶל־אָחִיו לֵאמֹר מַה־זֹּאת עָשָׂה
# אֱלֹהִים לָנוּ
# "[EN-AID] And he said to his brothers: My silver has been returned — and
# also, behold, it is in my bag! And their heart went out, and they
# trembled, each to his brother, saying: What is this God has done to us?"
m.step("Gen.42.28")
# ‹מַה־זֹּאת עָשָׂה אֱלֹהִים לָנוּ› (“what this make God to-us/our”) — fact
# holds: and-bring-forth-libam-what-this-make-God
m.fact("va_yetze_libam_ma_zot_asa_Elohim")
# witness-tier presupposed read: the_faculty_named_and_the_organ_removed on
# their_heart_went_out — read, not installed
m.witness_read("their_heart_went_out", "the_faculty_named_and_the_organ_removed",
                cites=["Onkelos Genesis 42:28"])

# -------------------------- Gen.42.29 · THE_REPORT_BEGINS ------------------
# וַיָּבֹאוּ אֶל־יַעֲקֹב אֲבִיהֶם אַרְצָה כְּנָעַן וַיַּגִּידוּ לוֹ אֵת
# כָּל־הַקֹּרֹת אֹתָם לֵאמֹר
# "[EN-AID] And they came to Jacob their father, to the land of Canaan; and
# they told him all that had befallen them, saying:"
m.step("Gen.42.29")
# ‹וַיַּגִּידוּ לוֹ› (“and-tell to-him/its”) — fact holds: and-tell-not-obj-
# marker-all-the-light-upon
m.fact("va_yagidu_lo_et_kol_ha_qorot")

# -------------------------- Gen.42.30 · THE_HARSH_LORD_RETOLD --------------
# דִּבֶּר הָאִישׁ אֲדֹנֵי הָאָרֶץ אִתָּנוּ קָשׁוֹת וַיִּתֵּן אֹתָנוּ
# כִּמְרַגְּלִים אֶת־הָאָרֶץ
# "[EN-AID] The man, the lord of the land, spoke with us harshly, and made
# us as spies of the land."
m.step("Gen.42.30")
# ‹דִּבֶּר הָאִישׁ אֲדֹנֵי הָאָרֶץ אִתָּנוּ קָשׁוֹת› (“speak the-man lord
# the-earth with-us/our severe”) — fact holds: speak-the-man-lord-the-earth-
# severe
m.fact("diber_ha_ish_adone_ha_aretz_qashot")

# -------------------------- Gen.42.31 · WE_SAID_HONEST ---------------------
# וַנֹּאמֶר אֵלָיו כֵּנִים אֲנָחְנוּ לֹא הָיִינוּ מְרַגְּלִים
# "[EN-AID] And we said to him: We are honest; we have never been spies."
m.step("Gen.42.31")
# ‹כֵּנִים אֲנָחְנוּ לֹא הָיִינוּ מְרַגְּלִים› (“set-upright we not be walk-
# along”) — fact holds: set-upright-we-not-be-walk-along
m.fact("kenim_anachnu_lo_hayinu_meraglim")

# -------------------------- Gen.42.32 · TWELVE_RETOLD ----------------------
# שְׁנֵים־עָשָׂר אֲנַחְנוּ אַחִים בְּנֵי אָבִינוּ הָאֶחָד אֵינֶנּוּ
# וְהַקָּטֹן הַיּוֹם אֶת־אָבִינוּ בְּאֶרֶץ כְּנָעַן
# "[EN-AID] We are twelve brothers, sons of our father: the one is not, and
# the youngest is today with our father in the land of Canaan."
m.step("Gen.42.32")
# ‹שְׁנֵים־עָשָׂר אֲנַחְנוּ אַחִים› (“two -teen we brother”) — fact holds:
# two--teen-we-the-one-enennu
m.fact("shenem_asar_anachnu_ha_echad_enennu")

# -------------------------- Gen.42.33 · LEAVE_ONE_TAKE_GO ------------------
# וַיֹּאמֶר אֵלֵינוּ הָאִישׁ אֲדֹנֵי הָאָרֶץ בְּזֹאת אֵדַע כִּי כֵנִים
# אַתֶּם אֲחִיכֶם הָאֶחָד הַנִּיחוּ אִתִּי וְאֶת־רַעֲבוֹן בָּתֵּיכֶם קְחוּ
# וָלֵכוּ
# "[EN-AID] And the man, the lord of the land, said to us: By this I shall
# know that you are honest — leave one brother of yours with me, and the
# famine of your households take, and go."
m.step("Gen.42.33")
# ‹אֲחִיכֶם הָאֶחָד הַנִּיחוּ אִתִּי› (“brother-you/your(pl) the-one deposit
# with-me/my”) — fact holds: achikhem-the-one-deposit-iti
m.fact("achikhem_ha_echad_hanichu_iti")

# -------------------------- Gen.42.34 · BRING_AND_TRADE --------------------
# וְהָבִיאוּ אֶת־אֲחִיכֶם הַקָּטֹן אֵלַי וְאֵדְעָה כִּי לֹא מְרַגְּלִים
# אַתֶּם כִּי כֵנִים אַתֶּם אֶת־אֲחִיכֶם אֶתֵּן לָכֶם וְאֶת־הָאָרֶץ
# תִּסְחָרוּ
# "[EN-AID] And bring your youngest brother to me, that I may know you are
# not spies, that you are honest; your brother I will give to you, and the
# land you shall trade."
m.step("Gen.42.34")
# ‹וְאֶת־הָאָרֶץ תִּסְחָרוּ› (“and-obj-marker the-earth travel-round”) —
# fact holds: and-obj-marker-the-earth-travel-round
m.fact("ve_et_ha_aretz_tischaru")

# -------------------------- Gen.42.35 · THE_BUNDLES_AND_THE_FEAR -----------
# וַיְהִי הֵם מְרִיקִים שַׂקֵּיהֶם וְהִנֵּה־אִישׁ צְרוֹר־כַּסְפּוֹ
# בְּשַׂקּוֹ וַיִּרְאוּ אֶת־צְרֹרוֹת כַּסְפֵּיהֶם הֵמָּה וַאֲבִיהֶם
# וַיִּירָאוּ
# "[EN-AID] And it was, as they were emptying their sacks — and behold, each
# man's bundle of silver was in his sack; and they saw their bundles of
# silver, they and their father, and they feared."
m.step("Gen.42.35")
# ‹וַיִּרְאוּ אֶת־צְרֹרוֹת כַּסְפֵּיהֶם הֵמָּה וַאֲבִיהֶם וַיִּירָאוּ›
# (“and-see obj-marker parcel silver-them/their they and-father-them/their
# and-fear”) — fact holds: and-see-obj-marker-parcel-kaspehem-and-fear
m.fact("va_yiru_et_tzerorot_kaspehem_va_yirau")
# witness-grounded state (its own tier): the_father_suspects_his_own_sons on
# the_silver_reappearing
m.witness_state("the_silver_reappearing", "the_father_suspects_his_own_sons",
                cites=["Bereshit Rabbah 91:9"])

# -------------------------- Gen.42.36 · YOU_HAVE_BEREAVED_ME ---------------
# וַיֹּאמֶר אֲלֵהֶם יַעֲקֹב אֲבִיהֶם אֹתִי שִׁכַּלְתֶּם יוֹסֵף אֵינֶנּוּ
# וְשִׁמְעוֹן אֵינֶנּוּ וְאֶת־בִּנְיָמִן תִּקָּחוּ עָלַי הָיוּ כֻלָּנָה
# "[EN-AID] And Jacob their father said to them: Me you have bereaved —
# Joseph is not, and Simeon is not, and Benjamin you would take: upon me are
# they all."
m.step("Gen.42.36")
# ‹אֹתִי שִׁכַּלְתֶּם יוֹסֵף אֵינֶנּוּ וְשִׁמְעוֹן אֵינֶנּוּ› (“obj-marker-
# me/my miscarry Joseph there-is-not-him/its and-Simeon there-is-not-
# him/its”) — fact holds: me-miscarry-Joseph-enennu-and-Simeon-enennu
m.fact("oti_shikaltem_yosef_enennu_ve_shimon_enennu")

# -------------------------- Gen.42.37 · REUBENS_PLEDGE ---------------------
# וַיֹּאמֶר רְאוּבֵן אֶל־אָבִיו לֵאמֹר אֶת־שְׁנֵי בָנַי תָּמִית אִם־לֹא
# אֲבִיאֶנּוּ אֵלֶיךָ תְּנָה אֹתוֹ עַל־יָדִי וַאֲנִי אֲשִׁיבֶנּוּ אֵלֶיךָ
# "[EN-AID] And Reuben said to his father, saying: My two sons you may kill
# if I do not bring him to you; give him into my hand, and I will return him
# to you."
m.step("Gen.42.37")
# ‹תְּנָה אֹתוֹ עַל־יָדִי› (“set-ward obj-marker-him/its over hand-me/my”) —
# Reuben speaks a demand — LET: tena-it-over-yadi
m.declare("reuven", "LET",
          "tena_oto_al_yadi")

# -------------------------- Gen.42.38 · MY_SON_SHALL_NOT_GO_DOWN -----------
# וַיֹּאמֶר לֹא־יֵרֵד בְּנִי עִמָּכֶם כִּי־אָחִיו מֵת וְהוּא לְבַדּוֹ
# נִשְׁאָר וּקְרָאָהוּ אָסוֹן בַּדֶּרֶךְ אֲשֶׁר תֵּלְכוּ־בָהּ וְהוֹרַדְתֶּם
# אֶת־שֵׂיבָתִי בְּיָגוֹן שְׁאוֹלָה
# "[EN-AID] And he said: My son shall not go down with you — for his brother
# is dead, and he alone is left; and should harm befall him on the way you
# go, you would bring down my gray hair in sorrow to Sheol."
m.step("Gen.42.38")
# ‹וַיֹּאמֶר לֹא־יֵרֵד בְּנִי עִמָּכֶם› (“and-say not go-down son-me/my
# with-you/your(pl)”) — fact holds: not-go-down-beni-imakhem
m.fact("lo_yered_beni_imakhem")
# witness-tier presupposed read: the_accuser_accuses_only_in_danger on
# lest_disaster_on_the_way — read, not installed
m.witness_read("lest_disaster_on_the_way", "the_accuser_accuses_only_in_danger",
                cites=["Bereshit Rabbah 91:9", "Onkelos Genesis 42:38"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shilchu_mikem_echad', 'et_achikhem_ha_qaton_taviu_elai', 'tena_oto_al_yadi']
    assert len(m.SPECS["log"]) == 5
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['yesh_shever_be_mitzrayim', 'et_binyamin_lo_shalach_pen_ason', 'be_tokh_ha_baim_ki_ha_raav_be_eretz_kenaan', 'va_yakirem_va_yitnaker_alehem', 've_hem_lo_hikiruhu', 'lo_adoni_avadekha_bau_lishbor_okhel', 'kulanu_bene_ish_echad_nachnu', 'ervat_ha_aretz_batem_lirot', 'shenem_asar_ve_ha_echad_enennu', 'hu_asher_dibarti_meraglim_atem', 'be_zot_tibachenu_chei_faro', 'el_mishmar_sheloshet_yamim', 'achikhem_echad_yeaser_ve_atem_lekhu', 'aval_ashemim_anachnu_al_achinu', 'halo_amarti_al_techetu_va_yeled', 'ki_ha_melitz_benotam', 'va_yikach_et_shimon_va_yeesor', 'va_yetzav_u_le_hashiv_kaspehem', 'va_yisu_et_shivram_al_chamorehem', 'va_yar_et_kaspo_be_fi_amtachto', 'va_yetze_libam_ma_zot_asa_Elohim', 'va_yagidu_lo_et_kol_ha_qorot', 'diber_ha_ish_adone_ha_aretz_qashot', 'kenim_anachnu_lo_hayinu_meraglim', 'shenem_asar_anachnu_ha_echad_enennu', 'achikhem_ha_echad_hanichu_iti', 've_et_ha_aretz_tischaru', 'va_yiru_et_tzerorot_kaspehem_va_yirau', 'oti_shikaltem_yosef_enennu_ve_shimon_enennu', 'lo_yered_beni_imakhem'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    assert sorted(m.WORLD["witnessed"]) == ['go_down', 'he_made_himself_strange', 'lest_harm_befall_him', 'the_interpreter', 'the_silver_reappearing']
    assert m.WORLD["witnessed"]['go_down']["cites"] == ['Bereshit Rabbah 91:2', 'Bereshit Rabbah 91:6']
    assert all('the_imperative_carries_the_years_of_the_bondage' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['he_made_himself_strange']["cites"] == ['Onkelos Genesis 42:7', 'Bereshit Rabbah 91:7']
    assert all('disguise_against_deliberation_unresolved' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['lest_harm_befall_him']["cites"] == ['Onkelos Genesis 42:4', 'Onkelos Genesis 42:38']
    assert all('the_word_lives_only_here_and_in_the_capital_law' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_interpreter']["cites"] == ['Bereshit Rabbah 91:8']
    assert all('identified_as_the_viceroys_elder_son' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['the_silver_reappearing']["cites"] == ['Bereshit Rabbah 91:9']
    assert all('the_father_suspects_his_own_sons' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('grain_in_egypt', 'a_pun_the_chain_builds_on'), ('ten_brothers_went_down', 'nine_parts_brotherhood_one_part_grain'), ('among_those_who_came', 'the_quorum_of_ten_derived_here'), ('the_governor_over_the_land', 'three_edicts_that_make_the_finding_possible'), ('he_knew_them_they_knew_him_not', 'the_beard_as_the_recognition_variable'), ('the_nakedness_of_the_land', 'rendered_as_the_breach_in_the_defenses'), ('by_pharaohs_life', 'identified_as_a_false_oath_formula'), ('on_the_third_day', 'an_enumerated_member_of_the_canon_pattern'), ('the_confession', 'the_pit_entered_as_evidence_and_hearing_read_as_obedience'), ('simeon_bound_before_their_eyes', 'the_promised_repayment_arrives'), ('their_heart_went_out', 'the_faculty_named_and_the_organ_removed'), ('lest_disaster_on_the_way', 'the_accuser_accuses_only_in_danger')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 91:1', 'Onkelos Genesis 42:1']
    assert all('a_pun_the_chain_builds_on' not in f for f in m.WORLD["facts"])
    assert 'grain_in_egypt' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 91:2']
    assert all('nine_parts_brotherhood_one_part_grain' not in f for f in m.WORLD["facts"])
    assert 'ten_brothers_went_down' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 91:3']
    assert all('the_quorum_of_ten_derived_here' not in f for f in m.WORLD["facts"])
    assert 'among_those_who_came' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 91:4']
    assert all('three_edicts_that_make_the_finding_possible' not in f for f in m.WORLD["facts"])
    assert 'the_governor_over_the_land' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 91:7']
    assert all('the_beard_as_the_recognition_variable' not in f for f in m.WORLD["facts"])
    assert 'he_knew_them_they_knew_him_not' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Onkelos Genesis 42:9', 'Onkelos Genesis 42:12']
    assert all('rendered_as_the_breach_in_the_defenses' not in f for f in m.WORLD["facts"])
    assert 'the_nakedness_of_the_land' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 91:7']
    assert all('identified_as_a_false_oath_formula' not in f for f in m.WORLD["facts"])
    assert 'by_pharaohs_life' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 56:1', 'Onkelos Genesis 42:18']
    assert all('an_enumerated_member_of_the_canon_pattern' not in f for f in m.WORLD["facts"])
    assert 'on_the_third_day' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 91:8', 'Onkelos Genesis 42:21', 'Onkelos Genesis 42:22']
    assert all('the_pit_entered_as_evidence_and_hearing_read_as_obedience' not in f for f in m.WORLD["facts"])
    assert 'the_confession' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 84:16', 'Bereshit Rabbah 99:7']
    assert all('the_promised_repayment_arrives' not in f for f in m.WORLD["facts"])
    assert 'simeon_bound_before_their_eyes' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Onkelos Genesis 42:28']
    assert all('the_faculty_named_and_the_organ_removed' not in f for f in m.WORLD["facts"])
    assert 'their_heart_went_out' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 91:9', 'Onkelos Genesis 42:38']
    assert all('the_accuser_accuses_only_in_danger' not in f for f in m.WORLD["facts"])
    assert 'lest_disaster_on_the_way' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
