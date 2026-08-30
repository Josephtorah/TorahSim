#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_18_the_rise — 7:17-24
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_18_the_rise.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The rise: the waters lift the ark, all flesh dies, only Noach is left (7:17-24)"""
from machine import Machine

m = Machine("gen_18_the_rise")

# -------------------------- Gen.7.17 · THE_LIFT_AND_THE_RISE ---------------
# וַיְהִי הַמַּבּוּל אַרְבָּעִים יוֹם עַל־הָאָרֶץ וַיִּרְבּוּ הַמַּיִם
# וַיִּשְׂאוּ אֶת־הַתֵּבָה וַתָּרָם מֵעַל הָאָרֶץ
# "And the flood was forty days upon the earth; and the waters increased,
# and bore up the ark, and it was lifted up above the earth."
m.step("Gen.7.17")
# ‹וַיְהִי הַמַּבּוּל אַרְבָּעִים יוֹם עַל־הָאָרֶץ› (“and-be the-deluge
# forty day over the-earth”) — fact holds: the-deluge-forty-day-over-the-
# earth
m.fact("ha_mabul_arbaim_yom_al_ha_aretz")
# ‹וַיִּרְבּוּ הַמַּיִם וַיִּשְׂאוּ אֶת־הַתֵּבָה› (“and-increased the-waters
# and-they-lifted obj-marker the-ark”) — event: lift — agent the-waters;
# theme the-ark
m.event("lift", agent="ha_mayim", themes=["ha_tevah"])
# ‹וַתָּרָם מֵעַל הָאָרֶץ› (“and-it-rose from-over the-earth”) — event: rise
# — theme the-ark
m.event("rise", themes=["ha_tevah"])
# reads without prior install (flag, not fix): ark, waters
m.presupposed("tevah", "mayim")

# -------------------------- Gen.7.18 · THE_PREVAIL_DEBUT_THE_ARK_WALKS -----
# וַיִּגְבְּרוּ הַמַּיִם וַיִּרְבּוּ מְאֹד עַל־הָאָרֶץ וַתֵּלֶךְ הַתֵּבָה
# עַל־פְּנֵי הַמָּיִם
# "And the waters prevailed, and increased greatly upon the earth; and the
# ark went upon the face of the waters."
m.step("Gen.7.18")
# ‹וַיִּגְבְּרוּ הַמַּיִם› (“and-prevailed the-waters”) — event: prevail —
# agent the-waters
m.event("prevail", agent="ha_mayim")
# ‹וַיִּרְבּוּ מְאֹד עַל־הָאָרֶץ› (“and-increased very over the-earth”) —
# fact holds: and-increased-very-over-the-earth
m.fact("va_yirbu_meod_al_ha_aretz")
# ‹וַתֵּלֶךְ הַתֵּבָה עַל־פְּנֵי הַמָּיִם› (“and-it-walked the-ark over
# face-of the-waters”) — event: walk — agent the-ark; theme over-face-of-
# the-waters
m.event("walk", agent="ha_tevah", themes=["al_pnei_ha_mayim"])

# -------------------------- Gen.7.19 · THE_MOUNTAINS_GO_UNDER --------------
# וְהַמַּיִם גָּבְרוּ מְאֹד מְאֹד עַל־הָאָרֶץ וַיְכֻסּוּ כָּל־הֶהָרִים
# הַגְּבֹהִים אֲשֶׁר־תַּחַת כָּל־הַשָּׁמָיִם
# "And the waters prevailed exceedingly upon the earth; and all the high
# mountains that were under the whole heaven were covered."
m.step("Gen.7.19")
# ‹גָּבְרוּ מְאֹד מְאֹד … כָּל־הֶהָרִים הַגְּבֹהִים אֲשֶׁר־תַּחַת
# כָּל־הַשָּׁמָיִם› (“prevailed very very … all the-mountains the-high which
# under all the-heavens”) — fact holds: prevailed-very-very-over-the-earth;
# all-he-mountains-the-high-under-all-the-heavens
m.fact("gavru_meod_meod_al_ha_aretz",
       "kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim")
# ‹וַיְכֻסּוּ כָּל־הֶהָרִים הַגְּבֹהִים› (“and-were-covered all the-
# mountains the-high”) — event: cover — theme all-he-mountains-the-high
m.event("cover", themes=["kol_he_harim_ha_gevohim"])
# witness-tier presupposed read: territorial_claim_defeated on
# all_mountains_quantifier — read, not installed
m.witness_read("all_mountains_quantifier", "territorial_claim_defeated",
                cites=["Bereshit Rabbah 32:10"])

# -------------------------- Gen.7.20 · FIFTEEN_CUBITS_UPWARD ---------------
# חֲמֵשׁ עֶשְׂרֵה אַמָּה מִלְמַעְלָה גָּבְרוּ הַמָּיִם וַיְכֻסּוּ הֶהָרִים
# "Fifteen cubits upward did the waters prevail; and the mountains were
# covered."
m.step("Gen.7.20")
# ‹חֲמֵשׁ עֶשְׂרֵה אַמָּה מִלְמַעְלָה גָּבְרוּ הַמָּיִם› (“five teen cubit
# upward prevailed the-waters”) — fact holds: five--teen-cubit-from-upward-
# prevailed
m.fact("chamesh_esreh_amah_mi_lemalah_gavru")
# ‹וַיְכֻסּוּ הֶהָרִים› (“and-were-covered the-mountains”) — event: cover —
# theme mountains
m.event("cover", themes=["he_harim"])

# -------------------------- Gen.7.21 · ALL_FLESH_EXPIRES -------------------
# וַיִּגְוַע כָּל־בָּשָׂר הָרֹמֵשׂ עַל־הָאָרֶץ בָּעוֹף וּבַבְּהֵמָה
# וּבַחַיָּה וּבְכָל־הַשֶּׁרֶץ הַשֹּׁרֵץ עַל־הָאָרֶץ וְכֹל הָאָדָם
# "And all flesh perished that moved upon the earth, both fowl, and cattle,
# and beast, and every swarming thing that swarmeth upon the earth, and
# every man;"
m.step("Gen.7.21")
# ‹וַיִּגְוַע כָּל־בָּשָׂר› (“and-expired all flesh”) — event: expire —
# theme all-flesh
m.event("expire", themes=["kol_basar"])
# ‹בָּעוֹף וּבַבְּהֵמָה וּבַחַיָּה וּבְכָל־הַשֶּׁרֶץ … וְכֹל הָאָדָם› (“in-
# flying-creature and-in-livestock and-in-beast and-in-all the-swarming-
# creature … and-all the-human”) — fact holds: in-the-flying-creature-and-
# and-livestock-and-and-beast-and-and-swarming-creature-and-all-the-human
m.fact("ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam")

# -------------------------- Gen.7.22 · THE_COMPOUNDED_BREATH_CRITERION -----
# כֹּל אֲשֶׁר נִשְׁמַת־רוּחַ חַיִּים בְּאַפָּיו מִכֹּל אֲשֶׁר בֶּחָרָבָה
# מֵתוּ
# "all in whose nostrils was the breath of the spirit of life, whatsoever
# was in the dry land, died."
m.step("Gen.7.22")
# ‹נִשְׁמַת־רוּחַ חַיִּים בְּאַפָּיו … מִכֹּל אֲשֶׁר בֶּחָרָבָה מֵתוּ›
# (“breath-of spirit life in-his-nostrils … from-all which on-dry-land
# died”) — fact holds: breath-of-spirit-wind-life-in-his-nostrils; from-all-
# which-in-dry-land-died
m.fact("nishmat_ruach_chayim_be_apav",
       "mi_kol_asher_be_charavah_metu")
# witness-tier presupposed read: legal_definition_of_life on nishmat_formula
# — read, not installed
m.witness_read("nishmat_formula", "legal_definition_of_life",
                cites=["Yoma 85a:11", "Yoma 85a:12", "Mishnah Yoma 8:7"])
# witness-tier presupposed read: fish_exempted_by_the_wording on
# dry_land_limiter — read, not installed
m.witness_read("dry_land_limiter", "fish_exempted_by_the_wording",
                cites=["Kiddushin 13a:14"])

# -------------------------- Gen.7.23 · THE_WIPE_EXECUTED_ONLY_NOACH_LEFT ---
# וַיִּמַח אֶת־כָּל־הַיְקוּם אֲשֶׁר עַל־פְּנֵי הָאֲדָמָה מֵאָדָם
# עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמַיִם וַיִּמָּחוּ מִן־הָאָרֶץ
# וַיִשָּׁאֶר אַךְ־נֹחַ וַאֲשֶׁר אִתּוֹ בַּתֵּבָה
# "And He blotted out every living substance which was upon the face of the
# ground, both man, and cattle, and creeping thing, and fowl of the heaven;
# and they were blotted out from the earth; and Noah only was left, and they
# that were with him in the ark."
m.step("Gen.7.23")
# ‹וַיִּמַח אֶת־כָּל־הַיְקוּם› (“and-He-wiped obj-marker all the-standing-
# substance”) — event: wipe — theme all-the-standing-substance
m.event("wipe", themes=["kol_ha_yequm"])
# ‹מֵאָדָם עַד־בְּהֵמָה עַד־רֶמֶשׂ וְעַד־עוֹף הַשָּׁמַיִם› (“from-human
# until livestock until creeper and-until flying-creature the-heavens”) —
# fact holds: from-human-until-livestock-until-creeper-and-until-flying-
# creature
m.fact("me_adam_ad_behemah_ad_remes_ve_ad_of")
# ‹וַיִּמָּחוּ מִן־הָאָרֶץ› (“and-they-were-wiped from the-earth”) — event:
# wiped — theme all-the-standing-substance
m.event("wiped", themes=["kol_ha_yequm"])
# ‹וַיִשָּׁאֶר אַךְ־נֹחַ וַאֲשֶׁר אִתּוֹ בַּתֵּבָה› (“and-was-left only Noah
# and-which with-him in-ark”) — event: remain — theme only-Noach-and-which-
# with-him
m.event("remain", themes=["akh_noach_va_asher_ito"])
# reads without prior install (flag, not fix): Noach
m.presupposed("noach")
# witness-tier presupposed read: two_worlds_two_verbs on double_wipe_verb —
# read, not installed
m.witness_read("double_wipe_verb", "two_worlds_two_verbs",
                cites=["Jerusalem Talmud Sanhedrin 10:3:2"])
# witness-tier presupposed read: initiator_punished_first on
# from_man_to_beast_order — read, not installed
m.witness_read("from_man_to_beast_order", "initiator_punished_first",
                cites=["Mekhilta DeRabbi Yishmael, Tractate Vayehi Beshalach 2:8"])

# -------------------------- Gen.7.24 · THE_HUNDRED_AND_FIFTY_DAYS ----------
# וַיִּגְבְּרוּ הַמַּיִם עַל־הָאָרֶץ חֲמִשִּׁים וּמְאַת יוֹם
# "And the waters prevailed upon the earth a hundred and fifty days."
m.step("Gen.7.24")
# ‹וַיִּגְבְּרוּ הַמַּיִם עַל־הָאָרֶץ› (“and-prevailed the-waters over the-
# earth”) — event: prevail — agent the-waters
m.event("prevail", agent="ha_mayim")
# ‹חֲמִשִּׁים וּמְאַת יוֹם› (“fifty and-hundred day”) — fact holds: fifty-
# and-hundred-day-over-the-earth
m.fact("chamishim_u_meat_yom_al_ha_aretz")

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
    assert sorted(m.WORLD["facts"]) == sorted(['ha_mabul_arbaim_yom_al_ha_aretz', 'va_yirbu_meod_al_ha_aretz', 'gavru_meod_meod_al_ha_aretz', 'kol_he_harim_ha_gevohim_tachat_kol_ha_shamayim', 'chamesh_esreh_amah_mi_lemalah_gavru', 'ba_of_u_va_behemah_u_va_chayah_u_va_sheretz_ve_khol_ha_adam', 'nishmat_ruach_chayim_be_apav', 'mi_kol_asher_be_charavah_metu', 'me_adam_ad_behemah_ad_remes_ve_ad_of', 'chamishim_u_meat_yom_al_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('all_mountains_quantifier', 'territorial_claim_defeated'), ('nishmat_formula', 'legal_definition_of_life'), ('dry_land_limiter', 'fish_exempted_by_the_wording'), ('double_wipe_verb', 'two_worlds_two_verbs'), ('from_man_to_beast_order', 'initiator_punished_first')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 32:10']
    assert all('territorial_claim_defeated' not in f for f in m.WORLD["facts"])
    assert 'all_mountains_quantifier' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Yoma 85a:11', 'Yoma 85a:12', 'Mishnah Yoma 8:7']
    assert all('legal_definition_of_life' not in f for f in m.WORLD["facts"])
    assert 'nishmat_formula' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Kiddushin 13a:14']
    assert all('fish_exempted_by_the_wording' not in f for f in m.WORLD["facts"])
    assert 'dry_land_limiter' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Jerusalem Talmud Sanhedrin 10:3:2']
    assert all('two_worlds_two_verbs' not in f for f in m.WORLD["facts"])
    assert 'double_wipe_verb' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Mekhilta DeRabbi Yishmael, Tractate Vayehi Beshalach 2:8']
    assert all('initiator_punished_first' not in f for f in m.WORLD["facts"])
    assert 'from_man_to_beast_order' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
