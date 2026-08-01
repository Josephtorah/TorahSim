#!/usr/bin/env python3
# =============================================================================
# gen_16_ark_spec — 6:9-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_16_ark_spec.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The ark spec: the blueprint, the covenant word, the first obeyed command (6:9-22)"""
from machine import Machine

m = Machine("gen_16_ark_spec")

# -------------------------- Gen.6.9 · TOLEDOT_NOACH_THE_WALKER -------------
# eleh toledot Noach Noach ish tzaddik tamim hayah be-dorotav et-ha-Elohim
# hithalekh-Noach
# "These are the generations of Noah. Noah was in his generations a man
# righteous and whole-hearted; Noah walked with God."
m.step("Gen.6.9")
m.section("toledot_noach", "eleh toledot noach — the third generations header")
m.fact("ish_tzaddik_tamim_be_dorotav",
       "et_ha_elohim_hithalekh_noach")
m.presupposed("noach")

# -------------------------- Gen.6.10 · THREE_SONS_RESTATED -----------------
# va-yoled Noach shloshah vanim et-Shem et-Cham ve-et-Yafet
# "And Noah begot three sons, Shem, Ham, and Japheth."
m.step("Gen.6.10")
m.event("beget", agent="noach", themes=["shem", "cham", "yafet"])

# -------------------------- Gen.6.11 · EARTH_CORRUPTED_FILLED --------------
# va-tishachet ha-aretz lifnei ha-Elohim va-timale ha-aretz chamas
# "And the earth was corrupt before God, and the earth was filled with
# violence."
m.step("Gen.6.11")
m.event("corrupt", themes=["ha_aretz"])
m.fact("va_timale_ha_aretz_chamas")

# -------------------------- Gen.6.12 · THIRD_SEEING_BEHOLD_CORRUPTED -------
# va-yar Elohim et-ha-aretz ve-hinneh nishchatah ki-hishchit kol-basar et-
# darko al-ha-aretz
# "And God saw the earth, and, behold, it was corrupt; for all flesh had
# corrupted their way upon the earth."
m.step("Gen.6.12")
m.event("see", agent="Elohim", themes=["ha_aretz"])
m.spec_delta("va-yar Elohim et-kol-asher asah ve-hinneh tov meod — and behold, very good (1:31, frozen day 6)",
             "va-yar Elohim et-ha-aretz ve-hinneh nishchatah — and behold, CORRUPTED (6:12)")
m.fact("hishchit_kol_basar_et_darko")

# -------------------------- Gen.6.13 · END_DECREE_SPOKEN_TO_NOACH ----------
# va-yomer Elohim le-Noach qetz kol-basar ba lefanai ki-malah ha-aretz
# chamas mi-pneihem ve-hineni mashchitam et-ha-aretz
# "And God said unto Noah: 'The end of all flesh is come before Me; for the
# earth is filled with violence through them; and, behold, I will destroy
# them with the earth.'"
m.step("Gen.6.13")
m.event("say", agent="Elohim", themes=["noach"])
m.fact("qetz_kol_basar_ba_lefanai",
       "hineni_mashchitam_et_ha_aretz")

# -------------------------- Gen.6.14 · COMMISSION_MAKE_THE_ARK -------------
# aseh lekha tevat atzei-gofer qinim taaseh et-ha-tevah ve-khafarta otah mi-
# bayit u-mi-chutz ba-kofer
# "Make thee an ark of gopher wood; with rooms shalt thou make the ark, and
# shalt pitch it within and without with pitch."
m.step("Gen.6.14")
m.declare("Elohim", "LET",
          "aseh(noach, tevah)")
m.fact("tevat_atzei_gofer_qinim",
       "ve_khafarta_ba_kofer")

# -------------------------- Gen.6.15 · BLUEPRINT_DIMENSIONS ----------------
# ve-zeh asher taaseh otah shlosh meot amah orekh ha-tevah chamishim amah
# rochbah u-shloshim amah qomatah
# "And this is how thou shalt make it: the length of the ark three hundred
# cubits, the breadth of it fifty cubits, and the height of it thirty
# cubits."
m.step("Gen.6.15")
m.fact("shelosh_meot_amah_orekh",
       "chamishim_amah_rochbah",
       "sheloshim_amah_qomatah")

# -------------------------- Gen.6.16 · BLUEPRINT_LIGHT_DOOR_DECKS ----------
# tzohar taaseh la-tevah ve-el-amah tekhalenah mi-lemalah u-fetach ha-tevah
# be-tzidah tasim tachtiyim shniyim u-shlishim taaseha
# "A light shalt thou make to the ark, and to a cubit shalt thou finish it
# upward; and the door of the ark shalt thou set in the side thereof; with
# lower, second, and third stories shalt thou make it."
m.step("Gen.6.16")
m.fact("tzohar_la_tevah",
       "petach_ba_tzidah",
       "tachtiyim_shniyim_u_shlishim")

