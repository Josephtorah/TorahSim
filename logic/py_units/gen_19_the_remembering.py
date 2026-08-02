#!/usr/bin/env python3
# =============================================================================
# gen_19_the_remembering — 8:1-14
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_19_the_remembering.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The remembering: God remembers Noach, the waters go home, the earth dries (8:1-14)"""
from machine import Machine

m = Machine("gen_19_the_remembering")

# -------------------------- Gen.8.1 · THE_REMEMBERING_THE_WIND -------------
# va-yizkor Elohim et-Noach ve-et kol-ha-chayah ve-et-kol-ha-behemah asher
# ito ba-tevah va-yaaver Elohim ruach al-ha-aretz va-yashoku ha-mayim
# "And God remembered Noah, and every living thing, and all the cattle that
# were with him in the ark; and God made a wind to pass over the earth, and
# the waters assuaged;"
m.step("Gen.8.1")
m.event("remember", agent="elohim", themes=["noach", "kol_ha_chayah_ve_ha_behemah"])
m.event("pass", agent="elohim", themes=["ruach_al_ha_aretz"])
m.event("subside", themes=["ha_mayim"])
m.presupposed("noach", "tevah", "mayim")

# -------------------------- Gen.8.2 · THE_SHUT_MIRROR ----------------------
# va-yisakhru mayenot tehom va-arubot ha-shamayim va-yikkale ha-geshem min-
# ha-shamayim
# "the fountains also of the deep and the windows of heaven were stopped,
# and the rain from heaven was restrained."
m.step("Gen.8.2")
m.event("stop_up", themes=["mayenot_tehom_va_arubot_ha_shamayim"])
m.event("restrain", themes=["ha_geshem"])

# -------------------------- Gen.8.3 · THE_WATERS_COMMUTE_BRACKET_CLOSED ----
# va-yashuvu ha-mayim me-al ha-aretz halokh va-shov va-yachseru ha-mayim mi-
# qetzeh chamishim u-meat yom
# "And the waters returned from off the earth continually; and after the end
# of a hundred and fifty days the waters decreased."
m.step("Gen.8.3")
m.event("return", agent="ha_mayim")
m.fact("halokh_va_shov",
       "mi_qetze_chamishim_u_meat_yom")
m.event("diminish", themes=["ha_mayim"])

# -------------------------- Gen.8.4 · THE_ARK_RESTS ------------------------
# va-tanach ha-tevah ba-chodesh ha-shevii be-shivah-asar yom la-chodesh al
# harei Ararat
# "And the ark rested in the seventh month, on the seventeenth day of the
# month, upon the mountains of Ararat."
m.step("Gen.8.4")
m.event("rest", themes=["ha_tevah"])
m.fact("ba_chodesh_ha_shevii_be_shivah_asar_yom",
       "al_harei_ararat")

# -------------------------- Gen.8.5 · THE_TOPS_APPEAR ----------------------
# ve-ha-mayim hayu halokh ve-chasor ad ha-chodesh ha-asiri ba-asiri be-echad
# la-chodesh niru rashei he-harim
# "And the waters decreased continually until the tenth month; in the tenth
# month, on the first day of the month, were the tops of the mountains
# seen."
m.step("Gen.8.5")
m.fact("halokh_ve_chasor_ad_ha_chodesh_ha_asiri",
       "ba_asiri_be_echad_niru_rashei_he_harim")

# -------------------------- Gen.8.6 · THE_WINDOW_HE_MADE -------------------
# va-yehi mi-qetz arbaim yom va-yiftach Noach et-chalon ha-tevah asher asah
# "And it came to pass at the end of forty days, that Noah opened the window
# of the ark which he had made."
m.step("Gen.8.6")
m.fact("mi_qetz_arbaim_yom")
m.event("open", agent="noach", themes=["chalon_ha_tevah"])

# -------------------------- Gen.8.7 · THE_RAVEN ----------------------------
# va-yeshallach et-ha-orev va-yetze yatzo va-shov ad-yevoshet ha-mayim me-al
# ha-aretz
# "And he sent forth a raven, and it went forth to and fro, until the waters
# were dried up from off the earth."
m.step("Gen.8.7")
m.event("send", agent="noach", themes=["ha_orev"])
m.fact("yatzo_va_shov_ad_yevoshet_ha_mayim")

# -------------------------- Gen.8.8 · THE_DOVE_THE_QUESTION ----------------
# va-yeshallach et-ha-yonah me-ito li-reot ha-qalu ha-mayim me-al pnei ha-
# adamah
# "And he sent forth a dove from him, to see if the waters were abated from
# off the face of the ground."
m.step("Gen.8.8")
m.event("send", agent="noach", themes=["ha_yonah"])
m.fact("li_reot_ha_qalu_ha_mayim")

# -------------------------- Gen.8.9 · NO_RESTING_PLACE_THE_HAND ------------
# ve-lo-matzah ha-yonah manoach le-khaf-raglah va-tashav elav el-ha-tevah
# ki-mayim al-pnei khol-ha-aretz va-yishlach yado va-yikkacheha va-yave otah
# elav el-ha-tevah
# "But the dove found no rest for the sole of her foot, and she returned
# unto him to the ark, for the waters were on the face of the whole earth;
# and he put forth his hand, and took her, and brought her in unto him into
# the ark."
m.step("Gen.8.9")
m.fact("lo_matzah_ha_yonah_manoach_le_khaf_raglah",
       "ki_mayim_al_pnei_khol_ha_aretz")
m.event("return", agent="ha_yonah")
m.event("send", agent="noach", themes=["yado"])
m.event("take", agent="noach", themes=["ha_yonah"])
m.event("bring", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.10 · THE_FIRST_WAIT ----------------------
# va-yachel od shivat yamim acherim va-yosef shallach et-ha-yonah min-ha-
# tevah
# "And he stayed yet other seven days; and again he sent forth the dove out
# of the ark."
m.step("Gen.8.10")
m.event("wait", agent="noach")
m.fact("od_shivat_yamim_acherim")
m.event("send", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.11 · THE_LEAF_AT_EVENING -----------------
# va-tavo elav ha-yonah le-et erev ve-hinneh aleh-zayit taraf be-fiha va-
# yeda Noach ki-qalu ha-mayim me-al ha-aretz
# "And the dove came in to him at eventide; and lo in her mouth an olive-
# leaf freshly plucked; so Noah knew that the waters were abated from off
# the earth."
m.step("Gen.8.11")
m.event("come", agent="ha_yonah", themes=["le_et_erev"])
m.fact("aleh_zayit_taraf_be_fiha")
m.event("know", agent="noach", themes=["ki_qalu_ha_mayim"])

# -------------------------- Gen.8.12 · THE_SECOND_WAIT_THE_LAST_OD ---------
# va-yiyachel od shivat yamim acherim va-yeshallach et-ha-yonah ve-lo-yasfah
# shuv-elav od
# "And he stayed yet other seven days; and sent forth the dove; and she
# returned not again unto him any more."
m.step("Gen.8.12")
m.event("wait", agent="noach")
m.event("send", agent="noach", themes=["ha_yonah"])
m.fact("ve_lo_yasfah_shuv_elav_od")

# -------------------------- Gen.8.13 · NEW_YEARS_DAY_THE_COVER_OFF ---------
# va-yehi be-achat ve-shesh-meot shanah ba-rishon be-echad la-chodesh charvu
# ha-mayim me-al ha-aretz va-yasar Noach et-mikhseh ha-tevah va-yar ve-
# hinneh charvu pnei ha-adamah
# "And it came to pass in the six hundred and first year, in the first
# month, the first day of the month, the waters were dried up from off the
# earth; and Noah removed the covering of the ark, and looked, and behold,
# the face of the ground was dried."
m.step("Gen.8.13")
m.time_anchor("shnat_601_chodesh_1_yom_1")
m.fact("charvu_ha_mayim_me_al_ha_aretz")
m.event("remove", agent="noach", themes=["mikhseh_ha_tevah"])
m.event("see", agent="noach", themes=["pnei_ha_adamah"])
m.fact("ve_hinneh_charvu_pnei_ha_adamah")

# -------------------------- Gen.8.14 · THE_EARTH_DRY -----------------------
# u-va-chodesh ha-sheni be-shivah ve-esrim yom la-chodesh yavshah ha-aretz
# "And in the second month, on the seven and twentieth day of the month, was
# the earth dry."
m.step("Gen.8.14")
m.fact("ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom",
       "yavshah_ha_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'mayim', 'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['halokh_va_shov', 'mi_qetze_chamishim_u_meat_yom', 'ba_chodesh_ha_shevii_be_shivah_asar_yom', 'al_harei_ararat', 'halokh_ve_chasor_ad_ha_chodesh_ha_asiri', 'ba_asiri_be_echad_niru_rashei_he_harim', 'mi_qetz_arbaim_yom', 'yatzo_va_shov_ad_yevoshet_ha_mayim', 'li_reot_ha_qalu_ha_mayim', 'lo_matzah_ha_yonah_manoach_le_khaf_raglah', 'ki_mayim_al_pnei_khol_ha_aretz', 'od_shivat_yamim_acherim', 'aleh_zayit_taraf_be_fiha', 've_lo_yasfah_shuv_elav_od', 'charvu_ha_mayim_me_al_ha_aretz', 've_hinneh_charvu_pnei_ha_adamah', 'ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom', 'yavshah_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
