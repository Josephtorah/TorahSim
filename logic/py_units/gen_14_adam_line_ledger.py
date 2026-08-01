#!/usr/bin/env python3
# =============================================================================
# gen_14_adam_line_ledger — 5:1-32
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_14_adam_line_ledger.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The book of Adam's line: the death ledger and the man who walked (5:1-32)"""
from machine import Machine

m = Machine("gen_14_adam_line_ledger")

# -------------------------- Gen.5.1 · BOOK_HEADER_LIKENESS_ONLY ------------
# ze sefer toldot adam be-yom bero Elohim adam bi-demut Elohim asa et-o
# "This is the book of the generations of Adam. In the day that God created
# man, in the likeness of God made He him;"
m.step("Gen.5.1")
m.section("sefer_toledot_adam", "zeh sefer toledot adam — the book header labels; installs nothing")
m.fact("be_yom_bero_elohim_adam_bidmut_elohim_asah_oto")
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS (1:26, frozen day 6)",
             "bidmut elohim asah oto — LIKENESS ONLY, the image-word dropped from the restatement (5:1)")
m.presupposed("adam")

# -------------------------- Gen.5.2 · SPECIES_BLESSED_AND_NAMED ------------
# zakhar u-neqeva beraa-m va-yevarekh et-m va-yiqra et-shema-m adam be-yom
# hibara-m
# "male and female created He them, and blessed them, and called their name
# Adam, in the day when they were created."
m.step("Gen.5.2")
m.event("bless", agent="Elohim", themes=["zakhar_u_nekevah"])
m.name("adam_species", "Adam")
m.fact("zakhar_u_nekevah_beraam",
       "be_yom_hibaram")

# -------------------------- Gen.5.3 · SHET_IN_SWAPPED_IMAGE ----------------
# va-yechi adam sheloshim u-meat shana va-yoled bi-demut-o ke-tzalm-o va-
# yiqra et-shem-o shet
# "And Adam lived a hundred and thirty years, and begot a son in his own
# likeness, after his image; and called his name Seth."
m.step("Gen.5.3")
m.event("beget", agent="adam", themes=["shet"])
m.spec_delta("be-tzalmenu ki-dmutenu — in-our-IMAGE after-our-LIKENESS, God to human (1:26, frozen day 6)",
             "bi-dmuto ke-tzalmo — in-his-LIKENESS after-his-IMAGE: order swapped, prepositions swapped, direction man-to-son (5:3)")
m.name("shet", "Shet")

# -------------------------- Gen.5.4 · LEDGER_ADAM_AFTER --------------------
# va-yihyu yeme-adam achare holid-o et-shet shemone meot shana va-yoled
# banim u-vanot
# "And the days of Adam after he begot Seth were eight hundred years; and he
# begot sons and daughters."
m.step("Gen.5.4")
m.fact("banim_u_vanot(adam)")

# -------------------------- Gen.5.5 · LEDGER_ADAM_TOTAL_DIES ---------------
# va-yihyu kal-yeme adam asher-chay tesha meot shana u-sheloshim shana va-
# yamot
# "And all the days that Adam lived were nine hundred and thirty years; and
# he died."
m.step("Gen.5.5")
m.fact("kol_yemei_adam_930_shanah")
m.event("die", agent="adam")

# -------------------------- Gen.5.6 · LEDGER_SHET_BEGETS -------------------
# va-yechi-shet chamesh shanim u-meat shana va-yoled et-enosh
# "And Seth lived a hundred and five years, and begot Enosh."
m.step("Gen.5.6")
m.event("beget", agent="shet", themes=["enosh"])

# -------------------------- Gen.5.7 · LEDGER_SHET_AFTER --------------------
# va-yechi-shet achare holid-o et-enosh sheva shanim u-shemone meot shana
# va-yoled banim u-vanot
# "And Seth lived after he begot Enosh eight hundred and seven years, and
# begot sons and daughters."
m.step("Gen.5.7")
m.fact("banim_u_vanot(shet)")

