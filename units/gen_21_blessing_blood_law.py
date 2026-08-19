#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_21_blessing_blood_law — 9:1-7
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_21_blessing_blood_law.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The blessing and the blood-law: be fruitful again, but the blood is Mine (9:1-7)"""
from machine import Machine

m = Machine("gen_21_blessing_blood_law")

# -------------------------- Gen.9.1 · THE_BLESSING_REISSUED_SHORTER --------
# וַיְבָרֶךְ אֱלֹהִים אֶת־נֹחַ וְאֶת־בָּנָיו וַיֹּאמֶר לָהֶם פְּרוּ וּרְבוּ
# וּמִלְאוּ אֶת־הָאָרֶץ
# "And God blessed Noah and his sons, and said unto them: 'Be fruitful and
# multiply, and replenish the earth."
m.step("Gen.9.1")
# ‹וַיְבָרֶךְ אֱלֹהִים אֶת־נֹחַ וְאֶת־בָּנָיו … פְּרוּ וּרְבוּ וּמִלְאוּ
# אֶת־הָאָרֶץ› (“and-He-blessed God obj-marker Noah obj-marker his-sons …
# be-fruitful and-multiply and-fill obj-marker the-earth”) — blessing: God
# blesses Noach-and-vanav — mandate: CMD!(peru), CMD!(revu), CMD!(milu(et-
# the-aretz))
m.bless("elohim", "noach_u_vanav", mandate=["CMD!(peru)", "CMD!(revu)", "CMD!(milu(et_ha_aretz))"])
# reads without prior install (flag, not fix): Noach, banav
m.presupposed("noach", "banav")

# -------------------------- Gen.9.2 · FEAR_AND_DREAD_IN_DOMINIONS_PLACE ----
# וּמוֹרַאֲכֶם וְחִתְּכֶם יִהְיֶה עַל כָּל־חַיַּת הָאָרֶץ וְעַל כָּל־עוֹף
# הַשָּׁמָיִם בְּכֹל אֲשֶׁר תִּרְמֹשׂ הָאֲדָמָה וּבְכָל־דְּגֵי הַיָּם
# בְּיֶדְכֶם נִתָּנוּ
# "And the fear of you and the dread of you shall be upon every beast of the
# earth, and upon every fowl of the air, and upon all wherewith the ground
# teemeth, and upon all the fishes of the sea: into your hand are they
# delivered."
m.step("Gen.9.2")
# ‹וּמוֹרַאֲכֶם וְחִתְּכֶם … בְּיֶדְכֶם נִתָּנוּ› (“and-the-fear-of-you and-
# the-dread-of-you … into-your-hand they-are-given”) — fact holds:
# moraakhem-and-chitkhem-over-all-living-the-earth; in-yedkhem-nittanu
m.fact("moraakhem_ve_chitkhem_al_kol_chayat_ha_aretz",
       "be_yedkhem_nittanu")

# -------------------------- Gen.9.3 · THE_MEAT_GRANT_CITES_THE_OLD ---------
# כָּל־רֶמֶשׂ אֲשֶׁר הוּא־חַי לָכֶם יִהְיֶה לְאָכְלָה כְּיֶרֶק עֵשֶׂב
# נָתַתִּי לָכֶם אֶת־כֹּל
# "Every moving thing that liveth shall be for food for you; as the green
# herb have I given you all."
m.step("Gen.9.3")
# ‹כָּל־רֶמֶשׂ אֲשֶׁר הוּא־חַי … לְאָכְלָה› (“all moving-thing which it
# living … for-food”) — role assigned: all-moving-thing-which-it-living ->
# food-to-you
m.assign("kol_remes_asher_hu_chai", "okhlah_la_khem")
# ‹לָכֶם יִהְיֶה לְאָכְלָה› (“to-you shall-be for-food”) — God speaks a
# demand — LET?: yihyeh(all-moving-thing-living, for-food)
m.declare("elohim", "LET?",
          "yihyeh(kol_remes_chai, le_okhlah)")
# ‹כְּיֶרֶק עֵשֶׂב נָתַתִּי לָכֶם אֶת־כֹּל› (“as-the-green-of herb I-have-
# given to-you obj-marker all”) — fact holds: like-as-the-green-of-herb-I-
# have-given-to-you-obj-marker·et-all
m.fact("ke_yereq_esev_natati_la_khem_et_kol")

# -------------------------- Gen.9.4 · THE_FIRST_PROHIBITION_SINCE_EDEN -----
# אַךְ־בָּשָׂר בְּנַפְשׁוֹ דָמוֹ לֹא תֹאכֵלוּ
# "Only flesh with the life thereof, which is the blood thereof, shall ye
# not eat."
m.step("Gen.9.4")
# ‹אַךְ־בָּשָׂר בְּנַפְשׁוֹ דָמוֹ לֹא תֹאכֵלוּ› (“only flesh with-its-life
# its-blood not you-shall-eat”) — God speaks a demand — LET-NOT: eat(flesh-
# in-nafsho-damo)
m.declare("elohim", "LET-NOT",
          "akhal(basar_be_nafsho_damo)")

# -------------------------- Gen.9.5 · THE_RECKONING_LADDER -----------------
# וְאַךְ אֶת־דִּמְכֶם לְנַפְשֹׁתֵיכֶם אֶדְרֹשׁ מִיַּד כָּל־חַיָּה
# אֶדְרְשֶׁנּוּ וּמִיַּד הָאָדָם מִיַּד אִישׁ אָחִיו אֶדְרֹשׁ אֶת־נֶפֶשׁ
# הָאָדָם
# "And surely your blood of your lives will I require; at the hand of every
# beast will I require it; and at the hand of man, even at the hand of every
# man's brother, will I require the life of man."
m.step("Gen.9.5")
# ‹וְאַךְ אֶת־דִּמְכֶם לְנַפְשֹׁתֵיכֶם אֶדְרֹשׁ … אֶדְרְשֶׁנּוּ … אֶדְרֹשׁ›
# (“and-only obj-marker your-blood for-your-lives I-will-require … I-will-
# require-it … I-will-require”) — standing constraint: obj-marker·et-
# dimkhem-to-nafshoteikhem-I-will-require
m.invariant("et_dimkhem_le_nafshoteikhem_edrosh")
# ‹מִיַּד כָּל־חַיָּה … וּמִיַּד הָאָדָם מִיַּד אִישׁ אָחִיו› (“from-the-
# hand-of all living … and-from-the-hand-of the-human from-the-hand-of a-man
# his-brother”) — fact holds: from-hand-of-all-beast-and-from-hand-of-the-
# human-a-man-his-brother
m.fact("mi_yad_kol_chayah_u_mi_yad_ha_adam_ish_achiv")

# -------------------------- Gen.9.6 · THE_TALION_ON_THE_IMAGE_GROUND -------
# שֹׁפֵךְ דַּם הָאָדָם בָּאָדָם דָּמוֹ יִשָּׁפֵךְ כִּי בְּצֶלֶם אֱלֹהִים
# עָשָׂה אֶת־הָאָדָם
# "Whoso sheddeth man's blood, by man shall his blood be shed; for in the
# image of God made He man."
m.step("Gen.9.6")
# ‹שֹׁפֵךְ דַּם הָאָדָם בָּאָדָם דָּמוֹ יִשָּׁפֵךְ› (“the-shedder-of the-
# blood-of the-human by-the-human his-blood shall-be-shed”) — standing
# handler — if shedder-of(blood-of-the-human) then in-the-human-damo-shall-
# be-shed
m.handler("shofekh(dam_ha_adam)",
          "ba_adam_damo_yishafekh")
# ‹כִּי בְּצֶלֶם אֱלֹהִים עָשָׂה אֶת־הָאָדָם› (“that in-the-image-of God He-
# made obj-marker the-human”) — fact holds: that-in-image-of-God-make-obj-
# marker·et-the-human
m.fact("ki_be_tzelem_elohim_asah_et_ha_adam")

# -------------------------- Gen.9.7 · THE_FRAME_REDOUBLED ------------------
# וְאַתֶּם פְּרוּ וּרְבוּ שִׁרְצוּ בָאָרֶץ וּרְבוּ־בָהּ
# "And you, be ye fruitful, and multiply; swarm in the earth, and multiply
# therein.'"
m.step("Gen.9.7")
# ‹וְאַתֶּם פְּרוּ וּרְבוּ שִׁרְצוּ בָאָרֶץ וּרְבוּ־בָהּ› (“and-you be-
# fruitful and-multiply swarm in-the-earth and-multiply in-her/its”) — fact
# holds: and-you-be-fruitful-and-multiply-swarm-and-earth
m.fact("ve_atem_peru_u_revu_shirtzu_va_aretz")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'banav', 'noach'}
    assert m.REGISTRY["names"] == {'kol_remes_asher_hu_chai': 'okhlah_la_khem'}
    assert m.REGISTRY["writes"] == 1
    assert m.tests_list() == []
    assert m.open_demands() == ['yihyeh(kol_remes_chai, le_okhlah)', 'akhal(basar_be_nafsho_damo)']
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2, 'assigned_before_any_presence': 1}
    assert sorted(m.WORLD["facts"]) == sorted(['mandate: CMD!(peru)', 'mandate: CMD!(revu)', 'mandate: CMD!(milu(et_ha_aretz))', 'moraakhem_ve_chitkhem_al_kol_chayat_ha_aretz', 'be_yedkhem_nittanu', 'ke_yereq_esev_natati_la_khem_et_kol', 'mi_yad_kol_chayah_u_mi_yad_ha_adam_ish_achiv', 'handler: IF(shofekh(dam_ha_adam)) THEN(ba_adam_damo_yishafekh)', 'ki_be_tzelem_elohim_asah_et_ha_adam', 've_atem_peru_u_revu_shirtzu_va_aretz'])
    assert m.WORLD["invariants"] == ['et_dimkhem_le_nafshoteikhem_edrosh']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 5
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
