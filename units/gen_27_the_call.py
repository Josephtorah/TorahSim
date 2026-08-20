#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_27_the_call — 12:1-9
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_27_the_call.yaml) is CANONICAL (Pre-Code); this
# file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The call: go to the land I will show you (12:1-9)"""
from machine import Machine

m = Machine("gen_27_the_call")

# -------------------------- Gen.12.1 · THE_CALL_WITH_THE_OBJECT_WITHHELD ---
# וַיֹּאמֶר יְהוָה אֶל־אַבְרָם לֶךְ־לְךָ מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ
# וּמִבֵּית אָבִיךָ אֶל־הָאָרֶץ אֲשֶׁר אַרְאֶךָּ
# "Now the LORD said unto Abram: 'Get thee out of thy country, and from thy
# kindred, and from thy father's house, unto the land that I will show
# thee.'"
m.step("Gen.12.1")
# ‹לֶךְ־לְךָ … אֶל־הָאָרֶץ אֲשֶׁר אַרְאֶךָּ› (“go to-you/your … to the-earth
# which see-you/your”) — the-LORD speaks a demand — LET: go(Abram, to-the-
# earth-which-areka)
m.declare("YHWH", "LET",
          "lekh(avram, el_ha_aretz_asher_areka)")
# ‹מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ וּמִבֵּית אָבִיךָ› (“from-earth-you/your
# and-from-nativity-you/your and-from-house father-you/your”) — fact holds:
# go-to-you-from-artzekha-and-from-moladtekha-and-from-beit-avikha
m.fact("lekh_lekha_me_artzekha_u_mi_moladtekha_u_mi_beit_avikha")

# -------------------------- Gen.12.2 · THE_PROMISE_LADDER_AND_THE_SECOND_IMPERATIVE -
# וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ וֶהְיֵה
# בְּרָכָה
# "And I will make of thee a great nation, and I will bless thee, and make
# thy name great; and be thou a blessing."
m.step("Gen.12.2")
# ‹וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ› (“and-make-
# you/your to-nation great and-bless-you/your and-be-large name-you/your”) —
# fact holds: e-eskha-to-nation-great; and-avarekhkha-and-agadlah-shmekha
m.fact("e_eskha_le_goy_gadol",
       "va_avarekhkha_va_agadlah_shmekha")
# ‹וֶהְיֵה בְּרָכָה› (“and-be blessing”) — the-LORD speaks a demand — LET:
# heyeh(Abram, berakhah)
m.declare("YHWH", "LET",
          "heyeh(avram, berakhah)")

# -------------------------- Gen.12.3 · THE_ASYMMETRY_AND_THE_FAMILIES ------
# וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר וְנִבְרְכוּ בְךָ כֹּל
# מִשְׁפְּחֹת הָאֲדָמָה
# "And I will bless them that bless thee, and him that curseth thee will I
# curse; and in thee shall all the families of the earth be blessed.'"
m.step("Gen.12.3")
# ‹וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר› (“and-bless bless-you/your
# and-be-light-you/your execrate”) — fact holds: and-avarakhah-mevarakhekha;
# and-meqallelkha-execrate
m.fact("va_avarakhah_mevarakhekha",
       "u_meqallelkha_aor")
# ‹וְנִבְרְכוּ בְךָ כֹּל מִשְׁפְּחֹת הָאֲדָמָה› (“and-bless in-you/your all
# family the-ground”) — fact holds: and-nivrekhu-vekha-all-mishpechot-the-
# ground
m.fact("ve_nivrekhu_vekha_kol_mishpechot_ha_adamah")

# -------------------------- Gen.12.4 · THE_RECEIPT_IN_THE_LETTERS_OWN_GRAMMAR -
# וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה וַיֵּלֶךְ אִתּוֹ לוֹט
# וְאַבְרָם בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה בְּצֵאתוֹ מֵחָרָן
# "So Abram went, as the LORD had spoken unto him; and Lot went with him;
# and Abram was seventy and five years old when he departed out of Haran."
m.step("Gen.12.4")
# ‹וַיֵּלֶךְ אַבְרָם … וַיֵּלֶךְ אִתּוֹ לוֹט› (“and-go Abram … and-go with-
# him/its Lot”) — event: go — agent Abram
m.event("go", agent="avram")
# ‹וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה› (“and-go Abram like-
# as/which speak to-him/its YHWH”) — demand settled (popped from the queue):
# go(Abram, to-the-earth-which-areka)
m.result("lekh(avram, el_ha_aretz_asher_areka)", tmark="t1")
# ‹כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה … בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה›
# (“like-as/which speak to-him/its YHWH … son five years and-seventy years”)
# — fact holds: like-which-dibber-to-him-the-LORD; Abram-son-75-year-in-
# tzeto-from-Haran
m.fact("ka_asher_dibber_elav_YHWH",
       "avram_ben_75_shanah_be_tzeto_me_charan")
