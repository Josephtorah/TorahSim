#!/usr/bin/env python3
# =============================================================================
# lev_13_intake_quarantine — 13:1-8
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/lev_13_intake_quarantine.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The skin-mark intake: case, handlers, quarantine loop (Lev 13:1-8) — first law unit"""
from machine import Machine

m = Machine("lev_13_intake_quarantine")

# -------------------------- Lev.13.1 · FRAME_SPEECH ------------------------
# ‹וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה› (“and-spoke the-LORD to Moses”)
# ‹וְאֶל־אַהֲרֹן לֵאמֹר› (“and-to Aaron saying”)
# "And the LORD spoke unto Moses and unto Aaron, saying:"
m.step("Lev.13.1")
# ‹וַיְדַבֵּר יְהוָה› (“and-spoke the-LORD”)
# — event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# reads without prior install (flag, not fix): Moses, Aaron
m.presupposed("moshe", "aharon")

# -------------------------- Lev.13.2 · CASE_INTAKE -------------------------
# ‹אָדָם כִּי־יִהְיֶה בְעוֹר־בְּשָׂרוֹ› (“human when there-is in-skin-of
# his-flesh”)
# ‹שְׂאֵת אוֹ־סַפַּחַת אוֹ› (“swelling or scab or”)
# ‹בַהֶרֶת וְהָיָה בְעוֹר־בְּשָׂרוֹ› (“bright-spot and-it-becomes in-skin-of
# his-flesh”)
# ‹לְנֶגַע צָרָעַת וְהוּבָא› (“into-a-mark-of tzara'at and-he-shall-be-
# brought”)
# ‹אֶל־אַהֲרֹן הַכֹּהֵן אוֹ› (“to Aaron the-priest or”)
# ‹אֶל־אַחַד מִבָּנָיו הַכֹּהֲנִים› (“to one of-his-sons the-priests”)
# "When a man shall have in the skin of his flesh a rising, or a scab, or a
# bright spot, and it become in the skin of his flesh the plague of leprosy,
# then he shall be brought unto Aaron the priest, or unto one of his sons
# the priests."
m.step("Lev.13.2")
# ‹אָדָם כִּי־יִהְיֶה … וְהוּבָא› (“human when there-is … and-he-shall-be-
# brought”)
# ‹אֶל־אַהֲרֹן הַכֹּהֵן› (“to Aaron the-priest”)
# — case human, mark-in-skin-of-flesh(Most-High-or-scab-or-bright-spot) ->
# the-disease-mark routes to hova-to-the-priest
m.case("adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat", "hova_el_ha_kohen")
# reads without prior install (flag, not fix): human, skin-of-flesh, the-
# priest
m.presupposed("adam", "or_basar", "ha_kohen")
# witness-tier presupposed read: the_declaration_protocol on el_hakohen —
# read, not installed
m.witness_read("el_hakohen", "the_declaration_protocol",
                cites=["Sifra, Tazria Parashat Nega'im, Section 1 8", "Sifra, Tazria Parashat Nega'im, Section 1 9", "Sifra, Tazria Parashat Nega'im, Section 1 10"])

# -------------------------- Lev.13.3 · HANDLER_VERDICT_TAMEI ---------------
# ‹וְרָאָה הַכֹּהֵן אֶת־הַנֶּגַע› (“and-he-shall-see the-priest obj-marker
# the-mark”)
# ‹בְּעוֹר־הַבָּשָׂר וְשֵׂעָר בַּנֶּגַע› (“in-skin-of the-flesh and-hair in-
# the-mark”)
# ‹הָפַךְ לָבָן וּמַרְאֵה› (“has-turned white and-appearance-of”)
# ‹הַנֶּגַע עָמֹק מֵעוֹר› (“the-mark deeper than-skin-of”)
# ‹בְּשָׂרוֹ נֶגַע צָרַעַת› (“his-flesh mark-of tzara'at”)
# ‹הוּא וְרָאָהוּ הַכֹּהֵן› (“it-is and-he-shall-see-him the-priest”)
# ‹וְטִמֵּא אֹתוֹ› (“and-he-shall-declare-impure him”)
# "And the priest shall look upon the plague in the skin of the flesh; and
# if the hair in the plague be turned white, and the appearance of the
# plague be deeper than the skin of his flesh, it is the plague of leprosy;
# and the priest shall look on him, and pronounce him unclean."
m.step("Lev.13.3")
# ‹וְשֵׂעָר … הָפַךְ לָבָן› (“and-hair … has-turned white”)
# ‹וּמַרְאֵה … עָמֹק … וְטִמֵּא› (“and-appearance-of … deeper … and-he-
# shall-declare-impure”)
# ‹אֹתוֹ› (“him”)
# — standing handler — if hair-has-turned-white ∧ appearance-deeper-from-
# skin-of then classify(into-a-mark-of-leprosy-it-is) ∧ he-shall-declare-
# impure(status-impure)
m.handler("sear_hafakh_lavan ∧ mareh_amok_me_or",
          "classify(nega_tzaraat_hu) ∧ timme(status_tamei)")
# witness-tier presupposed read: the_calibration_layer on vera_ah_hakohen —
# read, not installed
m.witness_read("vera_ah_hakohen", "the_calibration_layer",
                cites=["Sifra, Tazria Parashat Nega'im, Section 1 4", "Sifra, Tazria Parashat Nega'im, Section 1 5", "Sifra, Tazria Parashat Nega'im, Section 2 6", "Sifra, Tazria Parashat Nega'im, Chapter 2* 2", "Sifra, Tazria Parashat Nega'im, Chapter 2* 3"])

# -------------------------- Lev.13.4 · HANDLER_CONFINE_FIRST ---------------
# ‹וְאִם־בַּהֶרֶת לְבָנָה הִוא› (“and-if bright-spot white it-is”)
# ‹בְּעוֹר בְּשָׂרוֹ וְעָמֹק› (“in-skin-of his-flesh and-deeper”)
# ‹אֵין־מַרְאֶהָ מִן־הָעוֹר וּשְׂעָרָה› (“is-not its-appearance than the-
# skin and-its-hair”)
# ‹לֹא־הָפַךְ לָבָן וְהִסְגִּיר› (“not has-turned white and-he-shall-
# confine”)
# ‹הַכֹּהֵן אֶת־הַנֶּגַע שִׁבְעַת› (“the-priest obj-marker the-mark seven-
# of”)
# ‹יָמִים› (“days”)
# "And if the bright spot be white in the skin of his flesh, and the
# appearance thereof be not deeper than the skin, and the hair thereof be
# not turned white, then the priest shall shut up him that hath the plague
# seven days."
m.step("Lev.13.4")
# ‹וְאִם … אֵין … לֹא› (“and-if … is-not … not”)
# ‹… וְהִסְגִּיר … שִׁבְעַת יָמִים› (“and-he-shall-confine … seven-of days”)
# — standing handler — if bright-spot-white ∧ is-not-deeper-its-appearance ∧
# not-has-turned-white then he-shall-confine(obj-marker-the-into-a-mark-of,
# seven-of-days)
m.handler("baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan",
          "hisgir(et_ha_nega, shivat_yamim)")
# witness-tier presupposed read: order_and_doubt on vesear_lo_hafach — read,
# not installed
m.witness_read("vesear_lo_hafach", "order_and_doubt",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 2 2", "Sifra, Tazria Parashat Nega'im, Chapter 2 3", "Sifra, Tazria Parashat Nega'im, Section 2 9"])

# -------------------------- Lev.13.5 · HANDLER_RECHECK_CONFINE_SECOND ------
# ‹וְרָאָהוּ הַכֹּהֵן בַּיּוֹם› (“and-he-shall-see-him the-priest on-the-
# day”)
# ‹הַשְּׁבִיעִי וְהִנֵּה הַנֶּגַע› (“the-seventh and-behold the-mark”)
# ‹עָמַד בְּעֵינָיו לֹא־פָשָׂה› (“has-stood in-its-appearance not has-
# spread”)
# ‹הַנֶּגַע בָּעוֹר וְהִסְגִּירוֹ› (“the-mark in-the-skin and-he-shall-
# confine-him”)
# ‹הַכֹּהֵן שִׁבְעַת יָמִים› (“the-priest seven-of days”)
# ‹שֵׁנִית› (“a-second-time”)
# "And the priest shall look on him the seventh day; and, behold, if the
# plague stay in its appearance, and the plague be not spread in the skin,
# then the priest shall shut him up seven days more."
m.step("Lev.13.5")
# ‹בַּיּוֹם הַשְּׁבִיעִי וְהִנֵּה› (“on-the-day the-seventh and-behold”)
# ‹… עָמַד … לֹא־פָשָׂה … שֵׁנִית› (“has-stood … not has-spread … a-second-
# time”)
# — standing handler — if in-the-day-the-seventh ∧ has-stood-in-its-
# appearance ∧ not-has-spread then he-shall-confine-him(seven-of-days-a-
# second-time)
m.handler("ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah",
          "hisgiro(shivat_yamim_shenit)")
# witness-tier presupposed read: shared_seventh_idempotence on bayom_hashvii
# — read, not installed
m.witness_read("bayom_hashvii", "shared_seventh_idempotence",
                cites=["Sifra, Tazria Parashat Nega'im, Chapter 2* 4", "Sifra, Tazria Parashat Nega'im, Chapter 2* 5", "Sifra, Tazria Parashat Nega'im, Chapter 2* 6", "Sifra, Tazria Parashat Nega'im, Chapter 2* 7"])

# -------------------------- Lev.13.6 · HANDLER_RELEASE ---------------------
# ‹וְרָאָה הַכֹּהֵן אֹתוֹ› (“and-he-shall-see the-priest him”)
# ‹בַּיּוֹם הַשְּׁבִיעִי שֵׁנִית› (“on-the-day the-seventh a-second-time”)
# ‹וְהִנֵּה כֵּהָה הַנֶּגַע› (“and-behold has-dimmed the-mark”)
# ‹וְלֹא־פָשָׂה הַנֶּגַע בָּעוֹר› (“and-not has-spread the-mark in-the-
# skin”)
# ‹וְטִהֲרוֹ הַכֹּהֵן מִסְפַּחַת› (“and-he-shall-declare-him-pure the-priest
# scab”)
# ‹הִיא וְכִבֶּס בְּגָדָיו› (“it-is and-he-shall-wash his-garments”)
# ‹וְטָהֵר› (“and-he-is-pure”)
# "And the priest shall look on him again the seventh day; and, behold, if
# the plague be dim, and the plague be not spread in the skin, then the
# priest shall pronounce him clean: it is a scab; and he shall wash his
# clothes, and be clean."
m.step("Lev.13.6")
# ‹כֵּהָה … וְטִהֲרוֹ … מִסְפַּחַת› (“has-dimmed … and-he-shall-declare-him-
# pure … scab”)
# ‹הִיא וְכִבֶּס בְּגָדָיו› (“it-is and-he-shall-wash his-garments”)
# ‹וְטָהֵר› (“and-he-is-pure”)
# — standing handler — if in-the-day-the-seventh-a-second-time ∧ has-dimmed
# ∧ not-has-spread then he-shall-declare-him-pure(status-pure) ∧
# classify(scab-it-is) ∧ wash-his-garments ∧ he-is-pure
m.handler("ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah",
          "tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher")

# -------------------------- Lev.13.7 · HANDLER_REOPEN_TRIGGER --------------
# ‹וְאִם־פָּשֹׂה תִפְשֶׂה הַמִּסְפַּחַת› (“and-if spread it-spreads the-
# scab”)
# ‹בָּעוֹר אַחֲרֵי הֵרָאֹתוֹ› (“in-the-skin after his-being-seen”)
# ‹אֶל־הַכֹּהֵן לְטָהֳרָתוֹ וְנִרְאָה› (“to the-priest for-his-purification
# and-he-shall-be-seen”)
# ‹שֵׁנִית אֶל־הַכֹּהֵן› (“a-second-time to the-priest”)
# "But if the scab spread abroad in the skin, after that he hath shown
# himself to the priest for his cleansing, he shall show himself to the
# priest again."
m.step("Lev.13.7")
# ‹פָּשֹׂה תִפְשֶׂה … אַחֲרֵי› (“spread it-spreads … after”)
# ‹הֵרָאֹתוֹ … וְנִרְאָה שֵׁנִית› (“his-being-seen … and-he-shall-be-seen
# a-second-time”)
# — standing handler — if spread-it-spreads(after-its-appearing-to-his-
# purification) then seen-a-second-time-to-the-priest
m.handler("pasoh_tifseh(acharei_heraoto_le_tohorato)",
          "nirah_shenit_el_ha_kohen")

# -------------------------- Lev.13.8 · HANDLER_REOPEN_VERDICT --------------
# ‹וְרָאָה הַכֹּהֵן וְהִנֵּה› (“and-he-shall-see the-priest and-behold”)
# ‹פָּשְׂתָה הַמִּסְפַּחַת בָּעוֹר› (“has-spread the-scab in-the-skin”)
# ‹וְטִמְּאוֹ הַכֹּהֵן צָרַעַת› (“and-he-shall-declare-him-impure the-priest
# tzara'at”)
# ‹הִוא› (“it-is”)
# "And the priest shall look, and, behold, the scab is spread in the skin;
# then the priest shall pronounce him unclean: it is leprosy."
m.step("Lev.13.8")
# ‹וְהִנֵּה פָּשְׂתָה … וְטִמְּאוֹ› (“and-behold has-spread … and-he-shall-
# declare-him-impure”)
# ‹… צָרַעַת הִוא› (“tzara'at it-is”)
# — standing handler — if behold-has-spread-the-scab then pronounce-
# impure(status-impure) ∧ classify(leprosy-it-is)
m.handler("hineh_pastah_ha_mispachat",
          "timmeo(status_tamei) ∧ classify(tzaraat_hi)")

# -------------------------- machine truth (baked from the Stage D run) -------
if __name__ == "__main__":
    m.report()
    assert m.created_set() == set()
    assert m.presupposed_set() == {'adam', 'aharon', 'ha_kohen', 'moshe', 'or_basar'}
    assert m.REGISTRY["names"] == {}
    assert m.REGISTRY["writes"] == 0
    assert m.tests_list() == []
    assert m.open_demands() == []
    assert len(m.SPECS["log"]) == 0
    assert sorted(m.LEDGER) == []
    assert m.flag_counts() == {'read_before_install': 5}
    assert sorted(m.WORLD["facts"]) == sorted(['case: adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat -> hova_el_ha_kohen', 'handler: IF(sear_hafakh_lavan ∧ mareh_amok_me_or) THEN(classify(nega_tzaraat_hu) ∧ timme(status_tamei))', 'handler: IF(baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan) THEN(hisgir(et_ha_nega, shivat_yamim))', 'handler: IF(ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah) THEN(hisgiro(shivat_yamim_shenit))', 'handler: IF(ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah) THEN(tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher)', 'handler: IF(pasoh_tifseh(acharei_heraoto_le_tohorato)) THEN(nirah_shenit_el_ha_kohen)', 'handler: IF(hineh_pastah_ha_mispachat) THEN(timmeo(status_tamei) ∧ classify(tzaraat_hi))'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 8
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('el_hakohen', 'the_declaration_protocol'), ('vera_ah_hakohen', 'the_calibration_layer'), ('vesear_lo_hafach', 'order_and_doubt'), ('bayom_hashvii', 'shared_seventh_idempotence')]
    assert m.WITNESS_READS[0]["cites"] == ["Sifra, Tazria Parashat Nega'im, Section 1 8", "Sifra, Tazria Parashat Nega'im, Section 1 9", "Sifra, Tazria Parashat Nega'im, Section 1 10"]
    assert all('the_declaration_protocol' not in f for f in m.WORLD["facts"])
    assert 'el_hakohen' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ["Sifra, Tazria Parashat Nega'im, Section 1 4", "Sifra, Tazria Parashat Nega'im, Section 1 5", "Sifra, Tazria Parashat Nega'im, Section 2 6", "Sifra, Tazria Parashat Nega'im, Chapter 2* 2", "Sifra, Tazria Parashat Nega'im, Chapter 2* 3"]
    assert all('the_calibration_layer' not in f for f in m.WORLD["facts"])
    assert 'vera_ah_hakohen' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 2 2", "Sifra, Tazria Parashat Nega'im, Chapter 2 3", "Sifra, Tazria Parashat Nega'im, Section 2 9"]
    assert all('order_and_doubt' not in f for f in m.WORLD["facts"])
    assert 'vesear_lo_hafach' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ["Sifra, Tazria Parashat Nega'im, Chapter 2* 4", "Sifra, Tazria Parashat Nega'im, Chapter 2* 5", "Sifra, Tazria Parashat Nega'im, Chapter 2* 6", "Sifra, Tazria Parashat Nega'im, Chapter 2* 7"]
    assert all('shared_seventh_idempotence' not in f for f in m.WORLD["facts"])
    assert 'bayom_hashvii' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
