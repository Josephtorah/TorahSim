#!/usr/bin/env python3
# TorahSim — (c) 2026 Brian LeBlanc · MIT license (see LICENSE at repo root)
# =============================================================================
# gen_19_the_remembering — 8:1-14
# PYTHON RENDERING — GENERATED from the FROZEN YAML by render_unit_py.py.
# The YAML (logic/units/gen_19_the_remembering.yaml) is CANONICAL (Pre-
# Code); this file is a derived, runnable rendering. Do not edit —
# regenerate. The assertion block at the bottom is baked from the Stage D
# interpreter's actual final state: running this file re-proves the unit.
# Experimental model — not binding religious law.
# =============================================================================
"""The remembering: God remembers Noach, the waters go home, the earth dries (8:1-14)"""
from machine import Machine

m = Machine("gen_19_the_remembering")

# -------------------------- Gen.8.1 · THE_REMEMBERING_THE_WIND -------------
# וַיִּזְכֹּר אֱלֹהִים אֶת־נֹחַ וְאֵת כָּל־הַחַיָּה וְאֶת־כָּל־הַבְּהֵמָה
# אֲשֶׁר אִתּוֹ בַּתֵּבָה וַיַּעֲבֵר אֱלֹהִים רוּחַ עַל־הָאָרֶץ וַיָּשֹׁכּוּ
# הַמָּיִם
# "And God remembered Noah, and every living thing, and all the cattle that
# were with him in the ark; and God made a wind to pass over the earth, and
# the waters assuaged;"
m.step("Gen.8.1")
# ‹וַיִּזְכֹּר אֱלֹהִים אֶת־נֹחַ וְאֵת כָּל־הַחַיָּה וְאֶת־כָּל־הַבְּהֵמָה›
# (“and-He-remembered God obj-marker Noah obj-marker all the-beast obj-
# marker all the-livestock”) — event: remember — agent God; theme Noach,
# all-the-beast-and-the-livestock
m.event("remember", agent="elohim", themes=["noach", "kol_ha_chayah_ve_ha_behemah"])
# ‹וַיַּעֲבֵר אֱלֹהִים רוּחַ עַל־הָאָרֶץ› (“and-He-passed God wind/spirit
# over the-earth”) — event: pass — agent God; theme spirit-wind-over-the-
# earth
m.event("pass", agent="elohim", themes=["ruach_al_ha_aretz"])
# ‹וַיָּשֹׁכּוּ הַמָּיִם› (“and-they-subsided the-waters”) — event: subside
# — theme the-waters
m.event("subside", themes=["ha_mayim"])
# reads without prior install (flag, not fix): Noach, ark, waters
m.presupposed("noach", "tevah", "mayim")
# witness-tier presupposed read: waters_proven_hot_by_verbal_analogy on
# vayashoku — read, not installed
m.witness_read("vayashoku", "waters_proven_hot_by_verbal_analogy",
                cites=["Rosh Hashanah 12a:4"])
# witness-tier presupposed read: depths_judged_mountains_spared on
# remembering_scope — read, not installed
m.witness_read("remembering_scope", "depths_judged_mountains_spared",
                cites=["Bereshit Rabbah 33:1"])

# -------------------------- Gen.8.2 · THE_SHUT_MIRROR ----------------------
# וַיִּסָּכְרוּ מַעְיְנֹת תְּהוֹם וַאֲרֻבֹּת הַשָּׁמָיִם וַיִּכָּלֵא
# הַגֶּשֶׁם מִן־הַשָּׁמָיִם
# "the fountains also of the deep and the windows of heaven were stopped,
# and the rain from heaven was restrained."
m.step("Gen.8.2")
# ‹וַיִּסָּכְרוּ מַעְיְנֹת תְּהוֹם וַאֲרֻבֹּת הַשָּׁמָיִם› (“and-were-
# stopped-up fountains-of the-deep and-windows-of the-heavens”) — event:
# stop-up — theme fountains-of-deep-and-windows-of-the-heavens
m.event("stop_up", themes=["mayenot_tehom_va_arubot_ha_shamayim"])
# ‹וַיִּכָּלֵא הַגֶּשֶׁם מִן־הַשָּׁמָיִם› (“and-was-restrained the-rain from
# the-heavens”) — event: restrain — theme the-rain
m.event("restrain", themes=["ha_geshem"])