# -------------------------- Gen.5.8 · LEDGER_SHET_TOTAL_DIES ---------------
# va-yihyu kal-yeme-shet shetem esre shana u-tesha meot shana va-yamot
# "And all the days of Seth were nine hundred and twelve years; and he
# died."
m.step("Gen.5.8")
m.fact("kol_yemei_shet_912_shanah")
m.event("die", agent="shet")

# -------------------------- Gen.5.9 · LEDGER_ENOSH_BEGETS ------------------
# va-yechi enosh tishim shana va-yoled et-qenan
# "And Enosh lived ninety years, and begot Kenan."
m.step("Gen.5.9")
m.event("beget", agent="enosh", themes=["qenan"])

# -------------------------- Gen.5.10 · LEDGER_ENOSH_AFTER ------------------
# va-yechi enosh achare holid-o et-qenan chamesh esre shana u-shemone meot
# shana va-yoled banim u-vanot
# "And Enosh lived after he begot Kenan eight hundred and fifteen years, and
# begot sons and daughters."
m.step("Gen.5.10")
m.fact("banim_u_vanot(enosh)")

# -------------------------- Gen.5.11 · LEDGER_ENOSH_TOTAL_DIES -------------
# va-yihyu kal-yeme enosh chamesh shanim u-tesha meot shana va-yamot
# "And all the days of Enosh were nine hundred and five years; and he died."
m.step("Gen.5.11")
m.fact("kol_yemei_enosh_905_shanah")
m.event("die", agent="enosh")

# -------------------------- Gen.5.12 · LEDGER_KENAN_BEGETS -----------------
# va-yechi qenan shivim shana va-yoled et-mahalalel
# "And Kenan lived seventy years, and begot Mahalalel."
m.step("Gen.5.12")
m.event("beget", agent="qenan", themes=["mahalalel"])

# -------------------------- Gen.5.13 · LEDGER_KENAN_AFTER ------------------
# va-yechi qenan achare holid-o et-mahalalel arbaim shana u-shemone meot
# shana va-yoled banim u-vanot
# "And Kenan lived after he begot Mahalalel eight hundred and forty years,
# and begot sons and daughters."
m.step("Gen.5.13")
m.fact("banim_u_vanot(qenan)")

# -------------------------- Gen.5.14 · LEDGER_KENAN_TOTAL_DIES -------------
# va-yihyu kal-yeme qenan eser shanim u-tesha meot shana va-yamot
# "And all the days of Kenan were nine hundred and ten years; and he died."
m.step("Gen.5.14")
m.fact("kol_yemei_qenan_910_shanah")
m.event("die", agent="qenan")

# -------------------------- Gen.5.15 · LEDGER_MAHALALEL_BEGETS -------------
# va-yechi mahalalel chamesh shanim ve-shishim shana va-yoled et-yared
# "And Mahalalel lived sixty and five years, and begot Jared."
m.step("Gen.5.15")
m.event("beget", agent="mahalalel", themes=["yered"])

# -------------------------- Gen.5.16 · LEDGER_MAHALALEL_AFTER --------------
# va-yechi mahalalel achare holid-o et-yered sheloshim shana u-shemone meot
# shana va-yoled banim u-vanot
# "And Mahalalel lived after he begot Jared eight hundred and thirty years,
# and begot sons and daughters."
m.step("Gen.5.16")
m.fact("banim_u_vanot(mahalalel)")

# -------------------------- Gen.5.17 · LEDGER_MAHALALEL_TOTAL_DIES ---------
# va-yihyu kal-yeme mahalalel chamesh ve-tishim shana u-shemone meot shana
# va-yamot
# "And all the days of Mahalalel were eight hundred ninety and five years;
# and he died."
m.step("Gen.5.17")
m.fact("kol_yemei_mahalalel_895_shanah")
m.event("die", agent="mahalalel")

