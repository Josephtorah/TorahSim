#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_36_gerar_dream_prophet — 20:1-18
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_36_gerar_dream_prophet.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Gerar: the dream-court, the prophet's prayer, the shut wombs (20:1-18)"""
from machine import Machine

m = Machine("gen_36_gerar_dream_prophet")

# -------------------------- Gen.20.1 · THE_JOURNEY_TO_GERAR ----------------
# וַיִּסַּע מִשָּׁם אַבְרָהָם אַרְצָה הַנֶּגֶב וַיֵּשֶׁב בֵּין־קָדֵשׁ וּבֵין
# שׁוּר וַיָּגָר בִּגְרָר
# "And Abraham journeyed from thence toward the land of the South, and dwelt
# between Kadesh and Shur; and he sojourned in Gerar."
m.step("Gen.20.1")
# ‹וַיִּסַּע מִשָּׁם אַבְרָהָם … וַיָּגָר בִּגְרָר› (“and-journey from-there
# Abraham … and-turn-aside-from-the-road in-Gerar”) — event: journey-sojourn
# — agent Abraham
m.event("journey_sojourn", agent="avraham")
# ‹בֵּין־קָדֵשׁ וּבֵין שׁוּר … בִּגְרָר› (“between Kadesh and-between Shur …
# in-Gerar”) — reads without prior install (flag, not fix): Gerar, Kadesh,
# Shur
m.presupposed("gerar", "qadesh", "shur")

# -------------------------- Gen.20.2 · THE_SECOND_CLAIM_AND_THE_TAKING -----
# וַיֹּאמֶר אַבְרָהָם אֶל־שָׂרָה אִשְׁתּוֹ אֲחֹתִי הִוא וַיִּשְׁלַח
# אֲבִימֶלֶךְ מֶלֶךְ גְּרָר וַיִּקַּח אֶת־שָׂרָה
# "And Abraham said of Sarah his wife: 'She is my sister.' And Abimelech
# king of Gerar sent, and took Sarah."
m.step("Gen.20.2")
# ‹אֲחֹתִי הִוא› (“sister-me/my he/it”) — fact holds: achoti-he/it
m.fact("achoti_hi")
# ‹אֲבִימֶלֶךְ מֶלֶךְ גְּרָר› (“Abimelech king Gerar”) — the world gains:
# Abimelech
m.install("avimelekh")
# ‹וַיִּשְׁלַח … וַיִּקַּח אֶת־שָׂרָה› (“and-send … and-take obj-marker
# Sarah”) — event: take — agent Abimelech; theme sarah
m.event("take", agent="avimelekh", themes=["sarah"])

# -------------------------- Gen.20.3 · THE_DREAM_VERDICT -------------------
# וַיָּבֹא אֱלֹהִים אֶל־אֲבִימֶלֶךְ בַּחֲלוֹם הַלָּיְלָה וַיֹּאמֶר לוֹ
# הִנְּךָ מֵת עַל־הָאִשָּׁה אֲשֶׁר־לָקַחְתָּ וְהִוא בְּעֻלַת בָּעַל
# "But God came to Abimelech in a dream of the night, and said to him:
# 'Behold, thou shalt die, because of the woman whom thou hast taken; for
# she is a man's wife.'"
m.step("Gen.20.3")
# ‹וַיָּבֹא אֱלֹהִים אֶל־אֲבִימֶלֶךְ בַּחֲלוֹם הַלָּיְלָה› (“and-come/bring
# God to Abimelech in-dream the-night”) — event: dream-say — agent God
m.event("dream_say", agent="elohim")
# ‹הִנְּךָ מֵת עַל־הָאִשָּׁה אֲשֶׁר־לָקַחְתָּ וְהִוא בְּעֻלַת בָּעַל›
# (“behold-you/your die over the-woman which take and-he/it be-master
# master”) — fact holds: hinkha-die-over-the-woman; and-he/it-be-master-
# master
m.fact("hinkha_met_al_ha_ishah",
       "ve_hi_beulat_baal")

