#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_26_shem_ledger — 11:10-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_26_shem_ledger.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The deathless ledger: Shem to Terach, and the two deaths that land (11:10-32)"""
from machine import Machine

m = Machine("gen_26_shem_ledger")

# -------------------------- Gen.11.10-11 · SHEM_HEADER_AND_THE_FIRST_DEATHLESS_ROW -
# אֵלֶּה תּוֹלְדֹת שֵׁם שֵׁם בֶּן־מְאַת שָׁנָה וַיּוֹלֶד אֶת־אַרְפַּכְשָׁד
# שְׁנָתַיִם אַחַר הַמַּבּוּל … וַיּוֹלֶד בָּנִים וּבָנוֹת
# "These are the generations of Shem. Shem was a hundred years old, and
# begot Arpachshad two years after the flood. And Shem lived after he begot
# Arpachshad five hundred years, and begot sons and daughters."
m.step("Gen.11.10-11")
# ‹אֵלֶּה תּוֹלְדֹת שֵׁם› (“these generations Sem”) — section generations-
# Sem: eleh toldot shem — the sixth toledot header labels; installs nothing
m.section("toledot_shem", "eleh toldot shem — the sixth toledot header labels; installs nothing")
# ‹שֵׁם בֶּן־מְאַת שָׁנָה … שְׁנָתַיִם אַחַר הַמַּבּוּל› (“Sem son hundred
# years … years after the-deluge”) — fact holds: Sem-son-hundred-year;
# years-after-the-deluge
m.fact("shem_ben_meat_shanah",
       "shenatayim_achar_ha_mabul")
# ‹וַיּוֹלֶד אֶת־אַרְפַּכְשָׁד› (“and-bear-young obj-marker Arphaxad”) —
# event: beget — agent Sem; theme Arphaxad
m.event("beget", agent="shem", themes=["arpakhshad"])
# ‹וַיְחִי־שֵׁם אַחֲרֵי הוֹלִידוֹ אֶת־אַרְפַּכְשָׁד חֲמֵשׁ מֵאוֹת שָׁנָה
# וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Sem after bear-young-him/its obj-
# marker Arphaxad five hundred years and-bear-young son and-daughter”) —
# fact holds: son-and-daughter(Sem)
m.fact("banim_u_vanot(shem)")

# -------------------------- Gen.11.12-13 · ARPACHSHAD_ROW_FRONTED_PERFECT --
# וְאַרְפַּכְשַׁד חַי חָמֵשׁ וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שָׁלַח …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Arpachshad lived five and thirty years, and begot Shelah. And
# Arpachshad lived after he begot Shelah four hundred and three years, and
# begot sons and daughters."
m.step("Gen.11.12-13")
# ‹וְאַרְפַּכְשַׁד חַי חָמֵשׁ וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שָׁלַח›
# (“and-Arphaxad live five and-thirty years and-bear-young obj-marker
# Salah”) — event: beget — agent Arphaxad; theme Salah
m.event("beget", agent="arpakhshad", themes=["shelach"])
# ‹וַיְחִי אַרְפַּכְשַׁד … שָׁלֹשׁ שָׁנִים וְאַרְבַּע מֵאוֹת שָׁנָה
# וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Arphaxad … three years and-four
# hundred years and-bear-young son and-daughter”) — fact holds: son-and-
# daughter(Arphaxad)
m.fact("banim_u_vanot(arpakhshad)")

# -------------------------- Gen.11.14-15 · SHELACH_ROW_FRONTED_PERFECT -----
# וְשֶׁלַח חַי שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־עֵבֶר … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Shelah lived thirty years, and begot Eber. And Shelah lived after he
# begot Eber four hundred and three years, and begot sons and daughters."
m.step("Gen.11.14-15")
# ‹וְשֶׁלַח חַי שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־עֵבֶר› (“and-Salah live
# thirty years and-bear-young obj-marker Eber”) — event: beget — agent
# Salah; theme Eber
m.event("beget", agent="shelach", themes=["ever"])
# ‹וַיְחִי־שֶׁלַח … שָׁלֹשׁ שָׁנִים וְאַרְבַּע מֵאוֹת שָׁנָה וַיּוֹלֶד
# בָּנִים וּבָנוֹת› (“and-live Salah … three years and-four hundred years
# and-bear-young son and-daughter”) — fact holds: son-and-daughter(Salah)
m.fact("banim_u_vanot(shelach)")

