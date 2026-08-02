#!/usr/bin/env python3
# =============================================================================
# gen_17_boarding — 7:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_17_boarding.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The boarding: you have I seen righteous, the date, the shut door (7:1-16)"""
from machine import Machine

m = Machine("gen_17_boarding")

# -------------------------- Gen.7.1 · COME_COMMAND_SECOND_PERSON_VERDICT ---
# va-yomer YHWH le-Noach bo-atah ve-khol-beitkha el-ha-tevah ki-otkha raiti
# tzaddik lefanai ba-dor ha-zeh
# "And the LORD said unto Noah: 'Come thou and all thy house into the ark;
# for thee have I seen righteous before Me in this generation.'"
m.step("Gen.7.1")
m.declare("YHWH", "LET",
          "bo(noach, el_ha_tevah)")
m.test("PASS", "tzaddik", "noach")
m.presupposed("noach", "tevah")

# -------------------------- Gen.7.2 · CLEAN_SEVENS_AMENDMENT ---------------
# mi-kol ha-behemah ha-tehorah tiqach-lekha shivah shivah ish ve-ishto
# u-min-ha-behemah asher lo tehorah hi shnayim ish ve-ishto
# "Of every clean beast thou shalt take to thee seven and seven, each with
# his mate; and of the beasts that are not clean two and two, each with his
# mate;"
m.step("Gen.7.2")
m.fact("shivah_shivah_ha_behemah_ha_tehorah",
       "shnayim_asher_lo_tehorah")

# -------------------------- Gen.7.3 · BIRDS_AND_THE_SEED_PURPOSE -----------
# gam me-of ha-shamayim shivah shivah zakhar u-nekevah le-chayot zera al-
# pnei khol-ha-aretz
# "of the fowl also of the air, seven and seven, male and female; to keep
# seed alive upon the face of all the earth."
m.step("Gen.7.3")
m.fact("le_chayot_zera_al_pnei_khol_ha_aretz")

# -------------------------- Gen.7.4 · COUNTDOWN_STACK_WIPE_SCHEDULED -------
# ki le-yamim od shivah anokhi mamtir al-ha-aretz arbaim yom ve-arbaim
# laylah u-machiti et-kol-ha-yequm asher asiti me-al pnei ha-adamah
# "For yet seven days, and I will cause it to rain upon the earth forty days
# and forty nights; and every living substance that I have made will I blot
# out from off the face of the earth.'"
m.step("Gen.7.4")
m.fact("od_shivat_yamim_anokhi_mamtir",
       "u_machiti_et_kol_ha_yequm")

# -------------------------- Gen.7.5 · REFRAIN_TWO --------------------------
# va-yaas Noach ke-khol asher-tzivahu YHWH
# "And Noah did according unto all that the LORD commanded him."
m.step("Gen.7.5")
m.fact("ke_khol_asher_tzivahu_YHWH")

# -------------------------- Gen.7.6 · AGE_AT_THE_FLOOD ---------------------
# ve-Noach ben-shesh meot shanah ve-ha-mabul hayah mayim al-ha-aretz
# "And Noah was six hundred years old when the flood of waters was upon the
# earth."
m.step("Gen.7.6")
m.fact("noach_ben_shesh_meot_shanah")

# -------------------------- Gen.7.7 · THE_ENTRY_DEMAND_POPPED --------------
# va-yavo Noach u-vanav ve-ishto u-neshei-vanav ito el-ha-tevah mi-pnei mei
# ha-mabul
# "And Noah went in, and his sons, and his wife, and his sons' wives with
# him, into the ark, because of the waters of the flood."
m.step("Gen.7.7")
m.event("come", agent="noach", themes=["el_ha_tevah"])
m.result("bo(noach, el_ha_tevah)", tmark="t1")

# -------------------------- Gen.7.8 · THE_CARGO_CLASSES --------------------
# min-ha-behemah ha-tehorah u-min-ha-behemah asher einenah tehorah u-min-ha-
# of ve-khol asher-romes al-ha-adamah
# "Of clean beasts, and of beasts that are not clean, and of fowls, and of
# every thing that creepeth upon the ground,"
m.step("Gen.7.8")
m.fact("ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes")

# -------------------------- Gen.7.9 · SELF_LOADING_REFRAIN_THREE -----------
# shnayim shnayim bau el-Noach el-ha-tevah zakhar u-nekevah ka-asher tzivah
# Elohim et-Noach
# "there went in two and two unto Noah into the ark, male and female, as God
# commanded Noah."
m.step("Gen.7.9")
m.fact("shnayim_shnayim_bau_el_noach",
       "ka_asher_tzivah_elohim_et_noach")