# reads without prior install (flag, not fix): Haran
m.presupposed("charan")

# -------------------------- Gen.12.5 · THE_ARRIVAL_THE_FROZEN_WALL_WAITED_FOR -
# וַיִּקַּח אַבְרָם אֶת־שָׂרַי אִשְׁתּוֹ וְאֶת־לוֹט בֶּן־אָחִיו
# וְאֶת־כָּל־רְכוּשָׁם אֲשֶׁר רָכָשׁוּ וְאֶת־הַנֶּפֶשׁ אֲשֶׁר־עָשׂוּ בְחָרָן
# וַיֵּצְאוּ לָלֶכֶת אַרְצָה כְּנַעַן וַיָּבֹאוּ אַרְצָה כְּנָעַן
# "And Abram took Sarai his wife, and Lot his brother's son, and all their
# substance that they had gathered, and the souls that they had gotten in
# Haran; and they went forth to go into the land of Canaan; and into the
# land of Canaan they came."
m.step("Gen.12.5")
# ‹וַיִּקַּח אַבְרָם אֶת־שָׂרַי אִשְׁתּוֹ וְאֶת־לוֹט בֶּן־אָחִיו …› (“and-
# take Abram obj-marker Sarai woman-him/its and-obj-marker Lot son brother-
# him/its”) — event: take — agent Abram; theme Sarai, Lot, all-rekhusham,
# the-living-being-which-make
m.event("take", agent="avram", themes=["saray", "lot", "kol_rekhusham", "ha_nefesh_asher_asu"])
# ‹וַיֵּצְאוּ לָלֶכֶת אַרְצָה כְּנַעַן› (“and-bring-forth to-go earth-ward
# Canaan”) — event: go-out — agent Abram
m.event("go_out", agent="avram")
# ‹וַיָּבֹאוּ אַרְצָה כְּנָעַן› (“and-come/bring earth-ward Canaan”) —
# event: come — agent Abram
m.event("come", agent="avram")
# ‹וְאֶת־כָּל־רְכוּשָׁם אֲשֶׁר רָכָשׁוּ וְאֶת־הַנֶּפֶשׁ אֲשֶׁר־עָשׂוּ
# בְחָרָן› (“and-obj-marker all property-them/their which lay-up and-obj-
# marker the-living-being which make in-Haran”) — fact holds: all-rekhusham-
# which-lay-up; and-obj-marker-the-living-being-which-make-and-Haran
m.fact("kol_rekhusham_asher_rakhashu",
       "ve_et_ha_nefesh_asher_asu_ve_charan")
# reads without prior install (flag, not fix): earth-Canaan
m.presupposed("eretz_kenaan")

# -------------------------- Gen.12.6 · THE_PASS_AND_THE_THEN ---------------
# וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה
# וְהַכְּנַעֲנִי אָז בָּאָרֶץ
# "And Abram passed through the land unto the place of Shechem, unto the
# terebinth of Moreh. And the Canaanite was then in the land."
m.step("Gen.12.6")
# ‹וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה› (“and-
# pass-over Abram in-earth until place Shechem until oak Moreh”) — event:
# pass — agent Abram; theme until-place-Shechem-until-oak-moreh
m.event("pass", agent="avram", themes=["ad_meqom_shekhem_ad_elon_moreh"])
# ‹וְהַכְּנַעֲנִי אָז בָּאָרֶץ› (“and-the-Kenaanite at-that-time in-earth”)
# — fact holds: and-the-Kenaanite-at-that-time-in-the-earth
m.fact("ve_ha_kenaani_az_ba_aretz")
# reads without prior install (flag, not fix): Shechem
m.presupposed("shekhem")

