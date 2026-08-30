#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_51_opened_womb_twelve_names — 29:31-30:24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_51_opened_womb_twelve_names.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The opened wombs and the twelve name-writes (29:31-30:24)"""
from machine import Machine

m = Machine("gen_51_opened_womb_twelve_names")

# -------------------------- Gen.29.31 · THE_SEEING_AND_THE_TWO_WOMBS -------
# וַיַּרְא יְהוָה כִּי־שְׂנוּאָה לֵאָה וַיִּפְתַּח אֶת־רַחְמָהּ וְרָחֵל
# עֲקָרָה
# "[EN-AID] And YHWH saw that Leah was hated, and He opened her womb; and
# Rachel was barren."
m.step("Gen.29.31")
# ‹וַיִּפְתַּח אֶת־רַחְמָהּ› (“and-open-wide obj-marker womb-her/its”) —
# event: patach — agent the-LORD; theme rechem-leah
m.event("patach", agent="YHWH", themes=["rechem_leah"])
# ‹וְרָחֵל עֲקָרָה› (“and-Rachel sterile”) — fact holds: hate(leah);
# sterile(Rachel)
m.fact("senua(leah)",
       "aqara(rachel)")
# witness-tier presupposed read:
# rendered_as_petition_and_acceptance_throughout on the_opened_womb — read,
# not installed
m.witness_read("the_opened_womb", "rendered_as_petition_and_acceptance_throughout",
                cites=["Onkelos Genesis 30:22", "Onkelos Genesis 30:6", "Onkelos Genesis 29:31"])

# -------------------------- Gen.29.32 · THE_FIRST_WRITE_REUVEN -------------
# וַתַּהַר לֵאָה וַתֵּלֶד בֵּן וַתִּקְרָא שְׁמוֹ רְאוּבֵן כִּי אָמְרָה
# כִּי־רָאָה יְהוָה בְּעָנְיִי כִּי עַתָּה יֶאֱהָבַנִי אִישִׁי
# "[EN-AID] And Leah conceived and bore a son, and she called his name
# Reuben, for she said: Because YHWH has seen my affliction; for now my
# husband will love me."
m.step("Gen.29.32")
# ‹וַתַּהַר לֵאָה וַתֵּלֶד בֵּן› (“and-be-pregnant Leah and-bear-young son”)
# — the world gains: son-1-leah
m.install("ben_1_leah")
# ‹וַתִּקְרָא שְׁמוֹ רְאוּבֵן› (“and-call name-him/its Reuben”) — named:
# son-1-leah := Reuben
m.name("ben_1_leah", "reuven")

# -------------------------- Gen.29.33 · THE_SECOND_WRITE_SHIMON ------------
# וַתַּהַר עוֹד וַתֵּלֶד בֵּן וַתֹּאמֶר כִּי־שָׁמַע יְהוָה כִּי־שְׂנוּאָה
# אָנֹכִי וַיִּתֶּן־לִי גַּם־אֶת־זֶה וַתִּקְרָא שְׁמוֹ שִׁמְעוֹן
# "[EN-AID] And she conceived again and bore a son, and said: Because YHWH
# has heard that I am hated, He has given me this one also; and she called
# his name Simeon."
m.step("Gen.29.33")
# ‹וַתַּהַר עוֹד וַתֵּלֶד בֵּן› (“and-be-pregnant still/again and-bear-young
# son”) — the world gains: son-2-leah
m.install("ben_2_leah")
# ‹וַתִּקְרָא שְׁמוֹ שִׁמְעוֹן› (“and-call name-him/its Simeon”) — named:
# son-2-leah := Simeon
m.name("ben_2_leah", "shimon")

# -------------------------- Gen.29.34 · THE_THIRD_WRITE_LEVI ---------------
# וַתַּהַר עוֹד וַתֵּלֶד בֵּן וַתֹּאמֶר עַתָּה הַפַּעַם יִלָּוֶה אִישִׁי
# אֵלַי כִּי־יָלַדְתִּי לוֹ שְׁלֹשָׁה בָנִים עַל־כֵּן קָרָא־שְׁמוֹ לֵוִי
# "[EN-AID] And she conceived again and bore a son, and said: Now this time
# my husband will be joined to me, for I have borne him three sons;
# therefore he called his name Levi."
m.step("Gen.29.34")
# ‹וַתַּהַר עוֹד וַתֵּלֶד בֵּן› (“and-be-pregnant still/again and-bear-young
# son”) — the world gains: son-3-leah
m.install("ben_3_leah")
# ‹קָרָא־שְׁמוֹ לֵוִי› (“call name-him/its Levi”) — named: son-3-leah :=
# Levi
m.name("ben_3_leah", "levi")

