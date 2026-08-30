#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_56_blessing_returned_first_altar — 33:1-20
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_56_blessing_returned_first_altar.yaml) is
# CANONICAL (Pre-Code); this file is a derived, runnable rendering. Do not
# edit — regenerate. The assertion block at the bottom is baked from the
# Stage D interpreter's actual final state: running this file re-proves the
# unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The blessing returned and the first altar (33:1-20)"""
from machine import Machine

m = Machine("gen_56_blessing_returned_first_altar")

# -------------------------- Gen.33.1 · THE_LIFTED_EYES_AND_THE_SPLIT -------
# וַיִּשָּׂא יַעֲקֹב עֵינָיו וַיַּרְא וְהִנֵּה עֵשָׂו בָּא וְעִמּוֹ אַרְבַּע
# מֵאוֹת אִישׁ וַיַּחַץ אֶת־הַיְלָדִים עַל־לֵאָה וְעַל־רָחֵל וְעַל שְׁתֵּי
# הַשְּׁפָחוֹת
# "[EN-AID] And Jacob lifted his eyes and saw, and behold, Esau was coming,
# and with him four hundred men. And he divided the children unto Leah and
# unto Rachel and unto the two maids."
m.step("Gen.33.1")
# ‹וַיִּשָּׂא יַעֲקֹב עֵינָיו וַיַּרְא וְהִנֵּה עֵשָׂו בָּא› (“and-
# lift/carry Jacob eye-him/its and-see and-behold Esau come/bring”) — fact
# holds: and-see-Esau-come/bring-and-cut(four-hundred-man)
m.fact("va_yar_esav_ba_va_yachatz(arba_meot_ish)")
# witness-tier presupposed read: collective_merit_disaggregated_under_test
# on dividing_the_children — read, not installed
m.witness_read("dividing_the_children", "collective_merit_disaggregated_under_test",
                cites=["Bereshit Rabbah 78:7"])

# -------------------------- Gen.33.2 · THE_ORDER_OF_LOVE -------------------
# וַיָּשֶׂם אֶת־הַשְּׁפָחוֹת וְאֶת־יַלְדֵיהֶן רִאשֹׁנָה וְאֶת־לֵאָה
# וִילָדֶיהָ אַחֲרֹנִים וְאֶת־רָחֵל וְאֶת־יוֹסֵף אַחֲרֹנִים
# "[EN-AID] And he put the maids and their children first, and Leah and her
# children behind, and Rachel and Joseph hindmost."
m.step("Gen.33.2")
# ‹וַיָּשֶׂם אֶת־הַשְּׁפָחוֹת וְאֶת־יַלְדֵיהֶן רִאשֹׁנָה› (“and-put/set obj-
# marker the-female-slave and-obj-marker child-them/their first”) — fact
# holds: first-other-other(seder-the-camp)
m.fact("rishona_acharonim_acharonim(seder_ha_machane)")

# -------------------------- Gen.33.3 · THE_BOW_INVERTED --------------------
# וְהוּא עָבַר לִפְנֵיהֶם וַיִּשְׁתַּחוּ אַרְצָה שֶׁבַע פְּעָמִים
# עַד־גִּשְׁתּוֹ עַד־אָחִיו
# "[EN-AID] And he himself crossed over before them and bowed to the ground
# seven times, until he came near to his brother."
m.step("Gen.33.3")
# ‹וַיִּשְׁתַּחוּ אַרְצָה שֶׁבַע פְּעָמִים› (“and-afflict earth-ward seven
# stroke”) — fact holds: and-afflict-seven-stroke(hipukh-the-berakha)
m.fact("va_yishtachu_sheva_peamim(hipukh_ha_berakha)")

# -------------------------- Gen.33.4 · THE_HAND_BECOMES_ARMS ---------------
# וַיָּרָץ עֵשָׂו לִקְרָאתוֹ וַיְחַבְּקֵהוּ וַיִּפֹּל עַל־צַוָּארָו
# וַׄיִּׄשָּׁׄקֵׄהׄוּׄ וַיִּבְכּוּ
# "[EN-AID] And Esau ran to meet him and embraced him, and fell on his neck
# and kissed him; and they wept."
m.step("Gen.33.4")
# ‹וַיָּרָץ עֵשָׂו לִקְרָאתוֹ וַיְחַבְּקֵהוּ› (“and-run Esau to-
# encountering-him/its and-clasp-him/its”) — fact holds: and-yechabqehu-and-
# weep(Esau-and-Jacob)
m.fact("va_yechabqehu_va_yivku(esav_ve_yaaqov)")
# witness-tier presupposed read: the_rules_own_tie_case_confirmed_in_our_ink
# on the_dotted_kiss — read, not installed
m.witness_read("the_dotted_kiss", "the_rules_own_tie_case_confirmed_in_our_ink",
                cites=["Bereshit Rabbah 78:9"])

