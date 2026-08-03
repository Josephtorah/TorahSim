#!/usr/bin/env python3
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
# ‹לֶךְ־לְךָ … אֶל־הָאָרֶץ אֲשֶׁר אַרְאֶךָּ› the-LORD speaks a demand — LET:
# lekh(avram, to-the-earth-which-areka)
m.declare("YHWH", "LET",
          "lekh(avram, el_ha_aretz_asher_areka)")
# ‹מֵאַרְצְךָ וּמִמּוֹלַדְתְּךָ וּמִבֵּית אָבִיךָ› fact holds: lekh-to-you-
# from-artzekha-and-from-moladtekha-and-from-beit-avikha
m.fact("lekh_lekha_me_artzekha_u_mi_moladtekha_u_mi_beit_avikha")

# -------------------------- Gen.12.2 · THE_PROMISE_LADDER_AND_THE_SECOND_IMPERATIVE -
# וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ וֶהְיֵה
# בְּרָכָה
# "And I will make of thee a great nation, and I will bless thee, and make
# thy name great; and be thou a blessing."
m.step("Gen.12.2")
# ‹וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל וַאֲבָרֶכְךָ וַאֲגַדְּלָה שְׁמֶךָ› fact holds:
# e-eskha-to-goy-gadol; and-avarekhkha-and-agadlah-shmekha
m.fact("e_eskha_le_goy_gadol",
       "va_avarekhkha_va_agadlah_shmekha")
# ‹וֶהְיֵה בְּרָכָה› the-LORD speaks a demand — LET: heyeh(avram, berakhah)
m.declare("YHWH", "LET",
          "heyeh(avram, berakhah)")

# -------------------------- Gen.12.3 · THE_ASYMMETRY_AND_THE_FAMILIES ------
# וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר וְנִבְרְכוּ בְךָ כֹּל
# מִשְׁפְּחֹת הָאֲדָמָה
# "And I will bless them that bless thee, and him that curseth thee will I
# curse; and in thee shall all the families of the earth be blessed.'"
m.step("Gen.12.3")
# ‹וַאֲבָרֲכָה מְבָרְכֶיךָ וּמְקַלֶּלְךָ אָאֹר› fact holds: and-avarakhah-
# mevarakhekha; and-meqallelkha-aor
m.fact("va_avarakhah_mevarakhekha",
       "u_meqallelkha_aor")
# ‹וְנִבְרְכוּ בְךָ כֹּל מִשְׁפְּחֹת הָאֲדָמָה› fact holds: and-nivrekhu-
# vekha-all-mishpechot-the-ground
m.fact("ve_nivrekhu_vekha_kol_mishpechot_ha_adamah")

# -------------------------- Gen.12.4 · THE_RECEIPT_IN_THE_LETTERS_OWN_GRAMMAR -
# וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה וַיֵּלֶךְ אִתּוֹ לוֹט
# וְאַבְרָם בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה בְּצֵאתוֹ מֵחָרָן
# "So Abram went, as the LORD had spoken unto him; and Lot went with him;
# and Abram was seventy and five years old when he departed out of Haran."
m.step("Gen.12.4")
# ‹וַיֵּלֶךְ אַבְרָם … וַיֵּלֶךְ אִתּוֹ לוֹט› event: go — agent avram
m.event("go", agent="avram")
# ‹וַיֵּלֶךְ אַבְרָם כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה› demand settled (popped
# from the queue): lekh(avram, to-the-earth-which-areka)
m.result("lekh(avram, el_ha_aretz_asher_areka)", tmark="t1")
# ‹כַּאֲשֶׁר דִּבֶּר אֵלָיו יְהוָה … בֶּן־חָמֵשׁ שָׁנִים וְשִׁבְעִים שָׁנָה›
# fact holds: like-which-dibber-to-him-the-LORD; avram-ben-75-year-in-tzeto-
# from-charan
m.fact("ka_asher_dibber_elav_YHWH",
       "avram_ben_75_shanah_be_tzeto_me_charan")
# reads without prior install (flag, not fix): charan
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
# ‹וַיִּקַּח אַבְרָם אֶת־שָׂרַי אִשְׁתּוֹ וְאֶת־לוֹט בֶּן־אָחִיו …› event:
# take — agent avram; theme saray, lot, all-rekhusham, the-nefesh-which-asu
m.event("take", agent="avram", themes=["saray", "lot", "kol_rekhusham", "ha_nefesh_asher_asu"])
# ‹וַיֵּצְאוּ לָלֶכֶת אַרְצָה כְּנַעַן› event: go-out — agent avram
m.event("go_out", agent="avram")
# ‹וַיָּבֹאוּ אַרְצָה כְּנָעַן› event: come — agent avram
m.event("come", agent="avram")
# ‹וְאֶת־כָּל־רְכוּשָׁם אֲשֶׁר רָכָשׁוּ וְאֶת־הַנֶּפֶשׁ אֲשֶׁר־עָשׂוּ
# בְחָרָן› fact holds: all-rekhusham-which-rakhashu; and-the-nefesh-which-
# asu-and-charan
m.fact("kol_rekhusham_asher_rakhashu",
       "ve_et_ha_nefesh_asher_asu_ve_charan")