# -------------------------- Gen.29.35 · THE_FOURTH_WRITE_YEHUDA ------------
# וַתַּהַר עוֹד וַתֵּלֶד בֵּן וַתֹּאמֶר הַפַּעַם אוֹדֶה אֶת־יְהוָה עַל־כֵּן
# קָרְאָה שְׁמוֹ יְהוּדָה וַתַּעֲמֹד מִלֶּדֶת
# "[EN-AID] And she conceived again and bore a son, and said: This time I
# will praise YHWH; therefore she called his name Judah. And she ceased
# bearing."
m.step("Gen.29.35")
# ‹וַתַּהַר עוֹד וַתֵּלֶד בֵּן› (“and-be-pregnant still/again and-bear-young
# son”) — the world gains: son-4-leah
m.install("ben_4_leah")
# ‹קָרְאָה שְׁמוֹ יְהוּדָה› (“call name-him/its Judah”) — named: son-4-leah
# := Judah
m.name("ben_4_leah", "yehuda")
# witness-tier presupposed read: gratitude_begins_where_entitlement_ends on
# thanks_at_the_fourth — read, not installed
m.witness_read("thanks_at_the_fourth", "gratitude_begins_where_entitlement_ends",
                cites=["Bereshit Rabbah 71:4"])
# witness-tier presupposed read:
# entered_under_a_four_cell_name_conduct_table on the_twelve_names — read,
# not installed
m.witness_read("the_twelve_names", "entered_under_a_four_cell_name_conduct_table",
                cites=["Bereshit Rabbah 71:3"])

# -------------------------- Gen.30.1 · THE_CHILDREN_DEMAND -----------------
# וַתֵּרֶא רָחֵל כִּי לֹא יָלְדָה לְיַעֲקֹב וַתְּקַנֵּא רָחֵל בַּאֲחֹתָהּ
# וַתֹּאמֶר אֶל־יַעֲקֹב הָבָה־לִּי בָנִים וְאִם־אַיִן מֵתָה אָנֹכִי
# "[EN-AID] And Rachel saw that she bore Jacob no children, and Rachel
# envied her sister; and she said to Jacob: Give me children, and if not, I
# die."
m.step("Gen.30.1")
# ‹הָבָה־לִּי בָנִים› (“give-ward to-me/my son”) — Rachel speaks a demand —
# LET: hava-banim(Jacob)
m.declare("rachel", "LET",
          "hava_banim(yaaqov)")
# witness-tier presupposed read: proof_verse_for_the_living_as_dead_census
# on give_me_children_or_i_die — read, not installed
m.witness_read("give_me_children_or_i_die", "proof_verse_for_the_living_as_dead_census",
                cites=["Bereshit Rabbah 71:6", "Bereshit Rabbah 45:2"])

# -------------------------- Gen.30.2 · THE_REDIRECT_TO_ELOHIM --------------
# וַיִּחַר־אַף יַעֲקֹב בְּרָחֵל וַיֹּאמֶר הֲתַחַת אֱלֹהִים אָנֹכִי
# אֲשֶׁר־מָנַע מִמֵּךְ פְּרִי־בָטֶן
# "[EN-AID] And Jacob's anger burned against Rachel, and he said: Am I in
# the place of God, who has withheld from you the fruit of the womb?"
m.step("Gen.30.2")
# ‹הֲתַחַת אֱלֹהִים אָנֹכִי אֲשֶׁר־מָנַע מִמֵּךְ פְּרִי־בָטֶן› (“the-under
# God which debar-from-benefit from-you/your fruit belly”) — fact holds:
# debar-from-benefit-God-fruit-belly(Rachel)
m.fact("mana_Elohim_peri_vaten(rachel)")
# witness-tier presupposed read:
# criticized_here_and_rewritten_by_the_translation on am_i_in_place_of_God —
# read, not installed
m.witness_read("am_i_in_place_of_God", "criticized_here_and_rewritten_by_the_translation",
                cites=["Bereshit Rabbah 71:7", "Onkelos Genesis 30:2"])