# -------------------------- Gen.11.16-17 · EVER_ROW_WAYYIQTOL_RESUMES ------
# וַיְחִי־עֵבֶר אַרְבַּע וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־פָּלֶג …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Eber lived four and thirty years, and begot Peleg. And Eber lived
# after he begot Peleg four hundred and thirty years, and begot sons and
# daughters."
m.step("Gen.11.16-17")
# ‹וַיְחִי־עֵבֶר אַרְבַּע וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־פָּלֶג› (“and-
# live Eber four and-thirty years and-bear-young obj-marker Peleg”) — event:
# beget — agent Eber; theme Peleg
m.event("beget", agent="ever", themes=["peleg"])
# ‹וַיְחִי־עֵבֶר אַחֲרֵי הוֹלִידוֹ אֶת־פֶּלֶג שְׁלֹשִׁים שָׁנָה וְאַרְבַּע
# מֵאוֹת שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Eber after bear-
# young-him/its obj-marker Peleg thirty years and-four hundred years and-
# bear-young son and-daughter”) — fact holds: son-and-daughter(Eber)
m.fact("banim_u_vanot(ever)")

# -------------------------- Gen.11.18-19 · PELEG_ROW_CAREER_CLOSES ---------
# וַיְחִי־פֶלֶג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־רְעוּ … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Peleg lived thirty years, and begot Reu. And Peleg lived after he
# begot Reu two hundred and nine years, and begot sons and daughters."
m.step("Gen.11.18-19")
# ‹וַיְחִי־פֶלֶג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־רְעוּ› (“and-live Peleg
# thirty years and-bear-young obj-marker Reu”) — event: beget — agent Peleg;
# theme Reu
m.event("beget", agent="peleg", themes=["reu"])
# ‹וַיְחִי־פֶלֶג אַחֲרֵי הוֹלִידוֹ אֶת־רְעוּ תֵּשַׁע שָׁנִים וּמָאתַיִם
# שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Peleg after bear-young-
# him/its obj-marker Reu nine years and-hundred years and-bear-young son
# and-daughter”) — fact holds: son-and-daughter(Peleg)
m.fact("banim_u_vanot(peleg)")

# -------------------------- Gen.11.20-21 · REU_ROW_WHOLE_CAREER_IN_SPAN ----
# וַיְחִי רְעוּ שְׁתַּיִם וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שְׂרוּג …
# וַיּוֹלֶד בָּנִים וּבָנוֹת
# "And Reu lived two and thirty years, and begot Serug. And Reu lived after
# he begot Serug two hundred and seven years, and begot sons and daughters."
m.step("Gen.11.20-21")
# ‹וַיְחִי רְעוּ שְׁתַּיִם וּשְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־שְׂרוּג› (“and-
# live Reu two and-thirty years and-bear-young obj-marker Serug”) — event:
# beget — agent Reu; theme Serug
m.event("beget", agent="reu", themes=["serug"])
# ‹וַיְחִי רְעוּ אַחֲרֵי הוֹלִידוֹ אֶת־שְׂרוּג שֶׁבַע שָׁנִים וּמָאתַיִם
# שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Reu after bear-young-him/its
# obj-marker Serug seven years and-hundred years and-bear-young son and-
# daughter”) — fact holds: son-and-daughter(Reu)
m.fact("banim_u_vanot(reu)")

