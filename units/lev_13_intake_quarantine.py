#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
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
# וַיְדַבֵּר יְהוָה אֶל־מֹשֶׁה וְאֶל־אַהֲרֹן לֵאמֹר
# "And the LORD spoke unto Moses and unto Aaron, saying:"
m.step("Lev.13.1")
# ‹וַיְדַבֵּר יְהוָה› (“and-spoke the-LORD”) — event: speak — agent the-LORD
m.event("speak", agent="YHWH")
# reads without prior install (flag, not fix): Moses, Aaron
m.presupposed("moshe", "aharon")

# -------------------------- Lev.13.2 · CASE_INTAKE -------------------------
# אָדָם כִּי־יִהְיֶה בְעוֹר־בְּשָׂרוֹ שְׂאֵת אוֹ־סַפַּחַת אוֹ בַהֶרֶת
# וְהָיָה בְעוֹר־בְּשָׂרוֹ לְנֶגַע צָרָעַת וְהוּבָא אֶל־אַהֲרֹן הַכֹּהֵן אוֹ
# אֶל־אַחַד מִבָּנָיו הַכֹּהֲנִים
# "When a man shall have in the skin of his flesh a rising, or a scab, or a
# bright spot, and it become in the skin of his flesh the plague of leprosy,
# then he shall be brought unto Aaron the priest, or unto one of his sons
# the priests."
m.step("Lev.13.2")
# ‹אָדָם כִּי־יִהְיֶה … וְהוּבָא אֶל־אַהֲרֹן הַכֹּהֵן› (“human when there-is
# … and-he-shall-be-brought to Aaron the-priest”) — case human, mark-in-
# skin-of-flesh(Most-High-or-scab-or-bright-spot) -> the-disease-mark routes
# to hova-to-the-priest
m.case("adam, mark_in_or_basar(seet_o_sapachat_o_baheret) -> nega_tzaraat", "hova_el_ha_kohen")
# reads without prior install (flag, not fix): human, skin-of-flesh, the-
# priest
m.presupposed("adam", "or_basar", "ha_kohen")

# -------------------------- Lev.13.3 · HANDLER_VERDICT_TAMEI ---------------
# וְרָאָה הַכֹּהֵן אֶת־הַנֶּגַע בְּעוֹר־הַבָּשָׂר וְשֵׂעָר בַּנֶּגַע הָפַךְ
# לָבָן וּמַרְאֵה הַנֶּגַע עָמֹק מֵעוֹר בְּשָׂרוֹ נֶגַע צָרַעַת הוּא
# וְרָאָהוּ הַכֹּהֵן וְטִמֵּא אֹתוֹ
# "And the priest shall look upon the plague in the skin of the flesh; and
# if the hair in the plague be turned white, and the appearance of the
# plague be deeper than the skin of his flesh, it is the plague of leprosy;
# and the priest shall look on him, and pronounce him unclean."
m.step("Lev.13.3")
# ‹וְשֵׂעָר … הָפַךְ לָבָן וּמַרְאֵה … עָמֹק … וְטִמֵּא אֹתוֹ› (“and-hair …
# has-turned white and-appearance-of … deeper … and-he-shall-declare-impure
# him”) — standing handler — if hair-has-turned-white ∧ appearance-deeper-
# from-skin-of then classify(into-a-mark-of-leprosy-it-is) ∧ he-shall-
# declare-impure(status-impure)
m.handler("sear_hafakh_lavan ∧ mareh_amok_me_or",
          "classify(nega_tzaraat_hu) ∧ timme(status_tamei)")

# -------------------------- Lev.13.4 · HANDLER_CONFINE_FIRST ---------------
# וְאִם־בַּהֶרֶת לְבָנָה הִוא בְּעוֹר בְּשָׂרוֹ וְעָמֹק אֵין־מַרְאֶהָ
# מִן־הָעוֹר וּשְׂעָרָה לֹא־הָפַךְ לָבָן וְהִסְגִּיר הַכֹּהֵן אֶת־הַנֶּגַע
# שִׁבְעַת יָמִים
# "And if the bright spot be white in the skin of his flesh, and the
# appearance thereof be not deeper than the skin, and the hair thereof be
# not turned white, then the priest shall shut up him that hath the plague
# seven days."
m.step("Lev.13.4")
# ‹וְאִם … אֵין … לֹא … וְהִסְגִּיר … שִׁבְעַת יָמִים› (“and-if … is-not …
# not … and-he-shall-confine … seven-of days”) — standing handler — if
# bright-spot-white ∧ is-not-deeper-its-appearance ∧ not-has-turned-white
# then he-shall-confine(obj-marker-the-into-a-mark-of, seven-of-days)
m.handler("baheret_levanah ∧ ein_amok_mareha ∧ lo_hafakh_lavan",
          "hisgir(et_ha_nega, shivat_yamim)")