# -------------------------- Gen.33.5 · THE_GRACE_VERB_IS_BORN --------------
# וַיִּשָּׂא אֶת־עֵינָיו וַיַּרְא אֶת־הַנָּשִׁים וְאֶת־הַיְלָדִים וַיֹּאמֶר
# מִי־אֵלֶּה לָּךְ וַיֹּאמַר הַיְלָדִים אֲשֶׁר־חָנַן אֱלֹהִים אֶת־עַבְדֶּךָ
# "[EN-AID] And he lifted his eyes and saw the women and the children, and
# said: Who are these to you? And he said: The children with whom God has
# graced your servant."
m.step("Gen.33.5")
# ‹חָנַן אֱלֹהִים אֶת־עַבְדֶּךָ› (“bend God obj-marker servant-you/your”) —
# fact holds: the-child-which-bend-God(maane-Jacob)
m.fact("ha_yeladim_asher_chanan_Elohim(maane_yaaqov)")
# witness-tier presupposed read: one_grace_outstanding_until_43_29 on
# the_children_God_graced — read, not installed
m.witness_read("the_children_God_graced", "one_grace_outstanding_until_43_29",
                cites=["Bereshit Rabbah 78:10"])

# -------------------------- Gen.33.6 · THE_FIRST_WAVE ----------------------
# וַתִּגַּשְׁןָ הַשְּׁפָחוֹת הֵנָּה וְיַלְדֵיהֶן וַתִּשְׁתַּחֲוֶיןָ
# "[EN-AID] And the maids came near, they and their children, and they
# bowed."
m.step("Gen.33.6")
# ‹וַתִּגַּשְׁןָ הַשְּׁפָחוֹת הֵנָּה וְיַלְדֵיהֶן וַתִּשְׁתַּחֲוֶיןָ› (“and-
# be the-female-slave themselves and-child-them/their and-afflict”) — fact
# holds: and-be-and-afflict(the-female-slave)
m.fact("va_tigashna_va_tishtachavena(ha_shefachot)")

# -------------------------- Gen.33.7 · THE_SECOND_AND_THIRD_WAVES ----------
# וַתִּגַּשׁ גַּם־לֵאָה וִילָדֶיהָ וַיִּשְׁתַּחֲווּ וְאַחַר נִגַּשׁ יוֹסֵף
# וְרָחֵל וַיִּשְׁתַּחֲווּ
# "[EN-AID] And Leah too came near, and her children, and they bowed; and
# after came Joseph near, and Rachel, and they bowed."
m.step("Gen.33.7")
# ‹וַתִּגַּשׁ גַּם־לֵאָה וִילָדֶיהָ וַיִּשְׁתַּחֲווּ› (“and-be also Leah
# and-child-her/its and-afflict”) — fact holds: and-afflict-kulam(Leah-
# Joseph-and-Rachel)
m.fact("va_yishtachavu_kulam(lea_yosef_ve_rachel)")

# -------------------------- Gen.33.8 · THE_CAMP_EXPLAINED ------------------
# וַיֹּאמֶר מִי לְךָ כָּל־הַמַּחֲנֶה הַזֶּה אֲשֶׁר פָּגָשְׁתִּי וַיֹּאמֶר
# לִמְצֹא־חֵן בְּעֵינֵי אֲדֹנִי
# "[EN-AID] And he said: What to you is all this camp which I met? And he
# said: To find grace in the eyes of my lord."
m.step("Gen.33.8")
# ‹מִי לְךָ כָּל־הַמַּחֲנֶה הַזֶּה אֲשֶׁר› (“who? to-you/your all the-camp
# the-this which”) — fact holds: who?-to-you-all-the-camp(come-in-contact-
# with)
m.fact("mi_lekha_kal_ha_machane(pagashti)")