# -------------------------- Gen.11.22-23 · SERUG_ROW_BEGETS_THE_FIRST_NACHOR -
# וַיְחִי שְׂרוּג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־נָחוֹר … וַיּוֹלֶד בָּנִים
# וּבָנוֹת
# "And Serug lived thirty years, and begot Nahor. And Serug lived after he
# begot Nahor two hundred years, and begot sons and daughters."
m.step("Gen.11.22-23")
# ‹וַיְחִי שְׂרוּג שְׁלֹשִׁים שָׁנָה וַיּוֹלֶד אֶת־נָחוֹר› (“and-live Serug
# thirty years and-bear-young obj-marker Nahor”) — event: beget — agent
# Serug; theme Nahor-son-Serug
m.event("beget", agent="serug", themes=["nachor_ben_serug"])
# ‹וַיְחִי שְׂרוּג אַחֲרֵי הוֹלִידוֹ אֶת־נָחוֹר מָאתַיִם שָׁנָה וַיּוֹלֶד
# בָּנִים וּבָנוֹת› (“and-live Serug after bear-young-him/its obj-marker
# Nahor hundred years and-bear-young son and-daughter”) — fact holds: son-
# and-daughter(Serug)
m.fact("banim_u_vanot(serug)")

# -------------------------- Gen.11.24-25 · NACHOR_ROW_BEGETS_TERACH --------
# וַיְחִי נָחוֹר תֵּשַׁע וְעֶשְׂרִים שָׁנָה וַיּוֹלֶד אֶת־תָּרַח … וַיּוֹלֶד
# בָּנִים וּבָנוֹת
# "And Nahor lived nine and twenty years, and begot Terah. And Nahor lived
# after he begot Terah a hundred and nineteen years, and begot sons and
# daughters."
m.step("Gen.11.24-25")
# ‹וַיְחִי נָחוֹר תֵּשַׁע וְעֶשְׂרִים שָׁנָה וַיּוֹלֶד אֶת־תָּרַח› (“and-
# live Nahor nine and-twenty years and-bear-young obj-marker Tarah”) —
# event: beget — agent Nahor-son-Serug; theme Tarah
m.event("beget", agent="nachor_ben_serug", themes=["terach"])
# ‹וַיְחִי נָחוֹר אַחֲרֵי הוֹלִידוֹ אֶת־תֶּרַח תְּשַׁע־עֶשְׂרֵה שָׁנָה
# וּמְאַת שָׁנָה וַיּוֹלֶד בָּנִים וּבָנוֹת› (“and-live Nahor after bear-
# young-him/its obj-marker Tarah nine -teen years and-hundred years and-
# bear-young son and-daughter”) — fact holds: son-and-daughter(Nahor-son-
# Serug)
m.fact("banim_u_vanot(nachor_ben_serug)")

# -------------------------- Gen.11.26 · TERACH_ROW_OPENS_THREE_SONS --------
# וַיְחִי־תֶרַח שִׁבְעִים שָׁנָה וַיּוֹלֶד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן
# "And Terah lived seventy years, and begot Abram, Nahor, and Haran."
m.step("Gen.11.26")
# ‹וַיְחִי־תֶרַח שִׁבְעִים שָׁנָה וַיּוֹלֶד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן› (“and-live Tarah seventy years and-bear-young obj-marker
# Abram obj-marker Nahor and-obj-marker Haran”) — event: beget — agent
# Tarah; theme Abram, Nahor-son-Tarah, Haran
m.event("beget", agent="terach", themes=["avram", "nachor_ben_terach", "haran"])

# -------------------------- Gen.11.27 · TERACH_HEADER_INSIDE_THE_OPEN_ROW --
# וְאֵלֶּה תּוֹלְדֹת תֶּרַח תֶּרַח הוֹלִיד אֶת־אַבְרָם אֶת־נָחוֹר
# וְאֶת־הָרָן וְהָרָן הוֹלִיד אֶת־לוֹט
# "Now these are the generations of Terah. Terah begot Abram, Nahor, and
# Haran; and Haran begot Lot."
m.step("Gen.11.27")
# ‹וְאֵלֶּה תּוֹלְדֹת תֶּרַח› (“and-these generations Tarah”) — section
# generations-Tarah: ve-eleh toldot terach — the seventh toledot header
# labels; installs nothing
m.section("toledot_terach", "ve-eleh toldot terach — the seventh toledot header labels; installs nothing")
# ‹וְהָרָן הוֹלִיד אֶת־לוֹט› (“and-Haran bear-young obj-marker Lot”) —
# event: beget — agent Haran; theme Lot
m.event("beget", agent="haran", themes=["lot"])