# -------------------------- Gen.12.7 · THE_APPEARANCE_THE_PLEDGE_THE_FIRST_ALTAR -
# וַיֵּרָא יְהוָה אֶל־אַבְרָם וַיֹּאמֶר לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ
# הַזֹּאת וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו
# "And the LORD appeared unto Abram, and said: 'Unto thy seed will I give
# this land'; and he builded there an altar unto the LORD, who appeared unto
# him."
m.step("Gen.12.7")
# ‹וַיֵּרָא יְהוָה אֶל־אַבְרָם› (“and-see YHWH to Abram”) — event: appear —
# agent the-LORD
m.event("appear", agent="YHWH")
# ‹וַיֹּאמֶר› (“and-say”) — event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ הַזֹּאת› (“to-seed-you/your set obj-marker
# the-earth the-this”) — fact holds: to-zarakha-etten-obj-marker-the-earth-
# the-this
m.fact("le_zarakha_etten_et_ha_aretz_ha_zot")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו› (“and-build there
# altar to-YHWH the-see to-him/its”) — event: build — agent Abram; theme
# altar-Shechem
m.event("build", agent="avram", themes=["mizbeach_shekhem"])
# ‹מִזְבֵּחַ› (“altar”) — the world gains: altar-Shechem
m.install("mizbeach_shekhem")

# -------------------------- Gen.12.8 · THE_TENT_THE_SECOND_ALTAR_THE_NAME_CALLED -
# וַיַּעְתֵּק מִשָּׁם הָהָרָה מִקֶּדֶם לְבֵית־אֵל וַיֵּט אָהֳלֹה בֵּית־אֵל
# מִיָּם וְהָעַי מִקֶּדֶם וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה וַיִּקְרָא בְּשֵׁם
# יְהוָה
# "And he removed from thence unto the mountain on the east of Beth-el, and
# pitched his tent, having Beth-el on the west, and Ai on the east; and he
# builded there an altar unto the LORD, and called upon the name of the
# LORD."
m.step("Gen.12.8")
# ‹וַיַּעְתֵּק מִשָּׁם הָהָרָה מִקֶּדֶם לְבֵית־אֵל› (“and-moved-on from-
# there the-mountain-ward from-the-east to Beth-el”) — event: move-on —
# agent Abram
m.event("move_on", agent="avram")
# ‹וַיֵּט אָהֳלֹה בֵּית־אֵל מִיָּם וְהָעַי מִקֶּדֶם› (“and-stretch tent-
# him/its Beth-el from-seas and-the-Ai from-the-east”) — event: pitch —
# agent Abram; theme ohel
m.event("pitch", agent="avram", themes=["ohel"])
# ‹וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה› (“and-build there altar to-YHWH”) —
# event: build — agent Abram; theme altar-beit-to
m.event("build", agent="avram", themes=["mizbeach_beit_el"])
# ‹מִזְבֵּחַ› (“altar”) — the world gains: altar-beit-to
m.install("mizbeach_beit_el")
# ‹וַיִּקְרָא בְּשֵׁם יְהוָה› (“and-call in-name YHWH”) — event: call —
# agent Abram; theme in-name-the-LORD
m.event("call", agent="avram", themes=["be_shem_YHWH"])
# reads without prior install (flag, not fix): beit-to, the-ai
m.presupposed("beit_el", "ha_ai")

# -------------------------- Gen.12.9 · THE_ROAD_SOUTH_STAYS_OPEN -----------
# וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה
# "And Abram journeyed, going on still toward the South."
m.step("Gen.12.9")
# ‹וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה› (“and-journey Abram
# walk/go and-journey the-south-ward”) — event: journey — agent Abram
m.event("journey", agent="avram")
# reads without prior install (flag, not fix): the-negev
m.presupposed("ha_negev")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach_beit_el', 'mizbeach_shekhem'}
    assert m.presupposed_set() == {'beit_el', 'charan', 'eretz_kenaan', 'ha_ai', 'ha_negev', 'shekhem'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == ['heyeh(avram, berakhah)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 6}
    assert sorted(m.WORLD["facts"]) == sorted(['lekh_lekha_me_artzekha_u_mi_moladtekha_u_mi_beit_avikha', 'e_eskha_le_goy_gadol', 'va_avarekhkha_va_agadlah_shmekha', 'va_avarakhah_mevarakhekha', 'u_meqallelkha_aor', 've_nivrekhu_vekha_kol_mishpechot_ha_adamah', 'ka_asher_dibber_elav_YHWH', 'avram_ben_75_shanah_be_tzeto_me_charan', 'kol_rekhusham_asher_rakhashu', 've_et_ha_nefesh_asher_asu_ve_charan', 've_ha_kenaani_az_ba_aretz', 'le_zarakha_etten_et_ha_aretz_ha_zot'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 16
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