# -------------------------- Gen.30.3 · THE_SARAI_SCRIPT_RERUN --------------
# וַתֹּאמֶר הִנֵּה אֲמָתִי בִלְהָה בֹּא אֵלֶיהָ וְתֵלֵד עַל־בִּרְכַּי
# וְאִבָּנֶה גַם־אָנֹכִי מִמֶּנָּה
# "[EN-AID] And she said: Behold my maid Bilhah; go in to her, that she may
# bear upon my knees, and I too may be built from her."
m.step("Gen.30.3")
# ‹בֹּא אֵלֶיהָ› (“come/bring to-her/its”) — Rachel speaks a demand — LET:
# come/bring-to-bilhah(Jacob)
m.declare("rachel", "LET",
          "bo_el_bilhah(yaaqov)")

# -------------------------- Gen.30.4 · THE_ROUTE_PERFORMED -----------------
# וַתִּתֶּן־לוֹ אֶת־בִּלְהָה שִׁפְחָתָהּ לְאִשָּׁה וַיָּבֹא אֵלֶיהָ יַעֲקֹב
# "[EN-AID] And she gave him Bilhah her maid as a wife; and Jacob went in to
# her."
m.step("Gen.30.4")
# ‹וַיָּבֹא אֵלֶיהָ יַעֲקֹב› (“and-come/bring to-her/its Jacob”) — demand
# settled (popped from the queue): come/bring-to-bilhah(Jacob)
m.result("bo_el_bilhah(yaaqov)", tmark="t2")

# -------------------------- Gen.30.5 · BILHAH_BEARS_A_SON ------------------
# וַתַּהַר בִּלְהָה וַתֵּלֶד לְיַעֲקֹב בֵּן
# "[EN-AID] And Bilhah conceived, and bore Jacob a son."
m.step("Gen.30.5")
# ‹וַתַּהַר בִּלְהָה וַתֵּלֶד לְיַעֲקֹב בֵּן› (“and-be-pregnant Bilhah and-
# bear-young to-Jacob son”) — the world gains: son-1-bilhah
m.install("ben_1_bilhah")

# -------------------------- Gen.30.6 · THE_FIFTH_WRITE_DAN -----------------
# וַתֹּאמֶר רָחֵל דָּנַנִּי אֱלֹהִים וְגַם שָׁמַע בְּקֹלִי וַיִּתֶּן־לִי
# בֵּן עַל־כֵּן קָרְאָה שְׁמוֹ דָּן
# "[EN-AID] And Rachel said: God has judged me, and has also heard my voice,
# and has given me a son; therefore she called his name Dan."
m.step("Gen.30.6")
# ‹קָרְאָה שְׁמוֹ דָּן› (“call name-him/its Daniel”) — named: son-1-bilhah
# := Daniel
m.name("ben_1_bilhah", "dan")

# -------------------------- Gen.30.7 · BILHAH_BEARS_A_SECOND ---------------
# וַתַּהַר עוֹד וַתֵּלֶד בִּלְהָה שִׁפְחַת רָחֵל בֵּן שֵׁנִי לְיַעֲקֹב
# "[EN-AID] And Bilhah, Rachel's maid, conceived again, and bore Jacob a
# second son."
m.step("Gen.30.7")
# ‹וַתַּהַר עוֹד וַתֵּלֶד בִּלְהָה› (“and-be-pregnant still/again and-bear-
# young Bilhah”) — the world gains: son-2-bilhah
m.install("ben_2_bilhah")

# -------------------------- Gen.30.8 · THE_SIXTH_WRITE_NAFTALI -------------
# וַתֹּאמֶר רָחֵל נַפְתּוּלֵי אֱלֹהִים נִפְתַּלְתִּי עִם־אֲחֹתִי
# גַּם־יָכֹלְתִּי וַתִּקְרָא שְׁמוֹ נַפְתָּלִי
# "[EN-AID] And Rachel said: Wrestlings of God I have wrestled with my
# sister; indeed I have prevailed. And she called his name Naphtali."
m.step("Gen.30.8")
# ‹וַתִּקְרָא שְׁמוֹ נַפְתָּלִי› (“and-call name-him/its Naphtali”) — named:
# son-2-bilhah := Naphtali
m.name("ben_2_bilhah", "naftali")
# witness-tier presupposed read: rebuilt_entirely_as_petition on
# the_wrestling_name — read, not installed
m.witness_read("the_wrestling_name", "rebuilt_entirely_as_petition",
                cites=["Onkelos Genesis 30:8", "Bereshit Rabbah 71:8"])

