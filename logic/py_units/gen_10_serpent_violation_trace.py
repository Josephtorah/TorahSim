#!/usr/bin/env python3
# =============================================================================
# gen_10_serpent_violation_trace — 3:1-13
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_10_serpent_violation_trace.yaml) is CANONICAL
# (Pre-Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""Eden III: the serpent, the misquoted rule, the eating, the interrogation (3:1-13)"""
from machine import Machine

m = Machine("gen_10_serpent_violation_trace")

# -------------------------- Gen.3.1 · SERPENT_ONSET_INVERTED_QUOTE ---------
# ve-ha-nachash hayah arum mi-kol chayat ha-sadeh asher asah YHWH Elohim va-
# yomer el-ha-ishah af ki-amar Elohim lo tokhlu mi-kol etz ha-gan
# "Now the serpent was more subtle than any beast of the field which the
# LORD God had made. And he said unto the woman: 'Yea, hath God said: Ye
# shall not eat of any tree of the garden?'"
m.step("Gen.3.1")
m.fact("arum(nachash)",
       "asah_YHWH_Elohim(nachash)")
m.presupposed("nachash", "ishah", "gan")
m.event("say", agent="nachash", themes=["ishah"])
m.spec_delta("akhol tokhel mi-kol etz ha-gan + one exclusion (gen_08 2:16-17: permission over ALL, prohibition on ONE)",
             "lo tokhlu mi-kol etz ha-gan (the serpent: negation over ALL — the scope INVERTED, and the addressee pluralized 2ms->2mp)")
m.spec_delta("YHWH_Elohim (the rule's issuer, gen_08 2:16 — the Eden-exclusive compound)",
             "Elohim (the serpent")

# -------------------------- Gen.3.2 · WOMAN_PERMISSION_REDUCED -------------
# va-tomer ha-ishah el-ha-nachash mi-peri etz-ha-gan nokhel
# "And the woman said unto the serpent: 'Of the fruit of the trees of the
# garden we may eat.'"
m.step("Gen.3.2")
m.event("say", agent="ishah", themes=["nachash"])
m.spec_delta("mi-KOL etz ha-gan AKHOL TOKHEL (gen_08 2:16: from ALL, with the emphatic doubling — the corpus first doubling)",
             "mi-peri etz-ha-gan nokhel (the woman: no mi-kol, no doubling — from the fruit of the garden trees we may eat)")

# -------------------------- Gen.3.3 · WOMAN_FENCE_AND_SOFTENED_PENALTY -----
# u-mi-peri ha-etz asher be-tokh-ha-gan amar Elohim lo tokhlu mimenu ve-lo
# tigu bo pen-temutun
# "'But of the fruit of the tree which is in the midst of the garden, God
# hath said: Ye shall not eat of it, neither shall ye touch it, lest ye
# die.'"
m.step("Gen.3.3")
m.presupposed("ha_etz")
m.spec_delta("me-etz ha-daat tov va-ra (gen_08 2:17: the tree named by its knowledge; located nowhere)",
             "ha-etz asher be-tokh ha-gan (the woman: the tree IN THE MIDST — the address 2:9 states for the tree of LIFE)")
m.spec_delta("lo tokhal mimenu (gen_08 2:17: eating prohibited — nothing else)",
             "lo tokhlu mimenu VE-LO TIGU BO (eating AND TOUCHING prohibited — a fence added to the rule)")
m.spec_delta("ki be-yom akholkha mimenu mot tamut (gen_08 2:17: certainty ON THE DAY, with the death-doubling)",
             "pen-temutun (the woman: LEST you die — risk for certainty, no doubling, no day-clock)")

# -------------------------- Gen.3.4 · SERPENT_CONTRADICTION ----------------
# va-yomer ha-nachash el-ha-ishah lo-mot temutun
# "And the serpent said unto the woman: 'Ye shall not surely die.'"
m.step("Gen.3.4")
m.event("say", agent="nachash", themes=["ishah"])
m.spec_delta("mot tamut (gen_08 2:17: the penalty, doubled — the emphatic device the woman had dropped)",
             "LO-mot temutun (the serpent: the doubling RESTORED in order to be NEGATED — the corpus first direct contradiction of a divine word)")

# -------------------------- Gen.3.5 · SERPENT_COUNTER_THEORY ---------------
# ki yodea Elohim ki be-yom akholkhem mimenu ve-nifqechu eineikhem vi-
# heyitem ke-Elohim yodei tov va-ra
# "'For God doth know that in the day ye eat thereof, then your eyes shall
# be opened, and ye shall be as God, knowing good and evil.'"
m.step("Gen.3.5")
m.event("claim", agent="nachash", themes=["nifqechu_eineikhem", "ke_Elohim"])

