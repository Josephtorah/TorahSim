#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_23_vineyard_curse — 9:18-29
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_23_vineyard_curse.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The vineyard and the curse: cursed be Canaan, blessed be the LORD (9:18-29)"""
from machine import Machine

m = Machine("gen_23_vineyard_curse")

# -------------------------- Gen.9.18 · THE_ROSTER_OUT_OF_THE_ARK -----------
# וַיִּהְיוּ בְנֵי־נֹחַ הַיֹּצְאִים מִן־הַתֵּבָה שֵׁם וְחָם וָיָפֶת וְחָם
# הוּא אֲבִי כְנָעַן
# "And the sons of Noah, that went forth from the ark, were Shem, and Ham,
# and Japheth; and Ham is the father of Canaan."
m.step("Gen.9.18")
# ‹וַיִּהְיוּ בְנֵי־נֹחַ הַיֹּצְאִים מִן־הַתֵּבָה … וְחָם הוּא אֲבִי
# כְנָעַן› (“and-they-were sons-of Noah going-out-of from the-ark … and-Ham
# he father-of Canaan”) — fact holds: sons-of-Noach-the-going-out-of-from-
# the-ark-Shem-Ham-and-Yefet; Ham-he-father-of-Canaan
m.fact("bnei_noach_ha_yotzim_min_ha_tevah_shem_cham_va_yefet",
       "cham_hu_avi_khenaan")
# reads without prior install (flag, not fix): Noach, ark, Canaan
m.presupposed("noach", "tevah", "kenaan")

# -------------------------- Gen.9.19 · THREE_AND_THE_SCATTERED_EARTH -------
# שְׁלֹשָׁה אֵלֶּה בְּנֵי־נֹחַ וּמֵאֵלֶּה נָפְצָה כָל־הָאָרֶץ
# "These three were the sons of Noah, and of these was the whole earth
# overspread."
m.step("Gen.9.19")
# ‹שְׁלֹשָׁה אֵלֶּה … וּמֵאֵלֶּה נָפְצָה כָל־הָאָרֶץ› (“three these … and-
# from-these was-scattered all the-earth”) — fact holds: three-these-sons-
# of-Noach; and-from-these-naftzah-all-the-earth
m.fact("shelosha_eleh_bnei_noach",
       "u_me_eleh_naftzah_khol_ha_aretz")

# -------------------------- Gen.9.20 · THE_GROUND_MAN_PLANTS_A_VINEYARD ----
# וַיָּחֶל נֹחַ אִישׁ הָאֲדָמָה וַיִּטַּע כָּרֶם
# "And Noah the husbandman began, and planted a vineyard."
m.step("Gen.9.20")
# ‹וַיָּחֶל נֹחַ› (“and-he-began Noah”) — event: begin — agent Noach
m.event("begin", agent="noach")
# ‹אִישׁ הָאֲדָמָה› (“man-of the-ground”) — fact holds: Noach-man-of-the-
# ground
m.fact("noach_ish_ha_adamah")
# ‹וַיִּטַּע כָּרֶם› (“and-he-planted vineyard”) — event: plant — agent
# Noach; theme kerem
m.event("plant", agent="noach", themes=["kerem"])
# ‹כָּרֶם› (“vineyard”) — the world gains: kerem
m.install("kerem")

# -------------------------- Gen.9.21 · THE_WINE_AND_THE_SELF_UNCOVERING ----
# וַיֵּשְׁתְּ מִן־הַיַּיִן וַיִּשְׁכָּר וַיִּתְגַּל בְּתוֹךְ אָהֳלֹה
# "And he drank of the wine, and was drunken; and he was uncovered within
# his tent."
m.step("Gen.9.21")
# ‹וַיֵּשְׁתְּ מִן־הַיַּיִן› (“and-he-drank from the-wine”) — event: drink —
# agent Noach; theme from-the-wine
m.event("drink", agent="noach", themes=["min_ha_yayin"])
# ‹וַיִּשְׁכָּר› (“and-was-drunk”) — event: become-drunk — agent Noach
m.event("become_drunk", agent="noach")
# ‹וַיִּתְגַּל בְּתוֹךְ אָהֳלֹה› (“and-uncovered-himself inside his-tent”) —
# event: uncover-self — agent Noach; theme in-inside-aholoh
m.event("uncover_self", agent="noach", themes=["be_tokh_aholoh"])
# witness-tier presupposed read: feminine_suffix_and_disputed_woe_count on
# drunkenness_verse — read, not installed
m.witness_read("drunkenness_verse", "feminine_suffix_and_disputed_woe_count",
                cites=["Bereshit Rabbah 36:4", "Sanhedrin 70a:17"])

# -------------------------- Gen.9.22 · THE_SEEING_AND_THE_TELLING ----------
# וַיַּרְא חָם אֲבִי כְנַעַן אֵת עֶרְוַת אָבִיו וַיַּגֵּד לִשְׁנֵי־אֶחָיו
# בַּחוּץ
# "And Ham, the father of Canaan, saw the nakedness of his father, and told
# his two brethren without."
m.step("Gen.9.22")
# ‹וַיַּרְא חָם אֲבִי כְנַעַן אֵת עֶרְוַת אָבִיו› (“and-he-saw Ham father-of
# Canaan obj-marker nakedness-of his-father”) — event: see — agent Ham;
# theme nakedness-of-aviv
m.event("see", agent="cham", themes=["ervat_aviv"])
# ‹וַיַּגֵּד לִשְׁנֵי־אֶחָיו בַּחוּץ› (“and-he-told to-his-two his-brothers
# outside”) — event: tell — agent Ham; theme to-me-shnei-echav
m.event("tell", agent="cham", themes=["li_shnei_echav"])
# witness-grounded state (its own tier): castration_or_sodomy on the_offence
m.witness_state("the_offence", "castration_or_sodomy",
                cites=["Sanhedrin 70a:19", "Bereshit Rabbah 36:7"])

# -------------------------- Gen.9.23 · THE_BACKWARD_COVERING ---------------
# וַיִּקַּח שֵׁם וָיֶפֶת אֶת־הַשִּׂמְלָה וַיָּשִׂימוּ עַל־שְׁכֶם שְׁנֵיהֶם
# וַיֵּלְכוּ אֲחֹרַנִּית וַיְכַסּוּ אֵת עֶרְוַת אֲבִיהֶם וּפְנֵיהֶם
# אֲחֹרַנִּית וְעֶרְוַת אֲבִיהֶם לֹא רָאוּ
# "And Shem and Japheth took a garment, and laid it upon both their
# shoulders, and went backward, and covered the nakedness of their father;
# and their faces were backward, and they saw not their father's nakedness."
m.step("Gen.9.23")
# ‹וַיִּקַּח שֵׁם וָיֶפֶת אֶת־הַשִּׂמְלָה› (“and-he-took Shem and-Yefet obj-
# marker the-garment”) — event: take — agent Shem-and-Yefet; theme the-
# simlah
m.event("take", agent="shem_va_yefet", themes=["ha_simlah"])
# ‹וַיָּשִׂימוּ עַל־שְׁכֶם שְׁנֵיהֶם› (“and-they-set over shoulder-of both-
# of-them”) — event: set — agent Shem-and-Yefet; theme over-shoulder-of-
# both-of-them
m.event("set", agent="shem_va_yefet", themes=["al_shekhem_shneihem"])
# ‹וַיֵּלְכוּ אֲחֹרַנִּית› (“and-they-walked backward”) — event: walk-
# backward — agent Shem-and-Yefet
m.event("walk_backward", agent="shem_va_yefet")
# ‹וַיְכַסּוּ אֵת עֶרְוַת אֲבִיהֶם› (“and-they-covered obj-marker nakedness-
# of their-father”) — event: cover — agent Shem-and-Yefet; theme nakedness-
# of-avihem
m.event("cover", agent="shem_va_yefet", themes=["ervat_avihem"])
# ‹וּפְנֵיהֶם אֲחֹרַנִּית וְעֶרְוַת אֲבִיהֶם לֹא רָאוּ› (“and-their-faces
# backward and-nakedness-of their-father not they-saw”) — fact holds: and-
# nakedness-of-avihem-not-they-saw
m.fact("ve_ervat_avihem_lo_rau")
# witness-tier presupposed read: prayer_law_on_a_gentile_subject on
# nakedness_covered — read, not installed
m.witness_read("nakedness_covered", "prayer_law_on_a_gentile_subject",
                cites=["Berakhot 25b:11", "Bereshit Rabbah 36:5"])

# -------------------------- Gen.9.24 · THE_AWAKENING_AND_THE_KNOWING -------
# וַיִּיקֶץ נֹחַ מִיֵּינוֹ וַיֵּדַע אֵת אֲשֶׁר־עָשָׂה־לוֹ בְּנוֹ הַקָּטָן
# "And Noah awoke from his wine, and knew what his youngest son had done
# unto him."
m.step("Gen.9.24")
# ‹וַיִּיקֶץ נֹחַ מִיֵּינוֹ› (“and-he-awoke Noah from-his-wine”) — event:
# awake — agent Noach
m.event("awake", agent="noach")
# ‹וַיֵּדַע אֵת אֲשֶׁר־עָשָׂה־לוֹ בְּנוֹ הַקָּטָן› (“and-he-knew obj-marker
# that-which did to-him his-son the-small”) — event: know — agent Noach;
# theme that-which-make-not-beno-the-small
m.event("know", agent="noach", themes=["asher_asah_lo_beno_ha_qatan"])

# -------------------------- Gen.9.25 · THE_FIRST_HUMAN_CURSE ---------------
# וַיֹּאמֶר אָרוּר כְּנָעַן עֶבֶד עֲבָדִים יִהְיֶה לְאֶחָיו
# "And he said: 'Cursed be Canaan; a servant of servants shall he be unto
# his brethren.'"
m.step("Gen.9.25")
# ‹וַיֹּאמֶר אָרוּר כְּנָעַן› (“and-he-said cursed Canaan”) — event: speak —
# agent Noach; theme cursed-Canaan
m.event("speak", agent="noach", themes=["arur_kenaan"])
# ‹אָרוּר כְּנָעַן› (“cursed Canaan”) — role assigned: Canaan -> cursed
m.assign("kenaan", "arur")
# ‹עֶבֶד עֲבָדִים יִהְיֶה לְאֶחָיו› (“slave-of slaves shall-he-be to-his-
# brothers”) — fact holds: slave-of-slaves-yihyeh-to-echav(Canaan)
m.fact("eved_avadim_yihyeh_le_echav(kenaan)")
# witness-tier presupposed read: legal_category_name_yet_exitable on
# slave_curse — read, not installed
m.witness_read("slave_curse", "legal_category_name_yet_exitable",
                cites=["Jerusalem Talmud Kiddushin 1:3:1", "Bereshit Rabbah 61:7", "Bereshit Rabbah 60:7"])

# -------------------------- Gen.9.26 · THE_FIRST_HUMAN_BLESSING ------------
# וַיֹּאמֶר בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם וִיהִי כְנַעַן עֶבֶד לָמוֹ
# "And he said: 'Blessed be the LORD, the God of Shem; and let Canaan be
# their servant.'"
m.step("Gen.9.26")
# ‹וַיֹּאמֶר בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם› (“and-he-said blessed YHWH God-
# of Shem”) — event: speak — agent Noach; theme blessed-yhwh-elohei-Shem
m.event("speak", agent="noach", themes=["barukh_yhwh_elohei_shem"])
# ‹בָּרוּךְ יְהֹוָה אֱלֹהֵי שֵׁם› (“blessed YHWH God-of Shem”) — blessing:
# Noach blesses yhwh-elohei-Shem
m.bless("noach", "yhwh_elohei_shem")
# ‹וִיהִי כְנַעַן עֶבֶד לָמוֹ› (“and-let-him-be Canaan slave to-them”) —
# Noach speaks a demand — LET: yehi(Canaan, slave-of-lamo)
m.declare("noach", "LET",
          "yehi(kenaan, eved_lamo)")

# -------------------------- Gen.9.27 · THE_ENLARGEMENT_AND_THE_DWELLING ----
# יַפְתְּ אֱלֹהִים לְיֶפֶת וְיִשְׁכֹּן בְּאָהֳלֵי־שֵׁם וִיהִי כְנַעַן עֶבֶד
# לָמוֹ
# "God enlarge Japheth, and he shall dwell in the tents of Shem; and let
# Canaan be their servant."
m.step("Gen.9.27")
# ‹יַפְתְּ אֱלֹהִים לְיֶפֶת› (“may-He-enlarge God to-Yefet”) — Noach speaks
# a demand — LET: may-He-enlarge(God, to-Yefet)
m.declare("noach", "LET",
          "yaft(elohim, le_yefet)")
# ‹וְיִשְׁכֹּן בְּאָהֳלֵי־שֵׁם› (“and-may-he-dwell in-the-tents-of Shem”) —
# Noach speaks a demand — LET: may-he-dwell(in-aholei-Shem)
m.declare("noach", "LET",
          "yishkon(be_aholei_shem)")
# ‹וִיהִי כְנַעַן עֶבֶד לָמוֹ› (“and-let-him-be Canaan slave to-them”) —
# Noach speaks a demand — LET: yehi(Canaan, slave-of-lamo)
m.declare("noach", "LET",
          "yehi(kenaan, eved_lamo)")
# witness-tier presupposed read: translation_charter on tents_of_shem —
# read, not installed
m.witness_read("tents_of_shem", "translation_charter",
                cites=["Bereshit Rabbah 36:8", "Megillah 9b:4", "Mishnah Megillah 1:8", "Jerusalem Talmud Megillah 1:9:2", "Yoma 9b:18"])

# -------------------------- Gen.9.28 · THE_YEARS_AFTER_THE_DELUGE ----------
# וַיְחִי־נֹחַ אַחַר הַמַּבּוּל שְׁלֹשׁ מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה
# "And Noah lived after the flood three hundred and fifty years."
m.step("Gen.9.28")
# ‹וַיְחִי־נֹחַ אַחַר הַמַּבּוּל שְׁלֹשׁ מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה›
# (“and-he-lived Noah after the-deluge three hundred year and-fifty year”) —
# fact holds: and-he-lived-Noach-after-the-deluge-350-year
m.fact("va_yechi_noach_achar_ha_mabul_350_shanah")

# -------------------------- Gen.9.29 · THE_LEDGER_ROW_CLOSES ---------------
# וַיִּהְיוּ כָּל־יְמֵי־נֹחַ תְּשַׁע מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה
# וַיָּמֹת
# "And all the days of Noah were nine hundred and fifty years; and he died."
m.step("Gen.9.29")
# ‹וַיִּהְיוּ כָּל־יְמֵי־נֹחַ תְּשַׁע מֵאוֹת שָׁנָה וַחֲמִשִּׁים שָׁנָה›
# (“and-they-were all days-of Noah nine hundred year and-fifty year”) — fact
# holds: all-days-of-Noach-950-year
m.fact("kol_yemei_noach_950_shanah")
# ‹וַיָּמֹת› (“and-he-died”) — event: die — agent Noach
m.event("die", agent="noach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'kerem'}
    assert m.presupposed_set() == {'kenaan', 'noach', 'tevah'}
    assert m.REGISTRY["names"] == {'kenaan': 'arur'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['yehi(kenaan, eved_lamo)', 'yaft(elohim, le_yefet)', 'yishkon(be_aholei_shem)', 'yehi(kenaan, eved_lamo)']
    assert len(m.SPECS["log"]) == 4
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['bnei_noach_ha_yotzim_min_ha_tevah_shem_cham_va_yefet', 'cham_hu_avi_khenaan', 'shelosha_eleh_bnei_noach', 'u_me_eleh_naftzah_khol_ha_aretz', 'noach_ish_ha_adamah', 've_ervat_avihem_lo_rau', 'eved_avadim_yihyeh_le_echav(kenaan)', 'va_yechi_noach_achar_ha_mabul_350_shanah', 'kol_yemei_noach_950_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 22
    assert sorted(m.WORLD["witnessed"]) == ['the_offence']
    assert m.WORLD["witnessed"]['the_offence']["cites"] == ['Sanhedrin 70a:19', 'Bereshit Rabbah 36:7']
    assert all('castration_or_sodomy' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('drunkenness_verse', 'feminine_suffix_and_disputed_woe_count'), ('nakedness_covered', 'prayer_law_on_a_gentile_subject'), ('slave_curse', 'legal_category_name_yet_exitable'), ('tents_of_shem', 'translation_charter')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 36:4', 'Sanhedrin 70a:17']
    assert all('feminine_suffix_and_disputed_woe_count' not in f for f in m.WORLD["facts"])
    assert 'drunkenness_verse' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Berakhot 25b:11', 'Bereshit Rabbah 36:5']
    assert all('prayer_law_on_a_gentile_subject' not in f for f in m.WORLD["facts"])
    assert 'nakedness_covered' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Jerusalem Talmud Kiddushin 1:3:1', 'Bereshit Rabbah 61:7', 'Bereshit Rabbah 60:7']
    assert all('legal_category_name_yet_exitable' not in f for f in m.WORLD["facts"])
    assert 'slave_curse' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 36:8', 'Megillah 9b:4', 'Mishnah Megillah 1:8', 'Jerusalem Talmud Megillah 1:9:2', 'Yoma 9b:18']
    assert all('translation_charter' not in f for f in m.WORLD["facts"])
    assert 'tents_of_shem' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