# -------------------------- Gen.30.9 · THE_ZILPAH_MOVE ---------------------
# וַתֵּרֶא לֵאָה כִּי עָמְדָה מִלֶּדֶת וַתִּקַּח אֶת־זִלְפָּה שִׁפְחָתָהּ
# וַתִּתֵּן אֹתָהּ לְיַעֲקֹב לְאִשָּׁה
# "[EN-AID] And Leah saw that she had ceased bearing; and she took Zilpah
# her maid, and gave her to Jacob as a wife."
m.step("Gen.30.9")
# ‹וַתִּקַּח אֶת־זִלְפָּה שִׁפְחָתָהּ וַתִּתֵּן אֹתָהּ לְיַעֲקֹב לְאִשָּׁה›
# (“and-take obj-marker Zilpah female-slave-her/its and-set obj-marker-
# her/its to-Jacob to-woman”) — fact holds: zilpah-given-to-Jacob(leah)
m.fact("zilpah_given_le_yaaqov(leah)")

# -------------------------- Gen.30.10 · ZILPAH_BEARS_A_SON -----------------
# וַתֵּלֶד זִלְפָּה שִׁפְחַת לֵאָה לְיַעֲקֹב בֵּן
# "[EN-AID] And Zilpah, Leah's maid, bore Jacob a son."
m.step("Gen.30.10")
# ‹וַתֵּלֶד זִלְפָּה שִׁפְחַת לֵאָה לְיַעֲקֹב בֵּן› (“and-bear-young Zilpah
# female-slave Leah to-Jacob son”) — the world gains: son-1-zilpah
m.install("ben_1_zilpah")
# witness-tier presupposed read: the_omission_is_complete_and_exact on
# bore_without_conceived — read, not installed
m.witness_read("bore_without_conceived", "the_omission_is_complete_and_exact",
                cites=["Bereshit Rabbah 71:9"])

# -------------------------- Gen.30.11 · THE_SEVENTH_WRITE_GAD_WRITTEN_AND_READ -
# וַתֹּאמֶר לֵאָה בגד בָּא גָד וַתִּקְרָא אֶת־שְׁמוֹ גָּד
# "[EN-AID] And Leah said: Fortune has come! And she called his name Gad."
m.step("Gen.30.11")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ גָּד› (“and-call obj-marker name-him/its Gad”) —
# named: son-1-zilpah := fortune
m.name("ben_1_zilpah", "gad")
# witness-grounded state (its own tier):
# resolved_in_the_record_by_its_own_subject on the_lineage_dispute
m.witness_state("the_lineage_dispute", "resolved_in_the_record_by_its_own_subject",
                cites=["Bereshit Rabbah 71:9"])

# -------------------------- Gen.30.12 · ZILPAH_BEARS_A_SECOND --------------
# וַתֵּלֶד זִלְפָּה שִׁפְחַת לֵאָה בֵּן שֵׁנִי לְיַעֲקֹב
# "[EN-AID] And Zilpah, Leah's maid, bore Jacob a second son."
m.step("Gen.30.12")
# ‹וַתֵּלֶד זִלְפָּה שִׁפְחַת לֵאָה בֵּן שֵׁנִי לְיַעֲקֹב› (“and-bear-young
# Zilpah female-slave Leah son second to-Jacob”) — the world gains:
# son-2-zilpah
m.install("ben_2_zilpah")

# -------------------------- Gen.30.13 · THE_EIGHTH_WRITE_ASHER -------------
# וַתֹּאמֶר לֵאָה בְּאָשְׁרִי כִּי אִשְּׁרוּנִי בָּנוֹת וַתִּקְרָא
# אֶת־שְׁמוֹ אָשֵׁר
# "[EN-AID] And Leah said: In my happiness! For the daughters will call me
# happy. And she called his name Asher."
m.step("Gen.30.13")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ אָשֵׁר› (“and-call obj-marker name-him/its Asher”)
# — named: son-2-zilpah := which
m.name("ben_2_zilpah", "asher")