# -------------------------- Gen.5.18 · LEDGER_YERED_BEGETS -----------------
# va-yechi-yered shetayim ve-shishim shana u-meat shana va-yoled et-chanokh
# "And Jared lived a hundred sixty and two years, and begot Enoch."
m.step("Gen.5.18")
m.event("beget", agent="yered", themes=["chanokh"])

# -------------------------- Gen.5.19 · LEDGER_YERED_AFTER ------------------
# va-yechi-yered achare holid-o et-chanokh shemone meot shana va-yoled banim
# u-vanot
# "And Jared lived after he begot Enoch eight hundred years, and begot sons
# and daughters."
m.step("Gen.5.19")
m.fact("banim_u_vanot(yered)")

# -------------------------- Gen.5.20 · LEDGER_YERED_TOTAL_DIES -------------
# va-yihyu kal-yeme-yered shetayim ve-shishim shana u-tesha meot shana va-
# yamot
# "And all the days of Jared were nine hundred sixty and two years; and he
# died."
m.step("Gen.5.20")
m.fact("kol_yemei_yered_962_shanah")
m.event("die", agent="yered")

# -------------------------- Gen.5.21 · LEDGER_CHANOKH_BEGETS ---------------
# va-yechi chanokh chamesh ve-shishim shana va-yoled et-metushalach
# "And Enoch lived sixty and five years, and begot Methuselah."
m.step("Gen.5.21")
m.event("beget", agent="chanokh", themes=["metushelach"])

# -------------------------- Gen.5.22 · WALK_REPLACES_LIVED -----------------
# va-yithalekh chanokh et-ha-Elohim achare holid-o et-metushelach shelosh
# meot shana va-yoled banim u-vanot
# "And Enoch walked with God after he begot Methuselah three hundred years,
# and begot sons and daughters."
m.step("Gen.5.22")
m.fact("hithalekh_chanokh_et_ha_elohim",
       "banim_u_vanot(chanokh)")

# -------------------------- Gen.5.23 · TOTAL_365_NO_REFRAIN_YET ------------
# va-yehi kal-yeme chanokh chamesh ve-shishim shana u-shelosh meot shana
# "And all the days of Enoch were three hundred sixty and five years."
m.step("Gen.5.23")
m.fact("kol_yemei_chanokh_365_shanah")

# -------------------------- Gen.5.24 · TAKEN_NOT_DEAD ----------------------
# va-yithalekh chanokh et-ha-Elohim ve-ene-nu ki-laqach et-o Elohim
# "And Enoch walked with God, and he was not; for God took him."
m.step("Gen.5.24")
m.fact("hithalekh_chanokh_et_ha_elohim",
       "einenu_ki_lakach_oto_elohim")
m.event("take", agent="Elohim", themes=["chanokh"])

# -------------------------- Gen.5.25 · LEDGER_METUSHELACH_BEGETS -----------
# va-yechi metushelach sheva u-shemonim shana u-meat shana va-yoled et-
# lamekh
# "And Methuselah lived a hundred eighty and seven years, and begot Lamech."
m.step("Gen.5.25")
m.event("beget", agent="metushelach", themes=["lemekh"])

# -------------------------- Gen.5.26 · LEDGER_METUSHELACH_AFTER ------------
# va-yechi metushelach achare holid-o et-lemekh shetayim u-shemonim shana
# u-sheva meot shana va-yoled banim u-vanot
# "And Methuselah lived after he begot Lamech seven hundred eighty and two
# years, and begot sons and daughters."
m.step("Gen.5.26")
m.fact("banim_u_vanot(metushelach)")

# -------------------------- Gen.5.27 · LEDGER_METUSHELACH_TOTAL_DIES -------
# va-yihyu kal-yeme metushelach tesha ve-shishim shana u-tesha meot shana
# va-yamot
# "And all the days of Methuselah were nine hundred sixty and nine years;
# and he died."
m.step("Gen.5.27")
m.fact("kol_yemei_metushelach_969_shanah")
m.event("die", agent="metushelach")