# -------------------------- Gen.6.17 · FLOOD_ANNOUNCED ---------------------
# va-ani hineni mevi et-ha-mabul mayim al-ha-aretz le-shachet kol-basar
# asher-bo ruach chayim mi-tachat ha-shamayim kol asher-ba-aretz yigva
# "And I, behold, I do bring the flood of waters upon the earth, to destroy
# all flesh, wherein is the breath of life, from under heaven; every thing
# that is in the earth shall perish."
m.step("Gen.6.17")
m.fact("hineni_mevi_et_ha_mabul_mayim",
       "kol_asher_ba_aretz_yigva")

# -------------------------- Gen.6.18 · COVENANT_PROMISED_BOARDING_LIST -----
# va-hakimoti et-briti itakh u-vata el-ha-tevah atah u-vanekha ve-ishtekha
# u-neshei-vanekha itakh
# "But I will establish My covenant with thee; and thou shalt come into the
# ark, thou, and thy sons, and thy wife, and thy sons' wives with thee."
m.step("Gen.6.18")
m.fact("va_hakimoti_et_briti_itakh",
       "u_vata_el_ha_tevah_atah_u_vanekha")

# -------------------------- Gen.6.19 · MANIFEST_TWO_OF_ALL -----------------
# u-mi-kol-ha-chai mi-kol-basar shnayim mi-kol tavi el-ha-tevah le-hachayot
# itakh zakhar u-nekevah yihyu
# "And of every living thing of all flesh, two of every sort shalt thou
# bring into the ark, to keep them alive with thee; they shall be male and
# female."
m.step("Gen.6.19")
m.fact("shnayim_mi_kol_tavi_el_ha_tevah",
       "zakhar_u_nekevah_yihyu")

# -------------------------- Gen.6.20 · MANIFEST_BY_KINDS_SELF_LOADING ------
# me-ha-of le-minehu u-min-ha-behemah le-minah mi-kol remes ha-adamah le-
# minehu shnayim mi-kol yavou elekha le-hachayot
# "Of the fowl after their kind, and of the cattle after their kind, of
# every creeping thing of the ground after its kind, two of every sort shall
# come unto thee, to keep them alive."
m.step("Gen.6.20")
m.fact("le_minehu_manifest_of_behemah_remes")

# -------------------------- Gen.6.21 · SECOND_IMPERATIVE_PROVISIONS --------
# ve-atah qach-lekha mi-kol-maakhal asher yeakhel ve-asafta elekha ve-hayah
# lekha ve-lahem le-akhlah
# "And take thou unto thee of all food that is eaten, and gather it to thee;
# and it shall be for food for thee, and for them.'"
m.step("Gen.6.21")
m.declare("Elohim", "LET",
          "qach(noach, mi_kol_maakhal)")
m.fact("ve_hayah_lekha_ve_lahem_le_akhlah")

# -------------------------- Gen.6.22 · THE_RECEIPT_BOTH_POPPED -------------
# va-yaas Noach ke-khol asher tzivah oto Elohim ken asah
# "Thus did Noah; according to all that God commanded him, so did he."
m.step("Gen.6.22")
m.event("make", agent="noach", themes=["tevah"])
m.install("tevah")
m.result("aseh(noach, tevah)", tmark="t2")
m.result("qach(noach, mi_kol_maakhal)", tmark="t2")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'tevah'}
    assert m.presupposed_set() == {'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 1, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['ish_tzaddik_tamim_be_dorotav', 'et_ha_elohim_hithalekh_noach', 'va_timale_ha_aretz_chamas', 'hishchit_kol_basar_et_darko', 'qetz_kol_basar_ba_lefanai', 'hineni_mashchitam_et_ha_aretz', 'tevat_atzei_gofer_qinim', 've_khafarta_ba_kofer', 'shelosh_meot_amah_orekh', 'chamishim_amah_rochbah', 'sheloshim_amah_qomatah', 'tzohar_la_tevah', 'petach_ba_tzidah', 'tachtiyim_shniyim_u_shlishim', 'hineni_mevi_et_ha_mabul_mayim', 'kol_asher_ba_aretz_yigva', 'va_hakimoti_et_briti_itakh', 'u_vata_el_ha_tevah_atah_u_vanekha', 'shnayim_mi_kol_tavi_el_ha_tevah', 'zakhar_u_nekevah_yihyu', 'le_minehu_manifest_of_behemah_remes', 've_hayah_lekha_ve_lahem_le_akhlah'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 10
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
