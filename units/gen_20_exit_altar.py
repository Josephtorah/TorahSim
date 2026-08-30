#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_20_exit_altar — 8:15-22
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_20_exit_altar.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The exit and the altar: go out, the families, the pleasing smell, never again (8:15-22)"""
from machine import Machine

m = Machine("gen_20_exit_altar")

# -------------------------- Gen.8.15 · THE_SPEAK_VERB_DEBUTS ---------------
# וַיְדַבֵּר אֱלֹהִים אֶל־נֹחַ לֵאמֹר
# "And God spoke unto Noah, saying:"
m.step("Gen.8.15")
# ‹וַיְדַבֵּר אֱלֹהִים אֶל־נֹחַ לֵאמֹר› (“and-He-spoke God to Noah saying”)
# — event: speak — agent God; theme to-Noach
m.event("speak", agent="elohim", themes=["el_noach"])
# reads without prior install (flag, not fix): Noach, ark
m.presupposed("noach", "tevah")
# witness-tier presupposed read: speech_verb_distinction_as_law on
# dibber_operator — read, not installed
m.witness_read("dibber_operator", "speech_verb_distinction_as_law",
                cites=["Jerusalem Talmud Makkot 2:6:11"])

# -------------------------- Gen.8.16 · THE_EXIT_COMMAND --------------------
# צֵא מִן־הַתֵּבָה אַתָּה וְאִשְׁתְּךָ וּבָנֶיךָ וּנְשֵׁי־בָנֶיךָ אִתָּךְ
# "'Go forth from the ark, thou, and thy wife, and thy sons, and thy sons'
# wives with thee."
m.step("Gen.8.16")
# ‹צֵא מִן־הַתֵּבָה› (“go-out from the-ark”) — God speaks a demand — LET:
# go-out(Noach, from-the-ark)
m.declare("elohim", "LET",
          "tze(noach, min_ha_tevah)")

# -------------------------- Gen.8.17 · THE_BRING_OUT_AND_THE_CHARGE --------
# כָּל־הַחַיָּה אֲשֶׁר־אִתְּךָ מִכָּל־בָּשָׂר בָּעוֹף וּבַבְּהֵמָה
# וּבְכָל־הָרֶמֶשׂ הָרֹמֵשׂ עַל־הָאָרֶץ הוצא הַיְצֵא אִתָּךְ וְשָׁרְצוּ
# בָאָרֶץ וּפָרוּ וְרָבוּ עַל־הָאָרֶץ
# "Bring forth with thee every living thing that is with thee, of all flesh,
# both fowl, and cattle, and every creeping thing that creepeth upon the
# earth; that they may swarm in the earth, and be fruitful, and multiply
# upon the earth.'"
m.step("Gen.8.17")
# ‹הוצא הַיְצֵא אִתָּךְ› (“bring-out-written bring-out-read with-you”) — God
# speaks a demand — LET: bring-out(all-the-beast, with-you)
m.declare("elohim", "LET",
          "hotze(kol_ha_chayah, itakh)")
# ‹וְשָׁרְצוּ בָאָרֶץ וּפָרוּ וְרָבוּ עַל־הָאָרֶץ› (“and-they-shall-swarm
# in-earth and-be-fruitful and-multiply over the-earth”) — fact holds: and-
# they-shall-swarm-and-be-fruitful-and-multiply-over-the-earth
m.fact("ve_shartzu_u_faru_ve_ravu_al_ha_aretz")
# witness-tier presupposed read: written_and_read_pair_encoding_reluctance
# on exit_command — read, not installed
m.witness_read("exit_command", "written_and_read_pair_encoding_reluctance",
                cites=["Bereshit Rabbah 34:8"])

# -------------------------- Gen.8.18 · THE_EXIT_RECEIPT --------------------
# וַיֵּצֵא־נֹחַ וּבָנָיו וְאִשְׁתּוֹ וּנְשֵׁי־בָנָיו אִתּוֹ
# "And Noah went forth, and his sons, and his wife, and his sons' wives with
# him;"
m.step("Gen.8.18")
# ‹וַיֵּצֵא־נֹחַ› (“and-he-went-out Noah”) — event: go-out — agent Noach
m.event("go_out", agent="noach")
# ‹וַיֵּצֵא־נֹחַ … אִתּוֹ› (“and-he-went-out Noah … with-him”) — demand
# settled (popped from the queue): go-out(Noach, from-the-ark)
m.result("tze(noach, min_ha_tevah)", tmark="t1")

# -------------------------- Gen.8.19 · OUT_BY_FAMILIES ---------------------
# כָּל־הַחַיָּה כָּל־הָרֶמֶשׂ וְכָל־הָעוֹף כֹּל רוֹמֵשׂ עַל־הָאָרֶץ
# לְמִשְׁפְּחֹתֵיהֶם יָצְאוּ מִן־הַתֵּבָה
# "every beast, every creeping thing, and every fowl, whatsoever moveth upon
# the earth, after their families, went forth out of the ark."
m.step("Gen.8.19")
# ‹לְמִשְׁפְּחֹתֵיהֶם יָצְאוּ מִן־הַתֵּבָה› (“by-their-families they-went-
# out from the-ark”) — fact holds: to-mishpechoteihem-they-went-out-from-
# the-ark
m.fact("le_mishpechoteihem_yatzu_min_ha_tevah")
# ‹יָצְאוּ מִן־הַתֵּבָה› (“they-went-out from the-ark”) — demand settled
# (popped from the queue): bring-out(all-the-beast, with-you)
m.result("hotze(kol_ha_chayah, itakh)", tmark="t1")
# witness-tier presupposed read: mortality_inside_read_off_a_plural on
# emergence_roster — read, not installed
m.witness_read("emergence_roster", "mortality_inside_read_off_a_plural",
                cites=["Sanhedrin 108b:18", "Sanhedrin 108b:19"])

# -------------------------- Gen.8.20 · THE_FIRST_ALTAR ---------------------
# וַיִּבֶן נֹחַ מִזְבֵּחַ לַיהוָה וַיִּקַּח מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה
# וּמִכֹּל הָעוֹף הַטָּהֹר וַיַּעַל עֹלֹת בַּמִּזְבֵּחַ
# "And Noah builded an altar unto the LORD; and took of every clean beast,
# and of every clean fowl, and offered burnt-offerings on the altar."
m.step("Gen.8.20")
# ‹וַיִּבֶן נֹחַ מִזְבֵּחַ לַיהוָה› (“and-he-built Noah altar to-YHWH”) —
# event: build — agent Noach; theme altar
m.event("build", agent="noach", themes=["mizbeach"])
# ‹מִזְבֵּחַ› (“altar”) — the world gains: altar
m.install("mizbeach")
# ‹וַיִּקַּח מִכֹּל הַבְּהֵמָה הַטְּהוֹרָה וּמִכֹּל הָעוֹף הַטָּהֹר› (“and-
# he-took from-all the-livestock the-clean and-from-all the-flying-creature
# the-clean”) — event: take — agent Noach; theme from-the-livestock-the-
# clean-and-from-the-flying-creature-the-clean
m.event("take", agent="noach", themes=["min_ha_behemah_ha_tehorah_u_min_ha_of_ha_tahor"])
# ‹וַיַּעַל עֹלֹת בַּמִּזְבֵּחַ› (“and-he-offered-up burnt-offerings on-the-
# altar”) — event: offer-up — agent Noach; theme burnt-offerings-in-the-
# altar
m.event("offer_up", agent="noach", themes=["olot_ba_mizbeach"])
# witness-tier presupposed read:
# celebrant_reassigned_and_purity_vocabulary_anchored on altar_op — read,
# not installed
m.witness_read("altar_op", "celebrant_reassigned_and_purity_vocabulary_anchored",
                cites=["Bereshit Rabbah 30:6", "Jerusalem Talmud Nazir 6:1:8"])

# -------------------------- Gen.8.21 · THE_SMELL_THE_HEART_THE_NEVER_AGAINS -
# וַיָּרַח יְהוָה אֶת־רֵיחַ הַנִּיחֹחַ וַיֹּאמֶר יְהוָה אֶל־לִבּוֹ לֹא־אֹסִף
# לְקַלֵּל עוֹד אֶת־הָאֲדָמָה בַּעֲבוּר הָאָדָם כִּי יֵצֶר לֵב הָאָדָם רַע
# מִנְּעֻרָיו וְלֹא־אֹסִף עוֹד לְהַכּוֹת אֶת־כָּל־חַי כַּאֲשֶׁר עָשִׂיתִי
# "And the LORD smelled the sweet savour; and the LORD said in His heart: 'I
# will not again curse the ground any more for man's sake; for the
# imagination of man's heart is evil from his youth; neither will I again
# smite any more every thing living, as I have done."
m.step("Gen.8.21")
# ‹וַיָּרַח יְהוָה אֶת־רֵיחַ הַנִּיחֹחַ› (“and-He-smelled YHWH obj-marker
# odor-of the-pleasing”) — event: smell — agent the-LORD; theme odor-the-
# pleasing-savor
m.event("smell", agent="YHWH", themes=["reiach_ha_nichoach"])
# ‹רֵיחַ הַנִּיחֹחַ› (“odor-of the-pleasing”) — test PASS — oracle-word
# pleasing-savor, on the-burnt-offering
m.test("PASS", "nichoach", "ha_olah")
# ‹וַיֹּאמֶר יְהוָה אֶל־לִבּוֹ› (“and-He-said YHWH to His-heart”) — event:
# say — agent the-LORD; theme to-His-heart
m.event("say", agent="YHWH", themes=["el_libo"])
# ‹לֹא־אֹסִף לְקַלֵּל עוֹד אֶת־הָאֲדָמָה בַּעֲבוּר הָאָדָם כִּי יֵצֶר לֵב
# הָאָדָם רַע מִנְּעֻרָיו› (“not will-I-again to-curse again obj-marker the-
# ground for-the-sake-of the-human for inclination-of heart-of the-human
# evil from-his-youth”) — standing constraint: not-will-I-again-to-curse-
# again-obj-marker·et-the-ground
m.invariant("lo_osif_le_qalel_od_et_ha_adamah")
# ‹וְלֹא־אֹסִף עוֹד לְהַכּוֹת אֶת־כָּל־חַי כַּאֲשֶׁר עָשִׂיתִי› (“and-not
# will-I-again again to-strike obj-marker all living as I-have-done”) —
# standing constraint: not-will-I-again-again-to-strike-obj-marker·et-all-
# living
m.invariant("lo_osif_od_le_hakot_et_kol_chai")
# witness-tier presupposed read: appeasement_and_comparative_ranking on
# aroma_op — read, not installed
m.witness_read("aroma_op", "appeasement_and_comparative_ranking",
                cites=["Eruvin 65a:18", "Vayikra Rabbah 7:4"])
# witness-tier presupposed read: oath_force_and_youth_clause_law on
# doubled_clause — read, not installed
m.witness_read("doubled_clause", "oath_force_and_youth_clause_law",
                cites=["Bereshit Rabbah 34:10", "Jerusalem Talmud Berakhot 3:5:7"])

# -------------------------- Gen.8.22 · THE_SEASONS_PLEDGE ------------------
# עֹד כָּל־יְמֵי הָאָרֶץ זֶרַע וְקָצִיר וְקֹר וָחֹם וְקַיִץ וָחֹרֶף וְיוֹם
# וָלַיְלָה לֹא יִשְׁבֹּתוּ
# "While the earth remaineth, seedtime and harvest, and cold and heat, and
# summer and winter, and day and night shall not cease.'"
m.step("Gen.8.22")
# ‹זֶרַע וְקָצִיר וְקֹר וָחֹם וְקַיִץ וָחֹרֶף וְיוֹם וָלַיְלָה לֹא
# יִשְׁבֹּתוּ› (“seedtime and-harvest and-cold and-heat and-summer and-
# winter and-day and-night not shall-cease”) — standing constraint:
# seedtime-and-harvest-and-cold-and-heat-and-summer-and-winter-and-day-and-
# night-not-shall-cease
m.invariant("zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu")
# witness-tier presupposed read: termination_condition_and_new_parameters on
# seasons_covenant — read, not installed
m.witness_read("seasons_covenant", "termination_condition_and_new_parameters",
                cites=["Bereshit Rabbah 34:11"])

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == {'mizbeach'}
    assert m.presupposed_set() == {'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == [('PASS', 'nichoach', 'ha_olah')]
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 2
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 2}
    assert sorted(m.WORLD["facts"]) == sorted(['ve_shartzu_u_faru_ve_ravu_al_ha_aretz', 'le_mishpechoteihem_yatzu_min_ha_tevah'])
    assert m.WORLD["invariants"] == ['lo_osif_le_qalel_od_et_ha_adamah', 'lo_osif_od_le_hakot_et_kol_chai', 'zera_ve_qatzir_ve_qor_va_chom_ve_qayitz_va_choref_ve_yom_va_laylah_lo_yishbotu']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 11
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('dibber_operator', 'speech_verb_distinction_as_law'), ('exit_command', 'written_and_read_pair_encoding_reluctance'), ('emergence_roster', 'mortality_inside_read_off_a_plural'), ('altar_op', 'celebrant_reassigned_and_purity_vocabulary_anchored'), ('aroma_op', 'appeasement_and_comparative_ranking'), ('doubled_clause', 'oath_force_and_youth_clause_law'), ('seasons_covenant', 'termination_condition_and_new_parameters')]
    assert m.WITNESS_READS[0]["cites"] == ['Jerusalem Talmud Makkot 2:6:11']
    assert all('speech_verb_distinction_as_law' not in f for f in m.WORLD["facts"])
    assert 'dibber_operator' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 34:8']
    assert all('written_and_read_pair_encoding_reluctance' not in f for f in m.WORLD["facts"])
    assert 'exit_command' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Sanhedrin 108b:18', 'Sanhedrin 108b:19']
    assert all('mortality_inside_read_off_a_plural' not in f for f in m.WORLD["facts"])
    assert 'emergence_roster' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Bereshit Rabbah 30:6', 'Jerusalem Talmud Nazir 6:1:8']
    assert all('celebrant_reassigned_and_purity_vocabulary_anchored' not in f for f in m.WORLD["facts"])
    assert 'altar_op' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[4]["cites"] == ['Eruvin 65a:18', 'Vayikra Rabbah 7:4']
    assert all('appeasement_and_comparative_ranking' not in f for f in m.WORLD["facts"])
    assert 'aroma_op' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[5]["cites"] == ['Bereshit Rabbah 34:10', 'Jerusalem Talmud Berakhot 3:5:7']
    assert all('oath_force_and_youth_clause_law' not in f for f in m.WORLD["facts"])
    assert 'doubled_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[6]["cites"] == ['Bereshit Rabbah 34:11']
    assert all('termination_condition_and_new_parameters' not in f for f in m.WORLD["facts"])
    assert 'seasons_covenant' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
