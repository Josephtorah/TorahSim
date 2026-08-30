#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_22_covenant_bow — 9:8-17
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_22_covenant_bow.yaml) is CANONICAL (Pre-Code);
# this file is a derived, runnable rendering. Do not edit — regenerate. The
# assertion block at the bottom is baked from the Stage D interpreter's
# actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The covenant and the bow: My bow I have set in the cloud (9:8-17)"""
from machine import Machine

m = Machine("gen_22_covenant_bow")

# -------------------------- Gen.9.8 · THE_TRIPLE_FRAME_OPENS ---------------
# וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ וְאֶל־בָּנָיו אִתּוֹ לֵאמֹר
# "And God spoke unto Noah, and to his sons with him, saying:"
m.step("Gen.9.8")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ וְאֶל־בָּנָיו אִתּוֹ› (“and-He-said God to
# Noah and-to his-sons with-him”) — event: speak — agent God; theme to-
# Noach-and-to-banav
m.event("speak", agent="elohim", themes=["el_noach_ve_el_banav"])
# reads without prior install (flag, not fix): Noach, banav, ark
m.presupposed("noach", "banav", "tevah")
# witness-grounded state (its own tier): demotion_or_elevation on
# address_widened
m.witness_state("address_widened", "demotion_or_elevation",
                cites=["Bereshit Rabbah 35:1"])

# -------------------------- Gen.9.9 · I_AM_ESTABLISHING --------------------
# וַאֲנִי הִנְנִי מֵקִים אֶת־בְּרִיתִי אִתְּכֶם וְאֶת־זַרְעֲכֶם אַחֲרֵיכֶם
# "'As for Me, behold, I establish My covenant with you, and with your seed
# after you;"
m.step("Gen.9.9")
# ‹הִנְנִי מֵקִים אֶת־בְּרִיתִי אִתְּכֶם וְאֶת־זַרְעֲכֶם› (“behold-I
# establishing obj-marker My-covenant with-you and-with your-seed”) — fact
# holds: hinni-mekim-obj-marker·et-My-covenant-itkhem
m.fact("hinni_mekim_et_briti_itkhem")

# -------------------------- Gen.9.10 · EVERY_LIVING_SOUL_A_PARTY -----------
# וְאֵת כָּל־נֶפֶשׁ הַחַיָּה אֲשֶׁר אִתְּכֶם בָּעוֹף בַּבְּהֵמָה
# וּבְכָל־חַיַּת הָאָרֶץ אִתְּכֶם מִכֹּל יֹצְאֵי הַתֵּבָה לְכֹל חַיַּת
# הָאָרֶץ
# "and with every living creature that is with you, the fowl, the cattle,
# and every beast of the earth with you; of all that go out of the ark, even
# every beast of the earth."
m.step("Gen.9.10")
# ‹וְאֵת כָּל־נֶפֶשׁ הַחַיָּה אֲשֶׁר אִתְּכֶם … מִכֹּל יֹצְאֵי הַתֵּבָה›
# (“and-with all soul-of the-living which with-you … from-all goers-out-of
# the-ark”) — fact holds: and-obj-marker·et-all-soul-of-the-beast-which-
# itkhem
m.fact("ve_et_kol_nefesh_ha_chayah_asher_itkhem")

# -------------------------- Gen.9.11 · THE_CUT_VERB_BORN_REFUSING ----------
# וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתְּכֶם וְלֹא־יִכָּרֵת כָּל־בָּשָׂר עוֹד מִמֵּי
# הַמַּבּוּל וְלֹא־יִהְיֶה עוֹד מַבּוּל לְשַׁחֵת הָאָרֶץ
# "And I will establish My covenant with you; neither shall all flesh be cut
# off any more by the waters of the flood; neither shall there any more be a
# flood to destroy the earth.'"
m.step("Gen.9.11")
# ‹וַהֲקִמֹתִי אֶת־בְּרִיתִי אִתְּכֶם› (“and-I-will-establish obj-marker My-
# covenant with-you”) — fact holds: and-I-will-establish-obj-marker·et-My-
# covenant-itkhem
m.fact("va_hakimoti_et_briti_itkhem")
# ‹וְלֹא־יִכָּרֵת כָּל־בָּשָׂר עוֹד מִמֵּי הַמַּבּוּל› (“and-not be-cut-off
# all flesh still/again from-the-waters-of the-deluge”) — standing
# constraint: and-not-yikkaret-all-flesh-still/again-from-waters-of-the-
# deluge
m.invariant("ve_lo_yikkaret_kol_basar_od_mi_mei_ha_mabul")
# ‹וְלֹא־יִהְיֶה עוֹד מַבּוּל לְשַׁחֵת הָאָרֶץ› (“and-not be still/again
# deluge to-destroy the-earth”) — standing constraint: and-not-yihyeh-
# still/again-deluge-to-destroy-the-earth
m.invariant("ve_lo_yihyeh_od_mabul_le_shachet_ha_aretz")

# -------------------------- Gen.9.12 · THE_FRAME_REOPENS_ON_THE_SIGN -------
# וַיֹּאמֶר אֱלֹהִים זֹאת אוֹת־הַבְּרִית אֲשֶׁר־אֲנִי נֹתֵן בֵּינִי
# וּבֵינֵיכֶם וּבֵין כָּל־נֶפֶשׁ חַיָּה אֲשֶׁר אִתְּכֶם לְדֹרֹת עוֹלָם
# "And God said: 'This is the token of the covenant which I make between Me
# and you and every living creature that is with you, for perpetual
# generations:"
m.step("Gen.9.12")
# ‹וַיֹּאמֶר אֱלֹהִים זֹאת אוֹת־הַבְּרִית› (“and-He-said God this sign-of
# the-covenant”) — event: speak — agent God; theme this-sign-of-the-brit
m.event("speak", agent="elohim", themes=["zot_ot_ha_brit"])
# ‹אֲשֶׁר־אֲנִי נֹתֵן בֵּינִי וּבֵינֵיכֶם … לְדֹרֹת עוֹלָם› (“which I giving
# between-Me and-between-you … for-generations-of everlasting”) — fact
# holds: I-giving-beini-and-veineikhem-to-generations-of-everlasting
m.fact("ani_noten_beini_u_veineikhem_le_dorot_olam")
# witness-tier presupposed read: exemptions_written_in_the_missing_letters
# on ledorot_clause — read, not installed
m.witness_read("ledorot_clause", "exemptions_written_in_the_missing_letters",
                cites=["Bereshit Rabbah 35:2"])

# -------------------------- Gen.9.13 · MY_BOW_IN_THE_CLOUD -----------------
# אֶת־קַשְׁתִּי נָתַתִּי בֶּעָנָן וְהָיְתָה לְאוֹת בְּרִית בֵּינִי וּבֵין
# הָאָרֶץ
# "I have set My bow in the cloud, and it shall be for a token of a covenant
# between Me and the earth."
m.step("Gen.9.13")
# ‹אֶת־קַשְׁתִּי נָתַתִּי בֶּעָנָן וְהָיְתָה לְאוֹת בְּרִית› (“obj-marker
# My-bow I-have-set in-the-cloud and-be for-a-sign covenant”) — fact holds:
# obj-marker·et-qashti-I-have-set-in-cloud; and-haytah-to-sign-of-brit-
# beini-and-vein-the-earth
m.fact("et_qashti_natati_be_anan",
       "ve_haytah_le_ot_brit_beini_u_vein_ha_aretz")
# witness-tier presupposed read: placed_not_made on bow_sign — read, not
# installed
m.witness_read("bow_sign", "placed_not_made",
                cites=["Pirkei Avot 5:6", "Mekhilta DeRabbi Shimon Ben Yochai 31:6"])

# -------------------------- Gen.9.14 · THE_WEATHER_WIRED_HANDLER -----------
# וְהָיָה בְּעַנְנִי עָנָן עַל־הָאָרֶץ וְנִרְאֲתָה הַקֶּשֶׁת בֶּעָנָן
# "And it shall come to pass, when I bring clouds over the earth, and the
# bow is seen in the cloud,"
m.step("Gen.9.14")
# ‹וְהָיָה בְּעַנְנִי עָנָן … וְנִרְאֲתָה הַקֶּשֶׁת … וְזָכַרְתִּי› (“and-be
# when-I-cloud-up cloud … and-is-seen the-bow … and-mark”) — standing
# handler — if in-anni-cloud-and-nireatah-the-bow then and-I-will-remember-
# obj-marker·et-My-covenant
m.handler("be_anni_anan_ve_nireatah_ha_qeshet",
          "ve_zakharti_et_briti")

# -------------------------- Gen.9.15 · THE_REMEMBERING_PLEDGED -------------
# וְזָכַרְתִּי אֶת־בְּרִיתִי אֲשֶׁר בֵּינִי וּבֵינֵיכֶם וּבֵין כָּל־נֶפֶשׁ
# חַיָּה בְּכָל־בָּשָׂר וְלֹא־יִהְיֶה עוֹד הַמַּיִם לְמַבּוּל לְשַׁחֵת
# כָּל־בָּשָׂר
# "that I will remember My covenant, which is between Me and you and every
# living creature of all flesh; and the waters shall no more become a flood
# to destroy all flesh."
m.step("Gen.9.15")
# ‹וְזָכַרְתִּי אֶת־בְּרִיתִי … וְלֹא־יִהְיֶה עוֹד הַמַּיִם לְמַבּוּל›
# (“and-I-will-remember obj-marker My-covenant … and-not be still/again the-
# waters into-a-deluge”) — fact holds: and-I-will-remember-obj-marker·et-My-
# covenant-beini-and-veineikhem; and-not-yihyeh-still/again-the-waters-to-
# deluge
m.fact("ve_zakharti_et_briti_beini_u_veineikhem",
       "ve_lo_yihyeh_od_ha_mayim_le_mabul")
# witness-tier presupposed read: standing_law_with_disputed_scope on
# never_again_oath — read, not installed
m.witness_read("never_again_oath", "standing_law_with_disputed_scope",
                cites=["Tosefta Ta'anit 2:11", "Sifrei Devarim 343:9"])

# -------------------------- Gen.9.16 · TO_REMEMBER_THE_EVERLASTING ---------
# וְהָיְתָה הַקֶּשֶׁת בֶּעָנָן וּרְאִיתִיהָ לִזְכֹּר בְּרִית עוֹלָם בֵּין
# אֱלֹהִים וּבֵין כָּל־נֶפֶשׁ חַיָּה בְּכָל־בָּשָׂר אֲשֶׁר עַל־הָאָרֶץ
# "And the bow shall be in the cloud; and I will look upon it, that I may
# remember the everlasting covenant between God and every living creature of
# all flesh that is upon the earth.'"
m.step("Gen.9.16")
# ‹וּרְאִיתִיהָ לִזְכֹּר בְּרִית עוֹלָם בֵּין אֱלֹהִים וּבֵין כָּל־נֶפֶשׁ
# חַיָּה› (“and-I-will-see-it to-remember covenant everlasting between God
# and-between all living-soul living”) — fact holds: and-reitiha-to-me-
# zekor-brit-everlasting
m.fact("u_reitiha_li_zekor_brit_olam")

# -------------------------- Gen.9.17 · THE_SEAL_I_HAVE_ESTABLISHED ---------
# וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ זֹאת אוֹת־הַבְּרִית אֲשֶׁר הֲקִמֹתִי בֵּינִי
# וּבֵין כָּל־בָּשָׂר אֲשֶׁר עַל־הָאָרֶץ
# "And God said unto Noah: 'This is the token of the covenant which I have
# established between Me and all flesh that is upon the earth.'"
m.step("Gen.9.17")
# ‹וַיֹּאמֶר אֱלֹהִים אֶל־נֹחַ› (“and-He-said God to Noah”) — event: speak —
# agent God; theme to-Noach
m.event("speak", agent="elohim", themes=["el_noach"])
# ‹זֹאת אוֹת־הַבְּרִית אֲשֶׁר הֲקִמֹתִי› (“this sign-of the-covenant which
# I-have-established”) — fact holds: this-sign-of-the-brit-which-I-will-
# establish
m.fact("zot_ot_ha_brit_asher_hakimoti")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'banav', 'noach', 'tevah'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 3}
    assert sorted(m.WORLD["facts"]) == sorted(['hinni_mekim_et_briti_itkhem', 've_et_kol_nefesh_ha_chayah_asher_itkhem', 'va_hakimoti_et_briti_itkhem', 'ani_noten_beini_u_veineikhem_le_dorot_olam', 'et_qashti_natati_be_anan', 've_haytah_le_ot_brit_beini_u_vein_ha_aretz', 'handler: IF(be_anni_anan_ve_nireatah_ha_qeshet) THEN(ve_zakharti_et_briti)', 've_zakharti_et_briti_beini_u_veineikhem', 've_lo_yihyeh_od_ha_mayim_le_mabul', 'u_reitiha_li_zekor_brit_olam', 'zot_ot_ha_brit_asher_hakimoti'])
    assert m.WORLD["invariants"] == ['ve_lo_yikkaret_kol_basar_od_mi_mei_ha_mabul', 've_lo_yihyeh_od_mabul_le_shachet_ha_aretz']
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 4
    assert sorted(m.WORLD["witnessed"]) == ['address_widened']
    assert m.WORLD["witnessed"]['address_widened']["cites"] == ['Bereshit Rabbah 35:1']
    assert all('demotion_or_elevation' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('ledorot_clause', 'exemptions_written_in_the_missing_letters'), ('bow_sign', 'placed_not_made'), ('never_again_oath', 'standing_law_with_disputed_scope')]
    assert m.WITNESS_READS[0]["cites"] == ['Bereshit Rabbah 35:2']
    assert all('exemptions_written_in_the_missing_letters' not in f for f in m.WORLD["facts"])
    assert 'ledorot_clause' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Pirkei Avot 5:6', 'Mekhilta DeRabbi Shimon Ben Yochai 31:6']
    assert all('placed_not_made' not in f for f in m.WORLD["facts"])
    assert 'bow_sign' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ["Tosefta Ta'anit 2:11", 'Sifrei Devarim 343:9']
    assert all('standing_law_with_disputed_scope' not in f for f in m.WORLD["facts"])
    assert 'never_again_oath' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