# -------------------------- Gen.20.4 · THE_KINGS_COUNT_QUESTION ------------
# וַאֲבִימֶלֶךְ לֹא קָרַב אֵלֶיהָ וַיֹּאמַר אֲדֹנָי הֲגוֹי גַּם־צַדִּיק
# תַּהֲרֹג
# "Now Abimelech had not come near her; and he said: 'Lord, wilt Thou slay
# even a righteous nation?"
m.step("Gen.20.4")
# ‹לֹא קָרַב אֵלֶיהָ … הֲגוֹי גַּם־צַדִּיק תַּהֲרֹג› (“not bring-near to-
# her/its … the-nation also just smite-with-deadly-intent”) — fact holds:
# not-bring-near-eleha; the-nation-also-tzaddiq-smite-with-deadly-intent
m.fact("lo_qarav_eleha",
       "ha_goy_gam_tzaddiq_taharog")

# -------------------------- Gen.20.5 · THE_INTEGRITY_DEFENSE ---------------
# הֲלֹא הוּא אָמַר־לִי אֲחֹתִי הִוא וְהִיא־גַם־הִוא אָמְרָה אָחִי הוּא
# בְּתָם־לְבָבִי וּבְנִקְיֹן כַּפַּי עָשִׂיתִי זֹאת
# "Said he not himself unto me: She is my sister? and she, even she herself
# said: He is my brother. In the simplicity of my heart and the innocency of
# my hands have I done this.'"
m.step("Gen.20.5")
# ‹הֲלֹא הוּא אָמַר־לִי … בְּתָם־לְבָבִי וּבְנִקְיֹן כַּפַּי› (“is-it-not
# he/it say to-me/my … in-completeness heart-me/my and-in-clearness palm-of-
# hand-me/my”) — fact holds: he/it-say-to-me-and-he/it-also-he/it-amrah; in-
# tom-levavi-and-and-clearness-kapai
m.fact("hu_amar_li_ve_hi_gam_hi_amrah",
       "be_tom_levavi_u_ve_niqyon_kapai")

# -------------------------- Gen.20.6 · THE_CONCESSION_AND_THE_WITHHOLDING --
# וַיֹּאמֶר אֵלָיו הָאֱלֹהִים בַּחֲלֹם גַּם אָנֹכִי יָדַעְתִּי כִּי
# בְתָם־לְבָבְךָ עָשִׂיתָ זֹּאת וָאֶחְשֹׂךְ גַּם־אָנֹכִי אוֹתְךָ מֵחֲטוֹ־לִי
# עַל־כֵּן לֹא־נְתַתִּיךָ לִנְגֹּעַ אֵלֶיהָ
# "And God said unto him in the dream: 'Yea, I know that in the simplicity
# of thy heart thou hast done this, and I also withheld thee from sinning
# against Me. Therefore suffered I thee not to touch her."
m.step("Gen.20.6")
# ‹יָדַעְתִּי … וָאֶחְשֹׂךְ … מֵחֲטוֹ־לִי … לֹא־נְתַתִּיךָ לִנְגֹּעַ› (“know
# … and-restrain … from-sin to-me/my … not set-you/your to-touch”) — fact
# holds: also-anokhi-know-and-tom-levavkha; and-restrain-otkha-what-sin-to-
# me; not-netatikha-lingoa
m.fact("gam_anokhi_yadati_ve_tom_levavkha",
       "va_echsokh_otkha_me_chato_li",
       "lo_netatikha_lingoa")

# -------------------------- Gen.20.7 · THE_PROPHET_AND_THE_RETURN_COMMAND --
# וְעַתָּה הָשֵׁב אֵשֶׁת־הָאִישׁ כִּי־נָבִיא הוּא וְיִתְפַּלֵּל בַּעַדְךָ
# וֶחְיֵה וְאִם־אֵינְךָ מֵשִׁיב דַּע כִּי־מוֹת תָּמוּת אַתָּה
# וְכָל־אֲשֶׁר־לָךְ
# "Now therefore restore the man's wife; for he is a prophet, and he shall
# pray for thee, and thou shalt live; and if thou restore her not, know thou
# that thou shalt surely die, thou, and all that are thine.'"
m.step("Gen.20.7")
# ‹וְעַתָּה הָשֵׁב אֵשֶׁת־הָאִישׁ› (“and-now return woman the-man”) — God
# speaks a demand — LET: return(woman-the-man)
m.declare("elohim", "LET",
          "hashev(eshet_ha_ish)")