# -------------------------- Gen.11.28 · HARAN_DIES_BEFORE_HIS_FATHER -------
# וַיָּמָת הָרָן עַל־פְּנֵי תֶּרַח אָבִיו בְּאֶרֶץ מוֹלַדְתּוֹ בְּאוּר
# כַּשְׂדִּים
# "And Haran died in the presence of his father Terah in the land of his
# nativity, in Ur of the Chaldees."
m.step("Gen.11.28")
# ‹וַיָּמָת הָרָן עַל־פְּנֵי תֶּרַח אָבִיו› (“and-die Haran over face Tarah
# father-him/its”) — event: die — agent Haran
m.event("die", agent="haran")
# ‹בְּאֶרֶץ מוֹלַדְתּוֹ בְּאוּר כַּשְׂדִּים› (“in-earth nativity-him/its in-
# Ur Chaldeans”) — fact holds: in-earth-moladto-in-Ur-Chaldeans(Haran)
m.fact("be_eretz_moladto_be_ur_kasdim(haran)")
# reads without prior install (flag, not fix): Ur-Chaldeans
m.presupposed("ur_kasdim")

# -------------------------- Gen.11.29 · THE_WIVES_TAKEN_ONE_GENEALOGY_WITHHELD -
# וַיִּקַּח אַבְרָם וְנָחוֹר לָהֶם נָשִׁים שֵׁם אֵשֶׁת־אַבְרָם שָׂרָי וְשֵׁם
# אֵשֶׁת־נָחוֹר מִלְכָּה בַּת־הָרָן אֲבִי־מִלְכָּה וַאֲבִי יִסְכָּה
# "And Abram and Nahor took them wives: the name of Abram's wife was Sarai;
# and the name of Nahor's wife, Milcah, the daughter of Haran, the father of
# Milcah, and the father of Iscah."
m.step("Gen.11.29")
# ‹וַיִּקַּח אַבְרָם וְנָחוֹר לָהֶם נָשִׁים› (“and-take Abram and-Nahor to-
# them/their woman”) — event: take — agent Abram; theme woman
m.event("take", agent="avram", themes=["nashim"])
# ‹שֵׁם אֵשֶׁת־אַבְרָם שָׂרָי וְשֵׁם אֵשֶׁת־נָחוֹר מִלְכָּה› (“name woman
# Abram Sarai and-name woman Nahor Milcah”) — fact holds: Sem-woman-Abram-
# Sarai; Sem-woman-Nahor-milkah
m.fact("shem_eshet_avram_saray",
       "shem_eshet_nachor_milkah")
# ‹מִלְכָּה בַּת־הָרָן אֲבִי־מִלְכָּה וַאֲבִי יִסְכָּה› (“Milcah daughter
# Haran father Milcah and-father Iscah”) — fact holds: milkah-daughter-
# Haran; Haran-father-milkah-and-father-yiskah
m.fact("milkah_bat_haran",
       "haran_avi_milkah_va_avi_yiskah")

# -------------------------- Gen.11.30 · SARAI_BARREN_THE_DOUBLED_ABSENCE ---
# וַתְּהִי שָׂרַי עֲקָרָה אֵין לָהּ וָלָד
# "And Sarai was barren; she had no child."
m.step("Gen.11.30")
# ‹וַתְּהִי שָׂרַי עֲקָרָה› (“and-be Sarai sterile”) — fact holds: Sarai-
# akarah
m.fact("saray_akarah")
# ‹אֵין לָהּ וָלָד› (“there-is-not to-her/its boy”) — fact holds: ein-lah-
# boy
m.fact("ein_lah_valad")