# -------------------------- Gen.8.3 · THE_WATERS_COMMUTE_BRACKET_CLOSED ----
# וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ הָלוֹךְ וָשׁוֹב וַיַּחְסְרוּ הַמַּיִם
# מִקְצֵה חֲמִשִּׁים וּמְאַת יוֹם
# "And the waters returned from off the earth continually; and after the end
# of a hundred and fifty days the waters decreased."
m.step("Gen.8.3")
# ‹וַיָּשֻׁבוּ הַמַּיִם מֵעַל הָאָרֶץ› (“and-they-returned the-waters from-
# over the-earth”) — event: return — agent the-waters
m.event("return", agent="ha_mayim")
# ‹הָלוֹךְ וָשׁוֹב … מִקְצֵה חֲמִשִּׁים וּמְאַת יוֹם› (“going and-returning
# … at-the-end-of fifty and-hundred day”) — fact holds: going-and-returning;
# from-at-the-end-of-fifty-and-hundred-day
m.fact("halokh_va_shov",
       "mi_qetze_chamishim_u_meat_yom")
# ‹וַיַּחְסְרוּ הַמַּיִם› (“and-they-diminished the-waters”) — event:
# diminish — theme the-waters
m.event("diminish", themes=["ha_mayim"])

# -------------------------- Gen.8.4 · THE_ARK_RESTS ------------------------
# וַתָּנַח הַתֵּבָה בַּחֹדֶשׁ הַשְּׁבִיעִי בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ
# עַל הָרֵי אֲרָרָט
# "And the ark rested in the seventh month, on the seventeenth day of the
# month, upon the mountains of Ararat."
m.step("Gen.8.4")
# ‹וַתָּנַח הַתֵּבָה› (“and-it-rested the-ark”) — event: rest — theme the-
# ark
m.event("rest", themes=["ha_tevah"])
# ‹בַּחֹדֶשׁ הַשְּׁבִיעִי בְּשִׁבְעָה־עָשָׂר יוֹם לַחֹדֶשׁ עַל הָרֵי
# אֲרָרָט› (“in-month the-seventh in-seven teen day of-month over mountain
# Ararat”) — fact holds: in-the-of-month-the-seventh-in-seven-teen-day;
# over-mountains-of-Ararat
m.fact("ba_chodesh_ha_shevii_be_shivah_asar_yom",
       "al_harei_ararat")

# -------------------------- Gen.8.5 · THE_TOPS_APPEAR ----------------------
# וְהַמַּיִם הָיוּ הָלוֹךְ וְחָסוֹר עַד הַחֹדֶשׁ הָעֲשִׂירִי בָּעֲשִׂירִי
# בְּאֶחָד לַחֹדֶשׁ נִרְאוּ רָאשֵׁי הֶהָרִים
# "And the waters decreased continually until the tenth month; in the tenth
# month, on the first day of the month, were the tops of the mountains
# seen."
m.step("Gen.8.5")
# ‹הָלוֹךְ וְחָסוֹר … נִרְאוּ רָאשֵׁי הֶהָרִים› (“going and-diminishing …
# were-seen the-tops-of the-mountain”) — fact holds: going-and-diminishing-
# until-the-of-month-the-tenth; in-the-tenth-in-one-were-seen-tops-of-he-
# mountains
m.fact("halokh_ve_chasor_ad_ha_chodesh_ha_asiri",
       "ba_asiri_be_echad_niru_rashei_he_harim")