# ‹וְיִתְפַּלֵּל בַּעַדְךָ וֶחְיֵה› (“and-judge in-up-to-you/your and-live”)
# — fact holds: and-judge-baadkha-and-cheyeh
m.fact("ve_yitpalel_baadkha_ve_cheyeh")
# ‹וְאִם־אֵינְךָ מֵשִׁיב דַּע כִּי־מוֹת תָּמוּת› (“and-if there-is-not-
# you/your return know that die die”) — fact holds: if-einkha-return-know-
# that-die-die
m.fact("im_einkha_meshiv_da_ki_mot_tamut")

# -------------------------- Gen.20.8 · THE_COURT_FEARS ---------------------
# וַיַּשְׁכֵּם אֲבִימֶלֶךְ בַּבֹּקֶר וַיִּקְרָא לְכָל־עֲבָדָיו וַיְדַבֵּר
# אֶת־כָּל־הַדְּבָרִים הָאֵלֶּה בְּאָזְנֵיהֶם וַיִּירְאוּ הָאֲנָשִׁים מְאֹד
# "And Abimelech rose early in the morning, and called all his servants, and
# told all these things in their ears; and the men were sore afraid."
m.step("Gen.20.8")
# ‹וַיַּשְׁכֵּם … וַיְדַבֵּר … וַיִּירְאוּ הָאֲנָשִׁים מְאֹד› (“and-rise-
# early … and-speak … and-fear the-man very”) — event: report-fear — agent
# Abimelech
m.event("report_fear", agent="avimelekh")

# -------------------------- Gen.20.9 · THE_GREAT_SIN_REBUKE ----------------
# וַיִּקְרָא אֲבִימֶלֶךְ לְאַבְרָהָם וַיֹּאמֶר לוֹ מֶה־עָשִׂיתָ לָּנוּ
# וּמֶה־חָטָאתִי לָךְ כִּי־הֵבֵאתָ עָלַי וְעַל־מַמְלַכְתִּי חֲטָאָה גְדֹלָה
# מַעֲשִׂים אֲשֶׁר לֹא־יֵעָשׂוּ עָשִׂיתָ עִמָּדִי
# "Then Abimelech called Abraham, and said unto him: 'What hast thou done
# unto us? and wherein have I sinned against thee, that thou hast brought on
# me and on my kingdom a great sin? thou hast done deeds unto me that ought
# not to be done.'"
m.step("Gen.20.9")
# ‹מֶה־עָשִׂיתָ לָּנוּ … חֲטָאָה גְדֹלָה … מַעֲשִׂים אֲשֶׁר לֹא־יֵעָשׂוּ›
# (“what make to-us/our … offence great … deed/work which not make”) — fact
# holds: meh-make-lanu-and-meh-sin; chataah-gedolah-over-mamlakhti
m.fact("meh_asita_lanu_u_meh_chatati",
       "chataah_gedolah_al_mamlakhti")

# -------------------------- Gen.20.10 · THE_SECOND_QUESTION ----------------
# וַיֹּאמֶר אֲבִימֶלֶךְ אֶל־אַבְרָהָם מָה רָאִיתָ כִּי עָשִׂיתָ אֶת־הַדָּבָר
# הַזֶּה
# "And Abimelech said unto Abraham: 'What sawest thou, that thou hast done
# this thing?'"
m.step("Gen.20.10")
# ‹מָה רָאִיתָ כִּי עָשִׂיתָ› (“what see that make”) — fact holds: mah-see-
# that-make
m.fact("mah_raita_ki_asita")

# -------------------------- Gen.20.11 · THE_FEAR_OF_GOD_GUESS --------------
# וַיֹּאמֶר אַבְרָהָם כִּי אָמַרְתִּי רַק אֵין־יִרְאַת אֱלֹהִים בַּמָּקוֹם
# הַזֶּה וַהֲרָגוּנִי עַל־דְּבַר אִשְׁתִּי
# "And Abraham said: 'Because I thought: Surely the fear of God is not in
# this place; and they will slay me for my wife's sake."
m.step("Gen.20.11")
# ‹אֵין־יִרְאַת אֱלֹהִים בַּמָּקוֹם הַזֶּה וַהֲרָגוּנִי› (“there-is-not fear
# God in-place the-this and-smite-with-deadly-intent-me/my”) — fact holds:
# say-ein-fear-God; and-haraguni-over-word/thing-ishti
m.fact("amarti_ein_yirat_elohim",
       "va_haraguni_al_devar_ishti")

