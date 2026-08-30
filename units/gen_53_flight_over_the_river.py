#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_53_flight_over_the_river — 31:1-21
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_53_flight_over_the_river.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The return-command and the flight over the river (31:1-21)"""
from machine import Machine

m = Machine("gen_53_flight_over_the_river")

# -------------------------- Gen.31.1 · THE_SONS_COMPLAINT ------------------
# וַיִּשְׁמַע אֶת־דִּבְרֵי בְנֵי־לָבָן לֵאמֹר לָקַח יַעֲקֹב אֵת כָּל־אֲשֶׁר
# לְאָבִינוּ וּמֵאֲשֶׁר לְאָבִינוּ עָשָׂה אֵת כָּל־הַכָּבֹד הַזֶּה
# "[EN-AID] And he heard the words of Laban's sons, saying: Jacob has taken
# all that was our father's, and from what was our father's he has made all
# this glory."
m.step("Gen.31.1")
# ‹וַיִּשְׁמַע אֶת־דִּבְרֵי בְנֵי־לָבָן לֵאמֹר› (“and-hear obj-marker
# word/thing son Laban to-say”) — fact holds: take-Jacob-all-which-to-
# avinu(word/thing-son-Laban)
m.fact("laqach_yaaqov_kol_asher_le_avinu(divre_vene_lavan)")
# witness-tier presupposed read: three_stage_trigger_ending_in_a_command on
# the_sons_words — read, not installed
m.witness_read("the_sons_words", "three_stage_trigger_ending_in_a_command",
                cites=["Bereshit Rabbah 73:12"])

# -------------------------- Gen.31.2 · THE_CHANGED_FACE --------------------
# וַיַּרְא יַעֲקֹב אֶת־פְּנֵי לָבָן וְהִנֵּה אֵינֶנּוּ עִמּוֹ כִּתְמוֹל
# שִׁלְשׁוֹם
# "[EN-AID] And Jacob saw the face of Laban, and behold, it was not toward
# him as yesterday and the day before."
m.step("Gen.31.2")
# ‹וְהִנֵּה אֵינֶנּוּ עִמּוֹ כִּתְמוֹל שִׁלְשׁוֹם› (“and-behold there-is-
# not-him/its with-him/its like-ago trebly”) — fact holds: face-Laban-not-
# khi-temol-trebly(Jacob)
m.fact("pene_lavan_lo_khi_temol_shilshom(yaaqov)")

# -------------------------- Gen.31.3 · THE_RETURN_COMMAND ------------------
# וַיֹּאמֶר יְהוָה אֶל־יַעֲקֹב שׁוּב אֶל־אֶרֶץ אֲבוֹתֶיךָ וּלְמוֹלַדְתֶּךָ
# וְאֶהְיֶה עִמָּךְ
# "[EN-AID] And YHWH said to Jacob: Return to the land of your fathers and
# to your kindred, and I will be with you."
m.step("Gen.31.3")
# ‹שׁוּב אֶל־אֶרֶץ אֲבוֹתֶיךָ וּלְמוֹלַדְתֶּךָ› (“return to earth father-
# you/your and-to-nativity-you/your”) — the-LORD speaks a demand — LET:
# return-earth-avot(Jacob)
m.declare("YHWH", "LET",
          "shuv_eretz_avot(yaaqov)")
# witness-tier presupposed read:
# blessing_on_property_conditioned_on_geography on return_to_your_land —
# read, not installed
m.witness_read("return_to_your_land", "blessing_on_property_conditioned_on_geography",
                cites=["Bereshit Rabbah 74:1", "Onkelos Genesis 31:3"])

# -------------------------- Gen.31.4 · THE_FIELD_SUMMONS -------------------
# וַיִּשְׁלַח יַעֲקֹב וַיִּקְרָא לְרָחֵל וּלְלֵאָה הַשָּׂדֶה אֶל־צֹאנוֹ
# "[EN-AID] And Jacob sent and called Rachel and Leah to the field, to his
# flock."
m.step("Gen.31.4")
# ‹וַיִּשְׁלַח יַעֲקֹב וַיִּקְרָא לְרָחֵל וּלְלֵאָה› (“and-send Jacob and-
# call to-Rachel and-to-Leah”) — fact holds: qara-to-Rachel-and-to-leah(the-
# field)
m.fact("qara_le_rachel_u_le_leah(ha_sade)")
# witness-tier presupposed read: prudence_rule_from_the_setting on
# counsel_in_the_open_field — read, not installed
m.witness_read("counsel_in_the_open_field", "prudence_rule_from_the_setting",
                cites=["Bereshit Rabbah 74:2"])

# -------------------------- Gen.31.5 · THE_CONDITION_DECLARED_TRUE ---------
# וַיֹּאמֶר לָהֶן רֹאֶה אָנֹכִי אֶת־פְּנֵי אֲבִיכֶן כִּי־אֵינֶנּוּ אֵלַי
# כִּתְמֹל שִׁלְשֹׁם וֵאלֹהֵי אָבִי הָיָה עִמָּדִי
# "[EN-AID] And he said to them: I see your father's face, that it is not
# toward me as yesterday and the day before; but the God of my father has
# been with me."
m.step("Gen.31.5")
# ‹וֵאלֹהֵי אָבִי הָיָה עִמָּדִי› (“and-God father-me/my be along-with-
# me/my”) — fact holds: elohe-avi-be-with-me(Jacob)
m.fact("elohe_avi_haya_imadi(yaaqov)")

# -------------------------- Gen.31.6 · THE_STRENGTH_LEDGER -----------------
# וְאַתֵּנָה יְדַעְתֶּן כִּי בְּכָל־כֹּחִי עָבַדְתִּי אֶת־אֲבִיכֶן
# "[EN-AID] And you know that with all my strength I have served your
# father."
m.step("Gen.31.6")
# ‹כִּי בְּכָל־כֹּחִי עָבַדְתִּי אֶת› (“that in-all vigor-me/my work/serve
# obj-marker”) — fact holds: in-all-kochi-work/serve(thou-and-thee)
m.fact("be_khol_kochi_avadti(atena)")

# -------------------------- Gen.31.7 · THE_TEN_CHANGES ---------------------
# וַאֲבִיכֶן הֵתֶל בִּי וְהֶחֱלִף אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת מֹנִים
# וְלֹא־נְתָנוֹ אֱלֹהִים לְהָרַע עִמָּדִי
# "[EN-AID] And your father has mocked me and changed my wages ten times;
# but God did not give him leave to harm me."
m.step("Gen.31.7")
# ‹וַאֲבִיכֶן הֵתֶל בִּי וְהֶחֱלִף אֶת־מַשְׂכֻּרְתִּי עֲשֶׂרֶת מֹנִים›
# (“and-father-ward deride in-me/my and-slide-by obj-marker wages-me/my ten
# something-weighed-out”) — fact holds: slide-by-maskurti-ten-something-
# weighed-out(Laban)
m.fact("hechelif_maskurti_aseret_monim(lavan)")

# -------------------------- Gen.31.8 · THE_WAGE_FLIP_RULE ------------------
# אִם־כֹּה יֹאמַר נְקֻדִּים יִהְיֶה שְׂכָרֶךָ וְיָלְדוּ כָל־הַצֹּאן
# נְקֻדִּים וְאִם־כֹּה יֹאמַר עֲקֻדִּים יִהְיֶה שְׂכָרֶךָ וְיָלְדוּ
# כָל־הַצֹּאן עֲקֻדִּים
# "[EN-AID] If he said thus: The speckled shall be your wage — then all the
# flock bore speckled; and if he said thus: The striped shall be your wage —
# then all the flock bore striped."
m.step("Gen.31.8")
# ‹אִם־כֹּה יֹאמַר נְקֻדִּים יִהְיֶה שְׂכָרֶךָ› (“if like-this say spotted
# be wage-you/your”) — fact holds: if-this-say-and-bear-young-so(sekharekha)
m.fact("im_ko_yomar_ve_yaldu_khen(sekharekha)")

# -------------------------- Gen.31.9 · THE_RESCUE_VERB_BORN ----------------
# וַיַּצֵּל אֱלֹהִים אֶת־מִקְנֵה אֲבִיכֶם וַיִּתֶּן־לִי
# "[EN-AID] And God has rescued your father's livestock and given it to me."
m.step("Gen.31.9")
# ‹וַיַּצֵּל אֱלֹהִים אֶת־מִקְנֵה אֲבִיכֶם וַיִּתֶּן־לִי› (“and-snatch-away
# God obj-marker something-bought father-you/your(pl) and-set to-me/my”) —
# fact holds: and-snatch-away-God-and-set-to-me(something-bought)
m.fact("va_yatzel_Elohim_va_yiten_li(miqne)")

# -------------------------- Gen.31.10 · THE_DREAM_AND_THE_CHANGED_ADJECTIVE -
# וַיְהִי בְּעֵת יַחֵם הַצֹּאן וָאֶשָּׂא עֵינַי וָאֵרֶא בַּחֲלוֹם וְהִנֵּה
# הָעַתֻּדִים הָעֹלִים עַל־הַצֹּאן עֲקֻדִּים נְקֻדִּים וּבְרֻדִּים
# "[EN-AID] And it was at the time the flock conceived, that I lifted my
# eyes and saw in a dream: and behold, the he-goats going up on the flock
# were striped, speckled, and mottled."
m.step("Gen.31.10")
# ‹וָאֶשָּׂא עֵינַי וָאֵרֶא בַּחֲלוֹם› (“and-lift/carry eye-me/my and-see
# in-dream”) — fact holds: and-see-in-the-chalom-prepared(go-up)
m.fact("va_ere_ba_chalom_atudim(olim)")

# -------------------------- Gen.31.11 · THE_HINENI -------------------------
# וַיֹּאמֶר אֵלַי מַלְאַךְ הָאֱלֹהִים בַּחֲלוֹם יַעֲקֹב וָאֹמַר הִנֵּנִי
# "[EN-AID] And the angel of God said to me in the dream: Jacob. And I said:
# Here I am."
m.step("Gen.31.11")
# ‹וָאֹמַר הִנֵּנִי› (“and-say behold-me/my”) — fact holds: behold-I(Jacob)
m.fact("hineni(yaaqov)")
# witness-tier presupposed read: medium_fixed_by_comparing_two_verses on
# the_angel_in_the_dream — read, not installed
m.witness_read("the_angel_in_the_dream", "medium_fixed_by_comparing_two_verses",
                cites=["Bereshit Rabbah 82:3"])

# -------------------------- Gen.31.12 · THE_RETOLD_LIFT_YOUR_EYES ----------
# וַיֹּאמֶר שָׂא־נָא עֵינֶיךָ וּרְאֵה כָּל־הָעַתֻּדִים הָעֹלִים עַל־הַצֹּאן
# עֲקֻדִּים נְקֻדִּים וּבְרֻדִּים כִּי רָאִיתִי אֵת כָּל־אֲשֶׁר לָבָן עֹשֶׂה
# לָּךְ
# "[EN-AID] And he said: Lift now your eyes and see: all the he-goats going
# up on the flock are striped, speckled, and mottled; for I have seen all
# that Laban is doing to you."
m.step("Gen.31.12")
# ‹שָׂא־נָא עֵינֶיךָ וּרְאֵה› (“lift/carry please eye-you/your and-see”) —
# fact holds: retold-lift/carry-enekha-and-see(dream)
m.fact("retold_sa_enekha_u_ree(ba_chalom)")

# -------------------------- Gen.31.13 · THE_SELF_NAME_BY_THE_REGISTRY ------
# אָנֹכִי הָאֵל בֵּית־אֵל אֲשֶׁר מָשַׁחְתָּ שָּׁם מַצֵּבָה אֲשֶׁר נָדַרְתָּ
# לִּי שָׁם נֶדֶר עַתָּה קוּם צֵא מִן־הָאָרֶץ הַזֹּאת וְשׁוּב אֶל־אֶרֶץ
# מוֹלַדְתֶּךָ
# "[EN-AID] I am the God of Bethel, where you anointed a pillar, where you
# vowed to Me a vow. Now arise, go out from this land, and return to the
# land of your kindred."
m.step("Gen.31.13")
# ‹אָנֹכִי הָאֵל בֵּית־אֵל אֲשֶׁר מָשַׁחְתָּ שָּׁם מַצֵּבָה אֲשֶׁר נָדַרְתָּ
# לִּי שָׁם נֶדֶר› (“the-strength Beth-el which rub-with-oil there pillar
# which promise to-me/my there promise”) — fact holds: anokhi-the-to-bet-
# to(rub-with-oil-pillar-promise-promise)
m.fact("anokhi_ha_el_bet_el(mashachta_matzeva_nadarta_neder)")

# -------------------------- Gen.31.14 · THE_INHERITANCE_QUESTION -----------
# וַתַּעַן רָחֵל וְלֵאָה וַתֹּאמַרְנָה לוֹ הַעוֹד לָנוּ חֵלֶק וְנַחֲלָה
# בְּבֵית אָבִינוּ
# "[EN-AID] And Rachel and Leah answered and said to him: Have we still a
# portion and an inheritance in our father's house?"
m.step("Gen.31.14")
# ‹הַעוֹד לָנוּ חֵלֶק וְנַחֲלָה בְּבֵית אָבִינוּ› (“the-still/again to-
# us/our smoothness and-inheritance in-house father-us/our”) — fact holds:
# the-still/again-lanu-smoothness-and-inheritance(Rachel-and-leah)
m.fact("ha_od_lanu_cheleq_ve_nachala(rachel_ve_leah)")

# -------------------------- Gen.31.15 · THE_SOLD_DAUGHTERS -----------------
# הֲלוֹא נָכְרִיּוֹת נֶחְשַׁבְנוּ לוֹ כִּי מְכָרָנוּ וַיֹּאכַל גַּם־אָכוֹל
# אֶת־כַּסְפֵּנוּ
# "[EN-AID] Are we not reckoned foreign women to him? For he has sold us,
# and has utterly devoured our silver."
m.step("Gen.31.15")
# ‹הֲלוֹא נָכְרִיּוֹת נֶחְשַׁבְנוּ לוֹ כִּי מְכָרָנוּ› (“is-it-not strange
# plait to-him/its that sell-us/our”) — fact holds: nokhriot-plait-that-
# mekharanu(lahen)
m.fact("nokhriot_nechshavnu_ki_mekharanu(lahen)")

# -------------------------- Gen.31.16 · THE_DO_ALL_DEMAND ------------------
# כִּי כָל־הָעֹשֶׁר אֲשֶׁר הִצִּיל אֱלֹהִים מֵאָבִינוּ לָנוּ הוּא
# וּלְבָנֵינוּ וְעַתָּה כֹּל אֲשֶׁר אָמַר אֱלֹהִים אֵלֶיךָ עֲשֵׂה
# "[EN-AID] For all the wealth which God has rescued from our father — it is
# ours and our children's. And now, all that God has said to you — do."
m.step("Gen.31.16")
# ‹וְעַתָּה כֹּל אֲשֶׁר אָמַר אֱלֹהִים אֵלֶיךָ עֲשֵׂה› (“and-now all which
# say God to-you/your make”) — Rachel-and-leah speaks a demand — LET: make-
# all-which-say(Jacob)
m.declare("rachel_ve_leah", "LET",
          "ase_kol_asher_amar(yaaqov)")

# -------------------------- Gen.31.17 · THE_RISING -------------------------
# וַיָּקָם יַעֲקֹב וַיִּשָּׂא אֶת־בָּנָיו וְאֶת־נָשָׁיו עַל־הַגְּמַלִּים
# "[EN-AID] And Jacob arose, and lifted his sons and his wives onto the
# camels."
m.step("Gen.31.17")
# ‹וַיָּקָם יַעֲקֹב› (“and-arise Jacob”) — fact holds: and-arise-and-
# lift/carry(Jacob)
m.fact("va_yaqam_va_yisa(yaaqov)")

# -------------------------- Gen.31.18 · THE_ABRAM_FORMULA ------------------
# וַיִּנְהַג אֶת־כָּל־מִקְנֵהוּ וְאֶת־כָּל־רְכֻשׁוֹ אֲשֶׁר רָכָשׁ מִקְנֵה
# קִנְיָנוֹ אֲשֶׁר רָכַשׁ בְּפַדַּן אֲרָם לָבוֹא אֶל־יִצְחָק אָבִיו אַרְצָה
# כְּנָעַן
# "[EN-AID] And he drove all his livestock and all his property which he had
# acquired — the livestock of his getting, which he acquired in Paddan-Aram
# — to come to Isaac his father, to the land of Canaan."
m.step("Gen.31.18")
# ‹וַיִּנְהַג אֶת־כָּל־מִקְנֵהוּ וְאֶת־כָּל־רְכֻשׁוֹ› (“and-drive-forth obj-
# marker all something-bought-him/its and-obj-marker all property-him/its”)
# — fact holds: and-drive-forth-something-bought-rekhush(to-come/bring-to-
# Isaac)
m.fact("va_yinhag_miqne_rekhush(la_vo_el_yitzchaq)")

# -------------------------- Gen.31.19 · THE_SHEARING_AND_THE_THEFT ---------
# וְלָבָן הָלַךְ לִגְזֹז אֶת־צֹאנוֹ וַתִּגְנֹב רָחֵל אֶת־הַתְּרָפִים אֲשֶׁר
# לְאָבִיהָ
# "[EN-AID] And Laban had gone to shear his flock; and Rachel stole the
# terafim that were her father's."
m.step("Gen.31.19")
# ‹וַתִּגְנֹב רָחֵל אֶת־הַתְּרָפִים אֲשֶׁר› (“and-steal Rachel obj-marker
# the-Teraphim-a-family-idol which”) — fact holds: and-steal-Rachel-
# Teraphim-a-family-idol(Laban-gozez)
m.fact("va_tignov_rachel_terafim(lavan_gozez)")
# witness-tier presupposed read: motive_supplied_here_verb_removed_there on
# the_theft — read, not installed
m.witness_read("the_theft", "motive_supplied_here_verb_removed_there",
                cites=["Bereshit Rabbah 74:5", "Onkelos Genesis 31:19", "Onkelos Genesis 31:20", "Onkelos Genesis 31:21"])
# witness-tier presupposed read: never_called_gods_in_the_translation on
# the_images — read, not installed
m.witness_read("the_images", "never_called_gods_in_the_translation",
                cites=["Onkelos Genesis 31:19", "Onkelos Genesis 31:30"])
# witness-tier presupposed read: tracked_as_cause_across_three_verses on
# the_curse_chain — read, not installed
m.witness_read("the_curse_chain", "tracked_as_cause_across_three_verses",
                cites=["Bereshit Rabbah 74:4"])
# witness-tier presupposed read: taunt_in_a_later_block_with_the_retort_kept
# on the_theft_echo — read, not installed
m.witness_read("the_theft_echo", "taunt_in_a_later_block_with_the_retort_kept",
                cites=["Bereshit Rabbah 92:8"])

# -------------------------- Gen.31.20 · THE_HEART_THEFT --------------------
# וַיִּגְנֹב יַעֲקֹב אֶת־לֵב לָבָן הָאֲרַמִּי עַל־בְּלִי הִגִּיד לוֹ כִּי
# בֹרֵחַ הוּא
# "[EN-AID] And Jacob stole the heart of Laban the Aramean, in that he did
# not tell him that he was fleeing."
m.step("Gen.31.20")
# ‹וַיִּגְנֹב יַעֲקֹב אֶת־לֵב לָבָן הָאֲרַמִּי› (“and-steal Jacob obj-marker
# heart Laban the-Aramite”) — fact holds: and-steal-Jacob-heart-Laban(the-
# Aramite)
m.fact("va_yignov_yaaqov_lev_lavan(ha_arami)")
# witness-tier presupposed read: declared_portentous_wherever_it_occurs on
# shearing — read, not installed
m.witness_read("shearing", "declared_portentous_wherever_it_occurs",
                cites=["Bereshit Rabbah 74:5"])

# -------------------------- Gen.31.21 · THE_FLIGHT_AND_THE_RIVER -----------
# וַיִּבְרַח הוּא וְכָל־אֲשֶׁר־לוֹ וַיָּקָם וַיַּעֲבֹר אֶת־הַנָּהָר
# וַיָּשֶׂם אֶת־פָּנָיו הַר הַגִּלְעָד
# "[EN-AID] And he fled, he and all that was his; and he arose and crossed
# the river, and set his face toward the mountain of Gilead."
m.step("Gen.31.21")
# ‹וַיִּבְרַח הוּא וְכָל־אֲשֶׁר־לוֹ וַיָּקָם וַיַּעֲבֹר אֶת־הַנָּהָר› (“and-
# bolt he/it and-all which to-him/its and-arise and-pass-over obj-marker
# the-river”) — fact holds: and-bolt-and-pass-over-the-river(panav-mountain-
# the-Gilead)
m.fact("va_yivrach_va_yaavor_ha_nahar(panav_har_ha_gilad)")
# witness-grounded state (its own tier): suspicion_concealment_and_a_mercy
# on the_search_ahead
m.witness_state("the_search_ahead", "suspicion_concealment_and_a_mercy",
                cites=["Bereshit Rabbah 74:9"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shuv_eretz_avot(yaaqov)', 'ase_kol_asher_amar(yaaqov)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['laqach_yaaqov_kol_asher_le_avinu(divre_vene_lavan)', 'pene_lavan_lo_khi_temol_shilshom(yaaqov)', 'qara_le_rachel_u_le_leah(ha_sade)', 'elohe_avi_haya_imadi(yaaqov)', 'be_khol_kochi_avadti(atena)', 'hechelif_maskurti_aseret_monim(lavan)', 'im_ko_yomar_ve_yaldu_khen(sekharekha)', 'va_yatzel_Elohim_va_yiten_li(miqne)', 'va_ere_ba_chalom_atudim(olim)', 'hineni(yaaqov)', 'retold_sa_enekha_u_ree(ba_chalom)', 'anokhi_ha_el_bet_el(mashachta_matzeva_nadarta_neder)', 'ha_od_lanu_cheleq_ve_nachala(rachel_ve_leah)', 'nokhriot_nechshavnu_ki_mekharanu(lahen)', 'va_yaqam_va_yisa(yaaqov)', 'va_yinhag_miqne_rekhush(la_vo_el_yitzchaq)', 'va_tignov_rachel_terafim(lavan_gozez)', 'va_yignov_yaaqov_lev_lavan(ha_arami)', 'va_yivrach_va_yaavor_ha_nahar(panav_har_ha_gilad)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 2
    assert sorted(m.WORLD["witnessed"]) == ['the_search_ahead']
    assert m.WORLD["witnessed"]['the_search_ahead']["cites"] == ['Bereshit Rabbah 74:9']
    assert all('suspicion_concealment_and_a_mercy' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('the_sons_words', 'three_stage_trigger_ending_in_a_command'), ('return_to_your_land', 'blessing_on_property_conditioned_on_geography'), ('counsel_in_the_open_field', 'prudence_rule_from_the_setting'), ('the_angel_in_the_dream', 'medium_fixed_by_comparing_two_verses'), ('the_theft', 'motive_supplied_here_verb_removed_there'), ('the_images', 'never_called_gods_in_the_translation'), ('the_curse_chain', 'tracked_as_cause_across_three_verses'), ('the_theft_echo', 'taunt_in_a_later_block_with_the_retort_kept'), ('shearing', 'declared_portentous_wherever_it_occurs')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 73:12']
    assert all('three_stage_trigger_ending_in_a_command' not in f for f in m.WORLD["facts"])
    assert 'the_sons_words' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 74:1', 'Onkelos Genesis 31:3']
    assert all('blessing_on_property_conditioned_on_geography' not in f for f in m.WORLD["facts"])
    assert 'return_to_your_land' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 74:2']
    assert all('prudence_rule_from_the_setting' not in f for f in m.WORLD["facts"])
    assert 'counsel_in_the_open_field' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 82:3']
    assert all('medium_fixed_by_comparing_two_verses' not in f for f in m.WORLD["facts"])
    assert 'the_angel_in_the_dream' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 74:5', 'Onkelos Genesis 31:19', 'Onkelos Genesis 31:20', 'Onkelos Genesis 31:21']
    assert all('motive_supplied_here_verb_removed_there' not in f for f in m.WORLD["facts"])
    assert 'the_theft' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Onkelos Genesis 31:19', 'Onkelos Genesis 31:30']
    assert all('never_called_gods_in_the_translation' not in f for f in m.WORLD["facts"])
    assert 'the_images' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 74:4']
    assert all('tracked_as_cause_across_three_verses' not in f for f in m.WORLD["facts"])
    assert 'the_curse_chain' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 92:8']
    assert all('taunt_in_a_later_block_with_the_retort_kept' not in f for f in m.WORLD["facts"])
    assert 'the_theft_echo' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 74:5']
    assert all('declared_portentous_wherever_it_occurs' not in f for f in m.WORLD["facts"])
    assert 'shearing' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