# reads without prior install (flag, not fix): earth-kenaan
m.presupposed("eretz_kenaan")

# -------------------------- Gen.12.6 · THE_PASS_AND_THE_THEN ---------------
# וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה
# וְהַכְּנַעֲנִי אָז בָּאָרֶץ
# "And Abram passed through the land unto the place of Shechem, unto the
# terebinth of Moreh. And the Canaanite was then in the land."
m.step("Gen.12.6")
# ‹וַיַּעֲבֹר אַבְרָם בָּאָרֶץ עַד מְקוֹם שְׁכֶם עַד אֵלוֹן מוֹרֶה› event:
# pass — agent avram; theme until-meqom-shekhem-until-elon-moreh
m.event("pass", agent="avram", themes=["ad_meqom_shekhem_ad_elon_moreh"])
# ‹וְהַכְּנַעֲנִי אָז בָּאָרֶץ› fact holds: and-the-kenaani-az-in-the-earth
m.fact("ve_ha_kenaani_az_ba_aretz")
# reads without prior install (flag, not fix): shekhem
m.presupposed("shekhem")

# -------------------------- Gen.12.7 · THE_APPEARANCE_THE_PLEDGE_THE_FIRST_ALTAR -
# וַיֵּרָא יְהוָה אֶל־אַבְרָם וַיֹּאמֶר לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ
# הַזֹּאת וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו
# "And the LORD appeared unto Abram, and said: 'Unto thy seed will I give
# this land'; and he builded there an altar unto the LORD, who appeared unto
# him."
m.step("Gen.12.7")
# ‹וַיֵּרָא יְהוָה אֶל־אַבְרָם› event: appear — agent the-LORD
m.event("appear", agent="YHWH")
# ‹וַיֹּאמֶר› event: say — agent the-LORD
m.event("say", agent="YHWH")
# ‹לְזַרְעֲךָ אֶתֵּן אֶת־הָאָרֶץ הַזֹּאת› fact holds: to-zarakha-etten-the-
# earth-the-this
m.fact("le_zarakha_etten_et_ha_aretz_ha_zot")
# ‹וַיִּבֶן שָׁם מִזְבֵּחַ לַיהוָה הַנִּרְאֶה אֵלָיו› event: build — agent
# avram; theme altar-shekhem
m.event("build", agent="avram", themes=["mizbeach_shekhem"])
# ‹מִזְבֵּחַ› the world gains: altar-shekhem
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
# ‹וַיַּעְתֵּק מִשָּׁם הָהָרָה מִקֶּדֶם לְבֵית־אֵל› event: move-on — agent
# avram
m.event("move_on", agent="avram")
# ‹וַיֵּט אָהֳלֹה בֵּית־אֵל מִיָּם וְהָעַי מִקֶּדֶם› event: pitch — agent
# avram; theme ohel
m.event("pitch", agent="avram", themes=["ohel"])
# ‹וַיִּבֶן־שָׁם מִזְבֵּחַ לַיהוָה› event: build — agent avram; theme altar-
# beit-to
m.event("build", agent="avram", themes=["mizbeach_beit_el"])
# ‹מִזְבֵּחַ› the world gains: altar-beit-to
m.install("mizbeach_beit_el")
# ‹וַיִּקְרָא בְּשֵׁם יְהוָה› event: call — agent avram; theme in-shem-the-
# LORD
m.event("call", agent="avram", themes=["be_shem_YHWH"])
# reads without prior install (flag, not fix): beit-to, the-ai
m.presupposed("beit_el", "ha_ai")

# -------------------------- Gen.12.9 · THE_ROAD_SOUTH_STAYS_OPEN -----------
# וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה
# "And Abram journeyed, going on still toward the South."
m.step("Gen.12.9")
# ‹וַיִּסַּע אַבְרָם הָלוֹךְ וְנָסוֹעַ הַנֶּגְבָּה› event: journey — agent
# avram
m.event("journey", agent="avram")
# reads without prior install (flag, not fix): the-negev
m.presupposed("ha_negev")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach_shekhem', 'mizbeach_beit_el'}
    assert m.presupposed_set() == {'ha_ai', 'shekhem', 'beit_el', 'charan', 'eretz_kenaan', 'ha_negev'}
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