# -------------------------- Gen.20.12 · THE_HALF_TRUTH ---------------------
# וְגַם־אָמְנָה אֲחֹתִי בַת־אָבִי הִוא אַךְ לֹא בַת־אִמִּי וַתְּהִי־לִי
# לְאִשָּׁה
# "And moreover she is indeed my sister, the daughter of my father, but not
# the daughter of my mother; and so she became my wife."
m.step("Gen.20.12")
# ‹אֲחֹתִי בַת־אָבִי הִוא אַךְ לֹא בַת־אִמִּי› (“sister-me/my daughter
# father-me/my he/it indeed not daughter mother-me/my”) — fact holds:
# achoti-daughter-avi-indeed-not-daughter-imi
m.fact("achoti_vat_avi_akh_lo_vat_imi")

# -------------------------- Gen.20.13 · THE_WANDERING_AND_THE_QUOTED_DEMAND -
# וַיְהִי כַּאֲשֶׁר הִתְעוּ אֹתִי אֱלֹהִים מִבֵּית אָבִי וָאֹמַר לָהּ זֶה
# חַסְדֵּךְ אֲשֶׁר תַּעֲשִׂי עִמָּדִי אֶל כָּל־הַמָּקוֹם אֲשֶׁר נָבוֹא
# שָׁמָּה אִמְרִי־לִי אָחִי הוּא
# "And it came to pass, when God caused me to wander from my father's house,
# that I said unto her: This is thy kindness which thou shalt show unto me;
# at every place whither we shall come, say of me: He is my brother.'"
m.step("Gen.20.13")
# ‹הִתְעוּ אֹתִי אֱלֹהִים … אִמְרִי־לִי אָחִי הוּא› (“vacillate obj-marker-
# me/my God … say to-me/my brother-me/my he/it”) — fact holds: vacillate-me-
# God-from-beit-avi; say-to-me-my-brother-he/it
m.fact("hitu_oti_elohim_mi_beit_avi",
       "imri_li_achi_hu")

# -------------------------- Gen.20.14 · THE_RETURN_CYCLE_CLOSES ------------
# וַיִּקַּח אֲבִימֶלֶךְ צֹאן וּבָקָר וַעֲבָדִים וּשְׁפָחֹת וַיִּתֵּן
# לְאַבְרָהָם וַיָּשֶׁב לוֹ אֵת שָׂרָה אִשְׁתּוֹ
# "And Abimelech took sheep and oxen, and men-servants and women-servants,
# and gave them unto Abraham, and restored him Sarah his wife."
m.step("Gen.20.14")
# ‹וַיָּשֶׁב לוֹ אֵת שָׂרָה אִשְׁתּוֹ› (“and-return to-him/its obj-marker
# Sarah woman-him/its”) — demand settled (popped from the queue):
# return(woman-the-man)
m.result("hashev(eshet_ha_ish)", tmark="t1")

# -------------------------- Gen.20.15 · THE_DWELL_GRANT --------------------
# וַיֹּאמֶר אֲבִימֶלֶךְ הִנֵּה אַרְצִי לְפָנֶיךָ בַּטּוֹב בְּעֵינֶיךָ שֵׁב
# "And Abimelech said: 'Behold, my land is before thee: dwell where it
# pleaseth thee.'"
m.step("Gen.20.15")
# ‹בַּטּוֹב בְּעֵינֶיךָ שֵׁב› (“in-good in-eye-you/your dwell/sit”) —
# Abimelech speaks a demand — LET: dwell/sit(in-the-good-in-einekha)
m.declare("avimelekh", "LET",
          "shev(ba_tov_be_einekha)")

