#!/usr/bin/env python3
# =============================================================================
# gen_11_sentences_exile — 3:14-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_11_sentences_exile.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden IV: the sentences, the skin garments, the exile (3:14-24)"""
from machine import Machine

m = Machine("gen_11_sentences_exile")

# -------------------------- Gen.3.14 · SENTENCE_SERPENT_FIRST_CURSE --------
# va-yomer YHWH Elohim el-ha-nachash ki asita zot arur atah mi-kol-ha-
# behemah u-mi-kol chayat ha-sadeh al-gechonkha telekh ve-afar tokhal kol-
# yemei chayekha
# "And the LORD God said unto the serpent: 'Because thou hast done this,
# cursed art thou from among all cattle, and from among all beasts of the
# field; upon thy belly shalt thou go, and dust shalt thou eat all the days
# of thy life.'"
m.step("Gen.3.14")
m.event("sentence", agent="YHWH_Elohim", themes=["nachash"])
m.presupposed("nachash")
m.assign("nachash", "arur_mi_kol_ha_behemah")
m.fact("al_gechonkha_telekh(nachash)",
       "afar_tokhal_kol_yemei_chayekha(nachash)")

# -------------------------- Gen.3.15 · ENMITY_PROGRAM ----------------------
# ve-eivah ashit beinkha u-vein ha-ishah u-vein zarakha u-vein zarah hu
# yeshufkha rosh ve-atah teshufenu akev
# "'And I will put enmity between thee and the woman, and between thy seed
# and her seed; they shall bruise thy head, and thou shalt bruise their
# heel.'"
m.step("Gen.3.15")
m.pattern("eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev")

# -------------------------- Gen.3.16 · SENTENCE_WOMAN ----------------------
# el-ha-ishah amar harbah arbeh itzvonekh ve-heronekh be-etzev teldi vanim
# ve-el-ishekh teshukatekh ve-hu yimshol-bakh
# "Unto the woman He said: 'I will greatly multiply thy pain and thy
# travail; in pain thou shalt bring forth children; and thy desire shall be
# to thy husband, and he shall rule over thee.'"
m.step("Gen.3.16")
m.presupposed("ishah")
m.fact("harbah_arbeh_itzvonekh_ve_heronekh(ishah)",
       "be_etzev_teldi_vanim(ishah)",
       "el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)")

# -------------------------- Gen.3.17 · SENTENCE_MAN_GROUND_CURSED ----------
# u-le-adam amar ki-shamata le-qol ishtekha va-tokhal min-ha-etz asher
# tzivitikha lemor lo tokhal mimenu arurah ha-adamah ba-avurekha be-itzavon
# tokhalenah kol yemei chayekha
# "And unto Adam He said: 'Because thou hast hearkened unto the voice of thy
# wife, and hast eaten of the tree, of which I commanded thee, saying: Thou
# shalt not eat of it; cursed is the ground for thy sake; in toil shalt thou
# eat of it all the days of thy life.'"
m.step("Gen.3.17")
m.event("sentence", agent="YHWH_Elohim", themes=["adam"])
m.presupposed("adam", "adamah")
m.assign("adamah", "arurah_baavurekha")
m.fact("be_itzavon_tokhalenah_kol_yemei_chayekha(adam)")

# -------------------------- Gen.3.18 · THORN_DIET --------------------------
# ve-kotz ve-dardar tatzmiach lakh ve-akhalta et-esev ha-sadeh
# "'Thorns also and thistles shall it bring forth to thee; and thou shalt
# eat the herb of the field.'"
m.step("Gen.3.18")
m.fact("kotz_ve_dardar_tatzmiach_lakh(adamah)",
       "ve_akhalta_et_esev_ha_sadeh(adam)")

# -------------------------- Gen.3.19 · MORTALITY_BOUNDARY ------------------
# be-zeat apekha tokhal lechem ad shuvkha el-ha-adamah ki mimenah lukachta
# ki-afar atah ve-el-afar tashuv
# "'In the sweat of thy face shalt thou eat bread, till thou return unto the
# ground; for out of it wast thou taken; for dust thou art, and unto dust
# shalt thou return.'"
m.step("Gen.3.19")
m.fact("be_zeat_apekha_tokhal_lechem(adam)",
       "ad_shuvkha_el_ha_adamah(adam)",
       "afar_atah_ve_el_afar_tashuv(adam)")
m.spec_delta("ki be-yom akholkha mimenu mot tamut (gen_08 2:17 — the armed HANDLER: dying-you-shall-die, IN THE DAY)",
             "ad shuvkha el-ha-adamah … ve-el-afar tashuv (the sentence: toil-terms + mortality as BOUNDARY — the return to dust as horizon; same-day death not executed)")