# -------------------------- Gen.30.14 · THE_MANDRAKE_DEMAND ----------------
# וַיֵּלֶךְ רְאוּבֵן בִּימֵי קְצִיר־חִטִּים וַיִּמְצָא דוּדָאִים בַּשָּׂדֶה
# וַיָּבֵא אֹתָם אֶל־לֵאָה אִמּוֹ וַתֹּאמֶר רָחֵל אֶל־לֵאָה תְּנִי־נָא לִי
# מִדּוּדָאֵי בְּנֵךְ
# "[EN-AID] And Reuben went in the days of wheat harvest and found mandrakes
# in the field, and brought them to Leah his mother. And Rachel said to
# Leah: Give me, please, of your son's mandrakes."
m.step("Gen.30.14")
# ‹וַיֵּלֶךְ רְאוּבֵן בִּימֵי קְצִיר־חִטִּים› (“and-go Reuben in-day severed
# wheat”) — fact holds: boiler-found-by-Reuben(field)
m.fact("dudaim_found_by_reuven(sade)")
# ‹תְּנִי־נָא לִי מִדּוּדָאֵי בְּנֵךְ› (“set please to-me/my from-boiler
# son-you/your”) — Rachel speaks a demand — LET: set-boiler(leah)
m.declare("rachel", "LET",
          "teni_dudaim(leah)")
# witness-tier presupposed read: dispute_mined_for_its_unanimous_residue on
# what_the_boy_brought — read, not installed
m.witness_read("what_the_boy_brought", "dispute_mined_for_its_unanimous_residue",
                cites=["Bereshit Rabbah 72:2", "Onkelos Genesis 30:14"])

# -------------------------- Gen.30.15 · THE_EXCHANGE_SET -------------------
# וַתֹּאמֶר לָהּ הַמְעַט קַחְתֵּךְ אֶת־אִישִׁי וְלָקַחַת גַּם אֶת־דּוּדָאֵי
# בְּנִי וַתֹּאמֶר רָחֵל לָכֵן יִשְׁכַּב עִמָּךְ הַלַּיְלָה תַּחַת דּוּדָאֵי
# בְנֵךְ
# "[EN-AID] And she said to her: Is it a small thing that you have taken my
# husband? And would you take also my son's mandrakes? And Rachel said:
# Therefore he shall lie with you tonight, in exchange for your son's
# mandrakes."
m.step("Gen.30.15")
# ‹לָכֵן יִשְׁכַּב עִמָּךְ הַלַּיְלָה תַּחַת דּוּדָאֵי בְנֵךְ› (“to-so lie-
# down with-you/your the-night under boiler son-you/your”) — fact holds:
# laila-under-boiler(exchange-set)
m.fact("laila_tachat_dudaim(exchange_set)")
# witness-tier presupposed read: priced_on_both_sides_and_into_the_grave on
# the_traded_night — read, not installed
m.witness_read("the_traded_night", "priced_on_both_sides_and_into_the_grave",
                cites=["Bereshit Rabbah 72:3"])

# -------------------------- Gen.30.16 · THE_HIRE_NIGHT ---------------------
# וַיָּבֹא יַעֲקֹב מִן־הַשָּׂדֶה בָּעֶרֶב וַתֵּצֵא לֵאָה לִקְרָאתוֹ
# וַתֹּאמֶר אֵלַי תָּבוֹא כִּי שָׂכֹר שְׂכַרְתִּיךָ בְּדוּדָאֵי בְּנִי
# וַיִּשְׁכַּב עִמָּהּ בַּלַּיְלָה הוּא
# "[EN-AID] And Jacob came from the field in the evening, and Leah went out
# to meet him and said: To me you shall come in, for hiring I have hired you
# with my son's mandrakes. And he lay with her that night."
m.step("Gen.30.16")
# ‹שָׂכֹר שְׂכַרְתִּיךָ בְּדוּדָאֵי בְּנִי› (“hire hire-you/your in-boiler
# son-me/my”) — fact holds: hire-sekharticha(laila)
m.fact("sakhor_sekharticha(laila)")
# witness-tier presupposed read: working_hours_defaults_with_their_exception
# on came_in_from_the_field_at_evening — read, not installed
m.witness_read("came_in_from_the_field_at_evening", "working_hours_defaults_with_their_exception",
                cites=["Bereshit Rabbah 72:4"])

