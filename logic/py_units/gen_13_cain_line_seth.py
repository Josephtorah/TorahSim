#!/usr/bin/env python3
# =============================================================================
# gen_13_cain_line_seth — 4:17-26
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_13_cain_line_seth.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Cain's line and Seth: the first city, the crafts, seventy-seven, calling on the Name (4:17-26)"""
from machine import Machine

m = Machine("gen_13_cain_line_seth")

# -------------------------- Gen.4.17 · FIRST_CITY_BUILT_NAMED --------------
# va-yeda Kayin et-ishto va-tahar va-teled et-Chanokh va-yehi boneh ir va-
# yiqra shem ha-ir ke-shem beno Chanokh
# "And Cain knew his wife; and she conceived, and bore Enoch; and he builded
# a city, and called the name of the city after the name of his son Enoch."
m.step("Gen.4.17")
m.event("bear", agent="eshet_kayin", themes=["chanokh"])
m.install("ir")
m.name("ir", "Chanokh")
m.presupposed("kayin", "eshet_kayin")

# -------------------------- Gen.4.18 · BEGETTING_CHAIN_FOUR_LINKS ----------
# va-yivaled la-Chanokh et-Irad ve-Irad yalad et-Mechuyael u-Mechiyael yalad
# et-Metushael u-Metushael yalad et-Lamekh
# "And unto Enoch was born Irad; and Irad begot Mehujael; and Mehujael begot
# Methushael; and Methushael begot Lamech."
m.step("Gen.4.18")
m.event("born", themes=["irad"])
m.event("beget", agent="irad", themes=["mechuyael"])
m.event("beget", agent="mechuyael", themes=["metushael"])
m.event("beget", agent="metushael", themes=["lemekh"])

# -------------------------- Gen.4.19 · FIRST_POLYGAMY ----------------------
# va-yiqach-lo Lemekh shtei nashim shem ha-achat Adah ve-shem ha-shenit
# Tzilah
# "And Lamech took unto him two wives; the name of the one was Adah, and the
# name of the other Zillah."
m.step("Gen.4.19")
m.event("take", agent="lemekh", themes=["shte_nashim"])
m.fact("shte_nashim_le_lemekh",
       "shem_ha_achat_adah",
       "shem_ha_shenit_tzilah")

# -------------------------- Gen.4.20 · OFFICE_TENT_AND_HERD ----------------
# va-teled Adah et-Yaval hu hayah avi yoshev ohel u-mikneh
# "And Adah bore Jabal; he was the father of such as dwell in tents and have
# cattle."
m.step("Gen.4.20")
m.event("bear", agent="adah", themes=["yaval"])
m.fact("avi_yoshev_ohel_u_mikneh(yaval)")

# -------------------------- Gen.4.21 · OFFICE_HARP_AND_PIPE ----------------
# ve-shem achiv Yuval hu hayah avi kol-tofes kinor ve-ugav
# "And his brother's name was Jubal; he was the father of all such as handle
# the harp and pipe."
m.step("Gen.4.21")
m.fact("shem_achiv_yuval",
       "avi_kol_tofes_kinor_ve_ugav(yuval)")

# -------------------------- Gen.4.22 · OFFICE_BRONZE_IRON_SISTER -----------
# ve-Tzilah gam-hi yaldah et-Tuval-Kayin lotesh kol-choresh nechoshet
# u-varzel va-achot Tuval-Kayin Naamah
# "And Zillah, she also bore Tubal-cain, the forger of every cutting
# instrument of brass and iron; and the sister of Tubal-cain was Naamah."
m.step("Gen.4.22")
m.event("bear", agent="tzilah", themes=["tuval_kayin"])
m.fact("lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)",
       "achot_tuval_kayin_naamah")

# -------------------------- Gen.4.23 · SWORD_SONG_FIRST_HUMAN_IMPERATIVES --
# va-yomer Lemekh le-nashav Adah ve-Tzilah shemaan qoli neshei Lemekh
# haazenah imrati ki ish haragti le-fitzi ve-yeled le-chaburati
# "And Lamech said unto his wives: Adah and Zillah, hear my voice; ye wives
# of Lamech, hearken unto my speech; for I have slain a man for wounding me,
# and a young man for bruising me."
m.step("Gen.4.23")
m.event("say", agent="lemekh", themes=["neshei_lemekh"])
m.declare("lemekh", "LET",
          "shema(neshei_lemekh, qol_lemekh)")
m.fact("ish_haragti_le_fitzi_ve_yeled_le_chaburati")

# -------------------------- Gen.4.24 · QUOTE_DIFF_SEVENTY_SEVEN ------------
# ki shivatayim yukam-Kayin ve-Lemekh shivim ve-shivah
# "If Cain shall be avenged sevenfold, truly Lamech seventy and sevenfold."
m.step("Gen.4.24")
m.spec_delta("kol-horeg Kayin shivatayim yukam — issuer YHWH, decree with mark (4:15, frozen gen_12)",
             "ki shivatayim yukam-Kayin ve-Lemekh shivim ve-shivah — issuer lemekh, boast, multiplier x11, target self, ratification NONE (4:24)")

# -------------------------- Gen.4.25 · SETH_REPLACEMENT_SEED ---------------
# va-yeda Adam od et-ishto va-teled ben va-tiqra et-shemo Shet ki shat-li
# Elohim zera acher tachat Hevel ki harago Kayin
# "And Adam knew his wife again; and she bore a son, and called his name
# Seth: 'for God hath appointed me another seed instead of Abel; for Cain
# slew him.'"
m.step("Gen.4.25")
m.event("bear", agent="eshet_adam", themes=["shet"])
m.name("shet", "Shet")
m.fact("shat_li_elohim_zera_acher_tachat_hevel",
       "harago_kayin_named_in_speech")
m.presupposed("adam", "eshet_adam")

# -------------------------- Gen.4.26 · ENOSH_CALLING_ON_THE_NAME -----------
# u-le-Shet gam-hu yulad-ben va-yiqra et-shemo Enosh az huchal likro be-shem
# YHWH
# "And to Seth, to him also there was born a son; and he called his name
# Enosh; then began men to call upon the name of the LORD."
m.step("Gen.4.26")
m.event("born", themes=["enosh"])
m.name("enosh", "Enosh")
m.fact("huchal_likro_be_shem_YHWH")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'ir'}
    assert m.presupposed_set() == {'adam', 'eshet_kayin', 'eshet_adam', 'kayin'}
    assert m.REGISTRY["names"] == {'ir': 'Chanokh', 'shet': 'Shet', 'enosh': 'Enosh'}
    assert m.REGISTRY["writes"] == 3
    assert m.tests_list() == []
    assert m.open_demands() == ['shema(neshei_lemekh, qol_lemekh)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 4, 'spec_delta': 1, 'named_before_any_presence': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['shte_nashim_le_lemekh', 'shem_ha_achat_adah', 'shem_ha_shenit_tzilah', 'avi_yoshev_ohel_u_mikneh(yaval)', 'shem_achiv_yuval', 'avi_kol_tofes_kinor_ve_ugav(yuval)', 'lotesh_kol_choresh_nechoshet_u_varzel(tuval_kayin)', 'achot_tuval_kayin_naamah', 'ish_haragti_le_fitzi_ve_yeled_le_chaburati', 'shat_li_elohim_zera_acher_tachat_hevel', 'harago_kayin_named_in_speech', 'huchal_likro_be_shem_YHWH'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 15
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