# -------------------------- Gen.33.9 · THE_KEEP_IT_JUSSIVE -----------------
# וַיֹּאמֶר עֵשָׂו יֶשׁ־לִי רָב אָחִי יְהִי לְךָ אֲשֶׁר־לָךְ
# "[EN-AID] And Esau said: I have much, my brother; let what is yours be
# yours."
m.step("Gen.33.9")
# ‹יֶשׁ־לִי רָב אָחִי› (“there-is to-me/my many/great brother-me/my”) — Esau
# speaks a demand — LET: be(to-you-which-to-you)
m.declare("esav", "LET",
          "yehi(lekha_asher_lakh)")

# -------------------------- Gen.33.10 · THE_FACE_CODA_AND_THE_ACCEPT_VERB --
# וַיֹּאמֶר יַעֲקֹב אַל־נָא אִם־נָא מָצָאתִי חֵן בְּעֵינֶיךָ וְלָקַחְתָּ
# מִנְחָתִי מִיָּדִי כִּי עַל־כֵּן רָאִיתִי פָנֶיךָ כִּרְאֹת פְּנֵי אֱלֹהִים
# וַתִּרְצֵנִי
# "[EN-AID] And Jacob said: No, please — if now I have found grace in your
# eyes, then take my offering from my hand; for therefore have I seen your
# face, as one sees the face of God, and you have accepted me."
m.step("Gen.33.10")
# ‹כִּי עַל־כֵּן רָאִיתִי פָנֶיךָ כִּרְאֹת פְּנֵי אֱלֹהִים וַתִּרְצֵנִי›
# (“very-widely-used-as-a-relati above set-upright see face-you/your like-
# see face God and-be-pleased-with-me/my”) — fact holds: very-widely-used-
# as-a-relati-see-face-God-and-tirtzeni(peniel-coda)
m.fact("ki_reot_pene_Elohim_va_tirtzeni(peniel_coda)")
# witness-tier presupposed read: comparison_removed_by_both_members on
# as_the_face_of_God — read, not installed
m.witness_read("as_the_face_of_God", "comparison_removed_by_both_members",
                cites=["Onkelos Genesis 33:10"])

# -------------------------- Gen.33.11 · THE_POP_THE_BLESSING_RETURNED ------
# קַח־נָא אֶת־בִּרְכָתִי אֲשֶׁר הֻבָאת לָךְ כִּי־חַנַּנִי אֱלֹהִים וְכִי
# יֶשׁ־לִי־כֹל וַיִּפְצַר־בּוֹ וַיִּקָּח
# "[EN-AID] Take, please, my blessing that was brought to you, for God has
# graced me, and because I have all. And he urged him, and he took."
m.step("Gen.33.11")
# ‹קַח־נָא אֶת־בִּרְכָתִי› (“take please obj-marker blessing-me/my”) — Jacob
# speaks a demand — LET: take-please-obj-marker-birkhati(Esau)
m.declare("yaaqov", "LET",
          "qach_na_et_birkhati(esav)")
# ‹וַיִּפְצַר־בּוֹ וַיִּקָּח› (“and-peck-at in-him/its and-take”) — demand
# settled (popped from the queue): take-please-obj-marker-birkhati(Esau)
m.result("qach_na_et_birkhati(esav)", tmark="t2")
# witness-tier presupposed read: booked_as_a_reversible_transfer on the_gift
# — read, not installed
m.witness_read("the_gift", "booked_as_a_reversible_transfer",
                cites=["Bereshit Rabbah 78:12"])

# -------------------------- Gen.33.12 · THE_DECLINED_CONVOY ----------------
# וַיֹּאמֶר נִסְעָה וְנֵלֵכָה וְאֵלְכָה לְנֶגְדֶּךָ
# "[EN-AID] And he said: Let us journey and go, and I will go opposite you."
m.step("Gen.33.12")
# ‹נִסְעָה וְנֵלֵכָה וְאֵלְכָה לְנֶגְדֶּךָ› (“journey and-go and-go to-
# front-you/your”) — Esau speaks a demand — CMD-US?: journey-and-go(Esau-
# and-Jacob)
m.declare("esav", "CMD-US?",
          "nisa_ve_nelekha(esav_ve_yaaqov)")