# -------------------------- Gen.3.6 · CREATURE_TEST_AND_TRIGGER ------------
# va-tere ha-ishah ki tov ha-etz le-maakhal ve-khi taavah-hu la-einayim ve-
# nechmad ha-etz le-haskil va-tiqach mi-piryo va-tokhal va-titen gam-le-
# ishah imah va-yokhal
# "And when the woman saw that the tree was good for food, and that it was a
# delight to the eyes, and that the tree was to be desired to make one wise,
# she took of the fruit thereof, and did eat; and she gave also unto her
# husband with her, and he did eat."
m.step("Gen.3.6")
m.test("PASS", "tov", "ha_etz_le_maakhal")
m.event("take", agent="ishah", themes=["pri"])
m.event("eat", agent="ishah", themes=["pri"])
m.event("give", agent="ishah", themes=["adam"])
m.event("eat", agent="adam", themes=["pri"])
m.presupposed("adam")

# -------------------------- Gen.3.7 · EYES_OPEN_FIRST_MANUFACTURE ----------
# va-tipakachnah einei shneihem va-yedu ki eirummim hem va-yitperu aleh
# te'enah va-ya'asu lahem chagorot
# "And the eyes of them both were opened, and they knew that they were
# naked; and they sewed fig-leaves together, and made themselves girdles."
m.step("Gen.3.7")
m.event("open_eyes", themes=["einei_shneihem"])
m.event("know", agent="shneihem", themes=["eirummim"])
m.event("make", agent="shneihem", themes=["chagorot"])
m.install("chagorot")

# -------------------------- Gen.3.8 · VOICE_AND_HIDING ---------------------
# va-yishme'u et-qol YHWH Elohim mithalekh ba-gan le-ruach ha-yom va-
# yitchabe ha-adam ve-ishto mi-penei YHWH Elohim be-tokh etz ha-gan
# "And they heard the voice of the LORD God walking in the garden toward the
# cool of the day; and the man and his wife hid themselves from the presence
# of the LORD God amongst the trees of the garden."
m.step("Gen.3.8")
m.event("hear", agent="shneihem", themes=["qol_YHWH_Elohim"])
m.event("hide", agent="shneihem", themes=["be_tokh_etz_ha_gan"])

# -------------------------- Gen.3.9 · FIRST_QUESTION -----------------------
# va-yiqra YHWH Elohim el-ha-adam va-yomer lo ayeka
# "And the LORD God called unto the man, and said unto him: 'Where art
# thou?'"
m.step("Gen.3.9")
m.event("call", agent="YHWH_Elohim", themes=["adam"])
m.event("ask", agent="YHWH_Elohim", themes=["ayeka"])

# -------------------------- Gen.3.10 · TESTIMONY_FEAR ----------------------
# va-yomer et-qolkha shamati ba-gan va-ira ki-erom anokhi va-echave
# "And he said: 'I heard Thy voice in the garden, and I was afraid, because
# I was naked; and I hid myself.'"
m.step("Gen.3.10")
m.event("say", agent="adam", themes=["YHWH_Elohim"])
m.fact("testimony_feared_naked_hid(adam)")

# -------------------------- Gen.3.11 · RULE_QUOTED_BACK --------------------
# va-yomer mi higid lekha ki erom atah ha-min-ha-etz asher tzivitikha le-
# vilti akhol-mimenu akhalta
# "And He said: 'Who told thee that thou wast naked? Hast thou eaten of the
# tree, whereof I commanded thee that thou shouldest not eat?'"
m.step("Gen.3.11")
m.event("ask", agent="YHWH_Elohim", themes=["mi_higid", "akhalta"])

# -------------------------- Gen.3.12 · BLAME_CHAIN_ADMISSION_1 -------------
# va-yomer ha-adam ha-ishah asher natatah imadi hiv natnah-li min-ha-etz va-
# okhel
# "And the man said: 'The woman whom Thou gavest to be with me, she gave me
# of the tree, and I did eat.'"
m.step("Gen.3.12")
m.event("say", agent="adam", themes=["ishah"])
m.fact("admission_va_okhel(adam)")

# -------------------------- Gen.3.13 · ADMISSION_2_HAPAX_DECEIT ------------
# va-yomer YHWH Elohim la-ishah mah-zot asit va-tomer ha-ishah ha-nachash
# hishiani va-okhel
# "And the LORD God said unto the woman: 'What is this thou hast done?' And
# the woman said: 'The serpent beguiled me, and I did eat.'"
m.step("Gen.3.13")
m.event("ask", agent="YHWH_Elohim", themes=["ishah"])
m.event("say", agent="ishah", themes=["nachash"])
m.fact("admission_va_okhel(ishah)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'chagorot'}
    assert m.presupposed_set() == {'ishah', 'nachash', 'adam', 'gan', 'ha_etz'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'tov', 'ha_etz_le_maakhal')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5, 'spec_delta': 7}
    assert sorted(m.WORLD["facts"]) == sorted(['arum(nachash)', 'asah_YHWH_Elohim(nachash)', 'testimony_feared_naked_hid(adam)', 'admission_va_okhel(adam)', 'admission_va_okhel(ishah)'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 20
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