# -------------------------- Gen.20.16 · THE_COVERING_AND_THE_VINDICATION ---
# וּלְשָׂרָה אָמַר הִנֵּה נָתַתִּי אֶלֶף כֶּסֶף לְאָחִיךְ הִנֵּה הוּא־לָךְ
# כְּסוּת עֵינַיִם לְכֹל אֲשֶׁר אִתָּךְ וְאֵת כֹּל וְנֹכָחַת
# "And unto Sarah he said: 'Behold, I have given thy brother a thousand
# pieces of silver; behold, it is for thee a covering of the eyes to all
# that are with thee; and before all men thou art righted.'"
m.step("Gen.20.16")
# ‹אֶלֶף כֶּסֶף … כְּסוּת עֵינַיִם … וְנֹכָחַת› (“thousand silver … cover
# eye … and-be-right”) — fact holds: thousand-silver-cover-einayim; and-be-
# right
m.fact("elef_kesef_kesut_einayim",
       "ve_nokhachat")

# -------------------------- Gen.20.17 · THE_PRAYER_AND_THE_HEALING ---------
# וַיִּתְפַּלֵּל אַבְרָהָם אֶל־הָאֱלֹהִים וַיִּרְפָּא אֱלֹהִים
# אֶת־אֲבִימֶלֶךְ וְאֶת־אִשְׁתּוֹ וְאַמְהֹתָיו וַיֵּלֵדוּ
# "And Abraham prayed unto God; and God healed Abimelech, and his wife, and
# his maid-servants; and they bore children."
m.step("Gen.20.17")
# ‹וַיִּתְפַּלֵּל אַבְרָהָם אֶל־הָאֱלֹהִים› (“and-judge Abraham to the-God”)
# — event: pray — agent Abraham
m.event("pray", agent="avraham")
# ‹וַיִּרְפָּא אֱלֹהִים … וַיֵּלֵדוּ› (“and-mend God … and-bear-young”) —
# event: heal — agent God; theme beit-Abimelech
m.event("heal", agent="elohim", themes=["beit_avimelekh"])

# -------------------------- Gen.20.18 · THE_SHUT_WOMB_CLOSER ---------------
# כִּי־עָצֹר עָצַר יְהוָה בְּעַד כָּל־רֶחֶם לְבֵית אֲבִימֶלֶךְ עַל־דְּבַר
# שָׂרָה אֵשֶׁת אַבְרָהָם
# "For the LORD had fast closed up all the wombs of the house of Abimelech,
# because of Sarah Abraham's wife."
m.step("Gen.20.18")
# ‹כִּי־עָצֹר עָצַר יְהוָה בְּעַד כָּל־רֶחֶם› (“that close close YHWH in-up-
# to all womb”) — fact holds: close-close-the-LORD-up-to-all-womb
m.fact("atzor_atzar_YHWH_bead_kol_rechem")
# ‹כִּי־עָצֹר עָצַר יְהוָה› (“that close close YHWH”) — note: zero events in
# this verse
m.note_zero_events()

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'avimelekh'}
    assert m.presupposed_set() == {'shur', 'gerar', 'qadesh'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['shev(ba_tov_be_einekha)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['achoti_hi', 'hinkha_met_al_ha_ishah', 've_hi_beulat_baal', 'lo_qarav_eleha', 'ha_goy_gam_tzaddiq_taharog', 'hu_amar_li_ve_hi_gam_hi_amrah', 'be_tom_levavi_u_ve_niqyon_kapai', 'gam_anokhi_yadati_ve_tom_levavkha', 'va_echsokh_otkha_me_chato_li', 'lo_netatikha_lingoa', 've_yitpalel_baadkha_ve_cheyeh', 'im_einkha_meshiv_da_ki_mot_tamut', 'meh_asita_lanu_u_meh_chatati', 'chataah_gedolah_al_mamlakhti', 'mah_raita_ki_asita', 'amarti_ein_yirat_elohim', 'va_haraguni_al_devar_ishti', 'achoti_vat_avi_akh_lo_vat_imi', 'hitu_oti_elohim_mi_beit_avi', 'imri_li_achi_hu', 'elef_kesef_kesut_einayim', 've_nokhachat', 'atzor_atzar_YHWH_bead_kol_rechem'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 9
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