# -------------------------- Gen.33.13 · THE_TENDER_PACE --------------------
# וַיֹּאמֶר אֵלָיו אֲדֹנִי יֹדֵעַ כִּי־הַיְלָדִים רַכִּים וְהַצֹּאן
# וְהַבָּקָר עָלוֹת עָלָי וּדְפָקוּם יוֹם אֶחָד וָמֵתוּ כָּל־הַצֹּאן
# "[EN-AID] And he said to him: My lord knows that the children are tender,
# and the flock and herd giving suck are upon me; and were they overdriven
# one day, all the flock would die."
m.step("Gen.33.13")
# ‹אֲדֹנִי יֹדֵעַ כִּי־הַיְלָדִים רַכִּים› (“lord-me/my know that the-child
# tender”) — fact holds: the-child-tender-and-suckle-alay(taanat-Jacob)
m.fact("ha_yeladim_rakim_ve_alot_alay(taanat_yaaqov)")

# -------------------------- Gen.33.14 · THE_PASS_BEFORE_JUSSIVE ------------
# יַעֲבָר־נָא אֲדֹנִי לִפְנֵי עַבְדּוֹ וַאֲנִי אֶתְנָהֲלָה לְאִטִּי לְרֶגֶל
# הַמְּלָאכָה אֲשֶׁר־לְפָנַי וּלְרֶגֶל הַיְלָדִים עַד אֲשֶׁר־אָבֹא
# אֶל־אֲדֹנִי שֵׂעִירָה
# "[EN-AID] Let my lord pass, please, before his servant, and I will lead on
# gently at my slow pace, at the foot of the work before me and at the foot
# of the children, until I come to my lord, to Seir."
m.step("Gen.33.14")
# ‹יַעֲבָר־נָא אֲדֹנִי לִפְנֵי עַבְדּוֹ› (“pass-over please lord-me/my to-
# face servant-him/its”) — Jacob speaks a demand — LET: pass-over-
# please(adoni, to-me-fene-avdo)
m.declare("yaaqov", "LET",
          "yaavar_na(adoni, li_fene_avdo)")
# witness-tier presupposed read:
# audited_unkept_and_reclassified_as_outstanding on i_will_come_to_seir —
# read, not installed
m.witness_read("i_will_come_to_seir", "audited_unkept_and_reclassified_as_outstanding",
                cites=["Bereshit Rabbah 78:14"])

# -------------------------- Gen.33.15 · THE_DECLINED_GARRISON --------------
# וַיֹּאמֶר עֵשָׂו אַצִּיגָה־נָּא עִמְּךָ מִן־הָעָם אֲשֶׁר אִתִּי וַיֹּאמֶר
# לָמָּה זֶּה אֶמְצָא־חֵן בְּעֵינֵי אֲדֹנִי
# "[EN-AID] And Esau said: Let me station with you, please, some of the
# people who are with me. And he said: Why so? Let me find grace in the eyes
# of my lord."
m.step("Gen.33.15")
# ‹אַצִּיגָה־נָּא עִמְּךָ מִן־הָעָם› (“place-permanently please with-
# you/your from the-people”) — fact holds: place-permanently-please-
# declined(to-what-this)
m.fact("atziga_na_declined(la_ma_ze)")

# -------------------------- Gen.33.16 · THE_FIRST_VECTOR -------------------
# וַיָּשָׁב בַּיּוֹם הַהוּא עֵשָׂו לְדַרְכּוֹ שֵׂעִירָה
# "[EN-AID] And Esau returned that day on his way to Seir."
m.step("Gen.33.16")
# ‹וַיָּשָׁב בַּיּוֹם הַהוּא עֵשָׂו לְדַרְכּוֹ שֵׂעִירָה› (“and-return in-
# day that Esau to-way/road-him/its Seir-ward”) — fact holds: and-return-
# Esau-seira(to-its-way)
m.fact("va_yashav_esav_seira(le_darko)")
# witness-tier presupposed read:
# run_as_procedure_with_its_one_logged_failure on the_portion — read, not
# installed
m.witness_read("the_portion", "run_as_procedure_with_its_one_logged_failure",
                cites=["Bereshit Rabbah 78:15"])

