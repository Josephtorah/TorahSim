#!/usr/bin/env python3
# =============================================================================
# gen_12_cain_abel — 4:1-16
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_12_cain_abel.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Cain and Abel: first offerings, sin at the door, first murder, the mark (4:1-16)"""
from machine import Machine

m = Machine("gen_12_cain_abel")

# -------------------------- Gen.4.1 · FIRST_BIRTH_NAME_SPEECH --------------
# ve-ha-adam yada et-Chavah ishto va-tahar va-teled et-Kayin va-tomer kaniti
# ish et-YHWH
# "And the man knew Eve his wife; and she conceived and bore Cain, and said:
# 'I have gotten a man with the help of the LORD.'"
m.step("Gen.4.1")
m.event("know", agent="adam", themes=["chavah"])
m.event("bear", agent="chavah", themes=["kayin"])
m.name("kayin", "Kayin")
m.presupposed("adam", "chavah")

# -------------------------- Gen.4.2 · SECOND_BIRTH_PROFESSIONS -------------
# va-tosef la-ledet et-achiv et-Havel va-yehi-Hevel ro'eh tzon ve-Kayin
# hayah oved adamah
# "And again she bore his brother Abel. And Abel was a keeper of sheep, but
# Cain was a tiller of the ground."
m.step("Gen.4.2")
m.event("bear", agent="chavah", themes=["hevel"])
m.fact("roeh_tzon(hevel)",
       "oved_adamah(kayin)")
m.presupposed("adamah")

# -------------------------- Gen.4.3 · FIRST_OFFERING -----------------------
# va-yehi mi-ketz yamim va-yave Kayin mi-peri ha-adamah minchah la-YHWH
# "And in process of time it came to pass, that Cain brought of the fruit of
# the ground an offering unto the LORD."
m.step("Gen.4.3")
m.event("bring", agent="kayin", themes=["minchah"])

# -------------------------- Gen.4.4 · SECOND_OFFERING_FAVOR ----------------
# ve-Hevel hevi gam-hu mi-bekhorot tzono u-me-chelvehen va-yisha YHWH el-
# Hevel ve-el-minchato
# "And Abel, he also brought of the firstlings of his flock and of the fat
# thereof. And the LORD had respect unto Abel and to his offering."
m.step("Gen.4.4")
m.event("bring", agent="hevel", themes=["bekhorot"])
m.test("PASS", "shaah", "hevel_u_minchato")

# -------------------------- Gen.4.5 · NON_REGARD_FIRST_ANGER ---------------
# ve-el-Kayin ve-el-minchato lo sha'ah va-yichar le-Kayin me'od va-yiplu
# panav
# "But unto Cain and to his offering He had not respect. And Cain was very
# wroth, and his countenance fell."
m.step("Gen.4.5")
m.fact("lo_shaah_el_kayin_ve_el_minchato")
m.event("burn", agent="kayin")

# -------------------------- Gen.4.6 · ANGER_DIAGNOSTIC ---------------------
# va-yomer YHWH el-Kayin lamah charah lakh ve-lamah naflu fanekha
# "And the LORD said unto Cain: 'Why art thou wroth? and why is thy
# countenance fallen?'"
m.step("Gen.4.6")
m.event("ask", agent="YHWH", themes=["kayin"])

# -------------------------- Gen.4.7 · COUNSEL_FIRST_IF ---------------------
# halo im-teitiv se'et ve-im lo teitiv la-petach chattat rovetz ve-elekha
# teshukato ve-atah timshol-bo
# "'If thou doest well, shall it not be lifted up? and if thou doest not
# well, sin coucheth at the door; and unto thee is its desire, but thou
# mayest rule over it.'"
m.step("Gen.4.7")
m.handler("teitiv(kayin)",
          "seet")
m.handler("lo_teitiv(kayin)",
          "la_petach_chattat_rovetz")
m.declare("YHWH", "LET?",
          "timshol(kayin, ba_chattat)")

# -------------------------- Gen.4.8 · EMPTY_QUOTE_FIRST_MURDER -------------
# va-yomer Kayin el-Hevel achiv va-yehi bihyotam ba-sadeh va-yakom Kayin el-
# Hevel achiv va-yahargehu
# "And Cain spoke unto Abel his brother. And it came to pass, when they were
# in the field, that Cain rose up against Abel his brother, and slew him."
m.step("Gen.4.8")
m.event("say", agent="kayin", themes=["hevel"])
m.event("kill", agent="kayin", themes=["hevel"])

# -------------------------- Gen.4.9 · DOCKET_FIRST_LIE ---------------------
# va-yomer YHWH el-Kayin ei Hevel achikha va-yomer lo yadati ha-shomer achi
# anokhi
# "And the LORD said unto Cain: 'Where is Abel thy brother?' And he said: 'I
# know not; am I my brother's keeper?'"
m.step("Gen.4.9")
m.event("ask", agent="YHWH", themes=["kayin"])
m.fact("lo_yadati_ha_shomer_achi_anokhi(kayin)")

# -------------------------- Gen.4.10 · BLOODS_CRY --------------------------
# va-yomer meh asita kol demei achikha tzo'akim elai min-ha-adamah
# "And He said: 'What hast thou done? the voice of thy brother's blood
# crieth unto Me from the ground.'"
m.step("Gen.4.10")
m.event("ask", agent="YHWH", themes=["kayin"])
m.fact("kol_demei_achikha_tzoakim_min_ha_adamah")

# -------------------------- Gen.4.11 · CURSE_REACHES_HUMAN -----------------
# ve-atah arur atah min-ha-adamah asher patztah et-piha lakachat et-demei
# achikha mi-yadekha
# "'And now cursed art thou from the ground, which hath opened her mouth to
# receive thy brother's blood from thy hand.'"
m.step("Gen.4.11")
m.assign("kayin", "arur_min_ha_adamah")
m.fact("ha_adamah_patztah_piha_lakachat_demei(kayin)")

# -------------------------- Gen.4.12 · GROUND_STRIKE_WANDERER --------------
# ki ta'avod et-ha-adamah lo-tosef tet-kochah lakh na va-nad tihyeh va-aretz
# "'When thou tillest the ground, it shall not henceforth yield unto thee
# her strength; a fugitive and a wanderer shalt thou be in the earth.'"
m.step("Gen.4.12")
m.fact("ki_taavod_lo_tosef_tet_kochah(adamah, kayin)",
       "na_va_nad_tihyeh(kayin)")

# -------------------------- Gen.4.13 · PLEA_UNBEARABLE ---------------------
# va-yomer Kayin el-YHWH gadol avoni mi-neso
# "And Cain said unto the LORD: 'My punishment is greater than I can bear.'"
m.step("Gen.4.13")
m.event("plead", agent="kayin", themes=["YHWH"])

# -------------------------- Gen.4.14 · FEAR_OF_FINDERS ---------------------
# hen gerashta oti ha-yom me'al pnei ha-adamah u-mi-panekha esater ve-hayiti
# na va-nad ba-aretz ve-hayah khol-motzi yahargeni
# "'Behold, Thou hast driven me out this day from the face of the land; and
# from Thy face shall I be hid; and I shall be a fugitive and a wanderer in
# the earth; and it will come to pass, that whosoever findeth me will slay
# me.'"
m.step("Gen.4.14")
m.fact("gerashta_oti_u_mi_panekha_esater(kayin)",
       "khol_motzi_yahargeni_fear(kayin)")

# -------------------------- Gen.4.15 · SEVENFOLD_HANDLER_MARK --------------
# va-yomer lo YHWH lakhen kol-horeg Kayin shivatayim yukam va-yasem YHWH le-
# Kayin ot le-vilti hakot-oto kol-motz'o
# "And the LORD said unto him: 'Therefore whosoever slayeth Cain, vengeance
# shall be taken on him sevenfold.' And the LORD set a sign for Cain, lest
# any finding him should smite him."
m.step("Gen.4.15")
m.handler("horeg(kayin)",
          "shivatayim_yukam")
m.fact("ot_le_kayin_levilti_hakot(kayin)")

# -------------------------- Gen.4.16 · EXIT_EAST_SETTLED_IN_WANDERING ------
# va-yetze Kayin mi-lifnei YHWH va-yeshev be-eretz-Nod kidmat-Eden
# "And Cain went out from the presence of the LORD, and dwelt in the land of
# Nod, on the east of Eden."
m.step("Gen.4.16")
m.event("go_out", agent="kayin", themes=["eretz_nod_kidmat_eden"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam', 'chavah', 'adamah'}
    assert m.REGISTRY["names"] == {'kayin': 'arur_min_ha_adamah'}
    assert m.REGISTRY["writes"] == 2
    assert m.tests_list() == [('PASS', 'shaah', 'hevel_u_minchato')]
    assert m.open_demands() == ['timshol(kayin, ba_chattat)']
    assert len(m.SPECS["log"]) == 1
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'named_before_any_presence': 1, 'read_before_install': 3, 'assigned_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['roeh_tzon(hevel)', 'oved_adamah(kayin)', 'lo_shaah_el_kayin_ve_el_minchato', 'handler: IF(teitiv(kayin)) THEN(seet)', 'handler: IF(lo_teitiv(kayin)) THEN(la_petach_chattat_rovetz)', 'lo_yadati_ha_shomer_achi_anokhi(kayin)', 'kol_demei_achikha_tzoakim_min_ha_adamah', 'ha_adamah_patztah_piha_lakachat_demei(kayin)', 'ki_taavod_lo_tosef_tet_kochah(adamah, kayin)', 'na_va_nad_tihyeh(kayin)', 'gerashta_oti_u_mi_panekha_esater(kayin)', 'khol_motzi_yahargeni_fear(kayin)', 'handler: IF(horeg(kayin)) THEN(shivatayim_yukam)', 'ot_le_kayin_levilti_hakot(kayin)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 19
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