# -------------------------- Gen.8.6 · THE_WINDOW_HE_MADE -------------------
# וַיְהִי מִקֵּץ אַרְבָּעִים יוֹם וַיִּפְתַּח נֹחַ אֶת־חַלּוֹן הַתֵּבָה
# אֲשֶׁר עָשָׂה
# "And it came to pass at the end of forty days, that Noah opened the window
# of the ark which he had made."
m.step("Gen.8.6")
# ‹מִקֵּץ אַרְבָּעִים יוֹם› (“at-the-end-of forty day”) — fact holds: from-
# at-the-end-of-forty-day
m.fact("mi_qetz_arbaim_yom")
# ‹וַיִּפְתַּח נֹחַ אֶת־חַלּוֹן הַתֵּבָה אֲשֶׁר עָשָׂה› (“and-he-opened Noah
# obj-marker window the-ark which he-had-made”) — event: open — agent Noach;
# theme window-the-ark
m.event("open", agent="noach", themes=["chalon_ha_tevah"])

# -------------------------- Gen.8.7 · THE_RAVEN ----------------------------
# וַיְשַׁלַּח אֶת־הָעֹרֵב וַיֵּצֵא יָצוֹא וָשׁוֹב עַד־יְבֹשֶׁת הַמַּיִם
# מֵעַל הָאָרֶץ
# "And he sent forth a raven, and it went forth to and fro, until the waters
# were dried up from off the earth."
m.step("Gen.8.7")
# ‹וַיְשַׁלַּח אֶת־הָעֹרֵב› (“and-he-sent obj-marker the-raven”) — event:
# send — agent Noach; theme the-raven
m.event("send", agent="noach", themes=["ha_orev"])
# ‹יָצוֹא וָשׁוֹב עַד־יְבֹשֶׁת הַמַּיִם› (“going-out and-returning until
# the-drying-of the-waters”) — fact holds: going-out-and-returning-until-
# drying-of-the-waters
m.fact("yatzo_va_shov_ad_yevoshet_ha_mayim")
# witness-tier presupposed read: argued_back_and_preserved_for_elijah on
# raven_dispatch — read, not installed
m.witness_read("raven_dispatch", "argued_back_and_preserved_for_elijah",
                cites=["Bereshit Rabbah 33:5", "Sanhedrin 108b:12"])

# -------------------------- Gen.8.8 · THE_DOVE_THE_QUESTION ----------------
# וַיְשַׁלַּח אֶת־הַיּוֹנָה מֵאִתּוֹ לִרְאוֹת הֲקַלּוּ הַמַּיִם מֵעַל פְּנֵי
# הָאֲדָמָה
# "And he sent forth a dove from him, to see if the waters were abated from
# off the face of the ground."
m.step("Gen.8.8")
# ‹וַיְשַׁלַּח אֶת־הַיּוֹנָה מֵאִתּוֹ› (“and-he-sent obj-marker the-dove
# from-him”) — event: send — agent Noach; theme the-dove
m.event("send", agent="noach", themes=["ha_yonah"])
# ‹לִרְאוֹת הֲקַלּוּ הַמַּיִם› (“to-see whether-they-abated the-waters”) —
# fact holds: to-me-see-the-whether-they-abated-the-waters
m.fact("li_reot_ha_qalu_ha_mayim")

# -------------------------- Gen.8.9 · NO_RESTING_PLACE_THE_HAND ------------
# וְלֹא־מָצְאָה הַיּוֹנָה מָנוֹחַ לְכַף־רַגְלָהּ וַתָּשָׁב אֵלָיו
# אֶל־הַתֵּבָה כִּי־מַיִם עַל־פְּנֵי כָל־הָאָרֶץ וַיִּשְׁלַח יָדוֹ
# וַיִּקָּחֶהָ וַיָּבֵא אֹתָהּ אֵלָיו אֶל־הַתֵּבָה
# "But the dove found no rest for the sole of her foot, and she returned
# unto him to the ark, for the waters were on the face of the whole earth;
# and he put forth his hand, and took her, and brought her in unto him into
# the ark."
m.step("Gen.8.9")
# ‹וְלֹא־מָצְאָה הַיּוֹנָה מָנוֹחַ לְכַף־רַגְלָהּ וַתָּשָׁב אֵלָיו
# אֶל־הַתֵּבָה כִּי־מַיִם עַל־פְּנֵי כָל־הָאָרֶץ› (“and-not she-found the-
# dove resting-place for-the-sole-of her-foot and-return to-him to the-ark
# that waters over face all the-earth”) — fact holds: not-found-the-dove-
# resting-place-to-sole-of-her-foot; that-waters-over-face-of-all-the-earth
m.fact("lo_matzah_ha_yonah_manoach_le_khaf_raglah",
       "ki_mayim_al_pnei_khol_ha_aretz")