# -------------------------- Gen.30.17 · THE_FIFTH_SON_HEARD ----------------
# וַיִּשְׁמַע אֱלֹהִים אֶל־לֵאָה וַתַּהַר וַתֵּלֶד לְיַעֲקֹב בֵּן חֲמִישִׁי
# "[EN-AID] And God heard Leah, and she conceived and bore Jacob a fifth
# son."
m.step("Gen.30.17")
# ‹וַיִּשְׁמַע אֱלֹהִים אֶל־לֵאָה› (“and-hear God to Leah”) — fact holds:
# hear-God-to-leah
m.fact("shama_Elohim_el_leah")
# ‹וַתַּהַר וַתֵּלֶד לְיַעֲקֹב בֵּן חֲמִישִׁי› (“and-be-pregnant and-bear-
# young to-Jacob son fifth”) — the world gains: son-5-leah
m.install("ben_5_leah")

# -------------------------- Gen.30.18 · THE_NINTH_WRITE_YISASHKHAR ---------
# וַתֹּאמֶר לֵאָה נָתַן אֱלֹהִים שְׂכָרִי אֲשֶׁר־נָתַתִּי שִׁפְחָתִי
# לְאִישִׁי וַתִּקְרָא שְׁמוֹ יִשָּׂשכָר
# "[EN-AID] And Leah said: God has given my wage, because I gave my maid to
# my husband. And she called his name Issachar."
m.step("Gen.30.18")
# ‹וַתִּקְרָא שְׁמוֹ יִשָּׂשכָר› (“and-call name-him/its Issachar”) — named:
# son-5-leah := Issachar
m.name("ben_5_leah", "yisashkhar")
# witness-tier presupposed read:
# study_and_commerce_chartered_with_their_numbers on the_two_tribes — read,
# not installed
m.witness_read("the_two_tribes", "study_and_commerce_chartered_with_their_numbers",
                cites=["Bereshit Rabbah 72:5", "Bereshit Rabbah 99:10"])

# -------------------------- Gen.30.19 · THE_SIXTH_SON ----------------------
# וַתַּהַר עוֹד לֵאָה וַתֵּלֶד בֵּן־שִׁשִּׁי לְּיַעֲקֹב
# "[EN-AID] And Leah conceived again, and bore Jacob a sixth son."
m.step("Gen.30.19")
# ‹וַתַּהַר עוֹד לֵאָה וַתֵּלֶד בֵּן־שִׁשִּׁי לְּיַעֲקֹב› (“and-be-pregnant
# still/again Leah and-bear-young son sixth to-Jacob”) — the world gains:
# son-6-leah
m.install("ben_6_leah")