# -------------------------- Gen.5.28 · SON_BORN_NAMELESS -------------------
# va-yechi-lemekh shetayim u-shemonim shana u-meat shana va-yoled ben
# "And Lamech lived a hundred eighty and two years, and begot a son."
m.step("Gen.5.28")
m.event("beget", agent="lemekh", themes=["ben_unnamed"])

# -------------------------- Gen.5.29 · NOACH_NAMED_CURSE_QUOTED ------------
# va-yiqra et-shem-o nocha le-mor ze yenachame-nu mi-maase-nu u-me-itzvon
# yade-nu min-ha-adama asher erra-ה YHWH
# "And he called his name Noah, saying: 'This same shall comfort us in our
# work and in the toil of our hands, which cometh from the ground which the
# LORD hath cursed.'"
m.step("Gen.5.29")
m.name("noach", "Noach")
m.fact("zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu",
       "min_ha_adamah_asher_ererah_YHWH")
m.spec_delta("arurah ha-adamah baavurekha — the ground cursed, curser unnamed in the sentence text (3:17, frozen gen_11)",
             "ha-adamah asher ererah YHWH — the curse attributed to YHWH by name, plus a comfort forecast no one ratifies (5:29)")

# -------------------------- Gen.5.30 · LEDGER_LEMEKH_AFTER -----------------
# va-yechi-lemekh achare holid-o et-nocha chamesh ve-tishim shana va-chamesh
# meot shana va-yoled banim u-vanot
# "And Lamech lived after he begot Noah five hundred ninety and five years,
# and begot sons and daughters."
m.step("Gen.5.30")
m.fact("banim_u_vanot(lemekh)")

# -------------------------- Gen.5.31 · LEDGER_LEMEKH_TOTAL_777 -------------
# va-yehi kal-yeme-lemekh sheva ve-shivim shana u-sheva meot shana va-yamot
# "And all the days of Lamech were seven hundred seventy and seven years;
# and he died."
m.step("Gen.5.31")
m.fact("kol_yemei_lemekh_777_shanah")
m.event("die", agent="lemekh")

# -------------------------- Gen.5.32 · NOACH_500_THREE_SONS ----------------
# va-yehi-nocha ben-chamesh meot shana va-yoled nocha et-shem et-cham ve-et-
# yafet
# "And Noah was five hundred years old; and Noah begot Shem, Ham, and
# Japheth."
m.step("Gen.5.32")
m.fact("noach_ben_chamesh_meot_shanah")
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam'}
    assert m.REGISTRY["names"] == {'adam_species': 'Adam', 'shet': 'Shet', 'noach': 'Noach'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'spec_delta': 3, 'read_before_install': 1, 'named_before_any_presence': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['be_yom_bero_elohim_adam_bidmut_elohim_asah_oto', 'zakhar_u_nekevah_beraam', 'be_yom_hibaram', 'banim_u_vanot(adam)', 'kol_yemei_adam_930_shanah', 'banim_u_vanot(shet)', 'kol_yemei_shet_912_shanah', 'banim_u_vanot(enosh)', 'kol_yemei_enosh_905_shanah', 'banim_u_vanot(qenan)', 'kol_yemei_qenan_910_shanah', 'banim_u_vanot(mahalalel)', 'kol_yemei_mahalalel_895_shanah', 'banim_u_vanot(yered)', 'kol_yemei_yered_962_shanah', 'hithalekh_chanokh_et_ha_elohim', 'banim_u_vanot(chanokh)', 'kol_yemei_chanokh_365_shanah', 'hithalekh_chanokh_et_ha_elohim', 'einenu_ki_lakach_oto_elohim', 'banim_u_vanot(metushelach)', 'kol_yemei_metushelach_969_shanah', 'zeh_yenachamenu_mi_maasenu_u_me_itzvon_yadenu', 'min_ha_adamah_asher_ererah_YHWH', 'banim_u_vanot(lemekh)', 'kol_yemei_lemekh_777_shanah', 'noach_ben_chamesh_meot_shanah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 24
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