# ‹וַתָּשָׁב אֵלָיו אֶל־הַתֵּבָה› (“and-return to-him to the-ark”) — event:
# return — agent the-dove
m.event("return", agent="ha_yonah")
# ‹וַיִּשְׁלַח יָדוֹ› (“and-he-sent hand-him/its”) — event: send — agent
# Noach; theme his-hand
m.event("send", agent="noach", themes=["yado"])
# ‹וַיִּקָּחֶהָ› (“and-took-her”) — event: take — agent Noach; theme the-
# dove
m.event("take", agent="noach", themes=["ha_yonah"])
# ‹וַיָּבֵא אֹתָהּ אֵלָיו אֶל־הַתֵּבָה› (“and-brought-her-in obj-marker to-
# him to the-ark”) — event: bring — agent Noach; theme the-dove
m.event("bring", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.10 · THE_FIRST_WAIT ----------------------
# וַיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים וַיֹּסֶף שַׁלַּח אֶת־הַיּוֹנָה
# מִן־הַתֵּבָה
# "And he stayed yet other seven days; and again he sent forth the dove out
# of the ark."
m.step("Gen.8.10")
# ‹וַיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים› (“and-he-waited again seven day
# other”) — event: wait — agent Noach
m.event("wait", agent="noach")
# ‹עוֹד שִׁבְעַת יָמִים אֲחֵרִים› (“again seven day other”) — fact holds:
# again-seven-day-other
m.fact("od_shivat_yamim_acherim")
# ‹וַיֹּסֶף שַׁלַּח אֶת־הַיּוֹנָה› (“and-he-again to-send obj-marker the-
# dove”) — event: send — agent Noach; theme the-dove
m.event("send", agent="noach", themes=["ha_yonah"])

# -------------------------- Gen.8.11 · THE_LEAF_AT_EVENING -----------------
# וַתָּבֹא אֵלָיו הַיּוֹנָה לְעֵת עֶרֶב וְהִנֵּה עֲלֵה־זַיִת טָרָף בְּפִיהָ
# וַיֵּדַע נֹחַ כִּי־קַלּוּ הַמַּיִם מֵעַל הָאָרֶץ
# "And the dove came in to him at eventide; and lo in her mouth an olive-
# leaf freshly plucked; so Noah knew that the waters were abated from off
# the earth."
m.step("Gen.8.11")
# ‹וַתָּבֹא אֵלָיו הַיּוֹנָה לְעֵת עֶרֶב› (“and-come/bring to-him the-dove
# at-the-time-of evening”) — event: come — agent the-dove; theme to-obj-
# marker·et-evening
m.event("come", agent="ha_yonah", themes=["le_et_erev"])
# ‹וְהִנֵּה עֲלֵה־זַיִת טָרָף בְּפִיהָ› (“and-behold leaf olive freshly-
# plucked in-her-mouth”) — fact holds: leaf-olive-freshly-plucked-in-her-
# mouth
m.fact("aleh_zayit_taraf_be_fiha")
# ‹וַיֵּדַע נֹחַ כִּי־קַלּוּ הַמַּיִם› (“and-he-knew Noah that abated the-
# waters”) — event: know — agent Noach; theme that-whether-they-abated-the-
# waters
m.event("know", agent="noach", themes=["ki_qalu_ha_mayim"])
# witness-grounded state (its own tier): killed_or_sustenance on taraf_verb
m.witness_state("taraf_verb", "killed_or_sustenance",
                cites=["Bereshit Rabbah 33:6", "Sanhedrin 108b:17"])

# -------------------------- Gen.8.12 · THE_SECOND_WAIT_THE_LAST_OD ---------
# וַיִּיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים וַיְשַׁלַּח אֶת־הַיּוֹנָה
# וְלֹא־יָסְפָה שׁוּב־אֵלָיו עוֹד
# "And he stayed yet other seven days; and sent forth the dove; and she
# returned not again unto him any more."
m.step("Gen.8.12")
# ‹וַיִּיָּחֶל עוֹד שִׁבְעַת יָמִים אֲחֵרִים› (“and-he-waited again seven
# day other”) — event: wait — agent Noach
m.event("wait", agent="noach")
# ‹וַיְשַׁלַּח אֶת־הַיּוֹנָה› (“and-he-sent obj-marker the-dove”) — event:
# send — agent Noach; theme the-dove
m.event("send", agent="noach", themes=["ha_yonah"])
# ‹וְלֹא־יָסְפָה שׁוּב־אֵלָיו עוֹד› (“and-not added to-return to-him again”)
# — fact holds: and-not-did-again-return-to-him-again
m.fact("ve_lo_yasfah_shuv_elav_od")

# -------------------------- Gen.8.13 · NEW_YEARS_DAY_THE_COVER_OFF ---------
# וַיְהִי בְּאַחַת וְשֵׁשׁ־מֵאוֹת שָׁנָה בָּרִאשׁוֹן בְּאֶחָד לַחֹדֶשׁ
# חָרְבוּ הַמַּיִם מֵעַל הָאָרֶץ וַיָּסַר נֹחַ אֶת־מִכְסֵה הַתֵּבָה וַיַּרְא
# וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה
# "And it came to pass in the six hundred and first year, in the first
# month, the first day of the month, the waters were dried up from off the
# earth; and Noah removed the covering of the ark, and looked, and behold,
# the face of the ground was dried."
m.step("Gen.8.13")
# ‹בְּאַחַת וְשֵׁשׁ־מֵאוֹת שָׁנָה בָּרִאשׁוֹן בְּאֶחָד לַחֹדֶשׁ› (“in-one
# and-six hundred year in-the-first-month in-one of-month”) — clock
# anchored: t0 := year-of-601-of-month-1-day-1
m.time_anchor("shnat_601_chodesh_1_yom_1")
# ‹חָרְבוּ הַמַּיִם מֵעַל הָאָרֶץ› (“were-parched the-waters from-over the-
# earth”) — fact holds: were-parched-the-waters-from-over-the-earth
m.fact("charvu_ha_mayim_me_al_ha_aretz")
# ‹וַיָּסַר נֹחַ אֶת־מִכְסֵה הַתֵּבָה› (“and-he-removed Noah obj-marker
# covering the-ark”) — event: remove — agent Noach; theme covering-the-ark
m.event("remove", agent="noach", themes=["mikhseh_ha_tevah"])
# ‹וַיַּרְא וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה› (“and-he-saw and-behold were-
# parched face the-ground”) — event: see — agent Noach; theme face-of-the-
# ground
m.event("see", agent="noach", themes=["pnei_ha_adamah"])
# ‹וְהִנֵּה חָרְבוּ פְּנֵי הָאֲדָמָה› (“and-behold were-parched face the-
# ground”) — fact holds: and-behold-were-parched-face-of-the-ground
m.fact("ve_hinneh_charvu_pnei_ha_adamah")
# witness-tier presupposed read: one_day_counts_as_a_year on date_formula —
# read, not installed
m.witness_read("date_formula", "one_day_counts_as_a_year",
                cites=["Rosh Hashanah 10b:6", "Jerusalem Talmud Rosh Hashanah 1:1:3", "Tosefta Rosh Hashanah (Lieberman) 1:3"])

# -------------------------- Gen.8.14 · THE_EARTH_DRY -----------------------
# וּבַחֹדֶשׁ הַשֵּׁנִי בְּשִׁבְעָה וְעֶשְׂרִים יוֹם לַחֹדֶשׁ יָבְשָׁה
# הָאָרֶץ
# "And in the second month, on the seven and twentieth day of the month, was
# the earth dry."
m.step("Gen.8.14")
# ‹בְּשִׁבְעָה וְעֶשְׂרִים יוֹם לַחֹדֶשׁ יָבְשָׁה הָאָרֶץ› (“in-seven and-
# twenty day of-month was-dry the-earth”) — fact holds: in-the-of-month-the-
# second-in-seven-and-twenty-day; was-dry-the-earth
m.fact("ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom",
       "yavshah_ha_aretz")

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
    assert sorted(m.WORLD["facts"]) == sorted(['halokh_va_shov', 'mi_qetze_chamishim_u_meat_yom', 'ba_chodesh_ha_shevii_be_shivah_asar_yom', 'al_harei_ararat', 'halokh_ve_chasor_ad_ha_chodesh_ha_asiri', 'ba_asiri_be_echad_niru_rashei_he_harim', 'mi_qetz_arbaim_yom', 'yatzo_va_shov_ad_yevoshet_ha_mayim', 'li_reot_ha_qalu_ha_mayim', 'lo_matzah_ha_yonah_manoach_le_khaf_raglah', 'ki_mayim_al_pnei_khol_ha_aretz', 'od_shivat_yamim_acherim', 'aleh_zayit_taraf_be_fiha', 've_lo_yasfah_shuv_elav_od', 'charvu_ha_mayim_me_al_ha_aretz', 've_hinneh_charvu_pnei_ha_adamah', 'ba_chodesh_ha_sheni_be_shivah_ve_esrim_yom', 'yavshah_ha_aretz'])
    assert m.WORLD["invariants"] == []
    assert m.WORLD["partitions"] == []
    assert len(m.EVENTS) == 23
    assert sorted(m.WORLD["witnessed"]) == ['taraf_verb']
    assert m.WORLD["witnessed"]['taraf_verb']["cites"] == ['Bereshit Rabbah 33:6', 'Sanhedrin 108b:17']
    assert all('killed_or_sustenance' not in f for f in m.WORLD["facts"])
    assert [(w["entity"], w["state"]) for w in m.WITNESS_READS] == [('vayashoku', 'waters_proven_hot_by_verbal_analogy'), ('remembering_scope', 'depths_judged_mountains_spared'), ('raven_dispatch', 'argued_back_and_preserved_for_elijah'), ('date_formula', 'one_day_counts_as_a_year')]
    assert m.WITNESS_READS[0]["cites"] == ['Rosh Hashanah 12a:4']
    assert all('waters_proven_hot_by_verbal_analogy' not in f for f in m.WORLD["facts"])
    assert 'vayashoku' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[1]["cites"] == ['Bereshit Rabbah 33:1']
    assert all('depths_judged_mountains_spared' not in f for f in m.WORLD["facts"])
    assert 'remembering_scope' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[2]["cites"] == ['Bereshit Rabbah 33:5', 'Sanhedrin 108b:12']
    assert all('argued_back_and_preserved_for_elijah' not in f for f in m.WORLD["facts"])
    assert 'raven_dispatch' not in m.WORLD["witnessed"]
    assert m.WITNESS_READS[3]["cites"] == ['Rosh Hashanah 10b:6', 'Jerusalem Talmud Rosh Hashanah 1:1:3', 'Tosefta Rosh Hashanah (Lieberman) 1:3']
    assert all('one_day_counts_as_a_year' not in f for f in m.WORLD["facts"])
    assert 'date_formula' not in m.WORLD["witnessed"]
    print("ALL ASSERTIONS GREEN — rendering matches the frozen unit's machine truth")