# -------------------------- Gen.33.17 · THE_SECOND_VECTOR_AND_THE_BOOTHS ---
# וְיַעֲקֹב נָסַע סֻכֹּתָה וַיִּבֶן לוֹ בָּיִת וּלְמִקְנֵהוּ עָשָׂה סֻכֹּת
# עַל־כֵּן קָרָא שֵׁם־הַמָּקוֹם סֻכּוֹת
# "[EN-AID] And Jacob journeyed to Sukkot, and built himself a house, and
# for his cattle he made booths; therefore he called the name of the place
# Sukkot."
m.step("Gen.33.17")
# ‹וְיַעֲקֹב נָסַע סֻכֹּתָה› (“and-Jacob journey Succoth-ward”) — fact
# holds: and-Jacob-journey-sukota(house-and-hut, report-only)
m.fact("ve_yaaqov_nasa_sukota(bayit_u_sukot, report_only)")

# -------------------------- Gen.33.18 · THE_WHOLE_ARRIVAL ------------------
# וַיָּבֹא יַעֲקֹב שָׁלֵם עִיר שְׁכֶם אֲשֶׁר בְּאֶרֶץ כְּנַעַן בְּבֹאוֹ
# מִפַּדַּן אֲרָם וַיִּחַן אֶת־פְּנֵי הָעִיר
# "[EN-AID] And Jacob came whole to the city of Shechem, which is in the
# land of Canaan, in his coming from Paddan-Aram; and he encamped before the
# city."
m.step("Gen.33.18")
# ‹וַיָּבֹא יַעֲקֹב שָׁלֵם עִיר שְׁכֶם› (“and-come/bring Jacob complete city
# Shechem”) — fact holds: and-come/bring-complete-who?-from-Padan(and-
# encamp)
m.fact("va_yavo_shalem_mi_padan_aram(va_yichan)")
# witness-tier presupposed read:
# gratitude_to_the_place_and_a_fence_enforced_twice on he_camped — read, not
# installed
m.witness_read("he_camped", "gratitude_to_the_place_and_a_fence_enforced_twice",
                cites=["Bereshit Rabbah 79:6"])

# -------------------------- Gen.33.19 · THE_SECOND_PURCHASE ----------------
# וַיִּקֶן אֶת־חֶלְקַת הַשָּׂדֶה אֲשֶׁר נָטָה־שָׁם אָהֳלוֹ מִיַּד
# בְּנֵי־חֲמוֹר אֲבִי שְׁכֶם בְּמֵאָה קְשִׂיטָה
# "[EN-AID] And he bought the portion of the field where he had pitched his
# tent from the hand of the sons of Hamor, father of Shechem, for a hundred
# qesita."
m.step("Gen.33.19")
# ‹וַיִּקֶן אֶת־חֶלְקַת הַשָּׂדֶה› (“and-erect obj-marker smoothness the-
# field”) — fact holds: and-erect-smoothness-the-field(in-hundred-ingot)
m.fact("va_yiqen_chelqat_ha_sade(be_mea_qesita)")
# witness-tier presupposed read:
# third_uncontestable_purchase_completing_the_set on the_hundred_units —
# read, not installed
m.witness_read("the_hundred_units", "third_uncontestable_purchase_completing_the_set",
                cites=["Bereshit Rabbah 79:7", "Onkelos Genesis 33:19"])