# -------------------------- Gen.7.10 · SEVEN_DAYS_ELAPSE -------------------
# va-yehi le-shivat ha-yamim u-mei ha-mabul hayu al-ha-aretz
# "And it came to pass after the seven days, that the waters of the flood
# were upon the earth."
m.step("Gen.7.10")
m.fact("le_shivat_ha_yamim_mei_ha_mabul")

# -------------------------- Gen.7.11 · THE_DATE_DOUBLE_BREACH --------------
# bi-shnat shesh-meot shanah le-chayei-Noach ba-chodesh ha-sheni be-shivah-
# asar yom la-chodesh ba-yom ha-zeh nivkeu kol-mayenot tehom rabbah va-
# arubot ha-shamayim niftachu
# "In the six hundredth year of Noah's life, in the second month, on the
# seventeenth day of the month, on the same day were all the fountains of
# the great deep broken up, and the windows of heaven were opened."
m.step("Gen.7.11")
m.time_anchor("shnat_600_chodesh_2_yom_17")
m.event("split", themes=["mayenot_tehom_rabbah"])
m.event("open", themes=["arubot_ha_shamayim"])

# -------------------------- Gen.7.12 · THE_RAIN_FORTY ----------------------
# va-yehi ha-geshem al-ha-aretz arbaim yom ve-arbaim laylah
# "And the rain was upon the earth forty days and forty nights."
m.step("Gen.7.12")
m.fact("ha_geshem_arbaim_yom_va_arbaim_laylah")

# -------------------------- Gen.7.13 · THE_SOLEMN_DAY_STAMP ----------------
# be-etzem ha-yom ha-zeh ba Noach ve-Shem-ve-Cham va-Yefet bnei-Noach ve-
# eshet Noach u-shloshet neshei-vanav itam el-ha-tevah
# "In the selfsame day entered Noah, and Shem, and Ham, and Japheth, the
# sons of Noah, and Noah's wife, and the three wives of his sons with them,
# into the ark;"
m.step("Gen.7.13")
m.fact("be_etzem_ha_yom_ha_zeh_ba_noach")

# -------------------------- Gen.7.14 · FULL_TAXONOMY_EVERY_WING ------------
# hemah ve-khol-ha-chayah le-minah ve-khol-ha-behemah le-minah ve-khol-ha-
# remes ha-romes al-ha-aretz le-minehu ve-khol-ha-of le-minehu kol tzippor
# kol-kanaf
# "they, and every beast after its kind, and all the cattle after their
# kind, and every creeping thing that creepeth upon the earth after its
# kind, and every fowl after its kind, every bird of every sort."
m.step("Gen.7.14")
m.fact("kol_ha_chayah_le_minah_ha_of_le_minehu",
       "kol_tzippor_kol_kanaf")

# -------------------------- Gen.7.15 · THE_PAIRS_AND_THE_BREATH ------------
# va-yavou el-Noach el-ha-tevah shnayim shnayim mi-kol-ha-basar asher-bo
# ruach chayim
# "And they went in unto Noah into the ark, two and two of all flesh wherein
# is the breath of life."
m.step("Gen.7.15")
m.event("come", themes=["kol_basar_shnayim_shnayim"])

# -------------------------- Gen.7.16 · THE_SEAL_YHWH_SHUTS -----------------
# ve-ha-baim zakhar u-nekevah mi-kol-basar bau ka-asher tzivah oto Elohim
# va-yisgor YHWH baado
# "And they that went in, went in male and female of all flesh, as God
# commanded him; and the LORD shut him in."
m.step("Gen.7.16")
m.fact("ha_baim_zakhar_u_nekevah_bau",
       "ka_asher_tzivah_oto_elohim")
m.event("shut", agent="YHWH", themes=["baado"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'tevah', 'noach'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tzaddik', 'noach')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['shivah_shivah_ha_behemah_ha_tehorah', 'shnayim_asher_lo_tehorah', 'le_chayot_zera_al_pnei_khol_ha_aretz', 'od_shivat_yamim_anokhi_mamtir', 'u_machiti_et_kol_ha_yequm', 'ke_khol_asher_tzivahu_YHWH', 'noach_ben_shesh_meot_shanah', 'ha_tehorah_ve_einenah_tehorah_ve_ha_of_ve_ha_romes', 'shnayim_shnayim_bau_el_noach', 'ka_asher_tzivah_elohim_et_noach', 'le_shivat_ha_yamim_mei_ha_mabul', 'ha_geshem_arbaim_yom_va_arbaim_laylah', 'be_etzem_ha_yom_ha_zeh_ba_noach', 'kol_ha_chayah_le_minah_ha_of_le_minehu', 'kol_tzippor_kol_kanaf', 'ha_baim_zakhar_u_nekevah_bau', 'ka_asher_tzivah_oto_elohim'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 7
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