# -------------------------- Gen.3.20 · NAME_CHAVAH -------------------------
# va-yiqra ha-adam shem ishto Chavah ki hiv haytah em kol-chai
# "And the man called his wife's name Eve; because she was the mother of all
# living."
m.step("Gen.3.20")
m.name("ishah", "Chavah")

# -------------------------- Gen.3.21 · SKIN_GARMENTS -----------------------
# va-yaas YHWH Elohim le-adam u-le-ishto kotnot or va-yalbishem
# "And the LORD God made for Adam and for his wife garments of skins, and
# clothed them."
m.step("Gen.3.21")
m.event("make", agent="YHWH_Elohim", themes=["kotnot_or"])
m.event("clothe", agent="YHWH_Elohim", themes=["adam"])
m.install("kotnot_or")

# -------------------------- Gen.3.22 · COUNCIL_CONCERN_SECOND_TREE ---------
# va-yomer YHWH Elohim hen ha-adam hayah ke-achad mimenu la-daat tov va-ra
# ve-atah pen-yishlach yado ve-lakach gam me-etz ha-chayim ve-akhal va-chai
# le-olam
# "And the LORD God said: 'Behold, the man is become as one of us, to know
# good and evil; and now, lest he put forth his hand, and take also of the
# tree of life, and eat, and live for ever.'"
m.step("Gen.3.22")
m.event("deliberate", agent="YHWH_Elohim", themes=["adam"])
m.fact("ke_achad_mimenu_la_daat_tov_va_ra(adam)",
       "pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam")
m.presupposed("etz_ha_chayim", "gan")

# -------------------------- Gen.3.23 · EXPULSION_WORK_HALF -----------------
# va-yeshallechehu YHWH Elohim mi-gan-eden la-avod et-ha-adamah asher lukach
# mi-sham
# "Therefore the LORD God sent him forth from the garden of Eden, to till
# the ground from whence he was taken."
m.step("Gen.3.23")
m.event("send_out", agent="YHWH_Elohim", themes=["adam"])

# -------------------------- Gen.3.24 · GUARDS_INSTALLED_WAY_KEPT -----------
# va-yegaresh et-ha-adam va-yashken mi-qedem le-gan-eden et-ha-keruvim ve-et
# lahat ha-cherev ha-mithapekhet li-shmor et-derekh etz ha-chayim
# "So He drove out the man; and He placed at the east of the garden of Eden
# the cherubim, and the flaming sword which turned every way, to keep the
# way to the tree of life."
m.step("Gen.3.24")
m.event("drive_out", agent="YHWH_Elohim", themes=["adam"])
m.event("station", agent="YHWH_Elohim", themes=["keruvim"])
m.install("keruvim", "lahat_ha_cherev")
m.assign("keruvim", "shomer_derekh_etz_ha_chayim")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'keruvim', 'kotnot_or', 'lahat_ha_cherev'}
    assert m.presupposed_set() == {'ishah', 'nachash', 'adam', 'gan', 'etz_ha_chayim', 'adamah'}
    assert m.REGISTRY["names"] == {'nachash': 'arur_mi_kol_ha_behemah', 'adamah': 'arurah_baavurekha', 'ishah': 'Chavah', 'keruvim': 'shomer_derekh_etz_ha_chayim'}
    assert m.REGISTRY["writes"] == 4
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6, 'spec_delta': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['al_gechonkha_telekh(nachash)', 'afar_tokhal_kol_yemei_chayekha(nachash)', 'pattern: eivah(bein_zera_ha_ishah, bein_zera_ha_nachash) ∧ hu_yeshufkha_rosh ∧ atah_teshufenu_akev', 'harbah_arbeh_itzvonekh_ve_heronekh(ishah)', 'be_etzev_teldi_vanim(ishah)', 'el_ishekh_teshukatekh_ve_hu_yimshol_bakh(ishah)', 'be_itzavon_tokhalenah_kol_yemei_chayekha(adam)', 'kotz_ve_dardar_tatzmiach_lakh(adamah)', 've_akhalta_et_esev_ha_sadeh(adam)', 'be_zeat_apekha_tokhal_lechem(adam)', 'ad_shuvkha_el_ha_adamah(adam)', 'afar_atah_ve_el_afar_tashuv(adam)', 'ke_achad_mimenu_la_daat_tov_va_ra(adam)', 'pen_yishlach_yado_ve_lakach_me_etz_ha_chayim_va_chai_le_olam'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 13
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