# -------------------------- Gen.33.20 · THE_ALTAR_AND_THE_OBLIQUE_WRITE ----
# וַיַּצֶּב־שָׁם מִזְבֵּחַ וַיִּקְרָא־לוֹ אֵל אֱלֹהֵי יִשְׂרָאֵל
# "[EN-AID] And he set up there an altar, and called it El-Elohe-Israel
# [God, the God of Israel]."
m.step("Gen.33.20")
# ‹וַיַּצֶּב־שָׁם מִזְבֵּחַ› (“and-stand there altar”) — the world gains:
# the-altar
m.install("ha_mizbeach")
# ‹וַיִּקְרָא־לוֹ אֵל אֱלֹהֵי יִשְׂרָאֵל› (“and-call to-him/its strength God
# Israel”) — named: the-altar := do-not-God-Israel
m.name("ha_mizbeach", "el_elohe_yisrael")
# witness-tier presupposed read: offence_priced_here_and_deleted_there on
# the_altars_name — read, not installed
m.witness_read("the_altars_name", "offence_priced_here_and_deleted_there",
                cites=["Bereshit Rabbah 79:8", "Onkelos Genesis 33:20"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ha_mizbeach'}
    assert m.presupposed_set() == set()
    assert m.REGISTRY["names"] == {'ha_mizbeach': 'el_elohe_yisrael'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['yehi(lekha_asher_lakh)', 'nisa_ve_nelekha(esav_ve_yaaqov)', 'yaavar_na(adoni, li_fene_avdo)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {}
    assert sorted(m.WORLD["facts"]) == sorted(['va_yar_esav_ba_va_yachatz(arba_meot_ish)', 'rishona_acharonim_acharonim(seder_ha_machane)', 'va_yishtachu_sheva_peamim(hipukh_ha_berakha)', 'va_yechabqehu_va_yivku(esav_ve_yaaqov)', 'ha_yeladim_asher_chanan_Elohim(maane_yaaqov)', 'va_tigashna_va_tishtachavena(ha_shefachot)', 'va_yishtachavu_kulam(lea_yosef_ve_rachel)', 'mi_lekha_kal_ha_machane(pagashti)', 'ki_reot_pene_Elohim_va_tirtzeni(peniel_coda)', 'ha_yeladim_rakim_ve_alot_alay(taanat_yaaqov)', 'atziga_na_declined(la_ma_ze)', 'va_yashav_esav_seira(le_darko)', 've_yaaqov_nasa_sukota(bayit_u_sukot, report_only)', 'va_yavo_shalem_mi_padan_aram(va_yichan)', 'va_yiqen_chelqat_ha_sade(be_mea_qesita)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 6
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('dividing_the_children', 'collective_merit_disaggregated_under_test'), ('the_dotted_kiss', 'the_rules_own_tie_case_confirmed_in_our_ink'), ('the_children_God_graced', 'one_grace_outstanding_until_43_29'), ('as_the_face_of_God', 'comparison_removed_by_both_members'), ('the_gift', 'booked_as_a_reversible_transfer'), ('i_will_come_to_seir', 'audited_unkept_and_reclassified_as_outstanding'), ('the_portion', 'run_as_procedure_with_its_one_logged_failure'), ('he_camped', 'gratitude_to_the_place_and_a_fence_enforced_twice'), ('the_hundred_units', 'third_uncontestable_purchase_completing_the_set'), ('the_altars_name', 'offence_priced_here_and_deleted_there')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 78:7']
    assert all('collective_merit_disaggregated_under_test' not in f for f in m.WORLD["facts"])
    assert 'dividing_the_children' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 78:9']
    assert all('the_rules_own_tie_case_confirmed_in_our_ink' not in f for f in m.WORLD["facts"])
    assert 'the_dotted_kiss' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 78:10']
    assert all('one_grace_outstanding_until_43_29' not in f for f in m.WORLD["facts"])
    assert 'the_children_God_graced' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Onkelos Genesis 33:10']
    assert all('comparison_removed_by_both_members' not in f for f in m.WORLD["facts"])
    assert 'as_the_face_of_God' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Bereshit Rabbah 78:12']
    assert all('booked_as_a_reversible_transfer' not in f for f in m.WORLD["facts"])
    assert 'the_gift' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 78:14']
    assert all('audited_unkept_and_reclassified_as_outstanding' not in f for f in m.WORLD["facts"])
    assert 'i_will_come_to_seir' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 78:15']
    assert all('run_as_procedure_with_its_one_logged_failure' not in f for f in m.WORLD["facts"])
    assert 'the_portion' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[7]["cites"] == ['Bereshit Rabbah 79:6']
    assert all('gratitude_to_the_place_and_a_fence_enforced_twice' not in f for f in m.WORLD["facts"])
    assert 'he_camped' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[8]["cites"] == ['Bereshit Rabbah 79:7', 'Onkelos Genesis 33:19']
    assert all('third_uncontestable_purchase_completing_the_set' not in f for f in m.WORLD["facts"])
    assert 'the_hundred_units' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[9]["cites"] == ['Bereshit Rabbah 79:8', 'Onkelos Genesis 33:20']
    assert all('offence_priced_here_and_deleted_there' not in f for f in m.WORLD["facts"])
    assert 'the_altars_name' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