# -------------------------- Lev.13.5 · HANDLER_RECHECK_CONFINE_SECOND ------
# וְרָאָהוּ הַכֹּהֵן בַּיּוֹם הַשְּׁבִיעִי וְהִנֵּה הַנֶּגַע עָמַד
# בְּעֵינָיו לֹא־פָשָׂה הַנֶּגַע בָּעוֹר וְהִסְגִּירוֹ הַכֹּהֵן שִׁבְעַת
# יָמִים שֵׁנִית
# "And the priest shall look on him the seventh day; and, behold, if the
# plague stay in its appearance, and the plague be not spread in the skin,
# then the priest shall shut him up seven days more."
m.step("Lev.13.5")
# ‹בַּיּוֹם הַשְּׁבִיעִי וְהִנֵּה … עָמַד … לֹא־פָשָׂה … שֵׁנִית› (“on-the-
# day the-seventh and-behold … has-stood … not has-spread … a-second-time”)
# — standing handler — if in-the-day-the-seventh ∧ has-stood-in-its-
# appearance ∧ not-has-spread then he-shall-confine-him(seven-of-days-a-
# second-time)
m.handler("ba_yom_ha_shevii ∧ amad_be_einav ∧ lo_fasah",
          "hisgiro(shivat_yamim_shenit)")

# -------------------------- Lev.13.6 · HANDLER_RELEASE ---------------------
# וְרָאָה הַכֹּהֵן אֹתוֹ בַּיּוֹם הַשְּׁבִיעִי שֵׁנִית וְהִנֵּה כֵּהָה
# הַנֶּגַע וְלֹא־פָשָׂה הַנֶּגַע בָּעוֹר וְטִהֲרוֹ הַכֹּהֵן מִסְפַּחַת הִיא
# וְכִבֶּס בְּגָדָיו וְטָהֵר
# "And the priest shall look on him again the seventh day; and, behold, if
# the plague be dim, and the plague be not spread in the skin, then the
# priest shall pronounce him clean: it is a scab; and he shall wash his
# clothes, and be clean."
m.step("Lev.13.6")
# ‹כֵּהָה … וְטִהֲרוֹ … מִסְפַּחַת הִיא וְכִבֶּס בְּגָדָיו וְטָהֵר› (“has-
# dimmed … and-he-shall-declare-him-pure … scab it-is and-he-shall-wash his-
# garments and-he-is-pure”) — standing handler — if in-the-day-the-seventh-
# a-second-time ∧ has-dimmed ∧ not-has-spread then he-shall-declare-him-
# pure(status-pure) ∧ classify(scab-it-is) ∧ wash-his-garments ∧ he-is-pure
m.handler("ba_yom_ha_shevii_shenit ∧ kehah ∧ lo_fasah",
          "tiharo(status_tahor) ∧ classify(mispachat_hi) ∧ kibbes_begadav ∧ taher")

# -------------------------- Lev.13.7 · HANDLER_REOPEN_TRIGGER --------------
# וְאִם־פָּשֹׂה תִפְשֶׂה הַמִּסְפַּחַת בָּעוֹר אַחֲרֵי הֵרָאֹתוֹ
# אֶל־הַכֹּהֵן לְטָהֳרָתוֹ וְנִרְאָה שֵׁנִית אֶל־הַכֹּהֵן
# "But if the scab spread abroad in the skin, after that he hath shown
# himself to the priest for his cleansing, he shall show himself to the
# priest again."
m.step("Lev.13.7")
# ‹פָּשֹׂה תִפְשֶׂה … אַחֲרֵי הֵרָאֹתוֹ … וְנִרְאָה שֵׁנִית› (“spread it-
# spreads … after his-being-seen … and-he-shall-be-seen a-second-time”) —
# standing handler — if spread-it-spreads(after-its-appearing-to-his-
# purification) then seen-a-second-time-to-the-priest
m.handler("pasoh_tifseh(acharei_heraoto_le_tohorato)",
          "nirah_shenit_el_ha_kohen")

# -------------------------- Lev.13.8 · HANDLER_REOPEN_VERDICT --------------
# וְרָאָה הַכֹּהֵן וְהִנֵּה פָּשְׂתָה הַמִּסְפַּחַת בָּעוֹר וְטִמְּאוֹ
# הַכֹּהֵן צָרַעַת הִוא
# "And the priest shall look, and, behold, the scab is spread in the skin;
# then the priest shall pronounce him unclean: it is leprosy."
m.step("Lev.13.8")
# ‹וְהִנֵּה פָּשְׂתָה … וְטִמְּאוֹ … צָרַעַת הִוא› (“and-behold has-spread …
# and-he-shall-declare-him-impure … tzara'at it-is”) — standing handler — if
# behold-has-spread-the-scab then pronounce-impure(status-impure) ∧
# classify(leprosy-it-is)
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
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