# -------------------------- Gen.11.31 · THE_JOURNEY_STATED_STOPPED_SETTLED -
# וַיִּקַּח תֶּרַח אֶת־אַבְרָם בְּנוֹ וְאֶת־לוֹט בֶּן־הָרָן בֶּן־בְּנוֹ
# וְאֵת שָׂרַי כַּלָּתוֹ אֵשֶׁת אַבְרָם בְּנוֹ וַיֵּצְאוּ אִתָּם מֵאוּר
# כַּשְׂדִּים לָלֶכֶת אַרְצָה כְּנַעַן וַיָּבֹאוּ עַד־חָרָן וַיֵּשְׁבוּ שָׁם
# "And Terah took Abram his son, and Lot the son of Haran, his son's son,
# and Sarai his daughter-in-law, his son Abram's wife; and they went forth
# with them from Ur of the Chaldees, to go into the land of Canaan; and they
# came unto Haran, and dwelt there."
m.step("Gen.11.31")
# ‹וַיִּקַּח תֶּרַח אֶת־אַבְרָם בְּנוֹ וְאֶת־לוֹט בֶּן־הָרָן בֶּן־בְּנוֹ
# וְאֵת שָׂרַי כַּלָּתוֹ אֵשֶׁת אַבְרָם בְּנוֹ› (“and-take Tarah obj-marker
# Abram son-him/its and-obj-marker Lot son Haran son son-him/its and-obj-
# marker Sarai bride-him/its woman Abram son-him/its”) — event: take — agent
# Tarah; theme Abram, Lot, Sarai
m.event("take", agent="terach", themes=["avram", "lot", "saray"])
# ‹וַיֵּצְאוּ אִתָּם מֵאוּר כַּשְׂדִּים› (“and-bring-forth with-them/their
# from-Ur Chaldeans”) — event: go-out — agent Tarah
m.event("go_out", agent="terach")
# ‹לָלֶכֶת אַרְצָה כְּנַעַן› (“to-go earth-ward Canaan”) — fact holds: to-
# go-artzah-Canaan
m.fact("la_lekhet_artzah_kenaan")
# ‹וַיָּבֹאוּ עַד־חָרָן› (“and-come/bring until Haran”) — event: come —
# agent Tarah
m.event("come", agent="terach")
# ‹וַיֵּשְׁבוּ שָׁם› (“and-dwell/sit there”) — event: settle — agent Tarah
m.event("settle", agent="terach")
# reads without prior install (flag, not fix): Haran, earth-Canaan
m.presupposed("charan", "eretz_kenaan")

# -------------------------- Gen.11.32 · TERACH_ROW_CLOSES_WITHOUT_ALL ------
# וַיִּהְיוּ יְמֵי־תֶרַח חָמֵשׁ שָׁנִים וּמָאתַיִם שָׁנָה וַיָּמָת תֶּרַח
# בְּחָרָן
# "And the days of Terah were two hundred and five years; and Terah died in
# Haran."
m.step("Gen.11.32")
# ‹וַיִּהְיוּ יְמֵי־תֶרַח חָמֵשׁ שָׁנִים וּמָאתַיִם שָׁנָה› (“and-be day
# Tarah five years and-hundred years”) — fact holds: days-of-Tarah-205-year
m.fact("yemei_terach_205_shanah")
# ‹וַיָּמָת תֶּרַח בְּחָרָן› (“and-die Tarah in-Haran”) — event: die — agent
# Tarah
m.event("die", agent="terach")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'charan', 'eretz_kenaan', 'ur_kasdim'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['shem_ben_meat_shanah', 'shenatayim_achar_ha_mabul', 'banim_u_vanot(shem)', 'banim_u_vanot(arpakhshad)', 'banim_u_vanot(shelach)', 'banim_u_vanot(ever)', 'banim_u_vanot(peleg)', 'banim_u_vanot(reu)', 'banim_u_vanot(serug)', 'banim_u_vanot(nachor_ben_serug)', 'be_eretz_moladto_be_ur_kasdim(haran)', 'shem_eshet_avram_saray', 'shem_eshet_nachor_milkah', 'milkah_bat_haran', 'haran_avi_milkah_va_avi_yiskah', 'saray_akarah', 'ein_lah_valad', 'la_lekhet_artzah_kenaan', 'yemei_terach_205_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