# -------------------------- Gen.30.20 · THE_TENTH_WRITE_ZEVULUN ------------
# וַתֹּאמֶר לֵאָה זְבָדַנִי אֱלֹהִים אֹתִי זֵבֶד טוֹב הַפַּעַם יִזְבְּלֵנִי
# אִישִׁי כִּי־יָלַדְתִּי לוֹ שִׁשָּׁה בָנִים וַתִּקְרָא אֶת־שְׁמוֹ זְבֻלוּן
# "[EN-AID] And Leah said: God has endowed me with a good endowment; this
# time my husband will dwell with me, for I have borne him six sons. And she
# called his name Zebulun."
m.step("Gen.30.20")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ זְבֻלוּן› (“and-call obj-marker name-him/its
# Zebulun”) — named: son-6-leah := Zebulun
m.name("ben_6_leah", "zevulun")

# -------------------------- Gen.30.21 · THE_ELEVENTH_WRITE_DINA ------------
# וְאַחַר יָלְדָה בַּת וַתִּקְרָא אֶת־שְׁמָהּ דִּינָה
# "[EN-AID] And afterward she bore a daughter, and called her name Dinah."
m.step("Gen.30.21")
# ‹וְאַחַר יָלְדָה בַּת› (“and-after bear-young daughter”) — the world
# gains: daughter-leah
m.install("bat_leah")
# ‹וַתִּקְרָא אֶת־שְׁמָהּ דִּינָה› (“and-call obj-marker name-her/its
# Dinah”) — named: daughter-leah := Dinah
m.name("bat_leah", "dina")
# witness-tier presupposed read: vain_prayer_rule_overridden_by_this_verse
# on the_daughter — read, not installed
m.witness_read("the_daughter", "vain_prayer_rule_overridden_by_this_verse",
                cites=["Bereshit Rabbah 72:6"])

# -------------------------- Gen.30.22 · THE_REMEMBERING_AND_THE_OPENING ----
# וַיִּזְכֹּר אֱלֹהִים אֶת־רָחֵל וַיִּשְׁמַע אֵלֶיהָ אֱלֹהִים וַיִּפְתַּח
# אֶת־רַחְמָהּ
# "[EN-AID] And God remembered Rachel, and God heard her, and opened her
# womb."
m.step("Gen.30.22")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־רָחֵל› (“and-mark God obj-marker Rachel”) —
# event: male — agent God; theme Rachel
m.event("zakhar", agent="Elohim", themes=["rachel"])
# ‹וַיִּפְתַּח אֶת־רַחְמָהּ› (“and-open-wide obj-marker womb-her/its”) —
# event: patach — agent God; theme rechem-Rachel
m.event("patach", agent="Elohim", themes=["rechem_rachel"])
# witness-grounded state (its own tier): operations_never_delegated on
# three_keys
m.witness_state("three_keys", "operations_never_delegated",
                cites=["Bereshit Rabbah 73:4"])
# witness-tier presupposed read: a_silence_confessed_earlier_in_this_block
# on what_was_remembered — read, not installed
m.witness_read("what_was_remembered", "a_silence_confessed_earlier_in_this_block",
                cites=["Bereshit Rabbah 71:8", "Bereshit Rabbah 73:4"])

# -------------------------- Gen.30.23 · THE_REPROACH_GATHERED_NON_POP ------
# וַתַּהַר וַתֵּלֶד בֵּן וַתֹּאמֶר אָסַף אֱלֹהִים אֶת־חֶרְפָּתִי
# "[EN-AID] And she conceived and bore a son, and said: God has gathered
# away my reproach."
m.step("Gen.30.23")
# ‹וַתַּהַר וַתֵּלֶד בֵּן› (“and-be-pregnant and-bear-young son”) — the
# world gains: son-1-Rachel
m.install("ben_1_rachel")
# ‹וַתֹּאמֶר אָסַף אֱלֹהִים אֶת־חֶרְפָּתִי› (“and-say gather-for-any-purpose
# God obj-marker contumely-me/my”) — fact holds: gather-for-any-purpose-God-
# cherpati(Rachel)
m.fact("asaf_Elohim_cherpati(rachel)")

# -------------------------- Gen.30.24 · THE_TWELFTH_WRITE_YOSEF_THE_OPEN_CARD -
# וַתִּקְרָא אֶת־שְׁמוֹ יוֹסֵף לֵאמֹר יֹסֵף יְהוָה לִי בֵּן אַחֵר
# "[EN-AID] And she called his name Joseph, saying: May YHWH add to me
# another son."
m.step("Gen.30.24")
# ‹וַתִּקְרָא אֶת־שְׁמוֹ יוֹסֵף לֵאמֹר› (“and-call obj-marker name-him/its
# Joseph to-say”) — named: son-1-Rachel := Joseph
m.name("ben_1_rachel", "yosef")
# witness-grounded state (its own tier):
# thanks_and_silence_as_heritable_capabilities on two_crafts
m.witness_state("two_crafts", "thanks_and_silence_as_heritable_capabilities",
                cites=["Bereshit Rabbah 71:5"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'bat_leah', 'ben_1_bilhah', 'ben_1_leah', 'ben_1_rachel', 'ben_1_zilpah', 'ben_2_bilhah', 'ben_2_leah', 'ben_2_zilpah', 'ben_3_leah', 'ben_4_leah', 'ben_5_leah', 'ben_6_leah'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ben_1_leah': 'reuven', 'ben_2_leah': 'shimon', 'ben_3_leah': 'levi', 'ben_4_leah': 'yehuda', 'ben_1_bilhah': 'dan', 'ben_2_bilhah': 'naftali', 'ben_1_zilpah': 'gad', 'ben_2_zilpah': 'asher', 'ben_5_leah': 'yisashkhar', 'ben_6_leah': 'zevulun', 'bat_leah': 'dina', 'ben_1_rachel': 'yosef'}
    assert m.REGISTRY["writes"] == 12
    assert m.tests_list() == []
    assert m.open_demands() == ['hava_banim(yaaqov)', 'teni_dudaim(leah)']
    assert len(m.SPECS["log"]) == 3
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['senua(leah)', 'aqara(rachel)', 'mana_Elohim_peri_vaten(rachel)', 'zilpah_given_le_yaaqov(leah)', 'dudaim_found_by_reuven(sade)', 'laila_tachat_dudaim(exchange_set)', 'sakhor_sekharticha(laila)', 'shama_Elohim_el_leah', 'asaf_Elohim_cherpati(rachel)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    assert sorted(m.WORLD["witnessed"]) == ['the_lineage_dispute', 'three_keys', 'two_crafts']
    assert m.WORLD["witnessed"]['the_lineage_dispute']["cites"] == ['Bereshit Rabbah 71:9']
    assert all('resolved_in_the_record_by_its_own_subject' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['three_keys']["cites"] == ['Bereshit Rabbah 73:4']
    assert all('operations_never_delegated' not in f for f in m.WORLD["facts"])
    assert m.WORLD["witnessed"]['two_crafts']["cites"] == ['Bereshit Rabbah 71:5']
    assert all('thanks_and_silence_as_heritable_capabilities' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_opened_womb', 'rendered_as_petition_and_acceptance_throughout'), ('thanks_at_the_fourth', 'gratitude_begins_where_entitlement_ends'), ('the_twelve_names', 'entered_under_a_four_cell_name_conduct_table'), ('give_me_children_or_i_die', 'proof_verse_for_the_living_as_dead_census'), ('am_i_in_place_of_God', 'criticized_here_and_rewritten_by_the_translation'), ('the_wrestling_name', 'rebuilt_entirely_as_petition'), ('bore_without_conceived', 'the_omission_is_complete_and_exact'), ('what_the_boy_brought', 'dispute_mined_for_its_unanimous_residue'), ('the_traded_night', 'priced_on_both_sides_and_into_the_grave'), ('came_in_from_the_field_at_evening', 'working_hours_defaults_with_their_exception'), ('the_two_tribes', 'study_and_commerce_chartered_with_their_numbers'), ('the_daughter', 'vain_prayer_rule_overridden_by_this_verse'), ('what_was_remembered', 'a_silence_confessed_earlier_in_this_block')]
    assert m.WITNESS_READS[0]["cites"] == ['Onkelos Genesis 30:22', 'Onkelos Genesis 30:6', 'Onkelos Genesis 29:31']
    assert all('rendered_as_petition_and_acceptance_throughout' not in f for f in m.WORLD["facts"])
    assert 'the_opened_womb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 71:4']
    assert all('gratitude_begins_where_entitlement_ends' not in f for f in m.WORLD["facts"])
    assert 'thanks_at_the_fourth' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 71:3']
    assert all('entered_under_a_four_cell_name_conduct_table' not in f for f in m.WORLD["facts"])
    assert 'the_twelve_names' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 71:6', 'Bereshit Rabbah 45:2']
    assert all('proof_verse_for_the_living_as_dead_census' not in f for f in m.WORLD["facts"])
    assert 'give_me_children_or_i_die' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 71:7', 'Onkelos Genesis 30:2']
    assert all('criticized_here_and_rewritten_by_the_translation' not in f for f in m.WORLD["facts"])
    assert 'am_i_in_place_of_God' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Onkelos Genesis 30:8', 'Bereshit Rabbah 71:8']
    assert all('rebuilt_entirely_as_petition' not in f for f in m.WORLD["facts"])
    assert 'the_wrestling_name' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 71:9']
    assert all('the_omission_is_complete_and_exact' not in f for f in m.WORLD["facts"])
    assert 'bore_without_conceived' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 72:2', 'Onkelos Genesis 30:14']
    assert all('dispute_mined_for_its_unanimous_residue' not in f for f in m.WORLD["facts"])
    assert 'what_the_boy_brought' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 72:3']
    assert all('priced_on_both_sides_and_into_the_grave' not in f for f in m.WORLD["facts"])
    assert 'the_traded_night' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 72:4']
    assert all('working_hours_defaults_with_their_exception' not in f for f in m.WORLD["facts"])
    assert 'came_in_from_the_field_at_evening' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[10]["cites"] == ['Bereshit Rabbah 72:5', 'Bereshit Rabbah 99:10']
    assert all('study_and_commerce_chartered_with_their_numbers' not in f for f in m.WORLD["facts"])
    assert 'the_two_tribes' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[11]["cites"] == ['Bereshit Rabbah 72:6']
    assert all('vain_prayer_rule_overridden_by_this_verse' not in f for f in m.WORLD["facts"])
    assert 'the_daughter' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[12]["cites"] == ['Bereshit Rabbah 71:8', 'Bereshit Rabbah 73:4']
    assert all('a_silence_confessed_earlier_in_this_block' not in f for f in m.WORLD["facts"])
    assert 'what_was_remembered' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
